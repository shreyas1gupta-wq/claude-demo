#!/usr/bin/env python3
"""THE single out-of-sample look for pass 2 (PREREG.md). Run once per frozen, gate-passing candidate.

For each module it runs evaluate.py three times on the SAME frozen signal:
  results/<name>.json            3 bp / 60 bp   (headline, 1.5x measured costs)
  results/<name>_c240.json       2 bp / 40 bp   (measured costs, secondary row)
  results/<name>_s690.json       6 bp / 90 bp   (stress)
and appends a line to results/OOS_LOOK_LOG.md so the number of looks is on the record.
Refuses to run a module that has not passed gate_check.py, or that already has an OOS result (a second look).
Usage: python oos_final.py signals/a.py [signals/b.py ...] [--force-relook "reason"]"""
from __future__ import annotations
import argparse, datetime as dt, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from gate_check import check  # noqa: E402

RES, DEV = HERE / "results", HERE / "dev_results"
LOG = RES / "OOS_LOOK_LOG.md"
SETTINGS = [("", 3.0, 60.0), ("c240", 2.0, 40.0), ("s690", 6.0, 90.0)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="+")
    ap.add_argument("--force-relook", default="", help="reason string; required to re-run a module that already has an OOS result")
    ap.add_argument("--skip-gates", action="store_true", help="only for the pre-existing pass-1 incumbents (their gates were not pre-registered)")
    a = ap.parse_args()
    if not LOG.exists():
        LOG.write_text("# Out-of-sample look log (append-only)\n\n| when (IST) | module | setting | note |\n|---|---|---|---|\n")
    for m in a.modules:
        p = Path(m); stem = p.stem
        if not a.skip_gates:
            dj = DEV / f"{stem}.json"
            if not dj.exists():
                print(f"REFUSED {stem}: no dev_results/{stem}.json"); continue
            g = check(str(dj))
            if not g["all_pass"]:
                print(f"REFUSED {stem}: DEV gates not passed -> {[k for k, v in g['gates'].items() if not v['pass']]}"); continue
        if (RES / f"{stem}.json").exists() and not a.force_relook:
            print(f"REFUSED {stem}: results/{stem}.json exists — this would be a second look (use --force-relook 'reason' and it is logged)"); continue
        for tag, c, f in SETTINGS:
            cmd = [sys.executable, str(HERE / "evaluate.py"), m, "--cost-bps", str(c), "--fin-bps", str(f)] + (["--tag", tag] if tag else [])
            r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
            print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-800:])
            note = ("signal look #1" if not tag else "same frozen signal, cost row") + (f"; RELOOK: {a.force_relook}" if a.force_relook else "")
            with LOG.open("a") as fh:
                fh.write(f"| {dt.datetime.now().strftime('%Y-%m-%d %H:%M')} | {stem} | {c:g}bp/{f:g}bp | {note} |\n")


if __name__ == "__main__":
    main()
