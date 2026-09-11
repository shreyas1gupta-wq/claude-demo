# sticky_tier — design note (lens 4, whipsaw minimiser)

Pass 2 of the Demeter dual-engine study. Development window only (data hard-truncated at 2012-06-30 by
`dev_harness.py`). Costs 3 bp per unit of leverage traded + 60 bp p.a. financing spread on the levered leg.
Written incrementally; the Mechanism section was written BEFORE the first harness run and is unchanged.

**One-line verdict.** The frozen rule passes all seven DEV gates (dev_1990 Sharpe 0.612, maxDD -14.3%, 0.44 changes
per year, plateau 90%, 5 tunables) and beats the in-lens bar volmanaged on Sharpe, drawdown and turnover — but it does
so as a 1x-or-cash regime filter (3x never held in 1990-2012, 2x on 6% of days, cash 67%), NOT as the "hold 2-3x in
calm bull years" model the lens hoped for. Every point that holds 2-3x in calm regimes fails the 1950-69 / 1970-89 era
drawdown gate, because the shocks that hurt a vol-regime tier come FROM calm (1962, 1987, 2011) and are taken at the
full held tier. That negative result is the main deliverable of this lens.

## Mechanism (written before any run)

The disease in both Demeter's record and the incumbent is whipsaw at leverage: 8 of Demeter's 12 worst months are
calm months (VIX 13-19) in which a quick-exit/quick-re-entry rule sold a dip at 3x and re-bought the recovery. The
incumbent trades 7 times a year and still only matches buy-and-hold on a risk-adjusted basis. This lens asks: what
is the LEAST-trading rule that still de-levers in genuine stress?

Why a vol regime should carry the leverage decision at all: realised equity volatility is strongly autocorrelated
(clusters) and the conditional mean excess return is roughly flat in the vol level, so the ratio mean/variance is
highest in calm regimes (Moreira-Muir 2017). A levered position sized to the regime therefore raises the Sharpe
ratio and, mechanically, holds little exposure through the long high-variance drawdowns (1973-74, 2000-02, 2007-09).
volmanaged (lens 3) exploits this with continuous inverse-variance scaling and is the in-lens bar: dev_1990 Sharpe
0.495, maxDD -19.8%, 1.8 changes/yr, average leverage 0.63, 0% cash.

Why DISCRETE and STICKY instead of continuous: every position change costs 3 bp per unit of leverage and, more
importantly, a change made on noise is reversed on noise. Three whipsaw controls, each with a distinct job:
1. Wide hysteresis: enter a tier only when vol is below its boundary, leave it only when vol is a fraction h ABOVE
   that boundary. Small vol wiggles inside the band change nothing.
2. Persistence: raise leverage only after the calmer regime has shown itself for P consecutive sessions; one quiet
   day after a shock is not evidence. De-levering is NOT delayed by persistence (structural): the evidence for a
   down move is already the hysteresis margin, and with the leverage effect (vol rises after the first down move)
   every session of delay at 3x in a real shock is expensive. The cost of the asymmetry is quantified in DEV.
3. Minimum hold / cooling-off: after any change, leverage may not be RAISED again for M sessions, and re-levering
   happens only on the first session of an ISO week (a weekly decision cadence). This kills the exit-dip /
   re-enter-recovery / exit-again loop.

What this buys and what it costs, stated in advance:
* Buys: in calm bull years (1990s, 2003-07) the rule should sit at 2-3x for months without trading, so average
  leverage should be well above volmanaged's 0.63 and CAGR should approach or beat SPY's 8.3% (dev_1990).
* Costs: (i) 1987 — a discrete tier de-levers late and coarsely; whatever tier is held at the 19-Oct close is taken
  in full; (ii) 2008 — the exit happens when the EWMA crosses the hysteresis band, which is after the first shock
  days; (iii) 2009 — the recovery starts while vol is still high, so the first leg is taken at cash/1x (all DEV
  models so far share this).
* A cash (0x) tier vs a 1x floor is a DEV question: a 1x floor keeps up-capture but takes the 2000-02 grind at
  1x (-47% SPX peak-to-trough) — predicted to breach the -30% drawdown gate; a cash tier avoids it. Both are run.

Predicted DEV outcome before running: Sharpe roughly 0.45-0.55, 2-6 changes/yr, average leverage 1.0-1.5, maxDD
-20 to -30%; the 1970-1989 era (1987) is the era most likely to fail the -40% gate.

*Post-run comparison with the prediction:* Sharpe higher than predicted (0.61), trades far fewer (0.44/yr), average
leverage far LOWER than predicted (0.39, not 1.0-1.5), drawdown smaller (-14%). The "buys" line did not materialise:
calm-year exposure is below volmanaged's, not above it. The era most at risk was 1950-69 (1962), not 1970-89.

## Rules (identical to the `signals/sticky_tier.py` docstring)

Decided at the close of day t from data up to that close; the engine applies the level to day t+1.
1. VOL REGIME. sigma_t = max( EWMA-vol(halflife hl), EWMA-vol(halflife hl*long_mult) ) of daily S&P 500 price
   returns, annualised (features.ewma_vol, 20-session warm-up; pre-warm-up = cash). The slow leg is the regime
   memory. Trailing only. No VIX, so the rule runs from 1950 (the data actually start in 1885).
2. TIER BOUNDARIES (Moreira-Muir inverse-variance shape, one scale parameter). Tier k is warranted when
   (target_vol/sigma)^2 >= k, i.e. v_k = target_vol/sqrt(k): v1 = 14.0%, v2 = 9.9%, v3 = 8.1% at the frozen point.
   Raw tier T(sigma) = number of boundaries sigma is below (3x below v3 … cash at or above v1) — the continuous
   volmanaged target rounded DOWN to an integer.
3. HYSTERESIS. UP when T(sigma) > held level c. DOWN when T_h(sigma) < c, T_h using every boundary inflated by
   (1+h) (1x is left at 16.8%). A down move goes straight to T_h(sigma); an up move goes to T(sigma).
4. PERSISTENCE (up only). The UP condition must hold for P consecutive sessions. Down moves act at once (P_DN = 1).
5. COOLING-OFF + WEEKLY CADENCE (up only). At least M_COOL = 10 sessions since the last change AND the first
   trading session of an ISO week (causal: this row's ISO week differs from the previous row's). Down moves are
   never blocked.
6. Long or cash only; leverage in {0,1,2,3}; FLOOR = 0.

## Parameters and how each was chosen

Window: 1990-01..2012-06 for selection, 1950-2012 as the ruin cross-check (eras). Five grids, 727 combinations.

| param | frozen | grid range(s) | why this point |
|---|---|---|---|
| target_vol | 0.14 | B: 0.12-0.20; C1: 0.12-0.15 | marginal Sharpe 0.46/0.52/0.54/0.50 at 0.12/0.13/0.14/0.15; every point at 0.16+ fails G4 (1950-69 DD -44 to -55%, 1970-89 -42 to -67%). 0.14 is the centre of the feasible band. ±15%/±30% perturbations: 0.36/0.37 (down, fail tol.) and 0.46/0.48 (up, pass) — the cliff is on the LOW side (0.119 → 85% cash). |
| h | 0.20 | A: 0.15-0.60; B: 0.15-0.50; C1: 0.20-0.40 | Sharpe flat 0.57-0.61 across 0.15-0.50 at frozen hl/long_mult; 0.20 has the largest era-DD margin (-33.9% vs -38.9% at 0.30 and -40.0% at 0.40 — the 1962 exit timing). Perturbations 0.53-0.57, all pass. |
| hl | 20 | A: 5-20; B: 8-20; C1: 16-26 | marginal Sharpe 0.39 (8) → 0.42 (13) → 0.53 (20) → 0.53 (26); flat from 20. Perturbations 0.53/0.51/0.60/0.62, all pass. |
| long_mult | 8 | B: 1-8; C1: 4-12 | marginal 0.39 (1), 0.45 (4), 0.52 (6), 0.53 (8), 0.52 (12); centre of the 6-12 plateau. Perturbations 0.59/0.55/0.60/0.67, all pass. |
| P | 5 | C2: 1-10 | P=1 re-enters 2x one week early in 1962 and fails G4 (-40.5%); P=3 and 5 identical; P=10 costs 0.04 Sharpe. Perturbations round to 4 and 6: 0.589/0.604, pass (only two distinct values). |

Structural decisions made on the grids (not tunables):
* **FLOOR = 0.** Grid A: 192 of 192 floor-1 combos fail G3 (best maxDD -53.6%); at the frozen point a 1x floor gives
  Sharpe 0.43, maxDD -50.8%, CAGR 9.2% (diag3). The cash tier's entire value is 2000-02 and 2007-09. A 1x floor
  gives the higher CAGR and a Sharpe that only matches the incumbent — it fails G3 and is rejected.
* **M_COOL = 10 (demoted from tunable).** Grid C2: identical results for M ∈ {0, 5, 10, 21} (the slow leg keeps
  sigma above the re-entry boundary for months after any exit, so the cooling-off never binds). A dead tunable would
  only inflate the plateau share, so it is a constant safety rail. Budget: 5 tunables.
* **Ladder shape = inverse-variance, round-down.** Grid A's free geometric ladder (v_lo, gap; 384 combos, plain
  EWMA) found NO gate-feasible point: best maxDD -22.8% at Sharpe 0.32, best Sharpe 0.49 at maxDD -68%. The reason
  (diag1): a ladder holding 1-2x at 15-25% vol takes 2000-02 at 1-2x and re-levers on every lull. The MM shape
  puts 1x at 14% and 2x at 9.9%, i.e. the exposure volmanaged holds at the same vol level.
* **P_DN = 1, WEEKLY_UP = True** as designed; the "unsticky" comparison (h=0, P=1, M=0, daily) is in the
  stickiness table below.

## Grid summary

| grid | combos | what varied | gate-feasible (G2-G5 proxies) | best dev_1990 Sharpe | note |
|---|---|---|---|---|---|
| A | 384 | v_lo, gap, h, hl, floor (old geometric ladder, plain EWMA) | 0 | 0.489 (maxDD -68%) | structure abandoned |
| B | 135 | target_vol, h, hl, long_mult | 15 | 0.608 (fails G4 at -44.7%) | slow leg + MM ladder |
| C1 | 144 | target_vol 0.12-0.15, h, hl 16-26, long_mult 4-12 | 80 | 0.681 (era DD -39.99, cliff) | frozen point 0.612 chosen inside |
| C2 | 64 | M, P, long_mult {1,12} at target 0.14 | 28 | 0.678 | M dead, P weak |
| final | — | frozen point with plateau | ALL PASS | 0.612 | `dev_results/sticky_tier.json`; `sticky_tier_grid.csv` = C1 |

Plateau (harness, dev_1990): 18 of 20 single-parameter perturbations within 25% of base Sharpe 0.612 (90%); the two
failures are target_vol -15%/-30% (0.364/0.367: the rule goes to ~85% cash). dev_1950 plateau also 90%.
Cliffs: (i) target_vol ≥ 0.16 → G4 fails via 1962/1973-74; (ii) target_vol ≤ 0.12 → Sharpe falls toward 0.36 as the
rule stops investing; (iii) h = 0.40 or P = 1 → 1950-69 DD sits at -40.0/-40.5% (the 1962 2x-exit timing);
(iv) long_mult = 12 with hl = 26 → 0.49 (over-sticky, 75% cash). The frozen point is interior to all four.
Cost sensitivity: dev_1990 Sharpe 0.607 at 6 bp/90 bp, 0.614 at 2 bp/40 bp — costs are irrelevant at 0.44 changes/yr
(cost drag 0.013%/yr).

## Gate results (`python gate_check.py dev_results/sticky_tier.json`)

```
sticky_tier: ALL GATES PASS
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.6115542727934902 (bar 0.425)
  G3_dev1990_maxdd: pass  value=-14.252593625791265 (bar -30.0)
  G4_no_ruinous_era: pass
      1950-1969: ok: CAGR 10.00% maxDD -33.9%
      1970-1989: ok: CAGR 8.44% maxDD -17.3%
      1990-1999: ok: CAGR 12.70% maxDD -14.3%
      2000-2012H1: ok: CAGR 3.30% maxDD -4.5%
  G5_changes_per_year: pass  value=0.44428772919605075 (bar 25.0)
  G6_plateau: pass  value=0.9 (bar 0.5)
  G7_param_budget: pass  value=5 (bar 6)
```

Headline DEV numbers (3 bp / 60 bp, from `dev_results/sticky_tier.json`):

| window | CAGR | CAGR with T-bill zeroed on cash days | Sharpe | maxDD (monthly) | worst month | cash | avg lev | avg lev invested | chg/yr | up-capture | down-capture |
|---|---|---|---|---|---|---|---|---|---|---|---|
| dev_1990 | 7.38% | 5.31% | 0.612 | -14.3% | -8.7% | 66.7% | 0.39 | 1.18 | 0.44 (10 changes in 22.5 y) | 36% | 12% |
| dev_1950 | 8.55% | 6.30% | 0.348 | -48.2% | -16.9% | 44.0% | 0.74 | 1.32 | 0.98 | 67% | 60% |
| SPY 1x dev_1990 | 8.34% | — | 0.385 | -50.8% | -16.5% | 0 | 1.00 | 1.00 | 0 | 100% | 100% |

Leverage distribution dev_1990: cash 66.7%, 1x 27.5%, 2x 5.9%, 3x 0.0%. By decade: 1990s cash 50% / 1x 37% / 2x 13%
(avg 0.63); 2000s cash 75% / 1x 25% (avg 0.25); 2010-12H1 cash 100%. 3x was held only in 1964-66 (13% of the 1960s).

## In-lens comparison: sticky tier vs volmanaged (continuous scaling) vs SPY — dev window, 3/60

Recomputed with `engine.run` at 3/60 (volmanaged row matches `dev_results/volmanaged.json`).

| | Sharpe | CAGR | CAGR, T-bill zeroed | maxDD | chg/yr | avg lev | up-cap | down-cap | 1990-99 CAGR / avg lev / Sharpe | 2003-07 CAGR / avg lev / Sharpe |
|---|---|---|---|---|---|---|---|---|---|---|
| sticky_tier (frozen) | **0.61** | 7.38% | 5.31% | **-14.3%** | **0.44** | 0.39 | 36% | 12% | 12.7% / 0.63 / 0.84 | 5.8% / 0.50 / 0.54 |
| volmanaged | 0.49 | 7.39% | 7.39% | -19.8% | 1.78 | 0.63 | 55% | 40% | 13.6% / 0.85 / 0.81 | 6.6% / 0.83 / 0.49 |
| SPY 1x | 0.39 | 8.34% | 8.33% | -50.8% | 0 | 1.00 | 100% | 100% | 18.0% / 1.00 / 0.95 | 12.6% / 1.00 / 1.07 |

Verdict against the in-lens bar: the discrete sticky tier BEATS volmanaged's Sharpe (0.61 vs 0.49) with a smaller
drawdown and a quarter of the trades, so the bar is cleared — but it does NOT buy higher exposure in calm years. In
1990-99 it held 0.63x on average vs volmanaged's 0.85x and earned 12.7% vs 13.6% (SPY 18.0%); in 2003-07 0.50x vs
0.83x, 5.8% vs 6.6% (SPY 12.6%). Its Sharpe edge comes from being flat through 1997-2005 and 2007-2012, and 2.1 of its
7.4 CAGR points are T-bill interest on cash days (Demeter books cash at 0%: on that accounting the model's CAGR is
5.3%, below volmanaged's 7.4% and SPY's 8.3%).

**The higher-exposure point the lens hoped for, and why it is not frozen** (target_vol 0.18, h 0.15, hl 20,
long_mult 8; diag2 point C): dev_1990 CAGR 9.9% (> SPY 8.3%), Sharpe 0.53, maxDD -23.8%, avg lev 0.86, cash 49%,
1.4 changes/yr, 3x on 9% of days; calm 1991-99 CAGR 20.7% at 1.45x (SPY 20.6%), 2003-07 9.7% at 1.22x. It passes
G2, G3 and G5 but FAILS G4: 1950-69 maxDD -48.7% (Dec-1961..Jun-1962 taken at 2-3x from a sub-8% vol regime; the
window return is -39%) and 1970-89 maxDD -42.2% (1973-74 at 1-2x, -39% DD; 1987 window -30%). Every grid point that
holds 2-3x in calm regimes shares this fate: **the shocks that hurt a vol-regime tier come from calm**, so the tier
that is highest exactly when the regime is calmest is the tier that is fully exposed on the first shock days. The
leverage effect (vol rises after the price falls) makes this structural, not a tuning problem: shortening hl to 8
did not reduce drawdowns (grid B marginal DD -24.6% at hl 8 vs -24.2% at hl 20), it only added whipsaw.

## Stickiness: what it costs (1987, 2008) and what it buys (1990-99, 2003-07)

Variants at the frozen point (diag3; "unsticky" = same vol estimator with h=0, P=1, M=0, daily re-levering;
"no memory" = long_mult 1, i.e. plain EWMA(20) with the sticky controls kept):

| window | frozen | unsticky | no memory | volmanaged | SPY |
|---|---|---|---|---|---|
| dev_1990 Sharpe / maxDD / chg/yr / avg lev | 0.61 / -14.3 / 0.44 / 0.39 | 0.52 / -13.7 / 2.22 / 0.36 | 0.39 / -18.6 / 1.95 / 0.76 | 0.49 / -19.8 / 1.78 / 0.63 | 0.39 / -50.8 / 0 / 1.0 |
| 1990-99 CAGR / Sharpe / chg/yr | 12.7% / 0.84 / 0.8 | 11.1% / 0.71 / 3.8 | 13.7% / 0.64 / 2.4 | 13.6% / 0.81 / 2.7 | 18.0% / 0.95 |
| 2003-07 CAGR / Sharpe / chg/yr | 5.8% / 0.54 / 0.4 | 5.4% / 0.46 / 2.4 | 6.6% / 0.37 / 2.6 | 6.6% / 0.49 / 2.4 | 12.6% / 1.07 |
| 1987 Aug25-Dec31 total / position on 19-Oct | +2.2% / cash | +2.2% / cash | -5.6% / 0 on 19-Oct (77% cash) | -25.4% / 0.39x | -49.8% ann. (-25.0% total) |
| 2008 Sep1-Mar09 total / position on 29-Sep, 15-Oct | +0.4% / cash | +0.4% / cash | +0.4% / cash | -21.8% / 0.20x | -65.6% ann. (-40.8% DD) |
| 2009 Mar10-Dec31 total | +0.1% | +0.1% | +0.1% | +13.9% | +85.6% ann. (+67% total) |

* **Cost of stickiness in 1987 and 2008: nil in the crash weeks themselves** — the frozen rule was already in cash for
  regime reasons (exit 1x→0 on 1987-04-13 at sigma 17.4% after the 1986-87 vol pickup; exit on 2007-08-06 at 17.3%
  in the quant-quake week), and the unsticky variant held the same position on 16/19/26-Oct-1987 and on
  15/29-Sep and 15-Oct-2008. The late-de-levering cost the lens anticipated did not arise because the rule had left
  1x six months (1987) and two months (2008) before the crash. The cost of stickiness shows up instead as **late
  RE-levering**: cash from 1987-04-13 to 1992-03-30 (five years, SPX +~70%), from 1997-03-31 to 2005-02-07 (eight
  years, through the 1997-2000 run-up as well as the 2000-02 bear) and from 2007-08-06 to the end of DEV (the whole
  2009-2012 recovery, SPX +67% in Mar-Dec 2009 alone). The 160-session slow leg is what keeps the rule out.
* **What it buys in the 1990-99 and 2003-07 chop:** relative to the unsticky variant with the same estimator, the
  hysteresis + persistence + weekly cadence add +0.13 and +0.08 Sharpe, +1.6 and +0.4 CAGR points, and cut the trade
  count from 3.8 to 0.8 and 2.4 to 0.4 per year (dev_1990 overall: +0.09 Sharpe, 5x fewer trades). Relative to "no
  memory" (plain EWMA), the slow leg adds +0.22 Sharpe and removes 5 DD points on dev_1990, but it is also what
  halves the average leverage (0.76 → 0.39) and the up-capture (60% → 36%).
* The 1962 episode is where stickiness genuinely hurt: 2x from 1961-01-23 (sigma 9.8%), 2→1 on 1962-05-15 (12.5%),
  1→0 only on the 28-May -6.7% day (22.8%); window Dec-61..Dec-62 -29% vs SPX -8%. This single path sets the
  1950-69 era drawdown (-33.9%) and is the G4 cliff that h = 0.40 and P = 1 fall off.

## Stress narrative

Position path (all changes 1950-2012H1 are listed in `dev_results/sticky_tier_diag3.txt`; 61 changes in 62.5 years):
* **1987.** 1x from 1986-11-17; exit to cash 1987-04-13 (sigma 17.4%, a -2.4% day). Cash through the crash: window
  +2.2% (T-bills) vs SPX -25.0%. No re-entry until 1992-03-30. Verdict: protected by absence, then absent for five
  years of bull market.
* **1998 LTCM.** In cash since 1997-03-31 (sigma 17.0% on a -2.1% day). Window +2.1% vs SPX +4.9%.
* **2000-02 bear.** In cash for the entire episode (+9.7% T-bills vs SPX -47.2%); no re-entry attempts (the slow leg
  never fell below 14% until Feb-2005). Verdict: the whole G3 pass is this and 2007-09.
* **2002-03 recovery.** Missed entirely (+1.3% vs +45.5%); re-entry to 1x only on 2005-02-07 (sigma 13.9%).
* **2007-09 GFC.** 1x from 2005-02-07; exit to cash 2007-08-06 (sigma 17.3%, two months before the Oct-2007 top).
  Cash through the whole crisis: +2.2% vs SPX -54.8%. Position on 15-Sep, 29-Sep and 15-Oct-2008: cash.
* **2009 recovery.** Missed entirely (+0.1% vs +67.4%): with a 160-session slow halflife sigma stayed above 14% for
  the rest of DEV. The rule was in cash every day from 2007-08-06 to 2012-06-29.
* **2010 flash crash / 2011 debt ceiling.** Cash (0.0% / 0.0% vs SPX -8.4% / -5.6%). Not protection — absence.
* **Calm years.** 1x 1992-93; 2x 1993-12..1994-04, 1994-09..1994-11, 1995-04..1996-02 (each 2→1 exit on a
  12-13% sigma print); 1x 1996-02..1997-03; 1x 2005-02..2007-08. Never 3x after 1966.

## Spurious re-entry census

2000-02 bear: 0 entries to ≥2x (0% of days at ≥2x). 2007-09 GFC: 0 entries to ≥2x. This is trivially clean: the
rule never rose above cash inside either bear, so the census — which counts entries to ≥2x — cannot fire. The
equivalent honest statistic is the number of re-entries to 1x inside the two bears: zero as well (the slow leg
stayed above 14% throughout both).

## Event ladders (target leverage decided at each close)

* 2008-10-10 (Lehman capitulation): L0 on every day 10-07..10-20 (SPX -4.5, -2.5, -7.0, -2.4, +14.5, -1.5, -9.8,
  +4.2, -0.6, +6.0%). In cash since 2007-08-06.
* 2008-11-20 (Nov-08 low): L0 throughout 11-17..12-01 (SPX -6.4, -7.4, +5.4, +6.9 … -8.9%).
* 2009-03-09 (GFC low): L0 throughout 03-04..03-17 (SPX -4.1 … +6.0, +3.9, +3.1%). The exit fired 19 months before
  the low and the re-entry never fired in DEV — the opposite of the "re-enter near the low" the record shows.
* 2002-10-09 (bear low): L0 throughout 10-04..10-17 (SPX -2.8, +3.2, +4.4, +4.8%). Re-entry 28 months later.
* 1987-10-19 (for completeness): L0 throughout 10-14..10-27.

## Iteration count

13 distinct DEV evaluations: 5 grids (A 384 + B 135 + C1 144 + C2 64 = 727 combinations, each grid counted once)
+ 8 single runs (smoke test with the provisional defaults; 4 diag2 candidate re-runs A-D — all already in grid B;
the final harness run; and the 3 diag3 variants unsticky / no-memory / 1x-floor). Total parameter sets touched: 735.
No out-of-sample data, `evaluate.py` or Demeter monthly returns were used at any point; nothing was written to
`results/`.

## Honest weaknesses and the regime that would break it

1. **It is a regime filter, not a levered strategy.** 3x is never held in 1990-2012, 2x on 6% of days, cash 67%;
   average leverage 0.39; up-capture 36% (the record's target is ≥100%). The lens set out to hold 2-3x in calm
   years and trade least; it delivered "trade least" (10 decisions in 22.5 years) by being out of the market for
   13 of them.
2. **The DEV Sharpe rests on three invested spells** (1992-97, 2005-07 and the 1993-96 2x episodes) and two long
   cash spells that happened to contain both bears. Ten position changes is not a sample; the 0.61 should be read
   as "avoided 2000-02 and 2007-09", not as a repeatable timing edge.
3. **Over 1950-2012 it is worse than buy-and-hold on Sharpe** (0.35 vs 0.47): 1950-69 at 1.35x average took 1962
   at 2x (-33.9% DD vs SPX -22%); 1970-89 earned 8.4% vs 11.5% while 51% in cash. The G4 gate is passed, the
   long-window risk-adjusted case is not made.
4. **T-bill dependence.** 2.1 of 7.4 CAGR points in dev_1990 are cash interest. In a zero-rate world (2009-15) or on
   Demeter's 0%-cash accounting the model's return falls to ~5%, below SPY and volmanaged.
5. **Late re-levering is the true cost of the design:** the 160-session slow leg kept the rule out for the entire
   1988-91, 1997-2000 and 2009-2012 rallies. Any recovery that starts while trailing vol is still high is missed in
   full — the inference note (§7) says the record's rebound months carry the HIGHEST leverage, i.e. this rule does
   the opposite of what the record shows in Mar/Apr-2020 or the 2022 rallies (a known, pre-declared failure mode of
   vol-LEVEL gating, which the record rules out).
6. **Regimes that break it:** (a) a high-vol bull market (1982-87, 2009-12 style) — sits in cash while the index
   rallies; (b) a crash from a sub-14%-vol regime while at 1-2x (1962, or a Feb-2018/Aug-2011-type air pocket
   arriving at 2x) — taken at the full tier for 1-3 sessions until the fast EWMA crosses the exit boundary; (c) a
   world where vol and forward returns are positively related (levered melt-up on rising vol) — the mechanism
   inverts; (d) the exit-boundary neighbourhood: sigma oscillating around 14-17% (1994, 2007) produces the few
   changes the rule does make, each one a small loss.
7. **What would fix the lens** (not done here — out of budget and outside a pure vol regime): a crash exit that is
   price-based (consecutive-sigma days) rather than vol-based, so 2-3x can be held in calm regimes and cut within
   1-2 sessions of a shock, and a dissipation-based re-entry — i.e. lenses 1, 2 and 6. Grid B shows the price the
   pure vol regime pays for lacking them: CAGR 9.9% at target 0.18 is available only with -48% era drawdowns.

## Bugs found in shared code

None. Two observations (not bugs): (i) `dev_harness.plateau` perturbs integer parameters by ±15%/±30% and rounds,
so for P = 5 the four perturbations are only two distinct values (4 and 6) — the plateau count for small integers
is slightly optimistic by construction; (ii) `spurious_reentry_census` counts entries to ≥2x only, so a rule whose
ceiling inside a bear is 1x or cash passes it vacuously — for such rules the number of re-entries to 1x is the
informative statistic (reported above: zero).

## Files

`signals/sticky_tier.py` (signal), `dev_results/sticky_tier.json` (final harness run with plateau),
`dev_results/sticky_tier_grid.csv` (= grid C1, the grid the frozen point was chosen from), `dev_results/sticky_tier_gates.txt`,
grids A/B/C1/C2 (`sticky_tier_grid{,B,C1,C2}_spec.json`, `sticky_tier_grid{A,B,C1,C2}_grid.csv`, `_gridX.json`, `.log`),
diagnostics `sticky_tier_diag{1,2,3}.py`, `sticky_tier_diag{2,3}.txt`, `sticky_tier_gridsum.py`, `sticky_tier_extract.py`,
`sticky_tier_smoke.json` (provisional defaults, superseded), `sticky_tier_refsummary.py` (earlier attempt's reference
script, unused).
