---
title: 'Getting Started: Route Handlers'
description: 'Last updated February 20, 2026'
---

# Getting Started: Route Handlers | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/route-handlers

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Route Handlers

Copy page

# Route Handlers

Last updated February 20, 2026

## Route Handlers[](https://nextjs.org/docs/app/getting-started/route-handlers#route-handlers)

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

> **Good to know** : Route Handlers are only available inside the `app` directory. They are the equivalent of [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) inside the `pages` directory meaning you **do not** need to use API Routes and Route Handlers together.

### Convention[](https://nextjs.org/docs/app/getting-started/route-handlers#convention)

Route Handlers are defined in a [`route.js|ts` file](https://nextjs.org/docs/app/api-reference/file-conventions/route) inside the `app` directory:

app/api/route.ts

JavaScriptTypeScript
[code]
    export async function GET(request: Request) {}
[/code]

Route Handlers can be nested anywhere inside the `app` directory, similar to `page.js` and `layout.js`. But there **cannot** be a `route.js` file at the same route segment level as `page.js`.

### Supported HTTP Methods[](https://nextjs.org/docs/app/getting-started/route-handlers#supported-http-methods)

The following [HTTP methods](https://developer.mozilla.org/docs/Web/HTTP/Methods) are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`. If an unsupported method is called, Next.js will return a `405 Method Not Allowed` response.

### Extended `NextRequest` and `NextResponse` APIs[](https://nextjs.org/docs/app/getting-started/route-handlers#extended-nextrequest-and-nextresponse-apis)

In addition to supporting the native [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs, Next.js extends them with [`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request) and [`NextResponse`](https://nextjs.org/docs/app/api-reference/functions/next-response) to provide convenient helpers for advanced use cases.

### Caching[](https://nextjs.org/docs/app/getting-started/route-handlers#caching)

Route Handlers are not cached by default. You can, however, opt into caching for `GET` methods. Other supported HTTP methods are **not** cached. To cache a `GET` method, use a [route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) such as `export const dynamic = 'force-static'` in your Route Handler file.

app/items/route.ts

JavaScriptTypeScript
[code]
    export const dynamic = 'force-static'
     
    export async function GET() {
      const res = await fetch('https://data.mongodb-api.com/...', {
        headers: {
          'Content-Type': 'application/json',
          'API-Key': process.env.DATA_API_KEY,
        },
      })
      const data = await res.json()
     
      return Response.json({ data })
    }
[/code]

> **Good to know** : Other supported HTTP methods are **not** cached, even if they are placed alongside a `GET` method that is cached, in the same file.

#### With Cache Components[](https://nextjs.org/docs/app/getting-started/route-handlers#with-cache-components)

When [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) is enabled, `GET` Route Handlers follow the same model as normal UI routes in your application. They run at request time by default, can be prerendered when they don't access dynamic or runtime data, and you can use `use cache` to include dynamic data in the static response.

**Static example** \- doesn't access dynamic or runtime data, so it will be prerendered at build time:

app/api/project-info/route.ts
[code]
    export async function GET() {
      return Response.json({
        projectName: 'Next.js',
      })
    }
[/code]

**Dynamic example** \- accesses non-deterministic operations. During the build, prerendering stops when `Math.random()` is called, deferring to request-time rendering:

app/api/random-number/route.ts
[code]
    export async function GET() {
      return Response.json({
        randomNumber: Math.random(),
      })
    }
[/code]

**Runtime data example** \- accesses request-specific data. Prerendering terminates when runtime APIs like `headers()` are called:

app/api/user-agent/route.ts
[code]
    import { headers } from 'next/headers'
     
    export async function GET() {
      const headersList = await headers()
      const userAgent = headersList.get('user-agent')
     
      return Response.json({ userAgent })
    }
[/code]

> **Good to know** : Prerendering stops if the `GET` handler accesses network requests, database queries, async file system operations, request object properties (like `req.url`, `request.headers`, `request.cookies`, `request.body`), runtime APIs like [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers), [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection), or non-deterministic operations.

**Cached example** \- accesses dynamic data (database query) but caches it with `use cache`, allowing it to be included in the prerendered response:

app/api/products/route.ts
[code]
    import { cacheLife } from 'next/cache'
     
    export async function GET() {
      const products = await getProducts()
      return Response.json(products)
    }
     
    async function getProducts() {
      'use cache'
      cacheLife('hours')
     
      return await db.query('SELECT * FROM products')
    }
[/code]

> **Good to know** : `use cache` cannot be used directly inside a Route Handler body; extract it to a helper function. Cached responses revalidate according to `cacheLife` when a new request arrives.

### Special Route Handlers[](https://nextjs.org/docs/app/getting-started/route-handlers#special-route-handlers)

Special Route Handlers like [`sitemap.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata) remain static by default unless they use Dynamic APIs or dynamic config options.

### Route Resolution[](https://nextjs.org/docs/app/getting-started/route-handlers#route-resolution)

You can consider a `route` the lowest level routing primitive.

  * They **do not** participate in layouts or client-side navigations like `page`.
  * There **cannot** be a `route.js` file at the same route as `page.js`.



Page| Route| Result  
---|---|---  
`app/page.js`| `app/route.js`|  Conflict  
`app/page.js`| `app/api/route.js`|  Valid  
`app/[user]/page.js`| `app/api/route.js`|  Valid  
  
Each `route.js` or `page.js` file takes over all HTTP verbs for that route.

app/page.ts

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }
     
    // Conflict
    // `app/route.ts`
    export async function POST(request: Request) {}
[/code]

Read more about how Route Handlers [complement your frontend application](https://nextjs.org/docs/app/guides/backend-for-frontend), or explore the Route Handlers [API Reference](https://nextjs.org/docs/app/api-reference/file-conventions/route).

### Route Context Helper[](https://nextjs.org/docs/app/getting-started/route-handlers#route-context-helper)

In TypeScript, you can type the `context` parameter for Route Handlers with the globally available [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper) helper:

app/users/[id]/route.ts

JavaScriptTypeScript
[code]
    import type { NextRequest } from 'next/server'
     
    export async function GET(_req: NextRequest, ctx: RouteContext<'/users/[id]'>) {
      const { id } = await ctx.params
      return Response.json({ id })
    }
[/code]

> **Good to know**
> 
>   * Types are generated during `next dev`, `next build` or `next typegen`.
> 


## API Reference

Learn more about Route Handlers

### [route.jsAPI reference for the route.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/route)### [Backend for FrontendLearn how to use Next.js as a backend framework](https://nextjs.org/docs/app/guides/backend-for-frontend)

Was this helpful?

supported.

Send
