# Output schema

Column definitions and rating rubrics for `01_landscape_neutral`. Read this before
screening and again before filling `papers.csv`. `scripts/audit.py` enforces the parts
that can be checked mechanically.

All CSVs: RFC 4180, header row, **every cell quoted**, internal `"` doubled, newlines
inside a cell replaced with `; `. Use `not stated` where a source is silent. Never infer
a value to fill a cell.

---

## Identity

`identity_key` is assigned by `harvest.py` and is the join key across every file:
`doi:<lowercased doi>`, else `arxiv:<id>`, else `title:<slug>`. Never mint your own.

---

## `screening.csv` — your screening decisions

One row per record you screened. Written by you; never overwritten by `harvest.py`, so
re-harvesting cannot destroy this work.

| Column | Values |
|---|---|
| `identity_key` | must exist in `screened.csv` |
| `decision` | `in` / `out` |
| `tier` | `core` / `context` / empty when `out` |
| `subfield` | one of the ten below, or a periphery group |
| `cut_reason` | required when `out`. See below |
| `from_audit_sample` | `yes` for records screened from `audit_sample.md`, else `no` |
| `note` | free text, optional |

**Cut reasons** — use exactly one: `not-agentic` (an LLM is used but nothing plans, calls
tools, or acts), `not-geoscience`, `periphery` (in the neighbouring domains, counted not
read), `pre-llm-only` (agent work with no LLM component), `duplicate`, `not-a-source`
(podcast, table of contents, call for papers), `no-abstract-untriageable`.

`not-agentic` will be the largest bucket and it is the one judgment call that matters
most. The line: the system must **decide something for itself** — choose a tool, plan a
sequence of steps, iterate on its own output, or invoke code and act on the result.
A prompt-in / text-out application of an LLM is not agentic no matter what it is applied
to. Retrieval-augmented generation alone is not agentic; RAG inside a loop that decides
what to retrieve next is.

---

## Tiers

| Tier | What it means | What you produce |
|---|---|---|
| `core` | An agentic system in the core domain, described in enough detail to characterise its techniques, architecture and evaluation | Full text read, verbatim extracts in `papers.md`, every `papers.csv` column filled, a 4-6 line annotation in the report's paper list |
| `context` | On topic but thin, duplicative, abstract-only, or peripheral — real but not load-bearing | Abstract only. Fill `papers.csv` where the abstract supports it, `not stated` elsewhere. One-line annotation in the report's paper list, marked `context` |

Expect roughly 40-80 `core` and 100-250 `context`. Those are expectations, not quotas —
report the actual numbers. If `core` comes in under 25, say so and say why in `RUN.md`;
that is a finding about the field or about the search, and the audit sample tells you
which.

---

## `papers.csv` — the comparison grid

Column order is fixed; `audit.py` checks it.

| Column | Notes |
|---|---|
| `identity_key` | join key |
| `tier` | `core` / `context` |
| `system_id` | `<firstauthor><year>-<slug>`, or the system's own name. Several papers on one system share it. Counts in the prose are **per system**; this file is per source |
| `url`, `title`, `authors`, `year`, `venue` | from `screened.csv`, corrected against the full text |
| `source_type` | `peer-reviewed` / `preprint` / `industry` / `regulatory` / `repo` / `whitepaper` |
| `subfield`, `subfield_secondary` | assign by where the **evaluation** is set, not what the introduction invokes |
| `task` | one clause: what the system is for ("history matching of a fractured reservoir") |
| `agentic_techniques` | `;`-separated from the controlled list below |
| `architecture` | from the controlled list below |
| `base_model` | `GPT-4o`, `Llama-3-70B`, `not stated`, … — this is the field most often silently omitted, and it decides reproducibility |
| `tools_used` | what the agent can actually call: simulator, solver, database, plotting, code execution, retrieval index, physical instrument |
| `evaluation_method` | how it was tested |
| `baseline` | what it was compared against, or `none` |
| `held_out` | `yes` / `no` / `not stated` |
| `data_type` | `synthetic` / `benchmark` / `real-field` / `not stated` |
| `reported_result` | the headline number **as the source states it**, with its unit |
| `maturity_claimed` | strongest self-assertion, or `not stated` |
| `maturity_demonstrated` | from the rubric below, from the evaluation section only |
| `author_stated_limitations` | attributed, in the authors' terms |
| `code_availability` | URL, `on request`, `no`, `not stated` |
| `access_status` | `full-text` / `abstract-only` |
| `found_via` | `harvest` / `snowball` / `grey` |

### Controlled list — `agentic_techniques`

`tool-calling`, `code-execution`, `planning`, `task-decomposition`, `self-reflection`,
`memory`, `retrieval`, `multi-agent-debate`, `role-specialisation`, `human-in-the-loop`,
`simulator-in-the-loop`, `physics-solver-in-the-loop`, `instrument-control`,
`knowledge-graph`, `fine-tuning`, `guardrails-validation`.

Free text is allowed but only appended after the controlled terms, so the column stays
groupable. A grid that cannot be grouped is a list of papers.

### Controlled list — `architecture`

`single-agent`, `multi-agent-flat`, `multi-agent-hierarchical`, `pipeline-with-agent`,
`agent-plus-simulator`, `agent-plus-solver`, `agent-plus-database`, `router`,
`not stated`.

---

## Maturity rubric

Rate `maturity_demonstrated` from what the **evaluation section demonstrates**, never
from the abstract or introduction. The axis is what the evaluation data was and whether
the output touched reality — *not* how rigorous the evaluation was. Rigour is recorded
separately in `baseline` and `held_out`, so a careful synthetic study is not promoted
above a sloppy field trial.

| Level | Criterion |
|---|---|
| `M0` | Position or architecture paper, no working implementation |
| `M1` | Implemented; evaluated only on synthetic or textbook-scale data |
| `M2` | Evaluated on a reusable, site-agnostic benchmark — which may contain real data |
| `M3` | Evaluated on real field data from a **named** site, well, or campaign, retrospectively |
| `M4` | Output entered a real workflow or influenced a real decision; site or operator named; time-bounded |
| `M5` | Routine use beyond a trial, evidenced by someone other than the vendor |

Tie-breaks:
- M2 vs M3 is **benchmark versus site**, not synthetic versus real. A phase picker on
  STEAD is M2; the same picker on one named network's catalogue is M3.
- M3 requires the site to be named. "Real field data", unidentified, is M2 at most.
- M4 requires evidence an output was *used*. A field dataset alone is M3.
- Data source not stated: M1 at most, and record `not stated`.
- `access_status: abstract-only` forces `maturity_demonstrated: not stated (abstract only)`.

A gap between `maturity_claimed` and `maturity_demonstrated` is itself a finding.

---

## Subfields

Core, one per source: `geomechanics`, `seismology`, `hydrogeology`,
`reservoir_engineering`, `geothermal`, `ccs`, `mining`, `engineering_geology`,
`inversion`, `geological_modelling`.

Periphery, counted and characterised but never deep-read: `earth_observation`,
`climate_atmosphere`, `ocean`, `planetary`, `geoscience_general`.

---

## `papers.md` — the evidence trail

One `## <identity_key>` block per `core` paper. Inside it, verbatim quoted sentences —
not paraphrase — stating: what was built, what it could call, how it was evaluated, what
it achieved, and the `maturity_claimed` sentence. First line of each block is the URL and
how the text was obtained.

The report is written from these blocks. If a claim is not traceable to one, it does not
go in the report.
