# Decision Log

Newest first. One entry per decision: what, why, what it rules out.

## 2026-09-11 — 02_tango: unreachable sources retrieved by hand, written as v0.2

The corpus owner worked through `outputs/02_tango/v0.1/unreachable.md` — not `paywalled.md` —
and retrieved 20 PDFs into a local store outside this repository. 19 distinct works; 14 were
re-read. Three were `context`/abstract-only demotions and all three supported a full `core`
write-up, so core rises 98 → 101 and context falls 85 → 82. The admitted set is unchanged at
183: no source entered or left, no query ran, no threshold moved, and `screened.csv`,
`triage.csv`, `queries.csv`, `shortlist.md`, `audit_sample.md` and `triage_stats.md` are
byte-identical to v0.1.

**Going after `unreachable.md` rather than `paywalled.md` is what made this worth doing.**
`paywalled.md` lists what could not be read at all; `unreachable.md` also lists what *was*
read, but from a substitute — an author preprint, a reader proxy, a third-party deposit. Eleven
of the fourteen re-reads were in that second category, and they are where the corrections came
from. Every quoted span of five or more words in those eleven records was matched mechanically
against the version of record. Eight verified unchanged. Three had changed: a published paper
with a third case study its preprint lacked (`doi:10.1016/j.dche.2026.100312`), one reporting a
pass@1 robustness figure v0.1 had explicitly recorded as absent
(`doi:10.1016/j.taml.2026.100660`), and one describing a different mechanism and reporting a
hallucination incident the preprint does not contain (`doi:10.1145/3731599.3767349`). **Three of
six preprint-to-published pairs had diverged.** Rules out treating `IDENTITY MATCH IS INFERRED`
as a formality: on this sample it is a real caveat, and a run that reads preprints for blocked
publishers should say so in every affected row rather than once in a methods note.

Recovering table cells a reader proxy could not render did the same job in miniature.
`doi:10.3390/buildings15173190` claims "deviations under 1.5%" in its abstract; its own Table 9
reports 1.624%, 1.998% and 2.834% in three of eight case-direction pairs. Rules out treating a
proxy read as equivalent to a publisher read when any claim rests on a table.

**Written as a new `v0.2` directory rather than corrected in place, and that conflicts with the
01 precedent recorded below on the same day.** The 01 entry ("paywalled full text recovered via
institutional access, corrected in place") explicitly "rules out bumping the version number for
a correction that touches no harvested record, no query, and no scoring threshold" — which is
exactly what this is. AGENTS.md §A8 points the other way: a committed run directory is evidence
and a later recount belongs in a new version. Both were in force; the conflict is recorded here
rather than resolved silently, because the two files disagree and the next person will hit it
again. What settled it for this run is that v0.1 is committed and its numbers are cited in the
03_gaps run, so keeping an unmodified v0.1 on disk lets `gaps.py` be re-pointed deliberately
instead of silently re-measuring. If the repository prefers the 01 convention, v0.2's contents
supersede v0.1's file for file and can be moved over it; nothing in v0.2 depends on the
directory name.

Rules out, regardless of which convention wins: reading `tango_touchpoints: none` as a negative
without checking `access_status`. Two v0.1 rows carried `none` purely because no text could be
retrieved; both now carry six touchpoints each. v0.1 flagged that hazard in prose and v0.2 is
the measurement that it was real in 2 of 2 cases.

Twelve demotions remain unresolved — four ChemRxiv, two SSRN — and two records are still read
from an unverified substitute. `paywalled.md` and `unreachable.md` carry both lists.

## 2026-09-11 — two more runs, and the 01 pipeline is frozen rather than generalised

`prompts/02_tango.md` asks what exists that bears on making TANGO agentic;
`prompts/03_gaps.md` synthesises what the finished runs record as missing. Both
are slash commands by symlink, like 01.

**The 01 scripts were not touched.** The first attempt made `triage.py`'s domain
vocabulary config-driven and `harvest.py`'s smoke set config-declared — small,
backward-compatible changes. Both were rejected in favour of new scripts, and the
reason holds generally: a committed run is evidence, and a script that two runs
share is a script whose next edit silently re-measures the earlier one. So 02 has
`triage_tango.py` and `audit_tango.py`, and 03 has `gaps.py` and `audit_gaps.py`.
`harvest.py` is the exception and is reused unchanged, because it was already
`--config`-driven; 02 ships `reference/queries_tango.json` rather than a fork, and
`reference/queries_tango_smoke.json` because the `--smoke` flag names 01's groups
and would have built an empty plan against 02's config. A test asserts the smoke
config is a verbatim subset of the full one, since a mechanics test over a plan
the real run does not have proves nothing about it.

**One exception to the no-sharing rule, deliberately.** `triage_tango.py` imports
`triage.py`'s pattern lists, so "is this agentic" is defined once and a fix lands
in both runs. That makes a change to those lists a method change for both, which
is now recorded in AGENTS.md §B1 next to the map.

**02's domain filter barely filters, and that is the finding the smoke test
bought.** 01 asks whether a record is in one of ten solid-earth subfields, which
most agent papers fail. 02 asks whether it is computational, which most agent
papers pass. Measured, keyless, on 2026-09-11:

```bash
python3 scripts/harvest.py      --out outputs/02_tango/v0.1-test --no-s2 \
    --config reference/queries_tango_smoke.json
python3 scripts/triage_tango.py --out outputs/02_tango/v0.1-test \
    --config reference/queries_tango.json --min-score 3 --min-strong 1 \
    --min-domain 1 --audit-n 40
```

3 of the 22 query cells (`simulation_orchestration` and `optimisation_uq` core,
`software_engineering` periphery, A_agentic band only), 6 API calls, 1,325 unique
records, 86% with an abstract. Shortlist **557, or 42%** — against 01's 712 of
11,191, or 6%. All three cells hit their paging cap, which is what the smoke
config's `openalex_max_pages: 2` is for and is why no count above describes the
literature.

`triage_tango.py` therefore has a third knob, `--min-domain`, which took that
corpus 557 → 301 → 169 at 1 → 2 → 3. It is not free — at 2 it also drops an LLM
workflow for analog circuit sizing that runs a simulator in its optimisation loop
— so the prompt requires settling it from `triage_stats.md` and measuring the cost
in the audit sample rather than assuming it.

**The knob shipped broken and the smoke numbers caught it.** `domain_score` was
`sum(dom) or sum(per)`, which is zero for every record the `triage.general`
fallback rescues, so the default `--min-domain 1` deleted the whole
`simulation_general` bucket — 11 of 557, and the only visible trace was a
shortlist one point smaller. That is the v0.5 `scope: none` regression arriving
through a different door: a structural filter discarding a class, invisible in the
score. The fallback now counts its own matches, and
`TestTheFallbackBucketSurvivesTheDomainKnob` pins both halves.

The run directory is **not committed**, following `v0.5-test` and `v0.5-test2`
rather than `v0.4-test`: a harvest-and-triage mechanics pass is regenerable in ten
minutes from the two committed configs and the commands above, and the numbers it
produced are here. Rules out shipping a stricter default in the script, rules out
reporting a shortlist size from this run as comparable to 01's, and rules out
citing any of these figures as a measurement of the field.

**02 keeps 01's `papers.csv` columns unchanged** and adds `transfer.csv`,
`transfer.md` and `paywalled.md` instead. Two grids with the same columns join,
and `gaps.py` reads both without a special case. Rules out a TANGO-relevance
column inside the comparison grid.

**The run pauses once, after screening, to hand back the paywall list.**
Institutional access is the one thing the session cannot get for itself, and the
01 run demoted six screened-core records to context for want of a login.
`audit_tango.py` requires every `abstract-only` source to appear in
`paywalled.md`, so the handoff list is complete rather than partial, and
`blocked_by` separates `paywall` from `bot-protection` because v0.5 found a
gold-OA paper no route could retrieve — an OA flag is a licence status, not an
access outcome.

**03 extracts candidates mechanically and verifies them with an agent.** Run
against v0.5 it produced 117 candidates. Two shapes were wrong on the first pass
and both are now tested: five of six "empty categories" were periphery subfields,
which are empty by design, and `claim-gap` found nothing because `maturity_claimed`
is free text by SCHEMA — the mechanical comparison that does hold is a non-empty
claim against an M0/M1 evaluation, which finds 11. Rules out a gaps document
assembled from recall, and rules out `confirmed-absent` from a verification pass
that searched nothing.

## 2026-09-11 — third paywalled-recovery batch: the three EAGE EarthDoc records

The three EAGE records named as unresolved at the end of the second batch were supplied as
PDFs and read the same way (corpus owner's institutional access, full text read before any
file edit). All three cleared the agentic bar and promoted from `context`/abstract-only to
`core`: the Geowellex MCP + A2A surface-logging agent (First EAGE Workshop on Surface
Logging, M2), a LangGraph-orchestrated geological Q&A pipeline evaluated on the named
Acacia Grove-1 well (Sixth EAGE Digitalization Conference, M3), and a four-agent RAG
workflow revising Random-Forest sedimentological predictions (Sixth EAGE Borehole Geology
Workshop, M2). As in the second batch, none were reclassified `out`.

One subfield correction, from the same evaluation-focus rule used in both earlier batches:
the sedimentological workflow moves from `geological_modelling` to `reservoir_engineering`
(secondary `geological_modelling`), because it is evaluated on facies and genetic-element
prediction from wireline logs against cored-interval ground truth — the same reasoning that
moved the well-log papers in the first batch.

Two of the three sit close to the scope bar and were admitted on "iterates on its own
output" rather than on tool choice or planning: the LangGraph graph is fixed except for a
classifier LLM's regenerate-or-accept verdict, and the four-agent workflow reviews a
prediction the Random Forest made. Recording that explicitly rather than letting the tier
imply a uniform mechanism: a `core` row means the full text was read and the bar was
cleared, not that it was cleared the same way.

**This batch falsified a claim the report was making.** Sections 02 and 04 stated that
every core source recovered by institutional access named a base model — true of the first
fifteen, false of these. Two of the three name no LLM anywhere, taking unnamed-model core
rows from 9 of 38 to 11 of 41. The claim is corrected and re-scoped to the format rather
than removed, because what changed is the venue type being read, not the recovery route.
Three-to-five-page conference extended abstracts clear `core` on mechanism while omitting
base model, code availability and held-out status; none of the three states any of the
latter two.

Core rises from 38 to 41; context falls from 113 to 110; total admitted (151) is unchanged.
Report sections 00, 01, 02, 03, 04, 05, 06 and 08 and `index.md` were regenerated in place,
same reasoning as both earlier batches. Section 06 gained one entry, the first added by a
recovery pass: the LangGraph paper's correction-loop design is a direct methodological
disagreement with the GraphRAG catalog paper's "fundamental structural flaw in
retrieval-then-synthesize architectures", and the disagreement is only visible in full text.

Rules out reading `tier: core` as a uniform evidence standard across venue types — it is a
statement about what was read and what the system does, not about how completely the source
documents itself. Whether `papers.csv` completeness should be reported per tier is left to
v0.6 rather than fixed here, since changing what `core` asserts mid-run would re-measure the
earlier batches. Also rules out merging the Geowellex record with its own cited predecessor
(`doi:10.3997/2214-4609.2025101389`, still abstract-only): the identity-key rule keeps them
separate, and only the record actually read carries a `system_id`, so the pair cannot
inflate a per-system count.

## 2026-09-11 — second paywalled-recovery batch, same in-place correction

A second batch of eight PDFs, supplied the same way as the first (corpus owner's
institutional access, read in full before any file edit), all cleared the agentic bar and
promoted from `context`/abstract-only to `core`: a landslide-reconstruction agent
(Soils and Foundations), multi-GeoLLM (Automation in Construction 2025), a
supervisor-ReAct-blackboard tunnelling MAS (Computer-Aided Civil and Infrastructure
Engineering), a slope-reliability multi-agent framework (Advanced Engineering
Informatics), AGeoKE (Applied Computing and Geosciences), the GAGAW journal record (Big
Data and Earth System — a second, separately-keyed publication of the ESSOAr-preprint
system already in the corpus), EQSIM Agent (ACM), and a seismic-processing assistant (The
Leading Edge). Unlike the first batch, none were reclassified `out` — every record this
time genuinely decides something for itself (tool choice, planning, or self-correction over
its own output), so this batch is a pure recovery with no scope-corrections attached.

Two subfield corrections follow from the same evaluation-focus rule as the first batch:
the GAGAW journal record moves from `inversion` to `hydrogeology`, matching both its own
evaluation (subsurface water content, not an inversion task per se) and its sibling
preprint record's existing subfield; EQSIM Agent's architecture is corrected from
`single-agent` to `multi-agent-hierarchical` now that its vision and RAG sub-agents are
visible in full text.

One maturity call is a genuine tie-break, resolved for consistency rather than by a
sharper rule: the tunnelling MAS's evaluation site is real, contractor-supplied data from
a specific geo-located project, but the project itself is never given a formal name (only
dataset labels and borehole IDs) — rated `M2`, the same standard already applied to the
well-log papers' "100 field wells" in the first batch, rather than `M3`.

Core rises from 30 to 38; context falls from 121 to 113; total admitted (151) is
unchanged. Report sections 00, 01, 02, 03, 04, 05 and 08 were regenerated again from the
updated `papers.csv`/`papers.md`, in place — same reasoning as the first batch: this is
recovering evidence for already-admitted records, not a scoring or method change, so it
does not warrant a version bump. Rules out treating a second venue-publication of the same
system as a duplicate to merge — the identity-key rule keeps preprint and journal versions
separate, so GAGAW now has two rows, one still abstract-only and one full-text. Also rules
out chasing every remaining unread paywalled record indiscriminately: IEEE Xplore returned
nothing to an unauthenticated fetch for IEEE CAIBDA, and no PDF was supplied for IEEE CAIT
or the three remaining EAGE EarthDoc records, so those stay `context` rather than being
guessed at.

## 2026-09-11 — paywalled full text recovered via institutional access, corrected in place

The corpus owner has institutional access to several publishers this run could not reach.
Eleven `context`/abstract-only or textually-empty records — flagged in `unreachable.md` as
paywalled, OA-but-blocked, or lacking any retrievable abstract — were supplied as PDFs and
read in full, following the same step-4 procedure (full text, then the `papers.csv` row and
`papers.md` block together, never split) as the original run.

**Full text is read before deciding tier, not after.** Seven records turned out to be
genuinely agentic (an LLM decides something for itself: plans, calls a tool, iterates on
its own output) and are promoted to `core` — Hydro-Agent, OntoGRC, a tunnel
geological-forecasting agent, a well-log multi-agent framework, LogACF, the Geo-Resource
Agent and InsightsAI. Three of those also get a corrected `subfield`: two well-log papers
move from `inversion` to `reservoir_engineering`, and the Geo-Resource Agent moves from
`geomechanics` to `reservoir_engineering`, because SCHEMA.md assigns subfield by where the
evaluation is set and none of the three ever evaluates the task their old subfield implied.
Four other records — a second Ore Geology Reviews paper, an SPE drill-bit paper, an SSRN
preprint and a ResearchGate deposit — had looked plausibly agentic from title or abstract
alone, but full text showed either no LLM component at all (pure MARL) or an LLM confined
to a single non-agentic extraction/classification call feeding a deterministic pipeline it
never calls or iterates on. These four are reclassified `out` (`not-agentic` or
`pre-llm-only`) and removed from `papers.csv` entirely, not left in `context`.

**Corrected in place in the existing `v0.5` run, not a new version.** This is not a scoring
or method change — `triage.py`, `AGENT_COMPOUND` and the shortlist cut are untouched, and
no new query or re-triage was needed. It is the same class of correction as this run's own
"Recovered in close-out" pass in `unreachable.md`, just after the report was already
drafted: `screening.csv`, `papers.csv` and `papers.md` are corrected, and every report
section that cites a count (00, 01, 02, 03, 04, 05, 08, `index.md`) was regenerated from
those files rather than hand-adjusted. `README.md`'s headline numbers were updated to
match. Core rises from 23 to 30; context falls from 132 to 121; total admitted falls from
155 to 151. Rules out treating an abstract-only admission as reliable evidence of either
scope or maturity — in this batch the abstract was wrong about scope in four cases out of
eleven — and rules out bumping the version number for a correction that touches no
harvested record, no query, and no scoring threshold.

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
