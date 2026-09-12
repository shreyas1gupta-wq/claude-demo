#!/usr/bin/env python3
"""Build the ₹500 Cr NDPMS Operating Blueprint report (single self-contained HTML).

Inputs (defaults point at the workflow output folder; override with CLI args):
  1. blueprint_final.md   – the narrative blueprint (## numbered sections)
  2. blueprint_data.json  – the structured data pack behind the charts/tables
Output:
  ndpms/NDPMS_500Cr_Blueprint.html
"""
import json, re, sys, html, pathlib, datetime
import markdown

HERE = pathlib.Path(__file__).resolve().parent
SCRATCH = pathlib.Path('/tmp/claude-0/-home-user-claude-demo/f31f9728-4a4d-5703-8958-ff115211d242/scratchpad/ndpms')
MD_PATH = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else (HERE / 'NDPMS_500Cr_Operating_Blueprint.md')
JSON_PATH = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else (HERE / 'blueprint_data.json')
OUT_PATH = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else (HERE / 'NDPMS_500Cr_Blueprint.html')

md_text = MD_PATH.read_text(encoding='utf-8')
data = json.loads(JSON_PATH.read_text(encoding='utf-8'))

# ---------------------------------------------------------------- narrative → sections
def split_sections(text):
    """Split on level-2 headings. Returns list of (num, title, body_md)."""
    parts = re.split(r'(?m)^## +', text)
    preamble = parts[0]
    sections = []
    for chunk in parts[1:]:
        title, _, body = chunk.partition('\n')
        title = title.strip().rstrip('#').strip()
        m = re.match(r'^(\d+|[A-Z])[\.\):]?\s+(.*)$', title)
        if m:
            num, ttl = m.group(1), m.group(2).strip()
        else:
            m2 = re.match(r'^Appendix\s+([A-Z])[\.\):]?\s*(.*)$', title, re.I)
            if m2:
                rest = m2.group(2).strip().lstrip(':—-– ').strip()
                num, ttl = m2.group(1), ('Appendix ' + m2.group(1) + (' · ' + rest[:1].upper() + rest[1:] if rest else ''))
            else:
                num, ttl = '', title
        sections.append((num, ttl, body))
    return preamble, sections

MD = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists', 'attr_list'])
def render_md(txt):
    MD.reset()
    out = MD.convert(txt)
    # wrap tables for horizontal scroll
    out = out.replace('<table>', '<div class="tbl-wrap"><table>').replace('</table>', '</table></div>')
    return out

preamble, sections = split_sections(md_text)
doc_title_m = re.search(r'(?m)^# +(.*)$', preamble)
doc_title = doc_title_m.group(1).strip() if doc_title_m else '₹500 Cr NDPMS Mandate — Operating Blueprint'
preamble_body = re.sub(r'(?m)^# +.*$', '', preamble).strip()

def slug(num, ttl):
    base = re.sub(r'[^a-z0-9]+', '-', (ttl or '').lower()).strip('-')[:40]
    return f's{num}-{base}' if num else f's-{base}'

# figure placement: section number → list of figure ids (rendered before the narrative)
FIGS = {
    '1': ['fig-tax'],
    '2': ['fig-alloc', 'fig-stats', 'fig-cma', 'fig-calret', 'fig-deploy'],
    '3': ['fig-calendar'],
    '4': ['fig-rebal'],
    '5': ['fig-stress', 'fig-limits', 'fig-ewi', 'fig-hedge'],
    '6': ['fig-decomp'],
    '7': ['fig-cost'],
    '8': ['fig-dash', 'fig-raci'],
    '9': ['fig-matrix'],
    '10': ['fig-roadmap'],
    '11': ['fig-kpi'],
}

toc_items, section_html = [], []
for num, ttl, body in sections:
    sid = slug(num, ttl)
    toc_items.append((num, ttl, sid))
    figs = ''.join(f'<div class="fig-slot" data-fig="{f}"></div>' for f in FIGS.get(num, []))
    label = f'<span class="secnum">{html.escape(num)}</span>' if num else ''
    section_html.append(
        f'<section class="doc-section" id="{sid}">'
        f'<h2>{label}<span class="sectitle">{html.escape(ttl)}</span></h2>'
        f'{figs}<div class="prose">{render_md(body)}</div></section>'
    )

toc_html = ''.join(
    f'<li><a href="#{sid}"><span class="tnum">{html.escape(num)}</span><span>{html.escape(ttl)}</span></a></li>'
    for num, ttl, sid in toc_items
)

# ---------------------------------------------------------------- headline numbers for tiles
matrix = data.get('matrix', [])
cnt = {v: sum(1 for m in matrix if m.get('verdict') == v) for v in ('must', 'should', 'could', 'avoid')}
stats = {p.get('portfolio', ''): p for p in data.get('portfolio_stats', [])}
def find_stat(key):
    for k, v in stats.items():
        if key.lower() in k.lower():
            return v
    return {}
mod, agg = find_stat('moder'), find_stat('aggr')
stress = data.get('stress_scenarios', [])
worst_mod = min([s.get('moderate_pnl_cr', 0) for s in stress] or [0])
worst_agg = min([s.get('aggressive_pnl_cr', 0) for s in stress] or [0])
worst_name = next((s['scenario'] for s in stress if s.get('moderate_pnl_cr') == worst_mod), '')
sleeves = len(data.get('sample_allocation', []))
built = datetime.date.today().strftime('%d %b %Y')

META = {
    'title': doc_title,
    'built': built,
    'must': cnt['must'], 'should': cnt['should'], 'could': cnt['could'], 'avoid': cnt['avoid'],
    'mod_ret': mod.get('exp_return_pct'), 'mod_vol': mod.get('exp_vol_pct'), 'mod_dd': mod.get('exp_max_dd_pct'),
    'agg_ret': agg.get('exp_return_pct'), 'agg_vol': agg.get('exp_vol_pct'), 'agg_dd': agg.get('exp_max_dd_pct'),
    'worst_mod': worst_mod, 'worst_agg': worst_agg, 'worst_name': worst_name, 'sleeves': sleeves,
    'n_matrix': len(matrix),
}

TEMPLATE = (HERE / 'report_template.html').read_text(encoding='utf-8')
page = (TEMPLATE
        .replace('__DOC_TITLE__', html.escape(doc_title))
        .replace('__BUILT__', built)
        .replace('__TOC__', toc_html)
        .replace('__PREAMBLE__', render_md(preamble_body) if preamble_body else '')
        .replace('__SECTIONS__', ''.join(section_html))
        .replace('__META_JSON__', json.dumps(META, ensure_ascii=False))
        .replace('__DATA_JSON__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')))
OUT_PATH.write_text(page, encoding='utf-8')
print(f'wrote {OUT_PATH} ({OUT_PATH.stat().st_size/1024:.0f} KB); sections={len(sections)}; matrix={len(matrix)}; stress={len(stress)}')
