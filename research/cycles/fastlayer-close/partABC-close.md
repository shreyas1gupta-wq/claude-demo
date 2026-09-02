# The Fast-Layer Closer — Parts A, B, C & G, Argued in Full

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-02

Parts A, G, B & C · Atlas entries **5.4** (1-month cross-sectional reversal, `docs/CYCLE_ATLAS.md`
line 144: "Liquidity-provision premium (Cheng et al.) — real, but the most cost-fragile anomaly
known + 20bp STT round trip; zero India magnitude studies"; harvest **Tier-C flag only, ZERO return
budget → L1**), **5.5** (weekly/daily seasonals, line 145: "No surviving mechanism after costs at
our scale"; harvest **REJECT**), and **5.6** (intraday cycles, line 146: "Real microstructure, but
this is an EOD-data, weekly-cadence program by design"; harvest **Out of scope**). This chapter is
the fast layer's theory-and-evidence half; its companion,
`research/cycles/fastlayer-close/partDH-close.md`, already on record, is the routing table, the
algorithm note, the harvest, and the knowledge ledger (Parts D, E, F, H). Between the two documents
the full A-through-H lettering is filled for this entry, matching this program's other closing
monographs; this chapter never re-derives what the principal's own document has already settled.

**What this chapter is for.** `research/register/trial-ledger.md`'s Design MR1 block is explicit:
this is a **registered design, not a run trial** — "(awaits bhavcopy vault)" is its own status line,
and no desk number exists for 5.4, 5.5, or 5.6 as of this writing. Every figure below is a literature
number, an India institutional fact, or a public-record case, each carrying its own author-year or
verification tag; nothing here is computed on this program's own data. The through-line the
principal set is the honest one: **the last band is where speed premia live, and this desk's edge is
knowing exactly which speed games it cannot win.** Part A builds the theory and the math behind each
of the three verdicts; Part G turns to the operator rather than the market — why the fastest
patterns seduce a research desk, and what discipline refuses that seduction; Part B tests the theory
against the public record, cross-country and in India at double length as the task requires; Part C
specifies what MR1 needs when bhavcopy lands, and what stays deliberately unbuilt until it does.

---

## Part A — Theory, with the math

### A.1 Short-term reversal, formalized

**Jegadeesh (1990)**, "Evidence of Predictable Behavior of Security Returns," *Journal of Finance*
45(3): 881–898, sorts NYSE/AMEX stocks into deciles on trailing one-month return and finds strongly
**negative first-order serial correlation in monthly returns** — the loser-minus-winner decile
spread over 1934–1987 is **2.49%/month** [Verified via search] — even as the same securities show
strong *positive* serial correlation at twelve months, the opposite-signed structure this program's
momentum dossier already documents on the long side (`research/dossiers/01-momentum-reversal.md` §1
items 1–9; cross-referenced) and which atlas §11.1's "mean-reversion horizon sandwich" frames as one
phenomenon read at different horizons. **Lehmann (1990)**, "Fads, Martingales, and Market
Efficiency," *Quarterly Journal of Economics* 105(1): 1–28, works at weekly resolution and finds
weekly winners reverse the **following week**, with implied arbitrage profits **persisting after
bid-ask spread and plausible transaction-cost corrections** [Verified via search] — the first paper
to state what decades of cost-stack literature would spend itself re-litigating: a raw reversal
signal clears a first-pass cost test, and everything interesting happens in the gap between
"plausible" costs and the actual stack a real book faces (§A.3).

Formally, the object is negative own-autocorrelation in the cross-section: for stock $i$,
$\mathrm{Cov}(r_{i,t}, r_{i,t+1}) < 0$ at one week to one month, flipping sign through the momentum
band (three to twelve months) and again beyond two to five years (long-horizon reversal, atlas §11.1
routes to value, H64). A decile long-short's expected return is this covariance scaled by
ranking-period dispersion — which is why the anomaly's *raw* magnitude rises mechanically with
cross-sectional volatility, a structural fact that matters directly for §A.2's VIX result, since vol
dispersion and VIX co-move.

### A.2 The liquidity-provision interpretation, formalized

The mechanism question has a well-identified answer, and it is the strongest form of Contract §5's
category (iii): a genuine risk premium someone must be paid to bear. **Campbell, Grossman & Wang
(1993)**, "Trading Volume and Serial Correlation in Stock Returns," *Quarterly Journal of Economics*
108(4): 905–939, supply the founding equilibrium logic: risk-averse market makers absorb
liquidity-motivated order flow, and the expected return compensating that inventory risk is exactly
the negative autocorrelation observed; the paper's own signature is that **first-order daily
autocorrelation declines with volume** [Verified via search] — a high-volume down-move is more
likely liquidity-driven (reversal-prone) than a low-volume one, which more likely carries information
(and persists). This is the volume-conditioning ancestor of this program's own volume-momentum
feature test (`research/dossiers/01-momentum-reversal.md` item 18, Maheshwari-Dhankar 2017b).

**Nagel (2012)**, "Evaporating Liquidity," *Review of Financial Studies* 25(7): 2005–2039, makes the
mechanism dynamic: reversal returns proxy the compensation to liquidity provision, and that
compensation is **highly predictable from the level of the VIX** [Verified via search], because when
capital-constrained intermediaries retreat, the price of absorbing someone else's selling pressure
rises, and expected reversal returns (and conditional Sharpe ratios) **spike** in exactly those
episodes [Verified via search]. Stated as a regression,

$$R_t^{rev} = \alpha + \beta \cdot \mathrm{VIX}_{t-1} + \varepsilon_t, \quad \beta > 0,$$

with the strategy's conditional Sharpe near-monotone in lagged VIX — the mechanism Part B.2 tests
against 2008 and 2020. Nagel's VIX channel and Cheng, Hameed, Subrahmanyam & Titman (2017)'s
companion finding — reversal profits rise where institutional competition for the liquidity-provision
role is scarce (already verified in full, `research/dossiers/01-momentum-reversal.md` item 22,
cross-referenced) — are two proxies for one state: the price of immediacy. That price is exactly what
atlas 5.4 names as the thing a weekly-cadence desk cannot collect: harvesting it means *being* the
immediacy provider, at daily speed, in falling names, which Contract §1's EOD-data, weekly-preferred
mandate forecloses before a number is computed.

### A.3 The cost knife

**Avramov, Chordia & Goyal (2006)**, "Liquidity and Autocorrelations in Individual Stock Returns,"
*Journal of Finance* 61(5): 2365–2394, puts mechanism and cost in direct tension: reversal is
strongly related to illiquidity, and the **largest reversals — and largest potential contrarian
profits — occur precisely in the highest-turnover, lowest-liquidity names** [Verified via search];
yet the implied profits are **smaller than the likely transaction costs** of trading those same names
[Verified via search]. This is close to a structural impossibility result: the premium's size and its
harvesting cost are increasing functions of the *same* variable (illiquidity), so hunting further into
the tail raises the cost at the same rate it raises the raw spread.

**Novy-Marx & Velikov (2016)**, "A Taxonomy of Anomalies and Their Trading Costs," *Review of
Financial Studies* 29(1): 104–147, turns this into a hard empirical line: **most anomalies under
roughly 50% monthly one-way turnover generate significant net-of-cost spreads once cost-mitigated
(a stricter-entry-than-exit buy/hold spread is the single most effective technique); few above that
line do** [Verified via search]. Short-term reversal sits on the wrong side of this line by
construction: a monthly full-decile reformation implies one-way turnover on the order of 100%+ per
*month*, since a name in this month's loser decile is, almost by the anomaly's own definition, unlikely
to occupy it again next month. [VERIFY: the taxonomy's own reported turnover percentile specifically
for short-term reversal — this chapter states the mechanical consequence of monthly reformation
rather than a table figure not directly confirmed this pass.] Qualitatively the literature agrees:
short-term reversal is the highest-turnover anomaly commonly studied, sitting structurally on the side
of Novy-Marx-Velikov's own cutoff where net spreads are rarely significant.

India's cost stack sharpens this knife. `config/costs.yaml` (D05, re-verified FY2026-27) prices the
cash-delivery round trip at **[24, 32] bps all-in**: 10 bps STT on *each* leg (20 bps round trip
alone, `stt_buy: 0.0010, stt_sell: 0.0010`), stamp duty, exchange/SEBI turnover fees, GST on fees —
before market impact or brokerage. The STT leg has no US analogue whatsoever: Avramov-Chordia-Goyal
and Novy-Marx-Velikov price commissions, spread, and impact, never a transaction tax that cannot be
engineered away by any execution improvement. A book reforming its full deck monthly at 100%+
one-way turnover compounds to well over 1,000% one-way per year — illustratively, not as a desk
estimate, on the order of ten to twelve full reformations — at which point the STT leg alone (20 bps
× ~10–12 round trips) consumes on the order of **2.0–2.4% of NAV/yr** before impact is even modeled,
against a gross spread whose academic magnitude (Jegadeesh's 2.49%/month, itself pre-cost and
India-less) is not preserved once diluted by a year of that drag. This is atlas 5.4's "most
cost-fragile anomaly known" made arithmetic, and why the entry carries a *zero* budget rather than a
haircut: a haircut presumes a residual worth sizing.

### A.4 Day-of-week and weekend effects: the archetype of the mined calendar pattern

Where reversal fails on cost, the weekly/daily seasonal family (5.5) fails more fundamentally: no
mechanism ever survived to be cost-tested. **French (1980)**, "Stock Returns and the Weekend
Effect," *Journal of Financial Economics* 8(1): 55–69, found **significantly negative average Monday
returns** in every five-year subperiod of the 1953–1977 S&P sample, against positive averages the
other four weekdays [Verified via search] — rejecting both the calendar-time null (Monday should be
triple an ordinary day) and the trading-time null (weekdays should be equal). **Gibbons & Hess
(1981)**, "Day of the Week Effects and Asset Returns," *Journal of Business* 54(4): 579–596,
independently confirmed negative Mondays across the thirty Dow stocks with a companion methodology
[Verified via search] — cross-confirmation across two samples and methods that, in 1981, looked like
genuine discovery.

What happened next is the instructive part. **Sullivan, Timmermann & White (2001)**, "Dangers of
Data Mining: The Case of Calendar Effects in Stock Returns," *Journal of Econometrics* 105(1):
249–286, constructs the **full universe of 9,452 competing calendar rules** a century of daily data
would let an unprincipled researcher try, and applies the **stationary block bootstrap of Politis &
Romano (1994)** to the joint distribution of performance across all of them, yielding a
data-mining-adjusted p-value for whichever rule performs best [Verified via search]. Individual rules
— the weekend effect prominently — appear significant in isolation, exactly as French and
Gibbons-Hess found; but within the full universe that significance **largely disappears**, and even
the single best-performing rule of 9,452 **fails to beat buy-and-hold** once adjusted [Verified via
search]. The logic: if a researcher is implicitly free to have tried thousands of rules and report
only the winner, the correct null is the *maximum* over all candidate statistics under no true
effect — not any one statistic's marginal distribution — and under that correction the calendar
literature's significance is revealed as largely a multiple-testing artifact. This is the formal
content behind this program's own CW3/GS1 house discipline (§C.3): a twelve-month Kruskal-Wallis
omnibus, run twice on vaulted data, each pre-declaring that even a nominally significant print would
not overturn the reject — a twelve-way comparison expects ~0.6 false positives at 5% by chance, and
no mechanism has ever been proposed for a day-of-week or expiry-day pattern surviving the same
full-universe correction French's and Gibbons-Hess's single-rule tests never applied.

### A.5 The intraday U-shape: real microstructure, deliberately out of scope

The third entry (5.6) is the one requiring the most care, because the underlying phenomenon is
neither cost-fragile like 5.4 nor mechanism-free like 5.5 — it is real, mechanism-backed, and
extensively replicated — and the correct verdict is still to leave it alone, for a programmatic
rather than evidentiary reason. **Wood, McInish & Ord (1985)**, "An Investigation of Transactions
Data for NYSE Stocks," *Journal of Finance* 40(3): 723–739, documents that **return variability
across the trading day traces a crude U-shape** — high at the open, falling through the middle,
rising into the close [Verified via search]. **Admati & Pfleiderer (1988)**, "A Theory of Intraday
Patterns: Volume and Price Variability," *Review of Financial Studies* 1(1): 3–40, supplies the
equilibrium mechanism: discretionary liquidity traders and informed traders both prefer to
concentrate their activity in the same high-volume windows — liquidity traders because impact per
unit is lower when many others trade too, informed traders because their own flow is best camouflaged
inside a busy tape — producing **endogenously concentrated trading and price variability at the open
and close** [Verified via search]. This is a genuine strategic equilibrium, not a data-mined
curiosity: no microstructure theorist treats the U-shape as an artifact, and unlike reversal,
harvesting it does not require out-competing professional liquidity providers on their own turf — it
largely *describes* how those providers already behave.

The out-of-scope verdict therefore rests on neither of the arguments that dispose of 5.4 or 5.5. It
rests on Contract §1's architecture: this is an EOD-data, weekly-cadence program by design — inputs
(bhavcopy), signal construction (percentile ranks, weekly-to-monthly cadences per §10), and
evidentiary apparatus (embargo widths scaled to monthly-and-above half-lives per §9) are built for a
decision frequency measured in weeks. The desk **neither measures nor trades** intraday structure —
not because the U-shape's alpha is rejected on the merits, but because the question sits one layer
beneath where this desk's signals live. Its economic content is fully absorbed where a portfolio
decision is *translated into orders*: an execution algorithm pacing participation against intraday
volume (`config/costs.yaml`'s `participation_cap_per_day: [0.05, 0.10]`, Korajczyk-Sadka convention,
already registered) already inherits the Admati-Pfleiderer consequence — trading more where volume,
liquidity, and camouflage are naturally highest — without this desk ever measuring or trading the
U-shape as a signal in its own right. This is the scope boundary stated precisely, so silence is
never mistaken for ignorance.

---

## Part G — Operator psychology: the seduction of speed

Part A explains why the fast layer's three verdicts are what they are. This part explains why a
competent research team, in good faith, is structurally at risk of getting them backwards — of
promoting 5.4 past its zero budget, quietly re-testing 5.5 with tweaked parameters, or drifting into
building 5.6 machinery nobody asked for. The risk is not carelessness; it is a predictable pull built
into the statistics of fast signals, and naming it precisely is this program's actual defense —
Contract §8's Traps exist to guard against a failure mode individual diligence does not reliably
catch in the moment.

**The fastest patterns look most tradable because they produce the most backtest observations.**
Nearly an identity: a one-month-half-life signal yields roughly twelve observations per year of
history; a one-week signal roughly fifty; an intraday signal thousands. Holding true effect size
constant, $t \approx \sqrt{n} \cdot$ (effect / noise), so a fast signal tested over the same span
carries an order of magnitude more nominal power than a slow one, before any question of whether the
effect is real at that resolution or survives costs. This program's own CR2 and CW1 trials
demonstrate the mirror image (`research/register/trial-ledger.md`): CR2 found the named "mid-2025
quant unwind" invisible at monthly WML granularity — not because nothing happened, but because
monthly resolution is the wrong instrument for a days-scale event; CW1 found Budget-month volatility
ordinary at monthly resolution for the same reason. The fast layer's temptation runs the other way: a
phenomenon real but small and cost-fragile at its true resolution will, tested at that fine
resolution with enough history, produce statistics that *look* more dramatic than a slower, larger,
more robust signal over the same span — purely from accumulated degrees of freedom, not from being a
better bet. Contract §9's purged, embargoed cross-validation and §5's written survival-argument
requirement exist as structural countermeasures to an illusion that operates on the statistics
themselves, not on judgment.

**"We could day-trade this" is the last refuge of a desk out of ideas.** A desk whose slower signals
(credit cycle, value spread, momentum) are each argued to Tier-B-or-better and haircut per §5 has, by
that point, run out of comfortable places to look — every slow lever already pulled as far as its
evidence supports. The fast layer is where an evidence-exhausted effort goes next, not because its
evidence is better, but because a plausible mechanism story can still be told about *something*, and
the observation-count effect above makes that something look statistically confident. The tell is
usually linguistic: an argument beginning from *resolution* ("we could trade this daily") rather than
*mechanism* ("here is why this premium persists being known") has already inverted §5's own
discipline before a number is computed. Atlas §7 already checked this exact temptation once, for
options rather than reversal ("Options-premium harvesting cycles ... no argument we beat professional
vol desks at their own book," D12) — the fast layer generalizes a lesson this program already
learned in an adjacent domain.

**Out-of-scope versus reject: silence is not ignorance.** Atlas 5.6 states this in one sentence: "no
evidence claim is made either way." A **reject** (5.5) is a claim that the evidence and mechanism
were examined and neither survives; it can, per Contract §9, be reopened with a *new* mechanism
argument (never a rerun with tweaked parameters). An **out-of-scope** verdict (5.6) makes no claim on
the merits at all — it is a boundary statement about what this architecture is built to do, and
confusing it with a reject risks a future researcher, encountering genuinely new intraday evidence,
wrongly believing the question was already litigated and never bringing it forward; confusing a
reject with mere scope risks the opposite error, assuming daily-resolution machinery would make
day-of-week seasonality tradable, when the mechanism-free verdict has nothing to do with resolution.
The fix, as elsewhere in this program, is to write the reasoning down at the time the verdict is
reached, so a future researcher inherits the argument, not merely the label.

**Knowing which counterparty you would be.** The sharpest check: who is on the other side, and is
this desk better positioned than they are? For 1-month reversal, the counterparty is uncomfortable
and specific — the professional market-making firms inside NSE's own colocation facility (§B.8),
whose business exists to minimize exactly the latency and inventory-holding costs a weekly-cadence,
EOD-data desk cannot avoid. Nagel's (2012) own VIX-conditioning sharpens the asymmetry: the premium is
largest exactly when capital is scarcest and a book would need to react fastest — the one capability
this architecture structurally lacks. For a monthly-to-quarterly value or credit-cycle rebalance, the
honest answer is closer to *against no one in particular* — a view on multi-quarter fundamentals
against diffuse long-horizon holders, none with a structural speed advantage. This one question is a
faster, more reliable check against the fast layer's seduction than additional backtesting, because
it cannot be gamed by resolution or observation count the way a Sharpe ratio can.

---

## Part B — Cross-country evidence and the India cases

### B.1 US reversal profitability decay as HFT market-making capacity grew

Frazzini, Israel & Moskowitz, using roughly a trillion dollars of live institutional trading data
across nineteen developed markets 1998–2011, find **short-term reversal the single most
trading-cost-constrained anomaly** of the group they study (already verified in full, `research/
dossiers/01-momentum-reversal.md` item 24, cross-referenced) — significant here for what it implies
about the arc, not the level. That window is precisely when algorithmic and HFT market-making
capacity in US equities grew from marginal to dominant; NSE's own colocation facility (§B.8) imported
this infrastructure model into India starting in 2009, near the sample's midpoint. The implication
follows directly from Campbell-Grossman-Wang (1993) and Nagel (2012): as low-latency capital enters
market-making at scale, the compensation required to supply liquidity falls, and the reversal premium
— exactly that compensation — should compress. An anomaly only "plausibly" cost-robust in Lehmann's
1990 telling is, by the time Frazzini-Israel-Moskowitz study it with 2000s–2010s data, the *most*
cost-constrained in their cross-section — not because the mechanism vanished, but because the
population able to supply the same service cheaper grew enormously over exactly this period.

### B.2 Nagel's VIX-conditional spikes: 2008 and 2020 as the mechanism's own stress tests

The cleanest out-of-sample tests of Nagel's mechanism, relative to his original sample, are the two
most severe systemic liquidity-constraint episodes since: 2008 and March 2020. This program's own
vaulted-data work corroborates the underlying state variable on adjacent signals: **FS-U1/FS-U2**
(`trial-ledger.md`) demonstrate volatility clustering — the VIX-adjacent state Nagel conditions on —
as Tier-A and cross-asset-replicated even after monthly aggregation; **M4**, this program's own
crash-guard validation, finds the guard-ON regime at **−2.19%/month (n=95)** against **+1.81%/month
OFF (n=1069)** — the same "danger concentrates in the stress state" signature Nagel's conditioning
predicts, for an adjacent signal (momentum crashes rather than reversal spikes). [VERIFY: a
dedicated, India-specific reversal-return-vs-India-VIX estimate for 2008/2020 specifically — none was
located this pass; this chapter states the global mechanism and this program's own analogous evidence
as priors, not an India magnitude, consistent with atlas 5.4's own "zero India magnitude studies"
line.] The honest reading: even where the mechanism is confirmed at its most extreme, the episodes
where the premium is largest are the episodes where a weekly-cadence desk is least equipped to react
fast enough to collect it.

### B.3 The weekend effect's published-then-vanished arc

Part A.4 already gives the mechanics; this is the arc as one case, because its shape — discovery,
decade of replication, evaporation under a corrected test — is the archetype invoked whenever a fast,
mechanism-free calendar pattern is proposed. French (1980) and Gibbons-Hess (1981) independently
confirmed the same pattern within a year, the strongest confirmation an anomaly can receive absent a
corrected multiple-testing framework. Sullivan-Timmermann-White (2001) then showed, with a century of
data and the full universe of comparable rules, that the apparent confirmation was largely an
artifact of not correcting for how many rules the profession had implicitly searched. No mechanism
proposed for it — settlement-cycle timing, Friday/Monday news-reporting asymmetry, short-seller
unwinds — survived that correction. This is why atlas §7 treats month-of-year/day-of-week seasonals
as "the canonical data-mining trap" rather than an anomaly this program merely lacks data to test: the
data exists in abundance, has been tested exhaustively, and the honest reading is a rejection this
program inherits rather than re-derives.

### B.4 India case one — the 2009 upper-circuit day, argued as a reversal caricature

On **18 May 2009**, following the UPA's return with a much larger, Left-independent mandate, the
Sensex and Nifty hit their **first-ever upper circuit** within roughly thirty seconds of the open,
freezing trading for about an hour; on reopening the market ran into a **20% upper-circuit band** and
trading was **suspended for the remainder of the day**, closing up roughly **17.3%** (Sensex
+2,110.79 points to 14,284.21) [Verified via search; also on record in `research/cycles/
political-close/partABC-fold-rejects.md` §A.1, cross-referenced, not re-verified independently].
Read as a reversal caricature: a naive reversal trader, long the names that had fallen hardest into
the pre-election window, would have been rewarded spectacularly — the move **did mean-revert**, in
the most extreme form this market's history records. But the mechanism has nothing to do with Part
A.2's liquidity-provision story: no market maker was compensated for absorbing unwanted selling
pressure; the move was political information (a decisive, coalition-stable mandate) permanently
repricing the fundamental discount rate, not a transient liquidity dislocation. A signal that could
not distinguish these two economically opposite objects — genuine repricing versus transient,
liquidity-driven overshoot — would have profited identically from both, exactly the confound atlas
5.4's zero-budget verdict guards against.

### B.5 India case two — the 2024 election day, argued as the opposite caricature

The 2024 result day is the mirror image, and the contrast is the whole lesson. On **4 June 2024**,
exit polls implying an NDA landslide gave way to a BJP-short-of-majority count; the Sensex fell an
intraday low of ~**−7.4%** before closing **−5.74%** (−4,390 points), Nifty **−5.93%** (−1,379
points) [Verified via search; also `partABC-fold-rejects.md` §A.1, cross-referenced]. Unlike 2009,
this move **did** partially reverse — and fast: the next session (5 June), as the BJP secured firm
coalition commitments, the Sensex closed **+3.2%** (+2,306 points) to 74,385 and Nifty **+3.36%**
(+736 points) to 22,620 [Verified via search], with the broader arc headlined as a "rebound... Nifty
up 11% in one month" [Verified via search]. Compare 2004: on **17 May**, the Sensex fell **15.52%**
on the NDA's surprise defeat, partially offset intraday by state-financial-institution buying that
reversed "nearly half the losses" [Verified via search] — but the *multi-day* recovery was far
slower, with the Sensex returning to the 6,000 level only by **2 June 2004**, roughly two weeks later,
via a sequence of policy reassurances rather than a single next-day resolution [Verified via search].
Three violent political-surprise sessions, three different reversal signatures: 2009's positive
surprise never reversed at all — it *was* the repricing; 2004's negative surprise reversed intraday
but took two weeks, not one session, driven by credible reassurance rather than mechanical bounce;
2024's negative-then-resolved surprise reversed sharply within one session, exactly as its own
uncertainty (coalition viability) resolved within a day. **None of these three is the
liquidity-provision reversal Part A.2 formalizes**, and a mechanical signal applied naively across all
three would have produced three outcomes for reasons unrelated to the mechanism it claims to harvest
— precisely why atlas 5.4 restricts the flag to informing entry timing on positions the book already
wants, never to standing as an independent signal on episodes whose true driver is information
arrival, not transient illiquidity.

### B.6 STT's regime history and what it does to high-turnover anomalies

India's Securities Transaction Tax was introduced by the Finance Act 2004, effective **1 October
2004**, under Finance Minister P. Chidambaram, to tax the transaction itself rather than rely on
gains reporting [Verified via search]. Original rates: delivery equity **0.125%**, non-delivery
equity **0.025%**, derivatives **0.017%** [Verified via search]. The 2013 Budget, after sustained
broker/trader pressure, cut delivery equity to today's **0.1%** (both legs, 20 bps round trip),
futures to **0.01%** sell-side, and equity options to **0.05%** sell-side premium [Verified via
search]. [VERIFY: the complete dated sequence of every subsequent revision — `config/costs.yaml`'s
own decay note flags "two hikes in 18 months" on the statutory side without dating them precisely;
this pass confirmed the introduction, original rates, and the 2013 cut with confidence, not a
complete year-by-year ledger since.] The consequence is arithmetic, per §A.3: 20 bps round trip on a
strategy whose own construction implies annual one-way turnover in the multiple thousands of percent
consumes a low-single-digit percent of NAV/yr from the statutory leg alone — a drag with no developed-
market analogue in either Avramov-Chordia-Goyal (2006) or Novy-Marx-Velikov (2016), both of which
price commissions, spread and impact but never a transaction tax no execution technique can reduce.

### B.7 SEBI's own evidence that speed is where retail loses

SEBI's own research is the cleanest domestic evidence that concentrated, high-frequency activity is
systematically a losing proposition for the retail participants it draws. The July 2025
equity-derivatives study found **~91% of individual traders** net losers in FY25, aggregate losses
**~₹1.06 lakh crore** (+41% YoY) [Verified via search], extending a September 2024 update finding
**93%** of individual traders losing in equity F&O **FY22–FY24**, aggregate losses **>₹1.8 lakh
crore** over three years [Verified via search; both also cited for H57 elsewhere in this program's
register, cross-referenced]. The directly relevant finding: **59% of index-options turnover occurred
on the expiry day itself**, **~75% within one day of expiry** [Verified via search] — the
overwhelming majority of retail speed-game activity concentrated in the highest-velocity, shortest-
horizon window the market offers, correlating with rather than offsetting the aggregate loss rate.
Regulatory tightening (raised minimum contract values, weekly-expiry restrictions, upfront premium
collection, expiry-day safeguards, phased late 2024–mid 2025 [Verified via search]) reduced the loss
rate only modestly, to **~87.7%** [Verified via search] — restricting entry to the fastest game did
not, by itself, make the remaining players profitable, because the disadvantage is not primarily a
participation-threshold problem. This is the regulator's own evidence for Part G's counterparty
argument: speed is where this desk would be a retail-shaped counterparty against professionals, and
SEBI's own data on who wins that game is unambiguous.

### B.8 NSE's colocation ecosystem: the immediacy premium, already professionally harvested

NSE launched **colocation** in **August 2009** [Verified via search], letting brokers and HFT firms
house servers inside NSE's own data centre, cutting latency to the matching engine to milliseconds —
imperceptible to a human, decisive at the frequencies immediacy provision requires [Verified via
search]. The facility's own regulatory history — preferential-access allegations 2012–2014, a 2015
whistle-blower complaint, and a SEBI enforcement action that initially ordered ~₹625 crore
disgorgement before SEBI itself later dropped the charges [Verified via search] — is cited for what
it confirms: regulators, brokers, and the exchange have spent over a decade litigating exactly how
valuable microsecond execution priority is here, a level of capital commitment this research program
neither can nor needs to match. The consequence for atlas 5.4: whatever compensation exists for
supplying immediacy in Indian equities is being competed for, in real time, by exactly the colocated
capital this infrastructure houses — the India-specific instance of §B.1's US argument. This program
is not forgoing an unclaimed premium; it is declining to compete for one already being actively,
professionally harvested by counterparties this architecture was never built to out-race.

---

## Part C — India data engineering: what MR1 needs, and what stays unbuilt

### C.1 What MR1 needs when bhavcopy lands

`trial-ledger.md`'s Design MR1 entry (2026-09-02) is the binding specification for this grading path;
this section restates its requirements as data engineering rather than repeating its acceptance
language verbatim. None of the following exists yet, and none is built by this chapter:

- **Point-in-time NIFTY-750 membership.** Run the decile construction on the universe actually
  knowable on each historical rebalance date, not today's list projected backward — the same
  discipline Known Prior #7 (Contract §7) already states as decisive for the fundamentals book,
  applied here to membership. A name exiting the index (delisting, demotion below rank 750,
  acquisition) stays in the universe through its actual live dates and exits only from its actual
  exit date.
- **Survivorship handling.** Any delisted, suspended, or acquired name must contribute its actual
  realized return (including a delisting event where no clean exit price existed), never be silently
  dropped — dropping failed names biases the spread upward precisely in the small/illiquid tail where
  Avramov-Chordia-Goyal find the largest raw spreads concentrate, compounding rather than correcting
  §A.3's cost-fragility problem.
- **The liquid-half filter.** MR1's own construction restricts to "the liquid half of NIFTY 750" — a
  direct application of Chui, Ranganathan, Rohit & Veeraraghavan (2023)'s India finding that the
  **most illiquid tercile shows reversal instead of continuation** even in momentum (already verified,
  `research/dossiers/01-momentum-reversal.md` item 16, cross-referenced): an unfiltered construction
  risks conflating a genuine liquid-name signal with a structurally different illiquidity pattern in
  the tail — the same mechanism conflation §B.4/B.5 warn against at the panel rather than event level.
- **Decile construction at month-end with T+1 settlement alignment.** Ranking-period return and
  holding-period entry must align to when a position could actually be established under India's
  settlement cycle — a month-end decile enters (and is costed) as of the next settlement date, not
  the formation date, or the backtest silently assumes an execution capability the desk does not
  have; reversal's short holding period makes this error proportionally larger than for a 12-month
  momentum construct.
- **The cost model per book**, cited from `config/costs.yaml`. MR1's acceptance is explicitly "NET of
  the config/costs.yaml stack per book" — the cash-delivery round trip ([24, 32] bps all-in, D05
  F1–F4), the impact model's square-root form ($I = Y \cdot \sigma_{daily} \cdot \sqrt{Q/ADV}$,
  $Y \in [0.5, 1.0]$), and the (still `PROVISIONAL`) ADV-by-rank-bucket table — applied separately per
  book, since §A.3's arithmetic scales with exactly these book-specific parameters and one cost figure
  cannot honestly stand in for all three books.
- **The two-half-sample-plus-decay-haircut acceptance, already registered.** MR1's bar —
  net-of-cost spread positive across **both** halves **and** surviving the McLean-Pontiff haircut — is
  not this chapter's to loosen; it applies McLean & Pontiff (2016)'s decay framework (Contract §5) to
  a signal with, per atlas 5.4's own words, "zero India magnitude studies" behind it — MR1 is
  simultaneously the first India test of this horizon and one pre-committed to the same skeptical
  discount this program applies to every well-documented, heavily-arbitraged anomaly.

### C.2 What is deliberately not built, and why

Part E of the companion document states, and this chapter quotes rather than paraphrases: "5.4's flag
machinery, if MR1 ever unfreezes it, is a one-line percentile rank on the existing
expanding-percentile utility — deliberately NOT built today: building instruments for frozen signals
invites their use (the same reasoning that kept flow-momentum out of the FPI module's API)"
(`partDH-close.md`, Part E). Concretely: no reversal-percentile function, no liquid-half filter, no
decile-construction script exists in this codebase, and none should before bhavcopy lands and MR1's
own pre-registration formally opens — not because the specification above is unclear, but because an
*available* instrument for a *frozen* signal invites exactly the failure Part G names: a researcher
under deadline pressure finding it easier to run "just to see" than to hold the freeze until the
pre-registered bar is genuinely in place. The FPI-module precedent this sentence cites applies the
same discipline consistently across the program, not as a one-off for reversal.

### C.3 Day-of-week: nothing to engineer, and the CW3/GS1 precedent for why

Atlas 5.5's reject implies a distinct data-engineering consequence: no design is registered, no bar
pre-declared, no future bhavcopy pull earmarked for day-of-week or expiry-day seasonality in
isolation — as the companion states, "No trial is spent — CW3/GS1 already demonstrated the omnibus
discipline at monthly resolution, and a daily demonstration would require the bhavcopy vault to prove
a negative the register already prices at zero." **CW3** (`trial-ledger.md`) is the template: a
twelve-month Kruskal-Wallis omnibus on this program's own India market-factor data returned **H =
12.13, p = 0.354** — no calendar structure — but its own pre-declared rule states that even a
significant print would **not** overturn the reject, since Contract §8's mechanism ban and the
Sullivan-Timmermann-White correction (§A.4) both operate independently of any single omnibus result; a
twelve-way comparison expects ~0.6 false positives at 5% by chance, so a marginal print earns
dissection and logging, never promotion. **GS1** ran the identical demonstration on gold's monthly
seasonality (**H = 10.87, p = 0.454**, float era 1972–2026), confirming the discipline generalizes
across asset classes. Consequence: 5.5 needs no bhavcopy pull, no daily-resolution rerun, no
MR1-style acceptance bar — the reject rests on the mechanism-free Sullivan-Timmermann-White argument
in full, correctly inherited, and per Contract §9's ban on re-testing rejected ideas with tweaked
parameters, not one this program should spend a trial re-deriving at finer resolution merely because
finer data eventually exists.

---

## References

Jegadeesh, Narasimhan (1990), "Evidence of Predictable Behavior of Security Returns," *Journal of
Finance* 45(3): 881–898 [Verified via search]. · Lehmann, Bruce N. (1990), "Fads, Martingales, and
Market Efficiency," *Quarterly Journal of Economics* 105(1): 1–28 [Verified via search]. · Campbell,
John Y., Grossman, Sanford J. & Wang, Jiang (1993), "Trading Volume and Serial Correlation in Stock
Returns," *Quarterly Journal of Economics* 108(4): 905–939 [Verified via search]. · Nagel, Stefan
(2012), "Evaporating Liquidity," *Review of Financial Studies* 25(7): 2005–2039 [Verified via
search]. · Cheng, Hameed, Subrahmanyam & Titman (2017), "Short-Term Reversals: The Effects of
Institutional Exits and Past Returns," *JFQA* 52: 143–173 [already verified, `research/dossiers/
01-momentum-reversal.md` item 22 — cross-referenced]. · Avramov, Chordia & Goyal (2006), "Liquidity
and Autocorrelations in Individual Stock Returns," *Journal of Finance* 61(5): 2365–2394 [Verified
via search]. · Novy-Marx, Robert & Velikov, Mihail (2016), "A Taxonomy of Anomalies and Their Trading
Costs," *Review of Financial Studies* 29(1): 104–147 [Verified via search]. · Frazzini, Israel &
Moskowitz, "Trading Costs of Asset Pricing Anomalies" [already verified, `research/dossiers/
01-momentum-reversal.md` item 24 — cross-referenced]. · French, Kenneth R. (1980), "Stock Returns
and the Weekend Effect," *JFE* 8(1): 55–69 [Verified via search]. · Gibbons, Michael R. & Hess,
Patrick (1981), "Day of the Week Effects and Asset Returns," *Journal of Business* 54(4): 579–596
[Verified via search]. · Sullivan, Timmermann & White (2001), "Dangers of Data Mining: The Case of
Calendar Effects in Stock Returns," *Journal of Econometrics* 105(1): 249–286, using the stationary
block bootstrap of Politis & Romano (1994) [Verified via search]. · Wood, McInish & Ord (1985), "An
Investigation of Transactions Data for NYSE Stocks," *Journal of Finance* 40(3): 723–739 [Verified
via search]. · Admati, Anat R. & Pfleiderer, Paul (1988), "A Theory of Intraday Patterns: Volume and
Price Variability," *RFS* 1(1): 3–40 [Verified via search]. · Chui, Ranganathan, Rohit &
Veeraraghavan (2023), "Momentum, Reversals and Liquidity: Indian Evidence," *Pacific-Basin Finance
Journal* 82: 102193 [already verified, `research/dossiers/01-momentum-reversal.md` item 16 —
cross-referenced]. · McLean, R. David & Pontiff, Jeffrey (2016), "Does Academic Research Destroy
Stock Return Predictability?" *Journal of Finance* 71: 5–32 [already verified, Contract §5 and
`research/dossiers/01-momentum-reversal.md` item 10 — cross-referenced]. · Press reporting (NBC News;
*Fluctuation and Noise Letters* "A Brief Analysis of May 2004 Crash in the Indian Market"; Business
Standard) on the 17 May 2004 crash and its ~two-week recovery to 6,000 by 2 June 2004 [Verified via
search]. · Press reporting on the 18 May 2009 upper-circuit day, per `research/cycles/
political-close/partABC-fold-rejects.md` §A.1 (cross-referenced, not re-verified independently here)
[Verified via search]. · Business Standard, HDFC Sky, Gulf News on the 4–5 June 2024 election-result
sessions and the one-month rebound [Verified via search]. · Fyers, ICRIER Working Paper 273 (Neha
Malik), 5paisa on the STT's 2004 introduction and 2013 revision [Verified via search]. · SEBI press
release (Sept 2024) on FY22–24 equity F&O losses; SEBI's July 2025 equity-derivatives study (as
reported by Open, Moneylife) on FY25 losses and expiry-day turnover concentration [Verified via
search]. · NSE ("Co-location Facility"), Vajiram & Ravi, DatacenterDynamics, IRCCL on the August 2009
NSE colocation launch and its enforcement history [Verified via search]. · `research/CONTRACT.md`
§§1, 4, 5, 8, 9, 12. · `docs/CYCLE_ATLAS.md` §0, rows 5.1–5.6, §7, §11.1. · `research/cycles/
fastlayer-close/partDH-close.md` (Parts D, E, F, H — cross-referenced throughout, never re-derived).
· `research/register/trial-ledger.md` (CR2, CW1, CW3, GS1, FS-U1, FS-U2, M4, Design MR1). ·
`config/costs.yaml` (D05 F1–F4). · `research/dossiers/01-momentum-reversal.md` (cross-referenced for
Cheng et al., Frazzini-Israel-Moskowitz, Chui et al.). · `research/cycles/political-close/
partABC-fold-rejects.md` (the 2004/2009/2024 verifications, cross-referenced for the 2009 print). ·
`docs/CYCLE_ATLAS.md` line 163 (the options-premium rejection, D12, generalized in Part G).
