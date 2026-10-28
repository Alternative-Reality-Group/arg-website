<script lang="ts" setup>
const config = useRuntimeConfig()
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: false,
  },
  imageUrl: {
    type: String,
    required: true,
  }
})
</script>

<template>
  <div class="slide-up relative">
    <p class="pb-2 border-l-4 border-b-2 pl-2 text-2xl" v-if="title">{{ title }}</p>
    <div class="relative">
      <NuxtImg :src="imageUrl" class="border-black w-full shadow-md border-2 hover-reveal" />
      <div class="">
        <p class="absolute font-thin top-0 text-neutral-light text-justify opacity-0 hover:opacity-90 bg-primary overflow-scroll h-full w-full p-5" v-if="description">{{ description }}</p>
      </div>
    </div>
  </div>
</template>



<style>

</style>