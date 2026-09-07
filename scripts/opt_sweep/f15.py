#!/usr/bin/env python3
"""OP-D2 family F15 — BS structural math (registered: research/register/trial-ledger.md,
Entry OP-D2, 2026-09-07): "theta/gamma/vega for 1-sigma condors 7d vs 30d at VIX 12/18/30
+ stop-value math under the measured storm matrix (4) — analytic." NO data mining; no
PASS/MISS bar registered — all four cells are analytic/DESCRIPTIVE.

Registered cells (4):
  1. greeks_7d   : net theta/gamma/vega of the 1-sigma condor, 7d tenor, VIX 12/18/30
  2. greeks_30d  : same at 30d tenor
  3. tenor_tradeoff : structural 7d-vs-30d ratios (theta/day, gamma, vega, theta-per-vega)
  4. stop_value_storm : the spot move that breaches a 2x-credit stop after 1 day, priced
     against the MEASURED storm matrix (vault: NIFTY ret_{t+1} conditioned on India VIX_t)

Declared conventions (header of record):
  - S0 = 100: all values in % of spot (index-point payoffs scale linearly; no magic level).
  - Flat sigma = VIX/100, r = 0.06, q = 0 (OP-D2 conventions). T = calendar days / 365.
  - Condor = short 1.0-sigma strangle + long 2.5-sigma wings (wing width quotes the F16
    registration in the same OP-D2 entry); strikes K = S0*exp(k*sigma*sqrt(T)).
  - Theta per calendar day (annual/365); vega per vol point (dV/dsigma / 100);
    negative net gamma/vega = short.
  - Storm matrix (no lookahead: VIX state at t, NIFTY return at t+1): storm = |daily
    ret| >= 2% (OP-D1 convention); VIX buckets <15 / 15-24 / >=24 — the edges are the
    midpoints of the registered levels 12/18/30. Vault only: NIFTY daily 2007-2026 +
    India VIX 2010-2023 (overlap 2010-07..2023-04).
  - Stop math: position enters for net credit C; stop-2x = close when MTM loss = 2C.
    Breach move m* solves loss(m, T-1d, flat vol) = 2C by bisection. Vol-spike variant
    reprices at sigma + (median VIX jump on measured storm days)/100.
  - No BS machinery exists in quant/ (checked); closed forms implemented here. Process
    note #6 concerns quant/stats estimators — nothing statistical is re-implemented.
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f15.py
"""
import math
import sys

import numpy as np
import pandas as pd

REPO = "/home/user/claude-demo"
R = 0.06
S0 = 100.0
BODY_SIG, WING_SIG = 1.0, 2.5
VIX_LEVELS = [12.0, 18.0, 30.0]
TENORS_D = [7, 30]
BUCKET_EDGES = [15.0, 24.0]  # midpoints of registered 12/18/30
STORM = 0.02


def _ncdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _npdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def bs(S, K, T, sig, cp):
    """Price, gamma, theta(per yr), vega(per unit sigma) for European option, q=0."""
    sq = sig * math.sqrt(T)
    d1 = (math.log(S / K) + (R + 0.5 * sig * sig) * T) / sq
    d2 = d1 - sq
    if cp == "c":
        px = S * _ncdf(d1) - K * math.exp(-R * T) * _ncdf(d2)
        theta = (-S * _npdf(d1) * sig / (2 * math.sqrt(T))
                 - R * K * math.exp(-R * T) * _ncdf(d2))
    else:
        px = K * math.exp(-R * T) * _ncdf(-d2) - S * _ncdf(-d1)
        theta = (-S * _npdf(d1) * sig / (2 * math.sqrt(T))
                 + R * K * math.exp(-R * T) * _ncdf(-d2))
    gamma = _npdf(d1) / (S * sq)
    vega = S * _npdf(d1) * math.sqrt(T)
    return px, gamma, theta, vega


def condor_strikes(T, sig):
    w = sig * math.sqrt(T)
    return dict(sp=S0 * math.exp(-BODY_SIG * w), sc=S0 * math.exp(BODY_SIG * w),
                lp=S0 * math.exp(-WING_SIG * w), lc=S0 * math.exp(WING_SIG * w))


def condor_value(S, T, sig, K):
    """Cost to close (long-the-body view sign): shorts minus longs."""
    v = 0.0
    for leg, sgn, cp in (("sp", +1, "p"), ("sc", +1, "c"), ("lp", -1, "p"), ("lc", -1, "c")):
        v += sgn * bs(S, K[leg], T, sig, cp)[0]
    return v


def condor_greeks(T, sig):
    K = condor_strikes(T, sig)
    credit = condor_value(S0, T, sig, K)
    g = t = v = 0.0
    for leg, sgn, cp in (("sp", -1, "p"), ("sc", -1, "c"), ("lp", +1, "p"), ("lc", +1, "c")):
        _, gg, tt, vv = bs(S0, K[leg], T, sig, cp)
        g += sgn * gg
        t += sgn * tt
        v += sgn * vv
    # position greeks: theta per calendar day, vega per vol point
    return dict(credit=credit, gamma=g, theta_d=t / 365.0, vega_pt=v / 100.0, K=K)


def breach_move(T_days, sig_entry, sig_mark, side):
    """|m| such that after 1 day, MTM loss = 2x credit. side=+1 up, -1 down."""
    T0 = T_days / 365.0
    K = condor_strikes(T0, sig_entry)
    C = condor_value(S0, T0, sig_entry, K)
    T1 = max((T_days - 1) / 365.0, 0.5 / 365.0)

    def loss(m):
        return condor_value(S0 * (1.0 + m), T1, sig_mark, K) - C

    lo, hi = 0.0, 0.30
    if loss(side * hi) < 2 * C:
        return float("nan"), C
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if loss(side * mid) < 2 * C:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), C


def main():
    print("== OP-D2 f15: BS structural math (analytic; registered Entry OP-D2/F15) ==")
    print(f"conventions: S0=100 (% of spot), r={R}, flat sigma=VIX/100, wings {WING_SIG}sigma, body {BODY_SIG}sigma")

    # Cells 1-2: greeks tables
    tabs = {}
    for td in TENORS_D:
        print(f"\n-- cell: greeks_{td}d (1-sigma condor, T={td}d) --")
        rows = {}
        for vix in VIX_LEVELS:
            gr = condor_greeks(td / 365.0, vix / 100.0)
            rows[vix] = gr
            print(f"VIX {vix:4.0f}: credit={gr['credit']:+.4f}%S  theta/day={gr['theta_d']:+.5f}%S  "
                  f"gamma={gr['gamma']:+.5f}  vega/pt={gr['vega_pt']:+.5f}%S  "
                  f"shortK=[{gr['K']['sp']:.2f},{gr['K']['sc']:.2f}] wingK=[{gr['K']['lp']:.2f},{gr['K']['lc']:.2f}]")
        tabs[td] = rows

    # Cell 3: tenor tradeoff at each VIX
    print("\n-- cell: tenor_tradeoff (7d / 30d structural ratios) --")
    tt = {}
    for vix in VIX_LEVELS:
        a, b = tabs[7][vix], tabs[30][vix]
        r_theta = a["theta_d"] / b["theta_d"]
        r_gamma = a["gamma"] / b["gamma"]
        r_vega = a["vega_pt"] / b["vega_pt"]
        tpv7 = a["theta_d"] / abs(a["vega_pt"])
        tpv30 = b["theta_d"] / abs(b["vega_pt"])
        tt[vix] = (r_theta, r_gamma, r_vega, tpv7, tpv30)
        print(f"VIX {vix:4.0f}: theta/day 7d/30d = {r_theta:.2f}x  gamma 7d/30d = {r_gamma:.2f}x  "
              f"vega 7d/30d = {r_vega:.2f}x  theta-per-|vega| 7d={tpv7:.3f} 30d={tpv30:.3f}")

    # Cell 4: measured storm matrix + stop-value math
    print("\n-- cell: stop_value_storm --")
    nf = pd.read_csv(f"{REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                     parse_dates=["Date"]).set_index("Date").sort_index()
    ret = nf["Adj Close"].pct_change()
    vx = pd.read_csv(f"{REPO}/ingest/vault/vix/india_vix_daily_2010_2023.csv",
                     parse_dates=["date"]).set_index("date").sort_index()["close"]
    df = pd.DataFrame({"vix": vx}).join(
        pd.DataFrame({"ret_next": ret.shift(-1)}), how="inner").dropna(subset=["ret_next"])
    df["vix_next"] = vx.shift(-1).reindex(df.index)
    df["storm_next"] = df["ret_next"].abs() >= STORM
    print(f"joined days: {len(df)}  span {df.index[0].date()}..{df.index[-1].date()}")

    # median VIX jump on measured storm days (VIX_{t+1} - VIX_t when t+1 is a storm)
    jump = (df.loc[df["storm_next"], "vix_next"] - df.loc[df["storm_next"], "vix"]).dropna()
    med_jump = float(jump.median())
    print(f"storm days (|ret|>=2%): {int(df['storm_next'].sum())}  median VIX jump on storm day: {med_jump:+.2f} pts")

    buckets = [("<15", df["vix"] < BUCKET_EDGES[0]),
               ("15-24", (df["vix"] >= BUCKET_EDGES[0]) & (df["vix"] < BUCKET_EDGES[1])),
               (">=24", df["vix"] >= BUCKET_EDGES[1])]
    # breach thresholds (flat vol and storm-jump vol), per tenor at each registered VIX
    print("breach move m* (1-day MTM loss = 2x credit; min of up/down side):")
    mstar = {}
    for td in TENORS_D:
        for vix in VIX_LEVELS:
            s = vix / 100.0
            md = min(breach_move(td, s, s, -1)[0], breach_move(td, s, s, +1)[0])
            ms = min(breach_move(td, s, (vix + med_jump) / 100.0, -1)[0],
                     breach_move(td, s, (vix + med_jump) / 100.0, +1)[0])
            mstar[(td, vix)] = (md, ms)
            print(f"  T={td:2d}d VIX {vix:4.0f}: m*flat={md*100:.2f}%  m*+medVIXjump({med_jump:+.1f})={ms*100:.2f}%")

    print("measured storm matrix (P per day, by VIX_t bucket):")
    for name, mask in buckets:
        sub = df[mask]
        p_storm = sub["storm_next"].mean()
        line = f"  VIX {name:5s} n={len(sub):4d}  P(storm)={p_storm*100:5.2f}%"
        for td in TENORS_D:
            vix_ref = {"<15": 12.0, "15-24": 18.0, ">=24": 30.0}[name]
            mflat = mstar[(td, vix_ref)][0]
            pb = (sub["ret_next"].abs() >= mflat).mean()
            line += f"  P(|ret|>=m*{td}d@{vix_ref:.0f})={pb*100:5.2f}%"
        print(line)

    # stop value: what the stop saves vs gap-through, at VIX 18 (the middle registered level)
    print("stop value at VIX 18 (loss in multiples of credit; max loss = width - credit):")
    sv = {}
    for td in TENORS_D:
        s = 0.18
        T0 = td / 365.0
        K = condor_strikes(T0, s)
        C = condor_value(S0, T0, s, K)
        maxloss_c = (K["lc"] - K["sc"] - C) / C  # call-side width minus credit, in credits
        mflat = mstar[(td, 18.0)][0]
        # historical gap-through severity: among mid-bucket days with |ret_next| >= m*,
        # mark the condor at the realized move (flat vol) -> loss in credits
        sub = df[(df["vix"] >= BUCKET_EDGES[0]) & (df["vix"] < BUCKET_EDGES[1])]
        gaps = sub.loc[sub["ret_next"].abs() >= mflat, "ret_next"]
        T1 = max((td - 1) / 365.0, 0.5 / 365.0)
        if len(gaps):
            losses = np.array([(condor_value(S0 * (1 + m), T1, s, K) - C) / C for m in gaps])
            mean_gap_loss = float(losses.mean())
        else:
            mean_gap_loss = float("nan")
        sv[td] = (maxloss_c, mflat, len(gaps), mean_gap_loss)
        print(f"  T={td:2d}d: credit={C:.4f}%S  maxloss={maxloss_c:.1f}x credit  stop=2.0x  "
              f"m*={mflat*100:.2f}%  midVIX gap-through days={len(gaps)}  "
              f"mean 1d loss when gapped={mean_gap_loss:.1f}x credit")

    print("\n== summary ==")
    r18 = tt[18.0]
    print(f"7d condor vs 30d at VIX18: theta/day {r18[0]:.1f}x, gamma {r18[1]:.1f}x, vega {r18[2]:.2f}x; "
          f"theta-per-|vega| 7d {r18[3]:.2f} vs 30d {r18[4]:.2f}")
    print(f"stop-2x breach: 7d@18 {mstar[(7,18.0)][0]*100:.2f}% vs 30d@18 {mstar[(30,18.0)][0]*100:.2f}% day-move; "
          f"7d maxloss {sv[7][0]:.1f}x vs 30d {sv[30][0]:.1f}x credit")


if __name__ == "__main__":
    sys.exit(main())
