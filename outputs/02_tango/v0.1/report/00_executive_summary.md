# 00 Executive summary

[Certain] What exists in the literature on agentic systems that drive a simulator, solver,
optimiser, scientific code or engineering model; at what maturity; against which of TANGO's
surfaces; and on what evidence. This run is descriptive throughout.

## The corpus

[Certain] 35,046 records were harvested from OpenAlex and arXiv across 22 query cells, triaged
to a 773-record shortlist, and screened by hand to **183 admitted sources: 98 deep-read `core`
and 85 abstract-only `context`**. A random 150-record sample of the below-cut population gave a
2% false-negative rate. 126 of the 183 are from 2026 and 51 from 2025, so this is a literature
roughly two years old.

[Certain] The field is domain-agnostic in a way the harvest makes visible. The same control
pattern — an agent, a loop, and an engine it did not implement — appears in CFD, building
energy, reservoir engineering, process chemistry, materials, structural mechanics, power
systems, neuroimaging and lattice QCD, and the sources cite each other across those boundaries
only rarely. Admitted sources by subfield: simulation orchestration 48, solver control 37,
computational discovery 33, scientific computing 31, geoenergy and subsurface 14, optimisation
and uncertainty 11, simulation general 5, energy systems 4.

## What these systems do

[Certain] The dominant artefact is an input file. 96 of 183 rows carry `config-generation` and
76 carry `solver-control`, and the engines are named far more often than not: OpenFOAM,
EnergyPlus, LAMMPS, VASP, Quantum ESPRESSO, Aspen Plus, OPM Flow, GEOS, OpenRadioss, Ansys
HFSS, PandaPower, FEniCSx. Four emission modes divide the core tier almost evenly —
`code-execution` 29, `file-io` 26, `api` 19, `mcp` 18 — and the newest of them, a typed tool
surface the agent selects from rather than writes to, is also the only one with a head-to-head
measurement behind it: the same models on the same tasks went from 16% to 89% task success when
moved from writing simulator-driving code to calling typed tools, a gap the authors attribute
to the paradigm rather than the retry budget
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]].

[Certain] What closes the loop is narrower than what opens it. 74 of 98 core systems iterate
autonomously, and the loop is almost always *read the error, revise, resubmit, stop at a cap*.
Far fewer read the solver's physics rather than its exit status; energy-balance gating
[[doi:10.5281/zenodo.22554152]], chi-squared targeting [[doi:10.1016/j.bdes.2026.100042]] and a
plausible-barrier window [[arxiv:2606.05050]] are the clearest instances in the corpus. One
source measured the difference directly: 82.1% of its runs executed, 68.12% were scientifically
meaningful [[doi:10.1002/aidi.202500174]].

## Against TANGO's surfaces

[Certain] Touchpoint coverage is heavily uneven. Per row, across 183: config-generation 96,
solver-control 76, results-interpretation 57, verification-regression 45, optimisation-loop 42,
hpc-scale-out 33, tool-exposure 32, provenance-reproducibility 24, topology-construction 23,
surrogate-modelling 17, uncertainty-quantification 10, techno-economic 6. Section 03 gives the
core-only counts beside these, and the difference matters: an abstract over-reports scope.

[Absent-searched] (backed by query cells `q007`-`q010`) No admitted source drives a full life-cycle cost model — levelised cost,
discounted cash flow or equivalent — as the system it controls. Economic quantities appear as
objectives inside optimisation loops, not as the driven artefact. The energy-systems and
geoenergy cells (`q007`–`q010`) were harvested without a paging cap on the OpenAlex side and
eighteen further targeted web searches were logged.

## Maturity

[Certain] Demonstrated maturity across 98 core rows: M0 3, M1 37, M2 47, M3 11. All 85 context
rows are `not stated (abstract only)`.

[Absent-searched] (backed by query cells `q001`-`q014`) **Nothing in the corpus reaches M4 or M5.** No source shows a system in
routine use by people other than its authors, or an output that entered a real operational
decision with third-party evidence. The 11 M3 rows are retrospective work against references
the authors did not produce — a real reservoir [[doi:10.48550/arxiv.2605.15028]], named
catalyst systems [[arxiv:2606.05050]], real crash-validation decks
[[doi:10.5281/zenodo.22554152]], a hand-written expert implementation
[[doi:10.48550/arxiv.2607.15001]]. Several authors say so in their own terms: "an early
exploration rather than a production-ready solution" [[doi:10.1080/19401493.2026.2653969]];
"early experience, not a controlled productivity benchmark"
[[doi:10.20944/preprints202608.1323.v1]].

## What the evidence will not support

[Certain] 26 of 98 core sources report no baseline. 52 do not state whether their evaluation
data was held out. Only one benchmark in the corpus — FoamBench [[doi:10.48550/arxiv.2509.20374]]
— was picked up and reused unchanged by an independent group [[arxiv:2602.11689]], and it is
confined to CFD. 21 of 98 core sources state nothing about what happens when the driven code
fails, and that silence was searched for and recorded, not inferred.

[Certain] The access picture is part of the evidence. 15 records screened as core could not be
read in full and were demoted, so **13% of the intended deep-read was lost**, mostly to
preprint servers and publishers that refuse automated clients rather than to licensing. Two
admitted sources could not be read at all. `paywalled.md` and `unreachable.md` record every
route tried and what each source would have changed.
