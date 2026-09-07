#!/usr/bin/env python3
"""Rank the harvested corpus so the model reads a bounded, ordered shortlist.

The APIs return high recall and low precision: a full harvest is ~15-25k records, of
which a few hundred are agentic systems. Nothing about that ranking needs judgment, so
none of it is done by the model. This script scores every record from its title and
abstract, writes a ranked shortlist the model actually reads, and writes an audit
sample drawn from *below* the cut so the cut's cost is measured rather than assumed.

    python3 scripts/triage.py --out outputs/01_landscape/v0.4 [--min-score 3]

Writes, in --out:
    triage.csv     every harvested row + agentic_score, domain_score, band_flags, tier_suggest
    shortlist.md   the above-cut records as a compact digest, ranked, for the model to screen
    audit_sample.md  150 randomly drawn below-cut records, for the recall check
    triage_stats.md  score distribution and cut cost

Tune --min-score / --min-strong from triage_stats.md, then re-run. No network calls.
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import re
import sys
from collections import Counter

csv.field_size_limit(10_000_000)

# Weight 3, and self-sufficient: vocabulary that only appears in LLM-agent work. A hit
# here is on its own evidence that the record is LLM-era.
AGENT_LLM = [
    r"agentic", r"\bLLM[- ]?agents?\b", r"\bAI agents?\b", r"language model agents?",
    r"agent[- ]based (?:LLM|large language)", r"tool[- ]calling", r"function[- ]calling",
    r"\bLangChain\b", r"\bAutoGen\b", r"\bLangGraph\b", r"\bCrewAI\b", r"\bAutoGPT\b",
    r"AI scientist", r"agent(?:ic)? workflows?",
]
# Weight 3, but only when LLM vocabulary is independently present. These terms all have
# a large pre-LLM or unrelated literature: "multi-agent system" is 40 years old,
# "copilot" is an aircraft, and "tool use" is primatology.
AGENT_GENERIC = [
    r"multi[- ]?agent (?:system|framework|architecture|collaborat|approach)",
    r"autonomous agents?", r"\btool[- ]use\b", r"\btool[- ]using\b",
    r"agent orchestration", r"orchestrat\w+ agents?", r"self[- ]driving lab",
    r"autonomous experimentation", r"\bcopilots?\b", r"planning agents?",
]
# Case-SENSITIVE. "ReAct" is a prompting pattern; "react" is what chemicals do. Matched
# case-insensitively this single pattern produced 377 false positives in a 1795-record
# test corpus - more than every other signal combined.
AGENT_CASED = [r"\bReAct\b", r"\bMRKL\b", r"\bToT\b"]
# Weight 3, LLM-corroborated like AGENT_GENERIC. Systems that plan, automate or construct
# something with an LLM but never use the word "agent". Every false negative in the v0.4
# run's 60-record audit sample was this shape - "LLM-Powered Data Automation for 3D
# Geological Model Updating", "LLM-assisted workflow for geological unit harmonization" -
# and none could be recovered by lowering --min-score, because they scored on medium
# signals alone with strong_hits at 0. Adding them costs ~15% more shortlist.
AGENT_COMPOUND = [
    r"(?:LLM|large language model|GPT|foundation model|language model)[-\s]"
    r"(?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}"
    r"(?:workflow|pipeline|automation|framework|system|assistant)",
    r"knowledge[-\s]based\s+(?:Q&A|question[-\s]answering)",
    r"\bQ&A system\b|question[-\s]answering system",
    r"knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?",
    r"automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b",
]
# Weight 1: LLM-era vocabulary. Necessary but far from sufficient.
MEDIUM = [
    r"large language models?", r"\bLLMs?\b", r"\bGPT-?[345]\b", r"\bChatGPT\b",
    r"foundation models?", r"retrieval[- ]augmented", r"\bRAG\b", r"chain[- ]of[- ]thought",
    r"prompt engineering", r"in[- ]context learning", r"vision[- ]language model",
    r"\bClaude\b", r"\bLlama\b", r"\bGemini\b", r"generative AI", r"transformer",
]
# The 'agent' that is not an agent. Without these, chemistry and medicine flood the top.
NEGATIVE = [
    r"(?:chemical|contrast|reducing|oxidizing|chelating|foaming|antimicrobial|"
    r"therapeutic|blowing|curing|wetting|surface[- ]active|weathering|infectious)\s+agents?",
    r"agents?\s+of\s+(?:erosion|weathering|change)",
]
# Pre-LLM agent work: out of scope after v0.4, but flagged rather than silently dropped
# so the exclusion stays visible and reversible.
PRE_LLM = [r"agent[- ]based model", r"\bABM\b", r"blackboard architecture",
           r"expert system", r"reinforcement learning", r"swarm intelligence"]

DOMAIN = {
    "geomechanics": r"rock mechanic|geomechanic|rock mass|fault slip|hydraulic fractur|in[- ]situ stress",
    "seismology": r"seismolog|seismic|earthquake|microseism|phase pick|ground motion|aftershock",
    "hydrogeology": r"hydrogeolog|groundwater|aquifer|vadose|contaminant transport",
    "reservoir_engineering": r"reservoir (?:engineering|simulation|management)|well log|petroleum engineer|drilling|history match|production optimi",
    "geothermal": r"geothermal|enhanced geothermal|heat flow",
    "ccs": r"carbon capture|CO2 storage|carbon sequestrat|geological storage|\bCCS\b|\bCCUS\b",
    "mining": r"mineral explorat|mine planning|ore body|orebody|grade control|prospectivity|mining engineer",
    "engineering_geology": r"engineering geolog|slope stability|tunnel|landslide|geotechnic|site characteri",
    "inversion": r"geophysical inversion|full[- ]waveform inversion|seismic interpretation|resistivity tomograph|subsurface imaging|well logging",
    "geological_modelling": r"geological model|geologic model|geological map|stratigraph|basin model|geoscience knowledge graph",
}
PERIPHERY = {
    "earth_observation": r"remote sensing|satellite imag|earth observation|land cover|\bSAR\b",
    "climate_atmosphere": r"climate model|weather forecast|atmospheric|climate simulation|meteorolog",
    "ocean": r"oceanograph|ocean model|marine science",
    "planetary": r"planetary geolog|lunar surface|martian",
}

_C = re.IGNORECASE


def compile_all(pats): return [re.compile(p, _C) for p in pats]


AL_R, AG_R, AX_R, MEDIUM_R, NEG_R, PRE_R = map(
    compile_all, (AGENT_LLM, AGENT_GENERIC, AGENT_COMPOUND, MEDIUM, NEGATIVE, PRE_LLM))
AC_R = [re.compile(p) for p in AGENT_CASED]  # case-sensitive by design
DOMAIN_R = {k: re.compile(v, _C) for k, v in DOMAIN.items()}
PERIPH_R = {k: re.compile(v, _C) for k, v in PERIPHERY.items()}


def score(row: dict) -> dict:
    title, abst = row.get("title", ""), row.get("abstract", "")
    text = f"{title} . {abst}"
    neg_spans = [m.span() for r in NEG_R for m in r.finditer(text)]

    def hits(regexes):
        found = set()
        for r in regexes:
            for m in r.finditer(text):
                if any(s <= m.start() < e for s, e in neg_spans):
                    continue
                found.add(r.pattern)
                # A signal in the title is what the paper is about, not a passing mention.
                if m.start() < len(title):
                    found.add(r.pattern + "#title")
        return found

    al_hits, m_hits = hits(AL_R), hits(MEDIUM_R)
    # LLM-era vocabulary must be established independently of the generic agent terms,
    # otherwise "multi-agent system" alone promotes 1990s work into an LLM shortlist.
    llm_present = bool(al_hits or m_hits)
    ag_hits = (hits(AG_R) | hits(AC_R) | hits(AX_R)) if llm_present else set()
    s_hits = al_hits | ag_hits
    agentic = 3 * len(s_hits) + len(m_hits)
    dom = {k: len(r.findall(text)) for k, r in DOMAIN_R.items() if r.search(text)}
    per = {k: len(r.findall(text)) for k, r in PERIPH_R.items() if r.search(text)}

    if dom:
        group = max(dom, key=dom.get)
        scope = "core"
    elif per:
        group = max(per, key=per.get)
        scope = "periphery"
    else:
        group, scope = "", "none"

    return {
        "agentic_score": agentic,
        "strong_hits": len([h for h in s_hits if not h.endswith("#title")]),
        "domain_score": sum(dom.values()) or sum(per.values()),
        "scope_computed": scope,
        "group_computed": group,
        "llm_present": "yes" if llm_present else "no",
        "pre_llm_flag": "yes" if any(r.search(text) for r in PRE_R) else "no",
        "signals": ";".join(sorted(h.replace("#title", "*") for h in s_hits))[:300],
    }


def digest(r: dict, words: int = 55) -> str:
    a = " ".join((r.get("abstract") or "").split()[:words])
    ident = r.get("doi") and f"doi:{r['doi']}" or r.get("arxiv_id") and f"arXiv:{r['arxiv_id']}" or r.get("url", "")
    return (f"### {r['identity_key']}\n"
            f"**{r.get('title', '')}** ({r.get('year', '')}) — {r.get('venue', '') or 'n/a'} · "
            f"cites {r.get('cited_by', '') or '0'} · score {r['agentic_score']} "
            f"(strong {r['strong_hits']}) · {r['scope_computed']}/{r['group_computed']} · {ident}\n"
            f"signals: {r['signals'] or 'none'}\n"
            f"{a}{'…' if a else '(no abstract)'}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument("--min-strong", type=int, default=1,
                    help="require at least this many weight-3 signals")
    ap.add_argument("--audit-n", type=int, default=150,
                    help="below-cut records to sample. 60 was too few in v0.4: "
                         "4 false negatives gave 6.7%% with a confidence interval "
                         "wide enough to straddle the 5%% action threshold")
    ap.add_argument("--seed", type=int, default=20260903)
    args = ap.parse_args()

    src = os.path.join(args.out, "screened.csv")
    if not os.path.exists(src):
        raise SystemExit(f"{src} not found - run harvest.py first")
    rows = list(csv.DictReader(open(src, newline="", encoding="utf-8")))
    for r in rows:
        r.update(score(r))

    rows.sort(key=lambda r: (-r["agentic_score"], -int(r.get("cited_by") or 0)))
    cols = list(rows[0].keys())
    with open(os.path.join(args.out, "triage.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    def above(r):
        return (r["agentic_score"] >= args.min_score
                and r["strong_hits"] >= args.min_strong
                and r["llm_present"] == "yes"
                and r["scope_computed"] != "none")

    short = [r for r in rows if above(r)]
    below = [r for r in rows if not above(r)]
    core = [r for r in short if r["scope_computed"] == "core"]
    peri = [r for r in short if r["scope_computed"] == "periphery"]

    with open(os.path.join(args.out, "shortlist.md"), "w", encoding="utf-8") as f:
        f.write(f"# Shortlist — {len(short)} of {len(rows)} harvested records\n\n"
                f"Cut: agentic_score >= {args.min_score}, strong_hits >= {args.min_strong}, "
                f"LLM vocabulary present, a domain group identified. Ranked by score then citations.\n"
                f"Scores and groups are computed by `scripts/triage.py` from title+abstract; "
                f"they are a sorting aid and carry no authority. Screen every record below.\n\n")
        for label, group in (("Core (solid-earth / subsurface)", core),
                             ("Periphery (counted, not deep-read)", peri)):
            f.write(f"\n## {label} — {len(group)}\n\n")
            for r in group:
                f.write(digest(r) + "\n")

    rng = random.Random(args.seed)
    sample = rng.sample(below, min(args.audit_n, len(below)))
    with open(os.path.join(args.out, "audit_sample.md"), "w", encoding="utf-8") as f:
        f.write(f"# Recall audit — {len(sample)} records drawn at random from the "
                f"{len(below)} below the cut\n\n"
                "Screen these exactly as the shortlist. Any that should have been admitted is a "
                "false negative: report the rate in RUN.md and, if it exceeds 5%, lower "
                "--min-score and re-run triage. This is what makes the cut a measurement "
                "rather than an assumption.\n\n")
        for r in sample:
            f.write(digest(r) + "\n")

    dist = Counter(min(r["agentic_score"], 20) for r in rows)
    with open(os.path.join(args.out, "triage_stats.md"), "w", encoding="utf-8") as f:
        f.write(f"# Triage statistics\n\nHarvested: {len(rows)}  ·  Shortlisted: {len(short)} "
                f"({100 * len(short) // max(len(rows), 1)}%)  ·  Core: {len(core)}  ·  "
                f"Periphery: {len(peri)}  ·  Below cut: {len(below)}\n\n"
                f"Cut applied: min-score {args.min_score}, min-strong {args.min_strong}\n\n"
                "## Shortlist size at other thresholds\n\n"
                "Both knobs, because the cut is an AND of the two and varying only one hides\n"
                "which is binding. If a row is flat across `min-score`, the score is not what\n"
                "is cutting - `min-strong` is, and lowering `--min-score` will change nothing.\n\n"
                "| min-score | strong>=0 | strong>=1 | strong>=2 |\n|---|---|---|---|\n")

        def count(sc, st):
            return sum(1 for r in rows if r["agentic_score"] >= sc and r["strong_hits"] >= st
                       and r["llm_present"] == "yes" and r["scope_computed"] != "none")

        for t in (1, 2, 3, 4, 6, 8, 10, 12):
            f.write(f"| {t} | " + " | ".join(str(count(t, s)) for s in (0, 1, 2)) + " |\n")
        f.write("\n## Score distribution (all harvested)\n\n| score | n |\n|---|---|\n")
        for k in sorted(dist):
            f.write(f"| {k}{'+' if k == 20 else ''} | {dist[k]} |\n")
        f.write("\n## Core group counts, shortlisted\n\n| group | n |\n|---|---|\n")
        for g, n in Counter(r["group_computed"] for r in core).most_common():
            f.write(f"| {g} | {n} |\n")
        f.write("\n## Records with no abstract\n\n")
        na = sum(1 for r in rows if not r.get("abstract"))
        f.write(f"{na} of {len(rows)} ({100 * na // max(len(rows), 1)}%). These are screened on "
                "title alone and are the weakest part of the corpus; report the count in RUN.md.\n")

    print(f"shortlist {len(short)} (core {len(core)}, periphery {len(peri)}) "
          f"of {len(rows)}; audit sample {len(sample)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
