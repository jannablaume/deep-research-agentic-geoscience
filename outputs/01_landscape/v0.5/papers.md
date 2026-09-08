# Core-tier extracts

## doi:10.48550/arxiv.2609.01777

https://arxiv.org/html/2609.01777 — full text, arXiv HTML

- "We present TREMORS (Text Referenced Event Mapping and Output Renderer for Seismographs), an agentic framework that uses large language model reasoning within a constrained execution graph to automate seismic data retrieval."
- "The ObsPy API provides integration across multiple datacenters, e.g., EARTHSCOPE, ORFEUS, GEOFON, SCEDC, NCEDC, etc., for routine automation."
- "The event-based and continuous waveform examples demonstrate the model’s data acquisition across multiple datacenters highlighting its flexibility and practicability."
- NOT FOUND: a sentence stating a headline numerical result; the paper reports no quantitative performance figure of any kind.
- maturity_claimed: "TREMORS represents an advancement in observational seismology for data acquisition and provides a blueprint for reproducible multi-step data procurement and analyses across multiple repositories."
- limitation: "The semantic parsing stage may fail for ambiguous, imprecise, or unusually phrased prompts."

## doi:10.48550/arxiv.2603.21152

https://arxiv.org/html/2603.21152 — full text, arXiv HTML

- "Here we present TRACE (Trans-perspective Reasoning and Automated Comprehensive Evaluator), a multi-agent system that combines large language model planning with formal seismological constraints to derive auditable, physically grounded mechanistic inference from raw observations."
- "The library incorporates widely used seismological software packages such as ObsPy Beyreuther et al. (2010) , SeisBench Woollam et al. (2022) , DASPy Hu and Li (2024) , GaMMA Zhu et al. (2022) , and HypoDD Waldhauser (2000) , as well as earthquake catalog statistical analysis toolkits including EQcorrscan Chamberlain et al. (2018) , SeismoStats Mirwald et al. (2025) , and ETAS."
- "Two complex research tasks are included at this level, designed as representative real-world case studies (corresponding to the Ridgecrest inter-event and Santorini–Kolumbo volcanic crisis cases presented in Results), with evaluation focusing on the coherence of scientific reasoning, integration across tasks, and validity of the generated interpretations."
- "This workflow yielded over 90,000 precisely relocated earthquakes (Fig. 2 )."
- maturity_claimed: "By providing a generalizable infrastructure for deriving physical insights from seismic phenomena, TRACE advances the field from expert-dependent analysis toward knowledge-guided autonomous discovery in Earth sciences."
- limitation: "Despite these advancements, the efficacy of TRACE remains intrinsically bounded by the fidelity of underlying physical models and the computational cost of high-fidelity simulations."

## doi:10.48550/arxiv.2608.18272

https://arxiv.org/html/2608.18272 — full text, arXiv HTML

- "We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces it."
- "SeisEvo uses the Evolutionary Ensemble of Agents (EvE) ( Yu and Yang, 2026b ) , a decentralized evolutionary framework that organizes multiple coding agents to iteratively propose and refine candidate programs."
- "After the search ends, the discovered algorithm is tested on seismic data outside this set to assess its generalization."
- "For interpolation of field data without added synthetic noise, Evo-POCS improves the SNR over classic POCS by 3.49 dB on average across missing ratios from 30% to 70%, with the gain decreasing from 5.42 dB at 30% missing to 1.58 dB at 70% missing."
- maturity_claimed: "To the best of our knowledge, this is the first reported application of LLM-driven constrained program evolution to the discovery of standalone seismic reconstruction operators."
- limitation: "The present evidence, however, is restricted to seismic data reconstruction; extension to these tasks remains a hypothesis to be tested rather than a demonstrated capability."

## doi:10.48550/arxiv.2607.24984

https://arxiv.org/html/2607.24984 — full text, arXiv HTML

- "We present the first systematic application of graph-based retrieval-augmented generation (GraphRAG) directly to raw, tabular catalog records across three independently featured catalogs: a reservoir-adjacent swarm (Qiaojia-Dongchuan), the 2019 Ridgecrest tectonic sequence, and the 2021 Maduo Mw 7.4 aftershock sequence."
- "It begins with LLM-based entity and relationship extraction (using gpt-4o-mini ) to identify key seismic features—such as specific earthquakes, fault structures, and their spatiotemporal links."
- "We employed an LLM assistant to score the 1,200 GraphRAG and 300 baseline responses (from 0 to 3) against two ground truths."
- "Rigorous evaluation — 1,200 answers individually verified against catalog-derived ground truth and a rule-based reference graph — exposes failure modes, and four seismology-informed prompt fixes eliminate all targeted fabrications while sharply improving mechanism reasoning (up to 2.90/3)."
- maturity_claimed: "This is, to our knowledge, the first systematic demonstration of GraphRAG’s schema-free construction capability transferring across independent earthquake catalogs at essentially zero ontology-engineering cost, although downstream answer quality does not transfer uniformly (post-fix catalog-only averages of 1.69, 1.67, and 0.80/3)."
- limitation: "Because all our results rely on a single model ( gpt-4o-mini ), the rate of hallucinations and the effectiveness of our fixes might vary if a different model is used."

## doi:10.48550/arxiv.2608.13889

https://arxiv.org/html/2608.13889 — full text, arXiv HTML

- "We present an agentic NAS system in which a panel of three large language models (Claude, GPT-5.1, and Gemini 2.5 Pro) debates each candidate architecture to unanimous consensus, authors the complete PyTorch implementation, cross-reviews it, and submits it to an automated validate-train-score loop with a hard 450K parameter budget, keep-or-revert lineage, and a memory of failed mechanisms."
- "Validated candidates are trained from scratch and scored (Sec. III-D ); a mutation is kept only if its mean F1 over three independent trials beats the parent’s, otherwise it is reverted and its core mechanism enters a hard ban list the panel may not reintroduce."
- "Final comparisons train every architecture on all 100 training sections for 60 epochs under the identical loss and optimizer, and evaluate on the full test volume."
- "Under a training protocol identical for every row (full training volume, 60 epochs, same loss and optimizer, GroupNorm batch-1 adaptation for all baselines), the discovered network is simultaneously the smallest and the most accurate model: F1 0.578 and IoU 0.406 at 0.43M parameters."
- maturity_claimed: "For specialized dense-prediction tasks, reasoned code-level architecture search is now cheaper than scaling, and multi-model debate is an effective quality gate for scarce training compute."
- limitation: "This is because quantitative metrics are often insufficient to fully reflect model performance for fault segmentation given what is often times an incomplete and uncertain nature of ground-truth labels."

## doi:10.48550/arxiv.2512.14429

https://arxiv.org/html/2512.14429 — full text, arXiv HTML

- "We introduce the first Model Context Protocol (MCP) server suite for SPECFEM (supporting 2D, 3D Cartesian, and 3D Globe versions), which decomposes the entire simulation process into discrete, agent-executable tools spanning from parameter generation and mesh partitioning to solver execution and visualization."
- "For instance, a request to “simulate an earthquake” may trigger a sequence of tool calls: first to generate the necessary input files (e.g., interfaces.dat , Par_file , STATIONS …), followed by tools that run the mesher and then the solver."
- "We demonstrate the capabilities of our system through five case studies, each highlighting a different aspect of the LLM-driven workflow."
- NOT FOUND: a sentence giving a headline number; the strongest result statement is "Validated through multiple case studies, the workflow operates seamlessly in both autonomous and interactive modes, yielding high-fidelity results consistent with standard baselines.", which contains no number.
- maturity_claimed: "As the first application of MCP technology to computational seismology, this study significantly lowers the entry barrier, enhances reproducibility, and offers a promising avenue for advancing computational geophysics toward AI-assisted and automated scientific research."
- NOT FOUND: a sentence acknowledging a limitation of the present system; the paper has no limitations section and the Outlook states only what future work will add.

## arxiv:2601.18381

https://arxiv.org/html/2601.18381 — full text, arXiv HTML

- "To facilitate the transformation of legacy finite difference implementations into the Devito environment, this study develops an integrated AI agent framework."
- "Primary queries, following the comprehensive strategy, access information from the Neo4j graph database using four parallel retrieval mechanisms."
- "Table III presents the evaluation results for 13 Devito finite difference test cases covering varying difficulty levels and application domains."
- "The assessment indicates strong system performance, with a Grade-A success rate of 76.9%."
- maturity_claimed: "The principal contribution lies in the incorporation of feedback mechanisms motivated by reinforcement learning, enabling a transition from static code translation toward dynamic and adaptive analytical behavior."
- limitation: "Although the system is capable of collecting and storing comprehensive conversion history data, its capabilities for advanced data mining and pattern discovery remain limited."

## arxiv:2605.15028

https://arxiv.org/html/2605.15028 — full text, arXiv HTML

- "We propose PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization."
- "The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend."
- "We evaluate PetroGraph on three reservoir models of increasing complexity: the synthetic SPE1 model, the faulted SPE9 benchmark, and the real-field Norne model."
- "Using weighted normalized root mean square error as the objective, PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne."
- maturity_claimed: "These results demonstrate that multi-agent orchestration can automate key decisions in history matching, lower the expertise barrier for operating complex simulation workflows, and provide a flexible foundation for extensible, domain-aware reservoir model adaptation."
- limitation: "Here, the improvement in the metric diminishes as the model size and complexity increase."

## arxiv:2604.21501

https://arxiv.org/html/2604.21501 — full text, arXiv HTML

- "In this work, we propose GeoMind, a tool-augmented agentic framework that models lithology classification as a sequential reasoning process."
- "GeoMind organizes its toolkit into perception, reasoning, and analysis modules, which respectively translate raw logs into semantic trends, infer lithology hypotheses from multi-source evidence, and verify predictions against stratigraphic constraints."
- "Table 3 presents the overall performance comparison across four lithology benchmarks."
- "As shown in Figure 6, GeoMind consistently produces fewer anomalously short runs than XGBoost and GPT4TS, reducing fragmentation by up to 27.9% relative to XGBoost."
- maturity_claimed: "GeoMind's ability to combine fine-grained intermediate supervision with final predictions highlights its potential as a reliable tool for geoscience data analysis."
- limitation: "Although this is slower than neural-only baselines, not all tool calls involve generative inference; retrieval, voting, conflict detection, and transition validation are lightweight operations."

## doi:10.48550/arxiv.2605.00060

https://arxiv.org/html/2605.00060 — full text, arXiv HTML

- "We present TADI (Tool-Augmented Drilling Intelligence), an agentic AI system that transforms drilling operational data into evidence-based analytical intelligence."
- "Twelve domain-specialized tools, orchestrated by a large language model via iterative function calling, support multi-step evidence gathering that cross-references structured drilling measurements with daily report narratives."
- "Well 15/9-F-11 T2 is a sidetrack with 53 DDR reports spanning 2013-03-24 to 2013-05-15, rich WITSML data, and multiple hole sections, making it ideal for demonstrating multi-source evidence integration."
- "The system parses all 1,759 DDR XML files with zero errors, handles three incompatible well naming conventions, and is backed by 95 automated tests plus a 130-question stress-question taxonomy spanning six operational categories."
- maturity_claimed: "To our knowledge, TADI is the first system to integrate the operational Volve modalities used in this study—DDR XML, selected WITSML real-time objects, production records, formation tops, and perforations—into a unified, LLM-queryable analytical framework."
- limitation: "The exploration wells (15/9-19 series, 1980s–1990s) and the F-11 main bore (17 DDRs) produce lower-quality answers due to insufficient data for reliable phase detection and statistical analysis."

## arxiv:2607.18557

https://arxiv.org/html/2607.18557 — full text, arXiv HTML

- "To address this challenge, we present Agents4GEOS, an AI-agent framework built on the Model Context Protocol (MCP) that provides 52 domain-aware tools for natural-language-driven workflows with GEOS, an open-source multi-physics simulator."
- "The 52 MCP tools comprise 51 domain tools organized into six groups, plus a server health check, each group backed by a dedicated scientific library so that every quantity returned to the user results from an actual computation rather than from text generation."
- "Agents4GEOS was used to generate 200 PUNQ-S3 simulations with sampled variations of the permeability spatial field of the PUNQ-S3 benchmark as represented at Figure 8 (top)."
- "Everything that follows, from mining the papers to the figure that closes the loop (Figure 7), happened in a single conversational session, and took approximately one hour and consumed 343K tokens, in which the user wrote no XML and no shell commands."
- maturity_claimed: "Agents4GEOS demonstrates that a multi-agent system organized around a strict separation of concerns — where agents plan, tools compute, and knowledge modules encode domain expertise — can substantially lower the barrier to managing GEOS input files."
- limitation: "While Agents4GEOS can already launch jobs on computing clusters, more robust skill coverage is needed to ensure all simulations complete correctly."

## doi:10.48550/arxiv.2603.01022

https://arxiv.org/html/2603.01022 — full text, arXiv HTML

- "This paper introduces GeoMCP, a framework for analytical geotechnical calculations designed for AI-assisted engineering."
- "It exposes primitive tools for interacting with the method catalog (list methods, retrieve method cards, evaluate with numeric or unit-tagged inputs), skill discovery tools that enable clients to browse, search, and retrieve analysis skills, and composite tools for common multi-step analyses."
- "We validate GeoMCP against the official JRC Eurocode 7 worked examples [16], published by the European Commission as the authoritative implementation guide for EN 1997-1."
- "The JRC Eurocode 7 validation demonstrates that GeoMCP's evaluation engine reproduces an authoritative reference to high precision: bearing capacity factors within 0.15%, design actions exact to the reported precision, and design resistances within 0.012%."
- maturity_claimed: "Ultimately, GeoMCP provides a blueprint for transitioning the industry from isolated legacy software to an interoperable, AI-ready ecosystem where engineers can leverage modern AI without surrendering professional responsibility."
- limitation: "While GeoMCP could force an LLM to be deterministic with respect to use of analytical methods, it does not eliminate the potential for reasoning or data extraction errors."

## doi:10.48550/arxiv.2606.18661

https://arxiv.org/html/2606.18661 — full text, arXiv HTML

- "To address the aforementioned challenges, this paper proposes an instruction-driven agentic framework for landslide disaster response, transitioning from multimodal perception to the generation of specialized analytical reports."
- "The tool library encapsulates specialized landslide analysis capabilities into independent, callable nodes, such as image analysis, landslide candidate region segmentation, boundary refinement, type discrimination, terrain and geological querying, surrounding element retrieval, and comprehensive assessment."
- "To evaluate the operational capability of the proposed LandslideAgent, a representative landslide event in British Columbia, Canada, was selected for a case study."
- "Specifically, in the binary landslide scene classification task, LandslideVLM's accuracy on the LandslideBench test set increases from 85.84% to 96.80%."
- maturity_claimed: "LandslideAgent further enables autonomous multi-source spatial data inference, realizing full-process intelligence for landslide identification and analysis."
- limitation: "On the other hand, the marginal improvements observed in inferring landslide kinematic characteristics underscore that relying on single-frame static snapshots fundamentally restricts the agent's capacity to reconstruct complex hazard dynamics."

## doi:10.48550/arxiv.2606.10286

https://arxiv.org/html/2606.10286 — full text, arXiv HTML

- "This work introduces a simulator-driven Large Language Model (LLM) scheduling framework in which the LLM acts as an autonomous decision-making agent, guided at each step by a custom simulator that encodes geotechnical precedence, extraction-processing coupling, and dynamic capacity constraints directly into the action generation mechanism."
- "At each step, the simulator provides the LLM with the updated system state and the current feasible action list, with each candidate action characterized by its operational type, block identifier, admissible quantity, and marginal economic value."
- "Fig. 6 compares all scheduling strategies across a 27-block mine instance over 10 time periods, with MILP serving as the optimal reference."
- "Evaluated across mining instances of varying scale and time periods, the LLM-based framework recovers between 94% and 99% of the MILP optimal NPV while scaling linearly in computation time."
- maturity_claimed: "These results position simulator-constrained LLM agents as a practical and scalable alternative to classical optimization for long-horizon industrial scheduling under complex operational constraints."
- limitation: "Future work will extend evaluation to larger real-world block models, incorporate geological grade uncertainty and commodity price variability into the simulator state, and investigate structured prompting strategies to further close the remaining optimality gap."

## doi:10.48550/arxiv.2608.14055

https://arxiv.org/pdf/2608.14055 — full text, arXiv PDF. The `/html/` route returns HTTP 404
for this submission because the arXiv source is PDF-only, so the text was extracted from the
37-page PDF. PDF extraction inserts spurious intra-word spaces ("extra ction",
"pal aeontology") and non-breaking hyphens; those artefacts are normalised in the quotes
below, which are otherwise word-for-word.

- "We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents."
- "Each sub-agent—Parser, Entity Recognizer, Annotator, Validator, and Tracer—is optimized for a distinct phase of the extraction process."
- "Entity- and attribute-level metrics were calculated by comparing the archived pre-review output with the final expert-adjudicated reference dataset."
- "Extraction performance remained stable across fossil groups (average F1 scores of approximately 0.90 for entities and 0.91 for attributes), improving per-volume efficiency approximately sixfold relative to the tested fully manual baseline."
- maturity_claimed: "These results establish HERMES as a reusable framework for transforming scientific literature into structured, computable and evidence-traceable data resources."
- limitation: "The two-stage entity-attribute extraction strategy adopted in HERMES enhances system controllability and auditability but also introduces potential error propagation."

## doi:10.48550/arxiv.2511.03852

https://arxiv.org/html/2511.03852 — full text, arXiv HTML (v2, 09 Jun 2026)

- "We present Geothermal Analytics and Intelligent Agent, or GAIA, an AI-based system for automation and assistance in geothermal field development."
- "GAIA DT includes a set of tools for seismic waveform analysis, which can be used for tasks such as phase picking, event location estimation, magnitude estimation, and seismicity forecasting."
- "We asked GAIA, equipped with either Gemma 3 or Gemma 4, to answer the benchmark questions and compared its performance with a baseline models (Gemma 3 and Gemma 4 without RAG capabilities)."
- "In particular, we obtained up to 1.5x improvement in response accuracy, up to 1.3x improvement in response relevancy, up to 3.1x in response faithfulness, and up to 1.4x improvement in answer correctness compared to the baseline models."
- maturity_claimed: "To the best of our knowledge, GAIA is the pioneering effort in building an agentic AI system for geothermal project assistance."
- limitation: "Though we acknowledge that this problem under-represents real world scenario, it possesses similar non-uniqueness nature of most actual cases."

## doi:10.1007/s43503-026-00088-8

https://link.springer.com/content/pdf/10.1007/s43503-026-00088-8.pdf — full text, Springer OA PDF (pypdf extraction)

- "This preliminary study introduces and evaluates a router-based multi-agent framework for automated foundation design calculations through intelligent task classification and expert selection."
- "Search tools ( T {search}) : serpAPI integration for real-time information retrieval."
- "Initial evaluation on 27 test cases with triple-trial execution shows promising performance: the router-based system achieved 95.00% for shallow foundations and 90.63% for pile design, representing improvements of 8.75 and 3.13 percentage points over standalone Grok 3, respectively, and outperforming conventional workflows by 10.0–43.75 percentage points."
- "the router-based system achieved 95.00% for shallow foundations and 90.63% for pile design"
- maturity_claimed: "While these preliminary results suggest router-based multi-agent systems as a promising approach for foundation design automation, the limited sample size necessitates comprehensive validation on larger, more diverse datasets before deployment recommendations."
- limitation: "With 27 test cases, statistical power for detecting small effect sizes is inherently limited."

## doi:10.18653/v1/2025.findings-emnlp.1386

https://aclanthology.org/2025.findings-emnlp.1386.pdf — full text, ACL Anthology PDF (pypdf extraction)

- "We propose STA-CoT, a Structured Target-centric Agentic Chain-of-Thought framework that orchestrates planning, execution, and verification agents to decompose, ground, and iteratively refine reasoning steps over geological and hyperspectral image sets."
- "STA-CoT consists of three core roles: the planner, executor, and verifier, where the planner is instantiated with the Gemini-2.0"
- "We evaluate STA-CoT on the MineBench dataset (Yu et al., 2024), which is a recently proposed geological reasoning task focused on multi-image mineral deposit identification."
- "Evaluated on the MineBench benchmark, STA-CoT outperforms prior methods in both accuracy and consistency, particularly excelling in visual-grounded execution and stepwise error correction."
- maturity_claimed: "Our results establish STA-CoT as a reliable and robust solution for consistent multi-image geological reasoning, advancing automated scientific discovery in mineral exploration."
- limitation: "One limitation of our current framework is the increased computational overhead introduced by multi-step execution and iterative refinement, which may result in higher inference latency and resource usage."

## doi:10.1038/s44304-026-00262-z

https://arxiv.org/pdf/2607.16249 — full text, authors' OA arXiv PDF of the npj Natural Hazards article (Nature HTML was an AAP shell)

- "We present, to our knowledge, the first agentic interface to the end-to-end probabilistic seismic hazard and risk chain via an open-source server, addressable through the Model Context Protocol (MCP)."
- "MCP wraps the OpenQuake engine and the 2020 European Seismic Hazard and Risk Models using twenty-four typed endpoints."
- "Benchmarked against ESHM20 at seventy-three cities, replicated 475-year spectral accelerations match the published values within a median of 5%, and within 28% at 97% of cities."
- "Results are benchmarked against ESHM20 at seventy-three cities; the replicated 475-year spectral accelerations match official values within a median of 5 %, and a full hazard-to-loss estimate runs in minutes."
- maturity_claimed: "The result is both a working tool for the European earthquake engineering community and a reusable template for agentic interfaces to validated scientific computing."
- limitation: "The default branch subsets evaluate the dominant axes of the ESHM20 logic tree, but not every authorized branch."

## doi:10.1038/s41598-026-61824-9

https://www.nature.com/articles/s41598-026-61824-9_reference.pdf — full text, Nature accepted-manuscript PDF

- "We evaluate a borehole-report processing pipeline that converts Word documents into structured borehole entities, parses relative location descriptions, resolves survey-control references, and generates start/end coordinates for downstream inspection."
- "The parsing stage asks each LLM to populate a predefined JSON schema for borehole entities and to parse location descriptions into reference-point fields."
- "Eight representative LLMs were tested on 30 manually annotated reports from a real engineering project under a shared prompt-and-parser protocol, with three repetitions per model-document pair and document-level aggregation."
- "The results show that high entity and location recall does not guarantee executable coordinate generation: GPT-3.5-Turbo achieved near-perfect recall but CSR= 0.188, while the best-performing model reached CSR = 0.994."
- maturity_claimed: "The pipeline can extract entities, parse locations, and generate executable coordinates for downstream inspection; geometric accuracy validation against surveyed coordinates remains a necessary next step."
- limitation: "Limitations include the single-project dataset, confidentiality constraints, lack of released real documents, lack of manually verified coordinate ground truth, and provider-dependent runtime measurements."

## doi:10.3390/geosciences16050176

https://mdpi-res.com/d_attachment/geosciences/geosciences-16-00176/article_deploy/geosciences-16-00176.pdf — full text, MDPI PDF

- "This study proposes an AI agent-based Evaluator-Optimizer workflow that automates the model-development pipeline from prepared dataset input through model training, performance evaluation, hyperparameter optimization, and ensemble construction, with limited manual intervention after dataset definition."
- "The framework employs a multi-agent architecture comprising three collaborative agents—an Orchestrator, an Evaluator, and an Optimizer—supported by a large language model (LLM) reasoning layer."
- "The proposed AI agent-based Evaluator-Optimizer workflow was executed on the blasting dataset comprising 102 samples with six input parameters and PPV as the target variable."
- "Among the initial nine models, Gradient Boosting (GB) emerged as the best-performing model with an R 2 of 0.9356, an RMSE of 0.7608 mm/s, and an MAE of 0.5981 mm/s."
- maturity_claimed: "Applied to a 102-event tunnel-blasting field dataset, the proposed LLM-assisted Evaluator–Optimizer workflow enabled fully automated model comparison, targeted tuning, ensemble construction, and reporting under a deterministic and inspectable search protocol."
- limitation: "The small dataset (n = 102) is the dominant limitation of the study."

## doi:10.3390/mining6020026

https://mdpi-res.com/d_attachment/mining/mining-06-00026/article_deploy/mining-06-00026.pdf — full text, MDPI PDF

- "Addressing these challenges, this paper describes the Mine Intelligence and Decision Support (MINDS) framework."
- "The Optimization Engine implements pit limit calculation using the Lerchs–Grossmann (LG) algorithm [35]."
- "A proof-of-concept using the Marvin copper benchmark evaluates the framework, demonstrating automated request-to-report orchestration, execution stability with an average debate latency of 10.69 s and a transparent decision audit trail."
- "Twenty controlled trials achieved 100% execution reliability with sub-11 s debate latency, demonstrating that orchestration remains stable despite stochastic LLM generation."
- maturity_claimed: "These findings show that MINDS can systematize economic scenario analysis without sacrificing the governance and verification required for definitive feasibility studies."
- limitation: "Demonstration relied on the synthetic Marvin benchmark and curated news feeds."

## doi:10.1016/j.aei.2026.105058

https://arxiv.org/html/2604.11945 — full text, arXiv HTML (Elsevier landing page was unread; preprint recovered after the stalled OA batch)

- "For this reason, we present AutoSurrogate, a large-language-model-driven multi-agent framework that enables practitioners without ML expertise to build high-quality surrogates for subsurface flow problems through natural-language instructions."
- "Specifically, each agent operates in an iterative reason–act cycle (Yao et al., 2023). Given the current workflow state, the LLM first generates a natural-language reasoning trace that explains its assessment of the situation and its intended next step. It then issues a structured call to one of its permitted tools, observes the tool’s output, and updates its internal reasoning accordingly."
- "We evaluated the framework on a 3D geological carbon storage case, where the surrogate models learn to map permeability fields to pressure and CO2 saturation fields over 31 timesteps."
- "For CO2 saturation prediction, both AutoSurrogate configurations achieve R2 = 0.9532, outperforming the best baseline (RecurrentRUNet3D at 0.9359) by 1.73 percentage points."
- maturity_claimed: "Overall, the results indicate that autonomous, language-driven surrogate construction is a viable approach for realistic subsurface flow applications."
- limitation: "The residual errors of AutoSurrogate are primarily concentrated near the plume boundaries, where the saturation field changes rapidly. The discrepancies may also be attributed to limitations in the available training data."
