# Atlas 2.2 — shadow credit: the funding-run factor signature (SC1, pre-registered)

Data: vaulted IIMA monthly factors (log-cum 12m windows, 1994+). Bars fixed before
looking; comparator rows are context, no bars. Interpretation AFTER the print.

| Window | SMB 12m cum | SMB percentile | Market 12m cum | Market percentile |
|---|---|---|---|---|
| IL&FS crunch (2018-09..2019-08) | -24.8% | 18th | -20.2% | 16th |
| GFC (2008-09..2009-08) | -10.8% | 33th | +3.9% | 49th |
| Taper (2013-05..2014-04) | -1.7% | 49th | +7.7% | 57th |
| COVID (2020-02..2021-01) | -4.7% | 42th | +19.9% | 70th |

- Pre-registered bars (IL&FS window): SMB percentile ≤ 10th -> False; market
  percentile > 10th -> True. **SC1 FAIL**.

## Honest read (written AFTER the print)

- **SC1 FAILS, and the failure is a finding about propagation.** The mechanism-derived claim
  ("credit-supply event concentrated in small firms; market escapes") is half-right: SMB's
  −24.8% is severe (18th percentile) — but the market's −20.2% (16th) shows the freeze did
  NOT stay contained. Twelve months after IL&FS, the funding shock had propagated into a
  broad growth slowdown (autos, consumption credit) — which is precisely WHY the atlas routes
  the funding-freeze signature to L2 (fast stress): by the time a 12m equity window can see
  it, it is everyone's problem. A signature useful to the desk must be FASTER than this test.
- Comparator prints (context, no bars): the GFC and COVID 12m windows END after their
  rebounds began (+3.9%, +19.9% market) — window-end alignment matters and is stated, not
  hidden. Taper barely registers in factors at 12m.
- **No re-run at a different horizon** — that would be iterating until pass. The short-horizon
  version of this claim lives where the mechanism's native variables live: SC2's CP-spread
  freeze signature (runsheet-gated), with any equity-side acceptance registered THERE before
  running. Equity-factor claims from this entry stay dead.
