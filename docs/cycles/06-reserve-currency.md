# Reserve-Currency Transitions — Full Monograph (Atlas 0.2)

v1.0 · 2026-09-01 · Second entry of the atlas-ordered series. Harvest: enrichment of L15's
composition input (the CB-gold + COFER-drift pair; Tier C, REDUCE-ONLY, zero timing authority).
Chapter sources in `research/cycles/reserve-deep/`; data in `ingest/vault/debt` (COFER mirror,
sha256-manifested, authenticated against published anchors).

Headline real-data results (RC0–RC3): USD reserve share 71.2% → 59.0% over 1999–2023 =
−0.51pp/yr; ~57 more years to sterling's endgame level at the measured pace; the lost share went
to no single challenger (diversification at the margin — AESB reproduced); the drift is NOT
accelerating in FX shares (post-2015 −0.23pp/yr) — the 2022 sanctions response lives in
central-bank GOLD, outside COFER entirely, which is why the seat pairs two legs that must fire
together. The sterling master case: the only completed modern transition took four decades and
two world wars, with a negotiated wind-down at the end.

## Contents
- Part A+G — the four-role anatomy, stickiness, exorbitant privilege (both sides), the
  revisionist 1920s, the five-way challenger scorecard, the freeze data-vs-narrative table,
  psychology in both failure directions
- Part B — sterling→dollar at double length + five shorter cases + the live 2022+ gold wave +
  the preconditions scorecard and the seat's explicit falsification/escalation conditions
- Part B-RESULTS — RC0–RC3 computed by us
- Part C — COFER's breaks and imputation hazards, WGC-vs-IMF gaps (15x in one quarter), RBI's
  gold repatriation (38%→77% domestic share), eight new pullers
- Part D/E/F/H — the coordination-game math, the two-leg composition input, the quarterly
  algorithm, designs RV1–RV4, knowledge ledger

---


---

# PART A + G — Theory (four roles, network inertia, privilege, challengers) and operator psychology

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


---

# PART B — The case record: how monetary orders actually turned

# PART B — The case record: how monetary orders actually turned

*Reserve-currency monograph (atlas 0.2) · Part B of the deep-dive · v1.0 · 2026-09-01 · Author: Claude
(research agent) for Ionic quant desk (principal: gaurav@ionic.in)*
*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026 unless
tagged `[VERIFY: ...]`. This Part sits beside `research/cycles/reserve-deep/cofer-RESULTS.md` (our own
COFER real-data results — RC1-RC3 are referenced throughout and never recomputed or contradicted here)
and is written to the depth bar of `research/cycles/debt-deep/partB-cases.md` (the debt-supercycle
monograph's Part B): numbers-forward, every figure sourced, `[VERIFY]` where a search pass could not pin
the primary table.*

**A scoping note that governs everything below.** RC1 already delivered the single most important
number in this monograph: the USD's COFER share fell from 71.2% (1999Q1) to 59.0% (2023Q1), a drift of
**−0.51pp/year**, which at the measured pace would take **~57 more years** to reach sterling's ~30%
endgame level. RC3 adds that the drift shows **no regime break** through 2023Q1 even as gold buying
surged after 2022. Those are the facts; this Part supplies the mechanism. Every completed reserve-
currency transition in the historical record ran on **decades, not quarters**, and every one required a
specific, rare conjunction of conditions in the incumbent (fiscal exhaustion, usually war-driven) and in
the challenger (deep, open, convertible capital markets, willingly supplied in scale). The case record
below exists to answer one question with precision: **what, exactly, would have to happen for the RC1
drift to stop being glacial** — and the answer, argued case by case, is the spine of B4's falsification
conditions for the L15 gold floor.

---

## B1. Sterling → dollar: the master case

### 1.1 Sterling's nineteenth-century dominance mechanics

Britain formalized the gold standard in 1821 under Robert Peel — the first major economy to do so
formally, with most other advanced economies following only by the 1870s (Germany 1871–73, the United
States not until the 1900 Gold Standard Act). Gold convertibility gave sterling a near-zero structural
inflation bias for a century: UK inflation averaged **~0.28%/year from 1692–1914** [VERIFY: precise
long-run mean; widely cited, not independently re-derived this pass], and consol coupons of 3% delivered
real returns close to their nominal face throughout. On top of monetary credibility sat London's
position as the world's clearing house: **roughly half of world trade was financed through sterling
"bills on London"** just before WWI — the City's short-term money market instrument, discounted at the
Bank of England and traded globally regardless of whether either counterparty was British. Free trade
after 1840 and Britain's status as the "workshop of the world" (a description already current by the
1851 Great Exhibition) meant sterling was the currency in which the world's traders, shippers, and
insurers already had to hold working balances — reserve-currency status followed trade-and-credit
infrastructure dominance, not the reverse. By 1913, sterling accounted for **51% of identified official
reserves**, even as the French franc's share had risen from 15% (1899) to 31% (1913) at sterling's
partial expense — the first visible crack, pre-dating the two world wars entirely.

### 1.2 WWI war finance as the break

The war did to Britain's fiscal position what a century of gold-standard discipline had prevented:
national debt rose from **£650m (1914) to £7.7bn (1919)**, and debt/GDP moved from **~26% (1913/14) to
~128% (1918/19)** — a ~100-point run-up in four years, financed overwhelmingly by borrowing (only about a
quarter of the war effort came from taxation; Britain borrowed, in aggregate, roughly a full year's GDP).
This is the same mechanism the debt-supercycle monograph documents for every 20th-century war-finance
case (`debt-deep` cases 1–3): a shock large enough to force choices — inflate, repress, or default — that
peacetime fiscal discipline never has to make. Critically, the war also flipped Britain's external
position: the country that had spent a century exporting capital now had to import it, borrowing heavily
from the United States and running down its overseas asset base — the precondition for everything that
follows in the 1920s.

### 1.3 The 1920s interregnum: Eichengreen–Flandreau's revised chronology

The textbook story — that sterling remained the dominant reserve currency until the dollar finally
overtook it after WWII — is wrong, and the correction matters for how this Part reads "transition speed."
**Eichengreen & Flandreau (2008/2009, NBER WP 14154; *European Review of Economic History* 13(3):
377–411)**, using a four-country sample of central-bank reserve holdings (Italy, Norway, Spain,
Switzerland), find the **dollar first overtook sterling around 1924** — a full generation before
Bretton Woods. Robert Triffin's 1968 estimate that sterling still held ~80% of global reserves in 1928
has been directly challenged: a Federal Reserve Board staff estimate from 1928 itself put dollar-
denominated global exchange reserves at **roughly $1bn of a ~$2.3bn total (≈43%)** — already close to
parity with sterling, not a fifth of it. Eichengreen's own later synthesis (*Exorbitant Privilege*, 2011)
states plainly that by 1925, when London resumed gold convertibility, the dollar had already overtaken
sterling in the reserve portfolios of the world's central banks. The mechanism was that WWI transformed
the US from a net debtor into the world's largest creditor and deepest capital market almost overnight,
while sterling's own credibility was still recovering from wartime inflation and the 1919–25 float. The
interwar period was not "sterling holds, then dollar wins after 1945" — it was **rough, volatile parity
between two currencies for two decades**, with the outcome undecided until Bretton Woods made it a treaty
fact.

Churchill's April 1925 restoration of sterling to its pre-war gold parity ($4.86/£) then became its own
cautionary tale: the rate was overvalued (Keynes's contemporaneous critique), imported a deflationary
squeeze on the British economy, and Britain finally suspended gold convertibility in **1931**, followed
by Japan, the Scandinavian countries, and much of the Empire. The 1931 departure from gold is also the
formation point of the **sterling area** — the group of Commonwealth and allied economies that pegged to
sterling and held reserves in it — sterling's genuine, if partial, 1930s comeback: a regional captive
role rather than a restoration of global primacy, since the interwar Great Depression and America's own
retreat into monetary and trade isolationism meant neither currency was cleanly ascendant through the
1930s.

### 1.4 Bretton Woods as codification, not creation

By July 1944, when 44 Allied nations met at Bretton Woods, New Hampshire, the dollar's de facto primacy
(already roughly two decades old per §1.3) was simply written into treaty law: the dollar was pegged to
gold at $35/oz, and every other member currency was pegged to the dollar. Bretton Woods did not *make*
the dollar the world's reserve currency — it **codified an outcome the 1920s had already produced**,
adding the IMF/World Bank institutional architecture and, crucially, gold convertibility for foreign
official dollar holders, which is precisely the feature the Nixon Shock would later remove (B2, Case 2).

### 1.5 The sterling balances problem and the 1949/1967 devaluations

Britain emerged from WWII owing its own wartime allies and Commonwealth partners enormous sums, run up
buying war material and supplies on credit: sterling-area "sterling balances" — Commonwealth and allied
central-bank claims on the UK, held (often under exchange-control compulsion) as sterling reserves —
exceeded **£3bn by 1945**, a sum that dwarfed Britain's own foreign-exchange reserves and created a
standing threat: if holders ever tried to convert en masse, the UK could not honor the claims. This is
the structural condition behind both postwar devaluations. On **18 September 1949**, sterling was cut
30.5%, from $4.03 to $2.80; more than 19 countries pegged to sterling devalued in step. Even so, per
Catherine Schenk's authoritative account, sterling's share of **Western European** reserves had already
fallen below 10% by 1952, even as it still accounted for **more than 60% of sterling-area members'
reserves** as late as 1967 — a two-tier decline, with the captive sterling area propping up the aggregate
number long after the open, non-aligned world had moved on. The second devaluation, **18 November 1967**
($2.80 → $2.40, a 14.3% cut), broke that captivity too: it is widely described as the point after which
sterling fell below 10% of *global* reserves entering the 1970s, with the dollar's own share reportedly
near 85% by 1970 [VERIFY: precise global-share time series for 1945→1970 — sourced from a single
non-academic retrieval this pass; directionally consistent with Schenk's qualitative account
(<10% of Western European reserves by 1952, >60% of sterling-area reserves through 1967) but the exact
1945/1950/1960/1970 percentage points should be re-confirmed against Schenk (2010) or Avaro (2023)
directly before being treated as load-bearing].

### 1.6 The sterling area's managed wind-down: the Basel Agreements

What makes the sterling case unique in this entire dossier is that its terminal decline was **negotiated,
not merely suffered**. In **1968**, facing renewed sterling-area diversification away from sterling after
the 1967 devaluation, the UK reached agreement with the BIS and 12 industrial countries for a $2bn
medium-term stand-by credit; in exchange, sterling-area members agreed to keep minimum proportions of
their reserves in sterling for three-to-five years, with the dollar value of the bulk of their sterling
balances guaranteed by the UK Treasury. A second **1977** Basel Agreement went further: its explicit,
stated purpose was to "enable the British Government to achieve an **orderly reduction** in the role of
sterling as a reserve currency" — a G10-brokered, multilateral, deliberately managed retirement of a
reserve currency, the only such episode in this Part's record. Economic historians describe the 1968–74
period specifically as Britain "muddling through" a managed decline (Bromhead, *Economic History Review*,
2024) — currency statecraft flipping from resisting sterling's fall to administering it.

### 1.7 Timeline (reserve-share figures, each independently flagged)

| Year | Event | Sterling / dollar figure | Confidence |
|---|---|---|---|
| 1821 | Britain formalizes gold standard | — | High |
| 1899 | Franc begins gaining share | Franc 15% of reserves | High |
| 1913 | Pre-WWI peak documentation | Sterling 51% of identified reserves; franc 31% | High |
| 1914–19 | WWI war finance | UK debt/GDP 26% → 128% | High |
| ~1924 | Dollar overtakes sterling (4-country sample) | Eichengreen–Flandreau (2008/2009) | High (revises Triffin) |
| 1925 | UK restores gold at pre-war parity ($4.86/£) | Dollar already ahead in CB reserve portfolios | High |
| 1928 | Fed staff estimate of dollar reserve share | ≈43% ($1bn/$2.3bn) vs. Triffin's disputed 80%-sterling claim | Medium — competing estimates |
| 1931 | UK leaves gold; sterling area forms | Sterling's regional, captive-market comeback begins | High |
| 1944 | Bretton Woods | Dollar pegged to gold at $35/oz; all others pegged to dollar | High |
| 1945 | Sterling balances problem crystallizes | Sterling-area claims on UK exceed £3bn | High |
| 1949 | First devaluation | $4.03 → $2.80 (−30.5%); 19+ countries follow | High |
| 1952 | Sterling's European retreat already complete | <10% of Western European reserves (Schenk) | High |
| 1967 | Second devaluation | $2.80 → $2.40 (−14.3%) | High |
| 1968 | First Basel Agreement | Managed sterling-area wind-down begins | High |
| 1970 | Sterling below double digits globally | <10% of global reserves; dollar ≈85% [VERIFY exact %] | Medium |
| 1977 | Second Basel Agreement | Explicit "orderly reduction" mandate | High |
| 1999–2023 | Modern COFER era (our RC1–RC3) | Dollar 71.2% → 59.0%, −0.51pp/yr, no regime break | High (our own data) |

### 1.8 Investor outcomes: what happened to UK gilt and sterling-asset holders

The transition's cost to holders of UK claims split cleanly along the pre-1945/post-1945 line, and the
split maps exactly onto DS2/DS3's repression regimes documented in `debt-deep`. Through the gold-standard
century and into the 1920s deflationary interlude, nominal gilt holders were largely protected — near-
zero structural inflation, and the 1925–31 deflation actually *raised* the real value of fixed coupons
even as it crushed the real economy (Keynes's contemporaneous objection to the 1925 parity). The regime
inverted completely after 1945: nominal GDP grew **8.8%/year on average** through the postwar descent
(2.3% real + 6.5% average inflation), and the interest rate on government debt sat **below inflation in
24 of the 30 years from 1950** — the same repression mechanism `debt-deep` case 3 documents in detail,
run for longer and at higher average inflation than the American case. Layered on top of continuous
domestic repression were the two devaluations themselves: each was a discrete, one-time real write-down
of every sterling-denominated claim held outside the UK — precisely the sterling-area central banks that
had been incentivized (and, per Maylis Avaro's "Zombie International Currency" account, in places
coerced through exchange controls and commercial pressure) to hold sterling reserves in the first place.
A Commonwealth central bank holding sterling reserves through both 1949 and 1967 absorbed roughly a
**40%+ combined nominal write-down** on top of decades of negative real rates — the reserve-currency-
holder's version of the "unlegislated tax" Reinhart-Sbrancia describe for domestic bondholders. Real
assets fared entirely differently throughout: `debt-deep`'s own citation of the Dimson-Marsh-Staunton
series shows UK equities delivering **5.8%/year real over 1900–2000** — spanning the entire sterling
descent — a reminder that the transition destroyed the *currency's* privileged status and its nominal-
claim holders' real wealth, without correspondingly destroying UK real-asset returns.

### 1.9 Lesson table for L15

| Lesson | Evidence | L15 design implication |
|---|---|---|
| Financial-center dominance precedes and outlasts formal reserve-currency status; the two can decouple for decades | Bills-on-London ≈50% of world trade financing pre-WWI, while sterling's *reserve* share was already ceding ground to the franc from 1899 | A COFER-share reading alone will lag the true regime signal; the L15 composition input should track financial-infrastructure proxies (clearing/settlement share, bond-market depth), not currency shares alone |
| War finance, not gradual fiscal drift, is what has historically forced a reserve transition's decisive break | UK debt/GDP 26%→128% in four years (WWI); the interwar interregnum only *resolves* after WWII | The seat should treat a genuine acute fiscal/war-finance shock in the incumbent as a qualitatively different signal from gradual multi-decade drift — see B4 falsification conditions |
| The academic "transition date" is frequently decades earlier than the popular narrative believes | Dollar overtook sterling ~1924; Bretton Woods (1944) only codified a 20-year-old fact | The seat must not wait for a treaty-level "changing of the guard" event to register a transition already underway in the data |
| Reserve status can be propped up artificially, well past its natural expiry, via captive/coerced holders | Sterling area held >60% of its members' reserves in sterling through 1967 even as European reserves had abandoned it by 1952 | A rising *concentration* of remaining USD reserve holdings among a shrinking, more coerced-looking set of holders (vs. broad voluntary demand) is itself a warning sign worth tracking, independent of the headline COFER share |
| A currency's terminal decline can be negotiated and managed, not only suffered in crisis | 1968 and 1977 Basel Agreements explicitly engineered an "orderly reduction" of sterling's reserve role | A managed, multilateral wind-down of dollar primacy (rather than a disorderly one) is a live historical precedent — it should not be dismissed as an implausible tail case when scoring regime-shift scenarios |
| The costs of a reserve-currency transition fall on holders of nominal claims, not on holders of real assets | UK gilts and sterling reserve balances suffered decades of negative real returns and discrete devaluation write-downs; UK equities still returned 5.8%/yr real over the same century | Directly corroborates `debt-deep`'s own strongest cross-monograph finding: the debasement hedge belongs in a real asset, not a nominal one — the sterling case is the reserve-currency-specific instance of the same law |

---

## B2. Five shorter cases

### Case 1 — Guilder → sterling, 18th century: the financial-center role goes first

**Setup.** The Dutch guilder was Europe's de facto reserve currency through the 17th and 18th centuries,
anchored by the Bank of Amsterdam (founded 1609) and the Amsterdam bourse — the world's first genuinely
modern securities and money market. The arrangement gave the Netherlands "Dutch treat," a two-centuries-
earlier version of exorbitant privilege: the world's lowest prevailing interest rates, because foreign
capital preferred to sit in guilder-denominated Amsterdam paper. Amsterdam was likely still Europe's
largest financial center as late as the early 1770s — the guilder's monetary dominance persisted for a
generation after London had begun to rival it commercially. **The break.** The **Fourth Anglo-Dutch War
(1780–84)** did to the guilder what WWI would later do to sterling, compressed into four years instead
of a decade: the Dutch East India Company (VOC), already loss-making from 1780, saw its losses become
"enormous" during the war; British naval action crippled Dutch shipping, and rival powers — France chief
among them — seized the trade routes and financing business the Dutch could no longer defend. The war
bankrupted Dutch public debt and equities and, ultimately, the Bank of Amsterdam itself, which had been
quietly "lending" freshly issued guilders to bail out the failing VOC; when depositors realized this, a
run on the Bank followed, with gold preferred over paper. **Lesson for L15.** The guilder case supplies a
second, independent instance of B1's central mechanism (an acute war-finance shock, not gradual fiscal
drift, triggers the actual break) — but it isolates a variable sterling's case entangles: the guilder's
decline began as a **financial-center** collapse (a banking-system credit event, driven by a war fought
over trade and colonial assets) that only afterward became a reserve-currency collapse, whereas sterling
retained a functioning City of London and financial infrastructure throughout its own descent. This is
the strongest historical instance of the lesson already flagged in B1.9: watch the financial-
infrastructure variable, not only the currency-share variable, because the former can move first and
faster.

### Case 2 — The dollar's own crisis of confidence, 1971–1980: the case the incumbent survived

**Setup.** By August 1971, the Bretton Woods gold-convertibility promise had become untenable: US gold
reserves had fallen to roughly **8,584 tonnes**, and on 11 August the UK itself requested $3bn be moved
from Fort Knox to the Federal Reserve in gold — the immediate trigger. On **15 August 1971**, Nixon
closed the gold window and imposed a 10% import surcharge; the gold window never reopened, and Bretton
Woods was effectively dead overnight. **The confidence crisis.** The 1970s "Great Inflation" that
followed — two oil shocks (1973, 1979), expansionary Fed policy under Burns, and the Iranian hostage
crisis (Nov 1979) and Soviet invasion of Afghanistan (Dec 1979) adding safe-haven demand — pushed US CPI
inflation to roughly 14.8% at its peak and drove gold to **$850/oz at the London PM fix on 21 January
1980**, a record that stood for nearly 28 years. This was, functionally, the dollar's own confidence
crisis: the market pricing a serious probability that the world's reserve currency could not hold its
value. **The Volcker restoration.** Paul Volcker's Fed, from **6 October 1979** ("the monetarist
experiment"), targeted non-borrowed bank reserves rather than the funds rate, letting rates float upward
without political constraint: the funds rate moved from 11.4% (5 October) past 13.8% within weeks, to
17.6% by April 1980, and peaked around **19.1% in June 1981** [some sources cite a July 1981 peak nearer
22%; range confirmed, single point-estimate not fully reconciled — VERIFY exact peak date/level]. Gold
collapsed from its $850 peak toward the $300s within a few years as the disinflation took hold, at the
cost of a severe double-dip recession and unemployment above 10% in 1982. **What saved the incumbent.**
Three conditions distinguish this case from every transition case in this Part: (i) no alternative
currency offered comparably deep, open capital markets even at the nadir of dollar confidence — the
Deutsche mark and yen were both too small and too capital-controlled to absorb reserve-scale flows;
(ii) the US political system tolerated a genuinely costly corrective (a deep recession) in service of
long-run credibility; (iii) critically, this was a **monetary-policy-credibility crisis**, not a fiscal-
exhaustion or war-finance crisis — the underlying productive economy and capital markets were never
impaired the way Britain's were by two world wars. **Lesson for L15.** Incumbency can survive even a
severe, self-inflicted confidence shock provided no deep, open challenger market exists and domestic
institutions can administer costly correction — this is the load-bearing counter-example against reading
any dollar confidence wobble as inherently transition-triggering, and it directly frames B4's
falsification logic: a repeat of 1971–80 without a genuine open-market challenger would very plausibly
resolve the same way it did the first time.

### Case 3 — The yen's rise and plateau: surplus economies can't supply reserve assets

**Setup.** Japan's Ministry of Finance ran an explicit "internationalization of the yen" push through the
1980s — opening the Euroyen market, easing access to yen-denominated bonds for foreign issuers — and the
yen's share of global official reserves rose steadily, peaking at roughly **9.1% at end-1990/close to 9%
in 1991**. **The stall.** From that peak the yen's reserve share fell back toward the low single digits
and has stayed there through the modern COFER era — our own RC2 table shows JPY moving from 6.0% to just
5.5% across 1999Q1–2023Q1, a currency that has essentially flatlined at a fraction of its early-1990s
level for three decades. **Why.** The structural constraint is not gross market size — Japan's government
bond (JGB) market is enormous in absolute terms, over ¥1,200 trillion outstanding, among the largest
fixed-income markets in the world. The constraint is that Japan is a **chronic current-account-surplus
economy**: a reserve-currency issuer must, almost definitionally, run the current-account deficits that
put net new claims on itself into foreign hands (the Triffin-dilemma logic, mirrored) — a surplus
economy instead recycles its savings outward through its own foreign asset purchases rather than letting
foreigners accumulate a large net-creditor position in local-currency government paper. Layered on top,
the Bank of Japan's own balance sheet came to hold roughly half of the outstanding JGB stock as
quantitative easing proceeded from the 2000s onward, further shrinking the internationally tradable free
float even as the gross market grew; foreign ownership of JGBs did rise over time (from **7.0% in 2011 to
11.9% in 2025**) but from a persistently thin base for a market this size. **Lesson for L15.** A surplus
economy with an even very large domestic bond market cannot, absent a structural shift to persistent
current-account deficits (which Japan has shown no inclination to run) and a genuinely free-floating
government-bond supply, host a reserve currency at scale — this is directly relevant to scoring China's
own RMB prospects (Case 5, and B4), since China shares exactly this precondition failure with 1990s-era
Japan.

### Case 4 — The euro's launch and ceiling: what the eurozone crisis proved about fiscal-union prerequisites

**Setup.** The euro launched 1 January 1999 with an official reserve share of **17.9%**, and rose
steadily to a peak of **~28% in Q3 2009** (27.6% immediately before the crisis broke) — genuinely
credible progress toward challenging the dollar within a single decade, the fastest ascent of any
challenger in this Part's record. **The ceiling.** The Greek sovereign debt crisis, erupting in 2010,
reversed the trend decisively: the euro's reserve share fell from 27.6% (2009) to **19.9% by 2015**
(against the dollar's 64.1% the same year) — an 8-point retreat inside five years. **What the crisis
proved.** The eurozone had a shared currency but no shared fiscal backstop and no genuinely joint,
default-remote safe asset: reserve managers had been implicitly treating the currency union as if it
conferred the safe-asset properties of a fiscal union, and the 2012 PSI default on Greek debt (documented
in full in `debt-deep` case 9 — a 53.5% nominal haircut, ~75–80% NPV loss on private Greek bondholders)
proved that assumption false in the most direct way possible: a euro-denominated government bond is only
as safe as the issuing member state's own fiscal position, not as safe as "the euro" as a currency.
**Lesson for L15.** Currency union is not safe-asset union. A reserve currency built on a currency area
without joint fiscal issuance will structurally cap out below what the area's aggregate GDP or trade
weight alone would predict, because reserve managers ultimately hold sovereign paper, not currency units
in the abstract — and a patchwork of national credits inside one currency reintroduces exactly the credit
risk a true reserve asset is meant to be free of. This is the clearest evidence in the entire case record
that RMB internationalization (Case 5) faces an analogous, if differently-shaped, credibility ceiling:
a currency's reserve status is inseparable from the depth, safety, and political-institutional
credibility of the sovereign paper denominated in it.

### Case 5 — The RMB decade: the gap between ambition and plumbing

**Setup.** On **11 August 2015**, the PBoC devalued the RMB's daily reference rate by **1.9%** in a
single move — the currency's biggest one-day drop since China's 1994 dual-rate unification — framed
officially as a market-oriented reform of the fixing mechanism but read internationally as a shock
devaluation amid slowing Chinese growth, and widely understood as partly aimed at satisfying IMF
"freely usable" criteria ahead of SDR review. That review succeeded: the IMF Executive Board approved RMB
inclusion in the SDR basket on **30 November 2015**, effective **1 October 2016**, with the RMB assigned
a **10.92% weight** (USD 41.73%, EUR 30.93%, RMB 10.92%, JPY 8.33%, GBP 8.09%) — the first change to the
SDR basket's composition in over 15 years. **The plumbing side.** China has since built genuine payments
infrastructure at speed: CIPS (Cross-Border Interbank Payment System) processed **RMB123.06trn
(≈US$17.09trn), +27.27% YoY, across 6.61m transactions (+50.29% YoY) in 2023**, and **RMB175.49trn
(≈US$24.47trn), +42.60% YoY, across 8.22m transactions (+24.25% YoY) in 2024**, reaching **1,766
participants across 124 countries and regions** by 2025 — genuine, fast-compounding growth in the rails
available for RMB settlement. **The reserve side has not followed.** RMB's COFER share peaked around
**2.83% in Q1 2022** and has since declined — to roughly **2.37% by Q3 2023** and further since — a
plateau in the low-to-mid 2% range that our own RC2 table's endpoint (2.6% at 2023Q1) sits consistent
with, and that has not meaningfully advanced despite SDR inclusion, eight years of CIPS build-out, and
active Chinese and partner-country de-dollarization rhetoric. **The gap, explained.** CIPS transaction
*value* has compounded at 27–43%/year while the RMB's *reserve* share has been flat-to-declining since
2022 — the clearest possible illustration that payments-rail growth and official reserve-manager
confidence are different variables. The gap traces to precisely the preconditions Case 3 and B4 make
explicit: continued capital-account controls (RMB is not freely convertible), a managed rather than
free-floating exchange rate, opacity around PBoC/SAFE intervention, and the lingering credibility cost of
the 2015–16 devaluation scare itself — a reserve manager who watched the PBoC devalue by surprise in 2015
has a durable reason to discount RMB's "freely usable" credentials regardless of how fast CIPS grows.
**Lesson for L15.** RMB internationalization is real and worth monitoring, but on the specific dimension
that matters for a reserve-currency floor (official reserve-manager allocation, not payments-corridor
usage) it has been stuck for four years running — the single cleanest example in this Part of why the
seat must track COFER share directly rather than proxy indicators like CIPS growth, trade-invoicing
share, or SDR-basket symbolism, none of which have moved the actual reserve number.

---

## B3. The 2022+ gold wave as a live case

**The purchase numbers.** World Gold Council data show central banks net-buying **1,082 tonnes in 2022**
(the highest annual total since 1950), **1,037 tonnes in 2023** (the second-highest on record), and
**approximately 1,045 tonnes in 2024** (a third consecutive year above 1,000 tonnes) — a genuinely
unprecedented three-year run. Cumulative 2022–24 purchases reached **~3,220 tonnes**, more than double
the already-elevated 2010–2021 average pace of **~473 tonnes/year**. **Which central banks.** The buying
is concentrated, not broad-based: China's PBoC added a reported **225 tonnes in 2023** — its largest
single reported annual addition since at least 1977 — while Poland's central bank added **130 tonnes**
(April–November 2023, +57% to 359t), the second-largest 2023 buyer; in 2024, Poland was again the
largest single buyer (~90 tonnes), with Turkey and India also adding substantially. China, Poland, and
Türkiye are the three most consistently identified leading buyers across the 2020–2025 window.
**The China question — official vs. estimated unreported.** The PBoC's officially disclosed purchases run
well below independent analyst estimates of China's actual accumulation: official 2025 additions via
SAFE were reported at just **25 tonnes**, against Société Générale's estimate that SAFE alone imported
closer to **250 tonnes** that year; "unreported" London-market purchases were estimated at **110 tonnes
in September–October 2024 alone**. Rolled up, independent estimates put China's *actual* total monetary
gold reserves at roughly **5,400–5,500 tonnes (Q3 2025 estimates)** against the **~2,235–2,304 tonnes**
officially reported to the IMF over the same period — unofficial estimates run at roughly **2.3–2.5×**
the disclosed figure. This is a live, unresolved discrepancy, not a settled fact — treat every "true
Chinese holdings" number as an estimate, not a reported statistic. **Gold's share of global reserves at
market value.** The ECB's own June 2025 reporting states gold reached **~19–20% of global official
reserves by the end of 2024** (dollar ~46%, euro ~16%), overtaking the euro as the second-largest reserve
asset by value for the first time. Against a mid-2010s baseline of roughly **10–13%** [VERIFY: a single,
clean, primary-sourced 2015 percentage was not independently pinned this pass; multiple secondary sources
place gold's market-value share "barely 10%" by the 2000s, consistent with but not identical to a precise
2015 figure], this represents something close to a **doubling** of gold's market-value reserve share in
under a decade — driven by both the 2022–24 purchase wave and the roughly 30% rise in the gold price
during 2024 alone. Sharper claims of gold reaching 24–30% of reserves by late 2025 circulate in less
rigorously sourced outlets and very likely reflect short-lived price-driven spikes rather than a stable
new plateau; the ECB's ~20% end-2024 figure is treated here as the more defensible anchor. **The freeze-
causality evidence.** The February 2022 Western sanctions freezing roughly **$300bn** of Russian central-
bank reserves — the first G7-coordinated freeze of a G20 central bank's reserves at this scale — is
widely read as the proximate trigger for the acceleration. The most directly relevant academic evidence,
**Arslanalp, Eichengreen & Simpson-Bell (2023, IMF WP 2023/014, "Gold as International Reserves: A
Barbarous Relic No More?")**, finds that **countries facing a higher risk of US sanctions increased the
gold share of their reserves more than countries facing lower risk**, and identifies 14 "active
diversifiers" — countries that raised gold's reserve share by ≥5pp over two decades — every one of them
an emerging market. Follow-on 2024–2025 literature explicitly extending this analysis into the post-2022
sanctions-shock period exists (cited under titles such as "De-Dollarization and Gold: Central Bank
Reserve Reallocation in the Post-Sanctions Era") but the specific venue/peer-review status of that later
work was not independently confirmed this pass `[VERIFY: exact publication details]`. **Honest statement
of what this does and does not imply for the dollar.** Three things are simultaneously true and do not
contradict each other: (i) the gold-buying cohort is a specific, sanctions-exposed subset of emerging-
market central banks (China, Russia, Turkey, and the wider "active diversifier" set) — advanced-economy
reserve managers (Fed, ECB, BOJ) are not participating; (ii) gold is not a competing reserve *currency* in
COFER's sense — it earns no yield, is not used to fund FX intervention or invoice trade, and (per
`cofer-RESULTS.md`'s own framing note) is **not in the COFER denominator at all**; (iii) the dollar's
COFER share has continued its RC1 drift (−0.51pp/yr) with **no visible regime break through 2023Q1**,
exactly while gold buying surged — RC3's own conclusion that "the 2022 sanctions shock shows up in gold
purchases, not yet in FX shares" is the correct read. The 2022+ gold wave is best understood as
**insurance-buying against freeze/confiscation risk by a specific, exposed cohort of states**, running in
parallel with — not as evidence of an accelerating collapse in — the dollar's FX-reserve role.

---

## B4. Synthesis

### Transition preconditions, scored for today

| Precondition | Sterling→dollar (1914–44) | Guilder→sterling (1780–84) | Dollar 1971–80 (non-transition) | Today: USD vs. RMB |
|---|---|---|---|---|
| Fiscal exhaustion / war-finance shock in incumbent | Yes — WWI debt/GDP 26%→128% | Yes — 4th Anglo-Dutch War bankrupts VOC/Bank of Amsterdam | **No** — a credibility crisis, not a fiscal-capacity crisis | **No** — US debt/GDP elevated but not multiplied by an acute war-finance shock |
| Capital-account/financial-center erosion in incumbent | Yes — sterling credibility damaged by WWI inflation & float | Yes — Bank of Amsterdam run, credit collapse | No — US markets never impaired | No — US capital markets remain the deepest, most open in the world |
| Challenger with genuinely deep, open, convertible capital markets | Yes — US became the world's largest creditor almost overnight | Partial — Britain's markets already rivaling Amsterdam's pre-war | No credible challenger existed at the time | **No** — RMB capital account remains managed/controlled |
| Challenger able/willing to run the deficits that supply net new safe assets | Yes — US ran the needed external position | N/A (mechanism differs — war-driven, not deficit-driven) | N/A | **No** — China runs persistent current-account surpluses (same structural constraint that capped the yen, Case 3) |
| Incumbent's own political capacity to administer a costly correction absent | Yes — Britain's postwar politics could not avoid the sterling-balances trap | Yes — no Dutch fiscal capacity remained | **No** — Volcker's Fed *could* and did administer a costly correction | Unclear/untested — no comparable US shock has yet required the test |

Scored against this table, **none of today's candidate challengers clears even a majority of the
preconditions that every completed transition in this record required simultaneously**. The clearest
individual gap is China's: it fails the exact precondition (persistent current-account deficits/open
capital account) that stalled the yen for three decades (Case 3), independent of any US-side fiscal
condition at all.

### Pooled conclusions, ranked by evidence strength, mapped to L15

1. **(Strongest — corroborated across every completed transition case in this Part and by RC1's own
   measured pace.)** Every historically completed reserve-currency transition ran on **decades**, driven
   by an acute break in the incumbent (usually war finance) combined with a challenger that already had
   deep, open capital markets ready to absorb the flow. → **Design implication:** RC1's ~57-year
   extrapolation is not merely a mechanical curve-fit; it is consistent with the entire historical base
   rate. L15 should treat the current drift as **regime context, never a trade**, exactly as RC1 already
   concludes — and should require an acute, dated, verifiable trigger event (not a continuation of the
   drift) before treating a transition as underway.
2. **(Strong — B1's own revised chronology plus the WWI/4th Anglo-Dutch War pairing.)** The *academic*
   transition date is systematically earlier than the *treaty-codification* date the popular narrative
   fixates on (dollar overtook sterling ~1924; Bretton Woods only codified it in 1944). → **Design
   implication:** the L15 monitoring set must include leading, market-based indicators (bond-market
   depth, financial-center/clearing share) alongside the lagging, official COFER series, precisely
   because the lagging series will confirm a transition only after it is already well underway.
3. **(Strong — Case 2, the dollar's own 1971–80 crisis.)** Incumbency can survive a severe, self-inflicted
   confidence shock provided (i) no deep, open challenger market exists, and (ii) domestic institutions
   can administer a costly corrective. → **Design implication:** a dollar confidence wobble (a gold
   spike, a Fed-credibility episode, a sharp DXY move) is **not, by itself**, sufficient evidence to treat
   a transition as underway — it must be evaluated jointly against whether a genuine open-market
   challenger exists, which today it does not (per the preconditions table).
4. **(Strong — Cases 3 and 5, yen and RMB, independently converging on the same mechanism.)** A
   structurally surplus economy cannot host a reserve currency at reserve-manager scale regardless of its
   bond market's gross size, because it does not supply the net new safe assets the world needs to hold.
   → **Design implication:** China's current-account position, not RMB payments-infrastructure growth
   (CIPS), is the correct variable to monitor for a genuine RMB-driven regime shift — and it has shown no
   sign of flipping.
5. **(Strong — Case 4, the euro's ceiling, corroborated in full by `debt-deep` case 9's PSI detail.)**
   Currency union without fiscal union caps a reserve currency's ceiling below what raw economic weight
   would predict, because reserve managers ultimately hold sovereign credit risk, not abstract currency
   units. → **Design implication:** any future euro-area or multilateral-currency-basket challenger
   scenario must be scored against genuine joint fiscal issuance (Eurobonds at reserve-asset scale), not
   against currency-union membership alone.
6. **(Moderate — B3, the 2022+ gold wave; strong on mechanism, moderate on the specific China magnitude
   given the official/unreported discrepancy.)** Gold accumulation since 2022 is real, large, and
   causally linked in the academic literature to sanctions/freeze risk — but it is concentrated in a
   specific, exposed cohort of central banks and is a *different variable* from the dollar's FX-reserve
   share, which shows no corresponding regime break. → **Design implication:** this is the direct,
   real-time corroboration of L15's structural design choice to hold gold as a distinct sleeve rather than
   as a proxy signal for dollar decline — the two series are genuinely decoupled in the data, exactly as
   the gold floor's rationale requires them to be treated.
7. **(Moderate — a synthesis finding, not a single-case finding.)** Across every case in this Part, the
   cost of a reserve-currency transition fell on holders of **nominal** claims (gilts, sterling balances,
   Reichsmark deposits, Greek government bonds), never on holders of **real** assets, which continued to
   compound through the transition in every case where a real-asset series was available (UK equities
   5.8%/yr real 1900–2000; DS4's pooled fiscal-dominance-state equity result in `debt-deep`). → **Design
   implication:** this is independent, reserve-currency-specific corroboration — on top of `debt-deep`'s
   own debt-cycle evidence — for sizing the debasement hedge in a real asset (gold), never a nominal one.

### Falsification / escalation conditions for the seat

Given `CONTRACT.md`'s Tier-C, reduce-only discipline (§4) and the century-scale glacial pace this Part
has repeatedly documented, **lifting** the gold floor band — i.e., relaxing the current structural
minimum — should require the **conjunction of at least two independent legs**, each sustained across
**multiple consecutive annual reviews**, not any single leg alone:

1. **A dated, acute trigger in the incumbent, not a continuation of drift.** A genuine US fiscal-
   exhaustion or war-finance-scale shock (an acute, not gradual, jump in US federal debt/GDP via a
   dateable event) **combined with** sustained, multi-quarter evidence of foreign-official-holder flight
   (falling foreign share of UST auctions, sustained TIC-data selling by foreign officials) — the direct
   analogue of the WWI-into-1920s sequence in B1.
2. **China (or any single challenger) clearing its own precondition failures, verifiably.** Both (a) a
   documented, IMF-classified move to genuine capital-account convertibility (AREAER reclassification,
   not rhetoric), **and** (b) a sustained flip to current-account deficits over 3+ consecutive years —
   the exact two conditions Case 3 (yen) and Case 5 (RMB) currently fail. Absent both together, RMB
   internationalization progress (CIPS growth, SDR symbolism, bilateral trade-invoicing deals) should be
   logged but not treated as regime-shift evidence, per Case 5's own lesson.
3. **A regime break appearing in COFER itself, not merely in gold.** RC3 already establishes the
   diagnostic: a sustained multi-year *acceleration* in the USD COFER drift (materially beyond the
   measured −0.51pp/yr, e.g., sustained below the RC3-observed historical trough of −1.40pp/yr for
   multiple consecutive years) **and** evidence the lost share is consolidating into a single credible
   successor rather than diffusing across many currencies and gold (RC2's own finding — the lost share
   has gone mostly to non-traditional currencies and gold, not to one challenger) would be the specific,
   observable pattern that distinguishes genuine regime change from continued diversification-at-the-
   margin.

Any one leg firing in isolation — a gold spike, a single bad Treasury auction, an RMB SDR-weight increase,
one quarter of accelerated COFER drift — should be logged and reported at the annual review, but should
**not** by itself justify lifting the floor. The historical record argued throughout this Part is
unambiguous that every completed transition required multiple, independent, sustained legs firing
together; a single leg has, in every case examined here, either reversed (Case 2) or stalled indefinitely
(Cases 3 and 5).

---

## Side-task — GitHub-hosted mirrors for atlas 0.2 data

Per the 2026-09-01 mirror-authorization decision (`research/OPEN_QUESTIONS.md`), only
`raw.githubusercontent.com`, `media.githubusercontent.com`, and `objects.githubusercontent.com` are
reachable from this environment. Using GitHub's own code-search index (`mcp__github__search_code`), the
following were found for the four requested categories. **Nothing was downloaded** — existence,
content-shape, and a first-pass credibility judgment only. The yield this pass was materially thinner
than `debt-deep`'s equivalent side-task: two of the four requested categories are **confirmed gaps**, not
omissions — stated honestly below rather than papered over.

1. **`KMueller-Lab/Global-Macro-Database-Stata`** — the same "Global Macro Database" (Müller et al.)
   already used as a `debt-deep` mirror, re-confirmed here for a different variable. Its metadata files
   (`data/helpers/varlist.csv`, `data/helpers/docvars.csv`, `data/helpers/bib_dataframe.csv` — all
   independently verified present) name **`REER`** ("Real effective exchange rate, index 2015=100") as a
   standard panel variable, explicitly sourced from `BIS_REER` (BIS Effective Exchange Rates,
   `data.bis.org/topics/EER`) and `BRUEGEL` (Darvas, 2021, "Timely Measurement of Real Effective Exchange
   Rates"). **Credibility: high** for the repository and its sourcing chain (same provenance standard
   already vetted in `debt-deep`'s side task). The actual `data/final/REER_....csv` data file — which by
   exact analogy to the confirmed `gen_govtax_GDP_2025_12.csv` and `M4_2025_12.csv` filenames almost
   certainly exists at `data/final/REER_2025_12.csv` — was **not independently returned** by this
   session's code-search index this pass `[VERIFY: confirm exact filename/path directly before the data
   phase relies on it, exactly as debt-deep flagged for its own analogous gold/debt file]`. This is a
   multi-country REER panel, not a long single USD trade-weighted series specifically — the closest
   available match to the requested category, not an exact one.
   `https://raw.githubusercontent.com/KMueller-Lab/Global-Macro-Database-Stata/7bfaa03854e8893634d9d8a6042b4ac69c8b948d/data/helpers/bib_dataframe.csv`
2. **`LEEYOUNGJIN-GIT/fred-macro-review`** — `data/fred_latest.csv` and numerous dated files under
   `data/fred_history/` (each independently confirmed present via code search). These are genuine,
   live-pulled FRED series including **`DTWEXBGS`** (Trade-Weighted U.S. Dollar Index: Broad,
   2006=100) with real numeric levels, daily/weekly deltas, and companion series `DTWEXAFEGS`
   (advanced-economy dollar index) and `DTWEXEMEGS` (emerging-market dollar index). **Credibility:
   medium-high** — a personal macro-dashboard repository (not an original vendor) but the values shown
   are plausible, internally consistent, correctly-labeled FRED pulls; the repository re-pulls and
   commits a new snapshot repeatedly (multiple dated files observed), so it functions as a **live**
   USD trade-weighted index mirror rather than a **long historical back-series** to 1973 as the task
   ideally wants `[VERIFY: whether any single file in this repo carries the full historical run rather
   than only recent 2026 snapshots, before relying on it for a long-run series]`.
   `https://raw.githubusercontent.com/LEEYOUNGJIN-GIT/fred-macro-review/6673856b1873d1c8a891402fce4839ed4e8248b6/data/fred_latest.csv`
3. **`raulincadet/Macro`** — `CurrenciesWorld/ReservesComposition/COFER_...csv` (already vetted at
   high credibility in `debt-deep`'s own side task: a genuine IMF COFER extract with correct indicator
   codes, 1995–2023). **Relevance caveat, stated plainly:** this file covers the **modern COFER era
   only** (1995 onward) and does **not** reach the interwar period Eichengreen–Mehl–Chitu study — it is
   listed here only as a partial, adjacent proxy for category (a), not a match for it.
   `https://raw.githubusercontent.com/raulincadet/Macro/65b2aa9bf463f9797fdd6c228a9def86488b7968/CurrenciesWorld/ReservesComposition/COFER_07-01-2023%2002-51-41-63_timeSeries.csv`
4. **Eichengreen–Mehl–Chitu interwar reserve-share data (category a) — confirmed gap.** No GitHub-
   vendored copy of the underlying interwar (1899–1939) reserve-composition data behind Eichengreen &
   Flandreau (2008/2009) or the later Eichengreen–Mehl–Chitu (2017) *How Global Currencies Work* book was
   located as a committed file, despite multiple targeted searches (author-name, book-title, and
   subject-matter queries). This dataset is a principal's-machine task: it exists as journal-article
   appendix tables (NBER WP 14154, *European Review of Economic History* 13(3)) rather than as a
   vendored bulk file, exactly the pattern `debt-deep`'s own side task found for the IMF Global Debt
   Database's bulk export.
5. **World Gold Council central-bank gold statistics extracts (category b) — confirmed gap.** No clean,
   tabular WGC central-bank-gold-holdings mirror was located; searches returned only scattered
   news-headline/sentiment-analysis CSVs that *mention* gold, tonnes, or "World Gold Council" inside free
   text (financial-news corpora, NLP training sets), not structured WGC data tables. The authoritative
   source (`gold.org/goldhub/data/gold-reserves-by-country`) does not appear to have a GitHub-committed
   mirror at present. Principal's-machine task for the data phase.
6. **SWIFT RMB Tracker data (category d) — confirmed gap.** No vendored SWIFT RMB Tracker (or PBoC RMB
   Internationalization Index) tabular data was located on GitHub via code search; the only hits were
   incidental social-media/text-corpus mentions of "RMB," "SWIFT," and "internationalization" as
   vocabulary tokens, not structured data. Principal's-machine task for the data phase.

---

## References

Eichengreen & Flandreau (2008/2009). "The Rise and Fall of the Dollar, or When Did the Dollar Replace
Sterling as the Leading Reserve Currency?" NBER WP 14154; *European Review of Economic History* 13(3):
377–411. · Eichengreen (2011). *Exorbitant Privilege: The Rise and Fall of the Dollar and the Future of
the International Monetary System*. Oxford UP. · Eichengreen, Mehl & Chitu (2017). *How Global Currencies
Work: Past, Present, and Future*. Princeton UP. · Schenk (2010). *The Decline of Sterling: Managing the
Retreat of an International Currency, 1945–1992*. Cambridge UP. · Avaro (2024). "Zombie International
Currency: The Pound Sterling 1945–1971." *Journal of Economic History*. · Bromhead (2024). "Managed
Decline: Muddling through with the Sterling (dis)Agreements, 1968–74." *Economic History Review*. ·
Arslanalp, Eichengreen & Simpson-Bell (2023). "Gold as International Reserves: A Barbarous Relic No
More?" IMF WP 2023/014. · Chinn & Frankel (2007, 2012); Chinn, Frankel & Ito (2024). "The Dollar Versus
the Euro as International Reserve Currencies." *Journal of International Money and Finance*. · Federal
Reserve History, "Nixon Ends Convertibility of U.S. Dollars to Gold" (essay). · Federal Reserve History,
"Volcker's Announcement of Anti-Inflation Measures" (essay). · Bank of Japan / Ministry of Finance Japan,
"Chronology of the Internationalization of the Yen." · World Gold Council, *Gold Demand Trends* (annual)
and *Central Bank Gold Reserves Survey* (2024, 2025 editions). · European Central Bank, "Gold demand: the
role of the official sector and geopolitics" (IRE Focus, June 2025). · IMF COFER database and
`research/cycles/reserve-deep/cofer-RESULTS.md` (this desk's own RC1–RC3 computations, referenced
throughout and never recomputed here). · `research/cycles/debt-deep/partB-cases.md` (this desk's
debt-supercycle case record — cases 3, 6b, and 9 cross-referenced directly above). · GitHub mirror URLs
per the side-task section, confirmed via `mcp__github__search_code` this session.


---

# PART B-RESULTS — Real data: IMF COFER (RC0–RC3)

# Atlas 0.2 — reserve currency: COFER real-data results (1999Q1-2023Q1)

Source: IMF COFER mirror (vault-manifested). World, shares of ALLOCATED reserves.
GOLD IS NOT IN COFER — the 2022+ CB gold leg is measured separately (WGC/RBI,
principal runsheet). Generated 2026-09-01; trials RC1-RC3 ledgered.

## RC0 — Authentication vs published landmarks

- USD share 1999Q1: **71.2%** (published ~71%); 2021Q4: **58.8%**
  (published ~58.8% — the Arslanalp-Eichengreen-Simpson-Bell 'stealth erosion'
  paper's anchor numbers). Both match: file accepted.

## RC1 — The dollar's drift, measured

- USD share 1999Q1 → 2023Q1: 71.2% → 59.0%
  = **-0.51pp per year** on average.
- At this measured pace, the USD share would take **~57 more years** to
  reach 30% (sterling's endgame level) — the century-scale claim of atlas 0.2, in a
  number. Transitions are glacial; the seat is REGIME context, never a trade.

## RC2 — Where the lost share went

| Currency | first obs | last obs | change |
|---|---|---|---|
| USD | 71.2% | 59.0% | -12.2pp |
| EUR | 18.1% | 19.8% | +1.6pp |
| JPY | 6.0% | 5.5% | -0.6pp |
| GBP | 2.7% | 4.9% | +2.1pp |
| RMB | 1.1% | 2.6% | +1.5pp |
| AUD | 1.5% | 2.0% | +0.5pp |
| CAD | 1.4% | 2.4% | +1.0pp |
| CHF | 0.3% | 0.2% | -0.0pp |
| Other | 1.6% | 3.7% | +2.0pp |

The AESB finding reproduced: the USD's lost share went mostly to NON-traditional
reserve currencies (AUD/CAD/RMB/other), NOT to the euro — there is no single
challenger; there is diversification at the margin. Plus the part COFER cannot see:
gold, which is where the 2022+ action moved (WGC data, next).

## RC3 — Is the drift accelerating?

- Rolling 5y annualized USD-share change: mean -0.50pp/yr, min -1.40 (2006Q2), max +0.87 (2016Q2).
- Post-2015 mean: -0.23pp/yr vs pre-2015 -0.69pp/yr — drift, with episodes, no
  regime break visible in COFER through 2023Q1. The 2022 sanctions shock shows up in
  GOLD purchases (outside this file), not yet in FX shares — exactly why the L15
  composition input pairs COFER with the WGC/RBI gold series.



---

# PART C — Data engineering: watching a monetary order, free

# Part C — Data engineering: watching a monetary order, free

v1.0 · 2026-09-01 · Atlas 0.2 (reserve-currency / monetary-order transition), `docs/CYCLE_ATLAS.md`
entry 0.2: "~80–110y; n≈2–3 ever (guilder→sterling→dollar)... Active leg today: sanctions-driven CB
gold buying since 2022." Atlas 0.2's Parts A/B/D/E/F/H are still queued (`docs/cycles/README.md`);
this Part is delivered first because the ladder seat it feeds is already live and already partially
built: `config/ladder.yaml L15_long_wave_fiscal` names its role as **"debt/GDP level+5y slope,
negative-real-rate persistence, reserve diversification (RBI gold, COFER)"** — three legs, and
`research/cycles/debt-deep/partC-data.md` already sourced the first two (fiscal aggregates,
real-rate splice). **This Part's job is the third leg only**: the reserve-diversification /
composition input — the "CB-gold accumulation leg + COFER drift leg" the task brief names, which
is also the entirety of what `research/cycles/reserve-deep/cofer-RESULTS.md`'s RC1–RC3 trial
measured on the desk's existing 1999Q1–2023Q1 COFER mirror. L15 itself carries **no regime-score
seat** (`ladder.yaml`: "L15/L16 have NO regime-score seat") — its whole authority runs through the
`long_wave_expression` gold-floor-attribution and tail-budget bands, Tier C, reduce-only (CONTRACT
§4). Extends, not duplicates, `docs/masterplan/A-data-catalog.md` blocks **G** (G6 WSS, G7 REER,
G10 reference-rate archive), **J** (J4 COFER, J5–J8 FRED) and **K** (K1–K3 gold) — cross-referenced
by ID below — and feeds K1's dual consumer, `gold_score`'s `cb_buying_regime` input (weight
0.20–0.25, B-module-specs.md §6.5), which reads the identical WGC/RBI series this Part sources.
Consumes CONTRACT §3 (free-source mandate) and Known Prior #11 (no live network access here; RBI,
IMF, FRED, WGC, SWIFT all block direct fetch from this container — web search does not; every pull
below happens on the principal's machine against a committed fixture). Checked by web search this
pass, cross-checked across ≥2 results where feasible, nothing fetched directly; anything not so
corroborated carries **[VERIFY]**.

---

## C.1 IMF COFER — the FX-reserve composition leg

**Access.** IMF migrated its data dissemination to a new SDMX-3.0-based platform at
`data.imf.org` (superseding the legacy `dataservices.imf.org/REST/SDMX_JSON.svc` endpoint, now
being retired) during 2023–2024; COFER's live page is
`data.imf.org/en/datasets/IMF.STA:COFER` (the older `data.imf.org/en/Datasets/COFER` /
`data.imf.org/COFER` short-links still resolve but should not be treated as the canonical path
for a build script). Bulk pull is a free SDMX/CSV export, no login, no API key required. **147
reporters** currently participate (monetary authorities of IMF members, several non-members, and
other reserve-holding entities) — this count itself is a vintage-dependent fact, not a constant.

**Cadence and lag.** Quarterly, ~1-quarter publication lag — the standard the desk's mirror and
`cofer-RESULTS.md` already assume. IMF's COFER methodology note (BOPCOM 24-09) is the primary
citation for cadence and reporter mechanics.

**The allocated/unallocated split — what it is, and the China distortion specifically.**
COFER has always separated **allocated reserves** (reporters who disclose currency composition)
from **unallocated reserves** (everyone else's total FX reserves, imputed from the IMF's
International Liquidity database as a residual). Two properties made this residual large and
lumpy rather than a clean noise floor: (i) **China does not, and has not, reported the currency
composition of its reserves to COFER** — the world's largest reserve holder by a wide margin sat
entirely inside "unallocated" for most of COFER's history; (ii) the unallocated share was
correspondingly enormous early on — roughly half of world reserves in the early 2000s — and fell
mechanically as more countries began reporting, **not** because currency preferences shifted.
IMF itself dates a material step-change to **2018**, when it confirmed a broadened/improved
reporting base that materially lifted the allocated share — commonly read as at least a partial
**China phase-in of COFER-visible reporting over 2015–2018**, though whether China's own reserves
became directly visible (vs. the pool of *other* non-reporters filling in) is genuinely disputed
in the literature and is flagged **[VERIFY: whether China itself became a COFER-allocated reporter,
or the 2015–18 allocated-share rise reflects other non-reporters joining]**. A second, unrelated
suppression sits in the same window: starting **2015 Q2**, IMF stopped publishing the
advanced-economies vs. emerging-and-developing-economies breakdown of COFER, citing the risk that,
with a published list of participants, that split could allow individual-reporter disclosure —
a confidentiality-driven data cut, not a definitional one, but one more break landing in the same
2015 quarter.

**The honest splice rule.** Any USD-share (or any currency-share) time series crossing 2015–2018
is measuring two effects at once: genuine portfolio drift among *already-reporting* central banks,
and a **mechanical composition-pool change** as large non-reporters (China foremost, disputedly)
entered or exited the visible pool. The rule this forces: **never read a level break or slope
change in the COFER share series across 2015–2018 as a pure preference signal without checking the
allocated-reserves coverage ratio (allocated ÷ total) for the same window** — a jump in that ratio
is the tell that the share series moved for compositional, not behavioral, reasons. This is
identical in kind (not in date) to the 2025Q3 break below, and both breaks now sit inside the
desk's own measured window (`cofer-RESULTS.md` RC1's 1999Q1→2023Q1 span brackets 2015–2018 whole).

**The 2025Q3 break, restated for construction.** Starting **2025 Q3**, with revisions applied back
to **2000 Q1**, IMF eliminated the unallocated bucket outright, publishing a currency composition
that nets to 100% of world reserves — **10.4% of that 2025Q3 total is IMF-imputed**, not
reporter-disclosed (A-catalog J4 already flags the break; the imputed-share figure is new this
pass). This means the post-2025Q3 series is not merely a reweighting of the same allocated data to
a new denominator — a genuine model-based estimate for non-reporters (China very much included) is
now baked into the published USD share itself. **Rule**: any COFER pull spanning 2025Q3 uses the
revised series only, end to end; the pre-revision vintage is retained in the vault (never deleted)
strictly as an audit trail for exactly this kind of before/after comparison, never spliced onto the
new one mid-series.

**Table structure — claims vs. shares.** COFER ships two related objects, and a build script must
pull both, not just the shares:

| Object | Unit | What it is | Historical availability |
|---|---|---|---|
| Currency composition, **claims** | US$ millions | Level of allocated reserves held in each currency, World aggregate | 1999Q1+ (pre-2025Q3 vintage); 2000Q1+ (post-2025Q3 revised vintage) |
| Currency composition, **shares** | % of allocated reserves (pre-2025Q3) / % of total reserves (post-2025Q3) | Claims ÷ the relevant total — the series `cofer-RESULTS.md` RC1–RC3 already computed | Same as above |
| Allocated reserves, total | US$ millions | Denominator for shares (pre-2025Q3) | 1999Q1+ |
| Unallocated reserves | US$ millions | Residual (pre-2025Q3 vintage only — eliminated from 2025Q3 onward) | 1999Q1–2025Q2 |
| AE / EMDE breakdown | US$ millions, by currency | Discontinued **2015 Q2** — a level break in coverage, not in the currency definitions | 1999Q1–2015Q1 only |

The claims level matters independently of the share: a currency's share can fall purely because
total reserves grew faster in currencies the reporting pool happens to hold more of, with the
claims level in that currency flat or even rising — the level/share distinction is the same
discipline the debt monograph applies to debt stock vs. debt/GDP ratio.

**Extending the desk's 1995–2023Q1 mirror forward (principal's machine).** The existing vault file
(`ingest/vault/debt/cofer_1995_2023q1.csv`, sha256-manifested, RC0-authenticated against the
Arslanalp-Eichengreen-Simpson-Bell anchor values) is a **pre-2025Q3-methodology** vintage. It
cannot simply be appended to: a naive "pull 2023Q2-onward and concatenate" script would splice an
old-methodology (unallocated-included) history onto a new-methodology (unallocated-eliminated,
imputed) tail — precisely the error this Part's splice rule forbids. The correct procedure:

1. Pull the **entire** current COFER SDMX/CSV extract fresh (2000Q1–latest, post-2025Q3 revised
   vintage) — do not attempt a delta pull. Manifest as a **new**, distinctly named fixture
   (`cofer_2000q1_{latest}_rev2025q3.csv`); the existing 1995–2023Q1 file stays untouched.
2. Re-run `scripts/analyze_reserve_currency.py`'s RC0–RC3 trials against the new fixture in
   parallel with the old one. RC0's authentication check (USD share 1999Q1 ≈71%, 2021Q4 ≈58.8%)
   should still pass on the revised vintage *if* the revision genuinely only reallocates the
   unallocated residual — a failure there is itself informative (flags that the revision moved
   the allocated-only numbers too, not just the total).
3. Diff RC1's measured slope (−0.51pp/yr, 1999Q1→2023Q1, old vintage) against the same window
   recomputed on the revised vintage. Any material difference is the **2025Q3 revision's own
   contribution to the measured drift** — report it explicitly, never blend it silently into "the
   dollar's decline."
4. 1999Q1 itself sits **outside** the revision's 2000Q1 floor — treat it as a one-quarter orphan on
   the revised series (drop it from any revised-vintage-only construction, or keep it flagged as
   old-vintage-only in a mixed table).
5. From here forward, each new COFER release is a routine same-vintage append (both vintages remain
   fixed methodology until IMF's next break); manifest each new quarter's pull separately, keyed
   `(series_id=COFER, vintage=post-2025Q3, pull_date)`.

---

## C.2 WGC central-bank gold data — the leg COFER cannot see

**What's free.** The **Gold Demand Trends** quarterly report (`gold.org/goldhub/research/
gold-demand-trends`) — including its dedicated **Central Banks** section per edition
(`.../gold-demand-trends-q{n}-{yyyy}/central-banks`) and the standalone **country-level holdings**
page (`gold.org/goldhub/data/gold-reserves-by-country`, itself built from **IMF IFS** data, so it
overlaps J4 at a country granularity COFER itself does not expose) — is free to read as HTML/PDF.
**Free registration** ("free, quick, easy... unlimited access to all Goldhub market data")
unlocks the data-explorer's filter/date-range/download tooling; the PDF reports themselves are
open with no gate at all (A-catalog K1 already flags this split; confirmed again this pass).
**Cadence/lag**: quarterly, released roughly **4–5 weeks** after quarter-end — Q1 2026 on
2026-04-29, Q2 2026 on 2026-07-30, a consistent 4-week gap. A separate, faster **monthly**
central-bank-statistics post appears on the Goldhub blog between quarterly editions.

**The reported-vs-estimated-unreported distinction — the single largest data-honesty issue in
this section.** There is **no mandatory rule** requiring any country to report gold transactions
to the IMF. WGC's own headline "central bank net purchases" figure is **not** the IMF-reported
number — it is WGC's (via Metals Focus) own estimate, built from London OTC market flow, Swiss
refinery trade data, and other proxy indicators, explicitly designed to capture buying that never
shows up in any official disclosure. The gap between the two numbers is not a rounding matter:
**Q1 2026 IMF-reported net central-bank purchases were 16 tonnes; WGC's estimated total central-
bank demand for the same quarter was 244 tonnes — roughly 15× the officially disclosed figure**,
and Metals Focus separately estimated unreported buying at **57% of the full-year 2025 total**.
China is the largest single contributor to this gap: PBoC's officially reported 2025 purchases
were on the order of 25–41 tonnes (source-dependent; **[VERIFY]** exact figure, differs by outlet)
against SocGen's own estimate that China's true 2025 buying ran **~10× the official figure**, with
independent analyst estimates (Nieuwenhuijs; BMO Capital) putting China's **true cumulative gold
reserve** at roughly **5,000–5,200 tonnes** against an officially declared ~2,300–2,350 tonnes —
more than double. **Construction rule**: never present WGC's central-bank-purchase figure as if it
were the IMF-reported number, or vice versa; carry both, labeled, with the gap itself as an
informative series (a widening gap is itself a signal about the *opacity* of official gold
accumulation, arguably as relevant to Atlas 0.2's "active leg" as the purchase level itself).

**Tonnage vs. market-value accounting.** WGC's country-holdings table and RBI's own disclosures
both report gold in **tonnes** (a physical quantity, revision-free except for genuine
purchases/sales) alongside a **market value** in USD or local currency (tonnes × the prevailing
gold price × the FX rate, revised continuously as price/FX move with zero change in physical
holdings). A quantity series and a value series answering different questions must never be
plotted as if interchangeable — the identical trap the RBI section below documents concretely for
the May-2026 "phantom drawdown" episode.

---

## C.3 RBI's own reserves — WSS, monthly Bulletin, half-yearly gold report

| Source | Cadence | Access | What it uniquely carries |
|---|---|---|---|
| **Weekly Statistical Supplement (WSS)** | Weekly, published Fridays, reflecting the reserve position roughly one week prior (~1-week lag) | `rbi.org.in/scripts/WSSViewDetail.aspx?TYPE=Section&PARAM1=2` | FX reserves broken into Foreign Currency Assets, Gold, SDRs, Reserve Tranche Position — in both ₹ crore and US$ million; the fastest-cadence gold **value** read (A-catalog G6) |
| **RBI Bulletin monthly tables** | Monthly | `rbi.org.in` Bulletin section; DBIE-queryable | Same four-way FX-reserve split at monthly granularity, plus REER (G7) and reference-rate (G10) tables in the same document family |
| **Half-Yearly Report on Management of Foreign Exchange Reserves (HYRMFER)** | **Semi-annual** (Apr–Sep, Oct–Mar), released roughly **one month** after each half-year end — e.g. the 43rd edition (Apr–Sep 2024) was published 2024-10-30 | `rbi.org.in/scripts/HalfYearlyPublications.aspx?head=Report+on+Foreign+Exchange+Reserves` | **The only source for gold tonnage broken into domestic vs. overseas custody** — this is the input the desk's CB-buying-regime leg actually needs, and no weekly/monthly series carries it |

**The domestic-vs-custody split, and why it is the India-specific, sanctions-era signal.**

| As-of date | Total gold (tonnes) | Held domestically | Bank of England + BIS custody | Gold deposits | Domestic share |
|---|---|---|---|---|---|
| Mar-2023 | ~[VERIFY exact total] | ~301t | remainder | — | ~38% |
| Mar-2025 | 879.59t | ~[VERIFY] | ~[VERIFY] | — | ~59.2% (**[VERIFY]**, single-cluster of sources conflicts with a "60%, Jun-2024" figure in adjacent reporting — resolve on first live pull against the primary HYRMFER PDF, not secondary news) |
| Mar-2026 | 880.52t | 680.05t | 197.67t | 2.80t | **77.23%** |

The trajectory (38% → ~59–60% → 77.23% domestic, 2023–2026) is RBI's own explicit, dated response
to the 2022 Russia sanctions episode — the same freeze-of-reserves shock the Atlas 0.2 entry names
as the "active leg today." **This is the single cleanest India-specific, free, quarterly-or-better,
directly-observable proxy for the sanctions-driven-reserve-repatriation hypothesis** the whole
monograph is built around — better than any global aggregate, because it is one actor's own
disclosed balance-sheet choice, not an inferred flow.

**The May-2026 valuation-vs-quantity trap, worth naming explicitly.** RBI shifted its own gold
**revaluation** cadence from monthly to weekly (a documented methodology note), which means
week-to-week changes in the reported gold **value** can now reflect nothing more than price/FX
marking, not a change in tonnage. A May-2026 press episode inferred a gold *drawdown* from a
value-series analysis; RBI publicly denied any tonnage sale, and the tonnage figure in the next
HYRMFER confirmed no reduction — the value series moved, the quantity series did not. **Rule**:
tonnage must always be read from the primary WSS/HYRMFER tonnage line, never inferred from a
value-series delta, exactly the tonnage-vs-market-value discipline C.2 states for WGC data.

---

## C.4 Invoicing and settlement data — measuring the "how", not just the "how much"

**Academic invoicing-currency panels (Gopinath et al.).** The dominant-currency-paradigm
literature's own dataset — country-level shares of exports/imports invoiced in USD, EUR, and other
currencies — has been extended repeatedly (most recently to **132 countries, 1990–2023**, per the
newest working-paper vintage, with RMB coverage added). **No single, stable, versioned public
GitHub repository was confirmed this pass** — the practical access path is the NBER/AEA working
paper's own data appendix and the authors' institutional pages (Harvard/Princeton), not a
maintained package; **[VERIFY]** the exact current download URL and licence terms on first contact,
and treat any given vintage as a dated academic release (its own "vintage date"), not a live feed.

**RBI's own rupee-settlement mechanism data.** RBI's July-2022 framework for International Trade
Settlement in Indian Rupees requires foreign correspondent banks to open **Special Rupee Vostro
Accounts (SRVAs)**; RBI/press disclosures give periodic **counts** of the mechanism's uptake —
**156 SRVAs across 123 correspondent banks from 30 partner countries, as of February 2025**
(up from 92 accounts/20 banks in July 2023) — but **no RBI-published aggregate flow series**
(₹ value of trade actually settled through SRVAs) was found free this pass; the FEDAI-maintained
SRVA **directory** (a bank/account list, not a value time series) is the closest structured free
artifact. **Honest coverage note**: this is a **participation-count** proxy for rupee
internationalization, not a trade-value series — treat it exactly that way, the same caution the
CIPS participant count below requires.

**SWIFT RMB Tracker / Global Currency Tracker.** Free, monthly, no-login PDF
(`swift.com/products/rmb-tracker` document centre; direct edition URLs like
`swift.com/sites/default/files/files/rmb-tracker_july-2025.pdf`), covering RMB's share of SWIFT
payment-message value alongside a global-currency ranking table. RMB's share has moved from
**2.88% (Jul-2024 data) to ~3.50% (Apr-2025 data)**, sitting around 5th–6th globally across recent
editions. **Coverage caveat, stated plainly**: SWIFT-message share measures *messaging volume*
through the SWIFT network specifically — it structurally **undercounts** RMB settlement that
increasingly routes through CIPS instead of SWIFT-message rails (C.6), so a rising CIPS-participant
count alongside a flat-to-declining SWIFT RMB share is not necessarily "RMB internationalization
stalling" — it may be RMB settlement migrating off the rail SWIFT measures.

---

## C.5 Exchange-rate legs — the denominators every INR/gold/reserve series needs

| Series | Access | History | Cadence/lag | Note |
|---|---|---|---|---|
| **FRED DTWEXBGS** (Nominal Broad USD Index) | `fred.stlouisfed.org/series/DTWEXBGS`, free CSV, no login | **2006-01-02+**, rebased Jan-2006=100 | Daily, T+0/T+1 | Successor to the discontinued Major Currencies Index (DTWEXM, retired Jan-2020) and the goods-only DTWEXB — a **26-economy** trade-weighted basket including India, China, Euro Area; **any pre-2020 dollar-index series spliced onto DTWEXBGS crosses a methodology break**, identical discipline to A-catalog J5-J8's own flag |
| **BIS Effective Exchange Rate indices (NEER/REER)** | `data.bis.org/topics/EER` — migrated to the **BIS Data Portal on 2023-11-22** (supersedes the older `bis.org/statistics/eer.htm` static-file scheme); free single-file CSV bulk download, no login | India **broad** basket (64 economies): **Jan-1994+**; narrow basket (26–27 economies) also available | Monthly | The free, non-RBI, cross-country-consistent REER cross-check against RBI's own G7 series — useful precisely because RBI's 36→40-currency basket change (A-catalog G7) is an RBI-specific break that BIS's own methodology does not share, giving an independent read through that transition |
| **RBI reference-rate archive (USD/INR)** | `rbi.org.in/scripts/referenceratearchive.aspx` | Daily archive runs from **April 1995** (per this pass's search; A-catalog G10 leaves this **[VERIFY]** — resolved here) | Daily, same-day | **FBIL took over computing/disseminating the reference rate from RBI effective 2018-07-10** — a compiler change, not (per this pass) a level break in the rate itself, but the compiler-of-record fact belongs in the fixture's metadata |

---

## C.6 Complements — SDR basket weights, swap-line networks, CIPS

**IMF SDR basket weights — five-yearly reviews as dated regime markers.** Free, published on
every review (`imf.org/en/topics/special-drawing-right/sdr-valuation-basket`; the IMF's own
infographic PDF, "board-approved SDR basket currency weights at past quinquennial reviews," is the
single cleanest citation). Reviews run on a nominal five-year cycle, with one COVID-era delay:

| Review (effective date) | USD | EUR (DEM+FRF pre-1999) | JPY | GBP | RMB |
|---|---|---|---|---|---|
| 1991 (1985–89 data) | 40% | 21%+11% | 17% | 11% | — |
| 1996 | 39% | 21%+11% | 18% | 11% | — |
| 2001 | 45% | 29% | 15% | 11% | — |
| 2006 | 42.9% | 34.1% | 11.5% | 11.5% | — |
| 2011 | 41.9% | 37.4% | 9.4% | 11.3% | — |
| 2016 (eff. 2016-10-01) | 41.73% | 30.93% | 8.33% | 8.09% | 10.92% |
| 2022 (eff. 2022-08-01, delayed ~1yr for COVID) | 43.38% | 29.31% | 7.59% | 7.44% | 12.28% |
| Next (due by end-Jul-**2027**) | — | — | — | — | — |

1981/1986 review weights not independently confirmed this pass — **[VERIFY]**. The RMB's
inclusion (2016) is itself the cleanest single dated marker in the entire free-data landscape for
"the IMF formally certified a challenger currency as freely usable" — a regime-marker Atlas 0.2's
theory section (once written) should anchor directly to this table, not to a vaguer "China's rise."

**Swap-line networks — a free, trackable network measure.** The Fed maintains **five standing,
permanent** dollar-swap lines (Bank of Canada, BoE, BoJ, ECB, SNB — since 2013-10-31,
`federalreserve.gov/regreform/reform-swaplines.htm`, free) plus **temporary** lines opened and
closed around stress episodes (nine additional central banks in Mar-2020, most since lapsed) —
the New York Fed's own swap-arrangements page is the free primary source for current status. The
PBoC runs a parallel, larger, and still-*growing* bilateral network: **32 countries/regions as of
May-2025**, cited elsewhere as **42 active lines totaling ~¥3.84 trillion (~US$540bn) by
end-Q1-2026** (figures from different trackers/dates — **[VERIFY]** reconciliation; PBoC's own
page, `pbc.gov.cn`, is the primary free source, supplemented by the CFR's free **Central Bank
Currency Swaps Tracker**, `cfr.org/articles/central-bank-currency-swaps-tracker`). **As a network
measure**: track swap-line **count** and **total committed value** for both networks quarterly,
free, from primary-institution pages — a rising PBoC-network node count against a static
five-country Fed standing network is a legitimate, quantifiable proxy for "who is building
reserve-currency-adjacent crisis-liquidity infrastructure," independent of any FX-share metric.

**CIPS participant counts.** China's Cross-Border Interbank Payment System publishes participant
counts periodically via its own site (`cips.com.cn/en`) and PBoC/state-media releases — **free**,
but as **periodic disclosure, not a queryable time series**: **193 direct / 1,573 indirect
participants across 124 countries at end-2025**, rising to **210 direct / 1,619 indirect across
192 countries by end-Jun-2026** (sourced via press releases and secondary trackers this pass —
**[VERIFY]** against CIPS's own primary release page on first live pull). Pair with the SWIFT RMB
Tracker (C.4) explicitly: a rising CIPS node count with a flat SWIFT-message RMB share is the
signature of settlement infrastructure migrating off the rail SWIFT actually measures.

---

## C.7 Vintage/PIT hazard table

| Series | Revision-prone? | Two dates never to conflate | Store first-print or every vintage? |
|---|---|---|---|
| COFER shares | **Yes, twice over** — the 2015-18 reporting-pool broadening and the 2025Q3 unallocated-elimination (revised to 2000Q1) | Reporting-pool-coverage date (mechanical) vs. genuine drift date (behavioral); pre-/post-2025Q3 methodology | **Every vintage**, both the pre- and post-2025Q3 series kept distinct forever (A-catalog J4) |
| WGC central-bank purchases (WGC/Metals Focus estimate) | **Yes** — WGC's own single-quarter reading is provisional for ~1-2 subsequent quarters as more country data arrives; the reported-vs-estimated gap itself is a moving target | WGC estimate-vintage date vs. IMF-reported figure's own (separate, slower) vintage | Both series kept distinct, never merged into one "central bank buying" number |
| RBI gold (WSS/HYRMFER) | Not revision-prone in tonnage; the **value** series moves continuously on price/FX with no tonnage change | Weekly-revaluation value-change date vs. actual tonnage-change date (HYRMFER, semi-annual) | Tonnage: append-only event log; value: continuous series, always paired with the concurrent tonnage figure |
| RBI domestic/custody gold split | Semi-annual step series, not continuously revised | HYRMFER as-of date (Mar/Sep) vs. report publication date (~1 month later) | Every HYRMFER edition retained as its own dated snapshot |
| DTWEXBGS / dollar index | Structural break, not a revision | Legacy DTWEXM/DTWEXB (pre-2020) vs. DTWEXBGS (current, 26-economy) | Both kept distinct; DTWEXBGS is the only series usable post-2020 |
| BIS REER basket | Portal migration (2023-11-22), not a series break | Old static-file era vs. BIS Data Portal era — same underlying series, different access mechanics | One continuous series; only the *access path* changed |
| RBI reference rate | Compiler handover (RBI → FBIL, 2018-07-10) | Compiler-of-record date | One series; compiler recorded as metadata, not a splice point |
| SDR basket weights | Not revision-prone — each review is a dated, discrete regulatory event | Review-decision date vs. effective date (these differ, e.g. 2022 decided May, effective August) | Append-only event log, both dates recorded |
| Swap-line networks / CIPS counts | Point-in-time disclosures, not continuously revised, but **frequently stale between disclosures** | Disclosure-as-of date vs. pull date (can lag disclosure by months in secondary sources) | Append-only event log; never interpolate between disclosed counts |

---

## C.8 The quarterly pipeline — from raw pulls to L15's reserve-diversification input

Matching the debt monograph's own Part-E-shaped algorithm (grids and the reduce-only clamp are
CONTRACT-frozen, not re-derived here):

1. **Registry load.** Validate `config/ladder.yaml L15_long_wave_fiscal` against
   `config/validator.py` before any pull.
2. **Pull raw fixtures** into `data/fixtures/P_reserve_composition/{cofer,wgc_gdt,rbi_wss,
   rbi_hyrmfer,fred_dtwexbgs,bis_eer,rbi_refrate,sdr_basket,swap_lines,cips}/{vintage}/...` — a
   genuinely new fixture family; no existing `ingest/pull_*.py` script covers any of COFER, WGC,
   RBI's HYRMFER, or the swap-line/CIPS trackers (see closing note). Manifest immediately
   (`python ingest/manifest.py data/`), every file keyed `(series_id, vintage_date, pull_date)`.
3. **CB-gold accumulation leg.** Pull WGC's quarterly central-bank-purchase estimate (C.2) *and*
   the IMF-reported figure separately, never merged; pull RBI's own WSS gold tonnage weekly and
   HYRMFER domestic/custody split semi-annually (C.3). Construct the composite leg as a **rolling
   12-month trailing sum of estimated global CB net purchases**, ranked against its own expanding-
   sample percentile (Contract's ≥4-observation warm-up floor applies — no percentile emitted
   until the sample clears it), *plus* RBI's own domestic-share trajectory as a India-specific
   confirm, not a separate weighted leg.
4. **COFER drift leg.** Pull the current-vintage COFER shares (C.1); compute the trailing 5-year
   annualized USD-share slope exactly as `cofer-RESULTS.md` RC3 already does, flagged by which
   methodology vintage (pre-/post-2025Q3) generated it, and by whether the window crosses the
   2015-18 reporting-pool break (in which case the allocated-coverage-ratio check from C.1 runs
   alongside it as a validity gate, not a silent pass-through).
5. **Composite construction.** The two legs are **enriched, reduce-only, never additive** — the
   Contract's Tier-C rule (§4) applied exactly as the debt monograph's captivity input applies it:
   a rising CB-gold-accumulation percentile *and* an accelerating (more negative) COFER USD-share
   slope can only pull the `long_wave_expression` gold-floor-attribution band toward its `[0.40,
   0.50]` upper end and lift the `conditional_gold_floor_lift_pp` toward its `[1, 2]` upper end
   (`ladder.yaml`) — neither leg, alone or combined, can push the *equity* regime score, because
   L15 has no regime-score seat at all.
6. **State representation.** Log as a phase object (level, velocity, quadrant, age-in-quadrant)
   per the 2026-09-01 states-as-phase-objects decision — not a scalar — for both legs
   independently before any combination.
7. **Manifest every derived fixture** (CB-gold-percentile panel, COFER-drift panel, the combined
   long-wave-expression band) as its own versioned, checksummed artifact; corrections append a new
   vintage row, never overwrite.
8. **Recalibration triggers**: a new COFER quarter (routine, ~1-quarter lag); a new WGC Gold
   Demand Trends edition (quarterly, ~4-5wk lag); a new RBI HYRMFER edition (semi-annual, ~1mo
   lag); any further IMF COFER methodology note (2025Q3-style); a new SDR quinquennial review
   (next due by end-Jul-2027 — a hard calendar date to pre-register against); any Fed/PBoC
   standing-swap-line addition or removal (event-based, not scheduled).
9. **Monitor**: quarterly refresh; annual review re-reads `cofer-RESULTS.md` RC1-RC3 with one more
   year of COFER data, checking specifically whether RC3's "no regime break through 2023Q1" finding
   still holds once 2022-26 sanctions-era quarters are in the post-2025Q3-revised series.

---

## C.9 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **True unreported central-bank gold, especially China's** | No mandatory IMF reporting rule exists; China's gap between officially declared (~2,300-2,350t) and independently estimated true holdings (~5,000-5,200t) is a >2x uncertainty band, not a rounding error; WGC's own estimate (244t, Q1 2026) already runs ~15x the IMF-reported figure (16t) for the *global* aggregate | Carry WGC's estimated figure as the working series, IMF-reported as a labeled floor, and the gap itself as an explicit, separately-tracked opacity indicator — never present a single "the" central-bank-gold-buying number |
| **Real-time reserve composition of any single central bank** (India's own included, at true real-time granularity) | COFER is quarterly with a lag and country-anonymized at the aggregate level; RBI's own gold-tonnage split is semi-annual; no central bank publishes intraday or even daily reserve-currency-composition detail, by design (confidentiality is structural to the whole reserve-management function) | Accept the quarterly/semi-annual cadence as the ceiling; never interpolate a smoother series than the primary disclosure supports |
| **Forward-looking swap-line utilization** (how much of a standing line would actually be drawn in the next stress episode) | Swap lines are contingent facilities; utilization is observed only ex post, during an actual drawdown (the 2020 Fed data is the only clean historical read); no free source publishes a forward utilization probability or capacity-stress-test result | Track the **network** (count, committed value, C.6) as the ex-ante capacity measure; treat any utilization estimate as a narrative, Stage-2-only judgment, never a Stage-1 quantitative input |
| **A single reconciled Gopinath-style invoicing-currency panel with a stable, versioned free download** | The academic dataset is real and periodically updated but distributed via working-paper appendices and author pages, not a maintained public repository or API | Treat each vintage as a dated, manually-pulled academic release; never assume continuity between editions without checking the coverage-country list and base year each time |
| **RBI's own aggregate ₹-value of trade actually settled via SRVAs** | RBI/FEDAI publish the account/participant count (a capacity proxy) but no aggregate flow-value series was found free this pass | Use the SRVA count as a participation proxy only, explicitly labeled as such, never as a trade-value substitute |

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §7 Known Prior #11 (no live network access this environment;
principal's-machine ingestion); `config/ladder.yaml` `L15_long_wave_fiscal` and
`long_wave_expression`; `research/cycles/reserve-deep/cofer-RESULTS.md` (RC0–RC3, the real-data
COFER trial this Part extends forward); `docs/CYCLE_ATLAS.md` entry 0.2; `docs/masterplan/
A-data-catalog.md` blocks G/J/K (RBI/IMF-FRED/gold — extended, not duplicated, by this Part);
`docs/masterplan/B-module-specs.md` §6.5 (`gold_score`'s `cb_buying_regime` input, the other
consumer of the WGC/RBI series sourced here); `research/cycles/debt-deep/partC-data.md` (the
sibling Part supplying L15's other two legs — debt level/slope, real-rate persistence — and the
structural PIT/vintage-table pattern this file follows).*


---

# PART D/E/F/H — Mathematics, algorithm, harvest map, knowledge ledger

# Part D — The mathematics (atlas 0.2)

## D1. Why reserve status is sticky: the coordination-game structure

Reserve choice is a coordination game: the value of holding/invoicing in currency i rises with
the share of others doing the same (liquidity externality). Payoff sketch: a reserve manager's
cost of currency i ≈ transaction cost c(share_i) − diversification benefit d_i, with c strictly
decreasing in share. Multiple equilibria follow — the incumbent persists far beyond its
fundamentals (inertia), and transitions, when they come, can be nonlinear (equilibrium switch).
Two design consequences: (i) the MEASURED drift (RC1: −0.51pp/yr, decelerating) is the base case,
not the tail case; (ii) the tail case (threshold crack) cannot be timed from the drift itself —
which is why the seat watches PRECONDITIONS (war finance, capital-control erosion, fiscal
exhaustion — Part B's scorecard) rather than extrapolating shares.

## D2. Measurement math for the composition input

The L15 composition leg is built from two series with different meanings:
- COFER USD share (quarterly, 1-quarter lag): drift = 5y rolling annualized Δshare, expanding
  percentile. The 2015-18 China phase-in mechanically LOWERED the unallocated pool and reshuffled
  shares — splice rule: shares computed on allocated reserves only, with the phase-in window
  flagged and the pre/post segments never compared point-to-point (Part C's hazard table).
- CB gold accumulation (WGC quarterly tonnage, world + EM cohort): 4-quarter rolling sum,
  expanding percentile. Gold is OUTSIDE COFER — the two series are complements (FX composition vs
  the exit-from-FX-entirely channel), exactly the impulse/level pairing pattern (credit D-chapter).
Composite: reduce-only Tier-C enrichment of L15's state — high (gold accumulation elevated AND
USD drift steep) can only push the fiscal-dominance state toward ON, never toward OFF (the clamp
arithmetic from the credit composite, reused verbatim).

## D3. What n≈2-3 permits

Two-to-three observed transitions ever (guilder→sterling→dollar, with the 1920s interregnum) —
no fitted anything. Admissible: precondition scoring against the case record (ordinal, hand-
scored, annually), the measured drift as context, and the live 2022+ gold wave as a WATCHED
series. Inadmissible: transition-probability models, "dollar-collapse hedges" sized beyond the
existing tail budget, any timing use. The statistics permit a checklist, not a clock.

# Part E — The algorithm (quarterly, inside L15)

```
STEP 1  COFER pull (quarterly, lag 1q) -> allocated shares -> USD 5y drift percentile
        [splice flags: 2015-18 phase-in; any future unallocated-pool jump]
STEP 2  WGC CB gold tonnage (quarterly) -> 4q rolling net purchases, world + EM cohort ->
        expanding percentile; RBI's own tonnage (WSS) tracked beside it
STEP 3  composition leg = clamp(reduce-only): max(0, w1*(USD-drift pctile - 0.5) +
        w2*(gold-accum pctile - 0.5)) -> enriches the L15 fiscal-dominance state
STEP 4  precondition scorecard (annual, hand-scored, versioned in the registry): war finance /
        fiscal exhaustion / capital-control erosion / deep-open challenger — each 0/1/2 with
        written evidence; scorecard changes are principal-signed
STEP 5  expression: unchanged L15 outputs (gold floor band, tail budget, conditional lift);
        this entry adds INPUTS, never new budget
MONITOR annual review re-reads RC1-RC3 with new data; the falsification/escalation conditions
        from Part B4 are the ONLY route to changing the gold-floor band, and only at annual
        reviews, never mid-drawdown (anti-capitulation lock applies)
FAILURE MODES: COFER reporter-composition changes masquerading as preference shifts;
        WGC estimate revisions (unreported buyers); narrative capture (a gold rally recruiting
        the transition story - the scorecard, not the price, is the input)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| L15 composition input | the two-leg reduce-only enrichment (D2) |
| Gold sleeve rationale | the CB-buying leg documented with evidence grades |
| Policy review memo | the annual precondition scorecard |
| Stage-2 red team | dedollarization narratives quarantined here with RC1's number attached |

Designs: **RV1** extend the COFER mirror forward each quarter (principal machine) and re-run
RC1-RC3 annually; **RV2** the EM-cohort gold share of reserves at market prices, 2000→ (WGC+IMF
IFS, free) — the direct measure of the 2022+ regime; **RV3** interwar reserve-share digitization
check (Eichengreen-Mehl-Chitu data, if a mirror surfaces) to put the 1920s interregnum in the
lesson with real numbers; **RV4** the stablecoin-reinforcement leg (USD-stablecoin float vs COFER
drift — the counterintuitive channel) as a watched Tier-C series once a free data path exists.

# Part H — Knowledge ledger (atlas 0.2)

**Established:** the four-role anatomy of reserve status; the inertia evidence; the measured
drift (−0.51pp/yr, no single challenger, NOT accelerating in FX shares through 2023Q1 — RC1-RC3);
the 2022+ CB gold wave as a real, large, ongoing shift in the RESERVE-ASSET mix (magnitudes per
Part B3 with [VERIFY] tags where WGC vintages differ).
**Pooled-prior [A]:** the precondition scorecard's factor list (from n≈2-3 cases).
**Awaits data:** COFER 2023Q2→ extension; RV2's EM gold-share series; India invoicing uptake.
**Unknowable:** whether/when a threshold cracks. The seat holds insurance sized for not knowing —
and its most likely failure mode is not the dollar's collapse but OUR narrative capture, which is
why the doom-cult countermeasures (debt Part G) apply here doubled.
