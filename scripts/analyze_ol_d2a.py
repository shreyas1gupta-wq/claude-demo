"""OL-D2a — the windfall reverse experiment, run exactly as registered (2026-09-03).

Oil-DOWN years (annual log return < -log(1.10)), 1994-2015 India leg; flavor = sign of the
annual sum of Känzig supply-news shocks (negative = supply-driven). PRIMARY BAR: supply-mean
minus demand-mean >= +10pp. Desk prior: PASS at microscopic power (n~4-5); a fail refutes
nothing at this n.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"

br = pd.read_csv(V / "commodities/brent_monthly_eia.csv", parse_dates=["Date"])
br["Year"] = br.Date.dt.year
oil_ret = np.log(br.groupby("Year").Price.mean()).diff()

f = pd.read_csv(V / "factors/iima_monthly_factors.csv", na_values=["NA"])
f["Year"] = f.Date.str[:4].astype(int)
ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))

kz = pd.read_csv(V / "commodities/oil_supply_news_monthly_1975_2025.csv")
kz["Year"] = kz.date.str[:4].astype(int)
news_ann = kz.groupby("Year").news_shock.sum()

kil = pd.read_csv(V / "commodities/kilian_index_monthly_1973_2019.csv", parse_dates=["date"])
kil["Year"] = kil.date.dt.year
k_ann = kil.groupby("Year").kilian_index.mean()
k_rising = k_ann > k_ann.shift(1)

j = pd.concat([oil_ret, ind, news_ann, k_rising], axis=1,
              keys=["oil", "ind", "news", "k_rising"]).dropna(subset=["oil", "ind", "news"])
j = j.loc[1994:2015]
down = j[j.oil < -np.log(1.10)]
sup = down[down.news < 0]
dem = down[down.news >= 0]
print(f"OL-D2a: oil-DOWN years n={len(down)} -> supply-driven {len(sup)} / demand-driven {len(dem)}")
for y, r in down.iterrows():
    print(f"  {int(y)}: oil {np.expm1(r.oil)*100:+.0f}% | Känzig sum {r.news:+.2f} "
          f"({'SUPPLY' if r.news < 0 else 'DEMAND'}) | Kilian activity "
          f"{'rising' if r.k_rising else 'falling'} | India {r.ind*100:+.1f}%")

if len(sup) == 0 or len(dem) == 0:
    print("OL-D2a PRIMARY: UNTESTABLE (an empty flavor cell) — recorded, bar unmoved")
else:
    ms, md = float(sup.ind.mean()), float(dem.ind.mean())
    diff = ms - md
    verdict = "PASS" if diff >= 0.10 else "FAIL (underpowered by design — recorded, not a death)"
    print(f"OL-D2a PRIMARY: supply-driven {ms*100:+.1f}% vs demand-driven {md*100:+.1f}% -> "
          f"diff {diff*100:+.1f}pp (bar >= +10pp) -> {verdict}")

agree = int((down.news < 0).eq(down.k_rising).sum())
print(f"SECONDARY instrument agreement (Känzig supply == Kilian activity-rising): "
      f"{agree}/{len(down)} down-years")
