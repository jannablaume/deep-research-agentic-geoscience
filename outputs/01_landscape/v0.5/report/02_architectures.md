# 02 Architectures

Architecture values are from the controlled list in `papers.csv` (23 core sources).

[Certain] Eight of 23 core sources are `multi-agent-hierarchical`. TRACE
[[doi:10.48550/arxiv.2603.21152]], GeoMind [[arxiv:2604.21501]], Agents4GEOS
[[arxiv:2607.18557]], HERMES [[doi:10.48550/arxiv.2608.14055]], STA-CoT
[[doi:10.18653/v1/2025.findings-emnlp.1386]], MINDS [[doi:10.3390/mining6020026]], the
PPV Evaluator-Optimizer [[doi:10.3390/geosciences16050176]] and AutoSurrogate
[[doi:10.1016/j.aei.2026.105058]] all put a planner or orchestrator above specialised
workers. That is a plurality, not a majority.

[Certain] Three sources are `multi-agent-flat`: PetroGraph's six-agent LangGraph
[[arxiv:2605.15028]], SeisEvo's Evolutionary Ensemble of Agents
[[doi:10.48550/arxiv.2608.18272]], and the three-model NAS panel
[[doi:10.48550/arxiv.2608.13889]]. Three are `single-agent`: GeoMCP
[[doi:10.48550/arxiv.2603.01022]], LandslideAgent [[doi:10.48550/arxiv.2606.18661]] and
GAIA [[doi:10.48550/arxiv.2511.03852]]. GAIA's authors state that the current version
"uses a single main agent" rather than a multi-agent system
[[doi:10.48550/arxiv.2511.03852]].

[Certain] Three sources are `agent-plus-database`: TADI over DuckDB/ChromaDB on Volve
[[doi:10.48550/arxiv.2605.00060]], TREMORS over FDSN datacenters
[[doi:10.48550/arxiv.2609.01777]], and GraphRAG over earthquake catalogs
[[doi:10.48550/arxiv.2607.24984]]. Two are `agent-plus-solver`: ESHM20-MCP wrapping
OpenQuake [[doi:10.1038/s44304-026-00262-z]] and specfem-mcp wrapping SPECFEM
[[doi:10.48550/arxiv.2512.14429]]. One is `agent-plus-simulator`: Sim2Schedule
[[doi:10.48550/arxiv.2606.10286]]. One is `router`: the foundation-design system
[[doi:10.1007/s43503-026-00088-8]]. Two are `pipeline-with-agent`: Fortran-to-Devito
[[arxiv:2601.18381]] and the borehole-report coordinate pipeline
[[doi:10.1038/s41598-026-61824-9]].

[Certain] MCP as a tool-exposure pattern appears in ESHM20-MCP
[[doi:10.1038/s44304-026-00262-z]], Agents4GEOS [[arxiv:2607.18557]], GeoMCP
[[doi:10.48550/arxiv.2603.01022]] and specfem-mcp [[doi:10.48550/arxiv.2512.14429]].
Those four are otherwise different architectures (solver, hierarchical, single-agent,
solver). MCP is how tools are advertised, not a system topology.

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
and never names it [[doi:10.1016/j.aei.2026.105058]]. Six of 23 core rows have
`base_model` beginning `not stated`.

[Likely] Hierarchical multi-agent is the plurality, not the majority. Single-agent
tool-calling over a database or solver is the other repeated pattern (TADI, TREMORS,
ESHM20-MCP, specfem-mcp). The two patterns are not ranked against each other in any
core source's evaluation except where a paper ablates its own roles (STA-CoT
[[doi:10.18653/v1/2025.findings-emnlp.1386]], GeoMind [[arxiv:2604.21501]]).
