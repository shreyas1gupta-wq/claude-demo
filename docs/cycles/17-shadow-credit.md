# Shadow Credit — Sub-Component Monograph (Atlas 2.2; inside L10, feeds L2)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** NO new seat, NO new budget — and that is the deliverable. The composition
leg (NBFC/unsecured share) was already seated inside L10 by the credit monograph; market stress
is already L2's seat; what this entry OWNS is the funding-freeze signature — a CP-spread leg
plus a rollover-collapse leg offered to L2's existing input family, acceptance bars registered
when the data lands (two-pass rule). A "shadow-credit seat" would be two seated states wearing
a third name; the de-dup proof is Part D3.

**Headline results:**
- **SC1 (pre-registered) FAIL, informatively:** the IL&FS 12m window put SMB at −24.8% (18th
  percentile) AND the market at −20.2% (16th) — the freeze propagated to a broad macro event
  within a year. That is the measured routing argument: detection lives in funding variables
  at L2's daily/weekly cadence; equity-factor detection is a dead family, print attached.
- **The record:** India has completed the shadow cycle at least twice (1990s deposit-NBFC
  purge; 2018-20 CP-funded NBFC/HFC freeze) with the fragile node MOVING between runs —
  regulatory arbitrage as the conserved mechanism. The IL&FS anatomy (ratings AAA→D in five
  weeks; CP outstandings ₹6.40tn→₹4.15tn; resolution still running in 2026) is the centerpiece.
- **Verification note:** the case agent's search pass CORRECTED this desk's own briefing figure
  (DHFL's 2018-09-21 crash: ~−59.7% intraday, not the −42% assumed) — discrepancy flagged in
  place, per the never-trust-the-brief rule.

**Assembled from:** partA-theory-psychology.md · partB-cases.md · shadow-RESULTS.md ·
partC-data.md · partDEFH-math-algo-harvest-ledger.md.

---

# PART A + G — Run mechanics (six mechanisms, arbitrage as source) and operator psychology

# NBFC / Shadow-Credit Sub-Cycle Deep Dive — Part A & Part G

Part A: Theory — the funding-run machine · Part G: Operator psychology · v1.0 · 2026-09-02 ·
Atlas entry 2.2 (`docs/CYCLE_ATLAS.md` row 78: "Sub-component of L10 (the aggregate); its
funding-freeze signature also feeds L2," Tier B/C). No ladder seat of its own
(`config/ladder.yaml` has no `L_shadow_credit` entry by design — see A.4): the composition leg
lives inside `L10_credit_block`'s input #3, and the funding-freeze leg is a candidate INPUT
family to `L2_fast_stress`. Complements, never duplicates, `research/cycles/credit-deep/
partA-theory-psychology.md` (the credit monograph — especially its §A.4 Kiyotaki-Moore, §A.9
Mian-Sufi, and §A.12 synthesis table, which already seats "unsecured + NBFC share" as L10's
input #3) and this program's own `research/cycles/shadow-deep/shadow-RESULTS.md` (SC1, the
desk's own pre-registered trial) and `research/cycles/shadow-deep/partC-data.md` (the
funding-freeze data chapter this Part's design conclusions must speak to). Style and depth
calibrated to `research/cycles/fincycle-deep/partA-theory-psychology.md`. Status: theory/
citations verified here; the freeze-index construction is partC's; the India-conditioned test
(SC1) has already run and failed its pre-registered bar, informatively — read A.3 before
concluding this entry has no evidence behind it.

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)

---

## PART A — Theory: the funding-run machine

### A.1 The object

**What "shadow credit" means precisely in India.** A Non-Banking Financial Company (NBFC) is a
company registered under Chapter IIIB of the Reserve Bank of India Act, 1934, that carries on
the business of loans and advances, or acquisition of securities, without being a bank — the
one structural feature that matters most for this entry: an NBFC **cannot accept demand
deposits** (no current/savings accounts), is **not part of the payment-and-settlement system**
(cannot issue cheques drawn on itself), and — critically for A.2 — its liabilities are **not
covered by DICGC deposit insurance**, which protects commercial-bank deposits up to ₹5 lakh but
has no equivalent for NBFC paper of any kind. Housing Finance Companies (HFCs) were a separate
category regulated by the National Housing Bank until August 2019, when a Finance Act
amendment moved HFC regulation to the RBI itself, folding them into the same supervisory house
as NBFCs — a consolidation this entry treats as definitional, not incidental: HFCs run the same
CP/NCD funding model against long-tenor mortgage assets that heightens rather than dilutes the
mechanism this Part documents. **[Verified — RBI Act 1934 Ch. IIIB definition; DICGC coverage
scope; 2019 HFC-regulation transfer, standard attribution.]**

**The post-2021 scale-based regulation pyramid.** RBI's October 2021 "Scale Based Regulation"
framework (Master Direction, effective October 2022) replaced a simpler size-threshold binary
with a four-layer structure — **Base Layer** (small NBFCs, sub-₹1,000 crore, P2P platforms,
account aggregators), **Middle Layer** (all deposit-taking NBFCs regardless of size, plus
non-deposit NBFCs ≥₹1,000 crore), **Upper Layer** (named by RBI on risk/systemic criteria,
subject to bank-like capital and governance requirements), and a **Top Layer** deliberately kept
empty — a graduated regulatory response to exactly the lesson IL&FS taught: size and systemic
footprint, not the deposit-taking/non-deposit-taking label the pre-2021 regime organized
around, are what should set the prudential bar. **[Verified — RBI's Oct-2021 Scale Based
Regulation framework and its four-layer structure.]** The sector's own scale by mid-2020s is
large and growing faster than bank credit — press coverage of RBI/industry data places NBFC
credit in the low-₹30-to-low-₹50-lakh-crore range as of FY24–25 depending on definition and
source, projected toward ₹60 lakh crore by FY26, with retail (housing, auto, microfinance)
driving 16–18%/yr growth **[VERIFY: exact AUM figure — press aggregations of RBI FSR data
diverge materially by source and are not independently re-pulled from a primary RBI table this
session; the direction (large, retail-led, growing faster than bank credit) is the load-bearing
claim, not any single rupee figure]** — a scale at which the sector's funding structure is no
longer a niche curiosity but a system-relevant credit channel in its own right.

**Why this is a SUB-CYCLE of L10, not an independent cycle.** The credit monograph's own
framework (`credit-deep/partA-theory-psychology.md` §A.9) already establishes that India's
2021–24 credit upswing runs disproportionately through unsecured retail and NBFC exposure — the
**same borrowers** (households seeking unsecured personal credit, developers financing
construction, small businesses pledging property, microfinance clients, first-time vehicle
buyers) that L10's aggregate credit/GDP gap and composition input are already trying to read.
What differs is not the borrower but the **funder**: a bank funds these loans against retail and
wholesale deposits, largely insured, largely sticky; an NBFC funds the identical loan book
against commercial paper, non-convertible debentures, and bank credit lines — wholesale,
uninsured, and (A.2) rollover-dependent. Same asset side, different, more fragile liability
side — the textbook definition of a sub-cycle rather than a parallel cycle: it inherits L10's
demand-side drivers wholesale and adds one thing L10's bank-centric construction cannot see on
its own, a funding-supply-side fragility layer with its own, much faster clock.

**The atlas's two-route harvest — what is old and what is new here.** Atlas row 2.2 states the
routing explicitly, and this entry is disciplined about which route it owns. **Route one, the
composition leg, is ALREADY SEATED** inside `L10_credit_block`'s input #3 ("share of incremental
credit to unsecured retail + NBFC," `config/ladder.yaml`) — the credit monograph's own A.4
(Kiyotaki-Moore collateral-class weighting) and A.9 (Mian-Sufi household-channel identification)
already argue why that composition series carries real forecasting content, and I5's own
2021–24 chronology is the same data this entry would otherwise be tempted to re-cite. **This
Part does not re-derive, re-argue, or re-weight that seat** — doing so would double-count a
mechanism the credit monograph already owns, exactly the failure mode `docs/CYCLE_ATLAS.md`
§0 warns against ("most 'new' cycle families are projections of states Part I already holds").
**Route two, the funding-freeze signature, is the NEW content this entry owns**: what happens
on the liability side of an NBFC's balance sheet when wholesale funders stop rolling over paper,
how fast that propagates, and why the right home for detecting it is `L2_fast_stress` at
daily/weekly cadence rather than a monthly credit-quantity read. A.2 builds the mechanism; A.3
reports the desk's own measured test of the propagation claim; A.4 states precisely what gets
added to the design, and — the discipline the whole entry is built around — what does not.

---

### A.2 Run mechanics, strongest form

The composition leg (A.1) explains *who* the marginal borrower is. This section explains *why*
the funding side that lends to them is privately optimal to build and structurally prone to
freezing overnight — six mechanisms, escalating from the classical bank-run analogy through the
India-specific institutional chain to the political-economy reason the structure keeps
reappearing after every crackdown.

**A.2.1 Diamond-Dybvig applied to market funding — a run without the two things that stop one.**
**Diamond, Douglas W. & Dybvig, Philip H. (1983), "Bank Runs, Deposit Insurance, and Liquidity,"**
*Journal of Political Economy* 91(3): 401–419, **[Verified]** models a bank run as a
coordination failure with two equilibria supported by the *same* fundamentals: if every
depositor believes only genuine liquidity needs will trigger withdrawal, the bank's illiquid,
long-maturity assets need never be sold at a loss and everyone is paid in full; if every
depositor believes *others* will withdraw, running first is individually rational even for a
depositor with no genuine liquidity need, because the bank's assets cannot be liquidated fast
enough at fair value to pay late claimants — first-mover advantage converts a solvent
institution into an insolvent one purely through the sequencing of claims. Diamond-Dybvig's own
resolution is that **deposit insurance removes the incentive to run** by making the payoff to
waiting weakly dominate running regardless of what others do, and a **lender of last resort
(LOLR)** achieves the same result by standing ready to fund the bank through the liquidity
event rather than force asset sales. Applied to NBFC market funding, the mechanism is identical
in structure and *strictly worse* in its two escape hatches: an NBFC's commercial paper and
NCDs carry **no deposit insurance** (A.1) and an NBFC has **no standing LOLR access** — the RBI's
overnight liquidity windows (LAF, MSF) are built for banks, and an NBFC facing a rollover
shortfall must either find a fresh buyer for its paper, draw an existing bank credit line (which
banks can and do tighten precisely when they judge the borrower's risk has risen — A.2.6), or
sell assets into an illiquid secondary market at a fire-sale discount. Every element of
Diamond-Dybvig's fragile equilibrium is present; neither of Diamond-Dybvig's own proposed fixes
is.

**A.2.2 Gorton-Metrick — securitized banking runs and the repo-haircut analogue.**
**Gorton, Gary & Metrick, Andrew (2012), "Securitized Banking and the Run on Repo,"** *Journal
of Financial Economics* 104(3): 425–451, **[Verified]** document the 2007–08 US crisis as a run
not on retail deposits but on the **repo market** — short-term, collateralized wholesale funding
for securitized assets — transmitted through a mechanism with no depositor panic at a branch
window at all: as concerns about collateral quality spread, **repo haircuts** (the discount a
lender applies to collateral value before extending cash) rose across asset classes, including
ones with no direct subprime exposure, forcing borrowers to post more collateral for the same
cash or accept less cash for the same collateral — a *quantity* contraction achieved entirely
through the *terms* of rollover, without any single lender needing to refuse to roll at all. The
India analogue is structural, not just illustrative: CP investors do not literally apply a
"haircut" the way a repo counterparty does, but the **economically equivalent** action —
demanding a materially higher yield, shortening the tenor a fund will accept, or simply
declining to roll a maturing instrument at any price for anything but the most pristine
issuers — produces the identical quantity-through-terms contraction Gorton-Metrick document,
and it is precisely why the desk's freeze-index construction (`partC-data.md` §C.1) builds a
**spread** measure, not merely an outstanding-volume measure: the run shows up in price before
(and sometimes without ever fully showing up in) an outright refusal to lend.

**A.2.3 The CP-MF chain specific to India — first-mover advantage without deposit insurance or
LOLR access, made concrete.** Sections A.2.1–A.2.2 are the general theory; this is the specific
plumbing. An NBFC issues 90-day commercial paper (typically) to fund a book of longer-tenor
loans (auto loans, LAP, developer finance, microfinance — months to years). The natural buyer of
that paper is a debt mutual fund — liquid funds, ultra-short-duration funds, credit-risk funds —
because CP yields a spread over T-bills that these funds' mandates are built to harvest. Those
funds are themselves open-ended: **retail and institutional investors can redeem units on any
business day**, receiving that day's NAV. The chain has now stacked one maturity mismatch
(NBFC: long assets, 90-day funding) on top of another (mutual fund: portfolio of 90-day-and-
longer paper, daily-redeemable liabilities), and the second mismatch reproduces Diamond-Dybvig's
run equilibrium **one more time, at the fund level**: an investor who suspects other unitholders
will redeem first has every reason to redeem first too, because a fund forced to sell CP into an
already-stressed market to meet redemptions realizes losses that fall on whoever is left holding
units, not on the investor who exited at yesterday's NAV. The result is a run with **two**
first-mover-advantage layers instead of one, and neither layer carries deposit insurance or LOLR
access: CP holders are unsecured wholesale creditors of the NBFC, and mutual-fund unitholders
have no equivalent of a bank guarantee on their units. This is the mechanism `partC-data.md`
§C.2 is built to watch (debt-AUM-by-category redemption data, scheme-level CP holdings) and the
reason the entry insists the detection variable must be the **fund flow and the spread**, not a
lagging NBFC-level solvency metric.

**A.2.4 ALM mismatch economics — why long assets, short funding is privately optimal and
socially fragile.** **Diamond, Douglas W. & Rajan, Raghuram G. (2001), "Liquidity Risk, Liquidity
Creation, and Financial Fragility: A Theory of Banking,"** *Journal of Political Economy* 109(2)
**[Verified; exact page range VERIFY]**, supply the formal answer to a question A.2.1–A.2.3
leave open: if a fragile, run-prone funding structure is this dangerous, why does any rational
institution choose it? Their answer is that the fragility is not a mistake but the **mechanism
of value creation itself**: an intermediary that can credibly commit to demandable, run-prone
liabilities is *thereby* able to lend on terms an intermediary funded entirely with long,
locked-up capital cannot — the threat of a run disciplines the intermediary's own management
(illiquid, opaque loans are hard for outsiders to monitor directly; a demandable-liability
structure lets financiers monitor *collectively*, by their willingness to keep rolling over,
rather than each having to underwrite the loan book individually) and lets the intermediary
extend financing to borrowers who could not otherwise raise it. Applied to an NBFC: financing a
five-year auto loan or a two-year developer facility with 90-day CP is not an oversight the
management failed to correct — a shorter funding tenor is *cheaper* (the term premium on 90-day
paper is lower than on five-year paper, almost always), and rolling it every quarter is exactly
the market discipline Diamond-Rajan's theory says makes the lending possible at all: an NBFC
funded entirely with five-year money at a five-year-money interest rate would price many of
these loans out of viability. The mismatch is **privately optimal** for the NBFC (cheaper
funding, market discipline, viable margins) and **socially fragile** (A.2.1–A.2.3) precisely
because the entity bearing the fragility cost in a freeze — the borrower who loses access to
credit, the fund unitholder left holding a side-pocketed unit, the next NBFC down the chain that
also funds short — is not the same entity capturing the funding-cost benefit in normal times.
This is the standard externality argument for why regulators intervene in bank liability
structure at all, extended here to an entity class regulators historically intervened in far
less (A.2.6).

**A.2.5 Rollover risk as a coordination game — kept intuitive.** **Morris, Stephen & Shin, Hyun
Song (1998), "Unique Equilibrium in a Model of Self-Fulfilling Currency Attacks,"** *American
Economic Review* 88(3): 587–597 **[Verified]**, and their survey **Morris, Stephen & Shin, Hyun
Song (2003), "Global Games: Theory and Applications,"** in *Advances in Economics and
Econometrics* (Cambridge University Press) **[Verified]**, solve a problem Diamond-Dybvig's own
model leaves genuinely indeterminate: with *common knowledge* of fundamentals, a coordination
game like a bank run or a currency attack has multiple self-fulfilling equilibria and nothing in
the model says which one occurs or when — "sunspots" (arbitrary, payoff-irrelevant signals) can
tip the outcome. Morris-Shin's global-games refinement shows that once each agent observes the
true fundamental only with a small amount of **private, idiosyncratic noise** (nobody sees
exactly the same signal, however close), the multiplicity collapses to a **unique** equilibrium
in which agents attack (or run, or refuse to roll) exactly when their own noisy signal crosses a
threshold — turning "will there be a run" from an unpredictable coordination puzzle into a
threshold condition on the underlying fundamental plus the *precision* of what each rollover
investor can observe about it. Kept intuitive for a debt mutual fund's redemption decision: a
unitholder does not need to believe the NBFC is actually insolvent to have a rational reason to
redeem — only to believe enough *other* unitholders currently rate the NBFC's paper risky enough
to redeem *first*, and the less precisely any single holder can verify the NBFC's true funding
position (opaque disclosure, no real-time solvency signal — A.2.3's information gap), the lower
the bar for that belief to tip the whole fund into forced selling. **He, Zhiguo & Xiong, Wei
(2012), "Rollover Risk and Credit Risk,"** *Journal of Finance* 67(2): 391–430 **[Verified]**,
formalize the finance-specific consequence directly: when market-wide debt-rollover conditions
deteriorate, a firm financing itself with short-tenor debt can be pushed to default at a
**higher** fundamental threshold than an otherwise-identical firm financed longer — rollover
risk is not merely a liquidity inconvenience layered on top of credit risk, it *creates*
additional credit risk, because equityholders bear the losses of a costly rollover while
maturing debtholders are paid out first, making default optimal for the firm sooner than pure
fundamentals would dictate. Applied to L10's own composition seat: an NBFC-heavy borrower
segment is not just funded by a more fragile liability structure, it is *more likely to default*
purely because of that funding structure, independent of the underlying loan book's asset
quality — a reason the freeze and the credit-quality signal, though analytically distinct, feed
each other in exactly the direction A.3 documents.

**A.2.6 Regulatory arbitrage as the SOURCE of shadow growth — why regulators "keep re-creating"
the structure.** `docs/CYCLE_ATLAS.md` row 2.2's own mechanism line calls this out directly, and
the empirical literature is now unusually clean on the causal direction. **Irani, Rustom M.;
Iyer, Rajkamal; Meisenzahl, Ralf R. & Peydró, José-Luis (2021), "The Rise of Shadow Banking:
Evidence from Capital Regulation,"** *Review of Financial Studies* 34(5): 2181–2235 **[Verified]**,
use a supervisory US syndicated-loan register and a Basel III capital-requirement shock to show
that **less-capitalized banks retain fewer loans, especially the ones carrying higher capital
charges, and nonbanks step directly into the gap** — capital regulation does not shrink risky
lending, it relocates it to entities the regulation does not reach, with the paper's own further
finding that loans funded by fragile-liability nonbanks were **less likely to be rolled over**
and suffered **greater price volatility** in the 2008 crisis — A.2.1–A.2.5's mechanism,
independently confirmed at the loan level. **Buchak, Greg; Matvos, Gregor; Piskorski, Tomasz &
Seru, Amit (2018), "Fintech, Regulatory Arbitrage, and the Rise of Shadow Banks,"** *Journal of
Financial Economics* 130(3): 453–483 **[Verified]**, document the same mechanism in US
residential mortgages: shadow-bank origination share roughly doubled 2007–2015, driven jointly
by regulatory differences and technology — regulation pushes the *volume*, technology lowers the
*cost* of the entity that absorbs it. **India's own version of this story is institutionally
explicit, not merely analogous.** NBFCs are **not required to hold CRR or SLR** with the RBI —
the two reserve/liquid-asset requirements that constrain how much of a bank's deposit base can
be lent out at all — and RBI rules additionally let banks classify their **on-lending to NBFCs**
for housing, agriculture, and micro/small-enterprise finance as **priority-sector lending**
(PSL) itself, meaning a bank can satisfy its own PSL quota by funding an NBFC that then makes
the loan the bank was never structured to originate directly. **[Verified — NBFCs' CRR/SLR
exemption and the PSL on-lending provision are standard, publicly stated RBI regulatory
features.]** The chain this produces is not a one-off: Basel-driven bank capital discipline and
the 2015–18 Asset Quality Review (`credit-deep/partA-theory-psychology.md` §A.3, the same
recognition shock) tightened what banks could originate directly and how it had to be
provisioned, exactly the Irani-Iyer-Meisenzahl-Peydró mechanism; NBFC/HFC balance sheets grew
rapidly through the 2010s absorbing that displaced origination (aggregate reported NBFC
borrowings roughly **₹3.75 lakh crore (Mar-2009) → ₹9.98 lakh crore (Mar-2014)**
**[VERIFY: RBI-sourced aggregate, secondary citation]**); the 2018 IL&FS freeze (A.3) was the
first system-scale test of the funding structure that growth had built; RBI's regulatory
response — the 2021 scale-based pyramid (A.1), the November 2023 risk-weight increase on
unsecured retail and bank-to-NBFC exposure (`credit-deep/partA-theory-psychology.md` §A.9,
already the credit monograph's own citation), the 2023 First-Loss-Default-Guarantee (FLDG /
"Default Loss Guarantee") rules capping fintech-lender risk-sharing at 5% of a loan portfolio,
and the 2020 co-lending-model framework requiring an NBFC partner to retain a minimum 20% share
of any co-originated loan — each closes one specific channel the previous round of growth had
used. **[Verified — RBI Scale Based Regulation Oct-2021; Nov-2023 risk-weight action; June-2023
Default Loss Guarantee guidelines, 5% cap; Nov-2020 co-lending-model circular, 20% NBFC
retention.]** None of this stops shadow credit from existing; each round visibly **relocates**
where the fragile node sits — from balance-sheet NBFCs toward fintech loan-service-providers
partnering with smaller, less-scrutinized NBFCs under FLDG and co-lending structures that did
not exist in 2018 — which is precisely the design-relevant consequence A.4's regulatory-cycle
watch is built to track, and precisely the trap G.5 below names for an operator who assumes the
2018 map of "where the fragility sits" still applies unchanged.

**A.2.7 Synthesis — mechanism, India observable, and what it argues for.**

| Mechanism | India observable | What it argues for |
|---|---|---|
| Diamond-Dybvig run equilibrium (A.2.1) | No DICGC cover on CP/NCD; no NBFC LOLR access | Why a solvent NBFC can still be forced into a fire sale — the fragility is structural, not a solvency signal |
| Gorton-Metrick terms-not-quantity contraction (A.2.2) | CP/CD spread over matching-tenor T-bill (`partC-data.md` §C.1) | Why the freeze index is built on **spread**, not outstanding volume — the run shows up in price first |
| The CP-MF chain (A.2.3) | Debt-fund category AUM/redemptions, scheme-level CP holdings (`partC-data.md` §C.2) | Why the true fuse is two-layered (NBFC-to-fund, fund-to-unitholder) and doubly uninsured |
| Diamond-Rajan privately-optimal fragility (A.2.4) | Term-premium differential, 90-day CP vs. multi-year asset yield | Why the mismatch is not a governance failure to be regulated away — it is the funding model's source of viability |
| Morris-Shin global games / He-Xiong rollover-credit-risk (A.2.5) | Signal precision on NBFC funding position (opaque disclosure) | Why lower observability lowers the threshold for a self-fulfilling redemption wave, and why rollover risk is also credit risk |
| Regulatory arbitrage (A.2.6) | CRR/SLR exemption, PSL on-lending provision, sequence of RBI tightening rounds (scale-based regs, Nov-2023 risk weights, FLDG, co-lending) | Why the sector keeps regenerating after every crackdown, and why the fragile node **moves** rather than disappears (G.5) |

**What no free India observable captures.** Issuer-level rollover calendars — which specific
NBFC's paper matures next week, and to whom — are the run's true fuse and are visible only in
aggregate (`partC-data.md` §C.5); the freeze index this program can build detects the fire, not
the first spark, exactly as that chapter states. This is the same category of honest gap the
credit monograph's own §A.12 documents for leverage terms and the external finance premium: the
mechanism is understood in more granular detail than any free series can currently measure, and
the design states that gap rather than assuming a proxy closes it.

---

### A.3 The propagation lesson SC1 measured

A.2 is theory; this section is the desk's own evidence, and it is honest about a result that
**failed its pre-registered bar** — informatively. `shadow-RESULTS.md` pre-registered SC1 before
looking: over the IL&FS crunch window (Sep-2018–Aug-2019, 12-month cumulative), the
mechanism-derived claim was that a shadow-credit-specific shock should show up as a **severe,
concentrated** small-cap hit while the broad market **escapes relatively unscathed** — SMB
percentile ≤10th (small stocks devastated) while the market percentile stays >10th (the index
shrugs it off), consistent with a credit-supply shock landing disproportionately on the smaller
firms that depend on NBFC/marginal-lender financing. The print: **SMB cumulative −24.8% (18th
percentile)** — genuinely severe — but **market cumulative −20.2% (16th percentile)** — also
severe, and *below* the 10th-percentile bar the claim needed the market to clear to count as
"escaped." **SC1 FAILS**, exactly as `shadow-RESULTS.md` records, and reruns at a different
horizon are explicitly refused there as iterating-until-pass — the short-horizon version of this
claim is registered instead for SC2, gated on the freeze index `partC-data.md` is built to
assemble, never on a re-cut of SC1's own 12-month equity window.

**Why the failure is the finding, not a null result.** A shock this program's own mechanism
argues should be *concentrated* in small/marginal borrowers instead shows up as **everyone's
problem within twelve months** — autos, consumption credit, and developer financing all slowed
through 2019 alongside the small-cap hit, the market-wide reading `shadow-RESULTS.md` records
directly. The theory of *why* propagation runs this fast, tying A.2's mechanism to A.1's
composition claim: **NBFCs fund the marginal borrower specifically** — developers who cannot get
bank construction finance on bank terms, loan-against-property (LAP) borrowers whose collateral
a bank underwriter would discount more heavily, microfinance clients below any bank's cost-to-
serve threshold, used-vehicle buyers a bank credit process is not built to underwrite quickly.
When NBFC funding freezes, this is not a substitutable credit line — it is the **only** channel
many of these borrowers had. **Sharpe, Steven A. (1990), "Asymmetric Information, Bank Lending,
and Implicit Contracts: A Stylized Model of Customer Relationships,"** *Journal of Finance*
45(4): 1069–1087, **[Verified]**, supplies the reason banks cannot simply absorb the displaced
lending on short notice even where they are willing in principle: a lender's willingness to
extend credit on workable terms rests on **relationship-specific information capital** —
history with a specific borrower's cash-flow behavior, collateral quality, and repayment
discipline — that a bank competing for a newly-orphaned NBFC borrower does not possess and
cannot underwrite at NBFC speed or NBFC risk tolerance; Sharpe's own point that competition for
new customers pushes initial terms toward expected losses for the *lender* extending them is the
mechanism reason banks are neither fast nor eager to step into a freeze's gap, whatever the
headline liquidity-window announcements (G.6) might suggest. Layered onto this borrower-side
channel is a second, **wholesale contagion** route A.2.3 already built: as fund NAVs mark down
CP/NCD holdings to the (now much wider) spreads a freeze produces, unitholders in funds with *no
direct IL&FS exposure at all* observe falling NAVs across the credit-risk and corporate-bond
category, and redemption pressure spreads from the specifically-exposed funds to the
category as a whole — the same GFC-era wholesale-funding contagion Gorton-Metrick (A.2.2)
document for repo, running here through mutual-fund NAV marks instead of haircuts.

**The consequence, stated as this entry's central design argument.** By the time a 12-month
equity-factor window can see the propagation SC1 was built to test, the shock is **already
everyone's problem** — which is exactly why the atlas routes the funding-freeze signature to
`L2_fast_stress` rather than treating it as an L10-adjacent monthly credit read. A signal useful
to the desk must be **faster than the test that just failed**: the native variables of the
mechanism itself — CP/CD spreads over matching-tenor T-bills, rollover ratios (fresh CP issuance
over maturing amount), and debt-fund category AUM/redemption flow — move at **daily-to-weekly**
cadence, exactly `partC-data.md`'s freeze-index construction (§C.1's `z(CP spread) +
z(−rollover ratio)`) and exactly the cadence `L2_fast_stress`'s existing role already operates
at (`config/ladder.yaml`: "reactive risk-off switch... CCIL/NSDL funding-flow stress rank; any
one arms R4 cuts, two confirm"). This is not a preference for faster data over slower data in
the abstract — SC1 is the desk's own demonstration that the **slower** instrument (a 12-month
equity factor) cannot distinguish "contained shadow-credit event" from "systemic macro event"
until both have already happened, at which point de-risking on the equity-factor read alone
would already be too late relative to a CP-spread or fund-flow read moving weeks earlier in the
same episode. SC2's acceptance bars, pre-registered in `partC-data.md` §C.6 step 51 against
`L2`'s own stress dates before any backtest look, are where this claim gets its real test; this
entry's job is to state, with SC1's own numbers as the evidence, *why* the fast-variable
approach is the theoretically and empirically motivated one rather than an arbitrary preference
for more data.

---

### A.4 What the sub-cycle adds without double-counting

The de-dup discipline stated in A.1 is not a formality — it is the entry's most important design
constraint, restated here as a rule with teeth: `L10_credit_block` already carries the
composition leg (unsecured retail + NBFC share, credit-deep §A.4/A.9); `L2_fast_stress` already
carries market-wide stress detection (realized-vol percentile, India-VIX backwardation, general
CCIL/NSDL funding-flow stress rank). **This entry adds no new ladder seat and draws no new
regime-score budget.** What it contributes is narrower and, precisely because it is narrower,
stated exactly:

**(a) The CP/funding-spread family as L2 INPUT candidates, consistent with partC's freeze
index.** A.2's mechanism and A.3's evidence jointly argue that `L2_fast_stress`'s existing
"CCIL/NSDL funding-flow stress rank" component should be built, in the data phase, from the
specific series `partC-data.md` §C.1–C.2 already specifies — the CP-spread-plus-rollover-ratio
freeze index, and debt-AUM-by-category redemption flow — rather than from a generic funding-
stress proxy that does not target this mechanism specifically. This is a **measurement
enrichment of an existing input**, the same category the atlas already uses elsewhere for
LAF net liquidity (§15) and REER stretch (§15): no new seat, a better-targeted series inside one
that already exists, gated on SC2's own acceptance test (`partC-data.md` §C.6) before it enters
`L2` at all.

**(b) An NBFC-crunch PLAYBOOK — descriptive, reduce-only, never a timing call.** What 2018–19
teaches, stated as a lesson rather than a rule: sector-level effects arrived in a **sequence**
(NBFC/HFC equity and bond stress first, developer/real-estate and consumption-finance-linked
names next as the credit channel to those borrowers tightened, broad-market drawdown last as the
slowdown became a growth story rather than a sector story — the same sequencing `fincycle-
deep`'s own A.5iii bank-sector-channel logic documents for property busts transmitting through
bank equity before a lagging NPA print). A desk holding sector-level exposure through a
confirmed funding freeze should expect this sequence to *tend to* repeat in rough shape — the
NBFC-adjacent sectors feel it first, the broad market last — without any claim that the specific
names, the specific lag length, or the specific severity will match 2018–19's realization (n=1;
G.5 below names the trap of assuming it will). This is registered as a **descriptive, reduce-
only** conditioner exactly like the atlas's other sector-rotation material (§14: "the design does
sector rotation through its states, not through a canned early/late-cycle playbook") — it
informs which sectors a fast-stress-triggered de-risk should touch hardest, never a standalone
signal to add exposure against.

**(c) The regulatory-cycle watch — scale-based regulation, FLDG, co-lending each reshape where
the fragility sits.** A.2.6's own finding — that each round of tightening visibly relocates the
fragile node rather than eliminating it — is itself a piece of context the desk should carry
forward, not trade on directly: the 2021 scale-based pyramid, the 2023 FLDG cap, and the 2020
co-lending retention rule each closed a channel 2018's crisis exposed, and each opened a
plausible next channel (smaller NBFCs partnering with lightly-scrutinized fintech
loan-service-providers under the new FLDG/co-lending structures) that carries no 2018-era track
record at all. This is **CONTEXT**, in the atlas's own vocabulary (§0) — it shapes how the desk
reads a future freeze-index reading (a spike concentrated in fintech-partnered NBFC paper reads
differently than one concentrated in the largest Upper-Layer names) but moves no allocation by
itself.

**Explicitly, once more: no new seat, no new budget.** The composition leg stays exactly where
`credit-deep`'s own dossier put it, at exactly the tier and reduce-only status the credit
monograph's synthesis table (§A.12) already assigns. The funding-freeze leg stays a **candidate**
input to `L2`, gated on SC2, never an independent regime-score contributor. Everything in (a)–(c)
above is additive detail *inside* two seats that already exist, which is the entire point of
calling this an atlas *sub-cycle* rather than a ladder entry of its own.

---

## PART G — Operator psychology

Part A documents a mechanism whose fastest, most dangerous phase — the run itself — compresses
into days, arriving after a calm period in which every available signal (a AAA rating, a strong
NBFC growth print, a functioning RBI liquidity window) argues nothing is wrong. This Part maps
the specific ways a desk mishandles that combination to the countermeasures the program already
has in place, in the same spirit as `credit-deep`'s own Part G and `fincycle-deep`'s own Part G.

### G.1 The AAA illusion — ratings as lagging confirms, never inputs

**Mechanism.** IL&FS group entities carried **AAA ratings from multiple domestic agencies** even
as a subsidiary (IL&FS Transportation Networks) was already defaulting in June 2018; the
downgrade cascade to outright default (D) grade did not complete until **mid-September 2018**,
weeks after the first defaults were already public. **[Verified — IL&FS rating trajectory,
multiple contemporaneous sources.]** This is not a story about one rating agency's specific
failure; it is the structural reason `partC-data.md` §C.3 states the design rule directly: "a
rating is never an input, only a post-mortem variable." A credit rating is built from
periodically-reviewed information and an agency's own institutional caution about downgrading a
large, systemically-connected issuer — both properties that make it a **confirming**, not a
**leading**, indicator of exactly the kind Galbraith's bezzle names (`credit-deep`'s own G.4):
the rating looks best precisely when undiscovered stress is largest, because the discovery
process itself (a rating review, an audit, a missed payment finally becoming public) is what a
rating is lagging.

**Countermeasure.** Identical in spirit to the credit monograph's GNPA rule: ratings actions
enter this program's design **only** as lagging confirmation, structurally excluded from any
leading role in the freeze index (`partC-data.md` §C.3: "Ratings actions from public rationales
... are LAGGING confirms only — the IL&FS lesson is codified"). The countermeasure is not "read
ratings skeptically" — it is a design rule that never lets a rating enter the input side of the
signal at all.

### G.2 Reaching for yield in credit-risk mutual funds

**Mechanism.** A "credit-risk fund" category exists specifically to hold lower-rated, higher-
yielding corporate paper — including CP and NCDs from precisely the NBFC/HFC issuers this entry
documents — marketed on the incremental yield over a plain liquid or short-duration fund.
Investors and distributors alike face an obvious, well-documented incentive: in a low-rate
environment, the extra 50–150bp a credit-risk-fund category offers over a liquid fund is salient
and immediate, while the tail risk it is compensating for (A.2's run mechanics) is invisible
until it crystallizes. Franklin Templeton's six wound-up debt schemes (below, G.4) were
disproportionately positioned in exactly this higher-yield, lower-liquidity segment of the
market — the reaching-for-yield trade that looked, for years, like a reliable way to clip an
extra basis-point spread over cash.

**Countermeasure.** This program's own debt sleeve is explicitly excluded from this trade by
design (`CONTRACT.md` §3: "Debt sleeve: flat 10% return assumption — no credit model, no
duration overlay") — a flat-return assumption with no credit-spread-harvesting mandate removes
the incentive this failure mode runs on at the mandate level, before any operator judgment is
required. Where the shadow-credit signal touches the book at all, it is exclusively through
`L2`'s regime-score conditioning of the **equity and leverage** sleeves (A.4a), never through a
yield-seeking allocation into the credit instruments whose fragility A.2 documents.

### G.3 "It's just one group" — the IL&FS → DHFL → Yes Bank chain

**Mechanism.** Each step in the 2018–2020 chain was, at the time, defensible as contained: IL&FS
was "an infrastructure-financing conglomerate with a complex, opaque group structure — not
representative of the sector"; DHFL's board was superseded by the RBI on **20 November 2019**
and the company entered moratorium under the Insolvency and Bankruptcy Code from **29 November
2019** — "a housing financier with its own specific governance failures, not systemic"; Yes
Bank's RBI-imposed moratorium on **5 March 2020** and the subsequent **~₹8,415 crore write-down
of its Additional Tier 1 (AT1) bonds** followed disclosed exposure to IL&FS and DHFL of **11.5%
of the bank's book as of September 2019** — a bank-specific concentration story. **[Verified —
DHFL board supersession/moratorium dates; Yes Bank moratorium date and AT1 write-down; the 11.5%
IL&FS+DHFL exposure figure.]** Each individual "it's contained to this one name/group" reading
was locally defensible, and each was followed within roughly a year by the next link in the same
chain — the narrative-capture pattern `credit-deep`'s own G.3 names generically, given concrete,
sequential form here.

**Countermeasure.** A.3's own propagation lesson is the structural answer, not an appeal to be
less credulous the next time: SC1's finding is precisely that a shadow-credit shock does **not**
stay contained to its originating name or sector within a 12-month window, so the design does
not ask an operator to judge, case by case, whether "this one is different" — the freeze-index
and fast-stress architecture (A.3's central argument) is built to fire on the funding-market
signature itself, independent of which specific name or group is the proximate trigger, exactly
so that the chain's second and third links do not require a fresh, separately-argued judgment
call each time.

### G.4 Side-pocketing and gating as run accelerants, not run stoppers

**Mechanism.** SEBI's side-pocketing mechanism — permitting a mutual fund to segregate an
illiquid or defaulted asset into a separate NAV, ring-fenced from the liquid portion of the
scheme — was proposed on **12 December 2018** and formalized by circular on **28 December 2018**,
explicitly in response to the IL&FS-triggered NAV shocks earlier that year. **[Verified — SEBI
side-pocketing circular, Dec-2018, IL&FS-motivated.]** The mechanism is a genuine improvement
over a fund having no tool at all — but it is easily misread as a **run stopper**, when its
actual function is closer to a *fairness* device (preventing investors who redeem early from
exiting at a NAV that overstates a now-impaired asset's value) that does nothing to remove the
underlying incentive to redeem *before* segregation is triggered. Franklin Templeton's wind-up
of six debt schemes on **23–24 April 2020** — assets of **₹30,854 crore at end-March 2020**
falling to **₹25,856 crore by 22 April** (a 16% fall in three weeks, after the fund house had
already borrowed to meet redemptions) — is the sharpest illustration: the schemes were not
merely gated after the fact, they were **wound up entirely**, converting every remaining
unitholder's redemption right into an illiquid claim on a multi-month-to-multi-year wind-down
process. **[Verified — Franklin Templeton wind-up dates and AUM figures.]** For an operator, the
mechanism cuts the wrong way if read as reassurance: knowing a side-pocket or gate tool *exists*
can itself accelerate the run it is meant to contain, because a sophisticated investor's rational
response to "this scheme might invoke gating" is to redeem **before** the trigger, not after —
the same first-mover logic A.2.1 and A.2.5 already establish, now applied to the accelerant
itself.

**Countermeasure.** The freeze index's own construction (`partC-data.md` §C.2) treats **NAV
discontinuities and side-pocket events as break-registry entries, never silently dropped** — the
design does not read "a gate was invoked" as a signal the stress has been contained, it reads it
as confirmation the stress was already severe enough to force the fund's hand, consistent with
treating gating/side-pocketing as a **lagging, not risk-reducing**, event exactly parallel to
G.1's treatment of ratings.

### G.5 The desk's own trap: extrapolating the 2018 playbook to the next crunch

**Mechanism.** A.2.6's own regulatory-arbitrage argument is the direct warning here: the fragile
node **moves** with each regulatory round. An operator who has internalized 2018–19's specific
map — large, balance-sheet-heavy NBFCs like IL&FS/DHFL as the epicenter, CP/NCD funding as the
specific instrument, debt mutual funds as the specific transmission channel — risks applying
that exact map to the next crunch, when the 2021 scale-based pyramid, the 2023 FLDG cap, and the
2020 co-lending retention rule (A.2.6) have already pushed a meaningful share of new origination
toward smaller NBFCs partnering with fintech loan-service-providers under structures that
**did not exist** in 2018 and therefore carry no track record through a stress episode at all.
The playbook item at A.4(b) is deliberately named descriptive and reduce-only for exactly this
reason: the *sequence* (funding stress first, sector-linked equity next, broad market last) is a
reasonable prior; the *specific names and instruments* are not.

**Countermeasure.** A.4(c)'s regulatory-cycle watch is the structural answer — logged CONTEXT
that keeps the desk's own read of "where the fragility currently sits" updated against each
regulatory round, rather than frozen at the 2018 map. Mechanically, the freeze index itself
(`partC-data.md` §C.1) is built from CP/CD spreads and fund-flow aggregates that would register
stress in whichever segment of the shadow-credit market it originates in next, rather than a
name-specific or instrument-specific trigger tied to the 2018 episode's particular
protagonists — the same discipline `credit-deep`'s own G.3 names for narrative capture, applied
here to an operator's own prior experience rather than a market narrative.

### G.6 Treating RBI liquidity windows as guarantees

**Mechanism.** The 2020 policy response to the NBFC funding crunch was real and substantial: a
₹30,000 crore Special Liquidity Scheme (an SPV purchasing short-term NBFC/HFC paper), TLTRO 2.0
(₹50,000 crore for banks to on-lend into shadow-lender paper), and a ₹45,000 crore Partial Credit
Guarantee Scheme (a 20% first-loss government guarantee on lower-rated and unrated NBFC/HFC/MFI
paper). **[Verified — SLS, TLTRO 2.0, PCGS 2.0 amounts and mechanics.]** An operator could
reasonably read this as evidence the RBI now stands behind the sector as an effective backstop.
The uncomfortable fact the same episode also demonstrates: in TLTRO 2.0's **first auction, banks
bid only ₹12,850 crore against a ₹25,000 crore offering** — meaning the central bank's own
liquidity window, designed specifically to channel funding into shadow-credit paper, was
**under-subscribed because the banks who had to make the actual lending decision remained
unwilling to take the credit risk**, even with RBI funding on offer. **[Verified — TLTRO 2.0
first-auction under-bid.]** A policy backstop that depends on a private intermediary's own risk
appetite to transmit is not a guarantee in the sense an operator might assume from the headline
announcement — it is a **conditional** channel that can fail to clear exactly when it is needed
most, for the same reason Sharpe's (A.3) relationship-lending argument says banks will not
readily absorb an NBFC's orphaned borrowers: the willingness to extend credit, even RBI-
subsidized credit, still runs through the lending bank's own underwriting judgment.

**Countermeasure.** The design never treats a liquidity-window announcement as a reason to
relax a fast-stress-triggered de-risk in progress — `L2_fast_stress`'s existing architecture
(`config/ladder.yaml`: reactive, arms on realized-vol/backwardation/funding-stress rank) responds
to the **measured** stress state, not to policy headlines about the state, and the anti-
capitulation-style discipline the credit monograph's own G.2 documents (no rule change
*initiated* mid-episode) applies with equal force here: a policy announcement is not itself a
pre-registered trigger to re-risk, and re-risking on the strength of an announced-but-unproven
backstop is exactly the "this time the fundamentals are real" override `credit-deep`'s G.1
already forbids by design, applied to a policy assurance instead of a growth narrative.

### G.7 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| The AAA illusion | IL&FS held AAA weeks before default; ratings are a confirming, institutionally-cautious lagging indicator (Galbraith's bezzle, `credit-deep` G.4) | Ratings never enter as an input — lagging confirm only (`partC-data.md` §C.3), same rule as GNPA in L10 |
| Reaching for yield in credit-risk funds | Salient incremental spread vs. invisible tail risk; Franklin Templeton's wound-up schemes were concentrated in this trade | Debt sleeve mandate excludes credit-spread harvesting entirely (`CONTRACT.md` §3); shadow-credit signal touches only equity/leverage regime via L2 |
| "It's just one group" (IL&FS→DHFL→Yes Bank) | Each link locally defensible as contained; SC1 shows propagation is the norm, not the exception | Freeze-index/fast-stress design fires on the funding-market signature itself, independent of which name is the proximate trigger |
| Side-pocketing/gating misread as a run stopper | The tool is a fairness device, not a fragility fix; knowing it exists can itself accelerate pre-trigger redemption | NAV discontinuities/side-pockets are break-registry (lagging-confirm) entries, never read as stress having been contained |
| Extrapolating the 2018 playbook to the next crunch | Regulatory arbitrage relocates the fragile node each round (scale-based regs, FLDG, co-lending); the next crunch's protagonists are not 2018's | Regulatory-cycle watch (A.4c, CONTEXT only); freeze index built from spreads/flows, not name-specific triggers |
| Treating RBI liquidity windows as guarantees | TLTRO 2.0's own first auction under-bid shows a policy backstop still depends on bank risk appetite to transmit | L2 responds to measured stress, never to policy headlines; no rule change initiated mid-episode on an announced-but-unproven backstop |

None of these six countermeasures ask the operator to read a rating, a fund gate, or a policy
announcement more skeptically in the moment. Each converts what would otherwise be a live
judgment call — is this rating still informative, is this yield worth the tail risk, is this
group's trouble contained, has this gate stopped the bleeding, does the 2018 map still apply,
does this liquidity window make the position safe to hold — into a structural non-decision, made
once, in the design, before the moment (per A.3's own timing lesson) that a shadow-credit freeze
gives the desk the least warning to make it well.

---

*Word count: 7,294.*

---

# PART B — The case record (IL&FS anatomy at double length; two mirrors)

# PART B — The shadow-credit case record: the funding-run anatomy

*Shadow-credit sub-cycle monograph (atlas 2.2, sub-component of L10, funding-freeze signature also
feeds L2) · Part B · v1.0 · 2026-09-02 · Author: Claude (research agent) for Ionic quant desk
(principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 2.2 ("NBFC/shadow-credit
sub-cycle... shadow lenders fund long assets with short CP — a run-prone structure regulators keep
re-creating... n=1 clean [episode]: 2014→2018→2020") and `config/ladder.yaml`'s treatment of the
entry as a sub-component of `L10_credit_block`'s bank+NBFC aggregate, whose funding-freeze
signature also feeds `L2_fast_stress`. The desk's own pre-registered SC1 trial
(`research/cycles/shadow-deep/shadow-RESULTS.md`) already ran and **FAILED informatively** —
12-month-window SMB and market returns around the IL&FS crunch both fell hard (SMB −24.8%, 18th
percentile; market −20.2%, 16th percentile), meaning the freeze did **not** stay contained to small
caps: by the time a 12-month equity factor window could see it, "it is everyone's problem." That
finding — cited here directly, never recomputed — is this Part's organizing discipline: a
funding-run signature useful to the desk must be faster than a 12-month equity read, which is
exactly why the atlas routes it to L2 (weekly-cadence fast stress) rather than treating it as a
slow annual state. This Part does not re-run SC1 at a different horizon or propose an equity-side
acceptance test; any such claim belongs to SC2 (the CP-spread freeze signature,
`research/cycles/shadow-deep/partC-data.md`), pre-registered there before looking.
`research/cycles/capex-deep/partB-cases.md`'s own case 3 ("India 2011–2020") already covers
IL&FS's real-side transmission — NBFC/HFC real-estate exposure (~₹1.65 trillion, 7.5% of the
sector's book, March 2018, a figure that Part borrows from
`research/cycles/fincycle-deep/partB-cases.md`'s own §B3), the developer-financing freeze, and the
knock-on into capex/property data — and `research/cycles/credit-deep/partB-cross-country.md`
already uses IL&FS as case evidence for why a bank-only credit aggregate misses a shadow-banking
shock (the pre-registered **R7** composition-signal validation target). Neither cross-referenced
Part narrates the run itself: the ratings collapse, the default sequence, the government takeover,
the mutual-fund freeze, the CP market seizure, the equity panic, and the liquidity response. That
narrower, mechanism-level job — the **funding-run anatomy** — is this Part's own contribution, and
it is not duplicated elsewhere in the atlas. Style and evidentiary discipline follow
`research/cycles/fincycle-deep/partB-cases.md` (numbers-forward, every figure sourced, `[VERIFY]`
where a search pass could not pin the primary reconciliation, interpretation written honestly after
the numbers).*

---

## B1. Framing — what a shadow-credit run actually is, and why India keeps re-creating it

The mechanism CYCLE_ATLAS.md names in one sentence deserves stating in full before the cases: an
Indian non-bank finance company (NBFC) or housing finance company (HFC) typically funds long-dated
assets — infrastructure loans, developer finance, vehicle and personal loans repaid over years —
with short-dated liabilities: commercial paper (CP, 90-day-to-1-year, unsecured, rolled over
continuously), bank lines, and, for deposit-taking NBFCs, public fixed deposits. This is a maturity
mismatch by design, not by accident — it is the entire economic function of a non-bank intermediary
that cannot take retail current/savings deposits the way a bank can. The mismatch is stable exactly
as long as the rollover market believes the borrower is solvent; the moment that belief cracks, the
lender does not experience a slow credit deterioration — it experiences a **run**, because CP
holders (overwhelmingly mutual funds acting on behalf of retail unit-holders) have no reason to
wait and see. Every case below is a variation on this same run mechanic, with the difference lying
in what sits on the other end of the rollover chain — money-market mutual funds in India 2018 and
the US 2007–08, wealth-management-product buyers in China, bank depositors in the 1990s and at Yes
Bank — and in how fast the sovereign/central-bank backstop arrives once the run is visible.

---

## B2. IL&FS, 2018 — the funding-run anatomy (centerpiece)

### B2.1 The group: what "347 entities" actually meant

Infrastructure Leasing & Financial Services Ltd. (IL&FS), incorporated in 1987 as an infrastructure
finance and development company, had by 2018 grown — through three decades of holding-company
sprawl rather than any single strategic plan — into a four-layer conglomerate that its own newly
installed board could not immediately enumerate. The group's own new management initially
identified **347–348 group entities** once the crisis forced a full count; by April 2019, after 45
had been formally closed (42 foreign, 3 domestic), the operating group stood at **302 entities**
(133 foreign, 169 domestic) `[VERIFY: reconciling the 347 vs 348 count across contemporary sources
— both figures appear in period reporting; treated here as the same order-of-magnitude fact]`.
Sectorally, transportation carried the most subsidiaries (160 — chiefly **IL&FS Transportation
Networks Ltd., ITNL**, the group's listed roads/highways arm, itself carrying dozens of individual
special-purpose road-project vehicles), followed by energy (35) and financial services (30 —
chiefly **IL&FS Financial Services Ltd., IFIN**, the group's own NBFC lending and deposit-raising
arm, and the entity whose commercial paper and inter-corporate deposits (ICDs) are this Part's
central subject). Total group debt at the point of default is most commonly cited at **₹91,091
crore (~$13bn)** — the figure the credit-cycle monograph's own case record already uses — though at
least one contemporary compilation puts total outstanding group debt at **₹99,354 crore**
`[VERIFY: the exact reconciliation between the ₹91,091cr and ₹99,354cr figures — both are period
estimates and the gap is plausibly a snapshot-date or consolidation-scope difference, not a
correction of either]`. The structural lesson worth stating up front: a holding company with 300+
subsidiaries funded substantially through group-level CP and ICDs, cross-guaranteeing and
inter-lending across layers no external analyst could map in real time, is the platonic case of
the atlas's own warning — "a run-prone structure regulators keep re-creating" — because the
complexity itself, not merely the maturity mismatch, is what let the rating agencies and lenders
each assume someone else in the chain had done the diligence.

### B2.2 The ratings cliff — AAA to default in five weeks

| Date | Event |
|---|---|
| through mid-2018 | IL&FS and IFIN's principal long-term ratings stand at AAA/AA+ (ICRA, CARE); CP rated the top short-term grade, A1+ |
| 16 Aug 2018 | CARE issues the first crack: downgrade of IFIN's ₹4,800 crore non-convertible debenture (NCD) programme |
| 27–28 Aug 2018 | First payment stress becomes public: IFIN discloses (6 Sep) that CP due 28 Aug could not be paid on schedule and was settled late, on 31 Aug; separately, IL&FS entities miss instalments on ICDs owed to SIDBI (see B2.3) |
| early Sep 2018 | ICRA reaffirms **A1+ on IL&FS's own CP even while cutting the long-term rating from AAA to AA** (positive outlook) — the single detail that mattered most for the mutual-fund holders of that paper, who could keep treating it as top-rated short-term collateral days before the group's real condition became public |
| 8 Sep 2018 | ICRA downgrades IL&FS/IFIN's long-term ratings further |
| 14 Sep 2018 | IL&FS defaults on CP and ICD obligations falling due that day — the trigger default that made the stress undeniable across the market, not merely inside the rating agencies |
| 17 Sep 2018 | ICRA and CARE cut IL&FS's and IFIN's ratings straight to **'D'** (default) — from AAA/AA to the lowest junk grade, with the outstanding rated instruments at the moment of the cut standing at **₹11,725 crore (ICRA)** and **₹20,942 crore (CARE)** |

Read end to end, IL&FS group paper went from a AAA-rated, A1+-CP-backed instrument in June 2018 to
formal default ('D') by 17 September — roughly **five weeks** from the first visible crack (16
August) to the terminal downgrade, and a single day (14 September) between the payment default and
the rating catching up to it. The lesson the desk's own data-engineering chapter (`partC-data.md`)
already codifies from this exact sequence: "a rating is never an input, only a post-mortem
variable." Every stage of the ratings cliff above lagged, rather than led, the underlying default;
ICRA's own A1+ reaffirmation on CP in early September, made even as it was simultaneously cutting
the long-term rating, is the cleanest single artifact in this entire monograph of a rating agency
holding two inconsistent views of the same borrower's solvency at once.

### B2.3 The default sequence

The proximate defaults, reconstructed from contemporary reporting, ran through late August and
September 2018 across several group entities simultaneously rather than as one clean event:

- **SIDBI inter-corporate deposits.** IL&FS entities owed the Small Industries Development Bank of
  India three ICD tranches totalling **~₹350 crore**, due on staggered dates from 27 August 2018;
  only ₹50 crore of that was paid, leaving ₹300 crore outstanding `[VERIFY: a separate
  contemporary report cites a distinct ₹1,000 crore SIDBI short-term loan default around the same
  date — the two figures are not reconciled here and may describe different SIDBI exposures to
  different group entities]`.
- **IL&FS Financial Services CP.** CP due 28 August 2018 was not paid on schedule and was settled
  three days late, on 31 August — disclosed publicly only on 6 September, the first point at which
  the market had a documented admission of distress rather than rumor.
- **IL&FS Energy Development.** Defaulted on term-credit obligations to financial institutions,
  reported around 13 September 2018.
- **The 14 September trigger.** IL&FS defaults on CP and ICD obligations due that day — this is the
  date most consistently cited as the point at which the crisis became a market-wide, rather than
  counterparty-specific, event.

Two structural features of this sequence deserve emphasis for L2's own design. First, **the true
fuse — who was scheduled to be repaid next week — was never visible from the outside**: ICD markets
are bilateral and dark, and even the SIDBI exposure above surfaced only after journalists chased
leaked details, exactly the C.5 measurement gap the data-engineering chapter already states
("issuer-level rollover calendars... are visible only in aggregate; inter-corporate deposit markets
are dark"). Second, the defaults cascaded **within** the group before cascading **outside** it — a
subsidiary (IFIN, then IL&FS Energy) defaulting before the parent's own instruments were formally
marked down — meaning a monitoring system keyed only to the flagship entity's own paper would have
missed the first three weeks of the actual run.

### B2.4 The government takeover — 1 October 2018, and the Satyam precedent

On **1 October 2018**, the Mumbai bench of the National Company Law Tribunal (NCLT) approved a
Government of India petition to supersede IL&FS's entire board, invoking **Section 241(2) of the
Companies Act, 2013** on the ground that the existing management's conduct was prejudicial to
public interest. A new six-member board was installed: **Uday Kotak** (Kotak Mahindra Bank, as
non-executive chairman), **Vineet Nayyar** (a retired IAS officer), **G.N. Bajpai** (former SEBI
chairperson), **G.C. Chaturvedi** (ICICI's non-executive chairperson), **Malini Shankar** (IAS), and
**Nand Kishore** (a senior official from the Comptroller and Auditor General's office) — a board
composed entirely of regulatory and public-sector credibility rather than any incumbent IL&FS
management, financier, or resolution specialist.

This was, on contemporary legal commentary, only the **second** instance since the Companies Act of
1913 that the Government of India had taken over a private (non-government) company using
company-law machinery — the first being **Satyam Computer Services**, where the Company Law Board
barred the existing board on **10 January 2009**, days after founder Ramalinga Raju's confession of
a ₹7,000 crore accounting fraud, and installed ten nominee directors. The two episodes are legally
distinct (Satyam ran through the old Company Law Board under the Companies Act, 1956; IL&FS ran
through the NCLT under the Companies Act, 2013's Section 241/242 machinery, and on grounds of
mismanagement and public-interest risk rather than a confessed fraud) and financially incomparable
in scale (Satyam was ultimately sold, post-takeover, for **₹2,900 crore**; IL&FS carried
**~₹91,000–99,000 crore** of debt at default — roughly thirty times larger). A further, almost
uncanny detail ties the two cases together directly rather than merely by precedent: IL&FS had
itself, years earlier, acquired two entities from the Satyam promoter family's Maytas group —
**Maytas Infrastructure** and **Maytas Properties** — meaning the group that became India's second
government-superseded company had previously absorbed assets from the first one. **L2/L10 lesson.**
The takeover mechanism itself (NCLT board supersession under public-interest grounds) is now a
demonstrated, twice-used institutional tool for a systemically important non-bank failure —
distinct from, and generally faster to deploy than, the bank-resolution machinery (moratorium plus
RBI-administrator reconstruction) used three years later for Yes Bank (B4 below).

### B2.5 The mutual-fund freeze mechanics

India's debt mutual fund industry held IL&FS group CP and NCDs across dozens of schemes, and the
17 September downgrade to 'D' converted what had been marked as investment-grade collateral into
paper worth a fraction of face value overnight — precisely the NAV-discontinuity event
`partC-data.md` flags as a hard registry break, never a silent series adjustment. SEBI's regulatory
response, formalized in **December 2018** in direct reaction to the IL&FS episode (and extended the
following year to DHFL, B3 below), was to permit **"side-pocketing"**: segregating a scheme's
distressed, illiquid holdings into a separate portfolio so that (i) existing unit-holders bear the
loss on the specific defaulted paper rather than having it diluted across the whole NAV, and (ii)
new investors are not admitted at an artificially depressed NAV that still contains the bad asset.
Side-pocketing did not exist as a formal SEBI mechanism before this crisis; IL&FS is the event that
created it. The mechanism bit hardest at schemes structured as **fixed maturity plans (FMPs)** —
closed-end debt funds with a specific maturity date and a promised redemption — because an FMP
holding IL&FS paper due to mature had no flexibility to simply wait out a recovery: unit-holders
were owed cash on a fixed date, and the fund's own illiquid IL&FS exposure could not be converted to
cash on that same schedule, forcing either an early haircut disclosure or a maturity extension,
both of which are the retail-facing symptom of a wholesale-funding freeze that started three layers
upstream in the CP market. `[VERIFY: a list of the specific fund houses and FMP schemes most
exposed to IL&FS paper specifically — as distinct from DHFL, where the exposure map (160+ schemes,
~₹5,200 crore, B3 below) is well documented — could not be independently confirmed this pass; the
side-pocketing mechanism itself and its December 2018 origin date are confirmed.]`

### B2.6 The CP market seizure — autumn 2018

Total outstanding commercial paper in the Indian market fell from a peak of **₹6.40 trillion on 31
July 2018** — the last reading before the crisis became public — to **₹4.15 trillion by 31 December
2019**, a contraction of roughly **35% over seventeen months**, with the sharpest single-month
compression concentrated in the autumn of 2018 itself: CP issuance is reported to have hit an
**eight-year low in September 2018**, the same month as the rating cliff and the trigger default
above. By one contemporary compilation, roughly **₹7 trillion of corporate paper had been
downgraded** across the market in the period following the IL&FS episode (as reported by May 2019)
`[VERIFY: exact reference period and whether this figure captures cumulative downgrades across all
corporate CP/NCD paper market-wide or a narrower NBFC-specific subset]` — directionally consistent
with a market-wide repricing of credit risk, not merely an IL&FS-specific event. The magnitude of
CP spread widening (the price, rather than the volume, of the freeze) is directionally severe in
every contemporary account but a precise, sourced basis-point figure for the autumn 2018 episode
could not be pinned to a single primary series this pass `[VERIFY: CP spread-widening magnitude,
autumn 2018 — the desk's own SC2 data-engineering plan (`partC-data.md` §C.1) treats this as the
freeze index's native variable and defers precise historical reconstruction to the data phase]`.
The volume collapse itself is the cleaner, better-sourced fact, and it is the direct real-world
instance of the mechanism L2's own `partC-data.md` construction targets: "rollover collapse shows as
outstanding falling while rates spike."

### B2.7 The panic marker — NBFC stock crashes

The clearest single equity-market artifact of the autumn 2018 panic is **DHFL's 21 September 2018**
intraday move: the stock fell **~59.7% intraday** on the BSE, hitting a 52-week low of **₹246.25**,
as contagion fear — "an IL&FS-like situation... emerging across NBFCs" in contemporary press
framing — swept the sector on no company-specific news of its own that day; DHFL's own actual
default (June 2019, B3 below) was still nine months away. The stock partially recovered once DHFL's
own management issued reassurances, but the day itself is the sector's cleanest "this could be the
next one" panic print — a pure contagion event, not a fundamentals-driven repricing, and the housing
finance sub-sector broadly sold off in sympathy the same session. `[Note: search-verified magnitude
here is ~60% intraday, not the ~42% figure sometimes cited in secondary discussion of this episode
— the ~60% BSE intraday fall to ₹246.25 is the figure this pass's search corroborated directly from
period reporting and is used here in preference to any unverified alternative.]`

### B2.8 The RBI/NHB liquidity response

The regulatory response ran in two distinct registers — one that arrived quickly and one that
initially did not.

- **What did not come quickly: a dedicated NBFC liquidity window.** In **October 2018**, the RBI
  publicly declined to create a special refinancing window for NBFCs, on the stated ground that
  only around **200 of India's then 11,000+ NBFCs were deposit-taking** and that no systemic case
  had been made — an explicit judgment, in real time, that the crisis was contained. Events over
  the following three years (DHFL, Yes Bank) argued the judgment was premature, though it is also
  true that a blanket across-the-board NBFC liquidity facility was never subsequently created in
  the form initially requested.
- **What did come: targeted, incremental liquidity.** The **National Housing Bank (NHB)**, in
  **November 2018**, requested RBI raise its own refinance limit for housing finance companies from
  ₹300 billion to ₹500 billion, and separately proposed raising the permitted refinance-to-net-owned-
  funds multiple from 10x to 12.5–13x (against HFC sector net owned funds of roughly ₹800 billion at
  the time) — a sector-specific, rather than system-wide, liquidity lifeline. The RBI itself
  conducted large **open market operations (OMOs)** through the winter of 2018–19 explicitly framed
  in press coverage as addressing the liquidity deficit "amid concerns of a liquidity crisis...
  after the default by IL&FS Group companies": December 2018 OMO purchases totalled **₹50,000
  crore** for the month, January 2019 added a further **₹50,000 crore** (five auctions of ₹10,000
  crore each), and February 2019 added **₹37,500 crore** — a cumulative injection on the order of
  **₹2.5 lakh crore for the fiscal year** by one contemporary compilation. **A full year later**, the
  government moved on the credit-risk-sharing side directly: the **Partial Credit Guarantee Scheme**,
  announced in the July 2019 Budget and formally issued **10 August 2019**, let public-sector banks
  purchase high-rated pooled assets from financially sound NBFCs/HFCs (rated BBB+ or better, and
  eligible even if the originator had slipped into the RBI's SMA-0 early-stress category any time in
  the year before 1 August 2018) with a government guarantee covering first loss up to **10% of
  fair value, or ₹10,000 crore, whichever was lower**, against a total programme size of **₹1 lakh
  crore**; the purchase window ran through **30 June 2020** or until the ₹1 lakh crore was
  exhausted, whichever came first. **L2/L10 lesson.** The sequence — an initial "no systemic
  window" judgment, followed within weeks by system-wide OMO liquidity, followed within a year by a
  credit-risk-sharing scheme targeted specifically at the NBFC funding-freeze mechanism — is itself
  a template: the fast, blunt tool (OMO liquidity) arrived in days-to-weeks; the precise, targeted
  tool (the PCG scheme, addressing the actual asset-quality uncertainty rather than just system
  liquidity) took roughly eleven months, a lag this desk should read as structural rather than
  IL&FS-specific — precise, targeted, legislated schemes cannot move at OMO speed even when the
  underlying market stress is unambiguous within days.

### B2.9 Resolution — the long tail

IL&FS resolution has run for close to eight years and remains incomplete as of this writing. As of
**March 2025**, the group had discharged **₹45,281 crore** to creditors, with resolution completed
across **197 entities**; by **September 2025**, cumulative repayment had reached **₹48,463 crore**
(~80% of the ₹61,000 crore internal resolution target); by **June 2026**, the most recent status
filed before the NCLAT, cumulative repayment stood at **₹50,387 crore — 82.6% of the ₹61,000 crore
target**. Of the total ~₹91,000 crore owed, **~88.4% (~₹57,000 crore)** of the specific debt owed to
public-sector banks and financial institutions had been serviced through a mix of asset
monetization/InvIT transfers (₹21,581 crore), auto-debits and "green entity" servicing (₹9,026
crore), and interim distributions to external creditors (₹14,674 crore). **L2/L10 lesson, closing
the anatomy.** Set against the ratings-cliff timeline in B2.2 — five weeks from first crack to
formal default — the resolution timeline is the mirror-image fact this desk should carry forward
into any funding-run design: **a shadow-credit run can destroy a AAA rating in five weeks and take
the better part of a decade to substantially resolve**, an asymmetry between the speed of the
freeze and the speed of the workout that recurs, in different degree, in every case below.

---

## B3. DHFL and the second leg, 2019–2021 — a slow-motion resolution vs. IL&FS's takeover

Dewan Housing Finance Corporation (DHFL) was the second, and in retail terms more consequential,
leg of the same shadow-credit sub-cycle — its funding stress became visible within the same autumn
2018 panic (B2.7) but its own default, freeze, and resolution ran on an entirely different
institutional track from IL&FS's.

**CP stress to default, June 2019.** In June 2019, DHFL defaulted on a **₹1,000 crore-order bond
repayment**, the first of a series of missed payments; **CARE downgraded DHFL's fixed-deposit
programme from CARE A to CARE BBB−**, a cut that under SEBI/RBI norms compelled DHFL to stop
accepting fresh deposits and to halt both premature withdrawals and renewals of existing ones —
the FD-holder-facing mechanism below.

**The FD freeze.** DHFL had raised roughly **₹800 crore in public fixed deposits** placed with the
company by close to a dozen bank-adjacent channels and directly by retail depositors; once the CARE
downgrade forced a halt to withdrawals, FD holders were effectively frozen alongside the company's
banks and larger institutional lenders inside the subsequent resolution process — a retail-investor
lock-in with no equivalent in the IL&FS case, where the comparably retail-facing damage ran through
mutual-fund NAVs (B2.5) rather than direct fixed deposits, because IL&FS/IFIN's own deposit-taking
footprint was smaller.

**The mutual-fund exposure map — better documented than IL&FS's own.** More than **160 mutual fund
schemes** carried DHFL paper, totalling roughly **₹5,200 crore** of investor money; one high-profile
episode saw DSP Mutual Fund sell part of its DHFL debt holdings into the secondary market in June
2019, an action contemporary reporting directly credited with helping trigger the sharpest leg of
the DHFL stock's own subsequent crash. SEBI's side-pocketing mechanism, created for IL&FS the
previous December, was applied again here — the second live use of a tool invented six months
earlier for exactly this recurring mechanism.

**First financial-service-provider into the IBC, November 2019.** In November 2019, the RBI —
acting under **Section 45-IE of the RBI Act** — superseded DHFL's board, appointed an administrator,
and referred the company into insolvency proceedings under the **Insolvency and Bankruptcy Code**:
the **first time** the IBC had been invoked against a financial-service provider rather than an
ordinary corporate borrower, a genuinely new use of the statutory machinery distinct from IL&FS's
own NCLT-board-supersession route (B2.4) — the two large shadow-credit failures of this single
cycle were resolved through **two different institutional mechanisms**, one company-law (IL&FS), one
insolvency-law (DHFL), a design choice this desk should read as evidence that India's own workout
toolkit for a shadow-credit failure was still being invented case by case as recently as 2018–19,
not applied from an existing playbook.

**Piramal acquisition, 2021, and the retail-bondholder haircut.** Piramal Enterprises completed the
acquisition of DHFL on **30 September 2021**, paying total consideration of **₹34,250 crore**
(₹14,700 crore upfront cash plus ₹19,550 crore of new 10-year NCDs at 6.75%/year); together with
DHFL's own cash balance (~₹3,800 crore), creditors recovered an aggregate **~₹38,000 crore** against
DHFL's total claims — a recovery of roughly **46%** across DHFL's ~70,000 creditors in aggregate,
though **retail NCD holders specifically faced haircuts in the 65–75% range** by some creditor
accounts raised during the resolution process itself (a disputed, rather than final, figure — the
aggregate 46% recovery and the retail-specific 65–75% haircut both circulated as claims during the
process and are not fully reconciled here `[VERIFY]`). **L2/L10 lesson.** DHFL is this monograph's
cleanest India instance of the **slow-motion** resolution mode: two full years from board
supersession (November 2019) to a completed change-of-control transaction (September 2021), against
IL&FS's own comparatively fast October 2018 board takeover — the difference being that DHFL's
statutory route (IBC, requiring a competitive resolution-plan process, NCLT approval, and surviving
a legal challenge from 63 moons Technologies over the process itself) is inherently slower than a
direct government board supersession, even though both mechanisms ultimately answer the same
underlying funding-run failure.

---

## B4. The chain into banks: Yes Bank, March 2020, and the AT1 write-down — the shadow cycle's third leg

Yes Bank's March 2020 collapse is not a separate story from IL&FS/DHFL — it is this same
shadow-credit cycle's third and final leg, transmitted from the non-bank sector into a scheduled
commercial bank through a specific, documented bridge: **developer and NBFC exposure**. Yes Bank had
grown an aggressive corporate book through the 2010s that included substantial lending to stressed
developers and NBFCs — DHFL among its largest such exposures — meaning DHFL's own June 2019 default
(B3) directly impaired one of Yes Bank's own largest counterparty books at the exact moment the
bank's broader asset quality was already deteriorating.

**Moratorium and reconstruction.** On **5 March 2020**, the RBI placed Yes Bank under a 30-day
moratorium, superseded the bank's board, capped depositor withdrawals at **₹50,000**, and published
a draft reconstruction scheme the following day (6 March); on **14 March**, under that scheme, the
bank took a **permanent write-down of ₹8,415 crore (~$890 million) of Additional Tier-1 (AT1)
capital** — an action that, by inverting the conventional creditor-priority order (equity holders
were not wiped out even as AT1 bondholders were), became the subject of prolonged litigation: the
Bombay High Court set aside the write-off, ruling the RBI-appointed administrator had exceeded his
powers, and the matter remained before the Supreme Court of India as of 2026 `[VERIFY: current
status of the Supreme Court proceeding — search results confirm the matter was pending as of
2026 with no final resolution located this pass]`. The State Bank of India ultimately led a capital
infusion of **₹7,250 crore** for a 45% stake in the reconstructed bank, joined by a consortium of
other private banks. Yes Bank's stock, which had traded near ₹404 at its own peak `[VERIFY: exact
peak date — accounts vary between August 2018 and August 2019]`, fell to a record low of **₹5.65 in
March 2020** — a fall exceeding **98%** from peak.

**Why this is the cycle's third leg, not a separate story.** Three features tie Yes Bank directly to
the IL&FS/DHFL chain rather than treating it as an independent bank failure: (i) the proximate
counterparty-quality trigger runs through the same developer/NBFC exposure this whole monograph
tracks, with DHFL specifically named as a major Yes Bank credit; (ii) the AT1 write-down is a direct
structural echo of IL&FS's own "who actually bears the loss, and in what order" problem — just as
IL&FS's CP holders (mutual funds, ultimately retail unit-holders) absorbed losses ahead of what a
naive priority ordering would predict, Yes Bank's AT1 holders absorbed losses ahead of equity, a
recurring pattern of loss allocation landing on instruments that looked senior-ish to their holders
until a resolution authority decided otherwise; (iii) the timing itself — Yes Bank's moratorium
landed within days of COVID-19's own market shock, meaning the shadow-credit cycle's slowest-to-
resolve leg closed just as an entirely unrelated, much faster shock began, a sequencing this desk's
own contract (§7, item 8: "fast crashes cannot be met by cycles") already treats as a distinct
regime the credit-cycle apparatus is not built to anticipate.

---

## B5. The 2013 mini-squeeze — a RATES signature, not a CREDIT signature

The 2013 "taper tantrum" episode belongs in this monograph as the clean **negative control**: it
produced real, sharp CP/CD funding stress, but through an entirely different mechanism than 2018's,
and the desk should never conflate the two signatures.

**The trigger and the tool.** Following the Fed's May 2013 taper announcement, the rupee came under
sustained depreciation pressure; the RBI's defense, rather than a credit-quality intervention, was a
**rates** operation: in **July 2013**, the RBI raised the **Marginal Standing Facility (MSF)** rate
to **300 basis points above the repo rate** (repo then at 7.25%, MSF effectively 10.25%) —
deliberately inverting the normal policy corridor so that the MSF's upper bound, not the repo rate,
became the effective marginal cost of overnight bank funds, an extraordinary, explicitly temporary
measure aimed at choking off rupee-shorting speculative liquidity. The measure was gradually
unwound over the following months as the rupee stabilized and Raghuram Rajan took over as Governor
in September 2013, restoring repo as the effective policy anchor.

**NBFCs in 2013 vs. 2018 — different signatures.** The 2013 episode raised the cost of short-term
funds system-wide — banks, NBFCs, and CP issuers all faced a genuinely higher marginal borrowing
rate, mechanically, by policy design — but it did **not** involve a credit-quality collapse, a
ratings cliff, a specific borrower default, or a government takeover: no NBFC's solvency was
publicly questioned, no CP issuer defaulted, and no mutual fund side-pocketed anything, because
none of those instruments existed as a tool yet and none of the underlying triggering events
(a specific default) had occurred. The desk's own SC1 trial (`shadow-RESULTS.md`) reports the Taper
window (2013-05 to 2014-04) as the mildest of its four comparator prints by far — SMB −1.7% (49th
percentile, essentially the median), market +7.7% (57th percentile) — a result entirely consistent
with a **rates squeeze that raised funding costs without impairing credit quality**, versus IL&FS's
own window (SMB −24.8%, 18th percentile) where a specific credit event cascaded into a broad
market decline. **L2/L10 lesson.** A funding-stress signature keyed only to CP/CD spread widening
would have fired in both 2013 and 2018, but the two episodes require entirely different regime
responses: 2013's stress resolved once the rates operation was unwound (a policy-reversible,
transient state); 2018's stress required a ratings collapse, a government takeover, and years of
resolution to clear (a credit-impairment state). This is the strongest available argument for why
`partC-data.md`'s freeze index (CP spread + rollover-ratio z-scores) must be read jointly with the
credit-side ratings/default confirms `partC-data.md` also specifies, never on the funding-spread
leg alone — a pure rates-driven CP squeeze and a credit-driven CP freeze can look similar in the
spread series and mean opposite things for what regime action should follow.

---

## B6. Pre-history: the 1990s NBFC boom-bust and the regulatory ratchet

India's own first full shadow-credit cycle predates the atlas's own dating (2014→2018→2020, n=1
"clean" episode) by two decades, and the desk should read this pre-history as evidence the "clean"
count understates true persistence of the mechanism even while it correctly flags the post-1991
liberalization-era episode as the first one the model's own data can measure.

**The boom and the CRB Capital catalyst.** Post-1991 liberalization created a large, lightly
regulated population of deposit-taking NBFCs that competed aggressively for public deposits through
the mid-1990s. **CRB Capital Markets**, a high-profile NBFC, began defaulting on payments to lenders
in **1996**; when its cheques started bouncing, depositors converged on its branches, and a
subsequent investigation revealed the company had routed public deposit money through shell
companies. Estimated stakeholder losses from the CRB episode alone ran to roughly **₹1,200 crore**.

**The purge.** CRB's collapse triggered a nationwide run on deposit-taking NBFCs broadly — depositors
who had never heard of CRB specifically nonetheless pulled money from comparable companies on the
fear that any of them could be the next one, and "hundreds of companies downed their shutters" in
the aftermath — a 1997 instance of exactly the same contagion mechanic DHFL's stock experienced on
21 September 2018 (B2.7), two decades and one entirely different funding instrument (public
deposits vs. mutual-fund-held CP) apart. A precise, sourced count of the registration collapse
(how many NBFC registrations were cancelled or lapsed specifically in the 1997–99 window) could
not be independently confirmed this pass `[VERIFY: precise NBFC registration/deposit-taking-company
count before and after the 1997 purge — search located qualitative confirmation of "hundreds of
companies" shutting down but not a single authoritative before/after registration count]`.

**The regulatory ratchet — RBI Act amendments, 1997.** The country-wide furore forced the RBI Act,
1934 to be amended in **1997**, giving the RBI comprehensive new supervisory powers over NBFCs for
the first time — mandatory registration (a **Certificate of Registration** requirement), minimum
**Net Owned Fund** thresholds, and detailed "entry point norms" governing the manner, form, and
quantum of public deposit acceptance. In **January 1998**, the RBI issued the first comprehensive
regulatory framework built on these new powers, categorizing NBFCs into (i) public-deposit-accepting
companies, (ii) non-deposit companies engaged in loan/investment/hire-purchase/leasing business, and
(iii) non-deposit core investment companies — the direct institutional ancestor of the far more
granular **scale-based regulation** framework the RBI would issue 24 years later (B9 below). **L2/L10
lesson.** The 1997 amendment is this record's cleanest demonstration of the regulatory ratchet
pattern that recurs through every case in this monograph: a shadow-credit run forces a **new layer**
of supervisory architecture that did not previously exist (registration/NOF norms in 1997; SEBI
side-pocketing in 2018; scale-based "upper layer" supervision in 2021; the Nov-2023 risk-weight
tightening and the 2023 default-loss-guarantee rules — B9), each new layer addressing the specific
failure mode the most recent crisis exposed, none of them anticipating the next one's specific
mechanism in advance.

---

## B7. Mirror: the US shadow-banking run, 2007–08 — securitization at the center, not CP-MF

The United States' 2007–08 experience is the cross-country mirror this desk should read for the
**mechanism**, not for magnitude: the funding instrument at the center was securitized asset-backed
commercial paper (ABCP) and the tri-party repo market, rather than India's own CP-held-by-mutual-
funds chain, but the run dynamic — short-term rollover funding for long-dated, hard-to-value assets,
collapsing the instant valuation confidence cracked — is the same mechanism this whole monograph
tracks, expressed through a different plumbing.

**The ABCP freeze, August 2007.** On **9 August 2007**, BNP Paribas halted withdrawals from three
funds holding US subprime-mortgage-related securities and suspended net-asset-value calculation,
citing an inability to value the underlying assets — the single most-cited "start date" of the
global financial crisis. The overnight ABCP-to-Fed-funds spread widened from roughly **10 basis
points to 150 basis points within a single day** of the announcement; total ABCP outstanding fell
**37%, from $1.18 trillion (August 2007) to $745 billion (August 2008)** — a slower-motion, but
ultimately deeper, contraction than India's own 2018 CP market (which fell ~35% over roughly the
same order of elapsed time, B2.6). The mechanism behind the freeze's persistence: because banks
held no regulatory capital against ABCP-conduit assets (the entire point of the off-balance-sheet
structure), a conduit unable to roll its ABCP had no readily available capital cushion to absorb the
gap, forcing either fire-sale asset liquidation or a sponsor-bank bailout of its own "off-balance-
sheet" vehicle — precisely the opacity mechanism regulators worldwide subsequently moved against
(Basel III's securitization capital rules; China's 2018 asset-management rules, B8 below).

**The repo haircut spiral — Gorton and Metrick's reading.** Gary Gorton and Andrew Metrick's
"Securitized Banking and the Run on Repo" (*Journal of Financial Economics*, 2012) frames the 2007–
08 panic as fundamentally a run on the **sale-and-repurchase (repo) market** — the very large,
short-term financing market underpinning securitization activity broadly — rather than (or in
addition to) a deposit run in the classical sense. As concerns about the liquidity and true value of
mortgage-backed collateral spread, lenders progressively raised **repo haircuts** (the amount of
collateral required per dollar borrowed); each increase in haircuts forced borrowers to post more
collateral or delever, which in a system already leveraged against the same collateral pool
mechanically forced further asset sales, further price declines, and further haircut increases — a
self-reinforcing spiral that, on Gorton-Metrick's own account, rendered the US banking system
"effectively insolvent for the first time since the Great Depression" purely through this collateral
mechanism, independent of any single institution's own credit losses.

**Reserve Primary breaks the buck, September 2008.** The **Reserve Primary Fund**, at the time the
world's third-largest money-market fund with $62.5 billion in assets, held a **$785 million**
position in Lehman Brothers debt when Lehman filed for bankruptcy on **15 September 2008**. On **16
September 2008**, Reserve announced the fund had "broken the buck" — its net asset value per share
fell below $0.995 — becoming only the second money-market fund in US history, and the first to
affect a broad investor base, to do so. Redemption requests exceeded **$40 billion within two days**,
reaching roughly a quarter of the fund's assets by the afternoon of the announcement and more than
half by the following day — a run that, unlike a bank run, had no deposit-insurance backstop and no
central-bank lender-of-last-resort facility specifically designed for money-market fund redemptions
at that point, forcing the US Treasury to introduce an emergency temporary guarantee programme for
money-market funds within days. **L2/L10 lesson.** The US case is this monograph's clearest
demonstration that the same funding-run mechanism can be triggered through a completely different
instrument (repo/ABCP/MMF rather than CP-held-by-debt-mutual-funds) and still produce the identical
signature: a valuation shock at one node propagating through a chain of intermediaries each holding
short-dated claims on longer-dated, suddenly-uncertain collateral, with the terminal holder (a
retail-facing fund) absorbing the visible loss last and most publicly — precisely the same structure
India's own MF-side-pocketing mechanism (B2.5) was invented to manage a decade later.

---

## B8. Mirror: China's trust/WMP cycle — the implicit-guarantee unwind

China's shadow-banking sector supplies the mirror case for a **wealth-management-product** funding
chain rather than a CP-mutual-fund one, and its central lesson — an implicit, never-formally-stated
government guarantee can suppress a run for years before an explicit regulatory unwind forces the
issue — has no clean India parallel but bears directly on how this desk should read any future
India shadow-credit episode's own "who actually absorbs the loss" question.

**Trust products and wealth-management products.** Chinese banks and trust companies sold enormous
volumes of WMPs to retail and corporate savers, offering yields above deposit-rate ceilings by
funneling the proceeds into trust loans, corporate bonds, and (increasingly through the 2010s)
property-developer financing — India's own NBFC-to-developer channel's structural cousin, but funded
through bank-distributed retail products rather than CP held by mutual funds. Crucially, WMPs were
sold and widely understood by buyers to carry an **implicit guarantee**: if the underlying assets
underperformed, the issuing bank or trust would quietly make investors whole rather than let a
retail-facing product visibly default, sustaining demand for products whose actual credit risk was
never transparently priced.

**The 2018 asset-management rules.** On **27 April 2018**, the People's Bank of China, the banking
and insurance regulator (CBIRC), the securities regulator (CSRC), and the state foreign-exchange
administration jointly issued the **Guiding Opinions on Regulating the Asset Management Business of
Financial Institutions** — explicitly **prohibiting implicit guarantees on newly issued products**
and barring financial institutions from using proprietary or other managed funds to cover a
redemption shortfall. The rules applied uniformly across the previously fragmented product universe
— bank WMPs, mutual funds, and trust plans alike — aiming to break the "implicit guarantee of
repayment that has fueled risk-taking and built a culture of complacency" among Chinese retail
savers, in the regulator's own explicit framing.

**Evergrande's commercial-paper web.** China Evergrande's own funding structure by the early 2020s
extended this same implicit-guarantee logic to its own commercial paper, trust products, and
in-house WMPs sold directly to employees, suppliers, and retail clients — more than **80,000
people** bought Evergrande-issued wealth products, drawn by yields approaching **12%/year** plus
promotional gifts, on the implicit strength of "China's top-selling developer" rather than any
transparent credit assessment. As Evergrande's own liquidity crisis deepened through 2021,
repayments to WMP holders were suspended; the company began a phased repayment plan (a first 10%
instalment paid in September 2021) before Fitch downgraded it to "restricted default" on **9
December 2021** and S&P followed with "selective default" the same month over a missed coupon —
Evergrande becoming, by year-end, the **twelfth** Chinese property developer to default on bonds in
2021 and by far the largest. (The commodity monograph's own China case already covers Evergrande's
property-sector and commodity-demand dimensions in full; this Part's own addition is narrowly the
CP/WMP funding-web mechanism, cross-referenced rather than duplicated.)

**The implicit-guarantee unwind, still running.** Unlike IL&FS's five-week ratings cliff (B2.2),
China's unwind has been a multi-year, policy-paced process precisely because the 2018 rules targeted
**newly issued** products, leaving a large stock of legacy WMPs to run off gradually rather than
forcing an immediate system-wide repricing — the same "state-directed, policy-paced repair" pattern
the capex-deep monograph's own China case (its case 6) already documents for China's real-side
capacity-cut programme, now shown to apply equally to the financing side. **L2/L10 lesson.** China
supplies the clearest available evidence that an implicit guarantee, once withdrawn by explicit
regulatory fiat rather than by a market-discovered default, produces a **slower**, not faster,
repricing than India's own market-discovered-default pattern — the opposite of what a naive
"administrative intervention should resolve things quickly" prior would predict, and a direct
structural parallel to the credit-cycle monograph's own observation (via its own China case) that a
state-directed system suppresses the market-based signals (bond spreads, equity drawdowns) this
desk otherwise relies on to date a bust in real time.

---

## B9. The current state, 2021–2026, and where the next fragile node plausibly sits

**Scale-based regulation, October 2021.** The RBI issued a comprehensive revised regulatory
framework for NBFCs on **22 October 2021**, replacing the ad hoc 1998-era categorization (B6) with a
four-tier structure — Base Layer, Middle Layer, **Upper Layer**, and Top Layer — under which NBFCs
are scored annually (70% weight on quantitative parameters, 30% on qualitative ones) and assigned to
the Upper Layer if they cross the threshold; the ten largest NBFCs by asset size are placed in the
Upper Layer **automatically**, regardless of score. Upper Layer status carries enhanced prudential
requirements for a minimum of **five years**, even if the NBFC's own metrics later fall below the
qualifying threshold — a deliberately sticky classification designed against exactly the kind of
"we didn't think this one was systemic" judgment the RBI itself voiced about NBFCs broadly in
October 2018 (B2.8). The first Upper Layer list, published in **2022**, named **15 NBFCs**.

**Co-lending growth.** The RBI's original 2020 Co-Lending Model, restricted to priority-sector
lending between banks and NBFCs, has been substantially widened: the **Co-Lending Arrangements
Directions, 2025** (effective **1 January 2026**) extend the framework to **all** regulated
entities and **all** loan segments, not merely priority-sector loans, while introducing a minimum
10% retention requirement per originating entity, a 15-calendar-day mandatory transfer window, and —
notably — an explicit **Default Loss Guarantee (DLG)** provision capped at 5%, folding the digital-
lending FLDG framework (below) directly into the co-lending structure. Market estimates already put
**75% of bank co-lending volume** in non-priority-sector loans even before the 2025 Directions
formally permitted that scope — the regulation, in other words, is catching up to a market practice
that had already outgrown its original mandate, the same lagging-regulator pattern this monograph
documents in every prior episode.

**The November 2023 risk-weight increase — the countercyclical move this time.** On **16 November
2023**, the RBI raised risk weights on unsecured consumer credit exposures of both banks and NBFCs
by **25 percentage points, to 125%** (for bank personal loans and NBFC retail loans excluding
housing, education, vehicle, and gold-backed loans), and separately raised risk weights on
bank-to-NBFC exposures by the same 25 points over and above the exposure's own external rating, and
on credit-card receivables to **150% (banks)** and **125% (NBFCs)** — implemented by **29 February
2024**. This is, structurally, the single clearest instance in this entire monograph of a
**pre-emptive, countercyclical** regulatory move: unlike the 1997 RBI Act amendment (reactive to
CRB Capital's collapse), the 2018 liquidity scramble (reactive to IL&FS), or SEBI's side-pocketing
rule (reactive to IL&FS and DHFL), the November 2023 tightening was explicitly justified by the RBI
as addressing unsecured/retail credit growth it judged to be **overheating** — the desk's own dossier
03 already flags the same episode (non-food credit growth accelerating from 16.0% in Aug-2022 to
20.2% by Mar-2024, credit-deposit ratio hitting an all-time high near 80% by Mar-2024) as the
institutional confirmation of exactly the composition-signal design that dossier argues for. Whether
the move was well-timed is now testable against subsequent events: the sector it targeted
(unsecured retail, disproportionately routed through NBFC/microfinance channels) is precisely the
one that showed acute stress through 2024–25 (below) — consistent with, though not proof of, the
tightening having correctly identified the fragile node roughly a year before the stress became
visible in asset-quality data. `[Note: RBI subsequently eased elements of this risk-weight regime in
2025 as microfinance-sector stress mounted — a partial reversal this desk should read alongside the
2023 tightening as one continuous countercyclical policy arc, not two separate events;
[VERIFY: precise date and scope of the 2025 easing].`

**Digital lending and FLDG rules.** The RBI's **September 2022** digital-lending guidelines first
required that first-loss-default-guarantee (FLDG) arrangements between regulated lenders and
lending-service-provider fintechs comply with the existing **synthetic-securitisation** prohibition
under the 2021 Securitisation of Standard Assets Directions — effectively banning FLDG as it was
then structured. The RBI reversed course with dedicated **Default Loss Guarantee (DLG) Guidelines**
issued **8 June 2023**, formally permitting DLG/FLDG arrangements between regulated entities and
between REs and LSPs, subject to a hard cap of **5% of the outstanding loan portfolio** — the same
5% figure the 2025 Co-Lending Directions above reuse, unifying the risk-sharing cap across both
frameworks. This is a direct regulatory response to a funding-structure innovation (fintech-
originated, NBFC-funded, risk-shared lending) that grew faster than the existing rulebook
anticipated — the 2023 rules are, in effect, this decade's version of the 1998 categorization
framework: codifying a structure the market had already built.

**Microfinance stress, 2024–25.** India's microfinance sector showed acute, rapid asset-quality
deterioration through FY25: gross NPAs rose to roughly **₹55,000 crore (~14.8% of gross loans)** by
March 2025, from a much lower base the year before `[VERIFY: one industry compilation cites a
distinct 16% gross-NPA figure for the same date — the two readings are not reconciled here and may
reflect different scope (MFI-only vs. broader microfinance-adjacent lending)]`; loans overdue
30+ days (portfolio-at-risk) rose from **2.1% (FY24) to 6.2% (FY25)**, and the stricter 90+-day NPA
benchmark rose from **1.6% to 4.8%** over the same year. The sector's gross loan portfolio
contracted, from **₹4.24 trillion to ₹3.75 trillion**, and disbursals fell from **₹1.50 trillion to
₹1.12 trillion** — a genuine credit contraction, not merely a slowing growth rate. Contemporary
analysis attributes the stress substantially to **borrower over-leveraging** (multiple concurrent
loans across lenders to the same low-income borrower, a structural echo of the "who actually holds
the risk" opacity this whole monograph documents) compounded by a weak FY25 growth backdrop (GDP
growth at a four-year low of 6.4%) and localized shocks (heatwaves, floods, election-period
disruption to collection cycles). The industry body MFIN introduced a tightened self-regulatory
framework effective **January 2025** in direct response.

**Where the next fragile node plausibly sits — an honest scenario listing, no dates.** Consistent
with the Contract's own instruction that forward-looking judgement belongs to Stage 2, not Stage 1,
the following is offered as narrative context (CONTEXT-tier only, no allocation authority), not a
forecast: (i) **unsecured retail and microfinance-adjacent lending**, given the 2024–25 stress
documented above and the sector's structurally thin per-borrower underwriting visibility even after
the Nov-2023 tightening; (ii) **co-lending and FLDG arrangements themselves**, precisely because the
2025 Directions' expansion into non-priority-sector, all-segment lending recreates, in a new
wrapper, the "who actually bears first loss and can regulators see it" opacity every prior episode
in this monograph eventually exposed; (iii) **Upper-Layer NBFCs' continuing wholesale/CP
dependence**, since enhanced supervision addresses solvency and governance more directly than it
addresses the underlying maturity mismatch the atlas's own mechanism statement names as structural;
(iv) **developer/HFC exposure re-emerging** if the 2021–2026 residential upcycle the property-cycle
and capex monographs both document turns, given how directly the 2018 freeze transmitted through
exactly that channel; and (v) **global-cycle-driven funding-cost spillover** — an FPI-outflow or
dollar-tightening episode (L9) raising NBFC wholesale funding costs faster than balance sheets can
adjust, a channel this desk's own global-financial-cycle seat is built to monitor but which this
monograph's own India cases have not yet produced a clean instance of. None of these carries a
probability estimate or a timing claim; they are listed because the atlas's own instruction is that
"knowing why a cycle was rejected teaches more than knowing one was accepted" — the honest
complement here is that knowing where a recurring mechanism's structural preconditions currently
sit teaches more than pretending the cycle has been fully retired by the last round of regulation.

---

## B10. Synthesis

| Episode | Fragile funding structure | Trigger | Freeze-to-macro lag | Regulatory response | What L2 would have needed to see it EARLY |
|---|---|---|---|---|---|
| **IL&FS, 2018** | 300+-entity holding group funded via group-level CP/ICDs against long-dated infra assets; AAA/A1+ ratings resting on unmapped intra-group cross-guarantees | SIDBI/CP payment misses (late Aug 2018) → 14 Sep formal default → 17 Sep rating cut to 'D' | **~12 months** to become macro (SC1's own window, 2018-09→2019-08: market return −20.2%, 16th percentile) | NCLT board supersession (1 Oct 2018); OMOs (~₹2.5 lakh cr FY19); PCG scheme (Aug 2019, ₹1 lakh cr); SEBI side-pocketing (Dec 2018) | Issuer-level ICD/CP rollover-calendar visibility (dark in real time, per `partC-data.md` C.5) and a bank+NBFC combined credit aggregate months before the Aug-2018 rating crack, not a rating itself (ratings lagged the default by weeks) |
| **DHFL, 2019–21** | Bank/NBFC lending + ~₹800cr public FDs + CP, real-estate-adjacent asset book | CARE downgrade forces FD-programme freeze (Jun 2019) | ~2 years to a completed resolution (board super­session Nov 2019 → Piramal close Sep 2021) | RBI board supersession under RBI Act §45-IE; first FSP into IBC; SEBI side-pocketing (2nd use) | Cross-holding map of IL&FS-exposed lenders/MFs to DHFL — the 21-Sep-2018 stock panic (B2.7) was itself the leading signal, nine months before DHFL's own default |
| **Yes Bank, 2020** | Corporate book concentrated in stressed developers/NBFCs (incl. DHFL) funded via ordinary deposits + AT1 capital | DHFL-linked asset-quality deterioration culminating in a Mar-2020 moratorium | Essentially immediate once the moratorium hit (bank run risk is same-day by construction) | RBI moratorium + administrator + reconstruction scheme; AT1 write-down (₹8,415cr, litigated since) | Counterparty-concentration mapping of bank exposure to the *already-known* 2018-19 stressed-NBFC list — the DHFL linkage was public well before Mar-2020 |
| **2013 mini-squeeze** | System-wide CP/CD funding, no specific credit event | Fed taper announcement → rupee defense | No macro propagation (SC1: market +7.7%, 57th pctile) | MSF spiked 300bp (Jul 2013), unwound within months | Distinguishing a **rates**-driven spread widening from a **credit**-driven one — the same spread series looks similar; only the ratings/default confirm layer tells them apart |
| **CRB Capital / 1990s purge** | Deposit-taking NBFCs, thin regulation, no NOF/registration regime | CRB's 1996 payment defaults exposed shell-company fund diversion | Nationwide depositor run within months (qualitative; no free precise series) | RBI Act amended 1997 (mandatory registration, NOF norms); Jan-1998 categorization framework | No free real-time series exists pre-1998; the design's own honest limit — this episode is a narrative prior only, never a backtestable one |
| **US 2007–08** | ABCP conduits + tri-party repo funding securitized MBS/CDOs | BNP Paribas fund freeze, 9 Aug 2007 | Contained to financial-sector stress for ~13 months before Lehman (Sep 2008) turned it systemic | Fed emergency facilities; MMF temporary guarantee (Sep 2008); later Basel III securitization capital rules | Repo-haircut trend + ABCP-outstanding trend (both eventually became the standard 2007-08 US early-warning series) — mirrors India's own freeze-index construction (CP outstanding + spread) |
| **China trust/WMP** | Bank/trust-distributed WMPs funding developer + LGFV lending under an implicit repayment guarantee | 2018 asset-management rules ban new implicit guarantees; Evergrande's own WMP web unravels 2021 | Multi-year, policy-paced — still unresolved as of 2026 | State-directed rules (Apr 2018); developer defaults managed via court liquidation (Evergrande, Jan 2024) rather than a single crisis date | Not transferable to India — administrative suppression of market signals means no free market-based India-style CP/MF proxy exists for this mechanism |

**The one-line synthesis.** Every episode in this record is the same funding-run mechanism —
short-dated rollover finance against long-dated, hard-to-value assets — wearing a different
instrument (CP-and-mutual-funds in India 2018, public deposits in India 1997, ABCP-and-repo in the
US 2007–08, WMPs-and-trusts in China) and a different institutional resolution channel (NCLT board
supersession, IBC referral, RBI moratorium, a regulatory amendment, a court-ordered liquidation).
The design lesson this Part hands back to L2 and L10 is the one SC1 already forced into the open:
the run itself moves in **weeks** (IL&FS's own ratings cliff, B2.2); the equity market only fully
prices the consequence in **roughly a year** (SC1's own 12-month window); and full resolution takes
**years to a decade** (IL&FS's own 2018→2026 resolution tail, still at 82.6%). A regime system that
can only see the middle of that three-speed structure — an annual-cadence equity read — will always
be too slow to matter and too fast to have resolved; the freeze-index construction `partC-data.md`
already specifies (CP spread + rollover ratio, daily-to-weekly cadence) is aimed squarely at the
first, fastest layer, precisely because that is the only layer at which this mechanism is still
actionable rather than merely diagnostic after the fact.

---

## References

Wikipedia, *Infrastructure Leasing & Financial Services*; Moneylife, various 2018–19 reporting on
IL&FS group debt and subsidiary structure; Business Standard, contemporaneous 2018 reporting on
IL&FS rating downgrades (CARE 16 Aug 2018; ICRA 8 Sep 2018; ICRA/CARE 'D' cut 17 Sep 2018), SIDBI
ICD defaults, IL&FS Energy Development default, and the 1 Oct 2018 NCLT board supersession. ·
BusinessToday, coverage of the government's NCLT petition and the six-member Kotak-led board. ·
Mondaq / Wikipedia, *Satyam scandal* and its Company Law Board precedent. · Business Standard,
"NBFCs crash: Here's why DHFL tanked over 60% in trade today" (21 Sep 2018). · Business Standard/
PTI, coverage of RBI's Oct 2018 refusal of a special NBFC liquidity window; NHB's Nov 2018 refinance
request; RBI OMO purchase schedules, Dec 2018–Feb 2019. · PIB / PMO India / Business Standard,
Cabinet approval of the Partial Credit Guarantee Scheme (10 Aug 2019). · IBC Laws / BusinessToday,
DHFL's Jun 2019 default, FD freeze, and Nov 2019 RBI Act §45-IE board supersession into IBC. ·
Business Standard / Piramal Enterprises investor presentation, DHFL acquisition completion (30 Sep
2021) and creditor recovery figures. · EliScholar (Yale Journal of Financial Crises), *India: Yes
Bank Moratorium, 2020* and *Yes Bank Restructuring, 2020*; Wikipedia, *Yes Bank AT1 bond
controversy*; Business Standard, Yes Bank AT1 Supreme Court litigation status. · IIBF Vision
(October 2013), RBI Mid-Quarter Monetary Policy Review; contemporary reporting on the Jul 2013 MSF
rate hike to 300bp over repo. · Vinod Kothari Consultants, *NBFC Regulation turned sixty*; Shardul
Amarchand Mangaldas, *Amendments to RBI Act 1934 to give greater control over NBFCs*; BusinessToday,
*The Shadow Banking Crisis* (CRB Capital Markets, 1997 RBI Act amendment). · Wikipedia, *Asset-backed
commercial paper*; Berkeley Law, *Commercial Paper During the Financial Crisis of 2007-2009*
(BNP Paribas, 9 Aug 2007, ABCP spread/outstanding data). · Gorton, G. & Metrick, A. (2012),
"Securitized Banking and the Run on Repo," *Journal of Financial Economics* 104(3): 425–451. ·
Wikipedia, *Reserve Primary Fund*; EliScholar, *United States: Reserve Primary Fund Suspension,
2008*. · Norton Rose Fulbright / Conventus Law, China's Apr 2018 *Guiding Opinions on Regulating the
Asset Management Business of Financial Institutions*; Al Jazeera / Business Standard, Evergrande
wealth-management-product default coverage, 2021. · RBI, *Scale-Based Regulation of NBFCs* Master
Direction (22 Oct 2021) and Upper Layer NBFC list (2022). · RBI, Co-Lending Arrangements Directions,
2025 (effective 1 Jan 2026); RBI 2020 Co-Lending Model circular. · RBI press release, risk-weight
increase on unsecured consumer credit and bank-NBFC exposure (16 Nov 2023, effective 29 Feb 2024). ·
RBI, Digital Lending Guidelines (2 Sep 2022) and Guidelines on Default Loss Guarantee in Digital
Lending (8 Jun 2023). · CareEdge / MFIN, *Bharat Microfinance Report 2025*; Business Standard,
microfinance NPA and portfolio-at-risk data, FY25. · `research/CONTRACT.md`; `docs/CYCLE_ATLAS.md`
row 2.2; `config/ladder.yaml` (`L2_fast_stress`, `L10_credit_block` entries);
`research/cycles/shadow-deep/shadow-RESULTS.md` (SC1 pre-registered trial, cited directly
throughout, never recomputed); `research/cycles/shadow-deep/partC-data.md` (funding-freeze data
engineering, cross-referenced throughout); `research/cycles/capex-deep/partB-cases.md` (case 3,
IL&FS's real-side/capex transmission, cross-referenced not duplicated); `research/cycles/
credit-deep/partB-cross-country.md` (IL&FS as the R7 composition-signal validation target,
cross-referenced not duplicated); `research/cycles/fincycle-deep/partB-cases.md` (§B3, NBFC
real-estate exposure figures and house style for this series); `research/dossiers/
03-credit-financial-cycle.md` (bank+NBFC aggregation rule, I11, and the Nov-2023 tightening as
institutional confirmation).

---

# PART B-RESULTS — Real data: the funding-run factor signature (SC1)

# Atlas 2.2 — shadow credit: the funding-run factor signature (SC1, pre-registered)

Data: vaulted IIMA monthly factors (log-cum 12m windows, 1994+). Bars fixed before
looking; comparator rows are context, no bars. Interpretation AFTER the print.

| Window | SMB 12m cum | SMB percentile | Market 12m cum | Market percentile |
|---|---|---|---|---|
| IL&FS crunch (2018-09..2019-08) | -24.8% | 18th | -20.2% | 16th |
| GFC (2008-09..2009-08) | -10.8% | 33th | +3.9% | 49th |
| Taper (2013-05..2014-04) | -1.7% | 49th | +7.7% | 57th |
| COVID (2020-02..2021-01) | -4.7% | 42th | +19.9% | 70th |

- Pre-registered bars (IL&FS window): SMB percentile ≤ 10th -> False; market
  percentile > 10th -> True. **SC1 FAIL**.

## Honest read (written AFTER the print)

- **SC1 FAILS, and the failure is a finding about propagation.** The mechanism-derived claim
  ("credit-supply event concentrated in small firms; market escapes") is half-right: SMB's
  −24.8% is severe (18th percentile) — but the market's −20.2% (16th) shows the freeze did
  NOT stay contained. Twelve months after IL&FS, the funding shock had propagated into a
  broad growth slowdown (autos, consumption credit) — which is precisely WHY the atlas routes
  the funding-freeze signature to L2 (fast stress): by the time a 12m equity window can see
  it, it is everyone's problem. A signature useful to the desk must be FASTER than this test.
- Comparator prints (context, no bars): the GFC and COVID 12m windows END after their
  rebounds began (+3.9%, +19.9% market) — window-end alignment matters and is stated, not
  hidden. Taper barely registers in factors at 12m.
- **No re-run at a different horizon** — that would be iterating until pass. The short-horizon
  version of this claim lives where the mechanism's native variables live: SC2's CP-spread
  freeze signature (runsheet-gated), with any equity-side acceptance registered THERE before
  running. Equity-factor claims from this entry stay dead.

---

# PART C — Data engineering: the funding-freeze variables, free

# Part C — Data engineering: the funding-freeze variables, free (atlas 2.2)

*v1.0 · 2026-09-01 · desk principal's compact chapter (the entry's data surface is narrow —
funding variables — so this Part is written in-house; the per-source discipline follows the
house style of the sibling Part C chapters).*

The entry owns ONE new measurement job: the funding-freeze signature that feeds L2. The
composition side (NBFC share of credit) is already engineered in credit-deep partC (bank+NBFC
netting rule) — cross-referenced, not rebuilt. Everything below is a candidate INPUT to L2's
stress family, daily/weekly cadence, reduce-only consequences.

## C.1 CP market — the run's native variable

| Item | Source | Cadence / lag | Notes |
|---|---|---|---|
| CP outstanding, fortnightly issuance | RBI Weekly Statistical Supplement (WSS) + RBI Bulletin "Money Market" tables | weekly / ~1w | THE freeze variable: rollover collapse shows as outstanding falling while rates spike |
| CP/CD primary rates by rating/tenor | RBI Bulletin; FBIL money-market benchmarks | monthly (bulletin) / daily (FBIL) | spread over T-bill of matching tenor = the price of rollover risk [VERIFY FBIL CP curve free-access history depth] |
| CP/CD secondary trades | CCIL F-TRAC public dissemination | daily / T+0 | volume evaporation is itself the signal; portal likely proxy-blocked here — runsheet item |
| 91d T-bill (the spread's base leg) | RBI WSS / auction results | weekly | already in the debt-deep pull list — no duplication |

Construction: **freeze index = z(CP spread, 3m tenor, top-rated) + z(−rollover ratio)** where
rollover ratio = fresh issuance / maturing amount (both from WSS fortnightly tables). The two
z's on expanding windows (shared grids); daily FBIL leg when available, weekly WSS leg always.
Warm-up: WSS CP tables are continuous from the 2000s — ranks mature quickly at weekly cadence.

## C.2 Debt-MF chain — the holder's side

| Item | Source | Cadence / lag | Notes |
|---|---|---|---|
| Debt AUM by category (liquid, credit-risk, corporate bond) | AMFI monthly AUM releases | monthly / ~1w | category redemptions = the run, one step removed; liquid-fund AUM drops led both 2013 and 2018 stress [VERIFY lead precisely on pull] |
| Scheme portfolio disclosures (issuer-level CP holdings) | AMFI/fund-house monthly portfolios | monthly / ~10d | the EXPOSURE map: which funds hold whose paper; heavy engineering, Phase-2 of the runsheet |
| NAV history | portal.amfiindia.com NAVAll (ingest/pull_amfi.py, UNTESTED LIVE) | daily | side-pocket events appear as NAV discontinuities — breaks registry entries, never silent |

## C.3 The lender itself — NBFC returns and supervisory data

RBI FSR (half-yearly) NBFC chapter: sector CRAR, GNPA, funding-mix shares (CP dependence %),
ALM buckets — the SLOW confirmation layer (lag ~6m; regime documentation, never L2 input).
RBI's scale-based "upper layer" list (annual) = the watch list of systemic names. Ratings
actions from public rationales (Crisil/ICRA/CARE sites) are LAGGING confirms only — the
IL&FS lesson is codified: a rating is never an input, only a post-mortem variable.

## C.4 PIT/vintage hazards

| Hazard | Reality | Rule |
|---|---|---|
| WSS table reformatting | RBI reorganizes WSS periodically | breaks registry entry per reformat; puller pins table names per vintage |
| AMFI category redefinition | SEBI's 2017-18 scheme categorization re-drew every category series | pre/post-2018 category series never spliced silently |
| FBIL benchmark methodology | revisions documented by FBIL | registry entries; spread construction pinned to methodology vintage |
| Side-pockets/gates | NAV series survivorship | side-pocketed units tracked as separate series, never dropped |

## C.5 What cannot be measured free
Issuer-level rollover calendars (who matures next week) — the run's true fuse — are visible
only in aggregate; inter-corporate deposit markets are dark; bank lines' undrawn status is
quarterly at best. Stated once: the freeze index detects the fire, not the first spark.

## C.6 Runsheet addendum 8 (continuing from addendum 7's step 45 [VERIFY last number])
46. WSS money-market tables backfill (CP outstanding/issuance/rates, weekly, 2000s→) ~4-6h
47. FBIL money-market benchmarks daily pull + methodology-vintage registry ~3-4h
48. AMFI monthly AUM-by-category backfill (post-2018 categories; pre-2018 kept separate) ~3-4h
49. pull_amfi.py first live test + NAVAll daily cron + side-pocket break rules ~2-3h
50. CCIL F-TRAC access test from the principal's machine; daily CP/CD trade pull if open ~3-4h
51. Freeze-index assembly + SC2 acceptance registration (BEFORE any backtest look) ~4-6h
Total ~19-27h. SC2's acceptance bars are registered at step 51 against L2's stress dates,
per the two-pass rule — the design is in the ledger, the bars wait for the data.

---

# Parts D–H — freeze-index math, routing, harvest, ledger (atlas 2.2; sub-component entry)

## Part D — The mathematics

**D1. The freeze index.** freeze_t = z_t(CP spread, 3m top-rated over matched T-bill) +
z_t(−rollover ratio), both z's expanding-window (shared grids; weekly cadence from WSS, daily
FBIL leg when it exists). Two legs because a run has two faces: PRICE (the spread the marginal
issuer pays) and QUANTITY (paper that simply does not roll). 2018's lesson is that quantity can
lead price — issuance died before spreads fully repriced — so neither leg alone suffices, and
the index is a MAX-style alarm at consumption (L2 treats either leg's extreme as actionable),
not an average that lets one calm leg mute a screaming one. [Constructed at step 51 of the
runsheet; SC2's acceptance bars are registered THERE, before any backtest look.]

**D2. The horizon algebra SC1 fixed.** SC1 measured propagation: within 12 months of the
IL&FS default, SMB sat at its 18th percentile and the MARKET at its 16th — the freeze became a
macro event faster than a monthly/12m equity window can isolate it. Formally: if the freeze
hits fundamentals with lag ℓ_f (months) and funding variables with lag ℓ_v (days-weeks), the
detection edge is the gap ℓ_f − ℓ_v — and SC1 says ℓ_f ≤ 12m, so all the harvestable edge
lives in ℓ_v. That is a measured argument, not a preference: the sub-cycle's signature
belongs to L2's daily/weekly family. Monthly equity factors are POST-MORTEM variables here.

**D3. De-dup algebra.** The entry's information set splits three ways with ZERO new budget:
composition (NBFC/unsecured share) — ALREADY a leg inside L10's single seat; market stress —
ALREADY L2's seat; funding-freeze variables — NEW INPUTS offered to L2's existing family
under L2's existing budget. A "shadow-credit seat" would be L10's composition leg plus L2's
stress seat wearing a third name; the atlas's "sub-component" language is enforced literally.

## Part E — The algorithm (routing, weekly)

```
STEP 1  weekly: WSS CP outstanding/issuance -> rollover ratio; FBIL/bulletin spread leg
STEP 2  freeze legs -> expanding z's (shared grids); publish {spread_z, rollover_z, n_legs}
STEP 3  routing: EITHER leg beyond its registered extreme -> L2 stress-family input (fast,
        reduce-only consequences per L2's own rules); NEVER a standalone portfolio action
STEP 4  composition consumption unchanged in L10 (cross-ref credit-deep; no action here)
STEP 5  playbook layer (descriptive, Stage-2): the 2018-19 sector-rotation record as a
        briefing document when the index arms — reduce-only framing, no automatic trades
MONITOR AMFI category flows monthly (holder-side confirm); FSR NBFC chapter half-yearly
        (slow structure); regulatory-cycle watch (scale-based list, FLDG, co-lending,
        risk-weight moves) as breaks-registry entries — each move RELOCATES the fragile node
FAILURE MODES: WSS reformats (registry); FBIL access; the next crunch's node NOT being
        CP-funded NBFCs at all (the arbitrage lesson) -> the regulatory watch exists so the
        index's coverage question is re-asked annually, in writing
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| L2 fast stress | the freeze index (spread_z, rollover_z) as input candidates under L2's budget |
| L10 credit block | nothing new (composition already seated — the de-dup is the deliverable) |
| Stage-2 briefings | the crunch playbook (2018-19 rotation record, descriptive) |
| Sentinel | regulatory-cycle watch entries; AMFI flow confirms |
| Cycle School | Lesson 17: a run without deposits; why detection horizon is everything |

Designs: **SC2** (registered in the ledger, bars deferred to the data per the two-pass rule):
freeze index vs L2's stress dates — acceptance registered at runsheet step 51 BEFORE any
backtest look. **SC3** (holder-side): AMFI liquid/credit-risk category flow z's as a freeze
CONFIRM (design only; acceptance registered with SC2). No equity-factor design exists — SC1
killed that family and it stays dead.

## Part H — Knowledge ledger (atlas 2.2)

**Established (our run):** the 2018 freeze reached BROAD equities within 12m (SC1's honest
fail — SMB 18th pct, market 16th) — the measured case for funding-variable detection.
**Established (record):** India has run the full shadow cycle at least twice (1990s deposit
NBFCs; 2018-20 CP-funded NBFC/HFCs) with the fragile node MOVING between runs — the
regulatory-arbitrage mechanism in the wild. **India [n=1 clean modern cycle]:** 2014→2018→2020
is one observed boom-freeze-resolution arc; every quantitative claim inherits that n.
**Unknowable:** the next fragile node's address (co-lending? FLDG-backed digital books? MFI?)
— the watch list is a question re-asked annually, never an answer assumed. **Process:** the
entry ships with ZERO new seats and ZERO new budget — its deliverable is inputs, routing, and
the de-dup proof; the ledger records one dead family (equity-factor detection) with its
failing print attached.
