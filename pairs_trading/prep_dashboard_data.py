"""Compress the backtest outputs into one JSON payload for the dashboard."""
import json, numpy as np, pandas as pd, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")

eq = pd.read_csv(f"{R}/best_equity.csv", index_col=0, parse_dates=True)
w = eq.resample("W-FRI").last().dropna()
dd = (eq.strategy / eq.strategy.cummax() - 1).resample("W-FRI").min().dropna()
ddb = (eq.benchmark_ew / eq.benchmark_ew.cummax() - 1).resample("W-FRI").min().dropna()

summ = json.load(open(f"{R}/best_summary.json"))
yr = pd.read_csv(f"{R}/best_yearly.csv", index_col=0)
cost = pd.read_csv(f"{R}/best_cost_sensitivity.csv")
grid = pd.read_csv(f"{R}/grid_npairs_reform.csv")
cen = pd.read_csv(f"{R}/cointegration_census.csv")
var = pd.read_csv(f"{R}/variants.csv")
freq = pd.read_csv(f"{R}/pair_frequency.csv").head(14)
pnl = pd.read_csv(f"{R}/pair_pnl.csv")
mon = pd.read_csv(f"{R}/best_monthly.csv", index_col=0)
cand = pd.read_csv(f"{R}/all_candidates.csv")
trades = pd.read_csv(f"{R}/best_trades.csv")

payload = dict(
    summary=summ,
    equity=dict(dates=[d.strftime("%Y-%m-%d") for d in w.index],
                strategy=[round(v, 4) for v in w.strategy],
                vol_targeted=[round(v, 4) for v in w.vol_targeted],
                benchmark=[round(v, 4) for v in w.benchmark_ew],
                dd_strategy=[round(v * 100, 2) for v in dd],
                dd_bench=[round(v * 100, 2) for v in ddb]),
    yearly=dict(years=[int(i) for i in yr.index],
                strategy=[round(v * 100, 2) for v in yr.strategy],
                vol_targeted=[round(v * 100, 2) for v in yr.vol_targeted],
                benchmark=[round(v * 100, 2) for v in yr.benchmark_ew]),
    cost=cost[["cost_bps_leg_side", "roundtrip_bps", "sharpe", "cagr", "max_dd"]].round(4).to_dict("records"),
    grid=grid.round(3).to_dict("records"),
    census=cen.round(3).to_dict("records"),
    variants=var[["variant", "sharpe", "cagr", "max_dd", "vol", "n_trades", "win_rate",
                  "stop_pct", "avg_hold"]].round(4).to_dict("records"),
    pairs=freq.round(4).to_dict("records"),
    pair_pnl_top=pnl.head(10).round(4).to_dict("records"),
    pair_pnl_bot=pnl.tail(8).round(4).to_dict("records"),
    monthly=dict(years=[int(i) for i in mon.index],
                 data=[[None if pd.isna(v) else round(v * 100, 2) for v in mon.loc[i]] for i in mon.index]),
    halflife_hist=np.histogram(cand.half_life, bins=11, range=(5, 60))[0].tolist(),
    adf_hist=np.histogram(cand.adf_p, bins=10, range=(0, 0.05))[0].tolist(),
    trade_pnl_hist=np.histogram(trades.pnl * 100, bins=17, range=(-8.5, 8.5))[0].tolist(),
    hold_hist=np.histogram(trades.days, bins=12, range=(0, 60))[0].tolist(),
    sector_mix=dict(same=int(cand.same_sector.sum()), cross=int((~cand.same_sector).sum())),
    universe=sorted(pd.read_csv(f"{R}/prices_used.csv", index_col=0, nrows=1).columns.tolist()),
)
with open(f"{R}/dashboard.json", "w") as fh:
    json.dump(payload, fh, separators=(",", ":"))
print("bytes:", os.path.getsize(f"{R}/dashboard.json"))
print("weeks:", len(w), "| years:", payload["yearly"]["years"])
print("variants:", len(var), "| census pts:", len(cen))
