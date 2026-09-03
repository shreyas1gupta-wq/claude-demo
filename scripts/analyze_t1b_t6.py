"""T1b (overnight drift under stress) + T6-TOM (turn-of-month, SIP-era split) — as registered."""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import realized_vol

ROOT = Path(__file__).resolve().parents[1]

EPISODES = [  # frozen §3 in-span list (verbatim from analyze_nifty_daily.py)
    ("Jan-2008 crash", "2008-01-01", "2008-02-15"),
    ("GFC core", "2008-09-01", "2008-11-30"),
    ("EU/downgrade 2011", "2011-08-01", "2011-11-30"),
    ("Taper tantrum", "2013-05-01", "2013-09-30"),
    ("China deval 2015", "2015-08-01", "2015-09-30"),
    ("Demonetization", "2016-11-08", "2016-11-30"),
    ("Feb-2018 vol+LTCG", "2018-02-01", "2018-03-31"),
    ("IL&FS", "2018-09-01", "2018-10-31"),
    ("COVID crash", "2020-02-20", "2020-04-30"),
    ("Russia 2022", "2022-02-01", "2022-03-31"),
    ("Election day 2024", "2024-06-04", "2024-06-10"),
    ("INR/FII May-2026", "2026-05-01", "2026-06-30"),
]


def nw_t(x, lags=5):
    x = np.asarray(x, float)
    n, m = len(x), np.mean(x)
    e = x - m
    s = e @ e / n
    for l in range(1, lags + 1):
        s += 2 * (1 - l / (lags + 1)) * (e[l:] @ e[:-l]) / n
    return m, m / np.sqrt(s / n)


df = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["o"] = df["Open"] / df["Close"].shift(1) - 1
df["i"] = df["Close"] / df["Open"] - 1
df["ret"] = df["Close"].pct_change()

# ---------------- T1b ----------------
in_ep = pd.Series(False, index=df.index)
for _, s0, s1 in EPISODES:
    in_ep |= (df.Date >= s0) & (df.Date <= s1)
rets_clean = df.dropna(subset=["ret"])
rv_p = pd.Series(expanding_percentile(realized_vol(rets_clean["ret"].to_numpy(), 21),
                                      min_obs=252), index=rets_clean.index)
df["rv_hi"] = (rv_p.reindex(df.index).shift(1) >= 0.90)

d = df.dropna(subset=["o", "i"])
print("T1b — the overnight drift under stress (means %/yr, NW t):")
for label, mask in [("in-episode", in_ep[d.index]), ("out-of-episode", ~in_ep[d.index]),
                    ("rv_p>=0.90 (prior day)", d["rv_hi"].fillna(False)),
                    ("rv_p<0.90", ~d["rv_hi"].fillna(False))]:
    sub = d[mask.to_numpy() if hasattr(mask, "to_numpy") else mask]
    mo, to = nw_t(sub["o"])
    mi, ti = nw_t(sub["i"])
    print(f"  {label:24s} n={len(sub):5d}: overnight {mo*252*100:+7.2f}%/yr (t={to:+.2f}) | "
          f"intraday {mi*252*100:+7.2f}%/yr (t={ti:+.2f})")
ep = d[in_ep[d.index].to_numpy()]
mo_ep, to_ep = nw_t(ep["o"])
if to_ep <= -2:
    verdict = "overnight is where stress lands (significantly negative)"
elif abs(to_ep) < 2:
    verdict = "drift ABSENT in stress (null as barred)"
else:
    verdict = "drift SURVIVES stress (positive, significant) — prior wrong"
print(f"T1b VERDICT (in-episode overnight): {verdict}")

# ---------------- T6-TOM ----------------
r = df.dropna(subset=["ret"]).copy()
r["ym"] = r.Date.dt.to_period("M")
tom = pd.Series(False, index=r.index)
for ym, g in r.groupby("ym"):
    tom.loc[g.index[-1]] = True            # last trading day of month
    nxt = r[r.ym == ym + 1]
    tom.loc[nxt.index[:4]] = True          # first 4 of next month
r["tom"] = tom
def tom_stats(sub, tag):
    a, b = sub[sub.tom]["ret"], sub[~sub.tom]["ret"]
    u, p = stats.mannwhitneyu(a, b, alternative="greater")
    prem = (a.mean() - b.mean()) * 1e4
    print(f"  {tag:28s}: ToM n={len(a):4d} mean {a.mean()*1e4:+.1f}bp/d vs other "
          f"{b.mean()*1e4:+.1f}bp/d -> premium {prem:+.1f}bp/d, one-sided p={p:.4f}")
    return prem
print("\nT6-TOM — turn-of-month, era split at BR6 (2015-04):")
prem_full = tom_stats(r, "FULL 2007-2026")
prem_pre = tom_stats(r[r.Date < "2015-04-01"], "PRE-BR6 (2007-2015)")
prem_post = tom_stats(r[r.Date >= "2015-04-01"], "POST-BR6 / SIP era (2015-)")
print(f"T6 BAR (i) full-sample premium p<0.05: "
      f"{'PASS' if stats.mannwhitneyu(r[r.tom]['ret'], r[~r.tom]['ret'], alternative='greater')[1] < 0.05 else 'FAIL'}")
print(f"T6 BAR (ii) fingerprint (post > pre, direction only): "
      f"{'PRESENT' if prem_post > prem_pre else 'ABSENT — recorded against H61 index-level relevance'} "
      f"(pre {prem_pre:+.1f} vs post {prem_post:+.1f} bp/d)")
