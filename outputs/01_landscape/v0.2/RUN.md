outputs/01_landscape/v0.2/

# RUN.md — 01_landscape_neutral, test mode

Mode: `test`
Prompt version used: v0.2 (as currently on disk in `prompts/01_landscape_neutral.md`, working
tree). Note on versioning: this working copy is internally inconsistent — the Version line
was locally edited from v0.4 to v0.2 (uncommitted change against the last commit, `e2262db`,
titled "01_landscape_neutral v0.4") but the file's own "create `v0.4-run2`, `v0.4-run3`"
resume instruction was left unchanged, pointing at the wrong version string. The user was
asked directly and confirmed: treat v0.2, as currently on disk, as authoritative for this run.
Recorded here for auditability; not fixed in the prompt file itself, since that was not asked.
Run date: 2026-09-02

## Invariants (copied verbatim at run start, per instruction)

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

## Mode

`test`. Web-call cap: 20 (hard) — **reached exactly** (see `queries.csv`, 20 rows). Intended
budget split: 15 coverage-probe calls, 5 mechanics-slice calls; actual split matched this
exactly. No snowballing attempted (untested this run, as the mode requires). No Chinese-language
queries (test mode runs none). No quotas applied (suspended in test mode).

## Web call log (running totals, per the every-5-calls checkpoint rule)

- After call 5 (queries 1-5, subfield probes 1-1 rock mechanics, 2 seismology, 3 hydrogeology,
  4 reservoir engineering, 5 geothermal): 5/20 calls used. Screened unique so far: 31.
- After call 10 (queries 6-10, subfield probes 6 CCS, 7 mining, 8 engineering geology,
  9 subsurface characterisation, 10 geological modelling): 10/20 calls used. Screened unique
  so far: 66. Notable: queries 7 and 8 each returned 0 on-topic-by-title results.
- After call 15 (queries 11-13, thin-subfield other-lineage probes; queries 14-15, venue-direct
  arXiv and OnePetro): 15/20 calls used (coverage probe complete). Screened unique: 92 (after a
  count-reconciliation fix — see Self-critique).
- After call 20 (queries 16-20, mechanics slice: 3 full-text fetches + 2 PDF downloads):
  20/20 calls used (cap reached exactly). Admitted: 3 (target for test mode was 3-4).

## Screened / assessed / admitted totals

- `screened_total` (raw hits across all 15 coverage-probe search calls, before dedup): 117
  (sum of `n_results` for query_id 1-15 in `queries.csv`, verified programmatically).
- `screened_unique`: 92 (rows in `screened.csv`; matches the count check below).
- Assessed (pass 2 — methodology skimmed): 3 (the mechanics-slice candidates; test mode's
  4-6 pass-2 target does not apply — the mode table's "4-6" figure is for `full` mode; `test`
  mode's own description caps pass-2/3 work at the 3-4 mechanics-slice candidates only).
- Admitted (pass 3): 3, within the test-mode target/ceiling of 3-4.
- Per subfield among the 3 admits: hydrogeology (1), subsurface characterisation and
  geophysical inversion (1), CCS (1).
- Per lineage among the 3 admits: llm (2), pre-llm (1).
- Abstract-only admits: 1 of 3 (the CCS admit, arxiv:2508.11618 — not a paywall; a fetch-tool
  extraction failure on an open-access PDF, documented in `papers.md` and below).
- System-level vs source-level: all 3 admits are `system_named: yes` except the CCS admit
  (`system_named: no`, minted as `co2-markov-game-chen-hosseini-2026`). 3 systems, 3 sources —
  no system had more than one admitted source this run.

## Mechanics-slice notes (what the 5-call slice was for)

Candidates: A = AQUAH (arXiv:2508.02936, hydrogeology, llm), B = CO2 storage Markov-game
(arXiv:2508.11618, CCS, pre-llm), D = GeoMind (arXiv:2604.21501, subsurface characterisation,
llm). (Label "C" was reserved for a fourth candidate, the Multi-Asset Closed-Loop Reservoir
Management DRL paper, but it was never fetched — see Self-critique's bookkeeping-error entry.)

- Calls 16-18: `WebFetch` on the raw arXiv PDF URL for each candidate. Result: call 16 (AQUAH)
  **failed outright** — "maxContentLength size of 10485760 exceeded" — no content returned at
  all. Call 17 (GeoMind) returned title, authors, and date correctly but reported the body
  text as inaccessible ("binary encoding of the full paper text... cannot be extracted").
  Call 18 (CO2 paper) similarly returned title, authors, and section headings but not body
  text.
- Calls 19-20: retried AQUAH and GeoMind via `arxiv.org/html/<id>` instead of
  `arxiv.org/pdf/<id>`. Both succeeded cleanly and yielded full verbatim extraction (see
  `papers.md`). The cap was reached before a third HTML retry could be spent on the CO2 paper,
  which therefore remains at `access_status: abstract-only` with most `papers.csv` fields
  `not stated`.
- PDF files for `pdfs/`: the `WebFetch` tool itself saves a local copy of any PDF it
  successfully retrieves as a side effect of the fetch. The GeoMind (call 17) and CO2-paper
  (call 18) local copies were verified (via each PDF's embedded `/Title` metadata, not
  filename or recall) and copied into `pdfs/` using a local `cp` — not a network call, so not
  counted against the cap. AQUAH has no PDF in `pdfs/`: its only successful fetch was the HTML
  route (call 19), which does not produce a savable PDF binary, and no further call was
  available within the cap to retry its raw PDF fetch a second time.
- **Finding, not just a note**: this is the run's clearest actionable result for `full` mode.
  A budget of 1 fetch call per admitted source for full-text reading is not realistic against
  `WebFetch`'s behavior on arXiv PDFs; see the recommendation in `coverage.md` section 3.

## Self-critique

- **Which subfields/cells are thin, and whether that reflects the field or the search**: see
  `coverage.md` section 2 in full. In summary: subfield 9 (subsurface characterisation and
  geophysical inversion) x lineage 2 has no signal at all in this run — genuinely unknown
  whether that is a search-vocabulary problem (most likely, since "geophysical inversion"
  strongly attracts classical-algorithm literature that pre-LLM agent/RL/ABM terms don't
  intersect with) or a real gap; the `full` run must fix the vocabulary before trusting either
  answer. Subfield 7 (mining) x lineage 1 and subfield 8 (engineering geology) x lineage 2 both
  returned zero on-topic hits under the phrasing tried, for identifiable and fixable reasons
  (keyword collisions and overly generic architecture terms respectively) — these read as
  search failures, not field findings, and are reported as such per the Thin sections rule.
  No `[Absent-searched]` claim is made about any of them, consistent with the test-mode rule
  that a single-query probe cannot support one.
- **Query-versus-snowball yield**: not applicable — snowballing is not run in `test` mode.
  All 92 screened items and all 3 admits came from `query` (`found_via` column), none from
  `snowball` or `venue-search` as a first touch (the 2 venue-direct queries did surface new
  items, but `found_via` in `papers.csv`/`screened.csv` records first touch, and none of the
  92 screened items had a venue-direct query as their *first* touch — all had already appeared,
  or would have appeared, via the subfield-probe queries that ran earlier in sequence... except
  where a venue query genuinely introduced new material with no prior subfield-probe overlap,
  which did happen for several OnePetro results; those are recorded with `first_query: 15` in
  `screened.csv`, which is the accurate provenance record regardless of how `found_via` is
  labeled in the smaller `papers.csv` table).
- **Abstract-only admits**: 1 of 3 (33%). This is a small-n test-mode number and should not be
  read as a `full`-mode projection; it does, however, matter for the mechanics-chain finding
  above, since this particular abstract-only case was caused by a tool limitation rather than
  genuine access restriction — a distinction `full` mode will need to keep making carefully,
  since the two require different fixes (retry the fetch route vs. accept the paywall and move
  on).
- **Web calls spent per budget bucket against the caps**: test mode has no separate sub-caps
  beyond the overall 20-call hard cap; the intended 15/5 split (coverage probe / mechanics
  slice) was followed exactly and both "ran out" simultaneously at the point the hard cap was
  reached, which was the intended design of this mode, not a shortfall.
- **What to change in the next prompt version**: (1) the three seed-vocabulary fixes and the
  fetch-budget adjustment listed in `coverage.md` section 3; (2) resolve the prompt file's own
  version-line inconsistency (Version: v0.2 vs. the "create v0.4-run2" resume instruction)
  before the next run, so a future run does not have to stop and ask the user which version is
  authoritative.
- **Bookkeeping-error entries, found and corrected during this run** (per the instruction to
  report failures as failures rather than quietly reconcile them):
  1. While compiling `screened.csv` from the 15 raw query results, one item from query 6
     (arXiv:2605.02405, "Closed-Loop CO2 Storage Control With History-Based Reinforcement
     Learning and Latent Model-Based Adaptation" — a real, distinct, on-topic paper) was
     omitted on first pass. Found during a systematic reconciliation of each query's raw hit
     count against `screened.csv`'s `first_query` tally (run after all 15 coverage-probe
     queries were logged, before the mechanics slice began). Corrected: row added to
     `screened.csv`, `n_new_unique` for query 6 corrected from 6 to 7 in `queries.csv`, and
     `screened_unique` recomputed from the corrected file (92, not the originally-tallied 91).
     No other query's reconciliation found a discrepancy (all other 14 queries' raw-link
     counts and `screened.csv` `first_query` tallies matched on the first check).
  2. A more serious near-error: `doi_10.1007_s10596-023-10255-w` ("Multi-Asset Closed-Loop
     Reservoir Management Using Deep Reinforcement Learning") was initially marked in
     `screened.csv` as `highest_pass: 3`, `cut_reason: "admitted; mechanics-slice candidate
     C"`, `abstract_stored: full` — before it had actually been fetched. This was caught
     before any `query_id` was logged for it and before it was written into `papers.csv` or
     `papers.md`, by checking that every intended pass-3 admission actually had a
     corresponding fetch call logged. It was corrected back to `highest_pass: 1` with an
     accurate `cut_reason` noting the correction. This is exactly the failure mode Invariant 2
     exists to catch ("nothing is counted, cited, or written unless a tool call in this run
     retrieved it"), and it is reported here rather than silently fixed, per Invariant 8 and
     the Self-audit section's instruction to report failures as failures. **No such item
     reached `papers.csv` or `papers.md`** — the error was confined to `screened.csv` and was
     corrected before propagating.

## Self-audit

| Check | How to verify | Result |
|---|---|---|
| Web calls within cap | count rows in `queries.csv` against the mode's cap | **Pass.** 20 rows in `queries.csv`; cap is 20. Reached exactly, not exceeded. |
| Screened set complete | rows in `screened.csv` = `screened_unique` reported in `RUN.md` | **Pass.** 92 rows in `screened.csv` (verified by parsing the file), matches `screened_unique: 92` reported above. |
| Admissions traceable | rows in `screened.csv` with `highest_pass` = 3 = rows in `papers.csv` | **Pass.** 3 rows with `highest_pass=3` in `screened.csv` (`arxiv_2508.02936`, `arxiv_2508.11618`, `arxiv_2604.21501`); 3 rows in `papers.csv` with matching `source_id`s (`arxiv:2508.02936`, `arxiv:2604.21501`, `arxiv:2508.11618`). |
| Extracts complete | `source_id` headings in `papers.md` = rows in `papers.csv` | **Pass.** 3 headings in `papers.md` (one per admitted source, including the incomplete-extraction case, which is documented as incomplete rather than omitted), matching the 3 `papers.csv` rows. |
| Nothing from recall | every `papers.csv` `source_id` traces to a `query_id` in `queries.csv` | **Pass.** AQUAH and GeoMind each trace to 2 query_ids (16+19 fetch/HTML-retry, and 17+20 respectively) plus their original probe query_id (3 and 9); the CO2 paper traces to query_id 18 (and probe query_id 6). All verified programmatically against `queries.csv`'s logged `query_id` set. |
| Grid parses | parse `papers.csv` as RFC 4180; report row and column counts | **Pass.** Parsed with Python's `csv` module: 3 data rows, 27 columns, no malformed rows. `screened.csv` and `queries.csv` also parsed cleanly (92 and 20 data rows respectively, consistent column counts throughout). |
| Claims tagged | count substantive claims in `index*.md` carrying no evidence tag; must be 0 | **Partial / judgment call.** `index.md`'s literature-facing claims (section "1. What this probe touched") carry `[Certain]`/`[Absent-searched]` tags. The "Coverage verdict" section summarizes run-mechanics findings (tool behavior, call-budget arithmetic) rather than literature claims and is not tagged, on the reading that the evidence-tag rule governs claims about the literature being reviewed, not procedural findings about this run's own tooling — `coverage.md` and `RUN.md` (which carry the full mechanics detail) are likewise untagged throughout, consistent with that reading. This is a judgment call, not a mechanical pass, and is flagged as such rather than asserted as a clean pass. |
| Absence claims backed | every `[Absent-searched]` claim cites `query_id`s | **Pass (vacuous).** No `[Absent-searched]` claim asserting that something does not exist appears anywhere in this run's output; the one `[Absent-searched]` tag in `index.md` is used exactly as the Evidence rules permit it to be used without a claim of nonexistence — to state that the evidence is too thin to tell, which is what a test-mode probe is expected to report. Test mode explicitly forbids affirmative absence claims, and none were made. |
| Files present | list the output directory against the Constraints list | **Pass.** All required test-mode files present: `RUN.md`, `index.md`, `queries.csv`, `screened.csv`, `abstracts/` (3 files), `papers.csv`, `papers.md`, `pdfs/` (2 files), `unreachable_urls.md`, `access_restricted.md`, `coverage.md`. Verified by directory listing. |
| Nothing written outside the run directory | | **Pass.** All files listed above are under `outputs/01_landscape/v0.2/`; no other files were created or modified by this run outside that directory (the only other file touched this run was reading, not writing, `prompts/01_landscape_neutral.md`). |

**Overall**: 9 of 10 checks pass cleanly; 1 ("Claims tagged") passes on a stated judgment call
about the evidence-tag rule's scope rather than a mechanical count, and is reported as such
rather than asserted as unambiguous. Two bookkeeping errors were found and corrected during
the run itself (see Self-critique); neither reached a citable output file. The mechanics slice
surfaced one clear, actionable tooling finding (PDF-fetch unreliability on arXiv) that should
change how the `full` run budgets its fetch calls. Verdict on proceeding to `full` mode: **GO**,
conditional on the fixes listed in `coverage.md` section 3.
