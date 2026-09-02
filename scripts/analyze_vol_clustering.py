"""Atlas 5.1 — FS-U1/FS-U2: monthly vol clustering on the vaulted library (pre-registered).

Ledger 2026-09-02. Demonstration trials (framing pre-stated in the ledger): Ljung-Box on
|returns| lags 1-6 + lag-1 ACF sign, monthly resolution, two assets. Ljung-Box implemented
directly (statsmodels not installed in this environment): Q = n(n+2) sum rho_k^2/(n-k),
chi-square with h dof.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1] / "ingest" / "vault"


def acf(x, k):
    x = np.asarray(x, float)
    x = x - x.mean()
    return float(np.sum(x[k:] * x[:-k]) / np.sum(x * x))


def ljung_box(x, h=6):
    n = len(x)
    q = n * (n + 2) * sum(acf(x, k) ** 2 / (n - k) for k in range(1, h + 1))
    return q, float(stats.chi2.sf(q, h))


def run(name, ret):
    a = pd.Series(ret).dropna().abs().values
    q, p = ljung_box(a, 6)
    acs = [round(acf(a, k), 3) for k in range(1, 7)]
    verdict = "PASS" if (p < 0.05 and acs[0] > 0) else "FAIL"
    print(f"{name}: n={len(a)}  |ret| ACF(1..6)={acs}  LB(6) Q={q:.1f} p={p:.2e}  -> {verdict}")


mf = pd.read_csv(ROOT / "factors" / "iima_monthly_factors.csv")["MF"]
run("FS-U1 India MF (monthly, 1993-2025)", mf)

g = pd.read_csv(ROOT / "commodities" / "gold_monthly_1833_2026.csv")
g["Date"] = pd.to_datetime(g["Date"], format="%Y-%m")
g = g[g["Date"] >= "1972-01-01"]
run("FS-U2 gold float era (monthly, 1972-2026)", np.log(g["Price"]).diff() * 100)
