# 00 Executive summary

[Certain] What exists in the literature on agentic systems that drive a simulator, solver,
optimiser, scientific code or engineering model; at what maturity; against which of TANGO's
surfaces; and on what evidence. Descriptive throughout.

## The corpus

[Certain] 35,046 records were harvested from OpenAlex and arXiv across 22 query cells, triaged
to a 773-record shortlist, and screened by hand to **183 admitted sources: 101 deep-read `core`
and 82 abstract-only `context`**. A random 150-record sample below the cut gave a 2%
false-negative rate. 127 are from 2026 and 50 from 2025: a literature roughly two years old.

[Certain] The field is domain-agnostic in a way the harvest makes visible. The same control
pattern — an agent, a loop, and an engine it did not implement — appears in CFD, building
energy, reservoir engineering, process chemistry, materials, structural mechanics, power
systems, neuroimaging and lattice QCD, and these literatures rarely cite each other. By
subfield: simulation orchestration 48, solver control 37, computational
discovery 33, scientific computing 31, geoenergy 14, optimisation and uncertainty 11,
simulation general 5, energy systems 4.

## What these systems do

[Certain] The dominant artefact is an input file. 98 of 183 rows carry `config-generation` and
77 carry `solver-control`, and the engines are usually named: OpenFOAM, EnergyPlus, LAMMPS,
VASP, Aspen Plus, OPM Flow, GEOS, OpenRadioss, Ansys HFSS, FEniCSx. Four emission modes divide
the core tier almost evenly —
`code-execution` 29, `file-io` 28, `api` 19, `mcp` 19 — and the newest of them, a typed tool
surface the agent selects from rather than writes to, is also the only one with a head-to-head
measurement behind it: the same models on the same tasks went from 16% to 89% task success when
moved from writing simulator-driving code to calling typed tools — a gap the authors attribute
to the paradigm, not the retry budget
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]
[[doi:10.26434/chemrxiv.15006587/v1]], error feedback having recovered hallucinated variable
paths in zero of thirty instances.

[Certain] What closes the loop is narrower than what opens it. 77 of 101 core systems iterate
autonomously, almost always *read the error, revise, resubmit, stop at a cap*. Far fewer read
the solver's physics rather than its exit status; energy-balance gating
[[doi:10.5281/zenodo.22554152]], chi-squared targeting [[doi:10.1016/j.bdes.2026.100042]] and a
plausible-barrier window [[arxiv:2606.05050]] are the clearest instances. One source measured
the difference: 82.1% of runs executed, 68.12% were scientifically meaningful
[[doi:10.1002/aidi.202500174]].

## Against TANGO's surfaces

[Certain] Touchpoint coverage is heavily uneven: config-generation 98 and solver-control 77 at
the top, techno-economic 7 and uncertainty-quantification 11 at the bottom. Section 03
tabulates all twelve with core-only counts beside them, and the difference matters: an abstract
over-reports scope.

[Absent-searched] (backed by query cells `q007`-`q010`) No admitted source drives a full life-cycle cost model — levelised cost,
discounted cash flow or equivalent — as the system it controls. Economic quantities appear as
objectives inside optimisation loops, not as the driven artefact. Those cells were harvested
without a paging cap and eighteen targeted web searches logged.

## Maturity

[Certain] Demonstrated maturity across 101 core rows: M0 3, M1 38, M2 48, M3 12. All 82 context
rows are `not stated (abstract only)`.

[Absent-searched] (backed by query cells `q001`-`q014`) **Nothing in the corpus reaches M4 or M5.** No source shows a system in
routine use by people other than its authors, or an output that entered a real operational
decision with third-party evidence. The 12 M3 rows are retrospective work against references
the authors did not produce — a real reservoir [[doi:10.48550/arxiv.2605.15028]], named
catalyst systems [[arxiv:2606.05050]], crash-validation decks [[doi:10.5281/zenodo.22554152]],
an expert implementation [[doi:10.48550/arxiv.2607.15001]], six named campus buildings checked
against metered energy use [[doi:10.2139/ssrn.7333555]]. One author calls it "an early
exploration rather than a production-ready solution" [[doi:10.1080/19401493.2026.2653969]].

## What the evidence will not support

[Certain] 26 of 101 core sources report no baseline and 53 do not say whether their evaluation
data was held out. Only one benchmark — FoamBench [[doi:10.48550/arxiv.2509.20374]] — was reused
unchanged by an independent group [[arxiv:2602.11689]], and it is confined to CFD. 21 state
nothing about what happens when the driven code fails, a silence searched for, not inferred.

[Certain] Access is part of the evidence, and this run measured its cost. This run originally
demoted 15 core records it could not read, losing 13% of the intended deep-read — mostly to
hosts that refuse automated clients rather than to licensing. Fourteen sources were then
retrieved by hand: three of those fifteen, all of which supported a core write-up, taking the
core tier from 98 to 101 and leaving **11% still lost**; and eleven already-`core` sources
originally read from a preprint, proxy or deposit. Against the version of record, eight were unchanged and three corrected — a
missing case study [[doi:10.1016/j.dche.2026.100312]], an omitted pass@1 figure
[[doi:10.1016/j.taml.2026.100660]], and a different stated mechanism with a hallucination
incident [[doi:10.1145/3731599.3767349]]. `RUN.md` records the re-read; `paywalled.md` and
`unreachable.md` record every route tried.
