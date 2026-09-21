"""export_web_tango.py's own parsers and counters.

`papers.csv`, `RUN.md`, `audit.md` and friends share export_web.py's parsers by
import, and those are already covered in test_export_web.py. What is tested here is
what is new: `transfer.csv`, `paywalled.md`, the 02 vocabulary, and the `touchpoints`
report group.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

import export_web_tango as ewt
from audit import PAPERS_COLS
from conftest import ADMITTED, CONTEXT_KEYS, CORE_KEY, _paper, _write_csv

TRANSFER_COLS = [
    "identity_key",
    "system_id",
    "tango_touchpoints",
    "what_it_drives",
    "interface",
    "autonomy",
    "failure_handling",
    "access_status",
]


def test_parse_transfer_splits_touchpoints_and_defaults_none() -> None:
    rows = [
        {
            "identity_key": CORE_KEY,
            "system_id": "TESTFLOW",
            "tango_touchpoints": "config-generation;solver-control",
            "what_it_drives": "an OpenFOAM case directory",
            "interface": "api",
            "autonomy": "executes-and-iterates",
            "failure_handling": "retries with a smaller timestep",
            "access_status": "full-text",
        },
        {
            "identity_key": "doi:10.1000/ctx-b",
            "system_id": "CTXFLOW",
            "tango_touchpoints": "",
            "what_it_drives": "not stated",
            "interface": "",
            "autonomy": "",
            "failure_handling": "",
            "access_status": "abstract-only",
        },
    ]
    parsed = ewt.parse_transfer(rows)
    assert parsed[CORE_KEY]["touchpoints"] == ["config-generation", "solver-control"]
    assert parsed[CORE_KEY]["interface"] == "api"
    # An unclaimed row defaults to `["none"]` rather than an empty list, so a
    # multi-valued facet counted over it still gets a bar for "none".
    assert parsed["doi:10.1000/ctx-b"]["touchpoints"] == ["none"]
    assert parsed["doi:10.1000/ctx-b"]["interface"] == "not stated"
    assert parsed["doi:10.1000/ctx-b"]["autonomy"] == "not stated"


PAYWALLED_MD = """# Paywalled sources

One row per source whose full text could not be retrieved.

| identity_key | title | url | venue | blocked_by | tried | local_pdf | would_change |
|---|---|---|---|---|---|---|---|
| doi:10.1/a | A | https://x/a | V | paywall | doi; unpaywall | no | the tier it would support |
| doi:10.1/b | B | https://x/b | V | bot-protection | doi | no | nothing |
| doi:10.1/c | C | https://x/c | V | paywall | doi | no | nothing |

## Recovered by hand

None.
"""


def test_parse_paywalled_counts_rows_and_blocked_by() -> None:
    result = ewt.parse_paywalled(PAYWALLED_MD)
    assert result["total"] == 3
    assert result["would_change_nothing"] == 2
    by_label = {f["label"]: f["n"] for f in result["blocked_by"]}
    assert by_label["paywall"] == 2
    assert by_label["bot-protection"] == 1


def test_parse_paywalled_empty_file_is_zero_not_a_crash() -> None:
    result = ewt.parse_paywalled("# Paywalled sources\n\nNone.\n")
    assert result == {"total": 0, "blocked_by": [], "would_change_nothing": 0}


@pytest.fixture
def make_tango_run(tmp_path: Path) -> Callable[[], Path]:
    """A minimal `02_tango`-shaped run directory, built the way `make_run` builds
    a `01_landscape` one in `conftest.py` — just enough for `build()` to run over
    every branch, not enough to satisfy `audit_tango.py`'s 38 checks."""

    def _build() -> Path:
        out = tmp_path / "v0.1"
        (out / "report").mkdir(parents=True)

        papers = [
            _paper(
                CORE_KEY,
                "core",
                subfield="solver_control",
                access_status="full-text",
            ),
            *(
                _paper(
                    k, "context", subfield="simulation_orchestration", access_status="abstract-only"
                )
                for k in CONTEXT_KEYS
            ),
        ]
        _write_csv(out / "papers.csv", PAPERS_COLS, papers)

        (out / "papers.md").write_text(
            f"# Extracts\n\n## {CORE_KEY}\n"
            "https://example.org/core-a — accessed 2026-09-01\n"
            '- "The agent writes a solver input deck and re-runs on failure."\n'
            "- maturity_claimed: M2\n"
            "- limitation: single solver family\n",
            encoding="utf-8",
        )

        _write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [
                {
                    "identity_key": CORE_KEY,
                    "system_id": papers[0]["system_id"],
                    "tango_touchpoints": "solver-control;verification-regression",
                    "what_it_drives": "an in-house finite-element solver, unnamed",
                    "interface": "cli",
                    "autonomy": "executes-with-approval",
                    "failure_handling": "reruns with a relaxed convergence tolerance",
                    "access_status": "full-text",
                },
                *(
                    {
                        "identity_key": k,
                        "system_id": p["system_id"],
                        "tango_touchpoints": "",
                        "what_it_drives": "not stated",
                        "interface": "",
                        "autonomy": "",
                        "failure_handling": "",
                        "access_status": "abstract-only",
                    }
                    for k, p in zip(CONTEXT_KEYS, papers[1:], strict=True)
                ),
            ],
        )

        _write_csv(
            out / "screening.csv",
            ["identity_key", "decision", "cut_reason", "from_audit_sample", "subfield"],
            [
                {
                    "identity_key": k,
                    "decision": "in",
                    "cut_reason": "",
                    "from_audit_sample": "no",
                    "subfield": "",
                }
                for k in ADMITTED
            ]
            + [
                {
                    "identity_key": "doi:10.1000/out-x",
                    "decision": "out",
                    "cut_reason": "no-simulation-target",
                    "from_audit_sample": "no",
                    "subfield": "",
                },
                {
                    "identity_key": "doi:10.1000/out-y",
                    "decision": "out",
                    "cut_reason": "periphery",
                    "from_audit_sample": "no",
                    "subfield": "software_engineering",
                },
            ],
        )
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
                    "domain_group": "solver_control",
                    "query": "(agentic AI) AND (finite element)",
                    "status": "ok",
                    "n_available": "50",
                    "n_results": "10",
                    "n_new_unique": "10",
                },
                {
                    "query_id": "q021:openalex",
                    "api": "openalex",
                    "band": "A_agentic",
                    "scope": "periphery",
                    "domain_group": "software_engineering",
                    "query": "(agentic AI) AND (software engineering)",
                    "status": "ok",
                    "n_available": "9000",
                    "n_results": "200",
                    "n_new_unique": "200",
                },
            ],
        )
        (out / "audit.md").write_text(
            "# Self-audit\n\n"
            "| Check | Result | Detail |\n|---|---|---|\n"
            "| screened.csv parses and is non-empty | PASS | 35054 rows |\n"
            "| Every shortlist record was screened | PASS | all 773 shortlisted |\n",
            encoding="utf-8",
        )
        (out / "shortlist.md").write_text(
            "# Shortlist\n\n"
            f"### {CORE_KEY}\n**A record** · core/solver_control · deterministic\n\n",
            encoding="utf-8",
        )
        (out / "unreachable.md").write_text("# Unreachable\n\nNone.\n", encoding="utf-8")
        (out / "paywalled.md").write_text(PAYWALLED_MD, encoding="utf-8")
        (out / "RUN.md").write_text(
            "# Run record\n\n"
            "- date: 2026-09-11\n"
            "- prompt: prompts/02_tango.md v0.1\n"
            "- prompt commit: deadbee\n"
            "- model: test\n",
            encoding="utf-8",
        )
        (out / "report" / "00_executive_summary.md").write_text(
            f"# Executive summary\n\n[Certain] One system was admitted [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "03_touchpoints.md").write_text(
            "# Touchpoints\n\n"
            f"[Certain] `solver-control` is claimed by one core system [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "08_papers.md").write_text(
            f"# Papers\n\n- [[{CORE_KEY}]] An agent that drives a solver.\n",
            encoding="utf-8",
        )
        return out

    return _build


def test_build_end_to_end(make_tango_run: Callable[[], Path]) -> None:
    out = make_tango_run()
    data = ewt.build(out)

    assert data["run"]["admitted"] == 3
    assert data["run"]["core"] == 1
    assert data["run"]["context"] == 2

    funnel_labels = [row["label"] for row in data["funnel"]]
    assert "Excluded for no simulation target" in funnel_labels
    assert "Admitted as agentic and driving a simulation target" in funnel_labels

    fields = {f["label"]: f for f in data["fields"]}
    assert fields["solver_control"]["core"] == 1
    assert fields["simulation_orchestration"]["context"] == 2

    touchpoints = {t["label"]: t["n"] for t in data["transfer"]["touchpoints"]}
    assert touchpoints["solver-control"] == 1
    assert touchpoints["verification-regression"] == 1
    assert touchpoints["none"] == 0  # the only core row claims two touchpoints

    assert data["transfer"]["failure_handling"] == {"stated": 1, "not_stated": 0, "total": 1}
    assert data["paywalled"]["total"] == 3

    groups = {s["id"]: s["group"] for s in data["report"]}
    assert groups["03_touchpoints"] == "touchpoints"
    assert groups["00_executive_summary"] == "overview"

    unresolved = [
        sp
        for s in data["report"]
        for b in s["blocks"]
        if b["kind"] == "para"
        for sp in b["spans"]
        if sp["t"] == "cite" and not sp["resolved"]
    ]
    assert unresolved == []


def test_build_exits_when_papers_csv_missing(tmp_path: Path) -> None:
    with pytest.raises(SystemExit):
        ewt.build(tmp_path / "empty")


def test_main_writes_json(make_tango_run: Callable[[], Path], tmp_path: Path) -> None:
    out = make_tango_run()
    to = tmp_path / "written" / "tango.web.json"
    rc = ewt.main(["--out", str(out), "--to", str(to)])
    assert rc == 0
    assert to.exists()
    assert to.stat().st_size > 0
