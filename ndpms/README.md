# ₹500 Cr NDPMS Mandate — Operating Blueprint

What the Investment Office **can** do, **should** do and must **avoid** when running a
₹500 crore Non-Discretionary PMS mandate (SEBI PM Regulations 2020) across ETFs, index and
active MFs, AIFs, direct stocks, third-party PMS, bonds, REIT/InvITs, gold/silver, international
and cash — with a monthly-rebalance core, daily monitoring and tail-risk / performance dashboards.

## Files

| File | What it is |
|------|------------|
| `NDPMS_500Cr_Operating_Blueprint.md` | The blueprint narrative (sections 0–13 + appendices), critic-corrected |
| `blueprint_data.json` | Structured data pack behind every chart and table (allocations, CMAs, stress library, limits, KPIs, cost stack, matrix, roadmap, RACI …) |
| `NDPMS_500Cr_Blueprint.html` | Built report: charts + tables + full narrative, single self-contained page |
| `build_report.py` / `report_template.html` | Generator: `python3 build_report.py` rebuilds the HTML from the two inputs above |
| `research/` | The working papers: 7 domain designs, 2 verified data/fact packs, 4 adversarial critiques, completeness review |

## How it was produced

Seven domain designs (regulatory & tax, allocation, rebalancing & execution, risk, performance,
selection, operations) and two verified data packs (market history, regulatory/tax facts) were
written in parallel, then attacked by four reviewers (SEBI compliance, multi-asset CIO,
quant risk/performance, PMS operations). A synthesis pass merged them, a completeness critic
checked what was dropped or inconsistent, and a revision pass produced the final blueprint.
Numbers that could not be verified against a primary source are labelled *approx.* in the text.

## Rebuilding

```bash
python3 build_report.py            # reads the .md and .json next to it, writes NDPMS_500Cr_Blueprint.html
python3 build_report.py a.md b.json out.html   # explicit paths
```

Requires `pip install markdown`. Charts are plain SVG rendered client-side; the page uses the
Ionic palette re-stepped to pass colour-vision checks in light and dark themes.
