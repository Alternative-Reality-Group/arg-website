# //ARG. brand assets

The logo is a lavender scan-line slash, then the A's own left leg in violet (`//`), then ARG in ink,
closed by a violet square full stop. The icon is the two slashes alone. All type is outlined, so
nothing depends on Space Grotesk being installed.

Built files live in `public/brand/` and are served at `https://alternativereality.com/brand/…`.

| Use | File |
| --- | --- |
| Site header | `arg-wordmark-ink.svg`, `arg-wordmark-white.svg` |
| Full logo with tagline | `arg-logo-ink.svg` / `arg-logo-white.svg` (transparent), `arg-logo-light.svg` / `arg-logo-dark.svg` (on ground), PNGs at 1200px |
| Email signature | `arg-logo-email-600.png` (light ground, so dark-mode mail clients leave it alone) |
| App icon | `arg-icon-dark.svg`, `arg-icon-light.svg`, `arg-icon-512.png`, `arg-icon-192.png` |
| Small icon (around 32px) | `arg-icon-dark-small.svg` (5 scan lines) |
| Favicon | `/favicon.svg` (4 scan lines), `/favicon.ico` (16/32/48), `/apple-touch-icon.png` |
| Social share card | `og-image.png` (1200×630) |
| LinkedIn company page | `arg-linkedin-logo-400.png` (square corners; LinkedIn applies its own mask), `arg-linkedin-cover-1128x191.png` |
| Decorative mark | `arg-mark-light.svg`, `arg-mark-dark.svg` (the slashes, no tile) |

Colours: violet `#7C5CFF`, lavender `#B9A8FF` (scan slash on light), dim violet `#5B47B8` (scan slash
on dark), ink `#12101C`, paper `#F4F2ED`, night `#0B0F14`.

## Rebuilding

```sh
pip install fonttools uharfbuzz brotli pillow
python brand/build_logo.py     # SVGs
node brand/render_png.cjs      # PNGs (uses Playwright's Chromium)
python -c "from PIL import Image; d='public/brand/'; Image.open(d+'arg-favicon-48.png').save('public/favicon.ico', sizes=[(16,16),(32,32),(48,48)], append_images=[Image.open(d+'arg-favicon-16.png'), Image.open(d+'arg-favicon-32.png')])"
```

The fonts in `brand/fonts/` are Space Grotesk, under the SIL Open Font License (`brand/fonts/OFL.txt`).
