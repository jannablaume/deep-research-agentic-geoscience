"""gaps.py: the seven shapes a finished run records a gap in, and the three it must not.

What this battery is really pinning is the difference between **a gap in the literature**
and **an artefact of how the run was done**. Three of these tests exist because the first
pass over the real v0.5 run emitted the second kind: five periphery subfields reported as
empty categories, when a periphery group is empty by design.

The counting rule from AGENTS.md applies to every candidate: a count is emitted with its
denominator or it is not emitted at all.
"""

from __future__ import annotations

import csv
from collections.abc import Sequence
from pathlib import Path

import pytest

import gaps
from audit import PAPERS_COLS
from audit_tango import TRANSFER_COLS


def write_csv(path: Path, cols: Sequence[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(cols), quoting=csv.QUOTE_ALL, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def paper(key: str, **over: str) -> dict[str, str]:
    row = dict.fromkeys(PAPERS_COLS, "not stated")
    row.update(
        {
            "identity_key": key,
            "tier": "core",
            "system_id": key.rsplit("/", 1)[-1],
            "subfield": "seismology",
            "baseline": "PhaseNet",
            "held_out": "yes",
            "data_type": "benchmark",
            "maturity_claimed": "M2",
            "maturity_demonstrated": "M2",
            "author_stated_limitations": "single region",
            "access_status": "full-text",
        }
    )
    row.update(over)
    return row


def make_run(root: Path, papers: list[dict[str, str]], files: dict[str, str] | None = None) -> Path:
    out = root / "01_landscape" / "v9.9"
    (out / "report").mkdir(parents=True)
    write_csv(out / "papers.csv", PAPERS_COLS, papers)
    write_csv(
        out / "screening.csv",
        ["identity_key", "decision", "cut_reason", "subfield"],
        [
            {"identity_key": p["identity_key"], "decision": "in", "subfield": p["subfield"]}
            for p in papers
        ],
    )
    for name, text in (files or {}).items():
        path = out / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return out


def kinds(rows: list[gaps.Row], kind: str) -> list[gaps.Row]:
    return [r for r in rows if r["kind"] == kind]


class TestTheSevenShapes:
    def test_an_author_stated_limitation_becomes_a_candidate(self, tmp_path: Path) -> None:
        out = make_run(tmp_path, [paper("doi:10.1/a", author_stated_limitations="one basin only")])
        [c] = kinds(gaps.collect(out), "author-limitation")
        assert c["statement"] == "one basin only"
        assert c["evidence_ref"] == "doi:10.1/a"
        # Not a count, so no denominator — and `audit_gaps.py` checks the pair.
        assert c["count"] == "" and c["denominator"] == ""

    def test_an_absence_claim_carries_the_queries_that_looked(self, tmp_path: Path) -> None:
        out = make_run(
            tmp_path,
            [paper("doi:10.1/a")],
            {
                "report/01_techniques.md": "# T\n\n[Absent-searched] Nothing controls "
                "an instrument (`q001`, `q004`).\n"
            },
        )
        [c] = kinds(gaps.collect(out), "absence-claim")
        assert c["evidence_ref"] == "q001;q004"
        assert "[Absent-searched]" not in c["statement"]

    def test_an_unbacked_absence_claim_is_marked_rather_than_dropped(self, tmp_path: Path) -> None:
        # The run that wrote it should have failed its own audit. Recording it as
        # UNBACKED puts that in front of whoever reads the candidates.
        out = make_run(
            tmp_path,
            [paper("doi:10.1/a")],
            {"report/01_techniques.md": "# T\n\n[Absent-searched] Nobody does this.\n"},
        )
        assert kinds(gaps.collect(out), "absence-claim")[0]["evidence_ref"] == "UNBACKED"

    def test_a_silent_column_becomes_a_counted_candidate(self, tmp_path: Path) -> None:
        out = make_run(
            tmp_path,
            [
                paper("doi:10.1/a", base_model="GPT-4o"),
                paper("doi:10.1/b", base_model="not stated"),
            ],
        )
        [c] = [r for r in kinds(gaps.collect(out), "evidence-hole") if r["subject"] == "base_model"]
        assert (c["count"], c["denominator"]) == ("1", "2")

    def test_an_evaluation_with_no_baseline_is_counted_over_the_deep_read_set(
        self, tmp_path: Path
    ) -> None:
        out = make_run(
            tmp_path,
            [
                paper("doi:10.1/a", baseline="none"),
                paper("doi:10.1/b", baseline="PhaseNet"),
                paper("doi:10.1/c", tier="context", baseline="none"),
            ],
        )
        [c] = [r for r in kinds(gaps.collect(out), "evaluation-hole") if r["subject"] == "baseline"]
        # Denominator is the two core rows, not all three: a context row was never read.
        assert (c["count"], c["denominator"]) == ("1", "2")

    def test_a_subfield_with_sources_but_none_deep_read_is_a_candidate(
        self, tmp_path: Path
    ) -> None:
        out = make_run(
            tmp_path,
            [paper("doi:10.1/a", subfield="inversion", tier="context")],
        )
        [c] = kinds(gaps.collect(out), "empty-category")
        assert c["subject"] == "inversion"
        assert "none deep-read" in c["statement"]

    def test_an_unread_source_is_counted_with_its_denominator(self, tmp_path: Path) -> None:
        out = make_run(
            tmp_path,
            [paper("doi:10.1/a", access_status="abstract-only"), paper("doi:10.1/b")],
        )
        [c] = [
            r for r in kinds(gaps.collect(out), "unread-source") if r["subject"] == "abstract_only"
        ]
        assert (c["count"], c["denominator"]) == ("1", "2")

    def test_a_paywalled_row_contributes_what_reading_it_would_change(self, tmp_path: Path) -> None:
        out = make_run(
            tmp_path,
            [paper("doi:10.1/a")],
            {
                "paywalled.md": (
                    "| identity_key | title | url | venue | blocked_by | tried | local_pdf "
                    "| would_change |\n"
                    "|---|---|---|---|---|---|---|---|\n"
                    "| `doi:10.1/z` | A | u | v | paywall | DOI | no | would support a core "
                    "write-up |\n"
                    "| `doi:10.1/y` | B | u | v | paywall | DOI | no | nothing |\n"
                )
            },
        )
        rows = [
            r for r in kinds(gaps.collect(out), "unread-source") if r["subject"] != "abstract_only"
        ]
        # The `nothing` row is not a candidate: the run already said reading it changes
        # nothing, and repeating that as a gap would manufacture one.
        assert [r["subject"] for r in rows] == ["doi:10.1/z"]

    def test_a_touchpoint_nothing_claims_is_a_candidate(self, tmp_path: Path) -> None:
        out = make_run(tmp_path, [paper("doi:10.1/a")])
        write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [
                {
                    "identity_key": "doi:10.1/a",
                    "system_id": "a",
                    "tango_touchpoints": "config-generation",
                    "interface": "api",
                    "autonomy": "suggests",
                }
            ],
        )
        empty = {r["subject"] for r in kinds(gaps.collect(out), "empty-category")}
        assert "hpc-scale-out" in empty
        assert "config-generation" not in empty


class TestClaimGaps:
    def test_a_claimed_level_above_the_demonstrated_one_is_a_candidate(
        self, tmp_path: Path
    ) -> None:
        out = make_run(
            tmp_path, [paper("doi:10.1/a", maturity_claimed="M4", maturity_demonstrated="M2")]
        )
        [c] = kinds(gaps.collect(out), "claim-gap")
        assert "Claims M4" in c["statement"] and "demonstrates M2" in c["statement"]

    def test_a_free_text_assertion_over_a_floor_evaluation_is_a_candidate(
        self, tmp_path: Path
    ) -> None:
        # SCHEMA.md makes `maturity_claimed` the source's own words, so the columns are
        # usually not comparable as levels. On the real v0.5 run this is where all eleven
        # claim gaps came from, and the numeric comparison found none.
        out = make_run(
            tmp_path,
            [
                paper(
                    "doi:10.1/a",
                    maturity_claimed="the first application of MCP to computational seismology",
                    maturity_demonstrated="M1",
                )
            ],
        )
        [c] = kinds(gaps.collect(out), "claim-gap")
        assert c["statement"].startswith("Evaluation demonstrates M1")

    def test_a_claim_matched_by_the_evaluation_is_not_a_candidate(self, tmp_path: Path) -> None:
        out = make_run(
            tmp_path,
            [
                paper(
                    "doi:10.1/a", maturity_claimed="a benchmark result", maturity_demonstrated="M2"
                )
            ],
        )
        assert kinds(gaps.collect(out), "claim-gap") == []


class TestRunArtefactsAreNotGaps:
    def test_a_periphery_subfield_is_not_an_empty_category(self, tmp_path: Path) -> None:
        # The real failure: on v0.5 this emitted five of the six empty categories, which
        # was enough noise to bury the one that meant something. A periphery group is
        # harvested and counted, never admitted — reported as a gap it is an artefact of
        # the method, not a statement about the literature.
        out = make_run(tmp_path, [paper("doi:10.1/a")])
        write_csv(
            out / "screening.csv",
            ["identity_key", "decision", "cut_reason", "subfield"],
            [
                {"identity_key": "doi:10.1/a", "decision": "in", "subfield": "seismology"},
                {
                    "identity_key": "doi:10.1/p",
                    "decision": "out",
                    "cut_reason": "periphery",
                    "subfield": "ocean",
                },
            ],
        )
        assert "ocean" not in {r["subject"] for r in kinds(gaps.collect(out), "empty-category")}

    def test_a_core_subfield_that_was_screened_and_admitted_nothing_is_a_gap(
        self, tmp_path: Path
    ) -> None:
        out = make_run(tmp_path, [paper("doi:10.1/a")])
        write_csv(
            out / "screening.csv",
            ["identity_key", "decision", "cut_reason", "subfield"],
            [
                {"identity_key": "doi:10.1/a", "decision": "in", "subfield": "seismology"},
                {
                    "identity_key": "doi:10.1/m",
                    "decision": "out",
                    "cut_reason": "not-agentic",
                    "subfield": "mining",
                },
            ],
        )
        assert "mining" in {r["subject"] for r in kinds(gaps.collect(out), "empty-category")}


class TestEndToEnd:
    def test_ids_are_unique_across_runs_and_both_artifacts_are_written(
        self, tmp_path: Path
    ) -> None:
        # The report cites `c042` and it has to mean one thing, so ids are assigned over
        # the whole file rather than per run.
        first = make_run(tmp_path / "one", [paper("doi:10.1/a")])
        second = make_run(tmp_path / "two", [paper("doi:10.2/b")])
        out = tmp_path / "gapsrun"
        assert gaps.main(["--out", str(out), "--run", str(first), "--run", str(second)]) == 0

        rows = list(csv.DictReader((out / "gap_candidates.csv").open(encoding="utf-8")))
        assert len(rows) == len({r["candidate_id"] for r in rows})
        assert list(rows[0].keys()) == gaps.CANDIDATE_COLS
        assert {r["run"] for r in rows} == {"01_landscape/v9.9"}
        assert "Gap candidates" in (out / "gap_candidates.md").read_text(encoding="utf-8")

    def test_every_counted_candidate_carries_a_denominator(self, tmp_path: Path) -> None:
        out = make_run(tmp_path, [paper("doi:10.1/a"), paper("doi:10.1/b", tier="context")])
        for r in gaps.collect(out):
            assert bool(r["count"]) == bool(r["denominator"]), r

    def test_a_run_with_no_papers_is_refused(self, tmp_path: Path) -> None:
        out = tmp_path / "empty" / "v0.1"
        out.mkdir(parents=True)
        with pytest.raises(SystemExit, match=r"papers\.csv"):
            gaps.collect(out)
