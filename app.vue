<script setup>
useHead({
  htmlAttrs: { lang: "en-US" },
  title: "Alternative Reality Group",
  link: [{ rel: "icon", href: "/favicon.svg" }],
  meta: [
    {
      name: "Alternative Reality Group",
      content:
        "Alternative Reality Group provides product and digital transformation consulting services to clients primarily in the entertainment industry.  Certified ServiceNow professional services provided.",
    },
  ],
})

useSeoMeta({
  title: "Alternative Reality Group",
  description:
    "Alternative Reality Group provides product and digital transformation consulting services to clients primarily in the entertainment industry.  Certified ServiceNow professional services provided.",
  ogDescription:
    "Alternative Reality Group provides product and digital transformation consulting services to clients primarily in the entertainment industry.  Certified ServiceNow professional services provided.",
  ogTitle: "Alternative Reality Group",
  ogImage: "https://alternativereality.com/img/preview.svg",
  twitterCard: "summary_large_image",
})
</script>

<template>
  <div>
    <NuxtPage />
  </div>
</template>
