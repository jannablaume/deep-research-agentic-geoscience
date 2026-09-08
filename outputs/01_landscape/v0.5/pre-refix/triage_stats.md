# Triage statistics

Harvested: 11177  ·  Shortlisted: 606 (5%)  ·  Core: 296  ·  Periphery: 310  ·  Below cut: 10571

Cut applied: min-score 3, min-strong 1

## Shortlist size at other thresholds

Both knobs, because the cut is an AND of the two and varying only one hides
which is binding. If a row is flat across `min-score`, the score is not what
is cutting - `min-strong` is, and lowering `--min-score` will change nothing.

| min-score | strong>=0 | strong>=1 | strong>=2 |
|---|---|---|---|
| 1 | 4455 | 606 | 179 |
| 2 | 2983 | 606 | 179 |
| 3 | 1532 | 606 | 179 |
| 4 | 896 | 546 | 179 |
| 6 | 463 | 398 | 179 |
| 8 | 271 | 265 | 159 |
| 10 | 140 | 138 | 117 |
| 12 | 92 | 92 | 90 |

## Score distribution (all harvested)

| score | n |
|---|---|
| 0 | 5471 |
| 1 | 1800 |
| 2 | 1867 |
| 3 | 858 |
| 4 | 387 |
| 5 | 189 |
| 6 | 175 |
| 7 | 94 |
| 8 | 101 |
| 9 | 65 |
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
| seismology | 91 |
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

1646 of 11177 (14%). These are screened on title alone and are the weakest part of the corpus; report the count in RUN.md.
