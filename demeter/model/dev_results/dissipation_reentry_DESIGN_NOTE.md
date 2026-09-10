# dissipation_reentry — design note (lens 2, pass 2)

Signal file: `signals/dissipation_reentry.py`. Designer: candidate 2. DEV window only (data ending 2012-06-30 via
`dev_harness.py` / `E.load_market(end="2012-06-30")`). Written incrementally; the Mechanism section below was written
BEFORE the first harness run and has not been edited since (additions to later sections are dated in place).

## Mechanism (written before any run — 2026-09-04, before the first grid)

**The question this lens answers.** The pass-1 trap (`vix_dissipation`: 3x when VIX < its 10-day SMA) re-entered
levered into the 2000-02 and 2007-09 bears 26 and 14 times, 77-79% of those entries negative over the next ten
sessions, and lost 80%/67% in those episodes. The record's own re-entry (23-Mar-2020) was not "VIX below its SMA";
it was a *bullish vol divergence*: price at a fresh low (RSI(2) = 8, -34% from high) while VIX, at 61.6, sat 25% below
its 16-Mar peak. This lens asks whether a re-entry conditioned on that stricter profile — dissipation from an extreme
that is still an extreme, coincident with a fresh price down-thrust — can be made non-ruinous in the two grinding
DEV bears WITHOUT any trend filter, and whether it then earns anything.

**Why it could work (mechanism, not curve).** Implied vol is a forward-looking price of insurance. At a genuine
capitulation low, the marginal panic buyer of protection is exhausted before the last sellers of stock are: VIX puts in
its high days before price does, so the last leg down comes with a *lower* VIX high. That divergence is what the
23-Mar-2020 profile shows and it is a known bottom signature (1987-10-20/21, 2008-11-21, 2009-03-06/09, 2002-10-10 are
the candidates in DEV). Requiring VIX still above an absolute level (30-40) keeps the rule from firing on ordinary
pullbacks (where the pass-1 trap fired constantly) and restricts it to environments where the variance premium
harvest per unit of time is largest (vix_vrp's PANIC sort: Sharpe 0.8-1.2 above VIX 30). Requiring RSI(2) < 20
(price still being sold) instead of "price back above its 20-day SMA" is deliberate: the SMA leg is a mini trend
filter and is what let `shock_reentry` re-enter after up days; RSI(2) < 20 can only be true after down days, so
"VIX lower + price lower" is genuinely a divergence, not a rally chase.

**Why it might fail (pre-mortem, stated now so I cannot re-explain it later).**
1. In 2008 VIX made successive HIGHER highs (Oct-10 70, Oct-27 80, Nov-20 81) as price made lower lows: no
   divergence appears until the Mar-2009 low, and at that low VIX (49.7) was only ~5% below its 20-day max. A 20-30 day
   window will therefore likely miss the 2009 low; a window long enough to reach back to the Nov-2008 peak (≈ 70-90
   days) would catch Mar-2009 but would also fire in Jan-2009 (VIX 49 vs 81) and lose ~20% of index at 3x before the
   low. Prediction: the vix_win parameter has a cliff, and the 2009 recovery is captured mostly by the default tier,
   late, not by the re-entry.
2. In 2000-02 VIX rarely exceeded 30 and the bear ground down without capitulation spikes until Sep-2001 and
   Jul/Oct-2002. Prediction: few fires (< 8 in 638 sessions) at vix_min ≥ 30, so the rule is "safe by silence" rather
   than by skill there; the danger is the Sep-Oct-2001 and Jul-Aug-2002 post-spike dips.
3. The Oct-2002 low (VIX 42 on the low day, 45 two days before) shows no 25% divergence either. Prediction: missed.
4. The two-consecutive-sigma-day exit cannot fire inside a crash (at 60% RV a 2-sigma day is -7.6%), so the only
   protection on a burst is the bounded hold H. If a burst is placed a week before a Nov-2008-style leg, it loses
   3 x (leg) with nothing to stop it. Prediction: the hold_days parameter is where "non-ruinous" is decided.
5. Whipsaw at the RV threshold in the default engine (1x/cash flip-flop near rv_exit) will drive most of the trade
   count; the re-entry itself should contribute < 3 changes/yr.

**Design (state machine, decided at each close t, applied to t+1).** Three states.
* DEFAULT — the structural leverage tier of the incumbent (3x if RV21 < 0.10, 2x if RV21 < 0.15, else 1x), so the
  model is not cash-by-default in calm bull markets. Leaves DEFAULT on the stress trigger.
* STRESS — cash. Stress trigger = RV21 > rv_exit OR two consecutive days each below -2 sigma (sigma = previous day's
  RV21 / sqrt(252)). Leaves STRESS to DEFAULT when RV21 < 0.8 x rv_exit (hysteresis), or to REBOUND on the
  dissipation trigger.
* REBOUND — 3x. Dissipation trigger (all on the same close): VIX <= (1 - vix_fall) x max(VIX over the last vix_win
  sessions) AND VIX >= vix_min AND RSI(2) < 20. Hold exactly hold_days sessions (a fresh two-sigma double shock ends it
  early), then to DEFAULT if RV21 < 0.8 x rv_exit else STRESS. A new burst requires the trigger to fire again on a
  later day. The trigger may also fire from DEFAULT (same mechanism, no reason to require an intervening cash day).
* Pre-1990 (no VIX) the REBOUND state never occurs; the model is DEFAULT tier + stress exit only.

**Tunables (6):** rv_exit, vix_fall, vix_win, vix_min, hold_days, and — to be decided by what the grid shows about
1973-74 and the tier — NO sixth tunable is reserved yet; the sixth slot is held for a stop-loss on the burst
(cumulative index return since entry) if the grid shows hold_days alone cannot make 2008 non-ruinous. If the slot
is not needed it stays empty and n_tunable = 5.
**Structural constants (declared, never varied):** RV window 21 (scale only); tier thresholds 0.10/0.15 and levels
{3,2,1} borrowed verbatim from the incumbent `final_model_fewtrades` so the default engine is a known quantity;
RSI(2) < 20 (the brief's oversold definition; 23-Mar-2020 printed 8); sigma multiple Z = 2 for the double-shock exit
(conventional; two iid 2-sigma days ≈ once per 8 years by chance, Feb-2020's two -3% days at 10% vol were ≈ 4.7 sigma);
stress hysteresis 0.8 (RV must fall to 80% of rv_exit before the default tier resumes); rebound leverage 3x (the
record's Apr-2020 tier).

**What I will measure, in this order.** (1) Coarse grid, ≤ 600 combos, on rv_exit x vix_fall x vix_win x vix_min x
hold_days. (2) For the plateau candidate and the grid corners: an isolation script that lists every REBOUND burst
1990-2012 with entry date, VIX, VIX/max, RSI(2), burst length and the burst's own P&L at 3x net of 3 bp/60 bp — per
era counts, hit rate and summed P&L for 2000-02 and 2007-09 are the decisive numbers. (3) Only then the full harness
run with plateau and gate_check. If no region of the grid keeps 2000-02 and 2007-09 burst P&L non-ruinous without a
trend filter, that is the result and I stop there.

**Pre-declared success/failure reading.** "Non-ruinous" = burst P&L in each of 2000-02 and 2007-09 no worse than
-15% cumulative, with the episode's model total no worse than the incumbent's (-21.1% / -8.6%) by more than 10 points.
"Earns something" = the model's dev_1990 Sharpe with bursts exceeds the same model with the REBOUND state disabled
(same params) — I will run that ablation once and count it.

---
## Working log (banked as it happened; numbers copied from script output)

### Iterations 1-3 — smoke + two trigger corners (isolation script, 3 bp / 60 bp)
* Defaults (rv_exit .25, fall .25, win 20, vmin 35, H 10): **one burst in 22.5 years** — 2008-12-19 (VIX 44.9, 0.62 of
  its 20-day max, RSI2 19.7), +18.1% net. dev_1990 Sharpe 0.457 vs 0.423 with REBOUND disabled (+0.034). But the
  DEFAULT engine alone: 2000-02 bear **-47.6%** (SPY -47.2%), dev_1990 maxDD **-52.3%**. Without a trend filter the
  no-VIX default engine is buy-and-hold-with-a-tier through a grinding low-vol bear.
* Corner (vmin 30, fall .20, win 10, H 10): 4 bursts; 2008-11-06 (VIX 63.7, 0.795 of max) **-46.8%** straight-line
  (min path = final), exactly pre-mortem #1. Zero fires in 2000-02.
* Corner (vmin 30, fall .20, win 30, H 10): 16 bursts. **2000-02: 3 fires, 2 of 3 positive, +9.6% compound — not
  ruinous.** 2007-09: 4 fires, 1 of 4 positive, **-69% compound** (2008-11-06 -46.8%, 2009-02-13 -39.7%, 2009-01-09
  -19.1%, 2008-12-19 +18.1%). 2009 recovery: 2 fires, both positive, +36.8%. 2010-12H1: 5 fires, 4 positive, +36%.
  Model 2007-09 total -78.6% vs -30.5% with REBOUND off. The failure is precisely the VIX higher-high / price
  lower-low sequence of Oct-2008..Mar-2009. Zero fires in 1998 (VIX made its high on the low day both times).

### Grid 1 — 324 combos (dev_results/dissipation_reentry_g1_grid.csv; spec _grid_spec.json), no stop-loss
rv_exit {.20,.25,.30} x vix_fall {.20,.25,.30,.35} x vix_win {10,20,30} x vix_min {30,35,40} x hold_days {5,10,15}.
* Gate proxies: G2 (Sharpe ≥ .4253) 11/324; **G3 (maxDD ≥ -30%) 0/324** (best -51.4%); **G4 0/324** (worst era DD
  -49 to -80%); G5 324/324 (15-17 chg/yr). No row passes all.
* dev_1990 Sharpe range 0.03..0.468 (median 0.35). Best row: rv_exit .25, fall .25, win 30, vmin 30, H 10 → Sharpe
  0.468, CAGR 11.9%, maxDD -53.0%.
* Marginals: vix_fall .20 is the cliff (mean Sharpe .25, mean maxDD -68% vs .36 / -56% at ≥ .25; .30 and .35 are
  identical to each other — nothing fires between them). vix_min 30/35/40 nearly indistinguishable (fires are
  scarce above 30 anyway). hold_days 5 slightly better than 10, 15. rv_exit .25 best of the three on Sharpe;
  rv_exit .20 raises cash to 30% and still leaves maxDD -51%.
* Reading: the re-entry can be kept out of trouble (fall ≥ .25) but then it is a once-a-decade event; the model's
  drawdown is the default engine's 2000-02 loss and no trigger parameter can touch it.

### Decision after grid 1 (2026-09-04): fill the reserved sixth slot with the burst stop-loss (see docstring) — the two
2008/09 disasters were straight-line losses that a bounded hold cannot cap — and run a refinement grid that also
probes rv_exit .15/.18 as a DIAGNOSTIC of what the default engine would need to survive 2000-02 without a trend filter
(if only rv_exit ≤ .18 passes, the model has become a vol-level gate with a rare re-entry on top; that will be said).
Also fixed at this point: the loop allowed a same-day re-fire after a burst exit, contradicting the docstring; now a
natural expiry blocks re-entry for that close only, a stop-out blocks it for hold_days sessions.

### Iterations 328-329 — stop-loss corners (isolation script)
* fall .20 / win 30 / vmin 30 / H 10 / **stop .10**: same 16 bursts; 2007-09 compound **-69% → -28%** (stop-outs realise
  -13 to -17% because single days at 3x are -12 to -16%: gap risk), worst burst -17.1%; 2000-02 +5.9%; 2010-12 +30%.
  dev_1990 Sharpe 0.455 (REBOUND off 0.423), 2007-09 model total -50.0% vs -30.5% with REBOUND off — the bursts still
  cost 20 points in the GFC at fall .20.
* fall **.25** / win 30 / vmin 30 / H 10 / stop .10: 7 bursts. **2000-02: 2 fires, -1.7% compound. 2007-09: 2 fires,
  -0.4% compound (+18.1% 2008-12-19, -15.7% 2009-01-09 stopped after 3 sessions).** 2009 recovery: 0 fires (the
  Mar-2009 low shows no divergence within 30 sessions). 2010-12H1: 2 fires, +23.9%. dev_1990 Sharpe 0.470 vs 0.423
  REBOUND off (+0.047); 2007-09 model total -30.8% vs -30.5%. This is the first configuration that meets the
  pre-declared "non-ruinous" bar in BOTH bears. It does so by firing twice per bear.

### Grid 2 — 288 combos (dev_results/dissipation_reentry_g2_grid.csv; spec _grid2_spec.json), tier default, with stop
rv_exit {.15,.18,.20,.25} x vix_fall {.20,.25,.30} x vix_win {20,30} x vix_min {30,35} x hold_days {5,10} x stop {.08,.12,off}.
* G2 22/288, **G3 36/288 — all 36 at rv_exit .15** (maxDD -23.5%), G4 **0/288**, G5 288/288. No row passes all.
* The stop-loss: mean maxDD -49.2% (on) vs -53.4% (off), mean Sharpe .317 vs .295; .08 and .12 identical in every
  row (no burst path lands between them). vix_fall .20 remains the cliff (-58.9% mean maxDD). vix_win, vix_min and
  hold_days are second-order.
* rv_exit .18 is a Sharpe hole for the TIER default (.214 vs .344 at .15 and .291 at .20): resuming at 0.8 x .18 = .144
  puts the model straight into the 2x tier in mid-vol regimes. That interaction is the tier's, not the trigger's.
* At rv_exit .15 the G4 failure is a constant -46.9% worst-era DD across all VIX parameters → a pre-1990 era, i.e. the
  borrowed tier alone.

### Iterations 613-616 — single runs at the rv_exit .15 row (fall .25, win 30, vmin 30, H 10, stop .10)
| default engine | dev_1990 Sharpe | maxDD | chg/yr | cash | 1950-69 DD | 1970-89 DD | 1990-99 DD | 2000-12 DD | G4 |
|---|---|---|---|---|---|---|---|---|---|
| incumbent tier 3/2/1 (harness, _r15.json) | 0.45 | -23.5% | 10.2 | 52% | **-46.9%** | **-43.7%** | -23.5% | -20.3% | FAIL |
| tier 2/2/1 | 0.435 | -20.6% | 3.9 | 52% | -38.8% | -36.5% | -16.3% | -14.8% | pass (barely) |
| **flat 1x** | **0.447** | **-12.4%** | **3.9** | 52% | -19.6% | -13.8% | -8.0% | -12.4% | **pass** |
The tier levers into 1962 and 1973-74 with nothing to stop it (no trend, no VIX); flat 1x costs nothing in Sharpe.
Bursts are identical across the three (7 bursts; 2000-02 two fires -1.7%, 2007-09 two fires -0.4%). REBOUND-off ablation
at this row (tier default): Sharpe 0.379 → 0.445 with bursts (+0.066), i.e. the re-entry is now a third of the model's
edge over buy-and-hold (0.39).
**Structural decision (disclosed as a DEV-informed choice between the two defaults the brief allows): flat 1x.**
Candidate frozen for grid 3: rv_exit .15, vix_fall .25, vix_win 30, vix_min 30, hold_days 10, stop_loss .10 — subject to
grid 3 showing rv_exit .15 is on a plateau of the flat-1x version and not the edge of a cliff (it was the lowest value
in grid 2, so this must be checked before freezing).

### Iteration 617 — REBOUND-off ablation of the flat-1x candidate (isolation script, _bursts_frozen.csv)
| | Sharpe dev_1990 | CAGR | maxDD | chg/yr | 2000-02 | 2007-09 | 2009 rec. |
|---|---|---|---|---|---|---|---|
| flat 1x + RV gate + bursts (candidate) | **0.447** | 7.86% | -12.4% | 3.9 | +2.8% | -0.6% | +0.5% |
| same, REBOUND disabled | 0.389 | 6.16% | -8.0% | 3.2 | +4.7% | -0.2% | +0.5% |
Without the re-entry the model is a 1x realised-vol gate that FAILS G2 (0.389 < 0.4253). The seven bursts add +0.058
Sharpe and +1.7% CAGR for 4.4 points of extra drawdown; in the two bears they cost 1.9 and 0.4 points. The 2009 recovery
is missed either way (+0.5% vs SPY +67%): the Mar-2009 low had no 30-session VIX divergence, and RV21 stayed above 15%
until well into the rally.

## Rules (final form; identical to the signal file docstring)
1. DEFAULT engine (structural, borrowed verbatim from the incumbent): 3x if RV21 < 0.10, 2x if RV21 < 0.15, else 1x.
2. STRESS -> cash when RV21 > rv_exit OR two consecutive days each below -2 sigma (sigma = previous day's RV21/sqrt(252));
   back to DEFAULT only when RV21 < 0.8 x rv_exit.
3. REBOUND -> 3x, no trend condition, when on the same close VIX <= (1 - vix_fall) x trailing vix_win-day max AND
   VIX >= vix_min AND RSI(2) < 20. Held hold_days sessions unless ended early by a double shock or by the burst stop
   (burst's cumulative 3x excess return <= -stop_loss). Exit -> DEFAULT if RV21 < 0.8 x rv_exit else STRESS. After a
   natural expiry re-entry needs a later close; after a stop-out re-entry is blocked for hold_days sessions.
4. No VIX (pre-1990) -> rules 1-2 only. Warm-up -> 0. Leverage discrete {0,1,2,3}.

Frozen `DEFAULT_PARAMS = dict(rv_exit=0.15, vix_fall=0.25, vix_win=30, vix_min=30.0, hold_days=10, stop_loss=0.10)`.
Final harness run: `dev_results/dissipation_reentry.json` (3 bp / 60 bp, with plateau). All numbers below are copied from it
or from the isolation script's `_bursts_frozen.csv`.

## Parameters and how each was chosen (window: dev_1990 primary, dev_1950 for the non-VIX part; 3 grids, 828 combos)
| param | frozen | range explored | why this point |
|---|---|---|---|
| rv_exit | 0.15 | .12 .13 .15 .17 .18 .20 .25 .30 | Only .13-.15 pass G2+G3 with a flat-1x default (grid 3: 33 passing rows, all at .13/.15). .15 over .13: dev_1950 Sharpe .445 vs .363, cash 52% vs 64%, less extreme gate. **Weakest parameter**: +15%/+30% (0.1725/0.195) drop dev_1990 Sharpe to 0.30/0.28 (1x re-enters the 2000-02 bear when RV21 dips to 13-15%); -15%/-30% hold on dev_1990 but fail on dev_1950 (0.33/0.30). A one-sided cliff, disclosed. |
| vix_fall | 0.25 | .20 .25 .30 .35 | .20 is the cliff (Nov-6-2008 at 0.795 fires: -47% unstopped); .30/.35 leave a single burst in 22 years (a peak of one trade, see iteration 618). .25 is the middle. Perturbation -15% (0.2125) fails (0.298), -30% (0.175) holds (0.349) — fires are discrete events, response non-monotone. |
| vix_win | 30 | 10 20 30 | With 20 the frozen row has ONE burst (2008-12-19) and Sharpe 0.465 — higher, rejected as a one-trade peak. 30 gives seven bursts, i.e. the sample the lens exists to test. All four perturbations (21..39) hold (0.38-0.47). |
| vix_min | 30 | 25 30 35 40 | 30/35/40 indistinguishable in grids 1-2 (nothing fires between them); 25 slightly worse; 21 fails the plateau (0.307: fires on ordinary pullbacks). 30 = the brief's floor and the level where vix_vrp's PANIC sort begins. |
| hold_days | 10 | 5 10 15 | 10 ≥ 5 > 15 in grids 1-2. 13 fails the plateau (0.256): the tail days of a burst at 3x are where reversal losses sit. |
| stop_loss | 0.10 | .08 .10 .12 off | .08/.10/.12 identical in every grid row (no burst path lands between them); .07 → 0.49, .13 → 0.466. Flattest parameter. It matters only at vix_fall ≤ .20, where it converts -47%/-40% straight-line bursts into -13..-17% stop-outs (gap risk: single days at 3x are -12..-16%). Slot reserved before the first run, filled after grid 1. |

Structural choice made on DEV and disclosed: default engine flat 1x rather than the incumbent's 3/2/1 tier (both allowed
by the brief); the tier fails G4 in 1950-69 (-46.9%) and 1970-89 (-43.7%) because without a trend filter it levers into
1962 and 1973-74; flat 1x gives -19.6%/-13.8% at the same Sharpe (0.447 vs 0.445).

## Grid summary
* Grid 1 (324, tier default, no stop): G3 0/324, G4 0/324 — the default engine's -47% in 2000-02 dominates everything.
* Grid 2 (288, tier, stop): G3 36/288 all at rv_exit .15; G4 0/288 (pre-1990 eras, the tier).
* Grid 3 (216, flat 1x): **33/216 pass all gate proxies**, all at rv_exit ∈ {.13, .15}; Sharpe 0.018..0.511, maxDD -8.0..-46.0.
* Plateau (harness): **dev_1990 79% of 24** within 25% of base 0.4469 (fails: rv_exit +15/+30%, vix_fall -15%, vix_min -30%,
  hold_days +30%); dev_1950 92% of 24 (fails: rv_exit -15/-30%).
* Cliffs: rv_exit above ~0.16 (1x re-enters the 2000-02 bear: Sharpe 0.19 at .17, 0.13 at .18, 0.28 at .20); vix_fall at
  0.20 (the Nov-2008 fire); vix_min below ~22 (fires on pullbacks); hold_days ≥ 13.
* Cost rows (dev_1990): 2/40 Sharpe 0.4518 CAGR 7.92%; **3/60 Sharpe 0.4469 CAGR 7.86% maxDD -12.35%**; 6/90 Sharpe 0.4325
  CAGR 7.69% (still above the 0.4253 bar, by 0.007). Cost drag 0.15%/yr; 3.9 changes/yr.

## Gate results (`python gate_check.py dev_results/dissipation_reentry.json`, verbatim)
```
dissipation_reentry: ALL GATES PASS
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.44693380397095284 (bar 0.425)
  G3_dev1990_maxdd: pass  value=-12.351120013819127 (bar -30.0)
  G4_no_ruinous_era: pass
      1950-1969: ok: CAGR 9.50% maxDD -19.6%
      1970-1989: ok: CAGR 10.39% maxDD -13.8%
      1990-1999: ok: CAGR 9.90% maxDD -8.0%
      2000-2012H1: ok: CAGR 6.25% maxDD -12.4%
  G5_changes_per_year: pass  value=3.8653032440056414 (bar 25.0)
  G6_plateau: pass  value=0.7916666666666666 (bar 0.5)
  G7_param_budget: pass  value=6 (bar 6)
```
Headline DEV numbers (3/60): dev_1990 CAGR 7.86% (SPY 8.34%), Sharpe 0.447 (SPY 0.39), maxDD -12.4% (SPY -50.8%), worst
month -11.4%, cash 51.6% of days, avg leverage 0.50, beta 0.34, up-capture 52%, down-capture 33%, 3.9 changes/yr.
dev_1950 CAGR 9.19%, Sharpe 0.445 (SPY 0.47), maxDD -25.4%, cash 35%. Leverage distribution 1990-2012: 0x 51.6%, 1x 47.4%,
3x 1.0%. The model beats buy-and-hold on Sharpe by removing volatility, not by adding return.

## Stress narrative (model total / SPY total, from `stress_episodes`)
* **1987 crash: -1.0% / -25.0%**, cash 93%. RV21 crossed 15% in the first week of October; the ladder shows L0 from
  14-Oct on, so the model was already out before Black Monday — and stayed out through the +5.3%/+9.1% rebound and the rest
  of the year (RV21 > 12% until 1988). No VIX, so no re-entry: pure vol-gate behaviour.
* **1998 LTCM: -1.9% / +4.9%**, cash 92%. Zero bursts: on 31-Aug (VIX 44.3) and 8-Oct (VIX 45.7) implied vol made its HIGH
  on the low day — no divergence — and the Oct-Dec rally was missed because RV21 stayed above 12% into December.
* **2000-02 bear: +2.8% / -47.2%**, cash 94%, 8 changes in 638 sessions. Two bursts: 2001-10-29 (VIX 31.6, 0.72 of its
  30-day max, RSI2 15) +12.5% net over 10 sessions; 2002-08-28 (VIX 33.3, 0.74, RSI2 9) stopped after 3 sessions at -12.6%.
  Burst compound -1.7%. The 9/11 low (21-Sep: VIX 42.7, its max 43.7 the day before), the 23-Jul-2002 low (VIX 44.9 = max)
  and the 9-Oct-2002 low (VIX 42.1 vs 42.6 two days earlier) all show VIX peaking WITH price — no fire, L0 through each.
  The bear was survived by the RV gate keeping the model in cash 94% of the time, not by the re-entry.
* **2007-09 GFC: -0.6% / -54.8%**, cash 93%, 6 changes. Two bursts: 2008-12-19 (VIX 44.9, 0.56 of the Nov-20 peak, RSI2 20)
  +18.1%; 2009-01-09 (VIX 42.8, 0.63, RSI2 13) stopped after 3 sessions at -15.7% (the -5.3% 20-Jan day at 3x). Burst compound
  -0.4%. 10-Oct, 27-Oct and 20-Nov-2008 ladders: L0 throughout — VIX 70.0, 80.1, 80.9 were each a fresh high on the low day.
* **2009 recovery: +0.5% / +67.4%**, cash 95%. The 9-Mar low: VIX 49.7 against a 30-session max of ~52-57 (0.88-0.95), no
  divergence; RV21 stayed above 15% until the autumn, so the default engine was cash for the whole rally. **The recovery is
  missed entirely** — worse than the incumbent's +6.6% — and this is the vol-level gate's structural cost, exactly as the
  inference note warns for Mar/Apr-2020.
* **2010 flash: +13.6% / -8.4%**, cash 77%, 14.5% of days at 3x. One burst, 2010-06-29 (VIX 34.1, 0.745 of the 21-May max
  45.8, RSI2 3, -14% from the 60-day high) → +15.7% net, holding 3x through the 2-Jul low and the first eight sessions of the
  July rally. The cleanest divergence catch in DEV. (2010-05-14 at 0.763 did not fire at vix_fall .25; in the .20 corner it
  fired and lost 12.6%.)
* **2011 debt: +7.0% / -5.6%**, cash 91%. One burst, 2011-09-02 (VIX 33.9, 0.71 of the 8-Aug 48.0, RSI2 11) → +7.1%. The
  8-Aug downgrade day (VIX 48.0 = new max) and the 3-Oct low (VIX 45.5 = max) were L0: same non-divergence pattern.

## Spurious re-entry census (harness `spurious_reentry_census`, entries to ≥2x and next-10-session excess return)
| episode | this model | pass-1 trap `vix_dissipation` | incumbent |
|---|---|---|---|
| 2000-02 bear | **2** entries (2001-10-29, 2002-08-28), mean fwd10 **+0.62%**, 50% negative, 2.0% of days ≥2x | 26 entries, -2.34%, 77% negative, 19.9% of days | 1 entry, -1.33%, 100% neg |
| 2007-09 GFC | **2** entries (2008-12-19, 2009-01-09), mean fwd10 **-0.05%**, 50% negative, 3.7% of days | 14 entries, -3.17%, 79% negative, 10.1% of days | 0 |

Per-era isolated burst P&L at 3x net of 3 bp/60 bp (`dev_results/dissipation_reentry_isolate.py`, `_bursts_frozen.csv`):
| era | n bursts | hit rate | compound P&L | worst | notes |
|---|---|---|---|---|---|
| 1990-1999 | 0 | — | — | — | 1997-12-24 fires only at vix_fall .20 (-4.8%) |
| 2000-02 bear | 2 | 0.50 | **-1.7%** | -12.6% | +12.5% (Oct-01), -12.6% stop-out (Aug-02) |
| 2002-03 recovery | 1 | 1.00 | +18.0% | — | 2002-11-11 (VIX 31.3, 0.73, RSI2 9) |
| 2004-2007 Q3 | 0 | — | — | — | VIX never ≥ 30 |
| 2007-09 GFC | 2 | 0.50 | **-0.4%** | -15.7% | +18.1% (Dec-08), -15.7% stop-out (Jan-09) |
| 2009 recovery | 0 | — | — | — | no 30-session divergence at the Mar-09 low |
| 2010-2012H1 | 2 | 1.00 | +23.9% | — | +15.7% (Jun-10), +7.1% (Sep-11) |

**Answer to the lens question.** (1) The divergence re-entry is NOT the pass-1 trap: conditioning on VIX ≥ 30 AND ≥ 25%
below its 30-day max AND RSI(2) < 20 cuts the 2000-02 / 2007-09 entries from 26 / 14 to 2 / 2 and their 10-day mean from
-2.3% / -3.2% to +0.6% / -0.05%. In 2000-02 this is largely silence — VIX rarely reached 30 with a divergence — but the
two that fired netted -1.7%, inside the pre-declared -15% bar. (2) In 2007-09 the mechanism is intrinsically dangerous:
Oct-2008 → Mar-2009 is a sequence of VIX HIGHER highs on price LOWER lows, so the divergence appears only in the
Dec-08/Jan-09 lull, and at vix_fall .20 it fires into the Nov-2008 leg for -47% (four fires, -69% compound, exactly the
pre-mortem). It is made non-ruinous by two levers, both without a trend filter: vix_fall ≥ .25 (drops the Nov-6 and Feb-13
fires) and the 10% burst stop (caps the Jan-9 fire at -15.7% instead of -19%; at vix_fall .20 turns -69% into -28%).
Result -0.4% compound in the GFC. (3) It cannot be made to CATCH the 2002 or 2009 lows: neither showed a divergence,
and 1998, Sep-2001, Jul-2002, Oct-2008, Nov-2008 all had VIX peaking on the low day. The 23-Mar-2020 profile
(VIX 25% below a peak five sessions earlier, price at a new low) is rarer in DEV than the record makes it look: seven
fires in 22.5 years, four winners. (4) The model built around it passes all seven gates ONLY because the default engine
is a flat-1x realised-vol LEVEL gate at 15% — an ingredient the inference note rules out for reproducing 2020, and one with
a knife-edge at rv_exit ≈ 0.16-0.17 where 1x re-enters the 2000-02 bear and Sharpe drops to 0.19-0.30. Without the bursts
the same gate scores 0.389 and fails G2; the seven bursts are what lift it over the bar (+0.058 Sharpe, +1.7% CAGR).

## Event ladders (target leverage decided at each close; `event_ladders`)
2008-10-10 Lehman capitulation — L0 every day: 07-Oct -4.5% VIX 53.7 | 08 -2.5% 57.5 | 09 -7.0% 63.9 | **10 -2.4% 70.0** |
13 +14.5% 55.0 | 14 -1.5% 55.1 | 15 -9.8% 69.2 | 16 +4.2% 67.6 | 17 -0.6% 70.3 | 20 +6.0% 53.0. VIX made a new 30-day
high on the low day (70.0) and again on 17-Oct; the 13-Oct +14.5% day left RSI(2) high. Nothing to fire on; stress exit
had been in force since mid-September (RV21 > 15%).
2008-11-20 Nov-08 low — L0 every day: 17-Nov -1.3% 69.2 | 18 +1.9% 67.6 | 19 -6.4% 74.3 | **20 -7.4% 80.9** | 21 +5.4% 72.7 |
24 +6.9% 64.7 | 25 +0.7% 60.9 | 26 +3.9% 54.9 | 28 +1.3% 55.8 | 01-Dec -8.9% 68.5. VIX 80.9 = the cycle high on the low
day; the fall to 54.9 by 26-Nov came on UP days (RSI(2) high), so no divergence; 1-Dec (-8.9%, VIX 68.5 = 0.85 of max) did
not qualify either. The burst finally fired on 19-Dec at VIX 44.9 (0.56) and earned +18%.
2009-03-09 GFC low — L0 every day: 04-Mar +2.4% 47.6 | 05 -4.1% 50.2 | 06 +0.2% 49.3 | **09 -1.2% 49.7** | 10 +6.0% 44.4 |
11 +0.7% 43.6 | 12 +3.9% 41.2 | 13 +0.8% 42.4 | 16 -0.3% 43.7 | 17 +3.1% 40.8. VIX 49.7 vs a 30-session max in the
low-50s (0.88-0.95): the divergence condition needs the Nov-20 peak, 72 sessions back. The 9-Jan burst (0.63 of the
Dec-1 68.5) had already been stopped out and its hold_days block expired; nothing re-fired. RV21 kept the default engine
in cash for the whole recovery.
2002-10-09 bear low — L0 every day: 04-Oct -1.8% 39.5 | 07 -2.1% 42.6 | 08 +1.6% 41.0 | **09 -2.8% 42.1** | 10 +3.2% 37.5 |
11 +4.4% 35.7 | 14 +0.6% 36.0 | 15 +4.8% 34.0 | 16 -2.4% 36.0 | 17 +2.0% 34.1. VIX 42.1 on the low day vs 42.6 two days
earlier and ~45 in early Aug (30-session max): 0.93. No divergence; the rally to 17-Oct was missed. The 2002-11-11 fire
(VIX 31.3, 0.73) caught the second leg for +18%.
(Also in the JSON, all L0 on the low day: 1987-10-19, 1998-08-31, 1998-10-08, 2001-09-21, 2002-07-23, 2008-10-27, 2011-08-08,
2011-10-03. The only ladder showing L3 is 2010-07-02, from the 29-Jun fire.)

## Iteration count
Distinct parameter sets evaluated on DEV: **864** = grid 1 (324) + grid 2 (288) + grid 3 (216) + 12 manual single runs
(smoke defaults; two trigger corners; two stop corners; the rv_exit .15 row via harness and via the isolation script; flat
1x; tier 2/2/1; the frozen row via the isolation script; the final harness run; the vix_win-20 alternative) + the 24
single-parameter perturbations the harness evaluated for the plateau (each on two windows). Grid rows are stored in
`dev_results/dissipation_reentry_g1_grid.csv`, `_g2_grid.csv`, `_g3_grid.csv`; the required `dev_results/dissipation_reentry_grid.csv`
is a copy of grid 3 (the grid the frozen parameters come from). Scratch: `_isolate.py`, `_gridsum.py`, `_flat1x.py`, `_extract.py`.

## Honest weaknesses and the regime that would break it
1. **The protection is a vol-LEVEL gate with a knife-edge.** rv_exit .15 works in DEV because RV21 sat above 12-15% for 94%
   of 2000-02 and 93% of 2007-09. At .17 the model re-enters 1x in the bear's quieter stretches and Sharpe falls to 0.19;
   G6 passes only because the other five parameters are flat. A slow bear with RV21 in the 12-15% band (1973-74 had
   stretches like it; the flat-1x default survived it at -13.8% only because the 1974 leg was noisier) would be taken at 1x
   with no exit. The inference note rules this ingredient out for 2020: 'RV21<15%' gates earn ~0% in Mar/Apr-2020.
2. **It misses recoveries.** 2009: +0.5% vs +67%; 1987 and 1998 rebounds missed; up-capture 52%, avg leverage 0.50,
   CAGR below buy-and-hold in 1990-2012 (7.9% vs 8.3%) and 1950-2012 (9.2% vs ~11%). This is a low-beta (0.34) defensive
   strategy that wins on Sharpe by removing variance, not the record's 114% up-capture / 2x levered profile. It fails the
   record's leverage and up-capture targets outright; it meets the cash-share target (52%) by accident of the gate.
3. **The lens mechanism is statistically thin.** Seven bursts in 22.5 years, four winners; the +0.058 Sharpe uplift rests on
   the +18% (Dec-08), +18% (Nov-02), +15.7% (Jun-10), +12.5% (Oct-01) trades. One more Nov-2008-type sequence inside the
   .25 threshold would erase it. The vix_fall response is non-monotone (a discrete set of events), so the plateau
   reading on that axis is partly luck.
4. **Regime that breaks it:** a crash in which VIX keeps making higher highs on lower price lows for more than 30 sessions
   AND then produces a shallow divergence (0.70-0.75) before the final leg — every burst is stopped at -13..-17% and, with
   the hold_days re-entry block, the true low is then missed. Oct-08 → Mar-09 is that regime; the model escaped it in DEV
   by firing only twice. A 1987-style one-day crash at 3x inside a burst is unhedged: the stop is close-to-close and a
   -20% day is -60% of burst equity before it can act (no burst was live in Oct-1987, but that is luck of the calendar).
5. **What it would do in the OOS regime (stated as expectation, not used for any choice — [INFERENCE from the inference note's
   Appendix-B table, which I read but did not tune on]):** the 23-Mar-2020 close (VIX 61.6 vs 82.7 peak = 0.745, RSI2 8)
   satisfies the trigger, so a 10-session 3x burst would have started at the exact low; but Feb-2020 would be held at 1x until
   RV21 crossed 15% (~27-Feb) and the Apr-2020 rebound would be at most one more burst then cash — nothing like the record's
   14 of 21 days at 3x. 2022 would be mostly cash (RV21 20-30%) — the three 0.00% months yes, the Jul/Oct rallies no.
6. Gap risk on the stop realised -12.6% and -15.7% on a nominal -10%; at 6 bp / 90 bp the Sharpe margin over G2 is 0.007.

## Bugs found in shared code
None. (Cosmetic only: `gate_check.py` prints the G2 bar as 0.425 while the constant is 0.4253 — Python float formatting of
the tuple; the comparison uses 0.4253.) One caution for other designers, not a bug: `dev_harness.plateau` rounds integer
parameters, so `hold_days=10` at -15% is tested at 8 (round-half-even of 8.5) and at +15% at 12 — the tested set is
{7, 8, 12, 13}, not symmetric.
