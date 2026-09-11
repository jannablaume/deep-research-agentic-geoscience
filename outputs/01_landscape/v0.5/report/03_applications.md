# 03 Applications

Source counts are admitted rows in `papers.csv` (core plus context).

## geomechanics

[Certain] No admitted sources remain in this subfield. The one record previously listed here,
Geo-Resource Agent [[doi:10.56952/igs-2025-0391]], was read in full after institutional access
resolved the paywall and reclassified to `reservoir_engineering`: its two evaluated tasks are
reservoir-characterisation log interpolation and decline-curve forecasting, and the paper never
evaluates a mechanical-earth-model task despite naming one in its title. See reservoir_engineering
below.

## seismology

[Certain] Twenty-seven admitted sources, of which ten are core. The core set covers
catalog construction and physical reasoning (TRACE on Ridgecrest and Santorini–Kolumbo
[[doi:10.48550/arxiv.2603.21152]]), FDSN waveform retrieval (TREMORS
[[doi:10.48550/arxiv.2609.01777]]), SPECFEM configuration (specfem-mcp
[[doi:10.48550/arxiv.2512.14429]]), OpenQuake hazard (ESHM20-MCP
[[doi:10.1038/s44304-026-00262-z]]), GraphRAG over named catalogs
[[doi:10.48550/arxiv.2607.24984]], reconstruction-operator search (SeisEvo
[[doi:10.48550/arxiv.2608.18272]]), fault-segmentation NAS
[[doi:10.48550/arxiv.2608.13889]], Fortran-to-Devito translation
[[arxiv:2601.18381]], interactive exploration of the named Simulated Ground Motion Database
(EQSIM Agent [[doi:10.1145/3731599.3767402]]), and embedding-based tool selection over the
Madagascar processing suite for full-waveform sonic data, evaluated only qualitatively on
unidentified confidential files [[doi:10.1190/tle44020142.1]].

## hydrogeology

[Certain] Five admitted sources, two core. Hydro-Agent's two cooperating agents (a Hydro-Coder
that writes and self-debugs MODFLOW/TOUGHREACT calibration code, and an Executor that runs it)
inversely calibrate groundwater flow and reactive-transport parameters, retrospectively against
real observed data from the named Aquia Aquifer, Maryland
[[doi:10.1016/j.watres.2026.125886]]. GAGAW's config-driven agent chain calls open-source
geophysical packages (pyGIMLi, SimPEG, ResIPy) and self-tunes inversions, evaluated on three
named US field sites — the No-Name Experimental Watershed, Mt. Snodgrass, and Dry Creek
Experimental Watershed [[doi:10.1016/j.bdes.2026.100042]]; this is the journal publication of
the same system already in the corpus as an abstract-only ESSOAr preprint
[[doi:10.22541/essoar.176336946.65126612/v1]], kept as a separate record. The remaining two
context sources, GWFlowAI [[doi:10.5194/egusphere-egu26-20010]] and RaKsh
[[doi:10.5281/zenodo.20342672]], are described in abstracts only.

## reservoir_engineering

[Certain] Seventy admitted sources, of which nine are core: PetroGraph history matching
on SPE1, SPE9 and Norne [[arxiv:2605.15028]], GeoMind lithology classification on four
public well-log benchmarks [[arxiv:2604.21501]], TADI question answering over Volve
[[doi:10.48550/arxiv.2605.00060]], InsightsAI correlating WITSML logs with daily drilling
reports over the named Volve field [[doi:10.2118/229435-ms]], the Geo-Resource Agent's two
qualitative reservoir-characterisation and decline-curve walkthroughs
[[doi:10.56952/igs-2025-0391]], a hierarchical multi-agent well-log interpretation framework
tested on 100 unnamed field wells [[doi:10.1016/s1876-3804(26)60734-3]], LogACF's
reservoir-parameter prediction on the public SPWLA benchmark plus one unnamed tight-sandstone
field case [[doi:10.1016/j.petsci.2026.05.031]], the Geowellex surface-logging agent, which
drove an MCP tool layer end to end to train a lithology classifier on one unnamed real well
and separately coordinated two A2A drilling-safety agents
[[doi:10.3997/2214-4609.202535040]], and a four-agent RAG workflow that revises
Random-Forest sedimentological genetic-element predictions for uncored wells against stored
geological principles, tested on unnamed datasets across several depositional environments
[[doi:10.3997/2214-4609.2025640024]]. The last two were read in full in a third
institutional-access pass; both are EAGE workshop extended abstracts. The remaining 61 are
context, largely SPE, IPTC and EAGE extended abstracts.

## geothermal

[Certain] Four admitted sources, one core: GAIA, evaluated on a homemade unpublished QA
set and a simplified synthetic inversion [[doi:10.48550/arxiv.2511.03852]].

## ccs

[Certain] Four admitted sources, two core. Agents4GEOS reproduces the PUNQ-S3 CO2
sequestration benchmark by calling GEOS [[arxiv:2607.18557]]. AutoSurrogate, recovered
from arXiv:2604.11945 after the Elsevier page was unread, trains pressure and saturation
surrogates on 1000 synthetic GEOS realisations of an unnamed 80×80×20 storage aquifer
[[doi:10.1016/j.aei.2026.105058]]. The remaining two are context (a life-cycle UQ
framework and the IEAGHG Agent George workshop note).

## mining

[Certain] Thirteen admitted sources, four core: Sim2Schedule on synthetic block models
[[doi:10.48550/arxiv.2606.10286]], MINDS on the Marvin copper benchmark
[[doi:10.3390/mining6020026]], STA-CoT on MineBench
[[doi:10.18653/v1/2025.findings-emnlp.1386]], and OntoGRC's generate-reflect-correct
extraction of ore-forming knowledge triples, evaluated against the named Xinjiang
Taxkorgan-Yecheng Fe-Pb-Zn assessment report [[doi:10.1016/j.oregeorev.2026.107411]]. A
second Ore Geology Reviews record on the Chagai Belt, Pakistan, read in full after
institutional access resolved its paywall, was found not to be agentic — its LLM performs
one restricted, single-shot legend-text classification call feeding an otherwise
deterministic GIS pipeline — and so is not admitted to this corpus at all.

## engineering_geology

[Certain] Nineteen admitted sources, nine core: GeoMCP on a JRC Eurocode 7 worked example
[[doi:10.48550/arxiv.2603.01022]], LandslideAgent on LandslideBench
[[doi:10.48550/arxiv.2606.18661]], the PPV Evaluator-Optimizer on a named Xiushan tunnel
[[doi:10.3390/geosciences16050176]], the foundation-design router on 27 homemade cases
[[doi:10.1007/s43503-026-00088-8]], a GraphRAG-based tunnel geological-forecasting agent
evaluated against post-excavation ground truth on five named tunnels in Yunnan Province
[[doi:10.1016/j.autcon.2026.107055]], a landslide-reconstruction agent evaluated
retrospectively on four named historical Hong Kong landslides
[[doi:10.1016/j.sandf.2026.101789]], multi-GeoLLM's self-reviewing footing-design pipeline
on 160 textbook-derived cases [[doi:10.1016/j.autcon.2025.106257]], a supervisor-ReAct
tunnelling MAS evaluated on real (geo-located but unnamed) borehole data from a Singapore
project [[doi:10.1016/j.cacaie.2026.100079]], and a slope-reliability multi-agent
framework with a self-correcting surrogate-training loop, evaluated on synthetic slope and
foundation cases [[doi:10.1016/j.aei.2026.105065]].

## inversion

[Certain] Two admitted sources, none core: a petrophysicist proof-of-concept
[[doi:10.2118/229346-ms]] and PyHydroGeophysX [[doi:10.5281/zenodo.21288456]] remain
context, described in abstracts only. Three records previously listed here — LogACF, a
human-in-the-loop well-log multi-agent framework, and the GAGAW journal record — were read
in full after institutional access resolved their paywalls; all three are genuinely
agentic and were reclassified to `reservoir_engineering` (the two well-log papers) or
`hydrogeology` (GAGAW), since their evaluation sections rate reservoir parameters,
reservoir/lithology classification, or hydrological water content rather than a
geophysical inversion task per se. See those sections above.

## geological_modelling

[Certain] Seven admitted sources, four core: HERMES extracting the Treatise on Invertebrate
Paleontology into Treatise.geoLex [[doi:10.48550/arxiv.2608.14055]], the borehole-report
coordinate pipeline [[doi:10.1038/s41598-026-61824-9]], and AGeoKE, an MCP multi-agent
extraction system evaluated retrospectively against two named real reference sources — the
USGS Mineral Deposit Models and the NASA Lunar Sample Compendium's individually-numbered
Apollo samples [[doi:10.1016/j.acags.2026.100362]] — read in full after institutional
access resolved its paywall, and a LangGraph question-answering pipeline over legacy
geological reports for the named Acacia Grove-1 well, in which a secondary classifier LLM
judges each answer and sends it back for regeneration
[[doi:10.3997/2214-4609.202639012]]. The eighth source formerly counted in this subfield,
the sedimentological-prediction workflow, was read in full in the same pass and
reclassified to `reservoir_engineering`, since its evaluation rates facies and reservoir
characterisation from wireline logs rather than a modelling task; see that section above.
A likely sibling of the borehole-report pipeline, an SSRN
preprint reporting the same borehole-to-coordinate task, was also read in full and found
not to be agentic — the LLM performs one-shot entity extraction and location parsing
feeding a fixed downstream geometry pipeline it never calls or iterates on — and so is not
admitted to this corpus.

[Certain] One of the ten core subfields has no full-text core source in this run:
inversion. It is not empty of admitted literature; it is empty of readable evaluation
sections. Geomechanics has no admitted source at all, once its one candidate was
reclassified to reservoir_engineering on full-text review.
