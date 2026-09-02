#!/usr/bin/env python3
"""Atlas 2.7 — FP1a/FP1b, PRE-REGISTERED: pre-election windows in India's market factor.

Windows: the 3 months ENDING in each general-election result month (fixed list, n=8, tiny —
stated). FP1a (folk pre-election rally): PASS only if mean window monthly MF return > all-
months mean AND >=6/8 elections have positive window means. FP1b: median |monthly MF| inside
windows vs all months (measurement, no bar — L5 schedules vol, not direction).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "fiscal-deep" / "fiscal-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/fiscal-charts.json")

ELECTIONS = ["1996-05", "1998-03", "1999-10", "2004-05", "2009-05",
             "2014-05", "2019-05", "2024-06"]


def main() -> int:
    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv",
                    na_values=["NA"]).set_index("Date")
    mf = f.MF.astype(float).dropna()
    idx = list(mf.index)

    rows, win_means, result_month = [], [], {}
    for e in ELECTIONS:
        i = idx.index(e)
        w = mf.iloc[i - 2:i + 1]
        win_means.append(float(w.mean()))
        result_month[e] = float(mf.loc[e])
        rows.append((e, float(w.mean()), [round(float(x), 1) for x in w], float(mf.loc[e])))

    all_mean = float(mf.mean())
    pos = sum(1 for m in win_means if m > 0)
    a_ok = (np.mean(win_means) > all_mean) and (pos >= 6)
    fp1a = "PASS" if a_ok else "FAIL"

    win_abs = [abs(x) for e in ELECTIONS for x in
               mf.iloc[idx.index(e) - 2: idx.index(e) + 1]]
    med_win, med_all = float(np.median(win_abs)), float(np.median(mf.abs()))
    res_abs = [abs(v) for v in result_month.values()]

    res = [
        "# Atlas 2.7 — fiscal/political cycle: pre-election windows (FP1a/FP1b, pre-registered)", "",
        f"India market factor (IIMA), monthly. n = 8 general elections — TINY, stated up front.", "",
        "| Election (result month) | window mean %/m | window months % | result-month % |",
        "|---|---|---|---|",
        *[f"| {e} | {m:+.1f} | {w} | {r:+.1f} |" for e, m, w, r in rows],
        "",
        f"## FP1a — the folk pre-election rally",
        f"- Mean of window means **{np.mean(win_means):+.2f}%/m** vs all-months mean "
        f"**{all_mean:+.2f}%/m**; positive windows **{pos}/8** (bar: mean above AND ≥6/8).",
        f"- **{fp1a}**.", "",
        f"## FP1b — window absolute moves (measurement, prior set)",
        f"- Median |monthly MF| in windows **{med_win:.1f}%** vs all months **{med_all:.1f}%**;",
        f"  result-month |moves|: {sorted(round(x,1) for x in res_abs)} (median "
        f"{np.median(res_abs):.1f}%).", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "elections": [[e, round(m, 2)] for e, m, _, _ in rows],
        "all_mean": round(all_mean, 2), "med_win": med_win, "med_all": med_all,
        "result_abs": {e: round(abs(v), 1) for e, v in result_month.items()}},
        separators=(",", ":")))
    print(f"FP1a {fp1a} (win mean {np.mean(win_means):+.2f} vs all {all_mean:+.2f}, {pos}/8 pos) | "
          f"FP1b med|win| {med_win:.1f}% vs {med_all:.1f}% | result-month median "
          f"{np.median(res_abs):.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
