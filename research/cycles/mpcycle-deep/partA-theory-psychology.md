# The Monetary-Policy Cycle Deep Dive — Part A & Part G

Part A: Theory — the policy rate as public information, the transmission state as the private one ·
Part G: Operator psychology · v1.0 · 2026-09-02 · Atlas entry 2.6 (`docs/CYCLE_ATLAS.md` row 82;
ladder seat `L6_monetary_stance`, `config/ladder.yaml`). SEATED inside the `macro_credit_block`
alongside `L10_credit_block`, `L11_capex_cycle`, `L12_realestate_medium_cycle` (`docs/DESIGN.md`
§4.1–4.2). Complements, never duplicates, `research/dossiers/08-india-mid-cycles.md` (D08, esp. I1,
I2, and Edge A — the dossier's own survival argument for this exact seat) and this program's own
`research/register/trial-ledger.md` (entries MP1–MP3, pre-registered 2026-09-02 under the BC2
standing warning; **status at time of writing: pending** — §A.4 states this plainly rather than
guessing at a result). Evidence base: this file + D08 + `research/dossiers/03-credit-financial-
cycle.md` (D03, the credit-block sibling this seat shares its budget with) + `docs/cycles/
01-credit-cycle.md` (the assembled L10 monograph, whose Bernanke-Gertler-Gilchrist financial-
accelerator material is a distinct, complementary mechanism from this file's bank-lending-channel
material — never re-derived here). Style and depth calibrated to `research/cycles/fincycle-deep/
partA-theory-psychology.md`. Status: theory and citations verified in this session (see per-section
citation blocks); India coefficients await MP1–MP3 and the wider data phase.

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)

This file assumes the ladder's frozen construct as given: L6 is a **lagged (~1-year) loose/tight
regime input, never a same-day event trade** (`ladder.yaml` role line) — it reads the RBI DBIE repo
path against a 12–24-month `tau_half` prior, Tier B on n≈4–5 marginal domestic round trips (D08
I1), sharing the 20%-of-regime-score `macro_credit_block` budget with L10, L11 and L12 under the
de-duplication rule (`DESIGN.md` §4.2) — never a separate allocation. Part A supplies the
theoretical machine that construct compresses into one lagged classification, honest about what the
compression discards. Part G turns to the desk watching the single most-covered, most-anticipated,
most over-interpreted event on the Indian macro calendar — six times a year, forever — and asks what
a regime seat is actually protecting them from doing about it.

---

## PART A — Theory: the object nobody can arbitrage is the one nobody is watching

### A.1 The object

**(i) The distinction the seat is built on.** Every monetary-policy cycle contains two objects that
are easy to conflate and must not be: the **policy decision** — a repo-rate print, a stance word
("accommodative," "neutral," "withdrawal of accommodation"), a vote count, released to the entire
world simultaneously at a published time — and the **transmission state** — the slow, partial,
compounding effect that decision has on bank balance sheets, loan pricing, credit growth, investment,
and ultimately equity cash flows and discount rates, over the following several quarters. The first
object is, by construction, **public and unarbitrageable**: nobody on this desk, or any desk, holds
private information about what the Monetary Policy Committee (MPC) will announce at 10:00 IST on a
scheduled Thursday, and a large, well-capitalized, high-frequency market (rates futures, overnight
index swaps, government bonds) exists specifically to price that announcement within seconds of its
release. The second object is exactly the opposite: it is publicly *knowable in principle* — the
mechanism is not secret — but it cannot be **traded away** by knowing it, because acting on the
knowledge requires the same slow machinery (bank balance-sheet repricing, loan-reset cycles, credit
growth building or easing) to actually run its course. **This is the design sentence L6 is built to
encode**: the seat is not a bet on what the RBI will do next meeting, and it is not a bet on how
markets will react to what the RBI just did — both of those are the first object, priced instantly
and already arbitraged by faster, better-resourced participants. L6 is a bet on **where the economy
already sits** in the transmission of decisions already taken, twelve-to-eighteen months ago, that
have not yet finished working through the system — a state variable, not an event trade.

**(ii) The event-study literature, at its strongest.** The claim that policy *announcements* price
near-instantaneously and near-completely is not asserted here; it is one of the most replicated
findings in monetary economics, and the program's own no-invented-citations rule is easiest to honor
where the literature is this settled. **Kuttner, Kenneth N. (2001), "Monetary Policy Surprises and
Interest Rates: Evidence from the Fed Funds Futures Market"** (*Journal of Monetary Economics*
47(3): 523–544) **[Verified]** is the foundational high-frequency identification: using the change
in the fed funds futures rate on the day of an FOMC decision as a market-based measure of the
*surprise* component of a rate change (separating it from the anticipated component priced in
beforehand), Kuttner shows that longer-term interest rates respond strongly to the surprise
component of a policy move and only weakly, if at all, to the anticipated component — a clean
demonstration that markets price what they know in advance *before* the announcement, leaving only
the genuinely new information to move prices on the day itself. **Gürkaynak, Refet S.; Sack, Brian
& Swanson, Eric (2005), "Do Actions Speak Louder Than Words? The Response of Asset Prices to
Monetary Policy Actions and Statements"** (*International Journal of Central Banking* 1(1): 55–93)
**[Verified]** extends this decisively: a single "surprise" factor (the rate-change surprise alone)
is *not* sufficient to explain the full asset-price response to an FOMC announcement — a second,
independent **"path" factor**, capturing the surprise content of the accompanying statement about
the *future* policy path, is needed, and the two factors move asset prices through economically
distinct channels. The synthesis these two papers hand down is exactly the one L6 must respect: **on
the announcement day itself, essentially everything knowable — the rate decision and the forward
guidance — is priced within minutes**, by participants (rates desks, OIS market-makers, bond
dealers) whose entire business model is being faster at this specific task than a multi-cycle
portfolio model could ever be. There is no version of "predict the next RBI move and trade the
surprise" that survives this literature; the program does not attempt one.

**(iii) India, evidence-graded honestly.** Direct, India-specific high-frequency event-study evidence
is thinner than the US/advanced-economy literature but is not absent. **Lakdawala, Aeimit &
Sengupta, Rajeswari (2021, working paper; published 2025), "Measuring Monetary Policy Shocks in
Emerging Economies: Evidence from India"** (IGIDR Working Paper WP-2021-021; *Journal of Money,
Credit and Banking* 57(2–3), March–April 2025, pp. 407–437) **[Verified — publication and venue
confirmed by search; the paper's own headline empirical magnitudes were not independently re-pulled
this session, flagged VERIFY below]** constructs monetary-policy-shock measures for India from
high-frequency derivatives-market data around RBI announcements and studies their transmission,
finding that Indian bond and equity markets react strongly to the identified shocks, with notable
heterogeneity across different RBI-governor regimes **[VERIFY: exact effect sizes, the governor-
regime heterogeneity's magnitude, and whether the "notable heterogeneity" finding itself survives at
a stated statistical bar — not independently confirmed this session]**. This is corroborated in
kind, not in exact figure, by a strand of RBI-affiliated and market-structure research on
decomposing OIS-rate movements around policy days into "target" and "path" factors in the Kuttner/
Gürkaynak-Sack-Swanson spirit **[VERIFY: primary RBI working-paper citation for the India OIS
target/path decomposition — located via secondary search this session, not independently confirmed
as a single numbered publication]**, and by the qualitative, widely reported observation that under
the post-2016 MPC regime specifically, genuine "surprises" (decisions diverging from a pre-meeting
market-implied consensus, itself readable off OIS pricing) have become **rare** rather than common —
consistent with an increasingly transparent, well-communicated MPC successfully anchoring
expectations *before* the meeting, which is itself the mechanism by which the announcement becomes
even more thoroughly pre-priced than a surprise-prone regime would be **[VERIFY: the "rarity of
surprises 2016–2023" claim's precise operationalization and count — drawn from secondary discussion
of this research strand, not independently re-derived]**. None of this VERIFY-tagged uncertainty
weakens the design conclusion; if anything it strengthens it, because even the *weakest* honest
reading of this evidence — "India's policy announcements are reasonably well anticipated and quickly
priced by the OIS/bond/equity complex" — is already sufficient to rule out same-day event trading as
this program's edge (§A.4).

**(iv) Why the seat is built exactly where it is built.** Given (i)–(iii), the only defensible
design choice is the one the ladder already makes: L6 does not attempt to price the announcement; it
classifies the **stance** — loose or tight, on RBI's own DBIE repo-path history — and applies it only
after a lag calibrated to how long transmission structurally takes (A.2–A.3), never same-day. Three
consequences follow directly, each already load-bearing in `ladder.yaml`. **First**, the seat's
`role` field ("lagged (~1y) loose/tight regime input; never same-day event trade") is not a
stylistic caution — it is the entire survival argument in one sentence, and every subsequent section
exists to justify it from mechanism and evidence rather than assert it. **Second**, the Tier-B
classification with n≈4–5 marginal domestic round trips (D08 I1, §A.3v) reflects that the
*stance-classification* input is measured on a clean, free, continuously-available repo series, even
though the *cycle-counting* question sits right at the CONTRACT's clock-test boundary, exactly as
documented for the sibling credit and financial-cycle seats. **Third**, and most important for what
follows: because the announcement is unarbitrageable and the transmission lag is the only source of
durable information, **the remaining research question is *how long, through what channels, and with
what confidence* that lag actually runs** — the subject of A.2 (general theory) and A.3 (India's own
machinery).

---

### A.2 Transmission theory, strongest form

**(i) The four channels, named and sourced.** The textbook transmission mechanism decomposes a
policy-rate change into (at least) four distinct channels through which it eventually reaches output,
inflation, and — for this program's purposes — equity cash flows and discount rates. **The interest-
rate channel** is the direct, textbook IS-curve effect: a higher real policy rate raises the cost of
current consumption and investment relative to future consumption, cooling demand mechanically and
immediately in the pure New-Keynesian telling — though even this "fastest" channel is slowed in
practice by the repricing lags documented in A.3. **The credit (bank-lending) channel** is the
mechanism this file leans on most heavily, because India's financial system is bank-dominated (A.2iii
below): **Bernanke, Ben S. & Blinder, Alan S. (1988), "Credit, Money, and Aggregate Demand"**
(*American Economic Review* 78(2): 435–439) **[Verified]** is the founding formalization, modifying
the standard IS-LM apparatus to treat bank loans and bonds as *imperfect substitutes* rather than
perfect ones — meaning a policy tightening that drains reservable bank deposits does not simply cause
a one-for-one substitution into bond finance for credit-dependent borrowers (small firms, households,
in India's case a large share of even mid-sized corporates), because bank credit and market credit are
not interchangeable at the borrower level. **Kashyap, Anil K. & Stein, Jeremy C. (2000), "What Do a
Million Observations on Banks Say about the Transmission of Monetary Policy?"** (*American Economic
Review* 90(3): 407–428) **[Verified]** supplies the decisive micro-evidence for *why* the channel is
real and heterogeneous: using quarterly data on essentially every insured US commercial bank,
1976–1993, they show the lending response to a policy tightening is concentrated in banks with **less
liquid balance sheets** (a low ratio of securities to assets — banks that cannot simply run down a
securities buffer to protect their loan book), and this effect is driven overwhelmingly by smaller
banks — direct support for a genuine **bank-lending channel** distinct from the pure interest-rate
channel, and a mechanism this program's own L10 credit-block composition input (bank+NBFC aggregate,
per `docs/cycles/01-credit-cycle.md`) is built to be sensitive to. **The exchange-rate channel**
operates through uncovered interest parity and capital flows: a tightening that widens the domestic-
foreign rate differential should, all else equal, appreciate the currency, cheapening imports and
raising the relative price of exports — a channel D08's own Edge-A framing (§A.1iv above) and this
program's own India Khundrakpam-Jain replication (A.3iii below) both find comparatively **weak** in
India specifically, for reasons tied to capital-account management and the global-financial-cycle
seat (L9) this file does not re-litigate. **The asset-price/wealth channel** operates through equity
and property valuations: a rate change alters the discount rate applied to future cash flows
(directly relevant to every equity book this program runs) and, via wealth effects, household
consumption — the channel this program's own drawdown machinery (D04) and the L12 real-estate seat
(`research/cycles/fincycle-deep/partA-theory-psychology.md`) are built to price from the *other*
side of the same mechanism.

**(ii) "Long and variable lags," and the modern estimates.** **Friedman, Milton (1961), "The Lag in
Effect of Monetary Policy"** (*Journal of Political Economy* 69(5): 447–466) **[Verified]** is the
origin of the framing this entire seat is named for: Friedman's central, still-standing claim is that
monetary policy affects economic conditions only after a lag that is **both long and variable** —
variable specifically meaning the lag's *length* itself depends on prevailing economic and financial
conditions, not a fixed number of quarters that can be looked up once and applied forever. This is
precisely why the ladder's own `tau_half` for L6 is stated as a **range** (12–24 months) rather than a
point estimate, and precisely why the `tau_half_drift_policy` block (`ladder.yaml`) subjects every
ladder entry, L6 included, to living re-estimation rather than a frozen constant — Friedman's own
"variable" half of the claim is the reason a frozen point value would misrepresent the very mechanism
being modeled. Two modern methodological advances have since sharpened *how* this lag is measured
without contradicting Friedman's basic claim. **Romer, Christina D. & Romer, David H. (2004), "A New
Measure of Monetary Shocks: Derivation and Implications"** (*American Economic Review* 94(4):
1055–1084) **[Verified]** solves the central identification problem — a naive regression of output on
the policy rate confuses genuine policy shocks with the Fed's own *endogenous response* to
information about the economy it already expects — by combining the FOMC's internal, real-time
forecast records (the Greenbook) with the narrative record of policy intentions, isolating the
component of each rate change that is **not** explained by the Fed's own contemporaneous forecast.
Their identified shocks show policy has "large, relatively rapid, and statistically significant"
effects on both output and inflation, *stronger* than conventional measures suggest — naive measures
were **understating**, not overstating, transmission's true speed once endogeneity is purged. **Jordá, Òscar (2005),
"Estimation and Inference of Impulse Responses by Local Projections"** (*American Economic Review*
95(1): 161–182) **[Verified]** supplies the now-standard estimation tool for *tracing out* a lag
profile without committing to a single parametric VAR's implied dynamics: local projections estimate
the impulse response at each horizon directly, by regression, rather than extrapolating a VAR's
one-step dynamics arbitrarily far into the future — a technique now the field standard precisely
because it is more robust to misspecification and handles the highly nonlinear, state-dependent
responses a variable lag structure implies. Applying this machinery across the advanced-economy
literature, the **consensus finding is a peak transmission effect on output arriving roughly
12–24 months after a policy-rate shock**, with the effect on inflation typically peaking somewhat
later still — the exact window this program's own L6 `tau_half` prior (12–24 months) sits inside,
independently corroborated for India specifically in A.3iii below.

**(iii) Why bank-dominated systems transmit slower, and via quantities.** The channel decomposition
in (i) is not uniform across financial systems, and the difference matters directly for how India's
own seat should be built. **Cecchetti, Stephen G. (1999), "Legal Structure, Financial Structure, and
the Monetary Policy Transmission Mechanism"** (NBER Working Paper 7151; also *Federal Reserve Bank of
New York Economic Policy Review* 5(2): 9–28) **[Verified]** documents that cross-country differences
in financial structure — bank-dominated versus market-based systems, themselves traceable to
differences in legal structure and creditor protection — are a **proximate cause** of national
asymmetries in how monetary policy transmits: an economy where firms and households obtain most of
their external finance from banks (rather than issuing bonds or equity directly to the market)
transmits policy predominantly through the credit channel of (i), which operates on the **quantity**
of credit banks are willing and able to supply, not merely its **price** — banks facing a tightening
do not simply raise the rate uniformly to all borrowers; balance-sheet-constrained banks (Kashyap-
Stein's finding) *ration* credit at the margin, a quantity adjustment a pure price/interest-rate
channel would miss entirely. This distinction is exactly the euro-area/India-versus-US contrast this
section is built to state plainly: the US financial system is comparatively market-based (large,
liquid corporate-bond and commercial-paper markets give firms an outside option banks cannot fully
foreclose), so US transmission runs comparatively faster and more through prices; **the euro area and
India are each, for different institutional reasons, comparatively bank-dominated systems** — Indian
corporate and household credit is overwhelmingly a bank(+NBFC) balance-sheet phenomenon, precisely the
premise D08's Edge-A survival argument already states (§A.1iv) and precisely why India's own
transmission-speed estimates (A.3iii) sit toward the slower, more partial end of the international
range, and why this program's own L10 credit-block composition input and L6's stance classification
are, correctly, built to interact rather than operate as independent signals (A.2iv below).

**(iv) The risk-taking channel — tying L6 to L10's world.** A fifth channel, more recently
formalized, is the one that most directly explains *why* a monetary-cycle seat and a credit-cycle
seat must share one budget rather than be independently sized (`DESIGN.md` §4.2). **Borio, Claudio &
Zhu, Haibin (2012), "Capital Regulation, Risk-Taking and Monetary Policy: A Missing Link in the
Transmission Mechanism?"** (BIS Working Paper 268, first circulated 2008; published *Journal of
Financial Stability* 8(4): 236–251) **[Verified]** coins and formalizes the **risk-taking channel**:
monetary policy affects not only the quantity and price of credit but the financial system's own
**perception and pricing of risk** — a sustained period of low policy rates can, through its effect on
valuations, income, and cash-flow measures used in risk models, lead financial intermediaries to
take on **more risk** than they otherwise would, independent of any pure portfolio-rebalancing or
"search for yield" story that operates purely through relative asset returns. **Jiménez, Gabriel;
Ongena, Steven; Peydró, José-Luis & Saurina, Jesús (2014), "Hazardous Times for Monetary Policy: What
Do Twenty-Three Million Bank Loans Say About the Effects of Monetary Policy on Credit Risk-Taking?"**
(*Econometrica* 82(2): 463–505) **[Verified]** is the paper's definitive micro-evidence, using
Spain's exhaustive credit register (23 million bank-loan observations) with a two-stage design that
separates credit-supply composition from volume and demand effects: they find lower overnight rates
induce **less-capitalized banks specifically** to grant more loan applications to **ex ante riskier
firms**, with larger volumes and fewer collateral requirements attached — a precisely-identified
demonstration that an easing cycle changes not just *how much* credit is supplied but *whose risk* the
banking system is willing to underwrite, exactly the mechanism that eventually shows up, with the
~1-year-plus lag this section has established, as the credit-boom composition-quality deterioration
`docs/cycles/01-credit-cycle.md`'s own L10 construction is built to detect. **For this seat**: the
risk-taking channel is the theoretical bridge between L6 (the policy-stance input) and L10 (the
credit-quantity-and-quality output) — a sustained loose stance does not merely lower borrowing costs
mechanically, it changes the *composition* of what gets lent, which is precisely why the two seats'
information overlaps enough to require a shared budget rather than double-counting the same
underlying regime twice, and precisely why L6's `inputs: []` in `ladder.yaml` while L10 lists
`inputs: [L6_monetary_stance]` is the correct DAG direction — stance precedes and conditions the
credit-quality state, not the reverse.

---

### A.3 The Indian transmission machinery, specifically

**(i) The operating framework's evolution.** Before the modern single-rate corridor existed, RBI's
operative tool was the **Bank Rate**, supplemented from **April 1999 (interim) and fully from 2000**
by the **Liquidity Adjustment Facility (LAF)** — a repo/reverse-repo window through which RBI injects
or absorbs banking-system liquidity daily, the architecture this program's own debt-supercycle
monograph documents as the modern successor to the pre-1990s CRR/SLR-based repression apparatus
(`research/cycles/debt-deep/partC-data.md` §C.8–C.11). RBI adopted the modern **single-repo-rate
corridor in May 2011** **[Verified in outline per D08 I1; exact 2011 corridor-adoption mechanics not
independently re-pulled this session]**, and in **April 2016** narrowed the corridor from a wide
±100 basis points to a tight **±50 basis points** around the repo rate — reducing the Marginal
Standing Facility (MSF, added **2011** as the upper bound, the rate at which banks can borrow against
government-securities collateral when short of liquidity) by 75bp and raising the reverse-repo rate
by 25bp, explicitly to achieve finer alignment of the operative overnight call-money rate with the
repo rate itself **[VERIFY: exact 2016 corridor-narrowing magnitudes and date — sourced from
secondary aggregator search, not a directly-pulled RBI notification]**. This corridor was
**asymmetrically widened during the COVID liquidity surge** (the MSF borrowing limit raised from its
usual 2% of net demand-and-time-liabilities to 3%, phased back through 2022) **[VERIFY: exact
widening parameters and restoration timeline]**, and the reverse-repo leg was itself replaced on
**8 April 2022** by the **Standing Deposit Facility (SDF)** — a **collateral-free** overnight liquidity-absorption tool, set 25bp below
the repo rate, that lets RBI absorb surplus system liquidity without needing to hand banks government
securities in return, closing a technical gap the reverse-repo mechanism could not (the reverse repo
required RBI to have sufficient securities on its own balance sheet to offer as collateral, a genuine
operational constraint during periods of very large surplus liquidity) **[Verified — SDF launch
date, mechanism, and rate spread confirmed by search]**. **For this seat**, the corridor's width and
composition are not directly consumed as an L6 input (the seat reads the repo *path*, per
`ladder.yaml`'s `indicator` field), but they matter for interpretation: a narrower, better-anchored
corridor is itself evidence of an operating framework increasingly capable of keeping the *overnight*
rate close to the policy signal — which is a precondition for the repo rate to be a meaningful stance
proxy at all, rather than a number banks can systematically arbitrage around via the corridor's own
width.

**(ii) The lending-rate regimes as the transmission-bottleneck story.** If the LAF corridor governs
how faithfully the *overnight interbank* rate tracks the repo signal, a separate and more consequential
question is how faithfully **bank lending rates to the real economy** track it — and India's
regulatory history here is best read as a sequence of admissions that the previous regime transmitted
poorly. Banks priced loans off the **Benchmark Prime Lending Rate (BPLR)** until RBI introduced the
**Base Rate system, effective 1 July 2010** **[Verified — replacement date confirmed by search]**,
explicitly because BPLR's opacity (each bank set its own benchmark with limited transparency into the
methodology, and could and did lend *below* the benchmark to favored borrowers, so the published rate
carried little information about actual transmission) had "hampered the efficacy of the monetary
transmission mechanism" in RBI's own stated reasoning. The Base Rate system in turn proved
insufficiently uniform — banks retained latitude in how they calculated their cost of funds, with
"arbitrary elements" creeping into bank-specific formulas that again obscured genuine transmission —
prompting RBI to mandate the **Marginal Cost of Funds based Lending Rate (MCLR), effective 1 April
2016** **[Verified — effective date confirmed by search]**, a more standardized, marginal- (rather
than average-) cost-based methodology intended to make lending rates move faster and more
predictably with the policy rate. Yet even MCLR did not solve the problem: RBI's own **August 2019**
assessment found that despite repo-rate cuts, banks' MCLR-linked lending rates were **not** declining
proportionately **[Verified — RBI's own 2019 assessment confirmed by search]** — the direct proximate
cause of the fourth and most consequential reform, RBI's mandate that banks link **new floating-rate
retail and MSME loans to an External Benchmark (EBLR)** — typically the repo rate itself, or a
market-observable rate like a T-bill yield — **effective 1 October 2019** **[Verified — mandate and
effective date confirmed by search]**. The adoption pace itself is the honest measure of how binding
the old regime had been: the share of outstanding loans linked to external benchmarks rose from just
**2.4% in September 2019 to 28.5% by March 2021** **[Verified — figures sourced from RBI's own
"Monetary Transmission in India" reporting, cross-confirmed via secondary aggregation this session]**
— meaning even four years after MCLR's introduction and roughly eighteen months into the EBLR mandate,
the **large majority** of outstanding credit was still priced off internal benchmarks that had already
been diagnosed as transmitting poorly, a fact directly relevant to why this seat's own lag prior
(12–24 months) sits toward the *longer* end of the international consensus range established in A.2ii:
**each successive reform (BPLR → Base Rate → MCLR → EBLR) is itself dated evidence that the
mechanism this section's theory describes was, at each point in India's history, only partially
working** — a structural reason, not merely a data artifact, for the lag this program's seat is built
to respect rather than assume away.

**(iii) Verified transmission estimates for India — the primary citation the ladder itself asks
for.** `ladder.yaml`'s own `changes_if` field for L6 names, as one of two conditions that would move
the seat's confidence, "a primary RBI DEPR citation" for the transmission-lag range D08 states only
as a widely-repeated, imprecisely-sourced figure. This file supplies it. **Khundrakpam, Jeevan Kumar
& Jain, Rajeev (2012), "Monetary Policy Transmission in India: A Peep Inside the Black Box"** (RBI
Working Paper Series, WPS (DEPR) 11/2012) **[Verified — paper, authors, series number and headline
finding confirmed by search]** estimates a structural VAR on Indian quarterly data (1996–97:Q1 to
2011–12:Q1) to decompose the relative importance of the interest-rate, credit, asset-price and
exchange-rate channels (the same four-channel taxonomy this file's A.2i draws on) for India
specifically, finding the **interest-rate, credit, and asset-price channels are all significant,
while the exchange-rate channel is comparatively weak** — directly corroborating this file's A.2iii
claim about India's bank-dominated transmission structure, from India's own data rather than an
imported prior. The companion estimate this dossier and the ladder both lean on for the lag's
*magnitude* — **Mohanty, Deepak (2012), "Evidence of Interest Rate Channel of Monetary Policy
Transmission in India"** (RBI Working Paper Series, WPS (DEPR) 06/2012) **[Verified — paper, author
and series number confirmed by search]** — estimates a quarterly structural VAR finding that a
policy-rate change affects **output growth with a lag of roughly two quarters** and **inflation with
a lag of roughly three quarters**, with **both effects persisting for eight to ten quarters**
thereafter **[Verified — headline finding confirmed by search, cross-corroborated by the
Khundrakpam-Jain 11/2012 companion paper's own reported lag structure]**. Read together, these two
RBI DEPR papers are the honest primary-source answer to the atlas's own "2–6 quarter" range (`docs/
CYCLE_ATLAS.md` row 82): the **first, partial** effect on real activity begins inside two to three
quarters, the **fuller** effect on inflation and the persistence of both effects run out toward
eight-to-ten quarters (two-to-two-and-a-half years) — a range this program's own L6 `tau_half` prior
(12–24 months) sits centrally inside, and specifically justifies the "never same-day" design rule:
even the *fastest* documented channel (interest-rate) takes multiple quarters to show up in the real
variables this program's equity book ultimately cares about, let alone the credit-quantity channel
A.2i and A.2iv describe. A further, separately estimated pass-through figure sharpens the *bank*
leg specifically: complete pass-through from the repo rate to the call-money rate runs roughly
**3.2 quarters**, to the bank deposit rate roughly **2.9 quarters** **[VERIFY: exact figure and
primary source — sourced from a secondary industry-study aggregation this session, not confirmed
against a single named RBI/committee report]**, and the **weighted-average lending rate on fresh
rupee loans** rises only **26–47 basis points per 100bp of policy tightening** even under MCLR
**[VERIFY: same caveat]** — a materially **incomplete** pass-through, itself further evidence for
(ii)'s lending-rate-regime story: transmission has never been full, one-for-one, under any of the
four lending-rate regimes tried.

**(iv) CRR as the quantity tool, and the liquidity-versus-rate distinction.** The **Cash Reserve
Ratio (CRR)** — the share of a bank's net demand and time liabilities that must be held, non-interest-
bearing, with RBI — is this section's clearest illustration of a **quantity**, rather than **price**,
instrument, and its own history is a direct data point for A.2iii's channel-decomposition claim:
`research/cycles/debt-deep/partC-data.md` §C.8 documents CRR's own repression-era role (a statutory
15% ceiling-and-floor regime, 1934 RBI Act framework) and its **2006 deregulation** (the RBI
(Amendment) Act, 2006, removing both the 3% floor and 20% ceiling, giving RBI unrestricted discretion
to set CRR anywhere) — since that reform, CRR moves have functioned as a genuinely separate lever
from the repo rate itself: a CRR cut injects liquidity and expands lendable resources directly,
without necessarily moving the *price* of credit at all, exactly the quantity-channel mechanism
Bernanke-Blinder's (A.2i) and Kashyap-Stein's (A.2i) theory describes, and the identical logic
`research/cycles/buscycle-deep/partB-cases-dating.md`'s own GFC-response case documents: RBI's
**2008 response cut the repo rate from 9% to 4.75% while simultaneously cutting CRR**, a combined
price-and-quantity easing exactly matching the theory's own prediction that a bank-dominated system's
credit supply responds to both levers, not the rate alone. This motivates the section's second and
arguably more important distinction for a desk building a *stance* classifier: the **repo rate is
not, by itself, the state variable banks actually feel**. **System liquidity — whether the banking
system is in aggregate a net borrower from RBI's LAF window ("deficit") or a net depositor into it
("surplus")** — is at least as consequential for the actual cost and availability of bank funding as
the announced repo level, because the **weighted average call rate (WACR)**, the rate banks actually
transact at overnight, tracks the repo rate loosely in deficit conditions and can sit meaningfully
*below* it in surplus conditions, changing the effective stance banks experience without any MPC
decision at all. A nominally "tight" repo level delivered into a large system-liquidity surplus
transmits materially less tightening than the same repo level delivered into a deficit — which is
exactly why `docs/CYCLE_ATLAS.md` §15's own liquidity-family mapping table already flags **RBI system-
liquidity (LAF net surplus/deficit position) as a measurement enrichment to L6's own indicator list**,
consumed alongside the repo path itself rather than as a separately budgeted seat: it sharpens the
existing stance classification (is the *effective*, liquidity-adjusted stance looser or tighter than
the announced repo level alone implies) without creating new allocation authority the de-duplication
rule (`DESIGN.md` §4.2) would then have to arbitrate.

**(v) The MPC era — what changed, measurably.** The **Monetary Policy Committee (MPC)** was
constituted under the amended RBI Act in **2016**, with an explicit **flexible inflation-targeting
(FIT)** mandate — CPI inflation at **4% with a ±2% tolerance band** — formalized by the **February
2015 Monetary Policy Framework Agreement** and given statutory force via the **2016 RBI Act
amendment**; the government's own inflation-target notification ran **5 August 2016 to 31 March
2021** (subsequently renewed), and the **first MPC meeting was held in October 2016** **[Verified —
institutional chronology, the 4%±2% band, and the 2016 amendment date confirmed by search; the
precise February 2015 agreement date and August 2016 notification specifics carry the same
[VERIFY] status D08 I1 already flags]**. What changed *measurably*, as opposed to institutionally, is
the honest test this section owes the reader rather than merely asserting a before/after narrative.
On **inflation**, the shift is large by any account this session could locate: average CPI inflation
fell from roughly **7–8.5%** in the years immediately preceding FIT adoption to roughly **4.6–4.9%**
in the FIT era, and — the volatility claim that matters more for a *regime* classifier than the level
claim — the **standard deviation of headline CPI inflation fell from an estimated ~2.8 percentage
points pre-2016 to roughly ~1.1–1.5 points post-2016** **[VERIFY: exact figures and methodology —
multiple secondary sources converged on a fall of this rough magnitude and direction this session,
but the precise point estimates differ by source and none was independently re-derived from a single
primary RBI/EPW publication pulled directly]**. This is the same **era-stickiness** finding this
program's own inflation-regime monograph already establishes independently on the much longer JST
panel — `research/cycles/inflation-deep/partAB-theory-evidence.md`'s IR2 result finds inflation
*regimes*, not individual prints, persist at **81%** year-over-year pooled across 18 countries since
1871 — corroborating, from an entirely different dataset and era, that India's post-2016 low-and-
stable inflation reading is exactly the kind of **regime** object that literature predicts, not a
guarantee (§G.5 below returns to this point as an operator hazard). On the **rate-cycle amplitude**
question — whether MPC-era hiking/easing cycles have themselves become shallower or shorter than the
pre-2016 record — the honest answer is that this session located **no single, independently verified
India-specific study quantifying rate-cycle amplitude before versus after 2016** distinct from the
inflation-volatility finding above; the repo-path chronology itself (D08 I1: 9.00% Jun 2008 peak,
4.75% 2009 trough, 8.50% Oct 2011, a long bumpy easing to 5.15% Oct 2019, 4.00% COVID floor held ~22
months, 6.50% by Feb 2023, easing again from Feb 2025) shows both pre- and post-MPC cycles spanning
several hundred basis points, so **this file explicitly declines to assert a rate-cycle-amplitude
compression claim it cannot support** — flagged **[VERIFY: whether MPC-era rate-cycle amplitude is
measurably narrower than the pre-2016 record — not established this session; a genuine open research
question, not a settled fact quietly assumed]**, precisely the CONTRACT §12 discipline of tagging
rather than smoothing over a gap.

---

### A.4 What the desk harvests and refuses

**(i) Harvest — the lagged regime, and why it survives.** Three things, and only three, cross into
the traded book. **First, the lagged loose/tight regime itself** — L6's own seat, already fully
priced into the `macro_credit_block` per `ladder.yaml` — survives being fully public for exactly the
reason A.1 establishes: the announcement is arbitraged instantly by faster capital, but the
**transmission lag itself is not a piece of information a faster trader can buy** — it is a structural
property of a bank-dominated credit system (A.2iii, A.3ii–iii) that takes calendar time to unwind,
regardless of who knows the repo rate. This is CONTRACT §5's "survival argument" answered explicitly:
category **(iv) institutional constraint** — the bank-lending channel's own balance-sheet and
loan-reset mechanics are the constraint, not an informational edge anyone might close by publishing
this file. **Second, campaign persistence** is the specific reason a monetary *stance* is correctly
modeled as a **regime**, not a sequence of independent events: MP3, pre-registered in `research/
register/trial-ledger.md` (`P(sign of Δstir_{t+1} = sign of Δstir_t)`, pooled across the JST cross-
country analogue panel) asks directly whether tightening and easing campaigns persist — i.e., whether
knowing this meeting's direction tells you something about next meeting's direction beyond a coin
flip — and the answer, whatever it turns out to be, is the empirical justification for treating
"stance" as a multi-meeting state rather than re-deriving it fresh at every MPC decision. This mirrors,
deliberately, the persistence findings already banked elsewhere in this program: IR2's 81% pooled
inflation-era stickiness (§A.3v) and BC3's 77% pooled growth-state stickiness
(`research/register/trial-ledger.md`, Atlas 2.3 business-cycle entries) — if MP3 lands anywhere near
that range, it confirms monetary campaigns belong in the same "regimes persist, prints don't" family
this program has now measured three times independently. **Third, the transmission-lag profile
itself** — MP2, also pre-registered, measures the pooled cross-correlation of a one-year policy-rate
change with real-credit growth at leads/lags 0 through +3 years, a direct empirical check (on the
JST cross-country analogue panel, since India alone cannot supply enough independent observations) of
where the *peak* transmission effect actually sits — the exercise that calibrates, rather than merely
asserts, this seat's ~1-year lagging convention against something other than the Khundrakpam-Jain/
Mohanty RBI DEPR estimates (A.3iii) alone.

**(ii) Refuse — four moves explicitly out of bounds.** **Same-day event trades** — buying or selling
around the MPC announcement itself, on the theory that the market has mispriced the decision or the
accompanying statement — are excluded by the ladder's own role line and by A.1's entire argument: this
is precisely the object Kuttner (2001) and Gürkaynak-Sack-Swanson (2005) show is priced within minutes
by faster capital, and no version of this program's multi-cycle, weekly-to-monthly-cadence design has
any business competing with an OIS market-maker's millisecond reaction speed. **MPC-meeting
prediction** — building a model to forecast the *next* decision ahead of the market's own OIS-implied
consensus — is excluded for the identical reason, compounded by the finding (§A.1iii) that genuine
surprises have become rare precisely because the MPC's own communication has gotten better at
pre-anchoring expectations; a forecasting edge against an already-well-anchored consensus is a thinner
edge than the same exercise would have offered a decade ago, not a thicker one. **OIS-curve alpha** —
trading the term structure of India's overnight-index-swap market on the theory that it misprices the
future repo path — is excluded as **decayed and crowded**: this is a professional rates-desk product,
continuously arbitraged by dedicated participants with cheaper funding and faster infrastructure than
this program will ever have, the same "no argument we beat professional desks at their own book"
verdict `docs/CYCLE_ATLAS.md` §7 already reaches for options-premium harvesting (D12) and applies here
with equal force. **"RBI put" assumptions** — the belief that RBI will always, eventually, ease
enough to rescue equity valuations from a serious drawdown — are excluded on first-principles grounds
this file's own evidence undercuts directly: A.3iii's own transmission-lag findings mean even a fast,
decisive RBI response takes multiple quarters to reach the real economy, so a "put" framing
systematically understates how much drawdown can occur *before* any policy response could possibly
show up in the variables this program's own risk system tracks — the Mar-2020 case (`CONTRACT.md`
Known Prior #8: a five-week 38% fall met by no prior signal) is this program's own standing proof that
policy response speed and market-drawdown speed operate on entirely different clocks, and building a
regime seat that implicitly assumed otherwise would silently reintroduce the exact fast-crash blind
spot the program has already, elsewhere, priced honestly.

**(iii) Where BC2-style humility applies — MP1, stated honestly.** `research/register/trial-ledger.
md`'s BC2 entry (Atlas 2.3, business-cycle proper) is a **standing warning across this entire
program**, not a one-off finding local to the growth/credit lead-lag question it was run to test:
testing whether "credit leads growth," using the imported-from-Saini-et-al. direction as a
hypothesis rather than an assumption, the pooled JST panel result was a clean **FAIL at 11%** — 16 of
18 countries showed **growth** leading **credit** at cycle frequency, the opposite of the textbook
direction the literature is often imported into a design uncritically assuming. The lesson recorded
there — **imported lead-lag directions are hypotheses, never assumptions** — is exactly why MP1,
this seat's own analogous test ("does the policy rate lead credit, negatively, the direction this
entire file's transmission theory predicts?"), was pre-registered with **matched legs** (identical
simple one-year-change transformations on both the policy-rate and real-credit-growth series,
specifically to avoid the differential-smoothing artifact that can manufacture a spurious lead-lag
finding) and a **declared magnitude floor** (a country only counts toward the claim if its most
negative cross-correlation clears −0.10, so a country with essentially flat cross-correlations cannot
be forced into "voting" for a lag it barely displays). **At the time of writing, MP1, MP2 and MP3 are
pre-registered and their results are pending** (`research/register/trial-ledger.md` records all three
as "(pending)") — this file states that status plainly rather than inventing a result, exactly as
CONTRACT §12 and the program's own two-pass pre-registration discipline (already demonstrated across
every JST-panel test this ledger records, from FC1 through KJ1) require: the construction and its
bars are fixed and published *before* the print, and this file will not pre-empt that print with a
guessed number. What can be said now, honestly, is the methodological point BC2 forces: **this file's
entire A.2iv "risk-taking channel bridges L6 to L10" argument, and A.3iii's RBI DEPR lag estimates,
are themselves imported or India-specific-but-untested-on-the-cross-country-panel claims until MP1
independently checks the core directional prediction (tighter policy → slower subsequent credit
growth) on the same matched-transformation, floor-disciplined methodology BC2's own failure showed
was necessary** — if MP1 fails the way BC2 did, the honest response is not to discard L6 (the
announcement-unarbitrageability argument in A.1 does not depend on any lead-lag direction holding),
but to revisit exactly which mechanism (interest-rate, credit-quantity, or risk-taking) is actually
doing the work the seat's `tau_half` prior currently assumes, and this file's central claim survives
either way: **the object worth tracking is the lagged transmission state, whatever its precise
mechanism turns out to be, never the announcement itself.**

---

## PART G — Operator psychology

Part A documents a mechanism that is, in its first half, uniquely *un*-exploitable by this desk —
every rate decision is public, instantly priced, and actively arbitraged by better-resourced
participants — and, in its second half, uniquely slow: a lag measured in quarters, running through
balance-sheet mechanics no announcement can shortcut. That combination turns central-bank-watching
into theater: the most liquid, most continuously covered information event on the macro calendar,
six times a year, offers **genuinely nothing** to trade on the day itself, while the tradable object
sits a year or more downstream, unglamorous and easy to lose interest in. This Part maps the failure
modes that mismatch invites.

### G.1 Central-bank watching as theater — the "hawkish cut" circus

**Mechanism.** Every MPC decision now arrives bundled with a policy statement, a governor's press
conference, individual member votes, and (in advanced-economy practice this desk's own attention is
inevitably calibrated against) formal rate-path projections — material that is, per A.1ii's own
Gürkaynak-Sack-Swanson finding, genuinely informative about the **path** factor, not merely noise.
The hazard is not that this material is meaningless; it is that the *volume* of real-time
interpretive commentary it generates vastly exceeds its tradable content, and the commentary itself
becomes a self-reinforcing spectacle. The "**hawkish cut**" phenomenon — a rate *cut* delivered
alongside forward guidance read as more restrictive than expected, producing headlines and market
moves that argue about the *tone* of an easing decision — is the purest recent illustration: December
2024's Fed cut was widely termed "hawkish" specifically because the accompanying dot plot showed a
smaller expected 2025 easing path (a median 50bp versus a prior 100bp) than markets had priced,
producing a rates *sell-off* on a day the policy rate itself fell **[Verified — the December 2024
Fed episode and its "hawkish cut" characterization confirmed by search; used here as an illustrative,
general central-banking phenomenon, not an India-specific claim]**. RBI's own communication carries
the same structural temptation — stance language ("accommodative" → "neutral" → "withdrawal of
accommodation"), individual MPC member dissents, and post-meeting governor remarks are all
genuinely information-bearing in the Gürkaynak-Sack-Swanson sense, and all genuinely over-consumed
relative to their tradable content by a desk whose actual edge, per A.1–A.4, lives a year downstream.

**Countermeasure.** L6 does not consume stance *language* at all — its `indicator` field is the RBI
DBIE **repo path**, a number, not a transcript — precisely so that the seat's classification cannot
be moved by how excitingly or ambiguously a press conference was read. The desk may watch the theater
for Stage-2 red-team and narrative-context purposes (per `CONTRACT.md` §2's Stage-2 scope), but
Stage-1's L6 seat is mechanically immune to it by construction.

### G.2 The announcement-day trap — trading the public number

**Mechanism.** Every operator, at some point, feels the pull of the single most reproducible bad idea
in this literature: the belief that *this time*, the market's reaction to a decision is wrong, too
muted or too extreme, and a same-day trade can correct it faster than the OIS/bond/equity complex
itself will. A.1's event-study argument (Kuttner 2001; Gürkaynak-Sack-Swanson 2005) is the direct
rebuttal, worth restating here precisely because it is *correct on average* and *still tempting in
the instant* — every announcement day feels, subjectively, like the one where the market got it
wrong, because some participant's post-hoc "what the market missed" narrative is always being
published somewhere, creating an availability bias toward believing the exploitable-surprise story
is common when the evidence (§A.1iii: surprises rare in the MPC era) says the opposite.

**Countermeasure.** The ladder's `role` field states "never same-day event trade" as a **frozen
design constraint**, not a discretionary guideline re-litigated meeting by meeting — exactly the
"structural non-decision, made once, in the registry" pattern the fincycle-deep monograph's own G.5
names for its sibling seat. The decision not to trade the announcement is made here, in this file,
once, rather than remade under the pressure of a live 10:00 IST release six times a year.

### G.3 Anchoring on the last cycle's terminal rate

**Mechanism.** Because India has completed only a marginal n≈4–5 round trips since the early 2000s
(D08 I1, §A.1iv), every operator's felt sense of "how high rates can go" or "how low is unusually
low" is anchored, consciously or not, on the two or three terminal levels they have personally lived
through — 8.50% (Oct 2011), 6.50% (2023–24), 4.00% (the COVID floor) — treated as natural ceilings
or floors rather than levels a genuinely different inflation, growth, or global-rate environment
could exceed or undercut. This is the monetary-cycle-specific instance of the same n-is-small
extrapolation hazard `research/cycles/fincycle-deep/partA-theory-psychology.md` G.3 already names
for the real-estate cycle's single observed length, and the same-shaped hazard IR1's own two-completed-
arc inflation history (§A.3v) exists specifically to guard against on the inflation side.

**Countermeasure.** The classification L6 actually consumes is **loose/tight relative to the series'
own trailing history** (a percentile-style construction, in keeping with this program's own
no-magic-numbers rule, `CONTRACT.md` §6) rather than a fixed absolute level — so a terminal rate that
turns out to be genuinely unprecedented (higher or lower than any of the n≈4–5 prior round trips)
still registers correctly as an extreme reading on the seat's own continuous scale, rather than
silently failing to register at all because it breached an operator's personally-anchored ceiling
that was never written into the construction.

### G.4 Assuming transmission symmetry

**Mechanism.** A.2's channel theory and A.3's Indian-specific evidence both describe an *average*
lag; they say nothing, on their own, about whether tightening and easing transmit at the **same**
speed — and the honest evidence says they do not. Indian banks have been repeatedly documented
**raising** lending rates quickly after a policy tightening (loans are disproportionately variable-
rate and can reprice fast) while **cutting** them only slowly and partially after an easing, because
deposit costs — themselves fixed-tenor liabilities that cannot simply be marked down — do not fall
commensurately, and banks facing competitive pressure to retain deposit funding ("**the deposit
war**") resist cutting deposit rates even when the policy rate has already moved **[VERIFY: the
precise magnitude and consistency of this asymmetry across easing cycles — this session located
consistent qualitative reporting (RBI's own repeated public prodding of banks to pass on cuts faster;
a widely-cited ~13-month average pass-through to the interbank rate and materially longer, ~19-month,
pass-through specifically to lending rates) but no single primary academic study isolating and
quantifying the cut-vs-hike asymmetry coefficient was independently confirmed this session]**. An
operator who treats the seat's ~1-year lag as symmetric in both directions — expecting an easing
cycle's stimulative effect to arrive on the same clock a tightening cycle's cooling effect does —
is quietly assuming away a structural asymmetry this program's own evidence base cannot yet fully
quantify but can already document the *direction* of.

**Countermeasure.** The seat's stated `tau_half` (12–24 months) is carried as a **range**, not a
point, specifically so a direction-asymmetric transmission speed is representable inside the existing
construction without a redesign; the `tau_half_drift_policy`'s living-estimate and hysteresis
machinery (`ladder.yaml`) is the correct venue for testing, once India-conditioned data is available
in the data phase, whether easing legs and tightening legs need genuinely **different** lag
parameters rather than one shared range — a test this file registers as an open question rather than
resolving from priors alone.

### G.5 Assuming the low-inflation regime is permanent

**Mechanism.** §A.3v's own measured finding — inflation level and volatility both fell sharply after
the 2016 MPC/FIT adoption — is true and load-bearing for why India's post-2016 monetary cycle looks
calmer than its pre-2016 history. It is also exactly the kind of finding an operator, watching it hold
for the better part of a decade, can quietly convert into "the low-inflation, well-anchored regime is
now simply how India works," rather than "the current regime happens to be in a low-inflation phase of
an arc that, per this program's own independently-computed cross-country evidence, has never yet lasted
more than several decades." `research/cycles/inflation-deep/partAB-theory-evidence.md`'s own IR1
result is the direct corrective, computed on this program's own JST panel rather than asserted from
outside literature: pooled across 18 countries since 1871, the fiat-era inflation record shows
**exactly two completed arcs** — a 52-year up-arc (1930–1982) and a 38-year down-arc (1982–2020) — and
IR2's 81% pooled era-stickiness finding (§A.3v) cuts **both ways**: regimes persist while they last,
which is precisely why a regime that has persisted for a decade offers no logical guarantee it persists
for the next one. India's own FIT-era CPI history (2016–present) is barely a third of even the shorter
of those two historical arcs.

**Countermeasure.** L15's own long-wave machinery (`ladder.yaml` `tau_half_drift_policy`
`long_wave_expression`) already carries the structural, reduce-only budget this program allocates to
exactly this class of regime-reversal risk — a gold-floor attribution and slow-debasement tail budget
that exist *independently* of whether the current low-inflation regime persists or breaks — precisely
so the monetary-cycle desk is not required to personally judge, meeting by meeting, whether "this
time" the anchored-expectations regime is finally cracking. The judgment is pre-funded at the
portfolio level rather than left to be made, under pressure, the day CPI first prints outside the
4%±2% band for several consecutive quarters.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Over-reading stance language, dot-plots, and post-meeting tone ("hawkish cut" circus) | The path factor (Gürkaynak-Sack-Swanson 2005) is genuinely informative, but interpretive commentary volume vastly exceeds tradable content; December-2024 Fed episode as the generic illustration | L6 consumes the RBI DBIE **repo path only** — a number, never a transcript; Stage-2 may read commentary, Stage-1's seat cannot be moved by it |
| Trading the announcement day itself | Kuttner (2001) / Gürkaynak-Sack-Swanson (2005): surprises price within minutes via OIS/bond/equity markets faster and better-resourced than this program | `ladder.yaml` role line ("never same-day event trade") is a frozen design constraint, decided once in the registry, not re-litigated per meeting |
| Anchoring "how high/low rates can go" on the last 2-3 terminal levels personally observed | n≈4-5 marginal India round trips (D08 I1); the same small-n extrapolation hazard fincycle-deep G.3 names for real estate | Loose/tight classification is a **percentile on trailing history**, not a fixed absolute level — an unprecedented terminal rate still registers correctly |
| Assuming easing transmits on the same clock as tightening | Indian lending rates reprice up faster than down (variable-rate loans vs. sticky deposit costs, the "deposit war"); direction confirmed, precise coefficient `[VERIFY]` | `tau_half` carried as a **range** (12-24m), not a point; direction-specific lag split is an open, registered question for the data phase, not assumed away |
| Treating the post-2016 low-inflation, well-anchored regime as permanent | IR1 (own JST computation): only two completed fiat-era inflation arcs, 52y and 38y; IR2's 81% stickiness cuts both ways — persistence while it lasts is not a guarantee of continuation | L15's reduce-only gold-floor and tail-budget machinery is pre-funded independent of this desk's meeting-by-meeting judgment about whether the regime is cracking |
| Reading MP1 (or any single pre-registered test) as license to abandon the seat on a "wrong-direction" result | The BC2 precedent: a failed imported lead-lag direction does not by itself invalidate the seat it was meant to calibrate — it re-opens *which* mechanism explains the tau_half, never the announcement-unarbitrageability argument | A.4iii states MP1-MP3 are pending and commits in advance to revisiting mechanism attribution, not the seat's existence, on a BC2-shaped result |

None of these six countermeasures asks the operator to be more disciplined, in the moment, than Part
A's evidence justifies. Each converts a live judgment call — decide whether this particular press
conference finally contains tradable information, decide whether this specific surprise is the one
worth a same-day position, decide whether this cycle's terminal rate is really a ceiling, decide
whether this easing cycle will feel like the last one, decide whether the well-anchored regime has
finally ended, decide whether one disappointing pre-registered result means the seat itself was wrong
— into a structural non-decision, made once, in the registry, before the moment that would have made
it hardest. The object worth holding onto, across every row of that table, is the one A.1 opens with:
**the announcement is the least interesting thing about a monetary-policy cycle; the slow, partial,
quantity-and-quality-changing year that follows it is the only thing this desk is actually positioned
to harvest.**

---

> **[Desk note, added at assembly (2026-09-02, principal's edit — the trials landed after this
> chapter's ledger read):** `mp-RESULTS.md` now exists. MP1 **PASSED** the matched-legs test
> (9 qualifying countries at the −0.10 floor; 67% place the most-negative correlation at
> rate-leads lags, bar 60%) — the register's first surviving imported direction. MP2's lag
> profile: +0.07 contemporaneous flipping to a −0.06 peak at +1y, decaying by +3 — the seat's
> ~1y convention calibrated, and the sign flip is the measured case A.1 argues. MP3: 53%
> annual sign-persistence — the Δ-based stance variant this chapter contemplates is closed
> off; stance is LEVEL content. Full prints and the honest read: mp-RESULTS.md.]**

