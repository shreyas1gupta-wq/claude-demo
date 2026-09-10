# When Momentum Works, When It Doesn't, and When to Switch — the Condition Map

*Literature dossier, Track T (technical-quant-systematic), 2026-09-10. No web fetches —
written from training knowledge; every literature claim carries **[LIT]**, and where the
citation is solid but the magnitude is recalled with less confidence, **[LIT, hedge]** or
**[VERIFY: …]** names what to check before any number is sized. Desk numbers are quoted
verbatim from `research/register/trial-ledger.md` — entries M0–M5 (2026-09-01, momentum
real-data), VAL-D4 (2026-09-10, factor-level value complementarity), FUN-D10 (2026-09-09,
monetary-regime × factor), SC-D4 (2026-09-10, size-conditional edge map) — and QG-D2
(2026-09-08), which independently corroborates the EW-panel artifact SC-D4 also catches;
each marked **[DESK, <entry>]**, never re-derived here. Per CONTRACT §4/§9, every non-India
citation is a cross-country prior, Tier B at best until purged-CV India tests exist; per
§5, every candidate below is asked *why does this survive being known*, and "it backtests
well" is named as the unacceptable answer it is.*

---

## 1. Lookback structure: what horizon, and why

**Jegadeesh & Titman (1993)**, "Returns to Buying Winners and Selling Losers," *Journal of
Finance* 48(1) **[LIT]**, is the origin: a full 3×3 grid of formation periods (3, 6, 9, 12
months) crossed with holding periods (3, 6, 9, 12 months), skip-a-month between formation
and holding to avoid 1-month reversal contamination. The headline cell — 6-month
formation, 6-month holding, 1-month skip — earned roughly **1%/month (≈12%/yr)** hedge
return (winner-decile minus loser-decile) in 1965–1989 NYSE/AMEX data **[LIT]**. Every
cell in the grid was positive and mostly significant: momentum is a horizon *band*, not a
single-lookback artifact, the origin of the "3–12 month" language used ever since.

**Novy-Marx (2012)**, "Is Momentum Really Momentum?," *Journal of Financial Economics*
103(3) **[LIT]**, decomposed the 12-month lookback into two non-overlapping pieces —
months t-12 to t-7 ("intermediate horizon") and t-6 to t-2 ("recent horizon", excluding
t-1 as usual) — and found that **the intermediate-horizon piece alone reproduces most or
all of the standard 12-month momentum premium, while the recent 6-month piece alone earns
close to zero and in some specifications is slightly negative** **[LIT]**. This is the
"echo" framing: what looks like momentum on recent price action is largely a delayed
echo of returns from 7–12 months back, not recency per se. The mechanism candidates are
(i) return seasonality/earnings-announcement clustering that recurs on an annual cycle,
and (ii) genuine underreaction that takes several months to fully price, with the most
recent month's return contaminated by short-term reversal that offsets it.

**The debate.** **Goyal & Wahal (2015)**, "Is Momentum an Echo?," *Journal of Financial
and Quantitative Analysis* 50(6) **[LIT, hedge on the exact effect sizes]**, tested the
Novy-Marx decomposition across roughly 40 international markets and found the echo effect
does **not** robustly replicate outside the US sample — the recent-horizon (6-2) piece
often performs comparably to, or better than, the intermediate piece internationally, with
no consistent ordering. The honest reading: intermediate momentum is a real, well-
documented US-sample regularity, but the non-replication is a serious hedge against
treating "12-7 beats 6-2" as a structural law to import without first testing it on Indian
data — the CONTRACT §4 Tier-B discipline (cross-country evidence frozen at inception,
re-argued not assumed).

**What the two bands capture, conceptually.** A 3–6 month lookback sits closest to the
earnings-cycle: quarterly results and analyst-estimate drift (the Bernard–Thomas
underreaction mechanism this desk's ES track documents for PEAD) resolve on a roughly
quarterly cadence, so a 3–6 month window is disproportionately priced by the most recent
one or two earnings events. A 6–12 month lookback integrates across multiple earnings
cycles and is closer to the classical Jegadeesh-Titman underreaction story — slower
diffusion of news through analyst coverage and institutional rebalancing lags, requiring
several quarters to resolve. Chan, Jegadeesh & Lakonishok (1996) found price momentum is
only partly explained by earnings-surprise underreaction — the two bands carry partially
independent information, the standard justification for holding a momentum sleeve and a
fundamental-surprise sleeve as complements, not substitutes.

**Seasonality: the January interaction.** Momentum's canonical weak spot is the turn of
the calendar year: **momentum returns are reliably negative or sharply attenuated in
January**, documented since Jegadeesh & Titman's own paper and sharpened by later work
connecting it to small-cap tax-loss-selling — prior-year losers (small, beaten-down names
sold for tax purposes in December) rebound mechanically in January, exactly the leg a
momentum strategy is short **[LIT]**. This is a genuine calendar-anchored seasonal, not a
magic-number pattern-match — CONTRACT §8 forbids fixed calendar cycles as *forecasting*
devices, but a mechanism-explained degradation of an *existing* signal is a different
object: when NOT to hold full-size momentum, not a new cycle being fitted. India's own
January effect, and its interaction with the April fiscal-year rebalancing calendar, is
untested here and should be registered before being built into a switch rule.

## 2. Momentum crashes: the option-like tail

**Daniel & Moskowitz (2016)**, "Momentum Crashes," *Journal of Financial Economics* 122(2)
**[LIT]**, reframed momentum's risk profile from "occasionally volatile" to "occasionally
catastrophic, and predictably so." Crashes cluster in a specific state: **following a
trailing bear market, when the market then rebounds sharply and volatility is elevated**.
The mechanism: the loser leg, built from the hardest-hit names, becomes populated with
high-beta, distressed, effectively option-like stocks (embedded leverage rises as equity
value falls relative to debt), so when the market snaps back the short loser leg behaves
like a short call option and loses enormously. Daniel & Moskowitz document **1932 and
2009** as the two worst US episodes, multi-month drawdowns in the momentum portfolio on
the order of several tens of percent within a few months **[LIT, hedge: the precise point
magnitudes are recalled directionally only — extreme, multi-decile, concentrated in a 2–3
month rebound window — flag exact figures as VERIFY before quoting in a design document]**.
The structural insight — the loser leg is a short option whose moneyness worsens exactly
when the market recovers — is the load-bearing claim, independent of the exact figures.

**This desk has already replicated the mechanism three times, on two panels.** M2 tested
the DM conditional split on India: crash-zone months (trailing bear market, subsequent
market-up) returned **-2.24%/month against +3.93%/month in bear-and-down months and
+1.39%/month in bull markets — "the option-payoff signature confirmed on India"** **[DESK,
M2]**. M3 replicated the split on US data 1927–2025: crash-zone **-4.59%/month against
+6.85%/month in bear-and-down — "textbook"** **[DESK, M3]**. M4 tested the desk's own
`crash_guard` construct against real US months: guard-ON **-2.19%/month (n=95) against
guard-OFF +1.81%/month (n=1069) — "crash tail lives in guard-ON"** **[DESK, M4]**. Two
countries, one mechanism: the DM crash state is a replicated, real-data fact here, not a
theoretical curiosity.

**Barroso & Santa-Clara (2015)**, "Momentum Has Its Moments," *Journal of Financial
Economics* 116(1) **[LIT, hedge on the exact Sharpe multiple]**, propose the standard fix:
scale the momentum position each month to target a constant *ex-ante* volatility, using the
trailing realized volatility of the momentum portfolio itself (not the market's) as the
scaling denominator. Their headline claim is that constant-volatility-targeted momentum
**roughly doubles the Sharpe ratio and essentially eliminates the crash episodes**,
because the scaling mechanically shrinks exposure in the run-up to a crash — momentum's
own volatility rises sharply before the worst drawdowns, so a vol-target rule de-risks the
position ahead of the event without needing to identify the crash state explicitly.
**M5 on this desk directly replicates BSC's direction and magnitude class**: vol-managed
WML (12% target, 2x leverage cap) moved Sharpe **0.77 → 1.29** and cut maxDD **83% → 29%**
— **"direction matches BSC 2015"** **[DESK, M5]**. That maxDD improvement (83% to 29%) is
the single most important number in this dossier for sizing purposes: it says vol-scaling
alone, with no explicit crash-state detection, removes the overwhelming majority of
momentum's worst-case tail on this desk's own India data.

**Daniel & Moskowitz's own solution** is a related but distinct dynamic-weighting scheme:
rather than targeting a constant volatility level, they scale the position using an
ex-ante forecast of the portfolio's own variance and skewness (built from lagged market
volatility and the market's trailing return), so sizing responds specifically to the
crash-conducive bear-rebound combination rather than to volatility generically. BSC's
rule is state-agnostic (any elevated momentum-return volatility triggers de-risking); DM's
own rule is state-aware (it targets the bear-rebound configuration specifically). M5
validates the BSC-style state-agnostic version; a DM-style state-aware overlay is a
distinct, not-yet-tested refinement (see §7).

## 3. Volatility effects beyond the crash state

The DM crash condition is a specific joint state (bear market *and* rebound *and* high
vol). A broader question is whether momentum is simply worse, on average, in high-vol
regimes generally — not only in the narrow rebound window. The literature answer is a
qualified yes, mediated through two related but distinct channels.

**Cooper, Gutierrez & Hameed (2004)**, "Market States and Momentum," *Journal of Finance*
59(3) **[LIT]**, is the market-state paper: sorting on the sign of the trailing 3-year
market return, they find momentum profits are **large and significant only following UP
markets**, and **insignificant-to-negative following DOWN markets**. This is a slower,
longer-horizon conditioning variable than DM's bear/rebound trigger (3-year trailing return
vs. DM's shorter bear-then-rebound window) and is best read as a complementary, not
identical, market-state filter: CGH says "don't expect momentum to pay off coming out of a
multi-year down market," which is consistent with, and arguably a coarser version of, the
DM mechanism.

**Stivers & Sun (2010)**, "Cross-Sectional Return Dispersion and Time Variation in Value
and Momentum Premiums," *Journal of Financial and Quantitative Analysis* 45(4) **[LIT,
hedge: direction carried with moderate confidence, effect size less so]**, find **higher
contemporaneous cross-sectional return dispersion predicts lower subsequent momentum
returns** — momentum bets that winners keep winning and losers keep losing in *relative*
terms, which works best when the cross-section behaves in an orderly, low-dispersion way;
when dispersion spikes (typically alongside market stress) the relative ranking reshuffles,
compressing or reversing the premium. The caveat: dispersion and market-level realized
volatility are themselves highly correlated in most samples, so this channel may be
substantially the same state as a realized-vol gate — a collinearity to test before
carrying both as separate switch-rule inputs (§7).

## 4. When to switch or stand down: what the literature actually supports

Assembling §§2–3 into practical rules, the literature supports a small number of
genuinely-evidenced switches, and this desk should resist inventing more:

**Post-bear-market, high-vol stand-down** (DM + CGH): reduce or exit momentum exposure
specifically in the state where a trailing decline has occurred and volatility is
elevated — this is the best-evidenced discrete switch in the literature, and it is the one
this desk has independently replicated three times (M2/M3/M4 above).

**Volatility-scaling, always-on** (BSC): unlike the discrete stand-down, constant-vol
targeting is a continuous sizing rule that runs at all times, not a state-conditional
switch — and it is the rule with the cleanest desk replication (M5: Sharpe 0.77→1.29,
maxDD 83%→29%). The two are complementary, not substitutes: vol-scaling shrinks exposure
smoothly as momentum's own volatility rises (which happens to correlate with the crash
state, since crashes are preceded by volatility spikes), while a discrete stand-down can
act faster and harder in the specific bear-rebound configuration that vol-scaling alone
may not fully anticipate.

**Blend with value, as a passive/structural hedge — not a timing device.** This desk's own
**VAL-D4** result is the sharpest evidence available anywhere in the register for this
point: on VW FF6 US data 1963–2020, corr(HML, UMD) = **-0.21**, and the 50/50 HML+UMD
blend Sharpe is **0.70** against HML alone **0.32** and UMD alone **0.54** — "**the AMP
prior HIT decisively**" **[DESK, VAL-D4]**. With QG-D2's already-booked HML+RMW blend
Sharpe of 0.49, VAL-D4 established that **"the value book's complements are MOMENTUM
first, PROFITABILITY second"** **[DESK, VAL-D4]**. But VAL-D4's own b5 cell is the
necessary honesty check: **worst-12m HML alone -35.1% vs. the HML+UMD blend -37.4% — "the
blend does NOT truncate the tail... complementarity is a SHARPE fact, not a
crash-protection fact; sizing and the drawdown governor still own the tail"** **[DESK,
VAL-D4]**. This is the single most important discipline point in this dossier: a
value+momentum blend raises average risk-adjusted return, and does nothing whatsoever to
cap the momentum-crash tail — the two problems (Sharpe improvement, crash protection) need
two separate mechanisms (a passive blend for the first, vol-scaling plus a discrete
stand-down for the second), and conflating them would be a design error.

**Factor momentum as a meta-signal.** **Ehsani & Linnainmaa (2022)**, "Factor Momentum and
the Momentum Factor," *Journal of Finance* 77(3) **[LIT, hedge: direction recalled with
moderate-high confidence, exact attribution percentages lower]**, argue standard
individual-stock (UMD) momentum is substantially explainable as a byproduct of momentum
*in factor returns themselves* — recently-good factors keep doing well, and stock momentum
loads on this because winners are disproportionately exposed to recently-winning factors.
**Gupta & Kelly (2019)**, "Factor Momentum Everywhere," *Journal of Financial Economics*
**[LIT, hedge]**, extend this cross-asset-class and find factor momentum pervasive and
largely distinct from stock-level momentum. Practical read: a plausible *additional*
meta-signal, one abstraction level removed from anything on this ledger, requiring its
own India factor-return series before use — a flagged research candidate, not a
switch-rule input, until tested directly (§7).

**What does NOT work: timing momentum by valuing the momentum portfolio itself.**
Attempts to build a value-style timing signal *on top of* momentum — some multiple or
spread describing how "cheap" or "expensive" the momentum long-short book currently is,
used to forecast its own forward return — are not, to this dossier's knowledge, a robust,
replicated finding the way BSC's vol-scaling or DM's state conditioning are **[LIT, hedge,
low confidence: this line of practitioner/academic inquiry (AQR-adjacent) is recalled as
generally unsupportive or inconclusive, without a specific citation — an open, largely
negative question, not an asserted null result]**. This is distinct from VAL-D4, which
blends value and momentum as separate exposures — the unsupported idea is valuing
momentum *itself* as a timing device. Naming this matters per CONTRACT §5: it is exactly
the kind of plausible-sounding construct that could get built and defended with "it
backtests well" — the unacceptable answer the CONTRACT rules out.

## 5. Costs and capacity

Momentum is, by construction, the highest-turnover standard equity factor: a 12-month
lookback with monthly rebalancing continuously rotates both legs, and the short (loser)
leg is disproportionately populated by the illiquid, high-spread, hard-to-borrow names
most expensive to trade. **Korajczyk & Sadka (2004)**, "Are Momentum Profits Robust to
Trading Costs?," *Journal of Finance* 59(3) **[LIT]**, model price impact as increasing in
trade size relative to volume and find momentum profits **substantially reduced, though
not eliminated, by realistic transaction costs**, with capacity (the AUM at which costs
drive returns to zero) **smaller than value's or size's**, precisely because of the
turnover/illiquid-leg combination.

**Frazzini, Israel & Moskowitz**, "Trading Costs of Asset Pricing Anomalies" (an AQR
working paper using the firm's own live execution data across factor strategies) **[LIT,
hedge: exact venue/year recalled with moderate confidence — VERIFY before citing a
specific date]**, is the other side of the question, and reaches a more optimistic
conclusion: using real trade-level execution data rather than the price-impact models
Korajczyk-Sadka-style papers rely on, realized trading costs for momentum are
**substantially lower than the academic literature's estimates**, because live execution
(patient trading, crossing networks, algorithmic slicing) achieves materially better fills
than a naive price-impact model assumes. The honest synthesis: momentum is genuinely the
most cost-sensitive standard factor (Korajczyk-Sadka's structural point stands), but the
haircut's size is model-dependent, and live-execution evidence says academic estimates
likely overstate the true cost. Neither paper is dismissed; both bound an answer that is
execution-quality-dependent, not knowable from a backtest alone.

**Implication for a monthly-rebalance India desk under STT.** India's Securities
Transaction Tax adds a fixed, per-trade drag, turnover-linear by construction — it taxes
every rotation regardless of how optimistic or pessimistic the impact estimate is. This
compounds directly with turnover-cost logic already booked: CONTRACT known prior #6 states
turnover costs run **~3.9% of NAV/yr at 500% one-way (~0.6% at 100%)**, and item #10 is
explicit that **"the moderate book's engine is the FACTOR book, not momentum — value/
quality run ~5× momentum's half-life, so cost ~1/5 the turnover per unit of authority."**
This literature review reinforces that frozen choice independently: momentum's highest
turnover plus a short leg concentrated in the illiquid names where impact and STT both
bite hardest means it belongs as a satellite sleeve inside the factor book, not the
moderate book's primary engine.

## 6. India

The desk's own India momentum evidence, from the M0–M5 battery on the IIMA WML series
(ingest/vault/factors, sha256-manifested): **M1** finds full-period India WML of **+13.4%/
yr at 24.5% volatility**, with **no mean decay** post-2015 (+13.2%/yr vs. +13.1%/yr
1994–2014) but **volatility roughly halved**, lifting Sharpe from **0.21 to 0.51** —
**[DESK, M1]**. The standing 25–35% forward decay haircut from CONTRACT §5 (McLean-Pontiff
discipline) stays unchanged regardless, since it prices *future* decay risk, not the
realized absence of decay to date. **M0**, the authentication cell, matched the India
mirror's worst-month chronology exactly against the published crash set (**Nov-2001
-27.6%, May-2009 -25.0%**) but recorded a genuine **MISS** on the pairwise correlation bar
(0.892 realized vs. the pre-stated 0.9 threshold) — accepted with a note, per this
program's own discipline that misses are recorded, not massaged, and bars are never moved
after a print **[DESK, M0]**. That May-2009 crash month is the same event M2's DM-conditional
split diagnoses directly: India's crash-zone months (trailing bear, subsequent market-up,
elevated vol) returned -2.24%/month against the same-state's-not-yet-rebounded bear&down
months at +3.93%/month **[DESK, M2]** — i.e., the desk's own authentication crash and its
own DM-mechanism replication are the same underlying 2009 event examined two different
ways, which is a genuine cross-check, not a coincidence.

Beyond the desk's own register, India momentum has a public, if anecdotal, live track
record: NSE introduced the **Nifty200 Momentum 30 Index** (combining 6- and 12-month price
momentum with risk-adjustment, launched circa 2019) **[LIT, hedge: existence and approximate
launch window recalled with moderate confidence, exact live-return figures not — VERIFY
against NSE's own factsheet]**, and several AMCs subsequently launched funds tracking it —
anecdotal confirmation that momentum is implementable at index scale in India, but not a
substitute for the desk's own IIMA-based M0–M5 evidence.

**The retail-flow interaction, an open question, not a finding.** India's post-2020 retail
surge (demat growth, discount broking, elevated F&O volumes) plausibly cuts both ways:
broader retail flow could amplify trend-chasing (strengthening continuation) or increase
herding-driven whipsaw (worsening DM's crash tail). M1's finding — mean premium steady
while volatility roughly halved post-2015 — is at least directionally inconsistent with a
"retail makes momentum crash harder" story over that window, but this is an observation
about one completed sub-period, flagged as interpretation, not a registered result.

## 7. The switch-rule design brief for this desk, and edge candidates

**Design brief.** A registrable switch-rule spec separates three layers kept distinct
throughout this dossier: (1) a continuous, always-on vol-scaling layer (BSC-style,
validated via M5); (2) a discrete stand-down gate for the DM/CGH bear-rebound-high-vol
state (validated three times over via M2/M3/M4, but as a *conditional split*, not yet a
*forward-looking trigger rule* with pre-registered thresholds); and (3) the value+momentum
blend (VAL-D4), a portfolio-construction decision made once at design time, never relied
on for tail protection given its own b5 result.

*State variables* (all as quantile ranks against their own trailing history, per CONTRACT
§6's no-magic-numbers rule — never a fixed level):
- **Trailing market-state rank**: the CGH-style trailing 24–36 month market return as a
  percentile rank against full history (India realized index data runs from 1993 — the
  backbone series with adequate sample length for a quantile rank, unlike any implied-vol
  series).
- **Realized-vol rank**: trailing realized volatility of the market, and separately of the
  momentum portfolio itself (BSC), each ranked against history since 1993. India VIX is
  vaulted only 2010–2023 — under 15 years, so it cannot carry a Tier-A threshold (CONTRACT
  §4: ≥30 observations) and is usable only as a *confirming* leg for the post-2010 window,
  with realized vol as the estimable-from-1993 backbone.
- **Momentum-portfolio own-volatility rank** (the direct BSC scaling denominator) —
  distinct from market-level vol, and already validated on this desk (M5).
- **Cross-sectional dispersion rank** (Stivers-Sun) — register and test for collinearity
  against the realized-vol rank before treating as independent; per §3 the two plausibly
  measure the same stress state, and §6 discipline argues against one regime as two inputs.

*Thresholds*: not fixed magnitudes but quantile bands (e.g., "bottom quartile of trailing
market return AND top quartile of realized vol, both by own-history rank") — the CONTRACT
§6 form ("sign tests, quantile ranks, long-anchor scalings"), sized only after a purged,
embargoed walk-forward test per CONTRACT §9, with the embargo scaled to the momentum
signal's own half-life, and counted honestly into the cumulative deflated-Sharpe trial
ledger before a single threshold is chosen (CONTRACT §9's true-trial-count discipline;
process note #6's library-not-inline-reimplementation rule applies to any vol/CV machinery
used, via `quant/stats/`).

*Data needed*: the IIMA WML series already vaulted (M0–M5's source); India realized
index-return history since 1993 (usable per CONTRACT environment notes); India VIX
2010–2023 (confirm leg only); a cross-sectional dispersion series which, given the artifact
below, must be built from a value-weighted or delisting-aware panel, never EW-survivor.

**The EW-panel momentum-inversion artifact — a standing measurement caveat, not a
momentum finding.** SC-D4, on the US firm panel (data_ml, equal-weight, no-delisting
survivor construction), found the size-conditional momentum spread **NEGATIVE at every
size quintile — small -24.52%/yr down to large -9.07%/yr — "losers win everywhere — the
EW monthly reversal artifact, NOT a momentum verdict"** **[DESK, SC-D4]**. Not an isolated
print: QG-D2, on the *same* construction, independently flagged **"c10/c13 momentum/vol
within-rows contradict the VW factor-level literature -> artifact-suspect, not consumed"**
**[DESK, QG-D2]** — two registered designs, two dates, two questions, the same mechanism
(an equal-weight, non-delisting panel manufactures a junk-bounce signature that inverts
the true cross-sectional momentum premium). Standing rule: **momentum evidence here is
trustworthy only from value-weighted factor-level data (UMD, as in VAL-D4/FUN-D10) or a
delisting-aware India panel once it lands — never an EW-survivor firm panel**, exactly
what this section's data plan is built to avoid.

**Edge candidates, with magnitudes and kill conditions:**

1. **Vol-scaled WML (BSC-style, always-on).** Magnitude: Sharpe roughly doubles per BSC
   **[LIT, hedge]**; **desk-replicated at 0.77→1.29, maxDD 83%→29%** **[DESK, M5]**. Kill
   condition: if a genuine walk-forward (not in-sample) test fails to at least halve
   realized maxDD relative to unscaled WML across a crash-inclusive out-of-sample window,
   retire as a standalone sleeve and keep only as a base risk-control layer.

2. **DM/CGH bear-rebound stand-down (discrete, conditional).** Magnitude: crash-zone
   returns of roughly -2 to -5%/month against +4 to +7%/month in the adjacent bear-and-
   down state, replicated on two panels **[DESK, M2/M3]**. Kill condition: needs ≥10
   independent India regime transitions before trust beyond a Tier-B/C prior (CONTRACT
   §4, §8's ban on regime-switching models with fewer than 10 transitions) — M2/M3/M4 are
   validated *descriptions* of history, not yet a *forward trigger rule* on India data.

3. **Intermediate-momentum tilt (12-7 over 6-2).** Magnitude: the 12-7 slice reproduces
   most of the 12-month premium in the US **[LIT]**. Kill condition: Goyal-Wahal's
   international non-replication **[LIT, hedge]** is a standing veto — do not adopt until
   the India IIMA panel's own 12-7 vs. 6-2 split is registered and printed; treat as
   US-sample-specific until then.

4. **Value+momentum blend as a passive Sharpe hedge (not a tail hedge).** Magnitude:
   Sharpe 0.70 blended vs. 0.32 (HML)/0.54 (UMD) **[DESK, VAL-D4]**. Explicit non-kill
   caveat already booked: worst-12m of the blend (-37.4%) is *worse* than HML alone
   (-35.1%) **[DESK, VAL-D4]** — this candidate is admitted for Sharpe improvement only;
   any design that leans on it for drawdown control is mis-specified by the desk's own
   printed evidence.

5. **Rate-regime conditioning of the momentum sleeve.** Explicitly **refused**: FUN-D10
   found UMD's rising-vs-falling regime split at **+0.38pp — essentially flat**, against
   HML's **-3.84pp** and the market's era-fragile, sign-flipping split **[DESK, FUN-D10]**.
   This is a genuine, useful negative result: momentum needs no monetary-regime
   conditioning at all, freeing that design slot for the market-state/vol-rank variables
   above rather than RBI repo direction.

6. **Cross-sectional dispersion gate (Stivers-Sun).** Magnitude: directional only, no
   specific figure carried with confidence **[LIT, hedge, low confidence]**. Kill
   condition: if found highly collinear with the realized-vol rank on Indian data (likely),
   drop as a redundant state variable rather than double-count one regime as two inputs.

7. **Factor momentum (Ehsani-Linnainmaa / Gupta-Kelly) as a meta-signal.** Flagged
   research-only, not registrable today: requires its own adequately-long India factor
   return series before even a Tier-B read is possible **[LIT, hedge]**.

8. **Valuation-of-the-momentum-portfolio timing.** Not adopted. No robust supporting
   evidence recalled with confidence **[LIT, hedge, low confidence — largely negative/
   inconclusive as best recollected]**; named here to close off a plausible-sounding but
   empirically unsupported construct, per CONTRACT §5's discipline against "it backtests
   well" as an acceptable survival argument.
