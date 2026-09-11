# 02 Architectures

Architecture values are from the controlled list in `papers.csv` (38 core sources).

[Certain] Fourteen of 38 core sources are `multi-agent-hierarchical`. TRACE
[[doi:10.48550/arxiv.2603.21152]], GeoMind [[arxiv:2604.21501]], Agents4GEOS
[[arxiv:2607.18557]], HERMES [[doi:10.48550/arxiv.2608.14055]], STA-CoT
[[doi:10.18653/v1/2025.findings-emnlp.1386]], MINDS [[doi:10.3390/mining6020026]], the
PPV Evaluator-Optimizer [[doi:10.3390/geosciences16050176]], AutoSurrogate
[[doi:10.1016/j.aei.2026.105058]], a well-log multi-agent framework with a chief-engineer
planner over domain-expert agents [[doi:10.1016/s1876-3804(26)60734-3]], LogACF's
planning/execution/knowledge layers [[doi:10.1016/j.petsci.2026.05.031]], the
supervisor-ReAct-blackboard tunnelling MAS [[doi:10.1016/j.cacaie.2026.100079]], EQSIM
Agent's main agent over vision and RAG sub-agents [[doi:10.1145/3731599.3767402]], and the
slope-reliability framework's Orchestrating Agent over three subordinate agents
[[doi:10.1016/j.aei.2026.105065]], plus GAGAW's Context/Data/Inversion/Fusion/Evaluation
agent chain [[doi:10.1016/j.bdes.2026.100042]], all put a planner or orchestrator above
specialised workers. That is a plurality, not a majority.

[Certain] Six sources are `multi-agent-flat`: PetroGraph's six-agent LangGraph
[[arxiv:2605.15028]], SeisEvo's Evolutionary Ensemble of Agents
[[doi:10.48550/arxiv.2608.18272]], the three-model NAS panel
[[doi:10.48550/arxiv.2608.13889]], Hydro-Agent's Hydro-Coder/Executor pair
[[doi:10.1016/j.watres.2026.125886]], InsightsAI's named sub-agents over a shared
knowledge graph [[doi:10.2118/229435-ms]], and AGeoKE's four sequential agent teams
(OCR/preprocessing, Mindat matching, vocabulary preparation, vocabulary mapping)
[[doi:10.1016/j.acags.2026.100362]]. Five are `single-agent`: GeoMCP
[[doi:10.48550/arxiv.2603.01022]], LandslideAgent [[doi:10.48550/arxiv.2606.18661]], GAIA
[[doi:10.48550/arxiv.2511.03852]], the Geo-Resource Agent's LangGraph ReAct planner
[[doi:10.56952/igs-2025-0391]], and the Leading Edge seismic-processing assistant's
embedding-similarity tool selector [[doi:10.1190/tle44020142.1]]. GAIA's authors state
that the current version "uses a single main agent" rather than a multi-agent system
[[doi:10.48550/arxiv.2511.03852]].

[Certain] Three sources are `agent-plus-database`: TADI over DuckDB/ChromaDB on Volve
[[doi:10.48550/arxiv.2605.00060]], TREMORS over FDSN datacenters
[[doi:10.48550/arxiv.2609.01777]], and GraphRAG over earthquake catalogs
[[doi:10.48550/arxiv.2607.24984]]. Two are `agent-plus-solver`: ESHM20-MCP wrapping
OpenQuake [[doi:10.1038/s44304-026-00262-z]] and specfem-mcp wrapping SPECFEM
[[doi:10.48550/arxiv.2512.14429]]. One is `agent-plus-simulator`: Sim2Schedule
[[doi:10.48550/arxiv.2606.10286]]. One is `router`: the foundation-design system
[[doi:10.1007/s43503-026-00088-8]]. Six are `pipeline-with-agent`: Fortran-to-Devito
[[arxiv:2601.18381]], the borehole-report coordinate pipeline
[[doi:10.1038/s41598-026-61824-9]], OntoGRC's generate-reflect-correct loop
[[doi:10.1016/j.oregeorev.2026.107411]], the tunnel geological-forecasting agent's
perception-decision-feedback loop [[doi:10.1016/j.autcon.2026.107055]], the
landslide-reconstruction agent's two self-reflecting extraction/geometry pipelines
[[doi:10.1016/j.sandf.2026.101789]], and multi-GeoLLM's self-review-then-deterministic-tool
pipeline [[doi:10.1016/j.autcon.2025.106257]].

[Certain] MCP as a tool-exposure pattern appears in ESHM20-MCP
[[doi:10.1038/s44304-026-00262-z]], Agents4GEOS [[arxiv:2607.18557]], GeoMCP
[[doi:10.48550/arxiv.2603.01022]], specfem-mcp [[doi:10.48550/arxiv.2512.14429]], the
well-log multi-agent framework's inter-agent communication layer
[[doi:10.1016/s1876-3804(26)60734-3]], and AGeoKE's four agent teams, each exposed as a
callable MCP stage [[doi:10.1016/j.acags.2026.100362]]. Those six are otherwise different
architectures (solver, hierarchical, single-agent, solver, hierarchical, flat). MCP is how
tools are advertised, not a system topology.

[Certain] Two CCS cores both use GEOS, in opposite places. Agents4GEOS calls GEOS at
run time through `geos:run` [[arxiv:2607.18557]]. AutoSurrogate uses GEOS only to
generate the 1000-realisation training set; the deployed artefact is a neural surrogate
and the LLM never launches the simulator [[doi:10.1016/j.aei.2026.105058]].

[Certain] Several papers name a harness and not a model. Agents4GEOS names Claude Code
and routes to "the cheapest", "a mid-sized" and "the most capable" model without naming
any of the three [[arxiv:2607.18557]]. GeoMCP names ChatGPT and Claude as example MCP
clients and does not identify the walkthrough model [[doi:10.48550/arxiv.2603.01022]].
SeisEvo names only the EvE search backend [[doi:10.48550/arxiv.2608.18272]].
AutoSurrogate states that "all LLM inference is performed on a locally deployed model"
and never names it [[doi:10.1016/j.aei.2026.105058]]. InsightsAI and the Geo-Resource
Agent describe their agentic routines in detail but never name an underlying model
[[doi:10.2118/229435-ms]] [[doi:10.56952/igs-2025-0391]]. Nine of 38 core rows have
`base_model` beginning `not stated` — the same nine as before the second recovery pass:
every one of the sixteen recovered core sources across both passes names a specific
model.

[Likely] Hierarchical multi-agent is the plurality, not the majority. Single-agent
tool-calling over a database or solver is the other repeated pattern (TADI, TREMORS,
ESHM20-MCP, specfem-mcp). The two patterns are not ranked against each other in any
core source's evaluation except where a paper ablates its own roles (STA-CoT
[[doi:10.18653/v1/2025.findings-emnlp.1386]], GeoMind [[arxiv:2604.21501]]).
