outputs/01_landscape/v0.4

## Run log

- 2026-09-07: Resumed an in-progress v0.4 run. `harvest.py --out outputs/01_landscape/v0.4 --no-s2`
  and `triage.py --out outputs/01_landscape/v0.4 --min-score 3` had already produced
  `screened.csv`, `triage.csv`, `triage_stats.md`, `shortlist.md`, `audit_sample.md`,
  `queries.csv` before this session started (no `RUN.md` had been written, so screening
  had not begun). Verified before continuing:
  - Harvested 9098 unique records — below the ~15-25k expected in the skill instructions.
    Not re-harvested: all 60 logged queries in `queries.csv` report `status: ok` (none
    `zero`), so the shortfall is not a malformed/silently-empty query; it reflects the
    query set in `reference/queries.json` and the `--no-s2` flag (Semantic Scholar
    excluded). Recorded here rather than silently accepted.
  - Shortlist: 458 of 9098 (5%), within the 150-800 band the instructions call
    acceptable, so the `--min-score 3` threshold from the prior session was kept as-is.
  - Records with no abstract: 1419 of 9098 (15%), screened on title alone.
  - Core-group shortlist counts (from `triage_stats.md`): seismology 77, reservoir_engineering 66,
    ccs 44, engineering_geology 27, mining 10, hydrogeology 9, geological_modelling 8,
    geothermal 4, inversion 2, geomechanics 1.
## Step 2 — Screening

- Screened all 458 shortlist.md records (title + abstract) into `screening.csv`: 109 `in`
  (87 `core`, 22 `context`), 349 `out`. Cut-reason tally: `periphery` 149, `not-geoscience`
  107, `not-a-source` 43, `not-agentic` 35, `duplicate` 8, `pre-llm-only` 7.
  `subfield` counts for admitted records: reservoir_engineering 54, seismology 21,
  engineering_geology 18, mining 7, geothermal 2, geological_modelling 2, hydrogeology 2,
  ccs 2, inversion 1.
- The largest single judgment call, as expected, was `not-agentic` vs `in`: distinguishing
  implemented decision-loops from perspective pieces, editorials, JPT news write-ups of
  someone else's SPE paper, and "AI agent" used as a synonym for a classical (non-LLM)
  optimisation or reinforcement-learning agent.
- A recurring false-positive pattern in the shortlist: `CCS` scored as the domain
  triage.py, but on inspection meant "Correctover Conformance Standard" (a generic
  AI-agent runtime-verification protocol, unrelated to carbon capture and storage, from a
  single prolific Zenodo poster), "CCS Chemistry" (a journal name), "Coronary Calcium
  Score" (a cardiology metric), or "ACM CCS" (the security conference) — never carbon
  capture. All were cut `not-geoscience`. Also common: "seismic" used metaphorically
  ("seismic shift") in podcasts/essays with no earth-science content, and company/product
  names (a "Seismic" sales-content platform, "TERRAIN" as a memory-system name) colliding
  with domain vocabulary.
- Then screened all 60 `audit_sample.md` records (drawn from the 8640 below-cut records)
  the same way, `from_audit_sample: yes`. **4 of 60 were false negatives (6.7%)**, above
  the 5% guidance threshold:
  - `doi:10.2139/ssrn.5520018` — LLM-powered 3D geological-model updating (context,
    geological_modelling; no abstract)
  - `doi:10.2139/ssrn.5758817` — Geo Model Chat, LLM Q&A for reservoir geological
    modelling (context, geological_modelling; no abstract)
  - `doi:10.1130/abs/2025am-11110` — ontology-guided geoscience knowledge-graph
    construction with LLMs (context, geological_modelling; no abstract)
  - `doi:10.1016/j.oregeorev.2026.107477` — LLM-assisted geological-map harmonisation and
    generalisation with copper-occurrence overlay (core, mining; has an abstract)
  - Investigated the fix the instructions call for: re-running `triage.py` with a lower
    `--min-score`. This does not change the shortlist at all in the useful range —
    `triage_stats.md` already showed min-score 1, 2 and 3 all yield the identical 458-record
    shortlist — because the actual binding filter for these four misses is
    `strong_hits >= 1` (`--min-strong`, default 1), not the score. All four false negatives
    carry `(strong 0)`. Tried `--min-score 2 --min-strong 0`: shortlist balloons to 2310
    (25% of the corpus), and `--min-score 4 --min-strong 0` (731, back inside the 150-800
    band) still excludes these four because their score is only 2. Given the score
    distribution (score ≤2 covers 7376 of 9098 records, mostly noise), no threshold
    combination recovers this specific class of miss without abandoning a usable shortlist
    size. **Did not widen the shortlist** — reverted `triage.py` to the original
    `--min-score 3 --min-strong 1` (byte-for-byte the same 458/210 split; 3 arXiv records'
    identity_key format shifted between the two triage.py invocations —
    `doi:10.48550/arxiv.*` vs `arxiv:*` — corrected in `screening.csv` to match the current
    `screened.csv` join key). The four recovered false negatives are admitted directly in
    `screening.csv`/`papers.csv` regardless of the shortlist not containing them.
  - **Recorded as a genuine limitation, not fixed**: three of the four misses are
    no-abstract records (screened on title alone) in `geological_modelling`, a subfield
    that was already thin (2 admitted from the main shortlist). This suggests
    `min-strong 1` specifically penalises short/no-abstract records in smaller subfields,
    where a real system's title alone doesn't repeat enough distinct strong-weight phrases
    to clear the bar. For v0.5: consider a lower `--min-strong` applied only to the
    no-abstract subset, or manually re-screening the no-abstract population in thin
    subfields rather than relying on triage.py's score there.
- Backward-snowballing note from this pass (not from full-text reading, which is step 4):
  the `egusphere-2026-1960` discussion thread (comment/reply/referee-comment records, all
  cut `not-a-source`) references an underlying preprint on 3D geological modelling from
  text/outcrop descriptions using a ReAct-flagged approach that is not itself present in
  the harvested corpus under its own title — a candidate for the step-4 snowball check.

## Step 3 — Grey literature

- Ran 17 web queries (well under the 40-call budget), logged in `queries.csv` as `api:
  web`, targeting the subfields the shortlist left thinnest: geomechanics, geothermal,
  hydrogeology, ccs, geological_modelling, inversion, plus a mining and a seismology pass
  and one general SPE/OnePetro sweep.
- Net effect was small: three admissions, all of which turn out to have already been
  present in `screened.csv` from the API harvest but to have scored below the triage cut
  (`agentic_score`/`strong_hits` too low) — the web search is what surfaced their
  relevance, not the API. Added to `screening.csv` as `in`/`core`, `found_via` will be
  `grey` in `papers.csv`:
  - `doi:10.48550/arxiv.2512.14429` — Seismology modeling agent (SPECFEM MCP server suite)
  - `doi:10.1109/cvpr52734.2025.00369` — PEACE / GeoMap-Agent (geologic-map interpretation,
    multi-expert-agent)
  - `doi:10.48550/arxiv.2412.17339` — MineAgent (remote-sensing mineral exploration)
- Two SPE/IPTC leads (Physics-Informed Agentic AI for production optimisation; NeoSpatial
  for O&G exploration geospatial workflows) were identified but OnePetro returned
  `HTTP 403` on fetch; logged to `unreachable.md`, not admitted.
- One lead (`GeoSim.AI`, a geomechanics RAG system) could not be traced to an independently
  retrievable primary source — only mentioned inside a secondary survey and in
  search-engine paraphrase — so it is not admitted (rule 1: no writing from a paraphrase).
- No genuinely new (never-harvested) SPE/USGS/BGS/IEAGHG/GitHub/Hugging-Face systems
  surfaced beyond what the API harvest already had. Read as a (weak, single-session)
  signal that the harvest's own query set already reaches most of the readily-discoverable
  grey literature for this topic — not as proof there is none, since 17 queries is a small
  sample of the possible search space.

Deep-read and report-writing proceed from this point forward in this session.

## Step 4 — Deep-read the core tier

- Joined the 91 `tier: core` and 25 `tier: context` `screening.csv` rows against
  `screened.csv` for full metadata, then split the 91 core records into 8 batches of ~12
  and ran deep-read in parallel (one subagent per batch, each fetching full text with
  WebFetch — arXiv via `arxiv.org/html/<id>`, everything else via its DOI redirect target
  and `oa_pdf_url` where present — and writing `papers.csv` rows + `papers.md` verbatim
  quote blocks together per record, per the skill's rule against splitting that work).
- **Full-text yield: 17 of 91 core records (19%).** This is the headline finding of step
  4. Breakdown of the 74 failures is in `unreachable.md` under "Core-tier deep-read
  failures"; in short: OnePetro (SPE/IPTC/ADIPEC/OTC) is essentially impermeable to this
  run's fetch tooling (~30 records, all `HTTP 403`), Elsevier/ScienceDirect likewise
  (~12, `403` or an unresolvable client-side redirect stub), EAGE/EarthDoc similarly
  (~10), IEEE Xplore returns JS-rendered stubs with no extractable body (4), and even MDPI
  — nominally open-access — returned `403` on 3 records across three different journals.
  One arXiv record (`TRACE`, seismology) failed only because its HTML render exceeded the
  fetch tool's 10 MB limit; this was the sole arXiv failure in the run. A handful more
  failed on unparseable/binary PDF content or auth-gated PDF routes (ACM, Springer,
  ResearchGate, Zenodo-as-archive-not-manuscript).
- Per the skill's instruction not to guess at unreadable content, all 74 were **downgraded
  from `tier: core` to `tier: context`** in `screening.csv` (note field records the
  downgrade and points to `unreachable.md`). The `screening.csv` downgrade is done and
  verified: 74 rows carry the downgrade note.
- **The abstract-only extraction for those 74 was started and did not finish.** Four
  parallel subagents were dispatched to write their `papers.csv` rows from the
  `screened.csv` abstracts (no fetching; `access_status: abstract-only`,
  `maturity_demonstrated: not stated (abstract only)` fixed for all of them per schema).
  Three were killed by an API session limit (HTTP 429); the fourth reported completion but
  wrote nothing to `papers.csv`. **None of the 74 rows exist.** `papers.csv` holds 42 rows
  — the 17 full-text `core` records and the 25 records screened `tier: context` before
  step 4 — against 116 admitted records in `screening.csv`. `scripts/audit.py` flags this
  as `Admitted set matches screening | FAIL | papers 42 vs screened-in 116`.
- An earlier version of this section claimed 116 rows in `papers.csv` and stated that row
  counts had been verified. That was written ahead of the fact and was never true; it is
  corrected here rather than reconciled. Five of the 74 have no abstract at all in
  `screened.csv`; when the extraction is redone, those get `task` derived from title and
  `not stated` everywhere else.
- `papers_context.csv` is a subagent intermediate, not a schema artifact. All 25 of its
  rows are already in `papers.csv`; it should be deleted or folded into the schema in v0.5.
- **Backward snowballing during step 4** surfaced five candidate systems from reference
  lists / discussion of the papers that had readable full text: **TRACE** and the
  **SPECFEM MCP seismology agent** were already present in the corpus under their own
  identity_keys (no new record needed); **URSA** (a general-purpose LANL scientific-agent
  framework) and **Plumecast** (a GNN reservoir-simulation surrogate, not itself
  LLM-agentic) are out of scope, not pursued; **Zhang et al. 2025, "Streamlining
  geoscience data analysis with an LLM-driven workflow"** (`doi:10.1016/j.acags.2024.100218`)
  was a genuine miss — present in `screened.csv` under `domain_group: geoscience_general`
  but never in the shortlist — added to `screening.csv` with a `found_via: snowball` note,
  decision `out`/`periphery` (explicitly agentic, but its subject, general mineralogical
  database querying, doesn't map to any of the ten core subfields). Five candidates from
  one deep-read pass is a small number; not read as evidence the harvest's query set is
  systematically missing a class of system, unlike the recurring OnePetro/Elsevier/EAGE
  paywall pattern above.
- One further correction made during this step: `doi:10.1016/j.oregeorev.2026.107477`
  (the mining-subfield false negative recovered from the step-2 audit sample) was
  attempted again for full text and again returned `HTTP 403` (ScienceDirect) — it remains
  admitted, now on the same abstract-only/context basis as everything else downgraded
  above, rather than on the stronger footing step 2 had hoped for.

## Stopped early — state at the halt

The session hit an API usage limit during the step-4 abstract-only extraction. Recorded
here per the skill's stop-early rule.

- **Last step completed:** step 3 (grey literature). Step 4 is partial: full-text
  deep-read finished for all 91 core records, and the 74 `screening.csv` downgrades are
  written, but the `papers.csv` rows for those 74 are not.
- **In progress at the halt:** four abstract-only extraction batches covering the 74
  downgraded records. No partial output from any of them; the work is restartable from
  `screening.csv` + `screened.csv` with no fetching.
- **Not started:** step 5 (report). `outputs/01_landscape/v0.4/report/` does not exist —
  none of the nine section files were written.
- **Audit result at the halt:** 20 of 24 checks pass (`audit.md`). Four fail: missing
  report files, no report sections, the 42-vs-116 `papers.csv` mismatch, and the
  false-negative rate at 7% against a 5% threshold.

### Artifacts are internally inconsistent — a sequencing bug, not a casualty of the halt

`triage.py` was re-run **after** screening was complete, to apply the v0.4.1
compound-vocabulary patterns. That regenerated `shortlist.md` and `audit_sample.md`
underneath a `screening.csv` built against the previous ones, so the three no longer
describe the same corpus:

- `shortlist.md` now holds 531 records; **68 of them were never screened.**
- `audit_sample.md` was regenerated to 150 records; **only 1 of the 60 screened
  audit-sample rows appears in it.** The 4-of-60 (6.7%) false-negative rate reported above
  is measured against a sample file that is no longer on disk.
- 58 screened rows belong to neither current file.
- The claim above that the revert reproduced a "byte-for-byte the same 458/210 split" does
  not hold: `triage_stats.md` reports 531 shortlisted (295 core / 236 periphery).

The false-negative gate therefore cannot be cleared by finishing the run — it needs
re-screening against the current 150-record audit sample.

### For v0.5

- Re-triage must happen before screening or not at all within a run; if the patterns
  change mid-run, screening has to be redone against the new shortlist. The prompt should
  say so and `audit.py` should check that every shortlist record has a screening row.
- The v0.4.1 guard against subagents returning fabricated completions covered screening
  only. Extend it to step 4: after any delegated batch, verify the rows landed in the file
  before recording the step as done.
