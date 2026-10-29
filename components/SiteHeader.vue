<template>
  <header class="sticky top-0 z-20 border-b border-line bg-paper/90 backdrop-blur">
    <div class="mx-auto flex h-16 max-w-6xl items-center justify-between gap-6 px-4 sm:px-6">
      <NuxtLink to="/" class="flex shrink-0 items-center gap-3" aria-label="Alternative Reality Group, home">
        <img src="/brand/arg-wordmark-ink.svg" alt="" width="66" height="28" class="h-7 w-auto" />
        <span class="hidden border-l border-line pl-3 font-display text-[15px] font-medium text-ink sm:inline">
          Alternative Reality Group
        </span>
      </NuxtLink>
      <nav aria-label="Main" class="flex items-center gap-5 text-[15px] sm:gap-8">
        <a
          v-for="link in links"
          :key="link.href"
          :href="link.href"
          class="text-ink/80 transition-colors hover:text-ink"
          :class="{ 'hidden md:inline': link.desktopOnly }">
          {{ link.label }}
        </a>
      </nav>
    </div>
  </header>
</template>

<script setup>
// Four links don't fit beside the logo on small screens, so About only appears from the md breakpoint up.
const links = [
  { label: "Services", href: "/#services" },
  { label: "Portfolio", href: "/#portfolio" },
  { label: "About", href: "/#about", desktopOnly: true },
  { label: "Contact", href: "/#contact" },
]
</script>
