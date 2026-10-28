<template>
  <section id="industries" class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          Industry Expertise
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Focused on entertainment with capabilities that extend across multiple
          industries.
        </p>
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
              Our primary focus is the entertainment industry, with solutions
              spanning content creation, distribution, audience analytics, and
              operational systems.
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

          <div class="grid grid-cols-2 gap-6">
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
            alt="Entertainment Industry"
            class="rounded-lg shadow-xl" />
          <div
            class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-lg"></div>
          <div class="absolute bottom-6 left-6 text-white">
            <h4 class="text-xl font-bold mb-2">Entertainment Focus</h4>
            <p class="text-sm opacity-90">
              Transforming how content is created, distributed, and consumed
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const otherIndustries = [
  {
    title: "Game Development / Distribution",
    description:
      "Prepared to develop intelligent operational tools, analytics, and distribution platforms",
  },
  {
    title: "Retail & E-commerce",
    description:
      "Equipped to create personalization, inventory optimization, and customer insights",
  },
  {
    title: "Technology",
    description:
      "Ready to build SaaS platforms, fintech, and enterprise software solutions",
  },
]

const entertainmentFeatures = [
  "AI-Powered Content Creation Tools",
  "AI-Powered Content Metadata Analysis",
  "AI-Augmented Analytics & Insights",
  "Digital Asset Management Systems",
  "Production Workflow Automation",
]
</script>
