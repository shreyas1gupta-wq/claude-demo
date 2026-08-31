#!/usr/bin/env python3
"""AMFI NAV history (free text endpoint). UNTESTED LIVE from the build environment.

Daily NAVAll snapshots: https://portal.amfiindia.com/spages/NAVAll.txt (current day) and the
dated history endpoint NAVHistoryReport [VERIFY exact form on first contact — Appendix A row].
Usage: python ingest/pull_amfi.py data/raw/amfi [--dry-run]
SIP monthly flows are a manual portal download (see ingest/README.md step 4).
"""
from __future__ import annotations

import sys
import urllib.request
from datetime import date
from pathlib import Path

URL_TODAY = "https://portal.amfiindia.com/spages/NAVAll.txt"


def main(out_dir: str, dry: bool) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    dest = out / f"NAVAll_{date.today().isoformat()}.txt"
    print(f"{'DRY ' if dry else ''}{URL_TODAY} -> {dest}")
    if dry:
        return
    req = urllib.request.Request(URL_TODAY, headers={"User-Agent": "Mozilla/5.0"})
    dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    print("done; historical backfill: use the dated NAVHistoryReport endpoint per Appendix A")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] if args else "data/raw/amfi", "--dry-run" in args)
