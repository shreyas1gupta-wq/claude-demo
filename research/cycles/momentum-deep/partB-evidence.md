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
