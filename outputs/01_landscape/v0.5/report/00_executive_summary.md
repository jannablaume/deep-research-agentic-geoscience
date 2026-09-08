# 00 Executive summary

LLM-based agentic systems in solid-earth and subsurface geoscience, as harvested and
screened in this run. Descriptive only.

[Certain] The harvest returned 11,191 unique records. Triage shortlisted 712. Screening
admitted 155 (23 core, 132 context). The below-cut audit sample of 150 records found 0
false negatives. Core means full text was read: 0 of 23 core rows are abstract-only. The
twenty-third core source is AutoSurrogate, recovered from arXiv:2604.11945 after the
Elsevier page was unread [[doi:10.1016/j.aei.2026.105058]].

[Certain] On the 23 readable sources, demonstrated maturity is M1 = 10, M2 = 7, M3 = 5,
M4 = 1, M5 = 0. The single M4 is HERMES, whose extraction was released as the live
Treatise.geoLex database [[doi:10.48550/arxiv.2608.14055]]. The five M3 sources are
retrospective evaluations on named sites or sequences (Norne, Volve, Ridgecrest,
Santorini–Kolumbo, Qiaojia/Maduo, a Xiushan tunnel), not operator deployments.

[Certain] Three of ten core subfields have no full-text core source: geomechanics,
hydrogeology, inversion. Seismology has the most readable systems (8). Reservoir
engineering has the most admitted sources (68) and three of those in core. CCS has two
core sources, both using GEOS, one as a runtime simulator and one as a dataset generator.

[Certain] The modal techniques on the core tier are guardrails-validation, planning,
tool-calling, task-decomposition, retrieval and role-specialisation. Instrument-control
does not appear (`q001`–`q020`). Hierarchical multi-agent is the plurality architecture
(8 of 23), not the majority. MCP appears as a tool-exposure pattern in four otherwise
different architectures. Sixteen of 23 core sources are arXiv preprints; six of 23 do not
name the generator model; eight of 23 carry a code URL.

[Certain] No shared agent benchmark spans subfields. Named public artefacts that recur
inside one subfield (Norne, Volve, Ridgecrest, ESHM20, PUNQ-S3, Marvin, MineBench) are
each used by at most two core sources. Two core papers report no quantitative result.

[Certain] One hundred and thirty-two admitted sources cannot be maturity-rated because
only an abstract was available. That set is concentrated in industry venues. Two
abstracts describe named-site evaluations (Aquia Aquifer, Chagai Belt) that would be
shaped like M3 and are not counted. The core maturity distribution is the readable
slice, not the admitted literature.

[Likely] What exists, on this evidence, is a set of tool-calling and multi-agent
wrappers around existing simulators, catalogs, training loops and document pipelines,
evaluated mostly on synthetic cases, public benchmarks, or a single named retrospective
site, with one documented production knowledge-extraction run.
