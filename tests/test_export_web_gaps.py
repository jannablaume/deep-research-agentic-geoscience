"""export_web_gaps.py's own parsers: the gap blocks, the discard ledger, the
source-run table, and the evidence-key name lookup.

03 reads no `papers.csv` of its own kind — its only "corpus" is `gap_candidates.csv`
and `gaps.md` — so what needs testing here is different in shape from the other two
exporters: markdown block parsing rather than CSV counting, plus the accounting
identity `cited | discarded == every candidate` that `audit_gaps.py` also checks.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import export_web_gaps as ewg

RUN_MD = """outputs/03_gaps/v0.1-run2

## Run log

- date: 2026-09-11
- prompt: `.claude/skills/03_gaps/SKILL.md` v0.1
- prompt commit: e7010e1
- model: test

## Which runs were read, and at what state

| Run | Directory | Commit |
|---|---|---|
| 01_landscape | `outputs/01_landscape/v9.9` | `abc123` |
| 02_tango | `outputs/02_tango/v9.9` | `abc123` |

Some narrative text that must not be mistaken for a table row.

## Something else entirely
"""


def test_parse_run_table_reads_rows_under_the_named_heading() -> None:
    rows = ewg.parse_run_table(RUN_MD, "Which runs were read")
    assert rows == [
        {"run": "01_landscape", "directory": "outputs/01_landscape/v9.9", "commit": "abc123"},
        {"run": "02_tango", "directory": "outputs/02_tango/v9.9", "commit": "abc123"},
    ]


def test_parse_run_table_missing_heading_returns_empty() -> None:
    assert ewg.parse_run_table(RUN_MD, "Nonexistent heading") == []


GAPS_MD = """# Gaps the finished runs already contain

Intro paragraph, not a gap.

## G01 — A short gap about held-out data

- candidates: c001; c002
- runs: 01_landscape/v9.9; 02_tango/v9.9
- verdict: refuted
- evidence: doi:10.1/a; q041
- checked: 2026-09-11

[Certain] `held_out` is `not stated` on most admitted rows [doi:10.1/a].

[Certain] **Refuted as stated.** A handful of rows do record it.

## G02 — A second gap with one candidate

- candidates: c003
- runs: 01_landscape/v9.9
- verdict: confirmed-absent
- evidence: q041
- checked: 2026-09-11

[Absent-searched] Nothing found for q041.

## Discarded candidates

Every candidate in `gap_candidates.csv` is either cited by a gap above or listed here.

- c004 — `run-artefact`. Records the run's own access, not a limitation.
- c005 — `too-specific`. One system's own quirk with nothing else bearing on it.

### Candidates of refuted gaps

- c001; c002 — `refuted` (G01: A short gap about held-out data)
"""


def test_parse_gaps_md_extracts_gap_blocks() -> None:
    gaps, _discarded = ewg.parse_gaps_md(GAPS_MD)
    assert [g["id"] for g in gaps] == ["G01", "G02"]

    g1 = gaps[0]
    assert g1["title"] == "A short gap about held-out data"
    assert g1["candidates"] == ["c001", "c002"]
    assert g1["runs"] == ["01_landscape/v9.9", "02_tango/v9.9"]
    assert g1["verdict"] == "refuted"
    assert g1["evidence"] == ["doi:10.1/a", "q041"]
    assert g1["checked"] == "2026-09-11"
    assert len(g1["blocks"]) == 2
    assert g1["blocks"][0]["tag"] == "Certain"
    assert g1["blocks"][1]["spans"][0] == {"t": "strong", "v": "Refuted as stated."}

    g2 = gaps[1]
    assert g2["verdict"] == "confirmed-absent"
    assert g2["blocks"][0]["tag"] == "Absent-searched"


def test_parse_gaps_md_discard_ledger_excludes_the_refuted_gaps_subsection() -> None:
    _, discarded = ewg.parse_gaps_md(GAPS_MD)
    # Only the two flat bullets: c001/c002 are already cited by G01 and must not be
    # double-counted as discards via the "Candidates of refuted gaps" cross-reference.
    assert [d["id"] for d in discarded] == ["c004", "c005"]
    assert discarded[0]["reason"] == "run-artefact"
    assert discarded[1]["reason"] == "too-specific"


def test_build_end_to_end(tmp_path: Path) -> None:
    out = tmp_path / "v0.1-run2"
    out.mkdir()
    repo_root = tmp_path / "repo"
    (repo_root / "outputs/01_landscape/v9.9").mkdir(parents=True)
    (repo_root / "outputs/02_tango/v9.9").mkdir(parents=True)

    (repo_root / "outputs/01_landscape/v9.9/papers.csv").write_text(
        "identity_key,system_id\ndoi:10.1/a,TESTSYS\n", encoding="utf-8"
    )
    (repo_root / "outputs/02_tango/v9.9/papers.csv").write_text(
        "identity_key,system_id\n", encoding="utf-8"
    )

    (out / "gap_candidates.csv").write_text(
        "candidate_id,run,kind,subject,statement,evidence_ref,count,denominator\n"
        'c001,01_landscape/v9.9,evidence-hole,held_out,"most silent",q041,10,20\n'
        'c002,02_tango/v9.9,evidence-hole,held_out,"most silent",q041,,\n'
        'c003,01_landscape/v9.9,absence-claim,touchpoint,"none found",q041,,\n'
        'c004,01_landscape/v9.9,author-limitation,doi:10.1/a,"records access",doi:10.1/a,,\n'
        'c005,01_landscape/v9.9,author-limitation,doi:10.1/a,"quirk",doi:10.1/a,,\n',
        encoding="utf-8",
    )
    (out / "gaps.md").write_text(GAPS_MD, encoding="utf-8")
    (out / "RUN.md").write_text(RUN_MD.replace("v9.9", "v9.9"), encoding="utf-8")
    (out / "audit.md").write_text(
        "# Self-audit\n\n| Check | Result | Detail |\n|---|---|---|\n"
        "| gap_candidates.csv is non-empty | PASS | 5 candidates |\n",
        encoding="utf-8",
    )

    data = ewg.build(out, repo_root)

    assert data["candidates_total"] == 5
    assert data["gaps_total"] == 2
    assert data["cited_total"] == 3  # c001, c002, c003
    assert data["discarded_total"] == 2  # c004, c005
    assert data["unaccounted"] == []

    kinds = {k["label"]: k["n"] for k in data["kinds"]}
    assert kinds["evidence-hole"] == 2
    assert kinds["author-limitation"] == 2

    verdicts = {v["label"]: v["n"] for v in data["verdicts"]}
    assert verdicts["refuted"] == 1
    assert verdicts["confirmed-absent"] == 1

    g1 = next(g for g in data["gaps"] if g["id"] == "G01")
    assert g1["kinds"] == ["evidence-hole"]
    assert g1["evidence_named"] == [{"key": "doi:10.1/a", "name": "TESTSYS"}]


def test_build_flags_an_unaccounted_candidate(tmp_path: Path) -> None:
    out = tmp_path / "v0.1"
    out.mkdir()
    (out / "gap_candidates.csv").write_text(
        "candidate_id,run,kind,subject,statement,evidence_ref,count,denominator\n"
        'c001,01_landscape/v9.9,claim-gap,x,"y",q041,,\n'
        'c999,01_landscape/v9.9,claim-gap,x,"orphaned, cited nowhere",q041,,\n',
        encoding="utf-8",
    )
    (out / "gaps.md").write_text(
        "# Gaps\n\n## G01 — Only c001 is used\n\n"
        "- candidates: c001\n- runs: 01_landscape/v9.9\n- verdict: refuted\n"
        "- evidence: q041\n- checked: 2026-09-11\n\n[Certain] Something.\n",
        encoding="utf-8",
    )
    (out / "RUN.md").write_text("- date: 2026-09-11\n", encoding="utf-8")

    data = ewg.build(out, tmp_path)
    assert data["unaccounted"] == ["c999"]


def test_build_exits_when_gap_candidates_missing(tmp_path: Path) -> None:
    with pytest.raises(SystemExit):
        ewg.build(tmp_path / "empty", tmp_path)


def test_main_writes_json(tmp_path: Path) -> None:
    out = tmp_path / "v0.1"
    out.mkdir()
    (out / "gap_candidates.csv").write_text(
        "candidate_id,run,kind,subject,statement,evidence_ref,count,denominator\n"
        'c001,01_landscape/v9.9,claim-gap,x,"y",q041,,\n',
        encoding="utf-8",
    )
    (out / "gaps.md").write_text(
        "# Gaps\n\n## G01 — A gap\n\n"
        "- candidates: c001\n- runs: 01_landscape/v9.9\n- verdict: refuted\n"
        "- evidence: q041\n- checked: 2026-09-11\n\n[Certain] Something.\n",
        encoding="utf-8",
    )
    (out / "RUN.md").write_text("- date: 2026-09-11\n", encoding="utf-8")

    to = tmp_path / "written" / "gaps.web.json"
    rc = ewg.main(["--out", str(out), "--repo-root", str(tmp_path), "--to", str(to)])
    assert rc == 0
    assert to.exists()
    assert to.stat().st_size > 0
