---
title: 'Using Google Analytics with Next.js (through @next/third-parties/google)'
description: '> Prefer  when using the inline script for Google Analytics and Tag Manager.'
---

# Using Google Analytics with Next.js (through `@next/third-parties/google`) | Next.js

Source URL: https://nextjs.org/docs/messages/next-script-for-ga

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Using Google Analytics with Next.js (through `@next/third-parties/google`)

# Using Google Analytics with Next.js (through `@next/third-parties/google`)

> Prefer `@next/third-parties/google` when using the inline script for Google Analytics and Tag Manager.

## Why This Error Occurred[](https://nextjs.org/docs/messages/next-script-for-ga#why-this-error-occurred)

An inline script was used for Google Analytics which might impact your webpage's performance. Instead, we recommend using `next/script` through the `@next/third-parties` library.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/next-script-for-ga#possible-ways-to-fix-it)

### Use `@next/third-parties` to add Google Analytics[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-analytics)

**`@next/third-parties`** is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application. It is available with Next.js 14 (install `next@latest`).

The `GoogleAnalytics` component can be used to include [Google Analytics 4](https://developers.google.com/analytics/devguides/collection/ga4) to your page via the Google tag (`gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.

> **Recommendation** : If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the [documentation](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm) to learn more about the differences between Tag Manager and `gtag.js`.

To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { GoogleAnalytics } from '@next/third-parties/google'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
          <GoogleAnalytics gaId="G-XYZ" />
        </html>
      )
    }
[/code]

To load Google Analytics for a single route, include the component in your page file:

app/page.js
[code]
    import { GoogleAnalytics } from '@next/third-parties/google'
     
    export default function Page() {
      return <GoogleAnalytics gaId="G-XYZ" />
    }
[/code]

### Use `@next/third-parties` to add Google Tag Manager[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-tag-manager)

The `GoogleTagManager` component can be used to add [Google Tag Manager](https://developers.google.com/tag-manager/quickstart) to your page.

app/layout.tsx

JavaScriptTypeScript
[code]
    import { GoogleTagManager } from '@next/third-parties/google'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <GoogleTagManager gtmId="GTM-XYZ" />
          <body>{children}</body>
        </html>
      )
    }
[/code]

To load Google Tag Manager for a single route, include the component in your page file:

app/page.js
[code]
    import { GoogleTagManager } from '@next/third-parties/google'
     
    export default function Page() {
      return <GoogleTagManager gtmId="GTM-XYZ" />
    }
[/code]

## Good to know[](https://nextjs.org/docs/messages/next-script-for-ga#good-to-know)

  * If you are using the Pages Router, please refer to the [`pages/` documentation](https://nextjs.org/docs/pages/guides/third-party-libraries).
  * `@next/third-parties` also supports [other third parties](https://nextjs.org/docs/app/guides/third-party-libraries#google-tag-manager).
  * Using `@next/third-parties` is not required. You can also use the `next/script` component directly. Refer to the [`next/script` documentation](https://nextjs.org/docs/app/guides/scripts) to learn more.



## Useful Links[](https://nextjs.org/docs/messages/next-script-for-ga#useful-links)

  * [`@next/third-parties` Documentation](https://nextjs.org/docs/app/guides/third-party-libraries)
  * [`next/script` Documentation](https://nextjs.org/docs/app/guides/scripts)



Was this helpful?

supported.

Send
