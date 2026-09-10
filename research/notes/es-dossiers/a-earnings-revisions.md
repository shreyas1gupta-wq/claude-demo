# Analyst Earnings Revisions as a Return Predictor — Literature Dossier

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-10
Governed by `research/CONTRACT.md`. Numbers drawn from the literature carry **[LIT]**; nothing
here is a desk result — desk results live only in `research/register/trial-ledger.md`, and none
is quoted or invented in this note. This dossier stands **alongside**, not in place of,
`docs/cycles/31-revision-retail.md` (Atlas entry 3.5), which already carries this desk's formal
**REJECT-FOR-DATA** verdict on the earnings-revision cycle. That verdict is not reopened here —
it is confirmed, with a deeper literature base (Gleason-Lee, Zhang, Trueman, Hong-Kubik, Diether-
Malloy-Scherbina, Novy-Marx — none cited in the 3.5 monograph) and a sharper look at what a free
proxy can and cannot recover.

---

## 1. The classic evidence

**Givoly & Lakonishok (1979, 1980)** founded the field: *Journal of Accounting and Economics*
1(3) and *Journal of Banking and Finance* 4(3) show the **direction** of a change in analysts'
consensus earnings forecast carries information the market has not fully priced — months of
upward revision are followed by positive abnormal returns, downward revisions by negative ones.
This is the first demonstration that a forecast-**revision** signal, not merely the forecast
**level**, predicts returns.

**Stickel (1991)**, *The Accounting Review* 66(2), sharpens this into the signature this whole
literature is named for: prices continue **drifting** in the direction of a revision for an
extended period afterward rather than jumping to a new level immediately. The market underreacts
to the revision itself, not just to whatever news prompted it.

**Chan, Jegadeesh & Lakonishok (1996)**, *Journal of Financial Economics* — the paper this dossier
leans on hardest — tests earnings-based measures (standardized unexpected earnings, analyst
forecast revisions) against price momentum in the same sample and reaches the load-bearing
finding: **both measures independently predict subsequent drift, and each survives controlling
for the other** — risk, size, and book-to-market explain neither. Combining price momentum with
earnings/revision information produces a **materially larger** spread than either alone,
consistent with two only-partially-overlapping information channels rather than one channel
measured two ways. The paper also documents that analysts' own forecasts **respond sluggishly to
past price and earnings news**, worst among the poorest recent performers — underreaction by the
forecasters themselves, not just by price-setters. This partial-independence finding is the
single most important fact governing how a revisions signal should be read against a momentum
book that already exists: it is a genuinely separate channel, not a relabeling of price momentum,
but the CJL evidence is silent on how much of that incremental share survives cost and crowding
today.

**Bernard & Thomas (1989, 1990)**, *Journal of Accounting Research* 27 (Supplement) and *Journal
of Accounting and Economics* 13(4), are the sibling result on the realized-earnings side:
post-earnings-announcement drift (PEAD) — prices continue moving in the direction of an earnings
**surprise** for several quarters after the announcement, tracking a slow-diffusion mechanism the
revisions literature shares. PEAD is a **surprise** (realized-vs-expected) measure, not a
revision (expected-vs-previously-expected) measure; the distinction matters for §5 below, where
PEAD-style proxies are evaluated as an analyst-free substitute.

**Gleason & Lee (2003)**, *The Accounting Review* 78(1), isolates the price-discovery mechanics
of a revision directly: post-revision drift is **stronger** when the revision arrives **without**
an accompanying change in the analyst's stock recommendation (a "pure" forecast change, less
salient, more slowly digested) and is concentrated among stocks with **low institutional
following and low trading volume** — exactly the population where information diffuses slowly.
A revision bundled with a loud recommendation change gets priced faster; a quiet forecast-only
revision is where the drift survives longest. This maps the revisions premium onto a coverage/
liquidity gradient before Zhang formalizes the general point.

**Zhang (2006)**, *Journal of Finance* 61(1), generalizes that gradient into the "information
uncertainty" framework: momentum and revision-style drift profits are **larger** among stocks
with high information uncertainty — proxied by return volatility, analyst forecast dispersion,
small size, low analyst coverage, low share price, high cash-flow and earnings volatility. Higher
uncertainty means slower, noisier price discovery, which is exactly the condition under which an
underreaction-driven drift signal should be strongest and most durable against arbitrage.

**Commercial packaging.** The revisions signal is one of the oldest commercialized factor
categories: the **Zacks Rank** (Zacks Investment Research, since the 1980s) sorts stocks on
consensus-estimate revision trends and surprise history into quintiles; **StarMine's Analyst
Revisions Model (ARM)** (built on I/B/E/S data, now distributed via LSEG/Refinitiv) separates
revision **magnitude** from revision **breadth** (the share of covering analysts revising in each
direction) and combines both with StarMine's SmartEstimate (accuracy-weighted consensus) to
generate a "Predicted Surprise." Vendor-reported backtests of these products (marketing
material, not peer-reviewed) describe top-vs-bottom decile spreads on the order of high single
digits to low double digits of percent per year, pre-cost, concentrated in small/mid caps and
decaying toward zero in the largest, most liquid names — directionally consistent with the
academic coverage-gradient finding above, but these vendor figures are **not** literature-grade
and are stated here only as context for typical horizons: revisions signals are typically refreshed
monthly to quarterly (tracking the results calendar and interim broker notes) with an effective
predictive horizon of roughly one to two quarters — short relative to a value or quality signal,
longer than pure price reversal.

---

## 2. Decay and crowding

CONTRACT §5's governing principle is stated with two numbers already frozen into this program:
**McLean & Pontiff (2016)** find published anomalies decay **~26% out-of-sample** (pre-publication
data-mining bias corrected for) and **~58% post-publication** (arbitrage capital arriving once
the finding is public) **[LIT]**, averaged across ~97 anomalies in their sample, *Journal of
Finance* 71(1). Estimate-revision strategies were not singled out in their sample as an outlier
either direction; the generic average is the honest placeholder absent a signal-specific figure.

**Chordia, Subrahmanyam & Tong** (*Journal of Accounting and Economics* 58(1), 2014) test
attenuation directly over the post-decimalization, high-liquidity era and find anomaly returns
have **declined over time, with the decline concentrated in more liquid stocks** — consistent
with arbitrage capital finding easy execution in exactly the large-cap names where a revisions
signal is also, per Zhang (2006) and Gleason-Lee (2003), theoretically weakest to begin with. The
two findings compound rather than offset: liquid large caps are where crowding capital arrives
fastest **and** where the underreaction mechanism itself is thinnest — a signal with almost
nothing left to harvest in exactly the names easiest to trade it in.

**Reg FD (Regulation Fair Disclosure, US SEC, effective October 2000)** prohibited selective
disclosure of material non-public information to analysts ahead of the public market. **Gintschel
& Markov (2004)**, *Journal of Accounting and Economics* 37(3), find the average price impact per
unit of analyst forecast/recommendation revision **fell substantially post-Reg-FD [LIT: a decline
on the order of a third in their sample, cited with caveats — exact point estimate not
independently re-verified this session]**, consistent with analysts losing their private-
information edge and revising more on already-public information — a structural break specific
to the US regulatory regime with no India analogue (India has no equivalent selective-disclosure
ban with the same enforcement history, though SEBI's insider-trading and disclosure norms address
adjacent ground).

**Post-2010.** No source this dossier reached isolates a revisions-specific decay estimate
distinct from momentum's own — the same gap `docs/cycles/31-revision-retail.md` §A.3 already
flags and does not resolve; nothing here changes that conclusion. What is well established
qualitatively: the signal's fifty-year commercial availability (I/B/E/S since 1976), its packaging
into retail-accessible products (Zacks Rank), and its status as one of the most mechanically
computable, no-judgment-required anomalies in the taxonomy together make it a textbook candidate
for the compression Chordia-Subrahmanyam-Tong document — a pure information-gap anomaly with no
capacity limit, no compensated-risk story, and no institutional friction keeping large capital
out (CONTRACT §5's four survival categories, none of which this signal satisfies cleanly except
in the small-cap/low-coverage tail Zhang and Gleason-Lee identify).

---

## 3. Mechanisms: underreaction, herding, and three distinct constructs

**Why analysts revise gradually rather than jumping to the fully-updated number.**
**Trueman (1994)**, *Review of Financial Studies* 7(1), models analyst **herding**: analysts have
career and reputational incentive to publish forecasts close to the prevailing consensus and to
their own prior estimate, because an outlier forecast that turns out wrong is more damaging than
a consensus-hugging one that turns out wrong together with everyone else. This produces forecasts
that anchor on the last-published number and adjust toward new information only partially — the
direct microfoundation for Stickel's drift.

**Hong & Kubik (2003)**, *Journal of Finance* 58(1), find this is not just theory: relatively
inexperienced analysts are **more likely to be terminated** for inaccurate or "bold" (non-
consensus) forecasts, and analyst career outcomes reward optimistic and accurate-on-average
forecasting differently depending on brokerage prestige and tenure — a documented **career-
concerns** channel reinforcing Trueman's herding prediction with revealed labor-market
consequences, not just a plausible story.

**Why the market underreacts to the revision itself, not just to the news behind it.** **Hong &
Stein (1999)**, *Journal of Finance* 54(6), supplies the general theory: heterogeneous
"newswatcher" agents each observe only a fragment of private information and diffuse it into
prices gradually, generating momentum-style drift as a population-level information-processing
friction rather than any single agent's irrationality. Applied to revisions: the analyst
under-adjusts (Trueman/Hong-Kubik), and the market under-adjusts to the analyst's own
under-adjusted output — a "double diffusion" that is the standard explanation for why revisions
**lead** prices rather than being contemporaneously absorbed: the revision is itself informative
about a *further* revision not yet published, and price has no reason to anticipate information
that has not yet been generated.

**Three distinct constructs that must not be conflated** — the dossier's most important
discipline, since all three are sometimes loosely called "the revisions signal":

- **Revision LEVEL** — the sign and magnitude of the change in the consensus estimate itself.
  This is what Givoly-Lakonishok, Stickel, and CJL test; a **positive**-premium, direction-
  following signal.
- **Revision BREADTH (diffusion)** — the fraction of covering analysts revising up versus down,
  independent of the average magnitude (a market-internals-style "how many, not how much"
  construct). This is the leg StarMine's ARM adds explicitly alongside magnitude; it is a
  practitioner construct with no single dedicated academic paper this dossier can cite as its
  origin, correlated with but conceptually distinct from the level — two analysts revising up
  10% each reads differently from one revising up 20% and four revising down 5%, even though the
  average may match.
- **Forecast DISPERSION** — the cross-sectional **spread** across analysts' current estimates
  (not the change in any one of them). **Diether, Malloy & Scherbina (2002)**, *Journal of
  Finance* 57(5), show high dispersion predicts **lower** subsequent returns — the opposite sign
  from the revisions-level premium, and a genuinely different mechanism: under short-sale
  constraints, **Miller (1977)**, *Journal of Finance* 32(4), shows prices reflect only the more
  optimistic investors' views when pessimists cannot act on their beliefs, so a wide spread of
  opinion (proxied by forecast dispersion) signals overpricing that subsequently corrects
  downward. Dispersion says nothing about **direction** of revision and revision level says
  nothing about **disagreement** among forecasters; a stock can have a strongly positive revision
  trend with low dispersion (the clean case), a positive revision trend with high dispersion
  (agreement is breaking down even as the average rises — a weaker signal by the DMS logic), or
  any other combination. Any design that blends "high dispersion" and "negative revisions" into
  one state, or that treats dispersion as a magnitude-confidence weight on the revisions signal,
  is combining two literatures with **opposite-signed** premia and must say so explicitly rather
  than average them silently.

---

## 4. India: coverage, evidence, and the data wall

**The coverage landscape.** Sell-side analyst coverage in India is heavily concentrated: informal
market commentary and brokerage-industry reporting commonly put the number of NSE-listed
companies with active, multi-broker analyst coverage at roughly the **500-name** range — close to
the Nifty 500 — with coverage thinning sharply below that and becoming sparse-to-absent across
the microcap tail this desk's Aggressive book trades (ranks 500-750). This figure is **market
commentary, not a peer-reviewed statistic**, and is stated with that caveat rather than tagged
[LIT]. The practical consequence for this program is structural, not incidental: even a fully
funded, paid-data revisions signal would only ever be usable in the **Moderate and Conservative**
books (roughly ranks 1-500); the Aggressive book's mid/small tail is close to uncovered by
construction, no matter what data budget this desk had.

**Evidence from Indian markets.** Dedicated, India-specific academic literature testing analyst-
revision return predictability with the same rigor as the US corpus above is thin. Indian finance
research more often examines PEAD-style earnings-**surprise** drift (the realized, not forecast,
side) or analyst forecast **accuracy and optimism bias** in isolation, rather than a full
point-in-time consensus-revision-to-return pipeline; broader emerging-markets analyst-coverage
panels (studying business-group affiliation, coverage determinants, and forecast bias across
multiple EM countries) include India as one constituent among many rather than as a dedicated
subject. This dossier does not name specific India-only revisions-and-returns papers because none
were found with confidence sufficient to cite precisely, and CONTRACT's rule against fabricating
citations binds here as everywhere else. The likely reason the literature itself is thin is not
incidental: any India-based academic wanting to run this test faces the **same** paid-data wall
this desk does (I/B/E/S, BEst, Visible Alpha, Capital IQ), narrowed further by needing
institutional (typically WRDS-mediated) access — a data barrier that suppresses the supply of
India-specific academic evidence for the identical reason it suppresses this desk's ability to
trade the signal.

**The desk's own verdict, respected.** `docs/cycles/31-revision-retail.md` (Atlas 3.5, 2026-09-02)
already found, after a direct vendor hunt, that a genuine consensus estimate — a constructed
aggregate from a defined, continuously-maintained analyst panel with a preserved revision history
— is a paid commercial product everywhere, India included, with **no free substitute at any
comparable granularity or history**: Refinitiv/LSEG I/B/E/S, Bloomberg BEst, Visible Alpha, and
S&P Capital IQ all carry paywalled India coverage; domestic aggregators (Trendlyne, Capitaline)
publish only shallow free snapshots. That monograph's verdict — **REJECT FOR DATA**, the register's
fourth verdict type, distinct from an evidence-based reject, a fold, or a context entry — stands
unmodified by anything in this dossier. No free source has appeared since; the registered revisit
trigger (checked at the annual loop) has not fired.

---

## 5. Proxies that need no analyst data

**Novy-Marx (2015)**, NBER Working Paper 20984, "Fundamentally, Momentum is Fundamental Momentum,"
is the single most important paper for this section: it shows that momentum built from
**fundamentals** — persistence and revision in realized profitability/earnings measures, computed
entirely from filed accounting data with no analyst layer at all — captures a share of the
return-predictability space **comparable to** price momentum itself, and that fundamentals-based
momentum is not simply a noisier version of price momentum but carries real, largely independent
content. This is the direct academic foundation for an analyst-free "fundamental momentum" proxy:
rank-migration in reported EPS or ROE trend (is the trailing growth/profitability rank rising or
falling across the cross-section), built purely from as-filed quarterly results.

**Rank migration in reported EPS**, concretely: a state tracking whether a name's trailing
earnings-growth or profitability rank is improving or deteriorating quarter over quarter, using
only filed numbers (the RUNSHEET's owed "as-filed quarterly fundamentals" pull). This proxies the
**revision-level** construct's core intuition — something about this company's earnings path is
getting better or worse — without needing a forecast at all. The honest limitation, stated
plainly: it is backward-looking by construction (a change in *realized* results), where a true
consensus revision is forward-looking (a change in *expectation* ahead of the next realized
print) — so a rank-migration proxy will always **lag** a true revision signal by however long it
takes realized results to catch up with what analysts already suspected, the same "faster refresh
forgone" cost `docs/cycles/31-revision-retail.md` §A.5 already books against the paid alternative.

**Guidance revisions** (management's own forward guidance, where issued, changing over time) are
free from exchange filings but were already graded in the 3.5 monograph as measuring a
**different object**: unstructured commentary from one interested party (the company, with every
incentive to manage tone) rather than a cross-sectional aggregate of independent professional
forecasts. This dossier adds one further India-specific caveat: formal quantitative guidance is
**less prevalent** among Indian listed companies than among US issuers, where quarterly guidance
calls are closer to a market norm — narrowing this proxy's cross-sectional coverage further, on
top of its object-mismatch problem.

**What the literature says each proxy captures.** Reading CJL (1996) and Novy-Marx (2015)
together: fundamentals-only momentum (rank migration, Novy-Marx style) and price momentum
jointly recover **most** of what the combined price-plus-earnings-information strategy in CJL
achieves — but CJL's own central finding is that the analyst-forecast-revision channel carries
**incremental** content beyond price and realized-fundamentals momentum combined, precisely
because a consensus estimate can move on information (a competitor's results, a sector data
point, a macro print) **between** a company's own results dates, something no backward-looking
fundamentals proxy can ever see by construction. The honest accounting, consistent with
`docs/cycles/31-revision-retail.md` §A.5: analyst-free proxies capture the *bulk* of the
revisions-adjacent predictability space, but a specific, real, non-zero slice — the
between-results, forward-looking refresh — is only available with genuine analyst data and is
therefore permanently forgone under this desk's REJECT-FOR-DATA verdict.

---

## 6. Edge candidates for this desk

**(a) Fundamental-momentum / EPS-rank-migration state (Novy-Marx-style).**
*Mechanism*: persistence in realized profitability/earnings growth rank, an analyst-free
specialization of the same underreaction family as price momentum. *Expected magnitude*: no
India-specific or desk figure exists; the literature benchmark is Novy-Marx's finding that
fundamentals-based momentum matches price momentum's predictive content in US data **[LIT,
directional only — no point estimate carried forward]**. *Decay risk*: high overlap with
`L3_momentum_composite`, this ladder's existing central EDGE — CJL's own partial-independence
finding means the **incremental** value over price momentum alone is the open empirical question,
not the gross spread; treat as a refinement/confirmation input to the existing momentum seat
rather than a new standalone signal until tested. *Data needed*: as-filed quarterly EPS/ROE
history (RUNSHEET: "as-filed quarterly fundamentals," principal-machine, scrape-shaped) — already
queued for the QG track.

**(b) Result-day surprise / PEAD proxy.**
*Mechanism*: Bernard-Thomas drift following the price reaction to a filed result versus a
trend-extrapolation or year-over-year expectation (since no true consensus exists to surprise
against). *Expected magnitude*: PEAD is one of the most replicated drift effects in the
literature, but its size in India specifically, against a crude (non-consensus) expectation
proxy, has no citable magnitude here **[no LIT figure — not attempted]**. *Decay risk*: moderate;
PEAD-style drift is closer to a point measurement than a trend and is already partially inside
this ladder's own realized-return response, so the marginal contribution is likely small.
*Data needed*: bhavcopy (vaulted) plus filed results dates and figures (RUNSHEET: exchange
results calendars, "Priority 3").

**(c) Guidance-tone sentiment scoring.**
*Mechanism*: NLP-scored tone of management commentary/earnings-call transcripts as a leading
indicator of subsequent (unobserved) analyst moves. *Expected magnitude*: none citable; this is
flagged explicitly in `docs/cycles/31-revision-retail.md` §A.4.2 as measuring a different object
from the revision path, and its India coverage is thinner than the US given lower guidance
prevalence. *Decay risk*: unclear — genuinely under-researched rather than known-decayed, but the
object-mismatch problem is a ceiling on its value regardless of crowding. *Data needed*: exchange
filings / call transcripts (uneven availability across the NIFTY 750 tail); would require text
infrastructure this program does not currently have queued.

None of (a)-(c) is the revisions signal itself; each is graded here exactly as
`docs/cycles/31-revision-retail.md` §A.4.2 grades the two proxies it already examined — a
related but distinct object, admitted on its own evidence, never smuggled in under the
revisions name.

---

## 7. Data requirements — India

**What a true point-in-time revisions test would need.** (i) A defined, continuously maintained
panel of contributing sell-side analysts per stock, not a single-source estimate. (ii)
Individual-analyst forecasts date-stamped at submission, so a consensus can be reconstructed
as-of any historical date without look-ahead. (iii) A fixed consensus-construction rule (mean or
median, trimming convention, minimum contributor count) applied consistently across history. (iv)
A **preserved revision history** — the object the entire literature's predictive content lives
in — not merely the current snapshot a live terminal shows. (v) Coverage matched to the desk's
tradable universe; per §4, this ceiling is roughly the Nifty 500, so even a fully resourced build
would not extend into the Aggressive book's ranks 500-750 tail. (vi) Point-in-time snapshotting
with no retroactive restatement, the same WORM/two-pass discipline this program applies to every
other vault (CONTRACT §2, near-miss #4).

**Where it could come from, if anywhere.** Systematically, nowhere free today: I/B/E/S
(Refinitiv/LSEG), Bloomberg BEst, Visible Alpha, and Capital IQ are the institutional-grade
sources and all are paid subscriptions with no free equivalent; domestic aggregators (Trendlyne,
Capitaline) publish only shallow, inconsistent free snapshots with no defined panel or preserved
history. Scraping individual brokerage "upgrade/downgrade" and target-price headlines from
financial news wires is not a substitute even where technically feasible: it lacks a defined
contributor panel and a consistent construction rule, and — a **legal** caveat beyond the cost
one — redistributing or systematically aggregating licensed brokerage research would run against
the issuing broker's own copyright and distribution terms, a different and harder constraint than
a mere paywall. Academic-style access via a university WRDS subscription is the route actual
published research typically uses and is not available to this desk (CONTRACT §3: principal +
Claude, no institutional subscription). SEBI's Research Analyst Regulations require certain
disclosures from registered analysts but do not produce an aggregable, structured consensus
series. **Conclusion**: no free, legal, point-in-time India consensus-revision source exists
today. This confirms rather than reopens `docs/cycles/31-revision-retail.md`'s REJECT-FOR-DATA
verdict; the registered revisit trigger (a free, auditable India consensus source appearing,
checked at the annual loop) stands as the only mechanism by which this changes.
