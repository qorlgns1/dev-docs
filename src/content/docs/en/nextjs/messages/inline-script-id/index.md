---
title: 'Inline script id'
description: '> Enforce  attribute on  components with inline content.'
---

# Inline script id | Next.js

Source URL: https://nextjs.org/docs/messages/inline-script-id

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Inline script id

# Inline script id

> Enforce `id` attribute on `next/script` components with inline content.

## Why This Error Occurred[](https://nextjs.org/docs/messages/inline-script-id#why-this-error-occurred)

`next/script` components with inline content require an `id` attribute to be defined to track and optimize the script.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/inline-script-id#possible-ways-to-fix-it)

Add an `id` attribute to the `next/script` component.

pages/_app.js
[code]
    import Script from 'next/script'
     
    export default function App({ Component, pageProps }) {
      return (
        <>
          <Script id="my-script">{`console.log('Hello world!');`}</Script>
          <Component {...pageProps} />
        </>
      )
    }
[/code]

## Useful links[](https://nextjs.org/docs/messages/inline-script-id#useful-links)

  * [Docs for Next.js Script component](https://nextjs.org/docs/pages/guides/scripts)



Was this helpful?

supported.

Send
