"""ER-D1..D4 — the expected-return horizon battery (JST R6 + NIFTY/PWT India partial).

Registered 2026-09-05 in research/register/trial-ledger.md BEFORE this run. Spearman for
correlograms; OLS legs winsorized 1%/99%; overlapping windows flagged. Prints only.
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
Y0, Y1 = 1950, 2020
HORIZONS = [1, 3, 5, 10, 20]

df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_capgain", "eq_dp", "ltrate",
         "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()
df["rlt"] = (1 + df.ltrate / 100) / (1 + df.infl) - 1

frames = []
for c, gdf in df.groupby("country"):
    gdf = gdf.set_index("year").copy()
    # dividend index: D = cumprod(1+capgain) * dp ; real dividend growth
    pidx = (1 + gdf.eq_capgain).cumprod()
    d = (pidx * gdf.eq_dp)
    gdf["dgro"] = (np.log(d.where(d > 0)).diff() - np.log1p(gdf.infl))
    gdf.loc[~np.isfinite(gdf.dgro.fillna(np.inf)), "dgro"] = np.nan
    gdf["g5"] = gdf.g.rolling(5).mean()
    gdf["dg5"] = gdf.dgro.rolling(5).mean()
    gdf["r5"] = gdf.req.rolling(5).apply(lambda w: np.expm1(np.log1p(w).mean()), raw=False)
    for h in HORIZONS:
        fwd = np.log1p(gdf.req).rolling(h).mean().shift(-h)
        gdf[f"fwd{h}"] = np.expm1(fwd)
    gdf["country"] = c
    frames.append(gdf.reset_index())
p = pd.concat(frames)
p = p[(p.year >= Y0) & (p.year <= Y1)]

PRED = [("dp", "eq_dp", "dividend yield (valuation)"),
        ("g5", "g5", "trailing 5y GDP/cap growth"),
        ("dg5", "dg5", "trailing 5y real dividend growth"),
        ("rlt", "rlt", "real long rate"),
        ("r5", "r5", "trailing 5y real return")]
p = p.rename(columns={"eq_dp": "dp"})

print("ER-D1 — pooled Spearman rho: predictor(t) vs next-h-year real return CAGR")
print(f"{'predictor':34}" + "".join(f"{h:>7}y" for h in HORIZONS))
for key, _, label in PRED:
    row = ""
    for h in HORIZONS:
        j = p[[key, f"fwd{h}"]].dropna()
        rho, _ = stats.spearmanr(j[key], j[f"fwd{h}"])
        row += f"{rho:+7.2f} "
    print(f"{label:34}{row}  (n at 10y: {len(p[[key,'fwd10']].dropna())})")

# per-country dp -> 10y for the majors
print("  dp->10y per country:", end=" ")
for c in ["USA", "UK", "Japan", "Germany"]:
    j = p[p.country == c][["dp", "fwd10"]].dropna()
    print(f"{c} {stats.spearmanr(j.dp, j.fwd10)[0]:+.2f}", end="  ")
print()

# ---- India partial (descriptive strength; short sample) ----
nifty = pd.read_csv(f"{ROOT}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                    parse_dates=["Date"]) if True else None
try:
    ny = nifty.set_index("Date").sort_index().iloc[:, 0].resample("YE").last()
    nret = ny.pct_change().dropna()
    nret.index = nret.index.year
    pwt = pd.read_csv(f"{ROOT}/ingest/vault/macro/pwt100.csv")
    gcol = "rgdpmad"
except Exception as e:
    print("India leg input issue:", e)
lab = None
pwt = pd.read_csv(f"{ROOT}/ingest/vault/macro/pwt100.csv")
gdp_col = [c for c in pwt.columns if "GDP (output, multiple" in c][0]
ind = pwt[pwt.Entity == "India"].set_index("Year")
ind_g = np.log(ind[gdp_col].astype(float) / ind.Population.astype(float)).diff()
print("\nER-D1-IN — India (NIFTY 2008-2026 annual, PWT growth to 2019; SHORT, descriptive):")
for h in [1, 3]:
    fwd = np.log1p(nret).rolling(h).mean().shift(-h).apply(np.expm1)
    t3 = np.log1p(nret).rolling(3).mean().apply(np.expm1)
    j1 = pd.concat([t3, fwd], axis=1, keys=["x", "y"]).dropna()
    j2 = pd.concat([ind_g, fwd], axis=1, keys=["x", "y"]).dropna()
    r1 = stats.spearmanr(j1.x, j1.y)[0] if len(j1) > 4 else np.nan
    r2 = stats.spearmanr(j2.x, j2.y)[0] if len(j2) > 4 else np.nan
    print(f"  next-{h}y: trail-3y return rho {r1:+.2f} (n={len(j1)}) | GDP growth rho {r2:+.2f} (n={len(j2)})")

# ---- ER-D2: dilution/slippage ----
rows = []
for c, gdf in p.groupby("country"):
    j = gdf[["g", "dgro", "req"]].dropna()
    if len(j) >= 40:
        rows.append((c, j.g.mean() - j.dgro.mean(), float(np.expm1(np.log1p(j.req).mean()))))
sl = pd.DataFrame(rows, columns=["c", "gap", "ret"])
r_sl, p_sl = stats.spearmanr(sl.gap, sl.ret)
print(f"\nER-D2 — slippage (GDP growth - dividend growth), full postwar:")
print(f"  panel median gap {100*sl.gap.median():+.1f}pp/yr (positive in {int((sl.gap>0).sum())}/{len(sl)})"
      f" | cross-country corr(gap, real eq CAGR) = {r_sl:+.2f} (n={len(sl)})")
print("  worst slippage:", ", ".join(f"{c} {100*g:.1f}" for c, g, _ in
      sl.nlargest(3, "gap").itertuples(index=False)),
      "| least:", ", ".join(f"{c} {100*g:.1f}" for c, g, _ in sl.nsmallest(3, "gap").itertuples(index=False)))

# ---- ER-D3: hurdle interaction ----
p["hurdle"] = (1 + 1.25 * p.ltrate / 100) / (1 + p.infl) - 1
p["vc"] = p.dg5 - p.hurdle
j = p[["vc", "fwd5"]].dropna()
q = j.vc.quantile([1/3, 2/3])
top, bot = j[j.vc > q.iloc[1]], j[j.vc <= q.iloc[0]]
print(f"\nER-D3 — value-creation proxy (deliv. 5y div growth - real hurdle[1.25x lt yield]):")
print(f"  next-5y real return: TOP tercile {100*top.fwd5.mean():+.1f}%/yr vs "
      f"BOTTOM {100*bot.fwd5.mean():+.1f}%/yr (n={len(j)}, overlap flagged)")

# ---- ER-D4: the clubbed equation ----
def winz(s):
    lo, hi = s.quantile(0.01), s.quantile(0.99)
    return s.clip(lo, hi)

FACT = ["dp", "g5", "rlt", "infl", "r5"]
print("\nER-D4 — pooled OLS, winsorized 1%/99% (the clubbed equation):")
for h in [1, 3, 5, 10]:
    j = p[FACT + [f"fwd{h}", "year"]].dropna().copy()
    for c in FACT + [f"fwd{h}"]:
        j[c] = winz(j[c])
    X = np.column_stack([j[c] for c in FACT] + [np.ones(len(j))])
    y = j[f"fwd{h}"].to_numpy()
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r2 = 1 - ((y - X @ beta) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    line = f"  next-{h}y: R2 {100*r2:4.1f}% (n={len(j)})"
    if h in (5, 10):
        line += ("  eq: r = " + " ".join(f"{b:+.2f}*{c}" for b, c in zip(beta, FACT))
                 + f" {beta[-1]:+.3f}")
    print(line)
    # OOS Goyal-Welch test
    if h in (5, 10):
        tr = j[j.year <= 1989]
        te = j[(j.year >= 1990) & (j.year <= 2020 - h)]
        Xt = np.column_stack([tr[c] for c in FACT] + [np.ones(len(tr))])
        bt, *_ = np.linalg.lstsq(Xt, tr[f"fwd{h}"].to_numpy(), rcond=None)
        Xe = np.column_stack([te[c] for c in FACT] + [np.ones(len(te))])
        pred = Xe @ bt
        ye = te[f"fwd{h}"].to_numpy()
        bench = tr[f"fwd{h}"].mean()
        oos = 1 - ((ye - pred) ** 2).sum() / ((ye - bench) ** 2).sum()
        print(f"      OOS (fit<=1989, test 1990+): R2 vs historical-mean = {100*oos:+.1f}% (n={len(te)})")
