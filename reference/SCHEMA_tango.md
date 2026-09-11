# Output schema — 02_tango

Read `SCHEMA.md` first. It defines identity keys, CSV formatting, the `screening.csv`
columns, the `papers.csv` column order, the `agentic_techniques` and `architecture`
controlled lists, the maturity rubric, and the `papers.md` extract format. **All of that
is unchanged here**, deliberately: two runs with the same grid can be read together, and
`scripts/gaps.py` reads both without a special case.

This file records only what differs, plus the three artifacts 02 adds.
`scripts/audit_tango.py` enforces the parts that can be checked mechanically.

---

## What differs from SCHEMA.md

### Scope

`in`: a system in which an LLM or foundation model **decides something for itself** —
picks a tool, plans a sequence, iterates on its own output, calls code and acts on the
result — **and what it acts on is a simulator, solver, optimiser, scientific code, or an
engineering or techno-economic model.** The domain of the physics does not matter. A
flowsheet agent for a chemical plant and a well-placement agent for a geothermal doublet
run the same loop over a different engine, and it is the loop this run is about.

`out`: prompt-in/text-out applications with no decision loop; pre-LLM agent work; ML
surrogates with no agent deciding anything; anything before November 2022.

`periphery` — harvested, counted, characterised in one section, never deep-read:
software engineering agents, laboratory and robotic automation, web/GUI/computer-use
agents, and literature or writing agents. Software-engineering agents are periphery by
decision, not by accident: they are the largest agent literature there is, and this run
is about driving TANGO, not refactoring it.

### `cut_reason` values

As SCHEMA.md, with `not-geoscience` replaced by **`no-simulation-target`** — an agentic
LLM system whose artefact is not a simulation, solver, optimiser or model. Every other
value is unchanged: `not-agentic`, `periphery`, `pre-llm-only`, `duplicate`,
`not-a-source`, `no-abstract-untriageable`.

### `subfield` values

Core, one per source, matching the harvest groups in `reference/queries_tango.json`:
`simulation_orchestration`, `solver_control`, `optimisation_uq`, `energy_systems`,
`geoenergy_subsurface`, `scientific_computing`, `computational_discovery`, and
`simulation_general` for a source that drives a simulation but names no group.

Periphery: `software_engineering`, `lab_automation`, `interface_agents`,
`science_of_science`.

### Tier expectations

The 01 run admitted 155 sources from 11,191 harvested, 23 of them core. Nothing about
this corpus makes that a target. Report the actual numbers; if `core` is under 15, say
so and say why in `RUN.md`, and say which of the audit sample or the domain vocabulary
told you it was real.

---

## `transfer.csv` — what each system actually drives

One row per **admitted** source, `core` and `context` alike. Column order is fixed;
`audit_tango.py` checks it.

| Column | Notes |
|---|---|
| `identity_key` | join key; must exist in `papers.csv` |
| `system_id` | same value as the `papers.csv` row |
| `tango_touchpoints` | `;`-separated, from the controlled list below, **or `none`**. What the system's *evaluated* behaviour covers — not what its introduction says it could do |
| `what_it_drives` | the concrete thing it acts on, named: `Aspen Plus flowsheet`, `OpenFOAM case directory`, `SPECFEM input deck`, `a pymoo optimisation loop`. Where a source drives its own unnamed in-house code, say so — `an in-house chemical process simulator, unnamed` — rather than `not stated`: the first records that nobody else can reproduce it, the second records that you do not know. `not stated` only when the source never says what it drove at all |
| `interface` | how it reaches it: `api` / `cli` / `file-io` / `mcp` / `code-execution` / `gui` / `not stated` |
| `autonomy` | `suggests` (a human runs it) / `executes-with-approval` / `executes-and-iterates` (closes the loop on its own output) / `not stated`. Rate from the evaluation section only |
| `failure_handling` | what the source says happens when the driven code fails or does not converge, in the authors' terms, or `not stated` |
| `access_status` | `full-text` / `abstract-only`, same value as the `papers.csv` row |

A `context` row will mostly be `not stated`. That is the correct entry and it is a
measurement: it says the abstract did not describe the interface.

### Controlled list — `tango_touchpoints`

`config-generation`, `topology-construction`, `solver-control`, `optimisation-loop`,
`surrogate-modelling`, `uncertainty-quantification`, `hpc-scale-out`, `tool-exposure`,
`results-interpretation`, `techno-economic`, `verification-regression`,
`provenance-reproducibility`, `none`.

These are TANGO's own surfaces, taken from `tango_complete_reference.md` §2–§3. Free
text is not allowed in this column. If a system does something TANGO has no surface for,
that belongs in the report prose, not in a column that is counted.

**Assigning a touchpoint is a claim about the source, not about TANGO.** It records that
the source demonstrates an agent doing that kind of work on some system. It does not say
the technique would work in TANGO, and nothing in this run may say that — see
"Forbidden" in the prompt.

The `touchpoints` column in `triage.csv` is a **regex over title and abstract** and is a
different thing: a sorting aid, computed before anyone read anything. Never copy it into
`transfer.csv`.

---

## `transfer.md` — the evidence under `transfer.csv`

One `## <identity_key>` block per **core** source. Inside it, one verbatim quoted
sentence per touchpoint claimed on that row, plus the sentence the `autonomy` rating was
read from. Quotes, not paraphrase; `NOT FOUND: <what you looked for>` where the text does
not contain it.

Same rule as `papers.md`: if a touchpoint is not traceable to a block here, it does not
go in `transfer.csv`, and it does not go in the report.

---

## `paywalled.md` — what is behind a paywall, and what would open it

Written **as you go**, not at the end. The run pauses on this file once, after screening
(see the prompt, step 3a), because the person running it may have institutional access
you do not.

One table, one row per source whose full text could not be retrieved:

| Column | Notes |
|---|---|
| `identity_key` | join key |
| `title` | |
| `url` | the DOI or landing page, so it can be opened by hand |
| `venue` | |
| `blocked_by` | `paywall` / `bot-protection` / `no-full-text-anywhere` / `tooling-failure` / `no-abstract-in-any-api` |
| `tried` | every route attempted, `;`-separated: publisher DOI, Unpaywall, arXiv, author copy, repository |
| `local_pdf` | the filename if a copy is already in a local store, else `no`. Two stores: `paywalled_paper/` in the repository and `~/Downloads/paywalled_paper_2/` |
| `would_change` | what reading it could change — the `tier` it would support, or the maturity it could be rated at. `nothing` is a valid entry |

`blocked_by: bot-protection` is separated from `paywall` on purpose. The 01 run found a
gold-open-access paper that no route could retrieve, which means **an OA flag is a licence
status, not an access outcome** — a count of paywalled sources that quietly includes those
is wrong in a way nobody can see.

Before writing a row, check both local stores for a PDF: they already hold files retrieved
by hand for the 01 run, and a source is not unreachable if it is sitting on disk. The
filenames are publisher exports rather than titles, so match on the DOI or the article id.

`unreachable.md` is still required and still means what SCHEMA.md says. `paywalled.md` is
the subset that someone with the right credentials could fix, in a shape they can act on.

---

## Report sections

`$OUT/report/`, one file per section. Same rules as the 01 report — evidence tag on every
substantive paragraph, `[[identity_key]]` citations, no promotional framing, counts per
`system_id` or per row and always say which.

| File | Content |
|---|---|
| `00_executive_summary.md` | What exists, at what maturity, against which touchpoints, on what evidence. ≤800 words |
| `01_control_patterns.md` | How agents drive a simulator: what they emit (a config, a script, an API call), what they read back, what closes the loop. Grouped by pattern, not by paper |
| `02_architectures.md` | Recurring designs and what each is chosen for. No diagrams |
| `03_touchpoints.md` | One subsection per touchpoint in the controlled list, **including every one with no sources** |
| `04_evaluation.md` | How systems were tested, against what baseline, on what data; whether any shared benchmark exists |
| `05_maturity.md` | Distribution of demonstrated maturity across systems; how often claimed exceeds demonstrated; abstract-only counts beside it |
| `06_failure_and_limits.md` | What authors report their systems could not do, in their terms: non-convergence, wrong units, invalid configs, cost. Quoted, never generalised |
| `07_periphery.md` | Size and character of the excluded neighbouring agent literatures, from harvest counts |
| `08_papers.md` | The annotated paper list, grouped by subfield then tier. `core` 4–6 lines, `context` one line marked `[context]` |
| `index.md` | Table of contents plus the run's headline numbers |

`08_papers.md` and `index.md` are exempt from the evidence-tag check, as in the 01 run:
the annotated list's evidence is its citations.
