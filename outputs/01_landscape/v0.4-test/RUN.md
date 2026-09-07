outputs/01_landscape/v0.4-test

## Run log

- date: 2026-09-07
- prompt: prompts/01_landscape_neutral.md v0.4 (patched during this smoke test)
- purpose: mechanics test of the prompt (not a landscape). First harvest used `--limit-queries 6` (geomechanics, seismology, hydrogeology × A/B). That was itself a finding: `--limit-queries` skips periphery. `--smoke` was added afterward and is what a future mechanics test should use.
- model: Cursor Grok 4.6

## Step 1 — Harvest

- Command: `python3 scripts/harvest.py --out outputs/01_landscape/v0.4-test --no-s2 --limit-queries 6`
- Result: 1865 unique API records, 1517 with abstract (81%), 12 API calls, all `status: ok`, none `zero`. Later +2 grey rows → 1867 in `screened.csv`.
- Note: `openalex_max_pages: 5` (1000 records/query). No truncation on this slice.
- Shortlist band 150–800: not applied (partial harvest). `--min-score 3 --min-strong 1` kept.

## Step 2 — Screening

- Screened all 113 `shortlist.md` records into `screening.csv`.
- Screened 40 of 150 `audit_sample.md` records (`from_audit_sample: yes`) so `audit.py`'s ≥40 recall check would run. A full run still screens all 150.
- False negatives in the 40: **0 / 40 (0%)**.
- Admitted from shortlist: 32 (3 core, 29 context). Cut-reason mix dominated by `not-a-source` (Zenodo podcasts) and `not-geoscience` (“seismic shift” metaphor; Seismic sales platform).

## Step 3 — Grey literature (2 of 40)

- `w001`: SPE/geothermal agentic AI → GAIA `arxiv:2511.03852` (not in the 6-query harvest).
- `w002`: GitHub seismology MCP → `title:seismomcp`.
- Both appended to `screened.csv` then `screening.csv` (`found_via` in note / papers.csv). This is the join the schema now documents.

## Step 4 — Deep-read

- Full text: `arxiv:2601.18381` (Devito agent), `doi:10.48550/arxiv.2609.01777` (TREMORS), `doi:10.48550/arxiv.2603.21152` (TRACE). All via `arxiv.org/html/`.
- Other admits left `tier: context` / abstract-only by smoke-test design, not paywall.

## Step 5–6 — Report and audit

- Nine report files written. Thin on purpose.
- First `audit.py` run: 24/26. Failures were (1) triage 1865 vs screened 1867 after grey append, (2) untagged 4–6 line annotations in `08_papers.md`. Both are now script fixes, not number-edits.

## Closing numbers (this slice)

- harvested (API) / shortlisted / screened / core / context: 1865 / 113 / 155 decisions / 3 core / 31 context
- false-negative rate: 0% on n=40 (full run uses n=150)
- records with no abstract: 348 of 1865 (18%) at harvest; grey rows have abstracts
- snowballing: not done (smoke)
- periphery harvested: 0 (`--limit-queries 6`)

## What to change — done in this session, for the full run

- Use `$OUT`; never overwrite a directory that has `screening.csv`.
- Full harvest: `python3 scripts/harvest.py --out "$OUT" --no-s2` (all 30 groups). Do not use `--limit-queries`.
- `triage.py` refuses if `screening.csv` exists (`--force` only if re-screening from scratch).
- Grey/snowball: append `screened.csv` first.
- `audit.py` skips evidence tags on `08_papers.md` / `index.md`; allows web extras in `screened.csv`.
