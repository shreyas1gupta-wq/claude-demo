# OP-D2 SYNTHESIS — The Optimized Multi-Tenor Option Portfolio v2

**Date:** 2026-09-07 · **Scope:** adjudication of the OP-D2 sweep (22 families F01–F22, 12
combiners C01–C12; 73 pre-registered cells) into one coherent paper design. **Status:** design
brief for H60-VRP — PAPER-ONLY per CONTRACT (no live trade; options notional ≤50% directional /
≤75% tail; gross ≤1.5x; drawdown binding). Every number below is a printed desk number from
`research/opt_sweep/*.json`; no bar was moved (F05, F14, F16 MISSes recorded as such). Nothing
here is promoted — promotion requires H60-VRP's own pre-registration, which is **data-gated**
(§8).

---

## 1. Verdict board

| Family | Headline (printed) | Verdict |
|---|---|---|
| F01 HMM-2 regime | No-lookahead 2-state HMM fwd-21d vol spread 2.02x the VIX-pct baseline (12.9 vs 6.4 pts) — but the high state is rare (6.2% of days) and catches only 45% of storm days vs 82% for VIX-pct: NOT a substitute stress flag | MISS (on the ≤1.15x no-gain bar; info real, trigger unusable) |
| F02 HMM-3 | 3rd state adds NO crash-onset separation (0/41 onsets at t-1; onset reaction 2.4% vs K2's 22.0%) but widens fwd-vol separation 1.43x — a post-hoc tail-confirmation state only | TWO-SIDED |
| F03 EWMA grid | ewma_0.94 QLIKE 1.5016 vs roll-21 1.5200: +1.21% vs the ≥3% bar; still grid-best | MISS |
| F04 GARCH vs EWMA | Statistical tie (QLIKE gap −0.57%, inside \|2%\| band); BOTH lag the Mar-2020 onset by 72.1/73.6 vol pts (RV5 94.4 vs forecasts 22.4/20.8) | PASS x3 (prior confirmed) |
| F05 Vol-target sizing | Worst-month improvement +5.77% vs ≥30% bar (Mar-2020 entry predates the spike); mean "cost" −42.6% (a gain) | MISS (joint bar) |
| F06 Trend x VIX corners | belowMA+hiVIX has the widest fwd-21d dispersion (std 7.13 vs 4.0–6.2) and highest fwd vol (26.9 pts), n=247 | PASS |
| F07 Index 12-1 momentum | Sign is NEGATIVE vs fwd returns (fwd1m −1.93%, fwd3m −6.02%, \|t\|≥7.18) — post-crash V-rebound artifact of 2008/2020 troughs | MISS x2 |
| F08 5d z-score MR | Full-sample −0.16σ hides a SIGN FLIP: pre-2015 reversion +0.79σ vs post-2015 continuation −0.83σ (n=15/36, thin) | TWO-SIDED |
| F09 Breadth washout | corr null once overlap-corrected (r=−0.04, boot p=0.62); bottom-decile bounce +2.9pp (boot p=0.002) but ~11 episodes, top-2 = 50% of days, permutation p=0.044 | TWO-SIDED |
| F10 Candle graveyard | 6/8 null as registered; doji_fwd5d t=2.47 (fails Bonferroni ~2.75) and 3down_fwd5d t=3.02 flagged, neither promoted | PASS x6 / TWO-SIDED x2 |
| F11 Gap continuation | No significant intraday continuation on ≥1% gaps (−0.16/+0.16%, ns); hi-VIX fade differential p=0.07–0.08, underpowered and contemporaneous-labeled (down-gap leg nearly halves when lagged/actionable, −0.62→−0.30pp; up-gap leg holds at −0.33pp but was never significant — C07) | TWO-SIDED x4 |
| F12 Parkinson estimator | Parkinson-21d QLIKE 1.6347 is 7.5% WORSE than close-close 1.5200 vs a ≥5%-better bar | MISS |
| F13 VIX horizon / IV-HV | Corr peaks at 10d (0.666) not 21d (0.583) → MISS; Q5 spread bucket best (+6.80) → PASS — but **REFUTED on process** (groupby `.first()` Frankenstein row; true n=141 not 142). Dead until re-run and re-registered | MISS + PASS → REFUTED |
| F14 VIX spike decay | Half-life to pre-spike level: median 2 trading days vs the 15–40d sleeve-A bar; days to re-enter <60th pct: median 29d (descriptive) | MISS |
| F15 Structural greeks/stops | 7d 1σ condor = 2.0x theta/day + 2.1x gamma at 0.48x vega of 30d; stop-2x gap-through needs only 2.0–5.2% moves at 7d (vs 3.9–10.2% at 30d), P(gap)/day midVIX 0.55% vs 0.00%; gapped exits average 2.9x credit (max 8.6–9.0x) | DESCRIPTIVE (analytic) |
| F16 Monthly condor sim | Stop-2x MISSES both edges (worst-month cut 46.0% vs ≥50; mean cost 32.2% vs ≤30); delta-band roll dominates descriptively: 35.5% cut at 9.6% cost, best p5 (−1.044 vs −2.528 %S) | MISS (stop-2x) |
| F17 Weekly condor sim | +1.89%/wk per margin (80% hit) but ONE full-wing wipe (Budget wk 2016-02-29, −100%) makes per-unit-margin compounding RUIN vs monthly +13.96%/yr geo; daily close-stop buys only −100%→−93.3% | TWO-SIDED |
| F18 Kelly / DD sizing | Full Kelly f* 1.90 mo / 0.35 wk infeasible; the 10%-DD/1%-yr constraint binds ~10x below Kelly: f=0.165 mo / 0.035 wk (+2.9 / +1.3%/yr) — all UPPER bounds (iid bootstrap) | DESCRIPTIVE (constraint math) |
| F19 Event calendar | Budget window \|ret\| 0.95% vs 0.59% off-window, p=0.0049 (confirms the CW-D1a return leg; headline's CW-D1v attribution corrected in C08); election = the tail (2009-05-18 +17.74%, n=3 descriptive); RBI null (p=0.43) | PASS / DESCRIPTIVE / TWO-SIDED |
| F20 L2 stress overlay | pct≥0.90: left-tail trim +46.6% (bar ≥20) at cost +9.7% (bar ≤10); beats VIX-pct-alone by +4.4pp — but the edge reduces to 1–2 flagged months (2020-03 caught by both; 2019-09 the only extra) | PASS x2 (effective n=1–2) |
| F21 Stress betas | Bank-heavy beta CONTRACTS in stress (hi/lo 0.69: 0.95 vs 1.36) — AGAINST the expansion prior; smallcap-tercile stable (0.92) | DESCRIPTIVE (prior falsified) |
| F22 INR overlay | Null both axes (corr r=+0.01 p=0.92; weak/strong diff −0.61 p=0.55); stand-down flags 89/154 months, +79% trim at +53% cost — "NOT a usable overlay" | TWO-SIDED x3 |

**Combiner adjudications:** C01 stack-vs-single (VIX_PCT_ALONE_CARRIES_IT) · C02 sizing formula ·
C03 per-tenor management · C04 capital split + compounding verdict · C05 vol-input choice (EWMA
.94) · C06 state machine (VIX-pct retained) · C07 direction-overlay kill x4 · C08 event policy ·
C09 India overlays (INR dropped, bank-hedge killed) · C10 graveyard (10/22 families) · C11
risk-limit table · C12 completeness critic (data gates).

---

## 2. The entry-state machine (C06, C01, F16)

**Chosen: the expanding-percentile India-VIX rank ("VIX-pct", min_obs=252, no lookahead) — the
single state variable that gates entries.** No stacking, no HMM, no direction overlay.

- **Entry gate:** open a new premium cycle only when VIX-pct ≥ 0.60 (F16's registered gate; 41
  monthly entries of 136 blocks, mean +0.557 %S/mo, hit 0.80). Q5 VIX months carry +5.58 vol pts
  of monthly VRP vs +2.96 unconditional (C01, n=21/141).
- **Stacking rejected (C01):** the best 3-way stack (VIX-hi x IV-HV-hi x aboveMA) prints +8.43
  but at n=6 (71% sample shrink) and the spread state mechanically inherits VIX's level —
  verdict VIX_PCT_ALONE_CARRIES_IT. (The IV-HV leg's parent F13 is also process-REFUTED.)
- **HMM excluded outright (F01/F02, C06):** the 2-state high regime catches 45% of storm days vs
  VIX-pct's 82%; neither K=2 nor K=3 is EVER in its top state at t-1 before a crash onset (0/41)
  and K=3 reacts slower at onset (2.4% vs 22.0%). K3's only defensible role is a post-hoc
  tail-confirmation label, never a trigger.
- **Stand-down (de-risk) gate:** stress rank ≥ 0.90 → no new premium (§6). The L2 RV+DD
  composite (F20) edges VIX-pct here on registered bars but on effective n=1–2 events — and
  VIX-pct-alone at the same 0.90 gate prints only ~+42.2% trim at ~12.1% cost, MISSING F20's
  ≤10% cost bar (F20 cell 3 / C06); the L2 composite is a **monitored candidate**, not the switch; the production stand-down keys off the same VIX-pct
  machinery at the 0.90 grid point (grid pre-registered in config/ladder.yaml L2, not invented).
- **No direction overlays (C07):** momentum (F07), MR (F08), breadth (F09), gap (F11) all killed
  for structure-skewing — F07/F09 are 48.6% the SAME crash-rebound days (2.16x enrichment, 5
  episodes led by Feb-2016 and Mar–Jun-2020); F08 sign-flips across 2015; F11's actionable
  (lagged) form stays insignificant — the down-gap differential nearly halves (−0.62→−0.30pp)
  and the up-gap leg (−0.38→−0.33pp) was never significant to begin with (C07). **Base structure stays the symmetric condor**
  (short 1.0σ strangle + long 2.5σ wings, F15/F16 convention).

---

## 3. Sizing policy (C02, F18, F05, C05, C11)

**One formula — fraction of book posted as margin per monthly condor cycle:**

```
f_t = min( f_DD(arm) x s_t , f_cap )
s_t = min( target_vol_t / EWMA_vol_t(lambda=0.94) , 2.0 )     [F05 registered spec, no lookahead]
f_DD = 0.150 (monthly hold) | 0.185 (monthly stop-2x arm)      [C02: re-derived on vol-scaled
                                                                F16 returns under F18's
                                                                P(book maxDD>10%) <= 1%/yr]
f_cap = 0.10 of book (monthly)                                 [C11 structural override: a
                                                                full-margin wipe alone must not
                                                                breach the 10% DD ceiling]
Weekly sleeve: f <= 0.035 of book (F18), preferably 0.
```

- **Vol input:** EWMA λ=0.94 on close-to-close daily log returns (C05) — grid-best in F03
  (QLIKE 1.5016), statistically tied with GARCH(1,1) (F04, gap −0.57% inside the 2% band) with
  zero crisis-detection difference (onset lags 73.6 vs 72.1 pts), no optimizer/refit risk.
  Parkinson/OHLC ruled out (F12, −7.5% worse).
- **Concrete numbers** (C02, median s in VIX-pct band, before the 0.10 cap): monthly hold arm —
  pct 0.60: 0.197 → capped 0.10; pct 0.80: 0.165 → 0.10; pct 0.95: 0.124 → 0.10. Stop-2x arm:
  0.243 / 0.204 / 0.152 → all capped 0.10. Hard ceiling by construction 2 x f_DD (0.30/0.37),
  overridden by f_cap = 0.10. Use the LIVE s_t, never band medians (pct~0.95 IQR [0.47, 1.30]).
- **What s_t is and is not:** vol-targeting raised mean P&L (+4.21 vs +2.95 pts, F05's PASS leg)
  by upsizing calm months (31/154 at the 2x cap) but CANNOT protect against sudden onsets —
  Mar-2020 entered at s≈0.94 (F05 MISS: worst-month improvement +5.77% vs ≥30% bar) because no
  filter sees the crash coming (F04: 72–74-pt onset lag). Worse, s_t can actively AMPLIFY
  losses: on several next-worst months (Aug-2015, Aug-2013) trailing vol was low pre-entry, so
  vol-targeting UPSIZED into the loss and made it worse than fixed-1x (F05 caveat; the same
  mechanism is why C02's scaling LOWERS the DD-feasible base 0.165→0.150). **Tail safety rests
  entirely on the f_DD budget and the 2.5σ wings, never on s_t.**
- **Arm-mismatch caveat (C02 vs C03):** C02 derived f_DD only for the HOLD (0.150) and STOP-2x
  (0.185) arms — and itself preferred the stop-2x arm — while §4's management rule is the
  delta-band roll (C03, which rejects stop-2x). No f_DD has been bootstrapped on ROLL-managed
  returns; until H60-VRP derives one, the roll-managed sleeve uses the conservative hold-arm
  f_DD = 0.150 (the 0.10 cap binds regardless at prevailing s levels).
- **Kelly context (F18):** full Kelly 1.90 mo is levered margin, infeasible under CONTRACT's
  1.5x gross; half-Kelly (0.951) runs P(DD>10%) = 41%/yr. The DD constraint, not Kelly, sets
  the size (~f*/10). All F18 f's are UPPER bounds (iid bootstrap ignores vol clustering).

---

## 4. Management rules per tenor (C03, F15, F16, F17, C11)

**Monthly (primary sleeve, 21td cycles):**
- **Daily mark-to-market** at that day's VIX (F16 sim convention); management signal checked at
  every close.
- **Primary rule: delta-band roll — roll the tested short strike when \|delta\| ≥ 0.30, max 3
  rolls per cycle.** Delivers a 35.5% worst-month cut at 9.6% mean cost with the best left tail
  (p5 −1.044 %S vs hold −2.528) — 2.6x more cost-efficient than stop-2x (0.27 vs 0.70 cost per
  pp of cut, C03). NOT the 2x-credit hard stop: it registered-MISSED both edges (46.0% cut vs
  ≥50 bar at 32.2% cost vs ≤30 bar, 11/41 stops). Caveat: the roll is an UNBARRED descriptive
  cell — it needs its own pre-registered bar in H60-VRP before promotion.
- Hold to expiry otherwise; no re-strike after the 3rd roll — the 2.5σ wings cap the residual.

**Weekly (satellite sleeve, 7d cycles, if traded at all):**
- **No daily-close stop is credited with tail protection.** F17: the close-stop improves the
  worst week only −100% → −93.3% (+7%) at 11% mean cost, and its stopped arm still compounds to
  −28.96%/yr. F15's structural reason: at 7d the stop-2x gap-through threshold is only 2.0–5.2%
  of spot (vs 3.9–10.2% at 30d), P(gap-through) 0.55–2.01%/day (vs 0.00–0.25%), and a gapped
  exit averages 2.9x credit (max 8.6–9.0x). Weekly = gamma/gap risk (2.1x gamma at 0.48x vega
  of 30d) that close-based rules cannot see.
- **The binding controls are SIZING (f ≤ 0.035) and the 2.5σ wings themselves** — defined-risk
  is mandatory (F17's measured −100% week bans undefined risk outright).
- **Calendar exclusion:** never initiate a weekly whose ISO week contains a Budget-window day
  (§6) — F17's single ruin week WAS Budget week 2016-W09.

**Daily management common to both tenors (C11):**
- Book-level daily loss stop SET at 2x net premium outstanding (−2.22% of book at the premium
  cap) but BUDGETED at −3.22% realized on gap days (F15's 2.9x gapped-fill mean); breach → flat
  the sleeve, re-entry per §7.
- Stand-down check daily: stress rank ≥ 0.90 → no new premium, existing positions run their
  management rules.

---

## 5. Weekly/monthly capital split + the compounding verdict (C04, F17, F18)

**Split: 80/20 monthly/weekly of the VRP-overlay capital** — two independent methods bracket it:
F18 DD-constrained-f ratio 0.165 : 0.035 → 82.5/17.5; worst-cycle loss parity 30.6% : 100% →
76.6/23.4. In absolute terms both sleeves run concurrently at ≤ ~13.5% of book as margin under
the C11 caps (0.10 + 0.035), i.e. the split is a capital-earmark inside a small sleeve, not a
book-level allocation.

**The compounding verdict:** CONFIRMED as **sizing-dependent, refuted as a frequency claim**.
Weekly has the better per-unit arithmetic edge (+1.89%/wk; +37.4 vs +21.3%/yr uncompounded) but
compounding it at full margin gives P(ruin)=1 in-sample — one 2.5σ full-wing breach (Budget week
2016-02-29, −100% of margin) zeroes terminal wealth, while monthly never wipes (worst −30.6% of
margin, 2021-12-20) and compounds at +13.96%/yr geo. A ≤20% weekly earmark converts a would-be
ruin event into a bounded drawdown. Two C04 footnotes of record: (a) F17's own internal
"monthly" comparator is NOT F16's registered design (calendar months + broader gate, n=50 vs 41)
— the true registered monthly worst (−30.6%) is milder, reinforcing the direction; (b) the two
sleeves' per-margin historical worsts are 2,142 days apart (supportive but n=1 diversification
evidence — no joint-tail estimate exists; the split carries unquantified joint-tail risk).

---

## 6. Overlays kept and killed

**KEPT:**
1. **Event/Budget exclusion (C08, F19, CW-D1a/CW-D1v):** exclusion window = Budget T-1/T/T+1
   (19 matched events, 57 window days) — elevated realized moves (median \|ret\| 0.95% vs 0.59%,
   p=0.0049, the CW-D1a return leg) AND the day-0 IV crush (CW-D1v: −8.9% dlogVIX at day 0,
   p=2.7e-06). No fresh weekly into a Budget ISO week (30/970 weeks affected); monthly blocks
   (20/217 overlapping) need no hard exclusion (no full wipe on record). A dedicated T-1→T
   short-vega "budget trade" is a DESIGN BRIEF only — must be pre-registered before any number
   is run. No election rule (n=3, manual flag only: 2009-05-18 +17.74% is the single most
   extreme day in the vault) and no RBI rule (p=0.43, null).
2. **Stress stand-down (F20, C11):** no new premium at stress rank ≥ 0.90 — held as **cheap
   insurance** with eyes open. Attribution matters: the +46.6% trim at 9.7% cost PASS x2 is the
   **L2 RV+DD composite's** print; VIX-pct-alone at the same 0.90 gate prints ~+42.2% trim at
   ~12.1% cost and MISSES the ≤10% cost bar (F20 cell 3 / C06). The production stand-down is
   implemented on VIX-pct (C06) and therefore carries VIX-pct's own weaker, bar-missing print —
   not F20's PASS numbers. Either way the verifier shows the edge is 1–2 events (COVID
   dominates); the L2 RV+DD composite stays a monitored candidate (C06).
3. **F02's K3 crash state** as a post-hoc tail-confirmation label on the dashboard (fwd RV 35.6
   pts, 1.6% occupancy) — never a trigger.
4. **Hedge-instrument note (C09/F21):** if a beta-stable index proxy is needed across VIX
   regimes, prefer the smallcap-tercile basket (beta hi/lo 0.92) over bank-heavy (0.69 — bank
   beta CONTRACTS in stress, killing the amplified-stress-hedge assumption). Descriptive,
   survivor-biased panel, design input only.

**KILLED — the graveyard (C10: 10/22 families; C07/C09 kills folded in):**
| Killed | Why (one line) |
|---|---|
| F03 EWMA/rolling grid tuning | +1.21% vs ≥3% bar — tuning buys nothing over the default |
| F04 GARCH machinery | tie with EWMA, zero crisis edge — machinery cost, no payoff |
| F05 vol-target as tail protection | +5.77% vs ≥30% bar; kept ONLY as C02's mean-P&L multiplier |
| F07 momentum direction overlay | MISS x2; post-crash rebound artifact (C07 redundancy proof) |
| F08 MR overlay | sign flips across 2015; both regimes thin |
| F09 breadth washout | 11 episodes, top-2 = 50% of days; perm p=0.044 (~20x weaker than reported) |
| F10 candle patterns | 6/8 null; doji_fwd5d (t=2.47) fails Bonferroni ~2.75, 3down_fwd5d (t=3.02) clears it but stays unpromoted (overlapping fwd5d windows, no HAC — C10) |
| F11 gap continuation | null; the one split is underpowered and contemporaneous-labeled |
| F12 Parkinson | actively worse (−7.5% vs ≥+5% bar) |
| F13 IV-HV quintile gate | REFUTED on process (groupby leak) — dead until re-run + re-registered |
| F20-as-replacement-state | PASS/PASS but effective n=1–2 over plain VIX-pct — no incremental adoption |
| F22 INR gate | null both axes; 58% flag rate, +53% cost — "NOT a usable overlay" |
| Bank-heavy stress hedge (F21 prior) | beta contracts, not expands, in stress |
| HMM as regime gate (F01/F02) | 45% vs 82% storm capture; 0/41 onset detection |

---

## 7. Risk-limit table (C11 — all wings defined; undefined risk banned)

| # | Limit | Value | Source |
|---|---|---|---|
| 1 | Monthly margin cap | **f ≤ 0.10 of book** per cycle (tighter than F18's 0.165 upper bound; a full-margin wipe alone cannot breach the 10% DD ceiling) | C11, F18 |
| 2 | Weekly margin cap | **f ≤ 0.035** of book; preferably 0 (+1.3%/yr only) | F18, C04 |
| 3 | Max net premium at risk | **≤ 1.11% of book** per cycle (= 10% DD ceiling / F15's 9.0x max gapped loss) | C11, F15 |
| 4 | Max structural loss | 10% of book monthly (full 2.5σ wing breach at cap); measured-worst at cap 3.06% (F18: −30.6% of margin); weekly 3.5% | C11, F16/F17 |
| 5 | Daily loss stop | SET −2.22% of book (2x premium); BUDGET −3.22% realized on gaps (2.9x fills, max 8.6–9.0x) | F15, C11 |
| 6 | Position management | monthly: \|delta\| ≥ 0.30 roll, max 3 — NOT the 2x hard stop; weekly: wings are the stop | C03, F16 |
| 7 | DD governor | sleeve budget P(maxDD>10%) ≤ 1%/yr; HALVE size at −5% sleeve DD; FLAT at −10%; no upward discretionary override (all caps are upper bounds) | F18, C11 |
| 8 | Stand-down | stress rank ≥ 0.90 → no new premium (implemented on VIX-pct; F20's PASS x2 numbers belong to the L2 composite — see §6.2) | F20, C11 |
| 9 | Re-entry | only when the rank prints < 60th pct (median wait 29td, F14) — NEVER on the VIX snapback (median half-life 2d, F14 MISS); after a −10% flat, half size for one full cycle | F14, C11 |
| 10 | Calendar | no fresh weekly premium into Budget windows (T-1/T/T+1) | C08, F19 |
| 11 | Contract-level gross | delta-adjusted exposure counts inside the 1.5x gross cap; Tier-C reduce-only; no vol-forecast-scaled tail sizing (F05 MISS); no IV-HV gating (F13 REFUTED) | CONTRACT, C11 |
| 12 | Options notional caps | **≤50% of book directional options notional; ≤75% of book tail options notional** — separate hard caps from the 1.5x gross cap (row 11), not subsumed by it | CONTRACT |
| 13 | Tenor priority | monthly primary (+13.96%/yr geo vs weekly per-margin RUIN) | F17, C04 |

---

## 8. What remains data-gated + upper-bound caveats (C12)

Every seller-favorable number in this document is an **UPPER BOUND**, for five compounding
reasons:

1. **2008 is not in the VIX sample.** The India VIX vault runs 2010-07-23..2023-04-05 (n=3,142);
   the 362 NIFTY trading days of the GFC crash+recovery (2008-01..2009-06) never enter ANY
   VIX-conditioned family (F01/F02/F06/F11/F13/F14/F16/F17/F18/F20/F21/F22). F14's 2-day
   half-life, F16/F17's condor P&L and F18's Kelly/DD math are all calibrated on a crisis-light
   window whose only crisis is one V-shaped COVID month.
2. **The 743-day post-2023-04 tail is also missing** — including the 2024 election spike and the
   SEBI 2024-26 derivatives curbs (breaks-registry C2: contract size, weekly-expiry
   rationalization, upfront premium). F16/F17/F18 describe a **pre-curb microstructure that may
   no longer exist**; H60-VRP must carry an explicit era-split at that break, not just a
   sample-size caveat.
3. **No option chains.** F15–F18 are flat-sigma=VIX Black-Scholes paper sims: no smile/skew, no
   bid-ask, no slippage, no transaction costs, no strike granularity, margin proxy = max loss
   (not SPAN+exposure). F16's 32.2% stop cost and F17's ruin week are BEST-CASE execution
   numbers; F18's f-to-capital translation is untested against real margin.
4. **funding_rate unset** (`risk.yaml` funding_rate.value: null — the standing validator
   warning): the leverage feature arithmetic caps at 1.0x until the principal confirms the
   actual desk rate; the r=0.06 in all BS sims is an assumption, not a desk number.
5. **Paper-only per CONTRACT** — this entire design feeds the H60-VRP paper design brief; its
   registration is itself deferred to data landing (manager-frontier-sweep gate).

**Priority pulls (principal-machine; NSE egress blocked here):** (i) NSE India VIX primary via
`ingest/pull_india_vix.py --emit-auth-template` — the 2009 head through the 2026-09 tail (closes
the GFC front-end AND the election-spike/SEBI-curb back-end at once); (ii) NSE option-chain IV
snapshots (strikes, bid/ask, OI — RUNSHEET line 16) — without them F13/F15–F18 cannot be
upgraded past BS-analytic/VIX-proxy status.

**Open PARTIAL items before any promotion (C12 flag list):** F06's 200-DMA provenance; F07's
missing purge/embargo (quant/stats/cv.py unused); F09's bootstrap-vs-permutation gap; F10's
Bonferroni split; F13's REFUTED leak (re-run with `.head(1)`, re-register); F19's CW-D1a/CW-D1v
headline mislabel (corrected in C08); F20's effective-n; F21's wrong-sibling grid citation.
Additionally owed by the roll rule: a pre-registered bar for the delta-band roll (currently an
unbarred descriptive winner).

---

*Written by the OP-D2 synthesis stage, 2026-09-07. Sources: research/opt_sweep/f01–f22.json,
c01–c12.json; scripts/opt_sweep/*.py prints of record; research/register/trial-ledger.md;
research/CONTRACT.md. No new number was computed for this document.*

---

## Red-team findings

*Adversarial audit of this document against research/opt_sweep/f01–f22.json + c01–c12.json,
2026-09-07. Each issue below has been fixed in the body text above (dated in-place edits, per
process note; the original wording is recoverable from git history).*

1. **[FIXED — §2, §6.2, §7 row 8] Stand-down numbers contaminated by rule-swap (F20/C06).**
   The body prescribed implementing the stand-down on VIX-pct while quoting "+46.6% trim at
   9.7% cost on registered bars" — those PASS x2 numbers belong to the **L2 RV+DD composite**
   (f20.json cells 1–2). VIX-pct-alone at the identical 0.90 gate prints ~+42.2% trim at ~12.1%
   cost (f20 cell 3: L2 edge +4.42pp trim / −2.4pp cost; c06 evidence) and **misses the ≤10%
   cost bar**. The production choice (VIX-pct per C06) therefore carries a weaker, bar-missing
   print, not F20's PASS. Body corrected to attribute each number to its own rule.

2. **[FIXED — §6 graveyard F10 row] Bonferroni claim inverted.** The graveyard said "neither
   survivor clears family-wise correction" — c10/c12 print the opposite split: 3down_fwd5d
   (t=3.02) **clears** the ~2.75 family-wise Bonferroni bar; doji_fwd5d (t=2.47) does not.
   (Neither is promoted — overlapping fwd5d windows, no HAC — but the stated reason was wrong;
   the §1 verdict-board row was already correct.)

3. **[FIXED — §1 F07 row] t-stat drifted upward.** "\|t\|≥7.2" overstated the print: f07's
   fwd1m t is −7.179 (c07 quotes "both t≤−7.18"; c12 flags the same 7.2-vs-7.179 rounding in
   f07's own headline as an open item). Corrected to \|t\|≥7.18.

4. **[FIXED — §1 F11 row, §2] "Halves when lagged" overgeneralized.** Only the **down-gap**
   hi−lo differential nearly halves under the lagged/actionable labeling (−0.622 → −0.301pp,
   c07 Q3); the up-gap leg holds up (−0.376 → −0.334pp) and was simply never significant
   (p=0.068). The kill verdict is unchanged; the mechanism claim was imprecise.

5. **[FIXED — §3, new caveat bullet] Sizing base f_DD has no verified backing for the chosen
   management arm.** C02 derived f_DD only on HOLD (0.150) and STOP-2x (0.185) vol-scaled F16
   distributions — and C02's own recommendation *prefers the stop-2x arm* — while §4 (per C03)
   manages with the delta-band roll and rejects stop-2x. No f_DD was ever bootstrapped on
   roll-managed returns, and the C02-vs-C03 arm conflict was previously undisclosed here. Body
   now pins the roll-managed sleeve to the conservative hold-arm 0.150 pending an H60-VRP
   derivation, and discloses the conflict.

6. **[FIXED — §3 s_t bullet] Missing caveat: vol-target s_t can amplify losses, not merely
   fail to protect.** f05.json's caveat (and c02's evidence) record that on next-worst months
   (Aug-2015, Aug-2013) trailing vol was low pre-entry, so s_t UPSIZED into the loss and made
   it worse than fixed-1x — the same mechanism that lowers C02's scaled f_DD (0.165→0.150).
   The body had presented s_t only as "cannot protect against onsets."

7. **[FIXED — §7, risk-policy pass 2026-09-07] Missing limit: options notional caps.** The
   header (line 5) and CONTRACT.md (§ leverage: "the notional caps (≤50% directional / ≤75%
   tail) are separate hard caps" from the 1.5x gross cap) both bind this paper design, but the
   §7 table's old row 11 ("Contract-level") stated only the gross cap and Tier-C reduce-only,
   silently omitting the notional caps — a completeness gap against the table's own "all wings
   defined; undefined risk banned" standard. Added as new row 12, cited to CONTRACT, and row 11
   relabeled "Contract-level gross" to make the two caps' independence explicit; old row 12
   (Tenor priority) renumbered to 13.

**Checked and confirmed clean (no change needed):** the §5 monthly worst −30.6% of margin dated
2021-12-20 and the 2,142-day sleeve-worst separation (both are c04's bit-exact recomputation —
c04 explicitly supersedes f18.json's "(COVID)" mislabel); F13's REFUTED status is quarantined
everywhere it appears (stack bullet, §7 row 11, graveyard) and no recommendation loads on it;
the CW-D1a/CW-D1v attribution follows c08's correction; all F01–F22 headline numbers in the §1
verdict board, the C02 concrete sizing fractions, the F15 gap geometry (1.11%/2.22%/3.22%
chain), the C04 80/20 bracket (82.5/17.5 and 76.6/23.4), the C01 stack numbers (+8.43 n=6 vs
+5.58 n=21 vs +2.96 n=141), and the C12 data-gap counts (362 GFC days, 743-day tail, n=3,142)
reproduce from the JSONs as quoted.
