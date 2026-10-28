<script setup>
const props = defineProps({
  title: {
    type: String,
    required: false,
  },
  description: {
    type: String,
    required: false,
  },
  items: [
    { 
      title: String, 
      imageUrl: String, 
      description: String 
    },
  ],
});
</script>

<template>
    <h2 class="z-50 mt-3.5 text-3xl text-left p-6 sm:text-5xl" v-if="title">
      {{ title }}  <p class="inline">&#x21C1;</p>
    </h2>
    <div class="grid mx-12 md:grid-cols-3 gap-8">
      <div
        class="m-0 p-0" 
        v-for="item of items"
      >
        <Feature 
          :title = item.title
          :imageUrl = item.imageUrl
          :description = item.description
        >
        </Feature>
      </div>
    </div>

</template>
