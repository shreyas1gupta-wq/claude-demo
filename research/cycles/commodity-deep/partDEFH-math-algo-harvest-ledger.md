# Part D — The mathematics (atlas 1.3; candidate H53, Tier C)

## D1. Why the supercycle count is tool-made, said precisely

A band-pass filter with pass-band [20y, 70y] is a linear map whose output, BY CONSTRUCTION,
contains only oscillations in that band: applied to ANY sufficiently long series — including a
random walk — it returns smooth 20-70y waves. So "we band-passed 150 years of prices and found
3-4 supercycles" is partially a statement about the filter. It is also two-sided (uses future
observations), so its historical dating is not achievable in real time — the exact HP-filter
objection the Contract codifies (Hamilton, never HP). Our machinery (expanding, one-sided,
extrema with a declared min_gap) found 8 arcs at 15-21y spacing; the literature's supercycles
are alternate arcs of that finer sequence (CS1, ledgered). Neither resolution is "true"; ours
is the one a desk can compute on the day it trades.

## D2. The state, as the seat would compute it

Long leg (annual, 1850-): chained equal-weight Δlog real index (CS1b construction — identical
chronology to plain, composition-robust) → expanding Hamilton gap (annual h from the shared
{4,5,6} grid) → expanding percentile. Modern leg (monthly, 1980-): IMF panel group indices +
EIA crude, same machinery on the monthly shared grid. SPLICE RULE (registry entry required
before production use): the monthly leg takes over where it exists; the annual leg provides
the rank warm-up so the monthly percentile is never young — validated on the 1980-2015 overlap
(design CM4). India leg: the SAME world series re-weighted by the import basket (partC's
construction) — a linear re-weighting, no new estimator, so the machinery inherits all shared
grids. n_legs-style degradation is NOT needed here (world prices have no India-length problem);
what IS inherited is the Tier-C clamp: reduce-only contribution capped per ladder.yaml until
H53 graduates.

## D3. What CS1-CS4 permit and deny

CS2 (breadth PASS) licenses the ToT-state construction: an import-weighted index measures a
real common factor, not oil three times. CS1 (FAIL) bans period language anywhere in the seat:
no "we are X years into the supercycle", ever — states only. CS3/CS4 (FAIL at the bar) deny
any mechanical capacity-timing rule; the capex-lag mechanism stays case-record narrative and a
registered future design (CM2), not an input. India consumption: importer sign convention —
HIGH world/basket state = terms-of-trade HEADWIND macro-side (CAD/INR/WPI) AND metals/energy
sector TAILWIND — the two harvests are OPPOSITE-signed consumers of one state, which is why
the seat must expose the state, never a portfolio direction.

# Part E — The algorithm (H53, Tier C; monthly with annual history)

```
STEP 1  world legs: chained Δlog real index (annual, Jacks) + monthly group indices (IMF
        mirror vintages; EIA crude for the current edge) per D2; CPI deflation per registry
STEP 2  gaps + expanding percentiles on the shared grids; annual->monthly splice per the
        registered splice rule (CM4 validates on the 1980-2015 overlap)
STEP 3  India ToT state: import-basket weights (partC C.1, annual re-estimate, PIT) applied
        to the SAME world series; publish {world_state, india_tot_state, impulse} + vintage
STEP 4  consumption (ALL Tier-C, reduce-only, per ladder.yaml caps):
        (a) L9 enrichment: india_tot_state as a conditioning input, never standalone
        (b) sector projection: metals/energy tilt conditioner (with H54 when it exists)
        (c) hedge scheduling: high-state-with-negative-impulse joins the watch list
STEP 5  NO date output exists anywhere in the interface (CS1)
MONITOR annual re-run of CS1-CS4 with new vintages; IMF-mirror refresh as NEW vintage files
        (WORM); basket-weight re-estimate each fiscal year; H65b-style drift note if the
        measured arc spacing shifts across vintages
FAILURE MODES: mirror goes stale (edge carried by EIA crude alone -> breadth flag degrades);
        basket weights stale (trade-data lag ~1y, stated); administered-price wedge makes
        India RETAIL passthrough lag world state (feature, not bug - measured in partC C.3)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| L9 India-transfer | india_tot_state as enrichment input (H53's design intent) |
| Sector projection | metals/energy conditioner (reduce-only, Tier-C cap) |
| Hedge scheduling | high-state + negative-impulse watch flag |
| Cycle School | Lesson 14: tool-made cycle counts; state-vs-clock on 165y of data |
| Trial ledger | the CS1 chronology as the standing refutation of period language |

Designs: **CM1** India ToT state on real data (blocked only on basket-weight transcription —
partC runsheet); acceptance: sign-consistency of india_tot_state's WPI-fuel/metals passthrough
(direction, lags per partC C.3). **CM2** detrended capacity event study (the honest retry of
CS3/CS4: production DEVIATIONS from expanding trend around named price-boom events; bars to be
pre-registered BEFORE running — not run in this entry to avoid iterate-until-pass). **CM3**
H53 graduation test: does india_tot_state add to L9 and condition metals/energy sector
returns under purged CV (needs India sector return history in the vault — Phase 0). **CM4**
splice validation: monthly-leg vs annual-leg state agreement on the 1980-2015 overlap
(acceptance: rank corr of the two states' overlap ≥ a bar set at registration time).

# Part H — Knowledge ledger (atlas 1.3)

**Established (165y panel, our runs):** commodity real-price arcs space 15-21y (median 18y,
8 troughs since 1870, composition-robust) — the atlas prior, not the literature's 30-40y
label; breadth is real (CS2: +0.30 across groups, 89% positive pairs); the vault is
authenticated three-lineage (A1-A5 all pass, first run).
**Failed honestly:** the 3-4-supercycle shape claim (CS1); decade-window capacity mechanics
(CS3 55%, CS4 64% vs 70% bars) — trend-domination named, retry registered (CM2), bars unmoved.
**India [importer]:** one state, two opposite-signed harvests (macro headwind vs sector
tailwind) — the seat exposes the state, consumers apply their own sign.
**Unknowable:** whether the energy-transition decade produces the next canonical arc; the
seat conditions and waits — no date interface exists to be wrong about (D3).
**Process:** near-miss #4 (pre-written authentication "results") caught pre-run and logged;
the two-pass rule (bars pass, results pass) is now standing for authentication files too.
