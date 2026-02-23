---
title: 'Missing Suspense boundary with useSearchParams'
description: 'Reading search parameters through  without a Suspense boundary will opt the entire page into client-side rendering. This could cause your page to be b...'
---

# Missing Suspense boundary with useSearchParams | Next.js

Source URL: https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Missing Suspense boundary with useSearchParams

# Missing Suspense boundary with useSearchParams

## Why This Error Occurred[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#why-this-error-occurred)

Reading search parameters through `useSearchParams()` without a Suspense boundary will opt the entire page into client-side rendering. This could cause your page to be blank until the client-side JavaScript has loaded.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#possible-ways-to-fix-it)

You have a few options depending on your intent:

  * To keep the route statically generated, wrap the smallest subtree that calls `useSearchParams()` in `Suspense`, for example you may move its usage into a child Client Component and render that component wrapped with `Suspense`. This preserves the static shell and avoids a full CSR bailout.
  * To make the route dynamically rendered, use the [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) function in a Server Component (e.g. the Page or a wrapping Layout). This waits for an incoming request and excludes everything below from prerendering.



app/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
     
    export default async function Page() {
      await connection()
      return <div>...</div>
    }
[/code]

  * Before the `connection` API was available setting `export const dynamic = 'force-dynamic'` in a Server Component `page.tsx`, or `layout.tsx`, opted the route into on-demand rendering. Note that setting `dynamic` in a Client Component (`'use client'`) `page.tsx` has no effect.



app/layout.tsx

JavaScriptTypeScript
[code]
    export const dynamic = 'force-dynamic'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return children
    }
[/code]

  * Alternatively, a Server Component Page can pass the `searchParams` value down to Client Components. In a Client Component, you can unwrap it with React's `use()` (ensure a surrounding `Suspense` boundary). See [What to use and when](https://nextjs.org/docs/app/getting-started/layouts-and-pages#what-to-use-and-when).



app/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import ClientSearch from './client-search'
     
    export default function Page({
      searchParams,
    }: {
      searchParams: Promise<{ q?: string }>
    }) {
      return (
        <Suspense fallback={<>...</>}>
          <ClientSearch searchParams={searchParams} />
        </Suspense>
      )
    }
[/code]

app/client-search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { use } from 'react'
     
    export default function ClientSearch({
      searchParams,
    }: {
      searchParams: Promise<{ q?: string }>
    }) {
      const params = use(searchParams)
      return <div>Query: {params.q}</div>
    }
[/code]

  * Consider making the Page a Server Component again and isolating Client-only code (that uses `useSearchParams`) into child Client Components.



app/search.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
    import { Suspense } from 'react'
     
    function Search() {
      const searchParams = useSearchParams()
     
      return <input placeholder="Search..." />
    }
     
    export function Searchbar() {
      return (
        // You could have a loading skeleton as the `fallback` too
        <Suspense>
          <Search />
        </Suspense>
      )
    }
[/code]

## Disabling[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#disabling)

> **Note** : This is only available with Next.js version 14.x. If you're in versions above 14 please fix it with the approach above.

We don't recommend disabling this rule. However, if you need to, you can disable it by setting the `missingSuspenseWithCSRBailout` option to `false` in your `next.config.js`:

next.config.js
[code]
    module.exports = {
      experimental: {
        missingSuspenseWithCSRBailout: false,
      },
    }
[/code]

This configuration option will be removed in a future major version.

## Debugging[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#debugging)

If you're having trouble locating where `useSearchParams()` is being used without a Suspense boundary, you can get more detailed stack traces by running:
[code] 
    next build --debug-prerender
[/code]

This provides unminified stack traces with source maps, making it easier to pinpoint the exact component and route causing the issue.

## Useful Links[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#useful-links)

  * [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
  * [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [Dynamic Rendering guide](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)
  * [Debugging prerender errors](https://nextjs.org/docs/app/api-reference/cli/next#debugging-prerender-errors)



Was this helpful?

supported.

Send
