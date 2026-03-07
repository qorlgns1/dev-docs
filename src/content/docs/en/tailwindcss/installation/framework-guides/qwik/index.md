---
title: "Install Tailwind CSS with Qwik - Tailwind CSS"
description: "Start by creating a new Qwik project if you don't have one set up already. The most common approach is to use Create Qwik."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/qwik

# Install Tailwind CSS with Qwik - Tailwind CSS

01

#### Create your project

Start by creating a new Qwik project if you don't have one set up already. The most common approach is to use [Create Qwik](https://qwik.dev/docs/getting-started/#create-an-app-using-the-cli).

Terminal

```
    npm create qwik@latest empty my-projectcd my-project
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

Add the `@tailwindcss/vite` plugin to your Vite configuration.

vite.config.ts

```
    import { defineConfig } from 'vite'import { qwikVite } from "@builder.io/qwik/optimizer";import { qwikCity } from "@builder.io/qwik-city/vite";// …import tailwindcss from '@tailwindcss/vite'export default defineConfig(({ command, mode }): UserConfig => {  return {    plugins: [      tailwindcss(),      qwikCity(),      qwikVite(),      tsconfigPaths(),    ],    // …  }})
```

04

#### Import Tailwind CSS

Add an `@import` to `./src/global.css` that imports Tailwind CSS.

global.css

```
    @import "tailwindcss";
```

05

#### Start your build process

Run your build process with `npm run dev`.

Terminal

```
    npm run dev
```

06

#### Start using Tailwind in your project

Start using Tailwind’s utility classes to style your content.

index.tsx

```
    import { component$ } from '@builder.io/qwik'export default component$(() => {  return (    <h1 class="text-3xl font-bold underline">      Hello World!    </h1>  )})
```
