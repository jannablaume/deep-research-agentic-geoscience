# Gaps the finished runs already contain

What `outputs/01_landscape/v0.5` and `outputs/02_tango/v0.2` record as absent,
unstated, unevaluated, unread or empty, at commit `e7010e1`.

Every gap traces to a `candidate_id` in `gap_candidates.csv`.

Every verdict was returned by a verification pass recorded in `verification.md`.

Synthesis only. Nothing below ranks these gaps or says what to do about them.

## G01 — Neither corpus states whether its evaluation data was held out

- candidates: c095; c102; c248; c255
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: arxiv:2606.09774; doi:10.1190/tle44020114.1; arxiv:2605.17792; arxiv:2608.01369
- checked: 2026-09-11

[Certain] `held_out` is the emptiest evaluation column in both grids. In the landscape run
134 of 151 admitted sources state nothing for it, and 30 of the 41 deep-read systems report
no held-out evaluation. In the TANGO run 110 of 183 admitted sources state nothing for it,
and 79 of the 101 deep-read systems report none. The two runs read different literatures
and record the same proportion of silence: in both, the majority of even the full-text tier
does not say whether the problems it was evaluated on were separated from whatever the
system was built or tuned on.

[Certain] **Refuted as stated.** Both grids do record held-out evaluation where a source
reported it: `held_out` is `yes` on 16 of 151 admitted landscape rows (11 of 41 core) and
23 of 183 admitted TANGO rows (22 of 101 core). The verification pass also found four
in-scope records reporting held-out evaluation that were harvested and cut before
screening, among them `arxiv:2606.09774`, whose abstract reports held-out tasks on the GEOS
subsurface simulator and which carries `agentic_score` 0 in the TANGO triage. The two runs
also record the absence differently: of the 11 sources in both grids, 3 are `not stated` in
01 and `no` in 02, and 01 records `no` once in 151 rows against 02's 50 in 183.

## G02 — A quarter to a third of deep-read systems report no baseline

- candidates: c094; c101; c247; c254
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: arxiv:2606.09774; doi:10.48550/arxiv.2603.04756; doi:10.48550/arxiv.2606.10752
- checked: 2026-09-11

[Certain] 84 of 151 admitted landscape sources state nothing for `baseline`, and 6 of the
41 deep-read systems compared against none. 47 of 183 admitted TANGO sources state nothing,
and 12 of the 101 deep-read systems compared against none. In those rows the reported
result is the system working, with no stated comparison of any kind — not a human, not a
classical solver, not another agent, not an ablation of itself.

## G03 — The generator model is unnamed in half of one corpus and two fifths of the other

- candidates: c091; c245
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.1186/s13244-026-02236-1; doi:10.1158/1557-3265.aimachine-b021; arxiv:2605.04135
- checked: 2026-09-11

[Certain] 105 of 151 admitted landscape sources and 79 of 183 admitted TANGO sources state
nothing for `base_model`. The column records which language model produced the behaviour
the source reports, and in both grids it is blank more often than it is filled.

[Certain] **Refuted as stated.** Both grids map `tier` one-to-one onto `access_status`, and
the blank rows are almost all abstract-only: 6 of 41 core and 99 of 110 context in the
landscape grid, 6 of 101 core and 73 of 82 context in the TANGO grid. The landscape run's
own `report/02_architectures.md` already states the core figure, "Eleven of 41 core rows
have `base_model` beginning `not stated`". A reporting audit of 246 studies harvested by
the TANGO run but never screened records that "all studies reported LLM's name, only 27.6%
(68/246) specified the model version".

## G04 — Most admitted sources state nothing about code availability

- candidates: c100; c253
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.48550/arxiv.2504.06260; doi:10.48550/arxiv.2507.14267; doi:10.1016/j.taml.2025.100594
- checked: 2026-09-11

[Certain] `code_availability` is `not stated` for 127 of 151 admitted landscape sources and
for 110 of 183 admitted TANGO sources. Neither grid records a repository, a licence or a
statement of unavailability for those rows.

## G05 — No system in either corpus demonstrates maturity above M3

- candidates: c239; c242; c104; c257
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.2118/0426-0008-jpt; doi:10.1145/3748636.3764602; doi:10.2118/233425-ms; doi:10.2118/229325-ms
- checked: 2026-09-11

[Absent-searched] The TANGO run states, backed by query cells `q001`–`q014`, that nothing
in its corpus reaches M4 or M5: no source shows a system in routine use by people other
than its authors, or an output that entered a real operational decision with third-party
evidence, and its 12 M3 rows are retrospective work against references the authors did not
produce. Of its 101 deep-read systems, 41 demonstrate M1 or below and 12 reach M3 or above.
The landscape run's deep-read tier has the same shape at a different scale: 14 of 41
systems demonstrate M1 or below and 14 reach M3 or above.

[Certain] **Refuted as stated.** The verification pass found an operator deployment inside
the landscape corpus. `doi:10.2118/0426-0008-jpt` is `tier: context` with
`access_status: abstract-only` and `maturity_demonstrated: not stated (abstract only)`,
while its open full text describes an agentic framework deployed for ONGC driving SLB's
Pipesim engine over roughly 600 wells and 370 scenarios across three fields, checked
against models production engineers rebuilt by hand. Three further admitted records carry
deployment language under the same abstract-only rating, and two more —
`doi:10.1145/3748636.3764602` (deployed at USGS) and `doi:10.2118/229325-ms` (ADNOC) —
reached `scope_computed: core` in triage and have no `screening.csv` row. The M5 half
stands: a 166-hit search for third-party or independent evaluation returned nothing in
scope, and the one verification found is internal to the deploying organisation.

## G06 — No source reports its agent's output being acted on outside the experiment and later found wrong

- candidates: c243
- runs: 02_tango/v0.2
- verdict: confirmed-absent
- evidence: q001; q014
- checked: 2026-09-11

[Absent-searched] The TANGO run states, backed by query cells `q001`–`q014` and eighteen
targeted web searches, that no admitted source reports a case where its agent's output was
accepted, acted on outside the experiment, and later found to be wrong. Failures in that
corpus are reported as run-time errors caught inside the loop, as benchmark cases not
passed, or as capability gaps the authors defer — never as a downstream consequence.
The run records one source that comes closest and marks the boundary: hallucinated PDB IDs
were accepted by the pipeline and molecular dynamics ran on the wrong protein structures
before the authors identified them, inside their own experiment.

## G07 — Most of both admitted corpora was never read beyond an abstract

- candidates: c120; c298; c119
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.1016/s1876-3804(26)60734-3; doi:10.1016/j.petsci.2026.05.031; doi:10.1016/j.bdes.2026.100042
- checked: 2026-09-11

[Certain] 110 of 151 admitted landscape sources and 82 of 183 admitted TANGO sources were
never read beyond an abstract, so nothing in them contributes to any characterisation
either run makes. In the landscape run the effect reaches a whole subfield: `inversion` has
two admitted sources and neither was deep-read, so nothing in it is characterised beyond an
abstract.

## G08 — Named sources neither run could read, and what each records as the cost

- candidates: c299; c300; c301; c302; c303; c304; c305; c306; c307; c308; c309; c310; c311; c312; c313; c314; c315; c316; c317; c318; c319; c320; c321; c322; c323; c324; c325; c326; c130
- runs: 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.3778/j.issn.1673-9418.2508051; arxiv:2603.00214; doi:10.1145/3785462.3815873
- checked: 2026-09-11

[Certain] `paywalled.md` records, per blocked source, what reading it would have changed,
and the entries are specific rather than generic. Several name evidence with no substitute
in the corpus: the only head-to-head comparison of three MCP server designs
(`doi:10.3997/2214-4609.202639027`); the only source reporting calibrated coverage against
a human-expert pipeline on the same search (`doi:10.1016/j.net.2026.104573`); hash-verified
run specifications rejected before scheduling (`doi:10.1145/3785462.3815873`); the only
source whose central claim is that the agent should be kept out of the execution loop
(`doi:10.26434/chemrxiv.15002405/v1`); a 6,156-run agentic benchmark whose orchestration
modes sit in unreadable chapters (`title:agenticaienabled…`); a source whose agent-proposed
candidate was synthesised and measured (`doi:10.6084/m9.figshare.30931802`); and a
closed-loop campaign of 300 simulator evaluations whose reported non-monotonic convergence
is discussed only in the unreadable body (`doi:10.2139/ssrn.6942178`). Other entries record
that reading would change nothing or little, naming reviews, surveys and a predecessor
deposit already in the grid under the same `system_id`. One further source carries an
explicit limitations section that the run records as unread because the full text is
blocked (`Goyal2026-agentic-dt-survey`).

## G09 — `instrument-control` appears on no deep-read landscape row

- candidates: c089
- runs: 01_landscape/v0.5
- verdict: confirmed-absent
- evidence: q001; q020
- checked: 2026-09-11

[Absent-searched] The landscape run states, backed by query cells `q001`–`q020`, that
`instrument-control` does not appear on any core row. The technique is in the controlled
vocabulary and no deep-read system in that corpus carries it.

## G10 — No agent drives a life-cycle economic model as the system it controls

- candidates: c238; c240
- runs: 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.3390/en18215632; doi:10.54097/3dwqbf59; arxiv:2606.26346
- checked: 2026-09-11

[Absent-searched] The TANGO run states, backed by query cells `q007`–`q010` and eighteen
logged web searches, that no admitted source drives a full life-cycle cost model —
levelised cost of energy, discounted cash flow, or a comparable economic model — as the
system it controls. Economic quantities appear in that corpus as objectives inside
optimisation loops rather than as the driven artefact, and `techno-economic` is its
smallest non-empty touchpoint at 7 rows and 6 core.

[Certain] **Refuted as stated.** The TANGO run harvested `doi:10.3390/en18215632`, "An AI
Agent for Techno-Economic Analysis of Anaerobic Co-Digestion in Renewable Energy
Applications", triaged it `band: A_agentic`, `scope_computed: core`, `llm_present: yes`
with the `techno_economic` touchpoint attached, and never screened it; the landscape run
cut the same DOI as `not-geoscience`. Of 135 triage rows carrying that touchpoint, 3
reached `screening.csv`. The narrow reading survives: every counterexample found is in
bioprocess, chemical, power-market or generic-energy work rather than solid-earth
geoscience.

## G11 — Geometry, meshing and spatial reasoning are named as an unresolved limit across domains

- candidates: c011; c042; c153; c167; c170; c175; c196; c216; c225
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.48550/arxiv.2509.18178; doi:10.2139/ssrn.7083227; doi:10.48550/arxiv.2511.00122; doi:10.1016/j.ijheatfluidflow.2026.110399
- checked: 2026-09-11

[Certain] Authors in both corpora record the same limit in their own words. Meshing complex
reservoirs "is particularly challenging and warrants a dedicated specialized agent"
(Agents4GEOS, recorded in both runs); errors requiring "a deeper understanding of the
underlying physics, which the agent currently lacks" are the ones the agent cannot repair,
so "human oversight remains essential"; general-purpose models "still exhibit unreliability
when constructing complex geometries and generating meshes, struggling with curved
boundaries"; the most significant limitation "arises during geometry generation"; generated
geometries are limited in quality and controllability; a benchmark is restricted to simpler
geometries without CAD imports; complex geometries and boundary conditions defeat one CFD
framework; and a slope-reliability framework reports defective geometry and meshing among
the simulation-level failures it can only surface through tool diagnostics.

## G12 — A run that executes is not a run that is physically right, and the corpora record that the second is not checked

- candidates: c058; c061; c063; c132; c142; c150; c172; c199; c212; c220; c229; c235
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.48550/arxiv.2605.09360; doi:10.26434/chemrxiv.15007535/v1; doi:10.48550/arxiv.2603.20986; doi:10.48550/arxiv.2606.07850
- checked: 2026-09-11

[Certain] Authors in both corpora state that syntactic and execution success does not
establish physical correctness. Language models "excel at high-level linguistic narration
but consistently struggle to enforce the complete chain of physical constraints within the
generated executable code"; one source breaks its 49% failing cases into 10% semantically
misaligned but runnable and 32% terminating on divergence or unphysical results; one system
has no "built-in ability to verify whether the predicted" values are right; LLM-based
verification "is not a physical guarantee" and unsupervised automated assignments "could
propagate errors"; acceptance criteria are "screening-oriented heuristics" that "do not
constitute a replacement" for the real check; static consistency checks are stated as
insufficient for validating the underlying physics; and systems are recorded as operating
"without inherent grounding in physical feasibility", able to produce plausible but
non-physical output. Two sources state the ceiling as a property of the wrapped engine
rather than the agent: efficacy "remains intrinsically bounded by the fidelity of
underlying physical models", and an implementation that "does not aim to supplant the rigor
inherent in ab initio methods".

## G13 — Hallucination is recorded as present and unresolved rather than eliminated

- candidates: c032; c033; c036; c088; c123; c125; c143; c157; c192
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.26434/chemrxiv.15006587/v1; arxiv:2605.11234; doi:10.48550/arxiv.2608.30696
- checked: 2026-09-11

[Certain] Both corpora carry sources naming hallucination as a live property of the
deployed system. It is named as "a key challenge for tasks requiring precise intent"; as
something that persists in one model despite cost-efficiency; as a tendency that "worries
linger" about; as a risk mutually conflicting with human oversight and real-time
adaptability; as a knowledge gap alongside limited data and tool access; as errors that
"often present as structurally coherent" output; as a likelihood "when multiple requests
are given in a single query"; and as subtle errors in generated tool code "undetected until
runtime". None of these rows records the failure mode as closed.

## G14 — Authors state human oversight as a standing requirement, not a transitional one

- candidates: c001; c027; c031; c081; c087; c145; c163; c165; c179; c190; c195; c198; c223
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: arxiv:2512.14429; doi:10.48550/arxiv.2603.27738; doi:10.48550/arxiv.2603.20986; doi:10.48550/arxiv.2512.03549
- checked: 2026-09-11

[Certain] Across both corpora, authors record that the system is not autonomous and in
several cases that it should not be. Automation is stated as operating "only within
controlled boundaries" with validation and supervision under user control; AI "cannot and
should not replace a drilling engineer or automate the entire drilling cycle"; the system
"does not replace engineering judgement"; autonomy "should be granted only where the task
is repeatable, auditable"; one multi-agent system "is not totally autonomous end-to-end"
because it depends on a human termination step; one framework "functions predominantly in a
co-pilot modality"; one is "intentionally designed to avoid autonomous decision-making in
areas requiring physical judgment"; one is "currently a semi-automated intelligent
assistant"; one "does not reach the fully autonomous Level 3"; one is "designed to augment,
not replace, the established tools of the trade"; one explicitly disclaims being an
autonomous system or a replacement for Competent Persons; one reports that a robust ability
for optional human feedback "was not achieved"; and one states that "a measure of human
oversight remains critical to ensure correctness".

## G15 — Systems are confined to a predefined toolset, workflow or starting artefact

- candidates: c012; c035; c046; c047; c086; c138; c171; c181; c202; c224; c226; c227
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.48550/arxiv.2604.14609; arxiv:2603.00214; arxiv:2606.09774; arxiv:2604.12198
- checked: 2026-09-11

[Certain] Authors in both corpora record that what looks like an open-ended agent is bounded
by what someone prepared in advance. Operation is "strictly confined to a predefined
toolset, preventing agents from independently writing or debugging new scripts to handle
unexpected issues"; one system "relies on predefined workflows and expert rules, limiting
autonomous generalization under completely unknown geological conditions"; one "operates
within a predefined conceptual model and does not independently revise stratigraphic
interpretations, modify facies distributions, or adjust boundary conditions"; engineers
"must prepare examples and manually update tools for new design logic"; the queries behind
each tool "are hand-written so the model cannot go off-script"; knowledge "is encoded
procedurally in prompts and tools, limiting the ability of agents to adapt across tasks";
the workflow "was pre-defined in the prompts for this case study"; operator selection "is
still manual"; tool-call setup "still requires tailoring … depending on the task"; and three
building-energy sources record that the work begins from an existing model — a
"pre-existing baseline IDF, assuming that building geometry and HVAC topology are already
defined", a geometry "already established", and a tool set that "focuses on model analysis
and modification rather than complete model creation from scratch".

## G16 — Evaluations are narrow by the authors' own account: one site, one platform, one small set

- candidates: c020; c026; c028; c060; c078; c084; c137; c141; c148; c154; c164; c187; c189; c201; c228; c230; c237
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: arxiv:2604.03460; arxiv:2605.08941; arxiv:2605.09636; doi:10.20944/preprints202606.1410.v1
- checked: 2026-09-11

[Certain] Authors in both corpora state the narrowness of their own evidence and often give
its dimensions. A dominant limitation is a dataset of n=102 with 21 test cases; "the limited
sample size necessitates comprehensive validation on larger, more diverse datasets before
deployment recommendations"; evaluation "remains preliminary" and the case studies "do not
exhaust the range of geological and engineering scenarios"; validation "demonstrates
precision within a specific problem class" and a production release "will require
systematic validation"; a solver supports "only scalar heat equations"; benchmark problems
"are limited to Beams2D and Photonics2D"; an ablation is "limited to six regular benchmark
cases"; validation sits "within a limited set of platforms primarily CityLearn V2"; the
work is "a single-institution case study"; the evaluation "covers one application and one
workflow management system"; the evaluation is "at small to moderate scale on
representative workflows rather than large long-running pipelines"; demonstrations used "a
relatively simple residential model with three thermal zones"; "Six buildings in a single
climate zone (CZ5A) constrain statistical representativeness"; interpretation is shown "only
with limited data availability"; further real-world testing "across diverse geological
settings will be essential"; the remaining gap to peer-reviewed work "lies mainly in
experimental depth and evidence maturity"; and a vendor states that full-field history
matching with 200 wells "still needs other solutions".

## G17 — Sources that state no limitations at all, and grids that record the field as empty

- candidates: c024; c037; c044; c076; c082; c099; c149; c158; c186; c203; c205; c208; c252
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.48550/arxiv.2505.10852; doi:10.48550/arxiv.2509.18178; doi:10.48550/arxiv.2512.14429
- checked: 2026-09-11

[Certain] `author_stated_limitations` is `not stated` for 63 of 151 admitted landscape
sources and 66 of 183 admitted TANGO sources. Among deep-read sources the runs record the
absence individually: one seismology source states "none … the Conclusion and Outlook
contains only forward-looking statements about future capability"; three have "no
limitations section" or "no dedicated limitations section", with the nearest thing being a
remark about where residual errors concentrate; two state "essentially no limitations,
offering only future directions" and "essentially no limitations, framing the gaps as
extensions"; one "concede[s] very little — the only qualifiers are conditional"; one
two-page extended abstract has "no limitations or future-work text" in existence; one names
"future scope" instead of limitations; and one records the nearest qualifications as
"framing rather than limitation".

## G18 — Both runs record sources whose stated claim reaches past the maturity their evaluation demonstrated

- candidates: c105; c106; c107; c108; c109; c110; c111; c112; c113; c114; c115; c116; c117; c118; c258; c259; c260; c263; c265; c266; c267; c268; c269; c271; c272; c273; c274; c275; c276; c277; c278; c279; c280; c281; c282; c283; c284; c285; c286; c287; c291; c292; c293; c294; c295; c296; c297
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.48550/arxiv.2512.14429; doi:10.48550/arxiv.2508.07035; doi:10.48550/arxiv.2606.07850; doi:10.48550/arxiv.2604.11945
- checked: 2026-09-11

[Certain] Both grids carry `maturity_claimed` alongside `maturity_demonstrated`, and 47
rows rated M0 or M1 assert something the evaluation section did not show. The assertions
take three recurring forms. Disciplinary primacy: "the pioneering effort in building an
agentic AI system for geothermal project assistance"; "the first application of MCP
technology to computational seismology"; "the first novel and open-source Model Context
Protocol server for EnergyPlus". A new paradigm or transition: "a blueprint for
transitioning the industry from isolated legacy software to an interoperable, AI-ready
ecosystem"; "establishes a new paradigm for surrogate modeling"; "marks a new paradigm for
autonomous scientific exploration"; "exemplifies a rapid shift toward agentic computational
chemistry". Industrial or production readiness: "a practical and scalable alternative to
classical optimization for long-horizon industrial scheduling"; "demonstration of
production-grade reliability for the full agent stack"; "an open-source platform that fully
automates VASP workflows"; "a viable approach for realistic subsurface flow applications";
"can systematize economic scenario analysis without sacrificing the governance and
verification required for definitive feasibility studies"; "the stability required for
materials research". One row records a claim its own tables contradict: the abstract states
"deviations under 1.5% compared to reference" solutions, "a figure three of the eight
max-displacement entries in its own Table 9 exceed".

## G19 — Neither run read its periphery, and one names topics it never harvested

- candidates: c090; c244
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: arxiv:2605.17792; doi:10.31223/x5f47g; doi:10.1111/faf.70079
- checked: 2026-09-11

[Absent-searched] The TANGO run states, backed by query cells `q015`–`q022`, that beyond
six boundary records no periphery record was read, so it can say nothing about what the
software-engineering or laboratory-automation literatures contain beyond their size and
group labels; those cells were harvested and triaged but never screened. The landscape run
states, backed by `q005`, `q006` and `q021`–`q030`, that no dedicated periphery harvest was
run for hydrology-as-surface-water or ecology, and that those topics appear only where they
matched a core or named-periphery query.

## G20 — Data quality, explainability and trust are named as barriers without being measured

- candidates: c006; c008; c017; c019; c030; c049; c053; c054; c055; c062; c066; c071; c072; c122; c124; c134; c135
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.20944/preprints202606.0566.v1; doi:10.48550/arxiv.2607.26451; doi:10.48550/arxiv.2503.15511
- checked: 2026-09-11

[Certain] Both corpora carry sources — predominantly on the abstract-only tier — that name
the same set of obstacles in general terms. Recorded are: "limited foundational
understanding, skepticism about AI reliability and a lack of standardized practices";
"data quality, QA/QC protocols, inconsistent data standards and concerns around trust and
explainability"; "data scarcity, interpretability issues, scalability and
trustworthiness"; "data governance, explainability, cybersecurity and integration with
operational technology"; "data quality, model interpretability, and the need for
high-performance computing resources"; "reliability, robustness, evaluation, and human
oversight"; "bias and fairness"; "lack of explainability as the major barrier to adoption
in high-stakes decision-making"; "data resolution, uncertainty, and spatial coverage";
"project-level access controls … heterogeneous geospatial references … transparency";
"extreme label scarcity in a positive-unlabeled setting, spatial non-stationarity that
violates i.i.d. assumptions, and multi-format data heterogeneity"; "the need for skilled
professionals"; "data privacy and algorithm optimization issues"; and one framework that
"envisions incorporating explainable AI but that this is not implemented".

## G21 — Token, API and scheduler cost is named as a limit rather than measured as one

- candidates: c040; c056; c065; c126; c129; c173
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: arxiv:2603.20253; arxiv:2609.03598; doi:10.1145/3731599.3767584; doi:10.5281/zenodo.21158584
- checked: 2026-09-11

[Certain] Both corpora record cost and infrastructure mismatch as author-stated limits. One
source names "increased computational overhead from multi-step execution and iterative
refinement, which may result in higher inference latency and resource usage"; one names
"token limitations in interacting with the LLM"; one states its offline search cost is
"substantially more expensive than running a fixed hand-designed solver"; one states that
"traditional HPC job schedulers such as Slurm are not designed for dynamic, agentic
workflows"; one states that "API rate limits highlight the mismatch between parallel
computational workflows and sequential API processing"; and one names "expensive
computation at city-scale".

## G22 — Architectures described, designed or prototyped but not validated

- candidates: c002; c010; c021; c022; c051; c064; c067; c073; c121; c128; c136; c146; c162; c185
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: confirmed-absent
- evidence: q001; q014; q020
- checked: 2026-09-11

[Certain] Both corpora carry sources whose authors state that what is reported is a design
rather than a validated system. The architecture "is conceptual and is intended as a
scalable design pattern rather than a validated field case", recorded in both runs;
"mining-specific LLM-agent implementations are largely conceptual and await empirical
validation"; the work was "developed as a rapid proof of concept within eight weeks"; the
example is "deliberately conceptual and not conditioned on observational data"; a
"proof-of-concept implementation focused only on stuck pipe"; "ongoing research progress"
with real-time data and digital twins recorded as not yet done; work that "still needs to be
scaled up to support industrial use"; a "present implementation remains a proof-of-concept";
a pipeline realised "only up to the validation phase" with the critical review phase "not
implemented end to end"; open decision-making algorithms that are "very limited for
experimental scenarios"; existing digital twin systems with "limitations in responding to
dynamic environments"; concerns that operating "in the wild" raises about sensor
variability, communication delays and regulation; and one source in which two architectures
"were tested in separate scenarios" and the hybrid design named in its own conclusion "was
not evaluated".

## G23 — No shared or third-party benchmark, and no agreed way to score these systems

- candidates: c023; c131; c155; c211; c214; c218; c241
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: arxiv:2505.19897; arxiv:2510.21652; doi:10.48550/arxiv.2410.05080; doi:10.48550/arxiv.2409.11363
- checked: 2026-09-11

[Absent-searched] The TANGO run states, backed by query cells `q001`–`q006` and
`q011`–`q014` and eighteen targeted web searches, that no benchmark in its corpus is shared
across domains and no admitted source proposes or uses a cross-domain evaluation of agents
driving scientific codes. Authors in both corpora record the same absence from inside.
"Petroleum benchmarks are scarce; reservoir and production sub-disciplines lag"; the field
"remains limited by the scarcity of high-quality datasets and benchmarks, especially for
knowledge discovery"; "no automated CFD-paper rubric scores these workflows so
cross-framework comparison is manual"; establishing appropriate human references "is
non-trivial because performance depends strongly on the evaluator's domain knowledge and
experience, which are difficult to standardize and quantify"; one source "does not claim
state-of-the-art performance or present exhaustive cross-system leaderboards"; and one
benchmark "uses reference-ligand-derived centers and computational proxy metrics" rather
than experimental outcomes.

## G24 — Open-weight and smaller models are recorded as failing where frontier models do not

- candidates: c059; c152; c191; c197; c204; c221
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: arxiv:2601.05187; doi:10.26434/chemrxiv-2024-9g2w2; arxiv:2605.24844; doi:10.1016/j.acags.2025.100311
- checked: 2026-09-11

[Certain] Both corpora record the same measured split by model. "The 14B cannot write a
single working script in the 20-task suite (0/19 in the definitive run); the 32B manages
3-4/19"; qwen3:4b "possesses usable semantic competence but severe structural fragility
necessitating rigid programmatic gates"; "locally deployed smaller models such as QwQ-32B
struggled with generating valid solver files for complex processes"; performance "degrades
on more complex systems, particularly magnetic materials where all models exhibit pass rates
below 6%"; one framework "lags slightly behind the proprietary models"; and "open-source
multimodal LLMs (e.g. Qwen2.5-VL) still exhibit a noticeable gap in image recognition
capability".

## G25 — The agent drives a named subset of its engine, with the rest recorded as not yet covered

- candidates: c003; c005; c007; c013; c016; c052; c075; c085; c127; c144; c147; c169; c176; c177; c183; c193; c207; c215; c219; c231; c233; c234
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.48550/arxiv.2602.04850; doi:10.5281/zenodo.20543501; doi:10.48550/arxiv.2604.14609
- checked: 2026-09-11

[Certain] Authors in both corpora name the part of the engine, method space or vocabulary
their system does not reach. Joint and coupled inversion methods are "not yet integrated"
and geophysics coverage is "narrow, centered on ERT, seismic refraction, and basic climate
linkage", recorded in both runs; default branch subsets "do not cover every authorized
ESHM20 logic-tree branch"; SEG-Y support "is only queued and not yet implemented"; the
interface "currently targets steady-state simulation" and component definition "relies in
part on workarounds"; the system "is currently not able to fully cope with the analysis of
complex thermodynamic systems"; the framework "focuses on assembly and annotation workflows
for isolate microbial reads and does not cover the full diversity of analysis types";
limitations remain "for more complex simulations", naming multiphase and compressible flow;
"less commonly documented formulations such as stress minimisation with constraint
aggregation" are handled only by conditionally adding references; the knowledge graph
"covers only" part of its intended scope; methodological coverage is to be expanded to
"excited-state methods, explicit solvation and finite-field approaches"; model accuracy
"degrades above 1 GHz due to simplified geometric assumptions"; a selectivity prediction
"underestimates experiment because the multi-path KMC is not yet coupled"; the vocabulary is
"terrestrial-biased and misapplies Earth-centric terms"; the framework "does not directly
simulate slope stability or hydrological processes"; the system "does not adopt multiple
forward-backward algorithms for autonomous rollback" and "does not automatically switch to
backup models"; "advanced data mining and pattern discovery remain limited"; the model "is
yet to be fine-tuned to incorporate more data categories"; RAG coverage of "more nuanced
simulator behaviour" is future work; digitisation is limited by "incomplete information
about the chemicals, processing steps and operating" conditions; energy, water and waste
"were not part of the current validation"; and closing the gap in the harder categories is
recorded as not yet done.

## G26 — Recurrent agent-side failure modes recorded inside the loop

- candidates: c004; c018; c025; c039; c041; c057; c070; c083; c139; c140; c156; c161; c166; c168; c174; c180; c182; c184; c188; c194; c209; c213; c232
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: arxiv:2605.08941; doi:10.48550/arxiv.2606.21841; arxiv:2603.27646; arxiv:2608.02642
- checked: 2026-09-11

[Certain] Both corpora record specific, repeated ways the agent itself fails. Models
"cannot always self-correct malformed tool calls after several attempts"; recurrent failures
include "loss of task history, disregard of convergence results, attempts to bypass tool
refusals, incorrect arithmetic"; errors bypassing the solver's fatal-error macros — mpirun
option errors, decomposePar configuration failures, bare floating-point-exception traces —
are not caught; an 84% success rate "indicates a remaining reliability gap" with "invalid
generated arguments" terminating the workflow; a two-stage strategy "introduces potential
error propagation" with "cascading errors in the output structure"; the model "struggles
selecting correct functions from the vast library"; performance on plasticity is 60%; an
agent "could not reproduce the generalized stacking fault energy calculation from a minimal
prompt"; one run "failed to extract any" result; the agent "consistently struggles with …
tacit domain knowledge, including appropriate simulation timescales, equilibration
protocols"; language models show "erratic search dynamics in continuous spaces" and "a
pronounced dependence on initial prompt configurations"; there is "difficulty producing
floating-point values with high precision"; a repository documents failures per test rather
than limitations, one needing five iterations and hitting six API and mesh
incompatibilities; behaviour is "inherently probabilistic" with convergence characterisation
open; "a small subset of challenging queries causes the majority of failures"; sparse-data
wells "produce lower-quality answers" and the agent "does not ask clarifying questions when
scope is ambiguous"; natural-language uncertainty is reduced but "does not eliminate it";
improvement "diminishes as the model size and complexity increase"; cognitive boundaries are
described as inherent to "the current static reasoning paradigm"; challenges remain "in
reliably interpreting user intent"; there is "difficulty compiling answers across a large
set of documents and finding information within plots and graphs"; reliability of generating
robust solver configurations for complex flows remains "a primary limitation"; LLMs with
tool calling "cannot currently construct complex real-world science applications"; and
closed-loop recovery "remains useful even when the initial planner is strong since several
successful runs still depend on recovery or plan" modification.

## G27 — Verifying what the agent produced is recorded as an unsolved cost

- candidates: c068; c077; c133; c159; c206; c217; c236
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: refuted
- evidence: doi:10.48550/arxiv.2601.09749; doi:10.48550/arxiv.2608.29665; doi:10.1145/3731599.3767582; doi:10.1073/pnas.2524747123
- checked: 2026-09-11

[Certain] Both corpora record that checking the output is itself unresolved. The amount of
work that must be verified "grows with AI reliability", and faithfulness and reproducibility
problems make the burden unmanageable in HPC production; AI agents "remain weak in plan
verification"; a defect taxonomy "is seeded from defects actually encountered during
development, not a comprehensive catalog"; a reported 77.9% is "a conservative lower bound"
because the scoring rule "under-counts synonymous surface forms"; an embedding metric "was
not discriminative between models and fails to detect subtle variations in output quality";
a reported F1 "characterizes the end-to-end verification task rather than an autonomous
safety decision capability"; and "dependency management and environment reproducibility,
especially for tools like LAMMPS, Atomsk, and Phonopy, can become brittle across platforms".

## G28 — Evaluation data is synthetic, self-made, or of unestablished provenance

- candidates: c015; c038; c050; c069; c080; c103; c151; c160; c178; c200; c210; c256
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.1016/j.net.2026.104573; arxiv:2604.03460; arxiv:2608.01369
- checked: 2026-09-11

[Certain] 9 of the 41 deep-read landscape systems and 29 of the 101 deep-read TANGO systems
were evaluated on synthetic data only. Authors record the provenance problem directly. An
inversion problem is "intentionally simplified" and "under-represents real world scenario",
recorded in both runs, and the same system's evaluator was not itself optimised;
"pretraining-corpus opacity of the base LLM cannot rule out prior exposure to geological
literature"; generators and machine-learned potentials "trained on Materials Project data
… inherit shared distributional biases"; a demonstration "relied on synthetic Marvin and
curated news feeds"; insights "were extracted from simulated field data"; a lumped model
representation "was used for demonstration purposes"; a single-project dataset has "no
manually verified coordinate ground truth"; implicit calibration is sufficient only "in
small fully enumerable spaces"; and one conductivity estimate "is a calibrated consistency
check rather than a blind prediction".

## G29 — Further grid columns the runs could not fill from their sources

- candidates: c092; c093; c096; c097; c098; c246; c249; c250; c251
- runs: 01_landscape/v0.5; 02_tango/v0.2
- verdict: partially-addressed
- evidence: doi:10.48550/arxiv.2409.11363; doi:10.48550/arxiv.2601.09749
- checked: 2026-09-11

[Certain] Beyond held-out status, baseline, model and code, both grids record columns their
sources left empty. In the landscape run: `reported_result` 79 of 151, `data_type` 56 of
151, `tools_used` 52 of 151, `evaluation_method` 40 of 151, `maturity_claimed` 3 of 151. In
the TANGO run: `data_type` 69 of 183, `reported_result` 62 of 183, `maturity_claimed` 25 of
183, `tools_used` 1 of 183. The two runs differ most on `tools_used`, which is near-complete
in the TANGO grid and blank for roughly a third of the landscape grid.

## Discarded candidates

Every candidate in `gap_candidates.csv` is either cited by a gap above or listed here.

- c009 — `run-artefact`. The `author_stated_limitations` cell reads "not available - abstract only". It records the run's access, not a limitation.
- c029 — `run-artefact`. Cell reads "not available - software deposit description only".
- c043 — `run-artefact`. Cell reads "not available - abstract only".
- c045 — `run-artefact`. Cell reads "not available - software deposit description only".
- c074 — `run-artefact`. Cell reads "abstract says limitations are outlined but does not state them": a record of what the abstract withheld from the reader, not a stated limitation.
- c079 — `run-artefact`. Cell reads "not available - abstract only".
- c014 — `too-specific`. One neural-architecture-search run's finding that optimising recall alone discarded the best F1 designs. Nothing else in either corpus bears on it.
- c034 — `too-specific`. One system's noisy HTML structures and DOM element selection.
- c048 — `too-specific`. One catalog system's weak precise-statistics scores and its authors' attribution of them to retrieval-then-synthesize architectures. The landscape run records this as a disagreement between two sources rather than as an absence.
- c222 — `too-specific`. One repository's package name being held by a third-party PyPI upload.
- c261 — `run-artefact`. The extractor flags every M0/M1 row carrying a `maturity_claimed` string. This one reads "DynaMate2 offers a template rather than a finished product", which does not reach past M1.
- c262 — `run-artefact`. "reproducibility should be structural, not post-hoc" is a design principle, not a maturity claim.
- c264 — `run-artefact`. "WARA can already construct a clearer optimization research structure" does not reach past M1.
- c270 — `run-artefact`. The claim string is "proof-of-concept".
- c288 — `run-artefact`. "MDAgent can effectively assist experts in semi-automating domain-specific tasks, serving as a valuable support tool" does not reach past M1.
- c289 — `run-artefact`. "This work does not claim autonomous scientific discovery or fully automated research" is a self-limitation; the TANGO run's section 05 cites the same source as a counter-example to overreach.
- c290 — `run-artefact`. "The developed agent served as a prototype … with its current efficacy" does not reach past M1.
- c327 — `run-artefact`. Extracted from the "Recovered by hand" rows of `paywalled.md`: `doi:10.1039/d5dd00435g` was retrieved and read in the v0.2 round and is a core row carrying six touchpoints. The candidate records a v0.1 access failure the run itself resolved.
- c328 — `run-artefact`. Same shape: `doi:10.2139/ssrn.7333555` was read in v0.2 and is the corpus's fourth `uncertainty-quantification` core row at M3.
- c329 — `run-artefact`. Same shape: `doi:10.26434/chemrxiv.15006587/v1` was read in v0.2.

### Candidates of refuted gaps

Twelve gaps were refuted. Their blocks stay above as the record.

The candidates are listed here so nothing downstream reads them as a standing gap.

- c095; c102; c248; c255 — `refuted` (G01: Neither corpus states whether its evaluation data was held out)
- c091; c245 — `refuted` (G03: The generator model is unnamed in half of one corpus and two fifths of the other)
- c100; c253 — `refuted` (G04: Most admitted sources state nothing about code availability)
- c239; c242; c104; c257 — `refuted` (G05: No system in either corpus demonstrates maturity above M3)
- c238; c240 — `refuted` (G10: No agent drives a life-cycle economic model as the system it controls)
- c058; c061; c063; c132; c142; c150; c172; c199; c212; c220; c229; c235 — `refuted` (G12: A run that executes is not a run that is physically right, and the corpora record that the second is not checked)
- c012; c035; c046; c047; c086; c138; c171; c181; c202; c224; c226; c227 — `refuted` (G15: Systems are confined to a predefined toolset, workflow or starting artefact)
- c040; c056; c065; c126; c129; c173 — `refuted` (G21: Token, API and scheduler cost is named as a limit rather than measured as one)
- c023; c131; c155; c211; c214; c218; c241 — `refuted` (G23: No shared or third-party benchmark, and no agreed way to score these systems)
- c059; c152; c191; c197; c204; c221 — `refuted` (G24: Open-weight and smaller models are recorded as failing where frontier models do not)
- c004; c018; c025; c039; c041; c057; c070; c083; c139; c140; c156; c161; c166; c168; c174; c180; c182; c184; c188; c194; c209; c213; c232 — `refuted` (G26: Recurrent agent-side failure modes recorded inside the loop)
- c068; c077; c133; c159; c206; c217; c236 — `refuted` (G27: Verifying what the agent produced is recorded as an unsolved cost)
