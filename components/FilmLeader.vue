<template>
  <div class="z-40 fade-out hide-effect" @animationend="endAnimationHandler" id="leader-container">
    <div class="noise absolute h-full w-full film-grain-fx"></div>
    <div @animationiteration="increaseCounter" class="screen">
      <div class="noise h-full w-full film-grain-fx"></div>
    </div>
    <div class="lines"></div>
    <div class="number">{{ counter }}</div>
  </div>
</template>

<script setup>
  const animationHasRun = useState('animationHasRun')
  const displayLeader = ref(false)
  onMounted(()=>{
    if (import.meta.client) {
      if (!animationHasRun.value) {
      displayLeader.value = true
      } else {
        const leaderContainer = document.getElementById('leader-container');
        leaderContainer.classList.remove('hide-effect')
      }
    }
  })
  const bgImage = ref("");
  const config = useRuntimeConfig()
  const counter_start = 3
  const counter = ref(counter_start)
  const noiseImg = `url("/img/noise.png")`
  const increaseCounter = (event) => {
    if (event.animationName.startsWith('spin') ) {
      console.dir(event)
      counter.value = counter.value - 1
    }
  }

  const endAnimationHandler = (event) => {
    displayLeader.value=false
    animationHasRun.value = true
    const leaderContainer = document.getElementById('leader-container');
    bgImage.value = noiseImg
    leaderContainer.classList.add('film-grain-fx')
    leaderContainer.classList.remove('hide-effect')

  }

  onMounted(()=>{
    if (import.meta.client)  {
    }
  })

</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap");


#leader-container {
  margin: 0;
  position: absolute;
  top: calc( 0px - var(--header-height));
  left: 0;
  height:100%;
  width:100%;
  padding: 0;
  display: flex;
  box-sizing: border-box;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: "Roboto", sans-serif;
  overflow: hidden;
  box-shadow: inset 0 0 5em 1em #000;
  background-color: #efefef;
  background-image: v-bind(bgImage);
  clip-path:inset(0 0 var(--banner-height) 0);
}

.lines {
  display: v-bind("displayLeader ? 'inherit' : 'none'");
}

.lines::before {
  content: "";
  top: 50%;
  transform: translatey(-50%);
  left: 0;
  height: 8px;
  background: #000;
  width: 100%;
  position: absolute;
}

.lines::after {
  content: "";
  top: 0;
  left: 50%;
  transform: translatex(-50%);
  width: 8px;
  background: #000;
  height: 100vh;
  position: absolute;
}

.screen {
  clip-path: polygon(50% 50%, 50% 0, 100% 0, 100% 100%, 0 100%, 0 0, 50% 0);
  background: #e1e1e1;
  position: absolute;
  height: calc(100vh + 100vw);
  width: calc(100vh + 100vw);
  animation: spin 1000ms linear;
  animation-iteration-count: v-bind("counter_start");
  background-color: #4f4f4f;
  opacity: 0.5;
  display: v-bind("displayLeader ? 'flex' : 'none'");

}

@keyframes spin {
  0% {
    clip-path: polygon(50% 50%, 50% 0, 100% 0, 100% 100%, 0 100%, 0 0, 50% 0);
  }
  12.5% {
    clip-path: polygon(50% 50%, 100% 0, 100% 0, 100% 100%, 0 100%, 0 0, 50% 0);
  }
  37.5% {
    clip-path: polygon(50% 50%, 100% 100%, 100% 100%, 100% 100%, 0 100%, 0 0, 50% 0);
  }
  62.5% {
    clip-path: polygon(50% 50%, 0 100%, 0 100%, 0 100%, 0 100%, 0 0, 50% 0);
  }
  87.5% {
    clip-path: polygon(50% 50%, 0 0, 0 0, 0 0, 0 0, 0 0, 50% 0);
  }
  100% {
    clip-path: polygon(50% 50%, 50% 0, 50% 0, 50% 0, 50% 0, 50% 0, 50% 0);
  }
}

.number {
  font-size: 18rem;
  position: relative;
  display: v-bind("displayLeader ? 'inherit' : 'none'");
}

.number::after,
.number::before {
  content: "";
  border: #f7f7f7 solid 12px;
  border-radius: 50%;
  position: absolute;
}

.number::before {
  width: 480px;
  height: 480px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.number::after {
  width: 400px;
  height: 400px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.noise {
  background-image: v-bind(noiseImg);
  opacity: 0.5;
}


</style>