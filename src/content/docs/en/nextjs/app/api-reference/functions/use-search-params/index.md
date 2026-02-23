---
title: 'Functions: useSearchParams'
description: "is a Client Component hook that lets you read the current URL's query string."
---

# Functions: useSearchParams | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/use-search-params

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)useSearchParams

Copy page

# useSearchParams

Last updated February 20, 2026

`useSearchParams` is a **Client Component** hook that lets you read the current URL's **query string**.

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface.

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function SearchBar() {
      const searchParams = useSearchParams()
     
      const search = searchParams.get('search')
     
      // URL -> `/dashboard?search=my-project`
      // `search` -> 'my-project'
      return <>Search: {search}</>
    }
[/code]

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#parameters)
[code] 
    const searchParams = useSearchParams()
[/code]

`useSearchParams` does not take any parameters.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#returns)

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface, which includes utility methods for reading the URL's query string:

  * [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): Returns the first value associated with the search parameter. For example:

URL| `searchParams.get("a")`  
---|---  
`/dashboard?a=1`| `'1'`  
`/dashboard?a=`| `''`  
`/dashboard?b=3`| `null`  
`/dashboard?a=1&a=2`| `'1'` _\- use[`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) to get all values_  
  
  * [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): Returns a boolean value indicating if the given parameter exists. For example:

URL| `searchParams.has("a")`  
---|---  
`/dashboard?a=1`| `true`  
`/dashboard?b=3`| `false`  
  
  * Learn more about other **read-only** methods of [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), including the [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), and [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString).




> **Good to know** :
> 
>   * `useSearchParams` is a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) hook and is **not supported** in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) to prevent stale values during [partial rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions).
>   * If you want to fetch data in a Server Component based on search params, it's often a better option to read the [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) of the corresponding Page. You can then pass it down by props to any component (Server or Client) within that Page.
>   * If an application includes the `/pages` directory, `useSearchParams` will return `ReadonlyURLSearchParams | null`. The `null` value is for compatibility during migration since search params cannot be known during pre-rendering of a page that doesn't use `getServerSideProps`
> 


## Behavior[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#behavior)

### Static Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering)

If a route is [statically rendered](https://nextjs.org/docs/app/guides/caching#static-rendering), calling `useSearchParams` will cause the Client Component tree up to the closest [`Suspense` boundary](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples) to be client-side rendered.

This allows a part of the route to be statically rendered while the dynamic part that uses `useSearchParams` is client-side rendered.

We recommend wrapping the Client Component that uses `useSearchParams` in a `<Suspense/>` boundary. This will allow any Client Components above it to be statically rendered and sent as part of initial HTML. [Example](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering).

For example:

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function SearchBar() {
      const searchParams = useSearchParams()
     
      const search = searchParams.get('search')
     
      // This will not be logged on the server when using static rendering
      console.log(search)
     
      return <>Search: {search}</>
    }
[/code]

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import SearchBar from './search-bar'
     
    // This component passed as a fallback to the Suspense boundary
    // will be rendered in place of the search bar in the initial HTML.
    // When the value is available during React hydration the fallback
    // will be replaced with the `<SearchBar>` component.
    function SearchBarFallback() {
      return <>placeholder</>
    }
     
    export default function Page() {
      return (
        <>
          <nav>
            <Suspense fallback={<SearchBarFallback />}>
              <SearchBar />
            </Suspense>
          </nav>
          <h1>Dashboard</h1>
        </>
      )
    }
[/code]

> **Good to know** :
> 
>   * In development, routes are rendered on-demand, so `useSearchParams` doesn't suspend and things may appear to work without `Suspense`.
>   * During production builds, a [static page](https://nextjs.org/docs/app/guides/caching#static-rendering) that calls `useSearchParams` from a Client Component must be wrapped in a `Suspense` boundary, otherwise the build fails with the [Missing Suspense boundary with useSearchParams](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout) error.
>   * If you intend the route to be dynamically rendered, prefer using the [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) function first in a Server Component to wait for an incoming request, this excludes everything below from prerendering. See what makes a route dynamic in the [Dynamic Rendering guide](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
>   * If you're already in a Server Component Page, consider using the [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) and passing the values to Client Components.
>   * You can also pass the Page [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) directly to a Client Component and unwrap it with React's `use()`. Although this will suspend, so the Client Component should be wrapped with a `Suspense` boundary.
> 


### Dynamic Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#dynamic-rendering)

If a route is [dynamically rendered](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), `useSearchParams` will be available on the server during the initial server render of the Client Component.

For example:

app/dashboard/search-bar.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSearchParams } from 'next/navigation'
     
    export default function SearchBar() {
      const searchParams = useSearchParams()
     
      const search = searchParams.get('search')
     
      // This will be logged on the server during the initial render
      // and on the client on subsequent navigations.
      console.log(search)
     
      return <>Search: {search}</>
    }
[/code]

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
    import SearchBar from './search-bar'
     
    export default async function Page() {
      await connection()
      return (
        <>
          <nav>
            <SearchBar />
          </nav>
          <h1>Dashboard</h1>
        </>
      )
    }
[/code]

> **Good to know** :
> 
>   * Previously, setting `export const dynamic = 'force-dynamic'` on the page was used to force dynamic rendering. Prefer using [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) instead, as it semantically ties dynamic rendering to the incoming request.
> 


### Server Components[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#server-components)

#### Pages[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#pages)

To access search params in [Pages](https://nextjs.org/docs/app/api-reference/file-conventions/page) (Server Components), use the [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop.

#### Layouts[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#layouts)

Unlike Pages, [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) (Server Components) **do not** receive the `searchParams` prop. This is because a shared layout is [not re-rendered during navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) which could lead to stale `searchParams` between navigations. View [detailed explanation](https://nextjs.org/docs/app/api-reference/file-conventions/layout#query-params).

Instead, use the Page [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page) prop or the [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) hook in a Client Component, which is re-rendered on the client with the latest `searchParams`.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#examples)

### Updating `searchParams`[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#updating-searchparams)

You can use [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) or [`Link`](https://nextjs.org/docs/app/api-reference/components/link) to set new `searchParams`. After a navigation is performed, the current [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page) will receive an updated [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional).

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function ExampleClientComponent() {
      const router = useRouter()
      const pathname = usePathname()
      const searchParams = useSearchParams()
     
      // Get a new searchParams string by merging the current
      // searchParams with a provided key/value pair
      const createQueryString = useCallback(
        (name: string, value: string) => {
          const params = new URLSearchParams(searchParams.toString())
          params.set(name, value)
     
          return params.toString()
        },
        [searchParams]
      )
     
      return (
        <>
          <p>Sort By</p>
     
          {/* using useRouter */}
          <button
            onClick={() => {
              // <pathname>?sort=asc
              router.push(pathname + '?' + createQueryString('sort', 'asc'))
            }}
          >
            ASC
          </button>
     
          {/* using <Link> */}
          <Link
            href={
              // <pathname>?sort=desc
              pathname + '?' + createQueryString('sort', 'desc')
            }
          >
            DESC
          </Link>
        </>
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#version-history)

Version| Changes  
---|---  
`v13.0.0`| `useSearchParams` introduced.  
  
Was this helpful?

supported.

Send
