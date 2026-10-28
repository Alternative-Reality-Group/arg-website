<template>
  <section id="services" class="py-20 bg-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-gray-900 mb-4">
          What I do
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Engagements around AI strategy, custom software, training, and
          hands-on get-to-market work—mostly for founders and operators.
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-8">
        <div
          v-for="(service, index) in services"
          :key="index"
          class="bg-white rounded-xl border border-gray-200 hover:shadow-xl transition-all duration-300">
          <div class="p-8">
            <div
              :class="[
                'w-12 h-12 rounded-lg flex items-center justify-center mb-6',
                service.iconBg,
              ]">
              <Icon :name="service.icon" class="h-6 w-6 text-white" />
            </div>
            <h3 class="text-lg font-bold text-gray-900 mb-2">
              {{ service.title }}
            </h3>
            <p class="text-gray-600 text-sm mb-4">
              {{ service.description }}
            </p>
            <ul class="space-y-2">
              <li
                v-for="feature in service.features"
                :key="feature"
                class="flex items-center text-sm text-gray-700">
                <Icon
                  name="lucide:check-circle"
                  class="h-4 w-4 text-green-600 mr-2" />
                {{ feature }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  {
    icon: "lucide:map",
    title: "AI Strategy",
    description:
      "Practical AI roadmaps for founders and operators who know AI matters but aren't sure where to start.",
    iconBg: "bg-blue-600",
    features: [
      "Readiness assessment",
      "Use-case prioritization",
      "Vendor and tooling selection",
    ],
  },
  {
    icon: "lucide:code",
    title: "Custom Software & AI Systems",
    description:
      "Production software, AI-assisted tooling, and integrations built for real workflows.",
    iconBg: "bg-green-600",
    features: [
      "AI-powered applications",
      "Machine learning systems",
      "Metadata and content pipelines",
    ],
  },
  {
    icon: "lucide:rocket",
    title: "Get-to-Market Advisory",
    description:
      "Direct support for taking a product from prototype to real usage and revenue.",
    iconBg: "bg-purple-600",
    features: [
      "Launch planning",
      "Growth loops and feedback",
      "Operational readiness",
    ],
  },
  {
    icon: "lucide:bar-chart-3",
    title: "Analytics & Insights",
    description:
      "Data systems that turn messy operational and audience data into actionable insight.",
    iconBg: "bg-orange-600",
    features: [
      "Predictive analytics",
      "Business intelligence",
      "Data visualization",
    ],
  },
  {
    icon: "lucide:users",
    title: "Technical Advisory",
    description:
      "Ongoing guidance for architecture, performance, and AI implementation decisions.",
    iconBg: "bg-indigo-600",
    features: [
      "Architecture review",
      "Performance optimization",
      "Implementation support",
    ],
  },
  {
    icon: "lucide:presentation",
    title: "Workshops & Enablement",
    description:
      "Focused sessions to align stakeholders and accelerate AI adoption inside your team.",
    iconBg: "bg-teal-600",
    features: [
      "Ideation sessions",
      "Proof of concepts",
      "Team training",
    ],
  },
]
</script>
