<template>
  <nav
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
      scrolled ? 'bg-white shadow-lg' : 'bg-transparent',
    ]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center min-h-16 py-2">
        <div class="flex items-center">
          <LogoF
            alt="Alternative Reality Group Logo"
            class="max-h-12 w-auto transition-all duration-300"
            :class="scrolled ? 'text-gray-900' : 'text-white'" />
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <button
            v-for="item in navItems"
            :key="item"
            @click="$emit('scroll-to-section', item.toLowerCase())"
            :class="[
              'font-medium transition-colors hover:text-blue-600',
              scrolled ? 'text-#353538' : 'text-white',
            ]">
            {{ item }}
          </button>
          <button
            @click="$emit('scroll-to-section', 'contact')"
            class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors">
            Get Started
          </button>
        </div>

        <!-- Mobile Navigation Button -->
        <button
          @click="$emit('toggle-menu')"
          :class="['md:hidden', scrolled ? 'text-gray-900' : 'text-white']">
          <Icon
            :name="isMenuOpen ? 'lucide:x' : 'lucide:menu'"
            class="h-6 w-6" />
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Menu -->
    <div v-if="isMenuOpen" class="md:hidden bg-white border-t shadow-lg">
      <div class="px-4 py-6 space-y-4">
        <button
          v-for="item in navItems"
          :key="item"
          @click="$emit('scroll-to-section', item.toLowerCase())"
          class="block w-full text-left text-gray-700 hover:text-blue-600 py-2">
          {{ item }}
        </button>
        <button
          @click="$emit('scroll-to-section', 'contact')"
          class="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
          Get Started
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import LogoF from "~/assets/images/LogoF.svg?component"

defineProps({
  scrolled: Boolean,
  isMenuOpen: Boolean,
})

defineEmits(["toggle-menu", "scroll-to-section"])

const navItems = ["Founder", "What I Do", "Where I Focus", "Current Work", "Contact"]
</script>
