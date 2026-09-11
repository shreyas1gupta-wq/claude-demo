"""
Variant study: does ANY configuration of pairs trading work on NIFTY 50 names?

Extends the base engine with adaptive signal construction:
  z-score   : formation-static  vs  trailing-rolling
  hedge beta: formation-static  vs  trailing-rolling OLS
  re-formation frequency: 252d / 126d / 63d
All statistics are trailing-only, so no look-ahead is introduced.
"""
from __future__ import annotations
import os, json, itertools, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm
import pair_engine as E

warnings.filterwarnings("ignore")
OUT = E.OUT_DIR


def rolling_beta(ly: np.ndarray, lx: np.ndarray, win: int) -> np.ndarray:
    sy = pd.Series(ly); sx = pd.Series(lx)
    cov = sy.rolling(win).cov(sx); var = sx.rolling(win).var()
    b = (cov / var).bfill().values
    return b


def trade_pair_v(px, pair, form_dates, trade_dates, *, z_mode="static", beta_mode="static",
                 z_win=60, beta_win=120, cost_bps=E.COST_BPS, entry_z=E.ENTRY_Z,
                 exit_z=E.EXIT_Z, stop_z=E.STOP_Z, max_hold=E.MAX_HOLD):
    """Trade one pair; signal stats may be static (formation) or trailing-rolling."""
    y, x = pair["y"], pair["x"]
    full = form_dates.append(trade_dates)
    ly = np.log(px[y].reindex(full).values); lx = np.log(px[x].reindex(full).values)
    n_f = len(form_dates)

    beta = (np.full(len(full), pair["beta"]) if beta_mode == "static"
            else rolling_beta(ly, lx, beta_win))
    spread = ly - beta * lx
    if z_mode == "static":
        mu = np.full(len(full), pair["mu"] + pair["alpha"])   # alpha folded back in
        sd = np.full(len(full), pair["sd"])
        if beta_mode != "static":                             # recalibrate on formation
            mu = np.full(len(full), spread[:n_f].mean()); sd = np.full(len(full), spread[:n_f].std())
    else:
        s = pd.Series(spread)
        mu = s.rolling(z_win).mean().bfill().values
        sd = s.rolling(z_win).std().bfill().values
    z = (spread - mu) / np.where(sd > 0, sd, np.nan)
    z = np.nan_to_num(z)

    ry = np.diff(ly, prepend=ly[0]); rx = np.diff(lx, prepend=lx[0])
    c = cost_bps / 1e4
    pos = 0; hold = 0; ei = None
    pnl = np.zeros(len(full)); trades = []
    for i in range(n_f, len(full)):
        b = beta[i - 1] if pos != 0 else beta[i]
        g = 1.0 + abs(b); wy, wx = 1.0 / g, b / g
        if pos != 0:
            pnl[i] = pos * (wy * ry[i] - wx * rx[i]); hold += 1
        if pos != 0 and (abs(z[i]) < exit_z or abs(z[i]) > stop_z or hold >= max_hold):
            pnl[i] -= 2 * c
            trades.append(dict(pair=f"{y}/{x}", entry=str(full[ei].date()), exit=str(full[i].date()),
                               days=hold, side=pos, entry_z=float(z[ei]), exit_z=float(z[i]),
                               pnl=float(pnl[ei:i + 1].sum()),
                               reason="stop" if abs(z[i]) > stop_z else ("time" if hold >= max_hold else "target")))
            pos, hold, ei = 0, 0, None
        if pos == 0 and i < len(full) - 1 and entry_z < abs(z[i]) < stop_z and beta[i] > 0:
            pos = -int(np.sign(z[i])); pnl[i] -= 2 * c; ei, hold = i, 0
    if pos != 0:
        pnl[-1] -= 2 * c
        trades.append(dict(pair=f"{y}/{x}", entry=str(full[ei].date()), exit=str(full[-1].date()),
                           days=hold, side=pos, entry_z=float(z[ei]), exit_z=float(z[-1]),
                           pnl=float(pnl[ei:].sum()), reason="eow"))
    return pd.Series(pnl[n_f:], index=trade_dates), trades


def run_variant(px, *, z_mode="static", beta_mode="static", trading_days=252, n_pairs=E.N_PAIRS,
                entry_z=E.ENTRY_Z, exit_z=E.EXIT_Z, stop_z=E.STOP_Z, cost_bps=E.COST_BPS,
                z_win=60, max_hold=E.MAX_HOLD, formation_days=E.FORMATION_DAYS, collect=False):
    logpx = np.log(px); idx = px.index
    daily, trades, wins, sels = [], [], [], []
    start = formation_days
    while start + trading_days <= len(idx):
        f_dates = idx[start - formation_days:start]
        t_dates = idx[start:start + trading_days]
        cand = E.screen(logpx.loc[f_dates])
        sel = cand.head(n_pairs) if len(cand) else cand
        if len(sel):
            mat = []
            for _, p in sel.iterrows():
                pn, tr = trade_pair_v(px, p.to_dict(), f_dates, t_dates, z_mode=z_mode,
                                      beta_mode=beta_mode, z_win=z_win, cost_bps=cost_bps,
                                      entry_z=entry_z, exit_z=exit_z, stop_z=stop_z,
                                      max_hold=max_hold)
                mat.append(pn); trades += tr
            port = pd.concat(mat, axis=1).mean(axis=1)
            daily.append(port)
            wins.append(dict(trade_start=str(t_dates[0].date()), trade_end=str(t_dates[-1].date()),
                             candidates=len(cand), ret=float((1 + port).prod() - 1)))
            if collect:
                s = sel.copy(); s["trade_start"] = str(t_dates[0].date()); sels.append(s)
        start += trading_days
    d = pd.concat(daily)
    return dict(daily=d, trades=pd.DataFrame(trades), windows=pd.DataFrame(wins),
                selections=pd.concat(sels) if sels else pd.DataFrame())


if __name__ == "__main__":
    px = E.load_prices()
    rows, curves = [], {}
    grid = [
        ("A. Static z, static beta (Gatev-style)",      dict(z_mode="static",  beta_mode="static")),
        ("B. Rolling 60d z, static beta",               dict(z_mode="rolling", beta_mode="static")),
        ("C. Rolling 60d z, rolling 120d beta",         dict(z_mode="rolling", beta_mode="rolling")),
        ("D. Rolling 30d z, static beta",               dict(z_mode="rolling", beta_mode="static", z_win=30)),
        ("E. Rolling 90d z, static beta",               dict(z_mode="rolling", beta_mode="static", z_win=90)),
        ("F. B + re-form every 126d",                   dict(z_mode="rolling", beta_mode="static", trading_days=126)),
        ("G. B + re-form every 63d",                    dict(z_mode="rolling", beta_mode="static", trading_days=63)),
        ("H. B + wider stop (z=5)",                     dict(z_mode="rolling", beta_mode="static", stop_z=5.0)),
        ("I. B + no stop, 30d time exit",               dict(z_mode="rolling", beta_mode="static", stop_z=99.0, max_hold=30)),
        ("J. B + entry 1.5",                            dict(z_mode="rolling", beta_mode="static", entry_z=1.5)),
        ("K. B + entry 2.5",                            dict(z_mode="rolling", beta_mode="static", entry_z=2.5)),
        ("L. B + top 10 pairs",                         dict(z_mode="rolling", beta_mode="static", n_pairs=10)),
        ("M. B + top 40 pairs",                         dict(z_mode="rolling", beta_mode="static", n_pairs=40)),
        ("N. B + 2y formation",                         dict(z_mode="rolling", beta_mode="static", formation_days=504)),
    ]
    for name, kw in grid:
        r = run_variant(px, **kw)
        p = E.perf(r["daily"]); t = r["trades"]
        rows.append(dict(variant=name, **p, n_trades=len(t),
                         win_rate=float((t.pnl > 0).mean()) if len(t) else 0.0,
                         avg_hold=float(t.days.mean()) if len(t) else 0.0,
                         stop_pct=float((t.reason == "stop").mean()) if len(t) else 0.0))
        curves[name] = (1 + r["daily"]).cumprod()
        print(f"{name:45s} sharpe={p['sharpe']:6.2f} cagr={p['cagr']*100:6.2f}% "
              f"dd={p['max_dd']*100:6.1f}% trades={len(t)}")
    df = pd.DataFrame(rows).sort_values("sharpe", ascending=False)
    df.to_csv(os.path.join(OUT, "variants.csv"), index=False)
    pd.DataFrame(curves).to_csv(os.path.join(OUT, "variant_curves.csv"))
    print("\nBEST:\n", df.head(5).to_string(index=False))
