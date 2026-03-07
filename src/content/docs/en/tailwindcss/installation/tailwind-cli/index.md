---
title: "Tailwind CLI - Tailwind CSS"
description: "The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool. The CLI is also available as a standa..."
---

Source URL: https://tailwindcss.com/docs/installation/tailwind-cli

# Tailwind CLI - Tailwind CSS

## Installation

- ## [Using Vite](https://tailwindcss.com/docs/installation/using-vite)
- ## [Using PostCSS](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [Framework Guides](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Installing Tailwind CLI

The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool. The CLI is also available as a [standalone executable](https://github.com/tailwindlabs/tailwindcss/releases/latest) if you want to use it without installing Node.js.

01

#### Install Tailwind CSS

Install `tailwindcss` and `@tailwindcss/cli` via npm.

Terminal

```
    npm install tailwindcss @tailwindcss/cli
```

02

#### Import Tailwind in your CSS

Add the `@import "tailwindcss";` import to your main CSS file.

src/input.css

```
    @import "tailwindcss";
```

03

#### Start the Tailwind CLI build process

Run the CLI tool to scan your source files for classes and build your CSS.

Terminal

```
    npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

04

#### Start using Tailwind in your HTML

Add your compiled CSS file to the `<head>` and start using Tailwind’s utility classes to style your content.

src/index.html

```
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="./output.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```
