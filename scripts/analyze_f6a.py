"""F6a — the whipsaw/false-fire ledger, run exactly as registered (2026-09-03).

State construction, grid, episode list and COST are the F2-index script's VERBATIM
(scripts/analyze_f2_index.py is the record); this script adds only the ledger reads:
fire-start dates, TRUE/FALSE classification against the frozen episode windows,
missed-deep-episode counts, and whipsaw cost/yr at {8, 16, 28} bps per unit turnover.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.ladder.phase import phase_state

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "ingest" / "vault" / "index"
COST = 0.0028
EPISODES = [
    ("GFC core*", "2008-09-01", "2008-11-30"),
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
ph = phase_state(state, k_slope=21, smooth=5)
SLOWDOWN = 2

in_episode = np.zeros(len(r), bool)
ep_windows = []
for name, s0, s1 in EPISODES:
    i = np.where((dates >= np.datetime64(s0)) & (dates <= np.datetime64(s1)))[0]
    if len(i):
        in_episode[i] = True
        ep_windows.append((name, i))


def episode_dd(path_ret, i0, i1):
    lvl = np.cumprod(1.0 + path_ret[i0:i1 + 1])
    peak = np.maximum.accumulate(lvl)
    return float((1.0 - lvl / peak).max())


deep = [(name, i) for name, i in ep_windows if episode_dd(r, i[0], i[-1]) >= 0.20]
deep_names = [n for n, _ in deep]
print(f"Deep episodes (buy-hold DD>=20%): {deep_names}")
yrs = (dates[-1] - dates[0]) / np.timedelta64(365, "D")


def run_cell(trig, confirm, family):
    n = len(r)
    expo = np.ones(n)
    pos, pending_tranche, calendar_t0 = 1.0, 0, None
    fire_starts = []
    for t in range(1, n):
        if np.isnan(st_p[t - 1]):
            expo[t] = pos
            continue
        trig_on = st_p[t - 1] >= trig
        legs = int(rv_p[t - 1] >= trig) + int(dd_p[t - 1] >= trig)
        conf = legs >= (1 if confirm == "1of2" else 2)
        if pos == 1.0 and trig_on and conf:
            pos = 0.5
            fire_starts.append(t)
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
    true_f = sum(1 for t in fire_starts if in_episode[t])
    false_f = len(fire_starts) - true_f
    missed = [n for n, i in deep if not any(i[0] <= t <= i[-1] for t in fire_starts)]
    ann_turn = turn.sum() / yrs
    return {"fires": len(fire_starts), "false": false_f,
            "false_share": false_f / len(fire_starts) if fire_starts else np.nan,
            "missed": missed, "ann_turn": ann_turn,
            "cost_yr": {b: ann_turn * b / 1e4 * 100 for b in (8, 16, 28)}}


print(f"{'cell':32s} fires/yr false%  missed-deep  cost/yr @8/16/28bps")
rows = []
for trig in (0.8, 0.9, 0.95):
    for confirm in ("1of2", "2of2"):
        for family in ("phaseD", "decay", "calendar"):
            c = run_cell(trig, confirm, family)
            rows.append((trig, confirm, family, c))
            missed_str = ",".join(c["missed"]) if c["missed"] else "-"
            print(f"trig {trig:.2f} {confirm} {family:9s}: "
                  f"{c['fires'] / yrs:6.2f}  {c['false_share']*100 if c['fires'] else float('nan'):5.0f}%  "
                  f"{len(c['missed'])} {missed_str:20s} "
                  f"{c['cost_yr'][8]:.2f} / {c['cost_yr'][16]:.2f} / {c['cost_yr'][28]:.2f} %")

# prior reads
fs = {}
for trig, confirm, family, c in rows:
    fs.setdefault((trig, confirm), []).append(c["false_share"])
print("\nfalse-fire share by trigger x confirm (mean over re-entry families):")
for k in sorted(fs):
    print(f"  trig {k[0]:.2f} {k[1]}: {np.nanmean(fs[k])*100:.0f}%")
