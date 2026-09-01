# Atlas 1.6 — capex cycle (L11): analogue results, JST R6 (IN1-IN3, pre-registered)

India official series are proxy-blocked here; per the atlas's own 'C→B via analogues'
clause these trials run on the 18-country JST iy panel + vaulted real equity returns.
Bars pre-registered; interpretation AFTER the print.

## IN1 — capex state → forward 5y real equity return

| Country | corr(state, fwd 5y log real return) |
|---|---|
| AUS | -0.23 |
| BEL | -0.33 |
| CHE | +0.04 |
| DEU | +0.23 |
| DNK | -0.32 |
| ESP | -0.13 |
| FIN | -0.15 |
| FRA | +0.09 |
| GBR | +0.11 |
| ITA | +0.25 |
| JPN | -0.10 |
| NLD | -0.25 |
| NOR | -0.42 |
| SWE | -0.20 |
| USA | +0.08 |

- Sign-consistency: **60% negative** of 15 countries (bar ≥70%): **FAIL**.

## IN2 — post-peak repair length (iy regaining its peak)

- 195 peak spells; median repair **4y** (23 censored spells counted at censoring value, as pre-stated);
  IQR 1-12y.
- Bar (median ≥ 4y): **PASS**.

## IN3 — quintile asymmetry (measurement, prior set — informs the clamp)

- Pooled mean forward-5y log real return: top-quintile capex state **+0.242**,
  middle **+0.202**, bottom-quintile **+0.287** (n = 310/891/305 country-years).

## Honest read (written AFTER the print)

- **IN1 FAILS the sign-consistency bar (9/15 negative), and the failure calibrates the seat.**
  On the project's own scale this sits between demographics (4/16, rejected) and the financial
  cycle (17/17, seated Tier-B): a weak tilt, not a pooled regularity. The analogue panel does
  NOT supply the "C→B via analogues" graduation — L11 STAYS Tier C. No re-run, no bar moved.
- **IN2 PASSES exactly at the bar (median 4y) with a wide honest spread (IQR 1-12y).** The
  repair-takes-years claim holds at the median; the 1y quartile shows many iy peaks are
  shallow local maxima, not overbuilds — which is why the seat keys off PERCENTILE EXTREMES,
  not every wiggle. 23 censored spells counted at censoring value as pre-stated (biases the
  median DOWN, i.e. against the claim — it passed anyway).
- **IN3 is the clamp's vindication, in an unexpected shape.** Top-quintile forward returns
  (+0.242 over 5y, log) sit BELOW bottom-quintile (+0.287) — the mild overbuild penalty —
  but the middle (+0.202) is lowest of all: the state does not ORDER returns monotonically.
  A seat this weakly informative must never ADD regime score; subtract-only at the hot
  extreme, inside the shared budget, is precisely what min(0, ·) implements. The
  consistency-audit's design decision now has the analogue panel's numbers behind it.
- **Net:** seat CONFIRMED at its clamped, Tier-C, reduce-only station; graduation deferred to
  the changes_if clause (purged India backtest on OBICUS/IIP/GFCF once pulled — runsheet).
  The module ships as machinery with the degradation and clamp semantics tested; the evidence
  tier is unchanged by shipping code.
