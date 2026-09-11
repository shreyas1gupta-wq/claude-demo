# vix_vrp — lens 5 (variance-risk-premium) design note, pass 2

Status: COMPLETE 2026-09-10. Designer: lens-5 agent. Outcome: **`signals/vix_vrp_v2.py` goes forward (all seven gates
pass, dev_1990 Sharpe 0.6783 vs the original's 0.6084, same −19.8% maxDD); `signals/vix_vrp.py` is RETIRED** per the
pre-committed rule — the file stays on disk unchanged (rule 5), its status is the coordinator's register entry.
Scope: Part 1 = audit of the existing `signals/vix_vrp.py` (never modified). Part 2 = ablation → `vix_vrp_v2`.
Final numbers: dev_results/vix_vrp_v2.json; return object: dev_results/vix_vrp_v2_RETURN.json.

## Mechanism (written before any run)

Implied volatility is a forward-looking price; realised volatility is a backward-looking measurement. Their gap, the
variance risk premium (VRP = VIX/100 − trailing realised vol), is normally positive (options are priced above the vol
that materialises) and it collapses or inverts only while a shock is in progress — realised vol running above what
the market had priced. Two claims follow, both testable on 1990-2012 without any price-trend input:

1. **Level regimes carry different premia per unit of risk.** Calm implied vol (VIX ≲ 15) is when the equity premium
   is earned at low realised vol, so leverage compounds; elevated implied vol (VIX 16-30) is the regime of grinding
   bears and choppy corrections where the daily premium is near zero and the realised vol is 2-3x higher, so being
   levered there costs Sharpe; panic (VIX > 30) carries a large premium but at 30-55% realised vol, so it is
   harvested unlevered. Hysteresis on the level thresholds is what keeps the machine from flipping on every VIX print.
2. **The VRP is the shock detector and the re-entry trigger.** When realised vol exceeds implied by more than a
   threshold the market is moving faster than options had priced — the loss-making days of 1987/1998/2008 cluster
   here — so cash. When the VRP normalises (realised vol falls back under the still-elevated VIX) the shock has
   dissipated even though the VIX LEVEL is still high; that is the vol-dissipation signature the Demeter record
   points to (23-Mar-2020) and it is causal: both inputs are known at the close.

Why a v2 might be warranted (hypotheses to test one at a time, ablation style): (a) Demeter's calm tier is 3x, the
original uses 2x — if calm-regime Sharpe is genuinely ~0.5-0.6 at 10-12% vol, 3x should raise CAGR at a tolerable
drawdown; (b) ELEVATED = cash puts the strategy out of the market 64% of days — in the 1990s and 2003-07 bulls that
was a large opportunity cost; a 1x floor tests whether the elevated regime's premium is actually zero or merely low;
(c) a PANIC-state VRP-normalisation re-entry at 2-3x when the VIX has also fallen a set fraction from its trailing
peak (the Mar-2020 profile) — this is the ingredient most likely to be a trap in the grinding bears (crash_exit_dual
and the pass-1 trap fired 75-83% negative in 2000-02/2008), so it is judged by the spurious re-entry census first.

Pre-committed decision rule (from the task): only ONE version goes forward. v2 replaces the original only if it beats
the original's dev_1990 Sharpe with maxDD no worse than −25% and passes all seven gates; otherwise the original is
frozen unchanged and this note is the audit.

## Rules (original, unchanged — see signals/vix_vrp.py docstring)

Three-state VIX machine with shared hysteresis (CALM 2x / ELEVATED 0x / PANIC 1x) plus a VRP < vrp_min → cash filter.
Tunables (5): v_calm 15.5, v_panic 30, hyst 0.12, rv_win 10, vrp_min −0.15. Structural constants: leverage tiers
{2, 0, 1}, long-or-cash only, no price-based input.

## Part 1 — audit of the original on DEV (dev_results/vix_vrp.json, vix_vrp_audit.py, grids A/B)

**Reference numbers (harness, 3/60):** dev_1990 CAGR 10.61%, Sharpe 0.6084, monthly maxDD −19.78%, daily maxDD −28.60%,
worst month −10.74%, cash 64.3%, avg leverage 0.59 (1.65 when invested), 6.04 chg/yr, up-capture 60%, down-capture
30%, beta 0.39. 6/90: Sharpe 0.582; 2/40: 0.619. dev_1950 Sharpe 0.362 (cash before 1990). Lookahead ok at all five
cut-offs (max abs diff 0). Plateau 100% of 20 perturbations on both windows. Spurious re-entry census: zero entries
to ≥2x in both bears (the machine cannot reach 2x inside a bear — CALM requires VIX < 13.6).

**State machine occupancy 1990-2012H1:** CALM 23.1% of days (26 spells, median 28 d, max 204), ELEVATED 63.3% (58
spells, median 20 d, max 430), PANIC 13.6% (31 spells, median 7 d, max 196). The VRP filter overrode an investing
state on only **53 days in 22.5 years, all inside PANIC** (never in CALM). So the strategy is, in practice, a
VIX-LEVEL three-tier rule; the VRP is a rarely-firing panic-day filter, not the main engine.

**What the 64% cash cost and saved (1x SPX excess return on the days the model was in cash, by period):**

| period | cash days | 1x excess on all days | missed on ELEVATED-cash days | avoided on VRP-cash days |
|---|---|---|---|---|
| 1990-1994 | 57% | +17.9% | +13.4% | 0 |
| 1995-1999 | 71% | +172.3% | **+51.2%** | −6.1% |
| 2000-02 bear | 75% | −51.9% | **−52.8% (avoided)** | −3.3% |
| 2003-2007 | 47% | +88.4% | **+47.1%** | 0 |
| 2007-09 GFC | 72% | −55.7% | −30.9% (avoided) | −22.8% (avoided) |
| 2009 recovery | 59% | +67.2% | +15.7% | 0 |
| 2010-2012H1 | 83% | +28.1% | +9.7% | −3.9% |

The longest ELEVATED spells were all bull-market chop: 1996-02→1997-10 (430 d, +25.8% missed), 2003-04→2004-09
(358 d, +30.2%), 1991-01→1992-05 (337 d, +22.3%), 2010-07→2011-08 (272 d, +14.3%). The protection is the ELEVATED
cash state itself: the whole 2000-02 bear ran at VIX 20-30 and the model sat in cash for −52.8% of it. Sitting out
1995-99 and 2003-07 cost ~+50% of excess return in each bull — the price of that protection.

**2007-09 episode (model −15.7%, daily DD −28.6% from 2008-09-19 to 2009-03-09):** every invested day was the 1x
PANIC leg (99 of 356 days), and those 99 days lost −17.2% in total. The VRP filter did its job in Sep-Oct 2008
(cash on 22-Sep, 1-Oct, 14-Oct, 29-Oct after the −0.43/−0.34 VRP prints — it avoided −22.8% over 9% of the days),
but from 8-Dec-2008 the VRP was positive every day (+0.05..+0.24: realised vol fell back under a VIX of 40-55) so
the machine held 1x through the Jan-Mar-2009 grind: Jan −8.2%, Feb −10.7%, Mar-to-low −7.9% at exactly the market's
excess return. Worst days: 29-Sep-08 −7.8%, 20-Nov-08 −7.4%, 9-Oct-08 −7.0%, 19-Nov-08 −6.4% (all 1x PANIC). The
−28.6% daily DD is therefore not a leverage problem; it is the VRP-normalised 1x PANIC leg riding a grinding panic.
The same leg then took +44.4% of the +67.4% 2009 recovery (84 PANIC days at 1x, then 123 ELEVATED days at 0 — the
model never reached 2x in 2009 because VIX never fell below 13.6). Full daily table: dev_results/vix_vrp_gfc_daily.csv.

**Causality read of the code:** vix_regime is a forward loop over the VIX close with state carried from t−1 (causal);
F.realized_vol is a trailing rolling std with min_periods = window; ffill on the VIX only carries the last known
print forward; the VRP override uses same-day values; the engine shifts the target by one day. No centred windows,
no full-sample statistics, no shift(−k). Harness lookahead check: ok (max abs diff 0.0). One subtlety, disclosed in
the docstring: the VIX close is struck at 16:15 ET, 16 minutes after a 15:59 decision — ignored here as in the
literature. Second subtlety: 4 missing VIX prints are ffilled, which is causal but means those days act on stale
implied vol.

**Grid A (210 combos: v_calm {13,14,15,15.5,16,17,18} × v_panic {25,27.5,30,32.5,35,40} × hyst {.05,.08,.12,.16,.20},
rv_win/vrp_min at defaults):** Sharpe min 0.240, p10 0.378, median 0.500, p90 0.617, max 0.728. Share > 0.425: 75%;
> 0.50: **49.5%**; > 0.55: **28.6%**; > 0.60: 17%. 75% of cells pass the gate proxy (Sharpe/DD/turnover/era). Cliffs:
v_panic ≥ 35 (marginal mean 0.43, only 20% of cells > 0.5 — the PANIC 1x leg is a large part of the Sharpe: with
PANIC set to cash the whole model drops to 0.27); v_calm 18 (mean 0.42, 3% of cells > 0.5); hyst 0.05 (mean 0.47,
9.5 chg/yr). Ridge: v_panic 30 (mean 0.579, 80% of cells > 0.5) with v_calm 13-15. The base point (15.5/30/0.12) at
0.608 sits on that ridge, near the p90 of its own neighbourhood: a plateau in the hysteresis and calm-threshold
directions but a ridge in v_panic (25-32.5 fine, 35+ not).

**Grid B (225 combos: rv_win {5,7,10,15,21} × vrp_min {−.25,−.20,−.15,−.10,−.05} × hyst {.08,.12,.16} × v_calm
{14,15.5,17}):** median 0.494, share > 0.5: 45%, > 0.55: 23%. rv_win = 5 is a cliff (mean 0.374, avg maxDD −36%: a
5-day realised vol is so noisy that the VRP filter whipsaws in and out of the PANIC leg); rv_win 10-21 is flat
(0.52). vrp_min is flat across −0.25..−0.05 (0.47-0.51) — it barely matters, consistent with the filter firing 53
days in 22 years. v_calm 17 is worse (0.435) everywhere.

**Audit verdict:** 0.61 is a genuine plateau in hyst/v_calm/rv_win(≥7)/vrp_min, with two cliffs the single-parameter
test does not flag because ±30% stays inside the safe region: v_panic above ~33 and rv_win at 5. The Sharpe comes
from two legs — 2x CALM in the low-VIX bulls and 1x PANIC in the post-shock rebounds — while the ELEVATED cash state
is what protects the bears at the cost of ~half the 1990s and 2003-07 bull excess return. The VRP filter is not the
engine; the VIX-level machine is (the record says level gating is what Demeter did NOT do — an honest weakness).

## Part 2 — ablation (dev_results/vix_vrp_v2_ablate.py; 3/60; dev_1990 unless stated)

Round 1, one structural change at a time on the frozen original (all census counts are entries to ≥2x in the bear):

| variant | Sharpe | CAGR | maxDD | worst M | chg/yr | cash | 1990s CAGR | 2000-02 bear | GFC | 2009 rec | census 2000-02 / 2008 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V0 original 2/0/1 | 0.608 | 10.6 | −19.8 | −10.7 | 6.0 | 64 | 14.6 | +15.1 | −15.7 | +44.4 | 0 / 0 |
| V1 CALM 3x | 0.547 | 11.3 | −27.8 | −15.5 | 6.0 | 64 | 16.6 | +15.1 | −15.7 | +44.4 | 0 / 0 |
| V2 ELEVATED 1x floor | 0.524 | 11.1 | **−42.8** | −14.1 | 3.7 | 1 | 20.9 | **−43.9** | −41.6 | +67.4 | 0 / 0 |
| V3 CALM 3x + ELEV 1x | 0.510 | 11.8 | −42.8 | −14.1 | 3.7 | 1 | 23.0 | −43.9 | −41.6 | +67.4 | 0 / 0 |
| V2b ELEV 1x if VRP > 0.03 | 0.561 | 11.1 | −32.7 | −14.1 | 22.3 | 20 | 18.5 | −26.9 | −37.8 | +53.3 | 0 / 0 |
| V2c ELEV 1x if VRP > 0.06 | 0.647 | 12.1 | −20.0 | −13.8 | 24.8 | 38 | 16.0 | −2.7 | −22.7 | +54.9 | 0 / 0 |
| V2d ELEV 1x if VRP > 0.09 | **0.684** | 12.0 | −19.8 | −10.7 | 20.1 | 54 | 15.3 | +4.4 | −12.0 | +53.6 | 0 / 0 |
| V0b PANIC 0x | 0.271 | 5.5 | −18.9 | −10.5 | 2.3 | 77 | 9.8 | +9.7 | +2.2 | +0.1 | 0 / 0 |
| V0c PANIC 2x | 0.607 | 14.2 | −41.9 | −21.1 | 6.0 | 64 | 18.9 | +13.0 | −38.2 | +101.6 | 8 (38% neg) / 9 (56% neg) |
| V4 PANIC burst 2x, VIX ≤ 0.75×30d-max & VRP normal | 0.466 | 9.2 | −32.4 | −19.6 | 9.2 | 64 | 15.0 | +9.8 | −29.0 | +40.1 | 5 (40% neg) / **5 (80% neg, −3.3% mean)** |
| V4 burst 2x at 0.80 / 0.70 / 0.65 off peak | 0.445 / 0.478 / 0.526 | | −43.8 / −30.7 / −26.4 | | | | | | −41.0 / −27.2 / −22.6 | | 2008: 89% / 100% / 50% neg |
| V4 burst 3x (0.80..0.65 off peak) | 0.316-0.433 | | −61.9..−32.9 | −35..−21 | | | | | −59.8..−29.5 | | same entries, 3x the damage |
| V4b burst 2x, 60-day peak | 0.462 | 9.7 | −39.7 | −24.0 | 9.1 | | | | −39.6 | +61.9 | 5 (20% neg) / 3 (67% neg) |
| V4c burst 2x, 15-day peak | 0.557 | 10.0 | −24.6 | −10.7 | 8.0 | | | | −20.8 | +38.0 | 3 (33%) / 4 (50%) |
| V6 CALM 3x + burst 2x | 0.447 | 9.9 | −32.4 | −19.6 | 9.2 | | 17.0 | | −29.0 | +40.1 | 5 / 5 (80% neg) |

Readings. (a) **3x CALM is not supported on DEV**: Sharpe falls 0.61 → 0.55 and the worst month goes −10.7 → −15.5%
(the calm-regime Sharpe is not high enough to survive the 3x variance drag on the −3% days that occur inside CALM).
(b) **An unconditional 1x ELEVATED floor is ruinous** exactly where the original earns its keep: 2000-02 −43.9% (the
bear was an ELEVATED-state event) and GFC −41.6%; it does add +6 pts of CAGR in the 1990s and takes all of the 2009
recovery, which quantifies what cash-by-default costs (1990s CAGR 14.6 → 20.9; 2003-07 recovery +23 → +45). (c) The
**VRP-gated ELEVATED floor** (1x only when implied vol exceeds realised by more than a threshold — the variance risk
premium is rich) keeps the bear protection while recovering part of the bull cost: at VRP > 0.09, Sharpe 0.684 with
the SAME −19.8% maxDD, bear +4.4%, GFC −12.0%, 2009 +53.6%; but it trades 20/yr and the threshold has only been
scanned coarsely. (d) **Every PANIC-state dissipation burst is a trap on DEV**, as pre-warned: entries to 2x in 2008
were 50-100% negative over the next 10 days at every peak-fraction tested, maxDD worsens to −26..−44%, Sharpe falls
0.13-0.16. The PANIC leg is right at 1x (setting it to 0 halves the Sharpe; 2x doubles the drawdown). Burst re-entry
is rejected for v2. (e) The V4c 15-day-peak variant is the least bad burst but still below the original.

Decision after round 1: the only v2 candidate change is (c). Round 2 scans the VRP-gate threshold and three turnover
reducers (hysteresis band on the gate, 5-day smoothed VRP, 5-day minimum hold), then a harness grid on the v2 file.

Round 2 (16 variants; ELEVATED 1x when VRP > a; maxDD is −19.8% in every one of them — the drawdown is the GFC PANIC
leg, untouched by this change):

| gate form | a=0.07 | 0.08 | 0.09 | 0.10 | 0.11 | 0.12 | 0.14 | 0.16 | 0.20 |
|---|---|---|---|---|---|---|---|---|---|
| raw VRP > a: Sharpe | 0.700 | 0.597 | 0.684 | 0.713 | 0.662 | 0.678 | 0.611 | 0.611 | 0.608 |
| raw: chg/yr | 24.0 | 21.9 | 20.1 | 16.7 | 13.7 | 10.6 | 7.3 | 6.4 | 6.0 |
| raw: 2000-02 bear | −8.1 | −1.7 | +4.4 | +11.3 | +12.1 | +12.9 | +15.8 | +15.1 | +15.1 |
| raw: GFC | −15.3 | −14.3 | −12.0 | −11.3 | −10.2 | −9.5 | −15.7 | −15.7 | −15.7 |
| hysteresis band 0.03: Sharpe | | 0.595 | | 0.690 | | 0.652 | | | |
| 5-day smoothed VRP: Sharpe | | 0.695 | | 0.594 | | 0.626 | | | |
| 5-day min hold: Sharpe | | | | **0.756** (13.5 chg/yr, bear +19.9, GFC −16.6, 2009 +56.4) | | | | | |

Reading: the gate helps on average (raw 0.07-0.12 mean 0.672 vs 0.608) but the raw surface is jagged — adjacent
one-vol-point thresholds swing Sharpe by up to 0.12 (0.08 → 0.597, 0.10 → 0.713) — the signature of a daily gate that
flips on single realised-vol prints. Above a = 0.14 the gate rarely opens and the rule converges to the original.
Round 3 maps threshold × gate-form before any structural form is chosen (the map, not a point, decides).

Round 3 — threshold × gate-form map (42 cells, dev_results/vix_vrp_v2_map.csv; dev_1990 Sharpe; maxDD −19.8% in
every cell except hold5/hold10 at a ≤ 0.08, −21..−25%):

| a | raw | hold3 | hold5 | hold10 | smooth10 | hyst band .03 |
|---|---|---|---|---|---|---|
| 0.07 | 0.700 | 0.634 | 0.584 | 0.565 | 0.702 | 0.601 |
| 0.08 | 0.597 | 0.626 | 0.561 | 0.567 | 0.648 | 0.595 |
| 0.09 | 0.684 | 0.721 | 0.618 | 0.617 | 0.581 | 0.682 |
| 0.10 | 0.713 | 0.766 | 0.756 | 0.739 | 0.588 | 0.690 |
| 0.11 | 0.662 | 0.681 | 0.629 | 0.642 | 0.599 | 0.643 |
| 0.12 | 0.678 | 0.655 | 0.683 | 0.667 | 0.620 | 0.652 |
| 0.13 | 0.632 | 0.578 | 0.608 | 0.598 | 0.601 | 0.630 |
| column mean / min | 0.667 / 0.597 | 0.666 / 0.578 | 0.634 / 0.561 | 0.628 / 0.565 | 0.620 / 0.581 | 0.642 / 0.595 |

2000-02 bear (raw): −8.1, −1.7, +4.4, +11.3, +12.1, +12.9, +12.5 for a = 0.07..0.13; GFC (raw): −15.3, −14.3, −12.0,
−11.3, −10.2, −9.5, −13.0; chg/yr (raw): 24.0, 21.9, 20.1, 16.7, 13.7, 10.6, 8.9. The min-hold / smoothing / band
forms lower the mean Sharpe and make the bear and GFC worse (they keep the 1x on after the VRP has already thinned),
so the raw gate — no extra constant — is the structural choice. The whole 42-cell map is between 0.56 and 0.77
(mean 0.64) against the original's 0.608, i.e. the gate is an improvement on average, but its lower edge is below the
original, so the threshold must be chosen from the flat region a = 0.10-0.13 (raw 0.63-0.71, bear +11..+13, GFC
−9.5..−13), not from the 0.07-0.09 region where the bear goes negative.

**Structural decision for v2:** ELEVATED = 1x when VRP > vrp_elev (raw), else cash; everything else as the original;
sixth tunable vrp_elev. Built as signals/vix_vrp_v2.py; harness grids C (vrp_elev × v_calm × hyst × v_panic, 216)
and D (rv_win × vrp_elev × vrp_min, 72) decide the default from the plateau.

## Grid summary — v2 (harness grids, 3/60, dev_1990)

**Grid C (216 combos: vrp_elev {.09,.10,.11,.12,.13,.14} × v_calm {14,15,15.5,16} × hyst {.08,.12,.16} × v_panic
{27.5,30,32.5}; rv_win 10, vrp_min −0.15):** Sharpe min 0.461, p10 0.532, median **0.630**, p90 0.718, max 0.812.
Share > 0.425: 100%; > 0.50: **96.8%**; > 0.55: **85.2%**; > 0.60: 64.4%. maxDD better than −25% in 91.7% of cells;
gate proxy (Sharpe/DD/turnover/eras) passes in 97.7%. For comparison the original's regime grid (A) had median 0.500
and 49.5% of cells above 0.5 — the whole v2 surface sits above the original's, which is the evidence that the gate is
an average improvement and not a peak. Marginals: vrp_elev 0.09 → 0.659, **0.10 → 0.683**, 0.11 → 0.626, 0.12 →
0.626, 0.13 → 0.592, 0.14 → 0.575 (avg chg/yr 20.3, 16.8, 14.0, 10.7, 9.1, 7.6); v_calm 14/15/15.5/16 → 0.620/
0.679/0.624/0.585; hyst flat (0.62-0.63); v_panic 27.5/30/32.5 → 0.599/0.655/0.628. Cliffs (worst cells 0.46-0.50):
v_calm 16 with hyst 0.08 (maxDD −28..−30%) and vrp_elev ≥ 0.13 with v_calm 14/hyst 0.16 — the same two edges as
the original's grid, unchanged by the gate.

**Grid D (72 combos: rv_win {7,10,15,21} × vrp_elev {.09..0.14} × vrp_min {−.20,−.15,−.10}; other params default):**
median 0.578, > 0.5: 90%, > 0.55: 72%. rv_win 10 → 0.648 (all cells > 0.585), 21 → 0.611, 7 → 0.551, 15 → 0.534
(a dip: a 15-day RV makes the gate flip at different dates in 2000-02 and gives maxDD −27.6% with vrp_min −0.20);
vrp_min flat (0.57-0.60). rv_win 10 is kept (inherited and the flattest row).

**Choice of default:** vrp_elev = **0.12**, all five inherited parameters unchanged (15.5 / 30 / 0.12 / 10 / −0.15).
0.11-0.12 is a flat shelf (identical marginal means) between the 0.10 peak and the 0.13-0.14 decline, it has lower
turnover (10.6 vs 16.7 chg/yr), a better 2000-02 (+12.9 vs +11.3) and GFC (−9.5 vs −11.3), and if the effect is weaker
out of sample the rule degrades toward the original rather than toward the trap region. The inherited parameters were
NOT moved even though both grids say v_calm 15 is slightly better than 15.5 — v2 differs from the original in exactly
one rule so the comparison stays clean (that leftover is disclosed, not harvested).

## Rules (v2 — signals/vix_vrp_v2.py)

1. VIX three-state machine with shared hysteresis: CALM (enter VIX < v_calm·(1−hyst) = 13.64, leave > 15.5) → 2x;
   PANIC (enter VIX > 30, leave < 26.4) → 1x; ELEVATED = in between and the start state.
2. VRP = VIX/100 − RV(rv_win = 10). VRP < vrp_min (−0.15) → cash in every state; inside PANIC this is the re-entry rule.
3. NEW: ELEVATED → 1x when VRP > vrp_elev (0.12), else cash.
4. Long or cash, leverage ∈ {0, 1, 2}; no price input. Structural constants named in the docstring (tiers 2/1/1, raw
   gate form, RV estimator, VIX ffill).

## Parameters and how each was chosen

| param | default | window | grid ranges seen | why this point |
|---|---|---|---|---|
| v_calm | 15.5 | 1990-2012H1 | 13-18 (A), 14-17 (B), 14-16 (C) | inherited; flat 13-16, cliff at 18; 15 is marginally better in A and C but not moved (one rule change only) |
| v_panic | 30 | same | 25-40 (A), 27.5-32.5 (C) | inherited; the ridge — 25-32.5 fine, ≥35 collapses (mean 0.43) |
| hyst | 0.12 | same | 0.05-0.20 (A,B), 0.08-0.16 (C) | inherited; flat 0.08-0.20, 0.05 whipsaws (9.5 chg/yr) |
| rv_win | 10 | same | 5-21 (B), 7-21 (D) | inherited; 5 is a cliff (DD −36%), 10 the flattest row in D; 12-15 weaker (see weaknesses) |
| vrp_min | −0.15 | same | −0.25..−0.05 (B, D) | inherited; flat everywhere (the filter fires 53 days in 22 years) |
| vrp_elev | 0.12 | same | 0.07-0.13 (map), 0.09-0.14 (C, D) | centre of the 0.11-0.12 shelf; ≤0.09 turns the 2000-02 bear negative, ≥0.13 converges to the original |

## Gate results (python gate_check.py dev_results/vix_vrp_v2.json)

```
vix_vrp_v2: ALL GATES PASS
  G1_causality: pass  value=0.0
  G2_dev1990_sharpe: pass  value=0.6782706498277302 (bar 0.425)
  G3_dev1990_maxdd: pass  value=-19.77825374927784 (bar -30.0)
  G4_no_ruinous_era: pass
      1950-1969: N/A (all cash — signal not available in this era)
      1970-1989: N/A (all cash — signal not available in this era)
      1990-1999: ok: CAGR 15.29% maxDD -18.9%
      2000-2012H1: ok: CAGR 8.93% maxDD -19.8%
  G5_changes_per_year: pass  value=10.574047954866007 (bar 25.0)
  G6_plateau: pass  value=0.9583333333333334 (bar 0.5)
  G7_param_budget: pass  value=6 (bar 6)
```

Final harness (3/60) dev_1990: CAGR 11.71%, Sharpe 0.6783, monthly maxDD −19.78%, daily maxDD −28.60%, worst month
−10.74%, cash 61.9%, avg leverage 0.61 (1.61 invested), 10.57 chg/yr, up-capture 64%, down-capture 30%, beta 0.42,
cost drag 0.39%/yr. 6/90: Sharpe 0.642 (CAGR 11.21%); 2/40: 0.692. dev_1950: Sharpe 0.403 (cash before 1990; the
1950-89 numbers are the T-bill). Original at the same costs: 0.608 / 0.582 / 0.619. Plateau: 23 of 24 dev_1990
perturbations within 25% (the one failure: rv_win 12 → 0.505 against a 0.509 floor); 23/24 on dev_1950 too.
Leverage distribution 1990-2012H1: 0x 61.9%, 1x 15.0%, 2x 23.1%. Lookahead ok (max abs diff 0) at all five cut-offs.

**T-bill asymmetry disclosure:** 62% cash days earn the T-bill in the engine; over 1990-2012 that is roughly 2%/yr of
the 11.7% CAGR (Demeter books cash at 0%). The comparison column with the T-bill zeroed is the coordinator's step.

## Stress narrative (v2; original in brackets where different)

* **1987:** no VIX, all cash: +2.2% (T-bill) vs SPY −25.0%. The rule does not exist before 1990.
* **1990 Kuwait:** +4.2% [+5.1%] vs −8.6%; 41% cash, 13 changes. The new ELEVATED leg's worst day is here (−3.03% on
  6-Aug-1990: a rich VRP the day before the invasion sell-off) — a reminder that a rich VRP is not a shock guard.
* **1998 LTCM:** +24.0% [+16.7%] vs +4.9%. PANIC 1x through both lows (ladder: 1x on 31-Aug and 8-Oct, the VRP filter
  took it to cash only on 8/9-Sep after the −7.1% day pushed RV10 above the VIX); the gate added quiet-day 1x in the
  Jul and Nov-Dec ELEVATED spells.
* **2000-02 bear:** +12.9% [+15.1%] vs −47.2%; 74% cash, avg leverage 0.26. The bear was an ELEVATED-state event (VIX
  20-30, realised 20-25%, VRP thin) so the gate opened on only 11 days (−1.6%); the −18.9% DD is the 1x PANIC legs of
  Sep-2001 and Jul-2002 (the four −3% days into the 23-Jul-2002 low at 1x). The model held 1x at the Oct-2002 low and
  took the +3.2/+4.4/+4.8% rebound days.
* **2002-03 recovery:** +28.1% [+23.1%] vs +45.5%: 1x PANIC into early 2003, then ELEVATED cash; 2x only from 2004.
* **2007-09 GFC:** −9.5% [−15.7%] vs −54.8%, daily DD −28.6% (unchanged, 19-Sep-2008 → 9-Mar-2009). The PANIC path
  is identical to the original (VRP filter to cash on 22-Sep, 1-Oct, 14-Oct, 29-Oct-2008; 1x otherwise; Jan-Mar 2009 at
  1x with VRP +0.05..+0.24 → −8.2/−10.7/−7.9%). The improvement is five ELEVATED gate days in the 2008 relief phases
  (+7.5%).
* **2009 recovery:** +43.6% [+44.4%] vs +67.4%: 1x PANIC Mar-Jun (84 days), then ELEVATED with the gate open 18 days
  (−0.2%); never 2x because VIX never fell below 13.6 in 2009 — the model takes ~two-thirds of the rebound at 1x and
  misses the rest, the known cost of a level machine.
* **2010 flash:** +5.4% [+5.0%] vs −8.4%; **2011 debt:** +15.4% [same] vs −5.6% — 1x PANIC from 4-Aug through the
  3-Oct low and its rebound, cash on the −4.4% 10-Aug VRP day.

## Spurious re-entry census

Zero entries to ≥2x in both 2000-02 and 2007-09 (0.0% of days at ≥2x in either): the machine cannot reach 2x inside a
bear because CALM requires VIX < 13.64, and v2 adds only a 1x leg. The census was the deciding test for the rejected
PANIC-burst variants: at every peak-fraction (0.65-0.80 of the 30-day VIX max) the 2008 entries to 2x were 50-100%
negative over the next 10 sessions (mean −2.8..−3.4%), 2000-02 entries 36-67% negative; with a 15-day peak window 4
entries at 50%/+0.3% — still no better than the original. Same conclusion as crash_exit_dual and the pass-1 trap.

## Event ladders (date: SPX ret / VIX / target leverage decided at that close; identical to the original on these dates)

* **2008-10-10 Lehman capitulation:** 10-07 −4.5/53.7/1 · 10-08 −2.5/57.5/1 · 10-09 −7.0/63.9/1 · **10-10 −2.4/70.0/1**
  · 10-13 +14.5/55.0/0 · 10-14 −1.5/55.1/0 · 10-15 −9.8/69.2/0 · 10-16 +4.2/67.6/0 · 10-17 −0.6/70.3/0 · 10-20 +6.0/53.0/0.
  Held 1x into the low and through the +14.5% day, then the VRP filter (RV10 > VIX+15) took it to cash for the
  −9.8% 15-Oct day — and also for the +6.0% 20-Oct.
* **2008-11-20 Nov-08 low:** 11-17 −1.3/69.2/1 · 11-18 +1.9/67.6/1 · 11-19 −6.4/74.3/1 · **11-20 −7.4/80.9/1** · 11-21
  +5.4/72.7/1 · 11-24 +6.9/64.7/0 · 11-25 +0.7/60.9/0 · 11-26 +3.9/54.9/0 · 11-28 +1.3/55.8/0 · 12-01 −8.9/68.5/0.
  1x through the two −6/−7% days and the first +5.4% rebound, cash from 25-Nov (VRP −0.22) — missed +6.9/+3.9 but
  also the −8.9% 1-Dec.
* **2009-03-09 GFC low:** 03-04 +2.4/47.6/1 · 03-05 −4.1/50.2/1 · 03-06 +0.2/49.3/1 · **03-09 −1.2/49.7/1** · 03-10
  +6.0/44.4/1 · 03-11 +0.7/43.6/1 · 03-12 +3.9/41.2/1 · 03-13 +0.8/42.4/1 · 03-16 −0.3/43.7/1 · 03-17 +3.1/40.8/1.
  Steady 1x: no exit before the low, no re-lever after it. The rebound is captured at 1x only.
* **2002-10-09 bear low:** 10-04 −1.8/39.5/1 · 10-07 −2.1/42.6/1 · 10-08 +1.6/41.0/1 · **10-09 −2.8/42.1/1** · 10-10
  +3.2/37.5/1 · 10-11 +4.4/35.7/1 · 10-14 +0.6/36.0/1 · 10-15 +4.8/34.0/1 · 10-16 −2.4/36.0/1 · 10-17 +2.0/34.1/1.
  Same profile: 1x through the low and the first week of the rebound.

## Iteration count

796 distinct parameter sets evaluated on DEV (each grid combination counted): grid A 210 + grid B 225 (audit of the
original), ablation round 1 = 21 variants, round 2 = 16, round 3 map = 42 cells (35 new), grid C 216 + grid D 72 (v2),
final harness run 1. In runs: 4 grids + 3 ablation scripts + 1 final harness = 8 DEV runs; no OOS access of any kind.
The harness's own 48 plateau perturbations (24 per window) are not counted as design iterations.

## Honest weaknesses and the regime that would break it

1. **The gain over the original is a thin leg.** At vrp_elev 0.12 the new ELEVATED 1x is open on 132 of ~5,670 days
   (2.3%; the gate is open on 3.7% of ELEVATED days), in spells of ~2-3 days, ~2.3 entries a year. Those days earned
   +19.8 bp/day at 18.5% annualised vol (leg t-stat ≈ 1.9; positive in 5 of 7 sub-periods, negative in 1990-94, the
   2000-02 bear and 2009). +0.07 of Sharpe from 132 days is exactly the kind of improvement that can evaporate out of
   sample. What supports it: the whole 216-cell grid C surface sits above the original's grid A surface (median 0.63
   vs 0.50), the mechanism is a published one (a rich VRP predicts returns), and the rule degrades toward the original,
   not toward a trap, if the effect is absent.
2. **It does not fix cash-by-default.** The gate recovered +11.8% of the +51% excess missed in 1995-99 and +7.3% of the
   +47% missed in 2003-07; cash is still 62% of days (record target 48-52%), up-capture 64% (target ≥ 100%). Lower
   thresholds (0.07-0.09) open the gate on 40-54% of days but turn the 2000-02 bear negative (−8..+4%).
3. **Realised-vol-window sensitivity.** rv_win 12 → Sharpe 0.505 (the failed plateau row), rv_win 15 averages 0.53 in
   grid D with maxDD −27.6% at vrp_min −0.20: both the crash filter and the new gate flip on a 10-day RV, and a
   different window moves a handful of decisive days in 2000-02 and 2008. 10 and 21 are the good rows; 12-15 is not.
4. **Still a VIX-LEVEL machine**, which the record says Demeter is not: no 2x/3x in post-crash rebounds (2009 at 1x,
   ~65% of SPY), no crash exit faster than the VRP filter (which needs RV10 > VIX + 15 — one −7% day), and the
   original's −28.6% daily drawdown is untouched: the 1x PANIC leg rode Jan-Mar 2009 down −27% with a positive VRP.
   **The regime that breaks it:** a prolonged panic that grinds lower while realised vol normalises (Jan-Mar 2009 again,
   or 1x through a 2022-style slow bear if VIX sits above 30), or a multi-year bull with VIX pinned at 16-30 and
   realised vol close to implied (1996-97 chop, 2010-11), which the machine sits out almost entirely at ~0.2x.
5. **Turnover doubled** (6.0 → 10.6 chg/yr): the 6/90 cost row costs 0.036 of Sharpe (0.678 → 0.642) versus 0.026 for
   the original.
6. **1950-1989 is not evaluated** (no VIX): the dev_1950 Sharpe of 0.40 is 62% T-bill. Any claim about the rule's
   behaviour in 1962, 1973-74 or 1987 is untested.

## Bugs found in shared code

None. Two observations, not bugs: (i) `dev_harness.plateau` rounds integer parameters, so rv_win ±15% = 8/12 and
±30% = 7/13 — the test is coarser for small integer windows than for floats; (ii) `gate_check` G4 treats an era with
> 99% cash as N/A, so a VIX-only rule's 1950-1989 eras are neither a pass nor a fail (correct, but worth stating when
comparing with non-VIX candidates).

## Files

signals/vix_vrp_v2.py · dev_results/vix_vrp_v2.json (final, with plateau) · dev_results/vix_vrp_v2_gridC_grid.csv,
vix_vrp_v2_gridD_grid.csv (+ _spec.json, .log) · dev_results/vix_vrp_gridA_grid.csv, vix_vrp_gridB_grid.csv (audit
grids of the original) · dev_results/vix_vrp_audit.py, vix_vrp_gfc_daily.csv · dev_results/vix_vrp_v2_ablate.py,
vix_vrp_v2_ablation_all.csv, vix_vrp_v2_ablation_round2.csv, vix_vrp_v2_map.py, vix_vrp_v2_map.csv ·
dev_results/vix_vrp_v2_diag.py · dev_results/vix_vrp_gridsum.py, vix_vrp_print.py · dev_results/vix_vrp_v2_return.py,
vix_vrp_v2_RETURN.json. signals/vix_vrp.py and dev_results/vix_vrp.json untouched.
