# AGENTS.md

The single source of truth for anyone working in this repository, human or agent.
`CLAUDE.md` and `GEMINI.md` are pointers here and hold no content of their own.

**There are three jobs in this file.** Producing the landscape run is §A. Producing
either of the other two runs is §A2, which is written as a delta against §A and does
not repeat it. Changing the scripts is §B. Read the one you are here for; they need
almost nothing from each other.

One rule spans both, and it is the rule this repository exists to enforce:

> **A number is counted or it is not stated.** Nothing here estimates, rounds up
> from memory, or reports a cap as a measurement. Where a count cannot be
> computed, the artifact says so and the page renders an em dash — a missing
> count must never look like a measured zero.

---

# §A — Producing a landscape run

## A1. Understand what the run is before starting one

This is a **scoping review**: what has been built, how it was evaluated, how
mature it is. **Descriptive only.** No gap analysis, no research agenda, no
recommendation about what the field should do next. If you find yourself writing
a sentence about what is *missing* and why that matters, you have left the scope
— the exception is an `[Absent-searched]` claim, which is a measurement (see A6).

The current landscape is **v0.5**. `v0.2`, `v0.4` and the `-test` directories are
method tests, not landscapes. Do not read numbers out of them.

## A2. The split, and why you are not doing half of this

| Deterministic → **a script** | Needs judgment → **the model** |
|---|---|
| Search, paging, deduplication | Is this record in scope |
| Ranking and the shortlist cut | What does this system actually do |
| Every count, every share | Synthesis, and what the evidence supports |
| Contract compliance | Which subfield a general record belongs to |

The v0.1–v0.3 prompts asked the model to do all of it and spent most of their
length trying to stop it drifting. **Do not re-implement any left-hand column in
prose.** If a count is wrong, the script is wrong; fix the script.

The corollary matters just as much: `scripts/triage.py` produces a *sorting aid*,
not a verdict. Its scores carry no authority and shortlisting is not admission.
Screen every record on the shortlist yourself.

## A3. Set up

```bash
make setup                 # dev tooling and git hooks
```

The pipeline itself needs nothing installed — `python3 scripts/harvest.py` runs
on a bare Python 3.11+. `make setup` is for the dev tools.

Then fill in `.env`:

- `OPENALEX_API_KEY` — free, from <https://openalex.org>, and **effectively
  required**. OpenAlex meters a daily USD budget: $0.10 keyless, $1 with a key. A
  full harvest is ~300 search calls. Keyless it aborts partway through with
  "Insufficient budget". `harvest.py` refuses to retry that, because retrying
  turns one loud failure into a quiet half-corpus that every later count trusts.
- `OPENALEX_MAILTO` — optional, buys the faster polite pool.
- `S2_API_KEY` — optional. Without it Semantic Scholar 429s almost every call,
  which is why `--no-s2` is the documented default.

## A4. Bump the version before you run

```bash
OUT=outputs/01_landscape/v0.6           # a new directory, always
```

**Never point `harvest.py` or `triage.py` at a directory that already holds
`screening.csv`.** `harvest.py` merges and is safe. `triage.py` refuses unless
`--force`, and that refusal is load-bearing: regenerating `shortlist.md` and
`audit_sample.md` underneath decisions made against the previous pair leaves a
run that looks finished and measures its recall against a sample file that is no
longer on disk. `audit.py` has two checks whose only job is to catch it.

## A5. Run the mechanics test first, and use the right one

```bash
make plan  OUT=$OUT                     # the query plan, no calls
make smoke OUT=outputs/01_landscape/v0.6-test
```

**`--limit-queries N` is not a smoke test.** The plan is core groups first;
periphery starts at q021, so six queries harvest ~1900 records and zero
periphery, and `07_periphery.md` cannot be written from harvest counts at all.
`--smoke` runs seismology, hydrogeology and earth_observation — one periphery
group on purpose.

## A6. The full run

```bash
make harvest OUT=$OUT     # corpus → screened.csv, checkpointed every call
make triage  OUT=$OUT     # ranked shortlist + a sample from below the cut
#   ... you screen, deep-read and write ...
make audit   OUT=$OUT     # executed contract check, exits non-zero
make enrich  OUT=$OUT     # optional: countries + publication type from OpenAlex
make export  OUT=$OUT     # the one JSON document the front end reads
make web     OUT=$OUT     # the dashboard, into web/dist/
```

**Read `triage_stats.md` before touching a threshold.** The cut is an AND of four
conditions — score, strong hits, LLM vocabulary present, a domain group
identified — so a table that varies only `--min-score` hides which one is
binding. If a row is flat across `min-score`, lowering it will change nothing.
Twice now the binding filter has been structural rather than the score knob.

**Screen the audit sample exactly as you screen the shortlist.** It is drawn from
*below* the cut, so any record in it you would have admitted is a false negative.
That measurement is what makes the cut a measurement rather than an assumption.
Above 5%, diagnose which cut is binding before widening anything.

Every substantive paragraph carries its evidential status as its first token:

| Tag | Means |
|---|---|
| `[Certain]` | Stated in a source you read, and quoted in `papers.md` |
| `[Likely]` | Supported but inferred, or read from an abstract only |
| `[Absent-searched]` | Looked for and not found — **must cite the query id** (`q041`) that looked |

`[Absent-searched]` without a query id is an unbacked absence claim, and
`audit.py` fails the run for it. An absence you did not search for is not a
finding.

**No promotional framing.** "promising", "great potential", "revolutionary",
"paradigm shift", "cutting-edge", "state of the art" — `audit.py` greps for
these across every report file and fails the run. This review describes what
exists; it does not advocate for it.

## A7. Finish the run record

`RUN.md` is context for the numbers, never the source of one. Fill in every
field, including `prompt commit` — without it, nobody can reconstruct which
prompt produced the run:

```markdown
- date:
- prompt: prompts/01_landscape_neutral.md v0.6
- prompt commit:        # git rev-parse --short HEAD
- model:
- triage threshold:     # --min-score, and why
- false-negative rate:  # from the audit sample
- harvested / shortlisted / screened / core / context:
- notes:                # what broke, what to change next version
```

Then add an entry to `decisions.md`: what, why, and **what it rules out**. That
last clause is the point of the file — it is what stops a decision being
relitigated every version.

Commit the prompt and its output together. A run whose prompt is not in the same
commit is not reproducible.

## A8. What must never be lost

| File | Status |
|---|---|
| `screening.csv` | **Irreplaceable.** Your in/out decision per record |
| `papers.csv` | **Irreplaceable.** The comparison grid |
| `papers.md` | **Irreplaceable.** Verbatim extracts — the evidence trail under the prose |
| `screened.csv`, `triage.csv` | Regenerable in minutes; gitignored, 22 MB each |
| everything else | Regenerable from `reference/queries.json` |

A committed run directory is **evidence**. Do not reformat one, do not let a
formatter trim its whitespace, and do not edit a number in it to match a later
recount — write a new version instead. `.editorconfig`, `.pre-commit-config.yaml`
and `pyproject.toml` all exclude `outputs/` for this reason.

---

# §A2 — The other two runs

Three runs now share this repository. Everything in §A holds for all of them unless it
is contradicted here.

| Run | Prompt | Asks | Output |
|---|---|---|---|
| 01 | `prompts/01_landscape_neutral.md` | What exists in agentic AI for solid-earth geoscience | `outputs/01_landscape/v0.5` |
| 02 | `prompts/02_tango.md` | What exists that bears on making TANGO agentic | `outputs/02_tango/v0.2` |
| 03 | `prompts/03_gaps.md` | What the two finished runs record as missing | `outputs/03_gaps/v0.1` |

`outputs/02_tango/v0.2` is v0.1 plus a hand-retrieval round: same corpus, same screening
decisions, same 183 admitted sources, but 14 sources re-read from PDFs fetched by hand, three of
them promoted out of `context`. Quote v0.2. **`OUT_TANGO` in the Makefile still defaults to
`v0.1` on purpose** — `make gaps` reads it, and moving 03's inputs is a decision to take
deliberately rather than inherit. Pass `OUT_TANGO=outputs/02_tango/v0.2` when you mean v0.2.
`decisions.md` records why the round was written as a new directory and why that sits awkwardly
with the 01 run's in-place correction on the same day.

**The 01 pipeline is frozen.** `harvest.py`, `triage.py` and `audit.py` produced the
v0.5 landscape and a committed run is evidence; a later run must not be able to change
what an earlier one measured. So 02 and 03 got their own scripts rather than flags on
those three. The one exception is `harvest.py`, which is reused unchanged because it was
already `--config`-driven — 02 ships a query plan, not a fork of the harvester.

## A2.1 — 02_tango

```bash
make smoke-tango OUT_TANGO=outputs/02_tango/v0.1-test   # 3 cells, one periphery
make harvest-tango                                      # 22 cells, ~440 OpenAlex calls
make triage-tango
#   ... you screen, hand back the paywall list, deep-read and write ...
make audit-tango
```

Four things differ from §A and all four have bitten already:

- **The domain filter barely filters.** 01 asks "is this one of ten solid-earth
  subfields"; 02 asks "is this computational", which most agent papers pass. The v0.1
  smoke corpus shortlisted 42% at 01's thresholds against 01's 6%. `triage_tango.py` has
  a third knob, `--min-domain`, and it is usually the binding one. Settle it from
  `triage_stats.md` before screening, and measure what it cost in the audit sample.
- **A group harvested without a triage pattern is dropped silently**, which is the v0.5
  `scope: none` failure in a corpus far more exposed to it. `triage_tango.py` refuses to
  run if `reference/queries_tango.json`'s `triage` block and its `domain_groups` do not
  name the same groups.
- **The run pauses once**, after screening, to hand back `paywalled.md`. Institutional
  access is the one thing the session cannot get for itself, and a source demoted for
  want of a login is a measurement error that is cheap to fix before the report and
  expensive after. Hand-retrieved PDFs live outside this repository and are untracked by
  decision — publisher PDFs are not redistributable and the remote is public — so the run
  asks where the store is rather than assuming a path.
- **The report must not prescribe.** Describing what a system did is the job; saying
  what TANGO should do about it is not. `audit_tango.py` fails the run for the common
  forms, and the grep is not the specification.

Contract: `reference/SCHEMA_tango.md`, which is a delta against `SCHEMA.md` — same
`papers.csv` columns on purpose, so the two grids join and `gaps.py` reads both without
a special case. 02 adds `transfer.csv` (what each system actually drives, at what
autonomy, through what interface), `transfer.md` (the quotes under it) and
`paywalled.md`.

## A2.2 — 03_gaps

```bash
make gaps          # RUNS defaults to the 01 and 02 run directories
#   ... you read, cluster, and send a verification agent after each gap ...
make audit-gaps
```

03 harvests nothing. `scripts/gaps.py` reads seven shapes of gap out of the finished
runs' own artifacts — authors' stated limitations, `[Absent-searched]` claims with their
query ids, `not stated` columns with denominators, evaluations with no baseline or
held-out set, empty subfields and touchpoints, unread sources, and systems whose claim
outruns their evaluation. On the v0.5 run that is 117 candidates.

Three rules carry this run:

- **Synthesis, not reasoning.** A gap says what is absent and cites where that was
  recorded. Why it matters, what to do about it, which is biggest — none of that, and
  `audit_gaps.py` greps for it.
- **A verdict is returned, never assigned.** Each gap gets a verification subagent whose
  job is to find work that refutes it, searching the runs' own `screened.csv` first. A
  verification that searched nothing returns `undecidable`, and `refuted` is a result to
  keep rather than a failure to hide.
- **Every candidate is accounted for** — cited by a gap or in the discard ledger with a
  reason. One that quietly vanishes is indistinguishable from one nobody read.

Contract: `reference/SCHEMA_gaps.md`, which fixes the `gaps.md` block format because
`audit_gaps.py` parses it.

---

# §B — Changing the scripts

## B1. What this repository is

Methods and outputs for a scoping review. Two halves:

- `scripts/` — the deterministic half. Standard library only.
- `prompts/` — the judgment half, versioned, exposed as slash commands.

`.claude/skills/<name>/SKILL.md` is a **symlink** into `prompts/`. That is what
makes each prompt a slash command. A tool that replaces one with a copy forks the
prompt: the skill and `prompts/` drift apart, and a run then records a prompt
version that is not what was executed. `make check` asserts every skill entry is
still a live symlink, and a `destroyed-symlinks` pre-commit hook catches the
same thing earlier.

### The module map

| Script | Job |
|---|---|
| `harvest.py` | OpenAlex + arXiv (+ S2) → `screened.csv`. Merges preprint and published versions on a title slug. Checkpoints every call |
| `triage.py` | Scores every record from title+abstract, writes the shortlist and a sample from below the cut. No network |
| `audit.py` | Parses the run's own artifacts and checks 26 contract conditions. Exits non-zero |
| `enrich.py` | Author-institution countries and publication type for the admitted set, from OpenAlex. The only script the front end depends on that makes a network call, and the only optional one |
| `export_web.py` | One run → the single JSON document the front end reads. 01-only: its section list and subfield vocabulary are the landscape report's |
| `triage_tango.py` | 02's ranking. Imports the agentic half of the score from `triage.py`; its domain vocabulary and TANGO touchpoints come from `reference/queries_tango.json` |
| `audit_tango.py` | 02's gate. 38 checks, including the three artifacts 02 adds and one that fails a report for telling TANGO what to do |
| `gaps.py` | Finished runs → `gap_candidates.csv`. Seven extractors, no judgment |
| `audit_gaps.py` | 03's gate. 19 checks, three of which exist to stop a gap that rests on nothing |

**`triage_tango.py` imports `triage.py`'s pattern lists on purpose**, so "agentic" is
defined once. The consequence is that a change to `AGENT_LLM`, `AGENT_GENERIC`,
`AGENT_COMPOUND`, `MEDIUM` or `NEGATIVE` is a method change for **both** runs and needs a
re-triage of both, not one.

## B2. Setup and the gate

```bash
uv sync
uv run pre-commit install --install-hooks
```

Before every commit:

```bash
make check      # ruff, ruff-format, mypy --strict, pytest+coverage, pre-commit, symlinks
```

`make check` must pass from a bare clone: no network, no API key, no run
directory. **Never use `git commit --no-verify`.** If a hook is wrong, fix the
hook in a commit of its own.

## B3. Conventions

- **Standard library only in `scripts/`.** `urllib`, `csv`, `xml.etree`. A
  reviewer who wants to re-run the corpus should not have to resolve a dependency
  tree first, and that property is worth more than the convenience of `requests`.
  Dev tooling is a dev dependency; the pipeline has none.
- `mypy --strict` over `scripts/` and `tests/`. A `# type: ignore` must carry an
  error code and a one-line reason. Same for `# noqa`.
- `pathlib`, never `os.path`.
- Progress goes to **stderr**; the artifact goes to a file, and only `audit.py`'s
  table goes to stdout (so it can be piped into `RUN.md`).
- No bare `except`. Catch the exception you mean. The two broad handlers that do
  exist are deliberate and annotated — a dead API must not kill a 300-call run.
- Every script's `main()` takes `argv` so it is callable from a test.

## B4. Testing

`tests/` mirrors the scripts. `make check` runs the suite with a **65% coverage
floor** on `scripts/`. The floor is not 80% because `harvest.py`'s three API
readers are network calls that CI must never make; the parts that carry the
review's conclusions are near-complete.

Two test shapes matter here, and both exist because of a real failure:

- **`audit.py` is tested by mutation.** One fixture writes a run that passes all
  26 checks; each test breaks exactly one thing and asserts that exactly the
  corresponding check fails. A check that stops failing when its condition is
  broken has become decoration, and that is invisible from a green run. There is
  also a test asserting the battery is 26 long, so a new check cannot be added
  without extending the fixture that exercises it.
- **`triage.py`'s scoring is tested case by case.** It has been wrong twice — a
  case-insensitive `ReAct` that produced 377 false positives in a 1795-record
  corpus, and a structural `scope: none` filter that discarded 190 records the
  harvest existed to find. Neither was visible in any count. Both were found by
  reading a sample by hand; the tests are the cheap version of that reading.

**A change to the scoring is a method change.** It alters what a re-run admits, so
it belongs in a version bump with a re-triage and a `decisions.md` entry — never
folded into a refactor. Three known gaps are recorded as `strict=True` xfails in
`tests/test_triage.py` and `tests/test_export_web.py` for exactly this reason:
they document the intent, fail loudly if someone "fixes" them by accident, and
flip to XPASS when the change is made deliberately.

## B5. Commits

Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`,
`ci:`. Subject ≤ 72 characters, imperative. The body explains *why*.

A commit that changes a prompt must carry the output it produced, or neither.

## B6. Things that will bite you

- **A bare `AND` inside an OR group makes OpenAlex return zero results with no
  error.** The corpus is silently empty for that cell and every downstream count
  still looks plausible. `validate_config` refuses to run rather than harvest
  nothing — terms in `reference/queries.json` are single phrases, and the script
  joins them.
- **`n_available` is the API's own count, and it is why paging caps are
  visible.** A query that hit its cap is marked TRUNCATED. Without that, the
  periphery section reports the cap rather than the size of the literature —
  which is exactly what would have happened at `openalex_max_pages: 5`.
- **A zero-result query and a malformed query look identical downstream.** They
  are distinguishable only at the call site, which is why `status: zero` exists
  and why `audit.py` fails a run that has one.
- **`ReAct` is matched case-sensitively and must stay that way.** `react` is what
  chemicals do. Likewise bare `MCP` is monocyte chemoattractant protein, so it is
  only matched beside a system noun or as the tail of a hyphenated tool name.
- **Generic agent vocabulary requires independent LLM vocabulary.**
  "multi-agent system" is forty years old; without corroboration it promotes
  1990s work into an LLM-era shortlist.
- **`08_papers.md` and `index.md` are exempt from the evidence-tag check.** The
  annotated list's evidence is its citations. Scoring it as untagged prose fails
  every complete run.
