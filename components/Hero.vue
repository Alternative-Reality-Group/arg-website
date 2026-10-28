<script setup>

  const animationHasRunRef = ref(false)
  const animationHasRun = useState('animationHasRun', ()=>animationHasRunRef)

  const config = useRuntimeConfig()
  const noiseImg = `url("/img/noise.png")`
  const props = defineProps({
      title: {
        type: String,
        required: false,
      },
      description: {
        type: String,
        required: false,
      },
      imageUrl: {
        type: String,
        required: false,
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
  });
</script>

<template>
   <FilmLeader></FilmLeader>
  <div class="relative bg-neutral-dark w-full shadow-lg">
    <NuxtImg
      class="w-full hero-clip h-fit"
      :src="imageUrl"
      alt="Abstract flowing background image"
      loading="eager"
      format="avif"
      width="100%"
    />

    <div id="hero-container" class="text-4xl absolute left-0 p-4 bottom-6 text-pretty padding slide-left">
      <div>
        <h1 class="text-4xl text-white shadow-sm font-bold sm:text-5xl text-balance" v-if="title">{{ title }}</h1>
        <p class="max-w-xl mt-4 text-lg text-slate-100 sm:text-xl" v-if="description">
          {{ description }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
