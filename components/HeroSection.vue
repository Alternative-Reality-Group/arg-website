<template>
  <section class="relative min-h-screen flex items-center overflow-hidden">
    <div class="absolute inset-0">
      <img
        src="/assets/images/backdrop2.png"
        alt=""
        class="w-full h-full object-cover"
      />
      <div class="absolute inset-0 bg-black/60"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <p class="text-blue-300 font-semibold tracking-wide mb-4">
          Alternative Reality Group
        </p>
        <h1 class="text-4xl md:text-6xl font-bold text-white mb-6 leading-tight">
          AI and software strategy for
          <span class="text-blue-400">founders and operators</span>.
        </h1>
        <p class="text-lg md:text-xl text-gray-200 mb-8 leading-relaxed">
          I work with founders and operators who need to move from AI curiosity
          to production-ready systems—and from prototype to real revenue. Recent
          work includes travel and entertainment, but the pattern is the same:
          idea to shipping product.
        </p>
        <div class="flex flex-col sm:flex-row gap-4">
          <button
            @click="$emit('scroll-to-section', 'contact')"
            class="bg-blue-600 text-white px-8 py-3 rounded-lg text-base font-semibold hover:bg-blue-500 transition-colors">
            Book a 30-minute call
          </button>
          <button
            @click="$emit('scroll-to-section', 'founder')"
            class="border border-white/80 text-white px-8 py-3 rounded-lg text-base font-medium hover:bg-white/10 transition-colors">
            About the founder
          </button>
        </div>
        <p class="text-gray-300 text-sm mt-4">
          Remote consultations · West Los Angeles based
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import LogoF from "~/assets/images/LogoF.svg"

const props = defineProps({
  scrollY: Number,
})

defineEmits(["scroll-to-section"])
</script>
