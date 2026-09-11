"""Why the re-entry did / did not fire: print the dissipation-trigger components and the regime around dated
lows, plus the model's monthly path in the 2009 recovery. DEV window only."""
from __future__ import annotations
import importlib.util, sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import features as F  # noqa: E402

spec = importlib.util.spec_from_file_location("cde", HERE / "signals" / "composite_dual_engine.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

df = E.load_market(end="2012-06-30")
p = dict(M.DEFAULT_PARAMS)
lev = M.signal(df, **p).reindex(df.index)
vix = df["vix_close"].ffill()
vmax = vix.rolling(M.VIX_WIN, min_periods=M.VIX_WIN).max()
thr = (1 - M.VIX_FALL) * vmax
rsi2 = F.rsi(df["spx_px"], 2)
reg = M.vix_regime(vix, p["v_calm"], p["v_high"], p["hyst"])
regs = pd.Series(np.array(["CALM", "ELEV", "STRESS"])[reg], index=df.index)

print(f"frozen params {p}  (STRESSED entry VIX>{p['v_high']}, exit VIX<{p['v_high']*(1-p['hyst']):.2f}; "
      f"CALM entry VIX<{p['v_calm']*(1-p['hyst']):.2f}, exit VIX>{p['v_calm']})")
for lo, hi, lab in [("2009-03-02", "2009-04-17", "GFC low + rebound"),
                    ("2002-10-01", "2002-10-25", "2002 bear low"),
                    ("2008-11-17", "2008-12-31", "Nov-08 low -> the one GFC burst")]:
    print(f"\n== {lab}")
    for t in df.loc[lo:hi].index:
        print(f"  {t.date()} r{df['spx_ret'][t]*100:+5.2f} VIX {vix[t]:5.1f} 30dmax {vmax[t]:5.1f} "
              f"needVIX<= {thr[t]:5.1f} RSI2 {rsi2[t]:5.1f} {'DISSIP' if (vix[t] <= thr[t] and vix[t] >= M.VIX_MIN and rsi2[t] < M.RSI_MAX) else '      '} "
              f"{regs[t]:6s} L{lev[t]:.0f}")

print("\n== 2009 recovery: first date VIX closes under the STRESSED exit level")
s = vix.loc["2009-03-10":"2010-06-30"]
below = s[s < p["v_high"] * (1 - p["hyst"])]
print(f"   {below.index[0].date()} VIX {below.iloc[0]:.2f}   (model leverage that day: {lev[below.index[0]]:.0f})")
print(f"   model leverage 2009-03-10..2009-12-31 value counts: {lev.loc['2009-03-10':'2009-12-31'].value_counts().to_dict()}")
print(f"   VIX min over 2009-03-10..2009-12-31 = {vix.loc['2009-03-10':'2009-12-31'].min():.2f}")

print("\n== all burst (3x-from-non-3x via the re-entry) and tier-3x spells, 1990+: monthly count of 3x days by year")
l = lev.loc["1990":].fillna(0)
print((l >= 2.5).groupby(l.loc["1990":].index.year).sum().to_dict())
print("\n== worst 6 months, dev_1990")
r = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start="1990-01-01", end="2012-06-30")
mo = (1 + r.daily["ret"]).groupby([r.daily.index.year, r.daily.index.month]).prod() - 1
print((mo.sort_values().head(6) * 100).round(2).to_dict())
print("== best 6 months, dev_1990")
print((mo.sort_values().tail(6) * 100).round(2).to_dict())
