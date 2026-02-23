---
title: 'Getting Started: CSS'
description: 'Next.js provides several ways to style your application using CSS, including:'
---

# Getting Started: CSS | Next.js

Source URL: https://nextjs.org/docs/pages/getting-started/css

[Pages Router](https://nextjs.org/docs/pages)[Getting Started](https://nextjs.org/docs/pages/getting-started)CSS

Copy page

# How to use CSS in your application

Last updated February 20, 2026

Next.js provides several ways to style your application using CSS, including:

  * [Tailwind CSS](https://nextjs.org/docs/pages/getting-started/css#tailwind-css)
  * [CSS Modules](https://nextjs.org/docs/pages/getting-started/css#css-modules)
  * [Global CSS](https://nextjs.org/docs/pages/getting-started/css#global-css)
  * [External Stylesheets](https://nextjs.org/docs/pages/getting-started/css#external-stylesheets)
  * [Sass](https://nextjs.org/docs/app/guides/sass)
  * [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)



## Tailwind CSS[](https://nextjs.org/docs/pages/getting-started/css#tailwind-css)

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that provides low-level utility classes to build custom designs.

Install Tailwind CSS:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D tailwindcss @tailwindcss/postcss
[/code]

Add the PostCSS plugin to your `postcss.config.mjs` file:

postcss.config.mjs
[code]
    export default {
      plugins: {
        '@tailwindcss/postcss': {},
      },
    }
[/code]

Import Tailwind in your global CSS file:

styles/globals.css
[code]
    @import 'tailwindcss';
[/code]

Import the CSS file in your `pages/_app.js` file:

pages/_app.js
[code]
    import '@/styles/globals.css'
     
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

Now you can start using Tailwind's utility classes in your application:

pages/index.tsx

JavaScriptTypeScript
[code]
    export default function Home() {
      return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
          <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
        </main>
      )
    }
[/code]

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](https://nextjs.org/docs/app/guides/tailwind-v3-css).

## CSS Modules[](https://nextjs.org/docs/pages/getting-started/css#css-modules)

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `pages` directory:

/styles/blog.module.css
[code]
    .blog {
      padding: 24px;
    }
[/code]

pages/blog/index.tsx

JavaScriptTypeScript
[code]
    import styles from './blog.module.css'
     
    export default function Page() {
      return <main className={styles.blog}></main>
    }
[/code]

## Global CSS[](https://nextjs.org/docs/pages/getting-started/css#global-css)

You can use global CSS to apply styles across your application.

Import the stylesheet in the `pages/_app.js` file to apply the styles to **every route** in your application:

pages/_app.js
[code]
    import '@/styles/global.css'
     
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

Due to the global nature of stylesheets, and to avoid conflicts, you should import them inside [`pages/_app.js`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app).

## External stylesheets[](https://nextjs.org/docs/pages/getting-started/css#external-stylesheets)

Next.js allows you to import CSS files from a JavaScript file. This is possible because Next.js extends the concept of [`import`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import) beyond JavaScript.

### Import styles from `node_modules`[](https://nextjs.org/docs/pages/getting-started/css#import-styles-from-node_modules)

Since Next.js **9.5.4** , importing a CSS file from `node_modules` is permitted anywhere in your application.

For global stylesheets, like `bootstrap` or `nprogress`, you should import the file inside `pages/_app.js`. For example:

pages/_app.js
[code]
    import 'bootstrap/dist/css/bootstrap.css'
     
    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

To import CSS required by a third-party component, you can do so in your component. For example:

components/example-dialog.js
[code]
    import { useState } from 'react'
    import { Dialog } from '@reach/dialog'
    import VisuallyHidden from '@reach/visually-hidden'
    import '@reach/dialog/styles.css'
     
    function ExampleDialog(props) {
      const [showDialog, setShowDialog] = useState(false)
      const open = () => setShowDialog(true)
      const close = () => setShowDialog(false)
     
      return (
        <div>
          <button onClick={open}>Open Dialog</button>
          <Dialog isOpen={showDialog} onDismiss={close}>
            <button className="close-button" onClick={close}>
              <VisuallyHidden>Close</VisuallyHidden>
              <span aria-hidden>×</span>
            </button>
            <p>Hello there. I am a dialog</p>
          </Dialog>
        </div>
      )
    }
[/code]

## Ordering and Merging[](https://nextjs.org/docs/pages/getting-started/css#ordering-and-merging)

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.

For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:

page.tsx

JavaScriptTypeScript
[code]
    import { BaseButton } from './base-button'
    import styles from './page.module.css'
     
    export default function Page() {
      return <BaseButton className={styles.primary} />
    }
[/code]

base-button.tsx

JavaScriptTypeScript
[code]
    import styles from './base-button.module.css'
     
    export function BaseButton() {
      return <button className={styles.primary} />
    }
[/code]

### Recommendations[](https://nextjs.org/docs/pages/getting-started/css#recommendations)

To keep CSS ordering predictable:

  * Try to contain CSS imports to a single JavaScript or TypeScript entry file
  * Import global styles and Tailwind stylesheets in the root of your application.
  * **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
  * Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
  * Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
  * Extract shared styles into shared components to avoid duplicate imports.
  * Turn off linters or formatters that auto-sort imports like ESLint’s [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports).
  * You can use the [`cssChunking`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking) option in `next.config.js` to control how CSS is chunked.



## Development vs Production[](https://nextjs.org/docs/pages/getting-started/css#development-vs-production)

  * In development (`next dev`), CSS updates apply instantly with [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh).
  * In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
  * CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
  * CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.



## Next Steps

Learn more about the features mentioned in this page.

### [Tailwind CSSStyle your Next.js Application using Tailwind CSS.](https://nextjs.org/docs/pages/guides/tailwind-v3-css)### [SassLearn how to use Sass in your Next.js application.](https://nextjs.org/docs/pages/guides/sass)### [CSS-in-JSUse CSS-in-JS libraries with Next.js](https://nextjs.org/docs/pages/guides/css-in-js)

Was this helpful?

supported.

Send
