<template>
  <div>
    <SiteHeader />

    <main>
      <!-- Hero -->
      <section class="mx-auto grid max-w-6xl items-center gap-12 px-4 pb-20 pt-16 sm:px-6 md:grid-cols-[1fr_auto] md:pb-28 md:pt-24">
        <div class="flex max-w-2xl flex-col gap-6">
          <p class="eyebrow">A software company in Los Angeles</p>
          <h1 class="text-5xl font-bold leading-[1.05] sm:text-6xl">
            We build software products, and we ship them.
          </h1>
          <p class="text-xl text-ink/75">
            Alternative Reality Group is where Jim Kass builds and runs his own products. Two are live, three more
            are on the way, and a few times a year we build something for someone else.
          </p>
          <div class="mt-2 flex flex-wrap gap-3">
            <a href="#products" class="btn-primary">See the products</a>
            <a href="#contact" class="btn-secondary">Start a project</a>
          </div>
        </div>
        <img
          src="/brand/arg-mark-light.svg"
          alt=""
          width="53"
          height="78"
          class="hidden h-72 w-auto md:block lg:h-80" />
      </section>

      <!-- Products -->
      <section id="products" class="border-y border-line bg-white">
        <div class="mx-auto flex max-w-6xl flex-col gap-20 px-4 py-20 sm:px-6 md:gap-28 md:py-28">
          <div class="flex max-w-2xl flex-col gap-4">
            <p class="eyebrow">Products</p>
            <h2 class="text-4xl font-bold sm:text-5xl">What we've built</h2>
            <p class="text-lg text-ink/75">
              Each one is designed, built and run in-house. Some will grow into companies of their own.
            </p>
          </div>
          <ProductCard
            v-for="(product, i) in products"
            :key="product.name"
            v-bind="product"
            :flip="i % 2 === 1" />
          <div class="flex flex-col gap-10">
            <h3 class="font-mono text-sm uppercase tracking-widest text-muted">In development</h3>
            <div class="grid gap-12 md:grid-cols-3 md:gap-8">
              <ProjectTile v-for="project in upcoming" :key="project.name" v-bind="project" />
            </div>
          </div>
        </div>
      </section>

      <!-- Working with ARG -->
      <section class="mx-auto grid max-w-6xl gap-12 px-4 py-20 sm:px-6 md:grid-cols-2 md:py-28">
        <div class="flex flex-col gap-4">
          <p class="eyebrow">Work with us</p>
          <h2 class="text-4xl font-bold sm:text-5xl">A few outside builds a year</h2>
          <p class="text-lg text-ink/75">
            Most of what we make is our own. When we take on a project for someone else, it gets the same care: one
            team taking it from idea to launch, and staying around after.
          </p>
          <a href="#contact" class="btn-primary mt-4 self-start">Tell us about your project</a>
        </div>
        <dl class="flex flex-col divide-y divide-line border-y border-line">
          <div v-for="way in ways" :key="way.name" class="flex flex-col gap-2 py-6">
            <dt class="font-display text-xl font-bold">{{ way.name }}</dt>
            <dd class="text-ink/75">{{ way.text }}</dd>
          </div>
        </dl>
        <article class="grid items-center gap-8 rounded-lg border border-line bg-white p-6 sm:p-8 md:col-span-2 md:grid-cols-2 md:gap-12">
          <a href="https://travelcaremexico.com" class="block overflow-hidden rounded-md border border-line" aria-label="Visit TravelCareMexico">
            <img
              src="/img/products/travelcaremexico.webp"
              alt="The TravelCareMexico home page"
              width="1200"
              height="750"
              loading="lazy"
              class="aspect-[16/10] w-full object-cover object-top" />
          </a>
          <div class="flex flex-col gap-4">
            <span class="self-start rounded-full border border-ink/20 px-3 py-1 font-mono text-xs uppercase tracking-wider text-ink/70">Client project</span>
            <h3 class="text-3xl font-bold">TravelCareMexico</h3>
            <p class="text-lg text-ink/80">
              Travel assistance plans for visitors to Mexico, sold online with instant certificates and 24/7 bilingual
              help through a local partner.
            </p>
            <p class="text-ink/80">Taken from idea to launch: product design, engineering and go-to-market.</p>
            <a href="https://travelcaremexico.com" class="self-start font-medium underline decoration-violet decoration-2 underline-offset-4 hover:text-violet">
              travelcaremexico.com
            </a>
          </div>
        </article>
      </section>

      <!-- About -->
      <section id="about" class="border-t border-line bg-white">
        <div class="mx-auto grid max-w-6xl gap-12 px-4 py-20 sm:px-6 md:grid-cols-[1fr_2fr] md:py-28">
          <div class="flex flex-col gap-4">
            <p class="eyebrow">About</p>
            <h2 class="text-4xl font-bold sm:text-5xl">Jim Kass</h2>
            <p class="font-mono text-sm text-muted">Founder</p>
          </div>
          <div class="flex flex-col gap-5 text-lg text-ink/80">
            <p>
              Jim has spent 30 years in technology and entertainment. For more than a decade at Sony PlayStation he led
              product for the tools game developers and publishers use to work with PlayStation, including bringing
              generative AI into developer support.
            </p>
            <p>
              Before that he managed development at a motion picture digital asset management company, consulted on
              digital projects, and produced independent films. His first startup job was in 1995.
            </p>
            <p>
              Since 2024 he has run Alternative Reality Group, designing products and building them with AI coding agents.
            </p>
          </div>
        </div>
      </section>

      <ContactSection />
    </main>

    <SiteFooter />
  </div>
</template>

<script setup>
const products = [
  {
    name: "kidscancode",
    status: "Live · beta",
    live: true,
    summary: "Computer science for kids aged 8 to 10: how computers actually work, with real Python along the way.",
    facts: [
      "144 lessons, from binary and memory to Python, the internet and how AI works",
      "Kids sign in with a first name only: no email, no chat, no ads",
      "Free while in beta",
    ],
    url: "https://kidscancode.net",
    image: "/img/products/kidscancode.webp",
  },
  {
    name: "Bloginator",
    status: "Live",
    live: true,
    summary: "A writing companion for people who already have something to say. It writes with you, not for you.",
    facts: [
      "Sharpens your idea and drafts it in your own voice",
      "Publishes straight to WordPress.com or Ghost",
      "Free to start",
    ],
    url: "https://thebloginator.com",
    image: "/img/products/bloginator.webp",
  },
]

const upcoming = [
  {
    name: "Obosuru",
    status: "Coming to iPhone",
    summary:
      "A job tracker that saves each posting the moment you see it, fills in the application, and reads your inbox (read-only) so every status stays current.",
    image: "/img/products/obosuru.webp",
    imageAlt: "The Obosuru coming-soon page",
  },
  {
    name: "R U Interested",
    status: "Private beta",
    summary: "Discovery for what matters to you, your friends and your community.",
    image: "/img/products/ruinterested.webp",
    imageAlt: "The R U Interested home page",
    url: "https://ruinterested.com",
  },
  {
    name: "Hollywood Studio Simulator",
    status: "Working title · desktop game",
    summary: "Run a film studio: buy the script, sign the stars, and win the weekend box office.",
    image: "/img/products/studio-game.webp",
    imageAlt: "The game's main menu, with five generated film posters",
  },
]

const ways = [
  { name: "Build", text: "A defined product or feature, scoped up front, then designed, built and launched." },
  { name: "Advise", text: "Ongoing help with product, architecture and AI decisions for a founder or a team." },
  { name: "Partner", text: "On select projects, a share of the revenue in place of some or all of the fee." },
]
</script>
