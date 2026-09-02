"""FS-D3 — CBOE VIX as the interim L2 confirm leg (pre-registered).

Ledger 2026-09-02. Three-leg composite (RV21 pct + DD pct + CBOE-VIX pct, equal weights)
vs the two-leg composite on the F2a episode set at the same 0.3 threshold. VIX aligned to
NIFTY trading days with a 1-day availability lag (US closes after India — same-calendar-day
US data is NOT known at the India close; lag declared here, before running).
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"
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

df = pd.read_csv(VAULT / "index" / "nifty50_daily_2007_2026.csv", parse_dates=["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
r = df["ret"].values
dates = df["Date"]

vix = pd.read_csv(VAULT / "globalvol" / "cboe_vix_daily_1990_2026.csv", parse_dates=["DATE"])
vix = vix.sort_values("DATE").set_index("DATE")["CLOSE"]
vix_al = vix.reindex(pd.DatetimeIndex(dates)).ffill().shift(1).values  # 1-day availability lag

rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
vx_p = expanding_percentile(vix_al, min_obs=252)
s2 = fast_stress_composite(rv_p, dd_p)
s3 = fast_stress_composite(rv_p, dd_p, confirm_pct=vx_p, w_rv=1/3, w_dd=1/3, w_confirm=1/3)

d64 = dates.values
def detect(state):
    got, lags, mask = {}, {}, np.zeros(len(df), bool)
    for name, a, b in EPISODES:
        i = np.where((d64 >= np.datetime64(a)) & (d64 <= np.datetime64(b)))[0]
        if len(i) == 0:
            continue
        w0, w1 = max(0, i[0] - 5), min(len(df) - 1, i[-1] + 21)
        seg = state[w0:w1 + 1]
        hit = np.where(seg >= 0.3)[0]
        got[name] = len(hit) > 0
        if len(hit):
            lags[name] = int(hit[0] + w0 - i[0])
        mask[max(0, i[0] - 42):min(len(df) - 1, i[-1] + 42) + 1] = True
    ok = ~np.isnan(state)
    ff = int(np.nansum((state >= 0.3) & ~mask & ok))
    return got, lags, ff

g2, l2_, ff2 = detect(s2)
g3, l3_, ff3 = detect(s3)
n2, n3 = sum(g2.values()), sum(g3.values())
print(f"2-leg: {n2}/{len(g2)} detected, false-fire days {ff2}")
print(f"3-leg (+CBOE VIX, 1d lag): {n3}/{len(g3)} detected, false-fire days {ff3}")
for name in g2:
    tag = ""
    if g3[name] and not g2[name]: tag = "  <- GAINED by the VIX leg"
    if g2[name] and not g3[name]: tag = "  <- LOST by the VIX leg"
    dl = ""
    if name in l2_ and name in l3_:
        dl = f" | lag {l2_[name]:+d} -> {l3_[name]:+d}bd"
    print(f"  {name}: 2-leg {'HIT ' if g2[name] else 'miss'} / 3-leg {'HIT ' if g3[name] else 'miss'}{dl}{tag}")
net = n3 - n2
ff_rel = (ff3 - ff2) / max(ff2, 1)
ok = (net >= 1) and (ff_rel <= 0.5)
print(f"\nFS-D3a: net episodes {net:+d}, false fires {ff_rel:+.0%} -> BAR (>=+1 and <=+50%): {'PASS' if ok else 'FAIL'}")
both = [n for n in l2_ if n in l3_]
print(f"FS-D3b (measurement): median lag both-caught: 2-leg {np.median([l2_[n] for n in both]):+.0f}bd, "
      f"3-leg {np.median([l3_[n] for n in both]):+.0f}bd")
