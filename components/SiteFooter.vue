<template>
  <footer class="border-t border-line-dark bg-night text-muted-dark">
    <div class="mx-auto flex max-w-6xl flex-col gap-6 px-4 py-10 sm:flex-row sm:items-center sm:justify-between sm:px-6">
      <div class="flex items-center gap-3">
        <img src="/brand/arg-icon-dark-small.svg" alt="" width="32" height="32" class="h-8 w-8 rounded-md ring-1 ring-line-dark" />
        <p class="text-sm">&copy; {{ year }} Alternative Reality Group</p>
      </div>
      <div class="flex flex-wrap gap-x-6 gap-y-2 text-sm">
        <a href="mailto:contact@alternativereality.com" class="hover:text-paper">contact@alternativereality.com</a>
        <NuxtLink to="/privacy" class="hover:text-paper">Privacy</NuxtLink>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear()
</script>
