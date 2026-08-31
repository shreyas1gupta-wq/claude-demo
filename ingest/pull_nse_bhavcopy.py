#!/usr/bin/env python3
"""NSE bhavcopy history — handles BOTH URL schemes across the 2024-07-08 UDiFF boundary
(NSE Circular 62424; Appendix A finding). UNTESTED LIVE from the build environment.

Usage:
  python ingest/pull_nse_bhavcopy.py data/raw/nse --start 1996-01-01 [--end YYYY-MM-DD]
                                     [--segment cm|fo] [--dry-run] [--sleep 1.5]
Resumes safely: existing files are skipped. Weekends skipped; exchange holidays surface as 404s
and are recorded to holidays_404.txt (reconcile against the exchange holiday list afterwards).
[VERIFY on first contact]: exact archive hostnames/paths move periodically — Appendix A §risks
lists mirrors (getbhavcopy, Kaggle caches) if these 404 wholesale.
"""
from __future__ import annotations

import argparse
import time
import urllib.request
from datetime import date, timedelta
from pathlib import Path

UDIFF_BOUNDARY = date(2024, 7, 8)
# legacy (<= 2024-07-05): zipped CSV per day
LEGACY_CM = ("https://archives.nseindia.com/content/historical/EQUITIES/{yyyy}/{MON}/"
             "cm{dd}{MON}{yyyy}bhav.csv.zip")
LEGACY_FO = ("https://archives.nseindia.com/content/historical/DERIVATIVES/{yyyy}/{MON}/"
             "fo{dd}{MON}{yyyy}bhav.csv.zip")
# UDiFF (>= 2024-07-08)
UDIFF_CM = ("https://archives.nseindia.com/content/cm/"
            "BhavCopy_NSE_CM_0_0_0_{yyyymmdd}_F_0000.csv.zip")
UDIFF_FO = ("https://archives.nseindia.com/content/fo/"
            "BhavCopy_NSE_FO_0_0_0_{yyyymmdd}_F_0000.csv.zip")
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research-fixture-pull",
           "Accept": "*/*", "Referer": "https://www.nseindia.com/"}


def url_for(d: date, segment: str) -> str:
    if d >= UDIFF_BOUNDARY:
        base = UDIFF_CM if segment == "cm" else UDIFF_FO
        return base.format(yyyymmdd=d.strftime("%Y%m%d"))
    base = LEGACY_CM if segment == "cm" else LEGACY_FO
    return base.format(yyyy=d.strftime("%Y"), MON=d.strftime("%b").upper(), dd=d.strftime("%d"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", default=date.today().isoformat())
    ap.add_argument("--segment", default="cm", choices=["cm", "fo"])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sleep", type=float, default=1.5)
    a = ap.parse_args()

    out = Path(a.out_dir) / a.segment
    out.mkdir(parents=True, exist_ok=True)
    holidays = open(out / "holidays_404.txt", "a")
    d = date.fromisoformat(a.start)
    end = date.fromisoformat(a.end)
    n_ok = n_skip = n_404 = 0
    while d <= end:
        if d.weekday() < 5:
            dest = out / f"{a.segment}_{d.isoformat()}.csv.zip"
            if dest.exists():
                n_skip += 1
            else:
                url = url_for(d, a.segment)
                if a.dry_run:
                    if n_ok < 5 or d >= UDIFF_BOUNDARY and n_ok < 10:
                        print("DRY", url)
                    n_ok += 1
                else:
                    try:
                        req = urllib.request.Request(url, headers=HEADERS)
                        dest.write_bytes(urllib.request.urlopen(req, timeout=45).read())
                        n_ok += 1
                    except Exception as e:  # noqa: BLE001 - 404s are holidays; log and continue
                        holidays.write(f"{d.isoformat()} {e}\n")
                        n_404 += 1
                    time.sleep(a.sleep)
        d += timedelta(days=1)
    print(f"ok={n_ok} skipped={n_skip} missing/404={n_404} -> {out}")
    print("next: python ingest/manifest.py data/")


if __name__ == "__main__":
    main()
