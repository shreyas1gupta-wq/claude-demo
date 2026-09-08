"""SW2-A1 — the idle-cash accounting correction (one-shot). Registered 2026-09-08
BEFORE this run; frozen spec adopted verbatim from the SW-2 synthesis (f15 audit).

Credit rate 4.0%/yr on CORE_W x (1-expo.shift(1))+ (the engine's own lagged deployment
series), R/252 day-count, via run_book's extra_ret hook. Acceptance: bit-for-bit vs
f15's liquid_fund_4pct cell (CAGR 11.456, maxDD -11.3644) -> adopted as the corrected
baseline. c2: the 6%-repo footnote. c3: peak-margin re-read INCLUDING the missing
factor-sleeve margin line, both treatments (hedged 2.5% / unhedged 10% on gross)
printed as declared bounds. Prints only.
"""
import pandas as pd

_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
run_book, stats_of, core_stream = _g["run_book"], _g["stats_of"], _g["core_stream"]
dates, D0, D1 = _g["dates"], _g["D0"], _g["D1"]

CORE_W, SW_W, FAC_W, CAP = 0.65, 0.20, 0.15, 1.5

# the f15 credit-stream construction, verbatim
_, expo_full = core_stream(CAP, financing=True)
expo = expo_full.reindex(dates).ffill()
idle_book = CORE_W * (1 - expo.shift(1)).clip(lower=0)


def credit(rate):
    return (idle_book * (rate / 252.0)).fillna(0.0)


print(f"SW2-A1 — IDLE-CASH ACCOUNTING CORRECTION, {D0.date()}..{D1.date()}:")

# c1: baseline repro + credited-4% acceptance
eq0, pm0 = run_book(CORE_W, SW_W, FAC_W, cap=CAP, financing=True, syn_margin=True)
c0, d0_, y0 = stats_of(eq0)
eq4, pm4 = run_book(CORE_W, SW_W, FAC_W, cap=CAP, financing=True, syn_margin=True,
                    extra_ret=credit(0.04))
c4, d4, y4 = stats_of(eq4)
ok = (round(c4, 3) == 11.456) and (round(d4, 4) == -11.3644)
h1, h2 = eq4.loc[:"2016-12-31"], eq4.loc["2017-01-01":]
e1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
e2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)
print(f"  c1 baseline repro: {c0:+.4f}/{d0_:.4f} (a5 booked +11.13/-11.53) | "
      f"credited@4%: CAGR {c4:+.4f} (TR ~{c4 + 1.3:+.2f}) maxDD {d4:.4f} | "
      f"acceptance vs f15 (11.456/-11.3644): {'PASS — ADOPTED as corrected baseline' if ok else 'FAIL'}")
print(f"     worst yr {100 * y4.min():+.2f} ({y4.idxmin().year}) | eras {e1:+.2f}/{e2:+.2f} | "
      f"dCAGR {c4 - c0:+.4f}pp, dDD {d4 - d0_:+.4f}pp")

# c2: the 6%-repo footnote
eq6, _ = run_book(CORE_W, SW_W, FAC_W, cap=CAP, financing=True, syn_margin=True,
                  extra_ret=credit(0.06))
c6, d6, _ = stats_of(eq6)
print(f"  c2 footnote @6% repo: CAGR {c6:+.4f} (TR ~{c6 + 1.3:+.2f}) maxDD {d6:.4f} "
      f"(add {c6 - c0:+.4f}pp) — linear-rescale rule stands when funding_rate is set")

# c3: peak-margin re-read incl. the factor-sleeve margin line (declared bounds)
_, pm_h = run_book(CORE_W, SW_W, FAC_W, cap=CAP, financing=True, syn_margin=True,
                   extra_ret=credit(0.04), fac_margin_rate=0.025)
_, pm_u = run_book(CORE_W, SW_W, FAC_W, cap=CAP, financing=True, syn_margin=True,
                   extra_ret=credit(0.04), fac_margin_rate=0.10)
print(f"  c3 peak margin re-read: ex-factor {100 * pm4:.1f}% (as booked); incl. factor gross "
      f"@2.5% hedged {100 * pm_h:.1f}% | @10% unhedged {100 * pm_u:.1f}% — bounds pending a "
      f"principal convention on long-short SLB margin; all < the 30% feasibility prior")
