<script setup>
  const config = useRuntimeConfig()
  const { data: page } = await useAsyncData("index", () =>
    queryContent("/").findOne()
  );
  if (!page.value) {
    throw createError({
      statusCode: 404,
      statusMessage: "Page not found",
      fatal: true,
    });
  }
  definePageMeta({
    layout: "default",
  });
</script>

<template>
   <Container>
    <ContactForm></ContactForm>
  </Container>
</template>


<style scoped>
  
</style>