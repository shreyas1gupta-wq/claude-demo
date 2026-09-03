#!/usr/bin/env python3
"""Extract daily (New York 4 PM) settlement-aligned futures prices from a pysystemtrade clone.

pysystemtrade stores back-adjusted ("Panama-stitched") prices with UTC timestamps: one row per day
(stamped 23:00) before 2013-10, hourly bars afterwards. To align with the NYSE cash close we convert to
America/New_York and keep the last bar at or before 16:15 local time on each local date.

Usage:  python3 extract_pysystemtrade.py --src /path/to/pysystemtrade/data/futures [--symbols SP500 NASDAQ FED SOFR VIX]
Writes raw/pysystemtrade_<SYMBOL>_daily.csv with columns date, adj_price, price, price_contract, carry, carry_contract
"""
import argparse
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent


def to_daily(frame: pd.DataFrame, value_cols: dict) -> pd.DataFrame:
    f = frame.copy()
    ts = f["DATETIME"].dt.tz_localize("UTC").dt.tz_convert("America/New_York")
    f["ny_date"] = ts.dt.tz_localize(None).dt.normalize()
    f["ny_minutes"] = ts.dt.hour * 60 + ts.dt.minute
    # Era detection: rows before the first day with >= 4 bars are daily settlements (stamped 23:00 UTC) and are kept as-is;
    # in the hourly era keep only bars at or before 16:15 New York time.
    per_day = f.groupby("ny_date").size()
    hourly_days = per_day[per_day >= 4]
    era_start = hourly_days.index.min() if len(hourly_days) else None
    if era_start is not None:
        f = f[(f["ny_date"] < era_start) | (f["ny_minutes"] <= 16 * 60 + 15)]
    return f.groupby("ny_date").agg(**{k: (v, "last") for k, v in value_cols.items()})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--symbols", nargs="*", default=["SP500", "NASDAQ", "FED", "SOFR", "VIX"])
    a = ap.parse_args()
    src = Path(a.src)
    for sym in a.symbols:
        adj = pd.read_csv(src / "adjusted_prices_csv" / f"{sym}.csv", parse_dates=["DATETIME"]).dropna()
        mult = pd.read_csv(src / "multiple_prices_csv" / f"{sym}.csv", parse_dates=["DATETIME"])
        ad = to_daily(adj, {"adj_price": "price"})
        md = to_daily(mult, {"price": "PRICE", "price_contract": "PRICE_CONTRACT", "carry": "CARRY", "carry_contract": "CARRY_CONTRACT"})
        out = ad.join(md, how="left")
        out.index.name = "date"
        out.to_csv(HERE / "raw" / f"pysystemtrade_{sym}_daily.csv", float_format="%.6f")
        print(sym, len(out), out.index.min().date(), out.index.max().date())


if __name__ == "__main__":
    main()
