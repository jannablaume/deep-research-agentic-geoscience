# Evidence extracts

One block per `core` source. Verbatim quoted sentences only; `NOT FOUND: <what was looked for>`
where the text does not contain it. First line of each block is the URL and how the text was
obtained. The report is written from these blocks.

## doi:10.1145/3731599.3767349

https://doi.org/10.1145/3731599.3767349 - full text read from the local PDF store (`3731599.3767349.pdf`, the ACM version of record, SC Workshops '25). **In v0.1 this record was read from arXiv:2502.12280 and the identity match was inferred; it is now verified against the published version, and three of its quotes changed.** The preprint wording is noted below each one.

**What was built.** "In this work, we implemented Parsl to the LangChain tool calling to bridge the gap between the LLM agent and the HPC resource. Two implementations were set up and tested on a local Nvidia GPU workstation and the Polaris/ALCF HPC system." *(v0.1 quoted the preprint: "we implemented Parsl to the LangChain/LangGraph tool call setup, to bridge the gap between the LLM agent to the computing resource." The published version drops LangGraph from the sentence, names the HPC resource, and adds that there are two implementations.)*

**The two implementations.** "The first setup was implemented by modifying the LangChain tool calling, which converts the LangChain tool calls to Parsl functions and queues them to the Parsl workers for parallel execution. The second approach was achieved by designing a Parsl ensemble function as an LLM tool, which performed parallel tasks." *(This distinction is not in the preprint quote v0.1 carried.)*

**What it can call.** "The simulation tool is set up with the OpenMM software package to run on Nvidia GPUs. It takes a PDB file as input, and sets [up the system]." "It builds the protein topology, which comprises all the atomic bonded and nonboned interaction, using Gromacs pdb2gmx with Charm36m force field."

**The model.** "used OpenAI gpt-4o-mini as the LLM."

**How it was evaluated.** "The local runs were performed on a lambda machine with 8 Nvidia V100 GPUs. We prompted the workflow to run an 8-simulation ensemble with different protein input instructions, including a local PDB file, a PDB ID, or just protein names." "On Polaris, we tested 100 simulations with 100 GPUs on 25 nodes and 80 runs with 40 GPUs on 10 nodes."

**What it achieved.** "All 8 simulation were then submitted to the Parsl workers and finished in ~60 seconds." "On the Nvidia A100 GPUs, the 50-ps simulations of 2KKJ ran in ~340 ns/day, and were then finished within ~3 minutes. The majority of the run time was the queue time on Polaris." - the queue wait itself was "~265 minutes".

**A scaling limit the preprint quote did not carry.** "While implemented with the Parsl tool node (setup 1), the number of tool calls that LLM agent made were capped around 24, with 100 simulations specified in the input prompt during the experiment. Therefore, a different implementation was necessitated on the HPC systems for massive parallel tool calls."

**A hallucination the authors report.** "When the search tool only returned the top 5 results, it fetched PDB IDs of 148L, 1B7E, 1LYZ, 2LYZ, 3WEL, 5R2Z, 7BVM, and 7F26. Among these results, 1B7E is the structure of E. Coli transferase inhibitor, 3WEL is Sugar Beet alpha-Glucosidase and 5R2Z is Endothiapepsin. These PDB IDs were hallucinated by the LLM agent, as only 5 search results were generated from the researcher." "Based only on the model context, it failed to provide correct information for the following simulation runs."

**Maturity claimed.** "Our implementation enables the LLM agent to access any computing resource with a compatible Parsl configuration." *(v0.1 quoted the preprint's "any compatible computing resource through Parsl".)*

**Limitations, in the authors' terms.** "Due to the LLM tool call limitation and computing system requirements, it still requires tailoring of the tool call setup depending on the tasks and computing platforms." / "However, it is now the user's responsibility to develop the simulation ensemble function with Parsl." / "the computing nodes had no internet access by default, and the unpredictable queue time on the HPC system caused delays." / "This end-to-end design is less dependent on the LLM capability, and less likely to err, but too rigid for more sophisticated tasks."

## doi:10.48550/arxiv.2604.07681

https://arxiv.org/html/2604.07681 — full text read from arXiv HTML

**What was built.** "we present a scalable, hierarchical multi-agent framework for orchestrating high-throughput screening campaigns."

**What it can call.** "Executor agents invoke simulation tools exposed by the Chemistry MCP server to launch atomistic simulations through Parsl."

**How it was evaluated.** "we employed the open-weight gpt-oss-120b model to orchestrate a high-throughput screening of the Computation-Ready Experimental (CoRE) Metal-Organic Framework (MOF) database"

**What it achieved.** "the top 20% of candidates demonstrated high performance, with working capacities achieving 7.06 mol/kg."

**Maturity claimed.** "This work establishes a flexible paradigm for LLM-driven scientific automation on HPC systems, with broad applicability to materials discovery and beyond."

## doi:10.48550/arxiv.2512.07917

https://arxiv.org/html/2512.07917 — full text read from arXiv HTML

**What was built.** "We introduce CFD-copilot, a domain-specialized LLM framework designed to facilitate natural language-driven CFD simulation from setup to post-processing."

**What it can call.** "utilizes the model context protocol (MCP), an open standard that decouples LLM reasoning from external tool execution."

**How it was evaluated.** "The framework was evaluated on canonical aerodynamic benchmarks, including the NACA 0012 airfoil and the complex three-element 30P-30N high-lift configuration, to demonstrate its applicability to practical engineering problems."

**What it achieved.** "For the NACA 0012 airfoil case, the system achieved an average success rate of 52.86%, with velocity and pressure accuracies of 96.41% and 93.22%, respectively."

**Maturity claimed.** "By reducing reliance on domain-specific syntax and manual setup, CFD-copilot lowers the barrier to entry and allows operators to focus on the scientific objectives of their analysis rather than the intricacies of implementation."

## doi:10.48550/arxiv.2606.07850

https://arxiv.org/html/2606.07850 — full text read from arXiv HTML

**What was built.** "We present PDE-Agents, a multi-agent ecosystem that automates the full lifecycle of partial differential equation (PDE) / finite element method (FEM) simulations through natural-language interaction."

**What it can call.** "The Simulation Agent executes a ReAct loop with up to 25 reasoning steps and nine tools: check_config_warnings, query_knowledge_graph, validate_config, run_simulation, modify_config, debug_simulation, list_recent_runs, get_run_status, run_parametric_sweep."

**How it was evaluated.** "We run a three-way ablation study (KG On, KG Off, KG Smart) over 50 tasks with a frozen knowledge graph."

**What it achieved.** "KG Smart achieves 100% success and the highest output quality (physics score 0.933 vs. 0.853 for KG Off, MPF 0.926 vs. 0.796)."

**Maturity claimed.** "demonstration of production-grade reliability for the full agent stack"

## doi:10.11578/dc.20260516.1

https://www.osti.gov/doecode/biblio/181158 — OSTI DOECODE software record read in full plus the linked GitHub README. This is a software record, not a paper: it has no evaluation section, so maturity, autonomy, failure handling and touchpoints are absent by construction rather than by oversight

**What was built.** "matsim-agents is a multi-agent AI framework for atomistic materials simulation and discovery."

**What it can call.** "Multi-agent AI framework for atomistic materials simulation and discovery." The README states the system orchestrates large language models, machine-learned interatomic potentials and ASE-based atomistic workflows, with an Executor node that dispatches matching tools like structure relaxation.

**How it was evaluated.** NOT FOUND: the record contains no evaluation section and reports no test of the agent system.

**What it achieved.** NOT FOUND: no headline result with a number and unit is reported for the agent system.

**Maturity claimed.** NOT FOUND: no self-assertion about maturity or readiness beyond the v1.0 release designation.

## doi:10.1016/j.dche.2026.100312

https://doi.org/10.1016/j.dche.2026.100312 - full text read from the local PDF store (`1-s2.0-S2772508126000256-main.pdf`, *Digital Chemical Engineering* 19 (2026) 100312, the version of record). **In v0.1 this record was read from arXiv:2601.11650v1 and the identity match was inferred; the published version adds a third case study, so the evaluation described in v0.1 was incomplete.**

**What was built.** "To address this, a large language model (LLM) agent is integrated with AVEVA Process Simulation (APS) via Model Context Protocol (MCP), allowing natural language interaction with rigorous process simulations."

**What it can call.** "An MCP server toolset enables the LLM to communicate programmatically with APS using Python, allowing it to execute complex simulation tasks from plain-language instructions."

**How it was evaluated.** "Three case studies assess the framework across different task complexities and interaction modes." *(v0.1, from the preprint, recorded "Two water-methanol separation case studies assess the framework across different task complexities and interaction modes.")* The conclusion frames the same set as "Two case studies, both utilizing a water-methanol separation process as the test system, were conducted to assess the agent's performance across varying task complexities and interaction modes. In addition, a dedicated stability case study was conducted across prompt formulations, LLM versions, and process complexity to evaluate robustness beyond single-run behavior."

**What the third case study is.** "To assess stability, we vary the framework and task setup relative to the default trial (Prompt 1.0 in Case Study 1) by changing the LLM version, prompting style, and process complexity." "Using Prompt 1.0 from Case Study 1 as the default task, we repeated this flowsheet-analysis workflow across different prompt styles and LLM versions (trials 2-5 in Supplementary Material S3.3 Table S7) and additionally tested a substantially more complex process flowsheet (trial 6)."

**What it achieved.** "Close! That gives 93.9% methanol. Let me try 1.45 to get closer" / "Perfect! With a reflux ratio of 1.45, I've achieved 95.1 mol% [methanol purity in the distillate]."

**What the stability study found.** "In these repeated trials (2-5), the framework remained robust at the tool-execution and data-grounding levels. The agent consistently completed required MCP tool sequences and reliably reported simulator-grounded numerical values." "At the same time, variability was observed mainly in breadth of answers and depth of interpretation, not in basic data retrieval. The main residual weakness is therefore semantic interpretation rather than protocol execution." "This pattern indicates that retrieval is more stable than interpretation, which in turn supports our deployment strategy of dual verification: APS-level constraint enforcement plus expert review."

**Generalisation beyond the test flowsheet.** "Despite the added complexity of branched topology and recycling structure, the agent correctly reconstructed the main equipment connectivity and recycling-loop logic, indicating that the workflow is not limited to simple linear separation problems."

**Maturity claimed.** "the primary novelty is not connectivity to a commercial simulator per se, but, to the best of our knowledge, the first fully implemented and reproducible MCP-based integration with a commercial process simulator, combined with a protocol-mediated modular architecture and a trustworthiness-oriented evaluation in guided and higher-autonomy (dual-mode) operation."

**Limitations, in the authors' terms.** "While current limitations mainly involve the accurate interpretation of the physical results seen in minor reasoning mistakes, such as oversimplification or misleading suggestions, mean expert oversight is still needed." / "For inexperienced users, the main risks are overtrust in fluent but overconfident explanations, difficulty distinguishing highly relevant from marginal suggestions under open-ended prompts, and limited ability to detect unsupported derived values (e.g., economic estimates) without additional checks." / "For experienced users, the main limitations include occasional semantic mismatch in variable selection despite correct retrieval, non-negligible review effort for convergence-sensitive synthesis steps." / "the system is best positioned as a copilot that accelerates workflow execution, rather than as an autonomous decision-maker."

## doi:10.48550/arxiv.2605.20819

https://arxiv.org/pdf/2605.20819v2 — arXiv HTML returned HTTP 404 for all versions and ar5iv redirected to the abstract; full text read page by page from the PDF at arXiv:2605.20819v2

**What was built.** "DynaMate2 is a LangGraph-based multi-agent framework for converting expert-defined Python functions into persistent AI-callable tools."

**What it can call.** "Tools are bound to specific agents and can take many forms: retrievers, APIs, code interpreters, simulators, databases, or actuators, implemented as Python functions."

**How it was evaluated.** "To demonstrate the full capabilities of DynaMate2 as an agentic template for expert-defined workflows, we present a complete end-to-end molecular dynamics simulation driven entirely by natural language instructions."

**What it achieved.** "This example is intended to evaluate the orchestration of a multi-step computational workflow; it is not used to draw conclusions about NaCl-water structure, thermodynamics, or MLIP accuracy for solvated ions."

**Maturity claimed.** "For the broader scientific community, DynaMate2 offers a template rather than a finished product."

## doi:10.1145/3815572.3815744

https://www.biorxiv.org/content/10.64898/2026.06.01.729336v1.full — the ACM DOI was not retrievable; full text read from the open-access bioRxiv version of the same work

**What was built.** "a multi-agent system for automating such workflows within the DOE Systems Biology Knowledgebase (KBase)"

**What it can call.** the agent uses "wrappers for the KBase API (e.g., run_job, list_objects)" and "selects, parameterizes, validates and executes appropriate KBase applications."

**How it was evaluated.** "We integrate our LLM-as-a-Judge evaluator within LangSmith's evaluation framework, following an OpenEvals style setup in which the judge model is given both the agent generated workflow and the corresponding GT workflow"

**What it achieved.** "Claude Sonnet 4.5 (thinking enabled) achieved the highest mean score (0.906 on the EXP_MRA_0084523 dataset)"

**Maturity claimed.** "demonstrates the feasibility of domain-grounded, end-to-end scientific workflow automation in a production bioinformatics platform"

## doi:10.1016/j.cma.2026.118985

https://arxiv.org/html/2603.21011 — full text read from arXiv:2603.21011, the authors preprint with the same author list; SSRN and Elsevier both blocked. IDENTITY MATCH INFERRED, not verified against the CMAME version of record

**What was built.** "ALL-FEM, an autonomous simulation system that integrates agentic AI with domain-specific, fine-tuned LLMs for FEniCS code generation across solid, fluid, and multiphysics applications."

**What it can call.** "The Executor runs the code, captures any run-time output and errors, and returns this feedback to the FEniCS Coder."

**How it was evaluated.** "evaluated the system on 39 benchmarks that include problems of linear/nonlinear elasticity, plasticity, Newtonian/non-Newtonian flow"

**What it achieved.** "the best fine-tuned model (GPT OSS 120B) achieves code-level success of 71.79%"

**Maturity claimed.** "outperforming a non-agentic deployment of GPT 5 Thinking"

## doi:10.5281/zenodo.19597589

https://zenodo.org/doi/10.5281/zenodo.19597589 — Zenodo software record v1.2.1 read in full plus the linked GitHub README. A software record, not a paper: there is no evaluation, results or limitations section

**What was built.** "`aihydro-tools` is the Python backbone of the AI-Hydro platform. It turns a conversation with an AI agent into real hydrological computation - watershed delineation, streamflow retrieval, signature extraction, terrain analysis, and model calibration - with full structured provenance recorded automatically at every step."

**What it can call.** "Any AI model that supports MCP - Claude, GPT, Gemini - can call these tools directly."

**How it was evaluated.** "a deterministic benchmark suite (~26 fixture tasks) verifying computation paths"

**What it achieved.** NOT FOUND: no headline number, accuracy figure or success rate is reported anywhere in the record or README.

**Maturity claimed.** "reproducibility should be structural, not post-hoc"

## doi:10.25394/pgs.32118403

https://api.figshare.com/v2/articles/32118403 — the Purdue repository returned HTTP 403; metadata retrieved from the Figshare API and the full 19.8 MB thesis PDF downloaded and converted with pdftotext. This is an MS thesis, not a doctoral thesis

**What was built.** "Here, we show that a physics-driven generative AI, PUR-1 GPT, can be integrated as an interface with the Purdue University Reactor Number 1 Digital Twin (PUR-1 DT) as an operator-facing semantic layer for document retrieval, surrogate-model invocation, vector database visualization, and live reactor-state interpretation."

**What it can call.** "Surrogate Model Invocation: The Predict_K_Surrogate or Predict_Flux_Metrics agentic tool fetches the currently loaded Monte Carlo surrogate model path from the main DT GUI via a Flask API on a local host or default HOSVD model for the neutron flux distribution, executes the prediction, and posts the keff and flux distribution results back to update the visualization windows."

**How it was evaluated.** "Additionally, PUR-1 GPT's integration with live reactor data/ signals in the agentic domain is described in terms of it data/information acquisition workflow for keff (Fig. 5.4) and flux distribution (Fig. 5.5) predictions alike."

**What it achieved.** "The overall percentage difference between the OpenMC and experimental results was ~ 5.37% - 6.11%; thus, it quantifies the trust in the CAD-based Monte Carlo model of PUR-1."

**Maturity claimed.** "This work demonstrates a proof-of-concept architecture for using large language models as controlled interfaces to reactor digital twins."

## doi:10.48550/arxiv.2603.12813

https://arxiv.org/html/2603.12813 — full text read from arXiv HTML on the first attempt

**What was built.** "a multi-agent system that decomposes process development tasks: one agent solves the abstract engineering problem while another implements the solution as Chemasim code."

**What it can call.** "An extension is developed to directly trigger runs of the Chemasim simulation engine from the text editor. The extension can also be used by the agent, allowing it to autonomously run simulations and read and interpret the console output."

**How it was evaluated.** "three case studies covering a reaction-separation process, pressure-swing distillations for binary azeotropes, and heteroazeotropic distillations with entrainer selection."

**What it achieved.** "the obtained rigorous simulation results are in very good agreement with the simplified mass balance estimates of the process development agent."

**Maturity claimed.** "In all cases, the process development agent is able to design reasonable process flowsheets based solely on the analysis of thermodynamic behavior"

## doi:10.48550/arxiv.2608.14573

https://arxiv.org/html/2608.14573 — full text read from arXiv HTML on the first attempt

**What was built.** "WARA, a closed-loop multi-agent system for automated wireless optimization research"

**What it can call.** "invoke the designated solver" - the system executes Python/CVXPY code within "a fixed validation harness"

**How it was evaluated.** "ten manuscripts produced by the proposed closed-loop WARA workflow from ten wireless optimization topics" scored by "a structured LLM-based ScoringAgent"

**What it achieved.** "WARA obtains an average score of 68.5, compared with 37.4 for the topic-paired one-shot LLM baseline, yielding a 31.1-point improvement"

**Maturity claimed.** "WARA can already construct a clearer optimization research structure"

## doi:10.48550/arxiv.2509.18178

https://arxiv.org/html/2509.18178 — full text read from arXiv HTML (v2)

**What was built.** "To address these challenges, we introduce Foam-Agent , a multi-agent framework that automates the entire end-to-end OpenFOAM workflow from a single natural language prompt."

**What it can call.** "The Runner Agent interfaces with the OpenFOAM execution environment by preparing the simulation (cleaning artifacts, setting up output capture) and running the Allrun script."

**How it was evaluated.** "We evaluated Foam-Agent using a comprehensive benchmark dataset containing 110 OpenFOAM simulation cases across 11 distinct physics scenarios."

**What it achieved.** "With Claude 3.5 Sonnet, Foam-Agent achieves an 88.2% success rate compared to 55.5% for MetaOpenFOAM and 37.3% for OpenFOAMGPT-Alt."

**Maturity claimed.** "Foam-Agent is the first system to manage the full simulation pipeline, including advanced pre-processing with a versatile Meshing Agent capable of handling external mesh files and generating new geometries via Gmsh , automatic generation of HPC submission scripts, and post-simulation visualization via ParaView/Pyvista"

## arxiv:2602.11666

https://arxiv.org/html/2602.11666 — full text read from arXiv HTML (v1). Note: the paper's Conclusion states the headline backwards, as 51% to 26%; the abstract and Section 5.1 give 26% to 51%

**What was built.** "We introduce PhyNiKCE ( Phy sical and N umer i cal K nowledge C ontext E ngineering), a neurosymbolic agentic framework designed for autonomous CFD."

**What it can call.** "By interposing this validation step, the system ensures that the final execution in OpenFOAM is numerically stable and physically consistent with the user's intent, effectively preventing unstable CFD setups."

**How it was evaluated.** "Each of the 13 unique setups was executed multiple times for consistency, resulting in 100 runs per full evaluation cycle. The three primary configurations (Baseline, Partial PhyNiKCE, and Full PhyNiKCE) were tested across this matrix, totaling 300 runs. This study therefore comprises 340 experimental runs."

**What it achieved.** "PhyNiKCE gains a 96% relative improvement over SOTA baseline, increasing the accuracy from 26% to 51%."

**Maturity claimed.** "By tracing every configuration parameter to a specific rule in the Knowledge Base, the framework offers the white-box interpretability required for safety-critical engineering certification, aligning with the principles of Trustworthy AI."

## doi:10.48550/arxiv.2511.03852

https://arxiv.org/html/2511.03852 — full text read from arXiv HTML (v2) including Appendix A

**What was built.** "We present Geothermal Analytics and Intelligent Agent, or GAIA, an AI-based system for automation and assistance in geothermal field development."

**What it can call.** "GAIA Agent, powered by a pre-trained LLM, autonomously queries knowledge bases, executes domain-specific subroutines, and orchestrates multi-step analyses."

**How it was evaluated.** "To evaluate GAIA's performance, we curated a benchmark test set comprising various geothermal-related questions. The questions are generated using the Retrieval Augmented Generation Assessment (RAGAS) framework ( Es et al., 2024 )"

**What it achieved.** "we obtained up to 1.5x improvement in response accuracy, up to 1.3x improvement in response relevancy, up to 3.1x in response faithfulness, and up to 1.4x improvement in answer correctness compared to the baseline models."

**Maturity claimed.** "GAIA represents a pioneering application of agentic RAG workflows in geothermal field development. Unlike conventional decision-support systems, it combines autonomous task orchestration, physics-based digital twin modeling, and interactive user engagement within a single platform."

## doi:10.48550/arxiv.2608.29665

https://arxiv.org/html/2608.29665 — full text read from arXiv HTML (v1)

**What was built.** "To explore fully local agentic science, this work evaluates an open-weights qwen3:4b model executing an autonomous scientific pipeline across varying hardware constraints."

**What it can call.** "Every component runs locally and unmetered, on an open-weights qwen3:4b model [ 15 ] on a single local GPU via Ollama [ 16 ] and the SIESTA electronic structure package [ 17 ] ."

**How it was evaluated.** "Evaluated against 201 expert judgements, the extractor achieves 95.7 % precision (95% CI 90.3-98.1 %) and 67.3 % recall (59.8-74.0 %), ensuring extracted parameters are strictly factual."

**What it achieved.** "Driven to convergence, the workflow reproduces published lattice constants with a mean absolute relative error of 2.3 % where the relaxed structure retains its prototype"

**Maturity claimed.** "establishing that lightweight open-weights models can reliably drive autonomous agentic workflows when bounded by deterministic code gates."

## doi:10.2139/ssrn.4921381

https://arxiv.org/pdf/2407.21320 — the SSRN record is a duplicate of arXiv:2407.21320; arXiv HTML returns 404 at every version and ar5iv fails, so the full text was read from the PDF via pdftotext

**What was built.** "MetaOpenFOAM, as a novel multi-agent collaborations framework, aims to complete CFD simulation tasks with only natural language as input."

**What it can call.** "MetaOpenFOAM takes user requirements as input, generates OpenFOAM input files through LLM, and returns simulation results that meet user requirements after automatically running OpenFOAM."

**How it was evaluated.** "Eight cases, covering a range of multidimensional flow problems including both 2D and 3D flows, various compressible and incompressible flows with various physical processes such as turbulence, heat transfer, and combustion, were tested."

**What it achieved.** "Overall, the average pass rate (pass@1) of 85% and high executability score 3.6 demonstrate the outstanding performance of MetaOpenFOAM."

**Maturity claimed.** "Therefore, in terms of lowering the barrier to use, reducing labor costs, and increasing efficiency, MetaOpenFOAM is revolutionary."

## doi:10.48550/arxiv.2603.26005

https://arxiv.org/html/2603.26005 — full text read from arXiv HTML (v2); numeric tables render empty in the HTML so Tables 3 and 4 were additionally read from the PDF via pdftotext

**What was built.** "In this work, we introduce AutoB2G , an agentic framework for spatio-temporal building-grid co-simulation. AutoB2G formulates simulation construction as a workflow orchestration problem, where natural-language user intents are translated into executable simulation pipelines."

**What it can call.** "AutoB2G integrates CityLearn V2 ( Nweye et al., 2025 ) with power-system simulators including Pandapower and OpenDSS, to enable both balanced and three-phase unbalanced building-grid co-simulation."

**How it was evaluated.** "These simulation tasks are evaluated using three metrics: Execution Success Rate , which measures whether the generated workflow runs end-to-end without errors and produces the required outputs; Configuration Correctness , which assesses whether the simulation pipeline, modules, controllers, and network settings are correctly configured; and Simulation Validity , which examines whether the generated outputs are physically plausible and consistent with the task objectives."

**What it achieved.** "Overall, the complete SOCIA framework achieves the highest execution reliability, particularly for medium and complex tasks involving multi-stage orchestration and dependency coordination."

**Maturity claimed.** "Our results further highlight the potential of agentic LLMs as orchestration layers for scientific simulation in energy systems."

## doi:10.48550/arxiv.2605.06607

https://arxiv.org/html/2605.06607 — full text read from arXiv HTML including appendices A-G

**What was built.** "We present AI CFD Scientist, an open-source AI scientist for CFD that, to our knowledge, is the first to span literature-grounded ideation, validated execution, vision-based physics verification, source-code modification, and figure-grounded writing within a single inspectable workflow."

**What it can call.** "The framework runs on OpenFOAM through Foam-Agent and exposes three coupled pathways"

**How it was evaluated.** "AI CFD Scientist is run end-to-end with GPT-5.5. All evaluation is manual because no automated CFD-paper rubric currently scores the workflows the system produces."

**What it achieved.** "the system autonomously discovers a Spalart-Allmaras runtime correction that reduces lower-wall Cf RMSE against DNS by 7.89%"

**Maturity claimed.** "The framework is supervised scientific assistance, not unattended publication."

## doi:10.48550/arxiv.2505.04997

https://arxiv.org/html/2505.04997 — full text read from arXiv HTML. Note: arXiv now serves the updated version of this record, so the text read is the FoamBench/CFDLLMBench revision rather than the original 2025 v1

**What was built.** "We present Foam-Agent, a multi-agent framework that leverages large language models (LLMs) to automate the end-to-end CFD workflow in OpenFOAM from a single natural-language prompt."

**What it can call.** "Around these contributions, six specialist agents span planning, meshing, file writing, execution, review, and visualization; Foam-Agent additionally exposes its capabilities through the Model Context Protocol as a deployment surface for external orchestrators."

**How it was evaluated.** "We evaluate Foam-Agent on FoamBench, the end-to-end OpenFOAM simulation benchmark of the CFDLLMBench suite"

**What it achieved.** "On FoamBench, Foam-Agent achieves an 88.2% execution success rate on the 110 Basic-tier tasks and 62.5% on the out-of-distribution Advanced tier, all without expert intervention."

**Maturity claimed.** "These results show how strategic harnessing of specialized multi-agent systems can reduce expertise barriers while preserving the rigor of solver-based simulation workflows."

## doi:10.1016/j.compenvurbsys.2026.102449

https://discovery.ucl.ac.uk/id/eprint/10225208/1/Batty_ssrn-5596992.pdf — the Elsevier route returned only a redirect stub; full text read from the open-access accepted manuscript in the UCL repository

**What was built.** "This paper introduces a conceptual framework at the intersection of agentic AI, MCP, and cognitive digital twins."

**What it can call.** "For instance, in building energy management, agents can invoke tools such as EnergyPlus, OpenStudio, or Modelica to simulate HVAC performance and evaluate retrofitting strategies."

**How it was evaluated.** NOT FOUND: there is no evaluation, experiment or case-study section of the authors own system. The nearest is a description of prior work by others: "A real-world prototype is the RECOIL digital twin, developed by the University of Tennessee and Oak Ridge National Laboratory (ORNL)".

**What it achieved.** NOT FOUND: no numeric result of any kind is reported.

**Maturity claimed.** "Ultimately, agentic digital twins have the potential to evolve into a central operating system for smart cities, empowering human decision-makers with AI-augmented insights, automating operations at scale, and enabling more adaptive, efficient, and equitable urban futures."

## doi:10.48550/arxiv.2508.07035

https://arxiv.org/html/2508.07035 — full text read from arXiv HTML

**What was built.** "Here, we introduce VASPilot, an open-source platform that fully automates VASP workflows via a multi-agent architecture built on the CrewAI framework and a standardized Model Context Protocol (MCP)."

**What it can call.** "Our input-preparation tools automatically generate all necessary VASP input files and submit jobs to a Slurm scheduler."

**How it was evaluated.** "We performed band-structure and density-of-states (DOS) calculations for 2H-MoS2, plane-wave cutoff convergence tests, structural relaxations using van der Waals corrections, and band-gap comparisons across transition-metal dichalcogenides."

**What it achieved.** "In all cases, VASPilot completed the missions reliably and without manual intervention."

**Maturity claimed.** "an open-source platform that fully automates VASP workflows"

## arxiv:2607.20346

https://arxiv.org/html/2607.20346 — full text read from arXiv HTML including comparison tables

**What was built.** "IteraSim RAG, a retrieval-augmented software back-end for automated OpenFOAM case generation"

**What it can call.** "The same pipeline currently serves OpenFOAM, snappyHexMesh, blockMesh, Gmsh, pyFoam and ParaView"

**How it was evaluated.** "On an openly released 28-case benchmark spanning zero-shot setup, few-shot generalisation, single-parameter modifications and turbulence-model swaps, the pipeline attains a mean retrieval coverage of 77.9%."

**What it achieved.** "the pipeline attains a mean retrieval coverage of 77.9% (median 79.1%)"

**Maturity claimed.** "All six reference configurations run to completion on OpenFOAM v2506, and two synthetically corrupted cases are diagnosed and repaired within the bounded Reviewer loop."

## doi:10.31223/x5f47g

https://eartharxiv.org/repository/object/12219/download/21897/ — full 28-page EarthArXiv preprint PDF including supplementary sections S1-S4 read in full

**What was built.** "We propose an Agentic SWMM workflow, which embeds 'Skills' and model context protocols to automate model configuration, execution, and extract and plot quantities of interest."

**What it can call.** "In the proposed design, three MCP servers are used: a) swmm-gis-mcp for DEM data preprocessing; b) swmm-runner-mcp: generates inputs, runs swmm5, extracts quantities of interest (QoIs) and continuity metrics; and c) swmm-plot-mcp: reads INP/OUT artifacts and produces figures that conform to a fixed user's specification."

**How it was evaluated.** "In this section, we tested whether the results produced by the packaged MCP service are numerically consistent with a direct command-line interface (CLI) SWMM execution under identical model inputs."

**What it achieved.** "Figure 4 a and b, and Figure S2 in the Supplementary file show that the evaluation metrics, R2 and NSE are all identically 1.0, demonstrating consistent predictions across all 30 simulations."

**Maturity claimed.** "This enables hydrological analysis and modelling, and to the authors' knowledge, this is the first time Agentic AI (OpenClaw) has been applied to peak runoff prediction."

## doi:10.1080/09544828.2026.2624356

https://arxiv.org/pdf/2404.17525v3 — no arXiv HTML exists at any version and ar5iv fails; full text read from the PDF via pdftotext. The Taylor and Francis version of record was not fetched

**What was built.** "To address this, we propose a framework that leverages a pretrained Large Language Model (LLM) coupled with FEM module to autonomously generate, evaluate, and refine structural designs based on performance specifications and quantitative feedback."

**What it can call.** "We embed a pre-trained LLM in a closed-loop pipeline with a FEM module that scores each design iteration."

**How it was evaluated.** "Performance statistics are aggregated over ten independent trials for each configuration to ensure robust assessment."

**What it achieved.** "Comparative analysis against traditional optimization methods, such as Non-dominated Sorting Genetic Algorithm II (NSGA-II), shows that LLM-guided optimization achieves faster convergence and requires fewer FEM evaluations in highly discrete, multi-faceted design spaces"

**Maturity claimed.** "These results highlight the promise of LLM agents to function as a new class of natural language-based, reasoning-driven optimizers capable of independently generating and iteratively improving viable engineering solutions through structured feedback."

## doi:10.48550/arxiv.2604.27753

https://arxiv.org/pdf/2604.27753 — no arXiv HTML exists at any version; full 7-page text read from the PDF via pdftotext

**What was built.** "This article outlines a new framework of traffic light optimization through a digital twin of the transport infrastructure, managed by agentic AI to ensure real-time autonomous decisions."

**What it can call.** "an Action Layer that executes optimized signal adjustments via the Model Context Protocol (MCP) and traffic management APIs in a secure and regulation-compliant manner."

**How it was evaluated.** "Our experiments were based on simulations for a synthetic urban traffic network with 12 traffic-light-controlled intersections with varying traffic volumes (representing a mid-sized city street grid)."

**What it achieved.** "The proposed system also lowers the average vehicle delay to 49 seconds compared to 54 seconds (RL) and 60 seconds (Fixed-Time), which corresponds to an 18% reduction in waiting time over fixed-time control and a 9% reduction over the RL controller."

**Maturity claimed.** "The present work uniquely combines all three components-digital twin, agentic AI with LLM-driven reasoning, and MCP-secured action execution-into a unified, compile-ready operational framework."

## doi:10.48550/arxiv.2412.17146

https://arxiv.org/html/2412.17146 — full text read from arXiv HTML and verified against the PDF

**What was built.** "In this work we introduce FoamPilot, a proof-of-concept LLM agent designed to enhance the usability of FireFOAM, a specialized solver for fire dynamics and fire suppression simulations built using OpenFOAM, a popular open-source toolbox for computational fluid dynamics (CFD)."

**What it can call.** "The tool node provides access to utilities, which in the present work consist of a Shell Command Tool, a Python Interpreter Tool, and a Retrieval-Augmented Generation (RAG) tool."

**How it was evaluated.** "Therefore, each experiment was repeated five times to assess stability. A single user prompt was used in each experiment, and the same prompt was used in each repeat."

**What it achieved.** "In our exploration, we found that the agent was consistently successful for tasks of low complexity, but that its success rate dropped precipitously with increasing task complexity."

**Maturity claimed.** "The integration of these functionalities into a single LLM agent is a step aimed at accelerating the simulation workflow for engineers and scientists employing FireFOAM"

## arxiv:2607.01812

https://arxiv.org/html/2607.01812 — full text read from arXiv HTML and verified against the PDF

**What was built.** "This work introduces TO-Master, a large language model (LLM) agent framework that turns finite-element-based TO into a conversational, tool-orchestrated workflow."

**What it can call.** "The FEA and sensitivity evaluation are performed by the JAX-FEM-based solver described in Sec. 2.6."

**How it was evaluated.** "Each fuzzy-prompt condition was repeated five times. In total, the ablation study contains 6 reference runs and 6 x 4 x 5 = 120 fuzzy-prompt runs."

**What it achieved.** "The full instruction achieves the highest success rate, whereas removing tool-usage constraints causes the largest performance drop."

**Maturity claimed.** "By combining LLM-agent orchestration with deterministic finite element and optimization tools, TO-Master removes the burden of trivial setup and routine model construction, lowers the modeling barrier of TO, and preserves a reliable numerical workflow."

## doi:10.1063/5.0257555

https://arxiv.org/html/2501.06327 — full text read from the arXiv preprint arXiv:2501.06327; the AIP version of record was not fetched because AIP is known to block automated clients

**What was built.** "This work presents a large language model (LLM)-based agent OpenFOAMGPT tailored for OpenFOAM-centric computational fluid dynamics (CFD) simulations, leveraging two foundation models from OpenAI: the GPT-4o and a chain-of-thought (CoT)-enabled o1 preview model."

**What it can call.** "Inside the OpenFOAM agent, an Interpreter, Builder, and Runner collaborate to set up and execute the necessary OpenFOAM operations."

**How it was evaluated.** "To evaluate the its capabilities, we selected six cases from the OpenFOAM tutorials encompassing single- and multiphase flow, laminar and turbulent regimes, and ranging from straightforward to application-oriented examples."

**What it achieved.** "Once equipped with RAG, the agent successfully sets up all tested cases, underscoring the significance of retrieving relevant domain knowledge for complex CFD workflows."

**Maturity claimed.** "By reducing barriers to high-fidelity simulations, our framework holds promise for accelerating innovation across both fundamental research and industrial engineering processes."

## doi:10.1038/s43246-025-00994-x

https://www.nature.com/articles/s43246-025-00994-x.pdf — the plain Nature URL redirects into an identity-provider loop; appending .pdf to the article URL fetched the full open-access PDF directly

**What was built.** "This paper introduces MatSciAgent, a multi-agent framework that leverages large language models (LLMs) for materials retrieval, continuum simulation, crystal structure generation, and molecular dynamics simulation."

**What it can call.** "At its core is a master agent that interprets user queries, identifies the task type, and delegates to task-specific agent(s) equipped with tools."

**How it was evaluated.** "To evaluate the consistency of the LLM agent, we performed 10 independent runs of the same prompt."

**What it achieved.** "MatSciAgent demonstrates stability, with parameter extraction achieving 100% success across five runs and materials extraction consistent in 9 of 10 runs."

**Maturity claimed.** "With near-perfect reproducibility in most tasks and only minor, non-impacting variations in formatting or isolated extraction failures, the system shows the stability required for materials research."

## doi:10.48550/arxiv.2602.04850

https://arxiv.org/html/2602.04850 — full text read from arXiv HTML and verified against the PDF including supporting information

**What was built.** "we introduce El Agente Quntur, a hierarchical, multi-agent AI system designed to operate not merely as an automation tool but as a research collaborator for computational quantum chemistry."

**What it can call.** "These strategies grant Quntur complete control over the ORCA 6.0 quantum chemistry package [82, 83]."

**How it was evaluated.** "We asked Quntur to autonomously execute all questions five times independently to evaluate its robustness and reliability."

**What it achieved.** "confirms that it provides the best agreement with experimental results within chemical accuracy (< 1 kcal mol-1)"

**Maturity claimed.** "For example, in our own internal group research, El Agente Quntur is already being employed to study highly excited electronic states in atoms and to analyze exceptions to Hund's rules at several levels of theory."

## arxiv:2604.18233

https://arxiv.org/html/2604.18233 — full text read from arXiv HTML and verified against the PDF

**What was built.** "In this paper, we present Aether, a novel approach that integrates Generative Agentic AI with a multi-functional Network Digital Twin to automate and streamline network change validation workflows."

**What it can call.** "It supports model-based verification (Batfish [17]) and simulation-based tools (Routenet [20]), with emulation support planned."

**How it was evaluated.** "Our benchmark dataset includes 8 network change scenarios (Table IV) spanning a range of operational tasks (router maintenance, policy updates, topology migrations) and complex failure modes (protocol logic errors, cross-layer interactions, latent path defects)."

**What it achieved.** "achieving 94% Error Detection and 64% Precision in synthetic benchmarks, and 100% detection with 73% Precision in production environments."

**Maturity claimed.** "Aether demonstrates practical value for autonomous network operations, serving as an intelligent assistant for routine validation while operators focus on strategic decisions."

## doi:10.1039/d6dd00060f

https://pmc.ncbi.nlm.nih.gov/articles/PMC13251679/ — the RSC route returned HTTP 403; full text read from the PubMed Central mirror

**What was built.** "an LLM-assisted data pipeline that converts real-world, natural language text descriptions of chemical production into, first, machine-readable PFD-level flowsheet graphs and, second, converged simulations in commercial flowsheeting software."

**What it can call.** "The resulting digitized flowsheets are automatically translated into converged Aspen Plus simulations by augmenting missing information with black-box optimization."

**How it was evaluated.** "we have hand-collected a total of 101 expert-drawn flowsheets for 30 chemical production processes, enabling us to assess flowsheet similarity across expert interpretations."

**What it achieved.** "For most processes, the median similarity of LLM-generated flowsheets to expert flowsheets lies within the distribution of pairwise expert similarities."

**Maturity claimed.** "For the first time, we demonstrate that an automated pipeline can achieve expert-level accuracy in process topology digitization."

## doi:10.2139/ssrn.6074109

https://arxiv.org/pdf/2601.07252 — no arXiv HTML rendering exists at any version; the 26-page PDF was fetched and read in full. The abstract alone omits the base models, the baseline, the error-correction mechanism and the 20-iteration cap

**What was built.** "This paper introduces a new multi-agent simulation framework, SwarmFoam. SwarmFoam integrates functionalities such as Multi-modal perception, Intelligent error correction, and Retrieval-Augmented Generation, aiming to achieve more complex simulations through dual parsing of images and high-level instructions."

**What it can call.** "(4) Runner Agent: Executes simulation commands and captures potential error messages."

**How it was evaluated.** "As shown in Table 3, 25 independent test cases were established to evaluate the simulation performance and image parsing capabilities of SwarmFoam."

**What it achieved.** "The overall pass rate for the cases was 84% (using Gemini-2.5-flash). Among these, the pass rate for natural language input cases was 80% (Gemini-2.5-flash), while the pass rate for multimodal input cases was 86.67% (Gemini-2.5-flash)."

**Maturity claimed.** "The multi-agent framework for CFD based on multi-type LLMs (SwarmFoam) can effectively capture case image information and accurately understand users' simulation requirements, successfully realizing intelligent CFD proxy."

## arxiv:2607.05134

https://arxiv.org/html/2607.05134 — full text read from arXiv HTML

**What was built.** "We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines."

**What it can call.** "The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element backend, and stores the solutions as operator-ready tensors."

**How it was evaluated.** "We evaluate the input-handling workflow on 70 scripted ODE/PDE scenarios from the validation runners: 15 ODE, 30 PDE (1D) and 25 PDE (2D) cases."

**What it achieved.** "The complete system achieves the highest aggregate accuracy at 81.43%."

**Maturity claimed.** "The framework is designed for repeatable scientific and engineering workflows where many related physics configurations must be specified, simulated, learned, and queried with minimal manual intervention."

## arxiv:2605.14154

https://arxiv.org/html/2605.14154 — full text read from arXiv HTML

**What was built.** "TSAgent, an agentic workflow that automates TS search directly at the density functional theory (DFT) level of quantum chemical accuracy."

**What it can call.** "DFT calculations are performed with VASP 6.3."

**How it was evaluated.** "We evaluate TSAgent on a diverse 100-example subset of the OC20NEB heterogeneous catalysis benchmark"

**What it achieved.** "TSAgent achieves an overall success rate of 83% on the benchmark (95% CI via Wilson score: 74.5-89.1%)"

**Maturity claimed.** "TSAgent independently reproduces Bronsted-Evans-Polanyi scaling relationships for NH3 dissociation on metal and single-atom alloy surfaces from a published heterogeneous catalysis study, demonstrating that its utility extends beyond curated benchmarks to real scientific investigations."

## doi:10.48550/arxiv.2511.00122

https://arxiv.org/html/2511.00122 — full text read from arXiv HTML

**What was built.** "Engineering.ai, a platform for teams of AI engineers that addresses these challenges through comprehensive integration across multiple engineering domains."

**What it can call.** "The system integrates FreeCAD, Gmsh, OpenFOAM, CalculiX, and Python-based Brooks-Pope-Marcolini (BPM) acoustic analysis."

**How it was evaluated.** "The framework is validated through UAV wing optimization, where agents autonomously evaluated four NACA airfoils across Reynolds numbers ranging from 10^5 to 10^6."

**What it achieved.** "The automated workflow achieved a 100% success rate across over 400 parametric configurations, with zero mesh generation failures."

**Maturity claimed.** "This work demonstrates that agentic-AI-enabled AI engineers have the potential to perform complex engineering tasks autonomously."

## doi:10.48550/arxiv.2507.14267

https://arxiv.org/html/2507.14267 — full text read from arXiv HTML (v2)

**What was built.** "We introduce the DFT-based Research Engine for Agentic Materials Simulation (DREAMS), a hierarchical multi-agent framework for density functional theory (DFT) built around a multi-tier safety guard."

**What it can call.** "Structure generation uses AutoCat autocat to identify adsorption sites and ASE ase-paper to represent structures and prepare Quantum ESPRESSO inputs."

**How it was evaluated.** "We evaluate DREAMS on three periodic DFT benchmarks... DREAMS calculates lattice constants for the 27 elemental crystals in the Sol27LC dataset beef, spanning multiple crystal structures, with accuracy comparable to expert calculations."

**What it achieved.** "DREAMS achieves average errors below 1% on the Sol27LC lattice-constant benchmark."

**Maturity claimed.** "DREAMS operates at an enhanced L2 (L2+) automation level and demonstrates capabilities approaching L3 automation, providing a path toward trustworthy, high-throughput autonomous materials simulation."

## doi:10.1063/5.0294696

https://arxiv.org/html/2507.23693 — full text read from the arXiv preprint; the AIP version of record was not attempted because AIP is a known blocked host

**What was built.** "CFDagent, a zero-shot, multi-agent system that enables fully autonomous computational fluid dynamics (CFD) simulations from natural language prompts."

**What it can call.** "CFDagent integrates three specialized LLM-driven agents...the Solver Agent that configures and executes an immersed boundary flow solver."

**How it was evaluated.** "We validate CFDagent by reproducing canonical sphere flows at Reynolds numbers of 100 and 300 using three distinct inputs: a simple text prompt (i.e., 'sphere'), an image-based input, and a standard sphere model."

**What it achieved.** "The computed drag and lift coefficients from meshes produced by each input approach closely match available data."

**Maturity claimed.** "Through extensive tests on canonical and realistic scenarios, we demonstrate the robustness, versatility, and practical applicability of CFDagent."

## arxiv:2605.23273

https://arxiv.org/html/2605.23273 — full text read from arXiv HTML

**What was built.** "TopOptAgents, a multi-agent framework designed for autonomous topology optimization."

**What it can call.** "FEniCS library...for finite element analysis" and "pyOptSparse [Wu et al. [2020]] with SNOPT as the optimizer"

**How it was evaluated.** "Three benchmark topology optimization problems are considered herein: compliance minimization for a cantilever beam, compliance minimization for an MBB beam...and stress minimization for an L-shaped beam...evaluated over 10 independent sessions for each problem."

**What it achieved.** "The improvement from 10% to 80% on the L-shaped problem shows where the framework provides the largest gain."

**Maturity claimed.** "In such cases, the proposed framework reliably produces converged designs where a single state-of-the-art LLM struggles."

## doi:10.48550/arxiv.2512.06404

https://arxiv.org/html/2512.06404 — full text read from arXiv HTML

**What was built.** "GENIUS, an AI-agentic workflow that fuses a smart Quantum ESPRESSO knowledge graph with a tiered hierarchy of large language models supervised by a finite-state error-recovery machine."

**What it can call.** "The framework acts as an intelligent interface to computational tools, specifically designed here for generating and automatically debugging simulation protocols based on Density Functional Theory (DFT), and to validate our approach, we choose the Quantum ESPRESSO (QE) program."

**How it was evaluated.** "We tested GENIUS with multiple LLMs to evaluate our approach, each exhibiting incremental capabilities, to obtain more comprehensive diagnostic insights into the workflow's performance."

**What it achieved.** "GENIUS translates free-form human-generated prompts into validated input files that run to completion on ~80% of 295 diverse benchmarks, where 76% are autonomously repaired."

**Maturity claimed.** "By allowing researchers to focus on scientific questions rather than technical implementation, GENIUS delivers incremental efficiency gains while enabling a fundamental shift in how-and by whom-materials discovery can be conducted."

## doi:10.48550/arxiv.2512.13930

https://arxiv.org/html/2512.13930 — full text read from arXiv HTML

**What was built.** "We introduce Materials Agents for Simulation and Theory in Electronic-structure Reasoning (MASTER), an active learning framework where large language models autonomously design, execute, and interpret atomistic simulations."

**What it can call.** "This prompt is passed to Codex (version 0.57.0) via command-line interface as a subprocess, which returns a Python script using ASE library functions."

**How it was evaluated.** "All reasoning strategies were benchmarked within the above-mentioned transition-metal chemical space, enabling a controlled proof-of-principle testbed for autonomous discovery."

**What it achieved.** "Across two chemical applications, CO adsorption on Cu-surface transition metal (M) adatoms and on M-N-C catalysts, reasoning-driven exploration reduces required atomistic simulations by up to 90% relative to trial-and-error selection."

**Maturity claimed.** "Altogether, multi-agent collaboration accelerates materials discovery and marks a new paradigm for autonomous scientific exploration."

## doi:10.48550/arxiv.2605.24002

https://arxiv.org/html/2605.24002 — full text read from arXiv HTML

**What was built.** "AtomisticSkills, an open-source harness framework that empowers general-purpose AI coding agents to conduct atomistic research."

**What it can call.** "The framework integrates more than 100 human-curated multidisciplinary skills, including database access, thermodynamics and kinetics modeling, and diverse simulation engines employing machine learning interatomic potentials (MLIPs) and density functional theory (DFT)."

**How it was evaluated.** "We validate its functional coverage against scientific literature and demonstrate robust orchestration capabilities across diverse scientific campaigns."

**What it achieved.** "on average, AtomisticSkills covers 56.2% of computational materials skills usage."

**Maturity claimed.** "AtomisticSkills provides a critical agent infrastructure towards building fully autonomous AI scientists."

## arxiv:2605.26179

https://arxiv.org/html/2605.26179 — full text read from arXiv HTML

**What was built.** "Here, we introduce AutoDFT, a closed-loop multi-agent framework that embeds LLM reasoning into every stage of the DFT lifecycle"

**What it can call.** "AutoDFT, a closed-loop seven-agent framework built on top of VASP"

**How it was evaluated.** "We evaluate AutoDFT along three axes: (i) end-to-end task success on a benchmark of realistic VASP workflows, (ii) physical correctness of the properties extracted from successful runs, and (iii) the sources of improvement provided by closed-loop execution."

**What it achieved.** "With GPT-5.2, AutoDFT-Full solves 32 of 34 tasks, achieving the highest overall success rate of 94.1%, compared with 82.4% for AutoDFT-OpenLoop and 67.6% for Rule-Based."

**Maturity claimed.** "By closing the loop between planning and execution, AutoDFT enables experimentalists without deep computational expertise to obtain reliable first-principles results."

## doi:10.48550/arxiv.2509.10210

https://arxiv.org/html/2509.10210 — full text read from arXiv HTML

**What was built.** "We present a multi-agent system for literature-informed force field extraction and automated RASPA simulation setup."

**What it can call.** "Agents have access to general tools for file manipulation, while relevant agents also use functions to extract information from files without opening them directly."

**How it was evaluated.** "Each simulation setup is performed five times, and the resulting files are evaluated both manually and by executing them in RASPA to verify correctness and reproducibility."

**What it achieved.** "The system performed well in the experiment setup task (Table 2), with a high rate of successful and executable simulations"

**Maturity claimed.** "Initial evaluations demonstrate high correctness and reproducibility, highlighting this approach's potential to enable fully autonomous, scalable materials characterization."

## doi:10.1109/ipdps65963.2026.00114

https://arxiv.org/html/2505.05428v3 — IEEE Xplore not attempted; full text read from the arXiv version at v3

**What was built.** "Academy, a modular and extensible middleware designed to deploy autonomous agents across the federated research ecosystem, including HPC systems, experimental facilities, and data repositories."

**What it can call.** "The validation stage of the pipeline uses the LAMMPS GPU library to assess MOF stability (strain)."

**How it was evaluated.** "We measured weak scaling performance from two aspects: agent startup and action completion time using the hybrid exchange with the object store located on the head node."

**What it achieved.** "Academy starts 3,328 actors in 7.6 seconds and achieves 3.4K actions/second maximum throughput on a single agent."

**Maturity claimed.** "This framework enables scalable and flexible orchestration of intelligent agents across heterogeneous resources."

## doi:10.48550/arxiv.2608.15881

https://arxiv.org/html/2608.15881 — full text read from arXiv HTML (v1)

**What was built.** "MOOSEnger, developed at Idaho National Laboratory (INL), is a domain-specific, tool-enabled AI agent built for the MOOSE Framework."

**What it can call.** "the agent retrieves relevant MOOSE documentation and examples, drafts or edits input files, and calls MOOSE-aware tools to check, and run the resulting simulations."

**How it was evaluated.** "The benchmark prompts are organized into physics-oriented categories including diffusion, Navier-Stokes, phase field, plasticity, porous media flow, solid mechanics, transient heat transfer, and reactor mesh generation."

**What it achieved.** "Within the MOOSEnger harness, GPT 5.2 resolves 179 of 200 prompts (90%), compared to 153 of 200 (76.5%) for the locally-hosted Gemma 4 31b."

**Maturity claimed.** "moving toward fully capable, locally-hosted agents for MOOSE-based multiphysics modeling."

## doi:10.1145/3770855.3818856

https://arxiv.org/html/2605.29560v1 — the ACM route returned HTTP 403; full text read from the arXiv preprint of the same KDD 2026 paper, with the code repository confirming identity

**What was built.** "Battery-Sim-Agent, the first framework to deploy a Large Language Model (LLM) agent in a closed loop with a high-fidelity battery simulator."

**What it can call.** "We construct a diverse benchmark suite using the high-fidelity Doyle-Fuller-Newman (DFN) model in PyBaMM."

**How it was evaluated.** "From the valid cases (233 for Extreme Mode, 373 for Regular Mode), we randomly select 100 tasks per mode to form the final suite of 200 tasks."

**What it achieved.** "67-95% reduction in curve-matching error compared to traditional black-box optimization baselines."

**Maturity claimed.** "Our results highlight the promise of LLM-agents as reasoning-based optimizers for scientific discovery and battery parameter estimation."

## doi:10.48550/arxiv.2604.22571

https://arxiv.org/html/2604.22571 — full text read from arXiv HTML

**What was built.** "LARA-HPC, a validation-driven agentic framework to enable reliable workflow generation for atomistic modeling on HPC systems."

**What it can call.** "applying LARA-HPC to orchestrate DFT based simulations with the BigDFT program"

**How it was evaluated.** "demonstrating an end-to-end atomistic simulation workflow on HPC by applying LARA-HPC to Density Functional Theory simulations"

**What it achieved.** "This gives ~1.2 GB of headroom per process on the worst-case calculation (slab+water)."

**Maturity claimed.** "validation-driven generation significantly improves robustness and enables iterative correction of both syntactic and physical inconsistencies"

## doi:10.48550/arxiv.2604.11945

https://arxiv.org/html/2604.11945 — full text read from arXiv HTML

**What was built.** "AutoSurrogate, an LLM-driven multi-agent framework designed to autonomously construct, train, and deploy deep learning surrogate models for subsurface flow modeling."

**What it can call.** "The simulation of this case is implemented through the open-source multiphysics simulator, GEOS, which is designed for modeling geologic carbon storage processes."

**How it was evaluated.** "Each sample takes the static 3D permeability field of the storage aquifer with dimension 80x80x20 as input and produces pressure and CO2 saturation fields over 31 timesteps (including initial state) as output."

**What it achieved.** "AutoSurrogate@3 further improves to R2=0.9976, surpassing all baselines"

**Maturity claimed.** "AutoSurrogate is able to outperform expert-designed baselines and domain-agnostic AutoML methods, demonstrating strong potential for practical deployment."

## arxiv:2607.11084

https://arxiv.org/html/2607.11084 — full text read from arXiv HTML

**What was built.** "NAIS, a governed end-to-end agentic research system designed to support scientific workflows in institutionally constrained environments."

**What it can call.** "orchestrated: (1) SQL cohort extraction via the broker's SQL extraction pipeline, (2) phenotype tab-separated values (TSV) generation with fields including individual ID, hypertension label, systolic blood pressure (SBP) and diastolic blood pressure (DBP), (3) GWAS submission via the broker's GWAS pipeline with PLINK2 logistic regression"

**How it was evaluated.** "Systematic comparison with independently curated expert analyses showed that human-AI review identified phenotype discrepancies and enabled iterative refinement of the hypertension definition."

**What it achieved.** "the agent-orchestrated GWAS reproduced established hypertension-associated loci, including FGF5, ATP2B1, CNNM2, FTO, and GRB14, with the strongest signal at FGF5 reaching -log10 p ~ 70"

**Maturity claimed.** "These results demonstrate that governed agentic research systems can support scalable AI-assisted biomedical discovery while producing scientifically reliable outputs comparable to expert-led workflows."

## arxiv:2604.02688

https://arxiv.org/html/2604.02688 — full text read from arXiv HTML

**What was built.** "MatClaw, a _code-first_ agent that writes and executes Python directly, composing any installed domain library to orchestrate multi-code workflows on remote HPC clusters"

**What it can call.** "These libraries in turn submit jobs to materials computation backends (VASP, DeePMD-kit, LAMMPS, phonopy, etc.)"

**How it was evaluated.** "We evaluate RAG effectiveness using three multiple-choice QA benchmark suites spanning a spectrum of library popularity"

**What it achieved.** "retrieval-augmented generation over domain source code that raises per-step API-call accuracy to ~99%"

**Maturity claimed.** "LLMs already handle code generation and scientific interpretation reliably, and the rapid improvement in their capabilities will accelerate materials discovery"

## arxiv:2606.18425

https://arxiv.org/html/2606.18425 — full text read from arXiv HTML

**What was built.** "An LLM agent, grounded in a released plugin of Pegasus-specific skills, first produces a reviewable specification of checkable constraints and acceptance criteria, then generates the executable workflow."

**What it can call.** "_Pegasus_ plans and orchestrates the workflow and _HTCondor_ executes its jobs."

**How it was evaluated.** "Experiments ran on a distributed HTCondor pool on the FABRIC testbed with four GPU-equipped worker nodes across sites, HAWI (3 GPUs), MAX-1 (2), MAX-2 (2), and NCSA (2), totaling 9 GPUs."

**What it achieved.** "The fifty round experiments consist of 101 sub-workflows, 50 rounds across two datasets plus the top level, and generate over 2,000 jobs each."

**Maturity claimed.** "Production-ready means the generated workflow executed end to end on the pool of Section IV."

## arxiv:2512.23010

https://arxiv.org/pdf/2512.23010v2 — no arXiv HTML rendering exists at any version and ar5iv redirects to the abstract; the 47-page PDF was fetched and converted with pdftotext

**What was built.** "Here, we introduce Masgent, an AI-assisted materials simulation agent that unifies structure manipulation, automated VASP input generation, DFT workflow construction and analysis, fast MLP-based simulations, and lightweight machine learning (ML) utilities within a single platform."

**What it can call.** "The LLM backend identifies the intended operation, such as structure generation, defect creation, VASP input preparation, workflow construction, MLP evaluation, or results analysis, and maps it to a specific tool."

**How it was evaluated.** "We benchmarked Masgent's workflow preparation speed by measuring the time required to set up standard DFT simulations for a representative set of materials."

**What it achieved.** "Masgent prepared full workflows for each system in under 30 seconds, representing a dramatic improvement compared to manual scripting approaches, which typically require 1-3 hours per material depending on workflow complexity."

**Maturity claimed.** "Looking ahead, Masgent provides a robust foundation for incorporating active learning, autonomous optimization loops, expanded workflow coverage, and deeper integration with HPC workflow managers, positioning it as a next-generation computational assistant capable of accelerating both exploratory and production-level materials simulations."

## doi:10.1016/j.taml.2025.100623

https://arxiv.org/html/2504.02888 — Elsevier returned a stub, ScienceDirect HTTP 403 and the CSTAM mirror had an expired TLS certificate; full text read from the arXiv preprint of the same study, whose title differs slightly

**What was built.** "our recent work introduced OpenFOAMGPT, an LLM-based agent for OpenFOAM-centric CFD simulations"

**What it can call.** "OpenFOAM runner then executes the simulation with the setup files"

**How it was evaluated.** "Both scenarios were evaluated under zero-shot prompting and retrieval-augmented generation (RAG) conditions"

**What it achieved.** "achieving cost savings of up to two orders of magnitude compared to OpenAI o1"

**Maturity claimed.** "the framework adeptly handles a range of flow configurations (including single- and multi-phase flow) in just a few iterations"

## doi:10.48550/arxiv.2602.00185

https://arxiv.org/html/2602.00185 — full text read from arXiv HTML

**What was built.** "we introduce QUASAR, a universal autonomous system for atomistic simulation designed to facilitate production-grade scientific discovery."

**What it can call.** "QUASAR autonomously orchestrates complex multi-scale workflows across diverse methods, including density functional theory, machine learning potentials, molecular dynamics, and Monte Carlo simulations."

**How it was evaluated.** "We evaluated QUASAR using a three-tiered benchmark suite (Table 2) with the gemini-3-flashpreview LLM."

**What it achieved.** "Calculate the adsorption isotherm for CO2 in UiO-66 at 298 K. n10 bar=5.98 mmol/g"

**Maturity claimed.** "QUASAR, a production-level universal atomistic computation system designed to overcome these limitations"

## doi:10.48550/arxiv.2602.17886

https://arxiv.org/html/2602.17886 — full text read from arXiv HTML

**What was built.** "a hierarchical multi-agent framework for automating solid-state quantum chemistry workflows using the open-source Quantum ESPRESSO"

**What it can call.** "El Agente Solido can autonomously query external materials databases, generate and manipulate atomic structures...and select appropriate computational and physical parameters for each task."

**How it was evaluated.** "For each benchmarking exercise, we formulated two versions of the same question with varying difficulty levels (Level 1 and Level 2), each repeated five times (ten trials in total)."

**What it achieved.** "El Agente Solido achieved an average score of 97.9% based on rubrics designed by computational chemists"

**Maturity claimed.** "El Agente Solido exemplifies a rapid shift toward agentic computational chemistry...substantially accelerate materials discovery and design."

## doi:10.48550/arxiv.2504.08621

https://arxiv.org/html/2504.08621 — full text read from arXiv HTML

**What was built.** "MooseAgent, an automated system for the Moose multiphysics simulation framework that addresses these challenges."

**What it can call.** "automatically generate Moose input files and execute calculations"

**How it was evaluated.** "we conducted experiments using nine distinct test cases, each repeated five times. Performance was measured by success rate and token consumption."

**What it achieved.** "achieving an average success rate of 93%"

**Maturity claimed.** "MooseAgent can largely automate the simulation process" and "lays the technical foundation for developing more advanced fuel or reactor design intelligent agents"

## doi:10.1038/s41598-025-92337-6

https://www.nature.com/articles/s41598-025-92337-6?error=cookies_not_supported — PubMed Central returned a reCAPTCHA interstitial; full text obtained by following the Nature identity-provider chain

**What was built.** "Molecular Dynamics Agent (MDAgent), a framework designed to guide large models in automatically generating, executing, and refining simulation code."

**What it can call.** "Workers, specialized for domain-specific software such as LAMMPS, generate corresponding simulation scripts."

**How it was evaluated.** "Participants were tasked with defining MD simulations using natural language, and their interactions with the agent were monitored"

**What it achieved.** "Reduces the average task time by 42.22%, as compared to traditional models."

**Maturity claimed.** "MDAgent can effectively assist experts in semi-automating domain-specific tasks, serving as a valuable support tool."

## doi:10.48550/arxiv.2504.06260

https://arxiv.org/html/2504.06260 — full text read from arXiv HTML

**What was built.** "We present FEABench, a benchmark to evaluate the ability of large language models (LLMs) and LLM agents to simulate and solve physics, mathematics and engineering problems using finite element analysis (FEA)."

**What it can call.** "The LLM agent is expected to return a solution that should consist of the API calls that solve the problem, similar to Ground Truth Code"

**How it was evaluated.** "We benchmark different SOTA LLMs on their baseline (single-turn) performance with these metrics."

**What it achieved.** "Our best performing strategy generates executable API calls 88% of the time."

**Maturity claimed.** "LLMs that can successfully interact with and operate FEA software to solve problems such as those in our benchmark would push the frontiers of automation in engineering."

## doi:10.48550/arxiv.2603.03372

https://arxiv.org/html/2603.03372 — full text read from arXiv HTML

**What was built.** "a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design"

**What it can call.** "integrates Quantum Espresso (v7.4) with a unified API interface for accessing diverse commercial LLMs"

**How it was evaluated.** "DFTBench comprises 73 unique crystalline materials, exhibiting diversity in two aspects."

**What it achieved.** "TritonDFT delivers a >10x acceleration over manual expert execution"

**Maturity claimed.** "TritonDFT provides an open user interface for real-world usage"

## doi:10.48550/arxiv.2506.05616

https://arxiv.org/html/2506.05616 — full text read from arXiv HTML (v3)

**What was built.** "To this end, we propose Materials Agent unifying Planning, Physics, and Scientists, known as MAPPS. MAPPS consists of a Workflow Planner, a Tool Code Generator, and a Scientific Mediator."

**What it can call.** "This input context is passed to the Tool Code Generator, along with a collection of physics tools (e.g., CHGNetCalculator, pymatgen, ASE), which represent the available modeling and simulation environments."

**How it was evaluated.** "In this section, we evaluate MAPPS on a diverse range of real-world material discovery tasks, including crystal structure generation, crystal structure prediction, and discovering crystal structures with desired properties."

**What it achieved.** "On the MP-20 dataset, our method attains a match rate of 63.9% and an RMSE of 0.022, outperforming all baselines."

**Maturity claimed.** "We provide extensive experiments across diverse tasks to show that MAPPS is a promising framework for autonomous materials discovery."

## doi:10.48550/arxiv.2607.15001

https://arxiv.org/html/2607.15001 — full text read from arXiv HTML

**What was built.** "Here we present LQCDMaster, a tool-augmented, skill-guided and domain-specialized scientific computing agent that converts natural-language LQCD research tasks into executable PyQUDA computing workflows, including measurement scripts, job-submission artifacts, execution logs and numerical outputs."

**What it can call.** "The executor generates code according to the approved plan, producing PyQUDA and SLURM submission scripts."

**How it was evaluated.** "The benchmark suite consisted of 70 independent tasks on the C24P29 ensemble generated by the CLQCD collaboration [18, 19], with lattice spacing a=0.105 fm and lattice volume 24^3 x 72."

**What it achieved.** "The generated workflows exactly reproduce expert-written implementations in 63 of 70 tasks at machine precision, with three additional discrepancies attributable to convention mismatches."

**Maturity claimed.** "This work pioneers the paradigm of agentic scientific computing by automating the end-to-end scientific computing workflows in lattice QCD research, lowering its barrier and facilitating the exploration and verification of non-standard scientific ideas."

## doi:10.48550/arxiv.2601.20996

https://arxiv.org/html/2601.20996 — full text read from arXiv HTML (v2)

**What was built.** "We introduce MAterials Discovery Environments (MADE), a novel framework for benchmarking end-to-end autonomous materials discovery pipelines."

**What it can call.** "The orchestrator can invoke the following tools: generate_structures ... create_structure ... score_buffer ... list_compositions ... query_structures ... get_buffer_stats ... select_for_evaluation"

**How it was evaluated.** "We evaluate discovery performance across multiple chemical systems and random seeds. For each system, we run 5 independent discovery episodes with an oracle query budget of 50."

**What it achieved.** "The fully agentic LLM orchestrator achieves discovery efficiency comparable to the strongest modular pipelines, with significantly improved enhancement factor (EF = 6.0) and competitive AUDC and mSUN (Table 1)."

**Maturity claimed.** "By enabling controlled evaluation of these behaviors in closed-loop environments, MADE can help ground progress toward autonomous scientific discovery systems."

## doi:10.48550/arxiv.2601.09749

https://arxiv.org/html/2601.09749 — full text read from arXiv HTML

**What was built.** "In this paper, we propose R-LAM, a reproducibility-constrained framework for applying Large Action Models to scientific workflow automation."

**What it can call.** "Deterministic execution is enforced through explicit control of execution order, environment binding, and randomness sources. All external tool invocations are mediated by adapter layers that normalize inputs and outputs and restrict side effects."

**How it was evaluated.** "The workflow is executed under three conditions: (1) a deterministic script-based pipeline with no LAM involvement, (2) a naive LAM-driven pipeline where an LLM planner selects actions without reproducibility constraints, and (3) a LAM + R-LAM pipeline where the same planner operates under the reproducibility-constrained execution framework."

**What it achieved.** "The R-LAM pipeline executed the same 5 actions with complete trace capture (5/5 = 1.0), each action record containing 8+ metadata fields including timestamps, environment hashes, and dependency links."

**Maturity claimed.** "More broadly, we argue that reproducibility constraints are essential design requirements, not optional features, for deploying Large Action Models in any domain where execution correctness, auditability, and independent verification are paramount."

## doi:10.1038/s44172-025-00583-3

https://www.nature.com/articles/s44172-025-00583-3_reference.pdf — the accepted unedited article-in-press PDF was fetched directly from nature.com and converted with pdftotext

**What was built.** "Here we established a reasoning agent consisting of a large language model (LLM) and an extensive tool set to automate learning material collection, process simulation, optimization and carbon emission accounting of a representative methanol and ethanol distillation case study."

**What it can call.** "A reasoning agent was firstly established by combining a LLM, Grok 3, and several tools, including Aspen Plus, augmented-retrieval generation (RAG) and so on, as shown in Fig. 1a."

**How it was evaluated.** "With the prompts of natural language commands, the agent can autonomously execute process simulation, optimization, carbon accounting and result visualization, with all results rigorously validated by the authors to ensure reliability."

**What it achieved.** "Combining the heat pump-assisted process and renewables could substantially reduce the carbon emission by 98% compared with the coal-based traditional distillation process."

**Maturity claimed.** "The developed agent served as a prototype that successfully integrated reasoning with the Reasoning-Acting framework, with its current efficacy being shaped by both prompts and selection of LLMs."

## doi:10.69997/pse.120458

https://psecommunity.org/wp-content/plugins/wpor/includes/file/2607/LAPSE-2026.1218-1v1.pdf — the full record is a two-page FOPAM 2026 extended abstract of about 450 words of body text; there are no methods, evaluation or limitations sections to read, and the underlying method is in a ChemRxiv preprint on a blocked host

**What was built.** "Here, we present an automated workflow which gathers process knowledge, generates process simulations, and evaluates process performance."

**What it can call.** "The digitized flowsheet graphs are systemically translated into simulations within an established commercial process simulator."

**How it was evaluated.** "We show that our integrated pipelines can faithfully collect and digitize chemical process information by comparing to expert-curated datasets and manually drawn flowsheets."

**What it achieved.** "Furthermore, the generated process simulations are on par with expert interpretations with significantly less manual effort."

**Maturity claimed.** "We present case studies illustrating how the results of the automatically generated process simulations can be used to assess process sustainability and derive optimization potential."

## doi:10.48550/arxiv.2408.15866

https://arxiv.org/html/2408.15866 — full text read from arXiv HTML

**What was built.** "In this work, we introduce a novel autonomous agent framework leveraging Retrieval-Augmented Instruction-Tuning (RAIT) to enhance open, customizable small code language models (SLMs) for these calculations."

**What it can call.** "Such tools include APIs like Stack Overflow and Wolfram Alpha, as well as scholarly sources such as code documentation."

**How it was evaluated.** "We utilized custom-built MathComp and ChemProc datasets essential for building and evaluating a robust framework capable of handling real-world complex chemical and process engineering problems. These benchmark datasets were split into 70% training, 15% validation, and 15% test sets."

**What it achieved.** "The experimental results indicate that the proposed framework is effective; however, it lags slightly behind the proprietary models."

**Maturity claimed.** "Experimental results show that our framework matches the performance of large-scale proprietary models on benchmark datasets, proving its effectiveness and usability."

## doi:10.1016/j.ijheatfluidflow.2026.110399

https://arxiv.org/html/2504.19338 — the Elsevier version of record was not attempted as a known blocked host; full text read from the arXiv preprint with the same title and author list. IDENTITY MATCH IS INFERRED **v0.2: the Elsevier version of record was read from the local PDF store (`1-s2.0-S0142727X26001657-main.pdf`). Every quote in this block was checked against it and none differed, so the inferred identity match is now verified.**

**What was built.** "We propose the first multi-agent framework for computational fluid dynamics that enables fully automated, end-to-end simulations directly from natural-language queries."

**What it can call.** "The execution environment utilizes the OpenFOAM v2406 Docker container, providing a standardized, reproducible runtime environment independent of the host system configuration. This module automatically executes the \"Allrun\" script generated in the previous step, monitors the simulation progress, and captures all console output and log files for potential error analysis."

**How it was evaluated.** "In this section, we present a comprehensive evaluation of the proposed multi-agent, end-to-end workflow through five representative case studies that span a diverse range of CFD applications"

**What it achieved.** "Extensive validation through diverse case studies, including Poiseuille flows, single- and multi-phase porous media flows, and aerodynamic analyses, demonstrates 100% success and reproducibility rates across over 450 simulations."

**Maturity claimed.** "Rigorous trustworthiness verification confirms that properly designed multi-agent systems can achieve the reliability standards necessary for zero-tolerance scientific computing applications while significantly lowering entry barriers."

## doi:10.20944/preprints202608.1323.v1

https://r.jina.ai/https://www.preprints.org/manuscript/202608.1323/v1 — full text read through the r.jina.ai reader proxy; direct Preprints.org fetches returned HTTP 403

**What was built.** "We report early experiences using OpenAI's Codex and Anthropic's Claude Code as AI assistants for molecular simulation workflow development on OLCF resources."

**What it can call.** "We used the MACE program and the MACE-OFF23 potential as the primary framework for MLIP training and development [5,13,14], and its coupling with the LAMMPS and OpenMM HPC-based MD engines as representative simulation backends [15,16,17], deployed on Frontier, an HPE Cray EX system with AMD GPUs, and Wombat, an AArch64 Arm and NVIDIA testbed."

**How it was evaluated.** "Our observations support the idea that coding agents increase productivity for installation, testing, deployment, and management of HPC molecular simulation workflows. The results are early experience, not a controlled productivity benchmark, and the systems results are platform-specific."

**What it achieved.** "Codex enabled a substantial speedup in the time it takes to connect theory revisions to executable numerical tests; in some cases, the speedups could be estimated as over 1,000x."

**Maturity claimed.** "Under expert supervision and with file-based provenance, AI coding systems could reduce the translation cost between scientific intent and machine-specific execution, as long as scientific truth can be codified and agentic workflows can be verified with auditable artifacts."

## doi:10.1016/j.taml.2025.100594

https://arxiv.org/html/2504.09602v1 — the Elsevier version of record returned only a redirect interstitial, so the full text was read from the arXiv preprint 2504.09602v1 with the same title, authors and system description. IDENTITY MATCH IS INFERRED, not verified **v0.2: the Elsevier version of record was read from the local PDF store (`1-s2.0-S2095034925000261-main.pdf`). Every quote in this block was checked against it and none differed, so the inferred identity match is now verified.**

**What was built.** "We introduce a novel approach centered on domain-specific LLM adaptation. By fine-tuning Qwen2.5-7B-Instruct on NL2FOAM, our custom dataset of 28716 natural language-to-OpenFOAM configuration pairs with chain-of-thought (CoT) annotations, we enable direct translation from natural language descriptions to executable CFD setups."

**What it can call.** "As illustrated in Fig. 1, the system orchestrates four specialized agents-pre-checker, LLM generator, runner, and corrector-through a structured workflow that enforces OpenFOAM syntax compliance and numerical stability."

**How it was evaluated.** "We evaluate our framework using an incompressible flow benchmark of 21 cases (10 laminar, 11 turbulent) with [Re] spanning from [40] to [10^6], as listed in Tab. 2."

**What it achieved.** "Evaluation on a benchmark of 21 diverse flow cases demonstrates state-of-the-art performance, achieving 88.7% solution accuracy and 82.6% first-attempt success rate."

**Maturity claimed.** "This research introduces a new paradigm for engineering automation that bridges natural language interfaces with specialized numerical simulations."

## doi:10.1016/j.taml.2026.100660

https://doi.org/10.1016/j.taml.2026.100660 - full text read from the local PDF store (`1-s2.0-S2095034926000085-main.pdf`, *Theoretical and Applied Mechanics Letters* 16 (2026) 100660, the version of record). **In v0.1 this record was read from arXiv:2503.01273v1 and the identity match was inferred; the published version rewords the framing and adds a quantitative pass@1 robustness result that v0.1 recorded as absent.**

**What was built.** "In this study, we introduce OptMetaOpenFOAM, an innovative framework that employs a large language model driven multiagent architecture to automate sensitivity analyses and parameter optimization tasks in CFD via natural language instructions." *(v0.1 quoted the preprint: "OptMetaOpenFOAM-a novel framework that bridges MetaOpenFOAM with external analysis and optimization tool libraries".)*

**What it can call.** "The integration of external analysis tools, such as the active subspace method and L-BFGS-B optimization algorithm, further enhances the framework's capacity to perform detailed sensitivity analysis and multivariable optimization." "MetaGPT v0.8.0 was chosen for the integration of different agents, while OpenFOAM 10 was employed for CFD simulations."

**How it was evaluated.** "The framework's efficacy is demonstrated through comprehensive testing across 11 distinct CFD tasks-including fluid flow, combustion, and heat transfer-originating from standard OpenFOAM tutorials and an external validation case involving hydrogen combustion chamber optimization." *(v0.1 quoted the preprint's "The test dataset comprises 11 distinct CFD analysis or optimization tasks, including a baseline simulation task derived from an OpenFOAM tutorial".)*

**What it achieved.** "Remarkably, concise natural language commands (~200 characters) successfully triggered elaborate computational sequences involving simulation setup, postprocessing, sensitivity analysis, and parameter optimization, translating into over 2,000 lines of automated code execution." "Notably, the successful validation using a non-OpenFOAM-tutorial hydrogen combustion chamber case demonstrated its efficiency in handling complex combustion dynamics and optimization tasks."

**A quantitative result the preprint did not carry.** Table 1, "pass@1 comparison between the original and modified datasets": "Dataset 1 ... 86.6", "Dataset 2 ... 85.0". "These results confirm that OptMetaOpenFOAM maintains nearly identical success rates when handling semantically equivalent but syntactically different inputs, demonstrating strong prompt-level generalization and robustness of the proposed language-driven CFD automation framework." *(v0.1 recorded the evaluation as "focused on result presentation rather than quantitative executability metrics"; that was true of the preprint and is not true of the version of record.)*

**Maturity claimed.** "These findings underline the transformative potential of LLM-driven frameworks in revolutionizing CFD simulation workflows, making them more accessible, efficient, and effective for both industrial and research applications." *(v0.1 quoted the preprint's "These findings underscore the transformative potential of LLM-driven COT methodologies in linking external tool for advanced analysis and optimization".)*

**Limitations, in the authors' terms.** There is no limitations section. The single bounded statement is on the fitted surface: "owing to these inherent bounds, the fitted response surface is not perfect." The authors also note "A preliminary robustness and generalization analysis was presented in our previous work", deferring that evidence to MetaOpenFOAM 2.0.

## doi:10.5281/zenodo.20543501

https://zenodo.org/api/records/20543501 — the Zenodo record is a software deposit with no accompanying manuscript; the v1.1.0 archive was downloaded and its README, agent instructions, stress-test log, end-to-end post-mortems and plan were read. All quotes are repository documentation, not a paper

**What was built.** "OASiS is a **Model Context Protocol (MCP) server** that connects AI coding agents to **eight independent finite element codes** (FEniCSx, deal.II, 4C Multiphysics, NGSolve, scikit-fem, Kratos Multiphysics, DUNE-fem, FEBio)."

**What it can call.** "Any MCP-compatible AI tool (Claude Code, Cursor, Windsurf, GitHub Copilot) can **operate** solvers, **couple** them across codes, **develop** new solver capabilities, and **verify** simulation correctness - all through one protocol."

**How it was evaluated.** "These benchmarks have been run as end-to-end stress tests with a fresh AI agent. Each prompt was given verbatim to the agent with no additional guidance."

**What it achieved.** "E2E stress tests | **24 completed** (24 pass)"

**Maturity claimed.** "A genuinely knowledgeable multi-solver interface that: 1. **Knows everything each code can do** ... 2. **Can operate any code** ... 3. **Can develop and extend codes** ... 4. **Can couple codes intelligently**"

## doi:10.5281/zenodo.19835550

https://zenodo.org/api/records/19835550 — the Zenodo record metadata was read and the deposited submission PDF fetched and converted with pdftotext

**What was built.** "M.A.R.V.I.N. (Materials Agentic Research, Validation, and Inference Navigation) addresses this gap by establishing the CALPHAD-derived Gibbs energy function as the universal currency of an integrated autonomous discovery loop."

**What it can call.** "M.A.R.V.I.N. integrates AI reasoning agents through Anthropic's Model Context Protocol (MCP), which provides a standardized interface for an LLM to invoke external tools-databases, simulations, instruments-via typed function contracts with input validation and safety predicates."

**How it was evaluated.** "Sections 2 and 7 present implemented computational results: the compound energy formalism sublattice model for garnet LLZO, self-contained-SGTE-computed atmosphere diagrams, and the Nernst-Einstein conductivity estimates. Sections 3-6 describe designed architectural components that are not yet operational"

**What it achieved.** "a compound energy formalism sublattice model yields dopant-dependent vacancy concentrations that, when coupled to a Nernst-Einstein transport model, produce ionic conductivity estimates that match the experimental 0.87 mS cm-1 at x(Ta) = 0.125 of Allen et al. [52] by D0 calibration"

**Maturity claimed.** "By anchoring every autonomous decision to an assessed Gibbs energy function and logging all data with full provenance to FAIR standards within the design-make-test-analyse paradigm formalised by Tom et al. [7], M.A.R.V.I.N. provides generalizable, software-led architecture for reproducible materials discovery."

## doi:10.48550/arxiv.2509.20374

https://arxiv.org/html/2509.20374 — full text read from arXiv HTML (v3), including appendices

**What was built.** "We introduce CFDLLMBench, a benchmark suite comprising three complementary components: CFDQuery, CFDCodeBench, and FoamBench, designed to holistically evaluate LLM performance across three key competencies: graduate-level CFD knowledge, numerical and physical reasoning of CFD, and context-dependent implementation of CFD workflows."

**What it can call.** "This task requires an LLM to create the required OpenFOAM input files, save them in appropriate directories, and call different tools within OpenFOAM to run a physically accurate simulation, all based on a natural language prompt."

**How it was evaluated.** "On CFDQuery and CFDCodeBench, LLMs use a standard zero-shot prompt template that describes the task and the output format. For FoamBench, we evaluate LLMs zero-shot, as well as with agentic frameworks (described next). We use OpenFOAM v10 for all experiments."

**What it achieved.** "the best performing model achieves only 14% on CFDCodeBench and 34% on FoamBench."

**Maturity claimed.** "CFDLLMBench establishes a solid foundation for the development and evaluation of LLM-driven automation of numerical experiments for complex physical systems."

## doi:10.1002/aidi.202500174

https://arxiv.org/html/2506.02019 — the Wiley version of record was not attempted as a known blocked host; full text read from the arXiv version 2506.02019v3, whose abstract, 315-case benchmark, headline figures and author list match the journal record. IDENTITY MATCH IS INFERRED, not verified **v0.2: the Wiley version of record was read from the local PDF store. Every quote in this block was checked against it and none differed, so the inferred identity match is now verified.**

**What was built.** "This paper introduces ChatCFD, a LLM-driven agent system for end-to-end CFD automation. Powered by DeepSeek-R1/V3, a multi-agent architecture, structured OpenFOAM knowledge bases, precise error locator, and iterative reflection, ChatCFD dramatically outperforms prior systems."

**What it can call.** "ChatCFD is an automated CFD agent system that leverages the OpenFOAM framework to process multi-modal user inputs, including research articles and mesh files, to configure and execute CFD simulations based on user instructions."

**How it was evaluated.** "The performance of ChatCFD was rigorously evaluated through a series of validation experiments encompassing three distinct categories of CFD cases: (i) 205 benchmark tutorial cases drawn from OpenFOAM tutorials and the OpenFOAM wiki ... (ii) 110 perturbed variants ... and (iii) 2 advanced literature-derived cases"

**What it achieved.** "On 315 benchmark cases it attains 82.1% execution success (vs. 6.2% MetaOpenFOAM, 42.3% Foam-Agent) and, crucially, 68.12% physical fidelity-the first rigorous metric capturing whether a runnable simulation is scientifically meaningful."

**Maturity claimed.** "ChatCFD's modular, MCP-compatible design directly enables collaborative multi-agent networks and paves the way for scalable AI-driven CFD innovation."

## doi:10.48550/arxiv.2607.22596

https://arxiv.org/html/2607.22596 — full text read from arXiv HTML (v1), including appendices

**What was built.** "Here, we present an agent-based system embedded within the URSA (Universal Research and Scientific Agent) framework that automates the design, execution, and validation of atomistic simulations, demonstrated using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) tool."

**What it can call.** "In our work, we show that an entire MD workflow can be performed end-to-end, starting from selecting/downloading an interatomic potential to successfully executing LAMMPS, by a single agent."

**How it was evaluated.** "In this section, we demonstrate these features by benchmarking our agent against LAVA, a python toolkit for calculations with LAMMPS and the Vienna Ab initio Simulation Package (VASP). We choose aluminum (Al) as our benchmark problem and calculate material properties with the potential of Ref. 15."

**What it achieved.** "For all these quantities, we found that the agent was able to reproduce LAVA's calculation either via minimal prompting or using LAVA generated templates."

**Maturity claimed.** "With these contributions, we believe that our work significantly accelerates the adoption of agentic AI enabled workflows for the design and discovery of novel materials."

## arxiv:2604.24696

https://arxiv.org/html/2604.24696 — full text read from arXiv HTML (v3)

**What was built.** "To address this gap, we present NeuroClaw, a domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research."

**What it can call.** "It manages Python environments, Docker containers, GPU stacks, and neuroimaging toolchains such as FSL, FreeSurfer, and fMRIPrep so that users do not need to know which tool to invoke or how to configure the runtime across both medical-imaging and computational dependencies."

**How it was evaluated.** "NeuroBench is a system-level benchmark designed to evaluate whether an agent can complete realistic neuroimaging research tasks under practical constraints."

**What it achieved.** "Table 1 shows that all ten base models improve when run within the NeuroClaw framework, with an average absolute gain of 4.74 points."

**Maturity claimed.** "By offering a modular platform that can operate directly on raw data and standardized specifications, NeuroClaw enables neuroscience laboratories to move from fragile, irreproducible pipelines toward auditable, iterative experimental loops that more closely reflect scientific practice."

## arxiv:2606.05050

https://arxiv.org/html/2606.05050 — full text read from arXiv HTML (v2), re-extracted a second time preserving MathML alternative text to recover numeric values

**What was built.** "We present CatDT (Catalysis Digital Twin), a self-evolving multi-agent system that builds an autonomous digital twin of a working catalyst, unifying gas-solid and liquid-solid modeling."

**What it can call.** "Agent 7 (centre) coordinates eight specialized agents: Agent 1 (SurFF) for Wulff-shape prediction and facet ranking, Agent 2 (VSSR-MC ...) for condition-dependent surface modeling ..., Agent 3 (AdsorbDiff) for adsorption-site sampling, Agent M1 (UniMech) for multi-pathway enumeration and energy-guided pruning, Agent 4 (Geometry engine + Memento memory) for elementary-step endpoint design, Agent 5 (deterministic gates + energy screen) for validation, and Agent 6 (CatMAP / electrochemical kMC) for microkinetic modeling."

**How it was evaluated.** "To stress-test this design we selected seven gas-solid thermal catalysis benchmarks of increasing complexity, each adding one challenge the previous system did not require (Fig. 5)."

**What it achieved.** "The predicted propylene TOF at 550 C is 0.16 s-1, matching the experimental 0.13 s-1 within 25%."

**Maturity claimed.** "CatDT demonstrates that the full theoretical catalysis pipeline, from a bulk crystal to experimentally comparable kinetic observables, can be made autonomous, self-improving, and quantitatively predictive."

## arxiv:2602.11689

https://arxiv.org/html/2602.11689 — full text read from arXiv HTML (v1); the appendices render as empty headings

**What was built.** "We investigate the use of tool-using coding agents to automate end-to-end workflows in the open-source CFD package OpenFOAM. Building on general-purpose coding agent interfaces, we introduce a lightweight configuration that guides an agent toward tutorial reuse and log-driven repair to improve case setup and execution."

**What it can call.** "A tool-using coding agent (OpenCode) executes OpenFOAM workflows by issuing function calls (e.g., bash , read , edit ) to use external tools (OpenFOAM/Gmsh/Python)."

**How it was evaluated.** "We use FoamBench-Advanced from CFDLLMBench Somasekharan et al. [2025] , which evaluates context-dependent OpenFOAM workflow execution from natural-language prompts."

**What it achieved.** "Under the default prompt, only 4 out of 9 runs finish to the required end time (Fig. 2 (a))."

**Maturity claimed.** "These results suggest that coding agents have practical utility for automating portions of CFD workflows while highlighting areas that require further investigation."

## doi:10.5281/zenodo.22554152

https://zenodo.org/api/records/22554152 — the Zenodo record holds a single Word document; it was fetched through the Zenodo API and its text extracted. Figures are not readable

**What was built.** "Corridor is a pipeline that automates the diagnose-repair-score workflow end to end using an LLM-based repair agent, while requiring explicit human approval for any change classified as touching model physics."

**What it can call.** "Parses a real LS-DYNA-format deck, classifies any solver error against a taxonomy of known defect patterns, and - for errors requiring judgment rather than pattern lookup - runs a tool-using investigation: the agent inspects the deck content, proposes a scratch-probe (a minimal, disposable re-run that tests a hypothesis without committing to a change), and proposes a fix only once the probe confirms it."

**How it was evaluated.** "Table 1 reports live-run results across four real, structurally distinct models."

**What it achieved.** "Logged LLM spend across all four investigations totaled approximately $0.39 (Sonnet-class model, per-call cost logged automatically)."

**Maturity claimed.** "Corridor automates the diagnose-repair-score workflow for finite-element validation models while keeping physics-relevant decisions under explicit, structurally-enforced human approval rather than model self-assessment."

## doi:10.3389/fchem.2026.1914886

https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2026.1914886/pdf — the publisher PDF was fetched directly and converted with pdftotext

**What was built.** "we propose a Drug Discovery Agent (DDA), a traceable and auditable multi-agent biomedical informatics framework for automating SBDD."

**What it can call.** "In DDA, we organize RDKit (Landrum, 2006), pandas (McKinney, 2010), ADMET-AI, and Uni-Dock/Vina-family docking into a unified downstream evaluation pipeline."

**How it was evaluated.** "We evaluated DDA on a fixed 100-target test set from CrossDocked 2020."

**What it achieved.** "At the molecule level, 59.7% of DDA-delivered candidates passed the full multi-objective screen (QED > 0.5, SA < 4.0, and Vina < -5.0), compared with 39.2% for the best-performing specialized baseline (Pocket2Mol) and 7.8% for TargetDiff."

**Maturity claimed.** "DDA has immediate practical value as a computational triage system that supports human oversight and intervention."

## doi:10.1109/access.2025.3605803

https://r.jina.ai/https://ieeexplore.ieee.org/document/11150377/ — IEEE Xplore returned an empty response; the article is CC BY and was recovered in full through the r.jina.ai reader proxy. Equations are mangled by the proxy and figures and the results table are images that could not be read **v0.2: the IEEE PDF was read from the local PDF store (`Autonomous_Electromagnetic_Simulation_and_Modeling.pdf`). Every quote in this block was checked against it and none differed, and the equations and table values the proxy mangled are now legible - see "Table values recovered in v0.2" below.**

**What was built.** "We develop an LLM-agent framework that autonomously generates and simulates QFN package models in Ansys HFSS. Given textual package specifications, the agent uses a large language model to run the Python script defining the 3D geometry, materials, and excitation ports for HFSS."

**What it can call.** "In this work, PyAEDT was utilized to: Generate QFN package geometries based on user-defined specifications. Set up HFSS simulation projects, including excitation ports, solution setups, and frequency sweeps. Launch a simulation and monitor convergence status. Extract S-parameter datasets for further analysis."

**How it was evaluated.** "In order to test the model's ability to generate reliable and accurate equivalent circuits, we have to be sure that the simulation it sets up is accurate. To test that, we compared the 20-pin QFN simulation results with the measurements obtained with a two-port R&S-ZVB8 vector network analyzer (VNA), as detailed in [15]."

**What it achieved.** "The framework achieved good agreement with measured data up to 1 GHz, validating the approach for practical applications."

**Maturity claimed.** "The system successfully transforms user prompts into complete 3D models, executes electromagnetic simulations, extracts S-parameters, and synthesizes equivalent circuit models-all without manual intervention."

**What the publisher PDF adds in v0.2.** The proxy mangled the equations and could not render Figure 6; both are now legible. The RAG evaluation is reported as a scatter plot rather than a table, so there are no table cells to recover here - the correction is that **no numeric RAG accuracy figure exists in the source to quote**, which the mangled proxy rendering left ambiguous. The limitations section is now fully readable and is quoted below.

**Limitations, in the authors' terms.** "First, the current model accuracy degrades above 1 GHz due to simplified geometric assumptions in the HFSS model. Improving high-frequency fidelity will require implementing adaptive mesh refinement strategies and more sophisticated port modeling techniques." / "Second, the lumped RLC topology used in the paper is chosen as a proof of concept ... The accuracy of more complex equivalent circuit topologies should be validated by measurements in an extended frequency range to confirm model usability for high-frequency applications." / "Third, the system currently relies on predefined geometric templates for QFN packages ... This would enable true design exploration rather than parameter optimization within fixed topologies."

## arxiv:2602.20683

https://arxiv.org/html/2602.20683 — full text read from arXiv HTML (v1)

**What was built.** "This paper presents Grid-Mind, a domain-specific LLM agent that interprets natural-language interconnection requests and autonomously orchestrates multi-fidelity power system simulations."

**What it can call.** "The agent dispatches multi-fidelity simulations through an LLM-first architecture, leveraging an eleven-tool registry and a solver-agnostic base class that supports established simulation engines including PandaPower [ 12 ] , ANDES [ 13 ] , ParaEMT [ 14 ] , and PSS/E [ 15 ] ."

**How it was evaluated.** "The benchmark runner executes the complete agent loop-encompassing tool planning, tool execution, multi-round interaction, and memory-conditioned prompting-rather than evaluating raw model function-calling in isolation."

**What it achieved.** "End-to-end evaluation on 50 IEEE 118-bus scenarios (DeepSeek-V3, 2026-02-23) achieved 84.0% tool-selection accuracy and 100% parsing accuracy. A separate 56-scenario self-correction suite passed 49 of 56 cases (87.5%) with a mean score of 89.3."

**Maturity claimed.** "These results establish a reproducible baseline for continued refinement while maintaining auditable, simulation-grounded decision support."

## title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi

https://github.com/EPEL-SNU/Aspen_Plus_MCP — the accompanying ChemRxiv preprint is on a blocked host and was not retrieved; the repository README, evaluation README, failure taxonomy and ablation documents were read as raw files. All quotes are repository documentation, and the identity match between the repository and the underlying study is asserted by the repository itself, not independently verified

**What was built.** "An [MCP](https://modelcontextprotocol.io) server that exposes **typed, schema-constrained tools** for driving [Aspen Plus](https://www.aspentech.com/) via COM automation - so a language model can interrogate, specify, build, run, and optimize process flowsheets **without writing raw `win32com` code**."

**What it can call.** "`src/aspen_mcp_server.py` | The MCP server - 42 typed tools over the Aspen COM API (identical tool surface on both stdio and HTTP transports)"

**How it was evaluated.** "This package produces the empirical evidence for the paper's central claim: **schema-constrained MCP tool-calling is more reliable than raw win32com code-generation for driving Aspen Plus**, especially for local/small LLMs."

**What it achieved.** "So the 16%->89% gap is **paradigm, not retry budget** - a reviewer-proof control."

**Maturity claimed.** "**Autonomous conceptual synthesis** - build a *converged* flowsheet from a one-line brief (verified by reopening the persisted artifact)."

## title:mcpsolvermodelcontextprotocolserverforconstraintsolvingsatmaxsatsmtcpaspdp

https://raw.githubusercontent.com/szeider/mcp-solver/main/README.md — the source is a code repository rather than a paper; the v4 README was read in full as a raw file

**What was built.** "An MCP server for constraint solving (SAT, MaxSAT, SMT, CP, ASP, DP). It turns the connected LLM host into a solver-writing agent: the host gets a Python kernel preloaded with a real solver library, modeling instructions for the chosen backend, and a submission gate."

**What it can call.** "**`select_backend(solver)`** sets up a persistent IPython kernel with the backend's solver library and helper functions, and returns the modeling instructions for that backend."

**How it was evaluated.** "`mcp-solver-bench` runs the bundled test problems in `tests/problems/<solver>/` end-to-end and validates each result against a per-problem `*_ground_truth.py` validator (which reads the solution JSON on stdin and returns `{\"valid\": ..., \"message\": ...}`)."

**What it achieved.** "The MCP server path is validated with Claude Opus as host: 229/229 instances across CP-Bench (101) and ASP-Bench (128) solve correctly under strict semantic validation, as do the bundled SAT, MaxSAT, and SMT problems."

**Maturity claimed.** "Current status: in our runs with `gpt-5.6-terra`, all 30 bundled test problems solve correctly, including the four `didp` problems (TSPTW, knapsack, weighted tardiness, talent scheduling), each solved to proven optimality in every run."

## title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving

https://developer.nvidia.com/blog/24-7-simulation-loops-how-agentic-ai-keeps-subsurface-engineering-moving/ — full vendor blog post read directly

**What was built.** "This master architecture shown in Figure 1, below, integrates a central orchestration agent with specialized agents designed for simulator interaction and workflow management."

**What it can call.** "Trusted ecosystems: The agents utilize industry-standard simulation and orchestration software via the tool calls."

**How it was evaluated.** "To demonstrate this in action, we applied the multi-agent squad to a well-placement optimization for the Brugge benchmark model . The objective was to maximize net present value (NPV) by optimizing the locations of 30 wells."

**What it achieved.** "Figure 4. NPV convergence comparison: baseline vs. iterative agentic workflow (left) and remaining oil distribution comparison (right)"

**Maturity claimed.** "The opportunity cost of inaction is now measurable. While traditional workflows wait in queues, agentic systems are already exploring the next iteration."

## title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow

https://www.osti.gov/servlets/purl/2480816 — the OSTI landing page gave only the record and abstract; the full accepted manuscript PDF was fetched from the OSTI full-text servlet and converted with pdftotext. The harvest metadata for this record is wrong - it is a peer-reviewed journal article, not a report **v0.2: the Elsevier version of record was read from the local PDF store (`1-s2.0-S0378778824012325-main.pdf`), confirming the journal article is *Energy and Buildings* 327 (2025) 115116. Every quote in this block was checked against it and none differed.**

**What was built.** "Here, we developed a generic LLM-planning-based workflow that takes a building description as input and generates an error-free EnergyPlus building energy model. Our robust workflow includes four core agents: 1) Building Description Pre-Processing, 2) IDF Object Information Extraction, 3) Single IDF Object Generator Suite, and 4) IDF Debugging Agent."

**What it can call.** "The Debugging Agent, whose prompt for planning is shown in Listing 6, ensures the generated IDF file is error-free. If an error is detected, Agent 4 analyzes the .err file from the EnergyPlus simulation ... to identify the problematic class and its object name"

**How it was evaluated.** "We conducted 10 tests of the entire developed agentic workflow and observed the success rate in generating error-free and correct IDF files."

**What it achieved.** "As shown in Table 4, all 10 trials using the developed workflow successfully produced accurate and error-free IDF files, achieving a 100% success rate."

**Maturity claimed.** "The effectiveness of our workflow surpasses: 1) naive prompt engineering, 2) other LLM-based workflows, and 3) manual modeling, in terms of accuracy, reliability, and time efficiency."

## arxiv:2607.18557

https://arxiv.org/html/2607.18557 — full text read from arXiv HTML (v1)

**What was built.** "To address this challenge, we present Agents4GEOS, an AI-agent framework built on the Model Context Protocol (MCP) that provides 52 domain-aware tools for natural-language-driven workflows with GEOS, an open-source multi-physics simulator."

**What it can call.** "The tool layer provides 52 stateless MCP tools, grouped into six domains, which carry out all concrete work."

**How it was evaluated.** "The clearest way to convey what Agents4GEOS does is to follow a real session end-to-end. A reservoir engineer asks, in plain English, to reproduce in GEOS the PUNQ-S3 no-hysteresis CO 2 sequestration results of Salo-Salgado et al. (2024) , which in turn revisit the benchmark in Juanes et al. (2006) , providing only the two source PDF files and a set of mesh and well files."

**What it achieved.** "A 500-year eight-well run completed in 2   minutes 49   seconds, producing 101 reservoir snapshots."

**Maturity claimed.** "Agents4GEOS demonstrates that a multi-agent system organized around a strict separation of concerns - where agents plan, tools compute, and knowledge modules encode domain expertise - can substantially lower the barrier to managing GEOS input files."

## doi:10.1016/j.softx.2025.102367

https://www.osti.gov/servlets/purl/3015372 — ScienceDirect returned a bot-protection page; the full text was obtained from the laboratory deposit of the published open-access version and converted with pdftotext. Identity is certain - same DOI, title, authors and journal volume **v0.2: the Elsevier version of record was read from the local PDF store (`1-s2.0-S2352711025003334-main.pdf`) rather than the OSTI deposit. Every quote in this block was checked against it and none differed.**

**What was built.** "This paper introduces EnergyPlus-MCP, the first open-source Model Context Protocol (MCP) server specifically designed for EnergyPlus simulation workflows, establishing a new foundational infrastructure for AI-driven building energy modeling."

**What it can call.** "The MCP server implements a layered architecture with 35 specialized tools spanning model management, editing and analysis, HVAC and other systems configuration inspection, and simulation execution, enabling Large Language Models to interact with EnergyPlus through conversational interfaces."

**How it was evaluated.** "In this section, we demonstrate EnergyPlus-MCP through a simple energy retrofit analysis workflow using the 5ZoneAirCooled.idf model from EnergyPlus example files."

**What it achieved.** "Through practical demonstrations using a multi-zone building retrofit analysis, we show how the EnergyPlus-MCP server significantly reduces manual efforts while maintaining full simulation rigor."

**Maturity claimed.** "This paper introduced EnergyPlus-MCP, the first novel and open-source Model Context Protocol server for EnergyPlus building energy simulation."

## doi:10.26868/30680611.2026.1305

https://publications.ibpsa.org/proceedings/simbuild/2026/papers/simbuild2026_1305.pdf — the harvest metadata carried a malformed arXiv identifier that is not a real preprint; the full text was read from the open IBPSA conference proceedings PDF and converted with pdftotext

**What was built.** "This study introduces Eppy-LLM, a lightweight multi-agent framework that integrates large language models (LLMs) with EnergyPlus to support interpretable, reproducible, and adaptive analysis based on building energy modeling."

**What it can call.** "Process: Automatically executes EnergyPlus for each IDF with caching, consistent EPW file, and version-controlled directories."

**How it was evaluated.** "Validated using NREL's iUnit building model, the framework achieved 100% syntax-valid simulations and demonstrated adaptive parameter selection across diverse goals, including cooling load reduction, daylight optimization, and total energy minimization."

**What it achieved.** "During the iUnit case study, every generated IDF variant successfully passed the Eppy-based syntax validation, achieving a 100% correctness rate."

**Maturity claimed.** "Applied to the NREL iUnit case study, the framework achieved end-to-end automation-from semantic goal interpretation to validated EnergyPlus execution-without manual intervention."

## doi:10.1080/19401493.2026.2653969

https://r.jina.ai/https://www.tandfonline.com/doi/full/10.1080/19401493.2026.2653969 — the publisher site was reached through the r.jina.ai reader proxy, returning the complete narrative through the data-availability statement; tables and figures render as captions and alternative text, so table cell values were not quotable **v0.2: the publisher PDF was read from the local PDF store (`MCP-enabled agentic AI workflow for building energy modelling  framework and use cases.pdf`). Every quote in this block was checked against it and none differed, and the table cell values the proxy could not render are now quotable - see "Table values recovered in v0.2" below.**

**What was built.** "This paper introduces a novel Model Context Protocol (MCP)-enabled framework that connects AI assistants to EnergyPlus through MCP, a standardized interface for tool invocation and context management."

**What it can call.** "The consultant requested parallel simulation of all four models using the Golden, Colorado weather file. The _simulation\_manager_ tool executed simulation runs sequentially, completing in approximately 16 s total (3-5 s per model)."

**How it was evaluated.** "Based on experimental measurements across ten repeated runs, each workflow execution required approximately 9-12 min on average. For comparison, a graduate student with 1-2 years of BEM experience typically requires about 2.5 h to perform the same analysis, model modification, and simulation sequence manually."

**What it achieved.** "End-to-end demonstrations on a residential energy model show an 80% to 90% time reduction for model inspection, modification, and analysis tasks."

**Maturity claimed.** "These demonstrations establish MCP as a foundational layer for AI-assisted building energy modelling, enabling natural language interactions with simulation tools while preserving professional oversight and decision-making authority."

**Table values recovered in v0.2.** The reader proxy rendered tables as captions only; the publisher PDF makes the cells quotable. Table 7, "LLM token consumption statistics across repeated workflow executions": Runs 10, Mean total tokens 47085.0, Standard deviation 7912.1, Min 34793, Max 63120. Table 8, per-model token usage: "GPT5 | 10 | 7,352.5 | 626.7" and "GPT4-mini | 85 | 4,674.4 | 61.9". Table 6, top-5 sensitivity ranking from Agent 3c: Orientation_180 degrees 52.0%, Orientation_90 degrees 18.1%, Roof Insulation Thickness 7.0%, Window_to_Wall_Ratio_70% 3.6%, Window_to_Wall_Ratio_80% 2.6%.

The surrounding prose, which the proxy did render, attributes the variance: "GPT-5 is invoked once per run for schema reasoning and exhibits low variability (standard deviation of 627 tokens), while GPT-4o-mini handles repeated analytical tasks and contributes most of the run-to-run token fluctuation. Across 10 repeated runs, the top-ranked sensitive parameters remained consistent (orientation, roof insulation, window area)."

## doi:10.3390/buildings15173190

https://r.jina.ai/https://www.mdpi.com/2075-5309/15/17/3190 — the publisher returned HTTP 403 to direct fetches of both the article and its open-access PDF; the full text was read through the r.jina.ai reader proxy. The harvest metadata carries a preprint-server manuscript number in the arXiv field, which resolves to an unrelated paper **v0.2: the publisher PDF was read from the local PDF store (`buildings-15-03190.pdf`). Every quote in this block was checked against it and none differed, and the table cell values the proxy could not render are now quotable - see "Table values recovered in v0.2" below.**

**What was built.** "This study introduces a novel automation pipeline that couples generative AI with finite element modelling through the Model Context Protocol (MCP)-a modular, context-aware architecture that complements language interpretation with structural computation."

**What it can call.** "By interfacing GPT-4 with OpenSeesPy via MCP (JSON schemas, API interfaces, communication standards), the system allows engineers to specify and evaluate 3D frame structures using conversational prompts, while ensuring computational fidelity and code compliance."

**How it was evaluated.** "All configurations are evaluated with respect to compliance with relevant structural performance criteria, particularly storey drift limitations specified in the NEC-15 and ASCE 7-22 standards."

**What it achieved.** "Across four case studies, the GPT+MCP framework demonstrated predictive accuracy for key structural parameters, with deviations under 1.5% compared to reference solutions produced using conventional finite element analysis workflows."

**Maturity claimed.** "This work establishes a reproducible framework for trustworthy AI-assisted analysis in engineering, offering a scalable foundation for future developments in optimisation and regulatory automation."

**Table values recovered in v0.2.** The reader proxy rendered tables as captions only; the publisher PDF makes the cells quotable. Table 9, "Relative error (%) with respect to ETABS in the evaluation of max displacement in the X and Y directions", GPT+MCP column: Case A 1.427 / 1.427, Case B 1.208 / 1.624, Case C 2.834 / 0.233, Case D 1.998 / 1.422, against a standalone-GPT column running from 235.335 to 481.640. Table 10, base shear: GPT+MCP 0.007, 0.003, 0.022, 0.017 against standalone GPT 27.774, 30.489, 35.397, 43.590.

**A claim its own table does not support.** The abstract states the system achieves "accuracy for key structural parameters, with deviations under 1.5% compared to reference [solutions]". Table 9 reports GPT+MCP max-displacement errors of 1.624%, 1.998% and 2.834% in three of the eight case-direction pairs. The base-shear and period errors are far below 1.5%; the max-displacement errors are not. This is recorded here because it was invisible in v0.1, when the table cells could not be read.

## doi:10.3929/ethz-c-000801434

https://arxiv.org/html/2605.19743v2 — the institutional repository record gave metadata only with no full-text link; the full text was read from the arXiv preprint with the same title and authors. IDENTITY MATCH IS INFERRED, not verified

**What was built.** "EngiAI, a multi-agent reference implementation that operationalizes the benchmark by coordinating seven specialized agents"

**What it can call.** "topology optimization, document retrieval, HPC job orchestration, and 3D printer control"

**How it was evaluated.** "Each model-style cell comprises 15 runs (3 random seeds x 5 dataset samples)."

**What it achieved.** "proprietary models achieve 96-97% average task completion on Beams2D, while open-source 4B-parameter models reach 55-78%"

**Maturity claimed.** "LLM-based multi-agent systems can reliably support structured engineering workflows when backed by sufficiently capable foundation models"

## doi:10.48550/arxiv.2605.15028

https://arxiv.org/html/2605.15028 — full text read from arXiv HTML, including methodology, results and appendices

**What was built.** "We propose PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization."

**What it can call.** "The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend."

**How it was evaluated.** "We evaluate PetroGraph on three reservoir models of increasing complexity: the synthetic SPE1 model, the faulted SPE9 benchmark, and the real-field Norne model."

**What it achieved.** "Using weighted normalized root mean square error as the objective, PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne."

**Maturity claimed.** "These results demonstrate that multi-agent orchestration can automate key decisions in history matching, lower the expertise barrier for operating complex simulation workflows, and provide a flexible foundation for extensible, domain-aware reservoir model adaptation."

## doi:10.25417/uic.32994011.v1

https://arxiv.org/html/2603.28959 — the repository DOI was not fetched; the full text was read from the arXiv preprint whose identifier in the harvest record resolved to the matching title and authors

**What was built.** "a multi-agent framework that decomposes exploration-exploitation control into strategic policy mediation and tactical candidate generation"

**What it can call.** "LLMAgent1(Ptstrat)" for strategy and "LLMAgent2(Ptgen)" for candidate generation within Algorithm 1

**How it was evaluated.** "experiments across three representative problem classes: a classical analytical benchmark (Rosenbrock)...a high-dimensional machine learning task (hyperparameter tuning)...and a complex engineering control problem (robot pushing)"

**What it achieved.** "the multi-agent LLM achieves competitive, and in some runs superior, performance"

**Maturity claimed.** "separating strategic control from candidate generation substantially improves the effectiveness of LLM-mediated search"

## doi:10.1016/j.bdes.2026.100042

https://doi.org/10.1016/j.bdes.2026.100042 — every online route failed - the publisher returned HTTP 403 directly and through a reader proxy, the preprint server returned bot verification, and the preprint PDF host failed DNS - so a delegated agent could only reach an abstract summary. The version of record was then read from the local PDF store as 1-s2.0-S3050740526000024-main-2.pdf and converted with pdftotext

**What was built.** "Here, we introduce a Generalizable Automated Geophysical Agent Workflow (GAGAW) that reframes LLMs from code generators to domain-aware, multi-agent workflow orchestrators."

**What it can call.** "This configuration directs the central GAGAW with proper prompt engineering, which could then employ a suite of open-source Python packages (e.g., pyGIMLi, SimPEG, ResIPy) to execute the required geophysical data processing and interpretation tasks."

**How it was evaluated.** "We tested the GAGAW workflow in subsurface hydrology applications using three field datasets spanning diverse hydrogeologic settings across the western United States (Fig. 2a)."

**What it achieved.** "The resulting mean water content was 0.056 with high spatial uncertainty (mean sigma = 0.070; Fig. 3b, left)."

**Maturity claimed.** "GAGAW establishes a practical pattern for accessible, cross-modal geophysical analysis and marks a paradigm shift from LLM-assisted scripting to LLM-orchestrated, tool-centric workflows in Earth and environmental science."

## doi:10.1039/d5dd00435g

https://doi.org/10.1039/d5dd00435g — full text read from the local PDF store (`d5dd00435g.pdf`, the RSC version of record, CC-BY 4.0, published 9 December 2025). In v0.1 every route to this paper failed and the record was empty; this block replaces it.

**What was built.** "Here, we introduce a multi-agent artificial intelligence (AI) framework that autonomously performs end-to-end atomistic simulations, i.e. molecular dynamics (MD), with automated input and associated full suite of analyses, using large language models (LLMs) and multiple specialized AI agents."

**What it can call.** "Our system orchestrates the entire simulation pipeline, from structure generation via Atomsk and interatomic potential discovery through automated web mining, to simulation setup and execution using LAMMPS on high-performance computing (HPC) platforms. Post-simulation, our agentic framework performs automated data analysis and visualization with popular analysis tools like OVITO and Phonopy."

**How it reaches the machine.** "The HPC agent is responsible for packaging simulation files (structure, potential, input scripts), uploading via secure copy protocol (SCP), submitting jobs, monitoring job completion, and downloading results and notifying downstream agents for analysis."

**How it was evaluated.** "In all case study simulations, we validated the capabilities of the agentic pipeline by comparing all the results with human experts. For consistent comparison and due to the deterministic nature of the LAMMPS simulations, the human expert evaluation used the same initial structure and same potential files as those generated by the structure agent and the potential agent respectively."

**What it achieved.** Table 4, cohesive energy, agent versus human: "Fe (BCC) −4.3159 / −4.3159 / 0%", "Au−Cu (FCC) −3.8239 / −3.8246 / 0.018%". On melting: "the heat capacity curve is computed from fluctuations in enthalpy, and it exhibits a sharp peak at approximately 1604 K, which corresponds to the alloy's melting point."

**A number the source does not state.** "The system achieved average errors below x% compared to the results of human LAMMPS simulation experts." — the placeholder is in the published version of record, so the wider crystal-system accuracy claim has no value attached to it.

**Maturity claimed.** "our system successfully reproduced both static properties (lattice constants, cohesive energies, elastic constants, phonon dispersion) and dynamic properties (melting points) across a diverse set of elemental and alloy systems with accuracy comparable to human experts."

**Limitations, in the authors' terms.** "First, dependency management and environment reproducibility, especially for tools like LAMMPS, Atomsk, and Phonopy, can become brittle across platforms or HPC systems." / "Second, although the system is capable of autonomous decision-making and error recovery, the trustworthiness and explainability of some AI-driven actions, particularly LLM-based reasoning, remain open challenges." / "Third, while our framework already scales to a broad class of static and dynamic materials properties, accuracy vs. automation trade-offs become critical for complex tasks such as phonon dispersion, thermal conductivity, or defect energetics."

**Where the authors place the boundary of the agent's responsibility.** "Such variability stems from the intrinsic limitations and transferability of the potential itself, rather than from the agent's operation. Consequently, the agent should not be held responsible for errors originating from the underlying potential choice."

## doi:10.2139/ssrn.7333555

https://ssrn.com/abstract=7333555 - full text read from the local PDF store (`ssrn-7333555.pdf`, the SSRN preprint, watermarked "This preprint research paper has not been peer reviewed"). In v0.1 neither a full text nor an abstract could be retrieved from any route and the record held nothing but its title; this block replaces it.

**What was built.** "Geo2UBEM is introduced as the first end-to-end, meter-free workflow integrating automated scan-to-IDF 3D geometry reconstruction with an LLM-driven multi-agent system (LLM-MAS) for energy parameter inference."

**What it can call.** "The Geo2UBEM pipeline was developed in Python 3.11 and evaluated on a 32-core Windows 11 workstation. EnergyPlus 23.2 was the simulation engine. Bayesian optimization used Optuna TPE (seed = 42; 25 trials per pass; n_startup_trials=10; objective: minimize |NMBE|; no pruner)."

**How the agents divide the work.** The system "deploys a three-agent LLM-MAS system" - an Orchestrator, a Diagnosis Agent and a Parameter Tuning Agent. "The Diagnosis Agent receives the building context. It calls the Claude API (model: claude-sonnet-4-6, temperature = 0.1) with a structured [prompt and returns] a prioritised list of 3-5 parameters." "The Parameter Tuning Agent converts the Diagnosis Agent's recommendations into Optuna [search bounds]."

**What closes the loop.** "In place of the metered data conventionally required under ASHRAE Guideline 14, CBECS 2018 national median benchmarks are used: the LLM-MAS diagnoses simulation-benchmark discrepancies and iteratively narrows the Bayesian optimization search space until convergence."

**How it was evaluated.** "Applied to six calibrated campus buildings across four types at Purdue University (101,170 m2), Geo2UBEM achieves ASHRAE-consistent convergence (|NMBE| <= 5%; CV(RMSE) <= 15%) without any metered input, a result not previously demonstrated for a multi-building cohort. Independent validation against actual metered EUIs confirms all six models fall within CBECS sector ranges, at an average inference cost of $0.09 per building."

**What it achieved.** "Four buildings (Dudley Hall, John T. Myers, PMU, and University Hall) converged after a single LLM-MAS iteration from the neutral-parameter baseline; PMU Club required three iterations and MSEE seven." "Final convergence-check NMBE ranged from -1.22% (University Hall) to +1.04% (MSEE)." "The LLM reasoning layer incurs a modest and predictable overhead: $0.09 USD per building on average (Supplementary Table S1), totalling under $0.55 for the six-building campaign - negligible relative to the ~92-min parallel wall-clock cost."

**A negative result the authors report.** "A three-layer sensitivity and uncertainty analysis (Morris screening, Sobol decomposition, Monte Carlo propagation) reveals a cohort-level observability gap: equipment density accounts for 80-99% of annual energy-use variance, while envelope parameters, most directly recoverable from geometry, contribute negligibly. This challenges common geometry-driven UBEM assumptions, indicating calibration effort is better spent characterizing operational loads than refining envelope parameters."

**Maturity claimed.** "Collectively, these results establish a scalable, low-cost pathway to standards-consistent UBEM calibration for urban stocks lacking metered data."

**Limitations, in the authors' terms.** "Six buildings in a single climate zone (CZ5A) constrain statistical representativeness." / "Ideal-loads systems reduce modelling uncertainty but suppress equipment-level dynamics and contribute to simulation-adequacy gaps in district-heating-dominated buildings." / "LLM reasoning is externally hosted and cannot be fully reproduced across model versions." / "Hardware scalability is extrapolated beyond the observed workload. Parallel execution on six buildings converges wall-clock time to the single-building maximum (~92 min); projecting this linearly to an N-building portfolio on an N-core node has not been validated at larger scale. Memory bottlenecks, I/O contention, and EnergyPlus licence concurrency may break the linear assumption." / "tighter automation of upstream geometry quality control and reproducible pipeline orchestration, which remain the two most manual components in the current workflow."

## doi:10.26434/chemrxiv.15006587/v1

https://doi.org/10.26434/chemrxiv.15006587/v1 - full text read from the local PDF store (`chemrxiv.15006587%2Fv1.pdf`, the ChemRxiv preprint dated 23 July 2026). In v0.1 chemrxiv.org refused every automated client and this record was abstract-only; the system was in the grid only through the authors' repository under the same `system_id`.

**What was built.** "This work instead connects LLMs to Aspen Plus through the model context protocol (MCP), an open standard that lets an AI model operate external software through a predefined, validated set of operations rather than through code it writes itself."

**What it can call.** "An MCP server exposes the simulator as a fixed set of strongly typed tools covering flowsheet synthesis, simulation, and analysis; requests that do not match a tool's declared input format are rejected before they reach the simulator. A declarative builder constructs, converges, and analyzes a complete flowsheet from a single natural-language description, and the entire system runs on the user's own hardware, so no process data leaves the site."

**What the models were.** "In the reference deployment used throughout this work, an OpenClaw gateway orchestrates Qwen2.5-32B and 14B models that are quantized - compressed to lower numerical precision so they fit on modest [hardware]." "Qwen2.5-32B-Instruct and Qwen2.5-14B-Instruct, each served through vLLM on local accelerator hardware."

**How convergence is handled.** "Numerical convergence is the dominant obstacle to autonomous operation. Two specialized tools encode established engineering procedures directly. A shortcut-design tool applies the Winn-Underwood-Gilliland shortcut method to estimate a column's stage count and feed location, then initializes the rigorous model from that estimate - avoiding the solver failures that commonly attend an uninitialized column."

**How it was evaluated.** "Across 19 automatically scored tasks on three flowsheets, tool-calling raised the task success of a local 32B-parameter model from 16% to 89%, and of a 14B model from 0% to 84%." The comparison arm is raw COM code generation, and "The code-generation arm is additionally evaluated in an iterative variant: on failure, the execution error and traceback are re-[submitted]" for up to three attempts.

**What it achieved.** "Under the code-generation paradigm, the 32B model completed 3 of 19 tasks (16%), and the 14B model [0 of 19]." "Indeed, the 14B model with the interface outperforms the 32B model without it by 68 [percentage points]."

**The failure analysis, which is the paper's central evidence.** "Hallucinated variable paths dominate the code-generation failures - 14 of 16 for the 32B model and 15 of 19 for the 14B model in the definitive run, and approximately 78% of all code-generation failures aggregated across repetitions." "Under tool-calling, this entire failure class - together with syntax and type errors - was not merely reduced but absent, as the taxonomy predicts: such requests cannot reach the simulator. The only failure class observed for tool-calling was a silently incorrect answer."

**What error feedback did not fix.** "Iterative error feedback did not close this gap - hallucinated variable paths recovered in zero of thirty instances across both models, the sole rescued failure being an execution exception whose error message contained the repair - confirming that the missing ingredient is schema knowledge, which retries cannot supply but a typed interface provides structurally."

**Maturity claimed.** "reliability is thus a structural guarantee of the interface rather than a behavior the model must learn."

**Limitations, in the authors' terms.** "The interface currently targets steady-state simulation, and the definition of components and reacting systems relies in part on workarounds for limitations of the underlying automation interface." / "The empirical evaluation is likewise centered on a single family of open-weight models and a set of representative - but not exhaustive - flowsheets, so its quantitative conclusions should be read as indicative of the achievable reliability gains rather than as universal bounds." / "the tool layer does not yet cover every Aspen Plus unit-operation model: result extraction and declarative construction support the common block set, and models outside it currently fall back to the raw variable-access tools." / "A middle ground - letting the agent write code that calls the same tested functions - might recover part of the gap; we did not test it."
