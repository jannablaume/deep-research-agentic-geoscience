# Gap candidates — 329 extracted from 01_landscape/v0.5, 02_tango/v0.2

Written by `scripts/gaps.py` from the runs' own artifacts. **Nothing here is a gap yet.** Each row is a place where a finished run recorded that something is absent, unstated, unevaluated, unread or empty. Deciding which of these are research gaps, which are artefacts of how the run was done, and which are neither is the reading job — and every candidate has to be accounted for, including the ones discarded.

A count here always carries its denominator. A candidate with an empty `count` is a statement someone made, not a measurement.


## absence-claim — 9

### c089
**01_techniques.md** — 01_landscape/v0.5 · q001;q020

`instrument-control` does not appear on any core row (`q001`–`q020`).

### c090
**07_periphery.md** — 01_landscape/v0.5 · q005;q006;q021;q030

No dedicated periphery harvest was run for hydrology-as-surface-water or ecology (`q005`, `q006`, `q021`–`q030`); those topics appear only where they matched a core or named-periphery query.

### c238
**00_executive_summary.md** — 02_tango/v0.2 · q007;q010

(backed by query cells `q007`-`q010`) No admitted source drives a full life-cycle cost model — levelised cost, discounted cash flow or equivalent — as the system it controls. Economic quantities appear as objectives inside optimisation loops, not as the driven artefact. Those cells were harvested without a paging cap and eighteen targeted web searches logged.

### c239
**00_executive_summary.md** — 02_tango/v0.2 · q001;q014

(backed by query cells `q001`-`q014`) **Nothing in the corpus reaches M4 or M5.** No source shows a system in routine use by people other than its authors, or an output that entered a real operational decision with third-party evidence. The 12 M3 rows are retrospective work against references the authors did not produce — a real reservoir [[doi:10.48550/arxiv.2605.15028]], named catalyst systems [[arxiv:2606.05050]], crash-validation decks [[doi:10.5281/zenodo.22554152]], an expert implementation [[doi:10.48550/arxiv.2607.15001]], six named campus buildings checked against metered energy use [[doi:10.2139/ssrn.7333555]]. One author calls it "an early exploration rather than a production-ready solution" [[doi:10.1080/19401493.2026.2653969]].

### c240
**03_touchpoints.md** — 02_tango/v0.2 · q007;q008;q009;q010

(backed by query cells `q007`, `q008`, `q009`, `q010`) No admitted source reports an agent driving a full life-cycle cost model — levelised cost of energy, discounted cash flow, or a comparable economic model — as the system it controls. The energy-systems and geoenergy query cells that would surface such work were run without hitting a paging cap on the OpenAlex side (`q007`, `q008`, `q009`, `q010`; `q007:arxiv` and `q009:arxiv` lost six and one record respectively to truncation) and the grey pass added eighteen further targeted web searches, logged as `w001`–`w018` in `queries.csv`; the shortlist they produced contains economic *objectives* inside optimisation loops, as cited above, but no system whose driven artefact is an economic model.

### c241
**04_evaluation.md** — 02_tango/v0.2 · q001;q006;q011;q014

(backed by query cells `q001`-`q006` and `q011`-`q014`) **No benchmark in this corpus is shared across domains.** The core query cells covering simulation orchestration, solver control, scientific computing and computational discovery (`q001` through `q006`, `q011` through `q014`) were harvested in full after the paging caps were raised, and the grey pass added eighteen targeted web searches; no admitted source proposes or uses a cross-domain evaluation of agents driving scientific codes. Two sources argue for one from opposite directions — one calls for benchmarks that "evaluate both final predictions and the workflows used to obtain them" [[doi:10.48550/arxiv.2607.22596]], another notes that its own evaluation "does not yet constitute a blinded third-party benchmark" [[arxiv:2602.20683]] — but neither builds it.

### c242
**05_maturity.md** — 02_tango/v0.2 · q001;q014

(backed by query cells `q001`-`q014`) **No admitted source demonstrates M4 or M5.** Nothing in the corpus shows a system in routine use by people other than its authors, or one whose output entered a real operational or design decision with third-party evidence. The core query cells were harvested in full after the paging caps were raised (`q001` through `q014`), the grey pass added eighteen targeted web searches aimed precisely at vendor and deployment material where such evidence would appear, and the industry sources it found report demonstrations rather than deployments [[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]]. Several sources say as much themselves: "this work represents an early exploration rather than a production-ready solution" [[doi:10.1080/19401493.2026.2653969]]; "strong benchmark performance should be interpreted as infrastructure readiness rather than clinical readiness" [[arxiv:2604.24696]]; "the results are early experience, not a controlled productivity benchmark" [[doi:10.20944/preprints202608.1323.v1]].

### c243
**06_failure_and_limits.md** — 02_tango/v0.2 · q001;q014

(backed by query cells `q001`-`q014`) **No admitted source reports a case where its agent's output was accepted, acted on outside the experiment, and later found to be wrong.** Failures are reported as run-time errors caught inside the loop, as benchmark cases not passed, or as capability gaps for future work — never as a downstream consequence. One source comes closest and marks the boundary: hallucinated PDB IDs were accepted by the pipeline and molecular dynamics ran on the wrong protein structures before the authors identified them [[doi:10.1145/3731599.3767349]]. That is an incorrect output acted upon, but inside the authors' own experiment and reported by them; no source reports one reaching a decision, a publication or a user. The core query cells were harvested in full after the paging caps were raised (`q001` through `q014`) and the grey pass added eighteen targeted web searches; nothing admitted describes an incident, a retraction, or a corrected result. Given that section 05 finds no source above M3, this is what one would expect — systems that have not entered routine use cannot yet have failed in it — but it means the corpus contains no evidence at all about how these systems behave when they are trusted.

### c244
**07_periphery.md** — 02_tango/v0.2 · q015;q022

(backed by query cells `q015`-`q022`) Beyond those six, no periphery record was read, so this run can say nothing about what the software-engineering or laboratory-automation literatures contain beyond their size and their group labels. The periphery cells (`q015` through `q022`) were harvested and triaged but never screened, and `shortlist.md` was read only for core-scope records. Any statement here about periphery *findings* would be unsupported, and none is made.


## author-limitation — 205

### c001
**open-darts-MCP** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202639027

automation only within controlled boundaries; validation and supervision remain under user control

### c002
**Agentic Optimizer** — 01_landscape/v0.5 · doi:10.5281/zenodo.20109894

the architecture is conceptual and is intended as a scalable design pattern rather than a validated field case

### c003
**Fortran-to-Devito** — 01_landscape/v0.5 · arxiv:2601.18381

Authors state that although the system stores comprehensive conversion history, 'its capabilities for advanced data mining and pattern discovery remain limited'; that the quality evaluation framework relies on fixed predefined thresholds that cannot adjust to code type, complexity or historical performance, so adaptability 'is constrained by this static configuration'; and they concede the reported MRR 'look[s] too good' because each query has a set of valid references rather than a unique target, which 'limits the ability of MRR to differentiate retrieval quality under the current evaluation configuration'.

### c004
**PetroGraph** — 01_landscape/v0.5 · arxiv:2605.15028

Authors state 'the improvement in the metric diminishes as the model size and complexity increase', that Norne shows only 'a modest, yet discernible, reduction in misfit', and that a residual wNRMSE of 2.01 leaves substantial mismatch; they record that the Parameterizer exceeded its own prompt guidance (79 parameters on Norne against a recommended 3-20). Future work: extend RAG to 'more nuanced simulator behaviour', add long-term memory for multi-stage history matching, refine the agent graph for multi-cycle campaigns.

### c005
**chen2026-gagaw** — 01_landscape/v0.5 · doi:10.1016/j.bdes.2026.100042

fusion example uses only sequential structure-constrained inversion, other joint/coupled methods not yet implemented; geophysics coverage narrow (ERT, seismic refraction, basic climate linkage only); uncertainty quantification propagates only petrophysical parameter uncertainty, not survey/electrode/temperature-drift errors; LLM hallucination and malformed-JSON failures documented during development

### c006
**not stated** — 01_landscape/v0.5 · doi:10.1016/j.geoai.2025.100036

barriers include limited foundational understanding, skepticism about AI reliability and a lack of standardized practices; rigorous validation needed

### c007
**ESHM20-MCP** — 01_landscape/v0.5 · doi:10.1038/s44304-026-00262-z

Default branch subsets do not cover every authorized ESHM20 logic-tree branch; 20 km area-source discretisation and finite distance cutoffs; deterministic highest-weighted branches rather than full-tree Monte-Carlo (principal source of residual); some taxonomy strings lack ESRM20 vulnerability functions; topographic-slope VS30 proxy is uncertain at a single site; first-call hazard timings 37-488 s per site on one CPU core.

### c008
**ENERGYai** — 01_landscape/v0.5 · doi:10.2118/229240-ms

data quality, QA/QC protocols, inconsistent data standards and concerns around trust and explainability remain key hurdles

### c009
**MINDS** — 01_landscape/v0.5 · title:largelanguagemodelagentsindynamicmineplanningamodulardecisionsupportframework

not available - abstract only

### c010
**not stated** — 01_landscape/v0.5 · doi:10.1109/access.2026.3714775

mining-specific LLM-agent implementations are largely conceptual and await empirical validation

### c011
**guo2026-slope-reliability-agents** — 01_landscape/v0.5 · doi:10.1016/j.aei.2026.105065

validated only on classic two-dimensional synthetic scenarios; complex simulation-level failures (defective geometry, meshing issues, non-convergence) are reported via tool diagnostics rather than fully auto-corrected; Monte Carlo sample size is not yet automatically selected; future work needed for 3D and multi-physics-coupled real-world cases

### c012
**luo2026-logacf** — 01_landscape/v0.5 · doi:10.1016/j.petsci.2026.05.031

relies on predefined workflows and expert rules, limiting autonomous generalization under completely unknown geological conditions; reliability strongly dependent on data quality (depth alignment, core-log consistency); multimodal alignment strategy designed mainly for the conventional logging-NMR task; validation mainly based on the SPWLA dataset and one unnamed tight sandstone case, applicability to carbonate/shale reservoirs unverified

### c013
**pang2026-landslidereconstruction** — 01_landscape/v0.5 · doi:10.1016/j.sandf.2026.101789

the framework is data-driven and does not directly simulate slope stability or hydrological processes; effectiveness may be reduced in rural/remote areas with less contextual information; the geometry-estimation workflow is semi-autonomous with human-in-the-loop review, and errors can propagate down the pipeline

### c014
**StripPool-UNet+FPN** — 01_landscape/v0.5 · doi:10.48550/arxiv.2608.13889

Authors report a cautionary finding that 'optimizing recall alone silently discards the best F1 designs', noting an earlier recall-driven search 'had kept a worse model and reverted its genuinely best design'; they state quantitative metrics are often insufficient for fault segmentation given incomplete and uncertain ground-truth labels, so the pipeline can discard valid architectures on minor metric regressions, and propose a future agent to judge visual quality; they note published Thebe results are not directly comparable because they use tolerance-based OIS/ODS matching on different splits, and that one debate run was aborted on a provider transport failure.

### c015
**GAIA** — 01_landscape/v0.5 · doi:10.48550/arxiv.2511.03852

Authors acknowledge the inversion problem is intentionally simplified and 'under-represents real world scenario', and that 'the primary outcome is not the recovered fracture parameters themselves'; that 'GAIA + AlphaEvolve did not optimize the evaluator, likely because the evaluator design space is more complex and less intuitive than the system prompt', so that comparison was omitted; that GAIA DT covers only seismic waveform analysis and visualisation while 'many other components need to be added'; that the default Richter magnitude method 'has limitations in accurately estimating the magnitude of large events and events with complex waveforms'; that the current version 'uses a single main agent' rather than a multi-agent system; that a general-purpose rather than geothermal-fine-tuned LLM is used; that physics-based simulations remain too expensive for real-time use pending surrogates; and that the Streamlit interface is a prototype.

### c016
**not stated** — 01_landscape/v0.5 · doi:10.2118/229586-ms

the large language model is yet to be fine-tuned to incorporate more data categories

### c017
**GeoCopilot** — 01_landscape/v0.5 · doi:10.2118/221864-ms

GenAI faces challenges such as data scarcity, interpretability issues, scalability and trustworthiness

### c018
**TREMORS** — 01_landscape/v0.5 · doi:10.48550/arxiv.2609.01777

Authors state the agentic framework 'reduces uncertainty associated with natural-language interpretation' but 'does not eliminate it'; that semantic parsing may fail on ambiguous, imprecise or unusually phrased prompts; that correctness depends on the validity of the parsed schema and on embedded default parameter choices; that the system depends on external FDSN services and ObsPy interfaces and so is sensitive to heterogeneous metadata standards, incomplete station information, service outages and variability across datacenters; and that agents 'are not yet capable of replacing high-level subject matter experts or independently producing scientific discovery'.

### c019
**not stated** — 01_landscape/v0.5 · doi:10.63374/qitp-ijpeat_07_02_001

existing research remains fragmented; key challenges in data governance, explainability, cybersecurity and integration with operational technology

### c020
**Geologist Copilot** — 01_landscape/v0.5 · doi:10.3997/2214-4609.2024101588

suggests further exploration integrating various drilling data and operational challenges; interpretation shown only with limited data availability

### c021
**not stated** — 01_landscape/v0.5 · doi:10.2118/229603-ms

developed as a rapid proof of concept within eight weeks

### c022
**not stated** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202637165

the example is deliberately conceptual and not conditioned on observational data

### c023
**not stated** — 01_landscape/v0.5 · doi:10.20944/preprints202604.1814.v1

petroleum benchmarks are scarce; reservoir and production sub-disciplines lag; industry deployments outpace academic publication

### c024
**GeoMind** — 01_landscape/v0.5 · arxiv:2604.21501

No dedicated limitations section. Authors acknowledge an inference-cost penalty of roughly 4.4-4.7 tool calls and three LLM forward passes per window, 1.31-1.71 s per window and up to 6.6 minutes per well, stating 'this is slower than neural-only baselines'; that 'the moderate gap between GeoMind and the variant without the validator suggests that the validator is helpful but not the sole source of improvement'; they frame gains as 'consistent classification improvements under the evaluated settings' and cross-backbone gains as 'preliminary results', and flag the policy-collapse risk that motivated K-fold stacking.

### c025
**TADI** — 01_landscape/v0.5 · doi:10.48550/arxiv.2605.00060

Section 6.3 lists: sparse-data wells 'produce lower-quality answers'; the agent does not ask clarifying questions when scope is ambiguous; recommendation and hypothetical answers rest on LLM reasoning that 'is not formally validated'; field-wide rankings outside the five implemented benchmark modes 'may produce incomplete answers'; tool-selection errors and the 10-round limit create 'planning pressure that the agent occasionally fails to navigate optimally'; heuristic keyword issue labels 'can produce lexical false positives in drilling jargon'; multi-step arithmetic across tool results 'may accumulate errors'. The author states the ablation and baseline analyses are 'qualitative expectations rather than executed benchmark results' and the output checks are 'intentionally lightweight compliance heuristics rather than semantic verification'.

### c026
**Evaluator-Optimizer workflow** — 01_landscape/v0.5 · doi:10.3390/geosciences16050176

Authors state the small dataset (n=102, 21 test cases) is the dominant limitation; no head-to-head AutoML baseline; prompt-length and nested-CV cost at larger scale; fitted PPV models are site-tied.

### c027
**not stated** — 01_landscape/v0.5 · doi:10.2118/224532-ms

AI cannot and should not replace a drilling engineer or automate the entire drilling cycle

### c028
**Youwai2026-foundation-router** — 01_landscape/v0.5 · doi:10.1007/s43503-026-00088-8

Authors call this a preliminary study: 'the limited sample size necessitates comprehensive validation on larger, more diverse datasets before deployment recommendations'; 'Safety-critical requirements necessitate continued human oversight'; with 27 test cases 'statistical power for detecting small effect sizes is inherently limited' (standard error about +/- 4-6 percentage points).

### c029
**ESHM20-MCP** — 01_landscape/v0.5 · doi:10.5281/zenodo.21768634

not available - software deposit description only

### c030
**ENERGYai** — 01_landscape/v0.5 · doi:10.2118/229682-ms

key challenges remain in ensuring data quality; implementing robust QA/QC processes; and building trust in autonomous decision-making systems

### c031
**not stated** — 01_landscape/v0.5 · doi:10.2118/233094-ms

extraction completeness depends on input data quality; the system does not replace engineering judgement

### c032
**not stated** — 01_landscape/v0.5 · doi:10.2118/0925-0003-jpt

worries linger about the technology's tendency to hallucinate when providing answers

### c033
**kanfar2025-seismic-assistant** — 01_landscape/v0.5 · doi:10.1190/tle44020142.1

dependency on predefined tools/workflows limits handling of novel or highly specialized tasks; likely to hallucinate when multiple requests are given in a single query; demonstrated failure to execute three chained tasks and a guardrail bypass on an out-of-scope query

### c034
**not stated** — 01_landscape/v0.5 · doi:10.3390/computers15050294

primary challenges are noisy HTML structures and incorrect DOM element selection

### c035
**chen2026-well-log-multiagent** — 01_landscape/v0.5 · doi:10.1016/s1876-3804(26)60734-3

operation is strictly confined to a predefined toolset, preventing agents from independently writing or debugging new scripts to handle unexpected issues; the agent interaction structure still relies on manual presets, limiting adaptive adjustment to new scenarios; growing information/tool scale increases processing noise on the shared memory environment

### c036
**not stated** — 01_landscape/v0.5 · doi:10.3997/2214-4609.2025101389

Phi-3 Mini exhibited occasional hallucinations despite being cost-efficient

### c037
**InsightsAI** — 01_landscape/v0.5 · doi:10.2118/229435-ms

not stated as explicit limitations; future scope named instead: hybrid ML+GenAI workflow for auto-calibration of torque/drag friction factors; RAG-based ingestion of legacy systems into OSDU; reading PDFs containing trajectories, motor specifications, ladder plots and spider diagrams

### c038
**geo-drill-extractor** — 01_landscape/v0.5 · doi:10.1038/s41598-026-61824-9

Single-project dataset; confidentiality and no released real documents; no manually verified coordinate ground truth so CSR is executable-output compliance not geometric accuracy; provider-dependent latency.

### c039
**EQSIM Agent** — 01_landscape/v0.5 · doi:10.1145/3731599.3767402

models cannot always self-correct malformed tool calls after several attempts; only one user request supported at a time (no concurrent task execution); non-vectorizable multi-step tasks show degraded accuracy; LLM may misrepresent correct tool output when summarizing

### c040
**STA-CoT** — 01_landscape/v0.5 · doi:10.18653/v1/2025.findings-emnlp.1386

Authors state increased computational overhead from multi-step execution and iterative refinement, 'which may result in higher inference latency and resource usage'; that 'the toolkit design is tailored to domain-specific characteristics, and the scalability of STA-CoT to larger-scale or cross-domain multi-image reasoning tasks remains to be systematically validated'.

### c041
**not stated** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202639107

challenges remain in reliably interpreting user intent and ensuring context-aware responses

### c042
**Agents4GEOS** — 01_landscape/v0.5 · arxiv:2607.18557

Authors state 'several limitations remain': meshing complex reservoirs 'is particularly challenging and warrants a dedicated specialized agent'; although jobs can be launched on clusters, 'more robust skill coverage is needed to ensure all simulations complete correctly'; interacting with running simulations 'remains an open direction'; and token usage 'has emerged as a meaningful factor in the overall budget, one that is no longer secondary to CPU or GPU hours'. Within the session they report unresolved issues verbatim: an injection-rate discrepancy between the two source papers that 'remains unreconciled in the sources', a relative permeability that is 'an endpoint fit rather than the raw published curve', plan-view maps that 'used a density-based proxy', GEOS rejecting the first deck twice at run time despite valid XML, and the post-processing subagent initially plotting the domain maximum instead of the benchmark observation points. They also note only 9 of 1,490 ALE task instances come from Mining, Petroleum and Geological Engineering.

### c043
**not stated** — 01_landscape/v0.5 · doi:10.1109/caibda65784.2025.11182767

not available - abstract only

### c044
**Sim2Schedule** — 01_landscape/v0.5 · doi:10.48550/arxiv.2606.10286

No limitations section. In the conclusion and results the authors acknowledge that evaluation has not been extended to 'larger real-world block models', that geological grade uncertainty and commodity price variability are not in the simulator state, that a 'remaining optimality gap' persists, that DeepSeek 'yields a lower NPV at N = 45, indicating reduced robustness at larger scales', and that 'the local LLM implementation lacks native long-term memory'.

### c045
**GeoSAGE** — 01_landscape/v0.5 · doi:10.5281/zenodo.19078874

not available - software deposit description only

### c046
**xu2025-multi-geollm** — 01_landscape/v0.5 · doi:10.1016/j.autcon.2025.106257

relies on reference examples and if-elif-else logic tools, so engineers must prepare examples and manually update tools for new design logic; initialized for idealized, horizontally layered homogeneous strata and rigid/flexible footings, with reduced performance expected for heterogeneous strata or semi-rigid footings; effective agents require powerful commercial LLMs, creating cost/latency dependence

### c047
**ma2026-hydroagent** — 01_landscape/v0.5 · doi:10.1016/j.watres.2026.125886

the current implementation operates within a predefined conceptual model and does not independently revise stratigraphic interpretations, modify facies distributions, or adjust boundary conditions based on site-history information; the coupled hydrogeochemical models assumed spatially homogeneous reaction parameters and did not invert spatially distributed geochemical reaction fields; LLMs cannot yet substitute for the diagnostic capacity of a hydrogeologist in interpreting the mechanistic implications of modeling discrepancies

### c048
**Zhou2026-GraphRAG-catalogs** — 01_landscape/v0.5 · doi:10.48550/arxiv.2607.24984

Authors state precise-statistics queries remain weak across all conditions (0.50-1.04/3), attributing this to 'a fundamental structural flaw in retrieval-then-synthesize architectures when handling aggregate or ranking tasks' and recommending such questions be routed to deterministic database queries; that residual hallucinations persist after the fixes, including the true Ridgecrest M7.1 mainshock being misdated in 50-70% of relevant answers and an out-of-catalog Maduo mainshock presented as the catalog's own largest event in up to 60% of narrative-enriched answers; that per-catalog verification remains necessary before deployment, especially for well-known events; that narrative-text enrichment lowered scores for two of three catalogs and should be adopted only with per-catalog verification; and that because all results rely on a single model, hallucination rates and fix effectiveness might differ with another model.

### c049
**GeoIME-GPT** — 01_landscape/v0.5 · doi:10.1016/j.gsf.2026.102445

some data privacy and algorithm optimization issues

### c050
**not stated** — 01_landscape/v0.5 · doi:10.2118/227420-ms

insights were extracted from simulated field data; future enhancements needed for retrieval, validation and reasoning modules

### c051
**not stated** — 01_landscape/v0.5 · doi:10.2118/227906-ms

proof-of-concept implementation focused only on stuck pipe

### c052
**qian2026-srab** — 01_landscape/v0.5 · doi:10.1016/j.cacaie.2026.100079

does not adopt multiple forward-backward algorithms for autonomous rollback, citing context-management risk in multi-step reasoning; does not automatically switch to backup models; does not employ parallel agent execution; streaming-data anomaly detection is out of scope; robustness on other large-scale infrastructure projects left to future work

### c053
**not stated** — 01_landscape/v0.5 · doi:10.1016/j.geoai.2026.100106

important questions remain regarding reliability, robustness, evaluation, and human oversight

### c054
**not stated** — 01_landscape/v0.5 · doi:10.1016/j.jgsce.2024.205469

need for skilled professionals for implementation and limitations of model training on constrained datasets affecting adaptability across contexts

### c055
**not stated** — 01_landscape/v0.5 · doi:10.2118/221883-ms

ensuring data quality and navigating the complexity of operations

### c056
**not stated** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202410350

token limitations in interacting with the LLM

### c057
**not stated** — 01_landscape/v0.5 · doi:10.2118/228117-ms

difficulty compiling answers across a large set of documents and finding information within plots and graphs

### c058
**TRACE** — 01_landscape/v0.5 · doi:10.48550/arxiv.2603.21152

Authors state the efficacy of TRACE 'remains intrinsically bounded by the fidelity of underlying physical models and the computational cost of high-fidelity simulations', and that its performance 'under extreme or data-sparse seismic events requires further validation through the integration of real-time observational streams and adaptive learning algorithms'; they describe a 'dual-ceiling effect' in which seismological tool precision sets the operational baseline while scientific rigour is capped by the reasoning depth of the underlying LLM.

### c059
**sun2026-tunnel-agent** — 01_landscape/v0.5 · doi:10.1016/j.autcon.2026.107055

open-source multimodal LLMs (e.g. Qwen2.5-VL) still exhibit a noticeable gap in image recognition capability; since drill-and-blast tunnelling remains predominantly manual, the risk-control decisions generated by the agent and fed back through the iS3 platform must ultimately be executed by human operators, so fully automated or mechanized execution is not yet achievable

### c060
**Geo-Resource Agent** — 01_landscape/v0.5 · doi:10.56952/igs-2025-0391

our evaluation remains preliminary; the case studies illustrate feasibility but do not exhaust the range of geological and engineering scenarios where such agents could be deployed; demonstrating the full benefits of the framework will require more extensive benchmarking, rigorous validation across datasets, and careful testing of corner cases

### c061
**not stated** — 01_landscape/v0.5 · doi:10.2118/230773-ms

LLMs operate without inherent grounding in physical feasibility and can produce plausible but non-physical explanations; over-trust, automation bias and de-contextualized reasoning erode reliability

### c062
**not stated** — 01_landscape/v0.5 · doi:10.20944/preprints202607.2303.v1

extreme label scarcity in a positive-unlabeled setting, spatial non-stationarity that violates i.i.d. assumptions, and multi-format data heterogeneity

### c063
**X2Sim** — 01_landscape/v0.5 · doi:10.26153/tsw/62180

may not match the accuracy of high-fidelity numerical methods

### c064
**ccsnet.ai** — 01_landscape/v0.5 · doi:10.1162/daed.a.995

such work still needs to be scaled up to support industrial use

### c065
**SeisEvo** — 01_landscape/v0.5 · doi:10.48550/arxiv.2608.18272

Authors state the discovered mechanisms 'are not conceptually new'; that the offline search cost is 'substantially more expensive than running a fixed hand-designed solver'; that the present evidence 'is restricted to seismic data reconstruction' and extension to denoising, deconvolution and inversion 'remains a hypothesis to be tested rather than a demonstrated capability'; that the seed and objective are fixed before each run and the effect of their choice 'has not been studied systematically'; that a single search trajectory per case cannot establish whether the budget is adequate; that the SNR and SSIM objectives require a complete reference so the protocol suits offline discovery only; and that for Evo-MSSA at low input SNR 'its error volume still contains coherent signal energy and random noise, indicating signal leakage and residual noise'.

### c066
**not stated** — 01_landscape/v0.5 · doi:10.5194/egusphere-egu26-20914

ensuring project-level access controls are respected, handling heterogeneous geospatial references, providing tailored representations across spatial scales, and maintaining transparency and reliability in automatically generated outputs

### c067
**AI Drilling Agent** — 01_landscape/v0.5 · doi:10.2118/223828-ms

presents ongoing research progress; real-time data and digital twins left to future work

### c068
**not stated** — 01_landscape/v0.5 · doi:10.3390/app16168089

the reported F1 score characterizes the end-to-end verification task rather than an autonomous safety decision capability

### c069
**OntoGRC** — 01_landscape/v0.5 · doi:10.1016/j.oregeorev.2026.107411

pretraining-corpus opacity of the base LLM cannot rule out prior exposure to geological literature; results derived from Chinese-language texts only and may reflect regional terminology; long-range inter-sentence metallogenic information can exceed the model's effective context window and break the affiliation chain; synonym mapping/coreference resolution can fail under concise or thematically volatile paragraphs; spatial modelling and ontology interoperability comparatively weak; numerical-attribute (grade/threshold) representation not yet strengthened

### c070
**LandslideAgent** — 01_landscape/v0.5 · doi:10.48550/arxiv.2606.18661

Authors state their findings 'delineate the inherent cognitive boundaries of the current static reasoning paradigm': spectral confusion from high intra-class variance 'imposes a persistent bottleneck on fine-grained classification', and marginal gains on kinematic characteristics show that 'relying on single-frame static snapshots fundamentally restricts the agent's capacity to reconstruct complex hazard dynamics', which they call 'an ill-posed challenge even for advanced multimodal architectures'. They acknowledge LandslideVLM's 52.05% fine-grained accuracy 'still lags significantly behind the dedicated pure-vision models', so VLMs 'cannot yet entirely supplant specialized interpretative models'; that SegFormer's Landslide-IoU ceiling below 77% means unimodal optical features 'remain insufficient for precise landslide delimitation'; and that the agent's own report states 'no calibrated overall confidence score is reported'.

### c071
**GWFlowAI** — 01_landscape/v0.5 · doi:10.5194/egusphere-egu26-20010

limitations related to data resolution, uncertainty, and spatial coverage

### c072
**not stated** — 01_landscape/v0.5 · doi:10.3390/pr13051413

challenges remain including data quality, model interpretability, and the need for high-performance computing resources

### c073
**jacinto2025-smart-agents** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202535040

the two architectures were tested in separate scenarios and the hybrid A2A-orchestrator-over-MCP-tools design named in the conclusion was not evaluated; the well is not named and the base model is not stated

### c074
**GAGAW** — 01_landscape/v0.5 · doi:10.22541/essoar.176336946.65126612/v1

abstract says limitations are outlined but does not state them

### c075
**AGeoKE** — 01_landscape/v0.5 · doi:10.1016/j.acags.2026.100362

vocabulary-adaptive extraction still requires configuration and relies on hard-coded vocabulary parsing; GeoSciML vocabulary is terrestrial-biased and misapplies Earth-centric terms to lunar samples; output is limited to controlled-vocabulary terms, lacking relational/assertion-level knowledge; manual evaluation used a single reviewer with no inter-rater reliability reported

### c076
**specfem-mcp** — 01_landscape/v0.5 · doi:10.48550/arxiv.2512.14429

none stated - the Conclusion and Outlook contains only forward-looking statements about future capability (expanding MCP coverage to preprocessing, postprocessing, imaging, inversion and interpretation tools, deeper integration with inversion workflows, and enhancing error correction and experience summarization), and no shortcoming of the present system is acknowledged

### c077
**alakkas2026-langgraph-rag** — 01_landscape/v0.5 · doi:10.3997/2214-4609.202639012

the Word2Vec plus embedding metric was not discriminative between models and fails to detect subtle variations in output quality; the authors conclude that scientific LLM evaluation requires multiple assessment methods

### c078
**seksaf2025-multiagent-rag** — 01_landscape/v0.5 · doi:10.3997/2214-4609.2025640024

further real-world testing and validation across diverse geological settings will be essential; future work is to expand the individual agents, particularly the geological principles agent, and to use LLMs with a larger context window

### c079
**GALA** — 01_landscape/v0.5 · doi:10.1109/cait70489.2026.11553853

not available - abstract only

### c080
**MINDS** — 01_landscape/v0.5 · doi:10.3390/mining6020026

LLM non-determinism needing industrial guardrails; demonstration relied on synthetic Marvin and curated news feeds; debate currently evaluates commodity price only.

### c081
**Mining AGI Platform** — 01_landscape/v0.5 · doi:10.5281/zenodo.21204632

conceptual and methodological article; explicitly not presented as an autonomous AGI system, a generic language-model assistant, or a replacement for Competent Persons, Qualified Persons or statutory engineering authorities

### c082
**AutoSurrogate** — 01_landscape/v0.5 · doi:10.1016/j.aei.2026.105058

No dedicated limitations section. Residual saturation errors 'are primarily concentrated near the plume boundaries'; 'discrepancies may also be attributed to limitations in the available training data'. Pressure self-correction exhausted its retry budget and fell back to the global-best ResUNet3D checkpoint. The generator LLM is never named.

### c083
**HERMES** — 01_landscape/v0.5 · doi:10.48550/arxiv.2608.14055

Authors state the two-stage strategy 'introduces potential error propagation' with 'cascading errors in the output structure' when entities are missed or merged; that conservative paragraph filtering 'can also reduce recall when genuinely relevant fossil descriptions are incomplete or expressed without these cues'; that chunking and RAG on extremely long documents 'inevitably introduces a trade-off between efficiency and recall', consistent with lost-in-the-middle findings; that cross-page discontinuity can split a description so 'the latter part of the split description can be excluded'; that 'fully understanding table semantics remains difficult' for cross-page tables, merged cells and footnotes; that performance 'is influenced by the underlying OCR and layout analysis algorithms', worse for older scans; and that expert verification throughput 'represents a practical bottleneck'.

### c084
**GeoMCP** — 01_landscape/v0.5 · doi:10.48550/arxiv.2603.01022

Section 6.3 states 'The JRC validation demonstrates precision within a specific problem class' and that 'A production-ready release of GeoMCP will require systematic validation across a broader range of geotechnical problems'; that the method card approach 'is inherently restricted to closed-form equations and iterative systems'; that the framework 'does not eliminate the potential for reasoning or data extraction errors' because the LLM interprets the scenario and extracts parameters, so interpretation errors 'will propagate into the engine's inputs'; and that auditable, citation-rich output introduces 'the secondary risk of automation bias' that 'may discourage necessary critical review', making independent checking essential. The walkthrough also records that settlement 'has not been checked' and that reproducing the JRC numbers requires resolving a documented inconsistency in the source (groundwater at 1.5 m in the text against 2.5 m in the figure).

### c085
**petromcp** — 01_landscape/v0.5 · title:petromcplocalfirstmcpserverforpetroleumdataformatslasdlissegyheaderspumpcards

SEG-Y support via segyio is only queued and not yet implemented

### c086
**volve-drilling-advisor** — 01_landscape/v0.5 · title:volvedrillingadvisorrealtimedrillingadvisoryagenttoolcallingaimonitoringvolvewellf15drillingparameters

the queries behind each tool are hand-written so the model cannot go off-script

### c087
**not stated** — 01_landscape/v0.5 · title:designingagenticaisystemsforsubsurfaceworkflowslessonsfromautomatingwellloginterpretation

LLMs are stateless, probabilistic and conversational while engineering tools are physics-constrained and precise; autonomy should be granted only where the task is repeatable, auditable and physics-bounded

### c088
**not stated** — 01_landscape/v0.5 · doi:10.48550/arxiv.2608.22068

LLM-generated outputs can be prone to subjective biases and hallucinations

### c121
**Agentic Optimizer** — 02_tango/v0.2 · doi:10.5281/zenodo.20109894

the authors state the architecture is conceptual and is intended as a scalable design pattern rather than a validated field case

### c122
**AUDiTs** — 02_tango/v0.2 · doi:10.1007/s44212-025-00099-3

the authors identify bias and fairness among critical challenges

### c123
**ModSolAgent** — 02_tango/v0.2 · doi:10.1109/tii.2026.3669495

the authors name AI-generated hallucination as a key challenge for tasks requiring precise intent

### c124
**Bahukhandi2025-xai-subsurface-review** — 02_tango/v0.2 · doi:10.36227/techrxiv.175979241.11582889/v1

the author names lack of explainability as the major barrier to adoption in high-stakes decision-making

### c125
**FactoryFlow** — 02_tango/v0.2 · arxiv:2603.25898

the authors state that resilience to LLM hallucination, human oversight and real-time model adaptability remain challenging and often mutually conflicting requirements

### c126
**RASER** — 02_tango/v0.2 · arxiv:2609.03598

the authors state that traditional HPC job schedulers such as Slurm are not designed for dynamic, agentic workflows

### c127
**VicenteMartinez2026-conversational-dt** — 02_tango/v0.2 · doi:10.3390/electronics15091869

the authors state that additional variables such as energy, water and waste are envisioned for future work and were not part of the current validation

### c128
**Kalinin2026-dual-digital-twins** — 02_tango/v0.2 · doi:10.26434/chemrxiv.15005632/v1

the authors state that open decision-making algorithms such as MCDTs, reinforcement learning or dynamic programming are very limited for experimental scenarios due to extreme data requirements

### c129
**Shikalgar2026-urban-mobility-dt** — 02_tango/v0.2 · title:intelligentdigitaltwinsystemforurbanmobility

the author names expensive computation at city-scale and difficulty integrating multi-modal transportation services as challenges

### c130
**Goyal2026-agentic-dt-survey** — 02_tango/v0.2 · doi:10.1109/mcomstd.2026.3669229

the paper carries an explicit limitations section, unread because the full text is blocked

### c131
**Wan2026-pde-llm-review** — 02_tango/v0.2 · arxiv:2608.03600

the authors state the field remains limited by the scarcity of high-quality datasets and benchmarks, especially for knowledge discovery

### c132
**Chatar2026-drilling-language-ai** — 02_tango/v0.2 · doi:10.2118/230773-ms

the authors state that such systems operate without inherent grounding in physical feasibility, so incorrect or incomplete contextual inputs can produce plausible but non-physical outputs

### c133
**DTAI** — 02_tango/v0.2 · doi:10.1109/ticps.2026.3665499

the authors state AI agents remain weak in plan verification and are vulnerable to perception errors caused by dynamic environments and inconsistent Industrial Internet of Things data

### c134
**Sochat2026-descriptive-execution** — 02_tango/v0.2 · doi:10.48550/arxiv.2607.10081

the authors state it is important to assess reliability and strategies scoped to specific tasks

### c135
**AI-DT** — 02_tango/v0.2 · doi:10.3389/frai.2025.1655470

the authors state the framework envisions incorporating explainable AI but that this is not implemented

### c136
**DT Agent** — 02_tango/v0.2 · doi:10.1109/e-cargo65996.2025.11139170

the authors state existing digital twin systems have limitations in responding to dynamic environments, providing real-time feedback, and making adaptive decisions

### c137
**RUNSPEC** — 02_tango/v0.2 · title:runspecspectreaiagenticgenerationanditerationofopmflowreservoirsimulationdecks

the vendor states that full-field history matching with 200 wells still needs other solutions

### c138
**SimAgent** — 02_tango/v0.2 · doi:10.1145/3731599.3767349

the authors state that "Due to the LLM tool call limitation and computing system requirements, it still requires tailoring of the tool call setup depending on the tasks and computing platforms"; that the ensemble implementation makes it "the user's responsibility to develop the simulation ensemble function with Parsl"; that "the computing nodes had no internet access by default, and the unpredictable queue time on the HPC system caused delays"; and that merging topology building into the simulation function is "less dependent on the LLM capability, and less likely to err, but too rigid for more sophisticated tasks". Future work names "reducing the user interaction with Parsl, implementing function environment management, improving logging and checkpointing, and enabling asynchronous execution"

### c139
**Pham2026-multi-agent-mof-screening** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.07681

the authors state the observed success rate of 84% indicates a remaining reliability gap, that invalid generated arguments led to workflow termination, and that overhead is highly dependent on model inference throughput and API latency

### c140
**CFD-copilot** — 02_tango/v0.2 · doi:10.48550/arxiv.2512.07917

the authors state a primary limitation remains the reliability of generating robust solver configurations for highly complex flows, as indicated by the modest success rate for the 30P-30N case, and that meshes lacked the necessary resolution and structural adaptability at higher angles of attack

### c141
**PDE-Agents** — 02_tango/v0.2 · doi:10.48550/arxiv.2606.07850

the authors state the current solver supports only scalar heat equations, the verification study covers only steady-state and simple transient heat equation benchmarks, and the current architecture runs agents sequentially

### c142
**APS-Agent** — 02_tango/v0.2 · doi:10.1016/j.dche.2026.100312

the authors state that "current limitations mainly involve the accurate interpretation of the physical results seen in minor reasoning mistakes, such as oversimplification or misleading suggestions, mean expert oversight is still needed"; that for inexperienced users "the main risks are overtrust in fluent but overconfident explanations, difficulty distinguishing highly relevant from marginal suggestions under open-ended prompts, and limited ability to detect unsupported derived values (e.g., economic estimates) without additional checks"; that for experienced users the limitations "include occasional semantic mismatch in variable selection despite correct retrieval, non-negligible review effort for convergence-sensitive synthesis steps"; that the single-prompt synthesis mode raised "attempts to set unspecified variables, premature parameter adjustments, and minor redundancies in tool usage"; and that "The main residual weakness is therefore semantic interpretation rather than protocol execution". They position the system as "best positioned as a copilot that accelerates workflow execution, rather than as an autonomous decision-maker"

### c143
**DynaMate2** — 02_tango/v0.2 · doi:10.48550/arxiv.2605.20819

the authors state agent reliability is the most pressing concern, that generated tool code may contain subtle errors undetected until runtime because registration only checks syntactic validity, that all agents run sequentially within a single process which limits throughput, and that the implementation does not by itself constitute a security boundary

### c144
**KBase Research Agent** — 02_tango/v0.2 · doi:10.1145/3815572.3815744

the authors state the framework focuses on assembly and annotation workflows for isolate microbial reads and does not cover the full diversity of analysis types, excluding metagenomics, pangenome and metabolic modelling

### c145
**ALL-FEM** — 02_tango/v0.2 · doi:10.1016/j.cma.2026.118985

the authors state the multi-agent system is not totally autonomous end-to-end since it presently depends on a human termination step via the Admin agent, and that the dataset, agentic process and assessment methodology require design choices that restrict the scope of the study

### c146
**PUR-1 GPT** — 02_tango/v0.2 · doi:10.25394/pgs.32118403

the authors state the present implementation remains a proof-of-concept, that its practical utility depends on the fidelity and trustworthiness of the underlying models, that PUR-1 GPT should be evaluated through domain-specific benchmarks assessing tool-selection correctness and prompt-injection resistance, and that the architecture should remain firmly human-in-the-loop

### c147
**Schafer2026-chemasim-process-agent** — 02_tango/v0.2 · doi:10.48550/arxiv.2603.12813

the authors state the system is currently not able to fully cope with the analysis of complex thermodynamic systems and lacks tools for analyzing complex thermodynamic behavior

### c148
**WARA** — 02_tango/v0.2 · doi:10.48550/arxiv.2608.14573

the authors state the remaining gap to accepted peer-reviewed wireless papers lies mainly in experimental depth and evidence maturity

### c149
**Foam-Agent** — 02_tango/v0.2 · doi:10.48550/arxiv.2509.18178

the authors state essentially no limitations, offering only future directions - extending its modular services to other solvers and enhancing physics coverage

### c150
**PhyNiKCE** — 02_tango/v0.2 · arxiv:2602.11666

the authors break down the 49% of failing cases as 10% semantically misaligned but runnable, 32% simulation-halting errors terminating on divergence or unphysical results with root cause ambiguity, and 7% exceeding the reflection threshold, and conclude that the bottleneck is no longer model capability but the density and structure of the domain-specific knowledge base

### c151
**GAIA** — 02_tango/v0.2 · doi:10.48550/arxiv.2511.03852

the authors state GAIA plus AlphaEvolve did not optimize the evaluator, that the fracture-network problem under-represents real world scenarios, and that the distinguishing feature is not higher accuracy of the underlying algorithms but the autonomous orchestration

### c152
**Bhandari2026-local-agentic-dft-audit** — 02_tango/v0.2 · doi:10.48550/arxiv.2608.29665

the authors state that qwen3:4b possesses usable semantic competence but severe structural fragility necessitating rigid programmatic gates, that evidence grounding bounds fabrication but permits misattribution which the pipeline cannot detect, and that the Critic occasionally failed to return a schema-valid object leaving verdicts unreviewed

### c153
**MetaOpenFOAM** — 02_tango/v0.2 · doi:10.2139/ssrn.4921381

the authors state MetaOpenFOAM cannot directly recognise data requiring secondary calculation such as Reynolds number, that for complex geometries and boundary conditions natural language inputs alone are insufficient so human participation is needed, and that similarity match may fail due to inaccurate user requirements or an inadequate database

### c154
**AutoB2G** — 02_tango/v0.2 · doi:10.48550/arxiv.2603.26005

the authors state the framework has so far been implemented and validated within a limited set of platforms primarily CityLearn V2, that the primary reason for failures lies in the high degree of coupling among cross-module dependencies, and that task descriptions often exhibit a certain degree of ambiguity

### c155
**AI CFD Scientist** — 02_tango/v0.2 · doi:10.48550/arxiv.2605.06607

the authors state all numbers use a single backbone, that no automated CFD-paper rubric scores these workflows so cross-framework comparison is manual, and they include an appendix titled What AI CFD Scientist Does Not Yet Do Well; they conclude the framework is supervised scientific assistance, not unattended publication

### c156
**Foam-Agent** — 02_tango/v0.2 · doi:10.48550/arxiv.2505.04997

the authors state that errors bypassing the FatalErrorIn macros - mpirun option errors, decomposePar configuration failures and bare floating-point-exception traces - fall outside the error extractor, that closed-loop geometry modification is left to an extension, and that the external-mesh pathway is scoped to the Gmsh format

### c157
**Xu2026-agentic-urban-digital-twins** — 02_tango/v0.2 · doi:10.1016/j.compenvurbsys.2026.102449

the authors list knowledge gaps and AI hallucination, limited data and tool access because many key tools are proprietary and do not comply with FAIR principles, lack of explainability, unclear accountability in autonomy, contextual memory limits for large simulation outputs, and risks of over-automation of critical services

### c158
**VASPilot** — 02_tango/v0.2 · doi:10.48550/arxiv.2508.07035

the authors state essentially no limitations, framing the gaps as extensions - capabilities can be readily extended through additional agents and tools, and the framework can be adapted to other DFT codes by deploying the corresponding MCP server

### c159
**IteraSim RAG** — 02_tango/v0.2 · arxiv:2607.20346

the authors state the reported 77.9% is a conservative lower bound on operational retrieval quality, that the scoring rule under-counts synonymous surface forms, that two under-covered cases are attributable to corpus-coverage gaps, that the benchmark does not exercise multi-physics regimes, and that executability-tier evidence is deferred to a companion technical note

### c160
**Agentic SWMM** — 02_tango/v0.2 · doi:10.31223/x5f47g

the authors state they only encapsulated the peak flows of interest, that a lumped model representation was used for demonstration purposes, that poor prompting can lead to variability in how non-expert users specify tasks, and that the interpretability of the results does not arise from the agentic AI itself or from the underlying LLM

### c161
**Jadhav2024-llm-fem-truss-designer** — 02_tango/v0.2 · doi:10.1080/09544828.2026.2624356

the authors state a notable limitation is difficulty producing floating-point values with high precision for continuous parameters such as nodal coordinates, that in the absence of explicit objective functions LLMs may converge slowly or terminate prematurely, and that LLMs are best positioned not as replacements for traditional optimizers but as a new class of reasoning-based design agents

### c162
**Jan2026-agentic-digital-twin-ATSC** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.27753

the authors state that operating in the wild raises concerns regarding variability and reliability of sensor data, communication delays in congested cities, and regulatory concerns over fully autonomous traffic signal control, and that future research will involve pilot testing and connection with real infrastructure APIs

### c163
**FoamPilot** — 02_tango/v0.2 · doi:10.48550/arxiv.2412.17146

the authors state a robust ability for optional human feedback was not achieved due to technical challenges with the chosen agentization framework, that asynchronous simulation running requiring state save and recovery was not addressed, and that the experiments considered only GPT-4o

### c164
**TO-Master** — 02_tango/v0.2 · arxiv:2607.01812

the authors state the ablation study is limited to six regular benchmark cases, that users may need to inspect the previewed supports, loads and passive domains before optimisation, that the system assumes a self-consistent unit system, and that broader industrial benchmarks and standardised quantitative metrics are needed

### c165
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1063/5.0257555

the authors state a measure of human oversight remains critical to ensure correctness, and that fluctuations in model performance over time mean users must carefully monitor updates for mission-critical or high-precision applications

### c166
**MatSciAgent** — 02_tango/v0.2 · doi:10.1038/s43246-025-00994-x

the authors state LLMs alone are inherently limited in delivering rigorous scientific predictions for complex physical phenomena, that one run failed to extract any material IDs suggesting an isolated error, and that broadening data sources and enabling the agent to write or adapt code would increase flexibility

### c167
**El Agente Quntur** — 02_tango/v0.2 · doi:10.48550/arxiv.2602.04850

the authors state that LLMs struggle with more complex geometry-related tasks, that the most significant limitation arises during geometry generation for transition-state searches, that geometric reasoning is currently a major bottleneck for AI agents in chemistry, and that in one case study most transition-state results are likely incorrect

### c168
**Aether** — 02_tango/v0.2 · arxiv:2604.18233

the authors state a small subset of challenging queries causes the majority of failures, that the test executor agent's main failure mode is misuse of network digital twin tool parameters, that ground truth creation requires iterative expert validation, and that guardrails and agent monitoring are next steps toward production-grade autonomy

### c169
**text2flowsheet** — 02_tango/v0.2 · doi:10.1039/d6dd00060f

the authors state the main limitation of digitizing flowsheets from textual descriptions is incomplete information about the chemicals, processing steps and operating conditions, and that a significant challenge is the propagation of errors from LLM-based digitization to the final Aspen simulation

### c170
**SwarmFoam** — 02_tango/v0.2 · doi:10.2139/ssrn.6074109

the authors state general-purpose LLMs still exhibit unreliability when constructing complex geometries and generating meshes, struggling with curved boundaries and unstructured grids, that configuration errors accounted for 71.1% and 44.9% of errors in the multimodal and natural-language tests, and that future work needs simulation validation criteria rather than judging correction need from log errors alone

### c171
**PDEFlow** — 02_tango/v0.2 · arxiv:2607.05134

the authors state that operator selection is still manual, that the solver backend is currently limited to one- and two-dimensional rectangular domains with linear PDEs, and that support for nonlinear PDEs would require nonlinear residual assembly

### c172
**TSAgent** — 02_tango/v0.2 · arxiv:2605.14154

the authors state LLM-based verification is not a physical guarantee and automated transition-state assignments accepted without human oversight could propagate errors into downstream mechanistic conclusions, that the workflow assumes reasonable reactant and product geometries are provided, and that the evaluation is restricted to 100 of the 600 available reactions

### c173
**Engineering.ai** — 02_tango/v0.2 · doi:10.48550/arxiv.2511.00122

the authors state that API rate limits highlight the mismatch between parallel computational workflows and sequential API processing, and that privacy and intellectual property concerns arise when transmitting proprietary design specifications to external APIs

### c174
**DREAMS** — 02_tango/v0.2 · doi:10.48550/arxiv.2507.14267

the authors report recurrent failures including loss of task history, disregard of convergence results, attempts to bypass tool refusals, incorrect arithmetic, reduced verification during extended executions and circumvention of provenance checks, including one case where an unsupported value was passed through the identity x+0 to produce a valid provenance record without validating the original value

### c175
**CFDagent** — 02_tango/v0.2 · doi:10.1063/5.0294696

the authors state the limited quality and controllability of the generated geometries hinder precision, and that performance is constrained by the inherent complexity of CFD simulations, leading to significantly prolonged processing times

### c176
**TopOptAgents** — 02_tango/v0.2 · arxiv:2605.23273

the authors state that less commonly documented formulations such as stress minimisation with constraint aggregation are handled by conditionally adding references to the runtime context, and that three-dimensional topology optimisation and integration with manufacturing process parameters remain open directions

### c177
**GENIUS** — 02_tango/v0.2 · doi:10.48550/arxiv.2512.06404

the authors state that improving the knowledge graph, particularly the connections and conditions, remains future work, and that the present knowledge graph covers only pw.x so extending it to other Quantum ESPRESSO modules and codes beyond QE would broaden reach

### c178
**MASTER** — 02_tango/v0.2 · doi:10.48550/arxiv.2512.13930

the authors state that in small fully enumerable spaces such as their adatom benchmark the implicit calibration is sufficient, but that in larger or less well-characterised domains an additional retrieval-augmented agent would be needed to supply prior grounding

### c179
**AtomisticSkills** — 02_tango/v0.2 · doi:10.48550/arxiv.2605.24002

the authors state the framework functions predominantly in a co-pilot modality where human researchers provide high-level directives, and that human supervision remains critical to guide the agent through complex multi-day scientific workflows

### c180
**AutoDFT** — 02_tango/v0.2 · arxiv:2605.26179

the authors state that closed-loop adaptation remains useful even when the initial planner is strong since several successful runs still depend on recovery or plan modification, and that the scope excludes energy above hull, advanced optical excitations, transport coefficients and full phonon dispersions

### c181
**Petkovic2025-raspa-multiagent** — 02_tango/v0.2 · doi:10.48550/arxiv.2509.10210

the authors state that knowledge is encoded procedurally in prompts and tools, limiting the ability of agents to adapt across tasks or refine strategies based on past experience

### c182
**Academy** — 02_tango/v0.2 · doi:10.1109/ipdps65963.2026.00114

the authors state that LLMs combined with tool calling cannot currently construct complex real-world science applications, with frequent problems including improperly configured or invoked codes that ran without errors but produced incorrect results, and that permissions are currently coarse-grained

### c183
**MOOSEnger** — 02_tango/v0.2 · doi:10.48550/arxiv.2608.15881

the authors state that closing the remaining gap in the harder categories is a natural next step, through category-specific retrieval, expanded skills and refined instructions

### c184
**Battery-Sim-Agent** — 02_tango/v0.2 · doi:10.1145/3770855.3818856

the authors state the agent behaviour is inherently probabilistic and tighter theoretical characterisation of convergence remains open, that classical Bayesian optimisation remains competitive in low-headroom chemistries, and that simulator edge cases remain difficult for all methods because the forward PyBaMM model itself becomes numerically unstable

### c185
**LARA-HPC** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.22571

the authors state the implementation realises the pipeline only up to the validation phase and that the critical review phase is not implemented end to end

### c186
**AutoSurrogate** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.11945

there is no limitations section; the authors note only that residual errors concentrate near the plume boundaries where the saturation field changes rapidly

### c187
**NAIS** — 02_tango/v0.2 · arxiv:2607.11084

the authors state it is a single-institution case study, that the GWAS results constitute replication evidence rather than novel discovery, that a dataset of this size is insufficient for clinical-grade validation of drug-induced liver injury prediction, and that comparison between agent-derived labels and expert phenotypes revealed systematic discordance

### c188
**MatClaw** — 02_tango/v0.2 · arxiv:2604.02688

the authors state the agent consistently struggles with what they term tacit domain knowledge, including appropriate simulation timescales, equilibration protocols and sampling adequacy for phase transitions

### c189
**pegasus-ai** — 02_tango/v0.2 · arxiv:2606.18425

the authors state the evaluation covers one application and one workflow management system, and that future work will apply the methodology to other scientific workflows, workflow systems and AI coding agents to assess generality

### c190
**Masgent** — 02_tango/v0.2 · arxiv:2512.23010

the authors state Masgent is intentionally designed to avoid autonomous decision-making in areas requiring physical judgment such as functional selection and convergence settings, that although it prepares complete workflows it does not execute VASP jobs or manage HPC queues, and that ambiguous prompts may still require user clarification

### c191
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1016/j.taml.2025.100623

the authors state that locally deployed smaller models such as QwQ-32B struggled with generating valid solver files for complex processes, that zero-shot prompting commonly failed in simulations with intricate settings even for large models, and that challenges with boundary conditions and solver keywords stress the requirement for expert supervision

### c192
**QUASAR** — 02_tango/v0.2 · doi:10.48550/arxiv.2602.00185

the authors state that performance is bounded by the underlying domain knowledge of the chosen model, that LLM-induced errors often present as structurally coherent but numerically or physically unsound outputs, that the system does not support agent-driven HPC job submission, and that non-determinism affects reproducibility

### c193
**El Agente Solido** — 02_tango/v0.2 · doi:10.48550/arxiv.2602.17886

the authors state future developments will focus on expanding methodological coverage to excited-state methods, explicit solvation and finite-field approaches, that PBE pseudopotentials systematically overestimate lattice constants, that the quasi-harmonic approximation does not capture magnon-phonon couplings, and that prior work rarely evaluated consistency and reproducibility across multiple trials

### c194
**MooseAgent** — 02_tango/v0.2 · doi:10.48550/arxiv.2504.08621

the authors report poor performance on plasticity at 60% success, that the LLM struggles selecting correct functions from the vast library, a lack of accuracy in MOOSE fundamentals such as function expressions and input card format, and the infinite-loop failure mode

### c195
**MDAgent** — 02_tango/v0.2 · doi:10.1038/s41598-025-92337-6

the authors state MDAgent is currently a semi-automated intelligent assistant because current local small-parameter LLMs are not yet sufficient to automatically run all complex codes

### c196
**FEABench** — 02_tango/v0.2 · doi:10.48550/arxiv.2504.06260

the authors state the benchmark is restricted to simpler geometries without CAD imports and to problems solving in under a minute, that the physics block is the hardest component, and that adding more human-verified problems would be valuable

### c197
**TritonDFT** — 02_tango/v0.2 · doi:10.48550/arxiv.2603.03372

the authors state performance degrades on more complex systems, particularly magnetic materials where all models exhibit pass rates below 6%, that the system is limited to Quantum ESPRESSO, and that band-gap extraction is problematic in smeared calculations

### c198
**MAPPS** — 02_tango/v0.2 · doi:10.48550/arxiv.2506.05616

the authors state MAPPS currently has a human expert in the loop and does not reach the fully autonomous Level 3, that it focuses on materials discovery with extensions to molecules and polymers underexplored, and that many LLMs consistently produce five-step workflows often including useless or redundant steps

### c199
**LQCDMaster** — 02_tango/v0.2 · doi:10.48550/arxiv.2607.15001

the authors state the benchmark covers representative but not exhaustive tasks, that executable code and static consistency checks are insufficient for validating baryon contraction logic so direct numerical regression against trusted references remains necessary, and that for new observable classes reference comparisons and human review remain essential

### c200
**MADE** — 02_tango/v0.2 · doi:10.48550/arxiv.2601.20996

the authors state current experiments rely on generators and machine-learned potentials trained on Materials Project data and thus inherit shared distributional biases that may simplify discovery relative to real-world settings, and that extending to DFT or experimental oracles and multi-objective tasks are natural next steps

### c201
**R-LAM** — 02_tango/v0.2 · doi:10.48550/arxiv.2601.09749

the authors state the evaluation is at small to moderate scale on representative workflows rather than large long-running pipelines, that it does not involve real laboratory hardware or cyber-physical systems, that the framework inherits the probabilistic limitations of its planning LLM, and that it assumes external tools behave deterministically

### c202
**Tan2026-aspen-reasoning-agent** — 02_tango/v0.2 · doi:10.1038/s44172-025-00583-3

the authors state the workflow was pre-defined in the prompts for this case study, that tackling problems exceeding token limits would require autonomous agentic task decomposition, that each run took around 4 hours, and that embodied equipment emissions are assumed negligible

### c203
**Laub2026-text2flowsheet-pipeline** — 02_tango/v0.2 · doi:10.69997/pse.120458

none stated - the record is a two-page extended abstract with no limitations or future-work text; the only qualifier offered is that potential simplifications necessary to achieve convergence are recorded transparently

### c204
**Sakhinana2024-rait** — 02_tango/v0.2 · doi:10.48550/arxiv.2408.15866

the authors state the proposed framework is effective but lags slightly behind the proprietary models, and name more diverse instruction-tuning datasets, a wider range of external tools and improved explainability as future work

### c205
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1016/j.ijheatfluidflow.2026.110399

the authors concede very little - the only qualifiers are conditional, that the 100% success rate holds when provided with well-formulated user queries under carefully designed system prompts, and that LLM-generated configuration files may occasionally contain errors; no dedicated limitations section exists

### c206
**Sedova2026-olcf-ai-coding-agents** — 02_tango/v0.2 · doi:10.20944/preprints202608.1323.v1

the authors state that the amount of work that must be verified grows with AI reliability, faithfulness and reproducibility problems and "in the case of HPC production workflows, can become unmanageable", that the file volume from even a short agent session "can rapidly become overwhelming for human verification", that language models produce coherent plausible explanations which "can lead to over confidence in their methods, summaries and outputs", that the results are platform-specific, and that faithful evidence and provenance requirements "are currently out of the scope of state-of-the-art tools"

### c207
**NL2FOAM** — 02_tango/v0.2 · doi:10.1016/j.taml.2025.100594

the authors state that while the method performs well for incompressible benchmarks, limitations remain for more complex simulations, and name multiphase flows, compressible flows and heat transfer as future work; failure analysis found most errors in turbulence simulations, caused by divergence from unreasonable parameter values such as dissipation rates set orders of magnitude too high

### c208
**OptMetaOpenFOAM** — 02_tango/v0.2 · doi:10.1016/j.taml.2026.100660

there is no limitations section. The only limitation stated in the authors' own terms is that the propagation distance is confined between 0 and 0.0707 by the physics of the case, so "owing to these inherent bounds, the fitted response surface is not perfect". The published version adds a bounded robustness claim rather than a limitation: "OptMetaOpenFOAM maintains nearly identical success rates when handling semantically equivalent but syntactically different inputs"

### c209
**OASiS** — 02_tango/v0.2 · doi:10.5281/zenodo.20543501

the repository documents failures per test rather than a limitations section: deal.II test 3 needed five iterations for correct C++ and hit six API and mesh incompatibilities, the 4C test first produced a silently failing variable resolution with velocities thirty times too low and an MPI_ABORT that swallowed error messages, FEBio is listed as unavailable because it needs a binary, and contributors are warned off benchmark-specific parameter databases and model-specific templates as fine-tuning

### c210
**M.A.R.V.I.N.** — 02_tango/v0.2 · doi:10.5281/zenodo.19835550

the authors state that the ESPEI assessment is ongoing, that the conductivity estimate "is a calibrated consistency check rather than a blind prediction", that the atmosphere diagram is a ternary proxy rather than a full multicomponent garnet calculation, that the Nernst-Einstein model is a dilute-solution approximation applied outside its strict domain of validity to a system with around 40% octahedral vacancies, that the kawin precipitation module "cannot be exercised for LLZO", and that equilibrium phase stability is "a necessary but not sufficient condition for synthesis prediction"

### c211
**CFDLLMBench** — 02_tango/v0.2 · doi:10.48550/arxiv.2509.20374

the authors state that establishing appropriate human references "is non-trivial because performance depends strongly on the evaluator's domain knowledge and experience", that formal human baselines remain future work, that "the lack of spatial reasoning capabilities in LLMs appears to produce an incorrect geometry and mesh" and that geometry understanding "is a major area in need of improvement", and that models "often fail to fully understand the prompts and lack domain-specific reasoning"

### c212
**ChatCFD** — 02_tango/v0.2 · doi:10.1002/aidi.202500174

the authors state that language models "excel at high-level linguistic narration but consistently struggle to enforce the complete chain of physical constraints within the generated executable code", that "reflections beyond 75% of the limit (approximately 22 iterations) often fail to resolve remaining errors", that all agents show lower success rates in combustion and multiphase flow, that DeepSeek-R1 hallucinations such as spurious Markdown formatting persist despite prompt engineering and structured outputs, and that mesh support is limited to Fluent meshes and existing polyMesh directories

### c213
**URSA LAMMPS agent** — 02_tango/v0.2 · doi:10.48550/arxiv.2607.22596

the authors state that the agent could not reproduce the generalized stacking fault energy calculation from a minimal prompt, that the thermal-expansion run covered only part of the temperature range because the range was not specified in the prompt, that a melting-temperature discrepancy was attributable to "the lack of the LLM's knowledge about the two-phase method", and that protocols "can vary substantially across agentic frameworks, even when pursuing the same scientific objective", underscoring the need for benchmarks evaluating both predictions and workflows

### c214
**NeuroClaw** — 02_tango/v0.2 · arxiv:2604.24696

the authors state the work "does not claim state-of-the-art performance or present exhaustive cross-system leaderboards", that they "do not evaluate model quality for clinical outcomes or make regulatory claims", that the tasks "represent only a subset of real-world neuroimaging complexity", that the protocol "may underestimate the effect of skill usage in real deployments", and that cautious reasoning "can be partially penalized by the judge as extraneous to the narrow task requirement", so the gains "should therefore be interpreted conservatively"

### c215
**CatDT** — 02_tango/v0.2 · arxiv:2606.05050

the authors state that predicted propylene selectivity "underestimates experiment because the multi-path KMC is not yet coupled to UniMech's Sabatier gating, an integration left to follow-on work", that residual barrier offsets are "a residual attributable to the UMA-DFT methodological difference", that a kinetic dissection and synthesis-feasibility assessment of the leading candidates "lies outside the scope of the present infrastructure paper", and that machine-learned-potential backends still require separate training per target system

### c216
**Xiao2026-openfoam-coding-agent** — 02_tango/v0.2 · arxiv:2602.11689

the authors state that errors requiring "a deeper understanding of the underlying physics, which the agent currently lacks" are more challenging, so "human oversight remains essential", that "agent performance degrades as geometric complexity and physical stiffness increase", that extending to complex three-dimensional or industrial workflows "will require careful investigation and development", and that mesh quality is "largely determined by the LLM model itself"

### c217
**Corridor** — 02_tango/v0.2 · doi:10.5281/zenodo.22554152

the authors state the defect taxonomy "is seeded from defects actually encountered during development, not a comprehensive catalog", that every reported score "is a single-channel measurement; it is not a whole-model validation claim", that the verification gate "checks aggregate energy-balance and mass-added figures at the final solved cycle rather than the full time history", so "a transient event that self-resolves by the final cycle would pass the gate" and "hourglass energy is not currently checked", that API spend "is gated per call rather than per session", that escalation messages go to stdout rather than a machine-readable channel, and that the analyst agent "does not perform further investigation on its own"

### c218
**DDA** — 02_tango/v0.2 · doi:10.3389/fchem.2026.1914886

the authors state the benchmark "uses reference-ligand-derived centers and computational proxy metrics" so "experimental binding, activity, selectivity, pharmacokinetic, and safety studies remain necessary before biological or clinical conclusions can be drawn", that the improvement "mainly comes from framework-level completion and filtering strategies rather than performance breakthroughs in the underlying generation model itself", that DDA "does not dominate every individual molecular descriptor", that the recovery outcomes "are assessments of recovery-plan quality under controlled declared states, not physical re-execution", and that a same-tool generic-agent baseline "will be an important future experiment"

### c219
**LLeM** — 02_tango/v0.2 · doi:10.1109/access.2025.3605803

the authors state that "the current model accuracy degrades above 1 GHz due to simplified geometric assumptions in the HFSS model" and that fixing it "will require implementing adaptive mesh refinement strategies and more sophisticated port modeling techniques"; that "the lumped RLC topology used in the paper is chosen as a proof of concept" and "The accuracy of more complex equivalent circuit topologies should be validated by measurements in an extended frequency range"; and that "the system currently relies on predefined geometric templates for QFN packages", so it performs "parameter optimization within fixed topologies" rather than "true design exploration". On the retrieval evaluation they add that "a more comprehensive evaluation procedure can be developed for deeper assessment"

### c220
**Grid-Mind** — 02_tango/v0.2 · arxiv:2602.20683

the authors state that the transient and electromagnetic-transient acceptance criteria "are screening-oriented heuristics ... and do not constitute a replacement for utility-approved dynamic acceptance protocols", that "the evaluation does not yet constitute a blinded third-party benchmark", that "end-to-end numerical correctness validation against authoritative utility-grade reference studies ... has not yet been conducted", that the contingency threshold "is an implementation-specific parameter", that "the current mitigation action space is limited to shunt-like reactive compensation interventions", that "rigid pattern matching may fail to detect paraphrased or embedded numerical claims", and that memory may saturate the context window

### c221
**Aspen-MCP** — 02_tango/v0.2 · title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi

the repository states that "the 14B cannot write a single working script in the 20-task suite (0/19 in the definitive run); the 32B manages 3-4/19", that "the precise limitation is *global spec correctness*, not 'ignores errors'", that one design task "is NOT auto-scorable - its expected (0.5) is the target stated in the prompt, so the model scored a false PASS", that semantic correctness is measured only on the simulator side, that "Aspen COM does not initialize over SSH", that the reported means come from small suites, and that "reliability costs tokens, not time"

### c222
**MCP Solver** — 02_tango/v0.2 · title:mcpsolvermodelcontextprotocolserverforconstraintsolvingsatmaxsatsmtcpaspdp

the repository states that "v4 is not yet installable from PyPI" because the package name is held by a third-party upload of stale code and a name-transfer request is pending, and that the MiniZinc mode from the previous version is retired; no accuracy or failure-mode limitations are stated

### c223
**Onishi2026-reservoir-simulation-assistant** — 02_tango/v0.2 · title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving

none stated; the nearest qualifications are framing rather than limitation - that the assistant "is designed to augment, not replace, the established tools of the trade", and that integrating these capabilities into industry-standard high-fidelity platforms "represents an exciting evolution for the subsurface digital ecosystem"

### c224
**Zhang2025-llm-planning-bem-workflow** — 02_tango/v0.2 · title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow

the authors state that "each case study begins with the assumption that the model geometry is already established", that "only HVAC templates were utilized", that "there is a lack of user interaction; the current model operates without further engagement with the user", that "a more comprehensive validation approach across more diverse buildings, modeling cases, and input scenarios would be needed", that "data privacy concerns must be addressed when employing commercial LLMs", that they "focused on two common error examples", and that "the Gemini model fails to successfully operate Agent 3, specifically in generating single objects correctly"

### c225
**Agents4GEOS** — 02_tango/v0.2 · arxiv:2607.18557

the authors state that "meshing complex reservoirs is particularly challenging and warrants a dedicated specialized agent", that "more robust skill coverage is needed to ensure all simulations complete correctly", that "interacting with running simulations - monitoring convergence, diagnosing stalls, and steering or restarting runs mid-execution - remains an open direction", and that "token usage has emerged as a meaningful factor in the overall budget"; within the session they also record that the injection-rate tension "remains unreconciled in the sources", that the relative permeability "is an endpoint fit rather than the raw published curve", and that the saturation maps "used a density-based proxy"

### c226
**EnergyPlus-MCP** — 02_tango/v0.2 · doi:10.1016/j.softx.2025.102367

the authors state that "the current tool set focuses on model analysis and modification rather than complete model creation from scratch", that "the quality of AI-driven interactions heavily rely on the capabilities of the MCP client and the user's ability to formulate appropriate queries", that "users still need sufficient BEM knowledge to validate results", that "the protocol communication layer introduces minor computational overhead compared to direct EnergyPlus usage", and that "the server inherits any limitations present in the underlying EnergyPlus simulation engine"

### c227
**Eppy-LLM** — 02_tango/v0.2 · doi:10.26868/30680611.2026.1305

the authors state that "the workflow depends on a pre-existing baseline IDF, assuming that building geometry and HVAC topology are already defined", which "restricts applicability in early-stage design", that the rule-based editor "may encounter parsing inefficiencies when applied to large commercial buildings with nested zones or intricate control sequences", that "semantic ambiguity in natural-language prompts can influence LLM interpretation", that "the current scope of evaluation metrics is limited to energy and comfort indicators", and that "minor variability can occur in the ordering of lower-ranked parameters across repeated runs"

### c228
**Chen2026-mcp-bem-paradigms** — 02_tango/v0.2 · doi:10.1080/19401493.2026.2653969

the authors state that "this work represents an early exploration rather than a production-ready solution", that the demonstrations "employed a relatively simple residential model with three thermal zones and ideal loads" so complex models "may pose different challenges that this study does not address", that language models "can produce incorrect tool invocations, misinterpret user intent, or generate plausible but inaccurate explanations", that with many tools available "the model may select inappropriate tools or become confused by overlapping functionalities, and LLM non-determinism means identical prompts may yield different tool sequences across sessions", and that "token consumption and API latency accumulate across extended sessions, making scripted approaches potentially more efficient for large-scale parametric studies"

### c229
**GPT+MCP framework** — 02_tango/v0.2 · doi:10.3390/buildings15173190

the authors state the system relies on "pre-trained knowledge and the specific prompt it receives", that it has no "built-in ability to verify whether the predicted values align with physical laws unless such checks are explicitly added", that response times are unsuitable for larger studies, and that it depends on a commercial model accessed through a proprietary black-box API

### c230
**EngiAI** — 02_tango/v0.2 · doi:10.3929/ethz-c-000801434

the authors state the benchmark problems "are limited to Beams2D and Photonics2D", that "only four LLM backends were tested, primarily due to API cost constraints", that the cluster training benchmark "covers only two generative models ... and two cloud LLM backends", that a user study with practising engineers was omitted, and that no single-agent baseline with identical tool access was run

### c231
**PetroGraph** — 02_tango/v0.2 · doi:10.48550/arxiv.2605.15028

the authors state that "future work should focus on enhancing the RAG system to cover more nuanced simulator behaviour, implementing long-term memory for iterative multi-stage history matching, and refining the agent graph architecture to accommodate alternative workflows"

### c232
**Carbonati2026-multi-agent-llm-acquisition** — 02_tango/v0.2 · doi:10.25417/uic.32994011.v1

the authors state that language models exhibit "erratic search dynamics in continuous spaces" and a "pronounced dependence on initial prompt configurations", that the method "fails to achieve the fine-grained numerical refinement required" on smooth landscapes, and that single metric pairs are insufficient for complex objectives

### c233
**GAGAW** — 02_tango/v0.2 · doi:10.1016/j.bdes.2026.100042

the author states that the fusion example "uses a sequential, structure-constrained inversion, while other joint or coupled inversion methods are not yet integrated", that "geophysics coverage is narrow, centered on ERT, seismic refraction, and basic climate linkage", that "the current uncertainty quantification propagates only petrophysical parameter uncertainty" so "survey errors, including electrode position uncertainty, reciprocal measurement errors, and temperature drift, are not yet incorporated", that "LLM hallucinations pose risks without stricter schema validation, tests, and version pinning", that "climate-resistivity links are correlational without modeling", and that "GAGAW is designed to augment, not replace, geophysical expertise"

### c234
**Aspen-MCP** — 02_tango/v0.2 · doi:10.26434/chemrxiv.15006587/v1

the authors state that "The interface currently targets steady-state simulation, and the definition of components and reacting systems relies in part on workarounds for limitations of the underlying automation interface"; that "The empirical evaluation is likewise centered on a single family of open-weight models and a set of representative - but not exhaustive - flowsheets, so its quantitative conclusions should be read as indicative of the achievable reliability gains rather than as universal bounds"; that "the tool layer does not yet cover every Aspen Plus unit-operation model"; and that they did not test the middle ground of "letting the agent write code that calls the same tested functions"

### c235
**TanabeSugano** — 02_tango/v0.2 · doi:10.26434/chemrxiv.15007941/v1

the authors state the implementation "does not aim to supplant the rigor inherent in ab initio methods and remains fundamentally distinct from it"

### c236
**Vriza2025-multi-agentic-atomistic-simulations** — 02_tango/v0.2 · doi:10.1039/d5dd00435g

the authors state that "dependency management and environment reproducibility, especially for tools like LAMMPS, Atomsk, and Phonopy, can become brittle across platforms or HPC systems"; that "the trustworthiness and explainability of some AI-driven actions, particularly LLM-based reasoning, remain open challenges"; and that "accuracy vs. automation trade-offs become critical for complex tasks such as phonon dispersion, thermal conductivity, or defect energetics". They also exclude potential choice from the agent's account: "the agent should not be held responsible for errors originating from the underlying potential choice"

### c237
**Geo2UBEM** — 02_tango/v0.2 · doi:10.2139/ssrn.7333555

the authors list seven, among them that "Six buildings in a single climate zone (CZ5A) constrain statistical representativeness"; that "Ideal-loads systems reduce modelling uncertainty but suppress equipment-level dynamics"; that "LLM reasoning is externally hosted and cannot be fully reproduced across model versions"; and that "Hardware scalability is extrapolated beyond the observed workload" - projecting six-building parallelism linearly "has not been validated at larger scale". They also name "upstream geometry quality control and reproducible pipeline orchestration" as "the two most manual components in the current workflow"


## claim-gap — 54

### c105
**Fortran-to-Devito** — 01_landscape/v0.5 · arxiv:2601.18381

Evaluation demonstrates M1; the source asserts: "the incorporation of feedback mechanisms motivated by reinforcement learning, enabling a transition from static code translation toward dynamic and adaptive analytical behavior"

### c106
**guo2026-slope-reliability-agents** — 01_landscape/v0.5 · doi:10.1016/j.aei.2026.105065

Evaluation demonstrates M1; the source asserts: "The feasibility and accuracy of this framework have been validated across realistic scenarios of varying complexity."

### c107
**GAIA** — 01_landscape/v0.5 · doi:10.48550/arxiv.2511.03852

Evaluation demonstrates M1; the source asserts: "the pioneering effort in building an agentic AI system for geothermal project assistance and a pioneering application of agentic RAG workflows in geothermal field development"

### c108
**TREMORS** — 01_landscape/v0.5 · doi:10.48550/arxiv.2609.01777

Evaluation demonstrates M1; the source asserts: "an advancement in observational seismology for data acquisition and a blueprint for reproducible multi-step data procurement and analyses across multiple repositories"

### c109
**Youwai2026-foundation-router** — 01_landscape/v0.5 · doi:10.1007/s43503-026-00088-8

Evaluation demonstrates M1; the source asserts: "a promising approach for foundation design automation, with a methodological foundation for future research in AI-assisted geotechnical engineering"

### c110
**kanfar2025-seismic-assistant** — 01_landscape/v0.5 · doi:10.1190/tle44020142.1

Evaluation demonstrates M1; the source asserts: "The AI assistant developed in this work demonstrates the practical application of LLMs in automating seismic data processing workflows."

### c111
**geo-drill-extractor** — 01_landscape/v0.5 · doi:10.1038/s41598-026-61824-9

Evaluation demonstrates M1; the source asserts: "the pipeline can extract entities, parse locations, and generate executable coordinates for downstream inspection"

### c112
**Sim2Schedule** — 01_landscape/v0.5 · doi:10.48550/arxiv.2606.10286

Evaluation demonstrates M1; the source asserts: "a practical and scalable alternative to classical optimization for long-horizon industrial scheduling; the simulator is claimed as 'the first of its kind to be integrated with LLM agents'"

### c113
**xu2025-multi-geollm** — 01_landscape/v0.5 · doi:10.1016/j.autcon.2025.106257

Evaluation demonstrates M1; the source asserts: "This framework can significantly reduce the repetitive mechanical operations performed by engineers in geotechnical design."

### c114
**Geo-Resource Agent** — 01_landscape/v0.5 · doi:10.56952/igs-2025-0391

Evaluation demonstrates M1; the source asserts: "Case studies demonstrate transparent reasoning, reduced manual scripting, and scalable automation for subsurface engineering workflows."

### c115
**specfem-mcp** — 01_landscape/v0.5 · doi:10.48550/arxiv.2512.14429

Evaluation demonstrates M1; the source asserts: "the first application of MCP technology to computational seismology, significantly lowering the entry barrier and enhancing reproducibility"

### c116
**MINDS** — 01_landscape/v0.5 · doi:10.3390/mining6020026

Evaluation demonstrates M1; the source asserts: "MINDS can systematize economic scenario analysis without sacrificing governance and verification required for definitive feasibility studies"

### c117
**AutoSurrogate** — 01_landscape/v0.5 · doi:10.1016/j.aei.2026.105058

Evaluation demonstrates M1; the source asserts: "autonomous language-driven surrogate construction is a viable approach for realistic subsurface flow applications and a practical pathway toward lowering the expertise barrier"

### c118
**GeoMCP** — 01_landscape/v0.5 · doi:10.48550/arxiv.2603.01022

Evaluation demonstrates M1; the source asserts: "a blueprint for transitioning the industry from isolated legacy software to an interoperable, AI-ready ecosystem where engineers can leverage modern AI without surrendering professional responsibility"

### c258
**SimAgent** — 02_tango/v0.2 · doi:10.1145/3731599.3767349

Evaluation demonstrates M1; the source asserts: "Our implementation enables the LLM agent to access any computing resource with a compatible Parsl configuration."

### c259
**PDE-Agents** — 02_tango/v0.2 · doi:10.48550/arxiv.2606.07850

Evaluation demonstrates M1; the source asserts: "demonstration of production-grade reliability for the full agent stack"

### c260
**APS-Agent** — 02_tango/v0.2 · doi:10.1016/j.dche.2026.100312

Evaluation demonstrates M1; the source asserts: "the framework's capabilities in analysis, optimization, and guided construction suggest LLM-based agents can become valuable collaborators"

### c261
**DynaMate2** — 02_tango/v0.2 · doi:10.48550/arxiv.2605.20819

Evaluation demonstrates M1; the source asserts: "DynaMate2 offers a template rather than a finished product"

### c262
**aihydro-tools** — 02_tango/v0.2 · doi:10.5281/zenodo.19597589

Evaluation demonstrates M1; the source asserts: "reproducibility should be structural, not post-hoc"

### c263
**Schafer2026-chemasim-process-agent** — 02_tango/v0.2 · doi:10.48550/arxiv.2603.12813

Evaluation demonstrates M1; the source asserts: "In all cases, the process development agent is able to design reasonable process flowsheets based solely on the analysis of thermodynamic behavior"

### c264
**WARA** — 02_tango/v0.2 · doi:10.48550/arxiv.2608.14573

Evaluation demonstrates M1; the source asserts: "WARA can already construct a clearer optimization research structure"

### c265
**GAIA** — 02_tango/v0.2 · doi:10.48550/arxiv.2511.03852

Evaluation demonstrates M1; the source asserts: "GAIA represents a pioneering application of agentic RAG workflows in geothermal field development."

### c266
**Xu2026-agentic-urban-digital-twins** — 02_tango/v0.2 · doi:10.1016/j.compenvurbsys.2026.102449

Evaluation demonstrates M0; the source asserts: "agentic digital twins have the potential to evolve into a central operating system for smart cities"

### c267
**VASPilot** — 02_tango/v0.2 · doi:10.48550/arxiv.2508.07035

Evaluation demonstrates M1; the source asserts: "an open-source platform that fully automates VASP workflows"

### c268
**Jadhav2024-llm-fem-truss-designer** — 02_tango/v0.2 · doi:10.1080/09544828.2026.2624356

Evaluation demonstrates M1; the source asserts: "These results highlight the promise of LLM agents to function as a new class of natural language-based, reasoning-driven optimizers"

### c269
**Jan2026-agentic-digital-twin-ATSC** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.27753

Evaluation demonstrates M1; the source asserts: "The present work uniquely combines all three components - digital twin, agentic AI with LLM-driven reasoning, and MCP-secured action execution - into a unified, compile-ready operational framework."

### c270
**FoamPilot** — 02_tango/v0.2 · doi:10.48550/arxiv.2412.17146

Evaluation demonstrates M1; the source asserts: "proof-of-concept"

### c271
**TO-Master** — 02_tango/v0.2 · arxiv:2607.01812

Evaluation demonstrates M1; the source asserts: "TO-Master removes the burden of trivial setup and routine model construction, lowers the modeling barrier of TO, and preserves a reliable numerical workflow."

### c272
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1063/5.0257555

Evaluation demonstrates M1; the source asserts: "our results underscore the agent's potential to significantly streamline or even automate advanced CFD tasks with minimal human input"

### c273
**MatSciAgent** — 02_tango/v0.2 · doi:10.1038/s43246-025-00994-x

Evaluation demonstrates M1; the source asserts: "the system shows the stability required for materials research"

### c274
**SwarmFoam** — 02_tango/v0.2 · doi:10.2139/ssrn.6074109

Evaluation demonstrates M1; the source asserts: "successfully realizing intelligent CFD proxy"

### c275
**PDEFlow** — 02_tango/v0.2 · arxiv:2607.05134

Evaluation demonstrates M1; the source asserts: "The framework is designed for repeatable scientific and engineering workflows where many related physics configurations must be specified, simulated, learned, and queried with minimal manual intervent"

### c276
**Engineering.ai** — 02_tango/v0.2 · doi:10.48550/arxiv.2511.00122

Evaluation demonstrates M1; the source asserts: "This work demonstrates that agentic-AI-enabled AI engineers have the potential to perform complex engineering tasks autonomously."

### c277
**CFDagent** — 02_tango/v0.2 · doi:10.1063/5.0294696

Evaluation demonstrates M1; the source asserts: "Through extensive tests on canonical and realistic scenarios, we demonstrate the robustness, versatility, and practical applicability of CFDagent."

### c278
**TopOptAgents** — 02_tango/v0.2 · arxiv:2605.23273

Evaluation demonstrates M1; the source asserts: "In such cases, the proposed framework reliably produces converged designs where a single state-of-the-art LLM struggles."

### c279
**MASTER** — 02_tango/v0.2 · doi:10.48550/arxiv.2512.13930

Evaluation demonstrates M1; the source asserts: "multi-agent collaboration accelerates materials discovery and marks a new paradigm for autonomous scientific exploration"

### c280
**Petkovic2025-raspa-multiagent** — 02_tango/v0.2 · doi:10.48550/arxiv.2509.10210

Evaluation demonstrates M1; the source asserts: "highlighting this approach's potential to enable fully autonomous, scalable materials characterization"

### c281
**LARA-HPC** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.22571

Evaluation demonstrates M1; the source asserts: "The results show that validation-driven generation significantly improves robustness and enables iterative correction of both syntactic and physical inconsistencies."

### c282
**AutoSurrogate** — 02_tango/v0.2 · doi:10.48550/arxiv.2604.11945

Evaluation demonstrates M1; the source asserts: "the proposed framework establishes a new paradigm for surrogate modeling, shifting from manual and heuristic workflows to automated, scalable, and intelligent model construction"

### c283
**MatClaw** — 02_tango/v0.2 · arxiv:2604.02688

Evaluation demonstrates M1; the source asserts: "LLMs already handle code generation and scientific interpretation reliably, and the rapid improvement in their capabilities will accelerate materials discovery"

### c284
**Masgent** — 02_tango/v0.2 · arxiv:2512.23010

Evaluation demonstrates M1; the source asserts: "positioning it as a next-generation computational assistant capable of accelerating both exploratory and production-level materials simulations"

### c285
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1016/j.taml.2025.100623

Evaluation demonstrates M1; the source asserts: "the framework adeptly handles a range of flow configurations (including single- and multi-phase flow) in just a few iterations"

### c286
**El Agente Solido** — 02_tango/v0.2 · doi:10.48550/arxiv.2602.17886

Evaluation demonstrates M1; the source asserts: "El Agente Solido exemplifies a rapid shift toward agentic computational chemistry"

### c287
**MooseAgent** — 02_tango/v0.2 · doi:10.48550/arxiv.2504.08621

Evaluation demonstrates M1; the source asserts: "MooseAgent can largely automate the simulation process"

### c288
**MDAgent** — 02_tango/v0.2 · doi:10.1038/s41598-025-92337-6

Evaluation demonstrates M1; the source asserts: "MDAgent can effectively assist experts in semi-automating domain-specific tasks, serving as a valuable support tool."

### c289
**R-LAM** — 02_tango/v0.2 · doi:10.48550/arxiv.2601.09749

Evaluation demonstrates M1; the source asserts: "This work does not claim autonomous scientific discovery or fully automated research. The framework is designed to assist, not replace, human scientific judgment."

### c290
**Tan2026-aspen-reasoning-agent** — 02_tango/v0.2 · doi:10.1038/s44172-025-00583-3

Evaluation demonstrates M1; the source asserts: "The developed agent served as a prototype that successfully integrated reasoning with the Reasoning-Acting framework, with its current efficacy being shaped by both prompts and selection of LLMs."

### c291
**Laub2026-text2flowsheet-pipeline** — 02_tango/v0.2 · doi:10.69997/pse.120458

Evaluation demonstrates M1; the source asserts: "We show that our integrated pipelines can faithfully collect and digitize chemical process information"

### c292
**Sakhinana2024-rait** — 02_tango/v0.2 · doi:10.48550/arxiv.2408.15866

Evaluation demonstrates M1; the source asserts: "our framework matches the performance of large-scale proprietary models on benchmark datasets, proving its effectiveness and usability"

### c293
**OpenFOAMGPT** — 02_tango/v0.2 · doi:10.1016/j.ijheatfluidflow.2026.110399

Evaluation demonstrates M1; the source asserts: "Rigorous trustworthiness verification confirms that properly designed multi-agent systems can achieve the reliability standards necessary for zero-tolerance scientific computing applications while sig"

### c294
**M.A.R.V.I.N.** — 02_tango/v0.2 · doi:10.5281/zenodo.19835550

Evaluation demonstrates M0; the source asserts: "M.A.R.V.I.N. provides generalizable, software-led architecture for reproducible materials discovery."

### c295
**EnergyPlus-MCP** — 02_tango/v0.2 · doi:10.1016/j.softx.2025.102367

Evaluation demonstrates M1; the source asserts: "This paper introduced EnergyPlus-MCP, the first novel and open-source Model Context Protocol server for EnergyPlus building energy simulation."

### c296
**GPT+MCP framework** — 02_tango/v0.2 · doi:10.3390/buildings15173190

Evaluation demonstrates M1; the source asserts: "the abstract states the approach reaches "accuracy for key structural parameters, with deviations under 1.5% compared to reference" solutions - a figure three of the eight max-displacement entries in "

### c297
**Vriza2025-multi-agentic-atomistic-simulations** — 02_tango/v0.2 · doi:10.1039/d5dd00435g

Evaluation demonstrates M1; the source asserts: "our system successfully reproduced both static properties (lattice constants, cohesive energies, elastic constants, phonon dispersion) and dynamic properties (melting points) across a diverse set of e"


## empty-category — 1

### c119
**inversion** — 01_landscape/v0.5 · papers.csv · 0/2

Subfield `inversion` has 2 admitted sources and none deep-read, so nothing in it is characterised beyond an abstract.


## evaluation-hole — 8

### c101
**baseline** — 01_landscape/v0.5 · papers.csv (tier core) · 6/41

6 of 41 deep-read systems compared against no baseline.

### c102
**held_out** — 01_landscape/v0.5 · papers.csv (tier core) · 30/41

30 of 41 deep-read systems report no held-out evaluation.

### c103
**data_type** — 01_landscape/v0.5 · papers.csv (tier core) · 9/41

9 of 41 deep-read systems were evaluated on synthetic data only.

### c104
**maturity_ceiling** — 01_landscape/v0.5 · papers.csv (tier core) · 14/41

14 of 41 deep-read systems demonstrate M1 or below; 14 reach M3 or above.

### c254
**baseline** — 02_tango/v0.2 · papers.csv (tier core) · 12/101

12 of 101 deep-read systems compared against no baseline.

### c255
**held_out** — 02_tango/v0.2 · papers.csv (tier core) · 79/101

79 of 101 deep-read systems report no held-out evaluation.

### c256
**data_type** — 02_tango/v0.2 · papers.csv (tier core) · 29/101

29 of 101 deep-read systems were evaluated on synthetic data only.

### c257
**maturity_ceiling** — 02_tango/v0.2 · papers.csv (tier core) · 41/101

41 of 101 deep-read systems demonstrate M1 or below; 12 reach M3 or above.


## evidence-hole — 19

### c091
**base_model** — 01_landscape/v0.5 · papers.csv · 105/151

105 of 151 admitted sources state nothing for `base_model`.

### c092
**tools_used** — 01_landscape/v0.5 · papers.csv · 52/151

52 of 151 admitted sources state nothing for `tools_used`.

### c093
**evaluation_method** — 01_landscape/v0.5 · papers.csv · 40/151

40 of 151 admitted sources state nothing for `evaluation_method`.

### c094
**baseline** — 01_landscape/v0.5 · papers.csv · 84/151

84 of 151 admitted sources state nothing for `baseline`.

### c095
**held_out** — 01_landscape/v0.5 · papers.csv · 134/151

134 of 151 admitted sources state nothing for `held_out`.

### c096
**data_type** — 01_landscape/v0.5 · papers.csv · 56/151

56 of 151 admitted sources state nothing for `data_type`.

### c097
**reported_result** — 01_landscape/v0.5 · papers.csv · 79/151

79 of 151 admitted sources state nothing for `reported_result`.

### c098
**maturity_claimed** — 01_landscape/v0.5 · papers.csv · 3/151

3 of 151 admitted sources state nothing for `maturity_claimed`.

### c099
**author_stated_limitations** — 01_landscape/v0.5 · papers.csv · 63/151

63 of 151 admitted sources state nothing for `author_stated_limitations`.

### c100
**code_availability** — 01_landscape/v0.5 · papers.csv · 127/151

127 of 151 admitted sources state nothing for `code_availability`.

### c245
**base_model** — 02_tango/v0.2 · papers.csv · 79/183

79 of 183 admitted sources state nothing for `base_model`.

### c246
**tools_used** — 02_tango/v0.2 · papers.csv · 1/183

1 of 183 admitted sources state nothing for `tools_used`.

### c247
**baseline** — 02_tango/v0.2 · papers.csv · 47/183

47 of 183 admitted sources state nothing for `baseline`.

### c248
**held_out** — 02_tango/v0.2 · papers.csv · 110/183

110 of 183 admitted sources state nothing for `held_out`.

### c249
**data_type** — 02_tango/v0.2 · papers.csv · 69/183

69 of 183 admitted sources state nothing for `data_type`.

### c250
**reported_result** — 02_tango/v0.2 · papers.csv · 62/183

62 of 183 admitted sources state nothing for `reported_result`.

### c251
**maturity_claimed** — 02_tango/v0.2 · papers.csv · 25/183

25 of 183 admitted sources state nothing for `maturity_claimed`.

### c252
**author_stated_limitations** — 02_tango/v0.2 · papers.csv · 66/183

66 of 183 admitted sources state nothing for `author_stated_limitations`.

### c253
**code_availability** — 02_tango/v0.2 · papers.csv · 110/183

110 of 183 admitted sources state nothing for `code_availability`.


## unread-source — 33

### c120
**abstract_only** — 01_landscape/v0.5 · papers.csv · 110/151

110 of 151 admitted sources were never read beyond an abstract, so nothing in them contributes to any characterisation.

### c298
**abstract_only** — 02_tango/v0.2 · papers.csv · 82/183

82 of 183 admitted sources were never read beyond an abstract, so nothing in them contributes to any characterisation.

### c299
**doi:10.2118/229629-ms** — 02_tango/v0.2 · paywalled.md

core write-up; it is one of very few sources whose stated subject is an agent orchestrating sampling, simulator execution and adaptive surrogate retraining together, so it bears on `surrogate-modelling`, `optimisation-loop` and `hpc-scale-out` at once. Abstract-only forces `not stated (abstract only)` maturity

### c300
**doi:10.2118/229905-ms** — 02_tango/v0.2 · paywalled.md

core write-up; the abstract names simulation model compliance and well placement optimisation but not what engine is driven or how, which is exactly the `what_it_drives` and `interface` evidence the run is thinnest on

### c301
**doi:10.2118/232332-ms** — 02_tango/v0.2 · paywalled.md

core write-up; one of only a handful of admitted sources combining `surrogate-modelling`, `optimisation-loop`, `uncertainty-quantification` and `techno-economic` in one system

### c302
**doi:10.2118/230773-ms** — 02_tango/v0.2 · paywalled.md

nothing for the touchpoint grid — it is a high-level evaluation, already `context`. Reading it would firm up the periphery/`context` boundary in section 08 and nothing else

### c303
**doi:10.1063/5.0330986** — 02_tango/v0.2 · paywalled.md

core write-up; the abstract states an automated LLM workflow drives large-scale parametric CFD, which would be direct `config-generation` plus `hpc-scale-out` evidence with a named engine

### c304
**doi:10.1109/tii.2026.3669495** — 02_tango/v0.2 · paywalled.md

core write-up; Abaqus is named in the title, so `what_it_drives` is already known, but the evaluation, the autonomy rating and the hallucination-handling the abstract gestures at are not

### c305
**doi:10.1109/icept67137.2025.11157286** — 02_tango/v0.2 · paywalled.md

core write-up; mesh refinement is a `solver-control` surface that few admitted sources touch, and the abstract does not say what mesher or solver is driven

### c306
**doi:10.1109/e-cargo65996.2025.11139170** — 02_tango/v0.2 · paywalled.md

nothing — a review, already `context`

### c307
**doi:10.1109/etfa65518.2025.11205636** — 02_tango/v0.2 · paywalled.md

could support `core` — the abstract promises case studies as proof of concept, which is the difference between an architecture paper and an evaluated system

### c308
**doi:10.1109/mcomstd.2026.3669229** — 02_tango/v0.2 · paywalled.md

nothing for the grid — a survey, already `context`. Its "limitations" section would be quotable evidence for section 06 if opened

### c309
**doi:10.1109/sci68648.2025.11333875** — 02_tango/v0.2 · paywalled.md

nothing — admitted `context` under the HPC-operations rule, and reading it would not move it to `core`

### c310
**doi:10.1109/ticps.2026.3665499** — 02_tango/v0.2 · paywalled.md

could support `core` — plan verification against a simulation is `verification-regression` evidence, and the abstract says the verification exists but not how it was measured

### c311
**doi:10.3997/2214-4609.202639027** — 02_tango/v0.2 · paywalled.md

core write-up; it compares three MCP server designs against each other, which is the only head-to-head comparison of `tool-exposure` designs in the admitted set

### c312
**doi:10.3997/2214-4609.202637165** — 02_tango/v0.2 · paywalled.md

core write-up; the abstract describes grid construction, geometry manipulation, heterogeneity generation and well configuration from intent, which is `topology-construction` and `config-generation` evidence with no substitute in the corpus

### c313
**doi:10.3997/2214-4609.2024637030** — 02_tango/v0.2 · paywalled.md

little — a one-paragraph conference abstract proposing a framework; it would stay `context`

### c314
**doi:10.3778/j.issn.1673-9418.2508051** — 02_tango/v0.2 · paywalled.md

could support `core`; AutoCode4OF generates OpenFOAM interface code end-to-end and the abstract does not say whether the generated cases were run

### c315
**doi:10.6084/m9.figshare.30931802** — 02_tango/v0.2 · paywalled.md

core write-up, and it is one of the few admitted sources whose agent-proposed candidate was synthesised and measured, so it is the corpus's strongest candidate for a maturity above M3. Abstract-only forces `not stated (abstract only)`

### c316
**title:agenticaienabled…** — 02_tango/v0.2 · paywalled.md

core write-up; the abstract reports a 6,156-run agentic benchmark, which would be the largest single evaluation in the corpus, but the orchestration modes it compares and the failure behaviour are in the unreadable chapters

### c317
**doi:10.1016/j.net.2026.104573** — 02_tango/v0.2 · paywalled.md

core write-up; it is one of only three admitted sources tagged `uncertainty-quantification`, and the only one that reports calibrated coverage against a human-expert pipeline on the same search

### c318
**doi:10.26434/chemrxiv-2025-f1wcr** — 02_tango/v0.2 · paywalled.md

modest; the abstract already states the system generates rather than runs optimisation code, which fixes its `autonomy` at `suggests`. Reading it would settle whether the generated pipelines were executed

### c319
**doi:10.26434/chemrxiv.15005838/v1** — 02_tango/v0.2 · paywalled.md

core write-up; replayable state-graph orchestration is the corpus's clearest `provenance-reproducibility` design and the abstract gives no evaluation numbers at all

### c320
**doi:10.1016/j.jma.2025.08.021** — 02_tango/v0.2 · paywalled.md

little for the grid — the abstract makes clear the agent advises rather than drives, so it would stay `context` on the autonomy axis even if read

### c321
**doi:10.5281/zenodo.20388035** — 02_tango/v0.2 · paywalled.md

nothing that is not already covered. This is the seven-solver predecessor of the eight-solver OASiS deposit, which is admitted `core` and read in full under the same `system_id`, so the system is in the grid at its later version

### c322
**doi:10.2139/ssrn.6672588** — 02_tango/v0.2 · paywalled.md

core write-up; it is one of very few admitted sources that gates every critical decision on a human and still reports autocorrected cluster failures, which is exactly the `failure_handling` evidence the corpus is thinnest on

### c323
**doi:10.1145/3785462.3815873** — 02_tango/v0.2 · paywalled.md

core write-up; hash-verified run specifications rejected before scheduling is a `provenance-reproducibility` mechanism with no equivalent elsewhere in the corpus, and the overhead figures are not in the abstract

### c324
**doi:10.26434/chemrxiv.15002405/v1** — 02_tango/v0.2 · paywalled.md

core write-up; it is the only admitted source whose central claim is that the agent should be kept *out* of the execution loop, and the abstract gives the token numbers but not the failure behaviour

### c325
**doi:10.26434/chemrxiv.15007941/v1** — 02_tango/v0.2 · paywalled.md

little; the abstract is unusually complete and the source is a proof-of-concept solver wrapper with no scored evaluation, so it would stay `context`

### c326
**doi:10.2139/ssrn.6942178** — 02_tango/v0.2 · paywalled.md

core write-up; 300 simulator evaluations inside an agent-driven loop is among the larger closed-loop campaigns in the corpus, and the abstract reports that the search did *not* converge monotonically — a negative result whose discussion is unreadable

### c327
**doi:10.1039/d5dd00435g** — 02_tango/v0.2 · paywalled.md

everything. v0.1 recorded `tango_touchpoints: none` and `not stated` in every column because no route returned narrative text. The version of record is a full CC-BY paper: a multi-agent AutoGen/AG2 system driving LAMMPS on the Argonne Carbon cluster through Atomsk, Phonopy and OVITO, with an HPC agent doing SCP and torque submission. Rated `M1` against a human-expert baseline, now carrying six touchpoints

### c328
**doi:10.2139/ssrn.7333555** — 02_tango/v0.2 · paywalled.md

everything. v0.1 had nothing beyond the title. The preprint is a three-agent orchestrator/diagnosis/tuning system driving EnergyPlus 23.2 through an Optuna TPE loop at 25 runs per pass on six named Purdue University buildings, validated against metered energy-use intensities held back until after calibration. Rated `M3`, and the corpus's fourth `uncertainty-quantification` core row

### c329
**doi:10.26434/chemrxiv.15006587/v1** — 02_tango/v0.2 · paywalled.md

less than the two above, as v0.1 predicted: the system was already in the grid through the authors' repository under the same `system_id`, so no system entered or left the corpus. What it added is the peer-review-facing evidence — the models named as Qwen2.5-32B-Instruct and 14B-Instruct, the 19-task benchmark structure, the six-way failure taxonomy, and the finding that iterative error feedback recovered hallucinated variable paths in zero of thirty instances. Rated `M2`

