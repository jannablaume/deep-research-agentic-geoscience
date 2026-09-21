#!/usr/bin/env python3
"""Export the 03_gaps run as the JSON document the web front end compiles in.

    python3 scripts/export_web_gaps.py --out outputs/03_gaps/v0.1-run2

Writes `web/src/data/gaps.web.json`. 03 harvests nothing and reads no `papers.csv` of
its own, so this shares almost none of `export_web.py`'s machinery — the one thing it
does reuse is `spans()`, because `gaps.md` carries the same `[Certain]` /
`[Absent-searched]` / `**bold**` conventions as the other two reports and there is no
reason to parse that twice.

The whole run is `gap_candidates.csv` (what a script found, mechanically) narrowed into
`gaps.md` (what a person and a verification pass decided those candidates support) plus
a discard ledger (what was found and set aside, with a reason). Nothing here decides
which of that is correct — a number is counted from those two files or it is not stated,
same rule as the other two exporters.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import export_web as ew
from gaps import KINDS

Json = dict[str, Any]
Row = dict[str, str]

VERDICTS = ["confirmed-absent", "partially-addressed", "refuted", "undecidable"]

# `gap_candidates.csv`'s `kind` column, in the order `gaps.py`'s module docstring
# introduces them — so a chart over it reads as a list, not an alphabetisation.
KIND_ORDER = [
    "author-limitation",
    "absence-claim",
    "evidence-hole",
    "evaluation-hole",
    "empty-category",
    "unread-source",
    "claim-gap",
]


def parse_run_table(text: str, heading_fragment: str) -> list[Row]:
    """The one markdown table under a `## ` heading containing `heading_fragment`.

    `RUN.md`'s "which runs were read" table is the only place this run's own record
    names the exact directories a candidate's `evidence_ref` can be resolved against —
    not the run table in AGENTS.md, which is a pointer to *current* work and drifts as
    soon as a later run corrects one of the two source directories in place.
    """
    start = None
    for m in re.finditer(r"^##\s+(.*)$", text, re.M):
        if heading_fragment in m.group(1):
            start = m.end()
            break
    if start is None:
        return []
    rest = text[start:]
    end = rest.find("\n## ")
    body = rest[: end if end >= 0 else len(rest)]

    rows: list[Row] = []
    header: list[str] = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip(" `") for c in line.strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        if not header:
            header = [c.lower() for c in cells]
            continue
        rows.append(dict(zip(header, cells, strict=False)))
    return rows


FIELD_LINE = re.compile(r"^- (candidates|runs|verdict|evidence|checked):\s*(.*)$")


def parse_gaps_md(text: str) -> tuple[list[Json], list[Json]]:
    """`gaps.md` into its gap blocks and its discard ledger.

    Every top-level `## ` section is either a gap (`## G01 — <title>`) or the one
    closing section, `## Discarded candidates`. The prose inside a gap block is
    parsed exactly as a landscape report paragraph is — evidence tag, then
    `spans()` — because `gaps.md` uses the same inline conventions and carries no
    citations of its own to resolve, only bare `identity_key`s in running text.
    """
    gaps: list[Json] = []
    discarded: list[Json] = []
    for chunk in re.split(r"\n(?=## )", text):
        heading = re.match(r"^## (.*)$", chunk, re.M)
        if not heading:
            continue
        title_line = heading.group(1).strip()
        body = chunk[heading.end() :]

        m = re.match(r"^(G\d+)\s*—\s*(.*)$", title_line)
        if m:
            gaps.append(_parse_gap_block(m.group(1), m.group(2).strip(), body))
        elif title_line == "Discarded candidates":
            discarded = _parse_discard_ledger(body)
    return gaps, discarded


def _parse_gap_block(gap_id: str, title: str, body: str) -> Json:
    fields: dict[str, str] = {}
    prose_start = 0
    lines = body.splitlines(keepends=True)
    consumed = 0
    for line in lines:
        m = FIELD_LINE.match(line.strip())
        if m:
            fields[m.group(1)] = m.group(2).strip()
            consumed += len(line)
        elif line.strip() == "":
            consumed += len(line)
        else:
            break
    prose_start = consumed

    blocks: list[Json] = []
    for para in re.split(r"\n\s*\n", body[prose_start:]):
        para = para.strip()
        if not para:
            continue
        text = re.sub(r"\s+", " ", para).strip()
        tag = None
        tm = re.match(r"^\[(Certain|Likely|Absent-searched)\]\s*", text)
        if tm:
            tag, text = tm.group(1), text[tm.end() :]
        blocks.append({"kind": "para", "tag": tag, "spans": ew.spans(text, {}, {}), "cites": []})

    def split_list(value: str) -> list[str]:
        return [v.strip() for v in value.split(";") if v.strip()]

    return {
        "id": gap_id,
        "title": title,
        "candidates": split_list(fields.get("candidates", "")),
        "runs": split_list(fields.get("runs", "")),
        "verdict": fields.get("verdict", ""),
        "evidence": split_list(fields.get("evidence", "")),
        "checked": fields.get("checked", ""),
        "blocks": blocks,
    }


DISCARD_LINE = re.compile(r"^-\s+(\S+)\s+—\s+`([^`]+)`\.\s*(.*)$")


def _parse_discard_ledger(body: str) -> list[Json]:
    """The flat discard bullets only.

    `## Discarded candidates` also carries a `### Candidates of refuted gaps`
    subsection, which cross-references candidates already cited by a gap above —
    they are not additional discards, and counting them as such would double-count
    against `gaps.py`'s own accounting (`cited | discarded == every candidate`).
    """
    flat = body.split("\n### ", 1)[0]
    out: list[Json] = []
    for line in flat.splitlines():
        m = DISCARD_LINE.match(line.strip())
        if m:
            out.append({"id": m.group(1), "reason": m.group(2), "note": m.group(3).strip()})
    return out


def resolve_names(run_rows: list[Row], repo_root: Path) -> dict[str, str]:
    """`identity_key` → `system_id`, read from every source run's own `papers.csv`.

    `gaps.md` cites bare keys in running text rather than `[[key]]` markup, so
    there is nothing to resolve inline — this is for the evidence chips instead,
    so a reader can see which system an evidence key names without opening the
    source run.
    """
    names: dict[str, str] = {}
    for row in run_rows:
        directory = row.get("directory", "").strip("` ")
        if not directory:
            continue
        for r in ew.read_csv(repo_root / directory / "papers.csv"):
            names[r["identity_key"]] = r["system_id"]
    return names


def build(out: Path, repo_root: Path) -> Json:
    candidate_rows = ew.read_csv(out / "gap_candidates.csv")
    if not candidate_rows:
        sys.exit(f"no gap_candidates.csv under {out} — nothing to export")
    gaps_text = ew.read_text(out / "gaps.md")
    if not gaps_text:
        sys.exit(f"no gaps.md under {out} — nothing to export")

    run_log = ew.parse_run_log(ew.read_text(out / "RUN.md"))
    source_runs = parse_run_table(ew.read_text(out / "RUN.md"), "Which runs were read")
    audit = ew.parse_audit(ew.read_text(out / "audit.md"))
    names = resolve_names(source_runs, repo_root)

    gaps, discarded = parse_gaps_md(gaps_text)

    candidates: list[Json] = [
        {
            "id": r["candidate_id"],
            "run": r["run"],
            "kind": r["kind"],
            "subject": r["subject"],
            "statement": r["statement"],
            "evidence_ref": r["evidence_ref"],
            "count": int(r["count"]) if r["count"].isdigit() else None,
            "denominator": int(r["denominator"]) if r["denominator"].isdigit() else None,
        }
        for r in candidate_rows
    ]

    cited: set[str] = set()
    for g in gaps:
        cited.update(g["candidates"])
        # A gap's `kinds` is derived from the candidates it cites, so the page can
        # filter gaps by what kind of absence they synthesise without a second pass
        # over `gap_candidates.csv` client-side.
        kind_lookup = {c["id"]: c["kind"] for c in candidates}
        g["kinds"] = sorted({kind_lookup[cid] for cid in g["candidates"] if cid in kind_lookup})
        g["evidence_named"] = [
            {"key": e, "name": names.get(e, "")} for e in g["evidence"] if e in names
        ]

    total = len(candidates)
    discarded_ids = {d["id"] for d in discarded}
    unaccounted = sorted({str(c["id"]) for c in candidates} - cited - discarded_ids)

    verdict_counts = Counter(g["verdict"] for g in gaps)
    kind_counts = Counter(c["kind"] for c in candidates)
    run_counts = Counter(c["run"] for c in candidates)
    discard_reason_counts = Counter(d["reason"] for d in discarded)

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "run": {
            "path": str(out),
            "version": out.name,
            "date": run_log.get("date", ""),
            "prompt": run_log.get("prompt", ""),
            "model": run_log.get("model", ""),
            "source_runs": [
                {
                    "name": r.get("run", ""),
                    "directory": r.get("directory", "").strip("` "),
                    "commit": r.get("commit", "").strip("` "),
                }
                for r in source_runs
            ],
        },
        "audit": audit,
        "candidates_total": total,
        "gaps_total": len(gaps),
        "cited_total": len(cited),
        "discarded_total": len(discarded),
        "unaccounted": unaccounted,
        "verdicts": ew.facet(verdict_counts, VERDICTS, len(gaps)),
        "kinds": ew.facet(kind_counts, KIND_ORDER, total),
        "runs": ew.facet(run_counts, sorted(run_counts), total, keep_zeros=False),
        "discard_reasons": ew.facet(
            discard_reason_counts, sorted(discard_reason_counts), len(discarded), keep_zeros=False
        ),
        "gaps": gaps,
        "discarded": discarded,
        "candidates": candidates,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--out", required=True, help="run directory, e.g. outputs/03_gaps/v0.1-run2")
    ap.add_argument(
        "--repo-root",
        default=".",
        help="repository root the source runs' papers.csv paths are relative to",
    )
    ap.add_argument("--to", default="web/src/data/gaps.web.json", help="where to write the export")
    args = ap.parse_args(argv)

    data = build(Path(args.out), Path(args.repo_root))
    to = Path(args.to)
    to.parent.mkdir(parents=True, exist_ok=True)
    with to.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")

    size = to.stat().st_size / 1024
    ew.log(f"{to}  {size:.0f} KB")
    ew.log(
        f"  {data['candidates_total']} candidates -> {data['gaps_total']} gaps stated "
        f"({data['cited_total']} candidates cited), {data['discarded_total']} discarded"
    )
    for v in VERDICTS:
        n = sum(1 for g in data["gaps"] if g["verdict"] == v)
        if n:
            ew.log(f"  {v}: {n}")
    if data["unaccounted"]:
        ew.log(
            f"  WARNING: {len(data['unaccounted'])} candidates neither cited nor discarded: "
            f"{', '.join(data['unaccounted'][:10])}"
        )
    unnamed_kinds = sorted({str(c["kind"]) for c in data["candidates"]} - KINDS)
    if unnamed_kinds:
        ew.log(f"  WARNING: candidate kinds outside the controlled list: {unnamed_kinds}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
