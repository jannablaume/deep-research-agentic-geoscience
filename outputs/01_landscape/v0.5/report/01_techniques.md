# 01 Techniques

Technique counts below are source counts among the 38 full-text core rows.

[Certain] The most frequent controlled terms on the core tier are `guardrails-validation`
(33 of 38 sources), `planning` (29), `tool-calling` (27), `task-decomposition` (25),
`retrieval` (22) and `role-specialisation` (22). Next are `self-reflection` (21), `memory`
(17), `human-in-the-loop` (16) and `code-execution` (14). `physics-solver-in-the-loop`
appears on eight sources, `simulator-in-the-loop` and `knowledge-graph` on five each,
`fine-tuning` on three and `multi-agent-debate` on two.

[Absent-searched] `instrument-control` does not appear on any core row (`q001`–`q020`).

[Certain] Tool-calling is the mechanism that connects an LLM to a named simulator, solver,
catalog or database. TRACE calls ObsPy, SeisBench, GaMMA and HypoDD over SCEDC and EIDA
archives [[doi:10.48550/arxiv.2603.21152]]. TADI iterates twelve domain tools over DuckDB
and ChromaDB on the Volve daily drilling reports [[doi:10.48550/arxiv.2605.00060]].
ESHM20-MCP exposes twenty-four typed MCP endpoints wrapping OpenQuake
[[doi:10.1038/s44304-026-00262-z]]. specfem-mcp decomposes SPECFEM 2D/3D/Globe into
generate-mesh-solve-visualise tools [[doi:10.48550/arxiv.2512.14429]]. GeoMCP evaluates
closed-form geotechnical method cards through FastMCP [[doi:10.48550/arxiv.2603.01022]].
AutoSurrogate's agents issue structured tool calls for profiling, memory estimation, HPO
and training, while GEOS itself is used only to build the dataset
[[doi:10.1016/j.aei.2026.105058]].

[Certain] Physics-solver-in-the-loop (8 core sources) and simulator-in-the-loop (5) remain
a minority. PetroGraph history-matches through OPM Flow [[arxiv:2605.15028]]. Agents4GEOS
runs GEOS via `geos:run` [[arxiv:2607.18557]]. Sim2Schedule never lets the LLM call the
mine simulator: the model returns a JSON action tuple that the simulator executes
[[doi:10.48550/arxiv.2606.10286]]. Hydro-Agent's two agents write and self-debug MODFLOW
and TOUGHREACT calibration scripts, dynamically switching between a differential-evolution
global search and an L-BFGS-B/TNC local solver as the run progresses
[[doi:10.1016/j.watres.2026.125886]]. The SRAB tunnelling MAS invokes KALA, a discretized
kinematical-analysis solver, for tunnel-face stability risk assessment
[[doi:10.1016/j.cacaie.2026.100079]], and the slope-reliability framework's Sub-Agent 2
trains against an in-house NS-FEM finite-element solver, auto-debugging its own generated
training scripts when the solver run fails [[doi:10.1016/j.aei.2026.105065]].

[Certain] Retrieval is used both as RAG over manuals and as catalog or literature search.
PetroGraph retrieves from the OPM Flow Reference Manual [[arxiv:2605.15028]]. GAIA retrieves
over a LanceDB of more than 5,000 geothermal papers [[doi:10.48550/arxiv.2511.03852]].
HERMES hybrid-retrieves BM25 plus dense vectors from ultra-long documents
[[doi:10.48550/arxiv.2608.14055]]. The GraphRAG catalog paper retrieves over a constructed
earthquake-event graph [[doi:10.48550/arxiv.2607.24984]]. `knowledge-graph` recurs in three
of the newly-recovered core sources: the tunnel geological-forecasting agent's Cypher
retrieval over a Neo4j graph [[doi:10.1016/j.autcon.2026.107055]], InsightsAI's
ontology-driven graph linking WITSML entities to daily drilling reports
[[doi:10.2118/229435-ms]], and OntoGRC's OWL 2 DL ore-forming ontology used as a semantic
anchor for its generate-reflect-correct extraction loop [[doi:10.1016/j.oregeorev.2026.107411]].

[Certain] Role-specialisation and task-decomposition co-occur in the hierarchical
multi-agent papers: HERMES (Parser, Entity Recognizer, Annotator, Validator, Tracer)
[[doi:10.48550/arxiv.2608.14055]], STA-CoT (planner, executor, verifier)
[[doi:10.18653/v1/2025.findings-emnlp.1386]], MINDS (controller plus specialised agents)
[[doi:10.3390/mining6020026]], the Evaluator-Optimizer PPV workflow (Orchestrator,
Evaluator, Optimizer) [[doi:10.3390/geosciences16050176]], and AutoSurrogate (Data
Analysis, Model Selection, HPO & Training, Reporter) [[doi:10.1016/j.aei.2026.105058]].

[Certain] Self-reflection and memory are the loop, not the first action. AutoSurrogate
resumes training, tightens learning-rate bounds, or switches architecture when a run is
unstable or below a stated R2 target [[doi:10.1016/j.aei.2026.105058]]. STA-CoT majority-
votes candidate answers [[doi:10.18653/v1/2025.findings-emnlp.1386]]. SeisEvo keeps a
candidate and failure pool as search context [[doi:10.48550/arxiv.2608.18272]]. TADI and
TREMORS keep conversation or graph state across tool rounds
[[doi:10.48550/arxiv.2605.00060]] [[doi:10.48550/arxiv.2609.01777]].

[Certain] Multi-agent-debate appears twice: MINDS debates price scenarios
[[doi:10.3390/mining6020026]] and the Thebe NAS panel (Claude, GPT-5.1, Gemini 2.5 Pro)
debates architectures to unanimous consensus [[doi:10.48550/arxiv.2608.13889]].

[Certain] Guardrails-validation is the modal technique and is heterogeneous. GeoMCP
constrains a SymPy allowlist and Pint units [[doi:10.48550/arxiv.2603.01022]]. SeisEvo
applies programmatic legality gates to candidate reconstruction programs
[[doi:10.48550/arxiv.2608.18272]]. The borehole-report pipeline enforces a JSON schema
after prompting [[doi:10.1038/s41598-026-61824-9]]. HERMES runs a rule-based domain
Validator on nomenclature, units and chronostratigraphy [[doi:10.48550/arxiv.2608.14055]].
AutoSurrogate treats non-finite losses and exploding gradients as failure criteria that
trigger a recovery policy [[doi:10.1016/j.aei.2026.105058]].

[Certain] Fine-tuning is named on three core sources: GeoMind (Qwen3-4B SFT then MAPO)
[[arxiv:2604.21501]], LandslideAgent (LoRA on Qwen3-VL-8B)
[[doi:10.48550/arxiv.2606.18661]], and the landslide-reconstruction agent's fine-tuned
YOLOv8-seg segmentation model, used alongside a prompted multimodal LLM rather than a
fine-tuned one [[doi:10.1016/j.sandf.2026.101789]]. The rest of the core tier uses
prompted, tool-calling or RAG-augmented models without reporting a training run on the
agent itself.

[Likely] The technique profile of the readable core is therefore orchestration plus
validation. What the agent can call is more often a Python library, a catalog API, a
document index or a training loop than a physical device.
