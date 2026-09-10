# Beyond Beneish/DGLS — Practitioner Frameworks, Distress Scores, and Market-Based
# Manipulation Signals

*Literature dossier, Track EQ part 2, 2026-09-10. No web fetches — written from training
knowledge per instruction. Every claim carries **[LIT]**; a magnitude recalled with less
confidence than its citation gets **[LIT, LOW CONFIDENCE]**; a detail this dossier cannot
reconcile is tagged **[VERIFY: ...]** per CONTRACT §12. No desk numbers appear here — a
clean literature-and-data-gap dossier, extending eq-dossiers/a (Sloan/RSST/Xie/asset-growth,
Beneish/DGLS, cash conversion, auditor/RPT/restatement flags, promoter pledging) without
repeating its ground. Distinct organizing point of this dossier: red-flag detection splits
into three different KINDS of evidence — (a) ratio-based SCORES built from structured
financial-statement data (Altman Z, Ohlson O, Montier C — cousins of Beneish/DGLS already
covered), (b) a qualitative TECHNIQUE checklist requiring footnote-level reading, not a
formula (Schilit's Financial Shenanigans), and (c) MARKET/BEHAVIORAL signals that use no
accounting ratio at all (insider selling, short interest, options-grant timing, earnings-
call linguistics). The India buildability question is answered separately for each, per
the same P1-P6 handoff schema eq-dossiers/a mapped.*

---

## 1. Schilit's Financial Shenanigans — the practitioner canon, technique not formula

**Howard Schilit, *Financial Shenanigans* (1993, with later editions and a 2018 update
with Jeremy Perler)** [LIT] is the standard practitioner (not academic-econometric)
taxonomy — a checklist of manipulation TECHNIQUES read from footnotes and MD&A, not a
regression-estimated score. Seven categories, later grouped into revenue tricks,
expense tricks, and one-time-item tricks:

1. **Recording revenue too soon or of questionable quality** — bill-and-hold sales
   (recognizing revenue before goods ship), channel stuffing (pushing distributors to
   over-order near quarter-end), recognizing revenue while material future obligations
   (installation, service) remain unperformed.
2. **Recording bogus or fictitious revenue** — round-tripping (reciprocal transactions
   with no economic substance, each side recording the other's payment as revenue),
   booking investment gains or one-off items as operating revenue.
3. **Boosting income with one-time or unsustainable gains** — asset sales, investment
   gains, litigation settlements reclassified into the operating income line.
4. **Shifting current expenses to a later (or earlier) period** — capitalizing costs
   that should be expensed (the AQI mechanism Beneish already targets, dossier a §2),
   under-depreciating assets, delaying obviously-needed impairments.
5. **Failing to record or improperly reducing liabilities** — under-reserving for
   warranties/bad debts/litigation, or releasing prior-period reserves into income when
   convenient (the "cookie jar" on the liability side).
6. **Shifting current revenue to a later period** — holding back revenue in a strong
   quarter (deferred-revenue games) to smooth into a weak one — cookie-jar reserves on
   the revenue side, the mirror of #5.
7. **Shifting future expenses into the current period as a special charge** — "big
   bath" restructuring: kitchen-sinking every discretionary write-off into one bad
   quarter (commonly at a CEO transition) so future quarters look artificially strong
   by comparison.

**Why this matters for the desk's construction choices.** Beneish's eight ratios and
Montier's six flags (§3 below) are attempts to make several of these techniques
QUANTIFIABLE from structured data — DSRI/channel-stuffing maps to #1, TATA/AQI maps to
#4, LVGI is orthogonal (financing, not an earnings technique). But #2 (round-tripping),
#5/#6 (reserve smoothing), and #7 (big-bath timing) are NOT well-captured by any ratio
in eq-dossiers/a's list — they require reading the actual restructuring-charge and
reserve-rollforward footnotes, which no aggregate financial-statement field (Beneish's,
Montier's, or the India handoff's P1) can substitute for. **This is the honest boundary
of every quantitative red-flag score covered across both dossiers: they are proxies for
some Schilit techniques, not detectors of all seven.**

---

## 2. Bankruptcy/distress scores — a different target than manipulation, often conflated

Beneish/DGLS (dossier a §2) predict MANIPULATION. These next two predict FINANCIAL
DISTRESS/BANKRUPTCY — a related but distinct claim, worth keeping separate exactly as
dossier a §2 separated "detects manipulation" from "predicts returns."

**Altman Z-Score (1968), *Journal of Finance* 23(4)** [LIT] — the original
multiple-discriminant-analysis bankruptcy predictor for public manufacturers:
`Z = 1.2·(WC/TA) + 1.4·(RE/TA) + 3.3·(EBIT/TA) + 0.6·(MVE/TL) + 1.0·(Sales/TA)`
[LIT, LOW CONFIDENCE on the exact coefficient decimals — the five-ratio structure and
each ratio's rough weight-ordering are secure]. Zones: Z > 2.99 "safe," 1.81–2.99
"grey," Z < 1.81 "distress" [LIT, LOW CONFIDENCE on the exact cutoffs]. Altman later
published **Z'** (book value of equity replacing market value, for private firms) and
**Z''** (drops Sales/TA entirely, recalibrated — aimed at non-manufacturers and
EMERGING MARKETS specifically) [LIT, LOW CONFIDENCE on the Z''-EM coefficients] —
directly the India-relevant variant, though this dossier cannot cite its exact
coefficients with confidence.

**Ohlson O-Score (1980), *Journal of Accounting Research* 18(1)** [LIT] — a logit
(not discriminant-analysis) alternative, using log(Total Assets), Total
Liabilities/Total Assets, Working Capital/Total Assets, Current Liabilities/Current
Assets, Net Income/Total Assets, CFO/Total Liabilities, a funds-flow/NI-change term,
and dummy variables for negative equity and two consecutive years of losses [LIT, LOW
CONFIDENCE on the exact nine-variable list and coefficients]. Ohlson's own methodological
point — logit avoids the distributional assumptions discriminant analysis requires — is
a genuine improvement Altman's Z lacks, and is why O-Score is still commonly taught
alongside Z rather than treated as redundant with it.

**India buildability (P1-P6 schema, same discipline as dossier a §5d):** both scores
need **working capital** (current assets minus current liabilities) and Z needs
**retained earnings** specifically — P1 gives only the single aggregate `total_assets`
and `total_equity` figures, with no current-asset/current-liability sub-line and no
retained-earnings component of equity. **Neither Z-Score nor O-Score is fully
constructible from P1** — the same class of gap dossier a found for DSRI/AQI/SGAI/DEPI.
What IS buildable: EBIT/TA and Sales/TA (both P1 fields present) and a MVE/TL proxy
(`shares_outstanding` x adjusted price from P4, divided by `total_debt` as a stand-in
for total liabilities — an approximation, `total_debt` is not `total_liabilities`,
stated as a construction caveat); CFO/TL similarly approximable. A genuine
**Z-lite/O-lite composite** (EBIT/TA, Sales/TA, MVE/proxy-TL, CFO/proxy-TL) is
registrable on arrival, explicitly labeled as neither the true Altman nor Ohlson score.

---

## 3. Montier's C-Score — the practitioner's Beneish, and independent corroboration

**James Montier (GMO), the "C-Score"** (developed and popularized in GMO client notes
and Montier's *Value Investing* writings, circa 2008) [LIT, LOW CONFIDENCE on the exact
publication] — six binary red flags, summed 0-6, higher = more manipulation-likely:

1. A growing gap between net income and cash flow from operations (the same TATA/
   Hribar-Collins mechanism, dossier a §1 and EQ-D1's e1).
2. A growing gap in Days Sales Outstanding (receivables growing faster than sales — the
   same economic content as Beneish's DSRI, in a growth-rate rather than level form).
3. Growing Days Sales of Inventory (an inventory-buildup analogue Beneish's eight ratios
   do not have at all — a genuinely additional signal, not already covered).
4. Growing "other assets" relative to sales (a soft-asset-capitalization flag, close to
   Beneish's AQI in spirit).
5. Declining depreciation relative to gross property/plant/equipment (near-identical to
   Beneish's DEPI).
6. High total asset growth (the Cooper-Gulen-Schill / Fairfield-Whisenant-Yohn measure
   already anchored in dossier a §1, cited here as independent practitioner
   corroboration that asset growth belongs on every manipulation-adjacent checklist,
   not only the academic one).

**Why cite this alongside Beneish rather than treat it as redundant:** C-Score is
independent PRACTITIONER validation (a buy-side risk desk's own checklist, not an
academic paper) of the SAME handful of mechanisms — cash/earnings divergence, asset
growth, under-depreciation — the desk has already found evidence for in EQ-D1. Its one
genuinely NEW ingredient not already in this program's vocabulary is **Days Sales of
Inventory** (inventory building up faster than sales, a classic sign of channel-stuffed
or unsellable goods sitting on the balance sheet).

**India buildability:** items 1 and 6 are already covered (EQ-D1's TATA_proxy and the
Cooper-Gulen-Schill asset-growth line, both buildable from P1 per dossier a §5d). Items
2–5 all need line-item detail P1 does not carry — receivables (item 2), inventory (item
3), an "other assets" breakdown (item 4), and gross PP&E/depreciation (item 5, the exact
DEPI gap dossier a §5d already flagged). **C-Score is 2-of-6 buildable from the current
P1 schema** — the same ceiling-shape finding as Beneish's 4-of-8, from an entirely
independent framework, which strengthens rather than merely repeats the earlier
correction: the India handoff schema is structurally too aggregated for ANY of the
established manipulation-detection scores to run in full, not just Beneish's.

---

## 4. Benford's Law — a genuinely different KIND of test (distributional, not ratio)

**Benford's Law** (the empirical finding that naturally-occurring numerical datasets
show a logarithmic, not uniform, distribution of leading digits — "1" leads roughly 30%
of the time, "9" under 5%) [LIT] has a distinct forensic-accounting literature, most
associated with **Mark Nigrini's** applied work (*Digital Analysis Using Benford's Law*
and related) [LIT, LOW CONFIDENCE on specific citations], used by tax authorities and
forensic auditors to flag statistically improbable digit patterns in reported figures —
a genuinely different detection PRINCIPLE than every ratio-based score above: it does
not ask whether a number's ECONOMIC RELATIONSHIP to another number looks wrong (Beneish,
Altman, Montier all do this), it asks whether the SHAPE of the number itself looks
fabricated versus organically generated. Academic work extending this to financial-
statement fraud specifically (examining Benford-deviation patterns around SEC AAER
firms) exists [LIT, LOW CONFIDENCE — this dossier cannot cite specific papers with
citation-level confidence].

**Feasibility on this desk's data, stated honestly:** Benford tests need MANY digits
across MANY reported line items — the intended use case is a single company's full
general ledger or a complete filing's line-item detail, not a handful of aggregate
figures. P1's schema (total_assets, total_equity, total_debt, cash, revenue, ebit,
net_income, cfo — eight numeric fields per company-quarter) gives far too few
observations per company to run a within-company digit test with any power.
**[VERIFY: whether a POOLED, cross-sectional Benford test — stacking all companies'
P1 figures together as a data-quality/reporting-irregularity screen, rather than a
per-company fraud detector — is a meaningfully different and weaker claim than the
literature's intended use, or whether it is simply not worth registering at all given
the field count]**. Recorded here as a technique this program is aware of and has
explicitly declined to size, rather than silently omitted.

---

## 5. Market-based and behavioral signals — no accounting ratio at all

A distinct family: these use trading, disclosure, or communication DATA rather than
financial-statement ratios, and are frontier/quant-desk techniques rather than the
classical academic canon above.

**Abnormal insider selling.** The broader insider-trading-predicts-returns literature
(**Seyhun's** body of work on insider transactions [LIT]) has a specific fraud-adjacent
branch examining whether insiders sell disproportionately AHEAD of subsequently-
revealed bad news, restatements, or fraud [LIT, LOW CONFIDENCE on specific citations] —
directionally plausible (insiders know first) but confounded by routine, pre-scheduled
10b5-1 selling plans that carry no informational content; disentangling the two needs
transaction-level insider-filing data this program does not have specified anywhere in
P1-P6 (a genuine new data ask, distinct from P5's promoter-PLEDGE data, which is a
collateral-financing disclosure, not a buy/sell transaction record).

**Short interest as a forensic signal.** **Dechow, Lawrence & Ryans (2016), "Who Blows
the Whistle on Corporate Fraud?", *Journal of Accounting Research* 54(2)** [LIT, LOW
CONFIDENCE on the exact title/year] examine which market participants (short sellers,
analysts, auditors, the SEC, media, employees) first detect frauds, and — the citable
point — find short sellers are frequently among the EARLIEST, ahead of formal
enforcement action, consistent with short sellers doing genuine forensic-accounting
work rather than only directional betting. Not buildable from P1-P6 (needs short-
interest/securities-lending data, not specified; NSE/BSE F&O open-interest data is a
plausible future proxy, distinct from a true short-interest series).

**Auditor fee anomalies.** Post-Enron-era literature (**Frankel, Johnson & Nelson
(2002)** is the standard citation [LIT, LOW CONFIDENCE]) linked unusually high
non-audit/consulting fees paid to a company's own auditor, relative to audit fees, to
auditor-independence erosion and subsequent earnings management — a distinct
governance-adjacent flag from the auditor-CHANGE flag already covered in dossier a §4.
Needs audit-fee disclosure detail not in P1-P6.

**Options-grant timing ("spring-loading"/backdating).** **Erik Lie (2005), "On the
Timing of CEO Stock Option Awards," *Management Science* 51(5)** [LIT] and follow-on
work (Heron & Lie) [LIT, LOW CONFIDENCE] documented statistically improbable "luck" in
historical US option-grant dates (grants dated right before price run-ups, far more
often than chance) — a genuine governance red flag with a clean statistical test
(grant-date return patterns), though largely a mid-2000s US regulatory episode
(SEC enforcement followed, changing disclosure rules). Conceptually portable to India's
ESOP regime but needs grant-date/strike-price disclosure data not in P1-P6.

**Textual and vocal deception cues in earnings calls.** **Larcker & Zakolyukina (2012),
"Detecting Deceptive Discussions in Conference Calls," *Journal of Accounting Research*
50(2)** [LIT] find linguistic markers — fewer first-person pronouns, more extreme
positive-emotion language, fewer references to shareholder/generic-business terms,
more hesitation markers — statistically associated with calls that PRECEDE a later
restatement/AAER action. A companion literature on VOCAL cues (**Hobson, Mayew &
Venkatachalam**, on vocal pitch/stress in earnings calls as deception markers) [LIT,
LOW CONFIDENCE on the exact citation] extends this to audio, not just transcript text.
This is a genuinely different MODALITY (NLP/audio on earnings-call recordings/
transcripts) — not buildable from P1-P6 at all, but a real, actively-used quant-desk
technique and a plausible future data ask distinct from every field this handoff
specifies (NSE-listed company earnings-call transcripts are frequently public,
unlike short-interest or insider-transaction data, making this arguably the MOST
realistically obtainable of the five market-based signals in this section).

---

## 6. Summary table — every framework in both dossiers, one place

| Framework | Kind | Target claim | India-buildable from P1-P6? |
|---|---|---|---|
| Sloan accruals / Hribar-Collins TATA (dossier a §1) | ratio | mispricing of accrual component | YES |
| RSST reliability decomposition (dossier a §1) | ratio | which accrual sub-component mispriced | NO (needs WC/NCO/financial sub-split) |
| Xie discretionary accruals / modified Jones (dossier a §1) | ratio | manager-controlled accrual component | NO (needs receivables, gross PP&E) |
| Asset growth (CGS/FWY, dossier a §1) | ratio | overinvestment / accrual superset | YES |
| Beneish M-Score (dossier a §2) | ratio | manipulation classification | PARTIAL (4 of 8 components) |
| DGLS F-Score (dossier a §2) | ratio | misstatement classification | NO (needs lease/SPE, headcount data) |
| Cash conversion CFO/NI (dossier a §3) | ratio | earnings quality / distress | YES |
| Altman Z / Z'' (this dossier §2) | ratio | bankruptcy risk | PARTIAL (2 of 5 ratios; WC, RE blocked) |
| Ohlson O-Score (this dossier §2) | ratio | bankruptcy probability (logit) | PARTIAL (similar gap) |
| Montier C-Score (this dossier §3) | ratio | manipulation-pressure checklist | PARTIAL (2 of 6) |
| Benford's Law (this dossier §4) | distributional | digit-pattern fabrication | UNCLEAR — likely underpowered on 8 fields |
| Schilit's 7 Shenanigans (this dossier §1) | technique/qualitative | footnote-level manipulation reading | NO (needs footnote/MD&A text) |
| RPTs, auditor changes, restatement history (dossier a §4) | governance | distress/risk screen | NO (footnote/filing-text detail) |
| Promoter pledging (dossier a §5a) | governance, India-specific | reflexive crash mechanism | YES (P5) |
| Insider selling, short interest, auditor fees, options timing, call linguistics (this dossier §5) | market/behavioral | fraud detection via non-accounting data | NO (all need data sources outside P1-P6 entirely) |

**The honest ceiling, stated once for both dossiers:** of roughly a dozen major
red-flag/manipulation frameworks in the literature, only THREE are fully buildable from
the currently-specified India handoff schema (Sloan/Hribar-Collins accruals, asset
growth, cash conversion), plus one India-specific governance marker (promoter pledging)
outside the accounting-ratio family entirely. Everything else is partial-to-zero
without either a richer P1-schema ask (line-item balance-sheet/income-statement detail:
receivables, inventory, PP&E gross/depreciation, SG&A, current-asset/liability splits)
or an entirely separate data source (footnote text, insider transactions, short
interest, audit fees, ESOP grants, call transcripts).
