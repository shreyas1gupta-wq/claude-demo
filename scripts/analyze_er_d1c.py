"""ER-D1c — the persistent-regressor null band for the dp ladder (Stambaugh/BRW).

Registered 2026-09-05 BEFORE this run. Null: NO predictability; dp rebuilt by per-country
AR(1) recursion; joint (dp innovation, return innovation) year-blocks resampled with the
house stationary bootstrap (B=300, mean block 5y, seed 7). Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.stats.bootstrap import stationary_bootstrap  # noqa: E402

ROOT = "/home/user/claude-demo"
HORIZONS = [1, 3, 5, 10, 20]
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_dp"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1

YEARS = np.arange(1950, 2021)
panels = {}
for c, g in df.groupby("country"):
    g = g.set_index("year").reindex(YEARS)
    if g.eq_dp.notna().sum() >= 60 and g.req.notna().sum() >= 60:
        panels[c] = g

# per-country AR(1) on dp; innovations; return innovations
fits = {}
for c, g in panels.items():
    dp, r = g.eq_dp.to_numpy(), g.req.to_numpy()
    ok = ~np.isnan(dp[1:]) & ~np.isnan(dp[:-1])
    phi, a = np.polyfit(dp[:-1][ok], dp[1:][ok], 1)
    e = np.full(len(YEARS), np.nan)
    e[1:][ok] = dp[1:][ok] - (a + phi * dp[:-1][ok])
    u = r - np.nanmean(r)
    fits[c] = dict(a=a, phi=phi, e=e, u=u, dp0=dp[0] if not np.isnan(dp[0]) else np.nanmean(dp),
                   rbar=np.nanmean(r))
print(f"{len(fits)} countries; median AR(1) phi = "
      f"{np.median([f['phi'] for f in fits.values()]):.2f}")


def ladder(dp_panel, ret_panel):
    out = []
    for h in HORIZONS:
        xs, ys = [], []
        for c in dp_panel:
            d, r = dp_panel[c], ret_panel[c]
            lr = np.log1p(r)
            fwd = np.array([np.expm1(np.nanmean(lr[t + 1:t + 1 + h]))
                            if t + h < len(YEARS) and not np.isnan(lr[t + 1:t + 1 + h]).any()
                            else np.nan for t in range(len(YEARS))])
            m = ~np.isnan(d) & ~np.isnan(fwd)
            xs.append(d[m]); ys.append(fwd[m])
        x, y = np.concatenate(xs), np.concatenate(ys)
        out.append(stats.spearmanr(x, y)[0])
    return out


obs = ladder({c: panels[c].eq_dp.to_numpy() for c in fits},
             {c: panels[c].req.to_numpy() for c in fits})

# null simulations: joint year-block resampling of (e, u); dp* by AR(1) recursion; r* = rbar + u*
idx_paths = stationary_bootstrap(np.arange(len(YEARS)), 300, mean_block=5.0, seed=7).astype(int)
sim = np.full((300, len(HORIZONS)), np.nan)
for s, path in enumerate(idx_paths):
    dp_p, rt_p = {}, {}
    for c, f in fits.items():
        e_s = f["e"][path]
        e_s = np.where(np.isnan(e_s), 0.0, e_s)
        u_s = f["u"][path]
        dp_s = np.empty(len(YEARS))
        dp_s[0] = f["dp0"]
        for t in range(1, len(YEARS)):
            dp_s[t] = f["a"] + f["phi"] * dp_s[t - 1] + e_s[t]
        dp_p[c] = dp_s
        rt_p[c] = f["rbar"] + u_s
    sim[s] = ladder(dp_p, rt_p)

print("\nER-D1c — observed pooled dp ladder vs the no-predictability null (95% band, B=300):")
print(f"{'h':>4} {'observed':>9} {'null 2.5%':>10} {'null 97.5%':>11}  verdict")
for i, h in enumerate(HORIZONS):
    lo, hi = np.nanpercentile(sim[:, i], [2.5, 97.5])
    v = "OUTSIDE — beats the persistent-regressor null" if obs[i] > hi else "inside the null band"
    print(f"{h:>3}y {obs[i]:+9.2f} {lo:+10.2f} {hi:+11.2f}  {v}")

# (6) Amihud-Hurvich corrected 1y US dp slope
us = panels["USA"]
dp, r = us.eq_dp.to_numpy(), us.req.to_numpy()
ok = ~np.isnan(dp[:-1]) & ~np.isnan(r[1:]) & ~np.isnan(dp[1:])
b_ols = np.polyfit(dp[:-1][ok], r[1:][ok], 1)[0]
n = ok.sum()
phi_hat = np.polyfit(dp[:-1][ok], dp[1:][ok], 1)[0]
phi_c = phi_hat + (1 + 3 * phi_hat) / n + 3 * (1 + 3 * phi_hat) / n ** 2
e = dp[1:][ok] - (phi_c * dp[:-1][ok] + (dp[1:][ok].mean() - phi_c * dp[:-1][ok].mean()))
u = r[1:][ok] - (b_ols * dp[:-1][ok] + (r[1:][ok].mean() - b_ols * dp[:-1][ok].mean()))
theta = np.cov(u, e)[0, 1] / np.var(e)
b_c = b_ols + theta * (phi_c - phi_hat)
print(f"\nER-D1c (6) US 1y dp slope: OLS {b_ols:+.2f} -> Amihud-Hurvich corrected {b_c:+.2f} "
      f"(phi {phi_hat:.2f}->{phi_c:.2f}, theta {theta:+.1f}, n={n})")
