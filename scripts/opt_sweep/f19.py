"""OP-D2 / f19 -- event calendar: |move| and VIX behavior around budget/election/RBI dates.

Registered cell (research/register/trial-ledger.md, Entry OP-D2, family F19):
  "F19 event calendar: |move| and VIX behavior around budget/election/RBI dates
   (declared public dates) (3) -- prior: budget vol-crush (CW-D1v cited);
   elections = the tail."
Three registered cells, one per event type (budget / election / RBI), fixed BEFORE any
number was computed:
  Cell 1 BUDGET -- |return| on budget-day window (day -1,0,+1) vs all other days.
    Event list = BUDGET_DAYS, IDENTICAL to the canonical list already used by
    CW-D1a/CW-D1v/F5a (scripts/analyze_nifty_daily.py), quoted verbatim below.
    BAR (matches CW-D1a/CW-D1v convention): one-sided Mann-Whitney, window |ret|
    elevated vs off-window, p < 0.05.
  Cell 2 ELECTION -- |return| + (where covered) VIX pctile on the 3 declared election
    result days. n=3 (n=2 for the VIX leg, 2009 pre-dates the VIX vault) is too small
    for a hypothesis test -> DESCRIPTIVE ONLY, no bar (matches "elections = the tail"
    prior: report each event's percentile rank in the full |return| distribution).
  Cell 3 RBI -- |return| on RBI scheduled-policy-day window (day -1,0,+1) vs all other
    days. Event list = RBI MPC bi-monthly policy-outcome dates, Oct-2016..Dec-2019
    (the stable, well-documented bi-monthly-cadence sub-period only; pre-MPC and
    COVID-era emergency/off-cycle reviews excluded by design -- scope limitation
    stated up front, not moved after the fact). Dates recalled from public record,
    NOT independently re-verified against a live RBI source in this offline sandbox
    (NSE/RBI egress blocked per CONTRACT) -- tagged [VERIFY: RBI MPC policy calendar].
    No directional prior stated in the ledger one-liner for RBI -> BAR is two-sided:
    report whether window |ret| is elevated OR suppressed vs off-window, MW two-sided
    p < 0.05; verdict recorded TWO-SIDED regardless of direction.

No-lookahead: every stat below is a full-sample descriptive/rank-sum comparison over a
FIXED, pre-declared public event list -- no state is fit or refit at time t (no model
carries information forward), so the CONTRACT no-lookahead clause is satisfied trivially
(it binds fitted states, not comparisons against a public calendar).

Data: ingest/vault/index/nifty50_daily_2007_2026.csv (returns); ingest/vault/vix/
india_vix_daily_2010_2023.csv (VIX, cell 2 only, expanding percentile min_obs=252 via
quant.ladder.credit_cycle.expanding_percentile, per DATA CHEAT-SHEET).
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f19.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder.credit_cycle import expanding_percentile

NIFTY_PATH = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"
VIX_PATH = "/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv"
MIN_OBS = 252

# ---- BUDGET_DAYS: quoted verbatim from scripts/analyze_nifty_daily.py ----
BUDGET_DAYS = [
    "2008-02-29", "2009-02-16", "2009-07-06", "2010-02-26", "2011-02-28", "2012-03-16",
    "2013-02-28", "2014-02-17", "2014-07-10", "2015-02-28", "2016-02-29", "2017-02-01",
    "2018-02-01", "2019-02-01", "2019-07-05", "2020-02-01", "2021-02-01", "2022-02-01",
    "2023-02-01", "2024-02-01", "2024-07-23", "2025-02-01", "2026-02-01",
]

# ---- ELECTION_DAYS: Lok Sabha result days, public record ----
ELECTION_DAYS = ["2009-05-18", "2014-05-16", "2019-05-23"]

# ---- RBI_DAYS: MPC bi-monthly policy-outcome dates, Oct-2016..Dec-2019 only
#      ([VERIFY: RBI MPC policy calendar] -- recalled public record, not re-verified
#      live in this sandbox; pre-MPC era and COVID-era off-cycle reviews excluded) ----
RBI_DAYS = [
    "2016-10-04", "2016-12-07",
    "2017-02-08", "2017-04-06", "2017-06-07", "2017-08-02", "2017-10-04", "2017-12-06",
    "2018-02-07", "2018-04-05", "2018-06-06", "2018-08-01", "2018-10-05", "2018-12-05",
    "2019-02-07", "2019-04-04", "2019-06-06", "2019-08-07", "2019-10-04", "2019-12-05",
]

df = pd.read_csv(NIFTY_PATH, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["ret"] = df["Adj Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
print(f"NIFTY sample: {df['Date'].min():%Y-%m-%d}..{df['Date'].max():%Y-%m-%d} n={len(df)}")

vdf = pd.read_csv(VIX_PATH, parse_dates=["date"]).sort_values("date").reset_index(drop=True)
vdf["vix_pct"] = expanding_percentile(vdf["close"].to_numpy(float), min_obs=MIN_OBS)
print(f"VIX sample: {vdf['date'].min():%Y-%m-%d}..{vdf['date'].max():%Y-%m-%d} n={len(vdf)} "
      f"(expanding pctile min_obs={MIN_OBS})")


def window_test(event_days, label, alt):
    ev = pd.to_datetime(event_days)
    in_span = [d for d in ev if df["Date"].min() <= d <= df["Date"].max()]
    matched = [d for d in in_span if (df["Date"] == d).any()]
    is_ev = df["Date"].isin(set(matched))
    idx_ev = df.index[is_ev]
    w = sorted(set(i + k for i in idx_ev for k in (-1, 0, 1) if 0 <= i + k < len(df)))
    onw = df.loc[w, "ret"].abs() * 100
    off = df.loc[~df.index.isin(w), "ret"].abs() * 100
    u, p = stats.mannwhitneyu(onw, off, alternative=alt)
    print(f"\n{label}: {len(matched)}/{len(in_span)} events matched to trading days "
          f"({len(w)} window days)")
    print(f"  window median|ret|={onw.median():.3f}% vs off-window {off.median():.3f}%")
    print(f"  MW alt='{alt}' p={p:.6f}")
    return onw, off, p, len(matched), len(in_span)


print("\n=== CELL 1: BUDGET (bar: one-sided elevated, p<0.05) ===")
onw_b, off_b, p_b, m_b, tot_b = window_test(BUDGET_DAYS, "BUDGET", "greater")
bar1_pass = p_b < 0.05
print(f"BAR -> {'PASS' if bar1_pass else 'MISS'}")

print("\n=== CELL 2: ELECTION (n too small for a test -> DESCRIPTIVE) ===")
ev = pd.to_datetime(ELECTION_DAYS)
for d in ev:
    row = df[df["Date"] == d]
    if len(row):
        r = row["ret"].iloc[0] * 100
        rank = (df["ret"].abs() < abs(row["ret"].iloc[0])).mean() * 100
        print(f"  {d.date()}: ret={r:+.2f}%  |ret| percentile-rank in full sample={rank:.1f}")
    else:
        print(f"  {d.date()}: not a matched NIFTY trading day in vault")
    vrow = vdf[vdf["date"] == d]
    if len(vrow) and not np.isnan(vrow["vix_pct"].iloc[0]):
        print(f"    VIX close={vrow['close'].iloc[0]:.2f}, expanding pctile={vrow['vix_pct'].iloc[0]:.3f}")
    else:
        print(f"    VIX: no coverage (pre-vault or pre-min_obs warm-up)")
election_abs_rets = [df[df['Date'] == d]['ret'].iloc[0] * 100 for d in ev if len(df[df['Date'] == d])]
max_election_abs = max(abs(r) for r in election_abs_rets)
print(f"largest |election-day return| = {max_election_abs:.2f}%")

print("\n=== CELL 3: RBI (bar: two-sided, p<0.05, no direction pre-specified) ===")
onw_r, off_r, p_r, m_r, tot_r = window_test(RBI_DAYS, "RBI", "two-sided")
direction = "elevated" if onw_r.median() > off_r.median() else "suppressed"
bar3_signif = p_r < 0.05
print(f"direction observed: window |ret| {direction} vs off-window")
print(f"BAR (two-sided, p<0.05) -> {'SIGNIFICANT' if bar3_signif else 'NOT SIGNIFICANT'} "
      f"(recorded TWO-SIDED either way)")

print("\n=== SUMMARY ===")
print(f"cell1_budget_p={p_b:.6f} verdict={'PASS' if bar1_pass else 'MISS'}")
print(f"cell2_election_max_abs_ret={max_election_abs:.2f} verdict=DESCRIPTIVE")
print(f"cell3_rbi_p={p_r:.6f} direction={direction} verdict=TWO-SIDED")
