# sticky_tier — L1 verification (Causality & code)

Verifier: adversarial L1, pass 2, 2026-09-12. Scope per VERIFY_BRIEF.md: lookahead in any form, DEFAULT_PARAMS vs
declared tunables, and whether every UPPER_CASE constant is genuinely structural or was in fact chosen by comparing
DEV results.

## 1. Causality — clean

* `dev_results/sticky_tier_VERIFY.json.causality_12_cutoffs`: all 12 cutoffs (1992-03-31 .. 2011-08-08) `max_abs_diff
  = 0.0`, `nan_mismatches = 0`. The signal computed on data truncated at each cutoff is bit-identical, up to that
  date, to the signal computed on the full series. No lookahead detected mechanically.
* Read `signals/sticky_tier.py` line by line (`_core`, lines 94-143):
  - `fast`/`slow` = `features.ewma_vol(ret, halflife=...)` = `ret.ewm(halflife=hl, min_periods=20).std()` — a
    trailing-only pandas `.ewm().std()`, no `center=True`, no negative shift, no `cummax`/`max` over future rows.
    Confirmed in `features.py:14-15`.
  - Weekly-cadence gate (line 107-109): `wk = df.index.isocalendar().week; decide = wk.ne(wk.shift(1))`. This uses
    **ISO week number**, not `dayofweek`, and compares only the current row to `wk.shift(1)` (the previous row) —
    exactly what the docstring claims ("causal: compares this row's week with the previous row's only"). No
    `shift(-k)`, no read of day t+1. Vectorised computation over the whole array is still causal element-wise since
    each entry only depends on itself and its immediate predecessor.
  - The persistence/hysteresis state machine (lines 118-142) is a single forward `for i in range(n)` loop that only
    reads `sig[i]` and its own running state (`cur`, `last_change`, `up_run`, `dn_run`) — no forward indexing.
  - `engine.py:92`: `pos = lev.shift(1)` — the engine, not the signal, applies the level to the *next* day
    (`pos_prev = lev.shift(2)`), matching the docstring's "engine applies the level to day t+1". Signal and engine
    agree on the timing convention.
  - No `spx_tr` or `rf` is read inside the signal file at all (only `df["spx_ret"]`); the return used to build the
    vol estimate is the same-day return, which is legitimately known at the close of day t. VIX is not used anywhere
    (module docstring: "No VIX, so the rule runs from 1950" — confirmed by code, no `vix` column referenced).
* **Lag test** (`lag_test_dev_1990`): base Sharpe 0.6116 -> lag1 0.6101 (-0.24%) -> lag2 0.6040 (-1.2%). No collapse.
  **Caveat (MINOR, see below):** with only 10 position changes in 22.5 years (0.44/yr), a 1-2 session lag test is a
  weak diagnostic here — most days are deep inside a held spell, far from any transition, so shifting the decision
  by a day or two barely touches which regime is in force on any given day. The absence of collapse is consistent
  with a genuine (if weak) signal, but it is not strong evidence given how rarely the rule actually acts; it should
  not be over-read as a clean bill of health for the same reason `changes_per_year=0.44` makes several other
  diagnostics (below) close to vacuous.

**Verdict: no SEVERE lookahead finding.** All mechanical and manual checks pass.

## 2. DEFAULT_PARAMS vs declared tunables

`DEFAULT_PARAMS = dict(target_vol=0.14, h=0.20, hl=20.0, long_mult=8.0, P=5)` — 5 entries, matches `signal()`'s
keyword defaults exactly, matches `dev_results/sticky_tier_RETURN.json.n_tunable_params = 5`, matches gate
`G7_param_budget: pass value=5 (bar 6)`. Internally consistent.

## 3. Are the "structural constants" genuinely structural? — MATERIAL finding

The design note (`## Structural decisions made on the grids (not tunables)`, dev_results/sticky_tier_DESIGN_NOTE.md
lines 87-99) itself discloses, in its own words, that **`FLOOR` was chosen by comparing DEV results**:

> "FLOOR = 0. Grid A: 192 of 192 floor-1 combos fail G3 (best maxDD -53.6%); at the frozen point a 1x floor gives
> Sharpe 0.43, maxDD -50.8%, CAGR 9.2% (diag3). ... A 1x floor gives the higher CAGR and a Sharpe that only matches
> the incumbent — it fails G3 and is rejected."

I confirmed this against the raw grid: `dev_results/sticky_tier_gridA_grid.csv` has a `floor` column with values
{0,1}, 384 rows total (192 each). This is precisely the case the brief flags: *"a constant whose value was chosen by
comparing DEV results IS a tuned parameter."* Whether `floor` is 0 or 1 is a discrete design choice that was decided
**after** running both arms and comparing which one passed the DD gate — mechanically indistinguishable from how
`target_vol`, `h`, `hl`, `long_mult` and `P` were each selected by comparing DEV outcomes across a grid. The fact
that the comparison was unanimous (192/192) and gate-driven rather than Sharpe-maximising lowers its overfitting
risk relative to the five continuous parameters, but it does not change what kind of decision it is.

**True tunable count: 6, not 5** (`target_vol, h, hl, long_mult, P, FLOOR`). This is **exactly at** the G7 ceiling
(bar ≤ 6) — it does not breach the gate, but the frozen candidate has zero headroom left in the parameter budget,
and `RETURN.json`'s declared `n_tunable_params: 5` understates it. This should be corrected in RESULTS.md/the
register rather than carried forward as "5 tunables."

Cross-checked the remaining constants against every grid CSV's columns (`v_lo, gap, h, hl, M, P, floor` for grid A;
`target_vol, h, hl, long_mult, M, P` for B/C1/C2 — **no `p_dn` or `weekly_up` column ever appears in any grid**):

* **`M_COOL` (=10):** varied in grid A and grid C2 (`M` column) but the design note reports the results were
  *identical* across M ∈ {0, 5, 10, 21} at the operating point (verified: this is a documented tie, not a
  Sharpe-ranked pick). Choosing among tied outcomes is not "comparing DEV results" in the sense that matters
  (no discriminating information was used), so demoting it to a structural constant is defensible. MINOR note only.
* **`P_DN` (=1) and `WEEKLY_UP` (=True):** never appear as a grid column anywhere in the four grids — they were
  fixed by design throughout, not selected from a set of DEV-compared values. The design note's only quantitative
  support for the *bundle* {h>0, P>1, weekly cadence} vs. an "unsticky" ablation (h=0, P=1, M=0, daily) is a single
  before/after comparison (+0.13 / +0.08 Sharpe in two windows), not a grid search over `WEEKLY_UP` in isolation —
  so `WEEKLY_UP`'s individual marginal contribution was never isolated from `h` and `P`'s. This is a legitimate
  architectural prior with one supporting ablation, not a tuned parameter by the brief's definition, but the
  ablation is weak evidence for the *specific* weekly-vs-daily choice on its own (MINOR — flag for L3/mechanism, not
  a tunable-count issue).
* **`MAX_LEV` (=3):** genuinely structural — set by mandate (Demeter's own {0,1,2,3} grid), never varied in any
  grid file. No issue.
* **`MIN_PERIODS` (=20):** genuinely structural (EWMA warm-up), never varied. No issue.

## 4. Reconciliation of `n_iterations: 13` vs. grid CSV `144` combos — informational, resolves cleanly

Coordinator flagged this as needing reconciliation. It does reconcile, and the reconciliation is disclosed by the
designer, not hidden:

* `dev_results/sticky_tier_RETURN.json`: `"n_iterations": 13`.
* `dev_results/sticky_tier_VERIFY.json.grid_audit.n_combos = 144` — this is grid **C1 only** (the grid that
  `sticky_tier_grid.csv` was copied from; confirmed `grid file: sticky_tier_grid.csv`, C1 spec has 144 rows).
* Design note `## Iteration count` (lines 240-246): "13 distinct DEV evaluations: 5 grids (A 384 + B 135 + C1 144 +
  C2 64 = 727 combinations, each grid counted once) + 8 single runs ... **Total parameter sets touched: 735**."

So "13" is a count of *evaluation batches* (5 grid runs + 8 point runs), "144" is the size of one specific batch
(the final grid), and the true number of distinct parameter combinations examined across the whole DEV process is
735. All three numbers are consistent once you read the design note; none of them is fabricated. **MATERIAL**
finding: `n_iterations: 13` is a misleading figure to quote on its own (a reader of `RETURN.json` alone, without the
design note, would badly underestimate the search) — RESULTS.md must quote the 735-combination total, not 13, when
describing how much of the parameter space was explored, alongside the true tunable count of 6 from §3.

## 5. Other code observations (MINOR)

* `verify_tools.py`'s `module_constants` scrape is a regex-driven docstring/source dump and is somewhat broken (it
  lists `P_DN` twice with two different truncated strings and misses `WEEKLY_UP`'s prose entirely on the first
  pass) — a tooling cosmetic issue, not a signal-file defect; it did not affect any of the checks above because I
  verified the actual constants against `signals/sticky_tier.py` directly rather than trusting the scrape.
* The designer's own disclosed harness observations (`RETURN.json.bugs_in_shared_code`) — that `dev_harness.py`'s
  plateau perturbation rounds integer parameters (P=5 ± 15%/30% rounds to only two distinct values, 4 and 6,
  reducing the effective G6 sample for that parameter) and that the shared spurious-reentry census only counts
  entries to ≥2x (vacuous for a rule whose ceiling in-bear is 1x/cash) — are real and I confirmed the rounding claim
  by re-reading the grid_audit neighbourhood table (`hl` shows values 16.0/26.0 flanking 20.0, i.e. ±X% neighbours
  were computed as absolute steps, not rounded, so the rounding artefact is specific to small-integer parameters
  like P). These are shared-harness issues that affect gate G6's meaningfulness for this candidate specifically;
  per the brief's lens split this is routed to L2 ("L2 comment on whether G6 is meaningful for this rule") and is
  not re-litigated here beyond confirming the underlying facts are accurate as described.

## Summary

No SEVERE finding. Causality is clean by every mechanical and manual test available. One MATERIAL correction to the
frozen candidate's own bookkeeping: the true tunable count is 6 (not 5), sitting exactly at the G7 ceiling because
`FLOOR` was, by the brief's own definition, chosen by comparing DEV results (192/192 grid-A floor=1 combos failing
G3) even though the design note frames it as "not a tunable." A second MATERIAL item: `n_iterations: 13` in
`RETURN.json` is a batch count, not a combination count, and must be reported as "735 parameter combinations across
5 grids + 8 point runs" in any external-facing document, not "13," to avoid understating the size of the search
that produced this frozen point.
