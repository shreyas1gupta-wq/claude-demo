"""DEV-only calibration counts for crash_exit_dual: how often the exit ingredients fire, by year (data <= 2012-06-30)."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E, features as F

df = E.load_market(end="2012-06-30")
print("rows", len(df), df.index[0].date(), df.index[-1].date())
print(df.dtypes.to_string())
print("VIX first valid", df["vix_close"].first_valid_index().date(), "nan count", int(df["vix_close"].isna().sum()),
      "nan after 1990:", int(df.loc["1990":, "vix_close"].isna().sum()))
ret = df["spx_ret"]
sig_prev = ret.rolling(21, min_periods=21).std(ddof=1).shift(1)
z = ret / sig_prev
vix = df["vix_close"].ffill()
base = vix.shift(1).rolling(10, min_periods=10).mean()
yr = df.index.year
rows = []
for k in (2.0, 2.25, 2.5, 2.75, 3.0):
    sd = (z < -k).fillna(False)
    pair = sd & sd.shift(1, fill_value=False)
    s = pd.DataFrame({"single": sd, "pair": pair}).groupby(yr).sum()
    rows.append((k, s))
print("\nPer-year counts of single -k sigma days / consecutive pairs (1985-2012):")
hdr = "year " + " ".join(f"k{k:<4}" for k, _ in rows)
print(hdr)
for y in range(1985, 2013):
    print(f"{y} " + " ".join(f"{int(s.loc[y,'single']):2d}/{int(s.loc[y,'pair']):<2d}" for _, s in rows))
print("\nDecade totals of pairs:")
for k, s in rows:
    dec = s["pair"].groupby((s.index // 10) * 10).sum()
    print(f"k={k}: " + " ".join(f"{int(d)}s:{int(v)}" for d, v in dec.items()))
print("\nVIX jump counts per year for j in (0.15,0.2,0.25,0.3,0.4), floor 20:")
for j in (0.15, 0.2, 0.25, 0.3, 0.4):
    jm = ((vix > (1 + j) * base) & (vix >= 20)).fillna(False)
    c = jm.groupby(yr).sum().loc[1990:]
    print(f"j={j}: total {int(c.sum())} | " + " ".join(f"{y}:{int(v)}" for y, v in c.items() if v))
print("\nKey event days (z, VIX, VIX/base):")
for d in ["1987-10-14", "1987-10-15", "1987-10-16", "1987-10-19", "1998-08-04", "1998-08-27", "1998-08-28", "1998-08-31",
          "2008-09-15", "2008-09-29", "2008-10-06", "2008-10-07", "2010-05-06", "2011-08-04", "2011-08-08",
          "1997-10-27", "2007-02-27", "2000-04-14", "2001-09-17", "2002-07-19", "2002-07-22", "1974-11-18", "1974-10-03"]:
    t = pd.Timestamp(d)
    if t in df.index:
        print(f"  {d} ret {ret[t]*100:+.2f}% z {z[t]:+.2f} sigma_prev {sig_prev[t]*100:.2f}% VIX {vix[t]:.1f} VIX/base {vix[t]/base[t] if pd.notna(base[t]) else float('nan'):.2f}")
rv = F.realized_vol(ret, 21)
print("\nRV21 percentiles 1990-2012:", rv.loc["1990":].quantile([.1, .25, .5, .75, .9]).round(3).to_dict())
print("RV21 percentiles 1950-1989:", rv.loc["1950":"1989"].quantile([.1, .25, .5, .75, .9]).round(3).to_dict())
