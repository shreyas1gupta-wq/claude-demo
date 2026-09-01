# Ingestion kit — runs ONLY on the principal's machine (Contract prior #11)

This environment cannot reach any data host (verified again 2026-08-31: all endpoints blocked at
the proxy), so **nothing here has been executed against a live host** — every script was written
from Appendix A's web-verified access paths and ships with `--dry-run` (prints planned URLs, no
network). Expect first-contact fixes; that is normal and anticipated.

## Day-1 runsheet (distilled from `docs/masterplan/A-data-catalog.md` §4 — read it first)
1. **Confirm CCIL registration is actually free** (sign-in gated; if not free → FBIL's 7-day-
   lagged G-sec curve is the fallback; record the outcome in the data catalog).
2. `python ingest/pull_fred.py data/raw/fred` — VIX, broad dollar, 10y TIPS, Brent, LBMA gold PM
   fix (via FRED's free republication). Fastest win; validates the manifest flow end to end.
3. `python ingest/pull_nse_bhavcopy.py data/raw/nse --start 1996-01-01` — cash bhavcopy, both
   URL schemes (legacy CSV ≤ 2024-07-05, UDiFF from 2024-07-08). Long job; resumes safely.
   Then `--segment fo` for derivatives.
4. `python ingest/pull_amfi.py data/raw/amfi` — NAVAll history (SIP-flow monthlies are a manual
   download; see A-catalog).
5. `python ingest/pull_nsdl_fpi.py data/raw/nsdl` — FPI daily/fortnightly [VERIFY page scheme on
   first contact].
6. `python ingest/pull_indices.py data/raw/indices --dry-run` first — niftyindices endpoints are
   the most [VERIFY]-tagged; fix the endpoint from the browser's network tab if the documented
   one has moved, then run live.
7. RBI DBIE, MOSPI, OBICUS, IMF/BIS/WGC/UN: **manual portal exports** on day 1–2 (interactive
   portals; A-catalog gives the navigation path and expected filename per series). Drop the
   files under `data/raw/<org>/` and run `python ingest/manifest.py data/` to checksum.
8. Commit `data/manifest.json` (checksums + vintages). Raw files stay out of git (size); the
   manifest IS the fixture contract — any refreshed file gets a new vintage entry, never an
   overwrite of an old one.

## Rules
- Never overwrite a raw file: refreshes land beside the old vintage (`<name>.<vintage>.<ext>`).
- Every pull is followed by `manifest.py` — an unmanifested file does not exist for the pipeline.
- Rate limits: NSE pulls sleep politely (default 1.5s) and set a browser User-Agent; if blocked,
  use the archives/mirrors listed in A-catalog §risks rather than hammering.
- The 2026 base-year revision wave (GDP/CPI/IIP/WPI — A-catalog finding) means macro exports
  must record WHICH base the portal served; put it in the filename per A-catalog conventions.

## Addendum (2026-09-01) — India factor library via PyPI (principal's machine)

`pip install indiafactorlibrary` then:
```python
from indiafactorlibrary import IndiaFactorLibrary
lib = IndiaFactorLibrary()
print(lib.get_available_datasets())   # then lib.read("<dataset>") per docs
```
Package verified working here (v0.0.12) but its data host (invespar.com) is blocked at this
container's proxy — run on the principal's machine, save raw responses into ingest/vault/ifl/,
manifest them (sha256), and they become the external validation benchmark for our own bhavcopy
WML construction (momentum Part C §6: tracking-error acceptance test before our construction is
trusted). Also on this runsheet: BSE bhavcopy puller + corporate-actions puller (gaps identified
in momentum Part C — ingest/pull_nse_bhavcopy.py does not yet normalize the two eras' schemas,
and BSE had its own UDiFF-style rename).

## Addendum 2 (2026-09-01) — fundamentals pullers (day-1 gap, from value Part C §C.8)

No fundamentals puller exists in ingest/ at all. Required new scripts (principal machine):
- pull_nse_financial_results.py — quarterly Reg. 33 results (XBRL era: voluntary Jun-2015,
  mandatory 2017-04-01, Integrated Filing 2025-04-01); store announcement timestamps as
  knowledge_time; versioned schema parser per XBRL era.
- pull_nse_governance_events.py — shareholding patterns (Reg. 31, incl. pledge), board/auditor
  events (Reg. 30), RPT disclosures (Reg. 23) combined.
- Banks/financials: Form A/B statements parsed separately (different taxonomy; RBI Ind-AS
  deferral for banks still in force [VERIFY 2026 status]).
Reminder from Part C: balance sheet + cash flow are HALF-YEARLY/ANNUAL only in India — mixed-
frequency ("staircase") signal handling is pre-registered, not improvised.

## Addendum 3 (2026-09-01) — debt/fiscal pullers (from debt Part C)

New fixture family (nothing in ingest/ covers it): pull_status_paper_debt.py,
pull_receipt_budget_debt.py, pull_state_finances_rbi.py, pull_pdmc_quarterly.py (ownership/
captivity table), pull_weo_every_vintage.py (April+October, NEVER latest-only), pull_bis_credit_gov.py,
pull_chinn_ito.py, plus a one-time hand-built SLR/CRR/policy-rate change-date master table.
WARNING from Part C: the IMF "Historical Public Debt Database" (Abbas et al., starts 1880/1920)
and "Public Finances in Modern History" (starts 1800) are DIFFERENT products — scripts must name
which; grabbing HPDD under an "1800" assumption silently pulls the wrong one.
