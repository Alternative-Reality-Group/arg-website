<template>
  <footer class="bg-black text-gray-400 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="flex items-center mb-4 md:mb-0">
          <LogoF alt="Alternative Reality Group Logo" class="h-8" />
        </div>
        <p class="text-sm">
          Copyright &copy; {{ new Date().getFullYear() }} Alternative Reality
          Group. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>
<script setup>
import LogoF from "~/assets/images/LogoF.svg?component"
</script>
