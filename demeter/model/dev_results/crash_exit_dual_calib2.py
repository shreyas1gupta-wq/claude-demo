"""DEV-only: 2-day cumulative z alternative for the shock trigger, per-year counts + key events (data <= 2012-06-30)."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E, features as F

df = E.load_market(end="2012-06-30")
ret = df["spx_ret"]
sig1 = ret.rolling(21, min_periods=21).std(ddof=1).shift(1)          # sigma before day t
sig2 = sig1.shift(1)                                                 # sigma before day t-1 (before both days)
z1 = ret / sig1
z2 = (ret + ret.shift(1)) / (sig2 * np.sqrt(2))
yr = df.index.year
ks = (2.5, 3.0, 3.5, 4.0, 4.5)
print("Per-year counts of z2 < -k2 (2-day cumulative), 1985-2012:")
print("year  " + " ".join(f"k{k:<4}" for k in ks))
tab = {k: (z2 < -k).fillna(False).groupby(yr).sum() for k in ks}
for y in range(1985, 2013):
    print(f"{y}  " + " ".join(f"{int(tab[k].loc[y]):3d}  " for k in ks))
print("\nDecade totals z2 events:")
for k in ks:
    dec = tab[k].groupby((tab[k].index // 10) * 10).sum()
    print(f"k2={k}: " + " ".join(f"{int(d)}s:{int(v)}" for d, v in dec.items() if d >= 1950))
print("\nDistinct clusters (events separated by >5 sessions), 1990-2012:")
for k in ks:
    ev = (z2 < -k).fillna(False)
    idx = np.where(ev.values)[0]
    idx = idx[df.index[idx] >= pd.Timestamp("1990-01-01")]
    clusters = 1 + int(np.sum(np.diff(idx) > 5)) if len(idx) else 0
    print(f"  k2={k}: {len(idx)} events in {clusters} clusters ({clusters/22.5:.1f}/yr)")
print("\nKey event days: z1 (own day) and z2 (2-day cum):")
for d in ["1987-10-14", "1987-10-15", "1987-10-16", "1987-10-19", "1998-08-04", "1998-08-27", "1998-08-28", "1998-08-31",
          "2008-09-15", "2008-09-17", "2008-09-29", "2008-10-02", "2008-10-06", "2008-10-07", "2008-10-09", "2010-05-06", "2010-05-07",
          "2011-08-04", "2011-08-08", "1997-10-27", "2007-02-27", "2000-04-14", "2001-09-17", "2002-07-19", "2002-07-22",
          "1974-11-18", "1973-11-26", "1962-05-28", "1955-09-26", "1989-10-13", "1991-11-15", "1996-03-08", "1994-02-04",
          "2007-08-09", "2007-11-01", "2008-01-17", "2008-01-22", "2008-06-26", "2009-01-20", "2009-02-17", "2009-03-02"]:
    t = pd.Timestamp(d)
    if t in df.index:
        i = df.index.get_loc(t)
        print(f"  {d} ret {ret.iloc[i]*100:+.2f}% prev {ret.iloc[i-1]*100:+.2f}%  z1 {z1.iloc[i]:+.2f}  z2 {z2.iloc[i]:+.2f}  sigma_prev {sig1.iloc[i]*100:.2f}%")
