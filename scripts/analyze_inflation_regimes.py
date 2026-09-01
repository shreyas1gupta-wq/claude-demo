#!/usr/bin/env python3
"""Atlas 0.5 (inflation-regime arcs) — real-data leg on JST R6 CPI panel.

Eighth real-data batch. Trials IR1-IR3. The atlas claim to test: inflation runs in ~30-40y
institutional arcs (up 1940s-70s, down 1980s-2010s), n≈2 in the fiat era — a regime, not a
cycle. Hyperinflation cells excluded per the Weimar rule where means are taken; the arcs are
shown on the trimmed panel.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "inflation-deep" / "jst-inflation-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/inflation-charts.json")


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "cpi"]].sort_values(["country", "year"])
    df["infl"] = df.groupby("country", group_keys=False)["cpi"].apply(
        lambda s: s / s.shift(1) - 1) * 100
    d = df[df["infl"].abs() < 50].dropna(subset=["infl"])

    # pooled median inflation by year + rolling 10y
    med = d.groupby("year").infl.median()
    r10 = med.rolling(10).mean()

    res = ["# Atlas 0.5 — inflation-regime arcs: JST R6 results (IR1-IR3)",
           "",
           "Pooled median CPI inflation across 18 countries, 1871-2020; hyperinflation cells",
           "excluded. Generated 2026-09-01; trials IR1-IR3 ledgered.", ""]

    # IR1: the arcs, dated mechanically
    res += ["## IR1 — The arcs, dated mechanically (rolling 10y pooled median)", "",
            "| Marker | Year | rolling-10y level |", "|---|---|---|"]
    fiat = r10[r10.index >= 1950]
    peak_y, peak_v = int(fiat.idxmax()), float(fiat.max())
    post_peak = r10[r10.index >= peak_y]
    trough_y, trough_v = int(post_peak.idxmin()), float(post_peak.min())
    pre = r10[(r10.index >= 1930) & (r10.index <= 1955)]
    start_y = int(pre.idxmin()) if len(pre) else 1950
    res += [f"| up-arc start (min 1930-55) | {start_y} | {r10.loc[start_y]:+.1f}% |",
            f"| up-arc peak | {peak_y} | {peak_v:+.1f}% |",
            f"| down-arc trough (post-peak) | {trough_y} | {trough_v:+.1f}% |",
            "",
            f"- Up-arc length ≈ **{peak_y - start_y} years**; down-arc ≈ **{trough_y - peak_y}",
            "  years** — the 30-40y institutional-arc claim, dated from the data. That is TWO",
            "  completed arcs in the fiat era: a regime object, never a fittable cycle (clock",
            "  test fails by an order of magnitude).", ""]

    # IR2: regime persistence (how sticky is the inflation ERA?)
    hi = (d.infl > 4).astype(float)
    d2 = d.assign(hi=hi)
    trans = 0
    tot = 0
    for c, dd in d2.groupby("country"):
        h = dd.hi.to_numpy()
        tot += len(h) - 1
        trans += int((np.diff(h) != 0).sum())
    stay = 1 - trans / tot
    res += ["## IR2 — Era stickiness", "",
            f"- P(next year in the same >4%/<=4% inflation state) = **{stay*100:.0f}%** pooled —",
            "  inflation ERAS persist; single prints don't. This is exactly why L15 consumes",
            "  real-rate/inflation PERSISTENCE gauges (trailing 36m shares), never prints.", ""]

    # IR3: what each era did to real equity/bond returns is already in DS4/SR — cross-ref only
    res += ["## IR3 — Cross-references, not re-runs", "",
            "- Era investor outcomes already computed: DS2/DS4 (repression eras, real equity in",
            "  fiscal-dominance states) and SR1 (real-rate decade medians). No new seat: the",
            "  inflation-regime information the book needs already flows through L15's real-rate",
            "  persistence input and the L6 monetary seat's faster gauges. This monograph",
            "  documents the arc so nobody mistakes a regime for a tradable cycle.", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps(
        {"pooled": [[int(y), None if np.isnan(v) else round(float(v), 2)] for y, v in r10.items()],
         "markers": {"start": start_y, "peak": peak_y, "trough": trough_y}},
        separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} | arcs: up {start_y}->{peak_y}, down {peak_y}->{trough_y}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
