---
name: 03_gaps
description: Synthesise every research gap the finished 01_landscape and 02_tango runs already contain. Extracts candidates mechanically from the reports and the grids, clusters them, and sends a verification agent after each one before it is stated. Synthesis only — no reasoning about why a gap matters or what to do about it.
---

# 03 — The gaps the finished runs already contain

Version: v0.1

Read the finished runs and state, in one document, **what they record as absent,
unstated, unevaluated, unread or empty** — each gap traced to the artifact it came from
and checked against the literature before it is stated.

**Synthesis, not reasoning.** A gap here says what is missing and where that was
recorded. It does not say why it matters, what should be done about it, which gaps are
larger, or what anyone should work on next. `audit_gaps.py` fails the run for the common
forms of that; the rule is wider than the grep.

This is deliberate and it is not laziness. The runs measured a literature; ranking what
is missing is an argument, and an argument mixed into a file of measurements is
indistinguishable from one afterwards.

## Setup

Resolve the output directory first. Default is `outputs/03_gaps/v0.1/`. If it exists, use
`v0.1-run2`, `-run3`, … Record the resolved path on line 1 of `RUN.md`, and substitute it
for `$OUT` below.

Read `reference/SCHEMA_gaps.md` now. It defines `gaps.md`'s block format, the verdict
vocabulary and the discard ledger, and `audit_gaps.py` parses all three.

Then establish **which runs you are reading and at what commit**:

```bash
git log -1 --format='%h %ad %s' -- outputs/01_landscape/v0.5 outputs/02_tango/v0.1
git status --short outputs/
```

Record both in `RUN.md`. A gaps document is a statement about two specific runs, and
uncommitted changes under `outputs/` mean the thing you read is not the thing anyone else
will read.

## The four rules

1. Every gap traces to a `candidate_id` from `gap_candidates.csv`. Nothing enters this
   document because you know it about the field.
2. Every gap carries a verdict that a **verification pass returned**, not one you
   assigned. A gap nobody checked is `undecidable`.
3. Every candidate is accounted for — cited by a gap, or in the discard ledger with a
   reason. A candidate that quietly vanishes is indistinguishable from one nobody read.
4. Append as you go and verify against the file. **One writer per file**: subagents read,
   search and report; this session writes.

## Procedure

### 1. Extract the candidates — deterministic, no judgment

```bash
OUT=outputs/03_gaps/v0.1
python3 scripts/gaps.py --out "$OUT" \
    --run outputs/01_landscape/v0.5 \
    --run outputs/02_tango/v0.1
```

This writes `gap_candidates.csv` and `gap_candidates.md` and reads seven shapes out of
the runs: authors' own stated limitations, `[Absent-searched]` claims with their query
ids, `not stated` columns with denominators, evaluations with no baseline or no held-out
set, empty subfields and touchpoints, sources nobody could read, and systems whose claimed
maturity exceeds what they demonstrated.

If a run directory is missing, run 03 against the ones that exist and say so in `RUN.md`.
A gaps document over one run is a usable result; a gaps document that pretends to cover
two is not.

**Do not edit `gap_candidates.csv`.** If a candidate looks wrong — a limitation cell that
is really a metadata artefact, a count whose denominator makes no sense — that is a
finding about the run it came from. Record it in `RUN.md` and discard the candidate in the
ledger with `run-artefact`.

### 2. Read the runs' own prose

Read both runs' `report/*.md` end to end before clustering anything. The candidates are
the skeleton; the reports are where a run said in prose that the evidence was too thin to
tell, that two sources disagreed, or that a section could not be written. That last kind
never appears in a CSV cell.

Also read, in each run: `RUN.md` (what broke, what was left undone), `unreachable.md`,
and — for 02 — `paywalled.md` and `transfer.csv`.

### 3. When something is unclear, send an agent

Do not resolve an ambiguity by assuming. Where a candidate's meaning depends on something
you cannot see from the artifact — what a limitation cell actually referred to, whether
two systems are the same system under two names, whether a `not stated` is the source's
silence or the run's omission — **dispatch a subagent to check it against the files** and
report back.

Brief it with: the candidate id, the exact question, the files to look in, and what an
answer looks like. Ask for the quote and the file it came from, not a conclusion.

Then verify what it returns. An agent that reports a finding without a quote and a file
path has not checked anything, and its summary is not evidence. That failure has happened
in this repository before: a subagent returned a completed screening pass in 2.8 seconds
having written nothing.

### 4. Cluster into gaps

Group candidates that say the same thing into one gap. A gap that rests on one system's
own limitation and nothing else is usually `too-specific` — discard it and say so, unless
the verification pass finds it is the whole field's.

Write each block in the `reference/SCHEMA_gaps.md` shape, with the verdict line left as
`verdict: pending` until step 5 returns. Write `gaps.md` incrementally, a few blocks at a
time, and check the file after each batch:

```bash
grep -c '^## G' "$OUT/gaps.md"
```

**The paragraph under each block restates its candidates and nothing else.** If a sentence
is not a restatement of something cited on the `candidates` line, it does not belong. The
temptation here is to explain — resist it; explanation is what the next run is for.

### 5. Verify every gap, with an agent, before stating it

For each gap, dispatch a verification subagent. Its job is to find out whether the gap is
**actually a gap in the literature**, or only a gap in what these two runs harvested and
read. Those are different things, and the difference is the whole value of this step.

Brief each agent with: the gap statement, its candidate ids and their `evidence_ref`s, and
this instruction — *search for work that would refute it*. Tell it to search, in order:

1. The runs' own corpora: `outputs/*/screened.csv` and `triage.csv` hold every harvested
   record with its abstract, including everything screened out. A gap refuted by a record
   the run cut is the most informative outcome there is.
2. The bibliographic APIs, with `scripts/harvest.py --dry-run` to see how a query is built,
   or direct queries against OpenAlex and arXiv.
3. The open web, for grey literature and code releases.

It returns: what it searched (queries, verbatim), what it found (`identity_key`s or URLs),
and one verdict — `confirmed-absent`, `partially-addressed`, `refuted`, `undecidable`.

You write both `verification.md` and the verdict line in `gaps.md`; the agent writes
nothing. Two rules on what you write:

- **A verification that searched nothing returns `undecidable`,** whatever the agent
  concluded. An absence nobody looked for is not a finding — the same rule both other runs
  apply to `[Absent-searched]`.
- **A `refuted` verdict is a result, not a failure.** Keep the block, record what refuted
  it, and move the candidate to the discard ledger with `refuted`. A gaps document that
  only contains gaps that survived is a document that has hidden its own error rate.

Run these in parallel where they are independent — they are read-only and they do not
share a file. One agent per gap, not one per candidate.

### 6. Close the ledger and audit

Add `## Discarded candidates` to the end of `gaps.md`: one line per unused candidate with
a reason from `reference/SCHEMA_gaps.md`. Then:

```bash
python3 scripts/audit_gaps.py --out "$OUT"
```

`Every candidate is used or discarded with a reason` is the check that catches a clustering
pass that dropped half its input. Fix what it flags and re-run. **Never edit a number, or
delete a candidate, so a check passes.**

Close `RUN.md` with: which runs were read and at what commit; candidates by kind; gaps by
verdict; discards by reason; how many gaps the verification pass refuted or could not
settle; and what to change in v0.2.

## Forbidden

Reasoning about the gaps: why one matters, what it would take to close it, which is
largest or most tractable, what anyone should do next. No research agenda, no roadmap, no
prioritisation, no "opportunity".

Also forbidden: a gap with no candidate; a verdict you assigned rather than received; a
candidate deleted instead of discarded; promotional or dismissive framing; and any claim
about a run you did not read in this session.

The honest framing for everything in this document is *these two runs record X, and a
verification pass looking for Y found Z*. Nothing here is a claim about the field that is
not one of those.
