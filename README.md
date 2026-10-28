# alternativereality.com

The website for [Alternative Reality Group](https://alternativereality.com), a software company in Los Angeles that builds and runs its own products.

Built with [Nuxt 3](https://nuxt.com/) and [Tailwind CSS](https://tailwindcss.com/), generated as a static site and hosted on [Netlify](https://www.netlify.com/).

## Running it locally

```sh
bun install        # or npm install
bun run dev        # http://localhost:3000
bun run generate   # static build in dist/
```

## Layout

| Path | What's there |
| --- | --- |
| `pages/index.vue` | The home page: hero, products, working with ARG, about, contact |
| `pages/privacy.vue` | Privacy policy |
| `components/` | Header, footer, product cards and the contact form |
| `public/img/products/` | Product screenshots |
| `public/brand/` | Logo, icon, favicon and share-card files |
| `brand/` | The script that generates the logo files, and the brand guide ([`brand/README.md`](brand/README.md)) |

## Contact form

The form posts to `/post-form.html`, a hidden static copy of the form that Netlify uses to detect it. If you change the form's fields in `components/ContactSection.vue`, change them in `public/post-form.html` to match, or Netlify will drop them.

## Deploying

Netlify publishes `dist/`, the output of `nuxt generate` (see `netlify.toml`). Production deploys from `main`, and other branches get preview deploys when branch deploys are turned on.
