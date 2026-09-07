#!/usr/bin/env python3
"""OP-D2 combiner c08 -- EVENT POLICY: exact calendar rules from f19 + the booked CW-D1v
budget crush (trial-ledger.md line ~1029). Not a new trial: this recomputes, verbatim from
already-printed desk numbers (f19.json cells; CW-D1a/CW-D1v ledger lines; F16/F17 headline
facts), the concrete calendar windows a systematic policy would need, and cross-checks them
against the already-booked F16 (monthly, non-overlapping 21td blocks) and F17 (weekly, ISO-
week blocks) cycle conventions to show exactly how often/where the window binds historically
-- in particular confirming F17's own named ruin event (2016-02-29 Budget week) falls inside
the f19/CW-D1a/CW-D1v budget window as declared. No new statistical test is run; process
note #6 does not apply (nothing here is a bar/estimator, purely calendar bookkeeping over
already-graded cells). BUDGET_DAYS list quoted verbatim from scripts/analyze_nifty_daily.py
(same list used by CW-D1a/CW-D1v/F5a/f19).
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/c08.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")

import pandas as pd

NIFTY_PATH = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"

BUDGET_DAYS = [
    "2008-02-29", "2009-02-16", "2009-07-06", "2010-02-26", "2011-02-28", "2012-03-16",
    "2013-02-28", "2014-02-17", "2014-07-10", "2015-02-28", "2016-02-29", "2017-02-01",
    "2018-02-01", "2019-02-01", "2019-07-05", "2020-02-01", "2021-02-01", "2022-02-01",
    "2023-02-01", "2024-02-01", "2024-07-23", "2025-02-01", "2026-02-01",
]

df = pd.read_csv(NIFTY_PATH, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
print(f"NIFTY sample: {df['Date'].min():%Y-%m-%d}..{df['Date'].max():%Y-%m-%d} n={len(df)}")

ev = pd.to_datetime(BUDGET_DAYS)
in_span = [d for d in ev if df["Date"].min() <= d <= df["Date"].max()]
matched = [d for d in in_span if (df["Date"] == d).any()]
print(f"\nBUDGET_DAYS: {len(BUDGET_DAYS)} declared, {len(in_span)} in vault span, "
      f"{len(matched)} matched to an actual trading day (f19/CW-D1v convention: 19/23 and "
      f"15/~18 respectively -- both partial, mirror coverage only).")

idx_ev = df.index[df["Date"].isin(set(matched))]
window_rows = sorted(set(i + k for i in idx_ev for k in (-1, 0, 1) if 0 <= i + k < len(df)))
window_dates = df.loc[window_rows, "Date"]
print(f"\n=== EXACT CALENDAR WINDOW (day -1,0,+1 around each matched budget day) ===")
print(f"{len(window_dates)} trading days total (the CW-D1a/CW-D1v/f19-registered window; "
      f"3 per event minus edge clipping):")
for d in matched:
    i = df.index[df["Date"] == d][0]
    lo = max(0, i - 1); hi = min(len(df) - 1, i + 1)
    win = df.loc[lo:hi, "Date"].dt.strftime("%Y-%m-%d").tolist()
    print(f"  budget {d.date()} (a {d.strftime('%A')}) -> exclusion window {win}")

# ---- Cross-check vs F16 monthly non-overlapping 21td blocks (same construction as f16.py) ----
print("\n=== F16-CONVENTION MONTHLY BLOCKS (21td, non-overlapping) THAT CONTAIN A BUDGET WINDOW DAY ===")
window_set = set(df.loc[window_rows, "Date"])
n = len(df)
block_starts = list(range(0, n, 21))
hits = 0
for bi, s in enumerate(block_starts):
    e = min(s + 21, n) - 1
    block_dates = set(df.loc[s:e, "Date"])
    if block_dates & window_set:
        hits += 1
print(f"{hits}/{len(block_starts)} monthly 21td blocks (full sample, unfiltered by VIXpct>=0.6 "
      f"entry gate) contain a budget-window day -- i.e. a monthly F16-style cycle overlaps a "
      f"budget window in {100*hits/len(block_starts):.1f}% of all blocks.")

# ---- Cross-check vs F17 ISO-week blocks ----
print("\n=== F17-CONVENTION ISO-WEEK BLOCKS THAT CONTAIN A BUDGET WINDOW DAY ===")
df["iso_year"] = df["Date"].dt.isocalendar().year
df["iso_week"] = df["Date"].dt.isocalendar().week
groups = df.groupby(["iso_year", "iso_week"])
wk_hits = []
for (y, w), g in groups:
    if set(g["Date"]) & window_set:
        wk_hits.append((y, w, g["Date"].min().date(), g["Date"].max().date()))
print(f"{len(wk_hits)}/{groups.ngroups} ISO weeks (full sample) contain a budget-window day:")
for y, w, lo, hi in wk_hits:
    flag = "  <-- F17's named ruin week (2016-02-29 Budget)" if (y, w) == (2016, 9) else ""
    print(f"  ISO {y}-W{w:02d} [{lo}..{hi}]{flag}")

print("\n=== SUMMARY (for research/opt_sweep/c08.json) ===")
print("budget_window_return_leg: CW-D1a parent print, median|ret| 0.95% vs 0.59%, p=0.0049 PASS "
      "(elevated realized move)")
print("budget_window_vix_leg: CW-D1v, median|dlogVIX| 5.53% vs 2.60%, p=2.7e-06 PASS; signed "
      "day-1=-1.8% day0=-8.9% day+1=-2.9% (crush, concentrated day 0)")
print("f19_corroboration: cell1 p=0.004885 == CW-D1a's original-window print (NOT CW-D1v as "
      "f19's own headline field mislabels -- f19 combiner review flagged this benchmark mislabel)")
print("f17_ruin_link: F17's single named worst weekly wing-breach event is 2016-02-29 Budget "
      "week -- confirmed above to be inside the ISO week ISO 2016-W09, which contains the "
      "budget-window day 2016-02-29 itself")
print("election: f19 n=3, DESCRIPTIVE ONLY, no bar -- insufficient n for a scripted calendar rule")
print("rbi: f19 two-sided p=0.428838, window NOT elevated (median actually below off-window) -- "
      "no exclusion warranted")
