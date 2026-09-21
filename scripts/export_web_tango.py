#!/usr/bin/env python3
"""Export the 02_tango run as the JSON document the web front end compiles in.

    python3 scripts/export_web_tango.py --out outputs/02_tango/v0.1

Writes `web/src/data/tango.web.json`. Same job as `export_web.py`, different
research space and one extra artifact — `transfer.csv`, which `export_web.py`
has no reason to know about.

**The 01 exporter is imported, not copied, wherever the two runs share a
column.** `papers.csv` has the same schema in both runs by design (`SCHEMA_tango.md`),
so `agentic_techniques`, `architecture`, `base_model`, the framework derivation and
every parser over `papers.md` / `08_papers.md` / `RUN.md` / `audit.md` are
`export_web`'s functions, called here rather than restated. What is genuinely new is
02's own vocabulary — domain groups instead of subfields, its periphery, its cut
reasons — and the one artifact 01 does not have: `transfer.csv`, which records what
each system actually drives, at what autonomy, through what interface.

Same two rules as `export_web.py`: nothing is inferred beyond the one disclosed
derivation (the framework facet), and a number that can be counted from a CSV is
counted here rather than lifted out of prose.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import export_web as ew

Json = dict[str, Any]
Row = dict[str, str]

# --- 02's own vocabulary, mirrored from SCHEMA_tango.md and reference/queries_tango.json ---
# Order matters here for the same reason it does in export_web.py: a fixed axis lets
# a zero mean something and lets two runs be compared row for row.

SUBFIELDS = [
    "simulation_orchestration",
    "solver_control",
    "optimisation_uq",
    "energy_systems",
    "geoenergy_subsurface",
    "scientific_computing",
    "computational_discovery",
    "simulation_general",
]

PERIPHERY = ["software_engineering", "lab_automation", "interface_agents", "science_of_science"]

CUT_REASONS = [
    "not-agentic",
    "no-simulation-target",
    "periphery",
    "pre-llm-only",
    "duplicate",
    "not-a-source",
    "no-abstract-untriageable",
]

TOUCHPOINTS = [
    "config-generation",
    "topology-construction",
    "solver-control",
    "optimisation-loop",
    "surrogate-modelling",
    "uncertainty-quantification",
    "hpc-scale-out",
    "tool-exposure",
    "results-interpretation",
    "techno-economic",
    "verification-regression",
    "provenance-reproducibility",
    "none",
]

INTERFACES = ["api", "cli", "file-io", "mcp", "code-execution", "gui", "not stated"]

AUTONOMY = ["suggests", "executes-with-approval", "executes-and-iterates", "not stated"]

BLOCKED_BY = [
    "paywall",
    "bot-protection",
    "no-full-text-anywhere",
    "tooling-failure",
    "no-abstract-in-any-api",
]

# Section files, in report order, mapped onto where the page puts them. 02 has one
# section 01 does not: `03_touchpoints.md`, which is the run's central axis and gets
# its own page group rather than being folded into `systems`.
SECTIONS = [
    ("00_executive_summary.md", "overview"),
    ("01_control_patterns.md", "systems"),
    ("02_architectures.md", "systems"),
    ("03_touchpoints.md", "touchpoints"),
    ("04_evaluation.md", "evidence"),
    ("05_maturity.md", "evidence"),
    ("06_failure_and_limits.md", "evidence"),
    ("07_periphery.md", "periphery"),
]


def parse_transfer(rows: list[Row]) -> dict[str, Json]:
    """`transfer.csv` keyed by `identity_key`, with its `;`-joined column split.

    One row per admitted source, core and context alike, same as `papers.csv` — the
    join is by `identity_key`, checked at the call site rather than here.
    """
    out: dict[str, Json] = {}
    for r in rows:
        key = r["identity_key"]
        touchpoints = [t.strip() for t in r["tango_touchpoints"].split(";") if t.strip()]
        out[key] = {
            "touchpoints": touchpoints or ["none"],
            "what_it_drives": r["what_it_drives"],
            "interface": r["interface"] or "not stated",
            "autonomy": r["autonomy"] or "not stated",
            "failure_handling": r["failure_handling"],
            "access_status": r["access_status"],
        }
    return out


# One table, one row per source whose full text could not be retrieved. The header
# row's first cell is always `identity_key`, which is what makes this table
# distinguishable from `unreachable.md`'s prose sections without matching on a
# heading — `paywalled.md` is one table for the whole file, not one per heading.
def parse_paywalled(text: str) -> Json:
    """Row count and `blocked_by` distribution from `paywalled.md`'s one table.

    `would_change: nothing` is counted separately: it is the sub-count that answers
    "how many of these would change nothing if unblocked", which is the honest
    complement to the funnel's own admission that it cannot count paywall losses by
    cause alone.
    """
    blocked_by: Counter[str] = Counter()
    total = 0
    would_change_nothing = 0
    in_table = False
    header: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue  # the separator row
        if cells[0].lower() == "identity_key":
            in_table = True
            header = [c.lower() for c in cells]
            continue
        if not in_table:
            continue
        total += 1
        row = dict(zip(header, cells, strict=False))
        blocked = row.get("blocked_by", "").strip()
        if blocked:
            blocked_by[blocked] += 1
        if row.get("would_change", "").strip().lower() == "nothing":
            would_change_nothing += 1
    return {
        "total": total,
        "blocked_by": ew.facet(blocked_by, BLOCKED_BY, total, keep_zeros=False),
        "would_change_nothing": would_change_nothing,
    }


def build(out: Path) -> Json:
    papers_rows = ew.read_csv(out / "papers.csv")
    if not papers_rows:
        sys.exit(f"no papers.csv under {out} — nothing to export")
    screening = ew.read_csv(out / "screening.csv")
    queries = ew.read_csv(out / "queries.csv")
    transfer_rows = ew.read_csv(out / "transfer.csv")
    audit = ew.parse_audit(ew.read_text(out / "audit.md"))
    run_log = ew.parse_run_log(ew.read_text(out / "RUN.md"))
    extracts = ew.parse_extracts(ew.read_text(out / "papers.md"))
    annotations = ew.parse_annotations(ew.read_text(out / "report" / "08_papers.md"))
    countries_by_key, openalex_journals, openalex_types = ew.read_enrichment(out)
    unreachable = ew.parse_unreachable(ew.read_text(out / "unreachable.md"))
    paywalled = parse_paywalled(ew.read_text(out / "paywalled.md"))
    shortlisted_by_group, group_of = ew.parse_shortlist(ew.read_text(out / "shortlist.md"))
    transfer_by_key = parse_transfer(transfer_rows)

    names = {r["identity_key"]: r["system_id"] for r in papers_rows}
    refs = {r["identity_key"]: i for i, r in enumerate(papers_rows, start=1)}
    core_rows = [r for r in papers_rows if r["tier"] == "core"]

    papers: list[Json] = []
    for r in papers_rows:
        key = r["identity_key"]
        techniques = [t.strip() for t in r["agentic_techniques"].split(";") if t.strip()]
        papers.append(
            {
                "key": key,
                "ref": refs[key],
                "tier": r["tier"],
                "system_id": r["system_id"],
                "title": r["title"],
                "authors": r["authors"],
                "year": int(r["year"]) if r["year"].isdigit() else None,
                "venue": r["venue"],
                "url": r["url"],
                "source_type": ew.source_type_of(r["source_type"], openalex_types.get(key, "")),
                "subfield": r["subfield"],
                "subfield_secondary": r["subfield_secondary"],
                "task": r["task"],
                "techniques": techniques,
                "architecture": r["architecture"],
                "base_model": r["base_model"],
                "model_families": ew.model_families(r["base_model"]),
                "countries": countries_by_key.get(key, []),
                "journal": r["venue"].strip() or openalex_journals.get(key, ""),
                "tools_used": r["tools_used"],
                "frameworks": ew.frameworks_of(r["tools_used"], r["base_model"]),
                "evaluation_method": r["evaluation_method"],
                "baseline": r["baseline"],
                "held_out": r["held_out"],
                "data_type": r["data_type"],
                "reported_result": r["reported_result"],
                "maturity_claimed": r["maturity_claimed"],
                "maturity_demonstrated": r["maturity_demonstrated"],
                "limitations": r["author_stated_limitations"],
                "code_availability": r["code_availability"],
                "access_status": r["access_status"],
                "found_via": r["found_via"],
                "annotation": ew.summary(annotations.get(key, ""), r["task"]),
                "extract": extracts.get(key),
            }
        )

    n = len(papers)
    core = [p for p in papers if p["tier"] == "core"]
    context = [p for p in papers if p["tier"] == "context"]

    fields: list[Json] = []
    for name in SUBFIELDS + sorted({p["subfield"] for p in papers} - set(SUBFIELDS)):
        rows = [p for p in papers if p["subfield"] == name]
        if not rows:
            continue
        rows_core = [p for p in rows if p["tier"] == "core"]
        fields.append(
            {
                "label": name,
                "n": len(rows),
                "core": len(rows_core),
                "context": len(rows) - len(rows_core),
                "share": round(len(rows) / n, 4),
                "shortlisted": shortlisted_by_group.get(name, 0),
                "admitted_share": (
                    round(len(rows) / shortlisted_by_group[name], 4)
                    if shortlisted_by_group.get(name)
                    else None
                ),
                "from_own_query": sum(1 for p in rows if group_of.get(p["key"]) == name),
                "maturity": ew.facet(
                    Counter(p["maturity_demonstrated"] for p in rows_core),
                    ew.MATURITY,
                    len(rows_core),
                ),
                "systems": sorted({p["system_id"] for p in rows_core}),
            }
        )

    matched: Counter[str] = Counter(f for p in papers for f in p["frameworks"])
    orchestration = {
        label for label, kind, _p, _c in ew.FRAMEWORKS if kind in ew.ORCHESTRATION_KINDS
    }
    frameworks_coverage = {
        "core_total": len(core),
        "core_named": sum(1 for p in core if set(p["frameworks"]) & orchestration),
        "total": n,
        "named": sum(1 for p in papers if set(p["frameworks"]) & orchestration),
        "core_any_tool": sum(1 for p in core if p["frameworks"]),
        "context_any_tool": sum(1 for p in context if p["frameworks"]),
        "context_total": len(context),
    }

    framework_kinds: list[Json] = []
    for kind in ew.FRAMEWORK_KINDS:
        labels = [label for label, k, _p, _c in ew.FRAMEWORKS if k == kind]
        counts = Counter(f for f in matched.elements() if f in labels)
        items = [
            {
                "label": label,
                "n": counts[label],
                "share": round(counts[label] / n, 4),
                "core": sum(1 for p in core if label in p["frameworks"]),
            }
            for label in labels
            if counts[label]
        ]
        if items:
            framework_kinds.append(
                {"kind": kind, "items": sorted(items, key=lambda i: (-i["n"], i["label"]))}
            )

    periphery_screened = Counter(
        r["subfield"] for r in screening if r["cut_reason"] == "periphery" and r["subfield"]
    )
    periphery_available: Counter[str] = Counter()
    for q in queries:
        if q["scope"] == "periphery" and q["n_available"].isdigit():
            periphery_available[q["domain_group"]] += int(q["n_available"])

    sample = [r for r in screening if r["from_audit_sample"] == "yes"]

    # --- what each admitted system actually drives -------------------------------
    # `transfer.csv` covers admitted sources core and context alike, same as
    # `papers.csv`; a context row is mostly `not stated`, which SCHEMA_tango.md
    # records as the correct entry — the abstract did not describe the interface.
    transfer_rows_all = [transfer_by_key[p["key"]] for p in papers if p["key"] in transfer_by_key]
    transfer_rows_core = [transfer_by_key[p["key"]] for p in core if p["key"] in transfer_by_key]
    touchpoints_all = Counter(t for row in transfer_rows_all for t in row["touchpoints"])
    touchpoints_core = Counter(t for row in transfer_rows_core for t in row["touchpoints"])
    stated_failure = sum(
        1
        for row in transfer_rows_core
        if row["failure_handling"] and row["failure_handling"] != "not stated"
    )
    drives = [
        {
            "key": p["key"],
            "system_id": p["system_id"],
            "touchpoints": transfer_by_key[p["key"]]["touchpoints"],
            "what_it_drives": transfer_by_key[p["key"]]["what_it_drives"],
            "interface": transfer_by_key[p["key"]]["interface"],
            "autonomy": transfer_by_key[p["key"]]["autonomy"],
        }
        for p in core
        if p["key"] in transfer_by_key
    ]

    transfer = {
        "touchpoints": ew.facet(touchpoints_core, TOUCHPOINTS, len(transfer_rows_core)),
        "touchpoints_all": ew.facet(touchpoints_all, TOUCHPOINTS, len(transfer_rows_all)),
        "interface": ew.facet(
            Counter(row["interface"] for row in transfer_rows_core), INTERFACES, len(core)
        ),
        "autonomy": ew.facet(
            Counter(row["autonomy"] for row in transfer_rows_core), AUTONOMY, len(core)
        ),
        "failure_handling": {
            "stated": stated_failure,
            "not_stated": len(transfer_rows_core) - stated_failure,
            "total": len(transfer_rows_core),
        },
        "drives": drives,
    }

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "run": {
            "path": str(out),
            "version": out.name,
            "date": run_log.get("date", ""),
            "prompt": run_log.get("prompt", ""),
            "model": run_log.get("model", ""),
            "purpose": run_log.get("purpose", ""),
            "harvested": audit["harvested"],
            "shortlisted": audit["shortlisted"],
            "screened": len(screening),
            "admitted": n,
            "core": len(core),
            "context": len(context),
            "audit_sample": len(sample),
            "false_negatives": sum(1 for r in sample if r["decision"] == "in"),
            "api_calls": len(queries),
            "api_errors": sum(1 for q in queries if q["status"] != "ok"),
            "queries_core": sum(1 for q in queries if q["scope"] == "core"),
            "queries_periphery": sum(1 for q in queries if q["scope"] == "periphery"),
        },
        "funnel": [
            {
                "label": "Records harvested",
                "n": audit["harvested"],
                "of": None,
                "what": "unique records from OpenAlex and arXiv across "
                f"{len(queries)} API and web calls",
            },
            {
                "label": "Shortlisted by triage",
                "n": audit["shortlisted"],
                "of": audit["harvested"],
                "what": "passed a deterministic score on agent vocabulary and domain fit",
            },
            {
                "label": "Screened with a reason",
                "n": len(screening),
                "of": audit["harvested"],
                "what": "an in-or-out decision per record, each with a stated cause",
                "note": (
                    f"More than the shortlist, because {len(sample)} records were also "
                    "screened from below the triage cut to measure what the cut "
                    f"discarded. That sample found {sum(1 for r in sample if r['decision'] == 'in')} "
                    "false negatives, which is what makes the cut a measurement rather "
                    "than an assumption."
                ),
            },
            {
                "label": "Excluded as not agentic",
                "n": sum(1 for r in screening if r["cut_reason"] == "not-agentic"),
                "of": len(screening),
                "what": "an LLM is used, but nothing plans, calls a tool, or acts on a result",
            },
            {
                "label": "Excluded for no simulation target",
                "n": sum(1 for r in screening if r["cut_reason"] == "no-simulation-target"),
                "of": len(screening),
                "what": "agentic, but what it acts on is not a simulator, solver, "
                "optimiser or scientific code",
            },
            {
                "label": "Admitted as agentic and driving a simulation target",
                "n": n,
                "of": len(screening),
                "what": "the system decides something for itself, and what it acts on "
                "is a simulator, solver, optimiser, techno-economic model or scientific code",
                "emphasis": True,
            },
            {
                "label": "Full text read",
                "n": len(core),
                "of": n,
                "what": "the only rows that can be characterised or rated",
            },
            {
                "label": "Full text not obtained",
                "n": len(context),
                "of": n,
                "what": "abstract only: paywalled, delivery refused, a software "
                "deposit, or no manuscript",
                "note": (
                    f"{unreachable.get('full_text_refused', 0)} of these are tabulated in "
                    "unreachable.md as every route to the text refused, and "
                    f"{unreachable.get('no_abstract', 0)} had no abstract in any API. "
                    f"{paywalled['total']} sources are tabulated in paywalled.md as "
                    "specifically paywall-blocked, of which "
                    f"{paywalled['would_change_nothing']} would change nothing about "
                    "this run's ratings if unblocked. The remaining causes are "
                    "narrated rather than tallied."
                ),
            },
        ],
        "audit": audit,
        "rubric": ew.MATURITY_RUBRIC,
        "tags": ew.TAGS,
        "fields": fields,
        "techniques": ew.facet(ew.multi(papers_rows, "agentic_techniques"), ew.TECHNIQUES, n),
        "techniques_core": ew.facet(
            ew.multi(core_rows, "agentic_techniques"), ew.TECHNIQUES, len(core)
        ),
        "frameworks": framework_kinds,
        "frameworks_coverage": frameworks_coverage,
        "framework_terms": [
            {"label": label, "kind": kind, "matched": bool(matched[label])}
            for label, kind, _pattern, _cased in ew.FRAMEWORKS
        ],
        "architectures": ew.facet(Counter(p["architecture"] for p in papers), ew.ARCHITECTURES, n),
        "architectures_core": ew.facet(
            Counter(p["architecture"] for p in core), ew.ARCHITECTURES, len(core)
        ),
        "maturity": ew.facet(
            Counter(p["maturity_demonstrated"] for p in core), ew.MATURITY, len(core)
        ),
        "models": ew.facet(
            Counter(f for p in papers for f in p["model_families"]),
            [m for m, _ in ew.MODEL_FAMILIES],
            n,
            keep_zeros=False,
        ),
        "models_core": ew.facet(
            Counter(f for p in core for f in p["model_families"]),
            [m for m, _ in ew.MODEL_FAMILIES],
            len(core),
            keep_zeros=False,
        ),
        "models_multi": sum(1 for p in core if len(p["model_families"]) > 1),
        "types": ew.facet(Counter(p["source_type"] for p in papers), [], n, keep_zeros=False),
        "journals": ew.facet(
            Counter(p["journal"] for p in papers if p["journal"]), [], n, keep_zeros=False
        ),
        "countries": ew.facet(
            Counter(c for p in papers for c in p["countries"]),
            [],
            sum(1 for p in papers if p["countries"]),
            keep_zeros=False,
        ),
        "countries_coverage": {
            "with_country": sum(1 for p in papers if p["countries"]),
            "total": n,
            "multi_country": sum(1 for p in papers if len(p["countries"]) > 1),
            "distinct": len({c for p in papers for c in p["countries"]}),
        },
        "data_types": ew.facet(
            Counter(p["data_type"] for p in core),
            ["benchmark", "synthetic", "real-field", "not stated"],
            len(core),
            keep_zeros=False,
        ),
        "held_out": ew.facet(
            Counter(p["held_out"] for p in core),
            ["yes", "no", "not stated"],
            len(core),
            keep_zeros=False,
        ),
        "years": ew.facet(Counter(str(p["year"]) for p in papers if p["year"]), [], n),
        "cuts": ew.facet(
            Counter(r["cut_reason"] for r in screening if r["cut_reason"]),
            CUT_REASONS,
            len(screening),
            keep_zeros=False,
        ),
        "periphery": [
            {
                "label": name,
                "screened": periphery_screened.get(name, 0),
                "available": periphery_available.get(name, 0),
            }
            for name in PERIPHERY
            if periphery_screened.get(name) or periphery_available.get(name)
        ],
        "queries": [
            {
                "id": q["query_id"],
                "api": q["api"],
                "band": q["band"],
                "scope": q["scope"],
                "group": q["domain_group"],
                "query": q["query"],
                "status": q["status"],
                "available": int(q["n_available"]) if q["n_available"].isdigit() else None,
                "results": int(q["n_results"]) if q["n_results"].isdigit() else None,
                "new": int(q["n_new_unique"]) if q["n_new_unique"].isdigit() else None,
            }
            for q in queries
        ],
        "report": ew.parse_report(out / "report", names, refs, SECTIONS),
        "papers": papers,
        "transfer": transfer,
        "paywalled": paywalled,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--out", required=True, help="run directory, e.g. outputs/02_tango/v0.1")
    ap.add_argument("--to", default="web/src/data/tango.web.json", help="where to write the export")
    args = ap.parse_args(argv)

    data = build(Path(args.out))
    to = Path(args.to)
    to.parent.mkdir(parents=True, exist_ok=True)
    with to.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")

    run = data["run"]
    size = to.stat().st_size / 1024
    unresolved = sum(
        1
        for s in data["report"]
        for b in s["blocks"]
        if b["kind"] == "para"
        for sp in b["spans"]
        if sp["t"] == "cite" and not sp["resolved"]
    )
    ew.log(f"{to}  {size:.0f} KB")
    ew.log(
        f"  run {run['version']}: {run['admitted']} admitted "
        f"({run['core']} core, {run['context']} context) in {len(data['fields'])} domain groups"
    )
    ew.log(
        f"  {len(data['report'])} report sections, "
        f"{sum(len(s['blocks']) for s in data['report'])} blocks, "
        f"{unresolved} unresolved citations"
    )
    ew.log(
        f"  {sum(t['n'] for t in data['transfer']['touchpoints'] if t['label'] != 'none')} "
        f"touchpoint claims across {len(data['transfer']['drives'])} core systems"
    )
    if unresolved:
        ew.log("  WARNING: unresolved citations render as broken links; run scripts/audit_tango.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
