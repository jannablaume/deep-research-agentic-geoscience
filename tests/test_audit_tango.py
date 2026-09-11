"""audit_tango.py, tested the way audit.py is: one passing run, then one mutation each.

A passing baseline proves the 02 contract is satisfiable at all — which matters more here
than for 01, because 02 asks for three artifacts nobody has written yet and a contract
that cannot be satisfied is discovered halfway through a long run or not at all.

The mutations cover the checks that are **new in 02**. The dozen it shares with `audit.py`
(screening integrity, recall audit, citations, evidence tags) are the same code over the
same files and are mutation-tested in `test_audit.py`; repeating them here would test the
copy rather than the contract.
"""

from __future__ import annotations

import csv
from collections.abc import Callable, Sequence
from pathlib import Path

import pytest

import audit_tango
from audit import PAPERS_COLS
from audit_tango import TRANSFER_COLS

N_AUDIT = 40
CORE_KEY = "doi:10.1000/core-a"
CONTEXT_KEY = "doi:10.1000/ctx-b"
ADMITTED = [CORE_KEY, CONTEXT_KEY]

TOUCHPOINT_NAMES = sorted(audit_tango.TOUCHPOINTS - {"none"})


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
            "title": "An agent that sets up a flowsheet simulation",
            "authors": "Doe, J.",
            "year": "2025",
            "venue": "Journal of Test Simulation",
            "source_type": "preprint",
            "subfield": "simulation_orchestration",
            "task": "generating a process flowsheet from a text description",
            "agentic_techniques": "tool-calling;planning",
            "architecture": "agent-plus-simulator",
            "base_model": "GPT-4o",
            "tools_used": "Aspen Plus; Python",
            "evaluation_method": "ten case studies",
            "baseline": "manual setup",
            "held_out": "yes",
            "data_type": "benchmark",
            "reported_result": "8 of 10 flowsheets converged",
            "maturity_claimed": "a viable route to automated process design",
            "maturity_demonstrated": "M2",
            "author_stated_limitations": "single simulator, single fluid package",
            "code_availability": "public",
            "access_status": "full-text" if tier == "core" else "abstract-only",
            "found_via": "harvest",
        }
    )
    row.update(over)
    return row


def _transfer(key: str, **over: str) -> dict[str, str]:
    row = {
        "identity_key": key,
        "system_id": key.rsplit("/", 1)[-1],
        "tango_touchpoints": "config-generation;solver-control",
        "what_it_drives": "an Aspen Plus flowsheet",
        "interface": "api",
        "autonomy": "executes-and-iterates",
        "failure_handling": "retries once on a convergence failure, then reports it",
        "access_status": "full-text",
    }
    row.update(over)
    return row


@pytest.fixture
def make_tango_run(tmp_path: Path) -> Callable[[], Path]:
    """A factory writing the smallest 02 run directory that passes every check."""

    def _build() -> Path:
        out = tmp_path / "v0.1"
        (out / "report").mkdir(parents=True)

        audit_keys = [f"doi:10.1000/below-{i:03d}" for i in range(N_AUDIT)]
        rejected = ["doi:10.1000/out-x"]
        all_keys = [*ADMITTED, *audit_keys, *rejected]

        _write_csv(
            out / "screened.csv",
            ["identity_key", "title", "abstract", "source_apis", "query_ids"],
            [
                {
                    "identity_key": k,
                    "title": f"Record {k}",
                    "abstract": "An abstract, so the corpus does not read as title-only.",
                    "source_apis": "openalex",
                    "query_ids": "q001",
                }
                for k in all_keys
            ],
        )
        _write_csv(
            out / "triage.csv",
            ["identity_key", "agentic_score", "strong_hits", "domain_score"],
            [
                {"identity_key": k, "agentic_score": "9", "strong_hits": "2", "domain_score": "3"}
                for k in all_keys
            ],
        )
        _write_csv(
            out / "queries.csv",
            ["query_id", "api", "band", "scope", "domain_group", "query", "status", "n_results"],
            [
                {
                    "query_id": "q001:openalex",
                    "api": "openalex",
                    "band": "A_agentic",
                    "scope": "core",
                    "domain_group": "simulation_orchestration",
                    "query": "(agentic AI) AND (process simulation)",
                    "status": "ok",
                    "n_results": "44",
                }
            ],
        )

        screening = [
            {"identity_key": k, "decision": "in", "cut_reason": "", "from_audit_sample": "no"}
            for k in ADMITTED
        ]
        screening += [
            {
                "identity_key": k,
                "decision": "out",
                "cut_reason": "no-simulation-target",
                "from_audit_sample": "yes",
            }
            for k in audit_keys
        ]
        screening += [
            {
                "identity_key": k,
                "decision": "out",
                "cut_reason": "not-agentic",
                "from_audit_sample": "no",
            }
            for k in rejected
        ]
        _write_csv(
            out / "screening.csv",
            ["identity_key", "decision", "cut_reason", "from_audit_sample", "subfield"],
            screening,
        )

        (out / "shortlist.md").write_text(
            "# Shortlist\n\n" + "".join(f"### {k}\n**A record**\n\n" for k in ADMITTED),
            encoding="utf-8",
        )
        (out / "audit_sample.md").write_text(
            "# Recall audit\n\n" + "".join(f"### {k}\n**A record**\n\n" for k in audit_keys),
            encoding="utf-8",
        )
        (out / "triage_stats.md").write_text("# Triage statistics\n", encoding="utf-8")

        _write_csv(
            out / "papers.csv",
            PAPERS_COLS,
            [_paper(CORE_KEY, "core"), _paper(CONTEXT_KEY, "context")],
        )
        (out / "papers.md").write_text(
            f"# Extracts\n\n## {CORE_KEY}\n"
            "https://example.org/core-a — accessed 2026-09-11\n"
            '- "The agent writes the flowsheet file and calls the simulator."\n'
            "- NOT FOUND: any statement about runtime cost\n",
            encoding="utf-8",
        )
        _write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [
                _transfer(CORE_KEY),
                _transfer(
                    CONTEXT_KEY,
                    tango_touchpoints="none",
                    what_it_drives="not stated",
                    interface="not stated",
                    autonomy="not stated",
                    failure_handling="not stated",
                    access_status="abstract-only",
                ),
            ],
        )
        (out / "transfer.md").write_text(
            f"# Transfer extracts\n\n## {CORE_KEY}\n"
            '- config-generation: "The agent emits a complete input file for each case."\n'
            '- solver-control: "On a convergence failure it lowers the step size and retries."\n'
            "- NOT FOUND: any statement about parallel execution\n",
            encoding="utf-8",
        )
        # The one admitted source nobody could read, listed the way SCHEMA_tango.md wants.
        (out / "paywalled.md").write_text(
            "# Paywalled and unreadable\n\n"
            "| identity_key | title | url | venue | blocked_by | tried | local_pdf | would_change |\n"
            "|---|---|---|---|---|---|---|---|\n"
            f"| `{CONTEXT_KEY}` | A context source | https://example.org/ctx-b | J. Test | "
            "paywall | publisher DOI; Unpaywall; arXiv | no | would support a core write-up |\n",
            encoding="utf-8",
        )
        (out / "unreachable.md").write_text("# Unreachable\n\nNone.\n", encoding="utf-8")
        (out / "RUN.md").write_text(
            "# Run record\n\n- date: 2026-09-11\n- prompt: prompts/02_tango.md v0.1\n"
            "- prompt commit: deadbee\n- model: test\n- triage threshold: 3/1/2\n",
            encoding="utf-8",
        )

        (out / "report" / "00_executive_summary.md").write_text(
            "# Executive summary\n\n"
            "[Certain] Two sources were admitted, of which one was read in full text and "
            "carries a verbatim extract for every characterisation made of it in the "
            f"sections that follow [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "01_control_patterns.md").write_text(
            "# Control patterns\n\n"
            "[Likely] The one readable system emits a complete input file and calls the "
            "simulator itself, which is the pattern the abstract of the second source also "
            f"describes without giving enough detail to confirm it [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "02_architectures.md").write_text(
            "# Architectures\n\n"
            "[Absent-searched] No hierarchical multi-agent design appears in the admitted "
            "set; the query that would have found one is q001, which returned 44 records "
            "and none of them described more than one planning agent.\n",
            encoding="utf-8",
        )
        (out / "report" / "03_touchpoints.md").write_text(
            "# Touchpoints\n\n"
            + "".join(
                f"## {name}\n\n[Certain] One admitted source bears on `{name}`, and the "
                "count here is per system rather than per source, of which there is "
                f"exactly one either way [[{CORE_KEY}]].\n\n"
                for name in TOUCHPOINT_NAMES
            ),
            encoding="utf-8",
        )
        (out / "report" / "05_maturity.md").write_text(
            "# Maturity\n\n"
            "[Certain] The single core system reaches M2: it is evaluated on a reusable "
            "benchmark rather than on a named site, and its own authors describe the result "
            f"in those terms [[{CORE_KEY}]].\n",
            encoding="utf-8",
        )
        (out / "report" / "08_papers.md").write_text(
            f"# Papers\n\n- [[{CORE_KEY}]] An agent that sets up a flowsheet.\n"
            f"- [context] [[{CONTEXT_KEY}]] A context source.\n",
            encoding="utf-8",
        )
        (out / "report" / "index.md").write_text(
            "# Report\n\nSee the sections.\n", encoding="utf-8"
        )
        return out

    return _build


def results(out: Path, capsys: pytest.CaptureFixture[str]) -> dict[str, str]:
    audit_tango.main(["--out", str(out)])
    table = capsys.readouterr().out
    return {
        line.split("|")[1].strip(): line.split("|")[2].strip()
        for line in table.splitlines()
        if line.startswith("|") and "---" not in line and "Check" not in line
    }


class TestBaseline:
    def test_the_contract_is_satisfiable(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        assert audit_tango.main(["--out", str(out)]) == 0
        failed = [k for k, v in results(out, capsys).items() if v != "PASS"]
        assert failed == []

    def test_the_battery_is_the_length_the_tests_cover(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # A new check must come with the fixture change that exercises it, or it is
        # decoration that nothing proves is load-bearing.
        assert len(results(make_tango_run(), capsys)) == 38

    def test_it_writes_audit_md(self, make_tango_run: Callable[[], Path]) -> None:
        out = make_tango_run()
        audit_tango.main(["--out", str(out)])
        assert "Self-audit" in (out / "audit.md").read_text(encoding="utf-8")


class TestTransferGrid:
    def test_a_missing_transfer_row_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        _write_csv(out / "transfer.csv", TRANSFER_COLS, [_transfer(CORE_KEY)])
        assert results(out, capsys)["transfer.csv covers the admitted set exactly"] == "FAIL"

    def test_a_transfer_row_for_an_unadmitted_source_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        _write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [_transfer(CORE_KEY), _transfer(CONTEXT_KEY), _transfer("doi:10.1000/ghost")],
        )
        assert results(out, capsys)["transfer.csv covers the admitted set exactly"] == "FAIL"

    def test_a_reordered_transfer_header_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        cols = [TRANSFER_COLS[1], TRANSFER_COLS[0], *TRANSFER_COLS[2:]]
        _write_csv(out / "transfer.csv", cols, [_transfer(CORE_KEY), _transfer(CONTEXT_KEY)])
        assert results(out, capsys)["transfer.csv columns match SCHEMA_tango"] == "FAIL"

    @pytest.mark.parametrize("value", ["config-generation;made-up", "", "free text"])
    def test_a_touchpoint_outside_the_controlled_list_fails(
        self,
        make_tango_run: Callable[[], Path],
        capsys: pytest.CaptureFixture[str],
        value: str,
    ) -> None:
        # Free text in this column is what turns a counted grid back into a list.
        out = make_tango_run()
        _write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [_transfer(CORE_KEY, tango_touchpoints=value), _transfer(CONTEXT_KEY)],
        )
        assert results(out, capsys)["Touchpoints are from the controlled list"] == "FAIL"

    @pytest.mark.parametrize(
        ("field", "value"),
        [("interface", "REST"), ("autonomy", "fully autonomous"), ("interface", "")],
    )
    def test_an_interface_or_autonomy_value_outside_the_list_fails(
        self,
        make_tango_run: Callable[[], Path],
        capsys: pytest.CaptureFixture[str],
        field: str,
        value: str,
    ) -> None:
        out = make_tango_run()
        _write_csv(
            out / "transfer.csv",
            TRANSFER_COLS,
            [_transfer(CORE_KEY, **{field: value}), _transfer(CONTEXT_KEY)],
        )
        key = "Interface and autonomy values are from the controlled lists"
        assert results(out, capsys)[key] == "FAIL"

    def test_a_core_paper_with_no_transfer_block_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        (out / "transfer.md").write_text("# Transfer extracts\n\nNothing.\n", encoding="utf-8")
        assert results(out, capsys)["Every core paper has a transfer extract block"] == "FAIL"

    def test_a_transfer_block_that_only_paraphrases_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # A touchpoint resting on a paraphrase is a characterisation nobody can check.
        out = make_tango_run()
        (out / "transfer.md").write_text(
            f"# Transfer extracts\n\n## {CORE_KEY}\n"
            "- config-generation: the agent writes the input file itself.\n",
            encoding="utf-8",
        )
        key = "Transfer blocks carry a quote or an explicit NOT FOUND"
        assert results(out, capsys)[key] == "FAIL"


class TestPaywallLedger:
    def test_an_abstract_only_source_missing_from_paywalled_md_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # This is the check that makes the handoff list complete rather than partial:
        # every source nobody could read is one somebody else might be able to.
        out = make_tango_run()
        (out / "paywalled.md").write_text("# Paywalled\n\nNone.\n", encoding="utf-8")
        key = "Every abstract-only source is listed in paywalled.md"
        assert results(out, capsys)[key] == "FAIL"

    def test_an_unknown_blocked_by_value_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        text = (out / "paywalled.md").read_text(encoding="utf-8")
        (out / "paywalled.md").write_text(
            text.replace("| paywall |", "| too expensive |"), encoding="utf-8"
        )
        key = "paywalled.md blocked_by values are from the controlled list"
        assert results(out, capsys)[key] == "FAIL"

    def test_bot_protection_is_a_valid_value_distinct_from_paywall(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # The v0.5 run found a gold-OA paper no route could retrieve. An OA flag is a
        # licence status, not an access outcome, and the two must stay countable apart.
        out = make_tango_run()
        text = (out / "paywalled.md").read_text(encoding="utf-8")
        (out / "paywalled.md").write_text(
            text.replace("| paywall |", "| bot-protection |"), encoding="utf-8"
        )
        key = "paywalled.md blocked_by values are from the controlled list"
        assert results(out, capsys)[key] == "PASS"


class TestScreeningVocabulary:
    def test_an_01_cut_reason_fails_here(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # `not-geoscience` is 01's vocabulary; this run cuts on `no-simulation-target`,
        # and the two are not the same judgment.
        out = make_tango_run()
        rows = list(csv.DictReader((out / "screening.csv").open(encoding="utf-8")))
        rows[-1]["cut_reason"] = "not-geoscience"
        _write_csv(out / "screening.csv", list(rows[0].keys()), rows)
        assert results(out, capsys)["Cut reasons are from the 02 vocabulary"] == "FAIL"

    def test_an_01_subfield_fails_here(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_tango_run()
        _write_csv(
            out / "papers.csv",
            PAPERS_COLS,
            [_paper(CORE_KEY, "core", subfield="seismology"), _paper(CONTEXT_KEY, "context")],
        )
        assert results(out, capsys)["Subfields are from the 02 vocabulary"] == "FAIL"


class TestReport:
    @pytest.mark.parametrize(
        "sentence",
        [
            "TANGO should expose its unit registry as tools.",
            "We recommend the same split for the boundary-condition solver.",
            "This suggests a roadmap for TANGO built around config generation.",
            "TANGO would benefit from the same validation step.",
        ],
    )
    def test_prescription_fails(
        self,
        make_tango_run: Callable[[], Path],
        capsys: pytest.CaptureFixture[str],
        sentence: str,
    ) -> None:
        # The run describes a literature. The moment it tells TANGO what to build it is
        # no longer reporting what it read.
        out = make_tango_run()
        path = out / "report" / "01_control_patterns.md"
        path.write_text(path.read_text(encoding="utf-8") + f"\n[Likely] {sentence}\n", "utf-8")
        assert results(out, capsys)["No prescription for TANGO"] == "FAIL"

    def test_describing_what_a_system_did_passes(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # The counterpart to the test above: the check must not fire on the report's
        # actual job, which is naming TANGO's surfaces while describing other people's
        # systems.
        out = make_tango_run()
        path = out / "report" / "01_control_patterns.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n[Certain] Three systems generate a complete input file and validate it "
            "against a schema before running it, which is the touchpoint TANGO's YAML "
            f"graph corresponds to [[{CORE_KEY}]].\n",
            "utf-8",
        )
        assert results(out, capsys)["No prescription for TANGO"] == "PASS"

    def test_a_touchpoint_with_no_subsection_fails(
        self, make_tango_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # A section that silently omits its empty categories reads as a survey of what
        # exists rather than of what was looked for.
        out = make_tango_run()
        path = out / "report" / "03_touchpoints.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("## hpc-scale-out", "## something else"), encoding="utf-8")
        assert results(out, capsys)["03_touchpoints.md covers every touchpoint"] == "FAIL"


class TestVacuousPasses:
    def test_an_empty_run_fails_rather_than_passing_vacuously(self, tmp_path: Path) -> None:
        out = tmp_path / "empty"
        (out / "report").mkdir(parents=True)
        assert audit_tango.main(["--out", str(out)]) == 1
