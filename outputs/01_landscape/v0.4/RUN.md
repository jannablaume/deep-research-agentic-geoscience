outputs/01_landscape/v0.4

## Run log

- 2026-09-07: Resumed an in-progress v0.4 run. `harvest.py --out outputs/01_landscape/v0.4 --no-s2`
  and `triage.py --out outputs/01_landscape/v0.4 --min-score 3` had already produced
  `screened.csv`, `triage.csv`, `triage_stats.md`, `shortlist.md`, `audit_sample.md`,
  `queries.csv` before this session started (no `RUN.md` had been written, so screening
  had not begun). Verified before continuing:
  - Harvested 9098 unique records — below the ~15-25k expected in the skill instructions.
    Not re-harvested: all 60 logged queries in `queries.csv` report `status: ok` (none
    `zero`), so the shortfall is not a malformed/silently-empty query; it reflects the
    query set in `reference/queries.json` and the `--no-s2` flag (Semantic Scholar
    excluded). Recorded here rather than silently accepted.
  - Shortlist: 458 of 9098 (5%), within the 150-800 band the instructions call
    acceptable, so the `--min-score 3` threshold from the prior session was kept as-is.
  - Records with no abstract: 1419 of 9098 (15%), screened on title alone.
  - Core-group shortlist counts (from `triage_stats.md`): seismology 77, reservoir_engineering 66,
    ccs 44, engineering_geology 27, mining 10, hydrogeology 9, geological_modelling 8,
    geothermal 4, inversion 2, geomechanics 1.
- Screening, grey-literature search, deep-read and report-writing proceed from this point
  forward in this session.
