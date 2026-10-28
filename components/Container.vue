<template>
  <div :id="containerId" class="grid gap-0 max-w-full relative">
    <slot />
  </div>
</template>

<script setup>
const props = defineProps({
  containerId: String,
})


onMounted(() => {
  if (import.meta.client) {

    // const {animationRunning, endAnimation} = useAnimationState()
    const divs = document.querySelectorAll('div[class*="slide-"] > div');

    let observer = new IntersectionObserver(sections => {
      sections.forEach(section => {
        if (section.intersectionRatio > 0.25) {
          section.target.classList.add('animate');
        } else if (section.intersectionRatio < 0.35) {
          section.target.classList.remove('animate');
        }
      });
    }, { threshold: [0.0, 0.10, 0.20, 0.25, 0.5, 0.75, 1], rootMargin: "-110px 0px 0px 0px", });

    divs.forEach(section => observer.observe(section))




  }
}); 
</script>

