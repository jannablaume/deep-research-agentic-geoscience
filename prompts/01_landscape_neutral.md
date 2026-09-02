# 01 — What exists in agentic AI for geoscience

Version: v0.2
Output: `outputs/01_landscape/<version>/`, where `<version>` is this prompt's version string
(`v0.2`). If that directory already exists, create `v0.4-run2`, `v0.4-run3`, … and never
write into or over an existing one. Record the resolved output path as the first line of
`RUN.md`.

## Invariants

Copy this block verbatim into `RUN.md` at run start, and re-read this prompt file from disk
at every checkpoint. A long run is summarised and compacted repeatedly; a rule that is not
re-read stops being applied while the output continues to look complete.

1. Never exceed the web-call cap for the run mode. Log every call in `queries.csv`.
2. Nothing is counted, cited, or written unless a tool call **in this run** retrieved it.
   Never fill a count, a citation, or a CSV cell from recall.
3. Append to `queries.csv`, `screened.csv`, `papers.csv` and `papers.md` as you go, never
   only at the end.
4. Every substantive claim in the prose carries `[Certain]`, `[Likely]` or
   `[Absent-searched]`.
5. Verify every citation resolves before use; route failures to `unreachable_urls.md` or
   `access_restricted.md`.
6. Never write into or over an earlier run's output directory.
7. Never spend a web call solely to store an abstract.
8. Finish by answering the Self-audit table from the files, and report failures as failures.

## How to read this prompt

This prompt is long, and long prompts fail by drift rather than by disagreement: no rule is
ever rejected, they just stop being applied as the run is summarised, while the output goes
on looking complete. Two things counter that, and both are obligations, not suggestions.

**Re-read by section, not wholesale.** Read all of it once at run start. After that, re-read
only what the current step depends on:

| When | Re-read |
|---|---|
| Before each batch of searches | Search strategy, Stopping criterion |
| Before each pass 3 admission | Procedure, Maturity rating, the `papers.csv` columns |
| At each checkpoint | Invariants, Incrementally checkpoint |
| Before writing any prose | Synthesise do not summarise, Evidence rules, Report structure |
| Before finalising | Self-audit, Constraints |

**Then verify rather than assume.** The Self-audit section near the end converts every
invariant above into a check answered from the output files themselves. A rule that drifted
shows up there as a failed check instead of as a plausible-looking report.

## Goal

Map the existing research space of agentic AI in solid-earth and subsurface geoscience,
without injecting TANGO context or any research direction. Descriptive only: what has been
built, by whom, how it was evaluated, how mature it is. Gaps and research questions are
out of scope here — they belong to prompt 03.

## Run mode

State the mode in `RUN.md`. If the invocation does not specify one, run `test`.

| Mode | Web calls | Pass 1 unique screened | Pass 2 assessed | Pass 3 admitted | Quotas | Snowball | PDFs |
|---|---|---|---|---|---|---|---|
| `test` | ≤ 20 hard cap | whatever the 20 calls return | 4-6 | 3-4 | Suspended | None | Yes, for admits |
| `full` | ≤ 250 hard cap | ≥ 600 | 100-150 | 40-60 | All quotas below apply | Per snowball rule | Per PDF rule |

A **web call** is any tool call that reaches the network: a search, an abstract or
landing-page fetch, a full-text or PDF fetch, a Semantic Scholar or OpenAlex API call. The
cap counts them all together, including retries and calls that fail. Log every one in
`queries.csv` and report the running total in `RUN.md`. When the cap is reached, stop
searching and write up what you have. A run that stops at the cap and says so in `RUN.md`
is a successful run; a run that quietly exceeds it is not.

### What `test` mode is for

`test` mode must answer one question: **would the `full` run cover the landscape and
produce usable artifacts?** It answers it two ways at once, and the budget split is fixed.

- **Coverage probe — 15 of the 20 calls.** Breadth, not depth. Sample the subfield ×
  lineage cells per the test-mode probe plan in Search strategy step 1, and record the
  *yield per cell, including the zeros*. The zeros are the finding: a cell that returns
  nothing from a well-formed query is where the `full` run will fail its quota, and this
  probe is the only cheap way to learn that before the `full` budget is spent.
- **Mechanics slice — 5 of the 20 calls.** Take 3-4 candidates all the way through pass 2,
  pass 3, verification, extraction, PDF download and a `papers.csv` row, so that every
  artifact in the Constraints list exists with real content in it.

Every output file listed in Constraints is written in `test` mode, `coverage.md` and the
downloaded PDFs included. Small is fine; missing is not. `index.md` opens with a one-line
banner stating it is a coverage probe and not a landscape map, then carries only a short
section 1 and the go/no-go verdict from `coverage.md`. Do not write report sections 2, 3,
4, 7 or 8 in `test` mode — a synthesis of four sources is not a synthesis, and writing one
would disguise the probe as a landscape map.

Every verification, evidence, extraction and logging rule in this prompt applies unchanged
in both modes. Quotas, snowballing and the admission-order procedure do **not** apply in
`test` mode; the call cap replaces them.

## Prompt

You are conducting a **scoping review** of agentic AI in solid-earth and subsurface
geoscience: a review that maps the breadth of what exists, the methods used, and the
volume and type of evidence available. It is not a systematic review (no exhaustive
protocol) and not an argument for or against anything. Organise it **thematically**, not
chronologically and not source by source.

### Requester neutrality

- Do not personalise the report, do not adapt it to a presumed research agenda, and do not
  address the reader.
- Do not frame the report around, or give privileged treatment to, any specific project,
  research group, or author, including the requester's.
- Do not exclude a source because of who wrote it. If a source authored by the requester
  survives to pass 3, admit it on exactly the same criteria as any other and note in
  `RUN.md` that it was assessed unchanged. Suppressing it would bias the map as much as
  privileging it would.
- Do not treat any subfield, method family, or research group as the reference point
  against which others are compared.

### Scope

- **Domain**: geophysics, solid-earth and subsurface geoscience. The subfields below are
  the reporting buckets: each admitted source is assigned exactly one, and each gets one
  subsection in the report.
  1. rock mechanics and geomechanics
  2. seismology and induced seismicity
  3. hydrogeology and groundwater
  4. reservoir engineering (petroleum)
  5. geothermal
  6. CCS
  7. mining
  8. engineering geology
  9. subsurface characterisation and geophysical inversion
  10. geological modelling

  Where a source spans several buckets, assign it to the one its **evaluation** is set in,
  not the one its introduction invokes, and record the alternative in
  `subfield_secondary`. Since quotas and caps are computed from `subfield`, this rule is
  what keeps them meaningful.
- **Out of scope, by decision, not by accident**: atmospheric, ocean and climate science;
  planetary geoscience; Earth observation and satellite remote sensing; geodesy, GNSS and
  InSAR; geochemistry and geochronology; palaeoclimate. Most agentic-AI-in-geoscience work
  by volume sits in Earth observation and climate, so admitting it would dominate the map
  and drown the subsurface signal this review is about. In `full` mode run exactly one
  probe query per excluded area, record the hit counts in `queries.csv`, admit nothing from
  them, and state in section 1 that these areas were excluded deliberately and roughly how
  much material the probes suggest sits there. A documented boundary is a scope decision;
  an undocumented one is indistinguishable from a hole in the search.
- **"Agentic AI"**: report the full range, and keep the two lineages visibly separate.
  1. *LLM-based agents*: tool use, planning and decomposition, memory, retrieval,
     code execution, multi-agent orchestration, human-in-the-loop autonomy.
  2. *Pre-LLM autonomous and multi-agent systems*: reinforcement-learning controllers,
     agent-based models, autonomous sensing and instrument networks, classical
     multi-agent systems and blackboard architectures.
  Where the literature disagrees on what counts as "agentic", report the competing
  definitions and who holds them instead of picking one.
- **Time**: the two lineages have different windows, because lineage 2 predates the term.
  - Lineage 1 (LLM-based): end of 2022 to the run date.
  - Lineage 2 (pre-LLM): 2010 onward, with no lower bound for foundational architectures
    (blackboard systems, early expert and multi-agent systems) where a source is still
    the canonical reference for a design that later work builds on.
  Do not apply the lineage 1 window to lineage 2 searches — they are different searches
  with different vocabularies, not one search run twice.
- **Language**: search in English. In `full` mode only, additionally run exactly 6 Chinese
  queries — 3 lineage 1, 3 lineage 2 — against the subfield terms that yielded most in
  English, counted against the web-call cap. Run none in `test` mode: the Chinese track
  cannot be evaluated on a 20-call budget and would consume a third of it. Record the
  language of each admitted source in `language`.
  - Extracts from a non-English source go into `papers.md` verbatim in the original
    language, immediately followed by an English translation on the next line, labelled
    `[translation]`. The verbatim rule is not satisfied by a translation alone.
  - Where a Chinese-language index (CNKI, Wanfang) is not reachable without a
    subscription, log the attempt in `access_restricted.md` and say so in `RUN.md`. Do not
    substitute English-language surveys *about* Chinese work and record them as
    Chinese-language sources.

### Thin sections

A thin section — for any subfield, lineage, or language — is either a true finding about
the field or a failure of your search, and the two are indistinguishable in the output
unless you log the difference. The logged query list required under "Absence claims" is
what distinguishes them. Do not assume in either direction, for either lineage, and do not
inflate a section to make it look searched.

### Budget

Three separate budgets, per the run mode table above. Do not collapse them into one number.

| Stage | Meaning |
|---|---|
| Pass 1 — screened | Titles/abstracts inspected. Does not count against citation budget |
| Pass 2 — assessed | Methodology skimmed |
| Pass 3 — admitted | Deep-read, extracted, citable, one row in `papers.csv` |

In `full` mode, admitted is a **target range, not a ceiling**, and fewer than 40 admitted
sources is a failed run that must be reported as such in `RUN.md` with the reason — unless
the web-call cap was reached first, in which case record the shortfall against the calls
spent and treat it as a budget finding for the next version. In `test` mode 3-4 admits is
the target and also the ceiling: admitting more spends the mechanics slice's budget on
depth the probe does not need.

Every item counted in pass 1, 2, or 3 must originate from an actual search, fetch, or
snowball tool call made during this run. Do not enumerate candidate papers from training
knowledge to fill the screening count — if you recall a paper that seems relevant, you
must still locate and fetch it before it counts as screened.

**Screened means unique.** Deduplicate at pass 1 on the identity key (DOI, else arXiv ID,
else normalised URL) before counting. A source returned by six queries is one screened
item, not six. Report `screened_total` and `screened_unique` separately in `RUN.md`; the
budget is on `screened_unique`.

#### The screened set is an output, not scratch

Every unique item reaching pass 1 gets a row in `screened.csv` and its abstract stored,
whether or not it survives. This is the difference between a run that can be built on and a
run that has to be repeated. With `screened.csv` and `abstracts/`, a later version of this
prompt can widen the scope, change the subfield taxonomy, or re-triage under new criteria
without re-issuing a single query. Without them the several hundred items screened and cut
— roughly 90% of everything the search touched — are discarded at the moment they are
produced, and any change of criteria forces the whole run again.

- `screened.csv`, one row per unique screened item, RFC 4180, under the same CSV hygiene
  rules as `papers.csv` below. Columns: `identity_key` (DOI, else arXiv ID, else normalised
  URL), `title`, `authors`, `year`, `venue`, `first_query` (the `query_id` from
  `queries.csv` that first returned it), `n_queries_returning`, `subfield_guess`,
  `lineage_guess`, `highest_pass` (1 / 2 / 3), `cut_reason` (`admitted` where it survived
  to pass 3), `abstract_stored` (full / snippet-only / no).
- `abstracts/<identity_key>.md` — the abstract **as retrieved, verbatim**, one file per
  screened item, with the source URL and how it was obtained on the first line. Sanitize
  `/` in DOIs to `_`.

  **Never spend a web call solely to fill this file.** Storing abstracts is worth doing
  only because the screening step already put the text in front of you; fetching 600
  abstracts to populate a directory would consume the entire `full` cap twice over and is
  the opposite of the intent. Write whatever screening already returned, and record which
  in `abstract_stored`:
  - `full` — a complete abstract was in the search result, or on a landing page fetched
    anyway.
  - `snippet-only` — only the index's truncated snippet was available. Store it, marked
    truncated. A snippet still supports re-triage against a changed taxonomy, which is what
    this directory is for.
  - `no` — nothing usable was returned. Write no file.

  Never reconstruct or complete an abstract from recall: a fabricated abstract here poisons
  every later run that trusts this directory. Where a full text is fetched anyway at pass 2
  or 3, upgrade the file to the real abstract at that point, since the call is already
  being spent.
- `queries.csv`, one row per web call, appended before you act on the result. Columns:
  `query_id` (sequential integer), `mode`, `stage` (seed / probe / snowball / venue /
  fetch / verify / out-of-scope-probe), `query_or_url`, `index_searched`, `lineage`,
  `subfield`, `n_results`, `n_new_unique`, `status` (ok / error / rate-limited / paywalled),
  `notes`. This is the audit trail behind every absence claim, and it is what lets the next
  version skip re-running the phrasings that yielded nothing.

#### Quotas (`full` mode)

Attempt each quota. Where one cannot be filled after genuine search, record it in
`RUN.md` as unfilled with the queries tried — an unfilled quota is a reportable outcome,
not a failure to hide.

- **By lineage**: at least 10 admitted sources in lineage 2. Lineage 1 will usually return
  more hits per query; this quota exists so that lineage 2 is searched with equal effort,
  not so that it reaches a predetermined size.
- **By subfield**: attempt at least 3 admitted sources in each of the 10 subfields above.
  Where fewer than 3 exist, say so and state how hard you looked.
- **By source type**: at least 10 admitted sources that are *not* peer-reviewed papers or
  preprints, composed of at least:
  - 4 industry or operator sources (operator reports, SPE/OnePetro technical papers,
    vendor technical documentation, consortium deliverables),
  - 3 regulatory, standards, or geological-survey sources (e.g. USGS, BGS, IEAGHG,
    ISO/ASTM, permitting or licensing guidance),
  - the remainder code repositories or technical whitepapers.

  The split matters because report section 8 draws on this quota, and code repositories
  carry almost no stakeholder framing. Ten repositories would meet a bare count and leave
  section 8 unwritable.
- **Cap**: no single subfield may exceed 20% of admitted sources.

Feasibility check, so you can verify the quotas are jointly satisfiable before starting:
10 subfields × 3 = 30 admits as a floor against a 40-60 target, leaving 10-30 slots for
depth; the lineage and source-type quotas are satisfied by sources that also count toward
their subfield, so they do not add to the floor; the 20% cap allows 8-12 per subfield. If
you find these constraints in conflict during the run, stop and record the conflict in
`RUN.md` rather than silently dropping one.

#### Selection within a quota

Where more candidates survive pass 2 than the budget allows, prefer the most
methodologically detailed, then the most-cited, selected regardless of their stance.
Never fill a subfield quota by admitting a weaker source from an over-represented
subfield.

#### Admission order

Quotas are global but admission is sequential, so first-come admission will spend the
budget on whichever subfield you searched first and leave the later subfields unfillable.
Therefore:

1. Complete pass 1 and pass 2 for **all** subfields and both lineages, using the full seed
   set per subfield, before admitting anything at pass 3. Hold pass-2 survivors in a
   candidate list in `RUN.md`.
2. Then admit in two rounds: first the reserved floor (up to 3 per subfield, and the
   lineage and source-type minimums), then the remaining slots by the selection rule
   above.

If you must admit incrementally instead — e.g. the run is at risk of stopping early —
reserve slots explicitly: never let a subfield exceed 3 admits until every subfield has
been searched with its full seed set.

### Incrementally checkpoint

Write all four of these as you go, never only at the end. A long run is stopped by context
limits, rate limits and errors far more often than it is stopped by finishing.

- `queries.csv` — append the row the moment a web call returns, before acting on it.
- `screened.csv` and `abstracts/` — append the row and write the abstract file as each
  unique item is screened.
- `papers.csv` — append a row as each source is admitted. Write the header row exactly
  once, when the file is created. Before appending, check the existing rows for the
  source's identity key so a resumed run cannot duplicate a row.
- `papers.md` — write the source's extract block **in the same step as its `papers.csv`
  row**, never in a separate later pass. The extracts require the full text to be in front
  of you, so they are the most expensive thing the run produces. A run that dies with the
  CSV written and the extracts missing has kept the cheap half and lost the expensive half,
  and the prose cannot be written from CSV cells.

Update `RUN.md` with running totals — web calls used against the cap, screened
unique/assessed/admitted, per lineage and subfield — every ~100 screened items in `full`
mode, and after every 5 web calls in `test` mode.

**At every checkpoint, re-read this prompt file from disk before continuing.** This run
will be summarised and compacted several times over its length, and a rule that is not
re-read stops being applied while the output still looks complete — a silently dropped
verification rule at 40% costs the entire run. Re-reading costs a few thousand tokens and
is the cheapest insurance here. Re-read the Invariants block into `RUN.md` if it has
drifted.

If the run must stop before reaching budget, `RUN.md` must record exactly where it stopped
— last query run, last source in progress, current candidate list, web calls used — so it
can resume rather than restart.

### Search strategy

1. **Seed.** Run broad queries per concept, several independent phrasings each, using at
   minimum the term families below. Treat these as starting points, not a closed list.
   - *Lineage 1*: agentic AI, LLM agent, autonomous agent, tool use / function calling,
     ReAct, planning and decomposition, multi-agent LLM, retrieval-augmented generation,
     copilot / assistant, AI scientist, autonomous experimentation — each crossed with
     each subfield term (geophysics, seismology, inversion, reservoir, geothermal, CCS,
     geomechanics, borehole, geological modelling, well log, mining, engineering geology,
     hydrogeology).
   - *Lineage 2*: multi-agent system, agent-based model, intelligent agent, blackboard
     architecture, expert system, deep reinforcement learning control, closed-loop
     reservoir management, well placement optimisation, adaptive/autonomous sampling,
     AUV or robotic survey planning, autonomous seismic network, sensor network
     self-organisation — crossed with the same subfield terms. These share almost no
     vocabulary with lineage 1; querying "agentic" will not find them.

   **A query family is one term family from the two lists above** — "multi-agent LLM",
   "blackboard architecture" — and *not* a term × subfield pair. There are 11 lineage 1
   families and 12 lineage 2 families, 23 in total. Fix this reading before starting: the
   stopping criterion and the absence rule below are both stated per family, and read as
   term × subfield they would mandate well over 1,500 searches, which no budget in this
   prompt can pay for.

   **Seed budget, `full` mode.** Of the 250 web calls: at most 120 on seed queries, at most
   60 on snowballing, at most 40 on full-text and PDF fetches, 30 held in reserve for
   verification, re-fetches and the out-of-scope probes. Cross each family with subfield
   terms *selectively*, not exhaustively — open with 2-3 subfields per family, and widen
   only a family that is still returning new unique items. Record the running spend per
   bucket in `RUN.md`.

   **Screening rides on the search calls; it does not add to them.** One search returning
   10-20 hits screens 10-20 items for one call, and that ratio is the only arithmetic under
   which ≥600 screened fits inside 120 seed calls. Never fetch an item individually in
   order to screen it. Where the search tool returns results without abstracts, screening
   for those items is title-level: accept that, mark them `abstract_stored: no`, and record
   in `RUN.md` how many were screened on title alone — it bears directly on how far the
   pass 1 cut reasons can be trusted.

   **Test-mode probe plan — the 15 coverage calls.** Do not attempt the seed set; it does
   not fit and attempting it produces 15 lineage-1 queries and no map.
   - **10 calls**: one query per subfield, alternating lineage so each lineage gets 5
     subfields, using that lineage's strongest term for that subfield.
   - **3 calls**: the three subfields you expect to be thinnest, queried in the *other*
     lineage, so the probe holds at least one lineage-1 versus lineage-2 comparison in a
     cell where coverage is doubtful.
   - **2 calls**: direct venue search — arXiv (`physics.geo-ph`, `cs.MA`) and one
     industry index such as OnePetro — to establish whether venue-direct search is
     reachable at all before the `full` run depends on it.

   Record every one of the 20 subfield × lineage cells in `coverage.md`: the query run, the
   number of results, the number on-topic by title, and for cells you did not query, the
   literal word `unprobed`. **An unprobed cell is not an empty cell**, and neither
   `coverage.md` nor `index.md` may present it as one.
2. **Snowball.** For every source admitted at pass 3, chase citations in both directions,
   and run at least two rounds. Use Semantic Scholar (semanticscholar.org/api) or OpenAlex
   (api.openalex.org) for forward citations and citation counts; backward snowballing can
   use the source document itself.
   - **Not run in `test` mode at all.** Two rounds over even 20 admits is roughly 1,600
     candidate touches — the entire `full` search budget spent inside what is supposed to
     be a cheap probe. `test` mode makes no snowball calls and records snowballing as
     untested in `RUN.md`, so the `full` run's first snowball round is also its first
     check of this mechanism. Budget for that.
   - Bound it: backward = scan the full reference list at title level; forward = the top 20
     citing works by citation count. Without a bound, two full rounds over 40-60 admits is
     tens of thousands of candidate touches. Stop when the 60-call snowball budget is spent
     and record how many admits went unsnowballed.
   - If an API returns an error, is rate-limited, or requires a key you do not have, log
     the failure in `RUN.md` under the affected source. A snowball round that silently did
     not happen is the single easiest way for this run to look complete while being
     shallow. Do not substitute recalled citations for a failed API call.
   - Record in `RUN.md` how many admitted sources came from queries versus snowballing.
     `found_via` records **first touch** — the route by which the source first entered the
     screened set, not every route that later returned it.
3. **Search named venues and indexes directly**, not only via general web search:
   arXiv (`cs.AI`, `cs.MA`, `cs.CL`, `physics.geo-ph`), Computers & Geosciences,
   Geoenergy Science and Engineering, Geothermics, Geophysics (SEG), Geophysical Journal
   International, Seismological Research Letters, JGR Solid Earth, Water Resources
   Research, International Journal of Greenhouse Gas Control, Rock Mechanics and Rock
   Engineering, IJRMMS, IEEE TGRS, SPE/OnePetro, SEG/EAGE/AGU/EGU abstract archives,
   Stanford Geothermal Workshop proceedings, GitHub and Hugging Face, and the report
   series of operators, geological surveys and regulators (e.g. USGS, BGS, IEAGHG).
   Several of these are subscription-only. Expect abstract-only access to be common in the
   industry-facing venues, and handle it per the access rule in Procedure step 4 — do not
   quietly drop a whole venue because its full texts are unreachable.
4. **Absence claims require evidence of search.** Before writing that a subfield or
   concept has nothing, you must have run at least five distinct query phrasings for it
   *and* one snowball check from an adjacent admitted source. Cite the `query_id`s from
   `queries.csv` next to the absence claim. An absence not backed by logged `query_id`s is
   a search failure, not a finding, and must be labelled as such.
   **No absence claim may be made in `test` mode.** A single probe query per cell cannot
   distinguish an empty field from a badly phrased query, so a zero-yield cell in
   `coverage.md` is reported as `0 hits from 1 query`, never as "nothing exists".

### Stopping criterion

Applies in `full` mode only; in `test` mode the probe plan replaces it.

Stop expanding a query family — as defined in Search strategy step 1, 23 of them — once
three consecutive new phrasings return no new candidates, but never before five distinct
phrasings have been run for that family, so that stopping never blocks the absence claim in
Search strategy step 4. Log both the phrasings and the stop point in `queries.csv`, and the
stop point per family in `RUN.md`.

Five phrasings × 23 families is 115 of the 120 seed calls, so the floor and the seed budget
only just coexist. If honouring the floor for the remaining families would breach the seed
budget, stop, record in `RUN.md` which families went unprobed or underprobed, and make no
absence claim for those. Running out of budget is a reportable outcome; an absence claim
made on three phrasings is not.

### Procedure

1. **Triage in three passes.** Do not read anything end to end before it has earned it.
   - *Pass 1 — relevance*: **title and abstract only**, from the search result or the
     landing page. Do not fetch a full text at pass 1 — that is what pass 2 is for, and
     fetching at pass 1 is how a screening budget becomes a reading budget. Decide only
     whether the source is on-topic per the scope above. Most candidates are cut here.
     Log pass 1 **per item** — one `screened.csv` row and one `abstracts/` file each, with
     the `cut_reason` — and additionally roll the counts up per query family and per cut
     reason in `RUN.md`. The rollup is the summary; the rows are the database, and only
     the rows survive a change of criteria.
   - *Pass 2 — methodology*: skim methods, figures, and tables. Ask whether the study is
     designed so its findings are credible and **comparable to the others** — the same
     question you will answer in the `papers.csv` columns. Log every pass 2 cut
     individually, with the reason.
   - *Pass 3 — deep read*: only for survivors. Read discussion, limitations, and stated
     future work in full. Authors state the weaknesses of their own systems here, and
     that is the most reliable evidence you will get about maturity and about what was
     *not* demonstrated.
   Only sources that reach pass 3 may be cited in `index.md`. For non-paper sources
   (code repositories, industry or policy documents) apply the analogous three passes:
   README or landing page, then documentation and code structure, then full read.
2. **Deduplicate on system, not on source.** Assign every admitted source a `system_id`.
   Where one group publishes several papers on one system, they share a `system_id`. Use
   DOI or arXiv ID as the source identity key where one exists, URL otherwise, so preprint
   and published versions of the same work collapse to one row.
   - Many sources — most of lineage 2 — describe a method or a study, not a named system.
     For those, set `system_named` to `no` and mint `system_id` as
     `<firstauthor><year>-<short-method-slug>`. Do not invent a product name.
   - All counts, maturity distributions and "what exists" statements in the prose are
     **per system**; `papers.csv` stays one row per source. Report both totals in `RUN.md`.
   - Where sources sharing a `system_id` differ in demonstrated maturity, the **system's**
     maturity is the highest `maturity_demonstrated` among them, and `RUN.md` records which
     `source_id` supplied it. Note in section 6 how many systems have a lower-maturity
     earlier source, since that is what an incremental research programme looks like.
   - Because `system_named` is usually `no` for lineage 2 and usually `yes` for lineage 1,
     per-system counts are not directly comparable across the two lineages. State this
     wherever you compare them.
3. **Handle author-stated limitations as evidence, not as your own conclusions.** Record
   them in the `papers.csv` column for it, and use them in the evaluation and maturity
   sections as attributed statements ("the authors report that X was not tested on field
   data").
4. **Verify every citation before use.** Confirm the identifier resolves, the title and
   authors are as you state them, and the source actually contains the claim you
   attribute to it. Working from the document text lowers the risk of invention but does
   not remove it, so verify regardless. Never cite from memory or reconstruct a
   plausible-looking reference.
   Route failures to exactly one of two files — the distinction is whether the source
   *exists*:
   - `unreachable_urls.md` — the identifier or URL does not resolve, or verification
     failed: dead link, 404, title/authors not as stated, no evidence the source exists.
     These are not admitted and not counted at any pass.
   - `access_restricted.md` — the source is verified to exist but its full text is not
     reachable (paywall, login, subscription-only index). Record what *was* visible
     (abstract, landing page, figure captions) and the access barrier.

   A source with abstract-only access may be admitted, but set
   `access_status: abstract-only` and `maturity_demonstrated: not stated (abstract only)`.
   Never rate maturity from an abstract as though it were the full text. If the abstract
   cannot support the required `papers.csv` fields at all, do not admit it — send it to
   `access_restricted.md`.
   Count `access_status: abstract-only` per subfield in `RUN.md`. The industry-facing
   subfields will accumulate these disproportionately, which depresses their apparent
   maturity for reasons that have nothing to do with the field. Section 6 must state these
   counts alongside the maturity distribution so the distribution is not read as a finding
   about maturity when it is a finding about access.
5. **Extract before writing.** For each admitted source, quote verbatim the sentences
   stating what was built, how it was evaluated, and what it achieved. Put those extracts
   in `papers.md`. Write the report from those extracts only.
6. **Build the comparison grid** (`papers.csv`) before writing prose, so the prose is
   written from a comparable grid rather than from reading order.
7. **Self-critique in `RUN.md`** before finalising: which subfields, stakeholder groups,
   or viewpoints are thin or absent, and whether that reflects the field or your search;
   which quotas went unfilled and why; query-versus-snowball yield; how many admits were
   abstract-only; web calls spent per budget bucket against the caps in Search strategy
   step 1, and which bucket ran out first; what to change in the next prompt version.

### Maturity rating

Rate `maturity_demonstrated` from what the **evaluation section demonstrates**, never from
claims in the abstract or introduction.

Set `maturity_claimed` from the strongest maturity assertion the source makes about itself
in its abstract, introduction, or conclusion, and put the sentence you read it from in
`papers.md`. Where the source makes no such assertion, use `not stated` — do not infer a
claim from enthusiasm of tone.

The ordering axis is **what the evaluation data is and whether the system's output touched
reality** — not how rigorous the evaluation was. Rigour is recorded separately, in
`baseline` and `held_out`, so that a careful synthetic study is not promoted above a sloppy
field trial.

| Level | Criterion |
|---|---|
| M0 concept | Position or architecture paper, no working implementation |
| M1 toy demo | Implemented; evaluated only on synthetic or textbook-scale data |
| M2 benchmark prototype | Evaluated on a reusable, site-agnostic benchmark dataset — community or author-published — which may contain real observational data |
| M3 prototype on real data | Evaluated on real field or observational data from a named site, well, or campaign, retrospectively; not used operationally |
| M4 field trial | Outputs entered a real workflow or influenced a real decision; site or operator named; time-bounded |
| M5 production | In routine use beyond a trial, with evidence of sustained operation from a source other than the vendor's own marketing |

Tie-breaks, because M2 and M3 otherwise overlap and this is the boundary that decides
section 6:

- The M2/M3 split is **benchmark versus site**, not synthetic versus real. A phase picker
  evaluated on STEAD or INSTANCE is M2, even though those contain real waveforms, because
  the dataset is reusable and site-agnostic. The same picker evaluated on one named
  monitoring network's catalogue is M3.
- Where a source qualifies for both, rate M3 and set `benchmark_also: yes`.
- M3 requires the site, well, field, or campaign to be named or clearly identified.
  "Real field data" with no identification rates M2 at most.
- M4 requires evidence that an output was *used* — a decision, a workflow step, an
  operator action. A field dataset alone is M3.
- If the data source is not stated, rate no higher than M1 and record "not stated".

A gap between `maturity_claimed` and `maturity_demonstrated` is itself a finding; report
its frequency in section 6.

### Synthesise, do not summarise

The dominant failure mode of a review like this is serial summarising:

- Anchor every paragraph on a **concept**, and cite the several sources that bear on it.
  Not: "Author A built X. Author B built Y. Author C built Z."
  Instead: "Multi-agent designs are typically used to split simulation setup from
  interpretation (A; C), though single-agent tool-calling is reported as sufficient for
  narrower inversion tasks (B)."
- Every section must state where sources **agree** and where they **diverge**, or state
  that the evidence is too thin to tell.
- Nothing in the report should be a list of papers or a list of systems. `papers.csv` and
  `papers.md` hold the per-source detail; `index.md` holds ideas supported by sources.

### Evidence rules

- Tag every substantive claim with exactly one of three tags:
  - `[Certain]` — stated explicitly in a cited source.
  - `[Likely]` — inference across sources; must name the two or more sources it infers
    across.
  - `[Absent-searched]` — a statement that something was not found, backed by the logged
    query list required in Search strategy step 4. Statements that the evidence is too
    thin to tell also take this tag.

  If you cannot support a statement at one of these three levels, do not write it.
  Speculation belongs to prompt 03.
- Where consecutive sentences share the same tag and the same supporting sources, tag the
  paragraph once rather than every sentence. In a concept-anchored synthesis most claims
  are `[Likely]`, and per-sentence tagging bloats the prose into citation strings without
  adding provenance.
- If sources conflict, present both positions with their evidence. Do not adjudicate and
  do not average them into a consensus that no source states.
- If the retrieved material does not support a statement, say so rather than inferring it.
- Do not write gaps, opportunities, recommendations, or future work. Do not use
  promotional framing ("promising", "great potential", "revolutionise") or dismissive
  framing. Report what sources claim, attributed.

### Report structure

`full` mode only — in `test` mode `index.md` carries the banner, a short section 1 and the
`coverage.md` verdict, and nothing else.

`index.md`, in this order. The `full` report will exceed roughly 8000 words, so split it:
write `index_<n>_<section>.md` per section and reduce `index.md` to a table of contents.
Decide the split before drafting, not after.

1. **Executive summary** — what exists, at what maturity, where the evidence is thin.
   No recommendations.
2. **Agentic techniques** — planning, tool use, memory, retrieval, orchestration,
   human-in-the-loop, and their pre-LLM counterparts. What each is used for here.
3. **Architectures** — system designs: single-agent, multi-agent, hierarchical,
   pipeline-with-agent, agent-plus-simulator, agent-plus-physics-solver. Where sources
   describe the components, give a component list; no ASCII or rendered diagrams.
4. **Applications by subfield** — one subsection per subfield in Scope, including those
   where the search found nothing. Each subsection is a synthesis, not a roster; for
   absence, cite the logged queries per the Search strategy.
5. **Evaluation and benchmarks** — how systems were tested, against what baseline, on
   what data, and what was reported. Flag claims with no baseline or no held-out test.
   State whether any shared benchmark exists across systems, or whether every system
   defines its own.
6. **Maturity** — the *distribution* of demonstrated maturity across systems, what
   separates the systems that reached M3+ from those that did not, and how often
   `maturity_claimed` exceeds `maturity_demonstrated`. State the abstract-only counts per
   subfield from Procedure step 4 alongside the distribution, and the system-level
   aggregation rule from Procedure step 2. Per-system ratings live in `papers.csv`; do not
   restate them here as a list.
7. **Points of disagreement** — where authors contradict each other, and on what.
8. **Stakeholder views** — how framing and stated priorities differ between academic,
   industry/operator, and regulatory sources. Report as observed positions, not as truth.
   Draw primarily on the industry/operator and regulatory portions of the non-paper quota.

## Self-audit

Before finalising, in either mode, end `RUN.md` with this table. Answer every row **from
the output files themselves** — count the rows, parse the CSV, list the directory — never
from your memory of having done it. Memory of compliance is exactly what a compacted run
loses first.

| Check | How to verify | Result |
|---|---|---|
| Web calls within cap | count rows in `queries.csv` against the mode's cap | |
| Screened set complete | rows in `screened.csv` = `screened_unique` reported in `RUN.md` | |
| Admissions traceable | rows in `screened.csv` with `highest_pass` = 3 = rows in `papers.csv` | |
| Extracts complete | `source_id` headings in `papers.md` = rows in `papers.csv` | |
| Nothing from recall | every `papers.csv` `source_id` traces to a `query_id` in `queries.csv` | |
| Grid parses | parse `papers.csv` as RFC 4180; report row and column counts | |
| Claims tagged | count substantive claims in `index*.md` carrying no evidence tag; must be 0 | |
| Absence claims backed | every `[Absent-searched]` claim cites `query_id`s | |
| Files present | list the output directory against the Constraints list | |
| Nothing written outside the run directory | | |

Where a check fails, report it as failed with what caused it, and — if it is cheap and the
cap allows — fix the underlying artifact and re-run the check. **Never adjust a number so
that a check passes.** A failed check, found and reported, is this section working as
intended; a check quietly reconciled is the precise failure this section exists to catch,
and it leaves a run that is wrong and looks finished.

## Constraints

- Budgets and quotas as specified above, per run mode. Never collapse the three pass
  budgets into one number, and never let any of them override the web-call cap — the cap
  is the one hard limit in this prompt.
- Write every file into the output directory resolved at the top of this prompt. Never
  overwrite an earlier version or an earlier run.
- Required in the output directory, in **both** modes: `RUN.md`, `index.md` (plus its
  section files), `queries.csv`, `screened.csv`, `abstracts/`, `papers.csv`, `papers.md`
  (plus any split files), `pdfs/`, `unreachable_urls.md`, `access_restricted.md`. Create
  every one of them even if empty, with a line saying why it is empty. Additionally in
  `test` mode: `coverage.md`. `RUN.md` ends with the Self-audit table.
- `coverage.md` (`test` mode) is the run's primary deliverable and has three parts:
  1. **Yield table**, one row per subfield × lineage cell — all 20 rows, none omitted:
     `subfield`, `lineage`, `query_id`, `query text`, `n_results`, `n_on_topic_by_title`,
     or `unprobed`.
  2. **Projection**, per subfield: from the probe yield, the rough number of admits the
     `full` run should expect, and which subfields look unable to reach the 3-admit floor.
     State the arithmetic. A projection from one query is a rough indication, and must be
     labelled as one — this is an estimate, not a measurement.
  3. **Go/no-go verdict** on the `full` run, in these terms and no others: whether the
     artifact chain worked end to end on the 3-4 mechanics-slice sources (each file written,
     `papers.csv` parses, citations verified, PDFs downloaded); which subfield × lineage
     cells look too thin for the quota and what should change in the seed terms before the
     `full` run; whether the 250-call cap looks sufficient given the observed hits per
     query. If the verdict is no-go, say what to fix in prompt v0.5 rather than
     recommending the `full` run anyway.
- `papers.csv` is the comparison grid, one row per source, RFC 4180 CSV with a header row,
  with these columns: `source_id` (DOI or arXiv ID, URL if neither), `system_id`,
  `system_named` (yes / no), `url`, `title`, `authors`, `year`, `venue`, `source_type`
  (peer-reviewed / preprint / industry / regulatory / repo / whitepaper), `subfield`,
  `subfield_secondary`, `lineage` (llm / pre-llm), `agentic_techniques`, `architecture`,
  `evaluation_method`, `baseline`, `held_out` (yes / no / not stated), `data_type`
  (synthetic / benchmark / real-field / not stated), `benchmark_also` (yes / no),
  `reported_result`, `maturity_claimed`, `maturity_demonstrated`,
  `author_stated_limitations`, `code_availability`, `language`, `access_status` (full-text
  / abstract-only), `found_via` (query / snowball / venue-search). Use `not stated` where a
  source is silent — never infer a value to fill a cell.
- CSV hygiene, since several columns hold prose: quote **every** cell, escape internal
  double quotes by doubling them, and replace any newline inside a cell with `; `. A
  `papers.csv` that does not parse is a failed run — verify it parses before finalising.
- `papers.md` holds, per admitted source, the verbatim extracts from procedure step 5
  under a `source_id` heading, plus the `maturity_claimed` sentence from the Maturity
  rating section. It is the evidence trail for the prose, not a summary. If it exceeds
  roughly 8000 words, split it into `papers_<subfield>.md` files (one per Scope subfield,
  lineage-2 sources grouped separately per subfield if a subfield has both), with
  `papers.md` reduced to an index of `source_id` → file pointers, mirroring the
  `index_<n>_<section>.md` split rule above.
- PDFs are not committed to git (`*.pdf` is gitignored) and are not uploaded to GCS by this
  prompt. In **both** modes, where a PDF is legitimately downloadable (open access,
  preprint server, industry/regulator report), save it to
  `outputs/01_landscape/<version>/pdfs/<source_id>.pdf`, using the same `source_id` as the
  matching `papers.csv` row (sanitize `/` in DOIs to `_`). Each download counts as a web
  call against the cap. In `test` mode this applies to the 3-4 admitted sources, and
  downloading them is part of what the mechanics slice is testing — a `pdfs/` directory
  that is empty at the end of a `test` run is a failed mechanics check, not a saving. Do
  not fabricate or fetch a PDF for a source you could not actually access — if only an
  abstract or landing page was reachable, leave no file and note it in
  `access_restricted.md` instead.
