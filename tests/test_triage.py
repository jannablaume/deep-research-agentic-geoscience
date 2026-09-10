"""triage.py's scoring battery — the part of the pipeline that has been wrong twice.

`decisions.md` records both regressions: a case-insensitive `ReAct` that produced 377
false positives in a 1795-record corpus, and a structural `scope: none` filter that
discarded 190 records the harvest existed to find. Neither was visible in any count;
both were found by reading a sample by hand. These tests are the cheap version of
that reading.

A record's fate is an AND of four conditions — score, strong hits, LLM vocabulary
present, and a domain group identified — so each is pinned separately. A test that
only checked the score would have missed both regressions.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

import triage


def s(title: str, abstract: str = "") -> triage.Row:
    return triage.score({"title": title, "abstract": abstract})


class TestLlmCorroboration:
    def test_generic_agent_terms_alone_score_nothing(self) -> None:
        # "multi-agent system" is forty years old. Without independent LLM vocabulary
        # it must not promote 1990s work into an LLM-era shortlist.
        r = s("A Multi-Agent System for Seismic Interpretation")
        assert r["llm_present"] == "no"
        assert r["strong_hits"] == 0
        assert r["agentic_score"] == 0

    def test_generic_agent_terms_count_once_llm_vocabulary_is_present(self) -> None:
        r = s("A Multi-Agent System for Seismic Interpretation", "We use a large language model.")
        assert r["llm_present"] == "yes"
        assert r["strong_hits"] == 1

    def test_agent_llm_vocabulary_is_self_sufficient(self) -> None:
        # "agentic" only appears in LLM-agent work, so it establishes the era itself.
        r = s("An agentic AI approach to geoscience data")
        assert r["llm_present"] == "yes"
        assert r["strong_hits"] == 1

    def test_medium_vocabulary_alone_scores_but_wins_no_strong_hit(self) -> None:
        r = s("Fine-tuning a large language model on well logs")
        assert r["llm_present"] == "yes"
        assert r["strong_hits"] == 0
        assert r["agentic_score"] > 0


class TestCaseSensitivity:
    def test_react_the_prompting_pattern_is_a_signal(self) -> None:
        r = s("ReAct prompting for earthquake catalogs", "Uses an LLM.")
        assert r["strong_hits"] == 1
        assert r"\bReAct\b" in r["signals"]

    @pytest.mark.parametrize(
        "title",
        [
            "Minerals react with groundwater in the aquifer",
            "Reactive transport in a fractured aquifer",
            "How carbonates react under CO2 storage conditions",
        ],
    )
    def test_lowercase_react_is_not_a_signal(self, title: str) -> None:
        # Matched case-insensitively this one pattern produced more false positives
        # than every other signal combined.
        assert r"\bReAct\b" not in s(title, "Uses a large language model.")["signals"]


class TestNegativeSuppression:
    @pytest.mark.parametrize(
        "phrase",
        [
            "Chemical agents in groundwater remediation",
            "Contrast agents for borehole imaging",
            "Reducing agents in aquifer treatment",
            "Chelating agents and contaminant transport",
            "Agents of erosion in alpine catchments",
        ],
    )
    def test_the_agent_that_is_not_an_agent_scores_nothing(self, phrase: str) -> None:
        # Without this, chemistry and medicine flood the top of the ranking.
        assert s(phrase)["strong_hits"] == 0

    def test_suppression_is_local_to_the_phrase(self) -> None:
        # A paper that mentions reducing agents *and* is an LLM agent paper must still
        # score: the negative pattern masks its own span, not the whole record.
        r = s(
            "An LLM agent for geochemical modelling",
            "The workflow considers reducing agents in the aquifer.",
        )
        assert r["strong_hits"] >= 1


class TestModelContextProtocol:
    def test_bare_mcp_is_not_a_signal(self) -> None:
        # MCP is also monocyte chemoattractant protein.
        assert s("MCP levels in seismic swarm patients")["strong_hits"] == 0

    @pytest.mark.parametrize(
        "title",
        [
            "An MCP server for SPECFEM waveform simulation",
            "A model context protocol suite for well logs",
            "MCP-based tooling for earthquake catalogs",
        ],
    )
    def test_mcp_next_to_a_system_noun_is_a_signal(self, title: str) -> None:
        assert s(title)["strong_hits"] >= 1

    @pytest.mark.parametrize(
        "title", ["seismo-mcp: tools for earthquake catalogs", "open-darts-mcp"]
    )
    def test_a_hyphenated_tool_name_ending_in_mcp_is_a_signal(self, title: str) -> None:
        # These four tools — open-darts-MCP, specfem-mcp, seismo-mcp, GeoMCP — all
        # scored below the cut on a corpus harvested to find exactly them.
        assert s(title)["strong_hits"] >= 1


class TestCompoundVocabulary:
    @pytest.mark.parametrize(
        "title",
        [
            "LLM-Powered Data Automation for 3D Geological Model Updating",
            "An LLM-assisted workflow for geological unit harmonization",
            "A foundation model-based framework for seismic interpretation",
        ],
    )
    def test_a_system_that_never_says_agent_still_scores(self, title: str) -> None:
        # Every false negative in the v0.4 audit sample had this shape, and none could
        # be recovered by lowering --min-score: they scored on medium signals alone.
        r = s(title)
        assert r["strong_hits"] >= 1
        assert r["agentic_score"] >= 3

    @pytest.mark.xfail(
        reason="AGENT_COMPOUND lists a bare `GPT` head, but the compound patterns are "
        "only evaluated when `llm_present` is already true, and MEDIUM's GPT pattern is "
        "`\\bGPT-?[345]\\b` — it needs a version digit. So a title whose only LLM token is "
        "bare `GPT` ('GPT-driven pipeline') can never reach the head that was written for "
        "it. Fix is a MEDIUM entry for bare GPT; a scoring change, so it belongs in a "
        "version bump with a re-triage.",
        strict=True,
    )
    def test_bare_gpt_reaches_the_compound_head_written_for_it(self) -> None:
        assert s("GPT-driven pipeline for stratigraphic correlation")["strong_hits"] >= 1

    @pytest.mark.xfail(
        reason="AGENT_GENERIC's comma pattern allows {0,2} intervening word-units, but "
        "the title its own comment names has five ('Multi-Modal Large-Language-Model'). "
        "Widening to {0,5} matches it — a scoring change, so it belongs in a version bump "
        "with a re-triage, not in a refactor.",
        strict=True,
    )
    def test_canonical_comma_title_shape_matches(self) -> None:
        r = s("A Multi-Agent, Multi-Modal Large-Language-Model Framework for Seismology")
        assert r["strong_hits"] >= 1


class TestScopeAndGroup:
    @pytest.mark.parametrize(
        ("title", "group"),
        [
            ("An LLM agent for phase picking and earthquake catalogs", "seismology"),
            ("An LLM agent for groundwater and aquifer modelling", "hydrogeology"),
            ("An agentic workflow for CO2 storage and carbon sequestration", "ccs"),
            ("An AI agent for slope stability and landslide geotechnics", "engineering_geology"),
        ],
    )
    def test_a_named_subfield_yields_core_scope(self, title: str, group: str) -> None:
        r = s(title)
        assert r["scope_computed"] == "core"
        assert r["group_computed"] == group

    def test_the_most_mentioned_group_wins(self) -> None:
        r = s(
            "An LLM agent for subsurface work",
            "Groundwater, aquifer and groundwater contaminant transport, with one mention "
            "of earthquake data.",
        )
        assert r["group_computed"] == "hydrogeology"

    def test_a_periphery_domain_yields_periphery_scope(self) -> None:
        r = s("An LLM agent for satellite imagery and remote sensing land cover")
        assert r["scope_computed"] == "periphery"
        assert r["group_computed"] == "earth_observation"

    def test_general_geoscience_vocabulary_falls_back_to_core(self) -> None:
        # The v0.5 regression: 190 records said "geoscience" without naming a subfield,
        # got scope none, and were discarded regardless of score. Shortlisting is not
        # admission — these belong in front of the screener, who decides the subfield.
        r = s("An agentic AI approach to geoscience data")
        assert r["scope_computed"] == "core"
        assert r["group_computed"] == "geoscience_general"

    def test_no_geoscience_vocabulary_yields_no_scope(self) -> None:
        r = s("An agentic AI approach to protein folding")
        assert r["scope_computed"] == "none"
        assert r["group_computed"] == ""
        # It still scores. The cut is an AND, and scope is the condition that drops it.
        assert r["agentic_score"] > 0


class TestFlagsAndSignals:
    def test_pre_llm_work_is_flagged_not_scored(self) -> None:
        r = s("An agent-based model of reservoir simulation with reinforcement learning")
        assert r["pre_llm_flag"] == "yes"
        assert r["strong_hits"] == 0

    def test_a_title_hit_is_marked_with_a_star(self) -> None:
        assert "*" in s("An agentic AI approach to geoscience")["signals"]

    def test_an_abstract_only_hit_is_not_starred(self) -> None:
        r = s("A study of subsurface data", "The method is agentic AI.")
        assert "*" not in r["signals"]

    def test_a_title_hit_counts_once_towards_strong_hits(self) -> None:
        # The title copy inflates agentic_score deliberately — a signal in the title is
        # what the paper is about — but must not inflate the strong-hit count the cut
        # is applied to.
        title_only = s("An agentic AI approach to geoscience")
        abstract_only = s("A study of geoscience data", "The method is agentic AI.")
        assert title_only["strong_hits"] == abstract_only["strong_hits"] == 1
        assert title_only["agentic_score"] > abstract_only["agentic_score"]

    def test_signals_are_bounded(self) -> None:
        r = s(
            "An agentic AI LLM agent tool-calling function-calling LangChain AutoGen "
            "LangGraph CrewAI AutoGPT AI scientist agentic workflow for seismology",
            "model context protocol MCP server agent2agent multi-agent LLM autonomous agent",
        )
        assert len(r["signals"]) <= 300


class TestDigest:
    def test_digest_carries_the_key_score_and_provenance(self) -> None:
        row = s("An agentic AI approach to seismology")
        row.update(
            {
                "identity_key": "doi:10.1/a",
                "title": "An agentic AI approach to seismology",
                "year": "2025",
                "venue": "J. Test",
                "cited_by": "7",
                "doi": "10.1/a",
                "abstract": "word " * 100,
            }
        )
        out = triage.digest(row)
        assert out.startswith("### doi:10.1/a\n")
        assert "score " in out and "(strong " in out
        assert "doi:10.1/a" in out
        assert "cites 7" in out

    def test_digest_truncates_the_abstract(self) -> None:
        row = s("A title")
        row.update({"identity_key": "k", "title": "A title", "abstract": "word " * 200})
        assert triage.digest(row, words=10).count("word") == 10

    def test_digest_says_so_when_there_is_no_abstract(self) -> None:
        row = s("A title")
        row.update({"identity_key": "k", "title": "A title", "abstract": ""})
        assert "(no abstract)" in triage.digest(row)

    def test_digest_prefers_doi_then_arxiv_then_url(self) -> None:
        base = s("A title")
        base.update({"identity_key": "k", "title": "A title", "abstract": ""})
        assert "doi:10.1/a" in triage.digest({**base, "doi": "10.1/a", "arxiv_id": "2501.00001"})
        assert "arXiv:2501.00001" in triage.digest({**base, "arxiv_id": "2501.00001"})
        assert "https://example.org/x" in triage.digest({**base, "url": "https://example.org/x"})


CORPUS = [
    # (identity_key, title) — two clear admits, two clear rejects.
    ("doi:10.1/in-1", "An agentic AI workflow for earthquake catalogs"),
    ("doi:10.1/in-2", "An LLM agent for groundwater aquifer modelling"),
    ("doi:10.1/out-1", "Chemical agents in groundwater remediation"),
    ("doi:10.1/out-2", "A Multi-Agent System for traffic control"),
]


def write_corpus(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    with (out / "screened.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["identity_key", "title", "abstract", "cited_by"])
        w.writeheader()
        for key, title in CORPUS:
            w.writerow({"identity_key": key, "title": title, "abstract": "", "cited_by": "0"})


class TestEndToEnd:
    def test_the_cut_splits_the_corpus_and_writes_every_artefact(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        assert triage.main(["--out", str(out), "--audit-n", "2"]) == 0

        shortlist = (out / "shortlist.md").read_text(encoding="utf-8")
        assert "### doi:10.1/in-1" in shortlist
        assert "### doi:10.1/in-2" in shortlist
        assert "doi:10.1/out-1" not in shortlist
        assert "doi:10.1/out-2" not in shortlist

        # The sample is drawn from below the cut, so the rejects are what it can hold.
        sample = (out / "audit_sample.md").read_text(encoding="utf-8")
        assert "### doi:10.1/in-1" not in sample

        stats = (out / "triage_stats.md").read_text(encoding="utf-8")
        assert "Harvested: 4" in stats
        assert "Shortlisted: 2" in stats
        # Both knobs are reported, because the cut is an AND and varying one hides
        # which is binding.
        assert "| min-score | strong>=0 | strong>=1 | strong>=2 |" in stats

        assert (out / "triage.csv").exists()

    def test_the_sample_is_reproducible_for_a_given_seed(self, tmp_path: Path) -> None:
        # If the sample moved between runs, the false-negative rate would be measured
        # against a file that no longer exists.
        first, second = tmp_path / "a", tmp_path / "b"
        write_corpus(first)
        write_corpus(second)
        triage.main(["--out", str(first), "--audit-n", "1"])
        triage.main(["--out", str(second), "--audit-n", "1"])
        a = (first / "audit_sample.md").read_text(encoding="utf-8")
        b = (second / "audit_sample.md").read_text(encoding="utf-8")
        assert a == b

    def test_it_refuses_to_regenerate_underneath_screening(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        (out / "screening.csv").write_text("identity_key,decision\n", encoding="utf-8")
        with pytest.raises(SystemExit, match="exists"):
            triage.main(["--out", str(out)])

    def test_force_overrides_the_refusal(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        (out / "screening.csv").write_text("identity_key,decision\n", encoding="utf-8")
        assert triage.main(["--out", str(out), "--force", "--audit-n", "1"]) == 0

    def test_it_refuses_without_a_harvest(self, tmp_path: Path) -> None:
        out = tmp_path / "empty"
        out.mkdir()
        with pytest.raises(SystemExit, match=r"run harvest\.py first"):
            triage.main(["--out", str(out)])

    def test_a_stricter_cut_shortlists_less(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        triage.main(["--out", str(out), "--min-strong", "9", "--audit-n", "1"])
        assert "Shortlisted: 0" in (out / "triage_stats.md").read_text(encoding="utf-8")
