"""Assemble the sprite and the preview page."""
import figures
from palette import GROUND, GROUND_DARK, GROUND_DEEP, AMBER, defs


def sprite(symbols):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" '
            'style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">\n'
            + defs() + "\n" + "\n".join(symbols) + "\n</svg>")


def use(fid, w, h, label=None, cls="ig"):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {a}>'
            f'<use href="#{fid}"/></svg>')
