# 04 Evaluation

[Certain] How these systems were tested, against what, on what data, and whether the field
shares any benchmark. All counts are over the 98 `core` rows; context rows are excluded because
an abstract does not reliably report an evaluation design.

## Data

[Certain] `data_type` across core rows: benchmark 51, synthetic 28, real-field 14, not stated 5.
So roughly half of the corpus evaluates on a reusable, site-agnostic problem set, and under a
sixth touches a named real site, facility or measurement campaign.

[Certain] The 14 real-field rows are worth naming because they are what separates a
demonstration from a result. They include the Norne reservoir [[doi:10.48550/arxiv.2605.15028]],
the Tod Creek catchment [[doi:10.31223/x5f47g]], three western-US hydrogeophysics sites
[[doi:10.1016/j.bdes.2026.100042]], the NREL iUnit building [[doi:10.26868/30680611.2026.1305]]
[[doi:10.1080/19401493.2026.2653969]]
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]],
named OLCF systems [[doi:10.20944/preprints202608.1323.v1]], measured vector-network-analyser
data for a physical package [[doi:10.1109/access.2025.3605803]], real crash-validation decks
scored against published experimental corridors [[doi:10.5281/zenodo.22554152]], published
catalytic kinetics for seven named catalyst systems [[arxiv:2606.05050]], a production
university cluster [[doi:10.1145/3785462.3815873]], and public neuroimaging cohorts
[[arxiv:2604.24696]].

## Baselines

[Certain] **26 of 98 core sources report no baseline at all** — the result is the system
working, compared against nothing. Where a baseline exists it is one of four kinds, and the
kinds are not equivalent:

- **A human.** [Certain] Rare and usually informal: two named modellers taking two weeks and four hours against the workflow's nine minutes [[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]]; "a graduate student with 1-2 years of BEM experience typically requires about 2.5 h" [[doi:10.1080/19401493.2026.2653969]]; "an unassisted human computational researcher" [[doi:10.20944/preprints202608.1323.v1]]; a hand-written expert reference implementation compared at machine precision, which is the only rigorous human baseline in the corpus [[doi:10.48550/arxiv.2607.15001]]. One source states plainly why it did not attempt one: "establishing appropriate human references is non-trivial because performance depends strongly on the evaluator's domain knowledge and experience, which are difficult to standardize and quantify" [[doi:10.48550/arxiv.2509.20374]].
- **An analytical or published reference.** [Certain] The strongest form and reasonably common: an analytical Poiseuille solution [[doi:10.1016/j.ijheatfluidflow.2026.110399]], the Lame solution and a Terzaghi consolidation reference [[doi:10.5281/zenodo.20543501]], published results from two established reservoir simulators [[arxiv:2607.18557]], an accepted Strouhal number [[doi:10.5281/zenodo.20543501]], a field-measured water content [[doi:10.1016/j.bdes.2026.100042]].
- **Another agent system.** [Certain] Increasingly common and the closest thing the field has to competition: MetaOpenFOAM, Foam-Agent and ChatCFD appear as each other's baselines across seven core rows [[doi:10.1002/aidi.202500174]] [[doi:10.48550/arxiv.2509.20374]] [[doi:10.1016/j.taml.2025.100594]] [[arxiv:2602.11689]] [[doi:10.1016/j.taml.2026.100660]].
- **The same system with a component removed.** [Certain] An ablation, not a baseline, though the two are often reported together: removing retrieval or the reviewer costs about ten points [[doi:10.48550/arxiv.2509.20374]]; removing the chain-of-thought annotations takes accuracy from 88.7% to 78.2% [[doi:10.1016/j.taml.2025.100594]]; removing a solver template database "collapses accuracy to 48%" [[doi:10.1002/aidi.202500174]].

## Held-out data

[Certain] `held_out` across core rows: not stated 52, no 26, yes 20. **More than half of the
corpus does not say whether its evaluation problems were separated from whatever the system
was built or tuned on.** Where separation is claimed it is sometimes explicit and checkable —
"there is no configuration overlap between the training and benchmark sets"
[[doi:10.1016/j.taml.2025.100594]], "an automated overlap check confirms zero exact textual
overlap in user turns between the two suites" [[arxiv:2602.20683]], "few-shot demonstrations
selected exclusively from the … training split" [[doi:10.3389/fchem.2026.1914886]] — and
sometimes partial by the authors' own account, as where 205 of 315 benchmark cases "are drawn
from the same corpus used to build the knowledge base" [[doi:10.1002/aidi.202500174]].

## Is there a shared benchmark?

[Certain] Only in CFD, and only recently. FoamBench and the surrounding CFDLLMBench suite are
the one artefact in this corpus that a second, independent group picked up and reused: it was
introduced as a benchmark of 90 knowledge questions, 24 solver-coding tasks and 126 OpenFOAM
cases [[doi:10.48550/arxiv.2509.20374]], and was then used unchanged by a later study to
evaluate a different system [[arxiv:2602.11689]]. Both report low absolute numbers — a best
model at 14% on the coding tasks and 34% on the basic OpenFOAM set in the first
[[doi:10.48550/arxiv.2509.20374]], 9 of 9 advanced cases completed but on a nine-case slice in
the second [[arxiv:2602.11689]].

[Certain] Outside CFD, reuse is of the *problem* rather than of the benchmark. Three
independent building-energy systems evaluate on the same NREL iUnit model without sharing a
scored protocol [[doi:10.26868/30680611.2026.1305]] [[doi:10.1080/19401493.2026.2653969]]
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]],
and the same is true of the OpenFOAM tutorial corpus, MP-20, CrossDocked2020 and the IEEE
118-bus case, each of which anchors exactly one system in this corpus
[[doi:10.48550/arxiv.2506.05616]] [[doi:10.3389/fchem.2026.1914886]] [[arxiv:2602.20683]].

[Absent-searched] (backed by query cells `q001`-`q006` and `q011`-`q014`) **No benchmark in this corpus is shared across domains.** The core query
cells covering simulation orchestration, solver control, scientific computing and
computational discovery (`q001` through `q006`, `q011` through `q014`) were harvested in full
after the paging caps were raised, and the grey pass added eighteen targeted web searches; no
admitted source proposes or uses a cross-domain evaluation of agents driving scientific codes.
Two sources argue for one from opposite directions — one calls for benchmarks that "evaluate
both final predictions and the workflows used to obtain them"
[[doi:10.48550/arxiv.2607.22596]], another notes that its own evaluation "does not yet
constitute a blinded third-party benchmark" [[arxiv:2602.20683]] — but neither builds it.

## What gets measured

[Certain] Three quantities dominate and they measure different things. **Execution success** —
did the run complete — is the commonest, reported as pass rates from 82.1%
[[doi:10.1002/aidi.202500174]] to 100% [[doi:10.1016/j.ijheatfluidflow.2026.110399]]
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]].
**Numerical agreement** against a reference is next, and is where the corpus's tightest results
sit: machine precision on 63 of 70 tasks [[doi:10.48550/arxiv.2607.15001]], under 1.5%
deviation [[doi:10.3390/buildings15173190]], every prediction within a factor of two of
experiment across four orders of magnitude [[arxiv:2606.05050]]. **Cost** is reported
surprisingly often and precisely: $0.020 per solution [[doi:10.1016/j.taml.2025.100594]],
$0.208 per case [[doi:10.1002/aidi.202500174]], $0.0020 per scenario [[arxiv:2602.20683]],
47,085 tokens per run [[doi:10.1080/19401493.2026.2653969]], 343,000 tokens for one session
[[arxiv:2607.18557]], roughly $0.39 total [[doi:10.5281/zenodo.22554152]].

[Certain] Reproducibility is measured by a minority but measured well when it is: ten repeats
with zero schema drift [[doi:10.26868/30680611.2026.1305]], ten repeats with token variance
reported at 16.8% [[doi:10.1080/19401493.2026.2653969]], 100% reproducibility across more than
450 simulations [[doi:10.1016/j.ijheatfluidflow.2026.110399]], 120 repeatability runs across
two parameter sweeps executed by two different interfaces [[doi:10.31223/x5f47g]], and a
replay test scored as a falsifiable question [[doi:10.48550/arxiv.2601.09749]].

## Code availability

[Certain] 56 of 98 core sources give a working repository URL. Of the remainder, several state
the code is forthcoming [[arxiv:2606.05050]] [[doi:10.3929/ethz-c-000801434]], one states that
"the scenario definitions, benchmark runner, and timestamped result artifacts … are included in
the accompanying repository" without giving its address [[arxiv:2602.20683]], and one withholds
configuration on stated data-protection grounds [[doi:10.3389/fchem.2026.1914886]]. One source
notes an availability limit that no repository can fix: "Aspen Plus is proprietary, so the live
simulation paths cannot be reproduced without an Aspen license + Windows"
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]].
