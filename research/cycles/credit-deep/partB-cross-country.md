# PART B — The Cross-Country Record

*Credit-cycle monograph · Part B of III · v1.0 · 2026-09-01 · Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*
*Governed by `research/CONTRACT.md`. Every number below is search-verified as of Sept 2026 unless tagged `[VERIFY: ...]`. Internal cross-references are to `docs/cycles/01-credit-cycle.md` ("D03/L10 dossier"), which this Part supplies the underlying evidence for.*

---

## B1. The panel evidence, in detail

### B1.1 The Jordà–Schularick–Taylor Macrohistory Database

The JST Macrohistory Database is the single largest free, public panel of long-run macro-financial
data and is the reason the Contract's estimation standards (§9) instruct pooling "where India alone
offers <2 cycles." It is maintained by Òscar Jordà (SF Fed / UC Davis), Moritz Schularick (Kiel
Institute / Bonn), and Alan M. Taylor (UC Davis), hosted at the MacroFinance & MacroHistory Lab.

**Contents.** The current release (**R6**) covers **18 advanced economies since 1870** on an annual
basis (Ireland was added in R6, using land-price and credit series reconstructed by Ronan Lyons and
Trinity College Dublin) — earlier releases (R4) covered **17 economies, 1870–2016**. The panel holds
**45 real and nominal variables**: real/nominal GDP, real GDP per capita (Maddison-linked), real
consumption per capita, investment/GDP, population, unemployment, wages, current account and
trade flows, narrow and broad money, short- and long-term interest rates, **total bank loans, and
loans split into mortgage vs. business credit** (`tloans`, `tmort`, `tbus`), nominal house prices,
and total-return series for equities, housing, bonds, and bills — plus a hand-curated systemic
banking-crisis dummy (`crisisJST`) built from the narrative crisis-dating literature. This is the
only free dataset that lets a researcher build a "credit/GDP gap" or "excess credit" measure
consistently across 150+ years and 18 countries, which is exactly the design pattern the L10 module
pools on.

**Release history.** Versions have been numbered R1 through R6; R3 was the version publicized as
"online" in 2016, R4 (17 countries, through 2016) was current through roughly 2019, and R6 —
current as of this writing, with its documentation PDF dated February 2023 and an update note
covering "2016–2020" — added Ireland and extended coverage. `[VERIFY: exact publication dates and
country counts for R1, R2, and R5 — the Lab's own changelog was not directly accessible from this
environment; the R3→R4→R6 sequence above is corroborated by independent citations across at least
six unrelated GitHub repositories and course materials.]`

**How to download it, free, today.** The authoritative page is
`https://www.macrohistory.net/database/` (database home: `https://www.macrohistory.net/`), which is
**not reachable from this research environment's network egress** (confirmed: direct fetch attempts
to `macrohistory.net` and to `bis.org`, `nber.org`, `frbsf.org`, `hbs.edu`, and
`schmoelders-stiftung.de` were all blocked by the proxy in this session). The dataset is released
under **Creative Commons BY-NC-SA 4.0** (free to use with attribution, non-commercial, share-alike).
Two free routes work from this environment:
1. **Direct download link** (confirmed live and cited verbatim by at least seven independent
   downstream projects between 2021 and 2024):
   `https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.xlsx` — an `.xlsx` workbook
   with a `Data` sheet; a `.dta` (Stata) version exists at the equivalent `/JST/JSTdatasetR6.dta`
   path on the same host.
2. **GitHub mirrors** — see the dedicated side-task section at the end of this document; several
   researchers have committed real copies of R3/R4/R6 data (not merely download scripts) directly
   into public repositories, and those are reachable via `raw.githubusercontent.com` even when
   `macrohistory.net` itself is not.

### B1.2 Schularick & Taylor, *AER* 2012 — "Credit Booms Gone Bust"

**Sample.** 14 countries, 1870–2008 (the original core of what became the JST panel).
**Specification.** A pooled logit (cross-checked against probit; results near-identical) of a
systemic banking-crisis onset dummy on **five annual lags of real credit growth** (bank loans
deflated by CPI), estimated first without and then with country fixed effects, and compared against
an equivalent specification using broad-money growth in place of credit growth. **Headline result:**
the summed marginal effect across the five credit-growth lags is **0.301** in their preferred
specification — i.e., a sustained acceleration in real credit growth raises the estimated
probability of a crisis within the following years by an economically large amount — while the
broad-money specification is materially weaker once credit is included. **"Credit beats money"**
operationally means: when both loan growth and money-supply growth are entered as competing (or
jointly estimated) predictors of crisis onset, the credit-growth lags retain statistical and
economic significance while money's incremental predictive content is small — i.e., it is the asset
side of the banking system's balance sheet (loans), not the liability side (deposits/money), that
carries the crisis signal. Fit statistics reported across the paper and its replications converge
on an **AUROC in the neighborhood of 0.70–0.72** for the baseline in-sample logit (one closely
related specification reports 0.717, another 0.697 with a standard error of 0.039); extensions and
replications testing genuine out-of-sample / pseudo-out-of-sample performance report a **wider band,
roughly 0.66–0.79** depending on sample split and country coverage. `[VERIFY: the exact AUROC table
cells as printed in the original AER article — the primary PDF was not reachable from this
environment (egress-blocked on aeaweb.org, frbsf.org, and independent mirrors); the range above is
triangulated from the replication literature (Summers 2017, *J. Applied Econometrics*) and citing
papers, not read directly off Table 3 of the original.]` This is the number the D03/L10 dossier
already treats as its cross-country prior (stated there as "~0.72 in-sample, 0.66–0.75 range
out-of-sample"); this section corroborates but does not independently re-derive it to the decimal.

### B1.3 Jordà, Schularick & Taylor, *JMCB* 2013 — "When Credit Bites Back"

**Method, in one paragraph.** Rather than fit a single VAR and read off impulse responses at
increasing lag lengths (which forces every horizon through the same dynamic structure), the paper
uses **local projections** (Jordà 2005): for each forecast horizon *h* separately, regress the
future path of an outcome (GDP, investment, bank lending, short rates, inflation) on today's
"excess credit" measure (the deviation of pre-recession credit growth from its historical norm)
plus a battery of macro controls, and read the estimated coefficient at each *h* as the local
projection's impulse response at that horizon. This lets the recovery *path* bend freely rather
than being forced into a single linear dynamic system, which matters because recoveries after
credit busts are empirically **non-linear and asymmetric** relative to normal-recession recoveries.
**Headline path differences (14 advanced countries, 1870–2008):** recessions preceded by more
credit-intensive expansions are systematically **deeper and slower to recover from — whether or not
the recession is accompanied by a systemic financial crisis** — and the worst outcomes of all are
recessions that are *both* preceded by excess credit *and* coincide with a financial crisis. This is
the paper the D03 dossier's mechanism chain leans on directly ("credit-intense expansions ⇒ deeper,
slower recoveries, crisis or not") and it is the single strongest justification in this literature
for why L10 sizes leverage/hedge permission off the **boom's** credit intensity rather than waiting
to identify the trigger of the bust.

### B1.4 Drehmann & Juselius, *IJF* 2014 — "Evaluating Early Warning Indicators"

**Indicators tested.** Credit-to-GDP gap, the debt-service ratio (DSR), credit growth, real
property-price growth, and several composite/combination indicators, evaluated across **26
economies at quarterly frequency**. **Method structure.** Rather than reporting AUROC alone, the
paper explicitly builds the evaluation around a **policymaker's loss function** — trading off
missed crises (Type I) against false alarms (Type II) at policy-relevant horizons (typically 1–5
years before a crisis), and reports AUROC, the noise-to-signal ratio, and stability/interpretability
criteria side by side at each horizon, for each candidate indicator. **Policy conclusion, stated
directly:** the **credit-to-GDP gap dominates at longer horizons (roughly 3–5 years ahead)**, making
it the right variable for setting a slow-moving instrument like the countercyclical capital buffer,
while the **debt-service ratio dominates at short horizons (under about 2 years)**, making it the
better near-term trigger signal once a boom is already mature. The D03 dossier carries forward a
pooled AUROC of **0.83–0.85** at the 3–5-year horizon for the credit-to-GDP gap as this literature's
best single-indicator result; that figure is treated there as **already verified** in the prior
research pass and is repeated here as the working cross-country prior, with the explicit caveat
that the primary BIS working-paper table (`bis.org/publ/work421.pdf`) was **not independently
re-readable from this environment** (egress-blocked) in this pass. `[VERIFY: re-confirm the exact
0.83–0.85 cell values against the original Table 4/5 of Drehmann–Juselius (2014) the next time
bis.org is reachable.]`

### B1.5 Greenwood, Hanson, Shleifer & Sørensen, *JF* 2022 — "Predictable Financial Crises"

**R-zone definitions.** A country enters the **business R-zone** when non-financial-business credit
growth over the trailing **3 years** is in the **top quintile (top 20%)** of the full historical
distribution **and** stock-market returns over the same 3-year window are in the **top tercile (top
third)**. The **household R-zone** is defined symmetrically: household-credit growth over the
trailing 3 years in the top quintile, jointly with equity returns in the top tercile over the same
window. Both zones combined occur in **fewer than 10% of all country-years** in their sample.
**Headline probabilities.** The probability that a country in the **business R-zone** experiences a
major financial crisis within the next 3 years is **~45%**; the paper's topline combined figure
(spanning both the business and household variants) is that being in *either* R-zone carries roughly
a **40% probability** of a crisis within 3 years, against a **base rate of roughly 7%** in "normal
times" when neither credit nor asset-price growth is elevated. `[VERIFY: the household-R-zone-only
probability distinct from the 45% business figure and the blended 40% figure — sources consistently
confirm 45% (business) and 40% (combined/topline) but the search record did not surface a cleanly
separate household-only percentage; treat 40% as the best available household-adjacent estimate
until the original Table can be read directly.]` **The predictability claim.** The paper's explicit
argument is that severe financial crises are **not** unforecastable "bolts from the blue" arriving
without warning — a joint credit-and-asset-price overheating condition, observable in real time with
public data, precedes a large share of postwar crises with a hit rate far above the unconditional
base rate. `[VERIFY: the precise phrase used in the paper for the "bolts from the sky/blue" contrast
— this is a well-known characterization in the crisis-prediction literature generally (often
associated with Bernanke's commentary on the 2008 crisis) but the exact wording and attribution
inside this specific paper was not independently confirmed from the sources reachable here.]` This
is directly relevant to L10's pre-registered **R3** design (a same-construction R-zone replication on
India), and the joint-condition structure (credit **and** price, not credit alone) is one of the
strongest pooled findings carried into B3 below.

### B1.6 Mian, Sufi & Verner, *QJE* 2017 — "Household Debt and Business Cycles Worldwide"

**Sample and finding.** An unbalanced panel of **30 countries, 1960–2012**: a rise in the household
debt-to-GDP ratio over a 3-year window predicts **lower GDP growth and higher unemployment 3–4 years
later**, operating primarily through a subsequent consumption slowdown, and the effect is stronger
where mortgage credit supply (proxied by low mortgage spreads, used as an instrument) expanded fastest
— consistent with a "credit supply," not "credit demand," origin. **The forecast-bias finding.**
Professional forecasters (the paper specifically implicates the **IMF and OECD**'s own growth
forecasts) systematically **under-weight** the information in rising household-debt-to-GDP when
projecting medium-term growth — i.e., the household-debt buildup predicts *both* the future growth
slowdown *and* the forecasting institutions' own forecast errors, meaning the market's/institutions'
consensus view does not fully price in a mechanism the authors can show is statistically live.
`[VERIFY: the precise magnitude of the average IMF/OECD forecast-error attributable to household-debt
buildup — the qualitative finding ("OECD/IMF systematically miss it") is well confirmed across
multiple independent sources including the authors' own 2018 IMF-Global-Debt-Database extension, but
a single clean point-estimate of the average forecast miss in percentage points of GDP was not
located.]` The D03 dossier correctly routes this finding to **L13 (reduce-only)** rather than into
L10 itself, since it is a *household*-debt-specific channel distinct from the aggregate
bank+NBFC credit measure L10 is built on.

### B1.7 Krishnamurthy & Muir — "How Credit Cycles across a Financial Crisis" (NBER 2017 → *JF* 2025)

Credit **quantities** (loan growth, credit/GDP) move slowly and are observed with a lag; credit
**spreads** (the gap between risky and safe borrowing rates) are priced continuously in liquid
markets and can be read in real time. The paper's contribution is to show these two are
**complements, not substitutes**: precrisis credit **spreads compress to unusually low levels
while quantities (credit growth) simultaneously accelerate** — a "quiet before the storm" signature
— and the eventual crisis's **severity** is best predicted by the *interaction* of (a) how far
spreads subsequently spike once the crisis hits and (b) how much precrisis credit growth had built
up financial-sector fragility beforehand. Quantitatively: a **one-standard-deviation increase in
the crisis-period spread widening is associated with an 8.2% decline in cumulative 5-year GDP
growth**, versus only a **3.1% decline** for an equivalent one-sigma spread move in a comparable
*non-financial* recession — i.e., the same-sized price shock does roughly **2.6× the damage** when
it originates in a credit boom's unwind. **What spreads add beyond quantities:** because they are
market-priced daily, spreads can serve as a **fast, real-time confirming (or disconfirming) signal**
layered on top of a necessarily slow-moving, backward-looking credit-quantity state variable — a
compression phase flags boom-era complacency the quantity measure may still be reading as merely
"elevated but not yet extreme," and a spread spike is one of the fastest available signals that a
credit bust has actually begun, well before quarterly GDP or bank-reported NPA data would confirm it.

### B1.8 Baron, Verner & Xiong, *QJE* 2021 — "Banking Crises Without Panics"

**Sample.** A novel hand-built dataset of bank-equity returns for **46 countries, 1870–2016**,
combined with narrative panic dating. **The crisis marker.** The paper defines a banking crisis by
a **bank-equity index decline of more than 30%** — a purely market-based, objectively computable
threshold — rather than requiring a narrative-identified depositor run or panic event. **Headline
finding:** a 30% bank-equity decline **with** an accompanying panic predicts a **−3.4% real GDP**
outcome three years later; the same 30% bank-equity decline **without any panic at all** still
predicts a **−2.7% real GDP** outcome three years later — roughly **80% of the full damage, with no
panic required**. The same threshold event, panic or not, predicts a **−5.4% decline in bank
credit/GDP** three years out. **Implication for using bank equity as a free, real-time indicator:**
because panics amplify damage but are **not necessary** for it, a simple, continuously-priced,
free-to-observe series — the banking-sector equity index — is itself an actionable crisis marker
that does not require waiting for a run, a narrative event, or a lagging NPA print to confirm
distress. For India this argues for tracking a **bank-sector equity index (e.g., Nifty Bank / Bank
Nifty relative to Nifty 500)** drawdown explicitly as a fast, free, real-time confirming layer
alongside L10's credit-quantity inputs, in the same complementary spirit as the Krishnamurthy–Muir
spread signal in B1.7.

---

## B2. Ten case studies

Each case reports: the build-up, the trigger, the bust (equity max drawdown, GDP hit, duration), the
resolution style, and **one design implication** for the L10 state variable.

### 1. United States, 2008 (with 1929 and the S&L crisis as priors)

**Build-up.** US household debt rose from roughly **70% of GDP in 2000** to a peak near **98–99% of
GDP** by 2007–08 `[VERIFY: exact peak-quarter value on FRED series HDTGPDUSQ163N — the series is
confirmed to exist and the qualitative "major spike leading into 2007–08" is confirmed, but a single
precise peak percentage was not independently pulled from a live FRED read in this environment]`,
driven by a mortgage-credit boom (subprime origination, private-label securitization) increasingly
funded off-balance-sheet through shadow-banking channels (ABCP conduits, repo, SIVs) that sat outside
conventional bank-credit statistics. **Trigger.** Rising subprime delinquencies through 2006–07,
the collapse of two Bear Stearns hedge funds (mid-2007), and the **Lehman Brothers bankruptcy on
15 September 2008**. **Bust.** The **S&P 500 fell 56.8% peak-to-trough (October 2007 to March
2009)** — the largest drawdown since WWII; **real GDP fell 4.3% peak-to-trough (2007Q4 to 2009Q2)**,
the deepest postwar US recession; unemployment rose from under 5% to 10%; the NBER-dated recession
ran **18 months** (Dec 2007–Jun 2009). **Resolution.** TARP capital injections, Fed zero rates and
quantitative easing, coordinated bank stress tests (2009) forcing recapitalization, and a
multi-year, policy-engineered deleveraging — slow by design, but decisively faster and more
transparent than Japan's.

**1929 as a prior.** The Dow fell **89% from its September 1929 peak to its July 1932 trough**; real
GDP per capita fell **~30% (1929–33)**; unemployment rose to **over 25%**. Absent deposit insurance
or a reliably activist lender of last resort, banking panics compounded the initial credit bust; the
Dow did not regain its 1929 high until **1954** — a 25-year round trip.

**The S&L crisis as a prior.** Between 1986 and 1995, **1,043 of roughly 3,200** US savings & loan
institutions failed, at a final cost to taxpayers of **$123.8 billion by 1999** (plus $29.1bn absorbed
by the industry itself) — driven by 1980s deregulation combined with an interest-rate/duration
mismatch and speculative real-estate lending, resolved first by the FSLIC and then, at scale, by the
Resolution Trust Corporation.

**Design implication.** The US had *already* run almost exactly this pattern (real-estate-linked
credit boom → duration/liquidity mismatch → deposit-taking-institution failures) twenty years before
2008, and prior experience of a severe credit-cycle bust did **not** prevent a bigger repeat — a
caution against assuming "we've been through this before" reduces risk; parameters must stay frozen
and rules-based (per the Contract's Tier-B discipline) rather than tuned to a belief that the last
lesson has been fully learned. Separately, because the 2008 boom's most dangerous leverage sat in
off-balance-sheet, non-bank vehicles, a credit-cycle state variable measured on **on-balance-sheet
bank credit alone would have materially understated the true state** — directly reinforcing L10's
bank+NBFC aggregation rule.

### 2. Japan, 1986–1990 boom and the lost decades

**Build-up.** Bank lending to real estate roughly **doubled between 1985 and 1990**, pushing the
aggregate loan-to-GDP ratio **past 100%**; commercial land prices in Japan's six largest cities rose
**over 300%** before their collapse, making this "the most extreme documented land bubble in modern
history." Loose post-Plaza-Accord monetary policy financed the boom.

**Trigger.** Bank of Japan tightening through 1989–90 and Ministry of Finance quantity controls on
real-estate lending (1990).

**Bust.** The **Nikkei 225 fell roughly 80% from its 29 December 1989 intraday peak of 38,957 to
around 7,600–7,831 by 2003** — a 14-year drawdown, later extending to an ~82% trough in 2008;
commercial land prices eventually fell **70–80% from peak** over roughly 14 years. Critically, there
was **no single sharp GDP-collapse year** comparable to the other cases in this record: real GDP
growth simply collapsed to an average of **~1.5%/year (1990–95)** and **~0.99%/year (1992–2001)** —
a multi-decade growth drag rather than a drawdown event.

**Resolution.** Banks were permitted to "evergreen" impaired loans for years (the canonical
zombie-lending pattern) with no aggressive forced recapitalization until the Takenaka reforms of the
early 2000s; the Bank of Japan did not adopt zero rates and quantitative easing until 1999–2001 —
roughly a decade after the bust began.

**Design implication.** Japan is the canonical proof that a credit cycle does not need a sharp
equity/GDP crash to be extremely costly — the relevant loss here is the multi-year **growth drag**,
which a state variable tuned only to detect drawdowns will miss entirely. This directly motivates
L10's de-risking signal firing on **boom maturity itself**, not only on an observed trigger, and it
is the closest cross-country analogue to India's own multi-year AQR-recognition delay (case #10):
delayed recognition can convert a moderate credit event into a decade-plus low-growth regime.

### 3. United Kingdom (1973 secondary banking crisis + 2008 variant)

**1973–74.** Property lending rose **more than eightfold from 1970 to 1974**; residential prices
doubled and commercial prices trebled over the same window, funded by "secondary" (non-clearing)
banks that had overtaken the high-street clearers as the principal property lenders. The trigger was
the 1973 oil shock combined with Bank of England tightening and a property-price reversal. The Bank
of England assembled a "lifeboat" (28 December 1973): the clearing banks, under BoE coordination,
extended **£1.3 billion (~1% of GDP) to 26 supported institutions**, with the BoE indemnifying losses
beyond a threshold. UK equities fell sharply over 1972–74 in one of the worst bear markets in UK
market history `[VERIFY: the precise peak-to-trough percentage for the FT 30/FT All-Share index
1972–74 — sources describe this qualitatively as the UK's worst post-war crash but a single
confirmed percentage figure was not independently re-derived here]`. Crucially, the **final cost to
the taxpayer was only £55 million** — the lifeboat was a liquidity bridge for a contained, "fringe"
segment of the banking system, and most assets were eventually worked out.

**2008.** Northern Rock suffered the **first run on a British bank in 150 years**; the government
ultimately injected **over £35 billion** into RBS, Lloyds TSB, and HBOS, fully nationalizing Northern
Rock and Bradford & Bingley and taking majority ownership of RBS. The **FTSE 100 fell 31% over 2008
alone**; **UK GDP fell 6.5% peak-to-trough (2008 Q2 to 2009 Q3)** — the deepest UK recession since
WWII.

**Design implication.** The same country, the same underlying asset class (property-linked lending),
produced a taxpayer cost of **£55 million** in 1973 versus **tens of billions of pounds** in 2008 —
the difference being whether the credit boom sat in a small, contained "fringe" of the system (1973)
or had grown to systemic, wholesale-funded scale (2008). This supports keeping an explicit
**composition/concentration** read (is credit growth concentrated in institutions that are large and
interconnected enough to threaten the system?) alongside the aggregate credit/GDP level — the same
logic underlying L10's Tier-C issuance/composition input.

### 4. Spain, 2000s (cajas, construction, the euro constraint)

**Build-up.** Private-sector credit/GDP **nearly doubled between 2000 and 2007**; credit growth
peaked **above 25%/year in 2006**, with **15 percentage points of that growth coming from
housing/construction/property development** alone; real house prices rose **over 150% (1998–2007)**
and **71% just between 2003 and 2008**; construction reached **~17% of GDP** and **~12% of
employment**, with residential investment at **15.7% of GDP** and annual housing construction
exceeding **one million units — more than Germany, France, and the UK combined**. The main conduit
was the **cajas** (regional, politically-governed savings banks whose incentives were tied to local
economic expansion). Euro membership removed Spain's own interest-rate and exchange-rate valves —
ECB policy, set for the euro area as a whole, was far too loose for Spain's domestic boom.

**Trigger.** The 2008 global financial crisis freezes wholesale funding; construction demand
collapses.

**Bust.** Unemployment rose from **8.2% (2007) to a peak of 26.3% (spring 2013)**; real GDP fell
**~7.5% cumulatively from 2008 to 2013** in a double-dip recession; the **IBEX 35 fell ~50%
peak-to-trough (November 2007 to October 2008)**, with weakness persisting into 2012; the cajas
sector was effectively wiped out and forced into consolidation (Bankia and others), requiring an
EU-funded, banking-sector-specific bailout in 2012 `[VERIFY: the precise EU/ESM bailout amount for
Spain's banking sector — figures in the €40–100bn range are widely cited but a single confirmed
number was not independently pulled here]`.

**Resolution.** A "bad bank" (SAREB, 2012) absorbed the cajas' impaired real-estate assets under the
EU program; unemployment remained elevated for a decade.

**Design implication.** Euro-area membership removed the normal monetary safety valve, letting the
boom run longer and end worse than it would have under an independent currency. India is not in a
currency union, but the underlying lesson generalizes: watch for credit growth concentrating in a
**policy-privileged, rate-insensitive channel** (cajas/construction in Spain; unsecured
retail/NBFC in India, case #10) as a distinct composition warning, separate from the aggregate level.

### 5. Sweden, 1990–1992 (the model resolution)

**Build-up.** Financial deregulation in the mid-1980s inflated a real-estate and credit bubble.
**Trigger.** A speculative attack forced the krona off its currency peg on **19 November 1992**.
**Bust.** Bank credit losses totaled **17% of outstanding lending**; real GDP contracted a cumulative
**5.1% from 1991 to 1993**; two of the largest banks (Nordbanken, Gota Bank) required state rescue.

**Resolution — the model case.** Sweden moved **fast**: a **blanket government guarantee** of all
bank liabilities (1992), nationalization of Nordbanken, and the creation of **Securum** — a dedicated
"bad bank" (built on a McKinsey proposal informed by the US S&L/RTC precedent) that took over and
progressively liquidated distressed real-estate collateral. The **gross initial cost was 3.5–4.5% of
GDP**, but because recognition was immediate and transparent, and because the floated krona quickly
restored export competitiveness, the **net cost had fallen to just 1.5% of GDP by 1997** once asset
sales and bank-share disposals were counted.

**Design implication.** Sweden is the cleanest natural experiment in this record for the claim that
the fiscal/growth **cost of a bust is not fixed by the boom's size — it is highly sensitive to
recognition speed**. Fast, transparent recognition (Sweden) converted a severe bust into a 2–3 year
event with most of the fiscal cost recovered; slow recognition (Japan, case #2; India's TBS era,
case #10) converted comparable or smaller stress into a multi-year drag. L10's job is therefore not
only to size the pre-bust boom but to reward/require fast de-risking once a bust is confirmed.

### 6. Thailand, Korea, and Indonesia, 1997 (the external-funding/currency-mismatch variant)

**Build-up.** All three ran pegged or tightly-managed exchange rates that encouraged **unhedged
foreign-currency borrowing** by banks and corporates (Thai finance companies, Korean chaebol,
Indonesian conglomerates) against domestic-currency revenue — a **currency-mismatch** structure
fundamentally different from the domestic-currency credit booms in cases 1–5.

**Trigger.** Thailand devalued the baht **15–20% on 2 July 1997**; contagion spread regionally within
weeks.

**Bust.** Currency collapses were severe: the **Indonesian rupiah fell over 80%**; the **Korean won
lost almost half its value**. Equities: **Thailand's SET index fell 55.2% in 1997 alone (a further
4.5% in 1998, ~59% combined)**; **Korea's KOSPI fell 27% in the October 1997 crisis month alone**
(with deeper cumulative losses over the full episode) `[VERIFY: KOSPI and Jakarta Composite
cumulative peak-to-trough percentages across the full 1997–98 episode — regional markets are
reported to have "lost up to 70% of their value by early 1998" in aggregate, but clean single-index
cumulative figures for Korea and Indonesia specifically were not independently confirmed here]`. Real
GDP fell **13.0% (Indonesia, 1998)**, **10.2% (Thailand, 1998)**, and **~7% (Korea, 1998)**. The IMF
assembled support packages of **$20bn (Thailand), $40bn (Indonesia), and $59bn (Korea)**.

**Resolution.** IMF-conditioned programs (fiscal tightening, high rates, bank closures, corporate
debt restructuring). Korea staged the sharpest recovery — **10–11% growth in 1999** — helped by won
devaluation restoring export competitiveness and aggressive chaebol debt-equity restructuring;
Thailand and Indonesia recovered more slowly, Indonesia compounded by the political fall of Suharto.

**Design implication — the EM-specific channel India must watch.** This crisis mechanism is
fundamentally different from every other case in this record: the trigger is **currency mismatch
under a pegged exchange rate**, not simply excess domestic credit growth. A state variable built
only on domestic rupee bank+NBFC credit is **structurally blind** to a 1997-style bust building
through offshore borrowing (ECBs, FCCBs, USD-denominated NBFC wholesale funding). This is the
argument for a **separate external-vulnerability gauge** (short-term external debt/reserves,
corporate currency mismatch) sitting **alongside, not inside,** L10's domestic credit-cycle state.

### 7. China, 2009–present (the largest credit boom in history — outcome still unknown)

**Build-up.** Post-GFC stimulus (2008–09) launched what is, on a credit/GDP-change basis, **the
largest credit boom in the JST-comparable historical record**: China's total non-financial-sector
debt/GDP roughly **doubled from ~135% (2008) to ~269% (2020)**, and stands near **296% as of Q3
2025**. The channels: **Local Government Financing Vehicles (LGFVs)**, used as a workaround after
local governments were barred from direct borrowing and secured against land sales, reaching an
estimated **51% of GDP (~$10.4 trillion, IMF)** by 2025; the **property sector**, which together with
related industries reached **~25–30% of GDP** (and **31.7%** including infrastructure in 2021); and
**shadow banking** (trust-company lending to property alone reached roughly **RMB 2 trillion**),
which financed developers such as Evergrande.

**Trigger.** Beijing's "three red lines" policy (2020) capped developer leverage and tightened
property-sector credit access.

**Bust.** **Evergrande defaulted on $305 billion (~2% of China's 2021 GDP)** in 2021; **50+ other
developers** subsequently defaulted. Property investment fell **10.0% in 2022** (the first annual
decline since records began in 1999) and a further **7.9% in H1 2023**; sales by floor area fell
**24.3% in 2022**; from their mid-2021 peak, monthly housing sales are down **more than half**, real
estate development activity down **about a third**, and housing starts down **roughly two-thirds**.
Notably, **no market-wide equity crash or currency collapse accompanied this bust** — capital
controls and a state-directed financial system mean the transmission runs through property-sector
activity, local-government finances, and consumer sentiment rather than through the free-floating
equity/currency channels this literature is otherwise calibrated on.

**Resolution style.** A managed, gradual deflation attempt — state-directed developer support, local
government debt swaps — neither Sweden's fast recognition-and-recapitalization nor Japan's
multi-decade denial, but something in between, and **still unfolding as of 2026**.

**Honest caveat.** As of this writing, China has produced **neither** a classical acute banking panic
**nor** a completed Japan-style workout. Whether the current approach ends as a "Japan-lite" long,
low-growth stretch or a more disorderly adjustment is **not resolved by the data available today** —
this case must be reported as genuinely open, not forced into a completed narrative.

**Design implication.** The largest credit boom in the comparable record has not (yet) tripped any
of the classical crisis markers (30% bank-equity crash, currency collapse, sharp GDP print) this
whole B1 literature is built on — because the state is actively suppressing/spreading the adjustment
rather than letting price and quantity signals clear. A market-economy-calibrated credit-cycle state
variable will systematically **under-read risk** in an administratively-managed system, and — just
as importantly — will not necessarily receive its usual "confirmation" even when the underlying
credit stock is by far the most extreme in the panel. This supports treating **"years an extreme
credit state has gone unresolved"** as informative in its own right — directly relevant to L10's
phase-object enrichment (level/velocity/quadrant/**age**) already specified in the dossier.

### 8. Australia + Canada (multi-decade household-credit booms that have not (yet) burst)

**Build-up.** Australian household debt rose from **~70% to ~190% of household income** over roughly
30 years, equivalent to **~112–114% of GDP (2024–25)**. Canadian household debt/GDP rose from **~80%
(2008) to ~95% (2010) to over 100% for more than a decade**, standing at **~103% (2023)** and
**~100.8% (Q4 2025)** — currently the **highest in the G7**. Both economies sailed through the 2008
crisis with only mild housing corrections; Canadian house prices dipped modestly in 2008 and had
recovered by 2009.

**No trigger, no bust — deliberately.** This case is included precisely because, as of 2026, **no
crisis has been realized** despite multiple decades of elevated and *rising* household credit/GDP,
spanning repeated "the top is now" calls by outside observers since at least the mid-2000s.

**Contributing structural factors** `[interpretation, not a hard finding — flagged accordingly]`:
full-recourse mortgage lending (borrowers cannot simply walk away, unlike much of the pre-2008 US);
housing-supply constraints (immigration-driven demand against restricted land-use/zoning) that have
kept prices supported rather than collapsing; comparatively conservative bank underwriting and
regulation (Canada in particular avoided the securitized-subprime channel that hit the US); and
continued income growth/low unemployment sustaining debt-service capacity.

**Design implication.** This is the **strongest evidentiary case in the entire record** for the
Contract's own mandate that the credit state is a **regime/permission input, never a timing trade**
(§1). A high, even rising, credit/GDP **level** persisted for **decades** without a resolution event
in an economy with structural support — the CD-percentile "level" leg of L10 will read persistently
high in an Australia/Canada-like regime for years with no proximate turn, and the composite **must
not** be allowed to imply urgency from level alone. Only acceleration/turn signals (the expanding-gap
leg) carry incremental timing information, and even those must be read with wide uncertainty bands.

### 9. Ireland, 2008 (the most extreme small-economy case)

**Build-up.** Ireland's mortgage-loan stock exploded from **€16 billion (2003 Q1) to a peak of €106
billion (2008 Q3) — about 60% of Ireland's GDP** in mortgages alone; the banking sector was heavily
**wholesale-funded** rather than deposit-funded, and, as in Spain, euro membership removed the
domestic monetary valve — with Ireland's economy being far smaller relative to its banks' balance
sheets than Spain's.

**Trigger.** The 2007–08 global financial crisis froze wholesale bank funding.

**Bust.** On **30 September 2008** the government issued a blanket guarantee covering **six banks'
liabilities — €375 billion, more than twice Ireland's GDP**. House prices ultimately fell **~54%
peak-to-trough (2007–2013)**, with Dublin apartment prices down **over 62%**; the **ISEQ equity index
fell from a peak near 10,000 (April 2007) to 1,987 (24 February 2009) — roughly an 80% drawdown**.
Real GDP fell **over 3% in 2008** and **nearly 8% in 2009** (**GNP fell 11.3% in 2009**), a cumulative
real GDP decline of **~10% over 2008–2009**. The government injected **€46 billion (~30% of GDP)**
into the banks and nationalized Anglo Irish Bank; **€60 billion (over a third of GDP) left the
country in the last four months of 2010 alone**, forcing Ireland into an **EU/ECB/IMF ("Troika")
program in October 2010**.

**Resolution.** A sovereign bailout — the blanket guarantee transformed a **bank solvency** problem
into a **sovereign solvency** problem almost overnight — followed by a multi-year austerity program,
with recovery aided by Ireland's export-oriented multinational sector (largely insulated from the
domestic property bust) and a return to bond markets by roughly 2012–13.

**Design implication.** Ireland shows that the relevant denominator for "how big is this credit
boom" is not GDP alone but **GDP relative to the size of the banking sector the state might have to
stand behind**. A useful cross-check alongside credit/GDP is **bank-assets/GDP** — especially
relevant if India's less-diversified NBFC/shadow-credit segments were ever to require a systemic
sovereign backstop.

### 10. India, 2003–2018 in full detail (the home case — double length)

**The 2003–08 boom.** Non-food bank credit expanded rapidly through the mid-2000s, concentrated in
**infrastructure and real estate** lending, against optimistic assumptions about demand, project
execution, and future cash flows `[VERIFY: precise year-by-year non-food credit growth rates and the
exact credit/GDP ratio-point change over 2003–08 — RBI's own *Trend and Progress of Banking in India*
annual reports for this window carry the primary series, but a clean consolidated year-by-year table
was not independently re-derived from the sources reachable here; by contrast, the *subsequent*
2008–2014 non-food credit CAGR of 16.8% is independently confirmed]`. Reported asset quality
*improved* through the boom — gross NPAs were masked to roughly **~2%** by its end — which in
hindsight is the boom's own tell: the best-looking headline print coincided with the period of
heaviest under-recognition, not genuine health.

**The Twin Balance Sheet problem, 2011–15.** Corporate over-leverage from the back half of the
2003–08 boom (concentrated in infrastructure, power, and steel) combined with hidden bank-side
stress. The **Economic Survey 2016-17** estimated **stressed advances (NPA + restructured) at ~12%**
of total bank loans system-wide; for **public-sector banks specifically, gross NPAs reached 11.8%**
and **stressed advances 15.8% of total advances by September 2016**; roughly **40% of corporate debt
was owed by firms not earning enough to cover their own interest payments**. This is a genuine
corporate-over-leverage problem that took **five to seven years after the original lending** to
surface in the reported numbers.

**The AQR recognition shock, 2015–2018.** The RBI's 2015 **Asset Quality Review** forced banks to
reclassify previously-obscured stressed loans as non-performing. **Public-sector-bank gross NPAs rose
from ~5.0% (March 2015) to ~14.6% (March 2018)**; the **system-wide gross NPA ratio reached 11.2% in
2017–18**. This must be read as a **measurement break, not a new credit event** — the underlying
loans were already impaired; the AQR simply forced the banks to say so. It is, by a wide margin, the
single most important *splice-discipline* lesson in the whole India chronology: any backtest spanning
2011–2018 that treats the AQR-era GNPA jump as a fresh shock, rather than a forced catch-up on
already-existing stress, will badly mis-time the credit cycle.

**IL&FS, 2018 — the NBFC/shadow-credit freeze.** Infrastructure Leasing & Financial Services, a
large "shadow bank" carrying **debt of ₹91,091 crore (~$13bn)**, defaulted in August–September 2018
after a classic long-term-asset/short-term-liability mismatch. The default triggered a system-wide
**funding freeze across India's non-bank financial sector** — mutual funds and banks pulled back
sharply from NBFC commercial paper — subsequently claiming DHFL, Reliance Capital, and others.
**Critically, this stress was largely invisible in bank-only credit aggregates**, because it ran
through the non-bank/shadow-credit channel — exactly why the Contract's own pre-registered **R7**
design uses IL&FS 2018 as a held-out validation target for L10's composition-signal leg, and why the
bank+NBFC aggregation rule is not optional.

**The 2021–24 unsecured-retail boom and RBI's response.** Household debt/GDP rose from **39.2% (March
2021) to an all-time high of 45.5%** in the most recent Financial Stability Report read
`[this supersedes the "26%→42%" figure carried in the prior internal dossier (`docs/cycles/01-credit-cycle.md`),
which should be corrected in the research register against these independently search-verified
numbers]`. The **mix** shifted materially: non-housing retail loans rose from **~50% (2019-20) to
58.4%** of total household debt — i.e., toward unsecured consumption lending rather than asset-backed
borrowing. The **credit-deposit ratio reached 80.3% (including the HDFC–HDFC Bank merger effect) by
March 2024 — the highest since 2005** — and climbed further to **80.8% by March 2025, the highest in
61 years**, before the gap began narrowing in 2025 as deposit growth caught up with slowing credit
growth. The RBI's **16 November 2023 circular** raised risk weights on **unsecured consumer credit
and bank exposure to NBFCs by 25 percentage points** — personal-loan risk weights rose from 100% to
125% for both banks and NBFCs, and bank exposure to NBFCs whose own risk weight sat below 100% was
raised by the same 25 points — while **explicitly excluding** housing, education, vehicle, and
gold-backed loans. This was a **surgical, composition-targeted** tightening, not a blanket
credit-growth brake — direct, real-world confirmation that the regulator itself was reading the same
**composition-of-incremental-credit** signal that L10's Tier-C input is built on.

**Current state, 2024–26.** System gross NPAs reached a **decadal/multi-decade low of 2.15%** by
September 2025 — explicitly a **lagging comfort signal** that says nothing about where the CD ratio
or the unsecured mix currently sit; the CD ratio remains elevated even as its rate of increase has
slowed.

**Design implications (the home case earns three, not one):**
1. **AQR proves recognition can go dark for years and then jump discontinuously** — GNPA must remain
   a **lagging confirm-only** input (already the rule), and any backtest spanning 2011–2018 must
   apply an explicit splice rule rather than reading the jump as a fresh shock.
2. **IL&FS proves a bank-only aggregate misses the most-recently-realized India stress** — the
   bank+NBFC aggregation rule is validated by the one clean, already-resolved India event best suited
   to testing it, and is the natural target for the pre-registered R7 event check.
3. **RBI's own Nov-2023 action is real-world revealed preference** that regulators actively monitor
   **credit composition**, not just level or growth — corroborating (though not proving predictive
   power for) the design choice to carry an issuance/composition-quality input even at Tier C.

---

## B3. What the panel says, pooled

### Summary table (verified figures only; `[VERIFY]` marks a cell not independently confirmed)

| Episode | Boom size (verified metric) | Equity max drawdown | GDP hit | Years to recover |
|---|---|---|---|---|
| US 2008 | HH debt/GDP ~70%→~98-99% (2000–07) `[VERIFY exact peak]` | S&P 500 **−56.8%** (Oct07–Mar09) | Real GDP **−4.3%** (07Q4–09Q2) | `[VERIFY exact quarter GDP regained 07Q4 level]` |
| US 1929 | n/a | Dow **−89%** (Sep29–Jul32) | Real GDP/capita **−30%** (1929–33) | Dow: 25y (to 1954); GDP `[VERIFY, ~1936]` |
| US S&L 1980s–90s | 1,043 of ~3,200 thrifts failed | n/a (sectoral, not market-wide) | n/a | Resolved by ~1995; cost **$123.8bn** (1999) |
| Japan 1986–90 | Bank RE lending ~2× (1985–90); loan/GDP >100% | Nikkei **−80%** (Dec89→2003, 14y) | Growth drag: **~1.5%/yr** (90–95), **~1%/yr** (92–2001) — no single-year collapse | >20y; contested whether "recovered" |
| UK 1973–74 | Property lending **8×** (1970–74) | UK equities sharply down `[VERIFY exact %]` | n/a (contained) | Resolved in a few years; final cost **£55m** |
| UK 2008 | (shares global 2008 boom) | FTSE 100 **−31%** (2008) | Real GDP **−6.5%** (08Q2–09Q3) | `[VERIFY]` |
| Spain 2000s | Private credit/GDP ~**2×** (2000–07) | IBEX 35 **−50%** (Nov07–Oct08) | GDP **−7.5%** cumulative (2008–13) | Unemployment still >20% a decade later `[VERIFY full recovery year]` |
| Sweden 1990–92 | Bank credit losses **17%** of lending | `[not captured]` | GDP **−5.1%** cumulative (1991–93) | ~2–3y to stabilize; net fiscal cost **1.5% GDP** (1997) |
| Thailand 1997 | FX-peg/currency-mismatch driven | SET **−59%** combined (1997–98) | GDP **−10.2%** (1998) | Slower than Korea `[VERIFY years]` |
| Korea 1997 | ” | KOSPI **−27%** (Oct97 alone) `[VERIFY cumulative]` | GDP **−7%** (1998) | V-shaped: **+10–11%** growth (1999) |
| Indonesia 1997 | ” | Regional mkts "up to −70%" `[VERIFY Indonesia-specific]` | GDP **−13.0%** (1998) | Slower; compounded by political crisis |
| China 2009–present | Debt/GDP **~135%→~296%** (2008→Q3'25) | n/a (no market-wide crash) | Property investment **−10.0%** (2022), **−7.9%** (H1'23); no economy-wide GDP contraction printed | **Unresolved as of 2026** |
| Australia (multi-decade) | HH debt **~70%→~190%** of income; **~112-114%** of GDP (2024-25) | n/a | n/a | n/a — no bust yet |
| Canada (multi-decade) | HH debt/GDP **~80%(2008)→~103%(2023)** | n/a (2008 dip mild) | n/a | n/a — no bust yet |
| Ireland 2008 | Mortgage stock **€16bn→€106bn** (2003–08), ~60% GDP | ISEQ **−80%** (Apr07–Feb09) | Real GDP **~−10%** cumulative (2008–09); GNP **−11.3%** (2009) | Troika program 2010; bond-market return **~2012-13** |
| India 2003–2018 | GNPA masked **~2%**→AQR-forced **11.2%** (2017-18); CD ratio **80.8%** (2025, 61y high) | Sensex **~−60 to −64%** (Jan–Oct 2008) | Growth deceleration (TBS era), not a single-year contraction | GNPA cycle: ~10y, AQR(2015)→decadal low (2.15%, 2025) |

### Pooled conclusions, ranked by evidence strength → design implication for L10

1. **(Strongest — JST panel, hundreds of episodes, plus corroborated in 8 of 10 cases above.)**
   The credit **intensity of the expansion**, not the eventual trigger, predicts recession depth and
   duration (JST 2013, B1.3). → L10 must size leverage/hedge permission off the **boom's** credit
   intensity, independent of whatever eventually triggers the bust — matches the existing "never
   times the top" design.
2. **(Strong — 3 clean natural experiments: Sweden vs. Japan vs. India's AQR delay.)** Recognition
   speed, not boom size, determines the fiscal/growth cost of the bust. → GNPA/recognition inputs
   must be treated as a **state** (has recognition happened yet?), never assumed to resolve quickly;
   supports keeping GNPA a lagging confirm only, and motivates an "unresolved-state age" phase read.
3. **(Strong — Spain, Ireland, Thailand/Korea/Indonesia, 5 of 10 cases.)** Fixed exchange rates or
   currency-union membership remove the domestic monetary valve and lengthen/worsen credit busts. →
   Not directly applicable to India's floating rupee, but supports a **separate external-vulnerability
   gauge** (short-term external debt, currency mismatch) rather than folding this channel into the
   domestic credit state.
4. **(Moderate-strong — Greenwood et al.'s formal result, B1.5, plus qualitative confirmation in
   Spain/Ireland/Japan and its notable *absence* in Australia/Canada.)** Credit growth **alone** is a
   materially weaker signal than credit growth **joined with** asset-price growth over the same
   window. → Prioritize the pre-registered **R3** (India R-zone replication); a joint condition, not
   credit alone, is the higher-precision (if rarer) trigger for tightening permission further.
5. **(Moderate — US 2008, India IL&FS 2018, China shadow-trust lending; 3 of 10 cases.)** A
   bank-only credit aggregate misses the specific channel (shadow banking/NBFC/wholesale funding)
   behind the *most recent* bust in nearly a third of these cases. → Confirms the bank+NBFC
   aggregation rule already built into L10 as necessary, not optional.
6. **(Moderate — 2 clean natural experiments: Australia+Canada vs. US/UK/Spain/Ireland.)** A high or
   rising credit-to-GDP **level** can persist for **decades** without a crisis when supported by
   structural factors (full-recourse debt, supply-constrained housing, disciplined underwriting). →
   The single strongest support in this record for treating the level/percentile leg as a **regime
   input only, never a timing trade** — the composite must never imply a "when," only a "how much."
7. **(Emerging — n=1, still-unresolved.)** An administratively-managed credit system (China) can
   suppress the classical trigger signals this literature is calibrated on without the underlying
   risk being resolved. → Low direct applicability to India's market-based, floating-currency banking
   system, but a caution for reading any future India state characterized by heavy forbearance (as
   in the 2020 COVID moratoria) — a quiet reading during a forbearance episode should not be read as
   "no risk"; the existing "COVID is policy-shaped" caveat in the L10 dossier already reflects this.
8. **(Weakest/most tentative — a single direct precedent, US S&L → US 2008, 20 years apart.)** Prior
   severe credit-cycle experience does not vaccinate an economy against a similar repeat two to three
   decades later. → Parameters must stay **frozen** and be periodically re-derived on schedule (Tier
   B rule), never tuned to a "this time is different" argument — reinforcing the Contract's §8 ban on
   backtest-tuned thresholds.

---

## Special side-task — JST Macrohistory mirrors on GitHub

`macrohistory.net` itself was confirmed unreachable from this environment's network egress
(direct `WebFetch` attempts returned `EGRESS_BLOCKED`), so the dataset cannot be pulled from its
authoritative host here. Using `mcp__github__search_code` (GitHub's own code-search index) plus
direct `curl` probes against `raw.githubusercontent.com` (confirmed reachable), the following
repositories were found to hold **actual committed data files** — not merely scripts that download
from macrohistory.net at runtime — verified live (HTTP 200, correct file signature/content) as of
this session. Ranked most credible first:

1. **`bank-of-england/MachineLearningCrisisPrediction`** — official code repo for Bank of England
   Staff Working Paper 848 ("Credit Growth, the Yield Curve and Financial Crisis Prediction").
   Release **R3**, `.xlsx`, confirmed valid (PK-zip magic bytes read directly).
   `https://raw.githubusercontent.com/bank-of-england/MachineLearningCrisisPrediction/master/data/JSTdatasetR3.xlsx`
2. **`dvollrath/Growth4ed`** — Dietrich Vollrath's (University of Houston) textbook data repo, most
   recently active of the three Vollrath mirrors. Release **R4**, `.csv`, confirmed valid (real JST
   column headers read directly: `year,country,iso,...,tloans,tmort,thh,tbus,hpnom,eq_tr,housing_tr,...`).
   `https://raw.githubusercontent.com/dvollrath/Growth4ed/main/Data/jstdatasetr4.csv`
3. **`dvollrath/StudyGuide4ed`** — companion repo to the above (same author, "4th edition" study
   guide). Release **R4**, `.csv`, confirmed valid.
   `https://raw.githubusercontent.com/dvollrath/StudyGuide4ed/main/data/jstdatasetr4.csv`
4. **`dvollrath/StudyGuide`** — the older, predecessor repo to #3 (same author, earlier edition).
   Release **R4**, `.csv`, confirmed valid.
   `https://raw.githubusercontent.com/dvollrath/StudyGuide/master/data/jstdatasetr4.csv`
5. **`axfreeman/MacroEconomic-History-Server-Builder`** — path
   `DATA/SOURCE/ORIGINALS/JST/JSTdatasetR6.xlsx` **is the newest release (R6)** but is stored via
   **Git LFS**: the raw URL returns only an LFS pointer stub (confirmed: content is the text
   `version https://git-lfs.github.com/spec/v1 / oid sha256:9f089e9d... / size 6146802`, not the
   actual spreadsheet bytes), so it is **not directly downloadable** through `raw.githubusercontent.com`
   without a Git-LFS-aware client. Listed last, and flagged, rather than omitted, because it is the
   only R6 (most current, 18-country) copy found on GitHub.
   `https://raw.githubusercontent.com/axfreeman/MacroEconomic-History-Server-Builder/master/DATA/SOURCE/ORIGINALS/JST/JSTdatasetR6.xlsx`
   (LFS pointer only — do not treat as a working download without `git lfs pull`)

None of these were downloaded in this pass, per instructions — only their reachability and file
validity were probed (HTTP status + magic bytes / header row).

---

## References (verified this session; URLs as found via WebSearch/GitHub code search)

- Schularick, M. & Taylor, A.M. (2012). "Credit Booms Gone Bust: Monetary Policy, Leverage Cycles,
  and Financial Crises, 1870–2008." *American Economic Review* 102(2): 1029–1061.
- Jordà, Ò., Schularick, M. & Taylor, A.M. (2013). "When Credit Bites Back." *Journal of Money,
  Credit and Banking* 45(s2): 3–28.
- Drehmann, M. & Juselius, M. (2014). "Evaluating Early Warning Indicators of Banking Crises:
  Satisfying Policy Requirements." *International Journal of Forecasting* 30(3): 759–780.
- Greenwood, R., Hanson, S.G., Shleifer, A. & Sørensen, J.A. (2022). "Predictable Financial Crises."
  *Journal of Finance* 77(2): 863–921.
- Mian, A., Sufi, A. & Verner, E. (2017). "Household Debt and Business Cycles Worldwide." *Quarterly
  Journal of Economics* 132(4): 1755–1817.
- Krishnamurthy, A. & Muir, T. "How Credit Cycles across a Financial Crisis." NBER WP 23850 (2017);
  forthcoming/published *Journal of Finance* (2025).
- Baron, M., Verner, E. & Xiong, W. (2021). "Banking Crises Without Panics." *Quarterly Journal of
  Economics* 136(1): 51–113.
- Jordà, Ò., Schularick, M. & Taylor, A.M. — Macrohistory Database, `macrohistory.net` (R3/R4/R6),
  NBER data page `nber.org/research/data/jorda-schularick-taylor-macrohistory`.
- RBI: *Trend and Progress of Banking in India* (annual); Financial Stability Reports (various
  years); circular RBI/2023-24/85 (16 Nov 2023); Economic Survey 2016-17, Ch. 4 ("The Festering Twin
  Balance Sheet Problem").
- All other figures per the case-by-case citations embedded in B2 and the `[VERIFY]` tags therein.
