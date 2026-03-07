---
title: "Install Tailwind CSS with Astro - Tailwind CSS"
description: "Start by creating a new Astro project if you don't have one set up already. The most common approach is to use create astro."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/astro

# Install Tailwind CSS with Astro - Tailwind CSS

01

#### Create your project

Start by creating a new Astro project if you don't have one set up already. The most common approach is to use [create astro](https://docs.astro.build/en/install-and-setup/#install-from-the-cli-wizard).

Terminal

```
    npm create astro@latest my-projectcd my-project
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

Add the `@tailwindcss/vite` plugin to your Vite plugins in your Astro config file.

astro.config.mjs

```
    // @ts-checkimport { defineConfig } from "astro/config";import tailwindcss from "@tailwindcss/vite";// https://astro.build/configexport default defineConfig({  vite: {    plugins: [tailwindcss()],  },});
```

04

#### Import Tailwind CSS

Create a `./src/styles/global.css` file and add an `@import` for Tailwind CSS.

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

Start using Tailwind's utility classes to style your content while making sure to import the newly created CSS file.

index.astro

```
    ---import "../styles/global.css";---<h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
