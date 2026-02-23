---
title: 'No Script Component in Head'
description: '> Prevent usage of  in  component.'
---

# No Script Component in Head | Next.js

Source URL: https://nextjs.org/docs/messages/no-script-component-in-head

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Script Component in Head

# No Script Component in Head

> Prevent usage of `next/script` in `next/head` component.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-script-component-in-head#why-this-error-occurred)

The `next/script` component should not be used in a `next/head` component.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-script-component-in-head#possible-ways-to-fix-it)

Move the `<Script />` component outside of `<Head>` instead.

**Before**

pages/index.js
[code]
    import Script from 'next/script'
    import Head from 'next/head'
     
    export default function Index() {
      return (
        <Head>
          <title>Next.js</title>
          <Script src="/my-script.js" />
        </Head>
      )
    }
[/code]

**After**

pages/index.js
[code]
    import Script from 'next/script'
    import Head from 'next/head'
     
    export default function Index() {
      return (
        <>
          <Head>
            <title>Next.js</title>
          </Head>
          <Script src="/my-script.js" />
        </>
      )
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-script-component-in-head#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)
  * [next/script](https://nextjs.org/docs/pages/guides/scripts)



Was this helpful?

supported.

Send
