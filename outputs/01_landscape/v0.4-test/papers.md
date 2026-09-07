# papers.md — evidence trail for tier: core sources

Smoke-test run. Three core papers with full text retrieved in this run.

## arxiv:2601.18381

https://arxiv.org/html/2601.18381 — fetched via arxiv.org/html full text.

"this study develops an integrated AI agent framework. Retrieval-Augmented Generation (RAG) and open-source Large Language Models are combined through multi-stage iterative workflows in the system’s hybrid LangGraph architecture."

"The agent constructs an extensive Devito knowledge graph through document parsing, structure-aware segmentation, extraction of entity relationships, and Leiden-based community detection."

"The evaluation employs eleven benchmark queries designed to represent common information retrieval demands arising during the code conversion process."

"The evaluation yields a Precision@5 value of 0.964 and a Recall@5 value of 0.930."

"The assessment indicates strong system performance, with a Grade-A success rate of 76.9%."

"its capabilities for advanced data mining and pattern discovery remain limited. Additionally, the existing quality evaluation framework relies on fixed, predefined thresholds, such as excellent_threshold=0.85 and acceptable_threshold=0.55."

## doi:10.48550/arxiv.2609.01777

https://arxiv.org/html/2609.01777 — fetched via arxiv.org/html full text.

"We present TREMORS (Text Referenced Event Mapping and Output Renderer for Seismographs), an agentic framework that uses large language model reasoning within a constrained execution graph to automate seismic data retrieval."

"In this application we use gpt-oss:120b that contains 120 billion parameters"

"The TREMORS agent requires a backend and interfaces with FDSN web services through the ObsPy API"

"Example workflows demonstrate support for both event-based and continuous waveform acquisition."

"Despite its practical utility, TREMORS is subject to limitations. While the chosen agentic framework reduces uncertainty associated with natural-language interpretation, it does not eliminate it. The semantic parsing stage may fail for ambiguous, imprecise, or unusually phrased prompts."

"TREMORS depends on external FDSN services and ObsPy-compatible interfaces, making it sensitive to heterogeneous metadata standards, incomplete station information, service outages, and variability across datacenters."

## doi:10.48550/arxiv.2603.21152

https://arxiv.org/html/2603.21152 — fetched via arxiv.org/html full text.

"Here we present TRACE (Trans-perspective Reasoning and Automated Comprehensive Evaluator), a multi-agent system that combines large language model planning with formal seismological constraints"

"Applied to the 2019 Ridgecrest sequence, TRACE autonomously identifies stress-perturbation-induced delayed triggering, resolving the cascading interaction between the Mw 6.4 and Mw 7.1 mainshocks"

"GPT-5 is implemented as the primary foundation model for all constituent agents within the TRACE framework."

"A specialized Planning Agent decomposes the request into structured protocols, which are overseen by human supervision"

"the efficacy of TRACE remains intrinsically bounded by the fidelity of underlying physical models and the computational cost of high-fidelity simulations. Furthermore, its performance under extreme or data-sparse seismic events requires further validation"
