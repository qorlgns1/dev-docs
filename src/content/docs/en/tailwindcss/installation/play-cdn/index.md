---
title: "Play CDN - Tailwind CSS"
description: "Use the Play CDN to try Tailwind right in the browser without any build step. The Play CDN is designed for development purposes only, and is not inten..."
---

Source URL: https://tailwindcss.com/docs/installation/play-cdn

# Play CDN - Tailwind CSS

## Installation

- ## [Using Vite](https://tailwindcss.com/docs/installation/using-vite)
- ## [Using PostCSS](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [Framework Guides](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Using Play CDN

Use the Play CDN to try Tailwind right in the browser without any build step. The Play CDN is designed for development purposes only, and is not intended for production.

01

#### Add the Play CDN script to your HTML

Add the Play CDN script tag to the `<head>` of your HTML file, and start using Tailwind’s utility classes to style your content.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```

02

#### Try adding some custom CSS

Use `type="text/tailwindcss"` to add custom CSS that supports all of Tailwind's CSS features.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>    <style type="text/tailwindcss">      @theme {        --color-clifford: #da373d;      }    </style>  </head>  <body>    <h1 class="text-3xl font-bold underline text-clifford">      Hello world!    </h1>  </body></html>
```
