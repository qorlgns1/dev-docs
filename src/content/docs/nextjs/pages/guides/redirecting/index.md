---
title: '가이드: 리디렉션'
description: 'Last updated February 20, 2026'
---

# 가이드: 리디렉션 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/redirecting

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)리디렉션

Copy page

# Next.js에서 리디렉션을 처리하는 방법

Last updated February 20, 2026

Next.js에서 리디렉션을 처리하는 방법은 몇 가지가 있습니다. 이 페이지에서는 사용 가능한 옵션, 활용 사례, 그리고 대량의 리디렉션을 관리하는 방법을 살펴봅니다.

API| 목적| 위치| 상태 코드  
---|---|---|---  
[`useRouter`](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook)| 클라이언트 측 내비게이션 수행| 컴포넌트| 해당 없음  
[`redirects` in `next.config.js`](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs)| 경로를 기준으로 들어오는 요청을 리디렉션| `next.config.js` 파일| 307(임시) 또는 308(영구)  
[`NextResponse.redirect`](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy)| 조건을 기준으로 들어오는 요청을 리디렉션| Proxy| 임의  
  
## `useRouter()` hook[](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook)

컴포넌트 내부에서 리디렉션이 필요하다면 `useRouter` 훅의 `push` 메서드를 사용할 수 있습니다. 예:

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

> **알아두면 좋은 점** :
> 
>   * 사용자에게 프로그래밍 방식 내비게이션이 필요하지 않다면 [`<Link>`](https://nextjs.org/docs/app/api-reference/components/link) 컴포넌트를 사용해야 합니다.
> 

자세한 내용은 [`useRouter` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 참고하세요.

## `next.config.js`의 `redirects`[](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs)

`next.config.js` 파일의 `redirects` 옵션을 사용하면 들어오는 요청 경로를 다른 목적지 경로로 리디렉션할 수 있습니다. 이는 페이지의 URL 구조를 변경했거나 미리 알고 있는 리디렉션 목록이 있을 때 유용합니다.

`redirects`는 [경로](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#path-matching), [헤더·쿠키·쿼리 매칭](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)을 지원하므로 들어오는 요청에 따라 유연하게 리디렉션할 수 있습니다.

`redirects`를 사용하려면 `next.config.js` 파일에 옵션을 추가하세요:

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

자세한 내용은 [`redirects` API 레퍼런스](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)를 참고하세요.

> **알아두면 좋은 점** :
> 
>   * `redirects`는 `permanent` 옵션으로 307(임시 리디렉션) 또는 308(영구 리디렉션) 상태 코드를 반환할 수 있습니다.
>   * `redirects`는 플랫폼별로 제한이 있을 수 있습니다. 예를 들어 Vercel에서는 1,024개의 리디렉션 제한이 있습니다. 1,000개 이상의 대량 리디렉션을 관리해야 한다면 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용해 커스텀 솔루션을 만드는 것을 고려하세요. 자세한 내용은 [대규모 리디렉션 관리](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced)를 참조하세요.
>   * `redirects`는 Proxy보다 **먼저** 실행됩니다.
> 

## Proxy에서 `NextResponse.redirect`[](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy)

Proxy는 요청이 완료되기 전에 코드를 실행할 수 있게 해줍니다. 그런 다음 들어오는 요청을 기준으로 `NextResponse.redirect`를 사용해 다른 URL로 리디렉션할 수 있습니다. 이는 조건(예: 인증, 세션 관리 등)에 따라 리디렉션하거나 [대량의 리디렉션](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced)을 처리할 때 유용합니다.

예를 들어 인증되지 않은 사용자를 `/login` 페이지로 리디렉션하려면 다음과 같이 합니다:

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

> **알아두면 좋은 점** :
> 
>   * Proxy는 `next.config.js`의 `redirects` **이후**, 렌더링 **이전**에 실행됩니다.
> 

자세한 내용은 [Proxy 문서](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 참고하세요.

## 대규모 리디렉션 관리(고급)[](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced)

1,000개 이상의 리디렉션을 관리하려면 Proxy를 활용한 커스텀 솔루션을 고려할 수 있습니다. 이렇게 하면 애플리케이션을 다시 배포하지 않고도 프로그래밍 방식으로 리디렉션을 처리할 수 있습니다.

이를 위해 다음을 고려해야 합니다:

  1. 리디렉션 맵 생성 및 저장
  2. 데이터 조회 성능 최적화



> **Next.js 예제** : 아래 권장 사항을 구현한 [Proxy with Bloom filter](https://redirects-bloom-filter.vercel.app/) 예제를 참고하세요.

### 1\. 리디렉션 맵 생성 및 저장[](https://nextjs.org/docs/pages/guides/redirecting#1-creating-and-storing-a-redirect-map)

리디렉션 맵은 데이터베이스(일반적으로 키-값 저장소) 또는 JSON 파일에 저장할 수 있는 리디렉션 목록입니다.

다음 데이터 구조를 참고하세요:
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

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 Vercel의 [Edge Config](https://vercel.com/docs/edge-config/get-started)나 [Redis](https://vercel.com/docs/redis) 같은 데이터베이스를 읽어 들어오는 요청에 따라 사용자를 리디렉션할 수 있습니다:

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

### 2\. 데이터 조회 성능 최적화[](https://nextjs.org/docs/pages/guides/redirecting#2-optimizing-data-lookup-performance)

모든 요청마다 대규모 데이터를 읽는 것은 느리고 비용이 많이 들 수 있습니다. 데이터 조회 성능을 최적화하는 방법은 두 가지입니다:

  * 빠른 읽기에 최적화된 데이터베이스 사용
  * 대용량 리디렉션 파일이나 데이터베이스를 읽기 전에 리디렉션 존재 여부를 효율적으로 확인할 수 있도록 [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) 같은 데이터 조회 전략 사용



이전 예제를 고려하면, 생성된 bloom filter 파일을 Proxy에 가져와서 들어오는 요청 경로가 bloom filter에 존재하는지 확인할 수 있습니다.

존재하는 경우 [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)로 요청을 전달해 실제 파일을 확인하고 적절한 URL로 사용자를 리디렉션합니다. 이렇게 하면 대형 리디렉션 파일을 Proxy에 직접 가져오지 않아 모든 요청이 느려지는 것을 방지할 수 있습니다.

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

API Route에서는 다음과 같이 처리합니다:

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

> **알아두면 좋은 점:**
> 
>   * bloom filter를 생성하려면 [`bloom-filters`](https://www.npmjs.com/package/bloom-filters) 같은 라이브러리를 사용할 수 있습니다.
>   * 악의적인 요청을 방지하려면 Route Handler로 들어오는 요청을 검증해야 합니다.
> 

Was this helpful?

supported.

Send
