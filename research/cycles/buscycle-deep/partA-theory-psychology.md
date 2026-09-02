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
