<script setup>
const title = "Alternative Reality Group: AI and software strategy for founders and operators"
const description =
  "Alternative Reality Group helps founders and operators move from AI curiosity to production-ready systems, and from prototype to real revenue. AI strategy, custom software, training and go-to-market support, based in Los Angeles."

useHead({
  htmlAttrs: { lang: "en-US" },
  link: [{ rel: "icon", href: "/favicon.svg" }],
})

useSeoMeta({
  title,
  description,
  ogTitle: title,
  ogDescription: description,
  ogType: "website",
  ogUrl: "https://alternativereality.com/",
  ogSiteName: "Alternative Reality Group",
  ogImage: "https://alternativereality.com/img/og-image.jpg",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  ogImageAlt: "AI and software strategy for founders and operators",
  twitterCard: "summary_large_image",
  twitterTitle: title,
  twitterDescription: description,
  twitterImage: "https://alternativereality.com/img/og-image.jpg",
})
</script>

<template>
  <div>
    <NuxtPage />
  </div>
</template>
