---
title: 'next.config.js: basePath'
description: 'Last updated February 20, 2026'
---

# next.config.js: basePath | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)basePath

Copy page

# basePath

Last updated February 20, 2026

To deploy a Next.js application under a sub-path of a domain you can use the `basePath` config option.

`basePath` allows you to set a path prefix for the application. For example, to use `/docs` instead of `''` (an empty string, the default), open `next.config.js` and add the `basePath` config:

next.config.js
[code]
    module.exports = {
      basePath: '/docs',
    }
[/code]

> **Good to know** : This value must be set at build time and cannot be changed without re-building as the value is inlined in the client-side bundles.

### Links[](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath#links)

When linking to other pages using `next/link` and `next/router` the `basePath` will be automatically applied.

For example, using `/about` will automatically become `/docs/about` when `basePath` is set to `/docs`.
[code] 
    export default function HomePage() {
      return (
        <>
          <Link href="/about">About Page</Link>
        </>
      )
    }
[/code]

Output html:
[code] 
    <a href="/docs/about">About Page</a>
[/code]

This makes sure that you don't have to change all links in your application when changing the `basePath` value.

### Images[](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath#images)

When using the [`next/image`](https://nextjs.org/docs/app/api-reference/components/image) component, you will need to add the `basePath` in front of `src`.

For example, using `/docs/me.png` will properly serve your image when `basePath` is set to `/docs`.
[code] 
    import Image from 'next/image'
     
    function Home() {
      return (
        <>
          <h1>My Homepage</h1>
          <Image
            src="/docs/me.png"
            alt="Picture of the author"
            width={500}
            height={500}
          />
          <p>Welcome to my homepage!</p>
        </>
      )
    }
     
    export default Home
[/code]

Was this helpful?

supported.

Send
