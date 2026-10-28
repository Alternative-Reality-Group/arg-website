<template>
  <div class="flex flex-wrap gap-4 p-8">
    <NuxtLink v-if="label && url" 
      :href="url" 
      class="inline-flex shadow-md border-1 px-7 py-2 duration-500 border-black hover:text-neutral-dark hover:bg-neutral-light"
      :class="{ 
        'bg-accent': useAccent, 
        'text-primary': useAccent,
        'bg-primary': !useAccent,
        'text-neutral-light': !useAccent,
      }">
      {{label}}
    </NuxtLink>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  label: String,
  url: String,
  useAccent: Boolean,
})
</script>

<style>

</style>