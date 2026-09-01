# Reserve-Currency / Monetary-Order Transition Deep Dive — Part A & Part G

Part A: Theory — why reserve status exists, persists, and shifts · Part G: Operator psychology ·
v1.0 · 2026-09-01 · Atlas entry 0.2 (`docs/CYCLE_ATLAS.md` line 43; τ½ prior ~80–110y, n≈2–3
ever). Complements, never contradicts, `research/cycles/reserve-deep/cofer-RESULTS.md`
(RC0–RC3: this program's own COFER computation, 1999Q1–2023Q1 — USD share drift **−0.51pp/yr**,
no single challenger [share went mostly to non-traditional currencies, not the euro], no
acceleration visible in FX shares through 2023Q1, gold outside COFER by construction). Also
anchors to `docs/DESIGN.md`'s L15 row (line 248, §4.3's harvest arithmetic) and to dossier
07 §C (Eichengreen's *Exorbitant Privilege*, Dalio's Big Cycle, n≈3 Tier-C narrative). Harvest
scope, stated once and held throughout: enrichment of **L15's composition input — the CB-gold
leg** — Tier C, reduce-only, **zero timing authority**. This file supplies the intellectual
history and verified evidence underneath that leg; it proposes no new numeric parameter and
carries forward, not re-derives, cofer-RESULTS.md's frozen numbers.

---

## PART A — Theory: why reserve status exists, persists, and shifts

### A.1 What reserve status IS operationally — four roles that need not travel together

**(i) Mechanism.** "Reserve currency" collapses four analytically distinct roles: a private
**invoicing currency** (how traded goods are priced), a private **funding currency** (the
denomination of cross-border bank credit and debt securities), an official **anchor currency**
(what a country's exchange-rate regime references, de jure or de facto), and the official
**reserve asset** (the currency composition of central-bank FX reserves — what COFER measures
directly). Gopinath, Boz, Casas, Díez, Gourinchas & Plagborg-Møller's **dominant-currency
paradigm (DCP)** supplies the formal theory for the first role: against the classical
Mundell-Fleming assumption that exporters invoice in their own currency (producer-currency
pricing), the empirical pattern is that a small number of "dominant currencies" — overwhelmingly
the dollar — invoice far more trade than the issuer's own trade share would predict, so
exchange-rate pass-through and trade-volume elasticities are governed by movements in the
dominant currency's bilateral rate, not the two trading partners' own rate: a 1% broad dollar
appreciation predicts a 0.6% decline within a year in trade volume between two *non-US*
countries.

**(ii) The four shares, verified and compared.** FX turnover (vehicle/funding role): the dollar
sat on one side of **89%** of all trades in the BIS's April 2025 Triennial Survey (turnover
sums to 200%; two currency legs per trade) — essentially flat from 88% in 2022, a series high.
Export/trade invoicing: roughly **54%** of global exports are dollar-invoiced against the US's
own ~10% share of world trade — DCP's headline finding, in a number. Official reserve assets:
**57%** of allocated COFER reserves as of late 2025 (Fed 2025-edition report; down from a 72%
peak in 2001) — a separately published, more recent reading than this file's own frozen RC0/RC1
base (71.2%/1999Q1 → 59.0%/2023Q1), consistent in direction but **not** part of the vault
computation and not to be conflated with it. Funding currency: dollar-denominated instruments
account for roughly **half** of all cross-border bank loans and international debt securities
outstanding (BIS banking statistics), several multiples of the US's ~25% world-GDP share —
Bruno & Shin (2015) and McCauley, McGuire & Sushko (2015) document how this channel transmits
US monetary conditions to borrowers with no US counterparty at all. Anchor currency: Ilzetzki,
Reinhart & Rogoff's exchange-rate-regime classification finds the dollar is, "by a wide margin,"
the world's dominant de facto anchor, more widely referenced today than seven decades ago, while
the euro's anchor role has stalled.

**(iii) For L15.** The four-way split is why L15's composition input reads COFER (the
reserve-asset role) paired with WGC/RBI gold, never invoicing-role headlines (a bilateral trade
deal priced in local currency is invoicing-role news, not reserve-asset-role news) — RC2 already
shows the actual reserve-share drift moving to non-traditional currencies and gold, not tracking
invoicing announcements. A genuine transition requires multiple roles to move together and
durably; A.7's indicator hierarchy is organized on exactly this principle.

**(iv) Citations.** Gopinath, Gita; Boz, Emine; Casas, Camila; Díez, Federico J.; Gourinchas,
Pierre-Olivier; Plagborg-Møller, Mikkel (2020), "Dominant Currency Paradigm," *American Economic
Review* 110(3) **[Verified via NBER WP 22943; exact AER page range recalled as 677–719 —
VERIFY]**. BIS (2025), Triennial Central Bank Survey of FX and OTC Derivatives Markets, April
2025 **[Verified]**. Fed (2025), "The International Role of the U.S. Dollar — 2025 Edition"
**[Verified]**. Bruno, Valentina & Shin, Hyun Song (2015), "Cross-Border Banking and Global
Liquidity," *Review of Economic Studies* 82(2) **[Verified existence/mechanism; exact page range
— VERIFY]**. Ilzetzki, Ethan; Reinhart, Carmen M.; Rogoff, Kenneth S., "Exchange Arrangements
Entering the 21st Century" (NBER WP 23134, 2017) and "Rethinking Exchange Rate Regimes" (NBER WP
29347, 2021) **[Verified]**.

---

### A.2 Network effects and why status is sticky

**(i) Mechanism.** Krugman (1980) built the founding formal case for why one currency tends to
dominate: conversion costs fall with the volume of trade already routed through a currency — a
network externality — so liquidity begets liquidity once usage crosses a threshold, a
self-reinforcing equilibrium rather than a continuously fundamentals-tracking outcome.
Matsuyama, Kiyotaki & Matsui's (1993) search-theoretic two-country random-matching model gives
this micro-foundations and, notably, **multiple stable equilibria**: currencies may circulate
only locally, one may circulate internationally (a vehicle-currency equilibrium), or both may —
which obtains depends on relative country size and matching frictions, not a unique prediction,
formalizing reserve status as a coordination/expectations equilibrium rather than a market
outcome that tracks fundamentals continuously.

**(ii) The inertia evidence — and its limit.** If network effects alone governed outcomes,
status should be almost purely path-dependent. Eichengreen, Mehl & Chitu's **"Mars or Mercury?"**
tests this against a rival geopolitical channel using pre-WWI reserve data (separating the two
cleanly, since both today's institutions and today's network effects are absent): they find
**both** matter — a security/military alliance with a currency's issuer raises that currency's
share in the ally's reserves by roughly **30 percentage points**, a "Mars" effect as large as
anything "Mercury" (economic size, credibility) delivers — and their extrapolation to a
hypothetical US geopolitical withdrawal implies long-term US rates could rise by as much as
**80bp** through the reserve-composition channel alone. Stickiness, honestly read, is jointly a
liquidity-network phenomenon and an alliance/security phenomenon — a shift in the latter, not
only relative GDP, can move reserve shares independent of any change in market depth.

**(iii) For L15.** Network-effect stickiness is the formal reason behind the atlas's τ½ prior
(~80–110y, line 43) and the reason RC1's −0.51pp/yr drift is glacial rather than abrupt. Mars/
Mercury is the reason the seat must not treat that stickiness as permanent: an alliance-structure
shock — invisible in COFER shares themselves, which lag — is a plausible channel through which
the multi-decade prior could compress, precisely the risk Part G.2 returns to.

**(iv) Citations.** Krugman, Paul R. (1980), "Vehicle Currencies and the Structure of
International Exchange," *Journal of Money, Credit and Banking* 12(3): 513–526 **[Verified]**.
Matsuyama, Kiminori; Kiyotaki, Nobuhiro; Matsui, Akihiko (1993), "Toward a Theory of
International Currency," *Review of Economic Studies* 60(2): 283–307 **[Verified]**.
Eichengreen, Barry; Mehl, Arnaud; Chitu, Livia, "Mars or Mercury? The Geopolitics of
International Currency Choice," *Economic Policy* 34(98): 315–363 (2019; NBER WP 24145, 2017)
**[Verified]**.

---

### A.3 Exorbitant privilege and its price

**(i) Mechanism.** "Exorbitant privilege" (Valéry Giscard d'Estaing's 1960s coinage) names the
reserve issuer's ability to run persistent external deficits financed by foreigners willingly
holding its liabilities at below-market yields. Gourinchas & Rey's **"From World Banker to World
Venture Capitalist"** formalizes it: the US external balance sheet is asymmetric by
construction — foreign liabilities disproportionately safe, liquid, short-duration (official
reserves, bank deposits); foreign assets disproportionately risky, illiquid, long-duration (FDI,
equity) — the US behaves like a leveraged intermediary, borrowing short-and-safe, lending
long-and-risky, "world banker" through Bretton Woods and increasingly "world venture capitalist"
after.

**(ii) Magnitudes — and the honest counter-evidence.** Gourinchas & Rey's original estimate is
excess US return of **3.32%/year (1973–2004)**; later extensions put it nearer **2.4–2.6%/year**
across adjacent windows (1952–72: ~2.6%; 1973–2016: ~2.4%). This is contested: **Curcuru,
Dvorak & Warnock**'s replication shows the differential is highly sensitive to how unmeasured
valuation adjustments ("other changes") in the international-investment-position data are
treated, and shrinks sharply — in places toward zero — once non-price capital gains are
excluded rather than imputed, an honesty-check structurally identical to this program's own
habit of pairing a headline finding with its best empirical rebuttal (cf. debt-deep's
Mauro-Zhou-vs-Blanchard treatment). **Triffin (1960)** named the price under the gold-anchor
constraint that actually broke Bretton Woods: a reserve issuer must run persistent
deficits/liability growth to supply the world's growing demand for reserve assets — a trajectory
that must eventually strain confidence in convertibility at a fixed price, an inherent tension
between supplying liquidity and keeping the promise credible. **Farhi & Maggiori (2018)** restate
Triffin for a fiat, floating-rate world with no gold anchor: modeling reserve-asset supply/demand
across hegemon-vs-multipolar and abundant-vs-scarce regimes, the same tension resurfaces as a
**fiscal-capacity** constraint — the issuer's ability to keep supplying safe assets the world
wants depends on confidence in its long-run fiscal capacity to service them — and, a
Nurkse-consistent result, a **multipolar** reserve system is generically **less** stable than a
hegemon's, because switching between imperfect substitutes is easier than abandoning a monopoly
and can itself trigger self-fulfilling reserve-composition runs.

**(iii) For L15.** Privilege and price sit on the same axis: the US earns a return subsidy for
supplying the world's reserve asset, but that supply is what eventually strains confidence — the
register in which "the privilege is fraying" claims should be read, and a genuinely unsettled
literature (Curcuru-Dvorak-Warnock), not a fact the seat can lean on in either direction. It
reinforces why L15's composition input stays measurement (COFER/WGC), never a forecast built on
this theory.

**(iv) Citations.** Gourinchas, Pierre-Olivier & Rey, Hélène (2007), "From World Banker to World
Venture Capitalist: US External Adjustment and the Exorbitant Privilege," in R. Clarida (ed.),
*G7 Current Account Imbalances: Sustainability and Adjustment*, University of Chicago Press for
NBER, pp. 11–66 (NBER WP 11563, 2005) **[Verified]**. Curcuru, Stephanie E.; Dvorak, Tomas;
Warnock, Francis E., "Cross-Border Returns Differentials" / "On Returns Differentials," Federal
Reserve Board IFDP **[Verified existence/critique; exact definitive-version pairing — VERIFY]**.
Triffin, Robert (1960), *Gold and the Dollar Crisis: The Future of Convertibility*, Yale
University Press **[Verified]**. Farhi, Emmanuel & Maggiori, Matteo (2018), "A Model of the
International Monetary System," *Quarterly Journal of Economics* 133(1): 295–355 **[Verified]**.

---

### A.4 How transitions actually happened

**(i) The revisionist dating.** Conventional wisdom held sterling dominant until after WWII,
the dollar's rise a post-1945 story tracking US supremacy — a winner-take-all narrative
consistent with pure network lock-in (A.2). **Eichengreen & Flandreau (2009)** overturn this
using newly assembled 1920s reserve-composition data for four countries (Italy, Norway, Spain,
Switzerland): sterling and the dollar ran roughly neck-and-neck through the decade, the dollar's
share overtaking sterling's around **1924** — two decades before the conventional dating, while
the British Empire was still larger than the US by most other measures. **Chitu, Eichengreen &
Mehl (2014)**, using bond-market currency-of-denomination data instead, find the overtaking
somewhat later — around **1929** — driven by New York's bond-market depth outstripping London's;
the two datings bracket "mid-to-late 1920s," and their gap is itself informative: which metric
moves first is an empirical question, not a single clean threshold, the same imprecision this
program insists on for its own indicator hierarchy (A.7).

**(ii) Multipolarity was the norm, not the exception.** The deeper claim is the shape, not just
the date: sterling and the dollar coexisted as roughly co-equal international currencies for
most of the interwar period — multipolarity was the historical norm during a transition, not a
brief interregnum between two monopolies — directly against pure network-lock-in's
one-vehicle-currency prediction, and consistent with Eichengreen's later book-length argument
(*Exorbitant Privilege*, 2011) that several currencies can plausibly coexist as partial reserve
assets simultaneously.

**(iii) What killed each incumbent.** Sterling's four-decade tail (1920s–1972) shows three
recurring mechanisms: **(a) war finance** — both world wars forced large-scale UK borrowing
(chiefly from the US), reversing its net-creditor position and leaving a sterling-balances
overhang authorities spent decades managing down; **(b) current-account exhaustion and episodic
confidence crises** — the September 1949 devaluation and the 14.3% devaluation of 19 November
1967 ($2.80→$2.40) both followed reserve drains capital controls could slow but not reverse, and
the 1956 Suez crisis showed reserve-currency status cuts both ways: the US applied pressure by
threatening to sell its own sterling-bond holdings, forcing a ceasefire Britain's military
position did not otherwise require — "sterling could not be defended without American support";
**(c) capital-control erosion of credibility** — the sterling area required steadily tightening
exchange controls through the 1960s and was effectively ended by the UK's own June 1972
extension of those controls to sterling-area members, formalizing a decade-long leak rather than
a single collapse. The prior transition — guilder to sterling across the 18th century — follows
the same pattern in miniature: Amsterdam's guilder-denominated markets were Europe's deepest
through the Dutch Golden Age, but the costly, lost Fourth Anglo-Dutch War (1780–1784) — fought
partly in retaliation for Dutch support of the American Revolution — combined with earlier
competitiveness erosion to hand London's deeper, war-finance-tested markets an incumbency the
guilder never recovered.

**(iv) For L15.** Three killers recur across both completed transitions — war finance flipping a
net-creditor position, current-account/confidence exhaustion capital controls delay but cannot
reverse, and capital-account credibility erosion — none a single-indicator threshold-crossing
event; each unfolded over one to several decades once underway. This directly grounds the
atlas's τ½ prior and the discipline of reading any single COFER quarter as noise, exactly RC3's
own finding that the 2022 sanctions shock has not (through the vault's window) produced a COFER
regime break.

**(v) Citations.** Eichengreen, Barry & Flandreau, Marc (2009), "The Rise and Fall of the
Dollar, or When Did the Dollar Replace Sterling as the Leading Reserve Currency?" *European
Review of Economic History* 13(3): 377–411 **[Verified]**. Chitu, Livia; Eichengreen, Barry;
Mehl, Arnaud (2014), "When Did the Dollar Overtake Sterling as the Leading International
Currency? Evidence from the Bond Markets," *Journal of Development Economics* 111: 225–245
**[Verified]**. Eichengreen, Barry (2011), *Exorbitant Privilege*, Oxford University Press
**[Verified — dossier 07 finding #6, upgraded from recall-verified this session]**. Sterling
devaluations: September 1949 **[Verified occurrence; exact percentage — VERIFY]**; 19 November
1967, 14.3%, $2.80→$2.40 **[Verified]**. Boughton, James M. (2001/2002), "Northwest of Suez: The
1956 Crisis and the IMF," *IMF Staff Papers* **[Verified]**. Sterling area's effective end, June
1972 exchange-control extension **[Verified]**. Guilder-to-sterling transition and the Fourth
Anglo-Dutch War (1780–1784) **[Verified generally; single canonical academic anchor beyond
general economic-history sourcing — VERIFY]**.

---

### A.5 The challenger scorecard today, honest

**(i) The bar.** A.1–A.2 set the test: deep, open capital markets, credible rule of law, and a
single-issuer safe-asset stock large enough for network effects to converge on. Score each
challenger against it plainly.

**(a) Euro — no fiscal union, fragmented safe asset.** The euro is the only currency with a
COFER share in the dollar's order of magnitude (~20% vs ~57%) and gained ground in specific
niches — it became the leading currency in green/sustainable international bond issuance in
2025, edging out the dollar there for the first time. But the ECB's own 2025/2026 "International
Role of the Euro" reports name the constraint directly: no fiscal union and no single, unified
sovereign safe asset — capital markets remain fragmented along national lines (differing legal
systems, tax codes, insolvency regimes) — so there is no eurozone equivalent of a single, deep
Treasury market for reserve managers to concentrate in. ECB President Lagarde's own framing —
"there is an opening... provided policymakers create the necessary conditions" — is itself an
admission the conditions are not yet met.

**(b) RMB — capital controls; fast plumbing, slow reserve-share growth.** CIPS processed
roughly **RMB 175tn (~$24.5tn) in 2024** (+43% y/y) and **RMB 180tn in 2025**, participants
spanning 180 countries by mid-2025; SWIFT data put RMB at ~4.3% of global payments by value
(Feb 2025) and ~6% of trade-finance transactions (Dec 2024, third after USD/EUR, up from 4.8% in
2023). None of this plumbing growth has moved the reserve-asset needle proportionally: RMB's
COFER share sat at 2.6% at RC2's endpoint (2023Q1) and recent estimates put it near 2% —
essentially flat-to-down while CIPS volumes roughly doubled, a clean illustration of A.1's
"roles need not travel together": a currency's payments/invoicing role can scale while its
reserve-asset role does not, because China's capital account remains substantially closed,
constraining conversion and market depth for reserve holders in ways private trade-settlement
flows do not face.

**(c) SDR — why it never worked.** SDRs are not a currency but a basket-weighted claim on IMF
members' currencies (weights reset every five years; the **2022 review** set USD 43.38%, EUR
29.31%, RMB 12.28%, JPY 7.59%, GBP 7.44%, RMB up from 10.92% in 2015), created and clearable
only through the IMF, unusable in private markets, issuable only via discrete allocation votes —
a reserve-pooling mechanism between members, not a source of new high-powered liquidity. The
scale gap is the clearest evidence: SDRs remain roughly **2%** of global reserves even after the
largest allocation in IMF history (the 2021 $650bn COVID allocation), against the dollar's ~57%.

**(d) Crypto/stablecoins — the counterintuitive dollar-reinforcement leg.** The naive prior is
that crypto, being outside sovereign control, erodes dollar dominance; the evidence runs the
other way. ~99% of stablecoin market cap is USD-pegged, backed overwhelmingly by US Treasury
bills: Tether alone held roughly **$135bn** in Treasuries by late 2025 — enough to rank among the
top-20 sovereign holders, ahead of South Korea and the UAE — while Tether and Circle (USDC)
together held ~$130bn, about **2.25%** of the entire T-bill market, mid-2025. In 2024 Tether was
reportedly the 7th-largest net buyer of US Treasuries even as China's holdings fell from over
$1tn to roughly $756bn. Mechanism: a stablecoin is functionally a narrow-bank claim on
short-dated dollar paper distributed globally without a US bank account — every non-US holder who
might otherwise diversify away from dollar savings instead holds a dollar claim, extending dollar
demand into populations traditional reserve/banking channels never reached. Evidence-thin in the
sense the asset class is young and policy-contingent (the same forward-looking caveat debt-deep
gives CBDC), but the balance-sheet evidence for reinforcement, not erosion, is now substantial
and Treasury-market-verifiable.

**(e) Gold — the "nobody's liability" diversification, quantified.** Central banks bought over
1,000 tonnes/year in 2022–2024 (2022: **~1,082–1,136t** depending on WGC revision vintage — the
highest since 1950; 2023: ~1,037–1,051t; 2024: ~1,045t) before cooling to **863t in 2025** —
still ~80% above the 2010–2021 annual average of ~473t. Purchases concentrate in a specific
cohort — Poland (+102t in 2025 alone, to 550t), Turkey (+27t through October 2025, to 644t),
China (officially +27t in 2025, to 2,306t) — disproportionately EM/geopolitically-exposed
central banks, not a broad developed-market rotation. Gold sits outside COFER by construction
(it is not a currency claim), which is precisely why cofer-RESULTS.md pairs COFER with WGC data
rather than reading COFER's flat-to-drifting FX shares as the whole diversification story.

**(iii) For L15.** None of the five currently satisfies A.1–A.2's multi-role bar — the euro
lacks the single safe asset, the RMB lacks capital-account openness, the SDR lacks private-market
usability, stablecoins currently *reinforce* rather than erode dollar demand, and gold is a
diversification hedge outside the currency system entirely, not a challenger currency. L15's
CB-gold leg is therefore a portfolio-diversification signal, never a "which currency wins next"
forecast — no free feed answers that question, and per A.1's four-role test none of the five
needs to win uniformly across all four roles for a transition to register. The honest read is a
slow broadening of the reserve-holder cohort (RC2), with gold as its one currently-measurable,
COFER-external leg.

**(iv) Citations.** ECB, "The International Role of the Euro," 2025/2026 editions **[Verified]**.
CIPS 2024/2025 volumes; SWIFT RMB payments/trade-finance shares **[Verified via multiple
industry/aggregator sources this session; SWIFT's own primary RMB Tracker not directly queried —
VERIFY]**. IMF (2022), SDR Valuation Review, Press Releases 22/153 and 22/281 **[Verified]**.
Tether/Circle Treasury holdings, 2025 **[Verified via secondary reporting of issuer transparency
reports; not cross-checked against primary attestations — VERIFY]**. WGC, *Gold Demand Trends*,
full-year 2022–2025 editions **[Verified directionally; exact 2022 tonnage varies 1,082–1,136t
across WGC revisions — VERIFY current authoritative figure]**. OMFIF (2024), central-bank
gold-motivation survey, 73 central banks **[Verified via secondary reporting; primary OMFIF
report not directly queried — VERIFY]**.

---

### A.6 Sanctions and weaponization — the 2022 freeze, cell by cell

**(i) The treatment event.** In February 2022 a G7+EU coalition froze roughly **$300bn** of the
Central Bank of Russia's ~$612bn total FX-and-gold reserves — about half its stock, immobilized
(not seized) chiefly via Euroclear in Belgium, which administers ~90% of the EU-held ~$200bn
portion. This is the first instance at scale of a G7 reserve currency's own custodial and
clearing infrastructure being used to immobilize a G20 central bank's reserves, demonstrating
that reserve assets held abroad are conditional on political alignment with the issuer, not an
unconditional store of value.

**(ii) DATA vs NARRATIVE, cell by cell.**

| Claimed response | Status | Evidence |
|---|---|---|
| CBs buying more gold *because of* the freeze | **NARRATIVE** (plausible, survey-supported, not causally proven) | OMFIF's 2024 survey (73 CBs): 40% cite geopolitical-risk hedging, 32% de-dollarization — self-reported motive, not a natural experiment; buying accelerated in 2022 but was already rising off the 2010–21 ~473t/yr base, so the freeze's marginal contribution is not cleanly separable in tonnage alone |
| USD COFER share fell *because of* the freeze | **DATA — and it says no** | Fed 2025-edition: dollar share "basically unchanged since 2022" (58%→~57%), concluding sanctions "have not led to fears of dollar weaponization causing a notable reallocation of reserves out of dollars" — this file's own RC3 (no regime break through 2023Q1) is the identical finding from an independent internal computation |
| EM CBs repatriating gold held abroad | **DATA** (partial, directional) | RBI moved gold onshore: 680t of ~880t total now held domestically (A.8) — a verifiable, if India-specific, data point |
| Bilateral non-dollar trade settlement scaling meaningfully | **NARRATIVE**, thinly supported | RBI's mechanism produced ~92 vostro accounts, 20 banks, ~22 countries by mid-2023 — infrastructure exists — but no consolidated settlement-*volume* figure was located; the largest visible balance (Russian-linked, ~$3.5bn per one 2024 report) reads as sanctioned counterparties' inability to repatriate proceeds, not organic bilateral preference |
| EM cohort's gold share of reserves rising | **DATA** | The 2022–2025 buyer cohort (Poland, Turkey, China, India among others) is visibly EM/geopolitically-exposed-weighted, not a broad DM rotation (A.5e) — a compositional fact distinct from the unproven causal claim |

**(iii) For L15.** Every DATA row is a level or compositional fact; every "...because of the 2022
freeze" causal claim is NARRATIVE, survey-supported at best, because no natural-experiment design
isolates the freeze's effect from the pre-existing 2010s diversification trend or the 2022–24
inflation/rate cycle's own effect on gold demand. L15's CB-gold leg reads the DATA rows only; the
causal story stays in the qualitative policy-review memo — the same Perez/fiscal-narrative
quarantine debt-deep's Part G.3 already established for the sibling seat, applied here.

**(iv) Citations.** As A.4–A.5 above for freeze magnitude and gold data; Fed (2025), "The
International Role of the U.S. Dollar — 2025 Edition" **[Verified]**; this program's own
cofer-RESULTS.md RC3 **[internal, frozen]**; RBI circular A.P. (DIR Series) No. 10, 11 July 2022
**[Verified]**; vostro-account counts via secondary reporting **[VERIFY: aggregate settlement
volume not located]**.

---

### A.7 What a transition would look like in our data feeds

**(i) Mechanism.** Given A.1's four-role split and A.2–A.4's evidence that transitions move
unevenly across roles over decades, no single series can be "the" leading indicator — the honest
design is a lag-and-quality-ranked hierarchy, read jointly, never singly.

**(ii) The hierarchy.**

| Indicator | Role tracked | Lag | Quality / caveat |
|---|---|---|---|
| IMF COFER shares | Reserve asset | Quarterly, ~1q publication lag | Highest-quality direct measure of the role that matters most; slow-moving by construction — a single quarter is noise (RC3) |
| WGC/RBI gold purchases | Reserve asset, non-currency leg | Monthly | Good frequency; self-reported with inconsistent disclosure completeness (China's cadence a standing question); a revalued stock, not flow-only — tonnage, not value share, is the cleaner read |
| BIS Triennial FX turnover | Vehicle/funding | Every 3 years | Excellent snapshot quality, unusable faster than a multi-year read |
| Trade-invoicing shares (DCP-style) | Invoicing | Academic-paper vintage, no live cadence | No continuously-updated free primary source located — the weakest leg, decadal context only |
| CIPS volumes / SWIFT RMB share | RMB plumbing/invoicing proxy | Monthly | High frequency but, per A.5b, scales independently of the reserve-asset role — a plumbing-capacity indicator, misleading as a reserve-share proxy |
| Swap-line network breadth | Funding backstop capacity | Event-driven | Directly observable, genuinely episodic — a discrete state, not a smooth series |
| IMF SDR basket weights | Composite official benchmark | Every 5 years (2015, 2022, 2027) | Slowest-moving in the hierarchy — a multi-decade cross-check only |

**(iii) For L15.** Ordered by lag-times-quality, COFER and WGC/RBI gold are the only two series
with both the frequency and the primary-source quality to function as an actual seat input —
exactly why they are the two series L15 already tracks (`docs/DESIGN.md` line 248) and why
cofer-RESULTS.md pairs them explicitly (RC3's own closing line). Everything else is context for
the quarterly-to-annual policy-review memo, not a numeric input — either the frequency is wrong
for a 120m+-τ½ seat, or (invoicing) no adequately-maintained free primary series exists at all.

**(iv) Citations.** As above; IMF (2025), "Improving the Analytical Usefulness of the IMF's
COFER Data," Technical Notes and Manuals 2025/014 **[Verified]**.

---

### A.8 India's position

**(i) Mechanism.** India is a reserve-currency **receiver**, not issuer — INR experiences
global dollar-liquidity cycles as an imported shock (FII flows, INR depreciation) rather than
exporting a reserve currency of its own; RBI's reserve-management choices are a large,
sophisticated receiver's risk management, not a data point about where the international system
is heading.

**(ii) Three verifiable behaviors, read honestly.** **Gold tonnage.** RBI held **880.52t** as of
31 March 2026 (680.05t domestic, 197.67t abroad — chiefly Bank of England and BIS) **[carrying
this file's own VERIFY forward: aggregator/press-sourced, not independently cross-checked
against RBI's own WSS/Annual Report primary release]**. This followed a 57.48t FY25 addition
(822.10t → 879.58t), and gold's share of RBI's total FX reserves rose from roughly 10% to
roughly 16% within about a year — driven by both continued buying and the 2025 gold-price rally
(a valuation effect, not purchases alone, the same stock/flow caveat A.7 flags for the WGC
series). RBI's own onshore repatriation (680t domestic) is the India-specific instance in A.6's
physical-repatriation DATA row. **The 1991 memory.** In May–July 1991, at the trough of the
balance-of-payments crisis (reserves near $1bn, ~2 weeks' import cover), the government pledged
**67 tonnes** of gold — 20t airlifted to the Union Bank of Switzerland, 47t to the Bank of
England — raising roughly $600mn to avoid default, conducted in secrecy to forestall panic. This
is a living institutional memory, not distant history, and plausibly the intuitive backdrop to
RBI's preference for an asset that — unlike an FX reserve deposit — cannot be frozen by a foreign
government's sanctions decision (A.6). **Rupee trade-settlement experiments.** The July 2022
special-vostro mechanism (A.6) is real infrastructure — 92 accounts, 20 banks, ~22 partner
countries by mid-2023 — but measured uptake is small against India's >$1.6tn annual goods-trade
turnover, and the most visible balances substantially reflect sanctioned counterparties' (chiefly
Russia's) inability to repatriate proceeds in hard currency, not organic bilateral preference
**[VERIFY: no consolidated aggregate INR-settlement-volume figure located this session — "tiny
uptake" is directional, sourced from account-count and anecdotal-balance reporting, not a
published volume series]**.

**(iii) What the seat should and should not read into this.** RBI's gold buying is a legitimate
instance of the global CB-gold-diversification mechanism (A.5e/A.6), feeding L15's WGC/RBI leg
directly, and its onshore repatriation is genuine data for the sanctions-era-caution story. It
should **not** be read as evidence India is positioning INR as a reserve-currency challenger — no
invoicing-scale, funding-scale, or COFER-visible anchor-scale shift accompanies the settlement
experiment (A.1's four-role test fails cleanly) — nor as an India-specific signal about the pace
of global dedollarization: RBI is one of dozens of buyers in a cohort A.5e already characterizes
as EM/geopolitically-exposed-weighted, not a uniquely informative one. The composition input
should weight RBI's gold behavior exactly as it weights any other central bank's in the pooled
WGC series, while the 1991 memory and the settlement experiments stay qualitative
policy-review-memo context, never a numeric override.

**(iv) Citations.** RBI gold tonnage/repatriation, March 2026 **[VERIFY — carries forward as
this monograph's own live figure, per this file's task brief]**. RBI FY25 gold addition
**[Verified via secondary reporting of RBI disclosure; primary release not directly queried —
VERIFY]**. 1991 gold pledge (67t, ~$600mn) **[Verified via multiple secondary business-press
sources; not cross-checked against a primary historical release — VERIFY]**. RBI rupee-settlement
circular and vostro-account counts **[Verified circular and counts; aggregate volume — VERIFY,
not located]**.

---

### A.9 Synthesis

| Mechanism | Observable (free series) | L15 input consumed | What nothing free captures |
|---|---|---|---|
| Four-role split (DCP; funding; anchor; reserve asset) | BIS turnover, invoicing estimates, IRR anchor classification, COFER | Confirms COFER as the correct role to track; no separate numeric input | A continuously-updated, primary-source trade-invoicing series — none located free |
| Network effects / geopolitical stickiness (Krugman; MKM; Mars-Mercury) | COFER level + drift | Sets τ½ (120m+) and the "one quarter is noise" discipline | An alliance-structure index — Mars/Mercury's own driver has no maintained free proxy |
| Exorbitant privilege / Triffin–Farhi-Maggiori | Academic return-differential estimates (not a live series) | Context only — no numeric input | A live, continuously-updated US return-differential series; academic estimates remain contested |
| Historical transitions (Eichengreen-Flandreau/Chitu; sterling's tail) | N/A — historical record | Grounds τ½ with two completed analogues (n≈2–3, atlas line 43) | A third, independent completed transition to raise the observation count |
| Challenger scorecard (euro, RMB, SDR, stablecoins, gold) | COFER-by-currency, CIPS/SWIFT, SDR weights, stablecoin Treasury holdings, WGC tonnage | COFER-by-currency (RC2) + WGC gold — L15's two live inputs | A single "who's winning" composite — none exists, and A.1 argues none should |
| Sanctions/weaponization (2022 freeze) | Frozen-reserve amount (one-off), COFER drift, WGC tonnage, RBI onshore share post-2022 | WGC/RBI gold leg (this file's harvest target); COFER read jointly, never alone (RC3) | A causal estimate isolating the freeze's effect from the pre-existing 2010s trend |
| Leading-indicator hierarchy | COFER, WGC/RBI, BIS turnover, CIPS, swap lines, SDR weights | COFER + WGC/RBI are the only two with adequate frequency/quality | A properly-frequent, primary-source invoicing series (the weakest leg, at any lag) |
| India's position | RBI WSS/Annual Report gold tonnage, vostro-account counts | WGC/RBI gold leg (India's own contribution to the pooled series) | A consolidated INR-trade-settlement-volume series; RBI gold data below full primary-source confirmation |

**What no free observable captures, in one line:** a continuously-updated, primary-source,
adequately-frequent trade-invoicing dataset — DCP's own headline finding (A.1) is
academic-paper-vintage, not a live feed, so the invoicing role of A.1's four-way split is the
one role this monograph's own hierarchy (A.7) cannot monitor at all, only cite historically.

---

## PART G — Operator psychology

Part A documents a real mechanism for gradual, sticky reserve-currency dominance sitting beside
equally real evidence that transitions do happen — faster than pure network-lock-in would
predict — once specific thresholds (war finance, current-account exhaustion, capital-control
credibility) crack. This Part maps the operator failure modes that two-sided inheritance invites
onto this program's governance layer: a doom cycle that oversells a −0.51pp/yr drift as an
emergency, its mirror — a permanence complacency Eichengreen's own 1920s finding argues against —
and gold-narrative capture, then the design countermeasures that convert each into a structural
non-decision.

### G.1 Dedollarization hype cycles vs RC1's measured drift

**Mechanism.** Financial media runs a "dollar collapse imminent" story on a cadence set by
salience — a debt-ceiling standoff, a BRICS-currency headline, a wobbly bond auction — almost
entirely decoupled from the measured pace of change. This program's own RC1 is the discipline:
71.2% (1999Q1) to 59.0% (2023Q1) is **−0.51pp/year**, a pace that would take **~57 more years**
to reach sterling's historical 30% endgame level held constant — "glacial," in the file's own
word, not a live regime break (RC3: no acceleration through 2023Q1; the Fed's independently
computed 2025-vintage read — "basically unchanged since 2022" — reproduces the same finding two
years further into the sample). Doom sells because a slow, multi-decade drift makes a poor
headline and an imminent-collapse framing makes a good one — the same asymmetry debt-deep's G.3
documents for fiscal-doom media, applied here to the reserve-currency register.

**Countermeasure.** Read the measured drift (RC1–RC3), never the narrative describing it, and
hold the review cadence (G.4) matched to L15's own 120m+ τ½ rather than news-cycle frequency.

### G.2 Dollar-permanence complacency — the mirror error

**Mechanism.** The opposite failure treats A.2–A.4's stickiness evidence as a promise that
nothing changes on any timescale relevant to a multi-decade design horizon. Eichengreen &
Flandreau's own revisionist finding (A.4) is the direct rebuttal: the conventional wisdom before
their 2009 paper — sterling secure until 1945 — was wrong by two decades, because contemporaries
under-weighted how far New York's capital markets had already deepened relative to London's by
the mid-1920s; multipolarity, once market depth and confidence cross a threshold, can arrive well
ahead of consensus expectations rather than announce itself gradually first. Mars/Mercury's
alliance-effect finding (A.2) sharpens this for today: a geopolitical realignment, not only a
change in relative GDP or market depth, is an independent, fast-acting channel through which
reserve shares can move — the 30pp per-alliance effect means "nothing changes until GDP shares
converge" is itself a category error, mistaking one channel (Mercury) for the whole mechanism.

**Countermeasure.** The seat does not bet on either error: the reduce-only gold-floor
construction (`docs/DESIGN.md` §4.3) is sized off the measured, glacial RC1–RC3 pace, but the
annual review cadence (G.4) exists precisely so a genuine threshold crack — a
Mars-hypothesis-consistent alliance shock, a sudden COFER regime break — is re-read within a
year, not discovered a decade late the way 1920s contemporaries discovered sterling's overtaking
only in retrospect.

### G.3 Gold-narrative capture

**Mechanism.** Every gold rally recruits the reserve-transition story after the fact — a sharp
price move gets narrated as "central banks are fleeing the dollar" whether or not WGC tonnage or
COFER currency shares actually moved that quarter, because the reserve-transition story is more
compelling than "gold rallied on the real-rate and price-momentum factors most gold moves are
actually driven by." A.6's own DATA-vs-NARRATIVE table is the discipline against exactly this:
the causal "CBs bought gold because of the 2022 freeze" claim is survey-supported (OMFIF: 40%
cite geopolitical-risk hedging) but not a proven natural-experiment result, and OMFIF's own
larger figure — 68% cite diversification generically, ahead of the 40% geopolitical-hedge share —
shows the less narratively-exciting motive is the bigger one even in central banks' own account
of their own behavior.

**Countermeasure.** L15's structural separation of COFER (currency shares) from WGC/RBI (gold
tonnage) as two paired, never-singly-read series (cofer-RESULTS.md's own closing line) is the
mechanical answer: a gold price rally alone moves neither series, so the narrative has nothing
numeric to attach to inside the seat's own inputs — the same principle debt-deep's G.2 uses
against gold-bug capitulation, applied here at input construction rather than allocation sizing.

### G.4 The design countermeasures

Three structural features do this Part's actual work, none requiring the operator to be wiser in
the moment than Part A's genuinely two-sided evidence justifies. **(1) The reduce-only clamp**
(CONTRACT §4/§10; Tier C). This file's harvest is explicitly bounded: an enrichment of L15's
composition input (the CB-gold leg), Tier C, reduce-only, zero timing authority — no reading of
A.4–A.6's evidence, however compelling in the moment (G.2/G.3's own risk), can push gold past its
pre-registered band or grant a timing call the registry's own validator does not already permit —
identical in structure to debt-deep's G.2 countermeasure against doom-cult capitulation, applied
to the sibling seat. **(2) The COFER+WGC pairing**, never one leg alone. RC3's own finding — the
2022 shock shows up in gold purchases, not (yet) in COFER's FX shares — is the empirical argument
for reading both jointly: a narrative only one leg supports (gold rallies with no COFER move, or
the reverse) is exactly the incomplete-evidence pattern G.3 exists to catch, made visible
mechanically rather than requiring the operator to remember to check. **(3) Annual review cadence
matched to τ½.** L15's 120m+ τ½ (atlas line 43) means the state should move meaningfully a few
times per decade at most; an annual — not quarterly, not news-cycle — review is the cadence at
which G.1's dedollarization-hype and G.2's permanence-complacency risks both get structurally
addressed: frequent enough to catch a genuine threshold crack within a reasonable window,
infrequent enough that no single quarter's headline can force a reading the underlying data does
not support.

### G.5 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Dedollarization doom cycle — a slow drift over-read as an emergency | RC1's −0.51pp/yr vs media's salience-driven "collapse imminent" cadence; Fed 2025-edition independently confirms "basically unchanged since 2022" | Read RC1–RC3's measured drift, never the narrative; annual, not news-cycle, review cadence |
| Dollar-permanence complacency — assuming nothing changes until GDP shares converge | Eichengreen-Flandreau: sterling's overtaking was already two decades ahead of consensus recognition; Mars/Mercury's 30pp alliance effect is a fast, GDP-independent channel | Annual review re-reads for a genuine threshold crack; reduce-only clamp bounds the response even once detected |
| Gold-narrative capture — every rally recruited into the reserve-transition story post hoc | Price moves narrated as reserve-diversification signal regardless of whether WGC tonnage or COFER shares moved; OMFIF's own 68% "diversification" exceeds its 40% "geopolitical hedge" | COFER+WGC read jointly, never singly (RC3); a price move alone moves neither series |
| Treating RBI's own gold buying as an India-specific reserve-status signal | A.8: RBI is one contributor among a global EM-weighted cohort (A.5e); rupee-settlement uptake too small/counterparty-concentrated to support a reserve-status reading | RBI's gold behavior weighted identically to any other central bank's in the pooled WGC series; 1991 memory and settlement experiments stay qualitative-memo-only |
| Re-admitting a single "transition indicator" — one COFER print or one gold-purchase month treated as the signal | A.7's hierarchy: no single series has both adequate frequency and quality; A.2/A.4's stickiness evidence means single-quarter moves are noise | Lag-and-quality-ranked hierarchy (A.7); only COFER + WGC/RBI qualify as numeric inputs, both read on a multi-quarter basis |

None of the five countermeasures asks the operator to resist a compelling narrative through
discipline alone in the moment it is most compelling — each removes the decision (how much to
read into this quarter's print, whether this rally means what the headline says, whether RBI's
own buying is special) before that moment arrives, converting it into a structural non-decision
made once, in the registry and in this file — the same closing pattern debt-deep's own Part G
establishes for its sibling seat.
