# coverage.md — test-mode coverage probe (primary deliverable)

This is a coverage probe, not a landscape map. Verdicts below are estimates from one query per
cell (plus a few incidental spillovers, marked as such) and must be read as rough indications,
never as measurements or as absence findings — no `[Absent-searched]` claim is made anywhere
in this run, per the test-mode rule.

## 1. Yield table — all 20 subfield x lineage cells

"Probed" = one of the 13 dedicated subfield x lineage queries (10 alternating + 3 thin-subfield
other-lineage). The 2 venue-direct queries (14, 15) are not one of the 20 dedicated cells but
sometimes returned material relevant to a cell not otherwise probed; that is noted as
"incidental" and is not a substitute for a dedicated probe.

| subfield | lineage | query_id | query text | n_results | n_on_topic_by_title |
|---|---|---|---|---|---|
| 1 rock mechanics/geomechanics | 1 llm | 1 | "LLM agent rock mechanics geomechanics geotechnical" | 8 | 5 |
| 1 rock mechanics/geomechanics | 2 pre-llm | — | unprobed | — | — |
| 2 seismology and induced seismicity | 1 llm | — | unprobed (incidental: query 1 and query 9 both surfaced "Seismology modeling agent," arXiv:2512.14429, an LLM-based agent) | — | — |
| 2 seismology and induced seismicity | 2 pre-llm | 2 | "autonomous seismic network induced seismicity monitoring reinforcement learning agent" | 6 | 2 |
| 3 hydrogeology and groundwater | 1 llm | 3 | "LLM agent groundwater hydrogeology model tool use" | 8 | 7 |
| 3 hydrogeology and groundwater | 2 pre-llm | — | unprobed (incidental: query 3 surfaced "Agent-based models of groundwater systems: A review," a pre-LLM ABM review, as spillover) | — | — |
| 4 reservoir engineering (petroleum) | 1 llm | — | unprobed (incidental: query 15, venue-direct OnePetro, surfaced 6 lineage-1 industry papers) | — | — |
| 4 reservoir engineering (petroleum) | 2 pre-llm | 4 | "closed-loop reservoir management reinforcement learning well placement optimization agent" | 8 | 8 |
| 5 geothermal | 1 llm | 5 | "LLM agent geothermal reservoir simulation autonomous" | 8 | 7 |
| 5 geothermal | 2 pre-llm | — | unprobed (incidental: query 10 surfaced one pre-LLM ABM paper on social acceptance of geothermal development, Tsuchiyu, Japan) | — | — |
| 6 CCS | 1 llm | — | unprobed (incidental: query 5 and 13 surfaced "AutoSurrogate," an LLM multi-agent framework whose case study is 3D geological carbon storage) | — | — |
| 6 CCS | 2 pre-llm | 6 | "agent-based model CO2 storage CCS injection monitoring" | 9 | 4 |
| 7 mining | 1 llm | 7 | "LLM agent mining autonomous operations copilot" | 7 | 0 |
| 7 mining | 2 pre-llm | 12 | "multi-agent system autonomous mining robotic survey planning" (thin-subfield probe, other lineage) | 6 | 3 |
| 8 engineering geology | 1 llm | 11 | "agentic AI LLM engineering geology site investigation geotechnical characterization" (thin-subfield probe, other lineage) | 10 | 8 |
| 8 engineering geology | 2 pre-llm | 8 | "expert system engineering geology multi-agent blackboard architecture" | 9 | 0 |
| 9 subsurface characterisation and geophysical inversion | 1 llm | 9 | "LLM agent geophysical inversion tool use planning" | 9 | 4 |
| 9 subsurface characterisation and geophysical inversion | 2 pre-llm | — | unprobed, and no incidental hits found anywhere in this run | — | — |
| 10 geological modelling | 1 llm | 13 | "LLM agent 3D geological modelling subsurface workflow" (thin-subfield probe, other lineage) | 8 | 7 |
| 10 geological modelling | 2 pre-llm | 10 | "agent-based model geological modelling simulation" | 7 | 7 |

Venue-direct probes (not part of the 20-cell grid):

| stage | query_id | query | n_results | n_on_topic_by_title | note |
|---|---|---|---|---|---|
| venue (arXiv) | 14 | "arxiv physics.geo-ph agentic agent LLM geoscience" | 7 | 3 | General web search, not a physics.geo-ph-restricted search; surfaced mostly general geospatial/GIS agent papers (out of scope) rather than physics.geo-ph-specific solid-earth ones. 1 of the 7 raw results was the arXiv listing page itself, not a candidate, and is excluded from the on-topic count. |
| venue (OnePetro) | 15 | "onepetro agentic AI LLM agent reservoir SPE technical paper" | 7 | 7 | All on-topic, all reservoir engineering, all 2025 SPE conferences, all lineage 1. Strongest single yield of the whole probe. Full-text access to OnePetro was not tested (no fetch attempted). |

## 2. Projection (rough, from one query per cell — not a measurement)

- **1 rock mechanics/geomechanics**: lineage 1 dense (5 distinct on-topic items from one
  query). Floor of 3 admits looks easily reachable. Lineage 2 completely unprobed with no
  incidental signal — full run needs a dedicated lineage-2 seed (e.g. pre-LLM expert systems
  for rock classification, RL-controlled tunnel support).
- **2 seismology and induced seismicity**: lineage 2 returned mostly non-agentic ML papers
  (phase picking, forecasting) rather than agent-framed work; only 2 of 6 results were
  agent-framed. Combined with 1 incidental lineage-1 hit, roughly 3 agentic candidates are
  visible across both lineages so far — floor is plausibly reachable but will need more
  phrasings than most subfields, and the field may simply have less agent-framed work relative
  to its ML literature.
- **3 hydrogeology and groundwater**: dense in both lineages (7 on-topic in lineage 1, plus an
  incidental pre-LLM ABM review). Floor easily reachable; this cell also produced 1 of the 3
  mechanics-slice admits (AQUAH).
- **4 reservoir engineering (petroleum)**: the densest subfield observed — 8 of 8 on-topic in
  the dedicated lineage-2 query (heavy cross-mirror duplication of 2-3 underlying systems, not
  8 distinct systems) plus 6 distinct on-topic industry papers from the OnePetro venue probe.
  Floor easily reachable; flag for the 20% cap in `full` mode, since this subfield could
  otherwise absorb a disproportionate share of admits.
- **5 geothermal**: lineage 1 dense (7 of 8 on-topic, including 2 mechanics-slice-quality
  candidates: GAIA Agent, Agents4GEOS). Lineage 2 thin (1 incidental item). Floor reachable,
  likely lineage-1-heavy.
- **6 CCS**: lineage 2 moderate (4 of 9 on-topic, including the CO2 Markov-game admit and a
  distinct closed-loop RL paper found during count reconciliation, arXiv:2605.02405). Lineage 1
  thin (1 incidental item, AutoSurrogate). Floor reachable via lineage 2; lineage 1 needs a
  dedicated seed.
- **7 mining**: the clearest lineage split in the whole probe. Lineage 1 returned **zero**
  on-topic results out of 7 (all generic-domain LLM copilots: code, agriculture, GIS, wireless,
  bench science — none about mineral extraction). Lineage 2 returned 3 on-topic results out of
  6 (underground multi-robot systems, autonomous inspection robots). Floor reachable only via
  lineage 2 unless lineage-1 seed terms are substantially reworked away from generic
  "agent"/"copilot" phrasing.
- **8 engineering geology**: the mirror image of mining. Lineage 2 (generic "blackboard
  architecture"/"expert system" terms) returned **zero** on-topic results out of 9 — every hit
  was a general AI-architecture paper with no stated geoscience application. Lineage 1 was the
  densest cell of the entire thin-subfield probe (8 of 10 on-topic), including a
  landslide-reconstruction paper in two venues. Floor easily reachable via lineage 1; lineage 2
  needs domain-specific pre-LLM vocabulary (e.g. "expert system slope stability," "knowledge-based
  system site characterization") rather than the generic architecture terms used here.
- **9 subsurface characterisation and geophysical inversion**: the single highest-risk cell.
  Lineage 1 is moderate (4 of 9 on-topic, including the GeoMind admit). Lineage 2 was neither
  probed nor found incidentally anywhere in this 15-query run — a true, currently-unexplained
  gap. This is the one cell where the `full` run cannot yet estimate whether the 3-admit floor
  is reachable at all; "geophysical inversion" as a search term may be dominated by classical
  algorithmic literature that this probe's pre-LLM vocabulary (multi-agent system, RL control,
  autonomous sampling) does not match, and the vocabulary itself likely needs rethinking before
  the full run, not just more calls with the same terms.
- **10 geological modelling**: dense in both lineages (7 of 7 on-topic in lineage 2, including
  a peer-reviewed Geoscientific Model Development paper; 7 of 8 on-topic in lineage 1, though
  most were duplicates of items already seen in other subfields' queries, with 1 new solid
  candidate, a voxel-based underground digital twin paper). Floor easily reachable, likely
  lineage-2-heavy.

**Arithmetic check on the 250-call full-mode budget**: this probe returned 92 unique screened
items from 15 search calls (raw hits per call ranged 6-10; unique-after-dedup average was
about 6.1/call, lower than the 10-20/call the seed budget in the prompt assumes, because of
heavy cross-query duplication of the same handful of systems and because several query
families drifted into out-of-scope territory - see queries 7, 8, 9, 14 above, where 0-4 of 6-9
hits were on-topic). At roughly this rate, 120 seed calls would be expected to yield in the
range of 400-700 unique screened items depending on how much the `full` run's broader query
diversity (5+ phrasings x 23 families, per the Stopping criterion) offsets the duplication seen
here. The ≥600 screened-unique target looks achievable but not comfortably so, and is sensitive
to fixing the domain-drift problem identified above before spending the full budget on the
same phrasings.

## 3. Go/no-go verdict

**Artifact chain (mechanics slice):** worked end to end, with one qualified gap. All required
`test`-mode files were written (see Constraints checklist in `RUN.md`). `papers.csv` parses as
RFC 4180 with 3 data rows and 27 columns (verified programmatically). All 3 admitted sources
were independently verified to exist and to match their stated title/authors against fetched
content, not from recall. `papers.md` carries verbatim extracts keyed to the same 3
`source_id`s. `pdfs/` is non-empty (2 of 3 candidates' PDFs saved).

The qualified gap: full-text extraction via `WebFetch` on raw arXiv PDF URLs was unreliable —
it failed outright on one candidate (AQUAH, exceeded a 10MB content-length limit) and returned
only title/section-headings/partial content on a second (the CO2 Markov-game paper), while
succeeding cleanly on GeoMind. Switching to arXiv's HTML rendering (`arxiv.org/html/<id>`
instead of `arxiv.org/pdf/<id>`) fixed extraction for AQUAH and would very likely have fixed it
for the CO2 paper too, but the 20-call hard cap was reached before that retry could be spent.
**This is the single most actionable mechanics finding of this run**: a `full`-mode run that
budgets exactly one fetch call per admitted source for full-text reading will hit this same
failure mode repeatedly; budget for an HTML-rendering fallback, or fetch the HTML route first
by default, and treat "PDF download to `pdfs/`" as a separate, additional call from "full-text
read," since the two returned different content in this run (the HTML fetch that fixed reading
did not itself yield a locally-savable PDF binary; only the raw PDF fetch did that, even when
its own text extraction failed).

**Cells too thin for the quota, and what to change before `full`:**
1. Subfield 9 (subsurface characterisation and geophysical inversion) x lineage 2 — no signal
   at all, dedicated or incidental. Needs new pre-LLM seed vocabulary specific to inversion
   (e.g. adaptive/evolutionary-algorithm inversion, self-organizing sampling for inversion)
   before the `full` run, not just a repeat of the multi-agent/RL/autonomous-sampling terms
   used here.
2. Subfield 8 (engineering geology) x lineage 2 — zero on-topic despite 9 raw hits, because
   "blackboard architecture"/"expert system" alone returns generic AI-architecture papers with
   no geoscience application. Needs domain-qualified phrasing.
3. Subfield 7 (mining) x lineage 1 — zero on-topic despite 7 raw hits, all generic-domain LLM
   copilots. Needs domain-qualified phrasing (e.g. "LLM agent" + "mineral exploration" /
   "mine planning" / "ore body," not bare "mining").
4. Query families anchored on bare "agent"/"agentic"/"copilot" without a strong domain
   qualifier (queries 7, 9, 14) reliably drift into GIS, aerospace, agriculture, and
   telecommunications false positives. The `full` run's seed phrasings should pair every
   lineage-1 term with an explicit solid-earth/subsurface noun, not rely on the subfield term
   alone to narrow the query.

**Is the 250-call cap sufficient?** Provisionally yes for the seed/screening budget (see
arithmetic above), but the PDF/full-text fetch bucket (40 calls in `full` mode) looks
under-budgeted at 1 call/source given the extraction failures observed here; recommend
planning for roughly 1.5 fetch calls per admitted source in that bucket, or reallocating a few
calls from the 30-call verification reserve.

**Overall: GO**, conditional on the three seed-vocabulary fixes above and the fetch-budget
adjustment being made in prompt v0.5 (or applied ad hoc at the start of the `full` run) before
spending the 120-call seed budget.
