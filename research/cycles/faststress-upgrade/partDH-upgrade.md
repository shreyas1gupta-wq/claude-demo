# Parts D–H (upgrade addendum) — fast stress at full standard (atlas 5.1/5.2/5.3 → L2)

The v1.0 entry's designs F1–F7 and its measured synthetic bounds STAND UNCHANGED (that
document's §4–§5 remain the operative pre-registrations). This addendum records what the
upgrade adds and how atlas 5.2/5.3 formally fold into the seat they always fed.

## Part D — What the upgrade adds to the evidence

**FS-U1/FS-U2 (our first real-data prints for this seat).** Monthly |return| autocorrelation
0.141–0.188 (India MF, LB(6) p=4e-11) and 0.170–0.245 (gold float era, p=3e-33). Two uses,
both honest: the Tier-A fact now has a print computed from OUR vault (library integrity),
and the magnitudes quantify the aggregation loss — monthly clustering at ~0.15–0.25 versus
the ~0.2–0.4 lag-1 range typical of daily |returns| in the literature. The fast layer's
daily-resolution design requirement is thereby MEASURED, not asserted: the resolution
theorem (CW1/CR2) applied in reverse — the phenomenon survives aggregation but its
usable sharpness does not.

**The order-of-arrival taxonomy (pre-registered as a classification, never fitted).** The
three legs see impairment in a stated order that differs by shock type: credit-transmission
crises run funding → vol → drawdown (2018: CP spreads widened weeks before index vol);
exogenous shocks run vol → drawdown → funding-if-at-all (2020, 2024-election). The
taxonomy's use is diagnostic (which playbook page), NOT predictive weighting; any
leg-weighting change must come from F2/F5's grids, and the classification is falsifiable
episode-by-episode as daily data lands (FS-D2).

## Part E — Seat status

Module seated and tested since v1.0 (planted-truth suite incl. the honest 92/98 detection
bound and no-look-ahead truncation). Upgrade-era wiring: the H58 statutory-drain quarantine
now lives in ladder.yaml L2's role text (funding-leg fires inside drain windows are flagged
mechanical, two-of-three confirmation overrides — exclusion_calendar.py, tested). Phase
overlay unchanged: U arms cuts, D is display-only until F7 passes.

## Part F — Designs (additions only; F1–F7 unchanged)

- **FS-D1 (VIX term-structure state, atlas 5.2):** distinct from F5 (which tests IV LEVEL
  redundancy). Object: backwardation flag — near/far implied-variance ratio > 1 (near-month
  India VIX vs 2-3 month, from NSE VIX futures history where listed, else the option-chain
  IV term slope). Bar at registration when the archive is vaulted: episode AUROC of the
  backwardation flag must ADD over the RV-rank leg alone on the §3 episode set (incremental,
  purged); a redundant flag is documented and excluded like any other.
- **FS-D2 (order-of-arrival, atlas 5.3):** on the vaulted daily set (CCIL spreads, India
  VIX, index RV): for each §3 episode, date each leg's first top-decile print; the 2018
  funding-led and 2020 vol-led orderings are the pre-stated shape checks; a taxonomy that
  fails them dies as a classification (the legs stay, unordered).
Both data-gated; runsheet pulls (India VIX archive, CCIL dailies, VIX-futures history).

## Part H — Knowledge ledger (upgrade)

**Established (our prints):** monthly-resolution clustering on the vault (FS-U1/U2), with
the aggregation loss quantified. **Established (synthetic, v1.0):** the module's detection
bound (92/98 at 0.3, median lag 1d) and its falsified-then-corrected 100%-claim history.
**Pooled-prior (Tier A/B):** clustering + leverage effect (A); vol-targeting DD control
(60y multi-asset); the CONTESTED alpha claim (Moreira-Muir vs Cederburg — prior unchanged:
DD control robust, alpha unproven); backwardation-as-stress (Whaley lineage, B);
funding-leads-vol in credit-transmission crises (Brunnermeier-Pedersen + the 2018 India
record, B). **Awaits India data:** F1–F7 in full, FS-D1/FS-D2. **Unknowable:** the next
spike's date — the seat reacts in days; it never predicts, and the monograph's every claim
is resolution-stamped.


---

## Post-assembly addendum (2026-09-02, same day): three of this monograph's designs printed

Run on the vaulted NIFTY daily mirror the same day this upgrade was assembled (full prints:
research/cycles/daily-batch/daily-RESULTS.md; ledger entries F2-index, F7a, FS-D3):
- **F2 (bounded index run):** 3/18 grid cells supportive, all at trigger 0.80 + 1-of-2
  confirm; the "any one arms" asymmetry measured; shortlist {calendar, decay} re-entry.
- **F7 (first real print, F7a):** FAIL (63bd forward returns U vs D at matched high state,
  p=0.653) — per this document's own frozen rule, **phase is display-only for L2**; the
  phaseD grid dominance was re-attributed to re-entry earliness (doctrine: levels, not
  directions). F2c (direction-free calendar-21bd) registered.
- **FS-D3 (interim global-VIX confirm leg):** REFUSED — symmetric averaging diluted domestic
  detection (lost the 2024 episode) while accelerating global-origin crises (2011 lag
  91→13bd); FS-D4 (arm-only) registered, deferred to full F2.
None of these bounded prints arms the R4 mapping; the full F2 (three legs, book costs, M4
walk-forward) remains the registered adjudicator.
