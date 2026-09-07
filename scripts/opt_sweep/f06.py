"""
OP-D2 family f06: 200d-MA trend x VIX-quintile -> fwd 21d ret/vol matrix.
Registered (trial-ledger.md, Entry OP-D2, F06), 4 cells:
  prior: belowMA+hiVIX has the widest fwd dispersion (structure-skew input);
  T-CTRL1 standalone-failure cited.
Cells = the 4 quadrant corners of {trend in (above200dMA, below200dMA)} x
{VIX-quintile extreme in (Q1 lowest, Q5 highest)}; full 5-quintile expanding
rank is computed en route but only the two extreme quintiles are registered.

NO LOOKAHEAD:
  - 200d MA at t uses AdjClose[t-199..t] only (trailing, min_obs=200).
  - VIX quintile at t uses expanding_percentile (min_obs=252): rank of VIX[t]
    within VIX[:t+1] only.
  - Forward 21d return/vol at t use AdjClose[t+1..t+21] — these are the FORWARD
    OUTCOME variables being tabulated by state at t, never inputs to the state.
Vault only. Prints only.
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd
from quant.ladder.credit_cycle import expanding_percentile

NIFTY_CSV = "ingest/vault/index/nifty50_daily_2007_2026.csv"
VIX_CSV = "ingest/vault/vix/india_vix_daily_2010_2023.csv"
MIN_OBS_MA = 200
MIN_OBS_VIX = 252
H = 21  # forward horizon, days

nifty = pd.read_csv(NIFTY_CSV, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
px = nifty["Adj Close"].astype(float).values
logret = np.r_[np.nan, np.diff(np.log(px))]

# 200d trailing MA trend state, no lookahead
ma200 = pd.Series(px).rolling(MIN_OBS_MA, min_periods=MIN_OBS_MA).mean().values
trend = np.where(np.isnan(ma200), np.nan, np.where(px > ma200, 1.0, 0.0))

# forward 21d simple return (%) and forward 21d realized vol (OP-D1 convention), no lookahead use
n = len(px)
fwd_ret21 = np.full(n, np.nan)
fwd_vol21 = np.full(n, np.nan)
for t in range(n - H):
    fwd_ret21[t] = (px[t + H] / px[t] - 1.0) * 100.0
    window = logret[t + 1: t + H + 1]
    if np.all(~np.isnan(window)):
        fwd_vol21[t] = np.sqrt(252.0 / H * np.sum(window ** 2)) * 100.0

nifty["trend"] = trend
nifty["fwd_ret21"] = fwd_ret21
nifty["fwd_vol21"] = fwd_vol21

vix = pd.read_csv(VIX_CSV, parse_dates=["date"]).sort_values("date").reset_index(drop=True)
vix_pct = expanding_percentile(vix["close"].astype(float).values, min_obs=MIN_OBS_VIX)
vix["vix_pct"] = vix_pct  # in [0,1], expanding rank -> no lookahead

merged = pd.merge(nifty[["Date", "trend", "fwd_ret21", "fwd_vol21"]],
                   vix[["date", "vix_pct"]],
                   left_on="Date", right_on="date", how="inner")

merged = merged.dropna(subset=["trend", "fwd_ret21", "fwd_vol21", "vix_pct"]).copy()

def quintile(p):
    if p < 0.20:
        return 1
    if p < 0.40:
        return 2
    if p < 0.60:
        return 3
    if p < 0.80:
        return 4
    return 5

merged["vq"] = merged["vix_pct"].apply(quintile)

print("=== f06: 200d-MA trend x VIX-quintile -> fwd 21d ret/vol matrix ===")
print(f"vault files: {NIFTY_CSV} | {VIX_CSV}")
print(f"merged overlap sample: n={len(merged)}  dates {merged['Date'].min().date()}..{merged['Date'].max().date()}")
print(f"min_obs: MA200={MIN_OBS_MA} (trailing), VIX expanding_percentile={MIN_OBS_VIX}")
print()
print("Full 5-quintile x trend matrix (descriptive, context only -- not registered cells):")
full = merged.groupby(["trend", "vq"]).agg(n=("fwd_ret21", "size"),
                                            mean_ret=("fwd_ret21", "mean"),
                                            std_ret=("fwd_ret21", "std"),
                                            mean_vol=("fwd_vol21", "mean")).round(3)
print(full)
print()

MIN_CELL_N = 30  # minimum obs for a cell bar to be evaluable, stated up front (no magic-number tuning post hoc; standard min sample for a mean/std estimate)

corners = {
    "aboveMA_loVIX": (1.0, 1),
    "aboveMA_hiVIX": (1.0, 5),
    "belowMA_loVIX": (0.0, 1),
    "belowMA_hiVIX": (0.0, 5),
}

results = {}
print("Registered 4 cells (corner quadrants):")
for name, (tr, vq) in corners.items():
    sub = merged[(merged["trend"] == tr) & (merged["vq"] == vq)]
    nobs = len(sub)
    mean_ret = sub["fwd_ret21"].mean() if nobs else float("nan")
    std_ret = sub["fwd_ret21"].std() if nobs else float("nan")
    mean_vol = sub["fwd_vol21"].mean() if nobs else float("nan")
    results[name] = dict(n=nobs, mean_ret=mean_ret, std_ret=std_ret, mean_vol=mean_vol)
    print(f"  {name}: n={nobs} mean_fwd21d_ret%={mean_ret:.3f} std_fwd21d_ret%={std_ret:.3f} mean_fwd21d_vol_pts={mean_vol:.3f}")

print()
evaluable = {k: v for k, v in results.items() if v["n"] >= MIN_CELL_N}
if len(evaluable) == 4:
    widest = max(results, key=lambda k: results[k]["std_ret"])
    print(f"Widest fwd-return dispersion (std) among 4 corners: {widest} (std={results[widest]['std_ret']:.3f})")
    prior_bar_pass = (widest == "belowMA_hiVIX")
    print(f"Prior test (belowMA+hiVIX widest dispersion): {'PASS' if prior_bar_pass else 'MISS'}")
else:
    thin = [k for k, v in results.items() if v["n"] < MIN_CELL_N]
    prior_bar_pass = None
    print(f"MISS: cell(s) below MIN_CELL_N={MIN_CELL_N} obs, prior test not evaluable: {thin}")
