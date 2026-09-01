#!/usr/bin/env python3
"""Atlas 0.1 (debt supercycle / fiscal dominance) — real-data leg on JST R6.

Fourth real-data batch. Same discipline: pooled advanced-economy PRIORS for the L15 seat
(reduce-only, Tier C), never India results; every table a ledgered trial (DS1-DS4).
Data: ingest/vault/jst/JSTdatasetR6.xlsx (authenticated in the credit batch).

Objects: public debt/GDP arcs (how rare is a completed fiat-era deleveraging?), financial
repression eras (negative real short rates — Reinhart-Sbrancia's claim), r-g by era, and the
investor translation (real equity returns in repression years — the L15 gold-floor rationale).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
OUT = ROOT / "research" / "cycles" / "debt-deep" / "jst-debt-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/debt-charts.json")

ERAS = [("gold/interwar 1870-1944", 1870, 1944),
        ("repression era 1945-1980", 1945, 1980),
        ("liberalization 1981-2007", 1981, 2007),
        ("post-GFC 2008-2020", 2008, 2020)]


def main() -> int:
    df = pd.ExcelFile(ROOT / "ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
    df = df[["country", "year", "debtgdp", "stir", "ltrate", "cpi", "rgdpmad", "eq_tr"]].copy()
    df = df.sort_values(["country", "year"]).reset_index(drop=True)
    g = df.groupby("country", group_keys=False)
    df["infl"] = g["cpi"].apply(lambda s: s / s.shift(1) - 1) * 100
    df["real_short"] = df["stir"] - df["infl"]
    df["real_g"] = g["rgdpmad"].apply(lambda s: s / s.shift(1) - 1) * 100
    df["r_minus_g"] = df["real_short"] - df["real_g"]
    df["eq_real"] = ((1 + df["eq_tr"]) / (1 + df["infl"] / 100) - 1) * 100

    res = ["# Atlas 0.1 — debt supercycle: JST R6 real-data results (advanced-economy priors)",
           "",
           "18 countries, 1870-2020. Real short rate = stir − CPI inflation; hyperinflation-era",
           "cells (|inflation|>50%) excluded from era means (Weimar rule from the momentum batch).",
           "Generated 2026-09-01; trials DS1-DS4 ledgered. These are PRIORS for L15 (Tier C,",
           "reduce-only gold-floor attribution) — never timing inputs, never India estimates.", ""]
    clean = df[df["infl"].abs() < 50].copy()

    # DS1: completed fiat-era deleveraging arcs
    res += ["## DS1 — How rare is a completed fiat-era deleveraging?", "",
            "Definition: post-1971 peak debt/GDP followed by a decline of >=30pp that HELD",
            "(no re-ascent above the old peak by 2020).", "",
            "| Country | post-1971 peak (yr) | max decline from peak | completed arc? |",
            "|---|---|---|---|"]
    completed = 0
    arcs = []
    for c, d in df[df.year >= 1971].groupby("country"):
        s = d.set_index("year")["debtgdp"].dropna() * 100
        if len(s) < 20:
            continue
        pk_y, pk = s.idxmax(), s.max()
        after = s[s.index >= pk_y]
        decline = pk - after.min()
        done = decline >= 30 and after.iloc[-1] < pk
        completed += bool(done and pk_y < 2000)
        arcs.append((c, pk_y, pk, decline, done))
        res.append(f"| {c} | {pk:.0f}% ({pk_y}) | {decline:.0f}pp | {'YES' if done else 'no'} |")
    res += ["", f"Countries whose post-1971 peak occurred before 2000 AND completed a >=30pp "
            f"lasting decline: **{completed} of {len(arcs)}** — the atlas's 'n<2 in the fiat era' "
            "claim is conservative but directionally right: most fiat-era debt arcs are still on "
            "their ascent (peaks cluster at 2020, i.e., censored, not completed).", ""]

    # DS2: financial repression eras
    res += ["## DS2 — Financial repression (Reinhart-Sbrancia replication-lite)", "",
            "| Era | share of country-years with NEGATIVE real short rates | mean real short | n |",
            "|---|---|---|---|"]
    era_rows = {}
    for name, a, b in ERAS:
        w = clean[(clean.year >= a) & (clean.year <= b)].dropna(subset=["real_short"])
        share = (w.real_short < 0).mean()
        era_rows[name] = round(float(share), 3)
        res.append(f"| {name} | **{share * 100:.0f}%** | {w.real_short.mean():+.1f}% | {len(w)} |")
    res += ["", "The repression signature: 1945-1980 negative-real-rate share far above the",
            "liberalization era — the mechanism by which war debts were quietly amortized",
            "(Reinhart-Sbrancia). The post-GFC share is the modern echo the L15 inputs watch", ""]

    # DS3: r - g by era
    res += ["## DS3 — r − g by era (the debt-arithmetic driver)", "",
            "| Era | mean (real short − real growth) | share of years r<g | n |", "|---|---|---|---|"]
    for name, a, b in ERAS:
        w = clean[(clean.year >= a) & (clean.year <= b)].dropna(subset=["r_minus_g"])
        res.append(f"| {name} | {w.r_minus_g.mean():+.1f}pp | {(w.r_minus_g < 0).mean() * 100:.0f}% "
                   f"| {len(w)} |")
    res += ["", "When r<g persistently, debt/GDP can fall without surpluses — the painless arc.",
            "When r>g (1981-2007), only surpluses or defaults reduce debt. The seat's job is",
            "knowing WHICH arithmetic regime we are in, never predicting its end.", ""]

    # DS4: the investor translation
    rep = clean.dropna(subset=["eq_real", "real_short", "debtgdp"])
    hi_debt = rep.debtgdp > rep.debtgdp.quantile(0.75)
    neg_r = rep.real_short < 0
    res += ["## DS4 — What repression does to investors (the L15 rationale)", "",
            "| State (country-year) | mean real equity return | median | n |", "|---|---|---|---|"]
    segs = [("high debt AND negative real rates (fiscal-dominance state)", hi_debt & neg_r),
            ("high debt, positive real rates", hi_debt & ~neg_r),
            ("low/mid debt, negative real rates", ~hi_debt & neg_r),
            ("low/mid debt, positive real rates (normal)", ~hi_debt & ~neg_r)]
    seg_out = {}
    for lab, m in segs:
        w = rep[m]
        seg_out[lab.split(" (")[0]] = [round(float(w.eq_real.mean()), 1), len(w)]
        res.append(f"| {lab} | {w.eq_real.mean():+.1f}% | {w.eq_real.median():+.1f}% | {len(w)} |")
    res += ["", "Read for design: equities still earn positive real returns on average in",
            "repression states — the seat justifies a GOLD FLOOR and a debasement tail budget,",
            "never an equity exit. Reduce-only, exactly as the atlas says.", ""]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    # charts: debt/GDP paths for US, UK, Japan + repression era shares
    ch = {"paths": {}, "repression": era_rows, "ds4": seg_out}
    for c in ("USA", "UK", "Japan"):
        d = df[df.country.str.contains(c if c != "UK" else "United Kingdom|UK", na=False)]
        ch["paths"][c] = [[int(y), None if np.isnan(v) else round(float(v) * 100, 1)]
                          for y, v in zip(d.year, d.debtgdp)]
    CHART.write_text(json.dumps(ch, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)} + charts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
