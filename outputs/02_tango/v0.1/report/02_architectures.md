# 02 Architectures

Recurring designs and what each is chosen for, from the 98 `core` rows unless stated. Counts
are per `papers.csv` row.

## The distribution

[Certain] Across all 183 rows: `multi-agent-hierarchical` 47, `pipeline-with-agent` 30,
`agent-plus-simulator` 26, `multi-agent-flat` 22, `single-agent` 22, `not stated` 21,
`agent-plus-solver` 12, `agent-plus-database` 2, `router` 1. Restricted to the 98 core rows,
where the label rests on a read architecture section rather than an abstract:
`multi-agent-hierarchical` 38, `multi-agent-flat` 17, `agent-plus-simulator` 14,
`pipeline-with-agent` 12, `single-agent` 9, `agent-plus-solver` 6, `agent-plus-database` 1,
`not stated` 1. Twenty of the 21 `not stated` rows are context rows: an abstract that says
"multi-agent" does not say how the agents relate.

## Hierarchical multi-agent: the default

[Certain] A supervisor decomposing a goal and dispatching to role-specialised workers is the
most common design in the corpus at 38 of 98 core rows, and the roles recur across unrelated
domains. A four-agent chain of description pre-processing, object extraction, object generation
and debugging for building energy models
[[title:automaticbuildingenergymodeldevelopmentanddebuggingusinglargelanguagemodelsagenticworkflow]];
a pre-checker, generator, runner and corrector for CFD [[doi:10.1016/j.taml.2025.100594]];
reviewer, planner, parameterizer, optimizer, simulator and summarizer for reservoir history
matching [[doi:10.48550/arxiv.2605.15028]]; a coordinator sequencing eight specialists through a
workflow state machine for catalysis [[arxiv:2606.05050]]. The recurring quartet is
**plan, generate, run, repair**, and it appears under different names in flowsheet, CFD,
reservoir, building-energy and materials work alike.

[Certain] The reason given for the hierarchy is usually context management rather than
capability. One source dispatches each subagent "as an independent agent instance whose
definition pins the model matching its tier, so mesh and fluid computations actually run on a
mid-sized model while the independent review runs on the most capable one"
[[arxiv:2607.18557]]. Another allocates GPT-5 to schema construction and a cheaper model to
repeated result interpretation [[doi:10.1080/19401493.2026.2653969]]. A third confines model
invocations to three bounded stages so that context does not grow with workflow length
[[doi:10.26434/chemrxiv.15002405/v1]].

[Certain] The corpus also contains a measured argument *against* elaborate orchestration. One
benchmark reports that the fully agentic orchestrator was competitive but not superior to
simpler modular pipelines [[doi:10.48550/arxiv.2601.20996]]. Another reports that workflow
validity depends more on the backbone than on the structure, with open-source four-billion
parameter models reaching 55–78% task completion where proprietary models reach 96–97% on the
same harness [[doi:10.3929/ethz-c-000801434]]. A third reports that "many LLMs consistently
produce five-step workflows often including useless or redundant steps"
[[doi:10.48550/arxiv.2506.05616]].

## Agent-plus-simulator and agent-plus-solver: the thin wrapper

[Certain] 20 core rows put a single agent against a single engine with no internal agent
society at all: 14 `agent-plus-simulator` and 6 `agent-plus-solver`. This is the design chosen
when the contribution is the *interface* rather than the policy — an MCP server exposing 35
tools over a building-energy engine [[doi:10.1016/j.softx.2025.102367]], 42 typed tools over a
process simulator
[[title:aspenplusmcpanmcpserveroftypedschemaconstrainedtoolsovertheaspenpluscomapi]], 11 tools
over four power-system engines [[arxiv:2602.20683]], a solver exposed so a client "operates the
solver rather than merely describing it" [[doi:10.26434/chemrxiv.15007941/v1]], a JSON schema
carrying geometry and materials to a finite-element library
[[doi:10.3390/buildings15173190]].

[Certain] Several of these papers say so directly: the deliverable is the tool layer and the
agent policy is deliberately left to whoever connects. One is "model-agnostic" by design and
lists five compatible clients [[doi:10.5281/zenodo.20543501]]; another stresses that its design
"allows the EnergyPlus-MCP server to work seamlessly with any MCP-compatible LLMs"
[[doi:10.1016/j.softx.2025.102367]]. The corresponding weakness is also stated: such a paper
can report what the tools are and not what an agent achieves with them, and one of them has no
quantitative result at all [[doi:10.1016/j.softx.2025.102367]].

## Pipeline-with-agent: the model inside a deterministic frame

[Certain] 12 core rows invert the usual arrangement: the workflow is a fixed deterministic
pipeline and the language model occupies one or two named slots inside it. A semantic
interpreter feeding a rule-based modifier and a rule-based runner
[[doi:10.26868/30680611.2026.1305]]; a deterministic executor consuming zero model tokens
during execution [[doi:10.26434/chemrxiv.15002405/v1]]; a static human-authored risk taxonomy,
"deliberately outside the model's reach", classifying every solver error before the agent is
allowed to act [[doi:10.5281/zenodo.22554152]]; a supervisor confining "LLM stochasticity to
recoverable workflow steps while keeping Bayesian optimization deterministic and reproducible"
[[doi:10.1016/j.net.2026.104573]].

[Certain] The claimed benefit is always reproducibility, and two sources measure it: repeated
trials under identical goals "produced identical modified IDFs and simulation results, with
zero schema drift observed across ten iterations" [[doi:10.26868/30680611.2026.1305]], and a
replay yielding "bitwise-identical outputs without re-executing prior actions"
[[doi:10.48550/arxiv.2601.09749]]. Against that, one source in this group reports a residual:
"because parameter recommendation is mediated by an LLM, minor variability can occur in the
ordering of lower-ranked parameters across repeated runs"
[[doi:10.26868/30680611.2026.1305]].

## Single-agent: a general coding agent pointed at a solver

[Certain] 9 core rows use one general-purpose agent with shell and file tools and no
domain-specific agent architecture at all — the contribution is the configuration, the skill
library or the prompt rather than the system. A lightweight prompt configuration guiding an
off-the-shelf coding agent toward tutorial reuse and log-driven repair, which took completion
from 4 of 9 to 9 of 9 runs on the same benchmark [[arxiv:2602.11689]]; commercial coding agents
used directly on a leadership-class machine [[doi:10.20944/preprints202608.1323.v1]]; a skill
library layered over a general agent [[doi:10.48550/arxiv.2605.24002]]. One benchmark reports
that a bare frontier coding agent produced 15 of 60 sound runs against 56 of 60 with the
domain skill installed [[arxiv:2606.05050]], and another that a general coding agent "failed to
yield executable scripts for any of the 20 local two-point-function tasks"
[[doi:10.48550/arxiv.2607.15001]].

## Techniques, across architectures

[Certain] Technique counts over the 98 core rows: tool-calling 95, code-execution 70,
role-specialisation 62, guardrails-validation 62, task-decomposition 61, simulator-in-the-loop
54, planning 53, retrieval 51, self-reflection 51, human-in-the-loop 42, memory 39,
physics-solver-in-the-loop 30, fine-tuning 5, knowledge-graph 5, router 3, multi-agent-debate 3,
instrument-control 1.

[Certain] Two of those numbers are worth stating together. `guardrails-validation` appears in
62 of 98 core systems — more often than planning — which is consistent with what section 01
found about where these systems spend their engineering. `fine-tuning` appears in 5, so the
corpus is overwhelmingly built on prompting and scaffolding around unmodified models. Where
fine-tuning is used it is reported as the central mechanism rather than an adjunct: a 7B model
fine-tuned on 28,716 natural-language-to-configuration pairs reaching 88.7% accuracy against
larger prompted models in the same framework [[doi:10.1016/j.taml.2025.100594]], and a 32B
chemistry model post-trained on a 214,000-molecule corpus
[[doi:10.26434/chemrxiv.15005838/v1]].

[Certain] Base models named in core rows, counted by family mention rather than by row (a row
can name several): GPT 52, Claude 24, Qwen 15, Gemini 15, DeepSeek 11, Llama 10, with Mistral,
Grok and MiniMax at 2 each. **21 of 98 core sources do not name the model at all**, which
matters for reproducibility: several of these are the same sources that report reproducibility
as their contribution.
