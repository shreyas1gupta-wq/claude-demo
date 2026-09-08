# Handoff prompt — India fundamentals data build (for the principal's other Claude)
Committed 2026-09-08. This exact text is given to a separate Claude session with data
access. The files it returns are vaulted here under two-pass AUTHENTICATION on arrival.

---

You are building a point-in-time Indian equity fundamentals dataset for a quantitative
research desk. The desk runs a strict pre-registration discipline: your job is DATA
ONLY — do not compute strategies, returns, deciles, or signals; the desk runs its own
registered designs on what you deliver. Accuracy and honest gaps beat completeness:
never interpolate, never fill, never substitute a restated number for an as-filed one.
If a field cannot be sourced, leave it blank and say so in the provenance file.

## The one rule that matters most: POINT-IN-TIME
Most free Indian sources (screener.in, moneycontrol, Trendlyne) show RESTATED history —
current shares outstanding, merged entities, Ind-AS applied retroactively. That data is
useless for backtesting. Everything you deliver must be AS ORIGINALLY FILED, with the
FILING DATE attached to every row, sourced from NSE/BSE corporate filings, exchange
result PDFs/XBRL, or original annual reports — so the desk can reconstruct exactly what
was knowable on any historical date.

## Deliverables (CSV, UTF-8, one header row; a zip of all files + PROVENANCE.md)

P1 — `fundamentals_quarterly.csv` (the core file). One row per company-quarter,
NIFTY 500 universe (see P2 for membership; include every name that was EVER a member
2014-01-01 → today, including delisted ones). Columns:
isin, ticker, company_name, fiscal_quarter_end (YYYY-MM-DD), filing_date (YYYY-MM-DD,
the actual exchange submission date), statement_basis (standalone/consolidated — prefer
consolidated where filed, and SAY which), total_assets, total_equity, total_debt,
cash_and_equivalents, revenue, ebit, net_income, cfo (operating cash flow — annual/
half-yearly if quarterly not filed, with period_months column), shares_outstanding,
source_url. Values in INR crore, as filed. Target span: quarters from FY2014 onward.

P2 — `index_membership.csv`: index (NIFTY500/NIFTY200/NIFTY50), isin, ticker,
effective_date, action (ADD/REMOVE), source_url. From NSE's index reconstitution
press releases / archived constituent lists. This is what makes the universe
point-in-time — do not skip it.

P3 — `delisted_registry.csv`: isin, ticker, company_name, last_trading_date, reason
(merger/acquisition/suspension/liquidation/voluntary), acquirer_if_any, source_url.
Every NSE mainboard delisting/suspension 2014 → today. This file is what removes
survivorship bias; it is as important as P1.

P4 — `prices_daily.csv.gz`: date, isin, ticker, close_unadjusted, close_adjusted,
volume — daily, 2014 → today, for the SAME universe including delisted names up to
their last trading day. Plus `corporate_actions.csv`: isin, ex_date, type
(split/bonus/dividend/merger/demerger/rights), ratio_or_amount, source_url — so
adjustments can be re-derived and audited.

P5 — `shareholding_pledge.csv`: isin, ticker, quarter_end, filing_date, promoter_pct,
promoter_pledged_pct_of_promoter_holding, source_url. From SEBI/exchange shareholding-
pattern filings (these ARE point-in-time by construction), quarterly, 2014 → today.

P6 (nice-to-have) — `nse_strategy_indices_tr.csv`: date, index_name, tr_level for
NIFTY200 Quality 30, NIFTY100 Quality 30, NIFTY Midcap150 Quality 50, NIFTY 500 TR,
NIFTY 200 TR — daily, from index launch dates (mark each index's LAUNCH date in
provenance; the desk treats pre-launch history as backfill).

## PROVENANCE.md (mandatory)
For each file: exact source (portal + URL pattern), pull date, row counts, coverage
stats (companies × quarters actually filled vs possible), every transformation you
applied (unit conversions, consolidated-vs-standalone choices), and a KNOWN GAPS
section listing what you could not get and why. If you had to use a secondary source
for any subset, mark those rows with a source flag column rather than silently mixing.

## Self-checks before you hand it back (report the results, do not fix by fudging)
1. Spot-verify 5 large names (e.g. Reliance, TCS, HDFC Bank, Infosys, ITC) for one
   recent and one 2016 quarter against their original filed results — values must
   match the as-filed PDFs, NOT today's restated screener values.
2. Confirm filing_date > fiscal_quarter_end for >99% of rows (typical lag 30-45 days);
   list violations.
3. Confirm the delisted registry is non-empty for every year (NSE delists/suspends
   names every year — an empty year means a gap, not a clean year).
4. Confirm P2 reproduces a known reconstitution (e.g. any published NIFTY 500
   semi-annual change) exactly.
5. Report per-year universe size from P2 (should be ~500 ± transitions).

## What NOT to do
No paid sources (no CMIE/Ace Equity extracts). No filling gaps from memory or from
restated aggregators. No computing ratios, scores, returns, or "helpfully" adding
derived columns. No dropping delisted or suspended names. If the full 2014 start is
infeasible for some field, deliver what exists with the honest start date per field.
