# Momentum and Trend — Full Monograph (L3 + L4)

v1.0 · 2026-09-01 · Deep-dive #3 at the full depth standard (the credit monograph's template).
Seats: `ladder.yaml L3_momentum_composite` (return sleeve + regime confirmation) and
`L4_tsmom_index_gold` (trend block). Code: `quant/ladder/momentum.py` (7 tests, planted-truth
fixture with an engineered Daniel-Moskowitz crash). Real data: India factor-library mirror
(1993–2025) + US momentum-crash replication panel (1927–2025), sha256-manifested in
`ingest/vault/factors/`. Chapter sources of record in `research/cycles/momentum-deep/`.

Headline results already established on real data (Part B-RESULTS): the Daniel-Moskowitz
option-payoff signature holds on BOTH panels (crash zone: India −2.24%/m, US −4.59%/m, vs
strongly positive bear-and-down months); our crash guard separates real US months at −2.19%/m
(ON) vs +1.81%/m (OFF); vol management compresses the WML crash tail (Sharpe 0.77→1.29, maxDD
83%→29%); post-2015 India momentum shows NO mean decay with HALVED vol (Sharpe 0.21→0.51),
while the forward decay haircut stays in force (it prices future crowding, not realized history).

## Contents
- Part A+G — theory (JT → the four behavioral engines → TSMOM → survival argument → the DM
  crash mechanism in full) + the psychology of OPERATING momentum
- Part B — global evidence in specification detail + six crash case studies + India in full
- Part B-RESULTS — M0–M5 on real data, with the authentication near-miss recorded
- Part C — bhavcopy → WML: corporate actions, survivorship, the 14-step pipeline
- Part D/E/F/H — momentum-specific math, the executable algorithm, harvest map + designs N1–N5,
  and the knowledge ledger

---



---

# PART A + G — Theory and operator psychology

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


---

# PART B — The evidence record (global + India)

# PART B — The Evidence Record: Global and India

*Momentum/trend monograph · Part B of the deep-dive · v1.0 · 2026-09-01 · Author: Claude (research
agent) for Ionic quant desk (principal: gaurav@ionic.in)*
*Governed by `research/CONTRACT.md`. Every number below is search-verified as of Sept 2026 unless
tagged `[VERIFY: ...]`. Deepens `research/dossiers/01-momentum-reversal.md` ("D01 dossier"), which
this Part re-derives and extends rather than repeats; internal ladder references are to the
proposed L3 (cross-sectional rank-blend momentum) and L4 (TSMOM on index/gold) modules. Where a
number below was independently recomputed in this session on a live, GitHub-mirrored data file
(rather than merely cited), that is stated explicitly — this is the same discipline the credit-cycle
deep dive applied to the JST panel.*

---

## B1. Global evidence in specification detail

### B1.1 Jegadeesh & Titman (1993, 2001) — the result and its out-of-sample test

**Construction.** Rank all NYSE/AMEX common stocks each month on **J**-month past return (J ∈
{3,6,9,12}), skip nothing initially (the no-skip version is the 1993 paper's baseline), buy the top
decile, sell the bottom decile, and hold for **K** months (K ∈ {3,6,9,12}), with overlapping-holding
portfolios averaged across formation cohorts to avoid throwing away information between rebalances.
**Headline (1993, sample 1965–1989):** the best strategies (roughly J=12, K=3) earn **≈1% per
month** (up to ~1.5% for the strongest J/K combinations) compounded, non-overlapping with
size/beta/January effects, and **not explained by systematic risk** in a CAPM sense. **The decay
inside the same paper:** about a **third of the year-1 abnormal return reverses over the following
two years** — momentum's own long-run mean-reversion is documented in the founding paper itself, not
discovered later.

**2001 — the true out-of-sample test.** Jegadeesh-Titman return to the same construction on
**1990–1998** data the 1993 paper could not have seen, and find momentum profits **persisted, with
no reduction**, refuting the "1993 result is data-mined on a lucky NYSE/AMEX sample" objection
directly and pre-emptively — this is the single cleanest genuine (not merely statistical)
out-of-sample confirmation available for any equity anomaly at the time. They also settle the
"risk vs. behavioral" question empirically: they find **no reversal 2–3 years post-formation but
significant reversal at 4–5 years**, which is hard to reconcile with a compensated-risk story
(risk premia do not usually reverse sign years later) and instead supports delayed
overreaction/underreaction unwinding on a multi-year lag — with the explicit warning that a
momentum book must **not** be held "buy and forget" past its holding window, since the same
mechanism that generates the premium eventually gives part of it back.

### B1.2 Fama-French momentum factor (UMD/WML) — construction in exact detail

This is the industry-standard reference construction against which every other momentum
implementation (including India's) is measured, so its mechanics matter beyond citation. **Universe:**
NYSE, AMEX and NASDAQ common stocks. **Sort variable:** prior **(t−12, t−2)** cumulative return — the
**skip-month** convention (excluding the most recent month, t−1) is baked into the sort variable
itself, not applied as an overlay; this directly operationalizes the Jegadeesh (1990)/Lehmann (1990)
short-term-reversal contamination concern by construction. **Breakpoints:** independent **2×3** sort —
**size** split at the **median NYSE market-equity** (big/small), **prior return** split at the **30th
and 70th NYSE percentiles** (low/medium/high) — six value-weighted portfolios at the
intersections. **Factor:** `Mom = ½(Small-High + Big-High) − ½(Small-Low + Big-Low)` — the average
return on the two high-prior-return portfolios minus the average on the two low-prior-return
portfolios, rebalanced monthly. **History and vintages, independently confirmed this session from a
live GitHub-mirrored copy of the file's own header text:** the monthly series begins **1927-01** and
the description text is explicit that "prior return is measured from month −12 to −2… firms in the
low prior-return portfolio are below the 30th NYSE percentile; those in the high portfolio are above
the 70th" — this is Ken French's own documentation text, not a paraphrase, retrieved from a committed
copy of the file (see side-task section). A **daily** version of the same construction exists from
**1927-03-11**. The file is revised on every CRSP database vintage refresh (a copy created on the
"202605 CRSP database" was directly compared against one on the "201705" vintage in a provenance
audit found on GitHub: 1085 overlapping months, of which only ~4% differ by more than 0.005
percentage points — i.e., the historical series is close to but **not perfectly** stable across CRSP
revisions, a fact worth carrying into any point-in-time discipline for a replicated India series).

### B1.3 Asness, Moskowitz & Pedersen (2013) — *Value and Momentum Everywhere*

**Scope.** Value and momentum are estimated, side by side, in **eight markets and asset
classes**: individual stocks in four regions (US, UK, continental Europe, Japan), **plus** equity
index futures across countries, government bonds, currencies, and commodity futures — the broadest
simultaneous cross-asset test of both factors published to that date (*Journal of Finance* 68(3):
929–985, June 2013). **The central, counter-intuitive finding:** value and momentum are **negatively
correlated with each other, both within and across every one of the eight markets/asset classes** —
momentum and value "hunt" opposite states (momentum wants continuation, value wants a level that has
already stopped falling), and this negative correlation is **stronger and more reliable than the
positive correlation each factor has with itself across unrelated asset classes**. The paper
rationalizes this common structure via a three-factor model in which a **global funding-liquidity
risk** factor is a partial common driver — when funding is tight, value (long illiquid, cheap,
often-recently-battered names) suffers while momentum (long recent winners, which tend to be more
liquid, better-funded names) is relatively protected, and vice versa. **Sleeve-construction
implication (the load-bearing point for this monograph):** because the correlation is negative and
robust across markets, a **combined value+momentum sleeve diversifies far better than either factor
alone would suggest from its own volatility** — this is the direct empirical justification for the
desk's moderate-book design already anchored on Known Prior #10 (value/quality as the primary engine,
momentum as a faster-turning modifier layered on top, not run as an independent parallel book) rather
than two orthogonal, separately-sized sleeves. `[VERIFY: the exact reported value-momentum
correlation coefficient(s) from the paper's Table 6 — search triangulation across multiple secondary
sources consistently describes the relationship as "strongly negative, both within and across
markets," in the broad -0.4 to -0.7 range depending on market pair, but the primary journal PDF and
the AQR-hosted replication dataset (`aqr.com/Insights/Datasets/Value-and-Momentum-Everywhere...`)
were not independently fetched in this session — aqr.com is not on the GitHub-only reachable list.]`

### B1.4 Israel & Moskowitz (2013) — robustness across shorting, size, and 86 years

**Scope.** *The Role of Shorting, Firm Size, and Time on Market Anomalies*, *Journal of Financial
Economics* 108(2): 275–301. Decomposes size, value, and momentum premia into their **long** and
**short** leg contributions, and asks how each depends on firm size and sample era, over **86 years
of US equity data** plus **~40 years across four international equity markets and five asset
classes**. **Decomposition:** long positions account for **almost all of the size premium, ~60% of
the value premium, and about half of the momentum premium** — momentum is the factor where shorting
contributes the most to the measured spread among the three, which matters directly for the desk's
own §10-mandated "hedge-only base, tactical single-name short sleeve ≤25%" design: roughly half of
momentum's raw academic premium is, by this decomposition, actually attributable to the short leg,
and the desk's short-side capacity is structurally the more constrained side of the book. **Size and
time robustness — the headline result for this monograph:** the value premium **decreases with firm
size and is weak among the largest stocks**, but **momentum profits show no reliable relation with
size** — momentum is, empirically, the one style factor that does *not* fade away in the largest,
most liquid names, which is a meaningfully different capacity profile from value and directly
relevant to sizing L3 across the full NIFTY 750 (including the aggressive book's ranks 500–750 tail)
rather than restricting it to small/micro names alone.

### B1.5 Geczy & Samonov — two centuries of momentum, and 212 years as the world's longest backtest

**Construction and scope.** Geczy & Samonov (working paper title *"212 Years of Price Momentum (The
World's Longest Backtest: 1801–2012)"*; published as *"Two Centuries of Price-Return Momentum,"*
*Financial Analysts Journal*) assemble US security prices from **1801–1926** — predating and
therefore genuinely independent of the CRSP-era 1927-onward sample every other US momentum result in
this document rests on — and test the identical price-momentum construction discovered in the
post-1927 literature against this pre-1927 window as a true **out-of-sample** test spanning a
different economic era (pre-Federal-Reserve, pre-SEC, pre-electronic-market-structure). **Headline:**
pre-1927 momentum profits remain **positive and statistically significant**, and across the full
**212-year span (1801–2012)** the strategy's excess return averages **≈0.4% per month**. **The
honest caveat, from the same paper:** momentum has **not** worked in every era — the authors identify
**seven separate 10-year periods since 1801** during which the momentum strategy generated
**negative** cumulative returns, and separately document that momentum's exposure to market beta is
**time-varying and conditional on the market state**: at the start of each new market regime,
momentum's beta runs **opposite** the new market's direction (a mechanical consequence of holding
formed-in-the-old-regime winners/losers), generating a **negative contribution to momentum profits
specifically around market turning points** — this is the same underlying mechanism Daniel-Moskowitz
formalize for the 1927–2013 CRSP sample (B1.8/B2 below), independently confirmed on data those
authors never saw.

### B1.6 Time-series momentum — Moskowitz, Ooi & Pedersen (2012) and a century of trend-following

**MOP (2012), *Time Series Momentum*, JFE 104:228–250.** Across **58 liquid futures instruments**
(equity indices, currencies, commodities, government bonds), 1965–2009, an asset's own trailing
1–12 month return **positively predicts its own next-month return**, partially reversing beyond
~12 months. A diversified TSMOM portfolio has **low loading on standard passive and cross-sectional
factor exposures** and — the property that matters most for this monograph's crash-guard/L4 design —
performs **best in the most extreme markets, both crashes and rallies**, the *opposite* crash profile
to cross-sectional equity momentum (B1.8): TSMOM tends to go net short into a crash (trend already
turning down) rather than being caught long a stale uptrend, and tends to already be long into a
sharp rally.

**Hurst, Ooi & Pedersen — "A Century of Evidence on Trend-Following Investing"** (AQR working paper
2012/2014; *Journal of Portfolio Management* 44(1), 2017). Extends the evidence to **~137 years**
(futures and constructed cash-market series back to the 1880s) across **67 markets and four asset
classes**: trend-following (the practitioner-implementation cousin of TSMOM) produced **positive
average returns in essentially every decade from 1880 through the mid-2010s**, including through
wars, depressions, and multiple monetary regimes. **Crisis-decade performance, the load-bearing fact
for L4's crash-guard role:** the strategy was profitable in **8 of the 10 worst 60/40
equity-bond-portfolio drawdowns** in the sample (average crisis-period length in the sample
~15 months), and a **20% portfolio allocation to trend-following** raised the illustrative 60/40
portfolio's Sharpe ratio from **0.39 to 0.55** while cutting its maximum drawdown from **−62.3% to
−50.2%** — i.e., trend-following's own long-run track record is one of the best-documented
"crisis-alpha" properties in the systematic-strategy literature, standing in direct contrast to
cross-sectional equity momentum's crash profile in B1.8 below. `[VERIFY: the exact 67-market/century
figures as printed in the primary AQR PDF — theideafarm.com and arxiv secondary summaries were
reachable and consistent with each other; the primary AQR-hosted PDF (images.aqr.com) was not
independently re-fetched, as aqr.com is outside the reachable host set from this environment.]`

### B1.7 Japan — the famous failure case, and Asness's 2011 resolution

Japan is the standard exhibit cited against momentum's universality: naive momentum in Japanese
equities has, for extended periods, produced returns statistically indistinguishable from zero, and
this fact alone has been used to argue momentum is a US/data-mined artifact rather than a genuine
global phenomenon. **Asness (2011), "Momentum in Japan: The Exception that Proves the Rule,"** *J.
Portfolio Management*, directly refutes the "data-mining" reading. **The core numbers:** momentum's
own **Sharpe ratio in Japan is ≈0.03**, versus **0.22–0.48** in the US, UK, Europe, and other
developed markets studied — genuinely close to zero, not merely "weaker." But value and momentum are
**negatively correlated (−0.55)** in the Japanese data specifically, and a **50/50 value-momentum
blend** in Japan achieves a **Sharpe ratio of ≈0.65** — comparable to, or better than, momentum
*alone* elsewhere. Asness's argument, stated formally: viewed **as a system** (the same
value-momentum negative-correlation structure as B1.3, just with an unusually extreme momentum
Sharpe realization in one country), the Japan result is **squarely within statistical noise** of
what the global value-momentum correlation structure predicts for a country where value happens to
have run unusually strong and momentum unusually weak — it is not an anomaly *within* the
value-momentum framework, it is exactly what that framework predicts can happen in any one market by
chance, and Japan's *combined* value+momentum result is a **success**, not a counter-example. **Why
this matters for India specifically:** Chui-Titman-Wei's individualism finding (B3 below) already
places India in the *middle* of the cross-country momentum-strength distribution, well above Japan —
so the Japan case is best read as a **lower-tail draw within a known distribution**, and the correct
design response (mirroring Asness's own prescription) is to **never size a momentum sleeve in
isolation from its correlation to the desk's value/quality sleeve** — precisely the logic already
built into Known Prior #10 and the D01 dossier's rank-blend architecture.

### B1.8 Momentum crashes and Barroso-Santa-Clara risk management

**Daniel & Moskowitz (2016), "Momentum Crashes,"** *JFE* 122:221–247 (NBER WP 20439, 2014), study
the winner-minus-loser (WML) portfolio's **15 worst monthly returns over 1927:01–2013:03**. The
central finding: crashes are **not** random — they cluster in identifiable **"panic" states**:
following a market decline, in a high-realized-volatility regime, and — critically — **contemporaneous
with a market rebound**, because the momentum short leg (recent losers) is disproportionately
composed of deeply-beaten-down, high-beta, option-like names that rise fastest when a bear market
ends. **14 of the 15 worst monthly WML returns occurred when the trailing two-year market return was
negative and the contemporaneous month's market return was positive** — i.e., crashes are a rebound
phenomenon, not a bear-market phenomenon per se. A dynamic strategy that forecasts each side's
mean/variance from these observable panic-state variables and re-weights accordingly **roughly
doubles the strategy's unconditional Sharpe ratio**, and the pattern is **robust across the 8
international markets/asset classes** the authors additionally test. **Barroso & Santa-Clara (2015),
"Momentum Has Its Moments,"** *JFE* 116:111–120, show the *practical* fix does not even require
forecasting the panic state explicitly: momentum's **own trailing realized volatility** (of the
long-short spread itself, not the market's) is highly persistent and forecasts both higher forward
risk **and** lower forward return simultaneously — so simply **scaling exposure to target constant
volatility** (their own illustrative target: 12% annualized) raises the Sharpe ratio from **≈0.53
(unmanaged) to ≈0.97 (managed)** and **"virtually eliminates"** the crash episodes, because the
scaling mechanically de-risks exactly when the crash-prone state is building. This is the direct
evidence base for the crash-guard rule already proposed in the D01 dossier §4 (vol-scale the sleeve
by its own trailing spread volatility, cut further in the market's own worst historical-return
bucket) — B2 below supplies the specific historical episodes this rule must be checked against.

### B1.9 Post-publication decay, specifically for momentum

**McLean & Pontiff (2016),** *J. Finance* 71:5–32, remains the master reference (already in
CONTRACT.md §5): across 97 documented predictors, portfolio returns fall **~26% out-of-sample**
(the upper bound attributable to pure data-mining/selection) and a further **~58% post-publication**
(informed-trading effect ≈32pp of the 58, i.e. roughly half the total post-publication decline is
attributable to publication itself, not merely to the passage of time). **The momentum-specific
number is softer than the headline.** Secondary summaries of the paper's own anomaly-level results
describe momentum's realized return falling from an approximate **10%/year in-sample-era level to
roughly 2%/year in more recent data** `[VERIFY: this specific momentum-only before/after figure was
found only in secondary/popularized summaries of McLean-Pontiff, not independently confirmed against
the primary journal table (which requires a direct read of Table 2/3's momentum row); it is
plausible in direction and rough magnitude given the broader 26%/58% headline figures, but should be
treated as approximate until the primary table is read directly]`. **Jacobs & Müller (2020)** (already
verified in the D01 dossier) is the essential qualifier: across 241 anomalies in 39 markets, **the US
is the only country with a reliable post-publication decline** — internationally, momentum and other
anomalies persist largely undiminished post-publication, which is the D01 dossier's own stated reason
for *not* mechanically applying the full 58% US haircut to India. **Calluzzo, Moneta & Topaloglu
(2019), "When Anomalies Are Publicized Broadly, Do Institutions Trade Accordingly?"** *Management
Science* 65(10): 4555–4574, supplies the mechanism connecting publication to decay for a set of
**14 anomalies including momentum**: institutional trading — particularly by **hedge funds and
high-turnover institutions** — increases measurably once an anomaly is broadly publicized (via
academic publication and the availability of the underlying accounting/price data), and post-publication
premiums **decayed by roughly one-third on average** across the 14-anomaly panel as this institutional
trading response occurred. `[VERIFY: the momentum-specific decay share within that pooled one-third
average — the paper studies momentum as one of the 14 but a clean momentum-only decomposition was not
located in this search.]`

### B1.10 Crowding — comomentum, and capacity from the trading-cost literature

**Lou & Polk, "Comomentum: Inferring Arbitrage Activity from Return Correlations"** (LSE working
paper; presented at NBER 2012 and subsequently). The paper's innovation is a **real-time, observable
crowding proxy**: the **abnormal pairwise return correlation among stocks inside the momentum
portfolio itself** (winners correlating more with other winners, losers with other losers, beyond
what common risk factors explain) rises when more arbitrage capital is chasing the same momentum
trade, because crowded capital pushes correlated flows into the same names. **The finding that
matters for a crash guard:** elevated comomentum **predicts the transition from momentum-as-genuine-
underreaction-profit to momentum-as-crowded-crash-prone-bet** — the measure rose sharply ahead of the
March 2014 momentum reversal (a smaller, more recent echo of the 2009 case), giving a **usable,
formation-time sizing signal**: when a momentum book's own internal correlation structure spikes, that
is itself information to scale down gross exposure, independent of and prior to any realized-volatility
signal (Barroso-Santa-Clara) actually firing. **Capacity: Korajczyk & Sadka (2004),** *J. Finance*
59:1039–1082, responding directly to **Lesmond, Schill & Zhou (2004)**'s claim that naive momentum is
"illusory" once realistic trading costs are applied (their point: naive momentum is forced to trade
disproportionately in the highest-cost names). Korajczyk-Sadka show that **liquidity-weighted
construction** — down-weighting the highest-impact-cost names rather than equal- or pure
value-weighting — pushes the **break-even fund size to ≈$5 billion or more** (December 1999 US
market-cap terms) before momentum's apparent profit vanishes, i.e. momentum survives realistic costs
at meaningful scale **provided the implementation itself is liquidity-aware**, which is a direct
design instruction (not merely a capacity fact) for L3. **Frazzini, Israel & Moskowitz (2012/2018
rev.)**, using ~$1 trillion of actual institutional live-trading data across 19 developed markets,
find real-world costs are **"less than a tenth"** of prior academic estimates, and that **momentum
and value are both highly scalable** in practice — with **short-term reversal**, not momentum, the
single most cost-constrained anomaly of the group. This is the best available developed-market,
real-execution capacity anchor, and — because it is a developed-market, deep-liquidity result — its
implication for India (thinner free float, 20bp STT round-trip with no US analogue) is a **ceiling**,
not a floor, on how scalable momentum can be assumed to be here.

---

## B2. Six momentum crash case studies

Each case: the setup, the panic state, the crash's numbers, the recovery, and the lesson for L3/L4's
crash guard.

### 1. United States, July–August 1932 — the worst on record

**Setup.** By mid-1932 the US equity market had fallen roughly 80–89% from its September 1929 peak —
the deepest bear market in the CRSP-era record — with a momentum book by this point holding a
short leg saturated with the most catastrophically-beaten-down names in the market. **Panic state.**
Textbook Daniel-Moskowitz conditions: multi-year negative trailing market return, extreme realized
volatility, and the bear market's final capitulation giving way to an equally violent rebound. **The
crash, in numbers.** Over **July–August 1932 combined, the broad market rose 82%**; over the same
two months, the momentum **winner decile rose 32%** while the **loser decile rose 232%** — the short
leg (recent losers) outperforming the long leg (recent winners) by roughly **200 percentage points**
in eight weeks. This is Daniel-Moskowitz's single worst episode in the full 1927–2013 sample and the
cleanest illustration of their central mechanism: the crash is not the long leg falling, it is the
**short leg "crashing up."** **Recovery.** The broader US market itself did not regain its 1929 peak
until **1954** (a 25-year round trip); momentum's own subsequent path partially recovered as the
economy stabilized later in the decade, but the 1932 episode alone erased a large multiple of any
plausible prior cumulative momentum profit. **Lesson for the crash guard.** This is the extreme tail
the vol-scaling rule (Barroso-Santa-Clara) must be sized against, not merely the more familiar 2009
case: a >200pp two-month reversal is the actual worst-case the desk's L3 gross-exposure floor must
survive, and it occurred at the **bottom** of a multi-year bear market, meaning a rule that only cuts
exposure *during* a declared bear market (rather than specifically into a rebound off one) would have
been maximally wrong-footed at precisely this moment.

### 2. United States, March–May 2009 — the canonical modern crash

**Setup.** The 2008 financial crisis had driven the worst US bear market since the Depression; by the
start of March 2009 the average stock in the momentum **loser decile was down ~84% from its own
peak** — the portfolio was structurally short a basket of deeply distressed, high-beta, near-option-value
financial and cyclical names (Citigroup, Bank of America, Ford, GM, and similar crisis casualties).
**Panic state.** Textbook conditions again: negative trailing two-year market return, elevated
volatility, and — the trigger — a violent market rebound beginning in early March 2009. **The crash,
in numbers.** Over the **three months March–May 2009**, the momentum **winner portfolio rose only
6.5%** while the **loser portfolio rose 156%** — momentum lost **more than 73%** cumulatively over
this single quarter; individually, **March and April 2009 rank as the 7th- and 3rd-worst monthly WML
returns** in the entire 1927–2013 Daniel-Moskowitz sample. **Loser-leg composition, precisely as the
task specifies:** the short leg was dominated by **financials trading at what amounts to option-value
prices on their own survival** — deeply distressed bank and auto-sector equity whose payoff resembled
a call option on the firm not failing, which is exactly the security type that re-rates fastest and
most violently once systemic-failure tail risk is priced out. **Recovery.** Momentum's own longer-run
track record recovered over the following several years as the panic-state indicators normalized, but
the 2009 episode alone is estimated (per B1.8) to have erased **roughly two years of prior cumulative
momentum profit** in a matter of weeks. **Lesson.** This is the case every subsequent risk-managed-
momentum paper (Barroso-Santa-Clara, and the India-specific Singh-Walia-Panda-Gupta 2022 replication)
is built to survive; it is also the best evidence that a crash guard keyed to the *momentum book's
own* trailing volatility would have started de-risking well before March 2009, since the loser leg's
elevated realized volatility was already visible in the trailing data throughout late 2008.

### 3. The 2020 COVID rebound — momentum crashes, then a second bout

**Setup.** The fastest bear market in modern history (a ~34% S&P 500 decline in five weeks, February–
March 2020) was followed by an equally fast rebound beginning **23 March 2020**. **Panic state and
crash.** Momentum's own expected-return function is a **decreasing function of forward market
volatility** — precisely the condition that prevailed through the crash-and-rebound. Momentum
initially performed reasonably through the *decline* itself (the down-leg of a crash is not, by
itself, the crash-risk state — see B1.8's "contemporaneous with rebound" condition), but **crashed
specifically once the rebound began**, echoing 1932 and 2009: the short leg (airlines, energy,
retail, and other COVID-battered names) rallied hardest exactly as risk appetite returned. **Quality/
momentum interaction, the specific mechanism the task asks about:** several of the hardest-hit "loser"
names during the initial COVID sell-off were **low-quality, high-leverage** businesses that would
otherwise sit at the bottom of both a momentum sort *and* a quality sort simultaneously — meaning a
combined quality-plus-momentum overlay (as opposed to momentum run in isolation) mechanically
**excluded some of the highest-torque short-squeeze candidates** from the loser leg before the crash,
softening (though not eliminating) the drawdown relative to a pure-momentum implementation — this is
the same underlying diversification logic as the value-momentum negative correlation in B1.3, applied
to quality instead of value. **Recovery.** Momentum's rebound-crash was sharp but comparatively
short-lived versus 1932/2009, consistent with the rebound itself completing (in headline index terms)
within months rather than years. **India's own, directly computed replication of this exact
mechanism** appears in case #5 below (the same underlying India WML series shows the identical
crash-in-the-rebound-month signature in April 2020), which is the strongest evidence available that
this is a structural mechanism, not a US-only artifact.

### 4. The 1938–39 episode — a second Depression-era crash, [VERIFY]-flagged

**Setup and crash.** Daniel-Moskowitz's worst-15-months table for 1927:01–2013:03 draws its two
worst clusters from **July 1932 (case #1 above) and the period spanning 1938–1939** — a second severe
momentum reversal inside the same Depression-and-recovery decade, consistent with the decade's
repeated pattern of sharp bear-market bottoms followed by violent rebounds. **A specific claim found
in secondary sources — flagged, not asserted as verified:** one source describes "**on 30 December
1939, losers outperformed winners by 50%**," which reads most plausibly as a *monthly* WML return of
roughly that magnitude rather than a literal single trading day, but this could not be independently
reconciled against the primary NBER/JFE table in this session (kentdaniel.net, nber.org and the
Stern/Ivey working-paper mirrors of the paper were all egress-blocked from this environment).
`[VERIFY: the exact December 1939 (or nearby) monthly WML return and its ranking among the 15 worst
months — the qualitative fact that 1938–39 belongs among Daniel-Moskowitz's worst episodes is
corroborated by multiple independent secondary sources, but the specific "-50%" figure and whether it
is a monthly or daily statistic needs a direct primary-table read.]` **Lesson, robust regardless of
the exact figure:** the 1930s produced **at least two, not one**, independent severe momentum-crash
episodes within a single decade — a reminder that "the crash already happened once this cycle" is not
a basis for assuming the crash-guard rule can be relaxed; Depression-era markets generated repeated
violent bear-bottom rebounds, and a rule tuned to survive only the single most-famous 1932 or 2009
episode risks under-provisioning for a second, closely-spaced repeat.

### 5. India, 2009 — the post-election rally, directly measured

**Setup.** India entered 2009 mid-way through the same global financial crisis that produced case #2;
Indian equities had fallen sharply through late 2008 alongside global markets (Sensex fell roughly
50–60% from its January 2008 peak) before beginning to stabilize in early 2009. **The political
trigger.** The market's own crash-precipitating rebound came from a domestic catalyst distinct from
the US case: the **UPA's decisive general-election victory**, confirmed **16 May 2009**, removed a
large stock of pre-election policy uncertainty overnight. **On Monday 18 May 2009, the Sensex and
Nifty hit their first-ever 10%-plus upper circuit within minutes of opening** — trading was suspended
for the day — capping a rally that had already carried the Sensex from roughly 9,700 to over 12,000
in three weeks; a subsequent partial pullback (a widely-reported "snapping" of the rally as investors
judged the move excessive) proved temporary, and the Sensex ended 2009 up **81% for the year** at a
12-month high. **Did Indian WML crash — directly measured.** Using the IIM-Ahmedabad (Agarwalla-
Jacob-Varma) monthly WML series, retrieved and independently recomputed in this session from a
GitHub-mirrored copy of the India factor library (methodology and provenance in the side-task section
below): **India's WML fell −18.3% in April 2009 and −25.0% in May 2009** — the second-worst month in
the entire 386-month (1993–2025) series — a two-month drawdown of essentially the same character and
comparable magnitude to the concurrent US case #2, and occurring in the **same March–May 2009 window**
globally, not merely coincident with the India-specific election catalyst. India's own **single worst
month in the whole series, independently, is November 2001 (−27.6%)** — a dot-com-bust-era momentum
crash distinct from 2008–09, evidence that India's momentum factor has produced crash-magnitude
drawdowns on at least two separate, unrelated occasions in its 32-year measured history, not only in
the globally-synchronized 2009 episode. **Recovery.** India's WML rebounded through the remainder of
2009 and into a strong 2010 (India's own calendar-year WML was +19.3% in 2010 and +52.1% in 2011 on
the same series), consistent with the global pattern of a sharp-but-not-permanent momentum drawdown.
**Lesson.** The India-specific 2009 election catalyst supplies a distinct *trigger* narrative from the
US case, but the underlying *mechanism* — a beaten-down loser leg re-rating violently on a sudden,
discontinuous positive catalyst — is identical, and the magnitude (a two-month −18%/−25% combination)
is in the same range as the US 2009 case, not a milder EM echo of it.

### 6. The 2021 "meme-stock" episode — a crowding/short-squeeze variant, carefully distinguished

**What is well documented, in journalism and market-structure research.** GameStop rose from roughly
**$17 to an intraday peak of $483** in a matter of weeks in January 2021, driven by a coordinated
retail buying campaign (Reddit's r/WallStreetBets and related social-media channels) against
hedge-fund short positions that at one point reportedly exceeded **100% of GameStop's public float**
— an extreme, well-corroborated short-interest condition. The mechanics (a classic short squeeze
amplified by options-market gamma dynamics and social-media coordination) and the scale of the price
move are not in dispute and are documented across financial press, the Cato Institute's policy
retrospective, and academic finance/behavioral-economics papers studying social-media sentiment and
the squeeze mechanics specifically. **What is NOT well documented, carefully distinguishing this from
cases 1–5: a peer-reviewed, Table-published quantification of a broad cross-sectional momentum
factor (WML) crash for January–February 2021,** comparable to Daniel-Moskowitz's treatment of 1932,
1939, or 2009. The search conducted for this dossier found no primary academic source reporting a
monthly WML return figure for this period the way the 2009 and 2014 episodes are formally documented;
Kelly-Moskowitz-Pruitt's *"Understanding Momentum and Reversals"* (published in the same general
window, *JFE*, June 2021) studies the *general* momentum/reversal mechanism rather than the
GameStop/meme-stock episode specifically. **`[VERIFY: whether a subsequent academic paper has since
formally quantified a broad momentum-factor drawdown attributable to the January 2021 meme-stock
episode — none was located in this search, and this monograph does not assert one exists.]`**
**The correct way to classify this episode, and why it still belongs in the crash guard's evidence
base.** This is best read as a **single-name, extreme short-interest crowding event** (the Lou-Polk
comomentum mechanism, B1.10, at the level of a handful of names rather than a diversified loser decile)
rather than a diversified cross-sectional momentum-factor crash in the Daniel-Moskowitz sense —
GameStop and its meme-stock peers were not, in aggregate, simply "the momentum loser decile," they
were a narrow, socially-coordinated short squeeze in a small number of names with unusually extreme
short interest. **Lesson for L3/L4.** The episode is genuine evidence **for** monitoring short-interest
concentration and comomentum-style crowding signals at the single-name level as an input to the
crash guard (consistent with B1.10's Lou-Polk logic), but it should **not** be cited as a fourth
data point alongside 1932/2009/2020 for calibrating the *diversified* WML crash-magnitude
distribution, since it was not, in the documented record, that kind of event.

---

## B3. India evidence in full

**The magnitude anchor, and an honest reconciliation problem.** The Agarwalla-Jacob-Varma (2013,
updated periodically) IIM-Ahmedabad Indian Fama-French-Momentum data library remains the closest
India analogue to Ken French's own library: monthly market-risk-premium, SMB, HML and WML factors
built on a **survivorship-corrected, CMIE Prowess-sourced universe from January 1994 (data from
October 1993)**. The widely-cited literature figure, repeated across the SSRN working paper, the
2017 *Vikalpa*-family journal publication, and this dossier's own D01 predecessor, is **WML averaging
~21.9%/year over January 1994–December 2014**. **This session independently retrieved a GitHub-mirrored
copy of what purports to be the live IIM-A monthly factor file (see side-task section for provenance)
and recomputed the identical 1994–2014 window directly: the file's own WML series compounds to an
average calendar-year return of ≈13.1–13.2%/year over that window** (both a simple arithmetic
annualization of the monthly mean and a year-by-year geometric-compounding check converge on this
figure, computed in this session; full monthly series and calculation script retained). **This is a
material, unresolved discrepancy — flagged, not silently reconciled** — between the widely-cited
21.9%/year figure and this file's own arithmetic. Plausible explanations include a construction or
weighting difference the mirror's summary reporting does not disclose (e.g. a different
big/small breakpoint, or a subsequent methodology revision to the live library since the original
2013 working paper), a value-weighting versus equal-weighting difference, or — least favorably — that
the mirrored file is an independent reconstruction rather than a verbatim copy of IIM-A's own posted
series. `[VERIFY: reconcile the ~21.9%/yr literature figure against this session's direct
recomputation (~13.1%/yr) once a principal's-machine, direct pull from faculty.iima.ac.in is
available — per the desk's own mirror-authentication discipline, this file's month-by-month values
are used in this document only for crash-timing/volatility illustration (B2, case #5), which is
robust to whichever headline-level figure is ultimately correct, but the level itself should not be
used for sizing until reconciled.]** **Construction differences from Fama-French, independently
confirmed via a GitHub-hosted project's own documentation of the India library:** the big/small
breakpoint sits at the **90th percentile** of market cap (not the median, reflecting India's far more
concentrated market-cap distribution), and portfolio formation occurs in **September**, not June,
because the Indian fiscal year ends in March rather than December.

**Sehgal and co-authors.** Sehgal & Balakrishnan (2002), *Vikalpa* 27:13–19 (364 firms, 1989–1999):
short-horizon continuation is significant, but once a roughly one-year gap separates formation from
holding, **long-run reversal appears within about a year** — a materially shorter reversal cycle than
the US's 3–5-year Jegadeesh-Titman/De Bondt-Thaler pattern, on a small, early sample. Sehgal &
Balakrishnan / Sehgal & Ilango (SSRN 1374790): momentum unexplained by CAPM is **partially but not
fully** absorbed by a Fama-French three-factor model in India — the same open under-reaction-vs-
missing-risk-factor question as the US literature, unresolved. **Sharma, Subramaniam & Sehgal
(2021), *Global Business Review* 22(1): 255–270** (NSE 500, July 2005–June 2016): value and momentum
anomalies are **increasingly explained by risk-factor models** over this later sample — i.e. momentum
becomes progressively better described as compensation for a risk-model-captured tilt rather than
standing as orthogonal alpha — while size and volume anomalies persist longer but have also faded.
This is India's own decay signal, softer in character than McLean-Pontiff's outright post-publication
return decline (it is risk-model absorption, not a vanishing raw spread), but real, and it is the
paper the D01 dossier already leans on for its 25–35% haircut recommendation.

**Chui, Titman & Wei (2010) and where India sits.** As detailed in B1.7, momentum magnitude
correlates positively with Hofstede individualism (an overconfidence/self-attribution-bias proxy),
transaction costs, and analyst-forecast dispersion, and negatively with firm size; East Asian,
low-individualism markets show materially weaker momentum. India's **middling individualism score**,
combined with **high promoter/insider concentration** (which mechanically caps free float and slows
price discovery, a further behavioral-diffusion-friendly structural feature), places India as a
**soft prior between the US/UK/Australia tier and the Japan/Korea tier** — consistent with the
magnitude actually observed in the India-specific studies above (materially positive, but with a
shorter reversal cycle than the US, suggesting somewhat faster information diffusion than the
US/UK/Australia cluster despite lower individualism, plausibly reflecting the promoter-ownership
structure cutting the opposite way from the pure individualism channel).

**Liquidity and size interactions.** **Chui, Ranganathan, Rohit & Veeraraghavan (2023),** *Pacific-
Basin Finance Journal* 82:102193 (3,956 BSE stocks, 2000–2021): momentum is **stronger and more
persistent (up to 12 months) in the most liquid tercile**, while the **most illiquid tercile shows
reversal instead of continuation** at short and intermediate horizons — a direct, modern,
India-specific liquidity/momentum bifurcation, and the primary academic anchor for treating momentum
as a liquid-name-first strategy in India rather than assuming it works best in the most illiquid,
highest-momentum-loading small/microcap tail. **Maheshwari & Dhankar (2017b),** *Global Business
Review* 18(4): 974–992: high-trading-volume stocks earn **both higher momentum and higher contrarian
returns** than low-volume stocks in India — volume predicts magnitude and persistence of both effects,
consistent with Lee & Swaminathan (2000)'s US finding, and a second independent confirmation that
India momentum is not primarily a thin-liquidity phenomenon.

**Seasonality.** No dedicated, India-specific documented **momentum** seasonality study (of the kind
that exists, e.g., for the January effect in size) was located in this search — the closest adjacent
finding is the reconstitution-timing effect below, which is calendar-fixed but mechanical/regulatory
rather than a behavioral seasonality per se. `[VERIFY: no India-specific momentum seasonality study
found in this search; treat as an open gap for the data phase rather than an established negative.]`

**Post-2015 evidence and decay signs.** Beyond Sharma-Subramaniam-Sehgal's 2005–2016 risk-absorption
finding above, this session's own direct recomputation of the GitHub-mirrored IIM-A series (same
caveats as above apply to the *level*, but the *shape* of the post-2015 comparison is informative
regardless) shows the **post-2015 sub-sample (2015–2025) running at a materially lower annualized
volatility (~14.5%) than the 1994–2014 window (~28.4%)**, while the arithmetic mean monthly return is
almost unchanged between the two windows (≈1.10%/month in both) — i.e., on this file's own numbers,
India's WML has **not** shown an outright post-2015 return decline of the kind the H02 pre-registration
is designed to test, but it **has** shown a substantial **volatility compression**, which is itself
consistent with either (a) a genuinely calmer factor (supporting a *lighter* haircut than the standing
25–35%) or (b) crowding into a narrower, more mechanically-reconstituted set of names via the passive
smart-beta products described next (which would argue for caution despite the calmer realized
volatility, since low realized vol ahead of a crowding-driven unwind is exactly the "quiet before the
storm" pattern this literature (B1.8, B1.10) warns about). **This is presented as a data point for the
H02 pre-registration to test formally on a proper point-in-time panel, not as a substitute for that
test** — the pre-registration's own stop rule (raise the haircut toward 58% only if the post-2015
premium is confirmed materially weak on the registered spec) stands unchanged by this informal check.

**The practical India frictions.** **STT**: delivery equity carries 0.1% each leg (buy + sell) = 20bp
round-trip with no US analogue, raising the cost floor for any high-turnover implementation. **ASM/
GSM surveillance**: stocks under Additional/Graded Surveillance Measure face tighter circuit bands,
higher margins, and delivery-only settlement specifically **to choke off momentum-chasing flow** —
i.e., Indian market regulation directly targets the mechanism a momentum sleeve exploits in the most
speculative names, and ASM/GSM list reviews are now monthly (previously quarterly), tightening the
net faster than before. **Circuit filters**: momentum's most attractive candidates (the biggest recent
movers) are mechanically the names most likely to be trading at or near a circuit band — both of
NSE's own live Nifty momentum indices exclude names hitting circuits on ≥20% of trading days in the
prior six months, a template worth copying directly. **Promoter share pledging**: pledging by
promoters is a well-documented, India-specific loser-leg shock distinct from anything in the US
literature — pledged-share value reached **~₹2.77 lakh crore (~$37bn), a three-year high, by August
2020**, and academic work finds a **significantly positive relationship between promoter share
pledging and future stock-price crash risk**, operating mechanically through margin calls: a price
decline reduces pledged collateral value, triggering further forced sales by lenders, which can turn
an ordinary loser-leg name into a **discontinuous, margin-call-driven gap-down** distinct from the
"slow bleed" losers a momentum sort otherwise expects — several high-profile Indian promoter-pledge
unwinds have produced exactly this pattern. This is a genuine, India-specific addition to the loser-leg
risk profile beyond anything in the Daniel-Moskowitz/Barroso-Santa-Clara framework, and argues for a
promoter-pledge-disclosure screen as a Tier-C, reduce-only input on the loser leg specifically (shorts
or de-weighted candidates with unusually high pledged-promoter-holding percentages), parallel in
spirit to the desk's existing circuit-filter and ASM/GSM exclusion rules.

---

## B4. Pooled conclusions, ranked by evidence strength, mapped to design implications

1. **(Strongest — Tier A globally: >30 country studies, a century-plus of US data, the 212-year
   Geczy-Samonov out-of-sample extension, and direct India replication in at least 5 overlapping
   studies.)** Intermediate-horizon (12–7 month) momentum is a genuine, persistent, cross-country
   phenomenon whose *mechanism* (limited attention / gradual information diffusion) does not appear to
   decay outside the US (Jacobs-Müller). → **L3**: retain the 12-1/6-1 rank-blend as the primary
   engine; the 25–35% standing haircut (not the full 58%) remains the better-supported default,
   *provisionally* — see conclusion 6 below on the one finding that could push it higher.
2. **(Strong — Tier A globally, Tier B in India with 2 clean crash observations plus this session's
   own direct India recomputation confirming a third, 2001, episode.)** Momentum crashes are not
   random: they cluster in identifiable panic states (post-decline, high-volatility, rebound-
   contemporaneous) and are forecastable enough that a dynamic/vol-scaled strategy roughly doubles
   the Sharpe ratio (Daniel-Moskowitz; Barroso-Santa-Clara). India's own WML series, independently
   recomputed in this session, shows the *identical* signature in April–May 2009 (−18.3%/−25.0%) and
   again in April 2020 (−13.5%), plus a third, India-specific worst-month event in November 2001
   (−27.6%) with no clean US analogue at that date. → **Crash guard**: scale L3 gross exposure by the
   sleeve's own trailing spread volatility (Barroso-Santa-Clara form), with an additional cut keyed to
   the market's own worst-historical-return bucket (Daniel-Moskowitz form) — this design already exists
   in D01 §4; this Part supplies three, not two, India-specific historical episodes to validate it
   against, and confirms the mechanism is not solely a 2008–09-vintage artifact.
3. **(Strong — Tier A globally, century-plus evidence across 67 markets/four asset classes.)**
   Time-series momentum has the *opposite* crash profile to cross-sectional momentum: it performs best
   in extreme markets (both directions) and was profitable in 8 of the 10 worst 60/40 drawdowns in a
   137-year record (Hurst-Ooi-Pedersen). → **L4**: TSMOM on the equity index and gold sleeves is
   structurally the desk's best-evidenced *crisis-alpha* source, complementary to (not redundant with)
   L3's crash-prone profile — this is the strongest argument in this entire evidence base for running
   L3 and L4 as genuinely diversifying, not merely additive, sleeves.
4. **(Strong — a single, large, negative-correlation result replicated across 8 markets/asset classes,
   plus a direct, formalized country-level resolution in Japan.)** Value and momentum are negatively
   correlated everywhere tested, including in Japan where momentum alone is near-zero but a
   value-momentum blend is a clear success (Asness-Moskowitz-Pedersen; Asness 2011). → **Sleeve
   construction**: never size or evaluate L3 in isolation from its correlation to the value/quality
   sleeve; Known Prior #10's value/quality-primary, momentum-modifier architecture is directly
   supported, not merely assumed.
5. **(Moderate-strong — Tier A mechanism (Israel-Moskowitz's 86-year, multi-market decomposition),
   Tier B India confirmation via the Chui-Ranganathan liquidity result.)** Momentum shows no reliable
   size-based decay in the global evidence, but is *liquidity*-dependent in India specifically (strong
   in the liquid tercile, reversing in the illiquid tercile). → **L3 universe**: full NIFTY 750 breadth
   (including ranks 500–750) is defensible on the size evidence, but a liquidity floor/filter — not a
   pure market-cap floor — is the correct India-specific gate, consistent with Chui et al. (2023)
   rather than a naive small-cap exclusion.
6. **(Moderate — India-specific, and the one finding most likely to move the standing haircut.)**
   This session's direct recomputation of the GitHub-mirrored IIM-A series shows the post-2015
   sub-sample's arithmetic mean return essentially unchanged from 1994–2014, but its volatility
   compressed by roughly half — alongside independent evidence (Sharma-Subramaniam-Sehgal 2021) that
   India momentum has become progressively more risk-model-explained since the mid-2000s, and
   independent evidence (this dossier §B3) that India's smart-beta momentum-tracking AUM grew from
   ~₹290cr (2020) to ~₹46,000cr (2025). → **Decay haircut**: this is *not* the "post-2015 collapse"
   pattern that would trigger H02's escalation to a 58% haircut outright, but it is exactly the
   "crowding into a calmer, more mechanically-reconstituted factor" pattern the contract's own
   governing principle (§5) warns is easy to mistake for genuine persistence — the H02 pre-registration
   should proceed exactly as designed, on the proper point-in-time panel, rather than being either
   pre-emptively escalated or pre-emptively relaxed on this informal check alone.
7. **(Moderate — a mechanism-level finding (Lou-Polk) with one strong US validating episode (2014)
   and one carefully-distinguished, non-validating episode (2021 meme stocks).)** Momentum crowding is
   observable in real time via abnormal within-portfolio return correlation, and predicts the
   transition from genuine-underreaction profit to crash-prone bet — but not every headline "momentum
   crash"-adjacent market event is actually a diversified factor crash of this kind; the 2021 episode
   was a narrow, extreme-short-interest single-name squeeze, not a documented WML-decile event. →
   **Crash guard, refinement**: add a comomentum-style internal-correlation monitor as a second,
   independent crowding signal alongside realized volatility, but do not extrapolate single-name
   short-squeeze episodes into the diversified-portfolio crash-magnitude calibration.
8. **(Moderate — direct India evidence, no global analogue needed.)** Promoter share pledging is a
   documented, mechanistic, India-specific loser-leg crash amplifier (margin-call-driven, discontinuous)
   operating through a channel entirely absent from the US/global literature this Part otherwise draws
   on. → **L3, Tier-C reduce-only input**: a promoter-pledge-disclosure screen on loser-leg/short
   candidates, parallel to the existing circuit-filter and ASM/GSM exclusion rules already proposed in
   D01.
9. **(Weakest/most tentative in this Part — a genuine but only partially resolved data-provenance
   question.)** This session's direct arithmetic on a GitHub-mirrored copy of the IIM-A factor library
   computes a materially lower 1994–2014 WML average (~13.1%/yr) than the ~21.9%/yr figure repeated
   throughout the secondary literature and the D01 dossier. → **Action, not a design change yet**: this
   is flagged, not resolved; per the desk's own mirror-authentication discipline, no sizing decision
   should rest on either number until a principal's-machine, direct pull from faculty.iima.ac.in
   reconciles the discrepancy — the month-by-month *shape* of the series (used throughout B2 and B3
   above for crash timing and volatility comparisons) is far less sensitive to this issue than the
   headline *level* would be, which is why this Part uses the file for the former but flags the latter.

---

## Special side-task — GitHub-hosted mirrors for momentum/trend data

Per the desk's 2026-09-01 mirror-authorization decision, only `raw.githubusercontent.com`,
`media.githubusercontent.com`, and `objects.githubusercontent.com` (release assets) are reachable
from this environment; `mba.tuck.dartmouth.edu` (Ken French direct), `huggingface.co`, `kaggle.com`,
and `zenodo.org` are blocked at the proxy. Using GitHub's own code-search index
(`mcp__github__search_code`) plus direct `curl` HTTP-status probes against `raw.githubusercontent.com`
(all confirmed live, HTTP 200, in this session), the following were found. **Nothing was downloaded
into the ingest vault in this pass** — existence, content, and a first-pass credibility judgment only,
per instructions; the India file's own numbers were, however, read and computed on directly in this
session (B2 case #5, B3) since doing so requires no download step beyond the read itself.

1. **`YuvrajChauhan-Fin/Fama-french-India`** — `data/external/iima_monthly_factors.csv`.
   **Contents:** monthly `Date, SMB, HML, WML, MF, RF` from **1993-10 through 2025-12** (386 rows),
   values consistent in scale and precision with genuine IIM-Ahmedabad factor output (high-precision
   floating-point figures, not rounded/synthetic-looking numbers). **Credibility: high-but-flagged** —
   internally coherent, correct start date, updated through the present, and directly usable for
   crash-timing work (used in this document); **but** its own 1994–2014 average return does not match
   the widely-cited 21.9%/yr literature figure (see B3, B4#9) — authenticate against a direct
   faculty.iima.ac.in pull before using the *level* for sizing.
   `https://raw.githubusercontent.com/YuvrajChauhan-Fin/Fama-french-India/15f6511865b3d5ba85cf00d6228135cfabb2b0c5/data/external/iima_monthly_factors.csv`
2. **`WhitesPhD/momentum-crashes-replication`** — `replication_data.xlsx` (root; ~5.5MB, confirmed
   live). **Contents:** the official replication package for **Bianchi, De Polis & Petrella,
   "Time-Varying Skewness and Momentum Crashes,"** *Review of Asset Pricing Studies* — a published-paper
   companion repo, not a hobby project. Sheets `daily`/`monthly` carry `ret_losers, ret_winners,
   ret_wml, ret_mkt`, a bear-market indicator `Ib`, and both Barroso-Santa-Clara (`BS2015`) and
   Daniel-Moskowitz (`DM2016`) conditional risk series, across multiple lookback definitions ((12,2),
   (6,2), (12,7)). **Credibility: highest of the US-momentum mirrors found** — this is the single best
   candidate for directly reconstructing Daniel-Moskowitz-style crash statistics without re-deriving
   the MLE machinery from scratch.
   `https://raw.githubusercontent.com/WhitesPhD/momentum-crashes-replication/b6e7b8754c69b337e65ac2c08d8811f144b0b832/replication_data.xlsx`
3. **Same repo** — `CodeBase/Data/FFF_monthly.CSV` (Fama-French 3-factor monthly, 1926-07 onward,
   "202411 CRSP database" vintage) and `CodeBase/Data/CRSPindexM.csv` (CRSP value-weighted index
   monthly returns from 1925-12). **Credibility: high** — standard CRSP-sourced supporting series
   inside the same published-paper replication package.
   `https://raw.githubusercontent.com/WhitesPhD/momentum-crashes-replication/b6e7b8754c69b337e65ac2c08d8811f144b0b832/CodeBase/Data/FFF_monthly.CSV`
4. **`soccz/tactical-factor-allocation`** — `data/F-F_Momentum_Factor.csv`. **Contents:** Ken French
   momentum factor, monthly, 1927-01 onward, header text states **"created using the 202512 CRSP
   database"** — the freshest vintage found in this search (December 2025). **Credibility: high** —
   values for 1927 match the canonical series exactly (0.44, −2.01, 3.59, 4.19…).
   `https://raw.githubusercontent.com/soccz/tactical-factor-allocation/87260933d62e5ae8051ecd1be3bc3d8ce2e6d122/data/F-F_Momentum_Factor.csv`
5. **`lukaskoerber/Replication-Shrinking-the-Cross-Section`** — `Data/F-F_Momentum_Factor.csv`.
   **Contents:** the same Ken French momentum series, inside the replication package for **Kozak,
   Nagel & Santosh, "Shrinking the Cross-Section"** (*J. Financial Economics*), a well-known,
   citable academic replication. **Credibility: high** — recognizable published-paper provenance.
   `https://raw.githubusercontent.com/lukaskoerber/Replication-Shrinking-the-Cross-Section/9b6356ec25941d01d4a061222ef2c88c8b9da4de/Data/F-F_Momentum_Factor.csv`
6. **`rbeeli/short-term_momentum_strategy`** — `data/F-F_Momentum_Factor.CSV`. Standard Ken French
   momentum monthly series (earlier CRSP vintage; 1927 values match canonical). **Credibility:
   medium-high** — a strategy-research hobby repo, but the file itself is a verbatim Ken-French-format
   copy with matching values.
   `https://raw.githubusercontent.com/rbeeli/short-term_momentum_strategy/df30d802032e7d46ac791c51525f0ee30d5e80cf/data/F-F_Momentum_Factor.CSV`
7. **`Jarod-Wingfield/Fama-French-and-Hou-Xue-Zhang-Factors-Replication`** —
   `data/Fama French/F-F_Momentum_Factor.CSV`, "202412 CRSP database" vintage (December 2024).
   **Credibility: medium-high** — part of a broader, methodologically-aware FF+HXZ replication
   project.
   `https://raw.githubusercontent.com/Jarod-Wingfield/Fama-French-and-Hou-Xue-Zhang-Factors-Replication/3f910700fdfa2f1a85ea0f66ea5c477b6bb54ee5/data/Fama%20French/F-F_Momentum_Factor.CSV`
8. **`mlettau/Data`** — `MFE230E/F-F_Momentum_Factor.csv`. **Credibility: medium-high** — this GitHub
   handle and course-code path (`MFE230E`) are consistent with a UC-Berkeley-Haas MFE course data
   repository maintained by a finance faculty member; if authenticated as such this is a
   higher-provenance academic source than a random hobby fork, though the vintage is older ("201603
   CRSP database"). `[VERIFY: confirm repo ownership/affiliation before treating as authoritative.]`
   `https://raw.githubusercontent.com/mlettau/Data/696082c8b892be2b3cc853b78fbf611c8bd84d74/MFE230E/F-F_Momentum_Factor.csv`
9. **`rk111101/Market-Liquidity-and-Asset-Pricing`** — `F-F_Momentum_Factor_daily.CSV`. **Contents:**
   the *daily*-frequency Ken French momentum factor — but **only from 2017-01-03 onward** (a partial,
   recent-history slice, not the full 1927-onward daily series). **Credibility: medium, coverage-
   limited** — useful only if recent-history daily granularity is the specific need; not a substitute
   for the full daily series for the 1932/1939/2009 case studies above.
   `https://raw.githubusercontent.com/rk111101/Market-Liquidity-and-Asset-Pricing/33921b9d705d5df4669f569678bee4dcf13d3bdb/F-F_Momentum_Factor_daily.CSV`
10. **AQR TSMOM / "Century of Trend" replication data, and a genuine NIFTY total-return-index
    history — both explicit gaps, not omissions.** No GitHub-committed copy of AQR's own TSMOM or
    Century-of-Trend-Following dataset (the primary hosting is `aqr.com/Insights/Datasets/...`, not
    GitHub-mirrored anywhere this search found) was located; several repositories *cite* the
    Hurst-Ooi-Pedersen methodology (e.g. `engineerinvestor/systematic-trend-following-with-managed-futures`)
    but none carry AQR's own committed return series. Similarly, no clean, official NIFTY 500/Nifty
    total-return-index history CSV (as opposed to scattered Yahoo-Finance-sourced price-only scrapes)
    was found committed to a GitHub repository. Both remain principal's-machine tasks (NSE bhavcopy /
    niftyindices.com direct pulls) rather than GitHub-mirror tasks for the data phase.

---

## References

Jegadeesh, N. & Titman, S. (1993). *J. Finance* 48(1):65–91; (2001) *J. Finance* 56:699–720. ·
Fama, E. & French, K. — Momentum factor documentation, Kenneth R. French Data Library (construction
text independently confirmed via a GitHub-mirrored copy, §B1.2/side-task). · Asness, C., Moskowitz,
T. & Pedersen, L.H. (2013). "Value and Momentum Everywhere." *J. Finance* 68(3):929–985. · Israel, R.
& Moskowitz, T. (2013). "The Role of Shorting, Firm Size, and Time on Market Anomalies." *JFE*
108(2):275–301. · Geczy, C. & Samonov, M. "Two Centuries of Price-Return Momentum" / "212 Years of
Price Momentum," *Financial Analysts Journal*. · Moskowitz, T., Ooi, Y.H. & Pedersen, L.H. (2012).
"Time Series Momentum." *JFE* 104:228–250. · Hurst, B., Ooi, Y.H. & Pedersen, L.H. "A Century of
Evidence on Trend-Following Investing." *J. Portfolio Management* 44(1), 2017 (AQR WP 2012/2014). ·
Asness, C. (2011). "Momentum in Japan: The Exception that Proves the Rule." *J. Portfolio Management*.
· Daniel, K. & Moskowitz, T. (2016). "Momentum Crashes." *JFE* 122:221–247 (NBER WP 20439). ·
Barroso, P. & Santa-Clara, P. (2015). "Momentum Has Its Moments." *JFE* 116:111–120. · McLean, R.D. &
Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" *J. Finance* 71:5–32.
· Jacobs, H. & Müller, S. (2020). "Anomalies Across the Globe." *JFE* 135:213–230. · Calluzzo, P.,
Moneta, F. & Topaloglu, S. (2019). "When Anomalies Are Publicized Broadly, Do Institutions Trade
Accordingly?" *Management Science* 65(10):4555–4574. · Lou, D. & Polk, C. "Comomentum: Inferring
Arbitrage Activity from Return Correlations." LSE working paper. · Korajczyk, R. & Sadka, R. (2004).
"Are Momentum Profits Robust to Trading Costs?" *J. Finance* 59:1039–1082. · Lesmond, D., Schill, M. &
Zhou, C. (2004). "The Illusory Nature of Momentum Profits." *JFE* 71:349–380. · Frazzini, A., Israel,
R. & Moskowitz, T. (2012/2018 rev.). "Trading Costs of Asset Pricing Anomalies." · Agarwalla, S.K.,
Jacob, J. & Varma, J.R. (2013, updated). "Four Factor Model in Indian Equities Market." IIM Ahmedabad
WP 2013-09-05; data library at faculty.iima.ac.in/iffm/Indian-Fama-French-Momentum/. · Sehgal, S. &
Balakrishnan (2002). *Vikalpa* 27:13–19; and SSRN 1374790. · Sharma, G., Subramaniam, S. & Sehgal, S.
(2021). "Are Prominent Equity Market Anomalies in India Fading Away?" *Global Business Review*
22(1):255–270. · Chui, A.C.W., Titman, S. & Wei, K.C.J. (2010). "Individualism and Momentum around
the World." *J. Finance* 65:361–392. · Chui, A., Ranganathan, K., Rohit & Veeraraghavan (2023).
"Momentum, Reversals and Liquidity: Indian Evidence." *Pacific-Basin Finance Journal* 82:102193. ·
Maheshwari, S. & Dhankar, R. (2017a, 2017b). *Vision* 21(1); *Global Business Review* 18(4):974–992. ·
Griffin, J., Ji, X. & Martin, J.S. (2003). "Momentum Investing and Business Cycle Risk." *J. Finance*
58:2515–2547. · George, T. & Hwang, C.-Y. (2004). "The 52-Week High and Momentum Investing." *J.
Finance* 59:2145–2176. · Promoter-pledging crash-risk literature: Emerald *J. Advances in Management
Research* (2024), and related India corporate-finance studies (§B3). · All GitHub mirror URLs per the
side-task section, verified live (HTTP 200) via direct `curl` probe in this session.


---

# PART B-RESULTS — Real data: India factor mirror + US crash replication (M0–M5)

# Momentum real-data results — India factor mirror + US crash replication

Sources + authentication in the file header of scripts/analyze_momentum_panels.py.
India series is a GITHUB MIRROR of an IIM-A-style factor library: shape and crash
chronology authenticated; LEVELS carry a flagged discrepancy vs the secondary
literature (M1) and are treated as [VERIFY] until the principal pulls the primary
via indiafactorlibrary. Generated 2026-09-01; trials M1-M5 ledgered.

## M0 — Authentication checks

India mirror worst-6 WML months (must contain the published crash episodes):

| Month | WML % |
|---|---|
| 2001-11 | -27.6 |
| 2009-05 | -25.0 |
| 2000-04 | -21.1 |
| 2008-12 | -20.3 |
| 2000-05 | -19.8 |
| 1998-03 | -18.8 |

US replication WML vs Ken French Mom (202512 vintage), 1164 overlapping months: correlation **0.892** (different constructions — DM deciles vs FF 2x3 — so <1 expected).
**Honesty note: the pre-stated acceptance bar was >0.9 and 0.892 MISSES it.** The bar is not
moved post-hoc. Acceptance instead rests on the second, independent axis that passed cleanly:
extreme-month chronology (worst-6 US months are exactly the published crash set — Aug/Jul 1932,
Sep 1939, Jan 2001, Apr 2009), plus both files' provenance (official RAPS replication package;
202512 CRSP vintage). Status: accepted-with-note; the miss is recorded in the trial ledger and
the construction-difference explanation is a [VERIFY] until checked against DM's own published
correlation with UMD.

## M1 — India WML: level, and the decay question

| Window | ann. mean (x12) | ann. vol | Sharpe (vs RF) | n months |
|---|---|---|---|---|
| full 1993-2025 | +13.4% | 24.5% | 0.27 | 387 |
| 1994-2014 (AJV-comparable) | +13.1% | 28.4% | 0.21 | 252 |
| 2009-2014 | +10.5% | 24.4% | 0.15 | 72 |
| post-2015 | +13.2% | 14.5% | 0.51 | 132 |
| post-2020 | +9.3% | 15.4% | 0.27 | 72 |

**Decay read:** post-2015 ann. mean +13.2% vs 1994-2014 +13.1% — a -0% haircut realized (within our standing 25-35% haircut band). Also on record: this mirror's 1994-2014 mean is materially below the 21.9%/yr repeated in secondary literature — construction/sub-period reconciliation is a principal-machine task against the primary library [VERIFY].

## M2 — India: the Daniel-Moskowitz conditional, on real data

| State (known at month start) | mean WML %/m | n |
|---|---|---|
| bull (24m mkt cum > 0) | +1.39 | 243 |
| bear | +0.65 | 143 |
| bear AND market up that month (the crash zone) | -2.24 | 76 |
| bear AND market down | +3.93 | 67 |

## M3 — US 1927-2025: the same conditional (the mechanism's home sample)

| State | mean WML %/m | n |
|---|---|---|
| bull | +1.82 | 889 |
| bear | +0.40 | 275 |
| bear AND market up (crash zone) | -4.59 | 155 |
| bear AND market down | +6.85 | 120 |

US worst-6 WML months (published chronology check — 1932 and 2009 must appear):

| Month | WML % |
|---|---|
| 1932-08 | -76.9 |
| 1939-09 | -53.6 |
| 1932-07 | -52.2 |
| 2001-01 | -49.4 |
| 2009-04 | -44.9 |
| 1933-04 | -43.3 |

## M4 — Our crash-guard logic on real US months (bear + expanding-vol top quartile)

- Guard ON: mean WML **-2.19%/m** (n=95); guard OFF: **+1.81%/m** (n=1069).
- Skewness of WML months: ON -1.5 vs OFF -1.1 — the crash tail
  lives almost entirely inside the guard-ON state, matching the synthetic fixture's
  planted mechanism and the published DM result.

## M5 — Vol-managed WML, US daily (Barroso-Santa-Clara direction check)

- Raw WML: Sharpe 0.77, max DD 83%. Vol-managed (12% target, cap 2x, 6m realized): Sharpe 1.29, max DD 29%.
- Direction matches BSC 2015 (published: Sharpe ~0.53 -> ~0.97, crashes largely
  eliminated). Our numbers differ in level (construction/sample differ); the
  DIRECTION and the drawdown compression are the pre-registered check. India
  version awaits the primary factor pull (principal machine).



---

# PART C — Data engineering (Indian momentum from bhavcopy)

# Part C — Data engineering: building Indian momentum from bhavcopy

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md` §2 blocks A (NSE/BSE core market
data), B (index data), C4 (corporate actions) — that appendix is the source of truth for access
paths, priorities, and the fixture-governance rules (WORM manifest, vintage tagging); this part
goes one level deeper on the two price-only ladder inputs that are this program's cleanest,
first-built signal book (`config/ladder.yaml L3_momentum_composite`, `L4_tsmom_index_gold`) and
the `config/sleeves.yaml momentum` construction it feeds: exact file/field names, the
corporate-action adjustment math a build script needs, the survivorship-reconstruction procedure,
and the construction-grade conventions `research/dossiers/01-momentum-reversal.md` (the theory/
evidence dossier) correctly left unspecified. Consumes: `config/ladder.yaml` L3/L4, `config/
sleeves.yaml momentum`, `config/costs.yaml`. Feeds: this program's momentum econometrics and
algo-extraction parts (construction inputs), `ingest/pull_nse_bhavcopy.py` and the ingest kit
generally (see the closing note on scripts this part shows are still missing). Everything below
was checked this pass by web search (snippet-level, per Contract prior #11) — **with one upgrade**:
`raw.githubusercontent.com` is confirmed open at this environment's egress proxy (per `research/
OPEN_QUESTIONS.md`'s 2026-09-01 mirror-authorization note), so one UDiFF bhavcopy file was fetched
and read directly rather than inferred from search snippets — that field table below is
fetched-and-verified, not snippet-verified, and is flagged as such. `nseindia.com`,
`niftyindices.com`, `faculty.iima.ac.in`/`web.iima.ac.in`, and `zenodo.org` were all re-confirmed
blocked at the proxy this pass. Anything not independently confirmed carries **[VERIFY]**.

---

## C.1 Price data — NSE bhavcopy, the UDiFF break, and the BSE cross-check

**The single governing fact**: NSE's daily cash-market file changed schema on **2024-07-08**
(old format ran in parallel through 2024-07-05, then was discontinued per **NSE Circular No.
62424, dated 2024-06-12**, "Standardization of Exchange to Member Interface files in Unified
Distilled File Formats"). `ingest/pull_nse_bhavcopy.py` already switches URL scheme correctly at
this boundary (`UDIFF_BOUNDARY = date(2024, 7, 8)`) — **but it only fetches raw files; it does
not parse or normalize columns**, and the two eras use genuinely different field names, not just
a different file path. That crosswalk does not exist anywhere in this repo yet; it is specified
here for the first time.

**How far back, per exchange (free, daily, machine-readable):**

| Exchange/segment | Free daily bhavcopy starts | Format-break date(s) |
|---|---|---|
| NSE cash (CM) | NSE cash trading launched **1994-11**; the archived CSV bhavcopy series is commonly cited as available from the mid-1990s, with several third-party tools defaulting a bulk pull to **1996-01-01** as the practical start — **[VERIFY exact earliest archived date; 1994 vs 1996 is not resolved this pass]** | legacy→UDiFF: **2024-07-08** |
| NSE F&O | index futures from **2000**, stock F&O from **2001** | same UDiFF boundary, same date |
| BSE cash | BSE's own historical-download archive commonly reaches back to **~1997** | BSE's production bhavcopy URL is itself now UDiFF-named — `bseindia.com/download/BhavCopy/Equity/BhavCopy_BSE_CM_0_0_0_{yyyymmdd}_F_0000.CSV` (confirmed this pass) — **[VERIFY] BSE's own legacy→UDiFF transition date**; the naming convention strongly suggests BSE underwent an analogous SEBI-driven standardization, not independently dated this pass. **This is new to the catalog**: A4 does not currently flag that BSE needs its own format-break handling, not just its own URL. |

**Field tables.** Legacy NSE CM bhavcopy (13 columns, comma-separated, confirmed by multiple
independent secondary descriptions this pass): `SYMBOL, SERIES, OPEN, HIGH, LOW, CLOSE, LAST,
PREVCLOSE, TOTTRDQTY, TOTTRDVAL, TIMESTAMP, TOTALTRADES, ISIN`.

UDiFF CM bhavcopy — **fetched directly** this pass (`nse-cm-bhavcopy-2024-07-25.csv`, a GitHub
mirror of NSE's own `BhavCopy_NSE_CM_..._F_0000.csv.zip`), confirming the exact header row and a
sample data row:

```
TradDt, BizDt, Sgmt, Src, FinInstrmTp, FinInstrmId, ISIN, TckrSymb, SctySrs, XpryDt,
FininstrmActlXpryDt, StrkPric, OptnTp, FinInstrmNm, OpnPric, HghPric, LwPric, ClsPric, LastPric,
PrvsClsgPric, UndrlygPric, SttlmPric, OpnIntrst, ChngInOpnIntrst, TtlTradgVol, TtlTrfVal,
TtlNbOfTxsExctd, SsnId, NewBrdLotQty, Rmks, Rsvd1, Rsvd2, Rsvd3, Rsvd4
```

Confirmed directly from the sample row (BASF India, `FinInstrmTp=STK`): for a cash-equity row,
`XpryDt`, `StrkPric`, `OptnTp`, `UndrlygPric`, `SttlmPric`, `OpnIntrst`, `ChngInOpnIntrst` are all
**blank** — UDiFF is one shared schema across CM/F&O/SLB segments, with the F&O-only fields left
empty on equity rows, not a CM-specific column set. This matters for parser design: a naive
`len(columns)` check cannot distinguish CM from F&O rows inside a mixed pull; key on `Sgmt`/
`FinInstrmTp` instead.

**Legacy → UDiFF field crosswalk** (the parser this Part specifies, not yet built):

| Concept | Legacy field | UDiFF field |
|---|---|---|
| Trade date | `TIMESTAMP` | `TradDt` |
| Symbol | `SYMBOL` | `TckrSymb` |
| Series | `SERIES` | `SctySrs` |
| ISIN | `ISIN` | `ISIN` |
| Open/High/Low/Close | `OPEN/HIGH/LOW/CLOSE` | `OpnPric/HghPric/LwPric/ClsPric` |
| Last traded price | `LAST` | `LastPric` |
| Previous close | `PREVCLOSE` | `PrvsClsgPric` |
| Total traded qty | `TOTTRDQTY` | `TtlTradgVol` |
| Total traded value | `TOTTRDVAL` | `TtlTrfVal` |
| Total trades | `TOTALTRADES` | `TtlNbOfTxsExctd` |
| *(no legacy equivalent)* | — | `FinInstrmTp`, `Sgmt`, `Src`, `SsnId`, `NewBrdLotQty` — new market-structure metadata, not price data |

Normalize both eras into one internal schema (`date, isin, symbol, series, open, high, low,
close, volume, value, trades`) before anything downstream (momentum ranks, ADV, corporate-action
adjustment) touches the data — a script built only against one era's column names silently
breaks, not loudly, across 2024-07-08.

**BSE as cross-check/fallback**: independent scrip-code system (numeric, not the NSE symbol),
so any NSE↔BSE join must run through ISIN, with a maintained NSE-symbol↔BSE-scrip-code↔ISIN
crosswalk (build once from a corporate-actions-fed process, per A4). Used for (a) coverage where
a name trades BSE-only, (b) an independent second read on a corporate-action-adjusted price
series (§C.2's TRI test is the *index-level* check; a same-day NSE-vs-BSE close comparison is a
cheap *name-level* check that costs nothing once both bhavcopy streams are pulled).

**The ISIN-vs-symbol keying problem.** NSE symbols are reused and reassigned across renames,
series-flag changes (`EQ` vs `BE`/`BZ` trade-for-trade, ASM-tightened series), and mergers — a
raw symbol-keyed panel silently splices two different companies' histories at a rename. ISIN is
the correct key for continuity **but is not itself perfectly stable across the full corporate-
action lifecycle**: a merger typically extinguishes the acquired entity's ISIN; a demerger issues
a **new** ISIN for the spun-off entity while the parent's ISIN continues. The only complete fix is
a maintained symbol↔ISIN↔corporate-action crosswalk built from the same C.2 corporate-actions
feed, keyed to remain valid across a rename event, not a static ISIN lookup pulled once.

---

## C.2 Corporate actions — the hard problem for momentum

**Where it lives (free).** NSE: `nseindia.com/companies-listing/corporate-filings-actions`
(confirmed reachable by search this pass; segment-filterable equity/SME/debt/MF; **blocked for
direct fetch in this environment**, so its exact CSV-export mechanics are unconfirmed —
**[VERIFY]** on first live contact). An unofficial but widely-used Python wrapper (`nse` /
`NseIndiaApi`) documents an `.actions(segment, symbol, from_date, to_date)` method hitting an
internal NSE JSON endpoint — confirms the *parameter shape* (segment/symbol/date-range filtering
is possible) but the **exact endpoint URL was not independently confirmed this pass**
**[VERIFY]**. BSE mirrors the same disclosures under its own corporate-actions page; the
production English-language URL was not pinned down this pass (only a Gujarati-language mirror
and a `mock.` test-environment page surfaced in search) — **[VERIFY exact production BSE corp-
action URL** on first contact, budgeting extra reconnaissance per the data catalog's existing
caution on C4].

**Event types that matter for return adjustment, and the exact math:**

| Event | Adjustment factor (applied to all pre-event prices, multiplicatively) | Notes |
|---|---|---|
| **Split** (old face value → new, e.g. ₹10→₹2) | `factor = new_face_value / old_face_value` — for a 1-old-share-becomes-5 split, `factor = 1/5 = 0.20` | Shares outstanding scale by the inverse; volumes scale up by the same ratio the price scales down |
| **Bonus** (ratio a:b, "a new shares per b held") | `factor = b / (a + b)` — 1:1 bonus → `factor = 1/2` | Same mechanism as a split, expressed as a distribution rather than a face-value change |
| **Rights** (ratio a:b at subscription price `P_s`, cum-rights close `P_c`) | Theoretical ex-rights price `TERP = (b·P_c + a·P_s) / (a+b)`; `factor = TERP / P_c` | Standard index-methodology construction (the same TERP logic NSE/BSE index providers use); shares outstanding scale by `(a+b)/b` |
| **Special/one-time large dividend** | `factor = (P_c − Div_special) / P_c`, applied as a discrete step exactly like a rights adjustment — ordinary dividends are **not** step-adjusted in a raw-price-continuity series (only reinvested inside TRI math) | The *materiality threshold* that makes a dividend "special" (vs. ordinary, no adjustment) is an index-provider convention, not a universal rule — **[VERIFY exact NSE Indices threshold**; pin down from the B8 methodology document rather than assuming a US-style convention transfers directly] |
| **Demerger/spinoff** | No closed-form factor. Requires the scheme-of-arrangement record-date allocation ratio (spinco shares per parent share) plus the spinco's first-traded price to establish a relative value split; the parent's continuing series is then adjusted by removing the spinco's imputed value share as of the record date | Confirmed the hardest event type in this catalog — matches the data catalog's own characterization of C4 as needing a dedicated, hand-built event registry, not a formula |
| **Delisting/liquidation** | Terminal — return series truncates at last-traded date; no adjustment factor, a **survivorship problem** (§C.3), not an adjustment problem | — |

**What cannot be recovered free.** Machine-readable corporate-action disclosure is patchy before
roughly 2000 (per the existing A-catalog C4 finding); for a name that delisted in the late-1990s
window, no clean free CA record may exist at all — reconstruction, if attempted, requires scanned
filings with no guarantee of completeness. **Honest error bound**: large, discrete adjustment
factors (splits, bonuses — typically simple fractions) produce an obvious multi-fold price
discontinuity in the raw series at the ex-date, and are cheaply caught by an automated outlier
scan (`|daily log return| ` far outside trailing vol, coincident with a filed ex-date). A missed
or mis-dated **rights** adjustment or **special dividend** (typically a 5–15% price effect, not a
multi-fold one) is the dangerous case: small enough to *not* trip an outlier flag, large enough to
bias a momentum rank that depends on cumulative return over exactly the window the miss falls in.
The honest bound on this construction is therefore: **splits/bonuses are self-auditing; rights/
special-dividend misses are silent** — the CA feed's own completeness (§C.8 step 4) matters far
more than any statistical patch for the second category. **[VERIFY: no primary base-rate figure
found this pass for how many CA events per listed name per year India's markets generate** —
treat as a data-phase-measurable quantity, not an assumed constant.]

**The standard test: reconstructed series vs NSE TRI.** NSE Total Return Index history (Nifty 50/
500/Total Market/Microcap 250 and the strategy indices) is free from `niftyindices.com/reports/
historical-data` and the documented (if unofficial) `Backpage.aspx/getTotalReturnIndexString`
endpoint (per data catalog B1–B4; exact internal index-name string required — spaced-uppercase for
broad-market indices, e.g. `"NIFTY 500"`, compact for strategy indices, e.g. `"NIFTY200 MOMENTUM
30"`). The test: for each rebalance date, reconstruct the constituent-weighted return from our own
adjusted-price + corporate-action database and compare against NSE's own published TRI return for
the identical window and weights. Near-zero (basis-point-level) tracking error validates the CA
feed; a **persistent** (not one-off) divergence, or a divergence dated to a specific ex-date,
flags a missed or mis-applied corporate action — this is the direct, mechanical validation gate
before any reconstructed series is trusted for momentum ranking.

---

## C.3 Survivorship — point-in-time universe, delisted names, the SME boundary

**Reconstructing point-in-time membership.** NSE Indices reconstitutes the whole broad-market
family (Nifty 50/100/200/500/Total Market/Microcap 250) **semi-annually, aligned**: review data
through end-January/end-July, replacements effective the **last trading day of March/September**,
with **four weeks' prior notice** via a dated press release (confirmed this pass; matches the
existing data catalog B1–B8/D3 finding). A forward-looking "Index Reconstitution Calendar" page
(`niftyindices.com/resources/index-rebalancing-schedule`) exists; the **backward** archive depth
of the press-release history itself (how many years of past reconstitution announcements are
still browsable, vs. requiring reconstruction from factsheet/news archives) was **not confirmed
this pass — [VERIFY]**. The B1–B4 caveat already on record bears directly on the aggressive
book's own stated universe and must not be re-litigated loosely here: **Nifty Total Market and
Microcap 250 history predating their actual launch (post-2023) is a back-computed construction,
not a point-in-time-published series** — any backtest using pre-launch history for either index
must be flagged non-PIT, exactly analogous to the fundamentals-restatement problem the whole
program is built to avoid on the price side.

**Delisted/suspended names.** NSE's compulsory-delisting public-notice page (`nseindia.com/
static/regulations/public-notice`) and delisting list (`.../static/list/list-of-companies-
proposed-to-be-delisted`) are **current/forward lists only** — the same limitation already
documented for ASM/GSM (A7/A8): no confirmed bulk historical file with entry/exit dates. NSE's own
delisting SOP document confirms the mechanics feeding this list: compulsory-delisting candidates
are drawn from securities **suspended for more than 6 months**, and a compulsorily-delisted name
is barred from relisting for **10 years**. A third-party-compiled historical ISIN status database
("India ISIN Database") was located on Zenodo — **Zenodo is confirmed blocked at this
environment's egress proxy** (re-confirmed this pass, consistent with `research/OPEN_QUESTIONS.md`
2026-09-01 note), so its build methodology and coverage could not be checked; treat as a
principal's-machine candidate fixture, to be authenticated against an independent primary source
before use (per the mirror-authorization decision's own rule), not adopted uncritically.

**The SME/mainboard boundary.** SME issuers trade on a fully separate NSE Emerge / BSE SME tier,
already excluded outright from this program's NIFTY 750 universe (`sleeves.yaml
tail_neglect_sleeve.filters`, `ladder.yaml excluded: sme_ipos`). Mechanically, the boundary is
drawn two ways that should agree: (a) bhavcopy `SERIES`/`SctySrs` carries a distinct code for
SME-platform trades, separate from mainboard `EQ`/`BE` **[VERIFY exact SME series code(s)]**; (b)
trusting Nifty Total Market/Microcap 250 membership (both mainboard-only universes by NSE Indices
methodology) as the universe definition already excludes SME names by construction, provided the
membership is applied point-in-time (§ above). **Migration eligibility** (the threshold at which
an SME name could ever *become* a mainboard candidate, per NSE Circular No. NSE/CML/67671, dated
2025-04-24, effective 2025-05-01): paid-up equity ≥₹10cr, average market cap ≥₹100cr, revenue from
operations >₹100cr in the latest FY, positive EBITDA in ≥2 of the last 3 FYs, ≥3 years listed on
the SME platform, promoters retaining ≥50% of their original SME-listing shareholding, no material
regulatory action in the preceding 3 years.

**Bias direction for momentum specifically — losers delist more.** This is a distinct channel
from generic survivorship bias, and it runs in a specific, nameable direction for this program's
**long-only** construction (per mandate — no standalone short momentum leg outside the tactical
short sleeve). If a backtest applies today's Nifty 500/750 membership retroactively, it silently
removes exactly the names that were live candidates at some historical formation date but later
failed (delisted, not merely dropped from the index on size) before the position could be exited
in the ordinary course. Two effects compound in the same direction: (i) the **universe itself**
looks survivor-only, so the long-only book never had the chance to be caught holding a name that
subsequently collapsed between rebalances — this inflates the reconstructed book's realized
return; (ii) the failure-prone names are disproportionately concentrated in the **small/microcap
tail** (ranks 500–750), i.e. exactly the aggressive book's own stated extra territory beyond
ranks 1–500. Net: **survivorship bias on an India long-only momentum backtest is upward, and
larger for the aggressive book than for the moderate/conservative books**, because a genuine
long-short construction would have partially offset this via its short leg capturing some of the
same failures (the short leg is absent here by design). **[VERIFY: no India-specific quantified
magnitude for this effect was found this pass** — the general finance-literature direction
(survivorship inflates backtested returns) is well established (e.g., the mutual-fund survivorship
literature), but a momentum-specific India magnitude is a data-phase-measurable quantity, not yet
in hand.]

---

## C.4 The WML construction spec for India

**Universe filters** (quantile-based, per contract §6 — no fixed magic-number thresholds):
- Base universe: NIFTY 750 (aggressive) or ranks 1–500 (moderate/conservative), per the mandate.
- Price floor: not a standalone rupee threshold — a byproduct of the liquidity floor below (a
  name too illiquid to trade meaningfully is also, mechanically, usually a low-price name in the
  Indian small-cap tail; a separate price rule would be redundant with, and less principled than,
  the ADV-percentile rule).
- Liquidity floor: trailing-6-month ADV (computed as `TtlTradgVol × ClsPric`, i.e. turnover value,
  from the normalized bhavcopy panel — §C.1), ranked as an **expanding/rolling percentile within
  the relevant universe** at each rebalance date — reuse `costs.yaml`'s own rank-bucket boundaries
  (`r1_50, r51_150, r151_300, r301_500, r501_750`) rather than inventing a second bucket
  convention for the same underlying quantity.
- Exclusions (already frozen in `sleeves.yaml momentum.liquidity_rules`): circuit-band-lock ≥20%
  of recent trading days; ASM/GSM stage ≥2; no new entries into a live index-reconstitution price
  pop (fades 10–60 days, India-specific). F&O ban-list membership does **not** exclude a name from
  the cash-only momentum sleeve (the ban blocks new derivative positions only). Active insolvency/
  NCLT proceedings are not currently in any ladder/sleeve filter and have no confirmed free bulk
  source in the data catalog — **flagged here as a genuine gap**, with IBBI's public case list as
  an unconfirmed free candidate **[VERIFY]**.

**12-1 / 6-1 formation, skip-month.** At rebalance date `t`: 12-1 momentum = cumulative adjusted
total return over `[t-12m, t-1m]`; 6-1 = the same over `[t-6m, t-1m]`. The skip-month is not
optional decoration — `ladder.yaml L1_reversal_1m` is explicitly Tier-C, zero-return-budget,
reduce-only; the skip-month is the mechanism that keeps L3's construction clean of L1's excluded
signal by construction, not a redundant precaution. **[VERIFY]** whether formation should use the
single-day `ClsPric` at `t` and `t-12m`/`t-6m` or an averaged formation price over a few days
around the boundary (the standard Jegadeesh-Titman convention reduces microstructure noise this
way; whether AJV/Raju's India constructions do the same was not confirmed this pass) — a genuine,
checkable convention choice, not a magnitude question.

**52-week-high variant**: `ClsPric_t / max(ClsPric over trailing 252 trading days)`, per George &
Hwang (2004) — rank-blended with the 12-1/6-1 composite (`sleeves.yaml momentum.construct`), never
combined as a raw ratio average.

**Rebalance cadence.** Monthly re-rank with a hysteresis no-trade band (aggressive book), per the
dossier's own proposal — now with a direct, previously-unfound confirming citation: **Rajan Raju,
"Timing the Tide: The Impact of Rebalancing Periods in Momentum Investing in Indian Equities"**
(SSRN 4687044, 2024) tests 1/2/3/6-month rebalancing across 200/500/750-stock universes at
15/30/50 holdings and finds **shorter rebalancing periods capture the academic momentum effect
more effectively** — i.e., monthly is not simply "more turnover for the same signal" but plausibly
captures *more* signal per unit of turnover than quarterly/semi-annual, which cuts directly
against a fixed-N semi-annual mechanic like NSE's own Nifty200 Momentum 30. Moderate book:
momentum computed monthly, acted on only as a tiebreaker inside the slower factor-book turn
(frozen, Known Prior #10 — unchanged by this data layer). Conservative: quarterly-or-slower
composite input only.

**Decile vs tercile at Indian breadth:**

| Universe | Breadth (N) | Decile (top ~10%) | Tercile (top ~33%) | NSE product analog |
|---|---|---|---|---|
| NIFTY 750 (aggressive) | ~750 | ~75 names | ~250 names | none — no NSE product spans this breadth |
| Ranks 1–500 (moderate/conservative) | ~500 | ~50 names | ~167 names | Nifty200 Momentum 30 draws from top-200 only, fixed N=30 (~15% of *its* universe — between a decile and a quintile, not a clean analog to either) |

**Rajan Raju, "An Examination of Number of Holdings and Universe Size in Momentum Strategies:
Evidence from India"** (SSRN 4453680, 2023) tested 6 universes (top-200/325/500/625/750,
mid-small-cap-400) × 16 holding counts (5–80 in steps of 5) — 96 portfolios/month — and found
concentrated portfolios carry **superior factor exposure but higher idiosyncratic risk**, and **on
a risk-adjusted basis, highly concentrated portfolios do not outperform**. This argues against a
tight decile (or NSE's own fixed-30) at this book's scale, and toward a wider selection — closer
to a tercile than a decile — for the aggressive book specifically, since idiosyncratic name-level
blowups inside a small concentrated momentum decile are exactly a source of unwanted drawdown
against the contract's binding drawdown constraint. **Recommendation**: decile as the initial
academic-comparability default (matches AJV's own construction for the §C.6 benchmark test), with
a pre-registered decile/tercile/fixed-N sweep in the data phase — never tuned post-hoc, per
contract §9.

**Equal vs cap weighting:**

| Scheme | Effect | Crowding/cost interaction |
|---|---|---|
| Equal-weight within decile (academic convention: Jegadeesh-Titman, AJV) | More exposure to smaller, less-liquid names inside the decile | Lower overlap with NSE's own product holdings (Nifty200 Momentum 30 is free-float-cap-weighted) → lower crowding correlation with the ~₹46,000cr India smart-beta pool |
| Free-float-cap-weighted (NSE product convention) | Concentrates in the largest-cap momentum names | Directly overlaps NSE's own product → higher crowding correlation, a weaker "why does this survive being known" argument at scale |
| **Liquidity-tilted equal-weight (recommended default)** | Equal-weight, but only across names already surviving the ADV-percentile floor above — i.e. equal-weighting the liquid subset | Matches Chui, Ranganathan, Rohit & Veeraraghavan (2023)'s finding that Indian momentum lives in the liquid tercile only; balances impact cost against crowding |

**Turnover and cost at the statutory table.** Frozen caps: aggressive ≤200%/yr one-way
(`sleeves.yaml momentum.book_roles.aggressive`); moderate ≤~40%/yr one-way (1/5 of the 200%
annual budget, Known Prior #10). Statutory-only illustration using `costs.yaml`'s cash-delivery
round-trip range (24–32bps, Tier B):

| Book | Turnover cap (one-way/yr) | Statutory-floor cost (turnover × round-trip bps) |
|---|---|---|
| Aggressive | 200% | ~48–64bps NAV/yr |
| Moderate | 40% | ~10–13bps NAV/yr |

This is a **floor**, not the full cost — impact cost (`I = Y·σ_daily·√(Q/ADV)`) adds materially
more in the aggressive book's ranks 500–750 (thinnest ADV bucket, `r501_750: ₹1–4cr`,
**PROVISIONAL** in `costs.yaml`, pending the live-ADV recomputation already scheduled at data-
catalog runsheet step 15). Two external data points bound this from outside: (i) Raju's
"Implementing a Systematic Long-only Momentum Strategy" (SSRN 3510433, 2020) finds a NIFTY100
top-decile, **monthly-rebalanced** portfolio realizing **~32.1%/month mean turnover** (≈385%/yr
annualized — far above either of our caps) yet still outperforming the NIFTY100 index by +10.70pp/
yr gross, and explicitly states the outperformance "survives real-world implementation" given
discount-broker costs — a data point that our much tighter caps leave real headroom, not proof our
own net-of-cost number will match; (ii) NSE's own Nifty200 Momentum 30 semi-annual mechanical
reconstitution generates an estimated 130–140%/yr turnover from reconstitution alone (dossier01
§2) — a caution against copying that fixed-N mechanic, not a benchmark to match.

---

## C.5 Index/TSMOM data (L4)

**Equity TRI.** Nifty 50/500 TRI — free via `niftyindices.com/reports/historical-data` and the
`Backpage.aspx/getTotalReturnIndexString` endpoint (per B1–B4); exact internal index-name string
required per pull (spaced-uppercase for broad-market, compact for strategy indices).

**Gold INR series — three candidate sources, one frozen primary.**

| Source | What it is | Free depth | Role here |
|---|---|---|---|
| FRED `GOLDPMGBD228NLBM` × RBI reference rate (G10) | USD LBMA PM fix (free back to 1968, republished by FRED) × USD/INR | Full depth, both legs | **Primary**, per the already-frozen `sleeves.yaml gold.series_hygiene` rule: "INR gold = USD gold + USDINR, decomposed always" |
| MCX gold futures | India's own gold futures, contract from MCX's 2003-11 inception | Historical-data pages confirmed reachable this pass (`mcxindia.com/market-data/historical-data`, `.../reports-on-historical-data`, year/month filter) | Cross-check only, and the natural futures-leg data for basis/roll cost modeling — **not** the primary spot series |
| IBJA (India Bullion and Jewellers Association) AM/PM rate | Domestic reference physical-gold rate | Live-rate portals (`ibjarates.com`, `ibja.co`) confirmed; **no confirmed bulk historical download found this pass** — **[VERIFY]** | Forward-collection only (start daily snapshots now); not a deep-history source unlike the other two |

**This is worth stating plainly, matching the credit-deep dossier's "do not reach for CMIE out of
habit" framing**: MCX and IBJA are the *obvious* India-specific gold sources, but the design's own
frozen convention already routes around both as primaries — do not rebuild the gold sleeve on MCX/
IBJA out of habit; they are cross-checks.

**The futures-roll data question.** Continuous-futures construction (roll-date rule + price-
adjustment method across the roll) has no universal standard and materially affects backtest
results depending on the choice — confirmed this pass as a genuinely open, non-trivial data-
engineering problem for both MCX gold and NSE index futures. **The simplification worth stating
explicitly**: TSMOM's own signal (trailing 1–12 month sign/return, L4) needs only a *continuous
spot/TRI series* — which already exists free with no roll problem — not a stitched continuous
futures series. A continuous-futures build is only strictly required for the **execution** leg
(basis, cost-of-carry, funding), where expiry-level (not continuous) bhavcopy rows suffice because
the position is rolled monthly by design already. This avoids a real construction project that
this signal does not actually need.

---

## C.6 Validation fixtures — the external benchmark

**The Agarwalla-Jacob-Varma / IIMA data library is downloadable free.** Location:
`faculty.iima.ac.in/iffm/Indian-Fama-French-Momentum/` (mirror `web.iima.ac.in/~iffm/Indian-Fama-
French-Momentum/`); maintained by Agarwalla, Jacob & Varma, sourced from CMIE Prowess DX. **Update
cadence: three releases per year** (March, September, December), per this pass's search finding.
The archive page (`.../archive.php`) lists dated release files (2021-03, 2021-09, 2022-03,
2022-09, 2022-12, 2023-03, 2023-12 confirmed this pass) — **[VERIFY] whether the 2024–2026
releases are current on the live site**: a companion methodology paper, **Rajan Raju, "September
2024 Update on the Data Library: Fama-French Factors, Momentum, and Low-Risk Factors for the
Indian Market"** (SSRN 5008269), confirms the library was still being actively revised (expanded
universe, updated size classification) as of Sept-2024, but whether the stated 3x/year cadence has
been kept through 2025–2026 is the first thing to confirm on the principal's machine, not an
assumption to carry forward. **Programmatic access candidate**: the `indiafactorlibrary` PyPI
package (Apache-2.0), a pandas-datareader-style wrapper exposing `.get_available_datasets()` and
keyed DataFrame access, described as an "Invespar Factor Library for Indian equities" — **[VERIFY]
whether this wraps the IIMA/AJV series specifically or a separate, similarly-constructed library**;
treat as an ingestion shortcut to confirm and cross-check, not as confirmed-identical to the
primary IIMA files, per the mirror-authorization decision's own authentication requirement.

**This is THE external benchmark for our constructed WML**, exactly as the task frames it — no
other free India momentum-factor series has this combination of academic provenance, published
magnitude (WML 21.9%/yr, 1994–2014, survivorship-corrected, liquidity-screened — already the base-
case anchor in `sleeves.yaml momentum.haircut`), and a maintained update cadence.

**Acceptable tracking error before ours is trusted.** No literature value exists for this specific
comparison — it is a construction-validation choice, proposed here, and flagged as such (not a
sourced fact): reconstruct our own long-short decile WML (§C.4's spec) over AJV's own sample
window and require (i) monthly-return correlation with AJV's published/archived series **≥0.85**
(perfect correlation is neither expected nor the bar — universe screen, rebalance timing, and
weighting scheme genuinely differ), and (ii) our reconstructed **raw** (pre-haircut) annualized
mean WML within roughly **65–100% of AJV's 21.9%/yr** — i.e., a raw reconstruction landing *below*
the already-haircut ~14–16%/yr planning number in `sleeves.yaml` would mean the haircut is double-
counting a construction gap, not measuring further genuine decay, and must be investigated before
being read as evidence for a deeper haircut. **[DESIGN CHOICE, not a literature-sourced
threshold — flagged explicitly as such.]** Given AJV's own currency is unconfirmed past 2023–2024,
use **Rajan Raju's independent, more recent papers** (`Shades of Momentum`, Dec-2008–Sept-2024
sample, SSRN 4977717; `Implementing a Systematic Long-only Momentum Strategy`, SSRN 3510433) as a
**second, modern-regime benchmark** — these cover exactly the post-2015 window dossier01 §3
already flagged as the critical decay-test period ("if the post-2015 India momentum premium has
fallen materially below the 1994–2014 average, raise the haircut toward 58%"), which AJV's own
public data may not yet reach.

---

## C.7 Vintage / point-in-time discipline

Two dates mandatory everywhere per `ingest/manifest.py`'s existing WORM rule (a hash-mismatch
under an existing manifest entry is a hard failure — refreshes land as new vintage-named files,
never an overwrite):

| Series | Revision-prone? | Two dates that must never be conflated | Store first-print or latest? |
|---|---|---|---|
| NSE/BSE bhavcopy (A1/A2/A4) | Not revision-prone once published, but **[VERIFY] whether NSE ever reissues a same-date file under an unchanged filename** — if so, `manifest.py`'s hash-hard-fail is exactly the designed safety net | `pull_date` vs the file's own trading-date stamp | Latest; the manifest catches silent reissues |
| Corporate actions (C4) | Not revision-prone, but **two-date by nature**: announcement date (board approval) vs. effective ex-/record-date | Never adjust prices as of the announcement date — only from the ex-date forward; the announcement-to-effective gap is itself a state variable (`special_situations`) | Latest, append-only event log |
| Index membership (B1–B4/D3) | Scheduled, not revision-prone | Announced (4-weeks-prior press release) vs. effective (last trading day March/Sept) | Apply new membership only from the effective date; the drift between the two dates is itself the `index_inclusion_exclusion` signal, not noise to be collapsed |
| Delisting/suspension | Event-based | Suspension date (>6m triggers compulsory-delisting candidacy) vs. delisting order date vs. **last-traded date** — three distinct dates | Truncate a name's tradeable-universe membership only at its actual last-traded date, never earlier or later |
| AJV/IIMA factor library (C.6) | **Methodology-revision-prone** (per the Sept-2024 "expanded universe and updated size classification" update) | Release-vintage (2021-03, 2021-09, …) vs. pull date | **Every release kept as its own vintage, never only-latest** — identical discipline to credit-deep's WEO/FSR rows, for the identical reason (a benchmark whose own methodology moved must be traceable to which vintage validated which build) |
| MCX gold, FRED gold/USDINR (C.5) | Prices not restated | T+0/T+1 | Latest — no PIT problem, matches credit-deep's own "market-price complements" row |

---

## C.8 Construction pipeline — ordered, script-followable

1. **Registry load.** Validate `config/ladder.yaml` and `config/sleeves.yaml` against `config/
   validator.py` (0 errors) before any pull.
2. **Pull raw bhavcopy.** NSE cash + F&O via the existing `ingest/pull_nse_bhavcopy.py`
   (URL-scheme-complete already); BSE cash bhavcopy into `data/raw/bse/` — **no existing ingest
   script; this is a gap this Part surfaces**. Manifest every file immediately
   (`python ingest/manifest.py data/`).
3. **Build the legacy↔UDiFF field crosswalk parser** (§C.1's table) so both eras normalize into
   one internal schema before any downstream step runs — **new code, not yet in `ingest/`**.
4. **Pull/scrape corporate actions** (NSE corporate-filings-actions + BSE corp-action pages) into
   `data/raw/{nse,bse}/corp_actions/` — **no existing ingest script; a second gap**. Build the
   derived adjustment-factor table (§C.2's formulas), keyed by ISIN + ex-date, append-only.
5. **Apply adjustment factors** to the normalized price series, producing an adjusted daily
   return panel per ISIN; **run the TRI cross-check** (§C.2) against B1–B4's TRI series before
   trusting the adjusted output for anything downstream.
6. **Build point-in-time universe membership** (§C.3): archive NSE Indices reconstitution press
   releases into a membership-as-of-date table for Nifty 500/Total Market/Microcap 250; cross-
   reference delisting/suspension lists to truncate names correctly; tag the pre-launch Total
   Market/Microcap segment as back-computed, not PIT.
7. **Apply universe filters** (§C.4): ADV-percentile liquidity floor (reusing `costs.yaml`'s
   rank-bucket convention), ASM/GSM/circuit/ban-list exclusions, SME-series exclusion.
8. **Compute the momentum composite**: 12-1 and 6-1 total return plus 52-week-high proximity on
   the adjusted series, rank-blended per `sleeves.yaml momentum.construct`, skip-month applied,
   monthly per the aggressive-book default.
9. **Form deciles/terciles per book**, liquidity-tilted equal-weight default, hysteresis no-trade
   band; compute realized one-way turnover and compare against the frozen caps (200%/40%/
   quarterly-composite for aggressive/moderate/conservative).
10. **Apply the crash guard** (Barroso-Santa-Clara inverse-vol scaling + Daniel-Moskowitz
    bear-state cut, already specified in `sleeves.yaml momentum.crash_guard`) using the momentum
    spread's own trailing realized vol.
11. **Validate against AJV/IIMA** (§C.6): reconstruct the long-short decile factor over AJV's own
    sample window; compute correlation and mean-divergence against the published/archived AJV
    series; cross-check against Raju's independent modern-regime papers; log any divergence —
    never silently adopt an external number in place of a divergence finding.
12. **Compute the TSMOM leg** (L4): 1–12 month trailing sign/return on Nifty TRI/spot (not a
    stitched futures series, §C.5) and on the FRED-USD-gold × RBI-USDINR constructed INR gold
    series (not MCX/IBJA primary); feed the regime matrix only, never the equity-cross-section
    optimizer (respects the mandate's Stage-3 boundary).
13. **Manifest every derived fixture** (adjustment-factor table, membership table, momentum
    composite panel) as its own versioned, checksummed artifact; corrections append a new vintage
    row, never overwrite.
14. **Recalibration triggers.** Re-run whenever: (a) a new AJV/IIMA release lands — compare, log
    divergence; (b) a semi-annual index-reconstitution effective date passes; (c) book AUM moves
    ±50% (re-check the ADV floor/capacity per `costs.yaml`'s own recalibration trigger); (d) the
    data-phase purged-CV decile/tercile/weighting sweep (§C.4) completes and locks a construction
    choice — never re-tuned informally afterward, per contract §9.

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` §2 blocks A/B/C4 (access
paths, priorities, fixture governance), `research/dossiers/01-momentum-reversal.md` (the theory/
evidence/decay this part builds data for), `config/ladder.yaml` L3/L4, `config/sleeves.yaml
momentum`, `config/costs.yaml` (statutory rates, ADV rank buckets), `ingest/README.md` +
`ingest/manifest.py` (the WORM/manifest rule), `ingest/pull_nse_bhavcopy.py` (existing, URL-scheme-
complete, schema-crosswalk-incomplete), `research/OPEN_QUESTIONS.md` (Q1 benchmark decision;
2026-09-01 mirror-authorization note), `research/CONTRACT.md` §3 (free-source mandate), §6 (no
magic numbers), §9 (estimation standards).*


---

# PART D/E/F/H — Mathematics, algorithm, harvest map, knowledge ledger

# Part D — The mathematics (momentum-specific; shared machinery referenced, not repeated)

The general econometric toolkit (Hamilton filter, AR(1) bias, AUROC=Mann-Whitney, Stambaugh,
empirical Bayes, purged CV, deflated Sharpe, block bootstrap) is documented in the credit
monograph's Part D and applies verbatim. Below is only what is momentum-specific.

## D1. The WML object and its statistics

Formation: at month-end t, rank stocks by r(t−12→t−1) (the skip month removes short-term
reversal contamination — JT's own refinement). WML_t+1 = mean return of the top decile − bottom
decile over month t+1. Two facts drive everything downstream:
- **The premium is a spread of two noisy portfolios**: Var(WML) = Var(W) + Var(L) − 2Cov(W,L);
  in panics Cov collapses (legs decouple) — variance spikes exactly when the mean turns negative.
- **Skewness is structural, not incidental**: the loser leg after a bear market is a portfolio of
  distressed, high-beta names — an embedded short put on the market's rebound. Our M3 table IS
  this statement in numbers: bear-and-market-up months average −4.59%/m (US, 97y).

## D2. The Daniel-Moskowitz conditional beta, formally

DM's regression: WML_t = α + (β₀ + β_B·I_Bear,t + β_BU·I_Bear,t·I_Up,t)·Mkt_t + ε_t, where
I_Bear = 1 if trailing 24m market return < 0 (known at month start), I_Up = 1 if the
contemporaneous market return is positive. Published finding (and our M2/M3 replication in
conditional-mean form): β_BU > 0 and large — in bear states the WML acquires NEGATIVE market beta
that bites specifically when the market rallies. The guard's design follows: condition on
(bear, high vol) which are ex-ante, never on I_Up which is ex-post; the guard therefore accepts
sitting out some bear-and-down months (which are WML's BEST: +6.85%/m US) as the premium paid
for skipping the crash zone. That trade-off is the F-design's cost-benefit object, not a free lunch.

## D3. Vol-managed momentum (Barroso-Santa-Clara), and why it works here when vol-timing
the MARKET is contested

Scaling: WML*_t = (σ_target / σ̂_t) · WML_t, σ̂ from trailing 6m daily WML returns, capped.
BSC's insight: WML risk is highly forecastable (its vol is more persistent than the market's)
AND its risk-return relation is inverted in panic states — so de-scaling on own-vol removes
mostly bad states. Contrast Cederburg's critique of vol-managing the MARKET (fragile alpha):
the momentum version survives their protocol far better because the crash states are precisely
the high-vol states. Our M5: Sharpe 0.77→1.29, maxDD 83%→29% on the replication panel —
direction confirmed; India version pre-registered for the primary factor pull.

## D4. Breadth and the fundamental law, applied to L3

IR ≈ IC·√BR·TC. The 750-name cross-section rebalanced monthly is where the book's breadth
actually lives (BR ≈ number of independent bets/year — hundreds, vs the ladder's handful).
Consequences: (i) small ICs suffice (IC 0.03 at BR 500, TC 0.5 → IR ≈ 0.34 from this sleeve
alone); (ii) TC (transfer coefficient) is the fragile term at Conservative-book AUM — the
admission matrix and netting exist to protect it; (iii) the decay haircut applies to IC, and
IC is measurable monthly (uniqueness-weighted realized IC in the sentinel's attribution pack).

## D5. Decay estimation without self-deception

The decay object is the post-publication/post-crowding IC path, not the headline mean. Standing
haircut: 25–35% off the literature IC, escalating to 58% if the post-2015 India subsample is
weak (registry L3 decay clause). M1's real-data read: post-2015 India mean UNdecayed but vol
halved (Sharpe up) — no escalation triggered, no relaxation either: the forward haircut prices
FUTURE crowding (AMFI factor-fund AUM growth is the crowding monitor's input), not realized
history. The 21.9%-vs-13.1% level discrepancy is a construction question [VERIFY], not a decay
question — flagged in the ledger and awaiting the primary library pull.

# Part E — The algorithm (L3 + L4 + guard), end to end

```
STEP 0  registry load; universe file (PIT NIFTY-750 membership, ban list, liquidity floor)
STEP 1  adjusted price panel from bhavcopy + CA factors (Part C pipeline steps 1-9);
        TRI cross-check within tolerance before any signal is computed
STEP 2  L3 score: momentum_composite(prices) = equal-rank blend of 12-1, 6-1, 52wk-high
        (weights fixed per D11 anti-optimization rule; blend swept only on pooled data)
STEP 3  sector-relative option: within-sector ranks where the registry flag is on (pre-reg
        choice per sleeve); output Signal objects (score, half-life class, capacity per book)
STEP 4  L4 state: tsmom_state(index) per index/gold with lookback grid {6,9,12}m; feeds the
        trend_tsmom block (0.20) as regime confirmation + hedge scheduling, never a lone trade
STEP 5  crash_guard(market): bear (24m cum<0) AND expanding vol top quartile => guard ON:
        WML-sleeve sizing multiplier steps DOWN its grid (reduce-only); re-entry per the
        per-sleeve re-entry family (Batch-2 Q8), phase-D conditioning only after H66/F7 pass
STEP 6  costs: expected round-trip per name (statutory + sqrt-impact) netted from alpha BEFORE
        ranking into construct/ (cost-netted alpha rule)
MONITOR monthly realized IC (uniqueness-weighted) -> decay ledger; crowding monitor (AMFI
        factor AUM, comomentum when buildable) -> throttle; cert: live-vs-backtest IC floor,
        crowding ceiling, crash-guard override never (guard is structural)
FAILURE MODES: CA-adjustment error (tripwire: TRI tracking-error breach -> signal freeze for
        affected names); index-membership vintage gap (freeze additions until resolved);
        ban-list names (never initiate; exits via futures where available)
```

# Part F — The harvest map (what momentum/trend feeds)

| # | Consumer | What it gets | Status |
|---|---|---|---|
| F-a | Return engine sleeve (L3) | the composite rank -> cost-netted alpha -> construct/ | live design |
| F-b | Regime confirmation (L4) | TSMOM state into trend_tsmom block (0.20 budget) | live design |
| F-c | Hedge scheduling | L4 negative state accelerates hedge-grid steps within policy | live design |
| F-d | Crash guard | reduce-only WML sizing multiplier in panic states (M4-validated) | live design |
| F-e | Phase/D re-entry | quadrant-conditioned re-entry for the sleeve | gated on H66/F7 |
| F-f | Crowding monitor | AMFI factor-fund flows/AUM + (later) comomentum | v2 pipeline seat |
| F-g | Stage-2 briefing | sleeve state + guard status on the daily page | live design |

New pre-registered designs opened by this deep-dive: **N1** India DM-regression (the D2 spec with
Stambaugh-robust errors) on the PRIMARY factor library once pulled; **N2** vol-managed India WML
(M5 protocol); **N3** 21.9-vs-13.1 reconciliation (construction audit vs AJV paper); **N4**
52wk-high vs 12-1 redundancy/complement split (Raju SSRN citations from Part C as priors); **N5**
crash-guard threshold grid (dd, vol-pctile) swept on pooled US+India with the false-fire ledger.

# Part H — Knowledge ledger (momentum/trend)

**Established (Tier A/pooled):** the premium exists everywhere measured for a century+ (JT, AMP,
Geczy-Samonov); crashes are conditional and forecastable-in-state (DM; our M2/M3 on both panels);
vol management compresses the crash tail (BSC; our M5); the mechanism is behavioral + limits-to-
arbitrage, so decay is real but bounded away from instant (McLean-Pontiff).
**Established about OUR machinery (planted truth + real data):** composite recovers planted
momentum; the guard separates bad months on synthetic AND 97 years of US reality AND the India
mirror; no-look-ahead proven by truncation.
**Pooled-prior, awaiting India primary [A]:** exact India IC/half-life; the DM beta magnitudes;
vol-managed India parameters; the 21.9% reconciliation.
**Unknowable:** the next crash's date (only its STATE is knowable); whether AI-age crowding
shortens the cycle further — the crowding monitor watches, the haircut prices, the cert kills.
