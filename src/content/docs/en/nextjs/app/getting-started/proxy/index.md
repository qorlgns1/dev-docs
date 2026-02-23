---
title: 'Getting Started: Proxy'
description: '> Good to know : Starting with Next.js 16, Middleware is now called Proxy to better reflect its purpose. The functionality remains the same.'
---

# Getting Started: Proxy | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/proxy

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Proxy

Copy page

# Proxy

Last updated February 20, 2026

## Proxy[](https://nextjs.org/docs/app/getting-started/proxy#proxy)

> **Good to know** : Starting with Next.js 16, Middleware is now called Proxy to better reflect its purpose. The functionality remains the same.

Proxy allows you to run code before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

### Use cases[](https://nextjs.org/docs/app/getting-started/proxy#use-cases)

Some common scenarios where Proxy is effective include:

  * Modifying headers for all pages or a subset of pages
  * Rewriting to different pages based on A/B tests or experiments
  * Programmatic redirects based on incoming request properties



For simple redirects, consider using the [`redirects`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects) configuration in `next.config.ts` first. Proxy should be used when you need access to request data or more complex logic.

Proxy is _not_ intended for slow data fetching. While Proxy can be helpful for [optimistic checks](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional) such as permission-based redirects, it should not be used as a full session management or authorization solution.

Using fetch with `options.cache`, `options.next.revalidate`, or `options.next.tags`, has no effect in Proxy.

### Convention[](https://nextjs.org/docs/app/getting-started/proxy#convention)

Create a `proxy.ts` (or `.js`) file in the project root, or inside `src` if applicable, so that it is located at the same level as `pages` or `app`.

> **Note** : While only one `proxy.ts` file is supported per project, you can still organize your proxy logic into modules. Break out proxy functionalities into separate `.ts` or `.js` files and import them into your main `proxy.ts` file. This allows for cleaner management of route-specific proxy, aggregated in the `proxy.ts` for centralized control. By enforcing a single proxy file, it simplifies configuration, prevents potential conflicts, and optimizes performance by avoiding multiple proxy layers.

### Example[](https://nextjs.org/docs/app/getting-started/proxy#example)

You can export your proxy function as either a default export or a named `proxy` export:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
     
    // This function can be marked `async` if using `await` inside
    export function proxy(request: NextRequest) {
      return NextResponse.redirect(new URL('/home', request.url))
    }
     
    // Alternatively, you can use a default export:
    // export default function proxy(request: NextRequest) { ... }
     
    export const config = {
      matcher: '/about/:path*',
    }
[/code]

The `matcher` config allows you to filter Proxy to run on specific paths. See the [Matcher](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher) documentation for more details on path matching.

Read more about [using `proxy`](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy), or refer to the `proxy` [API reference](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).

## API Reference

Learn more about Proxy

### [proxy.jsAPI reference for the proxy.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)### [Backend for FrontendLearn how to use Next.js as a backend framework](https://nextjs.org/docs/app/guides/backend-for-frontend)

Was this helpful?

supported.

Send
