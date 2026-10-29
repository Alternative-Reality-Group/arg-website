<template>
  <article class="flex flex-col gap-4">
    <component
      :is="url ? 'a' : 'div'"
      :href="url"
      class="block overflow-hidden rounded-lg border border-line bg-white shadow-sm"
      :aria-label="url ? `Visit ${name}` : undefined">
      <img
        :src="image"
        :alt="imageAlt"
        width="1200"
        height="750"
        loading="lazy"
        class="aspect-[16/10] w-full object-cover object-top" />
    </component>
    <span class="self-start rounded-full border border-amber-700/30 px-3 py-1 font-mono text-xs uppercase tracking-wider text-amber-800">
      {{ status }}
    </span>
    <h3 class="text-2xl font-bold">{{ name }}</h3>
    <p class="text-ink/80">{{ summary }}</p>
    <a v-if="url" :href="url" class="self-start font-medium underline decoration-violet decoration-2 underline-offset-4 hover:text-violet">
      {{ host }}
    </a>
  </article>
</template>

<script setup>
const props = defineProps({
  name: { type: String, required: true },
  status: { type: String, required: true },
  summary: { type: String, required: true },
  image: { type: String, required: true },
  imageAlt: { type: String, required: true },
  url: { type: String, default: "" },
})

const host = computed(() => (props.url ? new URL(props.url).host : ""))
</script>
