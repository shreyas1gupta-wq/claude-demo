"""T1 — overnight/intraday decomposition of the NIFTY, run exactly as registered.

o_t = Open_t/Close_{t-1} - 1 (overnight); i_t = Close_t/Open_t - 1 (intraday).
Cells: (1) full-sample decomposition; (2) the US-signature bar (overnight mean > 0 AND
intraday mean <= 0, NW t on mean(o-i) >= 2); (3) BR3 era split + COVID sensitivity
(descriptive). Consumption cap (registered): even a PASS cannot arm a trade; the print is
execution-timing context.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

df = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["o"] = df["Open"] / df["Close"].shift(1) - 1
df["i"] = df["Close"] / df["Open"] - 1
df = df.dropna(subset=["o", "i"]).reset_index(drop=True)


def nw_t(x, lags=5):
    x = np.asarray(x, float)
    n = len(x)
    m = x.mean()
    e = x - m
    s = e @ e / n
    for l in range(1, lags + 1):
        w = 1 - l / (lags + 1)
        s += 2 * w * (e[l:] @ e[:-l]) / n
    return m, m / np.sqrt(s / n)


def report(sub, tag):
    o, i = sub["o"].to_numpy(), sub["i"].to_numpy()
    n = len(sub)
    ann = 252
    mo, to = nw_t(o)
    mi, ti = nw_t(i)
    md, td = nw_t(o - i)
    tot = (1 + sub["Close"].iloc[-1] / sub["Close"].iloc[0]) if False else None
    print(f"{tag}: n={n}")
    print(f"  overnight mean {mo*ann*100:+.2f}%/yr (NW t={to:+.2f}) | "
          f"intraday mean {mi*ann*100:+.2f}%/yr (NW t={ti:+.2f}) | "
          f"o-i mean {md*ann*100:+.2f}%/yr (NW t={td:+.2f})")
    return mo, mi, td


print(f"T1 sample {df.Date.min():%Y-%m-%d}..{df.Date.max():%Y-%m-%d}")
mo, mi, td = report(df, "FULL SAMPLE")
bar = (mo > 0) and (mi <= 0) and (td >= 2)
print(f"T1 BAR (US signature: o>0 AND i<=0 AND NW t(o-i)>=2): "
      f"{'PASS' if bar else 'FAIL'}")

report(df[df.Date < "2019-02-01"], "PRE-BR3 (pre weekly-expiry, 2007-2019)")
report(df[df.Date >= "2019-02-01"], "POST-BR3 (2019-02 on)")
cov = (df.Date >= "2020-02-20") & (df.Date <= "2020-04-30")
report(df[~cov], "EX-COVID (sensitivity)")
