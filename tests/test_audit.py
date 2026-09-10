"""audit.py is the contract. These tests keep each of its checks load-bearing.

One baseline that passes all 26, then one mutation per check that should catch it.
A check that stops failing when its condition is broken has become decoration, and
that is invisible from a green run — which is the exact failure the script was
written to replace.
"""

from __future__ import annotations

import csv
from collections.abc import Callable
from pathlib import Path

import pytest

import audit
from conftest import ADMITTED, CORE_KEY, N_AUDIT

RunFactory = Callable[[], Path]


def results(out: Path, capsys: pytest.CaptureFixture[str]) -> dict[str, str]:
    """Run audit.py over a directory and return {check name: PASS|FAIL}."""
    audit.main(["--out", str(out)])
    table = capsys.readouterr().out
    rows: dict[str, str] = {}
    for line in table.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[1] in ("PASS", "FAIL"):
            rows[cells[0]] = cells[1]
    return rows


def rewrite_csv(path: Path, mutate: Callable[[list[dict[str, str]]], None]) -> None:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        rows = list(reader)
    mutate(rows)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)


def test_baseline_run_passes_every_check(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    assert audit.main(["--out", str(out)]) == 0
    table = capsys.readouterr().out
    failures = [ln for ln in table.splitlines() if "| FAIL |" in ln]
    assert not failures, "baseline fixture should satisfy the contract:\n" + "\n".join(failures)


def test_baseline_exercises_the_whole_battery(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    # A guard on the guard: if a check is added and the fixture is not extended, the
    # mutation tests below still pass while the new check is never exercised.
    assert len(results(make_run(), capsys)) == 26


def test_audit_md_is_written(make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> None:
    out = make_run()
    audit.main(["--out", str(out)])
    capsys.readouterr()
    text = (out / "audit.md").read_text(encoding="utf-8")
    assert text.startswith("# Self-audit")
    assert "| PASS |" in text


def test_missing_file_is_caught(make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> None:
    out = make_run()
    (out / "unreachable.md").unlink()
    assert results(out, capsys)["Required files present"] == "FAIL"


def test_nonzero_exit_on_failure(make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> None:
    out = make_run()
    (out / "unreachable.md").unlink()
    assert audit.main(["--out", str(out)]) == 1
    capsys.readouterr()


def test_empty_papers_does_not_pass_vacuously(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    # The failure mode this guards: with no admitted sources, every downstream check
    # holds trivially and the table reads as a clean run that produced nothing.
    out = make_run()
    rewrite_csv(out / "papers.csv", lambda rows: rows.clear())
    r = results(out, capsys)
    assert r["papers.csv is non-empty"] == "FAIL"


def test_zero_result_query_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def blank(rows: list[dict[str, str]]) -> None:
        rows[0]["status"] = "zero"

    rewrite_csv(out / "queries.csv", blank)
    assert results(out, capsys)["No silently-empty queries"] == "FAIL"


def test_orphan_screening_decision_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def add_orphan(rows: list[dict[str, str]]) -> None:
        rows.append({**rows[0], "identity_key": "doi:10.1000/never-harvested"})

    rewrite_csv(out / "screening.csv", add_orphan)
    r = results(out, capsys)
    assert r["Every screening decision traces to a harvested record"] == "FAIL"


def test_invalid_decision_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def bad(rows: list[dict[str, str]]) -> None:
        rows[0]["decision"] = "maybe"

    rewrite_csv(out / "screening.csv", bad)
    assert results(out, capsys)["Screening decisions are in/out"] == "FAIL"


def test_regenerated_shortlist_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    # Re-running triage.py after screening rewrites shortlist.md underneath decisions
    # made against the previous one. Without this check the run looks finished.
    out = make_run()
    (out / "shortlist.md").write_text(
        "# Shortlist\n\n### doi:10.1000/newly-shortlisted\n**A record**\n", encoding="utf-8"
    )
    assert results(out, capsys)["Every shortlist record was screened"] == "FAIL"


def test_stale_audit_sample_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "audit_sample.md").write_text(
        "# Recall audit\n\n### doi:10.1000/other\n", encoding="utf-8"
    )
    r = results(out, capsys)
    assert r["Audit sample matches the screened audit rows"] == "FAIL"


def test_undersized_recall_audit_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def thin(rows: list[dict[str, str]]) -> None:
        kept = 0
        for r in rows:
            if r["from_audit_sample"] == "yes":
                kept += 1
                if kept > 10:
                    r["from_audit_sample"] = "no"

    rewrite_csv(out / "screening.csv", thin)
    assert results(out, capsys)["Recall audit performed"] == "FAIL"


def test_high_false_negative_rate_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def admit_below_cut(rows: list[dict[str, str]]) -> None:
        flipped = 0
        for r in rows:
            if r["from_audit_sample"] == "yes" and flipped < N_AUDIT // 4:
                r["decision"] = "in"
                flipped += 1

    rewrite_csv(out / "screening.csv", admit_below_cut)
    r = results(out, capsys)
    assert r["False-negative rate acceptable"] == "FAIL"
    # Flipping decisions to `in` also breaks the admitted set, which is the point:
    # a false negative is a record that should have been in papers.csv.
    assert r["Admitted set matches screening"] == "FAIL"


def test_unparseable_corpus_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "screened.csv").write_text("identity_key,title\n", encoding="utf-8")
    r = results(out, capsys)
    assert r["screened.csv parses and is non-empty"] == "FAIL"


def test_untriaged_non_grey_record_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    # A record in the corpus with no triage row is fine only if it arrived via the
    # grey/snowball pass. An API record missing from triage.csv means the ranking
    # was run against a different corpus than the one screened.
    out = make_run()

    def add_untriaged(rows: list[dict[str, str]]) -> None:
        rows.append({**rows[0], "identity_key": "doi:10.1000/api-but-untriaged"})

    rewrite_csv(out / "screened.csv", add_untriaged)
    assert results(out, capsys)["triage.csv covers the API corpus"] == "FAIL"


def test_grey_extras_are_allowed(make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> None:
    # The other side of the same check: web/snowball rows are appended after triage
    # by design, so they must not be reported as a coverage gap.
    out = make_run()

    def add_grey(rows: list[dict[str, str]]) -> None:
        rows.append(
            {**rows[0], "identity_key": "doi:10.1000/grey", "source_apis": "web", "query_ids": "w1"}
        )

    rewrite_csv(out / "screened.csv", add_grey)
    assert results(out, capsys)["triage.csv covers the API corpus"] == "PASS"


def test_api_error_flood_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def all_errors(rows: list[dict[str, str]]) -> None:
        template = dict(rows[0])
        rows.clear()
        for i in range(5):
            rows.append({**template, "query_id": f"q{i:03d}:openalex", "status": "error"})

    rewrite_csv(out / "queries.csv", all_errors)
    assert results(out, capsys)["API errors within tolerance"] == "FAIL"


def test_title_only_corpus_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def strip_abstracts(rows: list[dict[str, str]]) -> None:
        for r in rows:
            r["abstract"] = ""

    rewrite_csv(out / "screened.csv", strip_abstracts)
    assert results(out, capsys)["Corpus carries abstracts"] == "FAIL"


def test_no_screening_decisions_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    rewrite_csv(out / "screening.csv", lambda rows: rows.clear())
    assert results(out, capsys)["screening.csv is non-empty"] == "FAIL"


def test_schema_drift_in_papers_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    with (out / "papers.csv").open(encoding="utf-8") as f:
        body = f.read()
    (out / "papers.csv").write_text(body.replace('"tier"', '"tier_v2"', 1), encoding="utf-8")
    r = results(out, capsys)
    assert r["papers.csv columns match SCHEMA"] == "FAIL"


def test_duplicate_paper_row_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    rewrite_csv(out / "papers.csv", lambda rows: rows.append(dict(rows[0])))
    assert results(out, capsys)["No duplicate rows in papers.csv"] == "FAIL"


def test_off_rubric_maturity_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def bad(rows: list[dict[str, str]]) -> None:
        rows[0]["maturity_demonstrated"] = "M7"

    rewrite_csv(out / "papers.csv", bad)
    assert results(out, capsys)["Maturity values are from the rubric"] == "FAIL"


def test_invalid_tier_is_caught(make_run: RunFactory, capsys: pytest.CaptureFixture[str]) -> None:
    out = make_run()

    def bad(rows: list[dict[str, str]]) -> None:
        rows[0]["tier"] = "important"

    rewrite_csv(out / "papers.csv", bad)
    assert results(out, capsys)["Tier values valid"] == "FAIL"


def test_abstract_only_core_paper_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()

    def bad(rows: list[dict[str, str]]) -> None:
        for r in rows:
            if r["tier"] == "core":
                r["access_status"] = "abstract-only"

    rewrite_csv(out / "papers.csv", bad)
    assert results(out, capsys)["Core tier was actually deep-read"] == "FAIL"


def test_missing_extract_block_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "papers.md").write_text("# Extracts\n\nnothing here\n", encoding="utf-8")
    assert results(out, capsys)["Every core paper has an extract block"] == "FAIL"


def test_untagged_paragraph_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "report" / "01_techniques.md").write_text(
        "# Techniques\n\n"
        "Tool-calling and planning are the two techniques named by the admitted "
        "systems, and this paragraph runs well past twenty-five words without ever "
        "saying how certain any of it is meant to be.\n",
        encoding="utf-8",
    )
    r = results(out, capsys)
    assert r["Substantive paragraphs carry an evidence tag"] == "FAIL"


def test_prose_under_a_heading_is_not_exempt(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    # The bug this pins: a block whose first line is a heading was once skipped
    # wholesale, exempting every untagged word beneath it from the tag check.
    out = make_run()
    (out / "report" / "01_techniques.md").write_text(
        "# Techniques\n\n"
        "## A heading with no blank line beneath it\n"
        "Tool-calling and planning are the two techniques named by the admitted "
        "systems, and this paragraph runs well past twenty-five words without ever "
        "saying how certain any of it is meant to be.\n",
        encoding="utf-8",
    )
    r = results(out, capsys)
    assert r["Substantive paragraphs carry an evidence tag"] == "FAIL"


def test_unresolvable_citation_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "report" / "05_maturity.md").write_text(
        "# Maturity\n\n[Certain] The single core system reaches M2 on a reusable "
        "benchmark rather than on field data from any named site, and the authors "
        "say as much themselves [[doi:10.1000/not-in-papers]].\n",
        encoding="utf-8",
    )
    assert results(out, capsys)["Every citation resolves to papers.csv"] == "FAIL"


def test_absence_claim_without_a_query_id_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str]
) -> None:
    out = make_run()
    (out / "report" / "02_architectures.md").write_text(
        "# Architectures\n\n[Absent-searched] No multi-agent architecture appears in "
        "the admitted set, and nothing here says which query was the one that looked "
        "for it or how many records that query returned.\n",
        encoding="utf-8",
    )
    assert results(out, capsys)["Absence claims cite query ids"] == "FAIL"


@pytest.mark.parametrize(
    "phrase", ["promising", "great potential", "revolutionary", "paradigm shift", "cutting-edge"]
)
def test_promotional_framing_is_caught(
    make_run: RunFactory, capsys: pytest.CaptureFixture[str], phrase: str
) -> None:
    out = make_run()
    (out / "report" / "00_executive_summary.md").write_text(
        f"# Executive summary\n\n[Certain] The three admitted sources describe a "
        f"{phrase} direction, which is exactly the kind of wording this review is "
        f"not allowed to use about its own subject [[{CORE_KEY}]].\n",
        encoding="utf-8",
    )
    assert results(out, capsys)["No promotional framing"] == "FAIL"


def test_papers_md_annotations_cover_the_admitted_set(make_run: RunFactory) -> None:
    # Not an audit check, but the property 08_papers.md is exempted from the tag
    # check *for*: it is an annotated list, so every admitted key must appear in it.
    out = make_run()
    text = (out / "report" / "08_papers.md").read_text(encoding="utf-8")
    for key in ADMITTED:
        assert f"[[{key}]]" in text
