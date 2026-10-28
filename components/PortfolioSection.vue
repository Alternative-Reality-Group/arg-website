<template>
  <section id="current-work" class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          Current Work
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Recent areas of focus and execution—from shipping products to
          building AI-assisted systems for operators.
        </p>
      </div>

      <div class="grid lg:grid-cols-2 gap-12 items-center mb-16">
        <div>
          <h3 class="text-2xl font-bold text-gray-900 mb-4">TravelCareMexico.com</h3>
          <p class="text-gray-700 mb-4">
            A travel platform launched from idea to production. This is the kind
            of founder-level execution ARG brings to engagements: product design,
            engineering, and go-to-market—not just recommendations.
          </p>
          <p class="text-gray-700 mb-6">
            For select projects, I’m open to revenue-participation terms instead
            of pure advisory billing. That means I’m aligned to product and
            revenue milestones, not just deliverables.
          </p>
          <button
            @click="$emit('scroll-to-section', 'contact')"
            class="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-500 transition-colors">
            Discuss your project
          </button>
        </div>
        <a href="https://travelcaremexico.com" class="block" aria-label="Visit TravelCareMexico.com">
          <img
            src="/images/travelcaremexico.webp"
            alt="The TravelCareMexico.com home page"
            width="1200"
            height="750"
            loading="lazy"
            class="rounded-lg shadow-xl w-full h-auto" />
        </a>
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
              {{ tag }}
            </span>
          </div>
        </div>
      </div>

      <div class="text-center mt-20 mb-10">
        <h3 class="text-2xl font-bold text-gray-900 mb-2">Also from ARG</h3>
        <p class="text-gray-600">
          ARG builds software for itself and for clients—same discipline,
          different products.
        </p>
      </div>
      <div class="grid md:grid-cols-3 gap-6">
        <div
          v-for="item in alsoFromArg"
          :key="item.description"
          class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h4 class="font-semibold text-gray-900 mb-2">{{ item.title }}</h4>
          <p class="text-sm text-gray-600 mb-3">{{ item.description }}</p>
          <a
            v-if="item.url"
            :href="item.url"
            class="text-sm font-medium text-blue-600 hover:text-blue-500">
            {{ item.linkText }}
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineEmits(["scroll-to-section"])

const projects = [
  {
    icon: "lucide:plane",
    title: "TravelCareMexico.com",
    description:
      "Travel platform launched from idea to production. Product design, engineering, and go-to-market execution.",
    gradient: "from-blue-50 to-blue-100",
    iconBg: "bg-blue-600",
    tags: ["Product launch", "Travel"],
  },
  {
    icon: "lucide:clapperboard",
    title: "Entertainment AI Tooling",
    description:
      "AI-assisted content tooling, metadata systems, and production workflow automation for media operators.",
    gradient: "from-purple-50 to-purple-100",
    iconBg: "bg-purple-600",
    tags: ["AI tooling", "Entertainment"],
  },
  {
    icon: "lucide:compass",
    title: "Operator Advisory",
    description:
      "Ongoing engagements with founders and operators on AI strategy, software systems, and get-to-market execution.",
    gradient: "from-green-50 to-green-100",
    iconBg: "bg-green-600",
    tags: ["Advisory", "AI strategy"],
  },
]

const alsoFromArg = [
  {
    title: "Bloginator",
    description: "AI-assisted writing companion. A product ARG is building and operating itself.",
    url: "https://thebloginator.com",
    linkText: "thebloginator.com →",
  },
  {
    title: "Future project",
    description: "ARG incubates operator-grade software alongside client work. More to show here soon.",
  },
  {
    title: "Future project",
    description: "Another internal or partnered product in progress. Check back for updates.",
  },
]
</script>
