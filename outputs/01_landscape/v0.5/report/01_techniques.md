# 01 Techniques

Technique counts below are source counts among the 23 full-text core rows.

[Certain] The most frequent controlled terms on the core tier are `guardrails-validation`
(19 of 23 sources), `planning` (18), `tool-calling` (14), `task-decomposition` (14),
`retrieval` (12) and `role-specialisation` (12). Next are `memory` (11), `self-reflection`
(10), `code-execution` (8) and `human-in-the-loop` (7). `simulator-in-the-loop` appears
on four sources, `physics-solver-in-the-loop` on three, `knowledge-graph` and
`multi-agent-debate` and `fine-tuning` on two each.

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

[Certain] Physics-solver-in-the-loop and simulator-in-the-loop remain the minority (3 and 4
core sources). PetroGraph history-matches through OPM Flow [[arxiv:2605.15028]].
Agents4GEOS runs GEOS via `geos:run` [[arxiv:2607.18557]]. Sim2Schedule never lets the LLM
call the mine simulator: the model returns a JSON action tuple that the simulator executes
[[doi:10.48550/arxiv.2606.10286]].

[Certain] Retrieval is used both as RAG over manuals and as catalog or literature search.
PetroGraph retrieves from the OPM Flow Reference Manual [[arxiv:2605.15028]]. GAIA retrieves
over a LanceDB of more than 5,000 geothermal papers [[doi:10.48550/arxiv.2511.03852]].
HERMES hybrid-retrieves BM25 plus dense vectors from ultra-long documents
[[doi:10.48550/arxiv.2608.14055]]. The GraphRAG catalog paper retrieves over a constructed
earthquake-event graph [[doi:10.48550/arxiv.2607.24984]].

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

[Certain] Fine-tuning is named on two core sources: GeoMind (Qwen3-4B SFT then MAPO)
[[arxiv:2604.21501]] and LandslideAgent (LoRA on Qwen3-VL-8B)
[[doi:10.48550/arxiv.2606.18661]]. The rest of the core tier uses prompted, tool-calling
or RAG-augmented models without reporting a training run on the agent itself.

[Likely] The technique profile of the readable core is therefore orchestration plus
validation. What the agent can call is more often a Python library, a catalog API, a
document index or a training loop than a physical device.
