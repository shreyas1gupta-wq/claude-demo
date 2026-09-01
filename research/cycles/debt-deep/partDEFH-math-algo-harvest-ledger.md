# Part D — The mathematics of the debt arc (atlas 0.1)

## D1. The one equation that runs the whole cycle

The debt-dynamics identity (an accounting fact, not a model):

    Δb_t = (r_t − g_t)·b_{t−1} − pb_t + sfa_t

b = debt/GDP, r = effective nominal rate on the stock ÷ deflator (real effective rate),
g = real GDP growth, pb = primary balance/GDP (surplus reduces debt), sfa = stock-flow
adjustments (bailouts, valuation effects, skeletons). Everything in this monograph is about who
controls each term and what they will do when b gets large. Three regimes fall out:
- **r > g** (liberalization era, DS3: +1.1pp mean): debt falls only via surpluses or default.
- **r < g** (repression era −4.3pp; post-GFC −1.0pp): debt can melt without surpluses — the
  "painless" arc — IF the state can keep r low, which is precisely financial repression.
- **Fiscal dominance**: when b is high enough that raising r to fight inflation blows up the
  budget, monetary policy loses independence (Sargent-Wallace "unpleasant monetarist arithmetic":
  tight money today ⇒ more debt ⇒ more inflation later). The fiscal theory of the price level is
  the limiting case: the price level becomes the variable that revalues nominal debt to satisfy
  the government budget constraint.

## D2. Repression, formalized as a tax

Reinhart-Sbrancia's "liquidation rate": the real return on government debt when real rates are
negative, times the domestic debt stock held captively (banks via SLR-type rules, pension
mandates, capital controls) = an unlegislated tax on savers. Measurement in our data: share of
country-years with negative real short rates (DS2: 44% in 1945-80, 76% post-GFC) and the
liquidation flow ≈ (−real rate)·(debt/GDP) when negative. India-specific: SLR is an EXPLICIT
captive-holding rule — the repression apparatus is standing infrastructure here, which is why
this seat exists for an Indian book at all.

## D3. Why n<2 and what that permits statistically

DS1: the fiat era contains 4 completed deleveraging arcs in 18 countries; 11 are right-censored
at their 2020 peaks. A process observed to completion ~4 times, under two different monetary
orders, admits NO fitted cycle model (clock test fails catastrophically). What the data DOES
support: (i) era-conditional distributions of investor outcomes (DS4 — computable because
country-years, not arcs, are the unit); (ii) regime CLASSIFICATION (which r−g / repression state
are we in NOW — an observable, not a forecast); (iii) cross-country sign consistency of the
repression→real-asset channel. Hence the seat's Tier C, reduce-only, state-classification-only
design — the statistics permit nothing stronger, and we take nothing stronger.

## D4. The gold-floor arithmetic (L15's budget, derived)

The seat's expression is a floor on the gold sleeve's attribution (0.40–0.50 of the gold
allocation's rationale) plus a slow-debasement tail budget (0.3–0.6%/yr of NAV) with a
conditional lift (+1–2pp) when the fiscal-dominance state is ON (high debt percentile AND
persistent negative real rates AND CB gold-accumulation leg). DS4 is the justification: the
state's real equity mean halves (+4.5% vs +9.5%) but stays positive — so the response is
insurance-sizing arithmetic, not allocation flight: budget ≈ P(state)·E[equity shortfall]·
hedge-effectiveness, evaluated on the pooled priors, floored and capped in the registry. No
optimizer touches it.

# Part E — The algorithm (L15 inputs, quarterly)

```
STEP 1  debt level & slope: IMF WEO/FM (India + world), RBI/CCIL for domestic structure;
        debt/GDP expanding percentile + 5y slope sign
STEP 2  real-rate persistence: repo − CPI (monthly), rolling share of trailing 36m with
        negative real rates (the repression gauge); US TIPS 10y as the global leg (FRED, on
        the principal-machine runsheet)
STEP 3  captivity/composition (Tier C, clamped): SLR trajectory, CB gold buying (WGC/RBI WSS),
        COFER USD share drift  -> reduce-only enrichment
STEP 4  state: fiscal-dominance dummy = (debt pctile high) AND (repression gauge ON);
        phase object logged like every other state (0.6U notation applies)
STEP 5  expression: gold-floor attribution within [0.40, 0.50]; tail budget within
        [0.3, 0.6]%/yr; conditional lift +[1,2]pp when state ON — ALL reduce-only vs the frozen
        gold cap (<=50%), never a timing trade, never an equity exit
MONITOR quarterly refresh with the Ilmanen dashboard; annual review re-reads DS1-DS4 with one
        more year of data; the 2030 design review re-reads the whole seat
FAILURE MODES: CPI regime break (2026 rebase splice); WEO revisions (vintage rule);
        the state being ON for a DECADE (it can - design must not fatigue: budget is sized to
        be carryable indefinitely)
```

# Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| L15 gold floor | attribution within the pre-registered band, state-conditional lift |
| Tail budget | 0.3-0.6%/yr slow-debasement allowance (options/gold structures per sleeves.yaml) |
| Policy review memo | the r−g regime classification, quarterly, to the humans (never optimized) |
| Stage-2 red team | Perez/fiscal narratives quarantined here — Stage-1 sees only the observables |

New designs: **DB1** India repression gauge history (repo−CPI + SLR trajectory since 1970s;
CONTEXT series — India's own repression era pre-1991 is the domestic analogue); **DB2** gold's
conditional performance in fiscal-dominance states on the pooled panel (extends DS4 to the gold
leg using free gold/CPI series — the direct test of the floor's premise); **DB3** the censoring
tracker: re-run DS1 annually — the day a major economy completes a deleveraging arc is the day
this seat's priors get their first fiat-era out-of-sample test.

# Part H — Knowledge ledger (atlas 0.1)

**Established (accounting + pooled):** the debt identity and its three regimes; repression
happened (DS2) and is echoing now (76% negative-real-rate share post-GFC); r<g is the operative
arithmetic post-2008 (73% of years); investor translation: repression halves but does not destroy
real equity returns (DS4).
**Pooled-prior [A]:** the state definition thresholds (percentile grids); gold's conditional
edge in the state (DB2 pending).
**Awaits India data:** the domestic repression gauge history (DB1); SLR/captivity trajectory.
**Unknowable:** how THIS arc resolves (11/18 censored), on what timeline, and whether the fiat
era's resolution toolkit (repression, inflation, growth, default) repeats its 1945-80 mix — the
seat is built so that not knowing is survivable: reduce-only insurance, sized to be carried for
a decade without fatigue.
