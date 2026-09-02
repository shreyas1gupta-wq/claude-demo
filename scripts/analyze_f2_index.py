"""F2-index — the bounded 18-cell de-risk grid on the vaulted NIFTY daily (pre-registered).

Ledger 2026-09-02. Index-proxy book (long-only, exposure 1.0 base, cut to 0.5 on trigger).
Triggers on the composite state's OWN expanding percentile; confirm on the legs' percentiles;
three re-entry families; costs 28bp per unit turnover. Episodes verbatim from
scripts/analyze_nifty_daily.py (the §3 in-span set). This run can disqualify cells and
shortlist survivors; it cannot arm the R4 mapping (full F2 remains registered).
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import (drawdown_depth, fast_stress_composite,
                                      realized_vol)
from quant.ladder.phase import phase_state

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"
COST = 0.0028
EPISODES = [
    ("GFC core*", "2008-09-01", "2008-11-30"),     # * partially in warm-up
    ("EU/downgrade 2011", "2011-08-01", "2011-11-30"),
    ("Taper tantrum", "2013-05-01", "2013-09-30"),
    ("China deval 2015", "2015-08-01", "2015-09-30"),
    ("Demonetization", "2016-11-08", "2016-11-30"),
    ("Feb-2018 vol+LTCG", "2018-02-01", "2018-03-31"),
    ("IL&FS", "2018-09-01", "2018-10-31"),
    ("COVID crash", "2020-02-20", "2020-04-30"),
    ("Russia 2022", "2022-02-01", "2022-03-31"),
    ("Election day 2024", "2024-06-04", "2024-06-10"),
]

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
r = df["ret"].values
dates = df["Date"].values

rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
st_p = expanding_percentile(state, min_obs=252)
ph = phase_state(state, k_slope=21, smooth=5)   # daily series: 1-month slope, 1-week smooth
DOWNTURN, SLOWDOWN = 3, 2  # quadrant codes; D = falling-from-high = slowdown code 2

def episode_dd(path_ret, i0, i1):
    lvl = np.cumprod(1.0 + path_ret[i0:i1 + 1])
    peak = np.maximum.accumulate(lvl)
    return float((1.0 - lvl / peak).max())

def run_cell(trig, confirm, family):
    n = len(r)
    expo = np.ones(n)
    pos, pending_tranche, calendar_t0 = 1.0, 0, None
    fires = 0
    for t in range(1, n):
        if np.isnan(st_p[t - 1]):
            expo[t] = pos
            continue
        trig_on = st_p[t - 1] >= trig
        legs = int(rv_p[t - 1] >= trig) + int(dd_p[t - 1] >= trig)
        conf = legs >= (1 if confirm == "1of2" else 2)
        if pos == 1.0 and trig_on and conf:
            pos = 0.5
            fires += 1
            calendar_t0, pending_tranche = t, 0
        elif pos < 1.0:
            reenter_full = False
            if family == "decay":
                reenter_full = st_p[t - 1] < 0.5
            elif family == "phaseD":
                back = ph.quadrant[max(0, t - 5):t]
                reenter_full = len(back) == 5 and (back == SLOWDOWN).all()
            elif family == "calendar":
                held = t - calendar_t0
                gate = st_p[t - 1] < trig
                if held >= 42 and gate and pending_tranche == 0:
                    pos, pending_tranche = 0.75, t
                elif pending_tranche and (t - pending_tranche) >= 21 and gate:
                    reenter_full = True
            if reenter_full:
                pos, pending_tranche = 1.0, 0
        expo[t] = pos
    turn = np.abs(np.diff(expo, prepend=1.0))
    pret = expo * r - turn * COST
    yrs = (dates[-1] - dates[0]) / np.timedelta64(365, "D")
    cagr_p = (np.prod(1 + pret)) ** (1 / yrs) - 1
    cagr_b = (np.prod(1 + r)) ** (1 / yrs) - 1
    deep, imps = [], []
    for name, s0, s1 in EPISODES:
        i = np.where((dates >= np.datetime64(s0)) & (dates <= np.datetime64(s1)))[0]
        if len(i) == 0:
            continue
        bh, rl = episode_dd(r, i[0], i[-1]), episode_dd(pret, i[0], i[-1])
        if bh >= 0.20:
            deep.append(name)
            imps.append(bh - rl)
    return {"drag_pp": (cagr_b - cagr_p) * 100, "deep_imp_pp": float(np.mean(imps)) * 100 if imps else np.nan,
            "deep_set": deep, "fires": fires,
            "time_cut": float((expo < 1.0).mean())}

print(f"Sample: {str(dates[0])[:10]}..{str(dates[-1])[:10]}; buy-hold CAGR "
      f"{((np.prod(1+r))**(1/((dates[-1]-dates[0])/np.timedelta64(365,'D')))-1)*100:.1f}%")
first = True
results = []
for trig in (0.8, 0.9, 0.95):
    for confirm in ("1of2", "2of2"):
        for family in ("phaseD", "decay", "calendar"):
            res = run_cell(trig, confirm, family)
            if first:
                print(f"Deep-episode set (buy-hold DD>=20%): {res['deep_set']}")
                first = False
            ok = (not np.isnan(res["deep_imp_pp"])) and res["deep_imp_pp"] >= 5.0 and res["drag_pp"] <= 2.0
            results.append((trig, confirm, family, res, ok))
            print(f"  trig {trig:.2f} {confirm} {family:9s}: deep-DD improvement "
                  f"{res['deep_imp_pp']:+5.1f}pp | drag {res['drag_pp']:+5.2f}pp/yr | "
                  f"fires {res['fires']:3d} | time cut {res['time_cut']:.0%} | "
                  f"{'SUPPORTIVE' if ok else 'disqualified'}")
n_ok = sum(1 for *_, ok in results if ok)
print(f"\nF2-index: {n_ok}/18 cells SUPPORTIVE (deep-DD imp >= 5pp AND drag <= 2.0pp/yr)")
