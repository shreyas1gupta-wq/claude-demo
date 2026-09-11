# crash_exit_dual — design note (Lens 1: two separate decisions with a real crash exit)

Designer: pass-2 candidate, lens 1. Development data only (harness-truncated at 2012-06-30). Written incrementally;
timestamps are Asia/Kolkata 2026-09-04. Every number in the later sections is copied from
`dev_results/crash_exit_dual*.json` / `_grid.csv`, never from memory.

## Verdict (added by the finisher, 2026-09-10, from the frozen point already banked — no re-tuning performed)

**Gate failure.** `crash_exit_dual` clears G1, G2, G5, G6, G7 (dev_1990 Sharpe 0.4494, comfortably above the 0.425
bar) but fails **G3** (dev_1990 monthly maxDD −52.76% against the −30% bar) and **G4** (three of the four eras are
ruinous by the −40% DD test: 1950-1969 CAGR 16.31%/DD −42.7%, 1970-1989 CAGR 13.48%/DD −46.9%, 2000-2012H1 CAGR
2.06%/DD −51.8%; only 1990-1999 clears at DD −23.9%). Per PREREG.md this candidate earns no out-of-sample look and
was never run through `evaluate.py`. **Why, mechanically:** the lens's exit is a genuine σ-normalised or
VIX-jump crash trigger, and it does exactly what it was designed to do on discrete shock events — 1987 −8.8% vs
SPY −25.0%, the GFC exit fired 15-Sep-2008 and stayed OUT through the October capitulation and the November low
(§7, §9). What it structurally cannot see is a **grinding bear that never produces a qualifying shock**: 2000-02
(−54.2%, *worse* than SPY's −47.2%) and the Jan–Mar-2009 second leg down were both ridden at the 1x tier floor
the entire way, because no single day or two-day cluster crossed k·σ and no VIX close jumped `j` above its
10-day mean while vol stayed chronically — not acutely — elevated (§7 items 2000-02 and GFC; §11 item 1-2). The
census (§8) shows the same "default IN" design also lets Decision B's 2x tier fire inside bear-market rallies (6
times in 2000-02, 4 in 2007-09; 75-83% of those followed by 10-day losses). The grid search — 1,272 combos across
four grid files (§5) — never found a point that fixes the drawdown without giving up the Sharpe edge: the
drawdown surface is flat at −50…−57% across the entire feasible k/j/rv region, and the one DD-constrained variant
actually tested (`ddalt`, j=0.10: DD −26.5%, 45% cash) drops Sharpe to 0.34 (below SPY's 0.39) and *still* fails
G4 on 1970-89 (DD −49.3%). This reads as a genuine, non-tunable failure of the lens as specified — "am I in the
market" defaulting to IN with only crash-shock exits — rather than a parameter-search miss: a trigger built to
catch discrete shocks cannot handle a slow bleed at 1-2σ/day, which is exactly the failure mode §1's mechanism
section predicted before any run.

**Spot-check of sections 7-9 against `dev_results/crash_exit_dual.json` (finisher verification, 2026-09-10):** five
numbers checked — (1) §7 1987 "−8.8% vs −25.0%, avgL 0.72, cash 32%" = JSON `1987_crash` model −8.784%/SPY
−24.968%/avg_leverage 0.7222/pct_days_cash 32.22% ✓; (2) §7 2000-02 "−54.2% vs −47.2%, avgL 0.96, cash 14%, 22
changes" = JSON model −54.218%/SPY −47.204%/avg_leverage 0.9561/cash 14.42%/n_changes 22 ✓; (3) §7 GFC "−42.5% vs
−54.8%, avgL 0.90, cash 20%" = JSON model −42.504%/SPY −54.767%/avg_leverage 0.9045/cash 19.94% ✓; (4) §7 2009
recovery "+53.8% vs +67.4%, avgL 1.03, cash 10%" = JSON model 53.770%/SPY 67.405%/avg_leverage 1.0290/cash 10.14%
✓; (5) §6 headline block (CAGR 11.19%, Sharpe 0.449, DD −52.8%, worst month −13.2%, cash 13.5%, 12.0 chg/yr,
up-capture 133%, down-capture 131%, beta 1.11, avg leverage 1.57) = JSON `windows.dev_1990` all fields match to the
quoted precision ✓. **No mismatches found; no correction needed.**

## 1. Mechanism (written BEFORE any run of the signal)

**The two decisions and why they are separate.** The incumbent's down-capture of 146% comes from one entangled rule:
the invest/cash gate is a slow trend filter (SMA100/200) and the leverage tier is a trailing-vol level. Both are
*late* by construction — a 200-day average needs weeks of decline before it flips, and a 21-day realised-vol
threshold needs the crash days already inside the window before it rises. So the model is still levered on the
first two or three crash days, which is where the bulk of any crash loss sits (Oct-1987: three days; Aug-1998 and
Sep/Oct-2008: a handful of days each). The lens separates the two questions:

* **Decision A — "am I in the market?"** A state machine whose default is IN (no trend filter; the record rules a
  slow trend gate out and the DEV central question is the 2009 recovery, which a trend gate misses). It EXITS only
  on a genuine crash trigger, i.e. an event that is itself the first observation of a volatility regime change:
  1. **Consecutive multi-sigma down days**: two sessions in a row each below −k × σ, where σ is the trailing 21-day
     daily standard deviation measured *up to the previous close* (so the shock does not dilute its own z-score).
     Mechanism: volatility clusters (GARCH persistence) and the leverage effect makes down-moves raise future vol
     more than up-moves lower it. A single −3% day in a 12%-vol regime is a 4σ event but happens a few times a year
     and is as often reversed as continued (Aug-2019 in the record; Oct-1997 and Feb-2007 in DEV). Two in a row is
     rare outside crashes: the second day is measured against a σ already inflated by the first, so it must be a
     ~3σ day on the new, higher vol — that is the regime change, not noise. k is chosen so one −3% day does not
     trip it and two do (arithmetic: after a −3% day in a 12% regime σ rises from 0.76% to ~0.99%; a second −3%
     day is −3.0σ, a following −1.5% day is −1.5σ; so k in [2, 3) separates the cases).
  2. **Implied-vol jump** (VIX era only): VIX closes more than j above its own trailing 10-day mean while VIX is
     above an absolute floor of 20. Mechanism: option markets reprice tail risk within the session, before realised
     vol windows can; a jump from a calm base (VIX 12 → 15) is normal-regime noise, hence the floor. This catches
     gap-type shocks that the two-day price rule misses (a single −5% day with a VIX spike, e.g. 27-Aug-1998,
     15-Sep-2008, 29-Sep-2008).
  Once OUT, the state persists for at least `min_out` sessions **after the last shock day** (any single day below
  −kσ, or any VIX jump, restarts the clock — a crash is over when shocks stop arriving, not when a calendar
  expires) AND until a simple dissipation condition holds: the vol proxy (VIX; before 1990, 10-day realised vol) is
  below its own trailing `n_dis`-day mean. Dissipation is used rather than calm because the record (and 2009 in
  DEV) says the strongest days come while vol is still high but falling; a "vol is low again" re-entry misses
  them. No trend filter anywhere.
* **Decision B — "how much leverage?"** Independent and slower: 3x when 21-day realised vol < rv_lo, 2x when
  < rv_hi, else 1x, each tier held at least 5 sessions (one trading week; a structural anti-churn constant, not
  tuned). Mechanism: the risk-adjusted return of the equity premium is roughly constant-to-declining in vol
  (Moreira–Muir), so risk budget per unit of realised vol is spent in calm regimes and withdrawn in stormy ones;
  the discrete {1,2,3} grid mirrors Demeter's discrete tiers and keeps trading discrete. Decision B never goes to
  0 — cash is Decision A's job — so the tier is not a vol-LEVEL gate.

**Why it should have worked in 1950–2012 and 1990–2012.** The equity premium at 3x in calm regimes (1991–96,
2003–06, 1950s, 1960s, 1985–86) is where a levered long earns its return; the crash exit removes the
handful of days per decade that destroy a levered book (Oct-1987, Aug/Oct-1998, Sep–Nov-2008, May-2010,
Aug-2011); the shock-refreshed cool-down keeps the book out through the clustered aftermath, which is where
bear-market losses concentrate (1973–74, 2000–02, 2008 are sequences of shock clusters, not single days); the
dissipation re-entry gets the book back for the post-cluster rebound at whatever leverage Decision B allows (1x
in Apr-2009, rising to 3x by late 2009 as RV21 falls) instead of waiting months for a trend confirmation.

**What I expect it to cost.** Whipsaw: a false two-day trigger in a calm year costs `min_out` sessions of missed
3x drift plus two round-trip costs; the record says these are the losses to expect (whipsaw at 3x in choppy calm
months, not crash losses). The grinding bears are the risk to the gates: with default IN and a 1x floor, any
stretch of a bear that produces no −kσ pair and no VIX jump is ridden at 1x. The DEV tests that decide this
lens: (i) event ladders — does the exit fire BEFORE 19-Oct-1987, 31-Aug-1998, 29-Sep-2008 / 10-Oct-2008;
(ii) dev_1990 Sharpe with the exit disabled vs enabled (whipsaw cost, measured); (iii) the 2000-02 and 2007-09
spurious re-entry census; (iv) G3 (−30% monthly DD) and G4 in 1970-89 (1973-74 at 1x, 1987 at 1-2x).

**Pre-registered expectations (falsifiable).** Exit fires at or before the close preceding Black Monday only if
k ≤ ~2.2 (15-Oct-1987 was about −2.1σ); at k ≥ 2.5 the 1987 ladder shows the model IN on 19-Oct — I will report
which. LTCM and Lehman are caught by the VIX jump, not the price pair. Whipsaw cost ≤ 0.10 Sharpe in
dev_1990. 2000-02: mostly 1x with several exits; total between −15% and −30%. 2009 recovery: better than the
incumbent's +6.6% but below SPY's +67% because Decision B stays at 1x until RV21 falls.

**Parameter budget (6 tunables):** k (shock z), j (VIX jump fraction), min_out (sessions), n_dis (dissipation
window), rv_lo, rv_hi. **Structural constants (declared, not tuned):** σ window 21 days, lagged one day;
consecutive count 2; VIX-jump base = 10-day mean; VIX floor 20; tier minimum hold 5 sessions; leverage grid
{0,1,2,3}; RV10 as the pre-1990 vol proxy.

### 1a. DEV-driven structural change after the first run (iteration 1, before any grid)

First run (`crash_exit_dual_try1.json`, k=2.5 j=0.25 min_out=10 n_dis=10 rv_lo=0.12 rv_hi=0.18, individual-day
pair trigger): dev_1990 Sharpe 0.277, maxDD −75.0%; 2000-02 −75.5% (cash 12%, 35% of days at ≥2x); GFC −57.0%;
1987 −37.9% with the model IN (1x) on 19-Oct. Two findings, both mechanism-level, fixed before the grid:

1. **Trigger form.** The individual-day pair ("each of two consecutive days < −kσ") cannot catch 1987 at any k:
   14-Oct was −2.36σ and 15-Oct −1.72σ because the second day is measured on a σ already inflated by the first.
   The 2-day cumulative z (r_t + r_{t−1} against σ measured before both days) was −2.99 on 15-Oct and −3.91 on
   16-Oct. Per-year counts (DEV): at k=3.0 the 2-day z fires 21 times in 1990-99 and 18 in 2000-09 (37 clusters,
   1.6/yr); at k=3.5, 16 and 9 (0.9/yr); at k=4.0, 8 and 5. Its cost: single large days from a very calm base
   (27-Feb-2007 z2 −5.9, 13-Oct-1989 −8.4, 15-Nov-1991 −4.8) fire it while the individual pair tolerates them.
   A bounded whipsaw versus a catastrophic miss → the 2-day cumulative form is adopted; k grid moves to 3.0–4.0.
2. **Bears.** rv_hi=0.18 puts the tier at 2x in 15-18% RV, which is bear-market vol in 2000-02; and min_out=10 with
   a 10-day dissipation mean re-enters within two weeks of every shock. The grid must span long min_out (to 63),
   a long dissipation mean (to 63) and rv_hi down to 0.14. The lens's alternative re-entry ("vol below the
   exit-day level × (1−f)") is built as a scratch variant `dev_results/crash_exit_dual_R2.py` and gridded too,
   so the re-entry choice is made on DEV evidence, not taste.

Also observed (ingredient calibration, DEV): VIX jumps with floor 20 fire 146 times in 1990-2012H1 at j=0.20, 88
at 0.25, 52 at 0.30 — 15-Sep-2008 (1.36), 29-Sep-2008 (1.39), 6-May-2010 (1.61), 4-Aug-2011 (1.45), 27-Oct-1997
(1.49), 17-Sep-2001 (1.61), 4-Aug-1998 (1.33), 27-Aug-1998 (1.25) are all inside j ≤ 0.25 except LTCM's 27-Aug
at j=0.25 (borderline). Deep in a crash the price trigger goes quiet (6-9 Oct 2008: −1.4 to −2.2σ on a 3% σ) —
the OUT clock then relies on VIX jumps and the dissipation condition; noted as a failure mode in the docstring.

## 2. Rules (as implemented in `signals/crash_exit_dual.py`; decided at close t, applied to t+1)

**Decision A — IN/OUT state machine, initial and default state IN.**
1. Exit trigger (either): (a) two-session shock — (r_t + r_{t−1}) < −k·√2·σ, σ = 21-day daily std through close
   t−2; (b) VIX jump — VIX_t > (1+j)·mean(VIX_{t−10..t−1}) and VIX_t ≥ 20 (1990+ only).
2. Shock events that restart the OUT clock: a two-session shock, a single day r_t < −k·σ_{t−1}, or a VIX jump.
3. Re-entry when ≥ `min_out` sessions have elapsed since the last shock event AND the vol proxy is below its
   trailing `n_dis`-day mean (proxy = VIX close from 1990; 10-day realised vol ×100 before that). An exit trigger
   on the same close overrides a re-entry.
**Decision B — leverage tier, independent of A.**
4. RV21 < rv_lo → 3x; RV21 < rv_hi → 2x; else 1x; each tier held ≥ 5 sessions before it may change. Never 0.
**Output.** Target leverage = tier if IN, 0 if OUT; NaN during the 21-day warm-up. Grid {0,1,2,3}.
**Structural constants:** σ window 21; shock span 2 sessions; VIX base 10 sessions; VIX floor 20; tier hold 5;
pre-1990 proxy RV10. None was gridded.

## 3. Grid history (every DEV evaluation, in order; all at 3 bp / 60 bp through dev_harness.py)

| step | file | n combos | what it tested | result |
|---|---|---|---|---|
| try1 | `crash_exit_dual_try1.json` | 1 | individual-day pair trigger, k=2.5 j=0.25 min_out=10 n_dis=10 rv 0.12/0.18 | Sharpe 0.277, DD −75.0%; 1987 missed; 2000-02 −75.5% |
| gridR1 | `crash_exit_dual_gridR1_grid.csv` | 432 | 2-day z trigger; k{3,3.5,4} j{.2,.3} min_out{10,21,42,63} n_dis{10,21,63} rv_lo{.10,.12} rv_hi{.14,.16,.18} | 0 gate-passers; best Sharpe 0.449 (k4 j.3 mo21 nd10 .10/.14) at DD −52.8%; G3 passed by 1 combo, G4 by 0 |
| gridR2 | `crash_exit_dual_R2_gridR2_grid.csv` (scratch variant) | 576 | re-entry = proxy < exit-day level × (1−f), f{−.5,−.25,0,.15} | 0 passers; 57 clear G3 (all at f=0.15, Sharpe ≈0.21), 11 clear G2, none both → exit-level re-entry dropped |
| r1best | `crash_exit_dual_r1best.json` | 1 | best gridR1 point on revised code (proxy jump pre-1990, down-day gate) | Sharpe 0.45, DD −52.8%; 1987 −8.8% (OUT on 19-Oct), LTCM +7.2%, GFC −42.5%, 2000-02 −54.2%, 2009 +53.8% |
| noexit | `crash_exit_dual_noexit.json` | 1 | same tier, exit disabled (k=j=99) — the whipsaw/benefit control | Sharpe 0.43, DD −56.8%; 1987 −26.5%, GFC −57.5%, 2000-02 −53.9%, 2009 +65.4% |

**What gridR1/R2 say about the mechanism.** Longer `min_out` lowers Sharpe (marginal 0.30 → 0.18 from 10 → 63
sessions) while the drawdown barely moves (−65% → −56%): the bear losses are NOT in the weeks after a shock — the
cool-down already covers those — they are in the grinding stretches that never produce a σ-normalised shock at
all (Sep-2000..Mar-2001, Apr-Jul-2002, Jan-Aug-2008), which a default-IN book rides at the 1x tier floor.
`rv_hi`=0.14 is uniformly better than 0.18 (DD −52% vs −65%): 15-18% RV21 is bear-market vol in 2000-02 and must
map to 1x, not 2x. The exit itself earns its keep (exit ON vs OFF: Sharpe +0.02, 1987 −8.8% vs −26.5%, GFC −42.5%
vs −57.5%) but leaves 2000-02 untouched (−54% either way). Next test (gridR1b): the vol-jump trigger at lower j
(0.10–0.20), where the floor of 20 makes it a regime-dependent "vol rising while elevated" exit — it fires 13-16×/yr
in 2000-02 and 0-6×/yr in 2003-06 on DEV counts — applied to the RV10 proxy before 1990 and gated on a down day.

Later grids (same table format):

| step | file | n combos | what it tested | result |
|---|---|---|---|---|
| gridR1b | `crash_exit_dual_gridR1b_grid.csv` | 216 | low-j vol jump (proxy pre-1990, down-day gate): k{3.5,4,5} j{.10,.15,.20} min_out{10,21,42} n_dis{10,21} rv_lo{.10,.12} rv_hi{.14,.16} | 0 passers; j=0.10 clears G3 in 22 combos (best Sharpe 0.339, DD −26.5%, cash 45%) but G2 never (max 0.352); j=0.20 best Sharpe 0.391 at DD −57% |
| gridR1c | `crash_exit_dual_gridR1c_grid.csv` | 48 (47 valid) | refinement around the max-Sharpe region: k{4,5} j{.3,.4} min_out{15,21,30} n_dis{10} rv_lo{.09,.10} rv_hi{.13,.14} | 0 passers; Sharpe 0.40–0.45 across the block, DD −51…−55% everywhere → a genuine plateau in Sharpe, a wall in DD |
| ddalt | `crash_exit_dual_ddalt.json` (with plateau) | 1+24 | the DD-constrained alternative k4 j.10 mo21 nd21 .10/.14 | Sharpe 0.34, DD −26.5%, cash 45%, chg/yr 12.3, plateau 83%; 1970-89 DD −49.3% (G4 fail); 2009 recovery only +4.8% |
| final | `crash_exit_dual.json` (with plateau) | 1+24 | frozen DEFAULT_PARAMS k4 j.30 mo21 nd10 .10/.14 | Sharpe 0.449, DD −52.8% — gate_check below |
| memchk | `crash_exit_dual_memchk.json` | 1 | re-run of the R1c combo that raised MemoryError (k4 j.4 mo21 nd10 .09/.14) | runs clean: Sharpe 0.35, DD −55.2% → transient |

Deliverable grid: `dev_results/crash_exit_dual_grid.csv` = R1 + R1b + R1c concatenated (696 rows, `grid` column names the
source; 1 row carries the transient error). The R2 scratch grid has a different parameter (`f`) and stays in
`crash_exit_dual_R2_gridR2_grid.csv`.

## 4. Parameters and how each was chosen (window: dev_1990 = 1990-01-01..2012-06-30, plateau-checked on 1950-2012H1)

| param | frozen | grids spanned | why this value |
|---|---|---|---|
| k | 4.0 | 2.5 (try1, pair form), 3.0–5.0 (2-day z) | Sharpe rises 3.0→4.0 (marginal 0.19→0.29 in R1) and is flat 4.0→5.0 (R1c 0.370 vs 0.378); 4.0 keeps the price trigger alive (14 two-day events 1990-2012, 13 clusters) while 5.0 would hand almost everything to the vol jump. Plateau rows: k=3.4 → 0.418, 4.6 → 0.452, 5.2 → 0.464; the cliff is at 2.8 (0.297). |
| j | 0.30 | 0.10–0.40 | Non-monotone: 0.10 → DD −38% but Sharpe 0.25 (many elevated-regime exits, whipsaw); 0.15 → 0.155 (worst); 0.20 → 0.32; 0.30 → 0.37 (R1c marginal); 0.40 → 0.38. 0.30 sits inside the flat 0.25–0.40 stretch (plateau rows 0.255 → 0.389, 0.345 → 0.423, 0.39 → 0.404); the cliff is at 0.21 (0.332). |
| min_out | 21 | 10–63 | 21 is the marginal maximum in every grid (R1: 0.316 vs 0.302 at 10 and 0.20 at 42; R1c: 0.401 vs 0.359/0.364). Longer cool-downs cut Sharpe without curing the DD (see §3). Plateau rows 15 → 0.384, 18 → 0.399, 24 → 0.496, 27 → 0.440. |
| n_dis | 10 | 10–63 | Inert: marginal Sharpe 0.256/0.257/0.237 for 10/21/63 (R1), 0.244/0.234 (R1b); all four plateau rows within ±0.02. Kept at 10 (the simplest "VIX below its two-week mean"). |
| rv_lo | 0.10 | 0.09–0.12 | 0.10 beats 0.12 in every grid (R1 0.269 vs 0.232; R1c 0.402 vs 0.346 for 0.09). RV21 < 10% is roughly the calmest quartile of 1990-2012 (25th pct 10.3%). Plateau rows 0.07 → 0.452, 0.085 → 0.413, 0.115 → 0.448, 0.13 → 0.440. |
| rv_hi | 0.14 | 0.13–0.18 | Monotone: 0.14 best on Sharpe and DD in every grid (R1: 0.291/−52% vs 0.208/−65% at 0.18); 15-18% RV21 is bear-market vol in 2000-02 and must be 1x. Plateau rows 0.098 → 0.474, 0.119 → 0.427, 0.161 → 0.423; cliff at 0.182 (0.321). |

Structural constants (σ window 21, shock span 2, vol-jump base 10, floor 20, tier hold 5, proxy RV10) were fixed before the
grids and never varied. One structural choice WAS changed on DEV evidence: the trigger form (individual-day pair → 2-day
cumulative z, §1a, after iteration 1 and before any grid).

## 5. Grid summary

696 signal-file combos (R1 432, R1b 216, R1c 48) + 576 scratch-variant combos (R2). Gate-passers (G2∧G3∧G4∧G5 proxies
computed from the grid columns): **0 of 1,272**. G2 alone: 5 (R1) + 0 (R1b) + 7 (R1c) + 11 (R2). G3 alone: 1 (R1) + 22
(R1b) + 0 (R1c) + 57 (R2). G4: never. Plateau at the frozen point: 88% of 24 dev_1990 perturbations (21/24) within 25% of
Sharpe 0.449; 100% on dev_1950. Cliffs: k ≤ 2.8 (single calm-base days start firing the 2-day trigger → whipsaw), j ≤
0.21 (elevated-regime jumps fire too often), rv_hi ≥ 0.18 (bears at 2x). Sharpe is flat over k 3.4–5.2, j 0.25–0.40,
min_out 15–30, n_dis 7–13, rv_lo 0.07–0.13, rv_hi 0.10–0.16. The drawdown surface is flat too — at −50…−57% — which is
the finding: no parameter in this design moves the drawdown into the gate without pushing Sharpe below the incumbent.

## 6. Gate results (`python gate_check.py dev_results/crash_exit_dual.json`, verbatim)

```
crash_exit_dual: GATE FAILURE
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.4493867731101121 (bar 0.425)
  G3_dev1990_maxdd: FAIL  value=-52.76362471539806 (bar -30.0)
  G4_no_ruinous_era: FAIL
      1950-1969: FAIL: CAGR 16.31% maxDD -42.7%
      1970-1989: FAIL: CAGR 13.48% maxDD -46.9%
      1990-1999: ok: CAGR 23.77% maxDD -23.9%
      2000-2012H1: FAIL: CAGR 2.06% maxDD -51.8%
  G5_changes_per_year: pass  value=12.040197461212975 (bar 25.0)
  G6_plateau: pass  value=0.875 (bar 0.5)
  G7_param_budget: pass  value=6 (bar 6)
```

Headline numbers (dev_1990, 3 bp / 60 bp): CAGR 11.19%, Sharpe 0.449, monthly maxDD −52.8%, worst month −13.2%, cash
13.5% of days, 12.0 changes/yr, up-capture 133%, down-capture 131%, beta 1.11, avg leverage 1.57. At 6/90: CAGR 10.51%,
Sharpe 0.420, DD −53.1%. At 2/40: 11.50%, 0.463, −52.6%. dev_1950: CAGR 13.54%, Sharpe 0.440, DD −60.5%, 12.6 chg/yr.
Whipsaw cost, measured: exit disabled (k=j=99, same tier) gives dev_1990 Sharpe 0.43 / DD −56.8% vs 0.449 / −52.8% with
the exit; in the 1990-99 era 0.83 vs 0.85. The exit pays for its false alarms (+0.02 Sharpe) but cannot fix the drawdown.

## 7. Stress narrative (frozen point; model total vs SPY total over the harness windows)

* **1987 (−8.8% vs −25.0%; avgL 0.72, cash 32%).** The realised-vol proxy jumped on the −2.95% 14-Oct day (RV10 ≥ 20,
  down day) and the book was OUT from the 14-Oct close through Black Monday and the rest of October — the exit worked,
  by the proxy-jump rule rather than the 2-day z (−2.99 on 15-Oct, −3.91 on 16-Oct, both above k=4). The −8.8% is the
  Aug-25..Oct-13 slide taken at 1-2x before any trigger existed.
* **1998 LTCM (+7.2% vs +4.9%; cash 41%).** OUT from the 4-Aug VIX jump (1.33 × base), clock refreshed by 27-Aug (1.25)
  and 31-Aug (1.37); sat out the −7.1% 31-Aug day and the Sep-Oct chop; re-entered 12-Oct at 1x, two sessions after the
  8-Oct second low, and rode Q4 at 1x.
* **2000-02 (−54.2% vs −47.2%; avgL 0.96, cash 14%, 22 changes).** The failure. Eleven round trips covered 14% of the
  days; the rest was ridden at 1x (RV21 15-25%) with 9% of days at 2x. None of the down-legs (Sep-00..Mar-01, Jun-Sep-01
  ex-9/11, Apr-Jul-02) produced a −4σ two-day move, and VIX at 25-35 rarely jumped 30% above its own 10-day mean. Jul-02:
  the ladder shows 1x through −3.2/−3.5/−3.0/−2.7% (18-23 Jul) — z1 of −1.6 to −1.9 on a 1.8% σ.
* **2007-09 GFC (−42.5% vs −54.8%; avgL 0.90, cash 20%).** Exit on 15-Sep-2008 (VIX 31.7, 1.36 × base); OUT through the
  Oct capitulation (ladders 10-10, 10-27 all L0) and the 20-Nov low; re-entered 24-Nov at 1x, caught the Nov-Dec rally
  but also 1-Dec (−8.9%) at 1x, and — the second failure mode — stayed IN at 1x for the whole Jan-9-Mar-2009 leg
  (−25%): −4.3% and −4.5% days were −1.8σ / −2.1σ on a 2.2-2.4% σ, and VIX at 45-52 never jumped 30%. Oct-2007..Aug-2008
  (−20%) was mostly ridden at 1x with three short exits.
* **2009 recovery (+53.8% vs +67.4%; avgL 1.03, cash 10%).** Already IN at 1x on 9-Mar; 2x from mid-year and 3x as RV21
  fell below 10% in Q4. This is the lens's real strength — the best 2009 capture in the repo (incumbent +6.6%,
  vix_vrp +44.4%, baseline +7.7%) — and it comes from exactly the property that kills it in the bears: default IN, no
  vol-level gate.
* **2010 flash (−8.0% vs −8.4%; cash 55%).** VIX jump on 6-May (1.61 × base) → OUT 7-May..late June; re-entered late
  June at 1x into the 2-Jul low (ladder L1), so the rebound was captured and the crash days were not.
* **2011 (−5.0% vs −5.6%; cash 25%).** Exit at the 4-Aug close (−4.7%, VIX 1.45 × base) → OUT through 8-10 Aug; back at
  1x by late September into the 3-Oct low; the Aug-Sep chop at 1x is where the −5% came from.

## 8. Spurious re-entry census (entries to ≥2x during the two grinding bears; harness definition)

| bear | entries to ≥2x | dates | mean fwd-10-day excess | share negative | days at ≥2x |
|---|---|---|---|---|---|
| 2000-02 | 6 | 2000-08-21, 2001-02-06, 2001-06-20, 2002-01-10, 2002-01-25, 2002-04-02 | −2.32% | 83% | 9.2% |
| 2007-09 | 4 | 2007-10-09, 2008-04-30, 2008-05-15, 2008-06-02 | −1.25% | 75% | 8.7% |

These are not re-entries in the trap's sense (the book was mostly IN anyway); they are Decision B stepping to 2x when RV21
dipped below 14% inside a bear rally — and 8 of 10 were followed by losses. Compare vix_dissipation (26 and 14 entries,
77-79% negative) and the incumbent (1 and 0). The tier is the right shape (never 2x for long in a bear: 9% of days) but
even a 14% threshold is crossed at the top of bear rallies.

## 9. Event ladders (lev_target = decision at that close; return = that day's SPX %)

```
2008-10-10 Lehman capitulation : 10-07:-4.5/L0  10-08:-2.5/L0  10-09:-7.0/L0  10-10:-2.4/L0  10-13:+14.5/L0  10-14:-1.5/L0  10-15:-9.8/L0  10-16:+4.2/L0  10-17:-0.6/L0  10-20:+6.0/L0
2008-11-20 Nov-08 low          : 11-17:-1.3/L0  11-18:+1.9/L0  11-19:-6.4/L0  11-20:-7.4/L0  11-21:+5.4/L0   11-24:+6.9/L1  11-25:+0.7/L1  11-26:+3.9/L1  11-28:+1.3/L1  12-01:-8.9/L1
2009-03-09 GFC low             : 03-04:+2.4/L1  03-05:-4.1/L1  03-06:+0.2/L1  03-09:-1.2/L1  03-10:+6.0/L1   03-11:+0.7/L1  03-12:+3.9/L1  03-13:+0.8/L1  03-16:-0.3/L1  03-17:+3.1/L1
2002-10-09 bear low            : 10-04:-1.8/L1  10-07:-2.1/L1  10-08:+1.6/L1  10-09:-2.8/L1  10-10:+3.2/L1   10-11:+4.4/L1  10-14:+0.6/L1  10-15:+4.8/L1  10-16:-2.4/L1  10-17:+2.0/L1
```
Reading: OUT for the whole of Oct-2008 (good — the +14.5% and −9.8% days both missed); re-entry 24-Nov-2008 one session
after the low (good timing, 1x) but then IN at 1x through 1-Dec and the entire final leg to 9-Mar-2009 (bad: nothing in
Jan-Mar 2009 was a σ-normalised shock). Oct-2002: IN at 1x through the low and the rebound (the −2.8% 9-Oct day was
−1.5σ). The lens is at the right place at the lows because it never left; it also never left the declines.

## 10. Iteration count

Distinct parameter sets evaluated on DEV: try1 1 + gridR1 432 + gridR2 (scratch variant) 576 + r1best 1 + noexit 1 +
gridR1b 216 + gridR1c 48 + ddalt 25 (1 + 24 plateau perturbations) + final 25 (1 + 24) + memchk 1 = **1,326**.
(The harness also evaluates the same 24 perturbation sets on dev_1950 in each plateau run; those are not distinct sets.)
Two structural choices were made on DEV evidence and are disclosed: the 2-day cumulative trigger (§1a) and dropping the
exit-level re-entry variant (R2) in favour of the pre-registered SMA-dissipation re-entry.

## 11. Honest weaknesses and the regime that would break it

1. **Structural, and it is the verdict:** a default-IN state machine whose only exits are σ-normalised crash triggers
   rides grinding bears at the tier floor. 2000-02 (−54%), Oct-2007..Aug-2008 and Jan..Mar-2009 (1x throughout),
   1973-74 (1970-89 era DD −46.9%) and 1962/1966/1969-70 (1950-69 era DD −42.7%) are all sequences of −1…−2σ days
   with vol already elevated; nothing in this design can see them, and the record's own 2022 (three whole months in
   cash, Demeter +19% vs SPY −18%) is the same regime — this lens would have taken 2022 at 1x. Regime that breaks it:
   any multi-month decline of 1-2% days at 20-30 VIX.
2. **σ-normalisation goes quiet deep in a crash.** −4.5% days on a 2.3% σ are −2σ; VIX at 50 does not jump 30% above a
   45 base. The clock therefore stops being refreshed exactly when the second leg begins (Feb-Mar 2009, Jul-2002).
3. **Down-capture 131% and cash 13.5%** against the record's ≤40% and 48-52%: this is a levered-beta book with a
   crash exit, not a replica of Demeter's cash-heavy asymmetry. Up-capture 133% and 2009 +53.8% are the flip side.
4. **The DD-constrained version is worse than doing nothing.** Forcing j to 0.10 (ddalt) reaches DD −26.5% and 45%
   cash but Sharpe 0.34 (SPY 0.39), 2009 recovery +4.8%, and 1970-89 DD −49.3%: it inherits the incumbent's weakness
   without the incumbent's Sharpe. There is no j between 0.10 and 0.30 that helps (0.15 is the worst of all).
5. **Whipsaw is real but affordable:** the exit adds +0.02 Sharpe net; calm-base single-day shocks (Feb-2007, Oct-1989)
   cost ~21 sessions of 3x drift each, roughly once every two years.
6. **What would be needed to pass** — and why it is a different lens: an exit that fires on "vol rising while elevated"
   with much smaller j and real hysteresis (lens 5/6 territory), or a vol-LEVEL cash tier (lens 3/4, and ruled out by
   the record for 2020). Within this lens's own definition of a crash, the DEV answer is no.

## 12. Bugs found in shared code

None. Two observations for the coordinator, neither a bug: (i) `dev_harness.grid_search` recorded
`MemoryError((31866,), dtype('int64'))` on 1 of 48 R1c combos (k4 j.4 mo21 nd10 .09/.14); the identical parameter set
re-run singly evaluates normally (`crash_exit_dual_memchk.json`, Sharpe 0.35) — a transient of this laptop's commit
charge, and the harness's per-combo try/except handled it as designed; (ii) the grid CSV name follows the module stem plus
tag, so a scratch module in `dev_results/` writes `<module>_<tag>_grid.csv` (my R2 grid landed at
`crash_exit_dual_R2_gridR2_grid.csv`) — expected, noted so nobody looks for a missing file.

## Progress checkpoint
- [x] Mechanism written before any run.  - [x] Reference JSONs read.  - [x] Signal file written; try1; trigger form revised.
- [x] Grids R1, R2 (scratch), R1b, R1c.  - [x] Plateau chosen, DEFAULT_PARAMS frozen, final run with plateau, gate_check.
- [x] All sections complete. Verdict: built, gates NOT all passed (G3, G4 fail; G1, G2, G5, G6, G7 pass).
