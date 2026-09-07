outputs/01_landscape/v0.4-test

## Run log

- date: 2026-09-07
- prompt: prompts/01_landscape_neutral.md v0.4
- purpose: mechanics test of the prompt (not a full landscape). Harvest limited to 6 of 30 query groups (`--limit-queries 6 --no-s2`) covering geomechanics, seismology, hydrogeology × bands A and B. Goal: walk steps 1–6, find where the prompt or scripts stall, fix them, leave the prompt runnable for a full harvest.
- model: Cursor Grok 4.6

## Step 1 — Harvest

- Command: `python3 scripts/harvest.py --out outputs/01_landscape/v0.4-test --no-s2 --limit-queries 6`
- Result: 1865 unique records, 1517 with abstract (81%), 12 API calls, all `status: ok`, none `zero`.
- Note: `openalex_max_pages: 5` (1000 records/query). q003 seismology A_agentic returned 693 of 693; q004 seismology B_llm 812 of 812; no truncation in this slice.
