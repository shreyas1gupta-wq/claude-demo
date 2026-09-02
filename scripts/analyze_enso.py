#!/usr/bin/env python3
"""Atlas 2.14 — EN1-EN3, PRE-REGISTERED: the physics clock, on vaulted El Niño-region SSTs.

Anomalies: by-month standardized, 3-month centered smooth. Episode onset: first month of a
run >= +0.5 sigma lasting >= 5 months (El Niño); <= -0.5 for La Niña. EN1 bar: El Niño
onset-to-onset spacing median in [2,7]y AND >=70% in [2,7]y. EN2/EN3: measurements, prior set.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "enso-deep" / "enso-RESULTS.md"
CHART = Path("/tmp/claude-0/-home-user-claude-demo/0aa565a7-7106-5915-a7bc-1374e0ec253a"
             "/scratchpad/enso-charts.json")


def onsets_of(z: pd.Series, thresh: float, min_run: int = 5):
    above = (z >= thresh) if thresh > 0 else (z <= thresh)
    out, run = [], 0
    for i, flag in enumerate(above.to_numpy()):
        run = run + 1 if flag else 0
        if run == min_run:
            out.append(above.index[i - min_run + 1])
    return out


def main() -> int:
    d = pd.read_csv(ROOT / "ingest/vault/climate/elnino_sst_1950_2010.csv").set_index("YEAR")
    z = (d - d.mean()) / d.std()
    long = z.stack()
    long.index = [y + (list(d.columns).index(m)) / 12 for y, m in long.index]
    s = pd.Series(long.values, index=long.index).sort_index()
    sm = s.rolling(3, center=True).mean().dropna()

    el = onsets_of(sm, +0.5)
    la = onsets_of(sm, -0.5)
    sp = [round(float(b - a), 2) for a, b in zip(el, el[1:])]
    med = float(np.median(sp))
    share = np.mean([2 <= v <= 7 for v in sp])
    en1 = "PASS" if (2 <= med <= 7) and share >= 0.7 else "FAIL"

    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv", na_values=["NA"])
    f["Year"] = f.Date.str[:4].astype(int)
    ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))
    el_years = sorted({int(t) for t in el if 1994 <= t <= 2010})
    r_el = [float(ind.loc[y]) for y in el_years if y in ind.index]
    all_mean = float(ind.loc[1994:2010].mean())

    sign = np.sign(sm)
    persist = float((sign.diff().fillna(0) == 0).iloc[1:].mean())

    res = [
        "# Atlas 2.14 — ENSO: the physics clock (EN1-EN3, pre-registered)", "",
        "Vault authenticated (EA1a-c, first run). Onset rule declared at registration.", "",
        "## EN1 — quasi-periodicity: the frequency sweep's control group", "",
        f"- El Niño onsets (n={len(el)}): {[round(float(t),1) for t in el]}",
        f"- Spacings: {sp}; median **{med:.1f}y**; share in [2,7]y **{share*100:.0f}%**.",
        f"- Bar (median in [2,7] AND ≥70% in [2,7]): **{en1}**.",
        f"- La Niña onsets for the record (n={len(la)}): {[round(float(t),1) for t in la]}", "",
        "## EN2 — El Niño-onset years vs India factor (measurement, n tiny)", "",
        f"- Onset years in the overlap 1994-2010: {el_years}; India returns those years: "
        f"{[f'{r*100:+.0f}%' for r in r_el]}; mean **{np.mean(r_el)*100:+.1f}%** vs all-years "
        f"mean **{all_mean*100:+.1f}%** (n={len(r_el)} — no bar, prior set).", "",
        "## EN3 — monthly sign persistence (forecastability shadow)", "",
        f"- P(smoothed anomaly sign persists next month): **{persist*100:.0f}%**.", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res) + "\n")
    CHART.write_text(json.dumps({
        "anom": [[round(float(t), 3), round(float(v), 2)] for t, v in sm.items()],
        "el_onsets": [round(float(t), 2) for t in el],
        "la_onsets": [round(float(t), 2) for t in la],
        "spacings": sp}, separators=(",", ":")))
    print(f"EN1 {en1} (n={len(el)}, med {med:.1f}y, {share*100:.0f}% in [2,7]) | "
          f"EN2 onset-yrs mean {np.mean(r_el)*100:+.1f}% vs {all_mean*100:+.1f}% (n={len(r_el)}) | "
          f"EN3 persist {persist*100:.0f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
