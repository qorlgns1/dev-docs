---
title: 'No Before Interactive Script Outside Document'
description: "> Prevent usage of 's  strategy outside of  or ."
---

# No Before Interactive Script Outside Document | Next.js

Source URL: https://nextjs.org/docs/messages/no-before-interactive-script-outside-document

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Before Interactive Script Outside Document

# No Before Interactive Script Outside Document

> Prevent usage of `next/script`'s `beforeInteractive` strategy outside of `app/layout.jsx` or `pages/_document.js`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#why-this-error-occurred)

You cannot use the `next/script` component with the `beforeInteractive` strategy outside `app/layout.jsx` or `pages/_document.js`. That's because `beforeInteractive` strategy only works inside **`app/layout.jsx`** or **`pages/_document.js`** and is designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server-side).

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#possible-ways-to-fix-it)

### App Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#app-router)

If you want a global script, and you are using the App Router, move the script inside `app/layout.jsx`.

app/layout.jsx
[code]
    import Script from 'next/script'
     
    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>{children}</body>
          <Script
            src="https://example.com/script.js"
            strategy="beforeInteractive"
          />
        </html>
      )
    }
[/code]

### Pages Router[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#pages-router)

If you want a global script, and you are using the Pages Router, move the script inside `pages/_document.js`.

pages/_document.js
[code]
    import { Html, Head, Main, NextScript } from 'next/document'
    import Script from 'next/script'
     
    export default function Document() {
      return (
        <Html>
          <Head />
          <body>
            <Main />
            <NextScript />
            <Script
              src="https://example.com/script.js"
              strategy="beforeInteractive"
            ></Script>
          </body>
        </Html>
      )
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document#useful-links)

  * [App Router Script Optimization](https://nextjs.org/docs/app/guides/scripts)
  * [Pages Router Script Optimization](https://nextjs.org/docs/pages/guides/scripts)



Was this helpful?

supported.

Send
