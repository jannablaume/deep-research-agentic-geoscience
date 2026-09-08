# 04 Evaluation

Shared-benchmark status is a count of named public datasets, not a judgement of quality.

[Certain] Eight core sources have `data_type: benchmark`, seven `synthetic`, seven
`real-field`, and one `not stated` (TREMORS [[doi:10.48550/arxiv.2609.01777]]). Held-out
status is `not stated` for 15 of 23, `yes` for seven, and `no` for one.

[Certain] No single evaluation protocol is reused across subfields. Named public artefacts
that do recur inside one subfield are Norne and Volve in reservoir engineering
([[arxiv:2605.15028]], [[doi:10.48550/arxiv.2605.00060]]), Ridgecrest in seismology
([[doi:10.48550/arxiv.2603.21152]], [[doi:10.48550/arxiv.2607.24984]]), ESHM20 as a
hazard reference [[doi:10.1038/s44304-026-00262-z]], PUNQ-S3 in CCS
[[arxiv:2607.18557]], Marvin/Minelib in mine planning [[doi:10.3390/mining6020026]],
and MineBench in mineral-image reasoning [[doi:10.18653/v1/2025.findings-emnlp.1386]].
Each of those is used by at most two core sources in this set.

[Certain] Two CCS cores both use GEOS and do not share a test. Agents4GEOS reproduces
published PUNQ-S3 saturation curves [[arxiv:2607.18557]]. AutoSurrogate trains on 1000
synthetic SGeMS/GEOS realisations of an unnamed 80×80×20 aquifer, holds out 200 samples,
and scores R2 / RMSE / relative L2 against eight zoo architectures and three AutoML
searchers [[doi:10.1016/j.aei.2026.105058]]. The simulator is common; the evaluation
artefact is not.

[Certain] Several core papers compare against a classical solver or a published model
rather than against another agent. Sim2Schedule reports 94–99% of a Gurobi MILP NPV
[[doi:10.48550/arxiv.2606.10286]]. ESHM20-MCP matches official ESHM20 475-year spectral
accelerations within a median of 5% [[doi:10.1038/s44304-026-00262-z]]. GeoMCP matches
JRC Eurocode 7 worked-example resistances within 0.012%
[[doi:10.48550/arxiv.2603.01022]]. SeisEvo reports SNR gains over classic POCS and MSSA
[[doi:10.48550/arxiv.2608.18272]]. AutoSurrogate reports saturation R2 0.9532 against
RecurrentRUNet3D 0.9359 and Optuna TPE 0.8915 [[doi:10.1016/j.aei.2026.105058]].

[Certain] Other core papers compare against neural or RAG baselines. GeoMind reports
weighted F1 against 17 time-series and lithology models [[arxiv:2604.21501]]. STA-CoT
reports Pos.F1 / Avg.F1 / MCC against MCoT, RAG, tool-augmented and MineAgent
[[doi:10.18653/v1/2025.findings-emnlp.1386]]. The GraphRAG catalog paper compares against
vanilla vector-RAG and a rule-based reference graph [[doi:10.48550/arxiv.2607.24984]].
The Thebe NAS work retrains every baseline under an identical protocol
[[doi:10.48550/arxiv.2608.13889]].

[Certain] Two core papers report no quantitative headline result: TREMORS (two
illustrative FDSN workflows) [[doi:10.48550/arxiv.2609.01777]] and specfem-mcp (five
qualitative SPECFEM case studies, "high-fidelity results consistent with standard
baselines" with no number) [[doi:10.48550/arxiv.2512.14429]]. TADI executes a
130-question taxonomy and 95 pytest tests but does not score Evidence Grounding
[[doi:10.48550/arxiv.2605.00060]].

[Certain] Six of 23 core sources do not name the generator model, including Agents4GEOS
[[arxiv:2607.18557]], GeoMCP [[doi:10.48550/arxiv.2603.01022]], SeisEvo
[[doi:10.48550/arxiv.2608.18272]] and AutoSurrogate [[doi:10.1016/j.aei.2026.105058]].
A code URL is present on 8 of 23 core rows.

[Likely] Evaluation in the readable core is therefore local: each system defines a task,
a dataset and a metric. Where a public Earth-science artefact is used, it is used as that
paper's test, not as a community agent benchmark.
