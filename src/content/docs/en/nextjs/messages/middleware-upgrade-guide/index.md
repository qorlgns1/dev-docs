---
title: 'Middleware Upgrade Guide'
description: "As we work on improving Middleware for General Availability (GA), we've made some changes to the Middleware APIs (and how you define Middleware in you..."
---

# Middleware Upgrade Guide | Next.js

Source URL: https://nextjs.org/docs/messages/middleware-upgrade-guide

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Middleware Upgrade Guide

# Middleware Upgrade Guide

As we work on improving Middleware for General Availability (GA), we've made some changes to the Middleware APIs (and how you define Middleware in your application) based on your feedback.

This upgrade guide will help you understand the changes, why they were made, and how to migrate your existing Middleware to the new API. The guide is for Next.js developers who:

  * Currently use the beta Next.js Middleware features
  * Choose to upgrade to the next stable version of Next.js (`v12.2`)



You can start upgrading your Middleware usage today with the latest release (`npm i next@latest`).

> **Note** : These changes described in this guide are included in Next.js `12.2`. You can keep your current site structure, including nested Middleware, until you move to `12.2` (or a `canary` build of Next.js).

If you have ESLint configured, you will need to run `npm i eslint-config-next@latest --save-dev` to upgrade your ESLint configuration to ensure the same version is being used as the Next.js version. You might also need to restart VSCode for the changes to take effect.

## Using Next.js Middleware on Vercel[](https://nextjs.org/docs/messages/middleware-upgrade-guide#using-nextjs-middleware-on-vercel)

If you're using Next.js on Vercel, your existing deploys using Middleware will continue to work, and you can continue to deploy your site using Middleware. When you upgrade your site to the next stable version of Next.js (`v12.2`), you will need to follow this upgrade guide to update your Middleware.

## Breaking changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#breaking-changes)

  1. [No Nested Middleware](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-nested-middleware)
  2. [No Response Body](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)
  3. [Cookies API Revamped](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)
  4. [New User-Agent Helper](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)
  5. [No More Page Match Data](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)
  6. [Executing Middleware on Internal Next.js Requests](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)



## No Nested Middleware[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-nested-middleware)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes)

  * Define a single Middleware file next to your `pages` folder
  * No need to prefix the file with an underscore
  * A custom matcher can be used to define matching routes using an exported config object



### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation)

Previously, you could create a `_middleware.ts` file under the `pages` directory at any level. Middleware execution was based on the file path where it was created.

Based on customer feedback, we have replaced this API with a single root Middleware, which provides the following improvements:

  * **Faster execution with lower latency** : With nested Middleware, a single request could invoke multiple Middleware functions. A single Middleware means a single function execution, which is more efficient.
  * **Less expensive** : Middleware usage is billed per invocation. Using nested Middleware, a single request could invoke multiple Middleware functions, meaning multiple Middleware charges per request. A single Middleware means a single invocation per request and is more cost effective.
  * **Middleware can conveniently filter on things besides routes** : With nested Middleware, the Middleware files were located in the `pages` directory and Middleware was executed based on request paths. By moving to a single root Middleware, you can still execute code based on request paths, but you can now more conveniently execute Middleware based on other conditions, like `cookies` or the presence of a request header.
  * **Deterministic execution ordering** : With nested Middleware, a single request could match multiple Middleware functions. For example, a request to `/dashboard/users/*` would invoke Middleware defined in both `/dashboard/users/_middleware.ts` and `/dashboard/_middleware.js`. However, the execution order is difficult to reason about. Moving to a single, root Middleware more explicitly defines execution order.
  * **Supports Next.js Layouts (RFC)** : Moving to a single, root Middleware helps support the new [Layouts (RFC) in Next.js](https://nextjs.org/blog/layouts-rfc).



### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade)

You should declare **one single Middleware file** in your application, which should be located next to the `pages` directory and named **without** an `_` prefix. Your Middleware file can still have either a `.ts` or `.js` extension.

Middleware will be invoked for **every route in the app** , and a custom matcher can be used to define matching filters. The following is an example for a Middleware that triggers for `/about/*` and `/dashboard/:path*`, the custom matcher is defined in an exported config object:

middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
     
    export function middleware(request: NextRequest) {
      return NextResponse.rewrite(new URL('/about-2', request.url))
    }
     
    // Supports both a single string value or an array of matchers
    export const config = {
      matcher: ['/about/:path*', '/dashboard/:path*'],
    }
[/code]

The matcher config also allows full regex so matching like negative lookaheads or character matching is supported. An example of a negative lookahead to match all except specific paths can be seen here:

middleware.ts
[code]
    export const config = {
      matcher: [
        /*
         * Match all request paths except for the ones starting with:
         * - api (API routes)
         * - _next/static (static files)
         * - favicon.ico (favicon file)
         */
        '/((?!api|_next/static|favicon.ico).*)',
      ],
    }
[/code]

While the config option is preferred since it doesn't get invoked on every request, you can also use conditional statements to only run the Middleware when it matches specific paths. One advantage of using conditionals is defining explicit ordering for when Middleware executes. The following example shows how you can merge two previously nested Middleware:

middleware.ts
[code]
    import type { NextRequest } from 'next/server'
     
    export function middleware(request: NextRequest) {
      if (request.nextUrl.pathname.startsWith('/about')) {
        // This logic is only applied to /about
      }
     
      if (request.nextUrl.pathname.startsWith('/dashboard')) {
        // This logic is only applied to /dashboard
      }
    }
[/code]

## No Response Body[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-1)

  * Middleware can no longer produce a response body
  * If your Middleware _does_ respond with a body, a runtime error will be thrown
  * Migrate to using `rewrite`/`redirect` to pages/APIs handling a response



### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-1)

To respect the differences in client-side and server-side navigation, and to help ensure that developers do not build insecure Middleware, we are removing the ability to send response bodies in Middleware. This ensures that Middleware is only used to `rewrite`, `redirect`, or modify the incoming request (e.g. [setting cookies](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)).

The following patterns will no longer work:
[code] 
    new Response('a text value')
    new Response(streamOrBuffer)
    new Response(JSON.stringify(obj), { headers: 'application/json' })
    NextResponse.json()
[/code]

### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-1)

For cases where Middleware is used to respond (such as authorization), you should migrate to use `rewrite`/`redirect` to pages that show an authorization error, login forms, or to an API Route.

#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before)

pages/_middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
    import { isAuthValid } from './lib/auth'
     
    export function middleware(request: NextRequest) {
      // Example function to validate auth
      if (isAuthValid(request)) {
        return NextResponse.next()
      }
     
      return NextResponse.json({ message: 'Auth required' }, { status: 401 })
    }
[/code]

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after)

middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
    import { isAuthValid } from './lib/auth'
     
    export function middleware(request: NextRequest) {
      // Example function to validate auth
      if (isAuthValid(request)) {
        return NextResponse.next()
      }
     
      const loginUrl = new URL('/login', request.url)
      loginUrl.searchParams.set('from', request.nextUrl.pathname)
     
      return NextResponse.redirect(loginUrl)
    }
[/code]

#### Edge API Routes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#edge-api-routes)

If you were previously using Middleware to forward headers to an external API, you can now use [Edge API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes):

pages/api/proxy.ts
[code]
    import { type NextRequest } from 'next/server'
     
    export const config = {
      runtime: 'edge',
    }
     
    export default async function handler(req: NextRequest) {
      const authorization = req.cookies.get('authorization')
      return fetch('https://backend-api.com/api/protected', {
        method: req.method,
        headers: {
          authorization,
        },
        redirect: 'manual',
      })
    }
[/code]

## Cookies API Revamped[](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-2)

Added| Removed  
---|---  
`cookies.set`| `cookie`  
`cookies.delete`| `clearCookie`  
`cookies.getWithOptions`| `cookies`  
  
### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-2)

Based on beta feedback, we are changing the Cookies API in `NextRequest` and `NextResponse` to align more to a `get`/`set` model. The `Cookies` API extends Map, including methods like [entries](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries) and [values](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries).

### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-2)

`NextResponse` now has a `cookies` instance with:

  * `cookies.delete`
  * `cookies.set`
  * `cookies.getWithOptions`



As well as other extended methods from `Map`.

#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-1)

pages/_middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
     
    export function middleware(request: NextRequest) {
      // create an instance of the class to access the public methods. This uses `next()`,
      // you could use `redirect()` or `rewrite()` as well
      let response = NextResponse.next()
      // get the cookies from the request
      let cookieFromRequest = request.cookies['my-cookie']
      // set the `cookie`
      response.cookie('hello', 'world')
      // set the `cookie` with options
      const cookieWithOptions = response.cookie('hello', 'world', {
        path: '/',
        maxAge: 1000 * 60 * 60 * 24 * 7,
        httpOnly: true,
        sameSite: 'strict',
        domain: 'example.com',
      })
      // clear the `cookie`
      response.clearCookie('hello')
     
      return response
    }
[/code]

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-1)

middleware.ts
[code]
    export function middleware() {
      const response = new NextResponse()
     
      // set a cookie
      response.cookies.set('vercel', 'fast')
     
      // set another cookie with options
      response.cookies.set('nextjs', 'awesome', { path: '/test' })
     
      // get all the details of a cookie
      const { value, ...options } = response.cookies.getWithOptions('vercel')
      console.log(value) // => 'fast'
      console.log(options) // => { name: 'vercel', Path: '/test' }
     
      // deleting a cookie will mark it as expired
      response.cookies.delete('vercel')
     
      return response
    }
[/code]

## New User-Agent Helper[](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-3)

  * Accessing the user agent is no longer available on the request object
  * We've added a new `userAgent` helper to reduce Middleware size by `17kb`



### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-3)

To help reduce the size of your Middleware, we have extracted the user agent from the request object and created a new helper `userAgent`.

The helper is imported from `next/server` and allows you to opt in to using the user agent. The helper gives you access to the same properties that were available from the request object.

### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-3)

  * Import the `userAgent` helper from `next/server`
  * Destructure the properties you need to work with



#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-2)

pages/_middleware.ts
[code]
    import { NextRequest, NextResponse } from 'next/server'
     
    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const viewport = request.ua.device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
[/code]

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-2)

middleware.ts
[code]
    import { NextRequest, NextResponse, userAgent } from 'next/server'
     
    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const { device } = userAgent(request)
      const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
[/code]

## No More Page Match Data[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-4)

  * Use [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) to check if a Middleware is being invoked for a certain page match



### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-4)

Currently, Middleware estimates whether you are serving an asset of a Page based on the Next.js routes manifest (internal configuration). This value is surfaced through `request.page`.

To make page and asset matching more accurate, we are now using the web standard `URLPattern` API.

### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-4)

Use [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) to check if a Middleware is being invoked for a certain page match.

#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-3)

pages/_middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest, NextFetchEvent } from 'next/server'
     
    export function middleware(request: NextRequest, event: NextFetchEvent) {
      const { params } = event.request.page
      const { locale, slug } = params
     
      if (locale && slug) {
        const { search, protocol, host } = request.nextUrl
        const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
        return NextResponse.redirect(url)
      }
    }
[/code]

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-3)

middleware.ts
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
     
    const PATTERNS = [
      [
        new URLPattern({ pathname: '/:locale/:slug' }),
        ({ pathname }) => pathname.groups,
      ],
    ]
     
    const params = (url) => {
      const input = url.split('?')[0]
      let result = {}
     
      for (const [pattern, handler] of PATTERNS) {
        const patternResult = pattern.exec(input)
        if (patternResult !== null && 'pathname' in patternResult) {
          result = handler(patternResult)
          break
        }
      }
      return result
    }
     
    export function middleware(request: NextRequest) {
      const { locale, slug } = params(request.url)
     
      if (locale && slug) {
        const { search, protocol, host } = request.nextUrl
        const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
        return NextResponse.redirect(url)
      }
    }
[/code]

## Executing Middleware on Internal Next.js Requests[](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)

### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-5)

  * Middleware will be executed for _all_ requests, including `_next`



### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-5)

Prior to Next.js `v12.2`, Middleware was not executed for `_next` requests.

For cases where Middleware is used for authorization, you should migrate to use `rewrite`/`redirect` to Pages that show an authorization error, login forms, or to an API Route.

See [No Response Body](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body) for an example of how to migrate to use `rewrite`/`redirect`.

Was this helpful?

supported.

Send
