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
