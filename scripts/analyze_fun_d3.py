"""FUN-D3 — India sector x market-cycle layer (ONE-WAY: survivor panel 2012-2021;
negatives kill, positives only suggest — stated on every read). Registered 2026-09-08
BEFORE this run. GDP-cycle conditioning is data-gated (IIP/PMI runsheet rows); this
partial uses declared MARKET-CYCLE proxies: NIFTY vs 12m MA x VIX-pct >=0.60, both
lagged one day. Sector reads RELATIVE to the equal-weight all-basket market. Prints only.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"

# baskets verbatim from the SEC battery
_sec = open("/home/user/claude-demo/scripts/analyze_sec_battery.py").read()
_ns = {}
exec(_sec.split("px = pd.read_csv")[0], _ns)
BASKETS = _ns["BASKETS"]

px = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz",
                 parse_dates=["Date"]).set_index("Date").sort_index()
ret = px.pct_change(fill_method=None)
mkt = ret.mean(axis=1)
rel = {}
for name, members in BASKETS.items():
    have = [t for t in members if t in ret.columns]
    rel[name] = ret[have].mean(axis=1) - mkt

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
S = nf["Adj Close"]
ma12 = S.rolling(252).mean()
up = (S > ma12).shift(1)
vx = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
pct = pd.Series(expanding_percentile(vx.to_numpy(), min_obs=252), index=vx.index)
stress = (pct >= 0.60).reindex(S.index).ffill().shift(1)

idx = ret.index
up_ = up.reindex(idx).ffill().fillna(False).astype(bool)
st_ = stress.reindex(idx).ffill().fillna(False).astype(bool)
state = pd.Series(np.where(up_ & ~st_, "CALM-UP", np.where(up_ & st_, "STRESSED-UP",
                  np.where(~up_ & ~st_, "CALM-DOWN", "RISK-OFF"))), index=idx)
STATES = ["CALM-UP", "STRESSED-UP", "CALM-DOWN", "RISK-OFF"]

GROUPS = {"DEFENSIVE": ["FMCG", "PHARMA", "IT"],
          "CYCLICAL": ["METALS", "AUTO", "CAPGOODS", "REALTY"],
          "FINANCIAL": ["PVTBANK", "PSUBANK", "NBFC"]}

# fwd 21d relative return per basket
f21 = {k: (1 + v).rolling(21).apply(np.prod, raw=True).shift(-21) - 1 for k, v in rel.items()}

print("FUN-D3 — India sector x market-cycle (ONE-WAY, survivor panel "
      f"{idx[0].date()}..{idx[-1].date()}; proxy states, NOT GDP phases — declared):")

# s1 frequencies/durations
fr = state.value_counts(normalize=True)
runs = (state != state.shift(1)).cumsum()
dur = state.groupby(runs).agg(["first", "size"]).groupby("first")["size"].median()
print("  s1 states: " + " | ".join(f"{s} {100*fr.get(s, 0):.0f}% (med run {dur.get(s, 0):.0f}d)"
                                    for s in STATES))

# s2-s5 group + full-table reads per state
for s in STATES:
    m = state == s
    grp = {g: 100 * np.nanmedian(pd.concat([f21[b][m] for b in bs]).dropna())
           for g, bs in GROUPS.items()}
    best = max(rel, key=lambda b: np.nanmedian(f21[b][m].dropna()))
    worst = min(rel, key=lambda b: np.nanmedian(f21[b][m].dropna()))
    print(f"  {s:>11}: DEF {grp['DEFENSIVE']:+.2f} | CYC {grp['CYCLICAL']:+.2f} | "
          f"FIN {grp['FINANCIAL']:+.2f} (med fwd-21d rel %) | best {best} "
          f"{100*np.nanmedian(f21[best][m].dropna()):+.2f} worst {worst} "
          f"{100*np.nanmedian(f21[worst][m].dropna()):+.2f}")

# s6 SEC-D6 consistency in RISK-OFF
m = state == "RISK-OFF"
ranks = sorted(((b, 100 * np.nanmedian(f21[b][m].dropna())) for b in rel),
               key=lambda x: -x[1])
print("  s6 RISK-OFF full ranking: " + " > ".join(f"{b}({v:+.1f})" for b, v in ranks[:5])
      + " ... " + " > ".join(f"{b}({v:+.1f})" for b, v in ranks[-3:]))

# s7 transition: 3 months after RISK-OFF -> CALM-UP flip
flips = idx[(state == "CALM-UP") & (state.shift(1) == "RISK-OFF")]
# also count flips through short intermediates: RISK-OFF in prior 10d
flips2 = idx[(state == "CALM-UP") & (state.shift(1) != "CALM-UP")
             & pd.Series((state == "RISK-OFF").rolling(10).max().shift(1), index=idx).astype(bool)]
use = flips2 if len(flips2) >= len(flips) else flips
f63 = {k: (1 + v).rolling(63).apply(np.prod, raw=True).shift(-63) - 1 for k, v in rel.items()}
if len(use):
    grp = {g: 100 * np.nanmedian(pd.concat([f63[b].reindex(use) for b in bs]).dropna())
           for g, bs in GROUPS.items()}
    print(f"  s7 3m after RISK-OFF->CALM-UP flips (n={len(use)} flip-days, SMALL): "
          f"DEF {grp['DEFENSIVE']:+.2f} | CYC {grp['CYCLICAL']:+.2f} | FIN {grp['FINANCIAL']:+.2f}")
else:
    print("  s7 no qualifying flips — cell prints n=0")

# s8 banks by state
for s in STATES:
    m = state == s
    pv = 100 * np.nanmedian(f21["PVTBANK"][m].dropna())
    ps = 100 * np.nanmedian(f21["PSUBANK"][m].dropna())
    print(f"  s8 {s:>11}: PVTBANK {pv:+.2f} vs PSUBANK {ps:+.2f}")

# s9 IT in RISK-OFF (USD-revenue check)
m = state == "RISK-OFF"
print(f"  s9 IT relative in RISK-OFF: median fwd-21d {100*np.nanmedian(f21['IT'][m].dropna()):+.2f}% "
      f"(CU-D7 USD-coupling check at sector level)")

# s10 era halves for the headline defensives-in-risk-off read
for lab, a, b in [("2012-16", "2012-01-01", "2016-12-31"), ("2017-21", "2017-01-01", "2021-12-31")]:
    m = (state == "RISK-OFF") & (idx >= a) & (idx <= b)
    d_ = 100 * np.nanmedian(pd.concat([f21[x][m] for x in GROUPS["DEFENSIVE"]]).dropna())
    c_ = 100 * np.nanmedian(pd.concat([f21[x][m] for x in GROUPS["CYCLICAL"]]).dropna())
    print(f"  s10 {lab} RISK-OFF: DEF {d_:+.2f} vs CYC {c_:+.2f}")
