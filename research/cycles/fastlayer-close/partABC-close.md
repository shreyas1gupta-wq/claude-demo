# The Fast-Layer Closer — Parts A, B, C & G, Argued in Full

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-02

Parts A, G, B & C · Atlas entries **5.4** (1-month cross-sectional reversal, `docs/CYCLE_ATLAS.md`
line 144, Band 5 — the sub-monthly fast layer: "Liquidity-provision premium (Cheng et al.) — real,
but the most cost-fragile anomaly known + 20bp STT round trip; zero India magnitude studies";
harvest **Tier-C flag only, ZERO return budget → L1**), **5.5** (weekly/daily seasonals, line 145:
"No surviving mechanism after costs at our scale"; harvest **REJECT**), and **5.6** (intraday
cycles, line 146: "Real microstructure, but this is an EOD-data, weekly-cadence program by
design"; harvest **Out of scope**). This chapter is the fast layer's theory-and-evidence half; its
companion — `research/cycles/fastlayer-close/partDH-close.md`, already on record — is the routing
table, the algorithm note, the harvest, and the knowledge ledger (Parts D, E, F, H). Between the two
documents the full A-through-H lettering is now filled for this entry, matching the convention this
program has used for its other closing monographs (`research/cycles/political-close/`,
`research/cycles/calendar-mechanics/`): **this chapter never re-derives what the principal's own
document has already settled** — Part D's three verdicts, Part E's deliberate non-build of flag
machinery, Part F's harvest table, and Part H's knowledge ledger are cited throughout, not repeated.

**What this chapter is for.** `research/register/trial-ledger.md`'s "Design MR1" block is explicit:
this is a **registered design, not a run trial** — "(awaits bhavcopy vault)" is MR1's own status
line, and no desk number of any kind exists for 5.4, 5.5, or 5.6 as of this writing. Every figure
below is therefore a literature number, an India institutional fact, or a public-record case,
each carrying its own author-year or its own verification tag; nothing here is computed on this
program's own data, and nothing here should be read as if it were. The chapter's job is to argue
each of the fast layer's three verdicts — the Tier-C flag, the reject, and the scope line — to its
strongest form before accepting it, following this program's house rule (stated most recently in
`research/cycles/political-close/partABC-fold-rejects.md` and, before that, the Kondratieff/Perez
monograph) that a refusal earns its verdict the same way a seat does. The through-line the principal
set for this entry is the honest one: **the last band is where speed premia live, and this desk's
edge is knowing exactly which speed games it cannot win.** Part A builds the theory and the math
behind each of the three verdicts; Part G turns the lens on the operator rather than the market —
why the fastest patterns are the most seductive to a desk, and what discipline refuses that
seduction; Part B tests the theory against the public record, cross-country and in India, at double
length for the India material as the task requires; Part C specifies exactly what MR1 needs when
bhavcopy lands, and exactly what stays deliberately unbuilt until it does.

---

## Part A — Theory, with the math

### A.1 Short-term reversal, formalized

The two founding results are close contemporaries and use different instruments to find the same
object. **Jegadeesh (1990)**, "Evidence of Predictable Behavior of Security Returns," *Journal of
Finance* 45(3): 881–898, sorts individual NYSE/AMEX stocks into decile portfolios on trailing
one-month return and finds **first-order serial correlation in monthly stock returns that is
strongly negative** — the decile spread between prior losers and prior winners over 1934–1987 is
**2.49% per month** [Verified via search], even as the same securities show strong *positive*
serial correlation at the twelve-month horizon — the exact opposite-signed structure this program's
own momentum dossier already documents on the long side (`research/dossiers/01-momentum-reversal.md`
§1, items 1–9; cross-referenced, not re-derived) and which atlas §11.1's "mean-reversion horizon
sandwich" (`docs/CYCLE_ATLAS.md` line 241) frames as one phenomenon read at different horizons:
reversal at both ends, continuation in the middle. **Lehmann (1990)**, "Fads, Martingales, and
Market Efficiency," *Quarterly Journal of Economics* 105(1): 1–28, works at weekly rather than
monthly resolution and reaches the harder-edged conclusion: stocks that are "winners" one week show
sizeable return **reversals the following week**, and the arbitrage profits implied **persist after
corrections for bid-ask spreads and plausible transaction costs** [Verified via search] — Lehmann's
own paper is, in other words, the first to state explicitly what six decades of subsequent
cost-stack literature would spend itself re-litigating: that a raw reversal signal survives a
first-pass cost adjustment, and that everything interesting about the anomaly's fate happens in the
gap between "plausible" costs and the *actual* cost stack a real book faces (§A.3 below).

Stated formally, the object both papers document is a negative own-autocorrelation in the
cross-section: for a stock $i$ with return $r_{i,t}$ over the ranking window and $r_{i,t+1}$ over the
holding window, $\mathrm{Cov}(r_{i,t}, r_{i,t+1}) < 0$ at horizons of roughly one week to one month,
reversing sign at horizons beyond about three months (the momentum band) and again beyond two to
five years (the long-horizon reversal atlas §11.1 routes to value, H64). A decile-sorted long-short
implementation — long the bottom decile on $r_{i,t}$, short the top decile — earns a portfolio
return whose expectation is the cross-sectional covariance term scaled by the dispersion of the
ranking-period return; this is precisely why the anomaly's magnitude *rises* mechanically with
cross-sectional return dispersion (more volatile months produce wider deciles, which produces larger
raw reversal spreads before any cost is subtracted) — a structural fact that matters directly for
§A.2's VIX-conditioning result, because vol dispersion and VIX co-move.

### A.2 The liquidity-provision interpretation, formalized

The mechanism question — *why* does a negative own-autocorrelation exist at all, rather than being
arbitraged to zero — has a specific, well-identified answer, and it is the strongest form of
category (iii) in the contract's own survival taxonomy (§5): **a genuine risk premium someone must
be paid to bear.** **Campbell, Grossman & Wang (1993)**, "Trading Volume and Serial Correlation in
Stock Returns," *Quarterly Journal of Economics* 108(4): 905–939, supply the founding equilibrium
logic: risk-averse market makers accommodate buying or selling pressure from liquidity-motivated
("noninformational") traders, and the expected return that compensates the market maker for
absorbing that inventory risk is exactly the negative autocorrelation the data shows — the paper's
own empirical signature is that **first-order daily return autocorrelation declines with trading
volume** [Verified via search]: a high-volume down-move is more likely to be liquidity-driven (and
therefore reversal-prone) than a low-volume one, which is more likely to carry genuine information
(and therefore persist). This is the volume-conditioning the task asks this chapter to name, and it
is the theoretical ancestor of this program's own already-seated volume-momentum feature test
(`research/dossiers/01-momentum-reversal.md` item 18, Maheshwari-Dhankar 2017b — cross-referenced).

**Nagel (2012)**, "Evaporating Liquidity," *Review of Financial Studies* 25(7): 2005–2039, takes the
same mechanism and makes it dynamic and directly measurable: the returns to a short-term reversal
strategy are a **proxy for the compensation to liquidity provision itself**, and that compensation
is **highly predictable from the level of the VIX** [Verified via search]. The economic logic runs
through capital scarcity rather than volume alone: when financial intermediaries who would ordinarily
supply liquidity are themselves capital-constrained — precisely the condition a spiking VIX signals
— the price of absorbing someone else's selling pressure rises, and expected reversal returns (and
conditional Sharpe ratios) **spike** in exactly those episodes [Verified via search]. Formally, if
$R_t^{rev}$ is the reversal strategy's realized return in month $t$, Nagel's regression is of the
shape

$$R_t^{rev} = \alpha + \beta \cdot \mathrm{VIX}_{t-1} + \varepsilon_t, \quad \beta > 0,$$

with the fitted relationship strong enough that the strategy's own conditional Sharpe ratio is a
near-monotone function of the lagged VIX level — the mechanism this chapter's Part B tests directly
against the 2008 and 2020 episodes, and the reason atlas 5.4's own entry cites "Cheng et al." (Cheng,
Hameed, Subrahmanyam & Titman 2017, already verified and cited in full in
`research/dossiers/01-momentum-reversal.md` item 22 — cross-referenced, not re-derived here) for the
companion finding that reversal profits **rise specifically where institutional competition for the
liquidity-provision role is scarce**: the same mechanism, read through market structure (who else is
willing to be the market maker) rather than through the VIX (how urgently the market maker must be
paid). Nagel's VIX channel and Cheng et al.'s institutional-competition channel are two observable
proxies for one underlying state — the price of immediacy — and that price is precisely what atlas
5.4's own verdict names as the thing a weekly-cadence desk cannot collect: harvesting it means
*being* the immediacy provider, at daily speed, in falling names, which this program's Contract §1
mandate (EOD data, weekly-preferred cadence) structurally forecloses before a single number is
computed.

### A.3 The cost knife

The mechanism argument establishes that reversal is a real premium; the cost argument establishes
that it is, of all real premia in the literature, the one an implementing book is least able to
keep. **Avramov, Chordia & Goyal (2006)**, "Liquidity and Autocorrelations in Individual Stock
Returns," *Journal of Finance* 61(5): 2365–2394, is the paper that puts the two facts in direct
tension: reversal is **strongly related to stock illiquidity**, even controlling for trading volume,
and the **largest reversals — and the largest potential contrarian-strategy profits — occur
precisely in the highest-turnover, lowest-liquidity names** [Verified via search]; but the paper's
own conclusion is that the implied contrarian trading profits are **smaller than the likely
transaction costs** of trading exactly those names [Verified via search]. This is not an incidental
finding — it is close to a structural impossibility theorem for the anomaly: the premium's magnitude
and the cost of harvesting it are both increasing functions of the *same* underlying variable
(illiquidity), so improving the raw spread by hunting further into the illiquid tail *simultaneously*
raises the cost that eats it. No cost-mitigation technique changes this relationship in kind, only
in degree.

**Novy-Marx & Velikov (2016)**, "A Taxonomy of Anomalies and Their Trading Costs," *Review of
Financial Studies* 29(1): 104–147, is the paper that turns this qualitative tension into a taxonomy
with a hard empirical line. Studying a broad cross-section of documented anomalies net of realistic
trading costs, the paper's headline finding is a turnover threshold: **most anomalies with less than
roughly 50% monthly one-way turnover generate significant net-of-cost spreads once designed with
cost mitigation (a buy/hold spread — stricter entry thresholds than exit thresholds — is the single
most effective technique); few anomalies with turnover above that line do** [Verified via search].
Short-term reversal sits on the wrong side of this line by construction, not by measurement:
a monthly-reformed decile reversal book that re-ranks and re-trades its full long-short book every
period has a raw one-way monthly turnover on the order of 100% or more — every name in this month's
losers decile is, almost by the anomaly's own definition (last month's biggest movers), unlikely to
be next month's losers decile, so persistence between adjacent months' rankings is low and the
reformation is close to a full portfolio replacement. [VERIFY: the taxonomy's own reported turnover
percentile for short-term reversal specifically — this chapter states the mechanical consequence of
monthly full-decile reformation rather than quoting a table figure not directly confirmed this
pass.] The consequence, however it is measured precisely, is qualitative and undisputed across the
literature this program has surveyed: **short-term reversal is the highest-turnover anomaly commonly
studied, and Novy-Marx-Velikov's own cutoff places it structurally on the side of the line where net
spreads are, empirically, rarely significant** — the paper's contribution is to make with a
cost-mitigation-optimized methodology the same point Avramov-Chordia-Goyal made with a simpler one:
the anomaly with the largest apparent gross spread and the anomaly with the largest cost drag are,
to a first approximation, the same anomaly.

India's cost stack sharpens this knife rather than dulling it. `config/costs.yaml` (D05, re-verified
FY2026-27) prices the cash-delivery round trip at **[24, 32] bps all-in** — a Securities Transaction
Tax of 10 bps on *each* leg (buy and sell, 20 bps round trip alone, per the statutory table's
`cash_delivery: {stt_buy: 0.0010, stt_sell: 0.0010, ...}`), plus stamp duty on the buy leg (1.5 bps),
exchange and SEBI turnover fees, and GST on the fee component — before a single basis point of market
impact is added, and before brokerage (`brokerage_per_side_bps`, itself only a placeholder pending
negotiated desk terms). The STT component alone has **no analogue whatsoever** in the Avramov-
Chordia-Goyal or Novy-Marx-Velikov US samples: a US institutional book pays commissions, spread, and
impact, but no transaction tax; an Indian book pays all of those *plus* a flat 20 bps round trip that
cannot be negotiated away, mitigated by execution algorithm, or arbitraged down by any market-
structure improvement, because it is levied by statute regardless of how the trade is executed. Apply
this to the turnover arithmetic directly: a reversal book reforming its full book monthly at ~100%+
one-way turnover per month compounds to well over 1,000% one-way turnover per year — call it, for
illustration only and explicitly *not* a desk estimate, on the order of ten to twelve full
reformations — at which point the STT leg alone (20 bps × ~10-12 round trips/yr) consumes on the
order of **2.0–2.4% of NAV per year** before impact cost is even modeled, against a raw gross spread
whose own academic magnitude (Jegadeesh 1990's 2.49%/month equivalent, itself a pre-cost, developed-
market, large-sample figure with no India analogue) is not preserved once diluted by a year of that
drag. This is the arithmetic form of atlas 5.4's own one-line verdict — "the most cost-fragile
anomaly known" — and it is why the entry carries a *zero* return budget rather than merely a haircut:
a haircut presumes a residual worth sizing; the cost knife here cuts closer to the bone than that.

### A.4 Day-of-week and weekend effects: the archetype of the mined calendar pattern

Where reversal fails a real mechanism on cost grounds, the weekly/daily seasonal family (atlas 5.5)
fails on a different and more fundamental axis: no mechanism ever survived to be cost-tested in the
first place. **French (1980)**, "Stock Returns and the Weekend Effect," *Journal of Financial
Economics* 8(1): 55–69, is the founding empirical result: under the "calendar time" null hypothesis
(returns accrue continuously, so Monday's return — spanning Friday close to Monday close — should be
roughly three times an ordinary day's expected return) the data instead show **significantly negative
average Monday returns**, in every five-year subperiod of the 1953–1977 S&P sample, while the other
four weekdays average positive [Verified via search] — directly rejecting calendar time in favor of
a "trading time" account in which expected returns per active trading session should instead be
equal across weekdays, and finding that null rejected too, since Monday is not merely a proportional
share of an otherwise-flat week but reliably *negative* in level. **Gibbons & Hess (1981)**, "Day of
the Week Effects and Asset Returns," *Journal of Business* 54(4): 579–596, independently confirms
negative Monday returns across the thirty Dow Jones Industrial stocks with a companion methodology
[Verified via search], and the effect's cross-confirmation across two independent studies, two
distinct samples, and two distinct econometric approaches is exactly the kind of result that looked,
in 1981, like a genuine anomaly rather than an artifact.

The genuinely instructive event, for this program's own epistemics, is what happened next: the
effect was published, widely replicated for a decade, offered dozens of competing behavioral and
institutional explanations (settlement-cycle timing, corporate bad-news-dumping on Fridays,
short-seller behavior), and then **evaporated** once anyone checked whether it had ever been more
than the best-performing member of a very large tested set. **Sullivan, Timmermann & White (2001)**,
"Dangers of Data Mining: The Case of Calendar Effects in Stock Returns," *Journal of Econometrics*
105(1): 249–286, is the canonical demonstration, and its method is the reason it is canonical rather
than merely another negative replication: rather than testing the weekend effect (or any other single
calendar rule) in isolation, the paper constructs the **full universe of 9,452 competing calendar
trading rules** an unprincipled researcher armed with a century of daily data could have tried, and
applies the **stationary block bootstrap of Politis & Romano (1994)** to the joint distribution of
performance measures across every rule simultaneously, yielding a data-mining-adjusted p-value for
whichever rule performs *best* in the full universe [Verified via search]. The result: individual
calendar rules — the weekend effect prominently among them — **appear significant when examined in
isolation**, exactly as French (1980) and Gibbons-Hess (1981) found; but once evaluated **within the
full universe of competing rules**, that significance **largely disappears**, and even the single
best-performing rule in the entire 9,452-rule universe **fails to deliver statistically significant
outperformance relative to buy-and-hold** after the data-mining adjustment [Verified via search]. The
bootstrap's logic, stated plainly: if a researcher is implicitly free to have tried thousands of
candidate rules and report only the one that worked, the correct null distribution against which to
judge "the best one I found" is the *maximum* over all 9,452 candidate statistics under the true null
of no effect — not the marginal distribution of any single statistic taken alone — and once that
correct comparison is made, the calendar-effect literature's apparent significance is revealed as
almost entirely a multiple-testing artifact rather than a mispricing anyone could trade. This is the
formal statistical content behind this program's own CW3/GS1 house discipline (§C below): a
Kruskal-Wallis omnibus across twelve calendar months, run twice on this program's own vaulted data
(CW3 on the India market factor, GS1 on gold), each pre-declaring in advance that even a nominally
significant print would not overturn the reject, for exactly the Sullivan-Timmermann-White reason —
a twelve-way comparison expects roughly 0.6 false positives at the 5% level by chance alone, and no
mechanism has ever been proposed for a day-of-week or expiry-day pattern that would survive the same
kind of full-universe correction French and Gibbons-Hess's original single-rule tests never applied.

### A.5 The intraday U-shape: real microstructure, deliberately out of scope

The third fast-layer entry (atlas 5.6) is the one this chapter must argue most carefully, because it
is the only one of the three where the underlying phenomenon is neither cost-fragile (like 5.4) nor
mechanism-free (like 5.5) — it is a **real, mechanism-backed, extensively replicated microstructure
regularity**, and the correct verdict is nonetheless to leave it alone, for a programmatic rather
than an evidentiary reason. **Wood, McInish & Ord (1985)**, "An Investigation of Transactions Data
for NYSE Stocks," *Journal of Finance* 40(3): 723–739, is the founding empirical documentation: using
transactions data from 1971–72 and 1982, the paper shows the **variability of returns across the
trading day traces a crude U-shape** — high near the open, falling through the middle of the session,
rising again into the close — with return distributions differing systematically among overnight
trades, the first thirty minutes after the open, trades near the close, and the ordinary middle of
the day [Verified via search]. **Admati & Pfleiderer (1988)**, "A Theory of Intraday Patterns: Volume
and Price Variability," *Review of Financial Studies* 1(1): 3–40, supplies the equilibrium mechanism
Wood-McInish-Ord's paper does not itself derive: in a model where **discretionary liquidity traders
strategically choose when to trade** and **informed traders concentrate their own activity to hide
inside the liquidity traders' volume**, both trader types converge on the *same* time-clustering
equilibrium — liquidity traders prefer high-volume periods because price impact per unit traded is
lower when many others are trading too, and informed traders prefer exactly the same periods because
their own informed volume is best camouflaged inside a busy tape — producing **endogenously
concentrated trading and price variability at the open and close**, precisely the U-shape the
transactions data show [Verified via search]. This is a genuine strategic-equilibrium account, not a
statistical curiosity: unlike the weekend effect, no serious market microstructure theorist regards
the U-shape as an artifact of data mining, and unlike 1-month reversal, harvesting it does not
require a book to out-compete professional liquidity providers on their own cost-minimized turf —
quite the opposite, the U-shape is in large part a description of *how* those liquidity providers and
informed traders already behave.

The out-of-scope verdict therefore rests on neither of the two arguments that dispose of 5.4 and 5.5.
It rests on Contract §1's own architectural fact, stated as plainly as the mandate states it: **this
is an EOD-data, weekly-cadence program by design** — the desk's data inputs (bhavcopy), its signal
construction (percentile ranks, monthly-to-weekly rebalance cadences per §10's working conventions),
and its entire evidentiary apparatus (purged, embargoed cross-validation at monthly-and-above
embargo widths per Contract §9) are built for a decision frequency measured in weeks, not minutes.
A program built this way **neither measures nor trades** intraday structure, and the honest
consequence is not that the U-shape's alpha is rejected on the merits — no trial has ever been run
to reject it, and the atlas is explicit that none should be — but that the entire question sits one
layer beneath where this desk's signals live. The U-shape's actual economic content is fully absorbed
at the point where a portfolio decision (rebalance a name, enter a position, execute a reformed
book) is *translated into orders*: an execution algorithm that paces participation against intraday
volume (Contract §10's "participation cap per rank bucket," `config/costs.yaml`'s
`participation_cap_per_day: [0.05, 0.10]`, Korajczyk-Sadka-style practitioner convention already
registered) is, whether or not anyone names it this way, already respecting the Admati-Pfleiderer
U-shape — trading more where volume (and therefore camouflage and liquidity) is naturally highest,
which is precisely the open-and-close concentration the theory predicts and the transactions data
confirm. This is the scope boundary stated precisely, per the atlas's own instruction that the
purpose of an out-of-scope entry is to prevent silence from being mistaken for ignorance: **the
mechanism is real, this program has read the theory that explains it, and this program's execution
layer already inherits its consequence through ordinary participation logic — without this desk ever
needing, or being able, to measure or trade the U-shape as a signal in its own right.**

---

## Part G — Operator psychology: the seduction of speed

The theory in Part A explains why the fast layer's three verdicts are what they are. This part
explains something different and, for an operating desk, arguably more important: why a competent
research team, working in good faith, is *structurally* at risk of getting exactly these three
verdicts backwards — of promoting 5.4 past its zero budget, of quietly re-testing 5.5 with tweaked
parameters until something clears a threshold, or of drifting into building 5.6 machinery nobody
asked for. The risk is not carelessness. It is a predictable psychological pull built into the
statistics of fast signals themselves, and naming the pull precisely is this program's actual
defense against it — Contract §12's instruction that research agents "never fabricate a citation" and
"prefer Indian evidence" is a defense against a different failure mode; this part is about the
failure mode the contract's Tier system and its Traps (§8) exist to guard against structurally,
because no amount of individual diligence reliably guards against it in the moment.

**The fastest patterns look most tradable because they produce the most backtest observations.**
This is close to an identity, not a coincidence, and it is worth stating as one. A signal with a
one-month half-life generates roughly twelve independent-ish observations per year of history; a
signal with a one-week half-life generates roughly fifty; a signal with an intraday half-life
generates thousands. Holding the *true* underlying effect size constant, a faster signal's
in-sample t-statistic mechanically grows with the observation count — $t \approx \sqrt{n} \cdot$
(effect size / noise), so a reversal signal tested at daily resolution over five years of history
carries an order of magnitude more nominal statistical power than the same economic idea tested at
monthly resolution over the same five years, even before any consideration of whether the underlying
effect is *real* at that resolution or whether costs eat it. This is exactly the mechanism this
program's own CR2 and CW1 trials already demonstrated from the opposite direction
(`research/register/trial-ledger.md`): CR2 found the named "mid-2025 quant unwind" **invisible** at
monthly WML granularity — not because nothing happened, but because monthly resolution is simply the
wrong instrument to see an event whose true timescale is days; CW1 found Budget-month volatility
statistically ordinary at monthly resolution ("the CR2 pattern again," the ledger's own phrase) for
the identical reason. The fast layer's temptation runs in the mirror-image direction: a phenomenon
that is *real* but *small and cost-fragile* at its true (daily-to-weekly) resolution will, if tested
at that same fine resolution with enough history, produce backtest statistics that *look* dramatically
more significant than a slower, larger, more robust signal tested over the same calendar span — purely
because the fast signal accumulated more nominal degrees of freedom, not because it is a better bet.
An operator who has not internalized this identity will find the fast layer's own in-sample evidence
more persuasive than the slow layer's, systematically and for a reason that has nothing to do with
which layer actually pays after costs. This is why Contract §9's insistence on purged, embargoed
cross-validation and Contract §5's insistence that every signal answer "why does this survive being
known" in writing exist as *structural* countermeasures rather than as due-diligence checklist items:
they are specifically designed to defeat an n-inflation illusion that individual researcher care
cannot reliably catch in the moment, because the illusion operates on the statistics themselves, not
on anyone's judgment about them.

**"We could day-trade this" is the last refuge of a desk out of ideas.** This is a psychological
observation about where the temptation actually shows up in practice, not a theoretical one. A desk
whose slower signals (the credit cycle, the value spread, cross-sectional momentum) have each been
argued to a Tier-B-or-better standard, sized, and haircut per Contract §5 has, by that point, run out
of *comfortable* places to look for incremental return — every slow lever has already been pulled as
far as its own evidence supports. The fast layer is where an under-resourced or evidence-exhausted
research effort goes next, not because the fast layer's evidence is better, but because it is the one
remaining place where a plausible-sounding mechanism story (liquidity provision! microstructure!) can
still be told about *something*, and because the backtest-observation-count effect described above
makes that something look, superficially, like the most statistically confident finding in the whole
program. The tell is almost always in the language: an argument that begins from the strategy's
*resolution* ("we could trade this daily instead of weekly") rather than from its *mechanism or
survival argument* ("here is why this specific premium persists being known") has already, before a
single number is computed, inverted the contract's own §5 discipline, which asks what argument
justifies the trade, not what frequency would make the trade's in-sample statistics look best. This
program's own atlas is unusually explicit that this exact temptation was already checked once, for
options rather than reversal (atlas §7's rejected list, `docs/CYCLE_ATLAS.md` line 163: "Options-
premium harvesting cycles ... no argument we beat professional vol desks at their own book (D12)")
— the fast layer's discipline generalizes a lesson this program had already learned in an adjacent
domain, and Part G's job is to name it explicitly rather than let each fast-signal candidate
re-discover it independently.

**The discipline of the out-of-scope verdict versus the reject: silence is not ignorance.** Atlas
5.6's own entry states this distinction in one sentence — "out-of-scope differs from reject: no
evidence claim is made either way" (`research/cycles/fastlayer-close/partDH-close.md` Part D) — and
Part G's contribution is the psychological argument for *why* the distinction matters operationally,
beyond mere precision of language. A **reject** (5.5) is a claim: this program looked at the evidence
and the mechanism, and concluded neither survives. It can, in principle, be *reopened* — Contract
§9's own rule ("re-opening requires a new mechanism argument as a NEW ledger entry carrying its own
count") explicitly anticipates this, and a genuinely new mechanism argument (not a re-run of the old
one with tweaked parameters, which the same rule bans) would deserve a fresh hearing. An **out-of-
scope** verdict (5.6) is not a claim at all — it is a boundary statement about what this program's
own architecture is built to do, and it should *never* be confused with either a pass or a fail on
the merits. The operational risk this distinction guards against runs in both directions: treating
an out-of-scope boundary as a quiet reject risks a future researcher, encountering fresh (and
genuinely compelling) intraday evidence, wrongly believing this program has already litigated and
rejected it, and therefore never bringing the evidence forward at all; treating a reject as merely
out-of-scope risks the opposite error — a future researcher reasonably assuming that if the desk ever
built daily-resolution machinery, day-of-week seasonality would suddenly become tradable, when in
fact the mechanism-free verdict has nothing to do with resolution and would not change with it. Atlas
5.6's closing sentence — "the entry exists so nobody mistakes silence for ignorance" — is this
program's own name for exactly this risk, and Part G's operator-psychology framing is that the risk
is not primarily a documentation failure; it is a *memory* failure of the kind organizations
routinely make about their own past decisions, and the fix is the same one this program applies
everywhere else: write the reasoning down, in full, at the time the verdict is reached, so that a
future researcher inherits the argument rather than merely the label.

**Knowing which counterparty you would be.** The single sharpest psychological check this chapter can
offer, and the one this program's own D12-citing rejection of options-premium harvesting already
modeled, is to ask concretely: *who is on the other side of this trade, and am I better positioned
than they are?* For the 1-month reversal trade, the answer is uncomfortable and specific: the
counterparty supplying the *opposite* side of the liquidity-provision premium — i.e., the desks this
program's own reversal book would be *competing with* to be the one paid for absorbing selling
pressure — are exactly the professional high-frequency market-making firms this chapter's Part B.6
documents inside NSE's own colocation facility, firms whose entire commercial existence is built
around minimizing precisely the latency and inventory-holding costs a weekly-cadence, EOD-data desk
cannot avoid. This is not a close contest to enter carefully; it is a contest this desk is, by
architecture, not equipped to enter at all, and Nagel's (2012) own VIX-conditional framing makes the
asymmetry sharper still: the moments when the reversal premium is *largest* (VIX spikes, capital-
constrained intermediaries) are precisely the moments when the professional liquidity-providing
counterparty is itself most stressed and most likely to widen its own required compensation — which
means the premium is biggest exactly when a slow-moving book would need to react fastest, the one
capability a weekly-cadence architecture structurally lacks. For a monthly-to-quarterly value or
credit-cycle rebalance, by contrast, the honest answer is closer to **against no one in particular**
— the desk is not competing against a specialized professional counterparty for the marginal unit of
immediacy; it is expressing a view about multi-quarter fundamentals against a diffuse set of other
long-horizon holders, none of whom has a structural speed advantage the desk's own architecture
cannot match. Asking this one question — which specific, real counterparty sits on the other side,
and does this desk's architecture out-compete them or merely hope not to notice them — is, in
Part G's own view, a faster and more reliable check against the fast layer's seduction than any
amount of additional backtesting, precisely because it cannot be gamed by resolution or observation
count the way a Sharpe ratio can.

---

## Part B — Cross-country evidence and the India cases

### B.1 US reversal profitability decay as HFT market-making capacity grew

The single cleanest cross-country test of Part A's liquidity-provision mechanism is not a new
regression; it is the historical fact of who supplies the liquidity a reversal strategy is paid to
provide, and how that population has changed. **Frazzini, Israel & Moskowitz** document, using
roughly a trillion dollars of live institutional trading data across nineteen developed markets
1998–2011, that **short-term reversal is the single most trading-cost-constrained anomaly** of the
group they study (already verified and cited in full in `research/dossiers/01-momentum-reversal.md`
item 24 — cross-referenced, not re-derived here), a finding whose significance for *this* chapter is
what it implies about the historical arc rather than the level: the paper's own sample window
(1998–2011) is precisely the window in which algorithmic and high-frequency market-making capacity in
US equities grew from a marginal presence to the dominant supplier of intraday liquidity — NSE's own
colocation facility, discussed in §B.6 below, deliberately imported this same infrastructure model
into India starting in 2009, roughly at the sample's midpoint. The mechanism this implies is
straightforward and consistent with both Campbell-Grossman-Wang's (1993) and Nagel's (2012)
equilibrium accounts: as dedicated, low-latency capital enters the market-making business at scale,
the compensation required to supply liquidity falls (more competitive supply of the same service),
and the reversal premium — which is precisely the compensation for that service — should compress.
This is exactly the qualitative pattern the transaction-cost literature's chronology traces: an
anomaly documented as economically large and only "plausibly" cost-robust in 1990 (Lehmann's own
phrase, §A.1) is, by the time Frazzini-Israel-Moskowitz study it with live 2000s-2010s institutional
data, the *most* cost-constrained anomaly in their entire cross-section — not because the underlying
mechanism disappeared, but because the population of professional counterparties willing and able to
supply the same service at lower cost grew enormously over exactly this period.

### B.2 Nagel's VIX-conditional spikes: 2008 and 2020 as the mechanism's own stress tests

If the reversal premium is genuinely priced as compensation for liquidity provision under capital
constraint, the two cleanest out-of-sample tests of that claim, relative to Nagel's (2012) original
sample, are the two most severe systemic liquidity-constraint episodes global markets have since
produced: the 2008 Global Financial Crisis and the March 2020 COVID liquidity shock. Both episodes
share the structural signature Nagel's mechanism predicts and this program's own vaulted-data work
has independently corroborated on adjacent signals: **FS-U1 and FS-U2** (`research/register/
trial-ledger.md`, 2026-09-02) demonstrate, on this program's own India-market-factor and gold series,
that volatility clustering — the same VIX-adjacent state variable Nagel's regression conditions on —
is a Tier-A, cross-asset-replicated fact even after monthly aggregation; and **M4**, this program's
own crash-guard validation on real US months, finds the crash-guard-ON regime carries a mean return
of **−2.19%/month (n=95)** against **+1.81%/month OFF (n=1069)** — precisely the "danger concentrates
in the stress state" signature Nagel's VIX-conditioning predicts for a *different* signal
(momentum crashes rather than reversal spikes), cited here as a directly analogous, already-completed
piece of this program's own evidence for how severely a fast-layer premium's magnitude and its
capital-availability regime are intertwined. [VERIFY: a dedicated, India-specific magnitude estimate
of reversal-strategy returns conditioned on India VIX during the 2008 and 2020 episodes specifically
— no such India study was located in this search, and this chapter states the global Nagel (2012)
mechanism and this program's own analogous crash-guard evidence as the relevant priors, explicitly
not as an India-specific reversal magnitude, consistent with atlas 5.4's own "zero India magnitude
studies" line.] The honest reading, consistent with Part A.3's cost-knife argument: even where the
*mechanism* is confirmed at its most extreme (VIX spikes genuinely do widen the price of immediacy),
the episodes in which the premium is largest are the same episodes in which a weekly-cadence,
EOD-data desk is least equipped to react fast enough to collect it — the premium's own conditional
structure works against exactly the architecture this program has chosen.

### B.3 The weekend effect's published-then-vanished arc

Part A.4 already establishes the mechanics of the weekend effect's collapse (Sullivan-Timmermann-
White's full-universe bootstrap); this subsection states the arc as a single cross-country case,
because the shape of it — discovery, decade of replication, then evaporation under a corrected
statistical test — is the archetype this program invokes every time a fast, mechanism-free calendar
pattern is proposed. French (1980) and Gibbons-Hess (1981) independently confirmed the same negative-
Monday pattern using different samples and methods within a year of each other, which is exactly the
kind of cross-replication that, absent a corrected multiple-testing framework, looks like the
strongest possible confirmation an anomaly can receive. Sullivan-Timmermann-White (2001) then showed,
using a full century of data and a statistically rigorous accounting of the *entire* universe of
comparable rules a researcher could have tried, that this apparent confirmation was largely an
artifact of not correcting for exactly how many candidate rules the profession, collectively, had
implicitly searched over the preceding decades. No mechanism was ever proposed for the weekend effect
that survived this correction — settlement-cycle stories, Friday-good-news/Monday-bad-news reporting
asymmetries, and short-seller unwind stories were each offered and each failed to generalize once
tested rigorously out of the sample that produced them. This is the single cleanest illustration
available of why atlas §8's rejected list treats "month-of-year / day-of-week seasonals" as "the
canonical data-mining trap" (`docs/CYCLE_ATLAS.md` line 160) rather than as an anomaly this program
merely lacks the data to test — the data to test it exists in abundance, has been tested exhaustively
by the profession at large, and the honest reading of that record is a rejection this program inherits
rather than one it needs to re-derive.

### B.4 India case one — the 2009 upper-circuit day, argued as a reversal caricature

India's own public record offers a case that plays out the reversal trade's logic almost as a
laboratory experiment, and this chapter argues it fully rather than merely citing the print already
on record elsewhere in this program. On **18 May 2009**, following the UPA's return to power with a
much larger, Left-independent mandate — the mirror image of the shock discussed in §B.5 below — the
Sensex and Nifty hit their **first-ever upper circuit** within roughly thirty seconds of the Monday
opening, freezing trading for about an hour; on reopening, the market immediately ran into a **20%
upper-circuit band**, and trading was **suspended for the remainder of the day**, with the session's
final print a gain of roughly **17.3%** on the prior close (Sensex closing at 14,284.21, up 2,110.79
points) [Verified via search; this event and its verification are also on record in
`research/cycles/political-close/partABC-fold-rejects.md` §A.1, cross-referenced and not
re-verified independently here]. Read as a reversal caricature rather than as the political-calendar
object that program's own political-close chapter already argues it as: a naive one-day-reversal
trader, observing that Indian equities had fallen sharply into the 13 May-to-18 May window on
pre-election uncertainty, might have wanted to be long precisely the names that had fallen hardest —
and would, on this one day, have been rewarded spectacularly, because the move **did mean-revert**,
in the most extreme and immediate form this market's own history records. But the mean-reversion here
has nothing to do with the liquidity-provision mechanism Part A.2 formalizes: no market maker was
compensated for absorbing unwanted selling pressure at a temporarily depressed price; the entire move
was driven by the release of political information (a decisive, coalition-stable mandate resolving
weeks of uncertainty) that changed the *fundamental* expected discount rate applied to Indian
equities, not a transient liquidity dislocation. A signal construction that could not distinguish
these two economically opposite objects — genuine information arriving and being priced in
permanently, versus a transient liquidity-driven overshoot with no informational content, temporarily
mispricing a security before predictable capital arrives to correct it — would have profited
identically from both, and this is exactly the confound atlas 5.4's own zero-return-budget verdict is
built to guard against: a mechanical 1-month, or even 1-week, reversal rule applied blindly to Indian
equities across 2009 would have picked up this print as validation of its own thesis, when the
correct economic reading is that nothing about the episode has anything to do with the compensated-
immediacy story Nagel (2012) and Cheng et al. (2017) formalize.

### B.5 India case two — the 2024 election day, argued as the opposite caricature

The 2024 general-election result day offers the case's mirror image, and the contrast between the two
is the entire lesson. On **4 June 2024**, exit polls implying a large NDA landslide gave way to an
actual count showing the BJP short of a standalone majority, requiring coalition partners; the Sensex
fell an intraday low of roughly **−7.4%** before closing down 4,390 points (**−5.74%**), and the
Nifty 50 closed down 1,379 points (**−5.93%**) [Verified via search; also on record in this program's
own `research/cycles/political-close/partABC-fold-rejects.md` §A.1, cross-referenced]. Unlike the
2009 print, this move **did** partially reverse in the manner a naive reversal trader would expect —
and did so quickly: the very next session (5 June 2024), as the BJP secured firm coalition
commitments from its two major allies (TDP, JD(U)), the Sensex closed **up 2,306 points (+3.2%)** to
74,385 and the Nifty50 closed **up 736 points (+3.36%)** to 22,620 [Verified via search], with
independent press coverage headlining the broader arc as a "rebound from election-result day setback"
that left the Nifty **up roughly 11% within one month** [Verified via search]. Compare this to the
2004 case discussed in the political-close chapter and re-examined here for its reversal content: on
**17 May 2004**, the Sensex fell **15.52%** on the NDA's surprise defeat, with the initial intraday
collapse partially offset **within the same session** by state-run financial institutions buying in
at the finance ministry's request, reversing "nearly half the losses suffered in early trading"
[Verified via search] — but the *multi-day* recovery that followed was materially slower than 2024's:
public reporting places the Sensex's return to the 6,000-point level only by **2 June 2004**, roughly
two weeks after the crash, following a sustained period of continued volatility and a series of
market-reassuring signals (cabinet composition, the incoming government's own statements on reform
continuity) rather than a single next-day resolution [Verified via search]. Placed side by side, the
two most violent political-surprise sessions in India's post-liberalization market history produced
opposite reversal signatures on almost identical variables: 2009's move (a positive surprise resolving
uncertainty) did not reverse at all — it *was* the fundamental repricing, full stop, with no
subsequent giveback; 2004's move (a negative surprise) partially reversed intraday but took roughly
two weeks, not one session, to fully recover, driven by a sequence of credible policy reassurances
rather than a mechanical liquidity-provision bounce; and 2024's move (a negative-then-resolved
surprise) reversed sharply within a single subsequent session, as the specific uncertainty that drove
the initial fall (coalition viability) was itself resolved within twenty-four hours. **None of these
three is the liquidity-provision reversal Part A.2 formalizes**, and a mechanical reversal signal
applied naively across all three would have produced three different outcomes for reasons entirely
unrelated to the mechanism it claims to harvest — which is precisely why atlas 5.4 restricts the
flag's "only legitimate job" to informing entry timing on positions the book already wants for other
reasons (`research/cycles/fastlayer-close/partDH-close.md` Part D), never to standing as an
independent signal on episodes whose true driver is information arrival, not transient illiquidity.

### B.6 STT's regime history and what it does to high-turnover anomalies

India's Securities Transaction Tax was introduced by the Finance Act, 2004, effective **1 October
2004**, under then-Finance Minister P. Chidambaram, explicitly to address capital-gains tax avoidance
by taxing the transaction itself rather than relying solely on gains reporting [Verified via search].
The original rate structure taxed delivery-based equity at **0.125%** and intraday (non-delivery)
equity at **0.025%**, with derivatives (futures and options) taxed at **0.017%** [Verified via
search]. The 2013 Union Budget, following sustained industry pressure from brokers and the trading
community, **reduced** the delivery-equity rate to its current **0.1%** (levied on both the buy and
sell leg, for a 20 bps round trip), cut the futures rate to **0.01%** on the sell side only, and cut
the equity-options rate to **0.05%** on the sell-side premium [Verified via search]. [VERIFY: the
complete, dated sequence of every intermediate STT revision between the 2004 introduction and the
2013 cut, and every derivatives-side revision since — `config/costs.yaml`'s own decay note flags "two
hikes in 18 months" on the statutory side without dating them precisely, and this chapter's search
this pass located the introduction, the original rates, and the 2013 cut with confidence but not a
complete year-by-year ledger of every subsequent adjustment.] The regime's consequence for a
high-turnover strategy is arithmetic rather than a matter of interpretation, and Part A.3 already
states it in full: 20 bps round trip on cash delivery, applied to a strategy whose own construction
(monthly full-decile reformation) implies annual one-way turnover measured in multiples of 1,000%,
consumes a return budget on the order of low single-digit percentage points of NAV per year from the
statutory leg alone — a drag with **no developed-market analogue** in either the Avramov-Chordia-
Goyal (2006) or Novy-Marx-Velikov (2016) cost accounting, both of which price commissions, spread, and
impact but never a transaction tax that cannot be reduced by any change in execution technique.

### B.7 SEBI's own evidence that speed is where retail loses

The regulator's own recent research supplies the cleanest domestic evidence available that
concentrated, high-frequency trading activity in India is systematically a losing proposition for the
retail participants drawn to it, and it bears directly on this chapter's operator-psychology theme
(Part G) even though its subject is F&O rather than cash-equity reversal. SEBI's **July 2025**
equity-derivatives study found that **nearly 91% of individual traders incurred net losses in FY25**,
with aggregate individual-trader net losses of roughly **₹1.06 lakh crore**, up 41% from FY24
[Verified via search] — extending an earlier, September-2024 SEBI update that found **93% of
individual traders** incurred losses in equity F&O across **FY22–FY24**, with aggregate losses
exceeding **₹1.8 lakh crore over the three years** [Verified via search; both figures also cited, for
a different purpose — the retail-participation-wave candidate H57 — in this program's own atlas §3.6
and the register's own trial-ledger entries under Band 3, cross-referenced rather than re-derived].
The expiry-day concentration finding is the piece most directly relevant to this chapter's own
subject: SEBI's study found **59% of index-options turnover occurred on the expiry day itself**, with
**roughly 75% occurring within one day of expiry** [Verified via search] — i.e., the overwhelming
majority of retail speed-game activity concentrates in exactly the highest-velocity, shortest-horizon
window the market offers, and the same study's own loss statistics show that concentration
correlating with, not offsetting, the aggregate loss rate. Subsequent regulatory measures — raising
the minimum contract value for index derivatives, restricting weekly expiries to one benchmark index
per exchange, requiring upfront premium collection, and adding expiry-day safeguards, phased in across
late 2024 through mid-2025 [Verified via search] — reduced the loss *rate* only modestly (to roughly
**87.7%** of individual traders still losing, per the same reporting lineage) [Verified via search],
which is itself an instructive result: restricting *entry* to the fastest game does not, by itself,
make the remaining players profitable, because the structural disadvantage retail traders face
against professional counterparties at that speed is not primarily a participation-threshold problem.
This is the regulator's own evidence, independent of any academic reversal or microstructure
literature, for exactly the claim Part G's counterparty-identification argument makes theoretically:
speed is where the desk this program is building would be a *retail-shaped* counterparty against
professional liquidity providers, and SEBI's own data on who actually wins that specific game is
unambiguous.

### B.8 NSE's colocation ecosystem: the immediacy premium, already professionally harvested

The institutional fact that completes this chapter's case for atlas 5.4's zero-return-budget verdict
is the identity of the counterparty a reversal strategy would actually be competing against inside
India's own market structure. NSE launched its **colocation** service in **August 2009** [Verified via
search] — allowing brokers and high-frequency trading firms to house their own servers physically
inside NSE's own data centre, reducing network latency to the exchange's matching engine to a few
milliseconds or less, a difference that is economically decisive at the trading frequencies immediacy
provision requires even though it is imperceptible to a human trader [Verified via search]. The
facility's own regulatory history — allegations of preferential access between 2012 and 2014, a 2015
whistle-blower complaint, and a long-running SEBI enforcement action that initially ordered the
exchange to disgorge roughly ₹625 crore before SEBI itself later dropped the charges against NSE and
several former officials [Verified via search] — is cited here not for its own sake but for what it
confirms about the stakes: regulators, brokers, and the exchange itself have spent over a decade
litigating exactly how valuable microsecond-level execution priority is in this market, a level of
institutional attention and capital commitment no EOD-data, weekly-cadence research program could
plausibly match or needs to. The direct consequence for atlas 5.4: whatever compensation exists for
being the marginal supplier of immediacy in Indian equities — the liquidity-provision premium Nagel
(2012) and Cheng et al. (2017) formalize — is being competed for, in real time, by exactly the
colocated, latency-optimized market-making capital this infrastructure exists to house. This is the
concrete, India-specific instance of Part B.1's US structural argument: the population of professional
counterparties able to supply liquidity faster and cheaper than any weekly-cadence book grew up
*inside the exchange's own data centre*, and the honest reading of atlas 5.4's verdict is that this
program is not choosing to forgo an unclaimed premium — it is declining to compete for a premium that
is already being actively, professionally harvested by counterparties this program's own architecture
was never built to out-race.

---

## Part C — India data engineering: what MR1 needs, and what stays unbuilt

### C.1 What MR1 needs when bhavcopy lands

`research/register/trial-ledger.md`'s "Design MR1" entry (2026-09-02) is already the binding
specification for this grading path, and this section restates its requirements in data-engineering
terms rather than repeating its acceptance language verbatim. Building the flag correctly — so that a
future freeze-or-unfreeze decision is trustworthy rather than an artifact of a sloppy construction —
requires each of the following, none of which exists yet and none of which this chapter builds:

- **Point-in-time NIFTY-750 membership.** The reversal decile construction must be run on the
  universe as it was actually knowable on each historical rebalance date, not on today's constituent
  list projected backward — the identical point-in-time discipline Known Prior #7 (Contract §7)
  already states as decisive for the fundamentals book ("a price-only, genuinely point-in-time factor
  book is the only instrument that can answer the central question"), applied here to membership
  rather than to restated financial statements. A name that exits the index (delisting, demotion
  below rank 750, acquisition) must remain in the historical universe for every date on which it was
  actually a live constituent, and must exit the universe only from its actual exit date forward.
- **Survivorship handling.** Directly downstream of point-in-time membership: any name that
  delisted, was suspended, or was acquired must contribute its actual, realized return (including a
  delisting or suspension event, where the position could not have been exited at a clean closing
  price) to the historical decile construction, rather than being silently dropped from the sample —
  dropping failed names biases the reversal spread upward in precisely the small/illiquid tail where
  Avramov-Chordia-Goyal (2006) find the largest raw spreads concentrate, compounding rather than
  correcting the cost-fragility problem Part A.3 already identifies.
- **The liquid-half filter.** Atlas 5.4's own construction restricts the decile long-short to "the
  liquid half of NIFTY 750" (`trial-ledger.md`, Design MR1) — a direct application of Chui,
  Ranganathan, Rohit & Veeraraghavan (2023)'s already-cited India finding that the **most illiquid
  tercile shows reversal instead of continuation** even in the momentum context (`research/
  dossiers/01-momentum-reversal.md` item 16, cross-referenced), meaning an *unfiltered* reversal
  construction risks conflating a genuine liquidity-provision signal in liquid names with a
  structurally different illiquidity-driven pattern in the tail — exactly the kind of mechanism
  conflation Part B.4/B.5's case studies warn against, now at the panel level rather than the
  single-event level.
- **Decile construction at month-end with T+1 settlement alignment.** The ranking-period return and
  the holding-period entry must be aligned to when a position could actually have been established
  under India's settlement cycle — a decile formed on a month-end closing price must enter (and be
  costed) as of the next available settlement date, not the formation date itself, or the backtest
  silently assumes an execution capability the desk does not have. This is the same T+1 discipline
  this program's other price-only modules already carry, restated here because reversal's short
  holding period makes a settlement-alignment error proportionally larger than it would be for a
  12-month momentum construct.
- **The cost model per book, cited from `config/costs.yaml`.** MR1's acceptance is explicitly
  "NET of the config/costs.yaml stack per book" (`trial-ledger.md`), meaning the grading exercise
  must apply the cash-delivery round-trip figure (**[24, 32] bps all-in**, D05 F1–F4), the impact
  model's square-root-law form (`I = Y · σ_daily · √(Q/ADV)`, `Y ∈ [0.5, 1.0]`, Bouchaud/Gatheral
  order-unity universality per `config/costs.yaml`), and the ADV-by-rank-bucket table (itself flagged
  `PROVISIONAL` pending live bhavcopy medians) — separately for whichever book's turnover cap and
  capital size the flag is ever tested against, since Part A.3's cost arithmetic scales with exactly
  these book-specific parameters and a single cost figure cannot honestly stand in for all three
  books simultaneously.
- **The two-half-sample-plus-decay-haircut acceptance, already registered.** MR1's own bar —
  "net-of-cost spread > 0 across BOTH halves of the sample AND survives the McLean-Pontiff haircut"
  (`trial-ledger.md`) — is not this chapter's to loosen or restate more favorably; it is cited here
  only to note that it applies McLean & Pontiff (2016)'s general post-publication decay framework
  (Contract §5, already the program's governing citation) to a signal with, per atlas 5.4's own
  words, "zero India magnitude studies" behind it — meaning MR1 is simultaneously the *first* India
  test of this specific horizon and a test already pre-committed to the same skeptical discount this
  program applies to every well-documented, heavily-arbitraged anomaly, a deliberately higher bar
  than a novel signal with no decay history would otherwise face.

### C.2 What is deliberately not built, and why

Part E of the companion document is explicit, and this chapter quotes it in full rather than
paraphrasing, per the instruction that this entry cross-reference rather than duplicate or contradict
the principal's own reasoning: "5.4's flag machinery, if MR1 ever unfreezes it, is a one-line
percentile rank on the existing expanding-percentile utility — deliberately NOT built today: building
instruments for frozen signals invites their use (the same reasoning that kept flow-momentum out of
the FPI module's API)" (`research/cycles/fastlayer-close/partDH-close.md`, Part E). The data-
engineering consequence of this sentence is concrete: no reversal-percentile function, no liquid-half
filter implementation, no decile-construction script exists in this program's codebase as of this
writing, and none should be written before bhavcopy actually lands and MR1's own pre-registration is
formally opened for execution — not because the specification above is unclear (it is not), but
because an *available* instrument for a *frozen* signal is a standing invitation for exactly the
psychological failure Part G names: a researcher under deadline pressure, with the machinery already
built and sitting idle, finding it easier to run "just to see" than to hold the freeze until the data
and the pre-registered acceptance bar are both genuinely in place. The FPI-module precedent this
sentence cites (flow-momentum kept out of that module's API despite the underlying data existing) is
the same discipline applied consistently across this program, not a one-off decision specific to
reversal.

### C.3 Day-of-week: nothing to engineer, and the CW3/GS1 precedent for why

Atlas 5.5's reject verdict, and Part A.4's argument for it, together imply a data-engineering
consequence distinct from 5.4's: **no design is registered, no acceptance bar is pre-declared, and no
future bhavcopy pull is earmarked for testing day-of-week or expiry-day seasonality in isolation** —
the companion document states this precisely: "No trial is spent — CW3/GS1 already demonstrated the
omnibus discipline at monthly resolution, and a daily demonstration would require the bhavcopy vault
to prove a negative the register already prices at zero" (`research/cycles/fastlayer-close/
partDH-close.md`, Part D). The **CW3** trial (`research/register/trial-ledger.md`, 2026-09-02) is the
directly relevant precedent, and its own pre-registered interpretation rule is worth restating here
because it is the template this program would apply to any future daily-resolution proposal on the
identical topic: a Kruskal-Wallis omnibus across the twelve calendar months on this program's own
India market-factor data returned **H = 12.13, p = 0.354** — "no calendar structure" — but the trial's
own pre-declared rule states explicitly that even a *significant* print (p < 0.05) would **not**
overturn the reject, because Contract §8's mechanism ban on fixed-period calendar cycles and the
Sullivan-Timmermann-White multiple-testing correction (§A.4 above) both operate independently of
whatever any single omnibus test happens to show; a twelve-way comparison expects roughly 0.6 false
positives at the 5% level purely by chance, so a marginal print earns dissection and logging, never
promotion (`trial-ledger.md`'s own phrase: "the print is logged and dissected, promoted NEVER").
**GS1** (also 2026-09-02) ran the identical demonstration on gold's monthly seasonality
(**H = 10.87, p = 0.454**, float era 1972–2026), confirming the same discipline generalizes across
asset classes rather than being an artifact specific to India equities. The consequence for this
entry: 5.5 requires no bhavcopy pull, no daily-resolution CW3-style rerun, and no MR1-style
pre-registered acceptance bar, because the reject does not rest on an absence of data at the
resolution where a day-of-week effect would need to show up — it rests on the mechanism-free
Sullivan-Timmermann-White argument Part A.4 already makes in full, a reject this program inherited
correctly and, per Contract §9's rule against re-testing rejected ideas with tweaked parameters,
should not spend a trial re-deriving at finer resolution merely because finer data eventually becomes
available.

---

## References

Jegadeesh, Narasimhan (1990), "Evidence of Predictable Behavior of Security Returns," *Journal of
Finance* 45(3): 881–898 [Verified via search]. · Lehmann, Bruce N. (1990), "Fads, Martingales, and
Market Efficiency," *Quarterly Journal of Economics* 105(1): 1–28 [Verified via search]. · Campbell,
John Y., Grossman, Sanford J. & Wang, Jiang (1993), "Trading Volume and Serial Correlation in Stock
Returns," *Quarterly Journal of Economics* 108(4): 905–939 [Verified via search]. · Nagel, Stefan
(2012), "Evaporating Liquidity," *Review of Financial Studies* 25(7): 2005–2039 [Verified via
search]. · Cheng, Si, Hameed, Allaudeen, Subrahmanyam, Avanidhar & Titman, Sheridan (2017),
"Short-Term Reversals: The Effects of Institutional Exits and Past Returns," *Journal of Financial
and Quantitative Analysis* 52: 143–173 [already verified in full, `research/dossiers/
01-momentum-reversal.md` item 22 — cross-referenced, not re-verified here]. · Avramov, Doron, Chordia,
Tarun & Goyal, Amit (2006), "Liquidity and Autocorrelations in Individual Stock Returns," *Journal of
Finance* 61(5): 2365–2394 [Verified via search]. · Novy-Marx, Robert & Velikov, Mihail (2016), "A
Taxonomy of Anomalies and Their Trading Costs," *Review of Financial Studies* 29(1): 104–147
[Verified via search]. · Frazzini, Andrea, Israel, Ronen & Moskowitz, Tobias (2012/2018 rev.),
"Trading Costs of Asset Pricing Anomalies" [already verified in full, `research/dossiers/
01-momentum-reversal.md` item 24 — cross-referenced, not re-verified here]. · French, Kenneth R.
(1980), "Stock Returns and the Weekend Effect," *Journal of Financial Economics* 8(1): 55–69
[Verified via search]. · Gibbons, Michael R. & Hess, Patrick (1981), "Day of the Week Effects and
Asset Returns," *Journal of Business* 54(4): 579–596 [Verified via search]. · Sullivan, Ryan,
Timmermann, Allan & White, Halbert (2001), "Dangers of Data Mining: The Case of Calendar Effects in
Stock Returns," *Journal of Econometrics* 105(1): 249–286, using the stationary block bootstrap of
Politis, Dimitris N. & Romano, Joseph P. (1994) [Verified via search]. · Wood, Robert A., McInish,
Thomas H. & Ord, J. Keith (1985), "An Investigation of Transactions Data for NYSE Stocks," *Journal of
Finance* 40(3): 723–739 [Verified via search]. · Admati, Anat R. & Pfleiderer, Paul (1988), "A Theory
of Intraday Patterns: Volume and Price Variability," *Review of Financial Studies* 1(1): 3–40
[Verified via search]. · Chui, Andy C.W., Ranganathan, Kavitha, Rohit & Veeraraghavan, Madhu (2023),
"Momentum, Reversals and Liquidity: Indian Evidence," *Pacific-Basin Finance Journal* 82: 102193
[already verified in full, `research/dossiers/01-momentum-reversal.md` item 16 — cross-referenced,
not re-verified here]. · McLean, R. David & Pontiff, Jeffrey (2016), "Does Academic Research Destroy
Stock Return Predictability?" *Journal of Finance* 71: 5–32 [already verified, Contract §5 and
`research/dossiers/01-momentum-reversal.md` item 10 — cross-referenced]. · Press reporting (NBC News,
WorldScientific *Fluctuation and Noise Letters* "A Brief Analysis of May 2004 Crash in the Indian
Market," Business Standard) on the 17 May 2004 Sensex crash (−15.52%, dual circuit-breaker halts,
same-day partial intraday recovery via state financial-institution buying, ~two-week recovery to the
6,000 level by 2 June 2004) [Verified via search]. · Press reporting (per `research/cycles/
political-close/partABC-fold-rejects.md` §A.1, cross-referenced and not re-verified independently
here) on the 18 May 2009 upper-circuit day (first-ever upper circuit within ~30 seconds of the open,
20% band, session suspended, close +2,110.79 points to 14,284.21, ≈+17.3%) [Verified via search]. ·
Business Standard, HDFC Sky, Gulf News reporting on the 4–5 June 2024 election-result sessions (Sensex
−4,390pts/−5.74% on 4 June, Nifty −1,379pts/−5.93%; Sensex +2,306pts/+3.2% and Nifty +736pts/+3.36% on
5 June; Nifty up ~11% within one month) [Verified via search]. · Fyers, ICRIER Working Paper 273
(Neha Malik), 5paisa, and related tax-guide sources on the Securities Transaction Tax's introduction
(Finance Act 2004, effective 1 October 2004, original delivery-equity rate 0.125%) and its 2013
revision (delivery-equity cut to 0.1%, futures to 0.01% sell-side, equity options to 0.05% sell-side
premium) [Verified via search]. · SEBI press release (September 2024), "Updated SEBI Study Reveals
93% of Individual Traders Incurred Losses in Equity F&O between FY22 and FY24; Aggregate Losses Exceed
₹1.8 Lakh Crores Over Three Years" [Verified via search, sebi.gov.in]. · SEBI's July 2025 equity-
derivatives study (as reported by Open, Moneylife, and related coverage): ~91% of individual traders
net losers in FY25, aggregate individual losses ~₹1.06 lakh crore (+41% YoY); 59% of index-options
turnover on expiry day, ~75% within one day of expiry; post-curb loss rate ~87.7% [Verified via
search]. · NSE static page ("Co-location Facility"), Vajiram & Ravi, DatacenterDynamics, IRCCL
("From Co-location to Kill Switches: Analyzing India's HFT Framework") on the August 2009 NSE
colocation launch and its 2012–2014/2015 preferential-access enforcement history (SEBI's initial
₹624.89 crore disgorgement order, later dropped) [Verified via search]. · `research/CONTRACT.md`
§§1, 4, 5, 8, 9, 12. · `docs/CYCLE_ATLAS.md` §0, rows 5.1–5.6, §7 (the rejected list), §11.1 (the
mean-reversion horizon sandwich). · `research/cycles/fastlayer-close/partDH-close.md` (Parts D, E, F,
H — the principal's own document, cross-referenced throughout, never re-derived). · `research/
register/trial-ledger.md` (CR2, CW1, CW2, CW3, GS1, FS-U1, FS-U2, M4, and the Design MR1 entry
itself). · `config/costs.yaml` (D05 F1–F4, the cash-delivery and impact-model cost stack). ·
`research/dossiers/01-momentum-reversal.md` (the momentum/reversal dossier, cross-referenced for
Cheng et al. 2017, Frazzini-Israel-Moskowitz, and Chui et al. 2023, none re-derived here). ·
`research/cycles/political-close/partABC-fold-rejects.md` (the 2004/2009/2024 election-day
verifications, cross-referenced for the 2009 print specifically). · `docs/CYCLE_ATLAS.md` line 163
(the options-premium-harvesting rejection, D12, cited in Part G as the precedent this chapter's own
counterparty-identification argument generalizes).
