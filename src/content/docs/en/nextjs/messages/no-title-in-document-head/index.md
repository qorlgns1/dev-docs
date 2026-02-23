---
title: 'No Title in Document Head'
description: '> Prevent usage of  with  component from .'
---

# No Title in Document Head | Next.js

Source URL: https://nextjs.org/docs/messages/no-title-in-document-head

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Title in Document Head

# No Title in Document Head

> Prevent usage of `<title>` with `Head` component from `next/document`.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-title-in-document-head#why-this-error-occurred)

A `<title>` element was defined within the `Head` component imported from `next/document`, which should only be used for any `<head>` code that is common for all pages. Title tags should be defined at the page-level using `next/head` instead.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-title-in-document-head#possible-ways-to-fix-it)

Within a page or component, import and use `next/head` to define a page title:

pages/index.js
[code]
    import Head from 'next/head'
     
    export function Home() {
      return (
        <div>
          <Head>
            <title>My page title</title>
          </Head>
        </div>
      )
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-title-in-document-head#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)
  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)



Was this helpful?

supported.

Send
