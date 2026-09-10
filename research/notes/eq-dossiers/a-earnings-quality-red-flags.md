# Earnings Quality and Accounting Red Flags — Detection Literature, Then India

*Literature dossier, Track EQ, 2026-09-10. No web fetches — written from training
knowledge per instruction. Every claim carries **[LIT]**; a magnitude recalled with less
confidence than its citation gets **[LIT, LOW CONFIDENCE]**; a detail this dossier cannot
reconcile is tagged **[VERIFY: ...]** per CONTRACT §12. No desk numbers appear here:
`trial-ledger.md` and `RUNSHEET.md` were checked before writing and carry no run against
Sloan accruals, Beneish M-Score, DGLS F-Score, or India pledge statistics — a clean
literature-and-data-gap dossier, not a report on printed numbers. Piotroski's F-Score is
already treated as a value-trap filter in `val-dossiers/b-value-complementarity.md`
(§2, §5) and `fun-dossiers/d-quality-metric-canon.md`; this dossier does not repeat that
ground, only cross-references it (§3, §5). Beneish and India forensic anecdotes (Satyam,
IL&FS/DHFL/Yes Bank) appear briefly in `f-india-quality-data.md`; this dossier goes
deeper on detection mechanics and adds the pledge-mechanism cases that file doesn't cover.*

---

## 1. The accrual anomaly proper

**Sloan (1996), "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows
about Future Earnings?," *The Accounting Review* 71(3)** [LIT] is the foundational
result. Total accruals are defined on the balance-sheet approach as
`ΔNon-cash working capital − Depreciation`, scaled by average total assets, decomposing
earnings into a cash-flow component and an accrual component and testing which is more
persistent. Sloan's finding: the accrual component is **less persistent** than the
cash-flow component (next-period earnings load less on this year's accruals than on
this year's operating cash flow), but investors' pricing behaves as if they **fixate on
aggregate earnings** and fail to unpack this — "functional fixation" in the
accounting-theory vocabulary. A hedge portfolio long low-accrual/short high-accrual
firms earned roughly **10%/year** in the original 1962–1991 sample [LIT, LOW CONFIDENCE
on the exact decimal — the decile-monotone pattern and rough decade-average magnitude
are secure, the third significant digit is not]. One of the most-replicated anomalies in
accounting/finance.

**Decay.** A McLean-Pontiff (CONTRACT §5) case study in its own right: replication and
out-of-sample work through the 2010s (Green, Hand & Soliman and related papers) reports
the anomaly's magnitude **attenuated materially after the mid-2000s**, coincident with
rising hedge-fund/quant attention [LIT, LOW CONFIDENCE on the exact attenuation
percentage; direction and rough scale are secure]. This is the CONTRACT §5 "why does
this survive being known" test failing outright: no capacity limit or institutional
constraint blocks arbitrage capital from a signal built entirely from public
financial-statement line items, so any accrual-based signal here starts from a larger
haircut than the program's typical prior.

**Richardson, Sloan, Soliman & Tuna (2005), "Accrual Reliability, Earnings Persistence
and Stock Prices," *Journal of Accounting and Economics* 39(3)** [LIT] refine the
mechanism: they decompose total accruals by **estimation reliability** — cash-based
items (most reliable) through receivables/payables/inventory (moderate) to the most
subjective long-horizon estimates, e.g. goodwill/pension assumptions (least reliable) —
and show **the least-reliable components predict the largest subsequent negative
abnormal returns and the sharpest earnings reversals**, while cash-based components show
little mispricing [LIT]. This RSST decomposition (working-capital/non-current-operating/
financial buckets) is the standard refinement when the raw Sloan spread is too blunt; it
needs balance-sheet granularity §5(d) addresses directly.

**Xie (2001), "The Mispricing of Abnormal Accruals," *The Accounting Review* 76(3)**
[LIT] applies the modified Jones (1991) model — regressing total accruals
cross-sectionally on ΔSales-net-of-ΔReceivables and gross PP&E, with the residual read
as the "discretionary" (manager-controlled) component — and finds **Sloan's mispricing
concentrates in the discretionary component**, with the fitted ("non-discretionary")
component showing materially weaker predictability [LIT, LOW CONFIDENCE on the exact
split]. This strengthens the manipulation reading of the accrual anomaly and foreshadows
§2, which targets discretionary accruals directly.

**Fairfield, Whisenant & Yohn (2003), *The Accounting Review* 78(1)** [LIT] and
**Cooper, Gulen & Schill (2008), *Journal of Finance* 63(4)** [LIT] (the latter already
anchored in dossier b §3) argue the accrual anomaly is a **special case of a broader
total-asset-growth anomaly**: firms that grow balance sheets aggressively — via
accruals, capex, or financing — subsequently underperform, and asset growth
**subsumes, and in some specifications exceeds**, the narrower accrual measure [LIT].
FWY frame this as reduced future profitability (Sloan's own spirit); CGS frame it as a
broader cross-sectional regularity. Practical read: **total-asset-growth is a strict
superset of a narrow accruals screen**, and — via dossier b §3's CMA/HML redundancy
result — close to what Fama-French's CMA factor formalizes. Do not budget accruals and
asset-growth as two independent signals; they are one family at different resolutions.

---

## 2. The fraud / manipulation detection literature

**Beneish (1999), "The Detection of Earnings Manipulation," *Financial Analysts
Journal* 55(5)** [LIT] built the M-Score from a sample of identified earnings
manipulators matched against non-manipulators, via a probit/logit-style estimation on
eight indices, each a **year-over-year ratio** (values near 1.0 = no change):

- **DSRI** — Days' Sales in Receivables Index: (Receivables/Sales)ₜ÷ₜ₋₁. A large rise
  suggests revenue inflation (channel-stuffing, premature recognition).
- **GMI** — Gross Margin Index: Gross Marginₜ₋₁÷ₜ. Deteriorating margin is framed as
  manipulation pressure.
- **AQI** — Asset Quality Index: `[1 − (Current Assets+Net PP&E+Securities)/Total
  Assets]`, t vs. t−1. Rising "soft" (non-current, non-PP&E) asset share signals
  aggressive capitalization of costs that should be expensed.
- **SGI** — Sales Growth Index: Salesₜ÷ₜ₋₁. High growth is manipulation *pressure*, not
  manipulation itself — fast growers face the strongest incentive and easiest cover.
- **DEPI** — Depreciation Index: depreciation rate (Depreciation/(Depreciation+Net
  PP&E)) at t−1 vs. t. A falling rate suggests stretched asset lives.
- **SGAI** — SG&A Index: (SG&A/Sales)ₜ÷ₜ₋₁.
- **TATA** — Total Accruals to Total Assets: (Income from continuing ops − CFO)/Total
  Assets — the Sloan accrual measure by another name, the direct §1–§2 link.
- **LVGI** — Leverage Index: (Total Debt/Total Assets)ₜ÷ₜ₋₁.

The model: `M = −4.84 + 0.920·DSRI + 0.528·GMI + 0.404·AQI + 0.892·SGI + 0.115·DEPI −
0.172·SGAI + 4.679·TATA − 0.327·LVGI` [LIT, LOW CONFIDENCE on the exact coefficient
decimals — sign, magnitude and the eight-variable set are secure; the decimals should be
checked against the primary source before being hard-coded]. Published cutoff **M >
−2.22** flags a probable manipulator [LIT]; `d-quality-metric-canon.md` in this register
cites **−1.78**, a threshold circulating in practitioner restatements of the model
[LIT, LOW CONFIDENCE — this dossier cannot reconcile which is the original-paper number;
**[VERIFY: Beneish 1999 exact cutoff, reconcile −2.22 vs. −1.78]**].

**False-positive rate and post-2000 track record.** Beneish's own in-sample detection
rate was **roughly three-quarters of known manipulators flagged** [LIT, LOW CONFIDENCE],
but — the standard critique of a model trained on a matched fraud sample — the
**false-positive rate on the broader population is high**: fast-growing,
margin-improving, working-capital-intensive but entirely legitimate firms score as
"manipulators" because the ratios also describe honest aggressive growth [LIT]. It is
often cited as flagging **Enron** retroactively [LIT, LOW CONFIDENCE — a widely repeated
claim this dossier cannot verify as a genuine *prospective* catch before 2001, only that
retrospective application to Enron's restated financials flags it], but has no
comparable prospective track record on the next decade's frauds; academic assessment
treats it as a **noisy screening heuristic**, not a reliable standalone detector [LIT].

**Dechow, Ge, Larson & Sloan (2011), "Predicting Material Accounting Misstatements,"
*Contemporary Accounting Research* 28(1)** [LIT] build the F-Score on the SEC's AAER
sample (formally identified misstatements — cleaner than Beneish's hand-identified
sample), adding three families beyond accrual quality: **(i) accrual quality** —
RSST-style change in net operating assets; **(ii) off-balance-sheet activity** —
leases, SPEs, receivables securitization — catching manipulation none of Beneish's
ratios can see; **(iii) market/nonfinancial incentives** — abnormal pre-period stock
performance, plus employee-count growth vs. asset growth (a real-activity check: growth
without matching headcount is a soft-asset-inflation tell, operationally sourced rather
than accounting-sourced). DGLS report the combined score **materially improves AAER
classification versus Beneish alone** [LIT, LOW CONFIDENCE on the exact improvement].

**The critical distinction — two different claims.** Both scores are built to predict
**whether a firm is manipulating/misstating** — a label from SEC enforcement or ex-post
identification. DGLS additionally find modest evidence of a **separate** claim: firms
scoring high subsequently earn **lower abnormal stock returns** — the market
under-prices the misstatement probability [LIT, LOW CONFIDENCE on the spread]. Worth
stating plainly because practitioner writing blurs the two: **"detects manipulation" and
"predicts underperformance" are not the same claim**, and the return-predictability
result is a secondary, weaker-evidenced add-on to both papers' primary (classification)
contribution. Any signal built from Beneish/DGLS components should be pre-registered
against the *return* claim specifically, not assumed to inherit the stronger *detection*
evidence base.

---

## 3. Cash-flow-based quality

**Cash conversion** — most commonly CFO/NI, sometimes CFO/EBITDA — is the practitioner
shorthand for "how much of reported profit is actually cash." Persistently below 1.0,
net income is running ahead of operating cash generation — mechanically almost
identical to Sloan's high-accrual firm (TATA = (NI−CFO)/Assets is the accrual measure;
CFO/NI is a ratio-form restatement of the same gap). "Quality of earnings" in
equity-research practice generally means exactly this ratio, often trend-checked (a
falling ratio over several quarters is more alarming than one low reading). **Ball &
Shivakumar (2005/2006), on accounting conservatism / asymmetric timeliness** [LIT]
supply the theory for why a *persistent* CFO<NI gap should matter: conservative
accounting recognizes economic losses immediately but economic gains only as realized in
cash — an asymmetric-timeliness property testable via earnings' differential response to
negative vs. positive stock returns. Low asymmetric timeliness (gains and losses
recognized at similar speed) implies more upward earnings management through the
accrual process conservatism is meant to constrain [LIT].

**What the evidence actually supports.** Distinguishing this from Piotroski (dossier b):
his F-Score treats CFO>NI as one of nine signals **conditioned on being inside the
already-cheap value universe**, validated as improving returns *within that subset*.
The broader cash-conversion literature is thinner: direct evidence that a low CFO/NI
ratio predicts **future abnormal returns unconditionally** (the whole market, not just
value stocks) is considerably weaker than the evidence it predicts **future earnings
reversals, restatement risk, and distress/bankruptcy risk** [LIT, LOW CONFIDENCE — a
qualitative characterization of a diffuse literature]. Cash conversion is well evidenced
as a **risk/distress and earnings-persistence predictor**; as a **standalone
unconditional return predictor** it is closer to Sloan's accrual result restated in
ratio form (inheriting that anomaly's decay caveat, §1) than a distinct signal. Treat it
as: (a) subsumed by the Hribar-Collins accrual construction (§1) when unconditional, and
(b) genuinely useful only **as a distress/trap screen conditioned on other
information** — Piotroski's architecture, not a new one.

---

## 4. Governance-adjacent red flags

Four commonly cited "red flag" items have real academic footprints, but the
return-prediction evidence for most is thin relative to the accrual and
fraud-detection literatures above.

**Auditor changes / qualified opinions.** Going-concern opinions and sudden
auditor-client separations are widely used in practitioner due diligence. The evidence
connects them reasonably well to elevated **distress and delisting risk** [LIT, LOW
CONFIDENCE], but direct evidence an auditor change alone predicts abnormal *stock
returns* — rather than co-occurring with already-observable fundamental deterioration —
is **[LIT, LOW CONFIDENCE]** at best: a risk-avoidance screen, not a documented alpha
source.

**Related-party transactions (RPTs).** **Johnson, La Porta, Lopez-de-Silanes & Shleifer
(2000), "Tunneling," *American Economic Review* 90(2)** [LIT] formalize how controlling
shareholders in concentrated-ownership systems extract value via RPTs (transfer
pricing, non-market asset sales, intercorporate loans) — directly relevant to India's
promoter-controlled structure (§5). Follow-on Asia-focused work (Cheung, Rau &
Stouraitis and related studies) [LIT, LOW CONFIDENCE on citations/magnitudes] finds
RPT-heavy firms show **lower valuations and, in some samples, weaker subsequent
performance** around RPT announcements — small samples, disclosure quality varies by
jurisdiction: treat RPT intensity as a **plausible-mechanism, low-confidence-magnitude**
red flag, a qualitative screen rather than a sized factor.

**Off-balance-sheet financing.** DGLS (§2) builds this into the F-Score as a distinct
component — a team judging it necessary to add what the eight Beneish ratios cannot see
is itself evidence this is a genuinely separate manipulation channel [LIT]. Standalone
evidence that off-balance-sheet intensity predicts returns on its own is thin [LIT, LOW
CONFIDENCE] — studied mostly as a composite component, not an independent signal.

**Restatement history.** The best-evidenced item here, but an *event-study* claim, not
an ex-ante one: restatement-announcement work (Palmrose, Richardson & Scholz and
related literature) [LIT, LOW CONFIDENCE on citations] documents significant
**negative announcement-period abnormal returns**, high-single-digit percent ranges
commonly cited [LIT, LOW CONFIDENCE on the exact number]. That shows the market is
surprised and penalizes restaters *at disclosure* — it does not establish that a firm's
*prior* restatement history predicts *future* returns; the ex-ante version is far less
developed than the event-study version. All four items: legitimate
**risk-avoidance / due-diligence screens**, none approaching the accrual or
Beneish/DGLS depth of *return-prediction* evidence — size them, if at all, as Tier-C
reduce-only filters (CONTRACT §4), never standalone return sources.

---

## 5. India specifics

**(a) Promoter share pledging — India's most distinctive, most measurable governance red
flag.** Promoter pledging is genuinely unusual at India's scale: concentrated
family/promoter control blocks are pledged as collateral against personal or
group-company borrowing far more commonly, and at far higher aggregate levels, than in
developed-market ownership structures, where control blocks are rarely leveraged this
way. It is also an unusually clean data object for this program: a **mandatory SEBI
disclosure** under the shareholding-pattern/takeover-code framework, filed quarterly by
regulatory requirement rather than voluntarily — unlike almost every other item in this
dossier, **genuinely point-in-time by construction**, on a fixed regulatory calendar
independent of restatement risk.

**The mechanism** is a reflexive spiral, and it is the mechanism, not any single
company's story, that the desk should trust: a promoter pledges shares as loan
collateral; if the price falls far enough, the lender issues a margin call; if the
promoter cannot post more collateral, the lender invokes the pledge and sells the
shares in the open market, pushing the price down further and potentially triggering
the next tranche's call — a self-reinforcing decline **independent of the underlying
business's operating performance**. This is a governance/liquidity-structure red flag,
not a fundamentals-quality one: a company can have clean accrual accounting and still
suffer a pledge-driven collapse, and a heavily pledged holding can trade normally for
years if price never approaches the margin-call threshold.

Several 2023–2025 India-focused papers examine pledging's association with crash risk
and find it **positively associated with future crash risk and negatively associated
with subsequent financial performance** [LIT, LOW CONFIDENCE on exact magnitudes and
specific papers] — directionally consistent with the mechanism, though a young
literature relative to the decades-deep US work in §1–§2.

**Case examples — explicitly [CASE-STUDY LORE, not a statistical claim].** Stories
widely reported in Indian financial media around **Zee Entertainment/Essel Group**,
**DHFL**, **Yes Bank**, various **Anil Ambani (Reliance ADAG) group companies**, and
**Café Coffee Day** are commonly invoked to illustrate the pledge-margin-call spiral
above. This dossier asserts **no specific fact** about any of these companies as
verified — details and causal attribution are contested or litigated in some instances,
and several involve additional mechanisms beyond pledging (DHFL/Yes Bank appear in
`f-india-quality-data.md` mainly through an ALM/balance-sheet lens, not a pledge lens —
the two dossiers describe different facets of overlapping situations, not duplicate
ground). These names are cited **solely as widely-reported illustrations of the
mechanism**, the way a textbook cites Enron for off-balance-sheet manipulation without
re-litigating Enron's accounting. Nothing here should be read as a confirmed factual
claim about any named company; the design implication rests entirely on the mechanism.

**(b) Indian-specific accrual / related-party issues.** Beyond §4's general RPT
literature, structural patterns recur in Indian mid-cap governance-failure narratives,
described at the **mechanism level only**, with no unverified allegation against any
named company: **promoter-entity loans** (the listed company advances loans to
promoter-controlled unlisted entities, opaquely disclosed and of uncertain
recoverability — inflating assets without economic substance); **corporate guarantees
to group companies** (an off-balance-sheet contingent liability structurally like the
DGLS component in §2; Companies Act §186 and SEBI LODR are the relevant disclosure
hooks, enforcement historically uneven); and **working-capital-loop concerns** (revenue
and receivables round-tripping with related unlisted counterparties, inflating both
top line and accruals — India's instantiation of the DSRI/AQI-style manipulation
Beneish targets, common in mid-cap fraud narratives of the past decade). These are
mechanism descriptions from the general governance/forensic literature, not claims
about any specific company.

**(c) The Ind-AS transition and accrual-measure comparability.** India's mandatory
transition from Indian GAAP to Ind-AS (converged IFRS) phased in starting **FY2016–17**
for the largest listed companies, extending to smaller entities over the following
one to two years — a material comparability break for **every** accrual-based measure
here: fair-value measurement for several asset classes, an expected-credit-loss
impairment model for financial assets/receivables (affecting the receivables base
DSRI-type measures would use, were receivables available — (d) below), revised
revenue-recognition rules (Ind-AS 115/IFRS 115, phased in a year or two later, changing
recognition timing for multi-element contracts), and first-time-adoption reconciliation
entries that can themselves look like one-off accrual spikes. **Any accrual, growth, or
margin measure spanning the FY2016–17 boundary compares two accounting regimes, not one
consistent series** — a testable analogue of CONTRACT Known Prior #7 (restated
fundamentals bias backtests upward), here a structural regime break rather than a
restatement: any accrual-family design must include an explicit transition dummy/regime
split, or restrict to a post-transition sample, pre-registered explicitly.

**(d) What the incoming handoff can and cannot construct — the data-gap map.** Mapping
the handoff schema (`handoff-prompt-india-fundamentals.md`, P1 fields: `isin, ticker,
company_name, fiscal_quarter_end, filing_date, statement_basis, total_assets,
total_equity, total_debt, cash_and_equivalents, revenue, ebit, net_income, cfo,
shares_outstanding, source_url`; P5 fields: `promoter_pct,
promoter_pledged_pct_of_promoter_holding`) against every component discussed above:

*Buildable from P1 alone, today, once the handoff lands:*
- **TATA / Sloan-Hribar-Collins accruals** = `(net_income − cfo) / average(total_assets)`
  — the modern cash-flow-statement-based accrual construction (Hribar & Collins, 2002,
  which supersedes the original balance-sheet approach precisely because it avoids
  M&A/discontinued-operations noise) is directly computable from three P1 fields already
  specified.
- **Total asset growth** (Cooper-Gulen-Schill, §1) = `total_assets_t / total_assets_{t-1}
  − 1` — directly computable, and per §1 a strict superset of the narrower accrual
  signal.
- **LVGI** (Beneish leverage index) = `(total_debt/total_assets)_t ÷
  (total_debt/total_assets)_{t-1}` — directly computable.
- **SGI** (Beneish sales-growth index) = `revenue_t / revenue_{t-1}` — directly
  computable.
- **A rough GMI-proxy**, not the literature's true gross-margin index (which needs
  COGS, absent from P1): an **EBIT-margin index** using `ebit/revenue` in place of gross
  margin — a materially different, noisier construct (EBIT margin nets out SG&A and
  D&A that gross margin does not), usable only as a labeled approximation, never
  presented as GMI itself.
- **Cash conversion (CFO/NI)** = `cfo / net_income` — directly computable.
- **Net share issuance** (Pontiff-Woodgate style, dossier b §5) — buildable by combining
  the `shares_outstanding` field in P1 with adjusted prices in P4, a genuine
  cross-file construction this program should register explicitly.
- **Promoter pledge level and pledge acceleration** (`promoter_pct`,
  `promoter_pledged_pct_of_promoter_holding`, and their quarter-over-quarter change) —
  directly computable from P5 alone, and — per (a) above — genuinely point-in-time by
  regulatory construction, unlike every field above, which needs the standard 30–45 day
  filing-lag buffer and carries the Ind-AS comparability caveat in (c).

*NOT buildable from P1–P6 — a precise gap list:*
- **DSRI** (Beneish) — needs a receivables balance; P1 has no `accounts_receivable`
  field.
- **AQI** (Beneish) — needs a current-assets / net-PP&E / securities breakdown of total
  assets; P1 gives only the single aggregate `total_assets` figure, no sub-line
  granularity.
- **SGAI** (Beneish) — needs SG&A expense; P1 has no operating-expense breakdown below
  `ebit`.
- **DEPI** (Beneish) — needs depreciation expense (or the depreciation rate against net
  PP&E); P1 has no D&A line, and therefore true **CFO/EBITDA** (as distinct from the
  buildable CFO/NI) is also not constructible, since EBITDA requires adding back D&A to
  EBIT.
- Because DSRI, AQI, SGAI and DEPI are four of the model's eight required components,
  **the full Beneish M-Score is not constructible from P1** — only a desk-original
  four-input composite (TATA, LVGI, SGI, EBIT-margin-proxy-GMI) inspired by, but
  explicitly not equivalent to, the published M-Score.
- **RSST reliability decomposition** (Richardson-Sloan-Soliman-Tuna, §1) — needs the
  working-capital / non-current-operating / financial-asset sub-decomposition of the
  balance sheet; not available at P1's aggregation level.
- **Xie's discretionary-accruals (modified Jones) model** — needs receivables (for the
  ΔSales-net-of-ΔReceivables regressor) and gross PP&E; neither is in P1.
- **DGLS off-balance-sheet component** — needs lease/securitization/special-purpose-
  entity disclosure; not in P1–P6.
- **DGLS nonfinancial-measure component** — needs headcount or unit-volume data; not in
  P1–P6.
- **Auditor opinion/qualification flags and restatement-history flags** (§4) — not
  specified anywhere in P1–P6; would require a filing-text or audit-report field the
  handoff does not ask for.
- **Related-party-transaction values** (§4, §5b) — not specified in P1–P6; would require
  footnote-level disclosure data outside this handoff's scope entirely.

---

## 6. Edge candidates for this desk

| Candidate | Mechanism | Magnitude [LIT+hedge] | Horizon | Data needed | Kill condition |
|---|---|---|---|---|---|
| Hribar-Collins accruals (NI−CFO)/assets | Functional fixation on aggregate earnings vs. persistence of accrual component (Sloan) | ~10%/yr decile spread in the original sample, materially decayed since [LIT, LOW CONFIDENCE]; no strong survival argument under CONTRACT §5 | 12m | P1 (`net_income`, `cfo`, `total_assets`) — buildable immediately | Spread is flat or sign-inconsistent once split pre/post FY2016-17 Ind-AS regime |
| Total asset growth | Superset of accruals; overinvestment/q-theory (Cooper-Gulen-Schill; Titman-Wei-Xie) | Comparable-to-larger spread than raw accruals [LIT, LOW CONFIDENCE]; likely redundant with the desk's existing CMA/value-composite work (dossier b §3) | 12m | P1 (`total_assets`) — buildable immediately | Spread does not survive once double-counted against the price-only value composite already in the design |
| Promoter pledge level × acceleration, interacted with falling price | Reflexive margin-call spiral — governance/liquidity risk, not a priced distress factor (mechanism in §5a) | Directional only; no India basis-point figure this dossier can cite with confidence [LIT, LOW CONFIDENCE] | Event-driven / discrete | P5 (`promoter_pct`, `promoter_pledged_pct_of_promoter_holding`) — PIT-clean, no lag buffer needed | The interaction fires no more often than a naive falling-price-alone screen once backtested against P3's delisting registry |
| Desk-original 4-input composite (TATA + LVGI + SGI + EBIT-margin-proxy) | Beneish-inspired manipulation-pressure proxy, explicitly NOT the published M-Score (§5d gap list) | Not sizeable from any published number — this is a new construct, not a replication | 12m | P1 fields only | Composite does not separate P3's actual delistings-for-cause from ordinary business failure |
| Cash conversion (CFO/NI) as an unconditional screen | Same mechanism as accruals, ratio form (§3) | Weak as a standalone return predictor; better evidenced as a distress/reversal predictor [LIT, LOW CONFIDENCE] | 12m | P1 (`cfo`, `net_income`) | No incremental return signal once the Hribar-Collins accrual measure above is already in the design (near-duplicate, per §3) |

**What is NOT buildable even after the handoff lands** (full list and reasons in §5d;
summarized): the full Beneish M-Score (blocked on DSRI/AQI/SGAI/DEPI — receivables,
CA/PP&E/securities breakdown, SG&A, depreciation, none in P1); true CFO/EBITDA (no D&A
line); the RSST accrual-reliability decomposition (no WC/NCO/FIN sub-split); Xie's
modified-Jones discretionary-accruals model (no receivables/gross PP&E); DGLS's
off-balance-sheet and nonfinancial-measure components (no lease/SPE or headcount/unit
data); auditor-opinion, qualification, and restatement-history flags (no filing-text
field in the schema); and related-party-transaction values (footnote-level, out of
scope). Any of these judged essential later is a **new handoff-schema ask**, not
something to approximate from P1–P6 by construction choice.
