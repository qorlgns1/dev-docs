---
title: '업그레이드: 버전 15'
description: 'Next.js 버전 15로 업데이트하려면  코데모드를 사용할 수 있습니다:'
---

# 업그레이드: 버전 15 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/upgrading/version-15

[가이드](https://nextjs.org/docs/app/guides)[업그레이드](https://nextjs.org/docs/app/guides/upgrading)Version 15

페이지 복사

# 버전 15로 업그레이드하는 방법

마지막 업데이트 2026년 2월 20일

## 14에서 15로 업그레이드[](https://nextjs.org/docs/app/guides/upgrading/version-15#upgrading-from-14-to-15)

Next.js 버전 15로 업데이트하려면 `upgrade` 코데모드를 사용할 수 있습니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm dlx @next/codemod@canary upgrade latest
[/code]

수동으로 진행하려면 최신 Next 및 React 버전을 설치했는지 확인하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add next@latest react@latest react-dom@latest eslint-config-next@latest
[/code]

> **알아두면 좋아요:**
> 
>   * 피어 종속성 경고가 표시되면 제안된 버전으로 `react`와 `react-dom`을 업데이트하거나 경고를 무시하기 위해 `--force` 또는 `--legacy-peer-deps` 플래그를 사용해야 할 수 있습니다. Next.js 15와 React 19가 모두 안정화되면 이 작업은 필요하지 않습니다.
> 


## React 19[](https://nextjs.org/docs/app/guides/upgrading/version-15#react-19)

  * `react`와 `react-dom`의 최소 버전이 이제 19입니다.
  * `useFormState`가 `useActionState`로 대체되었습니다. `useFormState` 훅은 React 19에서 여전히 사용할 수 있지만 더 이상 권장되지 않으며 향후 릴리스에서 제거될 예정입니다. `useActionState` 사용을 권장하며 `pending` 상태를 직접 읽을 수 있는 추가 속성을 제공합니다. [자세히 알아보기](https://react.dev/reference/react/useActionState).
  * `useFormStatus`에 이제 `data`, `method`, `action`과 같은 추가 키가 포함됩니다. React 19를 사용하지 않는 경우 `pending` 키만 사용할 수 있습니다. [자세히 알아보기](https://react.dev/reference/react-dom/hooks/useFormStatus).
  * [React 19 업그레이드 가이드](https://react.dev/blog/2024/04/25/react-19-upgrade-guide)에서 더 많은 내용을 확인하세요.



> **알아두면 좋아요:** TypeScript를 사용하는 경우 `@types/react`와 `@types/react-dom`도 최신 버전으로 업그레이드하세요.

## 비동기 요청 API(호환성 파괴 변경)[](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change)

런타임 정보에 의존하던 기존의 동기 Dynamic API가 이제 **비동기**로 동작합니다:

  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default), [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)의 `params`.
  * [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)의 `searchParams`



마이그레이션 부담을 줄이기 위해 [코데모드가 제공되며](https://nextjs.org/docs/app/guides/upgrading/codemods#150) 해당 API를 일시적으로 동기 방식으로 접근할 수 있습니다.

### `cookies`[](https://nextjs.org/docs/app/guides/upgrading/version-15#cookies)

#### 권장 비동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage)
[code] 
    import { cookies } from 'next/headers'
     
    // Before
    const cookieStore = cookies()
    const token = cookieStore.get('token')
     
    // After
    const cookieStore = await cookies()
    const token = cookieStore.get('token')
[/code]

#### 임시 동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage)

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

#### 권장 비동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-1)
[code] 
    import { headers } from 'next/headers'
     
    // Before
    const headersList = headers()
    const userAgent = headersList.get('user-agent')
     
    // After
    const headersList = await headers()
    const userAgent = headersList.get('user-agent')
[/code]

#### 임시 동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-1)

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

#### 권장 비동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-2)
[code] 
    import { draftMode } from 'next/headers'
     
    // Before
    const { isEnabled } = draftMode()
     
    // After
    const { isEnabled } = await draftMode()
[/code]

#### 임시 동기 사용법[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-2)

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

#### 비동기 레이아웃[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-layout)

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

#### 동기 레이아웃[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-layout)

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

#### 비동기 페이지[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-page)

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

#### 동기 페이지[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-page)
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

#### 라우트 핸들러[](https://nextjs.org/docs/app/guides/upgrading/version-15#route-handlers)

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

## `runtime` 구성(호환성 파괴 변경)[](https://nextjs.org/docs/app/guides/upgrading/version-15#runtime-configuration-breaking-change)

`runtime` [segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime)은 이전에 `edge` 외에도 `experimental-edge` 값을 지원했습니다. 두 구성은 동일한 의미이므로 옵션을 단순화하기 위해 이제 `experimental-edge`를 사용하면 오류가 발생합니다. 이를 해결하려면 `runtime` 구성을 `edge`로 업데이트하십시오. 이를 자동으로 처리해 주는 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#app-dir-runtime-config-experimental-edge)을 사용할 수 있습니다.

## `fetch` requests[](https://nextjs.org/docs/app/guides/upgrading/version-15#fetch-requests)

[`fetch` requests](https://nextjs.org/docs/app/api-reference/functions/fetch)는 이제 기본적으로 캐시되지 않습니다.

특정 `fetch` 요청을 캐시에 넣으려면 `cache: 'force-cache'` 옵션을 전달하면 됩니다.

app/layout.js
[code]
    export default async function RootLayout() {
      const a = await fetch('https://...') // Not Cached
      const b = await fetch('https://...', { cache: 'force-cache' }) // Cached
     
      // ...
    }
[/code]

레이아웃이나 페이지의 모든 `fetch` 요청을 캐시하도록 설정하려면 `export const fetchCache = 'default-cache'` [segment config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)을 사용할 수 있습니다. 개별 `fetch` 요청에서 `cache` 옵션을 지정하면 해당 값이 우선합니다.

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

[Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)의 `GET` 함수는 더 이상 기본적으로 캐시되지 않습니다. `GET` 메서드를 캐시하도록 설정하려면 Route Handler 파일에서 `export const dynamic = 'force-static'`과 같은 [route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)을 사용할 수 있습니다.

app/api/route.js
[code]
    export const dynamic = 'force-static'
     
    export async function GET() {}
[/code]

## Client-side Router Cache[](https://nextjs.org/docs/app/guides/upgrading/version-15#client-side-router-cache)

`<Link>` 또는 `useRouter`로 페이지 사이를 이동할 때, [page](https://nextjs.org/docs/app/api-reference/file-conventions/page) 세그먼트는 더 이상 클라이언트 측 라우터 캐시에서 재사용되지 않습니다. 그러나 브라우저 뒤로/앞으로 이동과 공유 레이아웃에서는 계속 재사용됩니다.

페이지 세그먼트를 캐시에 넣으려면 [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) 구성 옵션을 사용할 수 있습니다.

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

[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout)와 [loading states](https://nextjs.org/docs/app/api-reference/file-conventions/loading)는 여전히 캐시되며 탐색 시 재사용됩니다.

## `next/font`[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextfont)

`@next/font` 패키지는 기본 제공 [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)로 대체되어 제거되었습니다. import 이름을 안전하게 자동 변경해 주는 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font)이 제공됩니다.

app/layout.js
[code]
    // Before
    import { Inter } from '@next/font/google'
     
    // After
    import { Inter } from 'next/font/google'
[/code]

## bundlePagesRouterDependencies[](https://nextjs.org/docs/app/guides/upgrading/version-15#bundlepagesrouterdependencies)

`experimental.bundlePagesExternals`는 안정화되면서 이름이 `bundlePagesRouterDependencies`로 변경되었습니다.

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

`experimental.serverComponentsExternalPackages`는 안정화되면서 이름이 `serverExternalPackages`로 변경되었습니다.

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

Next.js 15에서는 Speed Insights에 대한 자동 계측이 제거되었습니다.

Speed Insights를 계속 사용하려면 [Vercel Speed Insights Quickstart](https://vercel.com/docs/speed-insights/quickstart) 가이드를 따르십시오.

## `NextRequest` Geolocation[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextrequest-geolocation)

호스팅 제공자가 이 값을 제공하므로 `NextRequest`의 `geo` 및 `ip` 속성이 제거되었습니다. 이 마이그레이션을 자동화하는 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150)가 제공됩니다.

Vercel을 사용하는 경우 [`@vercel/functions`](https://vercel.com/docs/functions/vercel-functions-package)의 `geolocation` 및 `ipAddress` 함수를 대신 사용할 수도 있습니다.

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
