"""
Walk-forward cointegration pairs-trading research engine for NIFTY 50 stocks.

Design
------
Formation window : 756 trading days (~3y)  -> pair selection + hedge ratio + spread stats
Trading window   : 252 trading days (~1y)  -> strictly out-of-sample, rolled annually
Signal           : z-score of the Engle-Granger residual (log prices), formation-calibrated
Execution        : dollar-neutral 2-leg spread, costs charged on gross traded notional

Every number reported by this script comes from the trading windows only.
"""
from __future__ import annotations
import os, json, itertools, warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

warnings.filterwarnings("ignore")

DATA_DIR = os.environ.get("PAIRS_DATA_DIR", "data")
OUT_DIR  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT_DIR, exist_ok=True)

# ----------------------------------------------------------------------------- config
FORMATION_DAYS = 756
TRADING_DAYS   = 252
N_PAIRS        = 20        # pairs traded per year
ENTRY_Z        = 2.0
EXIT_Z         = 0.5
STOP_Z         = 3.5
MAX_HOLD       = 60        # trading days
COST_BPS       = 10.0      # per leg, per side (brokerage + STT + impact + slippage)
ADF_P_MAX      = 0.05
HL_MIN, HL_MAX = 5, 60     # half-life bounds in days
MIN_CROSSINGS  = 12        # mean crossings per formation year

SECTOR = {
 "ADANIPORTS":"Infrastructure","ASIANPAINT":"Consumer","AXISBANK":"Bank","BAJAJ-AUTO":"Auto",
 "BAJFINANCE":"NBFC","BAJAJFINSV":"NBFC","BPCL":"Energy","BHARTIARTL":"Telecom",
 "BRITANNIA":"Consumer","CIPLA":"Pharma","COALINDIA":"Metals & Mining","DIVISLAB":"Pharma",
 "DRREDDY":"Pharma","EICHERMOT":"Auto","GRASIM":"Cement","HCLTECH":"IT","HDFCBANK":"Bank",
 "HEROMOTOCO":"Auto","HINDALCO":"Metals & Mining","HINDUNILVR":"Consumer","HDFC":"NBFC",
 "ICICIBANK":"Bank","ITC":"Consumer","IOC":"Energy","INDUSINDBK":"Bank","INFY":"IT",
 "JSWSTEEL":"Metals & Mining","KOTAKBANK":"Bank","LT":"Infrastructure","M&M":"Auto",
 "MARUTI":"Auto","NTPC":"Utilities","ONGC":"Energy","POWERGRID":"Utilities",
 "RELIANCE":"Energy","SHREECEM":"Cement","SBIN":"Bank","SUNPHARMA":"Pharma","TCS":"IT",
 "TATACONSUM":"Consumer","TATAMOTORS":"Auto","TATASTEEL":"Metals & Mining","TECHM":"IT",
 "TITAN":"Consumer","UPL":"Chemicals","ULTRACEMCO":"Cement","WIPRO":"IT",
}

# ----------------------------------------------------------------------------- data
def load_prices() -> pd.DataFrame:
    frames = {}
    for f in sorted(os.listdir(DATA_DIR)):
        if not f.endswith(".csv"):
            continue
        sym = f[:-4]
        df = pd.read_csv(os.path.join(DATA_DIR, f), parse_dates=["Date"])
        col = "Adj Close" if "Adj Close" in df.columns else "Close"
        frames[sym] = df.set_index("Date")[col].astype(float)
    px = pd.DataFrame(frames).sort_index()
    px = px.dropna(axis=1, thresh=int(0.99 * len(px)))   # drop late listings
    px = px.ffill().dropna()
    return px

# ----------------------------------------------------------------------------- stats
def half_life(spread: np.ndarray) -> float:
    s = pd.Series(spread)
    lag, delta = s.shift(1).iloc[1:], s.diff().iloc[1:]
    beta = sm.OLS(delta.values, sm.add_constant(lag.values)).fit().params[1]
    if beta >= 0:
        return np.inf
    return float(-np.log(2) / beta)

def eg_fit(y: np.ndarray, x: np.ndarray):
    """Engle-Granger: regress y on x, return (alpha, beta, resid, adf_p)."""
    res = sm.OLS(y, sm.add_constant(x)).fit()
    a, b = res.params
    resid = res.resid
    p = adfuller(resid, maxlag=1, regression="c", autolag=None)[1]
    return a, b, resid, p

_SCREEN_CACHE: dict = {}

def screen(logpx: pd.DataFrame) -> pd.DataFrame:
    """Screen every pair in a formation window. Returns a ranked candidate table.

    Memoised on the window key: the walk-forward grid re-uses identical
    formation windows across dozens of configurations."""
    key = (logpx.index[0], logpx.index[-1], logpx.shape[1])
    if key in _SCREEN_CACHE:
        return _SCREEN_CACHE[key]
    syms, rows = list(logpx.columns), []
    n_years = len(logpx) / 252.0
    for a, b in itertools.combinations(syms, 2):
        ya, yb = logpx[a].values, logpx[b].values
        corr = float(np.corrcoef(ya, yb)[0, 1])
        if corr < 0.7:                       # no economic link -> skip
            continue
        best = None
        for (dep, ind, dn, inn) in ((ya, yb, a, b), (yb, ya, b, a)):
            al, be, resid, p = eg_fit(dep, ind)
            if be <= 0:                      # negative hedge ratio = not a spread
                continue
            if best is None or p < best[-1]:
                best = (dn, inn, al, be, resid, p)
        if best is None:
            continue
        dn, inn, al, be, resid, p = best
        if p > ADF_P_MAX:
            continue
        hl = half_life(resid)
        if not (HL_MIN <= hl <= HL_MAX):
            continue
        z = (resid - resid.mean()) / resid.std()
        crossings = int(np.sum(np.diff(np.sign(z)) != 0) / n_years)
        if crossings < MIN_CROSSINGS:
            continue
        rows.append(dict(y=dn, x=inn, alpha=al, beta=be, adf_p=p, half_life=hl,
                         corr=corr, crossings=crossings,
                         mu=float(resid.mean()), sd=float(resid.std()),
                         same_sector=SECTOR.get(dn) == SECTOR.get(inn),
                         sector_y=SECTOR.get(dn, "?"), sector_x=SECTOR.get(inn, "?")))
    out = pd.DataFrame(rows)
    out = out.sort_values("adf_p").reset_index(drop=True) if len(out) else out
    _SCREEN_CACHE[key] = out
    return out

# ----------------------------------------------------------------------------- backtest
def trade_pair(px: pd.DataFrame, pair: dict, dates, cost_bps=COST_BPS,
               entry_z=ENTRY_Z, exit_z=EXIT_Z, stop_z=STOP_Z, max_hold=MAX_HOLD):
    """Trade one pair over `dates`. Returns (daily pnl on unit gross, trade list)."""
    y, x, be, mu, sd = pair["y"], pair["x"], pair["beta"], pair["mu"], pair["sd"]
    ly, lx = np.log(px[y].reindex(dates).values), np.log(px[x].reindex(dates).values)
    z = ((ly - pair["alpha"] - be * lx) - mu) / sd
    ry = np.diff(ly, prepend=ly[0]); rx = np.diff(lx, prepend=lx[0])
    gross = 1.0 + be                      # notional: 1 on y, beta on x
    wy, wx = 1.0 / gross, be / gross      # dollar-neutral, unit gross exposure
    c = cost_bps / 1e4

    pos = 0; hold = 0; entry_i = None
    pnl = np.zeros(len(dates)); trades = []
    for i in range(1, len(dates)):
        if pos != 0:
            pnl[i] = pos * (wy * ry[i] - wx * rx[i])
            hold += 1
        exit_now = pos != 0 and (abs(z[i]) < exit_z or abs(z[i]) > stop_z or hold >= max_hold)
        if exit_now:
            pnl[i] -= 2 * c                                    # both legs, unit gross
            trades.append(dict(pair=f"{y}/{x}", entry=str(dates[entry_i].date()),
                               exit=str(dates[i].date()), days=hold, side=pos,
                               entry_z=float(z[entry_i]), exit_z=float(z[i]),
                               pnl=float(pnl[entry_i:i + 1].sum()),
                               reason="stop" if abs(z[i]) > stop_z else
                                      ("time" if hold >= max_hold else "target")))
            pos, hold, entry_i = 0, 0, None
        if pos == 0 and i < len(dates) - 1 and abs(z[i]) > entry_z and abs(z[i]) < stop_z:
            pos = -int(np.sign(z[i]))      # short the spread when z high
            pnl[i] -= 2 * c
            entry_i, hold = i, 0
    if pos != 0:                            # mark-to-market close on last bar
        pnl[-1] -= 2 * c
        trades.append(dict(pair=f"{y}/{x}", entry=str(dates[entry_i].date()),
                           exit=str(dates[-1].date()), days=hold, side=pos,
                           entry_z=float(z[entry_i]), exit_z=float(z[-1]),
                           pnl=float(pnl[entry_i:].sum()), reason="eow"))
    return pnl, trades

def perf(daily: pd.Series, freq=252) -> dict:
    eq = (1 + daily).cumprod()
    yrs = len(daily) / freq
    cagr = eq.iloc[-1] ** (1 / yrs) - 1
    vol = daily.std() * np.sqrt(freq)
    sharpe = (daily.mean() * freq) / vol if vol > 0 else 0.0
    dd = (eq / eq.cummax() - 1).min()
    downside = daily[daily < 0].std() * np.sqrt(freq)
    return dict(cagr=float(cagr), vol=float(vol), sharpe=float(sharpe),
                sortino=float((daily.mean() * freq) / downside) if downside > 0 else 0.0,
                max_dd=float(dd), calmar=float(cagr / abs(dd)) if dd < 0 else 0.0,
                hit_days=float((daily > 0).mean()), total_ret=float(eq.iloc[-1] - 1),
                skew=float(daily.skew()), kurt=float(daily.kurt()))

def run(px: pd.DataFrame, n_pairs=N_PAIRS, cost_bps=COST_BPS, entry_z=ENTRY_Z,
        exit_z=EXIT_Z, stop_z=STOP_Z, same_sector_only=False, collect=False):
    logpx = np.log(px)
    idx = px.index
    daily_all, trades_all, windows, selections = [], [], [], []
    start = FORMATION_DAYS
    while start + TRADING_DAYS <= len(idx):
        f_slice = logpx.iloc[start - FORMATION_DAYS:start]
        t_dates = idx[start:start + TRADING_DAYS]
        cand = screen(f_slice)
        if same_sector_only and len(cand):
            cand = cand[cand.same_sector]
        sel = cand.head(n_pairs)
        if len(sel) == 0:
            start += TRADING_DAYS; continue
        pnl_mat, tr = [], []
        for _, p in sel.iterrows():
            pn, t = trade_pair(px, p.to_dict(), t_dates, cost_bps, entry_z, exit_z, stop_z)
            pnl_mat.append(pn); tr += t
        port = pd.Series(np.mean(pnl_mat, axis=0), index=t_dates)   # equal weight
        daily_all.append(port); trades_all += tr
        windows.append(dict(year=str(t_dates[0].date())[:4],
                            form_start=str(f_slice.index[0].date()),
                            form_end=str(f_slice.index[-1].date()),
                            trade_start=str(t_dates[0].date()),
                            trade_end=str(t_dates[-1].date()),
                            candidates=int(len(cand)), traded=int(len(sel)),
                            ret=float((1 + port).prod() - 1),
                            sharpe=float(port.mean() * 252 / (port.std() * np.sqrt(252)))
                                   if port.std() > 0 else 0.0,
                            n_trades=len(tr)))
        if collect:
            s = sel.copy(); s["trade_year"] = str(t_dates[0].date())[:4]
            selections.append(s)
        start += TRADING_DAYS
    daily = pd.concat(daily_all)
    return dict(daily=daily, trades=pd.DataFrame(trades_all), windows=pd.DataFrame(windows),
                selections=pd.concat(selections) if selections else pd.DataFrame())

# ----------------------------------------------------------------------------- main
if __name__ == "__main__":
    px = load_prices()
    print(f"universe: {px.shape[1]} stocks | {px.index[0].date()} -> {px.index[-1].date()} "
          f"| {len(px)} trading days")
    px.to_csv(os.path.join(OUT_DIR, "prices_used.csv"))

    base = run(px, collect=True)
    daily, trades, windows, sel = base["daily"], base["trades"], base["windows"], base["selections"]

    # benchmark: equal-weight buy & hold of the same universe, same OOS dates
    bench = px.pct_change().mean(axis=1).reindex(daily.index).fillna(0)

    summary = dict(
        universe=int(px.shape[1]),
        oos_start=str(daily.index[0].date()), oos_end=str(daily.index[-1].date()),
        strategy=perf(daily), benchmark=perf(bench),
        n_trades=int(len(trades)),
        win_rate=float((trades.pnl > 0).mean()),
        avg_hold=float(trades.days.mean()),
        avg_win=float(trades[trades.pnl > 0].pnl.mean()),
        avg_loss=float(trades[trades.pnl <= 0].pnl.mean()),
        exit_mix={k: int(v) for k, v in trades.reason.value_counts().items()},
        corr_to_bench=float(np.corrcoef(daily.values, bench.values)[0, 1]),
        beta_to_bench=float(np.polyfit(bench.values, daily.values, 1)[0]),
        config=dict(formation=FORMATION_DAYS, trading=TRADING_DAYS, n_pairs=N_PAIRS,
                    entry_z=ENTRY_Z, exit_z=EXIT_Z, stop_z=STOP_Z, max_hold=MAX_HOLD,
                    cost_bps_per_leg_per_side=COST_BPS, adf_p_max=ADF_P_MAX,
                    half_life_bounds=[HL_MIN, HL_MAX], min_crossings=MIN_CROSSINGS),
    )

    # ---- sensitivity grids -------------------------------------------------
    sens_cost = [dict(cost=c, **perf(run(px, cost_bps=c)["daily"])) for c in (0, 5, 10, 20, 30)]
    sens_entry = [dict(entry_z=e, **perf(run(px, entry_z=e)["daily"])) for e in (1.5, 2.0, 2.5, 3.0)]
    sens_n = [dict(n_pairs=n, **perf(run(px, n_pairs=n)["daily"])) for n in (5, 10, 20, 30, 50)]
    sect = run(px, same_sector_only=True)
    sens_sector = [dict(variant="same-sector only", **perf(sect["daily"])),
                   dict(variant="unconstrained", **perf(daily))]

    # ---- persist -----------------------------------------------------------
    daily.rename("ret").to_frame().assign(
        equity=(1 + daily).cumprod(), bench=bench,
        bench_equity=(1 + bench).cumprod()).to_csv(os.path.join(OUT_DIR, "equity.csv"))
    trades.to_csv(os.path.join(OUT_DIR, "trades.csv"), index=False)
    windows.to_csv(os.path.join(OUT_DIR, "windows.csv"), index=False)
    sel.to_csv(os.path.join(OUT_DIR, "selected_pairs.csv"), index=False)
    pd.DataFrame(sens_cost).to_csv(os.path.join(OUT_DIR, "sens_cost.csv"), index=False)
    pd.DataFrame(sens_entry).to_csv(os.path.join(OUT_DIR, "sens_entry.csv"), index=False)
    pd.DataFrame(sens_n).to_csv(os.path.join(OUT_DIR, "sens_npairs.csv"), index=False)
    pd.DataFrame(sens_sector).to_csv(os.path.join(OUT_DIR, "sens_sector.csv"), index=False)
    with open(os.path.join(OUT_DIR, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)

    print(json.dumps(summary, indent=2)[:2000])
