"""f05_factor_extensions — STRATEGY SWEEP 2, family f05_factor_extensions.
Registered 2026-09-08 BEFORE this run. PRE-REGISTRATION (bars fixed before any number
printed):

  Current sleeve (OP-D6b/OP-D7 frozen spec): combo = 0.5*WML + 0.5*HML (equal weight,
  IIMA monthly, %), EWMA(lambda=0.94) vol-targeted to 15%, cap 2.0x, both lagged one
  month (flev = (target/fvol).clip(upper=cap).shift(1)) — book weight 15% of NAV.

  Variants under test, ALL against the house no-lookahead convention (expanding/EWMA
  vol computed from data through t, sizing signal shifted 1 month before being applied
  to month t's return — matches quant convention already in scripts/analyze_op_d6b.py):
    (a) combo_smb  : equal-thirds (WML+HML+SMB)/3
    (b) combo_rp   : risk-parity — inverse-EXPANDING-vol weights on WML/HML separately
                     (min_obs=24m, weights shifted 1 month; equal-weight fallback during
                     warm-up), then combined
    (c) vol target : 12% / 15% / 18% (sleeve-level EWMA target)
    (d) cap        : 1.5x / 2.0x

  BARS (pre-registered, sleeve standalone, primary window D0..D1 = the standing book's
  eval window 2011-07-01..2023-03-31, full-period):
    B1 (promote combo change):  full-period Sharpe improves by >= 0.10 over the current
        combo AT THE SAME (target,cap)=(0.15,2.0) AND does not worsen maxDD by more than
        3pp, AND does not raise |corr to book core| by more than 0.10 in absolute value
        (a correlated "diversifier" that stops diversifying is not free).
    B2 (promote sizing change): full-period Sharpe improves by >= 0.05 over (15%,2.0x)
        at the SAME combo, with maxDD not worse by more than 2pp.
    B3 (book-level, decisive): the frozen recommended sleeve must raise the STANDING
        BOOK's full-period CAGR (run_book, fac_w=0.15, cap=1.5, financing=True,
        syn_margin=True — the OP-D6b a5 "honest baseline" convention) by a POSITIVE
        amount net of a 30%-of-mean haircut (OP-D7's own haircut convention) and must
        not worsen book maxDD by more than 1pp. Missing B3 sends the family to "keep
        current" regardless of standalone sleeve prints (a sleeve-level Sharpe gain
        that doesn't survive to the book, or doesn't survive the haircut, is not
        promotable — CONTRACT §5, decay assumption).
  Interpretation is written AFTER the prints below (process note #5 / CONTRACT rules
  for research agents).

No lookahead: every vol estimate is expanding or EWMA (both start-of-history, causal by
construction) and every sizing signal is .shift(1)'d before being multiplied onto the
return it sizes. Risk-parity weights are the SAME pattern. Verified against the engine's
own baseline (assertion below) before any variant print.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

# Reuse the book engine verbatim (house pattern, per CLAUDE.md process note #6 / task brief)
_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)  # noqa: S102 (trusted local file, house pattern)
ii = _g["ii"]
D0, D1 = _g["D0"], _g["D1"]
core_stream = _g["core_stream"]
run_book = _g["run_book"]
stats_of = _g["stats_of"]
fac_vm_baseline = _g["fac_vm"]  # engine's own current-design sleeve, for the sanity check

ERA_SPLIT = pd.Timestamp("2017-01-01")  # same split OP-D6b/D7 use throughout


def cagr_vol_sharpe_dd(m):
    """m: monthly return series (decimal). Returns (CAGR%, vol%/yr, Sharpe, maxDD%)."""
    m = m.dropna()
    if len(m) < 6:
        return (np.nan,) * 4
    eq = (1 + m).cumprod()
    yrs = len(m) / 12
    cagr = 100 * (eq.iloc[-1] ** (1 / yrs) - 1)
    vol = 100 * m.std() * np.sqrt(12)
    sharpe = (m.mean() * 12) / (m.std() * np.sqrt(12)) if m.std() > 0 else np.nan
    dd = 100 * (eq / eq.cummax() - 1).min()
    return cagr, vol, sharpe, dd


def expanding_vol_shift1(x, min_obs=24):
    """Expanding std, causal (uses data through row t inclusive), then shift(1) so the
    SIZE/WEIGHT applied at t only knows data through t-1. No lookahead by construction."""
    return x.expanding(min_periods=min_obs).std().shift(1)


# ---------------------------------------------------------------------------
# 1. Build the three combos on the full IIMA history (1993-10..2025-12), monthly
# ---------------------------------------------------------------------------
F = pd.DataFrame({
    "WML": ii["WML"] / 100,
    "HML": ii["HML"] / 100,
    "SMB": ii["SMB"] / 100,
}).dropna()

combo_base = 0.5 * F["WML"] + 0.5 * F["HML"]

combo_smb = (F["WML"] + F["HML"] + F["SMB"]) / 3

vol_wml = expanding_vol_shift1(F["WML"])
vol_hml = expanding_vol_shift1(F["HML"])
inv_w, inv_h = 1 / vol_wml, 1 / vol_hml
w_wml = (inv_w / (inv_w + inv_h)).fillna(0.5)  # equal-weight fallback pre-warm-up
w_hml = (inv_h / (inv_w + inv_h)).fillna(0.5)
combo_rp = w_wml * F["WML"] + w_hml * F["HML"]

COMBOS = {"base_5050_WML_HML": combo_base, "smb_equal_thirds": combo_smb,
          "risk_parity_WML_HML": combo_rp}

# ---------------------------------------------------------------------------
# 2. Sanity check: my re-implementation of the CURRENT design must reproduce the
#    engine's own fac_vm (imported from analyze_op_d6b.py) — proves no drift/bug
#    before any new variant is trusted.
# ---------------------------------------------------------------------------


def size_combo(combo, target, cap):
    fvol = combo.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(12)
    flev = (target / fvol).clip(upper=cap).shift(1)
    return (flev * combo).dropna()


mine_current = size_combo(combo_base, 0.15, 2.0)
common_idx = mine_current.index.intersection(fac_vm_baseline.index)
diff = (mine_current.loc[common_idx] - fac_vm_baseline.loc[common_idx]).abs().max()
assert diff < 1e-9, f"sanity check FAILED: reimplementation diverges from engine by {diff}"
print(f"[sanity] reimplementation of current design matches engine fac_vm exactly "
      f"(max abs diff {diff:.2e}) over {len(common_idx)} months\n")

# ---------------------------------------------------------------------------
# 3. Book core (for correlation), monthly, over the standing eval window
# ---------------------------------------------------------------------------
core_ret_d, _ = core_stream(1.5, True)  # the standing book's actual core config (cap 1.5x, financed)
core_m = (1 + core_ret_d).resample("ME").prod() - 1
core_m = core_m.loc[D0:D1]

# ---------------------------------------------------------------------------
# 4. The grid: 3 combos x 3 vol targets x 2 caps = 18 standalone sleeve cells
# ---------------------------------------------------------------------------
TARGETS = [0.12, 0.15, 0.18]
CAPS = [1.5, 2.0]
cells = []
print("Standalone sleeve grid (monthly, window %s..%s), 18 cells:" % (D0.date(), D1.date()))
print(f"{'combo':<22}{'tgt':>5}{'cap':>5} | {'CAGR':>7}{'vol':>7}{'Shrp':>7}{'maxDD':>8} | "
      f"{'CAGR_e1':>8}{'CAGR_e2':>8}{'DD_e1':>7}{'DD_e2':>7} | {'corr_core':>10}")
for cname, combo in COMBOS.items():
    for tgt in TARGETS:
        for cap in CAPS:
            sized = size_combo(combo, tgt, cap)
            win = sized.loc[D0:D1]
            cagr, vol, sharpe, dd = cagr_vol_sharpe_dd(win)
            e1 = win.loc[:ERA_SPLIT - pd.Timedelta(days=1)]
            e2 = win.loc[ERA_SPLIT:]
            c1, _, _, d1 = cagr_vol_sharpe_dd(e1)
            c2, _, _, d2 = cagr_vol_sharpe_dd(e2)
            aligned = pd.concat([win, core_m], axis=1, join="inner").dropna()
            corr = aligned.iloc[:, 0].corr(aligned.iloc[:, 1]) if len(aligned) > 6 else np.nan
            cell = dict(combo=cname, target=tgt, cap=cap, cagr=cagr, vol=vol, sharpe=sharpe,
                        maxdd=dd, cagr_era1=c1, cagr_era2=c2, dd_era1=d1, dd_era2=d2,
                        corr_to_core=corr, n_months=len(win))
            cells.append(cell)
            tag = f"{cname:<22}{tgt:>5.2f}{cap:>5.1f}"
            print(f"{tag} | {cagr:7.2f}{vol:7.2f}{sharpe:7.2f}{dd:8.2f} | "
                  f"{c1:8.2f}{c2:8.2f}{d1:7.2f}{d2:7.2f} | {corr:10.3f}")

CELLS_STANDALONE = len(cells)
print(f"\n{CELLS_STANDALONE} standalone cells computed.\n")

# ---------------------------------------------------------------------------
# 5. Bar checks (pre-registered B1, B2) against the exact current design
# ---------------------------------------------------------------------------
by_key = {(c["combo"], c["target"], c["cap"]): c for c in cells}
cur = by_key[("base_5050_WML_HML", 0.15, 2.0)]
print(f"CURRENT design (base 50/50, tgt15/cap2.0): CAGR {cur['cagr']:+.2f} vol {cur['vol']:.2f} "
      f"Sharpe {cur['sharpe']:.2f} maxDD {cur['maxdd']:.2f} corr_core {cur['corr_to_core']:+.3f}\n")

b1_results = {}
for cname in ("smb_equal_thirds", "risk_parity_WML_HML"):
    v = by_key[(cname, 0.15, 2.0)]
    d_sharpe = v["sharpe"] - cur["sharpe"]
    d_dd = v["maxdd"] - cur["maxdd"]  # both negative numbers; "worse" = more negative
    d_corr = abs(v["corr_to_core"]) - abs(cur["corr_to_core"])
    passed = (d_sharpe >= 0.10) and (d_dd >= -3.0) and (d_corr <= 0.10)
    b1_results[cname] = dict(d_sharpe=d_sharpe, d_dd=d_dd, d_corr=d_corr, bar="PASS" if passed else "MISS")
    print(f"B1 [{cname} @ tgt15/cap2.0 vs current]: dSharpe {d_sharpe:+.3f} (bar>=+0.10), "
          f"dMaxDD {d_dd:+.2f}pp (bar>=-3.0), d|corr| {d_corr:+.3f} (bar<=+0.10) -> {b1_results[cname]['bar']}")

b2_results = {}
for tgt, cap in [(0.12, 2.0), (0.18, 2.0), (0.15, 1.5), (0.12, 1.5), (0.18, 1.5)]:
    v = by_key[("base_5050_WML_HML", tgt, cap)]
    d_sharpe = v["sharpe"] - cur["sharpe"]
    d_dd = v["maxdd"] - cur["maxdd"]
    passed = (d_sharpe >= 0.05) and (d_dd >= -2.0)
    key = f"base_tgt{tgt}_cap{cap}"
    b2_results[key] = dict(d_sharpe=d_sharpe, d_dd=d_dd, bar="PASS" if passed else "MISS")
    print(f"B2 [{key} vs current]: dSharpe {d_sharpe:+.3f} (bar>=+0.05), dMaxDD {d_dd:+.2f}pp "
          f"(bar>=-2.0) -> {b2_results[key]['bar']}")

# Best standalone Sharpe overall (for reporting only; promotion still gated on B1-B3)
best_cell = max(cells, key=lambda c: c["sharpe"])
print(f"\nBest standalone Sharpe overall: {best_cell['combo']} tgt{best_cell['target']} "
      f"cap{best_cell['cap']} -> Sharpe {best_cell['sharpe']:.2f} CAGR {best_cell['cagr']:+.2f} "
      f"maxDD {best_cell['maxdd']:.2f}")

# ---------------------------------------------------------------------------
# 6. Book-level test (B3, decisive): does ANY candidate clearing B1/B2 move the
#    STANDING BOOK (fac_w=0.15, honest-baseline convention) net of a 30%-mean haircut?
#    Candidates entering this stage: current design (validation) + the best B1/B2
#    passer if any, else the single best-Sharpe standalone variant (for information
#    only, since it does not clear a promotion bar on its own).
# ---------------------------------------------------------------------------
candidates_for_book = [("current", "base_5050_WML_HML", 0.15, 2.0)]
any_b1_pass = [k for k, v in b1_results.items() if v["bar"] == "PASS"]
any_b2_pass = [k for k, v in b2_results.items() if v["bar"] == "PASS"]
if any_b1_pass:
    for k in any_b1_pass:
        candidates_for_book.append((f"B1pass_{k}", k, 0.15, 2.0))
if any_b2_pass:
    for k in any_b2_pass:
        tgt, cap = float(k.split("_tgt")[1].split("_cap")[0]), float(k.split("_cap")[1])
        candidates_for_book.append((f"B2pass_{k}", "base_5050_WML_HML", tgt, cap))
if not any_b1_pass and not any_b2_pass:
    candidates_for_book.append(("info_only_best_sharpe", best_cell["combo"], best_cell["target"], best_cell["cap"]))

print(f"\nBook-level cells (fac_w=0.15, cap=1.5 core, financed, syn_margin — OP-D6b a5 convention), "
      f"D0..D1 full period, candidates: {[c[0] for c in candidates_for_book]}\n")

book_results = {}
for label, cname, tgt, cap in candidates_for_book:
    sized = size_combo(COMBOS[cname], tgt, cap)
    mu = sized.loc[D0:D1].mean()
    eq, pm = run_book(0.65, 0.20, 0.15, cap=1.5, financing=True, syn_margin=True, fac_monthly=sized)
    c, d, y = stats_of(eq)
    eq_h, _ = run_book(0.65, 0.20, 0.15, cap=1.5, financing=True, syn_margin=True,
                        fac_monthly=sized - 0.30 * mu)  # OP-D7's own 30%-of-mean haircut convention
    ch, dh, yh = stats_of(eq_h)
    book_results[label] = dict(combo=cname, target=tgt, cap=cap, book_cagr=c, book_dd=d,
                                book_worst_yr=100 * y.min(), book_cagr_haircut=ch, book_dd_haircut=dh,
                                peak_margin=pm)
    print(f"  {label:<28} combo={cname} tgt={tgt} cap={cap} | book CAGR {c:+.2f} maxDD {d:.2f} "
          f"worst-yr {100*y.min():+.1f} | HAIRCUT-30%: CAGR {ch:+.2f} maxDD {dh:.2f} | peak margin {100*pm:.1f}%")

CELLS_BOOK = len(candidates_for_book) * 2  # each candidate = 1 book run + 1 haircut run
cur_book = book_results["current"]
print(f"\nCurrent-design book reproduction check: CAGR {cur_book['book_cagr']:+.2f} "
      f"(OP-D6b a5 printed +11.13) maxDD {cur_book['book_dd']:.2f} (printed -11.53) — "
      f"{'MATCHES' if abs(cur_book['book_cagr']-11.13) < 0.05 and abs(cur_book['book_dd']-(-11.53)) < 0.05 else 'DIVERGES — investigate'}")

# ---------------------------------------------------------------------------
# 7. B3 verdict + final recommendation
# ---------------------------------------------------------------------------
promotable = None
for label in book_results:
    if label == "current" or label.startswith("info_only"):
        continue
    r = book_results[label]
    d_cagr = r["book_cagr_haircut"] - cur_book["book_cagr"]  # vs current's un-haircut book (conservative: any candidate must beat current's ACTUAL printed number even after ITS OWN haircut)
    d_dd = r["book_dd_haircut"] - cur_book["book_dd"]
    b3_pass = (d_cagr > 0) and (d_dd >= -1.0)
    print(f"\nB3 [{label}]: haircut book CAGR {r['book_cagr_haircut']:+.2f} vs current {cur_book['book_cagr']:+.2f} "
          f"(d={d_cagr:+.2f}pp, bar>0) | haircut maxDD {r['book_dd_haircut']:.2f} vs current {cur_book['book_dd']:.2f} "
          f"(d={d_dd:+.2f}pp, bar>=-1.0) -> {'PASS' if b3_pass else 'MISS'}")
    if b3_pass and promotable is None:
        promotable = label

print("\n" + "=" * 70)
if promotable:
    r = book_results[promotable]
    print(f"VERDICT: PROMOTE {promotable} (combo={r['combo']}, target={r['target']}, cap={r['cap']}) "
          f"— clears B1/B2 standalone AND B3 book-level net of the 30% haircut.")
else:
    print("VERDICT: KEEP CURRENT (base 50/50 WML+HML, EWMA target 15%, cap 2.0x). "
          "No variant cleared the full B1/B2 (standalone) -> B3 (book, post-haircut) chain.")
print("=" * 70)

TOTAL_CELLS = CELLS_STANDALONE + CELLS_BOOK
print(f"\nTotal cells consumed: {CELLS_STANDALONE} standalone grid + {CELLS_BOOK} book-level "
      f"(book+haircut per candidate) = {TOTAL_CELLS}")

# ---------------------------------------------------------------------------
# 8. Dump JSON
# ---------------------------------------------------------------------------
import json  # noqa: E402

out = dict(
    family="f05_factor_extensions",
    window=[str(D0.date()), str(D1.date())],
    era_split=str(ERA_SPLIT.date()),
    sanity_check_max_abs_diff=float(diff),
    standalone_grid=cells,
    current_design=cur,
    b1_bar_checks=b1_results,
    b2_bar_checks=b2_results,
    best_standalone_by_sharpe=best_cell,
    book_level_results=book_results,
    book_reproduction_check=dict(
        cagr=cur_book["book_cagr"], dd=cur_book["book_dd"],
        printed_cagr=11.13, printed_dd=-11.53,
        matches=bool(abs(cur_book["book_cagr"] - 11.13) < 0.05 and abs(cur_book["book_dd"] - (-11.53)) < 0.05),
    ),
    verdict="promote" if promotable else "keep_current",
    promoted_key=promotable,
    cells_consumed=TOTAL_CELLS,
)
with open("/home/user/claude-demo/research/opt_sweep2/f05_factor_extensions.json", "w") as f:
    json.dump(out, f, indent=2, default=str)
print("\nJSON written to research/opt_sweep2/f05_factor_extensions.json")
