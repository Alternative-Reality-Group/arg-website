<template>
  <Container>
    <About></About>
  </Container>
</template>

<script lang="ts" setup>
const { data: page } = await useAsyncData("about", () =>
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

<style>
</style>