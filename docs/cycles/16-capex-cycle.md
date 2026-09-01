# The Capex Cycle — Full Monograph (Atlas 1.6, seat L11; Band 1 closes)

**Version 1.0 · 2026-09-01 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front (L11, Tier C, clamped):** the seat is CONFIRMED at its designed station and
GRADUATED nowhere. The analogue evidence is the weakest of any seated entry — measured, stated,
and engineered into the algebra: the macro block consumes min(0, state), so a hot capex print
can never ADD regime score (consistency-audit finding C2, now with the analogue panel's numbers
behind it). The raw state flows unclamped to one consumer only: capital-goods/infra sector-tilt
confirmation under the Tier-C cap.

**Headline results (trials IN1–IN3 on JST analogues, pre-registered; bars unmoved):**
- **IN1 FAIL:** capex state vs forward 5y real equity: 9/15 countries negative (60% vs 70% bar)
  — between demographics (4/16, rejected) and the financial cycle (17/17, Tier B) on the
  project's calibration scale. The "C→B via analogues" clause is NOT triggered.
- **IN2 PASS at the bar:** post-peak investment/GDP repair, 195 spells: median 4y (IQR 1–12y,
  censoring counted AGAINST the claim) — "balance-sheet repair takes years" measured. India's
  own 2011–2020 instance ran nine years (Part B).
- **IN3 (measurement):** forward-return quintiles NON-monotone (top +0.242 < bottom +0.287,
  middle +0.202 lowest) — the state does not order returns; subtract-only at the hot extreme
  is what the data permits.

**Operational alert from Part C:** the 2022-23 base revisions are LIVE — GFCF new base effective
2026-02-27, IIP effective 2026-06-01. The atlas's "post-2026 rebase splice!" warning is a
present-tense engineering task (splice rules + registry entries in C.2/C.3), not a future one.

**Module:** quant/ladder/capex_cycle.py (three-leg availability-weighted state, n_legs
degradation for India's staggered starts — GFCF 1950s / IIP-capgoods 1994 / OBICUS 2008 —
clamp as a consumption-side operation) + capex_economy fixture + 4 tests; suite at 64. The
docstring states the evidence tier: machinery is not evidence.

**Assembled from:** partA-theory-psychology.md · partB-cases.md · capex-RESULTS.md ·
partC-data.md · partDEFH-math-algo-harvest-ledger.md.

---

# PART A + G — Theory (accelerator, time-to-build, twin balance sheet, the clamp's origin) and operator psychology

# Investment/Capex Cycle Deep Dive — Part A & Part G

Part A: Theory — the investment/capex cycle as accelerator, gestation lag, and twin-balance-sheet
repair · Part G: Operator psychology · v1.0 · 2026-09-01 · Atlas entry 1.6 (`docs/CYCLE_ATLAS.md`
row 67; ladder seat `L11_capex_cycle`, `config/ladder.yaml` lines ~139–149). SEATED inside the
`macro_credit_block` alongside `L6_monetary_stance`, `L10_credit_block`, `L12_realestate_medium_
cycle` (`docs/DESIGN.md` §4.1–4.2). Complements, never duplicates, `docs/cycles/01-credit-cycle.md`
(the assembled L10 credit-cycle monograph) and its own sibling `research/cycles/fincycle-deep/
partA-theory-psychology.md` (L12; style bar for this file). Evidence base: this file +
`research/dossiers/08-india-mid-cycles.md` (D08, esp. I3/I4/Edge B), `research/dossiers/
03-credit-financial-cycle.md` (D03, esp. the TBS/AQR chronology), `research/register/
consistency-audit.md` (finding C2 — the clamp's own origin story), and this program's own
pre-registered analogue trial `research/cycles/capex-deep/capex-RESULTS.md` (IN1–IN3, JST
Macrohistory Database R6, cited below with real numbers — the file exists and its results are in).
Status: theory/citations verified here; India-specific coefficients (OBICUS, IIP capital goods,
GFCF/GDP) await the data phase.

This file assumes the ladder's frozen construct as given: L11 is a **clamped, reduce-only Tier-C**
seat (`contribution_clamp: non_positive`, `reduce_only: true`) that reads OBICUS/IIP-capital-goods/
GFCF percentile ranks against `L10_credit_block`'s output (`inputs: [L10_credit_block]`), τ½
36–60 months, sharing the 20%-of-regime-score `macro_credit_block` budget with L6, L10 and L12
under the de-duplication rule (`docs/DESIGN.md` §4.2) — and, uniquely among that block's four
members, **incapable of adding to the shared score under any reading**. Part A supplies the
theoretical machine that construct compresses, and is honest about what the compression discards
and why the discarding is deliberate. Part G turns to the desk operating a seat built to watch a
narrative — "India's capex supercycle" — the desk itself has every incentive to want to be true.

---

## PART A — Theory: the investment cycle as accelerator, gestation lag, and balance-sheet weather

### A.1 The object

**(i) What L11 is.** `ladder.yaml`'s own `role` field is the precise definition: "OBICUS/
IIP-capgoods/GFCF percentile ranks; sector-level tilt confirmation only." Three free, India-native
series stand in for a "capex cycle" no single official India series measures directly. **RBI's
OBICUS** (Order Books, Inventory and Capacity Utilisation Survey), published quarterly since
roughly 2008, gives manufacturing capacity-utilization readings that have run from the mid-60s
(percent) in slack years — notably 2013–2020 — to the mid-to-high 70s in boom years (D08 I3).
**MOSPI's IIP capital-goods sub-index** (monthly, use-based classification) is the closest free
proxy to a real-time capital-goods production read. **Quarterly Gross Fixed Capital Formation as
a share of GDP** (MOSPI National Accounts) is the slowest, broadest of the three — it peaked near
34–35% around the 2007–08 boom, fell to roughly 28–29% through the 2011–2020 "capex winter," and
has been recovering toward the low 30s since 2022–23 `[VERIFY: exact GFCF/GDP levels — D08's own
figures, recalled directionally with moderate confidence, not independently re-pulled this
session]`. None of the three is used as a level or a fixed threshold — Contract §6's "no magic
numbers" rule applies here exactly as D08 states it: the construction is the **percentile rank of
trailing OBICUS utilization**, never a fixed "~75% switches capex on" heuristic, however popular
that heuristic is among practitioners (D08 I3 flags this by name as the CONTRACT §6 trap).

**(ii) What L11 is NOT.** Two adjacent seats sit one row above and one row below L11 in the ladder,
and the atlas is explicit that all three, plus L6, are "views of the same corporate/household-
leverage phenomenon from the policy, credit, investment and property sides" (`DESIGN.md` §4.2,
citing D03 §7 and D08 §2). L11 is **not the credit cycle** (`L10_credit_block`): L10 reads bank and
NBFC balance sheets directly — credit/GDP gap, credit-deposit ratio, issuance quality, GNPA as a
lagging confirm — the *financing* side of the same boom. L11 is **not the property cycle**
(`L12_realestate_medium_cycle`): L12 reads RBI HPI/RESIDEX and housing-credit deployment — the
*collateral* side. L11 reads the *real* side — what actually got built, and at what utilization it
now sits — which is why its own dossier issues an explicit **double-counting warning**: "this
dossier's capex-cycle state variable and Workstream 03's credit-cycle/GNPA state variable are
likely highly correlated, not independent, and must not both be weighted at full strength in the
composite regime score" (D08 I4). The de-duplication rule this program actually enforces (§4.2
above, mechanics in A.4 below) is the direct institutional answer to that warning — one shared
20%-of-regime-score budget across all four views, a composite (first principal component or simple
average), never four full, independently-sized weights stacked on top of one underlying boom.

**(iii) Why L11's DAG input is L10's block, and not the reverse.** `ladder.yaml` declares
`inputs: [L10_credit_block]` for L11 — capex reads credit, not vice versa, in this construction's
dependency graph. This is not an assertion about which *economically* causes which — India's own
literature is explicitly agnostic and even runs the textbook direction backward at times (Atlas
row 2.3: in India "the credit cycle leads [the business cycle] less than textbooks claim," citing
Saini et al.'s finding that business leads credit domestically — the reverse of the usual
assumption). The DAG edge instead encodes a **computational and evidentiary** fact: L11's
own contribution to the shared composite must be assessable *against* L10's state before it can be
allowed to matter at all (A.4 makes this precise), which requires L10's block to exist first in the
computation order — the acyclicity the registry validator checks (Contract §10) is a build
requirement, not an economic claim. The genuine economic coupling this ordering leans on — that
capex and credit amplify each other through firms' financing constraints — is A.2.4's Bernanke-
Gertler mechanism below, stated as theory rather than smuggled into the DAG as an unstated one.

**(iv) Why 10–15 years with n≈2–3, and why "supercycle" means something narrower than it sounds.**
The atlas dates India's investment cycle at three episodes: a 2003–08 boom, a 2011–2020 "capex
winter" coinciding with the Twin Balance Sheet (TBS) drought (A.3 below), and a 2021+ revival
(PLI-scheme-linked manufacturing investment, private capex broadening from 2023–24; D08 I4). Three
episodes, at most two completed full legs — this fails the Contract §4 clock test (≥4 observed
complete periods) by a wide margin, exactly as it fails for the sibling L12 seat (n≈1) and for the
same reason: India's post-liberalization sample is simply too short to have lived through enough
complete arcs of a phenomenon whose own cross-country length runs a decade or more. The word
"supercycle" in the atlas's own row title is doing precise, narrow work here, and the distinction
matters for how the operator should read it. It does **not** mean a dateable clock — Atlas §0's own
epistemics course (Slutzky 1937, Granger 1966) is exactly the warning against reading any smoothed
macro series as a clock with a period. It means the **slow-moving component of the investment
share itself** — GFCF/GDP's own multi-year trend, distinct from and much slower than the
business-cycle-frequency wiggle in quarterly investment growth that the ordinary business cycle
(Atlas row 2.3) already captures. τ½ 36–60 months (`ladder.yaml`) is the honest operational object:
not the 10–15-year span of a full boom-bust arc (which is a claim about the *period*, unobservable
with n<4), but the **mean-reversion half-life of the state variable that tracks position within
that arc** — a quantity the Contract's own ordering principle says is estimable "from overlapping
windows with zero complete cycles" (Contract §4) precisely because half-life and period are
different statistical objects. This is the same distinction the credit-cycle monograph draws for
L10 and the financial-cycle monograph draws for L12; L11 inherits it rather than re-deriving it.

---

### A.2 Theory, strongest form

The literature offers at least five structurally distinct explanations for why investment moves in
persistent, amplitude-heavy swings rather than tracking demand smoothly. None is individually
sufficient for India; together they are the reason a *state variable* is defensible even where a
*clock* is not.

**A.2.1 The accelerator — Clark, Samuelson, Chenery.** **Clark, John Maurice (1917), "Business
Acceleration and the Law of Demand: A Technical Factor in Economic Cycles"** (*Journal of Political
Economy* 25(3): 217–235) is the founding statement: because a firm's desired capital stock is
roughly proportional to the *level* of output it expects to sell, and gross investment must cover
both net additions to that stock and depreciation, a modest swing in the **growth rate** of demand
produces a much larger swing in **investment** — the accelerator amplifies output changes into
investment changes rather than merely tracking them. **Samuelson, Paul A. (1939), "Interactions
between the Multiplier Analysis and the Principle of Acceleration"** (*Review of Economics and
Statistics* 21(2): 75–78) combines this accelerator with the Keynesian multiplier in a simple
linear dynamic system and shows, depending on the two parameters (the marginal propensity to
consume and the accelerator coefficient), the combined system can produce **damped, explosive, or
oscillatory** paths — the first formal demonstration that investment-driven cycles can be
essentially endogenous to an economy's own propagation mechanism, not merely a response to external
shocks. **Chenery, Hollis B. (1952), "Overcapacity and the Acceleration Principle"** (*Econometrica*
20(1): 1–28) supplies the version this seat actually leans on: Chenery reframes the accelerator
around **capacity utilization** specifically — firms invest not off the level of output alone but
off the gap between current output and installed capacity, so investment surges when utilization
is high and stalls when idle capacity is ample. **For our seat**: Chenery's capacity-gap framing is
the direct theoretical ancestor of using OBICUS utilization percentile as L11's cleanest leg (A.2.6
below) rather than a raw output or investment-growth series.

**A.2.2 Time-to-build — Kydland-Prescott, applied to infrastructure gestation.** **Kydland, Finn E.
& Prescott, Edward C. (1982), "Time to Build and Aggregate Fluctuations"** (*Econometrica* 50(6):
1345–1370) is the formal case for why investment cycles have genuine *length*, not just amplitude:
new productive capital requires **more than one period to construct** — the model's crucial feature
— so an investment decision today shows up as installed capacity only years later, and the
lag itself, not any information friction, is what stretches an investment boom's visible effects
across years the accelerator alone would not predict. Applied to infrastructure specifically —
power plants, roads, ports — construction gestation commonly runs several years from financial
close to commissioning `[VERIFY: precise India-specific gestation-length figures by asset class —
general infrastructure-project-finance knowledge, not independently re-verified against a primary
source this session; the fincycle-deep monograph's own analogous figure for housing, RERA-era
project completions of 3–5 years with pre-RERA overruns "routinely doubling that," is the nearest
verified comparator inside this program]`. **For our seat**: this is a second, independent reason
(alongside A.1iv's mean-reversion argument) why L11's τ½ sits in the multi-year band rather than
the quarter-to-quarter band L2's fast-stress triggers occupy — physical construction time is a
hard floor on how fast an investment cycle's *real* leg can turn, wholly separate from how fast
sentiment or credit availability can turn.

**A.2.3 Tobin's q, and its documented empirical weakness.** **Tobin, James (1969), "A General
Equilibrium Approach to Monetary Theory"** (*Journal of Money, Credit and Banking* 1(1): 15–29)
proposes the cleanest theoretical link between financial markets and real investment: firms should
invest when the market value of installed capital (q) exceeds its replacement cost, and stop when
q falls below 1 — a forward-looking, market-price-based investment rule requiring no reference to
cash flow or credit availability at all. The honest empirical record is that **q performs poorly**
as a stand-alone predictor of firm-level investment; **Fazzari, Steven M.; Hubbard, R. Glenn &
Petersen, Bruce C. (1988), "Financing Constraints and Corporate Investment"** (*Brookings Papers on
Economic Activity* 1988(1): 141–195) is the classic demonstration that **cash flow** has
incremental explanatory power for investment *even after controlling for q* — evidence read as
firms facing a "financing hierarchy" in which internal funds carry a real cost advantage over
external finance, contradicting frictionless q-theory's own prediction that financing source should
be irrelevant. **For our seat**: this is the theoretical license for why L11's construction leans
on **utilization and production quantities** (OBICUS, IIP capital goods) rather than any market-
value-based proxy for q — a market-price signal that theory says should be sufficient turns out,
empirically, to need a cash-flow/credit-availability co-signal exactly of the kind A.2.4's coupling
to L10 supplies.

**A.2.4 The corporate-finance channel — Bernanke-Gertler, and the L10–L11 coupling stated as
mechanism.** **Bernanke, Ben S. & Gertler, Mark (1989), "Agency Costs, Net Worth, and Business
Fluctuations"** (*American Economic Review* 79(1): 14–31) is the paper A.1iii's DAG edge is
ultimately theory for. Because external finance carries an agency-cost premium over internal funds
(the same financing-hierarchy logic A.2.3 flags empirically), a borrower's own **net worth**
determines how much external finance it can raise and at what premium — and net worth itself moves
procyclically with asset prices and cash flow. The resulting **financial accelerator**: a positive
shock raises net worth, which cheapens external finance, which raises investment, which (in
aggregate) raises asset prices and cash flow further, reinforcing the initial net-worth gain — and
the same loop runs in reverse on the way down, with investment collapsing further and faster than
a frictionless model would predict once collateral values and cash flow deteriorate together.
**For our seat**: this is the mechanism, stated explicitly rather than assumed, behind the ladder's
own coupling of L11 to L10 — investment amplifies credit conditions (firms invest more when
financing is cheap and available) and credit conditions amplify investment outcomes (a capex bust
depresses the collateral and cash-flow base future credit decisions are made against) in the same
loop, which is precisely why the two objects cannot be treated as independent evidence inside one
shared budget (A.4 below) even though they are measured from different data.

**A.2.5 Overinvestment traditions, handled honestly — the Austrian kernel minus its theology.**
The **Austrian** malinvestment tradition — Mises's original *Theory of Money and Credit* (1912) and
Hayek's subsequent elaboration — argues that artificially cheap credit (via fractional-reserve
banking or a central bank holding rates below the "natural" rate) systematically misdirects
investment toward projects that only appear profitable at the distorted price of capital, producing
a boom that must eventually "correct" once the distortion is recognized. Hayek's own specific
mechanism — cheap credit biases investment toward more **"roundabout"** (capital-intensive,
longer-gestation) production processes and more durable capital goods than final consumer demand
actually justifies, so the economy's capital structure becomes internally inconsistent with its own
underlying time preferences — is, read narrowly, a length-and-durability claim about *which* capex
gets built during a credit boom, structurally consistent with A.2.2's time-to-build point (the
longest-gestation infrastructure projects are exactly the ones a Kydland-Prescott-style multi-year
commitment cannot cheaply reverse once started) even though this program declines the surrounding
claim that only an undistorted natural rate would avoid the problem. The full doctrine carries
a policy theology this program explicitly declines to adopt — a claimed unique natural rate of
interest, and a prescription (liquidationism: let the bust run its full course, uncushioned) the
post-2008 policy record and the mainstream macro-finance literature broadly reject. What survives,
stripped of the theology, is a genuine descriptive kernel with real theoretical support elsewhere:
**capital heterogeneity** — a factory built for one product mix cannot costlessly become a factory
for a different one — combines with **irreversibility** under uncertainty, formalized rigorously in
**Dixit, Avinash K. & Pindyck, Robert S. (1994), *Investment Under Uncertainty*** (Princeton
University Press), which shows that once capital is sunk, waiting for better information has
genuine option value the naive net-present-value rule ignores, and a firm that invested at the top
of a boom holds an asset it cannot cheaply reallocate when conditions turn. **For our seat**: this
licenses treating an "overbuild" as a real, structural hazard — heterogeneous, irreversible capital
means a capex boom leaves behind capacity that cannot be quickly redeployed when demand disappoints
— without endorsing any claim about a unique correct interest rate or a policy prescription against
countercyclical stabilization; the kernel is descriptive risk, not doctrine.

**A.2.6 Utilization mean-reversion as the measurable core.** Of everything above, exactly one
object is bounded, definitionally mean-reverting, free, and available in real time without a
revision or splice problem: capacity utilization itself. A utilization rate cannot rise
indefinitely (physical capacity caps it near 100%) or fall indefinitely (firms idle or scrap
capacity, or exit, rather than run at 0% forever) — the series is mean-reverting **by
construction**, not by an empirical regularity that could someday fail to hold. This is why D08's
own construction insists on the **percentile rank of trailing OBICUS utilization**, never a fixed
threshold (A.1i) — Contract §6's no-magic-numbers rule and Chenery's capacity-gap theory (A.2.1)
point to the same operational choice from opposite directions, one a design principle and one an
economic mechanism. **For our seat**: OBICUS is the cleanest real-time leg of the three inputs
precisely because IIP capital-goods (subject to base-year revisions and index-methodology changes)
and GFCF/GDP (subject to the GDP denominator's own periodic rebasing — the 2022–23 base-year
revision released 27 February 2026, with a full back-series splice not due until December 2026,
sits directly inside this program's current research window) both carry measurement-continuity
risk that a bounded percentage utilization rate simply does not.

**Citations (A.2).** Clark, J.M. (1917), *JPE* 25(3): 217–235 **[Verified]**. Samuelson, P.A.
(1939), *REStat* 21(2): 75–78 **[Verified]**. Chenery, H.B. (1952), *Econometrica* 20(1): 1–28
**[Verified]**. Kydland, F.E. & Prescott, E.C. (1982), *Econometrica* 50(6): 1345–1370
**[Verified]**. Tobin, J. (1969), *JMCB* 1(1): 15–29 **[Verified]**. Fazzari, S.M.; Hubbard, R.G. &
Petersen, B.C. (1988), *Brookings Papers on Economic Activity* 1988(1): 141–195 **[Verified]**.
Bernanke, B.S. & Gertler, M. (1989), *AER* 79(1): 14–31 **[Verified]**. Dixit, A.K. & Pindyck, R.S.
(1994), *Investment Under Uncertainty*, Princeton University Press **[Verified]**.

---

### A.3 The twin-balance-sheet mechanism (the India-relevant core)

**A.3.1 The atlas's own capacity-limit sentence, unpacked.** The Atlas states L11's mechanism in
one line: "balance-sheet repair after an overbuild takes years of deleveraging no information flow
can shortcut (capacity limit)" (row 1.6). D08's own decay analysis states the same claim as a
survival argument: "a large capex/real-estate down-cycle unwind (stalled projects, land-title/
approval delays, sector-wide overleverage) takes years of real balance-sheet repair to resolve; no
amount of information efficiency shortens that physical/legal/financing timeline" (D08 Edge B).
This is a genuinely different survival argument from L3's momentum (limited attention, which
sophisticated capital could in principle correct faster) or L9's global cycle (a compensated risk
premium, which persists by definition rather than by friction) — it is **(ii) capacity limit** in
the Contract's own §5 taxonomy: the constraint binds regardless of how many desks know about it,
because the thing being constrained is physical, legal, and financial capacity to unwind, not
information. India's own official record already names the "stalled project" as a countable
object, not a metaphor: the **Economic Survey 2014–15** identified a secular rise in stalled
projects dating from 2007 — the tail end of the 2003–08 boom this file's own chronology dates
(A.1iv) — concentrated in infrastructure and linked sectors, with the private-sector share of
stalled-project value running **two-to-three times** the public-sector share `[VERIFY: exact
stalled-project value/GDP figures — Economic Survey 2014–15's own finding, corroborated across
secondary summaries this session, not independently re-pulled from the primary PDF]`. The Survey's
own diagnosis reads as a checklist of exactly the "physical/legal/financing" frictions D08 Edge B
names generically: cost overruns as global growth slowed, environmental and land-acquisition
clearances stalling mid-project, and rupee depreciation pushing corporate cash flows short of
already-contracted debt-servicing obligations — none of which a faster information flow would have
resolved any sooner, because none of them is an information problem.

**A.3.2 Koo's balance-sheet recession — the general theory.** **Koo, Richard C. (2003), *Balance
Sheet Recession: Japan's Struggle with Uncharted Economics and Its Global Implications*** (John
Wiley & Sons) supplies the mechanism for *why* the repair specifically takes years rather than
quarters. Koo's central claim: after a debt-financed asset boom collapses, firms whose balance
sheets are underwater do not respond to conventional monetary easing by borrowing and investing —
their objective function has shifted from profit maximization to **debt minimization**, because a
firm with liabilities exceeding assets rationally prioritizes repairing its balance sheet over
pursuing even genuinely profitable new projects, since new borrowing against an already-negative
net worth is either unavailable or irrational to seek. Cutting rates to zero does not fix this: the
constraint is not the *price* of credit but the *demand* for credit from balance-sheet-impaired
borrowers, and that demand recovers only as slowly as the underlying repair — years, in Koo's own
Japan case, not the quarters a standard monetary-transmission model would predict. **For our seat**:
this is the theoretical account of why L11's construction cannot be a fast-reacting series even in
principle — a genuine post-overbuild repair is gated by the balance-sheet-minimization behavior
Koo documents, not by anything a faster information flow could accelerate.

**A.3.3 Debt overhang — the corporate mechanism and its empirical duration.** **Myers, Stewart C.
(1977), "Determinants of Corporate Borrowing"** (*Journal of Financial Economics* 5(2): 147–175)
supplies the precise corporate-finance mechanism underneath the repair delay: a levered firm with
valuable future investment opportunities may rationally **reject positive-NPV projects** because
enough of the project's payoff would flow to existing creditors (via reduced default risk) rather
than to the equity holders funding the new investment — debt overhang, formally. A firm does not
need to be insolvent for this to bind; it merely needs enough legacy debt that new equity-funded
investment disproportionately benefits bondholders. This is a genuinely different channel from
Koo's behavioral debt-minimization account — Myers's mechanism is a rational response to a capital-
structure distortion, not a shift in objective function — and the two reinforce each other in
practice. For **how long** such an overhang typically persists, this program's own reading of
**Reinhart, Carmen M.; Reinhart, Vincent R. & Rogoff, Kenneth S. (2012), "Public Debt Overhangs:
Advanced-Economy Episodes since 1800"** (*Journal of Economic Perspectives* 26(3): 69–86) supplies
a cross-country empirical anchor for "years, not quarters," even though that paper's own object is
**sovereign**, not corporate, debt: across 26 identified advanced-economy public-debt-overhang
episodes since 1800, growth ran roughly one percentage point lower for an **average duration of
about 23 years**. This program uses that finding **analogically, not as a direct corporate-sector
estimate** — the mechanism (impaired balance sheets depress forward activity for a genuinely
multi-year, not multi-quarter, span) transfers; the specific 23-year figure does not, and this file
states that distinction rather than blur it.

**A.3.4 Zombie lending — Caballero-Hoshi-Kashyap, and India's own AQR parallel.** **Caballero,
Ricardo J.; Hoshi, Takeo & Kashyap, Anil K. (2008), "Zombie Lending and Depressed Restructuring in
Japan"** (*American Economic Review* 98(5): 1943–1977) supplies the mechanism for why the
*banking-system* side of a twin-balance-sheet drought can itself extend the repair beyond what
corporate deleveraging alone would take: banks facing their own capital constraints have an
incentive to **evergreen** loans to insolvent ("zombie") borrowers — extending fresh, subsidized
credit that lets a zombie firm avoid default — rather than recognize the loss and force
restructuring, because recognition would crystallize the bank's own capital shortfall. The result
is not merely forbearance toward individual weak firms; Caballero-Hoshi-Kashyap show it **congests
the market for healthy competitors**, depressing their profits, entry, and investment, and lowering
aggregate productivity and job creation/destruction in zombie-dominated industries. **India's own
2011–2018 chronology is a close domestic parallel**, already documented in this program's D03
credit-cycle dossier: the 2011–15 "Twin Balance Sheet" period saw corporate over-leverage and
rising restructured/disguised-standard bank assets accumulate largely unrecognized — the Economic
Survey 2016–17 estimated stressed assets (NPA plus restructured) near 12% of loans by the time the
problem was acknowledged — until RBI's 2015–18 **Asset Quality Review** (under Governor Rajan)
forced reclassification, and reported GNPA jumped mechanically from 5.1% (Sep-15) to 7.6% (Mar-16)
to 9.3% (FY17) to 11.2% (FY18) — not because bank asset quality suddenly worsened in those quarters,
but because years of **prior**, evergreening-style non-recognition were finally being marked to
reality in one multi-year recognition shock (D03, already the source for L10's own GNPA-as-lagging-
confirm-only design rule). **For our seat**: this is the specific historical episode L11's 2011–2020
"capex winter" reading is standing on — an overbuild (2003–08) that generated both the corporate
debt overhang (A.3.3) and the bank-side non-recognition (this section) simultaneously, with the
capex recovery only becoming visible in OBICUS/GFCF terms years **after** the AQR had forced the
credit system's own reckoning, consistent with Bernanke-Gertler's coupled-collapse mechanism
(A.2.4) running in reverse on the way back up.

**A.3.5 Why repair-time is the quantity this program's own analogue trial measures.** The desk's
own pre-registered IN2 trial (`capex-RESULTS.md`), run on the JST Macrohistory Database's
investment/GDP (`iy`) series across 18 advanced economies since 1870, is built to answer exactly
the question A.3.1–A.3.4 pose theoretically: once investment share peaks, how long until it
regains that peak? The pre-registered bar was **median repair length ≥ 4 years** — a threshold set
specifically to distinguish a "years, not quarters" repair story from a business-cycle-length one.
Result, on 195 identified peak spells (23 right-censored spells counted at their censoring value,
as pre-registered — a choice that biases the reported median **down**, against the hypothesis): the
median repair length is **exactly 4 years**, with a wide honest interquartile range of **1–12
years**. The result reads as a **pass at the bar, not a comfortable clearance** — the wide IQR
(a full quarter of peak spells recover within a year) is itself informative: many `iy` local
maxima are shallow, ordinary business-cycle wiggles, not genuine overbuilds, which is precisely why
L11's design (A.1i, A.2.6) keys off **percentile extremes** in the utilization/capex-share series
rather than reacting to every peak. The theory (A.3.1–A.3.4) predicts multi-year repair for a true
overbuild; the analogue evidence confirms a multi-year *median* while being honest that the
distribution is wide enough that "years" cannot be sharpened into a point estimate without
badly overstating the seat's own precision.

**Citations (A.3).** Koo, R.C. (2003), *Balance Sheet Recession*, John Wiley & Sons **[Verified]**.
Myers, S.C. (1977), *Journal of Financial Economics* 5(2): 147–175 **[Verified]**. Reinhart, C.M.;
Reinhart, V.R. & Rogoff, K.S. (2012), *Journal of Economic Perspectives* 26(3): 69–86
**[Verified]**. Caballero, R.J.; Hoshi, T. & Kashyap, A.K. (2008), *American Economic Review*
98(5): 1943–1977 **[Verified]**.

---

### A.4 Why the seat is CLAMPED non-positive

This is the seat's most counterintuitive design choice, and the desk's own working papers show it
was not obvious even to the design's own authors on a first pass — which is exactly why it earns a
full teaching treatment rather than a stated rule.

**A.4.1 The consistency-audit finding that forced the clamp.** `research/register/consistency-
audit.md` records the design gap in its own words, filed as finding **C2**: "A Tier-C entry (L11,
capex cycle) can add — not just reduce — regime score, through the shared-block average, with
nothing in DESIGN.md, ladder.yaml, or validator.py stopping it." The mechanics of the gap are worth
walking through precisely, because the failure mode is subtle and generalizes beyond this one seat.
Contract §4 states plainly: "Tier-C signals may only REDUCE risk — never add." `ladder.yaml`
correctly flagged L11 `tier: C, reduce_only: true` — the **flag** was right. But L11's `block` is
`macro_credit_block`, one of the six **additive** `regime_score_blocks`, not the segregated
`tierC_overlay` bucket the validator actually caps at ≤0.10 and treats as negative-only by
construction. `DESIGN.md` §4.2's own stated aggregation rule for that shared block — "the composite
uses the first principal component or a simple average" — says nothing about a sign restriction on
any *individual* member's contribution. A simple average of four series, three of them (L6, L10,
L12) full-authority Tier B with no sign restriction at all, blends L11's own reading in with
**nothing** forcing that specific contribution to zero-or-negative. If L11 reads positive (capex
cycle genuinely turning up), an unmodified average necessarily pushes the shared macro-credit
score up — which is precisely what a Tier-C entry is forbidden to do by Contract §4, and the
registry's own automated validator (which checks the `reduce_only` **flag**, not the **aggregation
formula**) would have loaded this cleanly regardless, because the flag and the arithmetic are
different things and only the former had an enforced check.

**A.4.2 The asymmetric information content — why the fix is a one-sided clamp, not a lower weight.**
The audit's fix — and the reason a **clamp** (`min(0, reading)` applied *before* aggregation) is
the right instrument rather than, say, simply down-weighting L11's coefficient — rests on a real
economic asymmetry, not merely an arithmetic patch. A hot capex reading (rising utilization, strong
capital-goods output, GFCF share climbing) is, on the strongest form of A.2's own theory, **mostly
already visible in L10's own reading**: Bernanke-Gertler's coupled-accelerator mechanism (A.2.4)
means an investment boom that is genuinely being financed shows up contemporaneously in credit
growth, issuance quality, and the credit/GDP gap L10 already reads directly — L11's positive signal
adds comparatively little **independent** information on the upside, which is exactly D08's own
double-counting warning (A.1ii) stated as an information claim rather than merely a budget-sharing
one. A weak or falling capex reading — utilization declining while capacity stays high, capital-
goods output rolling over — carries a **different** informational status: it can be the earliest
visible sign of an overbuild whose credit-side consequences (A.3's twin-balance-sheet repair) have
not yet shown up in L10's own series, because GNPA recognition specifically lags by construction
(D03's own AQR chronology, A.3.4, is the direct evidence: years of accumulating stress before the
2015–18 recognition shock). The academic asset-growth literature supplies independent, non-India,
mechanism-consistent support for exactly this asymmetry at the firm level: **Titman, Sheridan; Wei,
K.C. John & Xie, Feng (2004), "Capital Investments and Stock Returns"** (*Journal of Financial and
Quantitative Analysis* 39(4): 677–700) find firms that sharply increase capital investment
subsequently earn **negative** benchmark-adjusted returns, an effect the authors attribute to
investor under-reaction to the empire-building implications of the investment (G.1 below returns to
this same paper); **Cooper, Michael J.; Gulen, Huseyin & Schill, Michael J. (2008), "Asset Growth
and the Cross-Section of Stock Returns"** (*Journal of Finance* 63(4): 1609–1651) document the
effect at portfolio scale — the lowest-asset-growth decile earns roughly 26% annualized raw returns
against roughly 6% for the highest-growth decile, a 20-point annual spread, with asset growth
retaining forecasting power even after controlling for book-to-market, size, and momentum. Neither
paper documents a comparably strong *positive* signal from low investment — the asymmetry runs one
way in the firm-level literature just as A.3–A.4's mechanism argues it should at the macro/sector
level: overbuild predicts trouble with real information content; a strong-but-unremarkable capex
print mid-cycle carries comparatively little content the shared block does not already hold.

**A.4.3 The mechanics, stated precisely.** `ladder.yaml`'s `contribution_clamp: non_positive` field
implements `min(0, reading)` on L11's own state **before** it enters the `macro_credit_block`
composite — a hot capex print is mapped to exactly zero contribution to the shared score, never a
negative-but-small one and never a positive one, while a cold/overbuild-signature reading passes
through unmodified and can pull the shared composite down. This is deliberately robust to *how* the
composite itself is built: whether the eventual data-phase implementation uses a simple average or
a first principal component (`DESIGN.md` §4.2's stated options), clamping the individual
contributor's sign before aggregation guarantees the reduce-only property holds regardless of the
aggregation method chosen later — the fix targets the actual failure mode the audit found (a flag
that constrained the entry but not the arithmetic) rather than merely tightening one specific
formula that might later be swapped for another.

**A.4.4 What would ever unclamp it.** `ladder.yaml`'s own `changes_if` field for L11 states the
condition plainly: "purged India backtest; cross-country capex pooling." Two things are worth
being honest about here. First, the cross-country pooling path has **already been tried once**, by
this program's own pre-registered IN1 trial (`capex-RESULTS.md`): capex state versus forward 5-year
real equity returns, tested on 15 JST-panel countries against a pre-registered bar of ≥70%
sign-consistency (the same class of test the sibling financial-cycle monograph ran and cleared at
17/17 — a genuine pooled regularity). IN1 came back at **60% negative (9 of 15 countries)** —
**below** the bar. The trial's own honest read places this "between demographics (4/16, rejected)
and the financial cycle (17/17, seated Tier-B): a weak tilt, not a pooled regularity," and states
the consequence without hedging: "the analogue panel does NOT supply the 'C→B via analogues'
graduation — L11 STAYS Tier C. No re-run, no bar moved." The atlas's own "C→B via analogues" note
on row 1.6 names the *pathway*, not an accomplished fact — this program ran that pathway once, at a
pre-registered bar, and it did not clear. Second, and more directly relevant to the clamp
specifically rather than the tier: the companion IN3 trial measured quintile asymmetry in the same
pooled data — pooled mean forward 5-year log real returns of **+0.242** for the top capex-state
quintile versus **+0.287** for the bottom quintile (n=310/305 country-years), with the **middle**
quintile lowest of all at **+0.202** (n=891). The state does not order forward returns
monotonically. The trial's own honest read calls this "the clamp's vindication, in an unexpected
shape": the top-quintile penalty relative to the bottom is real but mild, the relationship is not
clean, and "a seat this weakly informative must never ADD regime score; subtract-only at the hot
extreme, inside the shared budget, is precisely what min(0,·) implements." Put plainly: the one
piece of analogue evidence that could argue for unclamping — a strong, clean, monotonic positive
tilt on the top-quintile side — is not what the desk's own pre-registered trial found. The realistic
remaining path to any change is the India-specific purged backtest on OBICUS/IIP/GFCF the `changes_
if` field names, which requires the data phase this research phase does not include, and even that
would need to clear a bar this program's own cross-country analogue already failed to clear on the
positive side.

**Citations (A.4).** Titman, S.; Wei, K.C.J. & Xie, F. (2004), *Journal of Financial and
Quantitative Analysis* 39(4): 677–700 **[Verified]**. Cooper, M.J.; Gulen, H. & Schill, M.J.
(2008), *Journal of Finance* 63(4): 1609–1651 **[Verified]**. IN1–IN3: `research/cycles/capex-
deep/capex-RESULTS.md` (this program's own pre-registered analogue trial, JST Macrohistory
Database R6).

---

### A.5 Harvest limits

**What L11 can do.** Three things, each already licensed by A.1–A.4 above and none exceeding them.
**First**, subtract regime score inside the shared `macro_credit_block` when the utilization/
capex-share state reads a cold, overbuild-consistent extreme — the one direction the clamp leaves
open, and the direction A.3's mechanism and A.4.2's asymmetric-information argument both say
carries genuine content. **Second**, condition sector-level tilts on infrastructure, industrial,
and capital-goods names — `ladder.yaml`'s own `role` field says this explicitly ("sector-level tilt
confirmation only"), and the atlas's own Band-2 sector-projection table (§14) is unambiguous that
cement/infra/cap-goods names decompose directly onto L11 and L12 — an overbuilt sector-level state
is a legitimate input to *which* names carry capex-cycle risk, entirely separate from the regime-
score question. **Third**, feed the hedge-scheduling watch — an overbuild reading co-occurring with
a deteriorating L10 credit state is exactly the R3/R4-bucket condition (`DESIGN.md` §5.1) the
hedge-ratio grid is meant to widen against, and L11's marginal contribution there is confirmatory
timing information (a capex-side confirmation that a credit-side deterioration is not an isolated
data artifact), not an independent trigger.

**What L11 cannot do.** Four things, each the direct negative of a claim A.1–A.4 explicitly
declined to make. It cannot **time a boom** — the clock test fails at n≈2–3 (A.1iv), timing
uncertainty on cycles this long runs ±20% or worse by the atlas's own stated epistemics (Atlas §0),
and IN1's own sign-consistency failure (A.4.4) is direct evidence the state carries too little
clean predictive content to support a dateable call even in the cross-country pooled data where
sample size is not the binding constraint. It cannot **add to the regime score** — the clamp is
mechanical, not a matter of degree, and A.4's reconstruction of the consistency-audit finding shows
precisely how easily this property leaks away without an explicit, arithmetic-level enforcement.
It cannot **stand alone outside the block** — L11 has no independent entry in `regime_score_blocks`
(`ladder.yaml`'s budget header lists exactly six blocks, and `macro_credit_block` is the only one
touching L11), and its DAG dependency on `L10_credit_block` means it is not even computable as a
free-standing series in this design; it exists only as a conditional adjustment to a composite three
other, higher-authority seats already anchor. And it cannot **claim a return-sleeve budget** — unlike
L3 (momentum) or L8 (value spread), which carry explicit EDGE authority inside the atlas's own
four-harvest taxonomy (Atlas §0), L11 is filed purely under REGIME, and the reduce-only clamp means
even that REGIME authority is one-directional. The honest summary, in the atlas's own harvest
language: L11 earns exactly one harvest — **REGIME (clamped reduce-only)** — and nothing this file
has found changes that classification.

**Synthesis — mechanism, observable, seat, and the honest gap.**

| Mechanism | Observable (free India/global series) | L11 input consumed | What nothing free captures |
|---|---|---|---|
| Accelerator / capacity-gap (A.2.1, Chenery) | OBICUS utilization percentile | The utilization leg — the cleanest, bounded, real-time input | Sector-level utilization granularity (OBICUS is manufacturing-aggregate; a single infra sub-sector's own utilization is not separately published free) |
| Time-to-build (A.2.2, Kydland-Prescott) | RERA-era completion timelines (qualitative); IIP capital-goods lead/lag vs GFCF | Sets the τ½ length prior (36–60m) and the expectation that recovery lags demand by years | India-specific, asset-class-level gestation-length data (power/roads/ports) — no free, project-level dataset exists |
| Tobin's q weakness / cash-flow channel (A.2.3) | N/A — deliberately not constructed | Justifies leaning on production/utilization quantities instead of a market-value proxy | A market-based q for unlisted or thinly-traded capital-goods issuers — not free, and theory itself says it would underperform cash-flow proxies |
| Financial accelerator (A.2.4, Bernanke-Gertler) | L10's own credit/GDP gap and issuance-quality series | The DAG coupling itself — L11 conditioned against L10, never independent | A direct India firm-level net-worth/investment sensitivity estimate — not attempted; the mechanism is imported, not re-estimated |
| Capital heterogeneity / irreversibility (A.2.5, Dixit-Pindyck) | Qualitative — sector capex commitments, stalled-project record (A.3.1) | Underwrites treating an overbuild as genuine structural risk, not merely a noisy print | An India-specific option-value-of-waiting estimate by sector — no free data supports this |
| Twin-balance-sheet repair (A.3.2–A.3.4, Koo/Myers/Caballero-Hoshi-Kashyap) | GFCF/GDP percentile; L10's GNPA-as-lagging-confirm; RBI FSR stressed-asset series | The repair-length expectation (A.3.5's IN2 median 4y) that keeps L11 from reacting to every wiggle | A verified India-specific corporate-debt-overhang duration estimate — Reinhart-Reinhart-Rogoff's 23y figure is sovereign-debt evidence used analogically only (A.3.3) |
| Asymmetric overbuild-vs-boom information content (A.4.2, Titman-Wei-Xie/Cooper-Gulen-Schill) | IN1/IN3 pooled JST-panel results | The clamp itself (`min(0, reading)`) | An India-specific firm-level asset-growth/forward-return test — queued behind the fundamentals-phase price-only mandate (Contract §7 prior #7) |

**The sharpest honest gap.** IN1's own sign-consistency failure (A.4.4, 60% vs a 70% bar) means
this seat's cross-country evidence is meaningfully weaker than its sibling L12's (17/17 on the
analogous financial-cycle co-movement test) even before any India-specific data exists — the clamp
is not a conservative buffer against a strong signal this program merely wants to size carefully; it
is the correct-sized response to a genuinely weak one, and this file states that plainly rather than
letting the mechanism-rich theory sections above imply a stronger empirical case than the desk's
own trial actually found.

---

## PART G — Operator psychology

Part A documents a mechanism this desk is unusually exposed to on two separate fronts at once.
First, the ordinary operator hazards every capex-cycle desk faces — CEOs who herd into capacity
expansion, analysts who extrapolate order books, governments that time infrastructure spending to
elections. Second, and specific to this desk in this decade: India's 2021–26 public-and-private
capex broadening is not a neutral background fact the desk observes from outside — it is a
narrative this desk, its principals, and the broader Indian financial-commentary ecosystem it reads
every day have every professional and personal incentive to want to be true. Both fronts point the
same direction, which is exactly why they compound rather than offset.

### G.1 CEO capex herding and empire-building

**Mechanism.** **Scharfstein, David S. & Stein, Jeremy C. (1990), "Herd Behavior and Investment"**
(*American Economic Review* 80(3): 465–479) formalizes why individually rational managers can
produce collectively irrational, synchronized investment booms: a manager concerned about how an
investment decision will be read by the labor market (does a contrarian call, right or wrong,
signal poor judgment more than a consensus call that turns out wrong?) has a reputational incentive
to **mimic peers' investment decisions rather than act on independent private information** — an
information cascade in which each firm's capacity expansion is read by the next firm as a signal
worth following, regardless of whether any firm actually possesses superior demand information.
This is a genuine mechanism for why capex cycles overshoot in a **correlated, sector-wide** way —
cement, steel, and infrastructure capacity commonly expand together, not because every firm
independently verified end-demand, but because none wanted to be the visible outlier if the boom
proved real. Layered on top, **Jensen, Michael C. (1986), "Agency Costs of Free Cash Flow,
Corporate Finance, and Takeovers"** (*American Economic Review* 76(2): 323–329) supplies the
incentive that makes herding into *expansion* specifically, rather than herding into caution, the
more common failure: managers controlling free cash flow in excess of positive-NPV opportunities
have a private incentive toward **empire-building** — firm size correlates with managerial power,
compensation, and prestige more reliably than payout discipline does — so absent strong governance
or debt-market discipline, cash-rich firms in a capex boom systematically over-invest relative to
the shareholder-value-maximizing benchmark. Titman-Wei-Xie's own finding (A.4.2) — that the
negative capex-investment/return relation is **stronger** specifically for firms with greater
"investment discretion" (higher cash flow, lower debt ratios) and weaker where hostile-takeover
discipline was more prevalent — is direct empirical confirmation of the Jensen mechanism operating
exactly where governance discipline is weakest.

### G.2 "This time capacity is different"

**Mechanism.** A.3.4's honest framing — RERA-style regulatory tightening or PLI-style targeted
manufacturing incentives plausibly making the 2021+ capex cycle more disciplined than 2003–08's —
is a genuine, evidence-consistent observation, exactly analogous to the fincycle-deep monograph's
own G.4 treatment of "RERA changed everything" for the property cycle. It is also precisely the
sentence a desk under narrative pressure converts into "this cycle's capacity build is structurally
different, so the old overbuild-then-repair pattern does not apply" — the general this-time-is-
different pattern the debt-supercycle monograph documents for sovereign debt and the fincycle-deep
monograph documents for the property cycle, recurring here in its capex-specific form. A
policy-driven capacity narrative (PLI-linked manufacturing, China+1 relocation, government capex
multiplier effects) can be entirely correct as a description of *why capacity is being built* while
being entirely irrelevant to whether Chenery's capacity-gap mechanism (A.2.1), Bernanke-Gertler's
financial accelerator (A.2.4), or Koo's balance-sheet-repair dynamics (A.3.2) have stopped
operating once that capacity meets whatever demand actually materializes.

**Countermeasure.** The Tier-C classification with a single named upgrade path (A.4.4) is the
structural answer: no narrative about *why this capex cycle is different*, however well-evidenced
on its own terms, moves L11 out of its clamped, reduce-only station — only a purged India backtest
or a cross-country pooling result clearing a pre-registered bar can, and A.4.4 already documents
that the one such trial run so far (IN1) did not clear it.

### G.3 Government-capex political cycles

**Mechanism.** **Nordhaus, William D. (1975), "The Political Business Cycle"** (*Review of
Economic Studies* 42(2): 169–190) is the founding formal case for opportunistic pre-election fiscal
and monetary expansion; **Drazen, Allan & Eslava, Marcela (2010), "Electoral Manipulation via
Voter-Friendly Spending: Theory and Evidence"** (*Journal of Development Economics* 92(1): 39–52)
sharpens this specifically toward **composition**: politicians facing re-election systematically
shift spending toward highly visible, voter-salient categories — the paper's own leading example is
infrastructure (roads, schools, water systems) — while contracting other spending, and voters
respond to the targeting. This has a direct measurement consequence for L11's own inputs: a
pre-election government capex push can show up in IIP capital-goods output and even in headline
order-book commentary as if it were private-sector capex-cycle acceleration, when the underlying
driver is a fiscal pulse timed to the electoral calendar rather than the accelerator or financial-
accelerator dynamics A.2 describes. Atlas rows 2.7 (fiscal/political spending cycle) and 3.7 (India
political/reform cycle, election n=9 since 1991, Tier B on timing) already carry this mechanism
inside the ladder as CONTEXT and a calendar-scheduling seat (L5) respectively — the operator hazard
specific to L11 is reading a government-capex-driven IIP capital-goods print as evidence of the
*private* capex cycle L11 is meant to be tracking. India's own recent Union Budget record supplies
a concrete magnitude for how large this pulse can be relative to the series L11 actually reads:
Union government capital expenditure rose from roughly ₹2.63 lakh crore (FY18) to a budgeted
₹11.21 lakh crore (FY26 BE) — near a 4.2x increase over eight years — with single-year jumps of
roughly 37.4% (FY24 budgeted growth) following 22.8% (FY23) `[VERIFY: exact lakh-crore figures and
year-on-year growth rates — press/PIB coverage of Union Budget documents, not independently
re-pulled from indiabudget.gov.in primary tables this session]`. A fiscal pulse of that magnitude,
landing in years adjacent to the 2019 and 2024 general elections, is large enough on its own to move
IIP capital-goods and GFCF readings independent of any private-sector accelerator or financial-
accelerator dynamics — exactly the confound this section names.

**Countermeasure.** No new machinery is required beyond what already exists: L5's own calendar-
scheduling role already exists precisely so election-window volatility is handled as scheduling,
not as a directional read (`ladder.yaml` L5: "leverage/vol scheduling into election/budget windows
… never a directional bet"), and the operator discipline this section adds is simply to route a
pre-election capital-goods surge through that same lens — a known, dateable, government-calendar-
linked pulse — rather than reading it as fresh evidence for or against L11's own private-investment
state.

### G.4 Analyst order-book extrapolation

**Mechanism.** Sell-side equity research routinely reports company order-book growth as a headline,
easily-disclosed number, and the natural analyst instinct — extrapolate the reported growth rate
linearly into forward revenue and EPS — ignores three things this file's own theory section already
names: execution and gestation lag (A.2.2's time-to-build result — an order book converts to
revenue only years later, and slowly), financing-constraint sensitivity (A.2.3's Fazzari-Hubbard-
Petersen finding — execution of the order book depends on cash-flow and credit access that can
tighten mid-execution), and the accelerator's own mean-reverting nature (A.2.1 — an order-book
growth *rate* this high is itself the kind of extreme a Chenery-style capacity-gap mechanism
predicts will not persist). This is the same anchoring-bias family D08 I3 already flags for
OBICUS's own "~75% magic number" practitioner heuristic (A.1i) — a salient, easily reported number
substituting for the harder, correctly-constructed percentile-rank read.

**Countermeasure.** L11's own construction is the guard by design: it never consumes order-book
data (unavailable free in any case — CMIE Capex-style project trackers are the paid alternative
D08 explicitly rules out under the Contract's free-data requirement) and instead reads realized
utilization and production quantities, which cannot be talked up by a sales narrative the way a
forward order pipeline can.

### G.5 The desk's own trap as an India bull

**Mechanism.** This is the section the other four exist to protect against in the desk's own
specific case. The "India capex supercycle" of 2021–26 — PLI-linked manufacturing, government
infrastructure push, private capex broadening from 2023–24 (A.1iv) — is not merely a data pattern
this desk observes; it is the dominant narrative of the India-investing commentary this desk reads
daily, a narrative every India-focused sell-side house, most financial media, and much of this
desk's own professional and social environment has a stake in being true. That creates a specific,
named motivated-reasoning risk: reading a genuinely positive OBICUS or GFCF print not as one
observation inside a Tier-C, n≈2–3 series the Contract's own tier system forbids from adding
regime-score authority (A.1iv, A.4), but as confirmation of a structural regime change the desk
already wants to believe in. The mechanism is not distinct from G.2's "this time is different" trap
in form — it is the same trap, aimed inward at the desk's own priors rather than at the market's.

**Countermeasure.** The clamp (A.4) is, among other things, exactly this discipline made mechanical
rather than aspirational: the desk cannot let itself size up on a hot capex print, however
compelling the accompanying narrative, because the seat is architecturally incapable of doing so —
`min(0, reading)` does not consult conviction. And the desk's own conduct on IN1 (A.4.4) is worth
naming as the concrete instance of the guard working as designed rather than merely existing on
paper: the sign-consistency bar (≥70%) was pre-registered before the print, IN1 came back at 60% —
a result an India-bullish desk under narrative pressure might have wanted to explain away, re-cut,
or re-run with adjusted country weights — and the trial's own written record states plainly "no
re-run, no bar moved." That is the Contract's pre-registration discipline (§9: "pre-register every
hypothesis before running it; never re-test a rejected idea with tweaked parameters") functioning
exactly as intended against exactly the motivated-reasoning risk this section names.

### G.6 Guards the Contract provides, and the failure-mode map

Four Contract-level mechanisms do this Part's actual protective work, none of them requiring the
operator to be wiser in the moment than the evidence justifies. **Tier-C, reduce-only by rule**
(Contract §4) — a structural classification, not a judgment call re-made each time a print lands.
**No magic numbers** (Contract §6) — the percentile-rank construction (A.1i, A.2.6) removes the
"~75% switches capex on" anchor a practitioner heuristic would otherwise supply. **Assume your
alpha decays, with a written survival argument** (Contract §5) — D08's own Edge B analysis already
states plainly that no India-specific quantified predictive study exists for the capex signal, Tier
B available only via the cross-country-analogue clause, with a generic McLean-Pontiff haircut band
as a placeholder pending validation — an honesty requirement that made room for IN1's negative
result rather than needing to explain it away. **Pre-registration with no re-test of a rejected
idea** (Contract §9) — the mechanism G.5 shows working directly on this program's own IN1 trial.

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Reading a hot OBICUS/GFCF print as regime-positive | Naive aggregation of a shared block gives a Tier-C entry unearned ADD authority (consistency-audit C2, A.4.1) | `contribution_clamp: non_positive` — `min(0, reading)` before aggregation; mechanical, not discretionary |
| Herding into sector-wide capacity expansion mistaken for demand-verified growth | Scharfstein-Stein reputational herding + Jensen empire-building (G.1) | L11 conditions sector tilts and hedge scheduling only, never a standalone capex-momentum bet; A.4.2's asymmetric-information argument already discounts the upside signal |
| "PLI/China+1/RERA-style discipline means this capex cycle won't overbuild" | This-time-is-different narrative capture (G.2), same pattern as fincycle-deep G.4 and debt-deep A.5 | Tier-C/Tier-B split frozen until a named evidentiary bar clears (A.4.4); IN1's own failure to clear that bar already on record |
| Mistaking a pre-election government capex pulse for private capex-cycle acceleration | Nordhaus opportunistic timing + Drazen-Eslava voter-friendly spending composition (G.3) | Routed through L5's existing calendar-scheduling seat, not read as an L11 state change |
| Extrapolating reported order-book growth linearly | Anchoring to a salient, easily reported number; ignores time-to-build and financing-constraint sensitivity (G.4) | L11 never consumes order-book data; reads realized utilization/production only |
| The desk's own India-bull priors reading a positive print as vindication | Motivated reasoning specific to this desk's professional environment (G.5) | Pre-registered bars set before the print (Contract §9); IN1's 60%-vs-70% result stands unmoved, unre-run |

None of these six guards asks the operator to notice the trap in the moment it is hardest to
notice — deciding whether *this* hot print is the one that finally means the cycle turned, deciding
whether *this* government infrastructure push is really private capex, deciding whether *this*
order book is the one worth trusting, deciding whether the desk's own India-bull instinct is right
this time. Each converts that live decision into a structural non-decision, made once, in the
registry and in the pre-registration record, before the moment that would have made it hardest —
which is the same design philosophy the sibling financial-cycle monograph's own G.5 states for L12,
applied here to a seat whose evidence, on this program's own honest first look, is weaker still.

---

*Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · 2026-09-01 ·
v1.0*

**Word count: 8,470**

---

# PART B — The case record (India at full length + three mirrors)

# PART B — The India capex-cycle case record

*Capex/infrastructure-supercycle monograph (atlas 1.6, seat L11) · Part B · v1.0 · 2026-09-01 ·
Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `config/ladder.yaml`'s `L11_capex_cycle` entry
(τ½ 36–60 months, **Tier C**, `reduce_only: true`, `contribution_clamp: non_positive`, shared
`macro_credit_block` budget with L6/L10/L12) as its governing design and `docs/CYCLE_ATLAS.md`
row 1.6 as its brief: "Balance-sheet repair after an overbuild takes years of deleveraging no
information flow can shortcut (capacity limit)." The desk's pre-registered analogue trials
IN1–IN3 now live in `research/cycles/capex-deep/capex-RESULTS.md` — that file existed by the
time this Part was finished and its numbers are cited directly below, never recomputed. **This
is the India seat**: unlike the property-cycle and credit monographs, where India supplies one
thin domestic instance against eight-to-ten rich cross-country cases, here India **is** the case
record — three full domestic episodes plus a live fourth — and the three international mirrors
(Asian Tigers, China, US shale) serve only to calibrate what "fast" and "slow" repair look like
elsewhere, never to substitute for India's own evidence. India's **credit-side mechanics** —
bank+NBFC aggregation, sectoral deployment, GNPA chronology, AQR, IL&FS — are already covered in
full in `research/cycles/credit-deep/partB-cross-country.md` (its own case #10, "India
2003–2018") and `research/dossiers/03-credit-financial-cycle.md`; this Part cross-references
those figures by name and does not re-derive them. India's **property-cycle** side (RERA, the
2021–2026 residential upcycle, IL&FS→developer-financing freeze) is fully covered in
`research/cycles/fincycle-deep/partB-cases.md` §B3; again cross-referenced, not duplicated. This
Part's own job is narrower and real-side: what India's investment rate, capacity utilization,
and capital-goods order books actually did across four episodes, in numbers.*

---

## B1. Why the India instance is thin evidence and OBICUS is younger than the cases it measures

CYCLE_ATLAS.md's own honest count is n≈2–3 (2003–08, the 2011–20 "drought," 2021+), and this
Part adds a fourth, older episode (1994–97→2002) that the Atlas's own dossier work (D08,
`research/dossiers/08-india-mid-cycles.md`, §I4) already flags but does not treat as fully
separate from the credit cycle's own chronology — "this dossier's capex-cycle state variable and
Workstream 03's credit-cycle/GNPA state variable are likely highly correlated, not independent."
That warning holds throughout what follows: every case below sits on top of a credit event this
desk's credit monograph already dates, and the two must never both be weighted at full strength
in the composite regime score (ladder.yaml already enforces this via the shared
`macro_credit_block` budget, not an additive one).

**The measurement-honesty problem this desk owes itself, stated up front (the direct capex
analogue of the property monograph's own §B3 admission).** RBI's Order Books, Inventories and
Capacity Utilisation Survey (OBICUS) — the cleanest, highest-frequency, free capacity-utilization
series India has — has been conducted only since 2008. That means **OBICUS did not exist for
case 1 (1994–2002) and covers only the tail end of case 2's boom (2003–2011)** — the two
episodes with the sharpest booms in this record are the two the desk's best instrument cannot
see in real time. MOSPI's IIP capital-goods sub-index runs further back (current base year
2011–12, after a revision from an earlier 2004–05 base `[VERIFY: exact revision year — dossier
08 flags this same uncertainty]`) but is itself subject to periodic base-year splices that
demand the same discipline the ladder's `tau_half_drift_policy` and the property monograph's
2026-rebase warnings already apply elsewhere. Quarterly GFCF/GDP (MOSPI National Accounts) is
the longest-running of the three free proxies and the only one that reaches back cleanly into
case 1, but it is a *ratio*, not a *rate of capacity use* — it tells you how much of GDP went
into fixed investment, not whether that investment was chasing genuine excess demand or
running into an already-glutted sector. The free substitute triad the credit-side dossier
already names — **OBICUS + IIP capital goods + GFCF/GDP** — is the correct free construction
(CMIE's project-level Capex database, the field's best-known tracker of stalled/announced/
completed projects, is a **paid** source and is used below only where a public news report has
already reproduced a specific CMIE-sourced figure, each flagged accordingly per the Contract's
free-data rule).

---

## B2. Four India case studies

### 1. India 1994–97 → 2002 — the first liberalization capex boom and bust

**Setup — what 1991 actually removed.** Facing a 1991 balance-of-payments crisis, the Government
of India dismantled the industrial licensing regime ("License Raj"), formally empowered SEBI as
market regulator, established the National Stock Exchange, and opened Indian equities to foreign
institutional investors. The immediate capital-markets effect was on *pricing freedom*: premium
(above-par) issues, which were just **1.37% of new issues in 1991–92**, rose to **45.90% by
1994–95** — the single cleanest statistic of how completely the pre-liberalization administered-
price regime for new capital had been dismantled in three years.

**The boom, dated precisely.** India's primary-equity-market mania "began towards the end of
1994 and peaked in February 1995." **January 1995 alone saw 145 equity issues open for
subscription**, including "mega issues" from Reliance Capital, Essar Oil, Jindal Vijaynagar
(now JSW Steel's predecessor), and Hindustan Petroleum. **In one week in February 1995, 78
companies went public**, capping a fiscal year (1994–95) that saw roughly **1,400 issues** hit
the market; year-on-year primary-market growth in 1995 alone ran at **32%**. This was the
capital that funded India's first wave of greenfield private-sector steel, textile, and
petrochemical capacity — the boom's real-economy content, distinct from a pure financial mania,
is that the equity actually financed physical plant that came onstream over the following
several years, exactly the capacity the 1997–98 commodity collapse then found itself competing
to sell into.

**The turn.** The boom halted with the July 1997 Asian financial crisis (the desk's own Asian
Tigers mirror, case 5 below, is the direct contagion source). India's own growth decelerated
from 7.8% (1996–97) to **4.8% in 1997–98**, recovering only partially to 6.5% the following
year; the rupee depreciated **13.1% between April and September 1998** as the crisis's regional
currency pressure reached India even though India's own trade exposure to Asia was modest (Asia-
directed exports were under 2% of GDP `[source: IMF ADBI working paper]`). Global commodity
prices — steel, petrochemicals, textiles chief among them — fell sharply through 1997–98,
directly compressing the revenues of the plants the 1994–96 equity wave had just built; a
precise, sourced capacity-utilization series for Indian steel/petrochem/textiles in this specific
window could not be independently confirmed this pass and is flagged `[VERIFY: sector-level
utilization data 1997–2001 — pre-OBICUS era, likely only recoverable from CII/FICCI/industry-
association archives or contemporary RBI Annual Reports, not a modern online database]` — this
is precisely the §B1 measurement gap in its starkest form: the boom whose bust this desk most
wants a utilization number for is the one era with no free, machine-readable series at all. The
Annual Survey of Industries (ASI, MOSPI) does run continuously back through this period and in
principle carries sector-level output and capacity data, but ASI's own multi-year publication lag
and its unit of observation (registered factories, not a use-based capacity-utilization percentage
comparable to OBICUS) make it a poor substitute for a real-time cycle read even after the fact;
contemporary industry-association commentary (CII, FICCI) from 1997–2001 is qualitatively
consistent with widespread steel/textile/petrochemical overcapacity but was not aggregated into
any single, citable, free index this pass could locate. The honest conclusion for the data phase:
**case 1 can be dated and sized on its financial side (equity issuance, GNPA) but not on its
real-capacity side** — any future purged backtest that tries to condition L11 on a full,
uniformly-measured 1994–2020+ history should expect its effective sample to begin no earlier than
MOSPI's IIP capital-goods series (itself base-year-spliced) or, cleanly, OBICUS in 2008 — meaning
roughly the first decade of this four-episode case record sits outside what any India-only L11
backtest could actually condition on, reinforcing why the ladder already treats cross-country
analogue pooling (as in `capex-RESULTS.md`'s IN1–IN3) as the only route to a Tier-B graduation.

**The NPA overhang, verified.** The banking system's own aggregate is the best-measured proxy
for the bust's severity. Total gross NPAs across the banking sector stood at **₹34,428 crore, or
roughly 14.4% of gross advances, in 1998**; GNPA growth ran at roughly 11% in 1999 before turning
negative after 2002. For nationalised banks specifically, the GNPA ratio fell from **19.05%
(1997) to 12.16% (2001)** — a genuine, multi-year improvement, but one that itself confirms how
extreme the starting point was: a system-wide NPA ratio in the high teens is the direct legacy of
the 1994–97 lending-and-equity boom meeting the 1997–98 commodity bust, still being worked off
five years later.

**CDR, born 2001.** The RBI's Corporate Debt Restructuring mechanism — the desk's first
institutional answer to exactly this kind of overhang — was formally issued via detailed
guidelines on **23 August 2001**: a voluntary, non-statutory, three-tier structure (CDR Standing
Forum, CDR Empowered Group, CDR Cell) built explicitly on the UK/Thailand/Korea/Malaysia
precedent, binding a minimum ₹100 million exposure once creditors representing 75% of value
agreed. CDR is the direct institutional ancestor of the SDR/5:25/S4A "alphabet" case 3 below
documents in more detail for the next cycle's bust — the mechanism type (restructure-in-place
rather than liquidate) recurs across both India busts even as the specific tools evolve.

**SICA/BIFR — the era's actual workout venue, and its weak record.** The Sick Industrial
Companies (Special Provisions) Act, 1985 (SICA) — predating this boom, born of 1980s industrial
sickness on the Tiwari Committee's recommendation — established the Board of Industrial and
Financial Reconstruction (BIFR) as the formal rehabilitation venue that absorbed much of the
1997–2002 overhang. By 2007, BIFR had registered **5,471 references** since inception, of which
**1,337 were recommended for winding up and only 825 revival schemes were ever sanctioned** — a
revival success rate of roughly **12–15%**. Roughly **4,700 cases were referred to BIFR across
its full 1987–2016 life** `[the two counts — 5,471 registered by 2007 vs. ~4,700 total referred
over 1987–2016 — are not fully reconciled by this pass; likely reflects registered-vs-referred
definitional differences; VERIFY]`. SICA was formally repealed effective **1 December 2016** (via
the Sick Industrial Companies Repeal Act, itself dated 2003 but implemented only in 2016) —
meaning the *legal machinery* born to handle the 1994–2002 bust remained the nominal venue for
industrial distress for another 14 years after the crisis it was built for had already passed,
right up until IBC 2016 (case 3 below) replaced it entirely. **L11 lesson.** This is the record's
cleanest demonstration that an India capex bust's *institutional* repair lags its *financial*
repair by a wide margin — GNPA improved from 19% to 12% over 1997–2001, but BIFR kept clearing a
backlog of the same era's sick companies for another decade and a half, a workout-venue lag this
desk should expect to recur (and, per case 3, did recur, in a different institutional form).

### 2. India 2003–2011 — the infra supercycle

**The GFCF/GDP arc — verified directionally, contested precisely.** Multiple sourcing passes
converge on the *shape* — a sustained investment-rate climb from the low-to-mid 20s (% of GDP) in
the early 2000s to a clear multi-year peak around 2007–08 — but not on one clean number, and the
gap is itself informative in the same way the fincycle monograph's US price-to-income
reconciliation gap was: one widely cited compilation puts GFCF near **27% of GDP by 2007–08**, up
from roughly 10% in the 1980s; a separate practitioner framing places the Manmohan Singh-era
peak closer to **30–35% of GDP**, and RBI's own historical Gross *Capital* Formation series
(which, unlike GFCF, includes inventory change and is therefore structurally higher) is the
likely source of readings nearer **36–38%** for the same peak year `[VERIFY: reconcile GFCF
(excludes inventories) vs. Gross Capital Formation (includes inventories) as the source of this
9–11-point spread — the task's own "~26% FY03 to ~36% FY08" framing sits inside this same
reconciliation gap and should not be read as a single authoritative print until the data phase
pulls the primary MOSPI National Accounts series directly]`. What is not contested: the direction
and the order of magnitude — a rise on the order of **10–15 percentage points of GDP over five
to six years**, among the largest sustained investment-rate accelerations this record documents
for any economy at any point (compare the Asian Tigers' own 30%+ decade below, case 5) — and a
peak concentrated in 2007–08, precisely the year OBICUS itself (once it starts in 2008) opens at
its own all-time high.

**Power — Ultra Mega Power Projects and merchant-power mania.** Of nine originally proposed
4,000 MW-scale UMPPs, **four were actually awarded**: **Mundra** (Gujarat, Tata Power, the first
UMPP commissioned, 4,000 MW), **Sasan** (Madhya Pradesh, handed to Reliance Power **7 August
2007**, 3,960 MW), **Krishnapatnam** (Andhra Pradesh, handed to Reliance Power **29 January
2008**, at a levelised tariff of ₹2.33/kWh), and **Tilaiya** (Jharkhand, handed to Reliance Power
**7 August 2009**, though ultimately never commissioned `[VERIFY: Tilaiya's final status]`). The
five unawarded UMPPs are themselves a data point — a scheme conceived at nine-project scale that
delivered four is the boom's first, quiet capacity-versus-ambition gap, well before the more
famous 2011–20 stalls (case 3). **Coal linkages** were the structural fault line power capacity
kept running into throughout this boom and into the next decade: fuel-supply-agreement
uncertainty for plants built without secured, long-term domestic coal linkage is the direct
through-line from this era's overbuild into case 3's 2011–13 stalls.

**Roads — NHDP, phase by phase.** The National Highways Development Project, launched **1998**
under PM Vajpayee, ran through this boom as India's flagship road-capex program, ultimately
covering **~49,260 km**: Phase I (Golden Quadrilateral, 5,846 km, declared complete as a
four-lane network **January 2012**), Phase II (North-South/East-West corridors, 7,142 km), Phase
III (**approved 12 April 2007**, 12,109 km on a Build-Operate-Transfer basis), Phase IV
(**approved 18 June 2008**, 20,000 km of non-Phase-I/II/III widening), Phase V (6,500 km
six-laning), Phase VI (**approved November 2006**, 1,000 km of expressways), Phase VII
(**approved December 2007**, ring roads/bypasses/flyovers). The clustering of Phase III, IV, VI,
and VII approvals in the 2006–08 window is itself a direct capex-cycle signature — four of seven
NHDP phases were greenlit inside a three-year span sitting exactly at this boom's peak, before
the program was eventually subsumed into Bharatmala around 2018 (spanning case 3's repair
years).

**Telecom — spectrum, administratively priced.** Following India's 2001 spectrum auction, the
government abandoned auction-based allocation in favor of **administrative allocation at fixed,
un-escalated prices**; in 2008, **122 new 2G licenses** were issued first-come-first-served at
**2001-era prices**, which the Comptroller and Auditor General later estimated cost the exchequer
on the order of **$40 billion** in foregone revenue (a separate estimate puts the associated
investment outflow at **₹2,90,000 crore, roughly $47 billion**) `[figures per CAG audit and
contemporary reporting; the precise reconciliation between the "$40bn exchequer loss" and
"₹2.9 lakh crore investment outflow" framings is not attempted here — VERIFY if the distinction
matters for a future dossier]`. This is a capex-*adjacent* rather than capex-proper episode — the
spectrum scandal is fundamentally a rent-allocation story, not an investment-rate one — but it
belongs in this chronology because the underpriced spectrum directly subsidized the huge
build-out of GSM network capacity (towers, base stations, backhaul) that *was* real capex, timed
squarely inside this same 2003–2011 window.

**SEZs — the land-mania leg.** Special Economic Zones approvals concentrated almost entirely in
this window: **235 SEZs formally approved in 2006** alone; of the **54 notified in 2006**, 51
were operational; of **96 notified in 2007**, 75 were operational; by **December 2008, 181
notified SEZs existed for IT alone**, 66% of the total SEZ count at that date. The UPA government
eventually cleared **576 SEZs covering 60,375 hectares**, of which **392 (45,636 hectares) were
formally notified by March 2014** — meaning even the *approval* pipeline (as distinct from actual
build-out) kept running for years after this boom's peak. The land-acquisition backlash —
**Nandigram, West Bengal, 2007**, the era's most politically consequential single episode — is
the direct institutional-memory link this desk should carry into how it reads any *future*
India land-intensive capex wave: SEZ-scale land acquisition triggered enough political cost that
no comparably aggressive SEZ program has been attempted since.

**The IPO/QIP funding wave and Reliance Power as the top-tick artifact.** The boom's financing
side ran overwhelmingly through public and quasi-public equity — precisely the 1994–97
mechanism recurring at ten times the scale. The single cleanest artifact in this entire case
record is the **Reliance Power IPO**: **₹11,700 crore**, priced at **₹450/share**, opened
**January 2008**, oversubscribed **73×**, for a company that at the time of its IPO had **no
operating assets and no cash flow** — pure greenfield power-capacity promise monetized at the
absolute top of a six-year boom. It listed **11 February 2008**: opened at ₹530 (a 17% premium
to issue), then closed the same day at **₹372** — a loss for day-one allottees before the stock
went on to fall much further over the following years. The date is not incidental: Reliance
Power's IPO closed for subscription within days of the Sensex's own then-all-time closing high
(January 2008) `[VERIFY: exact Sensex peak date and level in January 2008 — recalled as ~21,000
on 8 January 2008 with moderate confidence, not independently re-confirmed this pass]` — the
single most literal "IPO at the top" instance this desk's entire cycle-atlas project has yet
documented, a domestic Indian analogue to what the property monograph's own Ciudad Real airport
and golf-membership-index artifacts do for Spain and Japan respectively.

**Capital-goods order books as the cycle thermometer.** BHEL's own multi-year trajectory tracks
the boom-to-bust arc directly: the stock **peaked during the 2007–08 bull cycle**, then entered a
multi-year decline whose order-book evidence is covered in more detail under case 3 below (BHEL's
order book fell 7.3% YoY to ₹1,46,500 crore by December 2012, with a negative quarterly order
inflow around the same time) — the same capital-goods names that thermometer the boom's peak in
this case thermometer its bust in the next one, a single continuous instrument spanning both
episodes.

**The 2008 interruption and the 2009–11 last leg.** The global financial crisis interrupted, but
did not end, this boom: the Sensex fell **~60–64% between January and October 2008** (figure per
the credit monograph's own case #10, not recomputed here), but fiscal stimulus and continued
infra spending sustained real capex into **2009–11** — the boom's genuine "last leg," visible
most clearly in OBICUS's own opening years: capacity utilization reached an **all-time series
high of 83.2% in March 2011**, the single highest print OBICUS has ever recorded, arriving
*after* the 2008 interruption rather than before it. That print is this Part's cleanest example
of a textbook late-cycle utilization peak: the highest capacity-use reading in the whole 18-year
OBICUS history sits at the exact hinge between this boom and case 3's decade-long drought,
exactly the kind of signal L11's non-positive contribution clamp is designed to act on only in
its *falling* leg, never to chase on its way up.

### 3. India 2011–2020 — the twin-balance-sheet decade

**Framing — cross-referenced, not re-derived.** The credit-side chronology of this decade —
GNPA's masked-then-forced-disclosure arc, the AQR shock, IL&FS, the GNPA peak and trough — is
already fully documented in `research/cycles/credit-deep/partB-cross-country.md`'s own case #10
("India 2003–2018") and in the Economic Survey 2016-17's own Chapter 4, **"The Festering Twin
Balance Sheet Problem"** (already cited in that monograph's references). This Part's job is the
*real-side* record those credit-side numbers sit on top of: what capex, capacity use, and the
capital-goods order pipeline actually did across the nine years the credit monograph's own GNPA
cycle spans "roughly a decade: AQR (2015) → decadal low (2.15%, 2025)."

**2011–13: the stall begins, before AQR even forces recognition.** The proximate trigger long
predates 2015's formal reckoning. Coal-linkage, land-acquisition, and environmental-clearance
bottlenecks — the fault lines case 2's own UMPP and power-sector build-out had already exposed —
seized up broadly: an estimated **$45 billion of investment was held up** by clearance and
land-acquisition bottlenecks; **154 Coal India projects (210 million tonnes of production
potential)** sat awaiting environment/forest clearances, with delays projected to cost roughly
**190 million tonnes of lost output by March 2012**; individual projects stalled visibly and
publicly — the **Nabinagar Super Thermal Power Project (1,980 MW)** halted for 15 days in
February 2012 alone over farmer land disputes. CMIE's own project database — a **paid** source
under this Contract's free-data rule, cited here only via public reporting of its headline
figures — recorded new-project announcements collapsing to a **14-year low**, with roughly
**₹1 lakh crore of new projects launched in one quarter versus ₹4 lakh crore at the start of the
same year**, and new private-sector project announcements falling **62% quarter-on-quarter** at
one point in the decline `[VERIFY: exact reference quarter/year for this specific CMIE-sourced
figure — recovered from a secondary news compilation, not CMIE's primary release]`. Among stalled
projects broadly, **power accounted for 35.4%** and **manufacturing over 29%** — the two sectors
this Part's case 2 identifies as the boom's own two largest legs are also its two largest stall
categories, a direct overbuild-to-stall mapping.

**The restructuring alphabet, 2001→2016.** CDR (born 2001, case 1 above) proved insufficient for
this decade's scale; three further RBI mechanisms followed in quick, escalating succession:

| Mechanism | Date | Core feature |
|---|---|---|
| **CDR** (Corporate Debt Restructuring) | Guidelines 23 Aug 2001 | Voluntary, non-statutory; 75%-by-value creditor vote binds all; three-tier structure |
| **5:25 scheme** | Dec 2014 | Infra/core-sector loans >₹500 cr; tenor extendable to 25 years, refinanced every 5 years |
| **SDR** (Strategic Debt Restructuring) | 8 Jun 2015 | Lenders convert debt (incl. unpaid interest) into ≥51% equity; must sell ≥26% to a new promoter with right of first refusal |
| **S4A** (Scheme for Sustainable Structuring of Stressed Assets) | 13 Jun 2016 | Debt bifurcated into "sustainable" (≥50% of exposure, serviceable from current cash flow) and "unsustainable" (converted to optionally convertible debentures) |
| **IBC** (Insolvency and Bankruptcy Code) | Enacted 2016 | Time-bound (originally 180+90 day) resolution or liquidation via NCLT, replacing SICA/BIFR entirely |

Each successive mechanism tried to buy the restructured borrower more time or more creditor
control without forcing recognition or a change of control — and each was judged, within one to
three years, to have been insufficiently forceful, which is precisely why the sequence escalated
to statutory liquidation-backed resolution (IBC) rather than stopping at any earlier station.

**The AQR recognition shock, August 2015, and the RBI circular that followed.** Cross-referencing
the credit monograph directly: the AQR forced banks to reclassify previously obscured stressed
loans, a **measurement break, not a fresh credit event** (that monograph's own words). On top of
IBC, RBI issued a further circular on **12 February 2018** mandating banks to refer any account
with exposure over **₹2,000 crore** to IBC if unresolved within 180 days of default — a blanket,
size-triggered rule with no case-by-case discretion. The Supreme Court struck this circular down
as **ultra vires** the Banking Regulation Act in ***Dharani Sugars and Chemicals Ltd. v. Union of
India***, decided **2 April 2019** — RBI's Section 35AA power, the Court held, did not extend to
issuing directions for *all* cases without considering specific defaults; every action taken
under the circular, including Section 7 IBC applications already filed, was declared **non-est**.
**L11/credit-interface lesson.** A blanket administrative resolution mandate — the same
instinct behind Japan's 1990 MOF quantity controls and China's 2020 "three red lines" (see case 7
below and the fincycle monograph's own China case) — was tried in India too, and was the one
tool in this entire cross-country record to be **judicially invalidated** rather than merely
phased out or superseded; the desk should read India's institutional capacity to check its own
regulator, even mid-crisis, as a structural feature distinguishing this repair from several of
the mirror cases.

**The 12 large accounts, the second list, and the steel-vs-power resolution gap.** RBI directed
lenders on **13 June 2017** to refer a first list of **12 large stressed accounts** — Essar Steel, Bhushan
Steel, Electrosteel Steels, Amtek Auto, Bhushan Power and Steel, Alok Industries, Monnet Ispat,
Lanco Infra, Era Infra, Jaypee Infratech, ABG Shipyard, and Jyoti Structures — together
accounting for roughly **a quarter of the system's then ₹8 trillion of NPAs**. The two steel
resolutions were the record's cleanest successes: **Essar Steel** recovered **92% of ₹49,000
crore** owed, after an 850-day process that went all the way to the Supreme Court, with
ArcelorMittal ultimately taking control from the Ruia family; **Bhushan Power & Steel** recovered
roughly **41% of ₹47,000 crore** owed (₹19,350 crore realized), with JSW Steel completing the
takeover in **March 2021**. **Power's resolution ran on a dramatically longer, still-incomplete
clock.** The Ministry of Power classified **34 coal-based thermal plants (40.1 GW, ₹1.7 trillion
of debt, ~$23bn) as "stressed" in March 2018**; more broadly, roughly **66 GW of conventional
generation capacity** sat under some degree of financial stress (54,805 MW coal across 44
assets, 6,831 MW gas across 9 assets, 4,571 MW hydro across 13 assets). Thirty-four stressed
power projects (~40,000 MW) were expected at insolvency courts as RBI's referral deadline
arrived in August 2018 — yet **as of April 2023, only 26 of those 34 had been resolved fully or
partially, with strategic buyers acquiring just 11** `[VERIFY: precise current 2026 resolution
count — this pass located the April 2023 figure only]`. RBI followed the June 2017 list with a
**second letter to lenders, dated 28 August 2017**, naming **28 further large stressed accounts**
— together roughly **40% of a ~₹4 trillion bad-loan pool** — with a self-resolve deadline of
**13 December 2017** and a hard NCLT-referral deadline of **31 December 2017**; banks ultimately
referred **23 of the 28** to insolvency proceedings once the deadline passed. The two-list
structure (12, then 28 — 40 large accounts in total across roughly six months) is itself a data
point on how the regulator's own confidence in voluntary restructuring (CDR/SDR/5:25/S4A) had
collapsed by late 2017: a mechanism list that had taken **sixteen years to build** (2001→2016,
the table above) was, within eighteen months of IBC's enactment, effectively set aside in favor
of time-bound statutory referral for the system's largest defaulters. Set against Essar Steel's
850-day (2.3-year) full resolution, power's own referral-to-partial-resolution arc already ran past **five
years** for barely three-quarters of the cohort — the single clearest sector-level confirmation
in this whole India record that a capex bust's *physical and regulatory* complexity (tariff
regulation, fuel-linkage disputes, state-discom payment risk — none of which apply to a steel
mill in the same way) governs repair speed independent of the credit-side resolution machinery
available to it.

**IL&FS, September 2018, and the second leg down.** Cross-referencing the credit monograph
directly: IL&FS's default (debt of ₹91,091 crore, ~$13bn) triggered a system-wide NBFC funding
freeze. This Part's own addition, cross-referencing the fincycle monograph's own §B3: by the
mid-2010s NBFCs/HFCs had become **developers' primary — often sole — source of construction and
land finance** (NBFC real-estate exposure ~₹1.65 trillion, 7.5% of the sector's book, as of March
2018), so the September 2018 freeze hit real-estate and infrastructure capex with particular
force precisely because both sectors had grown so dependent on the single channel banks had
already largely exited post-AQR. **DHFL and YES Bank, 2019–20, the crisis's final leg.** DHFL's
own default fed directly into **YES Bank's** subsequent collapse — YES Bank had been a large
DHFL creditor — culminating in the RBI imposing a 30-day moratorium on **5 March 2020**,
superseding the bank's board, capping withdrawals at ₹50,000 per depositor, and drafting the
**"Yes Bank Ltd. Reconstruction Scheme, 2020"** the following day; the State Bank of India
ultimately infused ₹7,250 crore for a 45% stake. YES Bank's stock, which had traded near ₹404 at
its own peak `[VERIFY: exact peak date — one source recalls August 2019, though the more commonly
cited all-time high is August 2018; not reconciled this pass]`, fell to a record low of **₹5.65
in March 2020** — a >98% collapse from peak, and the decade's final, and in equity terms most
violent, single credit event before COVID arrived days later.

**Nine years of repair — the measured India instance of IN2's claim.** `capex-RESULTS.md`'s own
pre-registered IN2 trial (18-country JST panel, capacity-state "regaining its peak") finds a
**median repair length of 4 years**, passing its own pre-set bar (median ≥4y) "exactly at the
bar," with a wide IQR of 1–12 years across 195 peak spells. India's own 2011–2020 episode — nine
years from the 2011 GFCF/OBICUS peak to what most measures treat as the decade's real trough —
sits toward the **long end** of that pooled distribution, not at its median: a genuinely severe,
not merely typical, repair by the panel's own cross-country yardstick, consistent with IN2's own
note that the median is itself pulled down by "many iy peaks [that] are shallow local maxima, not
overbuilds" — 2011's OBICUS all-time-high print (case 2 above) was emphatically not a shallow
local maximum.

**What utilization/IIP-capgoods/GFCF actually printed.** OBICUS fell from its **March 2011
all-time high of 83.2%** to a **record low of 47.3% in June 2020** (the COVID trough, not a
"pure" capex-cycle print on its own, but the terminal point of a decade already in decline before
COVID arrived). GFCF/GDP fell from its **~34–35% 2007–08 boom peak** to roughly **28–29% through
the 2011–2020 "capex winter"** `[figures per dossier 08's own recollection-level estimate;
VERIFY against primary MOSPI data before any backtest use]`. IIP capital-goods and capital-goods
order books moved in the same direction across the same window: BHEL's order book fell **7.3%
year-on-year to ₹1,46,500 crore by December 2012**, with a negative quarterly order inflow
(~−₹1,800 crore) around the same date; L&T similarly cut its own FY16 fresh-order growth guidance
from an initial 15% down to 0–5% by December 2015, with FY16 order flow ultimately declining 12%
— a mid-decade order-book air-pocket sitting squarely inside the drought's second half, well
after the AQR shock had already begun forcing recognition, evidence that the real-side repair
lagged even the credit-side recognition event by several further years. **L11 lesson.** Every
free real-side proxy this desk can construct — capacity use, capital-goods orders, the investment
ratio itself — moved in the same direction, for the same nine years, as the credit-side GNPA
cycle the sibling monograph already documents; the two are not independent confirmations of one
underlying process, which is exactly why ladder.yaml's shared macro-credit-block budget (rather
than two additive seats) is the correct design and why L11's own `inputs: [L10_credit_block]`
dependency edge in the DAG is not decorative.

### 4. India 2021–2026 — the public-capex era

**The central capex budget arc, verified.** Union Budget capital expenditure allocations rose
sharply and consistently across this window:

| Fiscal year | Capex (Budget Estimate) | YoY / note |
|---|---|---|
| FY21 | ₹4.12 lakh crore | pre-PLI baseline |
| FY22 | ₹5.54 lakh crore | +34% |
| FY23 | ₹7.5 lakh crore | +35% |
| FY24 | ₹10.0 lakh crore | +39% |
| FY25 | ₹11.11 lakh crore (BE); ₹10.18 lakh crore (RE) | RE well below BE — the first visible execution gap |
| FY26 | ₹11.21 lakh crore | **only +0.9% vs. FY25 RE — a sharp deceleration** |
| FY27 | ₹12.21 lakh crore | +9% |

The **FY22–FY27 CAGR is ~19.4%**, and capex/GDP sits near **3.1%** by FY27 (BE) — but the FY25
RE-vs-BE shortfall and FY26's near-flat sequential growth are the arc's own honest caveat: the
public-capex engine that drove the first four years of this episode was already decelerating
before the private-capex-revival debate (below) had even resolved itself.

**PLI, verified.** Production-Linked Incentive schemes across **14 sectors** carry a combined
outlay of **₹1.97 lakh crore** (~$26bn) `[one PIB release cites ₹1.91 lakh crore for essentially
the same 14-sector count — the two-figure spread is not reconciled this pass, VERIFY]`. By
March 2024, **755 applications had been approved**, with **₹1.23 lakh crore of investment
attracted**; by December 2025, the cumulative count had grown to **836 applications approved**,
**over ₹2.16 lakh crore of cumulative investment**, **over ₹20.41 lakh crore of cumulative
sales**, **over ₹8.3 lakh crore of cumulative exports**, and **more than 14.39 lakh direct and
indirect jobs**. PLI is this episode's clearest example of *directed* private capex — incentive-
contingent, sector-targeted, and (unlike the 2003–11 boom's IPO-financed greenfield building)
explicitly manufacturing-export-oriented from inception.

**Corporate deleveraging, completed before this episode began, not during it.** The listed-
corporate debt/equity ratio fell from **0.73 (FY20) to 0.59 (FY21)** — "the lowest in six years"
— with roughly **750 companies reducing gross debt by a combined ₹3 trillion in FY21 alone**.
Net debt-equity had, in fact, already improved for **three consecutive years by FY18**,
meaning the deleveraging cycle this episode's private-capex-revival debate depends on had been
running for the better part of a decade before 2021, not as a response to it — a sequencing
point directly relevant to how much of 2021+'s capex should be read as balance-sheet-enabled
rather than newly demand-driven.

**Bank balance sheets cleaned, verified with a precise trend.** Gross NPA for scheduled
commercial banks has fallen for **six consecutive years** since its 2017–18 peak of 11.2%: **2.8%
by March 2024** (RBI Financial Stability Report), **2.6% for 37 SCBs by September 2024**, and a
**historic low of 2.15% (domestic operations) by September 2025** — explicitly lower than the
system's own 2010–11 level, i.e. below the level that prevailed even before case 2's own boom
had finished building the assets that eventually soured into case 3's crisis.

**The "private capex revival" debate, year by year, with the tension made explicit.** Private
capex rose sharply on one widely cited measure — **+67% year-on-year to ₹7.7 lakh crore**
(manufacturing ₹3.8 lakh crore, roughly half, led by metals/autos/chemicals; services ₹3.1 lakh
crore, led by trading/communications/IT) — described in contemporary coverage as "the strongest
investment revival in over a decade." Aggregate capex reported by **1,899 listed non-financial
companies grew 11% to ₹9.4 trillion in FY25**. Set directly against that: CMIE recorded
**₹14.3 lakh crore of project withdrawals in a single quarter in late 2025** — a reminder,
in the credit monograph's own house idiom, that "the boardroom can say 'approved' while the
construction site is still waiting for the bulldozer." L&T's own chairman stated in August 2025
that private capex is now "substantial" in the company's order book, the same capital-goods-
order-book thermometer cases 2 and 3 already establish as this record's most reliable
real-time gauge — but a single large contractor's order book is not, on its own, a system-wide
private-capex confirmation. **OBICUS, the free arbiter, sits right at the practitioner
threshold this desk's own dossier already flags as a magic-number trap:** **76.8% (Q4 FY24,
March 2024)**, **77.7% (Q4 FY25, up from 75.4% the prior quarter)**, **75.6% (Q3 FY26, December
2025, up from 74.3% in September 2025)** — a series oscillating in the mid-to-high 70s for two
full years, consistent with the "~75%" heuristic threshold at which practitioners claim fresh
private capex "switches on," but doing so as a *level*, not a *trend break* — exactly why
CONTRACT §6 and dossier 08 both insist on the *percentile rank* of this series as the correct
construction, never the fixed 75% number itself.

**Real-estate and power-demand upcycle.** The residential-property side of this episode is fully
covered in the fincycle monograph's own §B3 ("The 2021–2026 upcycle": record 302,867 unit sales
in 2024, the luxury/affordable divergence, RERA/GST as the structural reset) and is not
re-derived here. This Part's own free-standing addition is the power-demand side: India's peak
electricity load rose from **148 GW (2014) to 250 GW (2024), a 68% increase**, then to an
**all-time high of ~256 GW**, surpassing the prior 250 GW record set 30 May 2024. Air-conditioning
is the single largest marginal driver — **14 million AC units sold in 2024, up 27% from 11
million in 2023** — with cooling load estimated at **~60 GW of the 2024 peak**, projected toward
**one-third of total peak load by 2030**. Rising power demand is this episode's most demand-side-
driven capex trigger (as distinct from PLI's supply-side, incentive-driven capex), and the two
sit uneasily on the same "is this a real supercycle" question the next paragraph makes explicit.

**The honest open question, and why L11's clamp means the desk need not resolve it.** Is
2021+ arc #3 — a genuine repeat of case 2's investment-rate supercycle — or a public-spending
plateau that has not yet, and may never, hand off cleanly to broad-based private capex? The
evidence that would distinguish the two: (i) GFCF/GDP durably re-crossing back toward the
~34–36% 2007–08 peak rather than plateauing in the 31–33% range dossier 08 already estimates
for 2022–23 onward; (ii) OBICUS's percentile rank, not its level, breaking cleanly into its own
historical top quartile rather than oscillating near a round-number heuristic; (iii) private
capex broadening past PLI-eligible and large-conglomerate order books into the CMIE-tracked
project-announcement base *net* of the withdrawal rate already documented above; (iv) whether the
FY26 budget's near-flat capex growth (+0.9%) is a one-year pause or the start of the public-
spending engine's own rolloff without a private handoff underneath it. **The desk does not need
to answer this before the model can be built.** `capex-RESULTS.md`'s own IN3 trial found that a
hot capex state does not order forward five-year returns monotonically at all — the top-quintile
capex-state country-years produced *lower* pooled forward returns (+0.242, log) than the
bottom-quintile (+0.287), with the *middle* quintile lowest of the three (+0.202) — precisely
the "weakly informative, never monotonic" signature that ladder.yaml's `contribution_clamp:
non_positive` already encodes: L11 is built to matter only when the capex/utilization state is
extreme and hot, and only ever to *subtract* permission from the shared macro-credit-block
budget in that state, never to *add* on the strength of a plausible-sounding "arc #3" narrative.
Whether 2021+ eventually resolves as a supercycle or a plateau, the clamp guarantees the reading
can never do more than fail to fire — the one design choice in this entire monograph that turns
a genuinely unresolvable forecasting question into a non-issue for portfolio construction.

---

## B3. Three international mirrors — analogue calibration only

### 5. Asian Tigers 1990s — the overinvestment-plus-currency-mismatch benchmark

**The boom.** Domestic saving and investment rates in Thailand, Indonesia, Korea, and Malaysia
averaged **more than 30% of GDP across 1986–1996** (Radelet-Sachs), with the task's own framing
of "35–40%+" for individual peak years/countries consistent with, though not independently
re-derived to decimal precision by, this search pass `[VERIFY: country-by-country World Bank GFCF
series for the precise 1996 peaks by country]`. Crucially, unlike either of India's own booms
(cases 1 and 2, funded overwhelmingly in domestic-currency bank credit and domestic equity), a
large share of this investment was financed through **short-term, unhedged foreign-currency
debt** — the structural fault line India's own capex cycles have never carried at comparable
scale.

**The 1997 crisis.** The Thai baht floated **2 July 1997**, triggering contagion across Indonesia,
Korea, and Malaysia; **net private capital flows to the five crisis economies reversed by roughly
$105 billion between mid-1997 and early 1998 — about 10% of their combined GDP** (Radelet-Sachs,
independently verified this pass). Korea's IMF-led rescue was agreed **3 December 1997** at
**$58–58.4 billion** of standby financing (IMF plus World Bank, Asian Development Bank, and
bilateral creditors) — **the largest IMF rescue package in history at the time**, conditioned on
fiscal and financial austerity, high interest rates, chaebol-group dissolution/restructuring,
layoffs, and a floating exchange-rate regime; Indonesia's crisis compounded into a political
crisis (President Suharto's resignation, May 1998), the one instance in this entire cross-country
record where a capex/credit bust directly precipitated a head-of-state's fall.

**The Young/Krugman TFP debate, in one paragraph.** Paul Krugman's 1994 "The Myth of the Asian
Miracle" argued — building directly on Alwyn Young's earlier empirical growth-accounting work —
that East Asian growth had been overwhelmingly **input-driven** (capital and labor accumulation)
rather than productivity-driven, an explicit echo of the Soviet growth experience. Young's own
estimates, independently verified this pass: total factor productivity growth of **2.3%/year
(Hong Kong), −0.3%/year (Singapore), 1.6%/year (Korea), and 1.9%/year (Taiwan)** — modest to
negative TFP contributions underneath headline growth rates of 6–9%/year. The debate matters to
L11 directly: it is the strongest available academic argument that a *sustained, high investment
rate alone* — exactly the metric case 2's own GFCF/GDP arc tracks for India — is not, by itself,
evidence of durable, self-sustaining growth; capital can be accumulated well past the point
where its marginal product still justifies the accumulation, and the 1997 crisis is the
mechanism by which that overhang was eventually forced into the open.

**Repair lengths.** Korea's macro recovery was comparatively fast — a return to growth by 1999
`[VERIFY: precise 1999 GDP growth print]` — but banking-sector NPA cleanup and corporate
restructuring (the *chaebol* debt-equity unwind specifically) ran considerably longer, on the
order of **5–7 years** `[VERIFY]`. Thailand and especially Indonesia repaired more slowly, with
Indonesia's political transition adding a further, non-economic repair dimension no other case
in this record carries. **L11 lesson.** The mirror's clearest contribution is *negative*: it
argues for why none of India's own three completed booms produced an Asian-crisis-style
currency-collapse leg — India's capex has been financed in domestic-currency bank credit and
domestic equity throughout, never at the short-term unhedged FX-debt scale this mirror's crisis
mechanism required. This is a structural difference in funding channel, not evidence that Indian
capex busts are milder — cases 1 and 3 show they are not — only that they resolve through a
different, slower, domestic-currency-denominated channel (CDR/SICA/IBC) rather than a fast,
currency-triggered one.

### 6. China 2009–2015 — the state-directed capex wave and what it does differently

**The stimulus.** Premier Wen Jiabao's government announced a **RMB 4 trillion (~$585 billion)
stimulus program in November 2008**, explicitly targeting 8% GDP growth for 2009; **81% (RMB
3.25 trillion) went to infrastructure**, consuming enormous quantities of steel, nonferrous
metals, and cement. The financing channel was **state-directed bank lending and local-government
financing vehicles (LGFVs)**, not market capital — the single largest structural difference from
every case in this record so far: local-government debt rose from **RMB 5.6 trillion (2008) to
RMB 10.7 trillion (2012)**.

**SOE overcapacity, precisely measured by 2015.** By 2015, six industries were operating under
severe overcapacity: **steel at 67% utilization, coal at 64.9%, cement at 73.8%, flat glass at
68.0%, electrolytic aluminum at 75.4%, and shipbuilding at 69%** — steel production alone
exceeded demand by **roughly 200 million tonnes annually** by that year. These utilization
figures sit meaningfully *below* even India's own 2011–2020 "capex winter" OBICUS range
(roughly 65–75%, per dossier 08's own recollection-level figures), a useful cross-check on how
severe an administratively-driven overbuild can get relative to a market-cycle-driven one.

**Supply-side structural reform, 2016–17.** Xi Jinping proposed strengthening "supply-side
structural reform" in 2015, formalized through 2016–17 with five explicit tasks: cut
overcapacity, reduce inventory, deleverage, lower costs, and address weak areas. China cut
**115 million tonnes of steel capacity and over 400 million tonnes of coal capacity across
2016–2017 combined**; 2016 alone accounted for **65 million tonnes of outdated steel capacity**
and **290+ million tonnes of coal capacity**, with **700,000 laid-off workers retrained or
re-employed** the same year. This is the same administrative-mandate tool this Part's case 3
already flags as structurally similar to the (judicially invalidated) RBI Feb-2018 circular and
to Japan's 1990 MOF quantity controls (fincycle monograph) — and, later, to China's own 2020
"three red lines" property-sector deleveraging mandate (also fincycle monograph) — a recurring
pattern of governments reaching for direct capacity/lending caps once market-based signals have
been judged too slow or too politically costly to rely on.

**What a state-directed capex cycle does differently.** Three things distinguish this mirror
sharply from every India case above: (i) the **financing channel** is administratively directed
bank credit and LGFV debt rather than market capital, so market-based early-warning signals
(bond spreads, equity drawdowns, currency pressure) are systematically muted — the same
observation the fincycle monograph's own China property case (§7) makes for the 2021+ real-estate
unwind; (ii) the **capacity-cut response** is itself administratively mandated on a multi-year
government-plan timetable rather than a market-clearing bankruptcy/restructuring process, so
"repair" here means a *policy-paced* reduction rather than the demand-and-supply-driven repair
this record's other cases document; (iii) precisely because of (i) and (ii), China supplies **no
usable analogue for L11's own construction** (OBICUS/IIP-capgoods/GFCF are all market-economy
capacity-signal proxies with no reliable Chinese equivalent this desk can access free) — China's
relevance to this book runs entirely through the **global financial cycle / China credit impulse
channel (L9, candidate H54)**, never through L11 itself.

### 7. US shale 2010–2020 — the fastest private capex cycle on record

**The boom and its first bust, 2010–2016.** US shale capital spending accelerated sharply from
2010, peaking in **2014**; as oil prices fell from **$93/barrel (2014) to $43/barrel (2016)**,
the industry slashed capex just as sharply, with **nearly 300 shale-focused companies filing for
bankruptcy from 2016 onward**. The underlying business-model problem, stated plainly in
contemporary industry commentary: operators were spending roughly **two dollars for every dollar
of cash brought in**, prioritizing production growth over free cash flow — precisely the
overinvestment dynamic this record's other cases (Asian Tigers, China) also document, but
compressed here into a **two-year bust** rather than a multi-year one.

**The 2020 collapse, the sharpest single-year capex contraction in this record.** COVID demand
destruction drove the US oil-rig count from **847 rigs (July 2019) to 225 (July 2020) — an 85%
collapse — bottoming at 172 rigs in August 2020**. Oil prices fell from **$60/barrel (December
2019) to $17/barrel (April 2020)**, briefly trading **negative** on the futures market the same
month. US crude production fell from a peak of nearly **13 million barrels/day (November 2019)**
to average **11.3 million b/d across 2020**. Shale operators reinvested **less than 50% of cash
flow into new drilling in 2020** — an explicit shift into "maintenance capex" mode.

**Capital discipline, 2021+.** Rather than re-accelerating capex once prices recovered, the
industry structurally shifted toward maximizing free cash flow over production growth: **global
upstream oil-and-gas capex reached only ~$514 billion in 2022** — despite the demand recovery and
the Russia-Ukraine war's energy-price shock — **still roughly $70 billion below the 2011 peak**,
the clearest evidence in this entire monograph that a capital-markets-enforced discipline regime,
once adopted, can persist through a subsequent price upcycle rather than reverting to the old
growth-at-all-costs pattern.

**Why repair was fast, and why that speed does not transfer to India.** Three structural features
distinguish shale from every case above and explain the gap between its ~12–18-month repair
cadence and India's own multi-year-to-decade one: (i) **asset short-cyclicality** — a shale well's
production decline curve is steep (front-loaded output, rapid payback, typically well under two
years), so a capex cut translates into a supply response within quarters, not years, unlike a
UMPP-scale power plant or a multi-hundred-kilometre highway corridor with a multi-year
construction gestation regardless of financing availability; (ii) **no land-acquisition,
environmental-clearance, or fuel-linkage gestation lag comparable to Indian infrastructure** —
US shale drilling permits and private mineral-rights leasing move on a timescale of months, not
the multi-year land/clearance chronology case 3 documents for Indian coal-linked power; (iii)
**market, not administrative, capital discipline** — high-yield bond and public-equity investors
directly repriced growth-over-returns shale operators' cost of capital after 2014–16, forcing
discipline through the price of capital itself, whereas India's captive PSU-bank-dominated
lending system kept extending and restructuring credit (CDR→5:25→SDR→S4A) through most of the
2011–2020 decade without ever forcing an equivalent capital-markets repricing on the borrowers
themselves. **L11 lesson, the mirror's single most important contribution.** L11's own 36–60
month τ½ prior (ladder.yaml) is not a property of "capex cycles" as a category — it is calibrated
specifically to **India's own gestation-heavy asset mix** (power plants, highways, steel mills,
telecom towers), and this mirror proves that mix, not the "capex cycle" label, is what determines
repair speed: a hypothetical short-cycle, low-gestation Indian capex signal (there is none at
scale today) would need a materially shorter τ½ than L11's own India-calibrated prior, and this
desk should never import a shale-style "fast repair" expectation into any India-specific capex
read.

---

## B4. Synthesis

### The table

| Episode | Boom length | Funding channel | Repair length | What L11's three legs would have shown | Verdict, 10–15y/n≈2–3 framing |
|---|---|---|---|---|---|
| **India 1994–97→2002** | ~3y (1994–97 primary-market mania) | Public equity (IPO mania, premium-issue share 1.4%→46%) + bank project finance | ~5y to 2002 (GNPA 19%→12% by 2001); BIFR backlog cleared for another decade-plus | Pre-OBICUS/pre-IIP-2011-base era — **no usable free real-side series exists**; only GFCF/GDP and GNPA proxy the whole episode | Full round trip ≈8y (1994–2002) — **shorter** than the Atlas's 10–15y band, and the desk's own best instrument (OBICUS) cannot see it at all |
| **India 2003–2011** | ~5–6y to the 2007–08 peak, extended to 2011 by the fiscal-stimulus "last leg" | Public/QIP equity (2007 power IPOs, Reliance Power the top-tick), infra project debt, SEZ land, spectrum-subsidized telecom capex | N/A (this *is* the boom leg; 2008 was a 1-year interruption, not the repair) | **OBICUS all-time high 83.2%, March 2011** — the cleanest late-cycle utilization peak this desk has recorded anywhere in the atlas | The record's single cleanest full-amplitude boom — but note it does not cleanly separate from case 3 below; the two together span 2003–2020 |
| **India 2011–2020** | N/A — this episode *is* case 2's repair leg | (repair of case 2's funding) | **9y** (2011 OBICUS/GFCF peak → 2020 COVID trough); IN2's own pooled median is 4y (IQR 1–12y) — India sits toward the long end | OBICUS 83.2%→47.3% (COVID trough); GFCF/GDP ~34–35%→~28–29%; BHEL order book −7.3% YoY by Dec 2012; power-sector resolution still incomplete 5+ years after 2018 referral | The best-measured leg in the whole record — directly validates L11's 36–60mo τ½ as a **floor, not a ceiling** |
| **India 2021–2026** | 5y so far, ongoing, unresolved arc-vs-plateau | Central capex budget (₹4.12→₹11.21 lakh cr, FY21→FY26) + PLI (₹1.97 lakh cr outlay) + reviving private capex on cleaned balance sheets (GNPA 11.2%→2.15%) | N/A — boom phase, outcome undetermined | OBICUS 75–78% band (2024–26), oscillating at the practitioner "switches on" heuristic, not yet breaking to a new percentile regime; GFCF/GDP recovering toward ~31–33%, not yet back to the 34–36% 2007–08 peak | **Genuinely open** — and IN3's own non-monotonic quintile result is exactly why the clamp means the desk does not need to close it |
| **Mirror: Asian Tigers 1990s** | ~10y (1986–96) | Bank-intermediated + **short-term unhedged FX debt** (the fault line India never carried) | Korea macro-fast (~1999 growth resumption); banking/chaebol cleanup slower, ~5–7y `[VERIFY]`; Indonesia slowest, complicated by 1998 political transition | N/A (mirror only) | Argues India's booms never carried the FX-mismatch mechanism that made this crisis fast and currency-driven — a funding-channel difference, not a severity difference |
| **Mirror: China 2009–2015** | ~7y stimulus-fueled (2009–15), arguably to 2021 pre-property-bust | **State-directed bank credit + LGFV debt** — not market capital | Formal SSSR program ~2y (2016–17); underlying overcapacity/debt overhang arguably still unwinding into the 2020s (fincycle monograph's own China property case) | N/A (mirror only; no free market-based Chinese proxy exists for L11's own construction) | Argues capex-cycle repair speed under administrative direction is policy-paced, not market-paced — no transferable τ½ for L11 |
| **Mirror: US shale 2010–2020** | ~4–5y per leg (2010–14; 2017–19), genuinely short-cycle and repeating | High-yield corporate debt + public equity, continuously market-repriced | **~12–18 months per bust** — 2014–16 bust resolved by 2017; 2020 rig-count trough (Aug 2020) to discipline-era normalization by 2021–22 | N/A (mirror only) | The counterexample proving L11's long τ½ is **asset-mix-specific, not category-specific** — short-cycle, low-gestation capital repairs in quarters; India's gestation-heavy mix does not |

### The verdict on the Atlas's own "10–15y; n≈2–3" framing, stated honestly

Tested directly against the four India cases above, the Atlas's own row-1.6 framing survives in
spirit but not at face value. **On "n≈2–3":** the case record supports three named windows
(1994–2002, 2003–2020, 2021+) plus this Part's own addition of an even earlier partial instance —
but only the middle window (2003–2011 boom feeding directly into 2011–2020 repair) is measured
by more than one free real-side proxy across its *entire* length; case 1 predates every one of
this desk's usable capex series, and case 4 is incomplete by definition. On strict clock-test
terms (CONTRACT §4: ≥4 observed complete periods to earn even Tier-B "cycle" status), this record
delivers **at most one fully measured complete cycle** (2003→2020, boom-to-repair) plus two
partial or historically-thin analogues — which is *more conservative* than the Atlas's own n≈2–3,
not less, and directly explains why ladder.yaml already carries L11 at **Tier C**, not Tier B.
**On "10–15y":** the label fits a *single leg* (case 2's boom ran 5–6y; case 3's repair ran 9y,
each individually inside or near the stated band) but badly undercounts a *full* boom-to-repair
cycle measured start-to-finish — 2003 to 2020 is **17 years**, and even a narrower peak-to-peak
reading (OBICUS's own March-2011 high to whatever future print eventually re-tests it) is still
running past a decade and a half with no completed re-test as of this writing. The Atlas's
"10–15y" is best read as describing the *repair* leg alone (case 3's 9 years sits comfortably
inside it, with room to spare against IN2's own pooled 4y median-but-12y-IQR-upper-tail), not the
full cycle — and this Part recommends the next revision of `docs/CYCLE_ATLAS.md` row 1.6 make
that distinction explicit rather than quoting one span number for two different things. None of
this changes L11's design: a Tier-C, reduce-only, non-positive-clamped seat inside the shared
macro-credit-block budget was already the correct construction before this case record was
written, and every case above — the pre-OBICUS blind spot in case 1, the textbook late-cycle
peak in case 2, the nine-year repair in case 3, the unresolved arc-vs-plateau question in case 4,
and all three mirrors' confirmation that repair speed is asset-mix-specific rather than
category-specific — argues for keeping it exactly where it already sits, never for promoting it.

---

## References

RBI, Corporate Debt Restructuring (CDR) Mechanism guidelines, 23 August 2001. · Sick Industrial
Companies (Special Provisions) Act, 1985; BIFR registration/resolution statistics (various
compilations). · National Highways Authority of India, *About NHDP*; PIB releases on NHDP phase
approvals (2006–2008). · Government of India, Ministry of Power, *Ultra Mega Power Projects*
status notes; Central Electricity Authority, UMPP status reports. · Reliance Power Ltd., IPO
prospectus and listing-day trading data (11 February 2008); contemporary financial press (Forbes,
Bloomberg, Moneylife) on the IPO and its listing crash. · SEZ India (Ministry of Commerce and
Industry), Board of Approval agenda documents; ISID working papers on SEZ location and land
utilisation. · RBI, Strategic Debt Restructuring Scheme circular (8 June 2015); RBI, 5:25 scheme
circular (December 2014); RBI, Scheme for Sustainable Structuring of Stressed Assets (S4A)
circular (13 June 2016); RBI circular RBI/2017-18/131 (12 February 2018) and *Dharani Sugars and
Chemicals Ltd. v. Union of India* (Supreme Court of India, 2 April 2019). · Insolvency and
Bankruptcy Code, 2016; IBBI media coverage on the 12-large-accounts cohort and Essar
Steel/Bhushan Power & Steel resolutions. · Ministry of Power stressed-asset classification (March
2018); IEEFA, *NPAs in the Indian power sector and strategies for resolving them*. · RBI,
*Financial Stability Report* (various issues, GNPA trend); PIB press release on GNPA reaching
2.15% (September 2025). · RBI, Order Books, Inventories and Capacity Utilisation Survey (OBICUS),
quarterly since 2008; CEIC/Mirrority OBICUS series compilations. · Union Budget documents, FY21–
FY27 (capital expenditure allocations); PIB and IBEF coverage of PLI scheme outlays and cumulative
performance. · CMIE, CapEx database (paid source; cited only via secondary public reporting of
specific figures, each flagged). · Radelet & Sachs (1998), "The East Asian Financial Crisis:
Diagnosis, Remedies, Prospects," *Brookings Papers on Economic Activity*. · Krugman, P. (1994),
"The Myth of the Asian Miracle," *Foreign Affairs*; Young, A., underlying TFP growth-accounting
estimates (Hong Kong, Singapore, Korea, Taiwan). · Government of China, State Council reports on
the 2008–09 stimulus and 2016–17 supply-side structural reform; IMF Working Paper 18/216, "China's
Capacity Reduction Reform and Its Impact on Producer Prices." · Dallas Fed, *Oil and gas industry
shows discipline on capex, but risks remain* (2025); World Bank, *What triggered the oil price
plunge of 2014–2016*; contemporary reporting on the April 2020 negative-oil-price episode and the
2020 US shale rig-count collapse. · `research/CONTRACT.md`; `docs/CYCLE_ATLAS.md` row 1.6;
`config/ladder.yaml` (`L11_capex_cycle` entry); `research/dossiers/08-india-mid-cycles.md`
(house style; free-data-triad framing; CMIE paid-source flag); `research/cycles/capex-deep/
capex-RESULTS.md` (IN1–IN3 pre-registered analogue trials, cited directly throughout);
`research/cycles/credit-deep/partB-cross-country.md` (case #10, India 2003–2018 — credit-side
mechanics cross-referenced, never duplicated); `research/cycles/fincycle-deep/partB-cases.md`
(§B3, India's property-cycle record — cross-referenced, never duplicated; house style for this
series).

---

# PART B-RESULTS — Analogue data: JST R6 (IN1–IN3, pre-registered)

# Atlas 1.6 — capex cycle (L11): analogue results, JST R6 (IN1-IN3, pre-registered)

India official series are proxy-blocked here; per the atlas's own 'C→B via analogues'
clause these trials run on the 18-country JST iy panel + vaulted real equity returns.
Bars pre-registered; interpretation AFTER the print.

## IN1 — capex state → forward 5y real equity return

| Country | corr(state, fwd 5y log real return) |
|---|---|
| AUS | -0.23 |
| BEL | -0.33 |
| CHE | +0.04 |
| DEU | +0.23 |
| DNK | -0.32 |
| ESP | -0.13 |
| FIN | -0.15 |
| FRA | +0.09 |
| GBR | +0.11 |
| ITA | +0.25 |
| JPN | -0.10 |
| NLD | -0.25 |
| NOR | -0.42 |
| SWE | -0.20 |
| USA | +0.08 |

- Sign-consistency: **60% negative** of 15 countries (bar ≥70%): **FAIL**.

## IN2 — post-peak repair length (iy regaining its peak)

- 195 peak spells; median repair **4y** (23 censored spells counted at censoring value, as pre-stated);
  IQR 1-12y.
- Bar (median ≥ 4y): **PASS**.

## IN3 — quintile asymmetry (measurement, prior set — informs the clamp)

- Pooled mean forward-5y log real return: top-quintile capex state **+0.242**,
  middle **+0.202**, bottom-quintile **+0.287** (n = 310/891/305 country-years).

## Honest read (written AFTER the print)

- **IN1 FAILS the sign-consistency bar (9/15 negative), and the failure calibrates the seat.**
  On the project's own scale this sits between demographics (4/16, rejected) and the financial
  cycle (17/17, seated Tier-B): a weak tilt, not a pooled regularity. The analogue panel does
  NOT supply the "C→B via analogues" graduation — L11 STAYS Tier C. No re-run, no bar moved.
- **IN2 PASSES exactly at the bar (median 4y) with a wide honest spread (IQR 1-12y).** The
  repair-takes-years claim holds at the median; the 1y quartile shows many iy peaks are
  shallow local maxima, not overbuilds — which is why the seat keys off PERCENTILE EXTREMES,
  not every wiggle. 23 censored spells counted at censoring value as pre-stated (biases the
  median DOWN, i.e. against the claim — it passed anyway).
- **IN3 is the clamp's vindication, in an unexpected shape.** Top-quintile forward returns
  (+0.242 over 5y, log) sit BELOW bottom-quintile (+0.287) — the mild overbuild penalty —
  but the middle (+0.202) is lowest of all: the state does not ORDER returns monotonically.
  A seat this weakly informative must never ADD regime score; subtract-only at the hot
  extreme, inside the shared budget, is precisely what min(0, ·) implements. The
  consistency-audit's design decision now has the analogue panel's numbers behind it.
- **Net:** seat CONFIRMED at its clamped, Tier-C, reduce-only station; graduation deferred to
  the changes_if clause (purged India backtest on OBICUS/IIP/GFCF once pulled — runsheet).
  The module ships as machinery with the degradation and clamp semantics tested; the evidence
  tier is unchanged by shipping code.

---

# PART C — Data engineering: India's three legs, free

# Part C — Data engineering: measuring India's capex cycle, free (L11)

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)
v1.0 · 2026-09-01

Extends `docs/CYCLE_ATLAS.md` row 1.6 (infrastructure/capex supercycle, "10–15y; n≈2–3 (2003–08,
drought 2011–20, 2021+)... OBICUS utilization percentile, IIP capital goods, GFCF/GDP (post-2026
rebase splice!)... **REGIME (clamped reduce-only)** → L11 inside macro block; **C→B via
analogues**") and `config/ladder.yaml`'s already-seated `L11_capex_cycle` entry (`tier: C`,
`reduce_only: true`, `contribution_clamp: non_positive`, `block: macro_credit_block`,
`inputs: [L10_credit_block]`, `indicator: "RBI OBICUS, MOSPI IIP + GFCF"`). Consumes
`research/CONTRACT.md` §3 (free-source mandate), §4 (Tier-C reduce-only), §6 (no magic numbers),
§8 (Hamilton filter only, never HP), Known Prior #11 (no live network access from this container;
ingestion runs on the principal's machine, every indicator resolves against a committed fixture).
**This Part is the India-official-series data-engineering companion to `research/cycles/capex-deep/
capex-RESULTS.md`** (the JST-panel analogue trials IN1–IN3, already run and reported) — those
results and their interpretation are not restated here; this Part answers a different question
("how does the desk build L11 from India's own free data") and the two meet only at the
`contribution_clamp` design the analogue trials' IN3 already informs (§C.6 inherits that finding,
does not re-derive it). Structure follows `research/cycles/commodity-deep/partC-data.md` (the style
bar this Part matches: per-source sections, exact series names, cadence/lag, break registry,
PIT-hazard table, pipeline, runsheet addendum). **Scope discipline, stated first**: RBI's Sectoral
Deployment of Bank Credit (including its "Industry"/"Infrastructure" sub-lines), WPI, and RBI's
Balance of Payments are built in full elsewhere — `research/cycles/credit-deep/partC-data.md` §C.1/
§C.5 (sectoral deployment), `research/cycles/commodity-deep/partC-data.md` §C.3 (WPI) and §C.4
(BoP) — and are consumed here only as named cross-checks, never rebuilt. Cement (ICI), IIP
Infrastructure/Construction Goods, and finished-steel consumption (JPC) are already vaulted as L12
Tier-C supply-side confirms in `research/cycles/fincycle-deep/partC-data.md` §C.4; this Part points
to that construction rather than duplicating it. Checked by web search this pass (snippet-level,
cross-checked across ≥2 results where feasible; nothing fetched directly, per Known Prior #11).
Anything not so corroborated carries **[VERIFY]**.

---

## C.1 OBICUS — the utilization leg

**What it is.** The Order Books, Inventories and Capacity Utilisation Survey (OBICUS), run by RBI's
Department of Statistics and Information Management (DSIM), is a quarterly survey of manufacturing
companies collecting new orders received, opening/pending order backlog, finished-goods/work-in-
progress/raw-material inventory levels, and item-wise production quantity/value **against installed
capacity** — the last of these is the source of the headline "capacity utilisation" (CU) print RBI
folds into its monetary-policy commentary. Primary confirmed page:
`rbi.org.in/Scripts/QuarterlyPublications.aspx?head=Quarterly+Order+Books,+Inventories+and+Capacity+
Utilisation+Survey` (per-round PDF/press release); the modern DBIE bulk-query path for a queryable
CU time series is `data.rbi.org.in/DBIE/` under Statistics → Surveys — **[VERIFY]** the exact table
name/ID, not independently pinned down this pass (A-catalog's own G9 entry carries the identical
flag; inherited, not resolved here). Third-party aggregators (CEIC) mirror the series but are a
paid service, not the free primary source.

**History.** The survey was launched in **2008** and has run quarterly since; search evidence this
pass (a CU series "averaging 74.6% from Jun 2008 to Dec 2025, 71 observations," and RBI's own
"71st round... Q2:2025-26 (Jul–Sep 2025)" framing) is internally consistent with a **Q1 2008-09
(Apr–Jun 2008) launch** — 70 quarters between round 1 and round 71 is 17.5 years, which lands
almost exactly on Q2 FY2025-26. **[VERIFY]** the exact first reference quarter; the task brief's
own "Q1 2008-09" figure is consistent with, but not independently confirmed against, a primary RBI
statement this pass.

**Sample and the response-rate caveat.** RBI's own survey description covers **over 2,500** public
and private manufacturing companies in the sampling frame [VERIFY — search-derived, not confirmed
against a primary RBI methodology note this pass]. The desk's own working figure of **~750
responding companies** per round (per the task brief, tracing to the Atlas's own citation) is best
read as the *responding* panel, not the frame — a large gap between frame and response is exactly
what a voluntary survey produces, and it matters for more than sample-size arithmetic: **response is
almost certainly not missing at random**. A firm mid-distress is a worse responder than a firm
mid-boom, so a downturn quarter's CU print plausibly carries a mild *upward* self-selection bias at
precisely the moment the state variable most needs to read low — a caveat to log against the state,
not something a percentile transform fixes. **[VERIFY]** the exact current per-round responding N;
RBI's own round announcements do not always headline it.

**Seasonality — the Q4 spike, unadjusted.** OBICUS is published **not seasonally adjusted**. India's
fiscal Q4 (Jan–Mar) carries a well-known mechanical order-book/utilisation push — year-end capital-
budget spending, dealer/distributor stocking ahead of the fiscal close, and calendar-quarter demand
patterns in several manufacturing sub-sectors — so a naive quarter-over-quarter CU comparison is
contaminated by *which fiscal quarter* a reading falls in, not only by genuine cycle position.
**[VERIFY]** the exact magnitude of the Q4 effect; not independently quantified this pass, but its
existence is widely enough referenced in Indian macro commentary that the construction rule below
(§C.6) treats it as a design requirement, not a hypothesis to re-test. This is precisely the sort of
break a fixed threshold would launder silently — another argument, alongside Contract §6's general
rule, for ranking the series rather than reading any single quarter's level.

**Level vs. percentile — is 75% "high"?** The most recent reported reading this pass is **75.6%
(quarter ending Dec 2025)**, against a **2008–2025 historical average of ~74.6%** [VERIFY, both
figures search-derived, CEIC-mirror confidence]. Read as a level, 75% sounds high in absolute terms
— "three-quarters of installed capacity in use" — but read against the series' *own* history it sits
barely above the long-run mean, nowhere near either tail. This is the Atlas's own point stated in
data: **"high" is a percentile statement, never a level statement**, and it is the direct,
concrete argument for why L11's OBICUS leg must be built as an `expanding_percentile` rank (§C.6),
never compared to a fixed CU threshold (a "75% = overheating" rule would be exactly the kind of
magic number Contract §6 bans, and this single data point shows why: 75% is unremarkable against
2008–2025 history).

**Publication lag.** ~1 quarter after the reference quarter, timed to land alongside — and feed
into the commentary of — RBI's Monetary Policy Committee resolutions; OBICUS results are routinely
cited in the MPC's own "state of the economy" framing. This is a genuine construction convenience
(the release calendar is public and stable) but also a genuine construction hazard: an OBICUS print
released the same week as an MPC decision can be hard to disentangle, in press coverage, from the
MPC's own framing of it — the raw survey numbers, not RBI's narrative gloss on them, are what §C.6's
pipeline consumes.

---

## C.2 IIP capital goods + related use-based legs

**Source and structure.** MoSPI's Index of Industrial Production (IIP), current base **2011-12**
(launched **2017-05-12**, per the search-confirmed MoSPI IIP manual), classifies output by
**use-based category**: Primary Goods (**34.05%** weight), Capital Goods (**8.22%**), Intermediate
Goods (17.22%), Infrastructure/Construction Goods (**12.34%**), and Consumer Goods split into
durables (~12.84%) and non-durables (~12.83%) [VERIFY exact current-base weights; search-derived,
order-of-magnitude confidence, not independently reconciled against a primary MoSPI weight table
this pass]. Infrastructure/Construction Goods was **added as a distinct use-based category from the
2011-12 base** (the earlier 2004-05-base series did not carry it as a separate head) — Atlas 1.6's
own parenthetical ("added in 2011-12 base") is confirmed by this base-year structure, not merely
asserted. Portal: `esankhyiki.mospi.gov.in/macroindicators?product=iip` (confirmed live path per
A-catalog H3) and `mospi.gov.in/iip`.

**Base-year history and the live 2026 break.** IIP's base year has been revised repeatedly — 1946,
1951, 1956, 1960, 1970, 1980-81, **1993-94** (introduced 1998-05-27, 543 items), **2004-05** (682
items, broader coverage including mobile phones), **2011-12** (launched 2017-05-12) — a revision
roughly every 5–7 years by design (UNSD recommends every five). **The next break is not "coming" —
it has already happened**: MoSPI's new IIP series, **base year 2022-23**, became effective from the
**2026-06-01** release (per PIB's own "FIRST PRESS RELEASE OF ALL INDIA INDEX OF INDUSTRIAL
PRODUCTION OF NEW SERIES WITH BASE YEAR 2022-23," and MoSPI's own May-2026 embargo advisory), i.e.
**three months before this chapter's own writing date**. Atlas 1.6's "post-2026 rebase splice!"
flag is therefore live *now*, not a future risk to plan for: any capital-goods or infra/construction
series a builder pulls today already needs the **base-2011-12 (legacy) and base-2022-23 (new) series
kept distinct**, spliced by the same ratio-at-overlap discipline this program uses everywhere else
(never fit a trend through the break) — [VERIFY] the exact overlap window MoSPI's new release
exposes for a clean splice point. **[VERIFY]** whether the new base changed the use-based category
weights materially (a rebase this large plausibly does) — not independently confirmed this pass.

**Capital goods' notorious volatility.** MoSPI's own IIP manual documents a structural reason
capital-goods prints swing hard month to month: many capital-goods items have production spans
**longer than one month**, so the series captures them on a **"work-in-progress" basis** specifically
to manage this — an acknowledgment, in the methodology itself, that capital goods is a lumpy,
concentrated basket. Item selection is done at the 3-digit NIC-2008 level from ASI data, covering
**≥80% of each group's output** — a relatively narrow set of large items/firms can dominate a given
month's print. The popular-press shorthand the task brief itself invokes ("rubber insulated cable
era problems" — a single large, irregularly-timed order swinging the y-o-y capital-goods number)
**[VERIFY — the specific item is not independently confirmed this pass]** is exactly the kind of
single-print artifact this structural fact predicts; the design implication is unambiguous and does
not depend on confirming the specific anecdote: **L11 must never react to one month's print** —
only the Hamilton-filtered, expanding-percentile-ranked series (§C.6), which is precisely the
discipline that turns a lumpy, single-item-dominated index into a usable cycle read.

**Infrastructure/Construction goods and Primary goods — pointer, not rebuild.** The
Infrastructure/Construction Goods leg (cement-, steel-, and construction-materials-linked items,
**12.34%** of the 2011-12-base index) is already built as an L12 Tier-C supply-side confirm in
`fincycle-deep` §C.4, alongside cement's own ICI index and JPC finished-steel consumption — that
construction is not duplicated here. L11 is a different consumer of largely the same underlying
physical reality: where L12 reads construction-goods output as a *supply-lag* signal (how fast new
housing/commercial stock can be built), L11's own role (per `ladder.yaml`, "sector-level tilt
confirmation only") would read the same series as an *investment-heat* signal — the design should
draw the identical fincycle-deep-vaulted series for this purpose rather than standing up a second,
parallel construction-materials percentile inside L11 (the §4.2 de-duplication rule, applied one
level down). Primary Goods (34.05% weight — mining, electricity, basic-materials output) is the
IIP's largest category but is a general activity/nowcast series, not a capex-specific one; Atlas 1.6
lists it among the row's source names but it plays no distinct construction role in L11 beyond
general macro context already captured elsewhere (business-cycle nowcasting, Atlas 2.3) — noted for
completeness, not built as a fourth leg.

**Cadence, lag, revision.** Monthly, released **~6 weeks** after the reference month (A-catalog H3).
Standard IIP practice publishes a **Quick Estimate** that is subsequently **revised** (typically at
+1 and +2 months, converging toward a "final" figure) — treat every single-month pull as provisional
until at least two later releases confirm it, the same discipline this program applies to every
other MoSPI/RBI series with a first/final revision cycle.

---

## C.3 GFCF — the share leg

**Source and structure.** MoSPI's National Accounts Statistics (NAS) publishes Gross Fixed Capital
Formation two ways relevant to L11: (i) **quarterly current & constant-price GFCF** as part of the
expenditure-side GDP release (`esankhyiki.mospi.gov.in`, ~2-month lag, matching the general quarterly
GDP release cadence), and (ii) **annual GFCF by institutional sector** — Public non-financial
corporations, Private corporate sector, Household sector (including unincorporated enterprises and
NPISH), and General government — published in the annual NAS volume and the dedicated GFCF data page
(`mospi.gov.in/gross-capital-formation-gross-fixed-capital-formation-net-capital-stock-economic-
activity-current`, per A-catalog H4). **This institutional-sector split is the object the task
brief's own "~18-month lag" figure names** — [VERIFY exact lag; this pass's own search corroborates
only an older "~10-month" figure from a 2014 MoSPI publication note, not independently reconciled
with 18 months — budget confirming the *current* lag as a first-live-pull task, and treat the split
as arriving materially later than the quarterly aggregate GFCF figure regardless of the exact number].

**The 2011-12→2022-23 base — live now, not "post-2026."** GDP/GFCF's base-2022-23 series (replacing
base-2011-12) was released via MoSPI's own Press Note on **2026-02-27** — the anchor rebase every
other 2026 base change (CPI, WPI, IIP) aligns to, per this program's own repeated cross-references
(A-catalog H4; `debt-deep` §C.9: "FY26 nominal GDP revised **down ~3.3%**even as real growth was
revised **up to 7.6%**"). By this chapter's own writing date, the new base is not a future event to
plan a splice around — it is the *current* reality: **Q1 FY2026-27 GFCF was already published on the
new base at 11.9% real growth**, against **Q1 FY2025-26's 5.8%** (both figures per press coverage
this pass, [VERIFY against a primary MoSPI press note]). The Atlas's "post-2026 rebase splice!" flag
is triggered *today*: any GFCF pull for this project needs both base-2011-12 (legacy) and base-2022-23
(new) series kept distinct, spliced by the same ratio-at-overlap discipline used throughout this
program, never fit through as one continuous line.

**Back-series controversy — a PIT-hazard precedent, not a one-off.** The 2011-12 base itself (adopted
2015, replacing 2004-05) came bundled with a **methodology change**, not merely a reweighting — the
CSO began using the MCA-21 corporate database as an input, and the resulting GDP jump for 2013-14
(old methodology ~5.0% growth vs. new methodology ~6.4%) drew sustained, cross-ideological
skepticism, partly because GDP growth on the new series often diverged from other activity proxies
(industrial credit growth, two-wheeler sales) that commentators expected to track it. The
controversy did not end with the rebase: a **National Statistical Commission-appointed committee
released a "back-series" in November 2018** recomputing pre-2011-12 GDP on the new methodology,
revising UPA-era growth rates *downward* — a release contested partly on procedural grounds (it was
a committee output, not a standard CSO release) [VERIFY exact committee composition and sequence;
press-coverage confidence, not primary-document confidence, this pass]. **The design lesson for L11
is explicit and generalizable**: a GFCF/GDP back-series revision in India has historically been a
*politically* contested event, not merely a technical footnote — this program's own discipline
(keep every vintage, never silently adopt a single "official" retrospective series, annotate every
splice inline) is not excess caution here; it is the minimum response to a documented precedent, and
the 2022-23 rebase should be assumed capable of producing a comparably contested back-series before
one is confirmed either way.

**The institutional-sector split — why it matters for "private capex revival" claims.** Aggregate
GFCF/GDP looked healthy in recent readings (**~30.5% in H1 FY26**, per press coverage this pass,
[VERIFY]) — comfortably inside the range Indian macro commentary treats as "healthy" (commonly cited
as >30%). But the *institutional-sector split* tells a materially different story: the **private
corporate sector's share of total GFCF fell to a decade-low of ~33% in FY24**, while **public capex
has roughly tripled since FY20** under PM GatiShakti / the National Infrastructure Pipeline / PLI-
linked outlays [VERIFY both figures; press-coverage confidence this pass]. A rising GFCF/GDP headline
can therefore coexist with continued private-sector capex weakness if it is being carried by
government spending — which is exactly why L11's other two legs matter as a cross-check: OBICUS and
IIP capital goods both read **private manufacturing-sector** activity fairly directly, so a state
built only from the GFCF aggregate (without OBICUS/IIP confirmation) risks reading a public-capex-led
GFCF print as evidence of the *broad-based* capex upcycle the Atlas row is actually trying to detect.
This is a substantive argument for the three-leg design (§C.6), not merely a data-availability one.

---

## C.4 Project-pipeline proxies (free)

**RBI "Private Corporate Investment: Growth Trends" article.** RBI's Department of Economic and
Policy Research publishes an annual RBI Bulletin article on private corporate investment intentions,
constructed from the **phasing of the total cost of projects sanctioned by banks and financial
institutions during the year** — the closest free analogue this program has to CMIE CapEx's
project-tracking database, though materially coarser (aggregate sanctioned cost/count by year, not
project-level microdata). Recent editions confirmed by search this pass: **"Private Corporate
Investment: Growth in 2024-25 and Outlook for 2025-26"** (RBI Bulletin, ~August 2025), reporting
private corporate investment intentions up **~54% to ~₹2.45 lakh crore in FY2024-25**, an FY2025-26
outlook of **+21.5% to ~₹2.67 lakh crore**, and **greenfield projects at ~89% of total sanctioned
cost** [VERIFY all figures; press-coverage confidence]. A 2026-vintage edition covering FY2025-26
actuals / FY2026-27 outlook is very likely already published or imminent given this program's own
current date (2026-09-01) but was not independently pinned to an exact publication date this pass —
**[VERIFY]**. Access: RBI Bulletin archive (`rbi.org.in/scripts/BS_ViewBulletin.aspx`); **[VERIFY]**
a stable, predictable per-edition URL pattern (credit-deep §C.6 found CRISIL's default-study PDFs
follow one, ICRA's do not — RBI Bulletin articles' own pattern is unconfirmed this pass, budget
re-discovery each edition if none exists). No bulk historical file exists; this is an **annual
hand-transcription** project, the same discipline credit-deep §C.6 applies to GNPA and the CRISIL/
ICRA default studies.

**MoSPI/DPIIT infra project monitoring — stalled and overrun projects.** MoSPI's Infrastructure and
Project Monitoring Division (IPMD) tracks central-sector infrastructure projects costing **₹150
crore and above** via the Online Computerised Monitoring System (OCMS), now consolidating onto the
**PAIMANA** platform (`paimana-proj.mospi.gov.in`, confirmed live this pass; the legacy portal is
described at `ipm.mospi.gov.in/AboutUs/AboutIPMD`) [VERIFY exact migration completeness/date]. IPMD
publishes a **monthly "Flash Report on Central Sector Projects"** flagging time and cost overruns —
genuinely free, genuinely monthly, covering roughly **1,700–1,800 projects across ~17–20 central
ministries**. A July-2026 reading found in search this pass: **cumulative cost overrun of ~₹3.4 lakh
crore across 1,775 projects** (original combined sanctioned cost ~₹33.70 lakh crore, revised to
~₹37.11 lakh crore), with **road transport & highways carrying the most delayed projects (407)**,
followed by railways (114) and petroleum (86) [VERIFY all figures, press-coverage confidence]. This
is a **stock/overrun measure, not a flow** — it tells the design about *execution friction* on an
already-committed pipeline, not about new capex being initiated, so its correct L11 role is a
stalled-projects confirm/context input, never a capex-level component in its own right.

**Banks' capex-linked credit — cross-reference, no duplication.** RBI's Sectoral Deployment of Bank
Credit already carries "Industry" and "Infrastructure" sub-lines at monthly cadence, fully built and
break-annotated (the January-2019 reporting-format revision) in `credit-deep` §C.1/§C.5. L11 reads
this only as a lagging, financing-side confirm of a capex upswing already visible in OBICUS/IIP — the
same "confirm, never re-derive" discipline `commodity-deep` §C.6 applies to the China credit gap and
§C.4 applies to BoP. No new pull is proposed here.

**CGA monthly central capex — the fastest free public-capex flow in the whole catalog.** The
Controller General of Accounts (CGA), Department of Expenditure, publishes the Union government's
own monthly actuals — including a distinct **capital-expenditure line separate from revenue
expenditure** — via the interactive **"Union Government Monthly Accounts Dashboard"**
(`cga.nic.in/MonthDashboardReport/Published/list.aspx`, confirmed live this pass, interactive from
FY2015-16 onward) and the underlying ministry-wise **Monthly Report** tables
(`cga.nic.in/MonthlyReport/Published/...`), with the capital-account series itself running, per
search this pass, from **April 1997**. This is genuinely **monthly**, essentially **T+30–45 days**
— materially faster than OBICUS (quarterly, ~1-quarter lag), IIP capgoods (monthly, ~6-week lag), or
GFCF (quarterly, ~2-month lag for the aggregate; far longer for the institutional split). It is
**not one of L11's three named legs** (Atlas 1.6 names only OBICUS/IIP-capgoods/GFCF), but it is the
public-capex complement to all three — and, per §C.3's own finding that public capex is presently
doing much of the GFCF headline's work, an unusually valuable free monthly context series for
distinguishing a public-capex-led print from a broad-based one.

**State capex — CAG monthly accounts, a genuine construction cost, not a one-line pull.** Each
state's Accountant General (Accounts & Entitlement) office publishes **Monthly Civil Accounts**
covering April-to-date capital expenditure by major head, at per-state pages under the CAG portal
(confirmed pattern this pass: `cag.gov.in/ae/<state>/en/ae-state-accounts?cat=792`, e.g. Assam,
Madhya Pradesh). **No single, consolidated, all-India monthly state-capex file exists free** — this
would be a 28-state-plus-UT hand-aggregation project, each state page structured independently
[VERIFY whether page structure is consistent enough across states to script once]. CAG's own annual
**State Finances Audit Reports** (one PDF per state per year, `cag.gov.in`) are the more usable, if
far lower-frequency, free consolidated view — already the source A-catalog and `debt-deep` §C.1 draw
on for states' debt/GSDP context. Budget the monthly, all-state build as an **exploratory pilot** on
a handful of the desk's highest-priority states (§C.9 step 41), not a Phase-0 commitment.

---

## C.5 Corporate-side confirms

**Listed-company capex from disclosures — the aggregator-tier limit.** Quarterly results (Reg. 33)
and annual-report fixed-asset/capex schedules are free at source (NSE/BSE filings, company
investor-relations pages), but **no free source bulk-tabulates aggregate listed-company capex**
across the universe. Screener.in-type aggregators expose per-company capex/fixed-asset line items on
their free tier for casual, single-name lookups, but rate-limit or paywall bulk/API-scale access —
not usable as a systematic L11 input at the free tier. This is the identical gap `ingest/README.md`'s
own Addendum 2 already names for the desk's fundamentals pipeline generally (**no fundamentals
puller exists in `ingest/` at all yet**; `pull_nse_financial_results.py` is the eventual free source,
per that addendum's own plan). L11's corporate-capex confirm should ride on that pull once built,
not stand up a second, parallel fundamentals scraper here.

**BHEL/L&T order books — free, quarterly, genuinely useful thermometers.** Both companies report
explicit order-inflow and order-book figures with every quarterly result, straight from exchange
filings/company press releases — zero construction cost beyond reading the results. Search this pass
found: **L&T Q3 FY26 order inflows ~₹1.36 lakh crore, order book ~₹7.3+ lakh crore**; **BHEL FY26
order inflows ~₹75,000 crore, order book ~₹2.4 lakh crore** [VERIFY exact figures every quarter —
these are genuinely quarter-refreshed numbers, cited here as an existence proof, not a static fact].
Both are useful **qualitative** cross-checks — L&T is diversified across infra/defence/IT-services,
BHEL is power-equipment-concentrated, so each carries a different sector lens — but a
comparability problem across two structurally different, decades-spanning companies makes an
expanding-percentile construction of order-book growth an **open, unresearched question**, not a
decided design choice: use both as narrative/sanity confirms on the OBICUS/IIP/GFCF-based state
(§C.6), never as a fourth ranked leg, until that question is separately pre-registered and tested.

**Cement/steel volumes — cross-reference, no duplication.** Physical construction-materials demand
(cement ICI, JPC finished-steel consumption) is already vaulted as an L12 Tier-C supply-side confirm
in `fincycle-deep` §C.4; the *world-price*/equity-market lens on the same names (Nifty Metal sector
methodology) is built in `commodity-deep` §C.5. L11 draws on neither construction independently —
it is the same underlying physical-demand and equity-market reality those two Parts already read,
and a parallel L11-specific construction-materials percentile would violate the ladder's own
de-duplication rule (§4.2) at one remove. The design answer here is explicit non-duplication.

---

## C.6 The L11 pipeline

**Three legs, one composite, the shared machinery.** L11's construction mirrors L12's own
`financial_cycle_state` pattern (`quant/ladder/financial_cycle.py`) almost exactly, extended from two
legs to three: each leg is independently Hamilton-filtered (`quant/stats/hamilton.py`,
`mode="expanding"`, never HP) and `expanding_percentile`-ranked (`quant/ladder/credit_cycle.py`), the
three percentile ranks are converted to a signed `[-1,+1]` scale and combined as an **n_legs-aware
mean** — a date with all three legs present gets a full-confidence reading; a date with only one or
two legs present (necessarily true for most of India's history, since OBICUS starts 2008) gets a
**degraded** reading, flagged by `n_legs`, exactly as `financial_cycle_state` already flags a
short-HPI date for L12. **B-module-specs' own M16 spec already names the target function signature**:
`capex_cycle_clamped(obicus, iip_capgoods, gfcf) -> Series` — this Part's job is to specify the three
inputs that function consumes and the construction discipline around them, not to write the module.

**Warm-up arithmetic — when does each leg's own rank mature?** Reusing this program's established
convention (never inventing a new grid; commodity-deep and fincycle-deep both anchor a Band-1
monthly series at h=60 months/p=1/min_obs=48 months, treating the Contract's "≥4 observations"
Tier-B/C floor as ≈4 years scaled to the series' own cadence) and applying the same scaling logic to
L11's own faster registry tau_half prior (`[36, 60]` months, per `ladder.yaml`):

| Leg | Cadence | h, p (reused convention) | min_obs (≈4 obs, scaled) | Usable start | First trustworthy percentile |
|---|---|---|---|---|---|
| OBICUS (CU) | quarterly | 20q (5y), p=1 | 16q (4y) | 2008-Q2 | **≈2017** (2008 + 5y warm-up + 4y floor) |
| IIP capital goods | monthly | 60mo (5y), p=1 | 48mo (4y) | 2011-04 (current base only) | **≈2020** (naive, single-base window) |
| IIP capital goods | monthly | 60mo (5y), p=1 | 48mo (4y) | **~1994** (if ratio-spliced across 1993-94→2004-05→2011-12→2022-23) | **≈2003** (chained-history window) |
| GFCF/GDP | annual | 5y, p=1 | 4y | 1950-51 in principle; usable comparability **[VERIFY]** decade | mature well before this program's build (decades of runway either way) |

**GFCF matures earliest by a wide margin; OBICUS matures latest** — exactly the ordering the Atlas's
own "n_legs degradation design (GFCF longest, OBICUS shortest)" framing anticipates, now with actual
dates attached. The IIP capital-goods row shows a genuinely useful design fork: read naively (current
base only, since 2011), its own percentile does not mature until ~2020; but this program's own
established splice discipline (ratio-at-overlap chaining across all four IIP base vintages —
1993-94→2004-05→2011-12→2022-23, the same technique commodity-deep chains Jacks→IMF-PCPS→EIA) would
push its usable start back to ~1994 and its maturity to ~2003 — a materially more mature leg. This
Part **recommends** the chained approach (consistent with program practice elsewhere) but does not
build the four-vintage splice here — it is a genuine, nontrivial construction task, budgeted as
§C.9 step 36. **The exact (h, p, min_obs) triple for L11 is not yet fixed in `ladder.yaml`** (only
the `tau_half_months` prior is stored) — per Contract §6, this Part states the reused-convention
candidate above as the recommended default, not a unilateral decision; it is a pre-registration item
for the data phase, exactly as commodity-deep and fincycle-deep both flagged their own (h,p) choices
as reused-not-invented rather than silently final.

**The non_positive clamp — applied at consumption, not baked into the state.** Per the
consistency-audit's own C2 finding (`research/register/consistency-audit.md`) and its fix (now
encoded in `ladder.yaml`'s `contribution_clamp: non_positive` and enforced by `config/validator.py`),
a hot L11 reading must never *add* regime-score budget through the shared `macro_credit_block`
average — Tier-C may only reduce. **The correct place to apply that clamp is at block aggregation,
not inside L11's own state function.** Concretely: the three-leg composite above should be exposed
as a **raw signed state** in `[-1, +1]` (the exact `financial_cycle_state` pattern — no clamp inside
that function), and `capex_cycle_clamped(...)` should be a thin wrapper applying `min(0, raw)` **only
at the point `macro_credit_block` combines L6+L10+L11+L12** — the same split M16's own module spec
already implies by naming `capex_cycle_clamped` as a distinct function from whatever raw composite it
wraps. **Why this ordering matters, stated explicitly (the task's own question):** collapsing the
clamp into the state itself would make a raw reading of +0.05 (barely hot) and +0.85 (a dangerously
extended overbuild) both silently disappear to 0 the moment they are stored — correct for regime-
score purposes, but destructive for anything downstream that legitimately wants the *magnitude* of a
positive reading, not just its sign. L11's own registry role is explicitly **"sector-level tilt
confirmation"**, not only regime-score input: a rule deciding how hard to lean against cement/
capital-goods/infra sector weight (or, on the H62 capital-cycle candidate's own logic, Atlas 2.15/
13's asset-growth conditioner) needs to distinguish a mild overbuild from an extreme one, and that
distinction is only available if the raw signed state — not its clamped shadow — is what the module
stores and exposes. The clamp belongs exactly where Contract §4's rule actually binds: the one shared
regime-score aggregation point, and nowhere earlier in the pipeline.

**Splice/rebase handling.** OBICUS carries only a soft continuity caveat (panel-composition drift,
no formal base-year break). IIP capital goods and GFCF **both** crossed a hard base-year break within
the same six-month window in 2026 (IIP: 2026-06-01; GFCF/GDP: 2026-02-27) — meaning L11 is, at this
moment, the single seat inside `macro_credit_block` most directly exposed to the "2026 base-year
revision wave" this program repeatedly names, with **two of its three legs** breaking almost
simultaneously. Each leg's splice must be applied **independently, at its own overlap point** — never
a single joint correction that conflates the IIP break with the GFCF break, even though they landed
months apart in the same calendar year.

**Failure modes.** OBICUS response-rate collapse in a stress quarter (self-selection bias exactly
when the signal is most needed, §C.1); a single lumpy capital-goods print swinging a raw month-over-
month read (mitigated structurally by ranking the Hamilton-filtered series, never a raw MoM/YoY
number, §C.2); a contested GFCF back-series revision recurring at the 2022-23 rebase, echoing the
2015/2018 precedent (§C.3) — mitigated by keeping every vintage, never silently adopting the latest;
a joint multi-source stale-data risk if a MoSPI/RBI portal migration delays several releases inside
the same block at once (worth naming since L11 shares `macro_credit_block` with three other
multi-source composites, any one of which stalling degrades the shared aggregate).

**Monitor cadence.** OBICUS: quarterly (bound by its own ~1-quarter lag). IIP capital goods: monthly
(~6-week lag — nominally the freshest-refreshing leg, though, per the warm-up table above, presently
the *least* mature rank under the naive single-base window — a genuine tension between freshness and
trustworthiness worth carrying forward, not resolving by fiat). GFCF: quarterly for the aggregate
(~2-month lag), with the annual institutional-sector split treated as a slower **confirm-only**
input, never the primary ranking signal (mirroring how `commodity-deep` treats its own INR-terms
variant as downstream/secondary, never a substitute for the primary ranking). The composite should
recompute whenever any leg refreshes, with `n_legs` communicating partial updates — the exact
refresh-scheduling rule is a data-phase implementation detail this Part specifies the *inputs* for,
not the final code.

---

## C.7 Vintage/PIT hazard table

| Source | Publication lag | Revision policy | Break / date | Backtest hazard |
|---|---|---|---|---|
| RBI OBICUS | ~1 quarter | Not typically revised after release [VERIFY] | Soft panel-composition drift only; no formal base year | Voluntary-survey self-selection may bias stress-quarter readings upward (§C.1); no seasonal adjustment — Q4 spike contaminates raw QoQ reads |
| MoSPI IIP (capital goods, infra/construction) | ~6 weeks | Quick Estimate → revised (+1, +2 months) | **2011-12 → 2022-23, effective 2026-06-01** (already live); prior breaks 1993-94/2004-05/2011-12 | Any series crossing 2026-06 needs ratio-splice discipline; single-print volatility from lumpy WIP-basis items — never react to one month |
| MoSPI GFCF (aggregate, quarterly) | ~2 months | Provisional → first-revised → final, ~2-year cycle (standard NAS practice) | **2011-12 → 2022-23, effective 2026-02-27** (already live) | Splice discipline as IIP; treat every vintage as provisional until confirmed |
| MoSPI GFCF (institutional-sector split, annual) | **~10–18 months [VERIFY exact current lag]** | Same NAS revision cycle as aggregate | Same 2026-02-27 break | Confirm-only input, never primary ranking; 2015/2018 back-series precedent — assume any future back-series is contestable until independently confirmed |
| RBI "Private Corporate Investment" article | Annual (RBI Bulletin) | Not revised in the ordinary sense — a fresh edition each year | None identified | Hand-transcription-only, no bulk file; a coarse aggregate, not project-level — do not over-read precision |
| MoSPI/DPIIT IPMD Flash Report | Monthly | Cumulative overrun figures restated as projects re-report | OCMS → PAIMANA platform migration [VERIFY exact date] | Stock/overrun measure, not a flow — context only, never a capex-level input |
| CGA Monthly Accounts (capex line) | ~T+30–45 days | Actuals; not typically revised at the monthly cadence | None identified | The fastest, lowest-hazard series in this chapter — public capex only, not the whole capex cycle |
| CAG state Monthly Civil Accounts | Monthly, per-state | State-specific [VERIFY] | None identified at the series level | No consolidated free file exists; per-state page-structure consistency unconfirmed — a construction-cost hazard, not a data-quality one |
| BHEL/L&T order books | Quarterly (results date) | Not revised | None (company-level, continuous disclosure) | Two-name, structurally non-comparable thermometer — qualitative confirm only, never a ranked input |

---

## C.8 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **CMIE CapEx / Prowess project-level private investment database** | Paid subscription, explicitly excluded by Contract §3 | RBI's "Private Corporate Investment: Growth Trends" article (§C.4) — an aggregate, annual, coarser substitute (sanctioned cost/count/greenfield-share, not project-level microdata); this is the design's own already-named substitute (per `docs/masterplan/A-data-catalog.md` §6's gap-list entry, "DESIGN §13 already names the substitute") |
| **Project-level (not aggregate) sanctioned-investment microdata, free** | No free Indian source publishes this at the project level; CMIE is the only known product that does, and it is paid | Aggregate RBI article + IPMD's project-level *overrun* data (which covers execution status, not new sanctioning) — a partial, not a full, substitute; project-level *initiation* microdata remains genuinely unmeasured free |
| **Under-construction vs. commissioned capacity-by-vintage cut** | No free source publishes installed capacity broken out by vintage/commissioning date at an economy-wide level | OBICUS's own CU reading is the closest free proxy, but it reads utilization of *existing* capacity, not the vintage structure behind it |
| **Bulk, free, aggregate listed-company capex/fixed-asset time series** | No free aggregator bulk-tabulates this across the universe (screener-type sources rate-limit/paywall bulk access) | Wait on the desk's own eventual `pull_nse_financial_results.py` (ingest/README.md Addendum 2) rather than building a second scraper here |
| **A single, consolidated, free, all-India monthly state-capex file** | Each state's Accountant General publishes its own Monthly Civil Accounts independently; no central aggregator exists | Pilot a handful of priority states (§C.9 step 41) before committing to a 28-state-plus-UT build; fall back to CAG's lower-frequency annual State Finances Audit Reports for a consolidated, if far slower, view |
| **A stable per-edition URL pattern for the RBI Private Corporate Investment article** | RBI Bulletin's per-article URL scheme is not confirmed stable this pass (contrast CRISIL's confirmed stable pattern, credit-deep §C.6) | Re-discover the link each year if no pattern holds, the same discipline credit-deep already applies to ICRA's ID-keyed download links |

---

## C.9 Runsheet addendum 7

Continuing the global step numbering `commodity-deep` Part C's own runsheet (`ingest/README.md`'s
own addendum 6, §C.10) established through **step 34** — no existing `ingest/pull_*.py` script
covers any of L11's three named series or its project-pipeline proxies, so this is, like every
predecessor Part C, a genuinely new fixture family.

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 35 | Pull RBI OBICUS: all available rounds (PDF/Excel per round from the confirmed QuarterlyPublications page); confirm the exact DBIE bulk-query table path and the current per-round responding N | §C.1 | 3–4 | The shortest, latest-maturing leg (§C.6) — start it first so its warm-up clock is running while other legs are pulled |
| 36 | Pull MoSPI IIP capital goods + infrastructure/construction goods: both base-2011-12 (legacy) and base-2022-23 (new, effective 2026-06) full history; confirm the splice overlap window; **also attempt the four-vintage ratio-splice chain (1993-94→2004-05→2011-12→2022-23)** the §C.6 warm-up arithmetic recommends, piggybacking on whatever base-year documentation the fincycle-deep IIP pull (its own runsheet step 22) already retrieves | §C.2, §C.6 | 4–6 | The chained-vs-naive maturity-date gap (2003 vs 2020, §C.6) makes this the single highest-leverage pull in this addendum |
| 37 | Pull MoSPI GFCF: quarterly current+constant (both bases) plus the annual institutional-sector-split table, full available vintage history from the NAS annual publication and the GFCF-specific data page; hand-transcribe pre-digital-portal years if the bulk export does not reach far enough back | §C.3 | 4–6 | The longest-history, earliest-maturing leg, but the institutional-sector table's own format/lag makes it the most labor-intensive single pull here |
| 38 | Pull RBI "Private Corporate Investment: Growth Trends": every available annual RBI Bulletin edition; hand-transcribe sanctioned-cost/count/greenfield-share into a time series (no bulk file exists) | §C.4 | 3–4 | Same hand-transcription discipline as GNPA/FSR/CRISIL/ICRA (credit-deep §C.6) — small, high-value, no bulk shortcut available |
| 39 | Pull MoSPI/DPIIT IPMD Flash Report on Central Sector Projects: full available monthly history from OCMS/PAIMANA; confirm whether historical months are queryable or only the latest is exposed | §C.4 | 3–4 | Confirms whether this is a genuine time series or a single current snapshot before it is relied on as a monthly context input |
| 40 | Pull CGA Monthly Accounts Dashboard + ministry-wise Monthly Report: full available history (interactive dashboard from FY2015-16; capital-account series back toward April 1997 via the archive pages); isolate the capital-expenditure line | §C.4 | 2–3 | Cheap, high-value, the fastest-refreshing public-capex series in the whole catalog — do not defer |
| 41 | Pilot CAG state Monthly Civil Accounts on 3–5 priority states (set to be confirmed against the desk's own equity sector-tilt priorities); confirm whether the per-state page structure is consistent enough to script once before committing to a full 28-state-plus-UT build | §C.4 | 5–8 | Exploratory — may legitimately not scale to all states within budget; treat as a pilot, not a Phase-0 commitment |
| 42 | Pull BHEL + L&T quarterly results (order-inflow/order-book figures): full available quarterly history from investor-relations pages/exchange filings; piggyback on whatever bulk Reg. 33 results puller the desk eventually builds (ingest/README.md Addendum 2) rather than a bespoke two-name scraper | §C.5 | 1–2 | Small, cheap, qualitative-confirm-only — low priority relative to the three ranked legs |
| 43 | `config/` registry + CI validator smoke-test against the newly-pulled L11-adjacent fixtures; confirm the three-leg `n_legs` degradation logic runs clean across the pre-2008 (OBICUS-absent) period of the combined fixture set, and that `capex_cycle_clamped` reproduces `min(0, raw)` against the raw-state fixture | §C.6 | 2–3 | Confirms the pull satisfies the "every module runs on fixtures with zero live data" gate, unchanged from every other Part C's own closing step; also the first executable check on the raw-vs-clamped split §C.6 argues for |

**Total estimated incremental effort: ~27–40 hours**, on top of A-catalog's existing ~45–60-hour
Phase-0 estimate and the other Part Cs' own already-budgeted extensions — driven mainly by step 37
(GFCF's institutional-sector split, the most format-awkward single pull) and step 36's optional but
recommended four-vintage IIP splice chain, with step 41 (state capex) carrying the widest cost range
given its explicitly exploratory, may-not-scale framing.

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §6 (no magic numbers — the (h,p,min_obs) reuse argued in §C.6), §8
(Hamilton filter only), Known Prior #11 (no live network access; principal's-machine ingestion);
`config/ladder.yaml` L11_capex_cycle (tier C, reduce_only, `contribution_clamp: non_positive`,
`block: macro_credit_block`, `inputs: [L10_credit_block]`) — no registry edit made here;
`docs/masterplan/B-module-specs.md` M16 (`capex_cycle_clamped(obicus, iip_capgoods, gfcf) -> Series`,
the target this Part specifies inputs for); `research/register/consistency-audit.md` C2 (the
non_positive-clamp finding §C.6 inherits and explains the raw/clamped split for); `research/cycles/
capex-deep/capex-RESULTS.md` and `research/register/trial-ledger.md` (the JST-panel analogue trials
IN1–IN3 — not restated here); `quant/stats/hamilton.py` (`hamilton_filter`), `quant/ladder/
credit_cycle.py` (`expanding_percentile`), `quant/ladder/financial_cycle.py`
(`financial_cycle_state` — the exact pattern this Part's three-leg composite extends); `research/
cycles/credit-deep/partC-data.md` §C.1/§C.5 (sectoral deployment — inherited, not duplicated),
§C.6 (GNPA/CRISIL/ICRA hand-transcription discipline, reused for the RBI PCI article);
`research/cycles/commodity-deep/partC-data.md` §C.3 (WPI), §C.4 (BoP), §C.6 (China-credit scope
discipline, the "confirm, never re-derive" pattern §C.4 applies to sectoral deployment) — the style
bar this Part matches; `research/cycles/fincycle-deep/partC-data.md` §C.4 (cement ICI, IIP
Infrastructure/Construction Goods, JPC steel — inherited, not duplicated); `docs/masterplan/
A-data-catalog.md` G9 (OBICUS), H3 (IIP), H4 (GFCF), §6 (the CMIE-substitute gap-list entry this
Part's §C.8 restates with sourcing); `ingest/README.md` addenda 1–6 (existing pull scripts and gaps
— sectoral deployment, WPI, and BoP already covered elsewhere, not duplicated here) and this
chapter's own addendum 7 (§C.9).*

---

# Part D — The mathematics (atlas 1.6; seat L11, Tier C, clamped)

## D1. The three-leg state and the clamp's algebra

state_t = clip( Σ_i w_i·(2P_i,t−1)·1[i] / Σ_i w_i·1[i], −1, 1 ), i ∈ {util, capgoods, gfcf},
n_legs = Σ 1[i] first-class (India's legs start ~1950s / 1994 / 2008 — degradation is the
DESIGNED path for decades of history, tested). Consumption: the macro block reads
min(0, state) — the non_positive clamp — while sector-tilt consumers read state raw. The
ordering matters: clamping inside the state would destroy the positive half for everyone;
clamping at consumption destroys it only where the consistency audit showed it double-counts
(a hot capex print co-occurring with hot credit inside ONE shared 0.20 budget).

## D2. What IN1-IN3 permit — the weakest seated evidence in the ladder, said plainly

IN1 failed its bar (9/15 negative): the capex state is NOT a pooled forward-return regularity
on analogues. IN3's non-monotone quintiles (middle lowest) say the state does not order
returns. What survives: (i) IN2's repair result — overbuilds take years to regain peak
(median 4y, censoring counted against) — the capacity-limit sentence measured; (ii) the mild
top-vs-bottom penalty (−4.5pp/5y) at the HOT extreme only. Hence the seat's whole design:
subtract-only, extremes-only, inside the block, Tier C. This entry DOWNGRADES nothing (the
seat was already clamped) and GRADUATES nothing (C→B needs the India purged backtest,
changes_if). The atlas's rare honest position: a seat justified by its own weakness.

## D3. Impulse vs level, third verification

The gap legs collapsed at the planted turn (test suite) exactly as L1/L12's did — the
expanding Hamilton gap is an impulse object (verification #1 falsified the level reading;
this entry re-confirms on a third fixture). The LEVEL job (how mature is the boom) is carried
by the util-percentile leg alone, which is why it enters as a level rank, not a gap.

# Part E — The algorithm (L11, monthly/quarterly, India)

```
STEP 1  legs per partC: OBICUS utilization (quarterly, ~1q lag, from 2008), IIP capital goods
        (monthly, splice across 2004-05/2011-12/next bases per registry), GFCF share
        (quarterly, 2011-12 base; the post-2026 rebase lands as a NEW spliced series entry)
STEP 2  expanding percentiles on shared grids (warm-up per leg; OBICUS ranks mature ~2013)
STEP 3  state, n_legs = capex_cycle_state(util_pct, capgoods_pct, gfcf_pct)
STEP 4  consumption: macro_credit block reads clamp_non_positive(state) inside the 0.20
        budget (de-dup with L10/L12 per §4.2); sector projection (industrials, capital
        goods, infra financiers) reads state RAW as tilt confirmation, Tier-C caps
STEP 5  public-vs-private split (annual GFCF by institutional sector, ~18m lag) as a
        CONDITIONING annotation, never a leg — the 2021+ arc question stays open honestly
MONITOR quarterly leg freshness; base-revision registry; annual IN1-IN3 re-run; the India
        purged backtest (changes_if) once OBICUS/IIP/GFCF are vaulted (runsheet addendum 7)
FAILURE MODES: OBICUS discontinuation/sample change; IIP capgoods lumpiness (use 3m means,
        stated); rebase splice errors (the atlas's own flagged hazard); public-capex era
        making GFCF hot while private repair continues (n_legs fine, INTERPRETATION flagged
        by the split annotation)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| macro_credit block (0.20 shared) | min(0, state) — subtract-only in overbuilds |
| Sector projection | raw state as capital-goods/infra tilt confirmation (Tier-C cap) |
| Hedge scheduling | hot-state watch flag (with L10/L12 joint reads) |
| Cycle School | Lesson 16: the seat justified by its own weakness; clamp algebra |
| Trial ledger | IN1-IN3 as the calibration record between DG1 and FC1 |

Designs: **IC1** India three-leg state on real data (blocked on runsheet addendum 7 pulls);
acceptance: the 2011-2020 twin-balance-sheet decade must print as a persistent negative-to-low
state with n_legs rising 2→3 through 2008-2013 — a SHAPE check on known history, not a return
claim. **IC2** the graduation test (changes_if): purged-CV incremental value of min(0,state)
inside the macro block on India data — the C→B gate. **IC3** public/private split annotation
value: does the split flag 2021+ as a different animal than 2003-08 (descriptive, annual).

# Part H — Knowledge ledger (atlas 1.6)

**Established (analogues, our runs):** post-peak repair takes years (IN2, median 4y, honest
wide IQR); the capex state is NOT a pooled return signal (IN1 fail; IN3 non-monotone) — the
clamp design is evidence-backed. **India [the seat's own country]:** three legs with 1950s/
1994/2008 starts; two-and-a-half arcs on the public record (cases chapter); the 2021+ arc's
public-vs-private character is an OPEN question the seat annotates rather than answers.
**Unknowable:** whether the current public-capex era seeds arc #3 or a plateau; L11 waits at
its clamp and the sentinel watches n_legs. **Process:** module shipped at evidence tier C
with the tier stated in its docstring — machinery is not evidence.
