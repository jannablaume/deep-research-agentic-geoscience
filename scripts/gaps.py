#!/usr/bin/env python3
"""Extract every gap candidate the finished runs already contain, mechanically.

A research gap that a run can support is not something to be thought up. It is already
written down in the artifacts, in five shapes, and all five can be read out by a script:

1. **What the authors said their own system could not do** — `author_stated_limitations`
   in `papers.csv`, one per admitted source.
2. **What a run looked for and did not find** — `[Absent-searched]` paragraphs in the
   report, with the query ids that back them.
3. **What the evidence base cannot answer** — `not stated` cells per column, sources with
   no baseline, no held-out set, or only synthetic data.
4. **Categories with nothing in them** — a subfield or touchpoint that is declared, was
   screened for, and has no admitted or no deep-read source.
5. **What nobody could read** — abstract-only sources, and the `would_change` column of
   `paywalled.md` saying what reading them would have settled.

Every candidate carries its run, its kind, its evidence reference and — where it is a
count — its denominator, because a count without one is the failure this repository
exists to prevent.

    python3 scripts/gaps.py --out outputs/03_gaps/v0.1 \\
        --run outputs/01_landscape/v0.5 --run outputs/02_tango/v0.1

Writes, in --out: gap_candidates.csv and gap_candidates.md. No network calls, and no
judgment: nothing here decides whether a candidate is a gap. That is the model's job in
`prompts/03_gaps.md`, and a candidate that turns out to be nothing is still accounted
for there.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

from audit_tango import TOUCHPOINTS

Row = dict[str, str]

csv.field_size_limit(10_000_000)

CANDIDATE_COLS = [
    "candidate_id",
    "run",
    "kind",
    "subject",
    "statement",
    "evidence_ref",
    "count",
    "denominator",
]

KINDS = {
    "author-limitation",
    "absence-claim",
    "evidence-hole",
    "evaluation-hole",
    "empty-category",
    "unread-source",
    "claim-gap",
}

# Cells that carry no information. `papers.csv` uses `not stated` where a source is
# silent, and SCHEMA.md forbids inferring a value to fill one, so these are measurements
# of what the literature does not report.
EMPTY = {"", "not stated", "none", "n/a", "na", "not stated (abstract only)"}

# Columns whose silence is a fact about the literature rather than about the run. Left
# out: every metadata column, where `not stated` means the harvest missed something.
EVIDENCE_COLUMNS = [
    "base_model",
    "tools_used",
    "evaluation_method",
    "baseline",
    "held_out",
    "data_type",
    "reported_result",
    "maturity_claimed",
    "author_stated_limitations",
    "code_availability",
]

MATURITY_ORDER = ["M0", "M1", "M2", "M3", "M4", "M5"]


def load(path: Path) -> list[Row]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def blank(value: str | None) -> bool:
    return (value or "").strip().lower() in EMPTY


def run_label(run: Path) -> str:
    """`outputs/01_landscape/v0.5` → `01_landscape/v0.5`, which is what a reader cites."""
    parts = run.resolve().parts
    return "/".join(parts[-2:]) if len(parts) >= 2 else run.name


class Collector:
    """Accumulates candidates and hands out stable ids in emission order."""

    def __init__(self) -> None:
        self.rows: list[Row] = []

    def add(
        self,
        run: str,
        kind: str,
        subject: str,
        statement: str,
        evidence_ref: str,
        count: int | str = "",
        denominator: int | str = "",
    ) -> None:
        if kind not in KINDS:  # pragma: no cover - guards a typo in this file only
            raise ValueError(f"unknown candidate kind: {kind}")
        self.rows.append(
            {
                "candidate_id": f"c{len(self.rows) + 1:03d}",
                "run": run,
                "kind": kind,
                "subject": subject,
                "statement": " ".join(statement.split()),
                "evidence_ref": evidence_ref,
                "count": str(count),
                "denominator": str(denominator),
            }
        )


def collect_author_limitations(c: Collector, run: str, papers: list[Row]) -> None:
    for r in papers:
        if blank(r.get("author_stated_limitations")):
            continue
        c.add(
            run,
            "author-limitation",
            r.get("system_id") or r["identity_key"],
            r["author_stated_limitations"],
            r["identity_key"],
        )


def collect_absence_claims(c: Collector, run: str, report_dir: Path) -> None:
    if not report_dir.is_dir():
        return
    for path in sorted(report_dir.glob("*.md")):
        text = read_text(path)
        for para in re.split(r"\n\s*\n", text):
            if "[Absent-searched]" not in para:
                continue
            qids = sorted(set(re.findall(r"\bq\d{3}\b", para)))
            c.add(
                run,
                "absence-claim",
                path.name,
                para.replace("[Absent-searched]", "").strip(),
                ";".join(qids) or "UNBACKED",
            )


def collect_evidence_holes(c: Collector, run: str, papers: list[Row]) -> None:
    total = len(papers)
    if not total:
        return
    for col in EVIDENCE_COLUMNS:
        if col not in papers[0]:
            continue
        n = sum(1 for r in papers if blank(r.get(col)))
        if not n:
            continue
        c.add(
            run,
            "evidence-hole",
            col,
            f"{n} of {total} admitted sources state nothing for `{col}`.",
            "papers.csv",
            n,
            total,
        )


def collect_evaluation_holes(c: Collector, run: str, papers: list[Row]) -> None:
    core = [r for r in papers if r.get("tier") == "core"]
    if not core:
        return
    n = len(core)
    checks = [
        (
            "baseline",
            sum(1 for r in core if blank(r.get("baseline"))),
            "compared against no baseline",
        ),
        (
            "held_out",
            sum(1 for r in core if (r.get("held_out") or "").strip() != "yes"),
            "report no held-out evaluation",
        ),
        (
            "data_type",
            sum(1 for r in core if (r.get("data_type") or "").strip() == "synthetic"),
            "were evaluated on synthetic data only",
        ),
    ]
    for subject, count, phrase in checks:
        if count:
            c.add(
                run,
                "evaluation-hole",
                subject,
                f"{count} of {n} deep-read systems {phrase}.",
                "papers.csv (tier core)",
                count,
                n,
            )

    demonstrated = Counter((r.get("maturity_demonstrated") or "").strip() for r in core)
    low = sum(demonstrated[m] for m in ("M0", "M1"))
    high = sum(demonstrated[m] for m in ("M3", "M4", "M5"))
    c.add(
        run,
        "evaluation-hole",
        "maturity_ceiling",
        f"{low} of {n} deep-read systems demonstrate M1 or below; {high} reach M3 or above.",
        "papers.csv (tier core)",
        low,
        n,
    )


def collect_claim_gaps(c: Collector, run: str, papers: list[Row]) -> None:
    def level(value: str | None) -> int | None:
        m = re.search(r"\bM([0-5])\b", value or "")
        return int(m.group(1)) if m else None

    for r in papers:
        if r.get("tier") != "core":
            continue
        shown = level(r.get("maturity_demonstrated"))
        if shown is None:
            continue
        claimed = level(r.get("maturity_claimed"))
        if claimed is not None and claimed > shown:
            c.add(
                run,
                "claim-gap",
                r.get("system_id") or r["identity_key"],
                f"Claims {MATURITY_ORDER[claimed]}; the evaluation demonstrates "
                f"{MATURITY_ORDER[shown]}.",
                r["identity_key"],
            )
        elif claimed is None and shown <= 1 and not blank(r.get("maturity_claimed")):
            # SCHEMA.md makes `maturity_claimed` the source's strongest self-assertion in
            # its own words, so the two columns are usually not comparable as levels. The
            # one comparison that is mechanical: a source asserting something while its
            # evaluation demonstrates the floor. The statement says exactly that and no
            # more — whether the assertion actually exceeds M1 is a reading job.
            c.add(
                run,
                "claim-gap",
                r.get("system_id") or r["identity_key"],
                f"Evaluation demonstrates {MATURITY_ORDER[shown]}; the source asserts: "
                f'"{r["maturity_claimed"][:200]}"',
                r["identity_key"],
            )


def collect_empty_categories(
    c: Collector, run: str, papers: list[Row], screening: list[Row], transfer: list[Row]
) -> None:
    declared = {(r.get("subfield") or "").strip() for r in screening} - {""}
    declared |= {(r.get("subfield") or "").strip() for r in papers} - {""}
    # A periphery group is empty by design — it is harvested and counted, never admitted.
    # Reported as a gap it is a run artefact, and on the v0.5 run it was five of the six
    # empty categories, which is enough noise to bury the one that meant something.
    periphery = {
        name
        for name in declared
        if any(
            r.get("cut_reason") == "periphery"
            for r in screening
            if (r.get("subfield") or "").strip() == name
        )
        and not any(
            r.get("decision") == "in"
            for r in screening
            if (r.get("subfield") or "").strip() == name
        )
    }
    admitted = Counter((r.get("subfield") or "").strip() for r in papers)
    deep = Counter((r.get("subfield") or "").strip() for r in papers if r.get("tier") == "core")
    for name in sorted(declared - periphery):
        if not admitted[name]:
            c.add(
                run,
                "empty-category",
                name,
                f"Subfield `{name}` was screened for and no source was admitted.",
                "screening.csv; papers.csv",
                0,
                len(papers),
            )
        elif not deep[name]:
            c.add(
                run,
                "empty-category",
                name,
                f"Subfield `{name}` has {admitted[name]} admitted sources and none deep-read, "
                "so nothing in it is characterised beyond an abstract.",
                "papers.csv",
                0,
                admitted[name],
            )

    if transfer:
        seen = Counter(
            t
            for r in transfer
            for t in (r.get("tango_touchpoints") or "").split(";")
            if t and t != "none"
        )
        # The controlled list, not the values present: a touchpoint nothing matched is
        # exactly the candidate worth emitting, and it cannot be read off the data.
        for name in sorted(TOUCHPOINTS - {"none"}):
            if not seen[name]:
                c.add(
                    run,
                    "empty-category",
                    name,
                    f"Touchpoint `{name}` is claimed by no admitted source.",
                    "transfer.csv",
                    0,
                    len(transfer),
                )


def collect_unread_sources(c: Collector, run: str, papers: list[Row], run_dir: Path) -> None:
    abs_only = [r for r in papers if (r.get("access_status") or "").strip() == "abstract-only"]
    if papers:
        c.add(
            run,
            "unread-source",
            "abstract_only",
            f"{len(abs_only)} of {len(papers)} admitted sources were never read beyond an "
            "abstract, so nothing in them contributes to any characterisation.",
            "papers.csv",
            len(abs_only),
            len(papers),
        )
    pw = read_text(run_dir / "paywalled.md")
    # The table shape is fixed by SCHEMA_tango.md: the key is backticked in column one
    # and `would_change` is the last column.
    for line in pw.splitlines():
        cells = (
            [x.strip() for x in line.strip().strip("|").split("|")] if line.startswith("|") else []
        )
        if len(cells) < 8 or not cells[0].startswith("`"):
            continue
        would = cells[-1]
        if would.lower() in {"nothing", "would_change", ""}:
            continue
        c.add(run, "unread-source", cells[0].strip("`"), would, "paywalled.md")


def collect(run_dir: Path) -> list[Row]:
    run = run_label(run_dir)
    papers = load(run_dir / "papers.csv")
    screening = load(run_dir / "screening.csv")
    transfer = load(run_dir / "transfer.csv")
    if not papers:
        raise SystemExit(f"{run_dir}/papers.csv is missing or empty — nothing to read gaps out of")
    c = Collector()
    collect_author_limitations(c, run, papers)
    collect_absence_claims(c, run, run_dir / "report")
    collect_evidence_holes(c, run, papers)
    collect_evaluation_holes(c, run, papers)
    collect_claim_gaps(c, run, papers)
    collect_empty_categories(c, run, papers, screening, transfer)
    collect_unread_sources(c, run, papers, run_dir)
    return c.rows


def write_markdown(path: Path, rows: list[Row], runs: list[Path]) -> None:
    by_kind: dict[str, list[Row]] = {}
    for r in rows:
        by_kind.setdefault(r["kind"], []).append(r)
    with path.open("w", encoding="utf-8") as f:
        f.write(
            f"# Gap candidates — {len(rows)} extracted from "
            f"{', '.join(run_label(r) for r in runs)}\n\n"
            "Written by `scripts/gaps.py` from the runs' own artifacts. **Nothing here is a "
            "gap yet.** Each row is a place where a finished run recorded that something is "
            "absent, unstated, unevaluated, unread or empty. Deciding which of these are "
            "research gaps, which are artefacts of how the run was done, and which are "
            "neither is the reading job — and every candidate has to be accounted for, "
            "including the ones discarded.\n\n"
            "A count here always carries its denominator. A candidate with an empty "
            "`count` is a statement someone made, not a measurement.\n\n"
        )
        for kind in sorted(by_kind):
            group = by_kind[kind]
            f.write(f"\n## {kind} — {len(group)}\n\n")
            for r in group:
                measure = (
                    f" · {r['count']}/{r['denominator']}" if r["count"] and r["denominator"] else ""
                )
                f.write(
                    f"### {r['candidate_id']}\n"
                    f"**{r['subject']}** — {r['run']} · {r['evidence_ref']}{measure}\n\n"
                    f"{r['statement']}\n\n"
                )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="the 03_gaps run directory")
    ap.add_argument(
        "--run",
        action="append",
        required=True,
        dest="runs",
        help="a finished run directory to read. Repeat for each one.",
    )
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    runs = [Path(r) for r in args.runs]

    rows: list[Row] = []
    for run_dir in runs:
        found = collect(run_dir)
        # Ids are unique across the whole file, not per run: the report cites `c042`
        # and has to mean one thing.
        for r in found:
            r["candidate_id"] = f"c{len(rows) + 1:03d}"
            rows.append(r)
        print(f"{run_label(run_dir)}: {len(found)} candidates", file=sys.stderr)

    with (out_dir / "gap_candidates.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CANDIDATE_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    write_markdown(out_dir / "gap_candidates.md", rows, runs)

    counts = Counter(r["kind"] for r in rows)
    print(
        f"wrote {len(rows)} candidates to {out_dir}/gap_candidates.csv: "
        + ", ".join(f"{k} {n}" for k, n in sorted(counts.items())),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
