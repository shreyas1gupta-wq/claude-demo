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
