# 00 Executive summary

LLM-based agentic systems in solid-earth and subsurface geoscience, as harvested and
screened in this run. Descriptive only.

[Certain] The harvest returned 11,191 unique records. Triage shortlisted 712. Screening
admitted 151 (41 core, 110 context). The below-cut audit sample of 150 records found 0
false negatives. Core means full text was read: 0 of 41 core rows are abstract-only.
Nineteen core sources were recovered from a full text obtained after the record was first
screened, across three institutional-access recovery passes (see `unreachable.md`):
AutoSurrogate from arXiv:2604.11945 after the Elsevier page was unread
[[doi:10.1016/j.aei.2026.105058]]; a first batch of seven (Hydro-Agent, OntoGRC, a tunnel
geological-forecasting agent, a well-log multi-agent framework, LogACF, the Geo-Resource
Agent and InsightsAI); a second batch of eight (a landslide-reconstruction agent, a
multimodal geotechnical-design framework, an uncertainty-aware tunnelling MAS, a
slope-reliability multi-agent framework, AGeoKE, the GAGAW journal record, EQSIM Agent and
a seismic-processing assistant); and a third batch of three EAGE extended abstracts (the
Geowellex MCP/A2A surface-logging agent, a LangGraph geological question-answering
pipeline, and a four-agent sedimentological-prediction workflow). The first of those
passes also read four paywalled records in full and found them not to be agentic once the
mechanism was visible; those four (including a second Ore Geology Reviews paper and a
ResearchGate deposit that turned out to be LLM-free multi-agent reinforcement learning)
are excluded from the corpus entirely, not merely left in context. No record in the second
or third pass was reclassified out.

[Certain] On the 41 readable sources, demonstrated maturity is M1 = 14, M2 = 13, M3 = 13,
M4 = 1, M5 = 0. The single M4 is HERMES, whose extraction was released as the live
Treatise.geoLex database [[doi:10.48550/arxiv.2608.14055]]. The thirteen M3 sources are
retrospective evaluations on named sites, campaigns or reference documents (Norne, Volve,
Ridgecrest, Santorini–Kolumbo, Qiaojia/Maduo, a Xiushan tunnel, the Aquia Aquifer, a
Xinjiang Fe–Pb–Zn assessment report, five Yunnan Province tunnels, four named Hong Kong
landslides, three named US hydrology field sites, the Acacia Grove-1 well, the USGS Mineral
Deposit Models and NASA Lunar Sample Compendium), not operator deployments.

[Certain] One of ten core subfields has no full-text core source: geomechanics (no
admitted source at all — its one candidate was reclassified to reservoir_engineering).
Seismology has the most readable systems (10), just ahead of reservoir_engineering and
engineering_geology (9 each). Reservoir engineering has the most admitted sources (70) and
nine of those in core. CCS has two core sources, both using GEOS, one as a runtime
simulator and one as a dataset generator.

[Certain] The modal techniques on the core tier are guardrails-validation, planning,
tool-calling, task-decomposition, retrieval and role-specialisation. Instrument-control
does not appear (`q001`–`q020`). Hierarchical multi-agent is the plurality architecture
(15 of 41), not the majority. MCP appears as a tool-exposure pattern in seven otherwise
different architectures; A2A, as a way of advertising whole agents rather than tools,
appears in one. Sixteen of 41 core sources are arXiv preprints; eleven of 41 do not name
the generator model; fourteen of 41 carry a code URL.

[Certain] No shared agent benchmark spans subfields. Named public artefacts that recur
inside one subfield (Norne, Volve, Ridgecrest, ESHM20, PUNQ-S3, Marvin, MineBench) are
each used by at most two core sources. Three core papers report no quantitative headline
result, and eleven record no baseline of any kind.

[Certain] One hundred and ten admitted sources cannot be maturity-rated because
only an abstract was available. That set is concentrated in industry venues: 61 of the 70
admitted reservoir-engineering sources are abstract-only. The core maturity distribution is
the readable slice, not the admitted literature.

[Likely] What exists, on this evidence, is a set of tool-calling and multi-agent
wrappers around existing simulators, catalogs, training loops and document pipelines,
evaluated mostly on synthetic cases, public benchmarks, or a single named retrospective
site, with one documented production knowledge-extraction run.
