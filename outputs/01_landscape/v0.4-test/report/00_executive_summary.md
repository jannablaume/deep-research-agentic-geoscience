# Executive summary

This directory is a **mechanics test** of `01_landscape_neutral` v0.4, not a landscape of the field. Harvest was limited to six of thirty query groups (`geomechanics`, `seismology`, `hydrogeology` × bands A and B). [Certain]

The pipeline completed: harvest, triage, screening, a two-query grey-literature pass, deep-read of three arXiv core papers, report files, and `audit.py`. [Certain]

On this slice the harvested corpus is 1865 API records plus two grey additions (1867). Triage at `--min-score 3 --min-strong 1` shortlisted 113 (all tagged core-group; none periphery, because periphery query groups were never called). Screening admitted 34 sources (3 `core`, 31 `context`) and cut 121. An audit sample of 40 below-cut records produced 0 false negatives. [Certain]

The three deep-read systems are a LangGraph Fortran-to-Devito translator evaluated on synthetic finite-difference cases [[arxiv:2601.18381]], a constrained LangGraph FDSN retrieval assistant demonstrated on example workflows [[doi:10.48550/arxiv.2609.01777]], and a hierarchical multi-agent seismological reasoner applied to the named Ridgecrest and Santorini–Kolumbo sequences [[doi:10.48550/arxiv.2603.21152]]. [Certain]

Counts, subfield coverage and maturity distributions below are those of the six-query slice. They are not estimates for a full harvest. [Certain]
