"""audit_gaps.py: one passing gaps run, then one mutation per check that carries it.

The 03 run has a failure mode the other two do not — a gap that reads well and rests on
nothing — so the checks that matter here are the three that make that impossible: every
gap cites candidates that exist, every gap carries a verdict a verification pass returned,
and every candidate is either used or discarded with a reason.

The fixture is also the worked example of the `gaps.md` format, which is a format rather
than a suggestion because this script parses it.
"""

from __future__ import annotations

import csv
from collections.abc import Callable
from pathlib import Path

import pytest

import audit_gaps
from gaps import CANDIDATE_COLS

CANDIDATES = [
    {
        "candidate_id": "c001",
        "run": "01_landscape/v0.5",
        "kind": "author-limitation",
        "subject": "SomeSystem",
        "statement": "single region, no transfer tested",
        "evidence_ref": "doi:10.1/a",
        "count": "",
        "denominator": "",
    },
    {
        "candidate_id": "c002",
        "run": "01_landscape/v0.5",
        "kind": "evaluation-hole",
        "subject": "held_out",
        "statement": "21 of 30 deep-read systems report no held-out evaluation.",
        "evidence_ref": "papers.csv (tier core)",
        "count": "21",
        "denominator": "30",
    },
    {
        "candidate_id": "c003",
        "run": "02_tango/v0.1",
        "kind": "empty-category",
        "subject": "hpc-scale-out",
        "statement": "Touchpoint `hpc-scale-out` is claimed by no admitted source.",
        "evidence_ref": "transfer.csv",
        "count": "0",
        "denominator": "40",
    },
]

GAPS_MD = """# Gaps

## G01 — No admitted system reports a held-out evaluation of a driven simulator

- candidates: c001; c002
- runs: 01_landscape/v0.5; 02_tango/v0.1
- verdict: confirmed-absent
- evidence: q041; q052
- checked: 2026-09-11

[Certain] Twenty-one of thirty deep-read systems report no held-out evaluation, and the
one system whose limitation section addresses generalisation states that it was tested in
a single region with no transfer tested.

## G02 — Nothing in either corpus drives a simulation across an HPC batch

- candidates: c003
- runs: 02_tango/v0.1
- verdict: partially-addressed
- evidence: doi:10.1/b
- checked: 2026-09-11

[Likely] The touchpoint is claimed by no admitted source, and the verification pass found
one record below the triage cut that dispatches batch jobs without describing what decided
their contents.

## Discarded candidates

- c004 — run-artefact: the column is empty because the harvest did not fill it.
"""

VERIFICATION_MD = """# Verification

## G01

- searched: `outputs/01_landscape/v0.5/screened.csv` for "held-out"; OpenAlex q041, q052
- found: nothing that evaluates a driven simulator on a held-out set
- verdict: confirmed-absent
- what would change it: a source reporting a held-out split over simulation cases

## G02

- searched: `outputs/02_tango/v0.1/triage.csv` for SLURM and batch
- found: doi:10.1/b, below the cut, dispatching batch jobs
- verdict: partially-addressed
- what would change it: a full text showing the agent decides the batch contents
"""


@pytest.fixture
def make_gaps_run(tmp_path: Path) -> Callable[[], Path]:
    def _build() -> Path:
        out = tmp_path / "v0.1"
        out.mkdir(parents=True)
        with (out / "gap_candidates.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CANDIDATE_COLS, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(CANDIDATES)
        (out / "gap_candidates.md").write_text("# Gap candidates\n", encoding="utf-8")
        (out / "gaps.md").write_text(GAPS_MD, encoding="utf-8")
        (out / "verification.md").write_text(VERIFICATION_MD, encoding="utf-8")
        (out / "RUN.md").write_text(
            "# Run record\n\n- date: 2026-09-11\n- prompt: prompts/03_gaps.md v0.1\n"
            "- prompt commit: deadbee\n- model: test\n",
            encoding="utf-8",
        )
        return out

    return _build


def results(out: Path, capsys: pytest.CaptureFixture[str]) -> dict[str, str]:
    audit_gaps.main(["--out", str(out)])
    table = capsys.readouterr().out
    return {
        line.split("|")[1].strip(): line.split("|")[2].strip()
        for line in table.splitlines()
        if line.startswith("|") and "---" not in line and "Check" not in line
    }


def rewrite(out: Path, old: str, new: str) -> None:
    path = out / "gaps.md"
    text = path.read_text(encoding="utf-8")
    assert old in text, old
    path.write_text(text.replace(old, new), encoding="utf-8")


class TestBaseline:
    def test_the_contract_is_satisfiable(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        assert audit_gaps.main(["--out", str(out)]) == 0
        assert [k for k, v in results(out, capsys).items() if v != "PASS"] == []

    def test_the_battery_is_the_length_the_tests_cover(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert len(results(make_gaps_run(), capsys)) == 19


class TestGapsRestOnCandidates:
    def test_a_gap_with_no_candidates_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- candidates: c003\n", "")
        assert results(out, capsys)["Every gap cites at least one candidate"] == "FAIL"

    def test_a_gap_citing_a_candidate_that_does_not_exist_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- candidates: c003", "- candidates: c999")
        assert results(out, capsys)["Every cited candidate exists"] == "FAIL"

    def test_a_candidate_that_is_neither_used_nor_discarded_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # The check the whole run turns on: a candidate that quietly vanishes is
        # indistinguishable from one nobody read.
        out = make_gaps_run()
        rewrite(out, "- candidates: c001; c002", "- candidates: c001")
        assert results(out, capsys)["Every candidate is used or discarded with a reason"] == "FAIL"

    def test_discarding_it_with_a_reason_passes(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- candidates: c001; c002", "- candidates: c001")
        rewrite(
            out,
            "## Discarded candidates\n",
            "## Discarded candidates\n\n- c002 — too-specific: one system's own evaluation.\n",
        )
        assert results(out, capsys)["Every candidate is used or discarded with a reason"] == "PASS"

    def test_discarding_it_without_a_reason_still_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- candidates: c001; c002", "- candidates: c001")
        rewrite(out, "## Discarded candidates\n", "## Discarded candidates\n\n- c002\n")
        assert results(out, capsys)["Every candidate is used or discarded with a reason"] == "FAIL"


class TestVerdicts:
    def test_a_verdict_outside_the_controlled_list_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- verdict: confirmed-absent", "- verdict: probably")
        key = "Every gap carries a verdict from the controlled list"
        assert results(out, capsys)[key] == "FAIL"

    def test_confirmed_absent_without_query_ids_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # An absence nobody searched for is not a finding — the rule the other two runs
        # apply to [Absent-searched], applied to the verdict that asserts absence.
        out = make_gaps_run()
        rewrite(out, "- evidence: q041; q052", "- evidence: none")
        key = "confirmed-absent verdicts cite the queries that looked"
        assert results(out, capsys)[key] == "FAIL"

    def test_partially_addressed_without_a_source_key_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "- evidence: doi:10.1/b", "- evidence: several records")
        key = "partially-addressed and refuted verdicts name the sources that address it"
        assert results(out, capsys)[key] == "FAIL"

    def test_a_gap_with_no_verification_block_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        text = (out / "verification.md").read_text(encoding="utf-8")
        (out / "verification.md").write_text(text.split("## G02")[0], encoding="utf-8")
        assert results(out, capsys)["Every gap has a verification block"] == "FAIL"

    def test_a_verdict_that_disagrees_with_its_verification_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # Writing the verdict is the parent's job; disagreeing with what came back is
        # how an assigned verdict would get in.
        out = make_gaps_run()
        path = out / "verification.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- verdict: partially-addressed", "- verdict: refuted"
            ),
            encoding="utf-8",
        )
        assert results(out, capsys)["Verdicts agree between gaps.md and verification.md"] == "FAIL"

    def test_a_verification_that_searched_nothing_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        path = out / "verification.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- searched: `outputs/02_tango/v0.1/triage.csv` for SLURM and batch\n", ""
            ),
            encoding="utf-8",
        )
        key = "Every verification block records what it searched"
        assert results(out, capsys)[key] == "FAIL"


class TestSynthesisNotReasoning:
    @pytest.mark.parametrize(
        "sentence",
        [
            "This matters because nobody can reproduce the result.",
            "This should be prioritised over the others.",
            "Future work should evaluate on held-out cases.",
            "We recommend a shared benchmark.",
            "This is the most important gap in the set.",
            "The opportunity here is a shared benchmark.",
        ],
    )
    def test_reasoning_about_a_gap_fails(
        self,
        make_gaps_run: Callable[[], Path],
        capsys: pytest.CaptureFixture[str],
        sentence: str,
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "## Discarded candidates", f"[Likely] {sentence}\n\n## Discarded candidates")
        assert results(out, capsys)["No reasoning about the gaps"] == "FAIL"

    def test_a_quoted_claim_is_exempt_from_the_framing_checks(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        # Eleven v0.5 systems describe their own work as promising in the sentence
        # `maturity_claimed` records. Banning the word inside a quotation would force a
        # paraphrase of the one thing that has to be verbatim.
        out = make_gaps_run()
        rewrite(
            out,
            "## Discarded candidates",
            '[Certain] The source asserts "a promising approach for foundation design '
            'automation" while its evaluation demonstrates M1, which is the claim gap the '
            "candidate records.\n\n## Discarded candidates",
        )
        got = results(out, capsys)
        assert got["No promotional framing"] == "PASS"
        assert got["No reasoning about the gaps"] == "PASS"

    def test_an_untagged_paragraph_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rewrite(out, "[Certain] Twenty-one", "Twenty-one")
        assert results(out, capsys)["Substantive paragraphs carry an evidence tag"] == "FAIL"


class TestCandidateFile:
    def test_a_hand_edited_candidate_file_fails_on_its_columns(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        with (out / "gap_candidates.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["candidate_id", "statement"], quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerow({"candidate_id": "c001", "statement": "something"})
        assert results(out, capsys)["gap_candidates.csv columns match SCHEMA_gaps"] == "FAIL"

    def test_a_count_without_a_denominator_fails(
        self, make_gaps_run: Callable[[], Path], capsys: pytest.CaptureFixture[str]
    ) -> None:
        out = make_gaps_run()
        rows = list(csv.DictReader((out / "gap_candidates.csv").open(encoding="utf-8")))
        rows[1]["denominator"] = ""
        with (out / "gap_candidates.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CANDIDATE_COLS, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)
        key = "Every counted candidate carries its denominator"
        assert results(out, capsys)[key] == "FAIL"


class TestVacuousPasses:
    def test_an_empty_run_fails_rather_than_passing_vacuously(self, tmp_path: Path) -> None:
        out = tmp_path / "empty"
        out.mkdir()
        assert audit_gaps.main(["--out", str(out)]) == 1
