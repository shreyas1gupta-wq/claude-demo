# volmanaged — design note (lens 3: volatility-managed leverage, Moreira & Muir 2017)

Signal file: `signals/volmanaged.py`. Designer: candidate 3, pass 2. DEV only (data hard-truncated 2012-06-30 by
`dev_harness.py`; `evaluate.py` never run; `results/` never written). Costs quoted at 3 bp / 60 bp unless stated.

## 1. Mechanism (written before any run)

**Claim.** Realised equity volatility is strongly predictable at horizons of days to a month (daily variance
autocorrelation is high; a short EWMA of squared returns forecasts next-month variance with R² ≈ 0.5), while the
conditional *mean* excess return barely moves with volatility at those horizons (the short-horizon risk–return
trade-off is flat or weakly negative). If the mean is roughly constant and variance is forecastable, the
Sharpe-maximising rule for a single risky asset is exposure proportional to `mu / sigma_t^2`, i.e. inversely
proportional to *forecast variance*. Moreira & Muir (2017) implement exactly `w_t = c / RV_t^2` on the market
factor with a monthly rebalance and report a Sharpe increase of roughly 0.1–0.2 (annualised) over buy-and-hold,
with the gain concentrated in the fact that the managed portfolio takes *less* risk in high-variance months
(which historically did not pay proportionally more) and *more* risk in calm months. Because equity volatility
is mean-reverting and the highest-variance months contain the largest drawdowns, the same rule mechanically
cuts crash exposure.

**Why it should have worked in 1950–2012 and 1990–2012 specifically.** The three equity disasters in the
development window (1987, 2000–02, 2007–09) were all preceded by rising realised variance *before* the worst
weeks: in 1987 vol rose through 14–16 Oct; in 2000–02 the bear was a grinding high-vol regime for 2.5 years; in
2008 vol was elevated from Jan-2008 and exploded in Sep–Oct. A variance-inverse rule is therefore
under-invested in every long high-vol drawdown and over-invested (up to 3x) in the calm bull markets of the
1950s–60s, 1990s and 2003–06. The 1950–1989 era has no VIX, so this lens is one of the few that can be tested
across all four eras, and the mechanism (variance persistence) is not sample-specific.

**Where the mechanism is known to be weak (stated up front).**
1. *Leverage effect / late de-levering.* Volatility rises *after* the first down move; a trailing estimator
   therefore de-levers one to several days late. The first shock day is taken at the pre-shock leverage. For a
   single-day disaster (19-Oct-1987, −20%) a variance rule cannot avoid the day itself; it can only be less than
   3x going in (vol had already risen the prior week) and near zero afterwards. This must be quantified in 1987
   and Oct-2008, not assumed away.
2. *Late re-entry.* Vol stays high for months after a low (Apr–Jun 2009 RV 25–40%), so the rule is lightly
   invested through the first, sharpest leg of recoveries. It will miss most of the 2009 rebound, like every
   rule so far in this repo. The record's Apr-2020 (3x with VIX 31–57) is *not* something this lens can
   reproduce; it is the opposite of its mechanism. I am not attempting to reproduce Demeter.
3. *Turnover.* The raw rule changes exposure every day. Costs at 3 bp per unit of leverage traded make the
   daily version uneconomic; the no-trade band (and/or a coarser decision cadence) is the whole engineering
   question. The literature's monthly rebalance is too slow for the crash exit; a band on a daily target is the
   compromise: exposure moves only when the variance forecast has changed enough to matter.
4. *Chop.* Calm months with a few −1…−2% days will see leverage cut from 3x to ~1–2x and restored, paying costs
   for nothing. Cederburg, O'Doherty, Wang & Yan (2020) show the MM gain is fragile for most factors; for the
   market factor it survives but is modest. I expect the DEV Sharpe to sit near the G2 bar, not far above it.

**Pre-run predictions (falsifiable).**
- dev_1990 Sharpe at 3/60 in the 0.40–0.55 range; dev_1950 Sharpe above buy-and-hold (0.47) by 0.05–0.15.
- Drawdown materially better than buy-and-hold (−50.8%) and inside the −30% gate, driven by 2000–02 and 2008.
- 2009 recovery capture well below SPY's +67%.
- 1987: leverage in effect on 19-Oct between 0.5x and 1.5x (vol already up), month loss of order −10…−25%.
- Trade count is a monotone decreasing function of the band; band ≈ 0.5 lands near 10–20 changes/yr.
- Discretising to {0,1,2,3} costs at most a few hundredths of Sharpe (the rounding is a second band).
- `sigma^2` (MM's form) vs `sigma` (milder): sigma^2 should give the larger Sharpe gain but more turnover and
  more time clipped at 3x or at ~0; I will pick whichever is on the flatter plateau after costs.

**Ingredients deliberately NOT used.** No VIX (so the rule runs from 1950), no trend filter (ruled out by the
record and orthogonal to the mechanism), no mean-reversion re-entry, no price level. Minimal gating, as the
lens prescribes: the only non-MM ingredient is the optional shock override (cash for N sessions after a
> z-sigma down day), which is a faster version of the same variance update, and I will drop it if it does not
earn its two parameters.

## 1b. DEV log of structural decisions (banked as they were made; every variant is in `volmanaged_scratch_log.csv`)

**Batch 1 (23 variants, hl=10, 3/60 costs unless stated).** Pure Moreira-Muir daily rule (band 0, ~200-250
changes/yr): dev_1990 Sharpe 0.365 net / 0.418 gross at target_vol 0.15 (buy-and-hold 0.385), maxDD -38%;
dev_1950 DD -61%. So the literature's gain over buy-and-hold is about +0.03 gross on this window at a 3x cap, and
costs at 3 bp eat more than that. Band 0.5 cuts changes to ~10/yr and keeps most of the gross Sharpe.
- POWER 1 (inverse vol) vs 2 (inverse variance): p=1 reaches Sharpe 0.429 at tv 0.20 but DD -51%; p=2 at the same
  Sharpe has DD 10-15 points better because it cuts harder in high vol. **POWER = 2 fixed.**
- Discrete {0,1,2,3} vs continuous: discretising cost 0.03-0.05 Sharpe and DOUBLED the trade count (10 -> 19/yr)
  because integer jumps chatter at the rounding boundaries. **Continuous fixed** (the discretisation cost is
  therefore "yes, about 0.05 Sharpe and 2x turnover", answering the brief's question).
- Weekly band check: no better than daily at equal trade count (0.297-0.404 vs 0.354-0.412). **Daily fixed.**
- Shock override (cash 3 sessions after a -3 sigma day): -0.09 Sharpe at every target vol (0.354 -> 0.263). The
  -3 sigma days in 1990-2012 are followed by reversals more often than continuation. **Dropped; two parameters
  freed.**

**Diagnostic on the batch-1 baseline (tv 0.15, hl 10, band 0.5).** The drawdowns are NOT mainly "3x hit by the
first shock" -- they are the grinding moderate-vol bears taken at 0.5-1.5x the whole way down: 1999-07..2002-07
-40.4% (avgL 0.57 through the bear, still -35%), 2007-06..2009-03 -31.5%, and in the long sample 1968-11..1970-05
-61%, 1961-12..1962-10 -47%, 1966 -42% (1960s median vol 9% => 3x pinned, bears arrived at 12-20% vol => 1-1.5x
all the way down). Inverse variance has no directional input; that is the lens's structural weakness.
Leverage effect quantified: 1987 -- the rule was 0.60x from 1-Oct (vol 16-19%) and the target fell to 0.27 by 16-Oct
but the 0.5 band did not act, so 19-Oct was taken at 0.60x (-12.3% on the day), then 0.03x for the rest of October
(missed the +5.3/+9.1% rebound days too). Oct-2008 -- 0.84x into 15-Sep (-4.0% on the day), 0.26x from 16-Sep to
mid-Oct (the -7.8/-9.8% days cost -2.0/-2.6% each); the crash core was taken at about a quarter of market exposure.

**Batch 2 (22 variants).** Estimator variants at band 0.5, p=2: plain EWMA hl 5 / 10 / 20 -> Sharpe 0.411 / 0.354
/ 0.449 with DD -42 / -36 / -30 (slower = fewer whipsaws in the 1990s). Downside semi-vol: 0.22-0.32, DD -44..-66
(big UP days do not raise semi-vol, so it re-levers into choppy bears) -- rejected. **Two-horizon max(EWMA(hl),
EWMA(4hl))**: Sharpe 0.449 at tv 0.15 with DD -21.4% and 4.2 changes/yr; with an asymmetric band (down band
0.3x the up band) 0.455 / -19.4% / 8.1 chg/yr. Asymmetric band on plain EWMA also helps (0.354 -> 0.411-0.441,
DD -36 -> -27). The two-horizon forecast is the standard "fast up, slow down" vol-targeting estimator and stays
inside the lens (leverage is still a continuous inverse function of trailing realised variance).
**Structure fixed for the grid: EST = max2, POWER = 2, continuous, daily, no shock; tunables target_vol, hl,
long_mult, band_up, band_dn (5).**

**Batch 3 (16 variants, 5-tunable structure) + harness smoke test (1).** Harness reproduces the scratch numbers
(tv 0.15, hl 10, lm 4, band 0.5/0.3: Sharpe 0.47, DD -22.1%, 6.0 chg/yr, lookahead ok). Feasible region: target_vol
0.12-0.15 (0.165 breaks G4: 1970-89 era DD -42.8/-47.7%), hl 5-20 all fine on dev_1990 (0.46-0.48) but hl 20 puts
the 1970-89 era DD exactly at -40.0, long_mult 2-12 flat (0.448-0.460), band_up 0.75 best (0.485) with 0.35 worst
(0.397, more whipsaw), band_dn 0.15/0.3/0.5 flat (0.455/0.465/0.449). The tv axis is bumpy (0.12: 0.460, 0.135: 0.401,
0.15: 0.465, 0.165: 0.408) -- the dev_1990 Sharpe is driven by a handful of episodes, so I will pick the centre of
the widest region where every neighbour clears G2 AND every era DD clears -40% with margin, not the best cell.
Honest negative already visible: dev_1950 Sharpe 0.37-0.43 is BELOW buy-and-hold's 0.47 (the 1970-89 era runs at
~1x average with Sharpe 0.14 vs SPY's ~0.3); the rule beats buy-and-hold on Sharpe only on 1990-2012.
Coarse grid: 5 x 4 x 3 x 3 x 3 = 540 combos (`volmanaged_grid_spec.json`).

**Refinement grid (216 combos, `volmanaged_grid2_spec.json`).** Narrowed around the batch-3 region: target_vol
{0.13, 0.14} x hl {10, 13, 16, 20} x long_mult {5, 8, 12} x band_up {0.6, 0.75, 0.9} x band_dn {0.2, 0.3, 0.4}
= 2x4x3x3x3 = 216. Chosen point: target_vol=0.14, hl=13, long_mult=8, band_up=0.75, band_dn=0.30 (dev_1990 Sharpe
0.4946, DD -19.80%, 1.78 chg/yr, dev_1950 Sharpe 0.3616, DD -48.64% -- confirmed against `volmanaged_grid2_grid.csv`
row 148, exact match to the final harness JSON). This is the interior of the region that clears every gate with
margin (see Grid summary below), not the single best cell (best-cell hl=20 sits closer to the era-DD cliff --
see below).

*This finisher pass adds sections 2 onward below from the banked JSON, grids, iteration log and diagnostics; no
parameter was changed and no new harness run was made except `gate_check.py` (read-only) and `count_iterations.py`
(already-written, read-only).*

## 2. Rules

(Numbered as in `signals/volmanaged.py`'s module docstring; decided at the close of day t, engine applies at t+1.)

1. **Variance forecast.** `sigma_t = max(EWMA-vol(halflife=hl), EWMA-vol(halflife=hl*long_mult))` of daily S&P
   500 returns, annualised (`features.ewma_vol`, 20-session warm-up, trailing only). The max of a fast and a slow
   horizon makes the forecast rise as fast as the fast leg (quick de-lever after a shock) and fall only as fast as
   the slow leg (slow re-lever once a high-vol regime is established).
2. **Raw target.** `T_t = clip((target_vol / sigma_t) ** 2, 0, 3)` -- exposure inversely proportional to forecast
   *variance* (the Moreira-Muir form; POWER=1, inverse-vol, was tried and rejected in DEV -- see §1b batch 1).
3. **Asymmetric no-trade band.** Held level `H_t = H_{t-1}` unless `T_t - H_{t-1} > band_up` (target rose) or
   `H_{t-1} - T_t > band_dn` (target fell); then `H_t = T_t`. `band_dn < band_up` means the rule de-levers on a
   smaller move than it re-levers on (the leverage-effect asymmetry). The band is the sole turnover control.
4. Long-or-cash only, leverage continuous in [0, 3]. No VIX (runs from 1950), no trend filter, no price signal, no
   shock override (tested and rejected in DEV: forced cash after a -3-sigma day cost ~0.09 Sharpe because such days
   are followed by reversals more often than continuation in this window).

**Structural constants (not tunable, named in the docstring with reasons):** `MAX_LEV=3` (mandate cap);
`POWER=2` (Moreira-Muir inverse-variance form, chosen over POWER=1 in DEV); `DISCRETE=False` (rounding to
{0,1,2,3} cost ~0.05 Sharpe and doubled turnover in DEV); `WEEKLY=False` (a weekly band check was no better than
daily at equal trade count in DEV); `EST="max2"` (the two-horizon estimator; plain EWMA and downside semi-vol
were tried and rejected in DEV, §1b batch 2); `MIN_PERIODS=20` (EWMA warm-up sessions; pre-warm-up level = 0 =
cash); `SHOCK_Z=SHOCK_DAYS=0` (shock override held OFF for reproducibility of the DEV comparisons that rejected it).

## 3. Parameters and how each was chosen

All five tunables were chosen on **dev_1990** (1990-01-02..2012-06-29, 3bp/60bp), cross-checked against
**dev_1950** (1950-01-03..2012-06-29) and the four eras, per the docstring and §1b above. Grid ranges and the
region each value was drawn from:

| param | value | grid tested | why this point |
|---|---|---|---|
| `target_vol` | 0.14 | coarse 0.12-0.16 (step 0.01); refinement 0.13/0.14 | dev_1990 Sharpe is flat 0.35-0.63 across 0.12-0.15 (grid1 group means 0.445-0.448) and degrades sharply at 0.16 (era-DD failure rate jumps from ~42/108 to 73/108, see Grid summary); 0.14 sits at the centre of the surviving 0.12-0.15 band with margin on both sides. |
| `hl` | 13 | coarse 6/8/10/13; refinement 10/13/16/20 | dev_1990 Sharpe rises monotonically with hl (group means 0.428 at 6 -> 0.469 at 13 in grid1; 0.467 at 10 -> 0.511 at 20 in grid2) and the failure count falls the same way, but the docstring records hl=20 puts the 1970-89 era DD "exactly at -40.0" (the G4 boundary) on cross-check against dev_1950; 13 is the largest value in the interior of the plateau that keeps that era-DD margin, so the +-30% perturbation (9.1-16.9) stays inside the passing region (confirmed in `plateau_dev_1990`: hl perturbations score 0.446-0.566, all within tolerance). |
| `long_mult` | 8 | coarse 3/5/8; refinement 5/8/12 | dev_1990 Sharpe group means rise with long_mult (0.427 -> 0.462 in grid1, 0.466 -> 0.506 in grid2) and long_mult=3 is the worst cell in both grids (102/180 and 19/72 combos failing a listed gate); 8 is the flat, non-extreme choice inside 5-12 rather than the nominal best (12), leaving room on both perturbation directions. |
| `band_up` | 0.75 | coarse 0.5/0.75/1.0; refinement 0.6/0.75/0.9 | Sharpe is close to flat across the coarse grid (group means 0.442/0.450/0.444) with 0.75 the best of the three and the interior point of the refinement range; the design note (§1b batch 3) independently found 0.75 "best (0.485)" against 0.35 "worst (0.397, more whipsaw)" at the batch-3 stage. |
| `band_dn` | 0.30 | coarse 0.15/0.30/0.45; refinement 0.2/0.3/0.4 | Flat in both grids (group means 0.435/0.451/0.449 and 0.489/0.492/0.489); 0.30 is the interior, symmetric-feeling choice and (per §1b batch 2) the down-band that made the two-horizon estimator's asymmetric-band version outperform the symmetric one (0.30x the up-band, i.e. de-lever on a smaller move than re-lever). |

I cannot independently confirm, from the banked artifacts, a sharper reason for 8 vs 12 on `long_mult` or 0.75
vs the nominal-best band_up cell beyond "flat region, pick the interior, non-edge point for plateau margin" --
the scratch log states the region but not a cell-by-cell tie-break rationale, so I report the criterion actually
used (interior-of-plateau) rather than inventing a sharper one.

## 4. Grid summary

Two grids, 540 + 216 = **756 combos** (`volmanaged_grid.csv`, `volmanaged_grid2_grid.csv`; the harness JSON's own
`grid_n` field records 540 for the grid that shipped with the final run). Plateau share at the frozen point:
`plateau_dev_1990.share_within_25pct = 1.00` (20/20 single-parameter +-15%/+30% perturbations keep Sharpe within
25% of the 0.4946 base -- gate G6 needs >=50%, this clears it fully). `plateau_dev_1950` is also 1.00/20.

**Where the cliffs are** (computed from the two grid CSVs, gate thresholds G2/G3/G4/G5 applied per-row):

- Coarse grid1 (540 combos): 296 pass all four listed gates (54.8%). The clearest cliff is on `target_vol`:
  failure count is flat at 42-45/108 for 0.12-0.15 and jumps to 73/108 at 0.16 (era max-DD breaches -40% much more
  often). `hl` shows a gradient, not a cliff: 79/135 fail at hl=6 falling steadily to 37/135 at hl=13. `long_mult=3`
  is a soft cliff (102/180 fail vs 66/180 at long_mult=8). `band_up`/`band_dn` are flat across their grid1 range
  (68-90/180 failing regardless of value) -- these two are turnover/shape controls, not stability controls.
- Refinement grid2 (216 combos): 187 pass all four listed gates (86.6%) -- the refined region is much safer than
  the coarse grid on average. `hl=20` has the fewest failures (2/54) but the docstring/§1b flag it as touching the
  -40.0% era-DD boundary on a different cross-check (dev_1950, not the dev_1990-only gate table above), which is
  why 13 was kept over 20 despite the raw failure count favouring 20.

## 5. Gate results (`python gate_check.py dev_results/volmanaged.json`, verbatim, re-run by the finisher unchanged)

```
volmanaged: ALL GATES PASS
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.4945800022969806 (bar 0.425)
  G3_dev1990_maxdd: pass  value=-19.80145206761278 (bar -30.0)
  G4_no_ruinous_era: pass
      1950-1969: ok: CAGR 11.53% maxDD -34.5%
      1970-1989: ok: CAGR 8.40% maxDD -27.1%
      1990-1999: ok: CAGR 13.59% maxDD -15.2%
      2000-2012H1: ok: CAGR 2.67% maxDD -19.8%
  G5_changes_per_year: pass  value=1.777150916784203 (bar 25.0)
  G6_plateau: pass  value=1.0 (bar 0.5)
  G7_param_budget: pass  value=5 (bar 6)
```

## 6. Stress narrative

Overall dev_1990: avg_leverage = **0.63x**, avg_leverage_when_invested = 0.63x (identical -- because
`pct_days_cash = 0.0%`), position changes 1.78/yr (40 changes over 22.5 years). **This is a continuously
de-levered market exposure, not a market-timing in/out rule**: the model is long the S&P every single day of
dev_1990 and dev_1950, just scaled well below 1x on average (0.63x) and never at the 3x cap for long. Read every
episode below with that framing -- there is no "sat out the crash in cash" story here, only "carried less size."

- **1987 crash** (90-day stress window): model -11.5% vs SPY -25.0%, model max-DD -13.2% vs SPY -32.9%, avg
  leverage 0.19x, 1 band change, 0% days at 3x. Vol had already risen through 1-16 Oct, so the rule entered
  Black Monday at 0.39x (not the 3x cap) and still lost -7.97% same-day (see ladder in §8-adjacent detail);
  leverage then fell to 0.03x for the rest of the month and stayed there, missing the +5.3%/+9.1% rebound days.
- **1998 LTCM**: model +2.7% vs SPY +4.9%, DD -2.3% vs SPY -19.0%, avg leverage 0.14x, 0 changes -- the rule was
  already de-levered from the 1997-98 EM/Russia vol and simply held through LTCM without reacting.
- **2000-02 bear**: model -0.1% vs SPY -47.2%, DD -4.6% vs SPY -47.5%, avg leverage 0.1396x, **0 band changes in
  638 days** -- the rule locked onto its low band-floor level (see §10) at the start of the bear and never moved
  for its entire 2.5-year length. This protects capital but is a static exposure, not an active response.
- **2007-09 GFC**: model -19.8% vs SPY -54.8%, DD -20.2% vs SPY -55.2%, avg leverage 0.425x, 1 band change over
  356 days -- one step down (0.54x -> 0.20x, mid-September 2008) and then flat through the Oct/Nov acceleration
  and the Mar-2009 low (see §8).
- **2009 recovery**: model +11.4% vs SPY +67.4%, avg leverage 0.20x, 0 changes -- confirms the pre-run
  prediction; the rule captures 17% of the rebound because it is still pinned at the crisis-low band level the
  whole recovery.
- **2010 flash crash window**: model -1.6% vs SPY -8.4%, DD -3.2% vs SPY -15.7%, avg leverage 0.20x, 0 changes.
- **2011 debt-ceiling**: model -0.8% vs SPY -5.6%, DD -3.7% vs SPY -17.9%, avg leverage 0.20x, 0 changes.

## 7. Spurious re-entry census

`spurious_reentry_census` covers the two grinding bears the brief flags (2000-02, 2007-09): **0 entries to >=2x
leverage in either bear** (`pct_days_2x_plus = 0.0%` for both; `mean_fwd10_excess_pct` / `share_fwd10_negative`
are null because there were no qualifying entries to measure). This is a direct, mechanical consequence of the
rule rather than a tuned-in safety margin: realised variance stayed elevated throughout both bears (see the
2002-10-09 and event-ladder ranges below), so `T_t = (target_vol/sigma_t)^2` never approached 2x until volatility
had genuinely and durably fallen. The rule that killed `vix_dissipation` (spurious 2x+ re-entry on a volatility
head-fake) cannot occur in a pure inverse-variance rule with no dissipation trigger.

## 8. Event ladders (from `event_ladders` in the JSON; `lev_target` is the banded held level in effect, not the raw daily target)

**2002-10-09** ("bear low", held pinned at 0.1396x the whole window):
| date | spx ret% | VIX | held |
|---|---|---|---|
| 2002-10-04 | -1.83 | 39.5 | 0.140 |
| 2002-10-07 | -2.07 | 42.6 | 0.140 |
| 2002-10-08 | +1.57 | 41.0 | 0.140 |
| **2002-10-09** | **-2.82** | **42.1** | **0.140** |
| 2002-10-10 | +3.24 | 37.5 | 0.140 |
| 2002-10-11 | +4.38 | 35.7 | 0.140 |
| 2002-10-14 | +0.56 | 36.0 | 0.140 |
| 2002-10-15 | +4.81 | 34.0 | 0.140 |
| 2002-10-16 | -2.42 | 36.0 | 0.140 |
| 2002-10-17 | +1.99 | 34.1 | 0.140 |

The market's own October-2002 low (a two-sided +/-2-4%/day whipsaw) produces zero reaction -- the rule is inert
at its band floor.

**2008-10-10** ("Lehman capitulation", held pinned at 0.2011x):
| date | spx ret% | VIX | held |
|---|---|---|---|
| 2008-10-07 | -4.48 | 53.7 | 0.201 |
| 2008-10-08 | -2.52 | 57.5 | 0.201 |
| 2008-10-09 | -6.98 | 63.9 | 0.201 |
| **2008-10-10** | **-2.43** | **70.0** | **0.201** |
| 2008-10-13 | +14.52 | 55.0 | 0.201 |
| 2008-10-14 | -1.48 | 55.1 | 0.201 |
| 2008-10-15 | -9.84 | 69.2 | 0.201 |
| 2008-10-16 | +4.17 | 67.6 | 0.201 |
| 2008-10-17 | -0.60 | 70.3 | 0.201 |
| 2008-10-20 | +6.01 | 53.0 | 0.201 |

**2008-11-20** ("Nov-08 low", held still pinned at 0.2011x -- six weeks after the Oct step-down, VIX has since
risen from 70 to 80.9 with no further de-lever):
| date | spx ret% | VIX | held |
|---|---|---|---|
| 2008-11-17 | -1.33 | 69.2 | 0.201 |
| 2008-11-18 | +1.88 | 67.6 | 0.201 |
| 2008-11-19 | -6.41 | 74.3 | 0.201 |
| **2008-11-20** | **-7.42** | **80.9** | **0.201** |
| 2008-11-21 | +5.39 | 72.7 | 0.201 |
| 2008-11-24 | +6.93 | 64.7 | 0.201 |
| 2008-11-25 | +0.74 | 60.9 | 0.201 |
| 2008-11-26 | +3.86 | 54.9 | 0.201 |
| 2008-11-28 | +1.26 | 55.8 | 0.201 |
| 2008-12-01 | -8.86 | 68.5 | 0.201 |

**2009-03-09** ("GFC low", still 0.2011x, five months after the Oct-2008 step-down):
| date | spx ret% | VIX | held |
|---|---|---|---|
| 2009-03-04 | +2.37 | 47.6 | 0.201 |
| 2009-03-05 | -4.08 | 50.2 | 0.201 |
| 2009-03-06 | +0.17 | 49.3 | 0.201 |
| **2009-03-09** | **-1.18** | **49.7** | **0.201** |
| 2009-03-10 | +5.96 | 44.4 | 0.201 |
| 2009-03-11 | +0.65 | 43.6 | 0.201 |
| 2009-03-12 | +3.94 | 41.2 | 0.201 |
| 2009-03-13 | +0.78 | 42.4 | 0.201 |
| 2009-03-16 | -0.30 | 43.7 | 0.201 |
| 2009-03-17 | +3.06 | 40.8 | 0.201 |

The same 0.201x level persists across three ladders spanning October 2008 to March 2009 (Lehman, the Nov-08 low
and the eventual GFC low) -- one band-down move in mid-September 2008 accounts for the entire crisis, confirming
the "late re-entry" prediction from the mechanism section: the rule is not still reacting to the crash's worst
acceleration or timing the actual low, it is coasting on a level fixed weeks earlier.

## 9. Iteration count

From `volmanaged_iterations.csv` (807 lines incl. header = **806 distinct parameter sets**) and
`volmanaged_count_iterations.py`'s own tally: **821 total evaluations including repeats** across
`volmanaged_grid.csv` (540), `volmanaged_grid2_grid.csv` (216), `volmanaged_batch1.json` (23), `volmanaged_batch2.json`
(22), `volmanaged_batch3.json` (16), plus 4 individual smoke/diagnostic re-runs (the harness smoke test, the
batch-1-baseline diagnostic re-run, and the final-point diagnostic re-run twice under different tags). Per the
brief's counting rule (a grid counts as one grid; each manual re-run counts as one), the reportable iteration
count is **806 distinct parameter combinations** evaluated on DEV.

## 10. Honest weaknesses and the regime that would break it

1. **Trails buy-and-hold in bull markets.** 1950-1969 era: Sharpe 0.51 vs SPY 0.85, CAGR 11.5% vs SPY 13.3%
   (worse on both). 1990-1999 era: Sharpe 0.81 vs SPY 0.95, CAGR 13.6% vs SPY 18.0%. Even the DD-favourable
   1970-1989 era has Sharpe 0.10 vs SPY's 0.28 (CAGR 8.4% vs 11.5%; DD is better, -27.1% vs -42.7%, but the
   Sharpe gap shows the era's edge is mostly a drawdown story, not a risk-adjusted-return story). A regime of
   several consecutive calm-to-moderate bull years (no repeat of a 1990s-style Sharpe boost from cutting risk in
   the rare down months) is exactly where this rule gives up the most relative return, because
   `avg_leverage_when_invested` is only 0.63x in dev_1990 -- the rule is well below 1x most of the time, not
   frequently at the 3x cap.
2. **Leverage effect quantified.** 1987: avg leverage over the 90-day crash window was 0.19x; the rule still lost
   -11.5% (vs SPY -25.0%) because it entered Black Monday itself at 0.39x, not near-zero (-7.97% same-day loss),
   and then sat at 0.03x for the rest of October, missing the +5.3%/+9.1% rebound days. GFC: avg leverage over
   the 356-day 2007-09 window was 0.43x, but the event ladders (§8) show the *effective* de-lever was a single
   step (0.54x -> 0.20x) in mid-September 2008 that then held flat for the Oct/Nov acceleration, the actual
   November low, and the March-2009 low five months later -- the rule does not react a second time inside a
   single sustained crisis once it has already stepped down once and landed at or below `band_dn`.
3. **2009 recovery capture is poor by design**: +11.4% vs SPY's +67.4% at a constant 0.20x -- confirmed exactly
   as predicted pre-run. This lens is structurally the wrong tool for capturing a V-shaped, still-high-vol
   recovery; that is the trade-off for its crash behaviour, not a bug.
4. **A previously-undocumented structural artifact, found while finishing (not tuned away, and not a bug in
   shared code -- it lives entirely in this signal's own band logic):** once the held level `H_t` falls to or
   below `band_dn` (0.30), the de-lever condition `H_{t-1} - T_t > band_dn` can never trigger again, because
   `T_t >= 0` always, so `H_{t-1} - T_t <= H_{t-1} <= 0.30 = band_dn` (never strictly greater). Every held level
   observed below ~0.30x in the data (e.g. 0.14x through the entire 2000-02 bear, 0.03x after 19-Oct-1987) was
   reached either from the unconditional first post-warm-up assignment (`cur = target` with no band check) or
   from a single band-down step that landed below 0.30, not from a second, deeper in-bear de-lever. In effect the
   asymmetric band gives the rule exactly one "emergency" de-lever per crisis; after that it is frozen until a
   large (>0.75) re-levering signal fires. This is a reasonable design (it caps whipsaw) but it means the rule
   is not continuously responsive to a crisis that keeps deepening after the first step down -- which is also
   why the 2008-10-10, 2008-11-20 and 2009-03-09 ladders (§8) all show the identical 0.201x level.
5. **No true cash state after warm-up.** `pct_days_cash = 0.0%` in both dev_1990 and dev_1950; the smallest
   leverage bucket ever observed in dev_1990 is 0.14x (`leverage_distribution_dev_1990`). "0 = cash" (per the
   docstring) applies only during the 20-session EWMA warm-up; the crash floor thereafter is a soft ~0.03-0.20x,
   never a hard exit. A regime demanding a genuine zero-exposure response (not just "small") would not get one
   from this rule.
6. **No directional input.** By construction the rule cannot distinguish a grinding moderate-vol bear (where it
   is right to be de-levered) from a grinding moderate-vol advance (where it gives up the identical amount of
   upside) -- it reacts to variance, not to the sign of returns. The 1970-1989 Sharpe shortfall vs SPY (item 1)
   is partly this.

## 11. Bugs found in shared code

None. No mention of a shared-code (`engine.py`/`features.py`/`dev_harness.py`) bug anywhere in
`volmanaged_scratch_log.csv`, the batch JSONs, or the pre-existing design-note sections; the lookahead check
(`lookahead_check.ok = True`, `max_abs_diff = 0.0` at all five cutoffs) also shows no engine-side lookahead issue
surfaced by this signal.

