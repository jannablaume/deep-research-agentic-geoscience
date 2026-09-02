<!-- This is a coverage probe (test mode), not a landscape map of agentic AI in solid-earth and
subsurface geoscience. It answers one question — would a full run cover the landscape and
produce usable artifacts? — and nothing else. It does not describe the state of the field. -->

**This is a coverage probe, not a landscape map.** It reports the yield of 15 exploratory
search calls plus a 5-call mechanics check, not a synthesis of the literature. Report sections
2-4 and 7-8 (agentic techniques, architectures, applications by subfield, disagreements,
stakeholder views) are intentionally not written here: three or four admitted sources cannot
support a synthesis, and writing one would disguise a probe as a finished review. See
`coverage.md` for the full yield table and verdict.

## 1. What this probe touched

Three sources were carried to a full extraction this run, spanning three subfields and both
lineages: `AQUAH` (hydrogeology, LLM-based agent for end-to-end hydrologic modeling, arXiv
2508.02936), `GeoMind` (subsurface characterisation/geophysical inversion, LLM-based agentic
workflow for lithology classification benchmarked against non-agentic baselines, arXiv
2604.21501), and a Constrained-Markov-Game/safe-multi-agent-RL framework for multi-site CO2
storage management (CCS, pre-LLM lineage, arXiv 2508.11618, extraction incomplete — see
`papers.md`). `[Certain]` Both AQUAH and GeoMind report evaluation against real or benchmark
data with author-stated results and limitations, extracted verbatim in `papers.md`; the CO2
storage paper's evaluation section could not be read this run due to a fetch-tool limitation,
not an access restriction, and no claim is made about it beyond its title, authors, and
architecture framing. `[Absent-searched]` No absence claim is made anywhere in this run:
`test` mode's single-query-per-cell probe cannot distinguish an empty subfield from a
badly-phrased query (see `coverage.md`), and the prompt explicitly forbids absence claims in
this mode.

Beyond these three, the 15 coverage-probe queries screened 92 unique titles across all 20
subfield x lineage cells (13 probed directly, 7 unprobed with incidental spillover noted where
it occurred); the full yield table, per-cell projections, and the go/no-go verdict on the
`full` run are in `coverage.md`, which is this run's primary deliverable.

## Coverage verdict (from `coverage.md`)

**Overall: GO**, conditional on three seed-vocabulary fixes (subsurface characterisation x
pre-LLM, engineering geology x pre-LLM, mining x LLM-based — each returned zero or
near-zero on-topic hits under the phrasing tried here) and a fetch-budget adjustment for
full-text PDF reading, where this run found `WebFetch` unreliable on raw arXiv PDF URLs
(one outright failure exceeding a content-length limit, one partial extraction) with an
HTML-rendering fallback (`arxiv.org/html/<id>`) that worked cleanly where tried. Full detail,
including the per-cell yield table and arithmetic on the 250-call `full`-mode budget, is in
`coverage.md`.
