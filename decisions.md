# Decision Log

Newest first. One entry per decision: what, why, what it rules out.

## 2026-09-10 — every derived facet publishes its own denominator

Two panels were answering a question with a number whose base was invisible, and
both invited the same wrong reading.

**The framework facet now leads with how many papers name anything.** Only 13 of
the 23 core systems name an orchestration framework or harness at all; the other
10 describe planners, role-specialised agents and tool loops without saying what
they are built with, and on the 132 context rows — where `tools_used` comes from
an abstract — 19 name any tool the keyword list looks for. That is why LangGraph
sits at 5 against MCP at 12: MCP is in the paper *titles* (ESHM20-MCP,
specfem-mcp, GeoMCP, petro-mcp, open-darts-MCP) because it is a selling point,
while LangGraph is plumbing nobody advertises. The facet measures naming
behaviour, and 4 of its 5 LangGraph mentions are core tier — naming your
framework correlates with being readable at all. Rules out reading any framework
count as adoption.

**The fields section now shows the admission rate, which is what actually
explains its distribution.** Reservoir engineering has 44% of the admitted
literature not because its query returned more — seismology's returned more, 96
shortlisted against 74 — but because 92% of what it returned was admitted,
against 28% for seismology and 7% for CCS. What its query returns is the SPE,
IPTC, OTC and IADC conference circuit: short papers that are agentic by their
own account, correctly admitted, and unreadable in detail. 65 of those 68 rows
are abstract-only and only 3 are core, so the field with the most literature
supports 3 of the 23 characterisable systems. Rules out reading field size as
research volume, and rules out reading it as evidence of where the readable work
is.

The denominator comes from `shortlist.md`, and finding it corrected something:
**`RUN.md`'s per-group shortlist figures are stale.** They record the 606-record
shortlist from before the mid-run triage refix, not the 712 the run finished
with — seismology is 96 there, not 91. `shortlist.md` is the tracked artifact of
the final cut and is now the only thing the page counts from. The two columns are
also different taxonomies — the query family that *found* a record versus the
subfield screening assigned it by where its evaluation is set — so the panel
prints how many rows moved between them, and a rate at or above 100%
(inversion 250%, geothermal 100%) is that mismatch rather than a perfect yield.

## 2026-09-09 — dashboard: a summary table, filters first, and two counting fixes

Five changes after reading the first build.

**The page opens on a table, not on tiles.** Seven counted rows from 11,191
harvested to 132 unreadable, each naming its own denominator. The six KPI tiles
are gone: the table says strictly more and having both put the same numbers on
screen twice. The funnel is deliberately not presented as nested — `screened`
(1,028) exceeds `shortlisted` (712), because 150 records were screened from
below the triage cut — so the share column names its denominator per row rather
than being headed "of previous", which would have been wrong on exactly the row
whose surprise it has to explain.

**The paywall row states what is counted and no more.** `papers.csv` has no
paywall column, and `access_status: abstract-only` covers paywalls, refused
delivery on nominally open articles, software deposits and records with no
abstract in any API. `unreachable.md` accounts for all of them but tabulates
only two subsets (6 rows and 2 rows) and narrates the rest. So the row reports
132 full text not obtained, cites those two counted subsets, and says the run
cannot put a number on paywalls alone. Rules out a "paywalled: N" figure that
would have been a guess.

**The explorer moved to second.** Filtering is what most readers open the page
to do, and it was the fifth section.

**`model_family` became `model_families`.** It was single-valued and returned
the first match from an ordered list with GPT first, so 11 of 23 core rows were
attributed to GPT — and 7 of those 11 also name Claude, Gemini, Qwen or
DeepSeek, several because comparing backbones *is* their method. The facet read
as market share while measuring "GPT appears somewhere in the cell, and GPT
sorts first". Multi-valued, its bars sum to more than 23 and the panel says so.
Rules out reading the model chart as a share of systems.

**`scripts/enrich.py` is new, and is the only optional script.** Author
affiliation is in no tracked artifact, and the alternative to a network call was
inferring nationality from author names, which the contract forbids. Three
keyless OpenAlex calls give countries for 97 of 155 sources and a publication
type for 140; the output is committed so `make export` still needs no network,
and `export_web.py` omits the geography panel when the file is absent. The same
call repaired `source_type`, which was blank on 108 of 155 rows — normalised,
because the run's vocabulary and OpenAlex's collide (`article` and
`journal-article` were the same kind on two bars). Rules out inferring country
from names or venue, and rules out a geography chart drawn over an unstated
subset: 97 is printed beside every bar.

## 2026-09-09 — the run is readable as a static dashboard

`scripts/export_web.py` turns one run directory into a single JSON document, and
`web/` renders it as a static Astro site. `make export && make web` produces
`web/dist/`, 472KB, which opens by double-clicking `index.html`.

**Static, with the run compiled into the page.** The research direction is
unpublished and lives on institutional GitLab, so the distribution method is
handing somebody a folder. That rules out a server, a database and a runtime
fetch — and it is why `web/scripts/relativise.mjs` exists: Astro emits
`/assets/…` for every value of `base`, and an absolute path resolves against the
filesystem root when a page is opened as a file, so the page loads unstyled and
inert for the recipient while working perfectly over `http://localhost`. The
built folder makes no network request of any kind, including for fonts.

**The report is re-cut, not appended to.** Each thematic section renders beside
the counts it describes; `export_web.py` assigns every section a `group` so the
mapping lives in one place. Evidence tags become filters and citations become
numbered markers that open a source's full record, including the verbatim
`papers.md` quotes for the 23 core rows. Rules out a prose dump beside unrelated
charts, and rules out any characterisation on the page that cannot be traced to
the sentence it came from.

**One derived facet, and it is labelled.** "Frameworks the agents call" is a
keyword match over `tools_used` and `base_model` — not a `SCHEMA.md` column and
not covered by any audit check. Everything else on the page is read from an
artifact or counted from one. Method prints the whole keyword list *including
the eight terms that matched nothing*, because a derived count is only checkable
if the reader can see what was searched for; two of those greyed terms were how
we found that `\bSPECFEM\b` cannot match `SPECFEM2D` and that the harness names
sit in `base_model` rather than `tools_used`. Rules out presenting the facet as
a census, and rules out a derived value sitting unmarked in a column of read
ones.

**Maturity is never a colour.** Six ordinal steps of one hue cannot hold a
visible lightness gap against a white surface — the palette validator fails the
ramp — so the level is carried by axis position and by filled pips, which
survive grayscale, print and any colour vision. The distribution also plots the
132 unratable rows as a bar of their own: a maturity chart drawn over 23 rows
without it looks like a survey of the field. Rules out an M0–M5 colour scale,
and rules out quoting the distribution as the field's operational maturity.

Two data corrections fell out of building it, both the same word-boundary bug in
different places: `MODEL_FAMILIES` matched Qwen as `\bQwen\b`, which cannot match
`Qwen3-4B`, so both core Qwen systems were counted as `other named`; the fix is
a `(?![a-z])` lookahead rather than dropping the boundary, which would have
matched `Qwenzhou`. That was a `strict=True` xfail in `tests/test_export_web.py`
and is now a passing parametrised test. `export_web.py` also printed its summary
to stdout, which AGENTS.md B3 reserves for `audit.py`'s table; it goes to stderr.

Also recorded: on v0.5, 0 of 155 annotated-list summaries differ from the row's
own `task` cell, so `08_papers.md` adds no sentence the paper record did not
already carry. The exporter reports that count on every run rather than leaving
it to be inferred from an empty field.

Rules out: a hosted or server-rendered front end for this repository; reading
any number off the page that the run did not compute; and treating the framework
facet as schema data.

## 2026-09-07 — v0.5 landscape run

First full landscape under the v0.5 prompt. Harvest: 11,191 unique records (API plus 14
grey extras). Shortlist after a mid-run triage refix: 712. Admitted: 155 (23 core
full-text, 132 context). Grey pass used 11 of 40 web calls.

Three method changes landed during the run, not before it:

- **Paging caps raised** (`openalex_max_pages` 5 → 20, `arxiv_max_results` 200 → 1000).
  The shipped caps truncated periphery queries; section 07 would have reported the cap as
  the size of the neighbouring literature.
- **OpenAlex key is required for a full harvest.** Keyless allowance is $0.10/day; a
  spent budget now aborts instead of retrying into a quiet half-corpus. `n_available` is
  logged so a cap is visible in `queries.csv`.
- **Triage dropped a whole class of records.** Anything that said "geoscience" without a
  named subfield got `scope none` and was discarded regardless of score (190 records).
  MCP vocabulary was also missing. Patterns were widened, triage re-run with `--force`,
  and the previous cut kept under `pre-refix/`. Shortlist 606 → 712; core tier 36 → 54
  before paywall demotions.

Rules out: treating `v0.4` as the landscape; running a full harvest without an OpenAlex
key; lowering `--min-score` to recover the dropped class (the binding filter was
structural, not the score knob).

## 2026-09-07 — bump to v0.5

The smoke-test fixes ( `$OUT`, `--smoke`, triage refuse, grey extras, `08_papers` tag
exemption) are the v0.5 prompt. Full runs write to `outputs/01_landscape/v0.5/`. The
`v0.4` and `v0.4-test` directories stay as prior runs. Rules out: starting the first
complete harvest under a v0.4 path that already holds a stalled run.

## 2026-09-07 — smoke test of v0.4 before a full run

A mechanics pass (`--limit-queries 6`, then scripts/prompt fixes) showed four failures
that would have stopped a full run or made its audit lie.

**`--limit-queries N` is not a smoke test.** The plan is core groups first; periphery
starts at q021. Six queries harvested 1865 records and zero periphery, so `07_periphery.md`
could not be written from harvest counts. `--smoke` now runs seismology, hydrogeology, and
earth_observation (A_agentic only). Rules out: using `--limit-queries` to “test the prompt”.

**Re-triage after screening, and grey rows after triage.** `triage.py` now refuses if
`screening.csv` exists unless `--force`. Grey/snowball records are appended to
`screened.csv` (`source_apis: web`) without re-triage; `audit.py` allows those extras
instead of requiring `len(triage)==len(screened)`. `screening.csv` has no `found_via`
column — that field is `papers.csv` plus a note.

**The evidence-tag check scored `08_papers.md`.** Core 4–6 line annotations have no
`[Certain]` tag by design. Audit now skips `08_papers.md` and `index.md` for tags (still
checks citations and promotional language across all report files). Rules out: a finished
annotated list failing the contract.

**Commands hardcoded `outputs/01_landscape/v0.4` after telling the model not to overwrite
it.** The prompt now uses `$OUT` everywhere.

## 2026-09-07 — v0.4.1: fixes from the first real run

Three problems the v0.4 run exposed. All three were invisible until real data arrived,
which is the argument for running the audit sample at all.

**The false-negative remedy named the wrong knob.** The run measured 6.7% false negatives
(4 of 60) and the prompt said to lower `--min-score`. That would have admitted nothing:
all 4 misses had `strong_hits: 0`, so `--min-strong` was the binding half of the AND, and
`triage_stats.md` hid this by varying only `--min-score` — the column read 458 at every
threshold from 1 to 3 and nobody could see why. The stats table now varies both knobs, and
the prompt requires diagnosing which is binding before widening.

**The misses were a vocabulary class, not a threshold problem.** All 4 were systems that
plan or automate with an LLM while never using the word "agent" — "LLM-Powered Data
Automation for 3D Geological Model Updating", "LLM-assisted workflow for geological unit
harmonization". Recovering them by threshold meant screening 2,310 records instead of 458;
recovering them with an `AGENT_COMPOUND` pattern list costs 73. Shortlist goes 458 → 531,
all 4 are caught, and all 109 previously admitted records are unaffected. Rules out:
treating a recall failure as a threshold problem before checking whether it is a lexical
one.

**The audit sample was too small to act on.** 4 of 60 gives 6.7% with a confidence
interval wide enough to straddle the 5% action threshold, so the run could not tell
whether it was obliged to widen. Default is now 150.

Also: `screened.csv` and `triage.csv` are gitignored. 22MB each into a 416KB repo, and
both regenerate from `reference/queries.json` in minutes.

Separately, a forked subagent returned a fabricated completion for the screening pass —
2.8s, zero tool calls, no file written. The session caught it by checking the filesystem
and retried successfully. The prompt now forbids delegating screening and requires every
batch to be verified with `wc -l` against the file rather than against the model's memory
of having written it.

## 2026-09-03 — v0.4: bibliographic APIs replace web search; the deterministic half becomes code

v0.3 was 870 lines, roughly half of it justifying its own rules against past run failures.
It was long because the model was doing work that does not need judgment, and it was
fragile because compliance was self-attested. Both are fixed by moving work out of the
prompt rather than by writing more prompt. v0.4 is 150 lines plus `reference/SCHEMA.md`.

**Search moves to OpenAlex and arXiv, called from `scripts/harvest.py`.** OpenAlex returns
200 records per call with abstracts, citation counts and DOIs, and accepts boolean
queries; a four-subfield single-band test returned 1,795 unique records with 83% abstract
coverage from 8 calls. v0.3 budgeted 100 web searches for ~600 title-and-snippet items at
a measured 6.1 unique per call. This is roughly a 30× change in records per call and it is
what makes comprehensive coverage arguable at all. It also deletes a whole failure class:
the abstract arrives with the record, so no call is ever spent storing one and
`screened.csv` cannot be written without its text. Rules out: absence claims resting on
web-search phrasings, and the entire five-bucket web-call budget.

**Pre-LLM agent work is out of scope.** It shared no vocabulary with lineage 1, doubled
the search surface, and forced the 23-query-family scheme that most of v0.3's budget
arithmetic existed to ration. `triage.py` still flags pre-LLM records so the exclusion
stays visible and reversible.

**The excluded periphery is counted rather than asserted.** EO, climate, ocean and
planetary are harvested and characterised in one report section from harvest counts, which
costs almost nothing once the API returns them anyway, and replaces v0.3's six
out-of-scope probe queries with a measurement.

**Triage is deterministic; its cost is measured.** `triage.py` scores every record and
writes both a ranked shortlist and a random sample from *below* the cut. Screening the
sample yields a false-negative rate, so the shortlist threshold is a reported measurement
instead of a hope. Two scoring bugs found while building it are worth recording, because
both fail silently: matching `ReAct` case-insensitively produced 377 false positives out
of 470 at one score level ("react" is what chemicals do), and counting an agent term as
evidence of LLM vocabulary let 40-year-old multi-agent work into an LLM shortlist.

**`scripts/audit.py` replaces the self-audit table.** Every check parses the artifacts and
exits non-zero on failure — column order, citation resolution, evidence tags, absence
claims backed by query ids, extract parity, promotional framing. v0.3 asked a compacted
run to verify its own compliance from memory, which is the one thing it cannot do.

**A malformed query now fails loudly.** A bare `AND` inside an OR group makes OpenAlex
return zero results with no error, which is indistinguishable downstream from an empty
field. `harvest.py` refuses to run on such a config and marks any zero-result call `zero`
rather than `ok`. Eight terms in the initial query set had this bug.

**Deliverable shape, decided:** executive summary, techniques, architectures,
then a full annotated paper list, tiered `core` (deep-read, 4-6 lines each) and `context`
(one line from the abstract). Rules out: a report that is a list of papers, and a paper
list that only covers the deep-read set.

## 2026-09-03 — v0.3: pass 2 stops fetching, screened set carries its own text

The v0.2 test run exposed three arithmetic impossibilities that would each have stopped or
hollowed out the `full` run.

**Pass 2 no longer fetches.** 100-150 pass-2 assessments at one fetch each needed 100-150
calls against a 40-call fetch bucket that pass 3 also drew on; the run would have blown the
cap or silently skimmed abstracts while reporting methodology assessments. Pass 2 is now
explicitly judged from the abstract and snippet, at zero calls, with
`pass2-undecidable-from-abstract` as a logged cut for the cases it cannot settle. Assessed
stays at 100-150 rather than shrinking, because breadth is now free — the landscape's width
comes from the seed calls, not from documents opened. Rules out: any maturity rating from
pass 2, and any claim that a pass-2 cut was methodological when it was abstract-level.

**Buckets re-split to 100 seed / 60 reads / 30 PDFs / 40 snowball / 20 reserve.** Reads and
PDF downloads are separate line items because they are separate calls: raw `arxiv.org/pdf`
failed 2 of 3 times in the test run (10 MB limit; undecompressable text), `arxiv.org/html`
worked, and the HTML route yields no saved binary. Two rounds of snowballing over every
admit needed 80-120 calls against 40, so snowballing is now a bounded scheme — thin
subfields first, round 2 only on the productive lookups, 10 calls held for the 429s that
Semantic Scholar returns without a key. Most admits will go unsnowballed by design.

**`abstracts/` shrinks to the sources actually fetched; `screened.csv` gains `snippet`.**
89 of 92 rows in the test run stored no text, leaving 97% of the screened set re-triageable
by title only — the exact failure the retained-screened-set decision existed to prevent, and
it happened because storing text was a second write to a second location. The snippet the
search already returned now goes in the row being written anyway: no extra web call, cheaper
than 600 files, and `no` requires an in-cell reason with a stop-and-report rule above 25%.

Phrasing floor drops from 5 to 3 per family (5 now applies per cell where an absence claim
is actually made, bought from the widening allowance), the three zero-yield cells from the
probe get prescribed replacement vocabulary, and two self-audit rows are added: snippet
coverage, and a cross-check of `queries.csv` fetch rows against the artifacts and `pdfs/`.
The second exists because two of twenty rows in the test run described calls that never
happened as logged — `queries.csv` is written from intent, before the fact, and nothing was
reconciling it afterwards.

## 2026-09-02 — v0.2: hard web-call cap, test run becomes a coverage probe

Every run mode gets a hard cap on network calls (`test` 20, `full` 250) instead of only
pass-count budgets, which were unbounded on the search side. `test` is redefined from a
mechanics check to a coverage probe: 15 calls sampling all 10 subfields × 2 lineages into
`coverage.md` (yield table, projection, go/no-go verdict), 5 calls taking 3-4 sources
through the whole artifact chain including PDF download. Snowballing and the Chinese track
are `full`-only — both cost more than the whole `test` budget.

Runs now retain `queries.csv`, `screened.csv` and `abstracts/`, so scope or taxonomy can
change without re-searching. Rules out: `test` producing any landscape synthesis, and any
absence claim from a `test` run.

Two follow-on corrections in the same version. Storing abstracts must never cost a web call
— screening rides on the search results, so `abstract_stored` becomes
`full / snippet-only / no` rather than requiring a fetch that would blow the cap. And
compliance with a 700-line prompt is now verified rather than assumed: a section-by-section
re-read schedule, plus a Self-audit table closing `RUN.md` in which every invariant is
checked against the output files (row-count parity between `screened.csv`, `papers.csv` and
`papers.md`, CSV parses, every admit traceable to a `query_id`).

## 2026-08-31 — Host on institutional GitLab

Repo is private, on institutional GitLab, with a second maintainer.
The research direction is unpublished, so it stays on institutional infrastructure next to
the existing wiki and object storage. Cost: no `gh`/agent PR tooling.

## 2026-09-01 — Run Test Run first and evaluate prompt

The 01_landscape_neutral.md prompt is run first with max 20 web sources to check its result.
No pdfs are stored in GCP.
