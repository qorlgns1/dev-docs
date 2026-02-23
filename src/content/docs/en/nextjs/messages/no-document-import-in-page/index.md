---
title: 'No Document Import in Page'
description: '> Prevent importing  outside of .'
---

# No Document Import in Page | Next.js

Source URL: https://nextjs.org/docs/messages/no-document-import-in-page

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Document Import in Page

# No Document Import in Page

> Prevent importing `next/document` outside of `pages/_document.js`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-document-import-in-page#why-this-error-occurred)

`next/document` was imported in a page outside of `pages/_document.js` (or `pages/_document.tsx` if you are using TypeScript). This can cause unexpected issues in your application.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-document-import-in-page#possible-ways-to-fix-it)

Only import and use `next/document` within `pages/_document.js` (or `pages/_document.tsx`) to override the default `Document` component:

pages/_document.js
[code]
    import Document, { Html, Head, Main, NextScript } from 'next/document'
     
    class MyDocument extends Document {
      //...
    }
     
    export default MyDocument
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-document-import-in-page#useful-links)

  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)



Was this helpful?

supported.

Send
