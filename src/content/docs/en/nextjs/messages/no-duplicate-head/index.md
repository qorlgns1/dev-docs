---
title: 'No Duplicate Head'
description: '> Prevent duplicate usage of  in .'
---

# No Duplicate Head | Next.js

Source URL: https://nextjs.org/docs/messages/no-duplicate-head

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Duplicate Head

# No Duplicate Head

> Prevent duplicate usage of `<Head>` in `pages/_document.js`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-duplicate-head#why-this-error-occurred)

More than a single instance of the `<Head />` component was used in a single custom document. This can cause unexpected behavior in your application.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-duplicate-head#possible-ways-to-fix-it)

Only use a single `<Head />` component in your custom document in `pages/_document.js`.

pages/_document.js
[code]
    import Document, { Html, Head, Main, NextScript } from 'next/document'
     
    class MyDocument extends Document {
      static async getInitialProps(ctx) {
        //...
      }
     
      render() {
        return (
          <Html>
            <Head />
            <body>
              <Main />
              <NextScript />
            </body>
          </Html>
        )
      }
    }
     
    export default MyDocument
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-duplicate-head#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)



Was this helpful?

supported.

Send
