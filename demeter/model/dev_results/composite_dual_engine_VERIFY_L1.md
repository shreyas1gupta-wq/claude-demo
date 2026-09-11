# composite_dual_engine — L1 verification (Causality & code)

Verifier: L1 adversarial reviewer, pass 2. Scope: lookahead in any form, `_VERIFY.json` mechanical battery,
the lag test, and whether `DEFAULT_PARAMS` / declared tunables / UPPER_CASE constants are honestly counted
against the PREREG G7 budget (≤6 tunables). Coordinator notes for this candidate: none.

## Mechanical battery (`verify_tools.py`, run fresh — file was absent)

```
composite_dual_engine: causality ok=True max_abs_diff=0.00e+00 nan_mismatches=0
  lag test dev_1990 Sharpe: base 0.543 | lag1 0.582 | lag2 0.559
  grid: n=243 max Sharpe 0.548 median 0.454 share>=0.425 70% share passing G2-G4 63%
  frozen Sharpe 0.543 rank 2/243 (pctile 100%); neighbourhood 10 combos Sharpe 0.429..0.536, 100% within 25%
  constants: LEV_REB=3.0
  halves: [0.692, 0.4] thirds: [0.877, 0.323, 0.357]
  turnover: 122 changes, 7% in top-decile-vol days
```

## 1. Causality — CLEAN

* All 12 truncation cutoffs (1992 → 2011) give `max_abs_diff = 0.0`, `nan_mismatches = 0`. `lookahead_check`
  recomputes the signal on data hard-truncated at each cutoff and diffs it against the full-sample signal
  restricted to the same range — a real test, not a smoke test, and it is clean.
* Lag test does **not** collapse — it *improves* with an extra day of delay (base 0.543 → lag1 0.582 → lag2
  0.559). A rule that were peeking at t+1 would lose edge, not gain it, when you delay its application further
  from the peek; the direction here is exactly what a non-lookahead, momentum-adjacent-but-lagged rule produces.
  No implication of hidden lookahead.
* Manual line-by-line read of `signal()` and `vix_regime()` in `signals/composite_dual_engine.py` confirms every
  rolling/ewm feature is trailing (`features.rsi`, `features.days_since_true`, `.rolling(...).std().shift(1)`,
  `vix.shift(1).rolling(...).mean()`, `vix.rolling(VIX_WIN).max()`), the VIX-regime state machine is a
  single left-to-right pass with no future read, `ffill()` only reads backward, and the day-`i` decision loop
  only ever reads `ret[i]`, `x_ex[i]`, `vix[i]` (same-day-close quantities, legitimate at "decided at the close
  of day t") plus past state (`mode`, `cur`, `held`, `cum`, `last_change`, `block_until`). Engine applies the
  output via `.shift(1)` (`engine.py:92`), so the emitted signal for day t is correctly realised as the position
  on day t+1. **No `.shift(-k)`, no centered window, no full-sample statistic, no state read from t+1.**
* `since_shock` is extended (clock reset) by `shock_day | two_day | vol_jump`, but the actual OUT-mode *trigger*
  is `two_day | vol_jump` only — a single-day shock never opens OUT on its own, it only re-arms the "how long
  have we been clear" clock while already OUT. This matches the docstring's rule 2 exactly; flagged only as a
  MINOR readability note (§Minor 1), not a defect.

## 2. Parameter budget — **SEVERE: true tunable count is at least 7, not 6**

PREREG caps tunables at 6 (G7). The brief's rule for this lens is explicit: *"a constant whose value was chosen
by comparing DEV results IS a tuned parameter."* Two independent violations of that rule were found by reading
the design note against the signal file; either alone breaks G7.

### 2a. `LEV_REB` was selected by DEV-result comparison inside this candidate's own search

* The design note's own **pre-run** parameter-budget section (written before any harness call) lists it as
  undetermined: *"LEV_REB (3 pending census)"* (`DESIGN_NOTE.md:52`) — i.e. its value was explicitly not yet
  fixed by the record or by mechanism at declaration time.
* It was then fixed by running ablations **D / E / F** — the frozen model with the re-entry leverage set to
  3x / 2x / 1x — and comparing dev_1990 Sharpe: **0.543 / 0.522 / 0.485** (`DESIGN_NOTE.md:117-119`, table row
  D/E/F at `DESIGN_NOTE.md:225-227`, source `composite_dual_engine_ablate_frozen.csv`). The design note states
  outright: *"LEV_REB decided from the census, as pre-registered"* and *"the record's 3x is kept"* — kept
  **because** it scored highest in that three-way DEV comparison, not because 3x is what the record independently
  specifies (the docstring itself is explicit that LEV_REB is "decided by the spurious-re-entry census in DEV
  ... not by the record's 3x", `composite_dual_engine.py:31`).
* This is the textbook case the brief's rule targets: a value chosen by comparing DEV Sharpes across candidate
  values. It is the model's **7th tunable**. `gate_check.py`'s printed `G7_param_budget: pass value=6` is
  therefore wrong on the true count; on 7 tunables **G7 fails** (bar is ≤6). Per PREREG, "candidates failing
  any gate are reported as failures ... and are never run through `evaluate.py`."

### 2b. Six more "structural, borrowed unchanged" constants are verbatim copies of *other* candidates' own tuned parameters

Cross-checked `signals/dissipation_reentry.py` and `signals/crash_exit_dual.py` directly:

| composite constant | value | source file | source's own DEFAULT_PARAMS entry |
|---|---|---|---|
| `J_JUMP` | 0.30 | `crash_exit_dual.py` | `j=0.30` (declared tunable, `DEFAULT_PARAMS = dict(k=4.0, j=0.30, ...)`) |
| `VIX_FALL` | 0.25 | `dissipation_reentry.py` | `vix_fall=0.25` (declared tunable) |
| `VIX_WIN` | 30 | `dissipation_reentry.py` | `vix_win=30` (declared tunable) |
| `VIX_MIN` | 30.0 | `dissipation_reentry.py` | `vix_min=30.0` (declared tunable) |
| `HOLD_DAYS` | 10 | `dissipation_reentry.py` | `hold_days=10` (declared tunable) |
| `STOP` | 0.10 | `dissipation_reentry.py` | `stop_loss=0.10` (declared tunable) |

Every one of these six values is a member of *another* candidate's own declared 6-parameter tunable set (i.e.
each was itself selected there by that candidate's own DEV grid search — the identical mechanism the brief's
rule is written against). `composite_dual_engine.py`'s docstring relabels them "Structural constants
(declared, NOT tuned)" and "borrowed unchanged" (`composite_dual_engine.py:50,59-60`) and they are excluded
from this file's 6-parameter budget. Relabelling a value as a constant in the importing file does not change
that the number was produced by comparing DEV results — it only moves *where* the comparison happened. Note
also that `J_JUMP`'s source, `crash_exit_dual`, **failed PREREG gates G3/G4** (per `PREREG.md:72`); composite
inherits a DEV-tuned constant from a gate-failing candidate without re-testing it in its own right.
`RSI_MAX` (also borrowed from `dissipation_reentry.py`) is a genuine exception — it is a bare module constant
there too, never in that file's `DEFAULT_PARAMS`, so its structural pedigree is clean.

Taken together, a complete accounting is **6 declared + LEV_REB + 6 borrowed-but-externally-tuned = 13** knobs
that trace back to a DEV-result comparison somewhere in this study, against a stated budget of 6. `true_tunable_count`
reported to the coordinator is **7** (the count the letter of the L1 instruction supports — "the design note
shows were chosen by comparing DEV results" — since only the LEV_REB comparison is shown *in this file's own
design note*); the wider 13-knob reading is disclosed above for the coordinator to weigh, because the source
files were read directly, not inferred.

## 3. Mechanical-battery reliability — MATERIAL

`verify_tools.py`'s `constants()` auditor (`verify_tools.py:99-107`) uses the regex
`^([A-Z][A-Z0-9_]*)\s*=\s*(.+?)\s*(#.*)?$`, which only matches a **single** uppercase name at the start of a
line. `composite_dual_engine.py` declares almost all of its constants as multi-target tuple assignments
(`LEV_CALM, LEV_ELEV, LEV_STRESS = 3.0, 1.0, 0.0`; `J_JUMP, VIX_BASE, VIX_FLOOR = 0.30, 10, 20.0`; `VIX_FALL,
VIX_WIN, VIX_MIN, RSI_MAX, HOLD_DAYS, STOP = 0.25, 30, 30.0, 20.0, 10, 0.10`; `USE_SHOCK, USE_REENTRY = True,
True`), none of which the regex captures — it caught only `LEV_REB = 3.0`, the one single-name line, out of
~16 module constants. The mechanical `module_constants` field in `_VERIFY.json` is therefore **not** an
exhaustive audit for this file (or any file using this declaration style); §2 above was only found by manual
line-by-line cross-reading of the signal file and the design note, which the brief requires but the automated
battery cannot substitute for. This is a shared-code (`verify_tools.py`) defect; the design note's own "Bugs
found in shared code: None" (`DESIGN_NOTE.md:336`) did not catch it because the designer never ran `verify_tools.py`
(it audits the frozen file post hoc, not during design).

## 4. Cross-lens notes (not scored here — L2's remit, flagged for completeness)

* Grid rank: frozen point is 2nd of 243 grid combinations, 0.0055 Sharpe off the max, 99.6th percentile
  (`grid_audit.frozen_rank=2`, `frozen_percentile=0.9959`). The docstring's "interior plateau centre, not the
  grid maximum" is literally true (rank 2 ≠ rank 1) but the margin is small enough that a reader could be
  misled about how close to peak-hugging this actually is. The design note itself is candid about this
  (`DESIGN_NOTE.md:130,275-277`: *"the honest reading ... is that the model's DEV Sharpe is 0.50 ± 0.05, not
  0.543 exactly"*).
* Sub-sample stability: thirds Sharpe 0.877 / 0.323 / 0.357 (1990-97 / 1997-2005 / 2005-2012H1) — two of three
  thirds are well under the 0.425 gate bar on their own; the headline is carried by the first third.

## Findings summary

**SEVERE**
1. `LEV_REB` was selected by comparing DEV Sharpes across 3x/2x/1x (ablations D/E/F: 0.543/0.522/0.485) after
   being pre-declared undetermined ("pending census"); by the brief's own rule this is a tuned parameter, making
   the true count 7 and breaching G7 (≤6). `gate_check.py`'s `G7_param_budget: pass value=6` does not reflect
   this.
2. Six more constants (`J_JUMP`, `VIX_FALL`, `VIX_WIN`, `VIX_MIN`, `HOLD_DAYS`, `STOP`) are verbatim copies of
   *other* candidates' own DEV-tuned `DEFAULT_PARAMS` values (crash_exit_dual's `j`, dissipation_reentry's
   `vix_fall`/`vix_win`/`vix_min`/`hold_days`/`stop_loss`), relabelled "structural, borrowed unchanged" and
   excluded from this file's budget; one of them (`J_JUMP`) is inherited from a candidate that itself failed
   PREREG gates G3/G4. A complete accounting puts the true tunable lineage at 13, not 6.

**MATERIAL**
3. `verify_tools.py`'s `constants()` regex misses every multi-target tuple-assignment constant in this file
   (15 of 16), so the mechanical battery's `module_constants` output cannot be trusted to certify
   constant-genuineness here without the manual cross-read performed in §2 — a shared-code gap, not caught by
   the design note's "Bugs found in shared code: None."
4. Frozen point ranks 2nd of 243 grid points (0.0055 Sharpe off the max, 99.6th percentile) — closer to
   peak-hugging than the docstring's "interior plateau centre" framing suggests, though the design note discloses
   the honest 0.50±0.05 reading itself.
5. DEV Sharpe is front-loaded: thirds are 0.877 / 0.323 / 0.357 — the 0.543 headline is not evenly earned across
   the 22-year dev_1990 window.

**MINOR**
6. Single-day shocks (`shock_day`) extend the OUT-mode clock but never trigger OUT on their own (only
   `two_day`/`vol_jump` do) — matches the documented mechanism exactly, flagged only because a fast reading of
   "each restarts the clock" in the docstring could be misread as also being an entry condition.
7. `dev_harness.plateau`'s integer-parameter rounding gives asymmetric ±15%/±30% steps for `out_days`/`min_hold`
   (already self-disclosed in the design note) — a G6 measurement-precision note, confirmed here to have no
   bearing on causality.

## Verdict

**Refuted.** Two SEVERE findings (§2a unambiguous on this file's own evidence; §2b corroborating from direct
reads of the two source files). The candidate's own design note is unusually candid about weaknesses and even
concedes it does not beat the DEV leader — but candour about weak points does not cure a parameter-budget
miscount: on the true count this candidate fails G7 and, under PREREG's rule ("candidates failing any gate ...
are never run through `evaluate.py`"), should not receive the out-of-sample look in its current form.
