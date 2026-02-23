---
title: 'Upgrading: Version 15'
description: 'Last updated February 20, 2026'
---

# Upgrading: Version 15 | Next.js

Source URL: https://nextjs.org/docs/app/guides/upgrading/version-15

[Guides](https://nextjs.org/docs/app/guides)[Upgrading](https://nextjs.org/docs/app/guides/upgrading)Version 15

Copy page

# How to upgrade to version 15

Last updated February 20, 2026

## Upgrading from 14 to 15[](https://nextjs.org/docs/app/guides/upgrading/version-15#upgrading-from-14-to-15)

To update to Next.js version 15, you can use the `upgrade` codemod:

pnpmnpmyarnbun

Terminal
[code]
    pnpm dlx @next/codemod@canary upgrade latest
[/code]

If you prefer to do it manually, ensure that you're installing the latest Next & React versions:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add next@latest react@latest react-dom@latest eslint-config-next@latest
[/code]

> **Good to know:**
> 
>   * If you see a peer dependencies warning, you may need to update `react` and `react-dom` to the suggested versions, or use the `--force` or `--legacy-peer-deps` flag to ignore the warning. This won't be necessary once both Next.js 15 and React 19 are stable.
> 


## React 19[](https://nextjs.org/docs/app/guides/upgrading/version-15#react-19)

  * The minimum versions of `react` and `react-dom` is now 19.
  * `useFormState` has been replaced by `useActionState`. The `useFormState` hook is still available in React 19, but it is deprecated and will be removed in a future release. `useActionState` is recommended and includes additional properties like reading the `pending` state directly. [Learn more](https://react.dev/reference/react/useActionState).
  * `useFormStatus` now includes additional keys like `data`, `method`, and `action`. If you are not using React 19, only the `pending` key is available. [Learn more](https://react.dev/reference/react-dom/hooks/useFormStatus).
  * Read more in the [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide).



> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

## Async Request APIs (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change)

Previously synchronous Dynamic APIs that rely on runtime information are now **asynchronous** :

  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * `params` in [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default), [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), and [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons).
  * `searchParams` in [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)



To ease the burden of migration, a [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#150) to automate the process and the APIs can temporarily be accessed synchronously.

### `cookies`[](https://nextjs.org/docs/app/guides/upgrading/version-15#cookies)

#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage)
[code] 
    import { cookies } from 'next/headers'
     
    // Before
    const cookieStore = cookies()
    const token = cookieStore.get('token')
     
    // After
    const cookieStore = await cookies()
    const token = cookieStore.get('token')
[/code]

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage)

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies, type UnsafeUnwrappedCookies } from 'next/headers'
     
    // Before
    const cookieStore = cookies()
    const token = cookieStore.get('token')
     
    // After
    const cookieStore = cookies() as unknown as UnsafeUnwrappedCookies
    // will log a warning in dev
    const token = cookieStore.get('token')
[/code]

### `headers`[](https://nextjs.org/docs/app/guides/upgrading/version-15#headers)

#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-1)
[code] 
    import { headers } from 'next/headers'
     
    // Before
    const headersList = headers()
    const userAgent = headersList.get('user-agent')
     
    // After
    const headersList = await headers()
    const userAgent = headersList.get('user-agent')
[/code]

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-1)

app/page.tsx

JavaScriptTypeScript
[code]
    import { headers, type UnsafeUnwrappedHeaders } from 'next/headers'
     
    // Before
    const headersList = headers()
    const userAgent = headersList.get('user-agent')
     
    // After
    const headersList = headers() as unknown as UnsafeUnwrappedHeaders
    // will log a warning in dev
    const userAgent = headersList.get('user-agent')
[/code]

### `draftMode`[](https://nextjs.org/docs/app/guides/upgrading/version-15#draftmode)

#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-2)
[code] 
    import { draftMode } from 'next/headers'
     
    // Before
    const { isEnabled } = draftMode()
     
    // After
    const { isEnabled } = await draftMode()
[/code]

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-2)

app/page.tsx

JavaScriptTypeScript
[code]
    import { draftMode, type UnsafeUnwrappedDraftMode } from 'next/headers'
     
    // Before
    const { isEnabled } = draftMode()
     
    // After
    // will log a warning in dev
    const { isEnabled } = draftMode() as unknown as UnsafeUnwrappedDraftMode
[/code]

### `params` & `searchParams`[](https://nextjs.org/docs/app/guides/upgrading/version-15#params--searchparams)

#### Asynchronous Layout[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-layout)

app/layout.tsx

JavaScriptTypeScript
[code]
    // Before
    type Params = { slug: string }
     
    export function generateMetadata({ params }: { params: Params }) {
      const { slug } = params
    }
     
    export default async function Layout({
      children,
      params,
    }: {
      children: React.ReactNode
      params: Params
    }) {
      const { slug } = params
    }
     
    // After
    type Params = Promise<{ slug: string }>
     
    export async function generateMetadata({ params }: { params: Params }) {
      const { slug } = await params
    }
     
    export default async function Layout({
      children,
      params,
    }: {
      children: React.ReactNode
      params: Params
    }) {
      const { slug } = await params
    }
[/code]

#### Synchronous Layout[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-layout)

app/layout.tsx

JavaScriptTypeScript
[code]
    // Before
    type Params = { slug: string }
     
    export default function Layout({
      children,
      params,
    }: {
      children: React.ReactNode
      params: Params
    }) {
      const { slug } = params
    }
     
    // After
    import { use } from 'react'
     
    type Params = Promise<{ slug: string }>
     
    export default function Layout(props: {
      children: React.ReactNode
      params: Params
    }) {
      const params = use(props.params)
      const slug = params.slug
    }
[/code]

#### Asynchronous Page[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-page)

app/page.tsx

JavaScriptTypeScript
[code]
    // Before
    type Params = { slug: string }
    type SearchParams = { [key: string]: string | string[] | undefined }
     
    export function generateMetadata({
      params,
      searchParams,
    }: {
      params: Params
      searchParams: SearchParams
    }) {
      const { slug } = params
      const { query } = searchParams
    }
     
    export default async function Page({
      params,
      searchParams,
    }: {
      params: Params
      searchParams: SearchParams
    }) {
      const { slug } = params
      const { query } = searchParams
    }
     
    // After
    type Params = Promise<{ slug: string }>
    type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>
     
    export async function generateMetadata(props: {
      params: Params
      searchParams: SearchParams
    }) {
      const params = await props.params
      const searchParams = await props.searchParams
      const slug = params.slug
      const query = searchParams.query
    }
     
    export default async function Page(props: {
      params: Params
      searchParams: SearchParams
    }) {
      const params = await props.params
      const searchParams = await props.searchParams
      const slug = params.slug
      const query = searchParams.query
    }
[/code]

#### Synchronous Page[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-page)
[code] 
    'use client'
     
    // Before
    type Params = { slug: string }
    type SearchParams = { [key: string]: string | string[] | undefined }
     
    export default function Page({
      params,
      searchParams,
    }: {
      params: Params
      searchParams: SearchParams
    }) {
      const { slug } = params
      const { query } = searchParams
    }
     
    // After
    import { use } from 'react'
     
    type Params = Promise<{ slug: string }>
    type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>
     
    export default function Page(props: {
      params: Params
      searchParams: SearchParams
    }) {
      const params = use(props.params)
      const searchParams = use(props.searchParams)
      const slug = params.slug
      const query = searchParams.query
    }
[/code]
[code] 
    // Before
    export default function Page({ params, searchParams }) {
      const { slug } = params
      const { query } = searchParams
    }
     
    // After
    import { use } from "react"
     
    export default function Page(props) {
      const params = use(props.params)
      const searchParams = use(props.searchParams)
      const slug = params.slug
      const query = searchParams.query
    }
     
[/code]

#### Route Handlers[](https://nextjs.org/docs/app/guides/upgrading/version-15#route-handlers)

app/api/route.ts

JavaScriptTypeScript
[code]
    // Before
    type Params = { slug: string }
     
    export async function GET(request: Request, segmentData: { params: Params }) {
      const params = segmentData.params
      const slug = params.slug
    }
     
    // After
    type Params = Promise<{ slug: string }>
     
    export async function GET(request: Request, segmentData: { params: Params }) {
      const params = await segmentData.params
      const slug = params.slug
    }
[/code]

## `runtime` configuration (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-15#runtime-configuration-breaking-change)

The `runtime` [segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) previously supported a value of `experimental-edge` in addition to `edge`. Both configurations refer to the same thing, and to simplify the options, we will now error if `experimental-edge` is used. To fix this, update your `runtime` configuration to `edge`. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#app-dir-runtime-config-experimental-edge) is available to automatically do this.

## `fetch` requests[](https://nextjs.org/docs/app/guides/upgrading/version-15#fetch-requests)

[`fetch` requests](https://nextjs.org/docs/app/api-reference/functions/fetch) are no longer cached by default.

To opt specific `fetch` requests into caching, you can pass the `cache: 'force-cache'` option.

app/layout.js
[code]
    export default async function RootLayout() {
      const a = await fetch('https://...') // Not Cached
      const b = await fetch('https://...', { cache: 'force-cache' }) // Cached
     
      // ...
    }
[/code]

To opt all `fetch` requests in a layout or page into caching, you can use the `export const fetchCache = 'default-cache'` [segment config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config). If individual `fetch` requests specify a `cache` option, that will be used instead.

app/layout.js
[code]
    // Since this is the root layout, all fetch requests in the app
    // that don't set their own cache option will be cached.
    export const fetchCache = 'default-cache'
     
    export default async function RootLayout() {
      const a = await fetch('https://...') // Cached
      const b = await fetch('https://...', { cache: 'no-store' }) // Not cached
     
      // ...
    }
[/code]

## Route Handlers[](https://nextjs.org/docs/app/guides/upgrading/version-15#route-handlers-1)

`GET` functions in [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) are no longer cached by default. To opt `GET` methods into caching, you can use a [route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) such as `export const dynamic = 'force-static'` in your Route Handler file.

app/api/route.js
[code]
    export const dynamic = 'force-static'
     
    export async function GET() {}
[/code]

## Client-side Router Cache[](https://nextjs.org/docs/app/guides/upgrading/version-15#client-side-router-cache)

When navigating between pages via `<Link>` or `useRouter`, [page](https://nextjs.org/docs/app/api-reference/file-conventions/page) segments are no longer reused from the client-side router cache. However, they are still reused during browser backward and forward navigation and for shared layouts.

To opt page segments into caching, you can use the [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) config option:

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        staleTimes: {
          dynamic: 30,
          static: 180,
        },
      },
    }
     
    module.exports = nextConfig
[/code]

[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) and [loading states](https://nextjs.org/docs/app/api-reference/file-conventions/loading) are still cached and reused on navigation.

## `next/font`[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextfont)

The `@next/font` package has been removed in favor of the built-in [`next/font`](https://nextjs.org/docs/app/api-reference/components/font). A [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font) to safely and automatically rename your imports.

app/layout.js
[code]
    // Before
    import { Inter } from '@next/font/google'
     
    // After
    import { Inter } from 'next/font/google'
[/code]

## bundlePagesRouterDependencies[](https://nextjs.org/docs/app/guides/upgrading/version-15#bundlepagesrouterdependencies)

`experimental.bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // Before
      experimental: {
        bundlePagesExternals: true,
      },
     
      // After
      bundlePagesRouterDependencies: true,
    }
     
    module.exports = nextConfig
[/code]

## serverExternalPackages[](https://nextjs.org/docs/app/guides/upgrading/version-15#serverexternalpackages)

`experimental.serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // Before
      experimental: {
        serverComponentsExternalPackages: ['package-name'],
      },
     
      // After
      serverExternalPackages: ['package-name'],
    }
     
    module.exports = nextConfig
[/code]

## Speed Insights[](https://nextjs.org/docs/app/guides/upgrading/version-15#speed-insights)

Auto instrumentation for Speed Insights was removed in Next.js 15.

To continue using Speed Insights, follow the [Vercel Speed Insights Quickstart](https://vercel.com/docs/speed-insights/quickstart) guide.

## `NextRequest` Geolocation[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextrequest-geolocation)

The `geo` and `ip` properties on `NextRequest` have been removed as these values are provided by your hosting provider. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available to automate this migration.

If you are using Vercel, you can alternatively use the `geolocation` and `ipAddress` functions from [`@vercel/functions`](https://vercel.com/docs/functions/vercel-functions-package) instead:

middleware.ts
[code]
    import { geolocation } from '@vercel/functions'
    import type { NextRequest } from 'next/server'
     
    export function middleware(request: NextRequest) {
      const { city } = geolocation(request)
     
      // ...
    }
[/code]

middleware.ts
[code]
    import { ipAddress } from '@vercel/functions'
    import type { NextRequest } from 'next/server'
     
    export function middleware(request: NextRequest) {
      const ip = ipAddress(request)
     
      // ...
    }
[/code]

Was this helpful?

supported.

Send
