---
title: 'Guides: Tailwind CSS'
description: 'Last updated February 20, 2026'
---

# Guides: Tailwind CSS | Next.js

Source URL: https://nextjs.org/docs/pages/guides/tailwind-v3-css

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Tailwind CSS

Copy page

# Tailwind CSS

Last updated February 20, 2026

This guide will walk you through how to install [Tailwind CSS v3](https://v3.tailwindcss.com/) in your Next.js application.

> **Good to know:** For the latest Tailwind 4 setup, see the [Tailwind CSS setup instructions](https://nextjs.org/docs/app/getting-started/css#tailwind-css).

## Installing Tailwind v3[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#installing-tailwind-v3)

Install Tailwind CSS and its peer dependencies, then run the `init` command to generate both `tailwind.config.js` and `postcss.config.js` files:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D tailwindcss@^3 postcss autoprefixer
    npx tailwindcss init -p
[/code]

## Configuring Tailwind v3[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#configuring-tailwind-v3)

Configure your template paths in your `tailwind.config.js` file:

tailwind.config.js
[code]
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
[/code]

Add the Tailwind directives to your global CSS file:

styles/globals.css
[code]
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
[/code]

Import the CSS file in your `pages/_app.js` file:

pages/_app.js
[code]
    import '@/styles/globals.css'
     
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

## Using classes[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#using-classes)

After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.

pages/index.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
    }
[/code]

## Usage with Turbopack[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#usage-with-turbopack)

As of Next.js 13.1, Tailwind CSS and PostCSS are supported with [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css).

Was this helpful?

supported.

Send
