---
title: 'Guides: Redirecting'
description: 'Last updated February 20, 2026'
---

# Guides: Redirecting | Next.js

Source URL: https://nextjs.org/docs/pages/guides/redirecting

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Redirecting

Copy page

# How to handle redirects in Next.js

Last updated February 20, 2026

There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.

API| Purpose| Where| Status Code  
---|---|---|---  
[`useRouter`](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook)| Perform a client-side navigation| Components| N/A  
[`redirects` in `next.config.js`](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs)| Redirect an incoming request based on a path| `next.config.js` file| 307 (Temporary) or 308 (Permanent)  
[`NextResponse.redirect`](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy)| Redirect an incoming request based on a condition| Proxy| Any  
  
## `useRouter()` hook[](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook)

If you need to redirect inside a component, you can use the `push` method from the `useRouter` hook. For example:

app/page.tsx

JavaScriptTypeScript
[code]
    import { useRouter } from 'next/router'
     
    export default function Page() {
      const router = useRouter()
     
      return (
        <button type="button" onClick={() => router.push('/dashboard')}>
          Dashboard
        </button>
      )
    }
[/code]

> **Good to know** :
> 
>   * If you don't need to programmatically navigate a user, you should use a [`<Link>`](https://nextjs.org/docs/app/api-reference/components/link) component.
> 


See the [`useRouter` API reference](https://nextjs.org/docs/pages/api-reference/functions/use-router) for more information.

## `redirects` in `next.config.js`[](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs)

The `redirects` option in the `next.config.js` file allows you to redirect an incoming request path to a different destination path. This is useful when you change the URL structure of pages or have a list of redirects that are known ahead of time.

`redirects` supports [path](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#path-matching), [header, cookie, and query matching](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching), giving you the flexibility to redirect users based on an incoming request.

To use `redirects`, add the option to your `next.config.js` file:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      async redirects() {
        return [
          // Basic redirect
          {
            source: '/about',
            destination: '/',
            permanent: true,
          },
          // Wildcard path matching
          {
            source: '/blog/:slug',
            destination: '/news/:slug',
            permanent: true,
          },
        ]
      },
    }
     
    export default nextConfig
[/code]

See the [`redirects` API reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects) for more information.

> **Good to know** :
> 
>   * `redirects` can return a 307 (Temporary Redirect) or 308 (Permanent Redirect) status code with the `permanent` option.
>   * `redirects` may have a limit on platforms. For example, on Vercel, there's a limit of 1,024 redirects. To manage a large number of redirects (1000+), consider creating a custom solution using [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy). See [managing redirects at scale](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced) for more.
>   * `redirects` runs **before** Proxy.
> 


## `NextResponse.redirect` in Proxy[](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy)

Proxy allows you to run code before a request is completed. Then, based on the incoming request, redirect to a different URL using `NextResponse.redirect`. This is useful if you want to redirect users based on a condition (e.g. authentication, session management, etc) or have [a large number of redirects](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced).

For example, to redirect the user to a `/login` page if they are not authenticated:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse, NextRequest } from 'next/server'
    import { authenticate } from 'auth-provider'
     
    export function proxy(request: NextRequest) {
      const isAuthenticated = authenticate(request)
     
      // If the user is authenticated, continue as normal
      if (isAuthenticated) {
        return NextResponse.next()
      }
     
      // Redirect to login page if not authenticated
      return NextResponse.redirect(new URL('/login', request.url))
    }
     
    export const config = {
      matcher: '/dashboard/:path*',
    }
[/code]

> **Good to know** :
> 
>   * Proxy runs **after** `redirects` in `next.config.js` and **before** rendering.
> 


See the [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) documentation for more information.

## Managing redirects at scale (advanced)[](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced)

To manage a large number of redirects (1000+), you may consider creating a custom solution using Proxy. This allows you to handle redirects programmatically without having to redeploy your application.

To do this, you'll need to consider:

  1. Creating and storing a redirect map.
  2. Optimizing data lookup performance.



> **Next.js Example** : See our [Proxy with Bloom filter](https://redirects-bloom-filter.vercel.app/) example for an implementation of the recommendations below.

### 1\. Creating and storing a redirect map[](https://nextjs.org/docs/pages/guides/redirecting#1-creating-and-storing-a-redirect-map)

A redirect map is a list of redirects that you can store in a database (usually a key-value store) or JSON file.

Consider the following data structure:
[code] 
    {
      "/old": {
        "destination": "/new",
        "permanent": true
      },
      "/blog/post-old": {
        "destination": "/blog/post-new",
        "permanent": true
      }
    }
[/code]

In [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy), you can read from a database such as Vercel's [Edge Config](https://vercel.com/docs/edge-config/get-started) or [Redis](https://vercel.com/docs/redis), and redirect the user based on the incoming request:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse, NextRequest } from 'next/server'
    import { get } from '@vercel/edge-config'
     
    type RedirectEntry = {
      destination: string
      permanent: boolean
    }
     
    export async function proxy(request: NextRequest) {
      const pathname = request.nextUrl.pathname
      const redirectData = await get(pathname)
     
      if (redirectData && typeof redirectData === 'string') {
        const redirectEntry: RedirectEntry = JSON.parse(redirectData)
        const statusCode = redirectEntry.permanent ? 308 : 307
        return NextResponse.redirect(redirectEntry.destination, statusCode)
      }
     
      // No redirect found, continue without redirecting
      return NextResponse.next()
    }
[/code]

### 2\. Optimizing data lookup performance[](https://nextjs.org/docs/pages/guides/redirecting#2-optimizing-data-lookup-performance)

Reading a large dataset for every incoming request can be slow and expensive. There are two ways you can optimize data lookup performance:

  * Use a database that is optimized for fast reads
  * Use a data lookup strategy such as a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) to efficiently check if a redirect exists **before** reading the larger redirects file or database.



Considering the previous example, you can import a generated bloom filter file into Proxy, then, check if the incoming request pathname exists in the bloom filter.

If it does, forward the request to a  [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) which will check the actual file and redirect the user to the appropriate URL. This avoids importing a large redirects file into Proxy, which can slow down every incoming request.

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse, NextRequest } from 'next/server'
    import { ScalableBloomFilter } from 'bloom-filters'
    import GeneratedBloomFilter from './redirects/bloom-filter.json'
     
    type RedirectEntry = {
      destination: string
      permanent: boolean
    }
     
    // Initialize bloom filter from a generated JSON file
    const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter as any)
     
    export async function proxy(request: NextRequest) {
      // Get the path for the incoming request
      const pathname = request.nextUrl.pathname
     
      // Check if the path is in the bloom filter
      if (bloomFilter.has(pathname)) {
        // Forward the pathname to the Route Handler
        const api = new URL(
          `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
          request.nextUrl.origin
        )
     
        try {
          // Fetch redirect data from the Route Handler
          const redirectData = await fetch(api)
     
          if (redirectData.ok) {
            const redirectEntry: RedirectEntry | undefined =
              await redirectData.json()
     
            if (redirectEntry) {
              // Determine the status code
              const statusCode = redirectEntry.permanent ? 308 : 307
     
              // Redirect to the destination
              return NextResponse.redirect(redirectEntry.destination, statusCode)
            }
          }
        } catch (error) {
          console.error(error)
        }
      }
     
      // No redirect found, continue the request without redirecting
      return NextResponse.next()
    }
[/code]

Then, in the API Route:

pages/api/redirects.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
    import redirects from '@/app/redirects/redirects.json'
     
    type RedirectEntry = {
      destination: string
      permanent: boolean
    }
     
    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      const pathname = req.query.pathname
      if (!pathname) {
        return res.status(400).json({ message: 'Bad Request' })
      }
     
      // Get the redirect entry from the redirects.json file
      const redirect = (redirects as Record<string, RedirectEntry>)[pathname]
     
      // Account for bloom filter false positives
      if (!redirect) {
        return res.status(400).json({ message: 'No redirect' })
      }
     
      // Return the redirect entry
      return res.json(redirect)
    }
[/code]

> **Good to know:**
> 
>   * To generate a bloom filter, you can use a library like [`bloom-filters`](https://www.npmjs.com/package/bloom-filters).
>   * You should validate requests made to your Route Handler to prevent malicious requests.
> 


Was this helpful?

supported.

Send
