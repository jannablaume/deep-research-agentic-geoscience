# Decision Log

Newest first. One entry per decision: what, why, what it rules out.

## 2026-09-02 — v0.2: hard web-call cap, test run becomes a coverage probe

Every run mode gets a hard cap on network calls (`test` 20, `full` 250) instead of only
pass-count budgets, which were unbounded on the search side. `test` is redefined from a
mechanics check to a coverage probe: 15 calls sampling all 10 subfields × 2 lineages into
`coverage.md` (yield table, projection, go/no-go verdict), 5 calls taking 3-4 sources
through the whole artifact chain including PDF download. Snowballing and the Chinese track
are `full`-only — both cost more than the whole `test` budget.

Runs now retain `queries.csv`, `screened.csv` and `abstracts/`, so scope or taxonomy can
change without re-searching. Rules out: `test` producing any landscape synthesis, and any
absence claim from a `test` run.

Two follow-on corrections in the same version. Storing abstracts must never cost a web call
— screening rides on the search results, so `abstract_stored` becomes
`full / snippet-only / no` rather than requiring a fetch that would blow the cap. And
compliance with a 700-line prompt is now verified rather than assumed: a section-by-section
re-read schedule, plus a Self-audit table closing `RUN.md` in which every invariant is
checked against the output files (row-count parity between `screened.csv`, `papers.csv` and
`papers.md`, CSV parses, every admit traceable to a `query_id`).

## 2026-08-31 — Host on ETHZ GitLab

Repo lives at `gitlab.ethz.ch:jblaume/deep-research-agentic-geoscience`, private, Daniel as
Maintainer.
Research direction is unpublished and TANGO-adjacent, so it stays on institutional infra
next to Confluence and GCS. Cost: no `gh`/agent PR tooling.

## 2026-09-01 — Run Test Run first and evaluate prompt

The 01_landscape_neutral.md prompt is run first with max 20 web sources to check its result. 
No pdfs are stored in GCP. 
