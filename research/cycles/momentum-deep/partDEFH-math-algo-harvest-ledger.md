# Part D — The mathematics (momentum-specific; shared machinery referenced, not repeated)

The general econometric toolkit (Hamilton filter, AR(1) bias, AUROC=Mann-Whitney, Stambaugh,
empirical Bayes, purged CV, deflated Sharpe, block bootstrap) is documented in the credit
monograph's Part D and applies verbatim. Below is only what is momentum-specific.

## D1. The WML object and its statistics

Formation: at month-end t, rank stocks by r(t−12→t−1) (the skip month removes short-term
reversal contamination — JT's own refinement). WML_t+1 = mean return of the top decile − bottom
decile over month t+1. Two facts drive everything downstream:
- **The premium is a spread of two noisy portfolios**: Var(WML) = Var(W) + Var(L) − 2Cov(W,L);
  in panics Cov collapses (legs decouple) — variance spikes exactly when the mean turns negative.
- **Skewness is structural, not incidental**: the loser leg after a bear market is a portfolio of
  distressed, high-beta names — an embedded short put on the market's rebound. Our M3 table IS
  this statement in numbers: bear-and-market-up months average −4.59%/m (US, 97y).

## D2. The Daniel-Moskowitz conditional beta, formally

DM's regression: WML_t = α + (β₀ + β_B·I_Bear,t + β_BU·I_Bear,t·I_Up,t)·Mkt_t + ε_t, where
I_Bear = 1 if trailing 24m market return < 0 (known at month start), I_Up = 1 if the
contemporaneous market return is positive. Published finding (and our M2/M3 replication in
conditional-mean form): β_BU > 0 and large — in bear states the WML acquires NEGATIVE market beta
that bites specifically when the market rallies. The guard's design follows: condition on
(bear, high vol) which are ex-ante, never on I_Up which is ex-post; the guard therefore accepts
sitting out some bear-and-down months (which are WML's BEST: +6.85%/m US) as the premium paid
for skipping the crash zone. That trade-off is the F-design's cost-benefit object, not a free lunch.

## D3. Vol-managed momentum (Barroso-Santa-Clara), and why it works here when vol-timing
the MARKET is contested

Scaling: WML*_t = (σ_target / σ̂_t) · WML_t, σ̂ from trailing 6m daily WML returns, capped.
BSC's insight: WML risk is highly forecastable (its vol is more persistent than the market's)
AND its risk-return relation is inverted in panic states — so de-scaling on own-vol removes
mostly bad states. Contrast Cederburg's critique of vol-managing the MARKET (fragile alpha):
the momentum version survives their protocol far better because the crash states are precisely
the high-vol states. Our M5: Sharpe 0.77→1.29, maxDD 83%→29% on the replication panel —
direction confirmed; India version pre-registered for the primary factor pull.

## D4. Breadth and the fundamental law, applied to L3

IR ≈ IC·√BR·TC. The 750-name cross-section rebalanced monthly is where the book's breadth
actually lives (BR ≈ number of independent bets/year — hundreds, vs the ladder's handful).
Consequences: (i) small ICs suffice (IC 0.03 at BR 500, TC 0.5 → IR ≈ 0.34 from this sleeve
alone); (ii) TC (transfer coefficient) is the fragile term at Conservative-book AUM — the
admission matrix and netting exist to protect it; (iii) the decay haircut applies to IC, and
IC is measurable monthly (uniqueness-weighted realized IC in the sentinel's attribution pack).

## D5. Decay estimation without self-deception

The decay object is the post-publication/post-crowding IC path, not the headline mean. Standing
haircut: 25–35% off the literature IC, escalating to 58% if the post-2015 India subsample is
weak (registry L3 decay clause). M1's real-data read: post-2015 India mean UNdecayed but vol
halved (Sharpe up) — no escalation triggered, no relaxation either: the forward haircut prices
FUTURE crowding (AMFI factor-fund AUM growth is the crowding monitor's input), not realized
history. The 21.9%-vs-13.1% level discrepancy is a construction question [VERIFY], not a decay
question — flagged in the ledger and awaiting the primary library pull.

# Part E — The algorithm (L3 + L4 + guard), end to end

```
STEP 0  registry load; universe file (PIT NIFTY-750 membership, ban list, liquidity floor)
STEP 1  adjusted price panel from bhavcopy + CA factors (Part C pipeline steps 1-9);
        TRI cross-check within tolerance before any signal is computed
STEP 2  L3 score: momentum_composite(prices) = equal-rank blend of 12-1, 6-1, 52wk-high
        (weights fixed per D11 anti-optimization rule; blend swept only on pooled data)
STEP 3  sector-relative option: within-sector ranks where the registry flag is on (pre-reg
        choice per sleeve); output Signal objects (score, half-life class, capacity per book)
STEP 4  L4 state: tsmom_state(index) per index/gold with lookback grid {6,9,12}m; feeds the
        trend_tsmom block (0.20) as regime confirmation + hedge scheduling, never a lone trade
STEP 5  crash_guard(market): bear (24m cum<0) AND expanding vol top quartile => guard ON:
        WML-sleeve sizing multiplier steps DOWN its grid (reduce-only); re-entry per the
        per-sleeve re-entry family (Batch-2 Q8), phase-D conditioning only after H66/F7 pass
STEP 6  costs: expected round-trip per name (statutory + sqrt-impact) netted from alpha BEFORE
        ranking into construct/ (cost-netted alpha rule)
MONITOR monthly realized IC (uniqueness-weighted) -> decay ledger; crowding monitor (AMFI
        factor AUM, comomentum when buildable) -> throttle; cert: live-vs-backtest IC floor,
        crowding ceiling, crash-guard override never (guard is structural)
FAILURE MODES: CA-adjustment error (tripwire: TRI tracking-error breach -> signal freeze for
        affected names); index-membership vintage gap (freeze additions until resolved);
        ban-list names (never initiate; exits via futures where available)
```

# Part F — The harvest map (what momentum/trend feeds)

| # | Consumer | What it gets | Status |
|---|---|---|---|
| F-a | Return engine sleeve (L3) | the composite rank -> cost-netted alpha -> construct/ | live design |
| F-b | Regime confirmation (L4) | TSMOM state into trend_tsmom block (0.20 budget) | live design |
| F-c | Hedge scheduling | L4 negative state accelerates hedge-grid steps within policy | live design |
| F-d | Crash guard | reduce-only WML sizing multiplier in panic states (M4-validated) | live design |
| F-e | Phase/D re-entry | quadrant-conditioned re-entry for the sleeve | gated on H66/F7 |
| F-f | Crowding monitor | AMFI factor-fund flows/AUM + (later) comomentum | v2 pipeline seat |
| F-g | Stage-2 briefing | sleeve state + guard status on the daily page | live design |

New pre-registered designs opened by this deep-dive: **N1** India DM-regression (the D2 spec with
Stambaugh-robust errors) on the PRIMARY factor library once pulled; **N2** vol-managed India WML
(M5 protocol); **N3** 21.9-vs-13.1 reconciliation (construction audit vs AJV paper); **N4**
52wk-high vs 12-1 redundancy/complement split (Raju SSRN citations from Part C as priors); **N5**
crash-guard threshold grid (dd, vol-pctile) swept on pooled US+India with the false-fire ledger.

# Part H — Knowledge ledger (momentum/trend)

**Established (Tier A/pooled):** the premium exists everywhere measured for a century+ (JT, AMP,
Geczy-Samonov); crashes are conditional and forecastable-in-state (DM; our M2/M3 on both panels);
vol management compresses the crash tail (BSC; our M5); the mechanism is behavioral + limits-to-
arbitrage, so decay is real but bounded away from instant (McLean-Pontiff).
**Established about OUR machinery (planted truth + real data):** composite recovers planted
momentum; the guard separates bad months on synthetic AND 97 years of US reality AND the India
mirror; no-look-ahead proven by truncation.
**Pooled-prior, awaiting India primary [A]:** exact India IC/half-life; the DM beta magnitudes;
vol-managed India parameters; the 21.9% reconciliation.
**Unknowable:** the next crash's date (only its STATE is knowable); whether AI-age crowding
shortens the cycle further — the crowding monitor watches, the haircut prices, the cert kills.
