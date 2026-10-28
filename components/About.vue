
<script setup>
const config = useRuntimeConfig()
const props = defineProps({
  imageUrl: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  buttons: [
    {
      label: {
        type: String,
        required: false,
      },
      url: {
        type: String,
        required: false,
      },
    },
  ],
})

// Auth
// const { loggedIn, user, session, fetch, clear } = useUserSession()
</script>

<template>
  
  <div class="slide-up shadow-inner">
    <div
    id="about-section"
    class="relative w-full shadow-lg mt-8"
    >
      <NuxtImg
        class="absolute w-full top-0 left-0 h-full object-cover"
        :src="imageUrl"
        alt="image of handheld film camera"
        loading="eager"
        format="avif"
        width="100%"
      />
      <div class="absolute left-0 top-8">
        <h1 class="pl-10 text-4xl text-neutral-light shadow-sm font-bold sm:text-5xl text-balance" v-if="title">{{ title }}</h1>
        <p class=" pl-10 pr-10 max-w-xl mt-4 text-lg text-neutral-light sm:text-xl" v-if="description">
          {{ description }}
        </p>
        <div class="flex flex-wrap gap-4 p-8">
        <div v-for="button of buttons">
          <NuxtLink v-if="button.label && button.url" :href="button.url" class="shadow-md inline-flex border-1 border-neutral-dark px-7 py-2 text-neutral-light bg-primary duration-500 hover:text-neutral-dark hover:bg-neutral-light">{{button.label}}</NuxtLink>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>



<style>

</style>