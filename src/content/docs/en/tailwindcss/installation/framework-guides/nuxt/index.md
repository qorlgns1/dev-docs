---
title: "Install Tailwind CSS with Nuxt - Tailwind CSS"
description: "Start by creating a new Nuxt project if you don’t have one set up already. The most common approach is to use Create Nuxt."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/nuxt

# Install Tailwind CSS with Nuxt - Tailwind CSS

01

#### Create your project

Start by creating a new Nuxt project if you don’t have one set up already. The most common approach is to use [Create Nuxt](https://nuxt.com/docs/4.x/getting-started/installation#new-project).

Terminal

```
    npm create nuxt my-projectcd my-project
```

02

#### Install Tailwind CSS

Install `@tailwindcss/vite` and its peer dependencies via npm.

Terminal

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Configure Vite Plugin

Add the `@tailwindcss/vite` plugin to your Nuxt configuration as a Vite plugin.

nuxt.config.ts

```
    import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({  compatibilityDate: "2025-07-15",  devtools: { enabled: true },  vite: {    plugins: [      tailwindcss(),    ],  },});
```

04

#### Import Tailwind CSS

Create an `./app/assets/css/main.css` file and add an `@import` that imports Tailwind CSS.

main.css

```
    @import "tailwindcss";
```

05

#### Add the CSS file globally

Add your newly-created `./app/assets/css/main.css` to the `css` array in your `nuxt.config.ts` file.

nuxt.config.ts

```
    import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({  compatibilityDate: "2025-07-15",  devtools: { enabled: true },  css: ['./app/assets/css/main.css'],  vite: {    plugins: [      tailwindcss(),    ],  },});
```

06

#### Start your build process

Run your build process with `npm run dev`.

Terminal

```
    npm run dev
```

07

#### Start using Tailwind in your project

Start using Tailwind’s utility classes to style your content.

app.vue

```
    <template>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></template>
```
