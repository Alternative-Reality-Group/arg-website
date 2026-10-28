const globalAnimationHasRunState = reactive({
  hasRun: false
})

export const useAnimationState = () => {
  
  const animationEnded = () => {
    console.log(`called animation ended:`)
    globalAnimationHasRunState.hasRun = true
  }

  return {
    globalAnimationHasRunState,
    animationEnded
  }
}

