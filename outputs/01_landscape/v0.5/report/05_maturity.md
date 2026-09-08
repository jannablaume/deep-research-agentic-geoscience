# 05 Maturity

Counts below are sources (rows). Each of the 23 core rows is a distinct `system_id`.

## Distribution (core, n = 23 sources)

[Certain] M1: 10 sources. M2: 7. M3: 5. M4: 1. M0: 0. M5: 0.

[Certain] M4 is HERMES: unedited extraction archived, expert-adjudicated, released as the
live Treatise.geoLex database (32,277 entities, 451,878 attributes, 55 volumes, 53
person-days) [[doi:10.48550/arxiv.2608.14055]]. The adjudicating palaeontologists are
co-authors, so the verification is not independent of the producing group; that is why
the row is not M5.

[Certain] M3 sources are PetroGraph on Norne [[arxiv:2605.15028]], TADI on named Volve
wells [[doi:10.48550/arxiv.2605.00060]], TRACE on Ridgecrest and Santorini–Kolumbo
[[doi:10.48550/arxiv.2603.21152]], GraphRAG on Qiaojia, Ridgecrest and Maduo catalogs
[[doi:10.48550/arxiv.2607.24984]], and the PPV Evaluator-Optimizer on a 2024 railway
tunnel in Xiushan County, Chongqing [[doi:10.3390/geosciences16050176]]. Four of those
five use public or published field datasets; one (PPV) uses a named site's own blast logs.

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

[Certain] One hundred and thirty-two admitted sources are abstract-only for maturity
purposes, including 65 in reservoir_engineering. Two abstracts describe evaluations
shaped like M3 — Hydro-Agent on the Aquia Aquifer along a 96 km flow path
[[doi:10.1016/j.watres.2026.125886]] and map generalisation on the Chagai Belt
[[doi:10.1016/j.oregeorev.2026.107477]] — and neither is counted, because no evaluation
section was readable.

[Likely] The core distribution is therefore biased toward preprint and open-journal
systems, and biased away from SPE, EAGE, Elsevier and IEEE field papers. Reading M1 = 10,
M2 = 7, M3 = 5, M4 = 1 as a survey of the field's operational maturity over-weights the
readable slice.

## Abstract-only counts by subfield (admitted sources)

[Certain] geomechanics 1/1 abstract-only; seismology 19/27; hydrogeology 4/4;
reservoir_engineering 65/68; geothermal 3/4; ccs 2/4; mining 11/14;
engineering_geology 15/19; inversion 5/5; geological_modelling 7/9.
