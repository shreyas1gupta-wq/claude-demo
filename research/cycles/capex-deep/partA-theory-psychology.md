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
