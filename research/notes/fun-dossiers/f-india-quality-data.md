# Dossier F — India Quality/Growth/ROCE Evidence + the India Fundamentals Data Map

*Growth/ROIC/quality deep-dive, 2026-09-08; Sonnet research agent, adversarially
consumed. Every claim [LIT], approximate; TEST lines say what converts it to a print.*

## 1. The India quality premium

- **NSE strategy indices** (NIFTY100 Quality 30, NIFTY200 Quality 30 ~2018 launch,
  Midcap150 Quality 50 ~2021): composite = ROE + low leverage + earnings stability;
  factsheets show a few hundred bps/yr over parents — BUT the quoted history is
  overwhelmingly **pre-launch backfill** on restated financials with today's
  methodology. None of the pre-launch years are out-of-sample. TEST: compare ONLY the
  live post-launch segments vs parents; cross-check vs a desk-built PIT score.
- **Academic**: the vaulted IIMA (Agarwalla-Jacob-Varma ~2013) library is FF3+momentum —
  **no profitability/quality factor** [confirmed against the vaulted file's columns:
  SMB/HML/WML/MF/RF only]. Rajan Raju [LIT, LOW CONFIDENCE] a literature lead only.
- **The era-concentration warning (highest-confidence item)**: coffee-can/compounder
  investing (Mukherjea et al. ~2018) dominated 2010-2020, then the same
  strategies/funds underperformed badly 2021-2024 amid the value/PSU/cyclical rally
  [LIT, press]. A decade of dominance + a multi-year drawdown = the factor must be
  admitted regime-conditionally or not at all. TEST: reconstruct on the survivor panel
  + post-2021 extension; separate premium from multiple-rerating.

## 2. Why India differs structurally

- **Promoter ownership** ~45-50% median stake [LIT, SEBI patterns/Prime Database]:
  governance/alignment, not ROE-stability, may be India's real quality axis. TEST:
  promoter-stake level/change vs forward returns (SEBI quarterly filings are free and
  genuinely point-in-time).
- **Promoter pledging** as distress signal: Zee/Essel (~2019), ADAG (2018-19), DHFL,
  Yes Bank all pledged heavily pre-collapse [LIT, press]; formal academic study
  uncertain [LOW CONFIDENCE]. TEST: pledge level AND acceleration ×
  falling-price interaction (pre-registered, not discovered) vs fwd 6-12m
  returns/crash indicator.
- **Related-party transactions**: SEBI LODR tightened ~2021-22 — a regime break; RPT
  flags pre/post not comparable; text-parsing-bound, Tier-C narrative input.
- **Business groups**: Khanna-Palepu (~1997-2000 JF) — group affiliation
  value-ADDITIVE in emerging markets (internal capital markets substitute for missing
  institutions); a 25-year-old thesis that may have decayed with market deepening.
  TEST: group vs standalone forward returns, pre/post ~2015 split.
- **High-ROCE persistence claim** (HUL/Nestlé/Asian Paints "40%+ ROCE for decades")
  vs the fade literature (Fama-French ~2000): likely resolution = SURVIVORSHIP — the
  cited names are the ones that didn't fade. TEST: formation-decile ROCE persistence
  (full decile at each formation date, never today's famous names), needs a delisted
  registry.
- **Capital-cycle abuse** (Chancellor/Marathon, Capital Returns 2015): PSU dilution
  cycles, 2013-19 infra deleveraging. Forward quality-degradation signal =
  capex growth + dilution + debt growth, sector-neutralized.

## 3. Earnings quality in India

- Accruals anomaly: India adaptations exist, effect sizes vary [LIT, LOW CONFIDENCE].
- Beneish M-score: retrospectively flags Satyam (teaching example); the honest test is
  prospective (restatements/auditor qualifications/crashes), never n=1 retrofits.
- **Satyam (2009)**: ₹7,000+ cr fabricated cash; the tells — high cash with implausibly
  LOW interest income; the aborted Maytas related-party acquisition. Standing forensic
  screen: reported cash vs implied yield.
- **IL&FS (2018) / DHFL (2019) / Yes Bank (2019-20)**: ALM tenor mismatch,
  related-party lending, loan growth far above system + concentration — all visible in
  fundamentals before the repricing. Sector-scoped (financials) quality overlays.
- **Ind-AS transition (FY2016-17, leases 2019)**: a hard comparability seam; vendor
  histories are retroactively restated across it; treat as a sample split. Also
  coincides with demonetization/GST formalization shifts — disentangle before use.
- **MCA filings** = legal ground truth; per-company PDFs, forensic cross-check only.

## 4. ROE/ROCE in the Indian cross-section

- RBI Bulletin corporate-finance series: free, recurring, aggregate-level.
- Sector skew (robust): IT + FMCG at the high-ROCE asset-light end; PSU banks, power,
  infra at the low end; banks/NBFCs = leverage IS the model (ROE + Tier-1, never ROIC).
- **The leverage confound → SEC-D7 bridge**: ROE embeds leverage, ROCE strips it; a
  high ROE-rank-minus-ROCE-rank divergence = leverage-flattered economics = exactly
  the negative-convexity names SEC-D7 flagged. The divergence itself is a candidate
  cross-sectional risk signal — a fundamentals repackaging of booked doctrine. TEST:
  gated on firm fundamentals (the survivor panel holds prices only).

## 5. The India fundamentals data map

| Source | Has | Free? | PIT-ness | Feasibility |
|---|---|---|---|---|
| NSE/BSE filings (results, shareholding, pledge) | as-filed quarters, promoter/pledge % | yes | **genuinely PIT** (filed as-of-date) | per-company scrape; no bulk API |
| screener.in | derived ratios, ~10-15y | free tier | **restated** (current shares/mergers) | fragile scrape, ToS-bound |
| MCA21 | statutory filings, charges | ~free | as-filed ground truth | per-doc PDFs; forensic only |
| CMIE Prowess / Ace Equity | the academic panel | **paid** | restated (PIT variant = separate paid tier) | not accessible |
| Trendlyne / tijori / moneycontrol | ratios | freemium | restated | small-scale only |
| Annual reports + XBRL | full notes (RPT, auditor) | free | as-filed PIT if original docs | high per-doc effort |
| NSE quality-index TR series | index levels + methodology | free | live segment real; pre-launch BACKFILLED | easy; the live-only test |
| Damodaran India/EM datasets | industry aggregates, annual vintages | **free** | each vintage ~PIT at publication | easy; sector cross-check |
| Ken French intl/EM portfolios | EM factor aggregates | **free** | academic construction | easy; EM benchmark |
| S&P BSE factor variants | parallel family | free levels | same backfill caveat | easy |

**The PIT problem plainly:** every free bulk source computes ratios against the
CURRENT restated fact set (shares, mergers, Ind-AS retro-applied) with no
knowledge-date stamp, on a survivor universe. A clean design needs: as-filed numbers
dated by filing date; corporate actions applied only up to the as-of date; a
delisted-name registry; the Ind-AS seam flag; a 30-45 day reporting-lag before a
quarter's numbers are "known".

## 6. What to test first (ranked; bars and traps)

1. **ROE-vs-ROCE divergence** as a leverage-negative-convexity screen (extends SEC-D7).
   Bar: reproduces the crash/cemetery signature OOS. Trap: sector confound — must be
   sector-neutralized. GATED on firm fundamentals.
2. **Live-only NSE quality-index test** (backfill stripped). Bar: live premium clears
   rebalance-turnover costs. Trap: newest indices' live window sits inside the 2021-24
   quality drawdown — era-confounded.
3. **PIT quality-decile backtest** on as-filed vs restated ratios — sizes the
   restatement haircut for quality (Known-Prior-#7 analog). Trap: survivor panel can
   size restatement, NOT survivorship, without the delisted registry.
4. **Promoter-pledge overlay**. Bar: survives excluding the four famous blowups. Trap:
   level alone is noisy (benign pledging) — the pre-registered signal is
   pledge-acceleration × falling price.
5. **ROCE persistence, formation-decile**. Trap: run on survivors it IS the bias it
   tests; needs the delisted registry first.
6. **Ind-AS seam test** — the prerequisite gate for every fundamentals test; separate
   the accounting seam from the demonetization/GST formalization shifts.

Sequencing: everything here is principal-machine-pull-shaped (fundamentals scrape,
SEBI patterns, delisted registry, NSE index TR series); nothing new is
vault-runnable today beyond the already-booked QG-D1.
