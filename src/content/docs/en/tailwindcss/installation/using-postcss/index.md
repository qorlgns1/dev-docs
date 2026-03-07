---
title: "Installing Tailwind CSS with PostCSS - Tailwind CSS"
description: "Installing Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with frameworks like Next.js and Angular."
---

Source URL: https://tailwindcss.com/docs/installation/using-postcss

# Installing Tailwind CSS with PostCSS - Tailwind CSS

## Installation

- ## [Using Vite](https://tailwindcss.com/docs/installation/using-vite)
- ## [Using PostCSS](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [Framework Guides](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Installing Tailwind CSS as a PostCSS plugin

Installing Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with frameworks like Next.js and Angular.

01

#### Install Tailwind CSS

Install `tailwindcss`, `@tailwindcss/postcss`, and `postcss` via npm.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss postcss
```

02

#### Add Tailwind to your PostCSS configuration

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file, or wherever PostCSS is configured in your project.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  }}
```

03

#### Import Tailwind CSS

Add an `@import` to your CSS file that imports Tailwind CSS.

CSS

```
    @import "tailwindcss";
```

04

#### Start your build process

Run your build process with `npm run dev` or whatever command is configured in your `package.json` file.

Terminal

```
    npm run dev
```

05

#### Start using Tailwind in your HTML

Make sure your compiled CSS is included in the `<head>` _(your framework might handle this for you)_ , then start using Tailwind’s utility classes to style your content.

HTML

```
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/dist/styles.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

**Are you stuck?** Setting up Tailwind with PostCSS can be a bit different across different build tools. Check our framework guides to see if we have more specific instructions for your particular setup.

[Explore our framework guides](https://tailwindcss.com/docs/installation/framework-guides)
