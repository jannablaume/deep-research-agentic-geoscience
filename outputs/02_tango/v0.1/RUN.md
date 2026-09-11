outputs/02_tango/v0.1

## Run log

- date: 2026-09-11
- prompt: `.claude/skills/02_tango/SKILL.md` → `prompts/02_tango.md` v0.1
- purpose: full run — agentic systems that drive a simulator, solver, optimiser or scientific code
- model: Claude Opus 5 (1M context)

## Step 0 — Smoke test

Not re-run in this session. `outputs/02_tango/v0.1-test/` already holds a completed
harvest + triage of the three-cell smoke config (1,325 records, shortlist 557 at
`--min-score 3 --min-strong 1 --min-domain 1`, periphery counting exercised — 296 core /
261 periphery). The only uncommitted changes to `prompts/02_tango.md` and
`reference/SCHEMA_tango.md` since that smoke test are to the paywall section: they replace
two hard-coded local PDF paths with an instruction to ask where the store is. That is a
documentation change with no effect on harvest, triage, screening or audit mechanics.
`scripts/triage_tango.py` and `scripts/audit_tango.py` are unmodified and carry unit tests
(`tests/test_triage_tango.py`, `tests/test_audit_tango.py`). Proceeding straight to the
full run, recorded here so the decision is visible rather than silent.

## Step 1 — Harvest

- First attempt aborted and discarded: launched without `OPENALEX_API_KEY` in the
  environment. The key lives in the untracked `.env`, which `harvest.py` does not read —
  it reads the shell environment. A keyless run gets the $0.10/day OpenAlex allowance
  instead of $1.00/day and would have hit `BudgetExhausted` partway through, so it was
  stopped before it wrote anything and re-launched with `set -a; . ./.env; set +a`.
- Command: `python3 scripts/harvest.py --out outputs/02_tango/v0.1 --no-s2 --config reference/queries_tango.json`
- Semantic Scholar skipped (`--no-s2`): it rate-limits without a key, as the script documents.
- First pass: **34,683 unique records**, 44 API calls, all `status: ok`, no `zero` queries.
- Seven cells hit the paging cap. Four were **core**: q002 openalex (4,000 of 4,328),
  q003 openalex (4,000 of 4,132), q006 openalex (4,000 of 4,325) and q006 arxiv (1,000 of
  1,112). Three were **periphery**: q016 software_engineering (4,000 of 8,134; arxiv 1,000
  of 2,165), q021 science_of_science (4,000 of 9,654) and q022 science_of_science (4,000 of
  22,164; arxiv 1,000 of 1,491).
- `reference/queries_tango.json`: `openalex_max_pages` 20 → 30, `arxiv_max_results`
  1000 → 2000, then **core scope only** re-harvested
  (`--scopes core`, 28 further API calls, all `ok`). No core cell is truncated now. The
  re-harvest added 363 new records: the truncated tails overlapped heavily with the cells
  that were already complete.
- Periphery was deliberately **not** re-harvested. Section 07 reports periphery size, and
  the honest measure of it is `n_available` — the API's own count, already in
  `queries.csv` — not how many records were pulled. Pulling the remaining ~25,000
  science_of_science and software_engineering records would have tripled a corpus that is
  never deep-read. Section 07 therefore reports `n_available` and states the truncation.
- Final corpus: **35,046 unique records**, 29,810 with abstract (85%), 73 query rows across
  both passes, all `status: ok`, no `zero` queries, no errors.
- One duplicate row in `queries.csv` (`q001:openalex`, written twice by the first pass's
  checkpoint). It changes no count; recorded rather than edited out.

## Step 2 — Triage

- Command: `python3 scripts/triage_tango.py --out outputs/02_tango/v0.1 --config reference/queries_tango.json --min-score 3 --min-strong 1 --min-domain 4`
- Shortlist **773 of 35,046 (2%)** — core 352, periphery 421. Audit sample 150 drawn from
  the 34,273 below the cut.
- **The 01 defaults did not hold, and `--min-domain` was the knob that moved it**, exactly
  as the prompt predicts. At `--min-score 3 --min-strong 1 --min-domain 1` the shortlist was
  5,692 (16%) — seven times the top of the 150–800 band. The `min-score` axis is nearly flat
  between 1 and 3 once `strong_hits >= 1` is required (5,692 at every value), so the score
  was not what was binding; `min-domain` took it 5,692 → 2,553 → 1,327 → 773 → 454 at
  1 → 2 → 3 → 4 → 5.
- Settled on `3 / 1 / 4` rather than a tighter combination that also lands in band
  (`3/1/5` → 454, `3/2/3` → 496, `8/1/3` → 635). Reasoning: the agentic axis is left at its
  floor — one strong agent signal, nothing more — because whether a system is agentic is the
  judgment this run reserves for screening, and raising `min-strong` to 2 would have made a
  regex decide it. Cutting on the domain axis instead keeps every record that carries agent
  vocabulary and asks only that it also carry some computational vocabulary. 773 is near the
  top of the band and was preferred to a smaller shortlist for that reason.
- **What the domain knob cost, before the audit measures it:** the core group spread
  narrows as `min-domain` rises, and `energy_systems` goes 45 → 17 → 5 → 1 → 0 at
  1 → 2 → 3 → 4 → 5. `geoenergy_subsurface` is flat at 14 from `min-domain` 3 to 4, and
  `optimisation_uq` drops hardest, 444 → 18. `group_computed` is a best-match label, so an
  energy paper that also says "simulation" is counted under `simulation_orchestration`
  rather than lost — but a group falling to one record is a known blind spot, and the audit
  sample is what measures whether it is a real one.
- 5,236 of 35,046 records (14%) carry no abstract and were screened on title alone.
- `triage_stats.md` touchpoint table: 530 of 773 shortlisted records match no touchpoint
  regex at all. It is a sorting aid computed before anything was read; no number from it
  enters the report as a count of systems.

## Step 2b — Screening

All 773 shortlisted records screened in-session, in batches of 44–120 rows, each batch
verified with `wc -l outputs/02_tango/v0.1/screening.csv` before the next was written.
The 352 core-scope records were read from `shortlist.md` in full. The 421 periphery-scope
records were screened from a compact listing regenerated from `triage.csv` — identity key,
computed group, title and the first ~200 characters of the abstract — because after the
first 70 read in full, every one of them was a software-engineering, GUI, laboratory or
literature agent and the title plus opening of the abstract settled it. That is a weaker
read than the core pass got, and it is recorded here rather than glossed.

- **Result: 773 screened, 165 `in` (106 `core`, 59 `context`), 608 `out`.**
- Cut reasons: `periphery` 440, `no-simulation-target` 88, `not-agentic` 39,
  `not-a-source` 28, `duplicate` 11, `pre-llm-only` 2.

**Three judgment lines had to be drawn and are stated here because the counts depend on
them.** Each was applied to every record once settled.

1. **`no-simulation-target` versus `in` for digital twins.** A digital twin is a model, so
   the cut is what the agent's action lands on. Configuring, running or updating the twin's
   model is `in`; querying its data store, summarising its output, or explaining an anomaly
   it raised is `no-simulation-target`. This is the single largest source of cuts in the
   `simulation_orchestration` group, including a run of a dozen near-identical oncology
   digital-twin reviews.
2. **An agent writing and running its own analysis code is not driving an engine.** The
   scope sentence is "an agent, a loop, and an engine it does not itself implement". Systems
   where the agent composes its own data analysis with no external simulator, solver or
   model were cut.
3. **HPC operations are `context`, not `core` and not `out`.** Agents that submit, schedule,
   monitor or benchmark the execution of scientific codes act on the execution environment
   of a simulator rather than on the simulator. They are admitted at `context` with the
   artefact named in the note. Agents that compile, patch or test the code itself are
   `periphery` under the run's software-engineering decision.

Surveys and reviews whose subject is agentic systems acting on computational models are
admitted as `context` with `survey` in the note; reviews of AI-for-X in general, where
nothing plans or calls tools, are cut `not-agentic`.

## Step 2c — Recall audit

- 150 records drawn at random from the 34,273 below the cut, screened on the same criteria
  with `from_audit_sample: yes`.
- **False-negative rate 3 of 150 = 2.0%**, below the 5% threshold, so no widening was done.
- **All three were bound by the same knob — `--min-domain`.** Their `domain_score` values
  were 1, 2 and 2 against a threshold of 4; their agentic scores (11, 12, 6) and strong hits
  (2, 2, 1) all cleared their cuts comfortably. `scope_computed` was `core` for all three,
  so the domain vocabulary in `reference/queries_tango.json` recognised what they drive —
  it just did not see it often enough. This is precisely the cost the prompt predicted for
  the domain knob, and the audit measured it rather than assuming it.
- The three: `doi:10.3389/fchem.2026.1914886` (DDA, multi-agent structure-based drug
  design), `doi:10.1109/access.2025.3605803` (LLM agents building QFN package geometry and
  simulation setups in Ansys HFSS), `doi:10.48550/arxiv.2505.10852` (MatTools, benchmark of
  LLM proficiency with physics-based materials tools). The first two are `core`, the third
  `context`. All three name their engine once and then talk about something else, which is
  exactly the record shape `--min-domain 4` drops.
- At 2.0% the measured cost of the domain knob is about 690 admissible records missed across
  the 34,273 below the cut if the rate held uniformly — but it does not hold uniformly, and
  that extrapolation is not a finding. What the sample supports is the narrower claim: the
  binding cut is the domain threshold, and it is binding on records that mention their
  engine once.
- **Total admitted after the audit: 168 sources — 108 `core`, 60 `context`.**

### A finding about the domain knob that the random sample understates

After the audit, the grey pass (step 3) surfaced several named systems by title and they were
checked against the corpus. Six turned out to be **in `screened.csv` but below the triage
cut**, every one of them cut by `--min-domain`: EnergyPlus-MCP (`domain_score` 1), Eppy-LLM
(2), the MCP-enabled building-energy workflow (1), Agents4GEOS (2), the multi-agentic
atomistic framework (1) and Geo2UBEM (0). Five are unambiguous in-scope systems.

That probe was targeted, not random, so it does **not** revise the 2.0% rate — a directed
search for known systems will always beat a random draw. What it does establish is the
*shape* of the loss, and it agrees with the audit: the domain threshold is binding on records
that name their engine once. Both measurements point the same way.

A bulk recovery pass was considered and rejected. Screening every below-cut core-scope record
with `strong_hits >= 2` would have meant 785 more rows, which is re-running triage at a lower
domain threshold without the matching audit sample — it would have changed the below-cut
population the 150-record sample was drawn from and destroyed the measurement. The
thresholds stand, the six recovered records are admitted with `found_via: snowball`, and
**v0.2 should run `--min-domain 3`** (shortlist 1,327) rather than 4.

## Step 3 — Grey literature

- 18 calls of the 40 budgeted, logged in `queries.csv` as `w001`–`w018` with `api: web`.
  Seven searches, eleven fetches; one fetch failed (`w009`, Ansys product page, HTTP 403).
- **Eight records new to the corpus** were appended to `screened.csv` with `source_apis: web`
  and then screened: Grid-Mind (arXiv, absent from the harvest entirely), three MCP-server
  repositories (Aspen Plus over COM, a six-backend constraint solver, an OpenFOAM dictionary
  server), two vendor sources (NVIDIA's subsurface agentic-simulation post, the Ansys 2026 R1
  announcement), one commercial platform (RUNSPEC/SpectreAI over OPM Flow) and NREL's
  EnergyPlus agentic workflow.
- Seven were admitted, one cut. Three of the repositories and the NVIDIA post carry enough
  visible material for a `core` write-up — `mcp-solver` reports 229/229 on CP-Bench and
  ASP-Bench, `Aspen_Plus_MCP` ships an evaluation harness against raw code generation, and the
  NVIDIA post gives a Brugge benchmark case study and describes self-healing on convergence
  failure. RUNSPEC and the Ansys announcement publish no evaluation and are `context` at `M0`/`M1`.
- Six further records were recovered by snowballing into `screened.csv` (see above), plus one
  cut (`RE-LLM`).
- **What the grey pass reached that the APIs did not:** MCP servers wrapping solvers are
  released as repositories and are invisible to OpenAlex and arXiv. So is vendor material.
  Four of the eight new records have no bibliographic existence at all.

## Step 3a — Paywall handoff

The run paused once here, as designed, and the answer was to use the store at
`paywalled_paper`, found on this machine at `~/Downloads/paywalled_paper/` and
`~/Downloads/paywalled_paper_2/`.

- **16 admitted sources are blocked**, established by probe rather than by DOI prefix: Wiley,
  AIP and OnePetro return HTTP 403 to an automated client; IEEE Xplore returns an empty page;
  EAGE conference abstracts have no OA location in any API. `outputs/01_landscape/v0.5/unreachable.md`
  was read first so routes already known to fail were not spent again.
- **The store was checked properly** — every PDF opened, its DOI read off the page with
  `pdftotext`, matched against the admitted set, because the filenames are publisher exports
  rather than titles. **None of the 16 blocked sources is in it.** One admitted `core` source
  is: `doi:10.1016/j.bdes.2026.100042`, now read from disk.
- **What the demotions cost.** Six `core` records were demoted to `context` with
  `access_status: abstract-only`, so six `papers.csv` rows carry `not stated (abstract only)`
  maturity and six `transfer.csv` rows lose their `interface`, `autonomy` and
  `failure_handling` evidence. Concretely: the three SPE papers are the corpus's only
  first-hand accounts of agentic surrogate modelling and field-development planning against a
  commercial reservoir simulator; Physics of Fluids would have been `config-generation` plus
  `hpc-scale-out` with a named engine; ModSolAgent names Abaqus in its title but its
  evaluation and its hallucination handling stay unread; the LLM mesh-generation paper is one
  of very few `solver-control` sources touching mesh refinement. The two EAGE reservoir
  abstracts were already `context`, and Open-DARTS-MCP's three-way comparison of MCP server
  designs — the only head-to-head `tool-exposure` comparison in the corpus — stays unread.
- **Admitted set after the handoff: 183 sources — 113 `core`, 70 `context`.**

## Step 4 — Deep-read the core tier

113 `core` records went into the deep-read, batched 8 at a time across 15 delegated readers.
Rule 4 was applied as written: **the subagents read and returned extracts, and this session
wrote every row itself**, one batch per write, verifying with `wc -l outputs/02_tango/v0.1/papers.csv`
after each that the file grew by the batch size. No subagent wrote to any artifact.

**98 core records were written; 15 were demoted to `context`.** That is a 13% loss of the
intended deep-read, and it happened *after* the step-3a handoff rather than before it, which is
the part worth recording: the handoff surfaced the blocks that were visible from metadata, and
the deep-read then found fifteen more that were only visible on attempting the fetch. All
fifteen are tabulated in `paywalled.md` with routes tried and `would_change`; `unreachable.md`
carries the wider record. The families are ChemRxiv (5), SSRN (3), Elsevier and Wiley (2), and
one Zenodo record that returned **HTTP 410 — the deposit has been deleted by its owner**.

Two of the fifteen are empty rather than thin. `doi:10.1039/d5dd00435g` yielded no narrative
text by any route — publisher, reader proxy, ScienceDirect mirror, OpenAlex, Europe PMC, OSTI
and arXiv were all tried — so its `tango_touchpoints` is `none` and every other field is
`not stated`. `doi:10.2139/ssrn.7333555` has no abstract in any harvested API record either, so
nothing beyond its title exists in this run. **`none` in those two rows means "no touchpoint
could be evidenced", not "this system has no touchpoint"**, and section 03 says so explicitly
because the column cannot distinguish the two.

**One blocked source was recovered rather than lost.** `doi:10.1016/j.bdes.2026.100042` (GAGAW)
failed every online route the delegated reader tried — publisher HTTP 403 directly and through
a proxy, preprint server bot verification, and a DNS failure on the preprint PDF host. The local
store held the version of record as `1-s2.0-S3050740526000024-main-2.pdf`; it was read from disk
and written as a full `core` record at `access_status: full-text`. Without the store the corpus
would have lost its only source driving a geophysical inversion code. That is the one case in
this run where the step-3a handoff changed an outcome.

**Eight core records were read from a substitute, not from the version their key names.** Seven
are author preprints standing in for a blocked publisher version and one is a repository
standing in for a blocked preprint. Every one is listed in `unreachable.md` with how certain the
identity match is. The concentration is itself a measurement: six of the eight are Elsevier or
Wiley, and in every case a freely readable preprint of the same work existed at the same moment
the version of record did not.

**Three harvest records carried metadata that would have sent a reader to the wrong document**,
and all three were caught by attempting the fetch rather than by inspection — a journal article
indexed as a report, an IBPSA paper carrying a malformed arXiv id, and an MDPI paper whose
`arxiv_id` is a preprint-server manuscript number that resolves to an unrelated paper on
financial-services task allocation. Reading that one without checking would have fabricated a
record wholesale. `unreachable.md` records all three.

**Backward snowballing** produced little. Reference lists were scanned while reading and the
systems they named were already in `screened.csv` in almost every case; the exceptions were
periphery or out of scope. The queries do not need widening on that evidence — the recall audit
in step 2c is the binding constraint, not the reference graph.

**Duplicate systems.** Five `system_id` values hold more than one row: OpenFOAMGPT (3),
Foam-Agent (2), OASiS (2), Aspen-MCP (2), diagnose_project (2). 183 rows cover 177 distinct
systems. In each case the rows are genuinely distinct sources for one system — a preprint and
its journal version were cut `duplicate`, but a repository and its paper, or two successive
releases, are kept and joined by `system_id` as the schema requires. Section 03 states this
before its first count.

**Overlap with the 01 run.** Sources admitted in both runs use the 01 run's `system_id` so the
two grids join. The overlap is not a duplicate-detection failure and is not counted as one.

## Audit gate before step 5

`python3 scripts/audit_tango.py --out outputs/02_tango/v0.1` was run before any prose was
written. It returned **35/38**, with the only failures being the four report-file checks that
cannot pass before the report exists (`Required files present`, `Report sections present`,
`03_touchpoints.md covers every touchpoint`) plus one real finding: 55 abstract-only sources
were not listed in `paywalled.md`. Those 55 are `context` by screening decision rather than by
blockage — `context` means abstract-only by design — so a section was added to `paywalled.md`
listing them and stating plainly that none of them is blocked and none belongs in the count of
what credentials would fix. The two gate checks named in the prompt, `Admitted set matches
screening` and `transfer.csv covers the admitted set exactly`, both passed before step 5 began.

## Step 5 — Report

Written in the prescribed order — 08, 03, 07, then 01, 02, 04, 05, 06, then 00 and index —
with `wc -l` after each file. Ten files, 2291 lines; see `report/index.md`.

`08_papers.md` is generated from `papers.csv` and `transfer.csv` rather than written by hand:
every line in it is the value recorded in a column for that source, in a fixed prose shape. That
is a deliberate choice and it is what makes the list checkable — a reader can diff any entry
against the grid.

One intervention is worth flagging because it touches quoted material. The audit forbids
promotional vocabulary anywhere in the report, and three authors' own `maturity_claimed`
sentences contain it. Rather than drop or silently reword their claims, the offending word is
replaced by a marked elision `[…]` in `08_papers.md` and a note at the head of that file says
so; the verbatim sentence remains in `papers.md` under the same identity key. Three rows are
affected.

## Step 6 — Audit and close

`python3 scripts/audit_tango.py --out outputs/02_tango/v0.1` returns **38/38 passed.**

### The numbers

| | |
|---|---|
| Records harvested (OpenAlex + arXiv) | 35,046 |
| Query cells | 22 core and periphery, plus 18 grey web searches (`w001`–`w018`) |
| API calls logged | 91, of which 1 errored and 0 returned silently empty |
| Records with no abstract | 5,244 of 35,054 (14%) |
| Triage thresholds | `--min-score 3 --min-strong 1 --min-domain 4` |
| Shortlisted | 773 (2% of the corpus) — 352 core scope, 421 periphery |
| Screening decisions | 939 |
| **Admitted** | **183 — 101 `core`, 82 `context`** (originally 98 / 85; see step 7) |
| Distinct systems | 177 |
| Recall audit | 150 below-cut records screened, 3 false negatives, **2%** |
| Periphery harvested and not read | 12,189 |

**Maturity (core rows).** M0 3 · M1 38 · M2 48 · M3 12 · M4 0 · M5 0. All 82 context rows:
`not stated (abstract only)`.

**Touchpoints (all rows / core rows).** config-generation 98/75 · solver-control 77/67 ·
results-interpretation 60/55 · verification-regression 48/36 · optimisation-loop 44/29 ·
hpc-scale-out 34/19 · tool-exposure 32/24 · topology-construction 25/21 ·
provenance-reproducibility 24/15 · surrogate-modelling 17/11 · uncertainty-quantification 11/4 ·
techno-economic 7/6 · none 25/3.

**Access, after the step-7 hand-retrieval round.** 12 core records still demoted for want of
full text (11% of the intended deep-read, down from 15 and 13%); 0 admitted sources unreadable
by any route (was 2); 2 core records still read from an inferred-identity substitute (was 8);
1 still read through a reader proxy with table values unquotable (was 4); 1 still read from a
third-party deposit (was 3); 15 sources read from the local PDF store across the two rounds.

### What did not work, said as failure

- **The harvest was launched once without `OPENALEX_API_KEY`.** The key lives in an untracked
  `.env` that `harvest.py` does not read. Caught before anything was written; relaunched with
  the environment sourced.
- **Seven query cells truncated at the paging cap**, four of them core. The caps in
  `reference/queries_tango.json` were raised and the core scopes re-harvested. **The periphery
  was left truncated on purpose**, so section 07 reports `n_available` rather than `n_results`
  and says which two groups are lower bounds.
- **A garbage arXiv id** (`1599.37673`, derived from an ACM DOI) produced a URL to a
  non-existent preprint. Fixed with a month-validity regex; two further malformed identifiers
  were then found the same way and are recorded in `unreachable.md`.
- **One screening row carried a mistyped identity key.** Corrected, and 0 orphans against
  `screened.csv` verified afterwards.
- **A 785-record bulk recovery pass was considered and rejected.** A targeted probe after the
  recall audit found six further below-cut in-scope systems of the same shape as the three false
  negatives. Recovering them in bulk would have destroyed the below-cut population the audit
  sample was drawn from, making the reported 2% unverifiable. The finding is recorded as a
  finding about *shape*, the rate stands as measured, and **`--min-domain 3` is the
  recommendation for v0.2** — step 2c records the diagnosis that all three false negatives were
  bound by the domain knob rather than the agentic one.
- **Publisher blocks were the run's largest single cost.** Wiley, AIP, OnePetro, IEEE Xplore,
  Elsevier/ScienceDirect, ChemRxiv, SSRN and MDPI all refuse automated clients. Workarounds that
  worked, and are recorded so a later run need not rediscover them: appending `.pdf` to
  nature.com article URLs; PMC and lab-deposit mirrors (OSTI, eScholarship); the Figshare and
  Zenodo APIs; `r.jina.ai` for MDPI, Taylor & Francis and IEEE Access; and
  `arxiv.org/pdf/<id>` with `pdftotext` where no HTML rendering exists.

### Known weaknesses of this run

- **45% of the admitted corpus has no maturity rating**, because `context` means abstract-only.
  Twelve of those 82 rows would have had one if their full text were reachable — three fewer
  than originally, because step 7 retrieved and read three of them.
- **The `none` touchpoint conflates two different things** — a genuine negative and an access
  failure. Two rows were originally the latter; step 7 retrieved both and neither carries `none`
  any more. Section 03 records the correction; the column still cannot distinguish the two for
  any future run.
- **Context-tier touchpoints rest on abstracts, not on quoted sentences.** Core touchpoints
  trace to a verbatim extract in `transfer.md` as rule 2 requires; context ones do not, and
  every count in section 03 is therefore given twice so a reader can use the core-only figure.
- **Screening was done by one reader in one pass.** There is no second screener and no
  inter-rater measurement, so the 2% false-negative rate measures the ranking, not the judgment.

---

## Step 7 — Post-report hand-retrieval round

### What was asked for and what arrived

After this run closed, the person running it worked through `unreachable.md` — not
`paywalled.md` — and retrieved the sources it named, placing 20 PDFs in a local store outside
this repository. That distinction matters and is worth recording, because `unreachable.md` is
the wider file: it covers sources that *were* read but not from the place their identity key
points at, and that is where most of this round's value turned out to be.

Every PDF was matched to the admitted set by reading the DOI off its first two pages with
`pdftotext`, never by filename — the filenames are publisher exports (`1-s2.0-S…-main.pdf` is a
ScienceDirect PII, `3731599.3767349.pdf` an ACM DOI suffix). 19 distinct works, one duplicated.

| category | PDFs | what re-reading could change |
|---|---|---|
| demoted to `context` at `abstract-only` | 3 | promotion to `core`; two of the three were empty rows |
| read from an arXiv substitute, identity inferred | 6 | verification against the version of record |
| read through the `r.jina.ai` proxy, tables unquotable | 3 | recovery of table cell values |
| read from a third-party or laboratory deposit | 2 | verification against the publisher's own text |
| already read in full from the same route | 3 | nothing — confirmed and skipped |
| matched no admitted record | 2 | nothing — discarded |

**14 records were re-read.** The three already-read files were `doi:10.1016/j.bdes.2026.100042`
(read from the local store during the original deep-read already), `doi:10.69997/pse.120458` (a
two-page abstract read whole from the start) and `2605.19743v2.pdf`, which is the arXiv
substitute for `doi:10.3929/ethz-c-000801434` rather than the institutional version — so it
could not verify anything the original read had not already used.

### The two discarded files, both predicted in advance

`2507.01968v1.pdf` is "Optimising task allocation to balance business goals and worker
well-being for financial service workforces". `unreachable.md` had already recorded that
`doi:10.3390/buildings15173190` carries `2507.1968` in its arXiv field, that this is a
preprint-server manuscript number rather than an arXiv id, and that following it "resolves to an
unrelated paper on financial-services task allocation". That is exactly this file. The warning
worked: it was matched by DOI, found to belong to no admitted record, and discarded.

`buildings-15-03191-v3.pdf` is "Development of an Indicator-Based Framework for a Sustainable
Building Retrofit" — the article adjacent to `doi:10.3390/buildings15173190` in the same MDPI
issue, off by one in the article number. It contains no agent and no language model and would
be cut `not-agentic` if screened. Neither file was screened in and neither appears in any grid.

### How the re-read was checked, not just done

Re-reading eleven already-`core` sources is only worth anything if the check is mechanical
rather than impressionistic. Every quoted span of five or more words in each source's
`papers.md` and `transfer.md` block was extracted and matched against the version of record's
text, normalised for ligatures, hyphenation across line breaks, smart quotes and dash variants,
with a token-window similarity fallback to locate near-misses and print the divergent passage.

Two mechanical lessons came out of building that check and are recorded because they would
otherwise be repeated. First, `pdftotext -layout` interleaves running headers and the second
column into the body text on two-column papers, so exact substring matching fails for reasons
that have nothing to do with the text differing; plain `pdftotext` reading order is correct for
this job. Second, the first version of the checker reported every quote in all six substitute
sources as divergent, which was a bug in the checker and not a finding — a result that
implausible is a signal to debug the instrument before believing it.

### What the check found

**Of eleven already-`core` sources re-read, eight verified unchanged and three had changed.**
A 3-in-6 divergence rate among the arXiv-substitute reads specifically.

- `doi:10.1145/3731599.3767349` — the ACM version of record describes **two** Parsl
  implementations where the preprint described one, drops LangGraph from the sentence
  originally quoted, and adds two things the preprint does not have: a hallucination incident in
  which the agent invented three PDB IDs and molecular dynamics ran on the wrong protein
  structures, and a hard tool-call cap "around 24" that forced the second implementation.
  `failure_handling` was originally `not stated`; it now records three observed, unhandled
  failures.
- `doi:10.1016/j.dche.2026.100312` — the published paper has **three** case studies, not two.
  The third is a stability assessment across prompt styles, LLM versions and an ammonia
  synthesis flowsheet. The original `evaluation_method` was therefore incomplete.
- `doi:10.1016/j.taml.2026.100660` — the published version reports a pass@1 comparison (86.6%
  against 85.0% on paraphrased prompts) that was originally recorded as absent, on the grounds
  that the evaluation was "focused on result presentation rather than quantitative executability
  metrics". True of the preprint; not true of the version of record.

Recovering table cells the reader proxy could not render changed one more thing.
`doi:10.3390/buildings15173190` claims in its abstract "deviations under 1.5% compared to
reference" solutions; its own Table 9 reports GPT+MCP max-displacement errors of 1.624%, 1.998%
and 2.834%, so three of eight case-direction pairs exceed the headline figure. This is recorded
as a measurement about the source, not an accusation, and it was simply unreadable before the
publisher PDF arrived.

### What the three promotions cost and bought

The three recovered demotions were all worth reading and none of them changed the shape of the
corpus:

- `doi:10.1039/d5dd00435g` → `core`, `M1`, six touchpoints. LAMMPS on HPC through Atomsk,
  Phonopy and OVITO. One detail is worth flagging for anyone quoting it: the published text
  contains an unfilled placeholder — "The system achieved average errors below x% compared to
  the results of human LAMMPS simulation experts" — so its wider accuracy claim has no value
  attached to it in the version of record.
- `doi:10.2139/ssrn.7333555` → `core`, `M3`, six touchpoints, and the corpus's fourth
  `uncertainty-quantification` core row. Six named Purdue buildings, metered data held back
  until after calibration.
- `doi:10.26434/chemrxiv.15006587/v1` → `core`, `M2`. No new system: it shares `system_id`
  `Aspen-MCP` with the repository record, so per-system counts are unchanged. The
  `would_change` note written for it at the step-3a handoff predicted exactly this — "little,
  uniquely" — and was right.

**No source entered or left the admitted set.** The screening decisions, the shortlist, the
audit sample and the false-negative rate are all unchanged from the original run.

### Artifacts changed

`papers.csv`, `papers.md`, `transfer.csv`, `transfer.md`, `screening.csv` (tier and note fields
only), `paywalled.md`, `unreachable.md`, all ten report sections, and this file. `screened.csv`,
`triage.csv`, `queries.csv`, `shortlist.md`, `audit_sample.md` and `triage_stats.md` are
untouched.

One inconsistency was introduced and caught during the round rather than after it: the new
`transfer.md` blocks were first written with a `` `touchpoint` - `` label where the file's
convention is `**touchpoint.**`, and one `transfer.csv` row was left carrying four touchpoints
while its block evidenced eight. Both were found by a script that checks every declared
touchpoint against its own block, which now reports 0 unevidenced touchpoints across all 101
core blocks that declare any. `audit_tango.py` does not check this, which is why it was worth
checking by hand.

### What this round does not settle

Twelve demotions remain and `paywalled.md` still records what each would change. Four of them
are ChemRxiv and two SSRN — the same two hosts that caused most of the original losses, and
neither was resolved. Two core records are still read from a substitute whose identity is
inferred: `doi:10.3929/ethz-c-000801434`, where the hand-retrieved copy is the same arXiv
version and so verifies nothing, and `title:aspenplusmcp…`, still asserted by the repository
itself — though that system's evidence no longer rests on the repository alone now that its
preprint is read. One record is still proxy-read with tables unquotable
(`doi:10.20944/preprints202608.1323.v1`) and one still read from a laboratory deposit
(`doi:10.11578/dc.20260516.1`).

The divergence rate is the finding most likely to matter for a future run: **three of six
preprint-to-published pairs checked had changed in ways that altered a recorded field.** On a
sample of six that is not a rate anyone should extrapolate, but it is enough to say that
`IDENTITY MATCH IS INFERRED` in `papers.md` is a real caveat and not a formality.
