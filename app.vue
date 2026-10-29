<script setup>
const description =
  "Alternative Reality Group is an AI-native product company in Los Angeles. We help founders turn AI-built prototypes into real products, with product strategy, architecture, security, analytics, brand and go-to-market, and we build our own products the same way."

useHead({
  htmlAttrs: { lang: "en-US" },
  link: [
    { rel: "icon", href: "/favicon.svg", type: "image/svg+xml" },
    { rel: "icon", href: "/favicon.ico", sizes: "48x48" },
    { rel: "apple-touch-icon", href: "/apple-touch-icon.png" },
  ],
  meta: [{ name: "theme-color", content: "#0B0F14" }],
})

const title = "Alternative Reality Group: AI-native product development"
const image = "https://alternativereality.com/brand/og-image.png"

useSeoMeta({
  title,
  description,
  ogTitle: title,
  ogDescription: description,
  ogType: "website",
  ogUrl: "https://alternativereality.com/",
  ogSiteName: "Alternative Reality Group",
  ogImage: image,
  ogImageWidth: 1200,
  ogImageHeight: 630,
  ogImageAlt: "The //ARG. logo",
  twitterCard: "summary_large_image",
  twitterTitle: title,
  twitterDescription: description,
  twitterImage: image,
})
</script>

<template>
  <div>
    <NuxtPage />
  </div>
</template>
