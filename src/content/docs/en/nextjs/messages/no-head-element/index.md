---
title: 'No Head Element'
description: '> Prevent usage of  element.'
---

# No Head Element | Next.js

Source URL: https://nextjs.org/docs/messages/no-head-element

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Head Element

# No Head Element

> Prevent usage of `<head>` element.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-head-element#why-this-error-occurred)

A `<head>` element was used to include page-level metadata, but this can cause unexpected behavior in a Next.js application. Use Next.js' built-in `next/head` component instead.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-head-element#possible-ways-to-fix-it)

Import and use the `<Head />` component:

pages/index.js
[code]
    import Head from 'next/head'
     
    function Index() {
      return (
        <>
          <Head>
            <title>My page title</title>
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
          </Head>
        </>
      )
    }
     
    export default Index
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-head-element#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)



Was this helpful?

supported.

Send
