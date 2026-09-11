#!/usr/bin/env python3
"""Is there a harvestable variance risk premium in India, and what does an option-selling overlay earn?

Step 1 measures the premium directly: India VIX against the realised Nifty volatility that followed.
Step 2 simulates monthly option selling priced off that implied volatility and settled on the actual
index path, so the P&L is driven by real outcomes rather than by an assumed edge.

India VIX is a 30-day implied volatility on the Nifty, so the Nifty overlay uses it directly. The
midcap overlay scales it by the measured midcap/Nifty volatility ratio, which is an estimate and is
flagged as such in the output.
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
import numpy as np, pandas as pd

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "model"))
import costs  # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")
OUT = {}


def measure_vrp():
    d = IN.dropna(subset=["vix", "nifty_ret"]).copy()
    # realised volatility over the NEXT 21 sessions, annualised, aligned to the day the VIX was observed
    fwd = d["nifty_ret"].rolling(21).std().shift(-21) * np.sqrt(252) * 100
    v = pd.DataFrame({"iv": d["vix"], "rv_next": fwd}).dropna()
    v["vrp"] = v["iv"] - v["rv_next"]
    by_year = v.groupby(v.index.year)["vrp"].agg(["mean", "median", "count"])
    res = {"n_days": int(len(v)), "mean_iv": float(v.iv.mean()), "mean_rv_next": float(v.rv_next.mean()),
           "mean_vrp": float(v.vrp.mean()), "median_vrp": float(v.vrp.median()),
           "pct_days_positive_vrp": float((v.vrp > 0).mean() * 100),
           "iv_over_rv_ratio": float(v.iv.mean() / v.rv_next.mean()),
           "by_year": {int(y): {"mean_vrp": float(r["mean"]), "n": int(r["count"])} for y, r in by_year.iterrows()},
           "worst_month_vrp": float(v.vrp.min()), "best_month_vrp": float(v.vrp.max())}
    # midcap/nifty volatility ratio, for scaling implied volatility onto the midcap
    ov = IN.dropna(subset=["mcs_ret", "nifty_ret"])
    res["midcap_nifty_vol_ratio"] = float(ov["mcs_ret"].std() / ov["nifty_ret"].std())
    return v, res


def expiries(idx):
    """Last Tuesday of each month, the NSE monthly expiry convention since 2025."""
    df = pd.DataFrame(index=idx)
    df["ym"] = df.index.to_period("M")
    tues = df[df.index.dayofweek == 1]
    return list(pd.to_datetime(tues.groupby("ym").apply(lambda g: g.index.max()).values))


def simulate(index_key, iv_series, otm_call=0.04, otm_put=0.06, sell_call=True, sell_put=False,
             iv_scale=1.0, hs_bp=40.0, start=None, lot_notional=1_500_000.0):
    """Sell one monthly option per expiry cycle against a 1x long position, settle at expiry.

    Returns a monthly P&L series in percent of notional, net of the modelled transaction cost.
    """
    px = IN[index_key].dropna()
    if start:
        px = px.loc[start:]
    exps = [e for e in expiries(px.index) if e in px.index]
    rows = []
    for i in range(len(exps) - 1):
        t0, t1 = exps[i], exps[i + 1]
        s0, s1 = float(px.loc[t0]), float(px.loc[t1])
        days = int((t1 - t0).days)
        iv = float(iv_series.loc[:t0].iloc[-1]) / 100.0 * iv_scale
        if not np.isfinite(iv) or iv <= 0:
            continue
        yrs = days / 365.0
        gross_prem, payoff = 0.0, 0.0
        if sell_call:
            k = s0 * (1 + otm_call)
            p, _ = costs.bs(s0, k, iv, yrs, call=True)
            gross_prem += p
            payoff -= max(0.0, s1 - k)
        if sell_put:
            k = s0 * (1 - otm_put)
            p, _ = costs.bs(s0, k, iv, yrs, call=False)
            gross_prem += p
            payoff -= max(0.0, k - s1)
        # cost: charges apply to premium; squared off at expiry is not required for a short that expires
        # worthless, but the ITM case is closed out to avoid the 0.125% exercise STT, so charge a round turn.
        # scale index points to one real contract of rupee notional, so the flat brokerage is sized correctly
        mult = lot_notional / s0
        c = costs.option_round_turn(gross_prem * mult, lot_notional, n_legs=int(sell_call) + int(sell_put),
                                    half_spread_bp_of_premium=hs_bp)
        cost_pts = c["total"] / mult
        pnl = (gross_prem + payoff - cost_pts) / s0 * 100
        rows.append({"open": t0, "expiry": t1, "days": days, "spot0": s0, "spot1": s1, "iv_pct": iv * 100,
                     "premium_pct": gross_prem / s0 * 100, "payoff_pct": payoff / s0 * 100,
                     "cost_pct": cost_pts / s0 * 100, "pnl_pct": pnl,
                     "index_move_pct": (s1 / s0 - 1) * 100})
    return pd.DataFrame(rows)


def summarize(df, label):
    if df.empty:
        return {}
    n_years = (df["expiry"].iloc[-1] - df["open"].iloc[0]).days / 365.25
    tot = df["pnl_pct"].sum()
    return {"label": label, "n_cycles": int(len(df)), "years": round(n_years, 2),
            "annual_pnl_pct": float(tot / n_years), "mean_cycle_pct": float(df.pnl_pct.mean()),
            "win_rate_pct": float((df.pnl_pct > 0).mean() * 100), "worst_cycle_pct": float(df.pnl_pct.min()),
            "best_cycle_pct": float(df.pnl_pct.max()), "std_cycle_pct": float(df.pnl_pct.std()),
            "mean_premium_pct": float(df.premium_pct.mean()), "mean_cost_pct": float(df.cost_pct.mean()),
            "cost_as_pct_of_premium": float(df.cost_pct.sum() / df.premium_pct.sum() * 100),
            "pct_cycles_assigned": float((df.payoff_pct < 0).mean() * 100)}


def main():
    v, vrp = measure_vrp()
    OUT["vrp"] = vrp
    print("=== 1. VARIANCE RISK PREMIUM (India VIX vs the realised Nifty volatility that followed) ===")
    print(f"  days {vrp['n_days']}   mean implied {vrp['mean_iv']:.2f}%   mean subsequent realised {vrp['mean_rv_next']:.2f}%")
    print(f"  mean premium {vrp['mean_vrp']:+.2f} points   median {vrp['median_vrp']:+.2f}   implied/realised {vrp['iv_over_rv_ratio']:.2f}x")
    print(f"  implied exceeded realised on {vrp['pct_days_positive_vrp']:.1f}% of days")
    print("  by year: " + "  ".join(f"{y}:{d['mean_vrp']:+.1f}" for y, d in vrp["by_year"].items()))
    print(f"  midcap/Nifty volatility ratio {vrp['midcap_nifty_vol_ratio']:.2f}x")

    print("\n=== 2. MONTHLY OPTION-SELLING OVERLAY, settled on the actual index path ===")
    iv = IN["vix"].dropna()
    rows = []
    for label, kw in [
        ("Nifty: covered call 4% OTM", dict(index_key="nifty", otm_call=0.04, sell_call=True)),
        ("Nifty: covered call 6% OTM", dict(index_key="nifty", otm_call=0.06, sell_call=True)),
        ("Nifty: short put 6% OTM", dict(index_key="nifty", otm_put=0.06, sell_call=False, sell_put=True)),
        ("Nifty: strangle 4% call / 6% put", dict(index_key="nifty", otm_call=0.04, otm_put=0.06, sell_call=True, sell_put=True)),
    ]:
        d = simulate(iv_series=iv, start="2014-06-01", **kw)
        s = summarize(d, label); rows.append(s)
    r = vrp["midcap_nifty_vol_ratio"]
    for label, kw in [
        ("Midcap Select: covered call 5% OTM", dict(index_key="mcs", otm_call=0.05, sell_call=True, iv_scale=r, hs_bp=70)),
        ("Midcap Select: covered call 8% OTM", dict(index_key="mcs", otm_call=0.08, sell_call=True, iv_scale=r, hs_bp=70)),
        ("Midcap 50: covered call 5% OTM", dict(index_key="mc50", otm_call=0.05, sell_call=True, iv_scale=r, hs_bp=70)),
        ("Midcap 50: covered call 8% OTM", dict(index_key="mc50", otm_call=0.08, sell_call=True, iv_scale=r, hs_bp=70)),
    ]:
        d = simulate(iv_series=iv, start="2014-06-01" if "50" in label else "2021-09-16", **kw)
        s = summarize(d, label); rows.append(s)
    t = pd.DataFrame(rows)
    print(t[["label", "n_cycles", "years", "annual_pnl_pct", "win_rate_pct", "worst_cycle_pct",
             "mean_premium_pct", "cost_as_pct_of_premium", "pct_cycles_assigned"]].round(2).to_string(index=False))
    OUT["overlay"] = rows
    (HERE / "india_vrp.json").write_text(json.dumps(OUT, indent=2, default=float))
    print("\nwrote india_vrp.json")


if __name__ == "__main__":
    main()
