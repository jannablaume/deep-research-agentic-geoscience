#!/usr/bin/env python3
"""Fetch the author-institution countries for a run's admitted sources.

    python3 scripts/enrich.py --out outputs/01_landscape/v0.5

Writes `<run>/enrichment/countries.csv`. Nothing else in the pipeline depends
on it: `export_web.py` reads it when present and omits the geography facet when
it is not, so a run without this step is complete, just quieter.

**Why this is a separate script and not part of the harvest.** `harvest.py`
stores what it needs to screen a record — title, abstract, venue, citations.
Institution country is not in that set and is not in any tracked artifact, so
the alternative to a small extra fetch was inferring nationality from author
names, which the output contract forbids and which would be wrong often enough
to matter.

**Coverage is the finding, not a footnote.** OpenAlex records institutions from
the publisher's metadata, and preprint servers largely do not supply them —
sixteen of this run's twenty-three core sources are arXiv preprints. So a
country tally here is a tally over the *subset that reports affiliations*, the
script prints that denominator, and the page shows it. A geography chart drawn
over 40% of a corpus without saying so is the same mistake as a maturity chart
drawn over the readable slice.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.openalex.org/works"
BATCH = 50  # OpenAlex accepts an OR-joined filter; 50 keeps the URL sane.
FIELDS = "doi,authorships,primary_location,type"
UA = "deep-research-agentic-geoscience (https://github.com/jannablaume/deep-research-agentic-geoscience)"


def doi_of(identity_key: str) -> str | None:
    """The DOI an identity key implies, or None where it implies none.

    `arxiv:2604.11945` has a registered DOI of the form `10.48550/arxiv.<id>`,
    which is how OpenAlex indexes arXiv works, so those are recoverable.
    `title:<slug>` keys are not.
    """
    if identity_key.startswith("doi:"):
        return identity_key.split(":", 1)[1]
    if identity_key.startswith("arxiv:"):
        return f"10.48550/arxiv.{identity_key.split(':', 1)[1]}"
    return None


def fetch(dois: list[str], mailto: str | None, key: str | None) -> list[dict[str, object]]:
    """One batch. Raises on HTTP failure so the caller can decide."""
    params = {"filter": "doi:" + "|".join(dois), "select": FIELDS, "per-page": str(len(dois))}
    if mailto:
        params["mailto"] = mailto
    request = urllib.request.Request(  # noqa: S310 - scheme is from the literal API constant
        f"{API}?{urllib.parse.urlencode(params)}", headers={"User-Agent": UA}
    )
    if key:
        request.add_header("Authorization", f"Bearer {key}")
    with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - as above
        payload = json.load(response)
    results = payload.get("results", [])
    return results if isinstance(results, list) else []


def countries_of(work: dict[str, object]) -> list[str]:
    """Unique ISO country codes across every author's institutions.

    Deliberately a set, not a count: a paper with three German co-authors is one
    paper from Germany, and weighting by author would turn a large collaboration
    into a large country.
    """
    found: set[str] = set()
    authorships = work.get("authorships")
    if not isinstance(authorships, list):
        return []
    for authorship in authorships:
        if not isinstance(authorship, dict):
            continue
        institutions = authorship.get("institutions")
        if not isinstance(institutions, list):
            continue
        for institution in institutions:
            if isinstance(institution, dict):
                code = institution.get("country_code")
                if isinstance(code, str) and code:
                    found.add(code.upper())
    return sorted(found)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", required=True, help="run directory")
    parser.add_argument("--offline", action="store_true", help="make no calls; write an empty file")
    args = parser.parse_args(argv)

    run = Path(args.out)
    papers = run / "papers.csv"
    if not papers.exists():
        sys.exit(f"no papers.csv under {run} — nothing to enrich")

    with papers.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    wanted = {r["identity_key"]: doi_of(r["identity_key"]) for r in rows}
    lookup = {doi.lower(): key for key, doi in wanted.items() if doi}

    found: dict[str, list[str]] = {}
    journals: dict[str, str] = {}
    # OpenAlex's own `type` is captured because `source_type` in papers.csv is
    # blank on 108 of 155 rows, and because it is what explains the journal
    # gap: the 54 rows with no venue are conference papers, for which OpenAlex
    # holds no journal-level record at all.
    types: dict[str, str] = {}
    calls = 0

    if not args.offline:
        import os

        mailto = os.environ.get("OPENALEX_MAILTO")
        key = os.environ.get("OPENALEX_API_KEY")
        dois = sorted(lookup)
        for start in range(0, len(dois), BATCH):
            batch = dois[start : start + BATCH]
            try:
                works = fetch(batch, mailto, key)
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as error:
                # A dead or metered API must not produce a half-populated facet
                # that looks like a measurement. Abort and leave the previous
                # file, if any, untouched.
                print(f"enrich: aborted after {calls} call(s): {error}", file=sys.stderr)
                return 1
            calls += 1
            for work in works:
                raw = work.get("doi")
                if not isinstance(raw, str):
                    continue
                doi = raw.replace("https://doi.org/", "").lower()
                key_for = lookup.get(doi)
                if not key_for:
                    continue
                found[key_for] = countries_of(work)
                location = work.get("primary_location")
                source = location.get("source") if isinstance(location, dict) else None
                name = source.get("display_name") if isinstance(source, dict) else None
                journals[key_for] = name if isinstance(name, str) else ""
                kind = work.get("type")
                types[key_for] = kind if isinstance(kind, str) else ""
            time.sleep(0.2)

    target = run / "enrichment" / "countries.csv"
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        # LF, not RFC 4180's CRLF: .gitattributes sets `eol=lf` for the whole
        # repository and every other CSV in a run directory is LF, so writing
        # CRLF here would leave the working copy differing from the committed
        # blob on every checkout. `csv` reads either.
        writer = csv.writer(handle, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(
            ["identity_key", "countries", "openalex_journal", "openalex_type", "resolved"]
        )
        for row in rows:
            key_for = row["identity_key"]
            resolved = "yes" if key_for in found else "no"
            writer.writerow(
                [
                    key_for,
                    "; ".join(found.get(key_for, [])),
                    journals.get(key_for, ""),
                    types.get(key_for, ""),
                    resolved,
                ]
            )

    matched = len(found)
    with_country = sum(1 for c in found.values() if c)
    print(f"{target}  {calls} call(s)", file=sys.stderr)
    print(f"  {matched} of {len(rows)} admitted records matched in OpenAlex", file=sys.stderr)
    print(
        f"  {with_country} of {len(rows)} report an author institution with a country "
        f"({with_country * 100 // max(1, len(rows))}%) — the denominator the facet is drawn over",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
