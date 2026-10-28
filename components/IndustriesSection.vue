<template>
  <section id="industries" class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          Engagements
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Not every engagement looks the same. Most work fits one of these
          models, and I’ll recommend the right one after a short call.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-6 mb-16">
        <div
          v-for="model in models"
          :key="model.title"
          class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 class="text-lg font-bold text-gray-900 mb-3">{{ model.title }}</h3>
          <p class="text-gray-700 mb-3">{{ model.description }}</p>
          <p class="text-sm text-gray-600">{{ model.detail }}</p>
        </div>
      </div>

      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div>
          <div class="mb-8">
            <div class="flex items-center mb-4">
              <Icon name="lucide:film" class="h-8 w-8 text-blue-600 mr-3" />
              <h3 class="text-2xl font-bold text-gray-900">
                Entertainment & Media
              </h3>
            </div>
            <p class="text-gray-700 mb-4">
              Entertainment remains a core domain—content creation, metadata,
              production tooling, and distribution. The difference is that the
              same engagement models apply whether the product is a travel
              platform or a studio workflow tool.
            </p>
            <ul class="space-y-2">
              <li
                v-for="feature in entertainmentFeatures"
                :key="feature"
                class="flex items-center text-gray-600">
                <Icon
                  name="lucide:check-circle"
                  class="h-4 w-4 text-green-500 mr-2" />
                {{ feature }}
              </li>
            </ul>
          </div>

          <div class="grid gap-6">
            <div
              v-for="(industry, index) in otherIndustries"
              :key="index"
              class="bg-white p-6 rounded-lg shadow-sm">
              <h4 class="font-semibold text-gray-900 mb-2">
                {{ industry.title }}
              </h4>
              <p class="text-sm text-gray-600">{{ industry.description }}</p>
            </div>
          </div>
        </div>

        <div class="relative">
          <img
            src="https://images.pexels.com/photos/274937/pexels-photo-274937.jpeg"
            alt="Film clapperboard"
            class="rounded-lg shadow-xl" />
          <div
            class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-lg"></div>
          <div class="absolute bottom-6 left-6 text-white">
            <h4 class="text-xl font-bold mb-2">Operator-first engagements</h4>
            <p class="text-sm opacity-90">From idea to shipped product</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const models = [
  {
    title: "Standard consulting",
    description:
      "Scoped advisory and implementation work—strategy, system design, or hands-on building—with clear milestones and a fixed engagement shape.",
    detail:
      "Best for teams that know what they need and want an experienced operator to help execute it.",
  },
  {
    title: "1:1 training",
    description:
      "Direct mentorship for founders or engineering leads who want to level up their AI and software judgment faster.",
    detail:
      "Sessions are practical and product-focused, not theoretical. Good for operators who want to own the work after the engagement.",
  },
  {
    title: "Revenue participation",
    description:
      "For select projects, I’ll work on outcome terms instead of time-and-materials.",
    detail:
      "This is for operators who want a partner aligned to product and revenue milestones, not just deliverables.",
  },
]

const otherIndustries = [
  {
    title: "Travel & Consumer Products",
    description:
      "Recent proof point: TravelCareMexico.com, launched as a travel platform and brought to production. That’s the kind of founder-level execution I bring to engagements.",
  },
  {
    title: "Technology & SaaS",
    description:
      "Ready to support platform design, AI features, and go-to-market systems for early-stage and growth-stage products.",
  },
]

const entertainmentFeatures = [
  "AI-powered content tooling",
  "Content metadata and search",
  "Production workflow automation",
  "Digital asset and distribution systems",
]
</script>
