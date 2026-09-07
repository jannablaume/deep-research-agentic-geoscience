# Triage statistics

Harvested: 1865  ·  Shortlisted: 113 (6%)  ·  Core: 113  ·  Periphery: 0  ·  Below cut: 1752

Cut applied: min-score 3, min-strong 1

## Shortlist size at other thresholds

Both knobs, because the cut is an AND of the two and varying only one hides
which is binding. If a row is flat across `min-score`, the score is not what
is cutting - `min-strong` is, and lowering `--min-score` will change nothing.

| min-score | strong>=0 | strong>=1 | strong>=2 |
|---|---|---|---|
| 1 | 697 | 113 | 28 |
| 2 | 447 | 113 | 28 |
| 3 | 264 | 113 | 28 |
| 4 | 155 | 96 | 28 |
| 6 | 92 | 77 | 28 |
| 8 | 51 | 48 | 26 |
| 10 | 20 | 19 | 15 |
| 12 | 14 | 14 | 14 |

## Score distribution (all harvested)

| score | n |
|---|---|
| 0 | 1143 |
| 1 | 254 |
| 2 | 199 |
| 3 | 111 |
| 4 | 50 |
| 5 | 14 |
| 6 | 26 |
| 7 | 16 |
| 8 | 19 |
| 9 | 13 |
| 10 | 3 |
| 11 | 3 |
| 12 | 4 |
| 13 | 2 |
| 15 | 5 |
| 16 | 2 |
| 18 | 1 |

## Core group counts, shortlisted

| group | n |
|---|---|
| seismology | 90 |
| hydrogeology | 11 |
| reservoir_engineering | 4 |
| engineering_geology | 4 |
| geomechanics | 3 |
| geothermal | 1 |

## Records with no abstract

348 of 1865 (18%). These are screened on title alone and are the weakest part of the corpus; report the count in RUN.md.
