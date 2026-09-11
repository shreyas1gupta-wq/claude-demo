# HNI prospecting — figure set

Ten hand-built editorial figures for the *Cracking HNI prospecting* briefing:
a hero scene, five persona portraits, four section vignettes. Indigo duotone
with a single amber accent each, drawn as inline SVG.

Open **`preview.html`** to see the set at real sizes on the briefing's own
indigo ground, with the `<use>` snippet under each figure.

Original artwork — no stock, no licensing exposure, no external requests, and
crisp at any size. Photographs were not an option regardless of preference: the
artifact CSP blocks all external images, so stock could not render even setting
licensing aside.

## Dropping it in

Two steps, and **nothing existing changes**. The pack is additive by
construction — it defines no global CSS, occupies no layout, and never touches
a word of the briefing's copy.

**1. Paste the sprite once**, anywhere in the `<body>`. Take the whole block
from `figures-inline.html`. It renders nothing on its own.

**2. Place a figure** wherever you want one:

```html
<svg viewBox="0 0 400 500" role="img" aria-label="First-generation promoter">
  <use href="#fig-promoter"/>
</svg>
```

Size it with CSS — `width:100%;height:auto` is usually all it needs. For a
figure that is purely decorative, swap `role`/`aria-label` for
`aria-hidden="true"` so screen readers skip it instead of announcing it.

`figures.svg` is the same sprite as a standalone file if you would rather
reference it externally — but note a single-file artifact cannot fetch it, so
the inline block is the route that works there.

## What's in it

| Section | Symbol | viewBox | Renders well at |
|---|---|---|---|
| Overview | `#fig-hero` | 1000 × 560 | 600–1000px wide |
| Who you're meeting | `#fig-promoter` | 400 × 500 | 150–340px wide |
| Who you're meeting | `#fig-executive` | 400 × 500 | 150–340px |
| Who you're meeting | `#fig-professional` | 400 × 500 | 150–340px |
| Who you're meeting | `#fig-inheritor` | 400 × 500 | 150–340px |
| Who you're meeting | `#fig-founder` | 400 × 500 | 150–340px |
| The engine | `#fig-engine` | 300 × 300 | 100–260px |
| Trust | `#fig-trust` | 300 × 300 | 100–260px |
| Watch-outs | `#fig-watchouts` | 300 × 300 | 100–260px |
| The week | `#fig-week` | 300 × 300 | 100–260px |

The portraits hold up from 84px thumbnails to 340px cards. The vignettes are
drawn for ~100–260px; pushed much past that the mini-figures in `#fig-trust`
start to look simpler than the full portraits, since they are built for a size
where facial detail does not resolve.

## The five personas

I could not read your briefing from this session, so these are the archetypes
the segment actually contains — corroborated by the product and company tags in
the Aug-31 MIS (`RSU Wealth Planning`, `Pre-IPO Investments`,
`SME-focused NBFC`, `accredited investor`):

| Symbol | Archetype | Read |
|---|---|---|
| `#fig-promoter` | First-generation promoter | Built the business. Trusts people, not brochures. |
| `#fig-executive` | Senior corporate executive | RSU- and ESOP-heavy. Optimises, compares, decides on paper. |
| `#fig-professional` | Practice professional | Doctor, lawyer or CA. Time-poor, referral-driven. |
| `#fig-inheritor` | Next-generation inheritor | Family wealth, own views. Wants to be taken seriously. |
| `#fig-founder` | Post-exit founder | Liquidity event just landed. Moves fast, asks hard questions. |

**Renaming is a label change, not a redraw.** Each portrait is keyed only by its
symbol id, so pointing `#fig-executive` at *your* second persona means editing
the `aria-label` and the caption beside it. If your five are materially
different people — a different age, a woman where I drew a man — say so and
I'll redraw that one; the parameters live in one place.

## Rebuilding

```bash
python3 hni-prospecting-art/build/pack.py
```

Standard library only, no dependencies.

```
build/
  pack.py       entry point: writes figures-inline.html, figures.svg, preview.html
  palette.py    ramps, the shared modelling gradients, the grain filter, face clips
  head.py       the shared head: 5 face shapes, 5 hairstyles, features, eyewear
  figures.py    the ten figures — persona params, hero, vignettes
  sprite.py     sprite and <use> helpers
```

### How it's put together

**One shared `<defs>` block.** The indigo ramps, the vignette, the modelling
gradients and a single `feTurbulence` grain filter are defined once, so ten
figures cost roughly the bytes of two. Total sprite: ~59KB.

**One construction grid, one light.** Every head is built on the same
proportions and lit from the same key, which is what makes a set read as
commissioned rather than assembled. Distinctness comes from silhouette first —
face shape, hair mass, eyewear, collar, build, head tilt — because that is what
survives at thumbnail size when facial detail stops resolving.

**Modelling, not flat fills.** Skin is a base colour plus two gradients clipped
to the face outline (one horizontal for form, one vertical for the jaw). The
gradients read their colours from CSS custom properties, so one shared gradient
serves five different skin ramps, and a light ground would be a token change
rather than a redraw. Grain is composited *inside* the artwork via an SVG
filter rather than a blend mode, so it renders identically everywhere instead
of degrading to a grey haze where blend modes are unsupported.

**One amber accent per figure** — a pocket pen, a tie, a neckline, a lapel pin,
a lanyard. The restraint is what makes it read expensive.

### Two things I tried and threw away

**Hands.** The engine and trust vignettes originally showed hands — gripping a
flywheel rim, passing a document. At every size and in two different
constructions they read as splayed starfish. Premium financial illustration
rarely draws hands, and both scenes are clearer without: the engine became a
geared flywheel under its own momentum, and trust became the signed undertaking
standing between two people.

**A tapered ribbon path for watch-outs.** Drawn in plan view it read as an
organic blob, not a road. It is now a two-route decision diagram, which matches
the register of the gears and the week grid and reads instantly.

## Verification

All checks pass. Run `preview.html` headlessly in the pre-installed Chromium
via the global Playwright (`NODE_PATH=/opt/node22/lib/node_modules`):

- all 10 symbols defined, and every `<use>` resolves to one
- every figure renders non-zero **and paints actual pixels** — a resolved but
  blank symbol would slip past a size check, so each is screenshot and its byte
  count asserted
- every symbol carries a `<title>` and `<desc>`; every meaningful figure exposes
  an accessible name; the sprite itself is hidden from the accessibility tree
- the sprite defines no `<style>` rules and occupies zero height, so it cannot
  disturb a host page
- no horizontal scroll at 1440px, 820px or 400px
- zero console errors
