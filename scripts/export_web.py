#!/usr/bin/env python3
"""Export one run as the single JSON document the web front end compiles in.

    python3 scripts/export_web.py --out outputs/01_landscape/v0.5

Writes `web/src/data/landscape.web.json`. The front end reads nothing else and
fetches nothing at runtime, so the built folder opens from the filesystem and a
copy of it is a copy of the data.

Two rules this file follows, both inherited from the output contract:

**Nothing is inferred.** Every field is either read from an artifact or counted
from one. Where a source is silent the value stays `not stated` and the front
end renders it as such. The one exception is the framework facet, which is a
keyword match over `tools_used` and `base_model`, and is labelled derived so the page can
say so where it shows it.

**Counted beats parsed.** Where a number can be counted from a CSV it is
counted here rather than lifted out of `RUN.md` prose. `harvested` and
`shortlisted` are the two that cannot be — `screened.csv` and `triage.csv` are
gitignored, being 22MB each — so they come from `audit.md`, which `audit.py`
generates and whose format is therefore stable. Both are nullable, and a null
renders as an em dash rather than a zero: a missing count must not look like a
measured absence of records.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

# The export is one JSON document assembled from CSV and Markdown, so every
# intermediate shape here is a nested dict of primitives. `Any` is the honest
# annotation for those: the contract that matters is the emitted document's, and
# it is checked by the front end's own types plus `scripts/audit.py`, not by a
# TypedDict that would have to be rewritten for every schema change.
Json = dict[str, Any]
Row = dict[str, str]

csv.field_size_limit(10_000_000)

# --- the schema, mirrored ----------------------------------------------------
# These lists are `reference/SCHEMA.md`'s controlled vocabularies. They are
# duplicated here for one reason: order. A facet drawn from `Counter` alone is
# ordered by whatever this run happened to find, so a technique that drops to
# zero next run disappears from the axis instead of showing a zero, and two
# runs cannot be compared side by side. Any value found in the data but absent
# from these lists is appended rather than dropped, so a schema change shows up
# as an unordered tail instead of silently vanishing.

SUBFIELDS = [
    "seismology",
    "reservoir_engineering",
    "engineering_geology",
    "mining",
    "geological_modelling",
    "inversion",
    "geothermal",
    "ccs",
    "hydrogeology",
    "geomechanics",
]

PERIPHERY = ["earth_observation", "climate_atmosphere", "ocean", "planetary", "geoscience_general"]

TECHNIQUES = [
    "tool-calling",
    "code-execution",
    "planning",
    "task-decomposition",
    "self-reflection",
    "memory",
    "retrieval",
    "multi-agent-debate",
    "role-specialisation",
    "human-in-the-loop",
    "simulator-in-the-loop",
    "physics-solver-in-the-loop",
    "instrument-control",
    "knowledge-graph",
    "fine-tuning",
    "guardrails-validation",
]

ARCHITECTURES = [
    "single-agent",
    "multi-agent-flat",
    "multi-agent-hierarchical",
    "pipeline-with-agent",
    "agent-plus-simulator",
    "agent-plus-solver",
    "agent-plus-database",
    "router",
    "not stated",
]

MATURITY = ["M0", "M1", "M2", "M3", "M4", "M5"]

# The rubric, so the page can show what a level means next to the count of it
# rather than making the reader open SCHEMA.md.
MATURITY_RUBRIC = {
    "M0": "Position or architecture paper, no working implementation",
    "M1": "Implemented; evaluated only on synthetic or textbook-scale data",
    "M2": "Evaluated on a reusable, site-agnostic benchmark - which may contain real data",
    "M3": "Evaluated on real field data from a named site, well, or campaign, retrospectively",
    "M4": "Output entered a real workflow or influenced a real decision; site or operator named; time-bounded",
    "M5": "Routine use beyond a trial, evidenced by someone other than the vendor",
}

CUT_REASONS = [
    "not-agentic",
    "not-geoscience",
    "periphery",
    "pre-llm-only",
    "duplicate",
    "not-a-source",
    "no-abstract-untriageable",
]

# --- the derived facet ------------------------------------------------------
# `tools_used` is free text by design: it records what a given agent could
# actually call, and no controlled list would survive the next paper. But the
# question "which agent frameworks does this field actually build on" is
# answerable from it, and is not answerable from any other column.
#
# So: a curated keyword match, grouped by what kind of thing the match is. It
# is a reading of free text and it is marked `derived` everywhere it surfaces.
# Acronyms match case-sensitively; a lowercase name is bounded so that `cline`
# cannot be found inside `decline`.
FRAMEWORKS = [
    # (label, kind, pattern, case-sensitive)
    ("MCP / FastMCP", "agent framework", r"\b(?:MCP|FastMCP|Model Context Protocol)\b", True),
    ("LangGraph", "agent framework", r"\bLangGraph\b", False),
    ("LangChain", "agent framework", r"\bLangChain\b", False),
    ("GraphRAG", "agent framework", r"\bGraphRAG\b", False),
    ("AutoGen", "agent framework", r"\bAutoGen\b", False),
    ("CrewAI", "agent framework", r"\bCrewAI\b", False),
    ("LlamaIndex", "agent framework", r"\bLlamaIndex\b", False),
    (
        "EvE / OpenEvolve / AlphaEvolve",
        "agent framework",
        r"\b(?:EvE|OpenEvolve|AlphaEvolve)\b",
        True,
    ),
    ("Claude Code", "harness / client", r"\bClaude Code\b", False),
    ("cline", "harness / client", r"\bcline\b", False),
    ("Codex", "harness / client", r"\bCodex\b", False),
    ("VS Code", "harness / client", r"\bVS ?Code\b", False),
    ("Streamlit", "harness / client", r"\bStreamlit\b", False),
    ("Ollama", "harness / client", r"\bOllama\b", False),
    ("GEOS", "simulator / solver", r"\bGEOS\b", True),
    ("OPM Flow", "simulator / solver", r"\bOPM Flow\b", False),
    ("ECLIPSE", "simulator / solver", r"\bECLIPSE\b", True),
    ("OpenQuake", "simulator / solver", r"\bOpenQuake\b", False),
    # SPECFEM is always named by build: SPECFEM2D, SPECFEM3D_Cartesian,
    # SPECFEM3D_Globe. `\bSPECFEM\b` matched none of them, because there is no
    # word boundary between "M" and "2".
    ("SPECFEM", "simulator / solver", r"\bSPECFEM\w*", True),
    ("Devito", "simulator / solver", r"\bDevito\b", False),
    ("Pipesim", "simulator / solver", r"\bPipesim\b", False),
    ("SGeMS", "simulator / solver", r"\bSGeMS\b", False),
    ("Gurobi", "simulator / solver", r"\bGurobi\b", False),
    ("ObsPy", "domain library", r"\bObsPy\b", False),
    ("SeisBench", "domain library", r"\bSeisBench\b", False),
    ("DASPy", "domain library", r"\bDASPy\b", False),
    ("GaMMA", "domain library", r"\bGaMMA\b", False),
    ("HypoDD", "domain library", r"\bHypoDD\b", False),
    ("PhaseNet", "domain library", r"\bPhaseNet\b", False),
    ("EQcorrscan", "domain library", r"\bEQcorrscan\b", False),
    ("SeismoStats", "domain library", r"\bSeismoStats\b", False),
    ("ETAS", "domain library", r"\bETAS\b", True),
    ("PyTorch", "domain library", r"\bPyTorch\b", False),
    ("PyVista", "domain library", r"\bPyVista\b", False),
    ("Plotly", "domain library", r"\bPlotly\b", False),
    ("scikit-learn", "domain library", r"\bscikit-learn\b", False),
    ("SymPy", "domain library", r"\bSymPy\b", False),
    ("Pydantic", "domain library", r"\bPydantic\b", False),
    ("Docling", "domain library", r"\bDocling\b", False),
    ("DuckDB", "store / index", r"\bDuckDB\b", False),
    ("ChromaDB", "store / index", r"\bChroma ?DB\b", False),
    ("LanceDB", "store / index", r"\bLanceDB\b", False),
    ("Neo4j", "store / index", r"\bNeo4j\b", False),
    ("BM25", "store / index", r"\bBM25\b", True),
    ("Parquet", "store / index", r"\bParquet\b", False),
    ("OSDU", "store / index", r"\bOSDU\b", True),
    ("SharePoint", "store / index", r"\bSharePoint\b", False),
    ("FDSN datacenters", "archive / service", r"\bFDSN\b", True),
    ("SCEDC", "archive / service", r"\bSCEDC\b", True),
    ("EIDA", "archive / service", r"\bEIDA\b", True),
    ("IRIS", "archive / service", r"\bIRIS\b", True),
    ("USGS", "archive / service", r"\bUSGS\b", True),
    ("Nominatim", "archive / service", r"\bNominatim\b", False),
    ("ESHM20 / ESRM20", "archive / service", r"\bES[HR]M20\b", True),
]

# The two kinds that answer "what is this agent built with", as against the
# libraries, solvers and archives it happens to call. The framework facet is a
# floor over papers that name one of these at all, and most do not — so the page
# publishes that denominator the way the geography panel publishes its own.
ORCHESTRATION_KINDS = ("agent framework", "harness / client")

FRAMEWORK_KINDS = [
    "agent framework",
    "harness / client",
    "simulator / solver",
    "domain library",
    "store / index",
    "archive / service",
]

# `base_model` is the field SCHEMA.md calls "the one most often silently
# omitted", and the report makes a point of six core rows beginning
# `not stated`. Grouping it by family is the only way to show that at a glance;
# the raw string stays on the paper record.
MODEL_FAMILIES = [
    ("not stated", r"^not stated"),
    ("GPT / OpenAI", r"\b(?:GPT|ChatGPT|o[134]-|OpenAI|gpt-)"),
    ("Claude", r"\bClaude\b"),
    ("Gemini", r"\bGemini\b"),
    # A lookahead, not a word boundary and not a bare prefix. The canonical
    # spellings are `Qwen3-4B` and `Qwen3-VL-8B`; a digit is a word character,
    # so `\bQwen\b` matched neither and filed both core Qwen systems under
    # `other named`. Dropping the boundary outright would match `Qwenzhou`, so
    # the rule is "not followed by a lowercase letter" — which admits a
    # version number, a separator and the bare word, and nothing else. The
    # other families are unaffected: GPT has no trailing boundary already, and
    # Llama, DeepSeek and Mistral are conventionally written with a separator.
    ("Qwen", r"\bQwen(?![a-z])"),
    ("Llama", r"\bLlama\b"),
    ("DeepSeek", r"\bDeepSeek\b"),
    ("Mistral", r"\bMistral\b"),
    ("other named", r"."),
]

# `source_type` arrives in two vocabularies: the values the run wrote and the
# values OpenAlex uses to fill the 108 blanks. Left alone they collide -
# `article` (20) and `journal-article` (18) are the same thing on two bars. One
# label per kind, and anything unrecognised passes through so a new value shows
# up rather than being folded into the wrong bucket.
SOURCE_TYPES = {
    "article": "journal article",
    "journal-article": "journal article",
    "peer-reviewed": "journal article",
    "review": "review article",
    "conference-paper": "conference paper",
    "conference-abstract": "conference abstract",
    "proceedings-article": "conference paper",
    "preprint": "preprint",
    "posted-content": "preprint",
    "software": "software deposit",
    "dataset": "dataset",
    "thesis": "thesis",
    "editorial": "editorial",
    "report": "report",
}


def source_type_of(run_value: str, openalex_value: str) -> str:
    """One label for a publication kind, from whichever source has one."""
    raw = (run_value or openalex_value or "").strip().lower()
    if not raw:
        return "not stated"
    return SOURCE_TYPES.get(raw, raw)


TAGS = ["Certain", "Likely", "Absent-searched"]

# Section files, in report order, mapped onto where the page puts them. The
# page is the report re-cut so each thematic block sits next to the counts it
# describes, rather than a prose dump beside an unrelated chart.
SECTIONS = [
    ("00_executive_summary.md", "overview"),
    ("03_applications.md", "fields"),
    ("01_techniques.md", "systems"),
    ("02_architectures.md", "systems"),
    ("04_evaluation.md", "evidence"),
    ("05_maturity.md", "evidence"),
    ("06_disagreement.md", "evidence"),
    ("07_periphery.md", "periphery"),
]


# --- reading ----------------------------------------------------------------


def log(message: str) -> None:
    """Progress to stderr.

    AGENTS.md B3: the artifact goes to a file and stdout is reserved for
    `audit.py`'s table, which is meant to be piped into `RUN.md`. An export
    summary on stdout would be pipeable into the same place and mean nothing
    there.
    """
    print(message, file=sys.stderr)


def read_csv(path: Path) -> list[Row]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def parse_run_log(text: str) -> dict[str, str]:
    """The `- key: value` block that opens RUN.md, and nothing below it.

    README.md carries this as a template, so the keys are stable. Anything
    unparseable is simply absent from the result and renders as `not stated` —
    a run record is context for the numbers, never the source of one.
    """
    log: dict[str, str] = {}
    for line in text.splitlines():
        if line.startswith("## ") and log:
            break
        m = re.match(r"^- ([a-z][a-z /-]*):\s*(.*)$", line)
        if m:
            log[m.group(1).strip()] = m.group(2).replace("`", "").strip()
    return log


def parse_audit(text: str) -> Json:
    """`audit.md`'s pipe table into rows, and the two counts only it carries.

    Generated by `scripts/audit.py`, so this is parsing a machine's output
    rather than a person's prose. Shown in full on the page: 26 executed checks
    are a better statement about the dataset than any wording could be.
    """
    checks: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("Check", "---") or set(cells[0]) <= {"-"}:
            continue
        checks.append({"check": cells[0], "result": cells[1], "detail": cells[2]})

    def find(fragment: str, pattern: str) -> int | None:
        for c in checks:
            if fragment in c["check"]:
                m = re.search(pattern, c["detail"])
                if m:
                    return int(m.group(1))
        return None

    return {
        "checks": checks,
        "passed": sum(1 for c in checks if c["result"] == "PASS"),
        "harvested": find("screened.csv parses", r"(\d+) rows"),
        "shortlisted": find("Every shortlist record was screened", r"all (\d+) shortlisted"),
    }


# --- prose ------------------------------------------------------------------

CITE = re.compile(r"\[\[([^\]]+)\]\]")
# Punctuation a citation must not be separated from by a line break.
TRAILING_PUNCT = re.compile(r"[.,;:)\]]+")

INLINE = re.compile(r"\[\[([^\]]+)\]\]|`([^`]+)`|\*\*([^*]+)\*\*")


def spans(text: str, names: dict[str, str], refs: dict[str, int]) -> list[Json]:
    """Inline markdown into a span list, with citations resolved to papers.

    The report uses exactly three inline forms — `[[key]]`, backticked code and
    `**bold**` — and no links or tables, so this is a complete parser for it
    rather than a subset of one. A citation whose key is not in `papers.csv`
    stays a span with `resolved: false`; `audit.py` already fails a run where
    that happens, so it is a visible defect rather than a silently dropped
    reference.

    `names` maps every admitted `identity_key` to its `system_id` and `refs`
    maps it to its reference number. `refs` doubles as the resolution check — a
    key in it is a key `papers.csv` carries.
    """
    out: list[Json] = []
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            out.append({"t": "text", "v": text[pos : m.start()]})
        key, code, strong = m.groups()
        if key is not None:
            # Punctuation that follows a citation is carried on the citation
            # span, not left as the head of the next text run. Rendered as a
            # chip, a citation is an inline box, and a line that breaks between
            # the box and the full stop after it leaves the stop stranded at the
            # start of the next line — which reads as a typo in a document whose
            # whole argument is that its citations are exact.
            tail = TRAILING_PUNCT.match(text, m.end())
            out.append(
                {
                    "t": "cite",
                    "key": key,
                    "label": cite_label(key, refs),
                    "name": cite_name(key, names),
                    "resolved": key in refs,
                    "tail": tail.group(0) if tail else "",
                }
            )
            if tail:
                pos = tail.end()
                continue
        elif code is not None:
            out.append({"t": "code", "v": code})
        else:
            out.append({"t": "strong", "v": strong})
        pos = m.end()
    if pos < len(text):
        out.append({"t": "text", "v": text[pos:]})
    return out


def cite_label(key: str, refs: dict[str, int] | None = None) -> str:
    """A citation's visible text: its reference number.

    Three forms were tried here. The full DOI is longer than the clause holding
    it. Its suffix is unreadable — `s44304-026-00262-z` identifies nothing to a
    human. And `system_id`, which looked right, duplicates the prose: the report
    writes "TRACE on Ridgecrest and Santorini-Kolumbo [[doi:…]]", so a chip
    reading `TRACE` restates the word before it, and section 03 came out as
    "GAGAW GAGAW ... HERMES HERMES".

    So: a reference number, the convention this kind of document already uses.
    It is the shortest form that identifies anything, it never repeats the
    sentence, and the name is one hover away and one click from the full record.

    An unresolved key keeps its short textual form rather than getting a number
    it has no right to — it is not in the reference list, and `audit.py` fails a
    run that has one, so it must look wrong.
    """
    if refs and key in refs:
        return str(refs[key])
    if key.startswith("arxiv:"):
        return "arXiv:" + key.split(":", 1)[1]
    if key.startswith("doi:"):
        tail = key.split(":", 1)[1]
        m = re.match(r"10\.48550/arxiv\.(.+)$", tail)
        if m:
            return "arXiv:" + m.group(1)
        return tail.split("/", 1)[-1] if "/" in tail else tail
    return key


def cite_name(key: str, names: dict[str, str] | None = None) -> str:
    """The name behind a reference number, for its tooltip.

    `system_id` where the row has one; `not stated` rows fall back to the key,
    because a tooltip reading "not stated" tells the reader nothing about which
    paper they are about to open.
    """
    name = (names or {}).get(key, "").strip()
    return name if name and not name.startswith("not stated") else key


def parse_report(directory: Path, names: dict[str, str], refs: dict[str, int]) -> list[Json]:
    """Report markdown into blocks the page renders, tag by tag.

    Paragraphs carry `[Certain]` / `[Likely]` / `[Absent-searched]` as their
    first token. Lifting the tag out of the text and onto the block is what
    lets the page filter on it: the tag is the claim's evidential status, and
    reading only the certain claims is a thing a reviewer actually wants to do.
    """
    sections: list[Json] = []
    for filename, group in SECTIONS:
        raw = read_text(directory / filename)
        if not raw:
            continue
        blocks: list[Json] = []
        title = filename
        for chunk in re.split(r"\n\s*\n", raw):
            chunk = chunk.strip()
            if not chunk:
                continue
            if chunk.startswith("# "):
                title = chunk[2:].strip()
                continue
            if chunk.startswith("### "):
                blocks.append({"kind": "heading", "level": 3, "text": chunk[4:].strip()})
                continue
            if chunk.startswith("## "):
                blocks.append({"kind": "heading", "level": 2, "text": chunk[3:].strip()})
                continue
            if chunk.startswith("- "):
                items: list[list[Json]] = []
                for item in re.split(r"\n(?=- )", chunk):
                    body = re.sub(r"\s+", " ", item.lstrip("- ")).strip()
                    if body:
                        items.append(spans(body, names, refs))
                blocks.append({"kind": "list", "items": items})
                continue
            body = re.sub(r"\s+", " ", chunk).strip()
            tag = None
            m = re.match(r"^\[(Certain|Likely|Absent-searched)\]\s*", body)
            if m:
                tag, body = m.group(1), body[m.end() :]
            blocks.append(
                {
                    "kind": "para",
                    "tag": tag,
                    "spans": spans(body, names, refs),
                    "cites": CITE.findall(body),
                }
            )
        sections.append(
            {
                "id": filename.replace(".md", ""),
                "number": filename.split("_")[0],
                "title": re.sub(r"^\d+\s+", "", title),
                "group": group,
                "blocks": blocks,
            }
        )
    return sections


def parse_extracts(text: str) -> dict[str, Json]:
    """`papers.md` into the verbatim evidence behind each core paper.

    SCHEMA.md fixes this file's shape: one `## <identity_key>` block per core
    paper, a URL line, then quoted sentences. The prefixed bullets
    (`maturity_claimed:`, `limitation:`, `NOT FOUND:`) are pulled out because
    they answer specific questions the paper card asks; the rest stay as an
    ordered list of quotes.

    This is the file that makes the front end defensible. Every characterisation
    on a paper card can be checked against the sentence it came from, in the
    authors' words, without leaving the page.
    """
    extracts: dict[str, Json] = {}
    for block in re.split(r"\n(?=## )", text):
        m = re.match(r"## (\S+)\s*\n(.*)", block, re.S)
        if not m:
            continue
        key, body = m.group(1).strip(), m.group(2)
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        entry: Json = {
            "source": "",
            "source_note": "",
            "quotes": [],
            "not_found": [],
            "maturity_claimed": "",
            "limitation": "",
        }
        for line in lines:
            if line.startswith("http"):
                parts = re.split(r"\s+[-—]\s+", line, maxsplit=1)
                entry["source"] = parts[0]
                entry["source_note"] = parts[1] if len(parts) > 1 else ""
            elif line.startswith("- "):
                item = line[2:].strip()
                for field, prefix in (
                    ("maturity_claimed", "maturity_claimed:"),
                    ("limitation", "limitation:"),
                ):
                    if item.startswith(prefix):
                        entry[field] = item[len(prefix) :].strip().strip('"')
                        break
                else:
                    if item.startswith("NOT FOUND:"):
                        entry["not_found"].append(item[len("NOT FOUND:") :].strip())
                    else:
                        entry["quotes"].append(item.strip('"'))
        extracts[key] = entry
    return extracts


# An annotated-list entry opens `[<name>: ]<title> (<year>[, <venue>]).` and,
# on the context tier, continues into a one-line summary. Everything before the
# summary is already on the paper record — title, year, venue, system name — so
# only what follows the year is kept. A core entry ends at the year, and its
# summary is therefore empty, which is correct: its prose lives in the extract
# block, not here.
ANNOTATION_HEAD = re.compile(r"^.*?\((?:19|20)\d{2}(?:,[^)]*)?\)\.\s*")


def parse_annotations(text: str) -> dict[str, str]:
    """The one-line summaries from `08_papers.md`.

    The annotated list is the one place a context-tier source gets a sentence
    of prose; `papers.csv` gives it a `task` clause and nothing else. An entry
    is claimed by the citation key on its first line, so an entry whose key
    cannot be read is skipped rather than guessed at — a missing summary costs
    a sentence, a wrong one costs the point of the file.

    Bold markers are stripped rather than converted. The value is rendered as
    text on the paper record, and a literal `**TRACE.**` there is worse than no
    emphasis at all.
    """
    notes: dict[str, str] = {}
    for entry in re.split(r"\n(?=- )", text):
        if not entry.startswith("- "):
            continue
        head = entry.splitlines()[0]
        found = CITE.findall(head)
        if not found:
            continue
        body = re.sub(r"\s+", " ", CITE.sub("", head[2:])).strip()
        body = re.sub(r"^\[context\]\s*", "", body).strip()
        body = body.replace("**", "")
        body = ANNOTATION_HEAD.sub("", body).strip()
        notes[found[-1]] = body
    return notes


def summary(annotation: str, task: str) -> str:
    """The annotated-list summary, unless it is the `task` cell again.

    Both are one clause saying what a system is for, written from the same
    abstract, so on many context rows they come out word for word identical —
    and the paper record then shows the same sentence twice, once as the task
    and once under it. Where they agree, the summary is dropped: `task` is the
    schema column, so it is the one that stays.
    """

    def normalise(s: str) -> str:
        return re.sub(r"[\s.]+", " ", s).strip().lower()

    return "" if normalise(annotation) == normalise(task) else annotation


# --- counting ---------------------------------------------------------------


def facet(
    counts: Counter[str], order: list[str], total: int, keep_zeros: bool = True
) -> list[Json]:
    """A distribution, in a fixed order, with anything unexpected appended.

    `share` is against the population the facet was counted over rather than
    the sum of the bars: techniques are multi-valued, so the shares of a
    technique facet do not add to 1 and must not be presented as if they do.

    `keep_zeros` decides whether a controlled value nobody used still gets a
    row. It defaults on, because for the facets drawn from a rubric a zero is
    the finding: `M5: 0` says nothing in this corpus is in routine use, and
    `instrument-control: 0` is the report's one `[Absent-searched]` claim on
    the technique list. It is turned off for facets whose vocabulary is a
    guess at what might appear — model families, mostly — where an unused row
    is an artefact of this file rather than a measurement.
    """
    labels = list(order) + sorted(k for k in counts if k not in order)
    return [
        {
            "label": k,
            "n": counts.get(k, 0),
            "share": round(counts.get(k, 0) / total, 4) if total else 0.0,
        }
        for k in labels
        if counts.get(k, 0) or (keep_zeros and k in order)
    ]


def multi(rows: list[Row], column: str) -> Counter[str]:
    c: Counter[str] = Counter()
    for r in rows:
        for value in r[column].split(";"):
            value = value.strip()
            if value:
                c[value] += 1
    return c


def model_families(value: str) -> list[str]:
    """Every model family a `base_model` cell names, not just the first.

    This was single-valued and returned the first match from an ordered list,
    which put GPT first and therefore counted every multi-backbone paper as a
    GPT paper: 11 of 23 core rows were attributed to GPT, and 7 of those 11
    also name Claude, Gemini, Qwen or DeepSeek. Several are papers whose whole
    method is an ablation across backbones, so the chart read as market share
    when it measured "GPT appears somewhere in the cell, and GPT sorts first".

    Multi-valued, the facet answers the question actually being asked - how
    many of these systems were built on each family - and its bars deliberately
    sum to more than the number of systems. `not stated` is exclusive: a silent
    cell names nothing, so it never appears beside a family.
    """
    if re.match(r"^\s*not stated", value, re.I):
        return ["not stated"]
    found = [
        label
        for label, pattern in MODEL_FAMILIES
        if label not in ("not stated", "other named") and re.search(pattern, value, re.I)
    ]
    return found or (["other named"] if value.strip() else ["not stated"])


def frameworks_of(*columns: str) -> list[str]:
    """Match the keyword list over every column that can name a framework.

    `tools_used` is the obvious one. `base_model` is the other, and leaving it
    out cost the whole harness category: specfem-mcp records "tested via the
    cline VS Code agent" there, Agents4GEOS names Claude Code there, and
    ESHM20-MCP lists Codex among its clients — so the sub-facet that answers
    "what do these agents actually run inside" read as empty when it was only
    looking in the wrong cell.
    """
    text = " ".join(columns)
    return [
        label
        for label, _kind, pattern, cased in FRAMEWORKS
        if re.search(pattern, text, 0 if cased else re.I)
    ]


def read_enrichment(
    run: Path,
) -> tuple[dict[str, list[str]], dict[str, str], dict[str, str]]:
    """Author-institution countries and journal names, if `enrich.py` has run.

    Optional by design. The geography facet is the only thing on the page that
    needs a network call to produce, so a run without it stays complete and the
    page omits the panel rather than showing an empty one.
    """
    countries: dict[str, list[str]] = {}
    journals: dict[str, str] = {}
    types: dict[str, str] = {}
    for row in read_csv(run / "enrichment" / "countries.csv"):
        key = row.get("identity_key", "")
        if not key:
            continue
        countries[key] = [c.strip() for c in row.get("countries", "").split(";") if c.strip()]
        journals[key] = row.get("openalex_journal", "").strip()
        types[key] = row.get("openalex_type", "").strip()
    return countries, journals, types


def parse_unreachable(text: str) -> dict[str, int]:
    """Row counts from the two tables in `unreachable.md` that have tables.

    The file accounts for every source whose full text could not be read, but
    it accounts for most of them in prose: the first demotion pass is a
    six-row table, the two abstract-less records are a two-row table, and the
    second pass ("EAGE EarthDoc three times, IEEE CAIT, ACM EQSIM Agent…") is a
    paragraph. So this returns the two figures that are counted and nothing
    else.

    That matters for the summary table. The question "how many were lost to a
    paywall" has no computed answer in this run — `papers.csv` has no paywall
    column, and `access_status: abstract-only` covers paywalls, bot-protected
    nominal open access, software deposits and records with no abstract in any
    API alike. The page therefore reports `abstract-only` as what it is, shows
    these two counted subsets beneath it, and says the rest is narrated rather
    than tallied. A number is counted or it is not stated.
    """
    counts: dict[str, int] = {}
    sections = {
        "no_abstract": "Admitted with no abstract retrievable",
        "full_text_refused": "Screened core, demoted to context for want of full text",
    }
    for name, heading in sections.items():
        start = text.find(f"## {heading}")
        if start < 0:
            continue
        rest = text[start + len(heading) :]
        end = rest.find("\n## ")
        body = rest[: end if end > 0 else len(rest)]
        rows = 0
        for line in body.splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not cells or set("".join(cells)) <= set("-: "):
                continue  # the separator row
            if cells[0].lower() in ("identity_key", "doi"):
                continue  # the header row
            rows += 1
        counts[name] = rows
    return counts


def parse_shortlist(text: str) -> tuple[Counter[str], dict[str, str]]:
    """Shortlist size per query group, and the group each record came in under.

    Read from `shortlist.md` rather than `triage.csv`, which is gitignored at
    22MB, and rather than `RUN.md`, whose per-group figures are **stale**: they
    record the 606-record shortlist from before the mid-run triage refix, not
    the 712 the run finished with. `shortlist.md` is the tracked artifact of the
    final cut, so it is the only place a per-group denominator can be counted
    from a fresh clone.

    Note what the group is and is not. It is the query family that *found* a
    record, assigned by `triage.py` from title and abstract. It is not the
    `subfield` on the paper's row, which screening assigns by where the
    system's evaluation is set. The two share their names and mostly agree, and
    where they disagree the page has to say so rather than presenting a rate
    over two different populations as though it were one.
    """
    groups: dict[str, str] = {}
    counts: Counter[str] = Counter()
    key = ""
    for line in text.splitlines():
        heading = re.match(r"^### (\S+)\s*$", line)
        if heading:
            key = heading.group(1)
            continue
        tag = re.search(r"·\s*(core|periphery)/(\w+)\s*·", line)
        if tag and key:
            scope, group = tag.group(1), tag.group(2)
            if scope == "core":
                counts[group] += 1
                groups[key] = group
            key = ""
    return counts, groups


def build(out: Path) -> Json:
    papers_rows = read_csv(out / "papers.csv")
    if not papers_rows:
        sys.exit(f"no papers.csv under {out} — nothing to export")
    screening = read_csv(out / "screening.csv")
    queries = read_csv(out / "queries.csv")
    audit = parse_audit(read_text(out / "audit.md"))
    run_log = parse_run_log(read_text(out / "RUN.md"))
    extracts = parse_extracts(read_text(out / "papers.md"))
    annotations = parse_annotations(read_text(out / "report" / "08_papers.md"))
    countries_by_key, openalex_journals, openalex_types = read_enrichment(out)
    unreachable = parse_unreachable(read_text(out / "unreachable.md"))
    shortlisted_by_group, group_of = parse_shortlist(read_text(out / "shortlist.md"))

    # Every admitted key mapped to the name the report calls that system by.
    # Doubles as the citation-resolution check.
    names = {r["identity_key"]: r["system_id"] for r in papers_rows}
    # Reference numbers, in papers.csv row order — which SCHEMA.md fixes as
    # subfield then tier, so the numbering is stable across a re-export and a
    # reader working down the paper list sees them in order.
    refs = {r["identity_key"]: i for i, r in enumerate(papers_rows, start=1)}
    # `_rows` is the CSV as read; `papers` below is the same set with the
    # derived fields attached. `multi()` reads the raw `;`-joined cell, so both
    # shapes are needed and the suffix keeps them from being mistaken for each
    # other in a facet call.
    core_rows = [r for r in papers_rows if r["tier"] == "core"]

    papers: list[Json] = []
    for r in papers_rows:
        key = r["identity_key"]
        techniques = [t.strip() for t in r["agentic_techniques"].split(";") if t.strip()]
        papers.append(
            {
                "key": key,
                # The number the report's prose cites this source by, so a
                # marker in a paragraph and a row in the list name each other.
                "ref": refs[key],
                "tier": r["tier"],
                "system_id": r["system_id"],
                "title": r["title"],
                "authors": r["authors"],
                "year": int(r["year"]) if r["year"].isdigit() else None,
                "venue": r["venue"],
                "url": r["url"],
                # Blank on 108 of 155 rows, so OpenAlex fills the gaps rather
                # than the column staying two-thirds empty - normalised, because
                # the two sources do not share a vocabulary.
                "source_type": source_type_of(r["source_type"], openalex_types.get(key, "")),
                "subfield": r["subfield"],
                "subfield_secondary": r["subfield_secondary"],
                "task": r["task"],
                "techniques": techniques,
                "architecture": r["architecture"],
                "base_model": r["base_model"],
                "model_families": model_families(r["base_model"]),
                "countries": countries_by_key.get(key, []),
                # The run's own `venue`, corrected against the full text where one
                # was read, and OpenAlex's source name only where the run left it
                # blank. 101 of 155 rows carry a venue; the fallback lifts that to
                # 140 without ever overwriting a checked value.
                "journal": r["venue"].strip() or openalex_journals.get(key, ""),
                "tools_used": r["tools_used"],
                "frameworks": frameworks_of(r["tools_used"], r["base_model"]),
                "evaluation_method": r["evaluation_method"],
                "baseline": r["baseline"],
                "held_out": r["held_out"],
                "data_type": r["data_type"],
                "reported_result": r["reported_result"],
                "maturity_claimed": r["maturity_claimed"],
                "maturity_demonstrated": r["maturity_demonstrated"],
                "limitations": r["author_stated_limitations"],
                "code_availability": r["code_availability"],
                "access_status": r["access_status"],
                "found_via": r["found_via"],
                "annotation": summary(annotations.get(key, ""), r["task"]),
                "extract": extracts.get(key),
            }
        )

    n = len(papers)
    core = [p for p in papers if p["tier"] == "core"]
    context = [p for p in papers if p["tier"] == "context"]

    # Fields carry the run's central caveat as data rather than as a footnote:
    # a field's bar is its admitted literature, and the core half is the part
    # anybody could actually read an evaluation section in.
    fields: list[Json] = []
    for name in SUBFIELDS + sorted({p["subfield"] for p in papers} - set(SUBFIELDS)):
        rows = [p for p in papers if p["subfield"] == name]
        if not rows:
            continue
        rows_core = [p for p in rows if p["tier"] == "core"]
        fields.append(
            {
                "label": name,
                "n": len(rows),
                "core": len(rows_core),
                "context": len(rows) - len(rows_core),
                "share": round(len(rows) / n, 4),
                # The shortlist that the query family of the same name produced,
                # and what share of it survived screening. This is the number
                # that explains the field distribution: reservoir engineering
                # does not dominate because its query returned more, it
                # dominates because almost everything its query returned was
                # admitted. See `parse_shortlist` on why the two counts are not
                # the same taxonomy.
                "shortlisted": shortlisted_by_group.get(name, 0),
                "admitted_share": (
                    round(len(rows) / shortlisted_by_group[name], 4)
                    if shortlisted_by_group.get(name)
                    else None
                ),
                # How many admitted rows came in under that same query group, so
                # the reader can size the taxonomy mismatch rather than trust it.
                "from_own_query": sum(1 for p in rows if group_of.get(p["key"]) == name),
                "maturity": facet(
                    Counter(p["maturity_demonstrated"] for p in rows_core), MATURITY, len(rows_core)
                ),
                "systems": sorted({p["system_id"] for p in rows_core}),
            }
        )

    matched: Counter[str] = Counter(f for p in papers for f in p["frameworks"])

    orchestration = {label for label, kind, _p, _c in FRAMEWORKS if kind in ORCHESTRATION_KINDS}
    frameworks_coverage = {
        "core_total": len(core),
        "core_named": sum(1 for p in core if set(p["frameworks"]) & orchestration),
        "total": n,
        "named": sum(1 for p in papers if set(p["frameworks"]) & orchestration),
        # A tool of any kind, not just an orchestration framework. On the context
        # tier `tools_used` comes from an abstract, which is why it is so much
        # thinner.
        "core_any_tool": sum(1 for p in core if p["frameworks"]),
        "context_any_tool": sum(1 for p in context if p["frameworks"]),
        "context_total": len(context),
    }

    framework_kinds: list[Json] = []
    for kind in FRAMEWORK_KINDS:
        labels = [label for label, k, _p, _c in FRAMEWORKS if k == kind]
        counts = Counter(f for f in matched.elements() if f in labels)
        items = [
            {
                "label": label,
                "n": counts[label],
                "share": round(counts[label] / n, 4),
                "core": sum(1 for p in core if label in p["frameworks"]),
            }
            for label in labels
            if counts[label]
        ]
        if items:
            framework_kinds.append(
                {
                    "kind": kind,
                    "items": sorted(items, key=lambda i: (-i["n"], i["label"])),
                }
            )

    periphery_screened = Counter(
        r["subfield"] for r in screening if r["cut_reason"] == "periphery" and r["subfield"]
    )
    periphery_available: Counter[str] = Counter()
    for q in queries:
        if q["scope"] == "periphery" and q["n_available"].isdigit():
            periphery_available[q["domain_group"]] += int(q["n_available"])

    sample = [r for r in screening if r["from_audit_sample"] == "yes"]

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "run": {
            "path": str(out),
            "version": out.name,
            "date": run_log.get("date", ""),
            "prompt": run_log.get("prompt", ""),
            "model": run_log.get("model", ""),
            "purpose": run_log.get("purpose", ""),
            "harvested": audit["harvested"],
            "shortlisted": audit["shortlisted"],
            "screened": len(screening),
            "admitted": n,
            "core": len(core),
            "context": len(context),
            "audit_sample": len(sample),
            # Counted, not read: a below-cut record that screening admitted is
            # by definition a false negative, so the rate the run turns on is
            # recomputed here from screening.csv rather than quoted.
            "false_negatives": sum(1 for r in sample if r["decision"] == "in"),
            "api_calls": len(queries),
            "api_errors": sum(1 for q in queries if q["status"] != "ok"),
            "queries_core": sum(1 for q in queries if q["scope"] == "core"),
            "queries_periphery": sum(1 for q in queries if q["scope"] == "periphery"),
        },
        # The executive-summary table: the funnel, one counted row at a time,
        # each with the exact thing it counts. `note` is the honest caveat where
        # the obvious question ("how many to a paywall?") outruns the data.
        "funnel": [
            {
                "label": "Records harvested",
                "n": audit["harvested"],
                "of": None,
                "what": "unique records from OpenAlex and arXiv across "
                f"{len(queries)} API and web calls",
            },
            {
                "label": "Shortlisted by triage",
                "n": audit["shortlisted"],
                "of": audit["harvested"],
                "what": "passed a deterministic score on agent vocabulary and domain fit",
            },
            {
                "label": "Screened with a reason",
                "n": len(screening),
                "of": audit["harvested"],
                "what": "an in-or-out decision per record, each with a stated cause",
                "note": (
                    f"More than the shortlist, because {len(sample)} records were also "
                    "screened from below the triage cut to measure what the cut "
                    f"discarded. That sample found {sum(1 for r in sample if r['decision'] == 'in')} "
                    "false negatives, which is what makes the cut a measurement rather "
                    "than an assumption."
                ),
            },
            {
                "label": "Excluded as not agentic",
                "n": sum(1 for r in screening if r["cut_reason"] == "not-agentic"),
                "of": len(screening),
                "what": "an LLM is used, but nothing plans, calls a tool, or acts on a result",
            },
            {
                "label": "Admitted as agentic and in scope",
                "n": n,
                "of": len(screening),
                "what": "the system decides something for itself, in one of the ten core subfields",
                "emphasis": True,
            },
            {
                "label": "Full text read",
                "n": len(core),
                "of": n,
                "what": "the only rows that can be characterised or rated",
            },
            {
                "label": "Full text not obtained",
                "n": len(context),
                "of": n,
                "what": "abstract only: paywalled, delivery refused, a software "
                "deposit, or no manuscript",
                "note": (
                    f"{unreachable.get('full_text_refused', 0)} of these are tabulated in "
                    "unreachable.md as every route to the text refused, and "
                    f"{unreachable.get('no_abstract', 0)} had no abstract in any API. The "
                    "remaining causes are narrated there rather than tallied, and "
                    "papers.csv has no paywall column - so this run cannot put a number "
                    "on paywalls alone."
                ),
            },
        ],
        "audit": audit,
        "rubric": MATURITY_RUBRIC,
        "tags": TAGS,
        "fields": fields,
        "techniques": facet(multi(papers_rows, "agentic_techniques"), TECHNIQUES, n),
        "techniques_core": facet(multi(core_rows, "agentic_techniques"), TECHNIQUES, len(core)),
        "frameworks": framework_kinds,
        "frameworks_coverage": frameworks_coverage,
        # Every term the match looks for, including the ones that matched
        # nothing. A derived facet is only checkable if the reader can see what
        # was searched for as well as what was found: a term with zero hits is
        # either a tool this corpus does not use or a pattern that does not
        # work, and the page cannot tell you which — but it can show you the
        # term and let you judge.
        "framework_terms": [
            {"label": label, "kind": kind, "matched": bool(matched[label])}
            for label, kind, _pattern, _cased in FRAMEWORKS
        ],
        "architectures": facet(Counter(p["architecture"] for p in papers), ARCHITECTURES, n),
        "architectures_core": facet(
            Counter(p["architecture"] for p in core), ARCHITECTURES, len(core)
        ),
        "maturity": facet(Counter(p["maturity_demonstrated"] for p in core), MATURITY, len(core)),
        # Multi-valued: a paper contributes to every family it names, so these
        # bars sum to more than the population and the panel says so.
        "models": facet(
            Counter(f for p in papers for f in p["model_families"]),
            [m for m, _ in MODEL_FAMILIES],
            n,
            keep_zeros=False,
        ),
        "models_core": facet(
            Counter(f for p in core for f in p["model_families"]),
            [m for m, _ in MODEL_FAMILIES],
            len(core),
            keep_zeros=False,
        ),
        # How many systems name more than one backbone. This is the number that
        # explains the shape of the facet above, so it travels with it.
        "models_multi": sum(1 for p in core if len(p["model_families"]) > 1),
        "types": facet(
            Counter(p["source_type"] for p in papers),
            [],
            n,
            keep_zeros=False,
        ),
        "journals": facet(
            Counter(p["journal"] for p in papers if p["journal"]),
            [],
            n,
            keep_zeros=False,
        ),
        "countries": facet(
            Counter(c for p in papers for c in p["countries"]),
            [],
            sum(1 for p in papers if p["countries"]),
            keep_zeros=False,
        ),
        # The denominator every country bar is drawn over. OpenAlex records
        # institutions from publisher metadata and preprint servers largely do
        # not supply them, so this is well short of 155 and the panel must not
        # imply otherwise.
        "countries_coverage": {
            "with_country": sum(1 for p in papers if p["countries"]),
            "total": n,
            "multi_country": sum(1 for p in papers if len(p["countries"]) > 1),
            "distinct": len({c for p in papers for c in p["countries"]}),
        },
        "data_types": facet(
            Counter(p["data_type"] for p in core),
            ["benchmark", "synthetic", "real-field", "not stated"],
            len(core),
            keep_zeros=False,
        ),
        "held_out": facet(
            Counter(p["held_out"] for p in core),
            ["yes", "no", "not stated"],
            len(core),
            keep_zeros=False,
        ),
        "years": facet(Counter(str(p["year"]) for p in papers if p["year"]), [], n),
        "cuts": facet(
            Counter(r["cut_reason"] for r in screening if r["cut_reason"]),
            CUT_REASONS,
            len(screening),
            keep_zeros=False,
        ),
        "periphery": [
            {
                "label": name,
                "screened": periphery_screened.get(name, 0),
                "available": periphery_available.get(name, 0),
            }
            for name in PERIPHERY
            if periphery_screened.get(name) or periphery_available.get(name)
        ],
        "queries": [
            {
                "id": q["query_id"],
                "api": q["api"],
                "band": q["band"],
                "scope": q["scope"],
                "group": q["domain_group"],
                "query": q["query"],
                "status": q["status"],
                "available": int(q["n_available"]) if q["n_available"].isdigit() else None,
                "results": int(q["n_results"]) if q["n_results"].isdigit() else None,
                "new": int(q["n_new_unique"]) if q["n_new_unique"].isdigit() else None,
            }
            for q in queries
        ],
        "report": parse_report(out / "report", names, refs),
        "papers": papers,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--out", required=True, help="run directory, e.g. outputs/01_landscape/v0.5")
    ap.add_argument(
        "--to", default="web/src/data/landscape.web.json", help="where to write the export"
    )
    args = ap.parse_args(argv)

    data = build(Path(args.out))
    to = Path(args.to)
    to.parent.mkdir(parents=True, exist_ok=True)
    with to.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")

    run = data["run"]
    size = to.stat().st_size / 1024
    unresolved = sum(
        1
        for s in data["report"]
        for b in s["blocks"]
        if b["kind"] == "para"
        for sp in b["spans"]
        if sp["t"] == "cite" and not sp["resolved"]
    )
    log(f"{to}  {size:.0f} KB")
    log(
        f"  run {run['version']}: {run['admitted']} admitted "
        f"({run['core']} core, {run['context']} context) in {len(data['fields'])} fields"
    )
    log(
        f"  {len(data['report'])} report sections, "
        f"{sum(len(s['blocks']) for s in data['report'])} blocks, "
        f"{unresolved} unresolved citations"
    )
    log(
        f"  {sum(len(k['items']) for k in data['frameworks'])} frameworks derived "
        f"across {len(data['frameworks'])} kinds"
    )
    # Reported rather than left to be inferred from an empty field. On v0.5 this
    # is 0 of 155: every context annotation in `08_papers.md` restates the row's
    # own `task` cell, so the annotated list adds no sentence the paper record
    # did not already carry. That is a fact about the report, and a run where it
    # changes should be visible here rather than only in the JSON.
    kept = sum(1 for p in data["papers"] if p["annotation"])
    log(f"  {kept} of {len(data['papers'])} annotated-list summaries differ from `task`")
    if unresolved:
        log("  WARNING: unresolved citations render as broken links; run scripts/audit.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
