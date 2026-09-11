# volmanaged — L1 verification (Causality & code)

Verifier: adversarial L1, pass 2. Read `signals/volmanaged.py` fully (line-by-line), `dev_results/volmanaged.json`,
`dev_results/volmanaged_DESIGN_NOTE.md`, `dev_results/volmanaged_VERIFY.json`. No `evaluate.py` run, `results/`
untouched, no parameter proposed, no data past 2012-06-30 accessed (all evidence drawn from already-produced DEV
files).

## Finding 1 — SEVERE: true tunable-parameter count breaches G7 (≤6) under the brief's own counting rule

`gate_check.py`'s G7 check is mechanical: `value=5` (== `len(DEFAULT_PARAMS)`), so it reports PASS. But the design
note's own §1b log ("DEV log of structural decisions") documents that at least **four** of the module's UPPER_CASE
"structural constants" were not fixed by convention or mandate but were selected by explicitly comparing DEV Sharpe
/ drawdown across named alternatives — exactly the brief's test for "IS a tuned parameter":

| constant | frozen value | alternatives explicitly compared in DEV (design note evidence) |
|---|---|---|
| `POWER` | 2 | "POWER 1 (inverse vol) vs 2 (inverse variance): p=1 reaches Sharpe 0.429 at tv 0.20 but DD -51%; p=2 at the same Sharpe has DD 10-15 points better ... **POWER = 2 fixed.**" (§1b Batch 1) |
| `EST` | "max2" | plain EWMA hl 5/10/20 (Sharpe 0.411/0.354/0.449), downside semi-vol (0.22-0.32, rejected), two-horizon max2 (0.449, chosen) — "**Structure fixed for the grid: EST = max2**" (§1b Batch 2) |
| `DISCRETE` | False | "Discrete {0,1,2,3} vs continuous: discretising cost 0.03-0.05 Sharpe and DOUBLED the trade count ... **Continuous fixed**" (§1b Batch 1) |
| `WEEKLY` | False | "Weekly band check: no better than daily at equal trade count (0.297-0.404 vs 0.354-0.412). **Daily fixed.**" (§1b Batch 1) |

That already puts the true count at **5 declared + 4 = 9**. Two more constants, `SHOCK_Z`/`SHOCK_DAYS` (frozen at
`0.0, 0` = off), were also set by an explicit DEV comparison ("Shock override (cash 3 sessions after a -3 sigma
day): -0.09 Sharpe at every target vol (0.354 -> 0.263) ... **Dropped; two parameters freed**" — the design note's
own language treats them as two parameters), which the designer chose to turn off based on that comparison. Whether
or not those two are counted (they have zero effect on the frozen signal's output, confirmed by reading `_core`:
`shock_days=0` forces `blocked = zeros`), the count is **9 without them, 11 with them** — both far past the ≤6
budget in `PREREG.md` and the >6 = "G7 breach" threshold this brief names explicitly.

This is not a `len(DEFAULT_PARAMS)` coding bug — `gate_check.py` is doing exactly what it is written to do. The
defect is that the frozen signal file's declared "5 tunables" undercounts the actual DEV-informed search: 756
grid combos over 5 params PLUS a documented, comparison-driven selection among ≥2 forecast-power forms, ≥3
volatility estimators, discrete-vs-continuous, weekly-vs-daily, and (arguably) an on/off shock overlay. The
overfitting/selection-haircut math that G7 exists to bound must be applied to the true search, not the declared
one. **Severity: SEVERE — blocks the OOS look until the true parameter count is disclosed and G7 is re-adjudicated
against it** (this is an L1 code/spec-accuracy finding; its consequence for the Sharpe deflation estimate is for L2).

*(For contrast, `MAX_LEV=3.0` is genuinely structural — external mandate, never varied in any DEV comparison — and
`MIN_PERIODS=20` is the shared library default (`features.ewma_vol`'s own default `min_periods=20`), used
identically and un-varied in `signals/sticky_tier.py` too; neither was chosen by comparing this candidate's DEV
results, so neither counts.)*

## Finding 2 — MATERIAL: the asymmetric band has a proven absorbing floor at/below `band_dn`, and the docstring's
own stated failure mode does not match the empirically observed levels

**Code proof (line 117 of `signals/volmanaged.py`):** the de-lever branch fires only when `(cur - t[i]) > bd`. Since
`t[i]` (= `T_t`) is `.clip(lower=0.0, upper=MAX_LEV)`, `T_t >= 0` always, so `cur - t[i] <= cur`. Once the held
level `cur <= band_dn` (0.30), then `cur - t[i] <= cur <= band_dn`, so the strict inequality `> band_dn` is
**algebraically impossible** from that point on, no matter how much further `T_t` falls (even to exactly 0). The
rule can still *re-lever* (the up-band condition `T_t - cur > band_up` is unaffected), but it can never de-lever a
second time inside the same regime once it has landed at or below 0.30x. This is exactly the coordinator's
hypothesis, confirmed by direct inspection of the clip and the comparison operator — not by running new code.

**Empirical confirmation from already-computed DEV files** (no new harness run needed):
- `leverage_distribution_dev_1990` in `dev_results/volmanaged.json`: 29.4% of dev_1990 days held at exactly
  **0.14x** and 16.8% at exactly **0.20x**; the minimum leverage level ever observed in the whole dev_1990 sample
  is 0.14x — consistent with 0.30 being a hard floor that, once crossed, is never crossed again from above.
- Design-note event ladders (§8): the identical **0.2011x** level holds unchanged from the mid-September-2008
  step-down through the 2008-10-10 Lehman ladder, the 2008-11-20 low (VIX 80.9, its cycle high), and the
  2009-03-09 GFC low five months later — "one band-down move in mid-September 2008 accounts for the entire
  crisis." The 2002-10-09 ladder shows the same at **0.1396x**, unchanged for the entire 638-day, 2.5-year 2000-02
  bear (design note §6: "0 band changes in 638 days").
- The design note itself discloses this in full (§10 item 4, written by the finisher while completing the banked
  work) and correctly derives the same algebraic proof independently, calling it "a previously-undocumented
  structural artifact ... not a bug in shared code."

**Verdict — quirk, not a lookahead/coding defect, but the module docstring's own characterization of this failure
mode is empirically wrong for the two bears it names.** The code faithfully implements the band formula exactly as
stated in the docstring (§3 of the module docstring); there is no code-vs-formula mismatch, and no lookahead is
involved (this is a pure function of trailing-only state). But the docstring's "Known failure modes" list states
"(ii) a bear market at moderate volatility (1969-70, 2000-02) is taken at **0.5-1.5x** the whole way down because
the rule has no directional input" — the actual, exactly-quantified levels reached and then FROZEN in the two
named bears are **0.14x** (2000-02) and **0.20x** (2007-09 GFC), both well below the stated 0.5-1.5x range, and the
mechanism is not "wanders in a band due to no directional input" but "makes exactly one de-lever step, of whatever
size, that becomes permanently un-revisitable once it lands ≤0.30." The docstring's characterization is therefore
materially misleading about both the magnitude and the mechanism of the model's own flagship crash behaviour, even
though the design note (a separate, non-frozen document) discloses the truth in full. **Severity: MATERIAL —
required disclosure in RESULTS.md**; not SEVERE, because the underlying code is a correct, deterministic,
non-lookahead implementation of a legitimate (if under-described) rule, and the true behaviour is already
quantified and available in the design note.

## Finding 3 — confirmed clean: causality battery and lag test (no SEVERE finding here)

- `causality_12_cutoffs` in `dev_results/volmanaged_VERIFY.json`: `ok: true`, `max_abs_diff: 0.0` at all 12
  cutoffs (1992-03-31 .. 2011-08-08) — truncating the data at any cutoff reproduces the signal exactly up to that
  cutoff; no lookahead detected mechanically.
- `lag_test_dev_1990`: base Sharpe 0.4946 -> lag1 0.5249 -> lag2 0.5359, **rising** with added execution delay.
  This is the opposite signature of a same-close-dependence bug (which would collapse Sharpe when the signal can
  no longer see same-day information) — it says the signal has zero same-close dependence and, if anything, the
  engine's assumed one-day execution lag is slightly pessimistic relative to a further-lagged variant on this
  window (plausible: the two-horizon slow EWMA changes little day to day, so an extra day of delay costs little
  and occasionally helps by missing a whipsaw reversal). Not a defect.
- No VIX is used anywhere in this signal (`_core` only reads `df["spx_ret"]`), so the VIX 16:15-vs-15:59 close-timing
  approximation flagged in the brief does not apply to this candidate.
- Manually re-derived the frozen point's headline numbers against `gate_check.py`'s own re-run (design note §5,
  verbatim): `G2_dev1990_sharpe=0.49458` (bar 0.425), `G3_dev1990_maxdd=-19.80%` (bar -30%), `G5=1.78/yr` (bar 25),
  `G6=1.0` (bar 0.5) — all independently consistent with `dev_results/volmanaged.json`'s own `windows.dev_1990`
  block (`sharpe=0.49458`, `max_drawdown_pct=-19.801`, `position_changes_per_year=1.777`). No discrepancy between
  the design note's quoted numbers and the underlying JSON.

## Summary

One SEVERE (Finding 1, parameter-budget undercount), one MATERIAL (Finding 2, docstring failure-mode mismatch —
required disclosure), causality/lag/VIX-timing all clean.
