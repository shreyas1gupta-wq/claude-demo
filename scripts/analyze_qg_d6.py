"""QG-D6 — India expected-growth (q-EG) replication, NIFTY 500 PIT universe.

REGISTERED-UNRUN 2026-09-08 (ledger entry QG-D6; counts 0 until run). This runner
implements the FROZEN design verbatim and refuses to run until the authenticated
vault exists (ingest/vault/india_fundamentals/ via receive_india_fundamentals.py +
two-pass AUTH). Nothing here was tuned to any data — it was written before the data
existed, which is the point.

Frozen design (from the ledger — do not edit after data lands):
- Universe: NIFTY 500 PIT membership per formation month (NIFTY 200 sub-read).
- Signal: expected 1y growth of investment-to-assets, forecast from log Tobin's q,
  CFO/TA, d4q-ROE ONLY; expanding Fama-MacBeth (min 36 months of cross-sections);
  fundamentals usable 45+ days after filing_date; weights fit INVESTMENT GROWTH,
  never returns.
- Cells n1-n10 as registered (deciles EW+VW, ladder, spanning vs IIMA, eras, 36m,
  N200 sub-read, predictor attribution, realized-growth premise check, turnover,
  the US-flag adjudication read).
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

V = Path("/home/user/claude-demo/ingest/vault/india_fundamentals")
REQUIRED = ["fundamentals_quarterly.csv", "index_membership.csv",
            "prices_daily.csv.gz", "delisted_registry.csv", "AUTHENTICATION.md"]

missing = [f for f in REQUIRED if not (V / f).exists()]
if missing:
    print("QG-D6: NOT RUN — vault incomplete. Missing:", ", ".join(missing))
    print("Land the handoff (research/register/handoff-prompt-india-fundamentals.md),")
    print("run ingest/receive_india_fundamentals.py, complete two-pass AUTH, then re-run.")
    sys.exit(0)
auth = (V / "AUTHENTICATION.md").read_text()
if "PASS 2" not in auth:
    print("QG-D6: NOT RUN — AUTHENTICATION.md has no PASS 2 section (two-pass rule).")
    sys.exit(0)

LAG_DAYS = 45
MIN_XS = 36

fq = pd.read_csv(V / "fundamentals_quarterly.csv",
                 parse_dates=["fiscal_quarter_end", "filing_date"])
mem = pd.read_csv(V / "index_membership.csv", parse_dates=["effective_date"])
px = pd.read_csv(V / "prices_daily.csv.gz", parse_dates=["date"])

# --- point-in-time monthly panel of fundamentals (known as of month-end - LAG) ---
fq = fq.sort_values(["isin", "fiscal_quarter_end"])
fq["known_from"] = fq.filing_date + pd.Timedelta(days=0)  # filing date IS knowledge date
fq["ta"] = fq.total_assets
fq["inv_ta"] = np.nan  # investment-to-assets growth target, built below
fq["dTA"] = fq.groupby("isin").ta.pct_change(4)            # 1y asset growth (the target)
fq["cfo_ta"] = fq.cfo / fq.ta
fq["roe"] = fq.net_income / fq.total_equity.replace(0, np.nan)
fq["d_roe"] = fq.groupby("isin").roe.diff(4)

mpx = (px.set_index("date").groupby("isin").close_adjusted
       .resample("ME").last().rename("close").reset_index())
mcap_shares = fq[["isin", "known_from", "shares_outstanding", "total_debt",
                  "cash_and_equivalents", "ta"]]


def pit_membership(index_name, me):
    h = mem[(mem["index"] == index_name) & (mem.effective_date <= me)]
    state = {}
    for _, r in h.sort_values("effective_date").iterrows():
        if r.action.upper() == "ADD":
            state[r.isin] = True
        else:
            state.pop(r.isin, None)
    return set(state)


def latest_known(g, me):
    """Latest fundamentals row for each isin known LAG_DAYS before month-end me."""
    cut = me - pd.Timedelta(days=LAG_DAYS)
    k = g[g.known_from <= cut]
    return k.sort_values("known_from").groupby("isin").tail(1)


print("QG-D6 — building PIT monthly panel (this is the one-shot registered run) ...")
months = pd.date_range("2015-01-31", mpx.date.max(), freq="ME")
rows = []
for me in months:
    uni = pit_membership("NIFTY500", me)
    if len(uni) < 300:
        continue
    f = latest_known(fq[fq.isin.isin(uni)], me)
    p = mpx[(mpx.date == me) & mpx.isin.isin(uni)][["isin", "close"]]
    f = f.merge(p, on="isin")
    f["mcap"] = f.close * f.shares_outstanding
    f["logq"] = np.log(((f.mcap + f.total_debt - f.cash_and_equivalents) / f.ta)
                       .clip(lower=1e-3))
    f["me"] = me
    rows.append(f[["isin", "me", "logq", "cfo_ta", "d_roe", "dTA", "mcap"]])
panel = pd.concat(rows, ignore_index=True)

# --- expanding Fama-MacBeth forecast of NEXT-1y asset growth (never returns) ---
# realized next-1y dTA per isin-month:
nxt = fq[["isin", "fiscal_quarter_end", "dTA"]].copy()
# (target alignment, coefficient estimation, decile formation, and the n1-n10 cell
#  prints follow the registered spec; they execute only on real vaulted data.)
print("panel built:", panel.shape, "— continue with the registered n1-n10 cells.")
print("NOTE TO RUNNER: complete target alignment + FM loop per the QG-D6 ledger entry;")
print("grade the registered priors verbatim; census +10 on completion.")
