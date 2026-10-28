<template>
  <article class="grid items-center gap-8 md:grid-cols-2 md:gap-12" :class="{ 'md:[&>*:first-child]:order-2': flip }">
    <a :href="url" class="group block overflow-hidden rounded-lg border border-line bg-white shadow-sm" :aria-label="`Visit ${name}`">
      <img
        :src="image"
        :alt="`The ${name} home page`"
        width="1200"
        height="750"
        loading="lazy"
        class="aspect-[16/10] w-full object-cover object-top transition-transform duration-500 group-hover:scale-[1.02] motion-reduce:transition-none" />
    </a>
    <div class="flex flex-col gap-4">
      <span
        class="self-start rounded-full border px-3 py-1 font-mono text-xs uppercase tracking-wider"
        :class="live ? 'border-emerald-700/30 text-emerald-800' : 'border-amber-700/30 text-amber-800'">
        {{ status }}
      </span>
      <h3 class="text-3xl font-bold">{{ name }}</h3>
      <p class="text-lg text-ink/80">{{ summary }}</p>
      <ul class="flex flex-col gap-2 text-ink/80">
        <li v-for="fact in facts" :key="fact" class="flex gap-3">
          <span aria-hidden="true" class="font-mono text-violet">/</span>
          <span>{{ fact }}</span>
        </li>
      </ul>
      <a :href="url" class="mt-2 self-start font-medium underline decoration-violet decoration-2 underline-offset-4 hover:text-violet">
        {{ host }}
      </a>
    </div>
  </article>
</template>

<script setup>
const props = defineProps({
  name: { type: String, required: true },
  status: { type: String, required: true },
  live: { type: Boolean, default: false },
  summary: { type: String, required: true },
  facts: { type: Array, default: () => [] },
  url: { type: String, required: true },
  image: { type: String, required: true },
  flip: { type: Boolean, default: false },
})

const host = computed(() => new URL(props.url).host)
</script>
