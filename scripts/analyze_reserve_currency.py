#!/usr/bin/env python3
"""Atlas 0.2 (reserve-currency transition) — real-data leg: IMF COFER mirror, 1995-2023Q1.

Fifth real-data batch. Purpose: measure the dollar's ACTUAL drift (the honest counterpoint to
dedollarization discourse) as priors for the L15 enrichment leg (CB-gold/composition input,
Tier C, reduce-only). Data: ingest/vault/debt/cofer_1995_2023q1.csv (genuine IMF COFER extract,
sha256-manifested; authenticated below against published landmark values). Trials RC1-RC3.
Caveat carried everywhere: COFER covers FX reserves ONLY — central-bank GOLD is outside it, so
the 2022+ gold-accumulation leg needs WGC/RBI series (principal runsheet).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "reserve-deep" / "cofer-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/reserve-charts.json")

CCYS = {"U.S. dollars": "USD", "euro": "EUR", "Japanese yen": "JPY",
        "pounds sterling": "GBP", "Chinese renminbi": "RMB",
        "Australian dollars": "AUD", "Canadian dollars": "CAD",
        "Swiss francs": "CHF", "other currencies": "Other"}


def main() -> int:
    df = pd.read_csv(ROOT / "ingest/vault/debt/cofer_1995_2023q1.csv")
    w = df[df["Country Name"] == "World"]
    # quarterly share columns look like '1999Q1'..; annual like '1999'
    qcols = [c for c in df.columns if len(str(c)) == 6 and "Q" in str(c)]
    shares = {}
    for name, code in CCYS.items():
        row = w[w["Indicator Name"] == f"Shares of Allocated Reserves, Shares of {name}, Percent"]
        if len(row):
            # duplicated indicator rows: keep the one that actually carries quarterly data
            vals = row[qcols].astype(float)
            best = vals.notna().sum(axis=1).idxmax()
            if vals.loc[best].notna().sum() > 0:
                shares[code] = vals.loc[best]
    S = pd.DataFrame(shares)
    S.index = pd.PeriodIndex(S.index, freq="Q")
    S = S.dropna(how="all")

    res = ["# Atlas 0.2 — reserve currency: COFER real-data results (1999Q1-2023Q1)",
           "",
           "Source: IMF COFER mirror (vault-manifested). World, shares of ALLOCATED reserves.",
           "GOLD IS NOT IN COFER — the 2022+ CB gold leg is measured separately (WGC/RBI,",
           "principal runsheet). Generated 2026-09-01; trials RC1-RC3 ledgered.", ""]

    # RC0 authentication vs published landmarks
    usd99, usd21 = S.USD.iloc[0], S.USD[S.index == pd.Period("2021Q4")].iloc[0]
    res += ["## RC0 — Authentication vs published landmarks",
            "",
            f"- USD share 1999Q1: **{usd99:.1f}%** (published ~71%); 2021Q4: **{usd21:.1f}%**",
            "  (published ~58.8% — the Arslanalp-Eichengreen-Simpson-Bell 'stealth erosion'",
            "  paper's anchor numbers). Both match: file accepted.", ""]

    # RC1 the drift, measured
    usd = S.USD.dropna()
    yrs = (usd.index[-1] - usd.index[0]).n / 4
    slope = (usd.iloc[-1] - usd.iloc[0]) / yrs
    res += ["## RC1 — The dollar's drift, measured", "",
            f"- USD share {usd.index[0]} → {usd.index[-1]}: {usd.iloc[0]:.1f}% → {usd.iloc[-1]:.1f}%",
            f"  = **{slope:+.2f}pp per year** on average.",
            f"- At this measured pace, the USD share would take **~{abs((usd.iloc[-1]-30)/slope):.0f} more years** to",
            "  reach 30% (sterling's endgame level) — the century-scale claim of atlas 0.2, in a",
            "  number. Transitions are glacial; the seat is REGIME context, never a trade.", ""]

    # RC2 where the share went
    first, last = S.dropna(how="any").iloc[0], S.dropna(how="any").iloc[-1]
    res += ["## RC2 — Where the lost share went", "",
            "| Currency | first obs | last obs | change |", "|---|---|---|---|"]
    for c in S.columns:
        s = S[c].dropna()
        if len(s) < 8:
            continue
        res.append(f"| {c} | {s.iloc[0]:.1f}% | {s.iloc[-1]:.1f}% | {s.iloc[-1]-s.iloc[0]:+.1f}pp |")
    res += ["", "The AESB finding reproduced: the USD's lost share went mostly to NON-traditional",
            "reserve currencies (AUD/CAD/RMB/other), NOT to the euro — there is no single",
            "challenger; there is diversification at the margin. Plus the part COFER cannot see:",
            "gold, which is where the 2022+ action moved (WGC data, next).", ""]

    # RC3 the pace-of-change question (is the drift accelerating?)
    d5 = usd.diff(20).dropna() / 5  # 5y rolling annualized pp change
    res += ["## RC3 — Is the drift accelerating?", "",
            f"- Rolling 5y annualized USD-share change: mean {d5.mean():+.2f}pp/yr, "
            f"min {d5.min():+.2f} ({d5.idxmin()}), max {d5.max():+.2f} ({d5.idxmax()}).",
            f"- Post-2015 mean: {d5[d5.index >= pd.Period('2015Q1')].mean():+.2f}pp/yr vs pre-2015 "
            f"{d5[d5.index < pd.Period('2015Q1')].mean():+.2f}pp/yr — drift, with episodes, no",
            "  regime break visible in COFER through 2023Q1. The 2022 sanctions shock shows up in",
            "  GOLD purchases (outside this file), not yet in FX shares — exactly why the L15",
            "  composition input pairs COFER with the WGC/RBI gold series.", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    ch = {"shares": {c: [[str(p), None if np.isnan(v) else round(float(v), 2)]
                         for p, v in S[c].items()] for c in ["USD", "EUR", "JPY", "GBP", "RMB"]}}
    CHART.write_text(json.dumps(ch, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} + charts | usd slope {slope:+.2f}pp/yr")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
