# Superseded — read `outputs/02_tango/v0.1` instead

**This directory is not the authoritative 02_tango run.** Its numbers are
equivalent to `v0.1`'s, but `v0.1` is the record this repository stands behind
and the one `make verify` re-audits.

## Why there are two directories

On 2026-09-11 twenty hand-retrieved PDFs corrected the 02 run: three
`context`/abstract-only records supported a full `core` write-up, so core rose
98 → 101 and context fell 85 → 82. The admitted set did not change — 183 either
way — and no harvested record, no query and no scoring threshold moved.

That correction was first drafted as a fork into `v0.2`, then made **in place in
`v0.1`** instead, because `decisions.md` rules out bumping a version for a
correction that touches no harvested record, no query and no threshold. The
fork was already on disk and committed by then, so it stayed: a committed run is
evidence, and deleting one to tidy the tree is the same class of act as editing
a number inside one.

See the 2026-09-11 entries in [`decisions.md`](../../../decisions.md).

## Why it was not simply deleted

`outputs/03_gaps/v0.1-run2` cites `v0.2` paths in its own committed artifacts.
Deleting this directory would break citations inside another finished run — and
that run may not be edited to repoint them, for exactly the same reason. So the
superseded copy is marked rather than removed.

## What to do

| If you are… | Then |
|---|---|
| reading the 02 findings | use [`../v0.1`](../v0.1) |
| citing the 02 run | cite `outputs/02_tango/v0.1` |
| following a `v0.2` path out of `03_gaps/v0.1-run2` | the content is equivalent; the current path is `v0.1` |
| auditing reproducibility | `make verify` — it audits `v0.1`, not this directory |
