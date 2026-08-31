# Dossier 04 — Drawdown Control Machinery

Workstream: layered risk stack (vol targeting, trend/TSMOM filters, options, fast triggers,
re-entry/hysteresis, drawdown-control theory) mapped to the frozen constraint: portfolio maxDD
below Nifty 50's in every episode where the index falls >20% (flash-crash exclusion per
OPEN_QUESTIONS default #5: recovery of the pre-fall peak within ~63 trading days of the trough
excludes an episode), absolute ceiling 30–35%, while running mid/small downside beta ~1.1–1.3 and
state-contingent leverage averaging 1.10–1.15x.

Research-only. No backtests were run; every number below is either a verified literature figure,
a verified public-record India data point, or an explicitly labeled illustrative estimate awaiting
data-phase calibration.

---

## 1. Findings and literature

**Volatility targeting**

1. Moreira & Muir (2017), "Volatility-Managed Portfolios," *Journal of Finance* 72(4): 1611–1644
   [verified]. Scaling exposure by the inverse of trailing realized volatility raises Sharpe ratios
   and delivers large utility gains across the market, value, momentum, profitability, RoE,
   investment factors and the currency carry trade, because volatility changes are *not* offset by
   proportional changes in expected returns — vol is more persistent/forecastable than the
   conditional Sharpe ratio. The managed portfolio mechanically takes less risk in recessions.
   Effect size: reported Sharpe-ratio gains are economically large (roughly 30–50% relative
   improvement across the factors tested, varying by factor) [verified for direction and mechanism;
   the precise per-factor Sharpe deltas were not re-extracted from the full text this pass —
   VERIFY exact figures].

2. Harvey, Hoyle, Korgaonkar, Rattray, Sargaison & van Hemert (2018), "The Impact of Volatility
   Targeting," *Journal of Portfolio Management* 45(1): 14–33 [verified]. Tested on 60 assets with
   daily data back to 1926 (equities, bonds, currencies, commodities), 10% vol target. **Key
   asset-class split, directly load-bearing for this workstream**: the Sharpe-ratio benefit of vol
   targeting is material for equities and credit (linked to the leverage effect — vol and forward
   returns are negatively correlated for these asset classes) but *negligible* for bonds, currencies
   and commodities. Independent of the Sharpe result, vol targeting reduces the severity of
   left-tail (crash) outcomes **across every asset class tested**, because left tails cluster in
   high-vol periods when a vol-targeted book already holds reduced notional. This is the single most
   important verified finding for our design: it licenses vol targeting as a *risk-reduction* tool
   even where it does not raise Sharpe, and confirms equities (our dominant sleeve) are exactly the
   asset class where it earns its keep on both counts.

3. Barroso & Santa-Clara (2015), "Momentum Has Its Moments," *Journal of Financial Economics*
   116(1) [verified]. Scaling a momentum strategy by the inverse of its trailing 6-month realized
   volatility "virtually eliminates" momentum crashes and raises the Sharpe ratio from 0.53
   (unmanaged) to 0.97 (managed) in their US sample. This is the clean empirical analogue for
   applying the same inverse-vol scaling logic to a *trend/momentum-driven* exposure rather than to
   raw market beta — relevant because our mid/small tilt is itself a momentum-adjacent, high-vol
   exposure.

**Trend / time-series momentum as a risk filter**

4. Faber (2007), "A Quantitative Approach to Tactical Asset Allocation," *Journal of Wealth
   Management* [verified]. Simple 10-month SMA (~200 trading days) timing rule on five US asset
   classes, 1972–2005: reported Sharpe 0.81, CAGR 11.7%, maxDD 9.5%, vs. much deeper drawdowns
   buy-and-hold. This is the archetype "sign rule" the contract's "no magic numbers" clause
   endorses (price above/below a long moving average, not a fixed % threshold) — but it is a single,
   heavily-mined US backtest from 20 years ago; **treat its point drawdown numbers as maximally
   decayed** (see §3).

5. Moskowitz, Ooi & Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics*
   104(2): 228–250 [verified]. Documents time-series momentum (sign of own past 12-month return
   predicts next-month return) across 58 liquid futures instruments spanning equities, currencies,
   commodities and bonds; the diversified TSMOM portfolio performs best in extreme markets
   (crisis-alpha property) and has low correlation to standard factors.

6. Hurst, Ooi & Pedersen (2017), "A Century of Evidence on Trend-Following Investing," *Journal of
   Portfolio Management*, published via AQR [verified]. Extends TSMOM evidence back to 1880.
   Positive average returns in every decade since 1880; performed well in 8 of the 10 largest
   drawdown episodes for a 60/40 portfolio across the century — i.e., trend is a **slow-bear /
   sustained-crisis** hedge, not a single-day crash hedge, because it needs the trend to actually
   *develop* over weeks before the filter reacts.

7. Zakamulin, "Market Timing with Moving Averages: The Anatomy and Performance of Trading Rules"
   (book/SSRN working paper; also summarized in *Journal of Asset Management*, "The real-life
   performance of market timing with moving average and time-series momentum rules," 2014)
   [verified]. Two structural, load-bearing findings: (a) a single moving-average rule cannot
   escape the lag-vs-noise trade-off — shortening the average reduces lag but multiplies false
   ("whipsaw") signals, lengthening it does the opposite, and no parameter choice dominates; (b)
   moving-average crossover / band techniques trade some of that noise for *more* lag, they do not
   remove the trade-off. Out-of-sample testing on the S&P from 1870–2010 debunks several
   "moving-average timing beats buy-and-hold for free" claims — timing rules earn their keep mainly
   by cutting left-tail severity, not by raising the raw mean return, which is consistent with the
   vol-targeting literature above.

**Options / tail hedging**

8. Israelov (2017), "Pathetic Protection: The Elusive Benefits of Protective Puts," *Journal of
   Alternative Investments* 21(3): 6 (AQR) [verified]. Central, load-bearing, counter-intuitive
   finding: unless the purchase and maturity of a protective put is timed almost exactly around the
   drawdown, a protective-put overlay is frequently **worse** than the simple alternative of
   statically reducing (de-grossing) exposure to the underlying by an equivalent amount — it can
   increase both drawdown and volatility per unit of expected return relative to a plain notional
   cut. Tested against simulated put-protected portfolios and the CBOE S&P 500 5%-Put-Protection
   Index. Direct implication: a *permanently-on* put overlay is not obviously superior to a
   *vol-targeted leverage cut* of the same average size — the two must be compared on the same
   metric, not assumed complementary.

9. Israelov & Nielsen (2015), "Still Not Cheap: Portfolio Protection in Calm Markets," *Journal of
   Portfolio Management* 41(4): 108–120 (AQR) [verified]. Across ten global equity indices, it is
   the **volatility risk premium** (implied minus subsequent realized vol), not the absolute level
   of implied vol, that determines whether protection is actually cheap. Even in calm periods, when
   implied vol has been drifting up, subsequent realized vol tends to undershoot the implied level
   at purchase — the VRP is structurally positive and persistent, so "buy protection when VIX looks
   low" does not reliably work as a cost-timing rule.

10. AQR, "Tail Risk Hedging: Contrasting Put and Trend Strategies" (white paper; also appears as
    "Journal of Systematic Investing," Vol. 1, Issue 1, Feb 2021) [verified via title/venue search].
    Puts have a persistently negative standalone expected return (the cost of the valuable
    crash-time payoff) and become *more* expensive exactly when investors most want them (implied
    vol/skew richen with realized stress). AQR's own preference, net of these effects, tilts toward
    trend-following over discretionary put-timing as the primary tail-hedge sleeve, for cost and
    robustness reasons — though they note both approaches have merit and the "puts protect
    better/cost more" intuition is directionally correct. [The exact quantitative payoff/cost table
    in this paper was not independently re-extracted this pass — VERIFY specific figures before
    quoting numbers from it.]

11. The general "richness spikes exactly when insurance is most wanted" mechanism (sometimes
    summarized as "don't buy insurance when it's most expensive," associated with Ilmanen's writing
    on tail hedging, e.g. AQR/CFA-adjacent commentary) is corroborated by the same VRP result in
    finding 9 — implied vol and skew both richen contemporaneously with realized stress, so
    reactive, undisciplined put-buying after a shock is close to the worst-timed purchase point.
    [The exact Ilmanen title/venue for this specific framing was not pinned down to a single
    verified citation this pass — treat as a well-supported mechanism, not a single quotable paper —
    VERIFY.]

**Drawdown-control theory**

12. Grossman & Zhou (1993), "Optimal Investment Strategies for Controlling Drawdowns," *Mathematical
    Finance* 3: 241–276 [verified]. For a CRRA investor constrained to never lose more than a fixed
    fraction α of the running maximum of wealth, the optimal risky-asset holding at time *t* is
    proportional to the **surplus** `W(t) − α·M(t)`, where `M(t)` is the running peak of wealth. This
    is precisely a CPPI-style "cushion" rule and is the cleanest theoretical anchor for a
    leverage-as-function-of-state design: exposure should scale with distance-from-peak, not with a
    fixed calendar or a fixed drawdown threshold.
    **Caveat found in the same search**: Klass & Nowicki (2005), "The Grossman and Zhou investment
    strategy is not always optimal," show the continuous-time optimum is not always optimal once the
    problem is discretized — i.e., in a market that trades in discrete time with possible gaps
    (exactly India's circuit-halt reality, see §2), the closed-form surplus rule can be beaten or can
    breach the floor. Cvitanic & Karatzas (1995) extend to multi-asset, Cherny & Obloj (2013) to a
    general semimartingale setting [both mentioned only in a secondary citation-history snippet —
    VERIFY: titles/venues not independently confirmed by a dedicated search this pass]. **Design
    conclusion**: use Grossman-Zhou as the functional *form* (surplus-over-peak scaling) for the
    leverage-as-function-of-state rule, not as an exact optimal-control implementation to trust
    mechanically through a gap day.

---

## 2. India-specific evidence

**Nifty 50 drawdown history (the benchmark the constraint is measured against).** Episode-by-episode,
peak-to-trough, from public sources:

| Episode | Peak→trough | Duration | Recovery | Note |
|---|---|---|---|---|
| 2008 GFC | ≈ −55% to −64% | ~10 months | ~5 years | Range reflects different cited peak (Jan-2008 ~6357) / trough (Oct/Nov-2008 ~2253) pairs across sources; multiple independent public sources agree on the order of magnitude [verified, single episode so n=1 but high point-value confidence] |
| 2010–11 Eurozone/domestic policy | ≈ −28% | ~13 months | ~24 months (720 days post-trough) | [verified] |
| 2013 taper tantrum | ≈ −16 to −18% (illustrative, from ~6229 May-2013 to ~5119 Aug-2013) | ~3 months | — | **[VERIFY: exact peak/trough dates and % not independently confirmed this pass — search budget exhausted]**; only independently verified data point is a single day, Nifty −1.83% on 21-Aug-2013 on FII outflows [verified] |
| 2015–16 China-linked selloff | ≈ −25% (illustrative, ~9119 Mar-2015 to ~6825 Feb-2016) | ~11 months | — | **[VERIFY]**; independently verified: concurrent Shanghai Composite fell 43% in ~2 months (Jun–Aug 2015) [verified], and Nifty recorded its steepest single-day fall "in over four months" on the Jan-2016 China sell-off day [verified] |
| 2018 IL&FS/NBFC crisis | Nifty 50 itself only ≈ −15% (Aug→Oct 2018, ~11760→~10000); Midcap ≈ −19 to −30%; **Smallcap ≈ −32%** | Nifty ~2 months; SMID correction ran ~2 years | Nifty ~8 months; SMID much longer | [verified]. **Critical for our mandate**: the index-level (Nifty 50) drawdown *understates* what an actual mid/small-tilted book experienced by roughly 2x — this is direct evidence for the downside-beta 1.1–1.3 assumption and confirms the DD constraint (measured vs Nifty 50) is a genuinely binding, not cosmetic, target for a mid/small book |
| Feb–Mar 2020 COVID | **−38.4%**, 69 trading days | 69 days | 231 days | [verified]. Broadly consistent with, though not identical to, the CONTRACT's own prior-pass figure "Mar-2020 ≈ −36%" for a **levered portfolio** simulation (a different object — see note below) |
| 2024–25 SMID correction | Nifty ≈ −17% (illustrative, ~26277 Sep-2024 to ~21743 Mar-2025); midcap/smallcap materially worse, explicitly compared by financial press to the 2018 correction | ~6 months | — | **[VERIFY: inferred from an article title only, not independently confirmed this pass]** |
| 2026 stress (post knowledge-cutoff) | Not analyzed | — | — | A search result dated 22-May-2026 references a rupee/market stress event serious enough for commentary to invoke the 2013 taper-tantrum playbook. This event is **entirely outside this analyst's knowledge** (cutoff Jan-2026) and was not investigated further before the search budget was exhausted. **This is the single most important open item in this dossier**: the data phase must pull the full 2026 episode (Nifty drawdown, INR move, VIX behavior, circuit-breaker activity) before the flash-crash exclusion rule and the fast-trigger design are finalized, since it is the most recent live test of exactly this machinery. |

Note on the CONTRACT's own prior figures: "2008 at 1.25x ≈ −58%; Mar-2020 ≈ −36%" (CONTRACT §7.4) describe a **simulated levered portfolio**, not raw Nifty 50 — they are not directly comparable to the raw-index numbers in the table above (which is why 1.25× scaling of the raw Nifty numbers does not reconcile arithmetically with those two figures; the portfolio simulation embeds a downside-beta and partial-risk-control assumption this dossier does not have visibility into). Both sets of numbers are retained; the raw-index table above is this dossier's independently sourced contribution.

**India VIX** [verified via NSE white paper search + market commentary]. Computed CBOE-style (cubic-spline interpolation of near/next-month Nifty option best bid-ask quotes) to represent expected 30-calendar-day volatility; free, downloadable historically from NSE. During the Feb–Mar 2020 crash, India VIX rose from ~25 to ~64 within days and touched an intraday extreme near 80–87 by 23-Mar-2020, remaining above 60 for nearly a month. India VIX moves inversely with Nifty essentially by construction (put demand rises as spot falls) — this makes VIX-level or VIX-jump triggers **contemporaneous-to-slightly-leading at a same-day/1–2-day horizon**, not a multi-week early-warning signal; this follows directly from the vol-clustering mechanism already verified in findings 1–2 above, and is consistent with the general academic view that VIX is a coincident stress indicator rather than a forward-predictive one at longer horizons. Exact average India-specific VRP magnitude and skew steepness were **not verified this pass** — flagged for data-phase estimation directly from NSE's free historical India-VIX series against realized Nifty vol.

**Market-wide circuit breakers** [verified via SEBI circular search]. Since 2001 (SEBI circular, amended 2013), a 10%/15%/20% move in either the Sensex or the Nifty 50 (whichever breaches first) triggers a **coordinated, nationwide trading halt across both cash equity and equity-derivative markets simultaneously** — not just the underlying. This is structurally decisive for the "options vs futures de-grossing" question (§3, §4): on a circuit-halt day, index *futures* cannot be traded to de-gross, by definition, for the halt's duration; a **pre-existing** long option position, being European-style and cash-settled against a closing/settlement price rather than requiring an intraday trade, continues to provide its convex payoff through the halt. Individual-stock circuit filters (2/5/10/20% bands, tighter for less liquid/surveillance-flagged names) [verified] compound this: a mid/small name in the aggressive book can be un-tradeable at any price on its worst day, which is additional, uninsurable, name-level gap risk that a portfolio-level index hedge cannot reach.

**Surveillance frameworks (ASM/GSM) and the F&O ban mechanism** [general market-structure knowledge, not independently re-verified this pass — VERIFY current stage thresholds]. SEBI's Graded Surveillance Measure (GSM) and Additional Surveillance Measure (ASM) frameworks place stocks showing abnormal price/volume behavior into escalating stages carrying 100%-upfront margining and, at higher stages, trade-for-trade (no intraday netting) settlement — i.e., exactly the mid/small names the aggressive book is tilted toward can become the hardest to size, enter, or exit quickly precisely when they are most volatile. Separately, single-stock derivatives enter a **ban period** (no new positions, unwind-only) once open interest exceeds 95% of the exchange's market-wide position limit — a constraint that structurally cannot apply to the Nifty/Bank Nifty *index* contracts. Both facts are independent, mechanism-level arguments (not merely OPEN_QUESTIONS' stated preference) for restricting the leverage instrument to index futures (default #3) and the hedge instrument set to index options/futures (default #4): single-stock hedging capacity in the exact names most in need of it can vanish by regulatory design at the worst time.

**SAST 5% disclosure trigger** [general regulatory knowledge — VERIFY exact current regulation number/threshold]. SEBI's Substantial Acquisition of Shares and Takeovers framework requires disclosure on crossing 5% ownership in a listed company. Combined with typically low free float in many mid/small names, this reinforces promoter-concentration-driven thin liquidity in exactly the tail of the universe (ranks 500–750) the aggressive book is licensed to hold — another structural amplifier of downside beta in a genuine bear, independent of any signal decay argument.

**Free India-specific data sources for this workstream** (per CONTRACT's free-data list): NSE bhavcopy (daily OHLC + FII/DII/derivatives data) for realized vol and gap-distribution estimation; NSE's historical India VIX archive for implied-vol time series; NSDL's daily FPI/FII flow disclosure for a funding/flow-based fast-trigger candidate; CCIL for money-market/repo spread data as a funding-stress trigger (natural pairing with the credit/financial-cycle dossier's leading indicators); AMFI for mutual-fund (DII) flow data. All are free and already on the CONTRACT's approved list — no new source is required for this workstream's parameters.

---

## 3. Decay and crowding assessment

**Volatility targeting (equity sleeve).** Survival argument: (i) structural/behavioral — the
negative vol/expected-return correlation (leverage effect) that drives the Harvey et al. and
Moreira-Muir results is a feature of *how equity prices are formed* (debt-to-equity ratio rises
mechanically as prices fall, and investor risk aversion rises with realized stress); it is not an
arbitrageable mispricing that crowding erodes the way a return-predicting signal is eroded — and
(iv) institutional constraint — most Indian equity mutual funds (the natural competing capital)
operate under SEBI mandates requiring near-full equity investment at all times, so they structurally
cannot compete away a systematic degrossing edge even if they wanted to. **Decay assumption: low.**
This is a risk-shape tool, not an alpha-decay-prone anomaly; no numeric haircut is proposed on the
DD-reduction *mechanism* itself, though the **Sharpe-ratio benefit specific to India** (as opposed to
the tail-reduction benefit, which the literature finds asset-class-universal) is untested locally and
should be treated with the standard McLean-Pontiff-style caution (26%/58% haircut) until an
India-specific replication exists in the data phase.

**Trend/TSMOM as a slow-bear de-risking filter.** Survival argument: (i) behavioral
under-reaction/delayed over-reaction (Moskowitz-Ooi-Pedersen) plus (iii) a genuine risk premium for
providing "crisis liquidity" the trend-follower is paid to supply by being short/underweight risk
exactly when others are forced sellers (Hurst-Ooi-Pedersen's crisis-alpha finding). Both mechanisms
are multi-decade, multi-asset-class, and — critically for the contract's Tier system — **this
workstream only proposes to use trend as a reduce-only overlay** (cut gross on a trend break; never
add leverage on a trend confirmation beyond the state-contingent leverage cap), which is exactly the
CONTRACT's Tier-C license ("Tier-C signals may only REDUCE risk"). That lowers the evidence bar this
particular *use* of trend needs to clear. The genuine, quantified cost is **whipsaw** — and Zakamulin's
lag-vs-noise result is a hard mathematical constraint, not an estimation artifact: no lookback choice
escapes it. In a structurally high-drift market like India (multi-decade positive nominal-GDP-driven
equity drift), a short/medium lookback trend filter will generate a *higher false-positive rate* per
unit of true slow-bear signal than in a flatter market, because minor corrections that reverse are
more common relative to genuine multi-month bear starts when the unconditional drift is positive.
**Decay assumption / haircut**: no single verified TSMOM-specific decay statistic for India was found
this pass; absent one, apply the CONTRACT's generic McLean-Pontiff decay band (26% conservative /
58% aggressive) to any *return* attributed to the trend filter, but treat its *whipsaw-cost* estimate
as the primary design lever (a longer, cycle-anchored lookback — pairing with the slower cycle
dossiers rather than a fast technical trigger — is the correct response to a high-drift whipsaw
problem, not a shorter one).

**Options / VRP.** This is not really a decaying "edge" in the alpha sense at all — it was never
priced as free money; Israelov-Nielsen's finding is that the volatility risk premium is essentially
**always positive and persistent** (a genuine, structural risk premium, survival category (iii): the
short side is paid to bear tail risk that risk-averse capital structurally wants to offload, and this
has not been arbitraged away globally in decades of documented VRP studies). The correct design
response is therefore *not* to assume the cost will decay favorably, but to (a) treat the VRP as a
permanent, budgeted expected-cost line, and (b) minimize how much of it is paid by making the hedge
**state-contingent** (regime-gated, per §4) rather than permanently on — since Israelov (2017) shows a
permanently-on put overlay is often dominated by a plain notional cut of equal average size, and
Israelov-Nielsen (2015) shows waiting for "cheap" VIX readings does not reliably reduce the cost
either. **Decay assumption: none downward — if anything, expect India-specific VRP to *compress* as
retail options volumes have grown enormously in India in recent years (post-2019), which would raise
the effective cost of buying protection relative to older estimates; flagged as a data-phase question,
not assumed either way.**

**Fast triggers (realized-vol jump, VIX term structure, funding spreads).** Survival argument: (iii)
genuine information — vol clustering and funding stress are real, economically-grounded phenomena,
not statistical artifacts, so a same-day/short-lag reactive trigger is not "decaying" in the
anomaly sense. But as **forecasting** tools (as opposed to reactive triggers) their lead time is short
(same-day to a few days at best per the March-2020 VIX evidence, §2), so the design must not overclaim
predictive power — treat these strictly as fast, reactive "cut gross now" switches, never as
"call the top three weeks early" signals. The genuine cost to haircut is the **false-positive
(whipsaw) rate of the trigger itself**, which requires counting actual historical trigger events in
India — a data-phase task (see §6), gated by the CONTRACT's "no regime-switching model without ≥10
observed transitions" trap.

**Grossman-Zhou surplus-based leverage rule.** This is a mathematical theorem, not an empirical
anomaly, so "decay" does not apply to the functional form itself — but two things must be haircut:
(a) the Klass-Nowicki finding that continuous-time optimality does not transfer exactly to discrete,
gap-prone markets (exactly India's circuit-halt structure), and (b) any *calibrated parameter*
(the α floor ratio, the risk-aversion coefficient) fitted to Indian data is subject to the normal
small-sample cautions in §5. **Design response**: use the surplus-scaling *shape* with wide,
sensitivity-robust bands, not a single fitted α.

---

## 4. Proposed parameters

All values below are **forms and ranges**, not point thresholds, per the CONTRACT's "no magic
numbers" rule. Where a specific number appears, it is either a CONTRACT-frozen prior (cited as such)
or an explicitly-labeled illustrative anchor for the *shape* of the rule, not a fitted constant.

**Effective-beta arithmetic (the core identity tying every knob to the constraint).**

```
EffectiveBeta(regime) = DownsideBetaTilt × Leverage(regime) × [1 − HedgeRatio(regime) × HedgeEffectiveness(regime)]
PortfolioDD(episode) ≈ EffectiveBeta(regime-path) × NiftyDD(episode) + IrreducibleGapFloor
```

- `DownsideBetaTilt` ≈ 1.1–1.3 (CONTRACT prior, mid/small tilt).
- `Leverage(regime)` — state-contingent, averaging 1.10–1.15x (CONTRACT prior), but *ranging* from a
  vol-targeted floor near 0.5–0.7x in confirmed stress states up to the 1.5x gross cap in benign,
  cycle-favorable states (never breaching the hard cap).
- `HedgeRatio(regime)` — the CONTRACT's own frozen sweep grid: {0, 25, 50, 75, 100, 125, 150%},
  swept **jointly** with the regime that selects it (never fit independently, per CONTRACT §3).
- `HedgeEffectiveness(regime)` — a discount for basis risk (index hedge vs. mid/small book),
  option-delta/convexity mismatch, and gap risk; illustratively 0.6–0.75 in a slow bear (hedge has
  time to be rebalanced/rolled) and 0.45–0.6 in a genuine fast crash (circuit halts and gaps erode
  the hedge's realized effectiveness relative to its theoretical delta) — **Tier C illustrative,
  pending data-phase estimation from the historical gap distribution.**
- `IrreducibleGapFloor` ≈ 8–12% (CONTRACT prior pass, "fast crashes... 8–12% irreducible" — this
  dossier's circuit-breaker and options-settlement evidence in §2 supports the mechanism behind this
  number: a genuinely fast, no-prior-signal crash occurs faster than any reactive trigger, futures
  de-grossing, or intraday hedge adjustment can respond, and individual-name circuit locks can make
  even a partial cash-call impossible to execute in full on the worst day).

Worked illustration (Tier C, illustrative only — the actual regime-bucket values are a data-phase
estimation task, §6):

| Regime | Leverage | HedgeRatio | HedgeEffectiveness | EffectiveBeta | Comment |
|---|---|---|---|---|---|
| Normal (no signal fired) | 1.125x (CONTRACT avg) | 0% | — | ≈1.35 | Worse than Nifty on a naive basis — the whole point of the risk stack is that the system must *not* remain in this state through a qualifying >20% Nifty fall |
| Slow-bear confirmed (trend layer flips, vol elevated not extreme) | ~0.75x | ~50–75% | ~0.65 | ≈0.5–0.6 | Meaningful headroom below Nifty's own DD |
| Fast/tail trigger fired (vol-jump + VIX backwardation + circuit activity) | ~0.5–0.6x | ~75–100%+ (tail cap ≤75% notional, jointly with leverage cut) | ~0.5 | ≈0.25–0.35, **plus** the additive 8–12% gap floor | This is the regime the fast-trigger layer exists to reach *fast enough* |

**Leverage-as-function-of-state form**: `Leverage(t) = clip(L_base × f(Surplus(t)), L_floor, L_cap)`
where `Surplus(t) = [NAV(t) − α·Peak(t)] / NAV(t)` (Grossman-Zhou shape) and `f` is monotone
increasing in surplus — a CPPI-family cushion rule, not a fixed-threshold switch. `α` itself should
be swept, not fitted to a point (see §6), and `L_cap` is bound by the mandate's 1.5x gross ceiling
regardless of what the cushion rule would otherwise output.

**Hedge-ratio-by-regime sweep design**: cross the CONTRACT's frozen 7-point hedge-ratio grid against
a small number of *independently-defined* regime buckets (target: 3–4 buckets, e.g. "benign,"
"elevated-vol slow-bear," "tail/fast-crash," possibly a fourth "post-crash recovering" bucket for the
re-entry design below) built from (a) the slow trend/cycle state (fed by the cycle dossiers, not
re-derived here) and (b) the fast vol/VIX/funding trigger state (§4 below). This yields at most a
~28-cell design (7 hedge levels × 4 regimes) — the CONTRACT's own worked example of "the 7-point hedge
sweep × regime grid" (§9) — and the deflated-Sharpe true-trial-count requirement in the estimation
standards applies to the **entire grid**, not to the best cell found.

**Fast-trigger form** (realized-vol jump / VIX term structure / funding spread — all rank/quantile
based, no fixed level): fire a "cut gross" state when (a) a short-window realized-vol measure crosses
above its own trailing long-window percentile rank (e.g., "current 5–10 day realized vol in the top
decile of its trailing 1-year distribution" — a quantile rule, not a fixed vol number, so it
auto-adapts as India's baseline vol regime shifts over the multi-year sample), **confirmed by** (b)
India VIX term-structure inversion (near-dated implied vol above further-dated — backwardation is
itself a well-documented stress signature, requiring no fixed VIX level), **or** (c) a funding/flow
stress proxy (CCIL repo/CP spread widening beyond its own trailing rank, or a sustained multi-day FII
outflow run via NSDL data beyond its trailing rank) firing independently as a second, potentially
earlier-leading channel — motivated by 2018's funding-first character (§2) and naturally paired with
the credit/financial-cycle dossier's leading indicators.

**Cash-call trigger and re-entry rule** (per OPEN_QUESTIONS default #8: hysteresis band + 2–3 staged
tranches): de-risk trigger uses the *tighter* (entry) band of a two-band hysteresis system; re-entry
requires the *wider* (exit) band to be recrossed — mechanically identical to the "no-trade zone"
device Zakamulin analyzes for MA-crossover whipsaw reduction, applied here to the vol/state trigger
rather than to a price moving average. Re-entry is staged across 2–3 tranches (e.g., roughly a third
of the previously-cut exposure restored at each successive confirmation step, spaced by a minimum
number of sessions tied to the signal's own half-life) rather than restored in one step, so that a
single-point signal reversal cannot fully re-lever the book into a renewed leg down. The Grossman-Zhou
surplus rule provides the natural mechanical hysteresis for the *leverage* component specifically,
since the running peak `M(t)` only resets upward, never downward, on its own.

**Provenance table**

| Name | Value / range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Downside beta (mid/small tilt) | 1.1–1.3 | CONTRACT prior (data-derived) | B | high | n/a — structural, reinforced by 2018 index-vs-SMID gap in §2 | A data-phase re-estimate on the actual Nifty 750 ranks 500–750 universe |
| State-contingent leverage average | 1.10–1.15x agg / ~1.05x moderate | CONTRACT prior (data-derived) | B | high | n/a — mechanical constraint, not an alpha | Data-phase simulation of the leverage rule against 2008/2011/2018/2020 |
| Vol-targeting DD-reduction mechanism (equities) | qualitative: reduces left-tail severity | Harvey et al. (2018); Moreira-Muir (2017) | A globally (60 assets, ~90 yrs); B for India specifically | high (mechanism), medium (India magnitude) | low — structural/behavioral, reinforced by mandated-long-only competing capital | An India-specific replication finding equities do *not* show the leverage effect (would be surprising, not expected) |
| Vol-targeting Sharpe benefit | material for equity/credit; negligible for bonds/FX/commodities | Harvey et al. (2018) | A | high | low for the asset-class split itself; McLean-Pontiff 26–58% band for the India-specific point estimate until replicated | India-specific replication |
| Trend filter lookback (slow, de-risk-only) | long/cycle-anchored (e.g. multi-quarter), not a short technical window | Zakamulin (whipsaw trade-off); Hurst-Ooi-Pedersen (slow-bear crisis alpha) | B | medium | McLean-Pontiff 26–58% band on any *return* attributed to it; whipsaw-cost is the binding design constraint, not decay | A measured India-specific whipsaw rate at each candidate lookback (data phase) |
| Hedge-ratio grid | {0,25,50,75,100,125,150%} jointly with regime | CONTRACT frozen config | — (config, not an empirical estimate) | — | n/a | Principal override only |
| Options notional caps | ≤50% directional / ≤75% tail | CONTRACT frozen mandate | — | — | n/a | Principal override only |
| VRP / option-protection cost | globally positive, persistent (magnitude not India-verified) | Israelov & Nielsen (2015) | A globally; C for India (no verified India-specific magnitude this pass) | medium | none downward; possible *compression* risk from India's post-2019 retail options boom (untested direction) | NSE India-VIX-vs-realized-vol time series, data phase |
| Protective-put vs. static de-gross ranking | static de-gross often ≥ naive permanently-on puts | Israelov (2017) | A globally | high (mechanism) | n/a — this is a comparative-design finding, not a decaying edge | An India-specific replication using Nifty options data |
| Fast-trigger lead time (vol/VIX) | same-day to ~1–2 days, reactive not predictive | March-2020 India VIX behavior (this dossier, §2) + general vol-clustering literature | B (n=1 well-documented India episode; A-level globally for the *mechanism*) | medium | n/a (reactive-trigger design, not a forecast) | A full multi-episode (2008/2011/2013/2015-16/2018/2020/2026) lead-lag table — top data-phase priority |
| Circuit-halt / gap-risk floor | 8–12% irreducible | CONTRACT prior pass, reinforced by this dossier's circuit-breaker mechanism evidence (§2) | C (n<4 genuine fast-crash observations in India) | medium | Tier-C: reduce-only license applies — used to justify a permanent minimum options budget, never to add risk | A full accounting of every India circuit-halt/lock day 1996–2026, incl. the 2026 episode |
| Hedge effectiveness discount (basis + gap risk) | ~0.6–0.75 slow-bear / ~0.45–0.6 fast-crash | Illustrative, this dossier | C | low | n/a — parameter to estimate, not a decaying edge | Historical basis-risk measurement (Nifty/Bank Nifty hedge vs. SMID book returns) + historical single-day gap distribution from bhavcopy |
| Re-entry hysteresis band + staged tranches | 2–3 tranches, band width scaled to signal vol, not fixed % | OPEN_QUESTIONS default #8; mechanism per Zakamulin's no-trade-zone analysis | B (mechanism); C (India calibration) | medium | n/a | Count of actual India regime transitions since 1996 (data phase; gated by the ≥10-transition trap) |

---

## 5. Evidence-tier recommendations

- **Vol targeting mechanism (equities, tail-reduction effect)**: **Tier A globally** — Harvey et al.
  test 60 assets over up to ~90 years; the equity/credit-specific leverage-effect result and the
  universal left-tail-reduction result both clear the ≥30-observation bar comfortably at the
  cross-asset/cross-decade level. **Tier B for India specifically** until replicated locally (India
  offers a handful of major vol regimes since 1996 — well under 30 independent India-only
  observations).
- **Vol targeting Sharpe benefit, asset-class split**: **Tier A** as a cross-asset-class empirical
  regularity (same evidence base as above).
- **Trend/TSMOM as a reduce-only slow-bear filter**: **Tier A globally** for the raw phenomenon
  (Moskowitz-Ooi-Pedersen: 58 instruments; Hurst-Ooi-Pedersen: a century, multiple regimes) but
  **Tier C for India-specific whipsaw frequency and net cost**, because India offers at most ~4
  candidate "slow bear" observations since 1996 (2008, 2011, 2018-SMID, 2020's slower second leg) —
  borderline B/C on the clock test, and *whipsaw* frequency (the relevant cost variable) has not been
  counted at all yet. Its Tier-C reduce-only license is exactly why it is admissible in this design
  despite the thin India-specific count.
- **Options VRP existence**: **Tier A globally** (Israelov-Nielsen test ten global indices over
  multi-decade histories; VRP is one of the most replicated findings in derivatives research).
  **Tier C for the India-specific magnitude** — zero independently-verified Nifty-specific VRP
  statistic survives this pass; must be estimated from NSE's free India VIX archive in the data
  phase before it is Tier B or A for India.
- **Protective-put vs. static de-gross ranking**: **Tier A globally** (Israelov 2017's core result,
  extensively cited and reproduced in the derivatives-research community). **Untested for India** —
  no local replication exists to this dossier's knowledge; Tier C for India until one is run.
- **Fast triggers (vol-jump / VIX term structure / funding spreads) as reactive cut-gross switches**:
  **Tier B** at best for India — a genuine, quantifiable lead-lag relationship is confirmed for
  exactly one well-documented episode (Mar-2020, India VIX 25→64→~80s ahead of/alongside the Nifty
  −38% leg) with directional support from the broader vol-clustering literature (Tier A globally for
  the *mechanism*, not the India-specific lead time). 2008/2011/2013/2015-16/2018/2026 lead-lag
  behavior is **not yet counted** — closing this gap is the single highest-value data-phase task in
  this workstream (§6).
- **Grossman-Zhou surplus-scaling functional form**: mathematical theorem, not an empirical count —
  treat its *form* as structurally sound (Tier A as theory) while treating any *fitted parameter*
  (α, risk aversion) as Tier C until estimated on Indian data with the discrete-time/gap caveat
  (Klass-Nowicki) explicitly modeled in.
- **8–12% irreducible fast-crash floor**: **Tier C** — n<4 genuinely fast (sub-25-session,
  no-prior-signal) India crashes exist in the public record reviewed this pass (essentially one clear
  case, Feb–Mar 2020's initial leg, with the 2026 episode an unexamined candidate second case). Its
  Tier-C status is precisely why the CONTRACT treats it as a floor to respect (reduce risk /
  set expectations), never as a number to optimize toward.

---

## 6. Research method for the data phase

1. **Nifty/SMID drawdown episode table, complete and sourced to primary data.** Rebuild the §2 table
   directly from NSE bhavcopy (free) rather than secondary press summaries, closing the 2013 and
   2015–16 [VERIFY] gaps and fully investigating the 2026 episode. This is prerequisite to everything
   else in this workstream: the flash-crash exclusion rule (OPEN_QUESTIONS default #5, "regains
   pre-fall peak within ~63 trading days") must be applied *mechanically* to every episode, and the
   episode list itself is the sample the whole risk stack is validated against.

2. **Vol-targeting replication on India.** Estimate the vol/forward-return relationship for Nifty 50,
   Nifty 500, and a constructed mid/small (ranks 500–750) index using NSE bhavcopy daily closes back
   to the mid-1990s. Because India alone offers well under 30 independent vol-regime observations,
   **pool on the Jordà–Schularick–Taylor-style cross-country panel** (CONTRACT §9) using other EM
   index histories as the cross-country prior, explicitly reported as a separate, lower-confidence
   line from the India-only estimate. Purge and embargo test windows around each major episode by the
   estimated volatility half-life (do not use the HP filter anywhere per the CONTRACT trap; use
   Hamilton's 2018 regression filter if any trend/cycle decomposition is needed as an input).

3. **Trend-filter lookback and whipsaw count.** For each candidate lookback in a broad, pre-registered
   grid (not tuned post-hoc against realized Sharpe, per CONTRACT §9), count (a) how many true
   slow-bear entries it would have caught among the completed episode table from step 1, and (b) how
   many false (whipsaw) signals it would have fired in between. Report both counts raw — this is a
   frequency-counting exercise, not a backtest-Sharpe exercise, consistent with "we are not slaves to
   the literature" but still evidence-disciplined.

4. **Fast-trigger lead-lag table.** For every episode in step 1, pull India VIX (free NSE archive),
   a realized-vol series computed from bhavcopy, and CCIL/NSDL funding-and-flow series, and measure
   the actual lead/lag in days between each candidate trigger firing (on its pre-registered quantile
   rule) and the subsequent Nifty decline. This directly resolves the Tier-B→Tier-A upgrade path for
   this section's most important open item. Given India will likely offer well under 10 usable
   transitions, **do not fit a regime-switching model** to this data (CONTRACT trap) — report the
   raw lead-lag counts and keep the trigger rule-based/quantile-based rather than model-fitted.

5. **Options/VRP magnitude for Nifty.** Compute realized India VIX minus realized Nifty vol over
   rolling windows from the free NSE India-VIX archive, split pre- and post- the ~2019–2020 retail
   F&O volume expansion, to test directly for the compression risk flagged in §3 as untested. This
   also produces the actual expected annual cost of a given hedge-ratio choice, which the illustrative
   arithmetic in §4 currently only guesses at (Tier C, flagged there).

6. **Hedge-effectiveness / basis-risk and gap-distribution estimation.** Using bhavcopy, measure (a)
   the historical single-day gap (open vs. prior close) distribution for Nifty and for a constructed
   SMID basket, specifically on and around circuit-halt days, to calibrate the `HedgeEffectiveness`
   discount and the irreducible gap floor with real numbers rather than the current illustrative
   0.45–0.75 range; and (b) the realized tracking/basis risk between an index (Nifty/Bank Nifty)
   hedge and the actual mid/small book return during each episode in step 1.

7. **Grossman-Zhou parameter sweep, deflated-Sharpe-aware.** Sweep the surplus-rule's α and the
   leverage-response function `f` over a broad pre-registered grid *jointly* with the hedge-ratio ×
   regime grid from §4 — this is the CONTRACT's explicitly-named "7-point hedge sweep × regime grid"
   whose **true trial count** must enter the deflated Sharpe calculation (CONTRACT §9), not just the
   winning cell. Report out-of-sample performance against the historical-mean benchmark, never
   in-sample, using purged and embargoed cross-validation with an embargo scaled to the relevant
   signal's half-life.

8. **Turnover/cost reconciliation for the overlay.** Separately measure the one-way turnover and
   transaction cost generated by the leverage and hedge *overlays* (index futures/options rolling)
   as distinct from the equity sleeve's own turnover (already costed at ~0.6% NAV per 100% one-way in
   the CONTRACT's prior #6) — confirm or correct the directional claim in §3/§4 that overlay turnover
   cost is a small fraction of equity-sleeve cost per unit notional, using actual Nifty futures
   bid-ask and roll-cost data from bhavcopy plus documented STT/exchange-fee schedules.

---

## 7. Open questions and [VERIFY] items

- **2026 market-stress episode** (flagged in §2): a search snippet dated 22-May-2026 references a
  rupee/market stress event serious enough to be compared to the 2013 taper tantrum. Entirely
  outside this analyst's training-data knowledge (cutoff Jan-2026) and not investigated further
  before the search budget was exhausted. **Top-priority data-phase item.**
- **2013 taper tantrum and 2015–16 China-selloff Nifty peak/trough magnitudes**: presented as
  illustrative estimates in §2, not independently confirmed by search this pass (the session's shared
  web-search budget was exhausted mid-workstream — 20 successful searches were completed, target was
  15–40, and several planned follow-up queries on these two episodes, on Nifty futures cost-of-carry,
  and on ASM/GSM exact thresholds could not be run). [VERIFY: exact dates/levels for both episodes.]
- **Nifty option VRP magnitude and skew steepness**: no India-specific number was verified this pass;
  flagged in §3–§6 as the top options-related data-phase task. [VERIFY.]
- **Exact current ASM/GSM stage thresholds and current STT rates on index options (sale vs.
  exercise)**: described from general market-structure knowledge, not re-confirmed by a dedicated
  search this pass. [VERIFY before citing specific percentages in any downstream config.]
- **Cvitanic & Karatzas (1995) and Cherny & Obloj (2013)** extensions of Grossman-Zhou: seen only in a
  secondary citation-history snippet, titles/venues not independently confirmed. [VERIFY.]
- **Exact per-factor Sharpe-ratio deltas in Moreira & Muir (2017)** and the **exact quantitative
  payoff/cost table in AQR's "Tail Risk Hedging: Contrasting Put and Trend Strategies"**: mechanism
  and direction verified; precise figures not re-extracted from full text this pass. [VERIFY before
  quoting specific numbers from either.]
- **Whether hedge/leverage-overlay turnover counts toward each book's mandate turnover cap** (600% /
  200% / 100% one-way): the CONTRACT's turnover cap table is framed around the "equity universe" per
  book; this dossier assumes the overlay is a distinct risk instrument with its own (much smaller)
  cost line, but the CONTRACT does not say so explicitly. **Recommend an explicit principal ruling**
  and a corresponding OPEN_QUESTIONS entry.
- **Dallas Fed (2021)**, "Don't Look to the 2013 Tantrum for the Effect of Tapering on Emerging
  Markets": title and venue confirmed by search; full argument not read this pass — cited only as a
  cautionary cross-check that 2013-tantrum dynamics may not generalize cleanly to future episodes.
  [VERIFY full content before relying on its argument.]
- **India-specific replications of Israelov (2017)'s protective-put-vs-static-de-gross ranking and of
  Harvey et al. (2018)'s equity/credit-specific vol-targeting Sharpe result**: neither has a known
  local replication; both are currently imported as cross-country priors (Tier B/C per §5) and should
  be a first-wave data-phase deliverable given how directly they inform the hedge-vs-leverage-cut
  design choice in §4.
