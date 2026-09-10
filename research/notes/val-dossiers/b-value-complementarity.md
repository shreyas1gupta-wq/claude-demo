# What Combines With Value, and What Does Not — the Complementarity Literature

*Literature dossier, Track VAL, 2026-09-10. No web fetches this session — written from
training knowledge per instruction. Every literature claim carries **[LIT]**; where the
magnitude is recalled with less confidence than the citation itself, **[LIT, LOW
CONFIDENCE]**. Desk numbers are quoted verbatim from `research/register/trial-ledger.md`
(entries V0–V4, 2026-09-01, and TL-D2, 2026-09-07) and marked **[DESK, <entry>]** — not
re-derived here. Per CONTRACT §4/§9, every non-India citation is a cross-country prior,
Tier B at best for this program until purged-CV India tests exist.*

---

## 1. Value + momentum — the one pairing nobody disputes

**Asness, Moskowitz & Pedersen (2013), "Value and Momentum Everywhere," *Journal of
Finance* 68(3)** [LIT] is the anchor. Testing value and momentum side by side in eight
markets and asset classes (individual stocks in the US/UK/Europe/Japan, plus equity
index futures, government bonds, currencies and commodities), they show two things at
once: value and momentum each earn significant returns almost everywhere tested, and —
the counterintuitive result — **value and momentum are negatively correlated with each
other, both within and across markets**, more reliably than either factor correlates
positively with itself across unrelated asset classes [LIT]. Secondary sources converge
on a within-asset-class correlation near **−0.5**, individual-stock estimates running
closer to **−0.6** [LIT, LOW CONFIDENCE on the exact table cell]. The desk's own
recomputation confirms the sign and rough scale directly: **India HML/WML corr = −0.37,
US HML/Mom corr = −0.41** [DESK, V2] — AMP's diversification claim replicates on both
panels the desk actually holds, not merely on the published US/global sample.

**Mechanism.** AMP rationalize the common structure through a partial common driver — a
global funding-liquidity factor: when funding is tight, value (long illiquid, recently-
battered names) suffers while momentum (long recent winners, typically better-funded) is
comparatively protected, and vice versa [LIT]. A second, purely statistical framing:
momentum captures intermediate-horizon (3–12mo) continuation before it reverses; value
captures the longer-horizon reversion once an extrapolation error corrects — opposite
sides of the same reversal-versus-continuation tension at different horizons, enough on
its own to generate negative correlation without either factor being mispriced [LIT].

**The combination arithmetic.** For two zero-cost strategies with Sharpe ratios `SR₁,
SR₂` and correlation `ρ`, mean-variance algebra gives the optimal combination's Sharpe as
`SR_p² = (SR₁²+SR₂²−2ρ·SR₁·SR₂)/(1−ρ²)`. Any `ρ<1` raises the combined Sharpe above
either leg; negative `ρ` is doubly favorable, since `−2ρ·SR₁·SR₂` turns positive while
`(1−ρ²)` is unaffected — at AMP's approximate `ρ≈−0.5` with equal legs, the combined
Sharpe is exactly double either leg's own [LIT — a mean-variance identity, not a
paper-specific number]. The desk's own 50/50 blend confirms the arithmetic is not just
algebra: **US 50/50 Sharpe 0.72 vs. legs 0.33 (HML)/0.45 (Mom); India 50/50 Sharpe 0.86
vs. legs 0.42 (HML)/0.55 (WML)** [DESK, V3] — the blend beats *both* legs on *both*
panels, the reason this pairing is treated as the most robust cross-factor combination
in the literature: the correlation is negative, it holds across markets and asset
classes, and it survives replication on a completely separate data panel (the desk's own
India mirror), not just the original paper's own sample.

**The stock-level interaction — avoiding cheap-and-falling.** The portfolio-level
diversification story does not by itself tell an operator what to do with a name
simultaneously cheap (value flags it) and falling (momentum flags it short) — the
"falling knife" cell. The practitioner resolution, consistent with AMP's own framing and
O'Shaughnessy's composite-factor tradition [LIT], is to use momentum as a **timing/
admission filter inside value selection**, not an independent short-eligible signal in a
long-only book: cheap-but-bottom-momentum-decile is disproportionately "cheap because
genuinely deteriorating," while cheap-and-not-falling is closer to value's classic
mean-reversion setup. This is the architecture the desk's value-deep dossier already
committed to (`research/cycles/value-deep/partA-theory-psychology.md`, §A.8): momentum
as a rank-tiebreaker inside the value/quality book, earning its keep on diversification
rather than as a second standalone sleeve, given momentum's unfavorable turnover economics.

---

## 2. Value + quality/profitability — "the other side of value"

**Novy-Marx (2013), "The Other Side of Value: The Gross Profitability Premium," *Journal
of Financial Economics* 108(1)** [LIT]. Gross profitability (`(Revenue−COGS)/Assets`)
predicts returns with "roughly the same power" as book-to-market — the most profitable
quintile earns **≈0.31%/month** above the least profitable, a long-short **≈0.54%/month**
(t≈5) [LIT, LOW CONFIDENCE on the exact decimal] — despite profitable firms having
*lower* B/M and *larger* size. Profitability and value are close to orthogonal
empirically, so controlling for it **materially improves value-strategy performance**,
especially in large, liquid stocks where naive cheapness fades [LIT] — the central
argument for combining rather than choosing between value and quality.

**Piotroski (2000), "Value Investing...," *Journal of Accounting Research* 38
(Supplement)** [LIT] is the canonical value-trap filter, explicitly a **conditioning
overlay applied only within the cheap universe**, not a standalone factor. Nine binary
signals in three groups: **profitability** — ROA positive, ΔROA positive, CFO positive,
CFO exceeds net income; **leverage/liquidity/issuance** — leverage decreasing, current
ratio increasing, no new share issuance; **operating efficiency** — gross margin and
asset turnover improving. Summed into `F ∈ {0,...,9}`, computed **only within the top
B/M quintile**. Magnitudes, 1976–1996 US: **F-Score 8–9 beats the market by +7.5%/yr;
0–1 lags by −8.3%/yr; long-high/short-low earned 23%/yr, pre-cost** [LIT]. Works best,
per the paper's own cross-section, in **small, neglected, high-B/M names with low
analyst coverage** — the corner of the cheap universe most likely to be a genuine
"cheap for a reason" trap, and where the fundamental signal faces the least competition
from sophisticated capital already pricing it in.

**Greenblatt's "Magic Formula"** (*The Little Book That Beats the Market*, 2005) [LIT] is
the practitioner-accessible version of the same logic: rank on `EBIT/EV` (cheapness/
yield) plus `EBIT/(Net Working Capital + Net Fixed Assets)` (return-on-capital/quality),
buy the intersection. The book's own backtest claims roughly **30%/yr**, 1988–2004
[LIT]; independent replication and the formula's own live mutual-fund record have run
**materially weaker** — a McLean-Pontiff-style in-sample-to-live decay case study, not a
refutation of the underlying logic [LIT, LOW CONFIDENCE on the exact gap]. The lesson: a
combination this simple and this long-marketed is exactly where CONTRACT §5's "why does
this survive being known" test bites hardest — the mechanism likely survives; the
specific magnitude almost certainly does not.

**Fama & French on the double sort.** Both the original **1992/1993** size-and-B/M work
and the **2015 five-factor model** (adding profitability RMW and investment CMA) [LIT]
bear on this directly: in the five-factor spanning tests, **HML becomes statistically
redundant** once profitability and investment are added as separate factors — a large
share of the historical value premium overlaps a profitability/investment tilt [LIT].
This is the formal version of Novy-Marx's characteristic-level finding: value and
quality are not identical, but correlated enough that a well-specified quality factor
absorbs much of what a standalone value factor used to explain.

---

## 3. Value + low-vol, + investment/CMA, + carry — three overlaps of varying honesty

**Value + low-vol/QMJ.** The desk's own value-deep dossier already documents the
mechanism directly rather than importing it untested: **Frazzini & Pedersen (2014)
Betting Against Beta** [LIT] supplies the institutional-constraint story (leverage-averse
investors overpay for high-beta/glamour names, flattening the security market line), and
India's own dedicated test — **Agarwalla, Jacob, Varma & Vasudevan (2014)**, "Betting
Against Beta in the Indian Market" [LIT] — finds India's BAB premium **dominates size,
value and momentum but is largely explained once a profitability/quality factor is
added**: India's low-beta effect looks like a quality effect in beta's clothing. The
practical implication for this dossier's table: value+low-vol is not so much a clean,
additive pairing as a case where low-vol and quality substantially **share** a survival
mechanism (leverage-constrained institutions avoiding — or being unable to lever into —
junk), so stacking all three (value, quality, low-vol) as if fully independent risks
double- or triple-counting one underlying institutional-constraint story rather than
three orthogonal edges.

**Value + investment/asset growth — is CMA just value in drag?** Two lineages converge on
the same fact from different angles. **Titman, Wei & Xie (2004), "Capital Investments
and Stock Returns," *Journal of Financial and Quantitative Analysis*** [LIT] find firms
that ramp capital investment subsequently earn **abnormally low** returns, consistent
with overinvestment/empire-building. **Cooper, Gulen & Schill (2008), "Asset Growth and
the Cross-Section of Stock Returns," *Journal of Finance*** [LIT] generalize this to
total asset growth and find it one of the **strongest single return predictors** in the
US cross-section [LIT, LOW CONFIDENCE on the exact decile spread]. Fama-French's own
**CMA** factor formalizes this into the five-factor model — and, per §2, its inclusion is
precisely what renders HML redundant in spanning regressions [LIT]. **The honest answer:
substantially yes at the factor-return level, no at the mechanism level.** High-B/M
firms are, almost by construction, firms with poor investment opportunities and low
reinvestment — the same firms a low-asset-growth sort selects — so the two
characteristics are highly correlated and much of their *measured* return overlaps
[LIT]. But the *mechanisms* differ: value's leading stories are relative-distress risk
or extrapolative mispricing, while CMA's is a q-theory-consistent, investment-based
asset-pricing relation with no mispricing required (the agency/overinvestment reading is
the competing, behavioral explanation) [LIT, LOW CONFIDENCE on which camp dominates].
Practical read: **treat CMA/asset-growth as REDUNDANT with a majority-B/P value
composite**, but potentially **complementary to a price-only, non-B/P composite**
(dividend yield, NSI, sales/price — D02's preferred construction), since a price-only
composite does not mechanically encode the same book-value-based investment history HML
and CMA share.

**Value + carry across asset classes.** **Koijen, Moskowitz, Pedersen & Vrugt (2018),
"Carry," *Journal of Financial Economics*** [LIT] generalize the currency-carry-trade
concept into one "carry" measure — the expected return to holding an asset if its price
does not change — across global equities, bonds, currencies and commodities, finding it
earns significant returns in every asset class tested, only partially explained by
standard risk factors [LIT]. The overlap with value is asset-class-dependent: **in
single-country equities, "carry" is typically proxied by dividend/earnings yield —
already inside almost every value composite — so value+carry in equities is close to
REDUNDANT by construction.** **Across asset classes (bonds, FX, commodities), carry is
genuinely distinct** — no natural "B/M" exists for a currency or commodity future — so a
multi-asset carry sleeve (gold, any future rates/FX overlay) would be legitimately
complementary, not a duplicate. Given this program's mandate (equities, gold, debt —
CONTRACT §1): do not budget carry as a second equity sleeve; track it as a candidate
framing for the gold/debt legs later, where it would be genuinely new information.

---

## 4. What does NOT combine

**Value + small — the junk confound the desk has already booked.** Combining a value
tilt with a raw small-cap tilt looks, on paper, like stacking two independently
documented premia. **Asness, Frazzini, Israel, Moskowitz & Pedersen (2018), "Size
Matters, If You Control Your Junk," *Journal of Financial Economics* 129(3)** [LIT] show
why this is not simply additive: the raw size premium's instability across decades is
substantially explained by small-cap portfolios' heavier average tilt toward junk — low
profitability, high leverage, high distress risk — relative to large-cap portfolios; once
quality/junk exposure is held constant, a **quality-controlled** size premium is large
and stable, but the **raw, unconditioned** size tilt is not [LIT]. This desk's own India
evidence lands on the same conclusion from a completely different construction: **the US
small segment pays +1.5–2.7pp/yr across horizons (1.32x market vol) while the Indian
smallcap segment, at the factor level, is priced NEGATIVE at −2.9pp/yr over 32 years
(1.34x vol, −90% vs −62% max drawdown)** [DESK, TL-D2] — "the smallcap money in India is
selection inside the segment, never the segment" [DESK, TL-D2]. Layering a naive value
screen on top of a naive small-cap universe does not diversify two premia; it **doubles
down on the same junk/distress tilt** the size literature already shows is what makes
raw small-cap unreliable, and on the desk's own India print, actively negative — a
combination that is not merely non-additive but actively antagonistic unless a genuine
quality filter is interposed between the two.

**Value + dispersion.** Analyst-forecast dispersion — cross-sectional disagreement among
analysts' earnings estimates — is a documented predictor in its own right: **Diether,
Malloy & Scherbina (2002), "Differences of Opinion and the Cross Section of Stock
Returns," *Journal of Finance*** [LIT] find high-dispersion stocks earn **lower**
subsequent returns, a disagreement-plus-short-sale-constraint mechanism (optimists
dominate price when pessimists cannot short) [LIT, LOW CONFIDENCE on the exact spread].
This does not combine cleanly with value because it is informational overlap, not
statistical diversification: dispersion is highly correlated with the same distress/
uncertainty characteristics a value-trap screen (Piotroski, distress scores — §5) is
already built to catch, so conditioning value on dispersion mostly re-derives
information the quality/distress overlay already supplies. As an independent
value-timing conditioner, incremental out-of-sample evidence is weak [LIT, LOW
CONFIDENCE — closer to a practitioner overlay than a settled result]. Net read:
**largely REDUNDANT with the quality/distress overlay**, not a third independent axis.

**Value + growth forecasts — conditioning against the mechanism.** This is the sharpest
"do not combine" here, because the antagonism is structural. **La Porta (1996),
"Expectations and the Cross-Section of Stock Returns," *Journal of Finance*** [LIT] and
**Bordalo, Gennaioli, La Porta & Shleifer (2019), "Diagnostic Expectations and Stock
Returns," *Journal of Finance*** [LIT] (both already anchored in the value-deep dossier,
§A.2) show a long-low-forecast/short-high-forecast strategy on consensus long-term
growth forecasts earns a large return, driven by analysts' overextrapolation of recent
growth news. **The extrapolation error consensus growth forecasts embed is not noise on
top of the value premium — it IS a substantial part of what value is compensation for
harvesting** (LSV 1994; La Porta). A design that screens out cheap stocks *because*
their consensus forecasted growth is low is, under this mechanism, filtering out exactly
the names whose forecast is most likely to be wrong in the direction that pays value off
— fighting the mechanism, not refining it. This is distinct from Piotroski-style
conditioning on *realized, trailing* fundamentals (§5): trailing ROA/CFO checks whether
cheapness reflects genuine deterioration already underway, while forward consensus
growth forecasts are the object value is designed to exploit. Conditioning on the former
sharpens the signal; conditioning on the latter cancels it.

**Doubling on correlated value measures — fake diversification.** B/P, E/P, CF/P and
sales/price are legitimate value multiples that are also **highly correlated** — the
same firm looks cheap or expensive on most of them at once. Composite value
constructions (AQR-style composites; O'Shaughnessy's multi-metric screens) [LIT] average
several together, a genuine but mild improvement — it reduces idiosyncratic measurement
noise (a low-quality earnings number distorting E/P alone) — but it is **noise reduction
on one signal, not diversification across independent signals**, and should not be
sized as if three correlated multiples equalled three independent factors. Same trap in
miniature as CMA (§3): stacking correlated measures inflates the apparent signal count
without adding the independent information the trial-ledger's true-count discipline
(CONTRACT §9) requires — every extra multiple in a composite is a construction choice
to log, not a new edge to claim.

---

## 5. Value traps — what identifies them ex-ante

Three literatures converge on overlapping but distinguishable ex-ante filters.

**Leverage/distress.** **Campbell, Hilscher & Szilagyi (2008), "In Search of Distress
Risk," *Journal of Finance* 63(6)** [LIT] — already anchored in the value-deep dossier —
build a dynamic logit failure-probability model and find that, since 1981, financially
distressed stocks deliver **anomalously low** returns despite higher volatility, beta
and size/value loadings: the opposite of a compensated-risk prediction. **Dichev (1998),
"Is the Risk of Bankruptcy a Systematic Risk?," *Journal of Finance*** [LIT] reaches the
same conclusion earlier with Altman's Z-score/Ohlson's O-score: bankruptcy risk is not
rewarded with higher returns. **Griffin & Lemmon (2002), "Book-to-Market Equity,
Distress Risk, and Stock Returns," *Journal of Finance*** [LIT] sharpen this for value
specifically: the value premium is *concentrated* in high-distress-risk (high O-score)
firms, yet those same firms show the **largest** subsequent underperformance around
negative earnings surprises — cheap-and-distressed is simultaneously where the raw
premium looks largest in-sample and where trap risk concentrates. Together these three
are the strongest argument here that "cheap because distressed" is not a risk premium an
investor is paid to bear — closer to a behavioral overpricing/distress-avoidance-failure
story, exactly why screening it out is defensible.

**Falling fundamentals, issuance, and low accruals quality.** Piotroski's own
ΔROA/ΔCFO/Δmargin/Δturnover signals (§2) are the "falling fundamentals" check inside the
F-Score. **Pontiff & Woodgate (2008), "Share Issuance and Cross-Sectional Returns,"
*Journal of Finance* 63(2)** [LIT] — already anchored in D02 — show net share issuance
predicts returns with power exceeding size, B/M or momentum individually, post-1970 US;
issuing firms subsequently underperform. **Sloan (1996)** [LIT] and **Dechow & Dichev
(2002), "The Quality of Accruals and Earnings," *The Accounting Review*** [LIT] supply
the accruals-quality channel: earnings driven by large, poorly-matched accruals are less
persistent and predict lower forward returns — a distinct mechanism from issuance even
though both often co-occur in the same deteriorating firm.

**Which filter has the strongest evidence.** By replication count, magnitude and
mechanism clarity together, **the Piotroski F-Score composite has the strongest
practical evidence base** — most-replicated, largest-magnitude (+7.5%/−8.3% extremes,
23%/yr long-short pre-cost), and designed to fire only within the cheap universe. But
**the distress-risk literature (CHS/Dichev/Griffin-Lemmon) supplies the clearest
mechanism** for why a trap filter should work at all: distress is empirically **not** a
compensated risk, so screening it out is close to a free removal of downside rather than
surrendering a real premium. Synthesis: a composite anchored on Piotroski's structure,
with its leverage/liquidity/issuance signals read through the distress literature's lens
(proxying for the one channel — distress — the evidence says is genuinely avoidable), is
better evidenced than any single univariate filter used alone.

---

## 6. Timing value with the value spread — one paragraph

The desk already carries its own extended treatment of this debate (`research/dossiers/
02-value-quality-lowvol.md` §1/§4; `research/cycles/value-deep/partA-theory-psychology.md`
§A.4/§A.9), so this dossier does not re-derive it: **Cohen, Polk & Vuolteenaho (2003)**
[LIT] show the value spread's own percentile forecasts the value factor's forward return,
the direct evidentiary basis for a spread-conditioned sleeve weight; the countervailing
camp — **Asness, Ilmanen, Israel & Moskowitz's "contrarian factor timing is deceptively
difficult"** line and Arnott-Beck-Kalesnik-West's "smart beta gone horribly wrong" —
[LIT] warn that valuation-spread timing looks compelling mostly because of one or two
large episodes, that the effective number of independent timing "calls" is tiny once
autocorrelation is accounted for, and that a factor's own re-rating (not a repeatable
premium) can dominate its trailing return in either direction. Both camps agree on the
spread's descriptive predictive power; they disagree on how much of it is safely
exploitable net of estimation risk and re-rating risk — which is precisely why the
desk's own design treats the spread as a **quantile-based sleeve-weight conditioner
within a frozen range**, never a standalone timing trade, and requires Stambaugh-bias
correction before trusting any in-sample India regression of the same form.

---

## 7. India — value+momentum, value+quality, and promoter pledging

**India value+momentum.** **Agarwalla, Jacob & Varma (2013/2017), "Size, Value, and
Momentum in Indian Equities," *Vikalpa* 42(4)** [LIT] report HML averaging **15.3%/yr**
over Jan 1994–Dec 2014 against an 11.5%/yr market premium and 21.9%/yr momentum. The
desk's own vaulted mirror of a related India factor series prints materially different
sub-period levels — **full-period HML +8.6%/yr (Sharpe vs RF only 0.09); the 2015–2019
"growth mania" window +0.8%/yr (Sharpe −0.39); post-2020 +18.8%/yr (Sharpe 0.82)** [DESK,
V1] — a genuine, honestly-flagged discrepancy against the published AJV figure rather
than a reconciled number, consistent with the desk's own standing [VERIFY] on this
mirror's construction. What both sources agree on: **the value-momentum negative
correlation itself replicates cleanly in India (−0.37) [DESK, V2], and the 50/50 blend
beats both legs (Sharpe 0.86 vs. 0.42/0.55) [DESK, V3]** — AMP's core complementarity
claim is the most robustly confirmed India fact in this whole dossier, more robust than
either factor's own standalone level.

**India value+quality.** **Agarwalla, Jacob, Varma & Vasudevan (2014)** [LIT] find
India's BAB (low-beta) premium dominates size, value and momentum in raw form but is
**largely explained once a profitability/quality factor is added** — quality in beta's
clothing (§3 above). Two recent, direct India QMJ replications — one in *IIMB
Management Review* finding quality firms show greater crash-period resilience and
consistently outperform junk, a second (2025) extending the construction with an
ML-augmented factor — are the first *dedicated* (not BAB-proxied) India QMJ tests this
dossier is aware of [LIT, LOW CONFIDENCE on both papers' exact magnitudes]. Set against
this, **Sehgal's own India work** is more skeptical specifically on the risk-adjusted
question — reporting that size-, value-, reversal- and momentum-based India strategies
do not clearly survive risk-adjustment in his sample [LIT] — read as: the *raw* India
value and value-momentum-combination premia are not seriously disputed; whether they
survive costs and proper risk adjustment is the harder, open question. India's evidence
base is **Tier B at best** by the CONTRACT's own count rule — well short of the
≥30-observation Tier-A bar — and the desk's own SC-track findings this week (US SMB
momentum era-fragile pre-1981 only; India smallcap rebound timing *inverts* the US) are
a standing caution against assuming any single-country factor-interaction finding here
is free of era-fragility until purged-CV tested on the desk's own data.

**Promoter share pledging as an India-specific trap marker.** Multiple 2023–2025 India
papers (e.g., "Promoter Share Pledging and Downside Risk: Evidence from Indian Listed
Firms") [LIT, LOW CONFIDENCE on exact magnitudes] find pledging positively associated
with future crash risk and negatively with financial performance — worse CVaR/VaR,
deeper drawdowns. This has no close US analogue at comparable scale (US firms rarely
pledge control-block shares against personal margin loans the way concentrated Indian
promoters do): a **governance/ownership-structure** risk distinct from any imported QMJ
or F-Score component. **The design implication is concrete**: the India-fundamentals
handoff (`research/register/handoff-prompt-india-fundamentals.md`, deliverable P5)
specifies exactly this field — `shareholding_pledge.csv` (isin, ticker, quarter_end,
filing_date, promoter_pct, promoter_pledged_pct_of_promoter_holding), sourced from
SEBI/exchange shareholding-pattern filings, **genuinely point-in-time by regulatory
construction** (SAST/takeover-code thresholds, filed quarterly). Unlike the P&L/
balance-sheet fields in the same handoff, which need a 30–45 day lag buffer and carry
Ind-AS restatement risk, pledge data arrives already PIT-clean — usable as a value-trap
screen the moment it lands. Per the India fundamentals dossier's own proposed test
(`research/notes/fun-dossiers/f-india-quality-data.md`, §6.4): **pledge level alone is
noisy (benign pledging is common); the pre-registered signal is pledge-acceleration ×
falling price** — an interaction term, not a static threshold (CONTRACT §6), and
structurally the India-specific analogue of the CHS/Dichev distress-avoidance filter in
§5: a channel the evidence says is avoidable without giving up a real risk premium,
since a pledge-driven crash is a governance/liquidity event, not a priced distress
factor.

---

## 8. Edge candidates for this desk

| Candidate | Mechanism | Magnitude | Data needed |
|---|---|---|---|
| Value + momentum rank-tiebreak | AMP negative correlation; momentum as an admission filter avoiding "cheap and falling" | Combined Sharpe ≈2x either leg at ρ≈−0.5 [LIT+hedge]; desk's own 50/50 India Sharpe 0.86 vs. 0.42/0.55 legs [DESK, V3] | Already vault-available (India HML/WML mirror); needs purged-CV on the desk's own PIT panel once fundamentals arrive |
| Quality-conditioned value (Piotroski-style, distress-anchored) | Distress is empirically uncompensated (CHS/Dichev); F-Score screens the cheap universe for genuine vs. trap cheapness | +7.5%/−8.3% F-Score extremes, 23%/yr long-short pre-cost, 1976–96 US [LIT]; India replication fragmented, no pinned magnitude | PIT ROA/CFO/leverage/issuance/margin/turnover series — the handoff's P1 (fundamentals_quarterly.csv) |
| India-specific pledge-acceleration trap screen | Governance/ownership-concentration risk, not a priced distress factor — genuinely avoidable | Directional only; no India-specific bp figure found [LIT, LOW CONFIDENCE] | `shareholding_pledge.csv` (handoff P5) — already PIT by construction, no restatement lag needed |
| Cash-flow-based profitability over accrual-inclusive earnings | Ball-Gerakos-Linnainmaa-Nikolaev: cash-based operating profitability subsumes the accrual anomaly and outperforms gross profitability alone | [LIT, LOW CONFIDENCE on exact incremental spread]; not sized for India | CFO + revenue + COGS at filing-date granularity — P1 of the handoff |
| Price-only value composite (majority dividend yield/NSI/sales-price) | Avoids CMA/HML redundancy (§3) and the restatement bias (CONTRACT Known Prior #7) simultaneously, since price-only signals are PIT by construction | N/A — a construction choice, not a premium claim | Bhavcopy + corporate-action filings only; fully available today without waiting on the fundamentals handoff |

**Summary table — companion metric vs. value, per the literature reviewed above.**

| Companion metric | Verdict | One-line reason |
|---|---|---|
| Momentum | **COMPLEMENTARY** | Negative correlation (−0.4 to −0.6) [LIT], replicated on both US and India desk data [DESK, V2/V3]; combined Sharpe exceeds either leg |
| Gross profitability / QMJ quality | **COMPLEMENTARY** | Near-orthogonal characteristic to B/M [LIT]; combining materially improves large-cap value performance (Novy-Marx) |
| Piotroski F-Score / distress avoidance | **COMPLEMENTARY (conditioning, not standalone)** | Distress is uncompensated (CHS/Dichev); screening it inside the cheap universe removes trap risk without giving up premium |
| Low-vol / BAB | **PARTIALLY REDUNDANT with quality** | India's own BAB premium is largely explained once quality is added [LIT] — shares an institutional-constraint mechanism with QMJ rather than adding a fourth independent axis |
| Investment/asset growth (CMA) | **REDUNDANT at the factor level, situationally complementary** | HML statistically redundant once CMA/RMW added (FF 2015) — same firms, correlated characteristic; complementary mainly versus a price-only (non-B/P) value composite |
| Carry (cross-asset) | **REDUNDANT in equities / COMPLEMENTARY across asset classes** | Equity carry ≈ dividend/earnings yield, already inside most value composites; genuinely distinct in bonds/FX/commodities where no B/M analogue exists |
| Small/size (raw, unconditioned) | **ANTAGONISTIC unless quality-filtered** | Raw size premium is a junk-tilt artifact (AFIMP 2018); desk's own India print is negative (−2.9pp/yr) [DESK, TL-D2] — combining doubles down on distress risk, not diversification |
| Analyst dispersion | **REDUNDANT with distress/quality overlay** | Disagreement effect (Diether-Malloy-Scherbina) largely re-derives information a distress/quality filter already supplies [LIT] |
| Consensus growth forecasts (as a value screen) | **ANTAGONISTIC** | Extrapolation error in growth forecasts IS the mechanism value harvests (La Porta; BGLS); screening on it fights the premium's own source |
| Multiple correlated value measures (B/P+E/P+CF/P+sales/P, stacked as separate "factors") | **REDUNDANT (fake diversification)** | Highly correlated multiples; averaging reduces noise, does not add independent information — a construction choice, not a second edge |
