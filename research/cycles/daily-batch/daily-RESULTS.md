# The first daily-resolution batch — results and honest read
Written AFTER the prints (2026-09-02). Pre-registration: ledger CW-D1a/DW1/F1a/F2a.
Script: scripts/analyze_nifty_daily.py. Data: vaulted NIFTY 50 daily mirror
(2007-09-18..2026-04-13, n=4,553 returns; authentication 6/6).

## The prints
1. CW-D1a: budget-day-only |return| median 1.14% vs 0.59% all other days; MW one-sided
   p=0.110 — FAIL on the partial registration's bar. The ORIGINAL CW-D1 window (±1 day,
   registered 2026-09-02 before any daily data existed): median 0.95% vs 0.59%, p=0.0049 —
   PASS on that leg's bar. VIX leg still data-gated.
2. DW1: Kruskal-Wallis across weekdays H=2.83, p=0.587 — the 5.5 REJECT confirmed with
   evidence. Monday prints the HIGHEST median (+0.10%) — the opposite sign of the classic
   US weekend effect, and un-interpreted per the pre-stated rule.
3. F1a: two-leg composite tau_half ≈ 61 trading days ≈ 2.9 months — inside the ladder's
   registered [1,3] months, near the top. The block-bootstrap CI is documented as
   UNRELIABLE for this persistence (blocks ~ half-life); no CI is claimed.
4. F2a: 7/11 pre-named episodes detected at state ≥ 0.3 — FAIL against the ≥8/11 bar.
   False fires: 2.6% of valid days (measurement, no bar).

## Honest read
- **The resolution theorem's positive leg landed.** CW1 (monthly) showed February ordinary;
  the daily ±1-window print shows budget windows carry ~60% higher |returns| (p=0.005).
  Same phenomenon, two resolutions, both now measured — the L5 seat's vol-scheduling claim
  finally rests on OUR print, not only the literature. The day-only cut fails at n=19;
  nothing is promoted beyond what L5 already does (reduce-only scheduling, unchanged).
- **A process error is on the record:** the partial registration transposed the original
  CW-D1 window (day-only vs ±1). Caught at the honest-read stage because the original
  registration was written down first. Neither bar moved; both prints stand; the
  verification-log gets the note. The lesson: a PARTIAL run must quote its parent design
  verbatim, never paraphrase it.
- **F2a's fail is worth more than a pass.** The four misses decompose into: one
  untestable (warm-up NaN — a registration that failed to anticipate coverage), two
  design-consistent (2013 lived on the absent funding leg — direct evidence FOR the
  three-leg architecture and FS-D2's taxonomy; demonetization never moved the index), and
  one genuine discovery — **the 2008 shadow**: once a mega-crisis enters the expanding
  history, a Feb-2018-size vol event ranks low and the state stays cold. Expanding
  percentiles buy no-look-ahead at the price of post-crisis de-sensitization. This is now
  a measured property of the whole ladder's percentile machinery, and the F2 full design
  must sweep window-capped percentile variants (e.g., trailing-10y) against expanding —
  registered as F2b below.
- **F1a agrees with the ladder.** ~2.9 months sits inside the registered tau_half [1,3]m —
  the first real-data corroboration of L2's placement on the ladder (near the slow end of
  the fast band, consistent with a 21d RV window + drawdown leg).

## New registration (bars before data, as always)
- **F2b (percentile-memory sweep):** at the full F2 run, detection/false-fire tables for
  expanding vs trailing-{5y, 10y} percentile variants across the same episode set and
  threshold grid; adjudication stays episode-DD-improvement NET of costs (F2's original
  currency), never raw detection counts. Prior stated: trailing windows re-sensitize at
  the cost of earlier false fires; the desk expects a trade, not a free lunch.

---
# Addendum (same day): CR-D2a — the comomentum calibration
Prints: 108 months (2013-2021); lag-1 AC 0.65 (P1 PASS — the monitor is a state, not
noise); the 2018-accumulation shape prior FAILED — late-2017 comomentum was the SAMPLE'S
LOWEST (2017 annual mean 0.041 vs median 0.090), and the series instead peaks in Jun-2020
(the stress-correlation regime). Two dissections, both honest and both routed to the full
CR-D2 (PIT + FF-residualized): India's 2018 smallcap unwind may simply not have been a
momentum-crowding event — making this the THIRD independent print where the imported
factor-crowding narrative fails to appear in Indian data (CR1a: no negative WML skew;
CR2: the 2025 "quant unwind" invisible; CR-D2a: no 2017-18 comomentum build) — and/or the
simplified market-adjustment (not full residualization) lets the market-wide correlation
regime contaminate the measure, as the 2020 peak suggests. Either way the machinery now
exists, the bars were not moved, and the crowding candidate's monitors are calibrated
against their first real prints.

---
# Addendum 2 (same day): F2-index — the de-risk grid's first real-data pass
Prints (script analyze_f2_index.py; buy-hold CAGR 9.4% over 2007-2026): the pre-named
deep-episode set resolved to {GFC*, COVID} (EU-2011's in-window buy-hold DD fell short of
the 20% gate). 3 of 18 cells SUPPORTIVE, all sharing trigger 0.80 + 1-of-2 confirm:
- phaseD re-entry: +8.4pp mean deep-episode DD improvement at 0.56pp/yr drag (19 fires,
  16% of days cut) — the best cell, and INADMISSIBLE for adoption until F7 passes (phase-D
  is display-only by registration). Its dominance is the strongest case yet for running F7.
- calendar re-entry: +5.6pp at 1.23pp/yr — the best ADOPTABLE cell.
- decay re-entry: +5.6pp at 1.83pp/yr — clears the bar with the least headroom.
Architecture lessons, both pre-readable from the design and now measured: (i) requiring
2-of-2 confirmation destroys protection everywhere (the drawdown leg lags realized vol —
the ladder's "any one arms, two confirm" asymmetry is vindicated); (ii) triggers above the
0.80 percentile fire too late for a COVID-speed crash. Three high-trigger phaseD cells
printed NEGATIVE drag (de-risking that ADDED return) with sub-bar protection — logged and
not promoted (that is a timing-alpha claim this design does not adjudicate).
Caveats carried: GFC partially inside the percentile warm-up; n(deep)=2; single-path
in-sample; index proxy with flat 28bp costs. NONE of this arms R4 — the shortlist
{0.80, 1of2} x {calendar, decay} goes to the full F2 (three legs, book costs, M4
walk-forward), which this run makes cheaper by 15 cells.

---
# Addendum 3 (same day): F7a — the phase-direction test fails, and clarifies everything
At matched high stress (state pctile >= 0.8), falling-from-high days offer NO forward-return
advantage over rising days (63bd medians +5.62% vs +5.67%, MW p=0.653; n=18/34 at 21bd
spacing). Per F7's frozen decision rule, phase stays display-only for L2. The valuable part
is the reconciliation with F2-index's grid, where the phaseD re-entry family DOMINATED:
that dominance was earliness — being back in the market sooner during V-shaped recoveries —
not direction information, because BOTH directions at high state carry ~+5.5%/63bd forward
returns (the Daniel-Moskowitz panic-state rebound, level-driven). Doctrine gains a sibling:
**levels, not directions** — the stress LEVEL prices the rebound; the phase arrow adds
nothing measurable at this resolution. Consequence registered as F2c: the full F2 grid adds
a direction-free calendar-21bd re-entry variant expected to match phaseD's numbers without
any F7 dependence. The 2026-09-01 phase directive survives as DISPLAY machinery (trails on
every state), and its one traded ambition just got its honest answer from its own
pre-registered gate.

---
# Addendum 4 (same day): TS1 — the L4 calibration, and a prior inverted
NIFTY (2007-2026, monthly, 28bp/switch): only the 3-month rule passes its DD-shaped bar
(maxDD 22% vs 47% buy-hold, drag 1.1pp/yr — and its window INCLUDES 2008). The 6m and 12m
rules fail on drag (3.4/5.8pp/yr), and 12m prints a WORSE drawdown than its own-window
buy-hold (32% vs 29%). Two honesty notes: (i) the pre-stated prior ("12m passes via the
2008 exit; 3m whipsaws hardest") was INVERTED by the print — except that the k=12 valid
window begins 2009 after its warm-up, so the 2008-exit half of the prior was untestable
in-window rather than refuted; the comparability limit across k is recorded; (ii) each cell
was barred against its OWN valid-window buy-hold, so the per-cell verdicts stand.
Gold (float era, 654 months, 10bp [A]): all three lookbacks pass, 12m strongest — net CAGR
ABOVE buy-hold (+9.0% vs +8.0%) with maxDD 34% vs 62%. The gold-tilt leg of L4 is now
calibrated on 54 years of vaulted data.
The through-line with F2-index: on Indian equity at monthly cadence, SPEED is where
drawdown control lives — the fast lookback exits crashes the slow ones ride. This is the
CONTRACT's own prior ("shorter lookbacks have higher confidence") arriving as measurement.

---
# Addendum 5 (same day): N4a — the blend justified, a prior mis-windowed
Mean cross-sectional Spearman correlation between 12-1 momentum and 52-week-high proximity:
0.519, with only 19% top-decile overlap — COMPLEMENT, decisively: the frozen L3 construct's
rank blend combines two substantially different name-pickers, and a redundancy
simplification is off the table. The declared stress prior failed the interesting way:
correlation RISES in high-vol months (0.62 vs 0.51) because a crash compresses both signals
toward "who fell least" — George-Hwang's divergence (momentum chases the rebound, the
anchor does not) is a POST-TROUGH phenomenon, and top-decile-vol months are not rebound
months. The full N4 inherits a properly-defined rebound window. Survivorship note: both
signals computed on the identical roster — the structure verdict is robust to the panel's
bias in a way return claims are not (stated at registration).

---
# Addendum 6 (same day): FS-D3 — the global leg refused, for the right reason
The CBOE-VIX mirror (vaulted, two recorded misses in its authentication) was tested as an
interim symmetric third leg for L2. FAIL on both bars: it LOSES the one purely-domestic
episode (election day 2024 — global vol was quiet, and equal-weight averaging pulled the
composite under threshold) and adds 54% more false fires (global vol that never touched
India). The same print vindicates the order-of-arrival taxonomy: on global-origin crises
the leg is a major accelerant — EU-2011's detection lag collapses from +91 to +13 business
days, Russia-2022 from +17 to +9, the both-caught median from 24 to 14. The information is
real; the ARCHITECTURE was wrong. Symmetric averaging lets a quiet world veto a loud India.
FS-D4 (arm-only combination — global fire can accelerate, global calm can never subtract)
is registered with bars and DEFERRED to the full F2 run, keeping a deliberate gap between a
failed variant and its successor per the Contract's re-test discipline.

---
# Addendum 7 (same day): F2-WF — the walk-forward takes the shortlist away
The M4 harness's first real run re-evaluated the two adoptable F2-index cells over four
disjoint eras: BOTH FAIL the >=3-of-4 within-budget bar (each passes only the two quiet
2009-2018 eras; the 2018-2022 and 2022-2026 eras cost +2.5 to +4.1pp/yr). The full-period
drags that cleared the F2-index bar were era-averages flattered by a decade without deep
crashes — exactly the artifact walk-forward exists to expose, on the adjudicator's very
first outing. Two things the print keeps honest: (i) the value is real when it matters —
in the COVID era the same rules cut the crash drawdown from 37% to 26%, so what the folds
quantify is the PRICE of always-on insurance (2.5-4pp/yr in whipsaw-rich eras) against an
~11pp payout when the storm arrives; (ii) the per-era bar I declared is stricter than the
DESIGN budget's program-average framing — recorded as a possible over-tightening rather
than relitigated, because the registered adjudicator for arming anything was always the
FULL F2 (book-level costs, three legs, M4), which now inherits an empty index-level
shortlist and the era-dependence finding. No bar moved; no cell rescued.

---
# Addendum 8 (2026-09-02, evening): H53a — the link that runs backwards
The first measurable link of the H53 candidate (commodity prices → INR) FAILED with an
inverted sign: annual energy-price changes correlate NEGATIVELY with INR depreciation
(rho −0.52; all-commodity −0.64; 1993-2016, n=24 after the PCPS NaN head — recorded). The
mechanism story ("India imports energy, so energy up weakens INR") is real micro but swamped
by the macro: commodity booms ARE global risk-on episodes, and risk-on brings EM inflows
that strengthen INR — 2003-07 oil tripled while INR appreciated; 2008, 2013 and 2015
commodity crashes were INR's worst years. The global factor owns both series. Consequences:
(i) H53 stays exactly as registered — the ToT state must prove it ADDS TO L9, conditionally,
and can never be promoted on an unconditional print; (ii) a folk desk heuristic ("oil up =
India down") is now a measured casualty at annual horizon; (iii) the fx vault (INR/USD
1973-2026, 4/4 anchors) is admitted machinery for the conditional test when CAD lands.
