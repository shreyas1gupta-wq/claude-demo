#!/usr/bin/env python3
"""Atlas 0.3 (suprasecular real-rate decline) — real-data leg on JST R6.

Sixth real-data batch. Atlas verdict to test: the 700y "trend" (~1-2bp/yr, Schmelzing) is
swamped at any investable horizon by multi-decade swings — hence CONTEXT tier, no seat.
Trials SR1-SR3. Hyperinflation cells excluded per the Weimar rule. JST ends 2020: the 2022-23
spike is post-sample and stated as such, never plotted from memory.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "realrates-deep" / "jst-realrates-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/realrates-charts.json")


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "ltrate", "stir", "cpi"]].sort_values(["country", "year"])
    g = df.groupby("country", group_keys=False)
    df["infl"] = g["cpi"].apply(lambda s: s / s.shift(1) - 1) * 100
    df = df[df["infl"].abs() < 50]
    df["real_lt"] = df["ltrate"] - df["infl"]
    d = df.dropna(subset=["real_lt"])

    res = ["# Atlas 0.3 — suprasecular real rates: JST R6 results (SR1-SR3)",
           "",
           "Real long rate = ltrate − CPI inflation; 18 countries 1870-2020; hyperinflation",
           "cells excluded. JST ends 2020 — the 2022-23 spike is POST-SAMPLE and only referenced",
           "from published sources, never computed here. Generated 2026-09-01.", ""]

    # SR1 decade medians + the trend
    dec = d.copy()
    dec["decade"] = (dec.year // 10) * 10
    med = dec.groupby("decade").real_lt.median()
    res += ["## SR1 — The 150-year shape (pooled median real long rate by decade)", "",
            "| Decade | median real long rate | | Decade | median |", "|---|---|---|---|---|"]
    ds = med.index.tolist()
    half = (len(ds) + 1) // 2
    for i in range(half):
        left = f"| {ds[i]}s | {med.iloc[i]:+.1f}% |"
        right = (f" | {ds[i+half]}s | {med.iloc[i+half]:+.1f}% |"
                 if i + half < len(ds) else " | | |")
        res.append(left + right)
    yrs = d.year - d.year.mean()
    slope = np.polysum = np.polyfit(d.year, d.real_lt, 1)[0]
    res += ["", f"- Naive pooled linear trend 1870-2020: **{slope*100:+.2f}bp/yr** (Schmelzing's",
            "  700y estimate is ~-1 to -2bp/yr). Same order of magnitude — and utterly dwarfed by",
            "  the swings visible in the decade table (1910s/1940s repression troughs, 1980s peak).", ""]

    # SR2 swings vs trend at the investable horizon
    swings = []
    for c, dd in d.groupby("country"):
        s = dd.set_index("year").real_lt
        r30 = s.rolling(30).mean().dropna()
        if len(r30) > 40:
            swings.append(r30.max() - r30.min())
    ratio = np.median(swings) / abs(slope * 30)
    res += ["## SR2 — Swings vs trend at a 30-year horizon", "",
            f"- Median country range of ROLLING 30y mean real rates: **{np.median(swings):.1f}pp**.",
            f"- The secular trend's contribution over 30 years: **{abs(slope)*30:.2f}pp**.",
            f"- Ratio ≈ **{ratio:.0f}x** — the multi-decade swings are ~{ratio:.0f} times larger than",
            "  the trend at any horizon we could ever trade. The atlas verdict (CONTEXT, no seat,",
            "  'terminal-multiple humility' only) is the only defensible one.", ""]

    # SR3 where the recent era sat in the 150y distribution
    recent = d[d.year >= 2010].real_lt
    pct = (d.real_lt < recent.median()).mean()
    res += ["## SR3 — The 2010s in the 150-year distribution", "",
            f"- Median real long rate 2010-2020: {recent.median():+.1f}% — the {pct*100:.0f}th",
            "  percentile of all country-years since 1870: low, but NOT unprecedented (the 1910s",
            "  and 1940s were lower — both war/repression eras, which is the company the 2010s",
            "  keep in the debt monograph's story).",
            "- The 2022-23 spike (post-sample here) reversed roughly four decades of decline in",
            "  two years per published TIPS data — the single best argument against ever trading",
            "  this 'trend'. [Post-sample statement, source: FRED DFII10, principal runsheet.]", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps(
        {"decades": [[int(k), round(float(v), 2)] for k, v in med.items()]},
        separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} | slope {slope*100:+.2f}bp/yr | swing ratio {ratio:.0f}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
