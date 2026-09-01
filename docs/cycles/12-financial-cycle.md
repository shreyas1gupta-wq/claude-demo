# The Financial Cycle — Full Monograph (Atlas 1.1, seat L12)

v1.0 · 2026-09-01 · Band 1 opener, full seated treatment. Seat: L12 inside the macro_credit
block (0.20, SHARED — the de-duplication rule is this monograph's spine). Code:
`quant/ladder/financial_cycle.py` (4 tests incl. the graceful-degradation path for India's
short HPI). Chapter sources in `research/cycles/fincycle-deep/`.

Headline real-data results (FC1-FC3): credit-property amplification holds in 17/17 countries
(median corr +0.40 — the cleanest sign-consistency pass in the project, the exact contrast to
demographics' 4/16); cycle length direction 11y→13y post-1985 (Drehmann-Borio's lengthening on
our cruder tool — feeds H65b); crisis-at-PEAK dating honestly weak on our real-time construction
(1.2-1.3x) — the seat's own measured evidence for its states-never-dates rule. India: one
completed cycle, an invisible 2013-2020 real-price correction, and a short HPI whose degradation
path is designed and tested, not apologized for.

## Contents
- Part A+G — Borio/Drehmann in full, the property-collateral mechanics, the equity translation
  evidence-graded, the L10 de-duplication discipline, India double-weight, homevoter psychology
- Part B — the global house-price record + eight property-bust cases + India in full
- Part B-RESULTS — FC1-FC3 computed by us (with the FC3 honesty table)
- Part C — RBI HPI / RESIDEX / housing-credit engineering, supply-side confirms, the pipeline
- Part D/E/F/H — degradation semantics, the de-dup algebra, the algorithm, designs FN1-FN4

---


---

# PART A + G — Theory (Borio's synthesis, collateral mechanics) and operator psychology

# Medium-Term Financial Cycle Deep Dive — Part A & Part G

Part A: Theory — the financial cycle as credit and collateral breathing together · Part G:
Operator psychology · v1.0 · 2026-09-01 · Atlas entry 1.1 (`docs/CYCLE_ATLAS.md` row 62; ladder
seat `L12_realestate_medium_cycle`, `config/ladder.yaml`). SEATED inside the `macro_credit_block`
alongside `L6_monetary_stance`, `L10_credit_block`, `L11_capex_cycle` (`docs/DESIGN.md` §4.1–4.2).
Complements, never duplicates, `docs/cycles/01-credit-cycle.md` (the assembled L10 credit-cycle
monograph, especially its Part A §A.4 Kiyotaki-Moore, §A.9 Mian-Sufi, and its B1.8 Baron-Verner-
Xiong case) and this program's own `research/cycles/fincycle-deep/jst-fincycle-RESULTS.md`
(FC1–FC3: 17/17-country co-movement at median +0.40; peak-spacing lengthening 11y→13y on our own
construction; crisis-at-peak elevation honestly weak at 1.2–1.3x). Evidence base: this file +
`research/dossiers/03-credit-financial-cycle.md` (D03, esp. F1/F9), `research/dossiers/
07-long-waves.md` (D07, §D), `research/dossiers/08-india-mid-cycles.md` (D08, §I5/F7). Style and
depth calibrated to `research/cycles/debt-deep/partA-theory-psychology.md`. Status: theory/
citations verified here; India coefficients await the data phase.

This file assumes the ladder's frozen construct as given: L12 is a **phase-uncertainty prior**,
never a date — it reads RBI HPI, housing credit (sectoral deployment), and RBI FSR inputs against
L10's credit-block output (`inputs: [L10_credit_block]`), Tier B on the cross-country mechanism
and Tier C on India's own cycle length (n≈1), τ½ 60–96 months, sharing the 20%-of-regime-score
`macro_credit_block` budget with L6, L10 and L11 under the de-duplication rule (§4.2 below) —
never a separate allocation. Part A supplies the theoretical machine that construct compresses
into three inputs, honest about what the compression discards. Part G turns to the desk operating
a seat built on the one household asset every Indian investor already holds an outsized,
undiversifiable, sentimentally-loaded position in.

---

## PART A — Theory: the financial cycle as credit and collateral breathing together

### A.1 Borio's synthesis — definition, stylized facts, and the policy-regime precondition

**(i) Mechanism.** **Borio, Claudio (2012), "The Financial Cycle and Macroeconomics: What Have We
Learnt?"** (BIS Working Paper No. 395, December 2012; also *Journal of Banking & Finance* 45
(2014): 182–198) reframes the object macro-finance should actually be watching. Business-cycle
theory treats output gaps as the state variable that matters; Borio's claim is that a slower-
moving, larger-amplitude **financial cycle** — self-reinforcing interactions between *perceptions
of value and risk*, *attitudes toward risk*, and *financing constraints* — sits underneath it and
periodically overwhelms it. Operationally, Borio identifies the financial cycle with the **joint,
medium-term co-movement of credit and property prices**: in his own words, equity prices "do not
fit this picture well" internationally — they move at business-cycle frequency and correlate only
loosely with credit, whereas credit and property prices amplify each other on the multi-year
horizon that generates genuine crises. The mechanism chain is exactly Kiyotaki-Moore's collateral
loop (A.3 below) run at macro scale: easy credit bids up property, richer collateral values
support more credit, banks' own risk perception eases as losses stay low through the upswing, and
the loop only reverses when debt-service growth outruns income growth — at which point the same
amplification runs in reverse, faster than it built.

**(ii) The stylized facts.** Four, stated as Borio states them: **(a) length** — post-1985
liberalization-era financial cycles run materially longer than the traditional business cycle,
commonly cited in the **8–20-year range**, averaging roughly **16 years** across the post-1960
sample (the precise pre/post split is A.2's territory); **(b) amplitude** — the length increase
came with a **growth in amplitude**, i.e. these are not just slower business cycles, they overshoot
and undershoot further; **(c) crisis clustering** — financial-cycle **peaks coincide closely with
financial crises or serious banking-system stress**, and recessions that overlap a financial-cycle
contraction are systematically **deeper and more protracted** than recessions that do not; **(d)
the business-cycle/financial-cycle distinction** — the two objects can and do diverge: an economy
can run a healthy business-cycle expansion (rising output, contained CPI inflation) while its
financial cycle is quietly building toward an unsustainable peak, which is precisely why a central
bank watching only the output gap and near-term inflation can miss the more dangerous imbalance
building under its own read of "good times."

**(iii) The policy-regime precondition — why the cycle lengthened.** Borio's own explanation for
stylized fact (a) is not mechanical drift; it names two joint preconditions. **Financial
liberalization** (credit-market deregulation, interest-rate decontrol, capital-account opening from
the mid-1980s) relaxed the financing constraints that used to cap how far a credit boom could run.
Separately and jointly, **credible, anchored low inflation** — the post-Volcker, post-inflation-
targeting monetary regime — removed the traditional early-warning signal: a monetary authority
whose reaction function responds to near-term CPI inflation alone will not tighten against a credit
and asset-price boom that leaves consumer-price inflation low and stable, because nothing in its
own mandate is firing. Financial imbalances can build for years precisely *because* inflation stays
well-behaved — indeed positive supply-side developments (globalization, productivity gains) can
fuel both the credit boom and the low-inflation backdrop simultaneously, so the two preconditions
reinforce rather than merely coincide. **For our seat**, this is the reason L12's construction can
never be a fixed-length prior: the mechanism that sets the cycle's length is itself regime-
dependent (liberalization depth, monetary-framework credibility), and India's own liberalization
(1991 onward) and inflation-targeting regime (formally adopted 2016) are each barely one cycle old
— which is exactly why the India-length entry stays Tier C (§A.7) even as the cross-country
mechanism stays Tier B.

**(iv) Citations.** Borio, Claudio (2012), "The Financial Cycle and Macroeconomics: What Have We
Learnt?," BIS Working Paper No. 395 **[Verified — bis.org/publ/work395]**; republished *Journal of
Banking & Finance* 45 (2014): 182–198 **[Verified]**.

---

### A.2 Drehmann-Borio-Tsatsaronis — measurement, and why our own construction uses neither

**(i) Method.** **Drehmann, Mathias; Borio, Claudio & Tsatsaronis, Kostas (2012), "Characterising
the Financial Cycle: Don't Lose Sight of the Medium Term!"** (BIS Working Paper No. 380, June
2012) is the measurement paper underneath A.1's stylized facts, and uses **two independent
methods** on quarterly credit, credit/GDP, house-price and equity-price series for seven advanced
economies since 1960: **turning-point analysis** (a Bry-Boschan-style algorithm that dates local
peaks and troughs directly on the level series, requiring minimum phase-length and amplitude
rules) and **frequency-based band-pass filtering** (isolating the 8–30-year frequency band as the
"financial cycle" component, per Christiano-Fitzgerald/Baxter-King methodology). The two methods
broadly agree: financial-cycle duration averages **16 years across the full sample**, but only
**~11 years on pre-1998 data** versus **~20 years post-1998** — the length-and-amplitude increase
A.1 attributes to liberalization and low-inflation credibility. Financial-cycle peaks in this
measurement are the objects that cluster with crises (A.1c).

**(ii) Why our own construction uses neither.** Both methods carry a property this program has
already ruled out for the sister L10 seat: band-pass filters need the **full sample, including
future data**, to compute a mid-sample point, and both methods require choosing a target frequency
band or minimum-phase-length rule *ex ante* — exactly the "fitted to what we already know" risk
CONTRACT §8 bans the HP filter for, extended here to its band-pass cousins. Turning-point dating
additionally needs enough completed peak-trough pairs to calibrate its minimum-duration rule
reliably; with India's own single observed leg (A.7), there is nothing to calibrate it against
domestically. L12's construction instead **inherits L10's expanding Hamilton regression**
(`docs/cycles/01-credit-cycle.md` §4) applied to the property leg — house-price and housing-credit
series regressed on their own trailing values only, at each date using only information available
at that date, never revised by later data. This buys real-time honesty at a real cost, already
measured and stated plainly in this program's own results: **FC2** (`jst-fincycle-RESULTS.md`)
finds the combined credit+property expanding-Hamilton state's peak-to-peak spacing running
**pre-1985 median 11y (n=33) → post-1985 median 13y (n=32)** — the correct *direction* against
Drehmann-Borio-Tsatsaronis's own ~11y→~20y finding, but at roughly half the post-liberalization
magnitude. This program's own pre-registered check (H65b, `ladder.yaml
tau_half_drift_policy`) was the **direction**, not the level — and the direction holds — but the
gap between 13y and ~20y is the honest cost of a real-time-safe, crude expanding construction next
to a full-sample band-pass filter that has already seen the whole cycle. **This is FC2's crude-
tool caveat, stated here rather than buried**: nothing about L12's construction should be read as
matching Drehmann-Borio-Tsatsaronis's precision — it deliberately trades precision for the no-
look-ahead property the traded book actually needs.

**(iii) For our seat.** The Hamilton `h` grid pre-registered for L10 (16–24 quarters, R4 in D03's
design table) is inherited rather than re-derived for the property leg; L12's own design register
(when the data phase opens) must re-run the CD-ratio-style redundancy check (L10's R5) against the
house-price leg specifically, since property and credit gaps may span genuinely different
information (A.6) rather than redundant ones.

**(iv) Citations.** Drehmann, Mathias; Borio, Claudio & Tsatsaronis, Kostas (2012), "Characterising
the Financial Cycle: Don't Lose Sight of the Medium Term!," BIS Working Paper No. 380 **[Verified
— bis.org/publ/work380; also D03 F1]**.

---

### A.3 Why property is the collateral, part I — Kiyotaki-Moore recap and the supply-lag argument

**(i) Mechanism — Kiyotaki-Moore, by reference.** The credit monograph's §A.4 already establishes
the formal collateral-amplification mechanism in full: a durable asset that is simultaneously a
factor of production *and* the only thing that unlocks borrowing capacity produces amplification
because tomorrow's expected collateral value (`q_{t+1}`) sits on the right-hand side of *today's*
borrowing constraint (`b_t ≤ m·q_{t+1}·k_t/R`), and `q_{t+1}` is itself set recursively by
aggregate collateral demand next period. This file does not re-derive it; L12 inherits it wholesale
and asks the question Kiyotaki-Moore's own framework poses but does not answer on its own: *why is
property specifically* the collateral asset whose cycle is worth a dedicated seat, rather than
equities, inventory, or plant and machinery?

**(ii) The one structural argument that survives — supply elasticity.** **Glaeser, Edward L.;
Gyourko, Joseph & Saiz, Albert (2008), "Housing Supply and Housing Bubbles"** (*Journal of Urban
Economics* 64(2): 198–217) supplies the answer this program treats as load-bearing (D07 §D9,
already flagged there as "the one genuinely structural, not folk-numerological, argument in this
section"). Their model and cross-city US evidence show housing-**supply elasticity** — how quickly
new construction can respond to a price signal, itself set by land-use regulation and geography —
is the key structural moderator of both bubble size and bubble length: supply-**inelastic** markets
see larger, longer price run-ups and correspondingly sharper busts, while supply-**elastic** markets
self-correct faster with smaller swings, because new supply arrives quickly enough to meet demand
before price expectations become self-fulfilling. The mechanism is a genuine **capacity limit**,
not a behavioral bias or an arbitrage-competable mispricing: permitting, land acquisition and
construction of new housing stock take **years** regardless of how loudly the price signal is
shouting, so credit-fueled demand surges cannot be met quickly — mechanically generating a multi-
year cycle length that a purely credit- or sentiment-driven asset (which can reprice in days) does
not share. This is precisely why property, uniquely among collateral classes, carries its **own**
multi-year cycle length distinct from and longer than the underlying credit cycle it amplifies —
the empirical basis for the 10–20-year RANGE this program insists on (never the fixed "18-year"
point estimate; see G.4 below and D07 §D11's full treatment of that folk claim).

**(iii) For our seat.** Two design consequences follow directly. First, L12's τ½ prior (60–96
months) sits meaningfully longer than L10's (36–72 months) precisely because the property leg's
supply-lag mechanism has no credit-market analogue — bank lending standards can tighten in a
single quarter; a stalled apartment tower cannot un-build itself that fast. Second, the supply-
lag argument is a **length** argument, not a **magnitude** one: it says nothing about how large the
Indian cycle's amplitude should be, only that its floor duration is set by construction timelines
that were, and remain, genuinely years long in Indian metros (RERA-era project-completion
timelines commonly run 3–5 years; pre-RERA overruns routinely doubled that — A.7).

**(iv) Citations.** Glaeser, Edward L.; Gyourko, Joseph & Saiz, Albert (2008), "Housing Supply and
Housing Bubbles," *Journal of Urban Economics* 64(2): 198–217; also NBER Working Paper 14193
**[Verified]**.

---

### A.4 Why property is the collateral, part II — LTV procyclicality, the household channel, and non-reproducible land

**(i) LTV procyclicality.** Kiyotaki-Moore's `m` (the loan-to-value haircut lenders apply) is
modeled as a parameter; in practice it is itself procyclical — banks extend higher LTVs precisely
when collateral values are rising and perceived risk is falling, which is the same "neglected
crash risk" behavioral finding the credit monograph documents for bank-credit supply generally
(Baron-Xiong 2017, `docs/cycles/01-credit-cycle.md` §2). Property-specific procyclicality has an
extra amplification leg unique to real estate: because appraised value (the input to `m·q_{t+1}`)
is itself estimated from *recent comparable transactions in the same rising market*, the appraisal
and the price it is meant to discipline move together — a self-referential loop with no equivalent
in, say, corporate working-capital lending, where collateral (receivables, inventory) turns over
too fast to develop the same multi-year appraisal lag.

**(ii) The household leverage channel — Mian-Sufi, by reference.** The credit monograph's §A.9
already establishes Mian-Sufi's credit-driven household-demand channel in full — and already
identifies it, on India's own 2021–24 chronology, as **the currently-dominant mechanism** in
India's credit cycle (household debt/GDP 26%→42%, 2015–24; unsecured-retail-heavy composition).
Property is the asset through which that channel runs hardest: mortgage debt is the largest single
household liability by construction in every developed and most emerging financial systems, so a
household-leverage boom **is**, mechanically, substantially a property-collateral boom — the two
L10/L12 inputs (household-debt composition and house-price/housing-credit growth) are reading
different moments of the *same* underlying flow, which is exactly why §A.6's shared-budget
discipline matters rather than being bureaucratic housekeeping.

**(iii) Land's non-reproducibility.** The oldest argument in this literature, and the one modern
cross-country data has now actually tested. **Henry George (1879), *Progress and Poverty***,
argued land's supply is **fixed** — unlike produced capital, no amount of investment creates more
land, so rising demand against a literally inelastic aggregate supply must show up entirely in
price, not quantity, absent Glaeser-Gyourko's *permitted-supply* margin (A.3), which relaxes the
constraint at the regulatory margin without eliminating it at the physical one. **Knoll,
Katharina; Schularick, Moritz & Steger, Thomas (2017), "No Price Like Home: Global House Prices,
1870–2012"** (*American Economic Review* 107(2): 331–353) is the modern, 14-advanced-economy,
143-year test of this: real house prices were **essentially flat from 1870 through the mid-20th
century**, then **rose sharply and persistently** across the second half of the 20th century, with
substantial cross-country variation in the size of the rise. The paper's own decomposition
attributes this **not to rising replacement/construction cost** but to rising **land prices**
specifically — land price increases explain roughly **80% of the aggregate global house-price
rise since WWII**. Their explanation ties directly back to A.3's mechanism: pre-WWII, falling
transport costs continuously expanded the *effective* supply of usable land (new areas became
commutable), suppressing land prices even as population grew; since the mid-20th century,
comparable transport-cost-driven land-supply expansions have not recurred, while land-use
regulation has tightened and housing's expenditure share has risen — demand pressing against a
supply margin that stopped expanding. **For our seat**: this is the deepest structural reason
property, uniquely, deserves its own multi-decade cycle length distinct from produced-capital
assets — the underlying factor of production genuinely cannot be manufactured to meet a price
signal the way factory capacity, inventory, or (with enough time) even housing *structures*
themselves can; only the land under them cannot.

**(iv) Citations.** George, Henry (1879), *Progress and Poverty*, self-published/D. Appleton
**[Verified — canonical text, already the credit monograph's own citation for the Georgist
tradition]**. Knoll, Katharina; Schularick, Moritz & Steger, Thomas (2017), "No Price Like Home:
Global House Prices, 1870–2012," *American Economic Review* 107(2): 331–353 **[Verified]**.

---

### A.5 The equity-market translation, evidence-graded

**(i) What exists, stated honestly.** The task this file was commissioned under asks for an
evidence-graded account, and the honest grade is: **direct** studies of financial-cycle phase
predicting **forward equity returns** are thin; what exists in strength is **recession-risk**
forecasting, from which an equity-drawdown read must be inferred, one step removed. **Borio,
Claudio; Drehmann, Mathias & Xia, Fan Dora (2020), "Predicting Recessions: Financial Cycle versus
Term Spread"** (BIS Working Paper 818; published as "Forecasting recessions: the importance of the
financial cycle," *Journal of Macroeconomics* 66, 2020) run a horse race across advanced and
emerging-market economies between the term spread — finance's most widely used recession
indicator — and financial-cycle measures (credit and property gaps). Financial-cycle measures show
**significant in-sample and out-of-sample forecasting power even at a three-year horizon**, and
**outperform the term spread in nearly all specifications tested**. This is genuinely strong
evidence that the *financial-cycle state* forecasts *recession risk* — and since recessions and
equity bear markets are not the same object but overlap heavily (equity drawdowns cluster around,
and often lead, NBER/CMIE-style recession dating), this is the closest thing to a direct
equity-relevant finding this literature currently offers.

**(ii) Cycle interactions — Claessens-Kose-Terrones, verified.** **Claessens, Stijn; Kose, M.
Ayhan & Terrones, Marco E. (2012), "How Do Business and Financial Cycles Interact?"** (*Journal of
International Economics* 87(1): 178–190; companion to their IMF WP 11/76, D08 F7) build a 44-
country, 1960Q1–2010Q4 panel spanning **240+ business-cycle episodes and 870+ financial-cycle
episodes** (credit, house-price and equity-price cycles separately dated). Their central,
verified findings: **recessions coinciding with a house- or equity-price bust are systematically
longer and deeper** than recessions without one; **recoveries following an asset-price bust are
weaker**, while **recoveries accompanying rapid credit and house-price growth are stronger** — the
same amplification mechanism (A.1–A.4) running in both directions on the real economy. Their
panel further corroborates F7/D08's own reading (Claessens-Kose-Terrones's separate house-price-
cycle work, D08 §I5): house-price cycles run **longer and larger-amplitude** than credit or
equity cycles individually — direct cross-country support for A.3's supply-lag length argument,
independent of the Knoll-Schularick-Steger price-level evidence.

**(iii) The bank-sector channel — Baron-Verner-Xiong, by reference.** The credit monograph's
§B1.8 already documents **Baron, Verner & Xiong (2021), "Banking Crises Without Panics"** (*QJE*
136(1): 51–113) in full: a 46-country, 1870–2016 bank-equity panel defining a banking crisis
purely by a **>30% bank-equity index decline**, finding that panic or not, the same threshold
predicts **~80% of the eventual real-GDP damage** and a **−5.4% bank-credit/GDP** contraction
three years out. For L12 this licenses exactly the design move already flagged in the credit
monograph for L10: a **bank-sector equity index** (Bank Nifty relative to Nifty 500) is a free,
continuously-priced, real-time confirming layer — and because property busts transmit to the real
economy overwhelmingly *through* the banking system's own collateral book (mortgages, developer
loans, construction finance are disproportionately bank/NBFC balance-sheet items in India), a
property-cycle downswing should show up in bank-sector equity **before** it shows up in a lagging
NPA print, exactly the same logic the credit monograph already applies to L10.

**(iv) The honest statement — FC3 forecloses peak-dating, licenses level-states only.** This
program's own JST R6 replication (`jst-fincycle-RESULTS.md`, FC3) tested whether the combined
credit+property state's **peaks** cluster with crises on our own expanding-Hamilton construction,
and the result is honestly weak: the loose-peak grid cell (state>0.6, n=81) shows crisis-within-
±3y at 22% versus an 18% random-window base — an elevation of **1.2x**, "barely above base" in the
result file's own words, diluted by shallow local maxima. The major-peak cell (state>0.8, n=52)
reads 23% vs 18%, **1.3x** — the Borio-relevant cell, reported exactly as measured, still modest.
**This is decisive for how L12 is allowed to operate**: FC3 grades the *peak-dating* use of the
combined state specifically — trying to call a turn — and that use stays out of bounds
**regardless** of the elevation number, because the seat's design already forbids timing calls on
principle (§A.1's own point: financial cycles carry ±20%-or-worse timing uncertainty). The seat's
**primary** evidence for its existence remains FC1's 17/17-country, median +0.40 co-movement
finding — a *level* regularity, not a *turning-point* one — plus the credit monograph's own AUROC
work (D03 F9, Drehmann-Juselius 0.83–0.85). L12 therefore conditions permissions through
**level-states** (how high is the combined reading, how long has it sat there) exactly as A.6
below specifies, never through a claimed peak date, and FC3's own honesty about the tool's
weakness on the harder task is the reason that design boundary is enforced rather than merely
recommended.

**(v) Citations.** Borio, Claudio; Drehmann, Mathias & Xia, Fan Dora (2020), "Predicting
Recessions: Financial Cycle versus Term Spread," BIS Working Paper 818; *Journal of
Macroeconomics* 66 (2020) **[Verified]**. Claessens, Stijn; Kose, M. Ayhan & Terrones, Marco E.
(2012), "How Do Business and Financial Cycles Interact?," *Journal of International Economics*
87(1): 178–190 **[Verified]**. Baron, Matthew; Verner, Emil & Xiong, Wei (2021), "Banking Crises
Without Panics," *Quarterly Journal of Economics* 136(1): 51–113 **[Verified — already the credit
monograph's own B1.8]**.

---

### A.6 Interaction with L10 — what the property leg adds beyond the credit gap

**(i) The de-duplication rule, restated.** `docs/DESIGN.md` §4.2 fixes the shared arithmetic: L6
(monetary stance), L10 (credit block), L11 (capex, clamped Tier C), and L12 (this seat) share one
**macro-credit block budget, ≤20% of regime score** — the registry-enforced number — because all
four are "views of the same corporate/household-leverage phenomenon from the policy, credit,
investment and property sides" (D03 §7, D08 §2). The composite is a first-principal-component or
simple average across the block, with Tier-C L11 clamped to `min(0, reading)` before aggregation
so a hot capex print can never itself add regime-score budget. L12 enters this composite as a
**Tier-B, non-clamped** contributor (`reduce_only: false` in `ladder.yaml`) — it can add *and*
subtract regime score, unlike L11's reduce-only clamp, because its cross-country mechanism
evidence (A.1–A.5) clears the Tier-B bar even where India's own length prior does not (§A.7).

**(ii) What L12 adds that L10 alone cannot see.** Three distinct additions, each traceable to a
mechanism section above. **First, different data with a different lag structure**: L10's inputs
(credit/GDP gap, CD-ratio percentile) are monthly-to-quarterly, bank-balance-sheet-sourced, and
turn on lending-standard and deposit-funding dynamics that can shift within a single monetary-
policy cycle; L12's inputs (RBI HPI, housing-credit sectoral deployment, NHB RESIDEX) turn on the
Glaeser-Gyourko-Saiz supply-lag clock (A.3) — years, not quarters — so the two legs can and do
diverge in phase even when ultimately correlated (FC1's own median +0.40, not 1.0, is the honest
size of that correlation: co-movement, not identity). **Second, the household-collateral channel
specifically** (A.4): L10's composition input (#3, unsecured-retail + NBFC share) captures *how
much* of incremental credit is household-linked; L12's house-price leg captures whether that
credit is *chasing a rising or falling collateral price* — the Kiyotaki-Moore amplification loop
itself, which a credit-quantity series alone cannot distinguish from ordinary consumption-credit
growth. **Third, the combined state's documented superior crisis association**: Drehmann &
Juselius's own early-warning work (already the credit monograph's F9, D03) finds the credit-to-GDP
gap and a **similarly-constructed property-price gap perform well independently and materially
better in combination** — complementary rather than redundant information at the 3–5-year horizon
their AUROC exercise targets [VERIFY: exact incremental-AUROC magnitude for the combined indicator
— bis.org primary-source figures were not independently re-pulled this session, network egress to
bis.org is blocked at the proxy per CONTRACT §7 Known Prior #11; the qualitative "combination beats
either alone" finding is corroborated independently by Greenwood-Hanson-Shleifer-Sørensen's R-zone
result already in D03/L10 (credit growth AND asset-price growth jointly ⇒ ~40% crisis probability
vs ~7% unconditional, vs either alone being much weaker)].

**(iii) For our seat — the shared-budget discipline, made concrete.** None of the above licenses
double-counting. The practical rule already in the registry: L10 and L12 enter the same
`macro_credit_block` composite, so a boom that is simultaneously a credit boom *and* a property
boom (India's own current upswing arguably qualifies on both counts, §A.7) does **not** get double
regime-score weight for being visible in two places — it gets counted once, through the shared
20% cap, with L12's marginal contribution being specifically the property-leg information A.3–A.4
supply that L10 cannot: the supply-lag length prior, the collateral-appraisal feedback loop, and
land's own non-reproducibility. The design register's redundancy test (analogous to L10's own R5,
CD-ratio-vs-gap check) is the pending, pre-registered way to confirm this marginal contribution is
real rather than assumed once India-conditioned data is available.

**(iv) Citations.** Drehmann, Mathias & Juselius, Mikael (2014), "Evaluating Early Warning
Indicators of Banking Crises: Satisfying Policy Requirements," *International Journal of
Forecasting* 30(3); BIS Working Paper 421 **[Verified — already D03 F9]**. Greenwood, Robin;
Hanson, Samuel G.; Shleifer, Andrei & Sørensen, Jakob Ahm (2022), "Predictable Financial Crises,"
*Journal of Finance* 77(2): 863–921 **[Verified — already D03 F7]**.

---

### A.7 India — the measurement reality (double weight)

**(i) The one observed cycle, stated without inflation.** India's financial cycle, on this
program's own framing (`docs/CYCLE_ATLAS.md` row 1.1, `docs/DESIGN.md` L12 row), has completed at
most **one** full leg since liberalization: a **2003–2008 boom** (credit +25–30%/yr, infra/real-
estate surge, the same credit expansion D03's own chronology dates for L10), a **2013–2020
downswing** (well documented in industry press as a multi-year residential slump, especially acute
in NCR and Mumbai, historically high unsold-inventory months-to-sell), and a **2021+ upswing**
(premium-housing-led recovery, PLI-linked capex tailwind). This is **n=1**, unambiguously below
the clock test (CONTRACT §4). The cross-country mechanism (A.1–A.6) clears Tier B on its own
≥10-analogue-country evidence; India's own length and amplitude stay **Tier C**, admissible only
as a bounded check against the 10–20-year cross-country range (H19, `docs/masterplan/
C-hypothesis-register.md`), never as an independently fitted India parameter — and the
`ladder.yaml` `changes_if` field for L12 states this explicitly: the confidence upgrade condition
is "2nd domestic completed leg (2030s+)," not any amount of research effort applied to the first
one.

**(ii) The measurement instruments, and their honest limits.** **RBI's House Price Index (HPI)**
— quarterly, ten major cities, base 2010–11=100, published since **2010**, free via RBI DBIE,
built from **registered transaction values** at state sub-registrar offices — and **NHB
RESIDEX** — launched **July 2007** covering an initial 26 cities, published quarterly through
roughly **March 2015**, then paused and relaunched with an expanded ~**50-city** panel across 18
states/UTs using Laspeyres-index methodology, with the base year itself rebased from **FY2012–13
to FY2017–18 around the April–June 2018 quarter** [VERIFY: exact relaunch date and the 2015–18
transition mechanics — sourced from secondary aggregators (NHB's own 2023 RESIDEX methodology
white paper) rather than a primary RBI/NHB release pulled directly this session] — together
constitute the **entire** free, official India house-price record. Both are short (RBI HPI's
usable history barely covers the 2013–2020 downswing and none of the 2003–08 boom; RESIDEX's own
methodology break sits squarely inside the downswing window), urban-biased (major-city coverage
only; India's real-estate cycle outside the top ~10–50 cities is effectively unmeasured), and —
RESIDEX specifically — carry a **documented methodology discontinuity mid-sample**, meaning any
naive full-history RESIDEX series splices two different measurement regimes without adjustment.
This is a genuinely worse measurement-continuity problem than L10's own GNPA-recognition breaks
(AQR 2015–18) or GDP-rebase splice, because those at least sit on a single, continuously-run
series with a documented break date; RESIDEX's 2015 pause and 2018 relaunch is closer to a series
restart. **RBI's sectoral deployment of credit** — monthly, free, isolating bank credit to
"housing" — is the **longer, continuous proxy** this program leans on instead: it runs back
further than either price index, carries none of RESIDEX's discontinuity, and (per this session's
own search) shows housing credit outstanding rising from roughly **₹17.3 lakh crore (March 2022)
to ₹19.9 lakh crore (March 2023) to ₹27.2 lakh crore (March 2024)** [VERIFY: exact figures —
sourced from press coverage of RBI data this session, not a direct DBIE pull] — a credit-quantity
proxy for the property cycle's *demand* leg, complementary to, and longer-running than, either
price index for the *price* leg.

**(iii) RERA 2016 and the 2016–2020 inventory overhang as the structural-break story.** The **Real
Estate (Regulation and Development) Act, 2016** — core provisions effective **1 May 2016**, the
remainder (69 of 90 sections initially notified, the rest from **1 May 2017**) — is the single
clearest structural break in India's post-liberalization property cycle, and belongs in the same
category as L10's AQR recognition shock: a **regulatory** event, not a market one, that
permanently changed the data-generating process. RERA mandated project-level escrow accounts
(70% of buyer receivables ring-fenced for that project's construction, ending the practice of
diverting one project's buyer payments to fund a developer's *other* land purchases), state-level
regulatory authorities, and disclosure/completion-timeline accountability. It arrived directly
into the worst of the inventory overhang it was partly designed to address: **PropEquity data put
unsold housing inventory across the top eight cities at roughly 472,000 units as of March 2017**,
with months-to-sell running as high as **60 months in Noida, 43 in Mumbai, 38 in Chennai, 30 in
Bengaluru** [VERIFY: exact figures — PropEquity via secondary press coverage, not the primary
research report]. The mechanism connects directly to A.3–A.4: RERA raised the **cost of launching
speculative supply** (escrow discipline, disclosure liability) precisely as the 2013–2020
downswing's overhang was working through the system, which is a genuine candidate explanation for
why the 2021+ upswing looks more supply-disciplined than 2003–08 did — and equally a genuine
candidate for the desk hazard G.4 names below.

**(iv) The unofficial-cash component — measurement honesty, stated plainly.** No India property-
cycle discussion is complete without naming what the official series cannot see. Property has
long been documented as India's largest single destination for **unaccounted ("black") money**,
transacted at a premium to the government's own **circle rate** (the artificial statutory floor
value used for stamp-duty/registration, commonly 20–100%+ below prevailing market rates depending
on city and how recently the circle rate was last revised) — meaning registered transaction
values, the RBI HPI's own input, are known to sit at a **discount to true transaction prices**, by
an amount that varies by city, asset class and time period and is **not independently
measurable** from any free official series. Post-2016 survey evidence (LocalCircles, cited via
Forbes India/Business Standard coverage of demonetization's eighth anniversary, 2024) finds
roughly **two in three property buyers surveyed reported paying some portion of a recent
transaction in cash**, with a meaningful share paying **more than half** the value that way, and
**roughly nine in ten respondents** still believing black money remains rampant in the sector
despite demonetization (2016), RERA (2016–17) and GST (2017) [VERIFY: exact survey percentages and
methodology — LocalCircles self-reported online-panel survey, not a probability sample; treat as
directional, not a precise population estimate]. **The honest consequence for L12**: the registered-
transaction-value series this seat is built from is not merely noisy, it is **structurally biased
toward under-recording price appreciation** in exactly the high-value, high-informal-cash-share
segments where a speculative boom would show up first — a measurement gap this program states
rather than papers over, and one no free Indian data source currently closes.

**(v) What the India L12 state can actually be built from today versus 2030.** **Today (2026)**:
a length-and-amplitude check against the 10–20-year cross-country range (bounded, not fitted); the
RBI-HPI/RESIDEX-spliced price series from 2010–13 forward, explicitly flagged for its methodology
break; the housing-credit sectoral-deployment series as the primary, longer-running, continuity-
clean proxy; a qualitative RERA/inventory-overhang structural-break marker; and the composite's
correct placement inside the shared macro-credit budget (§A.6), reading as a **level-state** only,
never a peak call (§A.5iv). **Not available until at least the 2030s**: a second completed
domestic down-leg, without which India-specific length, amplitude, and (per FC3's own honesty)
any India-conditioned peak-dating exercise simply have no second data point to test against — the
`ladder.yaml changes_if` condition stated plainly rather than implied.

**(vi) Citations.** RBI HPI (base 2010–11=100, quarterly since 2010, ten cities, RBI DBIE)
**[Verified — RBI DBIE publication schedule]**. NHB RESIDEX (launched July 2007, 26 cities;
relaunched ~50 cities, base rebased to FY2017–18 ~2018) **[Verified in outline; relaunch date/
transition mechanics VERIFY per (ii) above]**. Real Estate (Regulation and Development) Act, 2016,
Government of India, effective 1 May 2016 (core provisions)/1 May 2017 (full notification)
**[Verified]**. PropEquity unsold-inventory figures, March 2017 **[VERIFY: primary report]**.
LocalCircles black-money-in-real-estate survey, 2024 **[VERIFY: methodology, exact percentages]**.

---

### A.8 Synthesis — mechanism, observable, seat, and the honest gap

| Mechanism | Observable (free India/global series) | L12 input consumed | What nothing free captures |
|---|---|---|---|
| Borio credit+property co-movement (A.1) | RBI HPI/RESIDEX + housing-credit deployment, alongside L10's own credit/GDP gap | The definitional pairing itself — L12 exists because this co-movement is real (FC1: 17/17, median +0.40) | Equity's own weak fit internationally is itself un-tested for India (I1: India's cycle is credit+equity-led, property fits *less* well than the BIS template — see (iii) below) |
| Liberalization + low-inflation precondition (A.1iii) | Capital-account openness proxies; India CPI post-2016 inflation-targeting regime | Sets why India's own cycle is barely one leg old — not a numeric input | Whether India's regime is "mature" enough for a stable length prior — unknowable before a 2nd leg |
| Drehmann-Borio-Tsatsaronis measurement (A.2) | N/A — methodology choice, not a series | Justifies the expanding-Hamilton construction over band-pass/turning-point | Full band-pass precision — deliberately traded for real-time honesty (FC2's crude-tool caveat) |
| Kiyotaki-Moore collateral loop (A.3i) | Already L10's own input #3 (collateral-class-weighted composition) | Recap by reference; no new series | Collateral-class granularity by asset type — a stated future refinement, per the credit monograph |
| Glaeser-Gyourko-Saiz supply lag (A.3ii) | RERA project-completion timelines (qualitative); OBICUS/IIP construction-materials proxies | The τ½ length prior (60–96m) itself | India-specific supply-elasticity measurement — no free, city-level land-use-regulation dataset exists |
| LTV procyclicality + Mian-Sufi household channel (A.4i–ii) | RBI FSR household-debt/GDP; housing-credit sectoral deployment | Confirms L10's Tier-C composition input is *also* the property-channel signal today | India-specific LTV time series by lender — not published free at the aggregate level |
| Knoll-Schularick-Steger land non-reproducibility (A.4iii) | N/A — global historical finding, context only | Underwrites why property gets its own multi-decade length, not a numeric input | An India-specific 1870-scale land-price history does not exist |
| Financial-cycle phase → recession risk (A.5i, Borio-Drehmann-Xia) | RBI HPI/housing-credit + L10 credit gap, jointly | Feeds the combined macro-block regime score, never a standalone equity-return forecast | A direct India equity-return regression conditioned on financial-cycle phase — not yet run (queued for the data phase) |
| Cycle interactions (A.5ii, Claessens-Kose-Terrones) | Same combined series | Corroborates deeper/longer recessions at financial-cycle peaks — context for the block's weight, not a separate input | India-specific business-vs-financial-cycle interaction test (I1/I4 already flag India's own causality runs opposite the textbook direction — see below) |
| Bank-sector channel (A.5iii, Baron-Verner-Xiong) | Bank Nifty / Nifty 500 relative drawdown | Real-time confirming layer, shared with L10 | A verified India-specific threshold-crisis replication — not yet run |
| RERA 2016 / inventory overhang (A.7iii) | Unsold-inventory months-to-sell (industry trackers, not fully free); RERA project registries (free, state-level, unaggregated) | Qualitative structural-break marker on the 2013–2021 window | A national, aggregated, free RERA project-pipeline dataset — does not exist; state portals are fragmented |
| Unofficial-cash discount to registered value (A.7iv) | None — by construction unmeasurable from official series | Explicit measurement-honesty caveat on the entire price-leg input | Any quantified estimate of the registered-vs-actual price gap, nationally or by city — genuinely unknowable free |

**The sharpest honest gap.** India's own published academic evidence (Behera & Sharma, RBI WPS
(DEPR) 03/2019, D03 I1) finds India's aggregate financial cycle is driven **mainly by credit and
equity, not house prices** — a genuine departure from Borio's own international finding that
equity "does not fit" and property does the work. This does not overturn A.1–A.6's cross-country
mechanism (which remains the Tier-B basis for L12's existence), but it is the single most important
India-specific caveat this monograph carries forward honestly rather than smoothing over: the BIS
template's property-centrism may simply transfer less cleanly to a market where retail/FII-active
equity participation is unusually high relative to mortgage-market depth — precisely the kind of
finding a future India-conditioned redundancy test (§A.6iii) needs to confront directly rather than
assume away.

---

## PART G — Operator psychology

Part A documents a mechanism the desk cannot personally arbitrage away even where it fully
understands it: property's collateral loop, its supply-lag length, and its land-non-reproducibility
floor are structural, not sentiment, and they run on a clock measured in years the operator will
personally live through only once or twice in a career. That combination — genuine mechanism, long
clock, and (in India specifically) a household asset every desk member already holds a large,
undiversified, emotionally-loaded personal position in — is exactly the setup that produces
confident, badly-timed conviction. This Part maps the failure modes that setup invites to the
countermeasures already built into L12's design.

### G.1 The homeowner-voter political economy — expect policy fightback at every downswing

**Mechanism.** **Fischel, William A. (2001), *The Homevoter Hypothesis: How Home Values Influence
Local Government Taxation, School Finance, and Land-Use Policies*** (Harvard University Press)
names the mechanism directly, in its original US local-government setting: because a home is the
median household's largest, least-diversifiable asset, and because local political decisions
(zoning, infrastructure, schools) visibly move that asset's value, homeowners become unusually
vigilant political actors specifically around anything threatening home values — voting, lobbying,
and organizing far more intensely on housing-price-relevant questions than the dollar stakes alone
would predict for a rational, diversified investor. The mechanism generalizes past Fischel's
original zoning/local-tax setting to the *national* political economy of a property downswing
anywhere households are heavily invested: a broad-based fall in property values is not merely an
asset-price event, it is a threat to the largest component of median household wealth **and** the
collateral base of the banking system, which together make policy intervention politically
close to inevitable rather than a tail scenario. **India's own record already demonstrates this
directly**, not by analogy: the **SWAMIH Fund** — launched November 2019, in the teeth of the
IL&FS-triggered NBFC funding freeze and the 2016–2020 inventory overhang — committed **₹10,000
crore of direct government seed capital toward a ₹25,000 crore total corpus**, specifically to
complete stalled, financially-viable-but-cash-starved housing projects (an SBICAP-Ventures-managed
vehicle, roughly 1,500 stalled projects and ~₹55,000 crore of completion funding identified by the
commissioning study). Stamp-duty cuts by multiple states (Maharashtra prominently) during
2020–21 are the demand-side mirror of the same instinct. **The operator should expect this pattern
to repeat at the next downswing, not treat it as a one-off 2019 emergency measure.**

**Countermeasure.** L12 is built to be **regime**, not **directional bet**: its output conditions
leverage and hedge *permission* inside the shared macro-credit budget (§A.6), never a short
position on property-linked names timed against a downswing the operator expects policy to
eventually blunt. The phase-uncertainty framing (never a date, per A.1's own ±20%-or-worse timing
uncertainty) already prices in that a downswing's *depth and duration* are policy-contingent in a
way a pure Kiyotaki-Moore mechanical model is not — the desk is not meant to be surprised when a
government facing a homeowner-voter base with 77% of household wealth in the affected asset class
(G.2) intervenes.

### G.2 "Property never falls" — India's strongest household prior

**Mechanism.** The **RBI Household Finance Committee Report (July 2017)** — the most authoritative
free measurement of Indian household balance sheets available — found the average Indian household
holds roughly **84% of total wealth in physical assets**, of which **~77% is real estate
specifically** and ~11% gold, against **under 5% in financial assets** (equities, mutual funds,
bonds combined). This is not merely a data point; it is the structural foundation of the single
strongest asset-price belief the Indian household sector carries: property, unlike equities (whose
1979–2003 flatness and periodic 50%+ drawdowns are within living memory for many investors), has
**no comparably salient national memory of a severe, sustained nominal decline** — the 2013–2020
downswing was real, well documented in industry data (A.7), but ran as **stagnation and slow real
erosion** (nominal prices mostly flat-to-down in specific markets, not a sharp nominal crash), which
is precisely the kind of decline **least likely to update a strongly-held prior** — a slow erosion
the household sector's own accounting (money illusion's cousin: a house "worth what I paid for it,
plus renovations" rarely gets marked to a falling market the way a listed equity position is marked
daily) can simply fail to register as a loss at all.

**Countermeasure.** L12's construction is explicitly **mark-to-market via the free indices**
(A.7ii), not via household perception — the composite state moves on RBI HPI/RESIDEX/housing-
credit readings regardless of whether the desk's own instinct (shared, structurally, with every
other Indian household) says property "doesn't really fall." This is the property-specific
instance of the same discipline the debt-supercycle monograph's G.1 documents for money illusion
on bondholder returns: a mechanical, computed series has nothing for the bias to attach to.

### G.3 Extrapolating the one observed Indian cycle

**Mechanism.** With n=1 (A.7i), every feature of India's single observed cycle — its ~5-year boom
length, its ~7-year downswing, its post-RERA recovery shape — is a **single draw**, not a
parameter. The specific hazard: because 2003–2008 and 2021+ are the *only* two upswings anyone on
the desk has personally watched, an operator can unconsciously treat their specific shape (say,
premium/luxury-housing-led in the current upswing, mass-market-led in 2003–08) as *the* pattern
the next cycle will repeat, rather than one realization among the 10–20-year cross-country range's
much wider space of possible shapes.

**Countermeasure.** The Tier-C India-length classification (versus Tier-B cross-country mechanism,
§A.7i) is the structural guard: L12's length and amplitude parameters are **frozen at the
cross-country cross-section**, not fitted to India's own n=1 realization, and the `ladder.yaml`
`changes_if` field names the only condition that changes this — a second completed domestic leg,
not any amount of narrative confidence about the first one. The design register's H19 bound-check
(does India's single observed length fall inside [10,20]y) is deliberately a **pass/fail bound**,
never a point estimate refit, precisely so n=1 cannot smuggle a fitted parameter into a Tier-B seat
through the back door.

### G.4 Confusing RERA-era supply discipline with a new paradigm

**Mechanism.** A.7iii's own honest framing — RERA plausibly explains why the 2021+ upswing looks
more supply-disciplined than 2003–08's did — is a genuine, evidence-consistent read. It is also
exactly the sentence a desk under pressure to justify running property-linked exposure harder
converts into "this time the structural reform means the old cycle doesn't apply" — the same
"this-time-is-different" pattern Reinhart-Rogoff document for sovereign debt (already the debt-
supercycle monograph's own A.5) and the same pattern the folk "18-year cycle" literature's own
survivorship-biased retrospective hit-rate depends on (D07 §D11). RERA is real regulatory change
with a real, named mechanism (escrow discipline raising the cost of speculative launches, A.7iii);
it is not evidence that Glaeser-Gyourko-Saiz's supply-lag mechanism (A.3ii) or Knoll-Schularick-
Steger's land-non-reproducibility floor (A.4iii) have stopped operating.

**Countermeasure.** The 10–20-year RANGE construction (never a single point, and never adjusted
mid-design for a regulatory narrative not yet tested across even one full cycle under the new
regime) is the structural answer — `ladder.yaml`'s own decay field for L12 states this explicitly:
"length is a 10–20y RANGE, never 18y point." A regulatory-regime change is exactly the kind of
qualitative structural-break marker A.7iii's own framing keeps out of the numeric length prior and
confined to context — logged, watched, and specifically **not** used to narrow or shift the
frozen Tier-B range until a second domestic leg gives it something to test against.

### G.5 Countermeasures mapped

Four structural features already carry this Part's actual work. **(1) Regime-only expression**
(G.1) — L12 conditions leverage/hedge permission inside the shared macro-credit budget, never a
directional bet timed against expected policy fightback. **(2) Mechanical, index-driven
construction** (G.2) — the composite moves on RBI HPI/RESIDEX/housing-credit readings, immune to
the household sector's own strongest asset-price prior because it never asks the operator whether
property "feels" like it's falling. **(3) The Tier-C/Tier-B split with a named, single upgrade
condition** (G.3) — India's own n=1 cycle cannot smuggle a fitted parameter into a Tier-B seat; only
a second completed domestic leg can. **(4) The frozen 10–20-year range** (G.4) — a structural-
reform narrative, however evidence-consistent in its own right, cannot narrow or shift the length
prior until it has itself survived a full cycle. None of the four asks the operator to be wiser in
the moment than Part A's evidence justifies; each removes the decision before the moment that would
have made it hardest.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Reading a policy-blunted downswing as evidence the mechanism failed | Fischel's homevoter political economy + India's own SWAMIH/stamp-duty-cut record: policy fightback is the norm, not the exception, when the median household's largest asset is threatened | L12 stays regime-only (leverage/hedge permission); phase-uncertainty prior already assumes policy-contingent depth and duration |
| "Property never falls" overriding the computed state | RBI Household Finance Committee: 77% of household wealth in real estate, near-zero salient memory of a sharp nominal decline (2013–20 was slow erosion, not a crash) | Mechanical index-driven construction (RBI HPI/RESIDEX/housing credit); never a felt judgment |
| Fitting India's length/amplitude to the one observed cycle | n=1; the only two upswings the desk has watched become, unconsciously, "the pattern" | Tier-C India length vs Tier-B cross-country mechanism; frozen at the cross-section; upgrade only on a 2nd domestic leg |
| "RERA changed everything" narrative capture | This-time-is-different pattern (cf. Reinhart-Rogoff, debt-deep A.5); a real mechanism (escrow discipline) over-extended into a claim the supply-lag/land-scarcity mechanisms themselves have stopped operating | 10–20y RANGE frozen by design; regulatory change logged as qualitative context, never used to narrow the numeric prior pre-2nd-leg |
| Double-counting a boom that is visible in both L10 and L12 | Same underlying credit/collateral flow, viewed from two data angles (A.6) | Shared 20% `macro_credit_block` budget across L6+L10+L11+L12; composite, not additive, aggregation |
| Treating FC3's 1.2–1.3x elevation as license to call a peak | The combined state's peak-dating performance is honestly weak on this program's own tools (FC3) | L12 conditions permission via level-states only; peak/turn-calling stays out of bounds regardless of the elevation number |

None of these six countermeasures asks the operator to be more disciplined than Part A's evidence
justifies. Each converts a live judgment call — decide whether this downswing is finally the one
policy won't blunt, decide whether this decline finally counts as real, decide whether India's one
cycle is representative enough to size against, decide whether RERA really did change the
mechanism, decide whether today's reading in two ladder entries deserves to move the book twice,
decide whether the combined state's elevation is finally strong enough to call a top — into a
structural non-decision, made once, in the registry, before the moment that would have made it
hardest.


---

# PART B — The property-cycle case record

# PART B — The property-cycle case record

*Financial-cycle monograph (atlas 1.1) · Part B · v1.0 · 2026-09-01 · Author: Claude (research agent)
for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026 unless
tagged `[VERIFY: ...]`. This Part sits beside `research/cycles/fincycle-deep/jst-fincycle-RESULTS.md`
("FC1–FC3," our own JST R6 pooled computations) — FC1–FC3 are referenced throughout and never
recomputed or contradicted here. `research/cycles/credit-deep/partB-cross-country.md` (the credit
monograph's own ten-case record) already covers the **banking-crisis mechanics** of several of the
same episodes (Japan, Spain, Sweden, Ireland, China, Australia/Canada) in specification detail; this
Part deliberately does not re-derive those — it is cross-referenced by name throughout — and instead
supplies the **property-price-specific angle**: boom magnitudes, construction/GDP shares,
price-to-income extremes, the physical-supply overhang, and the real-house-price peak-to-trough
record itself, which the credit monograph's bank-loss-and-recapitalization framing does not carry.
Style and evidentiary discipline follow `research/cycles/debt-deep/partB-cases.md` (the debt-supercycle
monograph's own Part B, the house style for this series): numbers-forward, every figure sourced,
`[VERIFY]` where a search pass could not pin the primary table, interpretation written honestly
after the numbers rather than fitted to a thesis.*

---

## B1. The global house-price record

**Knoll, Schularick & Steger (2017), "No Price Like Home: Global House Prices, 1870–2012"**
(*American Economic Review* 107(2): 331–353; CESifo WP 5006) is the field's foundational long-run
panel: annual real house-price indices for **14 advanced economies since 1870** (Australia, Belgium,
Canada, Denmark, Finland, France, Germany, Italy, Japan, Netherlands, Norway, Sweden, Switzerland,
UK, US in various vintages of the series). The headline shape is the hockey stick the task names, and
it is verified almost exactly as stated: **real house prices were essentially flat from the late 19th
century through the mid-20th century**, then rose strongly and with substantial cross-country
variation over the second half of the 20th century — on KSS's own reckoning, averaging **roughly a
tripling in real terms across the 14 countries since 1950**. The pivot is not gradual; it clusters at
the postwar reconstruction/Bretton Woods transition, consistent with our own FC-panel's observation
that the modern financial cycle is a post-1945, and especially post-1985, phenomenon (FC2 below).

**The land-share decomposition is the paper's second, arguably more important, finding.** KSS
decompose house prices into a replacement-cost (structure) component and a residual land-price
component, and find that **rising land prices — not construction or replacement costs — explain
roughly 80% of the global house-price boom since World War II**. This is the mechanistic core of
every L12-relevant case below: a house is a bundle of a depreciating, reproducible structure sitting
on a fixed, non-reproducible parcel of land, and virtually the entire post-1950 story is the price of
the land component, not the physical build. It is also the direct empirical ancestor of the
Glaeser-Gyourko supply-lag mechanism CYCLE_ATLAS.md already cites as L12's mechanism (`§1.2`) — a
credit boom cannot manufacture more land; it can only bid up the price of the fixed stock while
construction (which *can* respond, but only after a multi-year permit-and-build lag) catches up too
late and then overshoots.

**BIS residential property price statistics** are the modern, ongoing continuation of this record and
the practical mirror source for L12's own construction (per DESIGN.md, RBI HPI is India's own input;
BIS is the cross-country check). The BIS's **"selected" dataset covers roughly 59–60 countries at
quarterly frequency**, four series per country (nominal/real levels and nominal/real growth rates),
built on the BIS's own *Handbook on Residential Property Prices* methodology; the underlying
**"detailed" dataset carries 300+ series from the same ~60 countries**, collected directly from
national central banks, with **23 countries backdated to historical series reaching back to roughly
1970**. India is one of the reporting countries via the RBI HPI feed. This is the coverage backbone
against which every cross-country case below is checked; it is also the honest limit on how far back
a like-for-like international comparison can go before 1970 for most of the panel — which is exactly
why KSS's 1870-start academic reconstruction, not the BIS series, is the source for the pre-1970
hockey-stick claim above.

**Why property cycles run slower and longer than equity cycles — the volatility/liquidity contrast.**
Naively measured, housing looks far calmer than equities: one widely cited decomposition puts raw
housing-return standard deviation at **~5.4%/year versus ~18.2%/year for the S&P 500**. But that
headline number is an artifact of infrequent, appraisal-smoothed transactions, not a true risk
comparison — the same study finds that once **idiosyncratic risk from bid-ask spreads (+2.0pp/year)**
and **illiquidity risk from temporal smoothing (+1.3pp/year)** are added back in, housing's *effective*
volatility rises to **~8.7%/year**, still roughly half of equities', with a comparably adjusted Sharpe
ratio (**0.42** vs the S&P 500's **0.40**) — genuinely comparable risk-adjusted returns, at
meaningfully lower turnover. Jordà, Knoll, Kuvshinov, Schularick & Taylor's own JST-R6 total-return
work ("The Rate of Return on Everything, 1870–2015," *QJE* 2019) reaches the same qualitative
conclusion independently: housing total returns over the long run are comparable to equities but with
markedly lower volatility — and with **catastrophic tail risk concentrated specifically in busts**,
which is precisely FC1's territory (credit and property amplify each other on the way up; the same
amplification runs in reverse). The mechanism behind the slowness is structural, not merely
statistical: housing transacts infrequently (search costs, financing contingencies, months-long
closing timelines), each unit is heterogeneous (no continuous limit order book, no single "last
traded price"), and — per the KSS/Glaeser-Gyourko land-and-construction-lag logic above — *supply*
itself takes years to respond in either direction. An equity market re-prices new information within
seconds; a national housing stock re-prices it over quarters, and a construction pipeline over years.
This is the direct empirical grounding for L12's own **8–20 year** period estimate (post-1998 average
**~16 years** per Drehmann-Borio bandpass methods) against L10's (credit cycle) **36–72 month** τ½ and
L3's (equity momentum) **6–12 month** horizon — three amplitudes and three clocks on the same
underlying collateral-and-leverage mechanism, exactly the layered-cycle architecture the Contract's
mandate (§1) already specifies.

---

## B2. Eight property-cycle case studies

### 1. Japan, 1985–1991–2005 — the master case

**The boom, in property-specific terms.** Between 1980 and 1991, commercial land prices in Japan's
six largest cities rose **almost 130%**, residential land in the same cities **108%**; the credit
monograph's own case #2 (partB-cross-country.md) already documents the 1985–90 acceleration leg
(bank real-estate lending roughly doubling, loan/GDP passing 100%) — this Part adds the *price* side
those bank flows were chasing. The single cleanest boom metric in this entire record is Tokyo's
apartment price-to-income ratio: **8.08× in 1985, rising to 18.12× at the 1990 peak** — meaning the
average Tokyo household would have needed over eighteen years of full pre-tax income to buy a new
70sqm apartment, a multiple no other case in this record approaches even at its own extreme (compare
Australia's current, already-alarming, 8.2×, case 8 below). **The golf-membership economy** is the
boom's most vivid single artifact: memberships at ordinary clubs traded for **¥30–50 million**,
prestige clubs above **¥100 million**, tradable, mortgageable, and pledgeable as loan collateral in
their own right, tracked by a dedicated **Nikkei Golf Membership Index** that peaked at **948.17 in
1990**. **The turn** came via Bank of Japan tightening through 1989–90 and Ministry of Finance
quantity controls on real-estate lending (1990) — a direct, administrative credit-supply clamp, not a
market-driven repricing. **The bust** then ran for **13 consecutive years of decline, 1992–2005**, in
residential land in the six major cities; by 2002 the average land price nationwide had fallen
**roughly 70%** from its 1991 level; commercial land eventually fell **70–80%** from peak over
**roughly 14 years**, while residential land's fall was somewhat more muted (**~40%** by one measure)
— commercial land, having risen further, fell further, the pattern that recurs throughout this
record. The golf index tells the same story in miniature and faster: it sat at **57.79 by 2002**,
**about one-sixteenth** of its 1990 peak; **90% of Japan's 2,400 golf clubs were in debt by 2001**,
**1,700 bankrupt or in severe distress**, and **over 630 courses failed between 1991 and 2005**,
carrying roughly **$136 billion** of debt — an estimated **20% of Japan's entire ¥-denominated bad-loan
problem** traced to golf-course collateral alone, a genuinely startling single-asset-class share of a
systemic banking crisis. **Equity translation** (cross-referencing the credit monograph's own figures,
not recomputed here): the Nikkei 225 fell **~80% from its December 1989 peak (38,957) to ~7,600–7,831
by 2003**, a 14-year drawdown that later extended to **~82% at its 2008 trough**, and the index's
*price* level did not reclaim its 1989 high until **22 February 2024** — 34 years later. **L12 lesson.**
Japan is the record's cleanest demonstration that a real-estate cycle's *turning point itself is
slow to confirm*: there was no single crash day analogous to an equity-market break — land prices
peaked in 1991 and then simply declined, quarter after quarter, for thirteen years, with no
statistical method available in real time that could have confidently called the trough before it had
already passed. This is the strongest possible empirical grounding for L12's phase-uncertainty design
(DESIGN.md: "phase-uncertainty prior only, never a date") and for FC2's own finding that the financial
cycle lengthened from an 11-year to a 13-year median spacing post-1985 — Japan's own multi-decade
descent is the extreme tail of exactly that lengthening.

### 2. United States, 2000–2006–2012 — the best-measured bust

**The boom.** The Case-Shiller National Home Price Index (Jan 2000 = 100) rose to **roughly 190–198**
by its Q1 2006 peak — on the order of **90–98% nominal appreciation in six years**; residential
investment peaked at **6.7–6.8% of GDP in Q4 2005**, up from **~4.5% in 1994**, the US construction
boom's own (much smaller than Spain's, see case 3) overheating gauge. Price-to-income readings for
the 2006 peak vary sharply by methodology — a simple median-house-price/median-income "median
multiple" puts it near **4.1×** (versus the long-run US norm of ~3×), while a Case-Shiller-based
composite calculation used more recently puts a comparable multiple closer to **7×**
`[VERIFY: reconcile the two price-to-income methodologies and their exact 2006 point estimates]` —
the size of that gap is itself informative about how contested "boom magnitude" claims can be even
in the best-documented housing market in the world. **The subprime mechanics, briefly** — the credit
monograph covers the banking side (S&L-crisis precedent, off-balance-sheet vehicle leverage, the
2008 systemic transmission) in full; here it is enough to note that adjustable-rate mortgage resets
and private-label securitization allowed the *price* boom to run further past what income-based
underwriting alone would have supported, which is why the subsequent price fall was so much larger
than the 2001 recession's income shock alone would predict. **The bust, precisely measured.** On the
Case-Shiller National Index, the nominal peak-to-trough fall was **~27%** (Q1 2006 to Q1 2012); the
broader 20-city/National Composite indices — weighted toward the "sand states" (Nevada, Arizona,
Florida, California) — fell further, **~33–35% nominal**. In **real (CPI-deflated) terms**, using
Shiller's own long-run series (peak **198.01** in Q1 2006 to trough **113.89** in Q1 2012), the decline
reaches **~42.5%** — meaning real US home values gave back essentially their entire 2000–2006
appreciation and then some, returning close to year-2000 real levels by 2012. **The 2012
bottom-dating problem, precisely the phenomenon the task names.** Even the world's most granular,
highest-frequency, longest-running published property index (Case-Shiller, monthly since 1987)
cannot produce an *uncontested single trough date*: the National Index, the 20-city Composite, and
the 10-city Composite bottomed at different points spanning roughly late 2011 through mid-2012
depending on seasonal-adjustment choice, and a policy-driven double-dip (prices firming after the
2009–10 homebuyer tax credit, then re-falling once it expired) means a naive "lowest monthly print"
search returns a different answer than a trend-filtered one. **L12 lesson.** If the single
best-instrumented housing market on earth cannot agree on its own cycle trough to within several
months even with the benefit of full hindsight, no design that depends on *dating* a property-cycle
turn in real time can be taken seriously — precisely the discipline FC3 already enforces (states,
never dates) and precisely why L12's design (DESIGN.md) restricts itself to a phase-uncertainty prior
rather than a timing signal.

### 3. Spain, 1997–2007–2014 — construction as the overheating gauge

**The boom, by the numbers.** Private-sector credit/GDP nearly doubled 2000–2007 (credit monograph's
own case #4); the property-specific overheating signal sits alongside it: **residential
construction/GDP peaked at 11.7–11.8% in December 2006** (up from **6.2% in 1997**), and the *total*
construction sector — residential plus commercial plus public works — reached **~17% of GDP and ~12%
of employment** at the same peak, more than **double** the long-run OECD norm for the sector. Real
house prices rose **over 150% from 1998 to 2007**, with **71 percentage points of that concentrated
in just 2003–2008**; annual housing construction exceeded **one million units at the peak — more
than Germany, France, and the UK combined**, an overbuild whose scale becomes the story's second act.
The cajas (regional savings banks; credit monograph's own detail) were the conduit, but the *asset*
side of their balance sheet — the physical stock they financed — is this Part's focus. **The turn**
was the 2008 GFC's wholesale-funding freeze. **The bust.** Real house prices fell **~41% peak to
trough (2007–2014)**, a genuinely severe decline landing between Japan's residential-land fall and
its commercial-land fall in magnitude, compressed into roughly **seven years** rather than Japan's
fourteen; unemployment rose from **8.2% (2007) to 26.3% (spring 2013)**; the IBEX 35 fell **~50%**
(Nov 2007–Oct 2008), with weakness persisting into 2012; SAREB, the EU-backed "bad bank," absorbed the
cajas' impaired real-estate assets from 2012. **The ghost infrastructure** is Spain's own uniquely
vivid boom-artifact, playing the role Japan's golf memberships play above: **Ciudad Real Central
Airport**, built at a cost of **~€1.1 billion** with a terminal designed for 10 million passengers/year
and one of Europe's longest runways, opened in 2009, drew essentially no traffic, went bankrupt in
2012, and sold at a subsequent bankruptcy auction for a single bid of **€10,000** — a >99.999% recovery
loss on the physical asset. Castellón airport, opened the same boom era, sat effectively unused for
over a decade before a partial 2026 reopening. **L12 lesson.** Spain is the cleanest demonstration
that a construction-share-of-GDP gauge running at roughly double its long-run norm is itself an
overheating signal independent of the credit aggregates L10 already tracks — and that a property
bust's *physical* overhang (empty airports, one million-plus surplus housing units) takes far longer
to clear than the financial overhang, because unlike a loan write-down, a half-built exurban
development or an unused runway cannot be marked to zero and moved past; it must be physically
absorbed, converted, or demolished, a multi-year-to-decade process that keeps a local construction
sector depressed long after the banks themselves have been recapitalized.

### 4. Ireland, 2013 trough — the fastest full round trip

**The bust, precisely dated.** Ireland's own Residential Property Price Index (Jan 2005 = 100) rose to
an all-time high of **131.0 in April 2007** and fell to a record low of **58.7 in March 2013** — a
**54.4% nominal peak-to-trough decline**, compressed into roughly **six years**, one of the steepest
compressions in this record (Dublin fell **~56%** at its own trough; apartment prices fell
**over 62%**). **The recovery.** Irish house prices regained their **2007 nominal peak level in
mid-2022** — roughly **fifteen years** after the 2007 high — and by late 2025 stood **~23% above** the
2007 peak nationally (Dublin **+8.2%**, outside Dublin **+25.6%**), the recovery this time attributed
by analysts explicitly to a housing **supply shortage** rather than renewed credit excess. **Why "the
fastest full round trip" is the right description, carefully qualified.** Among every bust exceeding
**~50% peak-to-trough** in this record, Ireland is the only one that has *also* completed a full
round trip back above its old nominal peak: Japan's commercial land remains roughly **70% below** its
1991 high **35 years later**; Spain's national index has not durably reclaimed its 2007 nominal peak
in most regions even by the mid-2020s. Set against Hong Kong's comparably steep **~58–65%** fall over
a comparably short ~6-year window (case 6 below) — which recovered on its own, slower, multi-decade
timeline — Ireland's combination of *speed of fall* and *completeness of eventual recovery* is
genuinely distinctive rather than merely fast in one dimension. **L12 lesson.** A market making new
nominal highs is not, by itself, evidence of a *new* bubble forming by the *same* mechanism as the
last one — Ireland's 2022–25 highs were driven by a documented supply shortfall (a Glaeser-Gyourko
construction-lag story, the mechanism L12 is itself built on) rather than a credit-fuelled demand
surge, and a state-classification design that flagged "above old peak" as automatically HIGH without
checking the mechanism behind it would have mis-classified this specific case; L12's inputs (credit
growth alongside price growth, not price alone) already guard against exactly this failure mode.

### 5. Nordic 1987–1993 — the liberalization-cohort bust

**Setup — deregulation, not merely credit growth.** Finland and Sweden both deregulated their
domestic credit systems in the mid-1980s (interest-rate ceiling removals, expanded bank lending
authority), a structural regime change that preceded — and, on the mainstream reading, enabled — the
subsequent property and credit boom; this is the "liberalization cohort" framing the task names, and
it is distinct in kind from a garden-variety late-cycle credit boom because the lending *institutions
themselves* were operating under rules and risk models with essentially zero prior full-cycle
experience. **Sweden.** The property bubble peaked in **1989**; real property prices then declined
sharply, with nominal house prices falling roughly **25% by the end of 1993** from their 1992 turn,
and — reflecting continued Swedish krona-related inflation after the September 1992 float — the
**real, CPI-deflated peak-to-trough decline reached closer to ~30%**. Bank loan losses jumped from
**0.3% (1989) to 7% (1992)**, concentrated specifically in real-estate lending (more so than in Norway
or Finland); the credit monograph's own case #5 covers the recapitalization side (blanket state
guarantee, Nordbanken/Gota Bank rescues, ~2–3-year stabilization) in full. **Finland.** The property-
and credit-fuelled boom's unwind was harsher on the real economy than Sweden's: real GDP fell
**11% cumulatively 1990–93**, real consumption **10%**, investment collapsed to **55% of its 1990
level** — the episode is known domestically as the "Finnish Great Depression." Bank loan losses rose
from **0.5% (1989) to 4.7% (1992)**. **L12 lesson, distinct from the credit monograph's banking-crisis
framing of the same episode.** The property-price evidence here isolates a specific structural
vulnerability the credit-cycle literature alone underweights: a *first-cycle* liberalized system —
banks, borrowers, and regulators alike with no lived experience of a full boom-bust round trip under
the new rules — produced one of the sharpest property repricings in this entire record, sharper in
relative terms than several economies with far longer credit histories. This bears directly on how
L12 should read India's own post-liberalization cohorts: the RERA-2016/GST-2017 regime (§B3 below) is
itself a structural reset comparable in kind, if not in mechanism, to 1980s Nordic deregulation, and
the Nordic case argues for weighting India's *post*-RERA property cycle (2021+) as a genuinely new,
inexperienced regime rather than a simple continuation of the pre-2013 boom's dynamics.

### 6. Hong Kong, 1997–2003 — deflation without a banking crisis

**The setup.** Hong Kong's residential property market peaked in 1997, at the crest of a
pre-handover mania, under the territory's **Linked Exchange Rate System** — a currency-board peg of
**HKD 7.8 = USD 1**, in place since October 1983 and never devalued, including through the entire
1997–98 Asian Financial Crisis. **The bust, magnitude verified.** Residential property prices fell
**~58% from 1997 to 2003** on the most commonly cited headline figure, with some measures putting the
cumulative fall as steep as **61–65%** by the Q3 2003 trough — one of the deepest sustained property
declines in this entire record, rivaling Ireland's and exceeding Spain's, sustained over **six years**.
**The mechanism — the currency-board deflation variant.** Because the peg foreclosed the standard
exit valve every other case in this record eventually used in some form (devaluation, independent
monetary easing, or in the euro cases' absence of that valve, an internal devaluation accompanied by
a sovereign crisis), Hong Kong's entire post-1997 adjustment had to run through **domestic price
deflation** — property, wages, and the general price level all falling together — rather than a
currency-driven repricing. The distinguishing fact that makes this case a genuinely separate variant,
not merely a smaller Greece: **Hong Kong's banking sector did not experience a systemic crisis** —
conservative loan-to-value underwriting and well-capitalized banks meant negative equity was absorbed
directly on **household** balance sheets over a multi-year deflationary grind rather than crystallizing
as bank losses requiring recapitalization. **L12 lesson.** Hong Kong isolates the *property-price*
channel of a fixed-exchange-rate bust from the *banking-crisis* channel that usually accompanies it
(compare the credit monograph's own euro-era cases, where the currency constraint and a banking
crisis arrive together) — proving that a pegged or hard-anchored currency regime can, on its own,
without any bank failure at all, produce a Japan-scale magnitude of real property-price destruction
purely through the deflation mechanism. For L12's own design this argues for treating "exchange-rate
regime flexibility" as a conditioning variable on how a given financial-cycle bust is *expressed*
(banking crisis vs. pure price deflation vs. currency crisis) rather than on *whether* one occurs —
consistent with FC1's finding that the underlying credit-property amplification (median corr +0.40,
17/17 countries positive) holds regardless of exchange-rate regime, even though the resolution
channel visibly does not.

### 7. China, 2021–present — the managed-descent experiment, extended to its property core

**The presale system — the property-cycle-specific mechanism the credit monograph's banking framing
does not carry.** Chinese developers have historically sold the overwhelming majority of new homes
*before* construction completion: presales still accounted for **68% of new-home sales by floor
space in 2025**, and presale deposits plus mortgage proceeds together made up **~40–45% of developer
funding** (one late-2025 reading: deposits/advances/mortgages **44.6%** of the funding pool, versus
**36.1%** from developers' own self-raised funds) — meaning Chinese homebuyers were, in effect, the
system's single largest unsecured creditor class, financing construction with cash paid years before
delivery. **The three red lines** (August 2020) then cut off the *next* layer of financing at exactly
this system's most leveraged moment: liabilities/assets capped at **70%**, net debt/equity below
**100%**, and cash-to-short-term-debt required at **1.0× or higher** — a direct, administrative
deleveraging mandate (the same tool, note, that ended Japan's 1980s boom: MOF quantity controls in
1990) rather than a market-driven credit tightening. **The bust.** Evergrande — carrying **$300bn+**
in total liabilities, with **~$23bn** specifically in offshore debt it could not restructure — was
ordered into liquidation by a Hong Kong court on **29 January 2024**. Country Garden's total
liabilities stood at **~¥1.36 trillion (~$190bn)** as of mid-2023; it defaulted on **~$11bn** of
offshore bonds in October 2023 and has since pursued a restructuring proposal cutting its **$16.4bn**
offshore debt stock by **~70%** and its weighted average financing cost from **~5.8% to ~1–2.5%**.
**Price magnitude, updated to the current print.** The NBS 70-city new-home price index had fallen
**over 14% cumulatively from its August 2021 peak** through late 2024, and the decline streak reached
**32 consecutive months of month-on-month contraction through February 2026** — the longest sustained
national price decline on record for the series; secondary-market (existing-home) prices in tier-1
cities (Beijing, Shanghai, Shenzhen) are down **less than 10%** from their 2021 peaks, while smaller
tier-3 cities have fallen considerably further, a bifurcation the credit monograph's aggregate
property-investment figures (starts down ~two-thirds, sales down over half, from its own case #7) do
not resolve city-by-city. **The system dismantling itself, live.** As recently as August 2026,
Chinese regulators moved to raise the threshold for new-home presales and, under new central-bank and
financial-regulator guidance, tie mortgage disbursement to project *completion* rather than presale
status — the financing mechanism that enabled the entire 2009–2021 boom is now, in real time, being
unwound, a structural change with no completed historical analogue in this record. **Honest
outcome-unknown, extended.** The credit monograph's own case #7 already states the caveat that this
episode has produced neither a classical banking panic nor a completed Japan-style workout; this
Part's property-specific addition is that the *presale* mechanism means the household-level exposure
here is qualitatively different from every prior case — millions of buyers hold claims on
already-paid-for, undelivered homes, a delivery-risk channel with no analogue in Japan, Spain, Ireland,
or Hong Kong, where the buyer already owned a completed, occupiable asset even as its price fell.
**L12 lesson.** A state-directed, presale-financed property system can suppress every classical
market signal (bank-equity crash, currency collapse, bond-spread blowout) that the rest of this
record uses to *date* a bust, while the underlying physical adjustment proceeds on its own multi-year
schedule regardless — directly reinforcing the credit monograph's "age of an unresolved extreme
state" design point (its own case #7 lesson) and demonstrating that the property-specific transmission
channel (delivery risk on pre-paid, undelivered units) can matter as much to household balance sheets
as the price channel this Part otherwise tracks throughout.

### 8. Australia and Canada — the un-burst controls, doubled and updated honestly

**Australia — still the clean control, and further extended.** Australian household debt sits at
**~182% of income (Q4 2024)**, among the highest in the world; the national dwelling **value-to-income
ratio reached 8.2 in September 2025**, against a 20-year average of **6.8**, and mortgage repayments
now consume a record **50.6% of income** on the median-priced home (late 2024) — **only 14%** of
median-income households can afford the median dwelling, down from **43% just three years earlier**.
Forecasters expect **a further 6–10% rise in 2026**, taking values to fresh records. Supply-side
research attributes the persistence directly to the Glaeser-Gyourko mechanism L12 already encodes:
strict zoning, slow approvals, and infrastructure bottlenecks constrain new construction in
high-demand areas, while net migration has run well ahead of dwelling completions since the pandemic.
Australia also raised interest rates far less aggressively than its Anglophone peers through 2022–24,
removing one of the demand-side shocks that hit the other "control" economies. **Canada — the honest
update this record must carry.** As of the most current data available (mid-2026), Canada is **no
longer** a clean un-burst control: the national MLS Home Price Index stood at **$661,800 in July
2026**, **~20–21% below** its **March 2022 peak of $841,100**, having declined through the second half
of 2025 and into 2026 (Ontario and British Columbia hit hardest, roughly **−3% year-on-year** as of
mid-2026 on top of the earlier fall). The proximate driver: an October 2024 immigration crackdown
produced a **~100,000-person population decline in 2025** — the first since WWII — directly reversing
the demand side that had kept Canadian prices elevated. A separately-compiled real-terms cross-check
puts Canada's peak-to-trough real decline closer to **17%**, marked in that source as an already-
completed correction `[VERIFY: whether the Canadian correction was in fact complete by the compiling
date, or whether the mid-2026 softening documented above represents a fresh leg down — the two
readings are not fully reconciled by this pass]`. **New Zealand, the third leg of what is really a
trio.** NZ house prices peaked November 2021 and have fallen **~15–18% nominal** (Auckland **−25%**,
Wellington **−29%**) — in **real** terms, adjusted for inflation, the decline reaches **~28%**
nationally (Auckland **−35%**, Wellington **−40%**), with prices essentially flat for three years
running through mid-2026. **The honest reframing this Part owes the record.** What began, at the
task's own framing, as "Australia/Canada again as the un-burst controls" resolves, on the current
data, into two genuinely different outcomes from the *same* starting conditions (extreme
price-to-income ratios, high household leverage, a multi-decade run without a crash): Australia has
stayed aloft and is still climbing; Canada and New Zealand have delivered a **15–28% peak-to-trough
correction, compressed into 3–4 years, without a single banking failure or a sharp one-year crash** —
a genuine "un-crash": the same magnitude of real adjustment several of the crisis cases above achieved
through a discrete bust, achieved instead through a slow multi-year grind. **L12 lesson, doubled per
the task's own instruction.** First: a HIGH price-to-income state can persist for two to three
*decades* with no date-certain resolution — Australia's ratio has been elevated relative to its own
20-year average for most of that window, and any L12 design that reads "extreme" as an implicit timing
signal would have been wrong for most of the last twenty years running. Second, and this is the sharper
point the Canada/NZ update supplies: **identical entry conditions do not determine the exit path** —
the same starting state (extreme ratio, high leverage, long unburst run) resolved via a discrete,
severe crash in Spain and Ireland, via a multi-decade grinding stagnation in Japan, and via a
comparatively mild multi-year correction with no crisis at all in Canada and New Zealand. This is the
single strongest argument in the entire property-cycle record for L12's Tier-C, reduce-only,
state-classification-only mandate (matching L15's identical mandate in the debt-supercycle monograph,
for the identical structural reason): the entry state is observable and genuinely informative (FC1's
17/17 co-movement, FC3's elevated crisis odds at cycle peaks); the *timing and severity of the exit*
is not forecastable from that same state, and a design that tried to time it would be fitting noise.

---

## B3. India's property record in full

**The 2003–2013 boom.** India's real-estate sector entered a sustained boom from roughly 2002–03,
concurrent with — and amplified by — the economy's strongest sustained growth run (also the setting
for the debt-supercycle monograph's own India case: general-government debt/GDP falling from
**~84–86% (2003) to a ~66–67% trough around 2010–11**, a growth-led decline with a favorable r−g
backdrop for credit expansion generally). City-level price appreciation in the mid-2000s was extreme
by any cross-country standard in this record: one widely cited compilation of National Housing Bank
data puts city price indices (2003=100) at **Delhi 269 and Bengaluru 275 by 2007** — a near-tripling
in four years — against **Mumbai 178 and Kolkata 172** over the same window
`[VERIFY: the exact primary NHB source and index construction for these specific city-level 2003=100
figures — a search pass could confirm the NHB RESIDEX program's existence and structure but not
independently re-derive this precise table from a primary release]`. Year-on-year growth rates in the
boom's hottest years matched: Delhi ran **+34.0% (2006), +33.8% (2007)**; Bengaluru ran **+33.0%
(2003)** and **+27.8% to +31.8%** in the following years; Mumbai's pace was somewhat cooler but still
elevated, **+12.9% to +25.8%** across the same window. India's own **official** house-price index
infrastructure lagged the boom it was meant to measure: the NHB **RESIDEX** program began as a **2005
pilot in five cities** (Bengaluru, Bhopal, Delhi, Kolkata, Mumbai) using **2001 as its base year** to
stay comparable with WPI/CPI, capturing 2001–2005 price movement retrospectively before extending to
2007; it was **officially launched in July 2007** on a **2007 base**, and by its final pre-relaunch
edition (Jan–Mar 2013) covered **26 cities**. In other words: for the boom's most explosive years
(2003–2005), India's only official price-tracking apparatus was still a five-city pilot reconstructing
history after the fact — the first instance of the measurement-honesty problem this section closes
with.

**The 2013–2020 stagnation — the invisible correction.** Following the 2011–12 growth slowdown, Indian
residential prices in most markets stopped rising in any meaningful sense: RBI's own quarterly House
Price Index (ten cities: Mumbai, Delhi, Chennai, Kolkata, Bengaluru, Lucknow, Ahmedabad, Jaipur,
Kanpur, Kochi) shows **double-digit annual growth from 2010–2016, peaking at +26.3% year-on-year in
Q4 2011**, then decelerating sharply to just **~3.7%/year on average, 2017–2020** — a period explicitly
attributed to the compounding shocks of **demonetisation (Nov 2016), GST (July 2017), and RERA
(2016–17)** landing in close succession. Nominal flatness of **~3–5%/year** against CPI inflation
running at a comparable or higher rate for most of 2013–2020 means the arithmetic is unambiguous:
**real house prices fell in most Indian metros across this seven-year window**, even though headline
nominal indices rarely showed an outright *nominal* decline — precisely the "invisible correction" the
task names, a stagnation dressed as stability because the loss shows up only after deflating, not in
the raw nominal print a casual observer would check. This is the Indian instance of exactly the
pattern Spain, the US, and Japan display as sharp nominal *and* real falls; India's own version ran
quieter, longer, and — because circle-rate-anchored transaction reporting and infrequent official
index updates blunt the signal further (see the measurement-honesty discussion below) — was easy to
miss in real time.

**The IL&FS/NBFC link — tying directly to the credit monograph.** By the mid-2010s, commercial banks
had already substantially retreated from real-estate developer lending following the post-2013 NPA
recognition cycle, leaving **non-bank finance companies (NBFCs) and housing finance companies (HFCs)
as developers' primary — in many cases sole — remaining source of construction and land-acquisition
finance**: NBFC exposure to real estate stood at **~7.5% of the sector's book, or ~₹1.65 trillion, as
of March 2018**. The September 2018 default of **Infrastructure Leasing & Financial Services
(IL&FS)** — CYCLE_ATLAS's own **"NBFC/shadow-credit sub-cycle" (L10 sub-component, n=1 clean episode:
2014→2018→2020)** — triggered a sector-wide NBFC funding freeze that hit real-estate developers with
particular force precisely *because* they had become so dependent on this single channel: with banks
already retreated and NBFCs now themselves frozen out of wholesale funding, developer financing
effectively seized up across the board, delaying project completions nationwide and deepening the
stagnation already under way from demand-side weakness. This is the clean, documented transmission
mechanism connecting a shadow-banking credit event (the credit monograph's own subject matter) to a
multi-year real-side property outcome (this Part's subject matter) — the two monographs' cases meeting
at a single, dated event.

**RERA 2016 and GST as the structural reset.** The **Real Estate (Regulation and Development) Act,
2016** (RERA) — enacted 2016, brought into force in stages through 2017 — was designed explicitly to
address the sector's chronic pathologies: project-completion delays, diversion of buyer funds to
unrelated projects, opaque carpet-area-vs-super-area pricing, and one-sided builder agreements. Its
core structural mechanisms include mandatory project registration, an escrow requirement confining a
defined share of buyer receipts to the specific project they were collected for, and a **five-year
structural-defect liability** running from possession. **GST**, layered on in July 2017, initially
taxed under-construction property at **12%** (with input tax credit) and affordable housing at **8%**;
the GST Council cut these to **5% (standard) and 1% (affordable housing)** effective **1 April 2019**,
in both cases *without* input-tax-credit eligibility. Together, RERA and GST constitute a genuine
structural regime change comparable in kind — though very different in mechanism — to the Nordic
liberalization this Part's case 5 covers: a first-cycle set of rules for developers, lenders, and
buyers alike, with the 2013–2020 stagnation itself serving as the adjustment window during which the
industry consolidated around the new regime (smaller, undercapitalized developers were disproportionately
squeezed out by the escrow and disclosure requirements, a consolidation that shows up directly in the
current upcycle's supply concentration).

**The 2021–2026 upcycle.** Residential sales hit a **record 302,867 units in 2024** (roughly **+11%
year-on-year**), before momentum cooled through 2025: sales across the top seven cities fell **~14%
year-on-year to ~3.96 lakh units** in 2025 from **~4.59 lakh** in 2024, even as new launches edged up
**~2% to ~4.19 lakh units** — a volume-declining, launch-flat market. Despite the volume fall, **total
sales value rose ~6% to over ₹6 lakh crore** (from **~₹5.68 lakh crore**), the clearest single
statistic of the upcycle's defining character: **premiumization**, buyers concentrating into fewer,
larger, costlier units even as unit counts soften. Inventory remains within the textbook-healthy
range: the quarters-to-sell (QTS) ratio stood at **5.8 quarters (~17.4 months)** against a
conventionally healthy band of **18–24 months**, though the **₹2–5 crore bracket specifically saw
unsold inventory surge ~47% year-on-year**, a pocket of oversupply sitting inside an otherwise
balanced aggregate.

**Luxury-vs-affordable divergence — the upcycle's clearest structural feature.** Homes priced **above
₹2.5 crore** rose from **18% to over 21% of new launches** between 2024 and 2025; luxury residences
crossed **over 50% of total sales value in 2024** nationally. The divergence in unsold inventory is
the sharpest single statistic: **luxury unsold stock grew ~24% year-on-year to over 1.13 lakh units**
(from ~91,125), while **affordable-segment (under ₹40 lakh) unsold stock fell ~19% year-on-year to
~1.13 lakh units** (from ~1.40 lakh) — luxury oversupply and affordable undersupply converging to
almost the identical absolute unit count from opposite directions, a genuinely striking symmetry that
captures the entire post-2021 upcycle in one number: developers, chasing the higher-margin
premiumization trend, have systematically under-built the segment actual first-time buyers can afford.

**The measurement honesty this desk owes itself.** Three separate factors mean India's official
property data structurally *understates* the true amplitude of its own cycles, and any L12 input
built on them must carry this caveat explicitly. First, the **black-money/circle-rate gap**: in prime
localities (Delhi's Golf Links, Sunder Nagar, and comparable pockets elsewhere) market prices exceed
government-notified circle rates by **50–70%**, and — because Indian tax law (Section 50C/56 of the
Income Tax Act) treats a gap beyond roughly **10%** of the circle rate as taxable "deemed income" to
both parties — the incentive structure this creates has historically pushed a portion of true
transaction value into unrecorded cash ("on-money"), meaning registered, tax-reported transaction
prices — the raw input to most official indices, including RESIDEX — can sit meaningfully below the
true market clearing price, especially in high-value, high-cash-intensity segments and locations.
Second, **the official index infrastructure itself has been unstable**: NHB RESIDEX, launched 2007,
expanded to 26 cities by 2013, was updated only "periodically" through roughly 2015 before effectively
lapsing as the primary official series `[VERIFY: exact current operational status and coverage of
NHB RESIDEX post-2015 versus its 2013-era 26-city peak]`, leaving RBI's own quarterly HPI — ten cities,
published with a reporting lag, based on registration-authority data that inherits the circle-rate
problem above — as the closest thing India has to a Case-Shiller- or BIS-equivalent national series;
no unified, continuously-published, high-frequency Indian house-price index comparable to the US or
European members of the BIS panel currently exists. Third, and following directly from the first two:
**a genuine cycle-amplitude comparison against any of the eight cross-country cases in B2 above is
not currently possible for India on official data alone** — the 2013–2020 "invisible correction" this
section documents is itself evidence of exactly how much a thin, lagged, cash-blind measurement
apparatus can mute a real cycle's visible signature, which is the single most important reason L12's
own design (DESIGN.md) tags India's evidence as **Tier C** on cycle length even while the cross-country
mechanism itself sits at Tier B.

---

## B4. Synthesis

### The table — verified figures only

| Case | Real HP peak-to-trough | Duration | Bank/GDP damage | Equity drawdown |
|---|---|---|---|---|
| Japan 1991–2005 | Residential land ~−40%; commercial land −70 to −80% | ~14y (1991–2005) | ~20% of Japan's bad-loan stock traced to golf-course collateral alone; multi-decade zombie-lending | Nikkei 225 −80% (Dec1989–2003); price level not regained until Feb 2024 (34y) |
| US 2000–2012 | National index ~−42.5% real (Case-Shiller, Q1'06–Q1'12); ~−27% nominal (National), ~−33–35% nominal (Composite) | 6y (2006–2012) | Systemic (credit monograph's own case); GFC-scale | not case-specific here; GFC-era S&P 500 fall `[VERIFY exact %, credit-deep's domain]` |
| Spain 2007–2014 | ~−41% real (cross-check source) | ~7y | Cajas sector effectively wiped out; SAREB bad bank (2012) | IBEX 35 ~−50% (Nov2007–Oct2008) |
| Ireland 2007–2013 | −54.4% nominal (CSO RPPI, Apr2007–Mar2013) | ~6y down; ~15y full round trip back above 2007 peak (2022) | Credit monograph's own case #9 (banking side) | not recomputed here `[VERIFY: cross-ref credit-deep]` |
| Sweden 1989–1993 | ~−25% nominal by end-1993; ~−30% real (cross-check source) | ~4y | Loan losses 0.3%→7% (1989→1992); Nordbanken/Gota Bank rescue (credit-deep case #5) | not retrieved `[VERIFY]` |
| Finland 1989–1993 | not separately retrieved `[VERIFY]` | ~4y | Loan losses 0.5%→4.7% (1989→1992); GDP −11% cumulative (1990–93) | not retrieved `[VERIFY]` |
| Hong Kong 1997–2003 | ~−58% (headline); range −58% to −65% across sources | ~6y | None — no systemic banking crisis; household balance sheets absorbed negative equity | not retrieved `[VERIFY]` |
| China 2021–present | NBS 70-city index ~−14%+ cumulative (Aug2021–late2024); 32 consecutive months of MoM contraction through Feb 2026; tier-1 secondary <−10%, tier-3 much worse | 4y+, ongoing, outcome unknown | Evergrande liquidated (Jan 2024, $300bn+ liabilities); Country Garden defaulted ($11bn, Oct 2023) on $190bn total liabilities | No market-wide equity crash (credit-deep case #7) |
| Australia (control) | 0% — still rising; price/income 8.2x (Sep2025) vs 6.8x 20y avg | 30y+ unburst | None | N/A |
| Canada (re-examined) | ~−17% to −21% (nominal, Mar2022 peak to Jul2026) `[VERIFY: complete vs still-deepening]` | ~4y, ongoing as of mid-2026 | None — no banking crisis | N/A |
| New Zealand (bonus) | ~−28% real (Nov2021 peak) | ~4–5y, flat since | None | N/A |
| India, full arc | Real terms: nominal flat (~3–5%/yr) vs CPI, 2013–2020 → cumulative real fall over 7y `[VERIFY: precise magnitude — official series too thin to compute directly]` | Boom 2003–2013 (10y); stagnation 2013–2020 (7y); upcycle 2021–2026+ | IL&FS/NBFC freeze 2018–20 (credit-deep's own sub-cycle); no systemic bank crisis from property specifically | not retrieved `[VERIFY]` |

### Eight pooled conclusions, ranked by evidence strength, mapped to L12

1. **(Strongest — FC1's own 17-of-17-country co-movement result, corroborated in every boom leg
   above.)** Credit and property prices amplify each other on the way up in every single case in this
   record without exception, exactly as FC1 finds pooled (median corr +0.40). → **Design implication:**
   L12's construction as a macro-credit-block member (sharing budget with L6/L10/L11 per DESIGN.md) is
   correct — property price alone, decoupled from the credit aggregate driving it, is not the right
   unit of analysis; the two must always be read together, never singly.
2. **(Strong — Japan, Hong Kong, and the Ireland/Spain contrast all independently confirm.)** A
   property cycle's *turning point* is dramatically slower to confirm than an equity cycle's: Japan's
   13-year decline had no single crash day; even Case-Shiller, the best-instrumented series in the
   world, cannot produce an uncontested single trough month for the 2006–2012 US bust. →
   **Design implication:** this is the direct empirical grounding for L12's phase-uncertainty-only
   design (DESIGN.md: "never a date") and for FC2's own lengthening finding (11y→13y median spacing
   post-1985) — the trend toward *slower* cycles argues for widening, not narrowing, L12's phase
   uncertainty band over time, not the reverse.
3. **(Strong — Spain's ghost airports and China's presale-financed delivery risk, two structurally
   different mechanisms converging on the same point.)** A property bust's *physical* overhang (excess
   units, unfinished infrastructure, undelivered presold homes) clears far more slowly than its
   *financial* overhang — Spain's construction sector stayed depressed for the better part of a decade
   after its banks were recapitalized; China's presale delivery-risk channel has no completed
   historical analogue and continues to evolve four-plus years in. → **Design implication:** L12's
   own long τ½ (60–96 months, per DESIGN.md) should be read as a floor, not a ceiling, on how long a
   HIGH property-cycle state can persist once triggered — the real-side adjustment, not the credit
   adjustment, is usually the binding constraint on how fast the state can revert.
4. **(Strong — the doubled Australia/Canada/NZ case, the record's single cleanest natural
   experiment.)** Identical entry conditions (extreme price-to-income ratio, high household leverage,
   multi-decade unburst run) produced three genuinely different exits from the same starting point:
   Australia still climbing, Canada and New Zealand delivering a 15–28% multi-year correction with no
   crisis at all, while Japan/Spain/Ireland/Hong Kong delivered 40–65%+ crashes from comparably
   elevated (if not always identically extreme) starting states. → **Design implication:** this is the
   single strongest argument in the property-cycle record for L12's Tier-C, reduce-only,
   state-classification-only mandate — the entry state is observable and informative (this is FC1 and
   FC3's job); the exit path and severity are not forecastable from that state alone, and a design that
   tried to time either would be fitting noise onto a genuinely underdetermined outcome.
5. **(Moderate-strong — Nordic 1987–93 and India's own RERA/GST reset, a cross-country mechanism
   corroborated by one clean domestic instance.)** A "liberalization cohort" — banks, borrowers, and
   regulators operating for the first time under a newly deregulated or newly re-regulated system —
   shows systematically sharper repricing than an established-regime cycle of comparable credit growth;
   Finland and Sweden's 1987 deregulation-linked bust and the qualitatively similar post-RERA regime
   change India is still inside both point the same direction. → **Design implication:** L12 should
   weight India's post-2021 upcycle as occurring inside a still-young, still-untested regulatory
   regime (RERA/GST, in force less than a decade) rather than as a simple continuation of the
   pre-2013 boom's dynamics — the Nordic analogue argues this specific combination (new rules, first
   full cycle under them) carries elevated, not average, tail risk until at least one full round trip
   has been observed under the new regime.
6. **(Moderate — Hong Kong as the clean isolate, a single but structurally unambiguous natural
   experiment.)** A pegged or hard-anchored exchange rate can, entirely on its own, produce a
   Japan-scale magnitude of real property-price destruction through pure domestic deflation, with zero
   banking-sector crisis required — proving the property-price channel and the banking-crisis channel,
   which usually arrive bundled together in this literature, are in fact mechanistically separable. →
   **Design implication:** L12 should not infer "no banking crisis observed" as evidence that a
   property-cycle bust is mild or contained; Hong Kong's ~58–65% real fall with zero systemic bank
   failures is proof that the banking channel's silence is not informative about the property channel's
   severity.
7. **(Moderate — India's own documented, but thinly measured, 2013–2020 arc; the strongest available
   domestic evidence, appropriately Tier C on magnitude per the Contract's own tiering rule.)** India
   ran a genuine seven-year real-terms property correction that was nearly invisible in nominal,
   headline-level data — the RESIDEX/RBI-HPI measurement apparatus is thin enough, and cash-transaction
   leakage large enough, that a real cycle of this duration produced no obvious nominal signature. →
   **Design implication:** any India-specific L12 input must be explicitly flagged Tier C on magnitude
   (matching CYCLE_ATLAS.md's own existing tag) and should prefer *real*, CPI-deflated readings of the
   RBI HPI over nominal ones by default — India's own case is direct proof that nominal flatness and
   real decline can coexist for years without the gap being visible in the headline series a casual
   read would consult.
8. **(Moderate — China's presale mechanism, a single ongoing case but a structurally novel one with
   no completed historical analogue anywhere else in this record.)** A state-directed, presale-financed
   property system can suppress every classical crisis marker (bank-equity crash, currency collapse,
   bond-spread blowout) this literature otherwise relies on to observe a bust in progress, while the
   real, physical adjustment (starts down ~two-thirds, sales down over half, per the credit monograph's
   own figures) proceeds regardless — and adds a household delivery-risk channel with no parallel
   elsewhere in this record. → **Design implication:** directly reinforces the credit monograph's own
   "age of an unresolved extreme state is itself informative" design point (its case #7), and argues
   that any China-linked exposure in the book should discount market-based signals (equity, currency,
   spreads) specifically for the property-sector channel, weighting physical/administrative data
   (starts, presale-rule changes, developer liquidations) more heavily than the market-based inputs
   L10 otherwise defaults to.

---

## Side-task — GitHub-hosted mirrors for atlas 1.1 property data

Per the 2026-09-01 mirror-authorization decision (`research/OPEN_QUESTIONS.md`), only
`raw.githubusercontent.com`, `media.githubusercontent.com`, and `objects.githubusercontent.com`
(release assets) are reachable from this environment. Using `mcp__github__search_code`, the following
were found. **Nothing was downloaded** — existence, content-shape, and a first-pass credibility
judgment only.

1. **`datasets/house-prices-global`** — `data/real_year.csv`, `data/real_index.csv`,
   `data/nominal_year.csv`, `data/nominal_index.csv`. A genuine, structured mirror of the **BIS
   residential property price statistics "selected" dataset** — confirmed content shows per-country,
   per-quarter rows (e.g. Italy from 1927/1947 onward) in both nominal and real, level and
   year-on-year-change form, matching the BIS's own stated coverage (~59 countries) exactly. This is
   the same "datasets" open-data-collective org pattern the debt-supercycle monograph's own side-task
   already found reliable. **Credibility: high.**
   `https://raw.githubusercontent.com/datasets/house-prices-global/82eed8d7549deb7cc3fa14c6261d692a6bf2e215/data/real_year.csv`
2. **`johnkearns617/AEIEconDataRelease`** — `Data/data_save/CSUSHPISA.csv`. A genuine committed
   long-history mirror of the **Case-Shiller U.S. National Home Price Index**, explicitly covering
   **1987-01-01 through 2025-06-01** monthly per its own FRED-sourced metadata columns — this is the
   long Case-Shiller series the task asks for, not merely a same-day snapshot. **Credibility:
   medium-high** — an economics-research-tooling repository (AEI-adjacent per its name) with correctly
   structured FRED-vintage metadata, though not the BLS/S&P primary source itself.
   `https://raw.githubusercontent.com/johnkearns617/AEIEconDataRelease/315ebb66eff75d630a0d3779a75e6d45f735c851/Data/data_save/CSUSHPISA.csv`
3. **`itsmanasa-dev/RealVest`** — `Datasets/Bengaluru-City HPI Data Current-Q (Base Year 2013).xls`.
   A scraped capture of the **NHB RESIDEX Bengaluru dashboard** (`residex.nhbonline.org.in`) — the file
   is, unusually, an HTML/SVG chart export saved with an `.xls` extension rather than genuine tabular
   data, but it carries a hidden accessible data table with real recovered index points (e.g. Jun 2013
   = 105 through Mar 2018 = 141, Base Year 2013 = 100). **Credibility: medium** — content is
   genuinely NHB-RESIDEX-sourced and the values are recoverable, but the format is non-standard and
   single-city only; `[VERIFY: cross-check the recovered index points against the primary NHB RESIDEX
   quarterly booklet before treating as authoritative]`.
   `https://raw.githubusercontent.com/itsmanasa-dev/RealVest/d507e9811aeed0735f56a8e8da73d1fba89bbd97/Datasets/Bengaluru-City%20HPI%20Data%20Current-Q%20(Base%20Year%202013).xls`
4. **`michael-zumba/bytemind-website`** — `reports/property-market-analysis/data/figure8_international_real_price_declines.csv`.
   A compiled secondary cross-check table, "Peak-to-trough real house price declines by country,"
   confirmed content: Ireland −54%, Spain −41%, Sweden −30%, Canada −17%, Australia −5%* (ongoing),
   New Zealand −12%* (ongoing) — the same repository's `figure_sources_and_methodology.csv` documents
   these as author-compiled readings off the **BIS long real-HPI series** and the **OECD
   price-to-income indicator**. **Credibility: medium** — a personal analyst compilation rather than a
   primary vendor, but internally consistent with, and independently corroborating, several of this
   Part's own WebSearch-sourced figures (notably Ireland's −54% matching CSO's own RPPI exactly).
   `https://raw.githubusercontent.com/michael-zumba/bytemind-website/49ca5cb81f76faad8ac71f591fb27d756cd99365/reports/property-market-analysis/data/figure8_international_real_price_declines.csv`
5. **Knoll-Schularick-Steger — confirmed gap, not an omission.** No standalone GitHub-vendored copy of
   the original KSS 1870–2012 dataset (the AER 2017 paper's own replication files live on openICPSR,
   not GitHub) was located. The only GitHub-hosted trace found is `benjaminpeeters/wpd`'s R-package
   metadata file (`inst/extdata/METADATA_Y.csv`), which confirms the series ships **only inside JST R6**
   as `HPNOM_JST` ("House prices, nominal index, 1990=100," sourced to Jordà et al. 2017/2019) alongside
   `HOUSING_TR_JST` (total return) and `HOUSING_RENT_YD_JST` (rental yield) — but this is metadata
   describing the R package's variable list, not a vendored copy of the underlying values. **This
   directly answers the task's own question: no richer standalone KSS house-price dataset exists on
   GitHub beyond what our own atlas already draws from JST R6's `hpnom` field** — the pre-1950 flat
   portion of the hockey stick this Part's B1 relies on comes from the *academic* AER paper and its
   openICPSR replication archive (not egress-reachable from this environment per the same
   mirror-authorization decision), not from any GitHub mirror.
   `https://raw.githubusercontent.com/benjaminpeeters/wpd/dd881ceef43dab73e6f766bba5adf279fdb4c20a/inst/extdata/METADATA_Y.csv`
6. **NHB RESIDEX or RBI HPI — no clean, multi-city, primary-format mirror found beyond item 3 above.**
   Several repositories (`Jaswanthchowdary18/AI-Home-Renovation`, `ramanujamgond/financial-advisor-llm`)
   *reference* NHB RESIDEX or RBI HPI by name in planning/README documents as an intended future data
   source, but none of them vendor an actual multi-city extract; a genuine, primary-format, multi-city
   NHB RESIDEX or RBI HPI historical CSV remains a principal's-machine task (a direct RBI DBIE pull),
   exactly as the debt-supercycle monograph's own side-task found for the IMF Global Debt Database's
   bulk export and an India repression-history panel.

---

## References

Knoll, Schularick & Steger (2017). "No Price Like Home: Global House Prices, 1870–2012." *American
Economic Review* 107(2): 331–353; CESifo WP 5006. · BIS, *Residential Property Price Statistics*
(quarterly database) and *Handbook on Residential Property Prices*. · Jordà, Knoll, Kuvshinov,
Schularick & Taylor (2019). "The Rate of Return on Everything, 1870–2015." *QJE* 134(3): 1225–1298
(already the basis of DS1–DS4 and, via `hpnom`, this monograph's own FC1–FC3). · S&P CoreLogic
Case-Shiller U.S. National and Composite Home Price Indices (FRED series CSUSHPISA/CSUSHPINSA). ·
CSO Ireland, *Residential Property Price Index*. · Statistics Sweden / Statistics Finland, Nordic
banking-crisis-era house-price series. · Hong Kong Monetary Authority, *The Property Market and the
Macro-Economy*; HKMA, *The Currency Board Arrangement in Hong Kong, China*. · NBS China, 70-city new
construction commercial residential building price index. · National Housing Bank, *NHB RESIDEX*. ·
Reserve Bank of India, quarterly *House Price Index*. · RERA (Real Estate Regulation and Development
Act, 2016); GST Council notifications on real-estate rates (Feb 2019). · Glaeser & Gyourko (2018).
"The Economic Implications of Housing Supply." *Journal of Economic Perspectives* 32(1) (already
CYCLE_ATLAS.md's own L12 mechanism citation). · Drehmann, Borio & Tsatsaronis (various), on financial-
cycle length (already the basis of FC2). · `research/cycles/credit-deep/partB-cross-country.md`
(banking-crisis mechanics for the shared cases, cross-referenced throughout, never recomputed here).
· `research/cycles/debt-deep/partB-cases.md` (house style; L15's Tier-C mandate, the direct structural
analogue to L12's own). · GitHub mirror URLs per the side-task section, confirmed via
`mcp__github__search_code` this session.


---

# PART B-RESULTS — Real data: JST R6 (FC1–FC3)

# Atlas 1.1 — financial cycle: JST R6 results (FC1-FC3)

Combined financial-cycle state = mean of expanding percentiles of the credit/GDP and
REAL house-price Hamilton gaps (h=5y, p=1; parameter-free per country). House-price
coverage limits the panel (hpnom availability). Generated 2026-09-01; trials ledgered.

## FC1 — Credit and property amplify each other (the co-movement claim)

- corr(5y Δcredit/GDP, 5y Δlog real house prices), per country: median **+0.40**, 17/17 positive.
- Borio's amplification claim passes the sign-consistency bar that demographics
  failed — this is what a REAL pooled regularity looks like next to a narrative one.

## FC2 — Length, pre vs post liberalization

- Peak-to-peak spacing of the combined state: pre-1985 median **11y** (n=33), post-1985 median **13y** (n=32).
- Direction matches Drehmann-Borio's lengthening finding (their ~11y -> ~20y on
  bandpass methods); our expanding construction is deliberately cruder — the
  DIRECTION, not the level, is the pre-registered check (feeds H65b and the
  tau_half_drift_policy lengthening watch for L10-L12).

## FC3 — Crises at the cycle's peaks (both grid cells, honest)

| Peak definition | crisis within ±3y | vs random 7y window | elevation |
|---|---|---|---|
| loose (state>0.6, n=81) | 22% | 18% | 1.2x |
| major (state>0.8, n=52) | 23% | 18% | 1.3x |

- HONEST READ (interpretation written AFTER the print, per the standing rule): the
  loose-peak cell is barely above base — shallow local maxima dilute the test. The
  major-peak cell is the Borio-relevant one; its elevation is reported above exactly
  as measured. Either way the seat's PRIMARY evidence remains FC1's 17/17 co-movement
  and the credit monograph's own AUROC work — FC3 grades the PEAK-DATING use, which
  stays out of bounds regardless (states, never dates).



---

# PART C — Data engineering: measuring India's property cycle, free

# Part C — Data engineering: measuring India's property cycle, free

v1.0 · 2026-09-01 · Extends `jst-fincycle-RESULTS.md` (FC1–FC3: the combined financial-cycle state
as the mean of expanding percentiles of the credit/GDP and real-house-price Hamilton gaps, h=5y,
p=1, parameter-free per country) and `docs/masterplan/A-data-catalog.md` block **G4** — the *only*
existing catalog line touching this cycle at all (RBI HPI). This Part's job is the gap the catalog
leaves, the same first-build gap credit-deep Part C found for the NBFC layer and debt-deep Part C
found for centre/state debt stocks: **no catalog entry exists for NHB RESIDEX, housing-finance-
company (HFC) credit, RERA project registrations, stamp-duty/registration counts, or a housing-
specific construction-materials proxy** — this Part supplies all five, corrects one date A-catalog
G4 got wrong, and adds the city-expansion detail G4 did not have. Consumes `research/CONTRACT.md`
§3 (free-source mandate), §4 (evidence tiers, Tier-C reduce-only), §8 (no HP filter — Hamilton 2018
only), Known Prior #11 (no live network access here; ingestion on the principal's machine, every
indicator against a committed fixture). Feeds `config/ladder.yaml` **L12_realestate_medium_cycle**
(tier B, `reduce_only: false`, `block: macro_credit_block`, `inputs: [L10_credit_block]`). Structure
follows `research/cycles/debt-deep/partC-data.md` (the style bar this Part matches); the bank+NBFC
aggregation method follows `research/cycles/credit-deep/partC-data.md` §C.2, mirrored below to
bank+HFC. Checked by web search this pass (snippet-level, cross-checked across ≥2 results where
feasible; nothing fetched directly). Anything not so corroborated carries **[VERIFY]**.

---

## C.1 RBI House Price Index — the primary series, and the break sitting inside it right now

**Coverage, base, methodology (legacy series, 2010–2025).** The Reserve Bank compiles a quarterly
house price index (HPI, base **2010-11=100**) for **ten** major cities — Mumbai, Delhi, Chennai,
Kolkata, Bengaluru, Lucknow, Ahmedabad, Jaipur, Kanpur and Kochi. Construction is a chain-linked
stratified index built from **transaction-level data supplied by state Registration/Stamps
Departments** (actual registered sale-deed prices, not listings or valuations): for each
ward/administrative zone and quarter, properties are bucketed into three floor-space-area (FSA)
classes (small/medium/large); a simple average price per square metre is computed per class per
ward; classes are combined using weights fixed at the **base-period transaction mix (April
2010–March 2011)**; successive quarters chain-link onto the base rather than re-basing each time.
Data exists from **June 2010** (reference quarter Q1:2010-11) onward. The **all-India composite**
is a weighted average of the ten city indices, weighted by each city's **2011 Census population** —
a fixed weight, never re-estimated between Census years, a genuine if minor source of composite
drift as city populations diverge from their 2011 shares over a 15-year span.

**Publication lag.** NHB's comparably-constructed RESIDEX (§C.2) runs ~10–13 weeks; RBI's HPI is on
the faster end — Q1:2026-27 (quarter ended 2026-06-30) was released **2026-08-24**, an ~8-week lag;
earlier editions ran closer to 10–12 weeks (A-catalog G4's estimate). **[VERIFY]** any stated RBI
SLA; treat 8–13 weeks as the working range, not a point figure.

**Revision behavior — [VERIFY], a structural risk, not a confirmed fact.** The index is built from
registration-authority filings, and registration itself can lag the underlying transaction by weeks
(a statutory registration window applies) — a quarter's first print could in principle be revised
upward as late filings for that quarter are folded in. **No RBI documentation of an explicit
revision policy was found this pass**; a build script should difference successive vintages of the
same reference quarter to detect the answer empirically rather than assume either "never revised"
or "revised like GDP."

**The break sitting inside the series right now — base changed to 2022-23, coverage expanded to 18
cities, October 2025.** A-catalog G4 flagged this transition as "appearing around the Q2 FY2025-26
reporting cycle" without a confirmed date; that guess is corrected here. RBI released the HPI for
**Q1:2025-26** (reference quarter Apr–Jun 2025) on **2025-10-10**, on a **new base year (2022-23
=100)** and **expanded coverage to eighteen cities** — the original ten plus **Hyderabad,
Thiruvananthapuram, Pune, Ghaziabad, Thane, Gautam Buddha Nagar, Chandigarh and Nagpur**. A
retrospective back-series was published from Q1:2022-23, i.e., the **new-base series' own native
history starts in 2022-23**, not a backward extension of the 2010-11-base series. **This is a
genuine level break, identical in kind to NHB RESIDEX's own 2018 break (§C.2) and this monograph's
debt-deep Part C's documented 2026 CPI/GDP/IIP rebase wave** — never fit a Hamilton gap or a
percentile rank through it. Construction rule: treat the **2010-11-base, 10-city series as the long
history (2010–2025)**; treat the **2022-23-base, 18-city series as the current-vintage tail from
Q1:2025-26 forward**; splice with a ratio-at-overlap using the legacy series' last reported quarter
(`k = HPI_new(t0)/HPI_old(t0)`), the same pre-registered choice and argument credit-deep Part C
§C.3 makes for GDP base transitions. **[VERIFY]** whether the 18-city composite re-weights by a
newer population base or extends 2011 Census weights arithmetically to the eight new cities — not
confirmed either way this pass.

| Field | Legacy series (2010-25) | Current series (2025→) |
|---|---|---|
| Base | 2010-11 = 100 | 2022-23 = 100 |
| Cities | 10 | 18 (+8) |
| Native history | June 2010 → ~Q1:2025-26 | Back-series from Q1:2022-23; live from Q1:2025-26 |
| First live print under this base | (was itself new once, ~2011) | 2025-10-10, for Q1:2025-26 |
| Weighting | 2011 Census city population, fixed | **[VERIFY]** — population-base unconfirmed |

---

## C.2 NHB RESIDEX — the 2018 break, two price concepts, and current status (not discontinued)

**History.** NHB RESIDEX launched **July 2007**, base year 2007, for **five** cities (Bengaluru,
Bhopal, Delhi, Kolkata, Mumbai), gradually expanded to **26 cities**, then **stopped updating after
March 2015** (a multi-year gap, not a discontinuation announcement). It was **revamped and
relaunched in July 2017**, republished quarterly with base year **FY2012-13=100**. **The genuine
methodology break**: from the **April–June 2018 quarter**, the base shifted again, to
**FY2017-18=100** — a second rebase inside one year of relaunch, the one the task brief's "2018
methodology overhaul" names. **Current coverage: 50 cities** (18 State/UT capitals plus 37 "smart
cities," with overlap). **Status: active, not discontinued** — quarterly releases continue through
at least Q1 2026 [VERIFY exact latest print at first live pull; corroborated into 2025–2026 across
≥2 independent sources, but the most recent point value came from a single tertiary aggregator
(TradingEconomics), so treat that specific number as single-source].

**Two structurally different price concepts, not two cuts of one dataset.** RESIDEX publishes both:

| Version | Data source | What it actually measures |
|---|---|---|
| **HPI @ Assessment Prices** | Valuation data supplied by **banks and HFCs** | The price lenders assign to a property for loan-sanctioning purposes — a conservative, loan-to-value-anchored figure, not a transaction price |
| **HPI @ Market Prices** | Primary (under-construction) and secondary (resale) market listing/deal data | Closer to an actual asking/transacted price, for both new-launch and resale segments |

This is a genuinely different construction from RBI's HPI (§C.1), which is registration-price-only:
RESIDEX's assessment-price leg is a *lender's* number, not a market number, and its market-price leg
draws partly on listing data with the same asking-vs-transacted gap flagged for aggregators
generally (§C.6). **Neither RESIDEX version should be blended with RBI's HPI into one series** —
they answer different questions (bank collateral valuation vs. registered transaction price vs.
market listing/deal price) and any cross-check between them is a divergence to log, not an
inconsistency to reconcile away.

**Publication lag.** Quarter ended March 2024 → released **2024-06-11**, an ~10-week lag, in line
with RBI HPI's own range (§C.1). A **2013 ambition to move RESIDEX to a monthly cadence** was
reported at the time but the headline release remains quarterly through 2024–2026 per every source
checked this pass — **[VERIFY]** whether any individual-city sub-series ever went monthly; treat the
composite as quarterly-only until confirmed otherwise.

---

## C.3 Housing credit — the longer, faster proxy, and the bank+HFC aggregate

Both price series above are short (RBI HPI's usable native history is 15 years; RESIDEX's is
shorter still after the 2015 gap and 2018 rebase). Housing **credit** is the faster-updating,
longer-history leg the design needs to carry L12 through the years the price legs cannot cover
(§C.8's warm-up arithmetic makes this precise).

**Bank housing credit — RBI Sectoral Deployment of Bank Credit.** "Housing (Including Priority
Sector Housing)" is a named sub-line under the **Personal Loans** major head of the monthly
Sectoral Deployment release (`rbi.org.in/Scripts/Data_Sectoral_Deployment.aspx`; same filing stream
documented at A-catalog G1 and credit-deep Part C §C.1 — **not re-derived here**, only extended to
the housing-specific sub-line). Two facts this Part adds to the credit-deep base layer:

1. **Sample, not census.** Compiled from **40 select scheduled commercial banks**, ~93% of total
   non-food credit of all SCBs — a high-coverage proxy, but a proxy; the ~7% gap is unlikely
   housing-concentrated but is unquantified free of charge.
2. **The same January 2019 reporting-format break credit-deep Part C §C.1 names for the NBFC-in-
   Services sub-line applies to Housing and Commercial Real Estate too** — sub-sector definitions
   changed at that boundary; **[VERIFY]** the exact delta for Housing specifically (confirmed for
   NBFCs, not independently re-confirmed for Housing this pass).

**Commercial real estate / developer credit — the supply-side leg, same release.** "Commercial Real
Estate" is a separate named sub-line under **Services** in the same Sectoral Deployment release
(recent prints show ~16% y-o-y growth in this line) — this is the free, monthly, developer-side
credit proxy the task asks for, sourced from the identical filing as the household-side Housing
line, same publication lag (~3 weeks post month-end), same Jan-2019 format-break caveat.

**Housing Finance Companies (HFCs) — the shadow-credit leg, and a regulatory-lineage break of its
own.** HFCs were **NHB-regulated** from NHB's founding (1988) until the **Finance (No. 2) Act,
2019** amended the National Housing Bank Act; HFC regulatory power transferred to the **RBI**
effective **2019-08-09**, and HFCs are now formally classified as **one category of NBFC**. This is
a genuine data-lineage break: pre-Aug-2019 HFC prudential data flowed through NHB's own supervisory
returns; post-Aug-2019 through RBI's NBFC-HFC statistical returns — same entities, a different
regulator collecting the numbers, a documented date to flag on any HFC series crossing it. Two free
publications carry HFC aggregates:

| Source | What it carries | Cadence / lag |
|---|---|---|
| **NHB "Report on Trend and Progress of Housing in India"** | Sector-wide housing credit picture: HFC total loan portfolio, housing vs. non-housing split, PLI (Primary Lending Institution) performance, individual-housing-loans-outstanding aggregate (banks + HFCs combined) | Annual, released with a long lag — the FY2024-25 edition was hosted under a 2026-02 upload path, i.e., roughly an **11-month-plus lag** past FY-end (March) |
| **RBI Financial Stability Report, NBFC chapter** | HFCs as a sub-category of the NBFC sector's consolidated balance sheet, GNPA, capital adequacy (same chapter credit-deep Part C §C.2 already documents for NBFCs generally) | Biannual (June/December editions) |

Illustrative levels (both flagged as third-party-repeated NHB/ICRA figures, not this Part's own
computation): individual housing loans outstanding (banks + HFCs) **₹33.53 lakh crore at end-Sept
2024** (+14% y-o-y, NHB); HFCs' total loan portfolio **₹9.57 trillion at end-March 2024** (+14.36%
y-o-y; housing loans within that +11.88%, non-housing — loan-against-property, developer/construction
finance — +21%, ICRA industry estimate, **[VERIFY, commercial third-party, not primary NHB data]**).

**The bank+HFC aggregate — mirroring credit-deep Part C §C.2's bank+NBFC rule exactly, with one
added nuance.** Construction: `housing_credit_total = housing_credit_bank + (hfc_credit_total −
bank_credit_to_HFCs)`, netting bank lending *to* HFCs out of the HFC leg before summing, for the
identical double-counting reason credit-deep Part C documents (bank credit to HFCs already sits
inside `housing_credit_bank`'s parent Sectoral Deployment aggregate as part of bank credit *to
NBFCs*, since HFCs are now formally an NBFC sub-category — post-Aug-2019 this netting is literally
the same netting operation credit-deep's L10 construction already performs, not a second,
independent one to re-derive). **Frequency mismatch, same discipline**: bank housing credit is
monthly (~3-week lag); HFC credit is NHB-Trend-and-Progress-anchored (annual, ~11-month lag) or
RBI-FSR-anchored (biannual) — the combined series can only be as fresh as its slowest leg unless
upsampled by piecewise-linear log-interpolation between successive HFC reference dates, with a
staleness mask once a new edition is overdue, identical to credit-deep Part C §C.10's convention.

**The shared-block awareness this construction owes L10.** Because HFCs are now formally an NBFC
sub-category, L12's housing-credit leg is a *subset* of L10's own bank+NBFC aggregate, not an
independent measurement — `ladder.yaml`'s own comment on `macro_credit_block` ("shared by
L6+L10+L11+L12, de-duplication rule §4.2") already anticipates this overlap. Rule: **build the
housing-specific credit leg from Sectoral Deployment's own Housing/CRE sub-lines directly, never by
re-slicing L10's already-aggregated total** — the sub-line data is separately published at the same
source, so no re-derivation is required, but the two seats' outputs are not independent draws and
should never both be cited as separately-corroborating evidence of one underlying credit expansion.

---

## C.4 Supply-side free data — RERA, listings, and the classic materials proxies

**RERA state portals — genuinely scrapable, genuinely not a bulk download.** Every state runs its
own Real Estate Regulatory Authority under the central RERA Act, 2016 (MahaRERA, Karnataka RERA,
UP-RERA, TS-RERA, Gujarat RERA, etc.) — **there is no central, unified, bulk-downloadable national
RERA database**; each portal is a project-by-project search interface (by registration number or
project name), not a documented public API (**[VERIFY]** for all 28 states/UTs — confirmed this
pass only for Maharashtra and Karnataka). Third-party aggregators (`reradetails.in`, `rerawebsite.in`,
`realatic.com`) already scrape multiple state portals into unified search tools — evidence the
underlying sites are technically scrapable, not evidence a free bulk feed exists. **Budget a
state-wise RERA project-registry build as a genuine multi-week scraping project** (identical framing
to A-catalog's own IPO-anchor-registry item), starting with the five largest markets by
registration volume — Maharashtra, Karnataka, Telangana, Uttar Pradesh, Gujarat.

**Listing aggregators (99acres, MagicBricks, Housing.com/PropTiger, NoBroker) and industry-report
inventory data (ANAROCK, Knight Frank, JLL, CBRE) — exploration-only, mirroring the screener.in
rule.** These sources carry launches, unsold inventory, and asking prices at a city/micro-market
level, none behind a documented free bulk API, and — the disqualifying property, per the
2026-09-01 mirror-authorization decision (`research/OPEN_QUESTIONS.md`, applied identically in
value-deep Part C §C.6 to screener.in) — **no vintage layer**: a pull today shows today's
best-known snapshot, not what the site showed at any past date, so a backtest built on a scraped
history silently reintroduces the look-ahead bias Known Prior #7 already prices at 150–450bps/yr
for fundamentals. **Fine for fast exploration, never as the fixture a signal is evaluated against.**
Illustrative numbers (context only, not admissible evidence): unsold inventory across eight major
markets **~5.26 lakh units, H1 2026** (Knight Frank) vs. **~6.16 lakh units** on ANAROCK's own count
for the same broad period, a different city set and methodology — the two disagreeing by that much
is itself demonstration of why neither is a fixture-grade series.

**Cement production — Index of Eight Core Industries (ICI).** Cement carries a **5.37% weight**
within the ICI (itself ~40.27% of overall IIP weight), compiled by the **Office of the Economic
Adviser (OEA), DPIIT, Ministry of Commerce & Industry** — the same body that compiles WPI
(A-catalog H2). Released monthly on the **last working day of the following month** (~4-week lag),
first provisional, later revised — the standard two-vintage cadence RBI/MOSPI series generally
carry. **A base-year rebase is itself in-flight**: OEA released a revised Core Industries series
with base year **2022-23** around **2026-07-20**, the same 2026 rebase wave debt-deep Part C §C.11
documents for GDP/CPI/WPI/IIP — cement's ICI sub-index inherits that break.

**Steel consumption — Joint Plant Committee (JPC), Ministry of Steel.** JPC publishes monthly
finished-steel apparent-consumption bulletins (`jpcsteel.co.in`) — the classic construction-demand
cross-check alongside cement, at the same monthly cadence; **[VERIFY]** exact publication lag (not
independently pinned this pass; industry commentary implies a similar ~3–4 week lag to the ICI).

**Construction GVA — quarterly national accounts.** MOSPI's quarterly GDP/GVA release (already
documented at credit-deep Part C §C.3 — series from reference quarter Q1:1996-97, ~2-month lag) 
breaks the economy into three broad sectors; **Construction sits in the Secondary sector**
(alongside Manufacturing and Electricity/Gas/Water), at **~8% of nominal GVA in FY2025-26**, second
only to Manufacturing within that sector — this is the free, official, quarterly supply-side
building-activity flow. **Do not confuse it with "Real Estate, Ownership of Dwelling & Professional
Services,"** a *Tertiary*-sector GVA category dominated by imputed owner-occupied rent, a
stock/asset-services concept, not a construction-activity flow — the two categories are adjacent in
every press release table and easy to conflate; only "Construction" answers the supply-side
question this section is built for. Same 2026 rebase wave applies (base 2011-12 → 2022-23, per
debt-deep Part C §C.11's already-documented GDP transition), inherited without re-derivation here.

| Series | Compiler | Cadence | Lag | Weight/share | 2026 rebase status |
|---|---|---|---|---|---|
| Cement production (ICI) | OEA, DPIIT | Monthly | ~4 weeks | 5.37% of ICI | New base 2022-23, ~2026-07-20 |
| Finished-steel apparent consumption | JPC, Min. of Steel | Monthly | **[VERIFY]** | — | Not confirmed rebased this pass |
| IIP "Infrastructure/Construction Goods" (use-based) | MOSPI | Monthly | ~6 weeks | ~12.3% of IIP | New base 2022-23 from May-2026 (per A-catalog H3) |
| Construction GVA | MOSPI (National Accounts) | Quarterly | ~2 months | ~8% of nominal GVA | New base 2022-23 from 2026-02-27 |

---

## C.5 Transaction-side — registration counts, stamp duty, and home-loan disbursals

**Property registration counts and stamp duty collections.** The primary free source is each
state's own Registration/Stamps department portal; **Maharashtra's IGR** (`igrmaharashtra.gov.in`)
is the standard reference case — Maharashtra records over 10 lakh property registrations annually,
Mumbai alone contributing roughly 30%, and the portal exposes a daily/monthly registration-count and
revenue e-search facility. In practice the free, already-cleaned, ready-to-use version of this data
is **Knight Frank India's monthly Mumbai/Pune registration notes**, which state explicitly that they
are built from Maharashtra's Department of Registrations and Stamps' own published figures — i.e.,
Knight Frank does the state-portal scraping already, and republishes it monthly with a short lag
(within days of month-end for Mumbai; the underlying IGR data is available directly, if scraped
independently, essentially in near-real time). **[VERIFY]** the equivalent portal quality and
release cadence for the next-largest markets (Karnataka's Kaveri Online, Delhi's e-registration
system, Telangana's IGRS) — Maharashtra's IGR is confirmed as the best-documented case this pass,
not necessarily representative of every state.

**State budget documents.** Every state's own Budget "Receipts" annex carries stamp-duty-and-
registration-fee collections as a distinct revenue head, annual, with the same multi-month
publication lag general state fiscal data carries (debt-deep Part C §C.4's State Finances caveats
apply identically here) — useful as an annual cross-check on the monthly IGR-style flow data, not a
substitute for it.

**Home-loan disbursal data.** No free, structured, economy-wide *disbursal* (vs. *outstanding-
balance*) series was found this pass — Sectoral Deployment and NHB's Trend and Progress report both
give **outstanding stock** and its growth rate, a close but distinct concept from gross disbursal
(new loans originated, gross of repayments/prepayments). CRIF High Mark and Care/ICRA sector reports
carry disbursal-level detail but are paid products outside the Contract's free-source mandate — flag
**out of free reach**; the Sectoral Deployment growth rate is the free substitute, understood as a
*net* flow, not the gross figure a lender-side dataset would show.

---

## C.6 Price cross-checks — listing indices, and the circle-rate honesty note

**Listing-portal price indices** (99acres' own "Insite" index, MagicBricks' "PropIndex," Housing.com's
price trackers) exist and are free to view, but inherit the identical exploration-only rule §C.4
already states for inventory data — asking prices, not transacted prices, with no vintage archive
and no documented free bulk API. Use them only as a directional cross-check against RBI HPI/RESIDEX
movements in the same quarter (do the signs agree?), never as an input series.

**The circle-rate / ready-reckoner honesty note — bias direction stated, not hedged.** Every state
sets a minimum registerable transaction value (Maharashtra: "Ready Reckoner Rate";
Delhi/UP/Haryana/Punjab: "Circle Rate"/"Collector Rate"); a sale priced below this floor is deemed to
occur *at* the circle rate for stamp-duty and capital-gains purposes regardless of the actual
consideration paid — backstopped by Section 56(2)(x) of the Income Tax Act (any gap above ₹50,000
between declared price and circle rate is taxed as income to the buyer). The direction this forces
on every registration-based series (RBI HPI, RESIDEX's assessment leg, any IGR-derived stamp-duty
series): **where a cash/"black" component still rides on top of the registered price, circle rates
put a floor under what gets *reported*, so registered prices systematically run below true
transacted prices, and the gap widens exactly when informal-premium behavior is most active —
late-cycle, speculative phases.** The design's registration-price-based gauges therefore carry a
**structural downward bias in cycle amplitude, concentrated at peaks** — a documented narrowing of
the circle-rate/market-value gap in recent years reduces but does not eliminate this bias, and its
size is not independently quantifiable free. State this bias direction inline wherever the L12 price
leg is shown, the same discipline debt-deep Part C §C.8 applies to the pre-1991 administered-rate
caveat: a known, dated, one-directional distortion to disclose, not silently correct for.

---

## C.7 Vintage/PIT hazard table

| Series | Revision-prone? | Two dates never to conflate | Store first-print or every vintage? |
|---|---|---|---|
| RBI HPI | **Yes, structurally** — 2022-23/18-city rebase (2025-10-10, first print for Q1:2025-26); registration-lag revision risk within a base unconfirmed [VERIFY] | Base-transition date vs. reference quarter; within-base first-print vs. any later revision | Both bases kept distinct, checksum + vintage each; never overwrite |
| NHB RESIDEX | Yes — two dated breaks (2015 series lapse/2017 relaunch at FY2012-13 base; April–June 2018 quarter rebase to FY2017-18) | Relaunch date vs. rebase date — two separate events, both level breaks | Every base-year vintage kept distinct |
| RBI Sectoral Deployment — Housing/CRE sub-lines | Format break, not a value revision | January 2019 reporting-format change (confirmed for NBFC-in-Services, [VERIFY] for Housing/CRE specifically) | Old-format (pre-2019) and new-format series kept distinct |
| HFC credit (NHB Trend & Progress / RBI FSR) | Regulatory-lineage break, not a value revision | 2019-08-09 (HFC regulation transferred NHB→RBI; HFCs reclassified as an NBFC sub-category) | Flag pre-/post-2019-08-09 on any HFC-specific series |
| Cement (ICI), IIP Infra/Construction Goods, Construction GVA | Yes — all three inherit the 2026 base-2022-23 rebase wave (debt-deep Part C §C.11) | Rebase effective date (ICI ~2026-07-20; IIP May-2026; GVA 2026-02-27) vs. reference period | Both bases kept distinct per series |
| RERA project registrations | Not revision-prone in the GDP sense, but **status-mutable** — a project's registration record (timeline, completion %) is live-updated by the developer, so "today's snapshot" ≠ "the record as of any past date" | Snapshot-pull date vs. project's own last-updated date | Snapshot each pull, dated — no vintage archive exists upstream to rely on |
| Listing-aggregator inventory/price data | No vintage layer upstream at all (§C.4/§C.6) | N/A — exploration-only, never stored as a fixture for evaluation | Do not build a backtest-grade fixture from this source |
| IGR/stamp-duty registration counts | Not typically revised once posted, but state-specific cadence/format varies | Portal posting date vs. actual registration date (can lag by the statutory registration window) | Monthly snapshot, dated; cross-check against annual state Budget figures |
| Circle rate / ready reckoner rate | Event-based (rate-revision notifications), not a data revision | Notification effective date vs. any later news-report date | Append-only event log, dated by the state notification's effective date — same discipline debt-deep Part C §C.11 applies to SLR/CRR |

---

## C.8 The L12 India pipeline — from raw pulls to the two-leg state

**A design tension to resolve first, explicitly.** `ladder.yaml`'s L12 entry carries `inputs:
[L10_credit_block]` — a DAG edge to the *total* bank+NBFC credit/GDP gap L10 already builds — while
its own `indicator` field names `"RBI HPI, housing credit, RBI FSR"`, and this Part's brief calls
for a **housing-credit-specific** long leg (§C.3), not a re-use of L10's economy-wide aggregate.
JST's pooled construction (`jst-fincycle-RESULTS.md`'s header) uses generic, not sector-specific,
credit — that is what the global panel offers. **Resolution, argued**: build L12's credit leg from
the Sectoral Deployment Housing+CRE sub-lines directly (§C.3) — a more precise read of the
housing-driven leg than total credit, which mixes in unrelated industry lending — and retain the
L10 DAG edge strictly as a **validation cross-check**: confirming FC1's co-movement finding
(corr(Δcredit/GDP, Δlog real house prices), median +0.40, 17/17 countries) holds when India's own
housing-specific credit gap is compared against its house-price gap, never as a substitute
computation. Per Contract §5, this departure from the pooled paper's literal construction is
recorded with its argument, not silently substituted.

1. **Registry load.** Validate `config/ladder.yaml` L12 against `config/validator.py` before any
   pull, same gate every other seat's pipeline uses.
2. **Pull raw fixtures** into `data/fixtures/P_realestate/{rbi_hpi_legacy,rbi_hpi_2022base,
   nhb_residex,sectoral_deployment_housing,sectoral_deployment_cre,nhb_trend_progress,rbi_fsr_nbfc,
   rera_state_{state},igr_maharashtra,ici_cement,jpc_steel,iip_construction_goods,
   construction_gva}/{vintage}/...` — a genuinely new fixture family (no existing `ingest/pull_*.py`
   script covers any of these; see closing note). Manifest immediately
   (`python ingest/manifest.py data/`), every file keyed `(series_id, vintage_date, pull_date)`.
3. **STEP 1 — credit leg (the long leg).** Build `housing_credit_total = housing_credit_bank +
   (hfc_credit_total − bank_credit_to_HFCs)` per §C.3; apply Hamilton's (2018) regression filter
   (h=5y=60 months, p=1 lag, monthly — never the HP filter, Contract §8) to the credit/GDP ratio
   (nominal GDP denominator per credit-deep Part C §C.3's own ratio-splice convention); compute the
   **expanding percentile** against India's own history from the series' effective start
   (**[VERIFY]** exact month the Housing sub-line begins — bracket ~1998–2007; A-catalog G1 anchors
   the parent Sectoral Deployment release at ~1998). Warm-up: h+p=61 months lost before the first
   gap, plus a 48-month min-obs floor (mirroring the Contract's own "≥4 observations" Tier-B floor,
   scaled to monthly cadence) — first trustworthy credit-leg percentile lands **≈2003–2012**
   depending on the confirmed start date, comfortably ahead of the price leg.
4. **STEP 2 — price leg (short leg, warm-up stated honestly).** Splice the RBI HPI legacy (2010-11
   base) and current (2022-23 base) series per §C.1's ratio-splice rule; apply the same Hamilton
   filter (h=5y=20 quarters, p=1) to the real house-price level (deflated by CPI-Combined, itself
   spliced across its own 2011/2024/2026 base changes per debt-deep Part C §C.9 — not re-derived
   here). Warm-up: h+p=21 quarters lost from the June-2010 start → first gap **≈2015–2016**; a
   16-quarter min-obs floor → first trustworthy price-leg percentile **≈2019–2020** — the "supports
   ranks only from ~2020" fact the brief names, derived here, not assumed.
5. **STEP 3 — combine, with the India-length Tier-C clamp.** Before the price leg clears warm-up
   (pre-~2020): `L12_state = credit_leg_percentile` alone — the price leg is masked, not defaulted
   to neutral. From ~2020 onward: `L12_state` remains `credit_leg_percentile` as the primary read
   (the credit leg independently qualifies for Tier B via the Contract §4 "n<4 domestic + ≥10
   cross-country analogues" branch — Claessens-Kose-Terrones' panel, per `ladder.yaml`'s own L12
   provenance), and the **price-leg percentile is routed through the existing `tierC_overlay`
   mechanism** (`budgets.tierC_overlay_cap: 0.10`, negative-only shift of regime score R — the same
   generic channel L1/L13/L14 already use, no bespoke L12-only overlay invented): when the
   price-gap percentile is *also* extreme (>0.8) and the credit-gap is elevated, it can pull the
   score down within that existing budget; it can never push L12's contribution up beyond what the
   credit leg alone shows. **This is a deliberate departure from JST's symmetric mean-of-two-
   percentiles construction**, justified because India's house-price series has **zero completed
   domestic cycles** (n=0, stricter than L12's own "India n=1" credit-leg citation) and no
   cross-country-analogues branch rescues a country-specific *rank* the way it rescues the
   *existence* of the underlying concept — per Contract §4, an input this thin may only reduce
   risk, never add it. `changes_if`: revisit a full symmetric 50/50 mean once RBI HPI carries
   ~25–30 years of native history — not before the mid-2030s at the earliest.
6. **STEP 4 — supply/transaction-side context, not scored.** Cement (ICI), steel (JPC), IIP
   Infra/Construction Goods, and Construction GVA (§C.4) feed a **narrative supply-tightness
   cross-check** alongside the scored two-leg state — none carries enough India-specific cyclical
   history on its own to earn a ladder seat; they inform the Stage-2 narrative layer (red team) the
   way debt-deep Part C routes contingent liabilities there (§C.9 below).
7. **STEP 5 — state as a phase object.** Log L12 as (level, velocity, quadrant, age-in-quadrant) per
   the 2026-09-01 states-as-phase-objects decision (`research/OPEN_QUESTIONS.md`), not a scalar —
   identical discipline to debt-deep Part C §C.12 step 6.
8. **STEP 6 — regime-score expression.** Feed `macro_credit_block` (0.20 of the regime-score budget,
   shared with L6/L10/L11 per `ladder.yaml`'s own de-duplication rule §4.2) — L12 is additive here,
   unlike L15/L16, which have no regime-score seat at all.
9. **Manifest every derived fixture** (credit-leg and price-leg gap/percentile, combined-state
   panel) as its own versioned, checksummed artifact; corrections append a new vintage row, never
   overwrite.
10. **Recalibration triggers**: a new RBI HPI base/coverage change (already happened once, 2025-10);
    a new NHB RESIDEX base change; a Sectoral Deployment reporting-format change; a CPI/GDP rebase
    flowing into the deflator/denominator; a Core-Industries/IIP rebase flowing into the
    supply-side context series; the first India-domestic completed medium-cycle leg (unlocks
    re-arguing the credit leg's own frozen parameters, per `ladder.yaml`'s own `changes_if`).
11. **Grids** (per `state_phase_convention`, unchanged for L12): `slope_horizon_grid_periods:
    [3, 6, 12]`, `smoothing_grid_periods: [1, 3, 6]`, `deadband_percentile_grid: [0.15, 0.25, 0.35]`
    — pre-registered, chosen once by tau_half (60–96 months), then frozen.
12. **Monitor**: quarterly refresh (bound by the price leg, the slower leg); annual review re-reads
    FC1–FC3 with one more year of India data; the 2030 design review re-reads the whole seat,
    unchanged in cadence from debt-deep Part C §C.12 step 10.

---

## C.9 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **True transaction prices** (vs. registered prices) | Circle-rate floors and any residual cash component are unobservable in any public document by construction (§C.6) | Registration-based HPI/RESIDEX as the measured floor, bias direction (understated amplitude, worst at peaks) stated inline |
| **Unsold inventory, precisely and nationally** | No government census exists free; NHB itself was reported (Dec 2021) *seeking an external agency* to build one — confirmation the gap is real | ANAROCK/Knight Frank/PropTiger city-level estimates, exploration-only (§C.4), cross-checked for rough magnitude, never scored |
| **Developer leverage, granularly** (project debt, cost overruns, presales funding) | RERA discloses project *status and timelines*, not *balance sheets*; developer financials sit behind the same constraints value-deep Part C documents for listed names, and most developers are unlisted | Commercial Real Estate credit growth (§C.3) as an aggregate, sector-wide leverage-direction proxy only |
| **Land banks** (developer-held undeveloped land, valuation) | No free, structured disclosure exists outside listed-developer annual-report footnotes (inconsistent, unaggregated) | Named as a known-unknown in the Stage-2 narrative layer, identical framing to debt-deep Part C §C.13's contingent-liabilities treatment |
| **A single reconciled "the" house-price series** | RBI HPI, RESIDEX@Assessment, RESIDEX@Market, and listing indices measure four different things (registered / bank-valuation / market / asking price), no published bridge | Report each with source and construction stated; a persistent gap is a regime signal (§C.2), not a data error to average away |

---

## C.10 Runsheet additions for the principal's machine

No existing `ingest/pull_*.py` script covers any real-estate or housing-credit source — a larger
first-build gap than credit-deep Part C's NBFC layer, closer in scale to value-deep Part C's "no
fundamentals script exists at all" finding. Proposed additions to A-catalog §4's Phase-0 runsheet
(numbered as extensions past its existing 16 steps):

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 17 | Pull RBI HPI, both bases (legacy 10-city 2010-11, current 18-city 2022-23); confirm overlap window for the ratio-splice | §C.1 | 3–4 | Small, DBIE-adjacent (same portal family as G4), highest-priority price leg |
| 18 | Pull NHB RESIDEX, both post-2017 base vintages (FY2012-13, FY2017-18), both price concepts (Assessment/Market) | §C.2 | 3–4 | Second price cross-check; confirm current publication status live (this pass's confidence is search-only) |
| 19 | Pull Sectoral Deployment Housing + Commercial Real Estate sub-lines, full monthly history, both format eras (pre-/post-Jan-2019) | §C.3 | 2–3 | Piggybacks on the DBIE scraper credit-deep Part C's own runsheet step already budgets — same portal, two more sub-lines |
| 20 | Pull NHB "Trend and Progress of Housing in India" (all available annual editions) and RBI FSR NBFC chapters (HFC-specific tables), hand-transcribe | §C.3 | 3–4 | Manual PDF transcription, same discipline as credit-deep's own FSR/GNPA step |
| 21 | Build one state's RERA scraper end-to-end (Maharashtra MahaRERA first) as a template; confirm scrapability and rate-limit behavior before committing to a multi-state build | §C.4 | 6–10 | Genuinely new construction, not a download — start with one state to de-risk the approach before scaling to Karnataka/Telangana/UP/Gujarat |
| 22 | Pull cement (ICI), IIP Infrastructure/Construction Goods, finished-steel consumption (JPC), Construction GVA — all four, both pre-/post-2026-rebase vintages where applicable | §C.4 | 2–3 | Cheap, stable, mechanically easy; batch with the existing MOSPI/OEA pulls credit-deep Part C's runsheet already schedules |
| 23 | Build the Maharashtra IGR scraper (or confirm Knight Frank's own monthly notes are a sufficient free proxy before building one) | §C.5 | 4–6 | Confirm the cheaper substitute (Knight Frank's republished IGR data) covers the need before budgeting the heavier direct-portal scrape |
| 24 | `config/` registry + CI validator smoke-test against the newly-pulled L12 fixtures | all above | 2 | Confirms the pull satisfies the "every module runs on fixtures with zero live data" gate, same as A-catalog's own step 16 |

**Total estimated incremental effort: ~25–36 hours**, on top of A-catalog's existing ~45–60-hour
Phase-0 estimate — driven mainly by step 21's RERA build, the one item here with no existing scraper
to extend and no structured free bulk source to fall back on.

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §5 (survival argument for the JST-construction departure in §C.8), §8
(no HP filter), Known Prior #11 (no live network access; principal's-machine ingestion);
`config/ladder.yaml` L12_realestate_medium_cycle (tier B, macro_credit_block, inputs:
[L10_credit_block]), `budgets.tierC_overlay_cap`, `state_phase_convention` grids;
`research/cycles/fincycle-deep/jst-fincycle-RESULTS.md` (FC1–FC3, the combined-state definition this
Part sources data for); `research/cycles/credit-deep/partC-data.md` (bank+NBFC method mirrored to
bank+HFC in §C.3; Sectoral Deployment base layer, extended not duplicated); `research/cycles/
debt-deep/partC-data.md` (structure/PIT discipline this Part follows; the 2026 rebase wave, inherited
in §C.4/§C.7); `research/cycles/value-deep/partC-data.md` (exploration-only rule, mirrored to
listing aggregators in §C.4/§C.6); `docs/masterplan/A-data-catalog.md` block G4 (RBI HPI — extended,
corrected, not duplicated) and §4 (Phase-0 runsheet, extended in §C.10); `research/OPEN_QUESTIONS.md`
(2026-09-01 mirror-authorization decision, §C.4/§C.6; states-as-phase-objects decision, §C.8 step 7).*

# Part D — The mathematics (atlas 1.1; shared machinery in the credit monograph's Part D)

## D1. The two-leg state and its degradation semantics

state_t = clip( (w_c·(2C_t−1)·1[C] + w_h·(2H_t−1)·1[H]) / (w_c·1[C] + w_h·1[H]), −1, 1 ),
with C = credit-gap percentile, H = real-house-price-gap percentile, 1[·] availability
indicators. n_legs = 1[C]+1[H] is a FIRST-CLASS output: a date carried by one leg is a degraded
reading, flagged to the sentinel, never silently equal-dignity with a two-leg reading. This is
India's short-HPI reality (ranks only from ~2020 on a 2010-start series) turned into API
semantics instead of a footnote — and the test suite pins it.

## D2. Both legs are impulses — where the LEVEL lives

The expanding Hamilton gap is an acceleration/turn detector (the credit monograph's measured
finding, reproduced here on the property leg: 10/10 turn collapse at −0.88..−0.97). L12
therefore contributes impulse information; boom-MATURITY (level) information inside the macro
block comes from L10's CD-ratio leg. The de-duplication rule (§4.2) in one line of algebra: the
block's information set is {credit impulse, credit level, property impulse, composition,
confirm} with ONE budget (0.20) — L12 adds the third element only, and any weight it earns is
weight L10's inputs give up inside the same cap. No stacking, ever.

## D3. What FC1-FC3 permit

FC1 (17/17 co-movement) licenses the JOINT construction. FC2 licenses only a lengthening WATCH
(direction on a crude tool). FC3's weak peak-dating (1.2-1.3x) BANS date-like use — states,
never dates, now with the seat's own measured evidence for the ban. India n≈1 completed cycle:
the India leg enters Tier-C-length (clamped contribution per ladder.yaml L12) until a second
observed downswing exists — which may take a decade; the seat is built to wait.

# Part E — The algorithm (L12, monthly/quarterly)

```
STEP 1  housing-credit leg (monthly, sectoral deployment, bank+HFC rule) and RBI HPI leg
        (quarterly, lag ~1q) per Part C's pipeline; CPI deflation for the real HP series
STEP 2  gaps: expanding Hamilton, h from the shared 16-24q grid; percentiles with warm-up
        masks (HPI leg emits NaN until min_obs ranks exist - honesty by construction)
STEP 3  state, n_legs = financial_cycle_state(credit_pct, hp_pct); n_legs on the daily page
STEP 4  consumption: inside macro_credit (0.20) via the block combiner; India-length clamp:
        the L12 contribution is reduce-only until a second domestic downswing is on record
STEP 5  supply-side confirms (cement IIP, registrations, RERA launches) enter as Tier-C
        reduce-only conditioners per Part C - never as the state itself
MONITOR quarterly leg-freshness; RESIDEX/HPI methodology-break registry entries; annual
        re-run of FC1-FC3 with new data; H65b lengthening watch feeds tau_half_drift_policy
FAILURE MODES: HPI discontinuation/rebase (breaks registry; leg to NaN -> graceful
        degradation ALREADY the tested path); registration-data lag spikes; the black-money
        wedge biasing amplitude DOWN (stated: measured cycles understate true cycles)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| macro_credit block (0.20 shared) | the property impulse leg, de-duplicated per D2 |
| Hedge scheduling | joint-boom-turn states arm hedge steps earlier (with L10) |
| Sector projection | realty/financiers conditioning (projection principle; no new seat) |
| H65b / drift policy | FC2's lengthening watch |
| Sentinel | n_legs degradation flag; leg freshness |

Designs: **FN1** India two-leg state on real data (housing-credit leg from sectoral deployment
NOW; HPI leg as ranks mature) — acceptance: sign-consistency of the two legs' co-movement with
the panel's; **FN2** the combined-vs-single-leg crisis-association test on the panel (the
Drehmann-Juselius combined-indicator claim, our tools, ledgered grid); **FN3** supply-side
confirm value (cement/registrations lead-lag vs the HPI leg, event-framed); **FN4** the
un-burst-controls tracker (Australia/Canada high-state persistence — annual read informing the
high-state-without-date discipline).

# Part H — Knowledge ledger (atlas 1.1)

**Established (panel, our runs):** credit-property amplification (FC1, the cleanest
sign-consistency pass in the project); the impulse dynamics of both legs; lengthening direction
(FC2). **Weak, honestly:** peak-dating (FC3) — banned use, now with its own evidence.
**India [C-length]:** one completed cycle; the 2013-2020 invisible real correction (Part B); the
short-HPI degradation path is the DESIGNED path for the next several years.
**Unknowable:** the current upswing's remaining length — Australia/Canada prove high states can
persist for decades; the seat conditions permissions and waits.
