# Calendar as Signal — Atlas 4.1/4.2/4.11/4.12 (Parts A, G, B, C)

*Monograph #33 in the cycle-research series · v1.0 · 2026-09-02 · Author: Claude (research agent)
for Ionic quant desk (principal: gaurav@ionic.in) · governed by `research/CONTRACT.md`.*

**Verdict up front.** Four calendar hypotheses share one question — does a fixed date carry
information, or does it merely look like it does once averaged over enough Septembers? — and this
chapter answers it four different ways because the four dates are four different mechanisms, not
four instances of one phenomenon. Atlas **4.1** (Union Budget window) is a **REGIME seat, L5,
vol-scheduling only**: the Budget's date is fixed by constitutional convention and its content is
legally undisclosed until the Finance Minister rises to speak, which is exactly the timing-
certainty/content-uncertainty structure that prices a volatility premium around scheduled
announcements everywhere in the world — but the seat's authority rests on the **daily**-resolution
India VIX record and that mechanism, not on this desk's own monthly print: **CW1 FAILED** (Feb
median |MF| = 4.27 vs non-Feb 4.22, rank 7/12, one-sided Mann-Whitney p = 0.522), because a 1–3 day
event is invisible at monthly resolution, and the monograph says so without borrowing false comfort
from the daily literature it cannot itself recompute here. Atlas **4.2** (fiscal-year-end April
small-cap reversal) is the register's one genuine calendar **EDGE hypothesis with a named
mechanism** — India's tax year ends 31 March, tax-motivated loss-selling depresses small caps into
the close of the fiscal year, and the position mean-reverts in April — and it is also the register's
cleanest illustration of *instrumented, not promoted*: **CW2 PASSED** cleanly (April median SMB =
+2.47, rank 1/12, p = 0.020) and PROMOTION WAS STILL REFUSED, because a mechanism-consistent
monthly print is not the same evidentiary object as a cost-net paper-trade record, and this desk
does not conflate the two even when the print is this clean. Atlas **4.11** (month-of-year
seasonals generally) is **REJECTED — confirmed by evidence, not merely by contractual fiat**:
**CW3**'s omnibus (Kruskal-Wallis H = 12.13, p = 0.354 across the 12 months of MF) found no
calendar structure, which is precisely the demonstration the trial was pre-registered to run, and
its own false-positive-rich internal detail (November ranks #1 in |MF|, December ranks #1 in
median MF, in that same sweep) is the chapter's live specimen of the Slutzky trap the omnibus
exists to guard against. Atlas **4.12** (dividend season) is **REJECTED by mechanism** — the
ex-dividend price adjustment is a near-arbitrage-free accounting identity, priced by the tax
wedge between dividend and capital-gains treatment, and there is no seasonal residual left to
harvest once that identity is netted out. Every number cited from this desk's own record below is
reproduced **verbatim** from `research/cycles/calendar/calendar-RESULTS.md` and
`research/register/trial-ledger.md` (entries CW1–CW3, PL1) — this chapter recomputes nothing and
invents no new desk statistic.

**Cross-reference discipline, stated once and then honored throughout.** This chapter owns, at
teaching depth: the event-study/tax-loss-selling/Slutzky/scheduled-vol-premium/dividend-pricing
theory underlying every calendar-shaped hypothesis in the atlas (Part A); the psychology of why a
desk that has just rejected long clocks must reject short ones with the same instrument (Part G);
the cross-country and India case record for calendar-as-signal claims (Part B); and the concrete,
free-source India data pipeline for every claim this family of hypotheses could ever test (Part C).
It does **not** re-derive the political/election-cycle direction-is-surprise math (owned by Atlas
row 3.7 and trial PL1, cited here only by its one-line result: pre-window sign predicted the
result-month sign in **3/8** cases, at/below coin-flip); it does not re-litigate L2's fast
volatility-clustering seat, the crowding/quant-unwind monitor (CR1–CR2), or the momentum composite's
own reversal-contamination discipline — those are separate seats with their own dossiers. Every
figure below not already sourced to this desk's own ledger is search-verified as of September 2026
or explicitly tagged `[VERIFY: ...]`.

---

## Part A — Theory, formalized

Every calendar hypothesis this atlas entry touches reduces to one of two econometric objects: an
**event study** around a date whose *timing* is known in advance (Budget day), or a **calendar-
bucket seasonality test** across dates whose *recurrence* is claimed but whose *mechanism* must be
argued independently (fiscal-year-end, month-of-year, dividend season). This Part formalizes both
objects and the two structural theories — tax-motivated trading and scheduled-announcement risk
pricing — that are the only mechanisms Contract §8 will accept as a reason a calendar pattern is
allowed to survive scrutiny.

### A.1 Event-study econometrics: the market model, abnormal returns, and the variance ratio around scheduled announcements

The modern event study begins with **Ball & Brown (1968)**, "An Empirical Evaluation of Accounting
Income Numbers," *Journal of Accounting Research* 6(2): 159–178 — the paper that first showed
earnings announcements carry price-moving information by comparing realized returns around the
announcement date to a benchmark return the stock "should" have earned absent the announcement.
That comparison is the entire logical apparatus every Budget-day or FOMC-day study since has
inherited. Formally: pick a **market model** estimated over a clean estimation window that excludes
the event,

  R_it = α_i + β_i · R_mt + ε_it,

fit by OLS to recover (α̂_i, β̂_i), then define the **abnormal return** on any day t in the event
window as the realized return net of what the model would have predicted given the market's move
that day:

  AR_it = R_it − (α̂_i + β̂_i · R_mt).

Summing abnormal returns over an event window [t1, t2] gives the **cumulative abnormal return**,

  CAR_i(t1, t2) = Σ_{t=t1}^{t2} AR_it,

and averaging CAR_i across N events (N stocks around one Budget day, or one stock across N Budget
days) gives the cumulative *average* abnormal return, CAAR(t1, t2) = (1/N) Σ_i CAR_i(t1, t2), tested
against zero with a standard Brown-Warner-style t-statistic using the cross-sectional or
time-series standard deviation of CAR estimated from the clean pre-event window. This is the
instrument CW1 could not properly deploy — daily abnormal returns require daily prices, and the
desk's own vaulted factor series (IIMA monthly factors, 1993-10 through 2025-12) is monthly by
construction — which is precisely why CW1's FAIL is a **resolution** verdict rather than a
**mechanism** verdict: a genuine 1–3 day CAR spike around 1 February averages away almost
completely inside a monthly observation the moment the other 27–29 trading days of February are
ordinary, and February's monthly |MF| ranking 7th of 12 (calendar-RESULTS.md) is exactly the
signature a real but short event-window effect leaves behind at the wrong sampling frequency.

The frequency-domain cousin of the same point is the **variance ratio**. Following **Lo & MacKinlay
(1988)**, "Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification
Test," *Review of Financial Studies* 1(1): 41–66, define for an aggregation length q,

  VR(q) = Var(R_t + R_{t−1} + … + R_{t−q+1}) / (q · Var(R_t)),

which equals 1 under the i.i.d. random-walk null and departs from 1 under serial dependence. Around
a *scheduled* event the variance ratio computed on intraday or daily returns produces a **localized
kink** — realized variance is sharply elevated in the narrow window straddling the known date and
close to flat immediately outside it — which is qualitatively different from the smoothly rising
VR(q) that under-reaction/momentum diffusion produces (§B.11 of the atlas's momentum chapter, not
recapitulated here). The kink is the signature of "the market knows exactly *when* it will learn
something and prices that certainty," which is the entire content of **Savor & Wilson (2013)**,
"How Much Do Investors Care about Macroeconomic Risk? Evidence from Scheduled Economic
Announcements," *Journal of Financial and Quantitative Analysis* 48(2): 343–375: across scheduled
CPI, employment, and FOMC announcements in the US, 1958–2009, the average excess stock return on
announcement days was **11.4 basis points versus 1.1 basis points on all other days** — a
compensated risk premium for holding systematic macro-news risk over a date investors know is
coming, not a directional forecast of what the news will say. The India Budget is the same
structure wearing a fiscal-policy costume: the date is fixed by law (indiabudget.gov.in publishes
it annually, in advance, without ambiguity), the content is genuinely undisclosed until the Finance
Minister speaks (Budget secrecy — the "halwa ceremony" media ritual each January exists precisely
because leak risk is taken seriously), and the Savor-Wilson logic transfers directly: a premium for
bearing the announcement's risk, priced ex ante, resolved (in direction) only ex post. That transfer
is the entirety of L5's justification, and it is a **literature-plus-mechanism** argument, not a
desk-print argument — CW1 tested for the print and correctly reported that the print does not exist
at monthly resolution, which is the honest, narrower claim.

### A.2 The tax-loss-selling hypothesis, formalized — and its India mapping

The mechanism is a simple optimal-tax-trading argument, but it earns Tier status only because it has
been identified causally, not merely observed as a correlation. **Ritter (1988)**, "The Buying and
Selling Behavior of Individual Investors at the Turn of the Year," *Journal of Finance* 43(3):
701–717, shows directly in US brokerage data that individual investors' buy/sell ratio is
below-normal in late December and above-normal in early January, and that year-to-year variation in
the early-January buy/sell ratio explains **46%** of the year-to-year variation in the turn-of-year
return effect over 1971–1985 — the mechanism is not inferred from prices alone, it is observed in
the *trading behavior* that supposedly produces the price pattern. **Roll (1983)**, "Vas ist das?
The Turn-of-the-Year Effect and the Return Premia of Small Firms," *Journal of Portfolio Management*
(Winter): 18–28, locates the effect precisely at the boundary of the tax year (the last trading day
of the old year and the first several of the new one) and shows it is disproportionately a
*small*-firm phenomenon — small, illiquid names are exactly the names in which price-insensitive,
tax-motivated selling has the largest price impact, because there is comparatively little
arbitrage capital standing ready to absorb it. The identification that turns this from "a
correlation with a plausible story" into "a mechanism with causal evidence" is **Poterba &
Weisbenner (2001)**, "Capital Gains Tax Rules, Tax-Loss Trading, and Turn-of-the-Year Returns,"
*Journal of Finance* 56(1): 353–368: they exploit two US tax-law *changes* as natural experiments —
the 1969 reduction of the deductible fraction of long-term losses against ordinary income from 100%
to 50%, and the Tax Reform Act of 1976's extension of the long-term holding period from six months
to one year — and show that when the tax code's *incentive* to realize losses specifically before
year-end strengthened, the correlation between a stock's early-year losses and its turn-of-year
return weakened (because tax-motivated selling shifted earlier in the year), and when the incentive
was absent, the correlation was stronger. A pattern that moves *with the tax code itself*, holding
everything else about the stock and the calendar fixed, is the strongest available evidence that the
tax code — not investor superstition about January — is doing the causal work. This is exactly the
kind of "why does this survive being known?" argument Contract §5 demands, and it clears bar (i):
a structural, tax-code-driven incentive that persists precisely because it is a legal constraint on
optimal trading, not an information asymmetry that closes once discovered.

The India mapping is a derivation, not an analogy borrowed on vibes. India's financial year for tax
purposes runs 1 April to 31 March; capital losses and gains under the Income-tax Act are computed,
offset, and carried forward (short-term losses against short-term or long-term gains, long-term
losses only against long-term gains, unabsorbed losses carried forward eight assessment years but
only usable against future capital gains) on that same fiscal-year clock, for every PAN. A taxable
Indian equity investor sitting on a depressed position therefore faces the identical calendar
incentive an American investor faces on 31 December, shifted by nine months: crystallize the loss
before the fiscal year closes, inside the same assessment year as any gains it is meant to offset.
The mechanical prediction this derives — not fits — is **selling pressure concentrated in the two
months before FY-end (February–March), and a rebound concentrated in the first month of the new FY
(April)**, once the tax-motivated seller has no further reason to keep a name's price depressed.
This is exactly what this desk's own record shows: CW2's pre-registered bar (April SMB rank ≤2 of
12, median > 0, one-sided Mann-Whitney p < 0.10) was cleared cleanly — **April median SMB = +2.47,
rank 1/12, p = 0.020** — and the calendar-RESULTS.md honesty note records the selling leg as a
**post-hoc, NOT pre-registered** observation: February (−2.36) and March (−1.70) are the two most
negative SMB months in the same series, coherent with the same mechanism but tagged CW2b for a
future, separately pre-registered trial rather than claimed now. The reason the India "January
effect" analogue is specifically April, and never January, is that the tax-year anchor — not the
Gregorian new year — is what the mechanism actually depends on; this is precisely why the effect's
location moves when the fiscal calendar moves (see §B.2's UK evidence below, where an April-ending
tax year produces the effect in April rather than January, confirming the mechanism travels with
the tax code and not with any particular month's folklore).

### A.3 The Slutzky-Yule effect and the arithmetic of false "best months"

The atlas's own epistemics course (`docs/CYCLE_ATLAS.md` §0) already cites **Slutzky (1937)**,
"The Summation of Random Causes as the Source of Cyclic Processes," *Econometrica* 5(2): 105–146,
and **Yule (1927)**'s autoregressive-process work as the founding demonstration that applying a
summation or moving-average filter to pure random noise manufactures apparent periodic waves with
no underlying periodic cause whatsoever — the "cycle" is an artifact of the filter's own frequency
response, not a property of the generating process. Partitioning a return series into twelve
calendar-month buckets and reporting "the best month" is the direct descendant of the same error:
it is formally equivalent to applying twelve different band-pass selection filters to the same
series of shocks and reporting whichever filter happened to peak, and **Granger (1966)**'s companion
finding that aggregate macro time series show no privileged spectral peak at any claimed "cycle
length" — just a monotonically declining "typical spectral shape" — is the frequency-domain warning
against exactly this move.

The arithmetic is not subtle and this chapter states it because CW3 was designed to demonstrate it
rather than merely assert it. Testing k = 12 calendar-month buckets, each at a nominal α = 0.05
one-sided test for "this month differs from the rest," produces an **expected number of false
discoveries under the global null of k·α = 12 × 0.05 = 0.6** — under a genuinely flat null, a
dataset shaped exactly like this one is expected, on average, to produce more than half of one
"significant" month by chance alone, before any real structure has contributed anything. The
probability of finding **at least one** nominally significant month among twelve tests at α = 0.05,
even treating them as independent (a conservative approximation, since monthly buckets share a
common market factor and are not fully independent), is 1 − (1 − 0.05)^12 ≈ 46% — essentially a
coin flip's worth of "finding a story" with zero true signal anywhere in the data. A family-wise
(Bonferroni) correction that holds the overall Type-I rate at 0.05 across all twelve tests would
require each individual test to clear α/12 ≈ 0.0042, a bar dramatically higher than any single
month's raw p-value in this kind of series typically reaches. This is exactly why a **Kruskal-Wallis
omnibus** — one joint test statistic across all twelve groups, one p-value, computed and interpreted
under a rule written down before the number existed — is the statistically correct instrument for
"is there ANY month-of-year structure at all," rather than twelve separate tests bolted together
after the fact with an ad hoc correction applied only to the one that looked interesting. CW3's own
pre-stated interpretation rule (`p ≥ 0.05 → REJECT confirmed; p < 0.05 → REJECT still stands per
Contract §8's mechanism ban, logged as expected false-positive risk, never promoted`) is this
statistical logic converted directly into a governance rule.

The proof that this is not a hypothetical danger sits inside the desk's own CW1/CW3 numbers.
February ranks **7th of 12** in |MF| (CW1 — an entirely ordinary month for volatility), and yet in
the very same CW3 sweep, **November ranks #1 of 12 in |MF| and December ranks #1 of 12 in median
MF** — a reader hunting for patterns would "discover" both of those months as a story (a "risk-off
November," a "Santa Claus rally December") with evidentiary support no stronger than the 0.6
expected false discoveries the pure arithmetic above predicts at the 5% level across twelve buckets
— and here two rank-#1 findings already sit right at that base rate, logged and printed, never
interpreted. The omnibus (H = 12.13, p = 0.354, comfortably inside the null) is the single statistic
that stops the story from being told, and its existence — pre-registered, run, and reported
regardless of what it found — is the empirical, on-our-own-book proof of Contract §8's calendar ban:
the data-mining trap this desk is guarding against is not a textbook abstraction, it is sitting
inside the desk's own most recent print.

### A.4 The scheduled-event volatility premium: term-structure kinks, never direction

Model the implied-volatility term structure σ(τ) as reflecting the market's expectation of realized
variance accumulated over the remaining life [0, τ] of an option. Absent any scheduled information
event, this curve is smooth — near-dated implied vol typically sits at or below far-dated implied
vol in calm regimes (the classical Samuelson-effect maturity decay), rising only with the ordinary,
diffuse accumulation of uncertainty over time. A **known, dated** event that will resolve a discrete
block of uncertainty on a specific calendar date — a scheduled rate decision, a results date, a
Union Budget presentation — inserts a **localized hump or kink** in that curve exactly at the
maturity straddling the event date: options expiring just after the event must price in the
event-day variance explicitly, options expiring just before need not, and the resulting
discontinuity in σ(τ) as a function of maturity would not exist for information that arrives
diffusely rather than on a schedule. This is standard options-desk practice — "event-vol" or
"binary-event" bump pricing around earnings dates, central-bank meetings, and (in India) Budget
day and general-election result days — and it is the *pricing-side* twin of Savor & Wilson's
*realized-return* finding: the same timing-certainty/content-uncertainty structure that produces an
ex ante compensated excess return on the announcement day in the underlying also produces an ex ante
implied-volatility markup in the options market for the same day. Two markets, one risk, priced
twice.

The design conclusion this licenses for L5 is narrow by construction: **timing certainty licenses
scheduling; it says nothing whatsoever about direction.** Knowing exactly *when* the Budget will be
presented lets a desk pre-position its risk budget — reduce gross exposure, widen hedge ratios,
tighten stops — into a window it knows in advance will carry elevated event risk. It does not, by
any argument surveyed here, license a directional bet on what the Budget will say, because the
content genuinely is not known in advance (Budget secrecy is an institutional fact, not a modeling
assumption). This is precisely why `calendar_windows.py`'s public interface (`windows`,
`calendar_schedule`) returns only an `in_window` boolean, an overlap-depth count, and a `kind` trail
— never a sign — and the module's own test suite enforces this as a checked invariant rather than a
design intention that could silently erode over time: `test_no_directional_output_exists` greps the
module's public API for any name containing "direction," "signal," or "tilt" and asserts the result
is empty. The desk's own sibling measurement for the *directional* half of the same claim, on the
election window rather than the Budget window, already tested this discipline empirically and found
exactly what the theory predicts: trial **PL1** (`research/register/trial-ledger.md`) measured
whether the pre-window sign (the mean of the two months before a general-election result month)
predicts the result-month's own sign, across all eight general-election result months this desk's
event list carries, and found **3/8 agreement — at or below coin-flip**. "Direction is surprise" is
not an assumption this chapter asks the reader to accept; it is a measured property of the sibling
window this desk has already tested, and the Budget window inherits the same reduce-only design by
identical logical structure, not by analogy alone.

### A.5 Dividend capture and the no-arbitrage pricing of the ex-dividend drop

The naive "seasonal" intuition — buy before the ex-dividend date, collect the dividend, sell after —
treats the ex-date price drop as a free source of return net of the dividend received. **Elton &
Gruber (1970)**, "Marginal Stockholder Tax Rates and the Clientele Effect," *Review of Economics and
Statistics* 52(1): 68–74, supplies the no-arbitrage counter that kills this intuition analytically.
Under a marginal-investor, tax-clientele equilibrium, the ex-dividend price drop ΔP should satisfy

  ΔP / D = (1 − t_d) / (1 − t_g),

where t_d is the marginal investor's dividend tax rate and t_g their capital-gains tax rate: the
marginal (price-setting) holder must be indifferent between capturing the dividend (net of t_d) and
instead capturing the equivalent value through a pre-drop sale (net of t_g). Whenever dividends are
taxed more heavily than capital gains — the ordinary case in most tax codes across most history —
the price should fall by *less* than the full dividend amount, and clientele sorting (high-bracket
investors gravitating to low-yield, capital-appreciation stocks; low-bracket or tax-exempt investors
gravitating to high-yield stocks) pins the empirical ΔP/D ratio closer to parity for low-yield names
and further from parity for high-yield ones — precisely the pattern Elton-Gruber and the large
ex-dividend-day literature that followed it document. India's own tax treatment of dividends has, in
fact, undergone exactly the kind of tax-code change that would let a clean India study identify this
mechanism the way Poterba-Weisbenner identified the US turn-of-year effect: the Finance Act, 2020
abolished the Dividend Distribution Tax regime (under which the incidence sat with the paying
company rather than the shareholder) and reverted to taxing dividends as ordinary income in the
recipient's hands — a genuine natural experiment in the ΔP/D wedge that a future India dividend
study could exploit, and which this desk has not run (a runsheet item, not a claim made here). The
governing point for Atlas 4.12 is that the ex-date adjustment is a **mechanical, near-arbitrage-free
accounting identity** modulo that tax wedge and any short-lived liquidity effects around the record
date — there is no *net* exploitable seasonal return left over once the price drop is properly netted
against the dividend received, which is exactly the REJECT rationale the atlas states plainly:
"mechanical yield timing; priced." Of the four hypotheses this chapter examines, 4.12 is the
cleanest illustration that a real, well-documented, mechanistically-grounded calendar regularity can
still be *worthless as a trade* precisely because the mechanism that produces it is a pricing
identity, not a crowding-vulnerable premium — the opposite failure mode from 4.11's mechanism-free
seasonality, and worth holding the two REJECTs side by side for exactly that contrast.

---

## Part G — Operator psychology

Every section of Part A above is, in a narrow sense, unnecessary: a desk that has already built the
epistemics course at the front of `docs/CYCLE_ATLAS.md` — persistence, not periodicity; the clock
test; Slutzky/Yule/Granger named explicitly as the reason "an 8-year cycle" is usually a category
error — already possesses every intellectual tool this chapter needed to reject 4.11 and 4.12
on sight. The reason this Part exists anyway is that the same mind capable of holding that discipline
at the scale of a 45–60 year Kondratieff wave is not automatically immune to the identical failure
mode running at the scale of a single month, and the calendar is where that immunity gets tested
under the worst possible conditions: short feedback loops, vivid folklore, and a genuine mechanism
sitting one door down from three mechanism-free imitations that look, at a glance, exactly like it.

**The seduction of calendars is a pattern-hunger problem, not a finance problem.** Human cognition is
apophenic by default — it finds faces in clouds and, given a finite return series, it will always
find *some* calendar month, day-of-week bucket, or lunar-phase partition that happened to
outperform, because a finite series partitioned finely enough always contains a maximum. "Sell in
May and go away" long predates its academic legitimation — the saying is London-stockbroker folklore
older than any dataset that has since been built to test it — and it received serious empirical
treatment only with **Bouman & Jacobsen (2002)**, "The Halloween Indicator, 'Sell in May and Go
Away': Another Puzzle," *American Economic Review* 92(5): 1618–1635, precisely because the folklore
had circulated for generations on vibes alone, with no mechanism ever offered beyond a vague
appeal to summer illiquidity and August vacations. **Samuelson's dictum** — that markets are "micro
efficient but macro inefficient" (Paul Samuelson, "Summing Up on Business Cycles," address to the
Federal Reserve Bank of Boston conference, 1998) — is the adjacent warning from the same
intellectual tradition: individual mispricings get arbitraged away quickly by the minority who spot
them, but aggregate, index-level, broad-calendar patterns are exactly the terrain where crowding
pressure is weakest and therefore where folklore survives longest without being priced out — which
is precisely why calendar effects, of all anomaly classes, are the ones astrology-adjacent framing
gravitates to (lunar cycles, "sell in May," Mercury retrograde stock-picking columns) and precisely
why this desk cannot treat "it has a catchy name and three decades of anecdote" as evidence.

**A desk that has just rejected five long clocks must reject short ones with the same knife, or the
rejection was never principled.** Contract §7's own accounting — of 32 cycle candidates, five
survived the clock test, three of them calendar-anchored — and `docs/CYCLE_ATLAS.md` §7's visible
rejected list (Kondratieff waves, the fixed 18-year real-estate clock, Elliott Wave and Gann,
the US presidential cycle transplanted onto India) were all rejected for the *same* reason stated in
different words each time: a claimed periodicity with no mechanism that survives being known, or a
mechanism that changes from instance to instance and is therefore a label rather than a process.
Accepting "sell in April" or "the January effect, but it's India so let's call it March" on vibes
alone — no tax-code argument, no institutional-flow argument, just an observed pattern in a
backtest — would be the *identical* intellectual error committed at a different timescale, and
Contract §8's explicit ban on "fixed-period calendar cycles... unless a mechanism is named" exists
precisely to close this asymmetry before it opens: a desk cannot hold long cycles to a
decay-survival argument and let short calendar cycles skate by on pattern-matching, because the
epistemic sin is the same sin regardless of the clock's period.

**The discipline that actually blocks this is pre-naming the one month you are allowed to test,
before you have seen the number.** `research/register/trial-ledger.md`'s own language for this
entry — "PRE-REGISTERED before running... bars below written before any number was computed" — is
the operational form of the discipline. Exactly two months in this whole chapter were ever granted
a directional promotion bar, and both were named for a stated mechanism before any Mann-Whitney
p-value existed: **April**, for the fiscal-year-end tax-loss-selling hypothesis (CW2), and
**February**, for the Budget-month volatility hypothesis (CW1). Every other month — all ten of the
remainder — was reserved exclusively for the omnibus (CW3), whose entire purpose is to test the
joint null across *all twelve* months at once and thereby show, honestly, what an unconstrained
"best month" hunt across the same data would have produced had this desk not pre-registered: two
different rank-#1 findings (November in |MF|, December in median MF) sitting in the very same
sweep, neither of them named in advance, both of them therefore permanently un-promotable regardless
of how coherent a post-hoc story could be told about either. This is the register functioning
exactly as designed — not preventing the discovery of a pattern, but preventing the *promotion* of
one that arrived by the wrong evidentiary path.

**How a trader rationalizes a post-hoc month discovery, and how the register blocks each step.** The
psychological sequence is familiar to anyone who has watched a desk "discover" a seasonal edge: (1)
scan a return series across many partitions — calendar months, days of the week, festival dates,
sometimes lunar phases — until one clears a nominally impressive threshold; (2) retrofit a narrative
to the winning partition, frequently by reverse-engineering the January-effect template (tax-loss
selling, holiday liquidity, year-end window dressing) onto a month where none of those facts
actually apply locally; (3) present the retrofitted narrative as though it *generated* the test,
quietly erasing the multi-partition search that preceded it from the story told to a risk committee
or an investor. Step (3) is the load-bearing deception, and it is precisely what a written,
timestamped pre-registration makes impossible to smuggle past a second reader: the bar and the two
named months exist in `trial-ledger.md` with a stated interpretation rule *before* the Mann-Whitney
statistics existed, which means anyone auditing the desk's work later can verify, mechanically, that
the story was not built backward from the winning number. The discipline is even applied against the
desk's own most tempting finding: CW2's post-hoc observation that February and March are the two
most negative SMB months — a coherent, mechanism-consistent, genuinely interesting pattern that
this desk itself noticed — is explicitly tagged **CW2b, not claimed, and routed to a future,
separately pre-registered trial** rather than folded into CW2's promotion case. That is the rule
enforcing itself on the house's own best material: the same knife that blocks a stranger's
data-mined "best month" has to cut the desk's own post-hoc discovery too, precisely because a rule
with an exception for its own author is not a rule.

---

## Part B — Cross-country evidence and the India case record

### B.1 The US January effect: the paradigm case, and its own decay

**Keim (1983)**, "Size-Related Anomalies and Stock Return Seasonality: Further Empirical Evidence,"
*Journal of Financial Economics* 12(1): 13–32, is the paper that gave the small-firm effect its
calendar location: examining NYSE/AMEX daily abnormal returns by size decile and month, 1963–1979,
Keim found that daily abnormal-return means in January were large relative to every other month, and
that **nearly 50% of the average size effect over the full sample period was attributable to January
abnormal returns alone**, concentrated overwhelmingly in the first several trading days of the month
— the empirical fingerprint tax-motivated December selling and January reversal would leave, and the
fact that motivated Ritter's later behavioral confirmation and Roll's turn-of-year framing (§A.2
above). What makes the January effect the paradigm case for this chapter's larger argument about
decay, however, is what happened to it *after* it became famous: US size/January-effect magnitudes
documented in post-1980s samples are markedly smaller than the pre-1980 estimates that made the
effect well known, a pattern broadly consistent with — though not the specific headline number of —
**McLean & Pontiff (2016)**, "Does Academic Research Destroy Stock Return Predictability?," *Journal
of Finance* 71(1): 5–32, whose sample of 97 published return-predicting characteristics found returns
averaging **26% lower out-of-sample** than in the original published sample, and **58% lower**
specifically in the post-publication period. The January effect sits among the oldest and most
publicized members of that broad literature, and the direction of its own post-discovery decline is
the single cleanest illustration available anywhere in this program of Contract §5's governing
principle — assume your alpha decays — applied to a calendar-shaped anomaly rather than a
cross-sectional factor.

### B.2 Turn-of-year in Japan and the UK: the tax-year test that proves the mechanism travels

If tax-motivated trading is the true mechanism and not merely a US coincidence with January, the
effect should move when a country's tax year moves, and it does. **Gultekin & Gultekin (1983)**,
"Stock Market Seasonality: International Evidence," *Journal of Financial Economics* 12(4): 469–481,
surveyed major industrialized markets and found stock-market seasonality concentrated in January in
most countries **and in April specifically in the United Kingdom** — the UK's tax year historically
ran to 5 April — with the authors explicitly noting the coincidence between the seasonal peak and
each country's own turn-of-tax-year date (with Australia the noted exception). This is the direct
cross-country analogue this chapter's India argument leans on: the calendar anchor that matters is
the *tax* year, not the Gregorian year, and a country whose tax year ends in a month other than
December should show its turn-of-year effect shifted to that month — exactly the logic used in §A.2
to derive why India's own effect belongs in April rather than January. **Kato & Schallheim (1985)**,
"Seasonal and Size Anomalies in the Japanese Stock Market," *Journal of Financial and Quantitative
Analysis* 20(2): 243–260, examined monthly Japanese data 1964–1980 and documented a January size
effect in Japan as well — positive and disproportionately large January returns for small-to-medium
firms — despite Japan's own fiscal year running April-to-March for corporations, a detail the
Japanese literature has treated as evidence that calendar-year-end institutional and psychological
effects (bonus payments, year-end settlement conventions) can coexist with or dominate a purely
tax-year-driven story in some markets; the honest reading for this chapter is that the *tax-year*
channel is well identified in the UK case specifically (because the UK's turn-of-year effect moved
to track its own distinct tax year) while the Japanese case shows the same calendar slot can carry
more than one institutional mechanism at once, a genuine complication this chapter states rather
than smooths over.

### B.3 The Savor-Wilson scheduled-announcement premium and the FOMC-specific literature's post-2015 turn

Section A.1 already established Savor & Wilson (2013)'s general scheduled-macro-announcement
premium (11.4bp vs 1.1bp) across CPI, employment, and FOMC dates, 1958–2009. The FOMC-specific slice
of this literature has its own, separately documented decay story, and the two must not be
conflated: **Lucca & Moench (2015)**, "The Pre-FOMC Announcement Drift," *Journal of Finance* 70(1):
329–371, documented large average excess equity returns specifically in the **24 hours before**
scheduled FOMC statements, 1994–2011 — a distinct object from the announcement-day premium itself,
concentrated in the anticipation window rather than the announcement itself, and reported as having
*increased* over their sample, accounting for a striking share of total annual realized equity
returns by the end of the period. The out-of-sample turn came via **Kurov, Wolfe & Gilbert (2021)**,
"The Disappearing Pre-FOMC Announcement Drift," *Finance Research Letters* 40, who extended the
sample through December 2019 and found the pre-FOMC drift had **essentially disappeared after
2015** for FOMC statements not accompanied by a press conference, and weakened materially for those
that were — a finding the authors attribute to reduced policy uncertainty in the post-2015
communication regime rather than to arbitrage-driven crowding per se, though the observational
signature (a published anomaly weakening sharply after its own publication and after the sample
window that produced it) is exactly McLean-Pontiff's pattern applied to a single, narrowly defined
calendar effect rather than to a broad cross-sectional characteristic. This is the FOMC literature's
own internal proof of Contract §5's governing principle, running on a genuinely different mechanism
(anticipatory positioning ahead of a scheduled decision) from the announcement-day premium this
chapter's Budget-day argument leans on, and the distinction matters: L5's Budget-day design is built
on the announcement-day/scheduled-event-risk premium (Savor-Wilson's broader claim, still standing),
not on a pre-announcement drift claim (the narrower, now largely decayed Lucca-Moench claim) — the
two should never be cited interchangeably, and this chapter does not.

### B.4 Halloween / Sell in May and the Zhang-Jacobsen replication debate

**Bouman & Jacobsen (2002)** is the paper that took "sell in May and go away" from stockbroker
folklore to peer-reviewed anomaly, testing it across 37 countries and finding a robust, statistically
significant difference between November–April and May–October returns in most of them, with no
convincing risk-based explanation on offer — which is exactly why the paper's own title calls it
"another puzzle" rather than a solved mechanism. The subsequent literature split sharply on whether
the effect is real or a statistical artifact: doubt was raised by Maberly & Pierce (2003, 2004),
Lucey & Zhao (2007), and **Zhang & Jacobsen (2013)** [VERIFY: exact working-paper venue and title —
search results place this as a critical contribution inside the same debate but do not resolve a
peer-reviewed citation independent of the authors' own later restatement], while **Jacobsen &
Visaltanachoti (2009)** and Andrade et al. (2013) reported out-of-sample validation. Ben Jacobsen and
Cherry Yi Zhang then answered the accumulated methodological criticism — sample size, time-varying
volatility, outlier sensitivity, and inference problems — directly in **Zhang & Jacobsen (2021)**,
"The Halloween Indicator, 'Sell in May and Go Away': Everywhere and All the Time," *Journal of
International Financial Markets, Institutions and Money* (2021 print; a related SSRN/AEA-adjacent
manuscript circulated as "An Even Bigger Puzzle" [VERIFY: exact publication history of the two related
titles]), extending the test to **over 300 years of UK data** and to **109 stock markets across a
combined 323-year span**, finding November–April mean returns exceeding May–October mean returns in
**82 of the 109 markets** studied. The honest reading for this chapter is that Halloween/Sell-in-May
is the single most heavily replicated and most heavily *disputed* calendar anomaly in the entire
global literature, run through more robustness checks by more skeptical co-authors than any other
entry in this Part, and it remains — after three decades of adversarial replication — without an
agreed mechanism: no version of the debate offers a tax-code argument, an institutional-flow
argument, or an information-asymmetry argument comparable in rigor to Poterba-Weisbenner's
turn-of-year identification. That absence of mechanism is precisely why Contract §8 would bar this
desk from adopting a "sell in May" rule for India even if a future India-specific replication found
a statistically significant November–April gap in NSE data: statistical robustness across a
replication war is not the same evidentiary object as a named, survivable mechanism, and this desk's
own discipline (Part G) treats the two as categorically different bars.

### B.5 India — the double-length case record

**Budget-day event studies on Indian data: a literature quality problem worth stating plainly.**
Before any individual case, this chapter registers an honest caveat about the India-specific academic
record itself. A search of the Indian Budget-event-study literature surfaces a scattering of results
of visibly uneven quality: a 2025 arXiv preprint, "Analysis of the Impact of the Union Budget
Announcements on the Indian Stock Market: A Fractal Perspective" [VERIFY: peer-review status —
arXiv preprint as of the search date, not yet confirmed published in a peer-reviewed venue], compares
NIFTY 50 average abnormal returns and cumulative average abnormal returns across ±15-day windows for
the 2020, 2022, 2023, and 2024 Budgets; older work by Saraswat & Banga (2012) [VERIFY: exact journal],
Singhvi (2014) [VERIFY: exact journal], and Deepak & Bhavya (2014) [VERIFY: exact journal] reportedly
find, respectively, significant short-term but negligible long-term effects, no lasting effect on
NIFTY, and no significant influence of Budget announcements on market behavior over time — a genuinely
mixed record, not a settled one. One paper surfaced in the search, "Union Budget Anomaly and Stock
Market Reactions," appears in a journal whose name and scope (a neonatal-surgery journal publishing a
finance event study) is itself a visible red flag for predatory or hijacked-journal publication
practices, and this chapter excludes it from any evidentiary weight rather than cite a number from
it — a small but real illustration of why "cite honestly, tag what you cannot verify" is not a
formality in this specific literature. What *is* consistently reported across the more credible
practitioner and academic sources is the volatility-side finding this chapter's L5 argument actually
needs: aggregated retrospectives of India VIX behavior around Budget day (e.g., the Arihant Plus
15-year Nifty/Budget-day retrospective) [VERIFY: exact sample and methodology — practitioner-grade
blog analysis, not peer-reviewed] report that India VIX has historically **fallen**, often by a
double-digit percentage, in the sessions immediately following the Budget presentation on most years
studied — consistent with the scheduled-event-risk-resolution mechanism of §A.4 (uncertainty
collapses once the content is known, whichever direction the market then moves) rather than with any
directional Budget-day "effect." The honest state of this literature, then, is: real, if
methodologically uneven, evidence for a *volatility* pattern around Budget day; no reliable evidence
for a *directional* one; and this desk's own CW1 print (Feb rank 7/12 monthly) is entirely consistent
with both, because a real daily volatility spike is exactly what a monthly print would fail to detect.

**Case 1 — 24 July 1991: the liberalization budget as the mechanism's own founding instance.**
Finance Minister Manmohan Singh's 1991-92 Budget speech, delivered amid a balance-of-payments crisis
so severe that India's foreign-exchange reserves covered barely three weeks of imports, dismantled
the industrial licensing ("License Raj") regime, opened the economy to foreign direct investment, and
began the rupee devaluation and trade-liberalization program that is conventionally dated as the
start of India's post-1991 reform era — the budget closing with Singh's own often-quoted line, "Let
the whole world hear it loud and clear. India is now wide awake." This is included in the case record
not for any harvestable calendar signal (the desk makes none) but as the extreme instance proving the
mechanism §A.4 formalizes: a Budget in 1991 was a genuinely unscheduled-*content*, scheduled-*timing*
event of the largest possible magnitude — the entire direction of India's economic model was
undisclosed until the speech itself — which is why 1991 is the case every subsequent India Budget
retrospective measures itself against, and why "the content is genuinely unknown ex ante" is not a
theoretical assumption in the India context but a demonstrated historical fact.

**Case 2 — 28 February 1997: the "Dream Budget" and the limits of a good-news prior.** P.
Chidambaram's 1997-98 Budget, presented under the Deve Gowda government and immediately dubbed the
"Dream Budget" by the Indian press, cut the top marginal individual income-tax rate from 40% to 30%,
cut the domestic corporate tax rate from 40% to 35%, abolished the corporate surcharge, reduced peak
customs duty from 50% to 40%, and introduced a Voluntary Disclosure of Income Scheme aimed at
widening the tax net — a budget almost universally read, at the time and since, as unambiguously
market-friendly. Its inclusion here is a discipline case, not a triumph case: even a Budget this
widely regarded as "good news" in retrospect does not license, ex ante, a directional bet on Budget
day generally, because the 1997 case is exactly the kind of instance that tempts a desk into
believing "Budgets that cut taxes are buy signals" — a rule that would have to be tested against the
2020 and 2024 cases below (which cut nothing comparably dramatic in equity-favorable directions and
in one case actively raised the specific taxes equity investors care about) before it could be
trusted, and PL1's own 3/8 election-direction measurement (§A.4) is the desk's evidence that
"favorable content in one instance" does not generalize into "predictable direction across
instances" for this family of events.

**Case 3 — 3 February 2004 (interim) and 8 July 2004 (full budget) and 17 May 2004 (the crash the
interim budget could not see coming).** The 2004 election year produced the textbook "two-budget"
problem this chapter's Part C data pipeline must handle explicitly: Finance Minister Jaswant Singh
presented an **interim budget** (a vote-on-account, not a full budget) in February 2004 ahead of the
scheduled general election, and when the incumbent NDA government unexpectedly lost that election,
the newly formed UPA government's finance minister, P. Chidambaram, presented a **full budget** on
8 July 2004 — the first time in India's history that an interim and a full budget in the same fiscal
year were delivered by finance ministers from two different parties. Between the two budgets sits the
case this chapter treats as the cleanest illustration anywhere in this program of "the calendar
predicts the date, never the content": on **17 May 2004**, the trading session immediately following
the surprise electoral defeat of the BJP-led NDA, the BSE Sensex fell **15.5%** — its largest
single-day percentage fall in the exchange's history at that point — while the Nifty fell
approximately 12%, both driven by the market's shock at a result it had not priced in, compounded by
a simultaneous emerging-market sell-off. Nothing about the *February* interim-budget window predicted
this outcome, because the event that moved the market by an order of magnitude larger than any Budget
day in India's history was not the Budget at all — it was the election result three months later, a
different fixed-date-uncertain-content event this desk's own atlas already tracks separately as row
3.7 (L5's sibling seat) and measures via PL1. The 2004 episode is this chapter's strongest single
piece of evidence that Budget-window and election-window risk must be scheduled as **separate,
addable** windows exactly as `calendar_windows.py`'s `n_windows` overlap-depth counter is built to
do (a February budget window and a subsequent election window are two distinct sources of scheduled
uncertainty, not one, and the module was designed to let a consumer see when both are live at once)
— and it is the reason the L5 module's docstring explicitly documents "Election-year July full
budgets are NOT flagged (documented limitation; CW1)" as an honest gap rather than a silent one:
the July 2004 full budget sits entirely outside the February-anchored budget window this desk's
current design flags, a limitation the module states rather than hides.

**Case 4 — 1 February 2020: the Budget the crash swamped.** Finance Minister Nirmala Sitharaman's
2020-21 Budget, presented on the first Saturday session in the newly established February-1 calendar
slot, disappointed the market on its own terms: the Sensex fell **987.96 points (2.43%)** to close at
39,735.53 that same day, its steepest single-session Budget-day fall in over a decade, driven by a
wider-than-expected fiscal deficit target (revised to 3.8% of GDP from an earlier 3.3% goal), the
shift of dividend-distribution-tax incidence onto individual shareholders, and the absence of any
relief on long-term capital-gains tax that the market had been hoping for. Read in isolation, 2020
looks like a clean Budget-day event-study case — a specific policy disappointment, a same-day price
reaction, exactly the AR/CAR object §A.1 formalizes. Read in its actual context, it is the case that
best illustrates why a scheduled-window seat must never be mistaken for a forecasting tool: the
Sensex had set an all-time closing high of roughly 42,000 just two weeks earlier (mid-January 2020),
and within seven weeks of the Budget the index would fall to **25,981 on 23 March 2020** — a **38%**
peak-to-trough collapse driven entirely by the COVID-19 pandemic and India's nationwide lockdown
announcement, an entirely separate, unscheduled, non-calendar shock that overwhelmed the Budget
window by more than an order of magnitude within the same quarter. The Budget-day move and the
COVID crash are causally unrelated events that happened to share a calendar window, and a desk
that had built any directional conviction from the Budget-day disappointment (a bearish read, as it
happened, correctly signed but for entirely the wrong reason) would have been "right" by pure
coincidence of timing — the textbook case for why L5 schedules exposure reduction into the window
and stops there, never inferring a forward view from what the window itself contained.

**Case 5 — 1 July 2017 (midnight 30 June/1 July): the Goods and Services Tax rollout as a
non-Budget fixed-date fiscal event.** GST was launched at a special midnight session of Parliament's
Central Hall — the same chamber that hosted independence at midnight in August 1947 — with President
Pranab Mukherjee and Prime Minister Narendra Modi jointly pressing the launch button, in a ceremony
boycotted by the Congress party and several other opposition parties who argued the country was
under-prepared for the transition; the reform replaced a fragmented structure of state and central
indirect taxes with a unified national goods-and-services tax. GST's inclusion in this atlas is
deliberately as a **CONTRAST case, not a Budget-window case**: it is a fixed, legally scheduled,
one-time fiscal-calendar event — precisely the kind of date-certain, content-partially-known
(the GST Council had published rate schedules well in advance, unlike a Budget's genuinely sealed
content) transition Atlas row 4.3 (advance-tax/GST outflow dates) already routes to an **EXECUTION**
seat rather than a REGIME or EDGE one: GST's *recurring* monthly and quarterly compliance dates
(return filing, input-tax-credit reconciliation deadlines) drain system liquidity on known dates in a
way CCIL/RBI LAF data can observe mechanically, which is why the atlas treats it as a false-fire
exclusion calendar for funding-stress triggers (H58) rather than as a price-timing signal — the 2017
rollout itself was a single, non-repeating regime change, not a calendar cycle, and this chapter is
careful not to conflate "GST happened on a fixed date" with "GST is a calendar effect": it is the
former, and its recurring compliance-date liquidity drain (not its one-time 2017 launch) is the part
of GST that belongs in this family of hypotheses at all.

**Case 6 — 23 July 2024: the live case of tax-calendar mechanics moving prices in real time.** The
2024-25 Budget — itself a full budget following an interim budget earlier in the year ahead of the
2024 general election, the same two-budget structure as 2004 — raised the long-term capital-gains
tax rate on equity from 10% to 12.5%, raised the short-term capital-gains tax rate on specified
financial securities from 15% to 20%, raised the securities transaction tax on futures and options,
and raised the LTCG exemption threshold from ₹1 lakh to ₹1.25 lakh as a partial offset, alongside a
reclassification of the long-term/short-term holding-period boundary across asset classes. This is
the case this chapter treats as the most direct, contemporaneous illustration available anywhere in
the entire program of the tax-calendar mechanism formalized in §A.2/§A.5 operating in *real time*
rather than in a decades-old US dataset: a capital-gains tax-rate change announced on a specific,
legally fixed date is exactly the kind of natural experiment Poterba-Weisbenner used to identify the
US tax-loss-selling mechanism causally, and a future India-specific study exploiting the pre-/post-23
July 2024 discontinuity in equity capital-gains treatment — comparing turn-of-fiscal-year trading
behavior in FY2024-25 (post-change) against FY2023-24 and earlier (pre-change) — would be the
single cleanest identification strategy this desk could design for testing whether India's own
April/FY-end pattern (Atlas 4.2, CW2) is genuinely tax-driven rather than merely calendar-coincident,
exactly mirroring the identification logic Poterba-Weisbenner applied to the 1969 and 1976 US tax-law
changes. This is a runsheet item this desk has not yet built (it requires a clean pre/post panel spanning the July 2024 discontinuity), stated here as the concrete next step the case record itself
points to, not as a finding already in hand.

---

## Part C — India data engineering

Every hypothesis in this chapter resolves to a concrete, free-source data pipeline, and Contract §3
and §12 both require that every proposed indicator name its free source or be flagged unavailable.
This Part specifies each pipeline exactly enough that a future data phase can build it without
re-deriving the design.

**Budget dates, 1991–2026, and the interim-vs-full-budget problem in election years.** The
authoritative, free, primary source is **indiabudget.gov.in**'s own archive (`budget_archive/`
sub-paths keyed by fiscal year, e.g. `ub1997-98`, and the modern site's speech-PDF archive keyed by
year), which carries the finance minister's speech text, the exact presentation date, and — for
election years — whether the document was an interim budget/vote-on-account or a full budget. The
pipeline needs exactly three fields per fiscal year: presentation date, presenter, and
interim-vs-full flag, plus a fourth boolean for "railway budget presented separately" (true only
through FY2016-17, false from FY2017-18 onward per the 2016 merger decision implemented at the
Feb-2017 Budget). **The election-year double-budget years, confirmed from the case record above and
the general pattern of India's five-year election cycle intersecting the February budget calendar,
are: 1991 (interim, then the July 1991 full/reform budget under the new government), 1996, 1998,
1999, 2004 (Case 3 above — Feb interim by Jaswant Singh, July full by Chidambaram), 2009, 2014, 2019,
and 2024 (Case 6 above)** — every one of these years requires the pipeline to store **two** budget
dates rather than one, and any downstream consumer (including `calendar_windows.py`'s `BUDGET_MONTH`
anchor) that assumes exactly one February-anchored budget per year will silently mis-flag the
July full-budget window in every one of these years, which is exactly the "documented limitation"
the module's own docstring already flags rather than papering over. This chapter recommends the data
phase build the interim/full flag as a first-class field precisely so a future L5 revision can
decide, deliberately, whether to extend the window family to cover July full budgets in these
specific years (a design change, not a bug fix, and one that needs its own pre-registration before
any promotion).

**Presentation date AND time, and the 1999/2017 structural breaks in event-day definition.** Two
regime breaks must be encoded, not treated as noise. First: from Independence through the 1998-99
Budget, the Finance Minister presented at **5:00 PM** — a colonial-era holdover timed to coincide with
late-morning hours in London — meaning the market had already closed for the session by the time the
speech began, and full price discovery on Budget content necessarily spilled into the **next**
trading day's open. **Yashwant Sinha broke this convention on 27 February 1999**, presenting the
1999-2000 Budget at **11:00 AM** for the first time, explicitly to allow same-day parliamentary
debate and, in his own stated reasoning, to signal that a no-longer-colonial India could set its own
timetable; every Budget since has been presented at 11 AM. Second: **the presentation date itself
moved from the last working day of February to 1 February starting with the 2017-18 Budget**
(announced in 2016, implemented at the February 2017 presentation by Arun Jaitley, the same event at
which the Railway Budget was merged into the General Budget after 92 years of separate presentation).
The consequence for event-window construction is a genuine, dateable break in what "Budget-day
absorption" even means: for any Budget dated **1999–2016**, an event study should treat the **same
trading session's close** as the first observation capable of reflecting the speech (11 AM
presentation, market open through the close); for any Budget **before 1999**, the first
same-session close is *not* informative and the **following** trading day's open-to-close is the
correct first event-day observation (5 PM presentation, after the close); and Budgets from **2017
onward** additionally need the calendar-date field itself re-derived (1 February, adjusted for
weekends/holidays to the nearest trading day, rather than "the last day of February," which the
pre-2017 archive uses as its own dating convention). A pipeline that applies one uniform "Budget day
= presentation date, use close-to-close" rule across the full 1991–2026 span will silently misdate
the event window for every pre-1999 Budget in the sample, understating any real absorption effect by
splitting it across the wrong two sessions.

**India VIX, daily, around Budget days — the data-gated design for CW-D1.** India VIX exists from
**2 March 2009** (NSE began daily dissemination on this date, following the index's 2008 methodology
launch with CBOE); VIX futures did not launch until 26 February 2014, which matters only if a future
design wants futures-implied term-structure data rather than the spot index. **India VIX launched in
2009 and this desk does not claim any earlier data** — this is stated explicitly because it is the
single most common error a Budget-day India-VIX study could make (extrapolating a "VIX-like" measure
backward across the 1991, 1997, and 2004 cases in this chapter's Part B, none of which have any VIX
observation at all; those cases are narrative/price-only, and this chapter does not pretend
otherwise). The free source is **NSE's own historical-data archive** (`nseindia.com`'s VIX historical
reports page), which serves daily open/high/low/close India VIX values; the CW-D1 design this atlas
entry's own results file names as the "data-gated daily-resolution design" is: pull daily India VIX
for a ±10 trading-day window around every Budget date from 2009 onward (17 Budgets: FY2009-10 through
FY2026-27, correctly split into interim/full per the field above), compute the pre-event VIX level
(t−10 to t−2 average), the event-day VIX change, and the post-event decay path (t+1 through t+10),
and test — exactly as CW1 could not at monthly resolution — whether VIX systematically **falls** in
the sessions immediately following the presentation (consistent with uncertainty resolution, §A.4)
regardless of which direction the underlying index itself moved that day. This design is
pre-registered here as a runsheet item, not run in this chapter.

**NSE bhavcopy small-cap indices for an April-effect daily verification.** CW2's PASS was measured on
the IIMA monthly SMB factor (a long-short academic construction, 1993-10 onward); a daily verification
using **NSE's own published small-cap indices** — the Nifty Smallcap 250 (and its predecessor
Nifty Smallcap 100) and the BSE Smallcap index — pulled from the exchanges' daily bhavcopy archives
(free, `nseindia.com`/`bseindia.com` historical-data downloads) would let a future design test the
April effect on an **investable** index rather than an academic long-short factor, directly
addressing the atlas's own Tier-C "small, cost-fragile" caveat on 4.2: an investable small-cap index
return, net of the desk's own cost model (Contract §7 item 6's turnover-cost stack), is the right
object to measure against before CW-PT1's paper-trade rule (already registered per calendar-RESULTS.md
as the promotion path, "measured net of modeled costs, 3 Aprils minimum") can be evaluated honestly.
This is the concrete data step that separates "CW2 passed on an academic factor" from "an April
small-cap tilt is investable after costs" — the two are different claims, and only the second one
is ever eligible for a return budget.

**AMFI and exchange dividend calendars, for 4.12's documentation.** Two distinct free sources serve
two distinct objects here, and they must not be conflated. For **mutual-fund dividend/IDCW
(Income Distribution cum Capital Withdrawal) declaration dates**, AMFI (Association of Mutual Funds
in India, `amfiindia.com`) publishes scheme-level NAV and dividend/IDCW history; this is the relevant
source only if a future design wants to test dividend-season effects through the mutual-fund
wrapper specifically. For **individual-equity ex-dividend and record dates** — the object §A.5's
Elton-Gruber pricing test actually needs — the correct free sources are the **NSE and BSE corporate-
action archives** (`nseindia.com`/`bseindia.com` corporate-announcements pages), which publish
ex-date, record date, and per-share dividend amount for every listed company, from which a
`ΔP/D` ratio can be computed directly around each ex-date using the same bhavcopy price series
already in scope for the small-cap verification above. Given §A.5's conclusion that 4.12 is REJECTED
by mechanism rather than by absence of data, this pipeline's purpose is **documentation, not
promotion**: a future dossier revision could compute India's own empirical `ΔP/D` ratio (testing
whether it clusters below 1, as Elton-Gruber predicts under India's post-2020 ordinary-income
dividend tax treatment) purely to confirm the REJECT rests on measured evidence rather than
assumption, exactly the same discipline CW3 applied to 4.11.

**Event-window alignment pitfalls, consolidated.** Three distinct hazards recur across every
pipeline above and are worth stating together as a single checklist for whoever builds this in the
data phase: (1) the **11 AM vs 5 PM presentation-time break at 1999** changes which trading session
is the first informative one, as detailed above — get this wrong and every pre-1999 event study
misdates its own event day; (2) the **last-day-of-February vs fixed-1-February break at 2017**
changes how the calendar date itself is derived from the fiscal year, and additionally interacts
with weekends (1 February falls on a weekend in several years across 2017–2026, requiring a
next-trading-day adjustment the pre-2017 "last working day" convention never needed, because "last
working day" was already trading-day-native by construction); (3) the **election-year double-budget
problem** (this Part's first item) means any Budget-window flag anchored solely on February will
silently omit the July full-budget event in nine confirmed years since 1991, an omission
`calendar_windows.py`'s own docstring already discloses rather than hides. None of these three is a
data-availability problem — all three sources (indiabudget.gov.in, NSE/BSE bhavcopy, India VIX
archive) are free and already within Contract §3's approved list — they are pure **event-window
construction discipline**, and getting any one of them wrong would corrupt every downstream CW-D1
or Elton-Gruber verification this Part specifies, regardless of how much data volume is thrown at
the problem.

---

# Appendix: the desk prints (real-data leg)

# Atlas 4.1/4.2/4.11 — calendar-as-signal trials: results and honest read
Written AFTER the prints (2026-09-02). Pre-registration: trial-ledger CW1-CW3.
Script: scripts/analyze_calendar.py. Data: IIMA India monthly factors, 1993-10..2025-12
(MF n=386, SMB n=386; ~32 observations per calendar month).

## The prints
- CW1 (Budget-month vol): Feb median |MF| = 4.27 vs non-Feb 4.22; rank 7/12;
  Mann-Whitney one-sided p = 0.522. **FAIL** on both bar legs.
- CW2 (FY-end small-cap reversal): April median SMB = +2.47, rank 1/12 (next: Aug +0.93);
  Mann-Whitney one-sided p = 0.020. **PASS** on all three bar legs.
- CW3 (omnibus demonstration): Kruskal-Wallis H = 12.13, p = 0.354 across the 12 months
  of MF. Consistent with NO month-of-year structure; the 4.11 REJECT stands as pre-stated.

## Honest read
1. CW1 is the CR2 pattern a second time: a 1-3 day event (Budget-day policy reveal) is
   invisible at monthly resolution — February is the SEVENTH most volatile month, i.e.
   perfectly ordinary. Pre-stated routing applies: the L5 budget window survives on the
   daily-resolution record (India VIX event studies; the mechanism is a legally fixed
   reveal date) — but OUR print adds nothing to it, and the monograph must say so.
   The seat's justification is literature + mechanism, Tier B for timing only.
2. CW2 is the register's cleanest calendar pass and the only one with a mechanism:
   India's fiscal year ends March 31; tax-motivated selling depresses small caps into
   FY-end and they rebound in April (the January-effect analogue, shifted by the fiscal
   calendar). April was named BEFORE the print (one test, not twelve). Two honesty notes:
   (a) the post-hoc observation that Feb (-2.36) and Mar (-1.70) are the two most negative
   SMB months is the selling leg of the same story — coherent, but NOT pre-registered, so
   it is tagged CW2b for a future trial, not claimed; (b) SMB is an academic long-short
   factor — harvesting this means an April small-cap tilt, and the atlas prior
   ("small, cost-fragile", Tier C) plus the 20bp STT round trip stand. VERDICT:
   pass -> instrument, refuse budget. A pre-registered paper-trade rule (CW-PT1) goes to
   Part F; promotion needs the paper ledger, not this print.
3. CW3 did its declared job: the omnibus finds nothing (p=0.354), so the month-of-year
   REJECT is confirmed WITH evidence rather than by fiat. The pedagogical point the
   lesson must carry: November ranks #1 in |MF| and December #1 in median MF — a reader
   hunting patterns would "find" both; the omnibus and the mechanism ban are what stop us.

## Consequences
- L5 seat: unchanged (reduce-only vol scheduling; budget + election windows); our monthly
  print neither supports nor undermines it — daily-resolution VIX work is the data-gated
  design (CW-D1, runsheet).
- Atlas 4.2: EDGE hypothesis GRADUATES to instrumented Tier-C flag with paper-trade
  CW-PT1 (April small-cap tilt, measured net of modeled costs, 3 Aprils minimum).
- Atlas 4.11/4.12: REJECT confirmed (4.11 by CW3; 4.12 by mechanism — priced, mechanical).

---

# Parts D–H — calendar-as-signal (atlas 4.1 seat / 4.2 instrumented / 4.11 + 4.12 rejects)

## Part D — Econometrics: what the desk legs establish and refuse

Three trials, one pre-registration block, bars rank-based (no magic thresholds), all run
2026-09-02 on the IIMA monthly factor library (MF/SMB, 1993-10..2025-12, ~32 obs per
calendar month). Full prints: research/cycles/calendar/calendar-RESULTS.md.

**CW1 (Budget-month vol) FAIL.** February's median |MF| ranks 7 of 12 (4.27 vs 4.22
non-Feb; MW one-sided p=0.522). The pre-stated resolution caveat did the work: a 1–3 day
scheduled-reveal vol spike is diluted ~20× inside a month of ordinary variance. This is the
second time the register has measured the monthly-resolution wall (CR2 was the first), and
it now has a name in the ledger: *the resolution theorem* — an event-day phenomenon must be
tested at event-day resolution, and a monthly print can neither confirm nor kill it. The L5
budget window therefore rests on (i) the mechanism — a legally fixed reveal date with
direction unknowable, and (ii) the published daily-resolution India VIX event record, cited
in Part B — never on our monthly print. Our own daily-resolution test is data-gated (CW-D1).

**CW2 (April small-cap) PASS — and refused promotion.** April median SMB +2.47, rank 1/12,
MW one-sided p=0.020, with the month named before the print by a mechanism (FY ends Mar 31;
tax-motivated small-cap selling reverses). One test, not twelve — the family-wise trap CW3
demonstrates does not apply to a single pre-named month. What the pass buys: instrumentation
(a Tier-C flag) and a paper trade (CW-PT1) — NOT budget, because the atlas prior stands
un-refuted: the effect is a small-cap long expressed in the costliest corner of the book
(impact + 20bp STT round trip), the SMB factor is an academic long-short that no real
portfolio holds frictionlessly, and one monthly point per year means n=32 — Tier B by count,
Tier C by harvestability. The pass→refuse quadrant gets its cleanest member.

**CW3 (omnibus) null, as declared.** Kruskal-Wallis p=0.354 across 12 months of MF. The
demonstration worked in both directions: no calendar structure survives an omnibus test,
AND the two seductive rank-1 months the sweep surfaced (Nov in |MF|, Dec in median MF)
are exactly the post-hoc candidates the interpretation rule pre-committed us to ignore.

**Post-hoc observations, tagged and quarantined:** Feb (−2.36) and Mar (−1.70) are the two
most negative SMB medians — the selling leg of CW2's mechanism. Coherent, unregistered,
therefore CW2b in Part F: a future pre-registered trial, not a claim.

## Part E — The algorithm (quant/ladder/calendar_windows.py, seated)

The one module in the ladder that is a SCHEDULE, not a state. `windows()` builds explicit
Window objects — (start, end, kind, anchor) — so every flagged month carries its trail;
`calendar_schedule()` returns (in_window, n_windows, kinds) with overlap DEPTH (a February
inside an election window counts 2). Budget windows are February by construction (era-robust
at monthly resolution: last-day-of-Feb pre-2017 and Feb-1 post-2017 are the same month;
election-year July full budgets documented as a limitation, not silently flagged). Election
windows span [anchor−2, anchor+1] around supplied result months — an event list, never an
extrapolated clock: nothing is generated beyond announced calendars, and events outside the
sample are ignored. There is no directional output in the module's namespace, and a test
asserts that (`test_no_directional_output_exists`) — reduce-only is enforced structurally,
not by convention. Seven exact planted-truth tests (deterministic module, no stochastic
fixture needed); suite 80 green.

Consumption: L5 emits the mask to the risk system — leverage/vol scheduling only
(ladder.yaml `reduce_only: true`). The mandate-clarity re-lever rule (re-gross after a
decisive result) remains pre-registered-only until an election passes with the rule on
paper (HL-7's routing).

## Part F — Harvest map + pre-registered designs

Harvested now: the L5 seat machinery (above); the resolution theorem as register doctrine;
the CW2 Tier-C flag (April small-cap month, flag-only).

Designs registered, data-gated:
- **CW-D1 (daily budget-window vol):** India VIX daily (NSE, 2009-) around budget days;
  bar at registration: budget-day ±1 realized |NIFTY return| and VIX change vs matched
  non-event days, one-sided p<0.05 across the 2009-2026 set (n≈18 budgets + interims).
  Pre-2001 5pm-presentation era excluded by design (event-day definition break).
- **CW-PT1 (April paper trade):** each April, a modeled small-cap tilt (cost model from
  config/costs.yaml, aggressive book's impact schedule) held Apr-1..Apr-30, ledgered like
  HL-7; promotion discussable only after 3 Aprils AND net-of-modeled-cost positive in ≥2.
- **CW2b (the selling leg):** pre-registered now for the NEXT library refresh: Feb+Mar
  pooled median SMB < 0 with MW one-sided p<0.10 vs Apr-Jan. (Stated before any new data.)

## Part H — Knowledge ledger

**Established (our prints):** April small-cap seasonality at monthly resolution (CW2,
p=0.020, rank 1/12); no omnibus month-of-year structure in Indian market returns (CW3);
Budget-month vol invisible monthly (CW1) — the resolution theorem's second data point.
**Pooled-prior (literature, Tier B):** scheduled-announcement vol premia (Savor-Wilson
lineage); tax-loss-selling as the January-effect mechanism (Ritter/Roll/Poterba-Weisbenner),
mapped to India's April; the January effect's own post-publication decay (McLean-Pontiff) —
the standing warning on CW2's future.
**Awaits India data:** CW-D1 (daily VIX event study); CW-PT1 (paper Aprils); CW2b.
**Unknowable:** whether CW2 survives its own publication era — the effect is 30+ years old
in the US literature and decayed there; India's version gets the decay haircut BEFORE any
sizing conversation, per Contract §5.

Verdicts: 4.1 SEATED (scheduling only, mechanism + daily-resolution literature; our monthly
print abstains). 4.2 INSTRUMENTED (pass→refuse promotion; flag + paper trade). 4.11 REJECT
(omnibus-confirmed). 4.12 REJECT (priced mechanics, Elton-Gruber; no trial spent).
