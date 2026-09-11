# HNI Prospecting dashboard — what changed

Rebuilt from `HNI_Prospecting_Dashboard_2.html` against the *Cracking HNI
Prospecting* session note. The note is the source of truth; this records what
was restored from it, what was fixed, and what was deliberately left out.

Open **`HNI_Prospecting_Dashboard.html`**. Rebuild with
`python3 hni-prospecting/build.py` (standard library only).

## Restored from the note — three sections that weren't on the page

| New slide | From | Why it matters |
|---|---|---|
| **The proposition** | §5 | The ₹25 lakh trial, and **the three opening scripts** — *The second opinion*, *The single view*, *Allocate*. These are lines an RM says out loud; none of them asks for a rupee. The most directly usable content in the note, and none of it was on the page. |
| **The 60-second check** | §6 | The four pre-meeting questions, as a live checklist that reads "you're not ready" until all four are ticked. |
| **The pocket version** | closing | The six takeaways plus the "the competition reads the same reports you do" sign-off. |

Deck goes 9 → 12 slides, in the note's own order.

## Restored into existing slides

**Figures that were missing:** the ~$1.65 trillion held by the 3.9 lakh
millionaires; **+63%** UHNI growth over five years; the 8.5 lakh base rising to
~1.65 million by 2027; and the geographic spread into **Jaipur, Pune and
Indore**. Sources now cited — **Capgemini 2026** and **Deloitte** — where the
page previously cited none. The prospecting-time and referral figures moved into
the KPI grid so all eight sit together.

**Detail that had been flattened:** every engine lever regained its *what it is*
/ *why it works* split, so "speed-to-lead is a multiplier — the firm that reaches
a live lead first usually keeps it" is on the page rather than compressed away.
Rohit's attribution is restored on the product-proposition rule. The personas
carry their full "what he actually cares about" text. The meeting steps regained
their specifics — sector homework as "a policy shift, a deal, a margin trend",
"advisor rather than a distributor", and the low-friction entry via "a fund he's
had a bad experience with that also sits on your sell list". The discovery
technique — *chase the feeling under the number* — is back, as is the founder's
first investor among centres of influence, and "be present at the event, not six
months after it".

`coverage.py` asserts all 72 facts and phrases are present, so a later edit
can't quietly drop them.

## Four bugs fixed

**1 · The navigation was wrong on every phone.** Below 960px the stylesheet
gives `.main` `height:auto; overflow:visible`, so it stops being a scroll
container — measured `scrollHeight === clientHeight`. Every
`IntersectionObserver` was built with `{root: main}`, so all nine sections
reported as permanently intersecting and the last one won: the nav read **"The
week" while sitting at the top of the page**, and never updated. The observers
now use the viewport, and the scroll-spy picks the section covering a reference
line rather than trusting a threshold.

**2 & 3 · The count-up and the circle draw-in fired instantly on mobile** —
same root cause, same fix. Both now animate when their section is reached, at
either width.

**4 · The trust simulator's arithmetic was dead.**
`pct = Math.round(SUM/s/SUM*100)` reduces to `100/s`; the `SUM = 24` constant
cancelled itself out. The result was a 10-stop slider with three states where
**eight of the ten stops showed the same message**, and it contradicted the
equation printed above it — the numerator never moved. Rebuilt on the note's
actual formula: two sliders (how early you pitch, how much homework you did)
driving a visible numerator and denominator. Range 1.0–20.0; the four messages
now cover 15 / 17 / 20 / 29 of the 81 combinations. The markup is seeded with
the value init produces, so the old 100→50 flash is gone.

## Also fixed while in here

- **Ten contrast failures**, found by a checker added for the purpose. The worst
  were the three script-card labels at **2.04:1** on white. Each colour was
  moved the minimum distance that clears WCAG AA; the page now reports zero.
- **Four figures were hidden below 1040px.** They now stack under the content
  instead — losing 40% of the artwork on phones was the wrong trade.
- **The checkbox tick depended on a CDN icon.** It is now pure CSS, proven by a
  test that blocks cdnjs outright.

## Illustrations

The ten figures from `hni-prospecting-art/` are wired in: the hero scene, the
four vignettes (engine, trust, watch-outs, week) and the five portraits on the
persona tabs and panel. The sprite is injected at build time from
`hni-prospecting-art/figures-inline.html`, so the artwork stays authored in one
place.

Portraits are keyed to the note's five types, which differ from the figure set's
internal archetype names:

| Note's type | Figure |
|---|---|
| First-generation founder | `#fig-promoter` |
| GCC / MNC senior leader | `#fig-executive` |
| Senior doctor / professional | `#fig-professional` |
| Next-gen inheritor | `#fig-founder` |
| Corporate top & middle management | `#fig-inheritor` |

The last two are swapped relative to the set's own labels: the hoodie figure
reads younger, and the crew-neck-under-jacket figure reads corporate.

## Deliberately not done

- **No "Classified as Internal" marking.** The session note carries it on every
  page header; you chose to leave the dashboard unmarked. Flagged here only so
  the divergence from the source is on the record.
- **The Circle of Influence content is unchanged.** That section of the note is
  a bare heading with no body text and no image, so the four-layer content was
  authored elsewhere. It's good, and it stays.

## Verification

```bash
python3 hni-prospecting/build.py        # fails if a figure is missing or unreferenced
python3 hni-prospecting/coverage.py     # 72/72 facts and phrases from the note
```

Browser checks run headless in the pre-installed Chromium via the global
Playwright (`NODE_PATH=/opt/node22/lib/node_modules`), at 1440px **and 400px**:

- the scroll-spy is asserted correct for all 12 sections at both widths — the
  check that fails against the old file
- count-ups and the circle are asserted *not* to have fired before their section
  is reached, then asserted to have fired after
- the trust simulator is swept across all 81 slider combinations: the displayed
  fraction must equal the displayed score, both inputs must matter, pushing
  earlier must never raise trust, and no message may cover more than half the grid
- the 60-second check: starts not-ready, four ticks make it ready, untick reverts
- every figure resolves and renders non-zero; zero console errors; no horizontal
  scroll; no slide whose content overflows it; zero contrast failures
