"""Head construction, shared by every figure.

One proportion grid and one key light (upper-left) for all ten drawings. The
five portraits differ by silhouette — hair mass, eyewear, collar, build, head
tilt — not by nudging the face around, which is what keeps the set coherent.

Local coordinates: origin at head centre, +x right, +y down.
Head half-width 58, half-height 79. `turn` shifts the features to read as a
three-quarter view; the far side of the face carries the shadow plane.
"""

# Five face shapes so the set reads as five people, not one face restyled.
# Outlines are duplicated as clipPaths in palette.defs(); keep them in step.
FACES = {
    "square": ("M 0,-80 C 36,-80 59,-56 60,-20 C 61,10 56,34 44,52 C 34,66 18,76 0,76 "
               "C -18,76 -34,66 -44,50 C -56,32 -59,10 -59,-20 C -59,-56 -36,-80 0,-80 Z", 60, 76),
    "oval":   ("M 0,-80 C 34,-80 57,-56 58,-20 C 59,12 50,40 30,60 C 19,71 9,78 0,78 "
               "C -11,78 -23,68 -35,53 C -52,33 -57,10 -57,-20 C -57,-56 -34,-80 0,-80 Z", 58, 78),
    "heart":  ("M 0,-80 C 36,-80 58,-54 58,-18 C 58,14 46,42 24,62 C 14,72 6,78 0,78 "
               "C -7,78 -16,71 -27,60 C -48,40 -58,14 -58,-18 C -58,-54 -36,-80 0,-80 Z", 58, 78),
    "long":   ("M 0,-82 C 30,-82 52,-58 53,-22 C 54,14 46,44 28,64 C 18,75 8,82 0,82 "
               "C -9,82 -20,72 -31,58 C -47,38 -52,12 -52,-22 C -52,-58 -30,-82 0,-82 Z", 53, 82),
    "round":  ("M 0,-78 C 36,-78 60,-54 61,-18 C 62,10 54,32 38,50 C 26,63 12,71 0,71 "
               "C -13,71 -27,63 -39,49 C -55,31 -60,10 -60,-18 C -60,-54 -36,-78 0,-78 Z", 61, 71),
}

EYE_Y = -10          # eyeline sits just above head centre
BROW_Y = -30
NOSE_TIP_Y = 20
MOUTH_Y = 40


def _almond(cx, cy, w, h):
    return (f"M {cx - w:.1f},{cy:.1f} "
            f"C {cx - w * .55:.1f},{cy - h * 1.28:.1f} {cx + w * .55:.1f},{cy - h * 1.28:.1f} {cx + w:.1f},{cy:.1f} "
            f"C {cx + w * .5:.1f},{cy + h * .98:.1f} {cx - w * .5:.1f},{cy + h * .98:.1f} {cx - w:.1f},{cy:.1f} Z")


def _lid(cx, cy, w, h):
    """The upper lid as a filled crescent — a stroke reads mechanical here."""
    return (f"M {cx - w:.1f},{cy:.1f} "
            f"C {cx - w * .55:.1f},{cy - h * 1.28:.1f} {cx + w * .55:.1f},{cy - h * 1.28:.1f} {cx + w:.1f},{cy:.1f} "
            f"C {cx + w * .5:.1f},{cy - h * .62:.1f} {cx - w * .5:.1f},{cy - h * .62:.1f} {cx - w:.1f},{cy:.1f} Z")


def _eye(cx, far, skin, hair, kind="calm"):
    """One eye: socket, sclera, iris, catchlight, lid. Modest scale on purpose —
    oversized eyes are the single fastest way to turn editorial into cartoon."""
    w, h = (9.5, 5.3) if not far else (7.5, 4.5)
    if kind == "warm":
        h *= 1.06
    if kind == "narrow":
        h *= .84
    o = .9 if far else 1
    return f"""<g opacity="{o}">
   <path d="{_almond(cx, EYE_Y, w + 1.6, h + 1.3)}" fill="{skin['shade']}" opacity=".38"/>
   <path d="{_almond(cx, EYE_Y, w, h)}" fill="#EFE7DA"/>
   <circle cx="{cx + (1.2 if far else -.6):.1f}" cy="{EYE_Y + .6:.1f}" r="{h * .86:.1f}" fill="#2B2418"/>
   <circle cx="{cx + (1.2 if far else -.6) - 1.5:.1f}" cy="{EYE_Y - 1.3:.1f}" r="1.35" fill="#FFFFFF" opacity=".9"/>
   <path d="{_lid(cx, EYE_Y, w, h)}" fill="{hair['base']}"/>
   <path d="M {cx - w * .8:.1f},{EYE_Y + h * .95:.1f} C {cx:.1f},{EYE_Y + h * 1.35:.1f} {cx + w * .6:.1f},{EYE_Y + h * 1.1:.1f} {cx + w * .85:.1f},{EYE_Y + h * .7:.1f}"
     fill="none" stroke="{skin['deep']}" stroke-width="1.1" opacity=".5" stroke-linecap="round"/>
  </g>"""


def _brow(cx, far, hair, weight="medium", arch=.5):
    t = {"fine": 2.6, "medium": 4.0, "heavy": 5.6}[weight]
    w = 12.5 if not far else 11.0
    lift = 3.2 * arch
    return (f"""<path d="M {cx - w:.1f},{BROW_Y + 2.4:.1f} """
            f"""C {cx - w * .45:.1f},{BROW_Y - lift - 1.2:.1f} {cx + w * .45:.1f},{BROW_Y - lift:.1f} {cx + w:.1f},{BROW_Y + 1.4:.1f} """
            f"""C {cx + w * .5:.1f},{BROW_Y + 1.4 + t * .55:.1f} {cx - w * .5:.1f},{BROW_Y - lift + t:.1f} {cx - w:.1f},{BROW_Y + 2.4 + t * .5:.1f} Z" """
            f"""fill="{hair['base']}" opacity="{.95 if not far else .85}"/>""")


def _nose(turn, skin):
    x = turn
    return f"""<g>
   <path d="M {x + 3:.1f},{EYE_Y - 2:.1f} C {x + 1:.1f},{EYE_Y + 12:.1f} {x - 2:.1f},{NOSE_TIP_Y - 8:.1f} {x - 7:.1f},{NOSE_TIP_Y - 1:.1f}
     C {x - 2:.1f},{NOSE_TIP_Y + 3:.1f} {x + 7:.1f},{NOSE_TIP_Y + 2.4:.1f} {x + 10:.1f},{NOSE_TIP_Y - 3:.1f}
     C {x + 9:.1f},{EYE_Y + 9:.1f} {x + 7:.1f},{EYE_Y + 1:.1f} {x + 3:.1f},{EYE_Y - 2:.1f} Z"
     fill="{skin['shade']}" opacity=".5"/>
   <path d="M {x + 7.5:.1f},{NOSE_TIP_Y - 5:.1f} C {x + 10:.1f},{NOSE_TIP_Y - 2:.1f} {x + 9:.1f},{NOSE_TIP_Y + 1.4:.1f} {x + 6:.1f},{NOSE_TIP_Y + 1.2:.1f}"
     fill="none" stroke="{skin['deep']}" stroke-width="1.2" opacity=".55" stroke-linecap="round"/>
   <ellipse cx="{x - 5.6:.1f}" cy="{NOSE_TIP_Y - .2:.1f}" rx="2.2" ry="1.5" fill="{skin['deep']}" opacity=".55"/>
   <path d="M {x - 3:.1f},{NOSE_TIP_Y - 9:.1f} C {x + 1:.1f},{NOSE_TIP_Y - 11:.1f} {x + 4:.1f},{NOSE_TIP_Y - 9:.1f} {x + 4.5:.1f},{NOSE_TIP_Y - 6:.1f}"
     fill="none" stroke="{skin['lit']}" stroke-width="2.2" opacity=".5" stroke-linecap="round"/>
  </g>"""


def _mouth(turn, skin, kind="neutral"):
    x, y = turn, MOUTH_Y
    w = 16.5
    curve = {"neutral": -0.4, "warm": -3.8, "wide": -5.4, "firm": 1.4}[kind]
    return f"""<g>
   <path d="M {x - w:.1f},{y:.1f} C {x - w * .45:.1f},{y - 3.4 + curve:.1f} {x + w * .45:.1f},{y - 3.2 + curve:.1f} {x + w:.1f},{y - .6:.1f}"
     fill="none" stroke="{skin['deep']}" stroke-width="2" opacity=".8" stroke-linecap="round"/>
   <path d="M {x - w * .84:.1f},{y + 1.2:.1f} C {x - w * .4:.1f},{y + 7 - curve * .5:.1f} {x + w * .4:.1f},{y + 6.6 - curve * .5:.1f} {x + w * .84:.1f},{y + .4:.1f}
     C {x + w * .4:.1f},{y + 2.6:.1f} {x - w * .4:.1f},{y + 2.8:.1f} {x - w * .84:.1f},{y + 1.2:.1f} Z"
     fill="{skin['shade']}" opacity=".5"/>
   {f'<path d="M {x + w + 3:.1f},{y - 5:.1f} C {x + w + 8:.1f},{y - 1:.1f} {x + w + 7:.1f},{y + 5:.1f} {x + w + 2:.1f},{y + 7:.1f}" fill="none" stroke="{skin["shade"]}" stroke-width="2" opacity=".45" stroke-linecap="round"/>' if curve < -3 else ""}
   <path d="M {x - w * .5:.1f},{y + 8.6:.1f} C {x:.1f},{y + 10.4:.1f} {x + w * .45:.1f},{y + 9.2:.1f} {x + w * .7:.1f},{y + 6.8:.1f}"
     fill="none" stroke="{skin['shade']}" stroke-width="2.4" opacity=".42" stroke-linecap="round"/>
  </g>"""


# Each style is (back, front, highlight). `back` is the mass that shows around
# the face silhouette and any length falling past the jaw; `front` is the
# crescent sitting on the cranium, its inner edge a true hairline arc; `hi` is
# a highlight that follows the mass rather than a nudged copy of it.
HAIRSTYLES = {
    "sidepart": (
        "M 0,-88 C 42,-88 64,-56 63,-18 C 62,4 58,20 52,32 L 42,27 "
        "C 51,5 54,-16 52,-32 C 46,-62 26,-77 0,-77 C -26,-77 -46,-62 -52,-32 "
        "C -54,-16 -51,5 -42,27 L -52,32 C -58,20 -62,4 -63,-18 C -64,-56 -42,-88 0,-88 Z",
        "M 58,-20 C 54,-40 42,-54 22,-60 C 2,-66 -22,-62 -38,-48 C -50,-38 -56,-30 -57,-22 "
        "C -62,-56 -38,-88 2,-88 C 40,-88 63,-56 58,-20 Z",
        "M 30,-78 C 46,-70 56,-54 57,-34 C 50,-52 38,-64 20,-70 C 24,-74 27,-77 30,-78 Z"),
    "sweptback": (
        "M 0,-86 C 40,-86 61,-54 60,-18 C 59,2 56,16 51,28 L 42,24 "
        "C 50,4 52,-14 50,-30 C 44,-58 24,-74 0,-74 C -24,-74 -44,-58 -50,-30 "
        "C -52,-14 -50,4 -42,24 L -51,28 C -56,16 -59,2 -60,-18 C -61,-54 -40,-86 0,-86 Z",
        "M 54,-32 C 50,-46 40,-56 20,-60 C 0,-64 -22,-58 -36,-46 C -46,-38 -51,-32 -52,-26 "
        "C -60,-54 -36,-86 2,-86 C 40,-86 60,-54 54,-32 Z",
        "M 26,-76 C 42,-68 52,-54 53,-36 C 47,-52 36,-62 18,-68 C 21,-72 24,-75 26,-76 Z"),
    "bun": (
        # fuller mass, length framing the jaw on both sides, and the bun behind
        "M 0,-92 C 44,-92 68,-56 67,-14 C 66,16 60,44 52,66 L 26,60 "
        "C 38,32 44,6 42,-20 C 38,-56 22,-76 0,-76 C -22,-76 -38,-56 -42,-20 "
        "C -44,6 -38,32 -26,60 L -52,66 C -60,44 -66,16 -67,-14 C -68,-56 -44,-92 0,-92 Z"
        " M 56,4 C 76,-2 92,10 92,28 C 92,46 76,58 58,52 C 68,38 68,18 56,4 Z",
        "M 58,-20 C 55,-42 44,-56 22,-62 C 0,-68 -24,-62 -40,-48 C -51,-38 -57,-30 -58,-22 "
        "C -64,-54 -38,-90 0,-90 C 38,-90 64,-54 58,-20 Z",
        "M 28,-80 C 46,-72 56,-54 57,-32 C 50,-52 37,-65 18,-72 C 22,-76 25,-79 28,-80 Z"),
    "tousled": (
        "M 0,-92 C 44,-92 68,-58 66,-16 C 65,8 60,26 53,40 L 42,34 "
        "C 52,10 55,-14 53,-32 C 47,-64 26,-80 0,-80 C -26,-80 -47,-64 -53,-32 "
        "C -55,-14 -52,10 -42,34 L -53,40 C -60,26 -65,8 -66,-16 C -68,-58 -44,-92 0,-92 Z",
        # irregular outer edge and two fringe pieces dipping onto the forehead
        "M 58,-18 C 54,-38 44,-52 24,-58 C 12,-61 2,-48 -6,-56 C -16,-64 -28,-54 -40,-46 "
        "C -51,-37 -57,-28 -58,-20 C -67,-50 -57,-80 -28,-90 C -6,-97 20,-94 40,-83 "
        "C 60,-71 68,-45 58,-18 Z",
        "M 22,-84 C 42,-76 54,-58 56,-34 C 49,-56 35,-70 14,-77 C 17,-81 20,-83 22,-84 Z"),
    "crop": (
        "M 0,-84 C 38,-84 60,-54 59,-20 C 58,0 55,14 50,26 L 41,22 "
        "C 49,2 51,-14 49,-30 C 43,-58 24,-72 0,-72 C -24,-72 -43,-58 -49,-30 "
        "C -51,-14 -49,2 -41,22 L -50,26 C -55,14 -58,0 -59,-20 C -60,-54 -38,-84 0,-84 Z",
        "M 57,-26 C 53,-44 40,-58 18,-63 C -4,-68 -26,-62 -42,-48 C -51,-40 -56,-32 -57,-26 "
        "C -60,-52 -36,-84 0,-84 C 38,-84 61,-52 57,-26 Z",
        "M 26,-74 C 42,-66 52,-52 54,-34 C 48,-50 36,-60 18,-66 C 21,-70 24,-73 26,-74 Z"),
}


def _glasses(turn, kind, accent=None):
    """kind: 'round' | 'rect' | 'rimless'. accent paints the rim amber."""
    near, far = turn + 26, turn - 26
    col = accent or "#151530"
    wid = 1.9 if kind != "rimless" else 1.3
    op = 1 if kind != "rimless" else .55
    if kind == "round":
        lens = (f'<circle cx="{near}" cy="{EYE_Y}" r="15.5" fill="#DDEAF6" fill-opacity=".1" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>'
                f'<circle cx="{far}" cy="{EYE_Y}" r="14.2" fill="#DDEAF6" fill-opacity=".1" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>')
    else:
        lens = (f'<rect x="{near - 16}" y="{EYE_Y - 11}" width="32" height="22" rx="5" fill="#DDEAF6" fill-opacity=".1" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>'
                f'<rect x="{far - 14.5}" y="{EYE_Y - 10.4}" width="29" height="21" rx="5" fill="#DDEAF6" fill-opacity=".1" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>')
    r = 15.5 if kind == "round" else 16
    return f"""<g>
   {lens}
   <path d="M {far + r * .92:.1f},{EYE_Y:.1f} L {near - r * .92:.1f},{EYE_Y:.1f}" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>
   <path d="M {near + r * .95:.1f},{EYE_Y - 1:.1f} L 55,{EYE_Y - 3:.1f}" stroke="{col}" stroke-width="{wid}" opacity="{op}"/>
   <path d="M {near - 11:.1f},{EYE_Y - 6:.1f} C {near - 4:.1f},{EYE_Y - 10:.1f} {near + 5:.1f},{EYE_Y - 9:.1f} {near + 10:.1f},{EYE_Y - 5:.1f}"
     fill="none" stroke="#FFFFFF" stroke-width="2" opacity=".30" stroke-linecap="round"/>
  </g>"""


def head(skin, hair, *, face="oval", turn=-7, hairstyle="sidepart", brow="medium", arch=.5,
         eyes="calm", mouth="neutral", glasses=None, glasses_accent=None,
         moustache=False, stubble=False, age_lines=False, earring=None):
    """Return (behind, front) SVG fragments for one head, in local coordinates.

    `behind` holds the hair mass that sits under the face; `front` is the face
    and everything on top of it. Callers draw neck and shoulders between them.
    """
    back_hair, front_hair, hair_hi = HAIRSTYLES[hairstyle]
    outline, half_w, chin = FACES[face]
    near, far = turn + 26, turn - 26

    behind = f'<path d="{back_hair}" fill="{hair["base"]}"/>'

    face_svg = f"""
  <g clip-path="url(#ig-face-{face})">
   <path d="{outline}" fill="{skin['base']}"/>
   <rect x="-{half_w + 6}" y="-92" width="{2 * half_w + 12}" height="{chin + 96}" fill="url(#ig-model)"/>
   <rect x="-{half_w + 6}" y="-92" width="{2 * half_w + 12}" height="{chin + 96}" fill="url(#ig-jaw)"/>
  </g>"""

    ear = f"""
  <path d="M {half_w - 4},-6 C {half_w + 4},-10 {half_w + 10},-2 {half_w + 9},8 C {half_w + 8},18 {half_w + 2},24 {half_w - 5},22 C {half_w - 2},14 {half_w - 2},2 {half_w - 4},-6 Z" fill="{skin['base']}"/>
  <path d="M {half_w},0 C {half_w + 4},-1 {half_w + 6},4 {half_w + 5},10 C {half_w + 4},15 {half_w + 1},17 {half_w - 1},16" fill="none" stroke="{skin['deep']}" stroke-width="1.3" opacity=".55"/>"""

    stub = (f'<path d="M -30,26 C -22,54 -10,72 0,77 C 12,74 24,62 32,44 C 34,58 22,74 6,79 C -4,81 -18,72 -28,56 C -34,44 -34,34 -30,26 Z"'
            f' fill="{hair["base"]}" opacity=".20"/>' if stubble else "")

    must = (f'<path d="M {turn - 21:.1f},{MOUTH_Y - 13:.1f} C {turn - 15:.1f},{MOUTH_Y - 19:.1f} {turn - 6:.1f},{MOUTH_Y - 17:.1f} {turn + 1:.1f},{MOUTH_Y - 15:.1f}'
            f' C {turn + 9:.1f},{MOUTH_Y - 17:.1f} {turn + 20:.1f},{MOUTH_Y - 18:.1f} {turn + 22:.1f},{MOUTH_Y - 12:.1f}'
            f' C {turn + 19:.1f},{MOUTH_Y - 5:.1f} {turn + 10:.1f},{MOUTH_Y - 7:.1f} {turn + 1:.1f},{MOUTH_Y - 8:.1f}'
            f' C {turn - 9:.1f},{MOUTH_Y - 7:.1f} {turn - 17:.1f},{MOUTH_Y - 5:.1f} {turn - 21:.1f},{MOUTH_Y - 13:.1f} Z"'
            f' fill="{hair["base"]}"/>'
            f'<path d="M {turn - 20:.1f},{MOUTH_Y - 13:.1f} C {turn - 8:.1f},{MOUTH_Y - 17:.1f} {turn + 10:.1f},{MOUTH_Y - 17:.1f} {turn + 21:.1f},{MOUTH_Y - 12:.1f}"'
            f' fill="none" stroke="{hair["edge"]}" stroke-width="2" opacity=".5" stroke-linecap="round"/>'
            if moustache else "")

    lines = (f'<path d="M {turn + 14:.1f},{BROW_Y - 12:.1f} C {turn + 22:.1f},{BROW_Y - 14:.1f} {turn + 32:.1f},{BROW_Y - 12:.1f} {turn + 38:.1f},{BROW_Y - 8:.1f}"'
             f' fill="none" stroke="{skin["deep"]}" stroke-width="1.1" opacity=".3" stroke-linecap="round"/>'
             f'<path d="M {turn + 20:.1f},{MOUTH_Y - 14:.1f} C {turn + 26:.1f},{MOUTH_Y - 4:.1f} {turn + 27:.1f},{MOUTH_Y + 4:.1f} {turn + 24:.1f},{MOUTH_Y + 10:.1f}"'
             f' fill="none" stroke="{skin["deep"]}" stroke-width="1.3" opacity=".28" stroke-linecap="round"/>' if age_lines else "")

    ring = (f'<circle cx="{half_w + 3}" cy="21" r="3.6" fill="{earring}"/>' if earring else "")

    front = f"""{face_svg}{ear}
  {_brow(far, True, hair, brow, arch)}{_brow(near, False, hair, brow, arch)}
  {_eye(far, True, skin, hair, eyes)}{_eye(near, False, skin, hair, eyes)}
  {_nose(turn, skin)}
  {stub}{must}
  {_mouth(turn, skin, mouth)}
  {lines}
  <path d="{front_hair}" fill="{hair['base']}"/>
  <path d="{hair_hi}" fill="{hair['lit']}" opacity=".55"/>
  <path d="{front_hair}" fill="{hair['edge']}" opacity=".22"/>
  {_glasses(turn, glasses, glasses_accent) if glasses else ""}{ring}"""
    return behind, front
