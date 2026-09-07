"""MR-D1 — the mean-reversion battery. Registered 2026-09-08 BEFORE this run.

NIFTY vault 2011-07..2023-03; signals at signal-day close; expanding percentiles
min_obs=252. m5 = the overlay economics cell whose frozen inclusion rule gates the MR
axis of the OP-D7 grid. Prints only.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
D0, D1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31")
R = 0.06

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
S = nf["Adj Close"]
r = S.pct_change()
vx = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
pct = pd.Series(expanding_percentile(vx.to_numpy(), min_obs=252), index=vx.index)
sd = pct.reindex(S.index).ffill()

w = r.loc[D0:D1]
sd_w = sd.loc[D0:D1]
print(f"MR-D1 — mean-reversion battery, {D0.date()}..{D1.date()} (n={len(w)} days):")

# m1: next-1d after >=3 consecutive down days
down = (r < 0).astype(int)
run3 = (down.rolling(3).sum() == 3).reindex(w.index).fillna(False).astype(bool)
nxt = r.shift(-1).loc[D0:D1]
m1 = nxt[run3].mean()
print(f"  m1 next-1d after >=3 down days: {10000*m1:+.1f}bp vs unconditional {10000*nxt.mean():+.1f}bp "
      f"(n={int(run3.sum())})")

# m2: next-5d after bottom-decile trailing-5d return (expanding decile), calm/stress
r5 = S.pct_change(5)
r5p = pd.Series(expanding_percentile(r5.dropna().to_numpy(), min_obs=252), index=r5.dropna().index)
sig5 = (r5p <= 0.10).reindex(w.index).fillna(False).astype(bool)
f5 = (S.shift(-5) / S - 1).loc[D0:D1]
calm, stress = sig5 & (sd_w < 0.60), sig5 & (sd_w >= 0.60)
print(f"  m2a next-5d after bottom-decile 5d ret, CALM: {100*f5[calm].mean():+.2f}% (n={int(calm.sum())}) "
      f"vs unconditional {100*f5.mean():+.2f}%")
print(f"  m2b same, STRESS (VIX-pct>=0.60): {100*f5[stress].mean():+.2f}% (n={int(stress.sum())})")

# m3: weekly MR — next-week after k consecutive down weeks
wk = S.resample("W-FRI").last().pct_change().dropna()
win = wk.loc[D0:D1]
dwn = (wk < 0).astype(int)
nxtw = wk.shift(-1)
for k, tag in [(2, "m3a"), (3, "m3b")]:
    s_ = (dwn.rolling(k).sum() == k).reindex(win.index).fillna(False).astype(bool)
    print(f"  {tag} next-week after {k} down weeks: {100*nxtw.reindex(win.index)[s_].mean():+.2f}% "
          f"(n={int(s_.sum())}) vs unconditional {100*nxtw.reindex(win.index).mean():+.2f}%")

# m4: monthly bets — next-month after <=-5% month; + conditional VIX-pct>=0.80
mo = S.resample("ME").last().pct_change().dropna()
mom_w = mo.loc[D0:D1]
nxtm = mo.shift(-1)
big_dn = (mo <= -0.05).reindex(mom_w.index).fillna(False).astype(bool)
pct_me = sd.resample("ME").last().reindex(mom_w.index)
m4b_sig = big_dn & (pct_me >= 0.80)
print(f"  m4a next-month after a <=-5% month: {100*nxtm.reindex(mom_w.index)[big_dn].mean():+.2f}% "
      f"(n={int(big_dn.sum())}) vs unconditional {100*nxtm.reindex(mom_w.index).mean():+.2f}%")
print(f"  m4b same AND VIX-pct>=0.80: {100*nxtm.reindex(mom_w.index)[m4b_sig].mean():+.2f}% "
      f"(n={int(m4b_sig.sum())})")

# m5: the overlay economics cell — +0.30x book for 5td after (bottom-decile 5d AND pct>=0.60)
active = pd.Series(False, index=w.index)
cnt = 0
for t in w.index:
    if cnt > 0:
        active[t] = True
        cnt -= 1
    if bool(stress.get(t, False)) and cnt == 0:
        cnt = 5  # activates from the NEXT day (signal at close)
ov = (0.30 * (w - R / 252)).where(active, 0.0)
eqo = (1 + ov).cumprod()
yrs = (D1 - D0).days / 365.25
contrib = 100 * (eqo.iloc[-1] ** (1 / yrs) - 1)
exc = (w - R / 252)[active]
h1 = ov.loc[:"2016-12-31"]
h2 = ov.loc["2017-01-01":]
c1 = 100 * ((1 + h1).prod() ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
c2 = 100 * ((1 + h2).prod() ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)
print(f"  m5 overlay (+0.30x book, 5td, stress-gated): contribution {contrib:+.2f}%/yr | "
      f"active days {int(active.sum())} ({100*active.mean():.0f}%) | active-day mean excess "
      f"{10000*exc.mean():+.1f}bp | halves {c1:+.2f}/{c2:+.2f} %/yr")
inc = (exc.mean() > 0) and (c1 > 0) and (c2 > 0)
print(f"  INCLUSION RULE: active-day excess>0 AND both halves>0 -> "
      f"{'MET — MR axis ENTERS the OP-D7 grid' if inc else 'NOT MET — MR axis DROPPED'}")
