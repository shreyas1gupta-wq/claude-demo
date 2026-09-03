#!/usr/bin/env python3
"""India VIX daily history (NSE archive) — the runsheet's Priority-1 vix/ pull.

UNTESTED LIVE from the build environment (NSE blocked at the proxy). Run on the principal's
machine:
  python ingest/pull_india_vix.py data/raw/vix --start 2009-03-02 [--end YYYY-MM-DD]
  python ingest/pull_india_vix.py --emit-auth-template   # writes the pass-1 anchor skeleton

Then: assemble one CSV (Date, Open, High, Low, Close), copy to
ingest/vault/vix/india_vix_daily_2009_*.csv, FILL AND COMMIT the AUTHENTICATION.md pass-1
anchors BEFORE looking at values beyond format, run its checks, and `python ingest/manifest.py
ingest/vault/vix`. Unblocks: CW-D1's VIX leg, F5, FS-D1 (with futures/term data), VRP designs.

[VERIFY on first contact]: NSE serves VIX history via the reports/indices-historical-vix page
(CSV export) and archives endpoints that move periodically; the India VIX methodology changed
its underlying option-chain handling over time — capture the methodology note version with
the pull. India VIX disseminates from 2009-03-02 (a 2008-11 launch exists in some records as
non-continuous history — take 2009-03-02 as the series start and record any earlier rows as
a provenance note, not silently).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

AUTH_TEMPLATE = '''# Vault: vix/ — authentication record (two-pass, bars before results)

## india_vix_daily_2009_YYYY.csv
Source: NSE India VIX historical archive, pulled {DATE} on the principal's machine
(ingest/pull_india_vix.py). Methodology-note version captured alongside: [FILL].

### PASS 1 — anchors written BEFORE checking values (fill, commit, THEN check)
- A1: series starts 2009-03-02 (first dissemination day); no rows before it unless
  documented in provenance.
- A2: 2020 peak zone — max close in Mar-2020 >= 80 [VERIFY exact documented peak close at
  pull time from two independent sources; record the number HERE before checking the file].
- A3: the 2017 calm — full-year 2017 median close <= 14 [VERIFY same way].
- A4: dates strictly increasing, no duplicates; closes within (5, 100).
- A5: 240-255 rows per full year 2010-2025 (flag any year outside with dissection).

### PASS 2 — results (run only after pass 1 is committed)
(pending)
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir", nargs="?", help="raw download directory")
    ap.add_argument("--start", default="2009-03-02")
    ap.add_argument("--end", default=None)
    ap.add_argument("--emit-auth-template", action="store_true")
    args = ap.parse_args()
    if args.emit_auth_template:
        p = Path("ingest/vault/vix")
        p.mkdir(parents=True, exist_ok=True)
        out = p / "AUTHENTICATION.md"
        if out.exists():
            print(f"refusing to overwrite {out}")
            return 1
        out.write_text(AUTH_TEMPLATE)
        print(f"pass-1 skeleton written to {out} — fill [VERIFY] anchors and commit BEFORE checking data")
        return 0
    print("Live pull runs on the principal's machine (NSE unreachable from the build env).\n"
          "Start at https://www.nseindia.com/reports-indices-historical-vix — the page's CSV\n"
          "export covers custom ranges; chunk by year, save under", args.outdir or "data/raw/vix")
    return 0


if __name__ == "__main__":
    sys.exit(main())
