// Render the PNG set from the SVGs written by build_logo.py (needs Playwright's Chromium).
//   node brand/render_png.cjs
const { chromium } = require("playwright")
const fs = require("fs")
const path = require("path")

const root = path.resolve(__dirname, "..")
const brand = path.join(root, "public", "brand")
const svg = (name) => fs.readFileSync(path.join(brand, name), "utf8")

// [output file, source svg, width, height, page background or null for transparent]
const squares = [
  ["arg-icon-512.png", "arg-icon-dark.svg", 512],
  ["arg-icon-192.png", "arg-icon-dark.svg", 192],
  ["arg-icon-light-512.png", "arg-icon-light.svg", 512],
  ["../apple-touch-icon.png", "arg-icon-dark.svg", 180],
  ["arg-favicon-48.png", "arg-icon-dark-small.svg", 48],
  ["arg-favicon-32.png", "arg-icon-dark-small.svg", 32],
  ["arg-favicon-16.png", "arg-favicon.svg", 16],
  ["arg-linkedin-logo-400.png", "arg-icon-square.svg", 400],
]
const logos = [
  ["arg-logo-light-1200.png", "arg-logo-light.svg", 1200],
  ["arg-logo-dark-1200.png", "arg-logo-dark.svg", 1200],
  ["arg-logo-ink-1200.png", "arg-logo-ink.svg", 1200],
  ["arg-logo-white-1200.png", "arg-logo-white.svg", 1200],
  // email signatures: light ground, so dark-mode clients don't flip it
  ["arg-logo-email-600.png", "arg-logo-light.svg", 600],
]

;(async () => {
  const browser = await chromium.launch()
  const page = await browser.newPage()
  const shoot = async (file, html, width, height) => {
    await page.setViewportSize({ width, height })
    await page.setContent(`<style>html,body{margin:0;background:transparent}svg{display:block;width:${width}px;height:${height}px}</style>${html}`)
    await page.screenshot({ path: path.join(brand, file), omitBackground: true, clip: { x: 0, y: 0, width, height } })
    console.log("wrote", file)
  }
  for (const [file, src, size] of squares) await shoot(file, svg(src), size, size)
  for (const [file, src, width] of logos) await shoot(file, svg(src), width, Math.round((width * 148) / 340))

  // Social share card: white lockup centred on the dark ground
  await page.setViewportSize({ width: 1200, height: 630 })
  await page.setContent(`<style>html,body{margin:0}body{width:1200px;height:630px;background:#0B0F14;display:flex;align-items:center;justify-content:center}svg{width:720px;height:auto}</style>${svg("arg-logo-white.svg")}`)
  await page.screenshot({ path: path.join(brand, "og-image.png") })
  console.log("wrote og-image.png")

  // LinkedIn cover: logo on the right, since the page's profile logo covers the bottom-left
  await page.setViewportSize({ width: 1128, height: 191 })
  await page.setContent(`<style>html,body{margin:0}body{width:1128px;height:191px;background:#0B0F14;display:flex;align-items:center;justify-content:flex-end;padding-right:64px;box-sizing:border-box}svg{height:120px;width:auto}</style>${svg("arg-logo-white.svg")}`)
  await page.screenshot({ path: path.join(brand, "arg-linkedin-cover-1128x191.png") })
  console.log("wrote arg-linkedin-cover-1128x191.png")
  await browser.close()
})()
