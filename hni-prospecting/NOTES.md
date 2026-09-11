# HNI Prospecting deck — v3

12 slides, each a true **16:9 PPT page**. Open
`HNI_Prospecting_Dashboard.html`; rebuild with `python3 hni-prospecting/build.py`.

## This revision

1. **PPT-sized pages.** Every slide is a fixed 16:9 stage, letterboxed and
   centred, capped to the viewport height so nothing is ever cut off. Type
   scales with the page (`container-type:inline-size`, sizes in `cqw`), so a
   slide looks identical at 1440px and 1920px. `Ctrl/Cmd-P` gives one landscape
   page per slide with animation frozen at its end state.
2. **Copy cut hard.** Roughly half the prose is gone. Full sentences became
   phrases, the engine's seven levers lost their second paragraph, personas run
   two lines each, and the meeting steps are three short cards. Every figure and
   script from the note is still there.
3. **Human illustrations removed** — all of them: the hero scene, the five
   portraits, and the two figures in the trust vignette. The build fails if a
   reference to the old sprite reappears.
4. **Abstract marks instead.** An animated orbit on the hero, a growth-bar chart
   on the opportunity, five geometric key marks for the personas, a progress
   dial on the 60-second check, and the ring diagram on the circle. All inline
   SVG, no external assets.
5. **More animation.** Slides reveal on entry with staggered offsets; key
   phrases get an amber highlight that sweeps in behind the words; bars grow
   from the baseline; KPIs count up; the check dial fills as you tick; the
   circle rings scale in from the centre. Arrow and Page keys move between
   slides. All of it respects `prefers-reduced-motion`.
6. **Circle of influence moved** to slide 10, after *Five ways advisors quietly
   lose HNI deals* — it belongs with referrals, not before the engine.

## Order

`Overview · Opportunity · Engine · Who you're meeting · Proposition ·
Meetings · 60-second check · Trust · Watch-outs · Circle of influence ·
The week · Pocket version`

## Verification

`python3 hni-prospecting/build.py` checks nav order matches slide order, every
slide has a page stage, and no sprite reference survives.

Browser checks at 1440 / 1920 / 400px: every page measured at **1.778** and
fitting the viewport, no page overflowing its own frame, scroll-spy correct on
all 12 at every width, reveal animation firing, KPIs counting, persona panel
swapping, checklist reaching "ready" with the dial at 4, the trust fraction
equal to its score across all 81 slider combinations, the circle rings
switching, zero console errors, no horizontal scroll, and **zero contrast
failures**.

Two things only a screenshot could catch were fixed this pass: the amber
highlight wash turned muddy grey on the dark pages, and in the two indigo
callouts it sat *behind white text*. On any dark surface the highlight is now a
solid amber rule under the words instead of a wash behind them. A scripted
audit now checks every `.hl` against the luminance of the surface it actually
sits on, so the mismatch cannot come back silently.

## Self-contained

The two typefaces (Newsreader, Reddit Sans — latin subsets) are embedded as
base64 `@font-face` rules, so the file has **no external dependency at all**:
it renders identically offline, on a locked-down machine, or off a USB stick.
That is what takes it to ~795KB; there is still nothing to download alongside
it. Removing the Google Fonts link also cleared the last console error.

## Kept from v2

The trust equation still runs on the note's own formula with two sliders
driving a visible numerator and denominator. The scroll-spy is still
line-based, so it works whether or not `.main` is the scroll container — the
bug that pinned the nav to the last section on phones stays fixed.
