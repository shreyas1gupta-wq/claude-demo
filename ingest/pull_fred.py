#!/usr/bin/env python3
"""FRED pulls (free CSV endpoint, no key): the P0 global series.

UNTESTED AGAINST THE LIVE HOST from the build environment (blocked); endpoint form verified by
Appendix A. Usage: python ingest/pull_fred.py data/raw/fred [--dry-run]
"""
from __future__ import annotations

import sys
import time
import urllib.request
from pathlib import Path

SERIES = {
    "VIXCLS": "CBOE VIX (L9 global-cycle input)",
    "DTWEXBGS": "Broad dollar index (L9; successor of discontinued TWEXB ~2020)",
    "DFII10": "10y TIPS real yield (L15 real-rate persistence; gold real-rate input)",
    "DCOILBRENTEU": "Brent spot (L9 oil, Kilian-decomposed downstream)",
    "GOLDPMGBD228NLBM": "LBMA gold PM fix, free republication (gold sleeve) — resolves the LBMA paywall",
}
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"


def main(out_dir: str, dry: bool) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for sid, why in SERIES.items():
        url = URL.format(sid=sid)
        dest = out / f"{sid}.csv"
        print(f"{'DRY ' if dry else ''}{sid}: {url}  # {why}")
        if dry:
            continue
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(1.0)
    if not dry:
        print(f"done -> {out}; now run: python ingest/manifest.py {out.parent.parent}")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] if args else "data/raw/fred", "--dry-run" in args)
