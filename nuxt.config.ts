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
  compatibilityDate: "2024-12-18",
})
