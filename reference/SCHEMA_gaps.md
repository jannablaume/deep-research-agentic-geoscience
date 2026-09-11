# Output schema — 03_gaps

The 03 run produces one deliverable: **a synthesis of the gaps the finished runs already
contain**, with every one of them traced to the artifact it came from and checked against
the literature before it is stated.

It reads runs; it does not harvest one. There is no `screened.csv`, no shortlist and no
maturity rubric here. `scripts/audit_gaps.py` enforces what can be checked mechanically.

---

## The one rule this run adds

**Synthesis, not reasoning.** A gap statement says what is absent, unstated, unevaluated
or unread, and cites where that was recorded. It does not say why the gap matters, what
should be done about it, which gaps are more important, or what anyone should research
next. Those are the next run's job and stating them here would launder an opinion into a
file that looks like a measurement.

`audit_gaps.py` greps for the common forms — *matters because*, *should be prioritised*,
*future work*, *we recommend*, *the most important*. The grep is not the specification;
the rule is wider than it.

---

## `gap_candidates.csv` — written by the script, never by hand

`scripts/gaps.py` writes this. Do not edit it. If a candidate looks wrong, that is a
finding about the run it came from, and it belongs in `RUN.md`.

| Column | Notes |
|---|---|
| `candidate_id` | `c001`, unique across the whole file and stable for a given input |
| `run` | `01_landscape/v0.5`, the run the candidate was read out of |
| `kind` | `author-limitation`, `absence-claim`, `evidence-hole`, `evaluation-hole`, `empty-category`, `unread-source`, `claim-gap` |
| `subject` | what it is about: a `system_id`, a column name, a subfield, a touchpoint, a report file |
| `statement` | the text as the artifact carries it |
| `evidence_ref` | where it was read from: an `identity_key`, a filename, or the query ids behind an absence claim |
| `count`, `denominator` | present only where the candidate is a count. Never one without the other |

---

## `gaps.md` — the deliverable

One block per gap, in this shape. `audit_gaps.py` parses it, so the field lines are a
format, not a suggestion.

```markdown
## G01 — <the gap, in one sentence, present tense>

- candidates: c003; c017; c112
- runs: 01_landscape/v0.5; 02_tango/v0.1
- verdict: confirmed-absent
- evidence: q041; q052
- checked: 2026-09-11

[Certain] One paragraph restating what those candidates record, in the terms the sources
and the runs used. Every sentence here is a restatement of something cited above.
```

| Field | Values |
|---|---|
| `candidates` | `;`-separated `candidate_id`s. **At least one**, and every one must exist in `gap_candidates.csv` |
| `runs` | which runs the candidates came from |
| `verdict` | `confirmed-absent` / `partially-addressed` / `refuted` / `undecidable` — from the verification pass, never assigned by the writer |
| `evidence` | query ids (`q041`) for `confirmed-absent`; `identity_key`s for `partially-addressed` and `refuted`. Required for all three; `undecidable` may carry either or `none` |
| `checked` | the date the verification pass returned |

Evidence tags (`[Certain]`, `[Likely]`, `[Absent-searched]`) work exactly as in the other
two runs, and an `[Absent-searched]` paragraph must cite the query ids that looked.

### The discard ledger

`gaps.md` ends with a `## Discarded candidates` section: one line per candidate not used
by any gap, with a reason from this list — `duplicate-of <Gxx>`, `run-artefact` (it
records how the run was done, not what the literature lacks), `too-specific` (one
system's own limitation with nothing else bearing on it), `refuted` (the verification pass
found the work exists).

Every candidate is either cited by a gap or listed here. `audit_gaps.py` fails the run on
a candidate that is neither, because a candidate that quietly vanishes is indistinguishable
from one nobody read.

---

## `verification.md` — what was checked, and how

One `## G01` block per gap, written from what the verification subagent returned:

- **searched**: the queries it ran, and against what — the runs' own `screened.csv`,
  `papers.csv`, and any API or web call it made
- **found**: what came back, with `identity_key`s or URLs
- **verdict**: the same value as the `gaps.md` block
- **what would change it**: the finding that would move the verdict

A gap whose verification block says the agent searched nothing is `undecidable`, not
`confirmed-absent`. An absence nobody looked for is not a finding — the same rule the
other two runs apply to `[Absent-searched]`.

---

## `RUN.md`

- date, prompt, prompt commit, model
- which run directories were read, and their commit
- candidates extracted, by kind
- gaps stated, by verdict
- candidates discarded, by reason
- what the verification pass could not settle, and why
- what to change in v0.2
