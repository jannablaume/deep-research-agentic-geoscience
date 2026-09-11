# 01 Control patterns

[Certain] How agents drive a simulator, solver or engineering model: what they emit, what they
read back, and what closes the loop. Grouped by pattern. Counts are per `transfer.csv` row and
are restricted to the 98 `core` rows unless stated, because a context row's interface and
autonomy come from an abstract.

## What the agent emits

[Certain] Four emission modes account for all but one core row, and the split is close to
even:

| interface | core rows | all rows |
|---|---|---|
| code-execution | 29 | 38 |
| file-io | 26 | 30 |
| api | 19 | 27 |
| mcp | 18 | 26 |
| cli | 5 | 10 |
| not stated | 1 | 50 |

[Certain] `file-io` is the oldest and plainest pattern: the agent writes the simulator's own
input format and the simulator reads it. OpenFOAM case directories with `controlDict`,
`fvSchemes`, `fvSolution` and an execution script [[doi:10.1016/j.taml.2025.100594]]; EnergyPlus
input files edited object by object [[doi:10.26868/30680611.2026.1305]]; ECLIPSE-format decks
substituted at named keywords [[doi:10.48550/arxiv.2605.15028]]; LS-DYNA keyword decks edited
by block match-and-replace [[doi:10.5281/zenodo.22554152]]; a vendor process simulator whose
input files the agent writes and whose engine it then triggers
[[doi:10.48550/arxiv.2603.12813]]. The attraction is that nothing new has to be built; the
cost, reported repeatedly, is that a free-form text file is exactly where a language model can
invent a keyword that does not exist.

[Certain] `code-execution` moves the boundary: the agent writes a program that calls the
solver's library API, and the program rather than the file is the artefact. Python driving
ASE and CHGNet relaxations [[doi:10.48550/arxiv.2506.05616]], SciPy integrators and linear
algebra called from generated programs [[doi:10.48550/arxiv.2408.15866]], PyQUDA measurement
scripts generated with their own submission artefacts [[doi:10.48550/arxiv.2607.15001]],
scikit-learn and neuroimaging toolchains invoked inside pinned environments and containers
[[arxiv:2604.24696]] [[doi:10.48550/arxiv.2601.09749]]. This mode is where the corpus's
strongest verification results sit, because a program can be diffed against a reference
program in a way an input deck cannot [[doi:10.48550/arxiv.2607.15001]].

[Certain] `mcp` and `api` invert the arrangement: the agent does not write anything executable
at all, and instead selects from a fixed, typed tool surface someone else authored. This is
the newest pattern in the corpus by publication date and it is growing — 26 of 183 rows —
and its sources are explicit about why. A typed layer "removes that entire failure mode: the
model calls `get_stream_data`, `set_block_conditions`, `build_flowsheet_from_spec`, … and the
schema does the rest"
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]];
"requests that do not match a tool's declared input format are rejected before they reach the
simulator" [[doi:10.26434/chemrxiv.15006587/v1]]. Section 03 records the one head-to-head
measurement of this choice.

## What the agent reads back

[Certain] Almost every core system reads the solver's exit status; far fewer read its physics.
Three levels appear, and sources rarely implement more than one:

- **Did it run.** [Certain] The commonest. A return code, a log line, an error file. The EnergyPlus workflow reads the `.err` file to find "the problematic class and its object name" [[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]]; the OpenFOAM agent is "directed to use OpenFOAM's error logs to identify the first failure" [[arxiv:2602.11689]]; the SWMM pipeline records "the swmm5 return code" in its manifest [[doi:10.31223/x5f47g]].
- **Did it converge.** [Certain] Less common, and where it appears it is usually named as a distinct category from a crash. A run that exceeds "72 hours at most 10 correction attempts" without a convergent solution counts as failed [[doi:10.1016/j.taml.2025.100594]]; a nudged-elastic-band run that fails to converge triggers a geometric diagnosis and a targeted correction [[arxiv:2606.05050]]; a contingency tool "runs baseline PF first; explicit error on non-convergence" [[arxiv:2602.20683]].
- **Is it physically right.** [Certain] Rarest. Energy-balance and mass-error diagnostics gate the score, so a run that terminates but violates energy conservation "is not scored as though it were trustworthy" [[doi:10.5281/zenodo.22554152]]; a chi-squared target of approximately 1.0 separates underfitting from overfitting [[doi:10.1016/j.bdes.2026.100042]]; a barrier outside a physically plausible window returns the candidate to redesign [[arxiv:2606.05050]].

[Certain] One source states the consequence of stopping at the first level: executability and
scientific validity were measured separately and diverged by fourteen points, 82.1% against
68.12% [[doi:10.1002/aidi.202500174]]. Another states it as a design principle — successful
execution "does not by itself establish scientific correctness" — and therefore compares every
generated workflow numerically against a trusted reference [[doi:10.48550/arxiv.2607.15001]].

## What closes the loop

[Certain] 74 of 98 core rows are `executes-and-iterates`, 18 are `executes-with-approval`, 2
are `suggests` and 4 are `not stated`. The dominant loop is therefore read-error, revise,
resubmit, repeat until success or a cap. The caps are stated often enough to be a pattern in
themselves: 10 correction attempts [[doi:10.1016/j.taml.2025.100594]], 10 iterations
[[arxiv:2606.05050]], 3 review iterations [[arxiv:2607.18557]], 30 agent steps
[[title:mcpsolvermodelcontextprotocolserverforconstraintsolvingsatmaxsatsmtcpaspdp]], "a
user-specified limit on the number of iterations" [[doi:10.48550/arxiv.2607.22596]], and a
reflection budget beyond which the authors report that roughly 22 further iterations "often
fail to resolve remaining errors" [[doi:10.1002/aidi.202500174]].

[Certain] The 18 `executes-with-approval` rows are not a weaker version of the same thing; they
place the gate in different positions, and the position is the design decision. Before the run:
a critic sub-agent must approve the setup, which the repository states is "a hard precondition,
not a workflow suggestion" [[doi:10.5281/zenodo.20543501]]; a three-question decision gate is
returned to the user, each question carrying a recommendation and its trade-off
[[arxiv:2607.18557]]; engineers "review and approve agent-proposed plans before launching
workflows with hundreds of simulation jobs"
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]]. Before a specific
*class* of change: "a physics-classified fix requires a human to supply its exact error code to
`--approve` before it is applied" [[doi:10.5281/zenodo.22554152]]. After the plan but before
the search: a checkpoint "allows the user to adjust parameters and their bounds on the fly"
[[doi:10.48550/arxiv.2605.15028]].

[Certain] A distinct third arrangement appears in a handful of systems: the loop is closed not
by the agent but by a conventional optimiser the agent configured and launched. The agent sets
up the search and steps out of it [[doi:10.1016/j.net.2026.104573]]
[[doi:10.1016/j.taml.2026.100660]] [[doi:10.48550/arxiv.2604.11945]]. One source makes the
architectural case for this explicitly — confining model invocations to bounded planning
stages and delegating "all tool dispatch, parallel scheduling, arithmetic derivation, and
artifact routing to a deterministic … executor that consumes zero LLM tokens during execution"
[[doi:10.26434/chemrxiv.15002405/v1]].

## Where the loop is not closed at all

[Certain] 21 of 98 core sources state nothing about what happens when the driven code fails.
That is not a reading failure: each of these was read in full, with the evaluation and
limitations sections attended to, and the entry in `transfer.md` records `NOT FOUND` against a
search for such a statement [[doi:10.1145/3731599.3767349]] [[doi:10.25394/pgs.32118403]]
[[doi:10.1063/5.0294696]] [[doi:10.1016/j.taml.2026.100660]] [[doi:10.1109/access.2025.3605803]]
[[doi:10.1016/j.softx.2025.102367]] [[doi:10.1080/19401493.2026.2653969]]
[[doi:10.3929/ethz-c-000801434]]. In several the only nearby sentence is a capability
description that stops short: one paper's sole statement about convergence is that its tool
layer can "launch a simulation and monitor convergence status", with nothing about the response
to a failed solve [[doi:10.1109/access.2025.3605803]].

[Certain] Section 06 treats what those authors do say about their limits. The relevant point
here is structural: the corpus documents the success path of the control loop far better than
its failure path, and it does so consistently enough across domains, venues and years that it
reads as a convention of the literature rather than a property of any one system.
