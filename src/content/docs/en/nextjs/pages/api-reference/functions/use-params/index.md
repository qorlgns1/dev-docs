---
title: 'Functions: useParams'
description: 'Last updated February 20, 2026'
---

# Functions: useParams | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/use-params

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)useParams

Copy page

# useParams

Last updated February 20, 2026

`useParams` is a hook that lets you read a route's [dynamic params](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) filled in by the current URL.

pages/shop/[slug].tsx

JavaScriptTypeScript
[code]
    import { useParams } from 'next/navigation'
     
    export default function ShopPage() {
      const params = useParams<{ slug: string }>()
     
      if (!params) {
        // Render fallback UI while params are not yet available
        return null
      }
     
      // Route -> /shop/[slug]
      // URL -> /shop/shoes
      // `params` -> { slug: 'shoes' }
      return <>Shop: {params.slug}</>
    }
[/code]

## Parameters[](https://nextjs.org/docs/pages/api-reference/functions/use-params#parameters)
[code] 
    const params = useParams()
[/code]

`useParams` does not take any parameters.

## Returns[](https://nextjs.org/docs/pages/api-reference/functions/use-params#returns)

`useParams` returns an object containing the current route's filled in [dynamic parameters](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes), or `null` during [pre-rendering](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior-during-pre-rendering).

  * Each property in the object is an active dynamic segment.
  * The property name is the segment's name, and the property value is what the segment is filled in with.
  * The property value will either be a `string` or array of `string`s depending on the [type of dynamic segment](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes).
  * If the route contains no dynamic parameters, `useParams` returns an empty object.



For example:

Route| URL| `useParams()`  
---|---|---  
`pages/shop/page.js`| `/shop`| `{}`  
`pages/shop/[slug].js`| `/shop/1`| `{ slug: '1' }`  
`pages/shop/[tag]/[item].js`| `/shop/1/2`| `{ tag: '1', item: '2' }`  
`pages/shop/[...slug].js`| `/shop/1/2`| `{ slug: ['1', '2'] }`  
  
> **Good to know** : `useParams` is a [React Hook](https://react.dev/learn#using-hooks) and cannot be used with classes.

## Behavior[](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior)

### Behavior during pre-rendering[](https://nextjs.org/docs/pages/api-reference/functions/use-params#behavior-during-pre-rendering)

For pages that are [statically optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization), `useParams` will return `null` on the initial render. After hydration, the value will be updated to the actual params once the router is ready.

This is because params cannot be known during static generation for dynamic routes.

pages/shop/[slug].tsx

JavaScriptTypeScript
[code]
    import { useParams } from 'next/navigation'
     
    export default function ShopPage() {
      const params = useParams<{ slug: string }>()
     
      if (!params) {
        // Return a fallback UI while params are loading
        // This prevents hydration mismatches
        return <ShopPageSkeleton />
      }
     
      return <>Shop: {params.slug}</>
    }
[/code]

### Using with `getServerSideProps`[](https://nextjs.org/docs/pages/api-reference/functions/use-params#using-with-getserversideprops)

When using [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), the page is server-rendered on each request and `useParams` will return the actual params immediately:

pages/shop/[slug].tsx

JavaScriptTypeScript
[code]
    import { useParams } from 'next/navigation'
     
    export default function ShopPage() {
      const params = useParams<{ slug: string }>()
     
      // With getServerSideProps, this fallback is never rendered because
      // params is always available on the server. However, keeping
      // the fallback allows this component to be reused on other pages
      // that may not use getServerSideProps.
      if (!params) {
        return null
      }
     
      return <>Shop: {params.slug}</>
    }
     
    export async function getServerSideProps() {
      return { props: {} }
    }
[/code]

### Comparison with `router.query`[](https://nextjs.org/docs/pages/api-reference/functions/use-params#comparison-with-routerquery)

`useParams` only returns the dynamic route parameters, whereas [`router.query`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) from `useRouter` includes both dynamic parameters and query string parameters.

pages/shop/[slug].tsx

JavaScriptTypeScript
[code]
    import { useRouter } from 'next/router'
    import { useParams } from 'next/navigation'
     
    export default function ShopPage() {
      const router = useRouter()
      const params = useParams()
     
      // URL -> /shop/shoes?color=red
     
      // router.query -> { slug: 'shoes', color: 'red' }
      // params -> { slug: 'shoes' }
     
      // ...
    }
[/code]

## Examples[](https://nextjs.org/docs/pages/api-reference/functions/use-params#examples)

### Sharing components with App Router[](https://nextjs.org/docs/pages/api-reference/functions/use-params#sharing-components-with-app-router)

`useParams` from `next/navigation` works in both the Pages Router and App Router. This allows you to create shared components that work in either context:

components/breadcrumb.tsx

JavaScriptTypeScript
[code]
    import { useParams } from 'next/navigation'
     
    // This component works in both pages/ and app/
    export function Breadcrumb() {
      const params = useParams<{ slug: string }>()
     
      if (!params) {
        // Fallback for Pages Router during pre-rendering
        return <nav>Home / ...</nav>
      }
     
      return <nav>Home / {params.slug}</nav>
    }
[/code]

> **Good to know** : When using this component in the App Router, `useParams` never returns `null`, so the fallback branch will not be rendered.

## Version History[](https://nextjs.org/docs/pages/api-reference/functions/use-params#version-history)

Version| Changes  
---|---  
`v13.3.0`| `useParams` introduced.  
  
Was this helpful?

supported.

Send
