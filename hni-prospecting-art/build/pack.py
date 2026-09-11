#!/usr/bin/env python3
"""Build the drop-in artwork pack.

    python3 hni-prospecting-art/build/pack.py

Writes the sprite (inline and standalone), the preview page, and nothing else.
Nothing here touches the briefing itself — the pack is additive by design.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import figures                                     # noqa: E402
from palette import AMBER, GROUND, GROUND_DEEP, defs   # noqa: E402

USE_SNIPPETS = [
    ("Overview", "fig-hero", "1000 560", "An adviser and a prospective client in conversation"),
    ("Who you're meeting", "fig-promoter", "400 500", "First-generation promoter"),
    ("Who you're meeting", "fig-executive", "400 500", "Senior corporate executive"),
    ("Who you're meeting", "fig-professional", "400 500", "Practice professional"),
    ("Who you're meeting", "fig-inheritor", "400 500", "Next-generation inheritor"),
    ("Who you're meeting", "fig-founder", "400 500", "Post-exit founder"),
    ("The engine", "fig-engine", "300 300", "The engine"),
    ("Trust", "fig-trust", "300 300", "Trust"),
    ("Watch-outs", "fig-watchouts", "300 300", "Watch-outs"),
    ("The week", "fig-week", "300 300", "The week"),
]


def sprite_body():
    return defs() + "\n" + "\n".join(figures.all_symbols())


def inline_sprite():
    return ('<!-- Ionic HNI prospecting figures. Paste this block once, anywhere in the\n'
            '     body. It renders nothing on its own and changes no layout; each figure\n'
            '     is then drawn with a single <use> tag. -->\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true"\n'
            '     style="position:absolute;width:0;height:0;overflow:hidden">\n'
            + sprite_body() + "\n</svg>\n")


def standalone_svg():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1">\n'
            + sprite_body() + "\n</svg>\n")


def _snippet(fid, vb, label):
    return (f'&lt;svg viewBox="0 0 {vb}" role="img" aria-label="{label}"&gt;\n'
            f'  &lt;use href="#{fid}"/&gt;\n&lt;/svg&gt;')


def preview():
    personas = "".join(f"""<figure class="card">
     <svg viewBox="0 0 400 500" role="img" aria-label="{p['name']}"><use href="#fig-{p['key']}"/></svg>
     <figcaption><b>{p['name']}</b><span>{p['note']}</span>
      <code>#fig-{p['key']}</code></figcaption></figure>""" for p in figures.PERSONAS)

    vigs = "".join(f"""<figure class="vig">
     <svg viewBox="0 0 300 300" role="img" aria-label="{k.replace('watchouts', 'Watch-outs').title()}"><use href="#fig-{k}"/></svg>
     <figcaption><b>{dict(engine='The engine', trust='Trust', watchouts='Watch-outs', week='The week')[k]}</b>
      <code>#fig-{k}</code></figcaption></figure>""" for k, _ in figures.VIGNETTES)

    rows = "".join(f"""<tr><td>{sec}</td><td><code>#{fid}</code></td>
      <td class="n">{vb.replace(' ', ' × ')}</td><td>{label}</td></tr>"""
                   for sec, fid, vb, label in USE_SNIPPETS)

    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>HNI Prospecting Figures</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600&family=Reddit+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--ground:{GROUND};--deep:{GROUND_DEEP};--amber:{AMBER};--ink:#EDEDFB;--mut:#A9A9DE;--line:rgba(255,255,255,.13)}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ground);color:var(--ink);
 font-family:'Reddit Sans',system-ui,Arial,sans-serif;font-size:14px;line-height:1.6;
 padding:0 20px 80px;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto}}
header{{padding:56px 0 10px;border-bottom:1px solid var(--line);margin-bottom:34px}}
.kicker{{font-size:11px;letter-spacing:2.6px;text-transform:uppercase;color:var(--amber);font-weight:700}}
h1{{font-family:'Newsreader',Georgia,serif;font-weight:600;font-size:clamp(30px,5vw,50px);
 line-height:1.06;margin:12px 0 10px;letter-spacing:-.5px}}
.lede{{color:var(--mut);max-width:64ch;font-size:15px}}
h2{{font-family:'Newsreader',Georgia,serif;font-size:23px;font-weight:600;margin:52px 0 4px}}
.sub{{color:var(--mut);font-size:12.5px;margin-bottom:20px;max-width:70ch}}
.hero svg{{width:100%;height:auto;border-radius:20px;display:block}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(196px,1fr));gap:20px}}
.vgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(216px,1fr));gap:20px}}
figure{{margin:0}}
figure svg{{width:100%;height:auto;border-radius:14px;display:block}}
figcaption{{padding:11px 2px 0;font-size:12px;line-height:1.5}}
figcaption b{{display:block;font-size:13px}}
figcaption span{{color:var(--mut);display:block;margin-bottom:5px}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px;
 background:rgba(0,0,0,.3);border:1px solid var(--line);border-radius:5px;padding:1.5px 6px;color:var(--amber)}}
pre{{background:rgba(0,0,0,.32);border:1px solid var(--line);border-radius:12px;padding:16px 18px;
 overflow-x:auto;font-size:12px;line-height:1.65;color:#DCDCF6}}
pre code{{background:none;border:0;padding:0;color:inherit;font-size:12px}}
table{{width:100%;border-collapse:collapse;font-size:12.5px;
 background:rgba(0,0,0,.18);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
th,td{{padding:8px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}
th{{font-size:10px;letter-spacing:.6px;text-transform:uppercase;color:var(--mut);font-weight:600}}
tr:last-child td{{border-bottom:0}}
.scroll{{overflow-x:auto}}
footer{{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);color:var(--mut);font-size:12px}}
</style></head>
<body>
{inline_sprite()}
<div class="wrap">
<header>
 <div class="kicker">Ionic Wealth by Angel One</div>
 <h1>HNI prospecting — figure set</h1>
 <p class="lede">Ten hand-built editorial figures for the prospecting briefing: a hero scene,
  five persona portraits and four section vignettes. Indigo duotone with a single amber accent
  each, drawn as inline SVG — fully owned, no licensing exposure, no external files, crisp at
  any size.</p>
</header>

<h2>Hero</h2>
<p class="sub">For the Overview. The briefing's own concentric-circle motif sits behind the
 figures, so the hero art and “circle of influence” rhyme instead of reading as two ideas.</p>
<div class="hero"><svg viewBox="0 0 1000 560" role="img"
 aria-label="An adviser and a prospective client in conversation across a low table"><use href="#fig-hero"/></svg></div>

<h2>Five personas</h2>
<p class="sub">Each is a distinct face shape, hair mass, eyewear and collar, so they stay
 separable at card size. Names are labels — remap any of them to your own five personas
 without redrawing anything.</p>
<div class="grid">{personas}</div>

<h2>Section vignettes</h2>
<p class="sub">Each draws the actual mechanism rather than a decorative icon.</p>
<div class="vgrid">{vigs}</div>

<h2>Dropping these into the briefing</h2>
<p class="sub">Two steps, and nothing existing changes. The sprite renders nothing on its own
 and defines no global CSS.</p>
<pre><code>&lt;!-- 1. paste the sprite block once, anywhere in the body --&gt;
&lt;svg width="0" height="0" aria-hidden="true" style="position:absolute;…"&gt;
  …figures…
&lt;/svg&gt;

&lt;!-- 2. place a figure wherever you want one --&gt;
{_snippet('fig-promoter', '400 500', 'First-generation promoter')}</code></pre>
<p class="sub">Size it with CSS — the figure is resolution-independent, so
 <code>width:100%;height:auto</code> is usually all it needs. Use
 <code>aria-hidden="true"</code> in place of <code>role</code>/<code>aria-label</code> for a
 figure that is purely decorative.</p>

<div class="scroll"><table>
 <thead><tr><th>Section</th><th>Symbol</th><th class="n">viewBox</th><th>Accessible name</th></tr></thead>
 <tbody>{rows}</tbody></table></div>

<footer>Ten figures, one shared defs block. Original artwork — no stock, no external requests.
 The page is built for this indigo ground; fills come from CSS custom properties, so a light
 ground is a token change rather than a redraw.</footer>
</div>
</body></html>
"""


def main():
    out = {
        "figures-inline.html": inline_sprite(),
        "figures.svg": standalone_svg(),
        "preview.html": preview(),
    }
    for name, body in out.items():
        path = os.path.join(ROOT, name)
        with open(path, "w") as fh:
            fh.write(body)
        print(f"wrote {os.path.relpath(path):44s} {len(body):>8,d} bytes")
    print(f"\n{len(figures.all_symbols())} figures")


if __name__ == "__main__":
    main()
