# Workstream 08 — India Mid-Frequency Cycles and States (1–20y)

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout).
Scope: enumerate and evidence-grade every plausible India cycle/state variable between 1 and 20
years — RBI monetary policy, investment/capex, real estate, FII/FPI flow, earnings revision,
election, budget/tax-year, monsoon, the global financial cycle, oil shocks, and the IPO/issuance
cycle — apply the CONTRACT's clock test, and place each on the `tau_half`-ordered ladder with a
tier and influence cap.

**Methodological note, stated up front per CONTRACT §12's honesty requirement**: this workstream's
web-search budget was exhausted by earlier workstreams in this same research program before this
session could run its own searches (every `WebSearch` call returned "200 of 200 used"), and direct
`WebFetch` to RBI, SEBI, NBER, Wikipedia and other reference domains is blocked at the network
egress proxy in this environment (consistent with CONTRACT §7 Known Prior #11: "no market-data
network access… web search works" — that escape hatch was closed for this run). Every citation
below is therefore drawn from trained knowledge and graded by recollection confidence rather than
live verification, and is tagged accordingly: **(recalled, high confidence)** for citations I am
confident are stated correctly, or **[VERIFY: …]** naming exactly what needs checking (author,
year, venue, or a specific figure) once search/fetch access is restored. Per CONTRACT §12, findings
are kept, not dropped, and tagged. This dossier should be the first one re-run with live search
once budget resets, precisely because it is the most literature-dense of the batch.

---

## 1. Findings and literature

**F1. Santa-Clara & Valkanov, "The Presidential Puzzle: Political Cycles and the Stock Market"**
(*Journal of Finance* 58(5), 2003, pp. 1841–72) **(recalled, high confidence)**. U.S. monthly data,
1927–98: average excess equity returns are significantly **higher under Democratic presidencies
than Republican** (a differential on the order of several percentage points a year — I recall the
headline figure as roughly **9pp/yr**, **[VERIFY: exact pp figure]**), a spread **not explained** by
business-cycle risk proxies, and if anything associated with *lower* realized volatility under
Democrats — the opposite of a risk-based story. The paper is the canonical reference for "does the
identity of the government affect equity returns," directly relevant to India's own party-in-power
question, but the mechanism (partisan macro policy differences in a two-party system) does not
transplant cleanly to India's multi-party, coalition-prone system — used here only as the
methodological template (event-study + placebo macro controls), not as a transferable coefficient.

**F2. The broader U.S. "presidential/election-year cycle" literature** (Huang 1985; Booth & Booth
1997; Wong & McAleer 2009 among others) **[VERIFY: exact authors/years — recalled with only
moderate confidence]**, claiming U.S. stocks do best in **year 3** of the four-year presidential
term and worst in year 2. Multiple later re-examinations report the pattern **weakening or
disappearing out-of-sample** after the effect became well known — a textbook illustration of the
CONTRACT's own McLean-Pontiff decay logic, and the reason this dossier treats any specific
"calendar phase within the political cycle" pattern as **inadmissible without a fresh, pre-
registered India test**, not importable from the U.S. literature.

**F3. Rey, "Dilemma not Trilemma: The Global Financial Cycle and Monetary Policy Independence"**
(Jackson Hole Economic Policy Symposium, Federal Reserve Bank of Kansas City, Aug 2013; also
circulated as an NBER Working Paper, low-21,000s series **[VERIFY: exact WP number/year — I recall
approximately NBER WP 21162 but cannot confirm without search]**) **(recalled, high confidence on
substance)**. Central claim: a single global factor — correlated with the VIX — drives co-movement
in cross-border credit flows, leverage of global (mainly US/European) banks and asset managers, and
risky-asset prices worldwide, **largely independent of the exchange-rate regime**. This collapses
the classic Mundell-Fleming "trilemma" (fixed FX + free capital + independent monetary policy: pick
two) into a **"dilemma"**: independent monetary policy requires **capital controls**, full stop —
floating the currency does not, by itself, buy monetary autonomy once the global financial cycle
dominates. Mechanism = a structural/institutional feature of global bank and fund leverage, not a
crowdable cross-sectional anomaly.

**F4. Miranda-Agrippino & Rey, "US Monetary Policy and the Global Financial Cycle"** (*Review of
Economic Studies*, ~2020 **[VERIFY: exact volume/issue/pages — recalled as v87(6), pp. ~2754–76,
moderate confidence]**) **(recalled, high confidence on substance)**. Dynamic-factor extraction of a
single global factor from a large panel of risky asset prices; shows the factor is significantly
driven by **US monetary-policy shocks**, operating through a **risk-taking channel** (leverage
cycle of global intermediaries), not simply uncovered-interest-parity/trade-flow channels. Directly
operationalizes F3: gives a factor-model recipe for a constructible "global financial cycle" state
variable.

**F5. Forbes & Warnock, "Capital Flow Waves: Surges, Stops, Flight, and Retrenchment"** (*Journal
of International Economics* 88(2), 2012, pp. 235–51) **(recalled, high confidence)**. Distinguishes
**gross** flow episodes — surges/stops (foreigners) vs. flight/retrenchment (domestics) — across a
large emerging/advanced-market panel, and finds these episodes are driven substantially by **global**
factors (VIX-type risk proxies, global growth, global interest rates) rather than purely
country-specific "pull" factors. This is the paper that formalizes "capital flow waves" as
irregular, VIX-correlated episodes rather than a fixed-period cycle — directly informs this
dossier's classification of the FII-flow/global-financial-cycle candidates as **state variables**,
not periodic cycles (§2, clock-test table).

**F6. Cerutti, Claessens & Puy, "Push Factors and Capital Flows to Emerging Markets"** (IMF Working
Paper, later *Journal of International Economics*, ~2019 **[VERIFY: exact year/volume — moderate
confidence]**) **(recalled, moderate-high confidence on substance)**. Global "push" factors (VIX, US
rates) explain a large share of the variance of portfolio flows into EMs, with the sensitivity
**varying by the type of intermediary** — flows via open-end mutual funds are markedly more
sensitive to global risk swings ("hot money") than flows via more captive vehicles (e.g., pension
funds, sovereign wealth funds) — a genuinely useful India-relevant nuance: not all FII AUM is
equally flighty, and a crude aggregate net-FPI-flow series conflates fast and slow money.

**F7. Claessens, Kose & Terrones, "Financial Cycles: What? How? When?"** (IMF Working Paper
WP/11/76, 2011; related to their NBER *International Seminar on Macroeconomics* chapter and
"How Do Business and Financial Cycles Interact?", *Journal of International Economics*, 2012)
**(recalled, moderate-high confidence)**. Documents credit, house-price and equity-price cycles
across a panel of **~20+ advanced and emerging economies** over several decades; house-price
cycles are on average **longer and larger-amplitude** than credit or equity cycles, and recessions
coinciding with a housing-cycle downturn are markedly deeper and slower to recover from. This is
the cross-country panel this dossier leans on to argue India's real-estate cycle — domestically
observed for barely one down-leg — can still be defensibly graded Tier B via the CONTRACT's
"n<4 with ≥10 cross-country analogues" clause (§4).

**F8. Griffin, Nardari & Stulz, "Are Daily Cross-Border Equity Flows Pushed or Pulled?"** (*Review
of Economics and Statistics* 86(3), 2004) **(recalled, moderate confidence on exact country panel —
I believe South Korea, Taiwan and Thailand are core markets in the sample; **[VERIFY: whether India
is literally included, or only comparably-structured Asian markets]**)**. Central finding: daily
cross-border flows respond to **past domestic and US returns** (positive-feedback/return-chasing
behavior) far more than flows **predict future returns** — i.e., in the countries studied, **flows
follow returns**, contradicting the popular retail narrative that "FII buying drives the market."
Directly informs the FII causality question (§2, §3) even where the exact country panel needs
re-confirmation.

**F9. Baker & Wurgler, "The Equity Share in New Issues and Aggregate Stock Returns"** (*Journal of
Finance* 55(5), 2000) **(recalled, high confidence)**. When equity issuance's share of total
(equity+debt) financing is high, subsequent one-year **aggregate market returns are lower** —
firms and underwriters time issuance to periods of rich valuation, and the market partially
mean-reverts. This is the specific "IPO/issuance cycle as sentiment state" mechanism the workstream
brief names, predating the more famous 2006 cross-sectional paper below.

**F10. Baker & Wurgler, "Investor Sentiment and the Cross-Section of Stock Returns"** (*Journal of
Finance* 61(4), 2006) **(recalled, high confidence)**. Builds a composite sentiment index (closed-
end fund discount, NYSE turnover, IPO volume and average first-day return, equity share in new
issues, dividend premium); when sentiment is high, stocks that are **hard to value/arbitrage**
(small, young, volatile, unprofitable, high-growth/distressed) subsequently **underperform**, and
vice versa in low-sentiment states — a *conditioning* result (sentiment interacts with a
cross-section), not a pure market-timing signal.

**F11. Baker, Wurgler & Yuan, "Global, Local, and Contagious Investor Sentiment"** (*Journal of
Financial Economics* 104(2), 2012, pp. 272–87) **(recalled, moderate-high confidence; [VERIFY:
exact country panel — I believe six major developed markets, likely NOT including India in the
original set]**)**. Builds local sentiment indices for several major markets plus a "global"
component, finds the Baker-Wurgler cross-sectional conditioning result **replicates internationally**
and that a global sentiment factor has additional, "contagious" explanatory power beyond local
sentiment alone. Used here as the cross-country-analogue basis for treating the IPO-issuance-cycle
mechanism as Tier B for India (methodology transfers; India-specific numeric coefficient does not
yet exist in the literature to my knowledge).

**F12. Ritter, "The Long-Run Performance of Initial Public Offerings"** (*Journal of Finance* 46(1),
1991, pp. 3–27) **(recalled, high confidence)**, and the earlier Ibbotson & Jaffe, **"'Hot Issue'
Markets"** (*Journal of Finance* 30(4), 1975) **(recalled, moderate confidence)**. Establish the
"hot IPO market" pattern: periods of unusually heavy issuance and high first-day pops are followed
by **below-benchmark long-run returns** for that IPO cohort — the same mechanism as F9/F10 viewed
from the issuance-cohort side rather than the aggregate-market side, and the literature Jay Ritter's
long-maintained public IPO dataset (US-focused) has repeatedly reconfirmed over subsequent decades.

**F13. Hamilton, "Oil and the Macroeconomy since World War II"** (*Journal of Political Economy*
91(2), 1983, pp. 228–48) **(recalled, high confidence)**, and Kilian, **"Not All Oil Price Shocks
Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market"** (*American Economic
Review* 99(3), 2009, pp. 1053–69) **(recalled, high confidence)**. Hamilton: most post-WWII US
recessions were preceded by an oil price spike. Kilian's refinement — the crucial one for a net
oil-*importer* like India — is that the **source** of an oil shock matters: a **supply-driven**
shock (geopolitical disruption) is unambiguously a negative terms-of-trade/cost shock for an
importer, while a **demand-driven** shock (synchronized global growth) may coincide with strong
export/growth tailwinds that partly offset the import-bill damage. A flat "oil up = bad for India"
rule is a magic-number-style oversimplification the Kilian decomposition explicitly warns against.

**F14. Hirshleifer & Shumway, "Good Day Sunshine: Stock Returns and the Weather"** (*Journal of
Finance* 58(3), 2003, pp. 1009–32) **(recalled, high confidence)**. Sunshine in the city of a
country's main exchange correlates weakly but statistically significantly with that day's index
return, across 26 countries. This is a **daily-frequency behavioral-mood** effect, mechanistically
distinct from — and far higher-frequency than — the "monsoon as a macro/agri-income channel"
argument this workstream is actually evaluating; cited here only to draw that boundary explicitly
so the two are not conflated (see §2, monsoon).

---

## 2. India-specific evidence

**I1. RBI monetary-policy-rate chronology and the inflation-targeting regime.** The Monetary Policy
Committee (MPC) was constituted under the amended RBI Act in 2016, with an explicit flexible
inflation-targeting (FIT) mandate — CPI at **4% ± 2%** — formalized by the Feb 2015 Monetary Policy
Framework Agreement and given statutory force later that year; the first MPC meeting was Oct 2016
**(recalled, high confidence on the institutional facts; [VERIFY: exact 2015 agreement date]**)**.
Before 2011 the operative policy-rate architecture went through several transitions (Bank Rate era,
phased introduction of the Liquidity Adjustment Facility from 2000) before RBI adopted the modern
single-repo-rate corridor in **May 2011**. A best-effort repo-rate chronology since the early 2000s
(free source: RBI DBIE / RBI Monetary Policy Statements, all public): trough near **6%** (2003–04)
→ peak **9.00%** (Jun–Jul 2008, pre-GFC) → sharp GFC-response cuts to a trough near **4.75%**
(spring 2009) → hiking cycle to **8.50%** (Oct 2011) → partial easing to **~7.25%** (mid-2013),
interrupted by the **Sept 2013 taper-tantrum defense** (temporary MSF-corridor tightening under
Governor Rajan) → renewed hikes to **8%** (early 2014, coinciding with adoption of the Patel-
committee disinflation glide path, Jan 2014) → a long, bumpy easing sequence (brief 2018 hikes to
6.50% aside) to **5.15%** (Oct 2019) → COVID emergency cuts to a record-low **4.00%** (May 2020,
held for an unusually long ~22 months) → a sharp hiking cycle (May 2022–Feb 2023) to **6.50%**,
held through 2023–24 → a new easing cycle beginning **Feb 2025** under Governor Sanjay Malhotra
(figures for 2025 magnitude/pace **[VERIFY: too recent for confident recall without search]**).
Counting genuine full round-trips (trough→peak→trough) since 1998 is exactly as boundary-sensitive
as the credit-cycle counting problem documented in Workstream 03's dossier: depending on whether the
2009–2019 span is one long complicated easing-with-a-hiking-bump cycle or two, the domestic count is
**n≈4–5**, sitting right at the CONTRACT's clock-test threshold. **This is a marginal pass**, not a
clean one (§ clock-test table below).

**I2. RBI transmission-lag literature.** RBI's own Monetary Policy Reports and DEPR working-paper
series have repeatedly estimated the pass-through of a policy-rate change to output and inflation as
occurring with a lag on the order of **2–3 quarters for the first, partial effect and 4–6 quarters
(roughly 12–18 months) for the fuller effect** to show up **[VERIFY: I cannot confidently attribute
this to one specific numbered DEPR working paper without search access; this figure is a
widely-repeated summary of RBI's own stated framework rather than a single verified citation]**.
This is broadly consistent with international "long and variable lags" findings (the classic
Friedman framing) and matters directly for how this workstream's monetary-cycle state variable
should be lagged before use — a rate cut/hike should not be expected to show up in equity-relevant
growth/earnings data for roughly a year.

**I3. RBI OBICUS (Order Books, Inventory and Capacity Utilisation Survey)**, published quarterly
since **~2008**, free via RBI DBIE/press release: manufacturing capacity utilization has ranged
roughly **65–68% in slack periods** (notably through much of 2013–2020) to **75–78% in boom
periods**. A popular practitioner heuristic treats **~75%** utilization as the level above which
fresh private capex "switches on" — this is exactly the CONTRACT §6 "magic number" trap; the
correct construction is the **percentile rank of trailing OBICUS utilization**, not a fixed
threshold. **MOSPI's IIP capital-goods sub-index** (monthly, free, use-based classification,
current base year 2011–12 after a 2017-era revision from 2004–05 **[VERIFY: exact revision year]**)
and **quarterly Gross Fixed Capital Formation (GFCF) as % of GDP** (MOSPI National Accounts, free)
are the other two free capex-cycle proxies: GFCF/GDP peaked near **34–35%** in the 2007–08 boom,
fell to roughly **28–29%** through the 2011–2020 "capex winter," and has been recovering toward
**~31–33%** since 2022–23 **[VERIFY: exact GFCF/GDP figures — recalled directionally with moderate
confidence, not to be treated as precise]**. **Constructibility caveat**: the widely-cited
project-announcement-based capex trackers (e.g., CMIE Capex) are a **paid** data source and cannot
be used under the CONTRACT's free-data rule; RBI's own annual "Private Corporate Investment: Trends
and Prospects" article draws partly on CMIE-sourced data, so its headline investment-intentions
figures are not independently reconstructible for free — flagged as an **unavailable** input, with
OBICUS + IIP capital goods + GFCF/GDP as the free substitute triad.

**I4. India capex-cycle chronology (n = 2–3, per the workstream brief's own framing, corroborated
above): boom 2003–08, prolonged slump/"Twin Balance Sheet" drought 2011–2020, revival 2021+**
(PLI-scheme-linked manufacturing investment, private capex broadening from 2023–24). This overlaps
substantially with Workstream 03's credit-cycle chronology (same underlying corporate-leverage
story, viewed from the real/investment side rather than the credit/NPA side) — **explicit
double-counting warning**: this dossier's capex-cycle state variable and Workstream 03's credit-
cycle/GNPA state variable are likely **highly correlated, not independent**, and must not both be
weighted at full strength in the composite regime score.

**I5. RBI House Price Index (HPI)** (quarterly, 10 major cities, base 2010–11=100, published since
**2010**, free via RBI DBIE) and **NHB RESIDEX** (National Housing Bank, published since **2007**,
now covering roughly **50 cities**, free). Both indices are simply too short to observe more than
about **one** full up-down leg: a 2003–2008-ish boom (largely pre-dating both indices' clean start),
a long stagnation/correction roughly **2013–2020** (well documented in industry press as a
multi-year residential-real-estate slump, especially acute in NCR and Mumbai, with historically
high unsold-inventory months-to-sell), and a premium-housing-led recovery from **2021**. **Free
supplementary proxies**: RBI's sectoral-deployment-of-credit series isolates bank credit to
"housing" (monthly, free); some state sub-registrar portals (e.g., Maharashtra IGR) publish free
property-registration counts/values, though only for that state, not nationally. The real-estate
cycle is mechanically close to the "medium-term financial cycle" already characterized in
Workstream 03 (Borio et al.'s own finding that credit+property co-movement, not equity, defines the
international financial cycle) — again an explicit **overlap/double-counting flag**.

**I6. FII/FPI flow data and the flows-returns causality question.** NSDL publishes daily and monthly
net FPI investment (equity and debt separately) free at `fpi.nsdl.co.in`; SEBI also publishes FPI
registration and flow bulletins free. India-specific academic evidence on causality directionality
— **Chakrabarti, "FII Flows to India: Nature and Causes"** (*Money & Finance*, ICRA Bulletin, 2001)
**[VERIFY: exact venue — recalled with moderate confidence]**, using monthly data from the early
FII-regime years (FIIs were first permitted into Indian equities in **September 1992**), finds
**returns explain flows better than flows explain returns** — i.e., **positive-feedback/return-
chasing** by foreign investors, not the popular "FII buying causes the rally" story — consistent
with the international Griffin-Nardari-Stulz (F8) result. Several subsequent Indian studies broadly
corroborate a bidirectional-but-returns-leading relationship **[VERIFY: I recall this literature
existing (e.g., work along the lines of Mukherjee/Bose/Coondoo-style Granger-causality studies in
Indian finance journals through the 2000s) but cannot confidently attribute specific author/year/
venue triples without search]**. **Design implication**: a naive "buy when FII flows are positive"
signal is almost certainly trading on the *lagging*, return-chasing half of the relationship, which
should decay under the CONTRACT's own logic (it is a well-known, widely-published pattern by now) —
whereas an **FII-ownership-level/positioning-extremes** signal (percentile rank of cumulative
FII holding relative to its own trailing history, or of trailing 12-month cumulative net flow
relative to trailing-mean flow) is a structurally different, harder-to-arbitrage construct because
unwinding an extreme foreign-ownership position requires the actual capital to move, which is
capacity-limited (see §3).

**I7. India-specific institutional detail bearing directly on the FII-flow signal**: (a) **DII
(domestic institutional investor) flows — principally mutual-fund SIP inflows and insurance/pension
AUM growth — have become a structurally large, steadily growing counterweight to FII flow
volatility since roughly 2014–17**; AMFI publishes free, monthly systematic-SIP-inflow data, which
has grown from a few thousand crore/month in the mid-2010s to a figure regularly exceeding
**₹20,000 crore/month** by the mid-2020s **[VERIFY: exact recent monthly SIP figure — this grows
fast enough that any specific number is stale within months]**. This is a genuine, well-documented
("FII sells, DII buys" is now a standard financial-press framing) structural shift, and a strong
candidate **decay argument in the other direction**: the FII-flow-return relationship documented in
older studies (I6) may itself be *weakening over time* as DII flow has grown large enough to absorb
a meaningfully larger share of FII selling pressure than it could a decade ago — this should be
tested directly (rolling-window re-estimation of the flows-returns relationship) once the data phase
begins, rather than assumed. (b) **SEBI's shareholding-pattern disclosure requirement (SEBI LODR
Regulations)**: every listed company must disclose its full shareholding pattern — promoter, FII,
DII, public — **within 21 days of each quarter-end**, free, per-stock. This is an under-used **free,
quarterly, stock-level FII/DII/promoter-ownership panel** distinct from (and complementary to) the
NSDL aggregate flow series, and is the natural basis for constructing a **free-float-scaled** FII-
ownership-percentile signal at the individual-name level — important because India's unusually high
**promoter concentration** (many NIFTY 750 constituents have promoter holdings in the 40–75% range)
means a given rupee of FII buying moves a much smaller free float than the same flow would in a
dispersed-ownership market, so any FII-positioning signal must be scaled by free float, not total
market cap. (c) **SEBI's SAST (Substantial Acquisition of Shares and Takeovers) Regulations** set
disclosure triggers at an initial **5%** stake and further disclosure at each **2%** change
thereafter — a free, real-time (via exchange bulk/block-deal and SAST filings) source of large-
holder positioning changes, complementary to the quarterly shareholding-pattern data.

**I8. Election cycle.** Nine general elections since 1991 (**1991, 1996, 1998, 1999, 2004, 2009,
2014, 2019, 2024**), giving **eight completed inter-election intervals**, of which the **five since
1999** (1999–2004, 2004–09, 2009–14, 2014–19, 2019–24) ran the constitutionally-mandated full
**5-year** term (Article 83(2) caps the term at five years; the 1996–99 sequence reflects three
short-lived coalition governments and is the historical exception, not the rule, post-1999).
Result-day market behavior has been driven by **surprise relative to expectations**, not by the
mere fact of an election, which is the standard "uncertainty resolution" pattern found in
international election-and-volatility literature generally: **17 May 2004** — a surprise NDA
defeat and a Congress-led UPA government dependent on Left-Front outside support triggered one of
independent India's most famous single-day crashes (Sensex fell on the order of **10–15% intraday**,
trading halted by circuit breakers, closing down roughly **11%** **[VERIFY: exact % — recalled with
only moderate confidence on the precise number, high confidence on the episode itself]**), on fears
of a reform reversal. **18 May 2009** — UPA returned with a much larger, Left-independent mandate;
Sensex opened with a historic surge (on the order of **15–17%** intraday) large enough to trigger an
upper-circuit trading halt within minutes **[VERIFY: exact %]**. **16 May 2014** and **23 May 2019**
— Modi/BJP wins were both substantially pre-anticipated by exit polls and a preceding rally, so
result-day moves were comparatively muted ("buy the rumor" dynamics). **4 June 2024** — the sharpest
recent illustration of the expectations-vs-outcome point: 1 June 2024 exit polls implied a large
NDA landslide and markets rallied hard that day; the actual 4 June results showed BJP short of a
majority on its own, requiring coalition partners (TDP, JD(U)) — Sensex/Nifty fell sharply intraday
(on the order of **5–6%**, one of the larger single-session falls in recent years **[VERIFY: exact
%]**) before recovering over subsequent weeks as coalition stability firmed up. India VIX (NSE,
published since 2008, free) is the natural free instrument for observing the pre-election
uncertainty premium and its post-result collapse. **Design implication, consistent with CONTRACT
Known Prior #3**: the election clock is best used as a **volatility-regime/leverage-permission**
trigger — pre-scheduled de-risking into the vote window, conditional re-levering keyed to a
mandate-clarity classification post-result — not as a directional bet on which way the market will
move, since the direction is itself conditional on a surprise that cannot be forecast from the
calendar alone.

**I9. Budget/fiscal-year seasonality.** The Union Budget has been presented on **1 February** each
year since Budget 2017 (previously the last working day of February; the Railway Budget was also
merged into the general Budget starting that year) **(recalled, high confidence)**; India's fiscal
year runs **1 April – 31 March**, unlike the US calendar tax year. Budget day is well documented
(practitioner-level; a rigorous India-specific academic event-study citation is not confidently
recalled here — **[VERIFY]**) as a day of markedly elevated intraday volatility (India VIX spikes),
with sector-specific abnormal moves keyed to sector-targeted announcements (customs/excise duty
changes, capex allocation, PLI-scheme extensions). The **March/April fiscal-year-end** window is the
natural Indian analogue to the US "January effect" (Rozeff & Kinney 1976 **[VERIFY: exact citation,
recalled with moderate confidence]** — small-cap outperformance in January linked to December
tax-loss-selling): a plausible **March tax-loss-harvesting / April reversal** pattern in Indian
small- and micro-caps, given STCG/LTCG booking incentives before the 31 March fiscal year-end — I
hold only moderate confidence that a rigorous India-specific academic paper has quantified this
cleanly; treat as a **hypothesis for the data phase**, not an established finding. **STT
(Securities Transaction Tax)**, introduced in Budget 2004, is a permanent structural change (not a
cyclical signal) that materially affects the cost stack — cross-reference Workstream 05 rather than
re-deriving here. Free data: NSE/BSE bhavcopy, India VIX (NSE), Union Budget documents
(`indiabudget.gov.in`, free), PIB budget-speech archive (free).

**I10. Monsoon.** The India Meteorological Department (IMD) publishes South-West Monsoon
(June–September) seasonal rainfall as **% of Long Period Average (LPA)**, free, with a usable
public record extending back many decades (well beyond the equity-market sample). Agriculture is now
roughly **15–18% of GDP** (a shrinking share versus decades past), but **rural consumption**
(two-wheelers, tractors, FMCG rural volumes, agrochemicals) remains a genuinely monsoon-sensitive
equity theme, and monsoon shocks feed food-price inflation, which in turn feeds the RBI's
inflation-targeting reaction function (I1/I2). I do **not** hold a confident specific citation for a
rigorous India academic paper directly quantifying an **aggregate-index**-level monsoon-return
relationship — the workstream brief itself flags this as a "weak effect – quantify," and my honest
assessment is that the literature I can recall on this specific link is thin or uncertain enough to
warrant **[VERIFY: India monsoon–equity-market academic study]** rather than a citation. The
closest confidently-verified academic touchstone for "weather affects markets" is Hirshleifer &
Shumway (F14) — but that is a **daily-frequency sunshine-mood effect**, mechanistically unrelated to
the **seasonal agri-income channel** this workstream is actually assessing; the two should not be
conflated. **Design implication**: treat monsoon deviation as, at most, a narrow **sector-level**
(rural-consumption names), reduce-risk-only confirming input, not an index-level signal, pending a
proper India-specific quantified study.

**I11. Oil shocks and India.** India imports on the order of **85%+** of its crude oil requirement
**[VERIFY: precise current-year import-dependence %, this drifts slightly year to year]** — a large,
structural current-account/terms-of-trade channel. Rule-of-thumb sensitivities repeated across RBI
commentary and financial press (a genuine RBI working-paper citation for the exact coefficient is
**[VERIFY: not confidently recalled]**) put a sustained **$10/bbl** rise in crude at roughly
**0.4–0.5% of GDP** additional current-account-deficit widening and on the order of **20–30bps** of
additional CPI inflation, alongside fiscal-math pressure (though the pre-2014 administered-fuel-
price/subsidy regime has been substantially deregulated since). **Episode chronology, applying
Kilian's (F13) supply/demand decomposition**: the **1990–91 Gulf War** oil shock contributed
directly to India's 1991 balance-of-payments crisis (a genuine, high-confidence historical fact); the
**2003–08** secular rise (~$25 to ~$147/bbl, Jul 2008) was substantially demand-driven (synchronized
global boom, coinciding with India's own credit/capex boom) and therefore less unambiguously
damaging than a pure supply shock, though CAD still widened; the **2014–16 collapse** (~$115 to
~$27/bbl) was a large **net positive** for India as an importer, widely credited as a tailwind for
the 2014–17 disinflation and fiscal consolidation narrative; the **2022 Russia-Ukraine** spike
(Brent briefly above **$120/bbl**) was supply-driven and unambiguously negative for CAD/INR/
inflation, though India's shift toward large-volume **discounted Russian crude purchases** post-2022
(a well-documented, somewhat geopolitically contentious policy choice) materially cushioned the
direct import-bill impact — a genuinely current India-specific institutional wrinkle that changes
how a generic "oil shock" signal should be interpreted post-2022 versus pre-2022. **Free data**:
Brent/WTI spot (FRED series `DCOILBRENTEU`/`DCOILWTICO`, free); India's petroleum import bill and
crude basket price (Petroleum Planning & Analysis Cell, Ministry of Petroleum & Natural Gas, free);
RBI DBIE balance-of-payments tables (free); Kilian's own supply/demand-decomposed "global real
economic activity index" is maintained and freely downloadable from his personal academic webpage
**[VERIFY: current URL/maintenance status]**, a genuinely useful free input for separating demand-
from supply-driven oil moves rather than treating "oil price level" as a single undifferentiated
signal (consistent with CONTRACT §6's no-magic-numbers spirit).

**I12. IPO/issuance cycle — India SME IPO froth, 2023–24.** SME-platform IPOs (BSE SME, NSE Emerge)
saw a well-documented explosion of issuance volume, extreme oversubscription and outsized listing-day
gains through 2023–2024, prompting explicit **SEBI regulatory action** — a mid-2024 consultation
paper/circular tightening SME-IPO eligibility, promoter lock-in and disclosure norms, with public
comments from SEBI leadership flagging "froth" and possible manipulation in the segment
**[VERIFY: precise date and SEBI document reference for the 2024 SME-IPO tightening circular]**.
This is an unusually clean, **current, regulator-verified real-world instance** of the Baker-Wurgler
(F9/F10) mechanism playing out in India, even absent a peer-reviewed India-specific paper (the
episode is too recent for one to exist yet). **Mainboard IPO cycle**: distinguishable boom-bust legs
in 2007–08 (pre-GFC), a long lull 2009–2013/17, a large 2021 COVID-era boom (Zomato, Nykaa, Paytm,
PolicyBazaar and others, several richly priced and subsequently sharply corrected — Paytm's post-IPO
decline is a widely cited, almost canonical Indian illustration of hot-issuance-then-mean-reversion),
a quieter 2022, and a strong, broad-based revival 2023–2025 in which India became one of the largest
global IPO markets by count and, in some years, by value **[VERIFY: exact global-ranking claim and
year]**. **Free data for constructing an issuance-share/first-day-pop signal**: NSE/BSE issue
documents and listing data (free), SEBI's DRHP/offer-document repository and monthly "IPO
Watch"/bulletin (free), first-day listing gains fully computable from free bhavcopy (issue price vs.
listing-day close) — this is a genuinely **good-free-data** candidate, no paid feed required.
**SEBI's ASM/GSM (Additional/Graded Surveillance Measures) framework** — which places stocks
(often recently-listed small/SME names) showing unusual price-volume patterns under additional
margin and trading-band restrictions, published free and updated regularly by NSE/BSE — is itself a
usable free, real-time, regulator-generated "this name is frothy" flag, complementary to a
constructed issuance-share signal.

---

## 3. Decay and crowding assessment

**Edge A — RBI monetary-policy stance as a regime state variable** (I1, I2). *Survival argument*:
**(iv) institutional constraint** — even though every rate decision is immediately public and priced
by the OIS/bond market (no simple "buy after a cut" announcement-return anomaly should survive), the
**economic transmission** operates through structurally slow channels — bank balance-sheet
re-pricing, loan-reset dates, the bank-lending channel dominant in India's bank-heavy financial
system — so a **loose/tight stance classification lagged by roughly a year** (per I2's transmission-
lag literature) is not something a faster trader can arbitrage away merely by knowing the policy
rate. *Decay treatment*: treat this **only** as a lagged regime input (leverage/hedge-ratio
permission), never a same-day event-return trade; explicitly coordinate with Workstream 03's credit-
cycle block, since the mechanism (bank lending channel, credit-to-GDP gap) substantially overlaps —
apply a **shared risk budget**, not two independently-sized signals.

**Edge B — Capex and real-estate cycles as sector-level state variables** (I3, I4, I5). *Survival
argument*: **(ii) capacity limit** — a large capex/real-estate down-cycle unwind (stalled projects,
land-title/approval delays, sector-wide overleverage) takes years of real balance-sheet repair to
resolve; no amount of information efficiency shortens that physical/legal/financing timeline, so a
sector-level "avoid capex-heavy names in the down-phase" tilt is not quickly arbitraged away by
faster capital. *Decay treatment*: **no India-specific quantified predictive study exists for either
signal** at the domestic level (n too small even to attempt one); promote to **Tier B only via the
cross-country-analogue clause** (Claessens-Kose-Terrones, F7, for real estate; general EM-investment-
cycle literature, no single clean citation recalled for capex specifically — **[VERIFY]**), with an
explicit McLean-Pontiff-style generic haircut band (26%/58%) applied as a placeholder pending India
validation, and an explicit **double-counting flag** against Workstream 03's credit/business-cycle
block (I4, I5 above).

**Edge C — FII flow momentum vs. FII positioning extremes** (I6, I7). Two distinct edges requiring
opposite treatment. **FII flow *momentum*** (buy when trailing net flow is positive): *survival
argument* — **none holds**. This is the well-published, decades-old "flows follow returns"
positive-feedback pattern (F8, I6); it is public, mechanical, and exactly the kind of pattern
McLean-Pontiff's decay logic targets. **Explicit numeric haircut**: apply the full **McLean-Pontiff
26% (out-of-sample) / 58% (post-publication) band**, and additionally down-weight for the I7(a)
structural DII-growth argument (the mechanism this pattern relies on — thin domestic absorptive
capacity for FII flow shocks — has itself been shrinking for a decade). **FII ownership-level/
positioning-extremes** (percentile rank of cumulative FII holding or of trailing flow relative to its
own history, free-float-scaled per I7(b)): *survival argument* — **(ii) capacity limit** and **(iv)
institutional constraint** jointly — unwinding an extreme foreign-ownership position requires actual
capital reallocation at a scale no single domestic desk can front-run, and India's shallow, circuit-
band-constrained market for absorbing large directional unwinds (§2 institutional detail) slows any
correction further. *Decay treatment*: no specific quantified India study recalled; Tier C pending
data-phase construction, reduce-risk-only until validated (CONTRACT §4).

**Edge D — Election / Budget / Monsoon as a calendar-anchored bucket** (I8, I9, I10). *Survival
argument*: **(i) structural** — the *timing* of each event is fixed by law or the physical calendar
and cannot be arbitraged away (nobody can move an election date or a monsoon season), but the
**direction and magnitude of the market reaction is not similarly fixed** — I8 shows result-day
moves are driven by surprise-relative-to-expectation, not by the calendar slot itself, so any
directional edge here would need its own survival argument, which none of the three candidates
currently has beyond "the timing is known in advance." *Decay treatment*: use the calendar
predictability itself (permission-scheduling: reduce leverage into the vote window / budget day;
reduce-only for monsoon given the honestly weak/unquantified aggregate effect) rather than sizing any
directional bet; this sidesteps the decay question by not claiming a return edge that has to survive
crowding — the value here is **risk scheduling**, not alpha, consistent with CONTRACT Known Prior #3.

**Edge E — The global financial cycle / dollar-VIX regime hitting India** (F3–F6, F8, I6). *Survival
argument*: **(iii) genuine risk premium** combined with **(iv) institutional constraint** — EM assets
carry a compensated risk premium precisely because they are exposed to a common, undiversifiable
global factor (F3, F4) that domestic-only investors cannot hedge away, and India's own capital-flow-
management toolkit (FPI debt limits, macroprudential measures) is itself evidence the RBI treats this
as a structural vulnerability requiring institutional response, not a phenomenon that will be
arbitraged into irrelevance. *Decay treatment*: this is **not** a McLean-Pontiff-style crowded
cross-sectional anomaly — it is closer to a compensated tail-risk factor, evidenced by a large pooled
international literature (F3–F6 collectively span dozens of countries and multiple decades — easily
clearing Tier A's ≥30-observation bar at the pooled level). **The nuance that matters for sizing**:
treat the **methodology** (VIX/dollar-strength as a global risk-state proxy) as Tier A, but the
**India-specific transfer coefficient** (how much India-equity/INR/flow risk to price per unit of
global-factor move) as Tier B at best until estimated domestically — exactly the same "methodology
Tier A, India-actionable coefficient Tier B" distinction Workstream 03 draws for its own credit-
cycle findings.

**Edge F — Oil shocks** (F13, I11). *Survival argument*: **(iii) genuine risk premium** — India's
current-account exposure to oil is a real, undiversifiable structural fact, not a discovered
anomaly; the market should and does price it, and there is no reason to expect this exposure to
"decay." *Decay treatment*: not applicable in the McLean-Pontiff sense (this is a mechanism-based
state variable, not a factor return); the actionable design point instead is **Kilian's supply/
demand decomposition** — a flat "oil price level" signal is a magic-number-style oversimplification
that should be replaced with a demand-vs-supply-decomposed signal (via Kilian's public index or a
constructed India-specific analogue) before it is trusted.

**Edge G — IPO/issuance-share sentiment cycle** (F9–F12, I12). *Survival argument*: a genuine mix —
**(i) structural/behavioral** (issuers and underwriters have a persistent incentive to time issuance
to rich valuations; retail/SME investors chasing listing-day pops is a durable behavioral pattern,
not a one-off) and **(ii) capacity limit** (SEBI's own ASM/GSM and 2024 SME-IPO-tightening actions
are direct institutional evidence that regulators view this segment as structurally prone to
overheating and hard to arbitrage away quickly at scale, especially under the mandate's hedge-only
constraint — there is no clean way to short a hot SME IPO segment directly). *Decay treatment*:
Baker-Wurgler-style findings are decades old and well known (F9 is from 2000), so apply the generic
**McLean-Pontiff 26%/58% haircut band** as the default prior on any aggregate-issuance-share
market-timing signal, while treating the **stock-specific, hard-to-value-name conditioning result**
(F10) as a likely input to the already-existing momentum/quality workstreams (01/02) rather than a
new independent signal here — flag for reconciliation.

---

## 4. Proposed parameters

| Name | Value / range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| RBI monetary-cycle domestic count (post-1998) | n≈4–5 trough-to-trough round trips, boundary-sensitive | I1 | B (marginal) | Low-Medium | Not a crowdable anomaly; lag by ~1yr (I2) before use | A 6th completed round trip; a cleaner boundary convention |
| Monetary-policy transmission lag | ~2–3 quarters (partial), ~4–6 quarters (fuller effect) | I2 (RBI framework, [VERIFY exact WP]) | B | Medium | N/A — structural, not decaying | A primary RBI DEPR WP with a directly estimated lag distribution |
| Capacity-utilization (OBICUS) percentile rank | Percentile rank of trailing series, not a fixed 75% threshold | I3 | C (no quantified India predictive study) | Low-Medium | McLean-Pontiff generic band as placeholder | First purged/embargoed India backtest |
| GFCF/GDP percentile rank (capex-cycle proxy) | Percentile rank; historical range ~28%–35% | I3 | C | Low | Same | Same; also a structural GDP-denominator revision |
| Real-estate cycle (RBI HPI / RESIDEX) | Percentile rank of YoY HPI growth; n≈1 domestic full leg | I5; cross-country promotion via F7 | C domestic / B via ≥10-country-analogue clause | Low-Medium | Generic haircut band pending India study | 2nd domestic completed leg; India-specific replication of F7 |
| FII flow *momentum* (trailing net flow sign/level) | **Do not use directionally** — reduce-only at most | I6, F8 | C (established decaying pattern) | Low | Full McLean-Pontiff 26%/58% haircut, plus DII-growth-driven further discount (I7a) | A rolling-window re-estimate showing the relationship has NOT weakened |
| FII ownership-level / positioning-extreme percentile (free-float-scaled) | Percentile rank of cumulative FII holding vs. own trailing history; scale by free float (I7b) | I7 | C (no India quantified study) | Low | Reduce-only until validated | First purged/embargoed India backtest |
| Election-window volatility scalar | Reduce gross/leverage into the ±1–2 month vote window; re-lever conditional on a mandate-clarity classification, not a fixed date offset | I8 | B (timing) / C (any directional claim) | Medium (timing), Low (direction) | Timing itself doesn't decay; never size a directional bet on election outcome | A pre-registered mandate-clarity classification scheme tested out-of-sample |
| Budget-day volatility scalar | Reduce gross into the Budget-day session; use India VIX term-structure, not a fixed-day rule | I9 | B (timing) / C (direction) | Medium / Low | Same logic as election window | A rigorous India event-study of budget-day abnormal returns |
| March/April fiscal-year-end small-cap effect | Hypothesis only — not yet evidenced for India | I9 | C (hypothesis) | Low | N/A — untested | A pre-registered India event-study (analogue to Rozeff-Kinney) |
| Monsoon deviation (% of LPA) | Percentile rank, sector-level only (rural consumption), reduce-only | I10 | C | Low | Weak/unquantified effect; McLean-Pontiff band if ever used directionally | A rigorous India-specific quantified aggregate or sector study |
| Global financial cycle / dollar-VIX state (methodology) | VIX + broad dollar index (FRED) percentile/z-score, factor-model style per F4 | F3, F4, F5, F6 | A (pooled methodology) | Medium-High | Genuine risk premium — not expected to decay | An India-specific factor-loading estimate once constructed |
| Global financial cycle → India transfer coefficient | Not yet estimated for India specifically | Judgment placeholder pending data phase | B (India-actionable) | Low-Medium | Explicit stated placeholder, not literature-derived | First purged/embargoed India-conditioned estimate |
| Oil-shock signal (Kilian-decomposed) | Demand- vs. supply-decomposed oil move, not raw price level | F13, I11 | B (mechanism; India-specific quantified coefficients [VERIFY]) | Medium | Genuine risk factor — CAD/INR/inflation exposure structural, not decaying | An India-specific pass-through re-estimate (post-2022 discounted-Russian-crude regime shift) |
| IPO/issuance-share sentiment cycle | Percentile rank of trailing issuance share / first-day-pop, satellite-sleeve use only | F9–F12, I12 | B (methodology via cross-country analogue, F11) / C (India-specific coefficient) | Low-Medium | McLean-Pontiff generic haircut band as default prior | An India-specific pre-registered quantified study; SEBI's own ASM/GSM flags as a free confirming input |
| ASM/GSM regulatory flag (per-stock) | Binary/graded flag from NSE/BSE, free, real-time | I12 | C (no quantified predictive study; institutional confirmation only) | Low-Medium | Institutional-constraint mechanism, unlikely to decay (regulator keeps redefining criteria) | Any published study of return behavior conditional on ASM/GSM placement |
| Influence cap, calendar bucket (election+budget+monsoon combined) | ≤10–15% of regime-score weight, permission/scheduling use only, not alpha | Reasoned analogy to Workstream 03's block-cap treatment | B (design recommendation) | Medium | Revisit once purged-CV results exist | A validated directional effect size materially above zero |
| Influence cap, monetary/capex/real-estate macro-state bucket | ≤15–20% combined, explicitly coordinated with Workstream 03's credit-cycle cap (shared budget, not additive) | Reasoned analogy | B | Medium | Same | Same |
| Influence cap, global-financial-cycle/oil state bucket | ≤20–25% of the "global/EM risk-state" regime-score bucket (higher than domestic-only buckets given stronger pooled evidence) | Reasoned analogy, per §3 Edge E/F | B | Medium | Same | Same |
| Influence cap, Tier-C satellites (FII-positioning, capex/real-estate, IPO-issuance, monsoon) | Reduce-only; 0% positive-tilt budget; ≤10% combined negative-tilt contribution | CONTRACT §4 Tier-C rule | C by rule | High (rule, not estimate) | N/A — constraint | Promotion to Tier B per-signal on its own merits (≥4 India obs or defended ≥10-cross-country-analogue) |

---

## 5. Evidence-tier recommendations

- **Tier A** exists in this workstream **only at the pooled international level**: the global-
  financial-cycle/capital-flow-wave methodology (F3–F6, dozens of countries, multiple decades,
  easily ≥30 country-episode observations) and the Baker-Wurgler/Ritter issuance-sentiment
  methodology (F9–F12, decades of US/multi-country data). **No India-only estimate in this
  workstream clears Tier A** — every domestic count is either single digits (elections n=8–9,
  monetary cycles n≈4–5, capex/real-estate n≈1–3) or effectively zero for a quantified effect
  (FII-positioning, IPO-issuance-share, monsoon, capex — no India-specific study confidently
  recalled). Recommendation: as in Workstream 03, treat the **methodology** as Tier A where the
  pooled literature genuinely supports it, and the **India-actionable coefficient** as Tier B
  pending domestic (purged/embargoed) estimation.
- **Tier B**: election-cycle timing (n=8–9, or 5 clean full-term cycles — a robust count even
  though the *direction* of any effect is unresolved); budget-day timing (n>>30, annual, decades of
  free data — timing robust, direction/magnitude unresolved); monetary-cycle *timing* (n≈4–5,
  marginal); real-estate and capex cycles **via the cross-country-analogue clause** (F7 for real
  estate cleanly; capex less cleanly — no single clean pooling citation recalled); the global-
  financial-cycle and oil-shock **mechanisms** (strong pooled literature, India transfer coefficient
  pending); the IPO-issuance-cycle **mechanism** (via F11's cross-country replication, with the
  caveat that India was likely not in the original sample).
- **Tier C**: FII flow *momentum* directionally (an established, likely-decayed pattern — reduce-
  only at most, and arguably should not be used at all given the explicit decay logic in §3 Edge C);
  FII ownership-positioning-extremes (no India-specific quantified study yet); monsoon (honestly
  weak/unquantified at index level); the March/April fiscal-year-end small-cap hypothesis (untested
  for India); ASM/GSM-conditional return behavior (no quantified study, institutional-confirmation
  only). All Tier-C items here are **reduce-risk-only** per CONTRACT §4.
- **Observation-count summary (India-only, post-1991 regime)**: election n=8–9 (or 5 full-term);
  monetary cycle n≈4–5 (boundary-ambiguous); budget/tax-year n>>30 (annual); monsoon n>>30 (annual,
  though effect unquantified); capex cycle n≈2–3; real-estate cycle n≈1–2; global-financial-cycle
  "episodes" hitting India n≈5–8 (Taper Tantrum, GFC, Euro crisis, 2015–16 China/oil, COVID, 2022
  Fed-hiking/dollar-surge — irregular, not periodic); oil-shock episodes n≈6–8 (irregular, not
  periodic); FII-flow and IPO-issuance cycles have **no clean periodicity at all** (continuous
  state variables, not discrete countable periods).

---

## 6. Research method for the data phase

1. **Series construction** (on the principal's machine — this environment's egress to RBI, NSDL,
   SEBI, IMD, PPAC, FRED and AMFI endpoints is blocked, per CONTRACT §7 Known Prior #11): pull RBI
   DBIE repo-rate history, OBICUS, sectoral credit deployment; MOSPI IIP capital-goods and GFCF;
   RBI HPI + NHB RESIDEX; NSDL FPI daily/monthly flows; AMFI SIP monthly flows; SEBI shareholding-
   pattern filings (per-stock, quarterly) and ASM/GSM lists; IMD seasonal rainfall % of LPA; PPAC
   crude basket price and import volumes; FRED VIX (`VIXCLS`) and broad dollar index; Kilian's
   public oil-shock-decomposition index; ECI's official election-date calendar; `indiabudget.gov.in`
   budget dates and documents.
2. **Clock-test re-application with real data**: for each candidate, fix the "complete period"
   definition **before** looking at the data (pre-registration, CONTRACT §9) — trough-to-trough for
   monetary/credit-linked cycles, event-to-event for calendar-anchored ones — then count
   non-overlapping completed periods since 1991 (or since each series' free-data start date if
   later). Re-derive the counts in §5 from the actual series rather than from recollection.
3. **Filtering**: apply the Hamilton (2018) regression filter (never HP, per CONTRACT §8) to the
   monetary/capex/real-estate state variables, at horizon bands tied to each candidate's plausible
   full-cycle length (e.g., *h*≈8–16 quarters for the monetary cycle given a ~4–7y typical length,
   consistent with F10/F11 in Workstream 03's own reasoning); estimate `tau_half = ln(0.5)/ln(ρ)`
   from an AR(1) fit to the filtered series over overlapping windows, reporting a confidence
   interval, not a point estimate, exactly as Workstream 03 proposes for the credit cycle.
4. **Global-financial-cycle factor construction**: replicate Miranda-Agrippino & Rey's (F4)
   dynamic-factor approach at reduced scale using free India-relevant series (VIX, dollar index, US
   real rates, India FPI flow, INR, India VIX) to extract a single "global risk state" factor; this
   is a genuinely estimable free-data project and should be prioritized early given the strong
   pooled-literature backing (§5).
5. **Kilian decomposition for oil**: either pull Kilian's maintained public index directly, or
   reconstruct an India-usable demand/supply split from free global shipping/industrial-production
   proxies if his index proves stale/unavailable; never use raw oil price level as the signal.
6. **FII flow re-estimation with a structural-break test**: explicitly test whether the flows-
   returns relationship (I6/F8) has weakened as DII AUM has grown (I7a) via a rolling-window or
   Chow-test structural-break specification, pre-registered before running; report whichever
   direction the data show, including a null result.
7. **Election/budget event studies**: pre-register the exact event window (e.g., t−20 to t+20
   trading days around each of the 8–9 election result dates and each of the ~25–30 budget dates)
   and the exact volatility/return metrics **before** running, to avoid the CONTRACT's own
   hindsight-bias trap; given the tiny n for elections specifically, report confidence intervals
   wide enough to be honest about the limited power, and do not over-fit a "mandate-clarity
   classification" scheme without holding at least 2 elections out of sample.
8. **Stambaugh-bias correction**: apply to any persistent-regressor specification (credit-linked
   state variables, FII-ownership percentile), per CONTRACT §9.
9. **Out-of-sample validation**: R² and AUROC always judged against the historical-mean/base-rate
   benchmark, never in-sample; purged and embargoed cross-validation with embargo scaled to each
   candidate's estimated `tau_half`.
10. **Trial-count discipline and registry entry**: log every filter-horizon grid point, every
    mandate-clarity classification scheme variant, every issuance-share threshold/percentile
    specification tried, in the shared trial registry (CONTRACT §9's deflated-Sharpe requirement);
    every surviving indicator gets a `research/register/` entry with free-source URL, update
    frequency, evidence tier, and influence cap, validated in CI per CONTRACT §10.
11. **Cross-workstream reconciliation** (explicit deliverable, not yet done here): this workstream's
    monetary/capex/real-estate state variables substantially overlap Workstream 03's credit-cycle
    block; its global-financial-cycle/oil state variables may overlap a currency/EM-flows workstream
    if one exists; its election/budget/monsoon calendar bucket and IPO-issuance cycle are, to my
    knowledge, unique to this workstream. A single composite-regime-score assembly pass across all
    cycle dossiers must de-duplicate correlated inputs before assigning final budget weights.

---

## 7. Open questions and [VERIFY] items

1. **[VERIFY]** Every citation in §1 marked with a bracketed flag needs a live search pass once
   budget resets — this dossier was written with `WebSearch` fully exhausted (200/200 used by
   earlier workstreams) and `WebFetch` blocked at the egress proxy for every domain tried (NBER,
   Wikipedia, RBI, SEBI). Priority re-verification order: F3/F4 (Rey; Miranda-Agrippino & Rey —
   exact NBER WP number and RES volume/pages), F1 (Santa-Clara & Valkanov exact pp differential),
   F6 (Cerutti-Claessens-Puy exact venue/year), F11 (Baker-Wurgler-Yuan exact country panel).
2. **[VERIFY]** I2's monetary-transmission-lag figures and I11's oil-CAD/CPI sensitivity rule-of-
   thumb are both stated as widely-repeated summary figures rather than pinned to one specific RBI
   working paper — find and cite the actual primary DEPR/RBI working papers before loading into
   `research/register/` above Tier C.
3. **[VERIFY]** I8's exact percentage moves on the four cited election result days (2004 crash, 2009
   rally, 2024 fall) — directionally high-confidence, magnitudes need reconfirmation against
   contemporaneous NSE/BSE bhavcopy.
4. **[VERIFY]** I9's Budget-day and March/April fiscal-year-end effects — no confident India-
   specific academic citation found in recollection; this may be a genuine literature gap (an
   opportunity for a first-of-its-kind pre-registered India study) rather than a verification
   failure — flag for the data-phase team either way.
5. **[VERIFY]** I10's monsoon-equity link — same status as #4: possibly a genuine gap, not just an
   unrecalled citation. Recommend an explicit literature-gap search (not just fact-check) once
   search access returns.
6. **[VERIFY]** I12's exact SEBI SME-IPO tightening circular date/reference, and the "India among
   largest global IPO markets" ranking claim (year and source).
7. **Open design question**: how should this workstream's monetary/capex/real-estate state
   variables be merged with Workstream 03's credit-cycle block into one non-duplicated regime input?
   This dossier flags the overlap repeatedly (§2 I4/I5, §3 Edge A/B, §6 point 11) but does not
   resolve the merge — that requires a joint pass across dossiers, not a single-workstream decision.
8. **Open design question**: the election-cycle "mandate-clarity classification" proposed in §4 is
   a genuinely new construct (not lifted from a paper) needed to operationalize I8's finding that
   direction depends on surprise-vs-expectation rather than the calendar slot itself — it needs to
   be specified precisely (e.g., seat-count vs. exit-poll-implied seat-count, coalition-dependency
   binary) and pre-registered before the data phase tests it, given only 8–9 total observations ever
   available to validate it against.
9. **Open design question**: this dossier treats the global-financial-cycle/dollar-VIX state
   variable as failing the periodicity clock test but passing on pooled-evidence strength (§3 Edge
   E) — a genuinely unusual combination (strong evidence, no periodicity) worth flagging explicitly
   when the full cross-workstream ladder is assembled, since the CONTRACT's tau_half-ordering logic
   is built around cycles/states with at least loosely estimable persistence, and a "shock-episode"
   state variable like this one may need its own ordering convention (ordered by episode tau_half
   — i.e., how long a given risk-off regime persists once entered, order-of-magnitude 3–9 months
   proposed in §3 — rather than by inter-episode recurrence interval, which is irregular by
   construction).
10. **Open design question (OPEN_QUESTIONS.md linkage)**: Q10 defaults to a capped Tier-B satellite
    sleeve for special situations/IPOs in the aggressive book only — this workstream's F9–F12/I12
    findings directly support using the issuance-share/first-day-pop percentile rank (plus the free
    ASM/GSM regulatory flag) as the **sizing/avoidance-timing overlay** for that satellite sleeve;
    this is proposed here as the natural instantiation of Q10's default, not yet reconciled with
    whatever the special-situations workstream (if separately assigned) independently proposes.
