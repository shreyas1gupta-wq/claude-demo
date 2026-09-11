"""Final study: best configuration, robustness, costs, and per-pair diagnostics."""
from __future__ import annotations
import os, json, warnings
import numpy as np, pandas as pd
import pair_engine as E
from variants import run_variant, trade_pair_v

warnings.filterwarnings("ignore")
OUT = E.OUT_DIR
BEST = dict(z_mode="rolling", beta_mode="static", z_win=60, n_pairs=10,
            trading_days=63, entry_z=2.0, exit_z=0.5, stop_z=3.5, max_hold=60)

def yearly(s: pd.Series) -> pd.Series:
    return s.groupby(s.index.year).apply(lambda x: (1 + x).prod() - 1)

def monthly(s: pd.Series) -> pd.DataFrame:
    m = s.groupby([s.index.year, s.index.month]).apply(lambda x: (1 + x).prod() - 1)
    m.index.names = ["year", "month"]
    return m.unstack()

if __name__ == "__main__":
    px = E.load_prices()
    dump = {}

    # ---------- 1. refinement grid around the two best levers -----------------
    grid = []
    for n in (5, 8, 10, 15, 20):
        for td in (63, 126, 252):
            r = run_variant(px, z_mode="rolling", beta_mode="static", z_win=60,
                            n_pairs=n, trading_days=td)
            p = E.perf(r["daily"])
            grid.append(dict(n_pairs=n, reform_days=td, sharpe=p["sharpe"], cagr=p["cagr"],
                             max_dd=p["max_dd"], vol=p["vol"], n_trades=len(r["trades"])))
            print(f"n={n:2d} reform={td:3d} -> sharpe {p['sharpe']:5.2f}")
    pd.DataFrame(grid).to_csv(f"{OUT}/grid_npairs_reform.csv", index=False)

    # ---------- 2. best config, full diagnostics ------------------------------
    r = run_variant(px, collect=True, **BEST)
    daily, trades, sel = r["daily"], r["trades"], r["selections"]
    bench = px.pct_change().mean(axis=1).reindex(daily.index).fillna(0)

    # vol-targeted overlay (10% target, trailing 60d vol, 4x leverage cap)
    lev = (0.10 / (daily.rolling(60).std() * np.sqrt(252))).shift(1).clip(upper=4).fillna(1.0)
    vt = daily * lev

    eq = pd.DataFrame({"strategy": (1 + daily).cumprod(), "vol_targeted": (1 + vt).cumprod(),
                       "benchmark_ew": (1 + bench).cumprod(), "ret": daily,
                       "bench_ret": bench, "leverage": lev})
    eq.to_csv(f"{OUT}/best_equity.csv")
    trades.to_csv(f"{OUT}/best_trades.csv", index=False)
    sel.to_csv(f"{OUT}/best_selected_pairs.csv", index=False)

    yr = pd.DataFrame({"strategy": yearly(daily), "vol_targeted": yearly(vt),
                       "benchmark_ew": yearly(bench)})
    yr["excess"] = yr.strategy - yr.benchmark_ew
    yr.to_csv(f"{OUT}/best_yearly.csv")
    monthly(daily).to_csv(f"{OUT}/best_monthly.csv")

    # ---------- 3. cost sensitivity on the best config ------------------------
    cost_rows = []
    for c in (0, 2.5, 5, 7.5, 10, 15, 20, 30):
        rc = run_variant(px, cost_bps=c, **BEST)
        p = E.perf(rc["daily"])
        cost_rows.append(dict(cost_bps_leg_side=c, roundtrip_bps=4 * c, **p,
                              n_trades=len(rc["trades"])))
        print(f"cost {c:5.1f} bps/leg -> sharpe {p['sharpe']:5.2f} cagr {p['cagr']*100:5.2f}%")
    pd.DataFrame(cost_rows).to_csv(f"{OUT}/best_cost_sensitivity.csv", index=False)

    # ---------- 4. per-pair diagnostics ---------------------------------------
    pt = trades.groupby("pair").agg(trades=("pnl", "size"), total_pnl=("pnl", "sum"),
                                    avg_pnl=("pnl", "mean"), win_rate=("pnl", lambda s: (s > 0).mean()),
                                    avg_days=("days", "mean")).sort_values("total_pnl", ascending=False)
    pt.to_csv(f"{OUT}/pair_pnl.csv")

    sel["pair"] = sel.y + "/" + sel.x
    freq = sel.groupby("pair").agg(times_selected=("pair", "size"), avg_adf_p=("adf_p", "mean"),
                                   avg_half_life=("half_life", "mean"), avg_corr=("corr", "mean"),
                                   avg_beta=("beta", "mean"),
                                   same_sector=("same_sector", "first"),
                                   sector_y=("sector_y", "first"), sector_x=("sector_x", "first")
                                   ).sort_values("times_selected", ascending=False)
    freq = freq.join(pt[["trades", "total_pnl", "win_rate"]], how="left")
    freq.to_csv(f"{OUT}/pair_frequency.csv")

    # ---------- 5. universe-wide cointegration census -------------------------
    logpx = np.log(px); idx = px.index; census, allcand = [], []
    s = E.FORMATION_DAYS
    while s + 63 <= len(idx):
        f = logpx.iloc[s - E.FORMATION_DAYS:s]
        cand = E.screen(f)
        census.append(dict(form_end=str(f.index[-1].date()), n_candidates=len(cand),
                           pct_of_1081=100 * len(cand) / 1081,
                           same_sector=int(cand.same_sector.sum()) if len(cand) else 0,
                           med_half_life=float(cand.half_life.median()) if len(cand) else np.nan,
                           med_adf_p=float(cand.adf_p.median()) if len(cand) else np.nan))
        if len(cand):
            c = cand.copy(); c["form_end"] = str(f.index[-1].date()); allcand.append(c)
        s += 63
    pd.DataFrame(census).to_csv(f"{OUT}/cointegration_census.csv", index=False)
    ac = pd.concat(allcand); ac.to_csv(f"{OUT}/all_candidates.csv", index=False)

    # ---------- 6. statistical significance -----------------------------------
    rng = np.random.default_rng(7)
    boot = [E.perf(pd.Series(rng.choice(daily.values, len(daily), replace=True),
                             index=daily.index))["sharpe"] for _ in range(2000)]
    boot = np.array(boot)
    p_best = E.perf(daily)
    sig = dict(sharpe=p_best["sharpe"], boot_mean=float(boot.mean()),
               ci_low=float(np.percentile(boot, 2.5)), ci_high=float(np.percentile(boot, 97.5)),
               p_value_sharpe_le_0=float((boot <= 0).mean()),
               t_stat=float(p_best["sharpe"] * np.sqrt(len(daily) / 252)))

    summary = dict(
        universe=int(px.shape[1]), data_start=str(px.index[0].date()), data_end=str(px.index[-1].date()),
        oos_start=str(daily.index[0].date()), oos_end=str(daily.index[-1].date()),
        best_config=BEST | dict(cost_bps_per_leg_per_side=E.COST_BPS),
        strategy=p_best, vol_targeted=E.perf(vt), benchmark_ew=E.perf(bench),
        n_trades=int(len(trades)), win_rate=float((trades.pnl > 0).mean()),
        avg_hold=float(trades.days.mean()),
        avg_win=float(trades[trades.pnl > 0].pnl.mean()),
        avg_loss=float(trades[trades.pnl <= 0].pnl.mean()),
        payoff=float(abs(trades[trades.pnl > 0].pnl.mean() / trades[trades.pnl <= 0].pnl.mean())),
        exit_mix={k: int(v) for k, v in trades.reason.value_counts().items()},
        corr_to_bench=float(np.corrcoef(daily.values, bench.values)[0, 1]),
        beta_to_bench=float(np.polyfit(bench.values, daily.values, 1)[0]),
        time_in_market=float((daily != 0).mean()),
        significance=sig,
        breakeven_cost_bps=None,
    )
    cs = pd.DataFrame(cost_rows)
    neg = cs[cs.sharpe <= 0]
    summary["breakeven_cost_bps"] = float(neg.cost_bps_leg_side.min()) if len(neg) else ">30"
    with open(f"{OUT}/best_summary.json", "w") as fh:
        json.dump(summary, fh, indent=2, default=float)
    print(json.dumps({k: v for k, v in summary.items() if k != "best_config"}, indent=2, default=float)[:2500])
