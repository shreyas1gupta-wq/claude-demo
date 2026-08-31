#!/usr/bin/env python3
"""NSE indices TRI + constituent histories. THE MOST [VERIFY]-TAGGED PULLER — run --dry-run
first and fix endpoints from the browser network tab if moved (Appendix A rows B1-B8).

Targets: Nifty 50 / 500 / Total Market / Microcap 250 TRI histories + current constituent CSVs
+ the reconstitution-change archive (press releases). UNTESTED LIVE from the build environment.
Usage: python ingest/pull_indices.py data/raw/indices [--dry-run]
"""
from __future__ import annotations

import sys
import time
import urllib.request
from pathlib import Path

CONSTITUENT_CSVS = {
    "nifty50": "https://www.niftyindices.com/IndexConstituent/ind_nifty50list.csv",
    "nifty500": "https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv",
    "niftytotalmarket": "https://www.niftyindices.com/IndexConstituent/ind_niftytotalmarket_list.csv",
    "niftymicrocap250": "https://www.niftyindices.com/IndexConstituent/ind_niftymicrocap250_list.csv",
}
NOTE = ("TRI history: niftyindices.com -> Reports -> Historical Data (or the "
        "/Backpage.aspx/getHistoricaldatatabletoString POST endpoint) [VERIFY]. "
        "Constituent HISTORY (reconstitution changes) comes from the press-release archive - "
        "needed for the survivorship-free universe (R0.2) and the PIT-integrity task R0.2b: "
        "pre-2023 Total Market/Microcap membership is reconstructed, not published.")
HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.niftyindices.com/"}


def main(out_dir: str, dry: bool) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    print(NOTE)
    for name, url in CONSTITUENT_CSVS.items():
        dest = out / f"constituents_{name}_current.csv"
        print(f"{'DRY ' if dry else ''}{url}")
        if dry:
            continue
        req = urllib.request.Request(url, headers=HEADERS)
        dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(1.5)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] if args else "data/raw/indices", "--dry-run" in args)
