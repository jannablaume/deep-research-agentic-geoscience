"""export_web.py's parsers and counters.

The export is the one place a number can silently change meaning: a count lifted
out of prose instead of counted from a CSV, a share taken against the wrong
denominator, a citation quietly dropped because its key did not resolve. Each of
those is a test here.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable
from pathlib import Path

import pytest

import audit
import export_web as ew
from conftest import ADMITTED, CORE_KEY

RunFactory = Callable[[], Path]


class TestReading:
    def test_missing_csv_reads_as_empty(self, tmp_path: Path) -> None:
        assert ew.read_csv(tmp_path / "absent.csv") == []

    def test_missing_text_reads_as_empty_string(self, tmp_path: Path) -> None:
        assert ew.read_text(tmp_path / "absent.md") == ""


class TestParseRunLog:
    RUN = (
        "# Run record\n\n"
        "- date: 2026-09-07\n"
        "- prompt: `prompts/01_landscape_neutral.md` v0.5\n"
        "- prompt commit: f28f05f\n"
        "- model: test\n\n"
        "## Notes\n\n"
        "- date: 1999-01-01\n"
    )

    def test_the_opening_block_is_read(self) -> None:
        log = ew.parse_run_log(self.RUN)
        assert log["date"] == "2026-09-07"
        assert log["model"] == "test"

    def test_backticks_are_stripped(self) -> None:
        assert ew.parse_run_log(self.RUN)["prompt"] == "prompts/01_landscape_neutral.md v0.5"

    def test_a_multi_word_key_is_read(self) -> None:
        assert ew.parse_run_log(self.RUN)["prompt commit"] == "f28f05f"

    def test_nothing_below_the_first_heading_is_read(self) -> None:
        # A bullet under "## Notes" must not overwrite the run record's own date.
        assert ew.parse_run_log(self.RUN)["date"] == "2026-09-07"

    def test_an_empty_run_record_yields_nothing(self) -> None:
        assert ew.parse_run_log("") == {}


class TestParseAudit:
    TABLE = (
        "# Self-audit\n\n"
        "| Check | Result | Detail |\n"
        "|---|---|---|\n"
        "| screened.csv parses and is non-empty | PASS | 11191 rows |\n"
        "| Every shortlist record was screened | PASS | all 712 shortlisted records screened |\n"
        "| No promotional framing | FAIL | found: promising |\n"
    )

    def test_rows_are_parsed_and_the_header_skipped(self) -> None:
        a = ew.parse_audit(self.TABLE)
        assert len(a["checks"]) == 3
        assert a["checks"][0]["check"] == "screened.csv parses and is non-empty"

    def test_passes_are_counted(self) -> None:
        assert ew.parse_audit(self.TABLE)["passed"] == 2

    def test_the_two_counts_only_audit_md_carries_are_recovered(self) -> None:
        # screened.csv and triage.csv are gitignored, so these two numbers cannot be
        # counted from a fresh clone and come from audit.md instead.
        a = ew.parse_audit(self.TABLE)
        assert a["harvested"] == 11191
        assert a["shortlisted"] == 712

    def test_absent_counts_are_none_not_zero(self) -> None:
        # A missing count must render as an em dash, never as a measured zero.
        a = ew.parse_audit("| Check | Result | Detail |\n|---|---|---|\n")
        assert a["harvested"] is None
        assert a["shortlisted"] is None


class TestCiteLabel:
    def test_a_resolved_citation_shows_its_reference_number(self) -> None:
        # Not the DOI (longer than the clause holding it), not its suffix
        # (`s44304-026-00262-z` identifies nothing to a human), and not the
        # system name — that duplicates the prose, which already writes
        # "ESHM20-MCP wrapping OpenQuake" before the citation.
        assert (
            ew.cite_label("doi:10.1038/s44304-026-00262-z", {"doi:10.1038/s44304-026-00262-z": 7})
            == "7"
        )

    @pytest.mark.parametrize(
        ("key", "label"),
        [
            ("arxiv:2501.01234", "arXiv:2501.01234"),
            ("doi:10.48550/arxiv.2501.01234", "arXiv:2501.01234"),
            ("doi:10.1029/2024JB030123", "2024JB030123"),
            ("title:someslug", "title:someslug"),
        ],
    )
    def test_an_unnumbered_key_falls_back_to_its_shortest_honest_form(
        self, key: str, label: str
    ) -> None:
        # An unresolved key gets no number — it is not in the reference list —
        # and must stay identifiable: audit.py fails a run that has one, so
        # seeing which one is the entire point.
        assert ew.cite_label(key) == label
        assert ew.cite_label(key, {}) == label


class TestCiteName:
    def test_it_gives_the_system_behind_a_reference_number(self) -> None:
        assert ew.cite_name("doi:10.1/a", {"doi:10.1/a": "ESHM20-MCP"}) == "ESHM20-MCP"

    @pytest.mark.parametrize("system_id", ["not stated", "  ", "not stated (abstract only)"])
    def test_an_unnamed_row_falls_through_to_the_key(self, system_id: str) -> None:
        # A tooltip reading "not stated" tells the reader nothing about which
        # paper the marker is about to open.
        assert (
            ew.cite_name("arxiv:2501.01234", {"arxiv:2501.01234": system_id}) == "arxiv:2501.01234"
        )

    def test_a_key_absent_from_the_map_is_its_own_name(self) -> None:
        assert ew.cite_name("doi:10.1/missing", {}) == "doi:10.1/missing"


NAMES = {"doi:10.1/a": "PhasePicker"}
REFS = {"doi:10.1/a": 3}


class TestSpans:
    def test_the_three_inline_forms_are_recognised(self) -> None:
        out = ew.spans("plain **bold** and `code` and [[doi:10.1/a]].", NAMES, REFS)
        kinds = [sp["t"] for sp in out]
        # No trailing text span: the full stop is carried on the citation, not
        # left as the head of the next text run. See `tail` below.
        assert kinds == ["text", "strong", "text", "code", "text", "cite"]

    def test_a_citation_carries_the_punctuation_that_follows_it(self) -> None:
        # A reference marker is an inline box, and a line breaking between the
        # box and its full stop strands the stop at the start of the next line.
        assert ew.spans("unread [[doi:10.1/a]].", NAMES, REFS)[-1]["tail"] == "."
        assert ew.spans("a [[doi:10.1/a]], b", NAMES, REFS)[1]["tail"] == ","
        assert ew.spans("x [[doi:10.1/a]]).", NAMES, REFS)[-1]["tail"] == ")."

    def test_a_citation_not_followed_by_punctuation_has_an_empty_tail(self) -> None:
        out = ew.spans("see [[doi:10.1/a]] then", NAMES, REFS)
        assert out[1]["tail"] == ""
        # The words after it stay a text span of their own, space intact.
        assert out[2] == {"t": "text", "v": " then"}

    def test_a_citation_carries_its_key_number_name_and_resolution(self) -> None:
        out = ew.spans("see [[doi:10.1/a]]", NAMES, REFS)
        cite = next(sp for sp in out if sp["t"] == "cite")
        assert cite["key"] == "doi:10.1/a"
        assert cite["label"] == "3"
        assert cite["name"] == "PhasePicker"
        assert cite["resolved"] is True

    def test_an_unresolvable_citation_is_kept_and_marked(self) -> None:
        # Dropping it would hide a defect audit.py already fails the run for.
        out = ew.spans("see [[doi:10.1/missing]]", NAMES, REFS)
        cite = next(sp for sp in out if sp["t"] == "cite")
        assert cite["resolved"] is False
        assert cite["label"] == "missing"  # the DOI suffix — still identifiable

    def test_the_refs_map_doubles_as_the_resolution_check(self) -> None:
        # A key in `refs` is a key papers.csv carries, so there is only one
        # source of truth for "does this citation resolve".
        assert ew.spans("[[doi:10.1/a]]", NAMES, REFS)[0]["resolved"] is True
        assert ew.spans("[[doi:10.1/a]]", NAMES, {})[0]["resolved"] is False

    def test_plain_text_survives_intact(self) -> None:
        out = ew.spans("nothing inline here", {}, {})
        assert out == [{"t": "text", "v": "nothing inline here"}]

    def test_text_is_not_lost_at_either_end(self) -> None:
        out = ew.spans("**a** middle **b**", {}, {})
        assert "".join(sp.get("v", "") for sp in out) == "a middle b"
        assert [sp["t"] for sp in out] == ["strong", "text", "strong"]


class TestParseExtracts:
    TEXT = (
        "# Extracts\n\n"
        "## doi:10.1/a\n"
        "https://example.org/a — accessed 2026-09-01\n"
        '- "The agent calls ObsPy to fetch waveforms."\n'
        '- "It then runs PhaseNet."\n'
        "- maturity_claimed: M2\n"
        '- limitation: "single region"\n'
        "- NOT FOUND: any statement about runtime cost\n\n"
        "## doi:10.1/b\n"
        "https://example.org/b\n"
        '- "A single quote."\n'
    )

    def test_one_entry_per_core_paper(self) -> None:
        e = ew.parse_extracts(self.TEXT)
        assert set(e) == {"doi:10.1/a", "doi:10.1/b"}

    def test_the_source_url_and_its_note_are_split(self) -> None:
        e = ew.parse_extracts(self.TEXT)["doi:10.1/a"]
        assert e["source"] == "https://example.org/a"
        assert e["source_note"] == "accessed 2026-09-01"

    def test_quotes_keep_their_order_and_lose_their_quote_marks(self) -> None:
        e = ew.parse_extracts(self.TEXT)["doi:10.1/a"]
        assert e["quotes"] == [
            "The agent calls ObsPy to fetch waveforms.",
            "It then runs PhaseNet.",
        ]

    def test_prefixed_bullets_are_pulled_into_their_own_fields(self) -> None:
        e = ew.parse_extracts(self.TEXT)["doi:10.1/a"]
        assert e["maturity_claimed"] == "M2"
        assert e["limitation"] == "single region"
        assert e["not_found"] == ["any statement about runtime cost"]
        # ...and are not also counted as quotes.
        assert "M2" not in e["quotes"]

    def test_a_missing_note_is_empty_not_absent(self) -> None:
        assert ew.parse_extracts(self.TEXT)["doi:10.1/b"]["source_note"] == ""


class TestParseAnnotations:
    def test_an_entry_is_claimed_by_the_key_on_its_first_line(self) -> None:
        notes = ew.parse_annotations("- [[doi:10.1/a]] An agent that picks phases.\n")
        assert notes == {"doi:10.1/a": "An agent that picks phases."}

    def test_a_context_marker_is_stripped(self) -> None:
        notes = ew.parse_annotations("- [context] [[doi:10.1/b]] A context source.\n")
        assert notes["doi:10.1/b"] == "A context source."

    def test_an_entry_with_no_key_is_skipped_rather_than_guessed_at(self) -> None:
        # A missing blurb costs a sentence; a wrong one costs the point of the file.
        assert ew.parse_annotations("- A blurb with no citation at all.\n") == {}

    def test_continuation_lines_do_not_start_a_new_entry(self) -> None:
        notes = ew.parse_annotations("- [[doi:10.1/a]] First line.\n  continued here.\n")
        assert set(notes) == {"doi:10.1/a"}

    def test_only_the_summary_after_the_year_is_kept(self) -> None:
        # Everything before it — system name, title, year, venue — is already on
        # the paper record, and repeating the title under the title is noise.
        entry = (
            "- [context] TADI: Tool-Augmented Drilling Intelligence (2026, arXiv). "
            "natural-language question answering over drilling data. [[doi:10.1/a]]\n"
        )
        assert (
            ew.parse_annotations(entry)["doi:10.1/a"]
            == "natural-language question answering over drilling data."
        )

    def test_a_core_entry_ending_at_its_venue_yields_no_summary(self) -> None:
        # Core prose lives in the papers.md extract block, not in this list.
        entry = "- **TRACE.** TRACE: A Multi-Agent System (2026, arXiv). [[doi:10.1/a]]\n"
        assert ew.parse_annotations(entry)["doi:10.1/a"] == ""

    def test_bold_markers_are_stripped_not_carried_through(self) -> None:
        # The value renders as text on the paper record, where a literal
        # `**TRACE.**` is worse than no emphasis at all.
        entry = "- **TRACE.** A title (2026). **emphasised** summary. [[doi:10.1/a]]\n"
        assert ew.parse_annotations(entry)["doi:10.1/a"] == "emphasised summary."


class TestFacet:
    def test_the_declared_order_is_kept_regardless_of_counts(self) -> None:
        f = ew.facet(Counter({"M2": 5, "M0": 1}), ["M0", "M1", "M2"], 6)
        assert [i["label"] for i in f] == ["M0", "M1", "M2"]

    def test_a_declared_value_nobody_used_still_gets_a_row(self) -> None:
        # `M5: 0` is the finding: nothing in this corpus is in routine use.
        f = ew.facet(Counter({"M2": 5}), ["M2", "M5"], 5)
        assert {i["label"]: i["n"] for i in f}["M5"] == 0

    def test_keep_zeros_off_drops_the_unused_rows(self) -> None:
        f = ew.facet(Counter({"M2": 5}), ["M2", "M5"], 5, keep_zeros=False)
        assert [i["label"] for i in f] == ["M2"]

    def test_an_undeclared_value_is_appended_not_dropped(self) -> None:
        # A schema change should surface as an unordered tail, never as a vanished row.
        f = ew.facet(Counter({"M2": 1, "M9": 2}), ["M2"], 3)
        assert [i["label"] for i in f] == ["M2", "M9"]

    def test_share_is_against_the_population_not_the_sum_of_bars(self) -> None:
        # Techniques are multi-valued, so shares must not be presented as adding to 1.
        f = ew.facet(Counter({"a": 3, "b": 3}), ["a", "b"], 4)
        assert [i["share"] for i in f] == [0.75, 0.75]

    def test_a_zero_population_does_not_divide_by_zero(self) -> None:
        assert ew.facet(Counter(), ["a"], 0) == [{"label": "a", "n": 0, "share": 0.0}]


class TestMulti:
    def test_a_semicolon_cell_counts_once_per_value(self) -> None:
        c = ew.multi([{"t": "a;b"}, {"t": "b"}], "t")
        assert c == Counter({"b": 2, "a": 1})

    def test_whitespace_and_empty_values_are_ignored(self) -> None:
        assert ew.multi([{"t": " a ; ; b "}], "t") == Counter({"a": 1, "b": 1})

    def test_an_empty_cell_contributes_nothing(self) -> None:
        assert ew.multi([{"t": ""}], "t") == Counter()


class TestModelFamilies:
    @pytest.mark.parametrize(
        ("raw", "families"),
        [
            ("not stated", ["not stated"]),
            ("GPT-4o", ["GPT / OpenAI"]),
            ("ChatGPT", ["GPT / OpenAI"]),
            ("Claude 3.5 Sonnet", ["Claude"]),
            ("Gemini 1.5 Pro", ["Gemini"]),
            ("Llama 3.1", ["Llama"]),
            ("DeepSeek-V3", ["DeepSeek"]),
            ("some in-house model", ["other named"]),
        ],
    )
    def test_families_group_the_field_most_often_left_blank(
        self, raw: str, families: list[str]
    ) -> None:
        assert ew.model_families(raw) == families

    @pytest.mark.parametrize("raw", ["Qwen2.5-72B", "Qwen3-4B", "Qwen3-VL-8B", "Qwen 2"])
    def test_qwen_is_grouped_under_its_canonical_spelling(self, raw: str) -> None:
        # Was a strict xfail: `\bQwen\b` could not match any spelling that runs
        # straight into a digit, so both core Qwen systems in v0.5 — GeoMind
        # (Qwen3-4B) and LandslideAgent (Qwen3-VL-8B) — were counted as
        # `other named`. Fixed with a lookahead rather than by dropping the
        # boundary, which would have matched `Qwenzhou`.
        assert ew.model_families(raw) == ["Qwen"]

    def test_a_family_prefix_does_not_swallow_an_unrelated_word(self) -> None:
        assert ew.model_families("Qwenzhou Institute in-house model") == ["other named"]

    def test_not_stated_is_matched_at_the_start_only(self) -> None:
        # "a model, not stated which" is a named-model row with a hedge, not a silence.
        assert ew.model_families("a model, not stated which") == ["other named"]

    def test_every_family_named_is_returned_not_just_the_first(self) -> None:
        # The bug this replaced: single-valued, it returned the first match from
        # an ordered list, so a paper ablating across backbones was counted as a
        # GPT paper and the facet read as market share.
        assert ew.model_families("GPT-5 (primary); Claude-4 and Gemini-3 as alternatives") == [
            "GPT / OpenAI",
            "Claude",
            "Gemini",
        ]

    def test_families_come_back_in_the_declared_order(self) -> None:
        # Not the order the cell happens to name them in, so two papers naming
        # the same pair produce the same list and the facet is groupable.
        assert ew.model_families("Gemini 2.5 Pro then GPT-4o") == ["GPT / OpenAI", "Gemini"]

    def test_a_silent_cell_never_appears_beside_a_family(self) -> None:
        # `not stated` is exclusive: a cell that names nothing names nothing.
        assert ew.model_families("") == ["not stated"]
        assert "not stated" not in ew.model_families("GPT-4o and Qwen3-4B")


class TestSourceTypeOf:
    def test_the_runs_own_value_wins(self) -> None:
        assert ew.source_type_of("preprint", "article") == "preprint"

    def test_openalex_fills_a_blank(self) -> None:
        # The column is blank on 108 of 155 rows, so without the fallback the
        # facet is two-thirds empty.
        assert ew.source_type_of("", "conference-paper") == "conference paper"

    def test_the_two_vocabularies_are_normalised_to_one_label(self) -> None:
        # Left alone, `article` and `journal-article` are the same kind on two
        # separate bars.
        assert ew.source_type_of("journal-article", "") == ew.source_type_of("", "article")

    def test_an_unrecognised_value_passes_through(self) -> None:
        # So a new value shows up as its own bar rather than being folded into
        # the wrong bucket.
        assert ew.source_type_of("", "monograph") == "monograph"

    def test_silence_is_recorded_as_such(self) -> None:
        assert ew.source_type_of("", "") == "not stated"


class TestFrameworksOf:
    def test_a_framework_is_found_in_free_text(self) -> None:
        assert "LangGraph" in ew.frameworks_of("Built with LangGraph and ObsPy")

    def test_several_are_found_at_once(self) -> None:
        found = ew.frameworks_of("ObsPy; SeisBench; DuckDB")
        assert {"ObsPy", "SeisBench", "DuckDB"} <= set(found)

    def test_an_acronym_is_matched_case_sensitively(self) -> None:
        # Otherwise "iris" the flower and "eclipse" the event become tool citations.
        assert "IRIS" in ew.frameworks_of("Data from IRIS")
        assert "IRIS" not in ew.frameworks_of("the iris of the eye")

    def test_a_lowercase_name_is_bounded(self) -> None:
        # `cline` must not be found inside `decline`.
        assert "cline" in ew.frameworks_of("driven from cline")
        assert "cline" not in ew.frameworks_of("a decline in coverage")

    def test_nothing_is_found_in_unrelated_text(self) -> None:
        assert ew.frameworks_of("a bespoke script") == []


class TestBuild:
    @pytest.fixture
    def built(self, make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> ew.Json:
        out = make_run()
        audit.main(["--out", str(out)])  # build() reads the audit.md this writes
        capsys.readouterr()
        return ew.build(out)

    def test_every_paper_carries_a_reference_number(self, built: ew.Json) -> None:
        # The report cites by number and the list is where a number is looked
        # up, so a paper without one breaks the link in both directions. This
        # field was once dropped from the paper record while the prose kept
        # citing it, and the only symptom was `undefined` in the list.
        refs = [p["ref"] for p in built["papers"]]
        assert refs == list(range(1, len(built["papers"]) + 1))

    def test_every_citation_resolves_to_a_reference_number(self, built: ew.Json) -> None:
        refs = {p["ref"] for p in built["papers"]}
        cited = [
            sp["label"]
            for section in built["report"]
            for block in section["blocks"]
            if block["kind"] == "para"
            for sp in block["spans"]
            if sp["t"] == "cite" and sp["resolved"]
        ]
        assert cited, "the fixture's report cites nothing, so this proves nothing"
        assert all(label.isdigit() and int(label) in refs for label in cited)

    def test_the_run_block_counts_rather_than_quotes(self, built: ew.Json) -> None:
        run = built["run"]
        assert run["admitted"] == len(ADMITTED)
        assert run["core"] == 1
        assert run["context"] == len(ADMITTED) - 1
        assert run["version"] == "v9.9"

    def test_the_false_negative_rate_is_recomputed_from_screening(self, built: ew.Json) -> None:
        # Not read out of RUN.md prose: a below-cut record that screening admitted is
        # by definition a false negative, so it is counted here.
        assert built["run"]["false_negatives"] == 0
        assert built["run"]["audit_sample"] == 40

    def test_every_admitted_paper_is_exported(self, built: ew.Json) -> None:
        assert {p["key"] for p in built["papers"]} == set(ADMITTED)

    def test_the_core_paper_carries_its_extract(self, built: ew.Json) -> None:
        core = next(p for p in built["papers"] if p["key"] == CORE_KEY)
        assert core["extract"] is not None
        assert core["extract"]["quotes"]

    def test_a_paper_carries_its_annotation(self, built: ew.Json) -> None:
        core = next(p for p in built["papers"] if p["key"] == CORE_KEY)
        assert core["annotation"] == "An agent that picks seismic phases."

    def test_the_derived_framework_facet_is_read_from_tools_used(self, built: ew.Json) -> None:
        core = next(p for p in built["papers"] if p["key"] == CORE_KEY)
        assert set(core["frameworks"]) == {"ObsPy", "SeisBench"}

    def test_report_sections_are_grouped_and_tagged(self, built: ew.Json) -> None:
        ids = [s["id"] for s in built["report"]]
        assert "00_executive_summary" in ids
        paras = [b for s in built["report"] for b in s["blocks"] if b["kind"] == "para"]
        assert paras
        assert all(b["tag"] in ("Certain", "Likely", "Absent-searched") for b in paras)

    def test_no_citation_is_left_unresolved(self, built: ew.Json) -> None:
        unresolved = [
            sp
            for s in built["report"]
            for b in s["blocks"]
            if b["kind"] == "para"
            for sp in b["spans"]
            if sp["t"] == "cite" and not sp["resolved"]
        ]
        assert unresolved == []

    def test_the_maturity_rubric_travels_with_the_counts(self, built: ew.Json) -> None:
        # So the page can say what a level means beside the count of it.
        assert set(built["rubric"]) == {"M0", "M1", "M2", "M3", "M4", "M5"}

    def test_a_run_with_no_papers_refuses_to_export(self, tmp_path: Path) -> None:
        with pytest.raises(SystemExit, match="nothing to export"):
            ew.build(tmp_path)


class TestMain:
    def test_it_writes_the_single_document_the_front_end_reads(
        self, make_run: RunFactory, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_run()
        audit.main(["--out", str(out)])
        capsys.readouterr()
        target = tmp_path / "web" / "src" / "data" / "landscape.web.json"
        assert ew.main(["--out", str(out), "--to", str(target)]) == 0
        assert target.exists()
        assert target.read_text(encoding="utf-8").endswith("\n")

        # AGENTS.md B3: progress goes to stderr, and stdout stays empty. Only
        # audit.py writes to stdout, because only its table is meant to be piped
        # into RUN.md — an export summary landing there would be pasted into a
        # run record as though it were part of the contract check.
        captured = capsys.readouterr()
        assert "admitted" in captured.err
        assert captured.out == ""


class TestSummary:
    def test_a_summary_that_repeats_the_task_is_dropped(self) -> None:
        # Both are one clause written from the same abstract, so on many context
        # rows they come out identical and the record showed the sentence twice.
        task = "agent-driven reservoir simulation workflow automation"
        assert ew.summary(f"{task}.", task) == ""

    def test_the_comparison_ignores_case_spacing_and_full_stops(self) -> None:
        assert (
            ew.summary("History  matching of a reservoir.", "history matching of a reservoir") == ""
        )

    def test_a_summary_that_adds_something_is_kept(self) -> None:
        kept = ew.summary("automation through MCP servers.", "history matching")
        assert kept == "automation through MCP servers."


class TestParseUnreachable:
    TEXT = (
        "# Unreachable\n\n"
        "## Admitted with no abstract retrievable\n\n"
        "| identity_key | title |\n|---|---|\n"
        "| `doi:10.1/a` | A |\n| `doi:10.1/b` | B |\n\n"
        "## Screened core, demoted to context for want of full text\n\n"
        "| identity_key | venue | what was obtained |\n|---|---|---|\n"
        "| `doi:10.1/c` | X | abstract only |\n"
        "| `doi:10.1/d` | Y | abstract only |\n"
        "| `doi:10.1/e` | Z | abstract only |\n\n"
        "### A prose subsection with no table\n\nWords only.\n\n"
        "## Second demotion pass\n\nEAGE EarthDoc three times, IEEE CAIT. No table.\n"
    )

    def test_the_two_tables_that_exist_are_counted(self) -> None:
        counts = ew.parse_unreachable(self.TEXT)
        assert counts["no_abstract"] == 2
        assert counts["full_text_refused"] == 3

    def test_header_and_separator_rows_are_not_counted_as_records(self) -> None:
        assert ew.parse_unreachable(self.TEXT)["no_abstract"] == 2

    def test_a_later_section_does_not_leak_into_an_earlier_count(self) -> None:
        # The second demotion pass is prose, and its rows must not be attributed
        # to the table above it.
        assert ew.parse_unreachable(self.TEXT)["full_text_refused"] == 3

    def test_a_missing_file_yields_no_counts_rather_than_zeros(self) -> None:
        # The summary table renders a count it does not have as an em dash, so
        # absence has to stay distinguishable from a measured zero.
        assert ew.parse_unreachable("") == {}


class TestReadEnrichment:
    def test_a_missing_file_is_not_an_error(self, tmp_path: Path) -> None:
        # The geography facet is the only thing needing a network call, so a run
        # without it stays complete and the page omits the panel.
        countries, journals, types = ew.read_enrichment(tmp_path)
        assert (countries, journals, types) == ({}, {}, {})

    def test_countries_are_split_and_trimmed(self, tmp_path: Path) -> None:
        target = tmp_path / "enrichment" / "countries.csv"
        target.parent.mkdir(parents=True)
        target.write_text(
            "identity_key,countries,openalex_journal,openalex_type,resolved\n"
            'doi:10.1/a,"CH; DE ; FR",Nature,article,yes\n'
            "doi:10.1/b,,,conference-paper,yes\n",
            encoding="utf-8",
        )
        countries, journals, types = ew.read_enrichment(tmp_path)
        assert countries["doi:10.1/a"] == ["CH", "DE", "FR"]
        assert countries["doi:10.1/b"] == []
        assert journals["doi:10.1/a"] == "Nature"
        assert types["doi:10.1/b"] == "conference-paper"


class TestFunnel:
    @pytest.fixture
    def funnel(self, make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> list[ew.Json]:
        out = make_run()
        audit.main(["--out", str(out)])
        capsys.readouterr()
        rows: list[ew.Json] = ew.build(out)["funnel"]
        return rows

    def test_it_ends_on_the_access_split(self, funnel: list[ew.Json]) -> None:
        assert funnel[-2]["label"] == "Full text read"
        assert funnel[-1]["label"] == "Full text not obtained"

    def test_the_read_and_unread_rows_sum_to_the_admitted_row(self, funnel: list[ew.Json]) -> None:
        admitted = next(r for r in funnel if r["label"].startswith("Admitted"))
        assert funnel[-2]["n"] + funnel[-1]["n"] == admitted["n"]

    def test_the_paywall_question_is_answered_with_a_caveat_not_a_number(
        self, funnel: list[ew.Json]
    ) -> None:
        # papers.csv has no paywall column and `abstract-only` covers paywalls,
        # refused delivery, software deposits and missing abstracts alike. The
        # row must not invent a figure for paywalls alone.
        note = funnel[-1]["note"]
        assert "cannot put a number on paywalls" in note

    def test_every_row_names_what_it_counts(self, funnel: list[ew.Json]) -> None:
        assert all(row["what"] for row in funnel)


class TestParseShortlist:
    TEXT = (
        "# Shortlist — 4 of 100 harvested records\n\n"
        "## Core (solid-earth / subsurface) — 3\n\n"
        "### doi:10.1/a\n"
        "**A title** (2026) — n/a · cites 0 · score 31 (strong 6) "
        "· core/reservoir_engineering · doi:10.1/a\n"
        "signals: some;patterns\n\n"
        "### doi:10.1/b\n"
        "**B title** (2026) — n/a · cites 2 · score 9 (strong 1) "
        "· core/seismology · doi:10.1/b\n\n"
        "### doi:10.1/c\n"
        "**C title** (2025) — n/a · cites 1 · score 7 (strong 2) "
        "· core/reservoir_engineering · doi:10.1/c\n\n"
        "## Periphery — 1\n\n"
        "### doi:10.1/d\n"
        "**D title** (2026) — n/a · cites 0 · score 5 (strong 1) "
        "· periphery/earth_observation · doi:10.1/d\n"
    )

    def test_core_groups_are_counted(self) -> None:
        counts, _ = ew.parse_shortlist(self.TEXT)
        assert counts["reservoir_engineering"] == 2
        assert counts["seismology"] == 1

    def test_periphery_is_not_counted_as_a_core_group(self) -> None:
        # The rate this feeds is admitted-over-shortlisted for the ten core
        # subfields; a periphery group has no admitted rows to divide into.
        counts, groups = ew.parse_shortlist(self.TEXT)
        assert "earth_observation" not in counts
        assert "doi:10.1/d" not in groups

    def test_each_record_maps_to_the_group_it_came_in_under(self) -> None:
        # Used to size the taxonomy mismatch: the query family that found a
        # record is not the subfield screening assigned it to.
        _, groups = ew.parse_shortlist(self.TEXT)
        assert groups["doi:10.1/a"] == "reservoir_engineering"
        assert groups["doi:10.1/b"] == "seismology"

    def test_a_signals_line_does_not_claim_the_next_entry(self) -> None:
        # `signals:` lines carry raw regex that can contain anything, so a group
        # tag is only read from the line directly under its own heading.
        counts, _ = ew.parse_shortlist(self.TEXT)
        assert sum(counts.values()) == 3

    def test_a_missing_file_yields_nothing(self) -> None:
        assert ew.parse_shortlist("") == (Counter(), {})


class TestFieldRates:
    @pytest.fixture
    def fields(self, make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> list[ew.Json]:
        out = make_run()
        audit.main(["--out", str(out)])
        capsys.readouterr()
        rows: list[ew.Json] = ew.build(out)["fields"]
        return rows

    def test_a_field_with_no_shortlist_has_no_rate_rather_than_zero(
        self, fields: list[ew.Json]
    ) -> None:
        # A missing denominator must render as an em dash. A 0% admission rate
        # would be a measurement, and this is not one.
        for row in fields:
            if row["shortlisted"] == 0:
                assert row["admitted_share"] is None

    def test_the_rate_is_admitted_over_shortlisted(self, fields: list[ew.Json]) -> None:
        for row in fields:
            if row["shortlisted"]:
                assert row["admitted_share"] == pytest.approx(row["n"] / row["shortlisted"])

    def test_own_query_never_exceeds_the_admitted_count(self, fields: list[ew.Json]) -> None:
        assert all(row["from_own_query"] <= row["n"] for row in fields)


class TestFrameworksCoverage:
    @pytest.fixture
    def coverage(self, make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> ew.Json:
        out = make_run()
        audit.main(["--out", str(out)])
        capsys.readouterr()
        built: ew.Json = ew.build(out)["frameworks_coverage"]
        return built

    def test_the_named_subset_never_exceeds_its_population(self, coverage: ew.Json) -> None:
        # This is the denominator the framework panel publishes, so it has to be
        # a subset by construction — a floor cannot exceed the whole.
        assert coverage["core_named"] <= coverage["core_total"]
        assert coverage["named"] <= coverage["total"]
        assert coverage["context_any_tool"] <= coverage["context_total"]

    def test_naming_a_framework_implies_naming_a_tool(self, coverage: ew.Json) -> None:
        assert coverage["core_named"] <= coverage["core_any_tool"]
