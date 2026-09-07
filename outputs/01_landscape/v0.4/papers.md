# papers.md — evidence trail for tier: core sources

One `## <identity_key>` block per core paper with full text retrieved. Verbatim quoted
sentences only; see `unreachable.md` for core-tier records that could not be fetched
(downgraded to `context` tier in `screening.csv`/`papers.csv` accordingly).

## arxiv:2605.15028

https://arxiv.org/html/2605.15028 — fetched via arxiv.org/html full text.

"PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization."

"The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend."

"We evaluate PetroGraph on three reservoir models of increasing complexity: the synthetic SPE1 model, the faulted SPE9 benchmark, and the real-field Norne model. Using weighted normalized root mean square error as the objective..."

"PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne."

"This design enables users to initiate and steer history matching through natural language while preserving explicit control over selected parameters and optimization settings."

"Future work should focus on enhancing the RAG system to cover more nuanced simulator behaviour, implementing long-term memory for iterative multi-stage history matching, and refining the agent graph architecture to accommodate alternative workflows and multi-cycle campaigns."

## arxiv:2601.18381

https://arxiv.org/html/2601.18381 — fetched via arxiv.org/html full text.

"an integrated AI agent framework" combining "Retrieval-Augmented Generation (RAG) and open-source Large Language Models...through multi-stage iterative workflows in the system's hybrid LangGraph architecture."

"Neo4j migration and index building" for knowledge graph storage, together with "Fortran static analysis and query generation" and "Code formatting functionality provided by Ruff...incorporated into the Agent layer."

"G-Eval evaluation methodology with conventional static analysis techniques", using eleven benchmark queries across three complexity tiers and 13 Devito finite-difference test cases.

"Precision@5 value of 0.964 and...Recall@5 value of 0.930" for retrieval, and a "Grade-A success rate of 76.9%" across the 13 code-translation test cases, with a "5.75×" throughput improvement using four concurrent agents.

[not stated in fetched text]

"the system's capabilities for advanced data mining and pattern discovery remain limited"; "the existing quality evaluation framework relies on fixed, predefined thresholds, such as excellent_threshold=0.85 and acceptable_threshold=0.55...the system's adaptability across diverse conversion scenarios is constrained by this static configuration."

## doi:10.48550/arxiv.2609.01777

https://arxiv.org/html/2609.01777 — fetched via arxiv.org/html full text.

"TREMORS (Text Referenced Event Mapping and Output Renderer for Seismographs), an agentic framework that uses large language model reasoning within a constrained execution graph to automate seismic data retrieval."

"For data access the TREMORS agent requires a backend and interfaces with FDSN webservices through the ObsPy API...The ObsPy API provides integration across multiple datacenters, e.g., EARTHSCOPE, ORFEUS, GEOFON, SCEDC, NCEDC, etc."

"Example workflows demonstrate support for both event-based and continuous waveform acquisition" — illustrated via prompts such as "Find all magnitude > 6.0 earthquakes that occurred in 2021 in California," with no formal benchmark or quantitative metrics reported.

[not stated in fetched text]

"While agents are not yet capable of replacing high-level subject matter experts or independently producing scientific discovery, TREMORS represents an important first step in assisting scientists with routine data retrieval tasks."

"TREMORS depends on external FDSN services and ObsPy-compatible interfaces, making it sensitive to heterogeneous metadata standards, incomplete station information, service outages, and variability across datacenters."

## doi:10.1038/s44304-026-00262-z

https://arxiv.org/html/2607.16249 — fetched via arxiv.org/html full text.

"We present the first agentic interface to the end-to-end probabilistic seismic hazard and risk chain via an open-source server, addressable through the Model Context Protocol (MCP)."

"MCP wraps the OpenQuake engine and the 2020 European Seismic Hazard and Risk Models using twenty-four typed endpoints."

"Benchmarked against ESHM20 at seventy-three cities; the replicated 475-year spectral accelerations match official values within a median of 5 %."

"The replicated spectra agree with the official values within a median absolute ln-residual of 0.05 at the 475-year return period (about 5 %; mean 0.07)."

"A full hazard-to-loss estimate runs in minutes."

"Hazard is evaluated deterministically on the highest-weighted source and ground-motion branches, rather than by Monte-Carlo sampling of the full logic tree."

## arxiv:2604.21501

https://arxiv.org/html/2604.21501 — fetched via arxiv.org/html full text.

"GeoMind, a tool-augmented agentic framework that models lithology classification as a sequential reasoning process" organized with "perception, reasoning, and analysis modules."

The system can invoke: "Case Retriever," "Trend Pattern Extractor," "Neighbor Vote Aggregator," "Neural Probability Interpreter," "Semantic Reasoning Engine," "Consensus Conflict Scanner," and "Stratigraphic Sequence Validator."

"Experiments on four benchmark well-log datasets demonstrate that GeoMind consistently outperforms strong baselines in classification performance while providing transparent and traceable decision-making processes."

"GeoMind consistently produces fewer anomalously short runs than XGBoost and GPT4TS, reducing fragmentation by up to 27.9% relative to XGBoost."

"GeoMind consistently achieves superior performance compared to state-of-the-art methods"

"trained and evaluated on a machine equipped with 4× NVIDIA A800 GPUs, due to the additional memory and compute overhead introduced by multi-stage tool invocation."

## doi:10.48550/arxiv.2605.00060

https://arxiv.org/html/2605.00060 — fetched via arxiv.org/html full text.

"TADI (Tool-Augmented Drilling Intelligence), an agentic AI system that transforms drilling operational data into evidence-based analytical intelligence."

"Twelve domain-specialized tools, orchestrated by a large language model via iterative function calling, support multi-step evidence gathering that cross-references structured drilling measurements with daily report narratives."

"Backed by 95 automated tests plus a 130-question stress-question taxonomy spanning six operational categories" and "Three detailed case studies (multi-phase drilling analysis, operational issue diagnosis, cross-well benchmarking)."

"The system parses all 1,759 DDR XML files with zero errors, handles three incompatible well naming conventions, and integrates data into a dual-store architecture: DuckDB for structured queries over 12 tables with 65,447 rows, and ChromaDB for semantic search over 36,709 embedded documents."

"The complete 6,084-line, framework-free implementation is reproducible given the public Volve download and an API key."

"Sparse-data wells...produce lower-quality answers due to insufficient data for reliable phase detection." "Future work includes: quantitative evaluation of all 130 stress test questions with human expert scoring to validate the EGS metric against subjective quality judgments."

## doi:10.22564/19cisbgf2025.335

https://sbgf.org.br/mysbgf/eventos/expanded_abstracts/19th_CISBGf/7W9BKMP7YG.pdf — fetched via WebFetch redirect to publisher PDF, full text read (via Read tool PDF parsing).

"In this context, we present the Brazilian Intelligence for Seismic Analysis (BRISA), a system designed to facilitate the initial inspection of SEG-Y files by enabling interaction without requiring programming skills or dedicated software."

"It starts by reading and extracting information from the data using the Segyio (Equinor, 2025) and Segy-SAK (Hallam, 2025) libraries." "If the user requests a graphic, the assistant delegates the task to a chart specialist agent, which uses specific tools to generate the chart and compose an appropriate response."

[not stated in fetched text — the paper reports a single demonstration example (Figure 2, Jequitinhonha dataset, CDPs 1710–1712) rather than a described evaluation methodology]

[not stated in fetched text — no quantitative headline result is reported]

"This study demonstrates the feasibility and practicality of using an LLM-powered agent system with specialized tools to interact with seismic data through natural language."

"Future enhancements include support for additional data formats and deployment in real-world operational environments."

## doi:10.48550/arxiv.2511.03852

https://arxiv.org/html/2511.03852 — fetched via arxiv.org/html full text.

"We present Geothermal Analytics and Intelligent Agent, or GAIA, an AI-based system for automation and assistance in geothermal field development."

"GAIA DT encapsulates classical and surrogate physics models, which, combined with built-in domain-specific subroutines and visualization tools, enable predictive modeling of geothermal systems."

"we curate a benchmark test set comprising various geothermal-related scenarios and rigorously evaluate the system's performance."

"GAIA outperforms the baseline models in all metrics, demonstrating its superior ability to retrieve relevant information from its knowledge base and generate accurate responses. In particular, we obtained up to 1.5x improvement in response accuracy, up to 1.3x improvement in response relevancy, up to 3.1x in response faithfulness, and up to 1.4x improvement in answer correctness compared to the baseline models."

"The distinguishing feature of GAIA is not necessarily a higher accuracy of the underlying algorithms themselves, but the autonomous orchestration, integration, and adaptation of these algorithms within a unified scientific workflow."

"we plan to explore domain-focused LLMs that are fine-tuned on geothermal-specific data."

No batch-4 records yielded retrievable full text in this run. Every one of the 12 records
was attempted with WebFetch (per `deepread_instructions.md`) and blocked or extraction
failed; see `unreachable_batch_4.md` for the per-record detail. No papers.md blocks were
written, consistent with rule 1 ("nothing is written unless a tool call in this run
retrieved it").

## doi:10.5281/zenodo.21768634

https://zenodo.org/doi/10.5281/zenodo.21768634 — fetched via WebFetch on Zenodo landing page, full record description available (this is a companion code/data record, not the paper itself; the paper "An LLM-Agent Interface for End-to-End Probabilistic Seismic Hazard and Risk Analysis" is stated as "in review" at npj Natural Hazards and was not separately fetchable).

"Model Context Protocol (MCP) server exposing the 2020 European Seismic Hazard Model (ESHM20) and the 2020 European Seismic Risk Model (ESRM20) through 24 typed endpoints, backed by OpenQuake hazardlib."

"Covers hazard curves, uniform hazard and conditional mean spectra, surface (site-amplified) hazard, damage and average annual loss, retrofit comparison, per-tectonic-region custom ground-motion model substitution, and conditional-spectrum record selection from the Engineering Strong-Motion database."

[not stated in fetched text]

[not stated in fetched text]

"Companion code to Vemula, Jehel, Cotton and Gatti, 'An LLM-Agent Interface for End-to-End Probabilistic Seismic Hazard and Risk Analysis' (npj Natural Hazards, in review)."

[not stated in fetched text]

## doi:10.20517/aiagent.2026.11

https://www.oaepublish.com/articles/aiagent.2026.11 — fetched via WebFetch on DOI-redirected publisher page, full text available.

"DigMethpy integrates high-quality datasets, machine learning (ML) predictive models, and LLMs within a unified framework."

"The platform integrates ML predictive models, literature-derived knowledge bases, and LLMs...forming a closed-loop workflow."

"Cross-validation was employed as the primary evaluation method to ensure statistical robustness of the regression model."

"We designed the highly active quaternary molten alloy catalyst Bi70Ni18Cu6Co6, achieving methane conversion of 40.3% at 1,000 °C."

"DigMethpy is viewed as a practical first step toward an agentic infrastructure for molten catalyst design rather than a fully realized self-driving platform."

"Several bottlenecks still limit fully predictive molten catalyst discovery, including sparse literature data and incomplete compositional space coverage."

No records in batch 6 yielded fetchable full text. See `unreachable_batch_6.md` for the 12 attempted records and their exact failure modes (mostly OnePetro/SPE/IPTC and Elsevier paywalls, one oversized arXiv HTML render, two unparseable PDFs).

## arxiv:2607.18557

https://arxiv.org/html/2607.18557 — fetched via arxiv.org/html full text.

"The agent facilitates input-file creation, mesh inspection, fluid-property computation, and result post-processing."

"52 stateless MCP tools, grouped into six domains" covering schema/introspection, fluid & constitutive models, mesh generation, XML assembly & validation, post-processing, and preprocessing.

"everything that follows, from mining the papers to the figure that closes the loop...happened in a single conversational session, and took approximately one hour."

"The crest cell accumulates and holds, while the flank cells spike during injection and drain back to nearly zero — the no-hysteresis signature reported in both source papers."

"diagnoses issues, and suggests improvements, grounding every quantity in actual computation."

"Meshing complex reservoirs is particularly challenging and warrants a dedicated specialized agent. While Agents4GEOS can already launch jobs on computing clusters, more robust skill coverage is needed...Interacting with running simulations—monitoring convergence, diagnosing stalls, and steering or restarting runs mid-execution—remains an open direction."

## doi:10.48550/arxiv.2606.10286

https://arxiv.org/html/2606.10286 — fetched via arxiv.org/html full text.

"This work introduces a simulator-driven Large Language Model (LLM) scheduling framework in which the LLM acts as an autonomous decision-making agent, guided at each step by a custom simulator that encodes geotechnical precedence, extraction-processing coupling, and dynamic capacity constraints directly into the action generation mechanism."

"[The simulator] assesses viable actions, processes decisions, and updates the system state in real-time" — deployed via "the Ollama framework, enabling unrestricted local execution without reliance on external API services."

"Evaluated across mining instances of varying scale and time periods" against a novel MILP formulation, a greedy heuristic, and random selection, measuring NPV recovery, optimality gap ("(NPV_MILP - NPV_strategy) / NPV_MILP"), and execution time.

"the LLM-based framework recovers between 94\% and 99\% of the MILP optimal NPV while scaling linearly in computation time."

"Operating entirely without any LLM training, fine-tuning, or adaptation" and achieving "real-time adaptability and zero-shot generalization."

"Future work will extend evaluation to larger real-world block models" — the study incorporates "no geological grade uncertainty and commodity price variability."

## doi:10.48550/arxiv.2608.18272

https://arxiv.org/html/2608.18272 — fetched via arxiv.org/html full text.

"We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces it."

"an LLM-driven multi-agent search modifies only the components that the user has opened for editing" using "the Evolutionary Ensemble of Agents (EvE)," a "decentralized evolutionary framework that organizes multiple coding agents to iteratively propose and refine candidate programs"; "Candidates that violate the physical constraints of the task are rejected outright."

"Both operators retain their gains on data not used during the search," tested on "synthetic and field data that were not used during the search."

"Evo-POCS improves the SNR over classic POCS by 3.49 dB on average across missing ratios from 30% to 70%"; "Evo-MSSA improves the average reconstruction SNR by more than 7 dB over classic MSSA and by more than 3 dB over a stronger rank-reduction baseline."

"To the best of our knowledge, this is the first study to formulate the design of a seismic reconstruction operator as a constrained, LLM-driven program evolution task."

"The main cost at present is offline search computation: discovering an operator requires many candidate executions and is therefore substantially more expensive than running a fixed hand-designed solver."

## doi:10.48550/arxiv.2606.18661

https://arxiv.org/html/2606.18661 — fetched via arxiv.org/html full text (partial: methods/experiments/conclusion sections retrieved, page noted "Content truncated due to length" near the very end).

"LandslideAgent, a domain rule-enhanced agent taking LandslideVLM as its cognitive backbone, employs a dual-rule controller incorporating structured report metadata constraints and cross-validation identification constraints"

"LandslideAgent is equipped with specialized computational libraries (e.g., OpenMMLab for SegFormer and ConvNeXt) and interfaces with external geographic web services (including OpenTopography, Macrostrat, and OpenStreetMap)"

"LandslideBench comprises 2,130 samples. Each sample strictly adheres to the aligned Image-Mask-Text triplet structure"

"LandslideVLM achieves accuracy improvements of 10.96%, 32.87%, and 15.91% on landslide discrimination, fine-grained classification, and semantic description quality, respectively"

"LandslideAgent further enables autonomous multi-source spatial data inference, realizing full-process intelligence for landslide identification and analysis"

"Pervasive spectral confusion—driven by high intra-class variance and inter-class similarity—imposes a persistent bottleneck on fine-grained classification"

## doi:10.48550/arxiv.2512.14429

https://arxiv.org/html/2512.14429 — fetched via arxiv.org/html full text (complete: abstract, all five sections, case studies, conclusion, references).

"We introduce the first Model Context Protocol (MCP) server suite for SPECFEM (supporting 2D, 3D Cartesian, and 3D Globe versions)"

"tools that collectively turn these traditional codes into open computational engines amenable to programmatic control and intelligent automation"

"Validated through multiple case studies, the workflow operates seamlessly in both autonomous and interactive modes, yielding high-fidelity results consistent with standard baselines"

"The simulation completes successfully"

"the first application of MCP technology to computational seismology, this study significantly lowers the entry barrier, enhances reproducibility, and offers a promising avenue for advancing computational geophysics toward AI-assisted and automated scientific research"

"Future research will focus on expanding the MCP server functionalities to integrate a broader ecosystem of heterogeneous geophysical software...ultimately moving toward the vision of fully autonomous geophysical research"

## doi:10.1109/cvpr52734.2025.00369

https://arxiv.org/html/2501.06184 — fetched via arxiv.org/html full text (complete arXiv:2501.06184v1 content retrieved).

"GeoMap-Agent, the inaugural agent designed for geologic map understanding, which features three modules: Hierarchical Information Extraction (HIE), Domain Knowledge Injection (DKI), and Prompt-enhanced Question Answering (PEQA)."

"The tool pool provides various functionalities for modules of GeoMap-Agent. It currently contains more than 8 tools and is scalable to accommodate additional tools as needed."

"GeoMap-Bench, a benchmark for evaluating the performance of LLMs in geologic map understanding from 5 aspects: extracting, referring, grounding, reasoning, and analyzing."

"GeoMap-Agent achieves an overall score of 0.811 on GeoMap-Bench, significantly outperforming 0.369 of GPT-4o."

[not stated in fetched text]

"Despite incorporating domain knowledge from the expert group, conducting reasoning for question answering, such as fault detection and lithology composition, remains challenging. It struggles to recognize rocks with complex patterns or similar colors in the legend, especially in CGS subset."

## doi:10.48550/arxiv.2412.17339

https://arxiv.org/html/2412.17339 — fetched via arxiv.org/html full text (complete arXiv:2412.17339v1 content retrieved).

"MineAgent, a modular framework leveraging hierarchical judging and decision-making modules to improve multi-image reasoning and spatial-spectral integration."

"remote-sensing image judging tool suite is a collection of MLLM-based modules designed to extract critical features from remote-sensing data, including geological and hyperspectral images."

"Multiple complementary metrics are employed. The F1 score for positive classes (Pos.F1) evaluates the MLLMs' ability to identify deposits."

"highest improvement reaching 30.14% when paired with GPT-4o and 23.77% when paired with Qwen-7B."

"extensive experiments demonstrate the effectiveness of MineAgent, highlighting its potential to advance MLLMs in remote-sensing mineral exploration."

"This work can only recognize specific types of deposits, restricting its applicability to a wider range of mineral types."

