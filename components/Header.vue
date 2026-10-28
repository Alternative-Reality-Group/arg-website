<template>
  <header class="fixed top-0 left-0 w-full bg-white shadow z-10">
    <div class="mx-auto flex items-center justify-between p-2">
      <!-- Logo -->

      <a href="/" class="text-2xl font-bold">
        <!-- you can disable it: -->
         <div class="w-full h-min">
          <IconHome class="w-auto h-24" :fontControlled="false" filled />
         </div>
      </a>
      <!-- Navigation Menu -->
      <nav class="hidden md:flex space-x-4">
        <ARGButton 
          :url="'/contact'"
          :label="'Contact Us'"
          :useAccent="true"
         />
      </nav>
      <!-- Mobile Menu Button -->
      <button @click="isMenuOpen = !isMenuOpen"" class="md:hidden">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
    <!-- Mobile Navigation Menu -->
    <nav v-if="isMenuOpen" class="md:hidden bg-white shadow">
      <a href="/contact" class="block px-4 py-2 hover:bg-accent0">Contact</a>
    </nav>
  </header>
  <div id="header-block" class="w-full -z-0"></div>
</template>

<script setup>

  import IconHome from '~/assets/img/LogoF.svg'
  // IconHome.props.filled = false;
  const isMenuOpen = ref(false) // Track whether the mobile menu is open
</script>

<style scoped>

</style>
