# Dossier 01 — Momentum and Short-Term Reversal (India)

Workstream owner: research analyst · Phase: research-only, no data/code/backtests.
Complies with `research/CONTRACT.md` v0.1 and assumes all `OPEN_QUESTIONS.md` defaults
(notably Q1 Nifty 500 TRI signal benchmark / Nifty 50 TRI drawdown constraint, Q2
hedge-only shorting, Q5 flash-crash exclusion, Q6 moderate book as anchor).

---

## 1. Findings and literature

1. **Jegadeesh & Titman (1993)**, *Returns to Buying Winners and Selling Losers*, J. Finance
   48(1):65–91. Buying winners/selling losers on 3–12m formation, 3–12m holding earns
   ~1% per month (up to ~1.5% for the strongest formation/holding combinations) not
   explained by systematic risk or delayed reaction to common factors; roughly a third
   of year-1 abnormal return reverses over the following two years. Verified.
2. **Jegadeesh & Titman (2001)**, *Profitability of Momentum Strategies: An Evaluation of
   Alternative Explanations*, J. Finance 56:699–720. Confirms momentum persisted
   out-of-sample through the 1990s (not a data-snooped 1993 result); finds no reversal at
   2–3 years post-formation but significant reversal at 4–5 years — supporting the
   behavioral/delayed-overreaction story over a risk-based one, and warning against
   holding a momentum book "buy and forget" past its holding window. Verified.
3. **Novy-Marx (2012)**, *Is Momentum Really Momentum?*, J. Financial Economics 103:429–453.
   Momentum profit is concentrated in returns from month t-12 to t-7 ("intermediate
   horizon"); the recent-past t-6 to t-2 window contributes much less and is noisier. This
   directly reframes "12-2" momentum: most of its power is really "12-7," and a pure "6-2"
   or "3-1" signal is a materially weaker, more reversal-contaminated construct. Verified.
4. **George & Hwang (2004)**, *The 52-Week High and Momentum Investing*, J. Finance
   59:2145–2176. Nearness to the 52-week high dominates and subsumes past-return
   momentum's forecasting power; critically, 52-week-high-based return forecasts do
   **not** reverse in the long run, whereas plain past-return momentum does — implying
   the two are related but distinct phenomena with different crash risk. Verified.
5. **Griffin, Ji & Martin (2003)**, *Momentum Investing and Business Cycle Risk: Evidence
   from Pole to Pole*, J. Finance 58:2515–2547. Across 40 countries, momentum profits are
   large in both good and bad macro states and only weakly co-move across countries;
   neither unconditional nor conditional macro-risk models explain momentum; profits
   reverse over 1–5 year horizons — inconsistent with momentum being a single global
   risk-factor investors are compensated to bear. Verified.
6. **Chui, Titman & Wei (2010)**, *Individualism and Momentum around the World*, J. Finance
   65:361–392. Momentum magnitude is strongly and positively associated with a
   country's Hofstede individualism score (overconfidence/self-attribution-bias proxy),
   and with transaction costs and dispersion of analyst forecasts; East Asian
   (low-individualism) markets show materially weaker momentum. India is a
   middling-individualism, high-promoter-concentration market — this cross-country
   regularity is a soft prior that India's momentum premium sits below the
   US/UK/Australia level and above Japan/Korea, consistent with the India-specific
   magnitudes found below. Verified.
7. **Moskowitz, Ooi & Pedersen (2012)**, *Time Series Momentum*, J. Financial Economics
   104:228–250. Across 58 liquid futures instruments (equity index, currency, commodity,
   bond) 1965–2009, own-asset trailing 1–12 month return positively predicts the next
   month's return, partially reversing beyond ~12 months; a diversified TSMOM portfolio
   has low loading on standard factors and performs best in extreme markets (crashes
   *and* rallies) — the opposite crash profile to cross-sectional equity momentum.
   Verified.
8. **Daniel & Moskowitz (2016)**, *Momentum Crashes*, J. Financial Economics 122:221–247
   (NBER WP 20439, 2014). Momentum has strong average returns but occasional severe,
   persistent crashes (worst episodes: 1932, 1938–39, 1974–75, 2001–02, and 2009 — the
   2009 episode alone erased roughly two years of prior cumulative momentum profit in a
   few months). Crashes are partly forecastable: they cluster in "panic" states —
   following market declines, in high-volatility regimes — and are contemporaneous with
   market rebounds (momentum is short the very rally that ends the panic). A dynamic
   strategy forecasting each side's mean/variance and re-weighting accordingly
   roughly doubles the unconditional Sharpe ratio; robust across 8 markets/asset
   classes. Verified.
9. **Barroso & Santa-Clara (2015)**, *Momentum Has Its Moments*, J. Financial Economics
   116:111–120. Momentum's own risk (not market beta) is highly time-varying and
   forecastable from trailing realized volatility of the long-short spread itself; scaling
   exposure to target constant volatility (their illustration: 12% annualized) raises the
   Sharpe ratio from ~0.53 (unmanaged) to ~0.97 (managed) and "virtually eliminates"
   crashes, because high realized vol forecasts *both* higher risk and lower forward
   return. Verified.
10. **McLean & Pontiff (2016)**, *Does Academic Research Destroy Stock Return
    Predictability?*, J. Finance 71:5–32. Across 97 documented return predictors,
    portfolio returns fall ~26% out-of-sample (upper bound for pure data-mining) and a
    further ~58% post-publication (informed trading effect ≈32pp of the 58); declines
    are larger for higher in-sample returns and for predictors concentrated in
    high-idiosyncratic-risk, low-liquidity names. Verified (already in CONTRACT.md
    §5, re-verified here).
11. **Jacobs & Müller (2020)**, *Anomalies Across the Globe: Once Public, No Longer
    Existent?*, J. Financial Economics 135:213–230. Across 241 anomalies in 39 stock
    markets (>2 million anomaly-country-months), **the US is the only country with a
    reliable post-publication decline in long-short anomaly returns**; internationally,
    anomalies (momentum included) persist largely undiminished post-publication.
    Momentum specifically remains stronger in up-markets and low-volatility regimes
    internationally, mirroring the US pattern. This is the single most important
    "decay" fact for this workstream: it directly answers the contract's framing
    question, and argues the India momentum premium should **not** be given the full
    McLean-Pontiff 58% haircut by default — see §3. Verified.
12. **Agarwalla, Jacob & Varma (2013, updated periodically)**, *Four Factor Model in
    Indian Equities Market*, IIM Ahmedabad WP, and the associated IIM-A Fama-French-
    Momentum data library. Jan 1994–Dec 2014: momentum factor (WML) average **21.9%/yr**
    vs HML 15.3%/yr, SMB ~0%, market risk premium 11.5%/yr, on a survivorship-corrected,
    liquidity-screened CMIE Prowess universe. This is the closest thing India has to an
    AQR-style factor library and is the base-case magnitude reference for this dossier.
    Verified.
13. **Sehgal & Balakrishnan (2002)**, *Contrarian and Momentum Strategies in the Indian
    Capital Market*, Vikalpa 27:13–19 (364 firms, Jul 1989–Mar 1999). Short-horizon
    continuation (momentum) is significant and positive; once a ~1-year gap separates
    formation from holding, **long-run reversal appears within about a year of the
    ranking period** — i.e., India's long-horizon reversal cycle looks shorter than the
    3–5 year US pattern documented by Jegadeesh-Titman (2001) and De Bondt-Thaler. Small,
    early sample; confidence capped accordingly. Verified.
14. **Sehgal & Balakrishnan / Sehgal & Ilango, Momentum Profits, Portfolio Characteristics
    and Asset Pricing Models** (SSRN 1374790). Momentum returns unexplained by CAPM are
    partially (not fully) absorbed by the Fama-French three-factor model in India,
    leaving an open question — as in the US — whether the residual is under-reaction or
    a missing risk factor. Verified (SSRN working paper; exact journal outlet not
    independently confirmed — [VERIFY: final publication venue]).
15. **Sharma, Subramaniam & Sehgal (2021)**, *Are Prominent Equity Market Anomalies in
    India Fading Away?*, Global Business Review 22(1):255–270 (NSE 500, Jul 2005–Jun
    2016, CAPM + FF3 benchmarks). Value and momentum anomalies are **increasingly
    explained by risk-factor models** in this later sample (i.e., much of the raw
    momentum spread loads on other systematic factors rather than standing as
    orthogonal alpha), while size and volume anomalies persist but have faded. This is
    India's own version of a decay signal — softer than McLean-Pontiff (it is
    risk-model absorption, not an outright post-publication return decline), but it is
    real and must inform sizing (do not double-count a momentum sleeve against a
    value/quality sleeve — see §4). Verified.
16. **Chui, Ranganathan, Rohit & Veeraraghavan (2023)**, *Momentum, Reversals and
    Liquidity: Indian Evidence*, Pacific-Basin Finance Journal 82:102193 (3,956 BSE
    stocks, 2000–2021). Significant intermediate- and long-term price momentum on the
    BSE; **momentum is stronger and more persistent (up to 12 months) in the most
    liquid tercile**, while the **most illiquid tercile shows short- and
    intermediate-term reversal instead of continuation**. This is a direct, modern,
    India-specific liquidity/momentum interaction result and is treated as the primary
    academic anchor for the capacity discussion in §3–§4. Verified.
17. **Maheshwari & Dhankar (2017a)**, *The Effect of Global Crises on Momentum
    Profitability: Evidence from the Indian Stock Market*, Vision 21(1). Momentum
    returns are strongly positive pre-crisis, **turn negative during the 2008 crisis**,
    and rebound to high positive values post-crisis — an India-specific replication of
    the Daniel-Moskowitz crash pattern (crash-in-panic, rebound-with-market). Verified.
18. **Maheshwari & Dhankar (2017b)**, *Profitability of Volume-Based Momentum and
    Contrarian Strategies in the Indian Stock Market*, Global Business Review 18(4):
    974–992. High-trading-volume stocks earn **higher** momentum *and* contrarian
    returns than low-volume stocks — volume predicts both magnitude and persistence,
    consistent with Lee & Swaminathan (2000)'s US finding. Verified.
19. **Singh, Walia, Panda & Gupta (2022)**, *Risk-Managed Momentum: An Evidence from
    Indian Stock Market*, FIIB Business Review 11(3):347–358 (450 BSE stocks). A
    Barroso–Santa-Clara-style volatility-scaled momentum overlay **doubles the
    risk-adjusted (Sharpe-type) ratio** and materially improves downside risk/negative
    skew versus raw relative momentum in India. Non-elite journal, small sample of
    studies (n≈1-2 India replications) — Tier B, but directionally consistent with the
    much larger US/global evidence base. Verified.
20. **(Author names as published) (2022)**, *Risk-Managed Time-Series Momentum: An
    Emerging Economy Experience*, J. Economics, Finance and Administrative Science
    (Emerald) 27(54):328-. A revised, risk-managed TSMOM applied to the Indian equity
    market delivers **~2.5x the return** of standard TSMOM with materially better
    downside/higher-moment risk. One of the only two India-specific TSMOM papers found.
    Verified via publisher listing; [VERIFY: exact author byline — search results
    returned title/journal/findings but not a clean author string].
21. **NSE research working paper**, *Does the Stock Market Overreact? Empirical Evidence
    of Contrarian Returns from Indian Markets* (NSE archives, monthly data 1995–2008).
    Documents overreaction-led short-run momentum followed by long-run contrarian
    (reversal) profits, consistent with De Bondt-Thaler and Jegadeesh-Titman; a primary,
    exchange-hosted Indian source. Verified (nsearchives.nseindia.com/content/research/
    res_paperfinal223.pdf).
22. **Cheng, Hameed, Subrahmanyam & Titman (2017)**, *Short-Term Reversals: The Effects
    of Institutional Exits and Past Returns*, J. Financial and Quantitative Analysis
    52:143–173. The leading explanation for short-term reversal is compensation for
    liquidity provision; reversal profits rise when institutional ownership/competition
    for liquidity-provision falls — i.e., reversal is a genuine microstructure risk
    premium (survival argument iii) concentrated where liquidity providers are scarce.
    Verified.
23. **Korajczyk & Sadka (2004)**, *Are Momentum Profits Robust to Trading Costs?*,
    J. Finance 59:1039–1082, responding to **Lesmond, Schill & Zhou (2004)**, *The
    Illusory Nature of Momentum Profits*, J. Financial Economics 71:349–380. Lesmond et
    al. show naive momentum needs to trade disproportionately in the highest-cost names
    and can be wiped out by realistic costs; Korajczyk-Sadka show liquidity-weighted
    construction pushes break-even fund size to **≈$5bn+** (Dec-1999 US market cap
    terms) before the effect vanishes. Verified.
24. **Frazzini, Israel & Moskowitz (2012/2018 rev.)**, *Trading Costs of Asset Pricing
    Anomalies*, using ~$1tn of live institutional trading data, 1998–2011, 19 developed
    markets. Real-world costs are "less than a tenth" of prior academic estimates;
    value and momentum are highly scalable; **short-term reversal is the single most
    trading-cost-constrained anomaly** of the group. This is the single best
    "capacity" data point available for this workstream, and it is a developed-market,
    institutional-execution result — India's higher STT and thinner liquidity make its
    conclusion on reversal a ceiling, not a floor, for India. Verified.

---

## 2. India-specific evidence

- **Magnitude anchor**: Agarwalla-Jacob-Varma momentum factor ≈21.9%/yr average
  (1994–2014, long-short, survivorship-corrected, liquidity-screened). This is the
  single best Tier-B India number for a 12-month-family cross-sectional momentum
  factor and should anchor any "does it survive costs" arithmetic in the data phase.
- **Live product evidence**: NSE's own Nifty200 Momentum 30 and Nifty Midcap150
  Momentum 50 indices use a **6-month + 12-month blended, volatility-adjusted momentum
  score with no skip-month**, semi-annual reconstitution (June/December), stock weight
  = free-float market cap × normalized momentum score, capped at 5% or 5× float weight.
  Both indices exclude stocks that hit circuit limits ≥20% of trading days in the prior
  6 months and non-F&O names — a built-in liquidity/surveillance filter worth copying.
  [Primary source: niftyindices.com factsheets/whitepapers — could not be fetched
  directly in this sandbox (egress-blocked); content corroborated via multiple
  secondary citations (fund factsheets, index-change press coverage) and treated as
  reliable given full agreement across independent sources.]
- **Live-vs-backtest gap (the contract's explicit question)**: an independent 18-year
  backtest (Dec 2006–Jun 2025, BacktestIndia Research — a practitioner blog, **not
  peer-reviewed, Tier C source, cited only for its directional/crash-timing content**)
  finds the Nifty200 Momentum 30-style strategy: 14.0% net CAGR vs Nifty 50's 10.4%
  (+3.6pp/yr), but a **max drawdown of ‑70.5% from Oct-2007 to Dec-2008 with a 65-month
  (5.4-year) recovery** — a full crash-and-recovery cycle that **no live fund factsheet
  can show**, since these products only launched ~2021–2024. This is exactly the "live
  vs backtest gap" the workstream brief asks about: the backtest contains the 2008
  momentum crash the live track record has never faced. Live 5-year/10-year headline
  numbers (as of Nov-2024: 29.7%/5y, 23.3%/10y) are real but drawn from a benign
  2020–2024 upcycle window, not a stress window.
- **Reconstitution mechanics as a cost, and as a crowding signal**: the June-2025
  Nifty200 Momentum 30 semi-annual rebalance alone generated an estimated **68.4%
  one-way turnover** and ≈₹16,000cr (~US$1.9bn) of round-trip trade (Business
  Standard, Smartkarma/Brian Freitas index-flow estimates) — i.e., roughly 130–140%
  one-way turnover per year from reconstitution alone, before any weight-cap drift
  trading. That is already 65–70% of the **moderate book's entire 200% annual
  turnover cap** if replicated mechanically — a strong argument against mimicking
  NSE's semi-annual, fixed-30-name reconstitution mechanic (see §4 rebalance-cadence
  proposal). It is also a crowding signal: smart-beta/factor index AUM in India grew
  from ~₹290cr (2020) to **~₹46,000cr (end-2025)**, ~12% of passive equity AUM,
  concentrated in a small number of mechanically-reconstituted 30–50 name baskets.
  Individual product AUM figures scraped for this dossier were inconsistent/noisy
  (single funds reporting implausible multi-lakh-crore AUM alongside plausible
  ₹400–8,500cr figures for sibling share classes) — **[VERIFY: exact combined
  momentum-factor AUM in India]** — but the ₹46,000cr smart-beta total and the
  ₹16,000cr single-rebalance trade size are corroborated by independent press sources
  and are usable as an order-of-magnitude capacity ceiling.
- **Liquidity/turnover bifurcation**: two independent constructs point the same
  direction but are not identical. (a) Chui et al. (2023, academic, BSE 2000–2021):
  momentum lives in the **liquid** tercile; the **illiquid** tercile reverses instead
  of continuing. (b) BacktestIndia (practitioner, Tier C): stocks with high "scaled
  turnover" (a speculative-churn proxy, not simple liquidity) underperform — CAGR gap
  of ~10.9pp between low- and high-scaled-turnover momentum baskets, and adding a
  scaled-turnover "anti-speculation" filter to a momentum sleeve raised CAGR from
  14.0%→18.0% while cutting max drawdown by ~13 points. These are complementary, not
  contradictory: prefer momentum in float-liquid names generally (Chui et al.), and
  treat abnormal speculative-turnover spikes as a **risk-reduction-only filter**
  (consistent with the contract's Tier-C-reduce-only rule, since the filter's source
  is Tier C).
- **Institutional microstructure specific to India, relevant to signal design**:
  - **STT**: delivery equity 0.1% each leg (buy + sell) = 20bps round-trip tax alone,
    with no US analogue — this is the central reason short-horizon reversal is harder
    to run in India than in the Frazzini-Israel-Moskowitz US sample.
  - **ASM/GSM surveillance**: stocks under Additional/Graded Surveillance Measure face
    higher margins, delivery-only settlement, and tighter bands specifically to choke
    off momentum-chasing flow — i.e., regulation directly targets the crowding
    mechanism our signal would otherwise exploit in the most speculative names; ASM/GSM
    list reviews are now monthly (was quarterly), tightening the net faster than
    before.
  - **MWPL/F&O ban**: a stock enters F&O ban at 95% of market-wide position limit
    (MWPL = lesser of 15% free float or 65× average daily delivery value, Delta-based
    FutEq OI methodology from Oct-2025); ban blocks new derivative positions only,
    never cash equity — so a cash-equity momentum/reversal sleeve is unaffected, but
    any single-stock options overlay (out of scope per OPEN_QUESTIONS Q4 default) would
    be.
  - **Circuit price bands**: momentum's most attractive candidates (biggest recent
    movers) are mechanically the ones most likely to be trading at or near a circuit
    band, which both the Nifty momentum indices and any prudent proprietary
    methodology should exclude (NSE's own ≥20%-of-days-at-circuit exclusion rule is
    the right template).
  - **Index-reconstitution price effect**: Indian studies of Nifty inclusion/exclusion
    (Selvam, Indhumathi & Lydia 2012 and others) find abnormal inclusion gains fade
    within ~60 days and exclusion losses fade within ~10 days — a short-lived,
    price-pressure-driven (not permanent, not pure-liquidity) effect. Relevant because
    our own book should avoid mistaking a reconstitution-driven price pop in a
    to-be-included stock for genuine momentum, and can treat known reconstitution
    dates (semi-annual, publicly scheduled) as a state variable to avoid trading into.
  - **SAST 5% disclosure**: relevant only at the top of the aggressive book's
    concentration range in small/micro names; a 5–6% single-name entry cap (mandate
    §3) already sits below the SAST trigger for most cases, but staged-entry
    aggregation (≤20% mandate cap) should be checked against SAST in the data phase
    for any name approached from multiple sleeves simultaneously.

---

## 3. Decay and crowding assessment

For each candidate, the required "why does this survive being known" argument, then a
haircut.

**12-1 / 12-7 intermediate momentum (cross-sectional, equities).**
Survival argument: **(i) structural/behavioural** — gradual diffusion of information
under limited investor attention (Jacobs-Müller's own stated mechanism for
international momentum), reinforced by India's thinner analyst coverage outside the
Nifty200 and continued high promoter/insider ownership that mechanically caps free
float and slows price discovery. Decay: Jacobs & Müller (2020) find the **US is the
only market with reliable post-publication decline** across 39 countries — this is
direct evidence against reflexively applying McLean-Pontiff's 58% US post-publication
haircut to India. However, Sharma-Subramaniam-Sehgal (2021) show India momentum
becoming increasingly **risk-model-explained** over 2005–2016 — a softer, real form of
decay (crowding into a style tilt rather than an outright return decline). Net
haircut recommendation: **25–35% off the raw Agarwalla-Jacob-Varma 21.9%/yr**, i.e.
treat ~14–16%/yr gross long-short as the planning number pre-cost — closer to
McLean-Pontiff's 26% out-of-sample (data-mining) haircut than their 58%
post-publication figure, since Jacobs-Müller says the *post-publication* leg is
largely a US phenomenon. This is a judgment call with an explicit, falsifiable
trigger: **if the data-phase point-in-time backtest shows the India momentum premium
has fallen materially below the 1994–2014 IIM-A average in the post-2015 sub-sample,
raise the haircut toward the full 58%.**

**6-1 momentum.** Same mechanism, weaker evidence (Novy-Marx: recent 6-2-style
windows are dominated by the 12-7 component). Treat as a blend ingredient, not an
independent return source; no separate haircut beyond the 12-1 haircut, but do not
size it as if it were additive.

**3-1 momentum (as a standalone signal).** No independent survival argument beyond
what 12-1/6-1 already capture, and it overlaps the reversal zone documented by
Jegadeesh (1990)/Lehmann (1990). **Reject as a standalone sub-signal** — this is the
contract's "no magic numbers, no signal without a survival argument" rule applied
directly. Fold any 2–3 month information into the composite rank only as a tie-break,
never as a distinct return source.

**1-month cross-sectional reversal.** Survival argument: **(iii) genuine risk
premium** — Cheng-Hameed-Subrahmanyam-Titman (2017) show reversal is compensation for
liquidity provision, rising when institutional competition for that role falls; India's
mid/microcap tail plausibly has fewer systematic liquidity providers than US
large-cap, which argues *for* persistence there. But Frazzini-Israel-Moskowitz find
reversal is **the most cost-constrained anomaly even in the cheapest, most
institutionally-executed market (the US)** — and India adds a 20bp round-trip STT tax
that has no US analogue, on top of higher impact cost in exactly the small/illiquid
names where the premium is theoretically largest. **No dedicated modern India study
of 1-month cross-sectional reversal magnitude was found in this search** (existing
India reversal evidence — Sehgal-Balakrishnan 2002, the NSE overreaction paper — is
about 12–36 month reversal, not 1-month); this is a genuine evidence gap, tagged
**[VERIFY: no India-specific 1-month cross-sectional reversal magnitude/cost study
found]**. Per contract §4 tier rules, an effect with <4 independent India
observations and no clean magnitude estimate is Tier C: **it may be used to reduce
risk (e.g., as a contrarian sanity flag) but must carry zero return budget** until the
data phase produces a point-in-time, cost-inclusive Indian estimate.

**52-week high.** Survival argument: **(i) behavioural**, anchoring/reference-price
bias (George-Hwang 2004) — a harder-to-arbitrage bias than plain extrapolation because
it requires overriding a salient, easily-observed anchor. George-Hwang's own finding
that 52-week-high forecasts do **not** reverse long-run argues for a *smaller* haircut
than plain momentum (less of its return is a temporary overreaction subject to
give-back). No India-specific study found — **[VERIFY: India 52-week-high momentum
magnitude]** — treat as Tier B cross-country prior only, parameters frozen at
inception per contract §4.

**Griffin-Ji-Martin's macro-risk-neutrality result and Chui-Titman-Wei's
individualism result** together argue momentum in India is better modeled as a
behavioural/institutional effect of moderate (not top-tier) strength than as a "risk
premium someone must be paid to bear" — this shapes confidence more than sizing.

**Time-series momentum (index/gold, asset sleeve).** Survival argument: **(ii)
capacity limit is actually irrelevant at our size** (TSMOM runs at hundreds of
billions of dollars globally in liquid futures) but **(iv) institutional constraint**
does the real work — most asset owners run benchmarked, buy-and-hold-biased mandates
and cannot systematically trend-follow; that structural non-participation is what
leaves the premium on the table for unconstrained capital. Two India-specific
academic papers (Copernican Journal paper; Emerald risk-managed TSMOM paper) find
TSMOM significant, non-reversing at 12 months, and improvable in risk terms via
volatility management, consistent with the much larger global evidence base. Haircut:
modest, **10–20% off the Moskowitz-Ooi-Pedersen global magnitude**, reflecting only
generic emerging-market/liquidity friction (India equity index futures and MCX/COMEX
gold futures are both reasonably liquid), not a specific decay finding.

**Momentum crashes as a risk-form question, not an edge.** Daniel-Moskowitz and
Barroso-Santa-Clara are Tier A globally (>30 independent crash/rebound and
volatility-regime observations across a century and 8 markets). India replications
(Singh-Walia-Panda-Gupta 2022; the Emerald TSMOM paper; Maheshwari-Dhankar 2017a's
2008-crisis finding) are Tier B (2–3 India-specific studies, non-elite journals) but
directionally unanimous with the global result and with each other. This is the
evidence base for the crash-guard rule in §4.

---

## 4. Proposed parameters

All forms below are quantile-rank / sign / vol-scaling constructs, not fixed numeric
thresholds, per contract §6.

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Primary lookback family | 12-month total return, **skip most recent 1 month** (12-1); blend with 6-month, skip 1 month (6-1) via rank-average, not raw-return-average | Jegadeesh-Titman (1993/2001); Novy-Marx (2012) intermediate-horizon result; Agarwalla-Jacob-Varma India factor construction | B (India magnitude); A (global mechanism) | Medium-high | 25–35% haircut off raw India factor return (see §3) | Post-2015 India sub-sample premium materially below 1994–2014 average in the data-phase point-in-time backtest |
| Rejected standalone signal | 3-1 (or any pure 2–4 month) momentum as an independent sleeve | Novy-Marx (2012); Jegadeesh (1990)/Lehmann (1990) reversal-zone overlap | — | High (as a rejection) | N/A — no independent survival argument | A dedicated India study showing 3-1 momentum is NOT explained by the 6-1/12-1 composite |
| 52-week-high overlay | Price ÷ trailing 52-week high, quantile rank, combined with the 12-1/6-1 composite rank (equal-weight rank blend, not a fixed cutoff) | George & Hwang (2004); international extensions (George-Hwang-Liu 2007-era) | B (cross-country prior; no India study found) | Medium | Smaller haircut than plain momentum — no long-run reversal in the George-Hwang evidence | An India-specific 52-week-high study, positive or negative |
| Composite construction | Equal-weight (or evidence-weighted) **rank blend**, not raw z-score or fixed-return-threshold sort | Contract §6 (no magic numbers); Novy-Marx (component weighting rationale) | B | Medium-high | n/a (form choice, not a return estimate) | Purged-CV evidence in the data phase that unequal component weights are robustly better |
| Rebalance cadence — aggressive book | Monthly re-rank, **trade only names crossing a rank-quantile boundary by more than a half-decile margin** (hysteresis/no-trade band expressed as a quantile margin, not a fixed % return) | Contract §10 (weekly–monthly preferred); Nifty200 Momentum 30 turnover evidence (§2) as a cautionary anchor against full periodic reconstitution | B | Medium | n/a | Purged-CV turnover-vs-decay tradeoff study in the data phase |
| Rebalance cadence — moderate book | Momentum computed monthly but **only acted on as a modifier/tiebreaker inside the value/quality factor book's slower (quarterly-ish) turn**, consistent with Known Prior #10 | Known Prior #10 (contract §7.10); turnover-budget arithmetic below | B | Medium | n/a | Evidence that momentum's independent Sharpe contribution justifies its own turnover budget inside the 200% cap |
| Rebalance cadence — conservative book | Momentum as one input to a slow multi-factor composite, **rebalanced no more than quarterly**, never a standalone sleeve | Known Prior #3 (cycles buy permission for concentration, not turnover); 100% turnover cap | B | Medium | n/a | n/a — structural, not evidence-contingent |
| Crash-guard rule (form) | Scale momentum-sleeve gross exposure by the **inverse of the trailing realized volatility of the momentum long-short spread itself** (Barroso-Santa-Clara form), with an **additional cut when the trailing market-return quantile is in its own worst historical bucket** (Daniel-Moskowitz bear-state indicator) — both defined relative to the signal's own history, never a fixed %DD trigger | Barroso & Santa-Clara (2015); Daniel & Moskowitz (2016); India replications (Singh-Walia-Panda-Gupta 2022; Emerald TSMOM 2022) | A (global mechanism), B (India replication) | High (form), medium (India magnitude) | n/a (risk-management form, already the "haircut" mechanism for the crash itself) | Data-phase purged-CV confirmation that vol-scaling on Indian momentum spreads reduces realized max-DD without giving back a disproportionate share of return |
| 1-month reversal signal | **Zero return budget**; usable only as a risk-reduction / contrarian sanity flag, restricted (if used at all) to the aggressive book's most liquid top-100–200 names | Cheng-Hameed-Subrahmanyam-Titman (2017) mechanism; Frazzini-Israel-Moskowitz (2018) cost ranking; **no India magnitude study found** — [VERIFY] | C | Low | Full reduce-only per contract §4 Tier-C rule until an India, cost-inclusive estimate exists | A point-in-time, cost-inclusive India 1-month reversal magnitude estimate in the data phase — only then reconsider a small return-generating role |
| Reversal capacity ceiling | Reversal dies as a **return-generating** sleeve above roughly the **low end of the moderate book (~₹1,000–1,500cr)** even before the Tier-C zero-budget rule is applied, on cost-stack grounds alone (STT 20bp round-trip + India impact cost in small/illiquid names, against Frazzini-Israel-Moskowitz's finding that reversal is the most cost-constrained anomaly even in the cheaper US market) | Derived from Frazzini-Israel-Moskowitz (2018) + STT structural fact + Korajczyk-Sadka (2004) momentum (not reversal) $5bn breakeven as an upper-bound comparator for a *less* cost-sensitive strategy | C (derived, not directly estimated) | Low | n/a | A data-phase impact-cost model calibrated to NSE bhavcopy volumes, replacing this qualitative ceiling with a number |
| TSMOM — equity index sleeve | 1–12 month trailing sign/return on Nifty (and Bank Nifty where beta-relevant) futures, as an input to the **regime matrix**, not the equity-cross-section optimizer (respects mandate §2 Stage 3 boundary) | Moskowitz-Ooi-Pedersen (2012); Copernican Journal India TSMOM paper; Emerald risk-managed TSMOM paper | B (India), A (global) | Medium-high | 10–20% haircut off global TSMOM magnitude for generic EM friction | An India-specific TSMOM magnitude/cost estimate from the data phase |
| TSMOM — gold sleeve | Same 1–12 month trailing-return construct applied to gold (ETF/futures, per mandate's gold-instrument constraint), feeding the gold-tilt decision within the ≤50% gold cap and the existing policy-portfolio asset mix (never overriding it, per Known Prior #5) | Moskowitz-Ooi-Pedersen (2012) — gold is one of the 58 instruments; no India-specific gold-TSMOM academic study found — [VERIFY] | B (global only; India application untested) | Medium | 10–20% haircut, same logic as index sleeve | An India/MCX-specific gold-TSMOM estimate |
| Momentum vs value/quality turnover split (moderate book) | Momentum sleeve capped at roughly **≤1/5 of the 200% annual turnover budget** (i.e., ≤~40% one-way/yr), leaving ≥160% for the slower value/quality core | Known Prior #10 (contract §7.10: value/quality half-life ~5× momentum's, so ~1/5 the turnover per unit of authority); Nifty200 Momentum 30 reconstitution-turnover evidence (§2) as the cautionary anchor | B (derived from a data-derived prior, re-argued here) | Medium | n/a | A data-phase half-life estimate for India momentum vs India value/quality that revises the 5× ratio |
| Momentum sleeve indicative capacity — aggressive book | Full NIFTY 750 breadth including ranks 500–750; book (₹100–250cr) is small relative to India's total smart-beta/momentum-tracking AUM (order ₹15,000–46,000cr across products, per §2), so price impact is a name-selection/execution problem, not a strategy-level capacity problem | §2 AUM evidence (order-of-magnitude, flagged [VERIFY] on exact split); Chui et al. (2023) liquid/illiquid bifurcation | B | Medium | n/a | n/a — mechanical relative-size argument |
| Momentum sleeve indicative capacity — moderate book | Restricted to ranks ~1–500; modifier role only (see turnover-split row above); book (₹1,000–2,500cr) starts to approach a non-trivial fraction of any single reconstitution-day liquidity pool in mid-cap names | §2 (₹16,000cr single Nifty200 Momentum 30 rebalance-day trade size as a liquidity-pool anchor) | C (derived, order-of-magnitude) | Low-medium | n/a | Data-phase impact-cost modeling against actual NSE bhavcopy ADV by rank bucket |
| Momentum sleeve indicative capacity — conservative book | Contributory input to a multi-factor composite only, never a standalone sleeve; book (₹10,000–25,000cr) is large enough that a naive momentum replication would itself become a meaningful fraction of the ~₹46,000cr India smart-beta pool | §2; Frazzini-Israel-Moskowitz (2018) capacity framework, applied qualitatively | C (derived, order-of-magnitude) | Low | n/a | Data-phase impact-cost modeling; also depends on the final policy-portfolio equity allocation to this book |
| Reconstitution-date avoidance | Do not initiate new momentum entries into names experiencing a live Nifty/BSE index-inclusion price pop; the effect fades in ~10–60 days (India-specific) and is better treated as a state variable to wait out than as momentum signal | Selvam, Indhumathi & Lydia (2012) and related India index-effect studies | B | Medium | n/a | n/a — structural/regulatory-calendar fact |

---

## 5. Evidence-tier recommendations

- **Cross-sectional 12-1/6-1 momentum, global mechanism**: **Tier A**. >30 country
  studies, >90 years of US data, decades of international replication (Jegadeesh-
  Titman, Griffin-Ji-Martin's 40-country panel, Jacobs-Müller's 39-country/241-anomaly
  panel). The behavioural mechanism (limited attention / gradual diffusion) is
  well-established as a persistent, largely non-US-decaying effect.
- **Cross-sectional 12-1/6-1 momentum, India magnitude specifically**: **Tier B**.
  Observation count: roughly 5 independent India academic studies spanning ~1989–2021
  with overlapping but not fully independent samples (Sehgal-Balakrishnan 2002;
  Agarwalla-Jacob-Varma 2013; Sharma-Subramaniam-Sehgal 2021; Nigam-Pandey 2023;
  Chui-Ranganathan et al. 2023); at the signal's own ~6–12 month decay-relevant
  half-life, the effective number of non-overlapping India windows across these
  samples is on the order of 20–40 — comfortably above the Tier-B floor (4–30) but
  short of confident Tier-A status given the small number of genuinely independent
  full boom-bust cycles (essentially two: 2008 GFC, 2020 COVID) inside the sample.
  Parameters frozen at inception per contract §4.
- **Momentum crash pattern (Daniel-Moskowitz mechanism)**: **Tier A globally**
  (>30 crash/rebound and volatility-regime observations across a century, 8
  markets); **Tier B for India specifically** (essentially 2 clean India
  crash-and-rebound observations in the studies found: 2008–09 and 2020, per
  Maheshwari-Dhankar 2017a and the general India-market-crisis literature). Given
  only 2 India observations at the *crash-timing* level, the India-specific timing
  signal itself sits close to the Tier-B/Tier-C boundary — the risk-management form
  (vol-scaling) should be trusted globally (Tier A), while any India-specific
  crash-trigger calibration should default toward the conservative, reduce-only
  posture the contract mandates for low-observation-count signals.
- **1-month cross-sectional reversal, India magnitude**: **Tier C**. Zero dedicated
  India studies of the specific 1-month-horizon, cost-inclusive magnitude were found;
  existing India reversal evidence is all at the 12–36 month horizon. Reduce-only per
  contract §4.
- **52-week-high momentum, India**: **Tier B** as a cross-country prior only (no India
  study found); parameters frozen at inception.
- **Time-series momentum (index + gold), global**: **Tier A** (58 instruments, 1965–
  2009, Moskowitz-Ooi-Pedersen, plus decades of subsequent CTA-industry replication at
  scale). **India equity TSMOM specifically**: **Tier B** (2 India-specific academic
  studies found). **Gold TSMOM in India/MCX specifically**: no dedicated study found —
  treat as an untested application of a Tier-A global mechanism, i.e. Tier B at best,
  parameters frozen at inception, and flagged [VERIFY] for the data phase to confirm
  before any material sizing.

---

## 6. Research method for the data phase

Every parameter above must be re-derived, not merely looked up, honoring contract §9:

1. **Price-only-first discipline (contract's decisive point).** Build the price-only
   momentum/reversal signal book (12-1, 6-1, 52-week-high, TSMOM) before any
   fundamentals-dependent factor, since this workstream's signals are the ones least
   contaminated by the free-data point-in-time-knowledge problem (Known Prior #7) —
   this is the natural first module to build and the cleanest test of whether the
   central capacity/decay question can be answered at all with free data.
2. **Purged, embargoed cross-validation**, embargo width scaled to the ~6–12 month
   half-life estimated in §3/§5 (i.e., an embargo materially longer than the 1-month
   embargo appropriate for the (Tier-C, reduce-only) reversal signal).
3. **Out-of-sample R² vs historical mean**, never in-sample Sharpe; explicitly
   reproduce the McLean-Pontiff out-of-sample/post-publication split methodology on
   the India sample itself (split India's own history into a pre- and
   post-"publication" era, using Agarwalla-Jacob-Varma (2013)'s publication as the
   natural India split point) to directly test whether Jacobs-Müller's "US-only decay"
   finding holds for India in our own data, rather than relying on their reported
   country-panel result alone.
4. **Deflated Sharpe ratio with true trial count**, counting every lookback/blend
   variant swept (12-1 vs 12-2 vs 6-1 vs 52-week-high vs every rank-blend weighting)
   as a trial — this workstream alone proposes at minimum ~6–8 candidate constructs
   (per the provenance table), each of which must be pre-registered before testing
   per contract §9.
5. **Stambaugh-bias correction** on any persistent predictor used in the composite
   rank (momentum ranks are less persistent than value/quality ranks, but the
   half-life is still long enough at 6–12 months to warrant the correction rather than
   assuming OLS standard errors are unbiased).
6. **Cost-stack calibration specific to India**: build the impact-cost model directly
   from NSE bhavcopy volume/ADV data (free source) by market-cap rank bucket, and
   apply it *before* reporting any net-of-cost momentum or reversal number — this is
   the direct, first-principles answer to "what survives costs at each book size,"
   replacing the qualitative capacity rows in §4 with numbers. STT (public, fixed
   rate) should be added as a simple deterministic overlay on top of the modeled
   impact cost, separately for delivery (both legs) vs any derivative overlay.
7. **Fixture-based testability**: per Known Prior #11, since this remote research
   environment has no live NSE/bhavcopy access, the signal-construction code (when the
   data phase begins) must resolve against a small committed fixture (a few months of
   representative bhavcopy + a known index reconstitution event) so the momentum/
   reversal module is unit-testable with zero live data, with the full-history
   backtest run separately on the principal's machine.
8. **Flash-crash exclusion test (OPEN_QUESTIONS Q5 default)**: when computing episode
   drawdowns for the crash-guard rule's validation, apply the default recovery-within-
   ~3-months test testably, not judgmentally, and explicitly check whether the 2008–09
   India momentum crash documented qualitatively here (Maheshwari-Dhankar 2017a) would
   be *included* as a binding drawdown episode under that rule (it should be — recovery
   took years, not months, per the BacktestIndia 65-month figure, however that figure
   itself needs independent, non-blog confirmation in the data phase).
9. **Never re-test a rejected idea with tweaked parameters** (contract §9): the 3-1
   standalone-momentum rejection in §4 should not be quietly revisited as "2-1" or
   "4-1" without a fresh, pre-registered survival argument.

---

## 7. Open questions and [VERIFY] items

- **[VERIFY]** Exact final publication venue for Sehgal & Ilango (Balakrishnan),
  *Momentum Profits, Portfolio Characteristics and Asset Pricing Models* (SSRN
  1374790) — confirm journal/year before citing as published rather than working paper.
- **[VERIFY]** Author byline for the Emerald *Risk-Managed Time-Series Momentum: An
  Emerging Economy Experience* paper (J. Economics, Finance and Administrative
  Science, 27(54):328–, Dec 2022) — search results confirmed title/journal/findings
  but not a clean author string.
- **[VERIFY]** Exact combined AUM of India's momentum-tracking passive products
  (UTI/Kotak/ICICI/Motilal Oswal/HDFC/Baroda BNP/Tata Nifty200 Momentum30 and Nifty
  Midcap150 Momentum50 vehicles). Search results returned inconsistent/implausible
  figures for several individual funds (apparent data-scrape errors); the ~₹46,000cr
  total smart-beta AUM and ~₹16,000cr single-rebalance trade size are corroborated
  independently and safe to use as order-of-magnitude anchors, but a clean, dated AUM
  table should be pulled directly from AMFI (free source) in the data phase.
- **No India-specific 1-month cross-sectional reversal magnitude/cost study was found**
  in this search. This is flagged as a first-order data-phase task, not merely a
  citation gap — it is the input the contract's "what survives costs" question for
  reversal most directly needs, and its absence is itself informative (plausibly
  because the effect, once STT and impact are counted, has never been worth an
  Indian academic's while to publish as a standalone strategy).
- **No India-specific 52-week-high momentum study was found.** Treated throughout as
  a cross-country (Tier B) prior only; a first data-phase task should be constructing
  this signal on Indian price-only history to get a first India-specific estimate.
- **No India/MCX-specific gold time-series-momentum study was found.** The asset-sleeve
  TSMOM-on-gold proposal in §4 rests entirely on the global Moskowitz-Ooi-Pedersen
  result plus current (2025–2026) anecdotal gold-price trend behavior reported by the
  World Gold Council (MCX gold +20% q/q, +81% y/y to a record Q1-2026 average, per
  their India-focus update) — anecdote, not evidence, and explicitly flagged as such.
- **niftyindices.com and several India research-paper hosts (nber.org, kentdaniel.net,
  apcz.umk.pl, alphaarchitect.com, backtestindia.com) could not be directly fetched**
  in this sandboxed research environment (egress-blocked); all findings from those
  sources were corroborated through multiple independent WebSearch summaries rather
  than a single primary fetch, and should be re-verified against the primary PDF/HTML
  directly once the data phase has broader network access.
- **Open design question interaction**: OPEN_QUESTIONS.md Q1 (Nifty 500 TRI as the
  signal-research benchmark) is assumed throughout; if the principal instead sets a
  per-book benchmark, the "what survives costs at each book size" capacity rows in §4
  would need re-scaling against each book's own benchmark universe rather than a
  single shared one.
- **Tension to flag explicitly for the principal**: Known Prior #10 (moderate book's
  engine is the factor book, not momentum) and this dossier's own turnover-budget
  arithmetic (§4) are mutually reinforcing, but they imply momentum is a *smaller*
  contributor to the moderate and conservative books than the aggressive book — the
  aggressive book is therefore carrying a disproportionate share of this workstream's
  proposed edge, which should be weighed against the aggressive book's small absolute
  capital (₹100–250cr) when the principal sizes expected contribution to firm-level
  P&L across the three books.
