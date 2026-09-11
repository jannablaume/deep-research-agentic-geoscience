# Shortlist — 773 of 35046 harvested records

Cut: agentic_score >= 3, strong_hits >= 1, domain_score >= 4, LLM vocabulary present, a domain group identified. Ranked by score, then by touchpoint count, then citations.
Scores, groups and touchpoints are computed by `scripts/triage_tango.py` from title+abstract; they are a sorting aid and carry no authority. A touchpoint hit is not evidence that the system is relevant to TANGO, and no hit is not evidence that it is not. Screen every record below.


## Core (an agent that drives a simulator, solver, optimiser or scientific code) — 352

### doi:10.3997/2214-4609.202639027
**Open-DARTS-MCP: An MCP-Based Architecture for Agentic Reservoir Simulation Workflows** (2026) — n/a · cites 0 · score 31 (strong 6) · core/geoenergy_subsurface · doi:10.3997/2214-4609.202639027
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);[a-z]{3,}-mcp\b;[a-z]{3,}-mcp\b*;\bMCP[\s-]?(?:server|client|suite|frame
touchpoints: provenance_reproducibility;tool_exposure
Summary Recent advances in large language models (LLMs) and agentic systems have created new opportunities for automating complex engineering workflows. In subsurface modelling, where simulation pipelines combine structural and geological modelling, petrophysical property estimation, multiphase flow simulation, and history matching, such automation promises to significantly accelerate engineering workflows and decision-making. However, exposing computationally-intensive simulation capabilities…

### doi:10.3390/data11070180
**From Scientific Copilots to Tool-Grounded Autonomy: AI Agents in Simulation-Driven Materials Discovery** (2026) — Data · cites 0 · score 26 (strong 6) · core/computational_discovery · doi:10.3390/data11070180
signals: \bAI agents?\b;\bAI agents?\b*;\bcopilots?\b;\bcopilots?\b*;agent(?:ic)? workflows?;agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);self[- ]driving lab
touchpoints: provenance_reproducibility
Artificial intelligence (AI) agents and large language model (LLM) agents are beginning to move materials discovery beyond isolated prediction tasks and toward tool-grounded workflows that can retrieve prior knowledge, configure simulations, launch calculations, inspect outputs, and decide what to do next. However, adjacent reviews on materials informatics, self-driving laboratories, natural-language processing in materials science, and…

### doi:10.1145/3731599.3767349
**LangChain-Parsl: Connect Large Language Model Agents to High Performance Computing Resource** (2025) — n/a · cites 2 · score 24 (strong 5) · core/scientific_computing · doi:10.1145/3731599.3767349
signals: \bLLM[- ]?agents?\b;\bLangChain\b;\bLangChain\b*;agent(?:ic)? workflows?;language model agents?;language model agents?*;tool[- ]calling
touchpoints: hpc_scale_out
Large Language Models (LLMs) can improve performance in answering questions beyond their contextual understanding by running external tools, such as a calculator for arithmetics, an online query for real-time weather, et al. For scientific applications, this enables the LLM to perform and analyze simulation runs for more accurate answers. However, the increasing scale of scientific…

### doi:10.48550/arxiv.2604.07681
**Multi-Agent Orchestration for High-Throughput Materials Screening on a Leadership-Class System** (2026) — arXiv (Cornell University) · cites 0 · score 23 (strong 6) · core/scientific_computing · doi:10.48550/arxiv.2604.07681
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agent orchestration;agent orchestration*;agentic;model context protocol;
touchpoints: hpc_scale_out;tool_exposure
The integration of Artificial Intelligence (AI) with High-Performance Computing (HPC) is transforming scientific workflows from human-directed pipelines into adaptive systems capable of autonomous decision-making. Large language models (LLMs) play a critical role in autonomous workflows; however, deploying LLM-based agents at scale remains a significant challenge. Single-agent architectures and sequential tool calls often become serialization bottlenecks…

### doi:10.5281/zenodo.20055953
**Autonomous HPC Simulation Orchestration: Surveying Multi-Agent LLM Ecosystems and the NVIDIA Modulus Stack** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 21 (strong 5) · core/scientific_computing · doi:10.5281/zenodo.20055953
signals: \btool[- ]use\b;agent(?:ic)? workflows?;agentic;model context protocol;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*
touchpoints: hpc_scale_out;solver_control;tool_exposure
The orchestration of high-performance computing (HPC) physics simulations has historically demanded intensivemanual effort from domain specialists, encompassing problem specification, solver configuration, data pipeline construction,and iterative hyperparameter tuning. The emergence of large language model (LLM) agents capable of tool use and autonomous code generation presents a transformative opportunity to democratize and accelerate this process. This survey…

### doi:10.48550/arxiv.2512.07917
**CFD-copilot: leveraging domain-adapted large language model and model context protocol to enhance simulation automation** (2025) — arXiv (Cornell University) · cites 0 · score 21 (strong 4) · core/solver_control · doi:10.48550/arxiv.2512.07917
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bcopilots?\b;\bcopilots?\b*;model context protocol;model context protoc
touchpoints: tool_exposure
Configuring computational fluid dynamics (CFD) simulations requires significant expertise in physics modeling and numerical methods, posing a barrier to non-specialists. Although automating scientific tasks with large language models (LLMs) has attracted attention, applying them to the complete, end-to-end CFD workflow remains a challenge due to its stringent domain-specific requirements. We introduce CFD-copilot, a domain-specialized LLM…

### doi:10.48550/arxiv.2606.07850
**PDE-Agents: An LLM-Orchestrated Multi-Agent Framework for Automated Finite Element Simulations with Knowledge Graph-Augmented Reasoning** (2026) — arXiv (Cornell University) · cites 0 · score 19 (strong 4) · core/solver_control · doi:10.48550/arxiv.2606.07850
signals: \bLLM[- ]?agents?\b;\bLangGraph\b;language model agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: verification_regression
We present PDE-Agents, a multi-agent ecosystem that automates the full lifecycle of partial differential equation (PDE) and finite element method (FEM) simulations through natural-language interaction. Three large language model agents, Simulation, Analytics, and Database, are orchestrated by a LangGraph supervisor and run locally using Qwen3-Coder-Next and Llama 4 Scout on dual NVIDIA RTX PRO 6000…

### doi:10.5281/zenodo.20109894
**Agentic Optimizer: Multi-Agent LLM-Feedback-Driven AI Architecture for Subsurface Physics, Fluid-Flow Property Prediction, and Field Development Optimization** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 19 (strong 3) · core/geoenergy_subsurface · doi:10.5281/zenodo.20109894
signals: agentic;agentic*;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: optimisation_loop
Subsurface prediction and field development optimization require integrated reasoning over physics, fluid-flow behavior, heterogeneous rock properties, engineering constraints, incomplete data, dynamic operating decisions, and multi-objective trade-offs. This paper proposes an Agentic Optimizer of Feedback-Driven Multi-Agent AI Architecture as a reference architecture for subsurface physics, fluid-flow property prediction, and field development optimization. The architecture is conceptual…

### doi:10.11578/dc.20260516.1
**matsim-agents v1.0** (2026) — OSTI OAI (U.S. Department of Energy Office of Scientific and Technical Information) · cites 0 · score 18 (strong 5) · core/computational_discovery · doi:10.11578/dc.20260516.1
signals: \bLangGraph\b;agent orchestration;agentic;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: config_generation;hpc_scale_out;results_interpretation;solver_control
matsim-agents is a multi-agent AI framework for atomistic materials simulation and discovery. It orchestrates large language models (LLMs), machine-learned interatomic potentials (MLIPs), and DFT codes into a single agentic loop running on laptops and DOE leadership-class supercomputers. MULTI-AGENT ORCHESTRATION A LangGraph state machine with three nodes: a Planner that converts a natural-language research objective into…

### doi:10.1016/j.dche.2026.100312
**Large language model agent for user-friendly chemical process simulations** (2026) — Digital Chemical Engineering · cites 2 · score 18 (strong 4) · core/simulation_orchestration · doi:10.1016/j.dche.2026.100312
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);lan
touchpoints: results_interpretation;tool_exposure;topology_construction
Modern process simulators enable detailed process design, simulation, and optimization; however, constructing and interpreting simulations is time-consuming and requires expert knowledge. This limits early exploration by inexperienced users. To address this, a large language model (LLM) agent is integrated with AVEVA Process Simulation (APS) via Model Context Protocol (MCP), allowing natural language interaction with rigorous…

### doi:10.5281/zenodo.19593419
**7th International Conference on Big Data and Machine Learning (BDML 2026)** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 18 (strong 4) · core/scientific_computing · doi:10.5281/zenodo.19593419
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\btool[- ]using\b;autonomous agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){
touchpoints: hpc_scale_out;provenance_reproducibility;uncertainty_quantification
7th International Conference on Big Data and Machine Learning (BDML 2026) June 27 ~ 28, 2026, Copenhagen, Denmark https://www.bdml2026.org/Scope 7th International Conference on Big Data and Machine Learning (BDML 2026) will act as a major forum for the presentation of innovative ideas, approaches, developments, and research projects in the areas of Big Data and Machine…

### doi:10.1109/aiware69974.2025.00031
**HPCAgentTester: a Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation** (2025) — arXiv (Cornell University) · cites 1 · score 18 (strong 3) · core/scientific_computing · doi:10.1109/aiware69974.2025.00031
signals: \bLLM[- ]?agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+
touchpoints: hpc_scale_out
Unit testing in High-Performance Computing (HPC) is critical but challenged by parallelism, complex algorithms, and diverse hardware. Traditional methods often fail to address non-deterministic behavior and synchronization issues in HPC applications. This paper introduces HPCAgentTester, a novel multi-agent Large Language Model (LLM) framework designed to automate and enhance unit test generation for HPC software utilizing…

### doi:10.5194/egusphere-egu26-22037
**Risk to Resilience: LLM-Driven Agentic AI for Natural Hazard Assessment and Decision Support** (2026) — n/a · cites 0 · score 18 (strong 3) · core/simulation_orchestration · doi:10.5194/egusphere-egu26-22037
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: provenance_reproducibility
Recent advances in large language models (LLMs) are transforming how geoscientists interact with data, models, and decision-support systems. Beyond literature web search and text processing, LLMs now enable new forms of knowledge discovery, real-time analysis, and human–AI collaboration in natural hazards and climate-risk research. At the same time, the increasing availability of geospatial data, remote…

### doi:10.48550/arxiv.2605.20819
**DynaMate2: runtime registration of expert-defined tools for agentic scientific workflow automation** (2026) — arXiv (Cornell University) · cites 0 · score 18 (strong 4) · core/scientific_computing · doi:10.48550/arxiv.2605.20819
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLangGraph\b;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?
touchpoints: provenance_reproducibility
Agentic large-language-model systems can coordinate scientific tools, but many implementations remain difficult for domain scientists to extend without modifying the source orchestration code or relying on unconstrained code generation. DynaMate2 is a LangGraph-based multi-agent framework for converting expert-defined Python functions into persistent AI-callable tools. The architecture separates domain execution from LLM supervision: registered tools perform…

### doi:10.1145/3815572.3815744
**KBase Research Agent: Automated Multi-Agent Workflow Construction for Reproducible Genome Analysis** (2026) — bioRxiv (Cold Spring Harbor Laboratory) · cites 0 · score 18 (strong 3) · core/scientific_computing · doi:10.1145/3815572.3815744
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b*;agent(?:ic)? workflows?;agent(?:ic)? workflows?*;multi[- ]?agent[,\s]+(
touchpoints: provenance_reproducibility
Constructing multi-step bioinformatics workflows, from read quality control through genome assembly to functional annotation, requires expertise in both biology and computational tool selection, creating a bottleneck for scalable and reproducible analysis. We present the KBase Research Agent, a multi-agent system for automating such workflows within the DOE Systems Biology Knowledgebase (KBase). Given a set of…

### doi:10.5281/zenodo.21944484
**Reproducibility Artifact for Pre-Execution Auditing for Tool-Using AI Agents: A Reproducible Mixed Benchmark for Agentic Software Engineering** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 18 (strong 3) · core/scientific_computing · doi:10.5281/zenodo.21944484
signals: \bAI agents?\b;\bAI agents?\b*;\btool[- ]using\b;\btool[- ]using\b*;agentic;agentic*
touchpoints: provenance_reproducibility
This reproducibility artifact accompanies the paper Pre-Execution Auditing for Tool-Using AI Agents: A Reproducible Mixed Benchmark for Agentic Software Engineering. It contains the locked benchmark data, audit rubric, generated method outputs, aggregate results, paired comparisons, bootstrap confidence intervals, availability analysis, source-authority records, trace-replay results, benchmark runners, validators, verification records, and SHA-256 manifest supporting the manuscript.…

### doi:10.13031/ja.16663
**Frontier: LLM-Driven Agentic Digital Twins for Dairy Housing: From Data-Rich Facilities to Intelligent Controlled Environmental Systems** (2026) — Journal of the ASABE · cites 0 · score 18 (strong 3) · core/simulation_orchestration · doi:10.13031/ja.16663
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Highlights LLM agents transform dairy digital twins from prediction to reasoning. Agentic twins integrate physics, sensors, and management objectives. Edge–cloud agent twins enable robust long-term barn deployment. Explainable AI bridges engineering models and farm decisions. Keywords: Agentic AI, Computational fluid dynamics, Digital twins, Edge–cloud computing, Heat stress mitigation, Large language models, Precision livestock farming.…

### doi:10.3390/buildings15173190
**Human–AI Teaming in Structural Analysis: A Model Context Protocol Approach for Explainable and Accurate Generative AI** (2025) — Buildings · cites 8 · score 17 (strong 3) · core/solver_control · doi:10.3390/buildings15173190
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;model context protocol;model context protocol*
touchpoints: provenance_reproducibility;tool_exposure;verification_regression
The integration of large language models (LLMs) into structural engineering workflows presents both a transformative opportunity and a critical challenge. While LLMs enable intuitive, natural language interactions with complex data, their limited arithmetic reasoning, contextual fragility, and lack of verifiability constrain their application in safety-critical domains. This study introduces a novel automation pipeline that couples…

### doi:10.3929/ethz-c-000801434
**EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design** (2026) — ETH Zürich Research Collection · cites 0 · score 17 (strong 3) · core/scientific_computing · doi:10.3929/ethz-c-000801434
signals: \bLangGraph\b;\btool[- ]use\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: hpc_scale_out;topology_construction;verification_regression
Large Language Model (LLM) agents are increasingly applied to engineering design tasks, yet existing evaluation frameworks do not adequately address multi-agent systems that combine simulation, retrieval, and manufacturing preparation. We introduce a benchmark suite with three evaluation dimensions: (1) a workflow benchmark with seven prompt styles targeting distinct cognitive demands-including direct tool use, semantic disambiguation,…

### doi:10.26434/chemrxiv.15006587/v1
**Autonomous Flowsheet Synthesis, Simulation, and Analysis with a Locally Deployed Language Model Agent: An Open-Standard Interface to Aspen Plus** (2026) — ChemRxiv · cites 0 · score 17 (strong 4) · core/simulation_orchestration · doi:10.26434/chemrxiv.15006587/v1
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);language model agents?;language model agents?*;model context protocol;tool[- ]calling
touchpoints: tool_exposure;topology_construction
Large language model (LLM) agents are a promising route to automating rigorous process simulation, but the usual approach—having the model write the scripts that drive the simulator—is error-prone and insecure, especially for the compact open-weight models that industrial data confidentiality favors. This work instead connects LLMs to Aspen Plus® through the model context protocol (MCP),…

### doi:10.5194/wbf2026-553
**AI inference service in Digital Twins** (2026) — n/a · cites 0 · score 17 (strong 5) · core/simulation_orchestration · doi:10.5194/wbf2026-553
signals: \bCrewAI\b;\bLLM[- ]?agents?\b;\bLangChain\b;agent(?:ic)? workflows?;agentic
touchpoints: hpc_scale_out;results_interpretation
Biodiversity research increasingly relies on digital twins—high‑fidelity, data‑driven simulations that replicate ecosystems across spatial and temporal scales. While these twins excel at integrating heterogeneous observations (e.g., remote sensing, genomics, citizen science), they often remain limited by static model architectures and manual parameter tuning, constraining rapid hypothesis testing and adaptive management. We propose an inference service…

### doi:10.6084/m9.figshare.30931802
**Autonomous multi-agent AI accelerates hydroxide exchange membrane discovery through physics-grounded inverse design** (2025) — Figshare · cites 0 · score 17 (strong 4) · core/computational_discovery · doi:10.6084/m9.figshare.30931802
signals: \bLLM[- ]?agents?\b;model context protocol;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: optimisation_loop;tool_exposure
Hydroxide exchange membranes (HEMs) hold the key to platinum-free alkaline fuel cells and electrolyzers, yet their development remains constrained by a fundamental trilemma: ionic conductivity, alkaline stability and dimensional stability are governed by competing physical mechanisms, creating a complex Pareto frontier that has resisted decades of empirical optimization. Here we demonstrate that large language model…

### doi:10.48550/arxiv.2605.15028
**Multi-Agentic Approach for History Matching of Oil Reservoirs** (2026) — arXiv (Cornell University) · cites 0 · score 17 (strong 4) · core/optimisation_uq · doi:10.48550/arxiv.2605.15028
signals: agent orchestration;agentic;agentic*;language model agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: config_generation
History matching is a central inverse problem in reservoir engineering, where uncertain reservoir parameters must be calibrated against observations. Although automated history matching can reduce manual effort, practical deployment remains difficult because engineers must still configure heterogeneous workflows involving parameter selection, physically admissible bounds, optimizer choice, hyperparameter tuning, simulator execution, and diagnostic reporting. We propose…

### doi:10.63544/jbii.v5i5.188
**Self-Evolving Autonomous Software Architectures Using Large-Scale Graph Neural Networks and Real-Time Big Data Feedback Loops for Economic Optimization and Cost-Efficient Resource Allocation** (2026) — Journal of Business Insight and Innovation · cites 0 · score 17 (strong 4) · core/simulation_orchestration · doi:10.63544/jbii.v5i5.188
signals: \bAI agents?\b;agentic;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: hpc_scale_out
The rapid growth of cloud-native, microservice-based, and distributed computing environments has exposed the limits of conventional software architectures that rely on static rules, manually configured resource policies, and human-driven adaptation. These limitations often produce resource overprovisioning, higher operational costs, delayed failure recovery, and inefficient use of computational capacity. This study proposes a Self-Evolving Autonomous Software…

### doi:10.1016/j.bdes.2026.100042
**A generalizable automated geophysical agent workflow for accessible subsurface hydrology analysis** (2026) — Big Data and Earth System · cites 0 · score 17 (strong 3) · core/geoenergy_subsurface · doi:10.1016/j.bdes.2026.100042
signals: agent(?:ic)? workflows?;agent(?:ic)? workflows?*;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility
Geophysical methods are central to subsurface imaging, yet their end-to-end workflows from data ingestion and inversion to petrophysical conversion remain inaccessible to non-specialists due to steep software and methodological learning curves. Large language models (LLMs) are increasingly used as code assistants in scientific computing, but this approach still assumes that domain experts design and maintain…

### doi:10.25417/uic.32994011.v1
**Multi-Agent LLMs for Adaptive Acquisition in Bayesian Optimization** (2026) — University of Illinois Chicago · cites 0 · score 16 (strong 3) · core/optimisation_uq · doi:10.25417/uic.32994011.v1
signals: \bLLM[- ]?agents?\b;agentic;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*
touchpoints: optimisation_loop;provenance_reproducibility;surrogate_modelling
Bayesian Optimization (BO) is widely used to optimize expensive black-box objectives by learning a probabilistic surrogate and querying new points via an acquisition function. Classic approaches, however, bind acquisition behavior tightly to the surrogate (often a GP) and a small set of fixed statistics (e.g., mean/variance), which can make exploration–exploitation trade-offs inflexible and sensitive to…

### title:agenticaienabledphysicsinformedmachinelearningframeworkforintelligentbuildingmodelingcontrolandautomation
**AGENTIC AI-ENABLED PHYSICS-INFORMED MACHINE LEARNING FRAMEWORK FOR INTELLIGENT BUILDING MODELING, CONTROL, AND AUTOMATION** (2026) — Syracuse University Libraries (Syracuse University) · cites 0 · score 16 (strong 4) · core/simulation_orchestration · https://surface.syr.edu/etd/2334
signals: agentic;agentic*;language model agents?;model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: hpc_scale_out;tool_exposure
Buildings account for a significant share of global energy consumption, and meeting the 2050 net-zero decarbonization targets requires retrofitting approximately 10,000 buildings per day in the United States alone. However, current human-centered workflows for building modeling, simulation, control, and operation remain too slow and labor-intensive to support deployment at this scale. This dissertation proposes an…

### doi:10.1016/j.cma.2026.118985
**ALL-FEM: Agentic Large Language Models fine-tuned for finite element methods** (2026) — Computer Methods in Applied Mechanics and Engineering · cites 3 · score 16 (strong 3) · core/solver_control · doi:10.1016/j.cma.2026.118985
signals: agent(?:ic)? workflows?;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: results_interpretation
Finite element (FE) analysis guides the design and verification of nearly all manufactured objects. It is at the core of computational engineering, enabling simulation of complex physical systems, from fluids and solids to multiphysics systems. However, implementing FE codes and analyzing simulation results demands expertise across numerical analysis, continuum mechanics, and programming. Conventional Large Language…

### doi:10.1016/j.net.2026.104573
**Embedding Bayesian optimization in a multi-agent large language model framework for critical heat flux modeling with uncertainty quantification** (2026) — Nuclear Engineering and Technology · cites 0 · score 15 (strong 3) · core/optimisation_uq · doi:10.1016/j.net.2026.104573
signals: \bLLM[- ]?agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: optimisation_loop;provenance_reproducibility;uncertainty_quantification
Large language model (LLM) agents can automate engineering modeling, but self-generated hyperparameter searches often trail expert baselines and vary across runs. We present OPTIMA (Orchestrated, Physics-driven, Tool-Integrated Multi-Agent), an optimization-integrated multi-agent framework that delegates numerical search to a validated ensemble optimization tool rather than asking agents to generate optimization code. A supervisor coordinates coding, execution,…

### doi:10.5281/zenodo.19597589
**aihydro-tools: An Open Python MCP Server for Autonomous Hydrological Research** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 15 (strong 4) · core/scientific_computing · doi:10.5281/zenodo.19597589
signals: [a-z]{3,}-mcp\b;\bAI agents?\b;\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool)*;model context protocol
touchpoints: provenance_reproducibility;tool_exposure
aihydro-tools is the Python backend and MCP tool server that powers AI-Hydro. It provides an open, extensible set of validated hydrological research tools that any Model Context Protocol (MCP)-compatible AI agent can discover and invoke to carry out end-to-end computational hydrology workflows. Installable as a standalone Python package (pip install aihydro-tools), it exposes the aihydro-mcp…

### doi:10.1371/journal.pone.0353610
**Agentic AI-enhanced digital twins for Smart City civil infrastructure: A secure, autonomous and auditable management framework** (2026) — PLoS ONE · cites 2 · score 15 (strong 4) · core/simulation_orchestration · doi:10.1371/journal.pone.0353610
signals: \bLangChain\b;\bLangGraph\b;agent orchestration;agentic;agentic*
touchpoints: provenance_reproducibility
Smart city implementation increasingly relies on sensing and analytics; however, a persistent operational gap remains between anomaly detection and safe, timely, and accountable intervention in civil infrastructure systems. This paper proposes an Agentic AI-supported Digital Twin framework for smart city civil infrastructure management, where monitoring and action are linked and auditability is maintained. The Digital…

### doi:10.25394/pgs.32118403
**Physics Driven Generative Artificial Intelligence for Nuclear Reactor Digital Twins** (2026) — Purdue · cites 0 · score 15 (strong 4) · core/simulation_orchestration · doi:10.25394/pgs.32118403
signals: \btool[- ]use\b;agent(?:ic)? workflows?;agentic;tool[- ]calling
touchpoints: surrogate_modelling
Nuclear reactor digital twins integrate sensor data, documentation, simulation models, and state-estimation tools in a broader data assimilation scheme to support reactor monitoring and decision making. However, as reactor systems become increasingly digitalized, the problem shifts from data availability to one of information overload: the ability/inability of operators to retrieve, interpret, and act on the…

### doi:10.26434/chemrxiv-2025-f1wcr
**Honegumi RAG Assistant: An Agentic System for Accelerating Bayesian Optimization Adoption in Experimental Sciences** (2025) — ChemRxiv · cites 0 · score 15 (strong 3) · core/optimisation_uq · doi:10.26434/chemrxiv-2025-f1wcr
signals: \bLangGraph\b;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: optimisation_loop
Bayesian optimization (BO) has become increasingly important for experimental optimization across scientific domains, yet implementing BO pipelines requires significant programming expertise and familiarity with specialized frameworks. This creates a barrier for domain experts who could benefit from BO but lack the technical background to implement it. We present Honegumi RAG Assistant, an agentic AI system…

### doi:10.26434/chemrxiv.15005838/v1
**Raven: agentic AI for materials discovery enabled by post-trained chemistry LLMs** (2026) — ChemRxiv · cites 0 · score 15 (strong 3) · core/computational_discovery · doi:10.26434/chemrxiv.15005838/v1
signals: agentic;agentic*;language model agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility
Large language model agents can connect scientific text, molecular generation, simulation, and laboratory planning, but their use in materials discovery is limited by weak reproducibility, hidden intermediate state, and scarce domain-specific quantum-chemical data. Here we introduce Raven, a state-aware multi-agent framework for materials discovery powered by QuantumChem-200K, a corpus of more than 214,000 organic molecules…

### doi:10.1109/etfa54631.2023.10275362
**Towards autonomous system: flexible modular production system enhanced with large language model agents** (2023) — arXiv (Cornell University) · cites 92 · score 15 (strong 3) · core/simulation_orchestration · doi:10.1109/etfa54631.2023.10275362
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\bLLM[- ]?agents?\b;language model agents?;language model agents?*
touchpoints: none
In this paper, we present a novel framework that combines large language models (LLMs), digital twins and industrial automation system to enable intelligent planning and control of production processes. We retrofit the automation system for a modular production facility and create executable control interfaces of fine-granular functionalities and coarse-granular skills. Low-level functionalities are executed by…

### doi:10.7256/2454-0714.2026.3.78692
**Architecture for continuous business process reengineering based on agentic ai technology and digital twins of the organization (dto)** (2026) — Программные системы и вычислительные методы · cites 0 · score 15 (strong 4) · core/simulation_orchestration · doi:10.7256/2454-0714.2026.3.78692
signals: \bReAct\b;agent orchestration;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The paper presents a conceptual architecture for continuous business process reengineering based on the integration of Agentic AI and Digital Twin of Organization (DTO) technologies. The relevance of the study is driven by the fundamental inadequacy of the classical BPR paradigm under conditions of high environmental volatility in 2025–2026, where market windows shrink to weeks…

### doi:10.48550/arxiv.2603.12813
**Context is all you need: Towards autonomous model-based process design using agentic AI in flowsheet simulations** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 3) · core/simulation_orchestration · doi:10.48550/arxiv.2603.12813
signals: \bcopilots?\b;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Agentic AI systems integrating large language models (LLMs) with reasoning and tooluse capabilities are transforming various domains - in particular, software development. In contrast, their application in chemical process flowsheet modelling remains largely unexplored. In this work, we present an agentic AI framework that delivers assistance in an industrial flowsheet simulation environment. To this end,…

### doi:10.5281/zenodo.20792042
**Structured PREreview of "From Text to Simulation: A Multi-Agent LLM Workflow for Automated Chemical Process Design"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 15 (strong 2) · core/simulation_orchestration · doi:10.5281/zenodo.20792042
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:syste
touchpoints: none
This Zenodo record is a permanently preserved version of a Structured PREreview. You can view the complete PREreview at https://prereview.org/reviews/20792042. Does the introduction explain the objective of the research presented in the preprint? Yes The introduction explains the objective by describing the challenges of translating chemical process descriptions into simulation models and identifying the need…

### title:mechanicaldesignusingmultiphysicsagenticaivolume1fundamentalsaifundamentalsgenairlbasicsengineeringintroduction
**Mechanical design using multiphysics & Agentic AI - Volume 1: Fundamentals. AI fundamentals, Gen AI, RL basics & engineering introduction** (2026) — Research Portal (Queen's University Belfast) · cites 0 · score 15 (strong 3) · core/simulation_orchestration · https://pure.qub.ac.uk/en/publications/55235056-4ee0-4976-9ca0-5dad37a26975
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;agentic;agentic*;autonomous agents?
touchpoints: none
This foundational volume provides the complete theoretical and practical base for the entire 5-volume series. What is covered in Volume 1: Chapters 1–11: Full introduction to AI Fundamentals Core concepts of Agentic AI (autonomous agents that plan and act independently) Generative AI (LLMs such as Grok 4 for code generation) Reinforcement Learning (reward-based learning and…

### doi:10.2523/iptc-25122-ms
**Solving Upstream Complexity: EnergyAI's Agentic RAG and A2A Framework for Faster Subsurface Insights** (2026) — n/a · cites 0 · score 15 (strong 2) · core/geoenergy_subsurface · doi:10.2523/iptc-25122-ms
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Abstract The energy industry faces growing demands for efficiency, accuracy, and accelerated decision-making in upstream operations. EnergyAI addresses these challenges by leveraging cutting-edge AI technologies—Agentic AI, Multimodal AI, and Retrieval-Augmented Generation (RAG)—to enhance exploration, reservoir characterization, drilling optimization, and field development. By fine-tuning large language models (LLMs) with domain-specific knowledge, EnergyAI serves as an intelligent…

### doi:10.48550/arxiv.2608.14573
**WARA: Toward Automated Wireless Optimization Research with Closed-Loop LLM Agents** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 3) · core/simulation_general · doi:10.48550/arxiv.2608.14573
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*;\btool[- ]use\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large language model (LLM) agents are increasingly capable of tool use, code execution, artifact inspection, and iterative revision, creating new opportunities for automating scientific and engineering research. To the best of our knowledge, this paper presents the first end-to-end autoresearch framework for the wireless domain, with a focus on wireless resource allocation optimization. We propose…

### doi:10.2118/229629-ms
**Agentic Framework for Intelligent Surrogate Modeling of Simulator-Driven Workflows** (2025) — n/a · cites 0 · score 14 (strong 3) · core/optimisation_uq · doi:10.2118/229629-ms
signals: \bLLM[- ]?agents?\b;agentic;agentic*;autonomous agents?
touchpoints: solver_control;surrogate_modelling;uncertainty_quantification
Abstract We introduce a novel large-language-model (LLM) driven agentic framework to automate end-to-end surrogate modeling of simulator-driven workflows in the oil and gas domain. The autonomous agent orchestrates critical steps—initial sampling, simulator execution, adaptive retraining, and strategy switching—to minimize expensive simulator calls while meeting accuracy targets with minimal subject matter expert (SME) intervention. Applied to…

### doi:10.48550/arxiv.2509.18178
**Foam-Agent 2.0: An End-to-End Composable Multi-Agent Framework for Automating CFD Simulation in OpenFOAM** (2025) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/solver_control · doi:10.48550/arxiv.2509.18178
signals: agentic;model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: hpc_scale_out;tool_exposure
Computational Fluid Dynamics (CFD) is an essential simulation tool in engineering, yet its steep learning curve and complex manual setup create significant barriers. To address these challenges, we introduce Foam-Agent, a multi-agent framework that automates the entire end-to-end OpenFOAM workflow from a single natural language prompt. Our key innovations address critical gaps in existing systems:…

### doi:10.1016/j.jma.2025.08.021
**From LLM to Agent: A large-language-model-driven machine learning framework for catalyst design of MgH2 dehydrogenation** (2025) — Journal of Magnesium and Alloys · cites 17 · score 14 (strong 2) · core/computational_discovery · doi:10.1016/j.jma.2025.08.021
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: optimisation_loop
• AI framework automates MgH 2 catalyst data extraction from literature. • LLM to Agent approach accelerates MgH 2 catalyst discovery and design. • Machine learning predicts MgH 2 dehydrogenation with high accuracy. • Cat-Advisor provides actionable catalyst design recommendations. • Open database and AI tools advance hydrogen storage materials research. Magnesium hydride (MgH 2…

### doi:10.5281/zenodo.20388035
**Open FEM Agent: A Multi-Solver MCP Server for LLM-Driven Computational Mechanics** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 14 (strong 3) · core/solver_control · doi:10.5281/zenodo.20388035
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool)*;agent(?:ic)? workflows?;model context protocol
touchpoints: tool_exposure
Open FEM Agent is an open-source Model Context Protocol (MCP) server that connects general-purpose LLM coding agents to seven independently developed finite element solvers (FEniCSx, deal.II, 4C Multiphysics, NGSolve, scikit-fem, Kratos Multiphysics, DUNE-fem). It exposes a small set of shared tools for solver discovery, simulation preparation, mesh generation, run execution, multi-solver coupling, in-place solver development,…

### arxiv:2602.11666
**PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 2) · core/solver_control · doi:10.48550/arxiv.2602.11666
signals: agentic;agentic*;autonomous agents?
touchpoints: solver_control
The deployment of autonomous agents for Computational Fluid Dynamics (CFD), is critically limited by the probabilistic nature of Large Language Models (LLMs), which struggle to enforce the strict conservation laws and numerical stability required for physics-based simulations. Reliance on purely semantic Retrieval Augmented Generation (RAG) often leads to "context poisoning," where agents generate linguistically plausible…

### doi:10.48550/arxiv.2511.03852
**Advancing Subsurface Discovery and Geothermal Monitoring with an Agentic Artificial Intelligence Framework** (2025) — arXiv (Cornell University) · cites 0 · score 14 (strong 2) · core/geoenergy_subsurface · doi:10.48550/arxiv.2511.03852
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;agentic;agentic*
touchpoints: surrogate_modelling
Geothermal field development typically involves complex processes that require multi-disciplinary expertise in each process. Thus, decision-making often demands the integration of geological, geophysical, reservoir engineering, and operational data under tight time constraints. We present Geothermal Analytics and Intelligent Agent, or GAIA, an AI-based system for automation and assistance in geothermal field development. GAIA consists of…

### doi:10.65109/jlge7606
**MACC: Multi-Agent Collaborative Competition for Scientific Exploration** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/scientific_computing · doi:10.65109/jlge7606
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framewor
touchpoints: provenance_reproducibility
Scientific discovery still relies heavily on the manual efforts of individual researchers, leading to limited exploration, redundant trials, and reduced reproducibility. Human-participant data analysis competitions generate diverse approaches, yet fluctuations in participation and the lack of independent repetitions show that parallel exploration alone is insufficient for achieving reliable scientific inquiry. As advanced AI agents based…

### doi:10.48550/arxiv.2608.29665
**Evaluating a 4B open-weights local LLM for agentic DFT workflows: a literature reproducibility audit** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/scientific_computing · doi:10.48550/arxiv.2608.29665
signals: agent(?:ic)? workflows?;agentic;agentic*;autonomous agents?
touchpoints: provenance_reproducibility
Agentic workflows in materials science relying on hosted commercial models face severe reproducibility, economic, and data-privacy constraints. To explore fully local agentic science, this work evaluates an open-weights Qwen3:4B model executing an autonomous scientific pipeline across varying hardware constraints. Applied to pentagonal two-dimensional materials, the system extracts parameters from unstructured text, translates them into density…

### doi:10.2139/ssrn.4921381
**Metaopenfoam: An Llm-Based Multi-Agent Framework for Cfd** (2024) — SSRN Electronic Journal · cites 18 · score 14 (strong 2) · core/solver_control · doi:10.2139/ssrn.4921381
signals: \bLangChain\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Remarkable progress has been made in automated problem solving through societies of agents based on large language models (LLMs). Computational fluid dynamics (CFD), as a complex problem, presents unique challenges in automated simulations that require sophisticated solutions. MetaOpenFOAM, as a novel multi-agent collaborations framework, aims to complete CFD simulation tasks with only natural language as…

### doi:10.1049/icp.2025.2536
**AI-driven smart home energy optimization: integrating AI agents with IoT for adaptive decision-making** (2025) — IET conference proceedings. · cites 2 · score 14 (strong 3) · core/simulation_orchestration · doi:10.1049/icp.2025.2536
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b;\bAI agents?\b*;agentic
touchpoints: none
As the Internet of Things (IoT) revolutionizes intelligent environments, energy efficiency remains a critical challenge. Traditional IoT-based energy management systems rely on predefined rule-based automation, which lacks adaptability to dynamic environmental conditions. This study proposes an Agentic AIoT system that integrates AI Agents, Large Language Models (LLMs), and Digital Twin technology to enhance IoT decision-making…

### doi:10.48550/arxiv.2603.26005
**AutoB2G: Agentic Simulation and Reinforcement Learning for Spatio-Temporal Grid-Interactive Building Control** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/simulation_orchestration · doi:10.48550/arxiv.2603.26005
signals: \bLLM[- ]?agents?\b;agentic;agentic*;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
Grid-interactive building control has emerged as a promising approach for improving demand-side flexibility in modern power systems. Realistic studies of such systems, however, require tightly coupled co-simulation across buildings, reinforcement learning (RL), and distribution grids to capture time-varying control dynamics over spatially distributed grid infrastructures. Constructing these workflows remains highly challenging in practice: researchers must…

### doi:10.48550/arxiv.2605.06607
**AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/solver_control · doi:10.48550/arxiv.2605.06607
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);AI scientist;\bAI agents?\b;\bAI agents?\b*
touchpoints: none
Recent LLM-based agents have closed substantial portions of the scientific discovery loop in software-only machine-learning research, in chemistry, and in biology. Extending the same loop to high-fidelity physical simulators is harder, because solver completion does not imply physical validity and many failure modes appear only in field-level imagery rather than in solver logs. We present…

### doi:10.48550/arxiv.2509.07506
**Astra: A Multi-Agent System for GPU Kernel Performance Optimization** (2025) — arXiv (Cornell University) · cites 0 · score 14 (strong 3) · core/simulation_general · doi:10.48550/arxiv.2509.07506
signals: \bLLM[- ]?agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|wo
touchpoints: none
GPU kernel optimization has long been a central challenge at the intersection of high-performance computing and machine learning. Efficient kernels are crucial for accelerating large language model (LLM) training and serving, yet attaining high performance typically requires extensive manual tuning. Compiler-based systems reduce some of this burden, but still demand substantial manual design and engineering…

### doi:10.48550/arxiv.2505.04997
**Foam-Agent: A Large Language Model-Based Multi-Agent Framework for Automating Computational Fluid Dynamics Workflows** (2025) — arXiv (Cornell University) · cites 1 · score 13 (strong 2) · core/solver_control · doi:10.48550/arxiv.2505.04997
signals: model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: config_generation;tool_exposure
Computational fluid dynamics (CFD) has been the main workhorse of computational physics, yet its steep learning curve and fragmented, multi-stage workflow create significant barriers to entry. We present Foam-Agent, a multi-agent framework that leverages large language models (LLMs) to automate the end-to-end CFD workflow in OpenFOAM from a single natural-language prompt. Foam-Agent rests on three…

### doi:10.1016/j.compenvurbsys.2026.102449
**Towards fully automated city operations: Integrating agentic AI with urban digital twins** (2026) — Computers Environment and Urban Systems · cites 2 · score 13 (strong 3) · core/simulation_orchestration · doi:10.1016/j.compenvurbsys.2026.102449
signals: \bAI agents?\b;agentic;agentic*;model context protocol
touchpoints: tool_exposure
The convergence of generative AI with the emerging agentic AI paradigm, the Model Context Protocol (MCP), and urban digital twins offers transformative potential for automating the management of complex urban systems. In this paper, we demonstrate how agentic digital twins can generate knowledgeaugmented workflows through multi-step reasoning and autonomously execute them via coordinated AI agents…

### doi:10.2139/ssrn.6672588
**VirtualLab_CC: An LLM-Augmented Virtual Laboratory for Automated Computational Chemistry Research** (2026) — SSRN Electronic Journal · cites 0 · score 13 (strong 3) · core/scientific_computing · doi:10.2139/ssrn.6672588
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);AI scientist;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|
touchpoints: hpc_scale_out
Recent advances in large language models (LLMs) have opened new avenues for automating scientific research workflows. Systems like the AI Scientist [1] demonstrate fully autonomous endto-end research pipelines for machine learning, but their applicability to domains requiring expensive high-performance computing (HPC) resources, specialized quantum chemistry software, and rigorous thermochemical accuracy remains unexplored. Here we present…

### doi:10.1016/j.apenergy.2025.126670
**A systematic review of transformers and large language models in the energy sector: towards agentic digital twins** (2025) — Applied Energy · cites 56 · score 13 (strong 1) · core/simulation_orchestration · doi:10.1016/j.apenergy.2025.126670
signals: agentic;agentic*
touchpoints: none
Artificial intelligence (AI) has long promised to improve energy management in smart grids by enhancing situational awareness and supporting more effective decision-making. While traditional machine learning has demonstrated notable results in forecasting and optimization, it often struggles with generalization, situational awareness, and heterogeneous data integration. Recent advances in Transformer architecture, including Large Language Models (LLMs)…

### doi:10.1016/j.autcon.2026.106791
**LLM-enabled multi-agent framework for natural language interaction with graph-based digital twins** (2026) — Automation in Construction · cites 9 · score 13 (strong 2) · core/simulation_orchestration · doi:10.1016/j.autcon.2026.106791
signals: \bLangChain\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Digital twins are increasingly used in the Architecture, Engineering, and Construction (AEC) industry, but their adoption is often hindered by the need for specialised knowledge, such as database querying. This paper presents Graph-DT-GPT, a multi-agent framework that integrates Large Language Models (LLMs) with graph-based digital twins to enable natural language interaction. The framework is designed…

### doi:10.2118/229905-ms
**Multi-Agentic Generative AI Framework for Accelerating Field Development Planning** (2025) — n/a · cites 0 · score 13 (strong 2) · core/geoenergy_subsurface · doi:10.2118/229905-ms
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Abstract This paper introduces a multi-agentic solution that leverages Generative AI—specifically, Large Language Models (LLMs) coupled with domain-specific engines—to enhance the efficiency, consistency, and technical depth of reservoir simulation workflows. The solution targets three high-value areas: simulation model compliance, insight generation, and well placement optimization, with the goal of accelerating field development planning and institutionalizing…

### doi:10.64898/2026.07.29.741496
**Scientific computing in the age of agentic AI: an exploratory field report** (2026) — bioRxiv (Cold Spring Harbor Laboratory) · cites 0 · score 13 (strong 3) · core/scientific_computing · doi:10.64898/2026.07.29.741496
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLLM[- ]?agents?\b;agentic;agentic*
touchpoints: none
Abstract Scientific computing has become a central component of modern scientific discovery. Yet many computational tools are developed by small, specialized teams under incentives that encourage the release of rapidly prototyped tooling without commensurate attention to engineering concerns, including performance and maintainability. These gaps are particularly visible in the life sciences, where the advent of…

### doi:10.48550/arxiv.2508.07035
**VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations** (2025) — arXiv (Cornell University) · cites 2 · score 12 (strong 4) · core/computational_discovery · doi:10.48550/arxiv.2508.07035
signals: \bCrewAI\b;\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: config_generation;hpc_scale_out;tool_exposure
Density-functional-theory (DFT) simulations with the Vienna Ab initio Simulation Package (VASP) are indispensable in computational materials science but often require extensive manual setup, monitoring, and postprocessing. Here, we introduce VASPilot, an open-source platform that fully automates VASP workflows via a multi-agent architecture built on the CrewAI framework and a standardized Model Context Protocol (MCP). VASPilot's…

### doi:10.3997/2214-4609.202637165
**Conversational and Agentic Workflows for Constructing and Executing Fully-Differentiable Reservoir Simulation Models** (2026) — n/a · cites 0 · score 12 (strong 2) · core/geoenergy_subsurface · doi:10.3997/2214-4609.202637165
signals: agent(?:ic)? workflows?;agent(?:ic)? workflows?*;agentic;agentic*
touchpoints: provenance_reproducibility;solver_control;uncertainty_quantification
Summary The formulation of reservoir simulation models requires translating high-level geological and engineering intent into detailed numerical specifications that are internally consistent, executable, and physically meaningful. Even for conceptual studies, this translation involves numerous modeling decisions related not only to governing equations and parameters, but also to grid construction, geometry manipulation, heterogeneity generation, well configuration,…

### arxiv:2607.20346
**IteraSim RAG: A Multi-Stage Retrieval-Augmented Agentic Back-End for OpenFOAM-Based Computational Fluid Dynamics** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 1) · core/solver_control · doi:10.48550/arxiv.2607.20346
signals: agentic;agentic*
touchpoints: config_generation;provenance_reproducibility;solver_control
Configuring a computational fluid dynamics (CFD) case in OpenFOAM requires assembling a multi-directory input deck of mutually consistent solver, discretisation and boundary-condition dictionaries -- a task that remains a substantial barrier to non-specialist use of open-source CFD software. Large language models (LLMs) coupled with retrieval-augmented generation (RAG) can lower this barrier, but existing systems retrieve…

### doi:10.5281/zenodo.22062244
**TOPO-GEMMA-4-E4B-VISION: Concurrent Certification for Catastrophic Forgetting in Vision-Language Models A Multi-Agent Implementation of the TOPO-2026 Framework** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 12 (strong 3) · core/scientific_computing · doi:10.5281/zenodo.22062244
signals: agent orchestration;agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: config_generation;provenance_reproducibility;verification_regression
TOPO-GEMMA-4-E4B-VISION: Full Summary 📋 Overview TOPO-GEMMA-4-E4B-VISION is a vision-language model that achieves 100% accuracy across 13 classification tasks with 0% catastrophic forgetting through the TOPO-2026 prime-anchored memory architecture. Built on Google's Gemma-4-E4B-Vision base, the model uses a topological governor that locks embedding rows at prime indices {2,3,5,7,11,13}. The complete implementation is open-source on Hugging Face…

### doi:10.1145/3785462.3815873
**BioCodex: HPC-Native Agentic Genomics Workflows via MCP RunSpecs and Asynchronous Slurm Execution** (2026) — n/a · cites 0 · score 12 (strong 3) · core/scientific_computing · doi:10.1145/3785462.3815873
signals: [a-z]{3,}-mcp\b;agentic;agentic*;model context protocol
touchpoints: hpc_scale_out;provenance_reproducibility;tool_exposure
Agentic AI assistants show promise for accelerating scientific discovery, but production high-performance computing (HPC) deployment adds requirements such as queued execution, resource governance, and auditable provenance. We present BioCodex (palmetto-mcp), an HPC-native AI tooling framework that enables an assistant to discover scientific tools, generate deterministic execution plans, and dispatch heavy computation asynchronously to a Slurm…

### doi:10.5281/zenodo.21369399
**Artificial Intelligence as the Fourth Paradigm of Scientific Discovery: Integrating Physics, Computational Intelligence, and Materials Science for Next-Generation Research and Engineering Subtitle** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 12 (strong 3) · core/scientific_computing · doi:10.5281/zenodo.21369399
signals: AI scientist;autonomous experimentation;self[- ]driving lab
touchpoints: provenance_reproducibility;uncertainty_quantification
Alternative Combined Title–1 Why Physics Needs Artificial Intelligence: A Unified Framework for AI-Assisted Scientific Discovery, Computational Physics, and Intelligent Materials Engineering Subtitle From Classical Physics to Autonomous Scientific Intelligence through Machine Learning, Physics-Informed Neural Networks, and Digital Scientific Computing Alternative Combined Title–2 Artificial Intelligence Meets Physics: Transforming Scientific Discovery Through Computational Intelligence, Data-Driven Modeling, and…

### doi:10.31223/x5f47g
**Agentic Modelling Pipeline: Reproducible Rapid Stormwater Modelling Management System with OpenClaw** (2026) — n/a · cites 0 · score 12 (strong 3) · core/scientific_computing · doi:10.31223/x5f47g
signals: agentic;agentic*;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;model context protocol
touchpoints: provenance_reproducibility;tool_exposure
Configuring urban hydrological models, such as SWMM, for operational or real-time modelling remains onerous for many models. We propose an Agentic SWMM workflow, which embeds ‘Skills’ and model context protocols to automate model configuration, execution, and extract and plot quantities of interest. To ensure that the entire Agentic SWMM workflow is auditable and reproducible, each…

### doi:10.5281/zenodo.19595083
**fischesn/phys-mcp: v1.0.1** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 12 (strong 3) · core/simulation_orchestration · doi:10.5281/zenodo.19595083
signals: [a-z]{3,}-mcp\b;[a-z]{3,}-mcp\b*;\bAI agents?\b;model context protocol
touchpoints: provenance_reproducibility;tool_exposure
phys-MCP Prototype: Bridging Physical and Digital AI Systems This repository provides the reference prototype accompanying the paper: phys-MCP: Bridging Physical and Digital AI Systems via a Substrate-Aware Control Plane It implements a control-plane abstraction for integrating heterogeneous physical neural network (PNN) substrates into AI-driven systems, following an MCP-style interaction model. Overview The phys-MCP prototype demonstrates…

### doi:10.48550/arxiv.2511.11788
**MALBO: Optimizing LLM-Based Multi-Agent Teams via Multi-Objective Bayesian Optimization** (2025) — arXiv (Cornell University) · cites 0 · score 12 (strong 3) · core/optimisation_uq · doi:10.48550/arxiv.2511.11788
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[
touchpoints: optimisation_loop;surrogate_modelling
The optimal assignment of Large Language Models (LLMs) to specialized roles in multi-agent systems is a significant challenge, defined by a vast combinatorial search space, expensive black-box evaluations, and an inherent trade-off between performance and cost. Current optimization methods focus on single-agent settings and lack a principled framework for this multi-agent, multi-objective problem. This thesis…

### doi:10.5194/egusphere-egu26-15002
**Toward Federated Agentic Workflows for Numerical Weather Prediction With Chiltepin** (2026) — n/a · cites 0 · score 12 (strong 2) · core/scientific_computing · doi:10.5194/egusphere-egu26-15002
signals: agent(?:ic)? workflows?;agent(?:ic)? workflows?*;agentic;agentic*
touchpoints: hpc_scale_out;provenance_reproducibility
The development of efficient, scalable, and interoperable workflow management systems is critical for supporting reproducible research to drive the scientific advancement of earth system modeling capabilities. Many workflow systems targeted for earth system science have been developed to meet that challenge, each having similar capabilities as well as some unique strengths. However, the earth system…

### doi:10.1080/09544828.2026.2624356
**Large language model agent as a mechanical designer** (2026) — Journal of Engineering Design · cites 9 · score 12 (strong 2) · core/solver_control · doi:10.1080/09544828.2026.2624356
signals: \bLLM[- ]?agents?\b;language model agents?;language model agents?*
touchpoints: results_interpretation
Traditional mechanical design relies on iterative refinement cycles driven by expert heuristics and computationally expensive Finite Element Method (FEM) analyses to meet performance targets. While machine learning approaches have been developed to automate portions of this process, they typically demand large datasets, substantial computational resources, and remain narrowly tailored to specific domains, thereby limiting their…

### title:utilizingmodelcontextprotocolandaimodelstoenhanceorganizationsdigitaltwininfrastructures
**Utilizing Model Context Protocol And Ai Models To Enhance Organizations Digital Twin Infrastructures** (2026) — Jönköping University Publications (Jönköping University) · cites 0 · score 12 (strong 3) · core/simulation_orchestration · http://urn.kb.se/resolve?urn=urn:nbn:se:hj:diva-72873
signals: \bAI agents?\b;\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);model context protocol;model context protocol*
touchpoints: tool_exposure
The rapid digital transformation of modern organizations has increased the need to integrate physical operational environments with data-driven Artificial Intelligence (AI) systems. Digital twin platforms provide structured virtual representations of physical assets and their relationships, enabling contex- tualized access to data from buildings, infrastructure and technical systems. Despite their potential, integrating AI systems with digital…

### doi:10.48550/arxiv.2604.27753
**Autonomous Traffic Signal Optimization Using Digital Twin and Agentic AI for Real-Time Decision-Making** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 3) · core/simulation_orchestration · doi:10.48550/arxiv.2604.27753
signals: \bLangChain\b;agentic;agentic*;model context protocol
touchpoints: tool_exposure
This article outlines a new framework of traffic light optimization through a digital twin of the transport infrastructure, managed by agentic AI to ensure real-time autonomous decisions. The framework relies on physical sensors and edge computing to measure real-time traffic information and simulate traffic flow in a constantly updated digital twin. The traffic light is…

### doi:10.48550/arxiv.2412.17146
**LLM Agent for Fire Dynamics Simulations** (2024) — arXiv (Cornell University) · cites 0 · score 12 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2412.17146
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: hpc_scale_out
Significant advances have been achieved in leveraging foundation models, such as large language models (LLMs), to accelerate complex scientific workflows. In this work we introduce FoamPilot, a proof-of-concept LLM agent designed to enhance the usability of FireFOAM, a specialized solver for fire dynamics and fire suppression simulations built using OpenFOAM, a popular open-source toolbox for…

### arxiv:2607.01812
**TO-Master: an LLM-agent framework for automated topology optimization** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · core/solver_control · doi:10.48550/arxiv.2607.01812
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*;agent orchestration
touchpoints: topology_construction
Topology optimization (TO) has become a mature computational design method, but using it still requires substantial manual effort in geometry preparation, mesh generation, boundary-condition assignment, solver setup, and postprocessing. This implementation barrier limits the use of TO outside expert workflows, even when differentiable finite element solvers are available. This work introduces TO-Master, a large language…

### doi:10.3389/fcpxs.2026.1800335
**Kiso: a foundation for complex, agentic, and reproducible experiments** (2026) — Frontiers in Complex Systems · cites 0 · score 12 (strong 3) · core/scientific_computing · doi:10.3389/fcpxs.2026.1800335
signals: \bAI agents?\b;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility
Experimentation on distributed, heterogeneous computing environments—from edge devices to large-scale cloud platforms—demands orchestration technologies that are both flexible and extensible. Kiso is an open-source framework designed to provision resources and manage complex scientific workflows across the edge-to-cloud continuum. Its architecture unifies infrastructure provisioning, experiment configuration, and reproducible execution, enabling researchers to compose and monitor experiments…

### doi:10.5281/zenodo.20449354
**Genetic Finance and Autonomous AI Agents: Transforming FinTech-Driven Financial Services through Intelligent Computing Systems** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 12 (strong 3) · core/optimisation_uq · doi:10.5281/zenodo.20449354
signals: \bAI agents?\b;\bAI agents?\b*;agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: optimisation_loop
Genetic Finance and Autonomous AI Agents: Transforming FinTech-Driven Financial Services through Intelligent Computing Systems Editors: Dr. Preeti Chawla Associate Professor Department of Management IBMR Business School, Gurugram, Haryana Dr. Pooja Gupta Associate Professor Department of Business Studies Panipat Institute of Engineering & Technology (PIET) Samalkha (Panipat), India Preface The financial sector is undergoing a revolutionary…

### doi:10.1063/5.0257555
**OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics** (2025) — Physics of Fluids · cites 43 · score 12 (strong 1) · core/solver_control · doi:10.1063/5.0257555
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
This work presents a large language model (LLM)-based agent OpenFOAMGPT tailored for OpenFOAM-centric computational fluid dynamics (CFD) simulations, leveraging two foundation models from OpenAI: the GPT-4o (GPT means Generative Pre-trained Transformer) and a chain-of-thought–enabled o1 preview model. Both agents demonstrate success across multiple tasks. While the price of token with o1 model is six times…

### doi:10.18653/v1/2025.findings-naacl.420
**Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents** (2025) — arXiv (Cornell University) · cites 8 · score 12 (strong 2) · core/computational_discovery · doi:10.18653/v1/2025.findings-naacl.420
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
Materials discovery and design are essential for advancing technology across various industries by enabling the development of applicationspecific materials.Recent research has leveraged Large Language Models (LLMs) to accelerate this process.We explore the potential of LLMs to generate viable hypotheses that, once validated, can expedite materials discovery.Collaborating with materials science experts, we curated a novel dataset…

### doi:10.1038/s43246-025-00994-x
**Modular large language model agents for multi-task computational materials science** (2026) — Communications Materials · cites 5 · score 12 (strong 2) · core/computational_discovery · doi:10.1038/s43246-025-00994-x
signals: language model agents?;language model agents?*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The integration of large language models (LLMs) with domain-specific computational tools provides a pathway to streamline and enhance materials science workflows. This paper introduces MatSciAgent, a multi-agent framework supporting tasks such as materials data retrieval, continuum simulation, crystal structure generation, and molecular dynamics simulation. At its core is a master agent that interprets user queries,…

### doi:10.1002/aic.70488
**Context is all you need: Toward autonomous model‐based process design using agentic AI in flowsheet simulations** (2026) — AIChE Journal · cites 1 · score 12 (strong 2) · core/simulation_orchestration · doi:10.1002/aic.70488
signals: \bcopilots?\b;agentic;agentic*
touchpoints: none
Abstract Agentic AI systems integrating large language models (LLMs) with reasoning and tool‐use capabilities are transforming software development, yet their application in chemical process flowsheet modeling remains largely unexplored. We present an agentic AI framework that provides assistance in an industrial flowsheet simulation environment. We show that GitHub Copilot (GitHub, Inc., 2026), using state‐of‐the‐art LLMs…

### doi:10.48550/arxiv.2602.04850
**El Agente Quntur: A research collaborator agent for quantum chemistry** (2026) — arXiv (Cornell University) · cites 1 · score 12 (strong 4) · core/computational_discovery · doi:10.48550/arxiv.2602.04850
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;agentic;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pi
touchpoints: none
Quantum chemistry is a foundational enabling tool for the fields of chemistry, materials science, computational biology and others. Despite of its power, the practical application of quantum chemistry simulations remains in the hands of qualified experts due to methodological complexity, software heterogeneity, and the need for informed interpretation of results. To bridge the accessibility gap…

### arxiv:2604.18233
**Aether: Network Validation Using Agentic AI and Digital Twin** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 3) · core/simulation_orchestration · doi:10.48550/arxiv.2604.18233
signals: \bAI agents?\b;agentic;agentic*;orchestrat\w+ agents?
touchpoints: none
Network change validation remains a critical yet predominantly manual, time-consuming, and error-prone process in modern network operations. While formal network verification has made substantial progress in proving correctness properties, it is typically applied in offline, pre-deployment settings and faces challenges in accommodating continuous changes and validating live production behavior. Current operational approaches typically involve scattered…

### doi:10.48550/arxiv.2506.03543
**CogniPair: From LLM Chatbots to Conscious AI Agents -- GNWT-Based Multi-Agent Digital Twins for Social Pairing -- Dating & Hiring Applications** (2025) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · core/simulation_orchestration · doi:10.48550/arxiv.2506.03543
signals: \bAI agents?\b;\bAI agents?\b*;\bLLM[- ]?agents?\b
touchpoints: none
Current large language model (LLM) agents lack authentic human psychological processes necessary for genuine digital twins and social AI applications. To address this limitation, we present a computational implementation of Global Workspace Theory (GNWT) that integrates human cognitive architecture principles into LLM agents, creating specialized sub-agents for emotion, memory, social norms, planning, and goal-tracking coordinated…

### title:mechanicaldesignusingmultiphysicsagenticaivolume4advancedaiintegrationsinenergysystemstoolcouplingrloptimizationrealengi
**Mechanical design using multiphysics & Agentic AI - Volume 4: Advanced AI integrations in energy systems. tool coupling, RL Optimization & Real Engineering applications** (2026) — Research Portal (Queen's University Belfast) · cites 0 · score 12 (strong 3) · core/simulation_orchestration · https://pure.qub.ac.uk/en/publications/6e606b51-bc60-49a9-8d40-eb53026728c3
signals: \bAI agents?\b;\bAutoGen\b;agentic;agentic*
touchpoints: none
This volume takes Agentic AI and Reinforcement Learning to the next level by applying them to real-world energy systems, with a strong focus on Bismuth Tin-inspired downhole tools and Zimmerman’s multiphysics modeling. You will master advanced tool coupling between Agentic AI agents and the full open-source multiphysics toolchain (Gmsh, Elmer, Fortran subroutines). Using the same…

### doi:10.1109/ojcoms.2026.3724461
**AoI-Aware Agentic Federated Mixture-of-Digital-Twin Experts for 6G Vehicular Edge Intelligence** (2026) — IEEE Open Journal of the Communications Society · cites 0 · score 12 (strong 3) · core/simulation_orchestration · doi:10.1109/ojcoms.2026.3724461
signals: agent orchestration;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Digital twin-enabled vehicular edge intelligence is expected to become a fundamental service paradigm for sixth-generation (6G) intelligent transportation systems. However, the performance of such systems depends not only on model accuracy, but also on the freshness of digital twin states, timeliness of inference, privacy-preserving model training, and efficient use of heterogeneous edge resources. Existing DT-assisted…

### doi:10.1039/d6dd00060f
**Text-to-flowsheet: an LLM-assisted pipeline for expert-level digitization and automated simulation of chemical processes** (2026) — Digital Discovery · cites 0 · score 12 (strong 2) · core/simulation_orchestration · doi:10.1039/d6dd00060f
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Converting unstructured natural language descriptions into structured process flowsheets is a fundamental bottleneck in chemical engineering, traditionally requiring years of expert training. While large language models (LLMs) show promise in text comprehension, their ability to match human expertise in modeling complex chemical process flowsheets remains unproven. Here, we present a rigorous benchmark comparing a fully…

### doi:10.2139/ssrn.6074109
**SwarmFoam: An OpenFOAM Multi-Agent System Based on Multiple Types of Large Language Models** (2026) — SSRN Electronic Journal · cites 0 · score 12 (strong 2) · core/solver_control · doi:10.2139/ssrn.6074109
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|archite
touchpoints: none
Numerical simulation is one of the mainstream methods in scientific research, typically performed by professional engineers. With the advancement of multi-agent technology, using collaborating agents to replicate human behavior shows immense potential for intelligent Computational Fluid Dynamics (CFD) simulations. Some muti-agent systems based on Large Language Models have been proposed. However, they exhibit significant limitations…

### arxiv:2607.05134
**PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · core/simulation_general · doi:10.48550/arxiv.2607.05134
signals: agentic;agentic*;autonomous agents?;autonomous agents?*
touchpoints: none
We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines. The workflow links problem specification, data generation, operator training, and checkpoint-based inference. A stateful input graph converts multi-turn natural-language input and user edits into validated problem specifications. The data-generation module then samples parameters, solves the configured governing-equation…

### arxiv:2605.14154
**TSAgent: An Agentic Workflow for Autonomous Transition State Search** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2605.14154
signals: agent(?:ic)? workflows?;agent(?:ic)? workflows?*;agentic;agentic*
touchpoints: none
Identifying transition states (TSs) on potential energy surfaces is a central computational bottleneck in mechanistic studies of catalytic materials. A TS search is not a single calculation but a long-horizon, multi-step workflow of atomistic simulations with delayed, asynchronous feedback and heterogeneous failure modes that require a joint multimodal analysis of scalar convergence diagnostics and atomic…

### doi:10.20944/preprints202605.2011.v1
**The Evolving Blueprint: A Survey on Automated Optimization of LLM-Based Multi-Agent Systems** (2026) — Preprints.org · cites 0 · score 12 (strong 2) · core/simulation_general · doi:10.20944/preprints202605.2011.v1
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
The rapid rise of Large Language Model (LLM) agents is driving a fundamental paradigm shift in Multi-Agent Systems (MAS) research, moving from manually orchestrated static architectures toward automated configuration and optimization. Despite its significant potential, this frontier lacks a systematic and rigorous survey with clearly defined operational boundaries. To address this gap, this paper provides…

### doi:10.5194/egusphere-egu25-16905
**An AI-Copilot for JupyterLab for climate data analyses using FrevaGPT** (2025) — n/a · cites 0 · score 11 (strong 1) · core/scientific_computing · doi:10.5194/egusphere-egu25-16905
signals: \bcopilots?\b;\bcopilots?\b*
touchpoints: hpc_scale_out;provenance_reproducibility;results_interpretation
JupyterLab is a web-based interactive development platform that is widely used in the Earth science community. Using Jupyter Notebooks, it is possible to perform data analysis tasks, annotate and visualize results in a way that is easy to reproduce, present and share with others. JupyterLab allows the use of “extensions”, which add functionality to the…

### doi:10.48550/arxiv.2511.00122
**Engineering.ai: A Platform for Teams of AI Engineers in Computational Design** (2025) — arXiv (Cornell University) · cites 0 · score 11 (strong 3) · core/solver_control · doi:10.48550/arxiv.2511.00122
signals: agentic;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility;solver_control
In modern engineering practice, human engineers collaborate in specialized teams to design complex products, with each expert completing their respective tasks while communicating and exchanging results and data with one another. While this division of expertise is essential for managing multidisciplinary complexity, it demands substantial development time and cost. Recently, we introduced OpenFOAMGPT (1.0, 2.0),…

### doi:10.5281/zenodo.21854862
**AOBench: a role-aware, RBAC-enforced benchmark for LLM agents in HPC operations** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 11 (strong 2) · core/scientific_computing · doi:10.5281/zenodo.21854862
signals: \bAI agents?\b;\bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: hpc_scale_out;provenance_reproducibility
AOBench (Agent Operations Benchmark) is an open-source Python benchmark framework for evaluating AI agents that operate High-Performance Computing (HPC) systems. It measures whether an agent completes HPC operational tasks — job scheduling, telemetry interpretation, energy reasoning, and policy enforcement — using the right tools, the right roles, and the right permissions. The corpus is 88…

### doi:10.48550/arxiv.2507.14267
**DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation** (2025) — arXiv (Cornell University) · cites 10 · score 11 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2507.14267
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility
Large language model (LLM) agents can execute long-horizon scientific workflows, but their numerical outputs are difficult to trust: agents lose context, game verification checks, and can produce large volumes of plausible yet invalid results. We introduce the DFT-based Research Engine for Agentic Materials Simulation (DREAMS), a hierarchical multi-agent framework for density functional theory (DFT) built…

### doi:10.1063/5.0294696
**CFDAgent: A language-guided, zero-shot multi-agent system for complex flow simulation** (2025) — 中国科学院力学研究所 · cites 7 · score 11 (strong 2) · core/solver_control · doi:10.1063/5.0294696
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: results_interpretation
We introduce CFDAgent, a zero-shot, language-guided multi-agent framework that enables fully autonomous computational fluid dynamics (CFD) simulations from natural language prompts. CFDAgent integrates three specialized large language model driven agents: (i) the Preprocessing Agent generates Lagrangian surface meshes from inputs including natural language descriptions, two-dimensional images, or three-dimensional geometry; (ii) the Solver Agent configures and…

### doi:10.1145/3731599.3767401
**Agentic AI vs ML-based Autotuning: A Comparative Study for Loop Reordering Optimization** (2025) — n/a · cites 4 · score 11 (strong 1) · core/scientific_computing · doi:10.1145/3731599.3767401
signals: agentic;agentic*
touchpoints: hpc_scale_out
High Performance Computing (HPC) applications rely heavily on code optimizations to achieve good performance on modern CPU and GPU architectures. Traditional Machine Learning autotuning approaches have demonstrated success in exploring high-dimensional spaces, but they often require expensive compile-run evaluations and lack adaptability for large HPC applications. The recent advances in Large Language Models (LLMs) and…

### doi:10.5281/zenodo.22230054
**Evolving the RSE role in the age of generative and agentic AI** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 11 (strong 2) · core/scientific_computing · doi:10.5281/zenodo.22230054
signals: agent(?:ic)? workflows?;agentic;agentic*
touchpoints: provenance_reproducibility
Generative AI and agentic tools (GenAI) are dramatically changing research software practice. Researchers can now generate their research code more easily with less programming and software engineering experience. Anecdotal evidence suggests that researchers’ collaborations with RSEs now focus on more complex or higher-level software engineering tasks such as code review.These changes bring uncertainty: Will the…

### arxiv:2605.23273
**Self-Refining Topology Optimization via an LLM-Based Multi-Agent Framework** (2026) — arXiv · cites 0 · score 11 (strong 2) · core/simulation_general · arXiv:2605.23273
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: topology_construction
Topology optimization is a widely used design method that produces optimized material distributions for prescribed objectives and constraints through well-established numerical algorithms. Throughout the workflow, engineers make a series of decisions ranging from setting and adjusting numerical parameters to assessing whether the converged design meets considerations beyond those explicitly included in the optimization problem, such…

### doi:10.1109/access.2024.3415470
**Generation of Asset Administration Shell With Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0** (2024) — IEEE Access · cites 84 · score 11 (strong 1) · core/simulation_orchestration · doi:10.1109/access.2024.3415470
signals: language model agents?;language model agents?*
touchpoints: none
This research introduces a novel approach for achieving semantic interoperability in digital twins and assisting the creation of Asset Administration Shell (AAS) as digital twin model within the context of Industry 4.0. The foundational idea of our research is that the communication based on semantics and the generation of meaningful textual data are directly linked,…

### doi:10.48550/arxiv.2512.06404
**GENIUS: An Agentic AI Framework for Autonomous Design and Execution of Simulation Protocols** (2025) — arXiv (Cornell University) · cites 2 · score 11 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2512.06404
signals: agent(?:ic)? workflows?;agentic;agentic*
touchpoints: none
Predictive atomistic simulations have propelled materials discovery, yet routine setup and debugging still demand computer specialists. This know-how gap limits Integrated Computational Materials Engineering (ICME), where state-of-the-art codes exist but remain cumbersome for non-experts. We address this bottleneck with GENIUS, an AI-agentic workflow that fuses a smart Quantum ESPRESSO knowledge graph with a tiered hierarchy…

### doi:10.48550/arxiv.2504.08846
**AI University: An LLM-Powered Learning Assistant for Engineering---A Finite Element Method Case Study** (2025) — arXiv (Cornell University) · cites 1 · score 11 (strong 1) · core/solver_control · doi:10.48550/arxiv.2504.08846
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
We introduce AI University (AI-U), a flexible framework for AI-driven course content delivery that adapts to a course's instructional style. AI-U combines a fine-tuned large language model (LLM) with retrieval-augmented generation (RAG) and a reasoning synthesis model to generate style-aligned responses from lecture videos, notes, and textbooks. Using a graduate-level finite-element-method (FEM) course as a…

### doi:10.48550/arxiv.2512.13930
**Hierarchical Multi-agent Large Language Model Reasoning for Autonomous Functional Materials Discovery** (2025) — arXiv (Cornell University) · cites 1 · score 11 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2512.13930
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Artificial intelligence is reshaping scientific exploration, but most methods automate procedural tasks without engaging in scientific reasoning, limiting autonomy in discovery. We introduce Materials Agents for Simulation and Theory in Electronic-structure Reasoning (MASTER), an active learning framework where large language models autonomously design, execute, and interpret atomistic simulations. In MASTER, a multimodal system translates natural…

### doi:10.65713/ijaraiv13i1210
**THE FUTURE OF PRECISION ONCOLOGY: CONVERGING FOUNDATION MODELS, AGENTIC AI, DIGITAL TWINS, AND MULTIMODAL CLINICAL INTELLIGENCE** (2023) — International Journal of Advanced Research and Innovations · cites 0 · score 11 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv13i1210
signals: agentic;agentic*
touchpoints: none
Precision oncology is entering a transformative era driven by the convergence of foundation artificial intelligence (AI) models, agentic AI, digital twins, multimodal clinical intelligence, and continuously learning healthcare ecosystems. Traditional precision oncology has significantly improved diagnosis and treatment by incorporating molecular profiling and targeted therapies; however, fragmented biomedical data, limited interoperability, delayed clinical decision-making, and…

### doi:10.2196/preprints.87374
**Building Personalized Digital Twins from Public Health Data: An Agentic AI and Ontology-Guided Framework for Diabetes Progression Simulation and Risk Prediction (Preprint)** (2025) — n/a · cites 0 · score 11 (strong 2) · core/simulation_orchestration · doi:10.2196/preprints.87374
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
BACKGROUND Digital twins (DTs) offer a transformative paradigm for healthcare by creating dynamic, individualized models that simulate disease trajectories and support personalized interventions. However, DT development remains limited by the scarcity of standardized, temporally structured, and multidomain data suitable for modeling chronic disease progression. Most existing DT studies rely on narrowly scoped or proprietary datasets,…

### doi:10.48175/ijarsct-11962a
**EMDIF: An Explainable Multi-Agent Intelligence Framework for Cross-Domain Analytics** (2026) — International Journal of Advanced Research in Science Communication and Technology · cites 0 · score 11 (strong 2) · core/simulation_general · doi:10.48175/ijarsct-11962a
signals: \bAI agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
To address the challenges of limited decision transparency, insufficient reasoning interpretability, and weak cross-domain collaboration in AI-driven simulation and analytics systems, this paper proposes an Explainable Multi-Agent Intelligence Framework (EMAIF) for intelligent simulation-driven decision support across retail, finance, and networking domains. The proposed framework integrates specialized AI agents with a centralized orchestration layer to coordinate…

### arxiv:2603.23884
**POSIM: A Multi-Agent Simulation Framework for Social Media Public Opinion Evolution and Governance** (2026) — arXiv · cites 0 · score 11 (strong 2) · core/simulation_general · arXiv:2603.23884
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: none
Modeling social media public opinion evolution is essential for governance decision-making. Traditional epidemic models and rule-based agent-based models (ABMs) fail to capture the cognitive processes and adaptive behaviors of real users. Recent large language model (LLM)-based social simulations can reproduce group-level phenomena like polarization and conformity, yet remain unable to recreate the irrational interactions and…

### doi:10.48550/arxiv.2605.24002
**Harnessing AtomisticSkills for Agentic Atomistic Research** (2026) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2605.24002
signals: AI scientist;agentic;agentic*
touchpoints: none
Computational materials science and chemistry span vast knowledge domains and fractured software ecosystems. Although large language models (LLMs) have demonstrated research capabilities, scaling monolithic agents to manage the rigor and complexity of atomistic research remains a challenge. Here, we introduce AtomisticSkills, an open-source harness framework that empowers general-purpose AI coding agents to conduct atomistic research…

### arxiv:2605.26179
**AutoDFT: A Closed-Loop Multi-Agent Framework for Autonomous DFT Calculations** (2026) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2605.26179
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: none
Density functional theory (DFT) serves as the basis for computational discovery in materials science and chemistry, yet each calculation demands extensive human effort: adjusting algorithms when convergence stalls, revising plans when unexpected physics emerges, and inserting steps as intermediate results reshape the problem. Existing LLM-based agents automate only the initial planning stage, producing a full…

### arxiv:2607.19822
**WARA: A Closed-Loop Multi-Agent Framework for Wireless Optimization Autoresearch** (2026) — arXiv · cites 0 · score 11 (strong 2) · core/simulation_general · arXiv:2607.19822
signals: \btool[- ]use\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Large language model (LLM) agents have shown growing capabilities in tool use, code execution, artifact inspection, and iterative revision, creating new opportunities for automating scientific research. To the best of our knowledge, this paper presents the first end-to-end autoresearch framework for the wireless domain, with a particular focus on wireless resource allocation optimization, an essential…

### doi:10.5281/zenodo.21841883
**Artifact for "Works but Wrong: Static Diagnosis of HPC Simulation Setup Errors for AI Agents"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 2) · core/scientific_computing · doi:10.5281/zenodo.21841883
signals: \bAI agents?\b;\bAI agents?\b*;agentic
touchpoints: config_generation;hpc_scale_out;provenance_reproducibility
Artifact accompanying the AgenticAI4HPC'26 (SC26 workshop) paper "Works but Wrong: Static Diagnosis of HPC Simulation Setup Errors for AI Agents". A scientific simulation may complete successfully on an HPC system yet still produce incorrect results, usually because of a mistake in the setup files rather than a bug in the solver. This artifact accompanies a…

### doi:10.48550/arxiv.2509.10210
**Towards Fully Automated Molecular Simulations: Multi-Agent Framework for Simulation Setup and Force Field Extraction** (2025) — arXiv (Cornell University) · cites 1 · score 10 (strong 2) · core/simulation_orchestration · doi:10.48550/arxiv.2509.10210
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: provenance_reproducibility
Automated characterization of porous materials has the potential to accelerate materials discovery, but it remains limited by the complexity of simulation setup and force field selection. We propose a multi-agent framework in which LLM-based agents can autonomously understand a characterization task, plan appropriate simulations, assemble relevant force fields, execute them and interpret their results to…

### doi:10.1109/ipdps65963.2026.00114
**Empowering Scientific Workflows with Federated Agents** (2026) — arXiv · cites 0 · score 10 (strong 3) · core/scientific_computing · doi:10.1109/ipdps65963.2026.00114
signals: agent(?:ic)? workflows?;agentic;autonomous agents?
touchpoints: hpc_scale_out
Agentic systems, in which diverse agents cooperate to tackle challenging problems, are exploding in popularity in the AI community. However, existing agentic frameworks take a relatively narrow view of agents, apply a centralized model, and target conversational, cloud-native applications (e.g., LLM-based AI chatbots). In contrast, scientific applications require myriad agents be deployed and managed across…

### doi:10.20944/preprints202607.0644.v1
**Recent Progress, Challenges, and Future Perspectives in AI-Driven Discovery and Optimization of Advanced Materials** (2026) — Preprints.org · cites 0 · score 10 (strong 2) · core/computational_discovery · doi:10.20944/preprints202607.0644.v1
signals: autonomous experimentation;self[- ]driving lab
touchpoints: optimisation_loop
The rapid transition toward sustainable energy systems has created an urgent demand for advanced functional materials capable of improving energy conversion, storage, and utilization technologies. Artificial intelligence has emerged as a key enabling technology for accelerating materials discovery through data-driven prediction, inverse design, autonomous experimentation, and intelligent decision-making. This mini-review critically examines recent advances in…

### doi:10.1109/mipro60963.2024.10569919
**Enhancing Cognitive Digital Twin Interaction using an LLM Agent** (2024) — n/a · cites 18 · score 10 (strong 1) · core/simulation_orchestration · doi:10.1109/mipro60963.2024.10569919
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
This paper introduces a conceptual architecture design aimed at enhancing interactions with cognitive digital twins of countries through an Large Language Model (LLM) agent. By leveraging sophisticated data retrieval and summarization techniques, the architecture integrates data from diverse sources, including environmental sensors, web pages, and human inputs, to create a dynamic and comprehensive digital twin.…

### doi:10.1016/j.array.2026.100721
**Integrating agentic AI and digital twins for intelligent decision-making systems** (2026) — Array · cites 10 · score 10 (strong 2) · core/simulation_orchestration · doi:10.1016/j.array.2026.100721
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*
touchpoints: none
The integration of agentic artificial intelligence (agentic AI) and digital twins (DTs) enables decision-making systems that are intelligent, adaptive, and goal-oriented. This paper advances that convergence through a multilayer integration framework that organizes perception, knowledge and data management, LLM-based reasoning, learning, decision-making, action execution, and feedback adaptation into a cohesive structure. Within this framework, LLM-driven…

### doi:10.67294/knpyhb26
**Conceptualizing Cognitive and Agentic Digital Twins** (2026) — International Multidisciplinary Journal of Emerging Technologies and Applications · cites 1 · score 10 (strong 2) · core/simulation_orchestration · doi:10.67294/knpyhb26
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*
touchpoints: none
Digital Twins (DTs) have extended beyond the original concept of a static digital model, to a dynamic, data-driven, and increasingly intelligent cyber-physical structure, which underlies modern Industry 4.0 systems. The paper gives a comprehensive and integrative conceptualization of DTs, Cognitive Digital Twins (CDTs), and agentic AI-enhanced DTs through an organized narrative literature review which synthesizes…

### doi:10.48550/arxiv.2608.15881
**Deploying Frontier Agentic Technology in MOOSEnger, a Multiphysics-Capable AI Assistant** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · core/simulation_orchestration · doi:10.48550/arxiv.2608.15881
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
The Multiphysics Object-Oriented Simulation Environment (MOOSE) is an open-source finite-element framework for building multiphysics simulation applications. Using a multiphysics environment effectively demands specialized expertise, creating a barrier for many domain scientists and engineers. MOOSEnger, developed at Idaho National Laboratory (INL), is a domain-specific, tool-enabled AI agent built for the MOOSE Framework. This work extends MOOSEnger…

### doi:10.48550/arxiv.2608.00937
**Neuro-Symbolic Participation Governance for Verifiable AI Agents in Open Digital Twin Ecosystems** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · core/simulation_orchestration · doi:10.48550/arxiv.2608.00937
signals: \bAI agents?\b;\bAI agents?\b*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Autonomous AI agents, increasingly empowered by large language models, are becoming important components of human-machine systems for high-stakes decision support in digital twin ecosystems. However, existing multi-agent systems often lack robust verification for identity, capability, and policy compliance, especially in decentralized environments spanning multiple institutions. This paper proposes a neuro-symbolic decentralized governance framework for verifiable…

### doi:10.1109/cai68641.2026.11536542
**V2X enhanced Digital Twin for public bus priority. Towards Agentic-enabled Transport Systems** (2026) — n/a · cites 0 · score 10 (strong 2) · core/simulation_orchestration · doi:10.1109/cai68641.2026.11536542
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
This paper presents a vision-oriented systems contribution that advances the integration of V2X-standardized data, distributed Digital Twin (DT) architectures, and emerging Agentic AI concepts to enhance public Transport Signal Priority (TSP) in urban mobility environments. We propose a V2X-first Transportation Digital Twin architecture deployed across the cloud–edge continuum, enabling real-time synchronization between physical infrastructure, predictive…

### doi:10.48550/arxiv.2609.00795
**Agentic programs: an emerging form of scientific software in computational materials science** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · core/scientific_computing · doi:10.48550/arxiv.2609.00795
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*
touchpoints: none
Computational materials science has traditionally delegated algorithmic tasks to computers while leaving scientific judgments to humans. We argue that recent LLM-based agent harnesses enable an emerging form of scientific software, agentic programs, that combine deterministic algorithms with bounded LLM-based judgment, task-specific verification, episodic maturation, and complete delegation in production. We illustrate this concept with DeMARS,…

### doi:10.26434/chemrxiv.15002405/v1
**Q-planner: a harness system for quantum chemistry agents** (2026) — ChemRxiv · cites 0 · score 10 (strong 3) · core/computational_discovery · doi:10.26434/chemrxiv.15002405/v1
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLangGraph\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework
touchpoints: none
LLM-based agents for computational chemistry commonly place the model inside an accumulating execution loop, causing context growth proportional to workflow length, unpredictable token costs, and degraded plan reliability at scale. We present a chemistry computation harness that confines LLM invocations to three semantically bounded stages—compound identification, planning, and reporting—while delegating all tool dispatch, parallel scheduling,…

### doi:10.2118/232332-ms
**Agentic AI-Driven Geothermal Reservoir Simulation and Optimization Using Surrogate Modelling for Rapid Site Screening** (2026) — n/a · cites 0 · score 9 (strong 2) · core/geoenergy_subsurface · doi:10.2118/232332-ms
signals: \bAI agents?\b;agentic;agentic*
touchpoints: optimisation_loop;surrogate_modelling;techno_economic;uncertainty_quantification
Abstract Geothermal energy is a prime key contributor to the global transition toward low-emission and sustainable energy systems. As a reliable baseload renewable resource with minimal greenhouse gas emissions, geothermal power generation offers continuous or uninterrupted energy supply. Thus, accurate prediction of subsurface temperature evolution is therefore fundamental to geothermal reservoir engineering, as temperature directly…

### doi:10.1109/sci68648.2025.11333875
**CoMAS-HPC: A Collaborative Multi-Agent System for HPC Administration** (2025) — n/a · cites 0 · score 9 (strong 2) · core/scientific_computing · doi:10.1109/sci68648.2025.11333875
signals: model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: hpc_scale_out;provenance_reproducibility;tool_exposure
The administration of modern High-Performance Computing (HPC) systems is increasingly complex, with growing scale, heterogeneous resources, and massive telemetry streams overwhelming human operators. Traditional single-agent or monolithic approaches struggle to cope with this complexity, resulting in reactive problem-solving and limited scalability. To address these challenges, we propose CoMAS-HPC, a collaborative multi-agent system in which specialized…

### doi:10.3389/frma.2025.1595824
**Open science falling behind in the era of artificial intelligence** (2025) — Frontiers in Research Metrics and Analytics · cites 2 · score 9 (strong 1) · core/scientific_computing · doi:10.3389/frma.2025.1595824
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b
touchpoints: hpc_scale_out;provenance_reproducibility
Generative Artificial Intelligence (AI) refers to a new generation of content generation technologies that emerged after the rise of Transformer architecture in 2017, characterized by its core technical features of "compute-intensive architecture, model-driven paradigm, and data closed-loop system" (Table 1). AI is accelerating scientific discoveries and reshaping the research process, propelling AI for science towards…

### doi:10.1145/3770855.3818856
**Battery-Sim-Agent: Leveraging LLM-Agent for Inverse Battery Parameter Estimation** (2026) — arXiv (Cornell University) · cites 1 · score 9 (strong 1) · core/optimisation_uq · doi:10.1145/3770855.3818856
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: optimisation_loop;verification_regression
Parameterizing high-fidelity "digital twins" of batteries is a critical yet challenging inverse problem that hinders the pace of battery innovation. Prevailing methods formulate this as a black-box optimization (BBO) task, employing algorithms that are sample-inefficient and blind to the underlying physics. In this work, we introduce a new paradigm that reframes the inverse problem as…

### doi:10.48550/arxiv.2604.22571
**LARA: Validation-Driven Agentic Supercomputer Workflows for Atomistic Modeling** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2604.22571
signals: agentic;agentic*
touchpoints: hpc_scale_out;provenance_reproducibility
Large language models (LLMs) and agentic systems have recently demonstrated potential for automating scientific workflows, including atomistic simulations. However, their deployment in high-performance computing (HPC) environments remains limited by the lack of mechanisms ensuring correctness, reproducibility, and safe interaction with computational resources. Generated workflows suffer from inconsistencies, incorrect API usage, or invalid physical configurations -…

### doi:10.48550/arxiv.2604.11945
**AutoSurrogate: An LLM-Driven Multi-Agent Framework for Autonomous Construction of Deep Learning Surrogate Models in Subsurface Flow** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/geoenergy_subsurface · doi:10.48550/arxiv.2604.11945
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: surrogate_modelling;uncertainty_quantification
High-fidelity numerical simulation of subsurface flow is computationally intensive, especially for many-query tasks such as uncertainty quantification and data assimilation. Deep learning (DL) surrogates can significantly accelerate forward simulations, yet constructing them requires substantial machine learning (ML) expertise - from architecture design to hyperparameter tuning - that most domain scientists do not possess. Furthermore, the…

### arxiv:2605.00803
**Can Coding Agents Reproduce Findings in Computational Materials Science?** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · core/scientific_computing · doi:10.48550/arxiv.2605.00803
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic
touchpoints: provenance_reproducibility;results_interpretation
Large language models are increasingly deployed as autonomous coding agents and have achieved remarkably strong performance on software engineering benchmarks. However, it is unclear whether such success transfers to computational scientific workflows, where tasks require not only strong coding ability, but also the ability to navigate complex, domain-specific procedures and to interpret results in the…

### doi:10.1021/acs.chemrev.6c00154
**AI for Accelerated Materials Discovery: From Generative Design to Autonomous Realization** (2026) — Chemical Reviews · cites 0 · score 9 (strong 2) · core/computational_discovery · doi:10.1021/acs.chemrev.6c00154
signals: autonomous experimentation;self[- ]driving lab
touchpoints: provenance_reproducibility;topology_construction
Artificial intelligence (AI) is fundamentally transforming materials discovery, shifting the paradigm from labor-intensive trial-and-error approaches to data-driven, automated workflows. This review examines emerging AI methodologies for accelerated materials discovery, with particular emphasis on how computational design, data infrastructure, synthesis planning, and autonomous experimentation can be connected into experimentally grounded workflows. We begin by surveying generative…

### doi:10.48550/arxiv.2409.11363
**CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark** (2024) — arXiv (Cornell University) · cites 4 · score 9 (strong 3) · core/scientific_computing · doi:10.48550/arxiv.2409.11363
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\bAI agents?\b;\bAutoGPT\b
touchpoints: provenance_reproducibility
AI agents have the potential to aid users on a variety of consequential tasks, including conducting scientific research. To spur the development of useful agents, we need benchmarks that are challenging, but more crucially, directly correspond to real-world tasks of interest. This paper introduces such a benchmark, designed to measure the accuracy of AI agents…

### doi:10.20381/ruor-31909
**Emotion-Aware Digital Twin for a Large Language Model-Based Personalized Therapy Solution** (2026) — n/a · cites 0 · score 9 (strong 1) · core/simulation_orchestration · doi:10.20381/ruor-31909
signals: agentic
touchpoints: provenance_reproducibility
Mental health disorders are increasing worldwide, yet many individuals still face limited access to timely mental health support. At the same time, wearable devices such as smartwatches enable continuous collection of physiological signals that may provide useful indicators of affective states in everyday life. This thesis explores how wearable-based emotion recognition can be integrated with…

### doi:10.5281/zenodo.22145004
**The Scientific Method: A Domain-Agnostic Chain-of-Thought Protocol for Empirical Inquiry** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 9 (strong 2) · core/solver_control · doi:10.5281/zenodo.22145004
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\bAI agents?\b
touchpoints: provenance_reproducibility
⚡ TL;DR: This paper presents a universal, executable chain-of-thought protocol that standardizes the scientific method into seven logical steps, enabling AI agents and human researchers to conduct rigorous, falsifiable empirical inquiry across any domain. Abstract: This document presents a generic, executable chain-of-thought protocol for applying the scientific method to any quantifiable problem. It decouples the…

### arxiv:2607.18485
**Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2607.18485
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: hpc_scale_out
Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler. This arrangement creates…

### arxiv:2607.11084
**NVAITC AI Scientist: A Governed End-to-End Research System -- A Hypertension GWAS Case Study** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · core/scientific_computing · doi:10.48550/arxiv.2607.11084
signals: AI scientist;AI scientist*;agentic
touchpoints: provenance_reproducibility
Agentic research systems are emerging as a new paradigm for coordinating scientific workflows beyond isolated model inference, code generation, or statistical analysis. However, deployment in institutional biomedical environments requires governed mechanisms for research planning, data access, workflow orchestration, evidence tracking, reproducibility, and human oversight. We present NVAITC AI Scientist (NAIS), a governed end-to-end agentic research…

### title:atestbedframeworkforestimatingtheenvironmentalimpactofagenticaiworkflowsinhpc
**A Testbed Framework for Estimating the Environmental Impact of Agentic AI Workflows in HPC** (2026) — HAL (Le Centre pour la Communication Scientifique Directe) · cites 0 · score 9 (strong 2) · core/scientific_computing · https://hal.science/hal-05594455
signals: agent(?:ic)? workflows?;agentic;agentic*
touchpoints: hpc_scale_out
Agentic AI services heavily rely on High-Performance Computing (HPC) infrastructures and, despite the booming growth of such services and the underlying HPC infrastructure demand, little is known regarding methods to estimate their environmental impacts beyond carbon emissions. This paper proposes a novel methodology that leverages existing Life-Cycle Assessment (LCA) data to estimate the environmental impacts…

### doi:10.26434/chemrxiv.15007941/v1
**From Black Box to Dialogue: An MCP Server for Tanabe–Sugano Diagrams as a Reference Case for Conversational Scientific Tools** (2026) — ChemRxiv · cites 0 · score 9 (strong 2) · core/simulation_general · doi:10.26434/chemrxiv.15007941/v1
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool)*;model context protocol
touchpoints: tool_exposure
Interpreting the d–d electronic spectra of transition-metal complexes is a routine practice in inorganic chemistry, yet the underlying models behind such interpretations are unexpectedly challenging to operate. Rigorous treatments demand specialized software, expert parameterization, and often high-performance computing, while even the standard textbook tool for first-pass intuition takes practice to read. The Tanabe–Sugano (TS) diagram…

### arxiv:2604.02688
**MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2604.02688
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: hpc_scale_out
Existing LLM agents for computational materials science are constrained by pipeline-bounded architectures tied to specific simulation codes and by dependence on manually written tool functions that grow with task scope. We present MatClaw, a code-first agent that writes and executes Python directly, composing any installed domain library to orchestrate multi-code workflows on remote HPC clusters…

### doi:10.2139/ssrn.6942178
**Closed-Loop LLM-Guided Molecular Dynamics Screening of Thermal Transport in Co-Cr-Ni Medium-Entropy Alloys: A Proof-of-Concept Automated Materials Discovery Workflow** (2026) — SSRN Electronic Journal · cites 0 · score 9 (strong 1) · core/computational_discovery · doi:10.2139/ssrn.6942178
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b*
touchpoints: provenance_reproducibility
Thermal-transport property screening across the vast compositional space of medium-entropy alloys (MEAs) presents a persistent bottleneck: each candidate requires a manual cycle of composition selection, supercell construction, molecular dynamics (MD) equilibration, production, and data extraction before the next trial composition can be defined. This work reports a reproducible, closed-loop workflow that integrates a large language…

### doi:10.1002/csc3.70015
**From Screening to Generation: Reshaping the Paradigm of New Energy Materials Discovery With Artificial Intelligence** (2026) — cScience · cites 0 · score 9 (strong 2) · core/computational_discovery · doi:10.1002/csc3.70015
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic
touchpoints: optimisation_loop
Achieving global carbon neutrality requires a rapid transition toward a sustainable energy economy, a shift that fundamentally relies on the discovery of high-performance materials [1]. Central to this transition are modern energy systems requiring inorganic crystals with tailored properties, such as solid-state batteries for safe storage [2-4], perovskite solar cells for efficient power generation [5-7],…

### doi:10.1016/j.jmsy.2025.03.022
**IIoT-enabled digital twin for legacy and smart factory machines with LLM integration** (2025) — Journal of Manufacturing Systems · cites 44 · score 9 (strong 2) · core/simulation_orchestration · doi:10.1016/j.jmsy.2025.03.022
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Recent advancements in Large Language Models (LLMs) have significantly transformed the field of natural data interpretation, translation, and user training. However, a notable gap exists when LLMs are tasked to assist with real-time context-sensitive machine data. The paper presents a multi-agent LLM framework capable of accessing and interpreting real-time and historical data through an Industrial…

### doi:10.1007/s44212-025-00099-3
**Towards Agentic Urban Digital Twins (AUDiTs): advancing new urban science through Human-AI co-learning agents** (2026) — Urban Informatics · cites 3 · score 9 (strong 1) · core/simulation_orchestration · doi:10.1007/s44212-025-00099-3
signals: agentic;agentic*
touchpoints: none
Abstract While digital twins provide predictive and planning capabilities, they often underrepresent social complexity, ethical considerations, and stakeholder participation. Concurrently, advances in artificial intelligence offer new opportunities for real-time sensing, adaptive learning, and decision support; yet current applications remain narrowly focused on optimization or monitoring. This falls short of the broader mission of New Urban…

### doi:10.26434/chemrxiv.15001581/v1
**Text-to-Flowsheet: An Automated LLM-Pipeline for Digitization and Simulation of Chemical Processes with Expert-Level Accuracy** (2026) — ChemRxiv · cites 1 · score 9 (strong 2) · core/simulation_orchestration · doi:10.26434/chemrxiv.15001581/v1
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
Converting unstructured natural language descriptions into structured process flowsheets is a fundamental bottleneck in chemical engineering, traditionally requiring years of expert training. While large language models (LLMs) show promise in text comprehension, their ability to match human expertise in modeling complex chemical process flowsheets remains unproven. Here, we present a rigorous benchmark comparing a fully…

### doi:10.1145/3774748.3776593
**Designing Systems with Digital Twins and AI Agents** (2026) — n/a · cites 0 · score 9 (strong 2) · core/simulation_orchestration · doi:10.1145/3774748.3776593
signals: \bAI agents?\b;\bAI agents?\b*;autonomous agents?
touchpoints: none
With the increasing adoption of digital transformation across industries such as manufacturing, healthcare, and smart infrastructure, Digital Twin and AI Agent technologies are rapidly emerging as critical enablers of intelligent systems.Together, they offer the ability to create real-time virtual replicas of physical systems and augment them with autonomous, decision-making capabilities.This combination significantly enhances monitoring, predictive…

### doi:10.54941/ahfe1007674
**Agentic LLMs for Scalable, Verifiable System Health Digital Twins** (2026) — AHFE international · cites 0 · score 9 (strong 1) · core/simulation_orchestration · doi:10.54941/ahfe1007674
signals: agentic;agentic*
touchpoints: none
System Health Management (SHM) digital twins have evolved from specialized engineering tools into enterprise-wide critical systems supporting diagnostics and lifecycle decision support, yet scaling the creation, validation, and maintenance of detailed causal models remains a bottleneck due to labor-intensive, expert-driven processes that do not scale with system complexity or lifecycle evolution. This paper presents an…

### doi:10.48550/arxiv.2608.11679
**AgenticTwin: An Agentic LLM Framework Integrated with Digital Twin for Anomaly Detection** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2608.11679
signals: agentic;agentic*
touchpoints: none
Digital twins are increasingly used to monitor and simulate the behavior of cyber-physical systems. Even with skilled operators, interpreting anomalies detected within digital twin pipelines is challenging, as the sheer complexity and volume of raw sensor data make thorough analysis difficult. Recent advances in large language models (LLMs) offer promising capabilities for reasoning and explanation,…

### doi:10.1109/tii.2026.3669495
**ModSolAgent: Automated Finite Element Code Generation for Abaqus via LLM-Based Agent** (2026) — IEEE Transactions on Industrial Informatics · cites 0 · score 9 (strong 1) · core/solver_control · doi:10.1109/tii.2026.3669495
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Finite element simulation and solution process represents a critical component in engineering analysis. While large language models (LLMs) have demonstrated remarkable capabilities in general-purpose code generation from textual descriptions, their application to generating structured and specialized finite element simulation scripts presents unique challenges. A key challenge is AI-generated hallucination, as these tasks require precise intent…

### doi:10.48550/arxiv.2512.09209
**Beyond Algorithm Evolution: An LLM-Driven Framework for the Co-Evolution of Swarm Intelligence Optimization Algorithms and Prompts** (2025) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · core/simulation_general · doi:10.48550/arxiv.2512.09209
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The field of automated algorithm design has been advanced by frameworks such as EoH, FunSearch, and Reevo. Yet, their focus on algorithm evolution alone, neglecting the prompts that guide them, limits their effectiveness with LLMs, especially in complex, uncertain environments where they nonetheless implicitly rely on strategies from swarm intelligence optimization algorithms. Recognizing this, we…

### doi:10.36227/techrxiv.175979241.11582889/v1
**Explainability as a Catalyst for Agentic AI Adoption in Subsurface Oil & Gas Workflows** (2025) — n/a · cites 0 · score 9 (strong 2) · core/geoenergy_subsurface · doi:10.36227/techrxiv.175979241.11582889/v1
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Keywords Agentic AI; explainable AI; subsurface workflows; well test interpretation; reservoir engineering; human-in-the-loop 1.1 Background/Purpose Artificial intelligence (AI) has been widely adopted in surface-level oil and gas operations such as predictive maintenance and drilling optimization. However, subsurface workflows including well test interpretation, reservoir modeling, and production forecasting remain highly dependent on expert judgment. A major…

### doi:10.2523/iptc-25245-ms
**Agentic AI Framework for Technical Excellence: A Discipline-Based, Scalable Multimodal Assistant for Subsurface** (2026) — n/a · cites 0 · score 9 (strong 1) · core/geoenergy_subsurface · doi:10.2523/iptc-25245-ms
signals: agentic;agentic*
touchpoints: none
Abstract Objective This paper introduces an AI-powered framework designed to enhance business and technical decision-making, knowledge sharing, and technical advisory. Unlike generic assistants, the system uses discipline-specific agents with contextual awareness of technical literature, company procedures, best practices, and petrotechnical software. The approach adheres to the C7 framework, which guides the development, management, and governance…

### arxiv:2409.00853
**JaxLife: An Open-Ended Agentic Simulator** (2024) — arXiv · cites 0 · score 9 (strong 2) · core/simulation_general · arXiv:2409.00853
signals: \btool[- ]use\b;agentic;agentic*
touchpoints: none
Human intelligence emerged through the process of natural selection and evolution on Earth. We investigate what it would take to re-create this process in silico. While past work has often focused on low-level processes (such as simulating physics or chemistry), we instead take a more targeted approach, aiming to evolve agents that can accumulate open-ended…

### doi:10.5281/zenodo.21721947
**extradimen/llm_big5_ad_sem: Simulating Personality-Based Advertising Responses Using AI Agents and Structural Equation Modeling** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.21721947
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: provenance_reproducibility;uncertainty_quantification
This record contains the data and complete reproducibility package supporting the revised manuscript on persona-conditioned large-language-model simulations of advertising attitude and purchase intention. The prespecified primary analysis uses Chinese-culture, promotion-framed responses generated with DeepSeek-V2 236B across ten generation runs. The Big Five values were assigned before prompting and are therefore analyzed as observed experimental condition…

### doi:10.36347/sjet.2025.v13i12.006
**Intelligent Science, One World: A Pan-Disciplinary Review of Data Science, Python, Machine Learning & AI Across Big Data, Cloud–Edge & HPC/Quantum, IoT & Robotics, Cybersecurity, Bio/Health Informatics, Geospatial/Remote Sensing, Blockchain, Digital Twins, and Responsible Governance** (2025) — Scholars Journal of Engineering and Technology · cites 0 · score 8 (strong 2) · core/simulation_orchestration · doi:10.36347/sjet.2025.v13i12.006
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: hpc_scale_out;provenance_reproducibility
Modern discovery is increasingly shaped by an integrated AI–Data–Compute–Governance stack that spans algorithms, software ecosystems, distributed infrastructure, cyber-physical systems, and socio-technical oversight. This review offers a pan-disciplinary synthesis across ten pillars Python/data-science ecosystems; ML/AI foundations including multimodality and RAG/agents; big data and the compute continuum (cloud–edge–HPC/quantum); IoT, robotics, and digital twins; bio/health informatics; geospatial/remote sensing;…

### arxiv:2606.18425
**From Specification to Execution: AI Assisted Scientific Workflow Management** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 2) · core/scientific_computing · arXiv:2606.18425
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);model context protocol
touchpoints: provenance_reproducibility;tool_exposure
Scientific workflow management systems (WMS) support scalable and reproducible execution of complex pipelines, but workflow design, implementation, and debugging remain largely manual and require significant expertise. Recent approaches using large language models (LLMs) show promise for workflow generation from natural language, but often rely on direct code synthesis, which limits transparency, reproducibility, and integration with…

### arxiv:2512.23010
**Masgent: An AI-assisted Materials Simulation Agent** (2025) — arXiv · cites 0 · score 8 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2512.23010
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b*
touchpoints: hpc_scale_out;provenance_reproducibility
Density functional theory (DFT) and machine learning potentials (MLPs) are essential for predicting and understanding materials properties, yet preparing, executing, and analyzing these simulations typically requires extensive scripting, multi-step procedures, and significant high-performance computing (HPC) expertise. These challenges hinder reproducibility and slow down discovery. Here, we introduce Masgent, an AI-assisted materials simulation agent that unifies…

### doi:10.48550/arxiv.2401.17244
**LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation** (2024) — arXiv (Cornell University) · cites 24 · score 8 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2401.17244
signals: \bReAct\b
touchpoints: provenance_reproducibility
Reducing hallucination of Large Language Models (LLMs) is imperative for use in the sciences, where reliability and reproducibility are crucial. However, LLMs inherently lack long-term memory, making it a nontrivial, ad hoc, and inevitably biased task to fine-tune them on domain-specific literature and data. Here we introduce LLaMP, a multimodal retrieval-augmented generation (RAG) framework of…

### doi:10.1016/j.taml.2025.100623
**A status quo investigation of large-language models for cost-effective computational fluid dynamics automation with OpenFOAMGPT** (2025) — Theoretical and Applied Mechanics Letters · cites 12 · score 8 (strong 1) · core/solver_control · doi:10.1016/j.taml.2025.100623
signals: \bLLM[- ]?agents?\b
touchpoints: solver_control
• OpenFOAMGPT extended to DeepSeek V3 and Qwen 2.5-Max for CFD automation • Reduces token cost by ∼100x compared to OpenAI o1 while preserving quality • Zero-shot prompts set up and debug diverse CFD cases without RAG support • Local 32B model on one GPU fails OpenFOAM syntax—fine-tuning still needed • Study charts path toward…

### doi:10.48550/arxiv.2602.00185
**QUASAR: A Universal Autonomous System for Atomistic Simulation and a Benchmark of Its Capabilities** (2026) — arXiv (Cornell University) · cites 2 · score 8 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2602.00185
signals: agentic;tool[- ]calling
touchpoints: uncertainty_quantification
The integration of large language models (LLMs) into materials science offers a transformative opportunity to streamline computational workflows, yet current agentic systems remain constrained by rigid, carefully crafted domain-specific tool-calling paradigms and narrowly scoped agents. In this work, we introduce QUASAR, a universal autonomous system for atomistic simulation designed to facilitate production-grade scientific discovery. QUASAR…

### doi:10.1145/3788149.3788227
**Agentic LLM Pipelines for Reproducible Scientific Software: Opportunities and Challenges** (2025) — n/a · cites 1 · score 8 (strong 1) · core/scientific_computing · doi:10.1145/3788149.3788227
signals: agentic;agentic*
touchpoints: provenance_reproducibility
Reproducibility of scientific experiments in computer science is still a critical issue, especially because the experimental software becomes more and more complex, diverse, and depends on a specific environment. While tools that enable packaging and environment replication have greatly facilitated making research transparent, significant barriers continue to exist for using computational results especially when new…

### doi:10.48550/arxiv.2602.17886
**El Agente Sólido: A New Age(nt) for Solid State Simulations** (2026) — arXiv (Cornell University) · cites 1 · score 8 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2602.17886
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility
Quantum chemistry calculations are a key component of the materials discovery process. The results from first-principles explorations enable the prediction of material properties prior to experimental validation. Despite their impact, the practical use of first-principles methods remains limited by the expertise required to design, execute, and troubleshoot complex computational workflows. Even when workflows are successfully…

### doi:10.26190/unsworks/32312
**Transforming Water and Wastewater Treatment with Digital Twins** (2026) — UNSWorks (University of New South Wales, Sydney, Australia) · cites 0 · score 8 (strong 2) · core/simulation_orchestration · doi:10.26190/unsworks/32312
signals: \bcopilots?\b;agentic
touchpoints: techno_economic
The escalating complexity of global water challenges in the 21st century, arising from population growth, overexploitation, climate change and emerging contaminants, demands a fundamental rethinking of how water treatment infrastructure is planned, operated, and maintained. Traditional infrastructure design and management approaches often rely on experience-guided rules and reactive process control and maintenance (PC&M) strategies, which…

### doi:10.48550/arxiv.2504.08621
**MooseAgent: A LLM Based Multi-agent Framework for Automating Moose Simulation** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · core/solver_control · doi:10.48550/arxiv.2504.08621
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: solver_control
The Finite Element Method (FEM) is widely used in engineering and scientific computing, but its pre-processing, solver configuration, and post-processing stages are often time-consuming and require specialized knowledge. This paper proposes an automated solution framework, MooseAgent, for the multi-physics simulation framework MOOSE, which combines large-scale pre-trained language models (LLMs) with a multi-agent system. The framework…

### doi:10.1145/3708035.3736023
**Automating HPC Software Compilation, Deployment, and Error Resolution through an LLM-based Multi-Agent System** (2025) — n/a · cites 0 · score 8 (strong 1) · core/scientific_computing · doi:10.1145/3708035.3736023
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: hpc_scale_out
High-performance computing (HPC) systems rely on complex software configurations that are traditionally managed through manual processes, leading to inefficiencies and increased risk of errors.In this paper, we present an LLM-based multi-agent system designed to automate the compilation, deployment, and error resolution of HPC software.Our approach leverages state-of-the-art language models to generate, refine, and iteratively improve…

### doi:10.2139/ssrn.6547019
**Accelerating Battery Materials Discovery with an Agentic AI for Automated XPS Analysis Integrating Physical Constraints and Chemometrics** (2026) — SSRN Electronic Journal · cites 0 · score 8 (strong 1) · core/scientific_computing · doi:10.2139/ssrn.6547019
signals: agentic;agentic*
touchpoints: provenance_reproducibility
The chemical heterogeneity of interfaces, such as the solid-electrolyte interphase (SEI), is a critical factor governing battery performance and degradation, yet its characterization remains a major bottleneck for materials discovery. While X-ray Photoelectron Spectroscopy (XPS) is essential for probing surface chemistry, conventional manual analysis is slow, subjective, and severely limits the pace of research by…

### doi:10.1038/s41598-025-92337-6
**A fine-tuned large language model based molecular dynamics agent for code generation to obtain material thermodynamic parameters** (2025) — Scientific Reports · cites 11 · score 8 (strong 1) · core/scientific_computing · doi:10.1038/s41598-025-92337-6
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
In the field of materials science, addressing the complex relationship between the material structure and properties has increasingly involved leveraging the text generation capabilities of AI-generated content (AIGC) models for tasks that include literature mining and data analysis. However, theoretical calculations and code development remain labor-intensive challenges. This paper proposes a novel approach based on…

### doi:10.1609/aaai.v39i28.35373
**Agentic AI for Digital Twin** (2025) — Proceedings of the AAAI Conference on Artificial Intelligence · cites 10 · score 8 (strong 1) · core/simulation_orchestration · doi:10.1609/aaai.v39i28.35373
signals: agentic;agentic*
touchpoints: none
The complexity of the shipping industry, dynamic operational drivers, and diverse data sources present significant scalability challenges for digital twins. Agentic Large Language Models (LLMs) augmented with external tools offer a promising solution to accelerate digital twin adoption. Using pre-trained knowledge and reasoning capabilities, these LLMs autonomously select optimal tools and data streams for user-specific…

### doi:10.48550/arxiv.2509.20705
**Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2509.20705
signals: agentic;agentic*
touchpoints: none
The adoption of cyber-physical systems and jobsite intelligence that connects design models, real-time site sensing, and autonomous field operations can dramatically enhance digital management in the construction industry. This paper introduces BIM2RDT (Building Information Models to Robot-Ready Site Digital Twins), an agentic artificial intelligence (AI) framework designed to transform static Building Information Modeling (BIM) into…

### doi:10.5194/egusphere-egu25-19197
**Agentic AI for ship routing** (2025) — n/a · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.5194/egusphere-egu25-19197
signals: agentic;agentic*
touchpoints: none
The complexity of the shipping industry, with its dynamic operational drivers and diverse data sources, presents significant scalability challenges for digital twins. Agentic Large Language Models (LLMs), augmented with external tools, offer a promising solution to streamline operations and improve decision-making. By leveraging pre-trained knowledge and reasoning capabilities, these LLMs can autonomously select the most…

### doi:10.65713/ijaraiv14i1225
**INTELLIGENT CANCER DIGITAL TWINS: AI-DRIVEN VIRTUAL PATIENT MODELS FOR PREDICTIVE ONCOLOGY** (2026) — International Journal of Advanced Research and Innovations · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1225
signals: agentic
touchpoints: none
Intelligent cancer digital twins are emerging as one of the most transformative innovations in precision oncology by enabling continuously evolving virtual representations of individual patients capable of supporting predictive diagnosis, personalized therapeutic planning, adaptive disease monitoring, and evidence-based clinical decision-making. Conventional oncology frequently depends upon fragmented interpretation of radiological imaging, molecular diagnostics, pathological findings, and…

### doi:10.65713/ijaraiv14i1216
**PRECISION CANCER INTELLIGENCE: LEVERAGING FOUNDATION MODELS, DIGITAL TWINS, AND MULTIMODAL LEARNING FOR CLINICAL TRANSLATION** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1216
signals: agentic
touchpoints: none
Precision cancer intelligence is emerging as a transformative paradigm in modern oncology through the convergence of foundation artificial intelligence (AI) models, digital twins, multimodal learning, and translational clinical intelligence. Conventional oncology frequently relies on fragmented diagnostic modalities and isolated interpretation of molecular, imaging, pathological, and clinical information, thereby limiting comprehensive understanding of the dynamic biological…

### doi:10.48550/arxiv.2504.06260
**FEABench: Evaluating Language Models on Multiphysics Reasoning Ability** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 2) · core/solver_control · doi:10.48550/arxiv.2504.06260
signals: \bLLM[- ]?agents?\b;language model agents?
touchpoints: none
Building precise simulations of the real world and invoking numerical solvers to answer quantitative problems is an essential requirement in engineering and science. We present FEABench, a benchmark to evaluate the ability of large language models (LLMs) and LLM agents to simulate and solve physics, mathematics and engineering problems using finite element analysis (FEA). We…

### doi:10.65713/ijaraiv14i1212
**INTELLIGENT DIGITAL TWINS IN ONCOLOGY: REAL-TIME VIRTUAL PATIENT MODELING FOR PERSONALIZED THERAPEUTIC DECISION-MAKING** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1212
signals: agentic
touchpoints: none
Digital twin technology is emerging as one of the most transformative innovations in precision oncology by enabling the creation of continuously evolving virtual representations of individual cancer patients capable of supporting real-time therapeutic decision-making. Conventional oncology frequently relies on episodic clinical assessments and fragmented diagnostic information that inadequately capture the dynamic biological evolution of tumors…

### doi:10.65713/ijaraiv14i1218
**DIGITAL TWIN–ENABLED PRECISION ONCOLOGY: INTEGRATING LONGITUDINAL PATIENT DATA, MULTI-OMICS, AND ARTIFICIAL INTELLIGENCE** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1218
signals: agentic
touchpoints: none
Digital twin technology is rapidly emerging as one of the most transformative innovations in precision oncology by enabling continuously evolving virtual representations of individual cancer patients capable of supporting predictive, personalized, and adaptive clinical decision-making. Traditional oncology frequently depends on fragmented interpretation of radiological imaging, molecular diagnostics, pathological findings, and episodic clinical assessments, limiting comprehensive…

### arxiv:2603.25898
**On Integrating Resilience and Human Oversight into LLM-Assisted Modeling Workflows for Digital Twins** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2603.25898
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
LLM-assisted modeling holds the potential to rapidly build executable Digital Twins of complex systems from only coarse descriptions and sensor data. However, resilience to LLM hallucination, human oversight, and real-time model adaptability remain challenging and often mutually conflicting requirements. We present three critical design principles for integrating resilience and oversight into such workflows, derived from…

### doi:10.5281/zenodo.19910215
**Code for Text-to-Flowsheet: An LLM-Assisted Pipeline for Expert-Level Digitization and Automated Simulation of Chemical Processes** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.19910215
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
This repository contains the code for the flowsheet digitization pipelines described in "Text-to-Flowsheet: An LLM-Assisted Pipeline for Expert-Level Digitization and Automated Simulation of Chemical Processes". Please find the repositories here: https://gitlab.ethz.ch/epse/process-design-public/text2flowsheet https://gitlab.ethz.ch/epse/process-design-public/graph2simulation…

### doi:10.3778/j.issn.1673-9418.2508051
**Multimodal Information Fusion-Guided Graphical Interface Code Generation Framework for OpenFOAM** (2025) — DOAJ (DOAJ: Directory of Open Access Journals) · cites 0 · score 8 (strong 2) · core/solver_control · doi:10.3778/j.issn.1673-9418.2508051
signals: knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Addressing the dual challenges of OpenFOAM?s high learning curve due to its reliance on command-line operations and the generally long development cycles and high customization costs of traditional simulation interfaces, this paper proposes the AutoCode4OF framework, which aims to achieve end-to-end automatic generation of a complete OpenFOAM executable interface code from multimodal inputs. The main…

### arxiv:2604.01520
**LLM Agents as Social Scientists: A Human-AI Collaborative Platform for Social Science Automation** (2026) — arXiv · cites 0 · score 8 (strong 1) · core/simulation_general · arXiv:2604.01520
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
Traditional social science research often requires designing complex experiments across vast methodological spaces and depends on real human participants, making it labor-intensive, costly, and difficult to scale. Here we present S-Researcher, an LLM-agent-based platform that assists researchers in conducting social science research more efficiently and at greater scale by "siliconizing" both the research process and…

### arxiv:2607.06080
**From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations** (2026) — arXiv · cites 0 · score 8 (strong 2) · core/simulation_general · arXiv:2607.06080
signals: \bLLM[- ]?agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Putnam's Social Capital Theory is a foundational framework for collective action and community prosperity. However, traditional empirical methods face practical limits on control and replication. Meanwhile, LLM-based social simulations are typically behavior-driven and lack theory-aligned environments for modeling Putnam's core propositions. To address these gaps, we introduce SocaSim, an LLM-based multi-agent simulation framework to study…

### doi:10.18653/v1/2026.findings-acl.188
**Apeiron: A Scalable LLM-agentic Framework for Autonomous Full-lifecycle Demand-optimized Application Synthesis** (2026) — n/a · cites 0 · score 8 (strong 1) · core/simulation_general · doi:10.18653/v1/2026.findings-acl.188
signals: agentic;agentic*
touchpoints: none
We introduce Apeiron, a scalable and extensible framework for addressing amorphous user demands through autonomous, full-lifecycle application synthesis.Apeiron models the unstructured app development process as a heuristic optimization problem combining (i) a Computer-Use Agent (CUA) evaluator that simulates personas and demands, (ii) an Activity Tracer that grounds feedback in code-level interaction traces, and (iii) a…

### doi:10.48550/arxiv.2603.03372
**TritonDFT: Automating DFT with a Multi-Agent Framework** (2026) — arXiv (Cornell University) · cites 1 · score 7 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2603.03372
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: hpc_scale_out;optimisation_loop;verification_regression
Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a…

### doi:10.5281/zenodo.21841882
**Artifact for "Works but Wrong: Domain Tools Sharpen AI Diagnosis of HPC Simulation Setup Errors"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · core/scientific_computing · doi:10.5281/zenodo.21841882
signals: \bAI agents?\b;agentic
touchpoints: config_generation;hpc_scale_out;provenance_reproducibility
Artifact for the AgenticAI4HPC'26 (SC26 workshop) paper "Works but Wrong: Domain Tools Sharpen AI Diagnosis of HPC Simulation Setup Errors". A simulation can finish successfully on an HPC system and still be wrong, usually because of a mistake in its setup files rather than a bug in the solver. This artifact holds the code, test…

### doi:10.1002/adma.202515941
**Materials Informatics: Emergence to Autonomous Discovery in the Age of AI** (2026) — Advanced Materials · cites 10 · score 7 (strong 1) · core/optimisation_uq · doi:10.1002/adma.202515941
signals: self[- ]driving lab
touchpoints: optimisation_loop;uncertainty_quantification
We provide a perspective on the evolution of materials informatics, tracing its conceptual roots to foundational ideas in physics and information theory and its maturation through the integration of machine learning and artificial intelligence (AI). Early contributions from Chelikowsky, Phillips, and Bhadeshia laid the groundwork for what has become a transformative approach to materials discovery.…

### doi:10.20944/preprints202608.1323.v1
**Early Experiences Using AI Software Agents on OLCF Systems: From Installation and Environments to Simulation Workflows for Molecular and Materials Sciences** (2026) — Preprints.org · cites 0 · score 7 (strong 2) · core/scientific_computing · doi:10.20944/preprints202608.1323.v1
signals: agent(?:ic)? workflows?;agentic
touchpoints: hpc_scale_out;provenance_reproducibility
Scientific workflows on large computing clusters increasingly combine massively parallel simulation engines, machine-learned models, and theory development with the technical aspects of installation, testing and debugging, batch scheduling, and designing architecture-specific GPU-accelerated software. On leadership-class systems, these workflows can be difficult to deploy successfully for production science due to compounding problems: compilation, installation, and package…

### doi:10.5281/zenodo.20386682
**NoseSense: Benchmarking Tool** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.20386682
signals: \bLangChain\b
touchpoints: provenance_reproducibility;verification_regression
# NoseSense ## Artifact Description The rapid evolution of Large Language Models (LLMs) has rendered traditional, static evaluation studies quickly obsolete upon publication. In this fast-paced landscape, evaluation methodologies must enable continuous and immediate assessment of newly released models. Although benchmarks exist for various software engineering tasks, there is a lack of targeted evaluation frameworks…

### doi:10.48550/arxiv.2608.26016
**Bayesian Optimization for Self-Driving Materials Laboratories: From Algorithms to Physics-Informed Workflows** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · core/optimisation_uq · doi:10.48550/arxiv.2608.26016
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;self[- ]driving lab
touchpoints: optimisation_loop;surrogate_modelling
Self-driving laboratories (SDLs) are transforming materials research by closing the loop among synthesis, characterization, data analysis and experimental decision making. Bayesian optimization (BO) is a decision engine for these loops because it can select experiments from scarce and noisy data while balancing exploitation and exploration. Yet real materials campaigns often depart from the standard black-box…

### arxiv:2609.03598
**RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · core/scientific_computing · arXiv:2609.03598
signals: agent(?:ic)? workflows?;agentic
touchpoints: hpc_scale_out;verification_regression
The emergence of modern agents powered by large language models has created a demand for executing long-horizon, autonomous workflows in various domains that require significant computational resources. While High Performance Computing clusters provide the ideal infrastructure for these computation-intensive workloads, traditional HPC job schedulers such as Slurm are not designed for dynamic, agentic workflows characterized…

### doi:10.1016/j.taml.2025.100594
**Fine-tuning a large language model for automating computational fluid dynamics simulations** (2025) — Theoretical and Applied Mechanics Letters · cites 28 · score 7 (strong 1) · core/solver_control · doi:10.1016/j.taml.2025.100594
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: config_generation
• We fine-tuned a domain-specific LLM, empowering a multi-agent system to automate CFD simulation from natural language input. • We developed NL2FOAM, a dataset containing 28716 cases designed for automated OpenFOAM simulation driven by natural language. • The system achieves an 82.6% first-attempt success rate on the benchmark with an average accuracy of 88.7%, demonstrating…

### doi:10.1016/j.ecmx.2025.101329
**Artificial intelligence and machine learning for smart grids: from foundational paradigms to emerging technologies with digital twin and large language model-driven intelligence** (2025) — Energy Conversion and Management X · cites 23 · score 7 (strong 1) · core/simulation_orchestration · doi:10.1016/j.ecmx.2025.101329
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: hpc_scale_out
• Comprehensive review of AI/ML applications in smart grids and power systems. • Bibliometric analysis of 123 studies maps forecasting, control, and security clusters. • Examines frontier paradigms: Digital Twins, Federated Learning, LLMs, and GenAI. • Identifies gaps in interoperability, privacy, scalability, and adversarial robustness. • Proposes hybrid DT–LLM frameworks for resilient, sustainable energy intelligence.…

### doi:10.1145/3731599.3767584
**Evaluating the Efficacy of LLM-Based Reasoning for Multiobjective HPC Job Scheduling** (2025) — arXiv (Cornell University) · cites 3 · score 7 (strong 1) · core/scientific_computing · doi:10.1145/3731599.3767584
signals: \bReAct\b
touchpoints: hpc_scale_out
High-Performance Computing (HPC) job scheduling involves balancing conflicting objectives such as minimizing makespan, reducing wait times, optimizing resource use, and ensuring fairness. Traditional methods, including heuristic-based, e.g., First-Come-First-Served(FJFS) and Shortest Job First (SJF), or intensive optimization techniques, often lack adaptability to dynamic workloads and, more importantly, cannot simultaneously optimize multiple objectives in HPC systems. To…

### doi:10.1016/j.taml.2026.100660
**Large language model-assisted sensitivity analysis and parameter optimization in computational fluid dynamics** (2026) — Theoretical and Applied Mechanics Letters · cites 2 · score 7 (strong 1) · core/solver_control · doi:10.1016/j.taml.2026.100660
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: uncertainty_quantification
• Introduces a novel large language model-driven chain-of-thought (COT) framework that integrates computational fluid dynamics (CFD) simulations with sensitivity analysis and parameter optimization. • Proposes the OptMetaOpenFOAM system, enabling natural language inputs to automate complex CFD tasks and lowering the technical barriers for non-expert users. • Demonstrates the effectiveness of the approach on two benchmark…

### doi:10.5281/zenodo.20543501
**OASiS: an open-source multi-physics and multi-code framework for verified computer simulations** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · core/solver_control · doi:10.5281/zenodo.20543501
signals: agent(?:ic)? workflows?;model context protocol
touchpoints: tool_exposure
OASiS is an open-source Model Context Protocol (MCP) server that connects general-purpose LLM coding agents to eight independently developed finite element solvers (FEniCSx, deal.II, 4C Multiphysics, NGSolve, scikit-fem, Kratos Multiphysics, DUNE-fem, FEBio). It exposes a small set of shared tools for solver discovery, simulation preparation, mesh generation, run execution, multi-solver coupling, in-place solver development, and…

### doi:10.5281/zenodo.21369518
**## Artificial Intelligence for Advanced Materials Science: A Comprehensive Framework for Phase Transformations, Microstructure Evolution, Alloy Design, Additive Manufacturing, and Beyond** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · core/computational_discovery · doi:10.5281/zenodo.21369518
signals: autonomous experimentation;self[- ]driving lab
touchpoints: uncertainty_quantification
# ALTERNATIVE COMBINED TITLES ## Alternative Title 1**AI-Driven Materials Science: From Phase Transformations to Intelligent Manufacturing – A Unified Framework for Accelerated Discovery and Optimization** ### SubtitleIntegrating Machine Learning, Deep Learning, Physics-Informed Neural Networks, and Generative AI for Next-Generation Materials Development --- ## Alternative Title 2**Machine Learning and Deep Learning in Materials Science: A Comprehensive…

### doi:10.1038/s43246-026-01304-9
**Large-language-model-driven adaptive search space definition for autonomous closed-loop materials exploration** (2026) — Communications Materials · cites 0 · score 7 (strong 1) · core/optimisation_uq · doi:10.1038/s43246-026-01304-9
signals: self[- ]driving lab
touchpoints: optimisation_loop
Autonomous closed-loop materials exploration systems that couple machine learning with robotic experimentation, often called self-driving laboratories, are increasingly used to accelerate materials discovery. However, their end-to-end autonomy is limited by the need for human experts to specify and periodically reconfigure the search space. Herein, we propose a data-driven framework that adaptively redefines the materials search…

### doi:10.1109/kst67832.2026.11431975
**HPC-MentorFlow: Strengthening Institutional HPC Competencies through an LLM-Enhanced Tutoring System** (2026) — n/a · cites 0 · score 7 (strong 1) · core/scientific_computing · doi:10.1109/kst67832.2026.11431975
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: hpc_scale_out
The development of skilled professionals for diverse High-Performance Computing (HPC) environments is a substantial barrier to progress in both scientific and industrial areas. We present HPC-MentorFlow, an LLM-based tutoring system codesigned by the National Electronics and Computer Technology Center (NECTEC), Thailand, and the University of Luxembourg to deliver adaptive, accreditation-ready training tailored to local HPC…

### doi:10.3897/biss.9.183132
**MfN DataHub – a Centralized Service for Automated Biodiversity Data Integration at the Museum for Natural History Berlin** (2025) — Biodiversity Information Science and Standards · cites 0 · score 7 (strong 2) · core/scientific_computing · doi:10.3897/biss.9.183132
signals: \bAI agents?\b;\bLangChain\b
touchpoints: provenance_reproducibility
The Museum für Naturkunde Berlin (MfN) DataHub*1 is an open-source web service and workflow engine developed to execute automated data-integration and migration workflows in continuous and parallel scenarios. Data migration and integration remain major challenges in publishing biodiversity data that follow international standards. To overcome these, a centralized service was created to coordinate and concentrate…

### doi:10.31234/osf.io/wf5bv_v1
**Automating Reproducibility Checks Using Large Language Models** (2026) — PsyArXiv (OSF Preprints) · cites 0 · score 7 (strong 1) · core/scientific_computing · doi:10.31234/osf.io/wf5bv_v1
signals: agentic
touchpoints: provenance_reproducibility
Computational reproducibility checks are essential for scientific credibility, but most published papers are never independently verified because manual reproducibility audits are difficult and time-consuming. We tested whether an agentic large language model (LLM) could perform computational reproducibility checks at scale. We benchmarked computational reproducibility checks performed by an LLM analyst (Claude Opus 4.7, running in…

### doi:10.48550/arxiv.2605.02651
**ARA: Agentic Reproducibility Assessment For Scalable Support Of Scientific Peer-Review** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2605.02651
signals: agentic;agentic*
touchpoints: provenance_reproducibility
Scientific peer review increasingly struggles to assess reproducibility at the scale and complexity of modern research output. Evaluating reproducibility requires reconstructing experimental dependencies, methodological choices, data flows, and result-generating procedures, which often exceeds what human reviewers can provide. Agentic Reproducibility Assessment (ARA) formalizes reproducibility assessment as a structured reasoning task over scientific documents. Given a…

### doi:10.1016/j.coche.2025.101150
**Industrial Agentic AI and generative modeling in complex systems** (2025) — Current Opinion in Chemical Engineering · cites 28 · score 7 (strong 1) · core/simulation_orchestration · doi:10.1016/j.coche.2025.101150
signals: agentic;agentic*
touchpoints: none
Manufacturing, consumer, transportation, and supply chain processes present significant challenges in monitoring, control, and design due to their inherently nonlinear nature and the difficulty of measuring critical variables in real time. The convergence of major innovations from the computer science field has the potential to revolutionize the engineering and control of complex industrial systems. Digital…

### doi:10.1093/jamia/ocaf076
**Semi-automated pipeline to accelerate multi-site flowsheet alignment and concept mapping in electronic health records** (2025) — Journal of the American Medical Informatics Association · cites 5 · score 7 (strong 1) · core/simulation_orchestration · doi:10.1093/jamia/ocaf076
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b*
touchpoints: none
OBJECTIVES: Health-care institutions customize electronic health record (EHR) configurations to reflect their unique workflows and patient care priorities. Ensuring EHR alignment across sites facilitates seamless information exchange. We developed a pipeline for EHR flowsheet alignment between health-care organizations. The pipeline is augmented by mapping flowsheet data fields to concepts in the Clinical Care Classification (CCC)…

### doi:10.48550/arxiv.2601.01321
**Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models** (2026) — arXiv (Cornell University) · cites 1 · score 7 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2601.01321
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b
touchpoints: none
Digital twins, as precise digital representations of physical systems, have evolved from passive simulation tools into intelligent and autonomous entities through the integration of artificial intelligence technologies. This paper presents a unified four-stage framework that systematically characterizes AI integration across the digital twin lifecycle, spanning modeling, mirroring, intervention, and autonomous management. By synthesizing existing technologies…

### doi:10.3390/electronics15091869
**Integrating Conversational AI Agents with Digital Twins: A Systems Engineering Approach to Complex Infrastructure Management and Predictive Decision-Making** (2026) — Electronics · cites 0 · score 7 (strong 1) · core/simulation_orchestration · doi:10.3390/electronics15091869
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
Background: Managing complex infrastructure increasingly requires predictive, adaptive, and human-centered systems. Traditional approaches often struggle with operational complexity, fragmented data, and high technical barriers. Methods: This study presents a TRL4 proof of concept integrating a conversational AI agent with a user-adaptive digital twin for occupancy forecasting. Users can upload their own datasets, and dynamically configure…

### doi:10.65713/ijaraiv14i1229
**DIGITAL ONCOLOGY 5.0: THE CONVERGENCE OF ARTIFICIAL INTELLIGENCE, DIGITAL TWINS, AND PRECISION MEDICINE** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 7 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1229
signals: agentic
touchpoints: none
Digital Oncology 5.0 represents the next evolutionary stage of cancer medicine, characterized by the convergence of artificial intelligence (AI), digital twins, multimodal foundation models, precision medicine, and intelligent healthcare ecosystems capable of delivering predictive, preventive, personalized, participatory, and continuously adaptive cancer care. Conventional oncology frequently relies on fragmented diagnostic workflows, episodic clinical assessments, and isolated…

### doi:10.48550/arxiv.2608.22833
**Minimal Local Simulation Foundations for LLM- and VLM-Driven Agents in 2D and 3D Environments** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · core/simulation_general · doi:10.48550/arxiv.2608.22833
signals: \bLLM[- ]?agents?\b
touchpoints: none
Large language models (LLMs) and vision-language models (VLMs) are expanding the range of behaviors that can be represented in agent-based simulations, but many contemporary platforms are difficult to study, modify, or run on ordinary computers. We present two intentionally minimal simulation foundations for education and rapid prototyping. SD-AgentFoundry-2D provides a two-dimensional multi-agent environment in which…

### title:aplatformforprescriptivedigitaltwinsinaec
**A Platform for Prescriptive Digital Twins in AEC** (2026) — TSpace (University of Toronto) · cites 0 · score 7 (strong 2) · core/simulation_orchestration · https://hdl.handle.net/1807/153711
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Realizing the full potential of digital twins in facility management requires prescriptive modeling that does more than describe current states — it must anticipate operational needs, recommend actions, and adapt as conditions evolve. However, this remains difficult due to fragmented data silos and the lack of flexible mechanisms to connect diverse information sources. Most existing…

### doi:10.5281/zenodo.20050752
**Evolution of the Research Software Engineer role in the age of generative and agentic AI** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.20050752
signals: agentic;agentic*
touchpoints: none
Four images that represent the evolution of the role of Research Software Engineer (RSE) in the age of generative and agentic "artificial intelligence" (AI). These images are an outcome of a working group at the workshop "Research Software Engineering in the Age of Generative AI: Building a Community Vision" run by theResearch Software Alliance (ReSA).…

### doi:10.5281/zenodo.19835550
**M.A.R.V.I.N. – A Software-Led Infrastructure for Thermodynamically Grounded Autonomous Materials Discovery** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 2) · core/computational_discovery · doi:10.5281/zenodo.19835550
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);agentic
touchpoints: config_generation;provenance_reproducibility;tool_exposure
MARVIN — short for (Materials Agentic Research, Validation, and Inference Navigation)— is a software-led infrastructure for materials discovery that treats the CALPHAD-derived Gibbs energy function as the universal currency tying every step of an autonomous loop together. The motivation is a concrete gap in the current self-driving-laboratory (SDL) literature: systems like the A-Lab, Ada, and…

### doi:10.1016/j.mlwa.2025.100773
**Uncertainty quantification by large language models** (2025) — Machine Learning with Applications · cites 2 · score 6 (strong 1) · core/optimisation_uq · doi:10.1016/j.mlwa.2025.100773
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: uncertainty_quantification;verification_regression
As reasoning capabilities of large language models (LLMs) continue to advance, they are being integrated into increasingly complex scientific workflows, with the goal of developing agents capable of generating evidence-based explanations and testing hypotheses and theories. However, despite their rapid progress, most existing evaluations of LLM reasoning focus on accuracy or consistency rather than on…

### doi:10.26434/chemrxiv.15005632/v1
**Dual Digital Twins for Experimental Planning in Automated Laboratories: Physics-informed surrogate models for counterfactual experimental rollouts** (2026) — ChemRxiv · cites 0 · score 6 (strong 2) · core/simulation_orchestration · doi:10.26434/chemrxiv.15005632/v1
signals: agentic;autonomous agents?
touchpoints: provenance_reproducibility;surrogate_modelling
Automated laboratories increasingly combine automated and cloudified instruments, robotic operation, sample provenance and data infrastructures, and autonomous agents. Yet these capabilities primarily address execution, while planning remain limited to myopic optimization workflows or generic agentic approaches. At the same time, open decision-making algorithms such as MCDTs, reinforcement learning, or dynamic programming that worked exceptionally well…

### title:intelligentdigitaltwinsystemforurbanmobility
**Intelligent Digital Twin System for Urban Mobility** (2026) — Scholars Commons (Wilfrid Laurier University) · cites 0 · score 6 (strong 1) · core/simulation_orchestration · https://scholars.wlu.ca/etd/2908
signals: \bLangGraph\b
touchpoints: hpc_scale_out;provenance_reproducibility
Digital twin technology has emerged as a transformative paradigm for intelligent transportation systems, driven by the growing need to analyze, simulate and optimize increasingly complex urban transportation networks. Digital twin systems help fulfill this requirement through the exchange between physical transportation infrastructure and its virtual counterpart. Urban mobility, characterized by independent transport modes, volatile traffic…

### doi:10.48550/arxiv.2509.20374
**CFDLLMBench: A Benchmark Suite for Evaluating Large Language Models in Computational Fluid Dynamics** (2025) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/solver_control · doi:10.48550/arxiv.2509.20374
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: provenance_reproducibility;verification_regression
Large Language Models (LLMs) have demonstrated strong performance across general NLP tasks, but their utility in automating numerical experiments of complex physical system -- a critical and labor-intensive component -- remains underexplored. As the major workhorse of computational science over the past decades, Computational Fluid Dynamics (CFD) offers a uniquely challenging testbed for evaluating the…

### arxiv:2602.03783
**Efficient Estimation of Kernel Surrogate Models for Task Attribution** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/optimisation_uq · doi:10.48550/arxiv.2602.03783
signals: \bAI agents?\b
touchpoints: optimisation_loop;surrogate_modelling
Modern AI agents such as large language models are trained on diverse tasks -- translation, code generation, mathematical reasoning, and text prediction -- simultaneously. A key question is how to quantify the influence of each individual training task on performance on a target task, a problem we refer to as task attribution. The direct approach,…

### doi:10.3390/app16126093
**Reproducible Expert Weight Elicitation via LLM Multi-Agent Simulation: A Best–Worst Method Decision Support Framework for AI-Driven E-Commerce Platform Evaluation** (2026) — Applied Sciences · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.3390/app16126093
signals: \bLLM[- ]?agents?\b
touchpoints: provenance_reproducibility;uncertainty_quantification
The pervasive integration of artificial intelligence across e-commerce ecosystems has fundamentally transformed the competitive landscape, rendering systematic and reproducible platform evaluation frameworks an operational necessity rather than an academic exercise. Conventional multi-criteria decision analysis approaches for e-commerce evaluation remain structurally constrained by their dependency on human expert panels, which introduce recruitment costs, cognitive biases, limited…

### doi:10.5281/zenodo.20777543
**SafeCKD-Agent: Code, Data, and Reproducibility Artifacts for Retrieval-Grounded Clinical Decision Support** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 2) · core/scientific_computing · doi:10.5281/zenodo.20777543
signals: agent(?:ic)? workflows?;agentic
touchpoints: provenance_reproducibility;uncertainty_quantification
SafeCKD-Agent: Code, Data, and Reproducibility Artifacts This Zenodo record contains the reproducibility package for the study: SafeCKD-Agent: A Trustworthy Agentic AI Framework for Retrieval-Grounded Clinical Decision Support The package provides code notebooks, public data artifacts, processed datasets, retrieval knowledge base files, trained model artifacts, prediction outputs, agentic workflow outputs, audit logs, evaluation tables, generated figures,…

### doi:10.1145/3785462.3815852
**Empowering Cancer Researchers: An Agentic AI System for Intuitive Interaction with High-Performance Computing** (2026) — n/a · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.1145/3785462.3815852
signals: agentic;agentic*
touchpoints: hpc_scale_out;provenance_reproducibility
Memorial Sloan Kettering Cancer Center (MSKCC) investigates cancer's fundamental mechanisms across disciplines such as genetics, immunology, and molecular biology to understand the tumor microenvironment and its interactions with the body's ecosystem. Researchers are increasingly turning to computational systems to address complex scientific and medical questions. However, many translational researchers lack expertise in high-performance computing (HPC),…

### doi:10.11578/dc.20260331.2
**AstraAI v1** (2026) — OSTI OAI (U.S. Department of Energy Office of Scientific and Technical Information) · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.11578/dc.20260331.2
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: hpc_scale_out;provenance_reproducibility
AstraAI is an open-source, structure-aware AI coding agent designed for large scientific and DOE-HPC codebases such as AMReX-based applications. Unlike general-purpose coding assistants, AstraAI combines retrieval-augmented generation (RAG) with compiler-level Abstract Syntax Tree (AST) analysis to perform precise, scope-constrained code modifications. It identifies exact function spans, enforces locality of edits, and maintains cross-file invariants, enabling…

### doi:10.3389/fhpcp.2026.1771927
**OpenMP-annotated code dataset for large language model fine-tuning on parallel programming tasks** (2026) — Frontiers in High Performance Computing · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.3389/fhpcp.2026.1771927
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: hpc_scale_out;provenance_reproducibility
High-performance computing (HPC) plays a critical role in scientific discovery, engineering simulation, and data-intensive applications. OpenMP (Open Multi-Processing) is one of the most widely adopted shared-memory parallel programming interfaces, enabling developers to write multi-threaded applications in C, C++, and Fortran. However, correctly implementing OpenMP directives requires significant expertise, as developers must understand parallel programming concepts,…

### doi:10.3390/a19030218
**A Self-Deciding Adaptive Digital Twin Framework Using Agentic AI for Fuzzy Multi-Objective Optimization of Food Logistics** (2026) — Algorithms · cites 6 · score 6 (strong 1) · core/simulation_orchestration · doi:10.3390/a19030218
signals: agentic;agentic*
touchpoints: optimisation_loop
Due to the perishable nature of products, high uncertainty, and conflicting objectives, food supply chain logistics management requires dynamic and adaptive decision-making frameworks. In this study, an integrated decision-making architecture is presented that integrates a multi-objective fuzzy optimization model into an adaptive digital twin along with an agentic AI-based dynamic goal reset mechanism. The main…

### doi:10.1002/aidi.202500174
**ChatCFD: A Large Language Model‐Driven Agent for End‐to‐End Computational Fluid Dynamics Automation with Structured Knowledge and Reasoning** (2026) — Advanced Intelligent Discovery · cites 2 · score 6 (strong 1) · core/solver_control · doi:10.1002/aidi.202500174
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: solver_control
Computational fluid dynamics (CFD) is essential for advancing scientific and engineering fields, but is hindered by operational complexity, high expertise requirements, and limited accessibility. This article introduces ChatCFD, a large language model (LLM)‐driven agent system for end‐to‐end CFD automation. Powered by DeepSeek‐R1/V3, a multiagent architecture, structured OpenFOAM knowledge bases, precise error locator, and iterative reflection,…

### doi:10.1145/3731599.3767403
**Frameworks for Large Language Model Serving in HPC Environments** (2025) — n/a · cites 2 · score 6 (strong 1) · core/scientific_computing · doi:10.1145/3731599.3767403
signals: \bAI agents?\b
touchpoints: hpc_scale_out
We introduce open-source frameworks for deploying and running large language models (LLMs) within high-performance computing (HPC) environments. One such framework, AI-Flux, targets high-throughput batch inference, enabling users to submit LLM requests in an OpenAI-compatible format as traditional HPC jobs. Another framework is based on Ray Serve and it provides dynamic, on-demand allocation of HPC resources…

### title:mechanicaldesignusingmultiphysicsagenticaivolume3handsonmultiphysicsprojectshandsoncompositesfeaandmultiphysicsprojectsw
**Mechanical design using multiphysics & Agentic AI - Volume 3: Hands-on multiphysics projects. Hands-on composites FEA and multiphysics projects with Gmsh & Elmer** (2026) — Research Portal (Queen's University Belfast) · cites 0 · score 6 (strong 1) · core/simulation_orchestration · https://pure.qub.ac.uk/en/publications/7504f842-1380-4d16-8395-c6de6625d9fc
signals: agentic;agentic*
touchpoints: provenance_reproducibility
This volume is the hands-on core of the series. You move from theory and agent building to real engineering projects by replicating and automating classic case studies from Ever J. Barbero’s composites FEA and William B. J. Zimmerman’s multiphysics modelling — using only free open-source tools. You will complete six major portfolio projects: Vibration &…

### doi:10.48550/arxiv.2601.03113
**A Probabilistic Digital Twin of UK En Route Airspace for Training and Evaluating AI Agents for Air Traffic Control** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2601.03113
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: surrogate_modelling
This paper presents the first probabilistic Digital Twin of operational en route airspace, developed for the London Area Control Centre. The Digital Twin is intended to support the development and rigorous human-in-the-loop evaluation of AI agents for Air Traffic Control (ATC), providing a virtual representation of real-world airspace that enables safe exploration of higher levels…

### doi:10.62311/nesx/rb3jy-978-81-688729-7-4
**Post-Quantum Cybersecurity and Cryptographic Governance for AI-Era Digital Infrastructure** (2026) — n/a · cites 0 · score 6 (strong 2) · core/simulation_orchestration · doi:10.62311/nesx/rb3jy-978-81-688729-7-4
signals: agentic;autonomous agents?
touchpoints: provenance_reproducibility
Abstract: Post-quantum cybersecurity is emerging as a defining governance challenge for AI-era digital infrastructure because cryptographic decisions now shape the security of data, machine identities, model supply chains, autonomous agents, public services and cyber-physical systems. This monograph develops an integrated research architecture for understanding and governing that transition. It connects quantum threat horizons and cryptographic…

### doi:10.1109/icept67137.2025.11157286
**Automated Mesh Generation in FEM: A Novel Approach Using Large Language Models** (2025) — n/a · cites 0 · score 6 (strong 1) · core/solver_control · doi:10.1109/icept67137.2025.11157286
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: solver_control
The automation of mesh generation in finite element method (FEM) simulations plays a crucial role in reducing computational effort while ensuring high accuracy. Traditional approaches for mesh refinement, particularly in geometries with stress concentrations, often involve post-processing error estimation and iterative adjustments, resulting in significant computational overhead. Recent advancements in large language models (LLMs) have…

### doi:10.57760/sciencedb.taml.00004
**Source code for MetaOpenFOAM: LLM-assisted sensitivity analysis and optimization in CFD** (2026) — ScienceDB · cites 0 · score 6 (strong 1) · core/solver_control · doi:10.57760/sciencedb.taml.00004
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: uncertainty_quantification
This dataset provides the source code supporting the paper “Large Language Model-Assisted Sensitivity Analysis and Parameter Optimization in Computational Fluid Dynamics”, submitted to Theoretical and Applied Mechanics Letters.The repository contains the implementation of the OptMetaOpenFOAM framework, including the LLM-driven workflow orchestration, CFD simulation automation, post-processing, sensitivity analysis, and parameter optimization modules.All numerical results and figures…

### doi:10.48550/arxiv.2601.03513
**Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 2) · core/scientific_computing · doi:10.48550/arxiv.2601.03513
signals: agent(?:ic)? workflows?;agentic
touchpoints: provenance_reproducibility
Open-source scientific software is abundant, yet most tools remain difficult to compile, configure, and reuse, sustaining a small-workshop mode of scientific computing. This deployment bottleneck limits reproducibility, large-scale evaluation, and the practical integration of scientific tools into modern AI-for-Science (AI4S) and agentic workflows. We present Deploy-Master, a one-stop agentic workflow for large-scale tool discovery, build…

### doi:10.5281/zenodo.14446622
**ETP4HPC SRA White Paper - Programming Environment** (2024) — HAL (Le Centre pour la Communication Scientifique Directe) · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.14446622
signals: \bcopilots?\b
touchpoints: hpc_scale_out
This is a white paper released as part of the ETP4HPC’s Strategic Research Agenda 6. High-performance computing (HPC) applications achieve extreme levels of performance on large-scale systems by utilizing a wide range of tools, including compilers, runtime/middleware, APIs for memory access, debuggers and performance profilers, as well as high-level frameworks and domain-specific languages (DSLs). Modern…

### doi:10.48550/arxiv.2607.22596
**An Agentic Orchestration of Atomistic Simulations** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2607.22596
signals: agentic;agentic*
touchpoints: provenance_reproducibility
Atomistic simulations are central to materials design, but their execution involves complex, multi-step workflows that require significant human expertise. Here, we present an agent-based system embedded within the URSA (Universal Research and Scientific Agent) framework that automates the design, execution, and validation of atomistic simulations, demonstrated using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) tool.…

### arxiv:2512.15303
**Automatic generation of input files with optimised k-point meshes for Quantum Espresso self-consistent field single point total energy calculations** (2025) — arXiv (Cornell University) · cites 0 · score 6 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2512.15303
signals: agent(?:ic)? workflows?;agentic
touchpoints: config_generation
Performing density functional theory (DFT) calculations requires a careful choice of computational parameters to ensure convergence and obtain meaningful results. This represents a particularly important problem for high-throughput and agentic workflows, where due to computational cost, any additional convergence studies are preferably to be avoided. So, there is a need for tools and models which…

### doi:10.3390/smartcities8010028
**AI Agent-Based Intelligent Urban Digital Twin (I-UDT): Concept, Methodology, and Case Studies** (2025) — Smart Cities · cites 26 · score 6 (strong 1) · core/simulation_orchestration · doi:10.3390/smartcities8010028
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
The concept of digital twins (DTs) has expanded to encompass buildings and cities, with urban building energy modeling (UBEM) playing a crucial role in predicting urban-scale energy consumption via modeling individual energy use and interactions. As a virtual model within urban digital twins (UDTs), UBEM offers the potential for managing energy in sustainable cities. However,…

### doi:10.1080/00207543.2026.2630277
**Agentic digital twins: bridging model-based and AI-driven decision-making support for a new era of supply chain and operations management** (2026) — International Journal of Production Research · cites 19 · score 6 (strong 1) · core/simulation_orchestration · doi:10.1080/00207543.2026.2630277
signals: agentic;agentic*
touchpoints: none
Agentic AI (artificial intelligence) can profoundly impact model-based decision-making support. This paper conceptualises the notion of agentic supply chain digital twins (A-SCDT) triangulating the composition of agentic AI, digital twins, and model-based optimisation and simulation. Our contribution is twofold. First, we conceptualise the A-SCDT as a distinct and novel area of practical and theoretical importance.…

### doi:10.1109/qrs-c63300.2024.00021
**Towards LLM-Enhanced Digital Twins of Intelligent Computing Center** (2024) — n/a · cites 5 · score 6 (strong 1) · core/simulation_orchestration · doi:10.1109/qrs-c63300.2024.00021
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Digital twin techniques enable the digital modeling of the power and environmental systems of intelligent computing systems. However, the traditional analysis methods of digital twins do not integrated expert experience with data-driven approaches flexibly. They also analyze the information from multiple dimensions in isolation without considering their relations. This paper proposes a large language model-enhanced…

### doi:10.1109/etfa65518.2025.11205636
**An Architecture for Integrating Large Language Models with Digital Twins and Automation Systems** (2025) — n/a · cites 4 · score 6 (strong 1) · core/simulation_orchestration · doi:10.1109/etfa65518.2025.11205636
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large Language Models (LLMs) offer flexible reasoning capability but lack physical embodiment, while traditional automation systems can execute physical processes yet lack cognitive capability. This paper presents a layered architecture that bridges this gap by integrating LLMs with digital twins and physical automation systems, with reference to practical case studies as proof of concept. The…

### doi:10.1109/mcomstd.2026.3669229
**Empowering Digital Twins With Agentic AI: Applications, Case Studies, and Limitations** (2026) — IEEE Communications Standards Magazine · cites 2 · score 6 (strong 1) · core/simulation_orchestration · doi:10.1109/mcomstd.2026.3669229
signals: agentic;agentic*
touchpoints: none
Digital Twins (DTs) are emerging as a promising paradigm because of their ability to track real-time data from the physical entity they mirror while also providing simulation capabilities. Agentic AI (AAI), a rapidly evolving branch of AI, is becoming a standard paradigm for its ability to make autonomous decisions in a dynamic environment with goal-oriented…

### doi:10.1063/5.0330986
**Vortex state transitions in deep street canyons enabled by an automated large language model workflow** (2026) — Physics of Fluids · cites 1 · score 6 (strong 1) · core/solver_control · doi:10.1063/5.0330986
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Understanding airflow dynamics and vortex state transitions in urban street canyons is crucial for evaluating urban microclimates and pollutant dispersion. Computational fluid dynamics (CFD) simulations are a key tool for assessing urban wind flow. However, the traditional manual setup of these simulations is highly time-consuming, creating a critical computational bottleneck for the large-scale parametric studies…

### doi:10.48550/arxiv.2506.05616
**Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists** (2025) — arXiv (Cornell University) · cites 1 · score 6 (strong 1) · core/computational_discovery · doi:10.48550/arxiv.2506.05616
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
We aim at designing language agents with greater autonomy for crystal materials discovery. While most of existing studies restrict the agents to perform specific tasks within predefined workflows, we aim to automate workflow planning given high-level goals and scientist intuition. To this end, we propose Materials Agent unifying Planning, Physics, and Scientists, known as MAPPS.…

### doi:10.66857/b905
**FEDERATED COGNITIVE DIGITAL TWINS FOR AUTONOMOUS AI AGENT INSIDER THREAT PREDICTION AND CONTAINMENT** (2026) — Journal of Innovative Research and Technology · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.66857/b905
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
As users have legitimate access and business environments become more autonomous with the use of AI agents, insider threats continue to be a significant problem in the cybersecurity landscape. The current detection methods typically are reactive, require centralized data collection, and have privacy protection and scalability problems. In order to solve these problems, this paper…

### doi:10.3390/su18179099
**Autonomous Circular Economy Systems: The Role of AI Agents and Digital Twins in Self-Optimizing Sustainable Business Ecosystems** (2026) — Sustainability · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.3390/su18179099
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
This study examines how autonomous digital technologies are associated with Sustainable Business Performance in circular-economy settings. Drawing on the Resource-Based View and dynamic capabilities theory, it develops a framework linking AI Agent Autonomy, Digital Twin Capability, Self-Optimization Capability, Circular Process Integration, Algorithmic Trust, and Sustainable Business Performance. Cross-sectional survey data were collected from 319 purposively…

### doi:10.32620/reks.2025.4.01
**Digital transformation of the occupational health and safety management system in civil aviation through synergetic integration of digital twin and ai agents’ technologies** (2025) — RADIOELECTRONIC AND COMPUTER SYSTEMS · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.32620/reks.2025.4.01
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
The subject of this study is the digital transformation of the occupational safety management system in civil aviation. Owing to the country’s unique geopolitical position in the centre of Eurasia, the Republic of Kazakhstan’s rapid growth in cargo and passenger traffic is associated with increasing employee risks, making it critically necessary to review existing occupational…

### doi:10.17605/osf.io/w4sc9
**Agentic Digital Twins in Health Care: A Scoping Review** (2026) — n/a · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.17605/osf.io/w4sc9
signals: agentic;agentic*
touchpoints: none
Two strands of medical artificial intelligence have developed in parallel: digital twins, which maintain a synchronized virtual model of an individual patient and predict response to care; and agentic AI, which sets subgoals, calls external tools, and acts with limited human prompting. Systems that combine both — a digital twin that acts autonomously — behave…

### doi:10.65713/ijaraiv13i1214
**DIGITAL TWIN INTELLIGENCE IN ONCOLOGY: AI-POWERED VIRTUAL PATIENTS FOR PERSONALIZED TREATMENT OPTIMIZATION** (2023) — International Journal of Advanced Research and Innovations · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv13i1214
signals: agentic
touchpoints: none
Digital twin intelligence is emerging as one of the most transformative innovations in precision oncology by creating continuously evolving virtual representations of individual cancer patients that integrate multimodal biomedical information to support personalized diagnosis, therapeutic optimization, disease monitoring, and clinical decision-making. Unlike conventional predictive models, digital twins continuously synchronize with real-world patient data, enabling dynamic…

### doi:10.5281/zenodo.20054226
**Agricultural AI Agents Can Learn from Chemical Complex System Models** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.20054226
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
Smart farms and plant factories increasingly use sensors, automatic controllers, digital twins, and artificial intelligence models. However, nutrient management remains difficult because nutrient solutions are nonlinear chemical systems coupled with plant uptake dynamics. This paper proposes a simulation-first strategy for smart-farm nutrient management agents. The proposed strategy is grounded in previous studies on ion-selective electrode…

### doi:10.65713/ijaraiv14i1208
**AI-DRIVEN PRECISION CANCER ECOSYSTEMS: FROM LIQUID BIOPSY AND RADIOMICS TO DIGITAL TWINS** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1208
signals: agentic
touchpoints: none
Precision oncology is undergoing a profound transformation through the convergence of artificial intelligence (AI), liquid biopsy, radiomics, digital pathology, multi-omics, and digital twin technologies into intelligent computational ecosystems capable of continuously modeling cancer biology across the patient journey. Conventional oncology frequently relies on fragmented diagnostic modalities and episodic clinical assessments that inadequately capture the dynamic…

### doi:10.65713/ijaraiv13i1219
**PREDICTIVE ONCOLOGY THROUGH FOUNDATION AI: INTEGRATING LONGITUDINAL CLINICAL DATA, MULTI-OMICS, AND DIGITAL TWINS** (2023) — International Journal of Advanced Research and Innovations · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv13i1219
signals: agentic
touchpoints: none
Predictive oncology is undergoing a transformative evolution through the integration of foundation artificial intelligence (AI) models, longitudinal clinical data, multi-omics technologies, and digital twin systems into comprehensive computational ecosystems capable of anticipating disease progression, therapeutic response, recurrence, and survival. Conventional oncology frequently relies on static clinical assessments and isolated molecular analyses, limiting accurate prediction of…

### doi:10.1177/10711813251369797
**VirTLab-Eval: Human-Agent Team and Digital Twin Performance Evaluation Demonstration** (2025) — Proceedings of the Human Factors and Ergonomics Society Annual Meeting · cites 0 · score 6 (strong 2) · core/simulation_orchestration · doi:10.1177/10711813251369797
signals: \bAI agents?\b;agentic
touchpoints: none
The study of human-artificial intelligence (AI) teaming (HAT) and Human Digital Twin (HDT) modeling currently faces significant challenges in accurately simulating and assessing the effectiveness of interactions between humans and AI systems. Current methods typically rely on limited real-world data or simplified simulated representations that do not capture the complexity and variability of human digital…

### doi:10.32347/2412-9933.2026.66.54-62
**Information technology for multi-agent verification of digital twins of critical infrastructure objects** (2026) — Management of Development of Complex Systems · cites 0 · score 6 (strong 2) · core/simulation_orchestration · doi:10.32347/2412-9933.2026.66.54-62
signals: \bAI agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The relevance of this study is determined by the significant number of damaged critical infrastructure facilities in Ukraine, the need for prompt assessment of their technical condition, and the implementation of intelligent decision-support tools for monitoring and post-war recovery processes. The study focuses on digital twins of infrastructure facilities, AI-agent systems, and multimodal data analysis,…

### doi:10.21227/ynmh-r675
**"Dynamic Constitutional Control of Agentic Enterprise Digital Twins via Meta-Governor Agents"** (2026) — IEEE DataPort · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.21227/ynmh-r675
signals: agentic;agentic*
touchpoints: none
"Enterprise digital twins are evolving from passive monitoring replicas into agentic, decision-capable cyber-physical intelligence layers that can observe, reason, plan, and act across complex operational ecosystems. However, as autonomy increases, static governance policies become insufficient to manage risk, drift, compliance changes, and human trust requirements. This paper proposes a Dynamic Constitutional Control (DCC) framework for…

### doi:10.65713/ijaraiv14i1210
**FUTURE CANCER INTELLIGENCE: CONVERGING FOUNDATION AI, DIGITAL TWINS, MULTIMODAL LEARNING, AND PRECISION ONCOLOGY** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1210
signals: agentic
touchpoints: none
Cancer care is entering a new era driven by the convergence of foundation artificial intelligence (AI), digital twins, multimodal learning, and precision oncology into intelligent computational ecosystems capable of continuously modeling disease biology and supporting personalized clinical decision-making. Conventional oncology frequently depends upon fragmented diagnostic workflows, isolated biomarker interpretation, and episodic therapeutic assessment that inadequately…

### doi:10.65713/ijaraiv14i1220
**AUTONOMOUS PRECISION ONCOLOGY: THE CONVERGENCE OF FOUNDATION AI MODELS, DIGITAL TWINS, AND COMPUTATIONAL CANCER INTELLIGENCE** (2024) — International Journal of Advanced Research and Innovations · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.65713/ijaraiv14i1220
signals: agentic
touchpoints: none
Autonomous precision oncology represents the next evolutionary stage of computational cancer medicine, where foundation artificial intelligence (AI) models, digital twins, multimodal learning, and computational cancer intelligence converge to create continuously adaptive clinical ecosystems capable of supporting personalized diagnosis, prognostic prediction, therapeutic optimization, and longitudinal disease management. Conventional oncology frequently relies on fragmented diagnostic workflows, episodic…

### doi:10.54660/ijaiet.2024.5.1.97-101
**Cognitive Logistics Networks: Integrating Agentic Artificial Intelligence, Blockchain, Digital Twins, and Intelligent Transport Systems for Autonomous Multi-Modal Logistics Operations** (2024) — International Journal of Artificial Intelligence Engineering and Transformation · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.54660/ijaiet.2024.5.1.97-101
signals: agentic;agentic*
touchpoints: none
Background: Contemporary Logistics Networks are currently under increasing strain due to demand volatility, geopolitical disruption and the increasing challenges of coordinating multi-modal transport operations. Current approaches to managing logistics networks employ disparate information systems and reactive decision-making techniques, which do not suffice to provide the level of resilience and efficiency required by present day commerce.…

### doi:10.48550/arxiv.2511.09964
**EnvTrace: Simulation-Based Semantic Evaluation of LLM Code via Execution Trace Alignment -- Demonstrated at Synchrotron Beamlines** (2025) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2511.09964
signals: agentic
touchpoints: none
Evaluating large language models (LLMs) for instrument control requires methods that go beyond standard, stateless algorithmic benchmarks, since the behavior of physical systems cannot be fully captured by unit tests alone. Here we introduce EnvTrace, a simulation-based method that evaluates execution traces to assess semantic code equivalence. EnvTrace is demonstrated with a beamline control-logic digital…

### doi:10.13284/j.cnki.rddl.20251502
**Social Space Governance in the Artificial Intelligence Era** (2026) — DOAJ (DOAJ: Directory of Open Access Journals) · cites 0 · score 6 (strong 2) · core/simulation_orchestration · doi:10.13284/j.cnki.rddl.20251502
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\bAI agents?\b
touchpoints: none
With the pervasive penetration of artificial intelligence (AI) technologies, traditional paradigms of social space governance are undergoing a fundamental shift—from "digital governance" to "intelligent governance." In the governance space dimension, AI innovations such as AI-generated content (AIGC) and spatial intelligence have endowed digital twin spaces with unprecedented capabilities, transforming them from static reflections of physical…

### doi:10.1108/josm-07-2026-618
**Guest editorial: Service transformation: key forces, challenges and implications** (2026) — Journal of service management · cites 0 · score 6 (strong 1) · core/simulation_orchestration · doi:10.1108/josm-07-2026-618
signals: \bAI agents?\b
touchpoints: none
Transformative changes in society and service contexts call for dedicated investigation to set future research priorities and provide guidelines for practice (Ostrom et al., 2021). The world is experiencing significant changes (McColl-Kennedy et al., 2023; Ostrom et al., 2021), from global pandemics, climate change, multiple wars, the widespread pervasiveness of digital technologies, especially artificial intelligence…

### doi:10.5281/zenodo.21548827
**# Artificial Intelligence and the Future of Engineering Education, Metallurgical Research, and Human Employment: Opportunities, Challenges, and a Sustainable Framework** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 1) · core/computational_discovery · doi:10.5281/zenodo.21548827
signals: \bAI agents?\b
touchpoints: none
## Alternative Titles ### Alternative Title 1 (Comprehensive)**"AI-Driven Transformation in Metallurgy and Engineering Education: A Roadmap for Human-AI Collaboration in Industry 5.0"** ### Alternative Title 2 (Focus on Metallurgy)**"Machine Learning, Deep Learning, and Generative AI in Metallurgical Engineering: From Microstructure Analysis to Smart Manufacturing"** ### Alternative Title 3 (Focus on Employment)**"Beyond Job Displacement: Reskilling, Upskilling,…

### arxiv:2608.03600
**Large language models for partial differential equation workflows** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/solver_control · doi:10.48550/arxiv.2608.03600
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Partial differential equations (PDEs) become actionable in science and engineering not as isolated formulae, but as executable workflows that connect modelling assumptions, governing equations, numerical solvers, diagnostics, and decisions. Large language models (LLMs) are beginning to support such workflows by linking natural language, symbolic mathematics, code, solver outputs, and feedback. Here we examine recent advances…

### title:softwaredevelopmentforscientificcomputingusingaicodegeneration
**Software Development for Scientific Computing Using AI Code Generation** (2024) — Työväentutkimus Vuosikirja · cites 0 · score 6 (strong 1) · core/scientific_computing · http://hdl.handle.net/10138/587908
signals: \bcopilots?\b
touchpoints: none
Recent advancements in artificial intelligence (AI), particularly in generative AI and large language models (LLMs), have led to widespread adoption across various applications including code generation. Our paper examines the use of LLMs like GitHub Copilot for developing complex software systems (aka. domain-specific scientific computing software), specifically through a case study involving a satellite simulation…

### doi:10.48550/arxiv.2607.15001
**LQCDMaster: Agentic Scientific Computing for Lattice Quantum Chromodynamics Research** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2607.15001
signals: agentic;agentic*
touchpoints: none
Lattice quantum chromodynamics (LQCD) provides a first-principles framework for computing hadronic observables, but its practical use remains limited by the substantial expertise required to turn research motivation into reliable computing workflows. Here we present \textsc{LQCDMaster}, a tool-augmented, skill-guided and domain-specialized scientific computing agent that converts natural-language LQCD research tasks into executable PyQUDA computing workflows, including…

### doi:10.48550/arxiv.2601.20996
**MADE: Benchmark Environments for Closed-Loop Materials Discovery** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 2) · core/computational_discovery · doi:10.48550/arxiv.2601.20996
signals: \btool[- ]use\b;agentic
touchpoints: none
Existing benchmarks for computational materials discovery primarily evaluate static predictive tasks or isolated computational sub-tasks. While valuable, these evaluations neglect the inherently iterative and adaptive nature of scientific discovery. We introduce MAterials Discovery Environments (MADE), a novel framework for benchmarking end-to-end autonomous materials discovery pipelines. MADE simulates closed-loop discovery campaigns in which an agent or…

### arxiv:2509.08269
**A Systematic Survey on Large Language Models for Evolutionary Optimization: From Modeling to Solving** (2025) — arXiv · cites 0 · score 6 (strong 1) · core/simulation_general · arXiv:2509.08269
signals: agentic
touchpoints: none
Large language models (LLMs) are increasingly integrated with evolutionary computation to support optimization tasks. This survey primarily focuses on evolutionary optimization, i.e., optimization based on evolutionary computation. For brevity, we use the term optimization throughout to denote this scope. However, existing surveys typically examine isolated roles of LLMs and do not provide a unified view…

### doi:10.48550/arxiv.2608.15073
**BOCoDe: Engineering-Centered Benchmarking for Bayesian Optimization** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · core/optimisation_uq · doi:10.48550/arxiv.2608.15073
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: optimisation_loop;provenance_reproducibility;surrogate_modelling
Bayesian optimization (BO) is a sample-efficient, surrogate-based approach to black-box optimization (BBO), but its evaluation remains dominated by synthetic functions and hyperparameter optimization (HPO) tasks that are typically low-dimensional and single-objective. Engineering design poses a substantially different regime: problems are physics-based, often high-dimensional, constrained by requirements such as cost and manufacturability, and may involve multiple…

### doi:10.48550/arxiv.2511.12063
**TextBO: Bayesian Optimization in Language Space for Eval-Efficient Self-Improving AI** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · core/optimisation_uq · doi:10.48550/arxiv.2511.12063
signals: agentic
touchpoints: optimisation_loop;surrogate_modelling
Large Language Models (LLMs) have enabled self-improving AI systems that iteratively generate, evaluate, and refine their outcomes. Recent studies show that prompt-optimization-based self-improvement can outperform state-of-the-art reinforcement-learning fine-tuning of LLMs, but performance is typically measured by generation efficiency. However, in many applications, the constraint is evaluation efficiency: obtaining reliable feedback is far more costly than…

### doi:10.26434/chemrxiv.15002556/v1
**Accelerating Proton Affinity Prediction with Multi-Fidelity Machine Learning** (2026) — ChemRxiv · cites 0 · score 5 (strong 1) · core/computational_discovery · doi:10.26434/chemrxiv.15002556/v1
signals: agentic
touchpoints: optimisation_loop;uncertainty_quantification
Accurate gas-phase proton affinities (PAs) are essential for designing proton carriers in anhydrous fuel cells, rationalizing acid-base chemistry, and guiding high-throughput molecular screening, yet the expense of high-level quantum-chemical calculations limits their routine application to large libraries. We develop a multi-fidelity ∆-learning framework that learns the systematic correction between fast PM7 semi-empirical calculations and high-fidelity…

### doi:10.1093/af/vfaf054
**Artificial intelligence for animal science: from applications to integrated knowledge systems** (2025) — Animal Frontiers · cites 3 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1093/af/vfaf054
signals: \bAI agents?\b
touchpoints: provenance_reproducibility
AI is shifting from discrete tools to a system-level integrator, requiring a holistic approach to manage farm ecosystems rather than isolated disciplines. Advanced AI transforms farms into real-time living laboratories, accelerating knowledge creation and positioning AI as a co-producer of scientific discovery. The next frontier is a multiscale vision for AI, integrating data across molecular,…

### doi:10.3390/min15040374
**Knowledge-Inference-Based Intelligent Decision Making for Nonferrous Metal Mineral-Processing Flowsheet Design** (2025) — Minerals · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.3390/min15040374
signals: knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?
touchpoints: topology_construction
With the increasing diversification of ore types and the complexity of processing techniques in the mining industry, traditional decision-making methods for mineral processing flowsheets can no longer meet the high efficiency and intelligence requirements. This paper proposes a knowledge graph-based framework for constructing a mineral-processing design knowledge base and knowledge reasoning, aiming at providing intelligent…

### doi:10.1016/j.nxmate.2026.102883
**Autonomous laboratories for sustainable nanomaterials discovery** (2026) — Next Materials · cites 0 · score 5 (strong 1) · core/computational_discovery · doi:10.1016/j.nxmate.2026.102883
signals: autonomous experimentation
touchpoints: optimisation_loop
Autonomous nanomaterials discovery is rapidly transforming conventional trial-and-error experimentation into intelligent closed-loop scientific ecosystems that integrate artificial intelligence (AI), robotics-assisted experimentation, autonomous characterization, and cyber–physical laboratory infrastructures. Unlike previous reviews that primarily focus on individual enabling technologies, this critical review presents a systems-level synthesis of autonomous nanomaterials discovery by critically evaluating AI-guided optimization, robotics-assisted synthesis,…

### doi:10.64898/2026.03.25.26349036
**Elder-Sim: A Psychometrically Validated Platform for Personality-Stable Elderly Digital Twins** (2026) — medRxiv · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.64898/2026.03.25.26349036
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: provenance_reproducibility
Abstract Background Large language models (LLMs) enable patient-facing conversational agents, creating a plausible pathway toward patient digital twins that can capture older adults’ lived experiences, beliefs, and behavioral responses across time. A central barrier to clinical-grade digital twins is personality drift—inconsistent trait expression across repeated, longitudinal interactions—which can undermine the reliability of generated trajectories and…

### doi:10.26153/tsw/62180
**X2Sim** (2025) — Texas Digital Library (University of Texas) · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.26153/tsw/62180
signals: agentic
touchpoints: hpc_scale_out
Traditional methods for modeling natural hazards such as landslides, floods, and storm surges are computationally intensive and time-consuming, thus limiting their applicability in effective disaster preparedness and response in real-world scenarios. To address this challenge, we present a novel framework, through TACC’s HPC resources, for rapidly creating digital twins that significantly reduces the time, manual…

### doi:10.1002/adem.202600008
**Ontology‐Aligned Structuring and Reuse of Multimodal Materials Data and Workflows Toward Automatic Reproduction** (2026) — Advanced Engineering Materials · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.1002/adem.202600008
signals: knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?
touchpoints: provenance_reproducibility
Reproducibility of computational results remains a challenge in materials science, as simulation workflows are often reported in unstructured text. While literature is valuable for validation and reuse, the lack of machine‐readable workflow descriptions prevents large‐scale curation and systematic comparison. Existing text‐mining approaches typically extract entities or pairwise relationships but do not capture computational workflows. An…

### arxiv:2601.12582
**Ontology-aligned structuring and reuse of multimodal materials data and workflows towards automatic reproduction** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2601.12582
signals: knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?
touchpoints: provenance_reproducibility
Reproducibility of computational results remains a challenge in materials science, as simulation workflows and parameters are often reported only in unstructured text and tables. While literature data are valuable for validation and reuse, the lack of machine-readable workflow descriptions prevents large-scale curation and systematic comparison. Existing text-mining approaches are insufficient to extract complete computational workflows…

### doi:10.5281/zenodo.20636330
**Reproducibility Meta-Analysis of Divergent GPT-4o SWE-bench Performance Driven by Evaluation Protocol Discrepancies** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.20636330
signals: agentic
touchpoints: provenance_reproducibility
As Large Language Models (LLMs) become increasingly integrated into secure software development workflows, a critical question remains unanswered: can these models not only detect insecure code but also reliably classify vulnerabilities according to standardized taxonomies? In this work, we conduct a systematic evaluation of three state-of-the-art LLMs - Llama3, Codestral, and Deepseek R1 - using…

### doi:10.18130/8gtc-p504
**Designing Complex Alloys and Oxides With Targeted Mechanical and Optical Properties Using First Principles Calculations and Machine Learning** (2026) — Libra · cites 0 · score 5 (strong 1) · core/computational_discovery · doi:10.18130/8gtc-p504
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: surrogate_modelling
The advancement of next-generation aerospace propulsion and power generation systems is fundamentally constrained by the thermal and mechanical limits of materials operating in extreme environments. This dissertation addresses these limitations by establishing integrated computational frameworks for the design of high-performance alloys and ceramic coatings, specifically focusing on refractory high-entropy alloys (RHEAs) and thermal barrier coatings…

### doi:10.5281/zenodo.22144943
**Gemini-Scientibots-AutoSciencePro5: Technical Specification, Architectural Governance & Full-Cycle Workflow Engine** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.22144943
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: provenance_reproducibility
⚡ TL;DR: AutoSciencePro5 is an autonomous workflow engine that automates the scientific research lifecycle from hypothesis generation to camera-ready LaTeX manuscript production, while enforcing a mandatory 'Organics-First' ethical constraint for health and biomedical domains. Abstract: This document defines the technical architecture, operational directives, and 4-phase workflow engine governing Gemini-Scientibots-AutoSciencePro5. Designed as an autonomous science platform,…

### doi:10.5281/zenodo.20321133
**Research Software in an Age of AI-Assisted Development: Reflections from Edinburgh** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.20321133
signals: agentic
touchpoints: provenance_reproducibility
Important: This document began as a draft vision statement prepared in advance of the “Research Software Engineering in the Age of Generative AI” workshop, March 2026. It was intended to lead to discussion in the document before and discussion in-person at the workshop, including disagreement, and refinement. The current version of the document is a…

### doi:10.48550/arxiv.2601.09749
**R-LAM: Reproducibility-Constrained Large Action Models for Scientific Workflow Automation** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2601.09749
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: provenance_reproducibility
Large Action Models (LAMs) extend large language models by enabling autonomous decision-making and tool execution, making them promising for automating scientific workflows. However, scientific workflows impose strict requirements on reproducibility, auditability, and deterministic execution, which are not satisfied by generic LLM-based agents. Unconstrained action generation can lead to silent state changes, non-deterministic executions, and irreproducible…

### title:applicationawareiopredictionandoptimizationforhpcandaiworkloads
**Application-Aware I/O Prediction and Optimization for HPC and AI Workloads** (2026) — VTechWorks (Virginia Tech) · cites 0 · score 5 (strong 1) · core/scientific_computing · https://hdl.handle.net/10919/143770
signals: agentic
touchpoints: hpc_scale_out
High-performance computing (HPC) systems are essential for executing large-scale scien- tific and artificial intelligence workloads that demand extensive parallelism across compute, storage, and memory resources. Modern systems, such as Aurora at Argonne National Lab- oratory and the exascale Frontier system at Oak Ridge National Laboratory, have significantly expanded computational and I/O capabilities. However, storage and…

### doi:10.1109/iccv51701.2025.02290
**Online Reasoning Video Segmentation with Just-in-Time Digital Twins** (2025) — arXiv · cites 2 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1109/iccv51701.2025.02290
signals: \bAI agents?\b
touchpoints: none
Reasoning segmentation (RS) aims to identify and segment objects of interest based on implicit text queries. As such, RS is a catalyst for embodied AI agents, enabling them to interpret high-level commands without requiring explicit step-by-step guidance. However, current RS approaches rely heavily on the visual perception capabilities of multimodal large language models (LLMs), leading…

### doi:10.1007/978-3-032-07638-0_10
**Towards an LLM-Powered Social Digital Twinning Platform** (2025) — Lecture notes in computer science · cites 2 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1007/978-3-032-07638-0_10
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
We present Social Digital Twinner, an innovative social simulation tool for exploring plausible effects of what-if scenarios in complex adaptive social systems. The architecture is composed of three seamlessly integrated parts: a data infrastructure featuring real-world data and a multi-dimensionally representative synthetic population of citizens, an LLM-enabled agent-based simulation engine, and a user interface that…

### doi:10.3390/electronics14244806
**A Dual Digital Twin Framework for Reinforcement Learning: Bridging Webots and MuJoCo with Generative AI and Alignment Strategies** (2025) — Electronics · cites 1 · score 5 (strong 1) · core/simulation_orchestration · doi:10.3390/electronics14244806
signals: \bAI agents?\b
touchpoints: none
Deep reinforcement learning (DRL) has shown potential for robotic training in virtual environments; however, challenges remain in bridging simulation and real-world deployment. This paper introduces an extended reinforcement learning framework that advances beyond traditional single-environment approaches by proposing a dual digital twin concept. Specifically, we suggest creating a digital twin of the robot in Webots…

### doi:10.1038/s44172-025-00583-3
**Reasoning-agent-driven process simulation, optimization, carbon accounting and decarbonization of distillation** (2026) — Communications Engineering · cites 1 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1038/s44172-025-00583-3
signals: \bAI agents?\b
touchpoints: none
Distillation is the most energy-consuming unit operation of the chemical industry, however, its decarbonization strategy necessitates laborious manual process simulation, optimization and carbon emission accounting. Here we established a reasoning agent consisting of a large language model (LLM) and an extensive tool set to automate learning material collection, process simulation, optimization and carbon emission accounting…

### doi:10.1109/eeice65049.2025.11033896
**Integrating digital twin and large language models for advanced tower crane monitoring** (2025) — n/a · cites 1 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1109/eeice65049.2025.11033896
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Traditional monitoring approaches for tower crane operational safety primarily rely on manual inspections and univariate sensor threshold alarms, which exhibit significant limitations including delayed dynamic response and insufficient risk prediction capabilities, failing to meet real-time safety requirements in complex construction scenarios. To address these challenges, this study proposes an innovative intelligent monitoring system that integrates…

### doi:10.1016/j.cjme.2025.100164
**Embodied Digital Twin driven human-centric collaborative robot behavior: Cognitive inference of action strategies** (2026) — Chinese Journal of Mechanical Engineering · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1016/j.cjme.2025.100164
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Collaborative robot interacting autonomously with human operators through flexible behavioral strategies poses a significant challenge. The lack of sufficient attention to the status of human operators during autonomous collaboration has led to safety hazards, necessitating improvements in current robot behavioral strategy research. Digital twin (DT) can establish interactive ecosystems consisting of assets and human nodes,…

### doi:10.2118/229358-ms
**Generation of Non Invasive Measurement Signals for Digital Twin Based Knee Joint Deterioration Simulating of Drilling Employers** (2025) — n/a · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.2118/229358-ms
signals: \bAI agents?\b
touchpoints: none
Abstract Drilling employers’ knee joints deteriorate while influencing and developing by high pressure underground works, with undemand health issues influence productivity and downtime. Intermediate signal for simulating deterioration processes is necessary for helping health monitoring and work planning. Using acoustic emission(AE) as testing material, this study leverages generative AI agents and innovative prompting to generate…

### title:leveragingartificialintelligenceanddistributedledgertechnologiestowardsmartandautonomousbuildings
**Leveraging Artificial Intelligence and Distributed Ledger Technologies Toward Smart and Autonomous Buildings** (2025) — VTechWorks (Virginia Tech) · cites 0 · score 5 (strong 1) · core/simulation_orchestration · https://hdl.handle.net/10919/134294
signals: \bAI agents?\b
touchpoints: none
The increasing digitization of the built environment, along with the growing demand for sustainable, resilient, and intelligent infrastructure, has led to the emergence of smart buildings as a critical domain of innovation. These buildings leverage Internet of Things (IoT) devices, building automation systems, data analytics, and artificial intelligence (AI) to optimize operations, reduce energy consumption,…

### doi:10.69997/pse.120458
**Empowering Automated Process Analysis through LLM-Based Literature Mining, Flowsheet Digitization, and Simulation** (2026) — n/a · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.69997/pse.120458
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
The chemical industry needs to transition from predominantly linear, carbon-emitting production routes to circular, carbon-reusing processes. Therefore, every current and future production process needs to be critically evaluated and potentially re-designed. Today, process design and assessment rely on detailed process simulations [1]. However, constructing these simulations remains a bottleneck, demanding a high degree of expertise…

### doi:10.1055/s-0046-1827804
**Digital Twins in Oncology: From Multimodal Data Integration to Precision Clinical Practice** (2026) — Indian journal of radiology and imaging - new series/Indian journal of radiology and imaging/Indian Journal of Radiology & Imaging · cites 0 · score 5 (strong 1) · core/simulation_orchestration · doi:10.1055/s-0046-1827804
signals: agentic
touchpoints: none
Oncology digital twins are patient-specific computational models that are built by combining electronic health records, multiomics genomic data, and diagnostic imaging to simulate individual tumor biology and predict multiple treatment-related outcomes. Conceptually originated from aerospace engineering, it has matured clinically through convergent advances in radiomics, mechanistic tumor modeling, pharmacokinetic- pharmacodynamic systems, federated machine learning, and,…

### doi:10.2118/230773-ms
**From Data to Decisions: Harnessing the Potential of Language Based AI in Drilling** (2026) — IADC/SPE International Drilling Conference and Exhibition · cites 0 · score 5 (strong 1) · core/solver_control · doi:10.2118/230773-ms
signals: agentic
touchpoints: none
Abstract This paper provides a comprehensive high-level evaluation of language based AI applications across drilling. The rapid acceleration of Large Language Models (LLMs) and emerging agentic AI systems has introduced a new class of digital capability into drilling operations. It differs fundamentally from the historical evolution of physics-based, probabilistic, and cyber-physical drilling models. AI is…

### title:advancesinnumericalpartialdifferentialequationsfromdiscretizationbasedsolverstoneuraloperators
**Advances in numerical partial differential equations: From discretization-based solvers to neural operators** (2026) — SHAREOK (University of Oklahoma; Oklahoma State University; Central Oklahoma University) · cites 0 · score 5 (strong 1) · core/solver_control · https://hdl.handle.net/20.500.14446/350594
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Accurate numerical solutions of partial differential equations (PDEs) are crucial for numerous science and engineering applications, from precision agriculture and soil moisture monitoring to fluid dynamics and inverse problems. This dissertation presents comprehensive advances in numerical PDE solution methods by bridging traditional discretization-based approaches with modern machine learning techniques. We introduce the Message Passing Finite…

### doi:10.48550/arxiv.2408.15866
**Retrieval-Augmented Instruction Tuning for Automated Process Engineering Calculations : A Tool-Chaining Problem-Solving Framework with Attributable Reflection** (2024) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · core/energy_systems · doi:10.48550/arxiv.2408.15866
signals: autonomous agents?
touchpoints: none
The current technology landscape lacks a foundational AI model for solving process engineering calculations. In this work, we introduce a novel autonomous agent framework leveraging Retrieval-Augmented Instruction-Tuning (RAIT) to enhance open, customizable small code language models (SLMs) for these calculations. By combining instruction tuned code SLMs with Retrieval-Augmented Code Generation (RACG) using external tools, the…

### arxiv:2506.11057
**STRCMP: Integrating Graph Structural Priors with Language Models for Combinatorial Optimization** (2025) — arXiv · cites 0 · score 5 (strong 1) · core/simulation_general · arXiv:2506.11057
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Combinatorial optimization (CO) problems, central to operation research and theoretical computer science, present significant computational challenges due to their NP-hard nature. While large language models (LLMs) have emerged as promising tools for CO--either by directly generating solutions or synthesizing solver-specific codes--existing approaches often neglect critical structural priors inherent to CO problems, leading to suboptimality and…

### doi:10.5281/zenodo.22149574
**Entropy Reduction in Heterogeneous Experimental Systems: A Formal Framework for AI-Driven Hardware Orchestration and Standardized Scientific Pipelines** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.22149574
signals: \bAI agents?\b
touchpoints: optimisation_loop;provenance_reproducibility;verification_regression
ORCID: https://orcid.org/0009-0003-3001-717X Entropy Reduction in Heterogeneous Experimental Systems: A Formal Framework for AI-Driven Hardware Orchestration and Standardized Scientific Pipelines Author: Luigi Usai, https://orcid.org/0009-0003-3001-717X Date: 2026-08-28 Identifier: Technical Preprint / Zenodo Upload Candidate License: Creative Commons Attribution 4.0 International (CC BY 4.0) Abstract Experimental empirical sciences are constrained by operational entropy: the exponential divergence of state…

### doi:10.1016/j.ijheatfluidflow.2026.110399
**OpenFOAMGPT 2.0: End-to-end, trustworthy automation for computational fluid dynamics** (2026) — International Journal of Heat and Fluid Flow · cites 3 · score 4 (strong 1) · core/solver_control · doi:10.1016/j.ijheatfluidflow.2026.110399
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: provenance_reproducibility;verification_regression
We propose the first multi agent framework for computational fluid dynamics that enables fully automated, end to end simulations directly from natural language queries. The approach integrates four specialized agents Pre processing, Prompt Generation, OpenFOAMGPT (simulator), and Post processing decomposing complex computational fluid dynamics workflows into collaborative components powered by large language models. Extensive validation…

### doi:10.5281/zenodo.21549377
**# Artificial Intelligence in Metallurgical Engineering: A Comprehensive Review of Applications, Challenges, and Future Direction** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/computational_discovery · doi:10.5281/zenodo.21549377
signals: autonomous experimentation
touchpoints: hpc_scale_out;optimisation_loop
## ALTERNATIVE TITLES ### Alternative Title 1 (Comprehensive)**"AI-Driven Transformation in Metallurgical Engineering: From Microstructure Analysis to Smart Manufacturing and Sustainable Production"** ### Alternative Title 2 (Process-Focused)**"Machine Learning and Deep Learning Applications Across the Metallurgical Value Chain: A Systematic Review of Materials Discovery, Process Optimization, and Quality Control"** ### Alternative Title 3 (Industry 4.0 Focus)**"Industry 4.0…

### doi:10.1093/mam/ozag053.932
**Multistep Decision Making and Experiment Planning in Automated Microscopy** (2026) — Microscopy and Microanalysis · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.1093/mam/ozag053.932
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: surrogate_modelling;uncertainty_quantification
Automation in microscopy has historically been implemented as a fixed policy workflows [1,2] or optimization problems: tune imaging conditions to maximize image quality [3], or exploration to map structure–property relationships, or navigate materials spaces of combinatorial spread and random libraries [4]. In practice, however, microscope operation rarely reduces to a single objective. Even the simple…

### doi:10.17977/um067v6i52026p3
**Leveraging Machine Learning to Discover New Solid-State Materials: Topological Insulators, Semiconductors, And Solid Electrolytes Applications (Review Article)** (2026) — Jurnal MIPA dan Pembelajarannya · cites 0 · score 4 (strong 1) · core/computational_discovery · doi:10.17977/um067v6i52026p3
signals: self[- ]driving lab
touchpoints: provenance_reproducibility;uncertainty_quantification
Machine learning is used to rapidly predict, screen, and design materials functioning in solid-state for use in a growing range of chemical spaces that are too large for traditional trial and error approaches. This article reviews how machine learning accelerates the discovery of novel solid-state materials with emphasis on three technologically important classes: topological insulators,…

### doi:10.6084/m9.figshare.31387750
**Research software consulting in the age of AI** (2026) — Figshare · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.6084/m9.figshare.31387750
signals: \bcopilots?\b
touchpoints: hpc_scale_out;provenance_reproducibility
REANNZ's Research Software Consultancy service has supported researchers across New Zealand in improving the performance, scalability, and reliability of their computational workflows on high-performance computing (HPC) systems. Through hundreds of engagements, we have seen first-hand the challenges and successes of helping researchers translate domain expertise into efficient, reproducible code.Today, however, a new force is reshaping…

### doi:10.58647/rexpo.25000109.v1
**Advancing Biomedicine Through Computing, Networks, and AI: Opportunities and Challenges** (2025) — n/a · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.58647/rexpo.25000109.v1
signals: \bAI agents?\b
touchpoints: hpc_scale_out;provenance_reproducibility
The rapid transformation of biomedicine is being propelled by the powerful convergence of high-performance computing (HPC), large-scale data integration, network-based approaches, and artificial intelligence (AI). This talk will examine how these synergistic technologies are revolutionizing biomedical research, while critically addressing their current limitations and future challenges. HPC has emerged as an essential tool for processing…

### doi:10.5281/zenodo.21938270
**Open Modeling Foundation Agent Skills Alpha Release v2026.08** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.21938270
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b
touchpoints: provenance_reproducibility;uncertainty_quantification
🚀 Initial release: Open Modeling Foundation Agent Skills for computational modeling We're excited to share an initial release of the Open Modeling Foundation Agent Skills, a community-developed collection of [Agent Skills](https://agentskills.io) for building more transparent, reviewable, and reproducible computational models. The skills augment general-purpose AI coding and research agents with methodological guidance and workflows for…

### doi:10.5281/zenodo.19375962
**NikolaBlagojevic/pyrecodes: v0.3.0** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/solver_control · doi:10.5281/zenodo.19375962
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: hpc_scale_out;solver_control
pyrecodes Release Notes [v0.3.0] - March 2026 New Features Household-Level Recovery Modeling: A new household module introduces agent-based household models (Household abstract class, R2DBuildingWithHouseholds component). Households can make relocation decisions, track displacement, and participate in the regional recovery simulation. The BuiltEnvironmentWithHouseholds system class integrates household dynamics into the main simulation loop via an observer pattern.…

### doi:10.1021/acs.jpcc.5c01790
**Accelerating Computational Modeling of Reactant Adsorption through a Combined MACE+DFT Approach: Furfural on Cu Surfaces** (2025) — The Journal of Physical Chemistry C · cites 3 · score 4 (strong 1) · core/computational_discovery · doi:10.1021/acs.jpcc.5c01790
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: hpc_scale_out
Machine learning has great potential to accelerate computational discovery of new materials and catalytic reactions but is challenging to implement with quantum chemical accuracy for diverse chemical systems. Here, we explore the pretrained foundation model MACE-MP-0, a machine-learned interatomic potential (MLIP) using the MACE architecture, as a low-cost computational method for structure relaxation prior to…

### doi:10.1109/ticps.2026.3665499
**A Verifiable Digital Twin-Aided AI (DTAI) Agent-Based Production System Framework With Causally Consistent Symbiotic Simulation** (2026) — IEEE Transactions on Industrial Cyber-Physical Systems · cites 1 · score 4 (strong 1) · core/simulation_orchestration · doi:10.1109/ticps.2026.3665499
signals: \bAI agents?\b
touchpoints: optimisation_loop
Generative AI enables agent-based smart manufacturing to achieve flexible and reactive decision-making with pre-trained models. However, AI agents remain weak in plan verification and are vulnerable to perception errors caused by dynamic environments and inconsistent Industrial Internet of Things data. These limitations critically undermine the effectiveness of AI agent planning in complex production environments. To…

### doi:10.2118/0426-0013-jpt
**Technology Focus: Completions (April 2026)** (2026) — Journal of Petroleum Technology · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.2118/0426-0013-jpt
signals: agentic
touchpoints: surrogate_modelling
_ Imagine a day where completions can be designed in less than a day with high accuracy for operation and production success, a day where completions are autonomously designed based on minimal data inputs and can self-optimize upon changes in subsurface data. The effectiveness of the design is then autonomously assessed upon completion of the…

### doi:10.3997/2214-4609.2024637030
**A Framework for Life-cycle Subsurface Uncertainty Quantification** (2024) — n/a · cites 0 · score 4 (strong 1) · core/geoenergy_subsurface · doi:10.3997/2214-4609.2024637030
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: uncertainty_quantification
Summary Taking learning from oil industry in handling subsurface uncertainties, a new LLM-based framework is proposed for life-cycle subsurface uncertainty quantification, particularly a methodology to quantify full uncertainties encompassing all conceivable geological features in both geometries and their hydro-thermal-mechanical- (bio)chemical properties, for geoenergy and secure geological storage projects.…

### doi:10.5281/zenodo.20513034
**How do you use AI to develop quality research software?** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.20513034
signals: autonomous agents?
touchpoints: provenance_reproducibility
Generative AI is changing research software development practice. Guidance remains scattered, inconsistent, and often tool-specific. This document provides a framework for discussing AI use. It focuses on research software engineering contexts and practices. It describes a spectrum of AI usage intensity. This ranges from no GenAI use to autonomous agents. The spectrum reflects context, authority,…

### doi:10.5281/zenodo.20026745
**Gavin Farrell - IDPFUN2 Training School: RDM, DOME & Reproducibility** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.20026745
signals: agentic
touchpoints: provenance_reproducibility
The IDFUN2 training school took place in Budapest, Hungary, with the week's events commencing on Monday, 4 May 2026. The programme featured sessions led by Gavin Farrell from the University of Padova and ELIXIR Italy. The training focused on the intersection of data management, artificial intelligence, reproducibility, and career development within research infrastructure in the…

### doi:10.3929/ethz-c-000799878
**ARA** (2026) — Repository for Publications and Research Data (ETH Zurich) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.3929/ethz-c-000799878
signals: agentic
touchpoints: provenance_reproducibility
Scientific peer review increasingly struggles to assess reproducibility at the scale and complexity of modern research output. Evaluating reproducibility requires reconstructing experimental dependencies, methodological choices, data flows, and result-generating procedures, which often exceeds what human reviewers can provide. Agentic Reproducibility Assessment (ARA) formalizes reproducibility assessment as a structured reasoning task over scientific documents. Given a…

### doi:10.48550/arxiv.2607.10081
**Descriptive Execution of HPC Applications and Workflows** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2607.10081
signals: agentic
touchpoints: hpc_scale_out
The means to execute and orchestrate software components has changed from human-written code to descriptive prose. In high performance computing, this transition is represented in application orchestration, workload management, and system monitoring and debugging, to name a few. The underlying means to enable descriptive definition of tasks is the use of the Large Language Model…

### arxiv:2604.24696
**NeuroClaw Technical Report** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2604.24696
signals: agentic
touchpoints: provenance_reproducibility
Agentic artificial intelligence systems promise to accelerate scientific workflows, but neuroimaging poses unique challenges: heterogeneous modalities (sMRI, fMRI, dMRI, EEG), long multi-stage pipelines, and persistent reproducibility risks. To address this gap, we present NeuroClaw, a domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research. NeuroClaw operates directly on raw neuroimaging data across formats and…

### doi:10.5281/zenodo.22119449
**Instituto Doughel Investigación digital y computación post-clásica** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.22119449
signals: \bcopilots?\b
touchpoints: provenance_reproducibility
El Instituto Doughel es un instituto de investigación digital dedicado a la computación post-clásica. Desarrollamos teoría (CGFD), plataforma tecnológica (Duqueana Core) y motores de simulación avanzada (MREI Engine) que permiten ejecutar cálculos complejos en hardware clásico con una eficiencia sin precedentes. Nuestro ecosistema integra: ‣ teoría física post-clásica • arquitectura computacional avanzada, • simulaciones de…

### doi:10.1021/acsnano.5c04200
**Artificial Intelligence for Materials Discovery, Development, and Optimization** (2025) — ACS Nano · cites 150 · score 4 (strong 1) · core/computational_discovery · doi:10.1021/acsnano.5c04200
signals: autonomous experimentation
touchpoints: none
This review highlights the recent transformative impact of artificial intelligence (AI), machine learning (ML), and deep learning (DL) on materials science, emphasizing their applications in materials discovery, development, and optimization. AI-driven methods have revolutionized materials discovery through structure generation, property prediction, high-throughput (HT) screening, and computational design while advancing development with improved characterization and autonomous…

### doi:10.3389/frai.2025.1655470
**Generative and Predictive AI for digital twin systems in manufacturing** (2025) — Frontiers in Artificial Intelligence · cites 12 · score 4 (strong 1) · core/simulation_orchestration · doi:10.3389/frai.2025.1655470
signals: agentic
touchpoints: none
The integration of Artificial Intelligence (AI) and Digital Twin (DT) technology is reshaping modern manufacturing by enabling real-time monitoring, predictive maintenance, and intelligent process optimisation. This paper presents the design and partial implementation of an AI-enabled Digital Twin System (AI-DT) for manufacturing, focusing on the deployment of Generative AI (GAI) and Predictive AI (PAI) modules.…

### doi:10.1109/pesgm52009.2025.11225814
**Residential EV Charging Co-Simulation for Distribution Powerflow Impact Analysis** (2025) — n/a · cites 1 · score 4 (strong 1) · core/simulation_orchestration · doi:10.1109/pesgm52009.2025.11225814
signals: \btool[- ]using\b
touchpoints: none
As electric vehicle (EV) adoption accelerates, residential charging will impact distribution grid infrastructure. These impacts must be quantified and compared to the case when smart charge management is implemented. This paper demonstrates a new co-simulation tool, EVI-DiST: Electric Vehicle Infrastructure–Distribution System Integration Tool which co-simulates EV charging and distribution feeder powerflow to determine distribution system…

### doi:10.26118/2782-4586-2026-543-549
**Digital Twin cities and artificial intelligence: Smart Technology management** (2026) — Journal of Monetary Economics and Management · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.26118/2782-4586-2026-543-549
signals: \bLLM[- ]?agents?\b
touchpoints: none
The article examines the integration mechanisms of digital twin cities and artificial intelligence as the basis for managing smart urban technologies. Based on the analysis of international experience (the Republic of Korea – the Seoul Smart Core project worth 841.2 billion won, Egypt – The Spine project worth 27 billion dollars, the European BLUEPRINT and…

### arxiv:2606.05050
**Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2606.05050
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to narrow material families, for want of a faithful, condition-aware catalytic simulator. We present CatDT (Catalysis Digital Twin), a self-evolving multi-agent system that builds an autonomous digital twin of a working catalyst, unifying gas-solid and liquid-solid…

### doi:10.48550/arxiv.2411.01049
**Exploratory Models of Human-AI Teams: Leveraging Human Digital Twins to Investigate Trust Development** (2024) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2411.01049
signals: \bAI agents?\b
touchpoints: none
As human-agent teaming (HAT) research continues to grow, computational methods for modeling HAT behaviors and measuring HAT effectiveness also continue to develop. One rising method involves the use of human digital twins (HDT) to approximate human behaviors and socio-emotional-cognitive reactions to AI-driven agent team members. In this paper, we address three research questions relating to…

### doi:10.1097/js9.0000000000005252
**Bridging AI and digital twins for real-time precision surgery: translating the COFFEE histopathological classifier into clinical workflows** (2026) — International Journal of Surgery · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.1097/js9.0000000000005252
signals: \bcopilots?\b
touchpoints: none
Dear Editor, We read with great interest the prospective study by Lin et al detailing COFFEE, an innovative Transformer-based AI model for classifying histological growth patterns (HGPs) in colorectal liver metastases[1]. The model’s exceptional performance (AUC up to 1.00 in prospective cohorts) and its ability to augment junior pathologists’ diagnostic accuracy by 8.8% underscore its…

### doi:10.18154/rwth-2025-08916
**Evaluating multi-use operation of battery energy storage systems in a cyber-physical energy system testbed** (2025) — RWTH Publications (RWTH Aachen) · cites 0 · score 4 (strong 1) · core/simulation_orchestration · doi:10.18154/rwth-2025-08916
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Battery Energy Storage Systems (BESS) are a promising decentralized solution for the short-term balancing of increasingly volatile generation and demand in energy systems. Flexibility requirements are driven by the rapid expansion of volatile renewable generation and the rising electrification of the mobility and heat sectors. However, available power and capacity are often used for single-use…

### arxiv:2602.11689
**A Preliminary Assessment of Coding Agents for CFD Workflows** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · core/solver_control · doi:10.48550/arxiv.2602.11689
signals: \btool[- ]using\b
touchpoints: none
We investigate the use of tool-using coding agents to automate end-to-end workflows in the open-source CFD package OpenFOAM. Building on general-purpose coding agent interfaces, we introduce a lightweight configuration that guides an agent toward tutorial reuse and log-driven repair to improve case setup and execution. We evaluate this approach on the FoamBench-Advanced benchmark, covering both…

### doi:10.1162/daed.a.995
**Scaling Physics Intelligence for the Earth's Subsurface** (2026) — Daedalus · cites 0 · score 4 (strong 1) · core/geoenergy_subsurface · doi:10.1162/daed.a.995
signals: \bAI agents?\b
touchpoints: none
The progress of AI in the last decade has come with an enormous cost: energy. Modern AI development resembles a double Ouroboros, the Greek mythological symbol of two snakes biting each other's tails. To scale AI, we must reinvent the energy system, and to reinvent the energy system, we must harness the power of AI.AI…

### doi:10.5281/zenodo.22554152
**Corridor: an AI-orchestrated repair-and-scoring pipeline for finite-element validation models** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/simulation_general · doi:10.5281/zenodo.22554152
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Validating a finite-element (FE) model — a computer simulation of a physical structure built from many small connected elements — against published crash-test data is standard practice in occupant-safety and injury-biomechanics engineering, but the workflow is largely manual: an engineer must diagnose why a model fails to run, repair it, and score the simulated response…

### doi:10.5281/zenodo.18849549
**The Journal of Open Source Software (JOSS): An open community and platform providing credit to software developers in the time of GenAI** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.18849549
signals: \bAI agents?\b
touchpoints: none
The Journal of Open Source Software (JOSS; https://joss.theoj.org) publishes short articles describing open-source research software, with over 3200 papers/software packages published since 2016. In this talk, we aim to showcase JOSS as an open source community and platform, to encourage its use by RSEs, and to discuss how JOSS considers GenAI contributions. JOSS's platform is…

### doi:10.1145/3736273.3736284
**AI for Materials Discovery** (2025) — n/a · cites 0 · score 4 (strong 1) · core/computational_discovery · doi:10.1145/3736273.3736284
signals: autonomous experimentation
touchpoints: none
Artificial Intelligence (AI) is revolutionizing materials discovery by accelerating the design, synthesis, and characterization of novel materials with targeted properties. By leveraging machine learning models trained on experimental and computational datasets, AI enables predictive design, structure-property correlation mapping, and autonomous experimentation. Recent advancements, including generative models, graph neural networks, and large language models, have enhanced…

### doi:10.11578/dc.20260422.5
**SURGE - Surrogate Unified Robust Generation Engine** (2026) — OSTI OAI (U.S. Department of Energy Office of Scientific and Technical Information) · cites 0 · score 3 (strong 1) · core/optimisation_uq · doi:10.11578/dc.20260422.5
signals: agentic
touchpoints: provenance_reproducibility;surrogate_modelling;uncertainty_quantification
SURGE is a surrogate modeling framework for scientific workflows that integrates Scientific Machine Learning (SciML) and AutoML features, uncertainty quantification (UQ), and MLOps-grade provenance in a single declarative pipeline. It unifies data generation and ingestion, an extensible registry of model adapters (classical, neural, probabilistic, and ensemble), held-out and cross-validated evaluation with UQ, automated hyperparameter optimization,…

### doi:10.1680/jcien.2026.179.5.2
**Editorial** (2026) — Proceedings of the Institution of Civil Engineers - Civil Engineering · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1680/jcien.2026.179.5.2
signals: agentic
touchpoints: surrogate_modelling;uncertainty_quantification
Digitisation in civil engineering is no longer confined to drafting boards replaced by CAD or paper records converted to PDFs; it is reshaping how we conceive, deliver and operate the systems that support modern life. Over the past three decades, the industry has progressed from isolated design tools to connected information management, with building information…

### doi:10.48550/arxiv.2606.22425
**SVGym (SciVerseGym): An Environment for Reinforcement Learning and Bayesian Optimization in Crystal Discovery** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · core/optimisation_uq · doi:10.48550/arxiv.2606.22425
signals: agent(?:ic)? workflows?
touchpoints: optimisation_loop;provenance_reproducibility
Machine-learned interatomic potentials now enable efficient atomistic evaluation for interactive materials discovery, yet closed-loop crystal search methods remain fragmented across bespoke pipelines for editing, relaxation, scoring, constraints, and bookkeeping. We introduce SciVerseGym, a Gymnasium-compatible environment for sequential crystal discovery that frames crystal design as a Markov decision process. Agents observe an atomistic structure, apply chemically…

### doi:10.5281/zenodo.17537484
**Innovative Multidisciplinary Framework for Enhancing Precision, Rigor, and Experimental Applicability in Scientific Research** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/optimisation_uq · doi:10.5281/zenodo.17537484
signals: \bAI agents?\b
touchpoints: provenance_reproducibility;uncertainty_quantification
In the contemporary landscape of scientific inquiry, the reproducibility crisis and the persistent gap between theoretical conceptualizations and experimental validations pose significant challenges to advancing knowledge across disciplines. This paper introduces the **Precision Enhancement Framework for Scientific Inquiry (PEFSI)**, a novel multidisciplinary conceptual toolset that uniquely integrates advanced mathematical modeling, sensitivity analysis, uncertainty quantification, and…

### doi:10.5281/zenodo.18409875
**Supporting Data and Code for "QUASAR: A Universal Autonomous System for Atomistic Simulation and a Benchmark of Its Capabilities"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/computational_discovery · doi:10.5281/zenodo.18409875
signals: agentic
touchpoints: uncertainty_quantification;verification_regression
This repository contains the source code, documentation, and complete benchmark outputs for QUASAR (Universal Autonomous System for Atomistic Simulation), an open-source agentic AI system designed for production-grade computational chemistry and materials science research. QUASAR autonomously orchestrates complex multi-scale atomistic workflows across diverse computational methods, including: Density Functional Theory (DFT) Machine Learning Potentials Molecular Dynamics (MD)…

### doi:10.1021/acs.jctc.5c01794
**AIQM3: Targeting Coupled-Cluster Accuracy with Semi-Empirical Speed across Seven Main-Group Elements** (2026) — Journal of Chemical Theory and Computation · cites 4 · score 3 (strong 1) · core/computational_discovery · doi:10.1021/acs.jctc.5c01794
signals: \bAI agents?\b
touchpoints: hpc_scale_out
The AIQM series of methods are successful neural network-based models that target coupled-cluster accuracy while maintaining high robustness and transferability across various tasks by leveraging Δ-learning. However, the previous AIQM1 and AIQM2 models are limited to molecular systems with four elements: H, C, N, and O, which fall short of meeting the common needs for…

### doi:10.2514/6.2026-1794
**A Probabilistic Digital Twin of UK en Route Airspace** (2026) — arXiv · cites 2 · score 3 (strong 1) · core/simulation_orchestration · doi:10.2514/6.2026-1794
signals: \bAI agents?\b
touchpoints: surrogate_modelling
This paper presents the first probabilistic Digital Twin of operational en route airspace, developed for the London Area Control Centre. The Digital Twin is intended to support the development and rigorous human-in-the-loop evaluation of AI agents for Air Traffic Control (ATC), providing a virtual representation of real-world airspace that enables safe exploration of higher levels…

### title:cognitivedigitaltwinoperatingsystemforwayfindinginverticalsmartcities
**Cognitive Digital Twin Operating System forWayfinding in Vertical Smart Cities** (2026) — RIT Scholar Works (Rochester Institute of Technology) · cites 0 · score 3 (strong 1) · core/simulation_orchestration · https://repository.rit.edu/theses/12585
signals: \bAI agents?\b
touchpoints: surrogate_modelling
Vertically complex urban environments impose elevated spatial cognitive load on pedestrians, a demand that static wayfinding infrastructure is structurally incapable of addressing. Smart cities currently lack a formal cognitive navigation operating layer for managing pedestrian movement in multi-level urban systems. This research introduces and evaluates a Cognitive Digital Twin Operating System (Cognitive OS) — a…

### doi:10.5281/zenodo.21093988
**BU250 Cross-Domain Coupled Digital Twin under B_U BU250|B_U 体系下的跨域耦合数字孪生 AI-Power-Transport-Finance-Climate Coupling, Scenario Library, Hardware Evidence, Feedback Calibration, Policy Sandbox, and Settlement-Gated Twin Standing AI-电力-交通-金融-气候耦合、情景库、硬件证据、反馈校准、政策沙盘与结算门控型孪生 standing** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.21093988
signals: \bAI agents?\b
touchpoints: solver_control
BU250 establishes Cross-Domain Coupled Digital Twin under B_U as a framework for moving digital twins beyond simulation, visualization, or predictive modeling into a reality-settlement interface. The file argues that a digital twin obtains standing only when it preserves the correct object boundary, retains cross-domain semantic fidelity, accepts hardware-grade evidence, exposes residuals, absorbs real-world feedback, supports…

### doi:10.5281/zenodo.20492207
**Autonomous Procurement Systems for Resilient Global Supply Networks** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.20492207
signals: agentic
touchpoints: optimisation_loop
Abstract Global supply chains are increasingly exposed to disruptions arising from geopolitical conflicts, trade sanctions, climate-related events, logistics bottlenecks, supplier financial instability, and evolving ESG requirements. Traditional procurement systems remain largely reactive, relying on periodic supplier assessments, static risk scoring mechanisms, and fragmented decision-making processes that are insufficient for managing modern multi-tier supply networks. This…

### doi:10.3997/2214-4609.202637011
**Deep Learning Surrogate Models for Multiscale, Time-Dependent Heat Transport in Geothermal Reservoirs** (2026) — n/a · cites 0 · score 3 (strong 1) · core/geoenergy_subsurface · doi:10.3997/2214-4609.202637011
signals: agentic
touchpoints: surrogate_modelling
Summary Artificial Intelligence (AI) and Machine Learning (ML) allow computers to learn patterns from data. Artificial intelligence and machine learning provide a data-driven alternative to traditional numerical simulation for complex, nonlinear systems governed by partial differential equations [ 1 ]. In subsurface geothermal reservoirs, heat transport is controlled by heterogeneous geological properties such as porosity…

### doi:10.5281/zenodo.21317865
**PacisClassPass Load Generation and Verification Bundle: Reproducibility Software for a Custom Classroom Engagement Platform** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.21317865
signals: agentic
touchpoints: provenance_reproducibility
Reproducibility software supporting the study Agentic AI in Higher Education: Building a Custom Classroom Engagement Platform Through AI-Assisted Software Engineering (Pacis, 2026, under review at Educational Technology & Society). This bundle contains the load-generation, verification, and plotting scripts used to reproduce every numerical claim in §4 and §7 of the paper. It consumes the companion…

### doi:10.5281/zenodo.22102620
**BLOCK VECTOR Research Map** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/scientific_computing · doi:10.5281/zenodo.22102620
signals: \bAI agents?\b
touchpoints: provenance_reproducibility
BLOCK VECTOR Research Map The BLOCK VECTOR Research Map is a visual guide to the Stable Authority Boundary (SAB), its formalization, core principles, applications, and related research. The collection examines a common systems problem: a machine, AI agent, autonomous system, or distributed system may remain technically capable of acting even when the authority, evidence, conditions,…

### doi:10.1109/e-cargo65996.2025.11139170
**From Digital Twin to Digital Twin Agent** (2025) — n/a · cites 5 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1109/e-cargo65996.2025.11139170
signals: \bAI agents?\b
touchpoints: none
Digital Twin (DT), as a key technology for Industry 4.0 and smart manufacturing, demonstrates significant potential in improving industrial efficiency through simulating physical entities and integrating real-time data analysis. However, existing digital twin systems still have limitations in responding to dynamic environments, providing real-time feedback, and making adaptive decisions. This paper reviews the development of…

### doi:10.1007/s10270-025-01306-0
**AI simulation by digital twins: systematic survey, reference framework, and mapping to a standardized architecture** (2025) — Software & Systems Modeling · cites 5 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1007/s10270-025-01306-0
signals: \bAI agents?\b
touchpoints: none
Insufficient data volume and quality are particularly pressing challenges in the adoption of modern subsymbolic AI. To alleviate these challenges, AI simulation uses virtual training environments in which AI agents can be safely and efficiently developed with simulated, synthetic data. Digital twins open new avenues in AI simulation, as these high-fidelity virtual replicas of physical…

### doi:10.1145/3652620.3688253
**AI Simulation by Digital Twins: Systematic Survey of the State of the Art and a Reference Framework** (2024) — n/a · cites 4 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1145/3652620.3688253
signals: \bAI agents?\b
touchpoints: none
Insufficient data volume and quality are particularly pressing challenges in the adoption of modern subsymbolic AI. To alleviate these challenges, AI simulation recommends developing virtual training environments in which AI agents can be safely and efficiently developed. Digital twins open new avenues in AI simulation, as these high-fidelity virtual replicas of physical systems are equipped…

### doi:10.2514/6.2026-1793
**A Framework for Assuring the Accuracy and Fidelity of an AI-Enabled Digital Twin of en Route UK Airspace** (2026) — n/a · cites 1 · score 3 (strong 1) · core/simulation_orchestration · doi:10.2514/6.2026-1793
signals: \bAI agents?\b
touchpoints: none
Digital Twinning combines simulation, operational data and Artificial Intelligence (AI), and has the potential to bring significant benefits across the aviation industry. Project Bluebird, an industry-academic collaboration, has developed a probabilistic Digital Twin of en route UK airspace as an environment for training and testing AI Air Traffic Control (ATC) agents. Whilst the primary research…

### doi:10.3389/frai.2026.1715883
**Digital twin simulations of theory-driven crisis messaging during hurricane evacuations in synthetic populations: a Miami-Dade County case study** (2026) — Frontiers in Artificial Intelligence · cites 1 · score 3 (strong 1) · core/simulation_orchestration · doi:10.3389/frai.2026.1715883
signals: agentic
touchpoints: none
Background Digital twin and agentic artificial intelligence technology provide innovative systems for testing behavioral science theory, which can improve emergency communication in crisis situations. More advanced and effective evidence-based messaging is needed for better safety preparation for extreme weather and more trusted evacuation communication. Methods This study developed a digital twin of Miami-Dade County populated…

### doi:10.1201/9781003657804-8
**Intelligent Digital Twins and Ethical Decision-Making Support** (2026) — Auerbach Publications eBooks · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1201/9781003657804-8
signals: \bAI agents?\b
touchpoints: none
Digital Twins as virtual representation of physical objects and processes can influence both the development and runtime behavior of Cyber-Physical Systems. The concept of Intelligent Digital Twins aims to leverage both the frequency of synchronizing with the physical environment and the fidelity of informed behavior decisions. The basic capability of Intelligent Digital Twin models to…

### doi:10.1117/12.2664301
**AI on digital twin of facility captured by reality scans** (2023) — n/a · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.1117/12.2664301
signals: \bAI agents?\b
touchpoints: none
The power of artificial intelligence (AI) coupled with optimization algorithms can be linked to data-rich digital twin models to perform predictive analysis to make better informed decisions about installation operations and quality of life for the warfighters. In the current research, we developed AI connected lifecycle building information models through the creation of a data…

### doi:10.4018/979-8-3373-2797-6.ch005
**Enhancing IoT-Based Smart Farming With Digital Twin and XR** (2025) — n/a · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.4018/979-8-3373-2797-6.ch005
signals: \bAI agents?\b
touchpoints: none
The convergence of Internet of Things (IoT), LoRaWAN, Digital Twin (DT), and Extended Reality (XR) is transforming smart farming, especially in resource-constrained regions. This chapter proposes an integrated system that combines LoRaWAN-based soil sensors, edge gateways, a cloud-synchronized Digital Twin, and an XR interface for immersive monitoring and control. Real-time environmental data is visualized through…

### doi:10.64751/ajaccm.2024.v4.n3.pp30-34
**DIGITAL TWIN–DRIVEN 6G CAMPUS NETWORKS: INTELLIGENT FAULT RECOVERY AND ENERGY OPTIMIZATION** (2024) — American Journal of AI Cyber Computing Management · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.64751/ajaccm.2024.v4.n3.pp30-34
signals: agentic
touchpoints: none
This paper puts forward a framework for Digital Twin–driven 6G campus networks that are both private and autonomous and are supported by the convergence of agentic AI and Service Management and Orchestration (SMO) models to facilitate self-managing operations. The new network system uses the concept of digital twins for the purposes of intelligently forecasting faults…

### doi:10.48550/arxiv.2603.17420
**From Digital Twins to World Models:Opportunities, Challenges, and Applications for Mobile Edge General Intelligence** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.48550/arxiv.2603.17420
signals: agentic
touchpoints: none
The rapid evolution toward 6G and beyond communication systems is accelerating the convergence of digital twins and world models at the network edge. Traditional digital twins provide high-fidelity representations of physical systems and support monitoring, analysis, and offline optimization. However, in highly dynamic edge environments, they face limitations in autonomy, adaptability, and scalability. This paper…

### doi:10.66408/abc2.2026.55
**From Games to Smart Cities: How Game Engine Technology Became the Backbone of Urban Digital Twins?** (2026) — ABC2 Journal of Architecture Building Construction and Cities · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.66408/abc2.2026.55
signals: \bAI agents?\b
touchpoints: none
This paper investigates the accelerating convergence between the game design industry and the smart city digital twin platforms that are governing the world's most complex urban environments (Deng et al., 2021, Abdelrahman et al., 2025). Building directly upon prior empirical work examining Shanghai's city-scale digital twin implementation (Najafi, 2025) and the multi-scalar Urban Operating System…

### doi:10.21125/edulearn.2025.2312
**APPLICATION OF THE PROBLEM-BASED LEARNING (PBL) METHODOLOGY TO THE USE OF "DIGITAL TWINS" AND ARTIFICIAL INTELLIGENCE (AI) FOR THE FREELANCE CONSULTING SERVICES SECTOR** (2025) — EDULEARN proceedings · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.21125/edulearn.2025.2312
signals: \bAI agents?\b
touchpoints: none
[EN] Artificial intelligence is progressing beyond the automation of isolated tasks to the creation of digital twins (DT) of human experts. In this context, a digital twin is an AI-driven virtual representation of a person's knowledge, skills, and even personality, capable of performing tasks in a way similar to its human counterpart. Initially, the term…

### doi:10.24158/tipor.2026.5.3
**“Avatarization” of Library and Information Services (How a Fairy Tale Came True)** (2026) — Теория и практика общественного развития · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.24158/tipor.2026.5.3
signals: \bAI agents?\b
touchpoints: none
This article presents an analysis of the problem of modeling and using digital twins (avatars) in library and information services (LIS). Based on a terminological analysis of the concepts of “avatar”, “cyberphysical system” (CFS), “virtual librarian”, and “digital twin”, the following conceptual models are proposed: a) the digital twin of a librarian; c) the integration…

### doi:10.5281/zenodo.21196189
**MineProductivity** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.5281/zenodo.21196189
signals: \bAI agents?\b
touchpoints: none
MineProductivity v1.0.0 - Enterprise Architecture Platform This release marks the completion of the core enterprise architecture for MineProductivity. The platform now defines a complete, layered, enterprise-grade architecture for mining productivity analytics, KPI management, Digital Twin, and Decision Intelligence. This is an architecture milestone. It establishes the reference architecture that will guide all future implementation. Highlights…

### doi:10.3390/heritage9060233
**Towards Heritage World Models** (2026) — Heritage · cites 0 · score 3 (strong 1) · core/simulation_orchestration · doi:10.3390/heritage9060233
signals: agentic
touchpoints: none
Digital twins have become a central paradigm for cultural heritage documentation, monitoring, and preventive preservation. Yet, when cultural heritage systems promise prediction, simulation, intervention planning, and decision support, a more explicit account is needed of the computational commitments behind such claims. This position paper proposes the notion of the heritage world model as a conceptual…

### doi:10.5281/zenodo.20716327
**Boundary Conditions as Dynamical Variables: How Hagedorn Transitions, Quantum Post-Selection, Stochastic Inflation, Phantom Scalar Cosmology, and Gravitational Superfluorescence Jointly Suggest a Candidate Framework for Boundary-Induced Phase Reorganization in Gravitational Systems** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/solver_control · doi:10.5281/zenodo.20716327
signals: agentic
touchpoints: none
Version 2 — revised in response to an external structural review and an automated critique pass. See "Response to Review" appendix in the PDF for the change log. A recurring structural motif appears across several recent preprints in hep-th and gr-qc: systems whose macroscopic behavior is reorganized not by bulk dynamics alone, but by the…

### doi:10.5281/zenodo.20688774
**Boundary Conditions as Dynamical Variables: How Scalar Clouds, Robin Boundaries, Hagedorn Transitions, Stochastic Open Systems, Quantum Post-Selection, Entanglement Harvesting, and a Fluctuating Wall Jointly Suggest a Candidate Framework for Boundary-Mediated Phase Transitions in Curved Spacetime** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · core/solver_control · doi:10.5281/zenodo.20688774
signals: agentic
touchpoints: none
Version 2 — revised in response to an external structural review and an automated critique pass. See "Response to Review" appendix in the PDF for the change log. A recurring structural pattern across several recent preprints in hep-th and gr-qc suggests that **boundary conditions**, rather than bulk dynamics alone, act as primary control parameters for…

### arxiv:2607.08043
**Aleena: Alignment Agent for Research Software Engineering Collaborations** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · core/scientific_computing · doi:10.48550/arxiv.2607.08043
signals: agentic
touchpoints: none
Research software collaborations span meetings, informal chats, pull requests, and GitHub issues. A decision surfaced in a Slack thread, refined in a meeting, and implemented in a pull request can lose its original rationale across these artifacts, leaving domain researchers and research software engineers with divergent mental models of project intent, ownership, and scientific assumptions.…


## Periphery (counted, not deep-read) — 421

### doi:10.5281/zenodo.19919086
**Replication materials for the paper "Engineering LLM-Based Multi-Agent Systems: A Taxonomy of Emerging Frameworks"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 36 (strong 9) · periphery/science_of_science · doi:10.5281/zenodo.19919086
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|sma
touchpoints: none
This document describes the methodology used to identify, filter, and analyze gray literature following the multi-vocal study approach and established guidelines for systematic and tertiary studies in software engineering [1]. The study considers both white and gray literature. In addition, repositories are selected based on GitHub popularity metrics. The methodology is structured into three main…

### doi:10.5281/zenodo.19614868
**Autonomous AI Agents and Task Planning** (2024) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 26 (strong 7) · periphery/software_engineering · doi:10.5281/zenodo.19614868
signals: \bAI agents?\b;\bAI agents?\b*;\bAutoGPT\b;\bCrewAI\b;\bLangGraph\b;\bReAct\b;\btool[- ]use\b;autonomous agents?
touchpoints: none
Autonomous AI agents -- systems that perceive their environment, plan sequences of actions, use tools, and executemulti-step tasks with minimal human intervention -- represent a qualitative shift from AI as a prediction engine to AI as anactive participant in complex workflows. Powered by large language models with tool use capabilities, agents can browsethe web, write…

### doi:10.5281/zenodo.21478165
**Agentic AI in Enterprise Software Engineering: Multi-Agent Frameworks for Autonomous Development Workflows** (2026) — International Journal of Intelligent Systems and Applications in Engineering · cites 0 · score 22 (strong 5) · periphery/software_engineering · doi:10.5281/zenodo.21478165
signals: \bLangGraph\b;agent orchestration;agentic;agentic*;model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platf
touchpoints: tool_exposure
Software engineering organizations face a persistent productivity constraint: the routine cognitive and coordination tasks that constitute a substantial portion of development effort — code review, test generation, documentation, sprint planning, and incident triage — consume engineering attention that organizations would prefer to allocate toward design and innovation. Agentic AI systems, which combine large language model…

### arxiv:2510.09721
**A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System** (2025) — arXiv · cites 0 · score 19 (strong 4) · periphery/software_engineering · arXiv:2510.09721
signals: \bLLM[- ]?agents?\b;agentic;agentic*;autonomous agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The integration of Large Language Models (LLMs) into software engineering has driven a transition from traditional rule-based systems to autonomous agentic systems capable of solving complex problems. However, systematic progress is hindered by a lack of comprehensive understanding of how benchmarks and solutions interconnect. This survey addresses this gap by providing the first holistic analysis…

### doi:10.25394/pgs.32101480
**Scaling Language Intelligence: From Foundation Models to Agentic Systems** (2026) — Purdue · cites 0 · score 18 (strong 3) · periphery/software_engineering · doi:10.25394/pgs.32101480
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bToT\b;agentic;agentic*
touchpoints: none
Foundation models have achieved remarkable progress across natural language processing, computer vision, and multimodal learning. In particular, large-scale language models exhibit strong capabilities in zero- and few-shot learning, multi-step reasoning, and tool-assisted problem solving. Despite these advances, several limitations continue to hinder their full potential in both single-step inference and long-horizon reasoning. This thesis presents…

### doi:10.65222/viral.2026.7.40.60
**From ChatGPT to Autonomous Agents: A Systematic Literature Review and Bibliometric Analysis of Agentic Artificial Intelligence in Organizations** (2026) — International Journal of Education Leadership Artificial Intelligence Computing Business Life Sciences and Society · cites 0 · score 18 (strong 3) · periphery/science_of_science · doi:10.65222/viral.2026.7.40.60
signals: agentic;agentic*;autonomous agents?;autonomous agents?*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The rapid diffusion of generative artificial intelligence has altered the technological and organizational landscape, shifting scholarly and managerial attention from systems primarily designed to generate content toward increasingly autonomous systems capable of planning, reasoning, coordinating actions, and pursuing goals with limited human intervention. This transition has given rise to the concept of agentic artificial intelligence,…

### doi:10.1109/access.2026.3652325
**Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review** (2026) — IEEE Access · cites 4 · score 17 (strong 4) · periphery/software_engineering · doi:10.1109/access.2026.3652325
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*;autonomous agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0
touchpoints: none
The development of agentic software engineering (ASE) is shifting the software development process, specifically by adopting autonomous agents into the fundamental software development process, where autonomous agents using large language models (LLMs) and artificial intelligence (AI) make decisions, write code, and collaborate across the entire software development lifecycle. The systematic review is a summary of…

### doi:10.30574/wjarr.2025.25.3.0887
**Agentic workflows for end-to-end software engineering automation** (2025) — World Journal of Advanced Research and Reviews · cites 0 · score 17 (strong 3) · periphery/software_engineering · doi:10.30574/wjarr.2025.25.3.0887
signals: \bAI agents?\b;agent(?:ic)? workflows?;agent(?:ic)? workflows?*;agentic;agentic*
touchpoints: none
With the rise of large language models (LLMs) and independent AI systems, software engineering is undergoing a transformational shift. This conceptual paper theorizes agentic workflows systems, where an AI agent or agents proactively perceive, plan, act and reflect throughout the entire software development lifecycle (SDLC); its implications for end to end software engineering automation are…

### doi:10.1109/satc69565.2026.11542535
**Agentic Code Review: A Multi-Agent Framework with Meta-Cognitive Reflection and Human-in-the-Loop Alignment** (2026) — n/a · cites 0 · score 17 (strong 3) · periphery/software_engineering · doi:10.1109/satc69565.2026.11542535
signals: \bLangGraph\b;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Automated code review remains a persistent challenge in software engineering. Traditional static analysis tools depend on rigid pattern matching and produce excessive false positives, while large language model (LLM)-based approaches frequently hallucinate findings that reference nonexistent code. This paper presents a multi-agent framework that addresses both limitations through orchestrated specialization and adversarial self-verification. The proposed…

### doi:10.51583/ijltemas.2026.150700076
**Repogent: An Autonomous Multi-Agent System for End-To-End Repository Maintenance** (2026) — International Journal of Latest Technology in Engineering Management & Applied Science · cites 0 · score 17 (strong 4) · periphery/software_engineering · doi:10.51583/ijltemas.2026.150700076
signals: \bAI agents?\b;agent orchestration;agent(?:ic)? workflows?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Maintaining open-source repositories demands continuous attention to issue triage, code review, build monitoring, and community support—tasks that overwhelm individual maintainers when existing automation tools operate in isolation without shared context. Static analyzers check code quality, CI/CD systems run automated tests, and simple bots handle basic labeling, yet none of these tools share information with each…

### doi:10.5281/zenodo.22124312
**Intelligent Multi-Agent AI System with Predictive Analysis** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 17 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.22124312
signals: \bAI agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]
touchpoints: none
Efficient code review procedures are essential in modern software development in order to guarantee software quality, security, and maintainability. Traditional approaches to code review are usually time-consuming, rely on the expertise of the reviewers, and are unable to give thorough feedback with respect to a range of quality aspects. While static analysis tools can detect…

### doi:10.48550/arxiv.2606.28791
**From Determinism to Delegation: AI-Native Software Engineering and the Evolution of the Agentic Engineer** (2026) — arXiv (Cornell University) · cites 0 · score 17 (strong 4) · periphery/software_engineering · doi:10.48550/arxiv.2606.28791
signals: \btool[- ]use\b;agent(?:ic)? workflows?;agentic;agentic*;autonomous agents?
touchpoints: none
Software engineering is experiencing its most significant transformation since the emergence of high-level programming languages. As large language models (LLMs) increasingly enable sustained, multi-step, tool-mediated execution, engineering value is shifting from writing deterministic code to supervising probabilistic and autonomous behavior. This paper argues that AI-Native Software Engineering is a paradigm shift rather than a mere…

### title:agentscriptautonomousllmbasedagentforcomputeruseviaapplescript
**AgentScript autonomous LLM-based agent for computer use via AppleScript** (2026) — DR-NTU (Nanyang Technological University) · cites 0 · score 17 (strong 3) · periphery/interface_agents · https://hdl.handle.net/10356/214255
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Computer Use Agents (CUAs) that operate graphical user interfaces (GUIs) have become an active research frontier, with state-of-the-art vision-based systems achieving up to 72.1% on the OSWorld benchmark [1]. However, vision- based control suffers from fundamental limitations: brittle visual grounding [2], high inference latency, and prohibitive token costs from accumulating high- resolution screenshots across agent…

### doi:10.5281/zenodo.21716412
**Extended data for: An ontology of normative role design for LLM agent interactions in multi-agent systems** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 17 (strong 3) · periphery/science_of_science · doi:10.5281/zenodo.21716412
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|c
touchpoints: none
This dataset is the extended data accompanying the research article “An ontology of normative role design for LLM agent interactions in multi-agent systems” (Hassan Nejad, Braga de Vasconcelos & Hooshyar). It documents the systematic literature review and the ontology through which the study’s findings were produced. The study develops a conceptual ontology for examining how…

### doi:10.64898/2026.07.30.26359375
**A PRISMA-Aligned Agentic Framework for Medical Systematic Reviews and Evidence Synthesis** (2026) — medRxiv · cites 0 · score 16 (strong 4) · periphery/science_of_science · doi:10.64898/2026.07.30.26359375
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|sma
touchpoints: none
Medical systematic reviews are central to evidence-based medicine, but they remain slow, labor-intensive, and difficult to maintain under the full Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) workflow. Recent LLM-based deep research agents offer a promising route to addressing this challenge, yet reliable deployment in medical systematic reviews remains limited by insufficient clinical…

### doi:10.1016/j.acags.2026.100362
**An LLM-based multi-agent system for geoscience legacy document processing, knowledge extraction and quality control** (2026) — Applied Computing and Geosciences · cites 2 · score 15 (strong 3) · periphery/science_of_science · doi:10.1016/j.acags.2026.100362
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;model context protocol;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|plat
touchpoints: tool_exposure
Knowledge extraction from unstructured Earth Science documents into standardized knowledge bases is a complex task that used to be heavily reliant on manual curation and domain expertise. As an effort to automate this process, we proposed a modularized multi-agent system framework, Adaptive Geo Knowledge Extraction (AGeoKE), that leverages Large Language Models (LLMs) to automatically extract…

### arxiv:2603.01327
**SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2603.01327
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: provenance_reproducibility
Large language models (LLMs) exhibit strong performance on self-contained programming tasks. However, they still struggle with repository-level software engineering (SWE), which demands (1) deep codebase navigation with effective context management for accurate localization, and (2) systematic approaches for iterative, test-driven code modification to resolve issues. To address these challenges, we propose SWE-Adept, an LLM-based two-agent…

### doi:10.1109/isqed65160.2025.11014463
**EDA-Debugger: An LLM-Based Framework for Automated EDA Runtime Issue Resolution** (2025) — n/a · cites 3 · score 15 (strong 2) · periphery/software_engineering · doi:10.1109/isqed65160.2025.11014463
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The increasing complexity of integrated circuits (ICs) poses significant challenges for Electronic Design Automation (EDA) tools and users. Debugging EDA runtime issues can be time-consuming and frustrating due to complex error messages, extensive documentation, and limited knowledge sharing. Although open-source EDA tools like OpenROAD and OpenLane have democratized chip design, the dependence on expert knowledge…

### doi:10.48550/arxiv.2504.17934
**Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents** (2025) — arXiv (Cornell University) · cites 1 · score 15 (strong 3) · periphery/interface_agents · doi:10.48550/arxiv.2504.17934
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The rise of Large Language Models (LLMs) has revolutionized Graphical User Interface (GUI) automation through LLM-powered GUI agents, yet their ability to process sensitive data with limited human oversight raises significant privacy and security risks. This position paper identifies three key risks of GUI agents and examines how they differ from traditional GUI automation and…

### doi:10.48550/arxiv.2607.09101
**Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2607.09101
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:syste
touchpoints: none
Recently, the emergence of Large Language Models (LLMs) has spurred a surge of research into automated unit test generation, yielding impressive performance and reducing manual effort. However, existing LLM-based approaches still suffer from two major limitations: (1) they follow rigid, procedural workflows that underutilize the autonomous reasoning potential of LLMs, making it difficult to dynamically…

### arxiv:2604.26275
**Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 3) · periphery/software_engineering · doi:10.48550/arxiv.2604.26275
signals: \bcopilots?\b;\btool[- ]use\b;agentic;agentic*
touchpoints: none
The arrival of large language models (LLMs) capable of multi-step reasoning, tool use, and long-horizon planning has produced a qualitative shift in software engineering. Where earlier code-completion tools such as GitHub Copilot operated at the granularity of a line or function, modern agentic systems -- Claude Code, OpenAI Codex CLI, Google Jules, Devin, OpenHands, SWE-agent,…

### doi:10.48550/arxiv.2602.22764
**Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents** (2026) — arXiv (Cornell University) · cites 0 · score 15 (strong 3) · periphery/software_engineering · doi:10.48550/arxiv.2602.22764
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The Rust programming language presents a steep learning curve and significant coding challenges, making the automation of issue resolution essential for its broader adoption. Recently, LLM-powered code agents have shown remarkable success in resolving complex software engineering tasks, yet their application to Rust has been limited by the absence of a large-scale, repository-level benchmark. To…

### doi:10.1145/3803437.3806428
**TestAgent: A Multi-Agent LLM Framework for Repository-Level Unit Test Generation** (2026) — n/a · cites 0 · score 14 (strong 2) · periphery/software_engineering · doi:10.1145/3803437.3806428
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:syste
touchpoints: verification_regression
Automated unit test generation plays a critical role in maintaining software quality, yet existing LLM-based tools often struggle with limited repository-level context and rigid generation workflows. In this paper, we present TestAgent, a multi-agent tool implemented as a VS Code extension that automates the generation of high-quality unit tests for Java projects using repository-level Code…

### doi:10.5281/zenodo.20671187
**System-Level Impact Analysis for Microservice CI/CD via Cross-Repository Dependency Graphs** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 14 (strong 4) · periphery/software_engineering · doi:10.5281/zenodo.20671187
signals: \bLangGraph\b;\bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);agentic;orchestrat\w+ agents?
touchpoints: tool_exposure
Single-repository quality gates are blind to distributed system failures. A pull request that changes a REST endpoint signature can pass all local CI checks and unit tests while silently breaking three downstream consumer services in other repositories — failures that remain invisible until deployment. This paper presents the K11tech Microservice QA System (k11techlab-microservice-qa-system), a LangGraph-orchestrated…

### title:theadoptionandimpactofagenticaiinsoftwareengineeringacasestudyattrimble
**The adoption and impact of agentic AI in software engineering — A case study at trimble** (2026) — Aaltodoc (Aalto University) · cites 0 · score 14 (strong 3) · periphery/software_engineering · https://aaltodoc.aalto.fi/handle/123456789/144510
signals: agent(?:ic)? workflows?;agentic;agentic*;autonomous agents?
touchpoints: none
The use of AI tools has gained interest since the release of ChatGPT in late 2022. Advancements in Large Language Models and AI infrastructure have enabled agentic AI workflows. Experimentation with agentic tools and workflows is ongoing in the industry, with no clear consensus, as software engineering teams try to understand their capabilities or limitations.…

### doi:10.48550/arxiv.2601.19138
**AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection** (2026) — arXiv (Cornell University) · cites 0 · score 14 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2601.19138
signals: agentic;agentic*;autonomous agents?;autonomous agents?*
touchpoints: none
Secure code review is critical during pre-integration, where Atlassian developers rely on lightweight analysis tools, while deep security assessment is deferred to later stages, delaying feedback and increasing remediation costs. Existing static analyzers are often noisy and struggle with context-dependent or partially manifested vulnerabilities, while static large language model (LLM) reviewers are constrained by context…

### doi:10.5281/zenodo.20931332
**Supplementary material for "A Survey of Web-of-Agents Interoperability: From Multi-Agent Systems and Semantic Web Agents to LLM-Based Agent Protocols"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 14 (strong 2) · periphery/interface_agents · doi:10.5281/zenodo.20931332
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Supplementary material for the survey "A Survey of Web-of-Agents Interoperability: From Multi-Agent Systems and Semantic Web Agents to LLM-Based Agent Protocols" (Petrova, Bliznioukov, State; SEDAN Group, SnT, University of Luxembourg). Contents: the manuscript's 152-entry bibliography; a per-entry inclusion/exclusion log for all 206 screened candidates (152 included, 54 excluded); the OpenAlex bibliometric query design (ten queries),…

### doi:10.1109/icse55347.2025.00157
**RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (2025) — arXiv (Cornell University) · cites 87 · score 13 (strong 2) · periphery/software_engineering · doi:10.1109/icse55347.2025.00157
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces Repair Agent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a…

### doi:10.1145/3715754
**Demystifying LLM-Based Software Engineering Agents** (2025) — Proceedings of the ACM on software engineering. · cites 73 · score 13 (strong 2) · periphery/software_engineering · doi:10.1145/3715754
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe…

### doi:10.1145/3803418
**Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation** (2026) — ACM Transactions on Software Engineering and Methodology · cites 2 · score 13 (strong 2) · periphery/software_engineering · doi:10.1145/3803418
signals: \bLLM[- ]?agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*
touchpoints: none
Unit testing plays a critical role in ensuring software correctness. However, writing unit tests manually is labor-intensive, especially for strongly typed languages like Java, motivating the need for automated approaches. Traditional methods primarily rely on search-based or randomized algorithms to generate tests that achieve high code coverage and produce regression oracles, which are assertions derived…

### doi:10.48448/y53c-za56
**TDFlow: Agentic Workflows for Test Driven Development** (2026) — Underline Science Inc. · cites 0 · score 13 (strong 2) · periphery/software_engineering · doi:10.48448/y53c-za56
signals: agent(?:ic)? workflows?;agent(?:ic)? workflows?*;agentic;agentic*
touchpoints: none
We introduce TDFlow, a novel test-driven agentic workflow that frames repository-scale software engineering as a test-resolution task, specifically designed to solve human-written tests. Given a set of tests, TDFlow repeatedly proposes, revises, and debugs repository-scale patches using precisely engineered sub-agents and tightly constrained tools. The workflow decomposes software engineering program repair into four components governed…

### doi:10.1109/access.2026.3713401
**Self-Evolving AI Agents With Dual Memory for Automated Software Testing and Bug Localization** (2026) — IEEE Access · cites 0 · score 13 (strong 2) · periphery/software_engineering · doi:10.1109/access.2026.3713401
signals: \bAI agents?\b;\bAI agents?\b*;autonomous agents?
touchpoints: none
Large Language Model (LLM)-based autonomous agents have shown significant promise in automating software engineering tasks, yet existing systems still suffer from two fundamental limitations: i) the lack of persistent experiential knowledge across debugging sessions, which forces agents to repeat exploratory mistakes, and ii) the static nature of prompt structures, which prevents agents from adapting their…

### title:aiassistedcodereviewforproprietaryprogramminglanguagesalowcodeapproach
**AI-Assisted Code Review for Proprietary Programming Languages: A Low-Code Approach** (2026) — Tampere University Institutional Repository (Tampere University) · cites 0 · score 13 (strong 3) · periphery/software_engineering · https://trepo.tuni.fi/handle/10024/236067
signals: \bAI agents?\b;\bcopilots?\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
Quality assurance through code review is a critical but labor-intensive part of software development. In highly specialized environments, such as proprietary ERP systems, manual reviews are often bottlenecked by limited resources, creating a risk of defective code reaching production. Automating the review process with the help of AI is challenging because proprietary programming languages are…

### doi:10.48550/arxiv.2608.18167
**Adversarial Review: Structured Disagreement for Grounded Agentic Code Review** (2026) — arXiv (Cornell University) · cites 0 · score 13 (strong 3) · periphery/software_engineering · doi:10.48550/arxiv.2608.18167
signals: agentic;agentic*;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Early multi-agent LLM systems often used role-separated teams, yet scaling agent count yields diminishing returns on repository-level coding tasks. Recent alternatives treat agents as passive tools (subagents), yet this removes the benefits of agent interaction entirely. We study whether a subagent paradigm can support a middle ground: minimal agentic cooperation without the overhead of large…

### arxiv:2607.13196
**From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality** (2026) — arXiv (Cornell University) · cites 0 · score 13 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2607.13196
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Code review helps maintain software quality before code integration, but it also imposes a substantial workload on human reviewers. As generative artificial intelligence becomes part of software development, code review is shifting from a primarily human review process toward AI-supported review processes in which large language model (LLM) reviewers and AI agent reviewers participate alongside…

### doi:10.48550/arxiv.2507.02976
**How Safe Are AI-Generated Patches? A Large-scale Study on Security Risks in LLM and Agentic Automated Program Repair on SWE-bench** (2025) — arXiv (Cornell University) · cites 0 · score 13 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2507.02976
signals: agent(?:ic)? workflows?;agentic;agentic*
touchpoints: none
Large language models (LLMs) and their agentic frameworks are increasingly adopted to perform development tasks such as automated program repair (APR). While prior work has identified security risks in LLM-generated code, most have focused on synthetic, simplified, or isolated tasks that lack the complexity of real-world program repair. In this study, we present the first…

### doi:10.5281/zenodo.19643814
**Toward Autonomous AI-Driven Software Development: A Systematic Review of the Empirical Evidence on Agentic Systems (2022–2026)** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 13 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.19643814
signals: \bAI agents?\b;\bcopilots?\b;agentic;agentic*
touchpoints: none
Background. With the rapid emergence of autonomous AI software agents (Devin, Claude Code, Cursor Composer, Kiro, and others), debate has intensified regarding their ability to deliver complete software projects without human intervention. This systematic review evaluates the empirical evidence available between 2022 and 2026. Objectives. (1) Measure the actual performance of leading agentic systems on…

### doi:10.52202/085713-0788
**SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents** (2025) — n/a · cites 0 · score 13 (strong 3) · periphery/software_engineering · doi:10.52202/085713-0788
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;automat\w+\s
touchpoints: none
LLM-based agents have shown promising capabilities in a growing range of software engineering (SWE) tasks. However, advancing this field faces two critical challenges. First, high-quality training data is scarce, especially data that reflects real-world SWE scenarios, where agents must interact with development environments, execute code and adapt behavior based on the outcomes of their actions.…

### doi:10.65890/dmp-lncse.iciccs26.216
**From Robotic Process Automation to Agentic AI: A Systematic Review, Taxonomy, and Capability Assessment Framework for Intelligent Automation in Enterprise Accounting** (2026) — DMPedia Lecture Notes in Computer Science & Engineering · cites 0 · score 13 (strong 3) · periphery/interface_agents · doi:10.65890/dmp-lncse.iciccs26.216
signals: agent orchestration;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Enterprise accounting is undergoing a structural transition from rule-based robotic process automation (RPA) toward agentic artificial intelligence: systems built on large language models that plan multi-step workflows, invoke tools, and adapt their execution autonomously. Research on this transition remains fragmented across information systems, accounting, and artificial intelligence venues, and no unified conceptual structure yet characterises…

### doi:10.5281/zenodo.21362533
**Eliminating Human Intervention in the Software Development Lifecycle: A Novel Agentic Paradigm for Scalable Infrastructure Maintenance** (2026) — South African Computer Journal · cites 0 · score 12 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.21362533
signals: \bAI agents?\b;agentic;agentic*;model context protocol
touchpoints: tool_exposure
The persistent requirement for human intervention within software development and maintenance workflows has become the defining productivity bottleneck in modern platform engineering. Despite dramatic advances in AI-assisted code generation, the downstream lifecycle stages of build triage, code review, test authoring, and production incident response continue to impose a linear scaling constraint on engineering organizations: increasing…

### doi:10.48550/arxiv.2510.06223
**A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants** (2025) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2510.06223
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: tool_exposure
Advances in large language models (LLMs) and real-time speech recognition now make it possible to issue any graphical user interface (GUI) action through natural language and receive the corresponding system response directly through the GUI. Most production applications were never designed with speech in mind. This article provides a concrete architecture that enables GUIs to…

### doi:10.1145/3712003
**LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead** (2025) — ACM Transactions on Software Engineering and Methodology · cites 184 · score 12 (strong 2) · periphery/software_engineering · doi:10.1145/3712003
signals: autonomous agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Integrating Large Language Models (LLMs) into autonomous agents marks a significant shift in the research landscape by offering cognitive abilities that are competitive with human planning and reasoning. This article explores the transformative potential of integrating Large Language Models into Multi-Agent (LMA) systems for addressing complex challenges in software engineering (SE). By leveraging the collaborative…

### doi:10.1145/3798166
**On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub** (2026) — ACM Transactions on Software Engineering and Methodology · cites 25 · score 12 (strong 2) · periphery/software_engineering · doi:10.1145/3798166
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Large language models (LLMs) are increasingly being integrated into software development processes. The ability to generate code and submit pull requests with minimal human intervention, through the use of autonomous AI agents, is poised to become a standard practice. However, little is known about the practical usefulness of these pull requests and the extent to…

### doi:10.48550/arxiv.2407.01489
**Agentless: Demystifying LLM-based Software Engineering Agents** (2024) — arXiv (Cornell University) · cites 17 · score 12 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2407.01489
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe…

### doi:10.24136/oc.3994
**The algorithmic management of job loss and creation in the enterprise generative, multimodal, and agentic artificial intelligence economy** (2025) — Oeconomia Copernicana · cites 8 · score 12 (strong 3) · periphery/science_of_science · doi:10.24136/oc.3994
signals: agent(?:ic)? workflows?;agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Research background: Enterprise generative, multimodal, and agentic artificial intelligence (AI) technologies facilitate transformative productivity and workforce adaptation gains in innovative organizations, redesigns autonomous team and talent management for workforce and job rotation planning, skill development, and career paths, handle context-specific collaborative business processes, workflows, and decision-making, and augment multi-agent system scaling for labor productivity and…

### doi:10.48550/arxiv.2410.13825
**AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents** (2024) — arXiv (Cornell University) · cites 3 · score 12 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2410.13825
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Autonomy via agents using large language models (LLMs) for personalized, standardized tasks boosts human efficiency. Automating web tasks (like booking hotels within a budget) is increasingly sought after. Fulfilling practical needs, the web agent also serves as an important proof-of-concept example for various agent grounding scenarios, with its success promising advancements in many future applications.…

### doi:10.1145/3664647.3684998
**AssistEditor: Multi-Agent Collaboration for GUI Workflow Automation in Video Creation** (2024) — n/a · cites 3 · score 12 (strong 3) · periphery/interface_agents · doi:10.1145/3664647.3684998
signals: \bAI agents?\b;\bcopilots?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Graphical User Interface (GUI) Automation has shown significant potential recently. Previous works built GUI Agent systems to handle short-procedure tasks such as element grounding or functional assistance. In this paper, we propose a novel PC-Copilot, AssistEditor, that focuses on automating the video editing workflow. Unlike previous approaches, our system does not require users to input…

### doi:10.48550/arxiv.2512.22256
**Agentic Software Issue Resolution with Large Language Models: A Survey** (2025) — arXiv (Cornell University) · cites 2 · score 12 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2512.22256
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*
touchpoints: none
Software issue resolution aims to address real-world issues in software repositories based on natural language descriptions provided by users, and represents a key aspect of software maintenance. With the rapid development of large language models (LLMs) in reasoning and generation, LLM-based approaches have made significant progress in automated software issue resolution. However, resolving real-world software…

### doi:10.36227/techrxiv.175322671.12208812/v1
**GA: A Comprehensive Survey on LLM-based GUI Agent** (2025) — n/a · cites 2 · score 12 (strong 2) · periphery/interface_agents · doi:10.36227/techrxiv.175322671.12208812/v1
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The Graphical User Interface (GUI) is a visual method that allows users to interact with computers and mobile devices. Nowadays, users rely on GUI for completing some tasks, such as browsing web or using mobile applications. Users often meet some needs such as setting an alarm for 8:00 AM to wake them up and checking…

### doi:10.1109/icpc66645.2025.00067
**Building Bridges, Not Walls: Fairness-Aware and Accurate Recommendation of Code Reviewers via LLm-Based Agents Collaboration** (2025) — n/a · cites 1 · score 12 (strong 2) · periphery/software_engineering · doi:10.1109/icpc66645.2025.00067
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Code review is essential for maintenance of pull request-based software systems. Recommending suitable reviewers for code changes can enhance defect detection and knowledge dissemination. Despite extensive research, the inherent complexity of pull requests (PRs) and reviewer profiles continues to cause challenge for accurate matching them together. Furthermore, existing methods often amplify gender and racial/ethnic disparities…

### arxiv:2601.03556
**Do Autonomous Agents Contribute Test Code? A Study of Tests in Agentic Pull Requests** (2026) — arXiv (Cornell University) · cites 0 · score 12 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2601.03556
signals: agentic;agentic*;autonomous agents?;autonomous agents?*
touchpoints: none
Testing is a critical practice for ensuring software correctness and long-term maintainability. As agentic coding tools increasingly submit pull requests (PRs), it becomes essential to understand how testing appears in these agent-driven workflows. Using the AIDev dataset, we present an empirical study of test inclusion in agentic pull requests. We examine how often tests are…

### doi:10.5281/zenodo.19056667
**DocAware: Documentation-Augmented AI Agents for Reliable Code Review and API Migration** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 12 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.19056667
signals: \bAI agents?\b;\bAI agents?\b*;\bLLM[- ]?agents?\b
touchpoints: none
Large Language Models (LLMs) are increasingly used for automated code review and migration assistance, yet they frequently hallucinate API names, fabricate deprecated method signatures, and recommend patterns from incorrect library versions. We present DocAware, an open-source tool that augments LLM-based code review with structured, version-specific API documentation retrieval and a persistent memory layer. Through a…

### doi:10.22214/ijraset.2026.83359
**Generative AI in Mobile Application Development: A Systematic Literature Review** (2026) — International Journal for Research in Applied Science and Engineering Technology · cites 0 · score 12 (strong 1) · periphery/science_of_science · doi:10.22214/ijraset.2026.83359
signals: \bcopilots?\b
touchpoints: none
Generative Artificial Intelligence (GenAI) tools have become central to modern software engineering, fundamentally transforming how developers design, write, debug, test, and document code. This systematic literature review examines the measurable impact of GenAI tools — specifically GitHub Copilot, OpenAI GPT-4/ChatGPT, Google Gemini, Anthropic Claude 3, and Meta Code LLaMA — on Android and Flutter mobile…

### arxiv:2510.13913
**Synthesizing Agentic Data for Web Agents with Progressive Difficulty Enhancement Mechanisms** (2025) — arXiv · cites 0 · score 12 (strong 3) · periphery/interface_agents · arXiv:2510.13913
signals: \btool[- ]use\b;agentic;agentic*;tool[- ]calling
touchpoints: none
Web-based 'deep research' agents aim to solve complex question - answering tasks through long-horizon interactions with online tools. These tasks remain challenging, as the underlying language models are often not optimized for long-horizon reasoning and exploration. Prior work has proposed workflows for constructing instruction-tuning datasets, often leveraging knowledge graphs. However, such methods typically lack fine-grained…

### doi:10.20944/preprints202603.0129.v1
**A Self-Reflective Multi-Agent Collaboration Framework for Dynamic Software Engineering Tasks** (2026) — Preprints.org · cites 3 · score 11 (strong 2) · periphery/software_engineering · doi:10.20944/preprints202603.0129.v1
signals: \bAutoGen\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: topology_construction
Large Language Model (LLM) based multi-agent systems have demonstrated remarkable potential in automating complex software engineering tasks. However, existing frameworks such as MetaGPT and AutoGen suffer from critical limitations including static role assignments, cascading hallucinations in long-horizon tasks, and the absence of experience accumulation mechanisms. We propose Eco-Evolve, a self-reflective multi-agent collaboration framework that addresses…

### arxiv:2508.17343
**Agentic AI for Software: thoughts from Software Engineering community** (2025) — arXiv · cites 0 · score 11 (strong 2) · periphery/software_engineering · arXiv:2508.17343
signals: \bAI agents?\b;agentic;agentic*
touchpoints: verification_regression
AI agents have recently shown significant promise in software engineering. Much public attention has been transfixed on the topic of code generation from Large Language Models (LLMs) via a prompt. However, software engineering is much more than programming, and AI agents go far beyond instructions given by a prompt. At the code level, common software…

### doi:10.1109/cvpr52733.2024.01262
**AssistGUI: Task-Oriented PC Graphical User Interface Automation** (2024) — n/a · cites 11 · score 11 (strong 3) · periphery/interface_agents · doi:10.1109/cvpr52733.2024.01262
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framewor
touchpoints: none
Graphical User Interface (GUI) automation holds significant promise for assisting users with complex tasks, thereby boosting human productivity. Existing works leveraging Large Language Model (LLM) or LLM-based AI agents have shown capabilities in automating tasks on Android and Web platforms. However, these tasks are primarily aimed at simple device usage and entertainment operations. This paper…

### doi:10.48550/arxiv.2311.10776
**Chemist-X: Large Language Model-empowered Agent for Reaction Condition Recommendation in Chemical Synthesis** (2023) — arXiv (Cornell University) · cites 10 · score 11 (strong 2) · periphery/lab_automation · doi:10.48550/arxiv.2311.10776
signals: \bAI agents?\b;self[- ]driving lab
touchpoints: none
Recent AI research plots a promising future of automatic chemical reactions within the chemistry society. This study proposes Chemist-X, a comprehensive AI agent that automates the reaction condition optimization (RCO) task in chemical synthesis with retrieval-augmented generation (RAG) technology and AI-controlled wet-lab experiment executions. To begin with, as an emulation on how chemical experts solve…

### doi:10.48550/arxiv.2403.17927
**MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution** (2024) — arXiv (Cornell University) · cites 9 · score 11 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2403.17927
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
In software development, resolving the emergent issues within GitHub repositories is a complex challenge that involves not only the incorporation of new code but also the maintenance of existing code. Large Language Models (LLMs) have shown promise in code generation but face difficulties in resolving Github issues, particularly at the repository level. To overcome this…

### doi:10.48550/arxiv.2507.06185
**Hidden Prompts in Manuscripts Exploit AI-Assisted Peer Review** (2025) — arXiv (Cornell University) · cites 2 · score 11 (strong 3) · periphery/science_of_science · doi:10.48550/arxiv.2507.06185
signals: \bAI agents?\b;\bLLM[- ]?agents?\b;\btool[- ]use\b
touchpoints: none
A reusable protocol and a pilot baseline for measuring whether AI agents used in scientific writing and peer review refuse directives injected into the documents they process. Motivated by the 2025 discovery of hidden prompts (e.g. 'GIVE A POSITIVE REVIEW ONLY') embedded in arXiv manuscripts to manipulate AI-assisted peer review (Lin, arXiv:2507.06185), and by general…

### doi:10.1109/slaai-icai68534.2025.11318443
**An Agentic-AI Solution for Intelligent Code Review** (2025) — n/a · cites 1 · score 11 (strong 2) · periphery/software_engineering · doi:10.1109/slaai-icai68534.2025.11318443
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Manual pull request (PR) reviews are a critical but notoriously time-consuming and inconsistent part of modern software development, creating significant bottlenecks. This paper introduces the Intelligent Code Reviewer (ICR), an agentic AI system designed to automate and enhance this process. ICR accepts GitHub pull requests as input and generates comprehensive, structured reviews as output, seamlessly…

### doi:10.1109/tse.2026.3657900
**Agentic Recommender Systems: A Systematic Literature Review** (2026) — IEEE Transactions on Software Engineering · cites 1 · score 11 (strong 2) · periphery/science_of_science · doi:10.1109/tse.2026.3657900
signals: \bLLM[- ]?agents?\b;agentic;agentic*
touchpoints: none
Recommender systems (RSs) are software systems that use machine learning techniques to suggest items, such as movies, products or routes to users based on input provided over time. These systems have been widely used by companies, such as Amazon, Google, and Netflix, who rely heavily on recommendations as a core element of their interaction with…

### arxiv:2606.20243
**Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs** (2026) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2606.20243
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy. Phoenix decomposes the work across six specialized agents. Planner, reproducer, coder, tester, failure analyst and Pull Request (PR) agent, all coordinated by a label-based GitHub webhook state machine.…

### title:multiagentsystemforautomatedcodereviews
**Multi-Agent System for Automated Code Reviews** (2025) — Tampere University Institutional Repository (Tampere University) · cites 0 · score 11 (strong 2) · periphery/software_engineering · https://trepo.tuni.fi/handle/10024/232334
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipe
touchpoints: none
Code reviews play a key role in software quality assurance, yet the process is often time-consuming, inconsistent, and dependent on reviewer expertise. Although recent Large Language Model (LLM) advances have introduced automated review tools, single-model systems often suffer from inconsistency, redundancy, and limited trust when relying on a single agent. This thesis addresses these limitations…

### doi:10.48550/arxiv.2604.00917
**Investigating Autonomous Agent Contributions in the Wild: Activity Patterns and Code Change over Time** (2026) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2604.00917
signals: \bcopilots?\b;autonomous agents?;autonomous agents?*
touchpoints: none
The rise of large language models for code has reshaped software development. Autonomous coding agents, able to create branches, open pull requests, and perform code reviews, now actively contribute to real-world projects. Their growing role offers a unique and timely opportunity to investigate AI-driven contributions and their effects on code quality, team dynamics, and software…

### doi:10.5281/zenodo.22675104
**SMART SOFTWARE ENGINEERING WITH AI-BASED DATA INTEGRATION APPROACHES** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 11 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.22675104
signals: agent(?:ic)? workflows?;agentic;autonomous agents?
touchpoints: none
The rapid convergence of software engineering and artificial intelligence has fundamentally altered how modern digital systems are designed, built, and maintained. Traditional software development paradigms, while historically effective, increasingly struggle to handle the sheer volume, heterogeneity, and real-time demands of enterprise data. Smart Software Engineering with AI-Based Data Integration Approaches bridges this critical divide, presenting…

### doi:10.48550/arxiv.2604.15468
**The Semi-Executable Stack: Agentic Software Engineering and the Expanding Scope of SE** (2026) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2604.15468
signals: \btool[- ]using\b;agentic;agentic*
touchpoints: none
AI-based systems, currently driven largely by LLMs and tool-using agentic harnesses, are increasingly discussed as a possible threat to software engineering. Foundation models get stronger, agents can plan and act across multiple steps, and tasks such as scaffolding, routine test generation, straightforward bug fixing, and small integration work look more exposed than they did only…

### doi:10.70315/uloap.ulirs.2025.0202006
**AI-Driven Automation of Code Review Processes: Enhancing Software Quality and Reducing Human Error** (2025) — Universal Library of Innovative Research and Studies · cites 0 · score 11 (strong 3) · periphery/software_engineering · doi:10.70315/uloap.ulirs.2025.0202006
signals: \bLLM[- ]?agents?\b;agent(?:ic)? workflows?;agentic
touchpoints: none
In contemporary software engineering, expert code review practices have entered a phase of profound reconsideration under the influence of generative artificial intelligence technologies. In 2024–2025, a qualitatively new, exponential stage of integrating large language models (LLM) into the software development life cycle (SDLC) is being observed, which radically changes the balance between development speed, quality…

### title:agenticmultihunkrepaironswebenchverified
**Agentic multi-hunk repair on SWE-bench verified** (2026) — cIRcle (University of British Columbia) · cites 0 · score 11 (strong 2) · periphery/software_engineering · doi:10.14288/1.0452541
signals: \btool[- ]using\b;agentic;agentic*
touchpoints: none
Most research on automated program repair (APR) addresses defects whose fix occupies a single contiguous code region. However, a substantial proportion of real-world bugs require coordinated edits at multiple disjoint locations. These multi-hunk defects pose a distinct challenge: the unit of correctness is the complete patch, so an edit that is locally correct but globally…

### doi:10.48550/arxiv.2312.13108
**ASSISTGUI: Task-Oriented Desktop Graphical User Interface Automation** (2023) — arXiv (Cornell University) · cites 0 · score 11 (strong 3) · periphery/interface_agents · doi:10.48550/arxiv.2312.13108
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b;\bLLM[- ]?agents?\b
touchpoints: none
Graphical User Interface (GUI) automation holds significant promise for assisting users with complex tasks, thereby boosting human productivity. Existing works leveraging Large Language Model (LLM) or LLM-based AI agents have shown capabilities in automating tasks on Android and Web platforms. However, these tasks are primarily aimed at simple device usage and entertainment operations. This paper…

### doi:10.48550/arxiv.2411.02337
**WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning** (2024) — arXiv (Cornell University) · cites 0 · score 11 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2411.02337
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);autonomous agents?
touchpoints: none
Large language models (LLMs) have shown remarkable potential as autonomous agents, particularly in web-based tasks. However, existing LLM web agents heavily rely on expensive proprietary LLM APIs, while open LLMs lack the necessary decision-making capabilities. This paper introduces WebRL, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open LLMs.…

### doi:10.48550/arxiv.2505.16282
**ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay** (2025) — arXiv (Cornell University) · cites 0 · score 11 (strong 3) · periphery/interface_agents · doi:10.48550/arxiv.2505.16282
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\btool[- ]using\b;agentic
touchpoints: none
Training large language models (LLMs) as interactive agents for controlling graphical user interfaces (GUIs) presents a unique challenge to optimize long-horizon action sequences with multimodal feedback from complex environments. While recent works have advanced multi-turn reinforcement learning (RL) for reasoning and tool-using capabilities in LLMs, their application to GUI-based agents remains relatively underexplored due to…

### doi:10.17605/osf.io/xt4wp
**Do Human Cognitive Failures Map onto AI Agent Failures? A Structured Literature Review (v2)** (2026) — n/a · cites 0 · score 11 (strong 2) · periphery/science_of_science · doi:10.17605/osf.io/xt4wp
signals: \bAI agents?\b;\bAI agents?\b*;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)
touchpoints: none
Public OSF Project hosting the literature review "Do Human Cognitive Failures Map onto AI Agent Failures? A Structured Literature Review" (v2, MAST-fidelity revision, 2026-05-08), authored by Tuomo Nikulainen, Pisama, LLC. V2 changes relative to the v1 PsyArXiv submission (preprint t26sh_v1, May 3 2026): - New Appendix C: full crosswalk between MAST's 14 multi-agent failure modes…

### doi:10.5281/zenodo.22210843
**lit-screening-pipeline: hybrid semi-automated screening pipeline for systematic literature reviews** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 11 (strong 2) · periphery/science_of_science · doi:10.5281/zenodo.22210843
signals: \bcopilots?\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b*
touchpoints: none
Hybrid semi-automated screening pipeline for systematic literature reviews. Combines deterministic Python scripts for deduplication and hard filters with LLM adjudication (Claude Opus via GitHub Copilot Chat in agent mode). Designed for the ESGCI DBA thesis literature review on AI-assisted software development but generalises to any focused systematic review with a well-defined scope. Ships a SKILL.md,…

### doi:10.2196/84322
**Evaluation of Large Language Models for Peer Review in Transplantation Research: Algorithm Validation Study** (2026) — JMIR AI · cites 2 · score 10 (strong 1) · periphery/science_of_science · doi:10.2196/84322
signals: \bToT\b
touchpoints: solver_control
BACKGROUND: Peer review remains central to ensuring research quality, yet it is constrained by reviewer fatigue and human bias. The rapid rise in scientific publishing has worsened these challenges, prompting interest in whether large language models (LLMs) can support or improve the peer review process. OBJECTIVE: This study aimed to address critical gaps in the…

### doi:10.5281/zenodo.20283766
**Beyond Heuristics? Rethinking Targeted Unit Test Generation in the Era of LLM Agents** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.20283766
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: config_generation
# Beyond Heuristics? Rethinking Targeted Unit Test Generation in the Era of LLM Agents This repository contains the replication package for the paper **"Beyond Heuristics? Rethinking Targeted Unit Test Generation in the Era of LLM Agents"**, submitted to **ESEM 2026** (under double-blind review). ## Overview We conduct a comprehensive evaluation of LLM agents for **targeted…

### doi:10.5281/zenodo.20387265
**(Artifact) Ai LitReview - Web-Based Tool for LLM-Assisted Systematic Literature Reviews** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 1) · periphery/science_of_science · doi:10.5281/zenodo.20387265
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: results_interpretation
AI LitReview is a collaborative web-based platform designed to support researchers throughout the entire Systematic Literature Review (SLR) process, from protocol definition to evidence synthesis. The tool integrates Large Language Models (LLMs) via the OpenRouter API (with access to over 365 models) and locally via Ollama, enabling AI-assisted study selection, structured data extraction, and RAG-based…

### doi:10.2196/preprints.84322
**Evaluation of Large Language Models for Peer Review in Transplantation Research: Algorithm Validation Study (Preprint)** (2025) — n/a · cites 0 · score 10 (strong 1) · periphery/science_of_science · doi:10.2196/preprints.84322
signals: \bToT\b
touchpoints: solver_control
BACKGROUND Peer review remains central to ensuring research quality, yet it is constrained by reviewer fatigue and human bias. The rapid rise in scientific publishing has worsened these challenges, prompting interest in whether large language models (LLMs) can support or improve the peer review process. OBJECTIVE This study aimed to address critical gaps in the…

### doi:10.1038/s41467-024-54457-x
**An automatic end-to-end chemical synthesis development platform powered by large language models** (2024) — Nature Communications · cites 112 · score 10 (strong 2) · periphery/lab_automation · doi:10.1038/s41467-024-54457-x
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bcopilots?\b
touchpoints: none
The rapid emergence of large language model (LLM) technology presents promising opportunities to facilitate the development of synthetic reactions. In this work, we leveraged the power of GPT-4 to build an LLM-based reaction development framework (LLM-RDF) to handle fundamental tasks involved throughout the chemical synthesis development. LLM-RDF comprises six specialized LLM-based agents, including Literature Scouter,…

### doi:10.1016/j.jmsy.2025.02.008
**Chat with MES: LLM-driven user interface for manipulating garment manufacturing system through natural language** (2025) — Journal of Manufacturing Systems · cites 31 · score 10 (strong 2) · periphery/interface_agents · doi:10.1016/j.jmsy.2025.02.008
signals: \bAI agents?\b;\bLLM[- ]?agents?\b
touchpoints: none
This paper presents Chat with MES (CWM), an AI agent system, which integrates LLMs into the Manufacturing Execution System (MES), serving as the “ears, mouth, and the brain”. This system promotes a paradigm shift in MES interactions from Graphical User Interface (GUI) to natural language interface”, offering a more natural and efficient way for workers…

### doi:10.26434/chemrxiv-2024-6wmg4
**Accelerated end-to-end chemical synthesis development with large language models** (2024) — ChemRxiv · cites 11 · score 10 (strong 2) · periphery/lab_automation · doi:10.26434/chemrxiv-2024-6wmg4
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: none
The rapid emergence of large language model (LLM) technology presents significant opportunities to facilitate the development of synthetic reactions. In this work, we leveraged the power of GPT-4 to build a multi-agent system to handle fundamental tasks involved throughout the chemical synthesis development process. The multi-agent system comprises six specialized LLM-based agents, including Literature Scouter,…

### doi:10.20944/preprints202501.0413.v1
**LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects** (2025) — Preprints.org · cites 6 · score 10 (strong 1) · periphery/interface_agents · doi:10.20944/preprints202501.0413.v1
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
With the rapid rise of large language models (LLMs), phone automation has undergone transformative changes. This paper systematically reviews LLM-driven phone GUI agents, highlighting their evolution from script-based automation to intelligent, adaptive systems. We first contextualize key challenges, (i) limited generality, (ii) high maintenance overhead, and (iii) weak intent comprehension, and show how LLMs address…

### doi:10.5281/zenodo.16899501
**AIDev: Studying AI Coding Agents on GitHub** (2025) — arXiv (Cornell University) · cites 5 · score 10 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.16899501
signals: \bAI agents?\b;\bcopilots?\b;agentic
touchpoints: none
The future of software engineering--SE 3.0--is unfolding with the rise of AI teammates: autonomous, goal-driven systems collaborating with human developers. Among these, autonomous coding agents are especially transformative, now actively initiating, reviewing, and evolving code at scale. This paper introduces AIDev, the first large-scale dataset capturing how such agents operate in the wild. Spanning over…

### doi:10.1109/tse.2025.3621462
**Hydra-Reviewer: A Holistic Multi-Agent System for Automatic Code Review Comment Generation** (2025) — IEEE Transactions on Software Engineering · cites 2 · score 10 (strong 1) · periphery/software_engineering · doi:10.1109/tse.2025.3621462
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Review comment generation is a crucial task in code review, and significant progress has been made in automating. Previous research has generated review comments by fine-tuning pre-trained models or Large Language Models (LLMs). However, these studies have overlooked the necessity of conducting code reviews from multiple perspectives, resulting in the omission of potential issues in…

### doi:10.48550/arxiv.2411.04890
**GUI Agents with Foundation Models: A Comprehensive Survey** (2024) — arXiv (Cornell University) · cites 2 · score 10 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2411.04890
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|sma
touchpoints: none
Recent advances in foundation models, particularly Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs), have facilitated the development of intelligent agents capable of performing complex tasks. By leveraging the ability of (M)LLMs to process and interpret Graphical User Interfaces (GUIs), these agents can autonomously execute user instructions, simulating human-like interactions such as clicking…

### doi:10.1145/3696630.3728618
**AutoReview: An LLM-based Multi-Agent System for Security Issue-Oriented Code Review** (2025) — n/a · cites 1 · score 10 (strong 1) · periphery/software_engineering · doi:10.1145/3696630.3728618
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Software vulnerabilities can lead to severe security issues such as data breaches, financial losses, and service disruptions, making security issue-oriented code review a crucial part of the development process. Traditional approaches struggle with analyzing complex code and providing explanations, while large language models (LLMs) show promise in code review but do not focus on security-related…

### doi:10.1609/aaai.v40i47.41489
**LiRA: A Multi-Agent Framework for Reliable and Readable Literature Review Generation** (2026) — Proceedings of the AAAI Conference on Artificial Intelligence · cites 1 · score 10 (strong 2) · periphery/science_of_science · doi:10.1609/aaai.v40i47.41489
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
The rapid growth of scientific publications has made it increasingly difficult to keep literature reviews comprehensive and up-to-date. Though prior work has focused on automating retrieval and screening, the writing phase of systematic reviews remains largely under-explored, especially with regard to readability and factual accuracy. To address this, we present LiRA (Literature Review Agents), a…

### arxiv:2512.24630
**How Do Agentic AI Systems Address Performance Optimizations? A BERTopic-Based Analysis of Pull Requests** (2025) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2512.24630
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
LLM-based software engineering is influencing modern software development. In addition to correctness, prior studies have also examined the performance of software artifacts generated by AI agents. However, it is unclear how exactly the agentic AI systems address performance concerns in practice. In this paper, we present an empirical study of performance-related pull requests generated by…

### doi:10.48550/arxiv.2512.02329
**Towards autonomous normative multi-agent systems for Human-AI software engineering teams** (2025) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2512.02329
signals: autonomous agents?;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
This paper envisions a transformative paradigm in software engineering, where Artificial Intelligence, embodied in fully autonomous agents, becomes the primary driver of the core software development activities. We introduce a new class of software engineering agents, empowered by Large Language Models and equipped with beliefs, desires, intentions, and memory to enable human-like reasoning. These agents…

### doi:10.5281/zenodo.19127530
**AGENTIC AI-POWERED AUTONOMOUS SOFTWARE ENGINEERING FRAMEWORK FOR AUTOMATED CODE GENERATION AND DEBUGGING** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.19127530
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
This paper discusses the disruptive nature of agentic AI-based autonomous systems in software engineering, specifically the automated code generation and debugging. The main aim is to analyze the role of agentic AI-based systems, who combine autonomy, reasoning as well as adaptive learning in improving efficiency, accuracy, resilience, governance, and scalability within the contemporary development setting.…

### doi:10.5281/zenodo.18519189
**IMPACTE: An AI-First Software Engineering Framework** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.18519189
signals: \bAI agents?\b;\bLLM[- ]?agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
IMPACTE: An AI-First Software Engineering FrameworkAcronym for: Intelligent Multi-Agent Product-Centric Architecture with Cost-Efficiency and Trade-offs Engineering IMPACTE explores the emerging paradigm shift in software engineering where the primary bottleneck may be moving from implementation velocity to problem definition accuracy and regulatory compliance. The framework investigates how the Software Development Lifecycle (SDLC) might be restructured around…

### arxiv:2607.03316
**Is Agentic Code Review Helpful? Mining Developers' Feedback to CodeRabbit Reviews in the Wild** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2607.03316
signals: agentic;agentic*;autonomous agents?
touchpoints: none
Agentic code review, where autonomous agents provide code review comments on pull requests, is increasingly integrated into development workflows, yet there is limited empirical evidence on how developers respond to such comments in practice. In this paper, we present an empirical study of agentic code reviews using CodeRabbit as a case study. Through an empirical…

### doi:10.6084/m9.figshare.28538711
**Exploring Individual Factors in the Adoption of LLMs for Specific Software Engineering Purposes—Online Appendix** (2026) — Figshare · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.6084/m9.figshare.28538711
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b
touchpoints: none
The advent of large language models (LLMs) is transforming software development, significantly enhancing software engineering processes. Research has explored the general role of LLMs in software development teams, focusing also on the specific software engineering tasks they support, such as generating artifacts, supporting decision-making, and retrieving information. However, despite growing research on the role of…

### doi:10.55041/isjem07720
**VDA-SDLC: Validation-Driven Adaptive Agentic Software Development Life Cycle Framework for Autonomous Software Engineering** (2026) — International Scientific Journal of Engineering and Management · cites 0 · score 10 (strong 2) · periphery/software_engineering · doi:10.55041/isjem07720
signals: agentic;agentic*;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Abstract - This paper presents a Validation-Driven Adaptive Agentic SDLC Framework that automates multiple software engineering activities through a collaborative multi-agent architecture. The proposed framework integrates specialized agents responsible for requirement analysis, planning, code generation, validation, and packaging. Unlike conventional AI coding assistants, the framework employs a validation-driven feedback mechanism in which generated applications are…

### doi:10.5281/zenodo.19652205
**Generative Artificial Intelligence in Real-World Applications: A Survey of Architectures, Use Cases, and Implementation Challenges** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 10 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.19652205
signals: \bcopilots?\b
touchpoints: none
Abstract — Generative Artificial Intelligence (GenAI) has emerged as a transformative paradigm in modern computing, enabling the synthesis of novel content — including text, images, audio, and software code — through learned representations from large-scale datasets. Unlike discriminative models focused on classification and prediction, generative approaches introduce capabilities for automation, creativity augmentation, and human-computer interaction…

### arxiv:2507.15003
**The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering** (2025) — arXiv · cites 0 · score 10 (strong 3) · periphery/software_engineering · arXiv:2507.15003
signals: \bAI agents?\b;\bcopilots?\b;agentic
touchpoints: none
The future of software engineering--SE 3.0--is unfolding with the rise of AI teammates: autonomous, goal-driven systems collaborating with human developers. Among these, autonomous coding agents are especially transformative, now actively initiating, reviewing, and evolving code at scale. This paper introduces AIDev, the first large-scale dataset capturing how such agents operate in the wild. Spanning over…

### arxiv:2602.07900
**Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2602.07900
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large Language Model (LLM) code agents increasingly resolve repository-level issues by iteratively editing code, invoking tools, and validating candidate patches. In these workflows, agents often write tests on the fly, but the value of this behavior remains unclear. For example, GPT-5.2 writes almost no new tests yet achieves performance comparable to top-ranking agents.This raises a…

### arxiv:2602.13653
**Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2602.13653
signals: agentic;agentic*;autonomous agents?
touchpoints: none
Recent advances in Multimodal Large Language Models (MLLMs) have substantially driven the progress of autonomous agents for Graphical User Interface (GUI). Nevertheless, in real-world applications, GUI agents are often faced with non-stationary environments, leading to high computational costs for data curation and policy optimization. In this report, we introduce a novel MLLM-centered framework for GUI…

### doi:10.48550/arxiv.2402.16965
**WIPI: A New Web Threat for LLM-Driven Web Agents** (2024) — arXiv (Cornell University) · cites 0 · score 10 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2402.16965
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
With the fast development of large language models (LLMs), LLM-driven Web Agents (Web Agents for short) have obtained tons of attention due to their superior capability where LLMs serve as the core part of making decisions like the human brain equipped with multiple web tools to actively interact with external deployed websites. As uncountable Web…

### doi:10.48550/arxiv.2602.13516
**SPILLage: Agentic Oversharing on the Web** (2026) — arXiv (Cornell University) · cites 0 · score 10 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2602.13516
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agentic;agentic*
touchpoints: none
LLM-powered agents are beginning to automate user's tasks across the open web, often with access to user resources such as emails and calendars. Unlike standard LLMs answering questions in a controlled ChatBot setting, web agents act "in the wild", interacting with third parties and leaving behind an action trace. Therefore, we ask the question: how…

### doi:10.48448/czd6-1e77
**[V] Use of an AI Peer Review Panel to Assess Clarity, Novelty, and Impact** (2025) — Underline Science Inc. · cites 0 · score 10 (strong 2) · periphery/science_of_science · doi:10.48448/czd6-1e77
signals: \bAI agents?\b;multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)
touchpoints: none
Pawin Taechoyotin,1 Daniel E. Acuna1 Objective Nowadays, there is an excessive load on human reviewers to the point where the quality of peer reviews is often compromised. To alleviate this excessive load, we explored the possibility of a multiagent AI peer review panel that we have developed that considers text, figures, and citations to produce…

### doi:10.48550/arxiv.2605.03117
**ARISE: A Repository-level Graph Representation and Toolset for Agentic Program Repair and Fault Localization** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2605.03117
signals: \btool[- ]use\b;agentic;agentic*
touchpoints: tool_exposure
Automated program repair at repository scale requires an agent to locate a fault among thousands of files and synthesize a correct patch. Existing graph-based agents represent how a repository is organized into files, classes, and functions, but they do not model how variable values flow within a procedure, which leaves the agent without the semantic…

### doi:10.5281/zenodo.20881926
**Fast Dash** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 9 (strong 3) · periphery/software_engineering · doi:10.5281/zenodo.20881926
signals: [a-z]{3,}-mcp\b;\bAI agents?\b;\bLangChain\b
touchpoints: tool_exposure
Changelog v0.3.1 (2026-06-25) Fixed bugs: MCP: agent-facing tool schemas are generic untyped objects — type hints do NOT build the agent schemas, contradicting the docs #102 MCP: an agent can't read back the inputs it set — dash://components/get\_dash\_component never reflect set\_input, contradicting the docs' "current values" #100 backend="fastapi" never starts a server when launched the…

### doi:10.1145/3746027.3755189
**PG-Agent: An Agent Powered by Page Graph** (2025) — arXiv · cites 0 · score 9 (strong 2) · periphery/interface_agents · doi:10.1145/3746027.3755189
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: topology_construction
Graphical User Interface (GUI) agents possess significant commercial and social value, and GUI agents powered by advanced multimodal large language models (MLLMs) have demonstrated remarkable potential. Currently, existing GUI agents usually utilize sequential episodes of multi-step operations across pages as the prior GUI knowledge, which fails to capture the complex transition relationship between pages, making…

### doi:10.18653/v1/2024.emnlp-main.70
**AgentReview: Exploring Peer Review Dynamics with LLM Agents** (2024) — arXiv (Cornell University) · cites 27 · score 9 (strong 1) · periphery/science_of_science · doi:10.18653/v1/2024.emnlp-main.70
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
Peer review is fundamental to the integrity and advancement of scientific publication.Traditional methods of peer review analyses often rely on exploration and statistics of existing peer review data, which do not adequately address the multivariate nature of the process, account for the latent variables, and are further constrained by privacy concerns due to the sensitive…

### doi:10.48550/arxiv.2408.02479
**From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future** (2024) — arXiv (Cornell University) · cites 20 · score 9 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2408.02479
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
With the rise of large language models (LLMs), researchers are increasingly exploring their applications in var ious vertical domains, such as software engineering. LLMs have achieved remarkable success in areas including code generation and vulnerability detection. However, they also exhibit numerous limitations and shortcomings. LLM-based agents, a novel tech nology with the potential for Artificial…

### doi:10.1109/access.2025.3581139
**A GPT-Based Code Review System With Accurate Feedback for Programming Education** (2025) — IEEE Access · cites 9 · score 9 (strong 1) · periphery/software_engineering · doi:10.1109/access.2025.3581139
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The increasing demand for programming education and growing class sizes require immediate and personalized feedback. However, integrating Large Language Models (LLMs) like ChatGPT in introductory programming courses raises concerns about AI-assisted cheating. In large-scale settings, faulty code submissions may lead LLMs to overanalyze, causing unnecessary token consumption. This paper proposes a GPT-4o-based code review system…

### doi:10.18653/v1/2024.findings-emnlp.70
**Dynamic Planning for LLM-based Graphical User Interface Automation** (2024) — arXiv (Cornell University) · cites 9 · score 9 (strong 2) · periphery/interface_agents · doi:10.18653/v1/2024.findings-emnlp.70
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bReAct\b
touchpoints: none
The advent of large language models (LLMs) has spurred considerable interest in advancing autonomous LLMs-based agents, particularly in intriguing applications within smartphone graphical user interfaces (GUIs).When presented with a task goal, these agents typically emulate human actions within a GUI environment until the task is completed.However, a key challenge lies in devising effective plans to…

### doi:10.48550/arxiv.2404.18496
**AI-powered Code Review with LLMs: Early Results** (2024) — arXiv (Cornell University) · cites 6 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2404.18496
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bAI agents?\b
touchpoints: none
In this paper, we present a novel approach to improving software quality and efficiency through a Large Language Model (LLM)-based model designed to review code and identify potential issues. Our proposed LLM-based AI agent model is trained on large code repositories. This training includes code reviews, bug reports, and documentation of best practices. It aims…

### doi:10.48550/arxiv.2509.06216
**Agentic Software Engineering: Foundational Pillars and a Research Roadmap** (2025) — arXiv (Cornell University) · cites 5 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2509.06216
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;agentic;agentic*
touchpoints: none
Agentic Software Engineering (SE 3.0) represents a new era where intelligent agents are tasked not with simple code generation, but with achieving complex, goal-oriented SE objectives. To harness these new capabilities while ensuring trustworthiness, we must recognize a fundamental duality within the SE field in the Agentic SE era, comprising two symbiotic modalities: SE for…

### doi:10.1109/saner64311.2025.00009
**Beyond pip Install: Evaluating LLM Agents for the Automated Installation of Python Projects** (2025) — arXiv (Cornell University) · cites 3 · score 9 (strong 1) · periphery/software_engineering · doi:10.1109/saner64311.2025.00009
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
Many works have recently proposed the use of Large Language Model (LLM) based agents for performing ‘repository level’ tasks, loosely defined as a set of tasks whose scopes are greater than a single file. This has led to speculation that the orchestration of these repository-level tasks could lead to software engineering agents capable of performing…

### doi:10.1109/scam63643.2024.00031
**GitRev: An LLM-Based Gamification Framework for Modern Code Review Activities** (2024) — n/a · cites 3 · score 9 (strong 1) · periphery/software_engineering · doi:10.1109/scam63643.2024.00031
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Modern code review (MCR) is recognized as an effective software quality assurance practice that is broadly adopted by open-source and commercial software projects. MCR is most effective when developers follow best practices, as it improves code quality, enhances knowledge transfer, increases team awareness and shares code ownership. However, prior work highlights that poor code review…

### doi:10.48550/arxiv.2507.23370
**Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling** (2025) — arXiv (Cornell University) · cites 2 · score 9 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2507.23370
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Software issue resolution is a critical challenge in software engineering and has garnered increasing attention in recent years. With the rapid advancement of large language models (LLMs), substantial progress has been made in addressing real-world software engineering tasks. Recent studies have introduced ensemble reasoning techniques to enhance the performance of LLM-based issue resolution. However, existing…

### doi:10.1109/csnt64827.2025.10968728
**Coding Agents: A Comprehensive Survey of Automated Bug Fixing Systems and Benchmarks** (2025) — n/a · cites 2 · score 9 (strong 2) · periphery/software_engineering · doi:10.1109/csnt64827.2025.10968728
signals: agentic;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
One of the trickiest problems in software engineering is automating software issue fixes, which calls for a thorough comprehension of contextual relationships, code semantics, and dynamic debugging techniques. The development of automatic program repair (APR) is examined in this survey, which traces a path from early template and constraint-based approaches to more recent developments powered…

### doi:10.1109/coginfocom66819.2025.11200869
**Exploring the Relationship Between Code Metrics and the Ability of Large Language Models to Solve Code Issues** (2025) — n/a · cites 1 · score 9 (strong 2) · periphery/software_engineering · doi:10.1109/coginfocom66819.2025.11200869
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLLM[- ]?agents?\b
touchpoints: none
Large Language Models (LLMs) are increasingly integrated into software engineering workflows, assisting with tasks such as code generation, unit testing, and bug resolution. Despite their growing use, limited research has examined how code-level metrics such as Halstead complexity, maintainability index, and source lines of code correlate with issue resolution rates for LLM-powered agents when modifying…

### arxiv:2407.04722
**A GPT-based Code Review System for Programming Language Learning** (2024) — arXiv · cites 1 · score 9 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2407.04722
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The increasing demand for programming language education and growing class sizes require immediate and personalized feedback. However, traditional code review methods have limitations in providing this level of feedback. As the capabilities of Large Language Models (LLMs) like GPT for generating accurate solutions and timely code reviews are verified, this research proposes a system that…

### doi:10.48550/arxiv.2408.02544
**Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions** (2024) — arXiv (Cornell University) · cites 1 · score 9 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2408.02544
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
This paper investigates the faithfulness of multimodal large language model (MLLM) agents in a graphical user interface (GUI) environment, aiming to address the research question of whether multimodal GUI agents can be distracted by environmental context. A general scenario is proposed where both the user and the agent are benign, and the environment, while not…

### doi:10.18653/v1/2026.acl-long.1483
**Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective** (2026) — arXiv (Cornell University) · cites 1 · score 9 (strong 1) · periphery/interface_agents · doi:10.18653/v1/2026.acl-long.1483
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large language model (LLM) web agents are increasingly used for web navigation but remain far from human reliability on realistic, long-horizon tasks.Existing evaluations focus primarily on end-to-end success, offering limited insight into where failures arise.We propose a hierarchical planning framework to analyze web agents across three layers (i.e., high-level planning, low-level execution, and replanning), enabling…

### doi:10.48550/arxiv.2504.13865
**A Survey on (M)LLM-Based GUI Agents** (2025) — arXiv (Cornell University) · cites 1 · score 9 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2504.13865
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Graphical User Interface (GUI) Agents have emerged as a transformative paradigm in human-computer interaction, evolving from rule-based automation scripts to sophisticated AI-driven systems capable of understanding and executing complex interface operations. This survey provides a comprehensive examination of the rapidly advancing field of LLM-based GUI Agents, systematically analyzing their architectural foundations, technical components, and evaluation…

### doi:10.64898/2026.02.18.26346559
**In Search of Ethical Procedures for LLM-Assisted Systematic Review Production: A Proof-of-Concept Evaluation of Selected Review Components** (2026) — medRxiv · cites 1 · score 9 (strong 1) · periphery/science_of_science · doi:10.64898/2026.02.18.26346559
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
ABSTRACT Large language models (LLMs) are increasingly used in scientific writing, but the conditions under which they can be applied responsibly to evidence synthesis remain poorly defined. We conducted a proof-of-concept study examining selected components of the systematic review process rather than the systematic review as a whole, with the aim of identifying where LLM…

### doi:10.5120/ijca2024923651
**Building an AI-Native Software Engineering Team: A Stepwise Approach Using Multi-Agent Systems** (2024) — International Journal of Computer Applications · cites 0 · score 9 (strong 1) · periphery/software_engineering · doi:10.5120/ijca2024923651
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
The realm of Generative Artificial Intelligence (Gen AI) has propelled human ingenuity to unprecedented heights, promising to revolutionize the field of software engineering.Large Language Models (LLMs) and Generative Pre-trained Transformers are at the forefront of this transformation, reshaping the landscape of Software Engineering.With the integration of multi-agent systems, the evolution of software engineering is poised…

### doi:10.48550/arxiv.2606.13449
**Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2606.13449
signals: \bcopilots?\b;agentic;agentic*
touchpoints: none
AI-agents (e.g., GitHub Copilot) collaborate as teammates in different software engineering tasks, including code generation proposed through pull requests (Agentic-PRs). For better agent efficiency, developers create instruction files that guide the AI-agents, including how to navigate the project, locate the right components, run tests, respect best practices, and more. In this paper, we investigate the…

### doi:10.48550/arxiv.2603.15911
**Human-AI Synergy in Agentic Code Review** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2603.15911
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Code review is a critical software engineering practice where developers review code changes before integration to ensure code quality, detect defects, and improve maintainability. In recent years, AI agents that can understand code context, plan review actions, and interact with development environments have been increasingly integrated into the code review process. However, there is limited…

### doi:10.48550/arxiv.2505.23422
**From Knowledge to Noise: CTIM-Rover and the Pitfalls of Episodic Memory in Software Engineering Agents** (2025) — arXiv (Cornell University) · cites 0 · score 9 (strong 3) · periphery/software_engineering · doi:10.48550/arxiv.2505.23422
signals: \bAI agents?\b;\bReAct\b;agentic
touchpoints: none
We introduce CTIM-Rover, an AI agent for Software Engineering (SE) built on top of AutoCodeRover (Zhang et al., 2024) that extends agentic reasoning frameworks with an episodic memory, more specifically, a general and repository-level Cross-Task-Instance Memory (CTIM). While existing open-source SE agents mostly rely on ReAct (Yao et al., 2023b), Reflexion (Shinn et al., 2023),…

### doi:10.48550/arxiv.2609.00252
**Spec-Driven Development for Agentic Software Engineering: Harnessing Human-Agent Teamwork** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2609.00252
signals: agentic;agentic*;autonomous agents?
touchpoints: none
Context: Software engineering is moving from AI-assisted practices like vibe coding, in which assistants accelerate individual developers, towards Agentic Software Engineering (ASE), in which autonomous agents are delegated goal-level tasks. However, industry reports a productivity paradox: as individual productivity increases, team throughput, review capacity, and stability degrade because team-scale software engineering discipline is neglected. Objective:…

### doi:10.54097/d6775287
**A Review of Research on AI-Assisted Code Generation and AI-Driven Code Review** (2025) — Academic Journal of Science and Technology · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.54097/d6775287
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\bcopilots?\b
touchpoints: none
With the significant breakthroughs of deep learning technologies such as large language models (LLMs) in the field of code analysis, AI has evolved from an auxiliary tool to a key technology that deeply participates in code optimization and resolving performance issues. As modern software system architectures become increasingly complex, the requirements for their performance have…

### arxiv:2603.16107
**RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2603.16107
signals: \bLangGraph\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Repository-level code review requires reasoning over project structure, repository context, and file-level implementation details. Existing automated review workflows often collapse these tasks into a single pass, which can reduce relevance, increase duplication, and weaken prioritization. We present RepoReviewer, a local-first multi-agent system for automated GitHub repository review with a Python CLI, FastAPI API, LangGraph orchestration…

### doi:10.63282/3050-9246.ijetcsit-v4i2p124
**Context-Aware IDE Systems Using Large Language Models and Semantic Memory Architectures** (2023) — International Journal of Emerging Trends in Computer Science and Information Technology · cites 0 · score 9 (strong 1) · periphery/software_engineering · doi:10.63282/3050-9246.ijetcsit-v4i2p124
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
The fast evolution of software engineering practices has made the integrated development environment (IDE) increasingly complex and required the evolution of intelligent systems to interpret the intent of the developer, the contextual programming patterns and the long-term semantic relationships in large-scale software repositories. The syntax-aware compilation engines, static code analysis mechanisms, and rule-based auto-completion frameworks…

### title:evaluatingandimprovingthereliabilityofllmgeneratedcoderefactorings
**Evaluating and Improving the Reliability of LLM-Generated Code Refactorings** (2026) — QSpace (Queen's University Library) · cites 0 · score 9 (strong 1) · periphery/software_engineering · https://hdl.handle.net/1974/36882
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
With the rapid advancement of Large Language Models (LLMs), there is growing interest in leveraging these models to automate software engineering tasks such as code refactoring. Code refactoring aims to improve the internal quality of software systems without altering their external behavior, making it a critical activity for long-term maintainability. While prior work has demonstrated…

### doi:10.48448/k8mg-8q47
**SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks** (2025) — Underline Science Inc. · cites 0 · score 9 (strong 1) · periphery/software_engineering · doi:10.48448/k8mg-8q47
signals: agentic;agentic*
touchpoints: none
The rapid advancement of Large Language Models (LLMs) in software engineering has revealed critical limitations in existing benchmarks, particularly the widely used SWE-bench dataset. Recent studies have uncovered severe data contamination issues, e.g. SWE-bench~\cite{jimenez2023swe} reports 32.67\% of successful patches involve direct solution leakage and 31.08\% pass due to inadequate test cases. We introduce \textbf{SWE-MERA}, a…

### doi:10.48550/arxiv.2607.09524
**Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2607.09524
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Code review is a cornerstone of software development, where reviewers provide feedback through written comments to ensure code quality, maintainability, and correctness. The effectiveness of this process hinges on the quality of review comments. As large language models (LLMs) gain traction in automating code review tasks, the utility of these systems is directly limited by…

### doi:10.1145/3786583.3786851
**RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · periphery/software_engineering · doi:10.1145/3786583.3786851
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large Language Models (LLMs)-powered code review automation has the potential to transform code review workflows. Despite the advances of LLM-powered code review comment generation approaches, several practical challenges remain for designing enterprise-grade code review automation tools. In particular, this paper aims at answering the practical question: how can we design a review-guided, context-aware, quality-checked code…

### doi:10.48550/arxiv.2606.11042
**Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2606.11042
signals: \bAI agents?\b;agentic;agentic*
touchpoints: none
Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-value professional workflows across diverse domains. Current GUI benchmarks still predominantly focus on general-purpose software, relatively simple applications, and short-horizon tasks, leaving it largely…

### doi:10.48550/arxiv.2605.12481
**ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents** (2026) — arXiv (Cornell University) · cites 0 · score 9 (strong 3) · periphery/interface_agents · doi:10.48550/arxiv.2605.12481
signals: [a-z]{3,}-mcp\b;\btool[- ]use\b;agentic
touchpoints: none
Computer Use Agents (CUAs) can act through both atomic GUI actions, such as click and type, and high-level tool calls, such as API-based file operations, but this hybrid action space often leaves them uncertain about when to continue with GUI actions or switch to tools, leading to suboptimal execution paths. This difficulty stems from the…

### doi:10.1109/sp63933.2026.00042
**Investigating the Impact of Dark Patterns on LLM-Based Web Agents** (2026) — arXiv · cites 0 · score 9 (strong 1) · periphery/interface_agents · doi:10.1109/sp63933.2026.00042
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
As users increasingly turn to large language model (LLM) based web agents to automate online tasks, agents may encounter dark patterns: deceptive user interface designs that manipulate users into making unintended decisions. Although dark patterns primarily target human users, their potentially harmful impacts on LLM-based generalist web agents remain unexplored. In this paper, we present…

### doi:10.3390/axioms15060415
**Graph-Structured Persistent Memory for Efficient LLM-Based Computer Use Agents** (2026) — Axioms · cites 0 · score 9 (strong 1) · periphery/interface_agents · doi:10.3390/axioms15060415
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large language model (LLM)-driven computer use agents (CUAs) automate graphical user interface (GUI) tasks but often re-solve previously encountered subtasks, increasing token use and latency. We address this limitation with a directed graph-based persistent memory in which nodes represent observable GUI states and edges encode executable action sequences. We formalize the memory-augmented agent as S=⟨A,Σ,G,δ,π,Φ⟩,…

### doi:10.48550/arxiv.2505.22942
**WorkForceAgent-R1: Incentivizing Reasoning Capability in LLM-based Web Agents via Reinforcement Learning** (2025) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2505.22942
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large language models (LLMs)-empowered web agents enables automating complex, real-time web navigation tasks in enterprise environments. However, existing web agents relying on supervised fine-tuning (SFT) often struggle with generalization and robustness due to insufficient reasoning capabilities when handling the inherently dynamic nature of web interactions. In this study, we introduce WorkForceAgent-R1, an LLM-based web agent…

### doi:10.20944/preprints202604.1148.v1
**Functional Stability and Adaptive Control in LLM-Based Computer Use Agents via Graph-Structured Persistent Memory** (2026) — Preprints.org · cites 0 · score 9 (strong 1) · periphery/interface_agents · doi:10.20944/preprints202604.1148.v1
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Large language model (LLM)-driven computer use agents (CUAs) automate graphical user interface (GUI) tasks but often re-solve previously encountered subtasks, increasing token use, latency, and instability. We address this limitation with a directed graph-based persistent memory in which nodes represent observable GUI states and edges encode executable action sequences. We formalize the memory-augmented agent as…

### doi:10.1145/3808097
**PlayCoder: Making LLM-Generated GUI Code Playable** (2026) — Proceedings of the ACM on software engineering. · cites 0 · score 9 (strong 2) · periphery/interface_agents · doi:10.1145/3808097
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|
touchpoints: none
Large language models (LLMs) have transformed code generation, but their ability to generate code for applications with graphical user interfaces (GUIs), particularly games, remains underexplored. Prior code-generation benchmarks assess correctness using test cases, but this is insufficient for GUI applications. These applications are interactive and event-driven, and their correctness depends on stateful behavior over sequences…

### doi:10.48550/arxiv.2504.11281
**The Obvious Invisible Threat: LLM-Powered GUI Agents' Vulnerability to Fine-Print Injections** (2025) — arXiv (Cornell University) · cites 0 · score 9 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2504.11281
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
A Large Language Model (LLM) powered GUI agent is a specialized autonomous system that performs tasks on the user's behalf according to high-level instructions. It does so by perceiving and interpreting the graphical user interfaces (GUIs) of relevant apps, often visually, inferring necessary sequences of actions, and then interacting with GUIs by executing the actions…

### arxiv:2508.04412
**Beyond Pixels: Exploring DOM Downsampling for LLM-Based Web Agents** (2025) — arXiv · cites 0 · score 9 (strong 1) · periphery/interface_agents · arXiv:2508.04412
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
The advent of large language models (LLMs) has sparked an evolution of autonomous web browsing agents: given a web browsing task and serialised user interface (UI) state, an LLM is expected to suggest input actions that incrementally solve the given task. The central challenge lies in serialising UI state for LLMs. Web agents have increasingly…

### doi:10.3390/systems14060722
**Generative AI for IT Project Management: A Systematic Review and Future Research Agenda** (2026) — Systems · cites 0 · score 9 (strong 2) · periphery/science_of_science · doi:10.3390/systems14060722
signals: \bAI agents?\b;agentic
touchpoints: none
Nowadays, the literature on Generative AI (GenAI) in Information Technology (IT) project management is fragmented, focusing mainly on isolated tools, specific process groups, or practitioners’ perspectives, without offering a comprehensive synthesis. Therefore, there is a lack of systematic reviews to guide researchers in effectively and responsibly leveraging GenAI, including emerging innovations such as AI agents.…

### doi:10.5281/zenodo.19354154
**Ep. 106: Why Your AI Needs a Mouse and a Universal Power Strip** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 2) · periphery/interface_agents · doi:10.5281/zenodo.19354154
signals: agentic;model context protocol
touchpoints: tool_exposure
Episode summary: In this episode of My Weird Prompts, Herman and Corn explore the evolution of human-computer interaction, starting with Grace Hopper's vision in the 1950s and leading into the cutting-edge AI of late 2025. They break down the difference between simple chatbots and "Computer Use Agents" that can actually see and manipulate a computer…

### doi:10.1145/3650212.3680384
**AutoCodeRover: Autonomous Program Improvement** (2024) — arXiv (Cornell University) · cites 142 · score 8 (strong 2) · periphery/software_engineering · doi:10.1145/3650212.3680384
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLLM[- ]?agents?\b
touchpoints: none
Researchers have made significant progress in automating the software development process in the past decades. Automated techniques for issue summarization, bug reproduction, fault localization, and program repair have been built to ease the workload of developers. Recent progress in Large Language Models (LLMs) has significantly impacted the development process, where developers can use LLM-based programming…

### doi:10.1016/j.ijmedinf.2024.105531
**Implementation and evaluation of an additional GPT-4-based reviewer in PRISMA-based medical systematic literature reviews** (2024) — International Journal of Medical Informatics · cites 38 · score 8 (strong 1) · periphery/science_of_science · doi:10.1016/j.ijmedinf.2024.105531
signals: \bLangChain\b
touchpoints: none
BACKGROUND: PRISMA-based literature reviews require meticulous scrutiny of extensive textual data by multiple reviewers, which is associated with considerable human effort. OBJECTIVE: To evaluate feasibility and reliability of using GPT-4 API as a complementary reviewer in systematic literature reviews based on the PRISMA framework. METHODOLOGY: A systematic literature review on the role of natural language…

### doi:10.1109/icse-seip66354.2025.00038
**Evaluating Agent-Based Program Repair at Google** (2025) — arXiv · cites 14 · score 8 (strong 2) · periphery/software_engineering · doi:10.1109/icse-seip66354.2025.00038
signals: \btool[- ]use\b;agentic
touchpoints: none
Agent-based program repair offers to automatically resolve complex bugs end-to-end by combining the planning, tool use, and code generation abilities of modern LLMs. Recent work has explored the use of agent-based repair approaches on the popular open-source SWE-Bench [1], a collection of bugs from highly-rated GitHub Python projects. In addition, various agentic approaches such as…

### doi:10.1109/mlcad62225.2024.10740262
**Automated C/C++ Program Repair for High-Level Synthesis via Large Language Models** (2024) — arXiv (Cornell University) · cites 14 · score 8 (strong 1) · periphery/software_engineering · doi:10.1109/mlcad62225.2024.10740262
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
In High-Level Synthesis (HLS), converting a regular C/C++ program into its HLS-compatible counterpart (HLS-C) still requires tremendous manual effort. Various program scripts have been introduced to automate this process. But the resulting codes usually contain many issues that should be manually repaired by developers. Since Large Language Models (LLMs) have the ability to automate code…

### doi:10.1109/saner64311.2025.00068
**Evaluating Software Development Agents: Patch Patterns, Code Quality, and Issue Complexity in Real-World GitHub Scenarios** (2025) — arXiv (Cornell University) · cites 7 · score 8 (strong 2) · periphery/software_engineering · doi:10.1109/saner64311.2025.00068
signals: agent(?:ic)? workflows?;agentic
touchpoints: none
In recent years, AI-based software engineering has progressed from pre-trained models to advanced agentic workflows, with Software Development Agents representing the next major leap. These agents, capable of reasoning, planning, and interacting with external environments, offer promising solutions to complex software engineering tasks. However, while much research has evaluated code generated by large language models…

### doi:10.1145/3691620.3695291
**Unity Is Strength: Collaborative LLM-Based Agents for Code Reviewer Recommendation** (2024) — n/a · cites 7 · score 8 (strong 1) · periphery/software_engineering · doi:10.1145/3691620.3695291
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Assigning pull requests to appropriate code reviewers can accelerate the review process and help uncover potential bugs. However, the inherent complexities in pull requests and code reviewers present challenges in making suitable matches between them. Prior studies focus on mining rich semantic information from pull requests or profile information from code reviewers to improve efficiency.…

### doi:10.48550/arxiv.2507.23348
**SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution** (2025) — arXiv (Cornell University) · cites 2 · score 8 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2507.23348
signals: \btool[- ]using\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Issue resolution has made remarkable progress thanks to the advanced reasoning capabilities of large language models (LLMs). Recently, agent-based frameworks such as SWE-agent have further advanced this progress by enabling autonomous, tool-using agents to tackle complex software engineering tasks. While existing agent-based issue resolution approaches are primarily based on agents' independent explorations, they often get…

### doi:10.1097/icu.0000000000001179
**Toward autonomous discovery: agentic AI and the future of ophthalmic research** (2025) — Current Opinion in Ophthalmology · cites 2 · score 8 (strong 1) · periphery/science_of_science · doi:10.1097/icu.0000000000001179
signals: agentic;agentic*
touchpoints: none
PURPOSE OF REVIEW: Rapid advances in large language models (LLMs) have led to the emergence of agentic artificial intelligence (AI) systems capable of autonomously performing complex scientific tasks. This review examines recent developments in agentic AI, highlighting their transformative potential for ophthalmology research and clinical practice, and discusses associated ethical considerations. RECENT FINDINGS: Recent studies…

### doi:10.48550/arxiv.2601.14470
**Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering** (2026) — arXiv (Cornell University) · cites 1 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2601.14470
signals: agentic;agentic*
touchpoints: none
LLM-based Multi-Agent (LLM-MA) systems are increasingly applied to automate complex software engineering tasks such as requirements engineering, code generation, and testing. However, their operational efficiency and resource consumption remain poorly understood, hindering practical adoption due to unpredictable costs and environmental impact. To address this, we conduct an analysis of token consumption patterns in an LLM-MA…

### doi:10.1093/geroni/igaf122.1472
**Doing Systematic Literature Reviews With Artificial Intelligence Tools: What, Why, and How** (2025) — Innovation in Aging · cites 1 · score 8 (strong 2) · periphery/science_of_science · doi:10.1093/geroni/igaf122.1472
signals: \bLLM[- ]?agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Abstract Systematic reviews are indispensable to evidence-based practice but require considerable time and effort, particularly in screening large numbers of studies. Recent advances in large language models (LLMs) offer a promising avenue to reduce this burden through partial automation of the process. We present a two-stage multi-agent framework that leverages LLMs—to supplement human expertise—in conducting…

### doi:10.48550/arxiv.2605.17548
**Rethinking Code Review in the Age of AI: A Vision for Agentic Code Review** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2605.17548
signals: agentic;agentic*
touchpoints: none
Code review has evolved for decades, from informal peer checking to today's pull request (PR) workflows, yet it remains a largely manual and cognitively demanding process. The rise of Artificial Intelligence (AI) coding assistants has intensified this challenge: while these tools increase code production velocity, they also expand the volume of code requiring review, turning…

### doi:10.56038/oprd.v7i1.739
**A Modular Semantic Kernel Agent for Automated Code Review and Refactoring Feedback** (2025) — Orclever Proceedings of Research and Development · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.56038/oprd.v7i1.739
signals: agentic
touchpoints: none
In modern software development, maintaining clean, efficient, and reliable code is critical to team productivity and product quality. This paper introduces a modular Large Language Model (LLM)-based agent, designed using Microsoft’s Semantic Kernel framework, for automated code review and refactoring feedback. The agent leverages plugin-based function orchestration, Retrieval-Augmented Generation (RAG), and dynamic prompt engineering to…

### doi:10.48550/arxiv.2510.16059
**SIADAFIX: issue description response for adaptive program repair** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2510.16059
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);agent(?:ic)? workflows?
touchpoints: none
We propose utilizing fast and slow thinking to enhance the capabilities of large language model-based agents on complex tasks such as program repair. In particular, we design an adaptive program repair method based on issue description response, called SIADAFIX. The proposed method utilizes slow thinking bug fix agent to complete complex program repair tasks, and…

### doi:10.48550/arxiv.2601.18418
**daVinci-Dev: Agent-native Mid-training for Software Engineering** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2601.18418
signals: agent(?:ic)? workflows?;agentic
touchpoints: none
Recently, the frontier of Large Language Model (LLM) capabilities has shifted from single-turn code generation to agentic software engineering-a paradigm where models autonomously navigate, edit, and test complex repositories. While post-training methods have become the de facto approach for code agents, **agentic mid-training**-mid-training (MT) on large-scale data that mirrors authentic agentic workflows-remains critically underexplored due…

### doi:10.48550/arxiv.2606.12986
**The Rise of AI-Native Software Engineering: Implications for Practice, Education, and the Future Workforce** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2606.12986
signals: agent orchestration;agentic
touchpoints: none
Generative Artificial Intelligence (GenAI), Large Language Models (LLMs), and emerging Agentic AI constitute the most disruptive transformation in the history of software engineering (SE), reshaping development processes, required competencies, professional roles, and the educational outcomes that universities must deliver. This paper presents a systematic review of 48 verified, influential peer-reviewed publications (2016--2026) drawn from leading…

### doi:10.48550/arxiv.2601.08857
**Revisiting Software Engineering Education in the Era of Large Language Models: A Curriculum Adaptation and Academic Integrity Framework** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2601.08857
signals: \bcopilots?\b
touchpoints: none
The integration of Large Language Models (LLMs), such as ChatGPT and GitHub Copilot, into professional workflows is increasingly reshaping software engineering practices. These tools have lowered the cost of code generation, explanation, and testing, while introducing new forms of automation into routine development tasks. In contrast, most of the software engineering and computer engineering curricula…

### doi:10.1109/snpd65828.2025.11253974
**Evaluating the Source Code Review Performance of LLM-based AI Chatbots** (2025) — n/a · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.1109/snpd65828.2025.11253974
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Source code review plays a critical role in ensuring software quality by identifying bugs early in the development process. Although recent studies have explored the use of large language models (LLMs) for tasks such as vulnerability detection and automated code refinement, few studies have evaluated their performance against human reviewers during the review phase. In…

### doi:10.70917/ijcisim-2026-4666
**AgentCodeReview: Implementation and Comprehensive Benchmark Evaluation of a Multi-Agent Framework for Explainable Code Review and Automated Bug Repair** (2026) — International Journal of Computer Information Systems and Industrial Management Applications · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.70917/ijcisim-2026-4666
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Large Language Models (LLMs) have revolutionized software development, from analyzing code and generating suggestions to detecting bugs and errors, and even creating entire programs. Despite these advances, existing AI-driven code review solutions still provide a one-size-fits-all approach to code review with overall feedback and suggestions, often of a non-specific nature. This restriction promotes modular architectures…

### doi:10.48550/arxiv.2510.04905
**Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2510.04905
signals: autonomous agents?
touchpoints: none
Recent advances in large language models (LLMs) have significantly improved automated code generation. While existing approaches have achieved strong performance at the function and file levels, real-world software engineering requires reasoning over entire repositories, including cross-file dependencies, evolving execution environments, and global semantic consistency. This challenge has led to the emergence of Repository-Level Code Generation…

### doi:10.1145/3797126
**Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis** (2026) — Proceedings of the ACM on software engineering. · cites 0 · score 8 (strong 2) · periphery/software_engineering · doi:10.1145/3797126
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);autonomous agents?
touchpoints: none
Autonomous agents for automated program repair represent a promising frontier in software engineering, yet their effectiveness is often hindered by reliance on post-mortem, coarse-grained execution feedback. While integrating traditional interactive debuggers seems a natural solution, their low-level, line-by-line interaction paradigm turns to be cost-inefficient for LLM-based agents, leading to exhausted budgets and unproductive loops. To…

### title:aiikodproduktionochgranskningenjmfrandeanalysavllmbaseradeverktygjmfrtmedmnskligexpertis
**AI i kodproduktion och granskning : En jämförande analys av LLM-baserade verktyg jämfört med mänsklig expertis** (2026) — Diva portal (Dalarna University Library) · cites 0 · score 8 (strong 1) · periphery/software_engineering · http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-383091
signals: \bAI agents?\b
touchpoints: none
This thesis investigates the reliability and quality of AI-generated code compared to human expertise in a professional software development context, with findings relevant to developers, software engineering students, and others who work with code production and review in practical settings. Specifically, it compares a Large Language Model (Gemini 3 Pro) against human developers in code…

### doi:10.48550/arxiv.2603.26567
**Beyond Code Snippets: Benchmarking LLMs on Repository-Level Question Answering** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2603.26567
signals: agentic
touchpoints: none
Large Language Models (LLMs) have shown impressive capabilities across software engineering tasks, including question answering (QA). However, most studies and benchmarks focus on isolated functions or single-file snippets, overlooking the challenges of real-world program comprehension, which often spans multiple files and system-level dependencies. In this work, we introduce StackRepoQA, the first multi-project, repository-level question answering…

### doi:10.5281/zenodo.18276514
**Replication Package for "Beyond Code Snippets: Benchmarking LLMs on Repository-Level Question Answering"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.18276514
signals: agentic
touchpoints: none
Large Language Models (LLMs) have shown impressive capabilities across software engineering tasks, including question answering (QA). However, most studies and benchmarks focus on isolated functions or single-file snippets, overlooking the challenges of real-world program comprehension, which often spans multiple files and system-level dependencies. In this work, we introduce StackRepoQA, the first multi-project, repository-level question answering…

### title:usageofgenerativeaibasedplugininunittestingevaluatingthetrustworthinessofgeneratedtestcasesbycodiumateanidepluginpowered
**Usage of Generative AI Based Plugin in Unit Testing : Evaluating the Trustworthiness of Generated Test Cases by Codiumate, an IDE Plugin Powered by GPT-3.5 & 4** (2024) — Diva portal (Dalarna University Library) · cites 0 · score 8 (strong 1) · periphery/software_engineering · http://urn.kb.se/resolve?urn=urn:nbn:se:bth-26473
signals: \bcopilots?\b
touchpoints: none
Background: Unit testing is essential in software development, ensuring the functionality of individual components like functions and classes. However, manual creation of unit test cases is time-consuming and tedious, impacting testing efficiency and reliability. Problem: Automated unit test generation tools such as EvoSuite and Randoop have addressed some challenges, but they’re limited by language specificity…

### doi:10.66485/jsti.v1i3.34
**Software Engineer Competency Framework in the Era of Generative AI: A Literature Review** (2026) — Jurnal Serumpun Teknik Informatika · cites 0 · score 8 (strong 1) · periphery/science_of_science · doi:10.66485/jsti.v1i3.34
signals: \bcopilots?\b
touchpoints: none
Generative artificial intelligence (GenAI) technologies such as Claude Code, ChatGPT, and GitHub Copilot are fundamentally reshaping software development practices, shifting the core activities of software engineers from direct code authoring toward validation, orchestration, and architectural reasoning. This paradigm shift raises fundamental questions: what competencies do software engineers require to collaborate effectively alongside GenAI, and how…

### doi:10.5281/zenodo.20722987
**Empirical Lyapunov Stability: Growth-Ratio Energy Functions as Leading Indicators of Agent Task Failure** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.20722987
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
In our prior theoretical work, we proposed a physics-inspired framework for governing the semantic boundary layer of multi-agent AI systems, drawing on Lyapunov stability theory, Renormalization Group compression, and Vector Symbolic Architectures. That framework was a theoretical edifice; mathematically grounded but empirically unverified. This paper presents its empirical validation through a 5-condition ablation study (3,175…

### doi:10.1109/ubmk67458.2025.11206953
**Software Unit Test Automation with LLM-Based Generative AI: Evaluating Test Quality through Code Coverage and Edge-Case Analysis** (2025) — n/a · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.1109/ubmk67458.2025.11206953
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Software unit testing is a critical verification step to ensure the correctness and reliability of software. However, manual writing of test cases is a time-consuming and error-prone process. This paper examines the integration of generative artificial intelligence models (LLM) into software test engineering and addresses automatic unit test generation. In the proposed method, test functions…

### doi:10.48550/arxiv.2609.06780
**Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2609.06780
signals: agentic;agentic*
touchpoints: none
While autonomous software engineering (SWE) agents achieve high benchmark resolution rates, these scores can mask exploitative behaviors---such as leveraging local Git histories, accessing upstream repositories, or recalling memorized solutions---rather than demonstrating genuine problem solving. We systematize and audit these exploits across five open large language models on SWE-bench Multilingual and DeepSWE using a turn-level LLM-as-a-judge…

### doi:10.3390/electronics15163694
**A Formal Trustworthiness Construct for Large Language Model-Based Test Generation: A Multidimensional Index Empirically Evaluated Through a Multi-Agent Study** (2026) — Electronics · cites 0 · score 8 (strong 1) · periphery/software_engineering · doi:10.3390/electronics15163694
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Software code testing remains a critically important but labour-intensive process in software quality assurance. Existing research evaluates large language model (LLM)-based unit test generation using various quality metrics, such as correctness, coverage, mutation score, and test code smells. However, these single metrics do not reflect the trustworthiness of the unit test generation process. Therefore, this…

### doi:10.55041/ijcope.v2i8.072
**TEXA OS: Self Improving Agentic AI and Safe Task Automation** (2026) — International Journal of Creative and Open Research in Engineering and Management · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.55041/ijcope.v2i8.072
signals: agentic;agentic*
touchpoints: none
Conversational AI assistants such as Siri, Google Assistant, and ChatGPT have improved how users interact with digital systems, yet they remain confined to answering questions rather than completing real-world tasks. Users must still manually open applications, navigate websites, fill out forms, and switch between software to finish even simple workflows, which limits productivity and creates…

### doi:10.48550/arxiv.2510.02418
**BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2510.02418
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
LLM web agents now browse and take actions on the open web, yet current agent evaluations are constrained to sandboxed environments or artificial tasks. We introduce BrowserArena, a live open-web agent evaluation platform that collects user-submitted tasks, runs Arena-style head-to-head comparisons, and uses step-level human feedback to surface failure modes. Collecting and analyzing step-level annotations…

### doi:10.48550/arxiv.2504.12682
**WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2504.12682
signals: \bLLM[- ]?agents?\b;\bLLM[- ]?agents?\b*
touchpoints: none
Most recent web agent research has focused on navigation and transaction tasks, with little emphasis on extracting structured data at scale. We present WebLists, a benchmark of 200 data-extraction tasks across four common business and enterprise use-cases. Each task requires an agent to navigate to a webpage, configure it appropriately, and extract complete datasets with…

### arxiv:2503.11069
**API Agents vs. GUI Agents: Divergence and Convergence** (2025) — arXiv · cites 0 · score 8 (strong 2) · periphery/interface_agents · arXiv:2503.11069
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bLLM[- ]?agents?\b
touchpoints: none
Large language models (LLMs) have evolved beyond simple text generation to power software agents that directly translate natural language commands into tangible actions. While API-based LLM agents initially rose to prominence for their robust automation capabilities and seamless integration with programmatic endpoints, recent progress in multimodal LLM research has enabled GUI-based LLM agents that interact…

### doi:10.48550/arxiv.2608.04741
**LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2608.04741
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
LLM-based web agents automate user tasks by observing webpages and executing browser actions on behalf of users. As these agents operate on real web services, login becomes a sensitive authentication boundary because it involves credentials and sensitive information. Existing work shows that malicious webpage content can manipulate web agent actions, but it has not fully…

### arxiv:2602.09222
**MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks** (2026) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2602.09222
signals: agentic;agentic*
touchpoints: none
Large language model (LLM) based web agents are increasingly deployed to automate complex online tasks by directly interacting with web sites and performing actions on users' behalf. While these agents offer powerful capabilities, their design exposes them to indirect prompt injection attacks embedded in untrusted web content, enabling adversaries to hijack agent behavior and violate…

### doi:10.48550/arxiv.2509.13704
**InfraMind: A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management** (2025) — arXiv (Cornell University) · cites 0 · score 8 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2509.13704
signals: agentic;agentic*
touchpoints: none
Mission-critical industrial infrastructure, such as data centers, increasingly depends on complex management software. Its operations, however, pose significant challenges due to the escalating system complexity, multi-vendor integration, and a shortage of expert operators. While Robotic Process Automation (RPA) offers partial automation through handcrafted scripts, it suffers from limited flexibility and high maintenance costs. Recent advances…

### arxiv:2509.06501
**WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents** (2025) — arXiv · cites 0 · score 8 (strong 2) · periphery/interface_agents · arXiv:2509.06501
signals: agentic;tool[- ]calling
touchpoints: none
The paradigm of Large Language Models (LLMs) has increasingly shifted toward agentic applications, where web browsing capabilities are fundamental for retrieving information from diverse online sources. However, existing open-source web agents either demonstrate limited information-seeking abilities on complex tasks or lack transparent implementations. In this work, we identify that the key challenge lies in the…

### arxiv:2504.20464
**A Survey on GUI Agents with Foundation Models Enhanced by Reinforcement Learning** (2025) — arXiv · cites 0 · score 8 (strong 1) · periphery/interface_agents · arXiv:2504.20464
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Graphical User Interface (GUI) agents, driven by Multi-modal Large Language Models (MLLMs), have emerged as a promising paradigm for enabling intelligent interaction with digital systems. This paper provides a structured survey of recent advances in GUI agents, focusing on architectures enhanced by Reinforcement Learning (RL). We first formalize GUI agent tasks as Markov Decision Processes…

### doi:10.1111/1742-6723.70243
**The Potential for Artificial Intelligence to Augment Peer Review** (2026) — Emergency Medicine Australasia · cites 0 · score 8 (strong 1) · periphery/science_of_science · doi:10.1111/1742-6723.70243
signals: \bAI agents?\b
touchpoints: none
Artificial intelligence (AI) is a new technology that represents a promising tool to augment the scientific peer-review process, particularly by addressing the challenges of scalability, consistency and bias in the review process. The term AI was formally introduced by computer scientist John McCarthy in 1955 as a part of a proposal for the famous 1956…

### doi:10.5281/zenodo.19538011
**Council of Models: How Karpathy Built AI Peer Review** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 8 (strong 1) · periphery/science_of_science · doi:10.5281/zenodo.19538011
signals: \bAI agents?\b
touchpoints: none
Episode summary: In November, Andrej Karpathy released llm-council, a deceptively simple system that treats language models like an academic council: four frontier models answer questions independently, then anonymously rank each other's responses, and a Chairman model synthesizes the results. The architecture packs deliberate design choices into just 800 lines of code—including a clever anonymization scheme,…

### arxiv:2510.16549
**ReviewGuard: Enhancing Deficient Peer Review Detection via LLM-Driven Data Augmentation** (2025) — arXiv · cites 0 · score 8 (strong 1) · periphery/science_of_science · arXiv:2510.16549
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Peer review serves as the gatekeeper of science, yet the surge in submissions and widespread adoption of large language models (LLMs) in scholarly evaluation present unprecedented challenges. While recent work has focused on using LLMs to improve review efficiency, unchecked deficient reviews from both human experts and AI systems threaten to systematically undermine academic integrity.…

### doi:10.5281/zenodo.17911042
**smith6jt-cop/KINTSUGI: v1.2.0** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.17911042
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bcopilots?\b
touchpoints: config_generation;hpc_scale_out;tool_exposure
Changelog All notable changes to KINTSUGI will be documented in this file. The format is based on Keep a Changelog, and this project adheres to Semantic Versioning. Unreleased 1.2.0 - 2025-12-12 Added release: add automatic release versioning system integrate Claude Code with KINTSUGI for AI-assisted image processing; add MCP server commands and update documentation add…

### doi:10.5281/zenodo.14984518
**smith6jt-cop/KINTSUGI: v1.2.3** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.14984518
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bcopilots?\b
touchpoints: config_generation;hpc_scale_out;tool_exposure
Changelog All notable changes to KINTSUGI will be documented in this file. The format is based on Keep a Changelog, and this project adheres to Semantic Versioning. Unreleased 1.2.3 - 2025-12-12 Changed Merge branch 'main' of https://github.com/smith6jt-cop/KINTSUGI Refactor MCP configuration process and enhance project setup 1.2.2 - 2025-12-12 Changed Fix badge formatting in README.md 1.2.1…

### doi:10.5281/zenodo.17912340
**smith6jt-cop/KINTSUGI: v1.2.1** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.17912340
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bcopilots?\b
touchpoints: config_generation;hpc_scale_out;tool_exposure
Changelog All notable changes to KINTSUGI will be documented in this file. The format is based on Keep a Changelog, and this project adheres to Semantic Versioning. Unreleased 1.2.1 - 2025-12-12 Changed Merge branch 'main' of https://github.com/smith6jt-cop/KINTSUGI Update project setup and configuration files 1.2.0 - 2025-12-12 Added release: add automatic release versioning system integrate Claude…

### doi:10.5281/zenodo.17913982
**smith6jt-cop/KINTSUGI: v1.2.2** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.17913982
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bcopilots?\b
touchpoints: config_generation;hpc_scale_out;tool_exposure
Changelog All notable changes to KINTSUGI will be documented in this file. The format is based on Keep a Changelog, and this project adheres to Semantic Versioning. Unreleased 1.2.2 - 2025-12-12 Changed Fix badge formatting in README.md 1.2.1 - 2025-12-12 Changed Merge branch 'main' of https://github.com/smith6jt-cop/KINTSUGI Update project setup and configuration files 1.2.0 - 2025-12-12…

### doi:10.48550/arxiv.2506.07672
**MCPWorld: A Unified Benchmarking Testbed for API, GUI, and Hybrid Computer Use Agents** (2025) — arXiv (Cornell University) · cites 2 · score 7 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2506.07672
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);model context protocol
touchpoints: tool_exposure
(M)LLM-powered computer use agents (CUA) are emerging as a transformative technique to automate human-computer interaction. However, existing CUA benchmarks predominantly target GUI agents, whose evaluation methods are susceptible to UI changes and ignore function interactions exposed by application APIs, e.g., Model Context Protocol (MCP). To this end, we propose MCPWorld, the first automatic CUA testbed…

### doi:10.1109/saner67736.2026.00024
**Agentic Pipelines in Embedded Software Engineering: Emerging Practices and Challenges** (2026) — arXiv (Cornell University) · cites 1 · score 7 (strong 1) · periphery/software_engineering · doi:10.1109/saner67736.2026.00024
signals: agentic;agentic*
touchpoints: provenance_reproducibility
A new transformation is underway in software engineering, driven by the rapid adoption of generative AI in development workflows. Similar to how version control systems once automated manual coordination, AI tools are now beginning to automate many aspects of programming. For embedded software engineering organizations, however, this marks their first experience integrating AI into safety-critical…

### doi:10.48550/arxiv.2606.03394
**Human-AI Collaboration and the Transformation of Software Engineering Work** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2606.03394
signals: agent orchestration;agentic
touchpoints: verification_regression
The integration of Generative AI (GenAI) and Agentic AI into software development is reconfiguring software engineering from an activity centered on human authorship of code into a discipline centered on directing, verifying, and governing autonomous and semi-autonomous systems. Drawing on a curated, multi-source evidence base of recent peer-reviewed and archival studies -- including large-scale empirical…

### doi:10.5281/zenodo.19423014
**Pixels vs Protocols: The Computer Use Showdown** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/interface_agents · doi:10.5281/zenodo.19423014
signals: \bAI agents?\b;model context protocol
touchpoints: tool_exposure
Episode summary: The podcast explores the architectural tension between visual "Computer Use" agents—like Anthropic's demo—and API-first automation. Hosts analyze whether visual agents are a high-latency bridge to a protocol-driven world or a necessary tool for legacy systems. They discuss cost implications, reliability issues, and the potential for visual interaction to become just another capability rather…

### doi:10.48550/arxiv.2604.09815
**EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2604.09815
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b;model context protocol
touchpoints: tool_exposure
Computer-use agents that combine GUI interaction with structured API calls via the Model Context Protocol (MCP) show promise for automating software tasks. However, existing approaches lack a principled understanding of how agents should balance these two modalities and how to enable iterative self-improvement across diverse applications. We formulate MCP-GUI interplay as a unified hybrid policy…

### doi:10.1136/bjo-2024-326254
**Can large language models fully automate or partially assist paper selection in systematic reviews?** (2025) — British Journal of Ophthalmology · cites 23 · score 7 (strong 1) · periphery/science_of_science · doi:10.1136/bjo-2024-326254
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
BACKGROUND/AIMS: Large language models (LLMs) have substantial potential to enhance the efficiency of academic research. The accuracy and performance of LLMs in a systematic review, a core part of evidence building, has yet to be studied in detail. METHODS: We introduced two LLM-based approaches of systematic review: an LLM-enabled fully automated approach (LLM-FA) utilising three…

### doi:10.18260/1-2--46557
**An Exploratory Study on Upper-Level Computing Students’ Use of Large Language Models as Tools in a Semester-Long Project** (2024) — arXiv (Cornell University) · cites 9 · score 7 (strong 1) · periphery/software_engineering · doi:10.18260/1-2--46557
signals: \bcopilots?\b
touchpoints: none
Background: Large Language Models (LLMs) have begun to influence software engineering practice since the public release of GitHub's Copilot and OpenAI's ChatGPT in 2022.Tools built on LLM technology could revolutionize the way software engineering is practiced, offering interactive "assistants" that can answer questions and prototype software.It falls to software engineering educators to teach future software…

### doi:10.1109/llm4code66737.2025.00019
**Analysis of Student-LLM Interaction in a Software Engineering Project** (2025) — arXiv (Cornell University) · cites 5 · score 7 (strong 1) · periphery/software_engineering · doi:10.1109/llm4code66737.2025.00019
signals: \bcopilots?\b
touchpoints: none
Large Language Models (LLMs) are becoming increasingly competent across various domains, educators are showing a growing interest in integrating these LLMs into the learning process. Especially in software engineering, LLMs have demonstrated qualitatively better capabilities in code summarization, code generation, and debugging. Despite various research on LLMs for software engineering tasks in practice, limited research…

### doi:10.1109/icst62969.2025.10988960
**Poster: Unit Testing Past vs. Present: Examining LLMs' Impact on Defect Detection and Efficiency** (2025) — n/a · cites 4 · score 7 (strong 1) · periphery/software_engineering · doi:10.1109/icst62969.2025.10988960
signals: \bcopilots?\b
touchpoints: none
The integration of Large Language Models (LLMs), such as ChatGPT and GitHub Copilot, into software engineering workflows has shown potential to enhance productivity, particularly in software testing. This paper investigates whether LLM support improves defect detection effectiveness during unit testing. Building on prior studies comparing manual and tool-supported testing, we replicated and extended an experiment…

### doi:10.1145/3728981
**SWE-GPT: A Process-Centric Language Model for Automated Software Improvement** (2025) — Proceedings of the ACM on software engineering. · cites 4 · score 7 (strong 1) · periphery/software_engineering · doi:10.1145/3728981
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Large language models (LLMs) have demonstrated remarkable performance in code generation, significantly enhancing the coding efficiency of developers. Recent advancements in LLM-based agents have led to significant progress in end-to-end automatic software engineering (ASE), particularly in software maintenance (e.g., fixing software issues) and evolution (e.g., adding new features). Despite these encouraging advances, current research faces…

### doi:10.18653/v1/2025.acl-long.1523
**Completing A Systematic Review in Hours instead of Months with Interactive AI Agents** (2025) — arXiv · cites 4 · score 7 (strong 1) · periphery/science_of_science · doi:10.18653/v1/2025.acl-long.1523
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
Systematic reviews (SRs) are vital for evidencebased practice in high stakes disciplines, such as healthcare, but are often impeded by laborintensive and lengthy processes that can span months.Due to the high demand for domain expertise, existing automatic summarization methods fail to accurately identify relevant studies and generate high-quality summaries.To that end, we introduce InsightAgent, a…

### doi:10.1111/jdv.20354
**Will AI revolutionize literature reviews?** (2024) — Journal of the European Academy of Dermatology and Venereology · cites 3 · score 7 (strong 1) · periphery/science_of_science · doi:10.1111/jdv.20354
signals: \bcopilots?\b
touchpoints: none
The study by Passby et al. on artificial intelligence (AI)-generated dermatology literature reviews provides valuable insights into the potential of AI to transform scientific publishing, particularly in literature reviews.1 Their evaluation of three AI tools—The Literature, Microsoft's Copilot and Google's Gemini—across five dermatology topics demonstrated that AI-generated reviews could serve as a useful resource for…

### doi:10.4018/979-8-3373-0370-3.ch007
**Generative AI in Software Engineering Education** (2025) — Advances in computational intelligence and robotics book series · cites 2 · score 7 (strong 1) · periphery/software_engineering · doi:10.4018/979-8-3373-0370-3.ch007
signals: \bcopilots?\b
touchpoints: none
Generative AI has revolutionized numerous fields, including software engineering education. Tools like GitHub Copilot, ChatGPT, or Llama have reshaped learning by offering real-time suggestions, automating code generation, and enhancing debugging. However, software engineering encompasses far more than writing code—it spans requirements analysis, specification, design, implementation, testing, deployment, maintenance, configuration management, etc. The rise of generative…

### doi:10.1007/s10489-026-07230-0
**Code generation with large language models: a survey from neural program synthesis to autonomous software development** (2026) — Applied Intelligence · cites 2 · score 7 (strong 1) · periphery/software_engineering · doi:10.1007/s10489-026-07230-0
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Abstract Large language models have reshaped code generation, driving a transition from rule-based and statistical methods to transformer-based architectures pretrained on vast code corpora. This survey traces the intellectual lineage from classical program synthesis through pre-transformer neural approaches to contemporary large-scale models, examining code generation capabilities across model architectures, training strategies, task taxonomies, evaluation methodologies,…

### doi:10.52202/085713-0537
**Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks** (2025) — arXiv · cites 1 · score 7 (strong 1) · periphery/software_engineering · doi:10.52202/085713-0537
signals: \bLLM[- ]?agents?\b
touchpoints: none
Recent advances in Large Language Models (LLMs) have shown promise in function-level code generation, yet repository-level software engineering tasks remain challenging. Current solutions predominantly rely on proprietary LLM agents, which introduce unpredictability and limit accessibility, raising concerns about data privacy and model customization. This paper investigates whether open-source LLMs can effectively address repository-level tasks without…

### doi:10.18653/v1/2025.findings-emnlp.411
**Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents** (2025) — arXiv (Cornell University) · cites 1 · score 7 (strong 1) · periphery/interface_agents · doi:10.18653/v1/2025.findings-emnlp.411
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Graphical user interface (GUI) agents powered by multimodal large language models (MLLMs) have shown greater promise for human-interaction.However, due to the high fine-tuning cost, users often rely on opensource GUI agents or APIs offered by AI providers, which introduces a critical but underexplored supply chain threat: backdoor attacks.In this work, we first unveil that MLLMpowered…

### arxiv:2602.01465
**Agyn: A Multi-Agent System for Team-Based Autonomous Software Engineering** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2602.01465
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)*
touchpoints: none
Large language models have demonstrated strong capabilities in individual software engineering tasks, yet most autonomous systems still treat issue resolution as a monolithic or pipeline-based process. In contrast, real-world software development is organized as a collaborative activity carried out by teams following shared methodologies, with clear role separation, communication, and review. In this work, we…

### doi:10.5281/zenodo.19734492
**Cloud Patch Intelligence: An Autonomous AI Agent for Cloud Misconfiguration Detection and Automated Remediation via GitHub Pull Requests** (2026) — International Journal of Emerging Trends in Engineering and Development · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.19734492
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
Abstract Cloud infrastructure misconfigurations represent the leading cause of cloud security breaches, accounting for over 80% of incidents and costing organizations an average of $4.45 million per breach. Despite the availability of scanning tools, a critical gap exists: detection without automated remediation forces security teams to manually write fixes, open pull requests, and review changes…

### arxiv:2512.21426
**What Makes a GitHub Issue Ready for Copilot?** (2025) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2512.21426
signals: \bcopilots?\b;\bcopilots?\b*
touchpoints: none
AI-agents help developers in different coding tasks, such as developing new features, fixing bugs, and reviewing code. Developers can write a Github issue and assign it to an AI-agent like Copilot for implementation. Based on the issue and its related discussion, the AI-agent performs a plan for the implementation, and executes it. However, the performance…

### doi:10.5281/zenodo.19249555
**An Autonomy-Aware Metamodel for Human–AI Collaboration in Software Engineering** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.19249555
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language);multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
This spreadsheet contains the detailed data and modeling artifacts used in the study “An Autonomy-Aware Metamodel for Human–AI Collaboration in Software Engineering.” It documents how the proposed metamodel is instantiated on a concrete multi-agent LLM system for automated requirements analysis and prioritization in an agile software engineering context. The file encodes each task in the…

### arxiv:2512.23631
**BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization** (2025) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2512.23631
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large language models (LLMs) have shown strong reasoning and coding capabilities, yet they struggle to generalize to real-world software engineering (SWE) problems that are long-horizon and out of distribution. Existing systems often rely on a single agent to handle the entire workflow-interpreting issues, navigating large codebases, and implementing fixes-within one reasoning chain. Such monolithic designs…

### title:evaluatingaigeneratedtsqlcodereviewreportsinanenterprisescalecodebase
**Evaluating AI-Generated T-SQL Code Review Reports in an Enterprise-Scale Codebase** (2026) — Doria (University of Helsinki) · cites 0 · score 7 (strong 2) · periphery/software_engineering · https://www.doria.fi/handle/10024/194633
signals: \bcopilots?\b;\btool[- ]using\b
touchpoints: none
The use of generative AI in software development has rapidly increased, and there are signs that AI-assisted software development might allow developers to produce software faster. In some applications, however, the software development process requires a non-author human developer to approve any suggested changes in a code review before the changes can be applied. Code…

### doi:10.1109/iccta68914.2025.11520024
**Context-Aware Pipeline for Automated Code Review Using Large Language Models** (2025) — n/a · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.1109/iccta68914.2025.11520024
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Modern software projects are increasingly complex, placing significant demands on human reviewers during code review. While review is essential for ensuring quality, security, and maintainability, the rapid growth of contributions in large repositories often overwhelms reviewer capacity, leading to delays and inconsistent feedback. Existing automated tools, such as linters and static analyzers, provide only surface-level…

### doi:10.14569/ijacsa.2026.0170478
**The Impact of Modern AI on Software Development: A Systematic Literature Review** (2026) — International Journal of Advanced Computer Science and Applications · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.14569/ijacsa.2026.0170478
signals: \bAI agents?\b;agentic
touchpoints: none
As large language models, and agentic AI systems are increasingly being integrated into software engineering, an expanding amount of empirical evidence surrounding these technologies has emerged. This systematic literature review examines the impact of modern AI techniques and tools in software development lifecycle phases and related activities, covering studies published between 2023 and 2025 and…

### doi:10.48550/arxiv.2608.29204
**AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.48550/arxiv.2608.29204
signals: \bcopilots?\b;agentic
touchpoints: none
Generative AI-based software engineering agents are becoming routine contributors to real-world software projects. On GitHub, developers can assign tasks to the Copilot cloud agent, which autonomously explores the repository, edits code, runs commands, and opens or reviews pull requests, producing a detailed log of every step along the way. While existing datasets capture outcomes of…

### doi:10.1145/3821433
**Streamlining Repository Tasks with Effective Snippet Retrieval** (2026) — ACM Transactions on Software Engineering and Methodology · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.1145/3821433
signals: agent(?:ic)? workflows?;agentic
touchpoints: none
Repository-level software engineering tasks are increasingly automated using repo-level retrieval-augmented generation (RLRAG), where a retriever selects relevant snippets from a repository to assist a language model (LM) in completing tasks. However, existing retrievers often lack effective designs to support LMs of varying capacities. To bridge this gap, we introduce RepoET, a novel retriever for RLRAG.…

### doi:10.1109/apsec66846.2025.00028
**MUATC: Multi-Agent Utilization to Augment Test Coverage** (2025) — n/a · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.1109/apsec66846.2025.00028
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Unit testing, as a critical means of ensuring software quality, is often constrained in practice by the high cost and low efficiency of manual test case construction, resulting in limited test coverage and scarcity of unit test cases in real-world projects. Traditional test generation tools can improve coverage but suffer from poor readability and limited…

### doi:10.70315/uloap.ulirs.2026.0301009
**Accelerating Mobile Application Development and Testing with Artificial Intelligence: A Systematic Literature Review** (2026) — Universal Library of Innovative Research and Studies · cites 0 · score 7 (strong 2) · periphery/science_of_science · doi:10.70315/uloap.ulirs.2026.0301009
signals: \bLLM[- ]?agents?\b;multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
The article presents a systematic literature review examining how artificial intelligence methods (LLM/GenAI, computer vision, deep learning, and multi-agent architectures) accelerate mobile application development and testing within the mobile SDLC. The objective is to address a deficit of domain-specific systematisation for mobile engineering and to answer three classes of questions: which AI approaches are applied…

### arxiv:2512.22753
**From Rookie to Pro: Social Engineering LLMs for Automated Vulnerability Exploitation in Enterprise Software** (2025) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2512.22753
signals: \bcopilots?\b
touchpoints: none
LLMs democratize software engineering by enabling non-programmers to create applications, but this same accessibility fundamentally undermines security assumptions that have guided software engineering for decades. We show in this work how publicly available LLMs can be socially engineered to transform novices into capable attackers, challenging the foundational principle that exploitation requires technical expertise. To that…

### doi:10.48550/arxiv.2502.09801
**Unit Testing Past vs. Present: Examining LLMs' Impact on Defect Detection and Efficiency** (2025) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2502.09801
signals: \bcopilots?\b
touchpoints: none
The integration of Large Language Models (LLMs), such as ChatGPT and GitHub Copilot, into software engineering workflows has shown potential to enhance productivity, particularly in software testing. This paper investigates whether LLM support improves defect detection effectiveness during unit testing. Building on prior studies comparing manual and tool-supported testing, we replicated and extended an experiment…

### doi:10.5281/zenodo.21781711
**Dissecting Repository-Scale Code-Agent Harnesses: Retrieval, Context, and Action Interfaces Under Model-in-the-Loop Evaluation** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 7 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.21781711
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);\bReAct\b
touchpoints: none
A five-study controlled evaluation of repository-navigation and editing harnesses for local LLM coding agents. The release reports 5,453 audited experimental cells across three public repositories and three local models. Study 5 contributes 2,826 model-in-the-loop cells covering lexical, syntax, and dense retrieval components; retrieval-by-action interactions; graph, query, tool, and packing ablations; and a 17-task held-out validation.…

### arxiv:2509.14635
**SWE-QA: Can Language Models Answer Repository-level Code Questions?** (2025) — arXiv · cites 0 · score 7 (strong 2) · periphery/software_engineering · arXiv:2509.14635
signals: \bLLM[- ]?agents?\b;agentic
touchpoints: none
Understanding and reasoning about entire software repositories is an essential capability for intelligent software engineering tools. While existing benchmarks such as CoSQA and CodeQA have advanced the field, they predominantly focus on small, self-contained code snippets. These setups fail to capture the complexity of real-world repositories, where effective understanding and reasoning often require navigating multiple…

### title:automatedprogramrepairandtheadventoflargelanguagemodelsinsoftwareengineering
**Automated Program Repair and the Advent of Large Language Models in Software Engineering** (2025) — Open Research (University of Surrey) · cites 0 · score 7 (strong 1) · periphery/software_engineering · https://bia.unibz.it/esploro/outputs/doctoral/Automated-Program-Repair-and-the-Advent/991007095712701241
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Within just a few years, large language models have made the jump from research labs to the mainstream. Intelligent assistants building on this technology, such as OpenAI’s ChatGPT, Google’s Gemini or Mistral’s le Chat, have already been commercialized and are today used by millions, on smartphones and in web browsers. The recent advancements in AI…

### title:exploringtheuseoflargelanguagemodelsfordataextractionforsystematicreviewsinsoftwareengineering
**Exploring the Use of Large Language Models for Data Extraction for Systematic Reviews in Software Engineering** (2025) — KTH Publication Database DiVA (KTH Royal Institute of Technology) · cites 0 · score 7 (strong 1) · periphery/science_of_science · http://urn.kb.se/resolve?urn=urn:nbn:se:miun:diva-55634
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
To support evidence-based decision-making, software engineering employs systematic reviews to collect and consolidate relevant literature on a specific research topic. However, conducting systematic reviews is a labor-intensive and time-consuming task. Recent advancements in Large Language Models (LLMs), such as Generative Pre-trained Transformer (GPT) models, offer opportunities to streamline and reduce the manual effort required, particularly…

### doi:10.1145/3786580.3786990
**Prompting Without Principles: Are Students Transferring Software Engineering Knowledge to LLM Use?** (2026) — n/a · cites 0 · score 7 (strong 1) · periphery/software_engineering · doi:10.1145/3786580.3786990
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Generative AI (GenAI), in particular large language models (LLMs), have rapidly become part of software engineers’ toolboxes. While the software engineering community has been actively debating efficacy and extent of use of GenAI tools, little is known about how early-career developers apply these tools and transfer their classroom training into practice. To address this gap,…

### doi:10.48550/arxiv.2605.14290
**Web Agents Should Adopt the Plan-Then-Execute Paradigm** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 2) · periphery/interface_agents · doi:10.48550/arxiv.2605.14290
signals: \bLLM[- ]?agents?\b;\bReAct\b
touchpoints: none
ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. We argue that it is the wrong default for web agents. Instead, web agents should default to plan-then-execute: commit to a task-specific program before observing runtime web content, then execute it. The reason is that web content mixes…

### arxiv:2605.21082
**AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions** (2026) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2605.21082
signals: \bReAct\b
touchpoints: none
Large Language Model (LLM) based agents have demonstrated proficiency in multi-step interactions with graphical user interfaces (GUIs). While most research focuses on improving single-task performance, practical scenarios often involve repetitive GUI tasks for which invoking LLM reasoning repeatedly, i.e., the ReAct paradigm, is inefficient. Prior to LLMs, traditional Robotic Process Automation (RPA) offers runtime efficiency…

### arxiv:2509.26539
**Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents** (2025) — arXiv · cites 0 · score 7 (strong 2) · periphery/interface_agents · arXiv:2509.26539
signals: \btool[- ]use\b;autonomous agents?
touchpoints: none
Developing autonomous agents that effectively interact with Graphic User Interfaces (GUIs) remains a challenging open problem, especially for small on-device models. In this paper, we present Ferret-UI Lite, a compact, end-to-end GUI agent that operates across diverse platforms, including mobile, web, and desktop. Utilizing techniques optimized for developing small models, we build our 3B Ferret-UI…

### doi:10.1109/icme59968.2025.11209200
**G-TADS: GUI Task-Ability Decoupling Strategy for High-Adaptability Multimodal Intelligent Agents** (2025) — n/a · cites 0 · score 7 (strong 1) · periphery/interface_agents · doi:10.1109/icme59968.2025.11209200
signals: \b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b;\b(?:modell?ing|simulation|analysis|interpretation|advisory|research|smart|intelligent|expert|domain)\s+agents?\b*
touchpoints: none
Graphical User Interface (GUI) automation aims to help users interact with devices efficiently, and the integration of open-source multimodal large language models (MLLMs) with GUI agents shows great potential in this area. However, existing open-source model-based solutions typically treat GUI tasks as a single end-to-end process, overlooking the optimization of input-output design and training strategies,…

### doi:10.48550/arxiv.2503.16465
**OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents** (2025) — arXiv (Cornell University) · cites 0 · score 7 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2503.16465
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+);(?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)
touchpoints: none
Autonomous graphical user interface (GUI) agents powered by multimodal large language models have shown great promise. However, a critical yet underexplored issue persists: over-execution, where the agent executes tasks in a fully autonomous way, without adequate assessment of its action confidence to compromise an adaptive human-agent collaboration. This poses substantial risks in complex scenarios, such…

### doi:10.1145/3797115
**WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements** (2026) — Proceedings of the ACM on software engineering. · cites 0 · score 7 (strong 1) · periphery/interface_agents · doi:10.1145/3797115
signals: agentic;agentic*
touchpoints: none
Visual language model (VLM) agents show great promise in automating graphical user interface (GUI) testing against requirements in natural language. However, the probabilistic nature of language models can have inherent hallucinations. Therefore, given a detected inconsistency between the requirement and the web application, it is hard to distinguish whether it stems from the hallucination or…

### doi:10.5281/zenodo.22209733
**Replication package for: How Well Do Technical Debt Metrics Capture the Task Resolution and Internal Cost of AI Agents?** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.22209733
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: hpc_scale_out;provenance_reproducibility;techno_economic
Replication package for the paper "How Well Do Technical Debt Metrics Capture the Task Resolution and Internal Cost of AI Agents? An Empirical Analysis across Three Benchmarks and Ten Languages" (submitted to Empirical Software Engineering). The paper combines three benchmarks — SWE-bench Verified, Multi-SWE-bench, and SWE-bench Multilingual — covering 10 programming languages, 193 agent submissions,…

### doi:10.5281/zenodo.22160868
**Replication package for: How Well Do Technical Debt Metrics Capture the Task Solving and Internal Cost of AI Agents?** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.22160868
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: hpc_scale_out;provenance_reproducibility
Replication package for the paper "How Well Do Technical Debt Metrics Capture the Task Solving and Internal Cost of AI Agents?" (submitted to Empirical Software Engineering). The paper combines three benchmarks — SWE-bench Verified, Multi-SWE-bench, and SWE-bench Multilingual — covering 10 programming languages, 193 agent submissions, and approximately 124,000 task instances, and empirically analyzes how…

### doi:10.2139/ssrn.7234653
**SWE-Exp: Experience-Driven Software Issue Resolution** (2026) — SSRN Electronic Journal · cites 3 · score 6 (strong 1) · periphery/software_engineering · doi:10.2139/ssrn.7234653
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: uncertainty_quantification
Recent advances in large language model (LLM) agents have shown remarkable progress in software issue resolution, leveraging advanced techniques such as multi-agent collaboration and Monte Carlo Tree Search (MCTS). However, current agents act as memoryless explorers - treating each problem separately without retaining or reusing knowledge from previous repair experiences. This leads to redundant exploration…

### doi:10.48550/arxiv.2509.16941
**SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?** (2025) — arXiv (Cornell University) · cites 2 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2509.16941
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: hpc_scale_out
We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer…

### doi:10.1145/3763097
**PReMM: LLM-Based Program Repair for Multi-method Bugs via Divide and Conquer** (2025) — Proceedings of the ACM on Programming Languages · cites 1 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3763097
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: hpc_scale_out
Large-language models (LLMs) have been leveraged to enhance the capability of automated program repair techniques in recent research. While existing LLM-based program repair techniques compared favorably to other techniques based on heuristics, constraint-solving, and learning in producing high-quality patches, they mainly target bugs that can be corrected by changing a single faulty method, which greatly…

### doi:10.48550/arxiv.2606.19167
**Teaching Software Engineering with LLM and MCP Integration: From Classroom to Industry Practice** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2606.19167
signals: model context protocol
touchpoints: tool_exposure
The rapid integration of Large Language Models (LLMs) and the Model Context Protocol (MCP) into industrial software engineering has created a pressing need to update software engineering education to align with emerging technologies and evolving industry demands. This study investigates an innovative approach that integrates LLMs and MCP into a collaborative teaching model for software…

### doi:10.5281/zenodo.20084564
**GoodshytGroup/asterocrypta-celestial-linguistics: Citation.md** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.20084564
signals: \bMCP[\s-]?(?:server|client|suite|framework|architecture|based|tool);\bcopilots?\b
touchpoints: tool_exposure
What's Changed Enhance README with GitHub profile and README tips by @GoodshytGroup in https://github.com/GoodshytGroup/asterocrypta-celestial-linguistics/pull/47 Revert "Enhance README with GitHub profile and README tips" by @GoodshytGroup in https://github.com/GoodshytGroup/asterocrypta-celestial-linguistics/pull/48 Revert "Revert "Enhance README with GitHub profile and README tips"" by @GoodshytGroup in https://github.com/GoodshytGroup/asterocrypta-celestial-linguistics/pull/49 Main by @GoodshytGroup in https://github.com/GoodshytGroup/asterocrypta-celestial-linguistics/pull/50 Update README with project details, tips, and image sources…

### title:containerizedframeworkforllmenhancedoffensivecyberoperations
**CONTAINERIZED FRAMEWORK FOR LLM-ENHANCED OFFENSIVE CYBER OPERATIONS** (2026) — Calhoun: The Naval Postgraduate School Institutional Archive (Naval Postgraduate School) · cites 0 · score 6 (strong 1) · periphery/interface_agents · https://hdl.handle.net/10945/75679
signals: model context protocol
touchpoints: tool_exposure
This thesis presents a containerized framework that uses large language models (LLMs) to control offensive cyber tools through natural language. The research addresses challenges in military cyber operations such as mastering diverse tool syntax and deployment in air-gap environments. The research has three phases. Phase one involved Nmap integration with cloud-based language models, establishing natural…

### doi:10.30935/ojcmt/18689
**Agentic AI-driven creative media management in mass communication Education 5.0: A PRISMA-guided mixed-methods systematic review and bibliometric analysis** (2026) — Online Journal of Communication and Media Technologies · cites 0 · score 6 (strong 1) · periphery/science_of_science · doi:10.30935/ojcmt/18689
signals: agentic;agentic*
touchpoints: hpc_scale_out
Education 5.0 is driving a paradigmatic shift toward human-centered, artificial intelligence (AI)-enabled learning ecologies in which Agentic AI autonomously orchestrates creative media production, content management, and instructional design. This study offers a mixed-methods systematic review of Agentic AI-driven creative media management in mass communication education, integrating bibliometric and qualitative evidence to address the current fragmentation…

### doi:10.1145/3661167.3661216
**Using Large Language Models to Generate JUnit Tests: An Empirical Study** (2024) — arXiv (Cornell University) · cites 85 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3661167.3661216
signals: \bcopilots?\b
touchpoints: none
A code generation model generates code by taking a prompt from a code comment, existing code, or a combination of both. Although code generation models (e.g., GitHub Copilot) are increasingly being adopted in practice, it is unclear whether they can successfully be used for unit test generation without fine-tuning for a strongly typed language like…

### doi:10.1145/3643757
**CodePlan: Repository-Level Coding using LLMs and Planning** (2024) — Proceedings of the ACM on software engineering. · cites 76 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3643757
signals: \bcopilots?\b
touchpoints: none
Software engineering activities such as package migration, fixing error reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code. We formulate these activities as repository-level coding tasks. Recent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have…

### doi:10.1016/j.infsof.2025.107751
**Copiloting the future: How generative AI transforms Software Engineering** (2025) — Information and Software Technology · cites 47 · score 6 (strong 1) · periphery/software_engineering · doi:10.1016/j.infsof.2025.107751
signals: \bcopilots?\b
touchpoints: none
Context With rapid technological advancements, artificial intelligence (AI) has become integral to various sectors. Generative AI (GenAI) tools like ChatGPT or GitHub Copilot, with their unique content creation capabilities, pose transformative potential in Software Engineering by offering new ways to optimize software development processes. However, the integration into current processes also presents challenges that require…

### doi:10.1145/3593230
**Evaluating a Large Language Model on Searching for GUI Layouts** (2023) — Proceedings of the ACM on Human-Computer Interaction · cites 40 · score 6 (strong 1) · periphery/interface_agents · doi:10.1145/3593230
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
The field of generative artificial intelligence has seen significant advancements in recent years with the advent of large language models, which have shown impressive results in software engineering tasks but not yet in engineering user interfaces. Thus, we raise a specific research question: would an LLM-based system be able to search for relevant GUI layouts?…

### doi:10.1021/acs.iecr.4c04636
**Artificial Intelligence Meets Laboratory Automation in Discovery and Synthesis of Metal–Organic Frameworks: A Review** (2025) — Industrial & Engineering Chemistry Research · cites 36 · score 6 (strong 1) · periphery/lab_automation · doi:10.1021/acs.iecr.4c04636
signals: self[- ]driving lab
touchpoints: none
Abstract This review discusses the transformative impact of the convergence of artificial intelligence (AI) and laboratory automation on the discovery and synthesis of metal–organic frameworks (MOFs). MOFs, known for their tunable structures and extensive applications in fields such as energy storage, drug delivery, and environmental remediation, pose significant challenges due to their complex synthesis processes…

### doi:10.1109/icse55347.2025.00080
**SpecRover: Code Intent Extraction via LLMs** (2025) — arXiv (Cornell University) · cites 19 · score 6 (strong 1) · periphery/software_engineering · doi:10.1109/icse55347.2025.00080
signals: \bLLM[- ]?agents?\b
touchpoints: none
Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent. Since program repair or program improvement typically requires a specification of intended behavior - specification inference can be…

### doi:10.1145/3696410.3714842
**Large Language Models Empowered Personalized Web Agents** (2025) — arXiv (Cornell University) · cites 12 · score 6 (strong 1) · periphery/interface_agents · doi:10.1145/3696410.3714842
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Web agents have emerged as a promising direction to automate Web task completion based on user instructions, significantly enhancing user experience. Recently, Web agents have evolved from traditional agents to Large Language Models (LLMs)-based Web agents. Despite their success, existing LLM-based Web agents overlook the importance of personalized data (e.g., user profiles and historical Web…

### doi:10.1109/cseet62301.2024.10663035
**University Students' Perception and Expectations of Generative AI Tools for Software Engineering** (2024) — n/a · cites 7 · score 6 (strong 1) · periphery/software_engineering · doi:10.1109/cseet62301.2024.10663035
signals: \bcopilots?\b
touchpoints: none
Adopting Generative Artificial Intelligence (AI) tools in software engineering represents a shift in how tasks like coding and idea generation are approached. This paper investigates uni-versity students' perceptions and expectations regarding the use of Generative AI tools such as ChatGPT and Copilot in software engineering. To achieve this, we conducted a questionnaire study with volunteer…

### doi:10.1145/3763791
**CITYWALK : Enhancing LLM-Based C++ Unit Test Generation via Project-Dependency Awareness and Language-Specific Knowledge** (2025) — ACM Transactions on Software Engineering and Methodology · cites 7 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3763791
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Unit testing plays a pivotal role in the software development lifecycle, as it ensures code quality. However, writing high-quality unit tests remains a time-consuming task for developers in practice. More recently, the application of large language models (LLMs) in automated unit test generation has demonstrated promising results. Existing approaches primarily focus on interpreted programming languages…

### doi:10.1109/icsme64153.2025.00061
**Automated Code Review Using Large Language Models at Ericsson: An Experience Report** (2025) — arXiv (Cornell University) · cites 4 · score 6 (strong 1) · periphery/software_engineering · doi:10.1109/icsme64153.2025.00061
signals: \btool[- ]using\b
touchpoints: none
Code review is one of the primary means of assuring the quality of released software along with testing and static analysis. However, code review requires experienced developers who may not always have the time to perform an in-depth review of code. Thus, automating code review can help alleviate the cognitive burden on experienced software developers…

### doi:10.1109/botse67031.2025.00013
**Supporting Brainstorming Activities with Bots in Software Engineering Education** (2025) — n/a · cites 3 · score 6 (strong 1) · periphery/software_engineering · doi:10.1109/botse67031.2025.00013
signals: \bcopilots?\b
touchpoints: none
The recent rise in the performance and availability of large language models (LLMs) has fueled the adoption of generative artificial intelligence (AI) to support software engineering. Technologies such as Copilot and ChatGPT have become ubiquitous in software engineering, both in academic and professional settings. Nevertheless, the effects of such technologies on how engineers collaborate to…

### doi:10.52202/085713-1502
**OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents** (2025) — arXiv · cites 2 · score 6 (strong 1) · periphery/interface_agents · doi:10.52202/085713-1502
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Computer use agents are LLM-based agents that can directly interact with a graphical user interface, by processing screenshots or accessibility trees. While these systems are gaining popularity, their safety has been largely overlooked, despite the fact that evaluating and understanding their potential for harmful behavior is essential for widespread adoption. To address this gap, we…

### doi:10.1051/epjconf/202533701066
**Leveraging Large Language Models for Enhanced Code Review** (2025) — EPJ Web of Conferences · cites 1 · score 6 (strong 1) · periphery/software_engineering · doi:10.1051/epjconf/202533701066
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
This paper presents an innovative approach to software code review using Large Language Models (LLMs), incorporating open-source models. We introduce Pearbot, an open-source tool that implements a comprehensive code review workflow using open-weights LLMs, featuring multi-agent capabilities and reflection mechanisms. Our approach demonstrates the potential for LLMs to identify code issues and suggest improvements that…

### doi:10.5281/zenodo.18008772
**Why and When Agentic Pull Requests are (not) Accepted: An Exploratory Study** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 1 · score 6 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.18008772
signals: agentic;agentic*
touchpoints: none
Recently, Coding Agents gained considerable impact on software engineering processes such as on reviews, tests, documentation, code generation, but also pull requests. Those Agentic Pull Requests flood repositories, and thus, cause considerable effort for integrators that must review these pull requests. However, so far it is unclear which factors influence the acceptance of Agentic Pull…

### doi:10.64509/jicn.21.45
**GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph** (2026) — Journal of Intelligent Computing and Networking · cites 1 · score 6 (strong 1) · periphery/interface_agents · doi:10.64509/jicn.21.45
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Mobile graphical user interface (GUI) agents are designed to automate everyday tasks on smartphones. Recent advances in large language models (LLMs) have significantly enhanced the capabilities of mobile GUI agents. However, most LLM-powered mobile GUI agents operate in stepwise query-act loops, which incur high latency due to repeated LLM queries. We present GraphPilot, a mobile…

### doi:10.48550/arxiv.2509.14189
**AI and the Future of Academic Peer Review** (2025) — arXiv (Cornell University) · cites 1 · score 6 (strong 1) · periphery/science_of_science · doi:10.48550/arxiv.2509.14189
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Peer review remains the central quality-control mechanism of science, yet its ability to fulfill this role is increasingly strained. Empirical studies document serious shortcomings: long publication delays, escalating reviewer burden concentrated on a small minority of scholars, inconsistent quality and low inter-reviewer agreement, and systematic biases by gender, language, and institutional prestige. Decades of human-centered…

### doi:10.17605/osf.io/ugkv5
**Safe Implementation of Agentic Artificial Intelligence in Palliative Care: A Systematic Review** (2026) — n/a · cites 1 · score 6 (strong 1) · periphery/science_of_science · doi:10.17605/osf.io/ugkv5
signals: agentic;agentic*
touchpoints: none
This research project is a systematic review examining the safe implementation of agentic artificial intelligence in palliative care. Agentic AI refers to artificial intelligence systems capable of goal-directed recommendation, planning, adaptive interaction, workflow initiation, or partially autonomous decision support. While such systems may help improve patient identification, prognostication, advance care planning, documentation, and symptom-management support,…

### doi:10.31305/rrijm.2026.v11.n04.031
**Role of Artificial Intelligence in Revolutionizing Lesson Plan for teaching: A Systematic Review** (2026) — RESEARCH REVIEW International Journal of Multidisciplinary · cites 1 · score 6 (strong 1) · periphery/science_of_science · doi:10.31305/rrijm.2026.v11.n04.031
signals: \bcopilots?\b
touchpoints: none
The use of artificial intelligence (AI) in school education is becoming increasingly important. It has significant effects on various dimensions of education system such as instructional practices, assessment strategies, and administrative processes. It also plays a vital role in instructional design or lesson plan. However no systematic review studies focus on summarising research on the…

### doi:10.22214/ijraset.2025.73299
**AI Agents in Software Engineering Optimizing Software Development Processes and Enhancing Security Management in Learning Management Systems** (2025) — International Journal for Research in Applied Science and Engineering Technology · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.22214/ijraset.2025.73299
signals: \bAI agents?\b;\bAI agents?\b*
touchpoints: none
The use of AI agents in software engineering is an area of research that offers remarkable possibilities to improve software development processes and security management in LMS. In this paper, we investigate the use of AI agents in LMS development, concerning the AI ability to automate software engineering tasks, enhance system performance and guarantee secure…

### doi:10.32996/jcsts.2025.7.12.57
**Software Engineering Practices: In the era of AI / LLMs** (2025) — Journal of Computer Science and Technology Studies · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.32996/jcsts.2025.7.12.57
signals: autonomous agents?
touchpoints: none
The software development landscape is going through a major shift as generative artificial intelligence (AI) tools, including code assistants and autonomous agents, become increasingly widespread. Recent industry surveys indicate that more than 75% of developers currently use or plan to adopt AI-based solutions, with approximately half of professional developers utilizing these tools daily. Furthermore, organizational…

### doi:10.1117/12.3105122
**Observatory software management in the era of AI-assisted software engineering** (2026) — n/a · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.1117/12.3105122
signals: autonomous agents?
touchpoints: none
Thanks to advancements in generative AI and Large Language Models (LLMs), the last five years have seen exponential growth in the adoption of AI-Assisted software engineering across many industries. Simple developer tools used for code completion, static analysis and syntax linting have been augmented by semi-autonomous agents, able to contribute to a broad set of…

### doi:10.48550/arxiv.2506.10954
**SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks** (2025) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.10954
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Constructing large-scale datasets for the GitHub issue resolution task is crucial for both training and evaluating the software engineering capabilities of Large Language Models (LLMs). However, the existing GitHub issue resolution data construction pipeline is challenging and labor-intensive. We identify three key limitations in existing pipelines: (1) test patches collected often omit binary file changes;…

### doi:10.48550/arxiv.2506.10987
**Chain of Draft for Software Engineering: Challenges in Applying Concise Reasoning to Code Tasks** (2025) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.10987
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Large language models (LLMs) have become vital tools for software development, but they often require verbose intermediate reasoning for complex code tasks, leading to high latency and costs. This research extends the Chain of Draft (CoD) method to software engineering, designing and evaluating multiple CoD variants tailored for code tasks. Through comprehensive experiments on all…

### doi:10.17605/osf.io/f89yc
**Observability Gaps in Agentic AI Decision Chains: A Systematic Review of Cybersecurity Implications** (2026) — Open Science Framework · cites 0 · score 6 (strong 1) · periphery/science_of_science · doi:10.17605/osf.io/f89yc
signals: agentic;agentic*
touchpoints: none
Agentic artificial intelligence (AI) systems—autonomous software entities capable of making sequential decisions across multiple services without human intervention—are increasingly deployed in production environments, including enterprise cloud platforms, financial systems, and critical infrastructure. Unlike traditional AI models that perform single-task predictions, agentic systems operate through complex decision chains involving tool invocation, multi-step reasoning, and adaptive behavior.…

### doi:10.48550/arxiv.2607.01916
**ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2607.01916
signals: language model agents?
touchpoints: none
Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where useful evidence is mixed with irrelevant code and logs. This paper presents ContextSniper, AntTrail's code-repair module for precision evidence selection in repository-level program repair, part of AntTrail's broader agent-memory…

### doi:10.5753/sbqs.2025.13875
**Impact of Generative Artificial Intelligence on Knowledge Management in Software Engineering: A Systematic Mapping Study** (2025) — n/a · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.5753/sbqs.2025.13875
signals: \bcopilots?\b
touchpoints: none
Context: In recent years, Generative Artificial Intelligence (GenAI) has emerged as a transformative technology with high potential across various organizational contexts. Leveraging techniques such as Natural Language Processing (NLP) and Large Language Models (LLMs), tools like ChatGPT, GitHub Copilot, and DALL-E have begun to facilitate information creation and retrieval, automate tasks, and optimize decision-making processes.…

### doi:10.5281/zenodo.21929389
**The Impact of Artificial Intelligence on Software Engineering: Productivity, Code Quality, Security, and the Changing Role of Software Engineers** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 2) · periphery/software_engineering · doi:10.5281/zenodo.21929389
signals: \bAI agents?\b;\bcopilots?\b
touchpoints: none
The Impact of Artificial Intelligence on Software Engineering:Productivity, Code Quality, Security, and the Changing Role of Software Engineers Muzaffar AbdukadirovSoftware Engineering · 2026 Abstract Artificial intelligence (AI) coding assistants are changing how software engineers write, review, test, and maintain software. This paper examines the effects of AI-assisted development across four areas: developer productivity, code quality,…

### doi:10.36647/ciml/05.02.a001
**A Deep Dive into LLM-Powered Code Review Tools: A Comparative Analysis** (2025) — Computational Intelligence and Machine Learning · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.36647/ciml/05.02.a001
signals: \bcopilots?\b
touchpoints: none
In the software development landscape, code review plays a vital role in maintaining high code quality and ensuring the reliability of software products. This is particularly crucial in the field of data science, characterized by sophisticated algorithms, intricate data pipelines, and a relentless pursuit of model accuracy. However, conventional code review practices often struggle to…

### title:generatinguicodeforscientificcommandlinetoolsusinglargelanguagemodels
**Generating UI Code for Scientific Command Line Tools Using Large Language Models** (2025) — Tampere University Institutional Repository (Tampere University) · cites 0 · score 6 (strong 1) · periphery/interface_agents · https://trepo.tuni.fi/handle/10024/226965
signals: \bcopilots?\b
touchpoints: none
This thesis explores the current capabilities and limitations of using artificial intelligence (AI) and large language models (LLMs) to generate user interface (UI) code. In the action research component of this thesis, a graphical user interface (GUI) was developed for VeRyPy, a scientific Python library for solving vehicle routing problems. The GUI code was generated…

### title:automatiseeritudvearaportitelahendaminellmagentideabilsstemaatilinekirjanduselevaade
**Automatiseeritud vearaportite lahendamine LLM agentide abil: süstemaatiline kirjanduse ülevaade** (2025) — DSpace repository (University of Tartu) · cites 0 · score 6 (strong 1) · periphery/science_of_science · https://hdl.handle.net/10062/117075
signals: language model agents?
touchpoints: none
The goal of this thesis is to evaluate the ability of large language model agents in resolving issue reports present in repositories. A systematic literature review following Kitchenham’s methodology is conducted. Systematic literature review covers studies published in 2023 and later. Articles for this systematic literature review were selected according to their relevance towards large…

### title:vibecodingandtechnicaldebtamultivocalliteraturereviewandmixedmethodsstudy
**VIBE CODING AND TECHNICALDEBT: A MULTIVOCAL LITERATUREREVIEW AND MIXED-METHODSSTUDY** (2026) — KTH Publication Database DiVA (KTH Royal Institute of Technology) · cites 0 · score 6 (strong 1) · periphery/software_engineering · http://urn.kb.se/resolve?urn=urn:nbn:se:mdh:diva-77343
signals: \bcopilots?\b
touchpoints: none
The rapid adoption of large language models (LLMs) such as ChatGPT and GitHub Copilot has introduced new AI-assisted development practices in software engineering. One emerging approach, commonly referred to as vibe coding, involves generating source code directly from natural-language descriptions, often reducing or bypassing traditional software engineering activities such as detailed design and architectural planning.…

### doi:10.48550/arxiv.2312.10101
**A Review of Repository Level Prompting for LLMs** (2023) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2312.10101
signals: \bcopilots?\b
touchpoints: none
As coding challenges become more complex, recent advancements in Large Language Models (LLMs) have led to notable successes, such as achieving a 94.6\% solve rate on the HumanEval benchmark. Concurrently, there is an increasing commercial push for repository-level inline code completion tools, such as GitHub Copilot and Tab Nine, aimed at enhancing developer productivity. This…

### arxiv:2606.11416
**MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2606.11416
signals: \bLLM[- ]?agents?\b
touchpoints: none
Repository-level benchmarks for evaluating Large Language Model (LLM) code repair on Secure Multi-Party Computation (MPC) software do not yet exist, and directly transplanting general-purpose benchmarks such as SWE-bench fails on three structural fronts: (i) MPC repositories are dominated by generic Python infrastructure rather than cryptographic logic; (ii) high-value MPC fixes lack the standardized tests rigid…

### arxiv:2602.12256
**Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3794763.3794828
signals: \bcopilots?\b
touchpoints: none
Unit testing is essential for verifying the functional correctness of code modules (e.g., classes, methods), but manually writing unit tests is often labor-intensive and time-consuming. Unit tests generated by tools that employ traditional approaches, such as search-based software testing (SBST), lack readability, naturalness, and practical usability. LLMs have recently provided promising results and become integral…

### arxiv:2607.01929
**Beyond Textual Repository Exploration: Dual-Modal Structural Reasoning for Agentic Issue Resolution** (2026) — arXiv · cites 0 · score 6 (strong 1) · periphery/software_engineering · arXiv:2607.01929
signals: agentic;agentic*
touchpoints: none
Recent advances in agentic program repair have significantly improved issue resolution by enabling iterative repository exploration. However, existing approaches predominantly rely on sequential, text-based code navigation, which fundamentally limits their ability to reason over large-scale long-horizon repositories with complex and long-range dependencies. As issue-resolution agents traverse repositories through fragmented textual observations, structural information such as…

### arxiv:2507.19942
**Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem Solving** (2025) — arXiv · cites 0 · score 6 (strong 1) · periphery/software_engineering · arXiv:2507.19942
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large Language Models (LLMs) have shown remarkable capabilities in automating software engineering tasks, spurring the emergence of coding agents that scaffold LLMs with external tools to resolve repository-level problems. However, existing agents still struggle to navigate large-scale codebases, as the Needle-in-a-Haystack problem persists even with million-token context windows, where relevant evidence is often overwhelmed by…

### arxiv:2504.14757
**SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs** (2025) — arXiv · cites 0 · score 6 (strong 1) · periphery/software_engineering · arXiv:2504.14757
signals: \bLLM[- ]?agents?\b
touchpoints: none
Large language models (LLMs) are transforming automated program repair (APR) through agent-based approaches that localize bugs, generate patches, and verify fixes. However, the lack of high-quality, scalable training datasets, especially those with verifiable outputs and intermediate reasoning traces-limits progress, particularly for open-source models. In this work, we present SWE-Synth, a framework for synthesizing realistic, verifiable,…

### doi:10.1145/3796315.3796331
**Toward Responsible Autonomy: The Opportunities and Obstacles of Large Language Models in Software Engineering** (2026) — n/a · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3796315.3796331
signals: agentic
touchpoints: none
The rapid advancement of Large Language Models (LLMs) is reshaping the software engineering landscape, powering AI-driven tools that assist in coding, testing, documentation, and deployment. As these systems evolve toward greater autonomy, the field of AI for Software Engineering (AI4SE) faces a pivotal question: how much responsibility should be entrusted to machines within complex engineering…

### doi:10.1145/3808181
**ExpeRepair: Dual-Memory Enhanced LLM-Based Repository-Level Program Repair** (2026) — Proceedings of the ACM on software engineering. · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.1145/3808181
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Automatically repairing software issues remains a fundamental challenge at the intersection of software engineering and AI. Although recent advances in Large Language Models (LLMs) have demonstrated potential for repository-level repair tasks, current methods exhibit two notable limitations: (1) they often address issues in isolation, neglecting to incorporate insights from previously resolved issues, and (2) they…

### doi:10.48550/arxiv.2608.13292
**Refine After Generation: Toward Correct and Concise Patches in LLM-based Program Repair** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2608.13292
signals: agentic
touchpoints: none
Large language models (LLMs) have advanced automatic program repair (APR) to the point where agentic systems routinely resolve real-world, repository-level issues. Yet the generated patch has received little scrutiny beyond whether it passes tests. In this paper, we identify patch verbosity as a major yet overlooked concern in LLM-based APR. Characterizing 28 state-of-the-art approaches on…

### arxiv:2606.26978
**To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2606.26978
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based agents for program repair are increasingly built on a "generate-run-revise" paradigm, iteratively executing tests to evaluate and refine patches. This execution-based approach has become standard practice in state-of-the-art systems. However, executions can be time-consuming and expensive, yet their impact on these agents remains underexplored. In this paper, we conduct a two-stage empirical study over…

### doi:10.5281/zenodo.21804054
**Interviews with Central European Software Engineers on Vibe Coding and Agentic Software Engineering** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 6 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.21804054
signals: agentic;agentic*
touchpoints: none
This dataset contains seven anonymised in-depth interviews with Central European software professionals, including lead developers, software architects, a site manager, a frontend developer, and a CIO. The interviews were conducted between 10 and 26 July 2026. All interviews were organised around the central question: “What changes has AI brought about in your work at your…

### doi:10.48550/arxiv.2410.19461
**EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data** (2024) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2410.19461
signals: autonomous agents?
touchpoints: none
Autonomous agents operating on the graphical user interfaces (GUIs) of various applications hold immense practical value. Unlike the large language model (LLM)-based methods which rely on structured texts and customized backends, the approaches using large vision-language models (LVLMs) are more intuitive and adaptable as they can visually perceive and directly interact with screens, making them…

### arxiv:2604.19750
**Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.19750
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Recent advances in Large Language Model (LLM)-based agents have shown remarkable progress in code generation. However, current agent methods mainly rely on text-output-based feedback (e.g. command-line outputs) for multi-round debugging and struggle in graphical user interface (GUI) that involve visual information. This is mainly due to two limitations: 1) GUI programs are event-driven, yet existing…

### arxiv:2606.30119
**On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2606.30119
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Since 2023, a new class of bots has emerged: Web Agents. They can automate complex tasks on the Web, going beyond traditional browser automation tools such as Selenium, Puppeteer, or Playwright. Leveraging large language models (LLMs), these agents are capable of solving anti-bot mechanisms, mimicking human behavior, and, in some cases, operating directly from the…

### arxiv:2606.20910
**Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents** (2026) — arXiv (Cornell University) · cites 0 · score 6 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2606.20910
signals: \bAutoGen\b
touchpoints: none
As AI web agents proliferate, combining large language models with autonomous, browser-level control, indiscriminate content scraping by web agents has emerged as a privacy and security challenge. Existing defenses, such as robots.txt and active bot-blocking, are insufficient, as they are widely violated and easily circumvented. In this work, we demonstrate that AI web agents can…

### arxiv:2503.04957
**SafeArena: Evaluating the Safety of Autonomous Web Agents** (2025) — arXiv · cites 0 · score 6 (strong 1) · periphery/interface_agents · arXiv:2503.04957
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based agents are becoming increasingly proficient at solving web-based tasks. With this capability comes a greater risk of misuse for malicious purposes, such as posting misinformation in an online forum or selling illicit substances on a website. To evaluate these risks, we propose SafeArena, the first benchmark to focus on the deliberate misuse of web…

### doi:10.17605/osf.io/fk64b
**Hybrid Scientometric-Systematic Review: Cognitive Load, Agentic AI, and Human Resilience in Vocational Education** (2026) — OSF Preprints (OSF Preprints) · cites 0 · score 6 (strong 1) · periphery/science_of_science · doi:10.17605/osf.io/fk64b
signals: agentic;agentic*
touchpoints: none
This project contains the pre-registered protocol for a hybrid scientometric-systematic review examining cognitive load in Agentic AI environments, with focus on vocational education and human resilience. The review integrates bibliometric analysis (Phase 1) and PRISMA 2020 systematic review (Phase 2) to provide comprehensive evidence base for instrument development.…

### doi:10.48550/arxiv.2510.03588
**REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2510.03588
signals: agentic
touchpoints: verification_regression
Large Language Models (LLMs) have recently shown strong potential in automatic program repair (APR), especially in repository-level settings where the goal is to generate patches based on natural language issue descriptions, large codebases, and regression tests. However, despite their promise, current LLM-based APR techniques often struggle to produce correct fixes due to limited understanding of…

### arxiv:2510.18270
**Can Old Tests Do New Tricks for Resolving SWE Issues?** (2025) — arXiv · cites 0 · score 5 (strong 1) · periphery/software_engineering · arXiv:2510.18270
signals: agentic
touchpoints: verification_regression
Test suites in real-world projects are often large and achieve high code coverage, yet they remain insufficient for detecting all bugs. The abundance of unresolved issues in open-source project trackers highlights this gap. While regression tests are typically designed to ensure past functionality is preserved in the new version, they can also serve a complementary…

### arxiv:2505.11718
**REMOR: Automated Peer Review Generation with LLM Reasoning and Multi-Objective Reinforcement Learning** (2025) — arXiv · cites 0 · score 5 (strong 1) · periphery/science_of_science · arXiv:2505.11718
signals: agentic
touchpoints: optimisation_loop
AI-based peer review systems tend to produce shallow and overpraising suggestions compared to human feedback. Here, we evaluate how well a reasoning LLM trained with multi-objective reinforcement learning (REMOR) can overcome these limitations. We start by designing a multi-aspect reward function that aligns with human evaluation of reviews. The aspects are related to the review…

### doi:10.1109/icse-seip66354.2025.00043
**Automated Code Review in Practice** (2025) — arXiv (Cornell University) · cites 21 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/icse-seip66354.2025.00043
signals: \bcopilots?\b
touchpoints: none
Context: Code review is a widespread practice among practitioners to improve software quality and transfer knowledge. It is often perceived as time-consuming due to the need for manual effort and potential delays in the development process. Several AI-assisted code review tools (Qodo, GitHub Copilot, Coderabbit, etc.) provide automated code reviews using large language models (LLMs).…

### doi:10.18653/v1/2024.findings-acl.539
**CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation** (2024) — arXiv (Cornell University) · cites 10 · score 5 (strong 1) · periphery/interface_agents · doi:10.18653/v1/2024.findings-acl.539
signals: \bLLM[- ]?agents?\b
touchpoints: none
Multimodal large language models (MLLMs) have shown remarkable potential as human-like autonomous language agents to interact with real-world environments, especially for graphical user interface (GUI) automation.However, those GUI agents require comprehensive cognition including exhaustive perception and reliable action response.We propose a Comprehensive Cognitive LLM Agent, CoCo-Agent, with two novel approaches, comprehensive environment perception (CEP) and…

### doi:10.1109/ase63991.2025.00234
**Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories** (2025) — CISPA Helmholtz Center · cites 5 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/ase63991.2025.00234
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Large Language Model (LLM)-based agents are increasingly employed to automate complex software engineering tasks, such as program repair and issue resolution. These agents operate by autonomously generating natural language thoughts, invoking external tools, and iteratively refining their solutions. Despite their widespread adoption, the internal decision-making processes of these agents remain largely unexplored, limiting our understanding…

### doi:10.18653/v1/2024.findings-acl.8
**CHIME: LLM-Assisted Hierarchical Organization of Scientific Studies for Literature Review Support** (2024) — arXiv · cites 5 · score 5 (strong 1) · periphery/science_of_science · doi:10.18653/v1/2024.findings-acl.8
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Literature review requires researchers to synthesize a large amount of information and is increasingly challenging as the scientific literature expands.In this work, we investigate the potential of LLMs for producing hierarchical organizations of scientific studies to assist researchers with literature review.We define hierarchical organizations as tree structures where nodes refer to topical categories and every…

### doi:10.48550/arxiv.2402.02172
**CodeAgent: Autonomous Communicative Agents for Code Review** (2024) — arXiv (Cornell University) · cites 3 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2402.02172
signals: multi[- ]?agent (?:LLM|AI|artificial intelligence|large language)
touchpoints: none
Code review, which aims at ensuring the overall quality and reliability of software, is a cornerstone of software development. Unfortunately, while crucial, Code review is a labor-intensive process that the research community is looking to automate. Existing automated methods rely on single input-output generative models and thus generally struggle to emulate the collaborative nature of…

### doi:10.1145/3650212.3685562
**Collaboration to Repository-Level Vulnerability Detection** (2024) — n/a · cites 2 · score 5 (strong 1) · periphery/software_engineering · doi:10.1145/3650212.3685562
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection. However, due to the limitation of the length of input contexts of LLM, the existing LLM-based methods mainly focus on detecting function-level and leveraging the in-file context information for…

### doi:10.3390/healthcare14131877
**Do Multimodal Vision-Language Models Enhance the Medical Diagnostic Process? A Systematic Review** (2026) — Healthcare · cites 2 · score 5 (strong 1) · periphery/science_of_science · doi:10.3390/healthcare14131877
signals: \bcopilots?\b
touchpoints: none
Background/Objectives: Novel vision-language models (VLMs) can integrate patient textual data with image data to support medical diagnosis. Recent studies reported conflicting results regarding the performance of multimodal VLMs compared to other models and physician performance. This systematic review aims to assess the diagnostic performance of multimodal VLMs integrating both patient textual and image data across…

### doi:10.48550/arxiv.2411.00816
**CycleResearcher: Improving Automated Research via Automated Review** (2024) — arXiv (Cornell University) · cites 2 · score 5 (strong 1) · periphery/science_of_science · doi:10.48550/arxiv.2411.00816
signals: autonomous agents?
touchpoints: none
The automation of scientific discovery has been a long-standing goal within the research community, driven by the potential to accelerate knowledge creation. While significant progress has been made using commercial large language models (LLMs) as research assistants or idea generators, the possibility of automating the entire research process with open-source LLMs remains largely unexplored. This…

### doi:10.48550/arxiv.2409.16299
**HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale** (2024) — arXiv (Cornell University) · cites 1 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2409.16299
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large Language Models (LLMs) have revolutionized software engineering (SE), showcasing remarkable proficiency in various coding tasks. Despite recent advancements that have enabled the creation of autonomous software agents utilizing LLMs for end-to-end development tasks, these systems are typically designed for specific SE functions. We introduce HyperAgent, an innovative generalist multi-agent system designed to tackle a…

### doi:10.1145/3696630.3728518
**From Overload to Insight: Bridging Code Search and Code Review with LLMs** (2025) — n/a · cites 1 · score 5 (strong 1) · periphery/software_engineering · doi:10.1145/3696630.3728518
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
The software engineering (SE) research community has developed numerous tools to search and extract actionable insights from software artifacts, ranging from static analysis tools to testing frameworks and continuous integration pipelines (hereafter just "search tools"). Despite their potential, many of these search tools remain underutilized during code review, a critical process for ensuring software quality.…

### doi:10.65563/jeaai.v1i7.65
**SemanticForge: Repository-Level Code Generation through Semantic Knowledge Graphs and Constraint Satisfaction** (2025) — INNO-PRESS Journal of Emerging Applied AI · cites 1 · score 5 (strong 1) · periphery/software_engineering · doi:10.65563/jeaai.v1i7.65
signals: knowledge graphs?\s+(?:construction|generation)|construct\w*\s+(?:\w+\s+){0,3}knowledge graphs?
touchpoints: none
Large language models (LLMs) have transformed software development by enabling automated code generation, yet they frequently suffer from systematic errors that limit practical deployment. We identify two critical failure modes: \textit{logical hallucination} (incorrect control/data-flow reasoning) and \textit{schematic hallucination} (type mismatches, signature violations, and architectural inconsistencies). These errors stem from the absence of explicit, queryable representations…

### doi:10.52202/085713-4809
**Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning** (2025) — n/a · cites 1 · score 5 (strong 1) · periphery/software_engineering · doi:10.52202/085713-4809
signals: agentic
touchpoints: none
We propose CURE, a novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes, without any ground-truth code as supervision. This approach enables flexible and scalable training and allows the unit tester to learn directly from the coder's mistakes. Our derived ReasonFlux-Coder-7B and…

### doi:10.48550/arxiv.2506.10953
**Build the web for agents, not agents for the web** (2025) — arXiv (Cornell University) · cites 1 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2506.10953
signals: agentic
touchpoints: none
Recent advancements in Large Language Models (LLMs) and multimodal counterparts have spurred significant interest in developing web agents -- AI systems capable of autonomously navigating and completing tasks within web environments. While holding tremendous promise for automating complex web interactions, current approaches face substantial challenges due to the fundamental mismatch between human-designed interfaces and LLM…

### doi:10.48550/arxiv.2410.17401
**AdvAgent: Controllable Blackbox Red-teaming on Web Agents** (2024) — arXiv (Cornell University) · cites 1 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2410.17401
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Foundation model-based agents are increasingly used to automate complex tasks, enhancing efficiency and productivity. However, their access to sensitive resources and autonomous decision-making also introduce significant security risks, where successful attacks could lead to severe consequences. To systematically uncover these vulnerabilities, we propose AdvAgent, a black-box red-teaming framework for attacking web agents. Unlike existing approaches,…

### doi:10.1609/aaai.v40i45.41221
**Promoting Sustainable Web Agents: Benchmarking and Estimating Energy Consumption Through Empirical and Theoretical Analysis** (2026) — Proceedings of the AAAI Conference on Artificial Intelligence · cites 1 · score 5 (strong 1) · periphery/interface_agents · doi:10.1609/aaai.v40i45.41221
signals: agentic
touchpoints: none
Web agents, like OpenAI's Operator and Google's Project Mariner, are powerful agentic systems pushing the boundaries of Large Language Models (LLM). They can autonomously interact with the internet at the user's behest, such as navigating websites, filling search masks, and comparing price lists. Though web agent research is thriving, induced sustainability issues remain largely unexplored.…

### doi:10.48550/arxiv.2505.09875
**Characterizing Unintended Consequences in Human-GUI Agent Collaboration for Web Browsing** (2025) — arXiv (Cornell University) · cites 1 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2505.09875
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
The proliferation of Large Language Model (LLM)-based Graphical User Interface (GUI) agents in web browsing scenarios present complex unintended consequences (UCs). This paper characterizes three UCs from three perspectives: phenomena, influence and mitigation, drawing on social media analysis (N=221 posts) and semi-structured interviews (N=14). Key phenomenon for UCs include agents' deficiencies in comprehending instructions and…

### doi:10.1111/1750-3841.70537
**Peer Review—Can AI Help?** (2025) — Journal of Food Science · cites 1 · score 5 (strong 1) · periphery/science_of_science · doi:10.1111/1750-3841.70537
signals: \bcopilots?\b
touchpoints: none
One of my biggest concerns related to journal editing is the inconsistency in peer review. The fate of a manuscript often seems to depend on who is assigned as AE and who is called on to provide peer review comments. Let me qualify that. A really top-end paper will get accepted no matter what, and…

### arxiv:2512.23982
**Coding With AI: From a Reflection on Industrial Practices to Future Computer Science and Software Engineering Education** (2025) — arXiv · cites 0 · score 5 (strong 1) · periphery/software_engineering · arXiv:2512.23982
signals: agentic
touchpoints: none
Recent advances in large language models (LLMs) have introduced new paradigms in software development, including vibe coding, AI-assisted coding, and agentic coding, fundamentally reshaping how software is designed, implemented, and maintained. Prior research has primarily examined AI-based coding at the individual level or in educational settings, leaving industrial practitioners' perspectives underexplored. This paper addresses this…

### doi:10.1109/cseet66350.2025.00008
**Towards Implementing and Evaluating AI-Assisted Pull Requests in Software Engineering Education** (2025) — n/a · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/cseet66350.2025.00008
signals: \bcopilots?\b
touchpoints: none
Pull requests allow developers to suggest and review codebase changes collaboratively. This process is standard for maintaining code quality and following best practices. The recent emergence of Large Language Models like ChatGPT and GitHub Copilot has shown great potential in improving coding efficiency and accuracy in software engineering. This paper outlines a study design to…

### title:trustandcollaborationinaiassistedcodereviewforsoftwareengineeringteams
**Trust and collaboration in AI-assisted code review for software engineering teams** (2026) — LUTPub (LUT University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · https://lutpub.lut.fi/handle/10024/172104
signals: \bcopilots?\b
touchpoints: none
This thesis investigates the formation of trust and the support for cooperation in AI-assisted code review within software engineering groups. With the widespread application of tools like ChatGPT, Gemini and GitHub Copilot in software development, AI systems can assist in code generation, problem identification, testing, explanation and review. However, the suggestions from AI may be…

### doi:10.1109/icaiic68212.2026.11454249
**Examining Software Engineering Practices in the Pre-AI and Post-AI ERA** (2026) — n/a · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/icaiic68212.2026.11454249
signals: \bcopilots?\b
touchpoints: none
The rise of generative artificial intelligence (AI) coding tools such as GitHub Copilot and ChatGPT has reshaped software development, yet their impact on open-source software quality remains unclear. This study conducts a longitudinal analysis of code review and bug-fix patterns across six major Python and JavaScript repositories, pandas, scikit-learn, TensorFlow, Django, React, and Node.js, comparing…

### doi:10.1002/cae.70177
**Integrating GenAI Tools Into Software Engineering Education** (2026) — Computer Applications in Engineering Education · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.1002/cae.70177
signals: \bcopilots?\b
touchpoints: none
ABSTRACT This article addresses the challenge of integrating GenAI tools into formal higher education, specifically in software engineering, where structured approaches for their adoption into teaching and learning practices are currently lacking. The goal of this research is to explore how GenAI tools can be applied throughout various phases of the software development lifecycle and…

### doi:10.48550/arxiv.2506.14683
**Unified Software Engineering Agent as AI Software Engineer** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.14683
signals: \bLLM[- ]?agents?\b
touchpoints: none
The growth of Large Language Model (LLM) technology has raised expectations for automated coding. However, software engineering is more than coding and is concerned with activities including maintenance and evolution of a project. In this context, the concept of LLM agents has gained traction, which utilize LLMs as reasoning engines to invoke external tools autonomously.…

### doi:10.5281/zenodo.22092248
**AI-Driven Software Engineering Automated Development, Testing and Maintenance** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.22092248
signals: agentic
touchpoints: none
AI-Driven Software Engineering explores the transformation of software engineering through Machine Learning, Deep Learning, NLP, Large Language Models, Generative AI, Explainable AI, and Agentic AI. Covering the complete SDLC—from requirements engineering, architecture, code generation, testing, maintenance, and DevOps to security, governance, and autonomous software engineering—the book connects academic research with practical applications. It emphasizes human–AI…

### doi:10.48550/arxiv.2506.19290
**Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.19290
signals: \bLLM[- ]?agents?\b
touchpoints: none
Software engineering (SWE) has recently emerged as a crucial testbed for next-generation LLM agents, demanding inherent capabilities in two critical dimensions: sustained iterative problem-solving (e.g., >50 interaction rounds) and long-context dependency resolution (e.g., >32k tokens). However, the data curation process in SWE remains notoriously time-consuming, as it heavily relies on manual annotation for code file…

### title:impactofgenerativeaionsoftwareteamcollaborationandcodereviewworkflows
**Impact of generative AI on software team collaboration and code review workflows** (2026) — LUTPub (LUT University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · https://lutpub.lut.fi/handle/10024/172514
signals: \bcopilots?\b
touchpoints: none
Generative AI is now used everywhere in modern software engineering. This change directly affects how developers do their daily work. When tools like GitHub Copilot first arrived, the software industry focused mostly on one thing: how fast a single developer could type code. But this excitement missed a bigger problem inside engineering teams. Software development…

### doi:10.48550/arxiv.2511.13646
**Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2511.13646
signals: \bLLM[- ]?agents?\b
touchpoints: none
Large Language Models (LLMs) are reshaping almost all industries, including software engineering. In recent years, a number of LLM agents have been proposed to solve real-world software problems. Such software agents are typically equipped with a suite of coding tools and can autonomously decide the next actions to form complete trajectories to solve end-to-end software…

### doi:10.1109/access.2026.3691783
**Utilizing Dynamic Context and Static Analysis for Agent-Based Automated Program Repair** (2026) — IEEE Access · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/access.2026.3691783
signals: \bLLM[- ]?agents?\b
touchpoints: none
Automated Program Repair (APR) addresses the challenge of reducing software maintenance costs and improving software reliability. While recent advances in Large Language Models (LLMs) achieved measurable improvements in code generation tasks, their application to program repair faces specific challenges including limited context awareness, repetitive patch generation, and inability to learn from failed repair attempts. In…

### doi:10.63282/3117-5481/aijcst-v7i5p103
**AI Tools for Automating Code Reviews, Providing Contextual Feedback, and Improving the Efficiency of the Review Process** (2025) — American International Journal of Computer Science and Technology · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.63282/3117-5481/aijcst-v7i5p103
signals: \bcopilots?\b
touchpoints: none
Code review is an essential process in contemporary software development that guarantees code quality, safety, maintainability and teamwork. However, manual code reviews take a lot of time, are likely to fail because of mistakes, and depend on the reviewer's knowledge. As Artificial Intelligence (AI) becomes more popular, so does the trend toward automating and improving…

### doi:10.48550/arxiv.2412.11722
**GHIssuemarket: A Sandbox Environment for SWE-Agents Economic Experimentation** (2024) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2412.11722
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Software engineering agents (swe-agents), as key innovations in intelligent software engineering, are poised in the industry's end-of-programming debate to transcend from assistance to primary roles. we argue the importance of swe-agents' economic viability to their transcendence -- defined as their capacity to maintain efficient operations in constrained environments -- and propose its exploration via software…

### doi:10.1109/ms.2025.3597574
**When AI-Generated Unit Tests Validate Bugs: The Risk of Faulty Assertions** (2025) — IEEE Software · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.1109/ms.2025.3597574
signals: \bcopilots?\b
touchpoints: none
There is increasing research and commercial exploration into tools for automated unit test generation using Large Language Models (LLMs). This paper critically examines how recent LLM-based test generation tools pitched for unit testing such as Qodo Cover and GitHub Copilot handle buggy code. Considering bugs are only exposed by failing test cases, we explore the…

### doi:10.5281/zenodo.18106424
**Smart-Scan: AI-Powered Code Analysis and Review** (2025) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.18106424
signals: \bcopilots?\b
touchpoints: none
With the increasing complexity of software systems, maintaining high code quality is essential to ensure reliability, maintainability, and security. Traditionally, code reviews have been a manual and time-consuming process, often resulting in inconsistencies and missed issues due to human error. Recent advance- ments in artificial intelligence, specifically generative AI models like OpenAI's Chat- GPT and…

### doi:10.48550/arxiv.2604.25880
**From Threads to Trajectories: A Multi-LLM Pipeline for Community Knowledge Extraction from GitHub Issue Discussions** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2604.25880
signals: \bLLM[- ]?agents?\b
touchpoints: none
Resolution of complex post-production issues in large-scale open-source software (OSS) projects requires significant cognitive effort, as developers need to go through long, unstructured and fragmented issue discussion threads before that. In this paper, we present SWE-MIMIC-Bench, an issue trajectory dataset generated from raw GitHub discussions using an automated multi-LLM pipeline. Unlike simple summarization, this pipeline…

### doi:10.48550/arxiv.2604.26102
**SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2604.26102
signals: language model agents?
touchpoints: none
Large language model agents have made strong progress on software engineering, yet current systems suffer from a context coupling problem: the standard code editing interface conflates code inspection, modification planning, and edit execution within a single context window, forcing agents to interleave exploratory viewing with strictly formatted edit generation. Irrelevant context accumulates and edit reliability…

### arxiv:2607.24601
**Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review** (2026) — arXiv · cites 0 · score 5 (strong 1) · periphery/software_engineering · arXiv:2607.24601
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Background: Large language models (LLMs) are increasingly used to automate code review, but the reasoning behind their decisions remains hard to understand. Developers struggle to assess the validity of LLM-generated reviews, making it difficult to gauge how much trust to place in them. The role of Explainable AI (XAI) in code review and its impact…

### doi:10.48550/arxiv.2604.05955
**Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2604.05955
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Repository-level issue resolution benchmarks have become a standard testbed for evaluating LLM-based agents, yet success is still predominantly measured by test pass rates. In practice, however, acceptable patches must also comply with project-specific design constraints, such as architectural conventions, error-handling policies, and maintainability requirements, which are rarely encoded in tests and are often documented only…

### arxiv:2603.24359
**Gendered Prompting and LLM Code Review: How Gender Cues in the Prompt Shape Code Quality and Evaluation** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2603.24359
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLMs are increasingly embedded in programming workflows, from code generation to automated code review. Yet, how gendered communication styles interact with LLM-assisted programming and code review remains underexplored. We present a mixed-methods pilot study examining whether gender-related linguistic differences in prompts influence code generation outcomes and code review decisions. Across three complementary studies, we analyze…

### doi:10.48550/arxiv.2506.16650
**SemAgent: A Semantics Aware Program Repair Agent** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.16650
signals: agentic
touchpoints: none
Large Language Models (LLMs) have shown impressive capabilities in downstream software engineering tasks such as Automated Program Repair (APR). In particular, there has been a lot of research on repository-level issue-resolution benchmarks such as SWE-Bench. Although there has been significant progress on this topic, we notice that in the process of solving such issues, existing…

### doi:10.48550/arxiv.2604.26469
**An Empirical Study of Speculative Decoding on Software Engineering Tasks** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2604.26469
signals: agentic
touchpoints: none
Large Language Models (LLMs) have become widely used for Software Engineering (SE) tasks, spanning from function-level code generation to complex repository-level workflows. However, the high latency of autoregressive inference remains a significant bottleneck, hindering their deployment in interactive environments. While Speculative Decoding (SD) offers a promising technique for lossless acceleration, prior research on long-context repository-level…

### doi:10.48550/arxiv.2505.13652
**Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2505.13652
signals: agentic
touchpoints: none
Large language models (LLMs) have recently achieved remarkable results in complex multi-step tasks, such as mathematical reasoning and agentic software engineering. However, they often struggle to maintain consistent performance across multiple solution attempts. One effective approach to narrow the gap between average-case and best-case performance is guided test-time search, which explores multiple solution paths to…

### doi:10.48550/arxiv.2510.11838
**Lingxi: Repository-Level Issue Resolution Framework Enhanced by Procedural Knowledge Guided Scaling** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2510.11838
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Driven by the advancements of Large Language Models (LLMs), LLM-powered agents are making significant improvements in software engineering tasks, yet struggle with complex, repository-level issue resolution. Existing agent-based methods have two key limitations. First, they lack of procedural knowledge (i.e., how an issue is fixed step-by-step and rationales behind it) to learn and leverage for…

### doi:10.48550/arxiv.2511.16004
**InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Software Issue Resolution** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2511.16004
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Large language models have advanced software engineering automation, yet resolving real-world software issues remains difficult because it requires repository-level reasoning, accurate diagnostics, and strong verification signals. Existing agent-based and pipeline-based methods often rely on insufficient tests, which can lead to patches that satisfy verification but fail to fix the underlying defect. We present InfCode, an…

### doi:10.48550/arxiv.2506.11425
**Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2506.11425
signals: agentic
touchpoints: none
Reinforcement Learning from Verifiable Rewards (RLVR) has been widely adopted as the de facto method for enhancing the reasoning capabilities of large language models and has demonstrated notable success in verifiable domains like math and competitive programming tasks. However, the efficacy of RLVR diminishes significantly when applied to agentic environments. These settings, characterized by multi-step,…

### arxiv:2603.11078
**CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2603.11078
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Recent advances in frontier large language models have enabled code review agents that operate in open-ended, reasoning-intensive settings. However, the lack of standardized benchmarks and granular evaluation protocols makes it difficult to assess behavior of code review agents beyond coarse success metrics, particularly for tasks where false positives are costly. To address this gap, we…

### arxiv:2604.04580
**Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints** (2026) — arXiv · cites 0 · score 5 (strong 1) · periphery/software_engineering · arXiv:2604.04580
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Software engineers resolving repository-level issues do not treat existing tests as immutable correctness oracles. Instead, they iteratively refine both code and the tests used to characterize intended behavior, as new modifications expose missing assumptions or misinterpreted failure conditions. In contrast, most existing large language model (LLM)-based repair systems adopt a linear pipeline in which tests…

### doi:10.48550/arxiv.2601.22149
**DynaWeb: Model-Based Reinforcement Learning of Web Agents** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2601.22149
signals: agentic
touchpoints: none
The development of autonomous web agents, powered by Large Language Models (LLMs) and reinforcement learning (RL), represents a significant step towards general-purpose AI assistants. However, training these agents is severely hampered by the challenges of interacting with the live internet, which is inefficient, costly, and fraught with risks. Model-based reinforcement learning (MBRL) offers a promising…

### doi:10.1109/aixdke67294.2026.00021
**AI Web Agents in Practice: A Survey of Current Capabilities, Limitations, and Future Prospects** (2026) — n/a · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.1109/aixdke67294.2026.00021
signals: \bAI agents?\b
touchpoints: none
As many in the artificial intelligence and humancomputer interaction research communities recognize, the promise of autonomous web agents remains largely unfulfilled despite significant theoretical advances. Millions of users continue to manually navigate complex web interfaces daily, performing repetitive tasks that modern AI systems should theoretically handle with ease. However, recent developments in large language models…

### doi:10.6084/m9.figshare.31851544.v1
**Malva** (2026) — Figshare · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.6084/m9.figshare.31851544.v1
signals: agentic
touchpoints: none
Malva is a defect library for agentic GUI software, a class of systems in which large language model (LLM) agents autonomously operate graphical user interfaces to complete user-specified tasks without relying on programmatic APIs.This dataset supports an empirical study of defects in agentic GUI applications. It contains a benchmark of 40 open-source agentic GUI projects…

### doi:10.48550/arxiv.2604.24441
**AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark** (2026) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.24441
signals: autonomous agents?
touchpoints: none
Autonomous agents capable of navigating Graphical User Interfaces (GUIs) hold the potential to revolutionize digital productivity. However, achieving true digital autonomy extends beyond reactive element matching; it necessitates a predictive mental model of interface dynamics and the ability to foresee the "digital world state" resulting from interactions. Despite the perceptual capabilities of modern Vision-Language Models…

### arxiv:2501.01149
**A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation** (2025) — arXiv · cites 0 · score 5 (strong 1) · periphery/interface_agents · arXiv:2501.01149
signals: \bAI agents?\b
touchpoints: none
The advancement of Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) has catalyzed the development of mobile graphic user interface (GUI) AI agents, which is designed to autonomously perform tasks on mobile devices. However, a significant gap persists in mobile GUI agent evaluation, where existing benchmarks predominantly rely on either static frame assessments…

### doi:10.48550/arxiv.2510.17790
**UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action** (2025) — arXiv (Cornell University) · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2510.17790
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
Computer-use agents face a fundamental limitation. They rely exclusively on primitive GUI actions (click, type, scroll), creating brittle execution chains prone to cascading failures. While API-driven agents harness rich capabilities through structured interfaces and tools, computer-use agents remain constrained to low-level visual interactions. We present UltraCUA, a foundation model that transcends this limitation through hybrid…

### doi:10.48448/js4t-2a97
**42 - Promoting Sustainable Web Agents: Benchmarking and Estimating Energy Consumption Through Empirical and Theoretical Analysis** (2026) — Underline Science Inc. · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.48448/js4t-2a97
signals: agentic
touchpoints: none
Web agents, like OpenAI's Operator and Google's Project Mariner, are powerful agentic systems pushing the boundaries of Large Language Models (LLM). They can autonomously interact with the internet at the user's behest, such as navigating websites, filling search masks, and comparing price lists. Though web agent research is thriving, induced sustainability issues remain largely unexplored.…

### doi:10.18653/v1/2026.findings-acl.1465
**Web Sitemap Knowledge Can Enhance Autonomous Browsing** (2026) — n/a · cites 0 · score 5 (strong 1) · periphery/interface_agents · doi:10.18653/v1/2026.findings-acl.1465
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Recent advances in large language models (LLMs) have enabled web agents to perform interactive tasks on real-world websites.However, existing agents still suffer from limited robustness, efficiency, and task success, largely due to their lack of structural understanding of websites and the absence of browsing priors in pre-trained models.To address these challenges, this paper proposes the…

### arxiv:2505.18121
**ProgRM: Build Better GUI Agents with Progress Rewards** (2025) — arXiv · cites 0 · score 5 (strong 1) · periphery/interface_agents · arXiv:2505.18121
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based (Large Language Model) GUI (Graphical User Interface) agents can potentially reshape our daily lives significantly. However, current LLM-based GUI agents suffer from the scarcity of high-quality training data owing to the difficulties of trajectory collection and reward annotation. Existing works have been exploring LLMs to collect trajectories for imitation learning or to offer reward…

### arxiv:2607.07946
**DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2607.07946
signals: agentic
touchpoints: hpc_scale_out;verification_regression
DeepSWE is a benchmark of 113 original, long-horizon software engineering tasks for evaluating coding agents. Most public agentic coding benchmarks follow SWE-bench in mining merged fixes from public GitHub repositories, which creates two problems: the fixes and their discussion were likely seen during pretraining, so a high score can reflect recall rather than problem-solving; and…

### doi:10.1145/3696630.3728549
**Alibaba LingmaAgent: Improving Automated Issue Resolution via Comprehensive Repository Exploration** (2025) — arXiv (Cornell University) · cites 10 · score 4 (strong 1) · periphery/software_engineering · doi:10.1145/3696630.3728549
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: uncertainty_quantification
This paper presents Alibaba LingmaAgent, a novel Automated Software Engineering method designed to comprehensively understand and utilize whole software repositories for issue resolution. Deployed in TONGYI Lingma, an IDE-based coding assistant developed by Alibaba Cloud, LingmaAgent addresses the limitations of existing LLM-based agents that primarily focus on local code information. Our approach introduces a top-down…

### doi:10.1145/3807901
**Towards AI-Native Software Engineering (SE 3.0): A Vision and a Challenge Roadmap** (2026) — ACM Transactions on Software Engineering and Methodology · cites 4 · score 4 (strong 1) · periphery/software_engineering · doi:10.1145/3807901
signals: \bcopilots?\b
touchpoints: optimisation_loop
The rise of AI-assisted software engineering (SE 2.0), powered by Foundation Models (FMs) and FM-powered coding assistants, has shown promise in improving developer productivity. However, it has also exposed inherent limitations, such as cognitive overload on developers and inefficiencies. We propose a shift towards Software Engineering 3.0 (SE 3.0), an AI-native approach characterized by intent-centric,…

### title:designandevaluationofanaidriventasktocodefeedbackloopincicdpipelines
**Design and Evaluation of an AI-Driven Task-to-Code Feedback Loop in CI/CD Pipelines** (2026) — KTH Publication Database DiVA (KTH Royal Institute of Technology) · cites 0 · score 4 (strong 1) · periphery/software_engineering · http://urn.kb.se/resolve?urn=urn:nbn:se:bth-29715
signals: model context protocol
touchpoints: tool_exposure
Background. CI/CD pipelines shorten feedback cycles and enable early defect detection, but the path from a task description to a validated pull request still relies on manual coordination despite growing AI adoption in software development. Objectives. We design and evaluate ACID Bot (AI in CI/CD), a bounded three-agent pipeline (Enhancer, Solver, Publisher) built on the…

### doi:10.5281/zenodo.19358477
**Ep. 232: The Command Line Resurgence: Why the Terminal is Back** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.5281/zenodo.19358477
signals: \bAI agents?\b
touchpoints: surrogate_modelling
Episode summary: In this episode, Herman and Corn dive into the fascinating world of Command Line Interfaces (CLIs) and why they are seeing a massive resurgence in 2026. They trace the history of the terminal from 1950s punch cards to modern GPU-accelerated emulators, exploring how the "Unix Philosophy" of simple, composable tools is more relevant…

### arxiv:2601.20380
**OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2601.20380
signals: agentic
touchpoints: verification_regression
Graphical User Interface (GUI) agents show great potential for enabling foundation models to complete real-world tasks, revolutionizing human-computer interaction and improving human productivity. In this report, we present OmegaUse, a general-purpose GUI agent model for autonomous task execution on both mobile and desktop platforms, supporting computer-use and phone-use scenarios. Building an effective GUI agent model…

### doi:10.31219/osf.io/xbdrq_v1
**Enhancing Scientific Writing with AI: Tools, Techniques, and Ethical Practices** (2025) — n/a · cites 0 · score 4 (strong 1) · periphery/science_of_science · doi:10.31219/osf.io/xbdrq_v1
signals: \bcopilots?\b
touchpoints: verification_regression
Artificial Intelligence (AI) is rapidly reshaping the landscape of scientific writing, offering a suite of tools that assist researchers at every stage of document preparation—from brainstorming and outlining to drafting, editing, citation management, data analysis, and final formatting. This article provides a comprehensive exploration of AI applications in scientific writing, extending beyond the thesis-writing context…

### arxiv:2604.22294
**SLIDERS: Systematic Reviews via Automated Evidence Synthesis and Reconciliation** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/science_of_science · arXiv:2604.22294
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: provenance_reproducibility
Systematic reviews -- which requires comprehensive evidence collection and synthesis from large document corpora in response to targeted research questions -- are foundational in finance, social sciences, and other technical fields. Manual construction of evidence tables is labor-intensive, and recent LLM-based assistants relying on embedding or keyword based search often fail to meet the coverage…

### doi:10.1590/1806-9282.20230560
**The use of artificial intelligence to improve the scientific writing of non-native english speakers** (2023) — Revista da Associação Médica Brasileira · cites 151 · score 4 (strong 1) · periphery/science_of_science · doi:10.1590/1806-9282.20230560
signals: \bcopilots?\b
touchpoints: none
OBJECTIVE: Scientific writing in English is a daunting task for non-native English speakers. The challenges of writing in a foreign language are evident in the scientific literature where texts by non-native English-speaking scientists tend to be less clear and succinct, contain grammatical errors, and are often rejected by prestigious journals. METHODS: We conducted a non-systematic…

### doi:10.1002/spe.70005
**Generative Artificial Intelligence for Software Engineering—A Research Agenda** (2025) — Software Practice and Experience · cites 50 · score 4 (strong 1) · periphery/software_engineering · doi:10.1002/spe.70005
signals: \bcopilots?\b
touchpoints: none
ABSTRACT Context Generative artificial intelligence (GenAI) tools have become increasingly prevalent in software development, offering assistance to various managerial and technical project activities. Notable examples of these tools include OpenAI's ChatGPT, GitHub Copilot, and Amazon CodeWhisperer. Objective Although many recent publications have explored and evaluated the application of GenAI, a comprehensive understanding of the current…

### doi:10.1002/nur.22326
**Harnessing AI for enhancing scientific writing in nursing research: Prospects, pitfalls, and solutions** (2023) — Research in Nursing & Health · cites 20 · score 4 (strong 1) · periphery/science_of_science · doi:10.1002/nur.22326
signals: \bcopilots?\b
touchpoints: none
Artificial intelligence (AI) has been revolutionizing various domains of human endeavor, and the scientific writing landscape in nursing research is no exception (Davenport & Kalakota, 2019). Indeed, the increasing pervasiveness of AI tools for research writing offers significant advantages, but it also presents certain challenges. Nonetheless, with mindful use, these technologies can become pivotal for…

### doi:10.1186/s13643-025-02997-8
**Accelerating the pace and accuracy of systematic reviews using AI: a validation study** (2025) — Systematic Reviews · cites 10 · score 4 (strong 1) · periphery/science_of_science · doi:10.1186/s13643-025-02997-8
signals: \bcopilots?\b
touchpoints: none
BACKGROUND: Artificial intelligence (AI) can greatly enhance efficiency in systematic literature reviews and meta-analyses, but its accuracy in screening titles/abstracts and full-text articles is uncertain. OBJECTIVES: This study evaluated the performance metrics (sensitivity, specificity) of a GPT-4 AI program, Review Copilot, against human decisions (gold standard) in screening titles/abstracts and full-text articles from four published…

### doi:10.1109/tse.2025.3614469
**Seeing is Believing: Vision-Driven Non-Crash Functional Bug Detection for Mobile Apps** (2025) — IEEE Transactions on Software Engineering · cites 8 · score 4 (strong 1) · periphery/interface_agents · doi:10.1109/tse.2025.3614469
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Mobile app GUI (Graphical User Interface) pages now contain rich visual information, with the visual semantics of each page helping users understand the application logic. However, these complex visual and functional logics present new challenges to software testing. Existing automated GUI testing methods, constrained by the lack of reliable testing oracles, are limited to detecting…

### doi:10.1111/jdv.20237
**Appraisal of AI ‐generated dermatology literature reviews** (2024) — Journal of the European Academy of Dermatology and Venereology · cites 7 · score 4 (strong 1) · periphery/science_of_science · doi:10.1111/jdv.20237
signals: \bcopilots?\b
touchpoints: none
BACKGROUND: Artificial intelligence (AI) tools have the potential to revolutionize many facets of medicine and medical sciences research. Numerous AI tools have been developed and are in continuous states of iterative improvement in their functionality. OBJECTIVES: This study aimed to assess the performance of three AI tools: The Literature, Microsoft's Copilot and Google's Gemini in…

### doi:10.1609/aaai.v40i35.40187
**Agent-SAMA: State-Aware Mobile Assistant** (2026) — Proceedings of the AAAI Conference on Artificial Intelligence · cites 3 · score 4 (strong 1) · periphery/interface_agents · doi:10.1609/aaai.v40i35.40187
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Mobile Graphical User Interface (GUI) agents aim to autonomously complete tasks within or across apps based on user instructions. While recent Multimodal Large Language Models (MLLMs) enable these agents to interpret UI screens and perform actions, existing agents remain fundamentally reactive. They reason over the current UI screen but lack a structured representation of the…

### doi:10.48550/arxiv.2604.13940
**AI-Assisted Peer Review at Scale: The AAAI-26 AI Review Pilot** (2026) — arXiv (Cornell University) · cites 1 · score 4 (strong 1) · periphery/science_of_science · doi:10.48550/arxiv.2604.13940
signals: \btool[- ]use\b
touchpoints: none
Scientific peer review faces mounting strain as submission volumes surge, making it increasingly difficult to sustain review quality, consistency, and timeliness. Recent advances in AI have led the community to consider its use in peer review, yet a key unresolved question is whether AI can generate technically sound reviews at real-world conference scale. Here we…

### doi:10.2196/preprints.84862
**Artificial Intelligence for Depression Detection in Adults: A Systematic Review of Diagnostic Performance, Features, and Limitations (Preprint)** (2025) — n/a · cites 1 · score 4 (strong 1) · periphery/science_of_science · doi:10.2196/preprints.84862
signals: \btool[- ]using\b
touchpoints: none
BACKGROUND Mental health conditions, particularly major depressive disorder (MDD), are a significant and growing global concern. The World Health Organization (WHO) estimates that more than 264 million people worldwide suffer from depression, which is a leading cause of disability and premature mortality. In the United States alone, approximately 18.8 million adults experienced a major depressive…

### doi:10.5281/zenodo.21288634
**The AI Productivity Paradox in Software Engineering: A Systematic Review of Code Quality, Technical Debt, and Organizational Throughout (2024–2026)** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.21288634
signals: \bcopilots?\b
touchpoints: none
Background: The period 2024–2026 has seen accelerated adoption of AI coding assistants (e.g., GitHub Copilot, Cursor, CodeWhisperer, Amazon CodeWhisperer). Early productivity gains are well reported in industry white papers and short-term controlled experiments. However, emerging evidence suggests a paradox: perceived throughput increases may coincide with hidden declines in code quality and accelerated technical debt accumulation…

### doi:10.48550/arxiv.2603.23448
**Code Review Agent Benchmark** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2603.23448
signals: \bAI agents?\b
touchpoints: none
Software engineering agents have shown significant promise in writing code. As AI agents permeate code writing, and generate huge volumes of code automatically -- the matter of code quality comes front and centre. As the automatically generated code gets integrated into huge code-bases -- the issue of code review and broadly quality assurance becomes important.…

### doi:10.3390/computers15040235
**Adaptive Architectures for Gamified Learning in Software Engineering: A Systematic Review** (2026) — Computers · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.3390/computers15040235
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Effective software engineering education today requires tools that adapt to individual learner proficiency and progress, while ensuring positive student engagement. Gamified platforms represent an effective approach to learning and maintaining motivation, but their efficacy depends on a robust underlying architecture. This systematic literature review analyzes state-of-the-art artificial intelligence (AI)-based adaptive architectures designed to support gamified…

### doi:10.1145/3797092
**From Specifications to Implementation in the Gen-AI Era: Lessons from a Project-Based Software Engineering Course** (2026) — Proceedings of the ACM on software engineering. · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.1145/3797092
signals: \bcopilots?\b
touchpoints: none
By early 2025, AI code assistants had evolved into sophisticated collaborators capable of generating, explaining, reviewing, and modifying substantial portions of a software system. In February 2025, as we were delivering an upper-level undergraduate course on Software Engineering in our university, the term vibe coding emerged and quickly became popularized, referring to a practice in…

### doi:10.48550/arxiv.2603.15401
**SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2603.15401
signals: \bLLM[- ]?agents?\b
touchpoints: none
Agent skills, structured procedural knowledge packages injected at inference time, are increasingly used to augment LLM agents on software engineering tasks. However, their real utility in end-to-end development settings remains unclear. We present SWE-Skills-Bench, the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE). It pairs 49 public…

### title:theimpactofaidrivencodereviewondeveloperproductivityandsoftwarequality
**The Impact of AI-Driven Code Review on Developer Productivity and Software Quality** (2025) — KTH Publication Database DiVA (KTH Royal Institute of Technology) · cites 0 · score 4 (strong 1) · periphery/software_engineering · http://urn.kb.se/resolve?urn=urn:nbn:se:bth-29144
signals: \bcopilots?\b
touchpoints: none
Background: Code review is essential for ensuring software quality, but traditional review processes are time-consuming and may miss issues without human expertise. AI-driven tools such as Windsurf, Github Copilot, Claude Code, and Cursor have emerged to automate routine checks and improve productivity, yet empirical comparisons between different AI-driven tools remain limited. Objectives: This study evaluates…

### doi:10.36948/ijfmr.2026.v08i04.85314
**Assessing the Impact of Ai Vibe Coding on Reviewing and Debugging Ai-generated Code** (2026) — International Journal For Multidisciplinary Research · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.36948/ijfmr.2026.v08i04.85314
signals: \bcopilots?\b
touchpoints: none
The software engineering landscape is undergoing a radical transition from manual syntax craftsmanship to "Vibe Coding"a paradigm defined by prompt-driven, intent-based software generation. This research quantifies the impact of this shift on the software development lifecycle (SDLC), specifically evaluating the efficacy of code review and debugging. Utilizing a diagnostic pipeline with a 50-developer cohort, this…

### arxiv:2607.28587
**PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2607.28587
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
SWE-bench-like benchmarks are widely used for evaluating LLM's issue resolution capability. They typically follow a common construction pipeline: each PR (Pull Request) is paired with its linked issue by extracting issue references from the PR description; the issue description is used as the problem statement, and the PR patch serves as the test oracle. However,…

### doi:10.48550/arxiv.2509.02544
**UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning** (2025) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2509.02544
signals: autonomous agents?
touchpoints: none
The development of autonomous agents for graphical user interfaces (GUIs) presents major challenges in artificial intelligence. While recent advances in native agent models have shown promise by unifying perception, reasoning, action, and memory through end-to-end learning, open problems remain in data scalability, multi-turn reinforcement learning (RL), the limitations of GUI-only operation, and environment stability. In…

### arxiv:2602.02262
**OmniCode: A Benchmark for Evaluating Software Engineering Agents** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2602.02262
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-powered coding agents are redefining how real-world software is developed. To drive the research towards better coding agents, we require challenging benchmarks that can rigorously evaluate the ability of such agents to perform various software engineering tasks. However, popular coding benchmarks such as HumanEval and SWE-Bench focus on narrowly scoped tasks such as competition programming…

### doi:10.5281/zenodo.18351797
**Intelligent Language Systems in Autonomous Software Engineering Pipelines** (2026) — Journal of Information Systems Engineering & Management · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.18351797
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
This work introduces the IASP (Intelligent Autonomous Software Pipelines) framework, a novel conceptual architecture that unifies the fragmented landscape of AI-driven software engineering into a coherent, system-level model. The IASP framework organizes autonomous software engineering capabilities across four interdependent layers: Intelligent Code Reasoning (I), Adaptive Validation and Reliability (A), Self-Directed Autonomous Workflows (S), and Production…

### doi:10.48550/arxiv.2511.00872
**A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric Software Engineering Tasks** (2025) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2511.00872
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Unlike traditional automation tools or static LLM-based systems, agents combine decision-making and tool utilization to accomplish complex tasks, showing great potential in software engineering. However, existing studies largely focus on specific tasks or isolated aspects, providing an incomplete picture of agents' practical capabilities. To address this, we conduct a comprehensive empirical study evaluating seven general-purpose…

### doi:10.48550/arxiv.2602.10487
**Following Dragons: Code Review-Guided Fuzzing** (2026) — Minerva Access (University of Melbourne) · cites 0 · score 4 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2602.10487
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
Modern fuzzers scale to large, real-world software but often fail to exercise the program states developers consider most fragile or security-critical. Such states are typically deep in the execution space, gated by preconditions, or overshadowed by lower-value paths that consume limited fuzzing budgets. Meanwhile, developers routinely surface risk-relevant insights during code review, yet this information…

### arxiv:2605.22526
**"Refactoring Runaway": Understanding and Mitigating Tangled Refactorings in Coding Agents for Issue Resolution** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2605.22526
signals: agentic
touchpoints: none
Recent advances in coding agents have shown remarkable progress in software issue resolution. In practice, real-world issues are typically bug fixes or feature requests in which human developers naturally incorporate refactoring as part of the resolution process, resulting in tangled refactoring. Since LLMs are trained on large-scale open-source repositories, coding agents may inherit such behaviors.…

### arxiv:2607.11111
**Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2607.11111
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based coding agents have significantly advanced automated software issue resolution, yet they remain highly prone to factual errors caused by insufficient repository understanding. Recent methods attempt to mitigate this limitation through pre-repair repository exploration; however, their fix-driven strategies explore repositories without identifying the agent's knowledge gaps, often yielding imprecise context that fails to bridge the…

### arxiv:2607.07980
**3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2607.07980
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Coding agents now author entire pull requests, and practitioners sharply disagree about what this does to code review: whether it becomes the bottleneck, whether human review is still necessary, and whether it quietly erodes the understanding that it once built. Repository-mining studies measure surface trends but seldom explain the mechanisms beneath them, and the trends…

### arxiv:2606.16038
**Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2606.16038
signals: agentic
touchpoints: none
The path toward autonomous software engineering is currently bottlenecked by a severe deficit of diverse, large-scale trajectory data. We address this by introducing \ourdataset, an expansive dataset of 207,489 agentic trajectories spanning nine programming languages (Python, Go, TS, JS, Rust, Java, PHP, C, C++). Sourced from 20,000 real-world PRs via OpenHands and SWE-agent harnesses, the…

### arxiv:2606.07412
**Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2606.07412
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-driven software engineering agents have become a central testbed for real-world language-model capability, yet their training remains limited by the availability of high-quality SWE tasks. Existing synthetic data methods typically create tasks through fixed mutation or bug-injection procedures, making the resulting distributions largely independent of the agent's own weaknesses and training progress. We introduce Socratic-SWE,…

### arxiv:2605.27605
**Laguna M.1/XS.2 Technical Report** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2605.27605
signals: agentic
touchpoints: none
We present Laguna M.1 and Laguna XS.2, two Mixture-of-Experts foundation models built for long-horizon, agentic coding: M.1 has $225.8$B total parameters ($23.4$B activated per token) and XS.2 has $33.4$B total ($3$B activated). Both models were trained from scratch end-to-end inside the same internal system that we refer to as our Model Factory: a tightly-integrated stack…

### arxiv:2603.17826
**FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/software_engineering · arXiv:2603.17826
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Multimodal Automated Program Repair (MAPR) extends traditional program repair by requiring models to jointly reason over source code, textual issue descriptions, and visual artifacts such as GUI screenshots. While recent LLM-based repair systems have shown promising results, existing approaches face several limitations: rigid workflow pipelines restrict exploration during debugging, visual reasoning is often performed over…

### doi:10.48550/arxiv.2606.20120
**Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/lab_automation · doi:10.48550/arxiv.2606.20120
signals: self[- ]driving lab
touchpoints: none
Biological experiment protocols are written in natural language, whereas automation systems rely on predefined control commands, creating a semantic gap that limits autonomous execution. Microplate-based automatic experiments are particularly challenging due to the need to simultaneously control well mapping, sample-reagent combinations, replicate placement, and parallel dispensing. This study proposes an agent-based protocol translation framework that…

### arxiv:2606.03854
**CLI-Anything: Towards Agent-Native Computer Use** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2606.03854
signals: \btool[- ]use\b
touchpoints: none
As large language models advance in reasoning and tool use capabilities, researchers increasingly seek to leverage them for computer use agents that can interact with existing software. The dominant approach develops GUI agents that control applications through visual interfaces: interpreting screenshots, locating UI elements, and executing mouse clicks to mimic human interaction. This GUI-centric paradigm…

### doi:10.48550/arxiv.2412.09605
**AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials** (2024) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2412.09605
signals: function[- ]calling
touchpoints: none
Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity of high-quality trajectory data for training. Existing approaches rely on expensive human annotation, making them unsustainable at scale. We propose AgentTrek, a scalable data synthesis pipeline that generates web agent trajectories by leveraging publicly available…

### doi:10.48550/arxiv.2511.13087
**MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements** (2025) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2511.13087
signals: autonomous agents?
touchpoints: none
Graphical User Interface (GUI) grounding - the task of mapping natural language instructions to screen coordinates - is essential for autonomous agents and accessibility technologies. Existing systems rely on monolithic models or one-shot pipelines that lack modularity and fail under visual clutter and ambiguous instructions. We introduce MEGA-GUI, a multi-stage framework that separates grounding into…

### doi:10.1109/iccv51701.2025.00158
**UIPro: Unleashing Superior Interaction Capability for GUI Agents** (2025) — arXiv · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.1109/iccv51701.2025.00158
signals: autonomous agents?
touchpoints: none
Building autonomous agents that perceive and operate graphical user interfaces (GUIs) like humans has long been a vision in the field of artificial intelligence. Central to these agents is the capability for GUI interaction, which involves GUI understanding and planning capabilities. Existing methods have tried developing GUI agents based on the multi-modal comprehension ability of…

### arxiv:2604.13488
**Towards Scalable Lightweight GUI Agents via Multi-role Orchestration** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.13488
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) enable digital automation on end-user devices. While scaling both parameters and data has yielded substantial gains, advanced methods still suffer from prohibitive deployment costs on resource-constrained devices. When facing complex in-the-wild scenarios, lightweight GUI agents are bottlenecked by limited capacity and poor…

### doi:10.32657/10356/218901
**Building generalizable mobile sensing and GUI operation agents** (2026) — n/a · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.32657/10356/218901
signals: autonomous agents?
touchpoints: none
Autonomous agents operating in mobile systems need to continuously sense complex environments and perform interactions to accomplish user tasks under diverse users, devices, applications, and system constraints. This thesis investigates the key challenges and methodological innovations in this domain, with a particular focus on building generalizable mobile sensing and Graphical User Interface (GUI) operation agents…

### arxiv:2506.11127
**UITron-Speech: Towards Automated GUI Agents Based on Speech Instructions** (2025) — arXiv · cites 0 · score 4 (strong 1) · periphery/interface_agents · arXiv:2506.11127
signals: autonomous agents?
touchpoints: none
Autonomous agents for Graphical User Interfaces (GUIs) are revolutionizing human-computer interaction, yet their reliance on text-based instructions imposes limitations on accessibility and convenience, particularly in hands-free scenarios. To address this issue, we propose replacing text with speech as the instruction input modality for GUI agents, and introduce UITron-Speech, which is the first end-to-end GUI agent…

### doi:10.48550/arxiv.2608.24749
**From Natural Language Requirements to Graphical User Interfaces: Automated Prototyping and Verification with Pretrained Language Models** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2608.24749
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Requirements elicitation is essential for developing interactive software systems, as it helps ensure that the resulting product meets stakeholder needs. Since elicitation typically relies on natural language (NL), misunderstandings can arise from its inherent ambiguity. Formal specifications can reduce ambiguity but require technical expertise. GUI prototyping therefore provides a valuable alternative by turning requirements into…

### doi:10.48550/arxiv.2602.15384
**World-Model-Augmented Web Agents with Action Correction** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2602.15384
signals: multi[- ]?agent[,\s]+(?:\w+[-\s]+){0,2}(?:system|framework|architecture|collaborat|approach|workflow|platform|pipeline)
touchpoints: none
Web agents based on large language models have demonstrated promising capability in automating web tasks. However, current web agents struggle to reason out sensible actions due to the limitations of predicting environment changes, and might not possess comprehensive awareness of execution risks, prematurely performing risky actions that cause losses and lead to task failure. To…

### doi:10.1145/3805712.3808592
**WebMall - A Multi-Shop Benchmark for Evaluating Web Agents** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.1145/3805712.3808592
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based web agents have the potential to automate long-running web tasks, such as searching for products in multiple e-shops and subsequently ordering the cheapest products that meet the user's needs. Benchmarks for evaluating web agents either require agents to perform tasks online using the live Web or offline using simulated environments, the latter allowing for…

### doi:10.48550/arxiv.2604.06367
**WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.06367
signals: agentic
touchpoints: none
Web agents automate browser tasks, ranging from simple form completion to complex workflows like ordering groceries. While current benchmarks evaluate general-purpose performance~(e.g., WebArena) or safety against malicious actions~(e.g., SafeArena), no existing framework assesses an agent's ability to successfully execute user-facing website security and privacy tasks, such as managing cookie preferences, configuring privacy-sensitive account settings, or…

### doi:10.48550/arxiv.2604.16385
**StressWeb: A Diagnostic Benchmark for Web Agent Robustness under Realistic Interaction Variability** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.16385
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Large language model-based web agents have demonstrated strong performance on realistic web interaction tasks. However, existing evaluations are predominantly conducted under relatively stable and well-behaved interaction conditions, which may overestimate agent robustness. High task success in such idealized settings does not necessarily reflect performance under realistic web interaction. To address this limitation, we introduce a…

### doi:10.52202/085713-0817
**Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis** (2025) — arXiv · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.52202/085713-0817
signals: agentic
touchpoints: none
Graphical user interface (GUI) grounding, the ability to map natural language instructions to specific actions on graphical user interfaces, remains a critical bottleneck in computer use agent development. Current benchmarks oversimplify grounding tasks as short referring expressions, failing to capture the complexity of real-world interactions that require software commonsense, layout understanding, and fine-grained manipulation capabilities.…

### doi:10.48550/arxiv.2606.13385
**Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2606.13385
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
LLM-based web agents are increasingly deployed in real-world settings such as e-commerce, where they interact extensively with untrusted web content while executing actions that carry direct financial consequences. This makes them vulnerable to prompt-injection attacks, in which seemingly benign web content conceals adversarial instructions that manipulate the agent's behavior. Existing security benchmarks adopt an \textit{attack-centric}…

### doi:10.5281/zenodo.21292653
**Artifact for the PETS 2026 paper: "WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.5281/zenodo.21292653
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Artifact for the PETS 2026 paper "WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks" (Guruprasad Viswanathan Ramesh, Asmit Nayak, Basieem Siddique, and Kassem Fawaz; University of Wisconsin–Madison). WebSP-Eval measures how well LLM-powered web agents perform website security and privacy tasks (managing cookies, configuring privacy settings, revoking sessions, controlling newsletter/marketing preferences, etc.) on live…

### doi:10.5281/zenodo.21292654
**Artifact of PETS 2026 paper: "WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks"** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.5281/zenodo.21292654
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
# Zenodo upload metadata — WebSP-Eval PETS 2026 artifact File to upload: `webspeval_code-1.0.0-83026e5.zip` (2.4 MB, byte-identical to GitHub commit `83026e5a30bcacbacefd600953f9acb9b6c5a21c`). ## Form fields - **Resource type:** Software - **Title:** WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks (PETS 2026 Artifact) - **Publication date:** 2026-07-10 - **Version:** 1.0.0 - **Creators** (affiliation for all: University…

### doi:10.48448/kyp7-cc90
**InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection** (2026) — Underline Science Inc. · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48448/kyp7-cc90
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Graphical User Interface (GUI) Agents, powered by multimodal large language models (MLLMs), have shown great potential for task automation on computing devices such as computers and mobile phones. However, existing agents face challenges in multi-step reasoning and reliance on textual annotations, limiting their effectiveness. We introduce InfiGUIAgent, an MLLM-based GUI Agent trained with a two-stage…

### doi:10.48550/arxiv.2410.13757
**MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation** (2024) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2410.13757
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Existing Multimodal Large Language Model (MLLM)-based agents face significant challenges in handling complex GUI (Graphical User Interface) interactions on devices. These challenges arise from the dynamic and structured nature of GUI environments, which integrate text, images, and spatial relationships, as well as the variability in action spaces across different pages and tasks. To address these…

### doi:10.1109/icassp55912.2026.11463965
**AITG: Automating Intent-Oriented Task Generation for Mobile GUI-Agent** (2026) — n/a · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.1109/icassp55912.2026.11463965
signals: automat\w+\s+(?:\w+\s+){0,2}(?:workflow|pipeline)\b
touchpoints: none
The advancement of large language models has significantly propelled research in mobile graphical user interface (GUI) agents, concurrently amplifying the demand for high-quality benchmark and data. However, existing benchmark data collection methodologies remain heavily reliant on manual effort, especially for designing high-quality queries for mobile GUI-agent. Furthermore, most benchmarks and training data for mobile GUI…

### doi:10.48550/arxiv.2606.05171
**AppAgent-Claw: CLI Is All You Need for GUI Automation** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2606.05171
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
The OpenClaw platform provides a practical foundation for automation through its skill-oriented architecture, organizing external capabilities into lightweight, reusable components that can be invoked efficiently through a command-line interface (CLI). However, a significant bottleneck remains: many real-world tasks are confined to graphical user interfaces (GUIs) with no stable API available. While LLM-based GUI agents offer…

### arxiv:2604.13531
**RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management** (2026) — arXiv (Cornell University) · cites 0 · score 4 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2604.13531
signals: agentic
touchpoints: none
Graphical User Interface (GUI) agents show strong capabilities for automating web tasks, but existing interactive benchmarks primarily target benign, predictable consumer environments. Their effectiveness in high-stakes, investigative domains such as authentic e-commerce risk management remains underexplored. To bridge this gap, we present RiskWebWorld, the first highly realistic interactive benchmark for evaluating GUI agents in e-commerce…

### arxiv:2504.14239
**InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners** (2025) — arXiv · cites 0 · score 4 (strong 1) · periphery/interface_agents · arXiv:2504.14239
signals: (?:LLM|large[-\s]language[-\s]model|GPT|foundation model|language model)[-\s](?:powered|assisted|driven|augmented|based|enabled)\s+(?:\w+\s+){0,2}(?:workflow|pipeline|automation|framework|system|assistant|agents?|orchestrat\w+)
touchpoints: none
Multimodal Large Language Models (MLLMs) have powered Graphical User Interface (GUI) Agents, showing promise in automating tasks on computing devices. Recent works have begun exploring reasoning in GUI tasks with encouraging results. However, many current approaches rely on manually designed reasoning templates, which may result in reasoning that is not sufficiently robust and adaptive for…

### arxiv:2608.21374
**LitReview Arena: Evaluating Literature Review Agents with Battle-Style Peer Review Platform** (2026) — arXiv · cites 0 · score 4 (strong 1) · periphery/science_of_science · arXiv:2608.21374
signals: agentic
touchpoints: none
Literature reviews are essential to scientific progress, but rigorously evaluating automatically generated reviews remains difficult because many aspects of research utility depend on expert judgment rather than reference-overlap metrics. We introduce LitReview Arena, a battle-style evaluation platform with a structured protocol tailored to literature review quality: domain experts with AI paper-writing experience compare anonymized drafts,…

### doi:10.1007/s00146-026-03049-y
**Trust in human–AI collaboration in finance: a bibliometric–systematic literature review** (2026) — AI & Society · cites 1 · score 3 (strong 1) · periphery/science_of_science · doi:10.1007/s00146-026-03049-y
signals: \bAI agents?\b
touchpoints: hpc_scale_out
Abstract Artificial intelligence (AI) is becoming deeply embedded in financial services, including credit scoring, robo-advisory, trading, compliance, and reporting. In these contexts, failures of trust in human–AI collaboration do not merely affect technology adoption but raise fiduciary, reputational, and systemic concerns. Yet, despite its centrality, trust remains conceptually fragmented and inconsistently operationalized across the literature.…

### doi:10.48550/arxiv.2605.11720
**A Research Agenda on Agents and Software Engineering: Outcomes from the Rio A2SE Seminar** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2605.11720
signals: agentic
touchpoints: hpc_scale_out
The rise of agentic AI is reshaping software engineering in two intertwined directions: agents are increasingly applied to support software engineering tasks, and Agentic AI systems themselves are complex systems that require re-thinking currently established software engineering practices. To chart a coherent research agenda covering the two directions, we organized the A2SE seminar in Rio…

### doi:10.48550/arxiv.2509.01619
**Throttling Web Agents Using Reasoning Gates** (2025) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2509.01619
signals: model context protocol
touchpoints: tool_exposure
AI web agents use Internet resources at far greater speed, scale, and complexity -- changing how users and services interact. Deployed maliciously or erroneously, these agents could overload content providers. At the same time, web agents can bypass CAPTCHAs and other defenses by mimicking user behavior or flood authentication systems with fake accounts. Yet providers…

### doi:10.17632/bzfctjcfcf.2
**Bibliometric Dataset and Systematic Review Protocol for: Orchestrating the Cognitive Supply Chain** (2026) — Mendeley Data · cites 0 · score 3 (strong 1) · periphery/science_of_science · doi:10.17632/bzfctjcfcf.2
signals: agentic
touchpoints: hpc_scale_out
This dataset contains the supplementary materials for the systematic literature review titled 'Orchestrating the Cognitive Supply Chain: A Review of Agentic AI, Asset Administration Shells, and Data Spaces in the Era of Industry 5.0'. It includes: (1) The exact Boolean search strings used for Scopus and Web of Science; (2) The full list of included…

### doi:10.48550/arxiv.2405.15793
**SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (2024) — arXiv (Cornell University) · cites 29 · score 3 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2405.15793
signals: language model agents?
touchpoints: none
Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit…

### doi:10.37547/tajet/volume06issue07-11
**Explainable AI In Software Engineering: Enhancing Developer-AI Collaboration** (2024) — The American Journal of Engineering And Technology · cites 12 · score 3 (strong 1) · periphery/software_engineering · doi:10.37547/tajet/volume06issue07-11
signals: \bAI agents?\b
touchpoints: none
Artificial Intelligence (AI) tools are increasingly integrated into software engineering tasks such as code generation, defect prediction, and project planning. However, widespread adoption is hindered by developers’ skepticism toward opaque AI models that lack transparency. This paper explores the integration of Explainable AI (XAI) into software engineering to foster a “developer-in-the-loop” paradigm that enhances trust,…

### doi:10.48550/arxiv.2601.20171
**Who Writes the Docs in SE 3.0? Agent vs. Human Documentation Pull Requests** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/software_engineering · doi:10.48550/arxiv.2601.20171
signals: \bAI agents?\b
touchpoints: none
As software engineering moves toward SE3.0, AI agents are increasingly used to carry out development tasks and contribute changes to software projects. It is therefore important to understand the extent of these contributions and how human developers review and intervene, since these factors shape the risks of delegating work to AI agents. While recent studies…

### doi:10.5281/zenodo.19772005
**Replication Package for: "Understanding the Rejection of AI-Generated Code in Pull Requests** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · periphery/software_engineering · doi:10.5281/zenodo.19772005
signals: \bAI agents?\b
touchpoints: none
Replication Package: Understanding the Rejection of AI-Generated Code in Pull Requests This repository contains the supplementary material, datasets, and analysis scripts necessary to replicate the findings of the paper "Understanding the Rejection of AI-Generated Code in Pull Requests", submitted to the 40th Brazilian Symposium on Software Engineering (SBES 2026). ## Repository Structure and Contents This…

### doi:10.1007/s11334-026-00652-6
**Augmenting software engineering with AI. The ai4se taxonomy and its use** (2026) — Innovations in Systems and Software Engineering · cites 0 · score 3 (strong 1) · periphery/software_engineering · doi:10.1007/s11334-026-00652-6
signals: agentic
touchpoints: none
Abstract Although model-driven software engineering (MDSE) has proven effective in managing complex systems, its industrial adoption remains limited by the substantial maintenance overhead required for models and the specialised skills demanded of developers. Meanwhile, advances in artificial intelligence (AI), particularly generative and agentic AI, have shown great promise in automating code-related tasks such as comprehension,…

### doi:10.5281/zenodo.19712387
**Browser Automation vs. Geo-Restrictions: The Israeli Case** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.5281/zenodo.19712387
signals: \bAI agents?\b
touchpoints: none
Episode summary: Browser automation promises to eliminate tedious, repetitive tasks—like filling out job applications or submitting monthly tax forms. But in Israel, strict geo-restrictions and aggressive bot detection turn simple automation into a technical arms race. This episode explores why government and banking sites block foreign IPs, how Cloudflare's fingerprinting catches headless browsers, and whether…

### doi:10.52202/085713-1585
**Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence** (2025) — arXiv · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.52202/085713-1585
signals: \bAI agents?\b
touchpoints: none
AI agents today are mostly siloed - they either retrieve and reason over vast amount of digital information and knowledge obtained online; or interact with the physical world through embodied perception, planning and action - but rarely both. This separation limits their ability to solve tasks that require integrated physical and digital intelligence, such as…

### doi:10.48550/arxiv.2407.17490
**AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents** (2024) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2407.17490
signals: \bAI agents?\b
touchpoints: none
AI agents have drawn increasing attention mostly on their ability to perceive environments, understand tasks, and autonomously achieve goals. To advance research on AI agents in mobile scenarios, we introduce the Android Multi-annotation EXpo (AMEX), a comprehensive, large-scale dataset designed for generalist mobile GUI-control agents which are capable of completing tasks by directly interacting with…

### arxiv:2602.10814
**See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2602.10814
signals: \bAI agents?\b
touchpoints: none
Block-based programming environments such as Scratch play a central role in low-code education, yet evaluating the capabilities of AI agents to construct programs through Graphical User Interfaces (GUIs) remains underexplored. We introduce ScratchWorld, a benchmark for evaluating multimodal GUI agents on program-by-construction tasks in Scratch. Grounded in the Use-Modify-Create pedagogical framework, ScratchWorld comprises 83 curated…

### doi:10.48550/arxiv.2605.28258
**GUI Agents for Continual Game Generation** (2026) — arXiv (Cornell University) · cites 0 · score 3 (strong 1) · periphery/interface_agents · doi:10.48550/arxiv.2605.28258
signals: agentic
touchpoints: none
Generating a game is not the same as making one that can be played. Despite advances in code generation, existing approaches treat game generation as one-shot translation from prompt to artifact, leaving interaction-level failures undetected. We argue that evaluating and improving game generation requires a player, and study two roles for graphical user interface (GUI)…

### doi:10.5281/zenodo.19424075
**The Peer Review Experiment: The Root Failure of the Modern Knowledge System** (2026) — Zenodo (CERN European Organization for Nuclear Research) · cites 0 · score 3 (strong 1) · periphery/science_of_science · doi:10.5281/zenodo.19424075
signals: agentic
touchpoints: none
Title: The Peer Review Experiment: The Root Failure of the Modern Knowledge System Description:This essay reframes peer review not as a timeless safeguard of scientific rigor but as a mid‑20th‑century institutional experiment whose underlying assumptions—expert neutrality, disciplinary coherence, and methodological stability—no longer hold under contemporary conditions. Drawing on evidence from mass retractions, compromised review processes,…

### doi:10.64898/2026.07.01.26356995
**Comparing Artificial Intelligence versus Human Screening in Systematic Reviews** (2026) — medRxiv · cites 0 · score 3 (strong 1) · periphery/science_of_science · doi:10.64898/2026.07.01.26356995
signals: agentic
touchpoints: none
Abstract Introduction Systematic reviews are essential for informing health policy and practice. Artificial intelligence (AI) automates the article screening process and produces time savings, although the performance of AI screening compared to traditional human screening remains uncertain. We undertook this study to compare the performance of two agentic AI tools, namely Loon Lens TM and…

### doi:10.29121/shodhkosh.v7.i10s.2026.7927
**HUMAN-ARTIFICIAL INTELLIGENCE COLLABORATION IN KNOWLEDGE WORK: A SYSTEMATIC LITERATURE REVIEW OF PRODUCTIVITY, CREATIVITY, AND DECISION** (2026) — ShodhKosh Journal of Visual and Performing Arts · cites 0 · score 3 (strong 1) · periphery/science_of_science · doi:10.29121/shodhkosh.v7.i10s.2026.7927
signals: \bAI agents?\b
touchpoints: none
Human–Artificial intelligence (AI) is becoming increasingly prevalent in a variety of knowledge work fields, such as accounting, finance, logistics, marketing, manufacturing, and management. While AI is commonly utilized to enhance productivity, creativity, and decision-making in these fields, the impact of collaboration between humans and AI agents on these fields remains fragmented and incomplete. This systematic…

