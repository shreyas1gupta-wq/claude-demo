#!/usr/bin/env python3
"""Rebuild the Ionic RM Platform Review dashboard from the Aug-31 HNI MIS.

    python3 rm-platform-review/build/build_dashboard.py [--verify] [--sample N]

Reads the workbook, assembles DATA, runs the cross-check / random-check /
calc-check suites, and only then writes the dashboard.  If any check fails the
build aborts with a non-zero exit rather than shipping figures that do not tie.
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import assemble                                          # noqa: E402
import extract                                           # noqa: E402
import render                                            # noqa: E402
import verify                                            # noqa: E402
from sources import STALE_BLOCKS                         # noqa: E402
from xlsx_reader import Workbook                         # noqa: E402

WORKBOOK = os.path.join(ROOT, "source",
                        "HNI_Team_Intelligence_31Aug2026_MIS_FINAL_v7_FIXED.xlsx")
PRIOR_HTML = os.path.join(ROOT, "source", "prior_dashboard_FINAL_1_1.html")
FOCUS_CSV = os.path.join(ROOT, "data", "focus_rm.csv")
OUT_HTML = os.path.join(ROOT, "Ionic_RM_Platform_Review_Aug31.html")
OUT_DATA = os.path.join(ROOT, "data", "DATA.json")
OUT_QC = os.path.join(ROOT, "qc", "reconciliation.md")

SOURCE_LABEL = "HNI_Team_Intelligence_31Aug2026_MIS_FINAL_v7_FIXED.xlsx"


def build(workbook_path=WORKBOOK):
    wb = Workbook(workbook_path)

    roster = extract.roster(wb)
    ml, ml_notes = extract.market_leaders(wb, roster)
    actuals = extract.aug_actuals(wb)
    platform = extract.platform_detail(wb)
    buckets = extract.aum_buckets(wb)
    sheets = extract.team_sheet_detail(wb)
    series = extract.firm_series(wb)
    focus_team8, focus_firm = extract.focus_team_actuals(wb)

    supplied = assemble.mis_focus(FOCUS_CSV)
    if supplied is not None:
        focus_map, focus_basis = supplied, "mis"
    else:
        focus_map, focus_basis = assemble.prior_focus(PRIOR_HTML), "prior"

    records = assemble.build_records(roster, ml, ml_notes, actuals, platform,
                                    buckets, sheets, focus_map, focus_basis)
    desks = assemble.build_desks(records, focus_team8, series["product_deltas"])
    firm = assemble.build_firm(desks, records, buckets, platform, series,
                               focus_firm, focus_basis)
    return wb, {"firm": firm, "teams": desks}, records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="run the checks and print the report without writing files")
    ap.add_argument("--sample", type=int, default=20,
                    help="how many RMs the random check re-derives (default 20)")
    args = ap.parse_args()

    wb, data, records = build()
    checks, sample, slipping = verify.run_all(data, wb, sample_size=args.sample)

    print(checks.report())
    total = len(checks.rows)
    print(f"\n{total - len(checks.failed)}/{total} checks PASS")

    if checks.failed:
        print("\nBUILD ABORTED — the dashboard was not written.", file=sys.stderr)
        return 1

    if args.verify:
        print("\n--verify: checks only, no files written.")
        return 0

    os.makedirs(os.path.dirname(OUT_DATA), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_QC), exist_ok=True)

    with open(OUT_DATA, "w") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False)

    qc = render.qc_markdown(data, checks, sample, slipping, STALE_BLOCKS,
                            SOURCE_LABEL, PRIOR_HTML)
    with open(OUT_QC, "w") as fh:
        fh.write(qc)

    html = render.dashboard(data, checks, sample, STALE_BLOCKS, SOURCE_LABEL,
                            PRIOR_HTML)
    with open(OUT_HTML, "w") as fh:
        fh.write(html)

    print(f"\nwrote {os.path.relpath(OUT_HTML)}  ({len(html):,} bytes)")
    print(f"wrote {os.path.relpath(OUT_DATA)}")
    print(f"wrote {os.path.relpath(OUT_QC)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
