# TRACK T — results of record (technical-quant-systematic)
Opened 2026-09-03 (charter: research/frontier/manager-frontier-sweep.md §C). Same law as
everything else: pre-registration, census cells, DSR via census_n(), costs in.

## T1 (2026-09-03) — overnight/intraday decomposition. Script: scripts/analyze_t1_overnight.py
PRE-REGISTERED bar: US signature (overnight mean > 0 AND intraday <= 0, NW t(o−i) ≥ 2).
PRINT: **PASS, and not attenuated** — full sample 2007-2026 (n=4,553): overnight
**+24.0%/yr** (NW t=+10.5) vs intraday **−12.6%/yr** (t=−2.9); the gap +36.6%/yr at t=+7.6.
Robust ex-COVID (+36.9%/yr, t=+7.9) and STRONGER post-BR3 (2019+: gap +41.7%/yr, t=+6.8).
The ENTIRE Nifty risk premium — and more — accrues while the market is closed.

Honest read (written AFTER the print): the registered prior was half wrong — the desk
expected the signature "present but attenuated"; it is present at FULL strength, stronger
than typical US prints, and strengthening. Mechanics that must temper the reading: (i) the
Indian overnight window carries most global news (US session → India open), so part of this
is the geography of information, not a market inefficiency; (ii) index OPEN prints are
auction values — a real order at the open pays spread/impact the print ignores; (iii) the
CONSUMPTION CAP registered before the run stands absolutely: a 2-trade/day harvest dies at
STT instantly. What it IS: (a) execution-timing evidence — the desk's staged deployment
tranches should default to BUY-AT-CLOSE (capturing the average overnight accrual) rather
than buy-at-open, and de-risk executions should not reflexively wait for the close; (b) a
Track T context result that any future intraday-flavored design must respect.

## T-CTRL1 (2026-09-03) — the BLL MA family (control group). Script: scripts/analyze_tctrl1_ma.py
PRE-REGISTERED prior: ZERO survivors of net-Sharpe > buy-hold AND DSR > 0.95 at
n_trials = census+10 (=174), costs 28bps/unit turnover.
PRINT: **0/10 survivors — the graveyard printed as expected.** Two cells nose past buy-hold
on raw net Sharpe (VMA(1,150) 0.56; VMA(5,150)/1% 0.58 vs BH 0.55) and BOTH die under
deflation (DSR 0.92-0.94 < 0.95). The most-mined rule family in finance is dead on the
NIFTY net of costs and selection — exactly the calibration Track T's opening needed: any
future T-design must clear the bar these could not, and the census that killed them
(174 trials) is the same census that will judge the survivors.

Census: T1 = 5 reads (full + bar + 2 eras + ex-COVID); T-CTRL1 = 10 cells → +15.

## T3 / T4 (2026-09-03, late) — the backlog pair. Script: scripts/analyze_t3_t4.py
**T3 (dual momentum NIFTY vs INR-gold): FAIL at both k, and more decisively than the prior
predicted.** Net Sharpe 1.14 (k=3) / 1.13 (k=12) against INR-gold alone at 1.19 and the
50/50 static at 1.17 — and in the k=12 window the static's maxDD (11%) beat the rotation's
(18%) too. The registered prior expected the Sharpe fail but a DD consolation; there is
none — the 50/50 blend STRICTLY dominated. Honest read: a relative rule imposes one lookback
on two assets TS1 already showed trend at different speeds; the rotation buys timing risk
and sells the rebalancing premium. The quiet star of the print is the diversifier itself:
INR-gold Sharpe 1.19 over 2007-2026 — gold's USD run compounded by rupee depreciation — the
measured base for the books' standing gold allocations.
**T4 (India low-vol quintile, one-way): INCONCLUSIVE — the shape without the certificate.**
Beta 0.67, Sharpe 1.45 vs 1.34, maxDD 24% vs 34%: the defensive anomaly's exact signature;
alpha +2.65%/yr at NW t=1.88 misses the registered t≥2. Because the declared one-way runs
AGAINST low-vol on survivor data, this fail refutes nothing — and confirms nothing. The PIT
run decides; nothing enters the factor library today.
Census: +4 → 183.

## T2 (2026-09-03, late) — trend-on-states at the slow band. Script: scripts/analyze_t2_trendstates.py
**FAIL as registered** — the Kilian index's 12m trend sign adds nothing to its level for
next-month NIFTY (t=+0.48 vs the ≥2 bar; the level itself inert unconditionally at t=−0.54,
n=142). The levels-not-directions doctrine, closed at index resolution for the fast state,
now also holds at the slow-macro band; the phase file's reopening clause does not activate.
Track T's runnable backlog is now EMPTY: T5 (volume rules) and everything sharper waits on
PIT data; H60/H61 wait on their pulls. Census: +2 → 185.

## T1b / T6-TOM (2026-09-03, night). Script: scripts/analyze_t1b_t6.py
**T1b — the overnight drift is a calm-days phenomenon, and stress is an INTRADAY event.**
In-episode overnight: +9.2%/yr at t=+0.66 (the registered null); in-episode INTRADAY:
−66.3%/yr at t=−3.3. The prior expected stress to land overnight (global news); it lands in
the local session — a mechanism miss worth having on record. Ops guidance shipped: buy-at-
close holds on calm days (T1's +24%/yr accrual); in stress there is no drift to protect, so
de-risk fires may execute at the next open without measurable sacrifice.
**T6-TOM — the premium is real; the SIP fingerprint is not.** Full-sample turn-of-month
premium +7.2bp/day (p=0.025) — bar (i) pass. But across BR6 the premium SHRANK (+12.2 →
+3.8bp/d), the opposite of the SIP-amplification prediction — booked AGAINST H61's
index-level motivation exactly as the registration promised. The aggregate-multiplier test
(H61 proper, flows data) remains live and unbiased by this; the calendar shadow just isn't
where the inelasticity shows.
Census: +8 → 193.
