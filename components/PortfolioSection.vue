<template>
  <section id="current-work" class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          Current Work
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Recent areas of focus and exploration in AI-assisted entertainment and media systems.
        </p>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        <div
          v-for="(project, index) in projects"
          :key="index"
          :class="[
            'rounded-xl p-8 hover:shadow-lg transition-all duration-300 bg-gradient-to-br',
            project.gradient,
          ]">
          <div
            :class="[
              'w-12 h-12 rounded-lg flex items-center justify-center mb-6',
              project.iconBg,
            ]">
            <Icon :name="project.icon" class="h-6 w-6 text-white" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-4">
            {{ project.title }}
          </h3>
          <p class="text-gray-700 mb-4">{{ project.description }}</p>
          <div v-if="project.tags.length">
            <span
              v-for="(tag, tagIndex) in project.tags"
              :key="tagIndex"
              :class="[
                'inline-block text-xs font-medium px-2 py-1 rounded bg-gray-100 text-gray-700',
                tagIndex > 0 ? 'ml-2' : '',
              ]">
              {{ tag.name }}
            </span>
          </div>
        </div>
      </div>

      <div class="text-center mt-12">
        <button
          @click="$emit('scroll-to-section', 'contact')"
          class="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors inline-flex items-center gap-2">
          Discuss Your Project
          <Icon name="lucide:arrow-right" class="h-5 w-5" />
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
defineEmits(["scroll-to-section"])

const projects = [
  {
    icon: "lucide:brain",
    title: "AI Content Development Tools",
    description:
      "AI-powered solutions to streamline script development, marketing copy, and long-form content creation for writers, producers, and creative teams.",
    gradient: "from-blue-50 to-blue-100",
    iconBg: "bg-blue-600",
    tags: [{ name: "AI-Assisted Story Development" }],
  },
  {
    icon: "lucide:code",
    title: "AI Footage Analysis & Logging",
    description:
      "Automated scene detection and content tagging to simplify post-production workflows and accelerate content discovery from raw footage.",
    gradient: "from-green-50 to-green-100",
    iconBg: "bg-green-600",
    tags: [{ name: "Automated Footage Logging" }],
  },
  {
    icon: "lucide:trending-up",
    title: "AI Video Production & Prompt Tools",
    description:
      "Bridging creative vision and AI-generated video with tools that convert scripts into structured prompts and manage iterative refinement workflows.",
    gradient: "from-purple-50 to-purple-100",
    iconBg: "bg-purple-600",
    tags: [{ name: "Script-to-Video Workflows" }],
  },
]
</script>
