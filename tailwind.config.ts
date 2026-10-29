import defaultTheme from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ["Space Grotesk", ...defaultTheme.fontFamily.sans],
        sans: ["IBM Plex Sans", ...defaultTheme.fontFamily.sans],
        mono: ["IBM Plex Mono", ...defaultTheme.fontFamily.mono],
      },
      // Brand palette, taken from the //ARG. logo
      colors: {
        ink: "#12101C",
        paper: "#F4F2ED",
        night: "#0B0F14",
        violet: { DEFAULT: "#7C5CFF", dim: "#5B47B8", light: "#B9A8FF" },
        muted: { DEFAULT: "#5C5866", dark: "#A6A2B2" },
        line: { DEFAULT: "#E2DED6", dark: "#262A33" },
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
