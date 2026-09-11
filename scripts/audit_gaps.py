#!/usr/bin/env python3
"""Check a 03_gaps run against its contract, from the files themselves.

The 03 run has one failure mode the other two do not: a gap that reads well and rests on
nothing. Three of the checks here exist for it — every gap cites candidates that exist,
every gap carries a verdict that a verification pass returned, and every candidate is
either used or discarded with a reason. A candidate that quietly vanishes is
indistinguishable from one nobody read.

    python3 scripts/audit_gaps.py --out outputs/03_gaps/v0.1

Exits non-zero if any check fails. Prints a markdown table to paste into RUN.md.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

from gaps import CANDIDATE_COLS, KINDS

Row = dict[str, str]

csv.field_size_limit(10_000_000)

REQUIRED = ["RUN.md", "gap_candidates.csv", "gap_candidates.md", "gaps.md", "verification.md"]

VERDICTS = {"confirmed-absent", "partially-addressed", "refuted", "undecidable"}
DISCARD_REASONS = ("duplicate-of", "run-artefact", "too-specific", "refuted")
TAGS = ("[Certain]", "[Likely]", "[Absent-searched]")

# The 03 run synthesises; it does not argue. Everything here is a sentence that has left
# describing what the runs recorded and started telling someone what to do about it.
REASONING = (
    r"\bmatters because\b|\bis important because\b|\bshould be (?:prioriti[sz]ed|addressed|explored)\b"
    r"|\bfuture work\b|\bwe recommend\b|\bthe most (?:important|promising|pressing)\b"
    r"|\bhighest[- ]priority\b|\bresearch agenda\b|\bnext steps?\b|\bopportunit(?:y|ies)\b"
)

BLOCK = re.compile(r"^##\s+(G\d+)\b[^\n]*\n(.*?)(?=^##\s|\Z)", re.M | re.S)
FIELD = re.compile(r"^-\s*(candidates|runs|verdict|evidence|checked)\s*:\s*(.+)$", re.M)


def parse_blocks(text: str) -> dict[str, dict[str, str]]:
    """`## G01 — …` blocks and their field lines, per SCHEMA_gaps.md."""
    out: dict[str, dict[str, str]] = {}
    for gid, body in BLOCK.findall(text):
        out[gid] = {k: v.strip() for k, v in FIELD.findall(body)} | {"_body": body}
    return out


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    out = Path(args.out)
    checks: list[tuple[str, bool, str]] = []

    def chk(name: str, ok: object, detail: str = "") -> None:
        checks.append((name, bool(ok), detail))

    missing = [f for f in REQUIRED if not (out / f).exists()]
    chk(
        "Required files present",
        not missing,
        "missing: " + ", ".join(missing) if missing else "all present",
    )

    cand_path = out / "gap_candidates.csv"
    candidates: list[Row] = []
    if cand_path.exists():
        with cand_path.open(newline="", encoding="utf-8") as f:
            candidates = list(csv.DictReader(f))
    cand_ids = {r.get("candidate_id", "") for r in candidates} - {""}

    chk("gap_candidates.csv is non-empty", bool(candidates), f"{len(candidates)} candidates")
    chk(
        "gap_candidates.csv columns match SCHEMA_gaps",
        bool(candidates) and list(candidates[0].keys()) == CANDIDATE_COLS,
        "columns: " + ", ".join(candidates[0].keys()) if candidates else "absent",
    )
    # Read defensively from here down. `gap_candidates.csv` is written by a script and
    # must not be edited by hand, so a row missing a column means someone edited it — and
    # an audit that raises on that reports nothing at all, including the other 18 checks.
    bad_kind = sorted({r.get("kind", "") for r in candidates} - KINDS)
    chk("Candidate kinds are from the controlled list", not bad_kind, f"unknown: {bad_kind}")
    half_counted = [
        r.get("candidate_id", "?")
        for r in candidates
        if bool(r.get("count")) != bool(r.get("denominator"))
    ]
    chk(
        "Every counted candidate carries its denominator",
        not half_counted,
        f"{len(half_counted)} carry one without the other"
        + (f", e.g. {half_counted[0]}" if half_counted else ""),
    )

    gaps_text = (out / "gaps.md").read_text(encoding="utf-8") if (out / "gaps.md").exists() else ""
    ver_text = (
        (out / "verification.md").read_text(encoding="utf-8")
        if (out / "verification.md").exists()
        else ""
    )
    gaps = parse_blocks(gaps_text)
    verifications = parse_blocks(ver_text)

    chk("gaps.md states at least one gap", bool(gaps), f"{len(gaps)} gap blocks")

    no_cands = [g for g, b in gaps.items() if not b.get("candidates")]
    chk(
        "Every gap cites at least one candidate",
        not no_cands,
        f"{len(no_cands)} cite none" + (f", e.g. {no_cands[0]}" if no_cands else ""),
    )
    cited: set[str] = set()
    unknown: list[str] = []
    for gid, b in gaps.items():
        ids = [x.strip() for x in re.split(r"[;,\s]+", b.get("candidates", "")) if x.strip()]
        cited |= set(ids)
        unknown += [f"{gid}:{i}" for i in ids if i not in cand_ids]
    chk(
        "Every cited candidate exists",
        not unknown,
        f"{len(unknown)} unknown" + (f", e.g. {unknown[0]}" if unknown else ""),
    )

    bad_verdict = [g for g, b in gaps.items() if b.get("verdict") not in VERDICTS]
    chk(
        "Every gap carries a verdict from the controlled list",
        not bad_verdict,
        f"{len(bad_verdict)} invalid or missing"
        + (f", e.g. {bad_verdict[0]}" if bad_verdict else ""),
    )

    # An absence claim is only as good as the search behind it — the same rule the 01 and
    # 02 reports apply to [Absent-searched], applied to the verdict that asserts absence.
    unbacked = [
        g
        for g, b in gaps.items()
        if b.get("verdict") == "confirmed-absent"
        and not re.search(r"\bq\d{3}\b", b.get("evidence", ""))
    ]
    chk(
        "confirmed-absent verdicts cite the queries that looked",
        not unbacked,
        f"{len(unbacked)} unbacked" + (f", e.g. {unbacked[0]}" if unbacked else ""),
    )
    no_keys = [
        g
        for g, b in gaps.items()
        if b.get("verdict") in {"partially-addressed", "refuted"}
        and not re.search(r"(doi:|arxiv:|title:)", b.get("evidence", ""))
    ]
    chk(
        "partially-addressed and refuted verdicts name the sources that address it",
        not no_keys,
        f"{len(no_keys)} name none" + (f", e.g. {no_keys[0]}" if no_keys else ""),
    )

    missing_ver = sorted(set(gaps) - set(verifications))
    chk(
        "Every gap has a verification block",
        not missing_ver,
        f"{len(missing_ver)} missing" + (f", e.g. {missing_ver[0]}" if missing_ver else ""),
    )
    mismatched = [
        g
        for g in sorted(set(gaps) & set(verifications))
        if gaps[g].get("verdict") != verifications[g].get("verdict")
    ]
    chk(
        "Verdicts agree between gaps.md and verification.md",
        not mismatched,
        f"{len(mismatched)} disagree" + (f", e.g. {mismatched[0]}" if mismatched else ""),
    )
    # A verification that searched nothing cannot return confirmed-absent, however
    # confident it sounds.
    empty_search = [
        g
        for g, b in verifications.items()
        if not re.search(r"^-?\s*\*{0,2}searched\*{0,2}\s*:\s*\S", b["_body"], re.M | re.I)
    ]
    chk(
        "Every verification block records what it searched",
        not empty_search,
        f"{len(empty_search)} record no search"
        + (f", e.g. {empty_search[0]}" if empty_search else ""),
    )

    # --- the discard ledger: every candidate accounted for
    tail = gaps_text.split("## Discarded candidates", 1)
    discarded: set[str] = set()
    if len(tail) == 2:
        for line in tail[1].splitlines():
            ids = re.findall(r"\bc\d{3}\b", line)
            if ids and any(reason in line for reason in DISCARD_REASONS):
                discarded |= set(ids)
    unaccounted = sorted(cand_ids - cited - discarded)
    chk(
        "Every candidate is used or discarded with a reason",
        not unaccounted,
        f"{len(unaccounted)} of {len(cand_ids)} unaccounted for"
        + (f", e.g. {unaccounted[0]}" if unaccounted else ""),
    )

    # --- prose
    def prose_of(block: str) -> str:
        return "\n".join(
            ln
            for ln in block.splitlines()
            if not ln.lstrip().startswith(("#", "|", "```", ">", "---", "- ", "* "))
        )

    paras = [
        p for p in (prose_of(b) for b in re.split(r"\n\s*\n", gaps_text)) if len(p.split()) > 25
    ]
    untagged = [p.strip() for p in paras if not any(t in p for t in TAGS)]
    chk(
        "Substantive paragraphs carry an evidence tag",
        not untagged,
        f"{len(untagged)} of {len(paras)} untagged"
        + (f'; first: "{untagged[0][:70]}…"' if untagged else ""),
    )
    absent = re.findall(r"\[Absent-searched\][^\n]*", gaps_text)
    unbacked_abs = [a for a in absent if not re.search(r"q\d{3}", a)]
    chk(
        "Absence claims cite query ids",
        not unbacked_abs,
        f"{len(unbacked_abs)} of {len(absent)} unbacked",
    )
    # Quoted spans are exempt from the two framing checks, and only from those. This
    # document restates what sources said, and `maturity_claimed` on eleven v0.5 systems
    # is the authors calling their own work promising or a blueprint for future work.
    # Banning those words inside a quotation would force a paraphrase of the one thing
    # that has to be verbatim. The ban is on this run's own framing.
    unquoted = re.sub(r'"[^"\n]*"', "", gaps_text)
    reasoning = re.findall(REASONING, unquoted, re.I)
    chk(
        "No reasoning about the gaps",
        not reasoning,
        f'{len(reasoning)} found, e.g. "{reasoning[0]}"' if reasoning else "clean",
    )
    banned = re.findall(
        r"\b(promising|great potential|revolutionar|revolutioni[sz]|game[- ]chang|"
        r"paradigm shift|cutting[- ]edge|state of the art\b)\w*",
        unquoted,
        re.I,
    )
    chk(
        "No promotional framing",
        not banned,
        f"found: {', '.join(sorted(set(banned))[:5])}" if banned else "clean",
    )

    lines = ["| Check | Result | Detail |", "|---|---|---|"]
    for name, ok, detail in checks:
        lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
    table = "\n".join(lines)
    print(table)
    failed = [n for n, ok, _ in checks if not ok]
    print(
        f"\n{len(checks) - len(failed)}/{len(checks)} passed."
        + (f" FAILED: {', '.join(failed)}" if failed else ""),
        file=sys.stderr,
    )
    (out / "audit.md").write_text(
        "# Self-audit\n\nGenerated by `scripts/audit_gaps.py` from the output files.\n\n"
        + table
        + "\n",
        encoding="utf-8",
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
