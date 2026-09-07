"""ER-D9 — cross-country long-run structure sweep + the dividend-GDP tether.

Registered 2026-09-07 BEFORE this run. n~16 dots; Spearman; priors and the mechanical-share
caveat live in the registration. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_capgain", "eq_dp", "bond_tr", "bill_rate",
         "housing_tr", "debtgdp", "crisisJST", "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["rbond"] = (1 + df.bond_tr) / (1 + df.infl) - 1
df["rbill"] = (1 + df.bill_rate) / (1 + df.infl) - 1
df["rhouse"] = (1 + df.housing_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()

rows, tether_frames = [], []
for c, g in df.groupby("country"):
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    pidx = (1 + g.eq_capgain).cumprod()
    d = pidx * g.eq_dp
    dgro = np.log(d.where(d > 0)).diff() - np.log1p(g.infl)
    dgro[~np.isfinite(dgro.fillna(np.inf))] = np.nan
    j = pd.concat([g.req, dgro.rename("dgro"), g.infl, g.rbond, g.rbill, g.rhouse,
                   g.debtgdp, g.crisisJST, g.g], axis=1).dropna(subset=["req"])
    if j.req.notna().sum() < 45 or j.dgro.notna().sum() < 40:
        continue
    rows.append(dict(
        c=c,
        ret=float(np.expm1(np.log1p(j.req).mean())),
        dgro=j.dgro.mean(),
        infl=j.infl.mean(),
        rbond=float(np.expm1(np.log1p(j.rbond.dropna()).mean())),
        rbill=float(np.expm1(np.log1p(j.rbill.dropna()).mean())),
        vol=j.req.std(),
        crises=j.crisisJST.fillna(0).sum(),
        debt=j.debtgdp.mean(),
        house=float(np.expm1(np.log1p(j.rhouse.dropna()).mean())) if j.rhouse.notna().sum() >= 40 else np.nan,
    ))
    # tether: log real D / real GDP (levels; scale constants drop out of changes/percentiles)
    ln_ratio = np.log(d.where(d > 0)) - np.log1p(g.infl).cumsum() - np.log(g.rgdpmad)
    lvl = pd.Series(expanding_percentile(ln_ratio.to_numpy(), min_obs=20), index=g.index)
    chg = (ln_ratio.shift(-10) - ln_ratio) / 10
    tf = pd.concat([lvl.rename("lvl"), chg.rename("chg")], axis=1).dropna()
    tf["c"] = c
    tether_frames.append(tf)

cc = pd.DataFrame(rows)
print(f"ER-D9(a) — cross-country corr(mean X, real equity CAGR), n={len(cc)} dots:")
for k, label in [("dgro", "a1 delivered real div growth"), ("infl", "a2 mean inflation"),
                 ("rbond", "a3 real bond return"), ("rbill", "a4 real bill return"),
                 ("vol", "a5 equity return volatility"), ("crises", "a6 crisis count"),
                 ("debt", "a7 mean debt/GDP"), ("house", "a8 housing real return")]:
    j = cc[[k, "ret"]].dropna()
    rho = stats.spearmanr(j[k], j.ret)[0]
    flag = "  << clears |0.6|" if abs(rho) >= 0.6 else ""
    print(f"  {label:30}: rho {rho:+.2f} (n={len(j)}){flag}")

t = pd.concat(tether_frames)
rho_t = stats.spearmanr(t.lvl, t.chg)[0]
neg = sum(stats.spearmanr(g.lvl, g.chg)[0] < 0 for _, g in t.groupby("c") if len(g) >= 20)
tot = sum(1 for _, g in t.groupby("c") if len(g) >= 20)
print(f"\nER-D9(b) — the dividend/GDP TETHER:")
print(f"  b1 pooled corr(D/GDP ratio percentile, next-10y ratio change) = {rho_t:+.2f} (n={len(t)})")
print(f"  b2 own-country relation negative in {neg}/{tot} countries")
