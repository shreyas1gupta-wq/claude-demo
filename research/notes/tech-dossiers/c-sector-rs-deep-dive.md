# Sector Relative Strength / Rotation: A Deeper Pass

*Literature and practitioner dossier, Track T companion, 2026-09-10. No web fetches this
session — every literature and practitioner claim is from training knowledge, unverified
against a live source, and carries **[LIT]** or **[PRACTITIONER OBSERVATION, not
backtested by this desk]** with a confidence hedge; a citation whose author pairing, venue,
or exact figure I cannot stand behind carries **[VERIFY: ...]** per CONTRACT §12's
convention. Desk numbers are quoted verbatim from `research/register/trial-ledger.md` and
marked **[DESK, <entry>]** — none are re-derived here; bars are never moved after a print.

This dossier **extends dossier a's** §4 (Sector relative strength / rotation) — it does
not restate it. Dossier a already: (i) cited Moskowitz-Grinblatt (1999) as the anchor for
industry momentum as a first-class signal family; (ii) quoted FUN-D3's full result — the
textbook rotation inverting in India (defensives lag, cyclicals/financials lead, forward
21-day relative returns, in RISK-OFF states); (iii) named the NSE sectoral TR pull as the
Priority-1 unblock, gated to principal-machine; (iv) proposed three designs to pre-register
on arrival. Below is new material only: the practitioner canon in full (Fidelity's clock,
Stovall), the academic base widened (Moskowitz-Grinblatt magnitude/decay, Hong-Torous-
Valkanov, Grundy-Martin), Indian institutional practice in depth, a precise accounting of
what FUN-D3 does and does not cover, the target-series list with launch-year hedges, and a
refined verdict with a re-ranked edge-candidate list.

## 1. The practitioner canon

**Fidelity's "business cycle clock."** The most widely distributed version of the
sector-rotation heuristic in the retail- and advisor-facing literature. The claimed
sequence, as commonly presented **[PRACTITIONER OBSERVATION, not backtested by this
desk]**:

| Cycle stage | Overweight sectors | Stated rationale |
|---|---|---|
| Early cycle (recovery off a trough) | Cyclicals, Financials (also often Consumer Discretionary, Real Estate) | Credit eases, rate-sensitives re-rate first, pent-up demand releases |
| Mid cycle (the longest stage) | Industrials, Technology | Capex accelerates, earnings broaden beyond the initial re-rating |
| Late cycle (growth decelerating, inflation rising) | Energy, Materials, Staples, Health Care | Input-cost pass-through favors commodity producers; demand growth slows toward defensives |
| Recession | Utilities, Staples (Health Care often grouped here too) | Defensive, inelastic-demand cash flows preferred when earnings are falling broadly |

This is a **widely-taught heuristic, not a peer-reviewed result** — it is built by
overlaying historical average sector performance onto NBER-style business-cycle staging
determined with hindsight, then presented as a forward playbook. The stage boundaries
themselves (early/mid/late/recession) are not observable in real time with the precision
the chart implies; NBER recession calls alone arrive with a multi-month lag, and "mid"
vs "late" cycle is not a dated event at all, only a retrospective judgment.

**Stovall's "Sector Investing."** Sam Stovall (S&P's long-time sector strategist)
formalized a closely related wheel-shaped business-cycle/sector-leadership framework in a
practitioner book commonly cited as *Sector Investing* (McGraw-Hill) **[VERIFY: exact
year — recalled as mid-to-late 1990s]**. Stovall ties sector leadership to a four-phase
wheel (full recession → early recovery → full recovery → early recession) and to
coincident/leading indicators (ISM PMI, yield curve) rather than dated NBER phases — a
methodological improvement over the Fidelity chart (real-time-observable conditioning
variables) that still does not resolve the problem below **[PRACTITIONER OBSERVATION, not
backtested by this desk]**.

**Does the clock beat buy-and-hold out of sample?** This is where the testing literature
is least flattering to the canon **[LIT, LOW CONFIDENCE — no single canonical
peer-reviewed paper anchors this claim; a directional synthesis of a scattered
practitioner/academic testing literature]**. Gross-of-cost backtests using *ex post* phase
dating show real sector-return dispersion across phases — the clock is not describing
nothing — but three things erode it before it becomes tradable: (i) **regime-timing
error**, phase transitions identified with a lag (the lag FUN-D1 quantifies formally, §4),
so a real-time investor rotates a quarter or two after the textbook entry; (ii)
**transaction costs and whipsaw**, rotating four-plus sleeves on every phase call pays
turnover on false signals, and phases are not clock-like (CONTRACT §4's "persistence, not
periodicity" — only a handful of complete US cycles exist since sector data began, nowhere
near the ≥4-period bar for anything above Tier B); and (iii) **look-ahead in the canon's
own construction**, the textbook sector-to-phase assignments were largely built by looking
at which sectors *did* well in each historical phase — closer to curve-fitting than
ex-ante forecast. Net effect: published rotation-clock backtests that survive honest
out-of-sample and cost treatment are the exception, and several practitioner post-mortems
report underperformance versus a static sector-cap-weighted benchmark once lag and costs
are charged **[LIT, LOW CONFIDENCE]**. This is the gap dossier a's §4 already named
structurally ("rotation-over-the-cycle claims are almost always stated contemporaneously
with the identified phase, not as a tradable lead") — this section supplies the wider
practitioner-testing context behind that sentence.

## 2. The academic base, widened

**Moskowitz-Grinblatt (1999), in more depth.** Dossier a already gives the full citation
and headline claim (industry momentum "largely subsumes" individual-stock momentum). Two
further facts matter for this desk's own momentum book. **Magnitude and construction**:
M&G's central test held individual stocks *randomly selected within* winning/losing
industries — destroying stock-specific momentum information while preserving the
industry-level return — and found this randomized portfolio captured **most of the
profit** of standard individual-stock momentum, on the order of half or more of the raw
spread (exact split not citable with confidence) **[LIT, LOW CONFIDENCE — directionally
certain, the fraction is not]**; the complementary industry-neutral cut survives but is
smaller, and — distinctively — is **not** subject to the sharp January reversal that
plagues standard winner/loser portfolios **[LIT]**. **Decay at longer horizons**: industry
momentum is profitable at 1-12 months but, like stock momentum, subject to **long-run
reversal** beyond roughly a year — the industry-level analog of DeBondt-Thaler
**[LIT, LOW CONFIDENCE]**. This bounds how the desk should size any future industry-
momentum design: a 12-1 rank (dossier a's edge candidate #3) sits inside the window the
literature expects a positive spread; a 24-36 month version would fight the same reversal
literature that already killed T2 and F7a (dossier a §2).

**Hong, Torous & Valkanov — do some industries lead the market?** Hong, Torous & Valkanov
(2007), "Do Industries Lead the Stock Market?", *Journal of Financial Economics*
83(2):367-396 **[LIT — author/venue/year recalled with reasonable confidence; exact
volume/page as [VERIFY]]**. Finding: industries tied to macroeconomic fundamentals
(commodity-linked and consumer-facing industries, rather than technology) **lead** the
aggregate market by up to roughly two months — past industry returns forecast *future
market* returns better than the reverse **[LIT, LOW CONFIDENCE on the exact lead window
and industry list]**. Mechanism: gradual information diffusion (the Hong-Stein 1999
family) applied industry-to-market rather than firm-to-firm. This is a *lead-lag*, not a
*rotation*, claim — it says nothing about which sector to overweight when, only that some
industries carry unpriced information. It is a third, independent (from George-Hwang, from
BSV/HS) diffusion mechanism the desk should keep distinct when writing survival arguments
(CONTRACT §5) for any industry-level design.

**The Grundy-Martin re-examination — a complication, not a rebuttal.** Grundy & Martin
(2001), *Review of Financial Studies* 14(1):29-78 **[LIT — author pairing/venue recalled
with reasonable confidence; exact title/page range as [VERIFY]]**, re-examine momentum
with hedged, factor-neutral constructions. Relevant result: momentum hedged neutral to
industry (alongside size and book-to-market) still leaves a sizeable spread — the M&G
"industry explains most of momentum" claim is not the full story; a genuine
within-industry, stock-specific component remains economically large **[LIT, LOW
CONFIDENCE on the exact surviving magnitude]**. Bracketed together: M&G show industry
captures a large share of *raw* momentum profit; Grundy-Martin show a real residual
survives once industry is hedged out. This bears directly on this desk's **already-booked
momentum work** (L3's rank-blend, N4a's 52-week-high/12-1 overlap) — the desk has never
decomposed its own India momentum sleeve into industry-driven versus within-industry
components, and that decomposition is not a null question: a meaningful share of L3's
momentum leg could be re-expressible as undisclosed industry momentum, with different
decay/crowding properties than the stock-picking story told so far. Flagged as an open
decomposition question, not run here.

## 3. Indian institutional practice

*(All claims in this section are [PRACTITIONER OBSERVATION, not backtested by this desk] —
general knowledge of the Indian asset-management industry, not verified against a live
source or against desk data this session.)*

**Thematic and sector mutual funds as the retail vehicle.** Indian AMCs run standing
sector/thematic fund lines that are the primary retail-facing implementation of sector
calls: Banking & Financial Services, Technology/IT, Pharma & Healthcare, Infrastructure,
PSU-themed (incl. PSU-focused ETFs such as CPSE and Bharat 22 — divestment vehicles as
much as sector calls), and Consumption funds. These are typically marketed around a
narrative moment (a rate-cut cycle for banking funds, a global tech re-rating for IT
funds, a capex narrative for infrastructure funds, the 2023-24 PSU re-rating) — and NFO
timing is a known industry pattern worth flagging: launches and AUM inflows are
anecdotally concentrated **near sector performance peaks, not troughs** (infrastructure
funds proliferated into the 2007-08 peak; pharma launches clustered before 2016-2020
underperformance) — a flow-based contrarian indicator, folklore-grade, not backtested by
this desk, directionally consistent with (not proof of) the same "the identified narrative
is late" pattern FUN-D1/FUN-D3 establish formally (§4).

**NIFTY sector indices as the liquid tradeable proxy.** NSE's sectoral index family —
Nifty Bank, IT, Pharma, FMCG, Auto, Metal, Realty, Energy, Financial Services (broader than
Bank alone: NBFCs/insurance/capital markets), and Media — are among the **most liquid,
longest-running tradeable sector proxies in India**. Several run since the early-to-mid
2000s (base/launch dates hedged in §5), carry listed ETFs (e.g., Bank BeES), and **Nifty
Bank carries one of the most liquid derivatives contracts (futures, and especially weekly
options) in the Indian market** — arguably deeper than most single-stock F&O. This is
exactly why these indices are the natural target of the gated runsheet pull (§5): the
*best-instrumented* mid-frequency signal family available in India once it lands, better
instrumented than the survivor-panel-derived, equal-weighted baskets FUN-D3 currently uses
(§4).

**The informal cyclicality playbook Indian desks use.** As practiced conversationally
**[PRACTITIONER OBSERVATION, not backtested by this desk]**, folklore-grade: rate-
sensitives/banks **lead a rate-cut easing cycle** (mirroring the Fidelity "early cycle"
claim, §1, applied to India's monetary cycle); IT is a **defensive-with-currency-
optionality** (USD revenue provides a translation tailwind when INR weakens alongside
domestic stress); pharma is a **domestic defensive** (inelastic demand, plus a currency
tailwind for exporters); infrastructure/industrials/cement are **capex-cycle
beneficiaries** around government pushes (often overlaid with budget/election-cycle timing
— exactly the fixed-calendar framing CONTRACT §8 forbids admitting without a clock-test
pass). None of these four is backed by a citable India-specific academic literature, and —
per the cross-check below — the one piece the desk has actually tested (IT as a
currency-hedge defensive in risk-off) **already failed**.

## 4. Cross-check against the desk's own booked findings

**FUN-D1 — the phase-level base rate, quoted in full.** FUN-D1 (JST panel, 17 countries,
phase defined by growth level-and-direction, real-time-honest: phase in year *t*
conditions returns in year *t+1*) found: **"Next-yr real equity: RECOVERY +8.4% >
CONTRACTION +7.1% > EXPANSION +5.0% > SLOWDOWN +2.5%"**, with recovery beating expansion
in 13 of 16 countries, and the contrast sharper post-1950 (**CONTRACTION +12.0% / RECOVERY
+10.8%** vs **EXPANSION +5.7% / SLOWDOWN +1.2%**) **[DESK, FUN-D1]**. Critically, the
**same-year (contemporaneous)** read inverts this entirely: **"SAME-year equity is best in
EXPANSION (+8.6) and worst in CONTRACTION (+2.1)"** **[DESK, FUN-D1]** — the mechanism the
desk booked as "returns are CONCURRENT with the phase but by the time a phase is
identifiable you are being paid for the NEXT one." This is precisely the structural reason
the practitioner sector clock (§1) is vulnerable: it is built from the same kind of
contemporaneous phase-to-performance mapping FUN-D1's p6 cell shows to be the *wrong* one
to trade forward.

**FUN-D2 — the earnings-cycle anticipation asymmetry, quoted.** FUN-D2 (Shiller US
1871-2023) found price leads the earnings trough — **"price bottoms ~10m BEFORE the
earnings trough (price first in 75% of episodes) but does NOT reliably lead peaks (38%)"**
**[DESK, FUN-D2]** — markets anticipate recoveries but not recessions, an asymmetric-lead
fact that reinforces FUN-D1's phase-timing lesson from an independent (earnings-level,
not GDP-level) angle: whatever "cycle stage" a sector-rotation clock is keyed to, the
market has typically already moved before that stage is nameable, and it has moved
*more reliably* at troughs than at peaks — this asymmetry has no counterpart in the
symmetric four-stage rotation clocks (§1), which treat entering and exiting each stage as
equally identifiable events.

**FUN-D3 — the direct sector-level print, quoted in full, and precisely bounded.** FUN-D3
(India, survivor panel 2012-2021, one-way) tested the rotation-after-identified-state trade
directly and printed: **"In RISK-OFF states the DEFENSIVES lag forward (fwd-21d rel: DEF
-1.76, PHARMA worst -2.07, IT -1.86) while cyclicals and financials lead (+0.57%/+0.69%,
NBFC best at +1.73%), consistent in both the 2012-16 and 2017-21 era-halves"** **[DESK,
FUN-D3]**, with the IT-as-USD-hedge folk claim (§3) explicitly killed one-way at s9
(**-1.86**) **[DESK, FUN-D3]**, and a state-independent fact booked alongside it: **"PSU
banks were the chronic worst basket in both CALM-UP and CALM-DOWN and merely flat in
RISK-OFF"** **[DESK, FUN-D3]**.

**Does this already constitute indirect sector-rotation evidence? Yes, precisely bounded,
and the bound matters.** FUN-D3 is *not* a stock-characteristic proxy (beta, margin
cyclicality) standing in for sectors — it is already built from named, equal-weighted
sector baskets (FMCG/PHARMA/IT; METALS/AUTO/CAPGOODS/REALTY; PVTBANK/PSUBANK/NBFC, the
SEC-battery baskets reused verbatim), read relative to the all-basket market, conditioned
on a market-stress state. In that sense it **is** sector-level evidence that
business-cycle-adjacent phase (proxied here by NIFTY-vs-trend × VIX-percentile, not yet
true GDP phase) drives which sector groups lead and lag — a genuine, if narrow,
sector-rotation result, and the desk should stop describing its own position as merely
"no data yet." What FUN-D3 is **not**, and what a true sector-RS design still needs, is
four specific things, each traceable to the design's own stated scope:

1. **Survivorship.** The panel is 2012-2021 survivors only; it cannot see names that
   delisted mid-sample — FUN-D3's own entry names this "the partial's biggest caveat"
   **[DESK, FUN-D3 / dossier-a cross-reference]**. True NIFTY sectoral TR indices are
   float-cap-weighted with standard index-maintenance (survivorship-consistent by
   construction) — a methodologically different, not merely longer, instrument.
2. **Construction mismatch with the academic anchor.** FUN-D3 tests a *state-conditioned
   relative-return* read ("given state X, which basket led over the next 21 days"), not
   the Moskowitz-Grinblatt *cross-sectional industry momentum* construction ("rank all
   sectors on trailing 6-12 month return, buy top, sell bottom"). Different objects
   sharing a data need; FUN-D3 passing or failing says nothing about whether a genuine
   12-1/6-1 industry-momentum rank would work in India. Dossier a's edge candidate #3
   already flags this design as untested — it is not merely untested, it is *conceptually
   distinct* from what FUN-D3 measured, not a scaled-up version of it.
3. **Rotation magnitude, turnover, and whipsaw are entirely unpriced.** FUN-D3's own s1
   cell records its four states **"run short (2-8d median)"** with CALM-UP alone covering
   **64% of days** **[DESK, FUN-D3]**. A rotation overlay trading every implied state flip
   would churn at a rate no cell in FUN-D3 costed — the design is one-way, paper-only (no
   cost model, no turnover accounting), so even a fully-confirmed version of its sign
   pattern says nothing about whether trading it clears costs. This is the biggest gap
   between "an indirect rotation fact is booked" and "a rotation *strategy* exists" — the
   sectoral TR pull alone will not close it; it also needs the book's own cost stack
   (Known Prior #6) applied to a specific, not-yet-designed rotation rule.
4. **True business-cycle phase versus a market-technical proxy.** FUN-D3 states its states
   are **market-cycle proxies, "NOT GDP phases"** **[DESK, FUN-D3]** — the true GDP-cycle
   successor is **FUN-D4**, gated on the IIP monthly pull (`ingest/vault/india_macro/`,
   principal-machine per RUNSHEET.md), recorded there as "replaces FUN-D3's market
   proxies." The practitioner clock (§1) claims the *business* cycle, not the
   *market-stress* cycle; FUN-D3 is still one proxy layer removed from testing it directly.

In short: FUN-D3 already falsifies the single most commonly stated version of the India
sector playbook ("go defensive once risk-off is identifiable") and the IT-as-currency-
hedge sub-claim, one-way, at the sector-basket level, under a market-stress-state
definition. It does **not** yet test genuine cross-sectional industry momentum, price
rotation turnover/whipsaw, run survivorship-free, or condition on the true business-cycle
phase the practitioner canon claims to describe. All four gaps close only with data
gated to principal-machine pulls (§5).

## 5. Target series for the runsheet ask

RUNSHEET.md already carries a single consolidated row for this pull (destination
`ingest/vault/index_sector/`, principal-machine, unblocking FUN-D3 FULL, the SEC-D5 India
analog, and the sector-RS/industry-momentum design named there as "SECTOR-GATE,
2026-09-10"). For that row to be maximally actionable when it is finally pulled, the
individual series it bundles, named precisely:

| Index | Approx. base/launch | Note |
|---|---|---|
| Nifty Bank | base 1 Jan 2000 = 1000, trading early-to-mid 2000s **[VERIFY]** | deepest and most liquid; carries one of the most active options contracts in India |
| Nifty IT | base 1 Jan 1996 = 1000, published ~2000 **[VERIFY]** | post-dot-com relevance |
| Nifty FMCG | base ~1996, published early 2000s **[VERIFY]** | |
| Nifty Pharma | base ~2001 **[VERIFY]** | |
| Nifty Auto | base ~2004 **[VERIFY]** | |
| Nifty Metal | base ~2003-2004 **[VERIFY]** | |
| Nifty Realty | launched **2007 [VERIFY: exact month]** | youngest core sector; tracks the mid-2000s listed-developer wave |
| Nifty Energy | base ~2001 **[VERIFY]** | |
| Nifty Financial Services | launched **2011 [VERIFY]** | broader than Bank: NBFCs/insurance/capital markets/housing finance |
| Nifty Media | base ~2003-2004 **[VERIFY]** | |

Every one of these has daily history back to somewhere in the 2000-2007 window
(materially longer than the current 2012-2021 survivor panel), free via NSE (blocked at
this environment's proxy, hence the principal-machine gate). The vault destination and
unblock list are unchanged from RUNSHEET.md — this section only sharpens which named
series the row resolves to, so the pull can be scoped against this list directly.

## 6. Revised verdict

The dossier-a verdict as currently stated ("no confident academic magnitude for RS-based
sector rotation decay exists to cite at [LIT] strength; treat the practitioner playbook as
Tier C, directional-only, pending a real-time-conditioned test") is **still directionally
right but incomplete** — it undersells what FUN-D3 already established. The refined
sentence this desk should adopt:

> **No direct sector-index rotation edge is measurable today (the NSE sectoral TR pull has
> not landed); but indirect, one-way evidence already exists that in India, once a
> market-stress state is identifiable, the textbook defensive rotation has already missed
> its window and cyclicals/financials lead the rebound instead (FUN-D3) — consistent with
> the same contemporaneous-versus-forward inversion FUN-D1 establishes at the country-GDP-
> phase level and FUN-D2 establishes at the earnings-cycle level. This finding is booked
> Tier-C (one-way, survivor-panel, market-proxy states, no cost model) and is reduce-only
> per CONTRACT §4: it may inform a de-risking or basket-avoidance rule, never a positive
> rotation trade, until the NSE sectoral TR pull lands and both the survivorship and
> turnover-cost gaps are closed.**

## Edge candidates once the NSE sectoral pull lands, ranked by evidence strength

1. **FUN-D3 FULL — re-run the existing, already-once-confirmed design on survivorship-free
   sectoral TR.** Mechanism: none new — this is the identical state-conditioned relative-
   return construction, just retiring its stated weakest caveat. Magnitude: the partial's
   own print, **DEF -1.76 / cyclicals+financials +0.57 to +0.69 at fwd-21d** **[DESK,
   FUN-D3]**, to be reproduced or revised on the full history. Data needed: NSE sectoral TR
   daily (§5). Kill condition: sign or magnitude reversing once delisted names are
   included, or failing to reproduce across era-halves the way the partial did.
2. **Genuine cross-sectional industry momentum, Moskowitz-Grinblatt form, 12-1/6-1 rank
   across 8 NSE sectors.** Mechanism: industry momentum as a distinct, largely
   trend-continuation (not regime-state) construction **[LIT]**; expected decay beyond
   ~12 months per the M&G long-run-reversal finding (§2). Magnitude: not yet estimable for
   India — genuinely untested, distinct from FUN-D3 (§4, point 2). Data needed: NSE
   sectoral TR daily. Kill condition: failing to beat the stock-level L3 composite net of
   cost, or failing the same STW1999-style joint-bootstrap correction T-CTRL1 already
   applied to technical rules (dossier a §2).
3. **A rotation-turnover/whipsaw cost estimate applied to FUN-D3's own state structure.**
   Mechanism: none — a costing exercise, not a new signal; answers whether FUN-D3's sign
   pattern could ever clear costs given state durations of 2-8 days median **[DESK,
   FUN-D3, s1]**. Magnitude: unknown, that is the point. Data needed: sectoral TR (for
   realistic impact assumptions) plus the book's cost stack. Kill condition: implied
   turnover cost exceeding the FUN-D3 spread at any reasonable rebalancing discipline.
4. **FUN-D4 — the true GDP-cycle-phase successor.** Mechanism: replaces FUN-D3's
   market-stress proxy with actual India business-cycle phase (IIP-derived), testing the
   practitioner clock (§1) on its own terms for the first time. Magnitude: not yet
   estimable — no India GDP-phase sector print exists at all today. Data needed: India IIP
   monthly (MOSPI/RBI), already a named runsheet row distinct from the sectoral-TR pull.
   Kill condition: same as FUN-D1's own bar — if contemporaneous and forward reads do not
   separate the way FUN-D1 found at the country level, the practitioner clock fails on
   its home turf, not just as an India transplant.
5. **Flow-based contrarian sector-fund-NFO timing (weakest, folklore-only).** Mechanism:
   retail thematic-fund launch/AUM-inflow timing as a contrarian sentiment marker (§3)
   **[PRACTITIONER OBSERVATION, not backtested by this desk]**. Magnitude: none to cite —
   purely anecdotal instances (2007-08 infra, pre-2016 pharma, 2023-24 PSU). Data needed:
   AMFI scheme-level NFO and AUM-flow history by sector-fund category (not currently a
   named runsheet row). Kill condition: this would need its own pre-registered design
   before it earns anything above narrative status; it is listed last, and last in
   evidentiary weight, deliberately.
