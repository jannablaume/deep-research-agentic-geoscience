# Verification

One block per gap in `gaps.md`, written from what a verification subagent returned. Each
agent was briefed with the gap statement, its candidate ids and their `evidence_ref`s, and
one instruction: **search for work that would refute it**, in this order — the runs' own
`screened.csv` and `triage.csv` (every harvested record with its abstract, including
everything screened out), then the bibliographic APIs, then the open web.

The agents searched and reported; this session wrote every line below and every verdict
line in `gaps.md`. A verification that searched nothing returns `undecidable` whatever the
agent concluded.

## G01 — Neither corpus states whether its evaluation data was held out

- verdict: refuted
- searched: both runs' `papers.csv` (`held_out` tallied against `tier`); all four corpora
  (`screened.csv` and `triage.csv`, 11,191 + 11,177 + 35,054 + 35,046 rows) with a held-out
  regex — `held[- ]out|hold[- ]out|train[/\- ]test split|blind test|unseen (wells?|data|…)|
  out[- ]of[- ]sample|leave[- ]one[- ]out|cross[- ]validat|test set|k[- ]fold|80/20|70/15/15`
  — ANDed with an agentic pattern over title+abstract, 433 unique hits joined against each
  run's `screening.csv`; arXiv API, 8 queries; Crossref, 2 queries; two web searches.
- not searched: OpenAlex returned HTTP 503 (`Anonymous search is paused while the search
  cluster recovers from heavy load`) on all six attempts, so no independent bibliographic
  sweep was completed.
- found: the gap as stated is false against the runs' own grids. `held_out` is `yes` on 16
  of 151 admitted landscape rows (11 of 41 core) and 23 of 183 admitted TANGO rows (22 of
  101 core), with the split named in `evaluation_method` — for example "RMSE and R^2 on
  held-out test wells" (`doi:10.1016/j.petsci.2026.05.031`) and "a 70/15/15 split of two
  custom-curated datasets" (`doi:10.48550/arxiv.2408.15866`). Both tallies were re-derived
  in this session and match.
- found: four in-scope records reporting held-out evaluation were harvested, triaged and
  cut before screening. `arxiv:2606.09774` (SIGA) is the closest: `scope_computed` `core`,
  `band` `A_agentic`, `agentic_score` 0, absent from both runs' `screening.csv` and
  `papers.csv`, and its abstract reads "On GEOS, a multiphysics subsurface simulator,
  SIGA's main gain is reliability: on harder held-out tasks it improves TreeSim from 0.720
  to 0.789". Both the triage row and the absence were re-checked in this session. Also
  `doi:10.1190/tle44020114.1` ("in blind tests using experimental benchmark data"),
  `arxiv:2605.17792` ("across four held-out gauges") and `arxiv:2608.01369` ("its frozen
  82-case held-out split").
- found: the two runs code the same papers differently. Of the 11 `identity_key`s in both
  grids, 3 disagree and all 3 the same way — `not stated` in 01, `no` in 02. The landscape
  grid records `no` once in 151 rows; the TANGO grid records it 50 times in 183.
- what would change it: showing the four cut records out of scope on grounds independent of
  held-out reporting, and re-running the abstract regex over the admitted `not stated` rows
  to show the deep read missed no held-out language.

## G04 — Most admitted sources state nothing about code availability

- verdict: refuted
- searched: `code_availability` cross-tabulated against `tier` in both grids; 24 core rows
  recorded as `not stated` sampled and searched on the open web and GitHub (WebSearch for
  each system name; GitHub REST `/repos/…` and `/search/repositories?q=…` for
  `openfoamgpt`, `SeisEvo seismic`, `Agents4GEOS`, `MOOSEnger`, `FoamPilot`, `AutoSurrogate
  multi-agent`, `Geo2UBEM`, `PetroGraph history matching`); full-text greps for
  `github.com|gitlab.com|zenodo.org|huggingface.co` over arXiv HTML for 25 identifiers.
- found: the headline counts are dominated by rows that were never read in full. Exact
  `not stated` by tier, re-derived in this session: landscape core 20 of 41, landscape
  context 107 of 110; TANGO core 35 of 101, TANGO context 75 of 82. So 107 of the
  landscape's 127 and 75 of the TANGO run's 110 are abstract-only rows. At core tier the
  TANGO figure inverts: 66 of 101 state something and 58 give a working repository URL.
- found: three core rows recorded as `not stated` name a repository in plain text.
  `doi:10.48550/arxiv.2504.06260` (FEABench) ends its abstract "The code is available at
  this https URL" → `github.com/google/feabench`; `doi:10.48550/arxiv.2507.14267` (DREAMS)
  carries a section "Data and Code Availability" → `github.com/BattModels/material_agent`;
  `doi:10.1016/j.taml.2025.100594` (NL2FOAM) states "Our code and fine-tuned model have
  been deposited at https://github.com/YYgroup/AutoCFD." All three cells were re-checked in
  this session and all three read `not stated`. That is 3 of 24 sampled, and the FEABench
  statement is on the arXiv abstract page the row's own `url` points at.
- found: one case where the paper is silent but the artefact is public —
  `github.com/adricortes/agents4geos` exists under the first author's account, created
  2026-05-11, while `arxiv:2607.18557` links only the upstream GEOS repository.
- what would change it: re-extracting `code_availability` for the 35 TANGO core `not
  stated` rows against full text, and adding a category that separates "the paper is
  silent" from "no code exists".

## G11 — Geometry, meshing and spatial reasoning are named as an unresolved limit across domains

- verdict: partially-addressed
- searched: CSV-aware regex over title+abstract of all four corpora (35,055 + 11,192 rows)
  for `\bmesh(es|ing)?\b`, `\bgmsh\b`, `\bCAD\b|computer[- ]aided design|text-to-CAD`,
  `\bgeometr(y|ic|ies)\b`, `\bsalome\b`, `snappyhexmesh|blockmesh`, `grid generation|mesh
  generation|meshing agent|automatic mesh`, `discretiz|discretis` — 1,955 records carried a
  term, ~100 a strong one; literal greps for 16 named systems; arXiv API, 11 queries; three
  web searches; GitHub repo search.
- not searched: OpenAlex returned HTTP 503 for the whole session, so the bibliographic leg
  ran on arXiv alone, and six arXiv queries returned empty after rate-limiting.
- found: a dedicated meshing agent already exists inside the TANGO run's own core set.
  `doi:10.48550/arxiv.2509.18178` (Foam-Agent 2.0) was screened `in` at `core` and its
  abstract reads "advanced pre-processing with a versatile Meshing Agent capable of handling
  external mesh files and generating new geometries via Gmsh", with "an 88.2% success rate
  with Claude 3.5 Sonnet". Both the screening decision and the quote were re-checked in this
  session. Also in the corpus: "zero mesh generation failures" across 400+ parametric
  configurations (`doi:10.48550/arxiv.2511.00122`) and "100% success and reproducibility
  rates across over 450 simulations" driving blockMesh and snappyHexMesh
  (`doi:10.1016/j.ijheatfluidflow.2026.110399`).
- found: `doi:10.2139/ssrn.7083227` (MeshExpert, a physics-aware LLM meshing agent reported
  at 82.5% Pass@3 on 50 industrial automotive components) sits in the TANGO run's
  `screened.csv` and `triage.csv` with a zero-length abstract and is absent from
  `screening.csv`. Re-checked in this session: the abstract field is empty, so the triage
  scorer could not see it. SSRN returned HTTP 403, so the reported figure is from a search
  snippet and is not independently confirmed.
- found: eight further records reporting successful geometry or mesh generation were
  harvested and never screened, among them `doi:10.21203/rs.3.rs-8562963/v1` (FeaGPT,
  "complete geometry-mesh-simulation workflows"), `arxiv:2607.05573` ("98.97% mesh success")
  and `arxiv:2605.28978` (VFEAgent). An adjacent text-to-CAD literature (CAD-Coder, NURBGen,
  TOOLCAD, Zero-to-CAD, LLaMA-Mesh) has zero hits in either corpus.
- found: the descriptive half stands where the geometry is not parametric. One harvested
  record reports 70% success on simple shapes, 56% on assemblies and "This 0% success rate
  for Boolean operations represents the primary bottleneck for assembly automation"
  (`doi:10.3390/app152212114`). For geological and reservoir geometry specifically the
  agent found no refuting work at all.
- what would change it: reading MeshExpert's full text to see whether its 50 components
  include non-parametric imported CAD; or an evaluated agentic system building geological
  grids — corner-point, faulted, stratigraphic — on held-out real models.

## G06 — No source reports its agent's output being acted on outside the experiment and later found wrong

- verdict: confirmed-absent
- searched: all four corpora (11,191 / 11,177 / 35,054 / 35,046 rows), two regex passes over
  title+abstract — `\bretract(ion|ed|ing|ions)\b`, `\berrat(um|a)\b|\bcorrigend(um|a)\b`,
  `incident report|incident(s)? (database|taxonomy|analysis)`, `later (found|discovered|
  revealed) to be`, `post[- ]?mortem`, `near[- ]miss`, `corrected (result|finding|
  conclusion)`, `silently (propagat|corrupt|fail)|undetected (error|failure)` (240 hits),
  then a deployment/consequence pass restricted to LLM-agent rows (~120 hits); OpenAlex,
  10 queries; Crossref, 3 DOI lookups; arXiv, 9 queries; 15 web searches including the AI
  Incident Database.
- found: nothing satisfying all three conjuncts. The nearest artefacts are two
  post-publication notices, both in the runs' own corpora and neither readable:
  `doi:10.1016/j.autcon.2025.106421`, a corrigendum to an LLM-multi-agent geotechnical
  design paper, and `doi:10.1016/j.tramat.2026.100176`, "RETRACTED: Reshaping MOFs
  synthesis conditions mining with a dynamic multi-agents framework of large language
  model". Elsevier returned a redirect and HTTP 403 respectively, so neither notice's text
  was read and neither shows external use.
- found: the run's characterisation of its own near-miss is correct.
  `doi:10.1145/3731599.3767349` is an authors' own experiment.
- found: `arxiv:2508.14231` ("Incident Analysis for AI Agents") is a framework only — "no
  actual real-world incidents are described in detail … These are potential scenarios, not
  documented cases." The AI Incident Database's 1,400+ entries surfaced no
  scientific-simulation, solver or geoscience incident.
- caveat recorded rather than resolved: OpenAlex paused anonymous search for the first five
  queries, and the two most on-point notices could not be fetched. The verdict rests on "no
  such report was findable", not on "the two closest notices were read and ruled out".
- what would change it: the text of either notice, if it corrects an output a third party
  had used; or a Retraction Watch database query crossed with LLM/agent keywords, which was
  not run.

## G12 — A run that executes is not a run that is physically right, and the corpora record that the second is not checked

- verdict: refuted
- searched: all four corpora deduplicated to 44,962 records (38,293 with abstracts), regex
  over title+abstract for `physical(ly)? valid` (29), `conservation (law|check)` (32),
  `dimensional (analysis|consistency)` (40), `formal verification` (82), `method of
  manufactured solutions|grid convergence` (29), `physical(ly)? (correct|plausib|consistent|
  meaningful)` (140), `material balance|mass balance (error|check|residual)` (10), plus
  `evaluation_method` and `reported_result` scans of both grids; five web searches.
- not searched: OpenAlex returned HTTP 503 on every attempt, arXiv and Semantic Scholar
  HTTP 429. No bibliographic API result was obtained.
- found: separate physical-validity scoring already exists inside the TANGO run's own
  deep-read core set. `doi:10.48550/arxiv.2606.07850` (PDE-Agents) reports "physics score
  0.933 against 0.853"; `doi:10.48550/arxiv.2509.20374` (CFDLLMBench) aggregates "physical
  accuracy" into its success rate; `doi:10.1002/aidi.202500174` reports "82.1% execution
  success … with 68.12% physical fidelity". All three tier values and result strings were
  re-checked in this session.
- found: at least six dedicated physics-validation benchmarks and verifiers sit in the
  TANGO harvest unscreened — `doi:10.48550/arxiv.2605.09360` ("execution-only repair
  improves execution success while leaving 39-40% of all 220 cases runnable but still
  solving the wrong physics", with a deterministic Intent Fidelity Score),
  `doi:10.26434/chemrxiv.15007535/v1` (PROBE, five levels including "dimensional
  consistency (units)" and "physical invariants (mass/energy conservation)"),
  `doi:10.48550/arxiv.2603.20986` (AutoMOOSE, "a physics-grounded Skeptic"),
  `doi:10.48550/arxiv.2606.18789`, `doi:10.48550/arxiv.2604.23580` and
  `doi:10.1109/access.2026.3685519`.
- what would change it: restricting the gap to solid-earth and subsurface geoscience, where
  only `doi:10.48550/arxiv.2501.14186` (GeoSim.AI) and `arxiv:2603.00214` (JutulGPT) were
  found and neither reports a quantitative physical-validity rate.

## G13 — Hallucination is recorded as present and unresolved rather than eliminated

- verdict: partially-addressed
- searched: all four corpora deduplicated to 44,962 records, 15 regex families over
  title+abstract — `hallucinat\w*\s+(is|are|…)?\s*(eliminat|remov|prevent|preclud|
  impossib|obviat)` (7), `(zero|no|free (of|from)|without)[-\s]+hallucinat` (14),
  `hallucination[-\s]?free` (10), `constrained decod` (7), `schema[-\s]?(constrain|guid|
  enforc)` (54), `typed tool|typed (API|interface|function)|type[-\s]safe` (27),
  `grammar[-\s]?(constrained|based|guided)|GBNF` (10), `cannot (occur|happen|be
  (invent|hallucinat))|by construction` (49), `hallucinat` baseline (1,433), and a
  co-occurrence pass narrowed to geoscience and simulator terms (11); five web searches.
- not searched: OpenAlex HTTP 503 on all five queries, arXiv HTTP 429 on all five attempts.
- found: the second half of the gap as stated is wrong. `doi:10.26434/chemrxiv.15006587/v1`
  is a cited row, and the TANGO run's own `report/06_failure_and_limits.md` describes it as
  "the failure mode it designed out rather than mitigated", with invented object paths
  accounting for 78% of code-generation failures and structurally unreachable through typed
  tools.
- found: two further records in the TANGO harvest, neither screened. `arxiv:2605.11234`
  reports "unconstrained tool parameters produced a 43% hallucination rate for domain
  identifiers; ontology-grounded parameters reduced this to 0%" over 72 tool invocations on
  one model; `doi:10.48550/arxiv.2608.30696` states "By construction the design removes
  whole classes of failure … and narrows the strategic errors that remain".
- found: the first half stands. Every elimination claim is scoped to one failure class
  reachable by typing the interface — invented object paths, invented domain identifiers —
  with semantic and numeric error left standing. `doi:10.48550/arxiv.2512.06404` reports
  hallucinations "virtually" eliminated; `doi:10.1016/j.egyai.2026.100710` reports a
  reduction "from 100% to as low as 5%". Nothing reports the category closed in a
  subsurface or simulator-control deployment.
- what would change it: a measured zero over a defensible denominator in the solid-earth or
  simulator-control setting covering more than one failure class.

## G19 — Neither run read its periphery, and one names topics it never harvested

- verdict: partially-addressed
- searched: both `queries.csv` files and both query plans (`reference/queries.json`,
  `reference/queries_tango.json`) for `hydrolog`, `surface water`, `streamflow`, `runoff`,
  `watershed`, `catchment`, `ecolog`, `biodiver`, `river`, `flood`; joins of
  `triage.csv` × `screening.csv` × `papers.csv` in both runs; surface-water and ecology
  regex families over all four corpora; six web searches.
- not searched: OpenAlex HTTP 503, arXiv HTTP 429 throughout, so the external leg rests on
  web search and the corpora alone.
- found: c090 is exactly true. Neither query plan contains a surface-water or ecology term;
  the landscape run's five periphery groups are `earth_observation`, `climate_atmosphere`,
  `ocean`, `planetary`, `geoscience_general`, and `hydrogeology` is core with subsurface
  terms only.
- found: c244's "never screened" clause is contradicted by the TANGO run's own artifact.
  Re-derived in this session: of 939 screening rows, 469 are periphery-scope and all are
  `out`; 489 records matched only by cells `q015`–`q022` reached `screening.csv`, of which
  487 are `out`, one `in`/`core` and one `in`/`context`. The claim in
  `report/07_periphery.md` that those cells were "harvested and triaged but never screened"
  is wrong. The "never read" half is correct: 0 of 183 admitted rows is periphery.
- found: the uncovered ground is not empty, and the loss is a threshold rather than a
  periphery decision. Eighteen core-scope surface-water agent systems sit in the TANGO
  `triage.csv` unshortlisted, cut by `--min-domain 4` — among them `arxiv:2605.17792`
  (HydroAgent, calibrating VIC/hydrologic models, `agentic_score` 12, `domain_score` 1),
  `doi:10.48550/arxiv.2606.07681` (translating a 19,000-line Fortran land-surface model)
  and `doi:10.1016/j.jenvman.2026.130619` (SWMM stormwater).
- found: the consequence half is refuted for surface-water hydrology, which the TANGO run
  did deep-read twice — `doi:10.5281/zenodo.19597589` drives "HBV-light differentiable
  calibration and NeuralHydrology zoo rainfall-runoff models" and `doi:10.31223/x5f47g`
  drives "the EPA SWMM 5.2.4 command-line engine" at M3 — and confirmed for ecology, where
  0 records were deep-read in either run and four external systems were found outside both
  corpora, including `doi:10.1111/faf.70079`.
- what would change it: dropping the "never screened" clause and dropping surface-water
  hydrology from the unread list would make the remainder confirmed-absent.

## G23 — No shared or third-party benchmark, and no agreed way to score these systems

- verdict: refuted
- searched: all four corpora deduplicated to 44,962 records (38,293 with abstracts), named
  benchmark regex (`ScienceAgentBench|MLAgentBench|CORE-?Bench|SciCode|DiscoveryBench|
  LAB-?Bench|MatTools|FEABench|AstaBench|BixBench|ScienceBoard|DSBench|MLE-?bench|
  PaperBench`) and a `we (introduce|present|propose|release) … benchmark` pattern; per-term
  `grep -ci` across both grids; membership checks against `screening.csv`; six web
  searches; HuggingFace space search.
- not searched: OpenAlex HTTP 503 and arXiv HTTP 429, so API-level search largely failed.
- found: cross-domain benchmarks for agents driving simulators and scientific software
  exist and are reused by independent groups. `arxiv:2505.19897` (ScienceBoard, "169
  high-quality, rigorously validated real-world tasks … spanning … biochemistry, astronomy,
  and geoinformatics" over six packages) is reused by `arxiv:2508.20096`;
  `doi:10.48550/arxiv.2410.05080` (ScienceAgentBench) is reused by
  `doi:10.48550/arxiv.2603.28986`; `arxiv:2510.21652` (AstaBench, "2400+ problems …
  multiple scientific domains") carries a public leaderboard. `doi:10.1109/access.2026.3685519`
  (SimBench) ranks 33 models on digital-twin quality with a judge model and is accompanied
  by a replication archive.
- found: `https://arxiv.org/abs/2603.20253` (SimulCost, "2,643 single-round … and 2,304
  multi-round … tasks across 11 simulators from fluid dynamics, solid mechanics, and plasma
  physics") is absent from both corpora entirely.
- found: the run's own admitted set already contradicts the claim.
  `doi:10.48550/arxiv.2409.11363` (CORE-Bench, "270 tasks based on 90 scientific papers
  across three disciplines") is `in`/`context` in `screening.csv`, re-checked in this
  session; `doi:10.48550/arxiv.2505.10852` (MatTools) is `in`/`context` with the run's own
  note calling it a "false negative on the same line as the admitted CFD and FEA benchmarks".
- found: automated rubrics exist — `doi:10.48550/arxiv.2608.31076` (AutoSciRub, "induces a
  task-specific executable rubric") and AstaBench's 507 rubric items.
- what would change it: scoping the gap to solid-earth and subsurface geoscience, where no
  cross-domain benchmark and no leaderboard was found and the CFD-only FoamBench
  observation still holds.

## G05 — No system in either corpus demonstrates maturity above M3

- verdict: refuted
- searched: five regex passes over all four corpora (~46k records including everything
  cut) — a deployment pass (`deployed (in|at|on|to) (production|the field|an? (operator|
  operational|real|commercial|industrial|live))|productioni[sz]ed|operational deployment|
  field deployment`, 39 hits); the same ANDed with an LLM/agentic term (666); narrowed to
  geoscience or simulator terms (105); a title-level subsurface pass with strong deployment
  verbs (30); and an M5 probe (`independent(ly)? (evaluat|assess|validat|audit)|third[-
  ]party (evaluat|validat|verif)|blind (evaluation|trial)`, 166 hits); eleven web searches;
  six publisher fetches.
- not searched: OpenAlex HTTP 503 on all seven queries, arXiv HTTP 429 on all four, so the
  bibliographic leg is empty. OnePetro and ResearchGate returned HTTP 403.
- found: an M4-shaped source sits in the landscape corpus with an openly readable full
  text that the run never reached. `doi:10.2118/0426-0008-jpt` is `tier: context`,
  `access_status: abstract-only`, `maturity_demonstrated: not stated (abstract only)` —
  re-checked in this session — while the JPT article page carries the full text: an agentic
  framework "deployed for India's Oil and Natural Gas Corporation (ONGC)" driving "SLB's
  Pipesim engine" over roughly 600 wells and 370 simulation scenarios across three fields,
  with "a group of production engineers independently recreated a subset of models manually
  inside Pipesim and compared them with agent-generated models. The automated outputs were
  found to be fully consistent."
- found: three further admitted records carry deployment language and the same
  `not stated (abstract only)` rating — `doi:10.2118/233425-ms` ("deployed across a
  portfolio of over 1,000 wells … approximately 75%" time reduction),
  `doi:10.2523/iptc-25245-ms` ("Pilot deployments in Waterflood, Field A, and Reservoir
  Simulation") and `doi:10.2118/229240-ms` (ENERGYai at ADNOC). All four tier and rating
  values were re-checked in this session.
- found: two more reached `scope_computed: core` in triage and have no `screening.csv` row
  at all — `doi:10.1145/3748636.3764602` (DIGMAPPER, "Deployed at USGS … supporting
  national-scale critical mineral assessments", `agentic_score` 3, `domain_score` 0) and
  `doi:10.2118/229325-ms` (ADNOC AiPSO, "Aimed to be deployed across 25 fields",
  `agentic_score` 6, `domain_score` 1). Both absences re-checked in this session.
- found: the M5 half survives. The 166-hit independence probe returned nothing in scope,
  and the closest verification found is internal to the deploying organisation.
- what would change it: narrowing the claim to M5 — no verification by a party independent
  of the developing or deploying organisation — which nothing found here contradicts.

## G09 — `instrument-control` appears on no deep-read landscape row

- verdict: confirmed-absent
- searched: both grids for `instrument` in `agentic_techniques` and `tools_used`; all
  technique tokens tallied over the 41 core landscape rows; three regex sweeps over 46,245
  harvested records with abstracts — a hardware lexicon (`seismometer|seismic acquisition|
  geophone|downhole|logging tool|wireline|drill(ing)? rig|autodriller|managed pressure
  drilling|borehole (tool|instrument|probe)|sensor network|telemetry|SCADA|robot|drone|UAV|
  instrument control|self-driving lab|actuat|triaxial|shake table|centrifuge|piezometer|
  inclinometer|tiltmeter|GNSS station|hardware-in-the-loop|PLC|ROS2`) ANDed with an agent
  lexicon (1,788 hits), narrowed by a control verb and a geoscience term (305, then 55 read
  by title), and a proximity pass with eight named probes including `geosteering`, choke and
  setpoint control, and ocean-bottom seismometer deployment; OpenAlex, 12 search queries
  plus 50 filtered `title_and_abstract.search` queries using the repository's API key; six
  web searches; one fetch.
- not searched: arXiv returned HTTP 429 on all eight queries, so that leg rests on
  OpenAlex's arXiv coverage and web search.
- found: nothing controlling a physical instrument in solid-earth geoscience. The two core
  rows that could have earned the tag both drive software: `doi:10.48550/arxiv.2609.01777`
  (TREMORS) automates "seismic data retrieval" through ObsPy against FDSN web services, and
  `doi:10.3997/2214-4609.202535040` reads rig sensor streams through "MCP-exposed endpoints
  of preexisting surface logging applications" and commands software only.
- found: the TANGO run's single `instrument-control` row is `doi:10.1109/ipdps65963.2026.00114`
  (Academy), `subfield: scientific_computing` — DOE HPC and light-source middleware, not
  geoscience.
- found: the technique is well published elsewhere — X-ray microscopy
  (`doi:10.1093/mam/ozaf048.1092`, "autonomous operation of a Zeiss Versa X-ray Microscope
  via an API"), materials and microelectronics — and absent from solid-earth work. The
  nearest geoscience actuation, `doi:10.3390/drones9120829` (UAV volcanic gas monitoring on
  Santorini), carries `llm_present: no` and `agentic_score: 0`, so it is out of scope by
  construction.
- what would change it: an LLM agent issuing a command that changes the physical state of a
  geoscience instrument — a setpoint to an autodriller or choke, a gain or sample-rate
  change on a datalogger, a geosteering toolface command — with the command path described.

## G17 — Sources that state no limitations at all, and grids that record the field as empty

- verdict: partially-addressed
- searched: `author_stated_limitations` cross-tabulated against `tier` and `source_type` in
  both grids; eight deep-read core sources fetched in full from arXiv HTML or PDF and
  grepped for limitation, drawback, shortcoming, caveat and weakness; a sample of
  context-tier `not stated` rows with arXiv URLs fetched; eight web searches on limitation
  reporting as a meta-research topic.
- found: the headline counts are an abstract-only artefact. Re-derived in this session:
  landscape core 0 of 41, landscape context 63 of 110; TANGO core 2 of 101, TANGO context
  64 of 82. Both core exceptions are software deposits rather than papers —
  `doi:10.11578/dc.20260516.1` and `doi:10.5281/zenodo.19597589`, both `source_type: repo`.
  Across 138 core-tier papers in the two grids, none records `not stated`.
- found: at least one context-tier `not stated` row is wrong. `doi:10.48550/arxiv.2505.10852`
  (MatTools) has a section "A.3 Limitations" beginning "Despite the strengths of our
  automated pipeline, several limitations exist."
- found: the per-source records the gap cites are accurate. Eight were fetched and eight
  confirmed — Foam-Agent 2.0 (`doi:10.48550/arxiv.2509.18178`) has no limitations section
  and a forward-looking conclusion; VASPilot (`doi:10.48550/arxiv.2508.07035`) has no
  explicit limitation statement; specfem-mcp (`doi:10.48550/arxiv.2512.14429`) has a
  "Conclusion and Outlook" that is forward-looking only; AutoSurrogate
  (`doi:10.48550/arxiv.2604.11945`) has no limitations section and only the plume-boundary
  remark the grid recorded; GeoMind, Sim2Schedule, OpenFOAMGPT 2.0 and OptMetaOpenFOAM
  likewise.
- found: the phenomenon is already named and benchmarked outside this corpus — BAGELS
  (`arxiv:2505.18207`), "authors often underreport limitations in their papers and rely on
  hedging strategies" — and neither run harvested it.
- what would change it: restating the count at core tier, where it is 0 of 138 papers, and
  relabelling the 63 and 64 as a measure of reading depth.

## G18 — Both runs record sources whose stated claim reaches past the maturity their evaluation demonstrated

- verdict: partially-addressed
- searched: both grids cross-tabulated for core `maturity_demonstrated` in {M0, M1} against
  the `claim-gap` candidate set; seven of the quoted claims fetched from arXiv abstracts,
  HTML or PDF and checked verbatim against the evaluation each rests on; both source
  reports' own overreach sections read; four web searches on overclaiming in agent research.
- found: the count of 47 is a mechanical sweep, not an adjudication. Re-derived in this
  session: TANGO core M0/M1 is 41 rows and landscape core M0/M1 is 14, total 54; G18 cites
  54 minus the 7 discarded as obviously modest.
- found: both source reports give a much smaller number. `02_tango/v0.2/report/05_maturity.md`
  states "Of the 40 core sources demonstrating M0 or M1, 7 make a claim whose language
  reaches substantially further than the evidence rated … The remaining 33 make claims
  proportionate to a demonstration"; `01_landscape/v0.5/report/05_maturity.md` names five.
- found: several cited rows are result statements or hedged phrasing rather than overreach —
  "the pipeline can extract entities, parse locations, and generate executable coordinates",
  "suggest", "have the potential", "highlight the promise" — and c294 (M.A.R.V.I.N.) is cited
  in the TANGO run's own report under "Counter-examples worth recording".
- found: one candidate's quote is a fragment. c259's "demonstration of production-grade
  reliability for the full agent stack" is part of a sentence beginning "The 97.8% overall
  success rate (1,339/1,369 …) demonstrates", and that paper carries an explicit Section 8
  of limitations ("The current solver supports only scalar heat equations").
- found: for seven named systems the overreach is real and the quotes are verbatim —
  specfem-mcp ("the first application of MCP technology to computational seismology", five
  demos, no baseline, no numeric metric), VASPilot ("fully automates VASP workflows", four
  demo tasks), AutoSurrogate ("establishes a new paradigm for surrogate modeling", synthetic
  aquifer), Sim2Schedule, GAIA, MASTER and OpenFOAMGPT 2.0.
- found: the phenomenon is documented outside both corpora — "AI Agents That Matter"
  (`arxiv:2407.01502`), "overoptimistic claims about agent capabilities" — and a grep for it
  across both grids and both report sets returns nothing.
- what would change it: an adjudicated list giving, per row, the quote, the evaluation it
  rests on and a stated criterion for "reaches past", reconciled with the runs' own 7-of-40
  and 5-of-14.

## G02 — A quarter to a third of deep-read systems report no baseline

- verdict: partially-addressed
- searched: `baseline` cross-tabulated against `tier` and `access_status` in both grids;
  abstracts of all 18 core rows coded `none` checked for contradicting baseline language;
  regex sweep over all abstracts for an agentic term ANDed with a baseline term ANDed with a
  geoscience or engine term (1,101 loose, 370 strong, 44 tight-scope hits); baseline-language
  rate compared between admitted-core and cut triage-core abstracts; arXiv, 3 queries
  completed and 6 rate-limited; 3 web searches.
- not searched: OpenAlex HTTP 503 on all three queries.
- found: c094 and c247 measure two different things at once. Re-derived in this session,
  the landscape run's 84 is 75 rows reading `not stated` plus 9 reading `none`, and the
  TANGO run's 47 is 7 `not stated` plus 40 `none`. Every `not stated` row in both grids is
  `tier: context`, `access_status: abstract-only` — 75 of 75 and 7 of 7 — and 13 TANGO rows
  carry the literal string "none stated in the abstract". `scripts/gaps.py` treats `none`
  and `not stated` as the same empty cell, so the counts merge a silent abstract with a
  source that reports no comparator.
- found: c101 and c254 survive. All 18 core rows coded exactly `none` are `full-text`, and
  their `evaluation_method` cells confirm the absence independently — for example
  `doi:10.56952/igs-2025-0391`, "no quantitative benchmark, scoring metric or baseline
  comparison". Re-derived: 6 of 41 and 12 of 101.
- found: the stated rate is roughly double what those two candidates support. 6 of 41 and
  12 of 101 are 15% and 12%, not a quarter to a third; the 27% and 26% figures require
  counting every cell beginning "none", which includes ablation-only, analytical-reference
  and measurement-validated systems.
- found: the selection bias runs toward the gap, not against it. Baseline language appears
  in 40.5% of admitted-core landscape abstracts against 8.8% of cut triage-core ones, and
  29.5% against 14.3% in the TANGO run.
- found: at least nine in-scope systems with quantitative baselines were cut at triage and
  never screened, among them `arxiv:2606.09774` ("In a human calibration, SIGA reaches in
  about five minutes the deck quality a domain expert reached in about three hours",
  `agentic_score` 0), `doi:10.48550/arxiv.2603.04756` ("a 0.90 execution pass rate versus
  0.06 for an LLM-only baseline") and `doi:10.48550/arxiv.2606.10752`.
- what would change it: a full-text read of the 18 `none` core records; two or three
  extraction errors would collapse the finding.

## G16 — Evaluations are narrow by the authors' own account: one site, one platform, one small set

- verdict: partially-addressed
- searched: 13 regex families over all four corpora (44,962 unique records, 38,293 with
  abstracts) for multi-site, multi-basin, large problem-set, multi-engine, named-public-asset
  and blind-evaluation language, each ANDed with an agent term and cross-checked against
  `screening.csv` and `papers.csv`; structured scans of both grids' `data_type`, `held_out`,
  `evaluation_method` and `tools_used`; OpenAlex `title_and_abstract.search`, 3 queries;
  5 web searches.
- not searched: arXiv returned zero entries for every phrased query while a control query
  returned 186,077, so arXiv contributed nothing.
- found: "one platform" is contradicted inside the TANGO run's own deep-read set. OASiS
  exposes "13 MCP tools over FEniCSx, deal.II, 4C Multiphysics, NGSolve, scikit-fem, Kratos
  Multiphysics, DUNE-fem and FEBio"; NeuroClaw runs "FSL, FreeSurfer, fMRIPrep, QSIPrep and
  ANTs"; TRACE in the landscape core set drives ObsPy, SeisBench, DASPy, GaMMA, HypoDD,
  PhaseNet, EQcorrscan and more.
- found: larger evaluations exist and were cut at triage. `arxiv:2604.03460` (FermiLink)
  reports capabilities "across approximately 50 scientific software packages spanning nine
  research domains" with "132 real-world figure-level reproduction tasks with 44 packages",
  and carries `scope_computed: core`, `agentic_score` 0, absent from `screening.csv` —
  re-checked in this session. Also `arxiv:2605.08941` (MDGYM, 169 simulations over LAMMPS
  and GROMACS, `agentic_score` 11, `domain_score` 2) and `arxiv:2605.09636`
  (PDEAgent-Bench, "645 instances across 6 mathematical categories and 11 PDE families,
  with common FEM libraries for DOLFINx, Firedrake, and deal.II"), which contradicts c141
  and c230 as field-level statements.
- found: the landscape run cut a 7,440-question subsurface benchmark of its own,
  `doi:10.20944/preprints202606.1410.v1` (UpstreamBench), `scope_computed: core`,
  `agentic_score` 2, absent from `screening.csv`.
- found: the largest deployments are in the grids but tiered `context`, so they sit outside
  the 41 and 101 denominators by construction — `doi:10.2118/233425-ms` at "over 1,000
  wells" and `doi:10.2118/0426-0008-jpt` at ONGC.
- what would change it: restating the gap over the systems the runs deep-read rather than
  over the literature, and saying why the broad cases were excluded.

## G24 — Open-weight and smaller models are recorded as failing where frontier models do not

- verdict: refuted
- searched: five regex families over 46,245 unique records (39,355 with abstracts) pairing
  open-weight, parameter-count and fine-tuning terms with parity and outperformance terms
  against frontier-model terms (32, 77, 7, 8 and 0 hits); named-system probes; OpenAlex,
  4 queries before rate-limiting; Crossref, 4 queries; 4 web searches.
- not searched: arXiv returned zero bytes for every query including a control, so it is
  unreachable from that environment; Semantic Scholar HTTP 429.
- found: four results invert the claim on this exact task class. `arxiv:2601.05187`
  (SimuAgent) reports a "Qwen2.5-7B model fine-tuned with SimuAgent … even surpasses GPT-4o"
  on 5,300 simulator-modeling tasks; `doi:10.26434/chemrxiv-2024-9g2w2` reports finetuned
  models that "outperform the formally much more powerful GPT-4o model" at generating ORCA
  input files; `arxiv:2605.24844` (Geo-Expert) reports "a domain-aligned 8B model can
  outperform open-weight 70B generalists and proprietary GPT-4o on specialized geological
  reasoning"; `arxiv:2606.12821` (GeoNatureAgent) reports open-weight DeepSeek V3.2 at "93%
  of Claude's capability at 11.6x lower cost" on 93 geospatial-API agent tasks.
- found: the landscape run cut a parity result in its own home domain.
  `doi:10.1016/j.acags.2025.100311` states "the fine-tuned open-source model achieves
  performance comparable to proprietary models, extending the applicability of open LLMs to
  domain-specific agentic workflows"; it carries `agentic_score` 17, `strong_hits` 4,
  `domain_score` 0, and its `screening.csv` row reads `out`, `cut_reason: periphery` —
  re-checked in this session.
- found: every candidate cited by the gap tests a prompted, un-adapted model. The source of
  the QwQ-32B quote, `doi:10.1016/j.taml.2025.100623`, itself records "Local 32B model on
  one GPU fails OpenFOAM syntax—fine-tuning still needed".
- what would change it: restating the gap as un-adapted open-weight models underperforming,
  which the candidates do support; or full-text reads showing SimuAgent and the ORCA work
  are contaminated or compare against a weak frontier baseline.

## G26 — Recurrent agent-side failure modes recorded inside the loop

- verdict: refuted
- searched: title-level and abstract-level failure-taxonomy regex over all four corpora
  (40 title hits, 13 scoped hits, plus four narrower passes returning 0); named probes for
  MAST, AgentErrorTaxonomy, MDGYM, MDArena, PRBench and a dozen agent benchmarks; a
  landscape-only sweep pairing failure-mode terms with agent terms (40 records, none a
  cross-system taxonomy); OpenAlex, 4 queries before rate-limiting; Crossref, 4 queries;
  4 web searches; 2 fetches.
- not searched: arXiv unreachable (zero bytes for every query including a control);
  Semantic Scholar HTTP 429.
- found: cross-system failure taxonomies exist. `arxiv:2605.08941` (MDGYM) evaluates "three
  agentic frameworks -- Claude Code, Codex, and OpenHands -- with four LLMs" over 169 MD
  simulations on LAMMPS and GROMACS and reports that agents "fabricate numerical outputs
  without executing the underlying computation, or abandon tasks prematurely", concluding
  these modes are "qualitatively distinct from those observed in general software
  engineering benchmarks". `doi:10.48550/arxiv.2606.21841` is an "eight-category failure
  taxonomy" for LLM-assisted multiphysics simulation whose "false summit" and "silent
  drift" categories subsume c156 and c209. `arxiv:2603.27646` (PRBench) and
  `arxiv:2608.02642` (MDArena) each measure failure modes across multiple agent
  configurations.
- found: both in-corpus taxonomies were cut at triage. MDGYM carries `agentic_score` 11,
  `domain_score` 2; `doi:10.48550/arxiv.2606.21841` carries `agentic_score` 4,
  `strong_hits` 0, `domain_score` 4. Neither appears in `screening.csv` — re-checked in
  this session. MDArena and `arxiv:2509.25370` are in neither corpus.
- found: the landscape sweep returned no cross-system failure taxonomy for geoscience
  agents, so the claim survives if scoped to solid-earth and subsurface work.
- what would change it: rescoping to geoscience, where the absence holds and nothing
  refuting was found.

## G28 — Evaluation data is synthetic, self-made, or of unestablished provenance

- verdict: partially-addressed
- searched: contamination, blind-evaluation, knowledge-cutoff and third-party regex families
  over all four corpora (180, 129 and 116 hits), each cross-checked against `screening.csv`;
  `data_type`, `held_out`, `evaluation_method` and `author_stated_limitations` scanned in
  both grids for blind, contamination, independent, third-party and pre-registered language;
  OpenAlex, 3 queries; 5 web searches.
- found: the broad form is contradicted by the runs' own grids. Re-derived in this session,
  synthetic-only is a minority both times — landscape core `data_type` is real-field 20,
  synthetic 9, benchmark 9, not stated 3; TANGO core is benchmark 52, synthetic 29,
  real-field 15, not stated 5. Established third-party artefacts recur in the core sets:
  SPE1, SPE9 and Norne; Equinor Volve; OC20NEB; CrossDocked2020; the IEEE 118-bus case;
  MineBench; and metered energy data from Purdue Facilities Management.
- found: the narrow form — no blind or unaffiliated third-party evaluation — holds and is
  corroborated from inside. Grid-Mind's authors state "the evaluation does not yet
  constitute a blinded third-party benchmark", and `doi:10.26434/chemrxiv.15007866/v1`
  (cut at triage) reports that of thirteen comparable multi-agent systems, "One system
  (STELLA) has an independent external evaluation, reported by an unaffiliated group …
  The remaining eight report author-curated computational evaluation only."
- found: the three genuine blind or held-out instances were all lost by the runs.
  `doi:10.1016/j.net.2026.104573` (OPTIMA) is evaluated on "the OECD/NEA critical heat flux
  (CHF) benchmark of 24,579 measurements" and "reproduces physically consistent trends
  across blind slice datasets", and was demoted core to context for want of full text rather
  than on evidence; `arxiv:2604.03460` reports "a single-blinded study … on unpublished
  polariton physics problems" and was cut at triage; `arxiv:2608.01369` reports a "frozen
  82-case held-out split" and was cut at triage.
- what would change it: separating provenance from independence — the counts support
  "author-run, unblinded reuse of public data", not "synthetic or self-made".

## G10 — No agent drives a life-cycle economic model as the system it controls

- verdict: refuted
- searched: three passes over all four corpora (92,468 rows) — an economic regex
  (`lcoe|levelis|discounted cash|\bnpv\b|techno-?econom|\btea\b|life-?cycle cost|capex|opex|
  \bhomer\b|system advisor model|aspen econom|retscreen|payback period|\birr\b|cash flow`)
  ANDed with an agent regex, 431 unique hits with every title read; a named-tool pass;
  and an enumeration of every triage row carrying the `techno_economic` touchpoint
  cross-joined against `screening.csv` and `papers.csv`; Crossref, 10 queries; 7 web
  searches; 8 fetches.
- not searched: OpenAlex HTTP 503 on all 10 queries, arXiv HTTP 429/301 on all 19,
  Semantic Scholar HTTP 429 on all 6. The bibliographic leg rests on Crossref alone.
- found: the TANGO run harvested a paper titled "An AI Agent for Techno-Economic Analysis
  of Anaerobic Co-Digestion in Renewable Energy Applications" (`doi:10.3390/en18215632`),
  triaged it `band: A_agentic`, `scope_computed: core`, `llm_present: yes` with the
  `techno_economic` touchpoint attached, and never screened it. Its abstract reads "The
  research leverages an innovative AI-agent framework to streamline TEA" and reports "a net
  present value (NPV) of GBP 19 million and an internal rate of return (IRR) of 36%". The
  landscape run cut the same DOI as `out`, `cut_reason: not-geoscience`. All of this was
  re-checked in this session.
- found: 135 triage rows carry the `techno_economic` touchpoint and 3 of them reached
  `screening.csv` — re-derived in this session. The absence-claim was issued while 98% of
  the rows bearing that touchpoint were unread.
- found: two further unscreened records point the same way — `doi:10.54097/3dwqbf59`
  (CCS financial appraisal, in a low-credibility venue) and `doi:10.1016/j.rser.2023.113933`
  — and one external benchmark, `arxiv:2606.26346`, equips agents with "asset optimization
  models" and "tariff impact modeling" tools.
- found: the narrow reading survives. Every counterexample is in bioprocess, chemical,
  power-market or generic-energy work; the one admitted geothermal case,
  `doi:10.2118/232332-ms`, predicts "levelized cost of heat and electricity" as a surrogate
  KPI inside an optimisation, which is the pattern the gap already concedes.
- what would change it: the full text of `doi:10.3390/en18215632` showing its "AI-agent
  framework" is a fixed script rather than an LLM choosing tool calls.

## G20 — Data quality, explainability and trust are named as barriers without being measured

- verdict: partially-addressed
- searched: 20 regex families over all four corpora (44,962 unique records, 38,293 with
  abstracts) covering explainability and interpretability metrics (173 hits), trust
  calibration, data-quality ablation and perturbation (28), explanation faithfulness (6),
  and benchmark-for-trust framings (46); the same narrowed to the 16 earth-science
  `domain_group` values (727, 10, 10 and 2 hits); both grids scanned for explainability,
  trust, data-quality and user-study language; OpenAlex, 8 filtered queries plus 4
  fallbacks; 7 web searches; 2 fetches.
- not searched: arXiv HTTP 429 on all five attempts.
- found: the gap holds inside the two domains. No quantified explainability evaluation, no
  measured trust study and no data-quality-impact experiment for an LLM agent in solid-earth
  or subsurface work was found. `arxiv:2605.03383`, titled "A Coarse-to-Fine Agentic
  Workflow for Explainable Lithology Classification", reports classification accuracy only.
  OpenAlex returns five works in total at the trust × LLM × geoscience intersection.
- found: the methods exist and were harvested, then cut on domain.
  `doi:10.48550/arxiv.2607.26451` (ExplainBench) states "there are no benchmarks that
  evaluate the trustworthiness of agent-generated explanations … allowing quantitative
  comparison of explanation quality between agents" and was screened out as software
  engineering; `doi:10.1080/15623599.2026.2664476` prioritises exactly these barriers by
  Fuzzy AHP in construction; `doi:10.48550/arxiv.2512.19644` surveys 868 scientists who
  program.
- found: one in-corpus geoscience-adjacent source does measure it.
  `doi:10.20944/preprints202606.0566.v1` (`domain_group: engineering_geology`) reports "An
  exploratory ablation study investigated the faithfulness of AI-generated explanations
  using three complementary metrics."
- found: c124's own source is a review, not a measurement — the TANGO run's `screening.csv`
  note calls `doi:10.36227/techrxiv.175979241.11582889/v1` a "position piece on
  explainability as a precondition for agentic AI adoption in subsurface workflows".
- what would change it: a published quantified explainability evaluation, trust survey or
  data-quality experiment for a geoscience LLM agent.

## G21 — Token, API and scheduler cost is named as a limit rather than measured as one

- verdict: refuted
- searched: six cost and scheduling regex families over all four corpora — token-efficiency
  and budget-aware terms (61 hits), cost-benefit and cost-per-unit terms, scheduler terms
  ANDed with agent terms (35), rate-limit terms (37), latency and overhead profiling (36),
  and cost figures intersected with geoscience keywords (0 hits); OpenAlex, 8 filtered
  queries; 7 web searches; 2 fetches.
- not searched: arXiv HTTP 429 on all five attempts.
- found: `arxiv:2603.20253` (SimulCost) is the gap's mirror image and is in neither corpus —
  "the first benchmark targeting cost-sensitive parameter tuning in physics simulations …
  2,643 single-round and 2,304 multi-round tasks across 11 simulators", concluding "LLMs are
  1.5-2.7x slower than traditional scanning, making them uneconomical choices."
- found: c126 quotes its source's motivation as if it were an unresolved limit.
  `arxiv:2609.03598` (RASER) is itself the agent-aware scheduler and reports "reduces
  makespan by nearly 39% compared to static partitioning while achieving near-full CPU
  utilization". It is admitted `in`/`context` — re-checked in this session. A second
  scheduler, `doi:10.1145/3731599.3767584`, is admitted at `context` and evaluates an LLM
  scheduler "against FCFS, SJF, and Google OR-Tools (on 10 to 100 jobs)".
- found: rate-limit cost is measured too. `doi:10.5281/zenodo.21158584` reports enforcement
  "validated across 15 production LLM-integrated applications, $420K annual inference spend
  … 4.2 ms median proxy overhead, 38% aggregate cost reduction".
- found: the TANGO run's own `report/04_evaluation.md` already states that cost "is reported
  surprisingly often and precisely" and lists six per-run figures.
- found: a narrow claim survives. The cost-figures-intersected-with-geoscience pass returned
  0 hits across 38,293 abstracts.
- what would change it: restating the gap as cost unmeasured for agents driving simulators
  in solid-earth geoscience specifically.

## G14 — Authors state human oversight as a standing requirement, not a transitional one

- verdict: partially-addressed
- searched: four autonomy regex families over both triage corpora (46,223 records), each hit
  joined to its `screening.csv` decision — `self-driving lab|autonomous scientist|closed-loop
  autonomous|unsupervised agent` (40+ hits); `no human in the loop|without human
  intervention|zero human intervention|human-free` (77); `fully autonomous|end-to-end
  autonomous|completely autonomous` restricted to the twelve geoscience groups (10);
  `human-out-of-the-loop|unattended|no human (oversight|supervision)|autonomy level|level
  [345] autonomy` restricted to the solver and simulation groups (15); OpenAlex, 7 queries;
  5 web searches; 4 fetches.
- not searched: arXiv and Semantic Scholar HTTP 429 on every attempt.
- found: the landscape run's own deep-read core set contains a system presenting autonomy as
  a validated mode. `arxiv:2512.14429` (specfem-mcp) is `tier: core` with
  `author_stated_limitations: none stated`, and its abstract reads "the workflow operates
  seamlessly in both autonomous and interactive modes, yielding high-fidelity results" —
  both re-checked in this session.
- found: four further systems report unattended operation and none was adjudicated.
  `doi:10.48550/arxiv.2603.27738` (TianJi, "expert-level end-to-end experimental operations
  with zero human intervention") was cut `periphery` by the landscape run and never
  harvested by the TANGO one; `doi:10.48550/arxiv.2603.20986` (AutoMOOSE, "this verification
  arc operates without user intervention") and `doi:10.48550/arxiv.2512.03549` (PARC,
  "sustain progress without human intervention") sit in the TANGO triage unscreened;
  `doi:10.48550/arxiv.2311.10776` was cut `periphery`.
- found: the denominator is small. Of 101 TANGO core systems, 44 carry the
  `human-in-the-loop` tag and 27 state an autonomy-related limitation; of 41 landscape core
  systems, 17 and 5. The gap's 13 candidates are 13 of 142 deep-read systems.
- found: the corpora are genuinely mixed — `doi:10.2523/iptc-25209-ms` claims a "full
  autonomous mode" and a human-in-the-loop mechanism in the same abstract.
- what would change it: full texts of TianJi, AutoMOOSE, PARC and specfem-mcp showing a
  human gate the abstracts omit, plus a restatement scoped to the systems that address
  autonomy at all.

## G15 — Systems are confined to a predefined toolset, workflow or starting artefact

- verdict: refuted
- searched: seven tool-creation and from-scratch regex families over both triage corpora —
  `skill librar|tool creation|creates? (its|their) own tools|self-generated tools|tool
  synthesis|register(s|ing)? new tools|self-evolving tool` (23 hits); `tool generation|
  hand-curated toolset|static toolset|tool library.{0,40}(grow|evolv|expand)` (5);
  `dynamically (generat|creat|synthesi[sz]).{0,40}tools|on-the-fly tool|self-extend` (1);
  `Voyager|open-ended (agent|learning)|lifelong learning agent|tool learning` (40); `from
  scratch` (204) and a scoped variant (89); plus a grid scan of both `papers.csv` over 334
  deep-read rows; OpenAlex, 7 queries; 5 web searches.
- not searched: arXiv and Semantic Scholar HTTP 429 on every attempt.
- found: `doi:10.48550/arxiv.2604.14609` (El Agente Forjador) is a direct refutation and
  frames itself against the gap — "most of the current generation of agentic systems depend
  on static, hand-curated toolsets that hinder adaptation", against which its agents
  "autonomously forge, validate, and reuse computational tools", "Evaluated across 24 tasks
  spanning quantum chemistry and quantum dynamics on five coding agent setups". It carries
  `agentic_score` 14, `scope_computed: core`, and no `screening.csv` row — re-checked here.
- found: two subsurface systems build rather than edit. `arxiv:2603.00214` (JutulGPT) reports
  "autonomous reconstruction of a reference model from progressively abstract textual
  descriptions" against the JutulDarcy reservoir simulator, and sits unadjudicated in both
  runs' triage; `arxiv:2606.09774` (SIGA) "supports adapter self-evolution: prior
  trajectories can rewrite the adapter contents without modifying the underlying agent" on
  GEOS, also unscreened.
- found: `arxiv:2604.12198` reproduces 111 Quantum ESPRESSO papers "from scratch".
- found: the coverage figure behind all of this — 10,354 TANGO triage records are
  `band: A_agentic` and `scope_computed: core`, and 338 of them appear in `screening.csv`.
  Re-derived in this session.
- what would change it: full texts showing Forjador's forged tools come from a fixed
  generator template and that JutulGPT always starts from a retrieved example deck.

## G27 — Verifying what the agent produced is recorded as an unsolved cost

- verdict: refuted
- searched: a verification-and-provenance regex (`verif|validat|provenance|reproducib|
  auditab|attestat|formal method|proof|theorem prover|certif`) ANDed with an agent term and
  an evaluation term over all four triage files (46,225 records with abstracts); a separate
  burden regex (`verification (burden|cost|effort|overhead|tax)|review (time|effort|burden)|
  oversight (cost|burden)|time (spent|taken) (verifying|reviewing)`); `screening.csv` lookups
  for 14 candidate keys in both runs; 2 web searches.
- not searched: OpenAlex HTTP 503, arXiv HTTP 429.
- found: the gap is contradicted from inside the TANGO run's own deep-read set. Two core
  rows carry quantitative verification results — `doi:10.48550/arxiv.2601.09749` (R-LAM),
  "R-LAM scored 1.0 on replay, trace and failure with variance 0.0", and
  `doi:10.48550/arxiv.2608.29665` at M2, "extractor 95.7% precision and 67.3% recall; only
  19 of the 57 studies (33.3%) reproducible in principle". Both tiers and result strings
  re-checked in this session. The gap was extracted from `author_stated_limitations` only
  and never saw the adjacent columns of the same grid.
- found: evaluated tooling exists and sits unscreened in the harvest.
  `doi:10.1145/3731599.3767582` ("an evaluation methodology, reference architecture, and
  open-source implementation … covering diverse query classes and a real-world chemistry
  workflow", `agentic_score` 14, `scope_computed: core`, no `screening.csv` row — re-checked
  here); `arxiv:2607.16646` (a falsification battery "individually sound, so a violation
  certifies a faulty model … Across 326 ground-truth models"); `doi:10.1145/3784828.3785337`
  (semantic-equivalence verification of Fortran and C at "an F1 score of up to 0.913 …
  majority-vote ensembles … 0.972"); `doi:10.48550/arxiv.2605.02651` (ARA, "the highest
  accuracy reported on ReproBench").
- found: the burden has been measured. `doi:10.1073/pnas.2524747123` randomised "288
  researchers to 103 teams" and reports "AI-led teams, which achieved only a 37%
  reproduction rate, detected fewer errors across all categories … and required more time".
  The landscape run's own admitted `doi:10.2118/229603-ms` reports "reducing manual review
  time from 3 hours to less than 5 minutes per well".
- what would change it: a narrower claim — verification tooling exists where a specification
  or reference exists, not where the agent's output is itself the science.

## G29 — Further grid columns the runs could not fill from their sources

- verdict: partially-addressed
- searched: every count re-derived from both grids under a strict `== 'not stated'` match
  and cross-tabulated against `tier`; a loose match adding `not applicable|not specified|
  not named|not described` run against both; `reference/SCHEMA.md` and
  `reference/SCHEMA_tango.md` compared field by field.
- found: all nine counts reproduce exactly, and the cross-tab is the finding. Re-derived in
  this session: in the landscape grid `reported_result` is blank on 0 of 41 core rows and 79
  of 110 context, `tools_used` 0 of 41 and 52 of 110, `evaluation_method` 0 of 41 and 40 of
  110; in the TANGO grid `reported_result` 2 of 101 and 60 of 82, `data_type` 5 of 101 and
  64 of 82, `tools_used` 0 of 101 and 1 of 82. Of 336 blanks across both grids, 11 sit in a
  core row.
- found: the `tools_used` contrast has two causes and neither is a difference in the
  sources. The TANGO run wrote `not applicable` and paraphrases rather than `not stated` —
  the loose match moves its `tools_used` from 1 to 17 and its `evaluation_method` from 0 to
  26, while the landscape figures barely move — and `reference/SCHEMA_tango.md` requires
  that "what it acts on is a simulator, solver, optimiser, scientific code, or an
  engineering or techno-economic model", so a source cannot be admitted to that run without
  its abstract naming the driven artefact. The landscape run has no such requirement.
- found: the emptiness is what `reference/SCHEMA.md` prescribes for abstract-only reading,
  not a hole in the literature.
- what would change it: restating the gap over core rows only, where the residual is
  `data_type` 3 of 41 and 5 of 101, `reported_result` 2 of 101 and `maturity_claimed` 1 of
  101 — small, and genuinely about the sources.

## G03 — The generator model is unnamed in half of one corpus and two fifths of the other

- verdict: refuted
- searched: `base_model` cross-tabulated against `tier` and `access_status` in both grids
  under a bare and a qualified match; 17 regex families over all four corpora (44,962 unique
  records) for reporting-practice meta-research — `reproducib\w*` (1,889 hits),
  `(do(es)? not report|under-?report\w*|rarely report\w*)` (56), `(model (version|name|
  identifier|card)s?|unnamed (llm|model)|model-agnostic)` (207), `(reporting (standard|
  guideline|checklist)s?|PRISMA|reporting quality)` (1,474), a percentage-and-reporting
  pattern (642), and a geoscience-and-reproducibility conjunction (47); Crossref, 5 queries;
  4 web searches; 5 fetches.
- not searched: OpenAlex HTTP 503 on every attempt; arXiv HTTP 429 on all five substantive
  queries after a successful connectivity probe.
- found: the figure is a property of the runs' reading. Re-derived in this session, `tier`
  maps one-to-one onto `access_status`, and the bare `not stated` rate is 6 of 41 core and
  99 of 110 context in the landscape grid, 6 of 101 core and 73 of 82 context in the TANGO
  grid. So 99 of 105 and 73 of 79 unnamed rows were never read past an abstract, and the
  model is named in 85% and 94% of everything read in full. The cross-corpus contrast the
  gap draws is a difference in abstract-only harvest share — 110 of 151 against 82 of 183 —
  not a difference in the literatures.
- found: the landscape run already published the correct core figure that this gap bypassed.
  `report/02_architectures.md` states "Eleven of 41 core rows have `base_model` beginning
  `not stated`", which matches the qualified count re-derived here, and attributes part of
  the residual to venue format rather than to the literature.
- found: most core residuals name a harness rather than nothing — `arxiv:2607.18557` names
  Claude Code and tier-based routing without a model name, `doi:10.5281/zenodo.20543501` is
  model-agnostic by design, `doi:10.1016/j.softx.2025.102367` names GitHub Copilot as the
  client. Six rows per corpus are a bare, unexplained `not stated`.
- found: independent measurement points the other way and was harvested but never screened.
  `doi:10.1186/s13244-026-02236-1` audits 246 studies and reports "Although all studies
  reported LLM's name, only 27.6% (68/246) specified the model version" — present in the
  TANGO `screened.csv`, absent from its `screening.csv`, re-checked in this session.
  `doi:10.1158/1557-3265.aimachine-b021` reports "practically all publications (97.9%)
  reported the used model families … only 27% reported the exact model snapshot", and
  `arxiv:2605.04135` audits 112,303 records and finds "only 3.2% of abstracts (21.2% of
  full-texts) disclose reasoning-mode status".
- found: no study measures model-naming rates in geoscience or simulator-driving agentic
  work specifically; the targeted regexes returned zero.
- what would change it: restating at core tier — 6 of 41 and 6 of 101 bare, 11 and 19
  including qualified statements — which nothing found here refutes.

## G22 — Architectures described, designed or prototyped but not validated

- verdict: confirmed-absent
- searched: named-system regex over all four corpora (46,245 unique records) for each of the
  fourteen candidates; OpenAlex `cites:` queries for 19 identifiers and
  `author.id:…,from_publication_date:…` queries for 9 author groups, to find later work by
  the same teams; Zenodo API; GitHub repo metadata, commits, releases and tags; 10 web
  searches; 5 fetches.
- not searched: arXiv HTTP 429 on every attempt; OpenAlex anonymous *search* was paused
  mid-session, so DOI resolution and non-search filters were used instead.
- found: no later publication, release or evaluation validates any of the fourteen named
  architectures. Ten have zero citations; the four with citations are cited only by
  unrelated third-party systems.
- found: the three plausible leads each fail on inspection. `arXiv:2608.30186` validates the
  PUR-1 cyber-physical digital twin and "does not mention 'PUR-1 GPT,' a large language
  model, an LLM agent, or a semantic layer"; the LARA group's later
  `doi:10.48550/arxiv.2606.29100` uses a different testbed and never mentions the critical
  review phase; the mining review's own implementation, `doi:10.3390/mining6020026` (MINDS),
  is still "A proof-of-concept using the Marvin copper benchmark".
- caveat recorded rather than resolved: eleven of the fourteen were published within the
  last 4 to 16 months, so absence of a follow-up is short-horizon evidence.
- what would change it: a v2 of the Agentic Optimizer record reporting a field case; a LARA
  follow-up implementing the critical-review phase; or a mining LLM-agent paper reporting
  deployment on an operating mine rather than the Marvin benchmark.
- note on the evidence line: `SCHEMA_gaps.md` requires query ids for `confirmed-absent`, so
  `gaps.md` cites the core harvest cells that built the corpora this pass searched. The
  search that actually established the absence was a citation-graph sweep (OpenAlex `cites:`
  over 19 identifiers and `author.id:` over 9 author groups), which has no query id in
  either run's `queries.csv`.

## G25 — The agent drives a named subset of its engine, with the rest recorded as not yet covered

- verdict: partially-addressed
- searched: named-system and coverage-claim regex over all four corpora, including `full
  (range|set) of (calculations|capabilit|features|solvers|modules)`, `complete control over
  the`, `entire (feature|capability|API|command set)`, `exposes (the )?(entire|all|complete)`
  and `all (unit operation|solvers|modules|commands)`; OpenAlex `cites:` and author queries;
  GitHub releases, tags, READMEs and `docs/TOOLS.md` for seven repositories; Zenodo API;
  10 web searches.
- not searched: arXiv HTTP 429 throughout.
- found: one counterexample inside the TANGO run's own deep-read core set.
  `doi:10.48550/arxiv.2602.04850` (El Agente Quntur) states "Quntur supports the full range
  of calculations available in ORCA 6.0", its `papers.md` extract reads "These strategies
  grant Quntur complete control over the ORCA 6.0 quantum chemistry package", and its
  recorded limitations concern geometry reasoning rather than engine coverage. All three
  were re-checked in this session. `doi:10.5281/zenodo.20543501` (OASiS) and
  `doi:10.48550/arxiv.2604.14609` point the same way.
- found: no candidate has closed its own stated gap. petromcp is at release 0.8.1
  (2026-08-03) with its README still reading "`segyio` queued for a later slice";
  ESHM20-MCP is at v1.0.0 with "`run_fast` loads the top-3 ASM + top-2 FSM logic-tree
  branches (by weight)" and 20 km area discretisation against the official 10 km;
  Aspen-MCP's `docs/TOOLS.md` still offers steady-state cases only; GENIUS's journal version
  (`doi:10.1038/s43246-026-01167-0`, 2026-04-28) still translates prompts into Quantum
  ESPRESSO input files with the knowledge graph covering only pw.x; GAGAW's repository was
  last committed 2026-01-21 with joint and coupled inversion still unintegrated.
- found: the systems that do reach full coverage are quantum-chemistry and FEM agents. No
  geoscience-engine agent in either corpus claims full coverage.
- found: two harvest misses recorded independently of the verdict — the GENIUS journal
  version and `arXiv:2609.03718` are in neither corpus.
- what would change it: restating the gap as a per-system pattern with Quntur named as the
  counterexample, rather than as an absence.

## G07 — Most of both admitted corpora was never read beyond an abstract

- verdict: partially-addressed
- searched: all three counts re-derived from both grids; `paywalled.md` row structure
  counted; `unreachable.md`'s four recovery passes read; `subfield` and
  `subfield_secondary` cross-tabulated against `tier`; arXiv searched for agentic
  full-waveform and geophysical-inversion systems the runs might have missed.
- found: the counts are exact — 110 of 151 and 82 of 183 `context`/`abstract-only`, and
  `inversion` has 2 admitted rows and 0 core. All re-derived in this session.
- found: `tier` and `access_status` are perfectly collinear in both grids, so c120 and c298
  are one measurement each rather than two corroborating facts.
- found: the TANGO figure is mostly a tiering decision, not an access failure. Of its 82
  unread rows, 28 are the blocked list in `paywalled.md` and 55 are `context`-by-decision —
  reviews, surveys, conference abstracts, vendor pages and benchmarks the protocol never
  intended to deep-read, which `paywalled.md` separates out explicitly ("None of these was
  blocked … none belongs in the count of what credentials would fix"). Re-derived here: 31
  table rows and 55 by-decision bullets, with one record on both lists.
- found: c119 is an artefact of re-subfielding, not of `inversion` going unread. Three
  records that had carried `subfield: inversion` were deep-read in the recovery passes and
  moved — `doi:10.1016/s1876-3804(26)60734-3` and `doi:10.1016/j.petsci.2026.05.031` to
  `reservoir_engineering`, `doi:10.1016/j.bdes.2026.100042` to `hydrogeology` — and four
  core rows still carry `inversion` as `subfield_secondary`. Re-derived in this session.
  arXiv carries no agentic inversion system the runs missed, so the thinness is real but not
  caused by unread sources.
- what would change it: naming only the access-driven residual and restating c119 as a
  label that shrank because deep reads reassigned it.

## G08 — Named sources neither run could read, and what each records as the cost

- verdict: partially-addressed
- searched: 31 of 31 blocked rows checked for a non-empty cost statement; 13 DOIs probed
  hardest across roughly ten routes each — OpenAlex `best_oa_location`, Semantic Scholar,
  Crossref `link` and `license`, OpenAIRE, Europe PMC, OSTI, Figshare and Zenodo APIs,
  ChemRxiv public-api and asset gateway, DOAJ, institutional repositories, arXiv
  title/abstract search, and a reader proxy; Unpaywall refused the shared test address and
  was substituted by OpenAlex; fatcat was unreachable.
- found: one blocked source is obtainable and the agent read it.
  `doi:10.3778/j.issn.1673-9418.2508051` is recorded `blocked_by: no-full-text-anywhere`,
  but DOAJ carries a live publisher PDF link that served 2.3 MB over ranged requests at
  about 4 KB/s. The text answers the run's own stated `would_change` — it reports
  "AutoCode4OF achieves scores of 0.956, 0.997, and 100% in code quality, functional
  completeness, and compilation success rate" against direct OpenFOAM command-line results,
  so the generated cases were run.
- found: a blocked EAGE record has an open companion the runs already harvested.
  `doi:10.3997/2214-4609.202637165` is recorded as having no substitute in the corpus, but
  `arxiv:2603.00214` (JutulGPT, the same four authors, the same system on JutulDarcy) sits
  in both runs' `triage.csv` and `screened.csv` at `band: A_agentic`, `agentic_score` 10,
  with no `screening.csv` row and no `papers.csv` row in either run — re-checked in this
  session. In the landscape run it carries `scope_computed: none`; in the TANGO run
  `scope_computed: core` with `first_seen_run` 2026-09-11, after screening had run.
- found: one `blocked_by` value is wrong in kind. `doi:10.1145/3785462.3815873` is a CC-BY
  4.0 version of record labelled `paywall`; every ACM route returned HTTP 403 and the reader
  proxy hit a Cloudflare interstitial. The fix is a browser, not credentials.
- found: the rest of the list holds. Blockage was re-confirmed for 12 of the 13 probed DOIs,
  including c130's survey (IEEE returns HTTP 202 with an empty body, ResearchGate 403). The
  Zenodo tombstone (HTTP 410 Gone) and the Figshare dataset-only classification are both
  recorded correctly.
- what would change it: correcting the one readable row, re-screening the EAGE record
  against `arxiv:2603.00214`, and re-testing the openly-licensed but bot-blocked rows — the
  ACM CC-BY paper, two gold-OA Elsevier papers and four ChemRxiv preprints whose own
  advertised OA PDF URLs refuse automated clients — in a real browser, which would recast
  the list as sources no automated client can read.

