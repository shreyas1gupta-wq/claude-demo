"""ER-D6 — US + India country models: all vaulted metrics, linear vs nonlinear.

Registered 2026-09-05 in research/register/trial-ledger.md BEFORE this run. Nonlinear =
quadratic terms + 3x3 rank-bin grid (house style, no fitted trees). Prints only.
"""
import numpy as np
import pandas as pd

ROOT = "/home/user/claude-demo"


def winz(s):
    return s.clip(s.quantile(0.01), s.quantile(0.99))


def ols(j, cols, ycol):
    X = np.column_stack([j[c] for c in cols] + [np.ones(len(j))])
    y = j[ycol].to_numpy()
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ b
    r2 = 1 - (resid ** 2).sum() / ((y - y.mean()) ** 2).sum()
    # naive t-stats (homoskedastic; overlap inflates — flagged at print)
    dof = max(len(j) - len(cols) - 1, 1)
    s2 = (resid ** 2).sum() / dof
    try:
        vb = s2 * np.linalg.inv(X.T @ X).diagonal()
        t = b / np.sqrt(vb)
    except np.linalg.LinAlgError:
        t = np.full(len(b), np.nan)
    return b, r2, t, X, y


# ================= US =================
us = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
us = us[us.country == "USA"][["year", "cpi", "eq_tr", "eq_capgain", "eq_dp", "ltrate",
                              "stir", "rgdpmad", "tloans", "gdp"]].set_index("year")
us["infl"] = us.cpi.pct_change()
us["req"] = (1 + us.eq_tr) / (1 + us.infl) - 1
us["g5"] = np.log(us.rgdpmad).diff().rolling(5).mean()
pidx = (1 + us.eq_capgain).cumprod()
d = pidx * us.eq_dp
us["dgro"] = np.log(d.where(d > 0)).diff() - np.log1p(us.infl)
us["dg5"] = us.dgro.rolling(5).mean()
us["rlt"] = (1 + us.ltrate / 100) / (1 + us.infl) - 1
us["r5"] = np.log1p(us.req).rolling(5).mean().apply(np.expm1)
us["term"] = (us.ltrate - us.stir) / 100
us["cred5"] = (us.tloans / us.gdp).diff(5)
us["dp"] = us.eq_dp
for h in (5, 10):
    us[f"fwd{h}"] = np.log1p(us.req).rolling(h).mean().shift(-h).apply(np.expm1)
us = us[(us.index >= 1950) & (us.index <= 2020)]

F = ["dp", "g5", "dg5", "rlt", "infl", "r5", "term", "cred5"]
print("US (JST 1950-2020, 8 factors; overlap inflates all t's — flagged)")
for h in (5, 10):
    j = us[F + [f"fwd{h}"]].dropna().copy()
    for c in j.columns:
        j[c] = winz(j[c])
    jq = j.copy()
    jq["dp2"], jq["infl2"] = jq.dp ** 2, jq.infl ** 2
    bL, r2L, tL, _, _ = ols(j, F, f"fwd{h}")
    bQ, r2Q, tQ, _, _ = ols(jq, F + ["dp2", "infl2"], f"fwd{h}")
    print(f"  next-{h}y in-sample: LINEAR R2 {100*r2L:.1f}% | QUADRATIC R2 {100*r2Q:.1f}% (n={len(j)})")
    if h == 10:
        rank = sorted(zip(F, tL[:-1]), key=lambda x: -abs(x[1]))
        print("    factor ranking by |t| (10y):",
              ", ".join(f"{f} {t:+.1f}" for f, t in rank))
    # OOS
    tr = j[j.index <= 1989]
    te = j[(j.index >= 1990) & (j.index <= 2020 - h)]
    trq, teq = jq.loc[tr.index], jq.loc[te.index]
    for name, cols, dtr, dte in [("linear", F, tr, te),
                                 ("quadratic", F + ["dp2", "infl2"], trq, teq)]:
        b, _, _, _, _ = ols(dtr, cols, f"fwd{h}")
        Xe = np.column_stack([dte[c] for c in cols] + [np.ones(len(dte))])
        ye = dte[f"fwd{h}"].to_numpy()
        oos = 1 - ((ye - Xe @ b) ** 2).sum() / ((ye - dtr[f"fwd{h}"].mean()) ** 2).sum()
        print(f"    OOS {name:9} (fit<=1989, test 1990+): R2 {100*oos:+.1f}% (n={len(dte)})")

# the house nonlinear: 3x3 rank-bin grid, dp x infl terciles, next-5y
j = us[["dp", "infl", "fwd5"]].dropna()
dq, iq = j.dp.quantile([1/3, 2/3]), j.infl.quantile([1/3, 2/3])
lab = lambda s, q: np.where(s <= q.iloc[0], 0, np.where(s <= q.iloc[1], 1, 2))
j = j.assign(db=lab(j.dp, dq), ib=lab(j.infl, iq))
print("  3x3 bin grid: mean next-5y real return (rows=dp cheap->expensive TOP is cheap):")
gridtxt = []
for db in (2, 1, 0):
    cells = []
    for ib in (0, 1, 2):
        c = j[(j.db == db) & (j.ib == ib)].fwd5
        cells.append(f"{100*c.mean():+5.1f}({len(c):2d})" if len(c) >= 4 else "  n<4   ")
    gridtxt.append("    " + ("cheap " if db == 2 else "mid   " if db == 1 else "expens") +
                   " | " + " ".join(cells))
print("           infl: low     mid    high")
print("\n".join(gridtxt))

# ================= INDIA =================
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
ann = iima.groupby("year").agg(exc=("MF", lambda s: np.expm1(np.log1p(s / 100).sum())),
                               rf=("RF", lambda s: np.expm1(np.log1p(s / 100).sum())))
nifty = pd.read_csv(f"{ROOT}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                    parse_dates=["Date"]).set_index("Date").sort_index().iloc[:, 0]
vol = nifty.pct_change().groupby(nifty.index.year).std() * np.sqrt(252)
pwt = pd.read_csv(f"{ROOT}/ingest/vault/macro/pwt100.csv")
gcol = [c for c in pwt.columns if "GDP (output, multiple" in c][0]
ind = pwt[pwt.Entity == "India"].set_index("Year")
gr = np.log(ind[gcol].astype(float) / ind.Population.astype(float)).diff()

ii = ann.copy()
ii["trail1"] = ii.exc.shift(1)
ii["trail3"] = np.log1p(ii.exc).rolling(3).mean().shift(1).apply(np.expm1)
ii["vol"] = vol
ii["growth"] = gr
for h in (1, 3):
    ii[f"fwd{h}"] = np.log1p(ii.exc).rolling(h).mean().shift(-h).apply(np.expm1)

FI = ["trail3", "trail1", "rf", "vol", "growth"]
print("\nINDIA (annual; registered factor set needs the 2008-2019 intersection — tiny, as expected)")
for h in (1, 3):
    j = ii[FI + [f"fwd{h}"]].dropna()
    if len(j) > len(FI) + 2:
        b, r2, t, _, _ = ols(j, FI, f"fwd{h}")
        rank = sorted(zip(FI, t[:-1]), key=lambda x: -abs(x[1]))
        print(f"  next-{h}y in-sample: R2 {100*r2:.1f}% (n={len(j)} !!) | top |t|: "
              + ", ".join(f"{f} {tv:+.1f}" for f, tv in rank[:2]))
    else:
        print(f"  next-{h}y: n={len(j)} — unfittable as registered")
    # reduced no-vol variant for the descriptive read (1994-2019)
    FR = ["trail3", "rf", "growth"]
    jr = ii[FR + [f"fwd{h}"]].dropna()
    br, r2r, tr_, _, _ = ols(jr, FR, f"fwd{h}")
    print(f"    reduced [trail3, rf, growth] 1994+: R2 {100*r2r:.1f}% (n={len(jr)})"
          + " | t: " + ", ".join(f"{f} {tv:+.1f}" for f, tv in zip(FR, tr_[:-1])))
# India OOS descriptive: reduced model, fit<=2014 predict 2015+
h = 1
jr = ii[["trail3", "rf", "growth", "fwd1"]].dropna()
tr_, te_ = jr[jr.index <= 2014], jr[jr.index > 2014]
if len(te_) >= 4:
    b, *_ = ols(tr_, ["trail3", "rf", "growth"], "fwd1")
    Xe = np.column_stack([te_[c] for c in ["trail3", "rf", "growth"]] + [np.ones(len(te_))])
    ye = te_.fwd1.to_numpy()
    oos = 1 - ((ye - Xe @ b) ** 2).sum() / ((ye - tr_.fwd1.mean()) ** 2).sum()
    print(f"  India OOS (reduced, fit<=2014, test 2015+): R2 {100*oos:+.1f}% (n={len(te_)}, DESCRIPTIVE)")
