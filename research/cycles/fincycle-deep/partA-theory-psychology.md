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
