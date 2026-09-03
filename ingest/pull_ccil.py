#!/usr/bin/env python3
"""CCIL money-market dailies (TREPS/call/market repo) + RBI LAF position — Priority-1 funding/ pull.

UNTESTED LIVE from the build environment (CCIL/RBI blocked at the proxy). Run on the
principal's machine:
  python ingest/pull_ccil.py data/raw/funding [--start 2010-01-01]
  python ingest/pull_ccil.py --emit-auth-template

Then: assemble one CSV per series (Date, Rate/Amount), copy to ingest/vault/funding/,
FILL AND COMMIT the AUTHENTICATION.md pass-1 anchors BEFORE checking values, run its checks,
manifest. Unblocks: H58-D1 grading (the drain-window quarantine's bars), FS-D2
(order-of-arrival), L2 funding-leg calibration, F-series funding inputs.

[VERIFY on first contact]: CCIL publishes daily money-market summaries (TREPS/CBLO history —
note the CBLO->TREPS transition on 2018-11-05, a series break to encode, not smooth over);
call money via CCIL/RBI WSS; the RBI DBIE portal serves LAF net position (its export formats
change — capture the query used). WACR is RBI-published and makes a good cross-check series.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

AUTH_TEMPLATE = '''# Vault: funding/ — authentication record (two-pass, bars before results)

## treps_call_repo_daily_*.csv + laf_position_daily_*.csv
Source: CCIL publications + RBI DBIE/WSS, pulled {DATE} on the principal's machine
(ingest/pull_ccil.py). Query/export descriptors captured: [FILL].

### PASS 1 — anchors written BEFORE checking values (fill, commit, THEN check)
- A1: the CBLO->TREPS transition lands 2018-11-05 — CBLO rows end and TREPS rows begin
  within 3 business days of it (the break is ENCODED, never smoothed).
- A2: a documented stress print — call/TREPS spike in the IL&FS window (Sep-Oct 2018):
  [VERIFY a specific documented rate print from two sources at pull time; record it HERE
  before checking the file].
- A3: a documented calm print — the 2020-21 surplus-liquidity era: TREPS median in
  H2-2020 sits BELOW the reverse-repo-era floor zone [VERIFY the documented range HERE].
- A4: dates strictly increasing per series; rates within (0, 25)% annualized.
- A5: LAF net position sign matches the documented regime: deficit (negative for banks) in
  2018, large surplus in 2020-21 [directional check, no magic level].

### PASS 2 — results (run only after pass 1 is committed)
(pending)
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir", nargs="?")
    ap.add_argument("--start", default="2010-01-01")
    ap.add_argument("--emit-auth-template", action="store_true")
    args = ap.parse_args()
    if args.emit_auth_template:
        p = Path("ingest/vault/funding")
        p.mkdir(parents=True, exist_ok=True)
        out = p / "AUTHENTICATION.md"
        if out.exists():
            print(f"refusing to overwrite {out}")
            return 1
        out.write_text(AUTH_TEMPLATE)
        print(f"pass-1 skeleton written to {out} — fill [VERIFY] anchors and commit BEFORE checking data")
        return 0
    print("Live pull runs on the principal's machine (CCIL/RBI unreachable from the build env).\n"
          "Sources: CCIL daily money-market summaries (TREPS/call), RBI DBIE for LAF/WACR.\n"
          "Save raw exports under", args.outdir or "data/raw/funding")
    return 0


if __name__ == "__main__":
    sys.exit(main())
