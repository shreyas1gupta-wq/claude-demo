# Atlas 1.2 — real-estate cycle: JST R6 results (RE1-RE2)

Constructions and pass bars PRE-REGISTERED in the trial ledger before this ran; the
interpretation below was written AFTER the print (standing rule). Peaks = local maxima
of the 3y-centered-smoothed level, min_gap 8y, per country; spacings pooled.

## RE1 — the folk 18-year claim (real house prices)

- n = 109 spacings across 17 countries.
- Pooled spacing: median **14y**, IQR 10-17y, full range 8-45y.
- Share in the claimed [14, 22]y window: **45%** (bar: >=50%).
- Pre-registered bar: median in [14,22] -> True; share >=50% -> False. **FAIL**.

Per-country median spacings (y): Australia 13, Belgium 14, Canada 16, Denmark 13, Finland 18, France 11, Germany 20, Ireland 17, Italy 16, Japan 15, Netherlands 14, Norway 13, Spain 16, Sweden 16, Switzerland 13, UK 15, USA 10

## RE2 — the Kuznets 15-25y swing (investment/GDP)

- n = 177 spacings across 18 countries.
- Pooled spacing: median **11y**, IQR 9-15y.
- Share in the claimed [15, 25]y window: **25%** (bar: >=50%).
- Pre-registered bar: median in [15,25] -> False; share >=50% -> False. **FAIL**.
- Pre/post-1950 split (direction only, no bar): median 12y (n=82) vs 11y (n=95).

## Honest read (written AFTER the print)

- RE1 is an INFORMATIVE fail. The folk school is not hallucinating LENGTH: real house-price
  peaks live on a decade-plus scale (median 14y, IQR 10-17y) — far slower than business
  cycles, which is the part L12 already carries. What dies is the FIXED period: only 45% of
  spacings land in an 8-year-wide window centered near the claim, the full range runs 8-45y,
  and the per-country medians run 10y (USA) to 20y (Germany) — "18" is not even a stable
  country constant (Finland alone prints exactly 18). A date claim needs the distribution to
  be tight; this one is wide. States, never dates — now with the folk cycle's own numbers.
- Construction bias favors the claim and it still fails: min_gap 8y deletes all short
  spacings, mechanically pushing medians UP toward the claimed window. RE1 fails anyway.
- RE2 is a CLEAN fail: investment/GDP swings space at 11y median (25% in [15,25]y) — the
  Kuznets band is not there on this tool. The pre/post-1950 split (12y -> 11y) shows no
  "passing of the Kuznets cycle" direction either; our crude spacing tool may simply be
  blind to a swing that Abramovitz measured with amplitude, not spacing. We report the tool's
  limits rather than the tradition's vindication.
- Consequence for the monograph: the verdict section was drafted expecting exactly this
  shape (mechanism survives inside L12, fixed periods rejected). No pass bar was moved.
