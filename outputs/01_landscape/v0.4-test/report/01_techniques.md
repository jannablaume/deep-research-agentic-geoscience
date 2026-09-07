# Techniques

Constrained tool-calling inside a graph of predefined nodes is the pattern stated for TREMORS: the LLM parses a natural-language request into a schema, then LangGraph routes FDSN/ObsPy calls [[doi:10.48550/arxiv.2609.01777]]. [Certain]

Iterative self-check with structured output appears in the Devito translator: Pydantic contracts and a quality-score router decide whether to pass, refine, or reject a conversion [[arxiv:2601.18381]]. [Certain]

Role-specialised multi-agent planning is stated for TRACE: a planning agent decomposes a request, a coding agent links seismological modules, and checking agents validate physical consistency, with optional human supervision [[doi:10.48550/arxiv.2603.21152]]. [Certain]

Retrieval (GraphRAG over a Devito knowledge graph; RAG inside GAIA) is reported alongside tool-calling rather than as a standalone chatbot [[arxiv:2601.18381]] [[arxiv:2511.03852]]. [Likely]

Abstract-only industry papers name agentic RAG and A2A for subsurface workflows without enough visible text in this run to characterise the loop [[doi:10.2523/iptc-25122-ms]] [[doi:10.3997/2214-4609.202410350]]. [Certain]
