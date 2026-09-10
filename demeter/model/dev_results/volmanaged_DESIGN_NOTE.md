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
