# Unreachable and partially reachable sources

What could not be read, and what that costs the report. A source listed here is still
admitted and still counted; the entry records how thin its evidence is so no reader mistakes
a title for a finding. `paywalled.md` is the subset someone with the right credentials could
fix; this file is the wider record, and it includes sources that *were* read but not from the
place their identity key points at.

## Screened core, demoted to context for want of full text

Fifteen records screened `core` could not be read in full when the deep-read reached them,
and one further record was blocked at the step-3a handoff and stayed blocked. Every one is
tabulated in `paywalled.md` with the routes tried and what reading it would change; they are
not repeated here. The summary figure is the one that belongs in a methods section: **the
core tier fell from 113 to 98, so 13% of the intended deep-read was lost to access.**

Two of those fifteen are worse than thin — they are empty:

| identity_key | title | authors | year | venue |
|---|---|---|---|---|
| `doi:10.1039/d5dd00435g` | Multi-agentic AI framework for end-to-end atomistic simulations | Vriza, A.; et al. | 2025 | Digital Discovery (RSC) |
| `doi:10.2139/ssrn.7333555` | Geo2UBEM: 3D Geometry Abstraction and LLM Multi-Agent Parameter Inference for Automated Urban Building Energy Modeling | not stated in the harvest record | 2026 | SSRN Electronic Journal |

For the first, the only text any route returned is a one-sentence publisher-deposited
graphical abstract that names no simulation engine. For the second, no abstract exists in any
harvested API record either, so nothing beyond the title was available. Both carry
`tango_touchpoints: none` and `not stated` throughout, and **`none` here means "no touchpoint
could be evidenced", not "this system has no touchpoint"** — an important difference when
reading the touchpoint counts in the report, because a `none` of this kind is an access
failure wearing the same label as a genuine negative.

## Admitted and read, but not from the version the identity key names

Eight `core` records were read from a substitute that is almost certainly the same work but
was not verified against the version of record. This is not a minor bookkeeping point: every
quote in `papers.md` and `transfer.md` for these eight comes from the substitute, so a
revision made between preprint and publication would not be visible to this run.

| identity_key | what was read instead | why | how certain |
|---|---|---|---|
| `doi:10.1145/3731599.3767349` | arXiv:2502.12280 | ACM returned HTTP 403, IEEE HTTP 418 | inferred from identical authorship and content |
| `doi:10.1016/j.dche.2026.100312` | arXiv:2601.11650v1 | ScienceDirect returned HTTP 403 | inferred from identical authorship and title |
| `doi:10.1016/j.ijheatfluidflow.2026.110399` | arXiv:2504.19338 | Elsevier is an established blocked host | inferred from identical title and author list |
| `doi:10.1016/j.taml.2025.100594` | arXiv:2504.09602v1 | Elsevier returned only a redirect interstitial | inferred from identical title, authors and system description |
| `doi:10.1016/j.taml.2026.100660` | arXiv:2503.01273v1 | Elsevier is an established blocked host | inferred from identical title, authors and system name |
| `doi:10.1002/aidi.202500174` | arXiv:2506.02019v3 | Wiley is an established blocked host | inferred, and strongly — the 315-case benchmark and headline figures match |
| `doi:10.3929/ethz-c-000801434` | arXiv:2605.19743v2 | the institutional record carries metadata only, no full-text link | inferred from identical title and authors |
| `title:aspenplusmcp…` | the authors' GitHub repository | the accompanying ChemRxiv preprint is on a blocked host | asserted by the repository itself, not independently verified |

The concentration is the finding: seven of the eight are publisher blocks, six of those are
Elsevier or Wiley, and in every case an author-deposited preprint was freely readable at the
same moment the version of record was not. That is a fact about distribution, not licensing.

## Admitted and read, but through a proxy or a third-party deposit

Seven further `core` records were reached by a route other than the publisher's own site,
where the identity is certain because the DOI, title, authors and venue all matched:

- **Through the `r.jina.ai` reader proxy** (4): `doi:10.20944/preprints202608.1323.v1`,
  `doi:10.1109/access.2025.3605803`, `doi:10.1080/19401493.2026.2653969`,
  `doi:10.3390/buildings15173190`. Two of these are open-access articles that their own
  publishers refused to serve to an automated client — an OA licence is not an access
  outcome. The cost is real but bounded: the proxy renders tables and figures as captions and
  alternative text, so **table cell values were not quotable** for these records, and any
  number that existed only inside a table is absent from their `papers.csv` rows.
- **From a laboratory or repository deposit** (3): `doi:10.11578/dc.20260516.1`,
  `title:automaticbuildingenergymodel…`, `doi:10.1016/j.softx.2025.102367`. The last two were
  retrieved from US Department of Energy deposits after the publisher returned a
  bot-protection page.

## Admitted, read in full, and still thin — because the source is short

`doi:10.69997/pse.120458` is not an access failure. It was retrieved and read completely, and
the complete record is a two-page conference extended abstract of roughly 450 words with no
methods, evaluation or limitations sections in existence. Its `papers.csv` row is sparse
because the source is sparse. This distinction matters for anyone reading the `not stated`
counts in the report: a `not stated` produced by a two-page abstract is a fact about the
publication format, while a `not stated` produced by a blocked publisher is a fact about this
run's reach, and the two should not be pooled.

## One source was recovered from the local store rather than lost

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
  `peer-reviewed` on the evidence of the document, not the index.
- `doi:10.26868/30680611.2026.1305` carried `0611.2026` in the arXiv field, which is not a
  valid arXiv identifier. The full text was found in the open IBPSA proceedings instead.
- `doi:10.3390/buildings15173190` carried `2507.1968` in the arXiv field, which is a
  preprint-server manuscript number; `arxiv.org/html/2507.1968` resolves to an unrelated
  paper on financial-services task allocation. Had that been read without checking, the
  record would have been fabricated wholesale.
