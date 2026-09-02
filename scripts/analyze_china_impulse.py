#!/usr/bin/env python3
"""Atlas 2.11 — CI1a/CI1b, PRE-REGISTERED: China-pulse proxy in metals-vs-ags relative prices.

CI1a (Jacks annual): std of 3y change in metals_rel, 2000-2015 vs 1950-1999; bar >= 1.5x.
CI1b (IMF monthly): cumulative metals-minus-ags log change positive in BOTH pre-declared pulse
windows [2008-11..2010-12] and [2016-01..2017-06]; bar 2/2. Confounds stated at registration.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault" / "commodities"
OUT = ROOT / "research" / "cycles" / "china-deep" / "china-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/china-charts.json")

METALS = ["Iron ore", "Copper", "Steel", "Zinc", "Nickel", "Aluminum"]
AGS = ["Barley", "Corn", "Rice", "Rye", "Wheat", "Cocoa", "Coffee", "Cotton", "Palm oil",
       "Rubber", "Sugar", "Tea", "Tobacco", "Wool", "Beef", "Lamb", "Pork", "Hides"]


def main() -> int:
    j = pd.read_csv(V / "jacks_real_commodity_prices_1850_2015.csv").set_index("Year")
    rel = np.log(j[METALS]).mean(axis=1) - np.log(j[AGS]).mean(axis=1)
    d3 = (rel - rel.shift(3)).dropna()
    pre = d3.loc[1950:1999]
    post = d3.loc[2000:2015]
    ratio = float(post.std() / pre.std())
    ci1a = "PASS" if ratio >= 1.5 else "FAIL"

    imf = pd.read_csv(V / "imf_pcps_monthly_1980_2017.csv", parse_dates=["Date"]).set_index("Date")
    m_rel = (np.log(imf["Metals Price Index"].astype(float))
             - np.log(imf[["Agricultural Raw Materials Index",
                           "Food Price Index"]].astype(float)).mean(axis=1))
    wins = {"2008-11..2010-12": ("2008-11-01", "2010-12-01"),
            "2016-01..2017-06": ("2016-01-01", "2017-06-01")}
    checks = {}
    for name, (a, b) in wins.items():
        checks[name] = float(m_rel.loc[b] - m_rel.loc[a])
    npos = sum(v > 0 for v in checks.values())
    ci1b = "PASS" if npos == 2 else "FAIL"

    res = [
        "# Atlas 2.11 — China credit impulse: proxy trials CI1a/CI1b (pre-registered)", "",
        "Confounds stated at registration (energy, dollar, global IP): a proxy licenses",
        "state-enrichment candidacy only. Interpretation AFTER the print.", "",
        "## CI1a — metals-vs-ags variance shift (Jacks, annual)", "",
        f"- std of 3y Δ(metals_rel): 1950-1999 **{pre.std():.3f}** vs 2000-2015 "
        f"**{post.std():.3f}** — ratio **{ratio:.2f}x** (bar ≥ 1.5x): **{ci1a}**.", "",
        "## CI1b — named-pulse sign check (IMF monthly, n=2, tiny — stated)", "",
        *[f"- {k}: cumulative metals-minus-ags log change **{v:+.3f}**" for k, v in checks.items()],
        f"- Positive: **{npos}/2** (bar 2/2): **{ci1b}**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "rel_annual": [[int(y), round(float(v), 3)] for y, v in rel.dropna().loc[1950:].items()],
        "ratio": round(ratio, 2),
        "rel_monthly": [[str(i.date())[:7], round(float(v), 3)]
                        for i, v in m_rel.dropna().items()],
        "windows": wins, "checks": {k: round(v, 3) for k, v in checks.items()}},
        separators=(",", ":")))
    print(f"CI1a {ci1a} (ratio {ratio:.2f}x) | CI1b {ci1b} ({npos}/2: "
          + ", ".join(f'{k} {v:+.2f}' for k, v in checks.items()) + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
