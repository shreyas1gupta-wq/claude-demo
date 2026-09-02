#!/usr/bin/env python3
"""Atlas 3.3/3.4 — CR1a/CR1b/CR2, PRE-REGISTERED: crash asymmetry as the crowding shadow."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "crowding-deep" / "crowding-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/crowding-charts.json")


def main() -> int:
    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv",
                    na_values=["NA"]).set_index("Date")
    stats, worst = {}, {}
    for c in ("WML", "SMB", "HML"):
        x = f[c].astype(float).dropna()
        sk = float(((x - x.mean()) ** 3).mean() / x.std() ** 3)
        wz = float((x.min() - x.mean()) / x.std())
        stats[c] = (sk, wz, str(x.idxmin()), float(x.min()))
        worst[c] = wz
    cr1a = "PASS" if (stats["WML"][0] <= -0.5 and stats["WML"][0] < stats["SMB"][0]
                      and stats["WML"][0] < stats["HML"][0]) else "FAIL"
    cr1b = "PASS" if (worst["WML"] <= -4 and worst["WML"] < worst["SMB"]
                      and worst["WML"] < worst["HML"]) else "FAIL"
    w = f.WML.astype(float).dropna()
    z25 = ((w - w.mean()) / w.std()).loc["2025-01":"2025-12"]
    hits = [(i, round(float(v), 2), round(float(w.loc[i]), 1))
            for i, v in z25.items() if v <= -2]

    res = [
        "# Atlas 3.3/3.4 — crowding: crash asymmetry on India factors (CR1-CR2, pre-registered)", "",
        "| Factor | monthly skew | worst month (own σ) | worst month (date, %) |", "|---|---|---|---|",
        *[f"| {c} | {s:+.2f} | {z:+.1f}σ | {d} ({m:+.1f}%) |"
          for c, (s, z, d, m) in stats.items()],
        "",
        f"- CR1a (skew(WML) ≤ −0.5 AND most negative): **{cr1a}**.",
        f"- CR1b (WML worst ≤ −4σ AND most extreme): **{cr1b}**.", "",
        "## CR2 — 2025 WML months at ≤ −2σ (the named mid-2025 unwind, measurement)", "",
        (f"- Hits: {hits}" if hits else "- NO 2025 month reaches −2σ in India's WML."), "",
        f"- 2025 monthly WML z-scores: {[round(float(v),1) for v in z25]}", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "stats": {c: [round(s, 2), round(z, 1), d, m] for c, (s, z, d, m) in stats.items()},
        "wml_2025": {str(i): round(float(v), 2) for i, v in z25.items()},
        "wml_hist": [round(float(v), 1) for v in w]}, separators=(",", ":")))
    print(f"CR1a {cr1a} (skews WML {stats['WML'][0]:+.2f} SMB {stats['SMB'][0]:+.2f} "
          f"HML {stats['HML'][0]:+.2f}) | CR1b {cr1b} (worst {worst['WML']:+.1f}σ vs "
          f"{worst['SMB']:+.1f}/{worst['HML']:+.1f}) | CR2 hits {len(hits)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
