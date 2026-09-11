"""The ten figures: hero scene, five persona portraits, four section vignettes."""

from head import head
from palette import (AMBER, AMBER_DEEP, CLOTH, GROUND, GROUND_DARK, GROUND_DEEP,
                     HAIR, SKIN)

# ---------------------------------------------------------------------------
# shared bits
# ---------------------------------------------------------------------------

def _bg(w, h, clip):
    return (f'<rect width="{w}" height="{h}" fill="{GROUND_DEEP}"/>'
            f'<rect width="{w}" height="{h}" fill="url(#ig-vig)"/>')


def _neck(cx, top, skin, width=25, drop=26):
    """Neck plus the jaw shadow that does most of the work of not looking flat."""
    return f"""<path d="M {cx - width:.0f},{top:.0f} C {cx - width - 2:.0f},{top + drop * .6:.0f} {cx - width - 6:.0f},{top + drop:.0f} {cx - width - 10:.0f},{top + drop + 8:.0f}
   L {cx + width + 10:.0f},{top + drop + 8:.0f} C {cx + width + 6:.0f},{top + drop:.0f} {cx + width + 2:.0f},{top + drop * .6:.0f} {cx + width:.0f},{top:.0f} Z"
   fill="{skin['base']}"/>
  <path d="M {cx - width:.0f},{top:.0f} C {cx - width - 2:.0f},{top + drop * .6:.0f} {cx - width - 6:.0f},{top + drop:.0f} {cx - width - 10:.0f},{top + drop + 8:.0f}
   L {cx + width + 10:.0f},{top + drop + 8:.0f} C {cx + width + 6:.0f},{top + drop:.0f} {cx + width + 2:.0f},{top + drop * .6:.0f} {cx + width:.0f},{top:.0f} Z"
   fill="url(#ig-model)"/>
  <path d="M {cx - width:.0f},{top:.0f} C {cx - 16:.0f},{top + 20:.0f} {cx + 16:.0f},{top + 22:.0f} {cx + width:.0f},{top + 2:.0f}
   C {cx + 20:.0f},{top + 32:.0f} {cx - 20:.0f},{top + 32:.0f} {cx - width:.0f},{top:.0f} Z"
   fill="{skin['deep']}" opacity=".42"/>"""


def _shoulders(cx, top, bottom, half, slope, cloth, frame_w):
    """Torso silhouette. `half` sets build, `slope` sets how square the shoulders read."""
    inner = half * .42
    return f"""<path d="M {cx:.0f},{top:.0f}
   C {cx - inner:.0f},{top:.0f} {cx - half * .62:.0f},{top + slope * .34:.0f} {cx - half * .78:.0f},{top + slope:.0f}
   C {cx - half * .96:.0f},{top + slope + 26:.0f} {cx - half:.0f},{top + slope + 64:.0f} {cx - half - 6:.0f},{bottom:.0f}
   L {cx + half + 6:.0f},{bottom:.0f}
   C {cx + half:.0f},{top + slope + 64:.0f} {cx + half * .96:.0f},{top + slope + 26:.0f} {cx + half * .78:.0f},{top + slope:.0f}
   C {cx + half * .62:.0f},{top + slope * .34:.0f} {cx + inner:.0f},{top:.0f} {cx:.0f},{top:.0f} Z"
   fill="{cloth['base']}"/>
  <path d="M {cx - half * .78:.0f},{top + slope:.0f} C {cx - half * .96:.0f},{top + slope + 26:.0f} {cx - half:.0f},{top + slope + 64:.0f} {cx - half - 6:.0f},{bottom:.0f}
   L {cx - half * .34:.0f},{bottom:.0f} C {cx - half * .5:.0f},{top + slope + 50:.0f} {cx - half * .62:.0f},{top + slope + 14:.0f} {cx - half * .78:.0f},{top + slope:.0f} Z"
   fill="{cloth['shade']}" opacity=".8"/>
  <path d="M {cx + half * .5:.0f},{top + slope + 6:.0f} C {cx + half * .84:.0f},{top + slope + 30:.0f} {cx + half * .9:.0f},{top + slope + 70:.0f} {cx + half * .92:.0f},{bottom:.0f}
   L {cx + half + 6:.0f},{bottom:.0f} C {cx + half:.0f},{top + slope + 60:.0f} {cx + half * .94:.0f},{top + slope + 22:.0f} {cx + half * .78:.0f},{top + slope:.0f} Z"
   fill="{cloth['lit']}" opacity=".55"/>"""


def _collar(kind, cx, top, skin, cloth, accent=AMBER):
    """Collar and neckline — a big share of what separates one persona from another."""
    if kind == "open":          # open-neck shirt, no tie
        return f"""<path d="M {cx - 34:.0f},{top - 2:.0f} C {cx - 26:.0f},{top + 34:.0f} {cx - 10:.0f},{top + 54:.0f} {cx:.0f},{top + 58:.0f}
     C {cx + 10:.0f},{top + 54:.0f} {cx + 26:.0f},{top + 34:.0f} {cx + 34:.0f},{top - 2:.0f}
     C {cx + 20:.0f},{top + 6:.0f} {cx - 20:.0f},{top + 6:.0f} {cx - 34:.0f},{top - 2:.0f} Z" fill="{skin['shade']}" opacity=".85"/>
   <path d="M {cx - 44:.0f},{top - 8:.0f} L {cx - 6:.0f},{top + 30:.0f} L {cx - 22:.0f},{top + 44:.0f} L {cx - 54:.0f},{top + 14:.0f} Z" fill="{cloth['lit']}"/>
   <path d="M {cx + 44:.0f},{top - 8:.0f} L {cx + 6:.0f},{top + 30:.0f} L {cx + 22:.0f},{top + 44:.0f} L {cx + 54:.0f},{top + 14:.0f} Z" fill="{cloth['base']}"/>"""
    if kind == "suit_tie":
        return f"""<path d="M {cx - 30:.0f},{top - 4:.0f} C {cx - 22:.0f},{top + 22:.0f} {cx - 9:.0f},{top + 34:.0f} {cx:.0f},{top + 36:.0f}
     C {cx + 9:.0f},{top + 34:.0f} {cx + 22:.0f},{top + 22:.0f} {cx + 30:.0f},{top - 4:.0f} Z" fill="{CLOTH['white']['base']}"/>
   <path d="M {cx - 52:.0f},{top + 2:.0f} L {cx - 4:.0f},{top + 40:.0f} L {cx - 30:.0f},{top + 96:.0f} L {cx - 74:.0f},{top + 40:.0f} Z" fill="{cloth['lit']}"/>
   <path d="M {cx + 52:.0f},{top + 2:.0f} L {cx + 4:.0f},{top + 40:.0f} L {cx + 30:.0f},{top + 96:.0f} L {cx + 74:.0f},{top + 40:.0f} Z" fill="{cloth['shade']}"/>
   <path d="M {cx - 11:.0f},{top + 34:.0f} L {cx + 11:.0f},{top + 34:.0f} L {cx + 15:.0f},{top + 50:.0f} L {cx:.0f},{top + 60:.0f} L {cx - 15:.0f},{top + 50:.0f} Z" fill="{accent}"/>
   <path d="M {cx - 9:.0f},{top + 56:.0f} L {cx + 9:.0f},{top + 56:.0f} L {cx + 13:.0f},{top + 130:.0f} L {cx:.0f},{top + 146:.0f} L {cx - 13:.0f},{top + 130:.0f} Z" fill="{AMBER_DEEP}"/>"""
    if kind == "highneck":      # high-necked kurta / blouse
        return f"""<path d="M {cx - 30:.0f},{top - 6:.0f} C {cx - 24:.0f},{top + 12:.0f} {cx - 10:.0f},{top + 20:.0f} {cx:.0f},{top + 21:.0f}
     C {cx + 10:.0f},{top + 20:.0f} {cx + 24:.0f},{top + 12:.0f} {cx + 30:.0f},{top - 6:.0f}
     C {cx + 36:.0f},{top + 16:.0f} {cx + 20:.0f},{top + 32:.0f} {cx:.0f},{top + 32:.0f}
     C {cx - 20:.0f},{top + 32:.0f} {cx - 36:.0f},{top + 16:.0f} {cx - 30:.0f},{top - 6:.0f} Z" fill="{cloth['lit']}"/>
   <path d="M {cx - 30:.0f},{top + 26:.0f} C {cx - 14:.0f},{top + 38:.0f} {cx + 14:.0f},{top + 38:.0f} {cx + 30:.0f},{top + 26:.0f}"
     fill="none" stroke="{accent}" stroke-width="3" opacity=".9"/>"""
    if kind == "crew_jacket":
        return f"""<path d="M {cx - 32:.0f},{top - 2:.0f} C {cx - 24:.0f},{top + 26:.0f} {cx - 10:.0f},{top + 38:.0f} {cx:.0f},{top + 40:.0f}
     C {cx + 10:.0f},{top + 38:.0f} {cx + 24:.0f},{top + 26:.0f} {cx + 32:.0f},{top - 2:.0f} Z" fill="{CLOTH['linen']['base']}"/>
   <path d="M {cx - 34:.0f},{top + 2:.0f} C {cx - 26:.0f},{top + 30:.0f} {cx - 11:.0f},{top + 44:.0f} {cx:.0f},{top + 46:.0f}
     C {cx + 11:.0f},{top + 44:.0f} {cx + 26:.0f},{top + 30:.0f} {cx + 34:.0f},{top + 2:.0f}"
     fill="none" stroke="{CLOTH['linen']['shade']}" stroke-width="2.4" opacity=".7"/>
   <path d="M {cx - 56:.0f},{top + 6:.0f} L {cx - 16:.0f},{top + 44:.0f} L {cx - 40:.0f},{top + 120:.0f} L {cx - 78:.0f},{top + 44:.0f} Z" fill="{cloth['lit']}"/>
   <path d="M {cx + 56:.0f},{top + 6:.0f} L {cx + 16:.0f},{top + 44:.0f} L {cx + 40:.0f},{top + 120:.0f} L {cx + 78:.0f},{top + 44:.0f} Z" fill="{cloth['shade']}"/>
   <circle cx="{cx + 42:.0f}" cy="{top + 30:.0f}" r="4.6" fill="{accent}"/>"""
    if kind == "hoodie":
        return f"""<path d="M {cx - 34:.0f},{top - 4:.0f} C {cx - 26:.0f},{top + 26:.0f} {cx - 11:.0f},{top + 40:.0f} {cx:.0f},{top + 42:.0f}
     C {cx + 11:.0f},{top + 40:.0f} {cx + 26:.0f},{top + 26:.0f} {cx + 34:.0f},{top - 4:.0f} Z" fill="{skin['shade']}" opacity=".8"/>
   <path d="M {cx - 58:.0f},{top - 4:.0f} C {cx - 44:.0f},{top + 34:.0f} {cx - 22:.0f},{top + 54:.0f} {cx - 4:.0f},{top + 58:.0f}
     L {cx - 4:.0f},{top + 74:.0f} C {cx - 30:.0f},{top + 68:.0f} {cx - 56:.0f},{top + 42:.0f} {cx - 70:.0f},{top + 6:.0f} Z" fill="{cloth['lit']}"/>
   <path d="M {cx + 58:.0f},{top - 4:.0f} C {cx + 44:.0f},{top + 34:.0f} {cx + 22:.0f},{top + 54:.0f} {cx + 4:.0f},{top + 58:.0f}
     L {cx + 4:.0f},{top + 74:.0f} C {cx + 30:.0f},{top + 68:.0f} {cx + 56:.0f},{top + 42:.0f} {cx + 70:.0f},{top + 6:.0f} Z" fill="{cloth['shade']}"/>
   <path d="M {cx - 26:.0f},{top + 16:.0f} C {cx - 14:.0f},{top + 74:.0f} {cx + 14:.0f},{top + 74:.0f} {cx + 26:.0f},{top + 16:.0f}"
     fill="none" stroke="{accent}" stroke-width="3.4" stroke-linecap="round"/>"""
    return ""


# ---------------------------------------------------------------------------
# five persona portraits
# ---------------------------------------------------------------------------
# Distinctness is carried by build, hair mass, eyewear, collar and tilt, so the
# five stay separable at card size where facial detail stops resolving.

PERSONAS = [
    dict(key="promoter", name="First-generation promoter",
         note="Built the business. Trusts people, not brochures.",
         skin="olive", hair="salt", cloth="linen", collar="open",
         face="square", hairstyle="sweptback", turn=-12, tilt=-3, scale=1.02,
         half=186, slope=40, brow="heavy", arch=.35, eyes="narrow",
         mouth="firm", glasses=None, moustache=True, age_lines=True,
         accent="pocket-pen"),
    dict(key="executive", name="Senior corporate executive",
         note="RSU- and ESOP-heavy. Optimises, compares, decides on paper.",
         skin="warm", hair="dark", cloth="deepblue", collar="suit_tie",
         face="oval", hairstyle="sidepart", turn=-10, tilt=1, scale=0.96,
         half=163, slope=31, brow="medium", arch=.5, eyes="calm",
         mouth="neutral", glasses="rect", age_lines=False, accent=None),
    dict(key="professional", name="Practice professional",
         note="Doctor, lawyer or CA. Time-poor, referral-driven.",
         skin="mid", hair="jet", cloth="indigo", collar="highneck",
         face="heart", hairstyle="bun", turn=-13, tilt=2, scale=0.95,
         half=150, slope=37, brow="fine", arch=.72, eyes="warm",
         mouth="warm", glasses=None, earring=AMBER, accent=None),
    dict(key="inheritor", name="Next-generation inheritor",
         note="Family wealth, own views. Wants to be taken seriously.",
         skin="light", hair="jet", cloth="charcoal", collar="crew_jacket",
         face="long", hairstyle="tousled", turn=-14, tilt=-4, scale=0.98,
         half=168, slope=46, brow="medium", arch=.58, eyes="calm",
         mouth="warm", glasses=None, accent=None),
    dict(key="founder", name="Post-exit founder",
         note="Liquidity event just landed. Moves fast, asks hard questions.",
         skin="deep", hair="jet", cloth="indigo", collar="hoodie",
         face="round", hairstyle="crop", turn=-11, tilt=3, scale=0.97,
         half=172, slope=35, brow="heavy", arch=.42, eyes="calm",
         mouth="wide", glasses="round", glasses_accent=AMBER,
         stubble=True, accent=None),
]


def _accent(kind, cx, top, cloth):
    if kind == "pocket-pen":
        return (f'<path d="M {cx + 66:.0f},{top + 96:.0f} L {cx + 104:.0f},{top + 96:.0f} L {cx + 100:.0f},{top + 136:.0f} L {cx + 70:.0f},{top + 136:.0f} Z"'
                f' fill="{cloth["shade"]}" opacity=".75"/>'
                f'<rect x="{cx + 80:.0f}" y="{top + 82:.0f}" width="7" height="26" rx="3.5" fill="{AMBER}"/>')
    return ""


def portrait(p):
    skin, hair, cloth = SKIN[p["skin"]], HAIR[p["hair"]], CLOTH[p["cloth"]]
    cx, hy = 200, 186
    behind, front = head(
        skin, hair, face=p["face"], turn=p["turn"], hairstyle=p["hairstyle"], brow=p["brow"],
        arch=p["arch"], eyes=p["eyes"], mouth=p["mouth"], glasses=p.get("glasses"),
        glasses_accent=p.get("glasses_accent"), moustache=p.get("moustache", False),
        stubble=p.get("stubble", False), age_lines=p.get("age_lines", False),
        earring=p.get("earring"))
    s, neck_top = p["scale"], hy + 79 * p["scale"] - 16
    tf = f'translate({cx},{hy}) rotate({p["tilt"]}) scale({s})'
    return f"""<symbol id="fig-{p['key']}" viewBox="0 0 400 500">
 <title>{p['name']}</title>
 <desc>Illustrated three-quarter portrait of a {p['name'].lower()} — {p['note']}</desc>
 <g clip-path="url(#ig-frame)" style="--sk-deep:{skin['deep']};--sk-shade:{skin['shade']};--sk-lit:{skin['lit']}">
  {_bg(400, 500, 'ig-frame')}
  <g filter="url(#ig-tooth)">
   <ellipse cx="{cx}" cy="{hy - 6}" rx="104" ry="122" fill="{GROUND}" opacity=".26" filter="url(#ig-soft)"/>
   <g transform="{tf}">{behind}</g>
   {_neck(cx, neck_top, skin)}
   <g transform="{tf}">{front}</g>
   {_shoulders(cx, neck_top + 38, 500, p['half'], p['slope'], cloth, 400)}
   {_collar(p['collar'], cx, neck_top + 36, skin, cloth)}
   {_accent(p.get('accent'), cx, neck_top + 38, cloth)}
  </g>
 </g>
</symbol>"""


# ---------------------------------------------------------------------------
# hero scene
# ---------------------------------------------------------------------------

def hero():
    """Two figures across a low table, with the briefing's own concentric-circle
    motif behind them so the hero art and 'circle of influence' rhyme rather
    than sitting as two unrelated ideas."""
    rings = "".join(
        f'<circle cx="500" cy="214" r="{r}" fill="none" stroke="{AMBER}" '
        f'stroke-width="{1.2 if i == 1 else .8}" opacity="{.30 - i * .05:.2f}"/>'
        for i, r in enumerate((104, 168, 238, 312)))

    left_skin, left_hair, left_cloth = SKIN["warm"], HAIR["dark"], CLOTH["indigo"]
    right_skin, right_hair, right_cloth = SKIN["olive"], HAIR["salt"], CLOTH["linen"]

    # the adviser, turned toward the client; the client, turned back toward them
    lb, lf = head(left_skin, left_hair, face="oval", turn=8, hairstyle="sidepart",
                  brow="medium", arch=.5, eyes="calm", mouth="warm")
    rb, rf = head(right_skin, right_hair, face="square", turn=-13, hairstyle="sweptback",
                  brow="heavy", arch=.35, eyes="narrow", mouth="neutral",
                  moustache=True, age_lines=True)
    ls, rs = .80, .84

    def figure(cx, hy, sc, skin, cloth, back, front, half, collar):
        nt = hy + 79 * sc - 14
        tf = f"translate({cx},{hy}) scale({sc})"
        return f"""<g style="--sk-deep:{skin['deep']};--sk-shade:{skin['shade']};--sk-lit:{skin['lit']}">
    <g transform="{tf}">{back}</g>
    {_neck(cx, nt, skin, 22, 24)}
    <g transform="{tf}">{front}</g>
    {_shoulders(cx, nt + 34, 560, half, 34, cloth, 1000)}
    {_collar(collar, cx, nt + 32, skin, cloth)}
   </g>"""

    return f"""<symbol id="fig-hero" viewBox="0 0 1000 560">
 <title>An adviser and a prospective client in conversation</title>
 <desc>Illustrated scene: two figures seated across a low table, one leaning in,
  concentric circles behind them standing for a widening circle of influence.</desc>
 <g clip-path="url(#ig-wide)">
  <rect width="1000" height="560" fill="{GROUND_DEEP}"/>
  <rect width="1000" height="560" fill="url(#ig-vig)"/>
  {rings}
  <ellipse cx="500" cy="228" rx="316" ry="188" fill="{GROUND}" opacity=".22" filter="url(#ig-soft)"/>
  <g filter="url(#ig-tooth)">
   {figure(352, 208, ls, left_skin, left_cloth, lb, lf, 146, "suit_tie")}
   {figure(652, 200, rs, right_skin, right_cloth, rb, rf, 156, "open")}
   <!-- the table reads as a plane the figures sit behind, not a stripe -->
   <path d="M 108,486 L 892,486 L 916,560 L 84,560 Z" fill="{GROUND_DARK}"/>
   <path d="M 108,486 L 892,486 L 895,498 L 105,498 Z" fill="{CLOTH['deepblue']['lit']}" opacity=".9"/>
   <g>
    <path d="M 392,450 L 442,450 L 436,482 L 398,482 Z" fill="{AMBER}"/>
    <path d="M 442,458 C 454,458 454,472 442,472" fill="none" stroke="{AMBER_DEEP}" stroke-width="3"/>
    <ellipse cx="417" cy="450" rx="25" ry="5" fill="{AMBER_DEEP}" opacity=".8"/>
   </g>
   <g>
    <path d="M 596,456 L 638,456 L 633,482 L 601,482 Z" fill="{CLOTH['white']['base']}"/>
    <ellipse cx="617" cy="456" rx="21" ry="4.6" fill="{CLOTH['white']['shade']}"/>
   </g>
   <!-- a single sheet on the table: the proposition, which is the point -->
   <path d="M 462,468 L 576,460 L 583,482 L 469,490 Z" fill="{CLOTH['white']['base']}" opacity=".92"/>
   <path d="M 480,472 L 558,467 M 482,479 L 550,474" stroke="{GROUND_DARK}" stroke-width="1.6" opacity=".45"/>
  </g>
 </g>
</symbol>"""


# ---------------------------------------------------------------------------
# four section vignettes — each draws the mechanism, not a decorative icon
# ---------------------------------------------------------------------------

def _mini_figure(x, y, sc, skin, cloth, hair, back=False):
    """A small full bust for the vignettes, where a face would be too fine to
    resolve. `back` turns the figure away, for the fork-in-the-path scene."""
    face = "" if back else f"""
    <path d="M -44,-50 C -44,-76 -26,-96 -2,-96 C -18,-76 -24,-46 -18,-16 C -30,-22 -44,-34 -44,-50 Z" fill="{skin['shade']}" opacity=".5"/>
    <path d="M -25,-58 C -21,-63 -11,-63 -7,-58 C -11,-53 -21,-53 -25,-58 Z" fill="#EFE7DA"/>
    <path d="M 7,-58 C 11,-63 21,-63 25,-58 C 21,-53 11,-53 7,-58 Z" fill="#EFE7DA"/>
    <circle cx="-16" cy="-58" r="4" fill="#2B2418"/><circle cx="16" cy="-58" r="4" fill="#2B2418"/>
    <path d="M -26,-70 C -20,-74 -10,-74 -5,-71" fill="none" stroke="{hair['base']}" stroke-width="4" stroke-linecap="round"/>
    <path d="M 5,-71 C 10,-74 20,-74 26,-70" fill="none" stroke="{hair['base']}" stroke-width="4" stroke-linecap="round"/>
    <path d="M -2,-50 C -5,-44 -7,-38 -3,-35" fill="none" stroke="{skin['deep']}" stroke-width="2.6" opacity=".45" stroke-linecap="round"/>
    <path d="M -11,-27 C -4,-24 5,-24 12,-28" fill="none" stroke="{skin['deep']}" stroke-width="3" opacity=".6" stroke-linecap="round"/>"""
    return f"""<g transform="translate({x},{y}) scale({sc})">
    <path d="M 0,-96 C 26,-96 44,-76 44,-50 C 44,-26 26,-8 0,-8 C -26,-8 -44,-26 -44,-50 C -44,-76 -26,-96 0,-96 Z" fill="{skin['base']}"/>{face}
    <path d="M 0,-104 C 30,-104 50,-82 50,-54 C 40,-74 22,-86 0,-86 C -22,-86 -40,-74 -50,-54 C -50,-82 -30,-104 0,-104 Z" fill="{hair['base']}"/>
    <path d="M 0,-10 C 42,-10 76,20 82,72 L -82,72 C -76,20 -42,-10 0,-10 Z" fill="{cloth['base']}"/>
    <path d="M -82,72 C -76,20 -42,-10 -2,-10 C -26,10 -40,38 -44,72 Z" fill="{cloth['shade']}" opacity=".8"/>
   </g>"""


def engine():
    """A geared flywheel: the mechanism itself, no hand needed."""
    import math
    spokes = "".join(
        f'<path d="M 118,150 L {118 + 56 * math.cos(math.radians(a)):.1f},{150 + 56 * math.sin(math.radians(a)):.1f}" '
        f'stroke="{CLOTH["deepblue"]["lit"]}" stroke-width="8" stroke-linecap="round"/>'
        for a in (14, 86, 158, 230, 302))
    teeth = "".join(
        f'<rect x="{226 - 5.5:.1f}" y="{98 - 7:.1f}" width="11" height="14" rx="2.5" '
        f'fill="{CLOTH["deepblue"]["base"]}" transform="rotate({a} 226 148)"/>'
        for a in range(0, 360, 30))
    return f"""<symbol id="fig-engine" viewBox="0 0 300 300">
 <title>The engine</title>
 <desc>Illustrated vignette: a heavy flywheel geared to a smaller wheel, turning under its own momentum — the prospecting engine.</desc>
 <g clip-path="url(#ig-sq)">
  <rect width="300" height="300" fill="{GROUND_DEEP}"/><rect width="300" height="300" fill="url(#ig-vig)"/>
  <g filter="url(#ig-tooth)">
   <circle cx="226" cy="148" r="50" fill="{GROUND_DARK}"/>
   {teeth}
   <circle cx="226" cy="148" r="38" fill="{CLOTH['deepblue']['lit']}" opacity=".55"/>
   <circle cx="226" cy="148" r="13" fill="{GROUND_DARK}"/>
   <circle cx="118" cy="150" r="78" fill="none" stroke="{GROUND_DARK}" stroke-width="24"/>
   <circle cx="118" cy="150" r="78" fill="none" stroke="{CLOTH['deepblue']['base']}" stroke-width="16"/>
   <path d="M 118,72 A 78,78 0 0 1 196,150" fill="none" stroke="{AMBER}" stroke-width="16" stroke-linecap="round"/>
   {spokes}
   <circle cx="118" cy="150" r="20" fill="{CLOTH['deepblue']['lit']}"/>
   <circle cx="118" cy="150" r="9" fill="{GROUND_DARK}"/>
   <path d="M 118,42 A 108,108 0 0 1 212,96" fill="none" stroke="{AMBER}" stroke-width="3.4"
     stroke-linecap="round" stroke-dasharray="16 11" opacity=".85"/>
   <path d="M 206,86 L 216,98 L 201,101 Z" fill="{AMBER}"/>
   <path d="M 118,258 A 108,108 0 0 1 26,206" fill="none" stroke="{AMBER}" stroke-width="2.6"
     stroke-linecap="round" stroke-dasharray="13 10" opacity=".45"/>
  </g>
 </g>
</symbol>"""


def trust():
    """A signed undertaking passing between two parties."""
    a, b = SKIN["olive"], SKIN["light"]
    return f"""<symbol id="fig-trust" viewBox="0 0 300 300">
 <title>Trust</title>
 <desc>Illustrated vignette: a signed undertaking standing between two people — trust given, not claimed.</desc>
 <g clip-path="url(#ig-sq)">
  <rect width="300" height="300" fill="{GROUND_DEEP}"/><rect width="300" height="300" fill="url(#ig-vig)"/>
  <g filter="url(#ig-tooth)">
   <g style="--sk-deep:{a['deep']};--sk-shade:{a['shade']};--sk-lit:{a['lit']}" opacity=".92">
    {_mini_figure(46, 252, .60, a, CLOTH['indigo'], HAIR['jet'])}
   </g>
   <g style="--sk-deep:{b['deep']};--sk-shade:{b['shade']};--sk-lit:{b['lit']}" opacity=".92">
    {_mini_figure(254, 248, .60, b, CLOTH['linen'], HAIR['salt'])}
   </g>
   <!-- the second sheet offset behind the first: a document changing hands -->
   <g transform="rotate(5 150 138)">
    <path d="M 104,58 L 208,58 L 208,196 L 104,196 Z" fill="{CLOTH['white']['shade']}" opacity=".55"/>
   </g>
   <g transform="rotate(-4 150 134)">
    <path d="M 96,54 L 204,54 L 204,194 L 96,194 Z" fill="{CLOTH['white']['base']}"/>
    <path d="M 96,54 L 204,54 L 204,70 L 96,70 Z" fill="{CLOTH['white']['shade']}" opacity=".7"/>
    <path d="M 110,92 L 190,92 M 110,110 L 190,110 M 110,128 L 164,128" stroke="{GROUND_DARK}"
      stroke-width="4.2" opacity=".32" stroke-linecap="round"/>
    <path d="M 110,162 C 122,150 132,174 144,162 C 154,152 162,170 174,160" fill="none"
      stroke="{GROUND_DEEP}" stroke-width="3.8" stroke-linecap="round"/>
    <circle cx="182" cy="174" r="14" fill="{AMBER}"/>
    <circle cx="182" cy="174" r="7.5" fill="none" stroke="{AMBER_DEEP}" stroke-width="2.4"/>
   </g>
   <path d="M 70,150 L 88,150 M 212,150 L 230,150" stroke="{AMBER}" stroke-width="3"
     stroke-linecap="round" opacity=".7"/>
  </g>
 </g>
</symbol>"""


def watchouts():
    """Two routes out of one decision. Tapered ribbons read as blobs at this
    size, so this is drawn as a diagram — the same register as the gears and
    the week grid."""
    return f"""<symbol id="fig-watchouts" viewBox="0 0 300 300">
 <title>Watch-outs</title>
 <desc>Illustrated vignette: one decision with two routes out — one open and lit, the other flagged with a warning.</desc>
 <g clip-path="url(#ig-sq)">
  <rect width="300" height="300" fill="{GROUND_DEEP}"/><rect width="300" height="300" fill="url(#ig-vig)"/>
  <g filter="url(#ig-tooth)">
   <path d="M 150,286 L 150,212" stroke="{AMBER}" stroke-width="3.4" stroke-dasharray="13 10"
     stroke-linecap="round" opacity=".5"/>
   <path d="M 150,192 L 236,106" stroke="{AMBER}" stroke-width="13" stroke-linecap="round"/>
   <path d="M 252,92 L 230,95 L 249,114 Z" fill="{AMBER}"/>
   <path d="M 150,192 L 68,118" stroke="{CLOTH['deepblue']['lit']}" stroke-width="13" stroke-linecap="round" opacity=".85"/>
   <path d="M 52,104 L 74,110 L 57,127 Z" fill="{CLOTH['deepblue']['lit']}" opacity=".85"/>
   <circle cx="150" cy="196" r="15" fill="{GROUND_DEEP}"/>
   <circle cx="150" cy="196" r="9" fill="{AMBER}"/>
   <circle cx="150" cy="196" r="19" fill="none" stroke="{AMBER}" stroke-width="2" opacity=".4"/>
   <g transform="translate(96,84)">
    <path d="M 0,-19 L 16,9 L -16,9 Z" fill="{AMBER}"/>
    <rect x="-1.7" y="-10" width="3.4" height="11" rx="1.7" fill="{GROUND_DARK}"/>
    <circle cx="0" cy="4.5" r="2" fill="{GROUND_DARK}"/>
   </g>
   <circle cx="244" cy="150" r="4" fill="{AMBER}" opacity=".55"/>
   <circle cx="258" cy="132" r="2.6" fill="{AMBER}" opacity=".38"/>
  </g>
 </g>
</symbol>"""


def week():
    cols, marks = [], []
    for i, (lab, filled) in enumerate([("M", 3), ("T", 4), ("W", 2), ("T", 4), ("F", 1)]):
        x = 30 + i * 50
        live = i == 2
        cols.append(f'<rect x="{x}" y="70" width="36" height="184" rx="7" '
                    f'fill="{AMBER if live else CLOTH["deepblue"]["base"]}" opacity="{.16 if live else .5}"/>')
        cols.append(f'<text x="{x + 18}" y="60" text-anchor="middle" font-family="Georgia,serif" '
                    f'font-size="15" fill="{AMBER if live else "#9E9EDA"}">{lab}</text>')
        for j in range(filled):
            y = 92 + j * 40
            c = AMBER if live else CLOTH["indigo"]["lit"]
            marks.append(f'<circle cx="{x + 18}" cy="{y}" r="8.5" fill="{c}"/>'
                         f'<path d="M {x + 18 - 13},{y + 26} C {x + 18 - 11},{y + 12} {x + 18 + 11},{y + 12} {x + 18 + 13},{y + 26} Z" fill="{c}" opacity=".8"/>')
    return f"""<symbol id="fig-week" viewBox="0 0 300 300">
 <title>The week</title>
 <desc>Illustrated vignette: a week laid out as five columns with meetings placed across it, today's column lit.</desc>
 <g clip-path="url(#ig-sq)">
  <rect width="300" height="300" fill="{GROUND_DEEP}"/><rect width="300" height="300" fill="url(#ig-vig)"/>
  <g filter="url(#ig-tooth)">
   {"".join(cols)}
   {"".join(marks)}
   <path d="M 22,268 L 278,268" stroke="{AMBER}" stroke-width="2" opacity=".5"/>
  </g>
 </g>
</symbol>"""


VIGNETTES = [("engine", engine), ("trust", trust),
             ("watchouts", watchouts), ("week", week)]


def all_symbols():
    return ([hero()] + [portrait(p) for p in PERSONAS]
            + [fn() for _, fn in VIGNETTES])
