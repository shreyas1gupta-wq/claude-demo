"""Landing kit for the India fundamentals handoff (see
research/register/handoff-prompt-india-fundamentals.md for the schemas P1-P6).

Usage: PYTHONPATH=<repo> python3 ingest/receive_india_fundamentals.py <dropdir>

Validates the delivered files STRUCTURALLY (schema, spans, the handoff's own
self-checks), prints a pass/fail report, and emits a draft AUTHENTICATION.md
(pass-1 anchors) to <dropdir>/AUTHENTICATION.draft.md. It does NOT move files into
the vault and does NOT check values against filed PDFs — the two-pass rule stands:
the desk commits the anchors first, then verifies values, then vaults with
ingest/manifest.py. Nothing here computes returns or signals (register discipline).
"""
import sys
from pathlib import Path

import pandas as pd

REQ = {
    "fundamentals_quarterly.csv": ["isin", "ticker", "fiscal_quarter_end", "filing_date",
                                    "total_assets", "total_equity", "total_debt",
                                    "cash_and_equivalents", "revenue", "net_income",
                                    "cfo", "shares_outstanding", "source_url"],
    "index_membership.csv": ["index", "isin", "effective_date", "action", "source_url"],
    "delisted_registry.csv": ["isin", "last_trading_date", "reason", "source_url"],
    "prices_daily.csv.gz": ["date", "isin", "close_unadjusted", "close_adjusted", "volume"],
    "corporate_actions.csv": ["isin", "ex_date", "type", "source_url"],
    "shareholding_pledge.csv": ["isin", "quarter_end", "filing_date", "promoter_pct",
                                 "promoter_pledged_pct_of_promoter_holding", "source_url"],
}
OPTIONAL = {"nse_strategy_indices_tr.csv": ["date", "index_name", "tr_level"]}


def main(drop):
    drop = Path(drop)
    report, anchors = [], []
    ok_all = True
    for fname, cols in {**REQ, **OPTIONAL}.items():
        f = drop / fname
        optional = fname in OPTIONAL
        if not f.exists():
            report.append(f"{'MISSING (optional)' if optional else 'MISSING (REQUIRED)'}: {fname}")
            ok_all = ok_all and optional
            continue
        df = pd.read_csv(f, nrows=500000, low_memory=False)
        missing = [c for c in cols if c not in df.columns]
        if missing:
            report.append(f"FAIL {fname}: missing columns {missing}")
            ok_all = False
            continue
        report.append(f"ok   {fname}: {len(df):,} rows (first 500k), cols complete")
        anchors.append(f"- {fname}: rows>= {len(df):,}; required columns present.")
    # handoff self-checks (structural side)
    fq = drop / "fundamentals_quarterly.csv"
    if fq.exists():
        df = pd.read_csv(fq, usecols=["fiscal_quarter_end", "filing_date"],
                         parse_dates=["fiscal_quarter_end", "filing_date"])
        lag_ok = (df.filing_date > df.fiscal_quarter_end).mean()
        med_lag = (df.filing_date - df.fiscal_quarter_end).dt.days.median()
        report.append(f"self-check filing lag: filing>quarter-end on {100*lag_ok:.1f}% "
                      f"(bar >99%), median lag {med_lag:.0f}d (expect 30-45)")
        anchors.append(f"- filing-lag: {100*lag_ok:.1f}% positive, median {med_lag:.0f}d "
                       f"-> {'PASS' if lag_ok >= 0.99 else 'FAIL — interrogate before vaulting'}")
        ok_all = ok_all and lag_ok >= 0.99
    dl = drop / "delisted_registry.csv"
    if dl.exists():
        d = pd.read_csv(dl, parse_dates=["last_trading_date"])
        by_year = d.last_trading_date.dt.year.value_counts().sort_index()
        empty = [y for y in range(2015, 2026) if by_year.get(y, 0) == 0]
        report.append(f"self-check delistings by year: {dict(by_year)}; empty years: {empty or 'none'}")
        anchors.append(f"- delisted registry: {len(d)} names; empty years {empty or 'none'} "
                       f"-> {'PASS' if not empty else 'GAP — interrogate'}")
        ok_all = ok_all and not empty
    print("\n".join(report))
    print(f"\nSTRUCTURAL VERDICT: {'PASS — proceed to two-pass AUTH' if ok_all else 'FAIL — return to the data builder with this report'}")
    draft = (drop / "AUTHENTICATION.draft.md")
    draft.write_text("# AUTHENTICATION draft (pass-1 anchors) — india_fundamentals\n"
                     "Commit these anchors BEFORE any value check (near-miss #4 rule).\n\n"
                     "## PASS 1 anchors (structural, from receive_india_fundamentals.py)\n"
                     + "\n".join(anchors) +
                     "\n\n## PASS 2 value checks to run AFTER committing this file\n"
                     "- Spot-verify 5 large names (Reliance/TCS/HDFC Bank/Infosys/ITC), one recent\n"
                     "  + one 2016 quarter, against the as-filed PDFs the source_url column cites.\n"
                     "- Reproduce one published NIFTY 500 reconstitution from index_membership.csv.\n"
                     "- Cross-check prices_daily vs the vaulted nifty50 series on 5 overlap dates.\n")
    print(f"anchors draft written: {draft}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
