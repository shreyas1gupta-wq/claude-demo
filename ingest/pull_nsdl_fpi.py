#!/usr/bin/env python3
"""NSDL FPI flow data (free). UNTESTED LIVE from the build environment.

fpi.nsdl.co.in publishes daily/fortnightly/monthly FPI investment reports; the exact report URLs
are session-generated on the portal [VERIFY on first contact — Appendix A row gives the
navigation path: fpi.nsdl.co.in -> Reports -> Historical]. This script therefore only scaffolds
the destination layout and prints the navigation path; the first pull is manual, after which the
stable direct report URLs (if any) get filled in here.
Usage: python ingest/pull_nsdl_fpi.py data/raw/nsdl
"""
import sys
from pathlib import Path

NAV_PATH = ("MANUAL FIRST PULL: https://www.fpi.nsdl.co.in -> Reports -> "
            "'FPI Investment Details (Historical)' -> export daily + monthly series; "
            "save as nsdl_fpi_daily_<vintage>.csv / nsdl_fpi_monthly_<vintage>.csv")


def main(out_dir: str) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    print(NAV_PATH)
    print(f"drop files into {out}/ then run: python ingest/manifest.py data/")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/raw/nsdl")
