"""triage_tango.py: the domain half of the 02 score, and the config it comes from.

The agentic half is `triage.py`'s and is tested in `test_triage.py`; what is tested here
is what is new — a vocabulary loaded from the query config, the touchpoint pass, the
`--min-domain` knob, and the two config files agreeing with each other.

The regression these exist to prevent is the one `decisions.md` records from v0.5: a
record that scores well, matches no domain pattern, gets `scope: none`, and is dropped
from the shortlist without appearing in any count. In this run that failure is likelier,
not less likely, because the domain is all of computational science and the vocabulary
was written before the corpus existed.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import pytest

import triage_tango

REPO = Path(__file__).resolve().parents[1]
FULL_CONFIG = REPO / "reference" / "queries_tango.json"
SMOKE_CONFIG = REPO / "reference" / "queries_tango_smoke.json"


def load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        cfg: dict[str, Any] = json.load(f)
    return cfg


@pytest.fixture(scope="module")
def vocab() -> triage_tango.Vocabulary:
    """The shipped vocabulary, so these tests check the file a run would actually use."""
    return triage_tango.load_vocabulary(load(FULL_CONFIG))


def s(vocab: triage_tango.Vocabulary, title: str, abstract: str = "") -> triage_tango.Row:
    return triage_tango.score({"title": title, "abstract": abstract}, vocab)


class TestConfigIntegrity:
    def test_every_harvested_group_has_a_triage_pattern(self) -> None:
        # The whole point of `load_vocabulary`'s validation. If this fails, a group is
        # being harvested into a corpus nothing can score.
        assert triage_tango.load_vocabulary(load(FULL_CONFIG))

    def test_a_group_without_a_pattern_is_refused(self) -> None:
        cfg = load(FULL_CONFIG)
        del cfg["triage"]["core"]["solver_control"]
        with pytest.raises(SystemExit, match="same groups"):
            triage_tango.load_vocabulary(cfg)

    def test_a_pattern_for_a_group_that_is_never_harvested_is_refused(self) -> None:
        cfg = load(FULL_CONFIG)
        cfg["triage"]["core"]["astrology"] = "astrolog"
        with pytest.raises(SystemExit, match="same groups"):
            triage_tango.load_vocabulary(cfg)

    def test_a_config_with_no_triage_block_is_refused(self) -> None:
        cfg = load(FULL_CONFIG)
        del cfg["triage"]
        with pytest.raises(SystemExit, match="triage"):
            triage_tango.load_vocabulary(cfg)

    def test_a_config_with_no_general_fallback_is_refused(self) -> None:
        cfg = load(FULL_CONFIG)
        del cfg["triage"]["general"]
        with pytest.raises(SystemExit, match="general"):
            triage_tango.load_vocabulary(cfg)

    def test_the_smoke_config_is_a_verbatim_subset_of_the_full_one(self) -> None:
        # The smoke config exists because harvest.py is frozen and takes --config rather
        # than a smoke flag. Copying the cells means they can drift, and a mechanics test
        # that exercises a plan the full run does not have proves nothing about it.
        full, smoke = load(FULL_CONFIG), load(SMOKE_CONFIG)
        for band, spec in smoke["bands"].items():
            assert spec["terms"] == full["bands"][band]["terms"], band
        for scope, block in smoke["domain_groups"].items():
            for group, terms in block["groups"].items():
                assert terms == full["domain_groups"][scope]["groups"][group], group

    def test_the_smoke_config_exercises_periphery(self) -> None:
        # `--limit-queries N` cannot: the plan is core groups first. A smoke test with no
        # periphery cell leaves 07_periphery.md unwritable from harvest counts.
        assert load(SMOKE_CONFIG)["domain_groups"]["periphery"]["groups"]


class TestScopeAndGroup:
    @pytest.mark.parametrize(
        ("title", "group"),
        [
            ("An LLM agent that builds a process simulation flowsheet", "simulation_orchestration"),
            ("An agentic workflow for finite element mesh generation", "solver_control"),
            ("An LLM agent for Bayesian optimization of a surrogate model", "optimisation_uq"),
            ("An AI agent for techno-economic analysis of a power plant", "energy_systems"),
            ("An agentic workflow for geothermal reservoir simulation", "geoenergy_subsurface"),
            ("An LLM agent for molecular dynamics and catalyst design", "computational_discovery"),
        ],
    )
    def test_a_named_core_group_yields_core_scope(
        self, vocab: triage_tango.Vocabulary, title: str, group: str
    ) -> None:
        r = s(vocab, title)
        assert r["scope_computed"] == "core"
        assert r["group_computed"] == group

    @pytest.mark.parametrize(
        ("title", "group"),
        [
            ("An LLM agent for program repair and issue resolution", "software_engineering"),
            ("An agentic workflow for robotic laboratory chemical synthesis", "lab_automation"),
            ("A web agent for browser automation", "interface_agents"),
            ("An LLM agent for systematic review and literature review", "science_of_science"),
        ],
    )
    def test_the_neighbouring_agent_literatures_are_periphery(
        self, vocab: triage_tango.Vocabulary, title: str, group: str
    ) -> None:
        # Software-engineering agents are periphery by decision, not by accident: they
        # are the largest agent literature there is and this run is about driving TANGO,
        # not refactoring it.
        r = s(vocab, title)
        assert r["scope_computed"] == "periphery"
        assert r["group_computed"] == group

    def test_an_unnamed_computational_target_falls_back_to_core(
        self, vocab: triage_tango.Vocabulary
    ) -> None:
        r = s(vocab, "An agentic AI approach to running a numerical model")
        assert r["scope_computed"] == "core"
        assert r["group_computed"] == "simulation_general"

    def test_an_agent_that_drives_nothing_gets_no_scope(
        self, vocab: triage_tango.Vocabulary
    ) -> None:
        r = s(vocab, "An agentic AI approach to customer service tickets")
        assert r["scope_computed"] == "none"
        assert r["group_computed"] == ""
        # It still scores. The cut is an AND, and scope is the condition that drops it.
        assert r["agentic_score"] > 0

    def test_the_most_mentioned_group_wins(self, vocab: triage_tango.Vocabulary) -> None:
        r = s(
            vocab,
            "An LLM agent for engineering work",
            "Bayesian optimization of a surrogate model with uncertainty quantification, "
            "and one mention of a flowsheet.",
        )
        assert r["group_computed"] == "optimisation_uq"


class TestAgenticHalfIsShared:
    def test_the_agentic_score_is_triage_pys(self, vocab: triage_tango.Vocabulary) -> None:
        import triage

        row = {"title": "An agentic AI workflow for process simulation", "abstract": ""}
        assert s(vocab, row["title"])["agentic_score"] == triage.score(row)["agentic_score"]

    def test_generic_agent_vocabulary_still_needs_llm_corroboration(
        self, vocab: triage_tango.Vocabulary
    ) -> None:
        # "multi-agent system" is forty years old, and process simulation is older.
        r = s(vocab, "A Multi-Agent System for process simulation")
        assert r["llm_present"] == "no"
        assert r["strong_hits"] == 0


class TestTouchpoints:
    @pytest.mark.parametrize(
        ("text", "touchpoint"),
        [
            ("The agent writes the input deck for each case", "config_generation"),
            ("It selects solver settings after a convergence failure", "solver_control"),
            ("A multi-objective optimisation loop over the design", "optimisation_loop"),
            ("It trains a surrogate and an emulator of the simulator", "surrogate_modelling"),
            (
                "Latin hypercube sampling for uncertainty quantification",
                "uncertainty_quantification",
            ),
            ("Batch runs are dispatched to a SLURM cluster", "hpc_scale_out"),
            ("Tools are exposed through a model context protocol server", "tool_exposure"),
            ("It summarises the results and generates the plots", "results_interpretation"),
            ("The workflow computes LCOE and CAPEX", "techno_economic"),
            ("A regression test suite against reference solutions", "verification_regression"),
            ("Every run is tracked with DVC for reproducibility", "provenance_reproducibility"),
        ],
    )
    def test_each_touchpoint_matches_the_phrasing_it_was_written_for(
        self, vocab: triage_tango.Vocabulary, text: str, touchpoint: str
    ) -> None:
        # Every touchpoint is exercised, including the two that matched almost nothing on
        # the smoke corpus — a pattern that matches nothing anywhere is not a measurement
        # of the literature, it is a broken regex.
        assert touchpoint in s(vocab, "An LLM agent for simulation", text)["touchpoints"]

    def test_touchpoints_are_not_part_of_the_cut(self, vocab: triage_tango.Vocabulary) -> None:
        # A hit is a sorting aid. A record that touches nothing TANGO has is still
        # admitted or cut on the same criteria as one that touches everything.
        r = s(vocab, "An agentic AI workflow for process simulation")
        assert r["touchpoints"] == ""
        assert r["scope_computed"] == "core"


CORPUS = [
    # (identity_key, title, abstract)
    ("doi:10.1/in-1", "An agentic AI workflow for process simulation of a flowsheet", ""),
    (
        "doi:10.1/in-2",
        "An LLM agent for surrogate model calibration",
        "Bayesian optimization over a surrogate model with uncertainty quantification.",
    ),
    ("doi:10.1/out-1", "Chemical agents in groundwater remediation", ""),
    ("doi:10.1/out-2", "An agentic AI approach to customer service", ""),
]


def write_corpus(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    with (out / "screened.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["identity_key", "title", "abstract", "cited_by"])
        w.writeheader()
        for key, title, abstract in CORPUS:
            w.writerow({"identity_key": key, "title": title, "abstract": abstract, "cited_by": "0"})


class TestEndToEnd:
    def test_the_cut_splits_the_corpus_and_writes_every_artefact(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        argv = ["--out", str(out), "--config", str(FULL_CONFIG), "--audit-n", "2"]
        assert triage_tango.main(argv) == 0

        shortlist = (out / "shortlist.md").read_text(encoding="utf-8")
        assert "### doi:10.1/in-1" in shortlist
        assert "### doi:10.1/in-2" in shortlist
        assert "doi:10.1/out-1" not in shortlist
        assert "doi:10.1/out-2" not in shortlist

        stats = (out / "triage_stats.md").read_text(encoding="utf-8")
        assert "Harvested: 4" in stats
        assert "Shortlisted: 2" in stats
        # The provenance of both halves of the score, printed where the numbers are.
        assert "imported from `scripts/triage.py`" in stats
        assert "queries_tango.json" in stats
        # Both threshold tables, because the cut is an AND of three knobs now.
        assert "| min-score | strong>=0 | strong>=1 | strong>=2 |" in stats
        assert "| min-domain | shortlisted |" in stats
        assert (out / "triage.csv").exists()

    def test_the_domain_knob_tightens_the_cut(self, tmp_path: Path) -> None:
        # The knob the 01 run does not have, and the one the smoke corpus showed is
        # binding: 546 shortlisted at 1, 295 at 2.
        out = tmp_path / "run"
        write_corpus(out)
        argv = ["--out", str(out), "--config", str(FULL_CONFIG), "--audit-n", "1"]
        triage_tango.main([*argv, "--min-domain", "8"])
        assert "Shortlisted: 0" in (out / "triage_stats.md").read_text(encoding="utf-8")

    def test_every_touchpoint_is_listed_even_at_zero(self, tmp_path: Path) -> None:
        # A derived count is only checkable if the reader can see what was searched for.
        out = tmp_path / "run"
        write_corpus(out)
        triage_tango.main(["--out", str(out), "--config", str(FULL_CONFIG), "--audit-n", "1"])
        stats = (out / "triage_stats.md").read_text(encoding="utf-8")
        for name in triage_tango.load_vocabulary(load(FULL_CONFIG)).touchpoints:
            assert f"| {name} |" in stats

    def test_the_sample_is_reproducible_for_a_given_seed(self, tmp_path: Path) -> None:
        first, second = tmp_path / "a", tmp_path / "b"
        write_corpus(first)
        write_corpus(second)
        for out in (first, second):
            triage_tango.main(["--out", str(out), "--config", str(FULL_CONFIG), "--audit-n", "1"])
        a = (first / "audit_sample.md").read_text(encoding="utf-8")
        b = (second / "audit_sample.md").read_text(encoding="utf-8")
        assert a == b

    def test_it_refuses_to_regenerate_underneath_screening(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        (out / "screening.csv").write_text("identity_key,decision\n", encoding="utf-8")
        with pytest.raises(SystemExit, match="exists"):
            triage_tango.main(["--out", str(out), "--config", str(FULL_CONFIG)])

    def test_force_overrides_the_refusal(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        (out / "screening.csv").write_text("identity_key,decision\n", encoding="utf-8")
        argv = ["--out", str(out), "--config", str(FULL_CONFIG), "--force", "--audit-n", "1"]
        assert triage_tango.main(argv) == 0

    def test_it_refuses_without_a_harvest(self, tmp_path: Path) -> None:
        out = tmp_path / "empty"
        out.mkdir()
        with pytest.raises(SystemExit, match=r"run harvest\.py first"):
            triage_tango.main(["--out", str(out), "--config", str(FULL_CONFIG)])

    def test_it_refuses_a_config_that_is_not_there(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        write_corpus(out)
        with pytest.raises(SystemExit, match="not found"):
            triage_tango.main(["--out", str(out), "--config", str(tmp_path / "nope.json")])


class TestTheFallbackBucketSurvivesTheDomainKnob:
    """The v0.5 regression, arriving through a different door.

    `domain_score` was `sum(dom) or sum(per)`, which is zero for every record the
    general fallback rescues — so the default `--min-domain 1` deleted the whole
    `simulation_general` bucket: 11 records on the smoke corpus, invisible in every
    count, exactly the shape of the 190 records v0.5 lost to `scope: none`.
    """

    def test_a_fallback_record_carries_a_domain_score(self, vocab: triage_tango.Vocabulary) -> None:
        r = s(vocab, "An agentic AI approach to running a numerical model")
        assert r["group_computed"] == "simulation_general"
        assert r["domain_score"] >= 1

    def test_the_default_knob_keeps_the_fallback_bucket(self, tmp_path: Path) -> None:
        out = tmp_path / "run"
        out.mkdir(parents=True)
        with (out / "screened.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["identity_key", "title", "abstract", "cited_by"])
            w.writeheader()
            w.writerow(
                {
                    "identity_key": "doi:10.1/fallback",
                    "title": "An agentic AI workflow for running a numerical model",
                    "abstract": "",
                    "cited_by": "0",
                }
            )
        triage_tango.main(["--out", str(out), "--config", str(FULL_CONFIG), "--audit-n", "1"])
        assert "### doi:10.1/fallback" in (out / "shortlist.md").read_text(encoding="utf-8")
