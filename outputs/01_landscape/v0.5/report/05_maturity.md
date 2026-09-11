# 05 Maturity

Counts below are sources (rows). Each of the 38 core rows is a distinct `system_id`.

## Distribution (core, n = 38 sources)

[Certain] M1: 14 sources. M2: 11. M3: 12. M4: 1. M0: 0. M5: 0.

[Certain] M4 is HERMES: unedited extraction archived, expert-adjudicated, released as the
live Treatise.geoLex database (32,277 entities, 451,878 attributes, 55 volumes, 53
person-days) [[doi:10.48550/arxiv.2608.14055]]. The adjudicating palaeontologists are
co-authors, so the verification is not independent of the producing group; that is why
the row is not M5.

[Certain] M3 sources are PetroGraph on Norne [[arxiv:2605.15028]], TADI on named Volve
wells [[doi:10.48550/arxiv.2605.00060]], TRACE on Ridgecrest and Santorini–Kolumbo
[[doi:10.48550/arxiv.2603.21152]], GraphRAG on Qiaojia, Ridgecrest and Maduo catalogs
[[doi:10.48550/arxiv.2607.24984]], the PPV Evaluator-Optimizer on a 2024 railway
tunnel in Xiushan County, Chongqing [[doi:10.3390/geosciences16050176]], Hydro-Agent on
the named Aquia Aquifer, Maryland [[doi:10.1016/j.watres.2026.125886]], OntoGRC on the
named Xinjiang Taxkorgan–Yecheng Fe–Pb–Zn assessment report
[[doi:10.1016/j.oregeorev.2026.107411]], the tunnel geological-forecasting agent on five
named tunnels in Yunnan Province [[doi:10.1016/j.autcon.2026.107055]], InsightsAI on
the named Volve field [[doi:10.2118/229435-ms]], a landslide-reconstruction agent on four
named historical Hong Kong landslides [[doi:10.1016/j.sandf.2026.101789]], AGeoKE on the
named USGS Mineral Deposit Models and NASA Lunar Sample Compendium
[[doi:10.1016/j.acags.2026.100362]], and GAGAW on three named US hydrology field sites
[[doi:10.1016/j.bdes.2026.100042]]. Ten of those twelve use public, published, or
government/agency-maintained reference sources; two (PPV, the tunnel forecasting agent)
use a named site's own field records collected for the study.

[Certain] M3 here is named-site retrospective evaluation, not operator deployment. No core
source shows an output entering a time-bounded operational decision at a named operator
except HERMES's curation workflow, which is M4 and is not a field deployment.

[Certain] AutoSurrogate's GCS case is a synthetic 80×80×20 aquifer generated with SGeMS
and GEOS, with no named site, so the rubric scores it M1 even though the test split is
held out [[doi:10.1016/j.aei.2026.105058]]. Agents4GEOS on PUNQ-S3 is M2: a reusable
benchmark, not a named field campaign [[arxiv:2607.18557]].

## Claimed versus demonstrated

[Certain] Several M1 sources claim disciplinary primacy or industrial practicality.
GAIA is "the pioneering effort in building an agentic AI system for geothermal project
assistance" and is demonstrated on a homemade unpublished QA set plus a synthetic
inversion the authors say "under-represents real world scenario"
[[doi:10.48550/arxiv.2511.03852]]. GeoMCP offers a "blueprint for transitioning the
industry" and is demonstrated on one Eurocode 7 worked example
[[doi:10.48550/arxiv.2603.01022]]. MINDS claims it can "systematize economic scenario
analysis without sacrificing the governance and verification required for definitive
feasibility studies" on the synthetic Marvin model [[doi:10.3390/mining6020026]].
specfem-mcp claims the first MCP application to computational seismology and reports no
number [[doi:10.48550/arxiv.2512.14429]]. AutoSurrogate claims a "viable approach for
realistic subsurface flow applications" on an unnamed synthetic aquifer
[[doi:10.1016/j.aei.2026.105058]].

[Certain] The gap is itself a finding of the rubric: `maturity_claimed` is the authors'
strongest self-assertion, `maturity_demonstrated` is what the evaluation section shows.

## What the context tier cannot contribute

[Certain] One hundred and thirteen admitted sources are abstract-only for maturity
purposes, including 62 in reservoir_engineering. This run recovered full text for
nineteen paywalled or unreadable records via institutional access after this report was
first drafted, across two recovery passes (see `unreachable.md`): fifteen turned out to be
genuinely agentic and are now counted above at M1–M3, and four — from the first pass only,
including a second Ore Geology Reviews map-generalisation paper on the Chagai Belt
(`doi:10.1016/j.oregeorev.2026.107477`, not admitted) that had looked M3-shaped from its
abstract alone — turned out not to be agentic once the mechanism was visible in full text,
and are excluded from the corpus entirely rather than left in context. Every record in the
second recovery pass turned out to be genuinely agentic. That earlier reversal is itself
evidence for the caveat below: an abstract can look like a qualifying system and not be
one, in either direction.

[Likely] The core distribution is still biased toward preprint and open-journal
systems, and biased away from SPE, EAGE, and IEEE conference-proceedings papers whose full
text remains unread. Reading M1 = 14, M2 = 11, M3 = 12, M4 = 1 as a survey of the field's
operational maturity over-weights the readable slice.

## Abstract-only counts by subfield (admitted sources)

[Certain] geomechanics 0/0 abstract-only (no admitted source); seismology 17/27;
hydrogeology 3/5; reservoir_engineering 62/69; geothermal 3/4; ccs 2/4; mining 9/13;
engineering_geology 10/19; inversion 2/2; geological_modelling 5/8.
