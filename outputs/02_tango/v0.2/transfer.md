# Transfer evidence

One block per `core` source. One verbatim quoted sentence per touchpoint claimed on that
source's `transfer.csv` row, plus the sentence the `autonomy` rating was read from.
`NOT FOUND: <what was looked for>` where the text does not contain it.

## doi:10.1145/3731599.3767349

**hpc-scale-out.** "With the Parsl tool ensemble, the LangChain workflow was able to access the Polaris computing resource directly without setting up the submission commands or scripts. The simulation tasks were submitted to the Parsl queue, which then assigned them to the workers with available resources." "This tool launched 100 simulation to the Parsl queue. With pre-defined configuration, Parsl requested 25 nodes from the Polaris PBS queue."

**tool-exposure.** "The first setup was implemented by modifying the LangChain tool calling, which converts the LangChain tool calls to Parsl functions and queues them to the Parsl workers for parallel execution. The second approach was achieved by designing a Parsl ensemble function as an LLM tool, which performed parallel tasks." *(v0.1 quoted the preprint here: "When the LLM agent generates tool calls, it launches them to the Parsl queue, distributing them to the computing resource." The published text instead reads "when the LLM agent invokes tool calls, it converts the tools to Parsl functions and launches" them.)*

**autonomy (executes-and-iterates).** "The model was able to choose the correct simulation input parameters, including the number of tool calls, based on the input prompts. These 8 simulations were then distributed to the 4 GPUs on the workstation via Parsl." No human approval step appears between the prompt and the simulations running, and the agent selects its own tool arguments.

**What the version of record adds on failure.** The preprint record carried `failure_handling: not stated`. The published version reports hallucinated PDB IDs - "These PDB IDs were hallucinated by the LLM agent, as only 5 search results were generated from the researcher" - a tool-call cap "around 24", and worker load imbalance of "~177 seconds difference in execution time". None of these is handled by the system; they are observed and reported.

## doi:10.48550/arxiv.2604.07681

**autonomy (executes-and-iterates).** "Starting from a human natural language query, the planner agent interprets the scientific objective and decomposes it into structured, executable tasks."

**config-generation.** "invalid generated arguments led to workflow termination"

**solver-control.** "Executor agents invoke simulation tools exposed by the Chemistry MCP server to launch atomistic simulations through Parsl."

**hpc-scale-out.** "From the weak and strong scaling runs, we performed a total of 25 experiments. We observed 4 failures, resulting in an overall success rate of 84%."

**tool-exposure.** "Executor agents invoke simulation tools exposed by the Chemistry MCP server to launch atomistic simulations through Parsl."

**results-interpretation.** "the top 20% of candidates demonstrated high performance, with working capacities achieving 7.06 mol/kg."

**failure_handling.** "To mitigate this, failed runs were restarted from the initial query."

## doi:10.48550/arxiv.2512.07917

**autonomy (executes-and-iterates).** "Subsequently, the runner executes the simulation, while the corrector analyzes error logs and iteratively prompts for adjustments until successful completion."

**config-generation.** "The generator agent uses our fine-tuned Qwen3-8B model to produce OpenFOAM configurations."

**solver-control.** "Subsequently, the runner executes the simulation, while the corrector analyzes error logs and iteratively prompts for adjustments until successful completion."

**tool-exposure.** "utilizes the model context protocol (MCP), an open standard that decouples LLM reasoning from external tool execution."

**results-interpretation.** "The lift coefficient, Cl, exhibited a relative error of 2.58% compared to the experimental data. The larger drag coefficient error, 16.42%"

**failure_handling.** "As the flow becomes more complex at higher AoA, the success rate declines, and the average number of correction iterations increases, reflecting the agent's active error-handling as it adapts to challenging flow physics like separation."

## doi:10.48550/arxiv.2606.07850

**autonomy (executes-and-iterates).** "No manual intervention was required for mesh generation, solver configuration, boundary condition application, or post-processing."

**config-generation.** "No manual intervention was required for mesh generation, solver configuration, boundary condition application, or post-processing."

**solver-control.** "The Simulation Agent executes a ReAct loop with up to 25 reasoning steps and nine tools: check_config_warnings, query_knowledge_graph, validate_config, run_simulation, modify_config, debug_simulation, list_recent_runs, get_run_status, run_parametric_sweep."

**verification-regression.** "confirm second-order spatial convergence (O(h2)) for all three benchmark cases"

**provenance-reproducibility.** "All 11 services are orchestrated via Docker Compose, ensuring reproducible deployment."

**results-interpretation.** "KG Smart achieves 100% success and the highest output quality (physics score 0.933 vs. 0.853 for KG Off, MPF 0.926 vs. 0.796)."

**tool-exposure.** "The Simulation Agent executes a ReAct loop with up to 25 reasoning steps and nine tools"

**failure_handling.** "Of the 2.2% failures, the majority are attributable to invalid boundary condition combinations (e.g. pure Neumann systems without a reference point), mesh resolution requests exceeding GPU memory, and numerical divergence on stiff transients."

## doi:10.11578/dc.20260516.1

**autonomy (not stated).** NOT FOUND: there is no evaluation section, so autonomy cannot be read from one.

**none.** NOT FOUND: the source reports no evaluated behaviour, so no touchpoint is claimed. The README describes uncertainty gating, active-learning escalation and HPC scheduler submission as capabilities, none of them evidenced by a reported evaluation.

**failure_handling.** NOT FOUND: no statement about what happens when a DFT calculation or relaxation fails or does not converge.

## doi:10.1016/j.dche.2026.100312

**tool-exposure.** "An MCP server toolset enables the LLM to communicate programmatically with APS using Python, allowing it to execute complex simulation tasks from plain-language instructions."

**topology-construction.** "The next case study assesses autonomous flowsheet synthesis through both a step-by-step dialogue and a single prompt", and on the ammonia flowsheet "the agent correctly reconstructed the main equipment connectivity and recycling-loop logic."

**optimisation-loop.** "It then proceeds with a methodical approach by iteratively adjusting the reflux ratio and checking the targeted methanol purity", reaching "With a reflux ratio of 1.45, I've achieved 95.1 mol% [methanol]."

**results-interpretation.** "The first shows the agent autonomously analyzing flowsheets, finding improvement opportunities, and iteratively optimizing, extracting data, and presenting results clearly", and "The agent effectively extracts relevant data from thousands of variables, interprets complex thermodynamic relationships, and presents findings in accessible formats."

**autonomy (executes-with-approval).** the loop is explicitly broken at the convergence step - "At this stage, a critical manual intervention is required because the user must shift the distillation column setup from 'Configure' mode to 'Solve' mode to obtain rigorous simulation results. This step is intentionally delegated to the human user rather than the LLM agent." The authors' own summary is that the system is "best positioned as a copilot that accelerates workflow execution, rather than as an autonomous decision-maker".

## doi:10.48550/arxiv.2605.20819

**autonomy (executes-and-iterates).** "The supervisor maintained the thread context across all four sub-tasks, passing file paths and model identifiers generated in earlier steps as inputs to later steps without requiring any user intervention."

**tool-exposure.** "DynaMate2 is a LangGraph-based multi-agent framework for converting expert-defined Python functions into persistent AI-callable tools."

**config-generation.** "packmol_build_system was called with the resulting XYZ files, molecular counts, and box dimensions to produce nacl_water_box.xyz"

**solver-control.** "run_nvt_md was called with the configuration file, the downloaded checkpoint, a temperature of 300 K, 500,000 steps, and the output trajectory path nvt_nacl_water.traj"

**results-interpretation.** "plot_nvt_trajectory was called with the trajectory path and an output PNG filename, producing the final figure."

**failure_handling.** "Agent reliability is the most pressing concern: the current implementation requires carefully engineered execution rules injected into each agent's system prompt to prevent the common failure mode in which a specialist transfers control back to the supervisor without performing any work."

## doi:10.1145/3815572.3815744

**autonomy (executes-and-iterates).** "The automatic pipeline was applied to a set of 100 publicly available paired-end reads sequenced from isolate bacterial genomes...without human intervention"

**config-generation.** "selects, parameterizes, validates and executes appropriate KBase applications."

**tool-exposure.** "wrappers for the KBase API (e.g., run_job, list_objects)"

**results-interpretation.** the agent "autonomously performed read quality control, genome assembly, taxonomic classification with GTDB-Tk, and downstream analysis producing annotated genomes, reproducible Narratives, and draft manuscripts without human intervention"

**provenance-reproducibility.** "producing annotated genomes, reproducible Narratives, and draft manuscripts without human intervention"

**failure_handling.** "It features a self-correction loop where the Validation and Handle Error nodes can iteratively refine parameters to resolve runtime failures without human intervention"

## doi:10.1016/j.cma.2026.118985

**autonomy (executes-and-iterates).** "In our studies, the human did not give problem-solving help or corrections; the sole action was to stop the run after the Evaluator showed that the answer passed the acceptance requirement."

**config-generation.** "generates legacy FEniCS codes based on the problem formulation"

**solver-control.** "The Executor runs the code, captures any run-time output and errors, and returns this feedback to the FEniCS Coder."

**verification-regression.** "the sole action was to stop the run after the Evaluator showed that the answer passed the acceptance requirement"

**failure_handling.** "This interaction continues until the code executes without errors or the LLM reaches its token limit."

## doi:10.5281/zenodo.19597589

**autonomy (not stated).** NOT FOUND: there is no evaluation section, and no sentence describing who runs the tools in a trial.

**tool-exposure.** "Tools are exposed via the Model Context Protocol (MCP), the open standard for agent-tool communication."

**provenance-reproducibility.** "Session provenance: automatic storage of tool inputs, outputs, parameters, sources, and timestamps"

**failure_handling.** "Validators never raise - failures appear in `quality_flags` without crashing the tool."

## doi:10.25394/pgs.32118403

**autonomy (executes-and-iterates).** "When the operator switches on the 'Live Reactor Data' toggle in PUR-1 GPT, the PUR-1 GPT agents (LangChain and LangGraph) acknowledge the usage of the Read_Reactor_Live_Window tool as evident in Fig. 5.2 and Fig. 5.3."

**surrogate-modelling.** "physics-driven surrogate models trained on functional mappings between the Monte Carlo inputs and outputs were used to bypass such limitations"

**uncertainty-quantification.** "surrogate model to predict the effective multiplication factor keff and its uncertainty +/-1 sigma from control rod positions"

**results-interpretation.** "Agent emits the final plain-English answer to the user."

**tool-exposure.** "Compared with non-agentic retrieval, the agentic workflow enables structured tool use for rod-position parsing, effective multiplication factor prediction, neutron flux metric prediction, and live reactor data queries."

**failure_handling.** NOT FOUND: searched for fallback, retry and tool-failure handling across the whole thesis; nothing is said about what happens if a surrogate or live-data tool call fails.

## doi:10.48550/arxiv.2603.12813

**autonomy (executes-and-iterates).** "the agent makes a single change to the input file, runs the simulation, and reads the results"

**config-generation.** "one agent solves the abstract engineering problem while another implements the solution as Chemasim code"

**topology-construction.** "In all cases, the process development agent is able to design reasonable process flowsheets based solely on the analysis of thermodynamic behavior"

**solver-control.** "The extension can also be used by the agent, allowing it to autonomously run simulations and read and interpret the console output."

**results-interpretation.** "the agent makes a single change to the input file, runs the simulation, and reads the results"

**failure_handling.** "the agent recognizes error messages that - particularly in the case of syntax errors - often include precise information on the location of the error. This allows the agent to directly react by correcting the syntax error and running the simulation again"

## doi:10.48550/arxiv.2608.14573

**autonomy (executes-and-iterates).** "ExperimentAgent then invokes an LLM to generate a concrete experiment design"

**config-generation.** "ExperimentAgent then invokes an LLM to generate a concrete experiment design"

**solver-control.** "invoke the designated solver"

**optimisation-loop.** "an end-to-end autoresearch framework for wireless optimization"

**verification-regression.** "If validation succeeds, an executable experiment package is produced. Otherwise, the code, execution logs, validation report, and frozen contracts are returned to ExperimentAgent for bounded repair."

**failure_handling.** "If validation succeeds, an executable experiment package is produced. Otherwise, the code, execution logs, validation report, and frozen contracts are returned to ExperimentAgent for bounded repair."

## doi:10.48550/arxiv.2509.18178

**autonomy (executes-and-iterates).** "The success rate is measured by the percentage of cases that ran successfully through the agentic framework given the prompt describing the simulation scenarios."

**config-generation.** "the Input Writer Agent implements a structured file generation sequence that respects OpenFOAM 's hierarchical organization"

**topology-construction.** "We demonstrate the mesh generation capabilities of Foam-Agent utilizing Gmsh python library using two cases, where the natural language description of the mesh is provided to the agent."

**solver-control.** "The Runner Agent interfaces with the OpenFOAM execution environment by preparing the simulation (cleaning artifacts, setting up output capture) and running the Allrun script."

**hpc-scale-out.** "The agent generates the necessary OpenFOAM case files along with a Slurm submission script for the HPC platform Perlmutter ."

**results-interpretation.** "The agent will then execute the python file and correct errors if any (like the reviewer agent) till the visualization(s) is saved as a .png file in the run directory."

**failure_handling.** "This review-correction cycle is repeated iteratively until either the errors are resolved or a maximum number of attempts specified by the user is reached ( Figure 1 )."

## arxiv:2602.11666

**autonomy (executes-and-iterates).** "The Baseline agent required an average of 22.11 reflection rounds per case, relying on iterative trial-and-error. The Full PhyNiKCE agent, leveraging intelligent reflection with symbolic retrievers in Stage 3, reduced this burden by 59% to just 9.06 rounds"

**config-generation.** "the PhyNiKCE-enabled agents strategically 'front-load' their inference effort"

**solver-control.** "The validation matrix was made rigorous by testing multiple solvers ( simpleFoam , rhoCentralFoam , sonicFoam ) and RANS turbulence models ( SST , Spalart-Allmaras , and [k-epsilon] ) for each geometry."

**failure_handling.** "If the simulation fails, the agent triggers an autonomous error-reflection loop, iterating up to 30 times to resolve the issue."

## doi:10.48550/arxiv.2511.03852

**autonomy (executes-and-iterates).** "GAIA + AlphaEvolve : We let GAIA optimize the system prompt and the evaluator configuration for a maximum of 10 AlphaEvolve iterations."

**optimisation-loop.** "We employ OpenEvolve ( Sharma, 2025 ) , an open-source implementation of AlphaEvolve ( Novikov et al., 2025 ) , to evolve an inverse algorithm that maps to fracture parameters."

**results-interpretation.** "GAIA Agent will then analyze the waveform data, apply the selected phase picking method, and return the results in an interactive plot."

**failure_handling.** NOT FOUND: no statement about what happens when the driven code - OpenEvolve, the ObsPy routines or ETAS - fails, errors or does not converge.

## doi:10.48550/arxiv.2608.29665

**autonomy (executes-and-iterates).** "Convergence is never the agent's to declare: it is evaluated arithmetically in code before the agent is consulted, and any proposal that would make the calculation computationally cheaper is programmatically refused."

**config-generation.** "The DFT calculation is configured by the Translator agent, which maps extracted parameters onto SIESTA input directives."

**solver-control.** "Following each variable-cell relaxation (target force tolerance ), the Convergence agent reads the output and selects from four actions (increasing the mesh cutoff, expanding the basis set, densifying the in-plane -grid, or terminating execution), advancing monotonically along predefined parameter progressions"

**verification-regression.** "Before a final verdict is issued, the Critic agent selects verification checks to run from a vocabulary of eight options (symmetry, expected symmetry, calibration, convergence, units, structure file, literature claims, and literature methods)."

**provenance-reproducibility.** "Each agent call is written to a JSONL audit log recording what the agent proposed, what was finally applied, and which gate fired on any difference, from which override counts per agent are tallied."

**results-interpretation.** "Published and recomputed cells are therefore both sorted before comparison, and a comparison is formed only where the paper reports both in-plane constants."

**failure_handling.** "Non-converged calculations trigger an automated Diagnostician agent that parses error logs and extracts supporting failure lines; in the present campaign, all simulated targets achieved SCF convergence nominally without activating diagnostic recovery."

## doi:10.2139/ssrn.4921381

**autonomy (executes-and-iterates).** "Each metric for single experiments is the average of n tests (n=10). For the iteration metric in the cost, maximum iteration is set to 20 in the program to prevent infinite iterations. If executability does not reach 3 or above after 20 iterations, the test is automatically marked as failed and the iteration is terminated."

**config-generation.** "The InputWriter role focuses on generating and refining the necessary input files for the CFD simulation."

**solver-control.** "The Runner executes the CFD simulation using OpenFOAM. This role ensures that the simulation runs smoothly and monitors for any possible errors during execution."

**failure_handling.** "If an error occurs, the Runner provides the execution error command and error context to the Reviewer. The Reviewer examines the file architecture and context to identify and solve the error, then returns the revised instructions to the InputWriter."

## doi:10.48550/arxiv.2603.26005

**autonomy (executes-and-iterates).** "The generated program is subsequently executed to produce simulation results, followed by systematic evaluation. During execution and evaluation, the framework continuously monitors compilation status, interface conformance, runtime stability, and structural completeness."

**config-generation.** "Configuration Correctness , which assesses whether the simulation pipeline, modules, controllers, and network settings are correctly configured"

**topology-construction.** "Then add a capacitor bank at the weakest-voltage bus identified in the initial simulation, rerun the simulation, and compare the voltage regulation and line loading improvements before and after compensation."

**solver-control.** "At each simulation step, the aggregated building-level electricity demand generated by CityLearn is mapped to corresponding load buses in the grid network, where power flow analysis is performed to compute grid operating states."

**optimisation-loop.** "Train SAC controllers with and without voltage-aware reward terms. Analyze whether voltage-aware rewards improve voltage regulation and reduce grid constraint violations during simulation."

**results-interpretation.** "Simulation Validity , which examines whether the generated outputs are physically plausible and consistent with the task objectives."

**verification-regression.** "The results further show that iterative refinement mainly improves workflow executability by reducing runtime failures and dependency inconsistencies, leading to higher execution success rate across most settings."

**failure_handling.** "When violations or failures are detected, they are converted into structured feedback, which guides subsequent refinement."

## doi:10.48550/arxiv.2605.06607

**autonomy (executes-and-iterates).** "Given the periodic hill at Reh=5600, a starter SA case, reference wall friction coefficient (Cf) data, and the objective 'minimize lower-wall Cf RMSE,' AI CFD Scientist ran 44 discovery iterations (worked-example trace in Figure 3)."

**config-generation.** "The framework runs on OpenFOAM through Foam-Agent and exposes three coupled pathways"

**solver-control.** "the system autonomously discovers a Spalart-Allmaras runtime correction that reduces lower-wall Cf RMSE against DNS by 7.89%"

**optimisation-loop.** "AI CFD Scientist ran 44 discovery iterations"

**results-interpretation.** "vision-based physics verification"

**verification-regression.** "Appendix G Failure-Mode Taxonomy and Detection Gates CFD automation fails along distinct axes that require different gates."

**failure_handling.** "When a gate rejects a run, the rerun controller revises the requirement. It may reuse nearby successful cases, such as relaxation factors, or schemes."

## doi:10.48550/arxiv.2505.04997

**autonomy (executes-and-iterates).** "On FoamBench, Foam-Agent achieves an 88.2% execution success rate on the 110 Basic-tier tasks and 62.5% on the out-of-distribution Advanced tier, all without expert intervention."

**config-generation.** "dependency-aware file generation is formulated as a topological traversal of the OpenFOAM case dependency graph, so that each configuration file is synthesized in the context of its already-generated predecessors, enforcing cross-file consistency"

**solver-control.** "six specialist agents span planning, meshing, file writing, execution, review, and visualization"

**results-interpretation.** "It then executes the script and, like the Reviewer, repairs any errors until the visualizations are saved as PNG files in the run directory"

**tool-exposure.** "In our deployment the same unmodified server is driven by both Cursor and Claude Code."

**verification-regression.** "(a) Execution-success rate (Mexec) with Claude 3.5 Sonnet and GPT-4o on the CFDLLMBench dataset; the corresponding bucketed field-level fidelity (MNMSE) is reported in Table 1."

**failure_handling.** "a trajectory-conditioned reviewer loop iteratively repairs failed runs by conditioning each correction on the accumulated error-and-diagnosis trajectory of its own previous attempts, applying a minimal configuration edit that targets a reduced solver-error set"

## doi:10.1016/j.compenvurbsys.2026.102449

**autonomy (not stated).** NOT FOUND: no evaluation section exists. The nearest is hypothetical - "In a typical use case, a city logistics planner might query: 'What's the best way to transport 200 containers from Houston to New York within 36 hours?'"

**none.** "This paper introduces a conceptual framework at the intersection of agentic AI, MCP, and cognitive digital twins." - no behaviour of the authors own system is evaluated anywhere in the paper, so no touchpoint can be claimed.

**failure_handling.** NOT FOUND: the paper states a requirement rather than a mechanism - "They must be able to detect knowledge gaps, flag unsolvable problems, and communicate uncertainty to ensure scientific integrity."

## doi:10.48550/arxiv.2508.07035

**autonomy (executes-and-iterates).** "Acting autonomously, this agent confirmed the existence of the band structure image and the integrity of the computation using its dedicated validation tools."

**config-generation.** "Our input-preparation tools automatically generate all necessary VASP input files and submit jobs to a Slurm scheduler."

**solver-control.** "Here, we introduce VASPilot, an open-source platform that fully automates VASP workflows via a multi-agent architecture built on the CrewAI framework and a standardized Model Context Protocol (MCP)."

**hpc-scale-out.** "Our input-preparation tools automatically generate all necessary VASP input files and submit jobs to a Slurm scheduler."

**results-interpretation.** "We performed band-structure and density-of-states (DOS) calculations for 2H-MoS2, plane-wave cutoff convergence tests, structural relaxations using van der Waals corrections, and band-gap comparisons across transition-metal dichalcogenides."

**verification-regression.** "Acting autonomously, this agent confirmed the existence of the band structure image and the integrity of the computation using its dedicated validation tools."

**failure_handling.** "For failed jobs, the tool returns the VASP error messages; for successful runs, it reads the full result set via pymatgen, archives the data in the database."

## arxiv:2607.20346

**autonomy (executes-and-iterates).** "The Reviewer compiles any custom solver via wmake, launches the simulation and parses the resulting solver and build logs."

**config-generation.** "IteraSim RAG, a retrieval-augmented software back-end for automated OpenFOAM case generation"

**solver-control.** "The Reviewer compiles any custom solver via wmake, launches the simulation and parses the resulting solver and build logs."

**verification-regression.** "All six reference configurations run to completion on OpenFOAM v2506, and two synthetically corrupted cases are diagnosed and repaired within the bounded Reviewer loop."

**failure_handling.** "A dedicated error locator extracts the first physically meaningful error ... and feeds it back to the InputWriter as a targeted correction request. The corrective loop is bounded to ten cycles."

## doi:10.31223/x5f47g

**autonomy (executes-and-iterates).** "Agentic AI automatically generates/verifies inputs from the original dataset, calls swmm5 to execute simulations, and extracts key outputs."

**config-generation.** "In the Agentic SWMM scenario, Skill orchestrates the corresponding MCP to autogenerate the INPs file; runs the swmm engine; extracts indicators such as peaks and continuity"

**solver-control.** "Agentic AI automatically generates/verifies inputs from the original dataset, calls swmm5 to execute simulations, and extracts key outputs."

**results-interpretation.** "swmm-plot-mcp: reads INP/OUT artifacts and produces figures that conform to a fixed user's specification"

**verification-regression.** "the same INP file is run synchronously in the SWMM GUI, and the consistency of key indicators and resulting statistics is used as the basis for equivalence verification"

**provenance-reproducibility.** "To ensure that the entire Agentic SWMM workflow is auditable and reproducible, each run will create an independent manifest file that documents the SWMM version used, parameter mappings, input file hashes, and quality gate (e.g., continuity diagnostics)."

**tool-exposure.** "In the middle layer, we packaged SWMM's commands as callable tools through the MCP."

**failure_handling.** "swmm5 missing; INP errors; runDir not writable; nonzero return code" (Table 1, failure modes column for the swmm_run tool)

## doi:10.1080/09544828.2026.2624356

**autonomy (executes-and-iterates).** "The results highlight the LLM's ability to balance exploration and exploitation during structural optimization and to autonomously terminate the design process once further meaningful improvements were unlikely."

**optimisation-loop.** "The process continues over a fixed number of iterations or until an early stopping condition is triggered, at which point the best feasible structure found across all iterations is returned."

**topology-construction.** "In both tasks, the LLM is granted the flexibility to add nodes at arbitrary locations, define strategic connections, and select cross-sectional areas from the available set."

**results-interpretation.** "The raw output shows that the LLM first correctly interprets the optimization objective: minimizing maximum member stress while keeping total mass within limits."

**failure_handling.** "At each step, the LLM generates a candidate truss structure with up to 10 attempts allowed to account for failures where the output does not conform to the required format."

## doi:10.48550/arxiv.2604.27753

**autonomy (executes-and-iterates).** "The proposed system's performance gain is largest in Scenario S3, where traffic congestion caused by road incidents makes the RL controller's historically-optimised policy ineffective, while the digital twin's what-if simulation quickly finds a good re-routing and re-timing solution."

**optimisation-loop.** "Simulation Agent: Runs what-if simulations in the digital twin to assess the impact of different signal timings on congestion, throughput and waiting times in the simulated period."

**failure_handling.** NOT FOUND: no statement of what happens when the digital-twin simulation, an agent, or an API call fails or does not converge.

## doi:10.48550/arxiv.2412.17146

**autonomy (executes-with-approval).** "A request for human approval of any tool usage was included as a necessary safety precaution during testing; however, challenges arose in the LangChain/LangGraph framework with respect to the solicitation and inclusion of substantial human feedback between tool usages by the LLM agent."

**config-generation.** "Case Configuration example: Modifying burner size in FireFOAM's poolFireMcCaffrey tutorial case from 0.3m to 0.6m."

**solver-control.** "The agent then recovered and successfully ran the serial job"

**hpc-scale-out.** "The agent performed much more poorly in the HPC tests, only succeeding once in nine agent-tool loops."

**results-interpretation.** "Tool and plotted the results using the Python Interpreter Tool in 17 loops."

**failure_handling.** "In the failing run, the agent hallucinated the existence of a number of files in the case directory, and ultimately failed to recover."

## arxiv:2607.01812

**autonomy (executes-with-approval).** "A key feature is staged user confirmation. Before critical tool calls, the agent summarizes the inferred action, names the tool to be called, lists the key parameters, and asks for user approval."

**config-generation.** "the agent selects computational tools, constructs finite element TO models, checks meshes and boundary conditions, and launches sensitivity-based optimization with typed solver arguments."

**topology-construction.** "Regular domains are generated directly, uploaded meshes are previewed before use, and image inputs are processed through the image-to-geometry and geometry-to-mesh pipeline."

**optimisation-loop.** "The deterministic solver evaluates the finite element state, objective, constraints, and sensitivities, and MMA updates the density variables as described in Sec. 2.6."

**results-interpretation.** "After convergence, TO-Master returns optimized results, field distributions, convergence histories, and interactive visualizations."

**failure_handling.** "If a tool returns a warning or failure status, the agent reports the issue and pauses instead of continuing silently."

## doi:10.1063/5.0257555

**autonomy (executes-and-iterates).** "Throughout the simulation, error logs are monitored; if a failure is detected, the error data is appended to the user query and the process iterates."

**config-generation.** "In fact, OpenFOAMGPT chose the right boundary condition codedFixedValue, not others such as fixedValue, oscillatingFixedValue."

**solver-control.** "However, when using the agent, only the Motorbike case experienced errors that prevented it from running, while the PitzDaily case failed to converge after a few steps."

**failure_handling.** "Throughout the simulation, error logs are monitored; if a failure is detected, the error data is appended to the user query and the process iterates. Otherwise, the workflow concludes successfully."

## doi:10.1038/s43246-025-00994-x

**autonomy (executes-with-approval).** "All 10 runs correctly selected the MolecularDynamicsAgent as the appropriate sub-agent to handle the simulation task. In every run, the agent successfully extracted all 8 key simulation parameters and invoked the MDSimulationNVETool with an identical dictionary"

**config-generation.** "It interprets the natural language query to extract simulation conditions, identifying a constant energy (NVE) ensemble with a target temperature of 660 degrees C, which it correctly converts to 933.15 K"

**results-interpretation.** "Based on the CIF file, the agent constructs a natural language response that includes precise lattice parameters (a = b = c = 3.5555) and atomic positions (Al at (0, 0, 0) and Ni at (0, 0.5, 0.5)), consistent with the specified symmetry and stoichiometry."

**failure_handling.** NOT FOUND: no statement of what happens when a simulation or tool call fails or does not converge. The only failure reported is an outcome: "Run 5 failed to extract any material IDs, suggesting an isolated error."

## doi:10.48550/arxiv.2602.04850

**autonomy (executes-and-iterates).** "We asked Quntur to autonomously execute all questions five times independently to evaluate its robustness and reliability."

**config-generation.** "Creates and debugs ORCA 6.0 input files using the ORCA manual"

**solver-control.** "Upon computational validation that one proposed pathway is unfeasible, the agent autonomously reformulates the workflow to explore an alternative mechanism involving the triplet PES."

**results-interpretation.** "Quntur also realized that the calculations contradicted the known result that a shift in character between vertical excitation and the relaxed excited-state geometry occurs."

**failure_handling.** "Like its predecessor, Quntur is resilient: when a job fails, produces a warning, or the computed properties (e.g., energies, spin, and vibrational frequencies) indicate that a change in methodology is needed, it does not stop. Instead, it diagnoses the issue and tries a solution."

## arxiv:2604.18233

**autonomy (executes-with-approval).** "Aether is designed as a Human-in-the-Loop (HITL) system, ensuring that critical deployment decisions and risk acceptance remain under human operator authority."

**verification-regression.** "agents execute tests against the candidate change within the NDT environment"

**solver-control.** "For Batfish-based verifications, the NDT translates agent input into Batfish-specific parameters and normalizes results."

**results-interpretation.** "The user remains in the loop and may validate Aether's actions by analyzing the detailed final report and updating the ITSM ticket to improve test plan and verifications."

**failure_handling.** "If test results indicate issues, the user may iterate on the change implementation and re-initiate the validation process."

## doi:10.1039/d6dd00060f

**autonomy (executes-and-iterates).** "Unspecified design and operational parameters are estimated using black-box optimization, successively aligning the behavior of the individual unit operations."

**topology-construction.** "an LLM-assisted data pipeline that converts real-world, natural language text descriptions of chemical production into, first, machine-readable PFD-level flowsheet graphs and, second, converged simulations in commercial flowsheeting software."

**config-generation.** "The resulting digitized flowsheets are automatically translated into converged Aspen Plus simulations by augmenting missing information with black-box optimization."

**optimisation-loop.** "Parameters of the unit operations are additionally co-optimized for energy or solvent consumption in a multi-objective manner."

**failure_handling.** "Suppose that, after adding a new unit, the black-box optimization does not yield a converged flowsheet or a unit that fulfils its task in a meaningful way, as defined by thresholds on the objective functions. In that case, the most recently added unit is systematically simplified."

## doi:10.2139/ssrn.6074109

**autonomy (executes-and-iterates).** "Specifically, Iterations is the average number of error corrections required by the multi-agent system to successfully complete one simulation case."

**config-generation.** "(3) InputWriter Agent: Generates the initial OpenFOAM configuration files or corrects erroneous configuration files."

**solver-control.** "When triggered, the Runner Agent executes the \"Allrun\" file to start the case simulation, recording the execution sequence of the simulation commands."

**results-interpretation.** "As per the post-processing requirements, the ParaMaster Agent generated the velocity and pressure field distribution plots."

**failure_handling.** "If the simulation fails, the Runner Agent sequentially captures the error messages from each simulation log file."

## arxiv:2607.05134

**autonomy (executes-and-iterates).** "Each scenario is processed by the agent graph, and the generated JSON specification is compared with a reference specification."

**config-generation.** "The system converts multi-turn natural-language input into a validated JSON specification, generates solver-backed datasets, trains neural operators"

**solver-control.** "The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element backend, and stores the solutions as operator-ready tensors."

**surrogate-modelling.** "PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines."

**failure_handling.** "Invalid patches are not applied. The Repairer receives the current specification, the failed patch and the Validator feedback, then returns a corrected patch for another validation pass."

## arxiv:2605.14154

**autonomy (executes-and-iterates).** "TSAgent matches human-expert success rates (70% vs. 73+/-12%) without any human intervention."

**config-generation.** "ASE 3.26.0" is used "for structure preparation and NEB path interpolation"

**solver-control.** "TSAgent operates through a persistent plan-execute-analyze-replan loop, continuously adapting its strategy based on convergence diagnostics and geometric feedback without human intervention."

**hpc-scale-out.** "All DFT calculations are submitted to a SLURM-managed institutional HPC cluster using exclusive 128-core nodes (partition RM)."

**results-interpretation.** "TSAgent independently reproduces Bronsted-Evans-Polanyi scaling relationships for NH3 dissociation on metal and single-atom alloy surfaces from a published heterogeneous catalysis study"

**failure_handling.** "If a failure is identified during execution of the current plan, the PA diagnoses the issue using the failure summary provided by the EA, diagnostics from prior steps, expert-crafted debugging guidelines, and a replan log recording previous replanning decisions and their outcomes."

## doi:10.48550/arxiv.2511.00122

**autonomy (executes-and-iterates).** "The Aerodynamics Engineer autonomously executed all twelve simulation cases using OpenFOAM's simpleFoam solver."

**config-generation.** "The Structural Engineer autonomously executed 432 configurations through an integrated FreeCAD-Gmsh-CalculiX pipeline."

**solver-control.** "The Aerodynamics Engineer autonomously executed all twelve simulation cases using OpenFOAM's simpleFoam solver."

**optimisation-loop.** "The framework is validated through UAV wing optimization, where agents autonomously evaluated four NACA airfoils across Reynolds numbers ranging from 10^5 to 10^6."

**hpc-scale-out.** "By separating LLM-based planning (serial) from Docker-based CFD execution (parallel), the system achieves near-linear scaling up to the configured parallelism limit."

**failure_handling.** "For mesh-related failures, it reduces refinement parameters by 20%; for solver divergence, it adjusts relaxation factors from 0.7 to 0.3 for pressure and 0.5 to 0.2 for velocity."

## doi:10.48550/arxiv.2507.14267

**autonomy (executes-and-iterates).** "The supervisor dispatches one worker step at a time in a synchronous, sequential control loop."

**config-generation.** "Structure generation uses AutoCat autocat to identify adsorption sites and ASE ase-paper to represent structures and prepare Quantum ESPRESSO inputs."

**solver-control.** "The convergence agent analyzes input, output, and error files when calculations fail or require additional diagnosis, and recommends parameter modifications."

**hpc-scale-out.** "The HPC agent manages resource selection, job submission, job monitoring, and file retrieval."

**uncertainty-quantification.** "Bayesian ensemble sampling with van der Waals correction (BEEF-vdW)"

**provenance-reproducibility.** "In one case, an unsupported value was passed through the identity x+0, producing a valid provenance record without validating the original value."

**failure_handling.** "The convergence agent analyzes input, output, and error files when calculations fail or require additional diagnosis, and recommends parameter modifications."

## doi:10.1063/5.0294696

**autonomy (executes-and-iterates).** "Through natural language interaction, the framework is designed to manage three core stages...enabling fully language guided, zero-shot and end-to-end complex flow simulations."

**topology-construction.** "We validate CFDagent by reproducing canonical sphere flows at Reynolds numbers of 100 and 300 using three distinct inputs: a simple text prompt (i.e., 'sphere'), an image-based input, and a standard sphere model."

**config-generation.** "the Preprocessing Agent requests the geometry and Reynolds number, supporting three distinct input modes."

**solver-control.** "the Solver Agent that configures and executes an immersed boundary flow solver."

**results-interpretation.** "The Postprocessing Agent equips the LLM with scripts for analyzing physical quantities, visualizing flow fields, and fusing simulation results to generate realistic imagery."

**failure_handling.** NOT FOUND: no sentence describes what happens when the solver fails, errors or does not converge; the paper contains no error-handling, retry or divergence discussion.

## arxiv:2605.23273

**autonomy (executes-and-iterates).** "Executor agent is a non-LLM agent responsible for executing the program generated by Coder agent."

**config-generation.** "Executor agent is a non-LLM agent responsible for executing the program generated by Coder agent."

**optimisation-loop.** "pyOptSparse [Wu et al. [2020]] with SNOPT as the optimizer"

**results-interpretation.** "The cycle terminates when Critic again approves the new converged design under the same evaluation rubric."

**failure_handling.** "When errors arise during execution, Reviewer agent invokes Coder agent with a correction strategy, prompting it to revise the program until it runs successfully."

## doi:10.48550/arxiv.2512.06404

**autonomy (executes-and-iterates).** "Following the generation of a simulation protocol, the QE program is executed."

**config-generation.** "GENIUS translates free-form human-generated prompts into validated input files that run to completion on ~80% of 295 diverse benchmarks, where 76% are autonomously repaired."

**solver-control.** "Following the generation of a simulation protocol, the QE program is executed."

**failure_handling.** "If the execution fails, QE generates a CRASH file containing a descriptive error message." / "If an LLM uses all its retries without resolving the error, it switches to the next model in the hierarchy."

## doi:10.48550/arxiv.2512.13930

**autonomy (executes-and-iterates).** "The computed quantities, such as adsorption energies, are then returned to the review layer where a reviewer agent determines whether the specified criteria have been met or further exploration is required."

**config-generation.** "The Geometry Generator agent receives a natural language structure request and constructs a prompt containing the user query plus a JSON knowledge base with twelve ASE construction tips covering site placement, molecular orientation, and covalent radii for common surface atoms and adsorbates."

**solver-control.** "Once a candidate structure is chosen, the information is passed to the simulation layer, which provides a multimodal interface that converts high-level simulation objectives into validated DFT workflows."

**optimisation-loop.** "Across two chemical applications, CO adsorption on Cu-surface transition metal (M) adatoms and on M-N-C catalysts, reasoning-driven exploration reduces required atomistic simulations by up to 90% relative to trial-and-error selection."

**results-interpretation.** "The computed quantities, such as adsorption energies, are then returned to the review layer where a reviewer agent determines whether the specified criteria have been met or further exploration is required."

**failure_handling.** "Rejection triggers written feedback specifying identified deficiencies and returns control to the generator agent with incremented version numbering." NOTE: this describes rejection of a candidate structure by a reviewer agent, not a failed or unconverged DFT run; no sentence about non-convergence of VASP was found.

## doi:10.48550/arxiv.2605.24002

**autonomy (executes-with-approval).** "Following user review and approval, the agent then autonomously orchestrates the prolonged execution campaign."

**tool-exposure.** "The framework integrates more than 100 human-curated multidisciplinary skills, including database access, thermodynamics and kinetics modeling, and diverse simulation engines employing machine learning interatomic potentials (MLIPs) and density functional theory (DFT)."

**solver-control.** "Following user review and approval, the agent then autonomously orchestrates the prolonged execution campaign."

**failure_handling.** NOT FOUND: no sentence describing what happens when a simulation errors, crashes or fails to converge.

## arxiv:2605.26179

**autonomy (executes-and-iterates).** "Execution then enters a per-step loop. For each step, the Step Planner materializes VASP parameters informed by this accumulated History."

**config-generation.** "For each step, the Step Planner materializes VASP parameters informed by this accumulated History."

**solver-control.** "When the monitor issues a Terminate verdict, the Recovery Agent diagnoses the failure and generates modified parameters for a retry."

**verification-regression.** "We evaluate AutoDFT along three axes: (i) end-to-end task success on a benchmark of realistic VASP workflows, (ii) physical correctness of the properties extracted from successful runs, and (iii) the sources of improvement provided by closed-loop execution."

**results-interpretation.** "(ii) physical correctness of the properties extracted from successful runs"

**failure_handling.** "When the monitor issues a Terminate verdict, the Recovery Agent diagnoses the failure and generates modified parameters for a retry."

## doi:10.48550/arxiv.2509.10210

**autonomy (suggests).** "Each simulation setup is performed five times, and the resulting files are evaluated both manually and by executing them in RASPA to verify correctness and reproducibility."

**config-generation.** "We present a multi-agent system for literature-informed force field extraction and automated RASPA simulation setup."

**failure_handling.** "We define the success rate as the proportion of simulations correctly configured for their intended task, and the execution rate as the proportion that run without errors." NOTE: this defines a failure metric; no sentence describes what the system does when a run errors.

## doi:10.1109/ipdps65963.2026.00114

**autonomy (executes-and-iterates).** "We use four applications to demonstrate the practicality, generality, and robustness of Academy in real-world settings"

**hpc-scale-out.** "Academy starts 3,328 actors in 7.6 seconds and achieves 3.4K actions/second maximum throughput on a single agent."

**tool-exposure.** "Academy, a modular and extensible middleware designed to deploy autonomous agents across the federated research ecosystem, including HPC systems, experimental facilities, and data repositories."

**solver-control.** "The validation stage of the pipeline uses the LAMMPS GPU library to assess MOF stability (strain)."

**failure_handling.** "Given that research infrastructure can fail, agents may want to perform periodic state checkpointing; Academy does not enforce a specific checkpointing mechanism, as format, location, and frequency are application specific."

## doi:10.48550/arxiv.2608.15881

**autonomy (executes-and-iterates).** "Across 25 tool calls, the run required three validation-and-repair iterations, resolved three errors, and completed in 85.6 s."

**config-generation.** "the agent retrieves relevant MOOSE documentation and examples, drafts or edits input files, and calls MOOSE-aware tools to check, and run the resulting simulations."

**solver-control.** "Across 25 tool calls, the run required three validation-and-repair iterations, resolved three errors, and completed in 85.6 s."

**verification-regression.** "A prompt is considered successful when the generated input runs successfully and remains aligned with the requested physics, geometry, boundary conditions, and outputs."

**failure_handling.** "The agent uses this evidence to repair the actual input file and runs the checks again."

## doi:10.1145/3770855.3818856

**autonomy (executes-and-iterates).** "The agent mimics a human scientist's workflow: it interprets rich, multi-modal feedback from the simulator, forms physically-grounded hypotheses to explain discrepancies, and proposes structured parameter updates."

**optimisation-loop.** "Battery-Sim-Agent, the first framework to deploy a Large Language Model (LLM) agent in a closed loop with a high-fidelity battery simulator."

**results-interpretation.** "it interprets rich, multi-modal feedback from the simulator, forms physically-grounded hypotheses to explain discrepancies, and proposes structured parameter updates."

**failure_handling.** "Certain parameter combinations (e.g., extremely low diffusion coefficients paired with high C-rates) cause state variables such as particle surface concentration to become negative or singular."

## doi:10.48550/arxiv.2604.22571

**autonomy (executes-with-approval).** "Once a workflow has successfully passed validation and review, it is considered safe for execution."

**config-generation.** "applying LARA-HPC to orchestrate DFT based simulations with the BigDFT program"

**hpc-scale-out.** "12 nodes (48 MPI) would bring the peak to ~4,560 MB/process, leaving ~2.1 GB free per process"

**tool-exposure.** "remotemanager package to address operational and scheduling constraints" exposed via "Model Context Protocol (MCP)" using the "FastMCP library"

**verification-regression.** "If issues are detected, structured feedback is generated and the workflow is returned to the generation phase for correction."

**failure_handling.** "If issues are detected, structured feedback is generated and the workflow is returned to the generation phase for correction."

## doi:10.48550/arxiv.2604.11945

**autonomy (executes-and-iterates).** "Without any manual tuning, AutoSurrogate is able to outperform expert-designed baselines and domain-agnostic AutoML methods."

**surrogate-modelling.** "AutoSurrogate, an LLM-driven multi-agent framework designed to autonomously construct, train, and deploy deep learning surrogate models for subsurface flow modeling."

**optimisation-loop.** "Given a dataset and optional human instructions, the framework executes an end-to-end workflow that covers data inspection, architecture selection, hyperparameter optimization, training, evaluation, and artifact reporting."

**results-interpretation.** "Given a dataset and optional human instructions, the framework executes an end-to-end workflow that covers data inspection, architecture selection, hyperparameter optimization, training, evaluation, and artifact reporting."

**failure_handling.** "If numerical instability is detected, the hyperparameter search space is tightened by reducing the upper bound on admissible learning rates and strengthening gradient clipping constraints."

## arxiv:2607.11084

**autonomy (executes-with-approval).** "We retain approval authority over SQL plans and analysis launches, while the agent executes approved workflows and returns aggregate artifacts."

**config-generation.** "orchestrated: (1) SQL cohort extraction via the broker's SQL extraction pipeline, (2) phenotype tab-separated values (TSV) generation ... (3) GWAS submission via the broker's GWAS pipeline with PLINK2 logistic regression"

**verification-regression.** "Systematic comparison with independently curated expert analyses showed that human-AI review identified phenotype discrepancies and enabled iterative refinement of the hypertension definition."

**failure_handling.** "When jobs fail, the agent inspects broker events, pod logs, and pipeline status before resubmitting"

## arxiv:2604.02688

**autonomy (executes-and-iterates).** "The researcher provides a task description in natural language, and the LLM-driven agent generates Python code"

**solver-control.** "These libraries in turn submit jobs to materials computation backends (VASP, DeePMD-kit, LAMMPS, phonopy, etc.)"

**surrogate-modelling.** "(1) machine-learning force field training via active learning"

**optimisation-loop.** "(3) heuristic parameter-space search"

**hpc-scale-out.** "composing any installed domain library to orchestrate multi-code workflows on remote HPC clusters"

**failure_handling.** "When runtime errors arise (incorrect function calls, database limits, sandbox restrictions), the agent diagnoses the cause and self-corrects autonomously, typically within one or two additional steps"

## arxiv:2606.18425

**autonomy (executes-and-iterates).** "The loop ran autonomously throughout, without per-fix human approval, and human involvement was limited to post-hoc review of the applied changes."

**config-generation.** "An LLM agent, grounded in a released plugin of Pegasus-specific skills, first produces a reviewable specification of checkable constraints and acceptance criteria, then generates the executable workflow."

**topology-construction.** "The fifty round experiments consist of 101 sub-workflows, 50 rounds across two datasets plus the top level, and generate over 2,000 jobs each."

**hpc-scale-out.** "Experiments ran on a distributed HTCondor pool on the FABRIC testbed with four GPU-equipped worker nodes across sites, HAWI (3 GPUs), MAX-1 (2), MAX-2 (2), and NCSA (2), totaling 9 GPUs."

**verification-regression.** "A validation loop repairs runtime failures, checks code against those constraints, and regenerates the implementation from the specification alone."

**failure_handling.** "A validation loop repairs runtime failures, checks code against those constraints, and regenerates the implementation from the specification alone."

## arxiv:2512.23010

**autonomy (suggests).** "It is important to note that while the AI agent simplifies the setup, configuration, and post-processing of simulations, it does not execute VASP calculations directly."

**config-generation.** "Masgent provides turnkey utilities for generating high-quality VASP input files that follow best practices and established parameter standards."

**surrogate-modelling.** "To assess the accuracy and computational efficiency of Masgent's fast-simulation module, we benchmarked the supported MLPs, SevenNet, CHGNet, Orb-v3, and MatterSim, against DFT-PBE reference calculations."

**results-interpretation.** "From the resulting trajectories, the AI agent computed mean squared displacements (MSDs) and extracted Li diffusion coefficients (D) at each temperature."

**optimisation-loop.** "As shown in Figure 13b, Masgent automatically tuned the model hyperparameters using Optuna-based Bayesian optimization, efficiently identifying high-performing configurations while pruning unpromising trials."

**failure_handling.** "Certain expert-level tasks, such as diagnosing subtle VASP error messages or optimizing HPC job scheduling, may still require manual intervention and domain expertise."

## doi:10.1016/j.taml.2025.100623

**autonomy (executes-and-iterates).** "Despite 20 maximum inference iterations per trial, neither configuration successfully generated valid solver files"

**config-generation.** "Some of the present models efficiently manage different CFD tasks such as adjusting boundary conditions, turbulence models, and solver configurations, although their token cost and stability vary."

**solver-control.** "OpenFOAM runner then executes the simulation with the setup files"

**failure_handling.** "upon failure detection, the error data are appended to the original query and the process cycles again"

## doi:10.48550/arxiv.2602.00185

**autonomy (executes-and-iterates).** "Tier III cases were executed twice to verify consistency"

**config-generation.** "If clear issues are detected, such as a lack of DFT convergence, the Operator terminates the run and attempts to reconstruct or optimize the input parameters."

**solver-control.** "QUASAR autonomously orchestrates complex multi-scale workflows across diverse methods, including density functional theory, machine learning potentials, molecular dynamics, and Monte Carlo simulations."

**results-interpretation.** "Once the Evaluator verifies the successful completion of a task, it condenses the task context by distilling the valuable actions and outcomes while discarding noise and failed attempts."

**surrogate-modelling.** "The multiscale integration allows QUASAR to autonomously chain simulations across length and time scales...parameterize force fields from quantum calculations and then deploy the resulting force field for large-scale dynamics or adsorption studies."

**failure_handling.** "If clear issues are detected, such as a lack of DFT convergence, the Operator terminates the run and attempts to reconstruct or optimize the input parameters."

## doi:10.48550/arxiv.2602.17886

**autonomy (executes-and-iterates).** "All benchmarking exercises were performed in fully autonomous mode, with a single user prompt to facilitate the evaluation."

**config-generation.** "El Agente Solido can autonomously query external materials databases, generate and manipulate atomic structures...and select appropriate computational and physical parameters for each task."

**solver-control.** "If any calculation fails, the DFT Subagent troubleshoots the issue by modifying the input files and passing the revised files to the QE Running Subagent for resubmission."

**results-interpretation.** "Across 7 benchmarking exercises, each repeated at least 10 times with the same prompt, El Agente Solido achieved an average score of 97.9%"

**hpc-scale-out.** "runs a Quantum ESPRESSO calculation via SLURM"

**failure_handling.** "If any calculation fails, the DFT Subagent troubleshoots the issue by modifying the input files and passing the revised files to the QE Running Subagent for resubmission."

## doi:10.48550/arxiv.2504.08621

**autonomy (executes-and-iterates).** "Once an input file has been written, a multi-round execute-analyze-correct iterative process begins"

**config-generation.** "automatically generate Moose input files and execute calculations"

**solver-control.** "Once an input file has been written, a multi-round execute-analyze-correct iterative process begins"

**failure_handling.** "all unsuccessful attempts were caught in an infinite loop. Specifically, the agent would get stuck repeatedly trying to fix an error by calling a particular function."

## doi:10.1038/s41598-025-92337-6

**autonomy (executes-with-approval).** "Participants were tasked with defining MD simulations using natural language, and their interactions with the agent were monitored"

**config-generation.** "Workers, specialized for domain-specific software such as LAMMPS, generate corresponding simulation scripts."

**failure_handling.** "When the agent is unable to complete a task independently, it can pause the current process and request clarification or assistance from the user via the UI."

## doi:10.48550/arxiv.2504.06260

**autonomy (executes-and-iterates).** "The ControllerAgent calls a CorrectorSubAgent that proposes the next solution given the 'current' code and feedback, execution history and the result of tool calls."

**config-generation.** "The LLM agent is expected to return a solution that should consist of the API calls that solve the problem, similar to Ground Truth Code"

**solver-control.** "Failure modes b) and c) are far more common than a) and occur when the code is not fully correct and the partially constructed COMSOL Multiphysics model exports nothing or an incorrect value."

**results-interpretation.** "the partially constructed COMSOL Multiphysics model exports nothing or an incorrect value"

**verification-regression.** "We benchmark different SOTA LLMs on their baseline (single-turn) performance with these metrics."

**failure_handling.** "Failure modes b) and c) are far more common than a) and occur when the code is not fully correct and the partially constructed COMSOL Multiphysics model exports nothing or an incorrect value."

## doi:10.48550/arxiv.2603.03372

**autonomy (executes-and-iterates).** "the agent autonomously plans the entire solution path (pw.x-ph.x-q2r.x-matdyn.x in this case) without user specification"

**config-generation.** "Configurations that fail to achieve convergence are treated as invalid points in the accuracy-cost space and excluded from Pareto consideration"

**solver-control.** "the agent autonomously plans the entire solution path (pw.x-ph.x-q2r.x-matdyn.x in this case) without user specification"

**optimisation-loop.** "TritonDFT delivers a >10x acceleration over manual expert execution"

**hpc-scale-out.** "Following common practices adopted by DFT experts, the agent estimates the resource cost via a short default MPI run (within 30 seconds)."

**results-interpretation.** "The Interpreter parses the raw output to provides correctness and produces refinement suggestions or summaries."

**verification-regression.** "DFTBench comprises 73 unique crystalline materials, exhibiting diversity in two aspects."

**failure_handling.** "Configurations that fail to achieve convergence are treated as invalid points in the accuracy-cost space and excluded from Pareto consideration"

## doi:10.48550/arxiv.2506.05616

**autonomy (executes-with-approval).** "Notably, without human guidance, all models fail to produce valid workflows in all three tasks."

**surrogate-modelling.** "Subsequently, ML Force Fields (MLFFs) are used to efficiently relax candidate structures towards energetically favorable configurations, significantly reducing computational overhead compared to DFT calculations."

**solver-control.** "Optimize these candidate structures using Machine Learning force fields, ensuring the minimization of energy and refinement of lattice and atomic positions."

**failure_handling.** "If execution of the generated code results in runtime errors, a diagnostic error signal is generated, triggering the Tool Code Generator itself to revise and regenerate the code."

## doi:10.48550/arxiv.2607.15001

**autonomy (executes-with-approval).** "Before the plan is handed to the executor, a human checkpoint allows physicists to review the proposed plan and engage in optional interactions to refine it."

**config-generation.** "Given a natural-language research request specifying the target observable, ensemble and kinematic setup, the system produces a reviewable PyQUDA workflow comprising the measurement script, job-submission artifacts, execution logs and numerical outputs."

**hpc-scale-out.** "Realize the approved computation plan, generate the PyQUDA and SLURM scripts, and conduct tests to verify and revise the scripts"

**verification-regression.** "Because successful execution does not by itself establish scientific correctness, each generated workflow was validated by direct numerical comparison with a hand-written reference implementation for the same observable, ensemble and kinematic setup."

**failure_handling.** "Most issues were conventional implementation errors, including einsum-index mismatches, gauge-context handling mistakes, output-format inconsistencies and array-shape mismatches. These errors were detected by static checks, test execution or automated critique, and were corrected before final validation."

## doi:10.48550/arxiv.2601.20996

**autonomy (executes-and-iterates).** "At each iteration, the agent conditions on the complete history of evaluated structures and their stability outcomes, together with a summary of previously generated but unevaluated candidate structures stored in an internal buffer."

**optimisation-loop.** "MADE simulates closed-loop discovery campaigns in which an agent or algorithm proposes, evaluates, and refines candidate materials under a constrained oracle budget, capturing the sequential and resource-limited nature of real discovery workflows."

**surrogate-modelling.** "MLIP-based selection yields the largest single performance gain. The Chemeleon + MLIP pipeline achieves the highest AF among non-agentic methods (AF = 6.4) and the largest AUDC, consistent with prior work demonstrating the effectiveness of surrogate screening in materials discovery."

**failure_handling.** NOT FOUND: any statement of what happens when the MLIP oracle, relaxation or generator fails or does not converge. The nearest execution guards are a uniqueness filter re-applied to new generations and a 10-iteration limit per decision step.

## doi:10.48550/arxiv.2601.09749

**autonomy (executes-and-iterates).** "The LAM-driven pipelines incurred planning overhead due to LLM invocation but successfully selected appropriate actions without human intervention."

**provenance-reproducibility.** "A workflow execution is considered reproducible if replay yields bitwise-identical outputs without re-executing prior actions."

**failure_handling.** "Logs confirm that failed actions in R-LAM produce trace nodes with error status, exception type, and partial outputs, while the naive LAM baseline terminates without structured failure records."

## doi:10.1038/s44172-025-00583-3

**autonomy (executes-with-approval).** "With the prompts of natural language commands, the agent can autonomously execute process simulation, optimization, carbon accounting and result visualization, with all results rigorously validated by the authors to ensure reliability."

**config-generation.** "These results were fed to the agent along with the official guide and 13 relevant examples to generate the .inp file for the rigorous RadFrac model (Fig. 2a)."

**topology-construction.** "To quantify the potential energy-saving and decarbonization effect of heat pump, the agent was asked to convert the optimal traditional distillation process to a heat pump-assisted process by generating an .inp file for the process displayed in Fig. 4."

**optimisation-loop.** "A sensitivity analysis and a design specification were designed by the agent to execute the process optimization. The agent set various combinations of Nt and Fs in a sensitivity analysis."

**techno-economic.** "The heat pump-assisted distillation process could substantially reduce the energy demand by 80%, so the operation cost and total cost are also lower than the traditional distillation process, despite the capital expenditures on the compressor."

**failure_handling.** NOT FOUND: any statement of what happens when Aspen Plus errors or a design specification or sensitivity run fails to converge. The nearest is an input-file validity statement about 125 of 131 downloaded example files being executable.

## doi:10.69997/pse.120458

**autonomy (executes-and-iterates).** "Missing information on operating parameters is augmented by systematic, unit-by-unit black-box optimization."

**topology-construction.** "This knowledge is aggregated into one text per process and fed into the second pipeline, \"text2flowsheet\" [3], which digitizes expert-level flowsheet graphs from natural-language descriptions."

**config-generation.** "The digitized flowsheet graphs are systemically translated into simulations within an established commercial process simulator."

**optimisation-loop.** "Missing information on operating parameters is augmented by systematic, unit-by-unit black-box optimization."

**failure_handling.** "Potential simplifications necessary to achieve convergence are recorded transparently."

## doi:10.48550/arxiv.2408.15866

**autonomy (executes-and-iterates).** "Error Handling assesses the system's ability to manage errors during tool calling, measured as (Number of errors handled successfully / Total number of errors encountered)."

**solver-control.** "The Mathematical and Computational Instruction-Tuning (MathComp) dataset comprises over 7,500 instruction-question-answer triplets designed to adapt code SLMs to computational tool usage, facilitating the generation of executable code to solve ordinary differential equations (ODEs), partial differential equations (PDEs), differential-algebraic equations (DAEs), linear algebra problems, and optimization tasks."

**tool-exposure.** "Each protocol provides detailed information about its tool, including argument requirements specifying the inputs needed to run the tool, an overview of the tool's functionality and use cases, and the response schema outlining the expected output structure and type."

**failure_handling.** "If a runtime error occurs during program execution, a reflection mechanism identifies and revises the program to fix the error."

## doi:10.1016/j.ijheatfluidflow.2026.110399

**autonomy (executes-and-iterates).** "The system autonomously generated visualizations and identified displacement efficiency, demonstrating the framework's capability to conduct sophisticated multi-phase investigations without human intervention."

**config-generation.** "OpenFOAMGPT correctly generate configuration files for all cases, and the simulations completed successfully."

**solver-control.** "OpenFOAMGPT successfully generated all necessary configuration files, including appropriate boundary conditions for the pressure-driven channel flow, correct specification of the fluid properties, and proper numerical schemes for the icoFoam solver."

**results-interpretation.** "The Post-processing agent automatically generated plots that clearly illustrated the transition from Darcy flow ... to non-Darcy flow at higher gradients"

**verification-regression.** "As demonstrated in Table 1 and Figure 6, our framework achieved a 100% reproducibility rate across all test cases-including the most demanding multi-case parametric studies."

**failure_handling.** "In such cases, this module captures detailed error logs and contextual information about the failure, structuring this feedback for the LLM."

## doi:10.20944/preprints202608.1323.v1

**autonomy (executes-with-approval).** "We used Codex with GPT 5.4 in high accuracy mode, and Claude Code v2.1.232. Across the tests, the work remained human supervised. The user provided scientific goals and corrections."

**config-generation.** "Coding assistants can generate the basic configuration files from the cluster documentation, or by directly probing the installed software and module environments on the login nodes."

**hpc-scale-out.** "For distributed MACE training, a distributed-method check swept two to eight GCDs and found that torchrun passed all seven tested cases, while the tested Slurm and MPI launch methods failed all seven cases."

**provenance-reproducibility.** "We completed a 20,000-step ASE MACE MD trajectory and preserved the trajectory, log, manifest, and reasonableness-check artifacts."

**failure_handling.** "The coding assistant used a legitimate and documented mechanism when configuring the Spack environment; however, a combination of the cluster's user environment and the mishandling of already-loaded modules by Spack raises a compilation error during the final installation stage that can be detected only after extensive debugging."

## doi:10.1016/j.taml.2025.100594

**autonomy (executes-and-iterates).** "An 'experiment' proceeds from inputting a natural language description and mesh files to obtaining CFD simulation results. An experiment 'passes' if it achieves a convergent solution in 72 hours at most 10 correction attempts; otherwise, it 'fails'."

**config-generation.** "The fine-tuned LLM then generates the OpenFOAM case directory through structured CoT reasoning, including numerical configurations, initial fields, boundary conditions, and an execution script."

**solver-control.** "Furthermore, the benchmark includes multi-solver configurations (e.g., cylinder wake validated with icoFoam, simpleFoam, pisoFoam, and pimpleFoam) to test the framework's ability to select context-appropriate numerical methods."

**failure_handling.** "If errors occur, the corrector analyzes and resolves issues. The corrected files are then resubmitted to the runner, continuing this cycle until the simulation completes successfully."

## doi:10.1016/j.taml.2026.100660

`config-generation` and `solver-control` - "MetaOpenFOAM 2.0 primarily handles the CFD simulation and postprocessing tasks through Iterative COT and Question Decomposition COT (QDCOT) mechanisms", with "OpenFOAM 10 [...] employed for CFD simulations."

**optimisation-loop.** "The integration of external analysis tools, such as the active subspace method and L-BFGS-B optimization algorithm, further enhances the framework's capacity to perform detailed sensitivity analysis and multivariable optimization."

**surrogate-modelling.** "Figure 11 presents the response surface and the components of [the active direction] obtained by combining CFD analysis task 2 executed by OptMetaOpenFOAM with the active subspace method", and the authors qualify it: "owing to these inherent bounds, the fitted response surface is not perfect."

**results-interpretation.** "An external sensitivity analysis tool is then invoked to complete the sensitivity analysis task via graphical visualizations and textual explanations."

**autonomy (executes-and-iterates).** "concise natural language commands (~200 characters) successfully triggered elaborate computational sequences involving simulation setup, postprocessing, sensitivity analysis, and parameter optimization, translating into over 2,000 lines of automated code execution." A single prompt drives setup, execution, sampling, surrogate fitting and optimisation with no described human step in between.

**What the version of record adds.** A measured robustness figure: "pass@1 (%) ... Dataset 1 86.6 ... Dataset 2 85.0", across semantically equivalent but syntactically different prompts.

## doi:10.5281/zenodo.20543501

**autonomy (executes-and-iterates).** "**Do not call `run_simulation()` or `run_with_generator()` until a critic agent has reviewed and approved the setup.** This is a hard precondition, not a workflow suggestion."

**config-generation.** "The agent generates solver-specific input, runs the simulation, and validates results."

**topology-construction.** "`generate_mesh` | Gmsh mesh generation (L-domain, plate with hole, channel)"

**solver-control.** "Solve the heat equation on a unit square with T=1 on the left, T=0 on the right, and zero-flux top/bottom. Pick the best solver and verify against the analytical solution. | FEniCS (auto-selected) | PASS (L2 error = 7e-15, machine precision)"

**tool-exposure.** "It exposes a small set of shared tools for solver discovery, simulation preparation, mesh generation, run execution, multi-solver coupling, in-place solver development, and visualisation."

**verification-regression.** "Solve the Poisson equation with a known analytical solution on a 3D unit cube using NGSolve. Run an h-convergence study with 4 mesh refinement levels and verify optimal L2 convergence rate for P1 and P2 elements. | NGSolve | PASS"

**results-interpretation.** "Simulate 2D flow past a circular cylinder at Re=100 using FEniCS. Run long enough to capture periodic vortex shedding and measure the Strouhal number. Compare against the accepted value St~0.164. | FEniCS | PASS"

**failure_handling.** "If the simulation fails after multiple attempts with the chosen solver, consider whether an alternative solver might be more suitable - `prepare_simulation` shows what alternatives exist."

## doi:10.5281/zenodo.19835550

**autonomy (not stated).** "Implementation status: This section describes the theoretical instrumentation layer that the software is designed to orchestrate. No physical experiments have been performed as part of this work."

**none.** NOT FOUND: no touchpoint can be supported, because the evaluated content is CALPHAD computation performed by the authors rather than agent behaviour. The MCP agent layer and the provenance knowledge graph are described as architecture only: "Solid borders denote components implemented in this work (Sections 2 and 7); dashed borders denote components designed but not yet implemented (Sections 3-6)."

**failure_handling.** NOT FOUND: the paper never states what happens when a pycalphad, ESPEI or kawin call fails, errors or does not converge. The nearest statement is a capability gap rather than error handling: "The kawin precipitation kinetics module cannot be exercised for LLZO until interfacial energies and diffusion coefficients are available."

## doi:10.48550/arxiv.2509.20374

**autonomy (executes-and-iterates).** "RAG provides the framework with similar simulation files and the Reviewer allows for a trial and error approach to running OpenFOAM cases, mimicking human troubleshooting. The absence of either decreases the Success Rate by approximately 10% (Table 2), underscoring their critical roles in achieving optimal performance within the proposed framework."

**config-generation.** "This task requires an LLM to create the required OpenFOAM input files, save them in appropriate directories, and call different tools within OpenFOAM to run a physically accurate simulation, all based on a natural language prompt."

**topology-construction.** "The CFD simulation workflows in FoamBench have preprocessing steps where a correct geometry and mesh file must be generated by the LLM."

**solver-control.** "We use OpenFOAM v10 for all experiments."

**verification-regression.** "The holistic metric we use has three components: code executability, relative numerical error, and numerical convergence."

**failure_handling.** "We observe that RAG primarily mitigates configuration-related errors, such as missing physical properties, turbulence models, or undefined keywords, by providing accurate solver templates and reference parameters. In contrast, the Reviewer component reduces reasoning and consistency errors, such as mismatched boundary conditions or invalid inter-file dependencies."

## doi:10.1002/aidi.202500174

**autonomy (executes-and-iterates).** "ChatCFD demonstrated an operational success rate of 82.1% across the 315 benchmark and perturbed cases, with success defined as error-free configuration and execution leading to converged simulations."

**config-generation.** "(3) Case File Generation, generating OpenFOAM case files using the knowledge base; and (4) Execution and Error Reflection, running simulations..."

**solver-control.** "Flexibility experiments demonstrate ChatCFD's ability to autonomously select appropriate solvers across compressible/incompressible and steady/transient regimes (95.23% success) and switch turbulence closures (100% success), even on unseen configurations."

**results-interpretation.** "To enhance the transparency and user intelligibility of the computation process, ChatCFD integrates a dedicated Physics Interpreter in the fourth stage of the workflow."

**verification-regression.** "We define physical fidelity through a three-tier protocol. A case qualifies only if it meets all criteria without simplifications that compromise the scientific objective or user requirements"

**failure_handling.** "Persistent Errors: ChatCFD leverages short-term memory (recent error messages and file modification histories) and long-term memory (reflection histories) to address recurring issues. Reflection histories, stored as structured insights, enhance the system's ability to adapt and resolve complex errors iteratively."

## doi:10.48550/arxiv.2607.22596

**autonomy (executes-and-iterates).** "Our LAMMPS agent, either by autonomously selecting a potential as described in Sec. 3, or by using a user-provided potential, executes LAMMPS for the desired simulation task. As shown below, for standard tasks, this can be accomplished with minimal human input and prompting."

**config-generation.** "the agent first invokes an LLM that is tasked with authoring the script that is aligned with the user's requested simulation task."

**solver-control.** "With this script, the agent then executes the simulation via MPI, or kokkos in the case of GPU-enabled computing resources."

**results-interpretation.** "we employ this agent's 'write code' tool that allows the agent to write python code that can read, summarize, and visualize the simulation log files generated by the LAMMPS agent."

**verification-regression.** "Here, we further demonstrate the modular nature of URSA's agents by tasking the execution agent to call the arXiv agent as a tool to critique the core LAMMPS agent's calculation of the melting temperature."

**failure_handling.** "If the simulation results in an error, the agent iteratively attempts to fix it by invoking a second LLM and providing it with the full history of all previously generated LAMMPS scripts and their associated errors. This iterative procedure occurs until the simulation is successful or until a user-specified limit on the number of iterations is achieved."

## arxiv:2604.24696

**autonomy (executes-and-iterates).** "The current benchmark design requires models to complete each task autonomously from a fixed specification without human intervention."

**config-generation.** "This structure comprehensively tests a wide range of agent capabilities, including fine-grained command composition, complex parameter selection, modality-specific domain knowledge, long-horizon planning across preprocessing stages, and reproducible output validation."

**verification-regression.** "Each task is paired with a hand-crafted evaluation specification that explicitly defines input assumptions ... expected output artifacts (processed images, ROI tables, connectomes, and QC reports), naming conventions, and verifiable checkpoints."

**provenance-reproducibility.** "We also introduce NeuroBench, a benchmark with standardized specifications that assesses executability, output validity, and reproducibility readiness under realistic conditions."

**failure_handling.** "Across major tool and modality skills, NeuroClaw further standardizes post-execution verification through expected-artifact checks, missing-file detection, NaN/Inf screening, quality-control validation, and structured JSONL audit logs."

## arxiv:2606.05050

**autonomy (executes-and-iterates).** "In every case, CatDT received only a bulk crystal structure and a one-sentence natural-language reaction description, with all subsequent modeling performed autonomously."

**topology-construction.** "Agent 1 calls SurFF to predict surface free energies for all Miller-index slabs with an EquiformerV2 backbone, constructs the equilibrium Wulff shape, and returns the top- exposed facets as simulation-ready slabs."

**solver-control.** "Once every elementary step passes validation, a deterministic barrier tool runs two-phase climbing-image NEB on the UMA universal ML potential (Methods). Any barrier outside a physically plausible window triggers a return to Agent 5 for targeted redesign, closing an outer quality-control loop."

**optimisation-loop.** "A Discovery Agent seeded with PDH domain priors proposes a batch of candidate materials, each of which is evaluated by the full CatDT pipeline, and the structured result, comprising turnover frequency (TOF), propylene selectivity, apparent activation energy, and dominant mechanism, is returned as feedback for the next round of selection (Fig. 6 a)."

**results-interpretation.** "Throughout, Agent 7 acts as central coordinator: it sequences all agents through a workflow state machine, manages checkpoints, and produces energy diagrams, structure visualizations, and the final report."

**techno-economic.** "Under representative industrial loadings and May 2026 commodity prices ..., the leading agent-proposed analogues fall 20-130 below the PtSn benchmark in raw material cost, and the cost-per-activity figure of merit (Fig. b) places Ni@ZrO 2 about below the PtSn baseline"

**verification-regression.** "Agent 5 (Validation Auditor) applies a hybrid gate combining deterministic programmatic checks (element-count consistency, atomic overlap 0.8 A, interpolated-path collision detection), a UMA pre-NEB energy screen, and a reasoning-based geometric plausibility review."

**failure_handling.** "At every step of the pipeline, the agents reason about each result rather than calling tools and accepting their outputs: when an NEB run fails to converge or an endpoint is rejected by the deterministic gate, the validation auditor diagnoses overlap, element-count, or path-collision causes and proposes targeted geometric corrections that feed the next iteration."

## arxiv:2602.11689

**autonomy (executes-and-iterates).** "Each run is executed exactly once from its initial prompt with no follow-up instructions or corrective feedback. The only exception to this is when exploring the meshing capabilities of GPT-5.2, where additional iterations of human-guided prompts were applied to refine the mesh generation process."

**config-generation.** "Most of these tasks can be solved by copying a suitable tutorial case and making a small number of dictionary edits (e.g., turbulence model, boundary conditions, or geometry scaling)."

**topology-construction.** "We also tested GPT-5.2 on mesh generation via the Gmsh Python API, as also used in Yue et al. [2025b] , which enabled the creation of hybrid meshes that combine structured outer blocks with an unstructured refined core around the obstacle."

**solver-control.** "After making the required changes, the agent runs the meshing and solver pipeline until the specified endTime is reached."

**failure_handling.** "When errors occur, the agent is directed to use OpenFOAM's error logs to identify the first failure and apply corrective actions needed."

## doi:10.5281/zenodo.22554152

**autonomy (executes-with-approval).** "A physics-classified fix requires a human to supply its exact error code to --approve before it is applied."

**config-generation.** "the agent inspects the deck content, proposes a scratch-probe (a minimal, disposable re-run that tests a hypothesis without committing to a change), and proposes a fix only once the probe confirms it."

**solver-control.** "Solve. Runs the OpenRadioss solver against the repaired deck. Content-addressed caching ensures an identical deck is never re-solved."

**verification-regression.** "Verify. Parses the solver's energy-balance and mass-error diagnostics and gates on them before any score is computed."

**provenance-reproducibility.** "Documentation/Provenance. corridor repair and corridor sweep write a markdown record (repair_writeup.md, <plan.id>_writeup.md) alongside their existing outputs, templated directly from already-computed result data."

**failure_handling.** "Verify. Parses the solver's energy-balance and mass-error diagnostics and gates on them before any score is computed. A model that reaches solver termination but violates energy conservation - the basic physical sanity check for this class of simulation - is not scored as though it were trustworthy."

## doi:10.3389/fchem.2026.1914886

**autonomy (executes-and-iterates).** "Experimental results show that DDA can stably complete the full end-to-end process from target preparation to candidate prioritization, automatically handling tool calls, file format conversions, and abnormal recovery from intermediate steps."

**tool-exposure.** "Tool selection is evaluated by comparing the selected tool set S with a task-specific gold tool set G. We report precision, recall, and F1 as defined in Equation 12"

**config-generation.** "The code-execution suite evaluates the generation and execution of lightweight scientific wrappers using local inputs, declared expected outputs, and required CSV columns or JSON keys."

**verification-regression.** "After normal execution produces candidate products, deterministic validators inspect the final candidate table against the requested delivery count, required molecular fields, and docking-oriented score fields."

**results-interpretation.** "At this stage, DDA records molecule tables, property-prediction tables, docking-result tables, execution status, and failure flags, and aggregates them into ranked candidates, ADMET summaries, docking-oriented scores, recorded execution products, CSV files, and web visualization outputs."

**failure_handling.** "This process is bounded: if the requested delivery contract remains unmet after the configured retry budget is exhausted, the workflow returns an explicit partial-delivery status rather than silently reporting the task as complete."

## doi:10.1109/access.2025.3605803

**autonomy (executes-and-iterates).** "Once the HFSS model is generated, the agent runs a frequency sweep and extracts the resulting S-parameters without manual intervention."

**topology-construction.** "Given textual package specifications, the agent uses a large language model to run the Python script defining the 3D geometry, materials, and excitation ports for HFSS."

**config-generation.** "Set up HFSS simulation projects, including excitation ports, solution setups, and frequency sweeps."

**solver-control.** "Launch a simulation and monitor convergence status."

**surrogate-modelling.** "The agent processes the simulated S-parameters and fits a lumped-element network, producing a SPICE-compatible netlist that captures the QFN's RF behavior."

**results-interpretation.** "Subsequently, it interprets the results to generate a compact equivalent circuit model and produces a SPICE-compatible netlist."

**failure_handling.** NOT FOUND: no statement of what happens when HFSS fails, errors or does not converge. The nearest is the tool description "Launch a simulation and monitor convergence status."

## arxiv:2602.20683

**autonomy (executes-and-iterates).** "The benchmark runner executes the complete agent loop-encompassing tool planning, tool execution, multi-round interaction, and memory-conditioned prompting-rather than evaluating raw model function-calling in isolation."

**tool-exposure.** "The Action Registry exposes simulation capabilities as OpenAI-format function specifications [ 18 ] . The registry comprises eleven tools spanning assessment, analysis, topology queries, and system management."

**solver-control.** "Conditional escalation into dynamic analysis follows: if the request involves an inverter-based resource ( ), the pipeline may invoke a time-domain transient stability simulation ( ). When EMT analysis is enabled for IBR requests, an EMT screening stage ( ) is executed, which evaluates the short-circuit ratio against a configurable threshold (default 3.0)."

**optimisation-loop.** "This tool performs a bisection search over the MW range : at each iteration, a full CIA is executed at the midpoint, the search interval is narrowed based on the resulting approval status, and the procedure terminates when the interval width falls below a configurable tolerance (default: 1 MW)."

**results-interpretation.** "The pipeline produces a structured interconnection impact report comprising per-stage results, violation details, and a final recommendation (approve, reject, or borderline) accompanied by reason codes."

**verification-regression.** "The prompt-level self-correction loop serves as a regression gate over the 56-scenario conversation suite."

**failure_handling.** "Operationally, the intended fail-safe default follows an abstain-and-escalate paradigm: when solver convergence fails, required inputs are missing, or response numerics cannot be grounded, the agent routes to human review rather than issuing an autonomous approval recommendation."

## title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi

**autonomy (executes-and-iterates).** "Note the tool-calling arm even *reasoned about convergence* (ran the sim when it saw a null result) - visible with `--show`."

**tool-exposure.** "A typed tool layer removes that entire failure mode: the model calls `get_stream_data`, `set_block_conditions`, `build_flowsheet_from_spec`, ... and the schema does the rest."

**config-generation.** "`src/flowsheet_builder.py`, `src/flowsheet_spec.py`, `src/flowsheet_normalize.py`, `src/flowsheet_bkp.py` | Declarative spec -> simulatable `.bkp` builder"

**topology-construction.** "**compositional spec incompleteness** - defines the block but omits the feed stream and wiring ('unwired, not simulatable'); across 6 feedback attempts it patches local errors (SPEC_OPT) but never assembles a complete `components+blocks+streams+connections+params` spec"

**solver-control.** "`benz_interro_c0_temp` (C0 outlet T) | hallucinated_path (`Output\TEMP` vs real `B_TEMP`) | (5 calls: get_block_data->saw null->run->re-read 93.3)"

**techno-economic.** "**Techno-economic analysis** - `run_tea` auto-maps arbitrary block names onto the costing nomenclature and computes CAPEX / OPEX / annualized profit on any converged flowsheet."

**provenance-reproducibility.** "The curated logs in `results/*.jsonl` let you inspect and replot the paper's numbers without running Aspen."

**failure_handling.** "**Ground-truth COM crash** (`harness_error`): the evaluator's own Aspen instance occasionally dies under rapid open/close churn (`RPC server unavailable`), ~1 task/full run. **Mitigated** by retry-once on a fresh sandbox subprocess (0 harness-errors in the definitive run)."

## title:mcpsolvermodelcontextprotocolserverforconstraintsolvingsatmaxsatsmtcpaspdp

**autonomy (executes-and-iterates).** "Either way, the solving LLM drives the write -> execute -> verify loop in a persistent IPython kernel ... and must end the solve by calling `submit_code` with the final self-contained program (syntax-checked server-side, never written to disk by the kernel)."

**solver-control.** "the solving LLM drives the write -> execute -> verify loop in a persistent IPython kernel - the `ipython_mcp` server from [agentic-python-coder](https://github.com/szeider/agentic-python-coder) - and must end the solve by calling `submit_code` with the final self-contained program"

**optimisation-loop.** "all 30 bundled test problems solve correctly, including the four `didp` problems (TSPTW, knapsack, weighted tardiness, talent scheduling), each solved to proven optimality in every run."

**tool-exposure.** "**`select_backend(solver)`** sets up a persistent IPython kernel with the backend's solver library and helper functions, and returns the modeling instructions for that backend."

**verification-regression.** "`mcp-solver-bench` runs the bundled test problems in `tests/problems/<solver>/` end-to-end and validates each result against a per-problem `*_ground_truth.py` validator"

**provenance-reproducibility.** "It is never pip-installed into your environment; instead it is injected into each solve-time kernel via `uv run --with mcp-solver==<version>`, alongside the backend's solver library. This keeps the host environment clean and each solve reproducible."

**failure_handling.** "**Statistics** (optional): set `MCP_SOLVER_STATS=/path/to/stats.jsonl` in the server's `env` to log one JSON line per solving episode - tool-call counts, execution failures, submissions, wall time." NOT FOUND: any statement of what happens when a solver fails to find a solution or times out, beyond the step limit.

## title:247simulationloopshowagenticaikeepssubsurfaceengineeringmoving

**autonomy (executes-with-approval).** "Human-in-the-loop (HITL): Despite the high level of autonomy, engineers maintain total supervisory control. They review and approve agent-proposed plans before launching workflows with hundreds of simulation jobs."

**solver-control.** "By acting as a 24/7 orchestration layer, the squad ensures that as soon as one cycle finishes, the data is synthesized, the next parameters are proposed, and the subsequent run is launched immediately-effectively eliminating the idle dead time between iterations."

**optimisation-loop.** "Collaborative planning: A proposer agent suggests optimization strategies (e.g., genetic algorithms vs. particle swarm optimization with certain sets of hyper parameters), while a critic agent refines them via a debate loop."

**hpc-scale-out.** "They review and approve agent-proposed plans before launching workflows with hundreds of simulation jobs."

**results-interpretation.** "Automated data synthesis: A result analyst translates high-dimensional raw data into actionable insights."

**techno-economic.** "The objective was to maximize net present value (NPV) by optimizing the locations of 30 wells."

**failure_handling.** "The agent handles tedious keyword editing and baseline comparisons, while its self-healing logic proactively fixes convergence issues and input errors, with an optional human-in-the-loop, to keep simulations running 24/7."

## title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow

**autonomy (executes-and-iterates).** "The goal of the developed LLM-based workflow is to automate the modeling process with minimum human participation and finally generate an error-free EnergyPlus input file, or IDF file."

**config-generation.** "The case study demonstrates the successful translation of a building description into an error-free EnergyPlus model for the iUnit modular building at the National Renewable Energy Laboratory."

**solver-control.** "If an error is detected, Agent 4 analyzes the .err file from the EnergyPlus simulation, indicated by the placeholder of \"{severe_n_fatal_error_str}\", to identify the problematic class and its object name"

**failure_handling.** "The iterative nature of this process is crucial, as EnergyPlus errors may not appear simultaneously; some errors emerge only after others are resolved. Therefore, Agent 4 retains a form of short-term memory by recalling previous error messages to inform each subsequent iteration, enabling it to progressively eliminate all issues."

## arxiv:2607.18557

**autonomy (executes-with-approval).** "Everything that follows, from mining the papers to the figure that closes the loop (Figure 7 ), happened in a single conversational session, and took approximately one hour and consumed 343K tokens, in which the user wrote no XML and no shell commands."

**config-generation.** "The user describes the desired simulation in plain English, and a team of specialized agents collaborates to produce a schema-valid, physically sane GEOS XML file, backed by real fluid-property and meshing computations rather than by free-form text generation."

**solver-control.** "A 500-year eight-well run completed in 2   minutes 49   seconds, producing 101 reservoir snapshots."

**surrogate-modelling.** "Agents4GEOS was used to generate 200 PUNQ-S3 simulations with sampled variations of the permeability spatial field of the PUNQ-S3 benchmark as represented at Figure 8 (top)."

**results-interpretation.** "Post-processing the results with geos-postprocess subagent enables an overall evaluation of the flow dynamics: gas migrates from the eight dispersed injectors, mixes with the resident brine, and forms a mobile plume at the top of the formation"

**verification-regression.** "Validation against published ECLIPSE and MRST results confirms the fidelity of the GEOS simulations produced by Agents4GEOS, lending confidence to datasets generated at scale through this automated workflow."

**provenance-reproducibility.** "first by following one real session end to end, in which the system reproduces a published PUNQ-S3 CO 2 injection benchmark from a one-sentence request"

**failure_handling.** "GEOS rejected the first input deck with instructions for the simulation twice, that shows that even though the syntax is right and validated, some errors are only caught at running time, and this is where the learning loop earns its keep."

## doi:10.1016/j.softx.2025.102367

**autonomy (executes-and-iterates).** "In each subsection, we briefly describe the goals, human queries, and the agent's actions."

**tool-exposure.** "The MCP server implements a layered architecture with 35 specialized tools spanning model management, editing and analysis, HVAC and other systems configuration inspection, and simulation execution, enabling Large Language Models to interact with EnergyPlus through conversational interfaces."

**config-generation.** "In this demonstration, we consider reducing internal loads through lighting efficiency improvements and envelope modifications to minimize solar heat gain, demonstrating how the MCP tools enable rapid evaluation and implementation of energy-saving measures with built-in validation and error checking (Table 4)."

**solver-control.** "To compare the energy consumption between the baseline and modified models, we conduct comparative simulations of both models."

**results-interpretation.** "We systematically configure output variables to track lighting energy consumption, equipment loads, and solar heat gains, then execute simulations and generate interactive visualizations to assess retrofit effectiveness (Table 5)."

**failure_handling.** NOT FOUND: the paper never says what happens when a simulation fails or does not converge. The nearest statements are that the tools automate model validation and that "the server inherits any limitations present in the underlying EnergyPlus simulation engine."

## doi:10.26868/30680611.2026.1305

**autonomy (executes-and-iterates).** "The simulation runner automatically launches EnergyPlus for the baseline and all modified IDFs, using caching mechanisms to eliminate redundant runs."

**config-generation.** "Agent 2 operationalizes the semantic schema by applying deterministic, rule-based transformations to the identified parameters, producing validated IDF variants without manual intervention."

**solver-control.** "The simulation runner automatically launches EnergyPlus for the baseline and all modified IDFs, using caching mechanisms to eliminate redundant runs."

**results-interpretation.** "Equally important, Agent 3b enhanced explainability by converting numerical outputs into concise textual interpretations that link observed performance shifts to underlying physical causes"

**verification-regression.** "During the iUnit case study, every generated IDF variant successfully passed the Eppy-based syntax validation, achieving a 100% correctness rate."

**provenance-reproducibility.** "The modular execution strategy also ensured full reproducibility: repeated trials under identical user goals produced identical modified IDFs and simulation results, with zero schema drift observed across ten iterations."

**failure_handling.** "All simulations completed successfully except for one intentionally invalid glazing configuration, confirming the system's fault-tolerant behavior."

## doi:10.1080/19401493.2026.2653969

**autonomy (executes-and-iterates).** "By contrast, when orchestrated through the MCP simulation tool within the agentic workflow, the entire batch simulation stage is executed fully automatically and completes in approximately 10 min, substantially reducing human intervention and improving overall modelling efficiency."

**tool-exposure.** "Both paradigms leverage MCP's standardized tool interface but differ in their interaction styles, memory handling, and level of autonomy."

**config-generation.** "Alternative 1 applied the infiltration reduction measure using retrofit_manager with a 50% multiplier, systematically modifying all zone infiltration objects."

**solver-control.** "The _simulation\_manager_ tool executed simulation runs sequentially, completing in approximately 16 s total (3-5 s per model)."

**results-interpretation.** "A parsing agent systematically extracts key indicators from EnergyPlus CSV and ESO outputs, including annual heating and cooling loads and peak demand metrics."

**techno-economic.** "Beyond data visualization, the AI client synthesized cost-effectiveness recommendations directly from simulation results, prioritizing infiltration reduction as the highest ROI measure (delivering 85% of achievable savings at lowest cost)"

**provenance-reproducibility.** "To evaluate computational efficiency and account for LLM non-determinism, the complete workflow was executed 10 times under identical inputs."

**failure_handling.** NOT FOUND: the paper never states what the system does when a simulation fails. The nearest statements are that each run generates "error logs" and that "Agentic workflows provide automation and scalability but require well-specified objectives and robust error handling."

## doi:10.3390/buildings15173190

**autonomy (executes-with-approval).** "The prompt is interpreted by ChatGPT, which extracts engineering intent and encodes it into a structured JSON schema defining geometry, materials, and design actions."

**config-generation.** "The prompt is interpreted by ChatGPT, which extracts engineering intent and encodes it into a structured JSON schema defining geometry, materials, and design actions."

**solver-control.** "By interfacing GPT-4 with OpenSeesPy via MCP (JSON schemas, API interfaces, communication standards), the system allows engineers to specify and evaluate 3D frame structures using conversational prompts, while ensuring computational fidelity and code compliance."

**results-interpretation.** "All configurations are evaluated with respect to compliance with relevant structural performance criteria, particularly storey drift limitations specified in the NEC-15 and ASCE 7-22 standards."

**failure_handling.** "When a runtime error occurs-such as a stiffness matrix singularity or non-convergence-the server identifies the failure stage (input validation, execution, or numerical solution) and delivers both a machine-readable report and a concise human-readable explanation."

## doi:10.3929/ethz-c-000801434

**autonomy (executes-with-approval).** "the CLI agent executes local shell commands (with a whitelisted set of GUI applications and human-in-the-loop confirmation step before running commands)"

**topology-construction.** "topology optimization, document retrieval, HPC job orchestration, and 3D printer control"

**hpc-scale-out.** "an HPC benchmark evaluating end-to-end ML training orchestration on a SLURM cluster"

**tool-exposure.** "a workflow benchmark with seven prompt styles targeting distinct cognitive demands-including direct tool use, semantic disambiguation, conditional branching, and working-memory tasks"

**failure_handling.** "the agent simply ceases to issue subsequent calls" NOT FOUND: no error-recovery or non-convergence policy is described anywhere in the paper.

## doi:10.48550/arxiv.2605.15028

**autonomy (executes-and-iterates).** "Once an error-free parameterization is obtained, a Human-in-the-Loop (HITL) checkpoint allows the user to adjust parameters and their bounds on the fly."

**config-generation.** "The agent also validates the input deck by performing dry runs with the minimum and maximum substituted values; any error (e.g., a non-monotonic relative permeability curve or an arithmetic expression inside a keyword that does not support it) is relayed back, preventing mistakes that the probabilistic model might otherwise make."

**solver-control.** "The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend."

**optimisation-loop.** "Using weighted normalized root mean square error as the objective, PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne."

**results-interpretation.** "We propose PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization."

**failure_handling.** "The agent also validates the input deck by performing dry runs with the minimum and maximum substituted values; any error (e.g., a non-monotonic relative permeability curve or an arithmetic expression inside a keyword that does not support it) is relayed back, preventing mistakes that the probabilistic model might otherwise make."

## doi:10.25417/uic.32994011.v1

**autonomy (executes-and-iterates).** "At iteration t, the optimizer has access to a history of evaluated points...and must select a new candidate"

**optimisation-loop.** "At iteration t, the optimizer has access to a history of evaluated points...and must select a new candidate"

**failure_handling.** "LLM-based methods exhibit noisier trajectories with intermittent exploratory jumps and slower convergence" NOT FOUND: no handling policy for a failed or invalid evaluation is stated.

## doi:10.1016/j.bdes.2026.100042

**autonomy (executes-and-iterates).** "By integrating the diverse features from different open-source packages, the agent can autonomously handle the end-to-end workflow."

**config-generation.** "In this hydrogeophysical application, a user request is first parsed by the Context Input Agent into a normalized workflow configuration with strict JSON fields."

**solver-control.** "The Inversion Agent executed time-lapse inversions, computing resistivity changes relative to the snowmelt baseline."

**uncertainty-quantification.** "Monte Carlo sampling propagates parameter uncertainty through Archie's law, with the ensemble spread (shaded error bars in Fig. 3b, lower panel) narrowing as prior constraints tighten."

**results-interpretation.** "The Report Agent then synthesized geophysical and climate data into synchronized visualizations and performed automated correlation analysis."

**verification-regression.** "The Evaluation Agent scores inversion quality; in evaluation-only mode, it evaluates and recommends, whereas in self-tuning mode, it performs a bounded set of re-inversions by adjusting parameters, retains the best result, and logs the evaluation history for transparency."

**failure_handling.** "Typical failure cases encountered during development include invalid JSON configurations when the LLM returns malformed output and misidentified data formats. These are mitigated by the regex fallback parser, and file parser exceptions."

## doi:10.1039/d5dd00435g

`config-generation` — "A detailed system message was provided to the LAMMPS input creator for enabling the creation of the correct input files to perform these calculations" and "LAMMPS input agent created the input file with the appropriate thermo keywords."

`topology-construction` — "The agentic system initially created the structure using the structure agent" via Atomsk; "the agent began by generating an FCC crystal structure of gold with a 2 × 2 × 2 supercell and a lattice parameter of 4.078 Å."

`solver-control` — "the final step (iii) involves a heating simulation starting from room temperature and ramping up beyond and expected melting point (e.g. by 1000 K). The system is monitored until full melting is observed."

`hpc-scale-out` — "The simulations were executed on the carbon HPC cluster located within the Center for Nanoscale Materials at Argonne ... Carbon HPC uses a torque-based job scheduler", and "After uploading all 192 displacement directories to the HPC system and running them in batch, the forces were collected, and phonon band structure data was generated."

`results-interpretation` — "all the files were downloaded and the log.lammps file was read by the results analysis agent to extract the required quantities and provide a response to the user."

`verification-regression` — "The computed elastic matrix was validated for physical consistency through symmetry checks and Born stability criteria", and the vision agent "has to make is whether a 50 : 50 solid–liquid interface has been created and whether the structure is fully melted."

**autonomy (executes-and-iterates).** "A LAMMPS input script was created to relax the gold structure, but the simulation initially failed due to unrecognized or invalid commands (after read pause 0, then after minimize). These errors were progressively corrected, leading to successful relaxation and generation of a relaxed structure." The loop is closed on the system's own output without a human step, though AG2 "supports human-in-the-loop feedback".

## doi:10.2139/ssrn.7333555

**config-generation.** "Apply theta_k to IDF; Run EnergyPlus -> E_k; compute NMBE_k", with the Diagnosis Agent returning "a prioritised list of 3-5 parameters" per iteration; for PMU Club the agent "raised equipment density stepwise (75.0 -> 85.0 -> 100.0 W/m2, with lighting density reaching 16.0 W/m2)".

**topology-construction.** "Urban 3D geometry is generated from street-level imagery, with orientation-specific window-to-wall ratios refined through facade-aware enhancement", and "Custom Python scripts parse the unified [schema into an] EnergyPlus IDF."

**optimisation-loop.** "theta_k <- Optuna-TPE(B_k, n_trials = 25, seed = 42): // 25 EnergyPlus simulations", run inside a loop bounded by "MAX_ITER = 10".

**uncertainty-quantification.** "A three-layer sensitivity and uncertainty analysis (Morris screening, Sobol decomposition, Monte Carlo propagation) reveals a cohort-level observability gap", and "Sobol indices confirm that envelope parameters have negligible EUI sensitivity (S_T <= 0.005)."

**results-interpretation.** "the LLM-MAS diagnoses simulation-benchmark discrepancies and iteratively narrows the Bayesian optimization search space until convergence"; for MSEE, "Its P1F facade characterization initially pushed the LLM agent toward a high-intensity equipment-density range typical of engineering facilities, whereas its CBECS target (279.8 kWh/m2) is below the education-sector average. This mismatch required iterative downward bound refinement."

**verification-regression.** "Convergence criteria were |NMBE| <= 5% and CV(RMSE) <= 15%, with MAX_ITER = 10. An early-stop heuristic terminated the loop when the last two consecutive CV(RMSE) improvements were each below 0.5%." Plus the Tier 1 gate: "The TuningAgent requests a final LLM plausibility check, which returns an approved flag, a confidence score (0-1), and a concerns list."

**autonomy (executes-and-iterates).** the loop runs EnergyPlus, reads NMBE back, re-diagnoses and re-bounds without a human step - "The system required no manual parameter tuning, no metered data, and no building-specific configuration beyond the IDF and CBECS category." The human-in-the-loop gate is a post-hoc review queue, not an in-loop approval: "the HITL flag triggers review rather than automatic rollback".

## doi:10.26434/chemrxiv.15006587/v1

**tool-exposure.** "An MCP server exposes the simulator as a fixed set of strongly typed tools covering flowsheet synthesis, simulation, and analysis; requests that do not match a tool's declared input format are rejected before they reach the simulator."

**topology-construction.** "A declarative builder constructs, converges, and analyzes a complete flowsheet from a single natural-language description", and "topology tools likewise auto-assign valid block and stream identifiers when none are supplied."

**config-generation.** "A single block-specification tool accepts any valid pair and automatically selects the corresponding Aspen specification flag on the agent's behalf."

**solver-control.** "A design-specification tool meets a target on a calculated quantity - say, a required product purity - by adjusting a manipulated variable outside the simulator through bisection, repeatedly halving the search interval between a lower and an upper bound until the sampled output reaches the target."

**optimisation-loop.** "A companion optimization tool drives an equation-oriented optimizer that maximizes profit subject to a product-purity constraint, executing in an isolated simulator instance so that the agent's active flowsheet is untouched."

**techno-economic.** "A techno-economic analysis tool connects the live simulation to an existing evaluation framework: it detects each block's underlying Aspen model type, maps block names onto the costing nomenclature, assembles a cost configuration from defaults, and returns capital and operating costs, revenue, and annualized profit."

**results-interpretation.** "numerical values carry explicit units resolved against the flowsheet's unit table, and convergence status is returned as a plain-language summary with an explicit converged/not-converged flag."

**verification-regression.** "Both tools enforce a strict honesty discipline: an unconverged simulation is refused rather than costed, and an infeasible purity target is reported as such rather than answered with a fabricated optimum."

**autonomy (executes-and-iterates).** across the 19 scored tasks the model calls tools, reads self-describing errors back and continues without a human step - "an invalid connection request returns the valid ports for the target block ... turning errors into recoverable, in-loop feedback" - and the headline result is measured on end-to-end task completion, "we demonstrated that a compact, locally hosted model can, through these tools alone, construct and converge a rigorous simulation without writing any simulator-control code".
