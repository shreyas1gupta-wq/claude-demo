# The Issuance/Sentiment Cycle — Full Monograph (Atlas 3.2, seat L7)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** L7 confirmed at its Tier-B seat — and it is the register's rare signal
expected NOT to fully decay: an issuer's incentive to sell expensive paper is structural
(nobody arbitrages a promoter's decision not to float). The decay haircut applies to the
MAGNITUDE, never the existence; the honest counters (Schultz's pseudo-timing critique, the
US predictor's OOS record) ride along in Part A.

**Machinery shipped:** quant/ladder/issuance_sentiment.py — the two-leg froth state (issuance
value/mcap + first-day-pop expanding percentiles; BOTH legs required for the froth signature;
n_legs degradation through no-listing months; reduce-only froth_flag for the special-sits
shrink rule; no short-signal path exists) + the issuers-chase-valuation fixture (planted chase
+0.8; froth 0.90 vs winter 0.21) + 4 tests; suite at 73. **IS1/IS2 registered data-gated**
(IS1's prior stated in the ledger; IS2 = the ladder's own changes_if episodes: 2018's freeze,
2023-24's frenzy).

**The record's anchors (Part B, verified against sibling monographs):** four top-ticks in
three decades (1994-96 free-pricing flood → vanishing companies; 2007-08 crowned by Reliance
Power's 73x subscription listing days from the all-time top; 2021's record raise falling 27%
on listing day; 2023-25's SME frenzy — average subscription 242x at the Sept-2024 peak — ended
by SEBI's Dec-2024 curbs, the ladder's institutional confirmation) + the Baker-Wurgler
scorecard wave-by-wave.

**Assembled from:** partA-theory-psychology.md · partB-cases.md · partCDEFH.md.

---

# PART A + G — The persistent incentive, the evidence, India's machinery, psychology

# Issuance / Sentiment Cycle Deep Dive — Part A & Part G

Part A: Theory — why issuance timing is the signal the desk expects NOT to fully decay ·
Part G: Operator psychology · v1.0 · 2026-09-02 · Atlas entry 3.2 (`docs/CYCLE_ATLAS.md` row
107: "Issuers sell paper when it's expensive (Baker-Wurgler) — a persistent INCENTIVE, not an
information gap; SEBI's 2024 SME crackdown is the institutional confirmation"); ladder seat
`L7_issuance_sentiment` (`config/ladder.yaml`). SEATED inside the `valuation_sentiment` block
(0.10 of regime score) alongside `L8_value_spread`, its block-mate — L8 is the value
composite's own cheapness-dispersion percentile, fully treated in
`docs/cycles/04-value-quality.md` (Part A §A.4, "the value spread as a state") and referenced
here only where the two legs jointly confirm; this file never re-derives L8's own construction.
Sibling documents: `research/cycles/issuance-deep/partCDEFH.md` (data engineering, the
two-leg-state mathematics, the algorithm, the harvest map, the knowledge ledger — already
written, cited throughout by name rather than re-derived) and a forthcoming `partB-cases.md`
(India episode record — 1994–96, 2007–08, 2018, 2021, 2023–25 — outside this file's scope by
instruction). Style and depth calibrated to
`research/cycles/fincycle-deep/partA-theory-psychology.md`. Evidence base: this file plus
`research/dossiers/08-india-mid-cycles.md` (D08, §F9–F12/I12 — the workstream that first
argued this seat into the ladder) and `research/dossiers/12-india-microstructure-specials.md`
(D12, §F5 — the SME-universe-exclusion argument this file inherits rather than re-litigates).
Status: theory and citations verified here; India magnitudes await the data phase and the
sibling cases chapter.

This file assumes the ladder's frozen construct as given: L7 is Tier B, `reduce_only: false`
(it can add *and* subtract regime score inside the shared `valuation_sentiment` budget, unlike
the Tier-C reduce-only entries elsewhere on the ladder), τ½ prior 12–24 months, decay carried
at the generic McLean-Pontiff 26–58% band as a placeholder pending its own pre-registered
India test, and a role stated in two clauses: "sentiment state" (the block-level regime-score
contribution) and "sizes the special-sits sleeve (froth => shrink)" — a second, independently
reduce-only consumption path feeding the aggressive book's satellite sleeve (Decision Q10,
`research/OPEN_QUESTIONS.md`). Part A supplies the theoretical machine that construct
compresses into a two-leg percentile state; Part G turns to the desk operating a signal built
on a psychology — IPO-day euphoria — every member of it has personally felt at least once.

---

## PART A — Theory: why issuance timing survives being known

### A.1 The object: an incentive, not an information gap

**(i) The distinction that matters.** CONTRACT §5 demands, for every signal, a written answer
to "why does this survive being known?" — with four acceptable categories: (i) a
structural/behavioral mechanism persistent under crowding, (ii) a capacity limit, (iii) a
genuine risk premium, (iv) an institutional constraint. Most signals on this ladder answer with
one of these, sometimes two at once (value's fork, `docs/cycles/04-value-quality.md` A.1.iii,
is exactly "(iii)+(i)"). The issuance/sentiment seat's honest answer is narrower and, for that
reason, unusually durable: it is almost purely **category (i)**, and the specific form of (i)
it takes — a persistent *incentive*, not an information gap — is what the atlas phrasing is
built to flag. An information-gap anomaly (say, an accounting ratio the market underweights)
decays because someone can learn the ratio matters and trade against the mispricing until it is
gone; the informational content is a fact that, once known, can be arbitraged away by anyone
with capital and the will to act on it. **An issuer's decision not to sell equity is not a fact
anyone else can trade against.** A promoter, CFO, or private-equity sponsor who believes their
own stock is overvalued has a standing, personal, repeatable incentive to sell paper into that
overvaluation — bonus economics, exit timing, cost-of-capital arbitrage, and simple wealth
maximization all point the same direction — and no third party's knowledge of "issuers time the
market" can force that issuer to sell *less* paper when the price is rich. The mechanism the
Atlas names, "issuers sell paper when it's expensive," is not a mispricing academics discovered
and crowding subsequently competed away; it is a description of what a rational, self-interested
issuer does *by construction*, in any market, in any decade, regardless of how many people have
read the paper documenting it. This is why the seat's decay treatment (§A.2.6, §A.4) differs in
kind from every other haircut on this ladder: the haircut applies to the **magnitude** of the
resulting market-return predictability (which crowded capital genuinely can and does compress,
per §A.2.5's honest counters), never to the **existence** of the underlying incentive, which no
amount of publication or crowding touches.

**(ii) The two faces the seat reads.** The Atlas's own harvest line ("REGIME + EDGE-sizing")
and the ladder's role field ("sentiment state; also sizes special-sits sleeve") both point to a
construct with two distinct observable faces, and the seat's entire design (§A.4;
`partCDEFH.md` Part D) is organized around keeping them separate before combining them.
**VOLUME** is the supply-side face: how much paper issuers choose to bring to market, scaled
against the market's own size (issuance value / market capitalization) so that a genuinely hot
issuance regime is distinguished from a merely large one in absolute rupee terms. This is the
face Baker-Wurgler's own aggregate-return result (§A.2.1) and the classical "hot issue market"
literature (Ibbotson-Jaffe, §A.2.3) are built on — issuers, in aggregate, choosing to sell more
relative to the market's size precisely when the market's own pricing makes that sale
attractive. **RECEPTION** is the demand-side face: how the market receives what is brought —
first-day listing pops (the gap between issue price and first trade, or first-close), and
subscription ratios (how many times a book is covered across its QIB/HNI/retail tranches,
§A.3.2) — a face with no clean US analogue as *free, granular, per-issue public data* the way
India's exchange-published subscription books provide it (§A.3.2), and the specific face Baker-
Wurgler's 2006 sentiment index (§A.2.2) elevates from a side observation to a first-class
component. Reading only VOLUME risks mistaking healthy capital formation (a growing economy
genuinely needing more primary capital, at ordinary valuations) for froth; reading only
RECEPTION risks mistaking a supply-scarce, well-priced issue's oversubscription for market-wide
euphoria. The seat's central design claim — developed fully in §A.4 — is that the froth
signature this ladder actually wants to flag requires **both legs elevated together**, and that
claim is exactly why the construct is a two-input state rather than either input alone.

**(iii) What this is not.** The seat is explicitly not a claim that any individual issuer, or
any individual investor's demand for an IPO, can be timed with precision — the ±20%-or-worse
timing uncertainty this program attaches to every Band-2/3 state (`docs/CYCLE_ATLAS.md` §0)
applies here as everywhere. It is a claim about a **population-level incentive gradient**: as a
market's own valuation level rises, the population of issuers who find it attractive to sell
paper grows, and the population of investors willing to overpay for access to that paper also
grows — two populations whose joint behavior is measurable in aggregate (issuance share,
average pop, median subscription) even though no single issuer's or investor's decision is
individually forecastable. This population-level framing is also why the seat's honest
counter-literature (Schultz 2003, Butler-Grullon-Weston, §A.2.5) targets exactly the right
thing: not whether issuers *want* to time the market (nobody disputes that), but whether the
*ex-post statistical pattern* researchers observe is fully explained by that incentive alone, or
partly manufactured by how event-time returns get measured around a variable (issuance volume)
that is itself endogenous to past returns. Both readings can be true at once, and §A.2.6 takes
the honest position that they are.

### A.2 The evidence, at depth

#### A.2.1 Baker & Wurgler (2000) — the aggregate-market-timing result

**(i) Mechanism.** **Baker, Malcolm & Wurgler, Jeffrey (2000), "The Equity Share in New Issues
and Aggregate Stock Returns,"** *Journal of Finance* 55(5): 2219–2257, is the seat's founding
citation and the one the Atlas quotes by name. The construct is deliberately simple: define the
"equity share in new issues" as gross equity issuance divided by the sum of gross equity and
gross long-term debt issuance, economy-wide, for each year 1928–1997. If firms possess private
information about their own overvaluation (the Myers-Majluf-style adverse-selection logic
underlying nearly all corporate-finance issuance theory) and act on it in aggregate, then years
in which the equity share is unusually high should be years in which the *aggregate* market was,
in retrospect, overpriced — and should therefore be followed by lower market returns.

**(ii) Formal structure and magnitude.** The paper sorts years by the equity share's own
historical quartile and reports the subsequent year's equal-weighted market return conditional
on that quartile: when the equity share sits in its **bottom** historical quartile, the
following year's equal-weighted market return averages roughly **+27%**; when it sits in the
**top** quartile, the following year averages roughly **−8%** **[Verified]**. The predictive
relationship is stable across both halves of the 1928–1997 sample and survives controlling for
other known return predictors the paper tests it against. Baker & Wurgler's own interpretation
is pointed: they do not find the pattern consistent with a risk-based, efficient-markets
reading, because the equity share's predictive power runs in a direction (predicting
significantly *negative* subsequent returns) that a compensated-risk story struggles to
generate — issuers are not being paid a risk premium for issuing into a boom, they are, on this
reading, successfully selling into overvaluation.

**(iii) For our seat.** This is the direct ancestor of the VOLUME leg (§A.1.ii, §A.4): the
Indian construction (issuance value / market cap, expanding percentile, `partCDEFH.md` Part D)
is a India-data, India-cadence descendant of exactly this aggregate-share logic, adapted from an
annual US frequency to a monthly-aggregated Indian one and from a raw quartile sort to an
expanding-percentile rank (this program's standard no-look-ahead construction, consistent with
its refusal of the HP filter and fixed in-sample thresholds, CONTRACT §6/§8). The magnitude
itself (27% vs −8%) is **not** carried forward as an India parameter — it is 1928–1997 US
data, a different market structure, and a different measurement horizon (annual, not the
ladder's 12–24-month τ½ band) — but the *sign and shape* of the relationship (low issuance
share precedes strong returns; high issuance share precedes weak ones) is exactly what the
seat's regime-score direction (`role: sentiment state`) is built to encode.

**(iv) Citations.** Baker, Malcolm & Wurgler, Jeffrey (2000), "The Equity Share in New Issues
and Aggregate Stock Returns," *Journal of Finance* 55(5): 2219–2257 **[Verified — Wiley Online
Library DOI 10.1111/0022-1082.00285; also NYU Stern working-paper archive]**.

#### A.2.2 Baker & Wurgler (2006) — the sentiment index and cross-sectional conditioning

**(i) Mechanism.** **Baker, Malcolm & Wurgler, Jeffrey (2006), "Investor Sentiment and the
Cross-Section of Stock Returns,"** *Journal of Finance* 61(4): 1645–1680, generalizes the 2000
paper's single-variable logic into a composite index and shifts the question from "does
issuance predict the *aggregate* market" to "does sentiment predict the *cross-section* —
which stocks does it move most." The mechanism: sentiment (however measured) should move
easy-to-arbitrage, easy-to-value stocks the least, and hard-to-arbitrage, hard-to-value stocks
the most, because the second group is precisely where limits to arbitrage (short-sale
constraints, valuation uncertainty, thin analyst coverage) let sentiment-driven mispricing
persist longest before being corrected.

**(ii) Formal structure.** The composite sentiment index is built as the **first principal
component of six proxies**: the closed-end fund discount, NYSE share turnover, the number of
IPOs in a given period, the average first-day return on IPOs, the equity share in new issues
(the 2000 paper's own variable, now one input among six), and the dividend premium (the
log difference in average market-to-book between dividend payers and non-payers) **[Verified —
six-component construction corroborated across multiple independent secondary sources this
session; the paper's own precise relative-lag treatment across the six components — reported
in some secondary summaries as three components entered contemporaneously and three lagged one
year — is stated here only in outline: [VERIFY: exact lag specification against the primary
text, which this session's network access could not reach directly]]**. The paper's headline
finding: when beginning-of-period sentiment is **low**, subsequent returns are relatively
**high** for small, young, high-volatility, unprofitable, non-dividend-paying, extreme-growth
and distressed stocks — precisely the "hard to value, hard to arbitrage" category the mechanism
predicts — and when sentiment is **high**, the same category of stock earns relatively **low**
subsequent returns, while large, established, profitable, dividend-paying stocks show little to
no sentiment-conditional pattern either way.

**(iii) For our seat.** Two consequences follow directly. First, this paper is the direct
license for treating **IPO count and first-day return** as first-class sentiment inputs in
their own right, not merely as a curiosity alongside the aggregate equity-share variable — it
is the paper that elevates the RECEPTION face (§A.1.ii) to co-equal standing with the VOLUME
face, exactly the two-leg design this ladder's construct inherits. Second, the cross-sectional
finding (sentiment moves small/young/distressed names most) is the theoretical bridge to why
this seat's froth reading is specifically relevant to the **special-sits sleeve** (aggressive
book only, Decision Q10) rather than the broad factor book: special situations and recently
listed names are, definitionally, drawn from exactly the population — young, newly listed,
often unprofitable, hard to value against a track record — this paper identifies as most
sentiment-exposed, which is the direct theoretical grounding (beyond simple prudence) for the
ladder's "froth => shrink" sizing rule rather than a broader factor-book rule.

**(iv) Citations.** Baker, Malcolm & Wurgler, Jeffrey (2006), "Investor Sentiment and the
Cross-Section of Stock Returns," *Journal of Finance* 61(4): 1645–1680 **[Verified — Wiley
Online Library DOI 10.1111/j.1540-6261.2006.00885.x; NBER Working Paper 10449]**.

#### A.2.3 Loughran & Ritter (1995) and the issuer-cohort record — the other side of the same coin

**(i) Mechanism.** Where §A.2.1–A.2.2 read the aggregate market and the cross-section from the
*investor's* side, **Loughran, Tim & Ritter, Jay R. (1995), "The New Issues Puzzle,"** *Journal
of Finance* 50(1): 23–51, reads the same incentive from the **issuer-cohort** side: track the
long-run return of the specific firms that chose to issue, rather than the market they issued
into. If issuers time issuance to periods when their own stock (or the market broadly) is
overvalued, the cohort of firms that actually issued in a given period should, on average,
underperform otherwise-similar non-issuing firms over the years that follow — a direct,
firm-level test of the same incentive §A.2.1 tests at the aggregate-market level.

**(ii) Formal structure and magnitude.** Tracking US firms that conducted an IPO or a seasoned
equity offering (SEO) between 1970 and 1990, the paper finds both cohorts were, on average,
poor long-run investments: over the **five years** following issuance, IPO firms returned only
about **5% per year** and SEO firms about **7% per year**, against non-issuing, size-matched
comparables. The paper's own headline magnitude for the wealth effect: an investor would have
needed to invest roughly **44% more capital** in the issuing firms than in equivalent
non-issuing firms to arrive at the same terminal wealth five years later **[Verified]**. Book-
to-market differences between issuers and non-issuers explain only a modest share of this gap —
the underperformance is not simply "issuers happen to be growth stocks and growth stocks
underperformed value in this sample."

**(iii) Ritter's maintained, updated record.** Jay Ritter has maintained and periodically
updated this exact dataset for three decades; the most recent update available (data through
December 2025, an extended sample of 9,343 US operating-company IPOs, 1980–2024) finds
five-year, size-and-book-to-market-matched equal-weighted underperformance of roughly **2.1%
per year** — materially smaller than the original 1995 paper's magnitude, and itself direct,
first-party evidence of exactly the decay this seat must confront honestly (§A.2.6)
**[VERIFY: precise updated magnitude and sample construction — sourced from a secondary
aggregator summarizing Ritter's own site rather than the primary spreadsheet, which this
session's network access could not reach directly; Ritter's own data page,
site.warrington.ufl.edu/ritter/ipo-data, is the authoritative primary source for the data-phase
team to pull directly]**. Two refinements from Ritter's ongoing work matter for this seat's own
design. First, the underperformance is **not uniform across the issuer population**: it
concentrates in smaller, less profitable, growth-oriented offerings, and in issues from
high-volume "hot" issuance years specifically — directly consistent with the "windows of
opportunity" mechanism (§A.2.4) and with this seat's own VOLUME-leg logic (the froth reading is
a statement about *hot* years, not issuance in general). Second, large IPOs of established,
profitable firms (trailing sales above roughly $1 billion) show **much smaller, often
statistically insignificant** underperformance — a genuine heterogeneity this seat's own India
construction should expect to find echoed (mainboard vs. SME, §A.3.1, is plausibly this exact
distinction wearing Indian institutional clothing) — and a companion finding on "broken IPOs"
(issues trading materially below their offer price): among a tracked set of 654 such issues,
roughly **68%** produced negative three-year buy-and-hold returns from the offer price
**[VERIFY: precise cohort definition and percentage — secondary-sourced this session]**.

**(iv) Citations.** Loughran, Tim & Ritter, Jay R. (1995), "The New Issues Puzzle," *Journal of
Finance* 50(1): 23–51 **[Verified — Wiley Online Library DOI 10.1111/j.1540-6261.1995.tb05166.x;
also hosted at site.warrington.ufl.edu/ritter]**. Ritter, Jay R., maintained IPO
long-run-performance dataset, updated periodically, site.warrington.ufl.edu/ritter/ipo-data
**[Verified as an existing, actively maintained dataset; specific updated figures above
carry the [VERIFY] tags stated]**. Ibbotson, Roger G. & Jaffe, Jeffrey F. (1975), "'Hot Issue'
Markets," *Journal of Finance* 30(4): 1027–1042 **[Verified — the earliest documented statement
of the hot-issue-market pattern, already D08's own F11 citation]**.

#### A.2.4 Windows of opportunity — why issuance clusters, formalized

**(i) Mechanism.** The "windows of opportunity" literature supplies the theoretical bridge
between §A.2.1's aggregate-return result and §A.2.3's issuer-cohort result: it explains *why*
issuance should cluster in time at all, rather than arriving as a steady trickle. **Lucas,
Deborah J. & McDonald, Robert L. (1990), "Equity Issues and Stock Price Dynamics,"** *Journal of
Finance* 45(4): 1019–1043, extends Myers & Majluf's (1984) static adverse-selection framework
(managers with private information cannot cheaply issue debt, so equity issuance signals
unfavorable private information) into a **dynamic** setting: a manager who believes the firm's
stock is temporarily undervalued **delays** issuance until the price recovers, rather than
issuing at the depressed price and accepting the signaling discount immediately. Because stock
prices are correlated across firms (a market-wide rally lifts most stocks together), this
delay-until-recovery behavior generates **issuance clustering around market peaks** purely from
individually rational, privately-informed managers reacting to a common market signal — no
coordination or manipulation required.

**(ii) Formal structure and the demand-side complement.** **Choe, Hyuk; Masulis, Ronald W. &
Nanda, Vikram (1993), "Common Stock Offerings across the Business Cycle: Theory and Evidence,"**
*Journal of Empirical Finance* 1(1): 3–31, adds the demand-side half of the mechanism:
adverse-selection costs (the discount a firm must accept to issue when investors cannot
distinguish good firms from bad) are **lower in good economic conditions**, when investors can
more cheaply verify firm quality and are more receptive to new equity generally — so both the
issuer's willingness to supply and the investor's willingness to absorb rise together in good
times, reinforcing rather than offsetting each other. **Bayless, Mark & Chaplinsky, Susan
(1996), "Is There a Window of Opportunity for Seasoned Equity Issuance?,"** *Journal of Finance*
51(1): 253–278, supplies the direct SEO-timing test this composite theory predicts: "hot" SEO
markets (periods of unusually heavy issuance volume) are associated with systematically lower
issuance costs and, consistent with §A.2.3, weaker post-issue returns for the firms that issue
during them — the empirical signature of a genuine window, not a random clustering artifact.

**(iii) For our seat.** This is the theoretical justification for reading VOLUME as a genuinely
informative state rather than mere noise in issuance timing: if issuance clustering were purely
random (firms need capital on their own idiosyncratic schedule, unrelated to market pricing),
the aggregate-share result (§A.2.1) would have no mechanism to hang on. Windows-of-opportunity
theory supplies exactly that mechanism, and does so in a form — a **capacity-and-information**
argument (issuers cannot manufacture reasons to avoid the same market-wide receptivity that
makes issuance cheap right now) — that reinforces rather than substitutes for §A.1's incentive
argument: managers are not merely *able* to time issuance opportunistically, the theory predicts
they will do so **in aggregate and in clusters**, which is precisely the "hot issuance year"
object this ladder's VOLUME leg is built to detect.

**(iv) Citations.** Myers, Stewart C. & Majluf, Nicholas S. (1984), "Corporate Financing and
Investment Decisions When Firms Have Information That Investors Do Not Have," *Journal of
Financial Economics* 13(2): 187–221 **[Verified — foundational, pre-dates the windows-of-
opportunity extension]**. Lucas, Deborah J. & McDonald, Robert L. (1990), "Equity Issues and
Stock Price Dynamics," *Journal of Finance* 45(4): 1019–1043 **[Verified]**. Choe, Hyuk;
Masulis, Ronald W. & Nanda, Vikram (1993), "Common Stock Offerings across the Business Cycle:
Theory and Evidence," *Journal of Empirical Finance* 1(1): 3–31 **[Verified]**. Bayless, Mark &
Chaplinsky, Susan (1996), "Is There a Window of Opportunity for Seasoned Equity Issuance?,"
*Journal of Finance* 51(1): 253–278 **[Verified]**.

#### A.2.5 The honest counters — pseudo-market-timing and the limits of managerial foresight

**(i) Mechanism — Schultz's pseudo-market-timing critique.** **Schultz, Paul H. (2003),
"Pseudo Market Timing and the Long-Run Underperformance of IPOs,"** *Journal of Finance* 58(2):
483–517, is the sharpest, most direct challenge to reading §A.2.1–A.2.3's results as evidence
of genuine managerial foresight, and this seat's own design register (`partCDEFH.md` Part D)
already names it as "the honest counter carried alongside the Tier-B confidence." Schultz's
insight is subtle and, once seen, hard to unsee: **more firms choose to issue when stock prices
are high** — not because they can forecast that prices will subsequently fall, but simply
because a high price is, mechanically, an attractive time to raise capital on favorable terms,
full stop, with zero forecasting ability required. If issuance volume is genuinely higher in
some periods than others (which it demonstrably is — §A.2.4's clustering), and if the market's
*ex-post* average return across all periods is positive (which it generally is), then **even in
a perfectly efficient market where no one can predict anything**, a value-weighted or
event-time average of "returns following high-issuance periods" will mechanically look worse
than "returns following low-issuance periods" — an artifact of aggregation, not evidence of
timing skill.

**(ii) Formal structure and the simulation result.** Schultz's simulations, calibrated on
1973–1997 US issuance patterns, show that when the *true* expected abnormal return to issuing is
set to **exactly zero** by construction, the **event-time** (calendar-time-pooled-by-event)
measurement convention nonetheless produces a statistically significant *negative* median
abnormal return for issuers — pure pseudo-market-timing, manufactured by the measurement
convention itself. Switching to a **calendar-time** portfolio approach (which does not
over-weight high-issuance periods the way naive event-time pooling does) resolves the artifact.
**Viswanathan, S. & Wei, Bin (2005)** and **Dahlquist, Magnus & de Jong, Frank (2004)** provide
an important qualification the seat's own design should carry forward honestly: if the *number*
of IPOs per period is itself statistically stationary (not persistently trending), the
pseudo-market-timing bias Schultz identifies is a **small-sample artifact**, not a permanent
feature of the true data-generating process — meaning the size of the artifact is itself an
empirical question about issuance-count stationarity, not a fixed discount to apply universally.
**Butler, Alexander W.; Grullon, Gustavo & Weston, James P.** extend the same skepticism
directly to the equity-share-in-new-issues literature itself, arguing that a material share of
the predictive power researchers attribute to genuine managerial market-timing ability is better
explained by this same pseudo-market-timing measurement effect than by managers possessing
actual forecasting skill about the systematic (market-wide) component of future returns
**[VERIFY: exact title, venue, and year of the Butler-Grullon-Weston critique specifically
targeting the equity-share result — this session's search corroborated the finding's substance
and the authors' broader research program (their verified, closely related *Journal of Finance*
papers on debt-maturity and aggregate-market-forecast timing are cited below) but did not surface
a single, precisely-titled primary source for this specific claim; treat the finding as
directionally corroborated, not pinned to one verified citation]**.

**(iii) For our seat.** This is not a reason to demote the seat's Tier-B status or abandon the
construct — it is the reason the seat's decay treatment (§A.2.6) applies a stated, generic
haircut to the *statistical magnitude* researchers report, while leaving §A.1's incentive
argument for the construct's *existence* untouched. The two critiques operate on genuinely
different objects: Schultz's pseudo-market-timing concern is a **measurement-convention**
critique (does the reported effect size overstate the true one, given how event studies are
conventionally built), which this program's own no-look-ahead, expanding-percentile, purged-CV
discipline (CONTRACT §9; `partCDEFH.md` Part D) is specifically designed to avoid falling prey
to in its own India construction — a calendar-time, monthly-aggregated state (never an
event-time-pooled cohort average) sidesteps the exact artifact Schultz identifies. Butler-
Grullon-Weston's critique, if its precise claim is as strong as its substance suggests, would
attack something closer to §A.2.1's own aggregate-return magnitude directly — which is exactly
why this seat, per §A.2.1.iii, never carries the 2000 paper's 27%/−8% magnitude forward as an
India parameter, only its sign and shape, with the India-specific magnitude left entirely to the
data phase's own pre-registered test (§A.4, IS1 per `partCDEFH.md` Part F).

**(iv) Citations.** Schultz, Paul H. (2003), "Pseudo Market Timing and the Long-Run
Underperformance of IPOs," *Journal of Finance* 58(2): 483–517 **[Verified — Wiley Online
Library DOI 10.1111/1540-6261.00535]**. Viswanathan, S. & Wei, Bin (2005) and Dahlquist, Magnus
& de Jong, Frank (2004), on the small-sample-stationarity qualification to pseudo-market-timing
**[Verified as existing responses to Schultz (2003), cited across secondary literature reviews;
exact venues [VERIFY]]**. Butler, Alexander W.; Grullon, Gustavo & Weston, James P., critique of
managerial market-timing evidence in the equity-share literature **[VERIFY: precise citation, per
(ii) above; the authors' closely related, independently verified work — Butler, Grullon & Weston
(2005), "Stock Market Liquidity and the Cost of Issuing Equity," *Journal of Financial and
Quantitative Analysis* 40(2): 331–348 **[Verified]**, and their broader *Journal of Finance*
program on managerial forecasting ability — corroborates the authors' standing to make this
argument even where the specific title is unpinned]**.

#### A.2.6 The decay question, examined per component

**(i) Why this seat needs its own decay table, not one number.** CONTRACT §5 requires a
decay-survival argument in writing; §5's governing principle (McLean & Pontiff 2016: anomalies
decay ~26% out-of-sample, ~58% post-publication) is this program's generic prior for signals
whose survival rests on an information gap. This seat's own honest position, established in
§A.1 and defended through §A.2.1–A.2.5, is that its **components decay at different rates for
different reasons**, and collapsing them into one number would hide exactly the distinction
this seat's whole design (the two-leg VOLUME/RECEPTION split, `partCDEFH.md` Part D) exists to
preserve.

**(ii) The component-by-component read.**

| Component | What decays | What does not decay | Verdict |
|---|---|---|---|
| The issuer's timing incentive (§A.1) | Nothing — no arbitrage mechanism exists against a promoter's own decision not to float | The incentive itself, structurally, forever | No decay haircut applies to the mechanism's existence |
| Baker-Wurgler equity-share magnitude (§A.2.1) | The *precise* predictive R² and quartile-spread magnitude, as crowded capital and post-publication awareness compress the tradable edge; Ritter's own updated 5-year IPO-underperformance figure (§A.2.3.iii) shrinking from ~5%/yr shortfall in the original sample to a materially smaller updated estimate is first-party evidence of exactly this compression | The *sign and shape* — hot issuance still precedes weaker returns in every updated dataset checked | Generic McLean-Pontiff band (26–58%) applied to the **magnitude only**, per the ladder's own decay field |
| Reported statistical significance of the aggregate-return result (§A.2.5) | Some share is a Schultz-style measurement artifact rather than a real, tradable edge — the exact share is an open, empirically-contingent question (stationarity of issuance counts) | The underlying incentive (§A.1), which the artifact critique never targets | Additional discount for measurement-convention risk, mitigated (not eliminated) by this seat's own calendar-time, no-look-ahead construction |
| The RECEPTION leg's cross-sectional conditioning (§A.2.2) | Untested for whether India's own hard-to-arbitrage population (thin float, retail-dominated books, §A.3) behaves identically to the 1962–2001 US sample Baker-Wurgler test | Nothing established yet either way — an open India question, not a decay claim | Carried as an unverified cross-country prior (Tier B via methodology, Tier C via India coefficient), exactly the ladder's own confidence field |
| SEBI's own regulatory confirmation (§A.3.3) | Nothing — a regulator acting on froth is itself a fresh, dated observation each time it recurs, not a decaying academic result | The pattern of regulatory response recurring across cycles (2007, 2012, 2024, §A.3.3) | Treated as a fresh confirming data point at each recurrence, never a stale one |

**(iii) For our seat.** The net position, matching the ladder's own `decay: "MP 26-58% band
placeholder"` field precisely: this program applies the *generic* McLean-Pontiff band as a
conservative **placeholder** — not because the underlying mechanism is expected to decay like a
typical information-gap anomaly (§A.1 argues the opposite), but because the specific *magnitude*
any India-conditioned regression will recover has not yet been estimated, and a stated,
literature-typical haircut is the honest default until the pre-registered India test (`changes_if:
"India pre-registered test vs 2018/2023-24 episodes"`; IS1/IS2 per `partCDEFH.md` Part F) replaces
the placeholder with an evidence-based number. This is the single sentence this Part's title
promises to unpack: the seat is Tier B, carries a real haircut on its *statistical* estimate, and
is nonetheless the rare entry on this ladder the desk does **not** expect to fully decay, because
the thing decaying (a measured magnitude) and the thing this seat is actually built on (a
structural incentive) are different objects.

### A.3 India's machinery

This section describes the institutional plumbing the Indian issuance/sentiment cycle actually
runs on — not a backtested case record (deferred to the sibling `partB-cases.md`), but the
mechanics any India-conditioned test of §A.2's theory must be built against, and the reason
SEBI's own regulatory history functions as a free, real-time confirming layer this program
would be foolish not to use.

#### A.3.1 The issuance stack

India's primary-market issuance runs through several structurally distinct channels, and this
seat's own construction (`partCDEFH.md` Part C) keeps them as separate series precisely because
their microstructure differs; the era-by-era magnitudes each channel has carried are the sibling
cases chapter's own territory (`partB-cases.md`), cited here only where the mechanism itself is
the point. **Mainboard IPOs** — the NSE/BSE main-board listing process under SEBI's ICDR
framework — are the channel inside this program's tradeable universe (NIFTY 750). **SME
boards** — NSE Emerge (launched 2012) and BSE SME (launched 2012) — run under a deliberately
lighter-touch ICDR regime (smaller minimum lot sizes but a high per-lot rupee value, historically
~₹1–2 lakh minimum application, structurally restricting the investor base toward HNI/wealthy-
retail rather than mass retail) and are the home of the 2023–25 frenzy this Atlas names directly
(magnitudes: `partB-cases.md` case 7). Per D12's own F5 finding (already this program's binding
rule, not re-litigated here): **SME-platform issues are excluded from every book's tradeable
universe entirely** — thin float, high manipulation risk, and a liquidity profile incompatible
with proprietary-book-sized positions — which is precisely why this seat's own construction
(`partCDEFH.md` Part C, Part E Step 1) treats mainboard and SME as **separate series**, with the
SME series entering only as a satellite briefing line and an extreme-froth confirming signal,
never as a tradeable input or a component of the core state.

Beyond IPOs, three further channels feed the VOLUME leg. **QIPs** (Qualified Institutional
Placements) — a fast, institutions-only capital-raise mechanism restricted to sale into
institutional books, with no retail tranche and no listing-day pop to speak of — contribute
volume without a RECEPTION reading of their own kind. **OFS** (Offer for Sale through the
stock-exchange mechanism, introduced by SEBI on 1 February 2012) lets promoters and large
non-promoter shareholders sell existing shares directly on-exchange in a single trading day,
settled within two working days, originally built to help meet minimum public-shareholding norms
and increasingly used as a pure liquidity/exit channel (§A.3.4). **Rights issues** remain the
smallest, most muted channel by comparison, largely used for capital-structure repair rather than
opportunistic timing, and are not a first-order input to this seat's construction. **InvITs and
REITs** — SEBI-created listed-trust structures for infrastructure and real-estate assets
respectively — are a newer, fast-growing vehicle class, and a genuinely new supply channel
`partCDEFH.md` Part E's own "category audit" exists specifically to catch, since a future
issuance wave arriving predominantly through InvIT/REIT paper rather than classic equity would
otherwise slip past a construction built on the older channel taxonomy.

#### A.3.2 The RECEPTION instruments — a free variable most markets lack

India's book-building process publishes, for every mainboard issue, live and final subscription
data split by investor category — **QIB** (Qualified Institutional Buyers: mutual funds,
insurers, banks, FPIs, typically allotted **75%** of a mainboard issue's shares, proportionately),
**NII/HNI** (Non-Institutional Investors, applications above ₹2 lakh, since 2021 split into
sNII — ₹2–10 lakh, 5% reservation — and bNII — above ₹10 lakh, 10% reservation — both
proportionate), and **retail** (applications up to ₹2 lakh, **35%** reservation, allotted by
computerized lottery once the category is oversubscribed beyond 1x) **[Verified — reservation
percentages and category structure corroborated across multiple independent secondary sources]**.
NSE and BSE publish updated subscription multiples through the bidding window and final figures
at close — a genuinely free, per-issue, per-category RECEPTION variable most global markets do
not publish with comparable granularity, and exactly the free-data instrument this program's
CONTRACT §1 free-source mandate can build the RECEPTION leg from without any paid feed. A slice
of the QIB book is typically pre-committed the day before the issue opens through **anchor
investors**, whose allocation and subsequent (staggered, post-2022-rule) lock-in behavior is
itself a further, free, dated data point. Alongside the exchange-published subscription data,
India runs an unofficial, unregulated **grey market**: shares (or, more precisely, entire
un-allotted applications) trade informally before listing, at a premium or discount to the
issue price — the **Grey Market Premium (GMP)** — through two structures: **kostak** (a fixed
price paid for an entire application before allotment is known, transferring the allotment
lottery's own risk to the buyer) and **"subject to sauda"** (a deal contingent on the seller
actually receiving an allotment, cancelled if none is allotted). GMP is neither regulated nor
recognized by SEBI, NSE, or BSE, is not computed by any formula, and reflects pure informal
buyer/seller demand — but it is nonetheless a widely tracked, directionally informative,
continuously observed sentiment thermometer this program treats as **unofficial-but-observed**
context (per the Atlas's own phrasing), never as a formal state input given its unregulated,
unverifiable, manipulation-exposed nature. First-day listing pops themselves — issue price
against first-trade or first-close price — are fully computable from free bhavcopy data with no
grey-market dependence at all, and are the seat's actual, auditable RECEPTION input;
India-specific academic estimates of average IPO underpricing have historically run high by
international standards — Madhusoodanan & Thiripalraju (1997) find underpricing above
international norms in an early-1990s BSE sample, Shah (1995) finds average short-run returns of
roughly **106%** across 2,056 new listings January 1991–May 1995, and later work (Banerjee &
Bhat 2011; Madhusoodanan & Thiripalraju 2009) reports average underpricing commonly cited in the
**20–40%** range with long-run underperformance against NIFTY/SENSEX benchmarks consistent with
§A.2.3's global pattern **[Verified in outline; precise per-study magnitudes and sample windows
VERIFY against primary sources for the data phase]**.

#### A.3.3 SEBI's regime as the institutional thermometer

This program treats a regulator's own action as a free, dated, high-signal confirming layer —
"a regulator acting IS a froth reading," per `partCDEFH.md` Part E — and India's primary-market
regulatory history across three widely spaced episodes supports exactly that reading, each a
different instrument aimed at the same underlying excess. **2007**: SEBI's participatory-note
curbs, arriving in the teeth of the pre-GFC primary-market boom, and a **mandatory IPO-grading
regime (May 2007–February 2014)** requiring credit-rating agencies to score issues 1–5 on
fundamentals — later made optional once a 2013 SEBI-commissioned review found the mandatory
grade was not, in practice, serving its purpose **[Verified]**, itself a data point on how hard
an institutionally-mandated quality signal is to make stick against a determined issuance wave.
**2012**: the Primary Market Advisory Committee's discussion paper on a mandatory safety-net
mechanism — a proposed issuer/banker buy-back obligation toward small investors when a listing's
price fell materially below issue price, explicitly framed around "self-discipline in IPO
pricing" **[VERIFY: final adoption status — this session confirmed the discussion paper's
existence and framing but not whether it was subsequently mandated, watered down, or left
voluntary]**. **2024** is the Atlas's own named "institutional confirmation": SEBI's Chairperson
stated publicly that the regulator saw signs of manipulation in the SME segment, and the board's
December 2024 ICDR amendments tightened SME eligibility and fund-use norms directly in response
— the full rule set, and the oversubscription/pop record it responded to, is `partB-cases.md`
case 7's own territory, not re-derived here. Three widely spaced episodes, three different
regulatory instruments, one consistent posture: **the regulator moves against issuance/reception
excess precisely when this seat's own two legs would independently be flagging it** — a free,
institutional confirming layer this program's construction (`partCDEFH.md` Part C: "SEBI
actions... event registry entries") is built to log and annotate the state with, never to
substitute for the state itself.

#### A.3.4 Promoter and PE exit waves — OFS as smart-money selling, read honestly

The OFS mechanism (§A.3.1) has, across recent mainboard cycles, run predominantly as an exit
channel rather than a capital-formation one — a growing share of total mainboard proceeds
consistently OFS (existing holders cashing out) rather than fresh capital reaching the
businesses themselves, with promoter and private-equity block/bulk selling recurring at record
scale for consecutive years (the specific year-by-year totals are `partB-cases.md` case 7's own
territory). This is a direct, observable instance of §A.1's central claim in its purest form: a
promoter or PE sponsor selling into an OFS is, definitionally, an insider choosing to convert a
large personal stake into cash at the prevailing market price — the cleanest possible
revealed-preference signal available anywhere in this program's data set (elaborated fully in
Part G's psychology, §G.3). This program's own design register already flags OFS/promoter-
selling volume as a **candidate third leg** for this seat's state (`IS-D3` per `partCDEFH.md`
Part F: "promoter/PE OFS selling as a third leg candidate — design only, classification work
first") — not yet admitted to the construct, because classifying OFS volume cleanly
(distinguishing routine minimum-public-shareholding compliance sales from genuinely
opportunistic, valuation-timed exits) is unresolved work, but flagged here as the most promising
near-term enrichment to the two-leg state, and the reason this Part's own psychology section
(§G.3) treats promoter timing as a signal the desk should read carefully rather than dismiss as
"just an insider cashing out."

#### A.3.5 The special-sits sleeve linkage

Everything in §A.3.1–A.3.4 ultimately routes to one of two consumption points, and this section
closes the loop the ladder's own role field opens. The **mainboard** VOLUME and RECEPTION legs
feed the `valuation_sentiment` regime-score block (§A.4) as this seat's primary output. The
**special-situations sleeve** (aggressive book only, Decision Q10, capped Tier-B satellite,
frozen event rules per CONTRACT §10) draws directly on the same froth reading for its sizing
rule: per the ladder's own role line, "froth => shrink" — a name freshly listed into a hot
issuance/reception environment gets a **smaller** special-sits allocation than the same name
would receive in a cold issuance environment, never the reverse, and never a standalone timing
call to avoid the sleeve entirely (the sleeve's own frozen rules govern eligibility; this seat
only conditions size within them). The **SME satellite line** (§A.3.1) feeds neither path
directly — it is excluded from the universe by construction (D12 F5) — but functions as an
early-warning, extreme-froth confirming signal for Stage-2 briefings and as the specific object
Part G's own operator-trap (§G.5) warns against mistaking for a tradeable read.

### A.4 The state design

**(i) The construct.** Per `partCDEFH.md` Part D, the state is an availability-weighted mean of
two expanding percentiles: `pct(issuance_value / market_cap)` (the VOLUME leg) and
`pct(median_first_day_pop)` (the RECEPTION leg), with subscription-ratio medians carried as a
corroborating input to the RECEPTION leg rather than a third independent percentile (§A.3.2's
QIB/HNI/retail granularity is retained for Stage-2 briefing detail, not folded separately into
the state, to avoid triple-counting one underlying phenomenon). When no issue listed in a given
month, the construction degrades gracefully to the VOLUME leg alone (already tested per
`partCDEFH.md` Part C) rather than either stalling or manufacturing a false reading from stale
RECEPTION data.

**(ii) Why both legs, argued from first principles.** §A.1.ii already names the two faces;
here is why the froth signature this ladder cares about requires **both** elevated together,
not either alone. **Volume without pops** is healthy capital formation: an economy genuinely
absorbing more primary capital at ordinary, sensible valuations, with new issues clearing near
their offer price because investors are pricing them correctly rather than chasing them — a
state this program should read as regime-neutral-to-positive, not as sentiment excess, and a
state the VOLUME-only leg would, on its own, mistakenly flag as elevated. **Pops without
volume** is a scarcity premium: a small number of well-regarded, perhaps deliberately
under-priced issues generating strong first-day demand precisely because supply is thin relative
to investor appetite — again not the sentiment-excess signature this seat exists to catch, since
scarcity-driven pops can coexist with, and indeed partly result from, issuers being
*conservative* about how much paper they bring to market. **Both legs high together** — heavy
issuance volume *and* strong reception — is the genuine froth signature: issuers bringing
unusually large volumes of paper to market specifically because investors are unusually willing
to overpay for it, the exact joint condition §A.2.2's cross-sectional mechanism and §A.2.4's
windows-of-opportunity theory both predict should arrive together rather than independently.
This is also precisely why the seat carries **no short-signal path** (`partCDEFH.md` Part D,
Part E Step 3, stated explicitly): a reading of "both legs elevated" licenses reduce-only
sizing responses (regime-score contribution moving negative within the shared block budget;
special-sits sleeve shrinking), never a directional short thesis on any individual name or the
issuance-linked segment as a whole — consistent with the mandate's hedge-only short-side
constraint (CONTRACT §10) and with there being no clean, liquid way to short a hot primary-market
segment at this program's scale in the first place.

**(iii) τ½ and consumption.** The ladder's τ½ prior of 12–24 months places this seat meaningfully
faster than the value-spread block-mate L8 (τ½ 24–36 months, `docs/cycles/04-value-quality.md`
A.4) — sentiment waves in issuance and reception genuinely turn faster than a value composite's
own cross-sectional cheapness dispersion, consistent with issuance/reception being closer to a
Band-3 "intra-cycle state" (`docs/CYCLE_ATLAS.md` §4) than L8's own multi-year value-winter
dynamics (`docs/cycles/04-value-quality.md` A.9). Consumption runs through exactly one shared
budget with two conditioning uses. Inside the **`valuation_sentiment` block** (0.10 of regime
score, shared with L8, non-clamped: `reduce_only: false`), L7 and L8 together supply the
"double-confirm" this program's design already names: a market that is simultaneously
**expensive** (L8's spread reading) **and** issuing/receiving hot paper (L7's two-leg reading) is
a stronger regime-score signal than either alone, exactly mirroring the general design principle
this ladder applies elsewhere (Greenwood-Hanson-Shleifer-Sørensen's "R-zone," already cited in
the credit and financial-cycle monographs, where credit growth *and* asset-price growth jointly
predict crisis risk far better than either alone) — the same joint-confirmation logic, applied
here to valuation and issuance sentiment rather than credit and property. The **special-sits
sleeve sizing rule** (§A.3.5) draws on L7 alone, independently of L8, since the sleeve's own
population (recently listed, special-situation names) is precisely where §A.2.2's RECEPTION-leg
mechanism (sentiment moves hard-to-value names most) bites hardest.

**(iv) The data-gated India test.** The ladder's own `changes_if` field is explicit and binding:
"India pre-registered test vs 2018/2023-24 episodes." The **2018** episode is India's own
closest analogue to a clean natural experiment for this seat: a historically strong 2017 IPO
year riding a broader mid-and-smallcap rally, followed by a sharp 2018 reversal in which a
majority of the year's listings traded below issue price against a mid/smallcap complex falling
double digits from its own January 2018 peak (the full record: `partB-cases.md` case 5) — a
textbook hot-issuance-then-reversion sequence this seat's own two-leg construction should, if
the mechanism transfers to India as theorized, have flagged in advance via elevated VOLUME and
RECEPTION readings through 2017. The **2023–24** episode is the SME-frenzy-plus-mainboard-revival
case already documented throughout §A.3 and in full in `partB-cases.md` case 7, with the added
benefit of a dated, named regulatory confirmation (§A.3.3) arriving inside the test window
itself. Per this program's estimation standards (CONTRACT §9), this test must be
**pre-registered** before being run — hypothesis, threshold construction, and the specific
frozen episode dates fixed in advance — and is designated `IS1` (the core Baker-Wurgler-style
India regression) and `IS2` (the 2018/2023-24 episode-shape check specifically) in
`partCDEFH.md` Part F, neither of which this Part runs or anticipates the result of.

---

## PART G — Operator psychology

Part A documents a mechanism this desk cannot arbitrage away by understanding it (§A.1) and a
two-leg state built specifically to catch the moment issuance volume and market reception rise
together (§A.4). This Part maps the psychology of the desk that has to operate a signal whose
subject matter — the euphoria of a hot IPO, the thrill of an allotment, the story that "this one
is different" — is not an abstraction any of its members needs to be told about secondhand.
Nearly everyone on a India-facing desk has, at some point, personally applied for an IPO,
refreshed a subscription-status page, or felt the pull of a grey-market premium headline; this
seat's psychology section exists precisely because that lived familiarity is a liability, not an
asset, when the same person is asked to size a regime-score input rather than place a personal
bid.

### G.1 IPO FOMO mechanics — allotment lotteries and listing-day anchoring

**Mechanism.** The retail allotment mechanism itself (§A.3.2) is a designed-in psychology
amplifier, not an incidental detail. Once retail demand crosses 1x subscription, SEBI's rule
requires a **computerized lottery**: every valid application gets exactly one entry, regardless
of how many lots were applied for, converting an already-oversubscribed issue into a pure game
of chance for the retail investor — and lottery-structured payoffs are precisely the reward
schedule behavioral finance identifies as most likely to be systematically overweighted by
individuals (the same "lottery-ticket" preference for skewed, low-probability, high-payoff
outcomes documented for retail participation in penny stocks and out-of-the-money options
applies with equal force to IPO allotment odds). Once allotted, the investor's own reference
point for "success" becomes anchored not to the issue's fundamental value but to the **listing
price itself** — a name that lists at a 40% pop and drifts sideways for a year is remembered as
a triumph, while a name that lists flat and compounds steadily for the same year is remembered
as a disappointment, regardless of which delivered the better total return; this is anchoring
in its purest, most repeatable retail-market form, and it is precisely what makes the RECEPTION
leg's median-pop measurement (§A.3.2, §A.4) a genuine behavioral signal rather than a noisy
proxy — the anchoring effect is the mechanism, not a measurement artifact riding on top of it.

**Countermeasure.** The seat's construction (§A.4) reads the **median pop across the issuance
population**, never a single name's outcome, and consumes it only as a reduce-only,
block-shared regime-score input and a satellite-sleeve sizing lever — never as a signal to chase
or avoid any individual allotment. The desk's own operator discipline: no member's personal IPO
application experience (successful, lottery-missed, or post-listing regret) is permitted to
substitute for, or override, the constructed state's own reading, exactly the same discipline
this program applies elsewhere to keep a lived, personally-felt bias from smuggling itself into
a supposedly mechanical construct.

### G.2 "This IPO is different" — the cascade, and why it recurs

**Mechanism.** Every hot-issuance episode this section has documented — 2007's pre-GFC boom,
2017's record year, 2021's COVID-era digital-consumer wave (Zomato, Nykaa, Paytm, PolicyBazaar),
2023–25's SME frenzy and mainboard revival — arrived accompanied by a genuine, evidence-adjacent
narrative explaining why *this* wave was structurally different from the last: a new consumer
category, a new digital-adoption curve, a new regulatory regime (RERA-style discipline,
already documented for the real-estate cycle's own version of this trap,
`research/cycles/fincycle-deep/partA-theory-psychology.md` G.4), a genuinely larger and younger
investor base. Some of this is even true in isolated respects — India's demat-account base
genuinely quadrupled from roughly 39.3 million in 2019 to over 185 million by end-2024
**[Verified]**, a real, structural expansion of the retail investor base, not a mirage. The
psychological trap is not that these narratives are false; it is that a **partially true**
structural-change narrative is, from inside the moment, indistinguishable from the identical
narrative that has accompanied every prior wave this program's own record (`partCDEFH.md` Part
H: "India's issuance waves top-tick markets with regularity — 1994–96, 2007–08, 2021, 2024")
already shows recurring on a multi-year rhythm regardless of which specific narrative dressed it
each time.

**Countermeasure.** The seat's two-leg state is deliberately **narrative-blind**: it reads
issuance volume and reception pops as measured percentiles, with no input channel for "but this
time the story is different," and its consumption (the shared `valuation_sentiment` block, the
special-sits sizing rule) is a pre-specified, reduce-only mapping rather than a live judgment
call about whether this cycle's narrative deserves an exception. This mirrors exactly the
countermeasure structure the value/quality monograph documents for its own "redefining the
measure at the bottom" trap (`docs/cycles/04-value-quality.md` G.2) — a genuinely-plausible,
partially-true argument for treating the current episode as structurally exceptional is
precisely the pattern a mechanical, pre-registered construct exists to be immune to.

### G.3 Promoter timing as revealed preference — the cleanest insider signal, read backwards by retail

**Mechanism.** §A.3.4 already establishes the mechanics: a promoter or PE sponsor selling through
an OFS, or a founder timing a mainboard listing's fresh-issue-vs-OFS mix, is revealing genuine
private information about their own assessment of the firm's current value through an action
that costs them real money to be wrong about (an insider who sells too early forfeits future
upside; one who sells too late has been sitting on an overvalued position) — this is, in a
literal sense, the **cleanest insider signal available anywhere in this program's data set**,
cleaner than analyst upgrades, cleaner than promoter-pledge disclosures, cleaner than almost any
other governance signal the quality sleeve tracks (`docs/cycles/04-value-quality.md` A.6.iii),
precisely because it is revealed through an irreversible, economically costly action rather than
a costless statement. Retail investors, however, structurally read this signal **backwards**:
heavy promoter/PE selling into a hot issue is, if anything, treated by much of the retail base
as *confirmation* the deal is good enough that "smart money wants in" — the exact opposite
inference from the one the OFS-as-revealed-preference mechanism actually supports, and precisely
the inference a rising GMP (§A.3.2) or an oversubscribed QIB book can reinforce, since retail
investors typically see the subscription multiple and the enthusiasm it generates before they
see, or think carefully about, who is on the selling side of the same transaction.

**Countermeasure.** This is the specific, concrete argument for `IS-D3`'s eventual promotion
(§A.3.4): OFS/promoter-selling volume, once its classification work is done, is a natural
**third leg** for this seat precisely because it reads the same population's insider behavior
the retail-facing RECEPTION leg reads backwards — a state built to be immune to exactly the
inference error this section documents. Until that classification work lands, the desk's own
discipline is narrower but still load-bearing: OFS-heavy issuance years should never be read by
the desk itself as a *bullish* confirmation of deal quality, and Stage-2 briefings (per
`partCDEFH.md` Part F) should carry the OFS share explicitly rather than let a high subscription
multiple stand alone as the episode's headline number.

### G.4 Analyst quiet-period dynamics — the underwriter-optimism cascade, formalized and informal

**Mechanism.** In the US, FINRA Rule 2241 imposes a formal **quiet period** — historically 40
days, since shortened to 10 calendar days for lead/co-managing underwriters — during which
analysts affiliated with the issue's underwriters may not publish research on the newly listed
name; the well-documented pattern once that window lapses is a **coordinated burst of favorable
initiating coverage**, with the lead-left bookrunner's analyst typically publishing first,
joint bookrunners within a day or two, and co-managers over the following week — research
coverage whose favorable tilt is a well-established finding in its own right (underwriter
analysts have an obvious conflict: continued deal flow from the same issuer and its peers).
India has no identically legislated quiet-period statute of the FINRA-2241 kind
**[VERIFY: whether any SEBI (Research Analysts) Regulations, 2014 provision imposes an
equivalent formal quiet-period restriction specifically — this session did not locate one]**,
but the same underlying **underwriter-analyst-optimism** dynamic operates informally: merchant
bankers and their affiliated research arms have every reason to initiate favorable coverage on
their own recently-listed mandates once market practice permits it, and a newly listed name's
early analyst coverage is, structurally, disproportionately sourced from exactly the banks that
were paid to make the listing succeed in the first place.

**Countermeasure.** This program's own free-data, price-only-majority construction discipline
(already the guiding principle for the value/quality composite, `docs/cycles/04-value-quality.md`
A.10) applies with particular force to recently listed names: a fresh-issuance flag lowering a
name's quality-composite score until an independent, multi-quarter track record accrues (already
this program's own design position, per D12's F1) is the correct treatment of exactly the
analyst-optimism-cascade risk this section documents, and this seat's own RECEPTION leg
(median first-day pop) is deliberately built from **bhavcopy price data**, never from analyst
target prices or recommendation counts, for precisely this reason.

### G.5 The desk's own traps

**Trap one — shorting froth early.** The single most dangerous misreading of this seat's own
output is treating an elevated regime-score reading as a **short signal** on issuance-linked
names or the primary-market segment generally. It is not, and cannot be: §A.4.ii states plainly
that the construct carries **no short-signal path**, its consumption is reduce-only sizing (a
smaller special-sits allocation, a negative contribution within the shared regime-score budget),
and the mandate's own hedge-only short-side constraint (CONTRACT §10) forecloses a directional
short on newly listed names in any case. A froth reading two months before a mania peaks looks,
in real time, indistinguishable from a froth reading two years before it peaks — this program's
own timing-uncertainty discipline (`docs/CYCLE_ATLAS.md` §0: ±20%-or-worse on anything above the
annual band) applies here with full force, and an operator who reads "the state is elevated" as
"therefore short it now" has converted a permission-shrinking signal into a directional bet the
signal was never built to support, exposing the desk to exactly the multi-year premature-short
losses that have humbled value-camp skeptics of every hot market this program's own record
documents.

**Trap two — mistaking SME-board microstructure for sentiment.** The second trap runs in the
opposite direction: reading the SME board's own extreme numbers (74% average listing gains,
oversubscription multiples running into the hundreds) as a literal, scaled-up version of the
mainboard sentiment reading, rather than as a **different microstructure phenomenon** wearing
similar-looking numbers. SME floats are tiny (frequently a few crore rupees of public float),
circuit-filter and price-band dynamics dominate early trading in a way bhavcopy-level data can
mask, and SEBI's own 2024 manipulation concerns (§A.3.3) are specifically about **engineered**
subscription and price patterns on this board — meaning the SME board's own numbers are, at
least partly, a *microstructure-manipulation* signal, not a *market-wide-sentiment* signal, and
conflating the two would badly misstate how representative the SME frenzy's specific magnitude
is of broader market sentiment. This is precisely why `partCDEFH.md`'s own construction keeps
SME as a **separate, satellite** series rather than blending it into the core mainboard state —
the desk's own discipline is to treat SME-board extremes as a useful, free, early-warning
confirming flag (a regulator's own froth thermometer, §A.3.3) while never scaling the mainboard
state's response off the SME series' own more extreme numbers.

### G.6 Countermeasures mapped

Four structural features already carry this Part's actual work, mirroring exactly the pattern
the sibling monographs' own psychology parts document. **(1) Population-level, narrative-blind
construction** (G.1, G.2) — the seat reads measured percentiles across the issuance population,
with no input channel for any individual name's story or any operator's personal application
experience. **(2) The reduce-only, no-short-path design** (G.5, trap one) — a froth reading can
only shrink permission, never license a directional bet, foreclosing the single most dangerous
misuse before it can occur. **(3) Mainboard/SME separation by construction** (G.5, trap two) —
the universe-exclusion rule (D12 F5) and the satellite-line treatment jointly prevent the SME
board's manipulation-inflated numbers from ever driving the core state. **(4) Price-data-only
RECEPTION measurement** (G.4) — building the pop measurement from bhavcopy rather than analyst
output makes the seat structurally immune to the underwriter-optimism cascade regardless of
whether India ever legislates a formal quiet period.

### G.7 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Reading a froth reading as a short signal | §A.4's construct carries no short-signal path; a mid-mania reading is indistinguishable in real time from an early one under this program's own ±20% timing-uncertainty discipline | L7 conditions reduce-only regime score and special-sits sizing; the hedge-only mandate (CONTRACT §10) independently forecloses a directional short |
| Scaling the mainboard read off SME-board extremes | SME floats are tiny, circuit-driven, and SEBI's own 2024 findings suggest partly engineered (§A.3.3, §A.3.5) — a microstructure-manipulation signal, not a market-wide sentiment one | Mainboard and SME held as separate series by construction (`partCDEFH.md` Part C); SME enters only as a satellite briefing/confirming line, never the core state |
| Treating "this IPO wave is structurally different" as a reason to override the state | Every historical wave (1994–96, 2007–08, 2017–18, 2021, 2023–25) arrived with a partially-true structural narrative indistinguishable, from inside the moment, from every prior one | State construction is narrative-blind; consumption is a pre-specified, reduce-only mapping with no discretionary override channel |
| Reading heavy promoter/PE OFS selling as bullish "smart money" confirmation | OFS is the cleanest insider revealed-preference signal available (§A.3.4, §G.3); retail sentiment mechanically reads high subscription + high selling as validation rather than warning | OFS share flagged explicitly in Stage-2 briefings, not left implicit; `IS-D3`'s design purpose is to make this leg an explicit, correctly-signed state input |
| Letting underwriter-affiliated analyst optimism substitute for a measured signal | India lacks a US-style formal quiet period, but the underwriter-analyst-optimism dynamic operates informally regardless (§G.4) | RECEPTION leg built exclusively from bhavcopy price data; fresh-issuance flag lowers quality-composite score until an independent track record accrues (D12 F1) |
| Anchoring personal satisfaction/regret about an IPO allotment onto the desk's regime read | Lottery-structured allotment + listing-day price anchoring is a designed-in behavioral amplifier (§G.1), and every desk member has personally felt it | The state reads the median across the population; no individual operator's application outcome enters the construct at any point |
| Applying the McLean-Pontiff generic haircut to the mechanism's existence rather than its magnitude | §A.1/§A.2.6: the incentive is structural and does not decay; only the measured statistical magnitude does, and by an amount this program has not yet estimated for India | Haircut applied to the regression coefficient only, per the ladder's own `decay` field; the mechanism's existence is carried forward at full confidence, pending IS1/IS2 |

None of these seven countermeasures asks the operator to be wiser, calmer, or more skeptical of a
good story than Part A's evidence justifies. Each converts a live judgment call — decide whether
this froth reading has peaked yet, decide whether the SME board's extremes are "real" sentiment,
decide whether this wave's narrative earns an exception, decide whether heavy insider selling
should worry or reassure, decide whether a freshly-covered name's analyst enthusiasm is
information or salesmanship, decide whether a personally-felt IPO-day win or loss says anything
about the market, decide how much of a decades-old finding to still believe — into a structural
non-decision, made once, in the registry, before the moment (a hot allotment, a soaring GMP
headline, a regulator's own warning arriving a year too late for the desk's taste) that would
have made it hardest.

---

*Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in). Date:
2026-09-02. v1.0.*

---

# PART B — Seven issuance waves, 1992-2026

# PART B — The India issuance-wave case record

*Issuance/sentiment-cycle monograph (atlas 3.2; ladder seat `L7_issuance_sentiment`,
`config/ladder.yaml`, Tier B, τ½ 12–24 months) · Part B · v1.0 · 2026-09-02 · Author: Claude
(research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 3.2 ("Issuers sell paper
when it's expensive [Baker-Wurgler] — a persistent incentive, not an information gap; SEBI's 2024
SME crackdown is the institutional confirmation"), `config/ladder.yaml`'s `L7_issuance_sentiment`
entry (Tier B, τ½ 12–24 months, `reduce_only: false`, block `valuation_sentiment`, role "sentiment
state; also sizes special-sits sleeve [froth => shrink]", indicator "NSE/BSE listings, SEBI
bulletins, bhavcopy first-day pops", `changes_if`: "India pre-registered test vs 2018/2023-24
episodes"), and the companion machinery already specified in `research/cycles/issuance-deep/
partCDEFH.md` (Parts C–H: the two-leg construction, `state_t` = availability-weighted mean of
{pct(volume/mcap), pct(median listing-day pop)}; the **IS1** Baker-Wurgler India test, **IS2** the
2018/2023-24 episode shape check, and **IS-D3** the promoter/PE-OFS third-leg candidate — all
registered there, none re-derived here). **Scope, stated once and held throughout: this Part owns
the PRIMARY-MARKET record** — verified issuance volumes and counts, the reception record
(subscription ratios, first-day pops), what the secondary market did in the 12–24 months after,
the regulatory response, and what L7's two-leg state would have read, era by era — **not** the
flow/positioning record (`research/cycles/fpi-deep/partB-cases.md` §B2 already owns the October
2007 P-note episode's FLOW side — the 9% intraday crash, the same-day ~80% recovery — cross-
referenced, never re-derived here), **not** the credit/shadow-banking mechanics of the 2018 freeze
(`research/cycles/shadow-deep/partB-cases.md` §B2 and `shadow-deep/shadow-RESULTS.md` own the
IL&FS funding-run anatomy and its SC1 factor-propagation finding, cross-referenced), **not** the
capex-cycle real-side account of the 2003–11 and 1994–97 booms (`research/cycles/capex-deep/
partB-cases.md` owns OBICUS/GFCF, the premium-issue-share statistic, and the Reliance Power
"top-tick artifact" framing this Part borrows and extends on the reception/aftermath side, cross-
referenced not re-derived), and **not** the theory (this seat's own sibling theory chapter,
`partA-theory-psychology.md`, carries the Baker-Wurgler mechanism and the
survival-argument case in full; cited here, not restated). Primary-source SEBI bulletins were not
directly queryable this session (egress blocked at the network proxy per `research/CONTRACT.md`
§7 Known Prior #11), so every figure below is cross-checked against secondary financial-press
reporting and SEBI-bulletin-derived secondary tables, exactly as this program's house style
requires.*

---

## B1. The mechanism this record tests, and what "two-leg" means for `L7`

**The claim, stated once rather than re-argued.** Baker & Wurgler (2000, *Journal of Finance*,
"The Equity Share in New Issues and Aggregate Stock Returns") find that the share of equity (vs.
debt) in aggregate US new issues from 1928–1997 is a strong, robust predictor of subsequent
aggregate stock returns: firms issue relatively more equity precisely before periods of low market
returns. Baker & Wurgler (2002, "Market Timing and Capital Structure") extend this into a
persistent-incentive mechanism rather than an information asymmetry: issuers time equity sales to
windows when their own stock (and the market generally) is priced richly, and this incentive
cannot be arbitraged away by knowing about it — the desk cannot short an issuer's own decision to
sell paper, which is precisely the survival argument `config/ladder.yaml` records for `L7`
(Tier B, not Tier C, on the strength of this global evidence) while flagging India's own
coefficients as still untested (`changes_if`).

**What "two-leg" means, precisely, per `partCDEFH.md` Part D — stated here because every case
below is read against it.** `L7`'s state is **not** issuance volume alone. It is an
availability-weighted mean of two separately percentile-ranked legs: **Leg 1**, issuance value
scaled by aggregate market capitalization (so a given rupee volume reads "hotter" against a
smaller float than a larger one — necessary given how much India's own market-cap denominator has
grown across this record's 34 years); and **Leg 2**, the *median* listing-day pop across that
window's issues (not the pop of one flagship deal — a market of one spectacular IPO and forty flat
ones is not, on this construction, in froth). The design point stated in Part D bears repeating
because several cases below turn on it: **the froth signature needs BOTH legs high** — volume
alone is capital formation (a real economy raising money to build things, `capex-deep`'s own
domain), and pops alone are scarcity (too few deals for too much demand) — and a wave that runs
one leg hot without the other is a genuinely different, and less informative, state than one that
runs both. This Part reads every era for exactly that distinction, not merely for a total-rupee
headline.

**The budget this seat sits in.** `L7` is not reduce-only (`config/ladder.yaml`:
`reduce_only: false`) — unlike most of this ladder's Tier-C seats, a hot two-leg state can add to
the `valuation_sentiment` regime score (jointly with `L8`'s value-spread — an expensive market
*and* a hot primary market is the double-confirm `partCDEFH.md` Part D names), and independently
sizes the special-situations sleeve down when froth flags (`role`: "sizes special-sits sleeve
(froth => shrink)"). Every case below is therefore read on two separate questions the design
actually asks: what did the regime score's `valuation_sentiment` block see, and what would the
special-sits sleeve's size have been cut to, in real time, at each wave's peak.

---

## B2. Seven issuance waves, case by case

### 1. 1992–1996 — the free-pricing boom, India's founding issuance-cycle lesson

**The regime change.** Facing the 1991 balance-of-payments crisis, the Government of India
abolished the Controller of Capital Issues (CCI) — the administered-pricing regime under which new
equity could only be sold at government-set, near-par prices — and gave the newly created
Securities and Exchange Board of India statutory power over primary-market pricing. The effect on
pricing freedom alone is the single cleanest statistic in this record's opening chapter: **premium
(above-par) issues rose from just 1.37% of new issues in 1991–92 to 45.90% by 1994–95**
**[Verified, cross-checked against `capex-deep/partB-cases.md`'s own citation of the identical
figure]** — a complete dismantling, in three years, of the administered-price regime for new
capital.

**The flood, dated and counted.** India's primary-equity-market mania "began towards the end of
1994 and peaked in February 1995." **January 1995 alone saw 145 equity issues open for
subscription**, including mega issues from Reliance Capital, Essar Oil, and Hindustan Petroleum;
**one week in February 1995 saw 78 companies go public**, capping a fiscal year (1994–95) that
brought roughly **1,400 issues** to market, with primary-market volume growing **32% year-on-year
in 1995 alone**. **[Verified, all figures, cross-checked against `capex-deep`'s own independent
citation of the identical statistics.]** A broader four-year compilation puts the whole 1992–1996
window at **₹86,000 crore raised through public and rights issues by roughly 4,000 companies**,
bringing **1.5 crore (15 million) new investors** into the market through IPOs for the first time.
**[Verified, per a Moneylife retrospective.]** The boom's real-economy content is genuine, not a
pure financial mania: this equity financed India's first wave of greenfield private-sector steel,
textile, and petrochemical capacity — the exact plants the 1997–98 commodity collapse then found
itself competing to sell into (`capex-deep/partB-cases.md`'s own case 1, cross-referenced not
re-derived).

**The reception.** Retail demand at the peak was, by any standard, saturating: 78 companies
listing in a single week is not a market absorbing new supply calmly — it is a market where any
priced-above-par offer found a buyer. Systematic subscription-ratio and first-day-pop data for
this pre-NSDL, pre-electronic-settlement era could not be independently reconstructed this pass
`[VERIFY: a genuine per-issue subscription/pop series for 1994–96 — bhavcopy-based reconstruction
predates NSDL's own 1996 launch and the depository system generally, exactly the data gap
`capex-deep`'s own case 1 already documents for the real-side capacity data of the same years]`;
the qualitative record is unambiguous that issues were routinely and heavily oversubscribed at the
peak, consistent with the premium-issue-share statistic above.

**The vanishing-companies scandal.** The boom's dark twin, surfacing as the bust set in: companies
raised public money in collusion with investment bankers, brokers, and (in several documented
instances) banks, then simply disappeared, filing no further returns and leaving no operating
trace. **Over 600 companies vanished from the stock markets after raising money in 1998**; SEBI
named an initial **80 companies (having raised over ₹330 crore)** in May 1998, before widening
scrutiny to more than 600; a dedicated committee subsequently and more narrowly identified **238
listed companies** as genuinely "vanishing," of which **161 were eventually traced and 77 remained
untraceable**. **[Verified, the Moneylife retrospective's figures; the 600-vs-238 gap is itself
informative — a wide net cast, a narrower core confirmed]** `[VERIFY: precise reconciliation of
the >600 initial scrutiny count against the 238-company confirmed "vanishing companies" list — the
two are not the same population and this pass's search could not fully bridge them]`. Investor-
association estimates put the total value of vanished-company capital in excess of **₹29,000
crore**, out of an era-wide ₹86,000 crore raised — on this reckoning, roughly a third of everything
the boom raised. **[VERIFY: the ₹29,000 crore estimate's own primary source and methodology.]** A
separate, later retrospective count puts the number of listed companies that disappeared from
regional stock exchanges specifically at **roughly 700** `[VERIFY: whether this 700-company regional-
exchange count is the same population as, or additive to, the 238-company "vanishing companies"
list above]` — no single reconciled national count of "vanished" issuers from this era exists on
the record this pass could locate, and this Part states that honestly rather than picking one
number and presenting it as settled.

**The turn and the 1996–98 primary-market winter.** The July 1997 Asian financial crisis (the
contagion source `capex-deep`'s own case 1 and the Asian-Tigers capex mirror both document) ended
the boom; India's own growth decelerated from 7.8% (1996–97) to 4.8% (1997–98), and global
commodity prices for exactly the sectors the 1994–96 equity wave had built (steel, petrochemicals,
textiles) fell sharply, compressing the revenues of freshly built plants before they had even
amortized their construction cost. The primary market's own collapse is precisely, and severely,
measured: **1996–97 saw 882 issues raise ₹14,275.98 crore; 1997–98 saw just 111 issues raise
₹4,569.95 crore — a decline of 87.41% in the number of issues and 68.01% in the amount raised, in
a single year.** **[Verified, per SEBI's own Annual Report 1997–98 data.]** The workout that
followed ran for a decade and a half past the crisis itself: nationalised-bank GNPA fell from
**19.05% (1997) to 12.16% (2001)**, while the Board of Industrial and Financial Reconstruction
(BIFR) — the era's actual rehabilitation venue — registered **5,471 references by 2007**, of which
only **825 revival schemes were ever sanctioned** (a ~12–15% success rate), and the Sick Industrial
Companies Act itself was not repealed until **December 2016**, nineteen years after the crisis that
overwhelmed it. **[Verified, both, cross-referenced to `capex-deep/partB-cases.md`'s own case 1,
not re-derived.]** The RBI's Corporate Debt Restructuring mechanism, born **23 August 2001**, is
this era's first institutional answer to a boom-bust cycle it had no machinery to manage in real
time.

**What L7's two-leg state would have read.** No usable two-leg percentile exists this early — the
same structural gap `fpi-deep/partB-cases.md` §B1 documents for `L14`'s ownership percentile in
the identical years: a bhavcopy-and-listing-day-pop series requires the depository and electronic-
settlement infrastructure that NSDL only brought online from 1996, and the volume/mcap Leg 1
denominator itself is barely meaningful against a market capitalization this thin and this newly
opened. What the record *does* offer, directly and without needing the percentile machinery, is the
qualitative two-leg reading `partCDEFH.md` Part H already states as an established finding: 1994–96
is the record's founding instance of a wave that ran **both legs hot simultaneously** — extreme
issuance volume (Leg 1, on any reasonable reading given 1,400 issues against 1995's market
capitalization) and, on the qualitative record, extreme reception (Leg 2) — and that the same
extremity is exactly what let the vanishing-companies fraud hide inside genuine euphoria: a market
absorbing 78 IPOs in a week has no capacity left to scrutinize any one of them.

---

### 2. 1999–2000 — the tech mini-wave

**The build.** India's software-services boom — exports crossing **US$1 billion in 1997** and
reaching **US$6.2 billion within four years** — collided with Y2K remediation demand and the
global dot-com rally to produce the decade's second issuance wave, smaller and shorter than 1994–96
but carrying the same reception signature. **Infosys listed American Depositary Receipts on
Nasdaq in March 1999**, the first Indian company to do so, and its own share price run — reported
at levels on the order of ₹8,100 by 1999 before a further climb into 2000 — is the era's own
"top-tick artifact" in miniature, a domestic tech-mania stock whose price action tracked the
Nasdaq's own bubble almost exactly. **[Verified, the Nasdaq listing date and the exports figures;
the specific Infosys price levels reported across secondary sources vary and are flagged
`[VERIFY: precise Infosys share-price series 1999–2000]`.]** At the aggregate primary-market level,
**total funds mobilised across 151 issues came to roughly ₹7,817 crore in FY1999–2000**, with
average issue size of **₹53 crore** — falling to **₹6,108 crore and an average issue size of ₹24
crore in FY2000–01** as the wave rolled over. **[Verified, though the precise per-year issue-count
split behind the 151-issue figure is not cleanly disaggregated in the source located this pass;
`[VERIFY: the exact FY1999-2000 vs FY2000-01 issue-count breakdown]`.]** Rights issues from
established software names rode the same wave, though a clean, sourced rights-issue tally
specifically for this window could not be independently pinned this pass
`[VERIFY: FY1999-2000 rights-issue volume specifically, as distinct from fresh IPO volume]`.

**The reception.** Consistent with the boom's own genuine software-sector fundamentals (real export
growth, real Y2K-driven order books) layered under a speculative multiple, tech-adjacent IPOs and
rights issues of this window are qualitatively remembered as heavily oversubscribed and strongly
popped on listing, mirroring the Nasdaq-era mania premium global tech names commanded over the same
window; a systematic, sourced subscription-ratio table specific to this wave's individual issues
was not independently reconstructed this pass `[VERIFY: per-issue subscription data, 1999-2000
tech-sector IPOs and rights issues]`.

**What the secondary market did next.** The Ketan Parekh "K-10" stock-manipulation scandal unwound
from March 2001, compounding the global Nasdaq collapse; the Sensex fell on the order of **38%
during 2001** (cross-referenced to `fpi-deep/partB-cases.md` §B1's own figure, itself flagged
`[VERIFY: precise peak-to-trough Sensex dating]` there and not re-derived here). The genuinely
striking finding this Part inherits from `fpi-deep`'s own flow-side record, worth restating because
it bears directly on the issuance-wave read: **registered FII flows stayed net positive through
both FY2000–01 and FY2001–02** even as returns collapsed by nearly 40% — a domestically generated
crash (a manipulation unwind plus a global tech-bust echo) that foreign portfolio flows did not
meaningfully participate in selling into, per `fpi-deep` §B1's own honestly-flagged finding. This
Part's own contribution is the primary-market mirror of that same divergence: issuance volume
itself had already begun rolling over ahead of the crash (FY2000–01's ₹6,108 crore below
FY1999–2000's ₹7,817 crore), consistent with issuers' own incentive to sell into strength while it
still existed, rather than issuance being the proximate trigger of the 2001 collapse.

**The regulatory response.** SEBI and the exchanges' principal institutional response to this era
belongs more to the secondary-market manipulation side of the 2000–01 crash (the Ketan Parekh
investigation and subsequent badla/carry-forward-trading reforms) than to a primary-market-specific
intervention; no dedicated issuance-side regulatory reform specific to this wave (comparable to the
CCI abolition that opened the prior era, or the SME curbs that close this record) was located this
pass `[VERIFY: whether a specific 1999–2001 primary-market regulatory response, distinct from the
Ketan Parekh secondary-market inquiry, exists]`.

**What L7's two-leg state would have read.** Leg 1 (volume/mcap) reads only moderately hot on the
verified aggregate figures — ₹7,817 crore is a fraction of 1994–95's own scale, and it arrives
against a market capitalization already inflated by the tech rally itself, which mechanically
dampens the volume/mcap percentile even during genuine euphoria (the same denominator effect
`partCDEFH.md`'s own Part D flags as a reason to percentile-rank Leg 1 rather than read raw rupee
totals). Leg 2 (median pop), on the qualitative record, likely ran hotter than Leg 1 — a
sector-concentrated mania (software/tech names specifically) can produce extreme median pops on a
comparatively modest issuance base, precisely the "pops without matching volume" asymmetry Part D's
own AND-logic is built to distinguish from genuine broad-based froth. This Part flags, rather than
resolves, whether 1999–2000 constitutes a genuine both-legs-hot instance or a Leg-2-dominant one —
the per-issue data needed to settle it was not reconstructable this pass.

---

### 3. 2004–2008 — the great wave, and Reliance Power as the top-tick artifact

**The build, by scale.** India's 2003–2007 real-economy boom (`capex-deep/partB-cases.md`'s own
case 2, the "infra supercycle") ran alongside, and was substantially financed by, the largest
sustained equity-issuance wave in the record to that point. **ONGC's March 2004 IPO** — 142.59
million shares at ₹750 (retail discount ₹712.50), aggregating **₹10,694.50 crore** — mobilised bids
worth **~₹73,000 crore, oversubscribed 6.82 times**, one of the largest public issues in Indian
history to that date. **[Verified, all figures reconciled: 6.82 × ₹10,694.5cr ≈ ₹72,940cr, matching
the ~₹73,000cr bid total independently reported.]** **DLF's June–July 2007 IPO** — 175,000,000
shares at ₹525, aggregating **₹9,187.50 crore (~US$2 billion)** — was overall subscribed **3.47
times** (the QIB portion alone 5.13 times), listing 5 July 2007; contemporaneous reporting flagged
comparatively tepid *retail* demand even as institutional demand ran hot — an early instance of the
same leg-divergence this Part's later cases (2010, 2021) repeat at larger scale. **[Verified.]**
SEBI's introduction of the **Qualified Institutional Placement (QIP)** mechanism in 2006 added an
entirely new institutional-only supply channel mid-wave, layering directly atop the IPO calendar; a
precise FY2004–FY2008 cumulative IPO-plus-QIP total could not be pinned to one primary table this
pass `[VERIFY: exact FY03–08 five-year cumulative IPO+QIP figure — annual counts (78 IPOs/$7.23bn
in 2006; a widely cited 93–103 IPOs in 2007, figures not reconciled this pass) and a 2006–07
combined primary-market total of ₹1,61,769 crore (including private placement, not IPO-only) are
the closest independently verified anchors]`.

**The reception, and the era's own IPO-allotment scandal.** Retail-allotment fraud surfaced mid-wave
in the so-called **IPO Demat Scam**: Roopalben Panchal and associates used thousands of fictitious
demat accounts to corner retail-quota shares — the December 2005 YES Bank IPO was the case that
exposed it, and SEBI's subsequent probe widened to **105 IPOs across 2003–2005**, finding
irregularities in **21** of them; SEBI ultimately issued directions against **82 financiers, 24 key
operators, 12 depository participants, and 2 depositories**, and eventually disgorged and
redistributed roughly **₹41.34 crore to some 1.27 million investors**. **[Verified.]** Academic
work on IPOs listing across 2002–2006 finds average first-day underpricing (listing performance
against the market index) on the order of **46.55%** `[VERIFY: precise study scope, sample, and
exact index-adjustment methodology behind the 46.55% figure]` — consistent with a wave running hot
reception broadly, not merely at a handful of flagship names.

**Reliance Power, January 2008 — the top-tick artifact, cross-referenced from `capex-deep`, extended
on the reception side.** `capex-deep/partB-cases.md`'s own case 2 already names Reliance Power's
IPO "the single most literal 'IPO at the top' instance this desk's entire cycle-atlas project has
yet documented" — this Part does not re-derive that finding, only extends it on the primary-market
reception side its own scope owns. The issue: **₹11,700 crore, priced at ₹450/share, opened
January 2008, oversubscribed 73 times**, for a company that at the time of its IPO had **no
operating assets and no cash flow** — pure greenfield power-capacity promise monetized at the exact
top of a six-year boom. Subscription closed within days of the **Sensex's own all-time intraday
high, 21,206.77 on 10 January 2008**. **[Verified, both.]** It listed **11 February 2008**: opened
at ₹530 (a 17% premium to issue), touched an intraday low of ₹355.05, and closed the same day at
**₹372.50** — a loss for every day-one allottee before the stock fell much further over the
following years, never regaining its issue price; by November 2017 it had made a fresh low of ₹35,
and ₹10,000 invested at the IPO was worth roughly ₹1,636 a decade on. **[Verified, all figures,
cross-checked against `capex-deep`'s own independent citation of the identical listing-day
numbers.]** A 73× oversubscription record and a same-day negative return are not, on their face,
contradictory — they are the record's cleanest single demonstration that Leg 2's *median* pop and
a flagship deal's own outcome can diverge from the mania that produced the demand in the first
place: retail and institutional money chased the *name*, not a defensible valuation, and the price
discovered on day one reflected that gap almost immediately.

**What the secondary market did next — the 2008 shutdown.** Reliance Power listed five weeks before
the Sensex began its collapse; the global financial crisis then closed the primary market almost
completely. Calendar-2008 IPO count fell to **37–38 issues, raising a combined ~US$3.8 billion**,
down from **103 (2007, `[VERIFY: exact count, a competing source puts 2007 at 93]`) and 79 (2006)**
— **three major firms formally withdrew planned IPOs** for lack of investor response, and
**FY2008–09 mobilised just ₹2,034 crore through 21 small IPOs**, a collapse on the order of 95%+
from the prior fiscal year's pace. **[Verified, the aggregate figures.]** Nifty fell from its
January 2008 peak (~6,357) to its October 2008 trough (~2,252), on the order of **60–65%**
(cross-referenced to `fpi-deep/partB-cases.md` §B2 and the credit monograph's own case #10, not
re-derived here) — the primary market's own shutdown running in lockstep with, not ahead of or
behind, the secondary-market collapse.

**The regulatory response.** The Panchal-era demat-scam enforcement (above) is this wave's own
mid-cycle institutional response, tightening retail-allotment integrity years before the wave's own
top; no comparably dedicated *post*-2008 primary-market-specific reform (distinct from SEBI's
general disclosure and QIP-eligibility tightening across the following years) was located this pass
as a direct response to the Reliance Power episode specifically `[VERIFY]`.

**What L7's two-leg state would have read.** This is the record's cleanest instance of both legs
running hot simultaneously and in the same direction — Leg 1 (record cumulative volume, a wave
running IPO and the newly available QIP channel together) and Leg 2 (73× on the era's largest
single deal, 46.55%-average underpricing across the broader 2002–06 sample) both sit at, or near,
the top of any reasonable percentile construction, exactly the AND-condition `partCDEFH.md` Part D
requires for a genuine froth flag. `partCDEFH.md` Part H's own established finding — "India's
issuance waves top-tick markets with regularity (1994–96, **2007–08**, 2021, 2024)" — is directly
grounded in this case: a two-leg-hot state arriving five weeks before the market's own all-time high
is precisely the state the seat is built to catch, and precisely the case where the special-sits
sleeve's froth-triggered shrink rule would have been earning its keep at the exact moment retail
capital was chasing a pre-revenue power developer at 73 times demand.

---

### 4. 2010–2011 — the PSU/QIP echo

**The build.** Post-GFC recapitalization first ran through the QIP channel: **2009 saw 96
companies raise a combined ₹64,750 crore through QIPs, IPOs, and rights issues together**, and
real-estate companies specifically raised **₹14,224 crore via equity offerings in 2009, rising to
₹23,914 crore in 2010** — largely QIP-routed refinancing of balance sheets stressed by the
2008 shock. **[Verified, both years' real-estate figures; the ₹64,750cr 2009 combined figure per a
Business Standard year-end compilation.]** The IPO calendar itself then delivered a new record:
**64 companies mobilised ₹37,535 crore in 2010** — a new all-time high, surpassing every prior year
in this record including 2007–08's own peak. **[Verified.]** The centerpiece: **Coal India's
October 2010 IPO** — issue size **₹15,199.40 crore**, priced at **₹245/share**, offer window 18–21
October 2010 — was subscribed **15.28 times**, listed **4 November 2010**, and stood as **India's
largest-ever IPO**, surpassing Reliance Power's own then-record ₹11,700 crore. **[Verified, all
figures.]** The wave's supply, notably, was substantially **state-engineered**: a disinvestment
calendar of PSU share sales (Coal India chief among them), not an organically arising private-sector
issuance boom — a genuinely different mechanism from 1994–96's or 2007–08's private-sector-led
mania, worth flagging explicitly because it changes what Leg 1 alone would be measuring.

**The reception.** Coal India's 15.28× subscription is a genuine, broad-based demand signature, not
merely an institutional book-building formality; but a single flagship deal's own oversubscription
is not, on `L7`'s own construction, a substitute for the *median* pop across the year's full 64-deal
slate — and the 2011 QIB-participation collapse (below) is itself circumstantial evidence that
2010's reception was considerably more concentrated in a handful of PSU/large-cap names than the
headline record-year total suggests `[VERIFY: a genuine per-issue 2010 subscription/pop
distribution, to test whether the median (not merely the Coal India outlier) ran hot]`.

**What the secondary market did next — the 2011 fade.** The wave rolled over sharply within a
single calendar year: **India's primary market shrank over 64% in January–September 2011 versus
the year-earlier period — 38 companies raised ₹6,004 crore in the first nine months of 2011,
against 50 companies and ₹16,709 crore over the same window in 2010** — an **eight-year low** for
IPO fundraising. **Roughly 28 companies called off their public-issue plans for the year**, and
**26 of 39 issues (two-thirds) failed to receive even the minimum one-time QIB subscription**.
**[Verified, all figures.]** A contemporaneous retrospective found 2011's IPO cohort had, on
average, **eroded roughly one-third of its own aggregate issue-size value** by year-end — a genuine
wealth-destruction outcome for the year's own allottees, not merely a slower pace of new supply.
**[Verified.]** The Sensex itself fell on the order of the broader 2011 global-risk-off episode
(the Eurozone crisis, domestic policy paralysis, and rupee weakness `[VERIFY: precise Sensex
2010-peak-to-2011/12-trough figure — not independently re-derived this pass, and outside this
Part's own primary-market scope]`), consistent with — though this Part does not independently
verify a precise causal lag — the record's recurring pattern of a hot issuance year giving way to
weak subsequent secondary-market conditions within twelve to twenty-four months.

**The regulatory response.** No dedicated primary-market regulatory intervention specific to the
2010–11 wave (comparable to the 2005–06 demat-scam enforcement, or the 2024 SME curbs) was located
this pass; the era's own institutional lesson is executional rather than regulatory — a
disinvestment calendar timed to a strong secondary market extracted genuine value for the exchequer
(Coal India's own scale) but arrived close enough to the wave's own top that within a year two-
thirds of the following cohort's issues could not clear even the QIB minimum.

**What L7's two-leg state would have read.** This case is the record's clearest illustration of
Part D's own AND-logic design point stated in §B1 above: **Leg 1 alone, read in isolation, would
have flagged 2010 as an unambiguous froth year** — record cumulative volume (₹37,535cr), a
record-breaking flagship deal, and a genuine acceleration off 2009's already-elevated QIP-led base.
**Leg 2, read against the *median* rather than the flagship**, plausibly confirms only partially —
a state-engineered disinvestment supply wave concentrated demand in a small number of PSU names
precisely because the government, not organic private-sector sentiment, set the calendar, and
2011's immediate two-thirds QIB-shortfall rate is circumstantial evidence the broader deal slate's
underlying reception was considerably less universal than Coal India's own headline number implies.
A design that read Leg 1 without Leg 2 here would have overstated genuine speculative excess and
under-read how much of 2010's volume was supply-side (a state seller monetizing a strong tape)
rather than demand-side (buyers bidding up scarce paper) — precisely the "volume alone is capital
formation, pops alone are scarcity" distinction `partCDEFH.md` Part D states as the reason the
construction requires both legs together.

---

### 5. 2014–2018 — the institutional wave, and the IL&FS freeze

**The build.** A second post-election institutional-issuance wave ran 2014–2017, headlined by a run
of insurance, asset-management, and exchange listings that had, in several cases, waited years for
a regulatory or promoter-strategy green light. **HDFC Life's November 2017 IPO** — 29.98 crore
shares, aggregating **₹8,695 crore** — bid 7–9 November 2017. **HDFC AMC's July 2018 IPO** —
**₹2,800.33 crore**, bid 25–27 July 2018 — was **103% subscribed on Day 1** alone
`[VERIFY: the final, full-book multi-day subscription multiple — only the Day-1 headline figure
was independently pinned this pass]`. **General Insurance Corporation's IPO — the largest single
mainboard issue of the year at ₹11,257 crore** — anchored a record calendar-2017: **36 mainboard
IPOs raised ₹67,147–68,826 crore in 2017 [figures per two closely-agreeing secondary compilations,
`[VERIFY: exact reconciled total]`]**, decisively surpassing 2010's own ₹37,535 crore record; a
broader count including SME issues puts **153 total IPOs raising US$11.6 billion for the full
calendar year**. **[Verified, all figures.]** **Seventeen of the 36 mainboard issues received more
than 10× subscription, and 18 of the 36 delivered listing-day returns above 10%** — a genuinely
broad-based, not merely flagship-concentrated, reception signature, a useful contrast with case 4's
own concentration caveat.

**The reception.** The breadth statistic above — roughly half the year's mainboard cohort both
heavily oversubscribed *and* popping double digits on debut — is the strongest median-pop evidence
this Part's own record carries for any pre-2020 era, precisely the both-legs-simultaneously-broad
signature `partCDEFH.md`'s own Part H names 2007–08 for. Against a market capitalization that had,
by 2017, grown substantially past its 2007–08 scale, the *volume/mcap* Leg 1 percentile likely ran
somewhat less extreme in relative terms than 1994–96's or 2007–08's own readings even at a larger
absolute rupee total — the exact denominator effect §B1 above names.

**What the secondary market did next — the IL&FS freeze.** The **14 September 2018 default** of
Infrastructure Leasing & Financial Services (IL&FS) — `shadow-deep/partB-cases.md` §B2's own
centerpiece, cross-referenced not re-derived here — triggered a system-wide NBFC funding freeze
whose 12-month equity-factor propagation `shadow-deep/shadow-RESULTS.md`'s own SC1 trial measures
directly: small-cap returns fell **−24.8% (18th percentile)** and the broad market fell **−20.2%
(16th percentile)** over the September 2018–August 2019 window, a finding that chapter's own honest
read states plainly — "the freeze did NOT stay contained" to NBFC-adjacent names; by the time a
12-month equity window could see it, it was "everyone's problem." This Part's own contribution is
the primary-market transmission that finding implies but does not itself measure: the pipeline of
already-SEBI-approved issuers **froze in place** rather than reaching the market. By **December
2018**, SEBI's own chairman was publicly lamenting the slow pace of IPOs reaching market despite
roughly **₹600 billion (~US$8.43 billion) of standing SEBI approvals**; by **August 2019**, nearly
**two dozen companies' SEBI approvals were set to lapse** unused, together representing a further
**₹16,500 crore** of capital that never reached the market inside its approval window. **[Verified,
both figures.]** Calendar-**2019 IPO count fell to 62 issues raising US$2.53 billion
(~₹17,899 crore)** — a **62% decline in volume and 54% decline in proceeds** versus 2018 — confirming
the freeze extended through the whole of the following calendar year, not merely the acute
September–December 2018 window. **[Verified.]**

**The regulatory response.** SEBI's own December 2018 public commentary on the slow IPO pace is
itself a regulator reading the freeze in close to real time — exactly the "a regulator acting IS a
reading" annotation `partCDEFH.md` Part E's algorithm step 4 already builds into the seat's
construction. The freeze's actual resolution ran through the credit-side institutional machinery
`shadow-deep/partB-cases.md` §B2 documents in full (the Section-241(2) board supersession, the new
management's asset-monetization program) — not a primary-market-specific reform — consistent with
this being fundamentally a credit-shock transmission into the issuance pipeline, not an issuance-
side pathology in its own right.

**What L7's two-leg state would have read.** A moderate-to-high two-leg reading through 2017 (broad
subscription and broad pops, a somewhat damped Leg 1 percentile given the larger by-then market cap)
gives way, within a year, to a state where **both legs collapse simultaneously and for the same
external reason** — not a wave that priced its own excess (as 2007–08's did) but one interrupted by
an external credit shock arriving from outside the issuance mechanism entirely. This is a
genuinely different failure mode from every other case in this record: the two-leg state correctly
reads "cold" through 2019, but a design attributing that cold reading to *sentiment having turned
of its own accord* — rather than to a credit-side external shock this seat was never built to watch
(the same single-pool blind spot `fpi-deep/partB-cases.md` §B3 documents for `L14`'s own 2013 debt-
pool miss) — would mis-attribute the mechanism even while reading the state correctly.

---

### 6. 2020–2022 — the startup wave, and the leg-decoupling at its top

**The build.** India's post-COVID new-economy issuance wave ran through 2021 at a pace this
record's earlier eras never matched in *count*: calendar-**2020 saw 43 IPOs raise US$4.09 billion**,
building through the year (**19 IPOs worth US$1.84 billion in Q4 2020 alone**), before 2021
delivered the record itself. **[Verified.]**

**The reception, at its most euphoric.** **Zomato's July 2021 IPO** (price band ₹72–76) was
subscribed **38.25 times**, opening around ₹116 — a **~52% premium to its ₹76 issue price** — and
rising further intraday. **[Verified.]** **Nykaa's November 2021 IPO** — **₹5,300 crore**, price
band ₹1,085–1,125 — drew bids for **216.59 crore shares against an offer of 2.64 crore, an 81.78×
subscription**, and opened at **₹2,018, an 80% gain** over its ₹1,125 issue price. **[Verified.]**
Both are genuine both-legs-hot instances at the level of the individual deal: heavy demand (Leg-2-
relevant subscription) *and* a large pop, arriving inside a calendar year running record aggregate
volume (Leg 1).

**Paytm, November 2021 — where the legs decoupled.** **Paytm's IPO — ₹18,300 crore — was, at the
time, India's largest-ever public issue**, comfortably surpassing Reliance Power's 2008 record.
Day-1 subscription ran to only **~18%** of the retail/non-institutional book
`[VERIFY: the final, full-book overall subscription multiple across all investor categories — this
pass located only the Day-1 headline]`. It listed **18 November 2021**: opened at **₹1,950 on the
NSE — already 9.3% *below* the top of its ₹2,080–2,150 price band** — and closed the day down
**more than 27% at ₹1,560**, the single **largest listing-day fall in Indian IPO history**, wiping
out on the order of **₹38,000 crore of investor wealth on debut alone**. **[Verified, all figures.]**
Twelve months on, the divergence from 2021's other headline listings had only widened: by **22
November 2022**, Paytm shares had fallen to an all-time intraday low of **₹476.65** (closing
₹477.1) — a decline of roughly **78% from the ₹2,150 issue price**, and market capitalization was
down some **77%** from its IPO-day peak of over **₹1.38 lakh crore**. **[Verified, both figures —
the precise magnitude (≈78% at the twelve-month mark) is somewhat larger than the "≈75%" order-of-
magnitude figure this task's own framing carries; this Part adopts the more precisely sourced ≈78%
reading and flags the gap rather than silently rounding it away.]** This is the record's single
cleanest demonstration of Part D's own design point in the opposite direction from case 4: **Leg 1
spiked to a record on the back of a single mega-issue precisely as Leg 2 (the broader pop leg) was
already cracking** — a market that had just delivered Zomato's 52% and Nykaa's 80% pops absorbed a
record-size new issue with a *negative* Day-1 return, the clearest possible signature of a wave
arriving at, or just past, its own top rather than at its build phase.

**The LIC IPO, May 2022 — the wave's damp end-marker.** **LIC's IPO — ₹21,008.48 crore, India's
largest-ever at the time**, price band ₹902–949 — subscribed **~3 times overall** (67% on Day 1
alone) — but its listing was, in the words of contemporaneous reporting, "set for a lacklustre
market debut despite oversubscription." It listed **17 May 2022** down **7.8%** on debut — **the
second-worst first-day performance among the eleven global companies that raised over US$1 billion
through an IPO anywhere in 2022** — and by **9 June 2022** had fallen a further leg to stand **24%
below its issue price**. **[Verified, all figures.]** A subscribed-but-unloved debut, arriving
seven months after Paytm's own outright crash, is this record's cleanest closing signature for a
wave: not a collapse in issuance *supply* (LIC's own size confirms issuers, or in this case the
government as seller, were still willing and able to bring the largest deal in Indian history to
market) but a collapse in the market's willingness to *reward* new supply with a pop — precisely
the Leg-2 failure that marks a wave's genuine end, as distinct from Leg 1 merely running out of
deals to bring. The retail-participation overlap this wave rode — the demat-account surge and F&O
boom `docs/CYCLE_ATLAS.md` Atlas 3.6 already owns as its own row, cross-referenced not re-derived
here — is the standing domestic bid this Part's own reception figures show arriving in size for
Zomato and Nykaa, then visibly refusing to show up in the same size for Paytm and LIC seven months
apart.

**The regulatory response.** No SEBI action specific to the Paytm listing-day collapse was located
this pass (the episode is, on the public record, a market-pricing outcome rather than a disclosure
or process failure); SEBI's broader tightening of anchor-investor lock-in and pricing-disclosure
norms across 2021–22 is contextual, not a dedicated response to this wave's own top-tick episode
`[VERIFY: any SEBI-specific post-mortem or rule change directly attributable to the Paytm/LIC
episodes]`.

**What L7's two-leg state would have read.** 2021's calendar-year aggregate reads hot on both legs
through Zomato and Nykaa's own deals — but the two-leg construction's own AND-logic is precisely
what would have flagged Paytm's arrival as a warning rather than a confirmation: a record-scale Leg
1 contribution landing with an already-negative Leg 2 outcome is the textbook divergence signature
the design is built to catch, not merely a large number that happened to disappoint. `partCDEFH.md`
Part H's own established finding lists **2021** among the record's clean top-tick instances
alongside 1994–96 and 2007–08 — this case is the concrete mechanism behind that entry: the wave's
own largest single deal is where the two legs visibly came apart, seven months before the wave's own
final, confirming, damp-reception deal (LIC) closed the era out.

---

### 7. 2023–2026 — the SME frenzy and the broadening

**The mainboard build.** **FY2023–24 (FY24): 76 mainboard IPOs raised ₹61,915 crore**, up **~19–20%**
from **FY2022–23's 37 IPOs and ₹52,116 crore** — the largest single deal, **Mankind Pharma's April
2023 ₹4,326 crore** offer-for-sale, subscribed **15.3 times** on bids worth roughly **₹50,000
crore**, followed by Tata Technologies (₹3,043 crore) and JSW Infrastructure (₹2,800 crore).
**FY2024–25 (FY25): 79–80 mainboard IPOs raised over ₹1.62 lakh crore** — roughly **2.6× FY24's
total**, one of the most active fundraising years in the market's history. **[Verified, all
figures.]** Calendar-**2024 (mainboard + SME combined): 91 public offerings raised ₹1.59 lakh
crore**; calendar-**2025: 373 total issues (103 mainboard, 270 SME) raised ₹1.95 lakh crore**, the
largest calendar-year total on record, part of a **2020–2025 cumulative IPO fundraising figure of
₹5.39 lakh crore that itself exceeds the entire 2000–2020 twenty-year cumulative total of ₹4.56
lakh crore**. **[Verified, all figures.]**

**The SME-board frenzy, the wave's own genuinely new content.** **243 SME IPOs launched in 2024
(240 having debuted), raising roughly ₹8,700 crore net of anchor books** — a small fraction of the
mainboard's own rupee total but a genuinely distinct microstructure the wave brought fully into
view for the first time at this scale. **Oversubscription records were set repeatedly through the
year: HOAC Foods India at ~1,963 times (May 2024), Magenta Lifecare at ~1,003 times (June 2024)**,
and a further cluster — Green Hitech Ventures (771×), Koura Fine Diamond Jewellery (727×), Maxposure
(697×), Medicamen Organics (688×), Slone Infosystems (642×) — with **16 of the all-time top-20
SME-oversubscription list dated to 2024 alone**; the five most-overbought SME issues of the year
drew cumulative bids exceeding **₹65,000 crore against a combined ₹59.3 crore they aimed to
raise — over 1,100× in aggregate**. **[Verified.]** A genuine *central-tendency* reading, not
merely the outlier tail, is also on record for part of the year: the segment's own **average**
subscription multiple ran to **242 times in September 2024** before cooling to **112 times by
November 2024** as the frenzy's own pace decelerated intra-year — average listing gains for the
full FY24 SME cohort exceeded **50%**, with applications running to roughly **113,000 per
IPO** on average. **[Verified — an average, not the median this Part would prefer; a genuine
median-subscription series specific to the SME board was not independently located this pass
`[VERIFY: median, as distinct from mean, SME subscription multiple, 2024]`.]** **Listing-day
breadth confirms this was not a
handful-of-outlier-deals phenomenon: across FY2023–24 and FY2024–25, over 90% of SME IPOs listed at
a premium**, with **214 of the year's SME debuts closing their maiden session in the green against
just 22 closing lower**. **[Verified, all figures.]** This is the record's single clearest
instance of Leg 2 (median pop) running hot at genuinely extreme percentile levels across an entire
sub-market's breadth, not merely at its flagship deals — the SME board's own microstructure (thin
float, small deal sizes, retail-dominated books) is precisely why `partCDEFH.md`'s own Part C keeps
the SME series *separate* from the mainboard state rather than pooling them, and precisely why Part
E's algorithm treats SME as "a satellite briefing line" rather than folding it into the primary
state — "the 2023–25 frenzy showed why," as that document's own Step 1 already states.

**The regulatory response — SEBI's 2024 interventions, the ladder's own institutional
confirmation.** SEBI's board meeting of **18 December 2024** tightened SME-IPO rules directly in
response to exactly this pattern: concerns that companies were diverting IPO proceeds to
shell entities and manipulating financials through related-party transactions. The new rules
require **positive operating profit (EBITDA) in at least two of the three preceding financial
years**; raise the **minimum retail application size from ₹1 lakh to ₹2 lakh** (explicitly to
reduce retail participation in the riskiest issues); cap **general-corporate-purpose fund
allocation at 15% of issue size or ₹10 crore, whichever is lower**; cap **offer-for-sale at 20% of
the total issue size**; mandate a **monitoring agency with quarterly utilization reports for issues
above ₹50 crore**; and extend mainboard-style **related-party-transaction norms** to SME-listed
entities. **[Verified, the full rule set.]** This is precisely the episode `docs/CYCLE_ATLAS.md`
row 3.2 and `config/ladder.yaml`'s own `L7` entry both already cite as "the institutional
confirmation" of the issuance-sentiment mechanism — a regulator, observing the same froth this
Part's own oversubscription and pop statistics document, acting to curb it directly, exactly the
"a regulator acting IS a reading" design principle `partCDEFH.md` Part E's algorithm already
encodes as Step 4.

**QIP and OFS records, the wave's institutional-supply side.** **Qualified Institutional
Placements hit an all-time high in calendar 2024: roughly ₹1,37,560–1,41,482 crore raised across
95–99 QIPs** `[VERIFY: exact reconciled total and issue count — two closely-agreeing secondary
compilations differ modestly]`, up sharply from **₹54,350 crore across 45 issues in 2023** and
**75% above the prior 2020 record of ₹80,816 crore**; **FY2024–25 QIP fundraising reached ₹1.33
lakh crore**, itself a record. **Real estate dominated 2024's QIP activity, raising ₹22,320 crore**,
led by **Godrej Properties (₹6,000 crore, December 2024) and Prestige Estate Projects (₹5,000
crore)**. **[Verified, all figures.]** Alongside fresh-capital issuance, **promoter and private-
equity selling through block/bulk deals and OFS reached record scale for three consecutive years**:
**calendar-2024: ₹1.43 lakh crore**, then **calendar-2025: over ₹1.5 lakh crore** (of which roughly
**₹1.35 lakh crore ran through block/bulk deals and a further ₹18,000 crore through IPO/OFS
routes**) — the first time promoter selling has crossed the ₹1 lakh crore threshold three years
running. **[Verified.]** Notable single exits across the window include Baring PE's ~₹7,400 crore
Coforge stake sale (2023) and a May-2024 cluster (Star Health ₹2,211 crore, Cipla-promoter ₹2,725
crore, IRB Infrastructure ₹1,445 crore, Timken India ₹1,253 crore, Aptus Value Housing Finance
₹1,347 crore, Apollo Tyres ₹1,073 crore, RR Kabel ₹950 crore); **private promoter ownership of
NSE-listed companies fell to 40.58% by June 2025, an eight-year low.** **[Verified.]** This
promoter/PE-OFS dimension is precisely the third-leg candidate `partCDEFH.md` Part F already
registers as **IS-D3** — a design proposal, classification work only at this stage, not yet folded
into `L7`'s own two-leg state.

**Where the wave stands, 2025–26.** Calendar-2025's own record (₹1.95 lakh crore, 373 issues) has
not carried cleanly into 2026: **companies raised roughly US$5.78 billion through public offerings
in the first stretch of 2026, against US$7.32 billion over the same window a year earlier**, and
several closely watched candidates — Manipal Health Enterprises, Indo-MIM, and Juniper Green Energy
among them — **cut the size of their planned offerings**, while Zepto opted for a pre-IPO
placement instead of a public issue, Sify Infinit Spaces paused its offering, and PhonePe deferred
its own listing plans. **[Verified.]** This softening arrives inside a genuinely weaker secondary-
market backdrop: the **Sensex's own intraday all-time high, 85,978, was set 27 September 2024**,
and by **early September 2026 it stood near 76,944** — a decline on the order of **10–13%** from
that peak (touching a sharper ~14.5% drawdown intraday in mid-2026); the **Nifty 50's own all-time
high, 26,373, was set 5 January 2026**, and by the same date in September 2026 it had fallen to
roughly **23,100–23,200, a 12–13% decline**. **[Verified, both index peaks and the approximate
current levels; FII outflows, decelerating corporate-earnings growth off FY21–FY24's 15–20% pace,
and elevated crude/geopolitical risk are the commonly cited drivers, cross-referenced to
`globalcycle-deep`'s own May-2026 episode and `fpi-deep`'s own CY2026 flow record, not re-derived
here.]** Despite this, investment-bank forecasters (Kotak Mahindra Capital, Goldman Sachs) still
project **2026 as a potential record year — as much as US$25 billion, from 190-plus issues,
exceeding ₹2.5 lakh crore** — a genuinely open, two-sided read this Part states rather than
resolves, consistent with this program's own "states, never dates" discipline.

**What L7's two-leg state would have read.** Both legs run hot simultaneously through 2023–25 —
record mainboard and QIP volumes (Leg 1) and, distinctively, an SME sub-market running an
essentially unprecedented Leg-2 extreme (>90% premium-listing rate, four-digit oversubscription
multiples) that the mainboard/SME separation in `partCDEFH.md`'s own Part C construction is
precisely designed to surface without letting a handful of SME outliers distort the primary
mainboard state. SEBI's own December 2024 intervention is the clearest instance in this entire
record of the regulatory-action annotation (Part E Step 4) firing in close to real time on the same
signal this Part's own oversubscription statistics independently confirm — the closest this record
comes to a regulator's own real-time read matching the seat's own construction almost exactly.
Whether the 2024–25 volume-and-pop extreme was, in fact, followed by the kind of weak 12–24-month
forward secondary-market return Baker-Wurgler's own mechanism predicts is precisely what §B3(c)
below frames as this record's own live, still-resolving validation test.

---

## B3. Synthesis

### (a) The wave table

| Wave | Peak-year volume (₹, mainboard unless noted) | Reception peak | What followed (12–24m secondary-market return) | Regulatory response | L7 two-leg read |
|---|---|---|---|---|---|
| **1992–96 free-pricing boom** | FY1994–95: ~1,400 issues (exact ₹ total not pinned `[VERIFY]`); 1996–97: 882 issues, ₹14,275.98cr | Feb 1995: 78 IPOs in one week; premium-issue share 1.37%→45.90% (1991–92→1994–95) | 1997–98: 111 issues, ₹4,569.95cr (−87.4% issues, −68.0% amount, single year); GNPA 19.05%→12.16% (1997→2001), BIFR backlog cleared for another 15y | Vanishing-companies enforcement (partial, slow); CDR mechanism born 2001 | No usable percentile (pre-NSDL); qualitative both-legs-hot per `partCDEFH.md` Part H |
| **1999–2000 tech mini-wave** | FY1999–2000: 151 issues, ~₹7,817cr | Sector-concentrated tech/software mania, Nasdaq-linked | FY2000–01: ₹6,108cr (issuance already fading); 2001: Sensex ~−38% (Ketan Parekh + Nasdaq bust) — but FII flows stayed net positive through it (`fpi-deep` §B1) | Ketan Parekh secondary-market inquiry; no dedicated issuance-side reform found `[VERIFY]` | Leg 1 moderate (denominator-damped by rally-inflated mcap); Leg 2 plausibly hotter — genuinely unresolved, per-issue data not reconstructed |
| **2004–08 great wave** | 2006: 78 IPOs, $7.23bn; 2007: ~93–103 IPOs `[VERIFY]`; ONGC (2004) ₹10,694.5cr; DLF (2007) ₹9,187.5cr; Reliance Power (Jan 2008) ₹11,700cr | ONGC 6.82×; Reliance Power 73×; ~46.55% avg first-day underpricing (2002–06 study) `[VERIFY scope]` | Reliance Power −17%→−intraday low ₹355→closed ₹372.50 day one; 2008: 37–38 IPOs, $3.8bn (from 103/79 prior years); FY08–09: ₹2,034cr/21 issues; Nifty −60–65% (Jan–Oct 2008) | IPO demat-scam enforcement 2005–06 (82 financiers, 24 operators, 12 DPs barred/penalized) | Both legs hot simultaneously — the record's cleanest froth flag (`partCDEFH.md` Part H: 2007–08 named explicitly) |
| **2010–11 PSU/QIP echo** | 2010: 64 IPOs, ₹37,535cr (record); Coal India ₹15,199.4cr; RE-sector QIP ₹23,914cr (2010, up from ₹14,224cr 2009) | Coal India 15.28× | 2011 (9m): 38 issues/₹6,004cr vs 50/₹16,709cr prior year (−64%); 28 IPOs withdrawn; 26/39 issues missed min. QIB subscription; cohort lost ~1/3 of issue value by year-end | None issuance-specific found `[VERIFY]` | Leg 1 flagged froth; Leg 2 (median, not flagship) likely overstated by Coal India alone — state-supply-driven, not demand-driven, per §B2 case 4 |
| **2014–18 institutional wave** | 2017: 36 mainboard IPOs, ₹67,147–68,826cr (record, surpassing 2010); HDFC Life ₹8,695cr; HDFC AMC ₹2,800.33cr | 17/36 issues >10× sub; 18/36 >10% listing pop | IL&FS default 14 Sep 2018 → SC1's 12m SMB −24.8%/mkt −20.2% (`shadow-deep`); ₹600bn approved-but-frozen pipeline (Dec 2018); ~₹16,500cr of approvals lapsed unused (Aug 2019); CY2019: 62 issues, $2.53bn (−62% volume, −54% proceeds) | SEBI chairman's public lament (Dec 2018); resolution ran through credit-side machinery (`shadow-deep` §B2), not issuance-specific reform | Broad both-legs-hot through 2017, then external-shock collapse of both legs together — a different failure mode (credit shock, not self-correcting sentiment) |
| **2020–22 startup wave** | 2021 record calendar (aggregate `[VERIFY exact]`); Zomato (Jul21) subscribed 38.25×; Nykaa (Nov21) ₹5,300cr, 81.78×; Paytm (Nov21) ₹18,300cr (era's largest); LIC (May22) ₹21,008.5cr | Zomato +52%→ open; Nykaa +80% open; Paytm Day-1 sub only ~18% `[VERIFY final]`; LIC ~3× overall | Paytm: −27% listing day (record fall, ~₹38,000cr wealth wiped day one), −78% at 12m (Nov22); LIC: −7.8% listing day, −24% by 9 Jun 2022 | No issuance-specific SEBI action found for this wave `[VERIFY]` | Leg 1 record on Paytm's mega-issue landing exactly as Leg 2 cracked — the clean decoupling case; `partCDEFH.md` names 2021 a top-tick instance |
| **2023–26 SME frenzy/broadening** | FY24: 76 IPOs, ₹61,915cr; FY25: 79–80 IPOs, ₹1.62L cr (~2.6× FY24); CY2025: 373 issues (103 mainboard/270 SME), ₹1.95L cr (record); QIP CY2024: ~₹1.37–1.41L cr (record, +75% vs 2020's ₹80,816cr) | SME: >90% listed at premium; HOAC Foods ~1,963× sub; 214/236 SME debuts positive | Sensex ATH 85,978 (27 Sep 2024) → ~76,944 (Sep 2026), ~10–13% off peak; Nifty ATH 26,373 (5 Jan 2026) → ~23,100–23,200 (Sep 2026), ~12–13% off peak; 2026 issuance pace softening ($5.78bn vs $7.32bn YoY, several deals cut/deferred) | SEBI SME-IPO curbs, 18 Dec 2024 (EBITDA test, ₹2L min. retail ticket, 20% OFS cap, 15%/₹10cr GCP cap, monitoring agency); promoter/PE OFS record ₹1.43L cr (2024) then >₹1.5L cr (2025), 3rd straight year >₹1L cr | Both legs hot, SME extreme on Leg 2 specifically; SEBI action = regulator-read confirmation in near-real-time; IS-D3 (OFS third leg) registered as a design candidate, not yet live |

### (b) The Baker-Wurgler scorecard for India, qualitative, wave by wave

Read across all seven waves, the record supports the mechanism with real force but not without
genuine exceptions this Part states honestly rather than smoothing over. **Four waves show the
clean Baker-Wurgler signature — heavy issuance (both legs hot) followed, within 12–24 months, by
materially weak secondary-market returns**: **1994–96** (record volume and reception → the 1997–98
primary-market collapse and a multi-year real-economy overhang); **2004–08**, with **Reliance
Power's January 2008 top-tick** the single cleanest individual-deal instance in the entire record
(a 73×-oversubscribed IPO closing lower on day one, five weeks before the broader index's own
collapse); **2020–22**, with **Paytm's November 2021 listing** the cleanest instance of the two legs
*decoupling* right at the top rather than confirming each other; and **2023–26**, whose own
12–24-month forward window is still resolving as of this writing but whose index-level backdrop —
the Sensex's own 27 September 2024 all-time high arriving inside the same window as record FY24/
FY25 issuance, followed by a 10–14% drawdown into 2026 — is, on the record available today,
directionally consistent with the same pattern. **Two waves show a genuinely different, and
instructive, failure mode**: **2010–11**, where Leg 1 (state-engineered PSU disinvestment supply)
ran hot while Leg 2's *median* reception plausibly did not confirm as strongly as the Coal India
flagship implied — a case for reading the legs separately, not for the mechanism failing outright;
and **2014–18**, where the primary market's own collapse was **triggered externally** by a credit
shock (IL&FS) rather than by the issuance wave correcting its own excess — the two-leg state read
correctly (broad hot reception through 2017, broad cold reception from late 2018) but for a reason
the seat's own construction was never built to attribute. **One wave (1999–2000) remains genuinely
unresolved** on the evidence this pass could independently verify: issuance volume itself faded
ahead of the 2001 crash (consistent with issuers selling into strength before it ended), but a
clean per-issue reception dataset to confirm or reject a genuine both-legs-hot reading was not
reconstructable this pass. The desk's own honest summary: **India's issuance record supports Baker-
Wurgler's mechanism in the majority, and in the clearest, cases — but at least two waves show the
mechanism can be confounded by a supply-side (state disinvestment) or an external (credit-shock)
driver that the two-leg construction alone cannot distinguish from genuine sentiment-driven excess**,
precisely the honest caveat `research/CONTRACT.md` §5's own survival-argument discipline requires
this Part to carry forward rather than paper over.

### (c) The two validation episodes for the data-gated IS test

`config/ladder.yaml`'s own `changes_if` clause for `L7` names exactly two episodes as the
pre-registered validation set — **"India pre-registered test vs 2018/2023-24 episodes"** — and
`partCDEFH.md` Part F already registers the design as **IS2**, "the 2018/2023-24 episode shape
check — the ladder's own `changes_if`," alongside the more general **IS1** Baker-Wurgler India test.
Neither has been run: per `research/CONTRACT.md` §12, this research phase permits no backtests, no
data acquisition, and no model code — what follows is the pre-registration this Part's own case
record is positioned to support, stated before any data is pulled, not a result.

**2018 — the credit-shock confound, stated as the test's own null-hypothesis stress case.** §B2
case 5's own record shows the two-leg state reading *correctly* cold through late 2018 and all of
2019, but for a reason (an external NBFC funding-run) the seat's own construction does not itself
observe. **IS2's own design question for this episode**: does a *pre*-2018 two-leg reading (the
2017 broad-hot state, independently confirmed on both legs above) show genuine predictive lead
before the IL&FS trigger, or does the state only turn cold *after* the freeze is already visible in
the issuance calendar itself — i.e., is `L7` a leading regime indicator here, or a coincident one
riding on the same credit-shock transmission `shadow-deep/shadow-RESULTS.md`'s own SC1 trial
already shows arrives with a roughly 12-month lag into equity factors generally? A pre-registered
test that finds `L7` merely coincident with, rather than leading, the 2018 freeze would not
falsify the seat's Tier-B status (the Baker-Wurgler mechanism's own global evidence stands
independently) but would argue for a narrower interpretation of what the India-specific coefficient
can honestly claim to add.

**2023–24 — the live, still-resolving case, stated as the test's own cleanest currently-available
instance.** §B2 case 7's own record shows both legs running hot through FY24–FY25 with no
comparable external-shock confound yet identified — the closest this record comes to an
uncontaminated Baker-Wurgler instance since 2007–08. The Sensex's own all-time closing high (27
September 2024) arrived inside the same calendar window as the FY24/FY25 record issuance pace and
the SME frenzy's own extreme Leg-2 readings; the index's subsequent 10–14% drawdown into
2026 — alongside the demonstrated early-2026 softening in fresh issuance pace itself (§B2 case 7's
own final paragraph) — is, on the evidence available as of this writing, directionally consistent
with the mechanism, but the 24-month window from the FY24/FY25 issuance peak has not yet fully
elapsed as of September 2026, and this Part deliberately declines to call the episode's own
forward-return outcome settled ahead of that window closing, consistent with this program's
"states, never dates" discipline (echoed identically by `globalcycle-deep` and `fpi-deep` for their
own live 2025–26 episodes). **IS2's own design question for this episode**: once the full
24-month window has elapsed, does the magnitude of the 2024–2026 drawdown scale with the
independently-measured two-leg extremity of the FY24/FY25 issuance peak (a genuine dose-response
test), or is the drawdown better explained by the FII-outflow and earnings-deceleration drivers
this Part cross-references to `globalcycle-deep` and `fpi-deep` without re-deriving — i.e., does
`L7` add explanatory power *on top of* the ladder's own macro/flow blocks, or is it substantially
redundant with signals the `valuation_sentiment` block already shares budget with via `L8`? Both
questions are exactly what a purged, out-of-sample IS2 trial — run only once India-specific bhavcopy
and SEBI-bulletin data are pulled per `partCDEFH.md`'s own runsheet addendum 15 — is built to
answer; this Part's own contribution is the qualitative case record, era by era, that trial will be
tested against, not a substitute for running it.

---

## References

Baker, M. & Wurgler, J. (2000). "The Equity Share in New Issues and Aggregate Stock Returns."
*Journal of Finance* 55(5): 2219–2257. · Baker, M. & Wurgler, J. (2002). "Market Timing and Capital
Structure." *Journal of Finance* 57(1): 1–32. · SEBI Annual Report 1997–98 (the 1996–97/1997–98
issuance-collapse table); SEBI board decisions, 18 December 2024 (SME-IPO rule tightening). ·
Business Standard, BusinessToday, Moneylife, TechCrunch, and other contemporaneous financial-press
reporting for every dated issuance, subscription, listing, and index figure throughout, per the
`[VERIFY]` discipline stated at each figure's first use. · `research/cycles/capex-deep/
partB-cases.md` (case 1's 1994–97 primary-market chronology, GNPA/BIFR data, and case 2's Reliance
Power "top-tick artifact" framing — cross-referenced throughout, never re-derived here). ·
`research/cycles/fpi-deep/partB-cases.md` (the October 2007 P-note FLOW episode, the 2000–01/
2001–02 flow-vs-return divergence, and the 2013 single-pool-blind-spot motif this Part's own §B2
case 5 borrows) and `research/cycles/globalcycle-deep/partB-cases.md` (the May-2026 episode
anatomy) — both cross-referenced, not re-derived. · `research/cycles/shadow-deep/partB-cases.md`
and `shadow-deep/shadow-RESULTS.md` (the IL&FS funding-run anatomy and the SC1 12-month
factor-propagation trial). · `research/cycles/issuance-deep/partCDEFH.md` (the seat's own Parts
C–H: the two-leg `state_t` construction, the IS1/IS2/IS-D3 test designs, and the SME/mainboard
split — the machinery this Part's case record is written to be tested against). ·
`docs/CYCLE_ATLAS.md` row 3.2 and `config/ladder.yaml`'s `L7_issuance_sentiment` entry. ·
`research/CONTRACT.md` §4 (evidence tiers), §5 (the signal-survival test), and §12 (research-phase
rules: no backtests, no data acquisition).

---

*Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · 2026-09-02 ·
v1.0*

---

# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 3.2; seat L7, Tier B)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Cadence / notes |
|---|---|---|
| Issue calendar + sizes (mainboard/SME/QIP/OFS/rights) | NSE/BSE public issue pages; SEBI monthly bulletins; prime-database-style aggregates are PAID — the free build is exchange-first | per-issue; monthly aggregation |
| Subscription books (QIB/HNI/retail) | exchange live-bid archives + red-herring outcomes | per-issue; the free RECEPTION variable |
| First-day pops | bhavcopy (listing-day open/close vs issue price) — the existing puller family | per-issue |
| Market cap denominator | index factsheets/bhavcopy aggregates | monthly |
| SEBI actions (the institutional thermometer) | SEBI orders/circulars | event registry entries |

PIT hazards: SME-board survivorship (delisted/migrated issues retained); issue-price
restatements (anchor allotments vs final); the mainboard/SME split kept as SEPARATE series
(microstructure differs — the psychology chapter's SME caution is structural here); calendar
lag between filing, open, and listing (state timestamps on LISTING date, declared).
Runsheet addendum 15 (steps 78-81): 78 exchange issue-calendar scraper (mainboard+SME,
2000s→) ~5-6h; 79 subscription-book backfill ~3-4h; 80 listing-day pop assembly from bhavcopy
~2-3h; 81 IS1/IS2 acceptance fill + first India two-leg state (two-pass) ~2-3h.

## Part D — The mathematics

state_t = availability-weighted mean of {pct(volume/mcap), pct(median pop)} with n_legs
(no-listing months degrade to the volume leg — tested). Why the persistent-incentive argument
changes the decay prior: most seats assume alpha decays (Contract); L7's edge is an incentive
equilibrium — issuers CANNOT be arbitraged out of timing their own sales — so the desk's
haircut applies to the MAGNITUDE, not the existence, of the effect (the ladder's Tier-B
confidence with the Schultz pseudo-timing critique carried as the honest counter). The froth
signature needs BOTH legs high (volume alone = capital formation; pops alone = scarcity);
the flag threshold sits on the registered grid. Consumption is reduce-only twice over:
valuation_sentiment block confirm (with L8's spread — expensive market + hot primary = the
double-confirm) and the special-sits sleeve sizing (froth => shrink).

## Part E — The algorithm (L7, monthly)

```
STEP 1  monthly aggregation: issuance value / mcap; median listing pop; subscription medians
        (mainboard and SME as SEPARATE series; the state reads mainboard, SME is a satellite
        briefing line — the 2023-25 frenzy showed why)
STEP 2  expanding percentiles (shared grids) -> two-leg state + n_legs
STEP 3  consumption: valuation_sentiment block (0.10, with L8); special-sits sleeve sizing
        rule (froth_flag => shrink per the registered schedule); NO short-signal path exists
STEP 4  SEBI-action registry entries annotate the state (a regulator acting IS a reading)
MONITOR quarterly re-aggregation; the SME/mainboard divergence watch; IS1/IS2 at data-landing
FAILURE MODES: SME microstructure polluting the pop leg (separated by design); QIP/OFS
        classification drift; the wave arriving through NEW vehicles (REIT/InvIT waves —
        the calendar scraper's category audit is annual)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| valuation_sentiment block | the froth state (with L8 — the double-confirm) |
| Special-sits sleeve | the sizing rule (froth => shrink) per L7's role line |
| Stage-2 briefings | the SME satellite line + the SEBI-action annotations |
| Cycle School | Lesson 29: the signal that shouldn't decay, and why |

Designs: **IS1** (registered, prior stated) the Baker-Wurgler India test; **IS2** (registered)
the 2018/2023-24 episode shape check — the ladder's own changes_if; **IS-D3** promoter/PE OFS
selling as a third leg candidate (design only; classification work first).

## Part H — Knowledge ledger (atlas 3.2)

**Established (fixture-verified machinery + record):** the two-leg state separates planted
froth from winter (0.9 vs 0.2) and degrades honestly through no-listing months; the module
exposes no short-signal path. **Established (record, cases chapter):** India's issuance waves
top-tick markets with regularity (1994-96, 2007-08, 2021, 2024) and regulators confirm froth
institutionally (SEBI 2024 — the ladder's own citation). **Awaits India data [B]:** IS1/IS2 —
the seat's numbers; the primary-market vault is runsheet addendum 15. **Unknowable:** which
VEHICLE carries the next wave (the category-audit exists because the fragile node moves here
too). **Tier note:** L7 stays Tier B on the strength of the incentive argument + the global
evidence; the India-specific coefficients wait for their test, as the ladder's changes_if
already says.
