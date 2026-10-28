<script setup>
import ARGButton from './ARGButton.vue';

const props = defineProps({
  title: {
    type: String,
    required: false,
  },
  description: {
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
  <div class="slide-up">
    <div
      class="flex flex-col items-center px-10 py-10 mx-auto text-center border-2 border-none bg-primary text-neutral-light sm:px-20 sm:py-20"
    >
      <h2 class="text-4xl font-bold sm:text-5xl" v-if="title">{{title}}</h2>
      <p class="mt-4 text-lg text-zinc-600 sm:text-xl" v-if="description">
        {{ description }}
      </p>
      <div v-for="button of buttons">
      <ARGButton 
        :url="button.url"
        :label="button.label"
        :useAccent="true"
      />
      </div>
    </div>
  </div>
</template>
