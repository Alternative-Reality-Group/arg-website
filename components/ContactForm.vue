<script setup>
const config = useRuntimeConfig()
const imageUrl = "/img/contact.avif"
const email = ref("")

const handleSubmit = (event) => {
  console.log("Submitting Form")
  console.log(event)

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
      } else {
        document.getElementById("contact-form").classList.add("hidden")
        document.getElementById("contact-form-heading").classList.add("hidden")
        document.getElementById("contact-form-error").classList.remove("hidden")
      }
    })
    .catch((error) => alert(error))
}

onMounted(() => {
  if (import.meta.client) {
    email.value = "info@alternativereality.com"
  }
})
</script>

<template>
  <div class="lg:grid m-8 lg:grid-cols-2 gap-4 sm:flex-1">
    <div>
      <h1 class="text-5xl mb-8 font-black">Contact</h1>
    </div>
    <div>
      <div class="text-xl">
        <p class="">22704 Ventura Blvd, Unit #355</p>
        <p>Woodland Hills, CA 91364</p>
        <div class="relative group">
          <p class="mt-4">
            <a
              class="hover:border-b-primary hover:border-b-2"
              href="tel:818-900-2989"
              >818-900-2989</a
            >
          </p>
          <div
            class="absolute top-0 -translate-x-full -left-4 mb-2 w-max px-2 py-1 text-sm text-white bg-gray-700 rounded shadow-lg opacity-0 group-hover:opacity-100">
            Click to call
          </div>
        </div>
        <div class="relative">
          <p class="mt-4">
            <a
              class="hover:border-b-primary hover:border-b-2"
              :href="`mailto:${email}`"
              >{{ email }}</a
            >
          </p>
        </div>
      </div>
    </div>
    <div class="border-t-4 col-span-2 h-2 m-8"></div>
    <div class="m-8">
      <NuxtImg
        :src="imageUrl"
        class="border-black w-full sticky shadow-md border-0" />
    </div>
    <div class="pb-8 m-8">
      <div id="contact-form-error" class="hidden">
        <h1 class="text-3xl text-red-600">
          Sorry we are having an issue with our form submission, please try
          again later, or contact us via the email above.
        </h1>
      </div>
      <h2 id="contact-form-heading" class="text-4xl">
        Tell us about your next project
      </h2>
      <form
        id="contact-form"
        method="post"
        name="contact-form"
        class="flex gap-4 flex-col mt-10"
        @submit.prevent="handleSubmit">
        <input type="hidden" name="form-name" value="contact-form" />

        <div class="form-fields">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold">
            Name
          </label>
          <input
            class="bg-neutral-200"
            type="text"
            id="f_name"
            name="name"
            aria-required="true"
            required />
        </div>
        <div hidden>
          <label>Don’t fill this out: <input name="bot-field" /></label>
        </div>

        <div class="form-fields">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold">
            Company
          </label>
          <input
            class="bg-neutral-200"
            type="text"
            id="f_company"
            name="company"
            aria-required="true"
            required />
        </div>

        <div class="form-fields">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold">
            Email
          </label>
          <input
            class="bg-neutral-200"
            type="email"
            id="f_email"
            name="email"
            aria-required="true"
            required />
        </div>

        <div class="form-fields">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold">
            Message
          </label>
          <textarea
            row="8"
            class="bg-neutral-200"
            id="f_message"
            name="message"
            aria-required="true"
            required></textarea>
        </div>
        <div class="block">
          <button
            type="submit"
            class="inline-flex shadow-md border-1 px-7 py-2 duration-500 border-black text-neutral-light bg-primary hover:text-neutral-light hover:bg-neutral-dark">
            Send message
          </button>
        </div>
      </form>
      <div id="contact-form-success" class="hidden">
        <h1 class="text-3xl">
          Thanks for your request. We will be in touch soon!
        </h1>
      </div>
    </div>
  </div>
</template>

<style scoped>
.form-fields {
  position: flex;
}

input[type="text"],
input[type="email"],
textarea {
  padding: 8px 8px 12px 2px;
  width: 100%;
}

label input:required,
label textarea:required {
  content: " *";
  color: red;
}
</style>
