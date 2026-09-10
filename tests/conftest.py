"""Fixtures that build a complete, contract-satisfying run directory.

`scripts/audit.py` is 26 checks over a directory of files, so the only useful way
to test it is against a directory. `make_run` writes the smallest one that passes
every check; the tests then break exactly one thing and assert that exactly the
corresponding check fails. That shape is what stops a check from quietly becoming
vacuous — a passing baseline proves the contract is satisfiable at all, and each
mutation proves one check is still load-bearing.
"""

from __future__ import annotations

import csv
from collections.abc import Callable, Sequence
from pathlib import Path

import pytest

from audit import PAPERS_COLS

# Enough audit-sample rows to clear audit.py's `len(audited) >= 40` floor.
N_AUDIT = 40

CORE_KEY = "doi:10.1000/core-a"
CONTEXT_KEYS = ["doi:10.1000/ctx-b", "arxiv:2501.00001"]
ADMITTED = [CORE_KEY, *CONTEXT_KEYS]


def _write_csv(path: Path, cols: Sequence[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(cols), quoting=csv.QUOTE_ALL, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def _paper(key: str, tier: str, **over: str) -> dict[str, str]:
    row = dict.fromkeys(PAPERS_COLS, "")
    row.update(
        {
            "identity_key": key,
            "tier": tier,
            "system_id": key.rsplit("/", 1)[-1],
            "url": f"https://example.org/{key}",
            "title": "An agent for picking seismic phases",
            "authors": "Doe, J.",
            "year": "2025",
            "venue": "Journal of Test Geoscience",
            "source_type": "journal",
            "subfield": "seismology",
            "task": "phase picking",
            "agentic_techniques": "tool-calling;planning",
            "architecture": "single-agent",
            "base_model": "GPT-4o",
            "tools_used": "ObsPy; SeisBench",
            "evaluation_method": "benchmark",
            "baseline": "PhaseNet",
            "held_out": "yes",
            "data_type": "benchmark",
            "reported_result": "F1 0.91",
            "maturity_claimed": "M2",
            "maturity_demonstrated": "M2",
            "author_stated_limitations": "single region",
            "code_availability": "public",
            # Not abstract-only: audit.py allows at most len(core)//5 of those, which
            # is zero when there is one core paper.
            "access_status": "full-text",
            "found_via": "q001",
        }
    )
    row.update(over)
    return row


@pytest.fixture
def make_run(tmp_path: Path) -> Callable[[], Path]:
    """Return a factory that writes a run directory passing every audit check."""

    def _build() -> Path:
        out = tmp_path / "v9.9"
        (out / "report").mkdir(parents=True)

        audit_keys = [f"doi:10.1000/below-{i:03d}" for i in range(N_AUDIT)]
        rejected = ["doi:10.1000/out-x"]
        all_keys = [*ADMITTED, *audit_keys, *rejected]

        # --- the corpus, and the triage pass over it
        screened = [
            {
                "identity_key": k,
                "title": f"Record {k}",
                "abstract": "An abstract, so the corpus does not read as title-only.",
                "source_apis": "openalex",
                "query_ids": "q001",
            }
            for k in all_keys
        ]
        _write_csv(
            out / "screened.csv",
            ["identity_key", "title", "abstract", "source_apis", "query_ids"],
            screened,
        )
        _write_csv(
            out / "triage.csv",
            ["identity_key", "agentic_score", "strong_hits"],
            [{"identity_key": k, "agentic_score": "9", "strong_hits": "2"} for k in all_keys],
        )

        # --- the query log
        _write_csv(
            out / "queries.csv",
            [
                "query_id",
                "api",
                "band",
                "scope",
                "domain_group",
                "query",
                "status",
                "n_available",
                "n_results",
                "n_new_unique",
            ],
            [
                {
                    "query_id": "q001:openalex",
                    "api": "openalex",
                    "band": "A_agentic",
                    "scope": "core",
                    "domain_group": "seismology",
                    "query": "(agentic AI) AND (seismology)",
                    "status": "ok",
                    "n_available": "120",
                    "n_results": "44",
                    "n_new_unique": "44",
                }
            ],
        )

        # --- screening decisions: the admitted set, the audit sample, one plain reject
        screening = [
            {"identity_key": k, "decision": "in", "cut_reason": "", "from_audit_sample": "no"}
            for k in ADMITTED
        ]
        screening += [
            {
                "identity_key": k,
                "decision": "out",
                "cut_reason": "not-agentic",
                "from_audit_sample": "yes",
            }
            for k in audit_keys
        ]
        screening += [
            {
                "identity_key": k,
                "decision": "out",
                "cut_reason": "not-geoscience",
                "from_audit_sample": "no",
            }
            for k in rejected
        ]
        _write_csv(
            out / "screening.csv",
            ["identity_key", "decision", "cut_reason", "from_audit_sample", "subfield"],
            screening,
        )

        # --- the digests triage.py writes, which audit.py cross-checks against screening
        (out / "shortlist.md").write_text(
            "# Shortlist\n\n" + "".join(f"### {k}\n**A record**\n\n" for k in ADMITTED),
            encoding="utf-8",
        )
        (out / "audit_sample.md").write_text(
            "# Recall audit\n\n" + "".join(f"### {k}\n**A record**\n\n" for k in audit_keys),
            encoding="utf-8",
        )
        (out / "triage_stats.md").write_text("# Triage statistics\n", encoding="utf-8")

        # --- the admitted grid and the extracts behind the core row
        _write_csv(
            out / "papers.csv",
            PAPERS_COLS,
            [_paper(CORE_KEY, "core"), *(_paper(k, "context") for k in CONTEXT_KEYS)],
        )
        (out / "papers.md").write_text(
            f"# Extracts\n\n## {CORE_KEY}\n"
            f"https://example.org/core-a — accessed 2026-09-01\n"
            f'- "The agent calls ObsPy to fetch waveforms."\n'
            f"- maturity_claimed: M2\n"
            f"- limitation: single region\n"
            f"- NOT FOUND: any statement about runtime cost\n",
            encoding="utf-8",
        )

        (out / "unreachable.md").write_text("# Unreachable\n\nNone.\n", encoding="utf-8")
        (out / "RUN.md").write_text(
            "# Run record\n\n"
            "- date: 2026-09-09\n"
            "- prompt: prompts/01_landscape_neutral.md v0.5\n"
            "- prompt commit: deadbee\n"
            "- model: test\n"
            "- triage threshold: 3\n",
            encoding="utf-8",
        )

        # --- the report. Five sections, because audit.py wants at least five; every
        # paragraph over 25 words carries an evidence tag, and the one absence claim
        # cites the query that looked.
        (out / "report" / "00_executive_summary.md").write_text(
            "# Executive summary\n\n"
            "[Certain] Three sources were admitted, of which one was read in full text "
            "and carries a verbatim extract for every characterisation made of it in "
            f"the sections that follow [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "01_techniques.md").write_text(
            "# Techniques\n\n"
            "[Likely] Tool-calling and planning are the two techniques named by the "
            "admitted systems, though the sample is far too small for that pairing to "
            f"mean anything beyond this corpus [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "02_architectures.md").write_text(
            "# Architectures\n\n"
            "[Absent-searched] No multi-agent architecture appears in the admitted set; "
            "the query that would have found one is q001, which returned 44 records and "
            "none of them described more than a single agent.\n",
            encoding="utf-8",
        )
        (out / "report" / "05_maturity.md").write_text(
            "# Maturity\n\n"
            "[Certain] The single core system reaches M2: it is evaluated on a reusable "
            "benchmark rather than on field data from a named site, and the authors say "
            f"so themselves [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "08_papers.md").write_text(
            f"# Papers\n\n- [[{CORE_KEY}]] An agent that picks seismic phases.\n"
            + "".join(f"- [context] [[{k}]] A context source.\n" for k in CONTEXT_KEYS),
            encoding="utf-8",
        )
        (out / "report" / "index.md").write_text(
            "# Report\n\nSee the sections.\n", encoding="utf-8"
        )
        return out

    return _build
