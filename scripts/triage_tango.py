#!/usr/bin/env python3
"""Rank the 02_tango corpus so the model reads a bounded, ordered shortlist.

Same job as `triage.py`, different research space. The 01 pipeline is frozen, so this
is a second script rather than a flag on the first — but the two halves of the score
are split deliberately:

- **The agentic half is imported, not copied.** `triage.score()` decides whether a
  record is LLM-era and whether it plans, calls tools or acts, and that judgment is
  identical in both runs. It has been wrong twice (a case-insensitive `ReAct`, an
  LLM-corroboration hole) and carries a test battery recording both. Importing it
  means a fix lands in both runs at once; it also means **a change to `triage.py`'s
  vocabulary is a method change for this run too**, and belongs in a version bump with
  a re-triage here as well.
- **The domain half is this file's, and it comes from the config.** `triage.py` asks
  "which of the ten solid-earth subfields is this", which answers `none` for almost
  everything an agent could drive a simulator for. The vocabulary here lives in
  `reference/queries_tango.json` under `triage`, next to the queries that harvested
  the corpus, because a group that is harvested but has no scoring pattern is dropped
  from the shortlist without appearing in any count.

Also computed: `touchpoints`, a regex pass for TANGO's own surfaces — input-deck
generation, solver control, the optimisation loop, surrogates, UQ, HPC scale-out, tool
exposure, techno-economics, regression testing, provenance. It is a **sorting aid and a
counted signal, never an admission**: a hit does not mean the system is relevant to
TANGO, and no hit does not mean it is not.

    python3 scripts/triage_tango.py --out outputs/02_tango/v0.1 [--min-score 3]

Writes, in --out: triage.csv, shortlist.md, audit_sample.md, triage_stats.md.
No network calls.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, NamedTuple

import triage

# One row of screened.csv with the scores merged in. Values are a mix of str and int,
# so `Any` is the honest annotation rather than a TypedDict with every field optional.
Row = dict[str, Any]
Config = dict[str, Any]

csv.field_size_limit(10_000_000)

DEFAULT_CONFIG = "reference/queries_tango.json"

# The fields taken from `triage.score()`. All four are computed from agent and LLM
# vocabulary alone — no domain term reaches them — which is what makes it safe to keep
# them and recompute scope and group here.
AGENTIC_FIELDS = ("agentic_score", "strong_hits", "llm_present", "pre_llm_flag", "signals")


class Vocabulary(NamedTuple):
    """The domain half of the score, compiled from the run's query config."""

    domain: dict[str, re.Pattern[str]]
    periphery: dict[str, re.Pattern[str]]
    general: re.Pattern[str]
    touchpoints: dict[str, re.Pattern[str]]


def load_config(path: Path) -> Config:
    if not path.exists():
        raise SystemExit(
            f"{path} not found — triage_tango.py needs the query config it was harvested with"
        )
    with path.open(encoding="utf-8") as f:
        cfg: Config = json.load(f)
    return cfg


def load_vocabulary(cfg: Config) -> Vocabulary:
    """Compile the triage vocabulary, and refuse a config whose halves disagree.

    The failure this guards against is silent: a domain group with queries but no
    scoring pattern harvests records that then match nothing, score `scope: none`, and
    are cut by `above()` no matter how high they score. In the v0.5 run that shape cost
    190 records and was invisible in every count until someone read a sample by hand.
    """
    tri = cfg.get("triage")
    if not tri:
        raise SystemExit(
            "config has no `triage` block. Every domain group that is harvested needs a "
            "scoring pattern, or its records are dropped from the shortlist without "
            "appearing in any count."
        )
    missing: list[str] = []
    extra: list[str] = []
    for scope in ("core", "periphery"):
        harvested = set(cfg["domain_groups"].get(scope, {}).get("groups", {}))
        scored = {k for k in tri.get(scope, {}) if not k.startswith("_")}
        missing += [f"{scope}.{g}" for g in sorted(harvested - scored)]
        extra += [f"{scope}.{g}" for g in sorted(scored - harvested)]
    if missing or extra:
        for g in missing:
            print(f"config error: {g} is harvested but has no triage pattern", file=sys.stderr)
        for g in extra:
            print(f"config error: {g} has a triage pattern but is never harvested", file=sys.stderr)
        raise SystemExit("queries config: `triage` and `domain_groups` must name the same groups")
    if not tri.get("general"):
        raise SystemExit(
            "config has no `triage.general` fallback. Without it a record that names no "
            "specific group scores `scope: none` and is cut regardless of its score."
        )

    def compiled(block: dict[str, str]) -> dict[str, re.Pattern[str]]:
        return {k: re.compile(v, re.IGNORECASE) for k, v in block.items() if not k.startswith("_")}

    return Vocabulary(
        domain=compiled(tri["core"]),
        periphery=compiled(tri["periphery"]),
        general=re.compile(tri["general"], re.IGNORECASE),
        touchpoints=compiled(tri.get("touchpoints", {})),
    )


def score(row: Row, vocab: Vocabulary) -> Row:
    """Agentic score from `triage.score()`; scope, group and touchpoints from here."""
    text = f"{row.get('title', '')} . {row.get('abstract', '')}"
    base = triage.score(row)
    out: Row = {k: base[k] for k in AGENTIC_FIELDS}

    dom = {k: len(r.findall(text)) for k, r in vocab.domain.items() if r.search(text)}
    per = {k: len(r.findall(text)) for k, r in vocab.periphery.items() if r.search(text)}
    general = len(vocab.general.findall(text))
    if dom:
        group, scope, domain_score = max(dom, key=lambda k: dom[k]), "core", sum(dom.values())
    elif per:
        group, scope, domain_score = max(per, key=lambda k: per[k]), "periphery", sum(per.values())
    elif general:
        # The fallback bucket, and its score has to count too. It was `sum(dom) or
        # sum(per)` — zero for every record rescued here — so the default `--min-domain 1`
        # deleted the whole bucket: 11 of 557 on the smoke corpus, invisible in every
        # count. That is the v0.5 `scope: none` regression arriving through a different
        # door, and it is why the knob counts what the fallback matched.
        group, scope, domain_score = "simulation_general", "core", general
    else:
        group, scope, domain_score = "", "none", 0

    touched = sorted(k for k, r in vocab.touchpoints.items() if r.search(text))
    out.update(
        {
            "domain_score": domain_score,
            "scope_computed": scope,
            "group_computed": group,
            "touchpoints": ";".join(touched),
            "n_touchpoints": len(touched),
        }
    )
    return out


def digest(r: Row, words: int = 55) -> str:
    a = " ".join((r.get("abstract") or "").split()[:words])
    if r.get("doi"):
        ident = f"doi:{r['doi']}"
    elif r.get("arxiv_id"):
        ident = f"arXiv:{r['arxiv_id']}"
    else:
        ident = r.get("url", "")
    return (
        f"### {r['identity_key']}\n"
        f"**{r.get('title', '')}** ({r.get('year', '')}) — {r.get('venue', '') or 'n/a'} · "
        f"cites {r.get('cited_by', '') or '0'} · score {r['agentic_score']} "
        f"(strong {r['strong_hits']}) · {r['scope_computed']}/{r['group_computed']} · {ident}\n"
        f"signals: {r['signals'] or 'none'}\n"
        f"touchpoints: {r['touchpoints'] or 'none'}\n"
        f"{a}{'…' if a else '(no abstract)'}\n"
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument(
        "--config",
        default=DEFAULT_CONFIG,
        help="the query config the corpus was harvested with; its `triage` block is the "
        "domain vocabulary. Always the full config, never the smoke one.",
    )
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument(
        "--min-strong", type=int, default=1, help="require at least this many weight-3 signals"
    )
    ap.add_argument(
        "--min-domain",
        type=int,
        default=1,
        help="require at least this many domain-vocabulary hits. The knob 01 does not "
        "need: its domain is ten subfields, this one's is all of computational science, "
        "so a single passing mention of 'simulation' is most of what a record needs to "
        "reach core scope. The smoke corpus shortlisted 42%% at 1.",
    )
    ap.add_argument("--audit-n", type=int, default=150, help="below-cut records to sample")
    ap.add_argument("--seed", type=int, default=20260911)
    ap.add_argument(
        "--force",
        action="store_true",
        help="overwrite shortlist.md and audit_sample.md even if screening.csv exists",
    )
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    out_dir = Path(args.out)
    screening_path = out_dir / "screening.csv"
    if screening_path.exists() and not args.force:
        raise SystemExit(
            f"{screening_path} exists. Re-running triage would regenerate shortlist.md and "
            "audit_sample.md underneath screening already written. Pass --force only if you "
            "will re-screen both files from scratch."
        )

    cfg_path = Path(args.config)
    vocab = load_vocabulary(load_config(cfg_path))

    src = out_dir / "screened.csv"
    if not src.exists():
        raise SystemExit(f"{src} not found - run harvest.py first")
    with src.open(newline="", encoding="utf-8") as f:
        rows: list[Row] = list(csv.DictReader(f))
    for r in rows:
        r.update(score(r, vocab))

    # Touchpoints break the tie inside a score, so the records that touch most of what
    # TANGO is reach the screener first. Membership of the shortlist is unaffected —
    # that is the AND below, and touchpoints are not part of it.
    rows.sort(
        key=lambda r: (-r["agentic_score"], -r["n_touchpoints"], -int(r.get("cited_by") or 0))
    )
    cols = list(rows[0].keys())
    with (out_dir / "triage.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    def above(r: Row) -> bool:
        return bool(
            r["agentic_score"] >= args.min_score
            and r["strong_hits"] >= args.min_strong
            and r["domain_score"] >= args.min_domain
            and r["llm_present"] == "yes"
            and r["scope_computed"] != "none"
        )

    short = [r for r in rows if above(r)]
    below = [r for r in rows if not above(r)]
    core = [r for r in short if r["scope_computed"] == "core"]
    peri = [r for r in short if r["scope_computed"] == "periphery"]

    with (out_dir / "shortlist.md").open("w", encoding="utf-8") as f:
        f.write(
            f"# Shortlist — {len(short)} of {len(rows)} harvested records\n\n"
            f"Cut: agentic_score >= {args.min_score}, strong_hits >= {args.min_strong}, "
            f"domain_score >= {args.min_domain}, LLM vocabulary present, a domain group "
            f"identified. Ranked by score, then by touchpoint count, then citations.\n"
            f"Scores, groups and touchpoints are computed by `scripts/triage_tango.py` from "
            f"title+abstract; they are a sorting aid and carry no authority. A touchpoint hit "
            f"is not evidence that the system is relevant to TANGO, and no hit is not evidence "
            f"that it is not. Screen every record below.\n\n"
        )
        for label, group in (
            ("Core (an agent that drives a simulator, solver, optimiser or scientific code)", core),
            ("Periphery (counted, not deep-read)", peri),
        ):
            f.write(f"\n## {label} — {len(group)}\n\n")
            for r in group:
                f.write(digest(r) + "\n")

    # Seeded on purpose: the audit sample has to be the same records on a re-run, or the
    # false-negative rate is measured against a sample that no longer exists.
    rng = random.Random(args.seed)  # noqa: S311 - reproducibility, not secrecy
    sample = rng.sample(below, min(args.audit_n, len(below)))
    with (out_dir / "audit_sample.md").open("w", encoding="utf-8") as f:
        f.write(
            f"# Recall audit — {len(sample)} records drawn at random from the "
            f"{len(below)} below the cut\n\n"
            "Screen these exactly as the shortlist. Any that should have been admitted is a "
            "false negative: report the rate in RUN.md and, if it exceeds 5%, diagnose which "
            "cut is binding (min-score vs min-strong vs the domain vocabulary in "
            "`reference/queries_tango.json`) before widening. This is what makes the cut a "
            "measurement rather than an assumption.\n\n"
        )
        for r in sample:
            f.write(digest(r) + "\n")

    dist = Counter(min(r["agentic_score"], 20) for r in rows)
    with (out_dir / "triage_stats.md").open("w", encoding="utf-8") as f:
        f.write(
            f"# Triage statistics\n\nHarvested: {len(rows)}  ·  Shortlisted: {len(short)} "
            f"({100 * len(short) // max(len(rows), 1)}%)  ·  Core: {len(core)}  ·  "
            f"Periphery: {len(peri)}  ·  Below cut: {len(below)}\n\n"
            f"Cut applied: min-score {args.min_score}, min-strong {args.min_strong}, "
            f"min-domain {args.min_domain}\n\n"
            f"Agentic vocabulary: imported from `scripts/triage.py` — the same definition of "
            f"'agentic' as the 01 run.\n"
            f"Domain vocabulary and touchpoints: `{cfg_path}`.\n\n"
            "## Shortlist size at other thresholds\n\n"
            "Every knob, because the cut is an AND of them and varying one hides which is\n"
            "binding. If a row is flat across `min-score`, the score is not what is cutting.\n"
            f"Both tables below hold the other two knobs at what was applied: min-domain\n"
            f"{args.min_domain} in the first, min-score {args.min_score} and min-strong\n"
            f"{args.min_strong} in the second.\n\n"
            "| min-score | strong>=0 | strong>=1 | strong>=2 |\n|---|---|---|---|\n"
        )

        def count(sc: int, st: int, dm: int) -> int:
            return sum(
                1
                for r in rows
                if r["agentic_score"] >= sc
                and r["strong_hits"] >= st
                and r["domain_score"] >= dm
                and r["llm_present"] == "yes"
                and r["scope_computed"] != "none"
            )

        for t in (1, 2, 3, 4, 6, 8, 10, 12):
            f.write(
                f"| {t} | "
                + " | ".join(str(count(t, s, args.min_domain)) for s in (0, 1, 2))
                + " |\n"
            )
        f.write(
            "\n## Shortlist size at other domain thresholds\n\n"
            "The knob the 01 run does not have. This corpus's domain is all of computational\n"
            "science, so one passing mention of `simulation` is enough to reach core scope;\n"
            "`domain_score` counts how many domain terms a record actually carries.\n\n"
            "| min-domain | shortlisted |\n|---|---|\n"
        )
        for d in (1, 2, 3, 5, 8):
            f.write(f"| {d} | {count(args.min_score, args.min_strong, d)} |\n")
        f.write("\n## Score distribution (all harvested)\n\n| score | n |\n|---|---|\n")
        for k in sorted(dist):
            f.write(f"| {k}{'+' if k == 20 else ''} | {dist[k]} |\n")
        f.write("\n## Core group counts, shortlisted\n\n| group | n |\n|---|---|\n")
        for g, n in Counter(r["group_computed"] for r in core).most_common():
            f.write(f"| {g} | {n} |\n")

        # Printed for every touchpoint in the config including the ones that matched
        # nothing: a derived count is only checkable if the reader can see what was
        # searched for. A zero here is a fact about this corpus's abstracts, not about
        # what any system can do.
        f.write(
            "\n## Touchpoint signals across the shortlist\n\n"
            "Regex over title+abstract, a sorting aid only. Every touchpoint in the config "
            "is listed, including those that matched nothing.\n\n| touchpoint | shortlisted |\n|---|---|\n"
        )
        tp_counts = Counter(t for r in short for t in r["touchpoints"].split(";") if t)
        for name in vocab.touchpoints:
            f.write(f"| {name} | {tp_counts.get(name, 0)} |\n")
        none_touched = sum(1 for r in short if not r["touchpoints"])
        f.write(
            f"\n{none_touched} of {len(short)} shortlisted records match no touchpoint at all.\n"
        )

        f.write("\n## Records with no abstract\n\n")
        na = sum(1 for r in rows if not r.get("abstract"))
        f.write(
            f"{na} of {len(rows)} ({100 * na // max(len(rows), 1)}%). These are screened on "
            "title alone and are the weakest part of the corpus; report the count in RUN.md.\n"
        )

    print(
        f"shortlist {len(short)} (core {len(core)}, periphery {len(peri)}) "
        f"of {len(rows)}; audit sample {len(sample)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
