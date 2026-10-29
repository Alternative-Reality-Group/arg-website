<template>
  <section id="contact" class="bg-night text-paper">
    <div class="mx-auto grid max-w-6xl gap-12 px-4 py-20 sm:px-6 md:grid-cols-2 md:py-28">
      <div class="flex flex-col gap-6">
        <p class="eyebrow !text-muted-dark">Contact</p>
        <h2 class="text-4xl font-bold sm:text-5xl">Tell us about your product.</h2>
        <p class="max-w-md text-lg text-muted-dark">
          Where it stands, what's working and what's in the way. We reply to every enquiry within one business day.
        </p>
        <dl class="mt-4 flex flex-col gap-4">
          <div>
            <dt class="font-mono text-xs uppercase tracking-widest text-muted-dark">Email</dt>
            <dd><a href="mailto:contact@alternativereality.com" class="text-lg underline decoration-violet decoration-2 underline-offset-4 hover:text-violet-light">contact@alternativereality.com</a></dd>
          </div>
          <div>
            <dt class="font-mono text-xs uppercase tracking-widest text-muted-dark">Phone</dt>
            <dd><a href="tel:+18189002989" class="text-lg hover:text-violet-light">(818) 900-2989</a></dd>
          </div>
          <div>
            <dt class="font-mono text-xs uppercase tracking-widest text-muted-dark">Based in</dt>
            <dd class="text-lg">Woodland Hills, Los Angeles</dd>
          </div>
        </dl>
      </div>

      <div class="rounded-lg border border-line-dark bg-white/[0.03] p-6 sm:p-8">
        <p v-if="state === 'sent'" role="status" class="text-2xl font-display">
          Thank you. We've received your message and will reply within one business day.
        </p>
        <form v-else name="contact-form" method="post" class="flex flex-col gap-5" @submit.prevent="submit">
          <input type="hidden" name="form-name" value="contact-form" />
          <p hidden><label>Don't fill this out: <input name="bot-field" /></label></p>
          <div v-for="field in fields" :key="field.name" class="flex flex-col gap-2">
            <label :for="`f-${field.name}`" class="text-sm font-medium">
              {{ field.label }} <span v-if="!field.required" class="text-muted-dark">(optional)</span>
            </label>
            <textarea
              v-if="field.multiline"
              :id="`f-${field.name}`"
              :name="field.name"
              rows="5"
              :required="field.required"
              class="rounded-md border border-line-dark bg-night px-3 py-3 text-paper placeholder:text-muted-dark focus:border-violet focus:outline-none"
              :placeholder="field.placeholder"></textarea>
            <input
              v-else
              :id="`f-${field.name}`"
              :name="field.name"
              :type="field.type"
              :autocomplete="field.autocomplete"
              :required="field.required"
              class="min-h-[44px] rounded-md border border-line-dark bg-night px-3 text-paper placeholder:text-muted-dark focus:border-violet focus:outline-none"
              :placeholder="field.placeholder" />
          </div>
          <p v-if="state === 'error'" role="alert" class="text-red-300">
            Something went wrong sending that. Please try again, or email contact@alternativereality.com.
          </p>
          <button type="submit" class="btn mt-2 bg-violet text-white hover:bg-violet-dim disabled:opacity-60" :disabled="state === 'sending'">
            {{ state === "sending" ? "Sending…" : "Send message" }}
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
// Field names must match public/post-form.html, which Netlify uses to detect the form.
const fields = [
  { name: "name", label: "Name", type: "text", autocomplete: "name", required: true },
  { name: "email", label: "Email", type: "email", autocomplete: "email", required: true },
  { name: "company", label: "Company or product", type: "text", autocomplete: "organization", required: false },
  { name: "message", label: "About your product", multiline: true, required: true, placeholder: "What it does, how it was built so far, and what you need next." },
]

const state = ref("idle")

// Same event names and parameters as the previous site, so existing GA reports keep working.
const track = (name) => {
  if (typeof window.gtag === "function")
    window.gtag("event", name, { event_category: "contact", event_label: `manual_event_${name.toUpperCase()}`, value: 1 })
}

const submit = async (event) => {
  state.value = "sending"
  try {
    const response = await fetch("/post-form.html", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams(new FormData(event.target)).toString(),
    })
    if (!response.ok) throw new Error(`Form post failed: ${response.status}`)
    state.value = "sent"
    track("submit_lead_form")
  } catch {
    state.value = "error"
    track("submit_lead_form_error")
  }
}
</script>
