# The Context Quartet — Closing Band 4 (Atlas 4.7–4.10)

*Monograph #35 in the cycle-research series · v1.0 · 2026-09-02 · Author: Claude (research agent)
for Ionic quant desk (principal: gaurav@ionic.in) · governed by `research/CONTRACT.md`.*

**Verdict up front.** Four Band-4 rows — monsoon season (**4.7**), festive/wedding demand season
(**4.8**), gold demand seasonality (**4.9**), and SIP debit clustering / turn-of-month (**4.10**) —
share a structure this chapter exists to name: each is a **real, datable, mechanism-backed seasonal
in the underlying real economy or the underlying cash flow**, and each is **zero-budget** in the
design precisely because the mechanism, followed all the way through, never produces a tradable
price-timing claim. `docs/CYCLE_ATLAS.md` already carries the individual verdicts — 4.7 "**CONTEXT**
sector-level reduce-only," 4.8 "**CONTEXT** only," 4.9 "**CONTEXT**; local-premium hygiene for the
gold sleeve," 4.10 "**CONTEXT/EXECUTION** at most... listed to keep it from returning as 'discovered
alpha'" — and this desk's own pre-registered print on the sharpest of the four is already run and
already in the ledger: **GS1** (gold festival-seasonality demonstration; vaulted gold monthly, float
era 1972-02..2026-07, n=654 monthly log returns, ~54–55 observations per calendar month) returned
**Kruskal-Wallis H=10.87, p=0.454 across the twelve months** — no world-price calendar structure —
with the descriptive ranks teaching the sharper lesson than the omnibus: **April, Akshaya Tritiya's
own month, is the WORST month of twelve** (median −0.60%/mo), **May is 11th**, **November
(Dhanteras/wedding season) is 10th**, and the folk "September strength" claim sits at **rank 6 of
12 — dead middle**, while January's rank-1 (+1.50) "stays exactly where the register's discipline
puts every un-mechanismed rank-1: logged, never interpreted" (`context-RESULTS.md`, verbatim; these
are the only desk numbers this chapter cites and every one of them is reproduced exactly as printed
there — no number in this chapter is recomputed). The four verdicts do not move. What this chapter
adds is the argument for *why* they should not move, formalized with the math, the cross-country
contrast that proves the math has real content rather than being a rationalization, and the
psychology of why a desk needs these verdicts **written down** rather than re-derived from memory
each October.

**Cross-reference discipline, stated once and honored throughout.** This chapter does not restate
material three sibling monographs already own at depth. The ENSO physics, the teleconnection
mechanism, and the **H55** sector-conditioner design (rural-basket reduce-only, gated on *realized*
IMD rainfall and *realized* food CPI, never on a forecast headline) belong to
`research/cycles/enso-deep/partA-physics-teleconnection.md` and its India-case sibling
`partB-india-cases.md` (assembled at `docs/cycles/27-enso.md`); 4.7's monsoon economics is read
**through** that entry, not duplicated beside it, exactly as the atlas instructs ("ENSO-modulated —
see 2.14"). The event-study econometrics of *fixed-date* calendar effects (Budget-day volatility,
the fiscal-year-end small-cap hypothesis, the Slutzky trap, dividend-drop pricing) belong to
monograph #33, `research/cycles/calendar/partABC-calendar.md`; that chapter's own Part C confirms,
on inspection, that it never touches turn-of-month liquidity effects, which is exactly the gap this
chapter's §A.3 fills. The gold cost-of-carry mechanics, the price-taker identity, and the July-2024
duty cut belong to dossier **D06** (`research/dossiers/06-gold-debt-policy.md`) and the gold
monograph's own psychology chapter (`research/cycles/gold-deep/partAB-theory-evidence.md` §G.3,
"familiarity, not fear" on India's household gold-as-default anchoring); this chapter cites both
rather than re-deriving the wedge. The register's verdict taxonomy — evidence-reject, fold, context,
data-reject — was itself "completed" (its own word) in the retail-participation chapter
(`research/cycles/retail-deep/partDH-verdict-routing.md` Part D); §A.4 below extends it by exactly
the two distinctions 4.10 forces into existence. Every figure below not sourced to this desk's own
ledger is search-verified as of September 2026 or explicitly tagged `[VERIFY: ...]`.

---

## Part A — Theory, formalized

### A.1 Monsoon economics, formally: why the index is silent and the sector is not

IMD's operative statistic is a ratio, not a raw rainfall number. Let `R_t` be all-India June–
September rainfall in year `t` and `LPA` the fixed 1971–2020 baseline (**868.6 mm**, the "New
All-India rainfall normal," periodically re-based once a decade). IMD reports and classifies
`ρ_t = 100·R_t/LPA`: **normal/near-normal** for `ρ_t ∈ [96,104]`, **below normal** for `[90,96)`,
**deficient** for `ρ_t < 90`, **above normal** for `(104,110]`, **excess** for `ρ_t > 110`. This
single ratio is the entry point for two structurally different transmission channels, and the atlas
is right to keep them separate rather than folding them into one "monsoon effect."

**Channel 1 — the consumption-demand channel.** A stylized decomposition: `ΔRuralIncome_t ≈
β₁·(ρ_t − 100) + β₁'·ΔMSP_t + ε_t`, where kharif sowing acreage and yield respond to realized
rainfall with a roughly one-season lag, and Minimum Support Price revisions are a separate,
policy-controlled lever that can amplify or dampen the pass-through (the ENSO monograph's own
2014–16 case, cross-cited in §B.4 below, is precisely a demonstration of `ΔMSP_t` and targeted
import policy actively *offsetting* a realized `(ρ_t − 100)` deficit). The channel's downstream
consumers are named, mechanism-backed sectors: two-wheelers and tractors (rural income is a large
share of both categories' addressable demand), agri-inputs (fertilizer, seed, agrochemicals — demand
is close to mechanically tied to sown acreage), and the rural mix of FMCG revenue.

**Channel 2 — the food-CPI → RBI reaction channel.** A rainfall deficit that actually damages the
kharif crop feeds directly into food-basket inflation, and food carries a large weight in India's
CPI basket; a central bank running flexible inflation targeting must then weigh a rainfall-driven,
supply-side price shock against its mandate. This is **exactly** H55's own object, and this chapter
does not re-derive H55's transmission chain, its realized-only gating discipline, or its own
measured base rates (the ENSO monograph's EN1–EN3 trials, and its Part B event record) — it cites
them. What this chapter adds is the *aggregation* argument for why the **index-level** equity effect
stays "honestly unquantified" (the atlas's own phrase) even though both channels are individually
real and individually measurable.

**The aggregation argument, formally.** Both channels operate on a rural-and-agricultural base that
is now a *minority* of the denominator any index-level equity effect must clear. Agriculture,
forestry and fishing's share of India's gross value added has fallen from roughly 30%+ in the early
1990s to **roughly 18% at current prices in FY2024–25** (MOSPI provisional estimates; roughly 14% at
constant 2011-12 prices — the two bases diverge because agricultural prices have risen faster than
the deflator, a `[VERIFY: precise multi-decade series]` worth stating rather than assuming). Write
a rural-income shock's pass-through to *aggregate* corporate earnings as (sector weight) × (sector
sensitivity); even a fully realized, high `β₁` sensitivity inside agriculture-linked sectors is
diluted, at the **index** level, by a much larger non-agricultural earnings base that a monsoon
shock does not touch directly. The same `β₁`, evaluated against a **sector-specific** denominator —
a tractor maker's own revenue, an FMCG name's rural-mix revenue line, a fertilizer company's sales
volume — keeps its full size, because the denominator there *is* the exposed base, not the whole
economy. This is not a hedge-word; it is the mathematical content of the atlas's own sentence
("index-level effect honestly unquantified... sector-level has a mechanism"), and §B.3's 2009 case
below is the demonstration: agri-GDP growth of **~0.2%** against a headline GDP print of **7.4%** in
the worst drought since 1972 (ENSO monograph, cross-cited) is precisely the shrunken-denominator
story showing up in a single year's national accounts, with an equity index that never had to answer
to the smaller number at all.

### A.2 Demand seasonality vs. price seasonality, formally: the Samuelson–Working line

The single formal idea that organizes 4.8 and 4.9 together is that **a perfectly anticipated
seasonal shift in demand, for a storable and freely arbitraged asset, need leave no seasonal
residual in the realized spot-return series** — even though the underlying demand seasonality is
completely real. **Samuelson, Paul A. (1965), "Proof That Properly Anticipated Prices Fluctuate
Randomly,"** *Industrial Management Review* 6(2): 41–49 **[Verified]**, is the general theorem:
if a price change is properly anticipated, competitive risk-bearing capital has already traded
against it, and what remains in the realized-return series is only the *unanticipated* residual —
by construction, a calendar-anchored demand shift (a wedding season, a festival date fixed on a
lunar-solar calendar) is about as anticipated as an economic fact can be. **Working, Holbrook
(1949), "The Theory of Price of Storage,"** *American Economic Review* 39(6): 1254–1262
**[Verified]**, supplies the mechanism that does the arbitraging: a competitive inventory holder,
facing a known future demand pulse, adjusts holdings *ahead of time* so that the expected return to
carrying stock into the high-demand period equals the cost of carry (storage, insurance, financing)
— under free entry into storage and no capacity constraint, this pins the *forward curve's* seasonal
shape to a financing-cost term, not a demand-timing term, and — this is Samuelson's own point
applied to Working's setting — it removes the seasonal from the *spot-return* process entirely,
leaving only a small, roughly constant carry return that is a function of financing cost, not of
which month it is.

Formally: under the null that a storable asset's anticipated demand seasonal is fully arbitraged by
unconstrained competitive storage, `E[r_t | month = m] = c_m ≈ c` — a carry term, invariant to `m`
through any *demand* channel — where `r_t` is the log spot return. **GS1 is precisely a test of this
null on the world gold price**, and the print (`H=10.87, p=0.454, n=654`) fails to reject it. That
failure is not merely consistent with the folk claim being wrong — it is consistent with theory,
given three facts D06 already establishes and this chapter inherits: (i) gold trades on a genuinely
global, near-24-hour arbitraged market (London, Zurich, COMEX, Shanghai, MCX, all convertible within
minutes of one another); (ii) gold's physical deterioration is effectively zero and its storage cost
relative to value is tiny, so the "unconstrained storage capacity" assumption behind the Working
result is close to literally true — any bank vault or ETF trust can hold arbitrarily more gold at
near-constant marginal cost, which is not true of the commodities in §B.1; and (iii) India consumes
roughly a quarter of world gold demand but hosts essentially none of the price-formation venue (D06)
— so even a fully real, fully seasonal *local* demand pulse has no channel by which it could move a
*globally* clearing price on a predictable calendar date, because if it somehow did, shorting gold
into Diwali and covering after Dhanteras would be a scalable, near-riskless arbitrage available to
every trading desk on earth, and the arbitrage's own existence is what would compete the pattern away
before any backtest, this desk's included, could ever observe it. The theorem is therefore
self-enforcing in exactly the way market efficiency arguments always are: its empirical signature is
its own absence.

**The wedge is where the seasonal is allowed to live.** Decompose the domestic price identity as
`P_domestic = P_world · FX · (1 + duty + GST) · (1 + premium)`, where `premium` is the local
demand/supply wedge over landed cost. Global arbitrage pins the first three terms up to policy
discreteness (the July-2024 Union Budget cut total customs duty on gold from **15% to 6%** — "the
sharpest reduction on record... lowest since June 2013," per the World Gold Council — a level break
in the wedge, not a market move, exactly as D06 already flags); it does **not** pin `premium`,
because capital controls, import-licensing frictions, and physical-delivery logistics keep the local
dealer market from instantaneous arbitrage against the world price the way COMEX and LBMA arbitrage
against each other. Festival demand's entire economic content, if it has any price-side content at
all, must run through that one term — which is exactly why the atlas routes 4.9 to "local-premium
hygiene for the gold sleeve" and why `context-RESULTS.md`'s own honest read states the scope
boundary explicitly: "monthly world-price data cannot see the local premium cycle (the real 4.9
object) — that needs MCX-vs-landed premia, a runsheet series, registered... only if the gold sleeve
ever needs it." GS1 is the correct instrument to falsify a *world-price* festival claim; it was never
the instrument that could measure the *local-premium* object, and this chapter's Part C says plainly
what building that second instrument would require and why it is not being built now.

### A.3 The turn-of-month literature, formally, and its India mapping

**Ariel, Robert A. (1987), "A Monthly Effect in Stock Returns,"** *Journal of Financial Economics*
18(1): 161–174 **[Verified]**, is the founding empirical fact: US equal- and value-weighted
portfolio returns, 1963–1981, are positive and large across the first half of the calendar month
(the first nine trading days plus the last trading day of the prior month) and statistically
indistinguishable from zero across the second half. **Lakonishok, Josef & Smidt, Seymour (1988),
"Are Seasonal Anomalies Real? A Ninety-Year Perspective,"** *Review of Financial Studies* 1(4):
403–425 **[Verified]**, extends the finding's persistence across ninety years of the Dow and shows
it sitting alongside turn-of-year, turn-of-week, and pre-holiday effects — the same family of
calendar-clustered abnormal returns, tested jointly rather than cherry-picked one at a time (the
same joint-omnibus discipline this desk's own CW3 trial applied to 4.11, cited in monograph #33).
**Ogden, Joseph P. (1990), "Turn-of-Month Evaluations of Liquid Profits and Stock Returns: A Common
Explanation for the Monthly and January Effects,"** *Journal of Finance* 45(4): 1259–1272
**[Verified]**, supplies the mechanism that turns Ariel's fact into a testable causal claim rather
than a curiosity: modern payment systems **standardize** a large share of periodic cash flows —
wages, pension contributions, interest and dividend payments — onto specific calendar dates
(month-end credit, early-month settlement), so that new investable liquidity arrives lumped at the
turn of the month rather than spread uniformly across it; if any share of that liquidity is deployed
into equities with a short lag, expected returns should show a level shift concentrated exactly
where Ariel found one. **McConnell, John J. & Xu, Wei (2008), "Equity Returns at the Turn of the
Month,"** *Financial Analysts Journal* 64(2): 49–64 **[Verified]**, is the modern, international
confirmation at a scale that makes the mechanism hard to dismiss as a US-specific accounting
quirk: across 1926–2005 for the US, "investors received no reward for bearing market risk except
at turns of the month," and the effect appears in **31 of 35 countries examined** — while explicitly
*not* being explained by month-end trading volume or net mutual-fund flows, which the paper's own
tests rule out as the direct channel (a caveat worth carrying forward honestly rather than
overclaiming Ogden's mechanism as fully confirmed at the micro level).

**The India mapping is structurally the same standardization-of-payment-dates mechanism, transplanted
whole.** SIP mandates are executed through NACH auto-debit, and while an investor may nominate any
calendar date, AMC and registrar convention concentrates the *offered* and *default* dates on a small
early-month set — **1st, 5th, 7th, and 10th are the commonly used dates across AMCs**, with at least
one major AMC's own enrollment form defaulting an unspecified mandate to the **10th**
`[VERIFY: exhaustive AMC-by-AMC default-date survey — not independently confirmed this session]` —
and any date falling on a non-business day rolls to the next business day, the same calendar/
trading-day reconciliation problem the calendar-mechanics chapter's exclusion calendars already
solve for statutory drain dates and expiry days (`research/cycles/calendar-mechanics/
partDH-mechanics.md` §E; the same `numpy.busday`-class machinery applies here with no new code
required). This is Ogden's mechanism precisely: a large, periodic, calendar-standardized cash inflow
concentrated on early-month dates, which — if deployed into equities with a short lag — should
produce exactly the kind of turn-of-month pulse Ariel, Lakonishok-Smidt, and McConnell-Xu measured
in developed markets forty years earlier.

**The honest size argument.** Take the most recent verified monthly SIP print, **₹31,961 crore**
(July 2026, per AMFI data as reported; see §B.7 for the fuller series) against NSE's own reported
**FY2025 average daily cash-market turnover of ₹1.1 lakh crore**, up 38% year-on-year, with total
FY25 cash-market turnover of **₹281 lakh crore** (NSE, official release). At roughly 21 trading
sessions per month, ₹1.1 lakh crore/day implies **roughly ₹23 lakh crore of monthly cash-market
turnover** — so a smoothed, evenly-spread SIP flow is on the order of **~1.2–1.4% of monthly
turnover**. SIP debits are not evenly spread, however; concentrated into a realistic early-month
window of, say, the first seven to ten trading sessions rather than all twenty-one, the *implied*
incremental daily net-buy pressure inside that window is larger than the smoothed average by
roughly the compression ratio (on the order of two-to-three times), which puts the honest peak
magnitude at **low single digits of a single day's ADV even at its most concentrated** — real,
mechanical, non-zero, and nowhere near the scale needed to move a market this deep in any way that
survives transaction costs and market impact, a point §C below sharpens further by noting the actual
deployment lag between an investor's debit date and a fund manager's purchase date. This is the
size argument the atlas row gestures at ("₹20k+cr/month of SIP flow... a small, real, mechanical
demand pulse") made explicit with the two numbers that decide it, rather than asserted.

### A.4 The CONTEXT verdict, formalized: completing the register's taxonomy

The retail-participation chapter states the register's verdict taxonomy as **complete at four**:
**evidence-reject** (the claim is tested and its bar fails — war cycles, Kondratieff waves), **fold**
(the object is real but already seated under another name — the fixed 18-year property clock's
mechanism folded into L12), **context** (real, datable, but zero allocation authority by
construction), and **data-reject** (the claim may well be true, but its inputs violate the
free-source rule, with the forgone alpha stated rather than hidden). This quartet's fourth member,
4.10, exposes a distinction the existing four do not yet carry, and this chapter registers it
explicitly rather than smuggling it in as an unlabeled special case: a signal can **pass** a
statistical or evidentiary bar — §A.3's turn-of-month mechanism is real, measurable, and would very
plausibly clear a naive significance test on early-versus-late-month returns — and still be
**refused** a budgeted seat, not because the mechanism failed scrutiny (the fold/evidence-reject
distinction) and not because the data is unavailable (the data-reject distinction), but because the
desk's own honest size-versus-cost arithmetic (§A.3) says the object cannot pay for itself after
transaction costs, market impact, and the deployment-lag uncertainty §C names. Call this split
**pass-adopt** (the object clears its bar, the mechanism survives scrutiny, and a budgeted seat
follows — index-reconstitution flows for the special-sits sleeve, the momentum composite, the credit
cycle's regime seat) versus **pass-refuse** (the object would clear, or does clear, a bar, but the
desk declines the seat anyway on economic or scope grounds stated in writing). 4.10 is this
monograph's exhibit for **pass-refuse**: the mechanism is honest, the size is measured, and the
verdict is still no, with the reason on the record rather than left to be re-argued the next time
someone notices SIP flows are growing.

4.7, 4.8, and 4.9 are a different case entirely, and conflating them with 4.10's pass-refuse would
blur the taxonomy rather than complete it: none of the three was ever a **candidate** for a seat to
begin with, because the object each names — a rural-income flow, a wedding-season demand flow, a
local gold premium — is a fact about the real economy or a local market microstructure, not a claim
about a *tradable, timeable price move* in an instrument this desk can hold. **CONTEXT entries have
zero allocation authority by construction**, not because they were tried and found wanting on cost
grounds (pass-refuse) or on mechanism grounds (evidence-reject); they were never in that race. The
distinction matters operationally: a pass-refuse verdict is revisited if the cost structure changes
(cheaper execution, a capacity-unconstrained instrument); a CONTEXT verdict is revisited only if the
underlying object's *character* changes — if, for instance, 4.9's local-premium wedge itself became
freely, dailly, auditably observable (§C), it could in principle graduate into a *hygiene* input for
the gold sleeve, which is exactly the conditional the atlas and `context-RESULTS.md` already state
("registered as GS-D1 only if the gold sleeve ever needs it"). One further de-duplication point
belongs here explicitly, in the same spirit as the retail chapter's own sub-input rule: Atlas 3.6's
candidate **H57** (the retail-participation wave) also draws on AMFI SIP data, but at a different
object — H57 uses **new-SIP-registration counts** as a structural sentiment series (a *state*, not
a calendar fact), while 4.10 uses total **SIP rupee flow's within-month calendar timing** (a
mechanical *execution* fact). Same free source, two non-overlapping objects, no double count.

---

## Part G — Operator psychology

**Narrative seasonality runs on a fixed broadcast schedule the physical and financial calendars only
pretend to share.** Every June, financial media runs a "monsoon watch" segment tracking IMD's
forecast release with the same intensity a cricket broadcast tracks a toss; every October, a
"Dhanteras rally" story runs, invoking gold-buying auspiciousness as if it were a technical signal;
every month-end, a retail commentary piece notes that "₹20,000-plus crore of SIP money" is about to
hit the market as though that fact alone settled a directional question. These narratives are not
lies — the underlying calendar facts they invoke (a real forecast release date, a real festival, a
real AMFI print) are true — but a narrative running on a fixed annual or monthly broadcast schedule
is precisely the shape of thing the atlas's own epistemics course (`CYCLE_ATLAS.md` §0) warns against
mistaking for a tradable signal, and the warning bites hardest exactly where the underlying fact is
real, because a real fact wrapped in a compelling story is far harder to decline than an obviously
manufactured one.

**The analyst's temptation is to trade the weather instead of the state.** The ENSO monograph's own
psychology sections (`enso-deep/partA-physics-teleconnection.md`) already name the version of this
failure specific to El Niño itself — an availability-cascade around a *forecast* headline, when the
design's own H55 discipline gates on *realized* rainfall and *realized* CPI only. This quartet names
the adjacent, calendar-shaped version of the same failure: an analyst who has correctly internalized
"ENSO is a state, not a clock" can still slip into treating the mere fact that *it is June* — the
calendar date itself, independent of any realized rainfall reading — as though it carried forecasting
content the calendar cannot supply. "Trading the weather" here means reacting to the media cycle
that a season has *arrived* rather than to what the season has actually *delivered so far*; the same
error, one level removed, applies to trading "it is festival season" rather than what realized WGC
demand and realized local premia show, and to trading "it is turn-of-month" rather than the measured,
small pulse §A.3 actually derives. The desk's discipline — CONTEXT entries fire on realized data or
not at all — is the same knife the calendar monograph already applied to fixed-date effects and the
same knife the ENSO monograph applied to forecast-headline availability cascades; this chapter's
contribution is showing the knife cuts the *seasonal-narrative* version of the temptation with equal
force, because the narrative's vividness (a wedding, a festival, a payday) does not correlate at all
with whether the underlying object was ever a price-timing candidate.

**This is precisely why CONTEXT entries function as a desk's immune system.** A pre-written verdict
— logged, dated, with its reasoning attached — lets an operator decline a story in one line ("4.7 is
CONTEXT, sector reduce-only, gated on realized data; see H55") without re-deriving the entire
Samuelson–Working argument, or re-running GS1, every time a journalist, a client, or the operator's
own pattern-hungry cognition asks "is this a bad monsoon for markets?" or "should we buy ahead of
Dhanteras?" The alternative — re-litigating the question fresh each season — is exactly the setup
in which a plausible-sounding, narrative-driven exception eventually gets made, because a story this
familiar, repeated enough Octobers in a row, starts to feel like evidence in its own right even
though nothing about the underlying object has changed since the verdict was first written. Writing
the verdict down and dating it is what stops that erosion; the register's discipline is not merely
recording a conclusion, it is manufacturing the desk's own resistance to re-litigating a settled
question under social or narrative pressure.

**The SIP-flow fallacy is a base-rate problem wearing a large-number costume.** "₹20,000-plus crore
must move the market" is an intuitively compelling sentence because ₹20,000 crore is, in any
household or even most corporate contexts, an enormous sum — the fallacy is treating that felt
enormity as the relevant reference class, rather than the market's own scale. **Tversky, Amos &
Kahneman, Daniel (1974), "Judgment under Uncertainty: Heuristics and Biases,"** *Science* 185(4157):
1124–1131 **[Verified]**, is the general result this specific error instantiates: people
systematically neglect the base rate (here, NSE's own ~₹1.1 lakh crore *daily* cash-market turnover,
~₹23 lakh crore *monthly*) in favor of a vivid, available anchor (the SIP number itself, reported in
isolation, without its denominator) — the identical cognitive move the gold monograph's own §G.3
names for Indian household gold-buying ("familiarity, not fear... untethered from" a proper anchor)
and the commodity monograph names for nominal-price anchoring on "$100 oil." The corrective is not
a cleverer intuition; it is the mechanical habit of never citing a flow number without its ADV
denominator in the same sentence, which is exactly what §A.3 does and exactly what turns a
narrative-shaped question ("is ₹20,000 crore a lot?") into an arithmetic one with a small, stated
answer.

---

## Part B — Cross-country evidence and the India case record

### B.1 Heating oil and natural gas: a real, *priced* seasonal, and why gold is the exception

Energy commodities with genuine seasonal demand — heating oil and natural gas above all — are the
correct contrast case for §A.2's theorem, because they show what happens when the theorem's
"unconstrained storage" premise is violated. Natural gas storage runs on a physically capacity-bound
injection season (spring through autumn, refilling underground salt-dome and depleted-reservoir
sites ahead of winter) and withdrawal season (winter, drawing down stored gas to meet heating
demand); unlike a bank vault for gold, the number of storage sites and their injection/withdrawal
rate are hard physical constraints, not a cost that scales away with more capital. **Fama, Eugene F.
& French, Kenneth R. (1987), "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums,
and the Theory of Storage,"** studying 21 commodity futures, found that the futures basis varies
with interest rates and with seasonal patterns that proxy for time-varying convenience yield tied to
inventory levels — confirming Working's (1949) theory that when storage is the scarce resource,
a real, anticipated demand seasonal survives in the **forward curve** even under full information and
rational, competitive arbitrage, because the arbitrage that would flatten it (holding more inventory
ahead of the season) is itself capacity-constrained. Heating oil's own seasonal pattern is a useful
teaching wrinkle precisely because it is *not* naive: futures prices typically peak in **late
winter/early spring (February–April)** rather than at the height of visible heating demand in
December — a forward-looking, convenience-yield-driven pattern rather than a simple "cold months are
expensive" story, which is exactly the kind of real-but-non-obvious seasonal residual §A.2's theorem
predicts should exist once the storage-capacity premise is relaxed, and exactly what GS1 predicts
should be *absent* from gold, where that premise holds close to literally.

### B.2 US turn-of-month evidence and its decay — a partial contrast to gold's cleaner null

§A.3 already gives the founding results (Ariel 1987; Lakonishok-Smidt 1988; Ogden 1990; McConnell-Xu
2008). The decay question matters for the India mapping, and the honest answer is more nuanced than
a uniform McLean-Pontiff-style attenuation: McConnell and Xu's own 2009 follow-up, **"'Equity Returns
at the Turn of the Month': Further Confirmation and Insights,"** *Financial Analysts Journal* 65(4)
**[Verified — cited by title/venue; specific post-2010 magnitude trend `[VERIFY]`]**, reports the
effect persisting in later samples rather than vanishing outright, which stands in some tension with
Contract §5's general decay prior. The most economically coherent reading — consistent with §A.2's
symmetric point about the *arbitraging* side, not just the underlying asset, needing to be
unconstrained for a theorem to bite — is that turn-of-month liquidity clustering is harder to
arbitrage at scale than a pure cross-sectional return anomaly: there is no clean, low-cost trade that
shorts "day 20 of the month" and covers "day 2," because the effect is a *level* shift in the
aggregate market's own expected return around a diffuse, calendar-wide liquidity event rather than a
name-specific mispricing a long-short book can isolate cheaply. This is the same asymmetry §B.1
established for natural gas storage, applied to the arbitrage side of the trade rather than the
storage side — and it is precisely why §A.3's own honest India size argument, not a borrowed decay
rate, is what should govern whether 4.10 deserves a seat, rather than assuming either "all anomalies
decay" or "this one clearly hasn't" without doing the India-specific arithmetic.

### B.3 — 2009: a 78%-of-LPA drought and an 81% Sensex year

India's 2009 monsoon came in at roughly **78% of LPA** — at the time the worst since 1972 — while
the **BSE Sensex rose approximately 81% over calendar 2009**, driven overwhelmingly by the global
and domestic recovery from the 2008 financial crisis. This is the cleanest single-year demonstration
available of §A.1's aggregation argument: a genuinely severe, well-measured rainfall shock produced
severe, well-documented sector-level and macro-second-order effects (the ENSO monograph's own case
record: food inflation crossing 20% by December 2009, agri-GDP growth near 0.2% against a 7.4%
headline print — cross-cited, not re-derived here) and *no* discernible drag on the equity index,
because the index-level signal a monsoon shock could produce was, in a single year, several orders
of magnitude smaller than the signal a global liquidity recovery produced. `[VERIFY: exact Sensex
CY2009 return to the decimal — commonly cited near 81%, not independently recomputed this session]`.

### B.4 — 2014 and 2015: the double deficit, cross-cited to H55 rather than re-derived

Two consecutive deficient monsoons — **2014 at roughly 88% of LPA** and **2015 at roughly 85–86% of
LPA**, arriving as the build-up to the 2015–16 super El Niño — are the ENSO monograph's own central
India case (`partB-india-cases.md` §B2.5), and this chapter borrows its measured record rather than
re-deriving it: tractor sales falling roughly 22% from the 2013-14 peak through 2015-16, pulses
prices roughly doubling within the 2015 episode, and — the case's real teaching point — headline CPI
staying contained at **4.9–5.9%** across the two years (versus 2009's ~10% food-inflation episode)
because the RBI's newly operative flexible-inflation-targeting framework (from August 2016) and a
far more systematic pulses-import response (4.6 million tonnes, roughly $2.8 billion, in 2014-15
alone) absorbed a comparably severe shock with a visibly smaller price-level consequence. The
relevant index-level fact, already measured in EN2 and not recomputed here, is that El Niño-onset
years as a class show **no India-equity penalty** (+14.3% vs +14.0% all-years mean, n=6) — the same
null 2009 and 2014-15 each individually illustrate, now stated as a population fact rather than an
anecdote.

### B.5 — 2011: a near-normal monsoon and one of the two worst equity years on record

2011's monsoon finished close to normal — monthly readings of 112% (June), 85% (July), 110% (August)
and 106% (September) of LPA, cumulating to a season commonly read as near-normal to slightly above —
while the **Nifty fell approximately 25% over calendar 2011, the second-worst year in the index's
history after 2008's roughly 52% decline**. The proximate causes were the European sovereign-debt
crisis, elevated domestic inflation and a sequence of RBI rate hikes, the 2G and coal-allocation
corruption scandals, and rupee depreciation — none of which trace to rainfall in any channel §A.1
names. Read together, **2009 and 2011 bracket the null from both directions**: a severe drought
alongside a roaring market, and a near-normal monsoon alongside one of the two worst equity years on
record, jointly falsifying any monotone monsoon-to-index mapping far more convincingly than either
case alone — which is exactly the atlas's own point, that "monsoon years don't map to index years,"
made concrete with two dated, verifiable years rather than asserted as a general truth.
`[VERIFY: precise CY2011 Nifty return to the decimal and the exact seasonal cumulative % of LPA —
commonly cited near normal, not independently recomputed this session]`.

### B.6 — Dhanteras and Akshaya Tritiya volume records against GS1's world-price null, made concrete

The local-versus-world split §A.2 derives is not abstract: it is falsifiable against real festival
years, and it holds. **Dhanteras 2024** saw gems-and-jewellery trade estimated above **₹30,000
crore** with gold-specific trade near **₹20,000 crore**, despite a reported **15–16% year-on-year
volume decline** driven by record-high prices — silver, by contrast, posted roughly **30% volume
growth** the same festival, illustrating that even within one festival date the price-versus-volume
relationship is metal-specific and price-sensitive, not a fixed calendar effect. **Dhanteras 2025**
saw gold-and-silver sales estimated at roughly **₹60,000 crore**. **Akshaya Tritiya 2024** saw
jewellery sales "surge... despite record-high prices" on an estimated 18–20 tonnes; **Akshaya
Tritiya 2026** trade is projected above **₹20,000 crore**, up from an estimated **₹16,000 crore** the
prior year. Weddings alone are estimated to generate **roughly 50% of India's annual gold demand**
(World Gold Council). Every one of these is a real, large, well-documented **local** demand event —
and not one of them leaves a trace in the world-price series GS1 actually tested: April, Akshaya
Tritiya's own month, ranks the **worst of twelve** in the float-era world gold return series, and
November, Dhanteras's month, ranks **10th of twelve**. The local event and the world-price null are
both true at once, because they are facts about two different objects (a local retail flow; a
globally arbitraged clearing price) connected only by a wedge (§A.2) that the world price cannot see
and this desk has not built an instrument to measure. `[VERIFY: exact rupee/tonnage figures for each
festival year above — trade-body estimates, not an audited single source; ranges given reflect
genuine estimate dispersion across press reporting, not a data error]`.

### B.7 — The SIP flow series, 2016 to 2026: an order-of-magnitude decade

Monthly SIP contributions have grown from roughly **₹3,122 crore in 2016** to **₹31,961 crore in
July 2026** — an order-of-magnitude (roughly 10×) increase in nominal monthly flow over a decade,
though this is a nominal comparison and no inflation or AUM-share adjustment has been applied here
`[VERIFY: real-terms/AUM-normalized growth rate]`. The milestone path along the way is itself
informative about *pace*, not just level: SIP inflows crossed **₹26,000 crore/month for the first
time in December** `[VERIFY: exact year, most likely December 2024]`; **August 2025** printed
**₹28,265 crore** (roughly 20% above August 2024's ₹23,547 crore); **September 2025** set a fresh
record at **₹29,361 crore**; **October 2025** set another record at **₹29,529 crore**; and fiscal
2025's full-year SIP contribution reached **₹2.89 lakh crore, up 45.24% year-on-year**. This growth
is the retail-participation wave's own structural signature (Atlas 3.6, candidate **H57**) expressed
through the rupee-flow object rather than the registration-count object §A.4 already distinguished —
the same underlying wave of retail formalization and digital-onboarding growth, read at two different
counters, with no double-count between the two entries. The honest reading for 4.10's own purpose is
that a *faster-growing* flow makes the size argument in §A.3 more urgent to keep current, not less —
which is exactly why the verdict is written down with its arithmetic attached rather than as a
one-time dismissal that quietly stops being true as the flow compounds.

### B.8 — COVID, April 2020: the resilience test, and a genuine surprise in the data

If any single month should have broken a "small, mechanical, sticky" characterization of SIP flows,
it was April 2020 — a full national lockdown, a market that had just fallen more than 30% peak-to-
trough, and acute income uncertainty for exactly the salaried-household base that funds most SIP
mandates. The actual print is a genuine surprise relative to that expectation: **March 2020 SIP
inflows were ₹8,641 crore** (then a record); **April 2020 fell only to ₹8,376 crore, a decline of
roughly 3%**; **May 2020 fell further to an 11-month low of ₹8,123 crore** — a cumulative
peak-to-trough decline across the crash's worst two months of only around 6%, against an equity
index that had fallen by a factor of five to six times that magnitude. The full-year comparison
tells the same story at a coarser grain: **FY21 SIP collections totaled ₹96,080 crore against
FY20's ₹1,00,084 crore**, a roughly 4% year-on-year decline. The *actual* monthly trough, strikingly,
did not arrive until **November 2020 (₹7,302 crore)** — well after the market's own panic had passed
and after a substantial equity recovery was already underway, which reads far more plausibly as a
processing lag (bounced mandates, stoppage paperwork catching up with April–May's income shock) than
as a delayed investor reaction to the crash itself, an interpretation this monthly-resolution data
cannot fully confirm `[VERIFY: AMC/registrar-level stoppage-timing data, if it exists and is free, would
settle this directly]`. The resilience test's honest conclusion is not that SIP flows are immune to
shocks — they clearly dipped — but that the dip was small, gradual, and lagged relative to the market
event, which is exactly the profile of "real, mechanical, small" the atlas names: a flow this sticky
is a poor instrument for tactical timing in either direction, because it neither panics on the way
down nor surges on the rebound; it simply persists.

---

## Part C — India data engineering

Every object this chapter names resolves to a free pipeline or is flagged unavailable, per Contract
§3 and §12 — and, per `context-RESULTS.md`'s own scope-honesty note, **naming a pipeline here creates
no build obligation**: "CONTEXT entries do not accumulate data obligations," and nothing below is a
commitment, only a menu for if a future design (the gold sleeve's local-premium hygiene above all)
ever needs one of these built.

**IMD rainfall — free, primary, already the H55 pipeline.** IMD's seasonal bulletins
(`imd.gov.in`) publish the monthly and cumulative all-India and subdivision-level `% of LPA` figure
directly, on the 1971–2020 baseline (868.6 mm) described in §A.1; this is the *same* pipeline H55
already specifies and this chapter adds nothing to it beyond noting that any 4.7 sector-conditioner
build should consume it through H55's existing gating design, not re-implement a parallel reader.

**AMFI — monthly aggregates, and a genuine gap for 4.10's own object.** AMFI's monthly note
(`amfiindia.com`) publishes total SIP contribution and AUM at **monthly** granularity — the source
for every number in §B.7 and §B.8 — but AMFI does **not** publish a public date-of-month histogram of
SIP debits; the "clustering on the 1st/5th/7th/10th" claim in §A.3 rests on AMC-form conventions and
registrar-level (CAMS/KFintech) market commentary, not a downloadable AMFI series
`[VERIFY: whether CAMS/KFintech publish any aggregate, anonymized date-of-month distribution — not
located this session]`. This is a real limitation, not a rounding error: **AMFI's own data cannot
test 4.10's core clustering claim at all**. The free workaround is indirect: NSE's and BSE's own
**daily "provisional" cash-market activity releases** (published same-day or T+1, free, already
within Contract §3's approved sources) report aggregate DII/mutual-fund net buy-sell value per
trading session, which is a genuine — if imperfect — proxy for whether early-calendar-month sessions
show elevated net MF buying; the limitation to state plainly is that DII flow is not SIP flow (DIIs
buy and sell for many reasons besides SIP deployment), so this proxy can bound the question but
cannot isolate the mechanism cleanly.

**WGC India demand, quarterly — free, and the right instrument for 4.8/4.9's flow side.** The World
Gold Council's "Gold Demand Trends: India Focus" quarterly release (`gold.org/goldhub`) is the
correct free, citable source for every India consumer-demand figure in §B.6, and already the source
D06 and this chapter both draw on for the weddings-are-50%-of-demand figure and the quarterly
jewellery/investment split.

**MCX and dealer premia — the one genuinely unfree object in this chapter, stated as such.** The
actual 4.9 object — a domestic dealer premium or discount over landed cost, at daily or weekly
frequency — is **not** freely, auditably available as a published time series: WGC and industry-body
commentary sometimes cites premium/discount estimates, but these are commentary embedded in
reports, not a downloadable, replicable dataset, and this chapter says so rather than quietly
treating a cited number as if it were a series. What **is** free and fully reproducible: the customs
duty schedule itself (CBIC notifications, publicly gazetted, including the July-2024 15%-to-6% cut
cited in §A.2), and therefore the **landed-cost arithmetic** — `P_world · FX · (1 + duty + GST)` — as
a computable series with no survey input at all. A candidate free domestic reference *price* (not
premium) worth flagging for a future design is the India Bullion and Jewellers Association's daily
published rate `[VERIFY: IBJA data terms, history depth, and whether it is genuinely free/scrapable
— not confirmed this session]`; even if usable, it supplies a domestic reference *level*, and a true
premium series still requires netting it against the landed-cost arithmetic above, which is exactly
the GS-D1 design `context-RESULTS.md` already names as conditional, not committed.

**Auto sales, monthly — two free sources with a real difference.** SIAM's monthly press releases
(`siam.in`) report manufacturer-reported wholesale dispatches — the source for §B.6's adjacent point
about October/November 2025 records and the GST-cut confound worth flagging for any future festive-
season study (October 2025's record passenger-vehicle dispatch figure was explicitly co-driven by a
GST rate reduction alongside festive demand, a textbook confound a raw calendar comparison would
otherwise misattribute entirely to seasonality). VAHAN (`vahan.parivahan.gov.in`), by contrast,
reports vehicle **registrations** — a retail, consumption-facing number less exposed to
channel-stuffing at the wholesale-dispatch level, and the better instrument if a future H55 or 4.7
sector build ever wants the rural-consumption-facing series specifically.

**Turn-of-month construction from bhavcopy — a grid, not a magic window, per Contract §6.** NSE and
BSE historical bhavcopy (free, daily, already in scope for every other calendar entry in this
program) is the raw material; what must never be a single asserted constant is the **window
definition** itself. The literature alone offers at least three non-equivalent conventions: Ariel's
own first-nine-trading-days-plus-prior-month's-last-day; Lakonishok-Smidt's ±4-trading-days-around-
month-end; and McConnell-Xu's tighter four-day (t−1 to t+3) window — a **sensitivity grid across
window widths**, exactly the Contract's own "grids not magic numbers" discipline, is the only honest
way to construct this, never a single asserted definition chosen after seeing which one prints best.
Constructing any of these requires a trading-day calendar (holiday list) to convert calendar-date SIP
debit dates into trading-day offsets correctly — the identical busday-arithmetic problem the
calendar-mechanics chapter's exclusion calendars already solve for statutory drain and expiry dates,
reusable here with no new machinery.

**What is deliberately not vaulted.** No design is registered against any pipeline in this Part.
4.7's tradable content routes entirely through H55, already vaulted and already gated; 4.8 and 4.9's
flow-side content is documentary (Part B), not a return-budget candidate; 4.9's premium-side content
awaits a free, auditable series that does not yet exist and is not being built speculatively; and
4.10's own honest arithmetic (§A.3) is the reason no design is registered for it either — a
pass-refuse verdict, per §A.4, closes the question rather than opening a runsheet item. This is the
concrete meaning of "CONTEXT entries do not accumulate data obligations": every pipeline above is
written down so a future designer does not have to re-discover it, and none of it is owed to the
registry today.

---

# Appendix: the desk print (real-data leg)

# Atlas 4.7-4.10 — the CONTEXT quartet: desk print and honest read
Written AFTER the print (2026-09-02). Pre-registration: ledger GS1.
Script: scripts/analyze_gold_seasonality.py. Data: vaulted gold monthly (float era
1972-02..2026-07, n=654 monthly log returns, ~54-55 obs per calendar month).

## The print
GS1 (gold festival seasonality, demonstration): Kruskal-Wallis H=10.87, **p=0.454** across
the 12 months. No world-price calendar structure. The descriptive ranks land the lesson
better than the omnibus: April (Akshaya Tritiya's month) is the WORST month of twelve
(median −0.60%/mo), May is 11th, November (Dhanteras/wedding season) is 10th, and the folk
"September strength" claim sits at rank 6 of 12 — dead middle. January is rank 1 (+1.50)
and stays exactly where CW3's discipline puts every un-mechanismed rank-1: logged, never
interpreted.

## Honest read
1. This is D06 demonstrated, not discovered: India buys ~a quarter of world consumer gold
   demand but hosts none of the price formation — festival demand shows up in LOCAL premia
   (MCX/dealer premia over landed cost), not in the London/COMEX price. The quartet's
   verdicts don't move: 4.9 CONTEXT (local-premium hygiene for the gold sleeve only).
2. The print retires a folk claim cheaply: a desk that believed "buy gold before Dhanteras"
   would have been long the 10th-worst month. The lesson gets the bar chart.
3. Scope honesty: monthly world-price data cannot see the local premium cycle (the real
   4.9 object) — that needs MCX-vs-landed premia, a runsheet series, registered as GS-D1
   only if the gold sleeve ever needs it (no design registered now; CONTEXT entries do not
   accumulate data obligations).

## The other three (no trials, by scope)
- 4.7 monsoon: the tradable object is ENSO (2.14, H55 chain-conditioner) + IMD % of LPA in
  season; index-level effect honestly unquantified — CONTEXT, sector reduce-only.
- 4.8 festive/wedding demand: a flow fact in earnings expectations — CONTEXT only.
- 4.10 SIP turn-of-month: ₹20k+cr/month clustering on early-month debit dates is real and
  MECHANICAL — but monthly data cannot see it, its size vs ADV is small, and the honest
  routing is the H58 ops lens (it is a known demand pulse, not alpha). Listed to keep it
  from returning as "discovered alpha". CONTEXT/EXECUTION at most.

---

# Parts D–H — the CONTEXT quartet (atlas 4.7/4.8/4.9/4.10; Band 4 closes)

## Part D — What GS1 adds, and the theory it demonstrates

One print, one theorem made visible. The storage-arbitrage logic (Part A) predicts that a
perfectly anticipated demand seasonal leaves NO seasonal in the world price of a storable,
globally arbitraged asset — anticipation is the arbitrage. GS1 measures exactly that:
across 654 float-era months, no calendar structure (KW p=0.454), and the Indian festival
months rank WORST (Apr 12/12, May 11/12, Nov 10/12) while folk-September sits at 6/12.
The desk's gold sleeve learns two things it can act on: (i) never schedule gold entries by
festival calendar; (ii) the ONLY seasonal object that exists is the local premium wedge —
which is a hygiene input for execution (don't buy the sleeve through a fat premium week),
not a timing signal. n≈54-55 per month gives this null real teeth at seasonal effect sizes
worth trading; the demonstration is cheap, decisive, and closes the folk claim.

## Part E — No algorithm, by verdict

CONTEXT entries ship no module. Their operational form is the pre-written refusal: one line
per story, on file, so the desk declines each in real time without spending a meeting —
- monsoon story → "sector reduce-only via the ENSO/IMD chain (H55); index claim
  unquantified, no trade" (docs/cycles/27-enso.md owns the machinery);
- festive-demand story → "a flow fact already inside earnings expectations; no trade";
- Dhanteras-gold story → "GS1: the festival months are the worst months; premium hygiene
  only";
- SIP turn-of-month story → "real, mechanical, small vs ADV; H58's ops lens if it ever
  matters; no alpha".
The quartet's product is this immune-system card, and the register's taxonomy gains its
demonstration that CONTEXT is a verdict with content — not a shrug.

## Part F — Harvest map

Harvested: the refusal card (above); the GS1 print for the Cycle School (the cleanest
possible "demand seasonality is not price seasonality" chart). Registered designs: NONE —
stated deliberately. A CONTEXT verdict that spawned data obligations would be a seat wearing
a smaller badge; the scope-honesty note in context-RESULTS.md governs (the local-premium
series GS-D1 is named as the object we would need IF the gold sleeve ever escalates, and is
NOT registered now).

## Part H — Knowledge ledger (Band 4 closes)

**Established (our print):** no world-gold-price festival/month structure, float era (GS1).
**Pooled-prior (Tier B literature):** monsoon → rural income → sector demand (mechanism
solid, index mapping honestly unquantified); turn-of-month exists in US history with the
payday-liquidity mechanism and decays; anticipated seasonals cannot survive storage
arbitrage (Samuelson/Working). **Awaits India data:** nothing FOR THIS ENTRY (no designs,
by verdict); the monsoon chain's data needs live in the ENSO entry (H55). **Unknowable:**
each year's monsoon (that is weather, and the ENSO state only tilts its odds — the desk
reads states, never forecasts rain).

**Band 4's tally:** ONE new seat (L5 calendar windows — the schedule that cannot point) +
ONE ops pack (H58 exclusion calendars, no alpha surface, tests enforcing both refusals) +
ONE instrumented pass (CW2 April, promotion refused, paper-trade CW-PT1) + ONE edge design
(RC1 reconstitution, sleeve-side) + FOUR context verdicts with one demonstration print
(GS1) + TWO rejects with the omnibus evidence (CW3). The annual layer contributes exactly
what the atlas predicted: scheduling, mechanics, and immunity — and no return budget moved.
