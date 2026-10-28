<template>
  <section id="contact" class="py-20 bg-gray-900 text-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-12">
        <div>
          <h2 class="text-4xl font-bold mb-6">
            Let's talk about your project
          </h2>
          <p class="text-xl text-gray-300 mb-8">
            Tell me what you're trying to build or where you're stuck. I'll give
            you a direct read on whether it's a fit, and what the next step
            should be.
          </p>

          <div class="space-y-6">
            <div
              v-for="(contact, index) in contactInfo"
              :key="index"
              class="flex items-start space-x-4">
              <div
                :class="[
                  'w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0',
                  contact.bgColor,
                ]">
                <Icon :name="contact.icon" class="h-5 w-5" />
              </div>
              <div>
                <h4 class="font-semibold mb-1">
                  {{ contact.title }}
                </h4>
                <template v-if="contact.type === 'phone'">
                  <a
                    :href="`tel:${contact.value.replace(/[^+\d]/g, '')}`"
                    class="text-blue-300 underline hover:text-white transition-colors">
                    {{ contact.value }}
                  </a>
                </template>
                <template v-else>
                  <p class="text-gray-300">{{ contact.value }}</p>
                </template>
                <p v-if="contact.subtitle" class="text-gray-400 text-sm">
                  {{ contact.subtitle }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-gray-800 p-8 rounded-xl">
          <div id="contact-form-error" class="hidden">
            <h1 class="text-3xl text-red-400">
              Sorry, something went wrong. Please try again or email me directly.
            </h1>
          </div>
          <div id="contact-form-success" class="hidden">
            <h1 class="text-3xl text-green-400">
              Thank you for your message. I'll respond within one business day.
            </h1>
          </div>
          <h3 id="contact-form-heading" class="text-xl font-bold mb-6">
            Send a message
          </h3>

          <form
            id="contact-form"
            method="post"
            name="contact-form"
            class="space-y-6"
            @submit.prevent="handleSubmit">
            <input type="hidden" name="form-name" value="contact-form" />

            <div>
              <label for="name" class="block text-sm font-medium mb-2"
                >Name</label
              >
              <input
                v-model="form.name"
                type="text"
                id="name"
                name="name"
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-500"
                placeholder="Your name"
                required />
            </div>

            <div hidden>
              <label>Don’t fill this out: <input name="bot-field" /></label>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium mb-2"
                >Email</label
              >
              <input
                v-model="form.email"
                type="email"
                id="email"
                name="email"
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-500"
                placeholder="you@company.com"
                required />
            </div>

            <div>
              <label for="company" class="block text-sm font-medium mb-2"
                >Company</label
              >
              <input
                v-model="form.company"
                type="text"
                id="company"
                name="company"
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-500"
                placeholder="Your company"
                required />
            </div>

            <div>
              <label for="message" class="block text-sm font-medium mb-2"
                >Project brief</label
              >
              <textarea
                v-model="form.message"
                id="message"
                rows="4"
                name="message"
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-500"
                placeholder="What are you building? What's the bottleneck?"
                required></textarea>
            </div>

            <button
              type="submit"
              class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-500 transition-colors font-medium">
              Send Message
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const form = ref({
  name: "",
  email: "",
  company: "",
  message: "",
})

const contactInfo = [
  {
    icon: "lucide:mail",
    title: "Email",
    value: "contact@alternativereality.com",
    bgColor: "bg-blue-600",
    type: "email",
  },
  {
    icon: "lucide:phone",
    title: "Phone",
    value: "+1 (818) 900-2989",
    bgColor: "bg-green-600",
    type: "phone",
  },
  {
    icon: "lucide:map-pin",
    title: "Location",
    value: "Woodland Hills, CA",
    subtitle: "Available for remote consulting worldwide",
    bgColor: "bg-purple-600",
    type: "location",
  },
]

const expectations = [
  "Free initial consultation to understand your needs",
  "Honest assessment of project feasibility",
  "Customized solution roadmap with clear milestones",
  "Transparent pricing with no hidden costs",
]

const handleSubmit = (event) => {
  const myForm = event.target
  const formData = new FormData(myForm)

  fetch("/post-form.html", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString(),
  })
    .then((r) => {
      if (r.ok) {
        document.getElementById("contact-form").classList.add("hidden")
        document.getElementById("contact-form-heading").classList.add("hidden")
        document
          .getElementById("contact-form-success")
          .classList.remove("hidden")
        // google analytics form submission
        window.gtag("event", "submit_lead_form", {
          event_category: "contact",
          event_label: "manual_event_SUBMIT_LEAD_FORM",
          value: 1,
        })
      } else {
        document.getElementById("contact-form").classList.add("hidden")
        document.getElementById("contact-form-heading").classList.add("hidden")
        document.getElementById("contact-form-error").classList.remove("hidden")
        // google analytics form submission error
        window.gtag("event", "submit_lead_form_error", {
          event_category: "contact",
          event_label: "manual_event_SUBMIT_LEAD_FORM_ERROR",
          value: 1,
        })
      }
    })
    .catch((error) => alert(error))
}
</script>
