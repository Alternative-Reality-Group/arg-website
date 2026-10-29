<template>
  <div>
    <SiteHeader />

    <main>
      <!-- Hero -->
      <section class="mx-auto grid max-w-6xl items-center gap-12 px-4 pb-20 pt-16 sm:px-6 md:grid-cols-[1fr_auto] md:pb-28 md:pt-24">
        <div class="flex max-w-2xl flex-col gap-6">
          <p class="eyebrow">AI-native product company · Los Angeles</p>
          <h1 class="text-5xl font-bold leading-[1.05] sm:text-6xl">
            Your prototype works. Now make it a business.
          </h1>
          <p class="text-xl text-ink/75">
            Alternative Reality Group partners with founders who have built something with AI, whether it's a
            vibe-coded prototype or an early release, and need the strategy, architecture and launch plan to turn it
            into a product that lasts.
          </p>
          <div class="mt-2 flex flex-wrap gap-3">
            <a href="#contact" class="btn-primary">Discuss your product</a>
            <a href="#portfolio" class="btn-secondary">View our portfolio</a>
          </div>
        </div>
        <img
          src="/brand/arg-mark-light.svg"
          alt=""
          width="53"
          height="78"
          class="hidden h-72 w-auto md:block lg:h-80" />
      </section>

      <!-- What we do -->
      <section id="services" class="border-y border-line bg-white">
        <div class="mx-auto flex max-w-6xl flex-col gap-14 px-4 py-20 sm:px-6 md:py-28">
          <div class="flex max-w-2xl flex-col gap-4">
            <p class="eyebrow">What we do</p>
            <h2 class="text-4xl font-bold sm:text-5xl">Everything between a working demo and a real launch</h2>
            <p class="text-lg text-ink/75">
              A prototype proves the idea. Customers, investors and app stores expect more. We fill in what a prototype
              skips, starting from wherever your product is today.
            </p>
          </div>
          <dl class="grid gap-x-12 gap-y-10 sm:grid-cols-2 lg:grid-cols-3">
            <div v-for="service in services" :key="service.name" class="flex flex-col gap-2 border-t border-line pt-5">
              <dt class="font-display text-xl font-bold">{{ service.name }}</dt>
              <dd class="text-ink/75">{{ service.text }}</dd>
            </div>
          </dl>
          <p class="max-w-2xl text-ink/75">
            Our own products run on the same playbook, from Obosuru's brand book to Bloginator's KPI dashboards and
            launch plan.
          </p>
        </div>
      </section>

      <!-- How we work -->
      <section class="bg-night text-paper">
        <div class="mx-auto grid max-w-6xl gap-12 px-4 py-20 sm:px-6 md:grid-cols-2 md:py-28">
          <div class="flex flex-col gap-4">
            <p class="eyebrow !text-muted-dark">How we work</p>
            <h2 class="text-4xl font-bold sm:text-5xl">We work as partners</h2>
            <p class="text-lg text-muted-dark">
              Our preferred model is revenue participation. Rather than billing up front, we're paid from a share of
              your sales, so we only do well when the product does. We take no ownership in your company. If that
              isn't the right fit, we also offer training and fixed-scope projects.
            </p>
            <a href="#contact" class="btn mt-4 self-start bg-violet text-white hover:bg-violet-dim">Discuss your product</a>
          </div>
          <dl class="flex flex-col divide-y divide-line-dark border-y border-line-dark">
            <div v-for="model in models" :key="model.name" class="flex flex-col gap-2 py-6">
              <dt class="font-display text-xl font-bold">{{ model.name }}</dt>
              <dd class="text-muted-dark">{{ model.text }}</dd>
            </div>
          </dl>
        </div>
      </section>

      <!-- Portfolio -->
      <section id="portfolio" class="bg-white">
        <div class="mx-auto flex max-w-6xl flex-col gap-20 px-4 py-20 sm:px-6 md:gap-28 md:py-28">
          <div class="flex max-w-2xl flex-col gap-4">
            <p class="eyebrow">Portfolio</p>
            <h2 class="text-4xl font-bold sm:text-5xl">Our own products</h2>
            <p class="text-lg text-ink/75">
              We build and run our own products with the process we bring to founders. Some will become companies of
              their own.
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

      <!-- Client work -->
      <section class="border-t border-line">
        <div class="mx-auto flex max-w-6xl flex-col gap-10 px-4 py-20 sm:px-6 md:py-28">
          <div class="flex flex-col gap-4">
            <p class="eyebrow">Client work</p>
          </div>
          <article class="grid items-center gap-8 md:grid-cols-2 md:gap-12">
            <a href="https://travelcaremexico.com" class="block overflow-hidden rounded-lg border border-line bg-white shadow-sm" aria-label="Visit TravelCareMexico">
              <img
                src="/img/products/travelcaremexico.webp"
                alt="The TravelCareMexico home page"
                width="1200"
                height="750"
                loading="lazy"
                class="aspect-[16/10] w-full object-cover object-top" />
            </a>
            <div class="flex flex-col gap-4">
              <span class="self-start rounded-full border border-ink/20 px-3 py-1 font-mono text-xs uppercase tracking-wider text-ink/70">Client engagement</span>
              <h3 class="text-3xl font-bold">TravelCareMexico</h3>
              <p class="text-lg text-ink/80">
                An online travel assistance service for visitors to Mexico, with instant coverage certificates and 24/7
                bilingual support through a local partner.
              </p>
              <p class="text-ink/80">We took it from concept to launch, covering product design, engineering and go-to-market.</p>
              <a href="https://travelcaremexico.com" class="self-start font-medium underline decoration-violet decoration-2 underline-offset-4 hover:text-violet">
                travelcaremexico.com
              </a>
            </div>
          </article>
        </div>
      </section>

      <!-- About -->
      <section id="about" class="border-t border-line bg-white">
        <div class="mx-auto grid max-w-6xl gap-12 px-4 py-20 sm:px-6 md:grid-cols-[1fr_2fr] md:py-28">
          <div class="flex flex-col gap-4">
            <p class="eyebrow">About</p>
            <img
              src="/img/jim-kass.webp"
              alt="Jim Kass"
              width="640"
              height="640"
              loading="lazy"
              class="h-40 w-40 rounded-lg object-cover sm:h-48 sm:w-48" />
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
const services = [
  {
    name: "Product strategy",
    text: "A clear vision and positioning, and a roadmap tied to the metrics that matter for your business.",
  },
  {
    name: "Architecture",
    text: "An honest review of what you have, then a foundation built to scale, whether that means hardening the prototype or rebuilding the core.",
  },
  {
    name: "Security and privacy",
    text: "Authentication, data handling and access control, reviewed and fixed before real users arrive.",
  },
  {
    name: "Observability and analytics",
    text: "Logging, monitoring, product analytics and KPI dashboards, so you can see what's happening and decide on evidence.",
  },
  {
    name: "Brand",
    text: "A name if you need one, a visual identity, and a brand book the product can grow into.",
  },
  {
    name: "Go-to-market",
    text: "Pricing, positioning, a launch plan and the first channels for reaching customers.",
  },
]

const models = [
  {
    name: "Revenue participation",
    text: "Strategy, build and launch support, repaid from a share of sales. Once our fees are covered, the share drops to a small royalty. You keep full ownership.",
  },
  {
    name: "Training",
    text: "One-to-one coaching for founders who want to run the product themselves, from strategy and architecture to AI-native development and launch.",
  },
  {
    name: "Fixed-scope project",
    text: "A defined piece of work under a statement of work, such as an architecture review, a brand book or a go-to-market plan, delivered remotely for an agreed fee.",
  },
]

const products = [
  {
    name: "kidscancode",
    status: "Live · beta",
    live: true,
    summary: "A computer science course for children aged 8 to 10 that teaches how computers work, with real Python along the way.",
    facts: [
      "144 lessons covering binary, memory, algorithms, the internet and AI",
      "Built for privacy: children sign in with a first name only, with no email, chat or ads",
      "Free during beta",
    ],
    url: "https://kidscancode.net",
    image: "/img/products/kidscancode.webp",
  },
  {
    name: "Bloginator",
    status: "Live",
    live: true,
    summary: "An AI writing companion that helps people sharpen their own ideas and draft them in their own voice.",
    facts: [
      "Guided idea development, drafting and revision",
      "Publishes directly to WordPress.com and Ghost",
      "Free plan available",
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
      "An iPhone app for job seekers. It saves postings, fills in applications and reads the user's inbox, read-only, to keep every application's status current.",
    image: "/img/products/obosuru.webp",
    imageAlt: "The Obosuru coming-soon page",
  },
  {
    name: "R U Interested",
    status: "Private beta",
    summary: "A discovery platform for finding what matters to you, your friends and your community.",
    image: "/img/products/ruinterested.webp",
    imageAlt: "The R U Interested home page",
    url: "https://ruinterested.com",
  },
  {
    name: "Hollywood Studio Simulator",
    status: "Working title · desktop game",
    summary: "A film studio management game for desktop. Players develop, cast, shoot and release films and compete for the weekend box office.",
    image: "/img/products/studio-game.webp",
    imageAlt: "The game's main menu, with five generated film posters",
  },
]
</script>
