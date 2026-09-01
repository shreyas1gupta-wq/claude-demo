# Part D — The mathematics (atlas 1.1; shared machinery in the credit monograph's Part D)

## D1. The two-leg state and its degradation semantics

state_t = clip( (w_c·(2C_t−1)·1[C] + w_h·(2H_t−1)·1[H]) / (w_c·1[C] + w_h·1[H]), −1, 1 ),
with C = credit-gap percentile, H = real-house-price-gap percentile, 1[·] availability
indicators. n_legs = 1[C]+1[H] is a FIRST-CLASS output: a date carried by one leg is a degraded
reading, flagged to the sentinel, never silently equal-dignity with a two-leg reading. This is
India's short-HPI reality (ranks only from ~2020 on a 2010-start series) turned into API
semantics instead of a footnote — and the test suite pins it.

## D2. Both legs are impulses — where the LEVEL lives

The expanding Hamilton gap is an acceleration/turn detector (the credit monograph's measured
finding, reproduced here on the property leg: 10/10 turn collapse at −0.88..−0.97). L12
therefore contributes impulse information; boom-MATURITY (level) information inside the macro
block comes from L10's CD-ratio leg. The de-duplication rule (§4.2) in one line of algebra: the
block's information set is {credit impulse, credit level, property impulse, composition,
confirm} with ONE budget (0.20) — L12 adds the third element only, and any weight it earns is
weight L10's inputs give up inside the same cap. No stacking, ever.

## D3. What FC1-FC3 permit

FC1 (17/17 co-movement) licenses the JOINT construction. FC2 licenses only a lengthening WATCH
(direction on a crude tool). FC3's weak peak-dating (1.2-1.3x) BANS date-like use — states,
never dates, now with the seat's own measured evidence for the ban. India n≈1 completed cycle:
the India leg enters Tier-C-length (clamped contribution per ladder.yaml L12) until a second
observed downswing exists — which may take a decade; the seat is built to wait.

# Part E — The algorithm (L12, monthly/quarterly)

```
STEP 1  housing-credit leg (monthly, sectoral deployment, bank+HFC rule) and RBI HPI leg
        (quarterly, lag ~1q) per Part C's pipeline; CPI deflation for the real HP series
STEP 2  gaps: expanding Hamilton, h from the shared 16-24q grid; percentiles with warm-up
        masks (HPI leg emits NaN until min_obs ranks exist - honesty by construction)
STEP 3  state, n_legs = financial_cycle_state(credit_pct, hp_pct); n_legs on the daily page
STEP 4  consumption: inside macro_credit (0.20) via the block combiner; India-length clamp:
        the L12 contribution is reduce-only until a second domestic downswing is on record
STEP 5  supply-side confirms (cement IIP, registrations, RERA launches) enter as Tier-C
        reduce-only conditioners per Part C - never as the state itself
MONITOR quarterly leg-freshness; RESIDEX/HPI methodology-break registry entries; annual
        re-run of FC1-FC3 with new data; H65b lengthening watch feeds tau_half_drift_policy
FAILURE MODES: HPI discontinuation/rebase (breaks registry; leg to NaN -> graceful
        degradation ALREADY the tested path); registration-data lag spikes; the black-money
        wedge biasing amplitude DOWN (stated: measured cycles understate true cycles)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| macro_credit block (0.20 shared) | the property impulse leg, de-duplicated per D2 |
| Hedge scheduling | joint-boom-turn states arm hedge steps earlier (with L10) |
| Sector projection | realty/financiers conditioning (projection principle; no new seat) |
| H65b / drift policy | FC2's lengthening watch |
| Sentinel | n_legs degradation flag; leg freshness |

Designs: **FN1** India two-leg state on real data (housing-credit leg from sectoral deployment
NOW; HPI leg as ranks mature) — acceptance: sign-consistency of the two legs' co-movement with
the panel's; **FN2** the combined-vs-single-leg crisis-association test on the panel (the
Drehmann-Juselius combined-indicator claim, our tools, ledgered grid); **FN3** supply-side
confirm value (cement/registrations lead-lag vs the HPI leg, event-framed); **FN4** the
un-burst-controls tracker (Australia/Canada high-state persistence — annual read informing the
high-state-without-date discipline).

# Part H — Knowledge ledger (atlas 1.1)

**Established (panel, our runs):** credit-property amplification (FC1, the cleanest
sign-consistency pass in the project); the impulse dynamics of both legs; lengthening direction
(FC2). **Weak, honestly:** peak-dating (FC3) — banned use, now with its own evidence.
**India [C-length]:** one completed cycle; the 2013-2020 invisible real correction (Part B); the
short-HPI degradation path is the DESIGNED path for the next several years.
**Unknowable:** the current upswing's remaining length — Australia/Canada prove high states can
persist for decades; the seat conditions permissions and waits.
