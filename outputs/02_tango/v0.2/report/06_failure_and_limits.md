# 06 Failure and limits

[Certain] What authors report their systems could not do, in their own words. Quoted rather
than paraphrased, because the value of this section is that these are concessions the authors
chose to make. Counts are over the 101 `core` rows, where the limitations section was read.

## How much is stated at all

[Certain] 97 of 101 core sources state at least one limitation of their own; **4 state none**
[[doi:10.11578/dc.20260516.1]] [[doi:10.5281/zenodo.19597589]] [[doi:10.69997/pse.120458]]
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]]. Two of those four
are short-format sources — a two-page conference extended abstract with no limitations section
in existence [[doi:10.69997/pse.120458]] and a vendor blog post
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]] — so the absence is
partly a fact about the format.

[Certain] Separately, **21 of 101 core sources state nothing about what happens when the driven
code fails**, and that silence is recorded as `NOT FOUND` in `transfer.md` rather than inferred
(see section 01). Failure *handling* and stated *limitations* are different things, and a
source can be generous with one and silent on the other: one system reports a detailed failure
taxonomy in its own logs while its limitations section concedes only that small models cannot
write working scripts
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]].

## Geometry and meshing

[Certain] The most concrete recurring concession, in 16 core sources. "The lack of spatial
reasoning capabilities in LLMs appears to produce an incorrect geometry and mesh. We highlight
that the ability of LLMs to understand geometry is a major area in need of improvement"
[[doi:10.48550/arxiv.2509.20374]]. "Errors that go unnoticed or are more complex, such as
failing to properly represent an obstacle in the mesh or other physics-related issues, are more
challenging for LLM agents to address. These types of errors require a deeper understanding of
the underlying physics, which the agent currently lacks. As such, human oversight remains
essential" [[arxiv:2602.11689]]. "Meshing complex reservoirs is particularly challenging and
warrants a dedicated specialized agent" [[arxiv:2607.18557]]. One system's mesh quality is
reported as "largely determined by the LLM model itself" rather than by the framework
[[arxiv:2602.11689]].

## Physics that the code will accept but the world will not

[Certain] Nine core sources concede a version of the same problem: the generated artefact is
syntactically valid, runs, and is wrong. Stated most directly: language models "excel at
high-level linguistic narration but consistently struggle to enforce the complete chain of
physical constraints within the generated executable code" [[doi:10.1002/aidi.202500174]]. The
same paper reports its failures concentrated "in combustion and multiphase flow categories due
to their interdisciplinary complexity". Another traces its failures to "divergence caused by
unreasonable parameter values, such as dissipation rates in the k-epsilon model … set orders of
magnitude too high" [[doi:10.1016/j.taml.2025.100594]]. A third reports that even when "the
syntax is right and validated, some errors are only caught at running time"
[[arxiv:2607.18557]]. A fourth reports a run whose "variable resolution failed silently" and
produced "velocities 30x too low" [[doi:10.5281/zenodo.20543501]].

[Certain] One source separates this from execution failure and measures it: 82.1% of cases ran,
68.12% were scientifically meaningful [[doi:10.1002/aidi.202500174]]. Another reports the same
distinction as a design conclusion — successful execution "does not by itself establish
scientific correctness", so numerical regression against a trusted reference "remains
necessary" and "for new observable classes reference comparisons and human review remain
essential" [[doi:10.48550/arxiv.2607.15001]].

## Non-convergence and where iteration stops helping

[Certain] Nine core sources name convergence as a limit rather than a handled case. "In
preliminary attempts on high-speed combustion setups, the agent often triggered solver crashes
or divergence and did not consistently converge to a stable configuration through log-driven
edits alone" [[arxiv:2602.11689]]. "Even for ChatCFD, reflections beyond 75% of the limit
(approximately 22 iterations) often fail to resolve remaining errors, highlighting a current
limitation in LLM-based CFD agents where complex case errors require advanced knowledge
integration or alternative strategies beyond iterative reflection"
[[doi:10.1002/aidi.202500174]]. One pipeline resolves convergence failure by simplifying the
model and says so: "potential simplifications necessary to achieve convergence are recorded
transparently" [[doi:10.69997/pse.120458]]. One states the boundary where its agent must hand
back: on solver non-convergence "the agent routes to human review rather than issuing an
autonomous approval recommendation" [[arxiv:2602.20683]].

## Cost, in tokens and in wall time

[Certain] Five core sources name cost as a limit rather than a metric. "Token usage has emerged
as a meaningful factor in the overall budget, one that is no longer secondary to CPU or GPU
hours" [[arxiv:2607.18557]]. "Token consumption and API latency accumulate across extended
sessions, making scripted approaches potentially more efficient for large-scale parametric
studies" [[doi:10.1080/19401493.2026.2653969]]. "Reliability costs tokens, not time"
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]]. One
reports each run taking "around 4 hours" and names response time as unsuitable for larger
studies [[doi:10.1038/s44172-025-00583-3]]; another reports that only four backends were tested
"primarily due to API cost constraints" [[doi:10.3929/ethz-c-000801434]].

## Hallucination and non-determinism

[Certain] Five core sources name it explicitly, and their framings differ in a way worth
preserving. One reports it as persistent despite mitigation: hallucinations "such as inserting
unnecessary Markdown formatting, which can disrupt error correction … Despite mitigation efforts
using prompt engineering and pydantic for structured outputs, these issues persist"
[[doi:10.1002/aidi.202500174]]. One reports it as a risk conditional on engineering not yet
done: hallucinations "pose risks without stricter schema validation, tests, and version
pinning" [[doi:10.1016/j.bdes.2026.100042]]. One reports it as a tool-selection problem at
scale, adding that "LLM non-determinism means identical prompts may yield different tool
sequences across sessions" [[doi:10.1080/19401493.2026.2653969]]. One reports the failure mode
it designed out rather than mitigated — invented object paths accounting for 78% of
code-generation failures, which "cannot occur through typed tools"
[[doi:10.26434/chemrxiv.15006587/v1]]. The fifth reports it as an observed incident rather than
a category: given only five search results for a request naming eight structures, the agent
supplied eight PDB IDs of which three identify unrelated proteins — "These PDB IDs were
hallucinated by the LLM agent, as only 5 search results were generated from the researcher" —
and the authors add that "Based only on the model context, it failed to provide correct
information for the following simulation runs" [[doi:10.1145/3731599.3767349]]. This last was
not visible in v0.1, which read that source from its preprint; the passage is in the published
version only.

[Certain] One source reports the most uncomfortable version of this, from the human side rather
than the model side: "Language models are strong at producing coherent and plausible
explanations, which can lead to over confidence in their methods, summaries and outputs", and
adds that the file volume from a short agent session "can rapidly become overwhelming for human
verification", so that in HPC production workflows the verification burden "can become
unmanageable" [[doi:10.20944/preprints202608.1323.v1]].

## Scope, and the honesty about it

[Certain] The commonest concession, in 30 core sources, is simply that the demonstration is
narrow. It is usually stated precisely enough to be useful: "the workflow depends on a
pre-existing baseline IDF, assuming that building geometry and HVAC topology are already
defined", which "restricts applicability in early-stage design" [[doi:10.26868/30680611.2026.1305]];
"each case study begins with the assumption that the model geometry is already established"
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]];
"the current tool set focuses on model analysis and modification rather than complete model
creation from scratch" [[doi:10.1016/j.softx.2025.102367]]; "geophysics coverage is narrow,
centered on ERT, seismic refraction, and basic climate linkage"
[[doi:10.1016/j.bdes.2026.100042]]; "the demonstrations in this paper employed a relatively
simple residential model with three thermal zones and ideal loads"
[[doi:10.1080/19401493.2026.2653969]]; "benchmark problems are limited to Beams2D and
Photonics2D" [[doi:10.3929/ethz-c-000801434]].

## Human oversight, stated as permanent rather than transitional

[Certain] Five core sources make a claim that stands apart from the rest, because it is about
where the ceiling is rather than where the work has got to. "GAGAW is designed to augment, not
replace, geophysical expertise", and users "should examine inversion convergence, data misfit
distributions, and petrophysical parameter selections from the final report before accepting
final results" [[doi:10.1016/j.bdes.2026.100042]]. "Human oversight remains essential"
[[arxiv:2602.11689]]. "The reservoir simulation assistant is designed to augment, not replace,
the established tools of the trade"
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]]. Set against these are
sources whose abstracts claim operation "without manual intervention"
[[doi:10.1109/access.2025.3605803]] [[doi:10.26868/30680611.2026.1305]]. This report does not
adjudicate between them; both positions are held, in the same corpus, in the same year, and
section 05 records how each squares with what was measured.

## What no source reports

[Absent-searched] (backed by query cells `q001`-`q014`) **No admitted source reports a case where its agent's output was accepted,
acted on outside the experiment, and later found to be wrong.** Failures are reported as
run-time errors caught inside the loop, as benchmark cases not passed, or as capability gaps
for future work — never as a downstream consequence. One source comes closest and marks the
boundary: hallucinated PDB IDs were accepted by the pipeline and molecular dynamics ran on the
wrong protein structures before the authors identified them [[doi:10.1145/3731599.3767349]].
That is an incorrect output acted upon, but inside the authors' own experiment and reported by
them; no source reports one reaching a decision, a publication or a user. The core query cells were harvested in full after the paging caps were
raised (`q001` through `q014`) and the grey pass added eighteen targeted web searches; nothing
admitted describes an incident, a retraction, or a corrected result. Given that section 05
finds no source above M3, this is what one would expect — systems that have not entered routine
use cannot yet have failed in it — but it means the corpus contains no evidence at all about
how these systems behave when they are trusted.
