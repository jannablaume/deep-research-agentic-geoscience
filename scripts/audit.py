#!/usr/bin/env python3
"""Check a run's output against the contract, from the files themselves.

The v0.3 prompt asked the model to audit its own compliance from memory, which is the
one thing a compacted long run cannot do. Every check here is executed: it parses the
artifacts and reports what it finds. A failed check is a working audit.

    python3 scripts/audit.py --out outputs/01_landscape/v0.4

Exits non-zero if any check fails. Prints a markdown table to paste into RUN.md.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys

csv.field_size_limit(10_000_000)

REQUIRED = ["RUN.md", "screened.csv", "queries.csv", "triage.csv", "shortlist.md",
            "audit_sample.md", "triage_stats.md", "screening.csv", "papers.csv",
            "papers.md", "report/00_executive_summary.md", "unreachable.md"]

PAPERS_COLS = [
    "identity_key", "tier", "system_id", "url", "title", "authors", "year", "venue",
    "source_type", "subfield", "subfield_secondary", "task", "agentic_techniques",
    "architecture", "base_model", "tools_used", "evaluation_method", "baseline",
    "held_out", "data_type", "reported_result", "maturity_claimed",
    "maturity_demonstrated", "author_stated_limitations", "code_availability",
    "access_status", "found_via",
]
MATURITY = {"M0", "M1", "M2", "M3", "M4", "M5", "not stated (abstract only)", "not stated"}
TAGS = ("[Certain]", "[Likely]", "[Absent-searched]")


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = args.out
    checks: list[tuple[str, bool, str]] = []

    def chk(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    # --- files present
    missing = [f for f in REQUIRED if not os.path.exists(os.path.join(out, f))]
    chk("Required files present", not missing, "missing: " + ", ".join(missing) if missing else "all present")

    screened = load(os.path.join(out, "screened.csv")) or []
    triage = load(os.path.join(out, "triage.csv")) or []
    screening = load(os.path.join(out, "screening.csv")) or []
    papers = load(os.path.join(out, "papers.csv")) or []
    queries = load(os.path.join(out, "queries.csv")) or []

    chk("screened.csv parses and is non-empty", bool(screened), f"{len(screened)} rows")
    chk("triage.csv covers the whole corpus", len(triage) == len(screened),
        f"triage {len(triage)} vs screened {len(screened)}")

    # --- harvest health
    zero = [q for q in queries if q.get("status") == "zero"]
    err = [q for q in queries if q.get("status") == "error"]
    chk("No silently-empty queries", not zero,
        "zero-result queries: " + ", ".join(q["query_id"] for q in zero[:8]) if zero else
        f"{len(queries)} api calls, none empty")
    chk("API errors within tolerance", len(err) <= max(2, len(queries) // 10),
        f"{len(err)} of {len(queries)} calls errored")
    no_abs = sum(1 for r in screened if not r.get("abstract"))
    pct = 100 * no_abs // max(len(screened), 1)
    chk("Corpus carries abstracts", pct <= 30,
        f"{no_abs} of {len(screened)} ({pct}%) have no abstract; these were screened on title alone")

    # --- screening integrity
    skeys = {r["identity_key"] for r in screened}
    orphan = [r["identity_key"] for r in screening if r["identity_key"] not in skeys]
    chk("Every screening decision traces to a harvested record", not orphan,
        f"{len(orphan)} orphans" + (f", e.g. {orphan[0]}" if orphan else ""))
    bad_dec = [r["identity_key"] for r in screening
               if r.get("decision") not in {"in", "out"}]
    chk("Screening decisions are in/out", not bad_dec, f"{len(bad_dec)} invalid")
    audited = [r for r in screening if r.get("from_audit_sample") == "yes"]
    fn = [r for r in audited if r.get("decision") == "in"]
    rate = 100 * len(fn) / len(audited) if audited else 0
    chk("Recall audit performed", len(audited) >= 40,
        f"{len(audited)} below-cut records screened, {len(fn)} false negatives ({rate:.0f}%)")
    chk("False-negative rate acceptable", rate <= 5 or not audited,
        f"{rate:.0f}% - above 5% means lowering --min-score and re-running triage")

    # --- papers grid
    if papers:
        cols = list(papers[0].keys())
        chk("papers.csv columns match SCHEMA", cols == PAPERS_COLS,
            "extra: " + str(set(cols) - set(PAPERS_COLS)) + " missing: " + str(set(PAPERS_COLS) - set(cols))
            if cols != PAPERS_COLS else f"{len(cols)} columns")
    else:
        chk("papers.csv columns match SCHEMA", False, "papers.csv empty or absent")

    # Guard against vacuous passes: with no papers, every downstream check trivially
    # holds and the table would read as a clean run that produced nothing.
    chk("papers.csv is non-empty", len(papers) > 0, f"{len(papers)} admitted sources")
    chk("screening.csv is non-empty", len(screening) > 0, f"{len(screening)} decisions")

    in_keys = {r["identity_key"] for r in screening if r.get("decision") == "in"}
    pkeys = [r["identity_key"] for r in papers]
    chk("Admitted set matches screening", set(pkeys) == in_keys,
        f"papers {len(set(pkeys))} vs screened-in {len(in_keys)}; "
        f"only in papers: {len(set(pkeys) - in_keys)}, only in screening: {len(in_keys - set(pkeys))}")
    chk("No duplicate rows in papers.csv", len(pkeys) == len(set(pkeys)),
        f"{len(pkeys) - len(set(pkeys))} duplicates")

    bad_mat = [r["identity_key"] for r in papers if r.get("maturity_demonstrated") not in MATURITY]
    chk("Maturity values are from the rubric", not bad_mat, f"{len(bad_mat)} invalid")
    bad_tier = [r["identity_key"] for r in papers if r.get("tier") not in {"core", "context"}]
    chk("Tier values valid", not bad_tier, f"{len(bad_tier)} invalid")
    core = [r for r in papers if r.get("tier") == "core"]
    abs_only_core = [r for r in core if r.get("access_status") == "abstract-only"]
    chk("Core tier was actually deep-read", len(abs_only_core) <= len(core) // 5,
        f"{len(abs_only_core)} of {len(core)} core papers are abstract-only")

    # --- extracts
    pmd = ""
    for cand in ("papers.md",):
        p = os.path.join(out, cand)
        if os.path.exists(p):
            pmd = open(p, encoding="utf-8").read()
    heads = set(re.findall(r"^##\s+(\S+)", pmd, re.M))
    missing_ext = [k for k in {r["identity_key"] for r in core} if k not in heads]
    chk("Every core paper has an extract block", not missing_ext,
        f"{len(missing_ext)} missing" + (f", e.g. {missing_ext[0]}" if missing_ext else ""))

    # --- report
    rdir = os.path.join(out, "report")
    rfiles = sorted(f for f in os.listdir(rdir) if f.endswith(".md")) if os.path.isdir(rdir) else []
    text = "\n".join(open(os.path.join(rdir, f), encoding="utf-8").read() for f in rfiles)
    chk("Report sections present", len(rfiles) >= 5, f"{len(rfiles)} section files: {', '.join(rfiles)}")

    # Strip heading, table and code lines from each block rather than discarding any
    # block that starts with one: a heading with no blank line after it would otherwise
    # exempt the prose beneath it from the tag check entirely.
    def prose_of(block: str) -> str:
        return "\n".join(ln for ln in block.splitlines()
                         if not ln.lstrip().startswith(("#", "|", "```", ">", "---")))

    paras = [p for p in (prose_of(b) for b in re.split(r"\n\s*\n", text))
             if len(p.split()) > 25]
    untagged = [p.strip() for p in paras if not any(t in p for t in TAGS)]
    chk("Substantive paragraphs carry an evidence tag", not untagged,
        f"{len(untagged)} of {len(paras)} untagged" +
        (f'; first: "{untagged[0][:70]}…"' if untagged else ""))

    cited = set(re.findall(r"\[\[([^\]]+)\]\]", text))
    unknown = sorted(c for c in cited if c not in set(pkeys))
    chk("Every citation resolves to papers.csv", not unknown,
        f"{len(unknown)} unknown, e.g. {unknown[0]}" if unknown else f"{len(cited)} citations, all resolve")

    absent = re.findall(r"\[Absent-searched\][^\n]*", text)
    unbacked = [a for a in absent if not re.search(r"q\d{3}", a)]
    chk("Absence claims cite query ids", not unbacked, f"{len(unbacked)} of {len(absent)} unbacked")

    banned = re.findall(r"\b(promising|great potential|revolutionar|revolutioni[sz]|game[- ]chang|paradigm shift|cutting[- ]edge|state of the art\b)\w*",
                        text, re.I)
    chk("No promotional framing", not banned, f"found: {', '.join(sorted(set(banned))[:5])}" if banned else "clean")

    # --- report
    lines = ["| Check | Result | Detail |", "|---|---|---|"]
    for name, ok, detail in checks:
        lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
    table = "\n".join(lines)
    print(table)
    failed = [n for n, ok, _ in checks if not ok]
    print(f"\n{len(checks) - len(failed)}/{len(checks)} passed."
          + (f" FAILED: {', '.join(failed)}" if failed else ""), file=sys.stderr)
    with open(os.path.join(out, "audit.md"), "w", encoding="utf-8") as f:
        f.write("# Self-audit\n\nGenerated by `scripts/audit.py` from the output files.\n\n"
                + table + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
