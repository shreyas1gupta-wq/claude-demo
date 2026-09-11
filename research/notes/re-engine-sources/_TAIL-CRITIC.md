## §7 — WHAT WAS NEVER SWEPT, AND THE THREE WAYS THIS FAILS

A final agent read the four syntheses adversarially and asked what a hostile expert would say. Its
output is the most useful part of this pack, because everything above is what 22 agents *did* look
at and this is what none of them did.

### 7.1 The modalities nobody swept — and four of them are better than what was swept

Ranked by what they would change. The first three are **uncensored price observations**, which is
remarkable given that §§4.1-4.2 of the handoff prompt spend their length engineering around
censoring.

| Gap | Why it matters | Grade |
|---|---|---|
| **Listed-developer quarterly filings** — DLF, Macrotech, Godrej Properties, Oberoi, Prestige, Brigade, Sobha publish audited pre-sales value and volume, **average realisation per sqft by city**, launches, collections, inventory and net debt, every quarter | A dated, audited, per-sqft price series with **no evasion incentive and no notified floor** — and it is already public, already quarterly, and already point-in-time. The single largest omission in the pack | **Highest value** |
| **Public land auctions** — CIDCO, MHADA, HUDA/HSVP, NOIDA, DDA, state industrial corporations | Published, dated, plot-identified, competitively bid, **no under-reporting incentive and no floor to bunch at**. The clean comparison series the censoring model needs to calibrate against | **Highest value** |
| **Distressed sales** — SARFAESI bank e-auction notices, IBAPI reserve prices | Address-level, dated, and the one place the *downside* of the distribution is observable in a market whose registered prices are floored | High |
| **Demography and household formation** — headship rates, household-formation projections, internal migration, age structure | **The only variable class with any claim to ten-year forecastability, and it is entirely absent.** Credit, momentum and evasion are all short-horizon mechanisms, so the pack has nothing in the place where its promised horizon actually lives | **Highest value for the 10y layer** |
| **Physical-climate risk** — flood, heat, groundwater, subsidence, air quality | Locality-discriminating, publicly mapped, and unlike momentum genuinely forward-looking at ten years. Chennai 2015, Mumbai flooding, Bengaluru 2022 lake-bed inundation, NCR air quality. **The desk already owns a vaulted climate dataset** | High |
| **The developer incentive stack as a second wedge** — subvention and CLP plans, "stamp duty paid", floor-rise and PLC waivers, parking, club membership, furnishing credits | The pack models one wedge (cash under-reporting, widening late-cycle) and misses the second, which **widens in downturns while the headline rate is defended**. Two wedges moving in opposite cycle phases is a different measurement problem entirely | High |
| **Dubai Land Department** — free transaction-level microdata with an open API | An emerging market with two documented crashes, heavy Indian participation, and the most India-relevant **open-microdata** regime in the world. §2 lists ~25 countries and omits it, which is what a coverage list looks like versus an evidence list | Medium-high |
| **Litigation as an observable** — eCourts, NCLT/IBC real-estate admissions, RERA complaint orders | The pack carries the finding that *litigation, not regulation*, throttled India's supply response, then proposes no way to measure it. Free, dated, text-searchable | Medium |
| **District-level credit** — RBI Basic Statistical Return, district × sector outstanding | The finest free credit grain in India. The credit module as specified is national Sectoral Deployment only. Also missing: the **2019 external-benchmark (EBLR) mandate** as a monetary-transmission break, absent from an event calendar carrying eleven tax and RERA dates | Medium |
| **NRI / FX demand and gold substitution** | The desk owns a full currency battery (PPP +0.94, weak-INR year behaviour, a 71-episode crash anatomy) and gold to 1833, plus CI-D2 ranking gold above housing in high-and-rising inflation. None of it is connected to property demand anywhere. **A weak-INR year is a testable conditioner on NRI-heavy localities** — and SNAPSHOT-1 says India is in one now | Medium |
| **TDR markets and fiscal capitalisation** | Mumbai TDR is a traded instrument whose price is a direct read on FSI scarcity. Also absent: the Oates-lineage literature on tax and amenity capitalisation, land value capture, and society-redevelopment optionality (cessed buildings) — a genuinely India-specific source of value | Medium |
| **Thin-market index methods the menu omits** — hierarchical-trend and state-space repeat-sales (Francke; Schulz-Werwatz; Nagaraja-Brown-Zhao) | §4 lists eleven methods, rules out five in its own verdict column, and omits **the one family built precisely for "tens of transactions per cell"** | Medium |
| **Exit liquidity** | CN-D4 established that the exit plan matters more than the entry level, and the architecture promises a liquidity output — with no time-on-market or months-to-sell measurement specified for India | Medium |
| **The advisory and publication perimeter** — SEBI adviser perimeter, RERA agent provisions, disclaimer form | A locality-level forward distribution delivered to wealth clients is a different regulatory object from an equity research note. **The project can be complete, correct and unpublishable.** Cheap to answer now, expensive at the last gate | Do it first |

### 7.2 The three objections that would be made by people who know

**An RBI research economist:** *"Your states are not identified, so your conditional distributions
are not conditional on anything you observed."* India has roughly 61 quarters of a ten-city
registered-price index with a documented rebase and coverage change inside it, and **zero completed
domestic crash episodes** — at most one and a half national upcycles and no downcycle. Every p10 and
every "share of comparable states that subsequently fell 20%+" is therefore borrowed from an 18-country
advanced-economy panel and relabelled as an Indian conditional.

**A Mumbai developer's CFO:** *"You are measuring the gross number on the deed, and the gross number
is the one thing we hold constant in a downturn."* Primary sales clear at headline price minus an
undisclosed incentive stack. In a soft market the printed rate is defended and the stack widens. A
deed-based index will therefore **understate the drawdown precisely when the drawdown is what you
need** — the inverse of the error everyone worries about.

**A US quant housing researcher:** *"Your benchmark and your outcome are the same artifact, and your
effective sample size is one."* You construct the index, forecast the index, and benchmark against a
random walk on the index. Repeat-sales and appraisal-style indices are mechanically smoothed
(Geltner), manufacturing exactly the autocorrelation a momentum stage will harvest. Hundreds of
localities in one country in one era is **one** macro draw, not hundreds of independent observations.

### 7.3 The three ways this fails, ranked, each with the probe that detects it early

**FM1 — Acquisition never reaches locality grain, and the engine degrades into what RBI HPI and
RESIDEX already are.** Highest probability, and the pack establishes every precondition: no state
exposes bulk microdata, the free rungs are captcha-gated per-record lookups, and no parcel key
composes across systems. *Probe: attempt 200 real e-search retrievals for one Mumbai ward on the
desktop machine and measure the per-record cost in seconds and in blocks.*

**FM2 — The dependent variable gets built and is a compliance index wearing a price index's label.**
Three independent routes to it: the censoring model is structurally wrong (§6.2 #1), the tolerance
band changes declaration behaviour on dates unrelated to value, and the incentive stack moves
counter-cyclically. *Probe: the below-floor share (queue row 1), plus a placebo — does the index
jump at the 43CA tolerance-change dates?*

**FM3 — Something survives, it is the artifact, and it ships under the desk's name to clients.**
Third by probability, **first by cost.** The desk has hit this exact pattern five times already
(SC-D4, TECH-D3, MOM-D1, VAL-D2/D3, EQ-D1), and here the ingredients are all present: localities
enter the panel *because* they appreciated (Ulwe, Kokapet), the index is smoothed, and the reward
for a confident answer is high. *Probe: declare the one-way rule at registration — a bias that
flatters the finding makes a print for it non-evidence-grade — and run the entry-date placebo before
any result is written up.*

### 7.4 The critic's methodological complaint, which is upheld

**Four syntheses each carrying the other three's conclusions manufactures the appearance of
corroboration.** The loading factor appears in six places, the RBI rebase splice rule in five, the
reachability probe in four, the crash base rates in five. Repetition inside one pack written by one
model family is **not** independent confirmation, and this desk has a name for that failure. Read
§§1-4 as one document with four authors, not four documents that agree.

