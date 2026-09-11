# 07 Periphery

[Certain] The agent literatures this run harvested, counted and deliberately did not read.
Everything here comes from `triage.csv` and `queries.csv`; no periphery record was deep-read
and no claim below rests on one.

## What periphery means in this run

[Certain] Four groups are periphery by decision in `reference/queries_tango.json`:
software engineering, laboratory and robotic automation, web/GUI/computer-use agents, and
literature-and-writing agents (grouped as `science_of_science`). The decision rule is what the
agent's actions land on. A system that decides for itself and then files a pull request, runs a
pipetting robot, clicks through a browser or drafts a paper is fully agentic and is not driving
a simulator, solver or engineering model — so it is counted and not read.

[Certain] The counts are large enough that this was the right call on cost alone. Of the
35,046 records the two APIs returned, **12,189 were classified periphery**, against a
shortlist of 773 total and 352 in core scope. The periphery is roughly sixteen times the size
of the entire shortlist this run screened by hand.

## Size, by group

[Certain] Periphery records in the harvested corpus, by group:

| group | harvested records |
|---|---|
| science_of_science (literature, writing, review agents) | 6,093 |
| software_engineering | 4,488 |
| interface_agents (web, GUI, computer-use) | 1,196 |
| lab_automation | 412 |

[Certain] The split by band is almost even — 5,911 matched the agentic band and 6,278 the
broader LLM band — which says these literatures are not marginal cases that happened to
mention an agent, but substantial bodies of work in their own right.

## What the harvest could and could not reach

[Certain] The periphery query cells were **not fully retrieved, and deliberately so**. Sixteen
query cells were run against the two APIs for the four periphery groups, and twelve of them
truncated at a paging cap. The gap between what the APIs reported as available and what was
actually pulled is the honest measure of these literatures' size:

| group | records available | records retrieved | cells |
|---|---|---|---|
| science_of_science | 33,810 | 9,475 | 4 |
| software_engineering | 15,020 | 9,659 | 4 |
| interface_agents | 3,337 | 3,313 | 4 |
| lab_automation | 1,095 | 1,087 | 4 |

[Certain] Two cells dominate the shortfall: one science-of-science cell reported 22,164
records available and returned 4,000, and one software-engineering cell reported 8,134 and
returned 4,000. The core scopes were re-harvested with raised paging caps after the same
truncation was found there; **the periphery was left truncated on purpose**, because the
report needs its size and character, not its contents. `n_available` is therefore the number
to read in the table above, and it is a lower bound on two of the four groups.

[Certain] For contrast, the core scopes returned 352 shortlisted records across eight groups
after the cap was raised. The literature on agents that drive scientific software is, on these
queries, between one and two orders of magnitude smaller than the literature on agents that
write software.

## Character, from titles and abstracts only

[Certain] Six periphery-adjacent records were nonetheless admitted at `tier: context` because
their agent's actions land on something this run counts even though the paper's framing is
periphery: benchmarks asking whether general coding agents can reproduce published
computational pipelines [[doi:10.48550/arxiv.2409.11363]] [[arxiv:2605.00803]], a system
turning scientific repositories into containerised runnable capabilities
[[doi:10.48550/arxiv.2601.03513]], a materials-tooling benchmark
[[doi:10.48550/arxiv.2505.10852]], an HPC-administration multi-agent system
[[doi:10.1109/sci68648.2025.11333875]] and a security study of agents acting on HPC systems
[[arxiv:2607.18485]]. These are the boundary, and they are admitted rather than cut because in
each case a simulator, solver or scientific code is the thing being acted on.

[Absent-searched] (backed by query cells `q015`-`q022`) Beyond those six, no periphery record was read, so this run can say nothing
about what the software-engineering or laboratory-automation literatures contain beyond their
size and their group labels. The periphery cells (`q015` through `q022`) were harvested and
triaged but never screened, and `shortlist.md` was read only for core-scope records. Any
statement here about periphery *findings* would be unsupported, and none is made.

## One boundary that moved during screening

[Certain] The `lab_automation` group is the smallest periphery literature at 412 harvested
records, and it is the one whose boundary with core scope is genuinely blurred: several
admitted core systems couple a simulation loop to an experimental campaign at one end
[[doi:10.6084/m9.figshare.30931802]] [[arxiv:2606.05050]]. Those were admitted on the
simulation half of the loop, not the laboratory half, and their `what_it_drives` entries name
the simulation codes accordingly. The rule applied throughout was the one in the prompt: what
the agent's actions land on. Where they land on a physics engine, the record is in scope, even
if a robot sits downstream of it.
