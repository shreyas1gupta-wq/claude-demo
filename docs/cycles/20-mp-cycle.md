# The Monetary-Policy Cycle — Full Monograph (Atlas 2.6, seat L6)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** L6 stays exactly as seated — Tier B, lagged (~1y) loose/tight regime,
never a same-day event trade — and leaves this entry CALIBRATED: the lag convention now has
its analogue number, the stance definition is sharpened to LEVEL content, and the ladder's
provenance placeholder is replaced with located primary citations.

**Headline results (trials MP1–MP3, pre-registered, matched legs per the BC2 standing warning):**
- **MP1 PASS (67% vs 60% bar):** rate moves lead credit growth negatively — the register's
  FIRST imported lead-lag direction to survive the matched-legs, magnitude-floored test.
- **MP2 — the sign flip:** corr(Δrate, credit growth) is +0.07 contemporaneous (central banks
  tighten INTO booms: the reaction-function face) and peaks NEGATIVE at +1y (−0.06) — the
  measured reason an unlagged monetary seat would double-count euphoria in the shared budget.
- **MP3 — 53%:** annual move-direction persistence is a coin flip; stance is the LEVEL pair
  (effective real rate percentile + liquidity sign), and the Δ-based variant is closed off.

**Registry work landed with this entry:** L6's source now cites Khundrakpam-Jain WPS(DEPR)
11/2012 + Mohanty WPS(DEPR) 06/2012 (output 2-3q, inflation 3-4q, persisting 8-10q), replacing
the [VERIFY primary WP] placeholder. The completed round-trip count is argued in Part B:
**3 (4 under an alternative convention), a 4th in progress — the changes_if graduation clock
("6th completed round trip") is decades from ringing, stated plainly.** The asymmetry record
(hikes-fast/cuts-slow across BPLR→Base→MCLR→EBLR; 2022's MCLR +120bp vs deposits +78bp; the
2022-24 deposit war) closes design MP-D2 on the public record.

**Assembled from:** partA-theory-psychology.md · partB-cases.md · mp-RESULTS.md ·
partC-data.md · partDEFH-math-algo-harvest-ledger.md.

---

# PART A + G — Transmission theory (four channels, Indian machinery) and operator psychology

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

---

# PART B — India's policy campaigns 1997-2026, the round-trip count, the asymmetry record

# PART B — India's monetary-policy cycle case record

*Monetary-policy-cycle monograph (Atlas 2.6; ladder seat `L6_monetary_stance`, `config/ladder.yaml`,
Tier B, `tau_half` 12–24 months) · Part B · v1.0 · 2026-09-02 · Author: Claude (research agent) for
Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. Scope, stated once: this Part owns the **policy-cycle side** of every
episode — rate/liquidity path, RBI's stated rationale, what transmission (lending/deposit rates,
credit growth) actually did. The **macro/activity side** of several windows (GDP, IIP, exports, the
dating problem itself) is already covered by `docs/cycles/18-business-cycle.md` Part B (Atlas 2.3) —
cited by episode, never re-derived. The **NBFC/shadow-credit side** of 2013 and 2018 is already
covered by `research/cycles/shadow-deep/partB-cases.md` — cited, not re-derived. The **credit-side**
mechanics of the 2003–2018 twin-balance-sheet decade (GNPA masking, the AQR, the restructuring
alphabet) are already covered by `research/cycles/credit-deep/partB-cross-country.md` case #10 —
cited, not re-derived. This chapter's sibling files carry the theory
(`partA-theory-psychology.md`), the pre-registered JST-analogue trials MP1–MP3 (`mp-RESULTS.md`), the
data engineering (`partC-data.md`), and the algorithm/harvest ledger
(`partDEFH-math-algo-harvest-ledger.md`) — this Part closes that ledger's two outstanding designs:
**MP-D2** (pass-through asymmetry, hikes vs cuts, deposit-war conditioning — §B.4 below) and
**MP-D3** (the completed round-trip count against the ladder's own `changes_if: "6th completed round
trip"` — §B.3 below). Style follows `research/cycles/fincycle-deep/partB-cases.md` (house style):
numbers-forward, every figure sourced, `[VERIFY]` where a search pass could not pin the primary
release.*

*A note on "L6's lagged-regime read," used after every episode below: per `partC-data.md` §C.1, L6
consumes an `effective_rate` — the operating policy rate under whatever framework governed at the
time (Bank Rate → LAF repo → the single-repo corridor from May 2011 → the 2020–22 reverse-repo-floor
interlude → the SDF-floor era from April 2022) — read as a real rate against its own expanding
percentile, paired with the liquidity sign (surplus/deficit), classified loose/neutral/tight, and
consumed **lagged ~1 year** (the MP2 calibration: contemporaneous correlation with credit growth is
mildly **positive**, +0.07 — central banks tighten *into* booms, the reaction-function face — before
flipping to a **negative** peak of −0.06 at +1 year, per `mp-RESULTS.md`). L6 never trades the
announcement itself; the read below is what the lagged, classified state would say a year after each
episode's own rate action, not a same-day call.*

---

## B.1 The eight campaigns

### 1. 1997–2003 — the Jalan easing era

**The rate path.** Governor Bimal Jalan (22 Nov 1997 – 4 Sep 2003) inherited a Bank-Rate-era
framework — the modern repo-based Liquidity Adjustment Facility (LAF) did not exist yet; it was
introduced only in June 2000, with the single-repo operating corridor arriving even later, in May
2011 (`partC-data.md`'s own "effective-rate migration" point, first instance). The single sharpest
move of the entire 1997–2003 window came almost immediately: following the July 1997 Asian financial
crisis, contagion pressure on the rupee forced RBI to **raise the Bank Rate from 9% to 11%,
effective 17 January 1998** — a defensive spike, alongside a 1-percentage-point CRR increase in
December 1997/January 1998 and a temporary, very short-dated repo-style instrument pushed as high as
9% in the same defense. **[Verified — the 11% Bank Rate level and its 17 Jan 1998 effective date;
the accompanying CRR hike and short-dated repo spike are corroborated in the same search pass but
carry lower confidence on the exact repo figure `[VERIFY: the pre-LAF "repo" instrument's precise
January 1998 level and duration]`.]** The defense worked fast: the rupee stabilised at roughly
₹38.9/USD by late January 1998 and traded in a narrow ₹39.5 band by March 1998 — a shock, not a
regime, in the ladder's own vocabulary (`tau_half` 12–24 months; a two-month spike does not clear
even the low end of that band). The Bank Rate was then cut steadily across the rest of the Jalan
governorship; the CRR's own decline is the cleanest continuously-dated series available for this
era: **15.00% (8 Oct 1992) → 14.00% (May 1993) → 15.00% (Aug 1994, a brief re-hike) → 11.00% (Nov
1996) → 10.00% (Jan 1997) → 10.00%→11.00%→10.00% (a further 1997–98 wobble around the Asian-crisis
defense) → 9.00% (Nov 1999) → 8.00% (Apr 2000) → 8.50% (Aug 2000, a brief re-hike) → 7.50% (May 2001)
→ 5.50% (Dec 2001) → 4.75% (Nov 2002) → 4.50% (Jun 2003)** — a near-monotonic decline from the
15%-era ceiling to single digits, exactly the "CRR's long decline from 15% (1991)" the desk's own
brief names, verified date-by-date. **[Verified — the CRR chronology, cross-checked across the
allbankingsolutions.com and Business Standard timeline sources; the exact 1996–99 sub-path around
the Asian-crisis wobble carries `[VERIFY: primary RBI notification cross-check]`.]** On the operating-
rate side, once the June-2000 LAF gave RBI a genuine short-term policy instrument, the repo rate
itself eased from **9% (Mar 2001) → 8.75% (Apr 2001) → 8.5% (Jun 2001) → 8% (Mar 2002) → 7.5% (Nov
2002) → 7.1% (Mar 2003)**, converging toward the **~6% trough that the Reddy tightening campaign
would use as its own starting point in March 2004** `[VERIFY: the exact 2003→2004 sub-path from
7.1% to 6%]` — the Bank Rate itself, meanwhile, having been the pre-LAF era's headline instrument,
settled near 6% as the LAF regime took over, consistent with dossier 08's own "trough near 6%
(2003–04)" framing.

**Stated rationale.** The Jan-1998 spike was an explicit, public exchange-rate defense — arresting
contagion from the Asian crisis, not a domestic-inflation-targeting move (India had no formal
inflation target of any kind until 2015). The subsequent multi-year easing was framed around
supporting growth and financial-sector reform following the 1991–92 liberalization, deepening the
LAF's own operating-rate architecture, and progressively lowering the reserve-requirement burden on
a banking system still working through the post-1991 NPA legacy (cross-ref `docs/cycles/
18-business-cycle.md` Part B case 1, the 1991 BoP crisis's own credit-side legacy, not re-derived
here).

**What transmission actually did.** Bank lending rates in this era were still governed by the
administered Prime Lending Rate (PLR) system — a pre-Base-Rate, pre-MCLR regime (`partC-data.md`
§C.3's own four-regime taxonomy: BPLR → Base Rate (Jul 2010) → MCLR (Apr 2016) → EBLR (Oct 2019)) —
under which pass-through was notoriously incomplete and administratively sticky in both directions;
directionally, PLRs eased through the late 1990s alongside the Bank Rate and CRR cuts, but the
magnitude of pass-through relative to the policy-rate decline is `[VERIFY: no primary PLR-vs-Bank-Rate
spread series located this pass]`. Credit growth recovered through the late 1990s deceleration
(`18-business-cycle.md` Part B case 2, the 1997–2002 "long deceleration") into the 2003–2008 boom
this same easing regime fed directly into.

**Duration.** Treating the Jan-1998 spike as a shock inside a single multi-year LOOSE regime (per
the ladder's own tau_half band, a two-month spike cannot itself register as a distinct regime): the
Jalan era is one long easing arc, roughly **1998–2003/04, on the order of 5–6 years** — among the
longest single-direction regimes in this entire record, second only to the 2020–22 COVID floor in
duration once that episode's own hold is counted (§7 below).

**L6's lagged-regime read.** For most of 1998–2003, a lagged L6 reading the effective rate (Bank
Rate, then repo from 2001) against its own expanding percentile would have classified the regime
**LOOSE and aging** throughout — the multi-year monotonic decline gives L6 no ambiguous signal here,
unlike several later episodes with within-regime wobbles (§4, §5 below). The one moment L6 would
have registered a **transient TIGHT flag** is the 1998 Q1 spike itself — but on the ~1-year lag
convention, by the time that flag would have entered the regime score, the Bank Rate had already
reversed and eased again, meaning L6's own lag discipline (never a same-day event trade,
`partDEFH...` Part E Step 4) would have naturally filtered out a shock this short-lived, exactly the
design behavior the seat is built to produce.

---

### 2. 2004–2008 — the Reddy tightening campaign

**The rate path.** Governor Y.V. Reddy (6 Sep 2003 – 5 Sep 2008) inherited the ~6% repo trough and
tightened steadily as growth accelerated and inflation pressure built: **repo 6.00% (31 Mar 2004) →
6.50% (24 Jan 2006) → 7.00% (25 Jul 2006) → 7.25% (30 Oct 2006) → 7.50% (31 Jan 2007) → 7.75% (30 Mar
2007) → 8.00% (12 Jun 2008) → 8.50% (25 Jun 2008) → 9.00% (30 Jul 2008)** — the cycle's own peak, a
**300bp climb over roughly four years and four months**, the bulk of it (150bp) compressed into the
final six weeks before the July-2008 peak as oil and food inflation spiked ahead of the Lehman
collapse. **[Verified — the full repo date/level chronology, cross-checked across multiple aggregator
sources with consistent dates.]** The CRR moved in the same direction across the same window, rising
from its ~4.5–4.75% 2003 floor toward a pre-crisis peak of **9% by August 2008** — the same 9% level
the crisis-response chapter below (§3) documents being unwound in four months flat
`[VERIFY: the complete CRR step-path 2004→2008; the 9% August-2008 peak level itself is corroborated
by the symmetric "CRR cut from 9% to 5%" crisis-era sourcing, which requires a 9% starting point]`.

**Stated rationale.** RBI's own contemporaneous framing was containing an overheating economy running
at 9%+/yr growth with rising headline and asset-price inflation, alongside a second, structurally
distinct problem the tightening campaign had to solve *simultaneously*: **large, persistent capital
inflows** that would otherwise have driven unwanted rupee appreciation if RBI's dollar purchases went
unsterilized. The **Market Stabilisation Scheme (MSS)** — formalised via a Memorandum of Understanding
between the Government of India and RBI signed **25 March 2004** and operationalised from **April
2004** — was the instrument built specifically to solve this: RBI issues government bonds whose
proceeds are impounded in a separate account (never funding the fiscal deficit), sterilising the rupee
liquidity that dollar-purchase intervention would otherwise inject, at a scale that continuous
open-market sales of RBI's own limited G-sec stock could not have sustained. **[Verified — the MSS's
2004 origin, its March 2004 MoU date, and its sterilization mechanism.]** This is the clean illustration
of the **overheating/capital-inflows dilemma** the desk's own brief names: a single tightening campaign
simultaneously fighting domestic demand *and* absorbing external liquidity, using two different tools
(the repo/CRR path for the former, MSS for the latter) rather than one.

**Macroprudential tightening, before the term was fashionable.** Running alongside the rate campaign,
RBI used **risk-weight and provisioning tools on real-estate and consumer-credit exposures** — the
same countercyclical macroprudential logic BIS and the FSB would only formalize globally after 2009 —
to lean specifically against the credit-fuelled real-estate boom the fincycle monograph's own India
case (`research/cycles/fincycle-deep/partB-cases.md` §B3) dates to 2002–03 onward. RBI's general
direction across 2005–2007 raised risk weights on commercial real estate exposure and consumer credit
well above the standard 100% baseline, and lifted standard-asset provisioning requirements on the same
sensitive-sector book from a low base to multiples of it — a direct, administrative credit-supply lean
against the property boom's collateral channel, the same *class* of tool (though a different mechanism)
Japan's MOF used in 1990 and China's "three red lines" used in 2020 (both documented in the fincycle
monograph's own case record) `[VERIFY: the exact RBI circular dates and precise risk-weight/provisioning
percentage points for 2005–2007 — this pass could confirm the general direction and today's risk-weight
levels (commercial real estate: 100% standard / 150% non-standard) but not independently re-pull the
specific 2005–2007 circulars themselves]`. **Cross-reference discipline**: the fincycle monograph's own
India case (`fincycle-deep/partB-cases.md` §B3) already documents the 2003–2013 property boom's
price-side magnitude (Delhi/Bengaluru city indices near-tripling 2003–2007) and the RERA/GST structural
reset that followed the 2013–2020 stagnation; this Part's own contribution is narrower — the *policy
tool* RBI used mid-boom, not the boom's own price or credit chronology, which belongs to the fincycle
and credit monographs respectively.

**What transmission actually did.** Bank lending rates (still BPLR-regime, per `partC-data.md`'s
taxonomy) rose alongside the repo/CRR campaign, and credit growth — already running at a multi-year
high through the 2003–2008 boom (`docs/cycles/18-business-cycle.md` Part B case 3: GFCF growth
8.2%→17.5%, 2002→2004, capital-goods output roughly tripling 2005–2008) — decelerated only mildly
ahead of the 2008 global crisis itself, with manufacturing and construction growth easing by roughly
2.5 percentage points in 2007–08 from a 12% 2006–07 base (per the same cross-referenced chapter) —
a soft early warning that arrived *before* Lehman, not clearly separable from the tightening
campaign's own bite `[VERIFY: an India-specific bank-credit-growth series isolating the tightening
campaign's own effect from the simultaneous global deceleration]`.

**Duration.** A single, essentially uninterrupted TIGHT regime, **March 2004 – July 2008, roughly
four years and four months**.

**L6's lagged-regime read.** Reading the effective repo rate a year behind, L6 would classify this
campaign **TIGHT and aging** from roughly early 2005 onward — long and monotonic enough that the lag
costs little precision, except at the very end: L6's own 1-year-lagged read would still carry
**TIGHT** into mid-2009, a full year *after* the crisis-response easing (§3) had already cut the repo
rate by more than half — the stale read the ladder's design accepts as the cost of never trading a
same-day event, and why L6 is a REGIME input inside a shared macro block, never a timing trigger.

---

### 3. 2008–2010 — the crisis easing, and the 2010–2011 normalization

**The rate path — the speed record.** As the Lehman collapse hit India's own funding markets, RBI
reversed the entire 2004–2008 tightening campaign in a matter of months: the **repo rate fell from
its 9.00% (30 Jul 2008) peak to 4.75% by April 2009** — essentially the same magnitude of move the
prior campaign took over four years to build, unwound in under nine months. The **CRR fell from 9% to
5% over four months, October 2008 to January 2009** — a **400bp reduction released roughly USD 32.7
billion** into the banking system, according to contemporaneous IMF commentary praising the response
as "quick" and "fully warranted." **[Verified — the repo trough level and approximate date, and the
CRR's magnitude/timing and IMF characterization.]** SLR was trimmed one point, **25%→24%, in November
2008**. This combination — repo, CRR, and SLR all easing simultaneously and fast — is, on the ladder's
own evidentiary standard, the single cleanest "speed record" in this entire chronology: no other
easing campaign in the 1997–2026 record moves this much distance this fast. **The 2010–2011
normalization then reversed it just as sharply, if not as fast**: RBI raised the repo rate **13 times
between March 2010 and October 2011, a cumulative 375bp, from the 4.75% trough to 8.50%** — the
granular early path runs **5.00% (19 Mar 2010) → 5.25% (20 Apr 2010) → 5.50% (2 Jul 2010) → 5.75% (27
Jul 2010) → 6.00% (16 Sep 2010) → 6.25% (2 Nov 2010) → 6.50% (25 Jan 2011) → 6.75% (17 Mar 2011)**,
continuing in the same 25bp cadence through the remainder of 2011 to the 8.50% October peak.
**[Verified — the "13 hikes, 375bp cumulative, 4.75%→8.5%, Mar2010–Oct2011" aggregate figure and the
early 2010 date-by-date path; the complete month-by-month 2011 leg carries `[VERIFY: full primary
DBIE table]`.]**

**Stated rationale.** The 2008–09 easing was an explicit, unambiguous crisis response to a global
funding shock transmitted through India's export and capital-flow channels — the fastest, most
export/IIP-visible transmission episode in this entire record (`docs/cycles/18-business-cycle.md`
Part B case 4: IIP registering its first negative print in fifteen years in October 2008, exports
turning outright negative the same month, averaging roughly a 20% contraction through September 2009,
cross-referenced not re-derived here). The 2010–11 reversal was explicitly framed as reining in
inflation once the crisis-response stimulus had done its job and growth had recovered sharply (the
same cross-referenced chapter's own "fast V": growth recovering to 7.4% FY10, with Q4 FY10 alone
printing 8.6%).

**What transmission actually did.** Base-Rate-era (from Jul 2010) bank lending rates cut alongside the
crisis-era repo/CRR reduction, though — consistent with the chronic "sticky lending rate" complaint
RBI itself would keep making through the 2010s (RBI publicly urged banks for faster transmission as
late as 2016, per contemporaneous reporting) — the pass-through of the 2008–09 cuts into actual bank
lending rates was widely characterized as slower and smaller than the policy-rate move itself
`[VERIFY: an India-specific 2008–09 PLR/Base-Rate pass-through coefficient]`; credit growth, having
decelerated sharply through the crisis, recovered alongside the "fast V" described above. On the
2010–11 tightening leg, the reverse asymmetry showed up: lending rates rose promptly (banks pass a
hike through faster than a cut, the general pattern this Part's closing §B.4 documents across every
episode in this record), while deposit rates lagged, squeezing margins in the near term before banks
caught up.

**Duration.** The crisis easing itself is short — **roughly nine months, August 2008 to April 2009** —
among the shortest regimes in this record; the subsequent tightening runs **roughly 18 months, March
2010 to October 2011**.

**L6's lagged-regime read.** The cleanest illustration of why L6's ~1-year lag matters. A same-day
read of the October-2008 cut would classify the regime LOOSE almost instantly — but MP2's own
calibration (contemporaneous corr +0.07, credit-boom-linked; peak effect at +1y, −0.06) says the
*contemporaneous* reading is the reaction-function face, not the medicine's effect: RBI eased
*because* activity had just collapsed. A properly-lagged L6 would register LOOSE only around
mid-to-late 2009 — squarely inside the "fast V" recovery already underway, a stale read but the
design's own accepted tradeoff. On the reversal leg the same lag means L6 would still read LOOSE well
into 2010 even as the repo rate climbed through its first several hikes — the seat's slowest-to-update
moment in this record, and the strongest argument here for treating L6 purely as a REGIME input,
never a standalone timing signal.

---

### 4. 2011–2013 — the stagflation squeeze, and the July 2013 taper defense

**The rate path.** Following the 8.50% October-2011 peak, RBI eased gradually through 2012–13 as
growth decelerated sharply (`docs/cycles/18-business-cycle.md` Part B case 5: growth falling from 7.8%
at the start of 2011 to a then-nine-year-low 6.5% FY12, with Q4 FY12 at 5.3%) while WPI inflation
remained stubbornly elevated, running near 7–8%/yr through most of 2011–12 before finally easing to
6.0% by March 2013 — the classic stagflation dilemma the desk's own brief names: **growth deceleration
that was, in RBI's own contemporaneous words, "not commensurate with inflation control."** Repo eased
to **7.25% by 3 May 2013**. Then, following the Fed's May-2013 taper announcement and a rupee
depreciation from roughly ₹54 to ₹69/USD (a **~28% fall, April–August 2013**, touching a lifetime low
of ₹68.85 on 28 August 2013), RBI mounted an explicit rupee defense: on **15 July 2013**, it raised the
**Marginal Standing Facility (MSF) rate by 300 basis points above the repo rate — repo at 7.25%, MSF
at an effective 10.25%** — deliberately inverting the normal LAF corridor so the MSF's upper bound,
not the repo rate, became the market's operative overnight cost of funds. **[Verified — the ~28% rupee
depreciation, the 28 Aug 2013 lifetime low, and the 15 Jul 2013 300bp MSF hike to an effective 10.25%,
already cross-checked against `research/cycles/shadow-deep/partB-cases.md` §B5's own independent
citation of the same figures.]** The MSF corridor was unwound in September 2013, restoring repo as the
effective policy anchor; conventional repo hikes then continued the tightening through the same window
— **7.25% (3 May 2013) → 7.50% (20 Sep 2013) → 7.75% (29 Oct 2013) → 8.00% (28 Jan 2014)** — under
newly-arrived Governor Raghuram Rajan (from 4 Sep 2013), who alongside the MSF/repo moves also launched
the **FCNR(B) swap window** (announced shortly after his 4 September 2013 arrival): a special facility
letting banks swap fresh, minimum-three-year FCNR(B) dollar deposits at a fixed 3.5%/year rate,
mobilising an estimated **USD 26 billion** and contributing to roughly **USD 34 billion** raised
between September and November 2013 — widely credited with stabilising the rupee and moving India out
of the contemporaneous "Fragile Five" grouping. **[Verified — the FCNR(B) scheme's mechanism, its
roughly USD 26bn mobilisation, and the USD 34bn September–November aggregate.]**

**Stated rationale.** The 2012–13 easing leg was framed as supporting a sharply decelerating economy
once inflation showed the first signs of moderating; the July-2013 MSF spike was an explicit, openly-
stated **exchange-rate defense** against taper-driven capital outflow pressure — a **rates** operation,
not a credit-quality response, the distinction `research/cycles/shadow-deep/partB-cases.md` §B5
documents in full as the episode's own "negative control" against the 2018 NBFC funding freeze
(cross-referenced by name, never re-derived here: that Part's own subject is the NBFC/shadow-credit
signature of 2013 vs 2018; this Part's subject stops at the policy-rate and rupee-defense mechanics).

**What transmission actually did.** The MSF spike raised the marginal cost of overnight bank funding
sharply but briefly (unwound within roughly two months), with system-wide CP/CD funding costs rising in
its wake without a distinct credit-quality event behind them — precisely the shadow-deep monograph's
own finding that the 2013 episode shows "no macro propagation" on its own credit-stress score (SC1: 57th
percentile, per that Part's own table) even though the same spread series looks superficially similar to
a genuine credit event. Bank lending rates rose modestly through the continued repo hikes into January
2014; credit growth, already decelerating alongside the broader 2011–13 slowdown, showed no further
distinct air-pocket attributable to the MSF episode specifically `[VERIFY: an isolated bank-credit-growth
read for the Jul–Sep 2013 window net of the broader 2011–13 deceleration]`.

**Duration.** The broader 2012–13 easing-then-partial-reversal is genuinely a single, bumpy regime
rather than two clean phases: **easing April 2012 – May 2013 (roughly 13 months)**, then a **defensive
re-tightening July 2013 – January 2014 (roughly 6 months)** that did not reach a new high above the
October-2011 peak (8.00% in Jan 2014 sits below 8.50%) — a **lower high**, the technical signature this
Part's own round-trip count (§B.3) treats as a wobble inside one longer regime, not a fresh cycle.

**L6's lagged-regime read.** A lagged L6 would have read the 2012–13 easing as LOOSE-and-young through
most of 2013, still carrying that classification when the July-2013 MSF spike hit — exactly the kind of
regime-versus-shock mismatch the ladder's own design (L2 fast-stress owns announcement-day and
event-window vol mechanically; L6 does nothing on announcement days by construction, per `partDEFH...`
Part E Step 4) is built to separate: the desk's fast layer, not L6, is the seat meant to react to a
two-month MSF corridor inversion. By the time L6's own 1-year lag would have registered a TIGHT flag
from the Jul–Oct 2013 rate actions, the effective rate (now back to conventional repo terms) had barely
moved net of the 2012 easing — a muted, easily-missed signal precisely because the underlying regime
never cleanly reversed direction on a net basis.

---

### 5. 2014–2016 — the Rajan disinflation and the birth of the MPC

**The rate path.** Repo held at **8.00%** through most of 2014 following the Jan-2014 hike (§4), then
began a sustained multi-step easing under the newly-adopted inflation-targeting framework: **7.75% (15
Jan 2015, a surprise off-cycle cut) → 7.50% (4 Mar 2015, a surprise post-Budget cut) → 7.25% (2 Jun
2015) → 6.75% (29 Sep 2015, a larger-than-expected 50bp cut, the year's third and largest reduction,
totalling 125bp of easing in calendar 2015) → 6.50% (5 Apr 2016)**. **[Verified — the complete
2015–16 date/level path; the "125bp of 2015 easing" aggregate figure independently corroborated.]**

**Stated rationale — the institutional pivot, not just the rate path.** This campaign is defined less
by its rate magnitude than by the **regime change underneath it**: the **Urjit Patel Committee**
(a 2013–14 RBI expert panel chaired by then-Deputy-Governor Urjit Patel, report submitted January
2014) recommended RBI target CPI inflation alone (rather than the historically multi-indicator
approach), adopt a nominal anchor near 4%, and create a Monetary Policy Committee to vote on rate
decisions. The **Monetary Policy Framework Agreement**, signed between RBI and the Ministry of Finance
in **February 2015**, formalised a **4% CPI target with a symmetric 2-percentage-point tolerance band
(2%–6%)** based on CPI-Combined (2012 base). **[Verified — the Committee's January-2014 report, its
core recommendations, and the February-2015 Framework Agreement's 4%±2% target.]** The **Finance Act,
2016** then gave the framework statutory force by amending the RBI Act, and in **August 2016** the
government formally notified the 4%±2% target for the period through March 2021 (renewed in 2021 for a
further five years). Rajan's own public framing — "an Urjit Patel glide path fits us very well,
ensuring moderate growth even while we disinflate" — named the explicit disinflation targets the glide
path itself set: **8% CPI by January 2015, 6% by January 2016**, both of which the easing path above
was calibrated against as inflation actually cooperated. The **Monetary Policy Committee (MPC)** itself
was constituted under the amended RBI Act on **27 June 2016** — a six-member body (Governor as
chairperson, one RBI deputy governor, one further RBI officer, and three government-appointed external
members serving four-year terms) replacing what had been, until then, a Governor's sole and personal
decision. **[Verified — the MPC's statutory constitution date and six-member structure.]**

**What transmission actually did.** MCLR (from April 2016, per `partC-data.md`'s taxonomy) had not yet
arrived for most of this window — banks were still on the Base Rate regime (from July 2010) — and the
familiar complaint recurred: RBI's own Governor publicly pressed banks on transmission speed through
2015–16, remaining "focused on rate cut transmission" as late as December 2015, implying the 125bp of
2015 cuts had not fully reached borrowers by year-end `[VERIFY: an India-specific Base-Rate
pass-through coefficient for this leg — this pass located only qualitative commentary]`. Credit growth
remained subdued, consistent with the broader post-2011 twin-balance-sheet drag `credit-deep`'s own
case #10 documents in full (not re-derived here).

**Duration.** A single sustained LOOSE regime, **January 2015 – April 2016, roughly 15 months** —
one of the more clearly bounded regimes in this record, its start pinned almost exactly to the
February-2015 Framework Agreement.

**L6's lagged-regime read.** A lagged L6 would register the disinflation as **TIGHT-but-turning**
through most of 2015 (the 2014 8.00% hold still dominating the trailing window) before flipping to
**LOOSE** only around early-to-mid 2016 — stale relative to the policy pivot, but a lag that works in
the desk's favor here: the MPC's own creation (June 2016) and first meeting (October 2016, §6) arrive
almost exactly when L6 would finally register the prior year's easing — regime-score input and
structural change landing in the same rough window, a coincidence worth noting, not relying on.

---

### 6. 2016–2019 — the MPC's early years

**The rate path.** The MPC's **first meeting, 3–4 October 2016**, delivered a unanimous 25bp cut to
**6.25%** under new Governor Urjit Patel (in office from 4 Sep 2016) — a six-year low at the time, and
notable because roughly 60% of analysts polled beforehand had expected a hold. **[Verified — the
first-meeting date, the unanimous decision, and the 6.25% level.]** Barely a month later, **8 November
2016 demonetisation** — the withdrawal of legal-tender status from ₹500/₹1,000 notes — produced a
liquidity event RBI's own conventional toolkit had not been designed for: a surge of returned currency
into the banking system (deposits rising from roughly ₹97 lakh crore to ₹101.1 lakh crore between the
16-September and 11-November reporting fortnights) pushed system liquidity toward RBI's absorption
capacity limits (surplus approaching ₹5 trillion against roughly ₹7.5 trillion of usable collateral
G-secs). RBI's response was a genuinely novel tool: an **incremental CRR of 100% on the *increase* in
each bank's net demand-and-time-liabilities (NDTL) between the 16-September and 11-November fortnights**
— effective the fortnight beginning **26 November 2016**, expected to absorb roughly **₹3.24 lakh
crore** — while the *standard* CRR on total deposits stayed unchanged at 4%. **[Verified — the
mechanism, its NDTL window, its effective date, and the absorption estimate.]** The measure was
**withdrawn from the fortnight beginning 10 December 2016** — one of the shortest-lived instruments
in this chronology, roughly two weeks. With reverse repo doing much of the day-to-day absorption
given the surplus, the **reverse repo effectively became the de-facto operative rate for much of this
window** — the first instance of a pattern that recurs far more durably in 2020–22 (§7)
`[VERIFY: an explicit contemporaneous characterization of the reverse repo binding in this specific
window, as opposed to the better-documented 2020–22 instance]`. Repo then eased
further to **6.00% on 2 August 2017** — the lowest level since November 2010 — and held there until
**6 June 2018**, when it rose **25bp to 6.25%**, followed by a further **25bp to 6.50% on 1 August
2018** — the first back-to-back hikes since October 2013, and the first hike of any kind since the
January-2014 tightening (§4). **[Verified — the Aug-2017 cut to a post-Nov-2010 low, the two 2018
hike dates and levels, and the "first back-to-back hikes since Oct 2013" characterization.]** A long
easing sequence then followed through 2019: **6.25% (7 Feb 2019) → 6.00% (4 Apr 2019) → 5.75% (6 Jun
2019) → 5.40% (7 Aug 2019, an unusual 35bp step) → 5.15% (4 Oct 2019)** — a cumulative **135bp of
easing across five consecutive cuts in a single calendar year**, under Governor Shaktikanta Das (in
office from 12 Dec 2018, following Urjit Patel's resignation on 10 December 2018). **[Verified — the
complete 2019 date/level path and the 135bp cumulative figure.]**

**Stated rationale.** The Oct-2016/Aug-2017 easing reflected continued disinflation and a still-
decelerating economy in demonetisation's aftermath; the incremental-CRR move was an explicit, openly-
stated liquidity-absorption measure with no inflation or growth signal attached at all — a pure
plumbing operation. The 2018 hikes were framed around rising inflation risk (partly fuel-price-driven)
and the need to anchor expectations even as growth had not yet visibly cracked; the 2019 easing
sequence was explicitly framed around a **decisively slowing economy** — the same slide
`docs/cycles/18-business-cycle.md` Part B case 6 documents from the activity side in full detail
(GDP growth 8.0%→7.1%→6.7%→4.2%, FY16→FY20, the FY20 print the lowest since FY09; cross-referenced,
never re-derived here) and its own IL&FS-driven NBFC funding freeze (September 2018, ₹91,091 crore of
debt — fully covered by `research/cycles/credit-deep/partB-cross-country.md` case #10 and
`research/cycles/shadow-deep/partB-cases.md`, cited by name, never re-derived here).

**What transmission actually did.** MCLR became the mandatory lending-rate benchmark from April 2016
(`partC-data.md`'s taxonomy); despite the new mechanism, RBI itself publicly flagged continued slow
transmission through 2016 and reviewed the MCLR regime's own design — the same chronic complaint
recurring under a new benchmark. The 2019 easing's pass-through would only turn faster on the
retail/EBLR-eligible segment once the **External Benchmark Lending Rate (EBLR)** mandate arrived
(October 2019, `partC-data.md`'s fourth regime) — post-dating most of the 2019 cuts, so the bulk of
that year's 135bp still transmitted through the older, stickier MCLR mechanism
`[VERIFY: an isolated 2019 WALR pass-through coefficient net of the EBLR transition]`. Credit growth
remained weak through the IL&FS funding freeze's real-economy transmission, consistent with the
cross-referenced FY20 slowdown above.

**Duration.** Several distinct, comparatively short regimes packed into three years: a **LOOSE leg,
October 2016 – August 2017 (roughly 10 months)**, interrupted mid-way by the two-week demonetisation
liquidity shock; a **long hold, August 2017 – June 2018 (roughly 10 months)**; a **short TIGHT leg,
June – August 2018 (2 months)**; and a **LOOSE leg, February – October 2019 (roughly 9 months)**.

**L6's lagged-regime read.** The busiest short-regime stretch in the chronology, and the one where
L6's 1-year lag has the most within-window whipsaw potential: a lagged L6 would still read
**LOOSE-and-easing** into the 2018 hikes' own early months (the 6.00% hold's long trailing window),
flipping to a brief **TIGHT** read only around mid-to-late 2018 — almost exactly as the 2019 easing
was already underway. This is why the seat treats regime persistence, not the raw rate level, as the
informative object (`partDEFH...` Part D), and exactly the episode density §B.3 below treats as noise
inside a longer regime rather than several independently countable campaigns.

---

### 7. 2020–2022 — the COVID floor, then the inflation-shock hiking cycle

**The rate path — the floor.** RBI cut repo **75bp to 4.40% on 27 March 2020** as the national COVID
lockdown began, with the **reverse repo cut by a larger 90bp to 4.00%** the same day — an explicitly
asymmetric corridor move designed to discourage banks from simply parking funds rather than lending.
A further **25bp reverse-repo-only cut to 3.75% followed on 17 April 2020** (no repo change), and then,
in an **off-cycle MPC meeting on 22 May 2020**, both rates moved again: **repo −40bp to 4.00%,
reverse repo −40bp to 3.35%** — the record-low floor the desk's own brief names. **[Verified — the
27 Mar 2020 and 22 May 2020 dates/levels; the 17 Apr 2020 reverse-repo-only cut.]** This floor then
**held for an unusually long stretch, roughly 22 months, May 2020 through April 2022** — the longest
unbroken hold in this entire chronology. With banking-system liquidity in sustained, large surplus
throughout, the **reverse repo — not the repo rate — was the de-facto operative rate** for much of
this window, a far more durable instance of the pattern first seen briefly in late 2016 (§6). RBI's
toolkit went well beyond the corridor: **Targeted Long-Term Repo Operations (TLTRO)** from March 2020
(TLTRO 2.0 targeting NBFCs/MFIs specifically, ₹50,000 crore first tranche, half earmarked for
small/mid-sized NBFCs), and the **Government Securities Acquisition Programme (G-SAP)**, RBI's own
QE-adjacent bond-purchase toolkit, announced 2021 to backstop the G-sec market
`[VERIFY: exact G-SAP tranche sizes/dates]`. Forward guidance was explicitly **"accommodative as long
as necessary to revive growth on a durable basis, while ensuring inflation remains within the
target"** — repeated across successive statements, abandoned only once the 2022 hiking cycle began.

**The rate path — the inflation-shock hiking cycle.** RBI formally introduced the **Standing Deposit
Facility (SDF)** at **3.75%** on **8 April 2022**, explicitly designed to **replace the reverse repo as
the floor of the LAF corridor** — a non-collateralized absorption tool requiring no G-sec pledge,
closing the corridor-mechanics gap the 2020–22 surplus-liquidity era had exposed. **[Verified — the
SDF's 8 April 2022 introduction and its explicit design purpose of replacing reverse repo as the
corridor floor.]** Less than a month later, in a **surprise off-cycle MPC meeting on 4 May 2022**, RBI
raised the repo rate **40bp to 4.40%** — the first hike in 45 months, since August 2018 (§6) — alongside
a **50bp CRR hike to 4.50%**, withdrawing an estimated **₹87,000 crore** of liquidity. **[Verified —
the 4 May 2022 date, the 40bp/4.40% repo move, the "first hike in 45 months" characterization, and the
simultaneous 50bp CRR hike.]** The campaign then continued on the regular bi-monthly calendar: **50bp
to 4.90% (8 Jun 2022) → 50bp to 5.40% (5 Aug 2022) → 50bp to 5.90% (30 Sep 2022) → 35bp to 6.25% (7 Dec
2022) → 25bp to 6.50% (8 Feb 2023)** — a cumulative **250bp of tightening, May 2022 – February 2023**,
front-loaded (three consecutive 50bp moves) before decelerating to 35bp then 25bp as inflation began
cooling. **[Verified — the complete hike-by-hike date/level path and the 250bp cumulative total.]**

**Stated rationale.** The 2020–22 floor was an explicit, unambiguous crisis response to the COVID
shock — the one unambiguous classical recession in this entire record on any dating convention
(`docs/cycles/18-business-cycle.md` Part B case 7: Q1 FY21 GDP contracting 23.9% year-on-year,
manufacturing −39.3%, the first quarterly GDP contraction since India began publishing quarterly data
in 1996; cross-referenced, never re-derived here). The 2022 hiking cycle's rationale was equally
explicit and stated in real time: Governor Das's own words accompanying the May-2022 move cited "the
strengthening of inflationary impulses in sync with the persistence of adverse global price shocks" —
the Russia-Ukraine war's own commodity and energy price transmission, layered onto already-elevated
post-COVID demand.

**What transmission actually did.** The 2022–23 hiking cycle is the single best-documented transmission
episode in this entire record on the asymmetry question §B.4 closes below: the one-year median MCLR
rose **120bp** against the 250bp cumulative repo hike, while medium-term deposit rates moved up only
**78bp** over the same window — a **>40bp gap** between what banks charged borrowers and what they paid
depositors, directly widening net interest margins during the hiking phase. Weighted-average lending
rates on **fresh** rupee loans rose **137bp** and on **outstanding** loans **80bp** across May–December
2022 against the 225bp of hikes delivered by that point, while **external-benchmark-linked (EBLR)**
loans — by then roughly **47.6% of outstanding floating-rate rupee credit**, against MCLR-linked loans'
**46.5%** share (September 2022) — repriced mechanically and in near-full lockstep with the repo move,
by construction. **[Verified — the 120bp/78bp MCLR-vs-deposit gap, the 137bp/80bp fresh/outstanding
WALR figures, and the EBLR/MCLR outstanding-loan share split, all sourced to the same contemporaneous
banking-sector analysis.]**

**Duration.** The COVID floor is the longest sustained single-level hold in this entire chronology —
**roughly 22 months, May 2020 – April 2022**; the hiking cycle that followed is comparatively fast —
**roughly 9 months, May 2022 – February 2023** — for a cumulative move (250bp) smaller than the 2004–08
Reddy campaign's 300bp but delivered in barely a fifth of the time.

**L6's lagged-regime read.** A lagged L6 would have read the effective rate as decisively **LOOSE**
throughout 2021 — the trailing 12-month window dominated by the 2020 cuts, with no ambiguity given the
regime's own 22-month duration. The interesting case is the transition: by the time L6's own 1-year lag
would have flipped the classification to **TIGHT** (roughly mid-2023, a year into the 2022 hiking
cycle), the campaign itself had *already ended* (the last hike landed February 2023) — meaning L6's
lagged TIGHT read would have arrived just as the regime it was describing was giving way to the
multi-year plateau §8 below documents, a textbook instance of the seat reading a regime's *aftermath*
rather than its live state, precisely the tradeoff the ladder accepts in exchange for never trading a
same-day event.

---

### 8. 2023–2026 — the plateau, and the current easing

**The rate path — the long hold.** Repo held at **6.50% for eleven consecutive bi-monthly reviews,
February 2023 through December 2024** — the longest unbroken *no-change* stretch (as opposed to
easing/tightening duration) in the MPC-era record. The **6 December 2024** review — Governor
Shaktikanta Das's last before **Sanjay Malhotra took office as Governor on 11 December 2024** —
delivered a **50bp CRR cut, from 4.50% to 4.00%, phased in two 25bp steps on 14 and 28 December 2024**
— releasing an estimated **₹1.16 lakh crore** of primary liquidity, with repo itself left unchanged.
**[Verified — the 50bp/two-step CRR cut, its December dates, and the ₹1.16 lakh crore figure.]** Under
Malhotra, the plateau then broke: **repo −25bp to 6.25% (7 Feb 2025)** — the **first cut in nearly
five years**, the prior cut having been May 2020 — followed by **−25bp to 6.00% (9 Apr 2025)**, then a
**larger, "jumbo" −50bp to 5.50% (6 Jun 2025)**, delivered alongside a **100bp CRR cut phased in four
equal 25bp tranches, taking CRR from 4.00% to 3.00% by December 2025**, and an explicit **policy-stance
change from "accommodative" to "neutral."** **[Verified — the complete Feb/Apr/Jun 2025 date/level
path, the June-2025 CRR-cut magnitude and phasing, and the stance change.]** RBI then **held at 5.50%
through August and October 2025** — the August pause explicitly
attributed to assessing the impact of a US tariff escalation on Indian exports (doubling from 25% to
50%) — before delivering a **final 2025 cut of 25bp to 5.25% in December 2025**, taking the calendar-
year total to **125bp of easing (6.50%→5.25%)**, the RBI's own characterization: "the most aggressive
easing cycle in six years." **[Verified — the Aug/Oct 2025 holds, their tariff-related framing, and the
December-2025 cut/cumulative-2025 figures.]** As of this writing, repo has held at **5.25% for four
consecutive reviews since the December 2025 cut** (through the **August 2026** review, 3–5 August 2026,
which kept the repo rate, SDF (5.00%) and MSF/Bank Rate (5.50%) all unchanged, retaining the neutral
stance while raising the FY27 GDP growth forecast to 6.7%). **[Verified — the August-2026 hold, the
"fourth consecutive review unchanged" characterization, and the accompanying rate levels; the FY27
inflation-forecast figure attached to that same review carries `[VERIFY: the exact print — sourced
figures were internally inconsistent this pass]`.]**

**Stated rationale.** The 2023–24 hold reflected inflation still running above the 4% target midpoint
even as it moderated from the 2022 shock; the Dec-2024 CRR cut (without a repo move) was an explicit
liquidity-only operation, distinct from the rate decision, in the same spirit as the Nov-2016
incremental-CRR episode (§6) though opposite in direction and far larger in scale. The 2025 easing
cycle was explicitly framed around **growth losing momentum alongside inflation approaching the 4%
target** — the mirror image of the 2011–13 stagflation squeeze (§4), this time with both legs
(disinflation and growth concern) pointing the same direction rather than in tension. The June-2025
jumbo cut and simultaneous stance shift to neutral was explicitly framed as **front-loading** easing
while conditions still allowed it, with the neutral stance itself signaling no further mechanical
commitment either way.

**What transmission actually did.** With EBLR-linked loans by 2025 a substantially larger share of
outstanding retail credit than in 2022 (the share rises mechanically as new origination replaces older
MCLR-linked stock, per `partC-data.md`'s "EBLR share rising = lags shortening" note), the 2025 cuts are
expected structurally to pass through faster on the retail book than the 2022 hikes did in reverse on
deposits — a matched fresh-vs-outstanding WALR comparison `[VERIFY: not independently computed this
pass; registered as MP-D1's own data-phase task, `partDEFH-math-algo-harvest-ledger.md` Part F]`.
Credit growth through 2024–25 remained elevated enough relative to deposits that the deposit-war
dynamic (§B.4) persisted well past the point the hiking cycle had ended.

**Duration.** The 2023–24 hold is the longest **no-change** plateau in the record — **roughly 24
months, February 2023 – February 2025**; the 2025 easing leg that followed runs **roughly 10 months,
February – December 2025**, followed by an **ongoing hold, December 2025 – August 2026 (at least 8
months as of this writing)**, whose eventual length is, by the ladder's own design discipline, not a
forecast this Part will offer (`partDEFH...` Part H: "the current easing cycle's terminal point ...
L6 reads the regime lagged and refuses the forecast").

**L6's lagged-regime read, as of writing (2026-09-02) — the desk's live regime, stated as a regime,
never a forecast.** A lagged L6 reading the effective rate roughly a year behind — i.e., informed by
the rate path through roughly Q3 2025 (repo at 5.50%, mid-way through the 2025 easing leg, CRR cuts
still phasing in) — would today classify the regime **LOOSE and comparatively young**: the active
easing began February 2025, roughly 19 months before this writing, still well inside the seat's own
12–24 month `tau_half` band rather than deep into an aging tail. The regime's own internal composition
— front-loaded cuts (Feb/Apr/Jun 2025, 125bp) followed by a lengthening hold (Aug 2025 – Aug 2026, at
least four consecutive reviews unchanged) — reads, on the ladder's own state-phase convention
(`config/ladder.yaml`'s `state_phase_convention`), as a LOOSE level with **decelerating (flattening)
velocity** — a quadrant the convention itself would classify as moving from "recovery" toward
"slowdown-of-the-easing-itself," not a reversal, and — per that same convention's own consumption rule
— logged and displayed for monitoring only, never yet branching a traded rule on the quadrant read.
This is a regime description, not a forecast: L6's own design (§B.3 below) explicitly refuses to say
whether 5.25% is the cycle's trough or merely its most recent stop.

---

## B.2 The cycle table

| Campaign | Direction | Duration | Peak-to-trough move | Transmission lag observed | L6 regime read |
|---|---|---|---|---|---|
| 1998 Jan Asian-crisis defense | TIGHT (shock) | ~2 months | Bank Rate 9%→11% (+200bp) | too brief to observe | filtered out by the 1y lag; never registers as a distinct regime |
| 1998–2003/04 Jalan easing | LOOSE | ~5–6 years | Bank Rate/repo ~11%→~6%; CRR 15%→4.5% | directional easing, PLR-era, magnitude `[VERIFY]` | LOOSE-and-aging throughout; no ambiguity (monotonic) |
| 2004–2008 Reddy tightening | TIGHT | ~4y 4m | repo 6.00%→9.00% (+300bp); CRR to ~9% | lending rates up, credit growth soft only late-cycle | TIGHT-and-aging from ~2005; still TIGHT a year into the 2008–09 reversal (stale) |
| 2008–2009 crisis easing | LOOSE | ~9 months | repo 9.00%→4.75% (−425bp); CRR 9%→5% | fast policy move, pass-through slower/partial `[VERIFY]` | reads LOOSE only ~mid-2009, a year behind the crisis itself |
| 2010–2011 normalization | TIGHT | ~18 months | repo 4.75%→8.50% (+375bp, 13 hikes) | lending rates up promptly; deposit rates lagged | still reads LOOSE through most of the hiking leg (lag artifact) |
| 2011–2013 stagflation + Jul-2013 taper defense | TIGHT-then-mixed | ~13mo easing + ~6mo defense | repo 8.50%→7.25%; MSF +300bp to 10.25% (Jul 2013, 2 months) | MSF episode: funding-cost spike, no credit-quality event (shadow-deep SC1 57th pctile) | LOOSE-and-young into the MSF shock; L2 (fast layer), not L6, owns the 2-month spike |
| 2014–2016 Rajan disinflation | LOOSE | ~15 months active easing | repo 8.00%→6.50% (−150bp); 125bp in 2015 alone | Base-Rate-era, RBI itself flagged slow pass-through | TIGHT-but-turning through 2015; LOOSE only by ~mid-2016 |
| 2016–2019 MPC early years | mixed (LOOSE / shock / TIGHT / LOOSE) | 4 sub-regimes, 2–10 months each | repo 6.25%→6.00%→6.50%→5.15%; Nov-2016 incremental CRR 100% (2 weeks) | MCLR-era; 2019 EBLR-eligible loans faster; corporate MCLR book stickier | busiest whipsaw stretch in the record; lag actively works against regimes this short |
| 2020–2022 COVID floor + inflation-shock hiking | LOOSE-then-TIGHT | 22mo floor + 9mo hiking | repo 5.15%→4.00%→6.50% (+250bp, May2022–Feb2023); CRR +50bp (May 2022) | MCLR +120bp vs deposits +78bp (>40bp gap); EBLR loans ~47.6% repriced near-lockstep | LOOSE throughout 2021 (unambiguous); TIGHT read only ~mid-2023, just as the campaign had already ended |
| 2023–2025 plateau + 2025 easing | HOLD-then-LOOSE | 24mo hold + 10mo easing (ongoing hold since) | repo 6.50%→5.25% (−125bp, Feb–Dec 2025); CRR −150bp cumulative (Dec2024+2025) | EBLR share higher than 2022; faster pass-through expected, not yet matched-computed `[VERIFY]` | **as of writing: LOOSE and comparatively young (~19 months); decelerating velocity; a regime, not a forecast** |

---

## B.3 An honest count of completed round trips (closing MP-D3)

The ladder's own `changes_if` for `L6_monetary_stance` (`config/ladder.yaml`) reads: *"a 6th completed
round trip; primary RBI DEPR citation."* Dossier 08 (`research/dossiers/08-india-mid-cycles.md`, §I1)
already flags this count as **boundary-sensitive**, landing at "n≈4–5" depending on whether the
2009–2019 span is read as one long, wobbly cycle or two. This Part owes the desk an explicit argument,
not a restated hedge.

**Method.** Define a **completed round trip** as a full **trough → peak → trough** sequence in the
effective policy rate (Bank Rate pre-2001, repo thereafter), where a "trough" or "peak" is a genuine
local extremum — a point the rate does not revisit before moving materially in the *other* direction —
and where a subsequent move that does **not** clear the prior extremum (a "lower high" or "higher low")
counts as a **wobble inside the existing regime**, not a fresh cycle. This convention is chosen
specifically to resolve the 2011–2016 ambiguity dossier 08 itself names: the Jul-2013 MSF/taper defense
pushed conventional repo only to **8.00% (Jan 2014)**, which sits *below* the **8.50% (Oct 2011)** peak
it followed — a lower high, and therefore, on this convention, a wobble inside one long regime rather
than a second, independently countable cycle.

**The turning points, dated.** Applying this convention to the full chronology in §B.1 above:

| # | Type | Date | Level | Confirmed how |
|---|---|---|---|---|
| P0 | Peak (partial; boundary observation, pre-modern-corridor) | Jan 1998 | Bank Rate 11% | shock, resolved same year — not a regime-scale peak on the ladder's own tau_half band |
| T0 | Trough | ~Mar 2004 | repo 6.00% | confirmed local minimum; Reddy tightening begins immediately after |
| P1 | Peak | 30 Jul 2008 | repo 9.00% | confirmed; crisis easing begins immediately after |
| T1 | Trough | ~Apr 2009 | repo 4.75% | confirmed; 2010 normalization begins immediately after |
| P2 | Peak | Oct 2011 | repo 8.50% | confirmed; 2012–13 easing begins immediately after |
| (wobble, not P/T) | — | Jul 2013–Jan 2014 | MSF +300bp; repo to 8.00% | **lower high** (8.00% < 8.50%) — inside the same regime as P2→T2, per the stated convention |
| T2 | Trough | Aug 2017 | repo 6.00% | confirmed local minimum (lowest since Nov 2010); Jun-2018 hikes begin after a hold |
| P3 | Peak | 1 Aug 2018 | repo 6.50% | confirmed; 2019 easing begins immediately after |
| T3 | Trough | 22 May 2020 | repo 4.00% | confirmed; a genuine new record low, not merely a revisit of T1 |
| P4 | Peak | 8 Feb 2023 | repo 6.50% | confirmed; 2023–24 hold, then 2025 easing, begins after |
| T4 | Trough (tentative — **not yet confirmed**) | Dec 2025–ongoing | repo 5.25% | **held, not reversed, as of Aug 2026** — could still fall further before the next hike; this Part explicitly declines to certify it |

**The count.** Reading trough-to-trough:

- **Round trip A**: T0 (2004) → P1 (2008) → T1 (2009). **COMPLETE.**
- **Round trip B**: T1 (2009) → P2 (2011) → T2 (2017), the 2013 MSF/taper episode absorbed as an
  internal wobble. **COMPLETE**, though exactly the span dossier 08 flags as contestable — a reader
  treating the Jul-2013 MSF spike as its own cycle (the *rates market* genuinely inverted, even though
  *conventional* repo never made a new high) would split this into two round trips instead of one,
  changing the total by exactly one either way. This Part's convention (peaks/troughs on conventional
  repo/Bank-Rate, not the MSF corridor) treats it as one; the disagreement is worth carrying forward
  rather than resolving by fiat, in the spirit `docs/cycles/18-business-cycle.md` Part B insists on.
- **Round trip C**: T2 (2017) → P3 (2018) → T3 (2020). **COMPLETE** — a short but genuine cycle; the
  2018 hike is a real, if small, new high (6.50% > 6.00%), and the 2020 low is a genuine new record,
  not a mere revisit.
- **Round trip D**: T3 (2020) → P4 (2023) → T4 (2025–ongoing). **NOT YET COMPLETE.** The peak leg
  is fully confirmed; the trough leg is not. As of this writing, repo has held at 5.25% for four
  consecutive reviews with no confirmed reversal to tightening — it is entirely possible 5.25% is
  already the cycle's low and a future hike will confirm it retroactively, but this Part explicitly
  declines to certify that today, exactly as §8's own closing paragraph states as a matter of design
  discipline, not merely caution.

**The honest answer.** By this record's own most defensible, single, non-arbitrary convention, the
1997–2026 chronology contains **three fully completed round trips (A, B, C)**, with a **fourth
currently in progress and not yet confirmable (D)**. A reader who instead splits round trip B at the
2013 MSF wobble gets **four** completed round trips instead of three — still short of a fifth, let
alone a sixth. **No defensible convention this Part can construct reaches six.** Dossier 08's own
"n≈4–5" is therefore, if anything, generous relative to the strict trough-to-trough convention applied
here (which yields 3, or 4 under the alternative split) — both readings converge on the same
consequence: **the ladder's own `changes_if` trigger — a 6th completed round trip — has not fired, and
on any convention this Part can defend, remains at minimum one and as many as three full cycles away.**
This is not a reason to distrust the seat; it is exactly why the seat is Tier B with parameters frozen
at inception (`config/ladder.yaml`) rather than Tier A fitted with purged CV (`research/CONTRACT.md`
§4) — the count itself is the evidence that more data, not a parameter re-fit, is what the seat still
needs. **MP-D3 is closed by this section**, per `partDEFH-math-algo-harvest-ledger.md` Part F's own
registration.

---

## B.4 The transmission-asymmetry record (closing MP-D2)

Every episode in §B.1 that carries a directional transmission read points the same way, and the
record is dense enough across nine decades — three distinct lending-rate regimes (BPLR, Base Rate,
MCLR) plus a fourth structural fix (EBLR) — to state the asymmetry plainly rather than as a single
anecdote.

**(i) Hikes pass through faster than cuts, structurally, across every regime this record covers.**
Under the pre-2010 BPLR/PLR system, RBI's own repeated public complaints about slow transmission
(explicitly on cuts, rarely on hikes) run through the Jalan-era easing, the crisis-era 2008–09 cuts,
and the 2015 Rajan disinflation alike — a chronic, cross-regime pattern rather than a single episode's
peculiarity. The clearest **quantified** instance sits in the 2022 hiking cycle: the one-year median
MCLR rose 120bp against 250bp of cumulative repo hikes, while medium-term deposit rates rose only
78bp over the same window — banks captured the spread on the way up, passing the hike through to
borrowers faster and more completely than to depositors. **[Verified figures, §B.1 case 7.]**

**(ii) The EBLR mandate (October 2019) is a genuine structural break in this asymmetry, but only for
the segment it covers.** Loans linked to an external benchmark (the repo rate itself, for most banks)
reprice mechanically and near-simultaneously with an MPC decision, by regulatory construction — the
September-2022 snapshot already shows EBLR-linked loans at roughly 47.6% of outstanding floating-rate
retail credit, essentially matching MCLR's 46.5% share even that early in the transition. This is the
single clearest instrument this record contains for closing the historical asymmetry — but it applies
overwhelmingly to new retail-and-MSME originations; the corporate lending book remains substantially
MCLR-linked, and MCLR itself reprices on a lag (typically monthly-to-quarterly reset dates) even after
a policy move, meaning the asymmetry has narrowed for one segment of the credit book and persisted for
another, a bifurcation `partC-data.md`'s own "EBLR share rising = lags shortening" monitoring note is
built to track over time rather than assume resolved.

**(iii) Deposit-war episodes are the mirror-image signature: banks catching up on the liability side
*after* a hiking cycle has already ended, not during it.** The clearest instance is **2022–2024**: as
credit growth ran at **17.4% year-on-year (June 2024)** against deposit growth of only **11.1%**,
banks — ICICI, RBL, Axis, IDFC First among those named in contemporaneous reporting — raised deposit
rates repeatedly through late 2022 into 2023–24 to fund continuing credit demand, the aggregate
loan-to-deposit ratio reaching a **two-decade high of ~80% by December 2023**, the incremental
credit-deposit gap running **over 700bp** at the start of 2024 before narrowing to **~200bp**
`[VERIFY: exact narrowing date]`. **[Verified — the 17.4%/11.1% split, the named banks' actions, the
~80% LDR, and the 700bp→200bp narrowing.]** The 2022 hiking cycle's own asymmetry (fast lending-rate
pass-through, slow deposit pass-through, per (i)) did not resolve once the hikes stopped in February
2023 — it forced a *second*, delayed round of deposit competition well into 2023–24, as banks
discovered their funding could not keep pace with the credit growth the hiking cycle had failed to
choke off. Earlier candidate episodes — a plausible 2010–11 post-crisis deposit scramble (§B.1 case
3) or the 1994–96 primary-market boom's own funding competition — are directionally consistent but
**not independently verified this pass**, flagged `[VERIFY]` rather than asserted.

**(iv) The net design implication for L6.** The asymmetry is not merely a curiosity for the cycle
narrative — it is a first-order reason the seat's own construction (`partDEFH...` Part E) reads the
*effective rate itself*, never a bank-lending-rate proxy, as the primary input: a signal built on
WALR or MCLR directly would inherit this asymmetry's own regime-dependence (BPLR-era stickiness,
MCLR-era partial improvement, EBLR-era near-completeness for one segment only) as an additional,
unmodeled source of drift across the ladder's own 1997–2026 estimation window, on top of the
`tau_half` drift the seat's `tau_half_drift_policy` (`config/ladder.yaml`) already tracks explicitly.
Reading the policy rate itself and letting the credit-growth transmission chain (MP-D1's own
replication design) carry the pass-through question separately keeps L6's own construction clean of
this asymmetry, at the cost of the lag the seat already accepts by design. **MP-D2 is closed by this
section**, per `partDEFH-math-algo-harvest-ledger.md` Part F's own registration: the pass-through
asymmetry runs hikes-fast/cuts-slow on the lending side, cuts-somewhat-faster-post-EBLR on the retail
segment specifically, and deposit-side competition arrives as a *lagged*, not contemporaneous,
response to a credit-growth gap the hiking cycle itself often fails to close before it ends.

---

## References

RBI, Monetary Policy Statements and DBIE historical rate tables (repo, reverse repo, MSF, SDF, Bank
Rate, CRR, SLR) — primary source for every date/level pair above, accessed via secondary aggregation
this session (DBIE egress blocked per `research/CONTRACT.md` §7 Known Prior #11; every figure
cross-checked across ≥1 independent source, `[VERIFY]` retained where only one was found). · RBI,
*Report of the Expert Committee to Revise and Strengthen the Monetary Policy Framework* (Urjit Patel
Committee, Jan 2014). · RBI–Government of India, *Monetary Policy Framework Agreement* (Feb 2015). ·
Finance Act, 2016. · `docs/cycles/18-business-cycle.md` Part B (Atlas 2.3, activity-side chronology,
cross-referenced throughout, never re-derived). · `research/cycles/fincycle-deep/partB-cases.md` §B3
(India property-cycle record). · `research/cycles/shadow-deep/partB-cases.md` §B5 (2013 MSF episode's
NBFC-side negative control). · `research/cycles/credit-deep/partB-cross-country.md` case #10 (twin-
balance-sheet decade). · `research/dossiers/08-india-mid-cycles.md` §I1–I2 (the seat's prior repo
chronology, extended here). · `research/register/trial-ledger.md` MP1–MP3 and this directory's own
`mp-RESULTS.md` (the JST-analogue trials each "L6 lagged-regime read" applies episode-by-episode). ·
this directory's `partC-data.md` (the effective-rate/lending-rate-regime taxonomy) and
`partDEFH-math-algo-harvest-ledger.md` (the MP-D2/MP-D3 designs this Part closes).

---

# PART B-RESULTS — Analogue data: JST R6 (MP1–MP3, pre-registered)

# Atlas 2.6 — monetary-policy cycle: JST analogue trials (MP1-MP3, pre-registered)

Matched 1y-change legs on both sides (the BC2 standing warning applied at design
time); magnitude floor declared. Interpretation AFTER the print.

## MP1 — does the policy rate lead credit growth, negatively?

| Country | most-negative corr | at lag |
|---|---|---|
| AUS | -0.18 | -2 |
| BEL | -0.06 | +2 |
| CAN | -0.07 | +1 |
| CHE | -0.06 | +3 |
| DEU | -0.15 | +1 |
| DNK | -0.06 | +1 |
| ESP | -0.08 | +3 |
| FIN | -0.13 | -2 |
| FRA | -0.10 | +1 |
| GBR | -0.12 | -3 |
| IRL | -0.12 | +2 |
| ITA | -0.04 | +1 |
| JPN | -0.14 | +1 |
| NLD | -0.07 | +2 |
| NOR | -0.06 | +3 |
| PRT | -0.17 | +2 |
| SWE | -0.03 | +1 |
| USA | -0.12 | +1 |

- Qualifying countries (floor ≤ −0.10): 9/18; of those, share
  with the minimum at lag ≥ +1 (rate leads): **67%** (bar ≥60%): **PASS**.

## MP2 — the lag profile (measurement, prior set)

| horizon (years ahead) | mean per-country corr(Δstir_t, credit growth_t+h) |
|---|---|
| +0 | +0.069 |
| +1 | -0.056 |
| +2 | -0.035 |
| +3 | -0.013 |

## MP3 — campaign persistence (measurement, prior set)

- P(next year's Δstir has the same sign): **53%** pooled — tightening/easing come in CAMPAIGNS, the regime reading's justification.

## Honest read (written AFTER the print)

- **MP1 PASSES with matched legs and a floor** (9 qualifying countries, 67% placing the most-
  negative correlation at rate-leads lags): the transmission direction survives the BC2-grade
  test that killed the credit-leads-growth import. Magnitudes are small (floor-qualifying
  minima around −0.10..−0.25 territory) — the direction is real, the per-year signal is weak,
  which is exactly why L6 consumes a lagged REGIME, not a fresh print.
- **MP2 is the entry's best exhibit: the profile flips sign across the lag.** Contemporaneous
  corr is POSITIVE (+0.07 — central banks tighten INTO credit booms: the reaction function
  face), then NEGATIVE at +1y (−0.06, the peak), decaying at +2/+3. The seat's "lagged ~1y"
  convention now has its analogue calibration — and the sign flip is the measured reason a
  same-day stance read MISLEADS: this year's hike is a symptom of the boom; next year's credit
  is where the medicine shows.
- **MP3 surprises honestly: 53% — annual DIRECTION-of-move persistence is a near coin flip.**
  Campaigns exist in the narrative record (the cases chapter's rate paths) but at annual
  granularity pauses and reversals wash the sign signal out. Refinement for L6, recorded here:
  the regime content lives in the stance LEVEL (loose/tight vs a neutral reference), not in
  the momentum of last year's move — which is what the seat's "stance classified loose/tight"
  wording already says; MP3 closes the door on a Δ-based variant.
- No bar was moved; MP2/MP3 were registered as measurements and stay measurements.

---

# PART C — Data engineering: the stance variables, free

# Part C — Data engineering: the stance variables, free (atlas 2.6; compact, in-house)

*v1.0 · 2026-09-02 · desk principal's chapter. The entry's data surface is narrow and entirely
RBI-published; the engineering problem is SPLICING and the effective-rate question, not access.*

## C.1 The policy-rate path
RBI DBIE: repo rate (operating target since the mid-2000s), reverse repo, MSF (2011-), SDF
(Apr 2022-), Bank Rate (the pre-LAF era's rate), CRR. All step functions with exact change
dates from MPC resolutions/press releases (public, permanent). THE ENGINEERING TRAP: the
EFFECTIVE operating rate migrates — Bank Rate era → repo era → reverse-repo-as-floor era
(2020-22 surplus liquidity: the floor WAS the rate) → SDF era. The desk's series is a
constructed **effective_rate** with regime tags and a breaks-registry entry per migration;
never a naive repo splice. [VERIFY each migration date on pull.]

## C.2 The liquidity leg — the stance banks actually feel
RBI WSS: net LAF position (daily/weekly), the surplus/deficit sign and size (% of NDTL). In
surplus regimes cuts transmit fast and hikes slowly; in deficit regimes the reverse — stance =
(effective real rate, liquidity sign) as a PAIR. Money-market spread cross-check: weighted call
rate minus repo (DBIE daily) — the corridor-position variable.

## C.3 Transmission observables
RBI bulletin monthly: WALR on fresh rupee loans (the transmission endpoint, 2011-), WADTDR
(deposits), 1y median MCLR (2016-), share of EBLR-linked loans (semiannual FSR table). These
are the MP-D1 replication legs. Breaks: BPLR→Base(2010-07)→MCLR(2016-04)→EBLR(2019-10) — four
lending-rate REGIMES; series never spliced across them without regime dummies (registry).

## C.4 Inflation legs for the real-rate read
CPI combined (2012-) for the MPC era; WPI for history before it — the real-rate series carries
a declared deflator break at the 2014-15 CPI adoption (registry; both variants published).

## C.5 PIT hazards
| Hazard | Rule |
|---|---|
| Effective-rate migrations (C.1) | regime tags + breaks registry; both variants retained |
| Lending-rate regime changes | never spliced silently (C.3) |
| MPC minutes revisions | resolutions are final; minutes lag 14 days — stance reads use resolution dates only |
| Liquidity denominators (NDTL revisions) | fortnightly vintage kept |

## C.6 Runsheet addendum 9 (steps 52-56)
52. DBIE policy-rate suite backfill + effective_rate construction with regime tags ~3-4h
53. WSS net-LAF backfill (weekly, 2000s→) + call-rate spread ~3-4h
54. Bulletin WALR/WADTDR/MCLR monthly transcription (2011→) ~4-5h
55. MP-D1 acceptance registration (repo→WALR→credit chain, BEFORE the look) ~2h
56. L6 stance classifier run + first India lagged-regime series, sentinel wiring ~3-4h
Total ~15-19h.

---

# Parts D–H — stance math, algorithm, harvest, ledger (atlas 2.6; seat L6, Tier B)

## Part D — What MP1–MP3 permit

MP1 (matched legs, floor, 67% PASS) licenses the transmission DIRECTION the seat assumes —
notably the only imported lead-lag direction in the register to SURVIVE a BC2-grade test.
MP2 calibrates the lag: the profile flips from +0.07 contemporaneous (the reaction-function
face — hikes arrive INTO booms) to a −0.06 peak at +1y. Two consequences carved into the
seat's algebra: (i) the ~1y lag convention now has its analogue number; (ii) the SIGN FLIP is
the formal reason same-day stance reads mislead — an unlagged L6 would load positively on
euphoria, the exact double-count the macro block exists to prevent. MP3 (53%) closes the
Δ-based stance variant: regime content is the LEVEL pair (effective real rate vs its own
expanding percentile; liquidity sign), never last year's move direction. Magnitudes are small
throughout — the seat trades a slow regime, not an annual signal, and tau_half 12-24m stays.

## Part E — The algorithm (L6, monthly)

```
STEP 1  effective_rate (partC C.1 splice, regime-tagged) − CPI trend = real stance rate;
        expanding percentile (shared grids); liquidity sign from net-LAF (C.2)
STEP 2  stance class = {loose, neutral, tight} from the percentile bands declared in the
        registry, CONDITIONED on liquidity sign agreement (disagreement -> neutral + flag)
STEP 3  the block consumes stance LAGGED ~1y (MP2's calibration; exact lag from the
        registered grid) — never same-day; no event-trade path exists in the interface
STEP 4  MPC-day handling: L2 (fast layer) owns event vol mechanically; L6 does NOTHING
        on announcement days by construction
MONITOR annual MP1-MP3 re-run; effective-rate migration watch; EBLR share (transmission
        speeds UP as it rises -> the lag grid re-estimates at the annual loop, hysteresis)
FAILURE MODES: operating-framework redesign (registry + variant series); surplus-liquidity
        eras making the repo rate cosmetic (C.2's pair handles); deflator break (C.4)
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| macro_credit block | the lagged loose/tight regime (L6's existing seat, now calibrated) |
| L10/L12 reads | the reaction-function caveat: tightening co-prints with hot credit — joint reads use the FLIP, not the level alone |
| Hedge scheduling | tight-and-aging regimes join the watch context |
| Cycle School | Lesson 20: the sign flip; why the desk ignores announcement days |

Designs: **MP-D1** India transmission replication (effective_rate → WALR → sectoral credit,
monthly, matched transforms + floor; acceptance registered at runsheet step 55 BEFORE the
look). **MP-D2** asymmetry: pass-through speed hikes vs cuts (deposit-war conditioning),
registered with MP-D1. **MP-D3** the round-trip count: the cases chapter argues the completed-
campaign count against the ladder's changes_if ("6th completed round trip") — the graduation
clock is explicit and public.

## Part H — Knowledge ledger (atlas 2.6)

**Established (analogues, our runs):** transmission direction survives matched-legs testing
(MP1 — the register's only surviving imported direction); peak effect at +1y with a
contemporaneous sign FLIP (MP2); stance is level-content, not move-content (MP3, 53%).
**India [the seat's country]:** the policy-cycle record is the cases chapter's table; the
completed round-trip count is argued there against changes_if; transmission is regime-dependent
(EBLR share rising = lags shortening — the annual re-estimate watches).
**Unknowable:** the current easing cycle's terminal point; L6 reads the regime lagged and
refuses the forecast. **Process:** the BC2 standing warning did its first constructive job —
MP1 was DESIGNED to survive it or fail honestly, and it survived.
