# Deep Research: Agentic AI in Geoscience

Prompts and outputs for the literature deep research on agentic AI in geoscience.

## Structure

| Path | What |
|---|---|
| `prompts/` | Versioned research prompts, neutral → TANGO-specific |
| `outputs/<prompt>/<version>/` | One directory per run. Never overwritten |
| `decisions.md` | Decision log |
| `.claude/commands`, `.cursor/commands` | Symlinks to `prompts/`, so each prompt is a slash command |

## How to run

Launch the agent from this repo root, then invoke the prompt as a command, e.g.
`/01_landscape_neutral`.

Loop: edit prompt → bump version → run → inspect output → commit prompt and output
together.

## Output contract

Every run writes into its own `outputs/<prompt>/<version>/` and produces at least:

| File | Content |
|---|---|
| `RUN.md` | Run record, see template below |
| `index.md` | Entry point (+ `index_<n>_<section>.md` in `full` mode) |
| `coverage.md` | `test` mode only: yield table, projection, go/no-go verdict |
| `queries.csv` | One row per web call — the audit trail behind every absence claim |
| `screened.csv` | One row per unique screened item, with cut reason |
| `abstracts/` | Verbatim abstract per screened item, so a re-triage needs no re-search |
| `papers.csv` | Comparison grid, one row per admitted source |
| `papers.md` | Verbatim extracts per admitted source — the evidence trail for the prose |
| `pdfs/` | Downloaded PDFs for admitted sources, gitignored |
| `unreachable_urls.md` | Source could not be verified to exist |
| `access_restricted.md` | Source exists, full text unreachable |

`screened.csv` + `abstracts/` are what make a run reusable: scope or taxonomy can change
without re-issuing a query. No PDFs in git; this prompt does not upload to GCS.

### `RUN.md` template

```markdown
- date:
- prompt: prompts/01_landscape_neutral.md v0.1
- prompt commit:      # git rev-parse --short HEAD
- model:
- harness:            # agent-harness-config commit, or "default"
- sources requested:
- sources reached:
- notes:              # what broke, what to change next version
```
