---
title: 'No Head Import in Document'
description: '> Prevent usage of  in .'
---

# No Head Import in Document | Next.js

Source URL: https://nextjs.org/docs/messages/no-head-import-in-document

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Head Import in Document

# No Head Import in Document

> Prevent usage of `next/head` in `pages/_document.js`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-head-import-in-document#why-this-error-occurred)

`next/head` was imported in `pages/_document.js`. This can cause unexpected issues in your application.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-head-import-in-document#possible-ways-to-fix-it)

Only import and use `next/document` within `pages/_document.js` to override the default `Document` component. If you are importing `next/head` to use the `Head` component, import it from `next/document` instead in order to modify `<head>` code across all pages:

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
            <Head></Head>
          </Html>
        )
      }
    }
     
    export default MyDocument
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-head-import-in-document#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)



Was this helpful?

supported.

Send
