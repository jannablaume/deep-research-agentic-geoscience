# Reading a run as a dashboard

Every finished run can be read as a static page instead of as markdown: the same
report with each section beside the counts it describes, its evidence tags as
filters, its citations as links into a filterable source list, and the verbatim
quote behind every characterisation one click away.

There are three, one per run — landscape, tango and gaps — built by one command,
each carrying a switcher in its header to the other two.

![The dashboard: the run summary table, above the executive summary](img/dashboard.png)

**The built page is not in the repository.** `web/dist/` is gitignored, because
it is generated from a committed run and regenerates in seconds. Cloning gets
you the source; one command gets you the page.

## See it, from a fresh clone

```bash
git clone git@github.com:jannablaume/deep-research-agentic-geoscience.git
cd deep-research-agentic-geoscience

make export        # the committed run → web/src/data/landscape.web.json
make web           # that JSON        → web/dist/  (runs npm install for you)

open web/dist/index.html          # macOS
xdg-open web/dist/index.html      # Linux
start web\dist\index.html         # Windows
```

That is the whole procedure. Double-clicking `web/dist/index.html` in a file
browser works identically — there is no server to start and nothing is fetched
at runtime.

**The other two runs get their own page the same way.** `make export-tango` and
`make export-gaps` write `web/src/data/tango.web.json` and `gaps.web.json`; one
`make web` builds all three into `web/dist/` — `index.html`, `tango.html`,
`gaps.html` — and each carries a small switcher in its header to the other two.
A page whose export is missing says so rather than failing the build, so you
never have to run all three exporters just to look at one.

**You need Node.** The badge above says the *pipeline* has no dependencies, and
that is true: `python3 scripts/harvest.py` runs on a bare Python 3.11+. The
front end is the one exception — `make web` needs **Node 18.20.8, 20.3+, or 22+**
and npm 9.6.5+ (Astro's own requirement), used only at build time. Nothing Node
touches ends up in the page: the built folder loads no script from a CDN and no
font from a network.

| Want to… | Do this |
|---|---|
| just look at it | `make export && make web`, then open `web/dist/index.html` |
| send it to a colleague | zip `web/dist/` and email it — it opens on their machine with nothing installed |
| change the front end | `make web-dev` → hot reload on <http://localhost:4321> |
| point it at another run | `make export OUT=outputs/01_landscape/v0.6 && make web` |
| add the country facet | `make enrich` before `make export` — needs network, ~3 OpenAlex calls |

If the page opens **unstyled and inert**, you opened `web/src/pages/index.astro`
or a stale `dist/` — rebuild with `make web` and open `web/dist/index.html`. If
`make web` says *"No exported run"*, run `make export` first.

## Why it is a folder and not a URL

The front end is a static [Astro](https://astro.build) site with no runtime
dependencies and no backend: the run is compiled into the page, so a copy of the
folder is a copy of the data. That property is the point — the research
direction is unpublished and lives on institutional infrastructure, so "send a
reviewer the folder" is the distribution method, and a page that only works over
`http://` works for everybody except the person you sent it to.
`web/scripts/relativise.mjs` exists for that one reason, and it is the kind of
bug you cannot see from the machine that built it.

## What the dashboard adds over the markdown

- **A summary table first.** The funnel from 11,191 harvested records to the 38
  with a readable evaluation section, one counted row at a time, each naming its
  denominator and what it counts. The last row is the one that needed care: this
  run cannot say how many sources a paywall cost, because `papers.csv` has no
  paywall column and `access_status: abstract-only` covers paywalls,
  bot-protected nominal open access, software deposits and records with no
  abstract in any API alike — so the row reports what *is* counted and says the
  rest is narrated in `unreachable.md` rather than tallied.
- **Filters second.** The 151-source explorer is the second section, not the
  fifth, because filtering is what most readers came to do.
- **Bibliographic facets** — publication type, journal or venue, and country of
  author institution. Country is the one figure on the page that needs a network
  call (`make enrich`), and the one whose denominator is not the whole corpus:
  94 of 151 sources report an affiliation, because OpenAlex takes them from
  publisher metadata that preprint servers largely do not supply. The panel
  leads with that denominator.
- **The report, re-cut.** Each thematic section sits beside the counts it
  describes rather than in a prose file next to charts it never mentions.
- **Evidence tags as filters.** `[Certain]` / `[Likely]` / `[Absent-searched]`
  become chips, so "show me only what a source actually stated" is one click.
- **Citations that resolve on the page.** Every `[[doi:…]]` is a numbered
  reference marker; clicking it opens that source's full comparison-grid record,
  including — for the 38 core sources — the verbatim sentences from `papers.md`
  that the characterisation rests on.
- **All 151 sources, filterable** by tier, field, architecture, technique,
  framework, maturity, model family and year, with the filtered set
  downloadable as RFC 4180 CSV.
- **One derived facet, labelled as such.** "Frameworks the agents call" is a
  keyword match over `tools_used` and `base_model`, not a `SCHEMA.md` column and
  not covered by any audit check. The page says so everywhere it appears, and
  Method prints the whole keyword list including the terms that matched nothing.

Everything else on the page is either read from a run artifact or counted from
one, and the contract audit is reproduced in full: 26 executed checks, not a
claim of quality.

