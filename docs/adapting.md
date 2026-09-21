# Using this repository for your own review

This repository is a **method**, not only a result. The subject is agentic AI in
geoscience, but nothing in `harvest.py` or the scoring knows that. If you want a
scoping review of some other literature — one whose counts you can defend, whose
shortlist cut is measured rather than assumed, and whose report cannot quietly
state a number nobody computed — you can point this at your own field.

This page is the walkthrough. Read [`architecture.md`](./architecture.md) first
if you want to know *why* it is shaped this way; read
[`../AGENTS.md`](../AGENTS.md) §A for how a run is actually driven.

**Be realistic about the effort.** A full run is ~300–440 API calls and a day or
more of human screening and deep reading. The machinery removes the
bookkeeping, not the reading.

---

## 1. What you are inheriting

One idea, and everything follows from it:

> **Split the work by whether it needs judgment, and let neither half pretend to
> be the other.**

| Deterministic → a script | Needs judgment → you (or a model) |
|---|---|
| Search, paging, deduplication | Is this record in scope |
| Ranking and the shortlist cut | What does this system actually do |
| Every count, every share | Synthesis, and what the evidence supports |
| Contract compliance | Which subfield a general record belongs to |

And one rule the whole thing exists to enforce:

> **A number is counted or it is not stated.** Where a count cannot be computed,
> the artifact says so and the page renders an em dash — a missing count must
> never look like a measured zero.

If you keep those two and throw away everything else, you have taken the useful
part.

## 2. First, prove it works on your machine

Before changing anything:

```bash
git clone https://github.com/jannablaume/deep-research-agentic-geoscience
cd deep-research-agentic-geoscience

make verify      # re-audits all three finished runs. No network, no API key
make check       # lint, types, tests. Must pass from a bare clone
```

`make verify` re-executes each run's contract audit against the artifacts
committed beside it, and additionally asserts that the regenerated `audit.md`
matches the committed one byte for byte. It is the reproducibility claim, and it
is executed rather than asserted. If it passes, your clone is sound and you have
a known-good baseline to diverge from.

## 3. Decide how much you are forking

Three runs already live here, and they are three different amounts of reuse.
Pick the closest.

| You want | Copy | You write |
|---|---|---|
| The same review, new corpus or later date | 01 | a query plan; bump the version |
| A different subject, same *shape* of question | **02** | a query plan **with a `triage` block**, a prompt, and forked `audit_`/`export_web_` scripts |
| Synthesis over runs you already have | 03 | nothing new; point `gaps.py` at your runs |

**Copy 02, not 01, for a new subject.** 01's domain vocabulary is compiled into
`scripts/triage.py`; 02's is read from its query plan. That was a deliberate
decision — see the 2026-09-11 entry in [`../decisions.md`](../decisions.md) — and
it is what makes 02 the reusable one.

### Exactly what is free and what is not

I checked each file rather than assuming:

| Component | Status for a new topic |
|---|---|
| `harvest.py` | ✅ **Free.** `--config` driven; contains no topic |
| `triage.py`'s agentic scoring | ✅ **Free.** "Is this agentic" is topic-neutral, and `triage_tango.py` imports it so it is defined once |
| `triage_tango.py` | ✅ **Free.** Domain groups, fallback and touchpoints all come from the config. Only its docstrings say TANGO |
| `audit_tango.py` | ⚠️ **Fork.** `TOUCHPOINTS`, `SUBFIELDS`, `CUT_REASONS`, `TRANSFER_COLS`, `PRESCRIPTIVE` are constants at the top of the file |
| `export_web_tango.py` | ⚠️ **Fork.** `SUBFIELDS`, `PERIPHERY`, `TOUCHPOINTS`, `CUT_REASONS`, `SECTIONS`, same place |
| `prompts/*.md` | ❌ **Write your own.** Start from `01_landscape_neutral.md` |
| `reference/SCHEMA*.md` | ❌ **Write your own** if your columns differ |

The two forks are a copy-and-edit-the-constants job, not a rewrite — the
vocabularies sit in a block at the top of each file. They are duplicated from the
schema deliberately, to fix facet **order**: a facet ordered by `Counter` alone
is ordered by whatever this run happened to find, so a value that drops to zero
next run vanishes from the axis instead of showing a zero, and two runs stop
being comparable. See [`architecture.md`](./architecture.md) §14.

**Note the one thing a fresh clone cannot run: `prompts/02_tango.md`.** It hard-
depends on `tango_complete_reference.md`, which is gitignored because it carries
an unpublished commercial roadmap, and the prompt stops if it is absent. That is
the honest behaviour — you cannot reproduce the 02 *run* — but 02's **scripts and
query plan are fully available** and are the pattern to copy.
`prompts/01_landscape_neutral.md` is the prompt template that runs from a clone.

## 4. Write the query plan

This is the main event, and usually the only file you need before your first
harvest.

```bash
cp reference/queries_template.json reference/queries_mytopic.json
```

The template is annotated, topic-neutral and **validates as shipped**. Its
`bands` block — the technique axis, the agentic and LLM vocabulary — is reusable
verbatim unless you are reviewing something other than LLM-based systems. Its
`domain_groups` and `triage` blocks are marked `REPLACE`.

The full contract is [`../reference/SCHEMA_queries.md`](../reference/SCHEMA_queries.md).
The short version:

- **Two axes.** `bands` (technique) × `domain_groups` (subject). One query per
  scope × group × band.
- **`core` is deep-read, `periphery` is counted.** Keep at least one periphery
  group or the periphery section cannot be written from harvest counts.
- **Every term is a single phrase.** A bare `AND`/`OR`/`NOT` inside a term makes
  OpenAlex return zero results *with no error*; `harvest.py` refuses to start
  rather than harvest nothing.
- **The `triage` block's keys must match `domain_groups` exactly.** A group
  harvested with no triage pattern is dropped from the shortlist without
  appearing in any count. That shape cost 190 records once and was invisible in
  every number.
- **Aim each group at recall.** Screening narrows later; a record never
  harvested cannot be recovered by any downstream knob.

Then, before spending anything:

```bash
python3 scripts/harvest.py --out outputs/04_mytopic/v0.1 --dry-run \
    --config reference/queries_mytopic.json
```

`--dry-run` builds and validates the plan, prints every query with its id, and
calls nothing.

## 5. Get a key, then smoke-test

Get a free [OpenAlex key](https://openalex.org) and put it in `.env`. It is
effectively required: OpenAlex meters a daily USD budget — $0.10 keyless, $1 with
a key — and a full harvest is a few hundred calls. Keyless, a run aborts partway
through, and `harvest.py` refuses to retry a spent budget because retrying turns
one loud failure into a quiet half-corpus that every later count trusts.

Ship a smoke config — a **verbatim subset** of your plan with a lowered
`openalex_max_pages` — and run three cells, one of them periphery:

```bash
python3 scripts/harvest.py --out outputs/04_mytopic/v0.1-test --no-s2 \
    --config reference/queries_mytopic_smoke.json
python3 scripts/triage_tango.py --out outputs/04_mytopic/v0.1-test \
    --config reference/queries_mytopic.json --audit-n 40
```

**`--limit-queries N` is not a smoke test.** The plan emits core groups first, so
a truncated plan harvests zero periphery.

The smoke run is also where you discover how hard your domain filter actually
filters. 01 asks "is this one of ten solid-earth subfields", which most agent
papers fail, and shortlisted 6%. 02 asks "is this computational", which most
agent papers pass, and shortlisted 42% at the same thresholds. If your subject
axis is broad, `--min-domain` will be your binding knob, not `--min-score`.

## 6. Harvest, triage, and settle the thresholds honestly

```bash
python3 scripts/harvest.py      --out $OUT --no-s2 --config reference/queries_mytopic.json
python3 scripts/triage_tango.py --out $OUT --config reference/queries_mytopic.json
```

**Read `triage_stats.md` before touching a threshold.** The cut is an AND of
several conditions, so a table that varies only `--min-score` hides which one is
binding. If a row is flat across `min-score`, lowering it will change nothing —
twice in this repository's history the binding filter was structural rather than
the score.

## 7. Screen — including the sample from *below* the cut

A shortlist is a claim that the records beneath it did not matter, and that claim
is usually untested. `triage_tango.py` draws a seeded random sample from below
the cut and writes it in the same digest format as the shortlist.

**Screen it exactly as you screen the shortlist.** Any record in it you would
have admitted is a false negative, and that measurement is the entire difference
between a cut that is measured and a cut that is assumed. Above 5%, diagnose
which condition is binding before widening anything.

## 8. Write, with evidence tags

Every substantive paragraph carries its evidential status as its first token:

| Tag | Means |
|---|---|
| `[Certain]` | Stated in a source you read, and quoted in `papers.md` |
| `[Likely]` | Supported but inferred, or read from an abstract only |
| `[Absent-searched]` | Looked for and not found — **must cite the query id** that looked |

An absence you did not search for is not a finding, and the audit fails a run
that claims one without a query id.

## 9. Fork the audit, and keep it a gate

Copy `audit_tango.py`, edit the vocabulary constants, and keep its spirit:

> Checks get **added, never removed or softened to go green.** A gate that passes
> because it stopped checking is worse than an honest failure.

That is not decoration. `audit.py` exists because a previous version ended with a
self-audit table the model filled in, which was reliably green and occasionally
wrong — a long run gets compacted, and the compliance it is attesting to happened
before the compaction. Every check is now executed against the files on disk.

Keep the two **vacuity guards** in particular (`papers.csv is non-empty`,
`screening.csv is non-empty`). With no admitted sources every other check holds
trivially, and the table reads as a clean run that produced nothing.

If you add checks, keep the mutation tests: one fixture writes a run that passes
everything, and each test breaks exactly one thing and asserts that exactly the
corresponding check fails. A check that stops failing when its condition is
broken has become decoration, and that is invisible from a green run.

## 10. Export and publish

```bash
python3 scripts/export_web_mytopic.py --out $OUT     # your fork
make web                                             # → web/dist/
```

The front end reads **one** JSON document and nothing else — it never reads a
CSV, never parses report markdown and never fetches at runtime. That is what
makes `web/dist/` something you can zip and email: a copy of the folder is a copy
of the data, and it opens by double-clicking with nothing installed.

---

## Rules worth keeping

**A committed run is evidence.** Do not reformat one, do not let a formatter trim
its whitespace, and do not edit a number in it to match a later recount — write a
new version instead. `.editorconfig`, `.pre-commit-config.yaml` and
`pyproject.toml` all exclude `outputs/` for this reason.

**Do not edit 01's scripts.** `harvest.py`, `triage.py` and `audit.py` produced
the v0.5 landscape. A script two runs share is a script whose next edit silently
re-measures the earlier one.

**A scoring change is a method change.** It alters what a re-run admits, so it
belongs in a version bump with a re-triage and a decision-log entry, never folded
into a refactor.

**Commit the prompt and its output together.** A run whose prompt is not in the
same commit is not reproducible. Record the prompt commit in `RUN.md`.

**Write down what a decision rules out.** That clause is what stops it being
relitigated every version, and it is the most transferable habit here.

## Traps that cost this project real time

Each of these was paid for once already:

- **`ReAct` matched case-insensitively** produced 377 false positives in a
  1,795-record corpus. `react` is what chemicals do.
- **Bare `MCP`** is monocyte chemoattractant protein. Match it only beside a
  system noun or as the tail of a hyphenated tool name.
- **Generic agent vocabulary needs independent LLM vocabulary.** "Multi-agent
  system" is forty years old, "copilot" is an aircraft, "tool use" is
  primatology. Without corroboration they promote 1990s work into an LLM-era
  shortlist.
- **A paging cap is invisible unless you record the API's own count.** Store it
  next to the number you actually pulled and mark the query `TRUNCATED`, or your
  periphery section reports the cap rather than the size of a literature.
- **A zero-result query and a malformed query look identical downstream.** They
  are distinguishable only at the call site. Record `status: zero` there and fail
  the run on it.
- **Preprint and published versions are different documents.** Three of six
  preprint-to-published pairs checked here had materially diverged. If you read
  a substitute, say so in the row rather than once in a methods note.

## Licence, citation and credit

MIT for the scripts — reuse them freely. The report prose and the CSV artifacts
under `outputs/` are CC BY 4.0. Bibliographic metadata is from
[OpenAlex](https://openalex.org) (CC0) and [arXiv](https://arxiv.org); abstracts
remain under their publishers' terms.

If the method is useful, cite it: see [`../CITATION.cff`](../CITATION.cff). Cite
the version you used — each directory under `outputs/` is immutable and carries
its own `RUN.md`.

If you adapt this and find a trap of your own, a pull request that adds it to this
list is the most useful contribution you can make.
