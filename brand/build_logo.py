"""Build the //ARG. logo, icon and favicon SVGs with all type converted to outlines.

    pip install fonttools uharfbuzz brotli
    python brand/build_logo.py            # writes SVGs to public/brand/ and public/favicon.svg
    node brand/render_png.mjs             # then renders the PNGs from those SVGs

The mark: a lavender scan-line slash, then the A's own left leg in violet ("//"),
then ARG in ink, closed by a violet square full stop. The icon is the two slashes alone.
"""
import io
import pathlib

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "brand" / "fonts"
OUT = ROOT / "public" / "brand"

VIOLET = "#7C5CFF"
LAVENDER = "#B9A8FF"   # scan slash on light grounds
DIM_VIOLET = "#5B47B8" # scan slash on dark grounds
INK = "#12101C"
PAPER = "#F4F2ED"
NIGHT = "#0B0F14"

_fonts = {}


def _font(weight):
    if weight not in _fonts:
        tt = TTFont(FONTS / f"space-grotesk-latin-{weight}-normal.woff2")
        tt.flavor = None
        buf = io.BytesIO()
        tt.save(buf)
        data = buf.getvalue()
        _fonts[weight] = (TTFont(io.BytesIO(data)), hb.Font(hb.Face(data)))
    return _fonts[weight]


def outline(text, x, y, size, letter_spacing=0.0, weight=700):
    """Shape `text` with HarfBuzz (kerning on) and return it as one SVG path."""
    tt, font = _font(weight)
    glyphs, order = tt.getGlyphSet(), tt.getGlyphOrder()
    scale = size / tt["head"].unitsPerEm
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True})
    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    pen_x = x
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        transform = (scale, 0, 0, -scale, pen_x + pos.x_offset * scale, y - pos.y_offset * scale)
        glyphs[order[info.codepoint]].draw(TransformPen(pen, transform))
        pen_x += pos.x_advance * scale + letter_spacing
    return pen.getCommands()


# Wordmark geometry, in the 112px design space the logo was drawn in.
WORDMARK = outline("ARG", 18, 99, 112, -5)
TAGLINE = outline("ALTERNATIVE REALITY GROUP", 19, 139, 12.5, 2.8, 600)
CAP, BASE = 20.6, 99.0


# The A's left leg, measured from the Space Grotesk Bold outline.
def leg_outer(y):
    return 20.02 + (BASE - y) * 0.2628


def leg_inner(y):
    return 35.25 + (BASE - y) * 0.2496


LEG_WIDTH = leg_inner(BASE) - leg_outer(BASE)
SLASH_GAP = 2      # space between the scan slash and the A's leg
CLIP = 0.8         # keeps the clip edge off the glyph edge so no hairline shows


def leg_path(dx=0.0):
    pts = [(leg_outer(BASE), BASE), (leg_inner(BASE) + CLIP, BASE), (leg_inner(CAP) + CLIP, CAP), (leg_outer(CAP), CAP)]
    return "M" + "L".join(f"{x + dx:.2f} {y:.2f}" for x, y in pts) + "Z"


def scan_slash(rows, colour, duty=0.7):
    """The free slash as horizontal slices of the leg's shape, so its slanted sides survive."""
    dx = -(LEG_WIDTH + SLASH_GAP)
    band = (BASE - CAP) / rows
    parts = []
    for r in range(rows):
        top = CAP + r * band + band * (1 - duty) / 2
        bottom = top + band * duty
        pts = [(leg_outer(bottom), bottom), (leg_inner(bottom), bottom), (leg_inner(top), top), (leg_outer(top), top)]
        parts.append("M" + "L".join(f"{x + dx:.2f} {y:.2f}" for x, y in pts) + "Z")
    return f'<path d="{"".join(parts)}" fill="{colour}"/>'


def slashes(rows, on_dark):
    return scan_slash(rows, DIM_VIOLET if on_dark else LAVENDER) + f'<path d="{leg_path()}" fill="{VIOLET}"/>'


def svg(view_box, width, height, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="{width}" height="{height}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')


def logo(fg, background=None, tagline=True, rows=8):
    """Full lockup (with tagline) or the header wordmark (without)."""
    on_dark = fg != INK
    width, height = (340, 148) if tagline else (244, 104)
    view_box = f"0 0 {width} {height}" if tagline else f"0 8 {width} {height}"
    rest_of_a = f"M{leg_inner(130) + CLIP:.2f} 130L{leg_inner(-10) + CLIP:.2f} -10L400 -10L400 130Z"
    body = (f'<defs><clipPath id="arg-a"><path d="{rest_of_a}"/></clipPath></defs>'
            + (f'<rect width="{width}" height="{height}" fill="{background}"/>' if background else "")
            + f'<path d="{WORDMARK}" fill="{fg}" clip-path="url(#arg-a)"/>'
            + slashes(rows, on_dark)
            + f'<rect x="226" y="86" width="13" height="13" fill="{VIOLET}"/>'
            + (f'<path d="{TAGLINE}" fill="{fg}" opacity=".62"/>' if tagline else ""))
    return svg(view_box, width, height, body, "Alternative Reality Group")


def icon(on_dark=True, rows=8, fill=34, radius=9, size=48):
    """The two slashes alone, centred on a rounded tile."""
    left = leg_outer(BASE) - LEG_WIDTH - SLASH_GAP
    right = leg_inner(CAP) + CLIP
    k = fill / (BASE - CAP)
    tx = (48 - (right - left) * k) / 2 - left * k
    ty = (48 - (BASE - CAP) * k) / 2 - CAP * k
    body = (f'<rect width="48" height="48" rx="{radius}" fill="{NIGHT if on_dark else PAPER}"/>'
            f'<g transform="translate({tx:.2f} {ty:.2f}) scale({k:.4f})">{slashes(rows, on_dark)}</g>')
    return svg("0 0 48 48", size, size, body, "Alternative Reality Group")


def mark(on_dark=False, rows=8):
    """The two slashes alone on a transparent ground, for large decorative use."""
    left = leg_outer(BASE) - LEG_WIDTH - SLASH_GAP
    right = leg_inner(CAP) + CLIP
    view_box = f"{left:.2f} {CAP} {right - left:.2f} {BASE - CAP}"
    return svg(view_box, round(right - left), round(BASE - CAP), slashes(rows, on_dark), "//")


FILES = {
    # Lockups with tagline
    "arg-logo-ink.svg": logo(INK),
    "arg-logo-white.svg": logo(PAPER),
    "arg-logo-light.svg": logo(INK, PAPER),
    "arg-logo-dark.svg": logo(PAPER, NIGHT),
    # Header wordmark, no tagline, fewer scan lines
    "arg-wordmark-ink.svg": logo(INK, tagline=False, rows=6),
    "arg-wordmark-white.svg": logo(PAPER, tagline=False, rows=6),
    # Icon tiers: 8 scan lines large, 5 at 32px, 4 at 16px
    "arg-icon-dark.svg": icon(True, 8),
    "arg-icon-light.svg": icon(False, 8),
    "arg-icon-dark-small.svg": icon(True, 5),
    "arg-icon-light-small.svg": icon(False, 5),
    "arg-favicon.svg": icon(True, 4, fill=40, radius=8),
    # The slashes alone, for large decorative use
    "arg-mark-light.svg": mark(False),
    "arg-mark-dark.svg": mark(True),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, content in FILES.items():
        (OUT / name).write_text(content)
        print("wrote", OUT / name)
    (ROOT / "public" / "favicon.svg").write_text(FILES["arg-favicon.svg"])
    print("wrote", ROOT / "public" / "favicon.svg")
