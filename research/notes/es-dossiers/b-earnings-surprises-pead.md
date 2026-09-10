# Earnings Surprises and Post-Earnings-Announcement Drift — Literature Dossier

Knowledge synthesis (no web egress this session). Every literature claim is tagged **[LIT]**;
where I recall the substance but not the exact citation/venue/number with confidence, it carries
**[VERIFY: …]** naming what to check, per this program's citation-integrity convention. No number
here is a desk result — nothing was read out of `research/register/`, and none of the FUN-track
earnings-*cycle* prints (aggregate/index-level, already booked in the trial ledger) are quoted or
conflated with the firm-level *surprise* question addressed here — recession depth and
price-leads-earnings answer a different question than whether one stock's beat/miss predicts its
own subsequent return.

## 1. Foundations

**Ball & Brown (1968)**, "An Empirical Evaluation of Accounting Income Numbers," *Journal of
Accounting Research* 6(2) **[LIT]**, is the origin point of the entire literature and arguably of
empirical capital-markets accounting research itself. Their finding was narrower than PEAD as
later understood: firms whose annual income exceeded a naive expectation earned positive
abnormal returns *in the announcement month*, and firms that missed earned negative abnormal
returns — i.e., the market does price earnings news. The anomaly is what they found *afterward*:
roughly half of the full-year abnormal return associated with the eventual earnings outcome had
already accrued by the announcement month, but a residual continued to drift in the same
direction for months after, which is inconsistent with instant full-information pricing **[LIT]**.
This residual drift is what the later literature isolated, sized, and named.

**Bernard & Thomas (1989)**, "Post-Earnings-Announcement Drift: Delayed Price Response or Risk
Premium?," *Journal of Accounting Research* 27 (Supplement) **[LIT]**, is the paper that gave the
anomaly its name and its modern measurement. Sorting firms into deciles on standardized
unexpected earnings (SUE), they documented a hedge return (top SUE decile minus bottom) of
roughly **4–9% cumulative abnormal return over the ~60 trading days following the earnings
announcement** **[LIT, magnitude recalled as a range across BT89 and the closely related Foster–
Olsen–Shevlin estimates — VERIFY: exact BT89 point figure]**, essentially monotonic across
deciles (not just an extreme-decile effect), and — critically for their risk-premium test — not
explained by conventional risk adjustments (market beta, size). They interpreted this as market
underreaction rather than compensation for risk, though they framed the paper even-handedly as a
test between the two hypotheses.

**Bernard & Thomas (1990)**, "Evidence That Stock Prices Do Not Fully Reflect the Implications of
Current Earnings for Future Earnings," *Journal of Accounting and Economics* 13(4) **[LIT]**, gave
the mechanism. Quarterly earnings changes (seasonally differenced, i.e. Q_t minus Q_{t-4}) follow
an approximately autoregressive process with **positive autocorrelation at lags 1–3 quarters and
negative autocorrelation at lag 4** **[LIT]** — a well-documented time-series regularity in
quarterly earnings dating to Foster's and Griffin's earlier work on earnings time series
**[VERIFY: precise prior citations — Foster (1977), Griffin (1977), Watts (1975) are the usual
references for the quarterly-earnings ARIMA structure]**. Bernard & Thomas showed that investors
price current news as if this autocorrelation structure did *not* exist — they underreact to the
implication that a positive surprise this quarter forecasts further positive surprises next
quarter — and that returns around the *next three* quarterly announcements systematically
confirm or disconfirm the drift's direction. This is the single most important mechanism claim in
the literature: PEAD is not a diffuse three-month mispricing, it is a bet on predictable future
surprises that resolves in discrete lumps at future announcement dates.

**SUE construction.** Three variants recur:
- **Seasonal random walk (SRW)**: SUE = (E_q − E_{q−4}) / σ, where σ is the standard deviation of
  that same seasonal difference over the trailing ~8 quarters. This is the Foster–Olsen–Shevlin
  standardization and remains the default when analyst forecasts are unavailable **[LIT]**.
- **Analyst-based**: SUE = (actual EPS − consensus forecast) / price (or / forecast dispersion).
  Preferred where coverage is dense because it strips out earnings changes the market already
  anticipated, but it inherits I/B/E/S-style coverage gaps for smaller names **[LIT]**.
- **Standardization denominator** choices (σ of the SRW series vs. price vs. forecast dispersion)
  materially change decile composition and are a documented source of cross-study inconsistency
  **[LIT]**.

**Foster, Olsen & Shevlin (1984)**, "Earnings Releases, Anomalies, and the Behavior of Security
Returns," *The Accounting Review* 59(4) **[LIT]**, is the paper that popularized the SUE metric
and the decile-portfolio approach, documenting the drift across roughly a decade of US data at a
magnitude broadly consistent with the later Bernard–Thomas estimates. Contemporaneous work by
**Rendleman, Jones & Latane (1982)**, *Journal of Financial Economics* **[VERIFY: exact
title/venue — recalled as an early SUE-decile risk-adjustment paper]**, made the same point
independently: risk adjustment does not kill the drift.

## 2. Magnitudes and Shape

The decile spread is not a smooth 60-day ramp; it is front-loaded onto information events. A
recurring stylized fact across the Bernard–Thomas lineage is that **a substantial share — commonly
characterized as on the order of 40–60% — of the cumulative 60-trading-day drift is earned inside
the narrow (3-day) windows around the subsequent quarterly announcements**, i.e., a handful of
event days out of sixty carry a disproportionate fraction of the total return **[LIT, approximate
consensus figure — VERIFY: exact % and which follow-on paper isolates it most cleanly]**. This
matters enormously for implementation: a strategy that only holds through calendar time captures
some grind-return between events, but a strategy that can *time* the next announcement captures
much more per unit of holding risk.

**Small-vs-large gradient.** **Bhushan (1994)**, "An Informational Efficiency Perspective on the
Post-Earnings Announcement Drift," *Journal of Accounting and Economics* 18(1) **[LIT]**, showed
the drift is concentrated in stocks with low analyst following and low institutional ownership —
proxies for information-processing frictions and, empirically, for small-cap/illiquid names. This
single result is the pivot for nearly everything that follows in the decay literature: PEAD looks
like a liquidity/attention story, not a pure risk-premium story, because it dies exactly where
attention and arbitrage capital are richest.

**The Frazzini–Lamont earnings-announcement premium** is a related but analytically distinct
effect and should not be merged with PEAD. **Frazzini & Lamont**, "The Earnings Announcement
Premium and Trading Volume" **[VERIFY: exact venue/year — recalled as an NBER working paper
c. 2006–07, possibly not formally journal-published under that exact title]**, document that
stocks earn abnormally high (unconditional) returns in the days around *any* scheduled earnings
announcement, **regardless of surprise direction or sign** — an ex-ante compensation-for-risk (or
attention/liquidity) story tied to the announcement date itself, layered on top of, and separable
from, the surprise-conditional PEAD return. A monthly-rebalance desk should keep these two effects
analytically separate: PEAD requires knowing the *sign and magnitude* of the surprise; the
announcement premium requires only knowing the *date*.

## 3. Decay

PEAD is one of the most replicated anomalies in existence, which also makes it one of the most
scrutinized for arbitrage-driven decay — precisely the McLean & Pontiff (2016) mechanism this
program's governing principle (CONTRACT §5) already invokes generally. The PEAD-specific evidence:

**Sadka (2006)**, "Momentum and Post-Earnings-Announcement-Drift Anomalies: The Role of Liquidity
Risk," *Journal of Financial Economics* **[LIT, moderate-high confidence]**, showed that a
meaningful share of PEAD (and momentum) returns compensate for exposure to *variable* (as opposed
to level) liquidity risk — the anomaly partly survives risk-adjustment because it loads on a
priced but hard-to-hedge risk factor, which is itself a partial "why does this survive" argument
in the CONTRACT §5 sense (institutional-constraint / capacity-limit flavor).

**Chordia, Goyal, Sadka, Sadka & Bommaraju (2009)**, "Liquidity and the Post-Earnings-Announcement
Drift," *Financial Analysts Journal* 65(4) **[LIT, moderate confidence on exact author list/venue
— VERIFY]**, is the canonical "does it survive costs and does it survive time" paper for this
brief. Their finding, echoed by the broader Chordia–Subrahmanyam research program on anomaly
attenuation, is two-pronged: (i) PEAD is overwhelmingly concentrated in illiquid stocks, and a
large fraction of the *unadjusted* decile-spread return is consumed by realistic trading costs
once sized to any meaningful capital base; (ii) in the **post-2000 period**, and especially inside
the largest, most liquid names, the drift has **attenuated sharply relative to the 1970s–1990s
estimates** — consistent with faster institutional processing of earnings news, decimalization,
and the general arbitrage-capital-arrives mechanism this program already treats as a prior
(CONTRACT §5, Chordia–Subrahmanyam–Tong). The honest summary is not "PEAD is dead" but "PEAD has
migrated to where trading is hardest": small caps, low-coverage names, and non-US/emerging
markets, where analyst following is thinner and arbitrage capital has weaker incentive to compete
away a small-name anomaly at scale.

**Transaction-cost verdicts, Korajczyk–Sadka style.** **Korajczyk & Sadka (2004)**, "Are Momentum
Profits Robust to Trading Costs?," *Journal of Finance* 59(3) **[LIT]**, is not a PEAD paper but
supplies the template this brief borrows: model price impact as increasing in trade size relative
to average daily volume, and solve for the capital scale at which strategy returns net to zero.
Applied (by the Chordia et al. lineage and others) to SUE-sorted portfolios, the qualitative
verdict is that PEAD-based strategies are implementable, but at **modest capacity** relative to
their headline gross returns, because the return and the illiquidity that protects it from full
arbitrage are the same variable — you are paid partly *because* the position is hard to build and
unwind at size **[LIT, directional; I do not have confident specific breakeven-AUM figures from
memory and flag any such number as VERIFY rather than state one]**. For a desk of this program's
size (₹100–25,000 cr across three books), the implication is capacity-band-dependent: the
Aggressive book's tail (ranks 500–750) is exactly the segment where gross PEAD is largest and
costs bite hardest simultaneously — the same tension the program's turnover-cost work (CONTRACT
§7 item 6) already treats as a first-order design constraint.

**Non-US evidence.** International replications generally find PEAD present and often *larger* in
markets with lower analyst coverage, weaker institutional-arbitrage capacity, and less algorithmic
participation — Bhushan's (1994) cross-sectional logic applied across countries rather than
across firms within one **[LIT, directional; point magnitudes vary widely by study/sample and are
not carried with confidence — see §5 for India]**.

## 4. Fundamental Momentum Without Announcement Dates

A separate branch asks whether the underreaction-to-earnings-news mechanism can be harvested
*without* timing individual announcement windows at all — directly relevant to a desk that
rebalances monthly rather than event-by-event.

**Novy-Marx (2015)**, "Fundamentally, Momentum is Fundamental Momentum," NBER Working Paper
**[LIT, moderate-high confidence on substance, VERIFY exact WP number/year]**, sorts stocks each
month on recent earnings performance/earnings innovations (rather than on 12-month-minus-1-month
price return) and shows that this "fundamental momentum" captures much of conventional price
momentum's premium, correlates highly with it, and — his central point — is at least as robust,
without requiring any knowledge of when the next earnings announcement falls. The practical
argument for this desk is direct: a monthly-cadence sort on trailing earnings surprise/earnings
change avoids the event-window-timing problem entirely, trading the *concentration* of the
Bernard–Thomas per-event return (§2) for *implementability* on a fixed calendar.

**Chan, Jegadeesh & Lakonishok (1996)**, "Momentum Strategies," *Journal of Finance* 51(5)
**[LIT]**, is the decomposition this framing rests on. They show price momentum profits are
partly, but not fully, explained by underreaction to earnings-related news (SUE, analyst
revisions): combining a price-momentum sort with an earnings-surprise/revision sort produces
stronger returns than either alone, implying the two signals share a common underreaction
component but also each carry independent information — price momentum is not merely earnings
momentum in disguise, and vice versa **[LIT]**. This is the correct lens for a desk whose
"moderate book's engine is the factor book, not momentum" (CONTRACT §7 item 10): an
earnings-surprise sleeve is a *complement* to, not a substitute for, whatever price-momentum
exposure already exists in the design, and the CJL decomposition is the citation for why they are
not redundant.

**Revenue surprises.** **Jegadeesh & Livnat (2006)**, "Revenue Surprises and Stock Returns,"
*Journal of Accounting and Economics* 41(1–2) **[LIT]**, show that standardized revenue surprises
predict returns with power incremental to earnings surprises, and that the *interaction* matters:
firms beating on both earnings and revenue drift more than firms beating on earnings alone (which
can reflect margin expansion or one-off items rather than genuine demand strength), and firms
missing on both drift down more than an earnings-miss-only firm. The "why does this survive"
argument (CONTRACT §5) is cleaner for revenue than for EPS: revenue is materially harder to manage
via accounting discretion than bottom-line EPS, so a revenue-confirmed earnings surprise plausibly
carries less noise from earnings management and could decay more slowly — a testable, not merely
asserted, distinction.

## 5. India

The India-specific PEAD literature is real but thinner, more scattered across regional and
working-paper venues, and — being honest about study quality as instructed — considerably less
rigorously cross-validated than the US canon above. I can recall the shape of this literature with
moderate confidence but not pin every citation precisely; flagging accordingly rather than
inventing precision.

The broader Indian market-anomaly program that PEAD studies sit inside is anchored by **Sehgal &
Balakrishnan (2002)**, "Contrarian and Momentum Strategies in the Indian Capital Market,"
*Decision* (IIM Calcutta) **[LIT, moderate-good confidence]**, and related work by Sanjay Sehgal
and co-authors on momentum, size, and value effects in Indian equities through the 2000s–2010s.
This establishes the necessary precondition for PEAD to be plausible in India — general
underreaction-type return continuation is documented in the same market — without itself being a
PEAD study.

On PEAD specifically, I recall the existence of a small number of Indian studies (published
mainly in Indian and regional finance journals — e.g. outlets in the *Journal of Emerging Market
Finance* / IIM working-paper-series family) testing SUE-decile or analyst-surprise sorts on
NSE/BSE data and finding a drift qualitatively consistent with Bernard–Thomas: positive-surprise
deciles outperforming negative-surprise deciles over multi-month windows following results
**[VERIFY: I cannot confidently name a specific author/title/year for a dedicated India PEAD paper
without web search — this is a recalled pattern across the Indian anomaly literature, not a
citation I would sign off as verified]**. Where I have somewhat more confidence is in the general
finding *pattern* reported across this literature, which is worth relaying with appropriate
skepticism about underlying study quality:

- **Effect direction and rough magnitude**: reported drift is directionally consistent with the
  US literature and, where compared, often *larger* in raw magnitude — plausible given India's
  thinner analyst coverage outside the NIFTY 100–200 and higher retail participation, both of
  which are the same Bhushan (1994) mechanism that predicts a bigger effect where information
  processing is slower **[LIT, directional pattern; magnitude uncertain — VERIFY per-study]**.
- **Study-quality concerns recurring across this literature** (stated plainly, per instruction):
  short sample windows (often one decade of post-2000/2010 NSE data, short of the CONTRACT §4
  Tier-A bar of ≥30 independent observations once quarters are treated as overlapping); inconsistent
  SUE construction (SRW vs. a sparse analyst proxy, rarely reconciled in the same paper); little or
  no explicit handling of the exact announcement-timestamp problem (§6) — many appear to anchor on
  the *quarter label* rather than the *filing date*, blurring the event window by up to 45–60 days;
  and survivorship (current constituents tested, not a point-in-time universe), a concern the
  program's known-priors already flag for Indian fundamentals generally (CONTRACT §7 item 7). None
  of this means the India finding is wrong — underreaction is, if anything, a more plausible prior
  in a less-covered market — but the literature is a **directional Tier-B prior at best** (CONTRACT
  §4), not a calibrated magnitude, until this desk runs its own point-in-time test.

**The 45-day filing deadline and the event-window problem.** Under SEBI's Listing Obligations and
Disclosure Requirements (Regulation 33), listed companies must file quarterly financial results
within **45 days of quarter-end** for Q1–Q3, and audited annual results (in lieu of a standalone
Q4) within **60 days of financial-year-end**. This is a regulatory fact, not a literature estimate.
Its consequence for event-study design is structural: unlike the US, where nearly all S&P 500
constituents report within a tight 2–3 week window each quarter, Indian results are spread across
up to a 45–60 day filing season, with large-caps (IT bellwethers such as TCS/Infosys typically
reporting first each season, a widely observed practitioner regularity that functions as an
early read-through for the sector) clustering early and the smaller, thinner-coverage tail —
precisely the segment where PEAD is largest per Bhushan (1994) — filing close to the deadline.
**Earnings-season clustering** in India therefore looks roughly like: Q1 (Apr–Jun) results
concentrated in **July–August**; Q2 (Jul–Sep) in **October–November**; Q3 (Oct–Dec), often the
tightest cluster, in **January–February**; Q4/FY in **April–May** under the 60-day allowance. For
a desk that rebalances monthly, this clustering means that at any given rebalance date, different
names in the universe are at very different "days since last announcement" — some just reported,
some are three weeks stale, some are approaching the next filing deadline — which is exactly the
state variable a PEAD-aware overlay needs to track explicitly rather than assume away by rebalance
calendar alone (see §6).

## 6. Edge Candidates for This Desk

Each candidate states mechanism, expected magnitude, horizon, decay risk, and data need. No
magnitude below is a desk number; all are literature figures carried forward with their [LIT]
hedges from §§1–4, restated here for sizing intuition only, to be re-derived from a point-in-time
India panel before any config parameter is set (CONTRACT §6).

**(a) SUE-decile fundamental-momentum overlay, monthly rebalance, no event-window dependency.**
Mechanism: underreaction to the autocorrelated component of quarterly earnings surprises
(Bernard & Thomas 1990); harvested via a Novy-Marx-style monthly sort on most-recently-known SUE,
never requiring the desk to trade around a specific announcement date. Expected magnitude: on the
order of the Bernard–Thomas decile spread, discounted because a monthly-calendar sort captures
only the grind component, not the concentrated per-announcement pop that (§2) carries 40–60% of
the 60-day drift **[LIT, qualitative discount — no specific number claimed]**. Horizon: refreshes
on the quarterly filing cadence, held between rebalances (matches CONTRACT §10's per-sleeve
cadence). Decay risk: highest of any candidate here — the most-published corner of the anomaly
literature (§3) — so it needs the CONTRACT §5 survival argument stated explicitly; the one
available is capacity/illiquidity (Chordia et al. 2009, Korajczyk–Sadka logic): it survives
*because* it lives in names too small for large arbitrage capital, which is also this desk's
Aggressive-book habitat (ranks 500–750). Data needed: quarterly filed EPS with an 8-quarter
seasonal-random-walk history — deliberately avoiding the analyst-based SUE variant, given India's
thin coverage below the top few hundred names.

**(b) Event-timed drift capture in the small/micro tail, sized to exact announcement dates.**
Mechanism: the classical Bernard–Thomas drift, harvested with the timing precision the literature
says matters most (§2's concentration finding). Expected magnitude: the full ~4–9%/60-day decile
spread is only accessible to a strategy that can act within days of the announcement — a
monthly-rebalance desk captures a fraction depending on how close its rebalance date falls to each
name's announcement, arguing for an event-time overlay rather than a pure calendar rebalance.
Horizon: 60–180 trading days per Bernard & Thomas, front-loaded around the next 1–3 prints. Decay
risk: precisely the segment (illiquid, low-coverage) the decay literature (§3) says survives
*best*, but also where this program's turnover-cost math (CONTRACT §7 item 6) bites hardest, so
net-of-cost sizing must be re-derived, not assumed. Data needed: exact NSE/BSE
corporate-announcement timestamps (already a planned RUNSHEET pull, `ingest/vault/calendars/`,
feeding H58-D2) joined to filed EPS, so each monthly rebalance can compute a firm-specific "days
since last announcement" state rather than treating all names as equally fresh.

**(c) Revenue-surprise interaction as a confirmation/tiebreak signal.** Mechanism: Jegadeesh–Livnat
incremental and interactive information in revenue surprises, layered on top of (a) or (b) as a
signal-quality filter — an earnings beat confirmed by a revenue beat is a cleaner underreaction
signal than an earnings beat alone. Expected magnitude: incremental to, not additive on top of,
whatever base SUE-sort return is booked — sized as a filter/weight, not a standalone sleeve.
Horizon: matches whichever base signal (a/b) it is attached to. Decay risk: plausibly *lower* than
plain EPS-based SUE, because revenue is harder to manage via accounting discretion than EPS — a
structural (CONTRACT §5, argument (i)) survival case worth testing explicitly rather than
assuming. Data needed: quarterly revenue (top-line) as filed — part of the same standardized
Schedule III P&L format all NSE/BSE-listed companies file, so no incremental data-source risk
beyond what (a)/(b) already require.

**Explicitly deprioritized**: the Frazzini–Lamont unconditional earnings-announcement premium
(§2) is a date-driven, not surprise-driven, effect on a horizon of days, not months — it is not
implementable at this desk's monthly cadence without adding a separate weekly/event overlay sleeve,
and should only be revisited if such a sleeve is ever built for other reasons.

## 7. Data Requirements — India

For a genuinely point-in-time PEAD test (echoing this program's known-priors #7 on restatement
bias and the two-pass vault-discipline requirement in CONTRACT §2), the exact fields needed:

- **Announcement timestamp**: date *and* time-of-day as stamped by the exchange on receipt (NSE/
  BSE corporate-announcements feeds carry this), classified before-market-open / during-market-
  hours / after-market-close, since this classification determines which trading session is
  event day t=0 (a before-open filing is same-day t=0; an after-close filing pushes t=0 to the
  next session) — get this wrong and the whole event window is systematically mistimed.
- **Filed EPS, as originally reported** (not the latest-vintage restated figure): standalone vs.
  consolidated flagged separately (Indian filings carry both; pick one convention and hold it
  fixed), basic vs. diluted flagged separately, and — critically — the **same-quarter-prior-year
  comparison figure as it was reported at that earlier date**, not as later restated, so the SUE
  seasonal-random-walk denominator is not itself contaminated by hindsight (this is the same
  restatement-bias concern CONTRACT §7 item 7 already raises generally for Indian fundamentals,
  applied here to the specific SUE calculation).
- **Analyst consensus** (only where used as an SUE alternative to SRW): forecast value, forecast
  date (must precede the announcement), and analyst count — expect this field to be usably dense
  only in the NIFTY 100–200 zone and sparse-to-absent through the Aggressive book's 500–750 tail,
  which is the practical reason candidate (a) above defaults to the SRW construction rather than
  an analyst-based one.
- **Corporate-action adjustment factors**: split/bonus/rights ratios needed to normalize EPS and
  share counts across the trailing 8-quarter SUE history — a standard but easy-to-botch step.
- **Prices**: daily (ideally intraday for the first 1–3 sessions) total-return-adjusted prices
  (dividends and corporate actions folded in) bracketing each announcement, matched to the correct
  session per the timestamp convention above; the Nifty 500 TRI as the abnormal-return benchmark,
  consistent with this program's working convention (CONTRACT §10) for alpha/signal research; an
  average-daily-value or similar liquidity field per name, to route each observation into the
  illiquidity gradient the decay literature says the effect actually lives on (§3), rather than
  treating the universe as homogeneous.
- **Universe/rank-band membership at the announcement date**, not today's membership — needed to
  avoid survivorship and to correctly assign each observation to the Aggressive (ranks 500–750)
  vs. Moderate/Conservative (ranks 1–500) book split the mandate already uses (CONTRACT §1).

The exact-timestamp requirement is not a generic fundamentals problem — it is specifically why
NSE corporate-announcement data (not an aggregate/restated fundamentals database) is the
load-bearing input here, and it is already a planned free pull on the RUNSHEET
(`ingest/vault/calendars/`, feeding H58-D2). The filed-EPS content is the natural companion to
route alongside whatever lands from the India-fundamentals handoff already in flight; this
dossier opens no new runsheet row, it flags where a PEAD design plugs into pulls already queued.

---

### Provenance summary

| Claim | Source | Tag |
|---|---|---|
| Drift exists post-announcement, ~half the eventual return priced by announcement month | Ball & Brown (1968), *JAR* 6(2) | [LIT] |
| Drift named/measured, SUE deciles, 60-day horizon | Bernard & Thomas (1989), *JAR* 27(Suppl) | [LIT], magnitude range [VERIFY exact pt. figure] |
| Mechanism: underreaction to earnings autocorrelation (+ lags 1-3, − lag 4), drift resolves at next 3 announcements | Bernard & Thomas (1990), *JAE* 13(4) | [LIT] |
| SUE metric popularized, decile approach | Foster, Olsen & Shevlin (1984), *Acc. Rev.* 59(4) | [LIT] |
| Early SUE risk-adjustment result | Rendleman, Jones & Latane (1982), *JFE* | [VERIFY exact cite] |
| Drift concentrated in low-coverage/low-institutional-ownership names | Bhushan (1994), *JAE* 18(1) | [LIT] |
| Separate unconditional announcement-date premium | Frazzini & Lamont, NBER WP c.2006-07 | [VERIFY venue/year] |
| Liquidity risk explains part of PEAD/momentum | Sadka (2006), *JFE* | [LIT] |
| Post-2000 attenuation in liquid names; costs consume most of the raw spread | Chordia, Goyal, Sadka, Sadka & Bommaraju (2009), *FAJ* 65(4) | [LIT], author list [VERIFY] |
| Trading-cost/capacity template | Korajczyk & Sadka (2004), *JF* 59(3) | [LIT] (momentum, not PEAD; applied by analogy) |
| Fundamental momentum without event dates | Novy-Marx (2015), NBER WP | [LIT], WP # [VERIFY] |
| Momentum/earnings-momentum decomposition | Chan, Jegadeesh & Lakonishok (1996), *JF* 51(5) | [LIT] |
| Revenue surprises, incremental + interactive | Jegadeesh & Livnat (2006), *JAE* 41(1-2) | [LIT] |
| India momentum/contrarian precondition | Sehgal & Balakrishnan (2002), *Decision* | [LIT], moderate-good confidence |
| India PEAD studies (direction, larger magnitude, weak methodology) | various Indian/regional journals | [VERIFY: no specific citation confirmed] |
| SEBI LODR Reg. 33 filing deadlines (45d/60d) | regulatory fact, not literature | n/a |
