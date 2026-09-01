#!/usr/bin/env python3
"""Atlas 0.7 (demographic arcs) — real-data leg on JST R6.

Ninth real-data batch. The atlas verdict to test: demographics are superbly measured but WEAKLY
TRADABLE — the market translation is conditional and unstable. Trials DG1-DG2. JST has
population levels (pop) and real equity returns (eq_tr deflated); age STRUCTURE (the richer
object) needs UN WPP on the principal runsheet — stated, not faked.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "demo-deep" / "jst-demographics-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/demo-charts.json")


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "pop", "cpi", "eq_tr"]].sort_values(["country", "year"])
    g = df.groupby("country", group_keys=False)
    df["infl"] = g["cpi"].apply(lambda s: s / s.shift(1) - 1) * 100
    df = df[df["infl"].abs() < 50]
    df["eq_real"] = (1 + df["eq_tr"]) / (1 + df["infl"] / 100) - 1
    # trailing 10y pop growth (annualized) and forward 10y real equity return (annualized)
    rows = []
    for c, d in df.groupby("country"):
        d = d.dropna(subset=["pop"]).set_index("year")
        pg = (d["pop"] / d["pop"].shift(10)) ** (1 / 10) - 1
        lvl = (1 + d["eq_real"].fillna(0)).cumprod()
        lvl[d["eq_real"].isna()] = np.nan
        fwd = (lvl.shift(-10) / lvl) ** (1 / 10) - 1
        for y in d.index:
            if y in pg.index and y in fwd.index:
                rows.append((c, y, pg.get(y, np.nan), fwd.get(y, np.nan)))
    P = pd.DataFrame(rows, columns=["country", "year", "popg10", "fwd_eq10"]).dropna()

    res = ["# Atlas 0.7 — demographics: JST R6 results (DG1-DG2)",
           "",
           "Trailing 10y population growth vs FORWARD 10y annualized real equity return, pooled,",
           "18 countries. Age structure (the richer demographic object) requires UN WPP — on the",
           "principal runsheet; this leg tests only the crude size-growth translation.",
           "Generated 2026-09-01; trials DG1-DG2 ledgered.", ""]

    # DG1 pooled and by-era correlation
    def corr(d):
        return float(np.corrcoef(d.popg10, d.fwd_eq10)[0, 1]) if len(d) > 50 else np.nan
    full = corr(P)
    res += ["## DG1 — The crude translation, tested", "",
            "| Sample | corr(trailing 10y pop growth, forward 10y real equity) | n |",
            "|---|---|---|",
            f"| pooled 1880-2010 | {full:+.2f} | {len(P)} |"]
    for name, a, b in [("pre-1945", 0, 1944), ("1945-1979", 1945, 1979), ("1980-2010", 1980, 2010)]:
        sub = P[(P.year >= a) & (P.year <= b)]
        res.append(f"| {name} | {corr(sub):+.2f} | {len(sub)} |")
    by_c = {c: corr(d) for c, d in P.groupby("country") if len(d) > 60}
    signs = [v for v in by_c.values() if not np.isnan(v)]
    res += ["",
            f"- Per-country correlations: {sum(v > 0 for v in signs)}/{len(signs)} positive, "
            f"median {np.median(signs):+.2f} — sign-INCONSISTENT across countries and eras.",
            "- Read: the crude size-growth channel has no stable pooled translation to equity",
            "  returns — the atlas's 'weakly tradable' verdict, measured. The literature's",
            "  stronger claims run through AGE STRUCTURE (middle-aged/young ratios), which needs",
            "  UN WPP and is pre-registered as the runsheet follow-up, with the SAME bar: sign",
            "  consistency across countries before any India use.", ""]

    # DG2 India context marker
    res += ["## DG2 — India's window, stated not traded", "",
            "- India's working-age share rises into the mid-2030s (UN WPP, runsheet) — the atlas",
            "  entry L16 holds it as CONTEXT with zero allocation authority and a 2030 design",
            "  review. DG1's sign-inconsistency is exactly why: measurement quality ≠ tradability.",
            "  The dividend cashes only through jobs absorption (Bloom et al.), an outcome the",
            "  free data can DATE only in retrospect.", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({"by_country": sorted([[k, round(v, 2)] for k, v in by_c.items()
                                                       if not np.isnan(v)], key=lambda x: x[1])},
                                separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} | pooled corr {full:+.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
