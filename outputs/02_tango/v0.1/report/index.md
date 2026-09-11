# 02 — Agentic systems that drive a simulator, solver or engineering model

A descriptive scoping review. It maps what has been built, how it was evaluated, how mature it
is, and which of TANGO's surfaces each system touches. TANGO supplies the touchpoint
vocabulary and is not the subject: every claim here is about the source it cites. No sentence
in this report prescribes anything for TANGO — not what to build, adopt, prioritise or avoid.

Run log: `../RUN.md`. Grids: `../papers.csv`, `../transfer.csv`. Verbatim extracts:
`../papers.md`, `../transfer.md`. Access record: `../paywalled.md`, `../unreachable.md`.

## Contents

| Section | What it covers |
|---|---|
| [00 Executive summary](00_executive_summary.md) | What exists, at what maturity, against which touchpoints, on what evidence |
| [01 Control patterns](01_control_patterns.md) | What the agent emits, what it reads back, what closes the loop, and where the loop is not closed |
| [02 Architectures](02_architectures.md) | Recurring designs and what each is chosen for |
| [03 Touchpoints](03_touchpoints.md) | One subsection per touchpoint, including those nothing matched |
| [04 Evaluation](04_evaluation.md) | Baselines, held-out data, shared benchmarks, what gets measured |
| [05 Maturity](05_maturity.md) | Demonstrated maturity, and how often the claim outruns it |
| [06 Failure and limits](06_failure_and_limits.md) | What authors report their systems could not do, quoted |
| [07 Periphery](07_periphery.md) | Size and character of the excluded neighbouring agent literatures |
| [08 Papers](08_papers.md) | Annotated list of all 183 admitted sources, by subfield then tier |

## Headline numbers

**Corpus.** 35,046 records harvested from OpenAlex and arXiv across 22 query cells. Shortlist
773 at thresholds `--min-score 3 --min-strong 1 --min-domain 4`. 939 screening decisions.
**183 admitted: 98 core, 85 context**, covering 177 distinct systems.

**Recall.** A random 150-record sample of the below-cut population was screened; 3 were false
negatives, a rate of **2%**. All three were bound by the domain knob rather than the agentic
one. A separate targeted probe found six further below-cut in-scope systems of the same shape;
`RUN.md` records why that is a finding about shape and not a revision of the rate.

**Years.** 2026 — 126, 2025 — 51, 2024 — 6.

**Source types.** Preprint 98, peer-reviewed 71, repository 11, industry 3.

**Interfaces (core rows).** code-execution 29, file-io 26, api 19, mcp 18, cli 5, not stated 1.

**Autonomy (core rows).** executes-and-iterates 74, executes-with-approval 18, suggests 2, not
stated 4.

**Architectures (core rows).** multi-agent-hierarchical 38, multi-agent-flat 17,
agent-plus-simulator 14, pipeline-with-agent 12, single-agent 9, agent-plus-solver 6,
agent-plus-database 1, not stated 1.

**Demonstrated maturity (core rows).** M0 3, M1 37, M2 47, M3 11, M4 0, M5 0. All 85 context
rows: not stated (abstract only).

**Touchpoints (all rows / core rows).** config-generation 96/72 · solver-control 76/65 ·
results-interpretation 57/52 · verification-regression 45/33 · optimisation-loop 42/27 ·
hpc-scale-out 33/18 · tool-exposure 32/23 · provenance-reproducibility 24/15 ·
topology-construction 23/18 · surrogate-modelling 17/11 · uncertainty-quantification 10/3 ·
techno-economic 6/5 · none 27/3.

**Evidence gaps that were searched for.** No source above M3. No cross-domain benchmark. No
source driving a life-cycle cost model as its controlled artefact. No source reporting an
agent output that was acted on and later found wrong. 26 of 98 core sources report no
baseline; 52 do not state whether data was held out; 21 state nothing about what happens when
the driven code fails.

**Access.** 15 records screened as core could not be read in full and were demoted to context
— 13% of the intended deep-read. Two admitted sources could not be read at all. One blocked
source was recovered from the local PDF store rather than lost. Eight core records were read
from an author preprint whose identity was inferred rather than verified against the version of
record.

**Periphery.** 12,189 harvested records were classified periphery and not read: literature and
writing agents 6,093, software engineering 4,488, interface agents 1,196, laboratory automation
412. Two periphery groups were left truncated at the paging cap on purpose; `n_available` in
section 07 is the number to read.
