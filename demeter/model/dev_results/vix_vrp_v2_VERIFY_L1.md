# L1 verification — vix_vrp_v2 (Causality & code)

Verifier: adversarial L1, pass-2 three-lens review. Scope: lookahead in any form, `_VERIFY.json` causality/lag,
`DEFAULT_PARAMS` vs true tunable count. No parameters proposed, no `evaluate.py`, no `results/` touched.

## Files examined
`signals/vix_vrp_v2.py` (full read), `dev_results/vix_vrp_v2.json`, `dev_results/vix_vrp_v2_VERIFY.json`,
`dev_results/vix_vrp_v2_RETURN.json`, `dev_results/vix_vrp_v2_ablation_all.csv` (21 rows),
`dev_results/vix_vrp_v2_ablation_round2.csv` (16 rows), `dev_results/vix_vrp_VERIFY.json` (original, for comparison),
`features.py` (`realized_vol`), `engine.py` (`run`, position shift), `gate_check.py` (G7 implementation),
`PREREG.md`, `DESIGN_BRIEF.md`.

**Note on inputs:** `dev_results/vix_vrp_v2_DESIGN_NOTE.md` does **not exist** — see Finding 3.

---

## Finding 1 — SEVERE — true tunable count is 8, not 6: G7 budget is breached

`DEFAULT_PARAMS` declares 6 tunables (`v_calm, v_panic, hyst, rv_win, vrp_min, vrp_elev`) and both
`dev_results/vix_vrp_v2.json` and `_RETURN.json` self-report `n_tunable_params: 6`. `gate_check.py` line 32
computes `G7_param_budget` purely as `n_tunable_params <= 6` — a field the signal file supplies about itself; the
gate cannot see constants declared outside `DEFAULT_PARAMS`.

But two of the three module-level "structural" constants had their **values compared on DEV and one alternative
value rejected in favour of the default**, which is exactly the case the verification brief calls out: *"a constant
whose value was chosen by comparing DEV results IS a tuned parameter."*

* **`LEV_CALM = 2.0`.** `dev_results/vix_vrp_v2_ablation_all.csv` row `V1_calm3x` sets `lev_calm=3.0` and reports
  dev_1990 Sharpe **0.5475** vs the row-0 base **0.6084** (maxDD -27.8% vs -19.8%, worst month -15.5% vs -10.7%).
  The module docstring itself confirms this was a v2-build-time test: *"a 3x CALM tier ... tested one at a time and
  rejected on DEV (worse Sharpe and/or ruinous 2000-02/2008 behaviour)"* and repeats the exact numbers under
  "Structural constants": *"3x CALM was tested once on DEV and rejected (Sharpe 0.61 -> 0.55...)"*. This is a
  textbook DEV-comparison selection of a constant's value, not a structural declaration made before any run.
* **`LEV_PANIC = 1.0`.** The same CSV's row `V0c_panic2` sets `lev_panic=2.0` and reports Sharpe **0.6074** (barely
  different from base) but maxDD **-41.9%** and GFC **-54.4%** vs the frozen point's -19.8%/-28.6% — a materially
  worse drawdown/GFC outcome that was used to keep the value at 1. This comparison is **not** disclosed anywhere in
  the docstring's "Structural constants (not tuned, with reasons)" section, which only names the CALM and
  burst-re-entry ablations — an omission on top of the mis-classification.
* **`LEV_ELEV_ON = 1.0`** is the one constant that is genuinely never value-compared: every row of both ablation
  CSVs that varies `lev_elev` uses `1.0` throughout (`ablation_all.csv` rows 2-6, `ablation_round2.csv` all 16
  rows) — only the *gating rule around it* (unconditional floor vs VRP-gated) was compared, holding the level fixed.
  This one stays legitimately structural.

`plateau_dev_1990` in `dev_results/vix_vrp_v2.json` perturbs exactly the 6 declared tunables (24 = 6×4
perturbations) — the two DEV-selected constants above were never included in the G6 plateau/robustness check
either, so their sensitivity is untested by the very battery meant to catch this.

**True tunable count: 8** (6 declared + `LEV_CALM` + `LEV_PANIC`). This is a breach of **G7 (≤ 6)** by 2 — a
gate the candidate is recorded as having passed (`gates_all_pass: true`, `G7_param_budget: true` in
`vix_vrp_v2_RETURN.json`). Per PREREG.md, G7 is one of the gates a candidate must pass on ALL of before it "earns
one out-of-sample look"; on a correct count this candidate does not clear G7 as specified, and per the
pre-committed retirement rule (PREREG.md line 74) a SEVERE verification finding is explicitly one of the two things
that can override the provisional "vix_vrp_v2 replaces the original" selection.

## Finding 2 — SEVERE — the entire claimed v2-over-original edge inverts under a one-session slower fill

`dev_results/vix_vrp_v2_VERIFY.json` `lag_test_dev_1990` (via `verify_tools.sharpe_dev`, which itself passes the
lagged signal through `engine.run`'s own `pos = lev.shift(1)` — so "lag1"/"lag2" are a *second* and *third* day of
delay on top of the normal one-day execution lag, i.e., total fill delay of 2 and 3 sessions):

| | base (1-day fill) | lag1 (2-day fill) | lag2 (3-day fill) |
|---|---|---|---|
| **vix_vrp_v2** Sharpe | 0.6783 | **0.4219** | 0.4313 |
| **vix_vrp** (original) Sharpe | 0.6084 | **0.4862** | 0.4153 |
| **v2 − original** | **+0.070** | **−0.064** | +0.016 |

Causality itself is clean: `causality_12_cutoffs` reports `"ok": true, "max_abs_diff": 0.0"` at all 12 cut-off
dates, so the signal function does not read future rows — this is not a code-level lookahead bug. And the raw
collapse under lag is not unique to v2: the frozen, already-accepted original shows a comparably steep decay
(0.608 → 0.486 → 0.415), so a big absolute drop under added delay is a family trait of this hysteresis state
machine, not evidence against v2 specifically.

What *is* specific to v2 is the **sign flip of the difference**: the entire basis for selecting v2 over the
original — a dev_1990 Sharpe advantage of +0.070, the only number driving the provisional recommendation in
PREREG.md ("DEV ranking of gate passers ... vix_vrp_v2 0.678 ... Provisional DEV-chosen recommendation:
vix_vrp_v2") — reverses to **v2 being 0.064 worse** than the original the moment execution is one session slower
than the harness's exact next-day-open convention, before partially recovering at lag2. Since both models consume
identical `vix_close`/`rv` series (the new leg reuses rule 2's inputs unchanged), this is not a new same-close
information leak introduced by rule 3 relative to rule 2's existing (and already-accepted) 16:15-vs-15:59
approximation — checked and cleared, see Finding 4. It is consistent with the designer's own disclosed
`biggest_weakness` (ELEVATED-VRP leg open on 132 days / 22.5 years, in spells of ~2-3 days, leg t≈1.9): a leg that
thin and that short-lived is, by construction, going to be extremely sensitive to which exact day it is entered
and exited relative to a 2-3 day spell. That is a legitimate causal explanation for *why* the collapse happens, but
it does not make the finding go away — it means the +0.07 headline number is not a robust estimate of a capturable
edge under any execution model other than the one exact convention it was measured on, and it is at odds with the
stated academic mechanism (Bollerslev-Tauchen-Zhou variance-risk-premium predictability), which is documented at
much lower frequency than 2-3-day spells. This inconsistency between claimed mechanism and revealed execution
fragility is flagged here as a causality/robustness issue; its overfitting and mechanism implications are for L2
and L3 to size.

## Finding 3 — MATERIAL — the required per-candidate design note does not exist; the audit trail misrepresents it as complete

DESIGN_BRIEF.md deliverable #3 requires `dev_results/vix_vrp_v2_DESIGN_NOTE.md` with prescribed sections
(Mechanism, Rules, Parameters, Grid summary, Gate results, Stress narrative, Spurious re-entry census, Event
ladders, Iteration count, Honest weaknesses). No such file exists anywhere in the repository
(`find . -iname "*vix_vrp_v2*DESIGN_NOTE*"` returns nothing; only `dev_results/vix_vrp_DESIGN_NOTE.md`, the
*original's* note, exists). `dev_results/vix_vrp_v2_RETURN.json`'s own `design_note` field points to
`"dev_results/vix_vrp_DESIGN_NOTE.md"` — the original's file, not a new one for v2.

This contradicts `PREREG.md`'s deviation log (line 86-88): *"vix_vrp had completed the audit, built and
gate-tested vix_vrp_v2, **written the full design note** and its return JSON (so it is treated as complete...)."*
That claim is false as stated — no v2-specific design note was written. The substantive content that such a note
would contain is not lost (it is distributed across the `signals/vix_vrp_v2.py` module docstring, which is
unusually complete, and the RETURN.json `headline`/`biggest_weakness` fields — both of which this review relied on
and cross-checked against the raw ablation CSVs), so this is not a SEVERE information gap. But the deliverable
contract was not met, and the record used to justify treating the candidate as "complete" enough to trigger the
pre-committed automatic retirement of the original overstates what was actually produced. File the missing note
before this candidate is cited further.

Relatedly, `dev_results/vix_vrp_v2_VERIFY.json`'s `grid_audit` field is `{"error": "no vix_vrp_v2_grid.csv"}` —
the canonical grid file named by DESIGN_BRIEF.md deliverable #2 also does not exist (only `_gridC_grid.csv`,
`_gridD_grid.csv`, `_map.csv` and the two ablation CSVs do), so the mechanical battery's own plateau/rank
cross-check against a single grid could not run. This is the same pattern as the missing design note: real search
artifacts exist, but not filed under the names the process expects, degrading independent auditability.

## Finding 4 — checked, cleared — VIX 16:15-vs-15:59 timing is not a new exposure introduced by rule 3

The coordinator asked whether the new ELEVATED/VRP-gate leg is more sensitive to the accepted 16-minute
VIX-close-vs-decision-time approximation than the original. It is not: `signal()` computes `vrp = vix/100 - rv`
once and reuses it for both rule 2 (the pre-existing crash filter, `vrp < vrp_min`) and rule 3 (the new gate,
`vrp > vrp_elev`) — same `vix_close` series (forward-filled, per `data/build_dataset.py`), same `rv` series
(`features.realized_vol`, a trailing `rolling(window, min_periods=window).std()` — causal, confirmed by reading
`features.py`). Rule 3 carries exactly the same 16-minute approximation as rule 2 already carries in the
(previously accepted) original, no more and no less. The fragility identified in Finding 2 is a same-day
gate-timing/holding-period issue, not this specific approximation.

## Code-level lookahead scan (no findings)

Read `signals/vix_vrp_v2.py` line by line: no `.shift(-k)`, no centered windows, no full-sample statistics
(`vix_regime` is an explicit forward-only Python loop over a NumPy array with only `st` as running state; `rv` is
`features.realized_vol`'s trailing rolling std; `vrp` and the `np.select` leverage assignment are elementwise on
already-causal series). `engine.run` applies `pos = lev.shift(1)` (line 92) so the day-t decision is executed on
day t+1, matching the module docstring's stated contract. `causality_12_cutoffs` in `_VERIFY.json` independently
confirms this: identical signal values whether the market data is truncated at any of 12 cut-off dates or not
(`max_abs_diff: 0.0` throughout). No issue found.

## Minor

* `dev_results/vix_vrp_v2_VERIFY.json`'s `module_constants` scan lists `LEV_CALM` twice, the second entry's
  "value" a truncated slice of the docstring text rather than the real assignment — a scraping artifact in
  `verify_tools.py`, not a signal-file defect. Does not change any finding above (the real assignments were
  confirmed by direct reading of the source, lines 77-79).
* `dev_results/vix_vrp_v2_ablation_round2.csv` row `R2_hold5_a0.10` (a 5-day minimum-hold variant of the gate) posts
  dev_1990 Sharpe **0.7564** — higher than the frozen point's 0.6783 — while the docstring's "Gate form" paragraph
  states flatly that "the smoothed / min-hold / banded forms do not improve the average Sharpe over the threshold
  range." That may be true averaged over the (thin, single-`a`) set of hold-form rows tested, but the single best
  point in the designer's own search beats the frozen default outright and is not mentioned. Worth flagging to L2
  (selection-haircut / plateau-vs-peak) rather than blocking here, since it is a functional-form selection question
  rather than a numeric constant.

---

## Summary for JSON output

* `refuted = true` (Finding 1 and Finding 2 are each independently SEVERE).
* True tunable count: **8** (declared 6 + `LEV_CALM` + `LEV_PANIC`, both shown by the candidate's own ablation CSVs
  to have been value-selected by DEV comparison) — a G7 breach.
* Required disclosures (MATERIAL): the missing `vix_vrp_v2_DESIGN_NOTE.md` / `vix_vrp_v2_grid.csv` deliverables and
  the PREREG.md deviation-log misstatement that the note was written.
