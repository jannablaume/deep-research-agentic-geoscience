# papers.md — verbatim extracts (test mode, mechanics-slice candidates)

Three admitted sources this run. Extracts are verbatim quotations retrieved by the fetch
calls logged as `query_id` 16-20 in `queries.csv`. Nothing below is reconstructed from
recall.

## arxiv:2508.02936 — AQUAH: Automatic Quantification and Unified Agent in Hydrology

**What was built / architecture** (from https://arxiv.org/html/2508.02936, query_id 19):

> "AQUAH stitches together geospatial data retrieval, Earth-observation forcing data,
> hydrologic models (e.g., Coupled Routing and Excess Storage, crest), and automated
> visualization in a seamless workflow."

> "The architecture consists of: LLM Interface: Converts user-provided natural language
> inputs into structured simulation instructions...Tool Executor Layer: Manages and executes
> Python-based geospatial libraries..."

The system comprises eight specialized agents in sequence: Context Parser, Dataset
Retriever, Perceptor, OutletSelector, ParamInitializer, Operator, Report Writer, and
Feedback Reflector.

**How it was evaluated:**

> "To quantify the quality of the hydrological–simulation reports produced by our AQUAH, we
> conducted a two–tier evaluation."

> "The quality of each AQUAH-generated simulation is assessed through a two-tier protocol
> that combines objective statistical metrics and human expert review."

Testing occurred "across a range of U.S. basins" with real Earth-observation data (MRMS
precipitation, USGS discharge records, HydroSHEDS terrain), across ten independent
initialisations comparing LLM backbones. No non-agentic baseline is compared against.

**What was achieved:**

> "claude-4-opus achieves the highest average score (7.01), leading or tying on three of the
> four criteria."

> "AQUAH can complete cold-start simulations and produce analyst-ready documentation without
> manual intervention."

**Author-stated limitations:**

> "Further calibration and validation are still needed for operational deployment."

> "The prototype also depends on publicly hosted data and inference services (e.g., USGS,
> MRMS, and a cloud LLM), so regional access limits or temporary outages could reduce
> functionality."

**Maturity-claimed sentence** (abstract): "AQUAH autonomously retrieves the required terrain,
forcing, and gauge data; configures a hydrologic model; runs the simulation; and generates a
self-contained PDF report" from a natural-language prompt.

---

## arxiv:2604.21501 — GeoMind: An Agentic Workflow for Lithology Classification with Reasoned Tool Invocation

**What was built / architecture** (from https://arxiv.org/html/2604.21501, query_id 20):

> "GeoMind organizes its toolkit into perception, reasoning, and analysis modules, which
> respectively translate raw logs into semantic trends, infer lithology hypotheses from
> multi-source evidence, and verify predictions against stratigraphic constraints."

> "GeoMind organizes lithology interpretation as a multi-step decision process coordinated by
> a Planner-Executor-Reflector architecture."

**How it was evaluated:**

> "We benchmark our approach on four public well-log datasets covering diverse geological
> settings: SEAM, Facies, FORCE, and GeoLink."

Compared against "classical machine learning models, deep time-series classifiers, and
recent LLM-based formulations" including XGBoost, InceptionTime, MOMENT, GPT4TS, and
domain-specific methods, using weighted precision/recall/F1 on held-out test sets defined by
well identity.

**What was achieved:**

> "GeoMind consistently achieves the strongest (or near-strongest) weighted F1 scores"
> across all datasets, with improvements of approximately 5.7 F1 points on FORCE and 3.4
> points on Facies.

> "GeoMind consistently produces fewer anomalously short runs than XGBoost and GPT4TS,
> reducing fragmentation by up to 27.9%."

**Author-stated limitations:** the extracted text states only a compute-cost note: the
system was "trained and evaluated on a machine equipped with 4× NVIDIA A800 GPUs, due to the
additional memory and compute overhead." No further limitations or future-work statement was
located in the extracted content.

**Maturity-claimed sentence** (abstract): "Experiments on four benchmark well-log datasets
demonstrate that GeoMind consistently outperforms strong baselines in classification
performance while providing transparent and traceable decision-making processes."

**Code:** "The code is at https://github.com/lqzxt/GeoMind"

---

## arxiv:2508.11618 — Optimal CO2 storage management considering safety constraints in multi-stakeholder multi-site CCS projects: a Markov game perspective

**Extraction status: incomplete.** The fetch (query_id 18, PDF) returned title, authors, and
section headings but the body text could not be reliably decompressed by the fetch tool (see
RUN.md, mechanics-slice notes). No verbatim methods/results/limitations sentences could be
retrieved this run. What is verified to exist:

- Title and authors as given in `papers.csv`, confirmed from the fetched PDF's embedded
  document metadata (`/Title` field) and by direct binary inspection
  (`grep`-style extraction of the PDF's `/Title` object), not from recall.
- Section headings visible in the retrieved content: "Proposed Framework," "Mathematical
  Formulation," "Basin-Scale GCS System," "Reservoir and Model Setup," "Case Study and
  Results," "Comparison against MOO results."
- The method is self-described (from partially retrieved text) as a Constrained Markov Game
  (CMG) solved via safe multi-agent reinforcement learning (safe MARL).

No `maturity_claimed` sentence, no results, and no author-stated limitations could be quoted
verbatim this run. `papers.csv` records these fields as `not stated` rather than inferring
them, per the evidence rules. This is a tooling-extraction failure on an open-access source,
not a paywall, and is reported as a mechanics-slice finding in `RUN.md` and `coverage.md`.
