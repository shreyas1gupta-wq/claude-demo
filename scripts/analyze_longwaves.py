#!/usr/bin/env python3
"""Atlas 1.4 (Kondratieff rejection) — real-data leg. Trials KW1-KW2, PRE-REGISTERED.

KW1: 45-60y wave in the chained Jacks real commodity index (extrema machinery as CS1,
min_gap 25y). Bar: trough count in [2,4] AND >=50% of spacings in [45,60]y.
KW2: Kondratieff's actual object — price waves. JST cpi -> rolling 10y mean inflation for
UK/USA/France, same machinery. Bar: pooled median spacing in [45,60]y AND >=50% in-window.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

OUT = ROOT / "research" / "cycles" / "longwaves" / "longwaves-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/longwaves-charts.json")


def extrema(series: pd.Series, min_gap: int = 25):
    s = series.rolling(3, center=True).mean().dropna()
    years, vals = s.index.to_numpy(), s.to_numpy()
    peaks, troughs = [], []
    for i in range(1, len(vals) - 1):
        if vals[i] >= vals[i - 1] and vals[i] > vals[i + 1]:
            if not peaks or years[i] - peaks[-1] >= min_gap:
                peaks.append(int(years[i]))
        if vals[i] <= vals[i - 1] and vals[i] < vals[i + 1]:
            if not troughs or years[i] - troughs[-1] >= min_gap:
                troughs.append(int(years[i]))
    return peaks, troughs


def main() -> int:
    # KW1 — chained Jacks index (CS1b construction, verbatim)
    j = pd.read_csv(ROOT / "ingest/vault/commodities/jacks_real_commodity_prices_1850_2015.csv"
                    ).set_index("Year").drop(columns=["Entity"])
    chain = np.log(j).diff().mean(axis=1).fillna(0).cumsum()
    pk1, tr1 = extrema(chain)
    sp1 = [b - a for a, b in zip(tr1, tr1[1:])]
    in1 = [s for s in sp1 if 45 <= s <= 60]
    kw1_ok = (2 <= len(tr1) <= 4) and (len(sp1) > 0 and len(in1) / len(sp1) >= 0.5)

    # KW2 — JST cpi -> 10y mean inflation, UK/USA/France
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "cpi"]]
    sp2, chrono = [], {}
    for c in ("UK", "USA", "France"):
        d = df[df.country == c].set_index("year").cpi.astype(float)
        infl = np.log(d).diff().rolling(10).mean()
        pk, tr = extrema(infl.dropna())
        chrono[c] = {"peaks": pk, "troughs": tr}
        sp2 += [b - a for a, b in zip(tr, tr[1:])]
    in2 = [s for s in sp2 if 45 <= s <= 60]
    kw2_ok = (len(sp2) > 0 and 45 <= float(np.median(sp2)) <= 60
              and len(in2) / len(sp2) >= 0.5)

    res = [
        "# Atlas 1.4 — Kondratieff: the desk's own numbers (KW1-KW2, pre-registered)", "",
        "Bars pre-registered in the trial ledger before this ran; interpretation AFTER the",
        "print. Machinery identical to RE1/CS1 (one-sided, expanding-consistent), min_gap 25y.", "",
        "## KW1 — the 45-60y wave in real commodity prices (Jacks chained index, 1850-2015)", "",
        f"- Troughs: {tr1} (peaks {pk1}); spacings {sp1};",
        f"  in [45,60]y: {len(in1)}/{len(sp1)}.",
        f"- Bar (2-4 troughs AND ≥50% spacings in-window): **{'PASS' if kw1_ok else 'FAIL'}**.", "",
        "## KW2 — price waves, Kondratieff's own object (JST cpi, 10y mean inflation; UK/USA/France)", "",
        *[f"- {c}: troughs {v['troughs']}, peaks {v['peaks']}" for c, v in chrono.items()],
        f"- Pooled spacings {sorted(sp2)}: median "
        f"{float(np.median(sp2)) if sp2 else float('nan'):.0f}y; in [45,60]y: {len(in2)}/{len(sp2)}.",
        f"- Bar (median in [45,60] AND ≥50% in-window): **{'PASS' if kw2_ok else 'FAIL'}**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "kw1_troughs": tr1, "kw1_peaks": pk1, "kw1_spacings": sp1,
        "kw2": chrono, "kw2_spacings": sorted(sp2),
        "infl_uk": [[int(y), None if np.isnan(v) else round(float(v) * 100, 2)]
                    for y, v in (np.log(df[df.country == 'UK'].set_index('year').cpi.astype(float))
                                 .diff().rolling(10).mean()).items()],
    }, separators=(",", ":")))
    print(f"KW1 {'PASS' if kw1_ok else 'FAIL'} (troughs {len(tr1)}, in-window {len(in1)}/{len(sp1)}) | "
          f"KW2 {'PASS' if kw2_ok else 'FAIL'} (median {float(np.median(sp2)) if sp2 else float('nan'):.0f}y, "
          f"in-window {len(in2)}/{len(sp2)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
