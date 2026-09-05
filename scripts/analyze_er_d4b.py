"""ER-D4b — purged, honest-benchmark correction rerun of the ER-D4/ER-D6 OOS legs.

Registered 2026-09-05 BEFORE this run: purged split (train starts <= 1990-h), train-only
winsorization (quant/stats/preprocess.py), the REGISTERED test windows verbatim, expanding
per-country benchmark + the parent's frozen pooled mean for continuity. Prints only.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.stats.bootstrap import stationary_bootstrap  # noqa: E402
from quant.stats.preprocess import winsor_bounds, winsorize  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_dp", "ltrate", "stir",
         "rgdpmad", "tloans", "gdp", "eq_capgain"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1

frames = []
for c, g in df.groupby("country"):
    g = g.set_index("year").copy()
    g["g5"] = np.log(g.rgdpmad).diff().rolling(5).mean()
    g["rlt"] = (1 + g.ltrate / 100) / (1 + g.infl) - 1
    g["r5"] = np.log1p(g.req).rolling(5).mean().apply(np.expm1)
    g["dp"] = g.eq_dp
    for h in (5, 10):
        g[f"fwd{h}"] = np.log1p(g.req).rolling(h).mean().shift(-h).apply(np.expm1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
p = p[(p.year >= 1950) & (p.year <= 2020)]
FACT = ["dp", "g5", "rlt", "infl", "r5"]
TEST_END = {5: 2010, 10: 2000}          # the REGISTERED windows, verbatim


def fit_ols(j, cols, ycol):
    X = np.column_stack([j[c] for c in cols] + [np.ones(len(j))])
    b, *_ = np.linalg.lstsq(X, j[ycol].to_numpy(), rcond=None)
    return b


def predict(j, cols, b):
    return np.column_stack([j[c] for c in cols] + [np.ones(len(j))]) @ b


print("ER-D4b — pooled panel, PURGED split, train-only winsorization, registered windows")
for h in (5, 10):
    j = p[FACT + [f"fwd{h}", "year", "country"]].dropna().copy()
    tr = j[j.year <= 1990 - h].copy()                       # purged: no label crosses 1990
    te = j[(j.year >= 1990) & (j.year <= TEST_END[h])].copy()
    bounds = {c: winsor_bounds(tr[c]) for c in FACT + [f"fwd{h}"]}
    for c, bd in bounds.items():
        tr[c] = winsorize(tr[c], bd)
        te[c] = winsorize(te[c], bd)
    b = fit_ols(tr, FACT, f"fwd{h}")
    ye = te[f"fwd{h}"].to_numpy()
    err_m = ye - predict(te, FACT, b)
    # benchmark (a): expanding per-country mean of COMPLETED windows at each test start
    bench_a = np.full(len(te), np.nan)
    for i, (_, r) in enumerate(te.iterrows()):
        past = j[(j.country == r.country) & (j.year <= r.year - h)][f"fwd{h}"]
        bench_a[i] = past.mean() if len(past) else j[j.year <= r.year - h][f"fwd{h}"].mean()
    err_a = ye - bench_a
    # benchmark (b): the parent's frozen pooled train mean (continuity)
    err_b = ye - tr[f"fwd{h}"].mean()
    r2a = 1 - (err_m ** 2).sum() / (err_a ** 2).sum()
    r2b = 1 - (err_m ** 2).sum() / (err_b ** 2).sum()
    print(f"  {h}y (train<= {1990-h}, test 1990-{TEST_END[h]}, n={len(te)}): "
          f"OOS R2 vs expanding per-country mean {100*r2a:+.1f}% | vs frozen pooled {100*r2b:+.1f}%")
    if h == 10:
        # calendar-year block bootstrap band on the 10y R2 vs benchmark (a)
        years = np.sort(te.year.unique())
        ym = {y: i for i, y in enumerate(years)}
        idx_paths = stationary_bootstrap(np.arange(len(years)), 300, mean_block=5.0, seed=7)
        r2s = []
        te2 = te.assign(em=err_m, ea=err_a)
        for path in idx_paths.astype(int):
            sm = sb = 0.0
            for yi in path:
                rows = te2[te2.year == years[yi]]
                sm += (rows.em ** 2).sum()
                sb += (rows.ea ** 2).sum()
            r2s.append(1 - sm / sb)
        lo, hi = np.percentile(r2s, [5, 95])
        print(f"      10y block-bootstrap 90% band on R2 vs (a): [{100*lo:+.1f}%, {100*hi:+.1f}%]")

print("\nER-D4b — ER-D6 US cells, purged, train-only bounds, vs expanding US mean")
usF = FACT + ["term", "cred5", "dg5"]
us = p[p.country == "USA"].set_index("year").copy()
us["term"] = (us.ltrate - us.stir) / 100
us["cred5"] = (us.tloans / us.gdp).diff(5)
pidx = (1 + us.eq_capgain).cumprod()
d = pidx * us.eq_dp
us["dgro"] = np.log(d.where(d > 0)).diff() - np.log1p(us.infl)
us["dg5"] = us.dgro.rolling(5).mean()
for h in (5, 10):
    j = us[usF + [f"fwd{h}"]].dropna().copy()
    tr = j[j.index <= 1990 - h].copy()
    te = j[(j.index >= 1990) & (j.index <= TEST_END[h])].copy()
    bounds = {c: winsor_bounds(tr[c]) for c in usF + [f"fwd{h}"]}
    for c, bd in bounds.items():
        tr[c] = winsorize(tr[c], bd)
        te[c] = winsorize(te[c], bd)
    b = fit_ols(tr, usF, f"fwd{h}")
    ye = te[f"fwd{h}"].to_numpy()
    err_m = ye - predict(te, usF, b)
    bench = np.array([j[j.index <= t - h][f"fwd{h}"].mean() for t in te.index])
    r2 = 1 - (err_m ** 2).sum() / ((ye - bench) ** 2).sum()
    print(f"  US {h}y (n={len(te)}): OOS R2 vs expanding US mean {100*r2:+.1f}%")
