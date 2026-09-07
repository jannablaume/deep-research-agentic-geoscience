# Triage statistics

Harvested: 9098  ·  Shortlisted: 531 (5%)  ·  Core: 295  ·  Periphery: 236  ·  Below cut: 8567

Cut applied: min-score 3, min-strong 1

## Shortlist size at other thresholds

Both knobs, because the cut is an AND of the two and varying only one hides
which is binding. If a row is flat across `min-score`, the score is not what
is cutting - `min-strong` is, and lowering `--min-score` will change nothing.

| min-score | strong>=0 | strong>=1 | strong>=2 |
|---|---|---|---|
| 1 | 3267 | 531 | 177 |
| 2 | 2328 | 531 | 177 |
| 3 | 1282 | 531 | 177 |
| 4 | 791 | 482 | 177 |
| 6 | 434 | 371 | 177 |
| 8 | 255 | 249 | 158 |
| 10 | 140 | 138 | 117 |
| 12 | 92 | 92 | 90 |

## Score distribution (all harvested)

| score | n |
|---|---|
| 0 | 4667 |
| 1 | 1246 |
| 2 | 1410 |
| 3 | 708 |
| 4 | 320 |
| 5 | 172 |
| 6 | 165 |
| 7 | 91 |
| 8 | 89 |
| 9 | 60 |
| 10 | 32 |
| 11 | 27 |
| 12 | 31 |
| 13 | 16 |
| 14 | 15 |
| 15 | 14 |
| 16 | 10 |
| 17 | 7 |
| 18 | 6 |
| 19 | 2 |
| 20+ | 10 |

## Core group counts, shortlisted

| group | n |
|---|---|
| seismology | 90 |
| reservoir_engineering | 72 |
| ccs | 52 |
| engineering_geology | 29 |
| mining | 17 |
| geological_modelling | 15 |
| hydrogeology | 11 |
| geothermal | 4 |
| geomechanics | 3 |
| inversion | 2 |

## Records with no abstract

1419 of 9098 (15%). These are screened on title alone and are the weakest part of the corpus; report the count in RUN.md.
