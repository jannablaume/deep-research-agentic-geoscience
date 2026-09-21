# Query plan schema

The **input** contract. `SCHEMA.md`, `SCHEMA_tango.md` and `SCHEMA_gaps.md`
describe what a run produces; this file describes the one file that decides what
a run *searches*.

A query plan is the only file you must write to point this machinery at a
different literature. It is read by `scripts/harvest.py` (the `bands` and
`domain_groups` blocks) and, for a run modelled on 02, by
`scripts/triage_tango.py` (the `triage` block). Neither script contains a
research topic; both get it from here.

Worked examples: [`queries.json`](./queries.json) (01, no `triage` block),
[`queries_tango.json`](./queries_tango.json) (02, with one), and
[`queries_template.json`](./queries_template.json) — an annotated, topic-neutral
starter to copy.

---

## How a plan becomes queries

One query per **scope × domain group × band**:

```
openalex:  (band term OR band term OR …) AND (group term OR group term OR …)
arxiv:     (abs:term OR …)               AND (abs:term OR …)
```

Query ids are assigned in iteration order — `q001`, `q002`, … — scope by scope,
then group, then band. **That order is load-bearing.** `core` is emitted before
`periphery`, so `--limit-queries N` truncates the periphery away entirely. Use
`--smoke` instead; see [AGENTS.md §A5](../AGENTS.md).

Query ids are also cited by `[Absent-searched]` claims in the report, so a plan
edit that shifts ids invalidates the absence claims of every earlier run. This
is one of several reasons a changed plan means a new version directory rather
than a re-run in place.

## Top level

| Key | Type | Required | Meaning |
|---|---|---|---|
| `_comment` | string | no | Ignored by the scripts. Say what the plan is for |
| `from_date` | `YYYY-MM-DD` | **yes** | Publication-date floor. Records before it are dropped |
| `openalex_max_pages` | int | **yes** | Paging cap. 200 records per page |
| `arxiv_max_results` | int | **yes** | Cap on arXiv results per query |
| `bands` | object | **yes** | The technique axis. See below |
| `domain_groups` | object | **yes** | The subject axis. See below |
| `triage` | object | only for 02-style runs | Scoring vocabulary. See below |
| `smoke` | array | no | Which cells `--config <smoke file>` harvests |
| `venue_hints` | object | no | Advisory only; nothing filters on it |

**`openalex_max_pages` deserves a thought rather than a default.** It is a cap,
and a query that reaches it is marked `TRUNCATED` in `queries.csv` so that a
section cannot report the cap as the size of a literature. The 01 plan shipped
at 5 and was raised to 20 mid-run for exactly that reason.

## `bands` — the technique axis

```json
"bands": {
  "A_agentic": {
    "precision": "high",
    "note": "Explicit agent vocabulary. Nearly everything here is on-topic.",
    "terms": ["\"agentic AI\"", "\"AI agent\"", "\"LLM agent\""]
  },
  "B_llm": { "precision": "medium", "note": "…", "terms": ["…"] }
}
```

| Key | Meaning |
|---|---|
| `precision` | Documentation only. Recorded per record as the band it was found in |
| `note` | Documentation only |
| `terms` | Phrases, OR-ed together by the script |

A record found by both bands is reported under the **higher-precision** band,
because that is the stronger statement about it.

## `domain_groups` — the subject axis

```json
"domain_groups": {
  "core":      { "in_scope": true, "note": "Full depth.",      "groups": { "seismology": ["…"] } },
  "periphery": { "in_scope": true, "note": "Counted, not read.", "groups": { "ocean": ["…"] } }
}
```

Two scopes, `core` and `periphery`, and the names are fixed — `triage_tango.py`
and the smoke logic both look for those two keys. `groups` maps a group name to
its list of phrases.

**Group names are identifiers, not labels.** They appear in `screened.csv`, in
the triage block, in the export's facets and in the report's section headings.
Renaming one after a run has been committed breaks the join between the run and
its plan.

## Writing terms

**Every term is a single phrase. The script joins them.**

A bare `AND`, `OR` or `NOT` inside a term makes OpenAlex return zero results
*with no error* — the cell is silently empty and every downstream count still
looks plausible. `validate_config` refuses to start rather than harvest nothing.

```json
"terms": ["\"carbon capture\"", "\"CO2 storage\""]     ✅
"terms": ["\"carbon capture\" AND storage"]            ❌ refuses to run
```

Quote multi-word phrases (`"\"rock mechanics\""`); leave single words bare
(`"geomechanics"`).

Aim each group at recall, not precision — triage and screening narrow it later,
and a record never harvested cannot be recovered by any downstream knob.

## `triage` — only for 02-style runs

01's vocabulary lives in `scripts/triage.py`. A run modelled on 02 puts it here
instead, and `triage_tango.py` reads it, so **a new topic needs no new Python**.

```json
"triage": {
  "core":      { "simulation_orchestration": "flowsheet|co[- ]simulat|input deck" },
  "periphery": { "software_engineering": "…" },
  "general":   "simulat|solver|numerical model",
  "touchpoints": { "config_generation": "input deck|configuration file" }
}
```

Values are **regexes**, compiled case-insensitively.

| Key | Required | Meaning |
|---|---|---|
| `core`, `periphery` | **yes** | One pattern per harvested group. Keys must match `domain_groups` **exactly** |
| `general` | **yes** | Fallback for a record that names no specific group |
| `touchpoints` | no | A second, orthogonal regex pass. 02 uses it for the surfaces of the system under study |

Three refusals guard this block, and each is a failure that has actually
happened:

- **A group harvested with no triage pattern** scores `scope: none` and is cut
  no matter how high it scores. That shape cost 190 records in the v0.5 run and
  was invisible in every count. `triage_tango.py` refuses if `triage` and
  `domain_groups` do not name the same groups, in either direction.
- **No `general` fallback** and any record that names no specific group is
  discarded the same silent way.
- The fallback **counts its own matches** toward `domain_score`. It once did
  not, and the default `--min-domain 1` deleted an entire bucket while leaving
  a shortlist one point smaller as the only trace.

Case-sensitivity is a real design question here, not a detail: matched
case-insensitively, `\bReAct\b` produced 377 false positives in a 1,795-record
corpus, because `react` is what chemicals do. See
[`docs/architecture.md` §5](../docs/architecture.md).

## `smoke`

A list of cells the mechanics test harvests:

```json
"smoke": [
  { "scope": "core", "domain_group": "simulation_orchestration", "band": "A_agentic" },
  { "scope": "periphery", "domain_group": "software_engineering", "band": "A_agentic" }
]
```

**Include at least one `periphery` cell.** The periphery section cannot be
written from harvest counts if the smoke plan never reached one.

Ship it as a separate file with a lowered `openalex_max_pages` (02 uses
`queries_tango_smoke.json` at 2), and keep its cells a **verbatim subset** of the
full plan — a mechanics test over a plan the real run does not have proves
nothing about it. A test asserts this for 02.

## Checking a plan before you spend a budget

```bash
python3 scripts/harvest.py --out outputs/04_yours/v0.1 --dry-run \
    --config reference/queries_yours.json
```

`--dry-run` builds and validates the plan, prints every query with its id, and
calls nothing. It costs nothing and catches the bare-operator error, a
group/triage mismatch, and a plan whose query count is not what you expected.
