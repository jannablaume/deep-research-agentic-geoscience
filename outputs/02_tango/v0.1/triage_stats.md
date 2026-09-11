# Triage statistics

Harvested: 35046  ·  Shortlisted: 773 (2%)  ·  Core: 352  ·  Periphery: 421  ·  Below cut: 34273

Cut applied: min-score 3, min-strong 1, min-domain 4

Agentic vocabulary: imported from `scripts/triage.py` — the same definition of 'agentic' as the 01 run.
Domain vocabulary and touchpoints: `reference/queries_tango.json`.

## Shortlist size at other thresholds

Every knob, because the cut is an AND of them and varying one hides which is
binding. If a row is flat across `min-score`, the score is not what is cutting.
Both tables below hold the other two knobs at what was applied: min-domain
4 in the first, min-score 3 and min-strong
1 in the second.

| min-score | strong>=0 | strong>=1 | strong>=2 |
|---|---|---|---|
| 1 | 2425 | 773 | 294 |
| 2 | 1958 | 773 | 294 |
| 3 | 1487 | 773 | 294 |
| 4 | 1067 | 725 | 294 |
| 6 | 615 | 545 | 294 |
| 8 | 369 | 364 | 256 |
| 10 | 224 | 224 | 202 |
| 12 | 146 | 146 | 141 |

## Shortlist size at other domain thresholds

The knob the 01 run does not have. This corpus's domain is all of computational
science, so one passing mention of `simulation` is enough to reach core scope;
`domain_score` counts how many domain terms a record actually carries.

| min-domain | shortlisted |
|---|---|
| 1 | 5692 |
| 2 | 2553 |
| 3 | 1327 |
| 5 | 454 |
| 8 | 105 |

## Score distribution (all harvested)

| score | n |
|---|---|
| 0 | 13398 |
| 1 | 3481 |
| 2 | 5394 |
| 3 | 4003 |
| 4 | 2239 |
| 5 | 1284 |
| 6 | 1469 |
| 7 | 638 |
| 8 | 698 |
| 9 | 651 |
| 10 | 327 |
| 11 | 288 |
| 12 | 329 |
| 13 | 146 |
| 14 | 155 |
| 15 | 172 |
| 16 | 60 |
| 17 | 84 |
| 18 | 73 |
| 19 | 36 |
| 20+ | 121 |

## Core group counts, shortlisted

| group | n |
|---|---|
| simulation_orchestration | 137 |
| scientific_computing | 81 |
| computational_discovery | 43 |
| solver_control | 40 |
| optimisation_uq | 18 |
| simulation_general | 18 |
| geoenergy_subsurface | 14 |
| energy_systems | 1 |

## Touchpoint signals across the shortlist

Regex over title+abstract, a sorting aid only. Every touchpoint in the config is listed, including those that matched nothing.

| touchpoint | shortlisted |
|---|---|
| config_generation | 16 |
| topology_construction | 9 |
| solver_control | 15 |
| optimisation_loop | 29 |
| surrogate_modelling | 22 |
| uncertainty_quantification | 27 |
| hpc_scale_out | 65 |
| tool_exposure | 45 |
| results_interpretation | 9 |
| techno_economic | 3 |
| verification_regression | 21 |
| provenance_reproducibility | 99 |

530 of 773 shortlisted records match no touchpoint at all.

## Records with no abstract

5236 of 35046 (14%). These are screened on title alone and are the weakest part of the corpus; report the count in RUN.md.
