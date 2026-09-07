# Annotated paper list

Smoke-test admits only. Grouped by subfield then tier.

## seismology

### core

**[[arxiv:2601.18381]] Hou & Yang 2026, Devito translation agent.** LangGraph pipeline that reverse-engineers Fortran finite-difference code into Devito via GraphRAG (Neo4j), static analysis, Pydantic output and quality routing. Evaluated on 11 retrieval queries and 13 synthetic Devito cases (Precision@5 0.964; Grade-A 76.9%). M1. Authors: fixed quality thresholds limit adaptability.

**[[doi:10.48550/arxiv.2609.01777]] Hill et al. 2026, TREMORS.** gpt-oss:120b parses natural language into a schema; LangGraph drives ObsPy/FDSN event and continuous waveform pulls. Demonstrated on example workflows, not a named operational campaign. M1. Authors: parsing fails on ambiguous prompts; depends on FDSN completeness.

**[[doi:10.48550/arxiv.2603.21152]] Liu et al. 2026, TRACE.** Hierarchical multi-agent planner/coder/checker with GPT-5 and 2200+ seismology modules. Applied to 2019 Ridgecrest and 2025 Santorini–Kolumbo. M3. Authors: bounded by physical-model fidelity and cost; sparse events need more validation.

### context

- [[doi:10.3997/2214-4609.202576039]] [context] EAGE abstract: generative synthetic data and agentic workflows for subsurface scaling.
- [[doi:10.3997/2214-4609.202639010]] [context] EAGE abstract: agentic coupling of seismic interpretation and data management.
- [[doi:10.1038/s44304-026-00262-z]] [context] LLM-agent MCP interface to end-to-end PSHA/risk.
- [[doi:10.22564/19cisbgf2025.335]] [context] conference abstract: seismic analysis with AI agents and LLMs.
- [[doi:10.1145/3731599.3767402]] [context] EQSIM Agent for conversational exploration of earthquake simulation data.
- [[doi:10.3997/2214-4609.202639107]] [context] EAGE abstract: generative and agentic AI in seismic processing and imaging.
- [[doi:10.3997/2214-4609.202639016]] [context] EAGE abstract: agentic AI for seismic noise-attenuation outcomes.
- [[doi:10.3997/1365-2397.fb2026015]] [context] First Break: agentic AI over SEG-Y/MDIO subsurface archives.
- [[doi:10.2118/222053-ms]] [context] SPE multimodal geoscience copilot.
- [[doi:10.48550/arxiv.2607.24984]] [context] automatic knowledge-graph construction for earthquake catalogs.
- [[doi:10.5281/zenodo.21768634]] [context] ESHM20-MCP software: LLM-agent interface to European hazard/risk models.
- [[doi:10.32604/cmes.2026.084591]] [context] review from ML to agentic AI in earthquake engineering.
- [[doi:10.1190/tle44020142.1]] [context] TLE: generative AI / LLM seismic processing assistant.
- [[doi:10.3997/2214-4609.202410350]] [context] EAGE: ReAct LLM seismic processing assistant.
- [[doi:10.22564/19cisbgf2025.463]] [context] agentic framework for petabyte-scale subsurface data.
- [[doi:10.3997/2214-4609.2025101096]] [context] EAGE: agentic AI for subsurface predictive modelling.
- [[doi:10.67704/oep.2025.250012]] [context] DAS described as integrable with AI agents.
- [[doi:10.48550/arxiv.2608.18272]] [context] SeisEvo: agents evolving seismic reconstruction algorithms.
- [[title:seismomcp]] [context] GitHub MCP servers wrapping ObsPy, SAC, CWP/SU, GMT.

## hydrogeology

- [[doi:10.1016/j.watres.2026.125886]] [context] LLM multi-agent inverse modelling of groundwater (no harvest abstract).
- [[doi:10.5194/egusphere-egu26-20010]] [context] GWFlowAI one-step explorer of Indian public groundwater datasets.

## geothermal

- [[arxiv:2511.03852]] [context] GAIA agentic RAG + digital twin for geothermal development (grey pass).
- [[doi:10.2118/232332-ms]] [context] SPE abstract: agentic AI geothermal simulation and site screening.

## reservoir_engineering

- [[doi:10.2118/229240-ms]] [context] ENERGYai agentic AI across O&G value streams.
- [[doi:10.2523/iptc-25122-ms]] [context] EnergyAI agentic RAG / A2A for subsurface insights.
- [[doi:10.2118/229444-ms]] [context] OSDU + Fabric architecture for upstream agentic AI.
- [[doi:10.2523/iptc-25138-ms]] [context] agentic AI for drill-bit forensics and automation.
- [[doi:10.2118/229682-ms]] [context] SPE perspective on upstream agentic AI.

## engineering_geology

- [[doi:10.64862/ajeg.2025.2sp.95.232]] [context] agentic ML pipeline for drift-aware debris-flow detection.
- [[doi:10.1016/j.autcon.2026.107055]] [context] AI agent for geological forecasting in rock tunnels (no harvest abstract).
- [[doi:10.5194/egusphere-egu26-20914]] [context] conversational AI for slope-stability monitoring.

## geomechanics, ccs, mining, inversion, geological_modelling

No admits in this slice.
