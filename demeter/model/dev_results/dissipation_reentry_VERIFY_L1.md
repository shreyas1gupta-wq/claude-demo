# dissipation_reentry — VERIFY L1 (Causality & code)

Verifier: adversarial L1, pass 2. Scope: lookahead in any form, `_VERIFY.json` causality battery, lag test,
`DEFAULT_PARAMS` vs declared tunables, and whether every UPPER_CASE module constant is genuinely structural.

## SEVERE

### S1 — `LEV_TIER` is a DEV-compared constant, not a structural one: true tunable count = 7, which breaches G7 (>6)

`signals/dissipation_reentry.py` declares six module-level UPPER_CASE constants (confirmed via
`dev_results/dissipation_reentry_VERIFY.json` → `module_constants`): `RV_WIN`, `LEV_TIER`, `LEV_REBOUND`, `RSI_MAX`,
`Z_SHOCK`, `HYST`. `DEFAULT_PARAMS` has 6 keys and the harness reports `n_tunable_params: 6`
(`dev_results/dissipation_reentry.json`), so `gate_check.py`'s G7 check (`n_tunable_params <= 6`, see `gate_check.py`
line 32) mechanically passes — but that check only counts `signal()`'s keyword arguments; it cannot see whether a
module constant was itself chosen by comparing DEV results, which VERIFY_BRIEF.md explicitly requires this lens to
audit ("a constant whose value was chosen by comparing DEV results IS a tuned parameter").

`LEV_TIER = (1.0, 1.0, 1.0)` (flat 1x default) fails that test. The design note documents an explicit, quantified
DEV comparison between this value and the rejected alternative `(3.0, 2.0, 1.0)` (the incumbent's RV tier):

* Docstring (signal file, lines 6-11): "The incumbent's 3x/2x/1x RV tier … was tested on DEV at the frozen trigger
  parameters and REJECTED because, with no trend filter, it levers into the 1962 and 1973-74 bears: era maxDD -46.9%
  (1950-69) and -43.7% (1970-89), failing gate G4, while flat 1x gives -19.6% / -13.8% at the same dev_1990 Sharpe
  (0.447 vs 0.445)."
* Design note, Iterations 613-616 table (`dev_results/dissipation_reentry_DESIGN_NOTE.md` lines 138-147): three
  variants run and compared head-to-head — incumbent tier 3/2/1 (Sharpe 0.45, maxDD -23.5%, 1950-69 DD -46.9%,
  1970-89 DD -43.7%, **G4 FAIL**), tier 2/2/1 (Sharpe 0.435, G4 "pass (barely)"), flat 1x (Sharpe 0.447, maxDD -12.4%,
  **G4 pass**). The note's own words: "**Structural decision (disclosed as a DEV-informed choice between the two
  defaults the brief allows): flat 1x.**" (line 148) and again at lines 187-189: "Structural choice made on DEV and
  disclosed: default engine flat 1x rather than the incumbent's 3/2/1 tier (both allowed by the brief); the tier
  fails G4 … flat 1x gives -19.6%/-13.8% at the same Sharpe."

This is a textbook case of the exact failure mode VERIFY_BRIEF.md names: a discrete/categorical choice among
candidate structural defaults, selected because one candidate scores better (passes G4, matches Sharpe) than the
other(s) on DEV data. That the designer disclosed it prominently and honestly does not exempt it from the count —
the brief's rule is about the true number of DEV-informed degrees of freedom, not about disclosure. With `LEV_TIER`
counted, **true_tunable_count = 7**, which breaches the pre-registered budget of ≤6 (PREREG.md "Parameter budget: at
most 6 tunable parameters per candidate") and the mechanical G7 bar (`G7_PARAMS = 6` in `gate_check.py`).

Evidence checked and eliminated as innocent: `RSI_MAX=20`, `Z_SHOCK=2.0`, `HYST=0.8`, `RV_WIN=21` and
`LEV_REBOUND=3.0` do **not** appear anywhere in the design note's grids or iteration log as DEV-compared values —
`grep` for "RSI" (excluding the "RSI2"/"RSI(2)" indicator name), "0.8"/"hyster", "Z_SHOCK", and "LEV_REBOUND" in the
design note surfaces zero instances of a numeric comparison across candidate values for any of these five. They are
asserted once each and never revisited. `LEV_TIER` is the only one of the six with a documented multi-value DEV
comparison.

**Consequence:** per PREREG.md's own gate table, a candidate failing any gate is "reported as failures with their
DEV numbers and are never run through `evaluate.py`." G7 is failed under the true count. This blocks the OOS look
until either (a) the flat-1x default is re-justified on grounds that do not rest on the DEV Sharpe/G4 comparison
already run (not possible after the fact — the comparison has been seen), or (b) one of the six declared tunables is
retired to bring the true count to 6, or (c) the Principal/CIO explicitly rules that a binary structural-default
choice pre-declared as "either allowed by the brief" does not count against the budget — a policy call outside this
verifier's remit, but the note as written does not make that argument; it simply reports the comparison.

## MATERIAL

None beyond S1 (which is itself the required disclosure).

## MINOR

### m1 — Burst stop-loss tracker is computed gross of trading cost and financing spread (immaterial in size)

In `signal()`, the burst's own P&L tracker used for the `stop_loss` decision is `cum *= 1.0 + LEV_REBOUND * x_ex[i]`
where `x_ex = spx_tr_ret - rf_daily` — identical to `engine.asset_excess(df, "spx_tr")`, confirmed by reading
`engine.py` lines 45-52. But the engine's actual realised return additionally subtracts `d["lev_fin"]` (financing
spread on the levered leg) and `d["cost"]` (trading cost) — `engine.py` line 103: `ret = rf + pos*x - lev_fin - cost`.
The internal stop-loss accounting is therefore a shade more generous than the net P&L the engine will actually book.
Magnitude: at 60 bp p.a. financing spread on the 2x incremental leverage over a ≤10-session burst, the drag is
≈0.05% cumulative; at 3 bp/trade the entry+exit cost is ≈0.06%. Against a 10% stop threshold this is roughly 1/100th
of the trigger level — not large enough to move any burst's classification (stopped vs not) in the DEV record, but
should be named for completeness since the stop threshold is advertised in the docstring as "the burst's own
cumulative 3x excess return falling to -stop_loss."

### m2 — Docstring overstates the brief's specificity for `RSI_MAX=20` and `vix_min=30`

The signal docstring calls `RSI(2) < 20` "the brief's oversold definition" (line 39 of the signal file) and the
design note calls `vix_min=30` "the brief's floor" (design note line 183). `DESIGN_BRIEF.md` (line 104) only cites
the single historical data point "RSI(2)=8" on 23-Mar-2020 and does not define a general RSI oversold threshold or a
VIX floor value anywhere; `PREREG.md` likewise does not. `RSI_MAX` and the `30` reference point appear to be the
designer's own reasonable conventions (RSI(2)<20 is a standard technical-analysis oversold threshold; `vix_min=30`
is separately grid-searched as one of the six declared tunables, so its provenance claim does not affect the tunable
count). This is a documentation-attribution nit, not a causality or budget defect — flagged only because the brief
explicitly asked this lens to cross-check constant justifications against source documents.

### m3 — "Natural expiry" in the docstring is ambiguous about the double-shock early exit

The docstring states re-entry blocking rules as "After a natural expiry a new burst needs the trigger on a LATER
day; after a stop-out no new burst is allowed for `hold_days` sessions." The code's three exit conditions are
`stopped`, `held >= hold_days`, or `dbl[i]` (a fresh double shock); only `stopped` sets `block_until`. A double-shock
exit is therefore treated identically to a held-days natural expiry (next-day re-entry allowed, no cooldown) even
though the docstring's prose only names "natural expiry" for that lenient case. Confirmed by code read
(`signals/dissipation_reentry.py` lines 119-124): no branch distinguishes `dbl[i]`-triggered exits from
`held >= hold_days` exits for blocking purposes. This is a wording gap, not a behavioural bug — the behaviour is
internally consistent and deterministic, just under-specified in prose.

## Causality checks performed (no defect found)

1. **12-cutoff lookahead battery** (`dev_results/dissipation_reentry_VERIFY.json` → `causality_12_cutoffs`):
   `ok: true`, `max_abs_diff: 0.0` at every one of the 12 cutoffs (1992-03-31 … 2011-08-08, including 2008-10-10 and
   2009-03-09). Signal output computed on data truncated at each cutoff is bit-identical to the same dates' output
   computed on the full series — the strongest available mechanical evidence against any lookahead in the whole
   function, burst tracker included.
2. **Lag test** (`lag_test_dev_1990`): base Sharpe 0.447, lag-1 Sharpe 0.526, lag-2 Sharpe 0.473 — Sharpe does **not**
   collapse when the signal is delayed a session; if anything it rises. A genuine lookahead exploit would be expected
   to collapse under an added delay (the "unfair" future information would be lost); its absence here is consistent
   with, not merely permissive of, a causal signal.
3. **Manual trace of the state machine's day-index alignment** (coordinator's specific question — "the burst P&L
   tracker uses day i excess return while the exit decision is taken at close i"): confirmed causal. `engine.py`
   line 92, `pos = lev.shift(1)`, means the value `signal()` returns at index `i` (`out[i]`) is applied by the engine
   as the position **during day i+1**. Inside the loop, when `state==2` carries into iteration `i` (i.e. a burst
   entered via `out[i-1]=LEV_REBOUND` on a prior close), `cum *= 1 + LEV_REBOUND * x_ex[i]` uses day `i`'s excess
   return to mark the position that is, by the engine's own shift convention, actually in effect on day `i` — the
   correct and only return the burst could have earned. The resulting `stopped`/`held`/`dbl[i]` exit test at
   iteration `i` then uses only information known by the close of day `i` (today's completed return, today's VIX,
   today's RSI, yesterday's RV21 as the shock yardstick via `sigma_prev = (rv/sqrt(252)).shift(1)`) to set `out[i]`,
   which the engine will apply on day `i+1`. No day's return is used to decide that same day's own exposure ahead of
   time, and no day's exposure decision is applied to a return that predates it. Entry into a burst is symmetric: a
   decision at close `i` (`out[i]=LEV_REBOUND`) is first paid the return of day `i+1`, exactly matching when `held`
   and `cum` first increment inside the `state==2` branch — no day of the burst's actual holding period is skipped
   or double-counted.
4. **Same-day re-fire guard**: `if state != 2 and dis[i] and not exited and i >= block_until` — the `not exited`
   term (confirmed in code) prevents a burst that exits on close `i` from re-entering on that same close, matching
   the docstring and the design note's own account of a bug it caught and fixed before freezing (design note lines
   109-114, "the loop allowed a same-day re-fire after a burst exit, contradicting the docstring; now a natural
   expiry blocks re-entry for that close only").
5. **Feature causality** (`features.py`): `realized_vol` (`rolling(...).std()`), `rsi` (`ewm(..., adjust=False)`) and
   the `vix.rolling(vix_win).max()` used for the dissipation trigger are all trailing/backward windows including the
   current row, no centering, no `.shift(-k)`, consistent with the 12-cutoff battery passing exactly.
6. **`double_shock` construction**: `shock_day = ret < -Z_SHOCK * sigma_prev` where `sigma_prev` is `rv.shift(1)` —
   yesterday's realised vol used as today's yardstick, exactly as the docstring claims ("so a shock cannot inflate
   its own yardstick"); `double_shock = shock_day & shock_day.shift(1)` looks only at today and yesterday, never
   forward.

## Answer to the coordinator's specific L1 question

"Confirm the burst P&L tracker's day-i-excess-return-vs-close-i-decision is causal" — **confirmed causal**, both by
direct code trace against `engine.py`'s `pos = lev.shift(1)` convention (item 3 above) and by the mechanical 12-cutoff
battery returning `max_abs_diff: 0.0` at every cutoff, several of which (2008-10-10, 2009-03-09) fall inside the
exact window the burst mechanism is built to operate in.

"Check every UPPER_CASE constant against the note for DEV-based choice" — five of six (`RV_WIN`, `LEV_REBOUND`,
`RSI_MAX`, `Z_SHOCK`, `HYST`) are asserted once, never compared across values in the design note, and are reasonably
treated as structural. The sixth, `LEV_TIER`, was explicitly chosen by a three-way DEV Sharpe/G4 comparison
documented in the design note's own iteration log — see **S1**.
