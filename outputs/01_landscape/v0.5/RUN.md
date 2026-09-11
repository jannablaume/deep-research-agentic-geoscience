outputs/01_landscape/v0.5

## Run log

- date: 2026-09-07
- prompt: `.claude/skills/01_landscape_neutral/SKILL.md` v0.5
- purpose: full landscape run
- model: Claude Opus 5

## Step 0 — Smoke test

Two smoke runs, because the first one failed on infrastructure rather than mechanics.

- `outputs/01_landscape/v0.5-test`: `harvest.py --smoke` returned `error RuntimeError:
  HTTP 429` on 2 of 3 OpenAlex queries. Cause: OpenAlex has moved to a metered API. The
  free allowance is a daily USD budget — $0.10/day keyless, $1/day with a free key — and
  this machine's keyless allowance was already spent (`{"error":"Rate limit exceeded",
  "message":"Insufficient budget… Resets at midnight UTC","retryAfter":51180}`). arXiv and
  Crossref were unaffected; Semantic Scholar returned 429 without a key, as documented.
- A free OpenAlex API key was obtained and passed via `OPENALEX_API_KEY` (shell
  environment only; never written to a tracked file). Budget after the key: $1.00/day,
  against a harvest that costs ~$0.15 in `search` calls.
- `outputs/01_landscape/v0.5-test2`: re-smoke with the key. 3 queries, 6 API calls, all
  `ok`, 1757 unique records, 84% with abstract, shortlist 208 (core 93, periphery 115).
  Periphery counting exercised. Mechanics confirmed.

### Script changes made during the smoke test

- `harvest.py`: sends `OPENALEX_API_KEY` as a bearer token when set.
- `harvest.py`: HTTP 429 is now two distinct failures. A per-second throttle is retried;
  an exhausted daily budget raises `BudgetExhausted`, checkpoints, and aborts the run with
  a message. Retrying a spent budget turns one loud failure into a quiet half-corpus that
  every downstream count would have trusted.
- `harvest.py`: `queries.csv` gains `n_available`, the API's own result count, so a paging
  cap is visible in the artifact rather than only in stderr.
- `reference/queries.json`: `openalex_max_pages` 5 → 20, `arxiv_max_results` 200 → 1000.

## Step 1 — Harvest

- Command: `python3 scripts/harvest.py --out outputs/01_landscape/v0.5 --no-s2`
- Result: **11,177 unique records**, 9,531 with abstract (85%), 60 API calls, all
  `status: ok`. No `zero` queries, no errors.
- Semantic Scholar skipped (`--no-s2`): 429 without a key, as the script documents.
- Three full harvests were run. The first, at the shipped caps
  (`openalex_max_pages: 5`, `arxiv_max_results: 200`), returned 9,098 records but hit the
  paging cap on four queries — `earth_observation` B_llm reported 3,515 available and
  returned 1,000; `climate_atmosphere` B_llm 2,144 → 1,000; `geoscience_general` B_llm
  1,057 → 1,000; `ccs` B_llm on arXiv 230 → 200. Three of those four are periphery, and
  section 07 reports periphery size from harvest counts, so the caps would have been
  reported as the size of the neighbouring literature. Caps raised, re-harvested: 11,177
  records, no query truncated.
- The second re-harvest corrected a false truncation flag: arXiv reports every match but
  the harvester drops records before `from_date`, so `got < total` is routine there and
  lost nothing. The flag now fires only when the cap was actually reached.
- OpenAlex spend across all three harvests plus both smokes: **$0.393 of the $1.00 daily
  free budget**.

## Step 2 — Triage

- Command: `python3 scripts/triage.py --out outputs/01_landscape/v0.5 --min-score 3`
- Shortlist **606 of 11,177** (5%): core 296, periphery 310. Below cut 10,571.
- Threshold kept at `--min-score 3 --min-strong 1`. 606 is inside the 150–800 band, so no
  adjustment was called for. Note from `triage_stats.md` that the shortlist is flat at 606
  across min-score 1, 2 and 3 — at this end `min-strong` is the binding cut, not the
  score, so lowering `--min-score` alone would have admitted nothing.
- Records with no abstract: 1,646 of 11,177 (14%). Screened on title alone.
- Core group counts, shortlisted: seismology 91, reservoir_engineering 72, ccs 52,
  engineering_geology 29, mining 17, geological_modelling 15, hydrogeology 11,
  geothermal 4, geomechanics 3, inversion 2.

## Step 3 — Screening

Screened in this session, in batches, verified against `screening.csv` after each batch.

### Shortlist (606 records)

- **In 126** (core 36, context 90), **out 480**.
- Cuts: periphery 197, not-geoscience 157, not-a-source 72, not-agentic 39, duplicate 10,
  pre-llm-only 4, no-abstract-untriageable 1.
- Admitted by subfield (sources, not systems): reservoir_engineering 57, seismology 25,
  engineering_geology 16, mining 10, geological_modelling 7, inversion 4, geothermal 2,
  hydrogeology 2, ccs 2, geomechanics 1.
- `not-a-source` is large because the shortlist carries conference front matter, editors'
  notes, session announcements, textbook chapters, data deposits and review-comment
  threads that the APIs index as works.
- Provisional tiering rule, applied where the abstract alone could not settle it: default
  to `context` unless the source is open access or the abstract is definitive about the
  system's decision loop. Records deep-read in step 4 can move either way; ones whose full
  text cannot be reached stay `context`.

### Audit sample, first pass (150 records, pre-refix cut)

- **1 false negative: 0.7%**, well under the ~5% threshold that would require diagnosis.
- The false negative is `doi:10.3390/pr13051413`, a review of artificial general
  intelligence, LLMs included, in oil and gas reservoir development. Admitted as
  `context`, `reservoir_engineering`. It is the same class of source as the AGI geoenergy
  review admitted from the shortlist, so the inconsistency was mine and not the ranking's:
  triage gave it `agentic_score 2, strong_hits 0`, which is the correct score for an
  abstract that names no agent vocabulary.
- The remaining 149 were out: periphery 61, not-geoscience 44, not-agentic 26,
  not-a-source 18. Nothing in the sample was an LLM-based agentic system in a core
  subfield, which is the class the ranking exists to find.
- At the time, no change was made to `--min-score` or to `triage.py`. That decision was
  reversed: see "Two defects in triage.py" below. At 0.7% the cut looked sound, and
  re-triaging would invalidate the 606 screening decisions
  above against a `shortlist.md` no longer on disk.
- Two near-misses worth recording, both correctly out: `doi:10.5281/zenodo.21300935`, a
  supporting-data deposit for vision-AI and LLM extraction of public geological well-log
  records — the deposit is not a source and extraction is not a decision loop; and
  `doi:10.1051/itmconf/20268404017`, a centipede rescue robot driven by an LLM through
  LangGraph — genuinely agentic, but disaster robotics rather than geoscience.

## Two defects in triage.py, found mid-run and fixed

The grey-literature pass is what exposed them. Its first four searches surfaced
`Open-DARTS-MCP`, `TADI`, `TREMORS` and a SPECFEM MCP agent; three were already screened
in, but the SPECFEM one, `doi:10.48550/arxiv.2512.14429`, was sitting in `screened.csv`
below the cut and had not been drawn into the audit sample. A record that a single web
search finds first, and that the ranking scored 2 with `strong_hits` 0, is not a
sampling accident. Grepping the below-cut corpus for agent vocabulary confirmed two
independent defects.

**Defect 1 — a whole class of records dropped regardless of score.** `above()` in
`triage.py` requires `scope_computed != "none"`, and `scope_computed` is only set when the
text matches a specific subfield in `DOMAIN` or a periphery domain in `PERIPHERY`. A record
that says "geoscience" or "Earth science" without naming a subfield matched neither and
was discarded no matter how well it scored. **190 records cleared score, strong-hits and
LLM-presence and were dropped this way**, including a multi-agent geoscience
document-extraction system at score 12 (`doi:10.1016/j.acags.2026.100362`), a subsurface
hydrology agent workflow at 16 (`doi:10.22541/essoar.176336946.65126612/v1`), and the SPE
and EAGE multi-agent subsurface papers. This also explains the flat shortlist across
`min-score` 1–3 that Step 2 above attributed to `min-strong`: the binding filter was
structural, and neither knob would have moved it.

Fix: a `GENERAL` pattern checked only after `DOMAIN` and `PERIPHERY` both fail, assigning
`scope core`, `group geoscience_general`. Shortlisting is not admission, so the right
place for these is in front of the screener.

**Defect 2 — no Model Context Protocol vocabulary at all.** MCP is the most common way the
2025–26 systems in this corpus expose tools to an LLM, and none of `model context
protocol`, `MCP server` or the `*-mcp` tool-name form appeared in any pattern list. The
compound patterns also required fixed adjacency, so the standard title shape in this
literature did not match: `PetroAgents: A Multi-Agent, Multi-Modal Large-Language-Model
Framework` scored 1 with zero strong hits, because `Multi-Agent` was followed by a comma
and `Large-Language-Model` was hyphenated.

Fix, all in `scripts/triage.py`: MCP and A2A terms added to `AGENT_LLM`, with bare `MCP`
excluded because it collides with monocyte chemoattractant protein; the `multi-agent` head
in `AGENT_GENERIC` now tolerates a comma and up to two intervening modifiers; a pattern
added for agents named after their job ("modelling agent", "smart agents"); `AGENT_COMPOUND`
and `MEDIUM` made hyphen-tolerant for `large-language-model` and allowed `agent` as a tail.

**Effect, at the same `--min-score 3 --min-strong 1`:**

| | pre-refix | refixed |
|---|---|---|
| Shortlist | 606 | 712 |
| — core | 296 | 381 |
| — periphery | 310 | 331 |
| Admitted | 126 | 155 |
| — core tier | 36 | **54** |
| — context tier | 90 | 101 |

Purely additive: all 607 prior decisions carried forward on `identity_key`, none of the
previously shortlisted records fell below the refixed cut, and 105 new records were
screened. Core tier moved from 36, which is under the 25–80 expectation floor the skill
asks to be explained, to 54, which is inside it. `triage.py` was re-run with `--force`;
`shortlist.md`, `audit_sample.md`, `triage_stats.md` and `screening.csv` from the previous
cut are preserved under `pre-refix/`.

### Screening, refixed cut (712 records)

- **In 155** (core 54, context 101), **out 557**.
- Cuts: periphery 222, not-geoscience 188, not-a-source 81, not-agentic 50, duplicate 11,
  pre-llm-only 4, no-abstract-untriageable 1.
- Admitted by subfield (sources, not systems): reservoir_engineering 60, seismology 26,
  geological_modelling 23, engineering_geology 17, mining 13, hydrogeology 6, inversion 5,
  geothermal 2, ccs 2, geomechanics 1. `geological_modelling` absorbed most of the newly
  admitted records, because the systems the scope bug had been hiding are predominantly
  knowledge-extraction and document-processing agents over geoscience literature.

### Audit sample, second pass (150 fresh records, refixed cut)

- **0 false negatives: 0.0%.** The sample re-draws from the 10,465 now below the cut, and
  has no overlap with the pre-refix sample, so this is an independent measurement.
- Three near-misses, all checked against their full abstracts and all correctly out:
  `doi:10.1016/j.geoai.2025.100010` generates geological cross-sections by in-context
  learning with augmented prompting, which is prompt-in/text-out; `doi:10.3997/2214-4609.202539065`
  extracts structure from scanned geotechnical documents with GPT but defines no decision
  loop; and `doi:10.1016/j.gexplo.2026.108205`, GoldMiner-AI, which had no harvested
  abstract — the companion Earth Science Frontiers paper retrieved in this run shows its
  LLM does RAG-based Q&A while anomaly identification runs on separate deep-learning
  models, so the LLM chooses nothing.
- The 150 were cut as: periphery 60, not-geoscience 63, not-agentic 15, not-a-source 12.
- The 149 pre-refix audit rows that are neither shortlisted nor in the current sample are
  retained in `screening.csv` with `from_audit_sample` cleared and a note, so the earlier
  measurement stays traceable without contaminating the current one.

**What this says about the audit sample as an instrument.** Both measurements were honest
and the first one was misleading. A 150-record random draw from ~10,500 mostly irrelevant
records is well suited to catching a cut that is slightly too tight across the board, and
badly suited to catching a defect concentrated in one vocabulary or one branch of a scope
rule — the pre-refix sample contained none of the 190 dropped records. The grey-literature
pass found in four searches what the sample missed in 150 records. For v0.6: draw part of
the audit sample from the highest-scoring below-cut records rather than uniformly, which
is where a structural filter leaves its fingerprints.

## Step 3b — Grey literature

Eleven of the 40 permitted web calls used: ten searches and one fetch, logged in
`queries.csv` as `w1`–`w11`. Ten returned usable records; the eleventh, a direct fetch of
`doi:10.1016/j.gexplo.2026.108205`, failed with HTTP 406 from the publisher and was worked
around with a search.

**17 records added**, 14 of them new to `screened.csv` and appended there first:

- **Conference grey**: the Stanford Geothermal Workshop 2026 version of GAIA. The system
  itself was already in the corpus as an arXiv preprint, so this is a second source on one
  `system_id` rather than a new system.
- **Regulatory / programme grey**: the IEAGHG 2025-TR04 workshop report, which is the only
  reachable record of Agent George running over the OSDU platform for CCUS supply-chain
  data.
- **Nine code releases with no write-up**, which is the category the APIs cannot see at
  all: `seismo-mcp`, `petro-mcp`, `petromcp`, `AgentNexus`, `geotechcli`,
  `GeotechStaffEngineer`, `drilling-npt-agent`, `volve-drilling-advisor` and
  `pyResToolbox-MCP`. All are `context`: a repository README states what the agent can call
  but almost never how it was evaluated.
- **Two SPE trade-press articles**: the ONGC large-scale well-modelling case study, and a
  TWA practitioner account of architecture choices in automating well-log interpretation.
  Both are `abstract-only` in effect and both are unusually explicit about design
  trade-offs, which makes them useful to section 02 even at `context`.
- **Three corpus records the grey pass surfaced from below the cut**:
  `doi:10.48550/arxiv.2608.22068` on LLM decision support for geothermal well arrays,
  admitted `context`; an earlier version of it, cut `duplicate`; and the AskGDR preprint,
  cut `not-agentic` because it answers from curated metadata by retrieval and its own
  documentation states it is not a conversational agent.

**What the grey pass could not reach.** OnePetro and EarthDoc full texts are paywalled and
were not attempted beyond the abstract, as the skill directs. SPE's own `EnRG-LLM`, an
energy-domain model fine-tuned on the OnePetro corpus and an OTC Spotlight award winner,
is documented only in a webinar listing and vendor copy; there is no technical description
to screen, so it is recorded here and not admitted. AGAPEX is admitted on trade-press
copy alone, with a note on the row that the description is the vendor's own — no primary
publication was reachable. Hugging Face returned nothing in scope that was not already
covered by the GitHub releases above.

**Snowballing.** Deferred to step 4, where the full texts are in front of me.

### Admitted set after screening and grey

- **155 sources: 47 core, 108 context.**
- By subfield: reservoir_engineering 69, seismology 27, engineering_geology 19, mining 14,
  geological_modelling 9, inversion 5, geothermal 4, hydrogeology 4, ccs 3, geomechanics 1.
- Five of the ten core subfields came in thin — inversion 5, geothermal 4, hydrogeology 4,
  ccs 3, geomechanics 1 — and geomechanics is a single source. Section 03 reports each of
  those as its own count rather than pooling them.

### A judgment call worth recording: `geoscience_general`

`SCHEMA.md` lists `geoscience_general` among the **periphery** subfields, "counted and
characterised but never deep-read", while the skill's scope section names only Earth
observation, climate and atmosphere, ocean and planetary as periphery. My triage fix labels
the new fallback group `geoscience_general` with `scope core`, which is right for
shortlisting — it puts the record in front of a screener — but wrong as an admission.

Resolved as follows, applied uniformly and recorded here because the two reference documents
differ in emphasis: **a source is admitted to a core subfield when the system's output is an
artefact in one of the ten** — a geological model, map, stratigraphic or lithological
interpretation, an inversion result, a simulation, a drilling or reservoir decision, or a
structured knowledge base built from geological source material. **A source whose output is
generic research assistance** — literature search, data discovery, code generation, question
answering over mixed Earth-science content — **is `geoscience_general`, hence periphery, hence
cut.** 16 records moved to periphery under this rule after first being admitted, including
`Streamlining geoscience data analysis with an LLM-driven workflow`, `Accelerating earth
science discovery via multi-agent LLM systems`, the Intelligent National Map vision paper,
and the SPE natural-language geoscience search system. AGeoKE and HERMES stayed admitted,
because both build structured geological knowledge bases from geological source material.

Two hydrological platforms, HydroCraft and AI-Hydro, moved the same way: `hydrogeology` in
the core list is groundwater, aquifers and contaminant transport, and both systems are
surface-water modelling. That is what leaves hydrogeology at 4 sources.

## Step 4 — deep-read

155 sources are admitted: 47 core, 108 context. `papers.csv` needs a row for every one of
them, because `audit.py` checks the admitted set against `screening.csv` in both directions;
`papers.md` needs an extract block for the 47 core only.

Reading was delegated to subagents in eight batches and the rows are written here, following
the skill's rule that if you delegate, you delegate the reading and the parent writes. Each
batch was asked for the `papers.csv` field values plus six verbatim quotes per source — what
was built, what the agent can call, how it was evaluated, the headline number, the strongest
maturity claim, and an acknowledged limitation — with an explicit instruction that "not
stated" is the correct answer for a silent paper and that a failure to retrieve must be
reported as a failure rather than reconstructed. The 108 context rows were extracted from
the abstracts already stored in `screened.csv`, so that batch needed no network at all.

Batches: three over the 16 arXiv core records, two over the 13 core records expected to be
open access, three over the 18 core records expected to be paywalled.

### A tier constraint discovered while reading `audit.py`

`audit.py` fails the run if more than a fifth of the core tier is `abstract-only`
(`len(core) // 5`, so at most 9 of 47). That check encodes something the schema leaves
implicit: **core tier means deep-read, not merely important.** 18 of the 47 core records are
behind Elsevier, IEEE, ACM, SEG or EAGE paywalls, so on current access the core tier cannot
satisfy it.

This is the point at which the provisional tiering rule adopted during screening — default a
paywalled source to `context`, revisit once access is known — comes due. Any core record
that comes back abstract-only after the fallback routes (publisher, preprint search,
bibliographic API) is demoted to `context`, and the demotion is recorded per record rather
than applied silently. Core tier then reports what was actually read. The cost is visible in
Section 05: the maturity distribution for the paywalled literature rests on abstracts, which
systematically favour the authors' framing, and that limitation belongs in the report rather
than in a footnote here.

### The maturity rubric overrides the abstract-level ratings

`SCHEMA.md` ends the maturity rubric with a rule I had not carried into the delegation
brief: **`access_status: abstract-only` forces `maturity_demonstrated: not stated (abstract
only)`**, and `audit.py` accepts that string as a valid rubric value alongside `M0`–`M5`.

So the four context batches were asked the wrong question. They were told to rate what the
abstract evidenced, and they did it carefully — the batch-4 reader returned M0 = 4, M1 = 14,
M2 = 3, M3 = 2, M4 = 4 and flagged its own weakest calls unprompted, including an M4 that
rests on a vendor deployment claim with no site named and an M1 bulge that is really
"working implementation, no evaluation reported at all", a state the rubric has no level for.
Those flags are the argument for the rule rather than against it: an abstract is the authors'
framing of their own evaluation, and rating from it would have put 108 unfounded levels into
the distribution Section 05 reports.

The override is applied in the merge rather than by re-running the batches, which would cost
four more passes to reach a value the schema already fixes. The delegated M-levels are
discarded, not recorded, because keeping them would invite exactly the aggregation the rule
forbids.

**Consequence for the report:** the maturity distribution can only be computed over the
full-text records. Section 05 reports it that way, states the denominator, and does not
silently treat 155 sources as rated. This is a real limitation of the run and not a
presentational choice — and since 18 of the 47 core records are paywalled, the readable
denominator is smaller than the admitted set by a wide margin.

Two admitted context records have no abstract text at all in `screened.csv`. They are listed
in `unreachable.md`; their rows carry metadata and `not stated` throughout, since a title is
not evidence of an architecture.

### Verifying the 108 context rows

All four batches returned 27 rows with keys in input order, no illegal values in
`architecture`, `held_out`, `data_type` or `agentic_techniques`, and the merge joined
108 of 108 against `screening.csv` with nothing missing and nothing extra.

Rather than spot-check, I checked the two fields most exposed to fabrication against the
stored abstract text for every row:

- **`reported_result`: 29 rows report a number, and every numeral in all 29 appears verbatim
  in the source abstract.** No invented results.
- **`base_model`: 11 of 108 abstracts name a model at all.** Five rows tripped the checker
  and all five are honest — the flagged strings were parenthetical hedges the readers added,
  such as `OpenAI GPT (version not stated)` and `GPT; LLaMA; Gemini (user-selectable)`; the
  model names themselves are present in the abstracts. The hedges are kept, because they
  carry more than a bare family name does.

That 11-of-108 figure is itself a result for Section 04: the base model, which decides
whether any of this is reproducible, is absent from nine abstracts in ten.

### A tie-break I left out of the delegation brief

Three readers independently reported the same hard case — a system evaluated on real
proprietary field data with no named site or operator, which fits neither `M1` (synthetic or
textbook-scale) nor `M3` (named site). Batches 2 and 3 each invented a ceiling of `M2` for
it and applied it consistently, listing the affected records.

Their improvised rule is exactly the rule in `SCHEMA.md`: *"M3 requires the site to be
named. 'Real field data', unidentified, is M2 at most"*, alongside *"Data source not stated:
M1 at most"*. I had condensed the rubric for the brief and dropped both lines. The
convergence is reassuring rather than alarming — but it is my error, and it has a live
consequence: **the eight core-tier readers got the same condensed rubric.** Their returned
`maturity_demonstrated` values are therefore advisory. As the writer I re-derive the level
for each core row from the evaluation evidence and quotes they return, applying both omitted
tie-breaks, instead of transcribing their level.

This matters most for the industry venues. SPE, IPTC and EAGE papers routinely evaluate on
"a major North American operator" or "Field A", and several assert deployment while naming
no site — `233425-ms` claims a portfolio of over 1,000 wells and a 75% time reduction with
no operator named. Under the tie-breaks those cap at M2 however operational they sound, and
the anonymity of the industry corpus is a finding about the literature that belongs in
Section 05.

### M2 versus M3: public dataset or named site?

Batch B forced this one. PetroGraph history-matches the **Norne** field and TADI answers
questions over **Volve** wells 15/9-F-11 T2 and 15/9-F-1 C. Both datasets are simultaneously
a public download and real production history from a named North Sea field, and the two
readings give different levels. The context batches had split on the same question, scoring
Volve and the F3 block as M2 on the open-dataset reading.

`SCHEMA.md` settles it on the word **site-agnostic**: M2 is "a reusable, *site-agnostic*
benchmark — which may contain real data", and the tie-break contrasts "a phase picker on
STEAD" (M2) with "the same picker on one named network's catalogue" (M3). Public
availability is not the discriminator; whether the evaluation is tied to an identifiable
piece of ground is. Norne and Volve are one named field each, so they are M3. STEAD, SEAM,
FORCE, GeoLink and PUNQ-S3 aggregate or synthesise across sites, so they are M2.

Applied to batch B: PetroGraph M3, TADI M3, GeoMind M2 (four multi-well public benchmarks),
Agents4GEOS M2 (PUNQ-S3), LandslideAgent M2 (own held-out benchmark; its case study names
only a province), GeoMCP M1 (one Eurocode 7 worked example, textbook-scale by the rubric's
own wording). The readers' six levels stand under the fuller rubric.

Worth noting for Section 05: **M3 here rests on public benchmark data from a named field,
not on proprietary access.** That is a different and weaker thing than an operator
retrospectively testing an agent on its own wells, and the distribution should not be read
as evidence of industrial engagement.

### Two mechanical faults found while transcribing

**Identity keys are not reconstructible from a DOI.** The harvest keys arXiv-sourced records
as `arxiv:2605.15028` but OpenAlex-sourced ones as `doi:10.48550/arxiv.2605.15028`, so the
same preprint takes either prefix depending on which API saw it first. Three of the six rows
in batch B were staged under a guessed `doi:` key and would have silently dropped out of the
admitted set, surfacing much later as a bare count mismatch. `core_append.py` now checks
every key against `screening.csv` and also cross-checks the subfield, so a mismatch fails at
the point of writing.

**Two titles needed correcting against the documents.** The record harvested as
"Autonomous Landslide Analysis" reads "Autonomous Landslide **Identification and** Analysis";
`AGENTS4GEOS` is styled `Agents4GEOS`. Both were corrected from the source rather than the
metadata.

### A reproducibility observation from batch B

Two of six full texts do not name their model. Agents4GEOS names Claude Code as the harness
and describes tier-based routing to "the cheapest model", "a mid-sized model" and "the most
capable one" without naming any of the three; GeoMCP names ChatGPT and Claude only as
examples of MCP-compatible clients and never says what ran the walkthrough. These are
full-text system papers, not abstracts — so the gap is in the papers, not in the reading.

### The first M4, and why it is not M5

HERMES is the only source so far whose output demonstrably left the paper. Its extraction
was archived unedited before review, adjudicated by domain experts, and released as the live
`treatise.geolex.org` database holding 32,277 taxonomic entities and 451,878 attributes,
produced in a time-bounded run of 7 calendar days per volume across 55 volumes for 53
cumulative person-days, against a manual baseline of 45 days for one volume.

That satisfies M4's "output entered a real workflow", and the run is time-bounded. The
rubric's "site or operator named" clause is written for field deployments and has no
referent for a literature-extraction system; the named institution and the published
database are the closest analogue, and I have treated them as sufficient rather than
disqualifying the source on a clause that cannot apply to it. **It stops short of M5 because
the adjudicating experts are co-authors**, so the verification is not "evidenced by someone
other than the vendor".

Recording this because a single M4 in a corpus this size will carry disproportionate weight
in Section 05, and the level rests on a clause I read permissively.

### Whether a home-made benchmark counts as M2

Batch C forced a second discriminator. GAIA is evaluated on a RAGAS-generated
question-answering set built from its own internal knowledge base and never released, plus a
deliberately simplified synthetic inversion the authors say "under-represents real world
scenario", plus four seismic monitoring capabilities shown only as single walkthrough figures
with no metrics. LandslideAgent is evaluated on its own LandslideBench — also home-made, but
held out and published with the code.

M2 requires a **reusable** benchmark, and reusability requires availability. LandslideBench
is released, so M2; GAIA's QA set is not, so M1, which the "Data source not stated: M1 at
most" tie-break also supports for its unprovenanced seismicity catalogue. GAIA is the more
ambitious system of the two and lands lower, which is the rubric working as intended: it
scores what the evaluation demonstrates, not the reach of the architecture.

### Retrieval and naming artefacts from batch C

`arxiv.org/html/2608.14055` returns HTTP 404 for every version because the HERMES submission
is PDF-only. The reader fell back to the PDF and text-extracted 37 pages, which inserts
spurious intra-word spaces; it normalised those and said so. `papers.md` records the route
and the normalisation on that block, because "verbatim" and "de-artefacted" are not the same
claim and the distinction should be visible to anyone checking a quote.

Two naming observations worth keeping for Section 02. **The string "Sim2Schedule" appears only
in that paper's title and never once in its body**, which calls the system "the LLM-based
framework"; the same document carries an unfilled ACM template placeholder
(`DOI: XXXXXXX.XXXXXXX Journal: taas`), so its venue is arXiv and nothing more. And the GAIA
paper's title contains no "(GAIA)" — the acronym appears only in the abstract and body. Both
titles were corrected from the documents.

### Batch G: six for six unreadable

Every one of the six records in the first paywalled batch failed to yield full text — SEG,
IEEE, Elsevier three times, and an ARMA conference paper. The reader tried the publisher
DOI, Unpaywall, arXiv, and a title search for preprints and repository copies before falling
back to bibliographic abstracts, and reported the routes per record. All six are demoted to
`context`, which is the provisional tiering rule coming due exactly as anticipated.

Three findings from the failures, recorded in `unreachable.md` and carried into Section 05:

**Nominal open access is not access.** `doi:10.1016/j.oregeorev.2026.107477` is gold OA with
a CC-BY-NC-ND licence and a publisher OA location per Unpaywall, and was still unreadable:
Cloudflare interstitial on the DOI, HTTP 403 on the PDF, captcha through a proxy, nothing in
Scholar Archive. The licence permits redistribution and the delivery refuses retrieval. Any
open-access count in this report is a licence status, not an access outcome.

**One record has only a truncated abstract.** `doi:10.1016/j.autcon.2026.107055` has no
abstract in OpenAlex, Crossref or Semantic Scholar; the only text is a partial copy recovered
through a search engine, cut off at both ends. Two of its six quote slots are NOT FOUND.

**The demotion has a measurable cost, and it is not symmetric.** Two of the six describe
evaluations shaped exactly like `M3` — Hydro-Agent's 18-dimensional inversion on the **Aquia
Aquifer** along a 96 km flow path, and the **Chagai Belt** map generalization with a 96.4%
copper assignment rate. Both name a real site, both are retrospective. Neither can be rated,
because the rubric rates the evaluation section and there was no evaluation section to read.
So the maturity distribution is not merely thinner for the paywalled literature, it is
**biased downward exactly where the field work is**: the industry and applied-journal papers
most likely to involve real sites are the ones least likely to be readable. Section 05 must
state this rather than present the distribution as a survey of the field's maturity.

### Batch A: seven seismology full texts, none paywalled

All seven `/html/` routes returned complete documents. Two of them report no quantitative
headline result at all — TREMORS and specfem-mcp are demonstration papers with illustrative
case studies rather than scored evaluations. specfem-mcp also states no limitations, only
future work; that absence is recorded as `none stated` rather than inferred.

Maturity under the fuller rubric: TRACE M3 (Ridgecrest and Santorini–Kolumbo, named
sequences, retrospective), GraphRAG-on-catalogs M3 (Qiaojia, Ridgecrest, Maduo), SeisEvo M2
(held-out field data that is never named, so the unidentified-site tie-break blocks M3),
the Thebe NAS work M2 (open fault benchmark; Exmouth Plateau origin does not make it a
site evaluation), TREMORS M1, specfem-mcp M1, Fortran-to-Devito M1.

One discriminator worth keeping: Campi Flegrei and Tohoku appear in specfem-mcp's case
studies, but they configure synthetic forward simulations and are never compared against
recordings. A named place in a simulation setup is not a named site in the rubric's sense.

Two of seven full texts still do not name the generation model. SeisEvo names only the EvE
search backend; the Fortran-to-Devito paper names GPT OSS 120B as the G-Eval *evaluator*
and describes the generator as "open-source Large Language Models" behind a "chat.ese LLM
API". That is now four of sixteen arXiv full texts that leave the generator unnamed.

### Four remaining batches failed on a usage-limit switch

The two open-access batches and the two remaining paywalled batches returned no extracts:
the child agents hit an "Other Models usage limit" and were aborted before fetching. They
are relaunched on the model now running this session. Until they return, 16 of 47 originally
core records remain unread (13 expected OA plus the remaining 12 paywalled after batch G's
six).

### Remaining 25: two full texts, twenty-three demotions

The four relaunched readers never progressed past their opening tool calls. I fetched
OpenAlex/Unpaywall metadata for every remaining DOI, downloaded the two PDFs that actually
arrived as `application/pdf` (Springer 3.4 MB, ACL Anthology 9.4 MB), and demoted the rest.

`papers.csv` now has 155 rows matching the admitted set. Core is 18, all full-text:
M1=7, M2=6, M3=4, M4=1. Screening tiers were updated for 29 demotions so the CSV and the
grid agree. `papers.md` has 18 extract blocks.

Sibling pairs to keep from double-counting as independent corroboration: GAGAW
(ESSOAr preprint + BDES article), MINDS (Arizona thesis + MDPI Mining article),
ESHM20-MCP (Zenodo software + npj paper).

### Hung children: stop waiting, parent continues

The four remaining readers were relaunched at 15:39. One returned: OA batch A, with full
text for six papers. The other three (OA B, paywalled A, paywalled C) accepted the interrupt
and then sat on it without fetching. Waiting on them is what froze the run twice. They are
left running if they still are; this parent no longer blocks on them.

### Four promotions from OA batch A

Batch D had demoted four records after Nature/MDPI landing pages failed. OA A obtained the
texts by a different route, so they are restored to core:

| key | route that worked | maturity |
|---|---|---|
| `doi:10.1038/s44304-026-00262-z` | arXiv PDF 2607.16249 (Nature AAP shell) | M2 |
| `doi:10.1038/s41598-026-61824-9` | Nature `_reference.pdf` accepted manuscript | M1 (unnamed confidential project) |
| `doi:10.3390/geosciences16050176` | MDPI PDF | M3 (Xiushan County tunnel, 102 events) |
| `doi:10.3390/mining6020026` | MDPI PDF | M1 (synthetic Marvin) |

`papers.csv` now has 155 rows: 23 core, all `full-text`, and 132 context. Core extracts
cover 23/23. Remaining original-core records that stayed context are still paywalled,
JS-blocked gold OA, or software-only Zenodo deposits, as listed in `unreachable.md`.

### Report written in this parent

Hung children were not relaunched. Sections `08`, `07`, `01`–`06`, `00` and `index.md`
were written here. AutoSurrogate (`doi:10.1016/j.aei.2026.105058`) was recovered from
arXiv HTML `2604.11945` during close-out — that was the stalled OA batch's readable
miss — and promoted to core (M1). GAGAW ESSOAr still 403; AGeoKE still abstract-only.
`found_via` on the 15 grey-admitted `papers.csv` rows was corrected from `harvest` to
`grey`. Four previously blank core `system_id`s were filled from the extracts.

## Close

- **Output:** `outputs/01_landscape/v0.5/`
- **Threshold:** `--min-score 3 --min-strong 1`. After the triage refix the shortlist is
  712, inside the 150–800 band. `min-strong` remains the binding cut among scored
  records; the earlier flat shortlist at scores 1–3 was the `scope_computed == none`
  defect, not the score knob.
- **False-negative rate:** 0% on the refixed 150-record below-cut sample (0 of 150
  admitted). The pre-refix sample was 0.7% (1 of 150) and is retained in
  `screening.csv` with `from_audit_sample` cleared.
- **Counts:** harvested 11,191 unique records (11,177 API + 14 grey extras);
  shortlisted 712; screening decisions 1,028; admitted 155 (23 core, all full-text;
  132 context, all abstract-only).
- **Admitted sources per subfield:** reservoir_engineering 68 (3 core), seismology 27
  (8 core), engineering_geology 19 (4 core), mining 14 (3 core), geological_modelling 9
  (2 core), inversion 5 (0 core), geothermal 4 (1 core), ccs 4 (2 core), hydrogeology 4
  (0 core), geomechanics 1 (0 core). Thin: inversion, geothermal, hydrogeology,
  geomechanics — three of those have no readable core source.
- **No abstract:** 1,646 of 11,191 harvested records (14%), screened on title. One
  shortlist record was `no-abstract-untriageable`. Two admitted context records also
  have no abstract (`doi:10.13140/rg.2.2.28926.65602`, `doi:10.2139/ssrn.5520018`);
  title is not architecture evidence.
- **Grey pass:** 11 of 40 permitted web calls (`w1`–`w11`); 17 screening rows, 15
  admitted as context. Could not reach OnePetro/EarthDoc full texts, SPE EnRG-LLM
  (webinar/vendor copy only), or a primary AGAPEX publication.
- **Snowballing:** 0 new records. AutoSurrogate was already in `screened.csv` under its
  Elsevier DOI; the arXiv HTML was a full-text route, not a new source.
- **Core maturity (sources, n=23):** M1 10, M2 7, M3 5, M4 1, M5 0.
- **Screening cuts (out):** periphery 347, not-geoscience 284, not-agentic 114,
  not-a-source 111, duplicate 12, pre-llm-only 4, no-abstract-untriageable 1.
- **v0.6:** (1) draw part of the audit sample from the highest-scoring below-cut
  records, not uniformly; (2) keep MCP / hyphen-tolerant agent patterns; (3) treat
  gold-OA flags as access hypotheses — Elsevier/ScienceDirect and Cloudflare still
  blocked readable PDFs, while an arXiv HTML twin may exist under a different key;
  (4) before demoting a DOI as unread, search arXiv by title; (5) do not delegate
  unread core batches to children that can hang on a usage-limit switch —
  parent-fetch or demote.

## Addendum, 2026-09-11 — paywalled full text recovered via institutional access

The counts and per-subfield table above are the snapshot at the end of this run and are
left as recorded. They no longer match `papers.csv`/`screening.csv`: eleven paywalled or
textually-empty records were subsequently read in full via the corpus owner's institutional
access (not a tool call in this run), seven were promoted to `core` and three of those
moved subfield, and four were reclassified from `in`/`context` to `out` on full-text
evidence that they are not agentic. Current totals after this first pass: admitted 151
(30 core, 121 context). See `unreachable.md` ("Second recovery pass") for the per-record
detail and `decisions.md` (2026-09-11) for what changed and why.

## Addendum 2, 2026-09-11 — a second institutional-access batch

A further eight paywalled records were supplied and read in full the same way. All eight
were genuinely agentic; none were reclassified `out`. One (the GAGAW journal record) moved
subfield from `inversion` to `hydrogeology`. Current totals after this second pass:
admitted 151 (38 core, 113 context) — total admitted is unchanged from the first addendum,
since this pass reclassified no record `out`. See `unreachable.md` ("Third recovery pass")
and `decisions.md` (2026-09-11, second entry).

## Addendum 3, 2026-09-11 — a third institutional-access batch

The three EAGE EarthDoc records left unresolved at the end of the second batch were
supplied as PDFs and read in full the same way (not a tool call in this run). All three
were genuinely agentic; none were reclassified `out`. One (the Seksaf sedimentological
workflow) moved subfield from `geological_modelling` to `reservoir_engineering`, with
`geological_modelling` kept as secondary. Current totals after this third pass: admitted
151 (41 core, 110 context) — total admitted is unchanged from the first addendum, since
neither this pass nor the second reclassified any record `out`.

- **Records:** `doi:10.3997/2214-4609.202535040` (Geowellex MCP + A2A surface logging,
  M2), `doi:10.3997/2214-4609.202639012` (LangGraph geological Q&A on the named
  Acacia Grove-1 well, M3), `doi:10.3997/2214-4609.2025640024` (four-agent RAG over
  Random-Forest sedimentological prediction, M2).
- **Core maturity after this pass (sources, n=41):** M1 14, M2 13, M3 13, M4 1, M5 0.
- **Sections regenerated:** 00, 01, 02, 03, 04, 05, 06, 08 and `index.md`. Section 06
  gained an entry; 07 is unchanged, being written from harvest counts only.
- **What this pass changed about a standing claim.** Every core source recovered in the
  first two institutional passes named a base model, and sections 02 and 04 said so. Two
  of these three do not, taking unnamed-model core rows from 9 of 38 to 11 of 41. Both
  claims are corrected rather than dropped: the format, not the recovery route, is what
  differs.
- **Store rename:** the supplied-PDF directory is now `01_unreachable_paper/`, formerly
  `paywalled_paper_2/`. Paths in earlier `papers.md` blocks are left as written; blocks
  added in this pass use the current name. The store remains outside this repository and
  untracked by decision.
- **Still unresolved:** IEEE CAIBDA (`doi:10.1109/caibda65784.2025.11182767`), IEEE
  CAIT/GALA (`doi:10.1109/cait70489.2026.11553853`), and the ESSOAr GAGAW preprint
  (`doi:10.22541/essoar.176336946.65126612/v1`). All remain `context`/abstract-only.
- **For v0.6:** conference extended abstracts can clear the `core` bar on full text but
  routinely omit base model, code availability and held-out status. If the next run reads
  many of them, `papers.csv` completeness per tier is worth reporting alongside the tier
  counts, so `core` is not read as a uniform evidence standard.

See `unreachable.md` ("Fourth recovery pass") and `decisions.md` (2026-09-11, third entry).
