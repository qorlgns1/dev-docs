---
title: 'Getting Started: Fonts'
description: 'Last updated February 20, 2026'
---

# Getting Started: Fonts | Next.js

Source URL: https://nextjs.org/docs/pages/getting-started/fonts

[Pages Router](https://nextjs.org/docs/pages)[Getting Started](https://nextjs.org/docs/pages/getting-started)Fonts

Copy page

# How to use fonts

Last updated February 20, 2026

The [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.

To start using `next/font`, import it from [`next/font/local`](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts) or [`next/font/google`](https://nextjs.org/docs/pages/getting-started/fonts#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example, you can apply fonts globally in your [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) (`pages/_app`):

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={geist.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

If you want to apply the font to the `<html>` element, you can use a [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document) (`pages/_document`):

pages/_document.tsx

JavaScriptTypeScript
[code]
    import { Html, Head, Main, NextScript } from 'next/document'
    import { Geist } from 'next/font/google'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function Document() {
      return (
        <Html lang="en" className={geist.className}>
          <Head />
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
[/code]

## Google fonts[](https://nextjs.org/docs/pages/getting-started/fonts#google-fonts)

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Geist } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const geist = Geist({
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={geist.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

pages/_app.tsx

JavaScriptTypeScript
[code]
    import { Roboto } from 'next/font/google'
    import type { AppProps } from 'next/app'
     
    const roboto = Roboto({
      weight: '400',
      subsets: ['latin'],
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={roboto.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

## Local fonts[](https://nextjs.org/docs/pages/getting-started/fonts#local-fonts)

To use a local font, import your font from `next/font/local` and specify the [`src`](https://nextjs.org/docs/pages/api-reference/components/font#src) of your local font file. Fonts can be stored in the [`public`](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) folder or inside the `pages` folder. For example:

pages/_app.tsx

JavaScriptTypeScript
[code]
    import localFont from 'next/font/local'
    import type { AppProps } from 'next/app'
     
    const myFont = localFont({
      src: './my-font.woff2',
    })
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return (
        <main className={myFont.className}>
          <Component {...pageProps} />
        </main>
      )
    }
[/code]

If you want to use multiple files for a single font family, `src` can be an array:
[code] 
    const roboto = localFont({
      src: [
        {
          path: './Roboto-Regular.woff2',
          weight: '400',
          style: 'normal',
        },
        {
          path: './Roboto-Italic.woff2',
          weight: '400',
          style: 'italic',
        },
        {
          path: './Roboto-Bold.woff2',
          weight: '700',
          style: 'normal',
        },
        {
          path: './Roboto-BoldItalic.woff2',
          weight: '700',
          style: 'italic',
        },
      ],
    })
[/code]

## API Reference

See the API Reference for the full feature set of Next.js Font

### [FontAPI Reference for the Font Module](https://nextjs.org/docs/pages/api-reference/components/font)

Was this helpful?

supported.

Send
