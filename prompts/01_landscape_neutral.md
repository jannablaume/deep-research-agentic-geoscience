---
name: 01_landscape_neutral
description: Scoping review of LLM-based agentic AI in solid-earth and subsurface geoscience. Harvests the corpus from bibliographic APIs, screens it, deep-reads the core set, and writes a neutral landscape report with an annotated paper list.
---

# 01 — What exists in agentic AI for geoscience

Version: v0.5

Map what has been built in **LLM-based agentic AI for solid-earth and subsurface
geoscience**: the techniques, the architectures, how systems were evaluated, how mature
they are, and who built them. Descriptive only: no gaps, no recommendations, no research
agenda of any kind.

## Setup

Resolve the output directory first. Default is `outputs/01_landscape/v0.5/`. If it
exists, use `v0.5-run2`, `-run3`, … A mechanics test uses `v0.5-test` (see Smoke
test below). Never write into a directory that already has `screening.csv`. Record
the resolved path on line 1 of `RUN.md`, and substitute it for `$OUT` in every
command below.

Read `reference/SCHEMA.md` now, and again before step 4.

## Smoke test (before a full run)

Do this once after editing the prompt or scripts, in a fresh
`outputs/01_landscape/v0.5-test/` (or `-test2` if that exists). It is not a landscape.

```bash
OUT=outputs/01_landscape/v0.5-test
python3 scripts/harvest.py --out "$OUT" --no-s2 --smoke
python3 scripts/triage.py  --out "$OUT" --min-score 3 --audit-n 40
```

`--smoke` runs three queries (seismology A_agentic, hydrogeology A_agentic, and
earth_observation A_agentic) so periphery counting is exercised. `--limit-queries N`
takes the first N plan rows and **skips periphery** (periphery starts at q021); do
not use it as the smoke test.

Then screen the shortlist, screen the 40-record audit sample, deep-read 2–3 arXiv
core papers, write the nine report files (they will be thin), run `audit.py`. Do not
apply the 150–800 shortlist band. Do not write absence findings about the field.

If harvest, triage, `screening.csv`, `papers.md` extracts, report tags, and
`audit.py` all complete, the prompt is runnable. Then start a full run in a **new**
directory.

## The five rules

1. Nothing is written unless a tool call **in this run** retrieved it. No counts, no
   citations, no CSV cells from recall. A remembered paper must be found in the corpus
   before it can be used.
2. Quote before you characterise. Every claim about a system traces to a verbatim extract
   in `papers.md`.
3. Every substantive paragraph in the report carries `[Certain]`, `[Likely]` or
   `[Absent-searched]`.
4. Append as you go — `screening.csv`, `papers.csv` and `papers.md` — never only at the
   end. This run will be summarised and compacted several times. **One writer per file.**
   Parallel subagents each holding a batch in context and writing at the end defeats this:
   the unit that survives a crash becomes the whole batch plus a merge step, and the merge
   is the last thing to happen. If you delegate, delegate the reading and have the parent
   write, in batches, verifying each against the file.
5. Report failures as failures. A step that did not work, said plainly, is worth more than
   a plausible-looking substitute.

## Scope

**In**: systems where an LLM or foundation model **decides something for itself** — picks
a tool, plans a sequence, iterates on its own output, calls code and acts on the result —
applied to geomechanics, seismology, hydrogeology, reservoir engineering, geothermal, CCS,
mining, engineering geology, geophysical inversion, or geological modelling.

**Out**: prompt-in/text-out LLM applications with no decision loop; pre-LLM agent work
(multi-agent systems, agent-based models, RL controllers, expert systems) except where a
source in scope builds on it; anything before November 2022.

**Periphery** — Earth observation, climate and atmosphere, ocean, planetary: harvested and
counted, never deep-read. One report section reports their size and character from the
harvest counts. This makes the scope boundary a measurement instead of an assertion.

## Procedure

### 1. Harvest — deterministic, no judgment

```bash
python3 scripts/harvest.py --out "$OUT" --no-s2
python3 scripts/triage.py  --out "$OUT" --min-score 3
```

Expect ~15-25k unique records and a shortlist of a few hundred. Read `triage_stats.md`.
On a **full** harvest, if the shortlist is under 150 or over 800, adjust `--min-score`
and re-run `triage.py` — it costs no network call. That band does not apply to a
`--smoke` harvest. Record the threshold you settled on and why in `RUN.md`.

Do not re-run `triage.py` after `screening.csv` exists. The script refuses unless
`--force` is passed, and `--force` requires re-screening the new shortlist and audit
sample from scratch. Grey or snowball records are appended to `screened.csv` without
re-triage; `audit.py` allows those extras when `source_apis` contains `web`.

**Settle the threshold before step 2 begins.** `triage.py` overwrites `shortlist.md` and
`audit_sample.md`, and once `screening.csv` exists it describes the previous pair. If you
re-triage anyway — including to add vocabulary patterns — the shortlist and the audit
sample no longer match your screening decisions, and the false-negative rate you report is
measured against a sample file that is no longer on disk. Either finish the run on the old
cut and change the patterns in v0.6, or re-triage and screen the new records too.

If any query reports `status: zero`, it is malformed, not empty. Fix
`reference/queries.json` and re-harvest that band. A silently empty query is the one
failure that leaves every downstream number looking plausible.

Do not add web searches at this stage. The APIs cover the indexed literature better than
search does; web search is for step 3 only.

### 2. Screen

Read `shortlist.md` top to bottom. One `screening.csv` row per record, per
`reference/SCHEMA.md`. Batch it: write rows every ~50 records, not at the end.

**Do this yourself, in this session.** The shortlist is a few hundred digests — large, but
well inside one context. Do not hand screening to a subagent: it is the judgment this
whole run rests on, and a delegated pass returns a summary you cannot check against the
records that produced it.

**Verify every batch against the file, not against your memory of writing it:**

```bash
wc -l "$OUT/screening.csv"
```

The count must rise by the size of the batch you just wrote. If it did not, the rows were
not written — say so and write them, rather than continuing from the assumption that they
landed. This applies with no exceptions to any work you delegate anywhere in this run: an
agent that reports success while the file it was told to create is absent or unchanged did
not do the work, and its summary is not evidence that it did.

Then screen `audit_sample.md` the same way, with `from_audit_sample: yes`. These are
records the triage cut. Any you mark `in` is a false negative in the ranking. Report the
rate in `RUN.md` whatever it is — it is the only honest measure of what the corpus missed,
and it tells a reader how much to trust the map.

**If the rate exceeds ~5%, diagnose before you widen.** Look up each false negative in
`triage.csv` and read its `agentic_score`, `strong_hits` and `signals`. The cut is an AND
of two thresholds, and which one is binding decides the remedy:

- `strong_hits` **is 0** — the record carries no agent vocabulary at all and was cut by
  `--min-strong`, not by score. Lowering `--min-score` will admit nothing; check the
  `strong>=0` column in `triage_stats.md` for what dropping it would actually cost. This is
  usually better fixed by adding the missing phrasing to `AGENT_COMPOUND` in `triage.py`
  than by widening, because the whole class shares a vocabulary.
- `strong_hits` **is 1 or more but the score is below the cut** — the score is binding.
  Lower `--min-score`, re-run `triage.py`, and screen the new records.

Either way, record in `RUN.md` what you diagnosed, what you changed, and the rate before
and after. A false-negative rate that was measured and acted on is a result; one that was
measured and quietly accepted is not.

### 3. Fill the gaps the APIs cannot reach

Bibliographic APIs do not index grey literature, and a large share of subsurface agentic
work is industry-facing. Spend up to **40 web searches or fetches** here, no more, logged
by appending rows to `queries.csv` with `api: web`:

- SPE / OnePetro, operator and service-company technical papers
- USGS, BGS, IEAGHG, geological surveys and regulators
- GitHub and Hugging Face, for systems released as code and never written up
- Stanford Geothermal Workshop, SEG / EAGE / AGU / EGU abstract archives

Most of this is paywalled. Do not try to breach a paywall. What the report needs from
these sources is what was built and what it was applied to, and that is usually in the
abstract or landing page. Admit them as `access_status: abstract-only`, `tier: context`,
unless the visible text genuinely supports a `core` write-up.

A grey (or snowball) source not already in `screened.csv` must be appended there first
(same columns as `harvest.py`; `source_apis: web`; `identity_key` by the harvest rules
in SCHEMA.md). Only then add a `screening.csv` row. Put `found_via: grey` or
`found_via: snowball` in the `note` — `screening.csv` has no `found_via` column; that
field lives in `papers.csv`.

### 4. Deep-read the core tier

For each `tier: core` record: fetch the full text, read it — **especially the evaluation,
limitations and future-work sections**, where authors state what their system could not do
— then in the same step write both its `papers.csv` row and its `papers.md` extract block.
Never split those into separate passes: the extracts need the text in front of you and are
the expensive half; a run that dies with the CSV written and the extracts missing has kept
the cheap half.

For arXiv, fetch `arxiv.org/html/<id>`, not `/pdf/` — the PDF route fails on size limits
and undecompressable text. If a full text cannot be read for tool reasons, that is not an
access barrier: record it as a tooling failure in `RUN.md` and downgrade the record to
`tier: context` rather than guessing at its contents.

Verify each source exists and says what you attribute to it. Failures go to
`unreachable.md` with the reason.

Backward snowballing is free: while reading, scan the reference list for systems the
harvest missed and check them against `screened.csv`. Anything genuinely new is appended
to `screened.csv` first, then a `screening.csv` row with `found_via: snowball` in `note`.
Note in `RUN.md` how many that produced —
if it is many, the harvest queries need widening in v0.6.

Before writing a row, check whether the system already has a `system_id` in `papers.csv`.
Vendor platforms and conference-paper/trade-journal pairs recur under different titles, and
a second `system_id` for one system inflates every per-system count in the report.

**Gate step 5 on the audit.** Run `python3 scripts/audit.py --out "$OUT"`
now, before writing any prose. `Admitted set matches screening` is the check that catches a
step-4 that reported success and did not write. Do not start the report until it passes:
the report is the most expensive step and the most exposed to running out of budget, and a
report written over an incomplete grid has to be redone rather than repaired.

### 5. Write the report

Into `$OUT/report/`, one file per section:

| File | Content |
|---|---|
| `00_executive_summary.md` | What exists, at what maturity, in which subfields, on what evidence. ≤800 words. No recommendations |
| `01_techniques.md` | Which agentic techniques are used here and for what. Grouped by technique, not by paper |
| `02_architectures.md` | Recurring system designs, their components, and what each is chosen for. No diagrams |
| `03_applications.md` | One subsection per subfield, including the empty ones |
| `04_evaluation.md` | How systems were tested, against what baseline, on what data. Whether any shared benchmark exists or every system defines its own |
| `05_maturity.md` | The distribution of demonstrated maturity across **systems**, what separates M3+ from the rest, how often claimed exceeds demonstrated, and the abstract-only counts per subfield alongside it |
| `06_disagreement.md` | Where authors contradict each other, and on what. Omit with a one-line note if nothing does |
| `07_periphery.md` | Size and character of the excluded neighbouring literature, from harvest counts |
| `08_papers.md` | The annotated paper list — see below |
| `index.md` | Table of contents, plus the run's headline numbers |

**Write them in this order, not in file-number order: `08_papers.md`, then `07_periphery.md`,
then 01-06, then `05_maturity.md`'s counts, then `00_executive_summary.md` and `index.md`
last.** Sections 08 and 07 are the two that follow mechanically from `papers.csv` and the
harvest counts, so they are cheap and they are the sections a reader can still use if
nothing else gets written. The executive summary depends on every other section, so it goes
last; written first it can only be guesswork.

**Write one file, then confirm it exists and is non-empty, then start the next.** Do not
hold several sections in context to write in one pass. After each file:

```bash
wc -l "$OUT/report/"*.md
```

If a file is absent or empty, it was not written, whatever your notes say. This applies to
delegated section-writing with no exceptions — a subagent reporting a finished section is
not evidence that the file exists.

**How to write sections 1-6.** Anchor every paragraph on a concept and cite the several
sources bearing on it. Not "Author A built X, Author B built Y". Rather: "Multi-agent
designs typically split simulation setup from interpretation [[doi:…]] [[doi:…]], though
single-agent tool-calling is reported as sufficient for narrower inversion tasks
[[doi:…]]." State where sources agree and where they diverge, or state that the evidence
is too thin to tell. Nothing in these sections is a list of papers.

Cite with `[[identity_key]]`. Counts of systems are per `system_id`, counts of sources per
row — say which you mean every time.

**Section 08, the annotated paper list**, is a primary deliverable. Group by subfield,
then by tier:
- `core`: 4-6 lines each — what was built, what it could call, how it was evaluated, what
  it reported, demonstrated maturity, and the authors' own stated limitation.
- `context`: one line each, from the abstract, marked `[context]`.

Every admitted source appears. This is the list you will come back to. `audit.py`
does not require `[Certain]` / `[Likely]` / `[Absent-searched]` tags in
`08_papers.md` or `index.md`; citations are the evidence there. Sections 00–07 still
need tags on every substantive paragraph.

**Forbidden throughout**: gaps, opportunities, recommendations, future work. Promotional
or dismissive framing — "promising", "great potential", "revolutionise". Adjudicating
between conflicting sources, or averaging them into a consensus none of them states. If
you cannot support a statement at `[Certain]`, `[Likely]` or `[Absent-searched]`, do not
write it.

An `[Absent-searched]` claim must cite the `query_id`s that back it. Absence not backed by
logged queries is a search failure, not a finding.

### 6. Audit

```bash
python3 scripts/audit.py --out "$OUT"
```

It parses the artifacts and writes `audit.md`. Fix what it flags and re-run. **Never edit
a number so a check passes** — a failed check reported as failed is the audit working; a
check quietly reconciled leaves a run that is wrong and looks finished.

Then close `RUN.md` with: the shortlist threshold and why; the false-negative rate from
the audit sample; counts of harvested / shortlisted / screened / core / context; sources
per subfield and how many subfields came in thin; how many records had no abstract; what
the grey-literature pass reached and what it could not; what snowballing added; and what
to change in v0.6.

## Neutrality

Write for a reader you know nothing about. Do not personalise the report, address the
reader, or infer what any reader wants the answer to be. Every source is admitted or cut
on the criteria in `reference/SCHEMA.md` and nothing else — never on its authors, their
institution, or their affiliation with anything. Treat no subfield, method family, group
or system as the reference point the others are measured against; the report has no
protagonist.

## If the run must stop early

`RUN.md` records where it stopped: last step completed, last record in progress, and what
remains. The harvest and triage outputs are regenerable from `queries.json` in minutes;
`screening.csv`, `papers.csv` and `papers.md` are not. Protect those three.

Write that stop-early note **when you notice the budget running down, not when it runs
out**. If a step is partially done, say which records are in the file and which are not,
and name the file the remaining work can be restarted from. A stop between steps 4 and 5
with the audit passing is a usable result: `papers.csv` and `papers.md` are the grid and
the evidence, and the report can be written in a later run without re-harvesting or
re-screening anything. A stop that leaves `papers.csv` short of `screening.csv` is not,
which is why the audit gate above comes before the report and not after it.
