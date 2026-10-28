<template>
  <section id="founder" class="py-20 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="order-2 lg:order-1">
          <h2 class="text-4xl font-bold text-gray-900 mb-6">
            Built from shipped product, not just strategy advice
          </h2>
          <p class="text-lg text-gray-700 mb-6">
            Alternative Reality Group is led by a founder with deep roots in
            technology, entertainment, and artificial intelligence—spanning
            product development, engineering leadership, and applied AI.
          </p>
          <p class="text-lg text-gray-700 mb-6">
            Recent work includes launching TravelCareMexico.com, a travel
            platform built from idea to production. That kind of hands-on
            execution is what ARG brings to AI and software engagements: the
            ability to move from recommendation to working system.
          </p>
          <p class="text-lg text-gray-700 mb-8">
            Entertainment remains a core domain—content, metadata, production
            tooling, and distribution—but the underlying offer is the same for
            any operator trying to ship faster.
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
            <div class="bg-gray-50 border border-gray-200 rounded-lg p-5">
              <h4 class="font-semibold text-gray-900 mb-1">Background</h4>
              <p class="text-sm text-gray-600">
                Technology and entertainment experience across multiple roles and
                industries, with recent focus on applied AI and production systems.
              </p>
            </div>
            <div class="bg-gray-50 border border-gray-200 rounded-lg p-5">
              <h4 class="font-semibold text-gray-900 mb-1">Engagement style</h4>
              <p class="text-sm text-gray-600">
                Remote consulting, direct involvement with your team, and
                scoping engagements so you know the plan before a larger commitment.
              </p>
            </div>
          </div>

          <div class="flex flex-wrap gap-4">
            <button
              @click="$emit('scroll-to-section', 'contact')"
              class="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-500 transition-colors">
              Start a conversation
            </button>
            <button
              @click="$emit('scroll-to-section', 'current-work')"
              class="border border-gray-900 text-gray-900 px-6 py-3 rounded-lg font-medium hover:bg-gray-50 transition-colors">
              See current work
            </button>
          </div>
        </div>

        <div class="order-1 lg:order-2">
          <div class="relative">
            <img
              src="/image.png"
              alt="Founder"
              class="rounded-lg shadow-xl w-full h-auto"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import LogoF from "~/assets/images/LogoF.svg"

defineEmits(["scroll-to-section"])
</script>
