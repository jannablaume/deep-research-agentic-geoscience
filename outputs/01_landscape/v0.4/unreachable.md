# Unreachable sources

Records identified as plausibly relevant but whose text could not be verified in this run.
Not counted as admitted sources.

## Grey-literature leads, paywalled/blocked

- **"Physics-Informed Agentic AI: An Intelligent Assistant for Production Management and
  Optimization"** — SPE Permian Basin Energy Conference (25PBEC), OnePetro record 793947.
  `https://onepetro.org/spepbec/proceedings-abstract/25PBEC/25PBEC/793947` — WebFetch
  returned `HTTP 403 Forbidden`. Only a WebSearch-engine paraphrase was available, which is
  not a verbatim quote and was not used. Not admitted.
- **"NeoSpatial: Agentic AI Driven Solution, Revolutionizing Oil and Gas Exploration
  Geospatial Workflows"** — IPTC International Petroleum Technology Conference (26IPTC),
  OnePetro record 794830.
  `https://onepetro.org/IPTCONF/proceedings-abstract/26IPTC/26IPTC/D011S009R006/794830` —
  WebFetch returned `HTTP 403 Forbidden`. Not admitted for the same reason.

## Grey-literature lead, no independently retrievable primary source

- **"GeoSim.AI"** — a RAG-based system said to guide LLM translation of natural language
  into geomechanical simulation inputs. Cited by name only inside a secondary source
  (arXiv:2503.24047, "Towards Scientific Intelligence: A Survey of LLM-based Scientific
  Agents") and in WebSearch-engine summaries; a fetch of the survey's own abstract page did
  not surface its reference list, and no independent paper, repository or landing page for
  GeoSim.AI could be located. Not admitted — per rule 1, a system cannot be written up from
  a secondary paraphrase alone.

## Core-tier deep-read failures (step 4) — downgraded to `tier: context`, `access_status: abstract-only`

Of 91 `tier: core` records from screening, full text was obtained for only 17 (19%). The
74 below were attempted with WebFetch (arXiv: `arxiv.org/html/<id>`; DOI records: the DOI
redirect target and, where given, `oa_pdf_url`) and could not be read. Per the skill's
instructions, none were guessed at: each is downgraded to `tier: context` in
`screening.csv`/`papers.csv`, characterised from its abstract only (already retrieved by
`harvest.py` earlier in this run), with `maturity_demonstrated: not stated (abstract
only)`. This is the dominant failure mode of this run's step 4 and is reported here as a
finding, not smoothed over.

**Failure-mode breakdown across all 74:**
- OnePetro (SPE/IPTC/ADIPEC/OTC) landing pages: `HTTP 403 Forbidden` — the largest single
  category, roughly 30 of the 74.
- Elsevier/ScienceDirect (via `linkinghub.elsevier.com`): either an unresolvable
  client-side "Redirecting…" interstitial, or `HTTP 403 Forbidden` on the ScienceDirect URL
  itself — roughly 12 records.
- EAGE/EarthDoc: `HTTP 403 Forbidden`, or (for some) a client-side "Redirecting…"
  placeholder — roughly 10 records.
- IEEE Xplore: landing page returned no extractable body text (JS-rendered stub) — 4
  records.
- MDPI: `HTTP 403 Forbidden` on both the PDF route and the landing page, on journals
  ("Geosciences", "Sustainability", "Applied Sciences") that are nominally fully open
  access — 3 records. A real, if narrow, finding: MDPI's open-access status did not
  translate into fetchability by this run's tooling.
- arXiv where the HTML render exceeded the fetch tool's 10 MB content limit and the
  `/abs/` fallback gave only the abstract: 1 record (`TRACE`,
  `doi:10.48550/arxiv.2603.21152`) — notable because this is the one arXiv failure in the
  whole run, and it happens to be a system (`TRACE`, seismology) independently flagged as a
  related system by another paper's reference list (see the snowball note below); it
  remains downgraded to context on the same abstract-only basis as everything else here.
- Unparseable/binary PDF content (FlateDecode streams the fetch tool could not decode to
  text): 3 records (SBGF extended abstract, ACL Anthology/EMNLP Findings paper, AJEG
  extended abstract).
- ACM Digital Library, ResearchGate, Springer (auth-gated PDF), Zenodo (data/output archive
  page rather than the manuscript itself), ACM CAIT: one each, all `HTTP 403` or
  content-free landing pages.
- One EGU abstract (`doi:10.5194/egusphere-egu26-20010`, GWFlowAI) had been withdrawn by
  its authors as of the fetch (11 Aug 2026) and carries no content at all beyond title/
  citation metadata.
- Two records (`doi:10.1016/j.autcon.2025.106257`, `doi:10.1016/j.watres.2026.125886`) plus
  three more (see below) had no abstract in `screened.csv` to fall back on either, so their
  `papers.csv` rows carry `not stated` in nearly every field beyond title-derived `task`.

**Per-record detail:**

- doi:10.2523/iptc-24776-ms — "Application of Self-Supervised Autonomous Agent Framework With Growing Scheme for Digital Transformation of Elder/Existed Well Potentials Discovery". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2523/iptc-25122-ms — "Solving Upstream Complexity: EnergyAI's Agentic RAG and A2A Framework for Faster Subsurface Insights". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/230772-ms — "Self-Improving Generative AI Agents for Automated Daily Mud Report Parsing". `HTTP 403 Forbidden` (OnePetro).
- doi:10.3997/2214-4609.202539032 — "Enhancing Geoscience Document Mining with Large Language Models through GraphRAG Integration and Agentic Architectures". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.3997/2214-4609.202639010 — "Integration Between Seismic Interpretation and Data Management through Agentic Workflows". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.3997/2214-4609.202639027 — "Open-DARTS-MCP: An MCP-Based Architecture for Agentic Reservoir Simulation Workflows". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.2523/iptc-25230-ms — "Multi-Agentic Generative AI Framework for Accelerating Field Development Planning". `HTTP 403 Forbidden` (OnePetro).
- doi:10.5194/egusphere-egu26-9051 — "TunnelSentinel: An Agentic AI Framework for Geo-Structural Resilience and Settlement Safety in Immersed Tunnels". EGU meeting-organizer abstract page only, no body text.
- doi:10.2118/229603-ms — "Enhancing Risk Analysis in Drilling Operations Using an Agentic LLM Workflow". `HTTP 403 Forbidden` (OnePetro).
- doi:10.3997/2214-4609.202637165 — "Conversational and Agentic Workflows for Constructing and Executing Fully-Differentiable Reservoir Simulation Models". `HTTP 403 Forbidden` (EarthDoc/EAGE); the record's `arxiv_id` field ("4609.20263") is not a valid arXiv id, no arXiv fallback existed.
- doi:10.2118/0426-0008-jpt — "Case Study: An Agentic AI Framework for Large-Scale Well Modeling of Offshore Field Developments". `HTTP 403 Forbidden` (OnePetro/JPT).
- title:largelanguagemodelagentsindynamicmineplanningamodulardecisionsupportframework — "Large Language Model Agents in Dynamic Mine Planning: A Modular Decision-Support Framework" (UA thesis repository). `HTTP 403 Forbidden`.
- doi:10.1109/access.2026.3714775 — "Large Language Model Agents in Dynamic Mine Planning: Challenges, Opportunities, and Future Directions". IEEE Xplore JS-rendered stub, no extractable content.
- doi:10.3390/geosciences16050176 — "LLM-Powered Multi-Agent Framework for Automated PPV Prediction in Tunnel Blasting". `HTTP 403 Forbidden` on both MDPI PDF and landing-page routes.
- doi:10.1016/j.aei.2026.105065 — "An LLM-based multi-agent framework for automated reliability analysis of spatially variable soils". Elsevier "Redirecting" stub only.
- doi:10.2118/224532-ms — "Pragmatic AI Approach for Enhanced Well Planning and Execution…". `HTTP 403 Forbidden` (OnePetro).
- doi:10.1007/s43503-026-00088-8 — "Large language model-based multi-agent systems for automated foundation design…". Springer PDF route redirected to an auth-gated login page.
- doi:10.2118/229512-ms — "Agentic Retrieval Augmented Generation for Drilling: A Real-Time Framework for Dynamic Insights and Visualization". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/233094-ms — "Applying Specialized AI Agents for Plug and Abandonment Operation Analysis and Regulatory Compliance…". `HTTP 403 Forbidden` (OnePetro).
- doi:10.5194/egusphere-egu26-15632 — "A Multimodal Multi-Agent Framework for Automated Landslide Risk Management". EGU meeting-organizer abstract page only.
- doi:10.2118/221864-ms — "A Multi Modal Geologist Copilot GeoCopilot: … Lithology Interpretation While Drilling". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/229435-ms — "A Unified Agentic and Generative AI Framework for Enhancing Drilling Intelligence Through WITSML and Unstructured Data Interaction". `HTTP 403 Forbidden` (OnePetro).
- doi:10.5281/zenodo.19078873 — "GeoSAGE: A Multi-Agent Workflow for Geological Reasoning From Joint Gravity and Magnetic Inversion Models". Zenodo record is a data/output archive describing the manuscript, not the manuscript's own full text.
- doi:10.1145/3731599.3767402 — "EQSIM Agent: A Conversational AI for Interactive Exploration of Large-scale Earthquake Simulation Data". `HTTP 403 Forbidden` (ACM DL).
- doi:10.18653/v1/2025.findings-emnlp.1386 — "STA-CoT: Structured Target-Centric Agentic Chain-of-Thought for Consistent Multi-Image Geological Reasoning". PDF route returned unparseable binary content (tried twice); ACL Anthology landing page matched the abstract verbatim only.
- doi:10.3997/2214-4609.202639016 — "Agentic AI for Seismic Data Processing: Automating Outcomes, Not Workflows". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.3997/1365-2397.fb2026015 — "From Metadata to Embeddings: Enabling Agentic AI for Subsurface Intelligence". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.2118/232332-ms — "Agentic AI-Driven Geothermal Reservoir Simulation and Optimization Using Surrogate Modelling for Rapid Site Screening". `HTTP 403 Forbidden` (OnePetro).
- doi:10.64862/ajeg.2025.2sp.95.232 — "An Agentic Machine Learning Pipeline for Drift-Aware Debris Flow Detection". PDF fetched (323.7KB) but unparseable (compressed/encoded stream); landing page abstract-only.
- doi:10.36227/techrxiv.175979241.11582889/v1 — "Explainability as a Catalyst for Agentic AI Adoption in Subsurface Oil & Gas Workflows". `HTTP 403 Forbidden` (TechRxiv, both `/full` and `/pdf` routes).
- doi:10.2118/234989-ms — "Transforming Decision-Making with Agentic AI for Dynamic Business and Analytics Dashboards in Hydrocarbon Asset Management". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2523/iptc-25245-ms — "Agentic AI Framework for Technical Excellence: A Discipline-Based, Scalable Multimodal Assistant for Subsurface". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/230751-ms — "Enhanced Real-Time Stuck Pipe Prediction Using Hybrid Physics + AI Agents and Comprehensive Sticking Mechanism Evaluation". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2139/ssrn.6515171 — "MAS-LAND: A Multi-Agent System for Landslide detection and rapid response". `HTTP 403 Forbidden` (SSRN, both URL forms).
- doi:10.1016/j.autcon.2025.106257 — "Multimodal framework integrating multiple large language model agents for intelligent geotechnical design". `HTTP 403 Forbidden` (ScienceDirect); no abstract in `screened.csv` either.
- doi:10.1016/j.watres.2026.125886 — "Autonomous inverse modeling of complex groundwater systems via a physics-integrated large language model multi-agent framework". `HTTP 403 Forbidden` (ScienceDirect); no abstract in `screened.csv` either.
- doi:10.3390/su18021014 — "ResQConnect: An AI-Powered Multi-Agentic Platform for Human-Centered and Resilient Disaster Response". `HTTP 403 Forbidden` on every MDPI URL variant tried.
- doi:10.1109/acait63902.2024.11022201 — "ChenSi Big Model: LLM Intelligent Emergency Assistance Decision System Based on LangChain Framework". `HTTP 403 Forbidden` (IEEE Xplore).
- doi:10.2118/222053-ms — "Advancing Geoscience with Multi-Modal AI: A Comprehensive Copilot". `HTTP 403 Forbidden` (OnePetro).
- doi:10.1016/j.petsci.2026.05.031 — "Large language model-based AI agent for well logging data processing and interpretation". `HTTP 403 Forbidden` (ScienceDirect).
- doi:10.2118/229506-ms — "GenAI Multi-Agent Retrieval Augmented Generation for Oil & Gas Applications". `HTTP 403 Forbidden` (OnePetro).
- doi:10.1016/j.sandf.2026.101789 — "Reconstruction of landslide events in urban setting using LLM-based Agentic AI with multimodal data". Elsevier "Redirecting" stub, then `HTTP 403 Forbidden`; no abstract in `screened.csv` either.
- doi:10.1016/j.gsf.2026.102445 — "From local data to global risk maps: A geospatial generative pre-trained transformer framework for earthquake building vulnerability estimation". Elsevier "Redirecting" stub, then `HTTP 403 Forbidden`.
- doi:10.3997/2214-4609.202620128 — "Leveraging the GEOH5 Data Structure and AI Agents in Mineral Exploration". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.1016/j.cacaie.2026.100079 — "Uncertainty-aware multi-agent system for automated and real-time geotechnical analysis in tunneling". Elsevier "Redirecting" stub, then `HTTP 403 Forbidden`.
- doi:10.1016/j.bdes.2026.100042 — "A generalizable automated geophysical agent workflow for accessible subsurface hydrology analysis". Elsevier "Redirecting" stub, then `HTTP 403 Forbidden`.
- doi:10.1190/tle44020142.1 — "Intelligent seismic workflows: The power of generative AI and language models". Crossref chooser page metadata-only; GeoscienceWorld `HTTP 403 Forbidden`.
- doi:10.3997/2214-4609.202410350 — "Building a Large Language Model based Seismic Data Processing Assistant". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.2118/226728-ms — "Offshore Production Surveillance and Intervention Using Multi Agent AI" (the underlying SPE paper behind the JPT highlights piece admitted separately as context). `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/228117-ms — "Building an Intelligent Research Assistant – RAG Isn't All You Need". `HTTP 403 Forbidden` (OnePetro).
- doi:10.48550/arxiv.2603.21152 — "TRACE: A Multi-Agent System for Autonomous Physical Reasoning for Seismology". arXiv HTML render exceeded the fetch tool's 10 MB limit (both un-versioned and `v1`); `/abs/` fallback gave abstract only.
- doi:10.22564/19cisbgf2025.463 — "Massively Parallel Distributed Computing and Agentic Framework for Subsurface Data Management and Analysis". PDF retrieved (6.2MB) but unparseable binary/FlateDecode content.
- doi:10.1016/s1876-3804(26)60734-3 — "A multi-agent collaborative framework with human-in-the-loop for well log interpretation and applications". `HTTP 403 Forbidden` (Elsevier, both routes).
- doi:10.3997/2214-4609.2025101389 — "Leveraging Agent-Based Frameworks and LLMs for Multimodal Analysis in Drilling and Geological Operations". EarthDoc "Redirecting" JS stub only.
- doi:10.2118/233425-ms — "Transforming Engineering Workflows: A Data-Driven Generative AI Solution for Multidisciplinary Design Generation and Optimization". `HTTP 403 Forbidden` (OnePetro).
- doi:10.2118/229423-ms — "Multi-Agent Geophysical AI Workflow for Automated Reservoir Characterization". EarthArXiv PDF unparseable binary; EarthArXiv landing page abstract-only.
- doi:10.2118/229646-ms — "Large Language Model Empowered Automated Reservoir Agent: A Win-Win Strategy for Reservoir Intelligent Management and Transformation". `HTTP 403 Forbidden` (OnePetro).
- doi:10.3997/2214-4609.2025101096 — "Agentic AI in Geoscience: Advancing Predictive Models for Agile Decision-Making". EarthDoc "Redirecting" JS stub only.
- doi:10.2118/229346-ms — "New Role of Technical Specialists to Enable Digital Transformation in the Petroleum Industry: A Petrophysicist-Based Proof of Concept". `HTTP 403 Forbidden` (OnePetro).
- doi:10.1016/j.autcon.2026.107055 — "AI agent for advanced geological forecasting and risk control in rock tunnel construction based on multi-source information fusion". `HTTP 403 Forbidden` (ScienceDirect, both routes); no abstract in `screened.csv` either.
- doi:10.2523/iptc-25138-ms — "Smarter Bits, Faster Insights: Accelerating Drill Bit Innovation Through AI-Driven Forensics, Automation and Agentic AI". OnePetro "Redirecting" JS stub only.
- doi:10.67704/oep.2025.250012 — "Distributed acoustic sensing system integrable with AI agents". Journal page abstract/metadata only; guessed PDF path empty.
- doi:10.13140/rg.2.2.28926.65602 — "Autonomous Production Optimization in the Volve Field: A Multi-Agent Reinforcement Learning using Agentic AI". `HTTP 403 Forbidden` (ResearchGate); no abstract in `screened.csv` either.
- doi:10.2118/229716-ms — "Innovative AI Agent for Real-Time Drill Bit Selection Optimization". `HTTP 403 Forbidden` (OnePetro).
- doi:10.3997/2214-4609.202535055 — "Estimating Fluid Properties in North Sea Using a Causal AI Agent". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.1109/icftic68075.2025.11324812 — "A Knowledge-System-Driven Evolving AI Agent Architecture and its Application in Oil & Gas Exploration and Production". IEEE Xplore, no retrievable content.
- doi:10.1109/caibda65784.2025.11182767 — "Automated Mineralization Prediction System Driven by Large Language Models". IEEE Xplore, no retrievable content.
- doi:10.3997/2214-4609.202639113 — "Geological Modeling Agent: Automated Static Model Uncertainty Assessment Using AI Agent and Geology-Aware Guidance". `HTTP 403 Forbidden` (EarthDoc/EAGE).
- doi:10.56952/igs-2025-0391 — "Geo-Resource Agent for Automated Reservoir and Mechanical Earth Model Characterization…". `HTTP 403 Forbidden` (OnePetro/ARMA).
- doi:10.2118/223828-ms — "Development of the AI Drilling Agent: AI-Physics Hybrid Model for Accurate, Adaptive and Autonomous Decision-making". `HTTP 403 Forbidden` (OnePetro).
- doi:10.3390/app16168089 — "A Dual-Teacher Distilled MoE Agent for Complex Industrial Document Analysis". `HTTP 403 Forbidden` (MDPI, nominally open access).
- doi:10.4043/36352-ms — "AI Transformation: Unleashing Value with X.brain". `HTTP 403 Forbidden` (OnePetro/OTC).
- doi:10.5194/egusphere-egu26-20010 — "GWFlowAI: A One-Step, Location-Based AI Framework for Exploring Public Groundwater Datasets in India". Abstract withdrawn by authors as of 11 Aug 2026; no content.
- doi:10.1016/j.oregeorev.2026.107477 — "LLM-assisted workflow for geological unit harmonization and tectonic-unit-constrained map generalization with copper occurrence overlay". `HTTP 403 Forbidden` (ScienceDirect, both routes) — this is the mining-subfield false negative recovered from the audit sample in step 2; still unreachable at full text in step 4, downgraded to context on its abstract.

**Snowball candidates noted during step 4** (not themselves fetched/screened as new records unless stated): **TRACE** and the **SPECFEM MCP seismology agent** were independently named as related systems in another paper's reference list, but both are already present in this corpus under their own identity_keys (`doi:10.48550/arxiv.2603.21152`, listed above as unreachable, and `doi:10.48550/arxiv.2512.14429`, admitted with full text in step 3/4) — no new record needed. **URSA** (a general-purpose LANL scientific-agent framework) was named as foundational infrastructure but is not itself a solid-earth/subsurface geoscience system — out of scope, not pursued. **Plumecast** (a GNN reservoir-simulation surrogate) was named as trained on agent-generated data but is not itself described as an LLM-agentic system — not pursued. **Zhang et al. 2025, "Streamlining geoscience data analysis with an LLM-driven workflow"** (`doi:10.1016/j.acags.2024.100218`) was a genuine miss — present in `screened.csv` (domain_group `geoscience_general`) but never screened because it fell outside the shortlist; added to `screening.csv` with `found_via: snowball`, decision `out`/`periphery` (an explicitly agentic system, but its subject — general mineralogical database querying via the Mindat API — does not map to any of the ten core subfields).
