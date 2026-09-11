---
name: 02_tango
description: Scoping review of agentic systems that drive a simulator, solver, optimiser or scientific code — the control patterns relevant to making TANGO agentic. Harvests its own corpus, screens it, deep-reads the core set, and writes a neutral report plus a per-system record of what each system actually drives.
---

# 02 — What exists that bears on making TANGO agentic

Version: v0.1

Map what has been built in **agentic systems that drive a simulation, solver, optimiser,
scientific code, or engineering and techno-economic model**: the control patterns, the
architectures, how they were evaluated, how mature they are, and which of TANGO's own
surfaces they touch.

**Descriptive only.** This run says what exists and what each system was shown to do. It
does not say what TANGO should build, in what order, or whether any of it would work
here. `audit_tango.py` fails the run for a sentence that does — see *Forbidden*.

## What TANGO is, for the purposes of this run

Read `tango_complete_reference.md` (repo root) now, before anything else. It is the whole
description of TANGO available to this run: a YAML-driven `networkx.DiGraph` of physical
units, orchestrating third-party physics engines (TESPy, CoolProp, MOOSE, DWSIM, CMG)
through a time-stepped solve with a Newton boundary-condition iterator, pymoo
optimisation, LHS + DVC + SLURM parameter sweeps on ETH Euler, GPR surrogates, LCOE and
CAPEX economics, an LCOE regression suite, and an optional Flask/React tier.

Two things about that file matter for how you use it:

- It is **a note, not the code.** Its §9 lists what was never verified, including the
  actual state of the refactor branches. Do not treat anything in it as a measurement,
  and do not go looking for the `tango-core` repository — it is not in this repository
  and nothing in this run depends on it.
- It is the source of the **touchpoint list** in `reference/SCHEMA_tango.md`. The
  touchpoints are TANGO's surfaces, and tagging a source with one is a claim about
  *that source*, never about TANGO.

If `tango_complete_reference.md` is absent, stop and say so. The touchpoint column is
uninterpretable without it, and guessing at what TANGO is would make every row in
`transfer.csv` a fabrication.

## Setup

Resolve the output directory first. Default is `outputs/02_tango/v0.1/`. If it exists,
use `v0.1-run2`, `-run3`, … A mechanics test uses `v0.1-test` (see Smoke test below).
Never write into a directory that already has `screening.csv`. Record the resolved path
on line 1 of `RUN.md`, and substitute it for `$OUT` in every command below.

Read `reference/SCHEMA.md` and then `reference/SCHEMA_tango.md` now, and both again
before step 4. The second one is short and only records what differs; the first is where
the columns, the tiers and the maturity rubric actually live.

## Smoke test (before a full run)

Do this once after editing the prompt or the scripts, in a fresh
`outputs/02_tango/v0.1-test/` (or `-test2` if that exists). It is not a landscape.

```bash
OUT=outputs/02_tango/v0.1-test
python3 scripts/harvest.py      --out "$OUT" --no-s2 --config reference/queries_tango_smoke.json
python3 scripts/triage_tango.py --out "$OUT" --min-score 3 --audit-n 40
```

`reference/queries_tango_smoke.json` is three query cells — two core, one periphery — so
periphery counting is exercised. `--limit-queries N` cannot do that: the plan is core
groups first, so the first N rows are all core and `07_periphery.md` could not be written
from harvest counts at all. **Triage always reads the full config**, not the smoke one:
the smoke corpus is small, but records in it can still belong to any group.

Then screen the shortlist, screen the 40-record audit sample, deep-read 2–3 arXiv core
papers, write `transfer.csv` and `transfer.md` for them, write the ten report files (they
will be thin), and run `audit_tango.py`. Do not apply the shortlist band in step 1. Do not
write absence findings about the field.

If harvest, triage, `screening.csv`, the `papers.md` and `transfer.md` extracts, report
tags and `audit_tango.py` all complete, the prompt is runnable. Then start a full run in a
**new** directory.

## The five rules

1. Nothing is written unless a tool call **in this run** retrieved it. No counts, no
   citations, no CSV cells from recall. A remembered paper must be found in the corpus
   before it can be used. This includes anything you think you know about TANGO that is
   not in `tango_complete_reference.md`.
2. Quote before you characterise. Every claim about a system traces to a verbatim extract
   in `papers.md`; every touchpoint traces to one in `transfer.md`.
3. Every substantive paragraph in the report carries `[Certain]`, `[Likely]` or
   `[Absent-searched]`.
4. Append as you go — `screening.csv`, `papers.csv`, `papers.md`, `transfer.csv`,
   `transfer.md`, `paywalled.md` — never only at the end. This run will be summarised and
   compacted several times. **One writer per file.** If you delegate, delegate the reading
   and have the parent write, in batches, verifying each against the file.
5. Report failures as failures. A step that did not work, said plainly, is worth more than
   a plausible-looking substitute.

## Scope

**In**: an LLM or foundation model **decides something for itself** — picks a tool, plans
a sequence, iterates on its own output, calls code and acts on the result — **and what it
acts on is a simulator, solver, optimiser, scientific code, or an engineering or
techno-economic model.**

The physics does not matter and the domain does not matter. A flowsheet agent for a
chemical plant, a mesh-refinement agent for a CFD solver and a well-placement agent for a
geothermal doublet are the same object for this run: an agent, a loop, and an engine it
does not itself implement. That is exactly TANGO's shape, which is why this corpus is
domain-agnostic where the 01 corpus was solid-earth.

**Out**: prompt-in/text-out applications with no decision loop; pre-LLM agent work
(multi-agent systems, agent-based models, RL controllers, expert systems) except where a
source in scope builds on it; a machine-learned surrogate with no agent deciding anything
— a GPR emulator is a model, not an agent; anything before November 2022.

**Periphery** — software engineering, laboratory and robotic automation, web/GUI/computer-use
agents, literature and writing agents: harvested and counted, never deep-read. One report
section reports their size and character from the harvest counts.

Software-engineering agents are periphery **by decision**. They are the largest agent
literature there is, and this run is about an agent driving TANGO, not an agent
refactoring it. Record the count; do not read them.

## Overlap with the 01 run is expected, and is not a duplicate

`outputs/01_landscape/v0.5/papers.csv` holds 155 admitted sources, some of which will be
harvested again here. That is not a problem and they are not `duplicate` cuts: the two
runs ask different questions of the same paper. Screen each on this run's criteria alone.

When a source is admitted in both, use **the same `system_id`** as the 01 run so the two
grids can be joined. Note the overlap count in `RUN.md`; it is a measurement of how much
of the subsurface literature is also simulator-driving work, and nothing else.

## Procedure

### 1. Harvest — deterministic, no judgment

```bash
python3 scripts/harvest.py      --out "$OUT" --no-s2 --config reference/queries_tango.json
python3 scripts/triage_tango.py --out "$OUT" --min-score 3
```

22 query cells against two APIs. Read `triage_stats.md`. On a **full** harvest, if the
shortlist is under 150 or over 800, adjust the thresholds and re-run `triage_tango.py` — it
costs no network call. That band does not apply to the smoke config. Record the thresholds
you settled on and why in `RUN.md`.

**Expect to have to tighten, and expect `--min-domain` to be the knob that does it.** The
01 defaults will not hold here. Measured on the v0.1 smoke corpus — 3 of the 22 cells,
A_agentic only, 1,325 records — `--min-score 3 --min-strong 1 --min-domain 1` shortlisted
557, or 42%. The 01 run shortlisted 6% of its corpus. The difference is not that this
literature is more agentic: it is that 01's domain filter asks "is this one of ten
solid-earth subfields", which most agent papers fail, and this one asks "is this
computational", which most agent papers pass.

`--min-domain` requires N domain-vocabulary hits rather than one. On the smoke corpus it
took the shortlist 557 → 301 → 169 at 1 → 2 → 3. It is not free: at 2 it also drops
records whose abstract mentions its engine once, and on the smoke corpus those included an
LLM workflow for analog circuit sizing that runs a simulator in its optimisation loop.
**That is what the audit sample is for** — raising the threshold moves those records into
the pool it is drawn from, so the cost is measured rather than assumed. Settle the
thresholds, then screen, and report both the settings and the false-negative rate they
produced.

`triage_stats.md` carries a touchpoint table this run's stats have and 01's do not. It is
a regex over titles and abstracts and it is **a sorting aid**: a touchpoint with zero
shortlisted records is a fact about how abstracts are written, not about what exists.
Never carry a number from that table into the report as a count of systems.

Do not re-run `triage_tango.py` after `screening.csv` exists. The script refuses unless
`--force`, and `--force` requires re-screening the new shortlist and audit sample from
scratch — otherwise the false-negative rate you report is measured against a sample file
that is no longer on disk.

If any query reports `status: zero`, it is malformed, not empty. Fix
`reference/queries_tango.json` and re-harvest that band.

Do not add web searches at this stage. Web search is for step 3 only.

### 2. Screen

Read `shortlist.md` top to bottom. One `screening.csv` row per record, per
`reference/SCHEMA.md` with the 02 `cut_reason` and `subfield` vocabularies from
`reference/SCHEMA_tango.md`. Batch it: write rows every ~50 records, not at the end.

**Do this yourself, in this session.** Do not hand screening to a subagent: it is the
judgment this whole run rests on, and a delegated pass returns a summary you cannot check
against the records that produced it.

**Verify every batch against the file, not against your memory of writing it:**

```bash
wc -l "$OUT/screening.csv"
```

The count must rise by the size of the batch you just wrote. If it did not, the rows were
not written — say so and write them. This applies with no exceptions to any work you
delegate anywhere in this run: an agent that reports success while the file it was told to
create is absent or unchanged did not do the work, and its summary is not evidence that it
did.

The judgment call that matters most here is **`no-simulation-target`**, and it is not the
same line as 01's `not-agentic`. The system can be fully agentic and still be cut: an
agent that plans a literature search, writes code, or files a pull request decides plenty
for itself and drives nothing this run is about. Ask what the agent's actions land on. If
the answer is a document, a repository, a browser or a robot arm, it is out or periphery.

Then screen `audit_sample.md` the same way, with `from_audit_sample: yes`. Any you mark
`in` is a false negative in the ranking. Report the rate in `RUN.md` whatever it is.

**If the rate exceeds ~5%, diagnose before you widen.** This run has three candidate
binding cuts, not two:

- `strong_hits` **is 0** — no agent vocabulary at all. Lowering `--min-score` admits
  nothing; the fix is a vocabulary one, and it lives in `triage.py`'s `AGENT_COMPOUND`,
  which **this run shares with the 01 run**. Changing it is a method change for both.
- `strong_hits` **≥ 1 but the score is below the cut** — the score is binding. Lower
  `--min-score`, re-run, screen the new records.
- `domain_score` **is below `--min-domain`** — the record names its engine once and you
  tightened the domain knob to get the shortlist into band. Check how many of the false
  negatives share that shape before lowering it: the remedy may be a better domain pattern
  rather than a lower threshold, and lowering it costs a few hundred records to screen.
- `scope_computed` **is `none`** — the record is agentic and the domain vocabulary in
  `reference/queries_tango.json` did not recognise what it drives at all. This is the
  failure this run is most exposed to, because its domain is the whole of computational
  science and the vocabulary was written before the corpus existed. Add the missing pattern
  to the `triage.core` block, re-run, screen the new records.

Record in `RUN.md` what you diagnosed, what you changed, and the rate before and after.

### 3. Fill the gaps the APIs cannot reach

Bibliographic APIs do not index grey literature, and a large share of simulator-agent work
is released as code or written up by vendors. Spend up to **40 web searches or fetches**
here, no more, logged by appending rows to `queries.csv` with `api: web`. The venue list
is in `reference/queries_tango.json` under `venue_hints`.

Most of this is not peer-reviewed and some of it is marketing. Admit it as
`source_type: whitepaper` or `repo`, `tier: context`, unless the visible material —
including a repository's own README, tests and examples — genuinely supports a `core`
write-up. A repository with no evaluation of any kind is `M0` or `M1` and says so.

A grey or snowball source not already in `screened.csv` must be appended there first (same
columns as `harvest.py`; `source_apis: web`; `identity_key` by the harvest rules in
SCHEMA.md). Only then add a `screening.csv` row, with `found_via: grey` or
`found_via: snowball` in the `note`.

### 3a. The paywall handoff — stop here, once

Before step 4, write `paywalled.md` for every source you already know you cannot read, per
`reference/SCHEMA_tango.md`. Two things first:

- **Check the local PDF stores first.** Two of them hold files retrieved by hand for the
  01 run: `paywalled_paper/` in this repository, and `~/Downloads/paywalled_paper_2/`.
  A source sitting on disk is not unreachable; read it from there and record
  `local_pdf: <filename>`. Match on the DOI or the publisher's article id — the
  filenames are publisher exports (`1-s2.0-S0043135426005683-main.pdf` is a
  ScienceDirect PII, `tle44020142.1.pdf` is a DOI suffix), not titles, so a filename
  that means nothing to you may still be the paper you are looking for.
- **Check `previous_paywalled_paper.md`** (repo root) and
  `outputs/01_landscape/v0.5/unreachable.md`. What defeated the 01 run will defeat this
  one, and a route already known to fail is not worth spending a fetch on.

Then **stop and hand the list over.** Say plainly: how many sources are blocked, what they
would change if read (the `would_change` column), which of them already have a local PDF,
and which need credentials. Wait for an answer.

This is the one deliberate pause in the run. It exists because the person running it may
have institutional access that this session does not, and because a source demoted to
`context` for want of a login is a measurement error that is cheap to fix *before* the
report is written and expensive after.

If the answer is to carry on without them, carry on: demote them to `tier: context` with
`access_status: abstract-only`, keep every row in `paywalled.md`, and say in `RUN.md` what
the demotions cost. Do not try to breach a paywall, and do not let a delay here stall the
run indefinitely — if there is no answer, proceed and record that you proceeded.

### 4. Deep-read the core tier

For each `tier: core` record: fetch the full text, read it — **especially the evaluation,
limitations and future-work sections** — then in the same step write all four of its
records: the `papers.csv` row, the `papers.md` extract block, the `transfer.csv` row and
the `transfer.md` block. Never split those into separate passes: the extracts need the
text in front of you and are the expensive half.

For arXiv, fetch `arxiv.org/html/<id>`, not `/pdf/` — the PDF route fails on size limits
and undecompressable text. If the unversioned path returns nothing, append the version:
`arxiv.org/html/2601.06776v1` is what worked when the bare id did not. The abstract page
is not a substitute — on that same paper it answered four of five extraction questions
with nothing, and the HTML full text answered all five. If a full text cannot be read for
tool reasons, that is not an access barrier: record it as a tooling failure in `RUN.md`
and in `paywalled.md` with `blocked_by: tooling-failure`, and downgrade the record to
`tier: context`.

Three fields carry this run and are the ones most often fudged:

- **`what_it_drives`** must name a thing. "A simulator" is not an entry; "an Aspen Plus
  flowsheet", "OpenFOAM case files", "a SPECFEM3D input deck" are. If the source never
  names what it drove, that is `not stated`, and it is a finding about the source.
- **`autonomy`** is rated from the evaluation section only. A system described as
  autonomous in its abstract and run by hand in its experiments is
  `suggests`, and the gap goes in `maturity_claimed` versus `maturity_demonstrated`.
- **`failure_handling`** is where this literature is thinnest and where TANGO's own
  regression experience says the difficulty lives. Record what the authors say happens
  when the driven code does not converge or returns nonsense, in their terms. `not stated`
  is the expected entry and it is worth counting.

Verify each source exists and says what you attribute to it. Failures go to
`unreachable.md` with the reason, and to `paywalled.md` when someone else could open it.

Backward snowballing is free: while reading, scan the reference list for systems the
harvest missed and check them against `screened.csv`. Note in `RUN.md` how many that
produced — if it is many, the queries need widening in v0.2.

Before writing a row, check whether the system already has a `system_id` in `papers.csv`
**or in `outputs/01_landscape/v0.5/papers.csv`**. Vendor platforms and
conference-paper/preprint pairs recur under different titles, and a second `system_id` for
one system inflates every per-system count in the report.

**Gate step 5 on the audit.** Run `python3 scripts/audit_tango.py --out "$OUT"` now, before
writing any prose. `Admitted set matches screening` and `transfer.csv covers the admitted
set exactly` are the checks that catch a step-4 that reported success and did not write.
Do not start the report until they pass.

### 5. Write the report

Into `$OUT/report/`, one file per section, per the table in `reference/SCHEMA_tango.md`.

**Write them in this order, not in file-number order: `08_papers.md`, then
`03_touchpoints.md`, then `07_periphery.md`, then 01, 02, 04, 05, 06, then
`00_executive_summary.md` and `index.md` last.** Sections 08, 03 and 07 follow
mechanically from `papers.csv`, `transfer.csv` and the harvest counts, so they are cheap
and they are what a reader can still use if nothing else gets written. The executive
summary depends on every other section.

**Write one file, then confirm it exists and is non-empty, then start the next.** After
each file:

```bash
wc -l "$OUT/report/"*.md
```

If a file is absent or empty, it was not written, whatever your notes say.

**How to write sections 01–06.** Anchor every paragraph on a concept and cite the several
sources bearing on it. Not "Author A built X, Author B built Y". Rather: "Systems that
emit a whole input file are reported for flowsheet and reservoir setups
[[doi:…]] [[doi:…]], while systems that patch an existing one are reported where the
configuration is large enough that regenerating it loses information [[doi:…]]." State
where sources agree and where they diverge, or state that the evidence is too thin to
tell.

Cite with `[[identity_key]]`. Counts of systems are per `system_id`, counts of sources per
row — say which you mean every time.

**Section 03, the touchpoints**, is this run's primary deliverable alongside the paper
list. One subsection per touchpoint in the controlled list, **including every touchpoint
no source matched**, which is written as an `[Absent-searched]` paragraph citing the query
ids that looked. For each populated touchpoint: how many systems, what they drove, at what
autonomy, evaluated how, and what the authors said broke. Nothing in this section says
what TANGO should do with it.

**Section 08, the annotated paper list**, is a primary deliverable. Group by subfield, then
by tier: `core` 4–6 lines each — what was built, what it could call, how it was evaluated,
what it reported, demonstrated maturity, and the authors' own stated limitation. `context`
one line each, from the abstract, marked `[context]`. Every admitted source appears.

### 6. Audit

```bash
python3 scripts/audit_tango.py --out "$OUT"
```

It parses the artifacts and writes `audit.md`. Fix what it flags and re-run. **Never edit a
number so a check passes.**

Then close `RUN.md` with: the shortlist threshold and why; the false-negative rate and
which cut was binding; counts of harvested / shortlisted / screened / core / context;
sources per touchpoint and how many touchpoints came in empty; how many admitted sources
overlap the 01 run; how many records had no abstract; what the paywall handoff recovered
and what it did not; what the grey pass reached; what snowballing added; and what to change
in v0.2.

## Forbidden

**Prescription.** No sentence that says what TANGO should build, adopt, prioritise or
avoid. No roadmap, no recommendation, no "this would fit TANGO well", no ordering of the
touchpoints by how valuable they would be. `audit_tango.py` greps for the common forms and
fails the run; the rule is wider than the grep, and the grep is not the specification.

The line to hold: **describing what a system did is the job; judging what TANGO should do
about it is the reader's.** "Three systems generate a complete input file and validate it
against a schema before running it [[…]]" is the report. "TANGO could generate its YAML
this way" is not, however obviously true it seems.

**Also forbidden**: gaps, opportunities, future work — those are run 03's job and doing
them here corrupts both. Promotional or dismissive framing — "promising", "great
potential", "revolutionise". Adjudicating between conflicting sources, or averaging them
into a consensus none of them states. Any claim about TANGO's own capabilities beyond what
`tango_complete_reference.md` states, and any claim at all about the state of its refactor
branches — that file's §9 says they were never verified.

An `[Absent-searched]` claim must cite the `query_id`s that back it. Absence not backed by
logged queries is a search failure, not a finding.

## Neutrality

Write for a reader you know nothing about, including one who has never heard of TANGO.
Every source is admitted or cut on the criteria in `reference/SCHEMA_tango.md` and nothing
else — never on its authors, their institution, or whether the work is close to home.
Treat no domain, method family or group as the reference point the others are measured
against; the report has no protagonist, and TANGO is not one either. TANGO defines the
touchpoint vocabulary. It is not the subject of the report.

## If the run must stop early

`RUN.md` records where it stopped: last step completed, last record in progress, and what
remains. The harvest and triage outputs are regenerable from `reference/queries_tango.json`
in minutes; `screening.csv`, `papers.csv`, `papers.md`, `transfer.csv`, `transfer.md` and
`paywalled.md` are not. Protect those six.

Write that stop-early note **when you notice the budget running down, not when it runs
out**. A stop between steps 4 and 5 with the audit passing is a usable result: the grids
and the extracts are there, and the report can be written in a later run without
re-harvesting or re-screening anything. A stop that leaves `papers.csv` or `transfer.csv`
short of `screening.csv` is not, which is why the audit gate comes before the report.
