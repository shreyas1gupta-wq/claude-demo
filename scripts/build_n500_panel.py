"""Build the vaulted NIFTY500 panel matrices from the upstream per-stock CSVs.

Source: github.com/Ratnesh-bhosale/NIFTY500_dataset @ c2fe39b872488f87f9ea855d6ee79ae372fb4e75
(500 Yahoo-format daily CSVs, 2012-2022; survivorship-biased roster — see the vault's
AUTHENTICATION.md). Outputs two gzipped matrices (dates × tickers):
- n500_adjclose_2012_2022.csv.gz  — "Adj Close" (dividend/split-adjusted)
- n500_value_traded_2012_2022.csv.gz — Close × Volume (rupee value traded, liquidity filter)

Usage: python3 scripts/build_n500_panel.py <clone_dir>
"""
import re
import sys
from pathlib import Path

import pandas as pd

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "panel"

src = Path(sys.argv[1]) / "Dataset"
adj, val = {}, {}
skipped = []
for f in sorted(src.glob("*.csv")):
    ticker = re.sub(r"^\d+_", "", f.stem)
    try:
        df = pd.read_csv(f, parse_dates=["Date"])
        df = df.dropna(subset=["Adj Close"]).drop_duplicates(subset="Date").set_index("Date").sort_index()
        if len(df) == 0:
            skipped.append(ticker)
            continue
        adj[ticker] = df["Adj Close"]
        val[ticker] = df["Close"] * df["Volume"]
    except Exception as e:
        skipped.append(f"{ticker} ({e})")
A = pd.DataFrame(adj).sort_index()
V = pd.DataFrame(val).sort_index()
VAULT.mkdir(parents=True, exist_ok=True)
A.to_csv(VAULT / "n500_adjclose_2012_2022.csv.gz", compression="gzip", float_format="%.6g")
V.to_csv(VAULT / "n500_value_traded_2012_2022.csv.gz", compression="gzip", float_format="%.6g")
print(f"tickers: {A.shape[1]}, dates: {A.shape[0]} ({A.index.min():%Y-%m-%d}..{A.index.max():%Y-%m-%d})")
print(f"skipped: {skipped if skipped else 'none'}")
