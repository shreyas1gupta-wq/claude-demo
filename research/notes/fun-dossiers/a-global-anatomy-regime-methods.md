# Global Business-Cycle Anatomy and Regime-Identification Methods (Track FUN dossier A)

*2026-09-08; Sonnet research agent A, adversarially consumed by the desk. Knowledge
synthesis, no data access — every quantitative claim [LIT] with named source,
approximate; [LIT, LOW CONFIDENCE] where unsure. Cites, never repeats, the booked ground:
docs/cycles/18-business-cycle.md (Atlas 2.3) and 19-kitchin-juglar.md (the five-band
clock sweep: zero surviving fixed periods).*

## 1. The subparts

**Classical vs growth cycles** — argued in Atlas 2.3 §A.1 (Burns-Mitchell 1946 levels;
Mintz 1969 deviation-from-trend; growth-rate cycle one derivative out). Restated point:
since the 1980s essentially all advanced-economy dating operates in growth-cycle space —
default to that framing except in crisis-prone/EM samples [LIT — Mintz; OECD/ECRI].

**Two-phase vs four-phase** — two-phase (expansion/contraction) is NBER's operative
language and what Bry-Boschan outputs natively; four-phase
(recovery/expansion/slowdown/contraction) subdivides at growth-RATE inflections — the
quadrant scheme FUN-D1 ran. It is a derivative-of-a-derivative construct and inherits
choppiness and short phase length (FUN-D1's 28%/yr quadrant persistence is the house
measurement of exactly this).

**Sub-cycles** (all three already have program monographs and a dead clock verdict):
- *Kitchin* ~40m inventory (Kitchin 1923; Metzler 1941 stock-adjustment; bullwhip:
  Forrester 1961, Lee et al. 1997) — KJ1 booked 0/37 spacings in the claimed window:
  mechanism lives, clock dead.
- *Juglar* ~7-11y capex/credit (Juglar 1862; Schumpeter 1939 label) — object seated as
  L10/L11 bands; label retired.
- *Kuznets* ~15-25y construction (Kuznets 1930; demographic cohort mechanism [LIT, LOW
  CONFIDENCE on original figures]) — RE1 booked no fixed periodicity; the modern
  better-evidenced descendant is Borio's FINANCIAL CYCLE: a 10-20y BAND of
  credit-property co-movement, larger amplitude, implicated in the deepest recessions.

**Who leads whom (GDP vs IP vs profits vs credit vs market):**
- IP is COINCIDENT by construction (an NBER cross-check series).
- Corporate profits LEAD moderately — margins compress before output cuts [LIT, NBER
  tradition; LOW CONFIDENCE on quarter count]; the program's profit-share monograph
  carries the mechanism.
- Credit does NOT reliably lead the real cycle in phase (BC2: GDP leads credit 16/18 at
  home); credit's robust role is CRISIS PROBABILITY at multi-year horizons
  (Schularick-Taylor 2012, Baron-Xiong 2017, Drehmann-Juselius) — a different
  mathematical object (tail AUROC) from phase lead-lag. [FUN-D8 m3's horizon-separation
  print is the same fact from the return side.]
- The MARKET leads GDP ~1y and no further (booked ER-D8/GDP-D3/D4; 5:1 direction ratio) —
  **the internal bar: any candidate leading indicator must beat the market's own signal,
  not merely forecast GDP.** Conference Board taxonomy concurs: S&P 500 in the leading
  composite, IP in the coincident [LIT].

## 2. Regime-identification methods (practitioner-grade)

| Method | Inputs | Pub lag | Real-time reliability | Failure modes |
|---|---|---|---|---|
| NBER committee | GDP + monthly cross-checks | **6-18m announcement lag** (Dec-07 peak announced Dec-08; Jun-09 trough Sep-10; COVID peak 4m — extreme depth resolved fast) [LIT] | Gold-standard ex post, ~zero real-time trading value | Judgment, not a rule; unreplicable off-US |
| Bry-Boschan / Harding-Pagan | Local extrema + min-phase/cycle censoring | Input's lag + CONFIRMATION lag (months to >1y by construction) | Mechanical, replicable cross-country | End-of-sample turns revise away; min-length rules suppress short sharp cycles |
| Markov-switching (Hamilton 1989, Econometrica) | Single series, latent 2-state | None mechanically | **Real-time instability documented** (Chauvet-Piger 2008 JBES): filtered ≠ smoothed probabilities | Backtesting on SMOOTHED probabilities = lookahead; live signal only ever has filtered |
| Diffusion indices | Share of basket rising | Days-month | Good for Burns-Mitchell BREADTH | Threshold flips on noise; magnitude-blind |
| OECD CLI | 5-10 components/country, IIP reference (incl. India) | ~1m + REVISION | Long comparable history | Two-sided trend filter → endpoint (the point you need) least reliable [LIT] |
| Conference Board LEI | 10 components (hours, claims, new orders x2, ISM orders, permits, S&P 500, credit index, 10y-FF spread, expectations) [LIT; weights LOW CONFIDENCE] | ~3w | Long record | Recent-cycle false signals; embeds curve+permits (not independent evidence) |
| PMI 50-line | Diffusion survey | 1-3d | **Folklore overstates it**: 50 = vs-prior-month breakeven, NOT zero-GDP; ISM's own conversion puts zero-growth in the low-to-mid 40s [LIT, LOW CONFIDENCE on current value] | Sub-50 ≠ recession; manufacturing share shrinking makes mfg PMI noisier for the whole economy |
| Yield-curve probit (Estrella-Mishkin ~1996; NY Fed live) | Term spread, ~12m horizon | None (market price) | One of the best single-indicator recession-odds signals | False positives (1966, 1998 [LIT, LOW CONFIDENCE]); lead varies 6-24m (poor timing); QE-era term-premium distortion contested |
| Credit impulse (Biggs-Mayer-Pick ~2010) | Δ(flow of new credit)/GDP — second derivative | Weeks | Plausible in bank-intermediated economies (China headline case; India-relevant) | Flow-of-flow = noisy, revision-prone; untested by this program |
| Nowcasts (GDPNow, NY Fed) | Mixed-frequency bridge/factor models | None (running) | Volatile early-quarter, converges late [LIT, documented] | Early-quarter swings mistaken for regime information |

## 3. Which indicators actually lead (ranked, longest to shortest)

1. **Broad money growth** — "long and variable lags" (Friedman-Schwartz), ~1-2y
   historically, visibly degraded post-1980s deregulation/QE [LIT].
2. **Yield curve / term spread** — 6-18m, recession-odds only.
3. **Corporate credit spreads / EBP** (Gilchrist-Zakrajšek 2012 AER) — curve-like window,
   sharper concentrated move just ahead of downturns; incremental beyond the curve.
4. **Equity prices themselves** — the ~1y booked lead; the bar.
5. **Building permits/housing starts** — ~6-12m [LIT, LOW CONFIDENCE, share drift].
6. **New orders** — definitionally leads production by a few months.
7. **Average weekly hours (mfg)** — hours before headcount, ~a quarter.
8. **Initial claims** — fastest-arriving; genuine lead is SHORT (inflects near the turn).

**The bar restated:** nothing on the published record reliably out-leads the equity
market by more than a few months; several lead less. A new indicator earns a seat only by
(a) out-leading the market's ~1y GDP lead with comparable hit-rate, or (b) leading the
MARKET itself. Nothing tested so far clears either.

## 4. Turning-point asymmetry

The cycle is asymmetric: Neftçi (1984 JPE) — unemployment rises sharply, falls
gradually; Sichel (1993, Economic Inquiry) — **deepness** (troughs deeper than peaks are
tall), **steepness** (falls faster than rises), **sharpness** (V-troughs, rounded
peaks). Practical consequence: **recession-ENTRY detection is faster and more confident
than recovery-entry detection** — sharp downturns satisfy the comovement criterion
quickly; recoveries begin gradually and unevenly ("jobless recoveries": 1991, 2001,
2009 [LIT]); NBER trough announcements lag peak announcements. Desk implication: a dated
"entered contraction" is trustworthy sooner than a dated "entered recovery" — carry this
asymmetry in state-conditioning logic. [Joined to FUN-D2 e2/e3: PRICE anticipates
troughs (10m early, 75%) but not peaks — the market itself already trades this
asymmetry.]

## 5. Global data-point inventory

| Indicator | Freq | Pub lag | Free source | Identifies |
|---|---|---|---|---|
| Real GDP | Q | ~1m adv / ~3m final | BEA, Eurostat, MOSPI | The reference series |
| IP / IIP | M | ~4-6w | Fed G.17, MOSPI | Coincident; OECD's reference incl. India |
| PMI headline | M | 1-3d | ISM / S&P Global release | Sentiment breadth; weak at the 50-line |
| Initial claims | W | ~5d | DOL | Fastest genuine signal |
| Building permits | M | ~3-4w | Census/HUD | Classic lead via construction lag |
| New orders | M | ~3-4w | Census | Orders precede output |
| Avg weekly hours (mfg) | M | ~1w | BLS | Hours before headcount |
| Term spread | D | none | FRED/RBI | Recession odds (probit) |
| Credit spreads / EBP | D/M | 0-1m | FRED/Fed research | Credit stress; incremental lead |
| Broad money | M | ~2-4w | Central banks | Long variable lag, degraded |
| Credit impulse | M/Q | varies | CB aggregates | Demand lead in bank economies |
| Equity indices | D | none | vaulted | The ~1y bar |
| VIX/implied vol | D | none | CBOE (vaulted) | Risk-regime state |
| OECD CLI | M | ~1m+rev | OECD | Comparable composite; endpoint problem |
| Conference Board LEI | M | ~3w | TCB | The 10-component composite |
| GDPNow / NY Fed nowcast | cont. | none | Atlanta/NY Fed | Within-quarter nowcast |
| BIS credit-to-GDP gap | Q | ~1q | BIS | Crisis probability, not phase |
| GST/e-way/OBICUS/India PMI | M/Q | days-1q | GSTN/RBI/S&P | India nowcast surface (dossier B) |

**Summary.** The literature supports a layered, band-based (never fixed-clock) cycle —
the language the program's own frequency sweep reached independently. Mechanical dating
methods trade real-time reliability for replicability; the NBER gold standard is
unusable live (6-18m lag). The equity market is itself one of the best-documented
leading indicators — the program's ~1y bar is stringent, not low. Peaks confirm faster
than troughs; the desk's state logic should act faster on "entering contraction" than on
"entering recovery."
