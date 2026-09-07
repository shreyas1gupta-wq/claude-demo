"""DB-D1..D5 — the debt battery (levels, the >=100% outlier club, acceleration, US arc,
twin peaks). Registered 2026-09-07 BEFORE this run. Prints only."""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "bond_tr", "debtgdp", "tloans", "gdp",
         "crisisJST"]].sort_values(["country", "year"])

frames = []
for c, g in df.groupby("country"):
    g = g.set_index("year").copy()
    g["infl"] = g.cpi.pct_change()
    g["req"] = (1 + g.eq_tr) / (1 + g.infl) - 1
    g["rbond"] = (1 + g.bond_tr) / (1 + g.infl) - 1
    g["priv"] = g.tloans / g.gdp
    g["pub_pct"] = expanding_percentile(g.debtgdp.to_numpy(), min_obs=20)
    g["priv_pct"] = expanding_percentile(g.priv.to_numpy(), min_obs=20)
    g["dpub5"] = g.debtgdp.diff(5)
    g["dpriv5"] = g.priv.diff(5)
    g["dpriv5_pct"] = expanding_percentile(g.dpriv5.to_numpy(), min_obs=20)
    for h in (5, 10):
        g[f"feq{h}"] = np.log1p(g.req).rolling(h).mean().shift(-h).apply(np.expm1)
        g[f"fbd{h}"] = np.log1p(g.rbond).rolling(h).mean().shift(-h).apply(np.expm1)
    g["finfl10"] = g.infl.rolling(10).mean().shift(-10)
    g["crisis3"] = g.crisisJST.fillna(0).rolling(3).max().shift(-3)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)

print("DB-D1 — debt LEVELS (own-country percentile) -> future real equity, pooled Spearman:")
for k, lab in [("pub_pct", "public debt"), ("priv_pct", "private credit")]:
    for h in (5, 10):
        j = p[[k, f"feq{h}"]].dropna()
        print(f"  {lab:15} -> next-{h}y: rho {stats.spearmanr(j.iloc[:,0], j.iloc[:,1])[0]:+.2f} (n={len(j)})")

# DB-D2: the >=100% club
hi = p[p.debtgdp >= 1.0].dropna(subset=["debtgdp"])
episodes = []
for c, g in hi.groupby("country"):
    yrs = sorted(g.year)
    start = yrs[0]
    prev = yrs[0]
    for y in yrs[1:] + [None]:
        if y is None or y - prev > 5:
            episodes.append((c, int(start), int(prev)))
            start = y
        prev = y if y else prev
print(f"\nDB-D2(d1) >=100% public-debt club: {len(hi)} country-years, {len(episodes)} episodes:")
print("   " + "; ".join(f"{c} {a}-{b}" for c, a, b in sorted(episodes, key=lambda x: x[1])))

def stat(s):
    s = s.dropna()
    return f"median {100*s.median():+.1f}% | %>0 {100*(s>0).mean():.0f}% (n={len(s)})"
for thr, tag in [(1.0, ">=100%"), (1.3, ">=130%")]:
    d = p[p.debtgdp >= thr]
    print(f"DB-D2 from {tag} starts: next-10y REAL BOND {stat(d.fbd10)}  ||  EQUITY {stat(d.feq10)}")

print("DB-D2(d4) resolution table (episode entry year -> debt +10y/+20y, infl next-10y):")
dbmap = {(c, int(y)): v for c, y, v in p[["country", "year", "debtgdp"]].dropna().itertuples(index=False)}
infmap = {(c, int(y)): v for c, y, v in p[["country", "year", "finfl10"]].dropna().itertuples(index=False)}
for c, a, b in sorted(episodes, key=lambda x: x[1]):
    d0, d10, d20 = dbmap.get((c, a)), dbmap.get((c, a + 10)), dbmap.get((c, a + 20))
    fi = infmap.get((c, a))
    print(f"   {c:12} {a}: {100*d0:3.0f}% -> +10y {('%3.0f%%' % (100*d10)) if d10 else ' na'}"
          f" -> +20y {('%3.0f%%' % (100*d20)) if d20 else ' na'} | infl next-10y "
          f"{('%4.1f%%' % (100*fi)) if fi is not None else '  na'}")

print("\nDB-D3 — 5y debt ACCELERATION -> next-5y returns, pooled Spearman:")
for k, y, lab in [("dpub5", "feq5", "d(public)  -> equity"), ("dpriv5", "feq5", "d(private) -> equity"),
                  ("dpriv5", "fbd5", "d(private) -> bonds "), ("dpriv5_pct", "feq5", "d(private) rank -> eq")]:
    j = p[[k, y]].dropna()
    print(f"  {lab}: rho {stats.spearmanr(j.iloc[:,0], j.iloc[:,1])[0]:+.2f} (n={len(j)})")

us = p[p.country == "USA"].set_index("year")
pk = us.debtgdp.dropna()
print(f"\nDB-D4(d1) US debt/GDP arc: 1870 {100*pk.get(1870, np.nan):.0f}% | WWI peak 1919 "
      f"{100*pk.get(1919, np.nan):.0f}% | 1933 {100*pk.get(1933, np.nan):.0f}% | WWII peak 1946 "
      f"{100*pk.get(1946, np.nan):.0f}% | 1974 trough {100*pk.get(1974, np.nan):.0f}% | 2020 {100*pk.get(2020, np.nan):.0f}%")
d = us[us.debtgdp >= 0.9]
print(f"DB-D4(d2) US years with debt >= 90% ({sorted(int(y) for y in d.index)}):")
print(f"   next-10y real equity {stat(d.feq10)} | real bond {stat(d.fbd10)} | "
      f"infl next-10y median {100*d.finfl10.median():.1f}%")

print("\nDB-D5 — twin peaks (public pct >=0.8 x private pct >=0.8):")
p["hi_pub"] = p.pub_pct >= 0.8
p["hi_priv"] = p.priv_pct >= 0.8
for hp in (False, True):
    for hv in (False, True):
        d = p[(p.hi_pub == hp) & (p.hi_priv == hv) & p.pub_pct.notna() & p.priv_pct.notna()]
        print(f"  pub_hi={int(hp)} priv_hi={int(hv)}: next-5y equity mean "
              f"{100*d.feq5.mean():+5.1f}% | crisis-in-3y rate {100*d.crisis3.mean():4.1f}% (n={len(d)})")
