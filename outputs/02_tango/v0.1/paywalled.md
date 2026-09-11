# Paywalled and otherwise unreachable sources

The subset of admitted sources whose full text this session could not retrieve, in a shape
someone with the right credentials can act on. Written as the run goes; this first version
was written at the step 3a handoff, before the core tier was deep-read, and covers the
sources already known to be blocked. Records are added as step 4 hits further failures.

**Post-report note.** After the report below was first written, fourteen sources were
retrieved by hand into the local PDF store and read. Three of them were on the blocked list
below; their rows have moved to "Recovered by hand" at the end of this file and they are no
longer demoted. The remaining twelve blocked rows are unchanged, and the routes recorded
against them are still the routes that failed. `unreachable.md` records the wider outcome of
that round.

`blocked_by` values are from the controlled list in `reference/SCHEMA_tango.md`.
`bot-protection` is kept separate from `paywall` on purpose: several of the rows below are
not licensing failures at all — the publisher returns HTTP 403 to an automated client
regardless of whether the article is open.

## Established by attempt, not by assumption

Each publisher family below was probed once in this session rather than assumed from the
DOI prefix. What the probe returned:

| Publisher family | Probe | Result |
|---|---|---|
| Wiley (`aiche.onlinelibrary.wiley.com`) | `doi:10.1002/aic.70488` | HTTP 403 to the automated client |
| AIP (`pubs.aip.org`) | `doi:10.1063/5.0330986` | HTTP 403 to the automated client |
| OnePetro / SPE (`onepetro.org`) | `doi:10.2118/232332-MS` | HTTP 403 to the automated client |
| IEEE Xplore (`ieeexplore.ieee.org`) | `doi:10.1109/tii.2026.3669495` | page returned empty, no abstract and no full text |

The 01 run's `outputs/01_landscape/v0.5/unreachable.md` was read first and records the same
outcome for the publisher-DOI, Unpaywall, arXiv and author-copy routes on SEG, IEEE and
Elsevier material, including one gold-open-access paper no route could retrieve. Routes it
already recorded as refused were not spent again.

One blocked record was resolved rather than listed: `doi:10.1002/aic.70488` (AIChE Journal)
is the version of record of `doi:10.48550/arxiv.2603.12813`, whose arXiv full text is
readable. The preprint is admitted as `core` and the journal version is cut `duplicate`, so
nothing is lost and no row is needed here for it.

## The local PDF store was checked

The person running the run pointed the session at `paywalled_paper`, found on this machine
as `~/Downloads/paywalled_paper/` (20 PDFs) and `~/Downloads/paywalled_paper_2/` (8 PDFs, a
subset of the first). Every file was opened and its DOI read off the first two pages with
`pdftotext`, then matched against the admitted set — the filenames are publisher exports
(`1-s2.0-S…-main.pdf` is a ScienceDirect PII, `tle44020142.1.pdf` a DOI suffix), so matching
on names would have found nothing.

- **None of the 16 blocked sources is in the store.** The store holds the 01 run's
  solid-earth material: `spe-229435-ms` and `spe-229716-ms` are different SPE papers from the
  three blocked here, and `3731599.3767402` is a different paper in the same ACM proceedings
  as an admitted record.
- **One admitted `core` source was found there**: `doi:10.1016/j.bdes.2026.100042`
  (*A generalizable automated geophysical agent workflow for accessible subsurface hydrology
  analysis*), local file `1-s2.0-S3050740526000024-main-2.pdf`. It was not on the blocked
  list, but it is now read from disk rather than over the network.

The decision taken was to carry on. The six `core` records still blocked after the store
check were demoted to `tier: context` with `access_status: abstract-only`; their rows stay
below, and `RUN.md` records what the demotions cost.

## Blocked

| identity_key | title | url | venue | blocked_by | tried | local_pdf | would_change |
|---|---|---|---|---|---|---|---|
| `doi:10.2118/229629-ms` | Agentic Framework for Intelligent Surrogate Modeling of Simulator-Driven Workflows | https://doi.org/10.2118/229629-MS | SPE | paywall | publisher DOI; OnePetro landing page; no OA location in the harvest metadata | no | core write-up; it is one of very few sources whose stated subject is an agent orchestrating sampling, simulator execution and adaptive surrogate retraining together, so it bears on `surrogate-modelling`, `optimisation-loop` and `hpc-scale-out` at once. Abstract-only forces `not stated (abstract only)` maturity |
| `doi:10.2118/229905-ms` | Multi-Agentic Generative AI Framework for Accelerating Field Development Planning | https://doi.org/10.2118/229905-MS | SPE | paywall | publisher DOI; OnePetro landing page; no OA location in the harvest metadata | no | core write-up; the abstract names simulation model compliance and well placement optimisation but not what engine is driven or how, which is exactly the `what_it_drives` and `interface` evidence the run is thinnest on |
| `doi:10.2118/232332-ms` | Agentic AI-Driven Geothermal Reservoir Simulation and Optimization Using Surrogate Modelling for Rapid Site Screening | https://doi.org/10.2118/232332-MS | SPE | bot-protection | publisher DOI; OnePetro returned HTTP 403 | no | core write-up; one of only a handful of admitted sources combining `surrogate-modelling`, `optimisation-loop`, `uncertainty-quantification` and `techno-economic` in one system |
| `doi:10.2118/230773-ms` | From Data to Decisions: Harnessing the Potential of Language Based AI in Drilling | https://doi.org/10.2118/230773-MS | IADC/SPE | paywall | publisher DOI; no OA location in the harvest metadata | no | nothing for the touchpoint grid — it is a high-level evaluation, already `context`. Reading it would firm up the periphery/`context` boundary in section 08 and nothing else |
| `doi:10.1063/5.0330986` | Vortex state transitions in deep street canyons enabled by an automated large language model workflow | https://doi.org/10.1063/5.0330986 | Physics of Fluids (AIP) | bot-protection | publisher DOI; pubs.aip.org returned HTTP 403 | no | core write-up; the abstract states an automated LLM workflow drives large-scale parametric CFD, which would be direct `config-generation` plus `hpc-scale-out` evidence with a named engine |
| `doi:10.1109/tii.2026.3669495` | ModSolAgent: Automated Finite Element Code Generation for Abaqus via LLM-Based Agent | https://doi.org/10.1109/tii.2026.3669495 | IEEE Trans. Industrial Informatics | bot-protection | publisher DOI; IEEE Xplore returned an empty page | no | core write-up; Abaqus is named in the title, so `what_it_drives` is already known, but the evaluation, the autonomy rating and the hallucination-handling the abstract gestures at are not |
| `doi:10.1109/icept67137.2025.11157286` | Automated Mesh Generation in FEM: A Novel Approach Using Large Language Models | https://doi.org/10.1109/icept67137.2025.11157286 | IEEE ICEPT 2025 | bot-protection | publisher DOI; IEEE Xplore family established as unreadable by the probe above | no | core write-up; mesh refinement is a `solver-control` surface that few admitted sources touch, and the abstract does not say what mesher or solver is driven |
| `doi:10.1109/e-cargo65996.2025.11139170` | From Digital Twin to Digital Twin Agent | https://doi.org/10.1109/e-cargo65996.2025.11139170 | IEEE | bot-protection | publisher DOI; IEEE Xplore family established as unreadable | no | nothing — a review, already `context` |
| `doi:10.1109/etfa65518.2025.11205636` | An Architecture for Integrating Large Language Models with Digital Twins and Automation Systems | https://doi.org/10.1109/etfa65518.2025.11205636 | IEEE ETFA 2025 | bot-protection | publisher DOI; IEEE Xplore family established as unreadable | no | could support `core` — the abstract promises case studies as proof of concept, which is the difference between an architecture paper and an evaluated system |
| `doi:10.1109/mcomstd.2026.3669229` | Empowering Digital Twins With Agentic AI: Applications, Case Studies, and Limitations | https://doi.org/10.1109/mcomstd.2026.3669229 | IEEE Communications Standards Magazine | bot-protection | publisher DOI; IEEE Xplore family established as unreadable | no | nothing for the grid — a survey, already `context`. Its "limitations" section would be quotable evidence for section 06 if opened |
| `doi:10.1109/sci68648.2025.11333875` | CoMAS-HPC: A Collaborative Multi-Agent System for HPC Administration | https://doi.org/10.1109/sci68648.2025.11333875 | IEEE SCI 2025 | bot-protection | publisher DOI; IEEE Xplore family established as unreadable | no | nothing — admitted `context` under the HPC-operations rule, and reading it would not move it to `core` |
| `doi:10.1109/ticps.2026.3665499` | A Verifiable Digital Twin-Aided AI (DTAI) Agent-Based Production System Framework With Causally Consistent Symbiotic Simulation | https://doi.org/10.1109/ticps.2026.3665499 | IEEE Trans. Industrial Cyber-Physical Systems | bot-protection | publisher DOI; IEEE Xplore family established as unreadable | no | could support `core` — plan verification against a simulation is `verification-regression` evidence, and the abstract says the verification exists but not how it was measured |
| `doi:10.3997/2214-4609.202639027` | Open-DARTS-MCP: An MCP-Based Architecture for Agentic Reservoir Simulation Workflows | https://doi.org/10.3997/2214-4609.202639027 | EAGE | paywall | publisher DOI; no OA location in the harvest metadata; the 01 run recorded the same record as abstract-only | no | core write-up; it compares three MCP server designs against each other, which is the only head-to-head comparison of `tool-exposure` designs in the admitted set |
| `doi:10.3997/2214-4609.202637165` | Conversational and Agentic Workflows for Constructing and Executing Fully-Differentiable Reservoir Simulation Models | https://doi.org/10.3997/2214-4609.202637165 | EAGE | paywall | publisher DOI; no OA location in the harvest metadata | no | core write-up; the abstract describes grid construction, geometry manipulation, heterogeneity generation and well configuration from intent, which is `topology-construction` and `config-generation` evidence with no substitute in the corpus |
| `doi:10.3997/2214-4609.2024637030` | A Framework for Life-cycle Subsurface Uncertainty Quantification | https://doi.org/10.3997/2214-4609.2024637030 | EAGE | paywall | publisher DOI; no OA location in the harvest metadata | no | little — a one-paragraph conference abstract proposing a framework; it would stay `context` |
| `doi:10.3778/j.issn.1673-9418.2508051` | Multimodal Information Fusion-Guided Graphical Interface Code Generation Framework for OpenFOAM | https://doi.org/10.3778/j.issn.1673-9418.2508051 | Journal of Frontiers of Computer Science and Technology | no-full-text-anywhere | publisher DOI; indexed via DOAJ but no retrievable full text in the harvest metadata | no | could support `core`; AutoCode4OF generates OpenFOAM interface code end-to-end and the abstract does not say whether the generated cases were run |

## Not blocked, and why that is worth saying

The 183 admitted sources are dominated by open routes: 68 arXiv, 12 Zenodo, 6 ChemRxiv,
2 OSTI, plus 24 with an open-access PDF location recorded in the harvest metadata and 9
repositories, vendor pages and theses reached over the open web. The 16 rows above are the
whole of what is known to be blocked at the handoff. That is a smaller share than the 01
run's subsurface corpus, and the reason is visible in the corpus itself rather than inferred:
this literature is overwhelmingly preprint-first.

## Added during step 4 — the deep-read pass

Fifteen further `core` records could not be read in full when the original deep-read reached
them.
Every one was demoted to `tier: context` with `access_status: abstract-only` and
`maturity_demonstrated: not stated (abstract only)`, and its `screening.csv` note records
the demotion. The count matters: the core tier fell from 113 to 98, so **13% of the
intended deep-read was lost to access**, all of it after the handoff rather than before it.

**Three of these fifteen were later retrieved by hand and read, and all three supported a
full `core` write-up.** The core tier recovered to 101 and the loss to access fell to 11%.
Their rows are below the table, under "Recovered by hand"; the twelve that remain are listed
here.

Three families dominated the original fifteen and none of them is a paywall in the licensing
sense. ChemRxiv (five rows) and SSRN (three rows) both refuse automated clients outright. Of
the twelve that remain, ChemRxiv accounts for three and SSRN for two; the recovery came entirely
from those two families plus RSC.

| identity_key | title | url | venue | blocked_by | tried | local_pdf | would_change |
|---|---|---|---|---|---|---|---|
| `doi:10.6084/m9.figshare.30931802` | Autonomous multi-agent AI accelerates hydroxide exchange membrane discovery through physics-grounded inverse design | https://doi.org/10.6084/m9.figshare.30931802 | Figshare | no-full-text-anywhere | Figshare API; the deposit is a dataset record whose only narrative is the abstract | no | core write-up, and it is one of the few admitted sources whose agent-proposed candidate was synthesised and measured, so it is the corpus's strongest candidate for a maturity above M3. Abstract-only forces `not stated (abstract only)` |
| `title:agenticaienabled…` | Agentic AI-Enabled Physics-Informed Machine Learning Framework for Intelligent Building Modeling, Control, and Automation | https://surface.syr.edu/etd/2334 | Syracuse University | bot-protection | institutional repository record page (abstract retrieved in full); the full-text PDF returned HTTP 403 to every client tried, including a reader proxy | no | core write-up; the abstract reports a 6,156-run agentic benchmark, which would be the largest single evaluation in the corpus, but the orchestration modes it compares and the failure behaviour are in the unreadable chapters |
| `doi:10.1016/j.net.2026.104573` | Embedding Bayesian optimization in a multi-agent large language model framework for critical heat flux modeling with uncertainty quantification | https://doi.org/10.1016/j.net.2026.104573 | Nuclear Engineering and Technology | bot-protection | publisher DOI; Elsevier/ScienceDirect established as unreadable to automated clients | no | core write-up; it is one of only three admitted sources tagged `uncertainty-quantification`, and the only one that reports calibrated coverage against a human-expert pipeline on the same search |
| `doi:10.26434/chemrxiv-2025-f1wcr` | Honegumi RAG Assistant: An Agentic System for Accelerating Bayesian Optimization Adoption in Experimental Sciences | https://doi.org/10.26434/chemrxiv-2025-f1wcr | ChemRxiv | bot-protection | publisher DOI; chemrxiv.org established as unreadable | no | modest; the abstract already states the system generates rather than runs optimisation code, which fixes its `autonomy` at `suggests`. Reading it would settle whether the generated pipelines were executed |
| `doi:10.26434/chemrxiv.15005838/v1` | Raven: agentic AI for materials discovery enabled by post-trained chemistry LLMs | https://doi.org/10.26434/chemrxiv.15005838/v1 | ChemRxiv | bot-protection | publisher DOI; chemrxiv.org established as unreadable | no | core write-up; replayable state-graph orchestration is the corpus's clearest `provenance-reproducibility` design and the abstract gives no evaluation numbers at all |
| `doi:10.1016/j.jma.2025.08.021` | From LLM to Agent: A large-language-model-driven machine learning framework for catalyst design of MgH2 dehydrogenation | https://doi.org/10.1016/j.jma.2025.08.021 | Journal of Magnesium and Alloys | bot-protection | publisher DOI; Elsevier/ScienceDirect established as unreadable | no | little for the grid — the abstract makes clear the agent advises rather than drives, so it would stay `context` on the autonomy axis even if read |
| `doi:10.5281/zenodo.20388035` | Open FEM Agent: A Multi-Solver MCP Server for LLM-Driven Computational Mechanics | https://doi.org/10.5281/zenodo.20388035 | Zenodo | no-full-text-anywhere | Zenodo API returned **HTTP 410, a tombstone: the record has been deleted by its owner**. No other copy exists | no | nothing that is not already covered. This is the seven-solver predecessor of the eight-solver OASiS deposit, which is admitted `core` and read in full under the same `system_id`, so the system is in the grid at its later version |
| `doi:10.2139/ssrn.6672588` | VirtualLab_CC: An LLM-Augmented Virtual Laboratory for Automated Computational Chemistry Research | https://doi.org/10.2139/ssrn.6672588 | SSRN | bot-protection | publisher DOI; SSRN established as unreadable to automated clients | no | core write-up; it is one of very few admitted sources that gates every critical decision on a human and still reports autocorrected cluster failures, which is exactly the `failure_handling` evidence the corpus is thinnest on |
| `doi:10.1145/3785462.3815873` | BioCodex: HPC-Native Agentic Genomics Workflows via MCP RunSpecs and Asynchronous Slurm Execution | https://doi.org/10.1145/3785462.3815873 | ACM | paywall | publisher DOI; ACM Digital Library; no OA location in the harvest metadata | no | core write-up; hash-verified run specifications rejected before scheduling is a `provenance-reproducibility` mechanism with no equivalent elsewhere in the corpus, and the overhead figures are not in the abstract |
| `doi:10.26434/chemrxiv.15002405/v1` | Q-planner: a harness system for quantum chemistry agents | https://doi.org/10.26434/chemrxiv.15002405/v1 | ChemRxiv | bot-protection | publisher DOI; chemrxiv.org established as unreadable | no | core write-up; it is the only admitted source whose central claim is that the agent should be kept *out* of the execution loop, and the abstract gives the token numbers but not the failure behaviour |
| `doi:10.26434/chemrxiv.15007941/v1` | From Black Box to Dialogue: An MCP Server for Tanabe–Sugano Diagrams | https://doi.org/10.26434/chemrxiv.15007941/v1 | ChemRxiv | bot-protection | publisher DOI; chemrxiv.org established as unreadable | no | little; the abstract is unusually complete and the source is a proof-of-concept solver wrapper with no scored evaluation, so it would stay `context` |
| `doi:10.2139/ssrn.6942178` | Closed-Loop LLM-Guided Molecular Dynamics Screening of Thermal Transport in Co-Cr-Ni Medium-Entropy Alloys | https://doi.org/10.2139/ssrn.6942178 | SSRN | bot-protection | publisher DOI; SSRN established as unreadable | no | core write-up; 300 simulator evaluations inside an agent-driven loop is among the larger closed-loop campaigns in the corpus, and the abstract reports that the search did *not* converge monotonically — a negative result whose discussion is unreadable |

## Recovered by hand

Three of the fifteen step-4 demotions were retrieved by hand into the local PDF store after
the report below was first written, read in full, and promoted back to `tier: core` with
`access_status: full-text`. Their `screening.csv` notes record the promotion.

| identity_key | title | url | venue | blocked_by (originally) | tried | local_pdf | what reading it changed |
|---|---|---|---|---|---|---|---|
| `doi:10.1039/d5dd00435g` | Multi-agentic AI framework for end-to-end atomistic simulations | https://doi.org/10.1039/d5dd00435g | Digital Discovery (RSC) | bot-protection | publisher DOI and PDF (HTTP 403, Cloudflare); a reader proxy (CAPTCHA); the ScienceDirect RSC mirror; OpenAlex; Europe PMC; OSTI; arXiv | `d5dd00435g.pdf` | everything. This record originally carried `tango_touchpoints: none` and `not stated` in every column because no route returned narrative text. The version of record is a full CC-BY paper: a multi-agent AutoGen/AG2 system driving LAMMPS on the Argonne Carbon cluster through Atomsk, Phonopy and OVITO, with an HPC agent doing SCP and torque submission. Rated `M1` against a human-expert baseline, now carrying six touchpoints |
| `doi:10.2139/ssrn.7333555` | Geo2UBEM: 3D Geometry Abstraction and LLM Multi-Agent Parameter Inference for Automated Urban Building Energy Modeling | https://doi.org/10.2139/ssrn.7333555 | SSRN Electronic Journal | bot-protection | publisher DOI; SSRN established as unreadable; no abstract in any harvested API record either | `ssrn-7333555.pdf` | everything. This record originally had nothing beyond the title. The preprint is a three-agent orchestrator/diagnosis/tuning system driving EnergyPlus 23.2 through an Optuna TPE loop at 25 runs per pass on six named Purdue University buildings, validated against metered energy-use intensities held back until after calibration. Rated `M3`, and the corpus's fourth `uncertainty-quantification` core row |
| `doi:10.26434/chemrxiv.15006587/v1` | Autonomous Flowsheet Synthesis, Simulation, and Analysis with a Locally Deployed Language Model Agent | https://doi.org/10.26434/chemrxiv.15006587/v1 | ChemRxiv | bot-protection | publisher DOI; chemrxiv.org established as unreadable to automated clients | `chemrxiv.15006587%2Fv1.pdf` | less than the two above, as predicted at the time: the system was already in the grid through the authors' repository under the same `system_id`, so no system entered or left the corpus. What it added is the peer-review-facing evidence — the models named as Qwen2.5-32B-Instruct and 14B-Instruct, the 19-task benchmark structure, the six-way failure taxonomy, and the finding that iterative error feedback recovered hallucinated variable paths in zero of thirty instances. Rated `M2` |

The `would_change` column above had predicted "everything" for the first two and "little,
uniquely" for the third. All three predictions held.

## One blocked source was recovered from the local store

`doi:10.1016/j.bdes.2026.100042` (GAGAW) was reported unreadable by every online route the
delegated reader tried — publisher HTTP 403 directly and through a reader proxy, the
preprint server returning bot verification, and the preprint PDF host failing DNS. It was
**not** demoted. The local store flagged at the step-3a handoff holds the version of record
as `1-s2.0-S3050740526000024-main-2.pdf`, and it was read from there and written as a full
`core` record with `access_status: full-text`. It is the one case in this run where the
local store changed an outcome, and it is worth stating plainly: without it the corpus would
have lost its only source driving a geophysical inversion code.

## The other abstract-only sources, which are abstract-only by decision

The rows above are access failures. The 55 sources below are not: they were admitted at
`tier: context` during screening, and `context` means abstract-only by design — a one-line
annotation from the abstract, no deep read attempted, no full text sought. They are listed
here because `access_status: abstract-only` is the same value in both cases and a reader
checking the grid cannot otherwise tell the two apart. **None of these was blocked, so none
carries a `blocked_by` value**, and none belongs in the count of what credentials would fix.

They are `context` for one of three reasons, all recorded in each row's `screening.csv`
note: the source is a review, survey or position piece rather than a system; the source is a
conference abstract, thesis record or vendor announcement whose visible material cannot
support a `core` write-up; or the source is periphery-adjacent — a benchmark or a repository
whose agent drives something this run counts but whose evaluation is not reported.

- `title:runspecspectreaiagenticgenerationanditerationofopmflowreservoirsimulationdecks` — RUNSPEC / SpectreAI: agentic generation and iteration of OPM Flow reservoir simulation decks (runspec.io, 2026)
- `title:synopsyslaunchesansys2026r1meshagentdiscoveryvalidationagentandengineeringcopilot` — Synopsys Launches Ansys 2026 R1: Mesh Agent, Discovery Validation Agent and Engineering Copilot (Synopsys newsroom, 2026)
- `doi:10.1007/s10270-025-01306-0` — AI simulation by digital twins: systematic survey, reference framework, and mapping to a standar (Software & Systems Modeling, 2025)
- `doi:10.1007/s44212-025-00099-3` — Towards Agentic Urban Digital Twins (AUDiTs): advancing new urban science through Human-AI co-le (Urban Informatics, 2026)
- `doi:10.1016/j.apenergy.2025.126670` — A systematic review of transformers and large language models in the energy sector: towards agen (Applied Energy, 2025)
- `doi:10.1016/j.array.2026.100721` — Integrating agentic AI and digital twins for intelligent decision-making systems (Array, 2026)
- `doi:10.1016/j.coche.2025.101150` — Industrial Agentic AI and generative modeling in complex systems (Current Opinion in Chemical Engineering, 2025)
- `doi:10.1016/j.enbuild.2024.114788` — Advancing building energy modeling with large language models: Exploration and case studies (Energy and Buildings, 2024)
- `doi:10.1080/00207543.2026.2630277` — Agentic digital twins: bridging model-based and AI-driven decision-making support for a new era  (International Journal of Production Research, 2026)
- `doi:10.1145/3731599.3767584` — Evaluating the Efficacy of LLM-Based Reasoning for Multiobjective HPC Job Scheduling (arXiv (Cornell University), 2025)
- `doi:10.1145/3785462.3815852` — Empowering Cancer Researchers: An Agentic AI System for Intuitive Interaction with High-Performa (not stated, 2026)
- `doi:10.13031/ja.16663` — Frontier: LLM-Driven Agentic Digital Twins for Dairy Housing: From Data-Rich Facilities to Intel (Journal of the ASABE, 2026)
- `doi:10.1371/journal.pone.0353610` — Agentic AI-enhanced digital twins for Smart City civil infrastructure: A secure, autonomous and  (PLoS ONE, 2026)
- `doi:10.1609/aaai.v39i28.35373` — Agentic AI for Digital Twin (Proceedings of the AAAI Conference on Artificial Intelligence, 2025)
- `doi:10.3389/frai.2025.1655470` — Generative and Predictive AI for digital twin systems in manufacturing (Frontiers in Artificial Intelligence, 2025)
- `doi:10.3390/a19030218` — A Self-Deciding Adaptive Digital Twin Framework Using Agentic AI for Fuzzy Multi-Objective Optim (Algorithms, 2026)
- `doi:10.3390/data11070180` — From Scientific Copilots to Tool-Grounded Autonomy: AI Agents in Simulation-Driven Materials Dis (Data, 2026)
- `doi:10.3390/electronics14244806` — A Dual Digital Twin Framework for Reinforcement Learning: Bridging Webots and MuJoCo with Genera (Electronics, 2025)
- `doi:10.3390/electronics15091869` — Integrating Conversational AI Agents with Digital Twins: A Systems Engineering Approach to Compl (Electronics, 2026)
- `doi:10.3390/smartcities8010028` — AI Agent-Based Intelligent Urban Digital Twin (I-UDT): Concept, Methodology, and Case Studies (Smart Cities, 2025)
- `doi:10.5194/egusphere-egu26-15002` — Toward Federated Agentic Workflows for Numerical Weather Prediction With Chiltepin (not stated, 2026)
- `doi:10.5194/wbf2026-553` — AI inference service in Digital Twins (not stated, 2026)
- `doi:10.54941/ahfe1007674` — Agentic LLMs for Scalable, Verifiable System Health Digital Twins (AHFE international, 2026)
- `doi:10.67294/knpyhb26` — Conceptualizing Cognitive and Agentic Digital Twins (International Multidisciplinary Journal of Emerging Technologies and Applications, 2026)
- `title:agenticaienabledphysicsinformedmachinelearningframeworkforintelligentbuildingmodelingcontrolandautomation` — AGENTIC AI-ENABLED PHYSICS-INFORMED MACHINE LEARNING FRAMEWORK FOR INTELLIGENT BUILDING MODELING (Syracuse University Libraries (Syracuse University), 2026)
- `arxiv:2506.11057` — STRCMP: Integrating Graph Structural Priors with Language Models for Combinatorial Optimization (arXiv, 2025)
- `arxiv:2509.08269` — A Systematic Survey on Large Language Models for Evolutionary Optimization: From Modeling to Sol (arXiv, 2025)
- `arxiv:2603.25898` — On Integrating Resilience and Human Oversight into LLM-Assisted Modeling Workflows for Digital T (arXiv (Cornell University), 2026)
- `arxiv:2605.00803` — Can Coding Agents Reproduce Findings in Computational Materials Science? (arXiv (Cornell University), 2026)
- `arxiv:2607.18485` — Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Com (arXiv (Cornell University), 2026)
- `arxiv:2608.03600` — Large language models for partial differential equation workflows (arXiv (Cornell University), 2026)
- `arxiv:2609.03598` — RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters (arXiv (Cornell University), 2026)
- `doi:10.17605/osf.io/w4sc9` — Agentic Digital Twins in Health Care: A Scoping Review (not stated, 2026)
- `doi:10.2196/preprints.87374` — Building Personalized Digital Twins from Public Health Data: An Agentic AI and Ontology-Guided F (not stated, 2025)
- `doi:10.26153/tsw/62180` — X2Sim (Texas Digital Library (University of Texas), 2025)
- `doi:10.26190/unsworks/32312` — Transforming Water and Wastewater Treatment with Digital Twins (UNSWorks (University of New South Wales, Sydney, Australia), 2026)
- `doi:10.26434/chemrxiv.15005632/v1` — Dual Digital Twins for Experimental Planning in Automated Laboratories: Physics-informed surroga (ChemRxiv, 2026)
- `doi:10.36227/techrxiv.175979241.11582889/v1` — Explainability as a Catalyst for Agentic AI Adoption in Subsurface Oil & Gas Workflows (not stated, 2025)
- `doi:10.48550/arxiv.2409.11363` — CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibil (arXiv (Cornell University), 2024)
- `doi:10.48550/arxiv.2505.10852` — MatTools: Benchmarking Large Language Models for Materials Science Tools (arXiv (Cornell University), 2025)
- `doi:10.48550/arxiv.2512.09209` — Beyond Algorithm Evolution: An LLM-Driven Framework for the Co-Evolution of Swarm Intelligence O (arXiv (Cornell University), 2025)
- `doi:10.48550/arxiv.2601.01321` — Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models (arXiv (Cornell University), 2026)
- `doi:10.48550/arxiv.2601.03513` — Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day (arXiv (Cornell University), 2026)
- `doi:10.48550/arxiv.2607.10081` — Descriptive Execution of HPC Applications and Workflows (arXiv (Cornell University), 2026)
- `doi:10.48550/arxiv.2609.00795` — Agentic programs: an emerging form of scientific software in computational materials science (arXiv (Cornell University), 2026)
- `doi:10.5281/zenodo.20054226` — Agricultural AI Agents Can Learn from Chemical Complex System Models (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `doi:10.5281/zenodo.20055953` — Autonomous HPC Simulation Orchestration: Surveying Multi-Agent LLM Ecosystems and the NVIDIA Mod (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `doi:10.5281/zenodo.20109894` — Agentic Optimizer: Multi-Agent LLM-Feedback-Driven AI Architecture for Subsurface Physics, Fluid (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `title:aplatformforprescriptivedigitaltwinsinaec` — A Platform for Prescriptive Digital Twins in AEC (TSpace (University of Toronto), 2026)
- `title:intelligentdigitaltwinsystemforurbanmobility` — Intelligent Digital Twin System for Urban Mobility (Scholars Commons (Wilfrid Laurier University), 2026)
- `doi:10.5281/zenodo.21841882` — Artifact for ""Works but Wrong: Domain Tools Sharpen AI Diagnosis of HPC Simulation Setup Errors (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `doi:10.5281/zenodo.21841883` — Artifact for ""Works but Wrong: Static Diagnosis of HPC Simulation Setup Errors for AI Agents"" (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `doi:10.5281/zenodo.21854862` — AOBench: a role-aware, RBAC-enforced benchmark for LLM agents in HPC operations (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `doi:10.5281/zenodo.21938270` — Open Modeling Foundation Agent Skills Alpha Release v2026.08 (Zenodo (CERN European Organization for Nuclear Research), 2026)
- `title:openfoammcpopenfoammcpserverforreadingandmodifyingopenfoamconfigurationfiles` — openfoam-mcp: OpenFOAM MCP server for reading and modifying OpenFOAM configuration files (GitHub, 2026)
