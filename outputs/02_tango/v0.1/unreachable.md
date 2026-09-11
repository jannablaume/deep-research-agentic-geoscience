# Unreachable and partially reachable sources

What could not be read, and what that costs the report. A source listed here is still
admitted and still counted; the entry records how thin its evidence is so no reader mistakes
a title for a finding. `paywalled.md` is the subset someone with the right credentials could
fix; this file is the wider record, and it includes sources that *were* read but not from the
place their identity key points at.

**This file changed more than any other after the report was first drafted.** Fourteen of the
sources recorded below were later retrieved by hand from publisher and preprint sites and
placed in a local store outside this repository. All fourteen were read. What that recovered,
and what it did not, is recorded in each section and summarised under "What the hand-retrieval
round settled".

## Screened core, demoted to context for want of full text

Fifteen records screened `core` could not be read in full when the original deep-read reached
them, and one further record was blocked at the step-3a handoff and stayed blocked. **Three of
those fifteen were later recovered and promoted back to `core`**; the remaining twelve are
tabulated in `paywalled.md` with the routes tried and what reading them would change. The
summary figure is the one that belongs in a methods section: **the core tier fell from 113 to
98, recovered to 101 after the hand-retrieval round, so 11% of the intended deep-read remains
lost to access** — down from 13%.

Two of the fifteen were worse than thin — they were empty. Both are now read:

| identity_key | title | what was originally recorded | what is now recorded |
|---|---|---|---|
| `doi:10.1039/d5dd00435g` | Multi-agentic AI framework for end-to-end atomistic simulations | a one-sentence publisher-deposited graphical abstract naming no engine | the full CC-BY version of record, read from `d5dd00435g.pdf`: a multi-agent AutoGen/AG2 system driving LAMMPS on the Argonne Carbon cluster via Atomsk, Phonopy and OVITO, rated `M1` against a human-expert baseline |
| `doi:10.2139/ssrn.7333555` | Geo2UBEM: 3D Geometry Abstraction and LLM Multi-Agent Parameter Inference for Automated Urban Building Energy Modeling | nothing beyond the title — no abstract existed in any harvested API record either | the full SSRN preprint, read from `ssrn-7333555.pdf`: a three-agent system driving EnergyPlus 23.2 through an Optuna TPE loop on six named Purdue buildings, rated `M3` against held-back metered data |

Both originally carried `tango_touchpoints: none`. Both now carry six touchpoints each. This is
the concrete case for the warning this file always carried, now confirmed: **`none` produced by
an access failure looked identical in the column to a genuine negative, and in both cases the
column was wrong.** The third recovered record, `doi:10.26434/chemrxiv.15006587/v1`, was not
empty — its system was already in the grid through the authors' repository under the same
`system_id` — but reading the preprint moved the source itself from `context` to `core`.

## Admitted and read, but not from the version the identity key names

Eight `core` records were originally read from a substitute that was almost certainly the same
work but was not verified against the version of record. **Six of the eight were later verified
by reading the version of record from the local store.** Three of those six turned out to
differ from their preprint in ways that changed this run's records — which is the concrete
answer to a risk this file could originally only state, not size.

| identity_key | what was originally read instead | why | outcome |
|---|---|---|---|
| `doi:10.1145/3731599.3767349` | arXiv:2502.12280 | ACM returned HTTP 403, IEEE HTTP 418 | **verified, and corrected** — three quotes differ; the published version describes two Parsl implementations rather than one, and reports a hallucination incident and a tool-call cap absent from the preprint |
| `doi:10.1016/j.dche.2026.100312` | arXiv:2601.11650v1 | ScienceDirect returned HTTP 403 | **verified, and corrected** — the published paper has *three* case studies, not two; the third is a stability assessment across prompt styles, model versions and an ammonia synthesis flowsheet |
| `doi:10.1016/j.taml.2026.100660` | arXiv:2503.01273v1 | Elsevier is an established blocked host | **verified, and corrected** — the published version reports a pass@1 robustness comparison (86.6% against 85.0% on paraphrased prompts) that was originally recorded as absent |
| `doi:10.1016/j.ijheatfluidflow.2026.110399` | arXiv:2504.19338 | Elsevier is an established blocked host | **verified unchanged** — every quote matches the version of record |
| `doi:10.1016/j.taml.2025.100594` | arXiv:2504.09602v1 | Elsevier returned only a redirect interstitial | **verified unchanged** |
| `doi:10.1002/aidi.202500174` | arXiv:2506.02019v3 | Wiley is an established blocked host | **verified unchanged** |
| `doi:10.3929/ethz-c-000801434` | arXiv:2605.19743v2 | the institutional record carries metadata only, no full-text link | **still inferred** — the hand-retrieved copy is the same arXiv version, so this is not an independent check |
| `title:aspenplusmcp…` | the authors' GitHub repository | the accompanying ChemRxiv preprint is on a blocked host | **still asserted by the repository** — but the ChemRxiv preprint is now admitted and read as a separate `core` record under the same `system_id`, so the system's evidence no longer rests on the repository alone |

Two things are worth stating plainly. First, the concentration originally identified holds:
seven of the eight are publisher blocks, six of those Elsevier or Wiley, and in every case an
author-deposited preprint was freely readable at the same moment the version of record was
not. That is a fact about distribution, not licensing. Second, **three of six verified
substitutes had materially changed between preprint and publication — a 50% divergence rate on
a small sample.** This was flagged early as a risk that could not be sized; on these six it is
not negligible.

## Admitted and read, but through a proxy or a third-party deposit

Seven `core` records were originally reached by a route other than the publisher's own site.
**Five were later re-read from the publisher's own PDF**; two were not.

- **Through the `r.jina.ai` reader proxy** (4 originally). Three are now read from the
  publisher PDF: `doi:10.1109/access.2025.3605803`, `doi:10.1080/19401493.2026.2653969`,
  `doi:10.3390/buildings15173190`. One remains proxy-read:
  `doi:10.20944/preprints202608.1323.v1`. The cost originally recorded was specific — the
  proxy renders tables and figures as captions and alternative text, so **table cell values
  were not quotable** — and lifting it changed a finding. In
  `doi:10.3390/buildings15173190` the recovered Table 9 shows GPT+MCP max-displacement
  errors of 1.624%, 1.998% and 2.834% against an abstract claiming "deviations under 1.5%",
  so three of eight case-direction pairs exceed the paper's own headline figure. That
  discrepancy was unreadable until the publisher PDF arrived, and is now recorded in
  `papers.md` and section 08.
- **From a laboratory or repository deposit** (3 originally). Two are now read from the
  Elsevier version of record: `doi:10.1016/j.softx.2025.102367` and
  `title:automaticbuildingenergymodel…` — the latter confirming the article is *Energy and
  Buildings* 327 (2025) 115116. One remains a deposit read: `doi:10.11578/dc.20260516.1`.

## Admitted, read in full, and still thin — because the source is short

`doi:10.69997/pse.120458` is not an access failure. It was retrieved and read completely from
the start, and the complete record is a two-page conference extended abstract of roughly 450
words with no methods, evaluation or limitations sections in existence. Its `papers.csv` row
is sparse because the source is sparse. A copy of it was among the fourteen hand-retrieved PDFs
and confirmed that this is the whole of it. The distinction matters for anyone reading the
`not stated` counts: a `not stated` produced by a two-page abstract is a fact about the
publication format, while a `not stated` produced by a blocked publisher is a fact about this
run's reach, and the two should not be pooled.

## One source was recovered from the local store from the start

`doi:10.1016/j.bdes.2026.100042` (GAGAW) failed every online route — publisher HTTP 403
directly and through a reader proxy, the preprint server returning bot verification, the
preprint PDF host failing DNS. It is **not** demoted. The version of record was read from the
local PDF store flagged at the step-3a handoff and written as a full `core` record. Recorded
here because a reader comparing this file against the delegated reader's own report would
otherwise find a contradiction.

## Harvest metadata that was wrong, and what was done about it

Three records carried metadata that would have sent a reader to the wrong place, and all
three were caught by attempting the fetch rather than by inspection:

- `title:automaticbuildingenergymodel…` is indexed as a report; it is a peer-reviewed journal
  article (*Energy and Buildings* 327, 2025). Its `source_type` is recorded as
  `peer-reviewed` on the evidence of the document, not the index. The publisher PDF, read
  later, confirms the volume, year and article number.
- `doi:10.26868/30680611.2026.1305` carried `0611.2026` in the arXiv field, which is not a
  valid arXiv identifier. The full text was found in the open IBPSA proceedings instead.
- `doi:10.3390/buildings15173190` carried `2507.1968` in the arXiv field, which is a
  preprint-server manuscript number; `arxiv.org/html/2507.1968` resolves to an unrelated
  paper on financial-services task allocation. Had that been read without checking, the
  record would have been fabricated wholesale. **This warning was tested by the
  hand-retrieval round**: it included `2507.01968v1.pdf`, which is that unrelated
  financial-services paper. It was matched by DOI, found to belong to no admitted record, and
  discarded rather than read into the grid.

## What the hand-retrieval round settled

Fourteen PDFs were retrieved by hand and matched against the admitted set by DOI read off the
first pages, not by filename — the filenames are publisher exports. The outcome, stated as
counts because that is what this file is for:

| outcome | count |
|---|---|
| demoted records recovered and promoted to `core` | 3 |
| substitute reads verified against the version of record, unchanged | 3 |
| substitute reads verified and **corrected** | 3 |
| proxy or deposit reads replaced by the publisher's own PDF | 5 |
| already read in full from the same route, no change | 3 |
| PDFs that matched no admitted record and were discarded | 2 |

The two discarded files are worth naming because both were predicted by this file: `2507.01968v1.pdf`
is the unrelated financial-services paper the bad arXiv id in `doi:10.3390/buildings15173190`'s
metadata points at, and `buildings-15-03191-v3.pdf` is the article adjacent to
`doi:10.3390/buildings15173190` in the same MDPI issue — an indicator framework for building
retrofit with no agent and no language model in it. Neither was screened in; neither appears
in any grid.

Twelve demotions remain, listed in `paywalled.md`. Nothing in this round resolved them, and the
routes recorded there are still the routes that failed.
