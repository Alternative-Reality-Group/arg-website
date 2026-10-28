<template>
  <header class="sticky top-0 z-20 border-b border-line bg-paper/90 backdrop-blur">
    <div class="mx-auto flex h-16 max-w-6xl items-center justify-between gap-6 px-4 sm:px-6">
      <NuxtLink to="/" class="flex shrink-0 items-center" aria-label="Alternative Reality Group, home">
        <img src="/brand/arg-wordmark-ink.svg" alt="Alternative Reality Group" width="66" height="28" class="h-7 w-auto" />
      </NuxtLink>
      <nav aria-label="Main" class="flex items-center gap-5 text-[15px] sm:gap-8">
        <a v-for="link in links" :key="link.href" :href="link.href" class="text-ink/80 transition-colors hover:text-ink">
          {{ link.label }}
        </a>
      </nav>
    </div>
  </header>
</template>

<script setup>
const links = [
  { label: "Products", href: "/#products" },
  { label: "About", href: "/#about" },
  { label: "Contact", href: "/#contact" },
]
</script>
