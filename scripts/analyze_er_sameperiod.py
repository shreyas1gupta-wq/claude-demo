"""ER-D5 — same-period attribution: is the realized return explained by same-window metrics?

Registered 2026-09-05 in research/register/trial-ledger.md BEFORE this run. Prints only.
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
Y0, Y1 = 1950, 2020
HORIZONS = [1, 3, 5, 10, 20]

df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_capgain", "eq_dp", "rgdpmad"]]
df = df.sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()

frames = []
for c, gdf in df.groupby("country"):
    gdf = gdf.set_index("year").copy()
    pidx = (1 + gdf.eq_capgain).cumprod()
    d = pidx * gdf.eq_dp
    gdf["dgro"] = np.log(d.where(d > 0)).diff() - np.log1p(gdf.infl)
    gdf.loc[~np.isfinite(gdf.dgro.fillna(np.inf)), "dgro"] = np.nan
    ln_dp = np.log(gdf.eq_dp.where(gdf.eq_dp > 0))
    for h in HORIZONS:
        # all quantities measured over the SAME window t+1..t+h
        gdf[f"y{h}"] = np.log1p(gdf.req).rolling(h).mean().shift(-h)          # log real ret
        gdf[f"cg{h}"] = gdf.dgro.rolling(h).mean().shift(-h)                  # delivered
        gdf[f"cv{h}"] = -(ln_dp.shift(-h) - ln_dp) / h                        # revaluation
        gdf[f"ci{h}"] = np.log1p(gdf.eq_dp).rolling(h).mean().shift(-h)       # income
        gdf[f"gg{h}"] = gdf.g.rolling(h).mean().shift(-h)                     # GDP growth
        gdf[f"ii{h}"] = gdf.infl.rolling(h).mean().shift(-h)                  # inflation
    gdf["country"] = c
    frames.append(gdf.reset_index())
p = pd.concat(frames)
p = p[(p.year >= Y0) & (p.year <= Y1)]


def winz(s):
    return s.clip(s.quantile(0.01), s.quantile(0.99))


print("ER-D5(a) — pooled Spearman: SAME-window metric vs SAME-window real return CAGR")
print(f"{'metric':28}" + "".join(f"{h:>7}y" for h in HORIZONS))
for key, label in [("gg", "real GDP/cap growth"), ("cg", "real dividend growth"),
                   ("ii", "inflation")]:
    row = ""
    for h in HORIZONS:
        j = p[[f"{key}{h}", f"y{h}"]].dropna()
        row += f"{stats.spearmanr(j.iloc[:, 0], j.iloc[:, 1])[0]:+7.2f} "
    print(f"{label:28}{row}")

print("\nER-D5(b) — covariance shares of return variance (identity components):")
print(f"{'component':28}" + "".join(f"{h:>7}y" for h in HORIZONS))
shares = {k: [] for k in ["cv", "cg", "ci"]}
for h in HORIZONS:
    j = p[[f"y{h}", f"cg{h}", f"cv{h}", f"ci{h}"]].dropna()
    v = j[f"y{h}"].var()
    for k in ["cv", "cg", "ci"]:
        shares[k].append(np.cov(j[f"{k}{h}"], j[f"y{h}"])[0, 1] / v)
for k, label in [("cv", "revaluation (multiple move)"), ("cg", "delivered div growth"),
                 ("ci", "income (yield)")]:
    print(f"{label:28}" + "".join(f"{100*s:6.0f}% " for s in shares[k]))

print("\nER-D5(c) — macro-only R2 (same-window GDP growth + inflation, winsorized OLS):")
for h in HORIZONS:
    j = p[[f"gg{h}", f"ii{h}", f"y{h}"]].dropna().copy()
    for c in j.columns:
        j[c] = winz(j[c])
    X = np.column_stack([j[f"gg{h}"], j[f"ii{h}"], np.ones(len(j))])
    y = j[f"y{h}"].to_numpy()
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r2 = 1 - ((y - X @ b) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    print(f"  same-{h:>2}y window: R2 {100*r2:5.1f}%  (n={len(j)})")
