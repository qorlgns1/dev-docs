---
title: 'Architecture: Supported Browsers'
description: 'Last updated February 20, 2026'
---

# Architecture: Supported Browsers | Next.js

Source URL: https://nextjs.org/docs/architecture/supported-browsers

[Next.js Docs](https://nextjs.org/docs)[Architecture](https://nextjs.org/docs/architecture)Supported Browsers

Copy page

# Supported Browsers

Last updated February 20, 2026

Next.js supports **modern browsers** with zero configuration.

  * Chrome 111+
  * Edge 111+
  * Firefox 111+
  * Safari 16.4+



## Browserslist[](https://nextjs.org/docs/architecture/supported-browsers#browserslist)

If you would like to target specific browsers or features, Next.js supports [Browserslist](https://browsersl.ist) configuration in your `package.json` file. Next.js uses the following Browserslist configuration by default:

package.json
[code]
    {
      "browserslist": ["chrome 111", "edge 111", "firefox 111", "safari 16.4"]
    }
[/code]

## Polyfills[](https://nextjs.org/docs/architecture/supported-browsers#polyfills)

We inject [widely used polyfills](https://github.com/vercel/next.js/blob/canary/packages/next-polyfill-nomodule/src/index.js), including:

  * [**fetch()**](https://developer.mozilla.org/docs/Web/API/Fetch_API) — Replacing: `whatwg-fetch` and `unfetch`.
  * [**URL**](https://developer.mozilla.org/docs/Web/API/URL) — Replacing: the [`url` package (Node.js API)](https://nodejs.org/api/url.html).
  * [**Object.assign()**](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) — Replacing: `object-assign`, `object.assign`, and `core-js/object/assign`.



If any of your dependencies include these polyfills, they’ll be eliminated automatically from the production build to avoid duplication.

In addition, to reduce bundle size, Next.js will only load these polyfills for browsers that require them. The majority of the web traffic globally will not download these polyfills.

### Custom Polyfills[](https://nextjs.org/docs/architecture/supported-browsers#custom-polyfills)

If your own code or any external npm dependencies require features not supported by your target browsers (such as IE 11), you need to add polyfills yourself.

#### In App Router[](https://nextjs.org/docs/architecture/supported-browsers#in-app-router)

To include polyfills, you can import them into the [`instrumentation-client.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client).

instrumentation-client.ts
[code]
    import './polyfills'
[/code]

#### In Pages Router[](https://nextjs.org/docs/architecture/supported-browsers#in-pages-router)

In this case, you should add a top-level import for the **specific polyfill** you need in your [Custom `<App>`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) or the individual component.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import './polyfills'
     
    import type { AppProps } from 'next/app'
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
[/code]

#### Conditionally loading polyfills[](https://nextjs.org/docs/architecture/supported-browsers#conditionally-loading-polyfills)

The best approach is to isolate unsupported features to specific UI sections and conditionally load the polyfill if needed.

hooks/analytics.ts

JavaScriptTypeScript
[code]
    import { useCallback } from 'react'
     
    export const useAnalytics = () => {
      const tracker = useCallback(async (data: unknown) => {
        if (!('structuredClone' in globalThis)) {
          import('polyfills/structured-clone').then((mod) => {
            globalThis.structuredClone = mod.default
          })
        }
     
        /* Do some work that uses structured clone */
      }, [])
     
      return tracker
    }
[/code]

## JavaScript Language Features[](https://nextjs.org/docs/architecture/supported-browsers#javascript-language-features)

Next.js allows you to use the latest JavaScript features out of the box. In addition to [ES6 features](https://github.com/lukehoban/es6features), Next.js also supports:

  * [Async/await](https://github.com/tc39/ecmascript-asyncawait) (ES2017)
  * [Object Rest/Spread Properties](https://github.com/tc39/proposal-object-rest-spread) (ES2018)
  * [Dynamic `import()`](https://github.com/tc39/proposal-dynamic-import) (ES2020)
  * [Optional Chaining](https://github.com/tc39/proposal-optional-chaining) (ES2020)
  * [Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing) (ES2020)
  * [Class Fields](https://github.com/tc39/proposal-class-fields) and [Static Properties](https://github.com/tc39/proposal-static-class-features) (ES2022)
  * and more!



### TypeScript Features[](https://nextjs.org/docs/architecture/supported-browsers#typescript-features)

Next.js has built-in TypeScript support. [Learn more here](https://nextjs.org/docs/pages/api-reference/config/typescript).

### Customizing Babel Config (Advanced)[](https://nextjs.org/docs/architecture/supported-browsers#customizing-babel-config-advanced)

You can customize babel configuration. [Learn more here](https://nextjs.org/docs/pages/guides/babel).

Was this helpful?

supported.

Send
