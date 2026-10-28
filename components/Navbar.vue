<script setup>
const menuitems = [
  {
    title: "About Us",
    url: "/about"
  },
  {
    title: "Contact",
    url: "/contact"
  },
  {
    title: "Log in",
    url: "/login",
  },
];
</script>

<template>
  <Container>
    <header class="flex flex-row flex-wrap items-center justify-between my-4 gap-x-6 gap-y-4">
      <div class="flex items-center justify-between">
        <a href="/" class="text-2xl"
          ><span class="font-bold text-zinc-800"><span class="text-green-500">&#10070;</span> Alternative Reality Group</span>
        </a>
      </div>
      <nav class="flex w-auto">
        <ul class="flex flex-row gap-3 text-sm">
          <li v-for="item of menuitems">
            <a
              :href="item.url"
              class="flex px-3 py-2 text-gray-600 border rounded hover:text-gray-900"
            >
              {{ item.title }}
            </a>
          </li>
        </ul>
      </nav>
    </header>
  </Container>
</template>
