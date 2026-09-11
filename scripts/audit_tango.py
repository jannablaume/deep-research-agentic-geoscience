#!/usr/bin/env python3
"""Check a 02_tango run against its contract, from the files themselves.

`audit.py` is the 01 run's gate and is frozen; this is the same idea over a different
contract. Everything it shares with 01 is imported rather than restated —
`PAPERS_COLS`, so the comparison grid is defined once, and `load`. What is new here is
the three artifacts 02 adds (`transfer.csv`, `transfer.md`, `paywalled.md`), 02's
screening vocabulary, and one check 01 does not need: a run about making TANGO agentic
must not tell TANGO what to do.

    python3 scripts/audit_tango.py --out outputs/02_tango/v0.1

Exits non-zero if any check fails. Prints a markdown table to paste into RUN.md.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

from audit import MATURITY, PAPERS_COLS, TAGS, Row, load

csv.field_size_limit(10_000_000)

# fmt: off
REQUIRED = ["RUN.md", "screened.csv", "queries.csv", "triage.csv", "shortlist.md",
            "audit_sample.md", "triage_stats.md", "screening.csv", "papers.csv",
            "papers.md", "transfer.csv", "transfer.md", "paywalled.md",
            "unreachable.md", "report/00_executive_summary.md"]

TRANSFER_COLS = [
    "identity_key", "system_id", "tango_touchpoints", "what_it_drives", "interface",
    "autonomy", "failure_handling", "access_status",
]

TOUCHPOINTS = {
    "config-generation", "topology-construction", "solver-control", "optimisation-loop",
    "surrogate-modelling", "uncertainty-quantification", "hpc-scale-out", "tool-exposure",
    "results-interpretation", "techno-economic", "verification-regression",
    "provenance-reproducibility", "none",
}
INTERFACES = {"api", "cli", "file-io", "mcp", "code-execution", "gui", "not stated"}
AUTONOMY = {"suggests", "executes-with-approval", "executes-and-iterates", "not stated"}
CUT_REASONS = {
    "not-agentic", "no-simulation-target", "periphery", "pre-llm-only", "duplicate",
    "not-a-source", "no-abstract-untriageable",
}
SUBFIELDS = {
    "simulation_orchestration", "solver_control", "optimisation_uq", "energy_systems",
    "geoenergy_subsurface", "scientific_computing", "computational_discovery",
    "simulation_general", "software_engineering", "lab_automation", "interface_agents",
    "science_of_science",
}
BLOCKED_BY = {
    "paywall", "bot-protection", "no-full-text-anywhere", "tooling-failure",
    "no-abstract-in-any-api",
}
# fmt: on

# The 01 report must not advocate; this one must also not prescribe. "What exists that
# is interesting towards making TANGO agentic" is a description of a literature, and the
# moment a sentence tells TANGO what to build it is no longer reporting what it read.
PRESCRIPTIVE = (
    r"\bTANGO (?:should|must|ought|needs? to|could easily|would benefit|is well[- ]placed)\b"
    r"|\bwe (?:recommend|propose|suggest that TANGO|advise)\b"
    r"|\b(?:recommended|suggested) (?:approach|architecture|next step)s? for TANGO\b"
    r"|\broadmap for TANGO\b"
)


def md_blocks(text: str) -> set[str]:
    return set(re.findall(r"^##\s+(\S+)", text, re.M))


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

    # --- files present
    missing = [f for f in REQUIRED if not (out / f).exists()]
    chk(
        "Required files present",
        not missing,
        "missing: " + ", ".join(missing) if missing else "all present",
    )

    screened = load(out / "screened.csv") or []
    triage = load(out / "triage.csv") or []
    screening = load(out / "screening.csv") or []
    papers = load(out / "papers.csv") or []
    transfer = load(out / "transfer.csv") or []
    queries = load(out / "queries.csv") or []

    chk("screened.csv parses and is non-empty", bool(screened), f"{len(screened)} rows")

    tkeys = {r["identity_key"] for r in triage}
    skey_map = {r["identity_key"]: r for r in screened}
    missing_from_screened = tkeys - set(skey_map)

    def _greyish(r: Row) -> bool:
        apis = r.get("source_apis") or ""
        qids = r.get("query_ids") or ""
        return "web" in apis or bool(re.search(r"\bw\d+", qids)) or "snowball" in qids

    extras = [r for k, r in skey_map.items() if k not in tkeys]
    bad_extra = [r["identity_key"] for r in extras if not _greyish(r)]
    chk(
        "triage.csv covers the API corpus",
        not missing_from_screened and not bad_extra,
        f"triage {len(triage)} vs screened {len(screened)}; {len(extras)} grey/snowball "
        f"extras; missing from screened: {len(missing_from_screened)}; untriaged non-grey "
        f"extras: {len(bad_extra)}",
    )

    # --- harvest health
    zero = [q for q in queries if q.get("status") == "zero"]
    err = [q for q in queries if q.get("status") == "error"]
    chk(
        "No silently-empty queries",
        not zero,
        "zero-result queries: " + ", ".join(q["query_id"] for q in zero[:8])
        if zero
        else f"{len(queries)} api calls, none empty",
    )
    chk(
        "API errors within tolerance",
        len(err) <= max(2, len(queries) // 10),
        f"{len(err)} of {len(queries)} calls errored",
    )
    no_abs = sum(1 for r in screened if not r.get("abstract"))
    pct = 100 * no_abs // max(len(screened), 1)
    chk(
        "Corpus carries abstracts",
        pct <= 30,
        f"{no_abs} of {len(screened)} ({pct}%) have no abstract",
    )

    # --- screening integrity
    skeys = {r["identity_key"] for r in screened}
    orphan = [r["identity_key"] for r in screening if r["identity_key"] not in skeys]
    chk(
        "Every screening decision traces to a harvested record",
        not orphan,
        f"{len(orphan)} orphans" + (f", e.g. {orphan[0]}" if orphan else ""),
    )
    bad_dec = [r["identity_key"] for r in screening if r.get("decision") not in {"in", "out"}]
    chk("Screening decisions are in/out", not bad_dec, f"{len(bad_dec)} invalid")
    bad_cut = [
        r["identity_key"]
        for r in screening
        if r.get("decision") == "out" and r.get("cut_reason") not in CUT_REASONS
    ]
    chk(
        "Cut reasons are from the 02 vocabulary",
        not bad_cut,
        f"{len(bad_cut)} invalid" + (f", e.g. {bad_cut[0]}" if bad_cut else ""),
    )

    def md_keys(name: str) -> set[str]:
        path = out / name
        return (
            set(re.findall(r"^### (\S+)", path.read_text(encoding="utf-8"), re.M))
            if path.exists()
            else set()
        )

    shortlist_keys = md_keys("shortlist.md")
    sample_keys = md_keys("audit_sample.md")
    screened_keys = {r["identity_key"] for r in screening}
    unscreened = shortlist_keys - screened_keys
    chk(
        "Every shortlist record was screened",
        not unscreened,
        f"{len(unscreened)} of {len(shortlist_keys)} shortlisted records have no screening row"
        if unscreened
        else f"all {len(shortlist_keys)} shortlisted records screened",
    )

    audited = [r for r in screening if r.get("from_audit_sample") == "yes"]
    stale = [r["identity_key"] for r in audited if r["identity_key"] not in sample_keys]
    chk(
        "Audit sample matches the screened audit rows",
        not stale,
        f"{len(stale)} of {len(audited)} screened audit-sample rows are absent from the "
        "current audit_sample.md"
        if stale
        else f"all {len(audited)} audit rows present",
    )
    fn = [r for r in audited if r.get("decision") == "in"]
    rate = 100 * len(fn) / len(audited) if audited else 0
    chk(
        "Recall audit performed",
        len(audited) >= 40,
        f"{len(audited)} below-cut records screened, {len(fn)} false negatives ({rate:.0f}%)",
    )
    chk(
        "False-negative rate acceptable",
        rate <= 5 or not audited,
        f"{rate:.0f}% - above 5% means diagnose which cut is binding (min-score, min-strong, "
        "or the domain vocabulary in reference/queries_tango.json) before widening",
    )

    # --- papers grid
    if papers:
        cols = list(papers[0].keys())
        chk(
            "papers.csv columns match SCHEMA",
            cols == PAPERS_COLS,
            "extra: "
            + str(set(cols) - set(PAPERS_COLS))
            + " missing: "
            + str(set(PAPERS_COLS) - set(cols))
            if cols != PAPERS_COLS
            else f"{len(cols)} columns",
        )
    else:
        chk("papers.csv columns match SCHEMA", False, "papers.csv empty or absent")

    chk("papers.csv is non-empty", len(papers) > 0, f"{len(papers)} admitted sources")
    chk("screening.csv is non-empty", len(screening) > 0, f"{len(screening)} decisions")

    in_keys = {r["identity_key"] for r in screening if r.get("decision") == "in"}
    pkeys = [r["identity_key"] for r in papers]
    chk(
        "Admitted set matches screening",
        set(pkeys) == in_keys,
        f"papers {len(set(pkeys))} vs screened-in {len(in_keys)}; "
        f"only in papers: {len(set(pkeys) - in_keys)}, only in screening: "
        f"{len(in_keys - set(pkeys))}",
    )
    chk(
        "No duplicate rows in papers.csv",
        len(pkeys) == len(set(pkeys)),
        f"{len(pkeys) - len(set(pkeys))} duplicates",
    )
    bad_mat = [r["identity_key"] for r in papers if r.get("maturity_demonstrated") not in MATURITY]
    chk("Maturity values are from the rubric", not bad_mat, f"{len(bad_mat)} invalid")
    bad_tier = [r["identity_key"] for r in papers if r.get("tier") not in {"core", "context"}]
    chk("Tier values valid", not bad_tier, f"{len(bad_tier)} invalid")
    bad_sub = [r["identity_key"] for r in papers if r.get("subfield") not in SUBFIELDS]
    chk(
        "Subfields are from the 02 vocabulary",
        not bad_sub,
        f"{len(bad_sub)} invalid" + (f", e.g. {bad_sub[0]}" if bad_sub else ""),
    )
    core = [r for r in papers if r.get("tier") == "core"]
    abs_only_core = [r for r in core if r.get("access_status") == "abstract-only"]
    chk(
        "Core tier was actually deep-read",
        len(abs_only_core) <= len(core) // 5,
        f"{len(abs_only_core)} of {len(core)} core papers are abstract-only",
    )

    # --- extracts
    core_keys = {r["identity_key"] for r in core}
    pmd = (out / "papers.md").read_text(encoding="utf-8") if (out / "papers.md").exists() else ""
    missing_ext = sorted(core_keys - md_blocks(pmd))
    chk(
        "Every core paper has an extract block",
        not missing_ext,
        f"{len(missing_ext)} missing" + (f", e.g. {missing_ext[0]}" if missing_ext else ""),
    )

    # --- transfer grid: the artifact this run exists to produce
    if transfer:
        tcols = list(transfer[0].keys())
        chk(
            "transfer.csv columns match SCHEMA_tango",
            tcols == TRANSFER_COLS,
            "extra: "
            + str(set(tcols) - set(TRANSFER_COLS))
            + " missing: "
            + str(set(TRANSFER_COLS) - set(tcols))
            if tcols != TRANSFER_COLS
            else f"{len(tcols)} columns",
        )
    else:
        chk("transfer.csv columns match SCHEMA_tango", False, "transfer.csv empty or absent")

    tkeys_all = [r["identity_key"] for r in transfer]
    chk(
        "transfer.csv covers the admitted set exactly",
        set(tkeys_all) == set(pkeys) and len(tkeys_all) == len(set(tkeys_all)),
        f"transfer {len(set(tkeys_all))} vs admitted {len(set(pkeys))}; "
        f"missing: {len(set(pkeys) - set(tkeys_all))}, "
        f"unknown: {len(set(tkeys_all) - set(pkeys))}, "
        f"duplicates: {len(tkeys_all) - len(set(tkeys_all))}",
    )
    bad_tp = [
        r["identity_key"]
        for r in transfer
        if not r.get("tango_touchpoints")
        or any(t not in TOUCHPOINTS for t in r["tango_touchpoints"].split(";") if t)
    ]
    chk(
        "Touchpoints are from the controlled list",
        not bad_tp,
        f"{len(bad_tp)} rows carry an unknown or empty touchpoint"
        + (f", e.g. {bad_tp[0]}" if bad_tp else ""),
    )
    bad_iface = [r["identity_key"] for r in transfer if r.get("interface") not in INTERFACES]
    bad_auto = [r["identity_key"] for r in transfer if r.get("autonomy") not in AUTONOMY]
    chk(
        "Interface and autonomy values are from the controlled lists",
        not bad_iface and not bad_auto,
        f"{len(bad_iface)} bad interface, {len(bad_auto)} bad autonomy",
    )

    tmd = (
        (out / "transfer.md").read_text(encoding="utf-8") if (out / "transfer.md").exists() else ""
    )
    tblocks = md_blocks(tmd)
    missing_tb = sorted(core_keys - tblocks)
    chk(
        "Every core paper has a transfer extract block",
        not missing_tb,
        f"{len(missing_tb)} missing" + (f", e.g. {missing_tb[0]}" if missing_tb else ""),
    )
    # A block with no quoted line and no explicit NOT FOUND is a paraphrase, and a
    # touchpoint that rests on a paraphrase is a characterisation nobody can check.
    empty_tb = [
        k
        for k in sorted(core_keys & tblocks)
        if not re.search(
            rf"^##\s+{re.escape(k)}\s*$(?:(?!^##\s).)*?(?:\"|NOT FOUND)", tmd, re.M | re.S
        )
    ]
    chk(
        "Transfer blocks carry a quote or an explicit NOT FOUND",
        not empty_tb,
        f"{len(empty_tb)} blocks have neither" + (f", e.g. {empty_tb[0]}" if empty_tb else ""),
    )

    # --- paywalls: the list the run hands back to whoever has the credentials
    pw = (
        (out / "paywalled.md").read_text(encoding="utf-8")
        if (out / "paywalled.md").exists()
        else ""
    )
    pw_keys = set(re.findall(r"`(doi:[^`]+|arxiv:[^`]+|title:[^`]+)`", pw))
    abs_only = {r["identity_key"] for r in papers if r.get("access_status") == "abstract-only"}
    unlisted = sorted(abs_only - pw_keys)
    chk(
        "Every abstract-only source is listed in paywalled.md",
        not unlisted,
        f"{len(unlisted)} of {len(abs_only)} abstract-only sources are not listed"
        + (f", e.g. {unlisted[0]}" if unlisted else ""),
    )
    bad_blocked = [
        b
        for b in re.findall(r"^\|\s*`[^`]+`\s*\|[^|]*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|", pw, re.M)
        if b not in BLOCKED_BY
    ]
    chk(
        "paywalled.md blocked_by values are from the controlled list",
        not bad_blocked,
        f"{len(bad_blocked)} invalid" + (f", e.g. {bad_blocked[0]}" if bad_blocked else ""),
    )

    # --- report
    rdir = out / "report"
    rfiles = sorted(p.name for p in rdir.iterdir() if p.suffix == ".md") if rdir.is_dir() else []
    tagged_files = [f for f in rfiles if f not in {"08_papers.md", "index.md"}]
    text = "\n".join((rdir / f).read_text(encoding="utf-8") for f in tagged_files)
    all_text = "\n".join((rdir / f).read_text(encoding="utf-8") for f in rfiles)
    chk(
        "Report sections present",
        len(rfiles) >= 5,
        f"{len(rfiles)} section files: {', '.join(rfiles)}",
    )

    def prose_of(block: str) -> str:
        return "\n".join(
            ln
            for ln in block.splitlines()
            if not ln.lstrip().startswith(("#", "|", "```", ">", "---", "- ", "* "))
        )

    paras = [p for p in (prose_of(b) for b in re.split(r"\n\s*\n", text)) if len(p.split()) > 25]
    untagged = [p.strip() for p in paras if not any(t in p for t in TAGS)]
    chk(
        "Substantive paragraphs carry an evidence tag",
        not untagged,
        f"{len(untagged)} of {len(paras)} untagged"
        + (f'; first: "{untagged[0][:70]}…"' if untagged else ""),
    )
    cited = set(re.findall(r"\[\[([^\]]+)\]\]", all_text))
    unknown = sorted(c for c in cited if c not in set(pkeys))
    chk(
        "Every citation resolves to papers.csv",
        not unknown,
        f"{len(unknown)} unknown, e.g. {unknown[0]}"
        if unknown
        else f"{len(cited)} citations, all resolve",
    )
    absent = re.findall(r"\[Absent-searched\][^\n]*", all_text)
    unbacked = [a for a in absent if not re.search(r"q\d{3}", a)]
    chk("Absence claims cite query ids", not unbacked, f"{len(unbacked)} of {len(absent)} unbacked")

    banned = re.findall(
        r"\b(promising|great potential|revolutionar|revolutioni[sz]|game[- ]chang|"
        r"paradigm shift|cutting[- ]edge|state of the art\b)\w*",
        all_text,
        re.I,
    )
    chk(
        "No promotional framing",
        not banned,
        f"found: {', '.join(sorted(set(banned))[:5])}" if banned else "clean",
    )

    prescriptive = re.findall(PRESCRIPTIVE, all_text, re.I)
    chk(
        "No prescription for TANGO",
        not prescriptive,
        f'{len(prescriptive)} prescriptive sentences, e.g. "{prescriptive[0]}"'
        if prescriptive
        else "clean",
    )

    # Every touchpoint gets a subsection, including the ones nothing matched. A section
    # that silently omits its empty categories reads as a survey of what exists.
    tp_file = rdir / "03_touchpoints.md"
    tp_text = tp_file.read_text(encoding="utf-8") if tp_file.exists() else ""
    # Headings only. A touchpoint mentioned in passing in someone else's paragraph is not
    # a subsection, and matching anywhere in the file would accept exactly that.
    tp_headings = " ".join(re.findall(r"^#{2,4}\s+(.+)$", tp_text, re.M))
    tp_missing = sorted(t for t in TOUCHPOINTS - {"none"} if t not in tp_headings)
    chk(
        "03_touchpoints.md covers every touchpoint",
        not tp_missing,
        f"{len(tp_missing)} touchpoints have no subsection"
        + (f", e.g. {tp_missing[0]}" if tp_missing else ""),
    )

    # --- report
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
        "# Self-audit\n\nGenerated by `scripts/audit_tango.py` from the output files.\n\n"
        + table
        + "\n",
        encoding="utf-8",
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
