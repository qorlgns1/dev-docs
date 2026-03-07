---
title: "Install Tailwind CSS with SolidJS - Tailwind CSS"
description: "Start by creating a new SolidJS project if you don't have one set up already. The most common approach is to use the SolidJS Vite template."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/solidjs

# Install Tailwind CSS with SolidJS - Tailwind CSS

01

#### Create your project

Start by creating a new SolidJS project if you don't have one set up already. The most common approach is to use [the SolidJS Vite template](https://www.solidjs.com/guides/getting-started).

Terminal

```
    npx degit solidjs/templates/js my-projectcd my-project
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
    import { defineConfig } from 'vite';import solidPlugin from 'vite-plugin-solid';import tailwindcss from '@tailwindcss/vite';export default defineConfig({  plugins: [    tailwindcss(),    solidPlugin(),  ],  server: {    port: 3000,  },  build: {    target: 'esnext',  },});
```

04

#### Import Tailwind CSS

Add an `@import` to `./src/index.css` that imports Tailwind CSS.

index.css

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

App.jsx

```
    export default function App() {  return (    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  )}
```
