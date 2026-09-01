#!/usr/bin/env python3
"""Atlas 2.2 (NBFC/shadow-credit) — SC1, PRE-REGISTERED: the funding-run factor signature.

Claim: the IL&FS crunch (2018-09..2019-08) shows SMB 12m cum return in its bottom decile of
all rolling 12m windows while the MARKET factor is NOT in its own bottom decile — a credit-
supply event concentrated in small/funding-dependent firms, not a broad macro crash.
Comparators (GFC, taper, COVID) are context prints, no bars.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "shadow-deep" / "shadow-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/shadow-charts.json")

WINDOWS = {"IL&FS crunch": ("2018-09", "2019-08"), "GFC": ("2008-09", "2009-08"),
           "Taper": ("2013-05", "2014-04"), "COVID": ("2020-02", "2021-01")}


def main() -> int:
    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv",
                    na_values=["NA"]).set_index("Date")
    f.index = pd.PeriodIndex(f.index, freq="M")
    cum12 = {c: (np.log1p(f[c] / 100).rolling(12).sum() * 100) for c in ("SMB", "MF")}

    rows, chart = [], {"roll_smb": [], "roll_mf": [], "windows": WINDOWS}
    stats = {}
    for name, (a, b) in WINDOWS.items():
        end = pd.Period(b, freq="M")
        smb_w = float(cum12["SMB"].loc[end])
        mf_w = float(cum12["MF"].loc[end])
        pct_smb = float((cum12["SMB"].dropna() <= smb_w).mean())
        pct_mf = float((cum12["MF"].dropna() <= mf_w).mean())
        stats[name] = (smb_w, pct_smb, mf_w, pct_mf)
        rows.append(f"| {name} ({a}..{b}) | {smb_w:+.1f}% | {pct_smb*100:.0f}th "
                    f"| {mf_w:+.1f}% | {pct_mf*100:.0f}th |")

    smb_w, pct_smb, mf_w, pct_mf = stats["IL&FS crunch"]
    a_ok, b_ok = pct_smb <= 0.10, pct_mf > 0.10
    verdict = "PASS" if a_ok and b_ok else "FAIL"

    res = [
        "# Atlas 2.2 — shadow credit: the funding-run factor signature (SC1, pre-registered)", "",
        "Data: vaulted IIMA monthly factors (log-cum 12m windows, 1994+). Bars fixed before",
        "looking; comparator rows are context, no bars. Interpretation AFTER the print.", "",
        "| Window | SMB 12m cum | SMB percentile | Market 12m cum | Market percentile |",
        "|---|---|---|---|---|", *rows, "",
        f"- Pre-registered bars (IL&FS window): SMB percentile ≤ 10th -> {a_ok}; market",
        f"  percentile > 10th -> {b_ok}. **SC1 {verdict}**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    r = cum12["SMB"].dropna()
    chart["roll_smb"] = [[str(i), round(float(v), 1)] for i, v in r.items()]
    chart["roll_mf"] = [[str(i), round(float(v), 1)]
                        for i, v in cum12["MF"].dropna().items()]
    CHART.write_text(json.dumps(chart, separators=(",", ":")))
    print(f"SC1 {verdict} | IL&FS: SMB {smb_w:+.1f}% ({pct_smb*100:.0f}th), "
          f"MF {mf_w:+.1f}% ({pct_mf*100:.0f}th)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
