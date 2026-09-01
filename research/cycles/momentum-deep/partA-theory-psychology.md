# Momentum/Trend Deep Dive — Part A & Part G

Part A: Theory — why prices trend · Part G: Psychology of operating momentum
v1.0 · 2026-09-01 · Deepens `research/dossiers/01-momentum-reversal.md` (D01; does not
contradict it) and the momentum rows of `docs/DESIGN.md` §4.1/§6.1/§10 · Ladder seats:
**L3** (cross-sectional momentum: 12-1 blended 6-1 rank + 52-week-high), **L4**
(time-series momentum, Nifty & gold), **L2** (fast stress triggers feeding the
crash-guard/regime layer), and the momentum crowding monitor named in `docs/DESIGN.md`
§10 · Status: theory/citations verified here; India magnitudes remain D01's Tier-B
priors pending the data phase.

This file assumes D01's frozen construct as given — equal-weight rank blend of 12-1 and
6-1 total-return momentum plus 52-week-high proximity, skip-month retained, 25–35%
haircut off the Agarwalla-Jacob-Varma 21.9%/yr India anchor — and supplies the
theoretical machine that construct compresses into a rank, honest at each step about
what the compression throws away. Part G turns to the desk that has to *operate* that
rank without chasing or abandoning it at the two moments that matter most.

---

## PART A — Theory: why prices trend

### A.1 The core anomaly — Jegadeesh & Titman (1993, 2001)

**(i) Mechanism.** Sort stocks by their cumulative return over a **formation** window of
`J` months; go long the top decile ("winners"), short the bottom decile ("losers"); hold
the zero-cost portfolio for `K` months. Do this for every `J,K ∈ {3,6,9,12}` — sixteen
combinations in total — and **every single one** earns a positive average return. This
was the finding that stunned the efficient-markets consensus of 1993: momentum is not
one cherry-picked specification, it is the modal outcome of an entire 4×4 grid, on data
(NYSE/AMEX, 1965–89) that predates the paper and so cannot be a discovered coincidence
fitted to it. The return could not be explained by exposure to market beta, size, or
book-to-market — the standard risk-based explanations of the day — nor by simple
short-term bid-ask bounce or lead-lag effects, which JT rule out with a **skip-month**
between formation and holding (the ranking uses returns through month `t-1`, holding
starts at `t+1`, deliberately discarding the most recent month, which is the zone where
1-month reversal — market-microstructure noise and bid-ask bounce, not information — is
known to contaminate raw past-return sorts).

**2001 out-of-sample test.** The 1993 sample's most obvious threat is data snooping: did
JT simply find the best-performing rule in hindsight? The 2001 paper re-runs the
identical construct on 1990s data the original never saw, and finds **momentum
persisted, materially undiminished** — direct evidence against the "lucky sample"
objection, and why momentum is treated as a genuinely out-of-sample-replicated anomaly
rather than an artifact. It adds a second, equally important finding: **no reversal at
2–3 years post-formation, but significant reversal at 4–5 years** — the outperformance
does not merely fade, it eventually **gives back roughly a third of the year-1 abnormal
return** over the following two years. This matters for operating the strategy: direct
evidence against holding a momentum book "buy and forget" past its holding window, and
favoring a behavioral (delayed-overreaction, later reversing) story over a risk-based
one (a genuine risk premium would not need to give itself back).

**(ii) Formal structure.** Let `r_{i,t-J,t-1}` = stock `i`'s cumulative return over
months `t-J` to `t-1` (the formation window, already skip-adjusted). Rank all `i` into
deciles `D1...D10` by `r_{i,t-J,t-1}`. The zero-cost portfolio return over the holding
window is `WML_t = R_{D10,t+1:t+K} − R_{D1,t+1:t+K}` (equal-weighted decile returns). The
canonical "12-1" construct ranks on `r_{i,t-12,t-1}` and holds for `K` months (commonly
`K=6` or `K=12`, rebalanced monthly on an overlapping basis so every calendar month holds
several staggered `K`-month sub-portfolios simultaneously — the standard JT
implementation, which is what removes any single reconstitution date's discreteness).

**(iii) For our seats.** This is the literal construction of **L3**'s primary
lookback family (`docs/DESIGN.md` §6.1: "equal-weight rank blend of 12-1 and 6-1
total-return momentum ... skip-month retained"). The skip-month is not a cosmetic
convention — it is the mechanism that keeps **L1** (1-month cross-sectional reversal,
Tier C, zero return budget per D01) and **L3** orthogonal by construction: without the
skip, L3's raw rank would be partially re-absorbing the reversal effect L1 is
deliberately excluded from monetizing. JT2001's 4–5 year reversal finding is the direct
theoretical justification for D01's turnover-cadence design (never run L3 as a
buy-and-hold book) and for capping L3's holding window well inside the window where
reversal has not yet started.

**(iv) Citation.** Jegadeesh, Narasimhan & Titman, Sheridan (1993), "Returns to Buying
Winners and Selling Losers: Implications for Stock Market Efficiency," *Journal of
Finance* 48(1):65–91. **[Verified]** Jegadeesh, Narasimhan & Titman, Sheridan (2001),
"Profitability of Momentum Strategies: An Evaluation of Alternative Explanations,"
*Journal of Finance* 56(3):699–720. **[Verified]**

---

### A.2 Underreaction I — conservatism, representativeness, and gradual diffusion

**(i) Mechanism — Barberis, Shleifer & Vishny (1998).** BSV build a single
representative investor uncertain which of two false models governs a stock's earnings
process, updating that uncertainty by Bayes' rule. **Model 1** is a mean-reverting
regime the investor believes a priori more common; when it governs, a single earnings
surprise looks like noise expected to reverse — the investor systematically
**underreacts** to any one new piece of news (**conservatism**: beliefs update too
slowly). **Model 2** is a trending regime; once a **streak** of same-direction surprises
accumulates, it looks "representative" of a genuine trend (the representativeness
heuristic: judging probability by resemblance to a pattern, not correct base rates), and
the investor **overreacts**, extrapolating further than the true process warrants. One
Bayesian-updating apparatus thus produces **both** regularities: underreaction to
isolated news generates short-horizon **momentum**; delayed, extrapolative overreaction
to a streak eventually corrects, generating long-horizon **reversal**. This is the first
formal reason momentum and reversal are not two separate puzzles needing two theories.

**Mechanism — Hong & Stein (1999).** HS model two boundedly rational agent populations
trading the same asset. **Newswatchers** each observe a private piece of fundamental
information but cannot extract what everyone else collectively knows from the price —
information diffuses **gradually** across the population, one transmission at a time,
producing a slow, sluggish, but eventually complete adjustment. **Momentum traders**
observe only **past prices**, not fundamentals, and try to arbitrage the newswatchers'
sluggish adjustment with a simple trend-chasing rule. Because they cannot condition on
how much of a move is genuinely new information versus other momentum traders' own
earlier buying, their arbitrage **necessarily overshoots** — chasing the trend past fair
value once enough of it has already been chased. HS's central insight: underreaction and
overreaction are two **stages of one gradual-diffusion-plus-imperfect-arbitrage
process**, not separate phenomena needing separate mechanisms.

**(ii) Formal structure.** BSV: earnings follow one of two hidden regimes with
transition probabilities calibrated so Model 1 (mean-reverting) is a priori more
persistent — the source of conservatism-driven initial underreaction; a run of `≥2–3`
same-sign surprises shifts posterior weight toward Model 2 (trending), producing
representativeness-driven extrapolation. HS: the fraction of newswatchers informed of a
signal grows gradually over calendar time (an epidemic-style diffusion, not
instantaneous); momentum traders' aggregate demand is an increasing function of the
asset's own price change over a finite lookback window `k` — a mechanical trend-following
rule with no fundamentals input at all. The testable comparative static, taken to data
by **Hong, Lim & Stein (2000)**: since the *mechanism* is diffusion speed, momentum
should be (a) weaker in large, widely-held stocks; (b) — size held fixed — weaker where
**analyst coverage** is high; and (c) the coverage effect **stronger for past losers
than winners**, since firms have an asymmetric incentive to publicize good news and sit
on bad — "**bad news travels slowly**." All three were confirmed on US data.

**(iii) For our seats.** HS/HLS's confirmed prediction creates a genuine, unresolved
**tension** inside D01's own evidence base that the data phase must resolve, not paper
over: HS predicts momentum should be **strongest** in exactly the low-analyst-coverage,
small-cap tail the aggressive book's **L3** seat trades (ranks 500–750, thin or no
sell-side coverage) — yet Chui, Ranganathan, Rohit & Veeraraghavan (2023), already the
primary India anchor for D01's liquidity discipline, find the opposite empirical sign in
that same tail: the **illiquid** tercile **reverses** rather than continues. Slow
diffusion argues for *more* continuation there; the illiquidity/liquidity-provision-
premium story (Cheng-Hameed-Subrahmanyam-Titman, D01 §3) argues the opposite — which
dominates is an empirical, pre-registerable question (test momentum against an
analyst-coverage proxy crossed with a liquidity tercile, independently of each other,
rather than assuming the liquidity result already settles the coverage question).

**(iv) Citations.** Barberis, Nicholas; Shleifer, Andrei; Vishny, Robert (1998), "A Model
of Investor Sentiment," *Journal of Financial Economics* 49(3):307–343. **[Verified]**
Hong, Harrison & Stein, Jeremy C. (1999), "A Unified Theory of Underreaction, Momentum
Trading, and Overreaction in Asset Markets," *Journal of Finance* 54(6):2143–2184.
**[Verified]** Hong, Harrison; Lim, Terence; Stein, Jeremy C. (2000), "Bad News Travels
Slowly: Size, Analyst Coverage, and the Profitability of Momentum Strategies," *Journal
of Finance* 55(1):265–295. **[Verified]**

---

### A.3 Underreaction II — the disposition effect and the capital-gains-overhang channel

**(i) Mechanism.** Shefrin & Statman (1985) name the **disposition effect**: investors,
driven by prospect-theory loss aversion combined with mental accounting (each position
its own closed account, "settled" only on a realized gain), are reluctant to sell at a
loss and eager to sell at a gain. Applied to news arrival: when good news hits a stock
trading **below** the average holder's purchase price (a paper **loss**), a mass of
underwater holders becomes eager sellers into any rally — relieved to exit near
breakeven rather than reassessing fundamentals — which **caps** the immediate price
response and forces the news into the price only gradually, as sellers exhaust and
unanchored buyers take over. This mechanical selling-pressure friction, not any belief
distortion, generates post-news underreaction (drift). **Frazzini (2006)** takes this
directly to data using mutual-fund holdings (a proxy for a large investor class's
reference/purchase price) and finds **drift is significantly larger whenever the news
event's sign matches the sign of funds' existing paper gain or loss** — the friction
bites hardest exactly where prospect theory predicts. An event-driven strategy on this
pattern earns **over 200 basis points per month** of alpha in his sample.

**Grinblatt & Han (2005)** formalize the aggregate version and go one step further: they
build a **capital-gains-overhang** variable — a stock-level proxy for the current
market's average cost basis — and show that once this variable is included directly in
a return regression, **plain past-return momentum's predictive power vanishes**: the
overhang variable, not the raw past return, is what is actually driving the
cross-section. Momentum, on this reading, is not really a bet on trend continuation at
all — it is a **noisy proxy for the reference-price gap** between where a stock trades
and where its actual holder base is anchored.

**(ii) Formal structure.** Reference price (a proxy for the population-weighted average
holder cost basis): `RP_t = Σ_{n=1}^{N} w_n · P_{t-n}`, where the weight on a price `n`
periods back is `w_n = V_{t-n} · Π_{τ=1}^{n-1}(1 − V_{t-n+τ})` — a turnover-decayed
weight (`V_τ` = trading-volume/shares-outstanding in period `τ`, the probability any
given share changes hands that period), so older prices are progressively down-weighted
as more of the original holder base has since sold. **Capital-gains overhang**:
`g_t = (P_t − RP_t) / P_t`. Once `g_t` is included as a regressor, the coefficient on
raw past return collapses toward zero — `g_t` **subsumes** momentum rather than merely
correlating with it.

**(iii) For our seats.** This recasts **L3**'s rank blend as, honestly, a coarse and
freely-available proxy for a sharper but currently unbuilt signal. India's structurally
**high promoter/insider ownership concentration** (already flagged in D01 as a reason
free float is thin and price discovery slows) plausibly makes the reference-price
mechanism **stickier** here than in the US: promoter holdings rarely trade, so a large,
resistant fraction of the register never updates its component of the turnover-weighted
reference price — a testable prediction, not an assumption. **Data-phase
recommendation**: build `g_t` from NSE bhavcopy volume data (free, already approved) and
test whether it subsumes India's 12-1/6-1 rank as it does in the US, and whether the
effect is **stronger** in high-promoter-holding names, where a smaller tradable float
should make the reference-price gap larger and slower to close.

**(iv) Citations.** Shefrin, Hersh & Statman, Meir (1985), "The Disposition to Sell
Winners Too Early and Ride Losers Too Long: Theory and Evidence," *Journal of Finance*
40(3):777–790. **[Verified]** Frazzini, Andrea (2006), "The Disposition Effect and
Underreaction to News," *Journal of Finance* 61(4):2017–2046. **[Verified]** Grinblatt,
Mark & Han, Bing (2005), "Prospect Theory, Mental Accounting, and Momentum," *Journal of
Financial Economics* 78(2):311–339. **[Verified]**

---

### A.4 Overreaction and self-reinforcing continuation — Daniel, Hirshleifer & Subrahmanyam (1998)

**(i) Mechanism.** DHS build momentum from two psychological primitives operating on a
**single, sophisticated** trader (not two agent types, unlike HS99). **Overconfidence**:
the investor overestimates the *precision* of their own private signal (not its expected
value — its certainty), moving price too far toward their private view — an immediate
overreaction to private information. **Biased self-attribution**: when a later *public*
signal (an earnings print, an analyst call) **confirms** the prior private view,
confidence rises *disproportionately* — the investor credits their own skill; when a
public signal *disconfirms* it, confidence falls only a little — blamed on noise. The
asymmetry means a **run of confirming public news** pushes the investor progressively
*more* overconfident, pushing price further the same way — a **self-reinforcing**
overreaction to a sequence, generating short/intermediate-run **momentum**. Eventually,
as the truth surfaces, the compounded overreaction must fully unwind — generating
long-horizon **reversal**. Attested comparative statics: overconfidence alone implies
negative long-lag autocorrelation and excess volatility; biased self-attribution layers
in **positive short-lag autocorrelation (momentum)**, short-run earnings drift, and
**negative correlation between future returns and long-horizon past performance** — the
DeBondt-Thaler-style reversal, produced endogenously rather than assumed.

**DHS vs HS — different predictions about what kills momentum.** The two theories are
**not** interchangeable labels for "behavioral momentum" — they predict momentum decays
for **structurally different reasons**, pointing to different, separately testable
falsifiers:

| | HS99 (gradual diffusion) | DHS98 (overconfidence + self-attribution) |
|---|---|---|
| **Where the bias lives** | The *speed* information reaches the market (a population-diffusion friction) | *How* a given trader misprocesses information they already have (a belief-updating bias) |
| **What should shrink momentum** | Anything that speeds diffusion: more analyst coverage, more institutional ownership, faster media/retail information technology | Anything that reduces overconfidence/self-attribution at the marginal trader: crowding-in by rational, unbiased arbitrage capital trading *against* the bias |
| **Decay channel** | Structural/technological — a slow, secular trend as coverage and information speed improve | Capital-driven — tracks how much smart, unbiased money has entered to trade against retail-driven overconfidence |
| **Testable India proxy** | Track momentum profitability against analyst-coverage/media-speed proxies over time | Track momentum profitability against smart-beta/institutional momentum-product AUM (the crowding monitor, A.7 below) |

**(iii) For our seats.** D01's own decay evidence is currently ambiguous between these
two stories: Jacobs-Müller (2020) find international post-publication decay is largely
absent outside the US (consistent with slow, structural HS-style diffusion still
operating in most markets), while Sharma-Subramaniam-Sehgal (2021) find India momentum
increasingly **risk-model-explained** over 2005–16 (consistent with a DHS-flavored,
capital-driven crowding-in). This is a genuinely pre-registerable, separating hypothesis
the data phase does not yet distinguish: if India's post-2015 weakness (H02, already
registered) tracks analyst-coverage/information-technology proxies, that favors the HS
channel and a slow, largely irreversible decay; if it instead tracks the smart-beta/
momentum-fund AUM growth in D01 §2 (₹290cr→₹46,000cr, 2020–2025), that favors DHS and a
**crowding-driven, therefore cyclical** decay that could reverse if crowded capital is
flushed out (A.7 below formalizes this). The two carry opposite implications for
whether the haircut should ever move back down, and both tests should run.

**(iv) Citation.** Daniel, Kent; Hirshleifer, David; Subrahmanyam, Avanidhar (1998),
"Investor Psychology and Security Market Under- and Overreactions," *Journal of Finance*
53(6):1839–1885. **[Verified]**

---

### A.5 The frog-in-the-pan refinement — Da, Gurun & Warachka (2014)

**(i) Mechanism.** DGW refine limited-attention underreaction with a specific,
falsifiable claim: investors are less attentive to information arriving **continuously**
in many small pieces than to the identical cumulative information arriving in a few
large, discrete jumps — even when the total price-relevant content is the same. A stock
grinding steadily upward on many small positive days is the "frog in slowly heating
water" — nobody notices; a stock jumping in a handful of big, attention-grabbing news
days gets fuller, faster attention and so has **less** underreaction left to correct.
The formation-period return's *shape*, not just its sign and magnitude, therefore
carries independent forecasting information: the same cumulative winner return
forecasts **more** future continuation when built from continuous grinding than from a
few discrete jumps.

**(ii) Formal structure.** Information Discreteness: `ID = sign(PRET) × [%neg − %pos]`,
where `PRET` is the formation-period (an 11-month window in DGW's construction)
cumulative return, and `%pos`/`%neg` are the percentage of individual **daily** returns
during that window that were positive/negative respectively. For a winner (`PRET>0`)
built almost entirely from up-days (`%pos` large, `%neg` small), the bracket term is
strongly negative and `ID` is strongly negative — the "continuous," frog-in-the-pan
case, predicting **more** future momentum. For the same cumulative winner return built
instead from a few enormous up-days interspersed with many small down-days (`%neg`
larger relative to `%pos`), `ID` is less negative or positive — the "discrete," salient
case, predicting **less** future momentum, potentially none. `ID` is thus a variable
about the **path's shape**, constructed to be orthogonal to the sign and magnitude of the
formation return itself. Sorting stocks by `ID` produces a monotonic relationship: profit
is largest among the most continuous-information deciles and falls toward zero or
reverses among the most discrete-information deciles — the exact magnitude is
holding-period- and specification-dependent across the paper's tables and is not quoted
to a false decimal here (**[VERIFY: exact ID-quintile magnitude table for the paper's
headline 6-month-holding specification]**).

**(iii) For our seats.** `ID` is constructible from the **same free price-only data L3
already consumes** (bhavcopy daily closes → sign of each day's return over the formation
window → `%pos`/`%neg`) at **zero incremental data cost** — a genuinely free upgrade
candidate, unlike most refinements this dossier discusses. It is a strong, concrete
recommendation for a data-phase pre-registration: test `ID` as a **third rank-blend
component or tiebreak** alongside 12-1, 6-1, and 52-week-high, distinguishing which
winners/losers in the composite rank are likely to keep trending (continuous-information
names) from which are closer to a one-off, already-arbitraged event jump (a discrete,
earnings-surprise-driven "winner" that behaves more like a post-earnings-announcement
drift name than a genuine momentum name). This is a proposal for the research agenda,
not a design change — it is not yet part of D01's frozen construct and should enter only
via a pre-registered test.

**(iv) Citation.** Da, Zhi; Gurun, Umit G.; Warachka, Mitch (2014), "Frog in the Pan:
Continuous Information and Momentum," *Review of Financial Studies* 27(7):2171–2218.
**[Verified]**

---

### A.6 Time-series momentum — a different bet entirely

**(i) Mechanism.** Cross-sectional momentum (**L3**) is a bet on **relative**
performance: a stock's position depends on its past return *ranked against every other
stock in the universe at the same date*. Time-series momentum (**L4**, Moskowitz, Ooi &
Pedersen 2012) is a bet on an **asset's own trend in isolation**: an instrument's
position depends **only** on the sign of its own trailing return, with no reference to
any other instrument. This is the precise sense in which the two are mathematically
distinct, not merely applied to different asset classes: L3 is constructed to be
(roughly) market-neutral by cross-sectional demeaning; L4's aggregate market exposure is
**time-varying and can be net long or net short**, since if most instruments trend the
same way (a broad bull or bear market), L4 is net long or short the market as a
byproduct, with no demeaning to cancel it out. This single structural difference is *why*
the two have opposite crash profiles (A.8): L4 performs best in extreme markets either
way, since a strong trend is exactly what a sign-following rule is built to catch; L3 is
hurt specifically by a **sharp reversal after a bear market**, since its loser-leg
ranking does not update fast enough for a sudden rebound.

**(ii) Formal structure.** **L3** weight: `w_i,t ∝ rank_i(r_{i,t-J,t-1}) − mean(rank)`
across `i=1...N` at date `t` — self-financing (`Σw_i,t ≈ 0`) by construction, so its
market beta is near zero unless winners and losers systematically differ in beta (which
is exactly Daniel-Moskowitz's crash mechanism, A.8). **L4** weight:
`w_i,t = sign(r_{i,t-12,t}) × (vol_target/σ_i,t)` — a function of instrument `i`'s **own**
trailing sign and **own** volatility alone; portfolio beta to any common factor `f` is
`β_portfolio,f = Σ_i w_i,t·β_i,f`, which is **not** pinned to zero and moves with the
aggregate trend direction across the universe. MOP2012's actual empirical test: regress
next-month excess return (scaled by trailing volatility) on the **sign** of trailing
`h`-month return, separately for each lag `h`: `r_{i,t+1}/σ_i,t = α + β·sign(r_{i,t-h,t})
+ ε_i,t`, across 58 liquid futures instruments (equity indices, currencies, commodities,
government bonds), 1965–2009. `β` is significantly **positive** for essentially every `h`
from 1 to 12 months; run with `h` beyond roughly 12–24 months, the coefficient turns
**negative** — the empirical basis for "trend persists about a year, then partially
reverses."

**A century of evidence — Hurst, Ooi & Pedersen (2017).** HOP extend the same construct
back to **1880** on a reconstructed dataset across the same asset classes (equity
indices, bonds, commodities, currencies), roughly 137 years. Headline findings: a
diversified trend-following portfolio delivered **positive average returns in every
decade** since 1880, low correlation to buy-and-hold stocks and bonds throughout, and
performed well in **8 of the 10 largest drawdown episodes** for a 60/40 stock/bond
portfolio over the century — a genuine "crisis alpha" property holding across
recessions and booms, war and peacetime, high- and low-rate and -inflation regimes
alike. This is the single strongest piece of evidence that TSMOM's persistence is not a
post-1980s, futures-market-specific artifact.

**(iii) For our seats.** This formal distinction is exactly why **L4** sits inside the
**regime-matrix/gold-tilt** seat rather than the equity-cross-section optimizer
(`docs/DESIGN.md` §4.1 ladder table, L4 row, respecting Mandate §2's Stage-3 boundary
that the optimizer touches only the equity cross-section): L4's time-varying, non-zero
market beta makes it
a legitimate market-timing/regime signal — its sign literally states whether the asset's
own trend currently points up or down — whereas L3's zero-beta, relative-rank
construction makes it a pure stock-selection alpha with **no** legitimate claim on
market-timing information. The two must never be conflated mathematically merely because
both are colloquially called "momentum."

**(iv) Citations.** Moskowitz, Tobias J.; Ooi, Yao Hua; Pedersen, Lasse Heje (2012),
"Time Series Momentum," *Journal of Financial Economics* 104(2):228–250. **[Verified]**
Hurst, Brian; Ooi, Yao Hua; Pedersen, Lasse Heje (2017), "A Century of Evidence on
Trend-Following Investing," *Journal of Portfolio Management* 44(1):15–29.
**[Verified]**

---

### A.7 Why momentum survives being known — the survival argument, category by category

Per CONTRACT §5, every signal must answer *why does this survive being known*, with an
acceptable category attached. Momentum's answer is genuinely **weaker** than credit's
(credit-deep A.11's bias lives inside the credit-supplying institutions themselves, with
no outside "smart money" able to short an economy's lending psychology at scale), and
the treatment below says so directly.

**Limits to arbitrage — category (ii)/(iv), and 2009 as the enforcement mechanism.**
Momentum is not free to arbitrage away even once well understood, because *shorting* it
(or simply declining to run it) carries genuine **career risk**: a manager benchmarked
against peers running the strategy suffers visible, near-term tracking error for an
uncertain, possibly multi-year payoff. This limit was **enforced**, not merely
theorized, in **2009**: the spring crash erased roughly two years of prior cumulative
momentum profit in months (A.8) — exactly the kind of drawdown that forces
momentum-running capital to de-lever or exit at the worst possible moment, itself part
of *why* the anomaly persists (capital cannot hold the position through its own
worst-case realization at scale). A genuine, if modest, survival argument: the strategy
is protected less by anyone's inability to understand it, more by holding it through a
crash being organizationally hard.

**Crash risk as compensation — Daniel & Moskowitz (2016).** A complementary, risk-based
answer: part of momentum's average return **is** compensation for bearing the crash risk
detailed in A.8 — the loser leg's payoff resembles a short call option on market
recovery, and unconditional returns partly reflect the premium for being short that
option most of the time. This reframes some of the average return as a genuine, priced
risk premium, not a pure behavioral anomaly with no risk-based counterpart at all.

**Crowding cycles — Lou & Polk's comomentum as the measurable crowding state.** The
honest crowding story needs a **measurable** variable, not a vague "AUM is high" claim.
Lou & Polk build one: **comomentum** is the abnormal high-frequency return correlation
**among the stocks a typical momentum strategy would simultaneously trade** — when many
arbitrageurs run the same long-winners/short-losers book at once, their correlated
trading itself induces excess co-movement among winners (and separately losers) beyond
what common risk-factor exposure explains. Post-formation momentum returns are
**strongly, monotonically decreasing** in comomentum — the joint years-1-and-2 return
differential between the highest and lowest comomentum quintiles is **roughly −1.07% per
month** (t≈−3.35), and high comomentum also forecasts higher spread volatility and more
negative skewness: an *ex ante*, contemporaneously observable crowding signature that
predicts both lower forward returns and a higher chance of a crash-like episode. This is
precisely the measurable state variable `docs/DESIGN.md` §10 gestures at with its
"smart-beta AUM/crowding monitor" — comomentum is a stronger candidate than raw AUM,
being constructible from price data with no disclosure lag. The design's decay ledger
already flags a live instance: the **2025 quant-crowding episode** (quant long-short
managers losing an estimated 4.2% June–July 2025 per Goldman Sachs prime-services
estimates, a second drawdown in October 2025, a further ~2.8% loss in early January
2026) repeatedly named momentum as a participating, crowded factor in press coverage —
contemporary confirmation the mechanism is not a historical curiosity, presented here as
journalistic/industry evidence (Tier C by source), corroborating rather than proving the
academic mechanism.

**The honest counter-case — McLean-Pontiff decay applies here more than to credit.**
This is where momentum's survival argument is weakest relative to credit's, and must be
stated plainly rather than softened. Three independent lines of evidence converge:

1. **Chordia, Subrahmanyam & Tong (2014)** find that as liquidity and trading activity
   rose through the 2000s, momentum returns specifically **declined over time and
   converged toward zero** — a direct, dedicated study of momentum's own attenuation
   under growing arbitrage capital, not merely the average-anomaly decline McLean-Pontiff
   report across 97 predictors.
2. A recent, **not yet peer-reviewed** arXiv working paper (Lee 2025, "Not All Factors
   Crowd Equally") models factor alpha decay as hyperbolic, `α(t) = K/(1+λt)`, and finds
   momentum's realized decay fits this hyperbolic form better than linear or exponential
   alternatives (R²≈0.65 vs 0.51/0.61) — consistent with momentum being one of the
   "mechanical," easily-replicated factors (an unambiguous, simple signal like "buy
   recent winners") that decay fastest and most predictably under crowding, as opposed
   to judgment-dependent factors like value or quality. **This is a single-author,
   unreviewed preprint and is flagged as such** — cited for its directional consistency
   with the other two sources, not as a settled magnitude.
3. A practitioner data series (AlphaArchitect, using 30 years of US momentum-factor
   data, 1994–2024) reports the most recent decade (2014–2024) as **uniquely weak**:
   momentum averaged roughly **2.2%/year**, against double-digit annual returns typical
   of prior decades in the same series — directionally consistent with (1) and (2)
   without independently re-deriving the exact figure here.

None of these three overturn Jacobs-Müller's (2020) finding that **post-publication
decline is largely a US-specific phenomenon** (D01's basis for capping the India
haircut at 25–35% rather than the full 58%) — but they establish that *where* arbitrage
capital is deep and liquid (the US, and increasingly India's own smart-beta-heavy
large/mid-cap names per D01 §2's ₹46,000cr AUM figure), momentum decay is real,
measured, and ongoing — more so than credit's, where D-credit-deep A.11 argues the bias
is embedded in the credit-supplying institutions themselves and largely immune to
outside arbitrage. **This asymmetry is itself the strongest argument for treating L3's
haircut as escalating and state-contingent (already built into H02's falsifier), never
a single frozen number for the program's lifetime.**

**(iv) Citations.** Daniel, Kent & Moskowitz, Tobias J. (2016), "Momentum Crashes,"
*Journal of Financial Economics* 122(2):221–247. **[Verified]** Lou, Dong & Polk,
Christopher (2022), "Comomentum: Inferring Arbitrage Activity from Return Correlations,"
*Review of Financial Studies* 35(7):3272–3302. **[Verified]** Chordia, Tarun;
Subrahmanyam, Avanidhar; Tong, Qing (2014), "Have Capital Market Anomalies Attenuated in
the Recent Era of High Liquidity and Trading Activity?," *Journal of Accounting and
Economics* 58(1):41–58. **[Verified]** Lee, Chorok (2025), "Not All Factors Crowd
Equally: Modeling, Measuring, and Trading on Alpha Decay," arXiv:2512.11913.
**[Verified as an existing preprint; unreviewed — Tier C]** AlphaArchitect (blog),
"Momentum Factor Investing: 30 Years of Out of Sample Data." **[Verified as an existing
practitioner source; Tier C, directional use only]** McLean, R. David & Pontiff, Jeffrey
(2016), "Does Academic Research Destroy Stock Return Predictability?," *Journal of
Finance* 71(1):5–32. **[Verified — already in CONTRACT §5 and D01]**

---

### A.8 The momentum-crash mechanism in detail — Daniel & Moskowitz (2016)

**(i) Mechanism.** Momentum's average return is strongly positive, but its return
distribution is **severely negatively skewed**: rare, large crashes coexist with a
generally attractive Sharpe ratio in normal times. The worst episodes on record — 1932,
1938–39, 1974–75, 2001–02, and 2009 — are not randomly timed. They cluster in
**"panic" states**: **following market declines** and **during high-volatility
regimes**, and — the counterintuitive part — the crash itself occurs **contemporaneously
with market rebounds**, not the preceding decline. The reason is the loser leg's
changing composition: after a sustained bear market, the stocks in the portfolio's short
(loser) leg are, almost by definition, the most beaten-down, highest-leverage survivors
— precisely the names with the most **upside optionality** in any recovery, their equity
having come to resemble a deep out-of-the-money call on the firm's assets. When the
market rebounds, this loser leg **rallies hard** — momentum is short the very recovery
that ends the panic — while the winner leg, having spent the bear market in steadier,
lower-beta names, participates far less. This is why the crash occurs **in recoveries,
not in crashes**: the decline itself is not what hurts momentum (the loser leg is
genuinely losing money, as intended, during the decline) — it is the subsequent, sharp
bounce that hurts it, because the loser leg's beta has by then become far higher than
the winner leg's.

**Magnitude.** The two worst episodes: **June–August 1932**, the momentum portfolio lost
approximately **91%** over three months; **2009**, it lost more than **73%** over three
months, erasing roughly two years of prior cumulative profit (D01 §1) — both during
sharp market rebounds off a prior severe decline, exactly as the mechanism predicts.

**(ii) Formal structure — the conditional (time-varying) beta.** Unlike a static CAPM
beta, Daniel-Moskowitz model the winner and loser legs' betas as **time-varying and
state-dependent**, conditioning on a bear-market/panic-state indicator (the trailing
market return in its own worst historical bucket, combined with elevated realized/ex-ante
market volatility — a joint level-and-volatility condition on the market itself, not a
fixed calendar-dated episode). In the panic state, the **loser** portfolio's beta rises
sharply — becoming a high-beta, option-like claim on the market — while the **winner**
portfolio's beta stays comparatively low, so `WML = Winners − Losers`'s **effective beta
turns strongly negative** exactly where the market is most likely to rebound. Ex-ante
expected momentum returns in the panic state are therefore **low or negative**, not
because the strategy has stopped working, but because its beta has flipped sign at the
worst possible moment. A dynamic strategy explicitly forecasting each leg's conditional
mean/variance and re-weighting accordingly (de-grossing before and through the panic
state) **roughly doubles the unconditional Sharpe ratio**, robust across 8 international
markets and asset classes.

**(iii) For our seats.** This is the direct theoretical basis for D01's **crash-guard
rule** (`docs/DESIGN.md` §6.1): scale L3's gross exposure by the inverse of the trailing
realized volatility of the momentum spread itself (the Barroso-Santa-Clara form, already
Tier A globally: raises the Sharpe ratio from ≈0.53 to ≈0.97 and "virtually eliminates"
crashes in the US evidence, since high realized spread-vol forecasts *both* higher risk
and lower forward return) **plus** an additional cut when the trailing market-return
quantile sits in its own worst historical bucket (the Daniel-Moskowitz bear-state
indicator directly). This dual form is why the crash guard is **two independent
quantile conditions**, not one: vol-scaling alone would still be caught out by a bear
state with temporarily low realized vol right before the panic; the bear-state overlay
alone would miss a slow grind where the loser leg's fundamental beta is quietly rising.
The mechanism also explains **why crash timing is a leading, not lagging, signal
candidate for L2**: the panic-state indicator is defined on the *market's* trailing
return and volatility, available in real time, not on momentum's own realized crash
(observed only after the damage).

**(iv) Citation.** Daniel, Kent & Moskowitz, Tobias J. (2016), "Momentum Crashes,"
*Journal of Financial Economics* 122(2):221–247. **[Verified — cited fully in A.7]**

---

### A.9 Synthesis — mechanism, observable, seat, and the honest gap

| Mechanism | Observable proxy | Seat that consumes it | What no free observable captures |
|---|---|---|---|
| Gradual information diffusion (BSV98, HS99) | Formation-window rank; analyst-coverage/size cross-tabs | **L3** (rank blend) | No India analyst-coverage panel is free/point-in-time; the HS-vs-illiquidity tension (A.2.iii) is untested |
| Disposition effect / capital-gains overhang (Frazzini, Grinblatt-Han) | Turnover-weighted reference price `RP_t`, overhang `g_t` | **L3** — currently only a proxy via raw past return | `g_t` itself is not yet built; L3 is a noisy stand-in for a sharper, unbuilt signal |
| Overconfidence + self-attribution (DHS98) | Sequential public-news confirmation pattern | **L3** — the *behavioral* half of the survival argument | Cannot separate DHS's decay channel from HS's without the coverage-vs-AUM test in A.4.iii |
| Frog-in-the-pan / information discreteness (DGW14) | `ID = sign(PRET)×[%neg−%pos]` from daily bhavcopy | Candidate **L3** tiebreak (not yet in the frozen construct) | Not built; a genuinely free, zero-incremental-cost upgrade awaiting pre-registration |
| Time-series trend persistence (MOP2012, HOP2017) | Sign of own trailing 1–12m return | **L4** (regime-matrix + gold tilt) | India-specific TSMOM magnitude/cost estimate (D01 Tier B only) |
| Momentum crash / conditional beta (Daniel-Moskowitz) | Trailing market-return quantile + realized vol jointly | **L2** (panic-state trigger) feeding the **L3 crash guard** | India has only ≈2 clean crash-and-rebound observations (2008–09, 2020) — Tier B at best on India timing |
| Crowding cycle (Lou-Polk comomentum) | Abnormal same-side return correlation among momentum names | The **crowding monitor** (`docs/DESIGN.md` §10) | Comomentum has never been built on India data; today's proxy is AUM growth, a cruder, disclosure-lagged substitute |
| Publication/crowding decay (Chordia-Subrahmanyam-Tong, McLean-Pontiff) | Sub-sample return split, pre/post 2015 | H02's registered haircut escalation | Whether India decay is HS-style (structural) or DHS-style (crowding, reversible) is unresolved — the two imply opposite futures for the haircut |

**What no free observable captures — stated honestly.** The sharpest gap is the
**capital-gains-overhang / reference-price** variable (Grinblatt-Han): the one mechanism
here with direct evidence it **subsumes** plain momentum entirely, yet not part of D01's
frozen construct and still requiring a dedicated build, even though its inputs (price,
volume) are already free and in hand. The second gap is **comomentum**: the best
measurable crowding variable in the literature is unbuilt in India, leaving the desk on
the cruder, disclosure-lagged AUM-growth proxy D01 §2 already flags as noisy. Unlike the
credit block's gaps (leverage terms, the external finance premium), both are buildable
from data **the desk already possesses** for L3, not blocked by a missing free India
source — the highest-value, lowest-cost research-agenda items this dossier identifies.

---

## PART G — Psychology of operating momentum

Part A describes a system whose average return is real but whose distribution is
adversarial to the humans running it: attractive most of the time, catastrophic at
specific, identifiable moments, and structurally tempting to override at exactly the
wrong times. This part maps the recurring operator failure modes to the countermeasures
this program's design already carries — a discipline of non-decisions, not virtue.

### G.1 Buying tops — extrapolation applied to the strategy itself

**Mechanism.** Greenwood & Shleifer (2014) document, across six independent data
sources of investor return expectations spanning 1963–2011, that survey expectations of
*future* returns are strongly *positively* correlated with *past* returns and the
market's current level, and strongly *negatively* correlated with model-based rational
expected returns — investors expect the highest returns exactly when a properly
specified model says returns should be lowest. Bordalo, Gennaioli & Shleifer's (2018)
diagnostic-expectations mechanism explains *why*: agents over-weight scenarios made more
likely by *recent* news relative to their true probability. The bias does not stop at
individual stocks — it applies with equal force to the **momentum strategy itself**. A
desk that has just lived through several strong months of L3/L4 performance is
systematically prone to reading that run as evidence the strategy's *forward* return is
high, precisely when it more plausibly means the cycle (A.8) is closer to its panic
state than its start. This is the flip side of D01's live-vs-backtest gap: the NSE
momentum indices' benign 2020–2024 live record (29.7%/5y, 23.3%/10y, D01 §2) is real,
but drawn from a window that has never faced the −70.5% (Oct-2007 to Dec-2008) the
18-year practitioner backtest shows — reading the live numbers alone is extrapolating
from a sample that has not yet contained its own tail.

**Countermeasure.** Sizing is governed by the pre-registered decay haircut (H02;
`docs/DESIGN.md` §10: 25–35% off the AJV 21.9%/yr anchor, escalating toward 58% only on
a pre-registered falsifier) and by the Barroso-Santa-Clara vol-scaling rule, which caps
gross exposure as a function of the momentum spread's **own trailing volatility** —
neither responds to a run of good recent performance as a reason to add. A discretionary
increase in size *because* the strategy has recently done well is a hypothesis change
outside the pre-registered grid and is inadmissible without a scheduled Challenger
review, exactly as G.1 in the credit-deep dossier documents for the parallel override
temptation in booms.

### G.2 Abandoning at the bottom — capitulating exactly when forward returns are highest

**Mechanism.** The diagnostic-expectations bias mirrors itself at the trough: after a
drawdown, recent bad news is over-weighted, making "momentum is broken" feel
representative even though the mechanism argues the opposite. This is made structurally
worse by momentum's *own* documented behavior: the crash arrives, per A.8,
**contemporaneously with the market rebound** — the moment an operator is most tempted
to cut the sleeve (having just watched it lose 70%+ in a few months) is, mechanically,
close to the moment the loser leg's inflated beta has already delivered its damage and
the strategy, properly re-levered, is positioned to participate in whatever comes next.
The program's own phase framework (`research/OPEN_QUESTIONS.md`, 2026-09-01) names
exactly this trap for the **downturn quadrant**: reading "we're in the downturn
quadrant, therefore stay de-risked" is narrative capture applied to a label, not a
validated result — the phase object is logged everywhere but explicitly gated from
conditioning any traded rule until H66–H68 (quadrant asymmetry at matched levels, grid
stability, duration dependence of quadrant exit) pass. This mirrors the credit-deep
dossier's Baron-Xiong finding in reverse: bank-equity holders there demand *no*
compensation for forecastable crash risk; an operator abandoning momentum right after a
crash is demanding compensation for a risk that, mechanically, has already been paid.

**Countermeasure.** Two mechanisms work together, deliberately not relying on operator
judgment at the worst moment. First, the **anti-capitulation lock**
(`docs/PIPELINE.md` §2.11): no parameter, budget, or structural change to the momentum
sleeve may be *initiated* while it is beyond a grid-defined drawdown depth — executing
the pre-registered vol-scaling and bear-state cut is always allowed; changing the rules
mid-pain never is. Second, the **re-entry family assigned specifically to momentum/fast
sleeves** (`docs/DESIGN.md` §5.7): re-entry is **vol-target implied**, not discretionary
— exposure scales back up mechanically as the sleeve's own trailing volatility falls
through its quantiles (the same Barroso-Santa-Clara form that cut exposure on the way
down), so the sleeve re-levers on a schedule set by its own risk state, never by an
operator's read of "has the world stopped being scary yet." Neither mechanism asks the
operator to be brave at the bottom; both remove the bottom as a decision point.

### G.3 Style drift after underperformance — the institutional evidence

**Mechanism.** The individual-operator biases in G.1–G.2 have a well-documented
institutional-scale twin: **Goyal & Wahal (2008)** study 3,400 US pension-plan sponsors'
hiring and firing of investment managers, 1994–2003, and find sponsors systematically
**hire** managers *after* large positive excess returns and **fire** them after
underperformance — textbook return-chasing at the institutional level, not merely the
retail level Greenwood-Shleifer document. The critical finding is what this
return-chasing buys: hired managers' subsequent excess returns are **not** better than
what the fired managers would have delivered had the sponsor simply stayed — in matched
round-trip fire-then-hire comparisons, the switch delivers **no** net benefit. Applied
to a momentum sleeve: a desk that reduces L3's weight, drifts the composite toward a
different lookback blend, or rotates toward whichever sleeve most recently outperformed
— purely *because* momentum has just underperformed, with no pre-registered hypothesis
driving the change — re-enacts the Goyal-Wahal pattern at one remove, with the same
expected result: no net improvement, paid for in transition cost and a broken track
record.

**Countermeasure.** The trial-budget/pre-registration discipline (CONTRACT §9;
`docs/PIPELINE.md` FL7/FL14) requires any change to which construct is "online" —
including a reweighting away from momentum toward another factor sleeve — to happen only
via the Challenger Protocol on **scheduled review dates fixed a year in advance**, never
in reaction to a recent stretch of underperformance. This is the same structural answer
as G.1 and G.2 in reverse: a manager cannot be fired-and-rehired inside this desk's own
architecture on the basis of a recent return alone, because "the online variant" is
itself a pre-registered, dated decision, not a standing discretionary call.

### G.4 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Buying the top of the strategy's own cycle | Diagnostic expectations (Greenwood-Shleifer; Bordalo-Gennaioli-Shleifer) applied to recent Sharpe, not just recent stock returns | Barroso-Santa-Clara vol-scaling + frozen decay haircut — sizing never responds to a recent good run |
| Abandoning at the bottom | Diagnostic expectations mirrored on losses; crash lands in the rebound (Daniel-Moskowitz), the least-trusted moment to hold; D-quadrant narrative capture | Anti-capitulation lock (no rule change mid-drawdown) + vol-target-implied re-entry (mechanical, not discretionary) |
| Over-reading the downturn/recovery phase label | Phase object new and tempting to over-interpret before it has earned trust | Phase consumption gate: quadrant/age logged everywhere, condition no traded rule until H66–H68 pass |
| Style drift after underperformance | Goyal-Wahal procyclical institutional hire/fire pattern, no net benefit in matched comparisons | Challenger Protocol: which construct is "online" changes only on pre-fixed scheduled review dates |
| Treating a compelling decay/crowding narrative as proof | HS-vs-DHS decay channel unresolved; a plausible story either way | Both hypotheses must clear the pre-registered, purged-CV test in the data phase before either is acted on |
| Ignoring the crowding monitor because momentum "still backtests well" | Lou-Polk comomentum and the live 2025 quant-crowding episode show crowding is measurable and current, not merely historical | Crowding monitor is a stated design element (`docs/DESIGN.md` §10), reduce-only signal on the sleeve, independent of backtest Sharpe |

None of these six countermeasures ask the operator to be wiser in the moment. Each
converts a live judgment call — size up after a good run, cut after a bad one, drift
style after underperformance, over-trust a new label, pick a side in an unresolved decay
debate, or dismiss a crowding signal because the backtest still looks fine — into a
structural non-decision, the only form of discipline this Part's evidence shows
survives contact with an actual momentum cycle.
