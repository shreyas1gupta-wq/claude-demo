# The Business Cycle — Context Monograph (Atlas 2.3; no seat, zero budget)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** CONTEXT inside the macro block — the most famous cycle in economics gets
no seat and no budget, because the macro block's four seated states (L6 money, L10 credit, L11
capex, L12 property) already shadow it inside one shared weight. What the entry ships instead:
the dated India chronology as the desk's EVENT CLOCK, the monthly nowcast briefing surface, two
registered India designs (BD1/BD2), and one registry-level export:

**The headline (BC2, pre-registered): the imported "credit leads growth" direction FAILS on its
own home panel.** 16/18 JST countries peak at NEGATIVE lags (−3..−5y) — the GDP gap leads the
credit gap at cycle frequency almost everywhere; only 11% show credit leading (bar was 60%).
Saini et al.'s India finding (business leads credit) reads as the GENERAL case. Caveats logged
with the print (differential smoothing, grid-edge pinning, location-only); L10's crisis-warning
authority (J1 AUROC, a different mathematical object) is explicitly untouched. A STANDING
REGISTRY WARNING now applies to every imported lead-lag direction in every future entry.

**Also measured:** BC1 PASS — growth cycles are real at the claimed band (median 6y spacing,
65% in [3,7]y); BC3 — 77% one-year regime stickiness (cf. inflation eras' 81%). And the dating
record's honest core: India's chronologies genuinely DISAGREE (the annual-sign method finds no
1991 recession; the monthly Dua-Banerji method dates one Apr-Sep 1991) — the master table
preserves the disagreement; the Feb-2026 GDP rebase is a live splice hazard tagged in place.

**Assembled from:** partA-theory-psychology.md · partB-cases-dating.md · buscycle-RESULTS.md ·
partDEFH-math-algo-harvest-ledger.md.

---

# PART A + G — Theory (dating methodology, the no-seat argument, the India direction twist) and operator psychology

# Business Cycle Proper — Theory & Operator Psychology (Atlas 2.3)

Part A: Theory — the object, its measurement machinery, and why it carries no ladder seat · Part
G: Operator psychology · v1.0 · 2026-09-02 · Atlas entry 2.3 (`docs/CYCLE_ATLAS.md` row 79, §3
"Band 2 — the business-credit band"). Ladder status: **NO SEAT** — CONTEXT inside the
`macro_credit_block`, correlated with `L6_monetary_stance`, `L10_credit_block`, `L11_capex_cycle`
and `L12_realestate_medium_cycle` (`config/ladder.yaml`; `docs/DESIGN.md` §4.1–4.2's shared-budget
de-duplication rule: the four ladder seats already span money, credit, investment and property —
a fifth "growth state" built from the same underlying activity would be their correlated shadow
inside the same 20%-of-regime-score budget, never an independent claim on it). Complements, never
duplicates: `docs/cycles/01-credit-cycle.md` / `research/cycles/credit-deep/
partA-theory-psychology.md` §A.5 (Bernanke-Gertler-Gilchrist — not re-derived here) and
`research/cycles/capex-deep/partA-theory-psychology.md` §A.2.2 (Kydland-Prescott time-to-build —
not re-derived here). Evidence base: this file plus `research/dossiers/03-credit-financial-cycle.md`
(D03, esp. I1–I5 and I4's Saini-Ahmad-Bekiros finding), `research/dossiers/08-india-mid-cycles.md`
(D08, esp. I1–I3 monetary/capex nowcast inputs, I10 monsoon), and this program's own
`research/cycles/buscycle-deep/buscycle-RESULTS.md` (BC1–BC3, run on the JST R6 analogue panel —
India itself is not in JST) and `research/cycles/buscycle-deep/partDEFH-math-algo-harvest-ledger.md`
(construction/algorithm/harvest map this file's findings feed — a sibling pass, not re-derived
here). Style and depth calibrated to `research/cycles/fincycle-deep/partA-theory-psychology.md`.
Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in). Status: theory
and citations verified this session via live search (see per-citation tags); India's own dating
chronology — Dua-Banerji's turning points — is the cases chapter's job, a sibling dossier; this
file treats that chronology only as the free-standing "event clock" the entry contributes (§A.4).

This file assumes the ladder's frozen construct as given: Atlas row 2.3 is explicitly a **CONTEXT**
entry, not a ladder seat — zero regime-score budget, zero return budget, no `reduce_only` clamp
because it has no allocation authority to clamp. Part A supplies the theoretical case for why that
verdict is correct rather than a shortcut, and documents what the entry earns instead of a budget
line: an independently-dated event clock, a standing registry warning on imported lead-lag
directions, and a catalogued nowcast surface. Part G turns to the desk operating without a seat here
— the psychological pull of a headline-grabbing macro object that *feels* like a signal, and how
that pull shows up on a desk whose own growth-cycle reality departs from the imported picture at
almost every turn.

---

## PART A — Theory: the object, its measurement machinery, and why it carries no ladder seat

### A.1 The object, and why it gets no seat

**(i) What "the business cycle" is as a measured object.** **Burns, Arthur F. & Mitchell, Wesley
C. (1946), *Measuring Business Cycles*** (National Bureau of Economic Research) supplies the
definition every later dating exercise — including this program's own — still works from: "a
cycle consists of expansions occurring at about the same time in many economic activities,
followed by similarly general recessions, contractions, and revivals which merge into the
expansion phase of the next cycle." Two features of that sentence carry the whole methodological
tradition. First, the object is defined by **comovement across many series** — output, income,
employment, prices, interest rates, banking transactions, transportation — "taking into account
possible leads and lags in timing," not by any single headline print; this is precisely why the
NBER's own dating committee, to this day, refuses to anchor a call to GDP alone (A.3 below).
Second, the object is stated in **levels**: expansion and contraction are movements in the level
of aggregate activity, not merely its growth rate — the classical business cycle is a cycle in
*how much* the economy produces, not *how fast* it is accelerating. **[Verified — NBER's own
publication record, Burns-Mitchell 1946, and its restatement in Harding-Pagan 2002 below.]**

**(ii) NBER dating committee methodology — judgment, not a mechanical rule.** The U.S. NBER
Business Cycle Dating Committee places the most weight on real GDP but, because GDP is quarterly
and revised, cross-checks it against a small set of monthly series — principally real personal
income less transfers and payroll employment, supplemented by industrial production and real
manufacturing-and-trade sales — and applies three qualitative criteria jointly: **depth**
(how large the decline), **diffusion** (how broadly it is spread across sectors), and **duration**
(how long it persists), with the explicit rule that extreme severity on one criterion can offset
weakness on another. This is a **committee judgment**, not an algorithm — there is, in the
Committee's own words, "no fixed rule about which other measures contribute information to the
process." **[Verified — NBER's own "Business Cycle Dating Procedure: Frequently Asked Questions"
and related NBER dating-committee announcements.]** This judgment-based tradition is the historical
parent of two later, deliberately mechanical descendants this program actually uses for
construction: the Bry-Boschan turning-point algorithm and the Harding-Pagan BBQ variant (§A.3),
which trade the Committee's contextual flexibility for a repeatable, non-discretionary rule —
exactly the trade-off this program's own CONTRACT §6 ("no magic numbers... but broad,
sensitivity-robust rules") already prefers everywhere else in the design.

**(iii) Levels versus deviations — why India's own entry is necessarily a growth-cycle object, not
a classical one.** **Mintz, Ilse (1969), *Dating Postwar Business Cycles: Methods and Their
Application to Western Germany, 1950–67*** (NBER) is the paper that had to invent a second concept
because the first one stopped working: postwar West Germany, like many fast-growing economies,
essentially never posted an absolute decline in the level of output — yet it plainly had periods
of boom and periods of palpable slowdown that mattered to policy and to markets. Mintz's answer was
the **growth cycle**: fluctuations in the *deviation of activity from its trend growth path*
(a smoothed, detrended series), rather than fluctuations in the level itself. A further, even
higher-frequency refinement — the **growth-rate cycle** — dates turning points in the *rate of
growth* itself (year-over-year or smoothed first-differences), sitting one derivative further from
the classical object and correspondingly shorter and choppier. **[Verified — Mintz 1969, NBER
Books and Chapters record, including its own chapters on "Deviation Cycles" and "Step Cycles."]**
India's own record settles which of these three concepts applies here, and settles it starkly:
classical (level) contractions in India's post-independence record are documented at
**December 1964–November 1965, May 1966–April 1967, July 1972–May 1973, December 1973–February
1975, May 1979–March 1980, and April–September 1991** — six episodes clustered almost entirely in
the pre-liberalization, monsoon-shock-dominated era — with a long silence afterward until **2020**,
when the COVID shock produced two consecutive quarters of outright GDP contraction (Q1 FY21 roughly
−24%, Q2 FY21 roughly −7% **[VERIFY: exact NSO print magnitudes, recalled from press coverage, not
independently re-pulled from an MOSPI release this session; the pre-1991 dates and the post-1991 gap
themselves are corroborated across multiple India business-cycle papers surfaced this session]**),
India's first unambiguous classical recession of the post-liberalization era. Between 1991 and 2020,
India grew every single year in level terms — its "business cycle," to the extent
the word applies at all in the classical sense, is a sequence of **speed-ups and slowdowns in the
rate of growth**, never a sequence of booms and busts in the level of output. This is not a minor
technical point; it is the entire reason Atlas 2.3 must be read, cited, and harvested as a
**growth-cycle** (or growth-rate-cycle) object, and it is why any classical-business-cycle
literature imported wholesale — including much of the multiplier-accelerator and RBC theory in
§A.2 — needs translation before it applies to India at all.

**(iv) The design argument for CONTEXT-not-seat.** The ladder's macro block already holds four
seats reading, in effect, four faces of the same underlying corporate-and-household-leverage
phenomenon: **L6** (monetary stance — the policy face), **L10** (the credit block — the lending
face), **L11** (the capex cycle — the investment face), and **L12** (the medium financial cycle —
the property/collateral face), sharing one ≤20%-of-regime-score `macro_credit_block` budget under
the de-duplication rule (`docs/DESIGN.md` §4.2). A "business-cycle state" built from IIP momentum,
GST collections, and OBICUS utilization would not add a fifth, independent face to that block — it
would largely restate the *aggregate outcome* the other four are jointly trying to explain and
condition permission on. Output, credit, capex and property cycles comove by construction (this is
literally Burns-Mitchell's own comovement definition, §A.1i) — a growth-cycle reading is, to first
order, the correlated shadow the other four seats already cast. Giving it its own budget line would
either double-count the same signal inside one shared cap or require carving out a fifth slice of
the 20% budget for an entry whose Tier-B evidence (§A.4) supports its *existence and datability*,
not an independent predictive claim strong enough to earn scarce budget on its own. **CONTEXT**, in
this program's own vocabulary (`docs/CYCLE_ATLAS.md` §0), means exactly this: interpretation with
zero allocation authority — it shapes how the desk reads L6/L10/L11/L12's readings (is a given
credit-block deterioration happening *alongside* a dated growth slowdown, or *ahead of* one?), and
it supplies a nowcast briefing surface for the Stage-2 runsheet (§A.4c), but it never itself moves a
rupee. This is the identical design move already made, for an analogous reason, for L11 inside the same
block (Tier C, `contribution_clamp: non_positive`) — except 2.3 does not even clear a reduce-only
clamp; it clears nothing, since a CONTEXT entry has no allocation slot to clamp in the first place.

---

### A.2 Theory, strongest form

**(i) The multiplier-accelerator, and its knife-edge problem.** **Samuelson, Paul A. (1939),
"Interactions between the Multiplier Analysis and the Principle of Acceleration"** (*Review of
Economics and Statistics* 21(2): 75–78) is the founding formal model of an *endogenous* business
cycle: combine the Keynesian consumption multiplier with the accelerator principle (investment
responds not to the *level* of output but to its *rate of change*, because firms invest to expand
capacity in proportion to expected demand growth), add a one-period lag structure, and the
resulting second-order linear difference equation in national income admits multiple qualitatively
different solution paths — damped, explosive, or perfectly periodic oscillation — depending purely
on the values of two parameters (the marginal propensity to consume and the accelerator
coefficient). **[Verified — Samuelson 1939, Review of Economics and Statistics; commonly termed the
Hansen-Samuelson model, crediting Alvin Hansen's inspiration.]** The famous **knife-edge problem**
is that the model's most interesting case — a *sustained, regular* cycle that neither dies out nor
explodes — occupies a **single boundary curve** in two-dimensional parameter space, a set of measure
zero; nudge either parameter fractionally and the economy settles to a steady state or blows up.
Nothing in the underlying economics pins the parameters to that razor's edge — the model's own
honest admission that a textbook-regular cycle is not what any real, noise-driven economy should
produce, a finding this program's own epistemics course (`docs/CYCLE_ATLAS.md` §0, citing Slutzky
1937 and Granger 1966) already treats as the reason "persistence, not periodicity" is the correct
frame for almost everything on the ladder, not just Atlas 2.3.

**(ii) Metzler's inventory refinement.** **Metzler, Lloyd A. (1941), "The Nature and Stability of
Inventory Cycles"** (*Review of Economic Statistics* 23: 113–129) supplies the mechanism that gives
the shortest-frequency end of the business-cycle band its own name (Atlas 2.4, Kitchin): firms hold
inventory toward a *desired* stock-to-expected-sales ratio, but expected sales are themselves
adaptively updated from realized sales, creating a genuine feedback loop distinct from Samuelson's
fixed-coefficient accelerator. Metzler's stability analysis identifies six qualitatively distinct
parameter regimes — from strictly damped to explosive to sustained oscillation — governed by how
aggressively firms restock relative to how quickly they revise their sales expectations.
**[Verified — Metzler 1941, Review of Economic Statistics; the six-regime classification is the
paper's own contribution, foundational to the inventory-cycle literature.]** For this program,
Metzler's inventories-as-accelerator finding justifies treating IIP momentum and order-book survey
data (OBICUS, cross-ref L11) as legitimate *nowcast* inputs (§A.3) — a genuine, fast-moving
amplifier of the underlying cycle, even where (as in India, per Atlas row 2.4's own verdict) too
data-thin to earn a seat of its own.

**(iii) Real Business Cycle theory, treated honestly — and monsoon as India's actual "technology
shock."** The Kydland-Prescott RBC program treats business cycles as the economy's *efficient*
response to real shocks — principally exogenous total-factor-productivity shocks — propagated
through an otherwise frictionless equilibrium growth model; time-to-build (Kydland-Prescott 1982)
is the specific propagation mechanism already fully treated at `research/cycles/capex-deep/
partA-theory-psychology.md` §A.2.2 and not re-derived here (cross-ref only, per this program's own
no-duplication discipline). The honest critique, stated at the time rather than only in hindsight:
**Summers, Lawrence H. (1986), "Some Skeptical Observations on Real Business Cycle Theory"**
(*Federal Reserve Bank of Minneapolis Quarterly Review* 10(4): 23–27) objects that "it's hard to
find direct evidence of the existence of large technological shocks" of the size and frequency RBC
models require to fit observed output volatility, and that Prescott's own defense amounted to a
"price-free" analysis unwilling to confront the demand-side, nominal-rigidity evidence Keynesians
already had in hand. **[Verified — Summers 1986, Minneapolis Fed Quarterly Review; both critiques
directly quoted/paraphrased from the paper's own record.]** For India, the RBC program has a
genuine, India-specific rescue that is also India's genuine, India-specific complication: **Banerjee,
Shesadri & Basu, Parantap (2019), "Technology Shocks and Business Cycles in India"** (*Macroeconomic
Dynamics* 23(5): 1721–1756) estimate a small-open-economy New Keynesian DSGE model on India's
1971–2010 annual data (with explicit pre-/post-1991 liberalization subsamples) and find total-factor-
productivity and investment-specific-technology shocks are the **first and second most important**
contributors to India's aggregate output fluctuations, ahead of the model's demand-side shocks.
**[Verified — Banerjee & Basu 2019, Macroeconomic Dynamics, published record.]** But "technology
shock" in an Indian estimation window that includes the pre-1991 decades is doing real interpretive
work that the phrase does not do in a US RBC estimation: India's classical contraction dates (§A.1iii)
line up overwhelmingly with **monsoon failures**, not with anything resembling an autonomous shift
in the aggregate production function. A bad monsoon cuts agricultural output directly, and — in an
economy where agriculture is a shrinking but still large employment share (roughly **15–18% of
GDP**, per D08 I10, against a far larger share of the workforce) — propagates through rural income,
consumption demand, and food-price inflation into a broad-based slowdown that a TFP-shock
econometric specification will happily label "negative technology" without the label meaning what
it means in a Kydland-Prescott factory-productivity story **[VERIFY: whether Banerjee-Basu's own
TFP series decomposes or controls for rainfall variation in the pre-1991 subsample — not confirmed
from the abstract-level search record this session]**. The honest reading: India's business cycle
has had **two different engines** — a pre-1991 engine substantially driven by a genuine, weather-
forced supply shock wearing an econometric "technology shock" costume, and a post-1991 engine
(Banerjee-Basu's own post-liberalization subsample) increasingly resembling the investment-
inventory-credit dynamics §A.2i–ii and §A.2iv describe — and the growth-cycle framing of §A.1iii is
what lets one dating methodology span both eras without conflating them.

**(iv) The New Keynesian synthesis.** **Clarida, Richard; Galí, Jordi & Gertler, Mark (1999), "The
Science of Monetary Policy: A New Keynesian Perspective"** (*Journal of Economic Literature* 37(4):
1661–1707) is the canonical statement of the synthesis this program's own L6 seat (monetary stance)
already operationalizes: demand shocks propagate through an economy with **nominal rigidities**
(sticky prices/wages), and a central bank's **policy rule** (implicitly or explicitly inflation-
targeting) is itself a first-order determinant of how those shocks resolve into output and inflation
dynamics — the business cycle, on this view, is jointly a real-shock and a monetary-policy-regime
phenomenon, never purely either. **[Verified — Clarida-Galí-Gertler 1999, Journal of Economic
Literature; also NBER Working Paper 7147.]** This is the scaffolding underneath L6's own construction
(repo-path stance, lagged ~1 year, D08 I2) and is not re-derived here beyond noting the implication
for Atlas 2.3: since 2016's inflation-targeting adoption, India's own monetary reaction function is a
first-order shaper of how any growth impulse — including a monsoon shock — resolves into the reading
this entry tracks, one more reason the entry is read *alongside* L6 rather than apart from it.

**(v) Credit-cycle coupling — Bernanke-Gertler-Gilchrist, by reference, and then the India twist.**
**Bernanke, Ben S.; Gertler, Mark & Gilchrist, Simon (1999), "The Financial Accelerator in a
Quantitative Business Cycle Framework"** (*Handbook of Macroeconomics*, Vol. 1, Ch. 21: 1341–1393)
is already fully treated at `docs/cycles/01-credit-cycle.md` §A.5 / `research/cycles/credit-deep/
partA-theory-psychology.md` §A.5 and is not re-derived here; in one sentence for context, the
mechanism is that borrower balance-sheet net worth is procyclical (rising in booms, falling in
busts), which moves the external finance premium inversely, amplifying an ordinary business-cycle
shock through the credit channel — **credit leads and amplifies the real cycle** in the mechanism's
own textbook statement, the same direction Minsky-Kindleberger-style narratives and much of the
international financial-cycle literature (Borio 2012, `research/cycles/fincycle-deep/
partA-theory-psychology.md` §A.1) assume as a matter of course. **The India twist, stated plainly:**
**Saini, Deepika; Ahmad, Wasim & Bekiros, Stelios (2021), "Understanding the Credit Cycle and
Business Cycle Dynamics in India"** (*International Review of Economics & Finance* 76: 988–1006)
use over 30 years of firm-level data and find the **opposite ordering** for India — **the business
cycle leads the credit cycle**, not the reverse: repo rate, broad money, the real exchange rate and
industrial output explain business-credit dynamics, credit destruction is more volatile than credit
creation, and excess credit reallocation is countercyclical. **[Verified — Saini, Ahmad & Bekiros
2021, International Review of Economics & Finance; already independently verified and cited in
this program's own D03 §I4.]** The design implication D03 already draws, restated here for the
business-cycle entry specifically: **do not import the international "credit leads, output
follows" causal ordering uncritically into an Indian model.** India's own working-capital-heavy,
bank-dominated lending system plausibly extends credit *in response to* demand that has already
shown up — banks lending against receivables and inventory that materialize once a firm is already
producing more, rather than credit expansion itself autonomously kicking off the boom — which would
make a leading indicator in the international literature a **lagging** one on India's own panel, a
possibility no amount of methodological rigor imported from elsewhere can rule out by assumption.

**(vi) Why direction imports are dangerous — and the desk's own trial on the point.** The general
lesson §A.2v teaches is not "India is different" as an article of faith; it is that **the direction
of a lead-lag relationship is itself an empirical claim, not a mechanism-derived certainty**, and a
relationship's *strength* (does credit growth forecast crises? — yes, robustly, per Schularick-
Taylor and Greenwood et al., already the L10 seat's own Tier-B/A evidence) is a logically separate
question from its *phase* (does credit growth lead or lag the business cycle's own turning points?
- an entirely different, cross-spectral question). This program pre-registered exactly that
phase question as **BC2** (`research/register/trial-ledger.md`; construction and bars detailed in
`research/cycles/buscycle-deep/partDEFH-math-algo-harvest-ledger.md` Part D) and the result, now run
(`research/cycles/buscycle-deep/buscycle-RESULTS.md`), is the single most important finding this
entry contributes: on the **JST R6 advanced-economy analogue panel** — the very panel the
international "credit leads growth" convention is drawn *from* — the peak cross-correlation between
the credit gap and the GDP gap sits at a **negative** lag (GDP gap leading the credit gap) in
**16 of 18 countries** (AUS, BEL, CAN, CHE, DEU, DNK, ESP, FIN, FRA, IRL, ITA, JPN, NLD, PRT, SWE,
USA all peak at lags of −3 to −5 years; only GBR at +3y and NOR at +5y show credit leading), against
a pre-registered bar of ≥60% showing a peak lag ≥+1y — a clean, decisive **FAIL** for the imported
direction, on its own home turf. Three honesty caveats travel with the finding, stated in the
results file and repeated here rather than smoothed over: the credit gap and GDP gap use different
Hamilton-filter horizons (h=5y vs h=2y), which can mechanically bias peak location toward the more
heavily-smoothed series appearing to lag; several country peaks pin at the −5y grid boundary, so the
true peak may lie further out than the grid could register; and the test reads peak *location* only,
not *strength* — a direction finding, not a magnitude one. None of these caveats rescue the imported
direction; they qualify how confidently the *opposite* direction should be asserted, not whether
"credit leads growth" survives. **The honest synthesis**: Saini et al.'s India finding that business
leads credit does not read, on this desk's own analogue evidence, as an Indian peculiarity — it
reads as compatible with, perhaps even the **general case**, once a real-time-safe, non-look-ahead
construction (this program's Hamilton-filter discipline, never BIS's HP version) replaces the
full-sample band-pass constructions the international literature typically uses. This does **not**
touch the credit gap's own crisis-warning role — J1's AUROC evidence (0.62–0.65 pooled,
`research/register/trial-ledger.md`) concerns whether an elevated credit gap predicts a *tail crisis
event* years out, a quantile-exceedance question distinct from a cross-spectral phase question, and
L10's seat rests on the former, untouched by BC2. What BC2 forecloses, permanently, is treating
"credit leads the business cycle at cycle frequency" as an assumption importable without a test — a
standing warning this file carries forward for every future imported lead-lag claim (§A.4b).

---

### A.3 Dating and nowcasting machinery

**(i) From Burns-Mitchell to a repeatable algorithm.** Burns-Mitchell's own comovement definition
(§A.1i) was never accompanied by a fully mechanical dating rule — turning points were identified by
trained judgment applied to many series at once. **Bry, Gerhard & Boschan, Charlotte (1971),
"Cyclical Analysis of Time Series: Selected Procedures and Computer Programs"** (NBER) closed that
gap: a computer routine that locates local peaks and troughs in a single series subject to minimum-
phase-length and minimum-amplitude rules, removing subjective judgment from turning-point location
while still reproducing NBER's own U.S. recession dates closely enough to serve as the *de facto*
standard — and, applying the identical rule regardless of country, the standard instrument for
comparable chronologies across very different national economies.
**[Verified — Bry & Boschan 1971, NBER; corroborated by multiple subsequent methodological
surveys.]** **Harding, Don & Pagan, Adrian (2002), "Dissecting the Cycle: A Methodological
Investigation"** (*Journal of Monetary Economics* 49(2): 365–381) supplies the statistical
foundation Bry-Boschan's own procedure lacked, formalizing a variant — commonly called **BBQ**
(Bry-Boschan Quarterly) — that links a series' *turning points* to its *moments* (mean growth,
volatility, serial correlation, asymmetry), letting a researcher decompose *why* a cycle looks the
way it does rather than merely locate where it turns. **[Verified — Harding & Pagan 2002, Journal of
Monetary Economics; BBQ is the now-standard implementation, e.g. the `BCDating` R package.]** This
program's own construction (`research/cycles/buscycle-deep/partDEFH-math-algo-harvest-ledger.md`
Part D; BC1–BC3, `buscycle-RESULTS.md`) departs from both in the same direction the sister L10/L12
constructions already do, for the same reason: an **expanding Hamilton (2018) regression gap**
(CONTRACT §8 bans the HP filter everywhere on this desk for its endpoint-revision problem) computed
using only information available as of each date, never a full-sample band-pass filter or a
turning-point rule calibrated with the benefit of hindsight — real-time honesty purchased at a
real, already-measured cost (the sister L12 monograph's own FC2 finding, `research/cycles/
fincycle-deep/jst-fincycle-RESULTS.md`, is the template for how much precision that trade gives up).

**(ii) Growth-cycle dating for India — the Dua-Banerji chronology.** **Dua, Pami & Banerji, Anirvan**
— Dua at the Delhi School of Economics and the Economic Cycle Research Institute (ECRI), New York;
Banerji at ECRI — built India's first systematic classical-and-growth-cycle chronology using the
NBER's own Bry-Boschan-descended procedure, first in **Dua & Banerji (1999)**, revised in
**Dua & Banerji (2004a), "Monitoring and Predicting Business and Growth Rate Cycles in the Indian
Economy,"** and further updated in **Dua & Banerji (2012), "Business and Growth Rate Cycles in
India"** (Delhi School of Economics, Centre for Development Economics Working Paper 210, January
2012); this chronology is also **the** ECRI chronology for India, i.e., the reference other India
business-cycle papers benchmark against. **[Verified — the Dua-Banerji research program's existence,
institutional affiliations, and the 1999/2004a/2012 citation chain, cross-confirmed across multiple
independent search results this session, including ECRI's own attribution.]** Two distinct
chronologies come out of this program, and the desk must not conflate them: a **growth-rate-cycle**
dating (turning points in the smoothed rate of IIP growth itself — the shortest, choppiest concept
in §A.1iii's hierarchy), for which Dua & Banerji (2012) report an average **speed-up phase of 5
quarters and slowdown phase of 6 quarters** over 1960–2010 (implying a growth-rate-cycle full length
on the order of 2.5–3 years, well below the classical business cycle's own typical span), with a
documented run of India turning points from **1991 onward** — troughs at (month/year) **September
1991, April 1993, November 1996, October 1998, July 2001, October 2004, March 2006, and January
2009**, each paired with an intervening peak — and a **growth-cycle** dating proper (turning points
in the *deviation of the level from trend*, coarser and longer than the rate cycle, closer to what
Atlas row 2.3's own "~4–5y avg" figure most plausibly reflects). **[VERIFY: the exact growth-cycle
(as opposed to growth-rate-cycle) peak/trough dates and average full-cycle length — this session's
access is via secondary summaries of the CDE/ECRI working papers, not a direct primary-document
fetch (`cdedse.org`/`nipfp.org.in` are blocked at the proxy, per CONTRACT §7 Known Prior #11); the
growth-rate-cycle figures above carry higher confidence, corroborated across several independent
secondary sources.]** The "~4–5 year" duration Atlas 2.3 itself carries is independently
corroborated, at the growth-cycle-adjacent (not rate-cycle) frequency, by two already-verified D03
citations: **Behera & Sharma (2019/2022)**, D03 I1, report average business-cycle duration **≈5
years** (vs. credit-cycle ≈15 years, quarterly turning-point/band-pass methods, 1996–2018);
**Garg & Sah (2024)**, D03 I3, report **≈4 years** (annual HP-filtered — a method CONTRACT bans for
this program's own design use, but which still corroborates the *magnitude*, 1980–2021) — two
independently-verified citations converging on 4–5 years despite different filters, frequencies and
windows, exactly the cross-method corroboration D03 I3 itself reads as meaningful ("the number is
not robust to method, only the *ordering* is"). **Counting completed cycles since 1991** is, honestly,
as boundary-sensitive as the sister L6/L10 counts on this ladder: depending on how a 1991–2020 span
with no classical recession is partitioned into episodes, the count sits at **n≈4–5**, a marginal
pass of the clock test rather than a clean one — the identical verdict D08 I1 reaches for the RBI
monetary cycle, for the same reason (no India series runs long enough, under one consistent regime,
to settle the count precisely). This program's own analogue trial, **BC1** (`buscycle-RESULTS.md`,
run on the JST
R6 panel's real-GDP-per-capita series, not India directly), independently corroborates the *band*:
median peak-to-peak spacing **6 years** (IQR 5–9y, n=301 spacings across 18 countries), with **65%**
of spacings falling in the pre-registered [3,7]-year window — a clean **PASS** against the bar set
before running, evidence that the business-cycle band Atlas 2.3 claims is a real, datable object at
the claimed frequency, even though the analogue panel is advanced-economy GDP, not India's own.
**The OECD's Composite Leading Indicator (CLI)** system independently extends this tradition to
India today: India is one of five non-member economies (with Brazil, China, Indonesia, South
Africa) for which the OECD compiles a CLI, built from ~10–15 component series evaluated against
**industrial production as the reference series for the growth cycle** — i.e., the OECD's own India
methodology adopts IIP as the growth-cycle anchor, the same series Dua-Banerji's chronology and this
program's own nowcast surface (§A.3iii) already lean on. **[Verified — OECD's CLI methodology
documentation; FRED's mirrored India CLI series `INDLOLITONOSTSAM`.]**

**(iii) The modern nowcast surface.** India's growth-cycle dating problem has a genuinely new,
post-2017 solution the Dua-Banerji-era chronology could not have used: **GST collections**. Monthly
gross GST collection data has been published since **July 2017**, free, and — because GST is a
transactions-based consumption tax collected from formal-sector activity across the entire economy
— it is a genuinely new, high-frequency **fiscal-consumption** signal with no pre-GST analogue in
India's data landscape. The RBI's own nowcasting research already treats it as load-bearing:
**Bhadury, Soumya; Ghosh, Saurabh & Kumar, Pankaj (2020), "Nowcasting Indian GDP growth using a
Dynamic Factor Model"** (RBI Working Paper Series, WPS (DEPR) 03/2020, February 2020) identify 12
high-frequency indicators — GST revenue among them — and extract a single dynamic factor from
6-, 9- and 12-indicator variants to produce an early, within-quarter GDP-growth estimate ahead of
the official print. **[Verified — RBI WPS (DEPR) 03/2020, published record, GST revenue confirmed
as one of the input indicators.]** The rest of the nowcast surface this entry catalogues, none of it
new in kind but several pieces newly free and high-frequency: **e-way bills** (mandatory
electronic waybills for inter-state goods movement, pan-India from **1 April 2018**, all states by
mid-June 2018; monthly generation volumes free via GST Council/CEIC data, a genuine physical-
movement proxy distinct from the GST revenue figure itself, since a bill is generated at dispatch
regardless of the eventual tax outcome) **[Verified — e-way bill launch dates, GST Council/CEIC
public data.]**; **OBICUS** (RBI's Order Books, Inventory and Capacity Utilisation Survey, quarterly
since ~2008, cross-ref L11 — this entry reads it as a growth-cycle input, L11 reads the same series
as its own capex-cycle input, and the two must never be double-counted, per §A.1iv); **IIP
momentum** (MOSPI's monthly Index of Industrial Production, the OECD's own chosen India reference
series for the growth cycle, §A.3ii); **PMI** (the S&P Global/HSBC-sponsored Purchasing Managers'
Index — a private survey, but its **headline number is released free** monthly by S&P Global press
release even though the full sub-index time series is a paid subscription product; a reading above
50 signals expansion, below 50 contraction, versus the prior month) **[Verified — S&P Global PMI
public press-release structure and free-headline/paid-detail split.]**; and, at the older, physical
end of the surface, **rail freight loading and electricity generation** — quantity-based proxies for
real activity that predate and require no national-accounts machinery, in the same spirit as the
informal cross-country practice of tracking physical throughput as a check against a headline GDP
print an observer distrusts. **Why the desk's use of all this is a nowcast BRIEFING (Stage-2
context), never a state**: every series either carries a short history (GST barely nine years old;
e-way bills barely eight), is subject to revision (IIP and GDP prints both revise after first
release), or is subscription-gated at full resolution (PMI's own sub-indices). None of that
disqualifies the surface from being useful — a monthly briefing table is the right register for
short, noisy, revision-prone series — but none of it clears the bar for a ladder seat (Tier B at
minimum, a stated `tau_half`, a defensible influence cap), and every series is, in any case, the
same correlated-shadow argument from §A.1iv: different windows onto the activity the macro block's
four seated entries already condition permission on.

---

### A.4 What the entry contributes without a seat

Atlas 2.3 carries **Tier B** evidence for the object itself — cycles at the business-cycle band
exist and are datable (BC1's clean PASS, §A.3ii) — with the honest n≈4–5 India count stated plainly
rather than rounded up. That evidence licenses three contributions, each earning its keep without a
budget line:

**(a) The growth-cycle chronology as the desk's event clock.** A dated sequence of India growth-cycle
slowdowns and speed-ups — Dua-Banerji's chronology, maintained by the cases chapter (a sibling
dossier; not re-derived here) — is the natural, independent **validation instrument** for every
seated macro-block entry's behavior: did L10's credit-block reading actually deteriorate around the
1996, 2001, or 2008–09 growth-cycle troughs, or lag them longer than theory predicts? Did L11's
capex-cycle state confirm the dated 2011–20 slowdown independently of L10's own twin-balance-sheet
narrative? This is the use `partDEFH-math-algo-harvest-ledger.md` Part F already registers as
designs **BD1**/**BD2** (sign-consistency of an IIP-based growth-rate state against the Dua-Banerji
chronology; a direct India credit-vs-IIP lead-lag test with matched filter horizons, closing BC2's
own §A.2vi caveat) — an event clock earns its cost by letting every *seated* entry be checked
against ground truth, without itself needing a seat.

**(b) The direction-of-causality caution as a standing registry warning.** §A.2v–vi's finding — the
imported "credit leads growth" direction fails a clean, pre-registered bar on its own home
advanced-economy panel (16/18 countries, negative peak lag) — is not a one-off curiosity. It is
written into the registry (`partDEFH-math-algo-harvest-ledger.md` Part H) as a **standing warning
attached to every future imported lead-lag claim**: a documented leading indicator somewhere is not
evidence it leads *here*, and — as BC2 shows — is not even reliable evidence it leads *there*, once
measured with a real-time-safe, non-look-ahead construction rather than the full-sample band-pass
filters that literature typically uses. This is Atlas 2.3's single most consequential contribution,
delivered by a CONTEXT entry that cost zero regime-score budget to produce.

**(c) The nowcast surface catalog, for the principal's runsheet.** §A.3iii's inventory — GST, e-way
bills, OBICUS, IIP momentum, PMI headline, rail freight, electricity — is handed to Stage 2 as a
standing monthly briefing table (`partDEFH...` Part E, Step 1), reporting **levels and ranks only**,
never a fitted turning-point call (Part G below).

| Mechanism | What it licenses | What nothing free/India-specific captures |
|---|---|---|
| Burns-Mitchell comovement (§A.1i) + Mintz growth-cycle concept (§A.1iii) | The correct *concept* — India is a growth-cycle, not classical, object post-1991 | A quantified, India-specific classical-recession model — moot, since India has had only one classical recession (2020) to model |
| Multiplier-accelerator / Metzler inventory dynamics (§A.2i–ii) | The theoretical case for IIP-momentum/OBICUS as legitimate nowcast inputs | An India-estimated accelerator coefficient — no free, firm-level investment panel exists to fit one |
| RBC / Banerjee-Basu TFP-IST decomposition (§A.2iii) | A partial account of pre-1991 dynamics (monsoon-as-shock) and post-1991 dynamics jointly | A rainfall-controlled re-estimate distinguishing genuine TFP shocks from monsoon-driven agricultural supply shocks in the pre-1991 subsample — flagged, not yet run |
| BGG financial accelerator, by reference (§A.2v) | The textbook direction to test against, not assume | An India-estimated external-finance-premium series — thin/gated per D03 I10, already flagged there |
| Saini-Ahmad-Bekiros + BC2 (§A.2v–vi) | The standing direction-of-causality warning (§A.4b) | A matched-filter, India-direct lead-lag re-test (design BD2, queued, not yet run) |
| Bry-Boschan/Harding-Pagan + Dua-Banerji chronology (§A.3i–ii) | The event clock (§A.4a) | The growth-cycle (as opposed to growth-rate-cycle) primary dating document, direct-fetched rather than secondary-summarized — network-blocked this session |
| GST/e-way/OBICUS/IIP/PMI nowcast surface (§A.3iii) | The Stage-2 briefing table (§A.4c) | Any of these as a fitted, budgeted signal — every one is a correlated shadow of the seated macro block (§A.1iv) |

---

## PART G — Operator psychology

Part A documents an object the desk will be tempted to trade on precisely because it is the most
*talked-about* macro construct in financial media, dinner-table conversation, and the desk's own
instinctive vocabulary — "the cycle is turning," "we're mid-cycle," "this looks late-cycle" — despite
carrying no ladder seat and, per §A.2vi's own finding, an imported causal direction that fails even
where it was supposedly discovered. That combination — maximal cultural salience, zero allocation
authority, and a home-literature direction claim this desk's own trial just falsified on its home
turf — is exactly the setup that produces confident narration standing in for disciplined
non-decision. This Part maps the failure modes that setup invites to the countermeasures already
built into Atlas 2.3's CONTEXT-only design.

### G.1 Recession-calling as career risk — the asymmetric-loss problem

**Mechanism.** Calling a recession that does not arrive costs a forecaster a quiet, largely
forgettable miss — one call among many, correctable next release. **Missing** a recession that does
arrive — staying constructive through a downturn every other desk called correctly — is a career-
defining, repeatedly-cited failure, wildly disproportionate to the actual forecasting error, since
recessions are rare, hard-to-time events even for economists whose full-time job is calling them.
**Scharfstein, David S. & Stein, Jeremy C. (1990), "Herd Behavior and
Investment"** (*American Economic Review* 80(3): 465–479) — already this program's own citation at
`research/cycles/commodity-deep/partA-theory-psychology.md` §G.3, for an analogous commodity-
supercycle-calling asymmetry, not re-derived here — formalizes exactly this reputational asymmetry:
an agent who cares how skilled they are *perceived* to be rationally prefers to fail
**conventionally** (miss the same way the consensus misses) over failing **unconventionally** (being
wrong alone), because unconventional wrong calls carry disproportionate reputational damage. Applied
to recession-calling specifically, this is the mechanism behind the wry, decades-old observation —
**Samuelson, Paul A., Newsweek column "Science and Stocks," 19 September 1966** — that "Wall Street
indexes have predicted nine out of the last five recessions" **[Verified — Quote Investigator's
sourced attribution to Samuelson's own 1966 Newsweek column; the popular modern variant substitutes
"economists" for "Wall Street indexes," a drift in wording this file states honestly rather than
attributing the substituted phrasing to Samuelson himself]**: forecasters, individually and
collectively, over-call recessions relative to their actual frequency precisely because the
asymmetric reputational cost of *missing* one pushes false-positive calls to be the individually
rational choice, exactly as Scharfstein-Stein's model predicts for any forecaster operating under
reputational rather than purely accuracy-scored incentives.

**Countermeasure.** Atlas 2.3 is built to make a discretionary recession call structurally
unnecessary for this desk: it is CONTEXT, feeding L6/L10/L11/L12's own regime-score budget as an
interpretive overlay, never a standalone directional trigger a human operator could be individually,
reputationally exposed for calling wrong. The register's own sign-consistency-over-decades judging
convention (already stated for the commodity entry, `commodity-deep` §G.3, and equally applicable
here) removes the discretionary call the asymmetric-loss problem needs to bite on — a desk graded on
whether a pre-registered bar passed or failed, not on whether a headline call proved prescient, has
no reputational cost to reading a BC2-style FAIL as a FAIL.

### G.2 The "two quarters" folk rule versus India's growth-cycle reality

**Mechanism.** **Shiskin, Julius (1974), op-ed, *The New York Times*** — then U.S. Bureau of Labor
Statistics Commissioner — proposed a laundry list of quantitative proxies for the NBER's own
qualitative recession definition, including "two consecutive quarters of decline in real GNP"
alongside depth criteria (a 1.5% real-income decline, a 15% employment decline) and diffusion
criteria (a decline spread across more than 75% of industries). **[Verified — Shiskin's 1974 NYT
op-ed, its full multi-criterion content, and the well-documented subsequent drift in which every
criterion except "two down quarters" fell away from popular usage, leaving that single rule as the
now-common lay definition of "recession."]** Two down quarters is a workable rule of thumb for an
economy that regularly posts absolute output declines — the U.S., whose classical cycle IS the
relevant object. Applied uncritically to India, the rule is close to **vacuous**: §A.1iii's own
count shows India has produced two consecutive quarters of GDP decline exactly **once** since
liberalization (2020, an exogenous pandemic shock, not an endogenous cyclical turn). A desk member
reflexively reaching for "two down quarters" will, correctly, almost never see it fire — and may
then wrongly conclude India's business cycle barely exists, rather than concluding (correctly, per
Mintz 1969 and Dua-Banerji, §A.1iii/A.3ii) that the classical-cycle concept simply does not fit
India's growth-cycle reality, where the operative object is a slowdown in the *rate* of growth, not
a decline in its *level*.

**Countermeasure.** Every design document this desk produces states the growth-cycle framing
explicitly and up front (§A.1iii), and the nowcast surface (§A.3iii) is built to report **percentile
ranks of growth-rate deceleration**, never a binary "recession: yes/no" flag keyed to the folk two-
quarters rule. The Dua-Banerji-descended event clock (§A.4a) is precisely the structural alternative
to reaching for an imported, ill-fitting classical-recession trigger: it dates *India's own* growth-
cycle turning points on India's own data, using the same NBER-descended methodology (Bry-Boschan/
Harding-Pagan, §A.3i) but calibrated to the concept (growth cycle) that actually fits India's
observed history rather than the concept (classical business cycle) that fits the U.S.'s.

### G.3 GDP-print theater — revisions, base effects, and the discrepancy debates

**Mechanism.** India's national accounts have twice, in the current decade's own memory, become the
subject of a genuinely public credibility debate rather than a quiet technical footnote.
**Subramanian, Arvind (2019), "India's GDP Mis-estimation: Likelihood, Magnitudes, Mechanisms, and
Implications"** (Harvard Center for International Development Working Paper No. 354, June 2019)
argued the 2015 GDP-methodology rebasing (base year 2011–12, replacing 2004–05) plausibly caused
official growth to be **overestimated by roughly 2.5 percentage points per year between 2011–12 and
2016–17** — his point estimate placed true growth near 4.5% against an official ~7%, 95% confidence
band roughly 3.5–5.5%. **[Verified — Subramanian's Harvard CID WP 354, its publication record and
headline figures.]** The Economic Advisory Council to the Prime Minister publicly disputed the
finding, noting Subramanian's own cross-country model mis-estimated growth for 51 other countries by
comparably wide margins in either direction — a genuinely contested debate stated factually, on both
sides, rather than adjudicated here **[Verified — the EAC-PM's public rebuttal via contemporaneous
press coverage; the primary EAC-PM technical paper itself not independently re-pulled this session —
VERIFY]**. A second, more recent version of the same credibility question is the **FY22–24
discrepancy debate**: India's national accounts carry a residual "discrepancies" line reconciling
production-side and expenditure-side GDP, and its magnitude and *sign* have swung sharply —
roughly **−₹4.47 lakh crore (FY22)**, **−₹3.80 lakh crore (FY23)**, **+₹2.59 lakh crore (FY24)**
**[VERIFY: press-coverage sourced, not an independently re-pulled primary NSO table; the FY23→FY24
sign flip is the feature multiple commentators flagged as unusual]**, alongside a widely-reported
**GDP-GVA gap** — FY24 real GDP growth roughly **8.2%** against real GVA growth roughly **7.2%**,
wider than prior years, attributed substantially to falling subsidy expenditure (net taxes on
products rising faster than value added) **[VERIFY: press-coverage sourced figures]**. None of this
settles whether India's growth is "really" over- or under-stated in either episode; it establishes
only that **the discrepancy item and the GDP-GVA gap are real, documented, recurring features of
the data**, not a one-off — a desk narrating a single quarterly print as decisive evidence of "the
cycle turning" is narrating a number with a documented, sometimes multi-point residual inside it.

**Countermeasure.** This program's own estimation standards (CONTRACT §9, "out-of-sample R² judged
against the historical-mean benchmark," purged/embargoed cross-validation) already discipline against
over-weighting any single print; Atlas 2.3's own construction compounds this by using an **expanding
Hamilton regression gap** (§A.3i) rather than a level or a point-in-time growth print, which
mechanically smooths a single quarter's discrepancy-driven noise into a longer, less print-sensitive
state read. The nowcast surface (§A.3iii) is deliberately multi-series — GST, e-way bills, OBICUS,
IIP, PMI, rail freight, electricity — precisely so that no single headline GDP print, however
contested its residual, is ever the sole input to the desk's own read of where the growth cycle
currently sits.

### G.4 Nowcast overconfidence — GST and IIP's own monthly noise

**Mechanism.** GST collections and e-way bill volumes are genuinely new, high-frequency, and free —
exactly the combination that invites a desk to treat a single month's print as more informative than
it is. Both series are short (GST barely nine years old; e-way bills barely eight) and affected by
base effects, filing-deadline shifts, rate-slab changes, and compliance-drive effects (a crackdown
on fake invoicing mechanically moves reported collections without any change in underlying activity)
— none of which a naive month-over-month reading distinguishes from a genuine inflection. IIP
carries the mirror-image, longer-standing version: it is revised after first release, volatile at
the sub-index level, and (D08 I3) its capital-goods component underwent a base-year change whose
splice discipline the register already flags. The overconfidence risk is structural: a genuinely
new, free, monthly source is exactly what a resource-constrained desk is tempted to lean on harder
than its short, noisy history supports.

**Countermeasure.** §A.3iii's own framing states the discipline directly: the nowcast surface reports
**levels and percentile ranks**, never a fitted turning-point call, and every series in it is
explicitly flagged with its short-history caveat wherever it is used. The design register's own
queued check (design **BD3**, `partDEFH...` Part F) — the incremental correlation of a GST-collections
nowcast against next-month IIP momentum — is registered with the explicit statement that "the post-
2017 sample [is] honestly short — n stated with every print," precisely so that no future user of
this surface can present a GST-based read without also seeing how few genuinely independent monthly
observations back it.

### G.5 The desk's own trap — narrating every market move as "the cycle turning"

**Mechanism.** Because the business cycle is the single most *discussed* macro object in financial
commentary — more than the credit cycle, more than the capex cycle, more than any single ladder
seat — it is also the easiest post-hoc narrative device for explaining an ordinary market move that
had nothing to do with any dated growth-cycle turn: a soft IIP print, a strong PMI headline, a
GST beat or miss, each becomes a ready-made explanation for a day's price action regardless of
whether the underlying series moved outside its own noise band. This mirrors G.1's career-risk
asymmetry: it costs a desk member nothing, reputationally, to say "the cycle is turning" on a slow
news day, and the claim is essentially unfalsifiable in real time given the object's own multi-
quarter dating lag (a growth-cycle peak is typically confirmed only well after the fact, exactly as
Dua-Banerji's own chronology is itself retrospective, §A.3ii) — an unfalsifiable, costless narrative
is precisely the kind that proliferates unchecked absent a structural guard.

**Countermeasure.** The CONTEXT-not-seat verdict itself (§A.1iv) is the guard: because Atlas 2.3
carries no allocation authority, no permission, no leverage or hedge trigger is ever legitimately
justified by a desk member's own narrative reading of "the cycle turning" — any actual portfolio
action must trace to a seated entry (L6/L10/L11/L12) whose own construction and evidence this file
has stated plainly, never to an unbudgeted, un-dated, in-the-moment growth-cycle call. The event
clock (§A.4a) is the specific antidote to the unfalsifiability problem: because the Dua-Banerji-
descended chronology is a pre-existing, methodologically fixed dating exercise (not something the
desk re-derives on the fly to fit a live narrative), any claim that "the cycle is turning right now"
can and must be checked against it after the fact, at the next scheduled review, rather than
accepted uncritically in the moment it is made.

### G.6 Countermeasures mapped

Five structural features carry this Part's actual work, and none asks the operator to be more
disciplined in the moment than Part A's own evidence justifies. **(1) CONTEXT-only expression**
(G.1, G.5) — no discretionary recession call and no narrated "cycle turn" can legitimately move the
book; only the four seated macro-block entries can. **(2) The growth-cycle framing, stated up
front** (G.2) — the desk is told, in writing, not to reach for a classical-recession trigger that
cannot fire on India's own post-1991 record. **(3) Multi-series, print-resistant construction**
(G.3) — the Hamilton-gap state and the nowcast surface jointly dilute any single contested print's
influence. **(4) Rank-only, short-history-flagged nowcasting** (G.4) — the surface never outputs a
fitted call, and every series carries its own sample-size caveat. **(5) A fixed-methodology event
clock** (G.5) — "the cycle is turning" is checkable after the fact against a chronology the desk did
not construct in the moment to fit the narrative.

### G.7 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Making a discretionary recession call to avoid the reputational cost of missing one | Scharfstein-Stein reputational herding; the Samuelson "nine of the last five recessions" pattern of systematic over-calling under asymmetric loss | Atlas 2.3 is CONTEXT with no allocation authority; the register's sign-consistency judging convention removes the discretionary call the asymmetry needs to bite on |
| Reaching for "two down quarters" and concluding India has no business cycle when it (almost) never fires | Shiskin's 1974 rule of thumb, built for a classical-cycle economy, misapplied to a growth-cycle economy | The growth-cycle framing (§A.1iii) is stated explicitly; the nowcast surface reports growth-rate deceleration ranks, never a binary recession flag |
| Treating a single contested GDP print (or its discrepancy residual) as decisive evidence of a cycle turn | The FY22–24 discrepancy swings and the Subramanian mis-estimation debate — both real, documented, unresolved features of the data | Expanding Hamilton-gap construction smooths single-print noise; the multi-series nowcast surface never depends on one headline number |
| Over-reading a single month's GST/e-way-bill/IIP print as a turning-point signal | Genuinely new, genuinely free, genuinely high-frequency data inviting overconfidence relative to its short, noisy history | Levels/ranks reported only, never a fitted call; every series flagged with its own short-history caveat; BD3's own honest "n stated with every print" discipline |
| Narrating an ordinary market move as "the cycle turning" on a slow news day | Costless, unfalsifiable-in-real-time narrative device; the business cycle's own multi-quarter confirmation lag hides the claim from immediate scrutiny | CONTEXT-only status means no action can trace to the narrative alone; the fixed-methodology event clock (Dua-Banerji chronology) makes the claim checkable after the fact |
| Assuming an imported lead-lag direction (e.g., "credit leads growth") applies in India without testing it | BC2: the imported direction fails even on its own home advanced-economy panel (16/18 negative peak lags) | The standing registry warning (§A.4b) attaches to every future imported lead-lag claim; direction is tested (BD2, queued), never assumed |

None of these six countermeasures asks the operator to privately judge, in real time, whether this
quarter's slowdown is finally the real one, whether this print's residual finally proves the
official number wrong, or whether the imported textbook direction finally applies here after all.
Each converts that judgment call into a structural non-decision — a CONTEXT-only budget line, a
stated growth-cycle framing, a smoothed multi-series construction, a rank-only surface, and a
standing, dated event clock and registry warning — made once, in the design, before the moment that
would have made the call hardest.

---

**Word count: 8,007**

---

# PART B — India's dated chronology and the case record

# PART B — India's growth-cycle dating and case record

*Business-cycle-proper monograph (atlas 2.3, no independent ladder seat — CONTEXT inside the shared
`macro_credit_block`, correlated with L6/L10/L11 per `docs/CYCLE_ATLAS.md` row 2.3 and
`config/ladder.yaml`) · Part B · v1.0 · 2026-09-02 · Author: Claude (research agent) for Ionic
quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part's job is narrow and deliberately non-duplicative: the
capex/investment side of India's real-activity cycles (OBICUS, IIP capital goods, GFCF/GDP,
UMPP/NHDP/SEZ/PLI detail, the 2011–2020 twin-balance-sheet decade's real-side chronology) is
**already covered in full** by `research/cycles/capex-deep/partB-cases.md` — cited here by name,
never re-derived. The credit-side chronology of the same decades (GNPA masking and the AQR forced
recognition, IL&FS, the CD ratio, the restructuring alphabet CDR→SDR→5:25→S4A→IBC) is **already
covered in full** by `research/cycles/credit-deep/partB-cross-country.md`'s own case #10 ("India,
2003–2018 in full detail") and by `research/dossiers/03-credit-financial-cycle.md` — cited here by
name, never re-derived. This Part's own subject is what neither sibling monograph owns: **the
growth-cycle dating problem itself** (when did India's business cycle actually turn, according to
whom, and how much do the competing chronologies disagree) and **the episode narrative told from
the activity side** — what IIP, GST-collection nowcasts, OBICUS, exports, and GDP/GVA prints
themselves did, quarter by quarter, independent of what the credit or capex aggregates were doing
underneath. Atlas row 2.3's own framing is the brief: "in India the *credit* cycle leads it less
than textbooks claim (Saini et al.: business leads credit here — direction NOT imported blindly)."
Style and evidentiary discipline follow `research/cycles/fincycle-deep/partB-cases.md` (the
financial-cycle monograph's own Part B, the house style for this series): numbers-forward, every
figure sourced, `[VERIFY]` where a search pass could not pin the primary release, disagreement
between chronologies presented as a finding rather than resolved by fiat — a desk that refuses
false precision should want to see two credible dating schemes disagree by a year or a quarter, not
have that disagreement silently averaged away.*

---

## B.1 India's dated chronology (the chapter's spine)

**Why a "spine," not a single timeline.** The Contract's own epistemics (`docs/CYCLE_ATLAS.md` §0)
insist that almost nothing in macro time series is a clock — and India's business cycle is the
single clearest illustration of that inside this entire atlas. At least four independent dating
efforts exist, built on different definitions (annual GDP sign, monthly classical peak-trough,
growth-*rate* deviation-from-trend, OECD-CLI-reference-series turning points), and **they do not
agree with each other**, not because one of them is wrong but because "recession" and "slowdown"
are being measured against different yardsticks. The table below is deliberately built as a single
object with every disagreement left visible, per this chapter's own brief.

### The master table

| Episode / window | Annual GDP sign (NSO/World Bank, FY-average) | Dua-Banerji classical business cycle (ECRI method, monthly) | Dua-Banerji growth-rate cycle (peak/trough) | OECD CLI (India, non-member panel) | RBI/NCAER dating apparatus |
|---|---|---|---|---|---|
| 1957–58 drought | **−1.2%** (FY58) — one of only four negative-annual-growth years in independent India's pre-1991 record | predates the Dua-Banerji (1999) sample window `[VERIFY: exact sample start year]` | predates sample | predates OECD CLI's India coverage (post-1990s construction) | predates any formal apparatus |
| 1965–67 back-to-back droughts | **−3.66%** (FY66); **−0.32%** (FY73, a separate later episode, not 1967 itself) — FY67 itself is **not** one of the four negative-annual-growth years, despite the "1965–67 droughts" framing commonly used | contraction dated **December 1964–November 1965** and a **second, separate** contraction **May 1966–April 1967** — i.e. Dua-Banerji's monthly method finds **two** distinct classical downturns inside the window a single annual FY66 print compresses into one negative year | predates the growth-rate-cycle sample's clean start (their published peak/trough list begins with the 1990s window) `[VERIFY]` | predates coverage | predates apparatus |
| 1972–75 | **−0.32%** (FY73) is the third of the four negative-annual-growth years | contraction **July 1972–May 1973**, and a **further, separate** contraction **December 1973–February 1975** (the 1973–74 oil shock) — again two classical downturns where the annual-sign method shows only one negative FY | predates the clean growth-rate-cycle window | predates coverage | predates apparatus |
| 1979–80 | **−5.2%** (FY80; some series show **−5.27%**) — the fourth and largest of the four negative-annual-growth years, following a second monsoon failure and the second oil shock | contraction **May 1979–March 1980** | predates the clean growth-rate-cycle window | predates coverage | predates apparatus |
| **1991 BoP crisis** | **NOT a negative-annual-growth year** — FY92 growth was still positive (recalled ~1.4% `[VERIFY: exact FY92 print]`); industrial growth alone fell to **0.3%** (1991–92) before recovering to **3.2%** (1992–93) | contraction dated **April 1991–September 1991** — Dua-Banerji's monthly classical method **does** find a recession here, even though the annual-average print never turns negative | growth-rate-cycle **trough dated September 1991** — the two Dua-Banerji series agree with each other (classical contraction ends exactly where the growth-rate trough is dated) even though neither agrees with the annual-sign method | India not yet in OECD's tracked panel this early | predates apparatus; this is the episode every popular retelling calls "the recession," and it is the one case in this table where the annual-GDP criterion and the monthly classical-cycle criterion give **opposite answers** — the single cleanest illustration in this whole chronology of why "was there a recession" depends entirely on which ruler is used |
| 1997–2002 long deceleration | No negative annual print; growth simply fell from 7.8% (1996–97) to **4.8%** (1997–98) per `capex-deep`'s own case 1, recovering only partially to 6.5% the following year | growth-rate-cycle **trough October 1998**, **peak March 2000** — the trough lands almost exactly on the East Asian-crisis-transmission year the capex chapter dates from the real side | same as classical column (Dua-Banerji publish one combined chronology for this window) | India's coverage in OECD's tracked non-member panel is not confidently dated to this early a window `[VERIFY]` | — |
| 2003–2008 boom | No negative print; this is the acceleration leg, not a contraction | growth-rate-cycle **peak January 2007** — sits almost exactly at OBICUS's own eventual all-time-high print (March 2011, *after* OBICUS starts) and at the capex chapter's own dated 2007–08 investment-rate peak | peak January 2007 | India by this point sits inside OECD's tracked panel (components weighted >50% toward monetary/financial-area series per OECD's own published methodology note) | — |
| 2008–09 GFC transmission | No negative annual print — GDP growth **slowed to 6.7% (FY09)** from a 9.4%/yr average over 2005–06 to 2007–08, not a contraction | this window sits between two of Dua-Banerji's published growth-rate-cycle points (their public chronology, built on data through roughly the mid-2000s, does not cleanly extend a peer-reviewed date into 2008–09 `[VERIFY: whether a later Dua-Banerji update covers this window]`) | — | OECD's CLI, mechanically, would show a sharp trough here given the export/IIP collapse described in B2 below `[VERIFY: exact OECD-dated India trough month for 2008–09]` | — |
| 2011–2013 policy-paralysis slowdown | No negative print; growth fell to a then-nine-year low of **6.5%** (FY12), with Q4 down to **5.3%** | not confidently located in a published Dua-Banerji update reachable this pass `[VERIFY]` | — | — | — |
| 2016–2020 long slide | No negative print until the terminal COVID quarter; sequence runs **8.0% (FY16) → 7.1% (FY17) → 6.7% (FY18)** → **4.2% (FY20)**, the lowest full-year print since FY09's 3.09% | not confidently located `[VERIFY]` | — | — | — |
| **2020 COVID** | **−6.6%** (FY21, per the January 2022 revised estimate; the original May-2021 provisional print was **−7.3%**, and a further reading elsewhere shows **−5.8%** `[VERIFY: reconcile the −7.3% / −6.6% / −5.8% vintages before any backtest use — this is a genuine, still-unreconciled multi-vintage revision chain, not a typo]`) — the fifth and by far the sharpest of India's negative-annual-growth years, and the only one inside the post-1991 quarterly-GDP-reporting era | a monthly classical dating almost certainly finds a contraction bracketing Q1 FY21 at minimum; no published Dua-Banerji-branded date for this specific window was located this pass `[VERIFY]` | — | OECD's CLI-based recession-indicator series for India (FRED mnemonic `INDREC`) is explicitly marked **DISCONTINUED**, and this desk could not confirm from this pass whether a dated India CLI trough for 2020 was ever formally published before discontinuation `[VERIFY]` | — |
| 2021–2026 new cycle | **8.7%** (FY22, provisional May-2022 print, itself down from a 9.2% January-2022 advance estimate) → **7.6%** (FY23) → **9.2%** (FY24, first-revised) → **6.5%** (FY25, second advance, **old 2011–12-base series**) → **7.1%** (FY25, **restated under the new 2022–23-base series** released 27 Feb 2026) → **7.6%** (FY26, estimated, new-base series) — **two different, internally consistent growth chronologies coexist for FY23–FY26 depending on which GDP base year is used, and they must never be spliced without adjustment** | no published chronology located reaching this far forward `[VERIFY: any 2020s Dua-Banerji update]` | — | — | — |

**Reading the disagreement, honestly.** Three separate things are happening in this table, and the
desk should hold all three at once rather than collapsing them into one number:

1. **The annual-GDP-sign method is the most conservative and the most cited, and it delivers a
   clean, low count**: exactly **four** negative-annual-growth years before 1991 (FY58 −1.2%, FY66
   −3.66%, FY73 −0.32%, FY80 −5.2%) — a figure independently corroborated across multiple
   compilations this pass — plus **one** post-1991 negative year (FY21). By this criterion alone,
   **1991 itself was never a classical recession** — a genuinely counter-intuitive finding given how
   uniformly "the 1991 crisis" is discussed as India's defining downturn, and precisely the kind of
   result Contract §12 requires this desk to keep rather than smooth over.
2. **Dua-Banerji's monthly classical (ECRI/NBER-style) method delivers a longer list and finds two
   things the annual method cannot**: it splits some single negative-annual-growth years into *two*
   separate classical contractions (1965–67 becomes Dec1964–Nov1965 *and* May1966–Apr1967; 1972–75
   becomes Jul1972–May1973 *and* Dec1973–Feb1975), and it **finds a genuine recession in 1991**
   (Apr–Sep 1991) that the annual-sign method misses entirely, because a sharp but short-lived
   monthly-level contraction can wash out in an FY average when the other months of the fiscal year
   were growing. Six classical contractions are dated this way through 1991: **Dec1964–Nov1965,
   May1966–Apr1967, Jul1972–May1973, Dec1973–Feb1975, May1979–Mar1980, Apr1991–Sep1991**
   `[VERIFY: primary Dua & Banerji (1999) dates, cross-checked here only against secondary academic
   summaries, not the original NBER-methodology working paper itself]`.
3. **The growth-rate-cycle method (also Dua-Banerji) measures something different again** — not
   contractions in the *level* of output, but slowdowns in its *rate of growth* relative to trend —
   and its own published peak/trough list (**troughs September 1991, April 1993, November 1996,
   October 1998, July 2001, October 2004; peaks April 1992, April 1995, September 1997, March 2000,
   April 2004, January 2007**) captures cycles the other two methods are simply not designed to see
   at all: a growth-rate slowdown from, say, 9% to 5% growth is a "cycle" on this definition even
   though GDP never once falls in level terms — precisely the 1997–2002 and 2011–2013 episodes this
   Part treats as full case studies below, neither of which registers on the annual-sign method and
   only the first of which is confidently graded here on the classical monthly method.

**The clock-test verdict, stated in Contract terms.** None of these chronologies, on their own,
clears the Contract's clock test (§4: ≥4 observed complete periods) for a *periodic* business cycle
— the growth-rate-cycle list above gives six peak-to-trough round trips across roughly fifty years,
which is a marginal pass on count alone but fails on stationarity grounds `[docs/CYCLE_ATLAS.md`'s
own Band-0 "learning note": each "period" here ran under a genuinely different policy and openness
regime (License-Raj administered economy pre-1991 vs. liberalized, market-credit economy after)`]`.
This is exactly why atlas row 2.3 gives the business cycle proper **no independent ladder seat** —
it lives as CONTEXT inside the shared `macro_credit_block`, correlated with L6 (monetary stance),
L10 (credit), and L11 (capex), never budgeted on its own. **The classical-recession question,
resolved as honestly as the record allows**: on the annual-GDP-sign criterion, India has had **five**
classical recessions since Independence — 1957–58, 1965–66, 1972–73, 1979–80, and 2020–21 — and
**not** 1991, whatever the popular narrative claims; on the monthly classical-cycle criterion, the
count is **six**, splitting two of those years into back-to-back downturns and adding 1991 as its
own genuine (if brief) recession. Both counts are defensible; neither is *the* answer; a desk that
needs one clean number here is asking the data for more precision than the data can honestly supply.
**On RBI/NCAER**: no US-NBER- or CEPR-Euro-Area-style formal Business Cycle Dating Committee exists
for India — a 2020-era piece explicitly posed the question "does India need a Business Cycle Dating
Committee?" and answered, implicitly, no (none has since been formed) `[VERIFY: thewire.in, exact
date]`. NCAER instead runs a **Business Confidence Index** and quarterly **Business Expectations
Survey** (continuously since **1991**) plus a **Monthly Economic Review**, none of which constitutes
a dated peak/trough chronology — they are sentiment and nowcast instruments, not a dating apparatus,
and should not be confused with one. **On OECD**: India has sat inside the OECD's tracked
non-member CLI panel (alongside Brazil, China, Indonesia, South Africa) with GDP as the reference
series since an April-2012 methodology change, monetary/financial-area components weighted over
50% of the selected series — but the FRED-hosted, OECD-based recession-indicator series
specifically constructed for India (`INDREC`) is explicitly marked **DISCONTINUED**, and this pass
could not confirm a clean, currently-maintained, publicly dated India CLI turning-point chronology
comparable to Dua-Banerji's academic one `[VERIFY: current OECD India CLI turning-point dates and
discontinuation year/reason]`.

**The design consequence this desk should draw, stated once and then held throughout the rest of
this chapter.** Because no single dating authority commands consensus — not even within one
academic pair's own body of work, which itself publishes a classical chronology and a growth-rate
chronology that measure genuinely different things — atlas row 2.3's decision to give the business
cycle proper **no independent ladder seat** is not a shortcut; it is the only defensible response to
a genuinely multi-valued dating problem. A composite regime score that tried to consume "the
business-cycle phase" as a single dated input would be forced to pick one chronology arbitrarily
and would then inherit that chronology's own blind spots (the annual-sign method missing 1991
entirely; the classical monthly method offering no published date past the mid-2000s this pass
could confirm). Reading the business cycle only as CONTEXT — correlated with, and folded into, L6's
monetary-stance read, L10's credit-cycle read, and L11's capex-cycle read, exactly as
`config/ladder.yaml` already specifies — lets the desk use *all* of these chronologies as
cross-checks on each other's timing without ever having to adjudicate which one is "true."

---

## B.2 Episodes from the activity side

Each episode below is read through what the growth cycle actually *did* — GDP/GVA, IIP, exports,
GST-collection nowcasts, OBICUS where it existed — and cross-referenced, never duplicated, against
the capex and credit monographs' own already-published detail for the same windows.

### 1. 1991 BoP crisis — the classical case, and the one this chapter's own dating table complicates

**The mechanics, briefly (fuller detail in `capex-deep`'s own case 1 preamble).** By early 1991,
India's foreign-exchange reserves had fallen to the point of financing barely **three weeks of
imports**; the government devalued the rupee in two steps, **1 and 3 July 1991**, and dismantled
the industrial-licensing ("License Raj") regime via the New Industrial Policy the same month.
**Import compression** — a surcharge on oil imports, cash-margin requirements on other imports —
was the immediate, deliberate policy lever used to defend the external balance, precisely the
"activity-side" mechanism this chapter owns: a BoP crisis resolved partly by *compressing demand
for imports*, which mechanically compresses the industrial activity that consumes imported inputs
and capital goods.

**What the activity indicators actually printed.** Industrial growth fell to **0.3% in 1991–92**
before recovering to **3.2% in 1992–93** — a real, visible IIP-level deceleration, even though (per
B1's own table) the *annual GDP* print never turned negative. One academic retrospective describes
the capacity-utilization decline across 1991–92 and 1992–93 as driven primarily by a **decline in
demand** (falling real sales growth), not a supply-side production constraint — the activity-side
signature of an economy where compressed imports and a sharp relative-price shock (devaluation)
were suppressing *demand* for industrial output, distinct from a credit-crunch-driven supply
contraction. The recovery that followed was sharp: output growth is described in the literature as
following a textbook **"J-curve"** — the expected dip, then a boom that peaked at **13% growth in
1995–96** `[VERIFY: precise sourcing and index for this 13% figure]`, vindicating the reform
program on its own terms.

**Why this episode is the chapter's own cleanest illustration of "the chronology disagrees, and
that's the finding."** Dua-Banerji's monthly classical method dates a genuine recession here,
**April–September 1991**, ending exactly where their independently-constructed growth-rate-cycle
trough is dated (**September 1991**) — internal consistency between the two Dua-Banerji series. But
the annual-GDP-sign method — the criterion this chapter's own B1 table uses to certify India's four
(pre-1991) and one (2020) classical recessions — does **not** find a recession in 1991 at all,
because the fiscal-year average never turns negative. Every popular account of "India's 1991
recession" is therefore correct on the monthly classical measure and, strictly, incorrect on the
annual-average measure this same chapter uses to certify 1957–58/1965–66/1972–73/1979–80/2020–21 as
recessions. This is not a contradiction to be resolved by picking a side — it is direct, textbook
confirmation of `docs/CYCLE_ATLAS.md`'s own epistemics section: "the honest object is not a clock ...
timing uncertainty is ±20% or worse." **Cross-reference discipline**: the *credit-side* legacy of
this episode (the NPA overhang, CDR born 2001, SICA/BIFR's weak 12–15% revival rate) is fully
covered in `capex-deep`'s own case 1 and is not re-derived here; this Part's job stops at what the
activity indicators themselves show.

### 2. 1997–2002 the long deceleration — East Asia, domestic capex bust, and the "Hindu rate" fear revival

**The activity-side story, cross-referenced to the capex chapter's own case 1.** India's growth
decelerated from **7.8% (1996–97) to 4.8% (1997–98)**, recovering only partially to 6.5% the
following year, as the July-1997 Asian financial crisis's regional currency and commodity-price
contagion reached an India whose own direct Asia-trade exposure was modest (Asia-directed exports
under 2% of GDP `[source: IMF/ADBI working paper, per capex-deep]`) but whose *domestic* capex boom
(the 1994–97 primary-equity-market mania funding greenfield steel, textile, and petrochemical
capacity) was simultaneously colliding with a global commodity-price collapse that compressed the
revenues of the very plants that boom had just built. The rupee depreciated **13.1% between April
and September 1998**. This is the single clearest case in the entire chronology of a *dual-cause*
slowdown — an external contagion shock landing on top of a domestic overbuild already primed to
correct — and it is precisely why the capex chapter's own case 1 and this chapter's own activity
read of the same years must be cross-checked, never merged into one number: the capex chapter dates
the investment-side bust; this chapter's own dating (B1) places the **growth-rate-cycle trough at
October 1998**, almost exactly the window the rupee-depreciation and commodity-collapse evidence
independently corroborates.

**IIP stagnation and the fear revival.** Industrial output growth across this window is
characterized in the literature (via the capex chapter's own sourcing) as running through a
multi-year stagnation, compounding a bust the boom itself had set up; this is also the period in
which fears of a reversion to the pre-1991 **"Hindu rate of growth"** (the roughly 3.5%/year
average pinned on India's License-Raj decades — Raj Krishna's own coinage) resurfaced in
contemporary commentary, only to be decisively falsified by the 2003–2008 boom this same
chronology dates next. **Nowcast variables of the era**: pre-OBICUS (which starts only in 2008),
the only free real-time activity read available for this window is IIP itself and the GFCF/GDP
ratio — precisely the measurement-gap the capex chapter's own §B1 documents in detail ("the boom
whose bust this desk most wants a utilization number for is the one era with no free,
machine-readable series at all"), a gap this chapter inherits rather than resolves.

### 3. 2003–2008 the boom — activity indicators at full throttle

**What led, from the activity side.** GFCF growth rose sharply from **8.2% (2002) to 17.5% (2004)**,
holding firm through 2003–07; investment grew faster than consumption across this window, and the
capex boom (fully detailed in `capex-deep`'s own case 2 — UMPPs, NHDP, SEZs, the Reliance Power IPO
top-tick) is described in the literature as directly triggering an acceleration in productivity,
job creation, and income growth — the activity-side transmission mechanism from investment to
broader GDP momentum. **Capital goods, specifically**, tripled in index terms between roughly 2005
and 2008, the sharpest sectoral acceleration inside this boom and the clearest single confirming
signal that the investment surge was translating into actual industrial throughput, not merely
financial-market enthusiasm. A mild deceleration appeared as early as 2007–08 — manufacturing and
construction, having grown at **12% in 2006–07**, decelerated by roughly **2.5 percentage points**
the following year, a soft early warning that arrived *before* the 2008 global crisis itself, though
this pass could not confirm whether that deceleration was independently significant or already the
leading edge of the GFC's transmission. **Dating cross-check**: this chapter's own growth-rate-cycle
peak (**January 2007**) sits almost exactly where the capex chapter's own OBICUS-adjacent evidence
places the boom's climax — even though OBICUS itself would not register its own all-time-high print
until March 2011, *after* the 2008 interruption, on the capex chapter's own telling of the "last
leg." The two chronologies (growth-rate-cycle peak dated from GDP/IIP momentum; OBICUS peak dated
from capacity utilization) disagree on the exact peak month by roughly four years — a genuinely
useful illustration that *which* activity series is used to date "the peak" materially changes the
answer, precisely the same lesson B1 draws for the recession count.

**Services alongside industry, briefly, for completeness.** This boom is popularly remembered as an
industrial/infrastructure story (the capex chapter's own UMPP/NHDP/SEZ/telecom detail), but the
services sector — IT/BPO exports, financial services, telecom subscriber growth — expanded
alongside it over the same 2003–2008 window, and a full services-side activity read (a
continuously published India services PMI did not yet exist this early; the closest free proxies
are services-sector GVA growth and IT-export receipts) is not attempted in this chapter, since
neither sibling monograph owns it either — flagged here as a genuine gap in this desk's own
three-monograph coverage of the 2003–08 boom, worth a future dossier rather than a retrofit into
this Part.

### 4. 2008–09 the transmission — the fast V

**The collapse, precisely dated.** India's exports slowed sharply in September 2008 and **turned
outright negative from October 2008 onward**, averaging roughly a **20% contraction** across
October 2008–September 2009. IIP itself registered **4.8% growth in September 2008** and then
**−0.41% in October 2008 — the first negative IIP print in fifteen years**. Manufacturing IIP,
which had grown **9.6% in FY2007–08**, slowed to **0.5% in Q3** and then **−0.16% in Q4 FY2008–09**
— a clean, fast, sequential deceleration inside a single fiscal year, the sharpest quarter-to-quarter
activity-side air-pocket in this entire chronology outside 2020. **Full-year GDP growth slowed to
6.7% (FY09)**, down from a **9.4%/year average across 2005–06 to 2007–08** — a material deceleration,
but, crucially, **not** a negative-annual-growth year, consistent with B1's own finding that no
classical recession is certified for this window on the annual-sign criterion. **The policy
response, sized.** RBI cut the repo rate from **9% (August 2008) to 4.75%**, reduced the CRR from
9% to 5%, and trimmed the SLR by one point to 24%; the government's fiscal stimulus is sized at
roughly **1.3% of GDP in 2008–09**, with a first package (subsidizing exporter interest costs)
announced **2 January 2009** and the 2009–10 Budget extending the expansionary stance. **The fast
V, measured.** Growth recovered to **7.4% (FY10)**, with the fourth quarter of FY2009–10 alone
printing **8.6%** — a genuinely rapid transmission-and-recovery cycle, and the capex chapter's own
cross-reference (Sensex −60 to −64%, Jan–Oct 2008, per the credit monograph's case #10) marks the
*equity*-side amplitude of the same shock, not recomputed here. **Nowcast lesson.** This episode is
the chronology's cleanest textbook demonstration of export/IIP data leading the GDP print by roughly
a quarter — precisely the kind of high-frequency activity signal (exports, monthly IIP) that a
GST-collections-style nowcast today would have caught in real time, years before GST itself existed
as an instrument. The counterfactual is worth stating explicitly for the data phase: had a monthly
GST-collections series existed in 2008 (it did not; GST itself is a 2017 instrument), the October
2008 export/IIP break would almost certainly have shown up as a matching collections air-pocket
inside the same one- to two-month window, given how tightly indirect-tax collections track nominal
transaction volume in a bank-dominated, working-capital-financed economy — the single strongest
argument this chronology supplies for why a modern activity-side nowcast (IIP momentum plus GST
collections growth, the pairing this Part's own B3 proposes testing in the BC2 trial) should react
faster to a trade-channel shock than either the quarterly GDP print or the credit aggregates
`credit-deep`'s own L10 construction is built on.

### 5. 2011–2013 the policy-paralysis slowdown — activity peaked before credit stress showed

**The activity-side chronology.** GDP growth fell from **7.8% at the start of 2011** to **6.1% in
the quarter ending December 2011**; full-year FY12 growth landed at a then-**nine-year low of
6.5%**, with Q4 FY12 down to **5.3%**. The IMF's own contemporary assessment attributed roughly
**two-thirds of the slowdown to internal factors — "policy paralysis"** — rather than the global
environment; the capex chapter's own case 3 dates the real-side stall in granular detail: an
estimated **$45 billion of investment held up** by clearance/land-acquisition bottlenecks, **154
Coal India projects** awaiting environmental clearance, and CMIE-sourced (paid-source, cited only
via secondary reporting per the Contract's free-data rule) new-project announcements collapsing to
a **14-year low**. **The Saini direction, visible in this record — framed carefully.** This episode
is the chronology's single clearest illustration of Saini, Seema, Ahmad, Wasim & Bekiros, Stelios
(2021)'s own headline finding (detailed in full in B3 below): India's **business cycle leads its
credit cycle**, not the reverse. The activity-side stall documented here — GFCF and IIP momentum
visibly turning down from 2011, capital-goods order books (BHEL, L&T, per the capex chapter's own
figures) already softening — **predates** the credit-side recognition event by a wide margin: the
Asset Quality Review that forced banks to reclassify the same-era stressed loans did not arrive
until **August 2015**, and public-sector-bank gross NPAs did not visibly jump (from ~5.0% to ~14.6%)
until March 2015–March 2018 (per `credit-deep`'s own case #10). **The activity engine had already
stalled for three to four years before the credit engine was forced to admit it.** This is exactly
the pattern Saini et al.'s pooled 1980–2021 annual-data result would predict — a genuine,
episode-level confirmation of an aggregate academic finding, not a coincidence — though this
chapter flags the framing carefully rather than overclaiming: Saini et al.'s own method uses an
HP filter (banned outright by this Contract, §8, for its endpoint-revision problem), so the
*direction* of the finding is usable as a literature prior, but the *exact lead time* they estimate
should not be imported uncritically into any purged India backtest without first re-deriving the
relationship on a Hamilton-filtered series, per this desk's own standing rule. **Cross-reference
discipline**: the credit-side mechanics of this decade (GNPA masking, the restructuring alphabet,
IL&FS) are fully covered in `capex-deep`'s own case 3 and `credit-deep`'s own case #10; this
Part's activity-side reading is additive, not a substitute.

### 6. 2016–2020 the long slide — demonetisation, GST, IL&FS, and the FY20 pre-COVID trough

**The sequence, dated precisely.** GDP growth ran **8.0% (FY16) → 7.1% (FY17) → 6.7% (FY18)**, a
visible multi-year deceleration layered directly on top of three discrete shocks: **demonetisation**
(8 November 2016, withdrawing the legal-tender status of ₹500/₹1,000 notes, estimated by
contemporary studies to have shaved **0.25–1.00 percentage points** off GDP growth); **GST**
(rolled out 1 July 2017, with growth slipping to a then-three-year low of **5.7% in the April–June
2017 quarter**, underscoring the rollout's disruption to manufacturing activity in particular); and
**IL&FS** (defaulting September 2018, ₹91,091 crore of debt, ~$13bn — fully detailed from the
credit side in `credit-deep`'s own case #10 and cross-referenced, not re-derived, here), whose
system-wide NBFC funding freeze is the shadow-credit event most directly implicated in choking off
the *real-estate and infrastructure* capex this chapter's sibling `capex-deep` monograph already
documents in detail. **The FY20 pre-COVID trough, verified with a correction to the task's own
figure.** Official FY20 (2019–20) GDP growth landed at **4.2%**, the lowest full-year print since
FY09's 3.09% — **not** 3.9% as this Part's original brief framed it; that lower figure does not
match any officially-confirmed vintage located this pass and should be treated as a misremembered
estimate rather than an NSO print `[VERIFY: whether 3.9% corresponds to some intermediate
advance-estimate vintage this pass could not locate; the confirmed final figure is 4.2%]`. The
quarterly sequence inside FY20 itself shows the deceleration compounding through the year: **5.0%
(Q1) → 5.1% (Q2) → 4.7% (Q3) → 3.1% (Q4)** — the Q4 print a **44-quarter low**, landing just as the
25 March 2020 COVID lockdown began, meaning the pre-COVID trough and the COVID shock itself overlap
by a matter of days rather than sitting cleanly apart. **The auto-sales collapse, 2019, verified.**
India's ₹57 billion (~$57bn `[VERIFY: currency framing]`) auto-component industry recorded its
worst-ever half-yearly performance, revenues down **10.1% year-on-year to ₹1.79 lakh crore in
FY20** — a structural slowdown attributed to a mix of regulatory change (axle-load norms, BS-VI
transition costs, the looming EV-policy shift) and the broader macro sputtering this section
documents; a subsequent SIAM-data retrospective (cited in industry press as "Covid-19 washes out
six years of growth in auto sales") frames the sector's full decline as compounding straight through
into the 2020 shock rather than resetting between the two episodes. **Nowcast lesson.** This is the
chronology's clearest illustration of a *slow-motion* activity-side deceleration — no single sharp
trigger comparable to 2008's export collapse or 2020's lockdown, but a compounding sequence of three
discrete policy shocks landing on an economy already decelerating on trend, precisely the kind of
episode a GST-collections nowcast (had it existed pre-2017) or an OBICUS percentile-rank read would
have flagged early and gradually, rather than with one dramatic print.

### 7. 2020 COVID — the one unambiguous classical recession

**The print, verified.** India's GDP contracted **23.9% year-on-year in Q1 FY21** (April–June
2020), per the National Statistical Office's original release (August 2020) — the first quarterly
GDP contraction since India began publishing quarterly data in 1996, and, by any of B1's competing
annual or monthly dating methods, the single most unambiguous classical recession in this entire
chronology. **Sectoral detail**: GVA fell **22.8%**, manufacturing **39.3%**, mining **23.3%** —
while **agriculture grew 3.4%**, the quarter's sole bright spot and, in hindsight, the first visible
thread of the K-shaped pattern this section closes with. **The full-year print, and its own
unreconciled revision chain (a genuine finding, not an error to be smoothed over).** FY21 full-year
GDP contraction was first estimated at **−7.7%** (January 2021 advance estimate), then **−7.3%**
(May 2021 provisional), then revised to **−6.6%** (January 2022) — and at least one further reading
locates the "final" figure closer to **−5.8%** `[VERIFY: this pass could not fully reconcile the
−7.3% / −6.6% / −5.8% vintages against a single, dated, primary NSO release table — treat this as
an open reconciliation task before any backtest uses the FY21 print, not as a settled number]`.
This is precisely the multi-vintage revision problem `capex-deep`'s own case 4 and this chapter's
own B1 table both flag for the 2020s data generally — GDP is not one number even for the single
most consequential print in modern Indian economic history. **The K-shaped recovery.** Aggregate
output recovered quickly in level terms (India "fully recovered the pre-pandemic real GDP level of
2019-20" by FY22, per the government's own May-2022 framing), but the recovery's *composition* was
sharply unequal: **richer households, listed corporates, and formal-sector workers gained
disproportionately**, while poor, informal, and MSME segments lagged — luxury vehicle and premium
housing sales surged even as rural FMCG and two-wheeler demand stayed subdued, and **MGNREGA
demand remained above its pre-COVID baseline** for an extended period, a direct, free, real-time
signal of continued rural-labor-market distress sitting underneath a recovering aggregate print.
Only from the second half of FY25 did rural consumption growth begin to outpace urban — reaching
**7.7% year-on-year in Q2 FY26**, a 17-quarter high — closing, at least partially and belatedly, the
K-shape this section documents opening.

### 8. 2021–2026 the new cycle — honest, undated

**The rebound, with vintages kept explicit.** GDP growth recovered to **8.7%** in FY22 (provisional,
May 2022; the initial January-2022 advance estimate had run higher, at 9.2%, before a February-2022
first revision to 8.8% and a further pare-down to 8.7%), followed by **7.6% (FY23)** and **9.2%
(FY24, first-revised)** on the long-standing **2011–12-base** GDP series. FY25 growth was estimated
at **6.5%** on that same old-base series (NSO's own May-2025 second advance estimate) — but on **27
February 2026** the NSO released a wholesale GDP methodology revision, rebasing to **2022–23** and
simultaneously revising CPI to a 2024 base and IIP to a 2022–23 base; under the new series, FY25
growth is restated at **7.1%**, and FY26 is estimated at **7.6%** (tying, per the government's own
framing, for the sharpest expansion since FY22). The rebasing also lowered the *level* of nominal
GDP materially: government estimates put 2022–23 GDP roughly **2.9% lower** and both 2023–24 and
2024–25 roughly **3.8% lower** than under the old series — meaning FY23–FY26 now carries **two
internally-consistent but mutually incompatible growth chronologies**, and this chapter flags the
same splice-discipline warning `capex-deep` and `credit-deep` both already carry for their own
2020s-era rebase risks: **never compute a multi-year CAGR, backtest window, or purged-CV fold that
silently spans the old-base and new-base series without an explicit, documented adjustment.** Back-
series data reconciling the two vintages is not expected until **December 2026** per the NSO's own
release schedule. **The discrepancy-item debate.** India's national accounts "discrepancies" line
(production-side vs. expenditure-side GDP, the balancing residual) has swung sharply: **−₹4.47 lakh
crore (FY22) → −₹3.80 lakh crore (FY23) → +₹2.59 lakh crore (FY24)**, a magnitude and sign
volatility that has itself become a subject of public debate about India's GDP measurement quality.
A separate, contested academic study (name and exact authorship **not independently verified this
pass** `[VERIFY: full citation]`) argues that officially-reported growth for **2005–2011** may have
been *understated* by roughly 1–1.5 percentage points while growth for **2012–2023** was
*overstated* by roughly 1.5–2 percentage points, implying an actual 2011–2023 trend growth rate
nearer **4–4.5%/year** against the official ~6% average — a genuinely contested, high-stakes claim
this chapter records as a live debate, not a settled finding, precisely because Contract §12
requires keeping unverifiable-but-notable findings with an explicit flag rather than either
suppressing or asserting them. **Where the growth cycle plausibly stands, 2026 — honestly, and
undated.** FY26's real GDP growth estimate of 7.6% is described as tied for the sharpest since FY22,
with private final consumption expenditure accelerating to **7.7% (FY26) from 5.8% (FY25)** and
gross fixed capital formation picking up; the services sector is projected at **8.9%** growth, with
trade/hotels/transport/communication at **10.3%**. Rural consumption's own recent acceleration
(7.7% YoY, Q2 FY26, a 17-quarter high) is attributed to income-support schemes, favorable rainfall,
NBFC-led credit expansion, easing input costs, and steady MSPs — a composition that, on its face,
looks like a genuine broadening beyond the narrow, capex-driven, urban-skewed recovery of 2021–24.
**The desk does not need to resolve whether this constitutes a new, self-sustaining growth-cycle
upswing or a mid-cycle plateau before the model can be built** — precisely the same design
discipline `capex-deep`'s own case 4 already establishes for L11's non-positive contribution clamp:
atlas row 2.3 gives the business cycle proper no independent budget seat of its own, so a genuinely
unresolvable "where are we now" question here is a non-issue for portfolio construction, exactly as
intended.

---

## B.3 The direction-of-causality record

**The India-specific finding, cited precisely.** Saini, Seema, Ahmad, Wasim & Bekiros, Stelios
(2021), "Understanding the credit cycle and business cycle dynamics in India," *International
Review of Economics & Finance*, vol. 76, pp. 988–1006, uses annual data spanning **1980–2021**,
extracts business, credit, and investment cycles via the **Hodrick-Prescott filter** `[flagged
explicitly: this Contract bans the HP filter outright, §8, for its endpoint-revision problem — the
paper's methodology cannot be adopted wholesale by this desk, only its directional finding, pending
a Hamilton-filter re-derivation]`, and applies structural VAR and Granger-causality tests. Its
headline result: **the business cycle leads the credit cycle in India, at both the aggregate and
sectoral level** — average business-cycle duration runs roughly **4 years** against a credit-cycle
duration of roughly **3 years**, and the SVAR analysis further confirms a long-run relationship
among business, investment, and credit cycles jointly, with domestic and global financial cycles
shown to *diverge* from one another over the sample. A related, earlier-vintage RBI working paper —
**Krittika Banerjee, "Credit and Growth Cycles in India: An Empirical Assessment of the Lead and Lag
Behaviour"** (RBI Working Paper Series, No. 22 `[VERIFY: exact year]`) — examines the same lead-lag
question via a distinct methodology, and a more recent 2024 extension, **"Cyclical dynamics and
co-movement of business, credit, and investment cycles: empirical evidence from India"**
(*Humanities and Social Sciences Communications*, 2024), broadens the same question to explicit
co-movement analysis across all three cycle types — both are noted here as corroborating strands
`[VERIFY: exact findings of each, not independently re-derived from primary sources this pass]`,
not as independently re-verified results this chapter can stand behind at the same confidence level
as the Saini et al. headline finding above.

**The regime-dependence nuance — itself a finding, not a contradiction.** A separate line of
inquiry into India's credit-output causality (exact authorship not confidently pinned this pass)
examines three distinct sub-periods — **1950–51 to 1979–80, 1980–81 to 1990–91, and post-1991** —
and finds a genuine **structural break in the direction of causality itself**: credit was
predominantly *driving* output in the **pre-1980s, administered-credit era** (when bank lending was
directed by policy/priority-sector mandates rather than market-determined working-capital demand);
the relationship weakened to **near-zero** through the **1980s**; and in the **post-reforms period**,
causality runs **predominantly from output to credit** — i.e. the same direction Saini et al.'s own
2021 paper finds for its own overlapping post-1991 sample. **These two findings do not contradict
each other once the regime break is made explicit; they corroborate.** The mechanism that explains
both: pre-1980s India ran a heavily administered credit-allocation system in which the *quantum* of
credit was a policy lever largely independent of realized output — credit could genuinely drive
activity because it was rationed by fiat, not drawn against realized sales. Post-liberalization,
India's bank-dominated corporate lending runs overwhelmingly through **working-capital instruments**
(cash-credit accounts, overdraft facilities, working-capital demand loans) drawn against realized
turnover, inventory, and receivables — a genuinely different *mechanism* of credit extension from
the long-duration, asset-financed leverage (mortgages, corporate bonds, project finance drawn ahead
of realized cash flow) that dominates the rich-country panels the BIS/Borio literature is built on.
A working-capital-drawn-against-sales system is, almost by construction, an *accommodating* variable
that validates activity after the fact rather than a *driving* variable that creates activity ahead
of it — which is precisely why India's post-reform direction (business leads credit) can coexist,
without contradiction, with a genuinely different average pattern in the rich-country panel.

**The BIS/advanced-economy contrast, stated carefully.** The pooled international literature this
desk's own credit and financial-cycle monographs already lean on (Borio 2014; Claessens, Kose &
Terrones 2011/2012; Drehmann-Borio-Tsatsaronis) finds that in advanced economies, **recessions
coinciding with the contractionary phase of the financial cycle are roughly twice as severe** as
those that do not, and the credit/property/equity co-movement documented at FC1 in the
`fincycle-deep` monograph (median correlation +0.40, 17-of-17 countries positive) is built on
samples where credit *amplifies* the business cycle's amplitude, typically *around or ahead of* the
cycle's own turning points, rather than trailing behind it. This pattern rests on financing
mechanisms — long-tenor mortgage debt inflating property prices which in turn collateralizes further
lending, corporate bond issuance financing capex years ahead of realized demand — that are
structurally different in kind from India's own working-capital-dominated corporate credit system.
**The design implication, stated plainly**: this desk should not import the BIS/advanced-economy
"credit leads and amplifies" prior into India's own L10 credit-cycle construction as a *timing*
assumption — `config/ladder.yaml`'s own L10 entry already treats India's credit-cycle AUROC prior
(0.65–0.75) as a haircut against the pooled advanced-economy AUROC (0.83–0.85) for exactly this
reason, and this chapter's own case 5 (2011–2013) supplies the cleanest available India-specific
confirmation of *why* the haircut is directionally correct: the activity engine stalled years before
the credit engine was forced to admit it, the opposite sequencing the rich-country panel would
predict.

**What the desk's BC2 analogue trial would add.** No `research/cycles/buscycle-deep/buscycle-RESULTS.md`
file exists as of this writing — this chapter therefore proposes, by name only, a **BC2** trial
analogous in spirit to the credit monograph's own JST-panel work and the capex chapter's own
pre-registered IN1–IN3 analogue trials: a purged-and-embargoed test of whether an activity-nowcast
composite (IIP momentum, a GST-collections growth nowcast, and the OBICUS percentile rank) leads
L10's own Hamilton-filtered credit/GDP gap by roughly two to four quarters in India's post-1991
sample, against the null that the two move contemporaneously — the direct India-specific,
Hamilton-filtered (never HP-filtered) re-test that Saini et al.'s own HP-filter-based finding cannot,
on its own, license this desk to treat as pre-validated. Should that file come to exist by the time
a future revision of this chapter is written, its numbers should be cited directly here, exactly as
`capex-RESULTS.md`'s IN1–IN3 numbers are cited directly throughout `capex-deep`'s own Part B.

> **[Desk note, added at assembly (2026-09-02, principal's edit — the trials landed while this
> chapter was being written):** `buscycle-RESULTS.md` now exists. The BC2 that was RUN is the
> analogue-panel version (JST, 18 countries): peak cross-correlation lag between the credit gap
> (h=5) and the GDP gap (h=2) — and the imported direction FAILED at home: only 2/18 countries
> (11%, vs a pre-registered 60% bar) show credit leading at +1y or more; 16/18 peak at −3..−5y,
> i.e. the GDP gap leads. Caveats (differential smoothing, grid-edge pinning, location-only) are
> logged with the print. The India-specific purged test this paragraph proposes remains the
> right NEXT step and is registered as design **BD2** (matched h on both legs, magnitude floor)
> in Part F.]**

**A direct connection to the ladder's own phase-object representation.** The principal's 2026-09-01
decision (`research/OPEN_QUESTIONS.md`) to represent every ladder state as a phase object — level,
velocity, quadrant (recovery/boom/slowdown/downturn), age-in-quadrant — rather than a bare scalar is
directly informed by this chapter's own case 5. A scalar "credit is tight" or "credit is loose"
reading of 2011–2013 would have shown nothing unusual until 2015; a *quadrant* reading of the
activity-side state (L11's own capex/OBICUS input, L6's monetary stance) would have shown a clear
transition from boom to slowdown quadrant years earlier, exactly the state the Saini direction says
should be watched **instead of** waiting on the credit aggregate. This is not a case for giving the
business cycle its own ladder seat — atlas row 2.3's CONTEXT-only verdict stands — but it is a case
for making sure L6, L10, and L11's own phase quadrants are read jointly rather than any one being
treated as sufficient on its own, since this chapter's own record shows the activity-side quadrant
can lead the credit-side quadrant by years in exactly the episode where it would have mattered most.

---

## B.4 Synthesis table

| Episode | Growth-cycle dates (source) | Classical? | What led (activity / credit / policy / external) | Nowcast variables that saw it early | Seated-state cross-refs |
|---|---|---|---|---|---|
| **1957–58 drought** | Annual GDP −1.2% (FY58); pre-dates Dua-Banerji sample | **Yes** (annual-sign method) | External/agricultural — monsoon failure, no credit-cycle mechanism | None constructible (pre-modern-data era) | None (pre-dates the ladder's entire evidence base) |
| **1965–67 droughts** | Annual GDP −3.66% (FY66); Dua-Banerji classical: **two** separate contractions, Dec1964–Nov1965 and May1966–Apr1967 | **Yes** (both methods, though the classical method finds two downturns where the annual method finds one) | External/agricultural (food-grain production −20% in FY66) plus 1965 war-recovery drag | None constructible | None |
| **1972–75 (oil shock)** | Annual GDP −0.32% (FY73); Dua-Banerji classical: **two** contractions, Jul1972–May1973 and Dec1973–Feb1975 | **Yes** | External (1973–74 oil shock) layered on a domestic agricultural shortfall | None constructible | None |
| **1979–80 (BoP precursor)** | Annual GDP −5.2%/−5.27% (FY80); Dua-Banerji classical: May1979–Mar1980 | **Yes** — the largest pre-1991 contraction on record | Second monsoon failure + second oil shock; direct BoP-crisis precursor to 1980s external borrowing | None constructible | None |
| **1991 BoP crisis** | Annual GDP **positive** (no recession on this criterion); Dua-Banerji classical: **Apr–Sep 1991**; growth-rate-cycle trough **Sep 1991** | **Disputed** — Yes on the monthly classical method; **No** on the annual-sign method (B1's own central finding) | Policy/external jointly: reserve depletion → devaluation → import compression → IIP-level (not GDP-level) contraction | IIP (industrial growth 0.3% FY92 vs. 3.2% FY93) — the cleanest activity signal this early | Predates the ladder entirely; retrospectively informs L9 (global-cycle EM-stress channel) and L6 (monetary-regime-change context) |
| **1997–2002 long deceleration** | Growth-rate-cycle trough Oct1998, peak Mar2000 | No (no negative annual print; a growth-*rate* slowdown only) | External (Asian-crisis contagion, commodity collapse) landing on a domestic capex overbuild (cross-ref `capex-deep` case 1) | IIP stagnation, rupee depreciation (13.1%, Apr–Sep 1998) | L9 (global financial cycle transmission); L11 (capex, reduce-only, via `capex-deep` case 1) |
| **2003–2008 boom** | Growth-rate-cycle peak Jan2007 | N/A (acceleration leg) | Activity/capex-led: GFCF 8.2%→17.5% (2002–04), capital-goods index ~3x (2005–08) | GFCF/GDP ratio, IIP capital goods (cross-ref `capex-deep` case 2) | L11 (capex, clamped reduce-only); L10 (credit, via `credit-deep` case #10) |
| **2008–09 GFC transmission** | Not cleanly dated in the published Dua-Banerji chronology located this pass `[VERIFY]` | No (GDP growth slowed to 6.7%, FY09; no negative print) | External (trade-channel shock) — exports −20% avg, IIP −0.41% (Oct2008, first negative in 15y) — met by a fast, large monetary+fiscal response | Monthly exports, monthly IIP — both led the GDP print by roughly a quarter | L9 (global financial cycle); L6 (monetary stance, repo 9%→4.75%) |
| **2011–2013 policy-paralysis slowdown** | Not cleanly located in a published update `[VERIFY]` | No (GDP fell to a then-nine-year-low 6.5%, FY12; no negative print) | **Activity-led, credit-lagged** — the Saini direction: GFCF/capex/order-books stalled 2011–13; credit stress (AQR) not forced into the open until Aug 2015 | OBICUS, IIP capital goods, capital-goods order books (BHEL, L&T; cross-ref `capex-deep` case 3) | L11 (capex, clamped); L10 (credit — the lagging-confirm-only design this episode directly validates) |
| **2016–2020 long slide** | Not cleanly located `[VERIFY]` | No (until the terminal COVID quarter; FY20 4.2% is the era's trough, not a negative print) | Policy-shock-led: demonetisation (Nov2016) → GST (Jul2017) → IL&FS (Sep2018), compounding on top of a decelerating trend | GST-collection nowcast (post-2017 only), auto-sales data (−10.1% component-industry revenue, FY20), quarterly GDP sequence itself (5.0%→3.1%) | L10 (credit, IL&FS sub-cycle per `credit-deep`); L11 (capex, real-estate/NBFC freeze per `capex-deep` case 3) |
| **2020 COVID** | The one episode every dating method agrees is a classical recession | **Yes — unambiguous** | External/policy (lockdown-driven demand destruction), not a credit- or capex-cycle event at all | Real-time mobility/activity proxies (not free-sourced this pass); the GDP print itself (−23.9% Q1 FY21) arrived with the usual 2-month NSO lag | Outside every ladder seat's normal mechanism — a pure exogenous shock, not a state the ladder was designed to anticipate |
| **2021–2026 new cycle** | No published chronology reaches this far forward `[VERIFY]` | No; genuinely undated per this chapter's own B2 §8 | Contested/mixed: public capex (2021–24) → private-capex-revival debate (cross-ref `capex-deep` case 4) → rural-consumption broadening (2025–26) | GST-collections nowcast, OBICUS (mid-70s band), rural-vs-urban consumption growth split | L11 (capex, clamped — `capex-deep` case 4's own non-monotonic IN3 result); L10 (credit, GNPA at a multi-decade low, 2.15%) |

**The verdict, stated as plainly as the record allows.** Atlas row 2.3's own framing — that in
India "the credit cycle leads [the business cycle] less than textbooks claim" — is not merely
defensible on this record, it is the record's single most consistently corroborated finding: every
episode above where a clean lead-lag read is possible (1991's IIP-vs-GDP disagreement, the
2011–2013 activity-before-credit-recognition gap, the post-1991 direction found independently by
Saini et al. and by the regime-break study in B3) points the same way. What this chapter adds to
that finding, rather than merely repeating it, is the **dating disagreement itself as a first-class
result**: five different, defensible chronologies of "when did India's business cycle turn" coexist
in the literature and in this desk's own search pass, and they certify different recession counts
(four vs. five vs. six classical recessions, depending entirely on method) for the identical
underlying fifty-year history. No single number from B1's table should ever be quoted alone in a
future dossier without naming which method produced it — precisely the discipline this chapter's
own construction is meant to instill before the ladder consumes any activity-side input.

---

## References

Dua, P. & Banerji, A. (1999), original India classical-cycle and growth-rate-cycle dating; Dua, P.
(2012), "Business and Growth Rate Cycles in India," CDE Working Paper 210, Centre for Development
Economics, Delhi School of Economics `[VERIFY: exact original 1999 citation — this pass located
and cross-checked secondary academic summaries and later CDE/NIPFP working papers citing the
original dates, not the 1999 primary source directly]`. · NIPFP Working Paper 221, "Business Cycle
Measurement in India"; NIPFP Working Paper 175 (2016), "Dating Business Cycles in India." · Saini,
S., Ahmad, W. & Bekiros, S. (2021), "Understanding the credit cycle and business cycle dynamics in
India," *International Review of Economics & Finance*, 76: 988–1006. · Banerjee, K., "Credit and
Growth Cycles in India: An Empirical Assessment of the Lead and Lag Behaviour," RBI Working Paper
Series `[VERIFY: exact number/year]`. · "Cyclical dynamics and co-movement of business, credit, and
investment cycles: empirical evidence from India," *Humanities and Social Sciences Communications*
(2024). · OECD, *Composite Leading Indicators* methodology notes and India non-member-panel
documentation; FRED series `INDREC` (OECD-based recession indicator for India, discontinued) and
`INDLOLITOTRGYSAM`/`INDLOLITOTRSTSAM` (CLI trend-restored series). · NCAER, *Business Confidence
Index* and *Business Expectations Survey* (continuous since 1991); NCAER *Monthly Economic Review*.
· NSO/MOSPI, quarterly and annual GDP press releases (various vintages, 2020–2026, including the 27
February 2026 base-year-2022–23 revision and its FAQ document); Economic Survey (various years,
including 2019-20 and 2020-21 summaries). · World Bank, *GDP growth (annual %) — India*; ICRIER,
*India's Economic Growth History* occasional paper. · IMF, *Article IV Consultation, India* (2013);
IMF blog, "India's Slowdown May Have a Silver Lining" (2012). · Business Standard, BusinessToday,
National Herald, and other contemporary financial-press coverage of the Q1 FY21 GDP print, the FY20
slowdown, the FY22–FY26 growth sequence, and the 2026 GDP base-year revision, cited throughout with
figures cross-checked across multiple independent sources where possible. · `research/CONTRACT.md`;
`docs/CYCLE_ATLAS.md` row 2.3; `config/ladder.yaml` (L6/L10/L11/L12 entries, `macro_credit_block`);
`research/dossiers/08-india-mid-cycles.md` (house style; capex/real-estate double-counting flags
directly relevant to this chapter's own capex/credit cross-references). ·
`research/cycles/capex-deep/partB-cases.md` (India's capex/investment-side chronology, 1994–2026;
cross-referenced throughout, never duplicated). · `research/cycles/credit-deep/partB-cross-country.md`
(case #10, "India, 2003–2018 in full detail" — the credit-side mechanics for the same decades;
cross-referenced throughout, never duplicated). · `research/cycles/fincycle-deep/partB-cases.md`
(house style for this series; FC1's own credit-property co-movement finding, cited by contrast in
B3 above).

---

*Word count: 8,257 (prose and tables, excluding front matter fencing and this notice).*

---

# PART B-RESULTS — Analogue data: JST R6 (BC1–BC3, pre-registered)

# Atlas 2.3 — business cycle: JST analogue trials (BC1-BC3, pre-registered)

State: expanding Hamilton gap of log real GDP per capita (h=2y — the short-cycle band's
own h, declared at registration), expanding percentiles. Bars fixed before running;
interpretation AFTER the print.

## BC1 — growth-cycle spacing vs the 4-5y claim

- n = 301 peak-to-peak spacings; median **6y**, IQR 5-9y; share in [3,7]y: **65%**.
- Bar (median in [3,6] AND ≥50% in [3,7]): **PASS**.

## BC2 — does the credit gap LEAD the GDP gap on its home panel?

| Country | peak cross-corr lag (+ = credit leads, years) |
|---|---|
| AUS | -5 |
| BEL | -3 |
| CAN | -5 |
| CHE | -5 |
| DEU | -5 |
| DNK | -3 |
| ESP | -4 |
| FIN | -5 |
| FRA | -5 |
| GBR | +3 |
| IRL | -5 |
| ITA | -3 |
| JPN | -3 |
| NLD | -5 |
| NOR | +5 |
| PRT | -4 |
| SWE | -5 |
| USA | -5 |

- Share with peak lag ≥ +1y: **11%** of 18 (bar ≥60%): **FAIL**.

## BC3 — growth-state persistence (measurement, prior set)

- P(state stays on the same side of 0.5 next year), pooled: **77%**.

## Honest read (written AFTER the print)

- **BC1 PASS:** growth-cycle arcs at median 6y spacing (65% in [3,7]y) — the business-cycle
  band exists on the analogue panel with our short-h machinery; the object is real and datable,
  which is all a CONTEXT entry needs.
- **BC2 is the striking one: the imported direction fails ON ITS HOME PANEL.** 16/18 countries
  peak at NEGATIVE lags (mostly −3..−5): at business-cycle frequency, with real-time gap
  constructions, the GDP gap leads the credit gap almost everywhere — the "banks lend after
  demand shows up" reading (Saini et al.'s India finding) looks like the GENERAL case, not an
  Indian anomaly. Three honesty caveats, stated with the finding: (i) this does NOT touch the
  credit gap's crisis-warning role — J1's AUROC (0.62-0.65, tail events years ahead) is a
  different claim than cycle-frequency lead-lag, and L10 is seated on the former; (ii) the two
  gaps use different h (5 vs 2) — differential smoothing can shift cross-correlation peaks;
  (iii) many peaks pin at −5, the grid boundary, and peak LOCATION was registered without a
  magnitude threshold — locations only, no strength claim. None of these rescue the imported
  direction: whatever the mechanics, "credit leads the business cycle" cannot be assumed.
- **BC3 (prior set): 77% one-year stickiness** — growth regimes persist like inflation eras
  (IR2's 81%), supporting state-style (not print-chasing) consumption in briefings.
- **Design consequence (feeds Parts D-H):** a STANDING REGISTRY WARNING — imported lead-lag
  directions are hypotheses, never assumptions; L10's authority is tail-warning and state
  conditioning, not business-cycle timing. The CONTEXT-no-seat verdict for 2.3 is reinforced:
  the growth cycle is real, sticky, datable — and already shadowed by the seated macro states.

---

# Parts D–H — context machinery, the standing warning, harvest (atlas 2.3; CONTEXT entry)

## Part D — The mathematics

**D1. What BC1–BC3 permit.** BC1 (median 6y spacing, 65% in [3,7]y) establishes the OBJECT:
growth cycles exist on real-time machinery at the claimed band. BC3 (77% stickiness) says the
object is a REGIME (persists year-over-year), so briefing language should be state-shaped, not
print-shaped. BC2 establishes what may NOT be assumed: at cycle frequency the credit gap does
not lead the GDP gap on the advanced-economy panel (16/18 negative peak lags) — the imported
direction dies at home, and India's Saini finding reads as the general case.

**D2. The lead-lag caveats, formalized once.** Cross-correlation peak location between two
DIFFERENTLY-FILTERED series (h=5 credit vs h=2 GDP) is biased toward the smoother series
appearing to lag; peaks pinned at the −5 grid edge mean "≤ −5", not "= −5"; and location
without magnitude is a direction reading, not a strength reading. These caveats are recorded
WITH the finding — and none rescue the import, because the import's claim was direction.
Distinction preserved in writing: J1's crisis-AUROC (levels of the credit gap predicting TAIL
events years out) is untouched by BC2 — leading a crisis and leading the cycle are different
mathematical objects (quantile exceedance vs cross-spectral phase).

**D3. Why no seat, in one line of budget algebra.** The macro block's information set already
spans money (L6), credit (L10), capex (L11), property (L12); a growth state built from IIP/GST/
OBICUS would correlate with all four inside the SAME 0.20 budget — a fifth claim on weight
carrying mostly duplicated information. CONTEXT costs zero budget and keeps the chronology.

## Part E — The algorithm (a briefing, not a state)

```
STEP 1  nowcast surface (runsheet: IIP momentum, GST collections, e-way bills, PMI headline,
        rail freight, electricity; OBICUS cross-ref L11) — monthly briefing table, PIT-stamped
STEP 2  growth-rate-cycle read: expanding percentile of the IIP momentum family (shared
        grids) — published as CONTEXT lines in the Stage-2 brief; NO regime-score path exists
STEP 3  event clock: the dated chronology (Part B's master table) drives seat VALIDATION
        studies (how did L10/L11/L12 states behave around dated slowdowns) — designs BD1/BD2
STEP 4  the standing warning travels with every lead-lag claim in any future entry: imported
        directions are hypotheses to test (BC2's print is the citation), never assumptions
MONITOR annual re-run of BC1-BC3; chronology updates when Dua-Banerji/OECD revise; nowcast
        surface freshness in the sentinel
FAILURE MODES: GDP-print revisions re-dating episodes (chronology rows carry vintage tags);
        nowcast overfitting (the brief reports levels/ranks, never fitted turning-point calls)
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| Stage-2 briefings | the monthly nowcast table + growth-regime context line |
| Seat validation | the event clock (dated chronology) for L10/L11/L12 behavior studies |
| Registry | the STANDING WARNING on imported lead-lag directions (BC2 print attached) |
| Cycle School | Lesson 18: a real cycle that earns no seat; direction imports die at home |

Designs: **BD1** India growth-rate-cycle state on IIP (once pulled): acceptance = sign-
consistency of turning points with the Dua-Banerji chronology (dates within ±2q), registered
before the look. **BD2** the direct India lead-lag (credit vs IIP gaps, our constructions,
matched h on BOTH legs to close D2's caveat): direction read with a pre-registered magnitude
floor this time. **BD3** GST-collections nowcast value: incremental correlation of GST z vs
IIP momentum one month ahead (post-2017 sample honestly short — n stated with every print).

## Part H — Knowledge ledger (atlas 2.3)

**Established (analogues, our runs):** growth cycles exist at the 3-7y band (BC1); they persist
(BC3, 77%); the credit gap does NOT lead the GDP gap at cycle frequency on the home panel
(BC2, 16/18 negative) — the entry's exportable finding. **India [chronology]:** the dated
record is the cases chapter's master table; classical recessions are rare (2020 the clean
modern case) — growth-cycle language is the correct dialect here. **Unknowable:** the current
cycle's position with nowcast precision — the brief reports ranks, never turning-point calls.
**Process:** a CONTEXT entry with zero budget cost still produced a major registry-level
finding (BC2) — the atlas discipline of running trials even for unseated entries pays.
