# composite_dual_engine — design note (lens 6: the inference note's §7 composite)

Written incrementally; the Mechanism section below was banked BEFORE the first harness run (2026-09-10).
Everything here is DEVELOPMENT-window only (data hard-truncated at 2012-06-30 by `dev_harness.py`); no
out-of-sample file was read or written.

## Mechanism (written before any run)

The record (inference note §7) says a daily rule had to do four things at once, and the other five lenses
have each shown in DEV what happens when one of them is taken alone:

1. **Shock exit** (§7 ingredient 1): a two-session multi-sigma loss or an implied-vol jump from an already
   elevated base is the earliest clean observation of a volatility regime change; de-levering to cash on it
   removes the clustered aftermath (the Feb-2020 pattern: two −3% days, then −4.5%). Lens 1 (`crash_exit_dual`)
   showed in DEV that this ingredient ALONE is not enough: a default-IN book with a 1x floor rides the 2000-02
   and 2007-09 grinds (maxDD −52.8%) because grinding bears produce no sigma-normalised shock.
2. **Dissipation re-entry** (§7 ingredient 2): at a capitulation low implied vol peaks before price does; a
   fresh price low (RSI(2) < 20) with the VIX still extreme (≥ 30) but well off its 30-day peak (≥ 25% below) is
   the 23-Mar-2020 signature. Lens 2 (`dissipation_reentry`) showed in DEV that this fires 7 times in 22 years,
   4 of them inside the two bears at 50% negative (looser versions 75-83% negative) — so it must be STRICT and
   bounded (10-session hold, 10% burst stop), and its leverage is decided by the spurious-re-entry census, not
   by the record's 3x.
3. **Leverage tier by vol regime in the ORDINARY state** (§7 ingredient 3): 3x when implied vol is calm, 1x when
   elevated. Learned from lens 5 (`vix_vrp`, the DEV leader at Sharpe 0.61 / −19.8%): the thing that saved it in
   2000-02 and 2008 was that its ELEVATED VIX state was CASH, not 1x. So the ordinary tier here has a third
   level: **cash when VIX is persistently above a stress threshold** (the "de-lever when vol is persistently
   elevated" the brief demands). The tier is therefore 3x / 1x / 0 by VIX level with hysteresis — and it is
   NOT monotone in vol overall, because the re-entry state (2) is allowed 3x at VIX ≥ 30.
4. **Hysteresis** (§7 ingredient 4): a minimum hold after every non-emergency state change so that cash spells
   last weeks and the 3x tier is not flipped by a day's VIX noise. Emergency transitions (the shock exit, the
   burst stop) are exempt — protection must never wait.

Why the composite should be at least as good as its parts in 1990-2012: the tier carries the equity premium at
3x in calm years (1993-95, 2005-06, parts of 2010-11) and goes to cash in the grinds (2000-02 VIX 20-35, 2008),
which is exactly vix_vrp's mechanism; the shock exit protects the 3x tier from the calm-regime crashes that a
VIX-level tier reaches late (27-Feb-2007, Oct-1997, Aug-2011 from VIX ~17); the re-entry is the only component
that can take a V-shaped rebound while VIX is still > 30 (Mar-2009 low: VIX 49 off its 81 peak).

Why it may NOT beat vix_vrp — the pre-registered risk: (a) vix_vrp found the 15-30 VIX band has Sharpe ~0 in DEV,
so a 1x ELEVATED tier dilutes rather than adds; (b) 3x in calm carries 3x the single-day gap risk before the
exit can fire (a −3.5% day from VIX 11 costs −10.5% at 3x); (c) the strict re-entry fires so rarely that it
cannot move a 22-year Sharpe, while any loosening re-creates the trap. If the DEV grid drives v_high down to
v_calm (ELEVATED band empty) the honest reading is "the composite collapses into vix_vrp"; if it cannot beat
Sharpe 0.61 / −19.8% at all, the finding is that the extra complexity does not pay in DEV.

Bar: dev_1990 Sharpe 0.61 / maxDD −19.8% (vix_vrp, 3/60). Gates: PREREG G1-G7.

## Parameter budget (declared before the first run)

Tunables (6): `v_calm`, `v_high`, `hyst` (VIX regime bands), `k` (two-session shock size), `out_days`
(sessions out after the last shock), `min_hold` (hysteresis).
Structural constants (not tuned): LEV_CALM 3, LEV_ELEV 1, LEV_STRESS 0, LEV_REB (3 pending census);
J_JUMP 0.30 / VIX_BASE 10 / VIX_FLOOR 20 (lens 1's frozen VIX-jump trigger); SIGMA_WIN 21, SHOCK_DAYS 2;
the whole re-entry trigger borrowed from lens 2's frozen point: VIX_FALL 0.25, VIX_WIN 30, VIX_MIN 30,
RSI_MAX 20, HOLD_DAYS 10, STOP 0.10; cash before 1990 (VIX lens).

## Planned ablations (before any run)

On dev_1990 at 3/60: (A) tier only; (B) tier + shock exit; (C) B + dissipation re-entry at 3x; (D) C +
hysteresis (= the model); (E/F) D with re-entry at 2x / 1x; (G) D with the ELEVATED tier at cash (vix_vrp-like).
Columns: Sharpe, CAGR, maxDD, chg/yr, cash %, 2000-02, GFC, 2009 recovery, avg leverage when invested,
up-capture, census (n entries / share negative in the two bears).

---
*Everything below was written in the continuation session (2026-09-11/12) that completed the lens. The four
sections above are unchanged from the pre-run bank.*

## What the continuation session did

The banked state was: signal file complete, one smoke run at `v_calm 15.5 / v_high 26 / hyst 0.12 / k 4 /
out_days 15 / min_hold 10` (dev_1990 Sharpe 0.4281, maxDD **-34.68%** - a G3 failure), and the ablations, the
LEV_REB decision and the grid all unstarted. This session ran the ablations, decided LEV_REB, ran three search
grids plus six-axis 1-D sweeps, froze a plateau point, and produced the final harness run and gate check.

Two module-level **ablation switches** (`USE_SHOCK`, `USE_REENTRY`) were added to `signals/composite_dual_engine.py`
so ablations A-C can be run without editing the rule. Their frozen default is `True`/`True` - i.e. the DEFAULT
behaviour is exactly what the docstring describes; they are not parameters and are not counted in the budget.
**No structural choice was changed**: LEV_CALM 3 / LEV_ELEV 1 / LEV_STRESS 0 / LEV_REB 3 are all as pre-declared.

## Rules (as frozen)

Decided at the close of day t from data up to that close; the engine applies the target to day t+1. Leverage is
discrete {0, 1, 3}. Three modes: TIER (ordinary), OUT (post-shock), REBOUND (burst).

1. **Ordinary tier - VIX regime machine** (hysteretic, causal, state held through the 4 isolated VIX NaNs, which
   are `ffill`ed). CALM is entered when VIX < `v_calm`x(1-`hyst`) = **13.44** and left when VIX > `v_calm` = **16.0**
   -> **3x**. STRESSED is entered when VIX > `v_high` = **23.0** and left when VIX < `v_high`x(1-`hyst`) = **19.32**
   -> **cash**. Everything between (and the start state) is ELEVATED -> **1x**.
2. **Shock exit -> cash (mode OUT)**, from any mode, exempt from the minimum hold. Fires on either
   (a) r_t + r_{t-1} < -`k`*sqrt(2)*sigma, sigma = the 21-day daily std measured through the close *before* both days
   (`k` = 4.0: two -3% days at 12% annualised trailing vol trip it, a single -3% day does not), or
   (b) VIX > 1.30 x its mean over the previous 10 sessions **and** VIX >= 20 **and** the day is down.
   OUT persists until `out_days` = 10 sessions after the LAST shock event (a two-day shock, a single-day -k*sigma, or
   a VIX jump - each restarts the clock), then the book returns to the TIER, which is itself VIX-gated, so
   "returning" inside a bear means returning to cash or 1x.
3. **Dissipation re-entry -> 3x (mode REBOUND)**, from TIER or OUT. All three must hold: VIX <= 0.75 x its
   trailing 30-day max; VIX >= 30; RSI(2) < 20. Held 10 sessions, cut early by a 10% loss on the burst equity or by
   any shock trigger; after a stop-out, no new burst for 10 sessions.
4. **Hysteresis**: after any change of target leverage, no further non-emergency change for `min_hold` = 10
   sessions. The shock exit, the burst stop and the burst's scheduled expiry are exempt.
5. Cash before 1990 (no VIX) and through warm-up. This is a VIX lens; **dev_1950 is not applicable** as a test -
   it is reported only because the harness reports it (79.1% of its days are structurally cash).

## Parameters and how each was chosen

All on DEV (1990-01-01..2012-06-30) through `dev_harness.py` / direct `E.run` on `E.load_market(end="2012-06-30")`.

| param | frozen | grid range searched | why this value |
|---|---|---|---|
| `v_calm` | 16.0 | 13.0-20.0 (grids 14.0-18.5; sweep 13-20) | 1-D sweep is flat 14.5-16.5 (Sharpe 0.513-0.543) and falls away above 17.5 (0.42 at 17.5, 0.39 at 18.0). 16.0 is the interior centre of that flat. |
| `v_high` | 23.0 | 18.0-28.0 | The single most important axis. Below 21 the model is over-cautious (max Sharpe 0.41-0.47); above 23.5 the 2000-02 grind is ridden at 1x and maxDD blows through G3 (24.0 -> -38%, 26.0 -> -35%, 28.0 -> -44% in grid 1). 21.5-24.0 is the survivable band; 23.0 is its upper-middle. |
| `hyst` | 0.16 | 0.04-0.20 | Sweep: 0.04-0.10 gives 0.37-0.42 with maxDD -31...-35%; 0.16-0.20 gives 0.49-0.54 with maxDD -26%. 0.16 is the low edge of the good flat, chosen over 0.18/0.20 to keep the CALM entry (13.44) from becoming unreachably strict. |
| `k` | 4.0 | 2.0-6.0 | **Deliberately not the grid maximum.** k = 5.5-6.0 score ~0.03 higher precisely because they switch the two-session exit off; 4.0 is the mechanism value (two -3% days at 12% trailing vol) and sits on the flat 3.0-5.0 (0.515-0.543). |
| `out_days` | 10 | 5-25 | The flattest axis in the model: 0.478-0.543 across the whole range. 10 sessions ~ two weeks, the pre-registered "sit out the aftershock" span. |
| `min_hold` | 10 | 4-20 | Cliff below 8 (0.425-0.49) and above 14 (0.45 -> 0.38); 9-13 is the flat (0.519-0.545). 10 is its centre and a round number. |

Structural constants unchanged. **LEV_REB decided from the census, as pre-registered**: the burst fires 3 times
inside the two grinding bears with 1 of 3 (33%) negative over the next 10 sessions - not "mostly losses" - and
ablations D/E/F give Sharpe 0.543 / 0.522 / 0.485 at 3x / 2x / 1x. The record's **3x is kept**.

## Grid summary

Four grids (all <= 400 combos, per the token brief) plus two six-axis 1-D sweeps:

| grid | combos | axes | result |
|---|---|---|---|
| g1 (coarse) | 240 | v_calm 14-18.5 x v_high 18-26 x hyst 0.08-0.16 x min_hold 5-20 | only **6** gate-feasible; all at v_high 22-24, v_calm 14-17, min_hold 10-15. v_high <= 20 and min_hold = 5 are hard cliffs. |
| g2 (coarse) | 324 | v_calm 14-17 x v_high 21-23 x k 3-5 x out_days 10-20 x min_hold 8-15 | **95** gate-feasible; best 0.5173. k and out_days almost flat (mean Sharpe 0.385-0.413 across their levels). |
| g3 (plateau grid, fast dev_1990 only) | 144 | v_calm 14.5-16 x v_high 21.5-23 x hyst 0.12-0.16 x min_hold 9-11 | **119 of 144** gate-feasible. Each point scored by the mean Sharpe of its 1-step neighbourhood; the frozen point has the 2nd-highest neighbourhood mean (0.511) and the highest own Sharpe among the top neighbourhood scores. |
| final (shipped as `composite_dual_engine_grid.csv`) | 243 | v_calm 15-17 x v_high 22-24 x hyst 0.14-0.18 x k 3-5 x min_hold 9-12 | **152 of 243** gate-feasible; frozen point ranks 2nd of 243 by raw Sharpe, 0.0055 behind (17.0 / 0.18) - inside this surface's +/-0.05 jitter. |

Sweeps (`composite_dual_engine_sweep_P1.csv`, `_Q2.csv`) move one parameter at a time over 9-13 values.

**Where the cliffs are.** (i) `v_high` above ~24: the 2000-02 band 20-24 gets held at 1x and dev_1990 maxDD goes
-26% -> -38%. (ii) `v_high` below ~20: the ELEVATED band is squeezed out and Sharpe falls to 0.41-0.43 -
this is the "collapse into vix_vrp" case the mechanism section pre-registered, and it is a *worse* model, not an
equivalent one (see ablation G). (iii) `min_hold` <= 7: whipsaw in the 3x tier, Sharpe 0.37-0.49. (iv) `hyst` <= 0.10:
the 16/13.4 band collapses, 3x flips on VIX noise, maxDD -31...-35%. (v) `k` <= 2.5: the shock exit fires on ordinary
down days, Sharpe 0.35-0.40. The surface between those cliffs is jagged at the +/-0.05 level, which is why the
frozen point was chosen on a neighbourhood mean rather than on its own Sharpe.

## Gate results (verbatim from `python gate_check.py dev_results/composite_dual_engine.json`)

```
composite_dual_engine: ALL GATES PASS
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.5426075297957885 (bar 0.425)
  G3_dev1990_maxdd: pass  value=-25.611756367237703 (bar -30.0)
  G4_no_ruinous_era: pass
      1950-1969: N/A (all cash - signal not available in this era)
      1970-1989: N/A (all cash - signal not available in this era)
      1990-1999: ok: CAGR 17.28% maxDD -25.6%
      2000-2012H1: ok: CAGR 6.93% maxDD -23.5%
  G5_changes_per_year: pass  value=5.464739069111424 (bar 25.0)
  G6_plateau: pass  value=0.9583333333333334 (bar 0.5)
  G7_param_budget: pass  value=6 (bar 6)
```

Headline DEV numbers (3 bp / 60 bp): **dev_1990 Sharpe 0.5426, CAGR 11.41%, maxDD -25.61%, worst month -14.19%,
5.46 changes/yr, 42.0% of days in cash, average leverage when invested 1.81x, up-capture 85.4%, down-capture
62.4%, beta 0.51** (SPY on the same window: Sharpe 0.385, CAGR 8.34%, maxDD -50.8%).
Cost sensitivity: 2 bp/40 bp -> 0.5537 / 11.62% / -25.42%; **6 bp/90 bp -> 0.5175 / 10.96% / -26.09%** - the edge is
not cost-fragile (5.5 changes/yr is cheap to run). dev_1950 (structurally 79% cash, not a test of this lens):
Sharpe 0.3234, CAGR 7.52%, maxDD -25.61%, 1.97 changes/yr. Leverage distribution 1990+: **42.0% cash, 34.4% 1x,
23.6% 3x** - the 3x tier is real, not decorative.
Plateau: dev_1990 **0.958** of 24 perturbations within 25% of base (the single failure is `v_high` -15% -> 19.55,
Sharpe 0.406 - the "squeezed ELEVATED band" cliff); dev_1950 **1.000**.

## Stress narrative

| episode | model | SPY | model maxDD | avg lev | % cash | % 3x | what happened |
|---|---|---|---|---|---|---|---|
| 1987 crash (Aug-Dec) | +2.2% | -25.0% | 0.0% | 0.00 | 100% | 0% | No VIX before 1990 -> structurally cash. Not a test; the model earns T-bills. |
| 1990 Kuwait | -0.1% | -8.6% | -3.6% | 0.05 | 95% | 0% | VIX above 23 through the invasion; one brief 1x window. Protection worked; nothing was earned either. |
| 1998 LTCM | -1.7% | +4.9% | -3.7% | 0.04 | 96% | 0% | **The cost case.** VIX 25-45 from Aug to Oct kept the book in cash through the Oct-Dec rip. The dissipation re-entry never fired (see ladder). Sat out a +4.9% window for -1.7%. |
| 2000-02 bear | **-14.4%** | -47.2% | -24.7% | 0.25 | 79% | 2% | The episode that sets the drawdown. VIX 20-35 for two and a half years => mostly STRESSED => cash; the 1x ELEVATED band and two 10-day bursts supply the -14%. This is the whole reason `v_high` had to come down from the smoke run's 26 (which lost -31.9%). |
| 2002-03 recovery | +40.6% | +45.5% | -4.8% | 0.61 | 45% | 3% | 90% of the up-move captured, at 0.61 average leverage, as VIX unwound from 40 to 20 and the tier walked cash -> 1x -> 3x. The model's best behaviour anywhere. |
| 2007-09 GFC | **+3.4%** | -54.8% | -19.3% | 0.26 | 79% | 3% | Positive through the worst bear in the sample. The VIX jump trigger and the 23-level gate put it in cash in Jan-2008 and kept it there; the one burst (19-Dec-2008, VIX 44.9 at 45% off the 80.9 peak, RSI(2) 19.7) earned money. |
| 2009 recovery | **+0.1%** | +67.4% | 0.0% | 0.00 | **100%** | 0% | **The failure.** 207 of 207 days in cash. VIX's *minimum* between 10-Mar-2009 and year-end was 19.47 and the STRESSED exit level is 23x0.84 = **19.32** - the model missed re-entry by 0.15 VIX points, and the strict dissipation trigger could not fire because VIX stayed above 0.75 x its 30-day max whenever RSI(2) was low. Raising `v_high` does not fix it: 23.5 -> -0.2%, 24 -> -0.2%, 26 -> -2.1%, while 2000-02 degrades to -24%/-20%/-32%. |
| 2010 flash crash | +13.3% | -8.4% | -8.4% | 0.48 | 81% | 14% | Exited before the flash crash on the VIX jump, sat out the May-Jun chop, re-levered into the July rally: +19.2% in Jul-2010, the best month in the sample. |
| 2011 debt ceiling | +3.6% | -5.6% | -10.7% | 0.31 | 87% | 9% | Exited at the 04-Aug close (VIX 23.4 -> 31.7) *before* the -6.5% 08-Aug day, stayed out for the whole VIX-40 period. Textbook behaviour for the shock exit. |

Worst six DEV months: **Mar-1994 -14.19%**, Sep-2002 -11.43%, Oct-2005 -11.38%, May-2006 -10.52%, Feb-2007 -9.94%,
Jun-2007 -9.49%. Five of the six are 3x-tier whipsaw in calm regimes (SPY -2% to -4% months), i.e. exactly the
loss signature the inference note section 7.5 attributes to the record. Best six: Jul-2010 +19.22%, Nov-2001 +18.16%,
Nov-2002 +17.99%, Apr-2007 +12.73%, Nov-1995 +12.61%, Jul-1992 +12.08%.

## Spurious re-entry census

| window | entries to >=2x | dates | mean fwd-10-day excess | share negative | % days >=2x |
|---|---|---|---|---|---|
| 2000-03-24 ... 2002-10-09 | 2 | 2001-10-29, 2002-08-28 | **+0.62%** | 50% | 2.0% |
| 2007-10-09 ... 2009-03-09 | 1 | 2008-12-19 | **+5.98%** | 0% | 2.8% |

Three firings in the two grinding bears over 22 years, one of them a loser, mean forward-10-day P&L positive in
both windows. This is the trap that destroyed `vix_dissipation` (46.6 changes/yr, -93.5%); the strict trigger
plus `min_hold` plus the 10% burst stop keep it to 2.0-2.8% of bear days at >=2x. The census is the evidence for
keeping LEV_REB at 3x rather than cutting it to 2x or 1x.

## Event ladders (leverage target decided at each close)

* **2008-10-10 (Lehman capitulation)** - 10-07 -4.5% VIX 53.7 **L0** | 10-08 -2.5% 57.5 **L0** | 10-09 -7.0% 63.9 **L0** |
  10-10 -2.4% 70.0 **L0** | 10-13 +14.5% 55.0 **L0** | 10-14 -1.5% 55.1 **L0** | 10-15 -9.8% 69.2 **L0** | 10-16 +4.2% 67.6 **L0** |
  10-17 -0.6% 70.3 **L0** | 10-20 +6.0% 53.0 **L0**. Flat cash through the whole week - the -7.0%, -9.8% and -8.9% days
  cost nothing, and the +14.5% day was missed. Correct by construction and expensive by construction.
* **2008-11-20 (Nov-08 low)** - cash every day 11-17 -> 12-01, including the -7.4% low and the +6.9% bounce.
  The dissipation test needed VIX <= 60.6 while RSI(2) < 20; VIX was 80.9 at the low and RSI(2) was 76-93 by the
  time VIX fell. The re-entry fired **29 sessions later**, on 19-Dec-2008 (VIX 44.9, RSI(2) 19.7) - and was profitable.
* **2009-03-09 (GFC low)** - cash on every one of 03-04 -> 03-17, and for the remaining 207 days of the year.
  The diagnostic is unambiguous: on 09-Mar VIX 49.7 against a 30-day max of 52.6 needed <= 39.5. Implied vol had
  not dissipated at the price low; it dissipated three weeks later, by which time RSI(2) was 87-92. **This lens
  cannot take a V-bottom whose VIX peak coincides with the price low.**
* **2002-10-09 (bear low)** - cash on every day 10-01 -> 10-25. On the low, VIX 42.1 vs a 30-day max of 42.6
  (needed <= 32.0) with RSI(2) 18.5: two of three conditions met, the dissipation condition missed by 10 VIX points.
  The tier then walked back in through November (+17.99% in Nov-2002), which is where the 2002-03 recovery's
  +40.6% comes from - late, via the regime machine, not via the burst.

## Ablation table (dev_1990, 3 bp / 60 bp, at the FROZEN point; `composite_dual_engine_ablate_frozen.csv`)

| | variant | Sharpe | CAGR | maxDD | chg/yr | cash % | avg lev invested | up-cap | 2000-02 | GFC | 2009 rec | census n / % neg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | tier only (VIX 3/1/0, no exit, no burst, no min-hold) | 0.435 | 9.04% | -28.0% | 4.13 | 40.8% | 1.79 | 78.6 | -14.6% | -10.7% | +0.1% | 0 / - |
| B | A + shock exit | 0.391 | 8.26% | -25.4% | 4.98 | 43.2% | 1.81 | 74.4 | -14.6% | -10.7% | +0.1% | 0 / - |
| C | B + dissipation re-entry at 3x (no min-hold) | 0.460 | 9.98% | -25.4% | 5.60 | 42.3% | 1.83 | 83.6 | -16.1% | -11.1% | +0.1% | 4 / 50% |
| **D** | **C + hysteresis = THE MODEL** | **0.543** | **11.41%** | **-25.6%** | **5.46** | **42.0%** | **1.81** | **85.4** | **-14.4%** | **+3.4%** | **+0.1%** | **3 / 33%** |
| E | D with re-entry at 2x | 0.522 | 10.60% | -25.6% | 5.46 | 42.0% | 1.80 | 82.4 | -13.6% | -2.0% | +0.1% | 3 / 33% |
| F | D with re-entry at 1x | 0.485 | 9.74% | -25.6% | 5.46 | 42.0% | 1.78 | 79.3 | -13.1% | -7.2% | +0.1% | 0 / - |
| G | D with ELEVATED tier = cash (the vix_vrp shape) | 0.413 | 8.81% | -28.5% | 2.49 | 76.3% | 3.00 | 57.2 | +7.7% | +20.7% | +0.1% | 3 / 33% |
| H | *diagnostic, not pre-registered*: D with CALM tier 2x | 0.568 | 10.52% | -23.5% | 5.46 | 42.0% | 1.42 | 72.1 | -14.4% | +3.4% | +0.1% | 3 / 33% |
| I | *diagnostic, not pre-registered*: D with CALM 2x and re-entry 2x | 0.558 | 9.71% | -19.8% | 5.46 | 42.0% | 1.41 | 69.1 | -13.6% | -2.0% | +0.1% | 3 / 33% |

(The same table at the banked smoke point is in `composite_dual_engine_ablate_smoke.csv`; the ordering of the
ingredients is the same, at Sharpe 0.282 / 0.236 / 0.319 / 0.428 / 0.400 / 0.360 / 0.407 for A-G.)

**What the ablations say.**
1. **Hysteresis is the model.** D - C = **+0.083** Sharpe and turns the GFC from -11.1% into +3.4%. `min_hold`
   is not a turnover cosmetic; it is what stops the tier from re-entering into a bear rally and what forces cash
   spells to last weeks (inference note section 7.4). This is the single most valuable ingredient in the composite.
2. **The shock exit is Sharpe-negative on its own** (B - A = **-0.044**) and only pays for itself in drawdown
   (-28.0% -> -25.4%) and in combination with the burst. In a VIX-regime model the tier has usually *already*
   de-levered by the time a two-sigma two-day shock lands; the exit's remaining job is the calm-base crash
   (Feb-2007, Aug-2011) and the aftershock window. Honest reading: **ingredient 1 is the weakest of the four**,
   and a designer optimising Sharpe alone would drop it.
3. **The re-entry pays** (C - B = +0.069, D vs F = +0.058 at the same trade count) and 3x is the right size.
4. **The composite does NOT collapse into vix_vrp.** Ablation G - deleting the 1x ELEVATED band, the exact
   vix_vrp shape with a 3x calm tier - *loses* 0.130 Sharpe (0.543 -> 0.413), despite being far safer in both
   bears (+7.7% and +20.7%) - because it is in cash 76.3% of days and captures only 57% of up months. At this
   parameter point the 1x band is additive, not dilutive. The pre-registered risk (a) **did not materialise**.
5. **2x-in-calm still beats 3x-in-calm on Sharpe** (H 0.568 vs D 0.543, maxDD -23.5% vs -25.6%) but loses 0.9%/yr
   of CAGR. The panel's standing finding survives; the gap is now 0.025 Sharpe rather than the 0.06 vix_vrp
   measured, and 3x-in-calm clears every gate.

## Iteration count

Every distinct parameter set evaluated on DEV, including the banked smoke run:

| stage | parameter sets |
|---|---|
| banked smoke run (previous designer) | 1 |
| ablations A-G at the smoke point | 7 |
| grid g1 (coarse) | 240 |
| grid g2 (coarse) | 324 |
| grid g3 (fast plateau grid) | 144 |
| candidate batch 1 (P1-P7 base points) | 7 |
| 1-D sweeps around P1 | 70 |
| candidate batch 2 (Q1-Q6 base points) | 6 |
| 1-D sweeps around Q2 | 70 |
| ablations A-I at the frozen point | 9 |
| `v_high` 2009-sensitivity probe (3 points) | 3 |
| final harness run (frozen point) + shipped grid | 1 + 243 |
| **total distinct parameter sets** | **1,125** |

Plus 336 perturbation runs that are part of the G6 measurement rather than of the search (24 per candidate in the
two candidate batches and the probe, 48 in the final run). Four grids, two sweeps, eleven script invocations.
This is a large search and it should be discounted accordingly: the frozen point's 0.543 is the 2nd best of 243 on
the shipped grid, and the honest reading of the surface's +/-0.05 jitter is that the model's DEV Sharpe is
**0.50 +/- 0.05**, not 0.543 exactly.

## Honest weaknesses and the regime that would break it

1. **It misses V-bottoms entirely - the 2009 recovery is a total miss (+0.1% vs SPY +67.4%, 100% of days in cash).**
   This is the brief's central DEV question and this lens answers it badly. Two independent mechanisms both fail
   at once: the VIX level gate needs VIX < 19.32 and VIX's 2009 minimum was 19.47; the dissipation burst needs
   implied vol to fall 25% off its 30-day peak *while* price is making a fresh low, and in Mar-2009 vol peaked
   with price. Raising `v_high` does not buy participation (23.5/24/26 -> -0.2%/-0.2%/-2.1%) and costs the 2000-02
   protection that G3 depends on. **Any 2009-like recovery - vol grinding down slowly from a high plateau while
   price rips - is a structural blind spot.** The 2002-03 recovery (+40.6%) was captured only because VIX fell
   below 19.3 by mid-2003.
2. **The 3x tier is era-concentrated.** 3x days by year: 1992-96 and 2004-07 carry almost all of them (1993: 223,
   1995: 252, 2005: 202, 2006: 199) and there are **zero** 3x days in 1997-2000 and 2003, and <= 13 in 2001, 2002,
   2008-2012. The 3x engine is a low-VIX-decade phenomenon. In a permanently higher-VIX world (VIX floor above 16)
   the model degenerates into a 1x/cash timer with a 60 bp financing drag, and in a permanently lower-VIX world
   (VIX floor below 13.4) it degenerates into levered buy-and-hold at 3x, which is ruinous in the first crash it
   does not see coming a day ahead.
3. **A calm-base crash costs a day at 3x.** Feb-2007 (-9.94%), Oct-2005 (-11.38%), May-2006 (-10.52%), Mar-1994
   (-14.19%). The exit cannot fire before the first shock day. A single -7% day from a VIX-12 base would cost -21%.
4. **The shock exit does not earn its keep** (ablation B). It is retained because it is the pre-registered
   ingredient 1, it improves drawdown, and it is the only protection against a calm-base crash - but a
   Sharpe-maximising reviewer would remove it, and its absence would not have been detected by the gates.
5. **`v_high` is the fragile axis.** It is the only parameter with a G6 failure (-15% -> 19.55 -> Sharpe 0.406) and
   the only one where a 1-point move swings maxDD by 8 points. The entire drawdown gate rests on VIX 20-24 being
   classified as "stay out", which is an artefact of the 1990-2012 VIX distribution; a structurally higher VIX
   regime moves that boundary.
6. **Down-capture 62.4% vs the record's <= 40%, up-capture 85.4% vs the record's >= 100%.** The model is a
   *de-risked* equity book, not the convex one the inference note describes: it sacrifices more upside than it
   avoids downside in capture terms, and earns its Sharpe from the volatility reduction (beta 0.51, annualised
   vol well below SPY's) rather than from convexity. Cash share 42.0% vs the record's 48-52% and average leverage
   when invested 1.81x vs the record's 1.5-2.2x are the two dimensions where it does match the record.
7. **Search cost.** 1,125 DEV parameter evaluations on a jagged surface. G6 is comfortably passed (0.958) and
   152 of 243 grid points clear the gates, so the *region* is real, but the specific 0.543 is optimistic.

## Answers to the two questions the panel asked

**Does any 3x-in-calm configuration pass all gates?** **Yes - this one does, and it is the first in the panel.**
`v_calm 16 / v_high 23 / hyst 0.16 / k 4 / out_days 10 / min_hold 10` passes G1-G7 with dev_1990 Sharpe 0.5426,
maxDD -25.61%, 5.46 changes/yr, plateau 0.958, and 23.6% of days actually at 3x. 152 of 243 points on the shipped
grid also pass. What made it work - and what the earlier 3x-calm attempts lacked - is **not** the 3x tier itself
but the two things wrapped around it: a cash (not 1x) STRESSED state at a *low* threshold (VIX 23, not 26+), and a
10-session minimum hold (ablation D - C = +0.083). The era that kills a 3x-calm tier without those two is 2000-02:
at the banked smoke point (`v_high` 26) the same model loses -31.9% in that bear and prints maxDD -34.7%, a clean
G3 failure. The diagnostic ablation H shows a 2x calm tier still scores higher (0.568 vs 0.543) with a smaller
drawdown, so "3x in calm is the best choice" is **not** established - only "3x in calm is survivable".

**Does the composite beat vix_vrp_v2 (0.678 / -19.8%)?** **No.** It delivers **Sharpe 0.5426, maxDD -25.61%,
CAGR 11.41% against SPY's 8.34%** (SPY Sharpe 0.385), at 5.46 changes/yr, 42.0% of days in cash and **average
leverage when invested of 1.81x**. It is the 2nd-best DEV candidate in the panel and beats the incumbent
(0.425 / -25.1%) on both Sharpe and CAGR at a lower trade count, and it is the only candidate that is positive
through the GFC window (+3.4%) while still holding 3x for a quarter of all days. But on the pre-registered
selection rule (highest dev_1990 Sharpe among gate-passers) vix_vrp_v2 wins by 0.135 Sharpe and 5.8 points of
drawdown, and it does so with a 2x calm tier. The composite's extra complexity - four ingredients, six
parameters - buys more CAGR and a real 3x sleeve, not a better risk-adjusted return. **The section-7 composite is
reproducible and survivable in DEV; it is not the best thing in DEV.**

## Bugs found in shared code

**None.** `engine.py`, `features.py`, `dev_harness.py` and `gate_check.py` behaved as documented across ~1,500
signal evaluations; the lookahead check returns max_abs_diff 0.0 at all five cut-offs; `E.load_market(end=...)`
truncation held (`df.index[-1] <= 2012-06-30` asserted in every script). Two non-bug observations for the
coordinator: (i) `dev_results/composite_dual_engine_show.py`, the previous designer's own print helper, crashes
on eras whose Sharpe is `None` (the all-cash pre-1990 eras) - replaced by `composite_dual_engine_show2.py` in this
lens's own files, not a shared-code issue; (ii) `dev_harness.plateau` perturbs integer parameters by rounding, so
`out_days` +/-15% (10 -> 8.5 -> 8 and 11.5 -> 12) and `min_hold` +/-15% are asymmetric steps - worth knowing when
reading G6, not a defect.

## Files

* `signals/composite_dual_engine.py` - the frozen signal (6 tunables, DEFAULT_PARAMS = the frozen point).
* `dev_results/composite_dual_engine.json` - final harness run at 3/60 with plateau. `..._grid.csv` - shipped 243-combo grid.
* `dev_results/composite_dual_engine_g1_grid.csv`, `_g2_grid.csv`, `_plateaugrid_g3.csv` - the search grids.
* `dev_results/composite_dual_engine_sweep_P1.csv`, `_sweep_Q2.csv` - one-parameter-at-a-time sweeps.
* `dev_results/composite_dual_engine_ablate_frozen.csv`, `_ablate_smoke.csv` - ablation tables.
* `dev_results/composite_dual_engine_pick1.csv`, `_pick2.csv`, `_pick3.csv` - candidate scoring incl. measured plateau.
* Scripts: `_ablate.py`, `_gridan.py`, `_plateaugrid.py`, `_pick.py`, `_sweep.py`, `_diag.py`, `_show2.py`.

