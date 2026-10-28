<script setup>
const description =
  "Alternative Reality Group builds and runs its own software products, including kidscancode and Bloginator, and takes on a few outside builds each year. Based in Los Angeles."

useHead({
  htmlAttrs: { lang: "en-US" },
  link: [
    { rel: "icon", href: "/favicon.svg", type: "image/svg+xml" },
    { rel: "icon", href: "/favicon.ico", sizes: "48x48" },
    { rel: "apple-touch-icon", href: "/apple-touch-icon.png" },
  ],
  meta: [{ name: "theme-color", content: "#0B0F14" }],
})

useSeoMeta({
  title: "Alternative Reality Group: software products, built and shipped",
  description,
  ogTitle: "Alternative Reality Group",
  ogDescription: description,
  ogImage: "https://alternativereality.com/brand/og-image.png",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  ogImageAlt: "The //ARG. logo",
  twitterCard: "summary_large_image",
})
</script>

<template>
  <div>
    <NuxtPage />
  </div>
</template>
