# access_restricted.md

Empty this run. No fetch attempted this run hit a paywall, login wall, or subscription
gate — but that is a statement about what was tested, not a finding that everything is
open. The 20-call budget went entirely to arXiv sources (open access by construction) for
the mechanics slice; industry-facing venues that are typically subscription-gated in `full`
mode (OnePetro/SPE, ScienceDirect journals such as Water Research and Applied Energy) were
screened at title level only (per `screened.csv`) and never fetched, so their access status
is genuinely untested, not confirmed open.

One source this run, arxiv:2508.11618, had its full text become unreadable after a
successful, unrestricted fetch (a PDF text-stream decompression failure in the fetch tool,
not a paywall). That is recorded in `papers.md` and `RUN.md` rather than here, because the
source is verified to be openly accessible — the failure is on the reading side, not the
access side.

A `full`-mode run should expect ScienceDirect and OnePetro/SPE full-text fetch attempts to
populate this file; `test` mode's 3-candidate mechanics slice did not include any source from
those venues and so cannot speak to that.
