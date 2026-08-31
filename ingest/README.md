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
