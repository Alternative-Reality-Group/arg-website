import svgLoader from "vite-svg-loader"
export default defineNuxtConfig({
  ssr: true,
  vite: {
    plugins: [svgLoader()],
  },
  future: {
    compatibilityVersion: 4,
  },
  gtag: {
    id: "G-SMT04911K6",
  },
  // cookieConsent: {
  //   provider: "cookiebot",
  //   cbid: "8604f17d-2d10-40af-acfb-cf66bcbb84ab", // Replace with you own cbid

  //   // Optional
  //   // consentMode: false, // Disable consent mode (default: true)
  //   // consentModeDefaults: false, // Disable content mode defaults (default: true)
  // },
  devtools: { enabled: false },
  css: ["~/assets/css/main.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  modules: [
    "@nuxt/content",
    "nuxt-icon",
    "@nuxtjs/google-fonts",
    "nuxt-gtag",
    "@nuxtjs/robots",
    "@weareheavy/nuxt-cookie-consent",
    "nuxt-svgo",
    "@nuxt/image",
  ],
  googleFonts: {
    families: {
      "Space Grotesk": [500, 700],
      "IBM Plex Sans": [400, 500, 600],
      "IBM Plex Mono": [400, 500],
    },
    display: "swap",
  },
  // The old standalone pages now live as sections on the home page
  routeRules: {
    "/about": { redirect: "/#about" },
    "/contact": { redirect: "/#contact" },
  },
  compatibilityDate: "2024-12-18",
})
