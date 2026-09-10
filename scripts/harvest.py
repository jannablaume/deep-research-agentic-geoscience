#!/usr/bin/env python3
"""Harvest the candidate corpus from bibliographic APIs into screened.csv.

Replaces the model-driven search loop. Everything here is deterministic: the same
config produces the same corpus, counts are computed rather than estimated, and the
abstract arrives with the record so no call is ever spent to store one.

Sources: OpenAlex (primary, 200/page, abstracts, citation counts), arXiv (preprint
freshness — OpenAlex indexing lags months, which is most of this field's lifetime),
Semantic Scholar (supplement, best-effort; it rate-limits without a key).

Usage:
    python3 scripts/harvest.py --out outputs/01_landscape/v0.5 [--dry-run]
    python3 scripts/harvest.py --out outputs/01_landscape/v0.5 --no-s2
    python3 scripts/harvest.py --out outputs/01_landscape/v0.5-test --no-s2 --smoke

Re-running merges into the existing screened.csv: rows are never dropped, query
provenance accumulates, and a row's `first_seen_run` is preserved. Screening
decisions live in screening.csv and are never touched by this script.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

# One harvested bibliographic record. Values are a mix of str and int, and the merge
# step fills fields in from whichever source carried them, so `Any` is the honest
# annotation rather than a TypedDict that would need every field optional anyway.
Record = dict[str, Any]
# One cell of the query plan: the query strings for each API, plus its band and group.
Query = dict[str, str]
# reference/queries.json, parsed.
Config = dict[str, Any]

# Optional. OpenAlex serves a faster "polite pool" to callers who identify themselves, but
# works without. Left unset by default so no identity is baked into the repo; set
# OPENALEX_MAILTO in an untracked settings.local.json or the shell to opt in.
MAILTO = os.environ.get("OPENALEX_MAILTO", "")
USER_AGENT = "deep-research-agentic-geoscience" + (f" (mailto:{MAILTO})" if MAILTO else "")
# OpenAlex meters the API against a daily USD budget: $0.10/day keyless, $1/day with a
# free key. A full harvest is ~300 search calls at $0.001, so keyless it dies partway
# through with HTTP 429 "Insufficient budget" and leaves a corpus that looks complete.
# Set OPENALEX_API_KEY in the shell or an untracked settings.local.json.
OPENALEX_API_KEY = os.environ.get("OPENALEX_API_KEY", "")
# Optional. Without it Semantic Scholar returns 429 on nearly every call, which is why
# --no-s2 is the documented default; with it, S2 becomes a usable third index.
S2_API_KEY = os.environ.get("S2_API_KEY", "")

# fmt: off
SCREENED_COLS = [
    "identity_key", "doi", "arxiv_id", "url", "title", "authors", "year", "venue",
    "type", "cited_by", "oa_pdf_url", "abstract", "domain_group", "band",
    "source_apis", "query_ids", "n_queries", "first_seen_run",
]
QUERY_COLS = [
    "query_id", "api", "band", "scope", "domain_group", "query", "status",
    "n_available", "n_results", "n_new_unique", "elapsed_s", "note",
]
# fmt: on

# OpenAlex pages at 200; arXiv is capped by --arxiv_max_results; S2 by the call limit.
OPENALEX_PER_PAGE = 200
ARXIV_PAGE = 100
S2_LIMIT = 100

csv.field_size_limit(10_000_000)


# ---------------------------------------------------------------- http


class BudgetExhaustedError(RuntimeError):
    """OpenAlex daily budget spent. Fatal: the rest of the harvest would be empty."""


def _get(
    url: str,
    params: dict[str, str],
    timeout: int = 60,
    retries: int = 3,
    headers: dict[str, str] | None = None,
) -> str:
    qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    full = f"{url}?{qs}"
    last = None
    for attempt in range(retries):
        try:
            hdrs = {"User-Agent": USER_AGENT, **(headers or {})}
            req = urllib.request.Request(full, headers=hdrs)  # noqa: S310 - scheme is from a literal base URL above
            with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 - as above
                body: str = r.read().decode("utf-8", "replace")
                return body
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code == 429:
                # Two different failures share this code. A per-second throttle is worth
                # retrying; an exhausted daily budget is not, and retrying it turns one
                # loud failure into a quiet half-corpus that every later count trusts.
                detail = e.read().decode("utf-8", "replace")[:300]
                if "budget" in detail.lower():
                    raise BudgetExhaustedError(detail) from e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2**attempt * 3)
                continue
            break
        except Exception as e:  # noqa: BLE001 - network layer, report and move on
            last = type(e).__name__
            time.sleep(2**attempt * 2)
    raise RuntimeError(last or "unknown error")


# ---------------------------------------------------------------- normalise

_WS = re.compile(r"\s+")
_NONWORD = re.compile(r"[^a-z0-9]+")


def clean(s: str | None) -> str:
    return _WS.sub(" ", (s or "").replace("\n", " ")).strip()


def title_slug(title: str) -> str:
    return _NONWORD.sub("", (title or "").lower())[:120]


def norm_doi(doi: str | None) -> str:
    if not doi:
        return ""
    d = doi.strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p) :]
    return d


def norm_arxiv(s: str | None) -> str:
    if not s:
        return ""
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", s)
    return m.group(1) if m else ""


def inverted_to_text(inv: dict[str, list[int]] | None) -> str:
    if not inv:
        return ""
    pairs = [(p, w) for w, ps in inv.items() for p in ps]
    pairs.sort()
    return clean(" ".join(w for _, w in pairs))


def identity_of(rec: Record) -> str:
    if rec.get("doi"):
        return f"doi:{rec['doi']}"
    if rec.get("arxiv_id"):
        return f"arxiv:{rec['arxiv_id']}"
    return f"title:{title_slug(rec.get('title', ''))}"


# ---------------------------------------------------------------- sources


def openalex(query: str, from_date: str, max_pages: int) -> tuple[list[Record], int]:
    out: list[Record] = []
    cursor, total = "*", 0
    select = (
        "id,doi,display_name,publication_year,authorships,primary_location,"
        "cited_by_count,type,open_access,abstract_inverted_index"
    )
    for _ in range(max_pages):
        params = {
            "filter": f"from_publication_date:{from_date},title_and_abstract.search:{query}",
            "per-page": str(OPENALEX_PER_PAGE),
            "cursor": cursor,
            "select": select,
        }
        if MAILTO:
            params["mailto"] = MAILTO
        hdrs = {"Authorization": f"Bearer {OPENALEX_API_KEY}"} if OPENALEX_API_KEY else None
        data = json.loads(_get("https://api.openalex.org/works", params, headers=hdrs))
        total = data.get("meta", {}).get("count", 0)
        for r in data.get("results", []):
            loc = r.get("primary_location") or {}
            src = loc.get("source") or {}
            oa = r.get("open_access") or {}
            out.append(
                {
                    "doi": norm_doi(r.get("doi")),
                    "arxiv_id": norm_arxiv(loc.get("landing_page_url") or ""),
                    "url": r.get("doi") or loc.get("landing_page_url") or r.get("id", ""),
                    "title": clean(r.get("display_name")),
                    "authors": "; ".join(
                        clean((a.get("author") or {}).get("display_name"))
                        for a in (r.get("authorships") or [])[:12]
                    ),
                    "year": r.get("publication_year") or "",
                    "venue": clean(src.get("display_name")),
                    "type": r.get("type") or "",
                    "cited_by": r.get("cited_by_count") or 0,
                    "oa_pdf_url": oa.get("oa_url") or "",
                    "abstract": inverted_to_text(r.get("abstract_inverted_index")),
                    "source_apis": "openalex",
                }
            )
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or len(data.get("results", [])) < OPENALEX_PER_PAGE:
            break
        time.sleep(0.2)
    return out, total


def arxiv(query: str, from_date: str, max_results: int) -> tuple[list[Record], int]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out: list[Record] = []
    start, page = 0, ARXIV_PAGE
    cutoff = from_date
    total = 0
    while start < max_results:
        params = {
            "search_query": query,
            "start": str(start),
            "max_results": str(min(page, max_results - start)),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        # S314: arXiv's own Atom feed. Not user input, and ElementTree's default
        # parser resolves no external entities.
        root = ET.fromstring(_get("http://export.arxiv.org/api/query", params))  # noqa: S314
        tot = root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults")
        if tot is not None and tot.text:
            total = int(tot.text)
        entries = root.findall("a:entry", ns)
        if not entries:
            break
        stop = False
        for e in entries:
            pub = (e.findtext("a:published", "", ns) or "")[:10]
            if pub and pub < cutoff:
                stop = True
                continue
            aid = norm_arxiv(e.findtext("a:id", "", ns))
            doi_el = e.find("{http://arxiv.org/schemas/atom}doi")
            out.append(
                {
                    "doi": norm_doi(doi_el.text if doi_el is not None else ""),
                    "arxiv_id": aid,
                    "url": f"https://arxiv.org/abs/{aid}" if aid else e.findtext("a:id", "", ns),
                    "title": clean(e.findtext("a:title", "", ns)),
                    "authors": "; ".join(
                        clean(a.findtext("a:name", "", ns)) for a in e.findall("a:author", ns)[:12]
                    ),
                    "year": pub[:4],
                    "venue": "arXiv",
                    "type": "preprint",
                    "cited_by": "",
                    "oa_pdf_url": f"https://arxiv.org/pdf/{aid}" if aid else "",
                    "abstract": clean(e.findtext("a:summary", "", ns)),
                    "source_apis": "arxiv",
                }
            )
        if stop or len(entries) < page:
            break
        start += page
        time.sleep(3)  # arXiv asks for 3s between requests
    return out, total


def semanticscholar(query: str, from_date: str, limit: int = 200) -> tuple[list[Record], int]:
    params = {
        "query": query,
        "limit": str(min(limit, S2_LIMIT)),
        "year": f"{from_date[:4]}-",
        "fields": (
            "title,abstract,year,venue,citationCount,externalIds,openAccessPdf,publicationTypes"
        ),
    }
    hdrs = {"x-api-key": S2_API_KEY} if S2_API_KEY else None
    data = json.loads(
        _get("https://api.semanticscholar.org/graph/v1/paper/search", params, headers=hdrs)
    )
    out: list[Record] = []
    for r in data.get("data", []) or []:
        ext = r.get("externalIds") or {}
        oa = r.get("openAccessPdf") or {}
        aid = norm_arxiv(ext.get("ArXiv") or "")
        out.append(
            {
                "doi": norm_doi(ext.get("DOI")),
                "arxiv_id": aid,
                "url": (
                    f"https://doi.org/{norm_doi(ext.get('DOI'))}"
                    if ext.get("DOI")
                    else (f"https://arxiv.org/abs/{aid}" if aid else "")
                ),
                "title": clean(r.get("title")),
                "authors": "",
                "year": r.get("year") or "",
                "venue": clean(r.get("venue")),
                "type": "; ".join(r.get("publicationTypes") or []),
                "cited_by": r.get("citationCount") or "",
                "oa_pdf_url": oa.get("url") or "",
                "abstract": clean(r.get("abstract")),
                "source_apis": "s2",
            }
        )
    total: int = data.get("total", len(out))
    return out, total


def api_cap(api: str, cfg: Config) -> int:
    """The most records this API can return for one query under the current config.

    Kept next to the fetch dispatch because `n_results >= cap` is how a truncated
    query is detected, and a cap that drifts from the call that produced it turns a
    paging limit into an invisible one.
    """
    if api == "openalex":
        cap: int = cfg["openalex_max_pages"] * OPENALEX_PER_PAGE
        return cap
    if api == "arxiv":
        return int(cfg["arxiv_max_results"])
    return S2_LIMIT


def fetch_api(api: str, q: Query, cfg: Config) -> tuple[list[Record], int]:
    """Run one query against one API. Dispatch by name rather than a list of closures.

    The closures this replaced captured the loop variable, so they were correct only
    because they happened to be called in the same iteration that built them.
    """
    from_date = cfg["from_date"]
    if api == "openalex":
        return openalex(q["openalex"], from_date, cfg["openalex_max_pages"])
    if api == "arxiv":
        return arxiv(q["arxiv"], from_date, cfg["arxiv_max_results"])
    return semanticscholar(q["s2"], from_date)


# ---------------------------------------------------------------- query plan

_BARE_OP = re.compile(r"\b(AND|OR|NOT)\b")


def validate_config(cfg: Config) -> None:
    """A bare AND inside an OR group makes OpenAlex return zero results with no error.

    That is the worst possible failure: the corpus is silently empty for that cell and
    every downstream count still looks plausible. Terms are single phrases; the script
    joins them. Refuse to run rather than harvest nothing.
    """
    bad: list[tuple[str, str]] = []
    for name, band in cfg["bands"].items():
        bad += [(f"bands.{name}", t) for t in band["terms"] if _BARE_OP.search(t)]
    for sname, scope in cfg["domain_groups"].items():
        for g, terms in scope["groups"].items():
            bad += [(f"{sname}.{g}", t) for t in terms if _BARE_OP.search(t)]
    if bad:
        for where, term in bad:
            print(
                f"config error: {where}: {term!r} contains a bare boolean operator",
                file=sys.stderr,
            )
        raise SystemExit("queries.json: terms must be single phrases, no AND/OR/NOT")


def build_plan(cfg: Config, bands: list[str] | None, scopes: list[str]) -> list[Query]:
    plan: list[Query] = []
    qid = 0
    for scope_name, scope in cfg["domain_groups"].items():
        if scope_name not in scopes:
            continue
        for group, dterms in scope["groups"].items():
            for band_name, band in cfg["bands"].items():
                if bands and band_name not in bands:
                    continue
                a = " OR ".join(band["terms"])
                d = " OR ".join(dterms)
                qid += 1
                plan.append(
                    {
                        "query_id": f"q{qid:03d}",
                        "band": band_name,
                        "scope": scope_name,
                        "domain_group": group,
                        "openalex": f"({a}) AND ({d})",
                        "arxiv": "("
                        + " OR ".join(f"abs:{t}" for t in band["terms"])
                        + ") AND ("
                        + " OR ".join(f"abs:{t}" for t in dterms)
                        + ")",
                        "s2": clean(band["terms"][0].strip('"') + " " + dterms[0].strip('"')),
                    }
                )
    return plan


# ---------------------------------------------------------------- merge & io


def read_csv(path: Path) -> list[Record]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, cols: list[str], rows: list[Record]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def merge(
    store: dict[str, Record], alias: dict[str, str], rec: Record, q: Query, run_id: str
) -> bool:
    """Insert or merge one record. Returns True if it was new."""
    key = identity_of(rec)
    slug = title_slug(rec["title"])
    # A preprint and its published version arrive with different keys; the title
    # slug collapses them. Without this the corpus double-counts most of arXiv.
    if key not in store and slug and slug in alias:
        key = alias[slug]
    new = key not in store
    if new:
        rec = dict(rec)
        rec["identity_key"] = key
        rec["query_ids"] = q["query_id"]
        rec["domain_group"] = q["domain_group"]
        rec["band"] = q["band"]
        rec["first_seen_run"] = run_id
        store[key] = rec
        if slug:
            alias.setdefault(slug, key)
    else:
        cur = store[key]
        qids = [x for x in cur.get("query_ids", "").split(";") if x]
        if q["query_id"] not in qids:
            qids.append(q["query_id"])
            cur["query_ids"] = ";".join(qids)
        apis = {x for x in cur.get("source_apis", "").split(";") if x}
        apis.add(rec["source_apis"])
        cur["source_apis"] = ";".join(sorted(apis))
        # Prefer the record that actually carries content.
        for fld in ("abstract", "doi", "arxiv_id", "venue", "oa_pdf_url", "authors", "cited_by"):
            if not cur.get(fld) and rec.get(fld):
                cur[fld] = rec[fld]
        if q["band"] == "A_agentic":
            cur["band"] = "A_agentic"  # precision band wins for reporting
    return new


# ---------------------------------------------------------------- main


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="run output directory")
    ap.add_argument("--config", default="reference/queries.json")
    ap.add_argument("--bands", nargs="*", default=None)
    ap.add_argument("--scopes", nargs="*", default=["core", "periphery"])
    ap.add_argument("--no-arxiv", action="store_true")
    ap.add_argument(
        "--no-s2", action="store_true", help="skip Semantic Scholar (it rate-limits without a key)"
    )
    ap.add_argument("--dry-run", action="store_true", help="print the plan, call nothing")
    ap.add_argument(
        "--limit-queries",
        type=int,
        default=0,
        help="stop after N queries. First N of the plan — all core, so periphery "
        "is skipped. Use --smoke instead for a mechanics test.",
    )
    ap.add_argument(
        "--smoke",
        action="store_true",
        help="mechanics test: seismology A_agentic, hydrogeology A_agentic, "
        "and earth_observation A_agentic (one periphery group)",
    )
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    with Path(args.config).open(encoding="utf-8") as f:
        cfg: Config = json.load(f)
    validate_config(cfg)
    plan = build_plan(cfg, args.bands, args.scopes)
    if args.smoke:
        keep = {
            ("core", "seismology", "A_agentic"),
            ("core", "hydrogeology", "A_agentic"),
            ("periphery", "earth_observation", "A_agentic"),
        }
        plan = [q for q in plan if (q["scope"], q["domain_group"], q["band"]) in keep]
    elif args.limit_queries:
        plan = plan[: args.limit_queries]

    if args.dry_run:
        for q in plan:
            print(f"{q['query_id']}  {q['scope']:9s} {q['domain_group']:22s} {q['band']}")
            print(f"    openalex: {q['openalex'][:150]}")
        print(
            f"\n{len(plan)} queries; APIs per query: openalex"
            f"{'' if args.no_arxiv else ' + arxiv'}{'' if args.no_s2 else ' + s2'}"
        )
        return 0

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    out_dir = Path(args.out)
    screened_path = out_dir / "screened.csv"
    queries_path = out_dir / "queries.csv"

    store: dict[str, Record] = {}
    alias: dict[str, str] = {}
    for r in read_csv(screened_path):
        store[r["identity_key"]] = r
        s = title_slug(r.get("title", ""))
        if s:
            alias.setdefault(s, r["identity_key"])
    existing_queries = read_csv(queries_path)
    print(f"loaded {len(store)} existing rows from {screened_path}", file=sys.stderr)

    apis = ["openalex"]
    if not args.no_arxiv:
        apis.append("arxiv")
    if not args.no_s2:
        apis.append("s2")

    qrows: list[Record] = []
    for i, q in enumerate(plan, 1):
        for api in apis:
            cap = api_cap(api, cfg)
            t0 = time.time()
            try:
                recs, total = fetch_api(api, q, cfg)
                status, note = "ok", ""
            except BudgetExhaustedError as e:
                write_csv(screened_path, SCREENED_COLS, list(store.values()))
                write_csv(queries_path, QUERY_COLS, existing_queries + qrows)
                raise SystemExit(
                    f"\nOpenAlex daily budget exhausted at {q['query_id']} "
                    f"({i}/{len(plan)} queries done). {e}\n"
                    f"Partial corpus checkpointed to {screened_path} - it is NOT a full "
                    f"harvest. Set OPENALEX_API_KEY (free key = $1/day, 10x keyless) or "
                    f"wait for the midnight-UTC reset, then re-run to merge the rest."
                ) from e
            except Exception as e:  # noqa: BLE001 - a dead API must not kill the run
                recs, total, status, note = [], 0, "error", f"{type(e).__name__}: {e}"
            n_new = sum(merge(store, alias, r, q, run_id) for r in recs)
            if status == "ok" and not recs:
                # Distinguishable only here: an empty cell is a finding, a malformed
                # query is a bug, and both look identical downstream.
                status, note = "zero", "ZERO RESULTS - verify the query is well formed"
            # The API's own result count, kept alongside what we actually pulled. Without
            # it a paging cap is invisible, and the periphery section reports the cap
            # rather than the literature. Only a run that reached the cap is truncated:
            # arXiv reports every match but the harvester drops anything before
            # from_date, so got < total is routine there and means nothing was lost.
            if status == "ok" and total > len(recs) >= cap:
                note = (
                    note + "; " if note else ""
                ) + f"TRUNCATED at paging cap ({total} available)"
            qrows.append(
                {
                    "query_id": f"{q['query_id']}:{api}",
                    "api": api,
                    "band": q["band"],
                    "scope": q["scope"],
                    "domain_group": q["domain_group"],
                    "query": q.get(api, ""),
                    "status": status,
                    "n_available": total,
                    "n_results": len(recs),
                    "n_new_unique": n_new,
                    "elapsed_s": round(time.time() - t0, 1),
                    "note": note,
                }
            )
            print(
                f"[{i}/{len(plan)}] {q['query_id']} {api:9s} {q['domain_group']:22s} "
                f"total={total:<7} got={len(recs):<5} new={n_new:<5} {status} {note}",
                file=sys.stderr,
            )
            # Checkpoint every query: a run killed at 80% keeps its corpus.
            write_csv(screened_path, SCREENED_COLS, list(store.values()))
            write_csv(queries_path, QUERY_COLS, existing_queries + qrows)

    with_abs = sum(1 for r in store.values() if r.get("abstract"))
    print(
        f"\ncorpus: {len(store)} unique, {with_abs} with abstract "
        f"({100 * with_abs // max(len(store), 1)}%), {len(qrows)} api calls",
        file=sys.stderr,
    )
    print(f"wrote {screened_path} and {queries_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
