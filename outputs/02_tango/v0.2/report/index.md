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
**183 admitted: 101 core, 82 context**, covering 177 distinct systems.

**Recall.** A random 150-record sample of the below-cut population was screened; 3 were false
negatives, a rate of **2%**. All three were bound by the domain knob rather than the agentic
one. A separate targeted probe found six further below-cut in-scope systems of the same shape;
`RUN.md` records why that is a finding about shape and not a revision of the rate.

**Years.** 2026 — 127, 2025 — 50, 2024 — 6.

**Source types.** Preprint 98, peer-reviewed 71, repository 11, industry 3.

**Interfaces (core rows).** code-execution 29, file-io 28, api 19, mcp 19, cli 5, not stated 1.

**Autonomy (core rows).** executes-and-iterates 77, executes-with-approval 18, suggests 2, not
stated 4.

**Architectures (core rows).** multi-agent-hierarchical 40, multi-agent-flat 17,
agent-plus-simulator 15, pipeline-with-agent 12, single-agent 9, agent-plus-solver 6,
agent-plus-database 1, not stated 1.

**Demonstrated maturity (core rows).** M0 3, M1 38, M2 48, M3 12, M4 0, M5 0. All 82 context
rows: not stated (abstract only).

**Touchpoints (all rows / core rows).** config-generation 98/75 · solver-control 77/67 ·
results-interpretation 60/55 · verification-regression 48/36 · optimisation-loop 44/29 ·
hpc-scale-out 34/19 · tool-exposure 32/24 · topology-construction 25/21 ·
provenance-reproducibility 24/15 · surrogate-modelling 17/11 · uncertainty-quantification 11/4 ·
techno-economic 7/6 · none 25/3.

**Evidence gaps that were searched for.** No source above M3. No cross-domain benchmark. No
source driving a life-cycle cost model as its controlled artefact. No source reporting an
agent output that was acted on outside its own experiment and later found wrong. 26 of 101
core sources report no baseline; 53 do not state whether data was held out; 21 state nothing
about what happens when the driven code fails.

**Access.** v0.1 demoted 15 records screened as core that it could not read in full — 13% of
the intended deep-read. In v0.2, 14 sources were retrieved by hand from the local PDF store:
three of the demoted fifteen, all promoted back to core, leaving **12 demotions and 11% of the
intended deep-read still lost**; and eleven already-core records that v0.1 had read from a
substitute. Of those eleven, 8 were verified unchanged against the version of record and 3 were
corrected. The two records that had no retrievable narrative text at all are now read in full.
Two core records remain read from a substitute whose identity is inferred rather than verified:
an ETH institutional record read from its arXiv version, and a repository record whose
accompanying preprint is on a blocked host.

**Periphery.** 12,189 harvested records were classified periphery and not read: literature and
writing agents 6,093, software engineering 4,488, interface agents 1,196, laboratory automation
412. Two periphery groups were left truncated at the paging cap on purpose; `n_available` in
section 07 is the number to read.
