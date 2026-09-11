# _CRITIC — completeness critique of the RE evidence pack

*Run 2026-09-11, after `_SYNTH-A/B/C/D` and `_AUDIT-1/2/3`. Scope: what the pack does NOT contain,
what it leans on that nobody checked, and how the project most plausibly dies. No new numbers are
claimed. **Every paper, product or portal I name below that is not already in the pack is my own
`[CRITIC-RECALL]` — model memory, zero retrieval, same epistemic class as the pack's `[RECALL]`.**
I tag it that way deliberately: the pack's structural failure was unmarked recall, and a critic who
repeats it is worthless. Treat each as a search target, not a finding.*

**One framing point before the five answers.** The pack is a well-built argument that locality
house-price prediction is not possible at the horizons the project promises, followed by four
recommendation blocks that assume it is. `_SYNTH-A` §5 says no retrieved study beats a random walk
beyond 4–8 quarters and recommends the engine be **scoped to 1–4 quarters**; `§0` of the handoff
specifies **3, 5 and 10 years**. That contradiction is unresolved anywhere in 170KB of synthesis.
Everything below is downstream of it.

---

## 1. MODALITIES NEVER RUN

Ranked by how much each would change the design, not by how interesting it is.

**1.1 The listed-developer and listed-lender disclosure channel — the largest miss in the pack.**
Nobody swept exchange filings. India's listed developers (DLF, Macrotech, Godrej Properties,
Oberoi, Prestige, Brigade, Sobha, Phoenix) publish **quarterly, audited, exchange-filed, dated,
point-in-time** pre-sales bookings *value and volume*, **average realisation per sqft**, launches,
collections, unsold inventory and net debt — often split by city and sometimes by micro-market.
Listed HFCs and housing NBFCs (HDFC lineage, LIC Housing, PNB Housing, Can Fin, Aavas, Home First,
Aptus) publish quarterly **average ticket size, average LTV at origination, geographic mix and
state-level GNPA** `[CRITIC-RECALL on the field lists; the existence of quarterly investor decks is
not in doubt]`. This matters for four reasons the pack never states:
- It is a **supply-side realised-price series that is not censored by stamp duty**, does not run
  through a Sub-Registrar, and is not an asking price. `_SYNTH-C` §1 calls RBI HPI "closest to a
  transaction-price index"; a developer's realisation per sqft on booked sales is closer still for
  the primary segment, and it is free.
- It is **point-in-time by law** — the exact property `_SYNTH-C` §3 says every private vendor lacks
  ("the disqualifying property … is the absence of a vintage layer"). Filings are archived, dated
  and immutable. This is the only India property data class that is natively backtestable.
- It sits in **the one channel this desk can actually reach.** `_TAIL-PROBE` measured 36 of 37
  endpoints blocked — but the desk already runs equity vaults and the principal's machine pulls NSE.
  The pack treats the whole India estate as one uniform acquisition problem; it is not.
- The CN programme already proved the mechanism ports: `c-presale` established that developer
  **ownership predicted survival better than any leverage ratio**, and that presale liabilities
  made the Three Red Lines blind. India's analogue (RERA 70% escrow, IBC admissions, promoter
  pledging — which the desk has *already* named as India's cleanest PIT red flag in SYNTHESIS-LH1)
  was never connected to the property engine at all.
**Design consequence:** GATE 0 currently has one route (registration microdata) with a kill
criterion attached. This is a second, cheaper, independent route to a primary-segment realisation
series, and it should be probed before a fortnight is spent on CAPTCHA flows.

**1.2 Uncensored India price series — public auctions, both ends of the cycle.** `_SYNTH-D` §2 is
seven subsections of econometrics designed to work *around* circle-rate censoring. Nobody asked
whether India publishes prices that are not censored at all. Two classes:
- **Public land auctions** — CIDCO, MHADA, HUDA/HSVP, NOIDA/Greater NOIDA, DDA, state industrial
  corporations. Auction results are published, dated, plot-identified, and the price is a real
  cleared price with no evasion incentive and no notified floor to bunch at `[CRITIC-RECALL]`. This
  is the same instrument the CN programme used for China (land revenue/volume/price) and the desk
  has the composition-artifact lesson (CN: land price −23% vs volume −66%) ready-made.
- **Distressed/forced sales** — SARFAESI bank e-auction notices and the IBAPI portal publish
  reserve prices, addresses and dates for repossessed property `[CRITIC-RECALL]`. The engine's
  headline output is "share of comparable historical states that subsequently fell 20%+", and it
  has **no forced-sale or distressed-price channel anywhere** — so the tail of every published
  distribution is imported from JST. The relevant literature is also absent: forced-sale discounts
  (Campbell, Giglio & Pathak on foreclosure discounts `[CRITIC-RECALL]`) are exactly how a −32%
  index decline becomes a −45% realised exit for a leveraged holder.

**1.3 Demography and household formation — the only variable with any claim to 10-year
forecastability, and its own canonical failure.** The pack has zero demand-side demographics: no
headship-rate literature, no household-formation projection, no internal-migration series, no
age-structure channel. For a 3/5/10-year state-conditional engine this is a hole in the exact place
the horizon lives — credit, momentum and evasion are all short-horizon mechanisms. The literature
also supplies the failure case the pack's §5 table is missing: **Mankiw & Weil (1989)** forecast a
large multi-decade real house-price decline from age structure and were badly wrong
`[CRITIC-RECALL]`. That is the closest published analogue to what this project proposes to publish
at 10 years, it failed, and it is nowhere in a pack that carefully catalogues Zillow, Flu Trends
and Himmelberg-Mayer-Sinai. India-side, NSO/Census household-size decline and the census-town
growth pattern (Mukhopadhyay's subaltern urbanisation, which `_SYNTH-C` §5 name-drops and never
uses) are the demand-side spine.

**1.4 Physical-climate risk — absent, and the desk already owns a climate vault.** No flood, heat,
groundwater, subsidence or air-quality feature anywhere in a locality-level India engine. Chennai
2015, Mumbai's recurrent flooding, Bengaluru's 2022 lake-bed inundation and Delhi NCR air quality
are locality-discriminating, publicly mapped and, unlike momentum, *forward*-looking at 10 years.
The identified literature exists (Bernstein, Gustafson & Lewis on sea-level-rise exposure
discounts; Baldauf, Garlappi & Yannelis on belief-dependent pricing of the same exposure)
`[CRITIC-RECALL]`. CLAUDE.md lists a climate vault as already vaulted and usable. This is the
cheapest genuinely new feature class on the page.

**1.5 The thin-market index literature the method menu omits.** `_SYNTH-D` §1.1 lists eleven
methods and rules out five in their own verdict column, but never lists the family built precisely
for "tens of transactions per cell": **hierarchical trend / state-space repeat-sales indices**
(Francke's hierarchical trend model and his thin-market repeat-sales work; Schulz & Werwatz's
Berlin state-space index; Nagaraja, Brown & Zhao's autoregressive index) `[CRITIC-RECALL]`. A
Kalman-filtered local trend with a city-level latent factor is the same shrinkage idea as
Fay–Herriot but in the time dimension, which is where the sparsity actually bites. Omitting the
best-fit method class while cataloguing GWR and SAR is a coverage-over-evidence signature.

**1.6 The counter-cyclical incentive stack — a mechanism, not a data source.** See §3 (the CFO).
The pack models one wedge between recorded and true price (cash under-reporting, which widens
late-cycle) and misses the second (developer discount stacks and buyer incentives, which widen in
downturns while headline price is held). Two wedges moving in opposite phases of the cycle is a
different estimator problem from one wedge.

**1.7 Countries and natural experiments never swept.**
- **Dubai / UAE.** Dubai Land Department publishes free transaction-level microdata with an open
  API, in an emerging market, through two documented crashes (2008–09, 2014–16) and with heavy
  Indian buyer participation `[CRITIC-RECALL]`. `_SYNTH-B` §1 lists ~25 countries and not this one
  — the single most India-relevant open-microdata regime, and a live NRI-flow linkage.
- **The new-town / entrant-locality question.** The handoff registers locality entry as the
  survivor artifact's sixth incarnation (Ulwe, Kokapet) and the pack supplies **no evidence base**
  for it. China's new districts, Korea's Sejong, Egypt's new capital, and India's own
  **Amaravati** — a capital announced, de-announced and re-announced, i.e. a policy reversal with a
  price series attached — are the natural experiments for exactly this. Dholera appears in the
  handoff only as a fraud warning.
- **Japan's regional dispersion post-1991** is used for the land-vs-housing multiplier (c-japan)
  and not for the question it uniquely answers: what happens to peripheral localities that were
  never established markets.

**1.8 Four smaller ones, each design-relevant.**
- **District-level credit.** RBI's BSR gives district × sector credit outstanding `[CRITIC-RECALL]`.
  The pack's credit module is national (Sectoral Deployment). District housing credit is the finest
  free credit grain in India and it is not on the twelve-row runsheet.
- **Litigation as an observable.** eCourts, NCLT/IBC real-estate admissions, RERA complaint orders
  are free, dated and text-searchable `[CRITIC-RECALL]`. Dutta-Gandhi-Green's finding is that
  **litigation, not regulation, killed India's supply response** — and the pack carries the finding
  with no proposal to measure the mechanism.
- **TDR markets and municipal fiscal capitalisation.** Mumbai's TDR is a traded instrument whose
  price is a direct read on FSI scarcity; the whole Oates-lineage fiscal-capitalisation literature
  (property tax and local amenity capitalised into price) is absent, as is land value capture.
- **Rate-transmission breaks.** The pack correctly prefers a cash-flow variable (DSR/EMI-to-income,
  per Greenwald) and then supplies an event calendar of eleven tax/RERA dates with **no
  monetary-transmission break at all** — the 2019 external-benchmark (EBLR) mandate changed how
  fast repo reaches an EMI `[CRITIC-RECALL]`. If EMI-to-income is the binding regressor, its
  transmission regime is a registrable break.
- **NRI / FX demand and gold substitution.** The desk owns a full currency battery (PPP +0.94,
  weak-INR year behaviour, 71-episode crash anatomy) and a gold series to 1833, plus CI-D2 ranking
  gold above housing in the high-and-rising-inflation state. Neither is connected to property
  demand anywhere in the pack. A weak-INR year is a testable conditioner on NRI-heavy localities.

---

## 2. LOAD-BEARING CLAIMS STILL UNVERIFIED

Ordered by how much of the design collapses if the claim is wrong. Nothing here is a new
complaint about tagging; each is a place where a `[1-SOURCE]` or `[RECALL]` item is carrying a
structural decision.

**2.1 That the circle rate censors the recorded price at all.** The entire "intellectual core"
(`handoff §4.1`, `_SYNTH-D` §2) is `observed = max(true_price, c_it)`. `_AUDIT-2` R9 refuted that
model against `A5`'s own mechanics: **duty is charged on the higher of declared price or circle
rate, which constrains the tax base, not the declared consideration** — nothing stops a deed
recording a price below the floor, so the pile-up is a behavioural equilibrium to which a Tobit
likelihood assigns probability zero. Only *Section 50C's mechanics* reached `[2-SOURCE]`. So the
project's central econometric structure rests on a mechanism its own audit says is misspecified,
and the diagnostic that would settle it (share of declarations strictly below the local floor)
cannot be run until the first extract exists. **If this is wrong, §2.1 through §2.7 of `_SYNTH-D`
are void and the fallback is an unmodelled bias direction.**

**2.2 The 43CA/50C/56(2)(x) tolerance ladder (~5% FA2018 → ~10% FA2020 → ~20% builder-primary,
₹2cr cap, 12 Nov 2020–30 Jun 2021).** `[RECALL]`, and `_SYNTH-B` §3 flags the corroboration as
**two dossiers from the same model with search unavailable — correlated recall, not
corroboration.** `_AUDIT-3` C-10 calls it the best-reasoned item in its scope precisely because it
identifies a statutory parameter as **the free parameter of the econometric design**. The excluded
bunching window, the plateau-width quasi-event study and the rung-3 triple-difference are all
functions of these three numbers and four dates. Wrong band ⇒ contaminated counterfactual ⇒ S2 is
noise ⇒ the reliability weight on S1 is noise. **This is the single highest-value verification on
the page and it is a one-hour job against the Finance Acts.**

**2.3 Honoré (1992) with a genuinely time-varying censoring point.** `_SYNTH-D` §2.3 says the
canonical exposition, to recollection, normalises the threshold to a constant, and calls extension
to period-varying `c_it` "the single highest-value item on the verification queue." The ward
fixed-effects specification — the answer to the incidental-parameters problem, and the only listed
route to purged ward slopes — is either a citation away or a methods paper away, and nobody knows
which. That is a *schedule* risk of unbounded size sitting inside a phase gate.

**2.4 That RBI computes ward × FSA-band strata upstream.** `[DESK FILE]` from
`partC-data.md` §C.1, corroborated at `[1-SOURCE]` by A2 §64. Three things lean on it: the reframe
from "invention" to **"replication at finer grain"**, the top-ranked acquisition ask (RTI for
existing strata), and the free validation target (ward index aggregated at RBI's weights must
reproduce the published city index). **A `[DESK FILE]` tag is being read as evidence-grade, and it
is not** — `partC-data.md` was itself assembled in a search-only session. The pack invented
`[DESK FILE]` in `_SYNTH-C` and placed it above every snippet claim; that is defensible for
provenance of *desk decisions* and indefensible for *facts about RBI's internal method*. Do not let
this tag do the work `[DESK PRINT]` does. The same caution applies to the carpet bands
(≤60/60–110/>110 sqm), the fixed 2010–11 weight mix and the 8–13 week lag range — all
single-sourced, all load-bearing on the validation design.

**2.5 The two irreconcilable India yield families.** Family-1 (GPG, asking-over-asking) at ~5.16%
national vs Family-2 (portal/broker micro-market) at 2.0–4.0% in Mumbai, every cell
`[1-SOURCE]`. CN-D2 makes **rental yield the placement instrument** — the thing that told the desk
tier-1 China was a third of the way into a crash when price alone was ambiguous. So the
most decision-relevant question in the project ("are Indian metros near a historical peak yield of
3.29% or above a historical trough of 4.94%?") is answered by unverified portal arithmetic, and the
two answers point in opposite directions. No amount of modelling downstream fixes this.

**2.6 The cost wedge (~21.5% over five years).** Sourced to `handoff §1`, which itself says a
prior session computed it on **indicative** rates and that it must be redone with registry-sourced
rates. Print 15 is the project's stated thesis ("the cost drag is the whole game"), every published
distribution must be shown net of it, and the break-even and opportunity-cost benchmarks (#4, #5 of
the five-benchmark ladder) are functions of it. An unverified constant is currently setting the bar
every model must clear.

**2.7 Single-sourced anchors the feature design is built on.** Nagpal-Gandhi's Mumbai FAR
+17%/+58%/**−24% on prices** (one unrefereed manuscript, re-tagged from 2-SOURCE because three URLs
were one paper) is the *only* causally identified India supply magnitude and the anchor for the
whole supply-elasticity layer. Bhupal Singh's LTV elasticities (0.40–0.59 small-ticket vs
1.10–1.14 large-ticket, same mirror problem) are the *only* India credit numbers and they are what
makes ticket-size segmentation a design decision rather than a whim. Both are leads.

**2.8 Build-or-no-build parameters that are simply unknown.** ULPIN/Bhu-Aadhaar coverage (the
parcel key SPAR and repeat-sales both need — "coverage is unknown; no figure asserted"); the
Maharashtra free e-search year band (`_AUDIT-3` D-12 deleted the remembered range as an unverified
parameter a build decision was resting on); whether **any** leave-and-license rent aggregate exists
(the only India route to a transaction-based yield, and the highest-value state-specific row);
whether RERA **QPR history** is retained or only the latest report shown (the delay-trajectory
feature exists or does not exist on this answer); and SHRUG's licence and India coverage (called the
single highest-value item in `D4` if it verifies, and the crosswalk carries a <70% kill criterion).
Five unknowns, each of which flips a deliverable on or off.

**2.9 The transfer assumption, which is load-bearing and cannot be verified at all.** IN-D1,
CN-D1..D5, RE1/RE2 are genuine first-party prints and the best evidence in the pack. They are also
**18 advanced economies, national indices, no India, no city level, and no market at India's income
or urbanisation stage.** `handoff §9` states plainly that the 10-year layer must be *borrowed* from
them. So the 10-year output is not an India forecast with wide intervals; it is a foreign base rate
with an India label, and the pack's own CN finding (city dispersion exceeds national dispersion —
Wenzhou −63%, Hainan ≈−87%) says that base rate is a **floor** on locality extremes, not a cap.
This is the pack's most honest statement and the project's least honest deliverable.

---

## 3. WHAT A HOSTILE EXPERT REVIEWER WOULD SAY

**The RBI research economist.** *"Your states are not identified, so your conditional distributions
are not conditional on anything you observed."* India has ~61 quarters of a ten-city registered-price
index with a documented rebase and coverage change in October 2025, and **zero completed domestic
crash episodes** in the sample. A state-conditional distribution needs repeated realisations of each
state; you have at most one and a half national upcycles and no downcycle, so every p10 and every
"share of comparable states that fell 20%+" is imported from an 18-country advanced-economy panel
that excludes India by construction. Secondarily: you propose to reconstruct ward strata from
registration data supplied to us by state departments whose attribute schemas are neither consistent
across Sub-Registrar Offices nor stable over time, and then to validate by reproducing our published
city index — which, if you use our fixed 2010–11 weights, you will reproduce by construction, and if
you do not, will differ for reasons that say nothing about your index.

**The Mumbai developer's CFO.** *"You are measuring the gross number on the deed, and the gross
number is the one thing we hold constant in a downturn."* Primary sales clear at headline price
minus an undisclosed incentive stack — subvention and cash-flow-linked payment plans, stamp duty
"paid by builder", floor-rise and PLC waivers, free parking and club membership, furnishing
credits. In a soft market we defend the printed rate and widen the stack, because the printed rate
is what our own valuations, our lenders' collateral and the next buyer's anchoring all depend on.
So your index will show flat prices while realisations fall 15–20%, and your crash detector will
read stability. This is a **second wedge moving opposite in phase** to the cash under-reporting
wedge you have modelled, and your pack does not contain it. Also: my forward book — quarterly
pre-sales bookings value, volume and realisation per sqft — is published, audited and leads your
registration series by two to four quarters, and you did not use it. And the two most respected
houses in this city disagree by 17% on unsold inventory because nobody agrees what "unsold" means;
you have that number in your own pack and you still propose to wire an inventory indicator.

**The US quant housing researcher.** *"Your benchmark and your outcome are the same artifact, and
your effective sample size is one."* You construct the index, then you test whether you can forecast
the index, then you benchmark against a random walk on the index. Appraisal- and repeat-sales-style
indices are mechanically smoothed (Geltner), which manufactures precisely the autocorrelation your
stage-1 model will harvest — your own protocol step 2 says this and then step 1 makes the smoothed
series the target anyway. With 150–350 localities, ~60 quarterly observations and spatial clustering
at city level across 4–6 cities, your independent sample is on the order of one cycle in one
country; Clark-West with the HLN correction and a deflated Sharpe cannot rescue an effective N of
one, and a PIT histogram on 60 quarters has no power to detect exactly the tail miscalibration you
are publishing. Two more: your method menu omits the state-space and hierarchical-trend index
family that was built for thin cells, and you are forecasting a price index while your client
consumes a *net, after-cost, illiquid, indivisible, single-asset return* — with no time-on-market,
no exit-liquidity and no forced-sale channel, the distribution you publish is not the distribution
anyone faces.

---

## 4. HOW THIS MOST LIKELY FAILS, RANKED

**FM1 — Acquisition never reaches locality grain, and the engine degrades into something RESIDEX
already is. (Highest probability.)** The pack establishes every precondition for this: no state
exposes bulk microdata (Tier 3 "does not exist for microdata in any major state"), the free rungs
are CAPTCHA-gated per-record lookups, there is no composing parcel key (survey/khasra/CTS/gat do
not compose and ULPIN coverage is unknown), and the crosswalk carries its own <70% kill criterion.
The most likely end state is not a wrong model, it is **no dependent variable** — followed by the
temptation to proceed on asking prices, which `handoff §10` explicitly forbids and which the
15-month-stale, vintage-less portal data would silently reward.
*Early probe (week 1–2, before any modelling):* a **single-SRO throughput test** — attempt 500
Index-II retrievals in one Mumbai SRO and measure records/hour, cost per record, CAPTCHA failure
rate, **field completeness (is area basis present? property type? built-up vs carpet?)**, and
whether the same parcel is retrievable twice under the same key. In parallel, file the RTI for
RBI's existing ward strata on day one (it has a statutory clock; nothing else here does). Decide
at two weeks, not at Phase 2.

**FM2 — The dependent variable gets built and is a compliance index wearing a price index's label.
(Second.)** Three independent routes to the same end: (i) the censoring model is structurally wrong
(§2.1) so the likelihood is misspecified; (ii) the censoring share exceeds 50% in the wards that
matter, at which point CLAD and censored quantile regression identify **only an upper tail**, not
the "typical price" the engine wants, and the pack says so explicitly; (iii) the counter-cyclical
incentive stack (§3, the CFO) holds the recorded price flat through a real decline. In all three
cases the series is smoothest and best-fitting exactly where the data is worst — `_SYNTH-D` §5's
own warning — and any model selected on held-out fit will prefer the most corrupted wards.
*Early probe (first 10k linked records, before an estimator is chosen):* (a) **share of declared
consideration strictly below the local circle rate** — if non-zero, plain Tobit is dead and the
design changes that day; (b) **censoring share per ward-quarter** — if >50% in the target
localities, the median is unidentified and the deliverable must be re-specified as an upper-tail
object; (c) the **round-number heaping placebo** — bunching intensity in wards whose rate is *not*
near a round number, which is the one placebo the pack admits nobody has designed; (d) regress
recorded price on a developer-disclosure realisation series for the same city-quarter, and read the
residual as the incentive-stack wedge.

**FM3 — Something survives, it is the artifact, and it goes out under the desk's name to clients.
(Third by probability, first by cost.)** The ingredients are all present and the desk has hit this
exact pattern five times (SC-D4, TECH-D3, MOM-D1, VAL-D2/D3, EQ-D1) plus once more in the handoff's
own registration of locality entry. Localities enter the panel *because* they appreciated (Ulwe,
Kokapet); the index is smoothed; 150–350 localities at α=0.05 yield ~15 false positives under a
global null before any signal exists; and the horizon that will be published (3y, 5y, 10y) cannot
be falsified in time to embarrass anyone. A model that beats five benchmarks on this panel and
carries a "research authority" label to wealth clients is the most expensive outcome available.
*Early probe, and it should run before the real panel:* build a **synthetic null panel** — locality
entry driven by realised appreciation, no true predictive signal — and run the entire pipeline on it
end to end. **If the pipeline does not print null, nothing it prints later counts.** Then, on any
real survivor: reverse-time and shuffled-ward placebos, the Goyal-Welch **cumulative SSE-difference
plot** (reject any gain carried by one boom window), and the expected-false-discovery count printed
beside every "N localities beat the benchmark" headline. Declare the one-way rule per design in
writing first: a bias that flatters growth localities makes a print *against* them admissible and a
print *for* them non-evidence-grade.

*Not ranked, but named because nobody in the pack owns it:* the **publication and advisory
perimeter**. A locality-level forward distribution delivered to wealth clients is a different
regulatory object from an equity research note, and the pack contains no sweep of what may be
published, by whom, with what disclaimer, under SEBI's adviser perimeter or RERA's agent
provisions. The project can be complete and correct and still be unpublishable. That is a cheap
question to answer early and an expensive one to answer at GATE 3.

---

## 5. WHAT SHOULD BE CUT

Criterion: does the item change a build decision, or does it demonstrate that a territory was
visited? Everything below is the second.

1. **`_SYNTH-A` §3 (nowcasting / alternative data) — cut to two paragraphs.** It is 100% `[RECALL]`
   by its own disclosure (zero searches ran), and its own headline recommendation was refuted the
   same day by the desk's probe. **Keep** the random-split-versus-time-split mechanism (it stands on
   first principles and is the honest core) and the Zillow Offers *narrative* with **no number in
   it**. **Cut** the Zestimate MAPE ladder, the Zillow Prize purse, the Flu Trends specifics, the
   nightlights ~0.3 elasticity, and the GHSL epoch list (properly covered in `_SYNTH-D` §4). A
   recalled MAPE ladder is exactly the kind of figure a later agent lifts as a target.
2. **`_SYNTH-B` §1's ~25-country regime table — cut to four rows.** The design uses Netherlands
   (SPAR), Taiwan (statutory disclosure), Poland (BaRN paired collection) and India. Russia,
   Nigeria, Vietnam, Kenya, Colombia, Chile, Mexico, Philippines, Brazil and the Nordics contribute
   nothing but breadth, several carry their own `[VERIFY]` flags, and the real content of the
   section — the **four-way construction taxonomy** (asking / appraisal / registered deed /
   developer survey) — survives the cut intact. Ironically the one country worth adding (Dubai,
   §1.7) is not in the table at all, which is what a coverage list looks like.
3. **`_SYNTH-B` §3's floor-system tour — keep two, cut six.** Pakistan's three-tier stack (the
   actual structural analogue to India's sub-district heterogeneity) and Italy's *prezzo-valore*
   (the only inverted design, and therefore the only one suggesting a policy lever) earn their
   place. Greece, Portugal, Turkey, Egypt, Spain and Mexico are `[RECALL]` percentages and statute
   numbers that never enter an estimator.
4. **`_SYNTH-C` §4's infrastructure table, beyond the first-pass cities.** Bharatmala, Delhi-Meerut
   RRTS, Mumbai-Ahmedabad HSR, Bengaluru PRR and Chennai Metro Ph.2 are either right-censored or
   outside the 4–6 chosen cities. As written it is a national capex calendar, not a feature set —
   and a table that had to be corrected on five of its own dates (R9–R12) is a liability at this
   length. Keep corridor-level, two-column announce/commission rows for the chosen cities only.
5. **`_SYNTH-C` §5's "thin or unverifiable" paragraph — delete outright.** Eight institutions and
   ten names with no titles, no findings, no verified attributions, and one naming error inside it
   (Tiwari/IIMB). It is a bibliography-shaped hole labelled as literature, and its only likely
   effect is that some future agent cites one of these as if it had been read. Replace with one
   line: *"No refereed Indian infrastructure-premium hedonic was recoverable; commission a dedicated
   search or estimate from scratch."*
6. **`_SYNTH-C` §6's net-yield waterfall — cut the two-decimal precision, keep the range.** The
   largest single deduction (repairs, 0.75, 19% of gross rent) has **no source at all**, property
   tax rests on one Pune worked example against a defensible span four times as wide, and the output
   is quoted to two decimals (1.33 / 1.56). This is the number that will be lifted straight into a
   client brief. State it as "roughly 1–2% of value after tax, on three unmeasured inputs" and name
   the three, or defer it until one real landlord P&L exists.
7. **`_SYNTH-D` §4's 25-row geospatial table — cut to seven rows plus the vintage column.** Keep
   GHSL, VIIRS, SHRUG, OSM, Dynamic World, the pincode-polygon negative and the Census ward
   delimitation warning — the vintage/PIT column is genuinely the section's contribution. Cut SRTM,
   ASTER and CopDEM (their own row concedes they cannot detect construction), WorldCover (its own
   row concedes a 2022+ release would change the recommendation), Bhuvan (access-blocked), CPCB and
   OpenAQ (no ward grain), and the Earth Engine licensing discussion (that is counsel, not a data
   source).
8. **`_SYNTH-D` §1.1's eleven-method menu — compress to three live candidates plus the missing
   one.** Five rows are ruled out in their own verdict column ("forbidden as sole output", "never at
   ward level alone", "city cross-check only", "later, W registered", "only with a registered
   bandwidth"). Keep the stratified mix-adjusted median (the floor), SPAR (the primary candidate)
   and pooled hedonic + ward FE (the pooling layer), and add the state-space/hierarchical-trend
   family from §1.5. Cataloguing methods nobody will run is the clearest coverage tell in the pack.
9. **The four-fold restatement of the same corrections — collapse to one canonical statement
   each.** The loading factor L appears in six places; the RBI rebase splice rule in five; the
   36-of-37 probe in four; the CN-D1 crash base rates in five; IN-D1's "hot markets stay hot" in
   four. Four syntheses each carrying the other three's conclusions **manufactures the appearance of
   corroboration** — the precise failure `_AUDIT-2` names (correlated recall presented as
   agreement) and `_AUDIT-2`'s severity note calls pre-laundered. One statement, referenced.
10. **The three audits — compress to a single ranked verification queue.** ~130KB of adversarial
    prose currently supports **zero** verified citations. What the next session needs is not the
    narrative; it is ~25 must-verify items ordered by how much design each one carries (start:
    §2.2 the tolerance ladder, §2.1 the censoring mechanism, §2.3 Honoré, §2.4 the RBI strata,
    §2.5 the yield families, §2.6 the cost wedge). Everything else in the audits is preserved
    history, not working material.
11. **The forty numbered "what this section changes about the plan" recommendations across four
    files — collapse into one ordered list gated to GATE 0 / 1 / 2.** As delivered they have no
    priority, no owner and heavy overlap, and they cannot all be first. Ten of them are also
    blocked on items in §2.8 that nobody knows the answer to yet.

*Written 2026-09-11. Zero run cells; nothing here is a print. WebFetch not called (egress-blocked);
no searches run; no git commands run. Every non-pack citation above is `[CRITIC-RECALL]` — model
memory, unretrieved, and a search target rather than a fact.*
