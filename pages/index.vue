<template>
  <div class="min-h-screen bg-white">
    <Navigation
      :scrolled="scrolled"
      :is-menu-open="isMenuOpen"
      @toggle-menu="toggleMenu"
      @scroll-to-section="scrollToSection" />

    <HeroSection @scroll-to-section="scrollToSection" />
    <AboutSection />
    <ServicesSection />
    <IndustriesSection />
    <PortfolioSection @scroll-to-section="scrollToSection" />
    <ContactSection />
    <Footer />
  </div>
</template>

<script setup>
const isMenuOpen = ref(false)
const scrolled = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const scrollToSection = (sectionId) => {
  const sectionMap = {
    'founder': 'founder',
    'what i do': 'services',
    'where i focus': 'industries',
    'current work': 'current-work',
    'contact': 'contact',
  }
  const targetId = sectionMap[sectionId.toLowerCase()] || sectionId
  const element = document.getElementById(targetId)
  if (element) {
    element.scrollIntoView({ behavior: "smooth" })
  }
  isMenuOpen.value = false
}

onMounted(() => {
  const handleScroll = () => {
    scrolled.value = window.scrollY > 50
  }

  window.addEventListener("scroll", handleScroll)

  onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll)
  })
})
</script>
