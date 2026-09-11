# Triage statistics

Harvested: 1325  ·  Shortlisted: 557 (42%)  ·  Core: 296  ·  Periphery: 261  ·  Below cut: 768

Cut applied: min-score 3, min-strong 1, min-domain 1

Agentic vocabulary: imported from `scripts/triage.py` — the same definition of 'agentic' as the 01 run.
Domain vocabulary and touchpoints: `reference/queries_tango.json`.

## Shortlist size at other thresholds

Every knob, because the cut is an AND of them and varying one hides which is
binding. If a row is flat across `min-score`, the score is not what is cutting.
Both tables below hold the other two knobs at what was applied: min-domain
1 in the first, min-score 3 and min-strong
1 in the second.

| min-score | strong>=0 | strong>=1 | strong>=2 |
|---|---|---|---|
| 1 | 716 | 557 | 265 |
| 2 | 704 | 557 | 265 |
| 3 | 674 | 557 | 265 |
| 4 | 607 | 523 | 265 |
| 6 | 501 | 473 | 265 |
| 8 | 356 | 353 | 250 |
| 10 | 233 | 232 | 212 |
| 12 | 164 | 164 | 158 |

## Shortlist size at other domain thresholds

The knob the 01 run does not have. This corpus's domain is all of computational
science, so one passing mention of `simulation` is enough to reach core scope;
`domain_score` counts how many domain terms a record actually carries.

| min-domain | shortlisted |
|---|---|
| 1 | 557 |
| 2 | 301 |
| 3 | 169 |
| 5 | 62 |
| 8 | 10 |

## Score distribution (all harvested)

| score | n |
|---|---|
| 0 | 569 |
| 1 | 13 |
| 2 | 34 |
| 3 | 69 |
| 4 | 55 |
| 5 | 58 |
| 6 | 110 |
| 7 | 48 |
| 8 | 62 |
| 9 | 68 |
| 10 | 38 |
| 11 | 33 |
| 12 | 50 |
| 13 | 24 |
| 14 | 19 |
| 15 | 26 |
| 16 | 7 |
| 17 | 10 |
| 18 | 13 |
| 19 | 2 |
| 20+ | 17 |

## Core group counts, shortlisted

| group | n |
|---|---|
| simulation_orchestration | 150 |
| optimisation_uq | 103 |
| scientific_computing | 21 |
| simulation_general | 11 |
| solver_control | 7 |
| computational_discovery | 2 |
| geoenergy_subsurface | 1 |
| energy_systems | 1 |

## Touchpoint signals across the shortlist

Regex over title+abstract, a sorting aid only. Every touchpoint in the config is listed, including those that matched nothing.

| touchpoint | shortlisted |
|---|---|
| config_generation | 8 |
| topology_construction | 3 |
| solver_control | 3 |
| optimisation_loop | 46 |
| surrogate_modelling | 30 |
| uncertainty_quantification | 55 |
| hpc_scale_out | 13 |
| tool_exposure | 29 |
| results_interpretation | 4 |
| techno_economic | 3 |
| verification_regression | 9 |
| provenance_reproducibility | 36 |

367 of 557 shortlisted records match no touchpoint at all.

## Records with no abstract

178 of 1325 (13%). These are screened on title alone and are the weakest part of the corpus; report the count in RUN.md.
