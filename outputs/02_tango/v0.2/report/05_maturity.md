# 05 Maturity

[Certain] Demonstrated maturity across the corpus, how often the claim outruns it, and how much
of the picture is missing because the source could not be read.

## Distribution

[Certain] Demonstrated maturity, rated from the evaluation section only, across the 101 `core`
rows:

| level | core rows |
|---|---|
| M0 | 3 |
| M1 | 38 |
| M2 | 48 |
| M3 | 12 |
| M4 | 0 |
| M5 | 0 |

[Certain] All 82 `context` rows carry `not stated (abstract only)`. That figure is not a
rounding detail: **45% of the admitted corpus has no maturity rating at all**, and 12 of those
82 are records that were screened as core and demoted when their full text proved unreadable.
`paywalled.md` lists those 12 with what reading them would change; three of them are the sort of
source most likely to sit above M2 — including one whose top agent-proposed candidate was
synthesised and measured at 113 mS cm⁻¹ with durability beyond 2,000 hours
[[doi:10.6084/m9.figshare.30931802]]. The maturity distribution above therefore **understates**
the field rather than guessing at it.

[Certain] That understatement is measurable rather than asserted, because v0.2 measured part of
it. Three of the fifteen records demoted in v0.1 were retrieved by hand and read, and all three
turned out to support a core write-up: one rated M1 [[doi:10.1039/d5dd00435g]], one M2
[[doi:10.26434/chemrxiv.15006587/v1]], and one M3 on six named buildings validated against
metered data [[doi:10.2139/ssrn.7333555]]. Reading three of fifteen demotions moved the M3 count
from 11 to 12 and the M2 count from 47 to 48.

## The ceiling

[Absent-searched] (backed by query cells `q001`-`q014`) **No admitted source demonstrates M4 or M5.** Nothing in the corpus shows a
system in routine use by people other than its authors, or one whose output entered a real
operational or design decision with third-party evidence. The core query cells were harvested
in full after the paging caps were raised (`q001` through `q014`), the grey pass added eighteen
targeted web searches aimed precisely at vendor and deployment material where such evidence
would appear, and the industry sources it found report demonstrations rather than deployments
[[title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving]]. Several sources say
as much themselves: "this work represents an early exploration rather than a production-ready
solution" [[doi:10.1080/19401493.2026.2653969]]; "strong benchmark performance should be
interpreted as infrastructure readiness rather than clinical readiness" [[arxiv:2604.24696]];
"the results are early experience, not a controlled productivity benchmark"
[[doi:10.20944/preprints202608.1323.v1]].

## What M3 looks like here

[Certain] The 12 M3 rows are the corpus's high-water mark, and eleven of the twelve are
retrospective work on real, named data: a real reservoir [[doi:10.48550/arxiv.2605.15028]], a
real catchment [[doi:10.31223/x5f47g]], three named hydrogeophysics field sites
[[doi:10.1016/j.bdes.2026.100042]], real crash-validation decks scored against published
experimental corridors [[doi:10.5281/zenodo.22554152]], published kinetics for seven named
catalyst systems including one blind prediction [[arxiv:2606.05050]], measured
vector-network-analyser data for a physical package [[doi:10.1109/access.2025.3605803]], a
named gauge ensemble with every workflow checked against a hand-written expert implementation
[[doi:10.48550/arxiv.2607.15001]], a real research nuclear reactor model
[[doi:10.25394/pgs.32118403]], a genomics platform's own production jobs
[[doi:10.1145/3815572.3815744]], a named field campaign [[arxiv:2607.11084]] and six named
Purdue University campus buildings whose calibrated models were validated against metered
energy-use intensities held back until after calibration [[doi:10.2139/ssrn.7333555]]. The
twelfth is rated M3 on named machines rather than named data — real work on OLCF Frontier and
Wombat, reported retrospectively [[doi:10.20944/preprints202608.1323.v1]].

[Certain] What separates M3 from M2 in every one of these cases is the same thing: a reference
the authors did not themselves produce. None of them claims the output changed a decision, and
that is exactly the gap between M3 and M4.

## What M0 looks like here

[Certain] Three core rows sit at M0, and each is honest about why. One states that its agent
layer, experimental layer and dashboard are "designed but not yet implemented" and that "no
physical experiments, RL-optimized syntheses, or live dashboard deployments are reported in
this work", so the computation it does report was run by the authors' own scripts rather than
by an agent [[doi:10.5281/zenodo.19835550]]. The other two are architecture and framework
descriptions without an evaluated agent run [[doi:10.11578/dc.20260516.1]]
[[doi:10.1016/j.compenvurbsys.2026.102449]]. M0 in this corpus means "described, not run",
never "run and failed".

## Where the claim outruns the demonstration

[Certain] The gap is real but it is narrower than the literature's reputation would suggest.
Of the 40 core sources demonstrating M0 or M1, **7 make a claim whose language reaches
substantially further than the evidence rated** — autonomy, a new paradigm, or a
state-of-the-art position [[doi:10.48550/arxiv.2511.00122]] [[arxiv:2605.23273]]
[[doi:10.48550/arxiv.2512.13930]] [[doi:10.48550/arxiv.2509.10210]]
[[doi:10.48550/arxiv.2604.11945]]. The remaining 33 make claims proportionate to a
demonstration: a prototype, a proof of concept, a first implementation.

[Certain] Two specific forms of overreach recur and are worth separating. The first is
**autonomy claimed in the abstract and human involvement reported in the experiments.** One
source claims a system that works "all without manual intervention" while its own results
section contains no statement of who pressed run [[doi:10.1109/access.2025.3605803]]; another
claims end-to-end automation "without manual intervention" while a human supplies each of the
three natural-language goals [[doi:10.26868/30680611.2026.1305]]. Where authors resolve this
themselves they do it cleanly: one reports that "without human guidance, all models fail to
produce valid workflows in all three tasks" and rates its own system as not yet fully
autonomous [[doi:10.48550/arxiv.2506.05616]]; another states that "across the tests, the work
remained human supervised" [[doi:10.20944/preprints202608.1323.v1]].

[Certain] The second is **a 100% success rate reported on a small or self-designed problem
set.** Four core sources report 100% on some axis
[[doi:10.1016/j.ijheatfluidflow.2026.110399]] [[doi:10.26868/30680611.2026.1305]]
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]]
[[doi:10.31223/x5f47g]], and in each the qualifier is in the text rather than the headline: one
holds "when provided with well-formulated user queries under carefully designed system
prompts" [[doi:10.1016/j.ijheatfluidflow.2026.110399]], one counts syntax validity rather than
physical correctness [[doi:10.26868/30680611.2026.1305]], one is ten trials on one building
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]].
Against these, the two sources that evaluate on a third-party benchmark report 14% and 34%
[[doi:10.48550/arxiv.2509.20374]] and 82.1% execution against 68.12% physical fidelity
[[doi:10.1002/aidi.202500174]]. The corpus does not adjudicate this difference and neither does
this report; both numbers are what their authors measured, on what they chose to measure it on.

## Counter-examples worth recording

[Certain] A minority of sources state their own ceiling explicitly and rate themselves below
what their results would allow. One writes "this work does not claim autonomous scientific
discovery or fully automated research. The framework is designed to assist, not replace, human
scientific judgment" [[doi:10.48550/arxiv.2601.09749]]. One writes that its system "does not
claim state-of-the-art performance or present exhaustive cross-system leaderboards" and that
its gains "should therefore be interpreted conservatively" [[arxiv:2604.24696]]. One separates
implemented from designed components with solid and dashed borders in its own architecture
figure [[doi:10.5281/zenodo.19835550]]. One reports that its conductivity estimate "is a
calibrated consistency check rather than a blind prediction"
[[doi:10.5281/zenodo.19835550]].

## Year

[Certain] Publication years across all 183 rows: 2026 — 127, 2025 — 50, 2024 — 6. More than two
thirds of the corpus is from the most recent year, which is the single most important caveat on
every maturity number above: a literature this young has had no time to produce the multi-year
deployment evidence that M4 and M5 require.
