#!/usr/bin/env python3
"""Atlas 3.7 — PL1, PRE-REGISTERED measurement: does the pre-election window's sign predict
the result month's sign? (n=8; L5's 'direction is surprise' predicts ~coin-flip.)"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "cycles" / "political-close" / "political-RESULTS.md"
ELECTIONS = ["1996-05", "1998-03", "1999-10", "2004-05", "2009-05", "2014-05", "2019-05", "2024-06"]


def main() -> int:
    f = pd.read_csv(ROOT / "ingest/vault/factors/iima_monthly_factors.csv",
                    na_values=["NA"]).set_index("Date")
    mf = f.MF.astype(float).dropna()
    idx = list(mf.index)
    rows, agree = [], 0
    for e in ELECTIONS:
        i = idx.index(e)
        pre = float(mf.iloc[i - 2:i].mean())
        res = float(mf.loc[e])
        ok = np.sign(pre) == np.sign(res)
        agree += ok
        rows.append((e, pre, res, "same" if ok else "FLIP"))
    res_md = [
        "# Atlas 3.7 — direction-is-surprise, formalized (PL1, pre-registered measurement)", "",
        "| Election | pre-window mean %/m (2m) | result month % | sign |", "|---|---|---|---|",
        *[f"| {e} | {p:+.1f} | {r:+.1f} | {s} |" for e, p, r, s in rows],
        "",
        f"- Sign agreement: **{agree}/8** — L5's 'direction is surprise' predicted ~coin-flip;",
        "  measurement recorded, no bar (n=8).", "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(res_md) + "\n")
    print(f"PL1: sign agreement {agree}/8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
