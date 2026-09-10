"""harvest.py's identity, merge and query-plan logic.

No network. The three API readers are thin translations of a JSON or Atom payload
and are exercised only through their normalisation helpers; what is tested here is
everything that decides whether two records are the same paper, because that is
what every count downstream is built on.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

import harvest


class TestNormalise:
    def test_clean_collapses_whitespace_and_newlines(self) -> None:
        assert harvest.clean("  a\n  b\t c ") == "a b c"

    def test_clean_tolerates_none(self) -> None:
        assert harvest.clean(None) == ""

    def test_title_slug_ignores_case_and_punctuation(self) -> None:
        a = harvest.title_slug("An LLM Agent for Phase-Picking: A Study")
        b = harvest.title_slug("an llm agent for phase picking a study")
        assert a == b == "anllmagentforphasepickingastudy"

    def test_title_slug_is_bounded(self) -> None:
        assert len(harvest.title_slug("word " * 200)) == 120

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("https://doi.org/10.1000/AbC", "10.1000/abc"),
            ("http://doi.org/10.1000/abc", "10.1000/abc"),
            ("doi:10.1000/abc", "10.1000/abc"),
            ("  10.1000/ABC  ", "10.1000/abc"),
            ("", ""),
            (None, ""),
        ],
    )
    def test_norm_doi(self, raw: str | None, expected: str) -> None:
        assert harvest.norm_doi(raw) == expected

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("https://arxiv.org/abs/2501.01234v2", "2501.01234"),
            ("arXiv:2501.01234", "2501.01234"),
            ("2408.1234", "2408.1234"),
            ("no identifier here", ""),
            (None, ""),
        ],
    )
    def test_norm_arxiv_strips_the_version(self, raw: str | None, expected: str) -> None:
        assert harvest.norm_arxiv(raw) == expected

    def test_inverted_to_text_restores_word_order(self) -> None:
        inv = {"agent": [1], "An": [0], "picks": [2]}
        assert harvest.inverted_to_text(inv) == "An agent picks"

    def test_inverted_to_text_handles_repeated_words(self) -> None:
        inv = {"the": [0, 2], "agent": [1], "tool": [3]}
        assert harvest.inverted_to_text(inv) == "the agent the tool"

    def test_inverted_to_text_tolerates_none(self) -> None:
        assert harvest.inverted_to_text(None) == ""


class TestIdentity:
    def test_doi_wins_over_arxiv(self) -> None:
        rec = {"doi": "10.1000/x", "arxiv_id": "2501.01234", "title": "T"}
        assert harvest.identity_of(rec) == "doi:10.1000/x"

    def test_arxiv_is_used_when_there_is_no_doi(self) -> None:
        assert harvest.identity_of({"arxiv_id": "2501.01234", "title": "T"}) == "arxiv:2501.01234"

    def test_title_is_the_last_resort(self) -> None:
        assert harvest.identity_of({"title": "A Title"}) == "title:atitle"


def _rec(**over: Any) -> harvest.Record:
    base: harvest.Record = {
        "doi": "",
        "arxiv_id": "",
        "title": "An LLM agent for phase picking",
        "abstract": "",
        "venue": "",
        "oa_pdf_url": "",
        "authors": "",
        "cited_by": "",
        "source_apis": "openalex",
    }
    base.update(over)
    return base


def _query(qid: str = "q001", band: str = "A_agentic", group: str = "seismology") -> harvest.Query:
    return {"query_id": qid, "band": band, "scope": "core", "domain_group": group}


class TestMerge:
    def test_first_sighting_is_new_and_stamped(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        assert harvest.merge(store, alias, _rec(doi="10.1/a"), _query(), "run1") is True
        row = store["doi:10.1/a"]
        assert row["identity_key"] == "doi:10.1/a"
        assert row["query_ids"] == "q001"
        assert row["domain_group"] == "seismology"
        assert row["band"] == "A_agentic"
        assert row["first_seen_run"] == "run1"

    def test_second_sighting_accumulates_provenance(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(doi="10.1/a"), _query("q001"), "run1")
        new = harvest.merge(
            store, alias, _rec(doi="10.1/a", source_apis="s2"), _query("q002"), "run2"
        )
        row = store["doi:10.1/a"]
        assert new is False
        assert row["query_ids"] == "q001;q002"
        assert row["source_apis"] == "openalex;s2"
        # A row records the run that first saw it, not the run that last touched it.
        assert row["first_seen_run"] == "run1"

    def test_preprint_and_published_version_collapse_on_the_title(self) -> None:
        # Without the title alias the corpus double-counts most of arXiv: the same
        # paper arrives as arxiv:… from arXiv and as doi:… from OpenAlex.
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(
            store, alias, _rec(arxiv_id="2501.01234", source_apis="arxiv"), _query("q001"), "r"
        )
        new = harvest.merge(store, alias, _rec(doi="10.1/a"), _query("q002"), "r")
        assert new is False
        assert len(store) == 1
        assert store["arxiv:2501.01234"]["source_apis"] == "arxiv;openalex"

    def test_differing_titles_stay_separate(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(arxiv_id="2501.01234", title="One"), _query(), "r")
        harvest.merge(store, alias, _rec(doi="10.1/a", title="Another"), _query(), "r")
        assert len(store) == 2

    def test_empty_fields_are_backfilled_from_the_richer_record(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(doi="10.1/a", abstract=""), _query(), "r")
        harvest.merge(
            store,
            alias,
            _rec(doi="10.1/a", abstract="The real abstract.", venue="J"),
            _query(),
            "r",
        )
        assert store["doi:10.1/a"]["abstract"] == "The real abstract."
        assert store["doi:10.1/a"]["venue"] == "J"

    def test_populated_fields_are_not_overwritten(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(doi="10.1/a", abstract="first"), _query(), "r")
        harvest.merge(store, alias, _rec(doi="10.1/a", abstract="second"), _query(), "r")
        assert store["doi:10.1/a"]["abstract"] == "first"

    def test_precision_band_wins_for_reporting(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(doi="10.1/a"), _query(band="B_llm"), "r")
        assert store["doi:10.1/a"]["band"] == "B_llm"
        harvest.merge(store, alias, _rec(doi="10.1/a"), _query("q002", band="A_agentic"), "r")
        assert store["doi:10.1/a"]["band"] == "A_agentic"

    def test_recall_band_does_not_demote_a_precision_hit(self) -> None:
        store: dict[str, harvest.Record] = {}
        alias: dict[str, str] = {}
        harvest.merge(store, alias, _rec(doi="10.1/a"), _query(band="A_agentic"), "r")
        harvest.merge(store, alias, _rec(doi="10.1/a"), _query("q002", band="B_llm"), "r")
        assert store["doi:10.1/a"]["band"] == "A_agentic"


CONFIG: harvest.Config = {
    "from_date": "2022-11-01",
    "openalex_max_pages": 20,
    "arxiv_max_results": 1000,
    "bands": {
        "A_agentic": {"terms": ['"agentic AI"', '"AI agent"']},
        "B_llm": {"terms": ['"large language model"']},
    },
    "domain_groups": {
        "core": {"groups": {"seismology": ["seismology", '"phase picking"']}},
        "periphery": {"groups": {"ocean": ["oceanography"]}},
    },
}


class TestValidateConfig:
    def test_a_well_formed_config_passes(self) -> None:
        harvest.validate_config(CONFIG)

    @pytest.mark.parametrize("term", ['"a" AND "b"', '"a" OR "b"', 'NOT "b"'])
    def test_a_bare_operator_in_a_band_is_refused(self, term: str) -> None:
        # OpenAlex answers a query with a bare operator inside an OR group with zero
        # results and no error, so the cell is silently empty and every later count
        # still looks plausible. Refusing to run is the only visible failure available.
        cfg = {**CONFIG, "bands": {"A_agentic": {"terms": [term]}}}
        with pytest.raises(SystemExit):
            harvest.validate_config(cfg)

    def test_a_bare_operator_in_a_domain_group_is_refused(self) -> None:
        cfg = {
            **CONFIG,
            "domain_groups": {"core": {"groups": {"seismology": ['"seismic" AND "agent"']}}},
        }
        with pytest.raises(SystemExit):
            harvest.validate_config(cfg)

    def test_a_term_merely_containing_the_letters_is_allowed(self) -> None:
        # "SAND" and "MONOTONIC" contain AND and NOT; the check is word-bounded.
        cfg = {**CONFIG, "bands": {"A_agentic": {"terms": ['"sand production"', '"monotonic"']}}}
        harvest.validate_config(cfg)


class TestBuildPlan:
    def test_one_query_per_group_and_band(self) -> None:
        plan = harvest.build_plan(CONFIG, None, ["core", "periphery"])
        assert len(plan) == 4  # (1 core group + 1 periphery group) x 2 bands
        assert [q["query_id"] for q in plan] == ["q001", "q002", "q003", "q004"]

    def test_scopes_filter_the_plan(self) -> None:
        plan = harvest.build_plan(CONFIG, None, ["core"])
        assert {q["scope"] for q in plan} == {"core"}
        assert len(plan) == 2

    def test_bands_filter_the_plan(self) -> None:
        plan = harvest.build_plan(CONFIG, ["A_agentic"], ["core", "periphery"])
        assert {q["band"] for q in plan} == {"A_agentic"}

    def test_openalex_query_is_an_and_of_two_or_groups(self) -> None:
        plan = harvest.build_plan(CONFIG, ["A_agentic"], ["core"])
        assert (
            plan[0]["openalex"]
            == '("agentic AI" OR "AI agent") AND (seismology OR "phase picking")'
        )

    def test_arxiv_query_prefixes_every_term_with_abs(self) -> None:
        plan = harvest.build_plan(CONFIG, ["A_agentic"], ["core"])
        assert plan[0]["arxiv"] == (
            '(abs:"agentic AI" OR abs:"AI agent") AND (abs:seismology OR abs:"phase picking")'
        )

    def test_s2_query_is_the_leading_term_of_each_side_unquoted(self) -> None:
        plan = harvest.build_plan(CONFIG, ["A_agentic"], ["core"])
        assert plan[0]["s2"] == "agentic AI seismology"

    def test_an_unknown_scope_yields_nothing(self) -> None:
        assert harvest.build_plan(CONFIG, None, ["nonexistent"]) == []


class TestApiCap:
    def test_openalex_cap_is_pages_times_page_size(self) -> None:
        assert harvest.api_cap("openalex", CONFIG) == 20 * harvest.OPENALEX_PER_PAGE

    def test_arxiv_cap_comes_from_the_config(self) -> None:
        assert harvest.api_cap("arxiv", CONFIG) == 1000

    def test_s2_cap_is_the_call_limit(self) -> None:
        assert harvest.api_cap("s2", CONFIG) == harvest.S2_LIMIT


class TestCsvIo:
    def test_missing_file_reads_as_empty(self, tmp_path: Path) -> None:
        assert harvest.read_csv(tmp_path / "absent.csv") == []

    def test_roundtrip_keeps_the_declared_columns_only(self, tmp_path: Path) -> None:
        path = tmp_path / "sub" / "out.csv"
        harvest.write_csv(path, ["a", "b"], [{"a": "1", "b": "2", "ignored": "3"}])
        assert harvest.read_csv(path) == [{"a": "1", "b": "2"}]

    def test_missing_values_are_written_as_empty_strings(self, tmp_path: Path) -> None:
        path = tmp_path / "out.csv"
        harvest.write_csv(path, ["a", "b"], [{"a": "1"}])
        assert harvest.read_csv(path) == [{"a": "1", "b": ""}]

    def test_embedded_newlines_and_delimiters_survive(self, tmp_path: Path) -> None:
        path = tmp_path / "out.csv"
        harvest.write_csv(path, ["abstract"], [{"abstract": 'a, b\n"c"'}])
        assert harvest.read_csv(path)[0]["abstract"] == 'a, b\n"c"'
