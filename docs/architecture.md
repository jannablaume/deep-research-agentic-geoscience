# Architecture

Why this repository is shaped the way it is, and the decisions that look wrong
until you know why. Read this before removing anything that looks redundant.

`decisions.md` is the chronological record — what changed, when, and what it
ruled out. This file is the standing rationale.

---

## The one idea

**Split the work by whether it needs judgment, and let neither half pretend to be
the other.**

Searching, paging, deduplicating, ranking, counting and compliance-checking are
deterministic. Relevance, extraction and synthesis are not. The v0.1–v0.3
prompts asked one model to do all of it, and most of their length was spent
trying to stop it drifting: recounting numbers it had already reported,
re-deciding thresholds mid-run, and — the failure that ended the approach —
attesting to its own compliance from a context window that had been compacted
since the events it was attesting to.

Everything below follows from that split.

## 1. The scripts have no dependencies, on purpose

`urllib`, `csv`, `xml.etree`. Not `requests`, not `pandas`, not `httpx`.

A reviewer who wants to re-derive the corpus should be able to `git clone` and
run. Adding `requests` would save perhaps thirty lines in `harvest.py` and cost
that property. `pandas` would save more and cost more: a CSV read through
`pandas` acquires dtype inference, and a column of DOIs or years that silently
becomes a float is precisely the class of error this repository is built to
prevent.

The dev tooling is a different question — `ruff`, `mypy` and `pytest` are dev
dependencies, and `uv` manages them. Nothing the pipeline runs touches them.

## 2. `audit.py` parses the files instead of asking the model

The v0.3 prompt ended with a self-audit table the model filled in. It was
reliably green and occasionally wrong, because a long run gets compacted and the
compliance it is being asked about happened before the compaction.

Every check in `audit.py` is executed against the artifacts on disk. A failed
check is a working audit. It exits non-zero, and its output is a markdown table
designed to be pasted into `RUN.md`, so the run record carries a machine's
statement rather than the model's recollection.

**The two vacuity guards matter more than they look.** `papers.csv is non-empty`
and `screening.csv is non-empty` exist because with no admitted sources every
other check holds trivially — the table would read as a clean run that produced
nothing. A gate that passes because there is nothing left to check is the worst
possible outcome, since it looks exactly like success.

## 3. The recall audit is drawn from *below* the cut

A shortlist asserts that the records beneath it did not matter. Almost no review
tests that assertion, and it is where a review quietly loses part of its subject.

`triage.py` samples 150 records from below the cut and writes them in the same
digest format as the shortlist, so they can be screened identically. Any record
in that sample that should have been admitted is, by definition, a false
negative. That turns the cut from an assumption into a measurement with a number
attached.

**150, not 60.** In v0.4 the sample was 60, found 4 false negatives, and gave
6.7% — with a confidence interval wide enough to straddle the 5% action
threshold, which meant the measurement could not decide the thing it existed to
decide.

**Seeded, not random.** A re-run must draw the same 150. If the sample moved, the
false-negative rate would be measured against a file that no longer exists —
which `audit.py` now has a check for, because it happened.

## 4. The cut is an AND, and the stats report both knobs

A record survives triage only if it clears all four of: `agentic_score`,
`strong_hits`, LLM vocabulary present, and a domain group identified.

`triage_stats.md` therefore reports a grid over `min-score` × `min-strong`
rather than a single distribution. Varying one knob while holding the other
hides which is binding, and twice the answer has been "neither" — the binding
filter was structural:

- **v0.4**: every false negative in the audit sample scored on medium signals
  alone with `strong_hits` at 0. Lowering `--min-score` could not recover any of
  them. `AGENT_COMPOUND` — systems that plan or automate something with an LLM
  but never use the word "agent" — was the fix, at a cost of ~15% more
  shortlist.
- **v0.5**: 190 records cleared score, strong hits and LLM vocabulary, and were
  discarded anyway because they said "geoscience" without naming a subfield and
  so got `scope: none`. Among them a multi-agent geoscience document-extraction
  system at score 12. The `GENERAL` fallback was the fix. Shortlisting is not
  admission — a record whose subfield is unclear belongs in front of the
  screener, who decides.

If a row in that table is flat across `min-score`, stop turning that knob.

## 5. `ReAct` is case-sensitive and `MCP` is not matched bare

Three vocabulary decisions that each cost a run to learn:

- **`\bReAct\b`, case-sensitively.** Matched case-insensitively, this single
  pattern produced 377 false positives in a 1795-record test corpus — more than
  every other signal combined. `react` is what chemicals do, and geochemistry is
  in scope.
- **Bare `MCP` is never a signal.** It is also monocyte chemoattractant protein.
  It counts only beside a system noun (`MCP server`, `model context protocol`)
  or as the tail of a hyphenated tool name (`seismo-mcp`). Without those
  patterns, `open-darts-MCP`, `specfem-mcp`, `seismo-mcp` and `GeoMCP` all
  scored below the cut on a corpus harvested to find exactly them.
- **Generic agent vocabulary requires independent LLM vocabulary.**
  "multi-agent system" is forty years old, "copilot" is an aircraft, and "tool
  use" is primatology. Those terms count only once `AGENT_LLM` or `MEDIUM` has
  established the era on its own evidence.

And the inverse: `NEGATIVE` masks its own spans rather than disqualifying the
record. A paper about an LLM agent that also mentions reducing agents must still
score; only the phrase is suppressed, not the record.

## 6. `n_available` exists so that a paging cap cannot hide

`queries.csv` records the API's own result count next to the number of records
actually pulled. A query where `n_results >= cap` and `n_available > n_results`
is marked `TRUNCATED`.

Without it, a paging cap is invisible, and `07_periphery.md` reports the cap
rather than the size of the neighbouring literature. That is exactly what would
have happened at the shipped `openalex_max_pages: 5` — the v0.5 run raised it to
20 mid-flight for this reason.

The asymmetry is deliberate: arXiv reports every match but the harvester drops
anything before `from_date`, so `got < total` is routine there and means nothing
was lost. Only a run that reached its cap is truncated.

## 7. A zero-result query is a finding; a malformed one is a bug

Downstream they are identical — an empty cell either way. They are
distinguishable only at the call site, so `harvest.py` records `status: zero`
with a note, and `audit.py` fails any run that has one.

The stronger version of the same problem is caught earlier: **a bare `AND`
inside an OR group makes OpenAlex return zero results with no error.** The
corpus is silently empty for that cell and every downstream count still looks
plausible. `validate_config` refuses to start rather than harvest nothing —
terms in `reference/queries.json` are single phrases, and the script joins them.

## 8. Checkpoint every call, and abort on a spent budget

`harvest.py` writes `screened.csv` and `queries.csv` after every API call. A run
killed at 80% keeps its corpus, and re-running merges rather than restarting.

OpenAlex meters a daily USD budget — $0.10 keyless, $1 with a free key — and
returns HTTP 429 for both a per-second throttle and an exhausted budget. Those
are retried and *not* retried respectively. Retrying a spent budget turns one
loud failure into a quiet half-corpus that every later count trusts, which is
the same failure mode as a hidden paging cap and worse, because it looks like a
completed run.

## 9. Identity is DOI, then arXiv id, then title slug — and the alias map

A preprint and its published version arrive with different keys: `arxiv:…` from
arXiv, `doi:…` from OpenAlex. Without collapsing them on a normalised title
slug, the corpus double-counts most of arXiv, and "unique records" becomes a
number about the harvester rather than the literature.

Merging prefers whichever record actually carries content, accumulates query
provenance rather than overwriting it, preserves `first_seen_run`, and lets the
precision band win for reporting. That last one is asymmetric on purpose: a
record found by both bands is reported as `A_agentic`, because that is the
stronger statement about it.

## 10. `screened.csv` and `triage.csv` are gitignored; three files are not

22 MB each, regenerable from `reference/queries.json` in minutes. Committing
them would make every re-harvest an unreviewable diff.

`screening.csv`, `papers.csv` and `papers.md` are irreplaceable: they are
judgment, not computation, and no re-run reproduces them. `harvest.py` never
touches `screening.csv` for the same reason.

The cost is real and is paid deliberately: two of the report's numbers —
`harvested` and `shortlisted` — cannot be counted from a fresh clone. They are
read from `audit.md`, which a script generates and whose format is therefore
stable. Both are nullable in the export, and a null renders as an em dash rather
than a zero.

## 11. A committed run is evidence, so no tool may rewrite one

`outputs/` is excluded from `ruff`, from `.editorconfig`'s whitespace rules, and
from every pre-commit hook that modifies a file.

A formatter trimming whitespace inside a committed run produces a diff that
looks like a method change, and worse, establishes that run directories are
editable. They are not. If a number in a run is wrong, the answer is a new
version — never an edit to the record.

## 12. `08_papers.md` is exempt from the evidence-tag check

The annotated list's evidence is its citations: a four-to-six-line annotation
per source, no `[Certain]` tag by design. Scoring it as untagged prose failed
every complete run. `index.md` is exempt for the same reason.

They are *not* exempt from the citation-resolution check or the
promotional-language check, which apply to every file in `report/`.

## 13. The prompts are slash commands by symlink

`.claude/skills/<name>/SKILL.md` symlinks into `prompts/`. One file, two access
paths — so a prompt cannot be edited through one and read through the other.

A tool that replaces the symlink with a copy forks the prompt silently, and a
run then records a prompt version that is not what was executed. Three things
guard it: a `destroyed-symlinks` pre-commit hook, an assertion in `make check`,
and a job in both CI configurations.

## 14. The front end reads one exported document and nothing else

`export_web.py` writes a single JSON file. The page imports it; it never reads a
CSV, never parses the report markdown, and never fetches anything at runtime.

That is what makes the built folder something you can hand to somebody. It is
also why the export follows two rules of its own:

- **Nothing is inferred.** Every field is read from an artifact or counted from
  one. The single exception is the framework facet — a keyword match over the
  free-text `tools_used` column — and it is labelled `derived: true` everywhere
  it surfaces.
- **Counted beats parsed.** Where a number can be counted from a CSV it is
  counted, not lifted out of `RUN.md` prose. The false-negative rate is
  recomputed from `screening.csv` rather than quoted, because a below-cut record
  that screening admitted *is* a false negative and the definition should be
  applied rather than trusted.

The controlled vocabularies in `export_web.py` duplicate `reference/SCHEMA.md`
for one reason: order. A facet ordered by `Counter` alone is ordered by whatever
this run happened to find, so a technique that drops to zero next run disappears
from the axis instead of showing a zero, and two runs cannot be compared. Values
found in the data but absent from the list are appended rather than dropped, so
a schema change surfaces as an unordered tail instead of a vanished row.

## 15. A scoring change is a method change

`triage.py`'s regex battery decides what a re-run admits. Changing it is not a
refactor, and it does not belong in one: it belongs in a version bump, with a
re-triage, a fresh recall audit, and a `decisions.md` entry.

Three known gaps are recorded as `strict=True` xfails rather than fixed:

| Where | Gap |
|---|---|
| `AGENT_GENERIC` | The comma pattern allows `{0,2}` intervening word-units, but the canonical title its own comment names — "A Multi-Agent, Multi-Modal Large-Language-Model Framework" — has five. `{0,5}` matches it |
| `AGENT_COMPOUND` | Lists a bare `GPT` head, but compound patterns are only evaluated once `llm_present` is true, and `MEDIUM`'s GPT pattern needs a version digit. So "GPT-driven pipeline" never reaches the head written for it |
| `MODEL_FAMILIES` | `\bQwen\b` fails against the canonical `Qwen2.5-72B`, because a digit is a word character. Export-only: it miscategorises a model family rather than dropping a record |

`strict=True` means each flips to a failure the moment someone "fixes" it by
accident, and to XPASS when the change is made deliberately. That is the point:
the intent is recorded in the suite rather than in a comment nobody reads.
