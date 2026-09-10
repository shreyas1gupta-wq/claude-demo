# Valuation Measure Horse-Races and Combinations — the Empirical Literature to Mine

**Status: LITERATURE DOSSIER (2026-09-10), principal-directed. No web fetches — written from
training knowledge per instruction.** Complies with `research/CONTRACT.md` v0.1. Fourth of the
val-dossier set; does not repeat `a-valuation-measures-methods.md` (the ratio toolkit),
`b-value-complementarity.md` (what combines with value, and the "fake diversification"
critique of stacking correlated value measures, its §4), or `c-india-valuation.md` (India
evidence, distortions, the five ranked handoff designs) — all cross-referenced, not re-derived.
This dossier's job: paper-by-paper HORSE RACES (measure vs. measure, not measure vs.
companion-factor), the combination-construction literature, horizon/turnover, small-vs-large,
closing with a reconciliation against the desk's own booked VAL-D1..D6 ladder. Tags: **[LIT]**
= published/practitioner claim, hedged in the same breath; **[BOOKED <entry>]** = a print read
directly from `research/register/trial-ledger.md` this session. Per CONTRACT §4/§9 every
non-India citation is a cross-country prior, Tier B at best until purged-CV India tests exist.

---

## 1. The horse-race papers

**O'Shaughnessy, *What Works on Wall Street* — P/S's rise and demotion.** The clearest
practitioner horse race, re-run by its own author across four editions (1996-2011/12) [LIT,
HIGH CONFIDENCE the editions and arc exist; LOW on any specific number below]. The 1996
edition's headline: low P/S was the single strongest value predictor in his multi-decade
Compustat sample, beating P/E, P/B and P/CF — partly a data-quality argument, since sales is
almost never negative or restated, so a P/S screen never has to drop loss-making names the way
a naive P/E screen must [LIT, MEDIUM CONFIDENCE on the mechanism]. Later editions walk this
back: single-factor P/S loses ground to rank-averaged multi-measure composites (P/E, P/B, P/S,
P/CF, EBITDA/EV, shareholder yield) and to shareholder yield specifically, once the dot-com
bubble/bust is folded into the sample [LIT, LOW CONFIDENCE — well-documented arc, no specific
spread asserted]. Reads as a pre-registered case study in CONTRACT §5's decay discipline
applied to a valuation measure rather than a strategy.

**Loughran & Wellman (2011, *JFQA*), enterprise multiple.** Already anchored in dossier a §1 —
re-framed here only as a horse race. Their actual test is a joint Fama-MacBeth regression (EM
alongside B/M, size, momentum), finding EM's coefficient robust and not subsumed by B/M [LIT,
MEDIUM CONFIDENCE; LOW on magnitude]. This is an INCREMENTAL-information claim, narrower than
"EV/EBITDA beats P/B outright" — a distinction §6 leans on.

**Gray & Vogel, "Analyzing Valuation Measures: A Performance Horse-Race over the Past 40
Years"** (working paper, ~2010, precursor to Gray & Carlisle's *Quantitative Value*, Wiley
2012) [LIT, MEDIUM CONFIDENCE on existence/authorship/thesis; LOW on any spread]. Finds
EBIT/EV beats simple P/E and P/B because it is capital-structure- and non-operating-item-
neutral. *Quantitative Value* pairs this multiple with a Piotroski/Altman-style quality overlay
— the real conclusion is "EBIT/EV plus a trap filter," not the multiple alone.

**Basu (1977, *Journal of Finance* 32(3)).** The original published value anomaly, ~15 years
before Fama-French HML [LIT, HIGH CONFIDENCE on author/venue/year/priority]. Low-P/E NYSE
quintiles beat high-P/E on a risk-adjusted basis, 1950s-60s sample [LIT, MEDIUM-HIGH
CONFIDENCE on direction; no decimal claimed]. A 1983 follow-up controls for size and the effect
survives [LIT, MEDIUM CONFIDENCE]. Longest unbroken pedigree of any measure here.

**Ball, Gerakos, Linnainmaa & Nikolaev — retained earnings vs. contributed capital.** Plausibly
"Earnings, Retained Earnings, and Book-to-Market in the Cross Section of Expected Returns"
(*JFE*, ~2018-2020) [LIT, MEDIUM CONFIDENCE on existence/authorship/mechanism; exact
title/year `[VERIFY]`]. Splits book equity into retained earnings (cumulative profit kept) and
contributed capital (issuance proceeds); shows B/M's predictive power loads almost entirely on
the retained-earnings component, little on contributed capital [LIT, MEDIUM CONFIDENCE
direction; LOW magnitude]. This is the WHY and the WHEN: P/B works when cheapness reflects
discounted retained profit; it should fail for issuance-dominated firms (recent IPOs, serial
diluters, heavily-financed capital-intensive names) — a conditioning variable this desk carries
in neither the US panel nor the India handoff design today.

**Israel-Laursen-Richardson (2020) / Arnott-Harvey-Kalesnik-Linnainmaa (2021).** Fully anchored
in dossier a §1 (−55% HML drawdown 2007-2020 [LIT, MEDIUM-HIGH CONFIDENCE]; competing
intangibles-vs-spread-widening reads) — not re-derived. Neither is a multi-measure horse race;
both test B/M alone across time, so their contribution here is purely the regime-dating anchor
for §3/§6, not a measure ranking.

**Penman & Reggiani — earnings yield vs. book yield, joint E/P-B/P sort.** Likely "Returns to
Buying Earnings and Book Value: Accounting for Growth and Risk" (Penman & Reggiani, *Review of
Accounting Studies*, ~2013) [LIT, MEDIUM CONFIDENCE on authors/title; `[VERIFY]` exact
year/journal]. Frames B/P as a proxy for how much future growth is priced in (low B/P = growth
heavily priced) and E/P as current profitability per price paid. Holding E/P fixed, higher B/P
predicts higher returns; holding B/P fixed, higher E/P predicts higher returns — neither
subsumes the other, and low-E/P-and-low-B/P (paying up on both) is the worst corner [LIT,
MEDIUM CONFIDENCE mechanism; LOW magnitude]. The clearest precedent for rank-averaging distinct
multiples rather than picking one (§3), and support for treating B/P as "the most differentiated"
classic multiple (echoed independently in §3).

**Novy-Marx, "the other side of value."** Fully treated in dossier b §2 — cross-referenced
only. Not a price-based multiple (no price in numerator or denominator), so it belongs to §3's
combination literature rather than this section's horse race among price multiples.

---

## 2. P/S specifically

**Where it sits today.** Once multi-measure composites became standard (§1, §3), P/S settled
mid-pack: rarely the outright best in careful tests, valued for construction cleanliness
(sales almost never negative or restated) more than raw edge. **This desk has no direct P/S
horse-race cell.** VAL-D6's own registration states why: true P/S is not constructible on the
US firm_panel (fields arrive pre-uniformized into ranks, so rank-of-ratio cannot be un-scrambled
into mcap/sales), so VAL-D6 excludes P/S from the US ladder and reassigns it to the India
design set [BOOKED VAL-D6 registration]. Nothing in this desk's own numbers today can place P/S
on the ladder — open, India-only (§6iii).

**The sector-composition problem — the worst of any measure here.** Margin structure varies far
more across industries than earnings- or book-multiple equivalents do: a retailer at 3-6%
margin and P/S 0.3x can be fully priced while a software firm at 30% margin and P/S 7x is
genuinely cheap on the same raw ratio — the multiple says nothing about margin (dossier a §1's
stated weakness). A universe-wide raw P/S sort is more than any other measure here a disguised
sector bet, echoing dossier a §3/c §4's within-industry point with more force.

**Margin-adjusted P/S — algebra, not new information.** `P/E = P/S ÷ (Net Income/Sales)` when
using the same period's figures, so margin-adjusting with the CONTEMPORANEOUS margin is
identical to P/E. The useful variant normalizes to a mid-cycle margin — the firm-level analogue
of CAPE's earnings-smoothing (dossier a §1) — damping margin-cycle noise for
cyclical/commodity names, not adding orthogonal cross-sectional information beyond a
well-built earnings multiple.

**The honest verdict on adding P/S to an EV/FCF composite.** Because of the margin identity,
P/S's marginal value in a composite already holding an earnings/cash-flow leg is mostly
COVERAGE — it stays computable for firms with temporarily negative EBIT/FCF, where an
EV/EBIT or FCF-yield leg goes undefined — not incremental alpha. Consistent with the panel that
IS available: VAL-D1's Fcf_Yld is the weakest flow measure at nearly every horizon
(+0.59/−0.44/+1.47 vs. Pb's +16.08/+14.58/+8.37) [BOOKED VAL-D1] — a margin-cleaned sibling
measure should be expected to add robustness, not standalone alpha.

---

## 3. Combination methodology

**Rank-average vs. z-score vs. intersection.** Rank-averaging (percentile each measure, then
average) is the outlier-robust standard (O'Shaughnessy's Value Composite, AQR-style
composites) [LIT, LOW-MEDIUM CONFIDENCE, no replicated magnitude]: a P/E-3 and a P/E-300 name
both just get extreme percentiles. Z-scoring preserves more mid-distribution information but is
exposed to fat tails — a near-zero-earnings P/E z-score can dominate an average even after
naive winsorization, exactly the class of hazard this desk's 2026-09-05 ULTRACODE AUDIT flagged
generally (booked in `quant/stats/preprocess.py` per CLAUDE.md). Intersection portfolios (cheap
on every measure at once) concentrate into a small, correlated, distress-tilted tail — noisier,
higher-turnover, no larger measured premium in the practitioner literature [LIT, LOW
CONFIDENCE]. The desk's own VAL-D2/D3 print is a direct, if unintended, illustration of the
danger: conditioning further within the cheap bucket (low vol, high ROE, low debt) made every
trap filter print NEGATIVE, because on this no-delisting panel the deepest-distress corner is
exactly where the survivor bounce concentrates [BOOKED VAL-D2+VAL-D3 RESULT] — narrowing
further on this construction would compound, not diversify, a known artifact.

**How many measures before redundancy.** Flow-based multiples (E/P, CF/P, EV/EBIT, FCF/P) tend
to correlate strongly with each other, since they share related numerators updated every
reporting period; B/P, a slowly-updating balance-sheet stock, correlates less with any of them
[LIT, LOW-MEDIUM CONFIDENCE, standard factor-construction observation]. This collapses "pure
value" diversification to roughly two components — one flow-yield, one book — so a composite
needs about one flow measure plus B/P (plus a price-only payout measure, per dossier a/b) to
capture most of what is achievable; a fourth or fifth correlated flow multiple mostly re-derives
dossier b §4's "fake diversification" critique. The desk's own panel confirms this ceiling is
reached almost immediately: VAL-D1's v7 composite (Pb+Ev_Ebitda+Fcf_Yld) TIES Pb alone — +8.97
vs. +8.80 at szQ5 12m [BOOKED VAL-D1] — two additional flow legs atop one strong book leg bought
almost nothing.

**Regime dependence — hedged, no decade-specific number claimed.** Dividend yield/simple
earnings multiples dominate the mid-century literature (Basu's own sample); B/M rises with
Fama-French; the dot-com era splits P/S and growth-priced measures sharply from earnings/book
multiples before the 2000-02 reversal; the commodity supercycle (~2003-08) favors cash-flow/
EBITDA multiples in cyclicals; 2007-2020 is AHKL/ILR's B/M-drawdown window, echoed in dossier
c's India read (value +0.8%/yr, Sharpe −0.39, 2015-19 [BOOKED V1]) [LIT-lore, LOW CONFIDENCE
throughout]. The actionable consequence: no single measure's historical dominance should be
assumed stable, exactly why VAL-D1 pre-registered a full six-measure ladder rather than betting
on one prior decade's favorite.

**Post-hoc measure selection — the desk's own antidote, as context.** McLean & Pontiff
(~26%/~58% decay [LIT, CONTRACT's own governing citation]) and Hou-Xue-Zhang's ~two-thirds
anomaly-failure rate [LIT, MEDIUM CONFIDENCE, already booked via dossier a §2] make a composite
built by backtesting many candidates and keeping the best subset exactly the trap CONTRACT §9's
deflated-Sharpe/true-trial-count standard prices. This desk's discipline is the antidote in
practice: VAL-D1's six measures and the v7 composite's three legs were named at registration,
before any cell was computed [BOOKED VAL-D1 registration] — not chosen after seeing which
performed best.

---

## 4. Horizon structure

Two senses of "horizon" should not be conflated: how a return spread behaves as the forward
window lengthens, vs. how often a measure's rank churns (turnover, which governs cost).

**Return-spread decay by horizon — the desk's print.** VAL-D1 (cheap-minus-expensive ann.,
1m/12m/36m): Pb +16.08/+14.58/+8.37 (strongest everywhere, but roughly halving proportionally);
Pe +4.12/+3.53/+2.70 (gentler ~35% falloff despite a smaller absolute level); Ev_Ebitda
+3.13/+3.24/+1.80 (flat then mild decay); Fcf_Yld +0.59/−0.44/+1.47 (non-monotone); Div_Yld
−4.09/−4.55/+0.42 (a sign flip — the payout confound resolving over years) [BOOKED VAL-D1]. The
classical "P/B is the slow, long-horizon measure" claim is usually about rank TURNOVER, not
which measure's spread is largest at the longest horizon — on this panel Pb's edge is in fact
front-loaded even though it stays largest throughout; the two senses of "slow" should not be
run together.

**Turnover per measure and the cost implication.** P/B changes rank slowly — book value updates
quarterly (US) or semi-annually (India, dossier a §6) — so rank moves mostly with price alone
between reports: low churn, low turnover [LIT, MEDIUM CONFIDENCE]. P/E turns over faster —
EPS can jump on surprises/one-offs, moving rank without any price change [LIT, MEDIUM
CONFIDENCE]. EV/EBITDA is India's worst-behaved multiple specifically because it mixes cadences
within one ratio (quarterly EBITDA, semi-annual net debt — dossier a §6, not re-derived). Under
CONTRACT §3's turnover caps (200% one-way, moderate book), this is a direct cost lever: a
P/E- or EV/EBITDA-led composite burns the same turnover budget faster per unit of holding-period
alpha than a P/B-anchored one, reinforcing Known Prior #10 (value/quality run ~5× momentum's
half-life) and dossier a's existing book-multiple-majority weighting.

---

## 5. Small vs. large

Value-overall's size-habitat question is dossier b §4's ground (AFIMP 2018's junk-tilt
critique) — not repeated. Specific to measures: the classical small-value corner is built on
B/P and is exactly the cell AFIMP's critique targets — the raw small-cap B/P premium is the
most junk-contaminated [LIT, MEDIUM CONFIDENCE]. Gray & Vogel/Carlisle's EBIT/EV is sometimes
argued to travel better into large, complex-capital-structure names, since capital-structure
neutrality matters more there [LIT, LOW CONFIDENCE, no magnitude].

**The desk's own evidence is the strongest anchor.** VAL-D1's szQ5 column is flagged "the
honest weight" / "the implementable column" in its own registration [BOOKED VAL-D1]; there Pb
still leads (+8.80) but shrinks materially from the panel-wide figure (14.58 → 8.80) — a
real, own-panel instance of the AFIMP junk-discount mechanism, though VAL-D1 was not designed
as a small-vs-large study. Div_Yld's sign FLIPS between panel (−4.55) and large-cap (+5.10)
[BOOKED VAL-D1] — large-cap is where the payout confound resolves into a clean discipline
signal. **VAL-D6 tests this directly and has not printed.** Pre-registered with explicit small
(szQ1-2)/large (szQ4-5) halves, a full pure-measure ladder each, and three mixes (CQ=Pb+Roe,
VM=Pb+Mom_11M, VLV=Pb+lowVol) [BOOKED VAL-D6 registration]. Its own prior — mixes beat pure Pb
in large caps at 12m/36m — draws on already-booked factor-level precedent (VAL-D4's HML+UMD
Sharpe 0.70 vs. 0.32 alone; QG-D2's HML+RMW 0.49 vs. 0.32/0.41 [BOOKED VAL-D4, QG-D2]), but
remains a stated prior, not a result.

---

## 6. Close

### (i) Ranked table

| Measure | Best-evidence verdict | Horizon behavior | Size habitat | One-line caveat |
|---|---|---|---|---|
| **P/B** | Strongest on this panel; contested in the wider literature (intangibles debate) | Largest edge everywhere; largest proportional decay | Wins panel-wide AND large-cap; edge shrinks in the latter | Rides the no-delisting junk bounce (VAL-D2/D3); BGLN predicts WHEN it fails (issuance-dominated firms), untested here |
| **P/E** | Longest pedigree (Basu 1977); modest, proportionally stickier spread | Gentlest proportional decay of the six | Untested by size here | Denominator noise from lumpy quarters |
| **EV/EBITDA** | Loughran-Wellman's incremental claim held in their own test; MISSED as "beats P/B" here | Flat 1m→12m, mild 36m decay | Untested by size here | Worst cadence-mixing hazard in India |
| **FCF yield** | Weakest, noisiest flow measure; thin academic base | Non-monotone | Untested by size here | Not a standardized line item — construction degrees of freedom |
| **Dividend yield** | Panel-negative, large-cap POSITIVE — a real split | Sign flips 1m/12m vs. 36m | Best large-cap after Pb (+5.10) | QG-D1 payout-state confound |
| **Buyback yield** | Weakest tested; BMRR's total-payout logic unconfirmed here | Negative/flat throughout | Untested by size here | India's buyback instrument is young, tax regime unstable |
| **Composite (Pb+Ev_Ebitda+Fcf_Yld)** | Ties Pb, doesn't beat it | Tracks Pb's decay shape | Marginally best szQ5 (+8.97), not materially | Redundancy ceiling reached almost immediately |
| **P/S** | No desk print — excluded from the US panel by construction | Unknown | India-only, untested | Largest sector-composition problem; margin-adjustment collapses toward P/E |
| **Ebit/Bv** | Flagged a value-quality hybrid, not a pure measure | Not yet printed | Not yet printed | Wins, if it does, by smuggling in profitability |

### (ii) Reconciling the literature with the desk's own ladder

Two headline priors MISSED: FCF yield as recent-decade winner [LIT, LOW CONFIDENCE] and
EV/EBITDA ≥ P/B per Loughran-Wellman [LIT] — VAL-D1's own grade line says so plainly [BOOKED
VAL-D1]. Not a refutation of the cited paper: Loughran-Wellman's claim is INCREMENTAL
information from a joint regression controlling for B/M/size/momentum (§1), narrower than
"EV/EBITDA's univariate spread exceeds B/M's," which is what VAL-D1 actually tested — a
construction mismatch, not a clean contradiction, and a distinction worth carrying into any
India re-test.

P/B's outright win is sharper. VAL-D1's own registration stated the two-sided prior: "if Pb
wins outright the intangibles-era decay story is overstated on this panel" [BOOKED VAL-D1] —
and Pb won outright, at every horizon and in large-cap. But VAL-D2/D3, booked the same day,
supplies the necessary caveat: "within the cheap bucket of an EW panel with NO deaths, the
deep-distress corner mechanically outperforms — its casualties were deleted" [BOOKED
VAL-D2+VAL-D3 RESULT]. Pb's win is partly a survivorship artifact of this construction, not
necessarily a clean verdict on a debate fought on longer, delisting-inclusive, multi-country
samples. Pb still winning in large-cap is some real pushback on the intangibles story as a
universal claim — but the panel's own EW-survivor limitation is the dominant caveat on every
reconciliation here and should travel into the India re-test rather than being resolved by
assertion.

The Div_Yld split (panel −4.55, large-cap +5.10 [BOOKED VAL-D1]) is the cleanest reconciliation:
the PREDICTED consequence of combining two already-booked mechanisms — QG-D1's payout-state
confound (high payout co-occurs with depressed earnings 78% of the time [BOOKED QG-D1]) and
Boudoukh-Michaely-Richardson-Roberts' argument that payout signals are cleaner where payout
reflects genuine capital-return discipline rather than earnings-collapse noise (dossier a §1).
Small caps have more volatile earnings and are likelier to show a payout spike concurrent with
a collapse; large, established payers are less likely to. No single paper states this exact
split, but it falls directly out of two mechanisms already booked before VAL-D1 ran.

VAL-D2/D3's negative trap-filter prints reconcile with BGLN's retained-earnings mechanism in a
way not previously drawn out in this desk's files: on a no-delisting panel, the cheapest B/P
bucket disproportionately holds firms whose book value reflects retained LOSSES rather than
retained EARNINGS — exactly the population BGLN would flag as carrying the least genuine B/M
signal, yet whose survivor bounce is never punished. The trap filters may be systematically
removing the very names generating the artifact, which is why VAL-D2/D3 moves the within-cheap
question to the India PIT panel rather than treating today's negative prints as settled.

VAL-D6's Ebit_Bv flag reconciles with Gray & Vogel/Greenblatt (§1) and Penman-Reggiani (§1):
EBIT/book mixes an earnings-flow numerator with a book-value denominator, structurally closer
to a return-on-capital measure than a valuation ratio — exactly the caution VAL-D6 states
before any number prints. VAL-D6's central question (do mixes beat pure Pb in large caps) has a
strong prior from this desk's own factor work (VAL-D4's HML+UMD Sharpe 0.70 vs. 0.32 [BOOKED
VAL-D4]) — but VAL-D6 has not printed, and this dossier does not pre-empt it.

### (iii) The India P/S design note

Unlike the US firm_panel, India's incoming handoff makes true PIT P/S directly constructible:
P1 carries `revenue` and `shares_outstanding` as filed, each attached to a `filing_date`, and
P4 carries daily `close_adjusted` — so `P/S(t) = close_adjusted(t) / (revenue_ttm as of the
last known filing / shares_outstanding as of that filing)` is buildable with a proper lag,
exactly the PIT discipline CONTRACT §2 and this desk's survivorship doctrine (P3) require. This
is the reverse of VAL-D6's US-panel finding (rank-uniformization made P/S unconstructible) and
directly answers the gap that entry flagged. Two dependencies carry over rather than resolve
here: a margin-adjusted India P/S (§2) needs a normalized peer margin, which needs the
sector-classification tag dossier c §6 already names as a genuine gap (no field exists in P1-P6
today) — raw India P/S can be built on arrival, a margin-adjusted or within-industry version
waits on that same queued ask. Given §2's algebraic point and dossier a §6's finding that E/P
and sales/P are already the two cleanest, quarterly-native India multiples, the honest
expectation is that P/S's marginal India contribution mirrors §2's US-inferred verdict:
coverage and construction robustness (staying rankable for negative-EBIT/FCF names, common in
India's early-scaling and cyclical-trough population) rather than independent alpha — a prior
to test once a VAL-D6 India extension is registered, not a result to claim now.

---

## Data requirements — India (incremental to dossier c §6's list)

1. **P1's `revenue` + `shares_outstanding` + P4's `close_adjusted`** — already sufficient for
   raw PIT P/S; no new field needed.
2. **A sector/industry classification per company** — dossier c §6's existing gap, restated as
   the specific blocker for a margin-ADJUSTED India P/S.
3. **A book-value decomposition (retained earnings vs. contributed/paid-in capital)** — not in
   P1 as specified (`total_equity` arrives aggregated); needed to operationalize BGLN's
   conditioning variable (§1) flagging when a raw India P/B sort should carry little signal. A
   new ask, not urgent relative to dossier c's five ranked designs.
