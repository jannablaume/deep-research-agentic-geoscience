outputs/03_gaps/v0.1-run2

## Run log

- date: 2026-09-11
- prompt: `.claude/skills/03_gaps/SKILL.md` v0.1
- prompt commit: e7010e1
- model: Claude Opus 5 (1M context)

## Which runs were read, and at what state

| Run | Directory | Commit |
|---|---|---|
| 01_landscape | `outputs/01_landscape/v0.5` | `e7010e1` |
| 02_tango | `outputs/02_tango/v0.2` | `e7010e1` |

`git status --short outputs/` was clean at extraction time. Both were made clean *by this
session* before anything was read, and that is the first thing this file has to record
because it changed what the run reads.

### Why the output directory is `v0.1-run2`

`outputs/03_gaps/v0.1/` already existed, committed at `11101a9`, holding
`gap_candidates.csv` and `gap_candidates.md` from an extraction over
`01_landscape/v0.5` (pre-addendum-3) and `02_tango/v0.1`. The skill's rule is that an
existing output directory is not reopened, so this run is `v0.1-run2`. The earlier
extraction is left untouched and is the record of what the candidate extractor saw
against the earlier inputs.

### What this session changed before reading

Two things were pending in the working tree and both bore on what would be read:

1. **`outputs/01_landscape/v0.5` was modified in place** — "Addendum 3", a third
   institutional-access batch: three EAGE EarthDoc records read in full, core 38 → 41,
   eight report sections regenerated, and a standing claim about named base models
   corrected (unnamed-model core rows 9/38 → 11/41).
2. **`outputs/02_tango/v0.2` was untracked** — v0.1 plus a hand-retrieval round: 14
   sources re-read from hand-fetched PDFs, three promoted out of `context`, core 98 → 101,
   the admitted set unchanged at 183.

3. **`outputs/02_tango/v0.1` was itself modified**, carrying an in-place edit that was
   later forked into `v0.2`. That is a committed run directory being overwritten, which
   AGENTS.md §A8 forbids. It was restored to `HEAD` (`git checkout -- outputs/02_tango/v0.1`)
   rather than committed. Nothing was lost: every file that differed was verified to be
   superseded by `v0.2`, including the three hand-recovered records and the "Recovered by
   hand" section of `paywalled.md`.

The corpus owner was asked which state the gaps document should be a statement about and
chose to commit first and read the latest. `make check` passed and the result is commit
`e7010e1`. AGENTS.md §A2 independently says to quote v0.2, which is what this run does.

**This is a deviation from the skill text**, which names `outputs/02_tango/v0.1`. It is
recorded here rather than taken silently.

## Step 1 — Candidate extraction

```bash
python3 scripts/gaps.py --out outputs/03_gaps/v0.1-run2 \
    --run outputs/01_landscape/v0.5 \
    --run outputs/02_tango/v0.2
```

**329 candidates.** By run and kind:

| kind | 01_landscape/v0.5 | 02_tango/v0.2 | total |
|---|---|---|---|
| `author-limitation` | 88 | 117 | 205 |
| `claim-gap` | 14 | 40 | 54 |
| `unread-source` | 1 | 32 | 33 |
| `evidence-hole` | 10 | 9 | 19 |
| `absence-claim` | 2 | 7 | 9 |
| `evaluation-hole` | 4 | 4 | 8 |
| `empty-category` | 1 | 0 | 1 |
| **total** | **120** | **209** | **329** |

## Step 1b — What the candidate extractor got wrong, and where that is a finding

`gap_candidates.csv` was not edited. Three defects were found in it while clustering; each
is recorded here and handled in the discard ledger, per the skill's rule that a wrong-looking
candidate is a finding about the run it came from.

- **`claim-gap` flags every M0/M1 row that carries a `maturity_claimed` string**, whether or
  not the claim reaches past the demonstration. 54 of the 329 candidates are that sweep: 41
  TANGO core M0/M1 rows and 14 landscape ones, minus one whose `maturity_claimed` is itself
  `not stated`. Seven are self-evidently modest — "proof-of-concept", "DynaMate2 offers a
  template rather than a finished product", "This work does not claim autonomous scientific
  discovery" — and are discarded `run-artefact`. Both source runs adjudicate this far more
  narrowly than the extractor: `02_tango/v0.2/report/05_maturity.md` says 7 of 40 overreach,
  and `01_landscape/v0.5/report/05_maturity.md` names five.
- **`EMPTY` in `scripts/gaps.py` treats `none` and `not stated` as the same cell.** They are
  different facts. The landscape run's `baseline` count of 84 is 75 `not stated` plus 9
  `none`; the TANGO run's 47 is 7 `not stated` plus 40 `none`. One is a silent source, the
  other is a source that reports no comparator. Every `evidence-hole` candidate inherits the
  conflation.
- **`unread-source` reads `paywalled.md` without noticing recovery.** Three candidates
  (c327–c329) are the "Recovered by hand" rows of `02_tango/v0.2/paywalled.md` — sources the
  v0.2 round retrieved and read. They are discarded `run-artefact`.

A fourth issue is not the extractor's but is inherited by every count it produces: **no
candidate separates `core` from `context`.** `tier` maps one-to-one onto `access_status` in
both grids, so a `not stated` cell in a context row records that nobody read the source, not
that the source is silent. The verification pass turned this into the single most common
reason a gap failed (see below).

## Steps 2-4 — Reading, clustering

Both runs' `report/*.md` were read end to end, plus `RUN.md`, `unreachable.md`, and — for
02 — `paywalled.md` and `transfer.md`. Two ambiguities were resolved against the files
rather than assumed: GAIA is the same source in both corpora (`doi:10.48550/arxiv.2511.03852`
in each), and the `maturity_claimed` cell behind c296 is a reader's recorded contradiction
("the abstract states … deviations under 1.5% … a figure three of the eight
max-displacement entries in its own Table 9 exceed"), not an extraction artefact.

329 candidates clustered into **29 gaps**; 309 candidates cited, 20 discarded individually.

## Step 5 — Verification

21 subagents, one per gap or per closely-related pair, each briefed with the gap statement,
its candidate ids and their `evidence_ref`s, and the instruction to search for work that
would refute it — the runs' own `screened.csv` and `triage.csv` first, then the
bibliographic APIs, then the open web. Every finding they returned was re-checked in this
session against the files before it was written down; the counts in `verification.md` marked
"re-derived" or "re-checked" were recomputed here, and several agent figures were corrected
in the process (the `not stated` variants in `code_availability`, the tier of
`doi:10.1145/3731599.3767584`).

### Gaps by verdict

| verdict | gaps |
|---|---|
| `partially-addressed` | 14 |
| `refuted` | 12 |
| `confirmed-absent` | 3 |
| `undecidable` | 0 |

The three that survived are narrow, and all three are absences somebody looked for: G06 (no
source reports its agent's output acted on outside the experiment and later found wrong),
G09 (`instrument-control` on no deep-read landscape row), and G22 (no follow-up validates
any of fourteen conceptual architectures).

### Candidates discarded

| reason | candidates |
|---|---|
| `run-artefact` | 16 |
| `too-specific` | 4 |
| `refuted` | 87 (the candidates of the twelve refuted gaps) |

107 distinct candidates appear in the ledger; 20 of those are discards made during
clustering and 87 are candidates of gaps the verification pass refuted. `audit_gaps.py`
passes 19/19.

## What the verification pass found, and why it matters for how 03 is run

**Almost every refutation came from inside the runs' own harvest.** Three mechanisms
account for nearly all of it, and none of them is a fact about the literature:

1. **The triage thresholds.** 10,354 records in `02_tango/v0.2/triage.csv` carry
   `band: A_agentic` and `scope_computed: core`; 338 of them appear in `screening.csv`.
   Records refuting G02, G10, G12, G15, G21, G23, G24, G26 and G27 sat in that gap, never
   judged. The binding knob is `--min-domain 4`, which `02_tango/v0.2/RUN.md` had already
   recommended lowering to 3. Concretely: `arxiv:2606.09774` (SIGA, held-out tasks on the
   GEOS subsurface simulator) scored `agentic_score` 0; `doi:10.2139/ssrn.7083227`
   (MeshExpert) was harvested with a zero-length abstract; `doi:10.3390/en18215632`, titled
   "An AI Agent for Techno-Economic Analysis…", was triaged `core` with the
   `techno_economic` touchpoint and never screened — of 135 rows carrying that touchpoint,
   3 reached screening.
2. **Tier conflation in the candidate counts.** `tier` maps one-to-one onto `access_status`
   in both grids, and no candidate separates them. For G03, G04, G17 and G29 the headline
   figures were 90%+ abstract-only; at core tier G04 inverts (66 of 101 TANGO core rows
   state something) and G17 goes to zero across 138 core-tier papers.
3. **Column blindness.** G12, G13 and G27 were built from `author_stated_limitations` alone
   and are contradicted by `reported_result` in the same rows of the same grid — R-LAM
   scoring 1.0 on replay and trace, CFDLLMBench aggregating physical accuracy, ChatCFD
   reporting 68.12% physical fidelity beside 82.1% execution.

**Two findings about the source runs, recorded rather than corrected here.**
`02_tango/v0.2/report/07_periphery.md` states that cells `q015`–`q022` were "harvested and
triaged but never screened"; 489 such records reached `screening.csv`, 487 cut and 2
admitted. And `02_tango/v0.2/paywalled.md` records
`doi:10.3778/j.issn.1673-9418.2508051` as `no-full-text-anywhere`, but DOAJ carries a
working publisher PDF that a verification agent retrieved and read, answering that row's own
`would_change`; separately `doi:10.1145/3785462.3815873` is a CC-BY 4.0 paper labelled
`paywall` when the obstacle is bot protection.

**One source sits in both runs' harvest and neither grid.** `arxiv:2603.00214` (JutulGPT,
building reservoir simulation models on JutulDarcy) is `band: A_agentic` in both
`triage.csv` files, has no `screening.csv` row in either, and is the open companion of a
blocked EAGE record whose `paywalled.md` entry says its evidence has no substitute in the
corpus. In 01 it carries `scope_computed: none`; in 02 its `first_seen_run` is after
screening had run.

### What the verification could not settle

**The bibliographic-API leg failed for most of the pass.** OpenAlex returned HTTP 503
("Anonymous search is paused while the search cluster recovers from heavy load") to
anonymous search throughout; arXiv returned HTTP 429, and in two agents' environments
returned zero bytes even for a control query. Where agents reported this, it is written into
the `not searched` line of the block. So the corpus and open-web legs carried the pass, and
a re-run with working APIs could move verdicts in either direction.

**Publisher blocks bounded two verdicts.** G06 rests on "no such report was findable": the
two closest artefacts, a corrigendum to an LLM-multi-agent geotechnical design paper and a
retracted LLM-multi-agent materials paper, both returned HTTP 403 and neither notice was
read. G08's remaining list is openly licensed in several rows and refuses automated clients.

**G22 is short-horizon.** Eleven of its fourteen systems were published within 4 to 16
months of this run, so no follow-up is weak evidence of no validation.

## For v0.2

1. **Extract per tier.** Every `evidence-hole` and `unread-source` count should carry its
   core and context split. As it stands a candidate cannot distinguish a silent source from
   an unread one, and that single conflation refuted or qualified four gaps.
2. **Separate `none` from `not stated` in `EMPTY`.** They are different measurements and
   `scripts/gaps.py` merges them.
3. **Read the whole row, not one column.** `claim-gap` and `author-limitation` extraction
   should be checked against `reported_result` and `evaluation_method` on the same row
   before a gap is written; three gaps were contradicted by their own rows.
4. **Make `claim-gap` adjudicate rather than sweep.** It flags every M0/M1 row with a
   `maturity_claimed` string; both source runs adjudicate roughly a fifth of that.
5. **Check `paywalled.md` for recovery before extracting `unread-source`.** Three candidates
   described sources the v0.2 round had already read.
6. **A gap over a run's admitted set is not a gap in the literature, and the document should
   say which it is.** Most of this run's gaps were written as claims about the field and
   verified as claims about the corpus. Stating the scope in the gap sentence would have
   made at least seven of the twelve refutations into confirmed narrow findings instead.
