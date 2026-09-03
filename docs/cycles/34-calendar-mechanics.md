# Calendar Mechanics — The Plumbing That Moves Prices Without Moving Information

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-02

Parts A, B, C & G · Atlas entries **4.3** (advance-tax/GST liquidity drains, `docs/CYCLE_ATLAS.md`
line 124: "System liquidity drains on known dates → CCIL rates spike *mechanically*"; harvest
**EXECUTION → L2 false-fire exclusion calendar**), **4.4** (earnings-results season, line 125:
"Name-level vol clusters at results; staged entries through a results date take gap risk for
free"; harvest **EXECUTION**: results-date pause), **4.5** (derivative expiry cycle, line 126:
"Pinning/rollover flows distort closes; rebalancing on expiry day buys noise"; harvest
**EXECUTION**: expiry-day avoidance) and **4.6** (index-reconstitution calendar, line 127:
"Forced passive flows on known dates — the special-sits edge AND a 'don't mistake the pop for
momentum' exclusion"; harvest **EDGE** special-sits + **EXECUTION** momentum exclusion, Tier B).
All four entries are the H58 ops pack (`docs/CYCLE_ATLAS.md` §8, line 178) plus its atlas-4.6
sibling RC1, and the machinery already ships: `quant/ladder/exclusion_calendar.py`, seven exact
planted-truth tests (`tests/test_exclusion_calendar.py`), wired into `config/ladder.yaml`'s L2
role text. This chapter argues why that module's three date-arithmetic functions are the correct
and *sufficient* response to four calendars that move prices through settlement mechanics rather
than information — never why they should become a fifth return line. **Parts D–H — the
econometrics of an entry designed to run zero trials, the algorithm's own accounting, the harvest
map, and the knowledge ledger — are the principal's own document**
(`research/cycles/calendar-mechanics/partDH-mechanics.md`, already on record), cross-referenced
throughout and never re-derived here. This chapter's sibling on the annual/calendar band's other
half — the Budget window and the April small-cap effect (atlas 4.1/4.2) — is
`docs/cycles/33-calendar-signal.md`; that chapter asks whether a calendar date carries
*information content* worth a rank; this one asks only whether a calendar date moves the
*plumbing* enough to fool an unrelated trigger, and answers a flat no-alpha-claim throughout.

**What follows.** Part A formalizes each of the four mechanisms — the LAF corridor's arithmetic,
an earnings date's variance decomposition, the pinning SDE, and the index-demand-curve model —
because Contract §6 requires every constant the design uses to trace to an argument, and an
EXECUTION rule earns that scrutiny exactly as an EDGE would. Part G is this entry's honesty
check on the desk itself: why a mechanical spike keeps fooling a trained eye, and why the module
refuses every temptation to convert what it excludes into something it trades. Part B carries
the cross-country literature in specification detail and roughly ten dated case studies, India's
share doubled per this series' standing convention. Part C is the data-engineering appendix:
where every series in Parts A and B actually comes from, free, and where the seams are. **No
trial has run for this entry and none is claimed here** — the four registered designs (H58-D1,
H58-D2, H58-D3, RC1; `research/register/trial-ledger.md`, block "Designs H58-D1..D3 + RC1",
2026-09-02) are data-gated, and every number below not attached to a named published source or
this program's own already-completed trial (cited, never recomputed) is stated as illustrative
arithmetic on the module's own config defaults or flagged `[VERIFY]`.

---

## Part A — Theory, with the math

### A.1 India's liquidity plumbing, formally, and why a scheduled drain fools a stress classifier

System liquidity is banks' net reserve position with the Reserve Bank: call it `L_t`, the sum
banks hold at RBI net of what regulation requires them to hold. RBI's own liquidity-management
framework (RBI, *Liquidity Management Framework*, 2020; restated in every Monetary Policy Report's
"drivers of liquidity" section) decomposes its change into four "autonomous" drivers the central
bank does not directly choose — currency in circulation leaving or returning to bank vaults,
government cash-balance movements at RBI, RBI's own forex operations, and a residual — offset by
one "discretionary" lever, the Liquidity Adjustment Facility (LAF), through which RBI injects or
absorbs to keep the overnight rate near its policy target. Since 8 April 2022 the LAF corridor has
been the Standing Deposit Facility (SDF) as the **floor** and the Marginal Standing Facility (MSF)
as the **ceiling**, calibrated symmetrically around the repo rate — at introduction, SDF 25bp below
repo and MSF 25bp above it, replacing the fixed-rate reverse repo that had asymmetrically sat only
below the corridor before (RBI April 2022 monetary policy statement). The overnight **call money
rate**, whose volume-weighted average is the WACR, is the market print this corridor is built to
contain; an RBI internal working group has recently recommended WACR remain the operating target
of policy precisely because it is the cleanest reading of whether transmission is working
(*Business Standard*, Aug 2025, reporting the group's finding `[VERIFY: working group's formal
name/report not read directly]`). Collateralised triparty repo (TREPS, run by the Clearing
Corporation of India — CCIL) and market repo now carry roughly 98% of overnight money-market
volume, with the uncollateralised call segment a thin residual that nonetheless still anchors the
policy read (RBI liquidity commentary, reported *Business Standard*, April 2025). RBI's own
discretionary offset to a scheduled drain is not the corridor alone but a toolkit calibrated to how
long the drain is expected to last: variable-rate repo (VRR) auctions, typically one- to fourteen-
day tenors, are the standard response to a *transient* shortfall of exactly the advance-tax/GST
kind — the June 2026 episode cited above saw RBI clear two separate two-day VRR auctions, ₹50,016
crore and ₹22,284 crore, specifically to bridge the gap until the government's own spending cycle
returns the cash to the banking system — while variable-rate reverse-repo (VRRR) auctions absorb
the opposite, a persistent surplus, and outright open-market operations (OMO) or a change in the
Cash Reserve Ratio address a *durable* shift in the liquidity trend rather than a calendar spike.
That RBI itself reaches for a short-tenor, self-liquidating instrument specifically for these
dates — rather than a policy-rate move or a durable OMO — is itself evidence, from the operator who
actually manages the corridor, that the standard read of an advance-tax or GST print is mechanical
and temporary; a classifier that cannot distinguish the two is disagreeing with the central bank's
own revealed model of the event before any trial is even run.

Two elements of the fiscal calendar drain `L_t` **on dates fixed by statute**, not by market
conditions. First, advance tax: Income-tax Act §211 requires corporate and other qualifying
assessees to pay estimated annual tax in instalments due 15 June, 15 September, 15 December and 15
March — 15%, 45%, 75% and 100% of the estimated liability cumulatively by each date. Second, GST
settlement: the monthly GSTR-3B return and its associated cash-ledger payment fall due on the 20th
of the following month for regular monthly filers (CGST Rules; late filing draws a Section-47
fee). Both are cash movements *into* the government's account at RBI — the moment a taxpayer's
bank debits its deposit to pay tax, that reserve leaves the banking system's aggregate balance
sheet and sits in the Consolidated Fund's RBI account until the government spends it back out,
which does not happen on the same calendar. This is not a metaphor: it is exactly the "government
cash balance" driver in RBI's own liquidity accounting, and it is why press coverage of these
dates is a recurring, decade-spanning genre rather than a novel finding — "Liquidity tightens on
advance tax outflows" (*Business Standard*, June 2011), "As liquidity tightens, call money rate
jumps to 7% before easing" (March 2023, a fiscal year-end plus advance-tax confluence), "Banking
liquidity turns deficit after 3 months on tax outflows, cash drain" and "RBI injects ₹72,300 crore
as advance tax outflows squeeze liquidity" (both June 2026, the latter reporting WACR trading 12bp
*above* repo the same week) all describe the identical mechanical event recurring on a public
statutory calendar, fifteen years apart.

The arithmetic of *how much of the trading year* this touches is worth doing once, plainly, on the
module's own default parameters — not a fitted number, just a count. Sixteen statutory anchors a
year (four s.211 dates, twelve GSTR-3B 20ths) each open a window; with the module's stated
defaults of two business days before and one after (`pre_bd=2, post_bd=1`), each anchor's window
spans up to four business days. Sixteen anchors times four days is roughly sixty-four business
days a year sitting inside *some* drain window, against roughly 250 trading days a year on NSE —
about a quarter of the calendar. A second, non-obvious fact falls out of the same arithmetic:
every one of the four quarterly advance-tax months (June, September, December, March) *also*
carries that same month's GSTR-3B due date five calendar days later (15th, then 20th) — so the
four "big" quarters see a double-humped drain within an eight-to-ten-day span rather than a single
event, which is one honest reason the press record above clusters so heavily on March, June,
September and December specifically rather than spreading evenly across the year. Neither
observation is a magic number in the Contract §6 sense: both are exact counts on a statutory
calendar plus the module's own stated, config-owned window width, offered to show that the
false-positive exposure this module removes is not a rare corner case.

Formalize the contamination directly. Let a funding-stress classifier fire on day `t`,
`F_t ∈ {0,1}`, by some rank-based rule (a spread's own trailing percentile — never a fixed basis-
point threshold, per Contract §6) applied to WACR-minus-repo, CP spreads, or the CCIL/NSDL
funding-flow rank already inside L2's role text. Let `D_t ∈ {0,1}` mark a drain-window day and let
genuine stress episodes occur, independent of the calendar, on a small share `s` of days with
sensitivity `r = P(F_t=1 | genuine stress)`. Let the drain-window trigger rate be `q = P(F_t=1 |
D_t=1)`, high by construction — the whole point of a *scheduled* drain is that it moves the metric
predictably. With `f_D ≈ 0.25` the drain-window day-share computed above, precision (the share of
fires that are real) is

```
Precision = TP / (TP + FP) ≈ (s·r) / (s·r + f_D·q·(1−s))
```

Plug in stylized, clearly illustrative values chosen only to show the mechanism's shape — not a
measurement, since none exists for this entry — say genuine stress episodes on `s=2%` of days
with `r=0.8` sensitivity, and a drain-window trigger rate `q=0.9`: precision comes out near
`0.016 / (0.016 + 0.220) ≈ 6.8%` — over 90% of unfiltered fires would be calendar artifacts, not
stress, even with a classifier that is individually well-behaved on both legs. This is the
arithmetic case for `drain_window_mask`: it does not claim the excluded days carry zero
information, only that a classifier untouched by the calendar cannot tell a mechanical spike from
a real one on the metric's level alone, and that the false-positive rate scales linearly with how
much of the year the calendar occupies — which the count above shows is not small. Consistent with
the atlas's own "reduce-only in spirit" framing, the mask can only suppress a fire, never
manufacture one, and `H58-D1` (data-gated) is the design that will measure `q` and the mean-
reversion share against the ≥2x-base-rate and ≥80%-within-5-business-days bars already registered
— this chapter states the shape of the argument the trial will grade, not its result.

### A.2 Earnings-announcement gap risk, formally, and why it is not harvested

Decompose a name's daily log-return variance into a diffusion part and, on an announcement date, a
discrete jump part: `Var(R_t) ≈ σ²_diffusion · Δt` on an ordinary day (variance scaling with
elapsed trading time, the textbook diffusion assumption), while on the announcement date `t*`,
`Var(R_t*) = σ²_diffusion · Δt + σ²_gap`, where `σ²_gap` is a one-time, non-scaling mass reflecting
a full quarter's information resolving discretely rather than diffusing continuously — Ball and
Brown's (1968) founding result that accounting income numbers carry real information content, most
of it (by their own estimate, 85–90%) already reflected in prices by the announcement month, with
the remainder arriving as exactly this kind of discrete jump rather than a further slow drift. The
cross-country evidence for `σ²_gap`'s size and where it lives is direct: Barber, De George, Lehavy
and Trueman (2013, *Journal of Financial Economics* 108(1), "The Earnings Announcement Premium
Around the Globe") find average returns across announcement months exceed non-announcement months
by over 11%/year across 46 countries, and — the mechanistically important part — the premium is
*strongest exactly where idiosyncratic volatility rises most around the announcement*, i.e. where
`σ²_gap` is largest relative to `σ²_diffusion`. Frazzini and Lamont (2007, NBER WP 13090, "The
Earnings Announcement Premium and Trading Volume") document the US version at 7–18%/year excess
return with volume the common driver, evident back to 1927 but measurably weaker post-2004 (about
40bp/week lower average weekly excess return after 2004 than the prior decade) — a decay this
program's Governing Principle (Contract §5) would price in on its own even before considering
whether to harvest it.

The staged-entry pause is not an attempt to harvest that premium; it is the opposite move. A
tranche scheduled inside `[t*−pre_bd, t*+post_bd]` is filled at a price drawn from the
announcement's return distribution — high-kurtosis, `σ²_gap`-loaded — with no say over which tail
it lands in. Frame it against a genuine short straddle: an option seller who is short gamma into an
announcement is *paid a premium* for bearing exactly this jump risk, sized and timed by choice. A
mid-build staged-entry tranche is short the same gamma — worse-than-average execution on the good-
news side and only accidentally cheap on the bad-news side — while receiving nothing: it is short
gamma for free. Harvesting the Barber-et-al./Frazzini-Lamont premium would require the *opposite*
construction: a deliberate, sized, timed long position established *before* the announcement
window opens by design, with its own decay-survival argument and haircut under Contract §5 — a
proposal this ops module explicitly does not make. `results_pause_mask` only defers; it does not
recommend a direction, and the calendar it consumes is supplied by the caller (exchange results
announcements), never scraped inside the module itself, matching the docstring's own boundary.

### A.3 Expiry-day microstructure: pinning, rollover, and why the close is a biased print

Avellaneda and Lipkin (2003, *Quantitative Finance* 3(6), "A Market-Induced Mechanism for Stock
Pinning") formalize why a heavily-optioned name's close tends toward the nearest large strike on
expiry day: if open interest on a strike is unusually large, aggregate delta-hedging by the market
makers short that gamma is itself a large, price-sensitive order flow, entering the stock's own
price process as a **singular drift term** that grows as time-to-expiry shrinks and as price nears
the strike — large open interest, low realized volatility relative to that open interest, and
little time left all push the drift term's influence up. The model derives a finite, positive
probability the stock closes pinned to that strike as a function of volatility, time-to-maturity,
open interest, and a price-elasticity constant. The mechanism is the hedgers' own flow, not
information: nothing about the day's news content changes; the close is *set*, in part, by a
feedback loop between option sellers unwinding into their own hedge.

Layer on rollover: as a near-month future or option approaches expiry, open interest must migrate
to the next month, concentrating basis-crossing trades into the expiry session specifically.
Stoll and Whaley's triple-witching literature (Stoll & Whaley, 1986 and 1990/1991, on S&P 500
futures/options/options-on-futures simultaneous expiries) found volume in the last half-hour of an
expiring session running roughly 40% of the average month-end open interest during 1984–85, with
volatility evidence more mixed — real but "mostly temporary and small" where an effect is found at
all, and its *location* itself an artifact of settlement design: after the exchange moved index-
futures settlement from the Friday close to the Friday open (June 1987), the excess volume and
volatility measurably relocated from the close to the open along with the settlement price it was
chasing. That relocation result is the cleanest evidence that what is being observed on an expiry
day is not "the market is more informative that day" but "wherever the mechanical settlement price
is fixed, flow concentrates there" — a pure microstructure fact, portable to any market with a
cash-settled derivative and a fixed settlement reference.

This licenses the design choice precisely: `expiry_days` exists not because expiry-day *returns*
are reliably larger (the evidence for that is mixed even in the most-studied market on earth) but
because the expiry-day *close* is disproportionately explained by unwind and rollover flow rather
than information, which makes it a poor input for a weekly-cadence system that treats the EOD
print as ground truth for a rebalance decision. A rebalance benchmarked to a pinned or rollover-
distorted close inherits a transient, mechanically-set level into its target weights — noise
purchased at a price, not a risk the desk is compensated to hold. `H58-D3` (data-gated) will
measure |close-to-close| and closing-auction behavior on India's own expiry sessions against
matched weekdays; this chapter states why the question is worth measuring, not its answer.

An honest gap belongs on the record here rather than papered over: this chapter did not locate a
published India-specific pinning study analogous to Avellaneda-Lipkin's original US estimation, nor
a peer-reviewed measurement of closing-auction distortion specific to NSE or BSE index derivatives
`[VERIFY: an India pinning/expiry-microstructure paper may exist in the market-microstructure
literature and was not surfaced by this session's search]`. The design choice this entry makes —
avoid the day rather than model the pin — does not depend on that literature existing: Stoll-
Whaley's own finding that the distortion *relocates* with the settlement mechanism, rather than
disappearing, is a portable structural argument on its own, and `H58-D3`'s frequency count is
designed to stand on India's own bhavcopy record regardless of whether a formal India pinning
estimate is ever published.

### A.4 Index reconstitution: the demand-curve literature, formally, and the momentum exclusion

Shleifer (1986, *Journal of Finance* 41, "Do Demand Curves for Stocks Slope Down?") is the founding
result: stocks newly added to the S&P 500 earn a significant positive abnormal return at the
announcement that does not disappear within ten days, sized with measures of index-fund buying —
direct evidence against the null that demand for a large, liquid stock is perfectly elastic.
Model it simply: `P_added = P* + λ · (ΔD_passive / float)`, a price-pressure coefficient `λ > 0`
translating forced passive demand into a price level shift with no new information about `P*`
itself. Harris and Gurel (1986, *Journal of Finance* 41, "Price and Volume Effects Associated with
Changes in the S&P 500 List") measured the shift directly: prices rose over 3% immediately after
an addition announcement and the move was "nearly fully reversed" within two weeks — the
*temporary* price-pressure component, as distinct from any permanent re-rating. Chen, Noronha and
Singal (2004, *Journal of Finance* 59(4), 1901–1929, "The Price Response to S&P 500 Index
Additions and Deletions: Evidence of Asymmetry and a New Explanation") found the asymmetry that
gives the effect its modern shape: a *permanent* price increase for additions but no permanent
decline for deletions, which they attribute to a shift in investor awareness (a Merton (1987)
investor-recognition mechanism) rather than to price pressure alone, since price pressure predicts
symmetric effects and the data do not show them.

The effect's own decay is itself now a headline literature result, and it matters here precisely
because Contract §5 asks every signal to answer why it survives being known. The addition
abnormal return has fallen from an average near 7.4% in the 1990s to under 1% over the past decade
on some measures, with median excess returns to additions moving from roughly 8.3% (1995–99) to
essentially zero, slightly negative, over 2011–21 on others (Patel & Welch, 2017, and updated in
Greenwood & Sammon, 2025, *Journal of Finance*, "The Disappearing Index Effect") — attributed to
the rise of ETF market-making, arbitrage capital specifically targeting the announcement window,
and markets simply becoming more efficient at pricing a known, calendar-fixed flow. This is the
textbook shape of an anomaly meeting arbitrage capital (McLean & Pontiff, 2016, cited already at
Contract §5) and it is why any special-situations sleeve harvesting this effect in India carries a
stated numeric decay haircut and frozen Tier-B parameters rather than being sized as a stable edge.

India's transfer of the mechanism is a matter of AUM, not analogy: passive funds and ETFs tracking
Nifty-family indices held roughly ₹7.1 lakh crore across 391 funds as of end-February 2025, about
73% of total Indian passive AUM (NSE, *Nifty Passive Insights Quarterly Update*, Jan–Mar 2025) —
real, forced, calendar-dated demand that must transact at or near the effective date regardless of
view. NSE Indices' own methodology reviews Nifty 50 semi-annually (March and September effective
dates, on six-month average free-float market cap windows ending January and July respectively)
with roughly four weeks' prior notice between announcement and effective date. That four-week gap
is the exact mechanism this section's second, non-tradeable leg targets: between announcement and
effective date, anticipatory positioning by index arbitrageurs produces the Harris-Gurel-style
run-up *before* any passive fund is required to transact — a mechanical, calendar-terminated,
one-time level shift, not information diffusing under-reaction (the mechanism L3/L4's momentum
composite actually harvests). If a 6–12 month momentum lookback window happens to straddle a
name's own announcement-to-effective window, the trailing return used to rank it is contaminated
by a flow artifact with a known expiry, not a persistent signal — precisely the "don't mistake the
pop for momentum" clause in the atlas's own line 127. RC1 (data-gated; `research/register/
trial-ledger.md`) registers the event study that will size this for both legs: the special-
situations sleeve's harvestable pre-effective drift (Tier B, capped, aggressive book only per
Contract §10, carrying the Patel-Welch/Greenwood-Sammon decay prior before any India print lands)
and the momentum-hygiene exclusion, which needs no trial to adopt since it follows from what the
pop *is*, only from RC1 to size.

---

## Part G — Operator psychology: the plumbing-versus-information confusion under stress

A WACR print jumping to 7%, or a two-day funding-stress fire lighting up on 15 September, reads to
a trained eye exactly like the opening of a real freeze — the same raw shape a screen showed in
September 2018. This is not carelessness; it is the availability heuristic doing exactly what it
evolved to do, retrieving the most vivid, most recently rehearsed analogue the moment a metric
crosses a line. The honest antidote is not vigilance, which the heuristic defeats by definition,
but a *falsifiable distinguishing test* run before the pattern-match is trusted — which is exactly
what this program's own IL&FS-window trial already supplies. SC1 (`research/register/
trial-ledger.md`, Entries SC1–SC2) tested the IL&FS crunch (September 2018–August 2019) against a
declared bar and found the freeze's own signature was **broad and persistent**: small-cap factor
returns in the bottom 18th percentile of all rolling twelve-month windows since 1994, with the
market factor *also* in its own bottom 16th percentile over the same window — a twelve-month,
market-wide propagation, not a two-or-three-day rate print. A statutory-drain fire, by construction
and by `H58-D1`'s own registered acceptance bar, is supposed to mean-revert within five business
days in at least 80% of instances precisely *because* it has no persistence mechanism behind it —
the government spends the cash back out, the corridor pulls WACR back toward repo, and nothing
about bank balance sheets or NBFC funding structures has changed. "Feels like 2018" is the wrong
register to reason in exactly because 2018's tell was duration and breadth, not the print's peak
level on day one — and the desk now has its own measured number saying so, not just an argument.

The harder discipline is not spotting the false alarm; it is resisting the seduction of turning
every mechanical fact this module knows into a traded edge. Once a desk can see that GST and
advance-tax dates drain liquidity on a public schedule, that options market-makers pin names to
strikes on expiry day, and that passive funds must buy a known name on a known date, the pull to
ask "so why not trade around each of them" is immediate and, on the page, plausible. The answer is
the same one this program already gave itself in a different microstructure corner: the atlas's
own rejection of an options-premium-harvesting sleeve records that "no capacity, structural, or
risk-premium argument distinguishes this book from the many already-professionalized desks on the
other side of that trade" (`research/dossiers/12-india-microstructure-specials.md`, the D12
rejection). The identical sentence applies here without editing a word. The counterparty on a
pinning trade is a continuously-hedging options market-maker watching order flow tick by tick
through the session — a weekly-cadence, EOD-data desk sees only the day's close, structurally the
*last* participant to know anything the pin itself already encodes, which makes it a liquidity-
taker in that game by construction, never a liquidity-provider paid to be there. The counterparty
on reconstitution front-running is a dedicated event-driven or index-arbitrage desk positioned
within hours of the announcement, unwinding into the passive flow at the effective-date close — a
speed game this program's cadence cannot enter, any more than the fast-crash floor in Contract §7
Prior 8 pretends a weekly rebalance can dodge a five-week 38% fall. "No alpha claim" is not a
disclaimer bolted onto the module's documentation after the fact; it is load-bearing code:
`test_no_alpha_surface` walks the module's own namespace and asserts that no attribute name
contains `signal`, `alpha`, `tilt`, `direction`, or `score` — a substring ban enforced by the test
suite itself, so that a future edit adding a return-prediction path to what is meant to be pure
date arithmetic fails CI on the spot rather than depending on a reviewer's memory of this
paragraph. The module's entire ambition, stated plainly, is to make three other modules — L2's
stress classifier, the staged-entry executor, the rebalance scheduler — stop mistaking known
plumbing for news; it was never meant, and is now structurally prevented from becoming, a fourth
return line of its own.

---

## Part B — Cross-country evidence in specification detail and dated case studies

The genus these four atlas entries share with the rest of the world is exactly this: a public,
calendar-fixed rule inside market plumbing — tax remittance law, derivatives settlement design, or
an index committee's own published methodology — producing a price or funding-rate move that is
mechanical rather than informational, and that a naive detector will misread as news precisely
because it arrives with news-sized magnitude. What follows sets India's four instances against
their closest developed-market analogues (US quarter-end funding stress, Japan's fiscal year-end
squeeze, and the S&P index-effect literature's own decay in full specification) before turning to
roughly six dated India cases — this program's standing convention of doubling India's share holds
here as everywhere else in the series.

**US-1: the September 2019 repo blowup, the canonical scheduled-drain-gone-wrong.** On 17 September
2019, SOFR jumped from 2.43% on the 16th to 5.25%, touching 10% intraday — the US money market's
own version of a known-calendar liquidity drain colliding with an already-thin reserve buffer. The
Office of Financial Research's retrospective (Copeland, Duffie & Yang, 2023, "Anatomy of the Repo
Rate Spikes in September 2019," OFR Working Paper 23-04) attributes the spike to the *confluence*
of ordinarily survivable, individually known events: the 16 September corporate quarterly-tax
deadline draining bank reserves into the Treasury's account (functionally identical to India's
s.211/GSTR-3B mechanism — a calendar-fixed fiscal remittance pulling cash out of the banking
system into the sovereign's own account) landing on the same day as a large new Treasury coupon
settlement, against a declining aggregate level of bank reserves post-quantitative-tightening; the
Fed's own account adds that limited transparency across a segmented dealer market meant some
lenders never learned cash was scarce until it was too late to lend into the squeeze. The lesson
this program takes is not "the Fed should have anticipated it" (it substantially did — the *known*
date was on every desk's calendar) but that even a fully anticipated, calendar-fixed drain can
become genuinely disruptive when it lands on a reserve-scarce day — precisely the reason `H58-D1`
*quarantines* a drain-window fire rather than silently vetoing it, and why L2's two-of-three
confirmation architecture (`config/ladder.yaml`'s L2 role text) is designed to let a real crisis
that happens to straddle a drain date still get through.

**US-2: quarter-end window dressing as the drain's regulatory cousin.** A distinct but related US
and European phenomenon: banks facing a Basel leverage-ratio or G-SIB-surcharge calculation on a
reporting date temporarily shrink their repo books around quarter-ends specifically, producing a
mechanical funding-market wobble around a regulatory calendar rather than a fiscal one (ECB
Macroprudential Bulletin, Dec 2023, "Policy options to address window dressing in the G-SIB
framework"; the Basel Committee's own December 2018 statement on leverage-ratio window-dressing
behaviour). The shared structural feature with India's statutory drain — and the reason it belongs
in this genus rather than in a separate one — is that the calendar is *known and public in advance*
(quarter-end reporting dates are a fact of the regulatory framework, not a market surprise), yet
the resulting funding-market print still looks, in raw magnitude, like distress to an untrained
classifier.

**Japan-1: fiscal year-end (31 March) funding pressure.** More than three-quarters of Japanese
listed companies close their fiscal year on 31 March, and the domestic banking system's balance-
sheet behavior around that date — the so-called "Japan premium" in dollar funding, where Japanese
banks have at times paid a premium over other banks for otherwise-identical repo and swap
transactions — has generated a substantial BIS/BOJ working-paper literature on cross-currency
basis widening around fiscal year-ends `[VERIFY: this chapter located the literature's existence
and general mechanism (BIS WP 708 and adjacent BOJ working papers) but did not pin an exact
magnitude for the March-specific premium spike, as distinct from the broader post-2014 basis-
widening trend]`. The structural parallel to India is direct: a corporate fiscal-year-end (India's
own 31 March, atlas entry 4.2, already seated in `docs/cycles/33-calendar-signal.md`) compounds
with statutory tax remittance dates to concentrate multiple mechanical calendar events inside the
same short window — precisely why March is a recurring name in the Indian liquidity-stress press
record cited in A.1 above.

**Global-1: the S&P index-effect decay, in full specification.** The methodological arc is worth
restating with its exact event-study design choices, since India's RC1 will need to replicate the
shape, not merely the headline number. Shleifer (1986) and Harris & Gurel (1986) both use standard
announcement-to-effective-date event windows around S&P 500 committee decisions, with Harris-Gurel
explicitly separating the *announcement-date* price-pressure spike (>3%) from its *two-week*
reversal to isolate temporary pressure from any permanent re-rating. Chen-Noronha-Singal (2004)
extend the window further past the effective date specifically to test the asymmetry hypothesis,
finding the post-effective-date behavior of additions and deletions diverges in exactly the way a
pure price-pressure model (which predicts symmetric reversal) cannot explain, motivating their
investor-recognition account instead. Greenwood & Sammon (2025) then re-run the full chronology
1990–2021 on a rolling basis rather than a single pooled sample specifically to date the decay
itself — the empirical design choice (splitting the sample into rolling multi-year buckets rather
than one full-period average) is what lets them show the addition premium crossing from positive
to negative gradually across the 2000s and 2010s rather than jumping at one date, consistent with
arbitrage capital arriving progressively rather than all at once (Chordia, Subrahmanyam & Tong's
attenuation-with-crowding mechanism, Contract §5). A related, more recent design choice worth
naming: Vijh (2022, *Financial Management*, "Negative Returns on Addition to the S&P 500 Index and
Positive Returns on Deletion?") deliberately re-runs the event study using the S&P 400 (mid-cap) as
the *counterfactual* index a deleted or non-added stock would otherwise sit in, rather than the
broad market — a specification refinement that matters for RC1's own design, since a name dropped
from Nifty 50 typically falls straight into Nifty Next 50, an investable, actively-tracked index in
its own right rather than an unindexed void, meaning the "no permanent decline for deletions"
result cannot be taken off the US shelf unmodified: India's own reconstitution ladder (Nifty 50 →
Next 50 → 500 → Microcap 250, each independently tracked) makes the counterfactual-index choice a
first-order design decision for RC1, not a footnote.

**India-1: the 2018–19 IL&FS-era funding spikes versus ordinary advance-tax spikes — persistence as
the discriminator.** Already argued in Part G on the psychology side; restated here as the case's
own factual record. IL&FS's first default (commercial paper and inter-corporate deposits, roughly
₹450 crore) came in June 2018; the escalatory default wave landed 4 September 2018, with the
government superseding the board and moving the group to the NCLT by 1 October 2018 — a sequence
of downgrades and rollover failures stretching across a full quarter, not a single print. This
program's own SC1 trial (cited above) measured the propagation directly on real India factor data:
small-cap returns in the bottom-decile-adjacent 18th percentile and market returns in the 16th
percentile over the twelve-month crunch window — a signature the module's five-business-day
reversion bar is explicitly built to *fail to match*, which is the entire point of `H58-D1`'s
acceptance design.

**India-2: demonetisation (November 2016) — the drain signature briefly inverted.** From November
2016, India's banking system flipped from a chronic liquidity *deficit* (RBI injecting an average
near ₹28,365 crore a month over 2011–2016) to a liquidity *surplus* so large RBI averaged roughly
₹95,070 crore a month in *absorption* operations instead — banks collected upward of $120 billion
in new deposits within weeks of the note ban, managed initially via reverse repo and the Market
Stabilisation Scheme before RBI settled into variable-rate reverse-repo operations as the standing
absorption tool. The case matters here as a documented limitation, stated plainly: the H58 drain-
window mask assumes the *usual* direction of a scheduled outflow (a mechanical tightening event,
pushing WACR up toward or through repo), an assumption that plausibly weakens or inverts during an
extended liquidity-glut regime, where the same tax/GST cash movement instead merely trims an
outsized surplus rather than creating a deficit-driven stress print. The module's business-day
windows do not themselves distinguish a surplus regime from a deficit regime — that conditioning,
if it is ever needed, is a job for whatever regime state feeds L6 and L2, not for this pack's date
arithmetic, and is noted here as an honest boundary rather than resolved.

**India-3: GST rollout (1 July 2017) — the drain calendar itself changed regimes.** Before GST,
indirect-tax remittance sat on a patchwork of separate state VAT, central excise and service-tax
due dates, each on its own schedule; GST's rollout consolidated the monthly indirect-tax drain onto
a single calendar date across the whole economy. Even that single date was not stable at launch:
GSTR-3B itself was announced as an explicitly temporary, simplified stop-gap return (Finance
Minister Arun Jaitley's announcement, 18 June 2017) while the fuller GSTR-1/2/3 ecosystem was still
being built, and its due-date mechanics carried transition-period relaxations in the first two
filing months before settling into the now-familiar 20th-of-the-month convention. The case matters
for exactly the reason Part C below states as a data-engineering pitfall: any attempt to backtest
"monthly drain-date" behavior across a pre-2017 and post-2017 sample is measuring two structurally
different calendars, not one continuous series, and the module's `statutory_drain_dates` function
should not be applied mechanically to years before the regime it describes existed.

**India-4: the 2024–25 SEBI F&O curbs and the expiry-weekday reshuffle — the case for treating
weekday as config.** SEBI's October 2024 circular (reported as SEBI/HO/MRD/TPD-1/P/CIR/2024/132,
dated 1 October 2024 `[VERIFY: circular number as consistently reported by secondary sources;
this chapter did not fetch SEBI's primary circular text]`) restricted each exchange to a single
weekly-expiry benchmark index, effective 20 November 2024 — NSE retaining Nifty, BSE retaining
Sensex, both discontinuing weekly expiry on Bank Nifty, Nifty Financial Services, Nifty Midcap
Select, Nifty Next 50, Bankex and Sensex 50, alongside a minimum contract-value floor near ₹15
lakh. That alone collapsed what had been, in the years before, a market-wide cadence of an index
options expiry landing on several different weekdays across the week (each of the discontinued
products having carried its own weekly-expiry weekday `[VERIFY: exact pre-2024 per-product weekday
mapping]`) down to essentially two names. The weekday itself then moved twice within a single year:
BSE's Sensex weekly shifted from Friday to Tuesday effective 1 January 2025, then a further
exchange-wide reshuffle moved NSE's Nifty weekly from Thursday to Tuesday and BSE's Sensex weekly
from Tuesday to Thursday, both effective 1 September 2025 — ending, on NSE's side, a twenty-five-
year-old Thursday-expiry convention in one stroke (multiple press accounts, `[VERIFY: exact
underlying circular numbers for the September 2025 reshuffle]`). Retail losses in the equity
derivatives segment, concentrated overwhelmingly in weekly index options, ran ₹1.05 lakh crore in
FY2024-25 (up 41% from ₹74,812 crore the year before, 91% of individual traders net losers) before
SEBI's own measures are credited with an 18% reduction to ₹91,685 crore in FY2025-26 alongside a
roughly 20% fall in unique F&O participants — the regulatory motive for the whole reshuffle, stated
in SEBI's own six-measure framework, being to de-concentrate exactly the pinning and rollover flows
Part A.3 formalizes. This case is this chapter's single most load-bearing piece of evidence for
why `expiry_days(dates, weekday, which="last")` takes weekday as a required argument with no
default, enforced by its own test (`test_expiry_weekday_must_come_from_config`, asserting a bare
call raises `TypeError`): a hardcoded Thursday would have been a silent, correct-for-years,
suddenly-wrong constant exactly at the point a real book depended on it. It is worth stating
plainly where this account improves on this program's own earlier record: dossier D12
(`research/dossiers/12-india-microstructure-specials.md`, §"Index-options expiry regime after the
SEBI 2024–25 curbs") flagged its own description of this episode as *recalled* rather than
verified — guessing at a constrained Tuesday/Thursday weekday-assignment rule and missing the
January 2025 interim step entirely — and asked, in its own words, for the weekday-assignment
detail to be "checked first in any follow-up pass." This chapter is that pass: live search this
session confirms the reshuffle was two steps, not one (BSE's Friday-to-Tuesday move effective 1
January 2025, then the full exchange-wide Tuesday/Thursday swap effective 1 September 2025), and
that the destination state has NSE on Tuesday and BSE on Thursday, not the reverse. D12's
narrative arc — a single, cleanly-dated SEBI intervention settling the weekday question once — is
corrected to: the SEBI framework moved twice within one calendar year, exactly the pattern that
justifies treating weekday as a live config value rather than a constant retired after one update.

**India-5: Nifty 50 reconstitution episodes, dated, with estimated flow sizes.** Four recent,
independently reported instances anchor the forced-passive-flow mechanism concretely. Adani
Enterprises replaced Shree Cement effective 30 September 2022, with brokerage estimates near $213
million of net passive inflow. Bharat Electronics and Trent replaced Divi's Laboratories and
LTIMindtree effective 30 September 2024 (announced 23 August 2024, the standard roughly four-week
notice). Zomato and Jio Financial Services replaced BPCL and Britannia Industries effective 28
March 2025. InterGlobe Aviation (IndiGo) and Max Healthcare Institute replaced Hero MotoCorp and
IndusInd Bank effective 30 September 2025 (announced 22 August 2025), with brokerage estimates near
$600 million and $400 million of passive inflow respectively — sums large enough, against India's
₹7.1-lakh-crore Nifty-tracking passive base (Part A.4), to move even a large-float name over the
few sessions bracketing the effective date. Each instance carries the same roughly four-week
announcement-to-effective gap in which anticipatory index-arbitrage positioning can run ahead of
the mechanical flow — precisely the window RC1 will need to isolate and exclude from any 6–12
month momentum lookback measured on these names shortly after inclusion.

**India-6: MSCI's quarterly cadence as a second, faster reconstitution clock.** Nifty's semi-annual
March/September calendar is not the only forced-flow clock India's equity market answers to: MSCI
runs a full quarterly review (February, May, August, November announcement dates, effective at
each following month-end) across its Standard, Small Cap and other India indices, a strictly
faster cadence than NSE Indices' own semi-annual schedule. The August 2026 review is a live,
dated instance: MSCI's India additions — reported to include Adani Energy Solutions, Lenskart and
Groww among four names — were estimated by brokerages to draw roughly $1.5 billion in passive
inflows at the review's effective date (*Business Standard*, 13 and 31 August 2026). The
operational consequence for this module is direct: a name can carry *two independent* forced-flow
calendars at once — its own Nifty-family effective dates and its MSCI quarterly effective dates —
and RC1's event-study design must track both rather than assuming NSE Indices' semi-annual
calendar is the only mechanical-flow date a given constituent faces, since a momentum lookback
spanning an MSCI quarterly effective date is exposed to the identical contamination risk A.4
formalizes for Nifty's own reconstitution.

**India-7: T+1 settlement (27 January 2023) — the plumbing itself compressed the drain's timing.**
India's phased move to T+1 settlement (beginning with the smallest 100 stocks in February 2022,
completing across all listed equities by 27 January 2023, making India the second major market
after China to run T+1 as standard) shortened the gap between a trade and its cash/liquidity
consequence market-wide. The relevance here is structural rather than directional: any mechanical
event whose *liquidity* impact was previously spread across a T+2 window now clears a day sooner,
meaning the precise business-day offsets this module's `pre_bd`/`post_bd` parameters encode are
themselves settlement-regime-dependent facts, not universal constants — another instance, alongside
India-4's expiry weekday, of a plumbing parameter this program deliberately keeps in config rather
than in code.

---

## Part C — India data engineering: free pipelines, and where the seams are

**Call money, TREPS and WACR.** ClearCorp (CCIL's subsidiary) publishes a daily call-money-market
summary — trades, volumes, weighted average rates and rate range across dealt and reported segments
— freely on its own site; RBI's Database on Indian Economy (DBIE, `data.rbi.org.in/DBIE`) carries
the WACR series in its money-market tables, the natural home for the A.1 spread construction. TREPS
volumes, now roughly 98% of overnight money-market activity, are reported in RBI's periodic
liquidity commentary and Monetary Policy Reports rather than a single clean daily download; a
robust pipeline should treat CCIL's call-money print as the headline series and RBI's own
liquidity commentary as the qualitative cross-check on which segment is actually moving.

**RBI's daily LAF position.** RBI publishes daily money-market operations (repo/reverse-repo/SDF/
MSF/VRR/VRRR volumes and cut-off rates) and periodic system-liquidity estimates through its Weekly
Statistical Supplement and Monetary Policy Report liquidity-driver tables — free, if less
uniformly machine-readable than a single time series; this is the natural home for the "drivers of
liquidity" decomposition in A.1 (autonomous drivers versus LAF offset).

**Exchange results calendars.** NSE and BSE both maintain free corporate-announcement archives
(`nseindia.com` corporate announcements, `bseindia.com` corp announcements) that carry scheduled
board-meeting and results dates; per Contract §3 and this module's own docstring, this calendar is
always *supplied* to `results_pause_mask` by the caller from these archives, never scraped inside
`exclusion_calendar.py` itself.

**NSE expiry calendars and the circular trail.** NSE's circular archive (`nsearchives.nseindia.com/
content/circulars/`) is the primary source for expiry-weekday changes; India-4 above is the load-
bearing case for pulling the *exact* circular numbers and effective dates before hardcoding any
weekday into a runtime config, rather than trusting secondary reporting — several of the specific
circular numbers cited in this chapter are flagged `[VERIFY]` for exactly that reason, and a real
pipeline should resolve them against NSE's own archive rather than this chapter's press-derived
citations.

**Index-provider reconstitution announcements.** NSE Indices publishes its own semi-annual review
methodology and press releases (`niftyindices.com`) with the March/September effective-date
cadence and roughly four-week announcement lead described in A.4; MSCI publishes its quarterly
review calendar (announcement and effective dates for February, May, August and November reviews)
on its own site, free to read though the underlying index weights themselves are licensed.

**Alignment pitfalls.** Four are worth stating explicitly, since each has bitten a naive
implementation of exactly this kind of calendar logic before: (1) due-date shifts when the 15th or
20th falls on a bank holiday or weekend — both CBDT (advance tax) and CBIC (GSTR-3B) circulars
routinely extend a due date to the next working day, which the module's own `holidays` parameter
exists to absorb, but only if the caller supplies the correct exchange/CBIC holiday list for the
relevant year — the docstring's own words, "a supplied refinement, not assumed," mean an empty
`holidays=None` call silently uses the *unshifted* statutory date, a genuine trap for anyone who
forgets to pass the list; (2) the T+1 settlement-era timing compression described in India-7, which
changes what "two business days before" actually means in cash-liquidity terms pre- versus post-
27-January-2023; (3) the GST-regime break described in India-3, where `statutory_drain_dates`
applied to a pre-July-2017 year describes a calendar that did not yet exist; and (4) results
announced intraday versus after market close — the module's `results_pause_mask` works entirely in
business-day units and cannot itself distinguish a same-session intraday announcement (historically
more common among a handful of public-sector names, now rare) from the now-standard post-3:30pm
release, meaning an intraday-announced result carries a same-day gap risk the `pre_bd`/`post_bd`
window only partially captures unless the supplied results calendar itself flags announcement
timing — a limitation to document in the caller, not a bug in the date arithmetic.

---

## References

Ball, R. & Brown, P. (1968), "An Empirical Evaluation of Accounting Income Numbers," *Journal of
Accounting Research* 6(2), 159–178. Barber, B., De George, E., Lehavy, R. & Trueman, B. (2013),
"The Earnings Announcement Premium Around the Globe," *Journal of Financial Economics* 108(1),
118–138. Frazzini, A. & Lamont, O. (2007), "The Earnings Announcement Premium and Trading Volume,"
NBER Working Paper 13090. Shleifer, A. (1986), "Do Demand Curves for Stocks Slope Down?," *Journal
of Finance* 41(3), 579–590. Harris, L. & Gurel, E. (1986), "Price and Volume Effects Associated
with Changes in the S&P 500 List," *Journal of Finance* 41(4), 815–829. Chen, H., Noronha, G. &
Singal, V. (2004), "The Price Response to S&P 500 Index Additions and Deletions," *Journal of
Finance* 59(4), 1901–1929. Patel, A. & Welch, I. (2017 working-paper lineage) and Greenwood, R. &
Sammon, M. (2025), "The Disappearing Index Effect," *Journal of Finance*. Avellaneda, M. & Lipkin,
M. (2003), "A Market-Induced Mechanism for Stock Pinning," *Quantitative Finance* 3(6), 417–425.
Stoll, H. & Whaley, R. (1986, 1990, 1991), the triple-witching/expiration-day-effects literature on
S&P 500 futures and options settlement. Copeland, A., Duffie, D. & Yang, Y. (2023), "Anatomy of the
Repo Rate Spikes in September 2019," Office of Financial Research Working Paper 23-04. RBI,
*Liquidity Management Framework* (2020) and successive Monetary Policy Reports' liquidity-driver
sections. Press sources for dated India events are cited inline by outlet and date per Contract
§12; several circular numbers and one magnitude claim carry `[VERIFY]` tags above pending primary-
source confirmation.

---

# Parts D–H — calendar mechanics (atlas 4.3/4.4/4.5 = H58 ops pack; 4.6 = RC1 edge + exclusion)

## Part D — Econometrics of an entry with no trials, on purpose

This entry runs ZERO trials and that is its design, stated before any data lands: every claim
here is about MECHANICS — flows forced by statute, settlement, or index rules — and mechanics
are graded by frequency counts, not hypothesis tests. The four registered designs (trial
ledger, 2026-09-02) are counting exercises with their acceptance shapes fixed now:

- **H58-D1** is the only one with a bar, because it must EARN a suppression rule: quarantining
  L2 funding fires inside drain windows is justified only if drain-window fires are ≥2x the
  base rate (the calendar actually attracts fires) AND ≥80% of them mean-revert within 5
  business days (they are mechanical, not stress). The formal point: a stress classifier's
  precision is degraded by scheduled spikes exactly in proportion to their rate ratio — but a
  suppression rule that fires during a REAL crisis that happens to straddle Sep 15 is the
  catastrophic failure mode, which is why the rule QUARANTINES (flags for confirmation by the
  other two L2 legs) and never vetoes alone. The two-of-three confirmation architecture in
  L2's role already provides the override path; the ladder.yaml role text now carries it.
- **H58-D2/D3** are frequency reports with no bar: prudence rules whose cost (a tranche
  deferred a day or two) is bounded and whose benefit (a gap or a pinned close not bought)
  needs measuring, not proving.
- **RC1** is the entry's only alpha-adjacent object and it points AWAY from the ladder: the
  reconstitution pop is a special-sits sleeve question (Tier B, capped, aggressive book only,
  per CONTRACT §10) plus a HYGIENE rule for everyone else — an add's pre-effective pop is a
  one-time demand-curve level shift (Shleifer lineage) and must be excluded from L3/L4
  momentum lookbacks, or the trend legs buy a flow artifact. The exclusion needs no trial:
  it follows from what the pop IS; RC1 measures its size for the sleeve, not its existence.

## Part E — The algorithm (quant/ladder/exclusion_calendar.py, seated as ops)

Three deterministic calendars, seven exact tests, suite 87 green:
`statutory_drain_dates(year)` — the sixteen statutory dates (four s.211 advance-tax
instalments + twelve GSTR-3B due-20ths); `drain_window_mask(dates, pre_bd=2, post_bd=1)` —
business-day windows around them (numpy busday; exchange holiday lists a supplied
refinement); `results_pause_mask(tranches, results_dates)` — flags staged-entry tranche
dates crossing a SUPPLIED results calendar (never scraped); `expiry_days(dates, weekday)` —
last-weekday-of-month arithmetic where the weekday is a REQUIRED argument with no default:
the 2024-25 SEBI curbs and exchange weekday reshuffles make any hardcoded expiry day a
latent bug, so config owns it per (exchange, era) and a test enforces that a bare call
raises. The namespace contains no signal/alpha/tilt surface and `test_no_alpha_surface`
asserts it stays that way — the pack excludes and defers; it never recommends.

Consumption: L2's funding leg (quarantine, two-of-three override); the staged-entry
executor (defer past results windows); the rebalance scheduler (skip expiry days). All three
are execution-layer; none touches a budget block.

## Part F — Harvest map

Harvested now: the H58 ops rules (above) wired into L2's role text with provenance; the
momentum-hygiene exclusion stated as a rule for the L3/L4 build (reconstitution pops out of
lookbacks — implementation lands with the equity cross-section, where the add/drop lists
live). Registered, data-gated: H58-D1/D2/D3 counting designs; RC1 event study for the
special-sits sleeve. Nothing else — this entry's honest yield is plumbing-awareness, and the
budget it touches is zero.

## Part H — Knowledge ledger

**Established (mechanics, not measured by us):** the drain calendar itself (statute); expiry
and reconstitution dates (exchange/index rules) — these are facts of the plumbing, not
hypotheses. **Pooled-prior (literature, Tier B):** scheduled liquidity drains spike funding
rates (RBI's own liquidity commentary; the US Sep-2019 repo episode as the canonical
extreme); index-inclusion demand effects large in the 1990s-2000s US and DECAYING
post-2010 (Patel-Welch lineage) — the decay prior applies to India's version before RC1
prints. **Awaits India data:** all four designs. **Unknowable:** whether the next real
funding crisis straddles a drain date — which is exactly why the quarantine flags and the
two-of-three architecture decides, never the calendar alone.

Verdicts: 4.3/4.4/4.5 EXECUTION rules seated (ops pack, no alpha claim, tests enforce the
framing). 4.6 split: special-sits EDGE design registered (RC1, sleeve-side) + momentum
exclusion adopted as hygiene. No seat, no budget, no new ladder row — the entry's product
is that the fast layer stops lying to itself on sixteen known dates a year.

---

**Dated addendum (2026-09-03) — H58-D3a: the expiry day is an ordinary Thursday, at index
resolution.** The design's index partial ran (224 monthly expiries vs 702 other Thursdays,
weekday-matched because the weekly-expiry era makes Thursday itself special): median
|close-to-close| 0.674% vs 0.574%, two-sided p=0.211, and weaker in both era splits. No
measurable index-level expiry noise — which is the correct null for this block, whose rule
was always mechanical prudence about single-stock CLOSE-AUCTION behavior (still
bhavcopy-gated), never an index alpha claim. The exclusion stays; nothing about it is now
owed an index justification.
