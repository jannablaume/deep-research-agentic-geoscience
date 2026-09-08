# 06 Disagreement

Where core full texts contradict each other on a matter of fact or method, not where they
study different tasks.

[Certain] Authors disagree on whether a retrieval-then-synthesize agent should answer
aggregate statistical questions. The GraphRAG catalog paper states that precise-statistics
queries remain weak (0.50–1.04/3) because of "a fundamental structural flaw in
retrieval-then-synthesize architectures when handling aggregate or ranking tasks", and
recommends routing those questions to deterministic database queries
[[doi:10.48550/arxiv.2607.24984]]. TADI's design is the opposite choice: twelve tools
including SQL over DuckDB, with the LLM selecting tools for multi-step arithmetic, and
the author states that multi-step arithmetic across tool results "may accumulate errors"
[[doi:10.48550/arxiv.2605.00060]]. Both papers are seismology-adjacent catalog or
operational-record systems; they do not cite each other.

[Certain] Authors disagree on whether a vision-language model can replace a specialised
vision stack for geohazard mapping. LandslideAgent reports that LandslideVLM's 52.05%
fine-grained accuracy "still lags significantly behind the dedicated pure-vision models"
and that VLMs "cannot yet entirely supplant specialized interpretative models"
[[doi:10.48550/arxiv.2606.18661]]. STA-CoT reports the highest Pos.F1 / Avg.F1 / MCC
on MineBench against MCoT, RAG and MineAgent using Gemini-2.0 and GPT-4o with a visual
toolkit [[doi:10.18653/v1/2025.findings-emnlp.1386]]. The tasks differ (landslide scene
classification versus multi-image mineral deposit identification), so the two results are
not a head-to-head; they are opposing stances on how far a VLM agent currently goes in
geoscientific imagery.

[Certain] Authors disagree on how much of the scientific claim belongs to the LLM versus
the wrapped engine. GeoMCP states that the framework "does not eliminate the potential for
reasoning or data extraction errors" because the LLM still interprets the scenario and
extracts parameters [[doi:10.48550/arxiv.2603.01022]]. TRACE describes a "dual-ceiling
effect" in which seismological tool precision sets the operational baseline while
scientific rigour is capped by the LLM's reasoning depth
[[doi:10.48550/arxiv.2603.21152]]. Agents4GEOS states that every quantity returned to the
user "results from an actual computation rather than from text generation"
[[arxiv:2607.18557]]. AutoSurrogate goes further in the other direction: after training,
the deployed object is a neural surrogate and the LLM is no longer in the forward map
[[doi:10.1016/j.aei.2026.105058]]. The first two locate residual error in the LLM; the
third locates the numeric payload entirely in the tool; the fourth locates the payload in
a trained network that the agent only constructed.

[Likely] No core pair reports a contradictory number on the same dataset. The
disagreements above are about architecture and about where responsibility for error sits,
not about a contested empirical result.
