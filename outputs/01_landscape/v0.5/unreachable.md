# Unreachable and partially reachable sources

What could not be read, and what that costs the report. A source listed here is still
admitted and still counted; the entry records how thin its evidence is so no reader mistakes
a title for a finding.

## Admitted with no abstract retrievable

Both records were admitted on their titles and venue metadata. The harvest returned no
abstract from any API, so their `papers.csv` rows carry metadata and `not stated` throughout.
A title is not evidence of an architecture, a base model or an evaluation, and neither record
contributes to any count in the report beyond the corpus total and its subfield tally.

| identity_key | title | authors | year | venue |
|---|---|---|---|---|
| `doi:10.13140/rg.2.2.28926.65602` | Autonomous Production Optimization in the Volve Field: A Multi-Agent Reinforcement Learning using Agentic AI | Sharma, S. | 2026 | ResearchGate deposit, no venue stated |
| `doi:10.2139/ssrn.5520018` | LLM-Powered Data Automation for 3D Geological Model Updating: Uncovering Architectural Divergence and the Efficiency-Effectiveness Paradox | Yuan, L.; Le Du, Y.; Wang, B.; et al. | 2025 | SSRN Electronic Journal |

Two notes on what is lost. The first title names the Volve field, which would make it a
candidate for `M3` had the evaluation been readable; it is recorded as `not stated` instead,
so the maturity distribution understates rather than guesses. The second appears to be a
preprint of, or close sibling to, the deep-read record
`doi:10.1038/s41598-026-61824-9` (*LLM-powered borehole data automation for 3D geological
modeling workflows*) — same task, same framing. It is retained as a separate record because
the identity keys differ and the relationship is unconfirmed, but the two should not be read
as independent corroboration of each other.

## Screened core, demoted to context for want of full text

Six records screened as core turned out to be unreadable. Each was tried against the
publisher DOI, Unpaywall, arXiv, and a title search for a preprint, repository or author
copy; where no full text existed the abstract came from OpenAlex or Semantic Scholar. All six
are demoted to `context` and their `maturity_demonstrated` is
`not stated (abstract only)` per the SCHEMA rubric.

| identity_key | venue | what was obtained |
|---|---|---|
| `doi:10.1190/tle44020142.1` | The Leading Edge (SEG) | abstract only; Unpaywall `is_oa false`, no OA location |
| `doi:10.1109/caibda65784.2025.11182767` | IEEE CAIBDA 2025 | abstract only; Unpaywall `is_oa false` |
| `doi:10.1016/j.watres.2026.125886` | Water Research | abstract only, via Semantic Scholar; absent from OpenAlex and Crossref |
| `doi:10.1016/j.oregeorev.2026.107477` | Ore Geology Reviews | abstract only — **but see below** |
| `doi:10.1016/j.autcon.2026.107055` | Automation in Construction | **partial abstract only**, truncated at both ends |
| `doi:10.56952/igs-2025-0391` | IGS 2025 (ARMA/OnePetro) | abstract only; Unpaywall `is_oa false` |

### An open-access paper that is not accessible

`doi:10.1016/j.oregeorev.2026.107477` is gold open access. Unpaywall reports `is_oa: true`
with a CC-BY-NC-ND licence and a publisher OA location. Every route to the text was
nonetheless refused: the DOI resolved to a Cloudflare interstitial, the ScienceDirect PDF
returned HTTP 403 with an anti-bot page, a text-extraction proxy received the "Are you a
robot?" captcha, and Scholar Archive held no copy. The licence permits redistribution; the
delivery does not permit retrieval.

This is worth separating from the paywalled cases. The other five are unreadable because
someone is charging for them, which is a commercial fact. This one is unreadable because of
bot protection on a nominally open article, which means **an OA flag in a bibliographic
database is not evidence that a text can be read.** Any count of "open access" in this
corpus, including in Section 05, should be understood as a licence status rather than an
access outcome.

### A truncated abstract

`doi:10.1016/j.autcon.2026.107055` has no abstract in OpenAlex, Crossref or Semantic
Scholar. The only text obtained was a partial abstract recovered indirectly through a search
engine's copy of the ScienceDirect page, truncated at both the opening and the closing
sentence. Its row is filled only where the surviving text supports it, and two of its six
`papers.md` quote slots are recorded as NOT FOUND. It is the thinnest evidence base of any
admitted record apart from the two with no abstract at all.

### What the demotion costs

Two of the six describe evaluations that would have been ratable had the text been readable.
Hydro-Agent reports an 18-dimensional inversion on the **Aquia Aquifer** reproducing
chromatographic separation along a 96 km flow path, and the Ore Geology Reviews workflow
reports quantified generalization on the **Chagai Belt** in Pakistan. Both name a real site
and both are retrospective, which is the shape of `M3`. Neither is counted as M3, because
the rubric rates the evaluation section and no evaluation section was available. The named
sites survive in `evaluation_method` and `reported_result` so Section 05 can cite them as
described work without counting them as demonstrated maturity.

## Second demotion pass: remaining original-core records

After the first six paywalled failures, 25 original-core records were still unread. Four
delegated readers stalled after a usage-limit switch. I took the remainder directly.

**Full text obtained (remain core):** Springer OA PDF
`doi:10.1007/s43503-026-00088-8` (26 pages) and ACL Anthology PDF
`doi:10.18653/v1/2025.findings-emnlp.1386` (19 pages).

**Nominal OA, delivery refused (demoted to context).** Nature HTML timed out and the
`_reference.pdf` URLs returned HTML interstitials (`s44304-026-00262-z`,
`s41598-026-61824-9`). MDPI PDFs returned HTTP 403 (`geosciences16050176`,
`mining6020026`). ESSOAr PDF returned 403. Elsevier gold-OA records were flagged `is_oa:
true` by Unpaywall with **no `url_for_pdf`**, the same delivery failure as the Chagai Belt
paper. Arizona DSpace served a JavaScript shell; the abstract was recovered from the REST
search API, not a thesis PDF.

**Closed venues (demoted).** EAGE EarthDoc three times, IEEE CAIT, ACM EQSIM Agent,
Automation in Construction 2025.106257.

**Software deposits, not manuscripts (demoted).** Zenodo `21768634` is the ESHM20-MCP
code companion to the npj paper. Zenodo `19078874` is GeoSAGE code and notebooks for
Hannah and Iowa case studies; the associated manuscript was not in the deposit listing
that I retrieved.

**No abstract in any API (demoted, metadata only):**
`doi:10.1016/j.sandf.2026.101789` and `doi:10.1016/j.autcon.2025.106257`.

The npj ESHM20 paper's abstract reports a 73-city, 5% median match against published
spectral accelerations. That is the shape of an M2 evaluation. It is not counted, because
the evaluation section was not read. Same for OntoGRC's named Taxkorgan–Yecheng report
(would be M3) and the PED paper's 100 unnamed field wells (M2 at most).

## Recovered in close-out

`doi:10.1016/j.aei.2026.105058` (AutoSurrogate) was demoted with the rest of the Elsevier
gold-OA set. The matching preprint `arXiv:2604.11945` was fetched as HTML and the record
was promoted to core. GAGAW (`doi:10.22541/essoar.176336946.65126612/v1`) ESSOAr PDF
still returned 403. AGeoKE (`doi:10.1016/j.acags.2026.100362`) still has no readable PDF
from ScienceDirect or the Idaho repository page.

## Second recovery pass: institutional access after publication

After this report's first draft, the corpus owner obtained PDFs for eleven paywalled or
unreadable records through personal institutional access and supplied them for reading.
None of these were fetched by a tool in this run — the PDFs were supplied directly — so
each was read in full before any papers.csv/papers.md/screening.csv edit, per rule 1.

**Promoted to `core`** (full text supported the SCHEMA `core` bar and the system is
genuinely agentic — an LLM decides something for itself, not merely prompt-in/text-out):

| identity_key | title | was | now |
|---|---|---|---|
| `doi:10.1016/j.watres.2026.125886` | Hydro-Agent (groundwater inverse modeling) | context, abstract-only | core, M3 |
| `doi:10.1016/j.oregeorev.2026.107411` | OntoGRC (mineral exploration extraction) | context, abstract-only | core, M3 |
| `doi:10.1016/j.autcon.2026.107055` | Tunnel geological-forecasting agent | context, truncated abstract | core, M3 |
| `doi:10.1016/s1876-3804(26)60734-3` | Well-log multi-agent framework (PE&D) | context, abstract-only, subfield `inversion` | core, M2, subfield `reservoir_engineering` |
| `doi:10.1016/j.petsci.2026.05.031` | LogACF (well-log AI agent) | context, abstract-only, subfield `inversion` | core, M2, subfield `reservoir_engineering` |
| `doi:10.56952/igs-2025-0391` | Geo-Resource Agent | context, abstract-only, subfield `geomechanics` | core, M1, subfield `reservoir_engineering` |
| `doi:10.2118/229435-ms` | InsightsAI (WITSML + DDR agentic AI) | context, abstract-only | core, M3 |

The three subfield corrections follow the SCHEMA rule to assign by where the evaluation is
set: the well-log papers evaluate reservoir/lithology parameters, not an inversion task
narrowly construed, and the Geo-Resource Agent's two case studies are reservoir
characterisation and decline-curve forecasting — its "Mechanical Earth Model" scope is
named in the title but never evaluated.

**Reclassified `out`** (full text showed no LLM or foundation model deciding anything —
the abstract alone had looked like a plausible core candidate, but the mechanism does not
clear the scope bar):

| identity_key | title | reason |
|---|---|---|
| `doi:10.1016/j.oregeorev.2026.107477` | LLM-assisted geological unit harmonization, Chagai Belt | `not-agentic` — the LLM performs one restricted, single-shot legend-text classification call; all spatial generalisation runs through a deterministic GIS pipeline the model never touches |
| `doi:10.2118/229716-ms` | AI agent for drill bit selection | `not-agentic` — the bit-selection system is MLP/Random Forest classification; the paper's only LLM use is a separate, non-agentic document-extraction/chatbot module |
| `doi:10.2139/ssrn.5520018` | LLM-Powered Data Automation for 3D Geological Model Updating | `not-agentic` — one-shot zero-/few-shot entity extraction and location parsing feeds a fixed downstream coordinate-geometry pipeline the model never calls or iterates on |
| `doi:10.13140/rg.2.2.28926.65602` | Autonomous Production Optimization in the Volve Field | `pre-llm-only` — pure multi-agent reinforcement learning (PPO + DQN); the paper's own future-work section states GPT/LLM integration has not yet happened |

These four are removed from `papers.csv` entirely (an `out` decision carries no papers.csv
row) rather than left in `context`, and their `screening.csv` rows now carry the matching
`cut_reason`.

The `doi:10.2139/ssrn.5520018` read also bears on the sibling-record question raised
above: the author list and task match `doi:10.1038/s41598-026-61824-9` closely enough to
be plausibly the same underlying study, but the SSRN preprint's own running header reads
"preprint submitted to Elsevier," not Nature/Springer — a minor inconsistency that keeps
the relationship unconfirmed rather than resolving it.

Net effect on the run: core rises from 23 to 30 sources; context falls from 132 to 121;
one paywalled record judged M3-shaped from its abstract (Chagai Belt) is no longer counted
anywhere, because full text showed it does not qualify at all. Report sections
00, 01, 02, 03, 04, 05 and 08 were regenerated from the updated `papers.csv`/`papers.md`;
none of the changes required a re-harvest, a re-triage, or a new run directory, since
`screening.csv`, `papers.csv` and `papers.md` are corrected in place, per precedent (see
"Recovered in close-out" above).

## Third recovery pass: a second institutional-access batch

The corpus owner supplied PDFs for eight further paywalled records — six flagged in the
second recovery pass above as still-stuck-abstract-only candidates, plus one journal
publication of a system already in this corpus as a preprint (GAGAW), plus one paper
whose only prior access attempt (IEEE Xplore, fetched by tool) had returned nothing
usable. All eight were read in full before any file edit, per rule 1.

**Promoted to `core`** — every one of the eight cleared the agentic bar this time; none
were reclassified `out`:

| identity_key | title | was | now |
|---|---|---|---|
| `doi:10.1016/j.sandf.2026.101789` | Landslide-reconstruction agent (witness-report RAG + geometry estimation) | context, no abstract in any API | core, M3 |
| `doi:10.1016/j.autcon.2025.106257` | multi-GeoLLM (self-review agents for footing design) | context, no abstract in any API | core, M1 |
| `doi:10.1016/j.cacaie.2026.100079` | Supervisor-ReAct-blackboard MAS (tunnelling geotechnical analysis) | context, abstract-only | core, M2, subfield secondary `geological_modelling` added |
| `doi:10.1016/j.aei.2026.105065` | Slope-reliability multi-agent framework | context, abstract-only | core, M1 |
| `doi:10.1016/j.acags.2026.100362` | AGeoKE (geoscience legacy document extraction) | context, abstract-only | core, M3, subfield secondary `mining` added |
| `doi:10.1016/j.bdes.2026.100042` | GAGAW journal record | context, abstract-only, subfield `inversion` | core, M3, subfield `hydrogeology` |
| `doi:10.1145/3731599.3767402` | EQSIM Agent | context, abstract-only | core, M2, architecture corrected `single-agent` to `multi-agent-hierarchical` |
| `doi:10.1190/tle44020142.1` | Seismic-processing assistant (Madagascar tool selection) | context, abstract-only | core, M1 |

`doi:10.1016/j.bdes.2026.100042` is the peer-reviewed journal publication of the same
GAGAW/AQUAH system already in this corpus as an ESSOAr preprint
(`doi:10.22541/essoar.176336946.65126612/v1`, still `context`/abstract-only — its own PDF
was never supplied). Kept as a separate `identity_key` per this review's rules; its
subfield is corrected from `inversion` to `hydrogeology` to match both its evaluation
focus (subsurface water content) and its sibling preprint record's existing subfield.

The `doi:10.1016/j.cacaie.2026.100079` maturity call is a closer tie-break than most: the
evaluation uses real contractor-supplied borehole data from a named-in-figure-only,
geo-located tunnelling project in Singapore, identified by dataset labels (C1/C2/C3) and
borehole IDs rather than a formal project name. Rated `M2` rather than `M3`, for
consistency with how this run treats other "real field data, unidentified" cases (e.g.
the well-log papers evaluated on "100 field wells").

Two ninth/tenth candidates from the running target list — IEEE CAIBDA
(`doi:10.1109/caibda65784.2025.11182767`) and IEEE CAIT/GALA
(`doi:10.1109/cait70489.2026.11553853`) — and the three remaining EAGE EarthDoc papers
(`doi:10.3997/2214-4609.202535040`, `.202639012`, `.2025640024`) were not resolved in this
pass: IEEE Xplore returns nothing to an unauthenticated fetch, and no PDF was supplied for
the EAGE records or for CAIT. They remain `context`/abstract-only.

Net effect on the run: core rises from 30 to 38 sources; context falls from 121 to 113;
total admitted (151) is unchanged, since every record in this pass was already admitted
and none were reclassified `out`. Report sections 00, 01, 02, 03, 04, 05 and 08 were
regenerated again from the updated `papers.csv`/`papers.md`, in place, for the same
reasons given after the second recovery pass.
