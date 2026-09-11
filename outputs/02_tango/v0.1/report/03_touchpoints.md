# 03 Touchpoints

[Certain] One subsection per touchpoint in the controlled list of `reference/SCHEMA_tango.md`,
including those no source matched. A touchpoint tag is a claim about the source — that the
source demonstrates an agent doing that kind of work on some system — and never a claim
about TANGO.

[Certain] Counts below are **per `transfer.csv` row**, not per system. Five systems hold more than one
row: OpenFOAMGPT has three [[doi:10.1063/5.0257555]] [[doi:10.1016/j.taml.2025.100623]]
[[doi:10.1016/j.ijheatfluidflow.2026.110399]], and Foam-Agent [[doi:10.48550/arxiv.2509.18178]]
[[doi:10.48550/arxiv.2505.04997]], OASiS [[doi:10.5281/zenodo.20543501]]
[[doi:10.5281/zenodo.20388035]], Aspen-MCP
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]
[[doi:10.26434/chemrxiv.15006587/v1]] and diagnose_project [[doi:10.5281/zenodo.21841883]]
[[doi:10.5281/zenodo.21841882]] have two each. 183 rows cover 177 distinct `system_id`
values.

[Certain] Every count is given twice — all rows, then core rows only — because the two differ in what
they mean. A core tag rests on a quoted sentence from the full text, recorded in
`transfer.md`. A context tag rests on an abstract, and abstracts systematically over-report
scope and under-report mechanism.

| touchpoint | all rows | core rows |
|---|---|---|
| config-generation | 98 | 75 |
| solver-control | 77 | 67 |
| results-interpretation | 60 | 55 |
| verification-regression | 48 | 36 |
| optimisation-loop | 44 | 29 |
| hpc-scale-out | 34 | 19 |
| tool-exposure | 32 | 24 |
| topology-construction | 25 | 21 |
| provenance-reproducibility | 24 | 15 |
| surrogate-modelling | 17 | 11 |
| uncertainty-quantification | 11 | 4 |
| techno-economic | 7 | 6 |
| *(none)* | 25 | 3 |

---

### config-generation

**98 rows, 75 core — the most common touchpoint in the corpus by a wide margin.** [Certain]
The dominant shape is an agent that emits or edits a simulator's input file and then runs it.
The named artefacts are concrete and they repeat: OpenFOAM case directories
[[doi:10.48550/arxiv.2509.18178]] [[doi:10.1016/j.taml.2025.100594]] [[arxiv:2602.11689]]
[[doi:10.1002/aidi.202500174]], EnergyPlus input files
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]]
[[doi:10.26868/30680611.2026.1305]] [[doi:10.1080/19401493.2026.2653969]], GEOS XML decks
[[arxiv:2607.18557]], ECLIPSE-format reservoir decks [[doi:10.48550/arxiv.2605.15028]], EPA
SWMM INP decks [[doi:10.31223/x5f47g]], LAMMPS scripts [[doi:10.48550/arxiv.2607.22596]],
SIESTA input files [[doi:10.48550/arxiv.2608.29665]] and LS-DYNA keyword decks
[[doi:10.5281/zenodo.22554152]].

[Certain] Within that shape the corpus divides on a question it does not resolve: whether to
**generate the configuration or constrain it**. On one side are systems that let the model
write the input and then repair it from the solver's own error stream — OpenFOAM work is the
clearest case, with the corrector agent resubmitting until the run converges or a cap is hit
[[doi:10.1016/j.taml.2025.100594]], and a reflection module writing structured insights into
long-term memory when errors persist [[doi:10.1002/aidi.202500174]]. On the other are systems
that refuse to let the model emit free-form input at all: a rule-based editor applies
deterministic transformations to named fields and "prevents ill-formed edits such as missing
delimiters or invalid field counts" [[doi:10.26868/30680611.2026.1305]]; a typed tool schema
rejects requests before they reach the simulator
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]; a
schema-constrained JSON intermediate carries geometry, materials and actions to the solver
rather than code [[doi:10.3390/buildings15173190]]; dry runs at the extreme parameter values
validate a deck before an optimisation starts [[doi:10.48550/arxiv.2605.15028]].

[Certain] The one head-to-head measurement of those two designs is the Aspen Plus work, which
ran the same models both ways on the same tasks and attributes the 16%-to-89% gap to the
paradigm rather than the retry budget, because the dominant code-generation failure —
invented object paths that do not exist in the simulator — "cannot occur through typed tools"
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]
[[doi:10.26434/chemrxiv.15006587/v1]]. No other source in the corpus tests the two designs
against each other, so this is a single measurement and not a consensus.

### solver-control

**77 rows, 67 core.** [Certain] Almost every source that generates a configuration also runs
it, which is why this count tracks `config-generation` so closely; the gap between the two is
the set of systems that emit an input somebody else executes. Those exist and are worth
separating: one materials agent writes VASP decks and SLURM scripts that "a human submits"
[[arxiv:2512.23010]], and one building-energy system generates optimisation code without
running it [[doi:10.26434/chemrxiv-2025-f1wcr]].

[Certain] The engines driven are named far more often than not, and they are real production
codes rather than toys: OpenFOAM across at least a dozen rows, EnergyPlus, LAMMPS, VASP,
Quantum ESPRESSO [[doi:10.48550/arxiv.2507.14267]] [[doi:10.48550/arxiv.2602.00185]], GEOS
[[arxiv:2607.18557]], OPM Flow [[doi:10.48550/arxiv.2605.15028]]
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]], Aspen Plus
[[doi:10.1038/s44172-025-00583-3]], OpenRadioss [[doi:10.5281/zenodo.22554152]], Ansys HFSS
[[doi:10.1109/access.2025.3605803]], PandaPower and ANDES [[arxiv:2602.20683]], FEniCSx and
seven sibling finite-element codes [[doi:10.5281/zenodo.20543501]], and PyQUDA on GPU
[[doi:10.48550/arxiv.2607.15001]]. Where the engine is *not* named, that is almost always a
context row read from an abstract — the conference abstracts in particular say "a
physics-based geothermal reservoir simulator" [[doi:10.2118/232332-ms]] and "well-network flow
and gas processing simulations" [[doi:10.2118/229629-ms]] without identifying either.

[Certain] What closes the loop is narrower than what opens it. Several systems read only
whether the run terminated; a smaller set reads the solver's own physics diagnostics and gates
on them. Energy-balance and mass-error parsing before a score is computed
[[doi:10.5281/zenodo.22554152]], chi-squared targeting against the estimated error level
[[doi:10.1016/j.bdes.2026.100042]], and a physically-plausible-barrier window that returns a
candidate to redesign [[arxiv:2606.05050]] are the three clearest instances in the corpus.

### results-interpretation

**60 rows, 55 core.** [Certain] The near-identity of those two numbers is itself informative:
this is a touchpoint that full-text reading finds and abstracts do not mention. It is
generally the last stage of a pipeline and generally described briefly — a report agent that
"synthesized geophysical and climate data into synchronized visualizations and performed
automated correlation analysis" [[doi:10.1016/j.bdes.2026.100042]], a physics interpreter that
"automatically produces a technical summary immediately after the case is successfully
generated" [[doi:10.1002/aidi.202500174]], an agent converting numerical outputs into textual
interpretations that "link observed performance shifts to underlying physical causes"
[[doi:10.26868/30680611.2026.1305]].

[Certain] A minority go further and derive a physical quantity from the output rather than
describing it: a Strouhal number measured from a vortex-shedding run and compared against the
accepted value [[doi:10.5281/zenodo.20543501]], a lumped equivalent circuit fitted from
simulated scattering parameters [[doi:10.1109/access.2025.3605803]], the transition from Darcy
to non-Darcy flow identified from a porous-media sweep
[[doi:10.1016/j.ijheatfluidflow.2026.110399]]. The corpus does not report whether these
interpretations were checked for correctness separately from the numbers they rest on.

### verification-regression

**48 rows, 36 core.** [Certain] Three distinct things carry this tag and they are not
interchangeable. The first is agreement against an analytical or published reference — an L2
error of 7e-15 against an analytical heat-equation solution, seven solvers agreeing to 99.9%
on a cross-solver Poisson benchmark [[doi:10.5281/zenodo.20543501]], validation against
published results from two other reservoir simulators [[arxiv:2607.18557]], numerical
comparison against a hand-written expert implementation at machine precision on 63 of 70 tasks
[[doi:10.48550/arxiv.2607.15001]]. The second is repeatability of the agent itself — identical
inputs re-run ten times with zero schema drift [[doi:10.26868/30680611.2026.1305]], a 100%
reproducibility rate across over 450 simulations [[doi:10.1016/j.ijheatfluidflow.2026.110399]],
a workflow executed ten times with token accounting [[doi:10.1080/19401493.2026.2653969]]. The
third is a gate inside the loop that stops a bad result propagating — a deterministic
validation auditor combining element-count, atomic-overlap and path-collision checks with an
energy screen [[arxiv:2606.05050]], a mandatory critic sub-agent that must approve a setup
before any run is permitted [[doi:10.5281/zenodo.20543501]], expected-artifact and NaN/Inf
screening after execution [[arxiv:2604.24696]].

[Certain] One source separates executability from correctness explicitly and measures both,
reporting 82.1% execution success against 68.12% physical fidelity and calling the latter "the
first rigorous metric capturing whether a runnable simulation is scientifically meaningful"
[[doi:10.1002/aidi.202500174]]. Another states the same point from the other direction:
successful execution "does not by itself establish scientific correctness", so every generated
workflow was compared numerically against a trusted reference
[[doi:10.48550/arxiv.2607.15001]]. A third reports that its static checks were insufficient
and that the simulator "rejected the first input deck ... twice", because "some errors are only
caught at running time" [[arxiv:2607.18557]].

### optimisation-loop

**44 rows, 29 core.** [Certain] The corpus contains two clearly different arrangements and
mixes them under one label. In the first, the agent *is* the optimiser: it proposes the next
point itself, as in the multi-agent acquisition policy that replaces the acquisition function
inside a 30-query budget [[doi:10.25417/uic.32994011.v1]], the bisection search over
interconnection capacity [[arxiv:2602.20683]], or the closed-loop composition search over an
alloy ternary [[doi:10.2139/ssrn.6942178]]. In the second, the agent *drives* a conventional
optimiser and does not do the searching: a validated ensemble Bayesian-optimisation tool
[[doi:10.1016/j.net.2026.104573]], scipy's L-BFGS-B with an active-subspace response surface
[[doi:10.1016/j.taml.2026.100660]], genetic algorithms and particle swarm on well placement
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]], pymoo-style
multi-objective search [[doi:10.1080/09544828.2026.2624356]], the MMA density update inside a
topology-optimisation solver [[arxiv:2607.01812]].

[Certain] Where both arrangements were measured against each other, delegation won. The
nuclear-engineering system reports that delegating the search to a validated tool reached
12.6% error against a human-expert pipeline's 12.4%, and concludes that agents "are most
effective as orchestrators of validated scientific tools rather than generators of numerical
code" [[doi:10.1016/j.net.2026.104573]]. The materials-discovery environment found the
fully agentic orchestrator competitive but not dominant — an enhancement factor of 6.0 against
a best non-agentic pipeline acceleration factor of 6.4 [[doi:10.48550/arxiv.2601.20996]]. Two
measurements pointing the same way is not a settled finding, and neither paper claims it is.

### hpc-scale-out

**34 rows, 19 core.** [Certain] What is driven here is a scheduler, almost always Slurm:
job submission and monitoring [[doi:10.48550/arxiv.2507.14267]], measurement scripts and
submission artefacts generated together [[doi:10.48550/arxiv.2607.15001]], workflow DAGs
executed by HTCondor across four testbed sites [[arxiv:2606.18425]], training jobs dispatched
over SSH [[doi:10.3929/ethz-c-000801434]], hash-verified run specifications submitted as batch
jobs [[doi:10.1145/3785462.3815873]], workflows of "hundreds of simulation jobs" launched after
an engineer approves the plan
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]].

[Certain] The one source that reports what actually broke at leadership scale is the most
specific: a distributed-launch sweep in which "torchrun passed all seven tested cases, while
the tested Slurm and MPI launch methods failed all seven cases", a Spack and MPI linkage
failure detectable "only after extensive debugging", and the observation that the file volume
from a short agent session "can rapidly become overwhelming for human verification"
[[doi:10.20944/preprints202608.1323.v1]]. One source reports the opposite concern from the
agent's side — that interacting with running simulations, "monitoring convergence, diagnosing
stalls, and steering or restarting runs mid-execution — remains an open direction"
[[arxiv:2607.18557]].

### tool-exposure

**32 rows, 24 core.** [Certain] This touchpoint is where the Model Context Protocol
concentrates: 17 of the 26 rows with `interface: mcp` carry it. The counts of exposed tools
are stated precisely and vary by two orders of magnitude — 11 [[arxiv:2602.20683]], 13
[[doi:10.5281/zenodo.20543501]], 35 [[doi:10.1016/j.softx.2025.102367]], 42
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]] and 52
[[arxiv:2607.18557]].

[Certain] Two sources treat the tool surface itself as the object of study rather than as
plumbing. One measures tool-selection accuracy against a gold tool set and reports precision
0.953 [[doi:10.3389/fchem.2026.1914886]]; another reports 84.0% tool-selection accuracy across
50 scenarios and 0.0% for one competing backbone on one task slice [[arxiv:2602.20683]]. One
source states the cost directly: tool-calling consumed roughly 57 times more tokens than code
generation for comparable wall time, and concludes "reliability costs tokens, not time"
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]. A
counter-observation comes from the building-energy comparison, which warns that when many
tools are available "the model may select inappropriate tools or become confused by
overlapping functionalities" [[doi:10.1080/19401493.2026.2653969]].

### provenance-reproducibility

**24 rows, 15 core.** [Certain] The mechanisms are specific and they differ. Per-run manifests
recording the solver return code [[doi:10.31223/x5f47g]]; bitwise-identical replay without
re-executing prior actions, with fork isolation and failure auditability measured as three
falsifiable questions [[doi:10.48550/arxiv.2601.09749]]; a runtime-error knowledge base that
persists each diagnosis so the next deck benefits [[arxiv:2607.18557]]; version-pinned
injection of the solver package into each solve-time kernel
[[title:mcpsolvermodelcontextprotocolserverforconstraintsolvingsatmaxsatsmtcpaspdp]];
curated result logs that let a reader replot the reported numbers without owning the
proprietary simulator
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]];
hash-verified execution plans rejected before scheduling if tampered
[[doi:10.1145/3785462.3815873]]; markdown run records templated from already-computed results
[[doi:10.5281/zenodo.22554152]].

[Certain] One source argues the field's tooling is not yet adequate here, stating that
requirements for faithful evidence and provenance "are currently out of the scope of
state-of-the-art tools" and that future tools "should support negative evidence as a
first-class object" [[doi:10.20944/preprints202608.1323.v1]]. That is a minority position in
the corpus and it is stated by the only source reporting from a leadership-class facility.

### topology-construction

**25 rows, 21 core.** [Certain] This is the touchpoint where the agent decides the *structure*
of the model rather than its parameters, and it splits cleanly by domain. In process
engineering it means assembling a flowsheet: digitising a flowsheet graph from a natural-language
description and translating it into simulator units [[doi:10.1039/d6dd00060f]]
[[doi:10.69997/pse.120458]], converting a conventional column into a heat-pump-assisted
configuration by writing a new input file [[doi:10.1038/s44172-025-00583-3]]. In continuum
mechanics and CFD it means meshing and geometry: Gmsh mesh generation
[[doi:10.5281/zenodo.20543501]], hybrid structured-unstructured meshes around an obstacle via
the Gmsh Python API [[arxiv:2602.11689]], geometry generated by text-to-3D models and fed to a
flow solver [[doi:10.1063/5.0294696]], a topology-optimisation solver performing residual
assembly and density updates [[arxiv:2607.01812]]. In materials it means building the slab:
predicting surface free energies for all Miller-index facets and returning simulation-ready
slabs [[arxiv:2606.05050]].

[Certain] It is also where agents most visibly fail. The two-dimensional CFD study reports
that "the lack of spatial reasoning capabilities in LLMs appears to produce an incorrect
geometry and mesh" and names geometry understanding "a major area in need of improvement"
[[doi:10.48550/arxiv.2509.20374]]. The OpenFOAM coding-agent study reports failures "such as
failing to properly represent an obstacle in the mesh" that "require a deeper understanding of
the underlying physics, which the agent currently lacks", concluding "human oversight remains
essential" [[arxiv:2602.11689]]. The flowsheet harness reports "compositional spec
incompleteness" — the model defines a block but omits the feed stream and wiring, and across
six feedback attempts "never assembles a complete" specification
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]. The GEOS
work names meshing as the part that "warrants a dedicated specialized agent"
[[arxiv:2607.18557]].

### surrogate-modelling

**17 rows, 11 core.** [Certain] Two arrangements again, and here they are cleanly separable.
In the first, a machine-learned potential or emulator stands *in place of* the expensive
solver inside the agent's loop: machine-learned force fields relaxing candidate structures
"significantly reducing computational overhead compared to DFT calculations"
[[doi:10.48550/arxiv.2506.05616]], a machine-learned-potential formation-energy oracle used as
the evaluation budget [[doi:10.48550/arxiv.2601.20996]], four named machine-learned potentials
plus hyperparameter tuning [[arxiv:2512.23010]], MACE potentials alongside first-principles
codes [[doi:10.48550/arxiv.2602.00185]]. In the second, the agent *builds* the surrogate:
orchestrating a training and hyperparameter-optimisation loop over a thousand stored
geologic-carbon-storage simulations [[doi:10.48550/arxiv.2604.11945]], training a neural
operator from finite-element solves it configured itself [[arxiv:2607.05134]], generating 200
parametric simulations expressly as a training ensemble [[arxiv:2607.18557]], fitting a lumped
equivalent circuit from full-wave results [[doi:10.1109/access.2025.3605803]].

[Certain] One source reports the limit of the first arrangement in its own terms, attributing
a residual barrier offset to "the UMA-DFT methodological difference" rather than to the agent
[[arxiv:2606.05050]]. Another states that generators and machine-learned potentials trained on
the same public database "inherit shared distributional biases that may simplify discovery
relative to real-world settings" [[doi:10.48550/arxiv.2601.20996]].

### uncertainty-quantification

**11 rows, 4 core.** [Certain] This is the largest gap between context and core counts in the
table, and the reason is access rather than absence: four of the seven context rows are
conference abstracts and papers this run could not read
[[doi:10.2118/229629-ms]] [[doi:10.2118/232332-ms]] [[doi:10.3997/2214-4609.2024637030]]
[[doi:10.1016/j.net.2026.104573]], so their uncertainty claims stand on abstracts alone. The
four core rows are specific: Monte Carlo propagation of petrophysical parameter uncertainty
through Archie's law, with the ensemble spread narrowing as priors tighten
[[doi:10.1016/j.bdes.2026.100042]]; Gaussian-process and autoencoder surrogates of a
neutronics model [[doi:10.25394/pgs.32118403]]; density-functional calculations dispatched
with uncertainty-aware screening [[doi:10.48550/arxiv.2507.14267]]; and a three-layer
protocol of Morris screening, Sobol decomposition and Monte Carlo propagation run over an
EnergyPlus calibration cohort [[doi:10.2139/ssrn.7333555]].

[Certain] That fourth row is the only one in the corpus whose uncertainty analysis returns a
result that contradicts the modelling assumption it was run to support: "equipment density
accounts for 80-99% of annual energy-use variance, while envelope parameters, most directly
recoverable from geometry, contribute negligibly", which the authors state "challenges common
geometry-driven UBEM assumptions" [[doi:10.2139/ssrn.7333555]]. This source was originally
unreadable by any route and entered the core tier only after its full text was retrieved by
hand and read.

[Certain] The one source that states its own uncertainty budget as incomplete does so plainly:
"the current uncertainty quantification propagates only petrophysical parameter uncertainty",
so survey errors including "electrode position uncertainty, reciprocal measurement errors, and
temperature drift, are not yet incorporated into the final water content uncertainty maps"
[[doi:10.1016/j.bdes.2026.100042]].

### techno-economic

**7 rows, 6 core — the smallest non-empty touchpoint.** [Certain] Where it appears it is
usually a single objective rather than a costing model: net present value maximised over 30
well locations [[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]],
capital and operating expenditure computed on a converged flowsheet
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]
[[doi:10.26434/chemrxiv.15006587/v1]] — two rows of the same system, which is why this
touchpoint covers 7 rows but only 6 systems — a
cost-per-activity figure of merit computed from commodity prices and industrial loadings
[[arxiv:2606.05050]], operating-cost and return-on-investment recommendations synthesised from
simulation results [[doi:10.1080/19401493.2026.2653969]], and a heat-pump retrofit assessed on
capital and operating cost together with emissions [[doi:10.1038/s44172-025-00583-3]].

[Absent-searched] (backed by query cells `q007`, `q008`, `q009`, `q010`) No admitted source reports an agent driving a full life-cycle cost model —
levelised cost of energy, discounted cash flow, or a comparable economic model — as the
system it controls. The energy-systems and geoenergy query cells that would surface such work
were run without hitting a paging cap on the OpenAlex side (`q007`, `q008`, `q009`, `q010`;
`q007:arxiv` and `q009:arxiv` lost six and one record respectively to truncation) and the grey
pass added eighteen further targeted web searches, logged as `w001`–`w018` in `queries.csv`; the shortlist
they produced contains economic *objectives* inside optimisation loops, as cited above, but no
system whose driven artefact is an economic model.

### *(none)*

**25 rows, 3 core.** [Certain] Two-thirds of these are reviews, surveys and position pieces
admitted at `tier: context` — they describe the field rather than build in it, so no
touchpoint applies [[doi:10.48550/arxiv.2601.01321]] [[doi:10.1007/s10270-025-01306-0]]
[[arxiv:2608.03600]] [[arxiv:2509.08269]] [[doi:10.1016/j.apenergy.2025.126670]].

[Certain] Three core rows carry `none` and each for a different and stated reason. One is a
framework whose agent layer is explicitly designed but not built — "no physical experiments,
RL-optimized syntheses, or live dashboard deployments are reported in this work" — so the
CALPHAD computation it reports was run by the authors' own scripts rather than by an agent
[[doi:10.5281/zenodo.19835550]]. The other two drive artefacts that fall outside the
touchpoint vocabulary rather than outside scope [[doi:10.11578/dc.20260516.1]]
[[doi:10.1016/j.compenvurbsys.2026.102449]].

[Certain] Two further rows originally carried `none` for a different reason again:
`doi:10.1039/d5dd00435g` and `doi:10.2139/ssrn.7333555` could not be read by any route, so no
touchpoint could be evidenced for either. Both were later read from the local PDF store and
both are now core rows carrying six touchpoints each, which is why this count fell from 27 to
25. The episode is kept in `unreachable.md` because the distinction it illustrates still
holds for any future run: an access failure and a genuine absence carry the same label in the
column, and here the label was wrong in both cases.
