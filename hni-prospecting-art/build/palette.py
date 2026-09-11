"""Palettes and the shared <defs> sprite for the HNI prospecting figures.

Every figure draws from these ramps and reuses these defs, which is what makes
ten drawings read as one commissioned set rather than ten separate jobs.
"""

# Indigo ground the briefing already sits on.
GROUND = "#2B2BA6"
GROUND_DEEP = "#1E1E7A"
GROUND_DARK = "#16164F"

AMBER = "#FFB951"
AMBER_DEEP = "#E09A2C"

# Skin ramps. Five personas across a real range rather than one tone restated
# five times. Shadows are tinted toward indigo so faces sit in the page's light.
SKIN = {
    "light": {"lit": "#F6EBD8", "base": "#E6D3B6", "shade": "#C2A98C", "deep": "#9C8470"},
    "warm":  {"lit": "#EEDCC0", "base": "#DCC4A2", "shade": "#B4977A", "deep": "#8E7660"},
    "mid":   {"lit": "#E0C6A4", "base": "#CBAD86", "shade": "#A38466", "deep": "#7E6248"},
    "olive": {"lit": "#D2B390", "base": "#B99872", "shade": "#927154", "deep": "#6E523C"},
    "deep":  {"lit": "#B98F68", "base": "#9E7450", "shade": "#7A563A", "deep": "#5A3D28"},
}

HAIR = {
    "jet":      {"base": "#15152E", "lit": "#282850", "edge": "#3A3A6E"},
    "dark":     {"base": "#1C1C38", "lit": "#30305C", "edge": "#454578"},
    "salt":     {"base": "#3A3A58", "lit": "#63637E", "edge": "#8A8AA0"},
    "grey":     {"base": "#5C5C76", "lit": "#82829A", "edge": "#A6A6BA"},
}

# Garments. Indigo family so figures belong to the page, with two neutrals for
# contrast so five portraits don't flatten into one blue mass.
CLOTH = {
    "indigo":   {"lit": "#4242C8", "base": "#3232A6", "shade": "#232378", "fold": "#1A1A5C"},
    "deepblue": {"lit": "#2E3A72", "base": "#243058", "shade": "#1A2340", "fold": "#141A30"},
    "charcoal": {"lit": "#3C3C4E", "base": "#2E2E3C", "shade": "#21212C", "fold": "#181820"},
    "linen":    {"lit": "#E4DCCC", "base": "#CEC3AE", "shade": "#A89B84", "deep": "#857A66",
                 "fold": "#8E8270"},
    "white":    {"lit": "#F4F2EC", "base": "#DEDBD2", "shade": "#B4B0A4", "fold": "#98948A"},
}


def defs():
    """The shared sprite header: ramps, vignette, and the print-tooth filter.

    Defined once per page. Ten figures then cost roughly the bytes of two.
    """
    return f"""<defs>
 <radialGradient id="ig-vig" cx="50%" cy="42%" r="62%">
  <stop offset="0%" stop-color="{GROUND}" stop-opacity="0"/>
  <stop offset="62%" stop-color="{GROUND_DEEP}" stop-opacity=".38"/>
  <stop offset="100%" stop-color="{GROUND_DARK}" stop-opacity=".82"/>
 </radialGradient>
 <linearGradient id="ig-halo" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="{AMBER}" stop-opacity=".16"/>
  <stop offset="70%" stop-color="{AMBER}" stop-opacity="0"/>
 </linearGradient>
 <!-- grain kept strictly inside the artwork: no blend modes, so it renders the
      same everywhere instead of degrading to a grey haze where they're absent -->
 <filter id="ig-tooth" x="-2%" y="-2%" width="104%" height="104%">
  <feTurbulence type="fractalNoise" baseFrequency="1.15" numOctaves="2" seed="7" result="n"/>
  <feColorMatrix in="n" type="saturate" values="0" result="m"/>
  <feComponentTransfer in="m" result="s">
   <feFuncA type="linear" slope=".085"/>
  </feComponentTransfer>
  <feComposite in="s" in2="SourceGraphic" operator="in" result="g"/>
  <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="g"/></feMerge>
 </filter>
 <filter id="ig-soft" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="9"/>
 </filter>
 <linearGradient id="ig-model" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="var(--sk-shade)" stop-opacity=".30"/>
  <stop offset="18%" stop-color="var(--sk-shade)" stop-opacity=".19"/>
  <stop offset="48%" stop-color="var(--sk-shade)" stop-opacity="0"/>
  <stop offset="80%" stop-color="var(--sk-lit)" stop-opacity=".15"/>
  <stop offset="100%" stop-color="var(--sk-lit)" stop-opacity=".28"/>
 </linearGradient>
 <linearGradient id="ig-jaw" x1="0" y1="0" x2="0" y2="1">
  <stop offset="52%" stop-color="var(--sk-shade)" stop-opacity="0"/>
  <stop offset="100%" stop-color="var(--sk-shade)" stop-opacity=".34"/>
 </linearGradient>
 <clipPath id="ig-face-square"><path d="M 0,-80 C 36,-80 59,-56 60,-20 C 61,10 56,34 44,52 C 34,66 18,76 0,76 C -18,76 -34,66 -44,50 C -56,32 -59,10 -59,-20 C -59,-56 -36,-80 0,-80 Z"/></clipPath>
 <clipPath id="ig-face-oval"><path d="M 0,-80 C 34,-80 57,-56 58,-20 C 59,12 50,40 30,60 C 19,71 9,78 0,78 C -11,78 -23,68 -35,53 C -52,33 -57,10 -57,-20 C -57,-56 -34,-80 0,-80 Z"/></clipPath>
 <clipPath id="ig-face-heart"><path d="M 0,-80 C 36,-80 58,-54 58,-18 C 58,14 46,42 24,62 C 14,72 6,78 0,78 C -7,78 -16,71 -27,60 C -48,40 -58,14 -58,-18 C -58,-54 -36,-80 0,-80 Z"/></clipPath>
 <clipPath id="ig-face-long"><path d="M 0,-82 C 30,-82 52,-58 53,-22 C 54,14 46,44 28,64 C 18,75 8,82 0,82 C -9,82 -20,72 -31,58 C -47,38 -52,12 -52,-22 C -52,-58 -30,-82 0,-82 Z"/></clipPath>
 <clipPath id="ig-face-round"><path d="M 0,-78 C 36,-78 60,-54 61,-18 C 62,10 54,32 38,50 C 26,63 12,71 0,71 C -13,71 -27,63 -39,49 C -55,31 -60,10 -60,-18 C -60,-54 -36,-78 0,-78 Z"/></clipPath>
 <clipPath id="ig-frame"><rect x="0" y="0" width="400" height="500" rx="18"/></clipPath>
 <clipPath id="ig-sq"><rect x="0" y="0" width="300" height="300" rx="16"/></clipPath>
 <clipPath id="ig-wide"><rect x="0" y="0" width="1000" height="560" rx="20"/></clipPath>
</defs>"""
