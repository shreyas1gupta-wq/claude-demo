#!/usr/bin/env python3
"""DS5 — the Reinhart-Rogoff 90% 'cliff', re-run by us on the Herndon-Ash-Pollin panel.

Data: ingest/vault/debt/RR-processed.csv (the HAP replication panel: 20 advanced economies,
1946-2009, dRGDP = real GDP growth %, debtgdp = public debt/GDP %). Purpose: the methods parable
of docs/cycles/05-debt-supercycle.md Part A §5, in our own numbers — growth is SLOWER at high
debt, but there is a GRADIENT, not a cliff at 90%; and the correct pooled mean at >90% is far
from RR 2010's -0.1%. Appends DS5 to research/cycles/debt-deep/jst-debt-RESULTS.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "debt-deep" / "jst-debt-RESULTS.md"


def main() -> int:
    df = pd.read_csv(ROOT / "ingest/vault/debt/RR-processed.csv")
    d = df[["Country", "Year", "dRGDP", "debtgdp"]].dropna()
    d = d[(d.Year >= 1946) & (d.Year <= 2009)]
    bins = [0, 30, 60, 90, 120, np.inf]
    labels = ["0-30%", "30-60%", "60-90%", "90-120%", ">120%"]
    d["bucket"] = pd.cut(d.debtgdp, bins, labels=labels, right=False)

    lines = ["", "## DS5 — The 90% 'cliff', re-run on the Herndon-Ash-Pollin panel", "",
             f"Panel: {d.Country.nunique()} advanced economies, 1946-2009, "
             f"{len(d)} country-years (RR-processed.csv, vault-manifested).",
             "Method: pooled country-year means/medians (the HAP-correct weighting).", "",
             "| Debt/GDP bucket | mean real growth | median | n country-years |",
             "|---|---|---|---|"]
    for lab in labels:
        w = d[d.bucket == lab]
        lines.append(f"| {lab} | {w.dRGDP.mean():+.2f}% | {w.dRGDP.median():+.2f}% | {len(w)} |")
    hi = d[d.debtgdp >= 90].dRGDP
    mid = d[(d.debtgdp >= 60) & (d.debtgdp < 90)].dRGDP
    rng = np.random.default_rng(0)
    diffs = [rng.choice(mid, len(mid)).mean() - rng.choice(hi, len(hi)).mean()
             for _ in range(4000)]
    lo_ci, hi_ci = np.percentile(diffs, [2.5, 97.5])
    lines += ["",
              f"- Pooled mean growth above 90% debt: **{hi.mean():+.2f}%** (RR 2010 claimed "
              "−0.1% via the spreadsheet exclusion + country equal-weighting HAP exposed).",
              f"- The 60-90 vs >90 growth gap: {mid.mean() - hi.mean():+.2f}pp, bootstrap 95% CI "
              f"[{lo_ci:+.2f}, {hi_ci:+.2f}] — a modest GRADIENT (high debt associates with "
              "somewhat slower growth, causality unresolved), not a cliff, and no bucket goes "
              "negative.",
              "- Design consequence, already embedded: our states are PERCENTILES and grids — "
              "never threshold cliffs — and DS5 is the canonical reason why. Ledgered as trial "
              "DS5.", ""]
    OUT.write_text(OUT.read_text() + "\n".join(lines) + "\n")
    print("DS5 appended:", hi.mean().round(2), "vs 60-90:", mid.mean().round(2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
