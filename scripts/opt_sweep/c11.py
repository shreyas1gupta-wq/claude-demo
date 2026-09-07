"""OP-D2 combiner c11 — the risk-limit table.

Pure derivation from ALREADY-PRINTED desk numbers (no new data touched), per the
chapter-agent rule: every input below cites the family JSON it was printed in.

Inputs (all from research/opt_sweep/f*.json, verified board 2026-09-07):
  f15  maxloss ~8.6-9.0x credit (7d midVIX); gapped stop exit mean 2.9x credit vs 2x stop;
       P(gap-through)/day midVIX 0.55% (7d) / 0.00% (30d); 30d credit @VIX18 = 0.85 %S.
  f16  stop-2x MISS (46.0% cut @32.2% cost); delta-band roll |d|>=0.30 max 3 rolls:
       35.5% cut @9.6% cost, p5 -1.044 %S vs hold p5 -2.528 %S, worst -2.570 vs -3.984 %S.
  f17  weekly full-margin compounding = RUIN (one -100% week, Budget 2016-02-29);
       monthly +13.96%/yr geo; daily close-stop can't cap gap weeks (-100%->-93.3% only).
  f18  DD-constrained f (P(book maxDD>10%)<=1%/yr): mo hold 0.165 / mo stop2x 0.200 /
       wk 0.035-0.040; iid bootstrap understates clustering => these are UPPER bounds;
       F16 worst month -30.6% of margin (COVID).
  f14  VIX spike half-life median 2d (MISS vs 15-40d bar); re-enter <60th pct median 29d.
  f20  L2 stress-flag pct>=0.90: tail trim +46.6% @ +9.7% cost (PASS/PASS; PARTIAL —
       effective n=1-2 events, treat as cheap insurance, not broad protection).
  f04  GARCH & EWMA onset lag 72-74 vol pts (Mar-2020); f05 vol-target sizing MISS
       (worst-month +5.77% only) => ex-ante vol forecasts CANNOT set the limits.
  f19  budget-window |ret| 0.95% vs 0.59%, p=0.0049 (return leg; per verifier this
       corroborates CW-D1a, NOT CW-D1v). f17's ruin week was a Budget week.
  CONTRACT.md: gross leverage <=1.5x (delta-adjusted options count); drawdown binding.
  f13 REFUTED (groupby.first leak) => IV-HV-spread-quintile gating is EXCLUDED here.
"""

# ---- printed desk numbers (cited above) ----
MAXLOSS_X_CREDIT = 9.0        # f15 upper end of 8.6-9.0x (7d midVIX)
GAP_MEAN_X_CREDIT = 2.9       # f15 mean 1d loss when gapped vs the 2x stop
P_GAP_7D, P_GAP_30D = 0.0055, 0.0000   # f15 midVIX
DD_CEILING = 0.10             # f18 registered constraint P(book maxDD>10%)<=1%/yr
F_MO_HOLD, F_MO_STOP, F_WK = 0.165, 0.200, 0.035   # f18 dd-constrained f (upper bounds)
WORST_MO_PCT_MARGIN = 0.306   # f18: F16 worst month -30.6% of margin (COVID)
WORST_WK_PCT_MARGIN = 1.00    # f17: -100% week (Budget 2016-02-29)
REENTRY_DAYS = 29             # f14 median days to re-enter <60th pct
HALF_LIFE_D = 2               # f14 median spike half-life (why NOT to re-enter on snapback)

print("=== c11 risk-limit table (derived) ===")

# 1) Margin cap. f18's measured caps are upper bounds (iid caveat); the binding hard cap
#    is structural: a full-margin wipe is a measured event at WEEKLY tenor (f17 -100%),
#    so cap margin such that even a 100%-of-margin loss cannot alone breach the 10% DD.
mo_margin_cap = min(F_MO_HOLD, DD_CEILING)
wk_margin_cap = min(F_WK, DD_CEILING)
print(f"1. margin cap: monthly f<={mo_margin_cap:.3f} book "
      f"(= min(f18 0.165, structural 0.10)); weekly f<={wk_margin_cap:.3f} (f18 0.035)")

# 2) Max premium at risk per cycle: maxloss ~9x credit (f15) => premium sold such that
#    a full wing breach = the DD ceiling at most.
prem_cap = DD_CEILING / MAXLOSS_X_CREDIT
print(f"2. max premium at risk/cycle: {prem_cap*100:.2f}% of book "
      f"(10% DD ceiling / f15 maxloss {MAXLOSS_X_CREDIT:.1f}x credit)")

# 3) Max structural loss per book (defined-risk wings mandatory: f17 shows undefined
#    weekly risk = RUIN):
print(f"3. max structural loss/book: monthly {mo_margin_cap*100:.1f}% (=margin cap; "
      f"full wing breach); measured-worst at cap = {mo_margin_cap*WORST_MO_PCT_MARGIN*100:.2f}% "
      f"book (f18 -30.6% margin COVID); weekly {wk_margin_cap*WORST_WK_PCT_MARGIN*100:.1f}% book "
      f"(f17 -100% wk at f=0.035)")

# 4) Daily loss stop: stop-2x MISSED its bar (f16) and gaps fill ~2.9x (f15), so the
#    per-position rule is the delta-band roll; the book-level stop budgets the gap fill.
daily_stop_set = 2.0 * prem_cap    # the level you set
daily_stop_real = GAP_MEAN_X_CREDIT * prem_cap  # what a gap day actually costs (mean)
print(f"4. daily loss stop (book): set at -{daily_stop_set*100:.2f}% "
      f"(2x premium outstanding); BUDGET the realized gap fill at "
      f"-{daily_stop_real*100:.2f}% mean (f15 2.9x), tail to -{prem_cap*MAXLOSS_X_CREDIT*100:.1f}% "
      f"(=margin); P(gap-through)/day midVIX {P_GAP_7D*100:.2f}% (7d) / {P_GAP_30D*100:.2f}% (30d)")
p5_impr = (2.528 - 1.044) / 2.528 * 100
print(f"   per-position management: |delta|>=0.30 roll, max 3 (f16: p5 -1.044 vs hold "
      f"-2.528 %S = {p5_impr:.0f}% p5 improvement at 9.6% cost) — NOT the 2x hard stop (MISS)")

# 5) DD governor (f18 constraint + iid-understatement caveat => act before the ceiling):
print(f"5. DD governor: sleeve maxDD budget 10% @ <=1%/yr (f18 registered constraint); "
      f"HALVE size at -5% sleeve DD, FLAT at -10%; f18 caps are upper bounds (iid "
      f"bootstrap understates clustering), so no discretionary override upward")

# 6) Re-entry rules:
print(f"6. re-entry: after stress stand-down (f20 pct>=0.90 flag), re-enter only when the "
      f"rank falls <60th pct — median {REENTRY_DAYS} trading days (f14); NEVER on the VIX "
      f"snapback itself (median half-life {HALF_LIFE_D}d, f14 MISS); after a -10% flat, "
      f"re-enter at half size for one full cycle; no fresh WEEKLY premium into Budget "
      f"windows (f19 |ret| 0.95 vs 0.59%, p=0.0049; f17's -100% wk WAS Budget 2016-02-29)")

# 7) What the limits are NOT built on:
print("7. exclusions: vol-forecast sizing does NOT protect (f05 MISS +5.77%; f04 onset "
      "lag 72-74 pts) => hard structural caps only; f13 (IV-HV quintile) REFUTED — unused; "
      "f20 overlay kept as cheap insurance (PASS/PASS) but effective n=1-2 events; "
      "CONTRACT: delta-adjusted exposure inside the 1.5x gross cap, Tier-C reduce-only")

# 8) Frequency allocation:
print(f"8. tenor: MONTHLY primary (f17 geo +13.96%/yr vs weekly RUIN at full margin); "
      f"weekly sleeve optional at f<=0.035 only (+1.3%/yr, f18) — near-zero growth, "
      f"prefer 0")
