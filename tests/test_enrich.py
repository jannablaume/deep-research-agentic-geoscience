"""enrich.py's key mapping, country extraction, and offline behaviour.

The network call itself is not tested here — CI must never make one, and
`harvest.py`'s API readers are excluded for the same reason. What is tested is
everything around it: which identity keys can be resolved to a DOI at all, how
countries are read out of a work, and that the offline path still writes a
complete file so `export_web.py` has something well-formed to read.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

import enrich


class TestDoiOf:
    def test_a_doi_key_yields_its_doi(self) -> None:
        assert enrich.doi_of("doi:10.1038/s44304-026-00262-z") == "10.1038/s44304-026-00262-z"

    def test_an_arxiv_key_yields_its_registered_doi(self) -> None:
        # OpenAlex indexes arXiv works under a registered DOI, so these are
        # recoverable rather than lost.
        assert enrich.doi_of("arxiv:2604.11945") == "10.48550/arxiv.2604.11945"

    def test_a_title_key_yields_nothing(self) -> None:
        # A title slug is not resolvable, and guessing would attach a country to
        # the wrong paper.
        assert enrich.doi_of("title:some-slug") is None


class TestCountriesOf:
    def test_codes_are_collected_across_every_author(self) -> None:
        work: dict[str, object] = {
            "authorships": [
                {"institutions": [{"country_code": "ch"}]},
                {"institutions": [{"country_code": "DE"}, {"country_code": "FR"}]},
            ]
        }
        assert enrich.countries_of(work) == ["CH", "DE", "FR"]

    def test_a_country_counts_once_however_many_authors_share_it(self) -> None:
        # Three co-authors in one country are one paper from it. Weighting by
        # author would turn a large collaboration into a large country.
        work: dict[str, object] = {"authorships": [{"institutions": [{"country_code": "US"}]}] * 3}
        assert enrich.countries_of(work) == ["US"]

    @pytest.mark.parametrize(
        "work",
        [
            {},
            {"authorships": []},
            {"authorships": [{"institutions": []}]},
            {"authorships": [{"institutions": [{}]}]},
            {"authorships": [{"institutions": [{"country_code": ""}]}]},
            {"authorships": "not a list"},
            {"authorships": [{"institutions": "not a list"}]},
        ],
    )
    def test_a_work_with_no_usable_affiliation_yields_nothing(
        self, work: dict[str, object]
    ) -> None:
        # Preprint servers largely do not supply institutions, so this is the
        # common case rather than the edge case — it must not raise.
        assert enrich.countries_of(work) == []


class TestOfflineMain:
    @pytest.fixture
    def run(self, tmp_path: Path) -> Path:
        papers = tmp_path / "papers.csv"
        with papers.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle, quoting=csv.QUOTE_ALL)
            writer.writerow(["identity_key", "tier"])
            writer.writerow(["doi:10.1/a", "core"])
            writer.writerow(["arxiv:2604.11945", "context"])
        return tmp_path

    def test_it_writes_a_row_for_every_admitted_record(
        self, run: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert enrich.main(["--out", str(run), "--offline"]) == 0
        with (run / "enrichment" / "countries.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        # Every record gets a row even with nothing found, so a reader can tell
        # "no country recorded" from "not looked at".
        assert [r["identity_key"] for r in rows] == ["doi:10.1/a", "arxiv:2604.11945"]
        assert all(r["resolved"] == "no" for r in rows)
        assert all(r["countries"] == "" for r in rows)

    def test_offline_makes_no_call_and_says_so(
        self, run: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        enrich.main(["--out", str(run), "--offline"])
        err = capsys.readouterr().err
        assert "0 call(s)" in err
        # The denominator the facet is drawn over is always printed, because a
        # geography chart over an unstated subset is the failure mode.
        assert "0 of 2 report an author institution" in err

    def test_a_run_with_no_papers_refuses(self, tmp_path: Path) -> None:
        with pytest.raises(SystemExit, match="nothing to enrich"):
            enrich.main(["--out", str(tmp_path), "--offline"])
