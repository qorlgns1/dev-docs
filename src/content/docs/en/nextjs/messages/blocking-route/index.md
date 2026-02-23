---
title: 'Uncached data was accessed outside of <Suspense>'
description: 'When the  feature is enabled, Next.js expects a parent  boundary around any component that awaits data that should be accessed on every user request....'
---

# Uncached data was accessed outside of `<Suspense>` | Next.js

Source URL: https://nextjs.org/docs/messages/blocking-route

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Uncached data was accessed outside of `<Suspense>`

# Uncached data was accessed outside of `<Suspense>`

## Why This Error Occurred[](https://nextjs.org/docs/messages/blocking-route#why-this-error-occurred)

When the `cacheComponents` feature is enabled, Next.js expects a parent `Suspense` boundary around any component that awaits data that should be accessed on every user request. The purpose of this requirement is so that Next.js can provide a useful fallback while this data is accessed and rendered.

While some data is inherently only available when a user request is being handled, such as request headers, Next.js assumes that by default any asynchronous data is expected to be accessed each time a user request is being handled unless you specifically cache it using `"use cache"`.

The proper fix for this specific error depends on what data you are accessing and how you want your Next.js app to behave.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/blocking-route#possible-ways-to-fix-it)

### Accessing Data[](https://nextjs.org/docs/messages/blocking-route#accessing-data)

When you access data using `fetch`, a database client, or any other module which does asynchronous IO, Next.js interprets your intent as expecting the data to load on every user request.

If you are expecting this data to be used while fully or partially prerendering a page you must cache is using `"use cache"`.

Before:

app/page.js
[code]
    async function getRecentArticles() {
      return db.query(...)
    }
     
    export default async function Page() {
      const articles = await getRecentArticles(token);
      return <ArticleList articles={articles}>
    }
[/code]

After:

app/page.js
[code]
    import { cacheTag, cacheLife } from 'next/cache'
     
    async function getRecentArticles() {
      "use cache"
      // This cache can be revalidated by webhook or server action
      // when you call revalidateTag("articles")
      cacheTag("articles")
      // This cache will revalidate after an hour even if no explicit
      // revalidate instruction was received
      cacheLife('hours')
      return db.query(...)
    }
     
    export default async function Page() {
      const articles = await getRecentArticles(token);
      return <ArticleList articles={articles}>
    }
[/code]

If this data should be accessed on every user request you must provide a fallback UI using `Suspense` from React. Where you put this Suspense boundary in your application should be informed by the kind of fallback UI you want to render. It can be immediately above the component accessing this data or even in your Root Layout.

Before:

app/page.js
[code]
    async function getLatestTransactions() {
      return db.query(...)
    }
     
    export default async function Page() {
      const transactions = await getLatestTransactions(token);
      return <TransactionList transactions={transactions}>
    }
[/code]

After:

app/page.js
[code]
    import { Suspense } from 'react'
     
    async function TransactionList() {
      const transactions = await db.query(...)
      return ...
    }
     
    function TransactionSkeleton() {
      return <ul>...</ul>
    }
     
    export default async function Page() {
      return (
        <Suspense fallback={<TransactionSkeleton />}>
          <TransactionList/>
        </Suspense>
      )
    }
[/code]

### Headers[](https://nextjs.org/docs/messages/blocking-route#headers)

If you are accessing request headers using `headers()`, `cookies()`, or `draftMode()`. Consider whether you can move the use of these APIs deeper into your existing component tree.

Before:

app/inbox.js
[code]
    export async function Inbox({ token }) {
      const email = await getEmail(token)
      return (
        <ul>
          {email.map((e) => (
            <EmailRow key={e.id} />
          ))}
        </ul>
      )
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Inbox } from './inbox'
     
    export default async function Page() {
      const token = (await cookies()).get('token')
      return (
        <Suspense fallback="loading your inbox...">
          <Inbox token={token}>
        </Suspense>
      )
    }
[/code]

After:

app/inbox.js
[code]
    import { cookies } from 'next/headers'
     
    export async function Inbox() {
      const token = (await cookies()).get('token')
      const email = await getEmail(token)
      return (
        <ul>
          {email.map((e) => (
            <EmailRow key={e.id} />
          ))}
        </ul>
      )
    }
[/code]

app/page.js
[code]
    import { Inbox } from './inbox'
     
    export default async function Page() {
      return (
        <Suspense fallback="loading your inbox...">
          <Inbox>
        </Suspense>
      )
    }
[/code]

Alternatively you can add a Suspense boundary above the component that is accessing Request headers.

### Params and SearchParams[](https://nextjs.org/docs/messages/blocking-route#params-and-searchparams)

Layout `params`, and Page `params` and `searchParams` props are promises. If you await them in the Layout or Page component you might be accessing these props higher than is actually required. Try passing these props to deeper components as a promise and awaiting them closer to where the actual param or searchParam is required

Before:

app/map.js
[code]
    export async function Map({ lat, lng }) {
      const mapData = await fetch(`https://...?lat=${lat}&lng=${lng}`)
      return drawMap(mapData)
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Map } from './map'
     
    export default async function Page({ searchParams }) {
      const { lat, lng } = await searchParams;
      return (
        <Suspense fallback="loading your inbox...">
          <Map lat={lat} lng={lng}>
        </Suspense>
      )
    }
[/code]

After:

app/map.js
[code]
    export async function Map({ coords }) {
      const { lat, lng } = await coords
      const mapData = await fetch(`https://...?lat=${lat}&lng=${lng}`)
      return drawMap(mapData)
    }
[/code]

app/page.js
[code]
    import { cookies } from 'next/headers'
     
    import { Map } from './map'
     
    export default async function Page({ searchParams }) {
      const coords = searchParams.then(sp => ({ lat: sp.lat, lng: sp.lng }))
      return (
        <Suspense fallback="loading your inbox...">
          <Map coord={coords}>
        </Suspense>
      )
    }
[/code]

Alternatively you can add a Suspense boundary above the component that is accessing `params` or `searchParams` so Next.js understands what UI should be used when while waiting for this request data to be accessed.

#### `generateStaticParams`[](https://nextjs.org/docs/messages/blocking-route#generatestaticparams)

For Layout and Page `params`, you can use [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) to provide sample values for build-time validation, which allows you to await params directly without Suspense.

app/blog/[slug]/page.js
[code]
    export async function generateStaticParams() {
      return [{ slug: 'hello-world' }]
    }
     
    export default async function Page({ params }) {
      const { slug } = await params //  Valid with generateStaticParams
      return <div>Blog post: {slug}</div>
    }
[/code]

Note that validation is path-dependent. Runtime parameters may trigger conditional branches accessing runtime APIs without Suspense, or dynamic content without Suspense or `use cache`, resulting in errors. See [Dynamic Routes with Cache Components](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components).

### Short-lived Caches[](https://nextjs.org/docs/messages/blocking-route#short-lived-caches)

`"use cache"` allows you to describe a [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) that might be too short to be practical to prerender. The utility of doing this is that it can still describe a non-zero caching time for the client router cache to reuse the cache entry in the browser and it can also be useful for protecting upstream APIs while experiencing high request traffic.

If you expected the `"use cache"` entry to be prerenderable try describing a slightly longer `cacheLife()`.

Before:

app/page.js
[code]
    import { cacheLife } from 'next/cache'
     
    async function getDashboard() {
      "use cache"
      // This cache will revalidate after 1 second. It is so short
      // Next.js won't prerender it on the server but the client router
      // can reuse the result for up to 30 seconds unless the user manually refreshes
      cacheLife('seconds')
      return db.query(...)
    }
     
    export default async function Page() {
      const data = await getDashboard(token);
      return <Dashboard data={data}>
    }
[/code]

After:

app/page.js
[code]
    import { cacheLife } from 'next/cache'
     
    async function getDashboard() {
      "use cache"
      // This cache will revalidate after 1 minute. It's long enough that
      // Next.js will still produce a fully or partially prerendered page
      cacheLife('minutes')
      return db.query(...)
    }
     
    export default async function Page() {
      const data = await getDashboard(token);
      return <Dashboard data={data}>
    }
[/code]

Alternatively you can add a Suspense boundary above the component that is accessing this short-lived cached data so Next.js understands what UI should be used while accessing this data on a user request.

## Useful Links[](https://nextjs.org/docs/messages/blocking-route#useful-links)

  * [`Suspense` React API](https://react.dev/reference/react/Suspense)
  * [`headers` function](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`cookies` function](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`draftMode` function](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`connection` function](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [`cacheLife` function](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  * [`cacheTag` function](https://nextjs.org/docs/app/api-reference/functions/cacheTag)



Was this helpful?

supported.

Send
