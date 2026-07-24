# AZBY Portfolio Review — standard template deck

A reusable, tiered portfolio-review template for automating client proposals, built in the
Ionic Wealth house style (palette, logo and chart aesthetic extracted from the existing deck).
**`AZBY Family` is fictional and every holding is illustrative dummy data** — the deck exists to
standardise layout, content and charts, not to depict a real client.

## What's in the deck (46 slides, one tiered master)

Each content slide carries a tier chip so an advisor knows what to show:

| Tier | Chip colour | Use |
|------|-------------|-----|
| **RM · CORE** | green | always shown — the plain-language decision story |
| **STANDARD** | indigo | add the analytics (scoring, fund frameworks, quality-vs-price, frontier) |
| **UHNI · FAMILY OFFICE** | amber | consolidation, governance/succession, goal funding |
| **APPENDIX** | slate | reusable chart library, full registers, methodology |

Two personas run through it: an **HNI business family** (~₹5.3 Cr) anchors the IPS and the main
review; a **UHNI family office** (~₹78 Cr, five entities) anchors Section 07.

## Regenerating

```bash
python3 build_data.py      # -> azby_data.json (holdings from the NIFTY-750 scorecard, all derived metrics)
python3 build_charts.py    # -> assets/charts/*.png (24 charts in the Ionic palette)
npm install                # first time only (pptxgenjs)
node   build_deck.js       # -> AZBY_Portfolio_Review_Template.pptx
python3 render_preview.py  # -> assets/preview/*.png  (QA render; flags text overflow in red)
```

`build_data.py` reads the scorecard workbook (kept outside the repo). To retarget the template to
a real book, replace the holdings/fund lists in `build_data.py` (or point it at a client feed) and
re-run the pipeline — the charts and deck rebuild automatically from `azby_data.json`.

## Files

- `build_data.py` — dataset builder (holdings, scores, concentration, sector/cap, fund frameworks, personas)
- `build_charts.py` — matplotlib chart library (flat, frameless, semantic-colour, Ionic palette)
- `build_deck.js` — pptxgenjs deck generator (all slides, tier chips, IPS, narratives)
- `render_preview.py` — python-pptx + PIL QA renderer (LibreOffice-free)
- `assets/` — logo (indigo + white variants), chart PNGs
- `AZBY_Portfolio_Review_Template.pptx` — the built deck

## House palette

navy `#16233B` · indigo `#1B27A3` / `#4A57C4` · green `#1E9E6A` (Hold/positive) ·
coral `#E0402F` (Sell/negative) · amber `#F2A93C` (threshold/watch) · slate `#6B7280`. Font: Calibri.
