# Contributing

Thanks for looking. This repository holds both **code** and **research
evidence**, and the two are governed by different rules — most of what looks
unusual here follows from that.

- Changing the scripts, tests or docs? Read this file, then
  [AGENTS.md §B](./AGENTS.md).
- Producing or correcting a run? Read [AGENTS.md §A](./AGENTS.md).
- Pointing this at your own literature? Read [docs/adapting.md](./docs/adapting.md).

## The two rules everything else follows from

> **A number is counted or it is not stated.** Nothing here estimates, rounds up
> from memory, or reports a cap as a measurement. Where a count cannot be
> computed, the artifact says so and the page renders an em dash — a missing
> count must never look like a measured zero.

> **A committed run is evidence.** Anything under `outputs/` is a record of what
> was measured, when. It is never edited, reformatted or corrected in place to
> match a later recount.

## Setup

```bash
make setup      # venv, dev tools, git hooks
make check      # must pass before every commit
make verify     # re-audits the finished runs; no network, no API key
```

`make verify` checks two things: that every finished run still passes its
contract, and that a re-executed audit reproduces the committed `audit.md` byte
for byte. The second is why adding a check is a two-part job — the gate changes
*and* the runs' recorded gate output does, and `make verify` will tell you so
rather than letting one drift from the other.

Without `screened.csv` and `triage.csv` — gitignored, 22 MB each — three checks
per run cannot run, and `make verify` reports `PARTIAL` rather than either
`PASS` or `FAIL`. That distinction is deliberate and is the same rule the
reports follow: a check that could not run must not look like a measured
result. Regenerate them with `make harvest` to get a full `PASS`.

`make check` must pass **from a bare clone**: no network, no API key, no run
directory. That property is what makes CI meaningful, so a change that breaks it
is a bug even if the tests are green on your machine.

**Never use `git commit --no-verify`.** If a hook is wrong, fix the hook in a
commit of its own.

## Code conventions

- **Standard library only in `scripts/`** — `urllib`, `csv`, `xml.etree`. Not
  `requests`, not `pandas`. A reviewer who wants to re-run the corpus should not
  have to resolve a dependency tree first, and a column of DOIs that silently
  becomes a float under `pandas` dtype inference is exactly the class of error
  this repository exists to prevent. Dev tooling is a dev dependency.
- `mypy --strict` over `scripts/` and `tests/`. A `# type: ignore` carries an
  error code and a one-line reason. Same for `# noqa`.
- `pathlib`, never `os.path`.
- Progress to **stderr**; artifacts to files. Only `audit.py`'s table goes to
  stdout, so it can be piped into `RUN.md`.
- No bare `except`. Catch the exception you mean. The two broad handlers that
  exist are deliberate and annotated — a dead API must not kill a 300-call run.
- Every `main()` takes `argv`, so it is callable from a test.

## Testing

`tests/` mirrors `scripts/`, with a 65% coverage floor on `scripts/`. The floor
is not higher because `harvest.py`'s API readers are network calls CI must never
make; the parts that carry the review's conclusions are near-complete.

Two test shapes matter, and both exist because of a real failure:

- **Gates are tested by mutation.** One fixture writes a run that passes every
  check; each test breaks exactly one thing and asserts that exactly the
  corresponding check fails. A check that stops failing when its condition is
  broken has become decoration, and that is invisible from a green run. A test
  also asserts the battery's length, so a new check cannot be added without
  extending the fixture that exercises it.
- **Scoring is tested case by case.** It has been wrong twice — a
  case-insensitive `ReAct` that produced 377 false positives, and a structural
  filter that discarded 190 records the harvest existed to find. Neither was
  visible in any count. Both were found by reading a sample by hand; the tests
  are the cheap version of that reading.

Known gaps are recorded as `strict=True` xfails rather than left as comments.
They fail loudly if someone "fixes" them by accident and flip to XPASS when the
change is made deliberately.

## Things that are not refactors

Some changes look small and are not. Each of these needs a version bump, a
re-run of the affected stage, and a [`decisions.md`](./decisions.md) entry:

| Change | Why it is a method change |
|---|---|
| `triage.py`'s scoring patterns | Alters what a re-run admits. **Also affects 02**, which imports them |
| A query plan's terms, groups or ids | Query ids are cited by `[Absent-searched]` claims; shifting them invalidates earlier absence claims |
| Any threshold default | Changes the cut, and therefore every count downstream |
| Removing or softening an audit check | See below |

**Gates are append-only in spirit.** Checks get added, never removed or softened
to go green. A gate that passes because it stopped checking is worse than an
honest failure — which is the whole reason `audit.py` replaced a self-attested
audit table that was reliably green and occasionally wrong.

## Touching `outputs/`

Don't, except to add a new run directory.

`outputs/` is excluded from `ruff`, from `.editorconfig`'s whitespace rules and
from every pre-commit hook that modifies a file, so that no formatter can trim
whitespace inside a committed run. A cosmetic diff on a run reads like a method
change; a number edited to match a later recount is a rewritten record.

**If a run's numbers are wrong, write a new version.** The one exception is a
correction that touches no harvested record, no query and no scoring threshold —
and even then it is corrected in place *only* with a decision-log entry saying
so. Two such corrections are recorded, both dated 2026-09-11.

The irreplaceable files are `screening.csv`, `papers.csv` and `papers.md`: they
are judgment, not computation, and no re-run reproduces them. `screened.csv` and
`triage.csv` are gitignored — 22 MB each, and regenerable in minutes.

## Prompts are symlinks

`.claude/skills/<name>/SKILL.md` is a **symlink** into `prompts/`. That is what
makes each prompt a slash command. A tool that replaces one with a copy forks the
prompt: the skill and `prompts/` drift apart, and a run then records a prompt
version that is not what was executed.

Three things guard it — a `destroyed-symlinks` pre-commit hook, an assertion in
`make check`, and a CI job. If you edit a prompt, check `git diff` shows a change
to the file in `prompts/`, not a new regular file under `.claude/`.

**A commit that changes a prompt must carry the output it produced, or neither.**

## Commits and pull requests

Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`,
`ci:`. Subject ≤ 72 characters, imperative mood. **The body explains why** — the
what is in the diff.

Before opening a PR:

```bash
make check && make verify
```

In the PR description, say what the change **rules out**. That clause is the
point of the decision log and the most useful habit in this repository: it is
what stops a decision being relitigated every version.

## Reporting a problem

The most valuable issue you can file is **a number that does not reconcile**. If
a figure in a report does not match the artifact it should have been counted
from, that is a bug in the gate, not a typo — say which file, which number and
which artifact disagrees.

Also welcome:

- A trap you hit adapting this to another field (add it to
  [docs/adapting.md](./docs/adapting.md)).
- A check that passes when it should fail.
- Anything in the docs that is stale, since several files describe the same
  machinery from different angles.

## Licence

MIT for the scripts; report prose and the CSV artifacts under `outputs/` are
CC BY 4.0. By contributing you agree your contribution is released on those
terms.
