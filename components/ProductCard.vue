<template>
  <article class="grid items-center gap-8 md:grid-cols-2 md:gap-12" :class="{ 'md:[&>*:first-child]:order-2': flip }">
    <div class="relative overflow-hidden rounded-lg border border-line bg-white shadow-sm">
      <div
        ref="frame"
        tabindex="0"
        role="region"
        :aria-label="`${name} home page preview, scrollable`"
        class="aspect-[16/10] w-full overflow-y-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
        @scroll.passive="onScroll">
        <a :href="url" :aria-label="`Visit ${name}`" class="block">
          <img
            :src="image"
            :alt="`The ${name} home page`"
            width="1200"
            height="750"
            loading="lazy"
            class="block h-auto w-full"
            @load="measure" />
        </a>
      </div>
      <div
        aria-hidden="true"
        class="pointer-events-none absolute inset-x-0 bottom-0 flex h-20 items-end justify-center bg-gradient-to-t from-ink/40 to-transparent pb-3 transition-opacity duration-300 motion-reduce:transition-none"
        :class="scrollable && !atEnd ? 'opacity-100' : 'opacity-0'">
        <span class="rounded-full bg-white/90 px-3 py-1 font-mono text-xs uppercase tracking-wider text-ink shadow-sm">
          <span class="hidden [@media(hover:hover)]:inline">Scroll to explore</span>
          <span class="[@media(hover:hover)]:hidden">Swipe to explore</span>
        </span>
      </div>
    </div>
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

// The preview frame scrolls like the real page. Only show the hint when the
// image is actually taller than the frame, and hide it once the end is reached.
const frame = ref(null)
const scrollable = ref(false)
const atEnd = ref(false)

function measure() {
  const el = frame.value
  if (!el) return
  scrollable.value = el.scrollHeight > el.clientHeight + 8
  onScroll()
}

function onScroll() {
  const el = frame.value
  if (!el) return
  atEnd.value = el.scrollTop + el.clientHeight >= el.scrollHeight - 8
}

onMounted(() => {
  measure()
  window.addEventListener('resize', measure)
})
onBeforeUnmount(() => window.removeEventListener('resize', measure))
</script>
