# unreachable_urls.md

Empty this run. No identifier or URL that this run attempted to verify failed to resolve.

The three mechanics-slice fetches (queries 16-18) all resolved to the correct document (title
and authors confirmed against the fetched content in each case). One of the three
(arxiv:2508.11618) had a body-text extraction failure downstream of a successful resolution
— the URL loaded and returned real content, but the fetch tool could not decompress all of
the PDF's text streams. That is a different failure mode from "does not resolve" and is
documented instead in `papers.md` and `RUN.md`, not here.

No other candidate was fetched this run: the remaining ~88 screened items were screened at
title level only (per the test-mode budget) and none was individually verified, so none can
be reported here as either reachable or unreachable.
