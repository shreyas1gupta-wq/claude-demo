#!/usr/bin/env python3
"""OP-D2 family F17 — THE WEEKLY PAPER SIM (registered: research/register/trial-ledger.md,
Entry OP-D2, 2026-09-07): "storm/hi-vol entry weekly condor, mgmt {hold, daily-stop} +
per-unit-margin weekly-vs-monthly compounding compare (3) — the compounding claim
measured; two-sided." No PASS/MISS bar registered — family is TWO-SIDED.

Registered cells (3):
  1. weekly_hold_per_margin   : weekly condor paper sim, hold-to-expiry, P&L per unit
                                margin (base print; descriptive).
  2. weekly_daily_stop_vs_hold: daily-stop (2x-credit, F16/F15 stop convention) vs hold —
                                worst-week improvement + mean cost; two-sided.
  3. weekly_vs_monthly_compounding: per-unit-margin compounded growth, weekly vs monthly
                                cycles, SAME entry rule + sample; two-sided.

Declared conventions (header of record; match F15/F16 OP-D2 conventions):
  - Vault only: NIFTY daily Adj Close 2007-2026 + India VIX close 2010-2023 (inner join;
    overlap 2010-07..2023-04). Returns = pct_change of Adj Close. Spot = Adj Close.
  - VIX percentile = expanding percentile min_obs=252 (quant.ladder.credit_cycle).
  - ENTRY (storm/hi-vol, per registration): at cycle-start close, VIXpct >= 0.6 (the F16
    registered hi-vol threshold) OR a storm day (|daily ret| >= 2%, OP-D1 convention)
    within the last 5 trading days incl. t. All state at t uses data <= t (no lookahead).
  - Weekly cycle: entry first trading day of each ISO week at close, expiry last trading
    day of the same ISO week at close (needs >= 2 trading days). Monthly cycle: first ->
    last trading day of each calendar month. Non-overlapping by construction.
  - Condor = short 1.0-sigma strangle + long 2.5-sigma wings (F15/F16 convention),
    strikes K = S*exp(k*sigma*sqrt(T)) fixed at entry; flat sigma = VIX_t/100, r = 0.06,
    T = calendar days/365; index-point payoffs. MTM on day d: same strikes, spot = close_d,
    flat sigma = VIX_d/100 (VIX-flat vol, F16 convention), T = remaining calendar d/365.
  - Mgmt: hold = credit - intrinsic payoff at expiry close. daily-stop = exit at MTM close
    when loss >= 2x credit (checked entry+1 .. expiry-1), else hold payoff.
  - Margin per unit = max loss = max(call wing width, put wing width) - credit (index
    pts). Return per cycle = P&L / margin. Compounding: W *= (1 + pnl/margin) on entered
    cycles, flat otherwise; annualized geometric over the common valid-pct sample span.
  - No BS machinery in quant/ (F15 checked); closed forms local. Process note #6 concerns
    quant/stats estimators — nothing statistical is re-implemented here.
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f17.py
"""
import math
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile

REPO = "/home/user/claude-demo"
R = 0.06
BODY_SIG, WING_SIG = 1.0, 2.5
HI_VOL_PCT = 0.60          # F16 registered entry threshold
STORM = 0.02               # OP-D1 storm convention
STORM_LOOKBACK = 5         # trading days incl. t
STOP_MULT = 2.0            # F16/F15 stop-2x-credit convention
MIN_OBS = 252


def _ncdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_px(S, K, T, sig, cp):
    if T <= 0:
        return max(S - K, 0.0) if cp == "c" else max(K - S, 0.0)
    sq = sig * math.sqrt(T)
    d1 = (math.log(S / K) + (R + 0.5 * sig * sig) * T) / sq
    d2 = d1 - sq
    if cp == "c":
        return S * _ncdf(d1) - K * math.exp(-R * T) * _ncdf(d2)
    return K * math.exp(-R * T) * _ncdf(-d2) - S * _ncdf(-d1)


def condor_value(S, T, sig, K):
    """Cost to close the short condor (positive)."""
    return (bs_px(S, K["sc"], T, sig, "c") - bs_px(S, K["lc"], T, sig, "c")
            + bs_px(S, K["sp"], T, sig, "p") - bs_px(S, K["lp"], T, sig, "p"))


def load():
    nifty = pd.read_csv(f"{REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                        parse_dates=["Date"]).set_index("Date").sort_index()
    vix = pd.read_csv(f"{REPO}/ingest/vault/vix/india_vix_daily_2010_2023.csv",
                      parse_dates=["date"]).set_index("date").sort_index()
    df = pd.DataFrame({"close": nifty["Adj Close"], "vix": vix["close"]}).dropna()
    df["ret"] = df["close"].pct_change()
    df["storm"] = (df["ret"].abs() >= STORM)
    df["storm5"] = df["storm"].rolling(STORM_LOOKBACK, min_periods=1).max().astype(bool)
    df["vixpct"] = expanding_percentile(df["vix"].values, min_obs=MIN_OBS)
    df["entry_ok"] = (df["vixpct"] >= HI_VOL_PCT) | df["storm5"]
    df.loc[df["vixpct"].isna(), "entry_ok"] = False  # no state before min_obs
    return df


def sim_cycles(df, groups):
    """groups: list of (dates,) trading-day DatetimeIndex per cycle. Returns trade list."""
    trades = []
    for dates in groups:
        if len(dates) < 2:
            continue
        t0, tx = dates[0], dates[-1]
        row = df.loc[t0]
        if not bool(row["entry_ok"]):
            continue
        S0v, sig0 = float(row["close"]), float(row["vix"]) / 100.0
        T0 = (tx - t0).days / 365.0
        if T0 <= 0 or sig0 <= 0:
            continue
        w = sig0 * math.sqrt(T0)
        K = dict(sp=S0v * math.exp(-BODY_SIG * w), sc=S0v * math.exp(BODY_SIG * w),
                 lp=S0v * math.exp(-WING_SIG * w), lc=S0v * math.exp(WING_SIG * w))
        credit = condor_value(S0v, T0, sig0, K)
        if credit <= 0:
            continue
        margin = max(K["lc"] - K["sc"], K["sp"] - K["lp"]) - credit
        Sx = float(df.loc[tx, "close"])
        payoff = (max(Sx - K["sc"], 0) - max(Sx - K["lc"], 0)
                  + max(K["sp"] - Sx, 0) - max(K["lp"] - Sx, 0))
        pnl_hold = credit - payoff
        # daily-stop arm: mark entry+1 .. expiry-1 at close
        pnl_stop, stopped = pnl_hold, False
        for d in dates[1:-1]:
            Td = (tx - d).days / 365.0
            v = condor_value(float(df.loc[d, "close"]), Td,
                             float(df.loc[d, "vix"]) / 100.0, K)
            if v - credit >= STOP_MULT * credit:
                pnl_stop, stopped = credit - v, True
                break
        trades.append(dict(t0=t0, tx=tx, credit=credit, margin=margin,
                           rh=pnl_hold / margin, rs=pnl_stop / margin, stopped=stopped))
    return trades


def compounded_annual(trades, span_years):
    wlth = 1.0
    for tr in trades:
        wlth *= (1.0 + tr["rh"])
        if wlth <= 0:
            return None, 0.0  # RUIN: a cycle lost >= 100% of unit margin
    return (wlth ** (1.0 / span_years) - 1.0) * 100.0, wlth


def main():
    df = load()
    valid = df[df["vixpct"].notna()]
    span_years = (valid.index[-1] - valid.index[0]).days / 365.25
    print(f"sample: {valid.index[0].date()} .. {valid.index[-1].date()} "
          f"({span_years:.2f}y, {len(valid)} joint days)")
    iso = valid.index.isocalendar()
    wk_groups = sorted([g.index for _, g in
                        valid.groupby([iso.year.values, iso.week.values])],
                       key=lambda d: d[0])
    mo_groups = sorted([g.index for _, g in valid.groupby(valid.index.to_period("M"))],
                       key=lambda d: d[0])
    wk = sim_cycles(df, wk_groups)
    mo = sim_cycles(df, mo_groups)

    # Cell 1: weekly hold per unit margin
    rh = np.array([t["rh"] for t in wk])
    print(f"\n[cell 1] weekly_hold_per_margin: n={len(wk)} entered of {len(wk_groups)} "
          f"weeks ({100*len(wk)/len(wk_groups):.0f}%)")
    print(f"  mean {100*rh.mean():+.2f}%/wk  median {100*np.median(rh):+.2f}%  "
          f"hit {100*(rh>0).mean():.0f}%  worst {100*rh.min():+.1f}%  "
          f"best {100*rh.max():+.1f}%  sd {100*rh.std(ddof=1):.1f}%")

    # Cell 2: daily-stop vs hold
    rs = np.array([t["rs"] for t in wk])
    nstop = sum(t["stopped"] for t in wk)
    worst_h, worst_s = rh.min(), rs.min()
    mean_h, mean_s = rh.mean(), rs.mean()
    worst_impr = (abs(worst_h) - abs(worst_s)) / abs(worst_h) * 100.0  # + = stop cuts worst loss
    cost = (mean_h - mean_s) / abs(mean_h) * 100.0 if mean_h != 0 else float("nan")
    print(f"\n[cell 2] weekly_daily_stop_vs_hold: stops fired {nstop}/{len(wk)}")
    print(f"  worst wk: hold {100*worst_h:+.1f}% -> stop {100*worst_s:+.1f}% "
          f"(improvement {worst_impr:+.0f}%)")
    print(f"  mean: hold {100*mean_h:+.2f}% -> stop {100*mean_s:+.2f}% "
          f"(mean cost {cost:+.0f}% of hold mean)")

    # Cell 3: weekly vs monthly per-unit-margin compounding (hold arms, same rule/sample)
    g_wk, w_wk = compounded_annual(wk, span_years)
    g_mo, w_mo = compounded_annual(mo, span_years)
    rmo = np.array([t["rh"] for t in mo])
    fw = lambda g, w: (f"terminal W={w:.3f}, geo {g:+.2f}%/yr" if g is not None
                       else "RUIN (a cycle lost >=100% of unit margin)")
    print(f"\n[cell 3] weekly_vs_monthly_compounding (hold arms, per unit margin):")
    print(f"  weekly : n={len(wk)}, mean {100*rh.mean():+.2f}%/cycle, worst "
          f"{100*rh.min():+.2f}%, {fw(g_wk, w_wk)}")
    print(f"  monthly: n={len(mo)} entered of {len(mo_groups)} months, mean "
          f"{100*rmo.mean():+.2f}%/cycle, worst {100*rmo.min():+.2f}%, {fw(g_mo, w_mo)}")
    if g_wk is not None and g_mo is not None:
        print(f"  weekly - monthly = {g_wk - g_mo:+.2f} pp/yr")
    else:
        print(f"  weekly - monthly: not computable as geo diff — see RUIN line")
    nruin = int((rh <= -0.999).sum())
    order = np.argsort(rh)
    worst3 = [(str(wk[i]['t0'].date()), f"{100*rh[i]:+.1f}%") for i in order[:3]]
    print(f"  diagnostics: weekly cycles at <=-99.9% of margin: {nruin}; "
          f"worst 3 weeks: {worst3}")
    print(f"  arithmetic context (uncompounded, per unit margin): "
          f"wk {100*rh.mean()*len(wk)/span_years:+.1f}%/yr "
          f"vs mo {100*rmo.mean()*len(mo)/span_years:+.1f}%/yr")
    # context: stopped-arm weekly compounding
    wlth = 1.0
    for t in wk:
        wlth *= (1.0 + t["rs"])
    g_wks = (wlth ** (1.0 / span_years) - 1.0) * 100.0
    print(f"  context: weekly daily-stop arm geo {g_wks:+.2f}%/yr (terminal {wlth:.3f})")


if __name__ == "__main__":
    main()
