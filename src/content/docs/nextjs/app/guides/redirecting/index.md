---
title: '가이드: Redirecting'
description: '원본 URL: https://nextjs.org/docs/app/guides/redirecting'
---

# 가이드: Redirecting | Next.js

원본 URL: https://nextjs.org/docs/app/guides/redirecting

# Next.js에서 리디렉트를 처리하는 방법

최종 업데이트 2026년 2월 20일

Next.js에서 리디렉트를 처리하는 방법은 여러 가지가 있습니다. 이 페이지에서는 사용 가능한 각 옵션, 사용 사례, 그리고 대량의 리디렉트를 관리하는 방법을 다룹니다.

API| 목적| 사용 위치| 상태 코드
---|---|---|---
[`redirect`](https://nextjs.org/docs/app/guides/redirecting#redirect-function)| 변경 작업이나 이벤트 이후 사용자 리디렉트| Server Components, Server Functions, Route Handlers| 307(임시) 또는 303(Server Action)
[`permanentRedirect`](https://nextjs.org/docs/app/guides/redirecting#permanentredirect-function)| 변경 작업이나 이벤트 이후 사용자 리디렉트| Server Components, Server Functions, Route Handlers| 308(영구)
[`useRouter`](https://nextjs.org/docs/app/guides/redirecting#userouter-hook)| 클라이언트 측 내비게이션 수행| Client Components의 이벤트 핸들러| 해당 없음
[`next.config.js`의 `redirects`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs)| 경로 기반으로 들어오는 요청 리디렉트| `next.config.js` 파일| 307(임시) 또는 308(영구)
[`NextResponse.redirect`](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy)| 조건 기반으로 들어오는 요청 리디렉트| Proxy| 임의

## `redirect` 함수[](https://nextjs.org/docs/app/guides/redirecting#redirect-function)

`redirect` 함수는 사용자를 다른 URL로 리디렉트할 수 있게 해줍니다. [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data)에서 `redirect`를 호출할 수 있습니다.

`redirect`는 보통 변경 작업이나 이벤트 이후에 사용됩니다. 예를 들어 게시물을 생성할 때:

app/actions.ts

JavaScriptTypeScript
```
    'use server'

    import { redirect } from 'next/navigation'
    import { revalidatePath } from 'next/cache'

    export async function createPost(id: string) {
      try {
        // Call database
      } catch (error) {
        // Handle errors
      }

      revalidatePath('/posts') // Update cached posts
      redirect(`/post/${id}`) // Navigate to the new post page
    }
```

> **알아두면 좋아요** :
>
>   * `redirect`는 기본적으로 307(Temporary Redirect) 상태 코드를 반환합니다. Server Action에서 사용하면 303(See Other)을 반환하며, 이는 POST 요청 결과로 성공 페이지로 리디렉트할 때 일반적으로 사용됩니다.
>   * `redirect`는 오류를 던지므로 `try/catch`를 사용할 때는 `try` 블록 **밖에서** 호출해야 합니다.
>   * `redirect`는 렌더링 과정 중인 Client Components에서 호출할 수 있지만 이벤트 핸들러에서는 불가능합니다. 대신 [`useRouter` 훅](https://nextjs.org/docs/app/guides/redirecting#userouter-hook)을 사용할 수 있습니다.
>   * `redirect`는 절대 URL도 허용하므로 외부 링크로 리디렉트할 때 사용할 수 있습니다.
>   * 렌더링 전에 리디렉트하려면 [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) 또는 [Proxy](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy)를 사용하세요.
>

자세한 내용은 [`redirect` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/redirect)를 참고하세요.

## `permanentRedirect` 함수[](https://nextjs.org/docs/app/guides/redirecting#permanentredirect-function)

`permanentRedirect` 함수는 사용자를 다른 URL로 **영구적으로** 리디렉트할 수 있게 해줍니다. [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data)에서 `permanentRedirect`를 호출할 수 있습니다.

`permanentRedirect`는 보통 엔터티의 정식 URL이 변경되는 작업이나 이벤트 이후에 사용됩니다. 예를 들어 사용자가 사용자 이름을 변경한 뒤 프로필 URL을 업데이트할 때:

app/actions.ts

JavaScriptTypeScript
```
    'use server'

    import { permanentRedirect } from 'next/navigation'
    import { revalidateTag } from 'next/cache'

    export async function updateUsername(username: string, formData: FormData) {
      try {
        // Call database
      } catch (error) {
        // Handle errors
      }

      revalidateTag('username') // Update all references to the username
      permanentRedirect(`/profile/${username}`) // Navigate to the new user profile
    }
```

> **알아두면 좋아요** :
>
>   * `permanentRedirect`는 기본적으로 308(영구 리디렉트) 상태 코드를 반환합니다.
>   * `permanentRedirect`도 절대 URL을 허용하므로 외부 링크로 리디렉트할 때 사용할 수 있습니다.
>   * 렌더링 전에 리디렉트하려면 [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) 또는 [Proxy](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy)를 사용하세요.
>

자세한 내용은 [`permanentRedirect` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)를 참고하세요.

## `useRouter()` 훅[](https://nextjs.org/docs/app/guides/redirecting#userouter-hook)

Client Component의 이벤트 핸들러 안에서 리디렉트해야 한다면 `useRouter` 훅의 `push` 메서드를 사용할 수 있습니다. 예를 들어:

app/page.tsx

JavaScriptTypeScript
```
    'use client'

    import { useRouter } from 'next/navigation'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.push('/dashboard')}>
          Dashboard
        </button>
      )
    }
```

> **알아두면 좋아요** :
>
>   * 사용자를 프로그래밍적으로 내비게이션할 필요가 없다면 [`<Link>`](https://nextjs.org/docs/app/api-reference/components/link) 컴포넌트를 사용해야 합니다.
>

자세한 내용은 [`useRouter` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/use-router)를 참고하세요.

## `next.config.js`의 `redirects`[](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs)

`next.config.js` 파일의 `redirects` 옵션을 사용하면 들어오는 요청 경로를 다른 목적지 경로로 리디렉트할 수 있습니다. 이는 페이지의 URL 구조를 변경했거나 미리 알고 있는 리디렉트 목록이 있을 때 유용합니다.

`redirects`는 [경로 매칭](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#path-matching), [헤더·쿠키·쿼리 매칭](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching)을 지원하여 들어오는 요청에 따라 사용자를 유연하게 리디렉트할 수 있게 해줍니다.

`redirects`를 사용하려면 `next.config.js` 파일에 옵션을 추가하세요:

next.config.ts

JavaScriptTypeScript
```
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
```

자세한 내용은 [`redirects` API 레퍼런스](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)를 참고하세요.

> **알아두면 좋아요** :
>
>   * `redirects`는 `permanent` 옵션을 통해 307(임시 리디렉트) 또는 308(영구 리디렉트) 상태 코드를 반환할 수 있습니다.
>   * `redirects`에는 플랫폼별 제한이 있을 수 있습니다. 예를 들어 Vercel에서는 1,024개의 리디렉트 제한이 있습니다. 1000개 이상의 대량 리디렉트를 관리하려면 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용한 맞춤 솔루션을 고려하세요. 자세한 내용은 [대규모 리디렉트 관리](https://nextjs.org/docs/app/guides/redirecting#managing-redirects-at-scale-advanced)를 확인하세요.
>   * `redirects`는 Proxy보다 **먼저** 실행됩니다.
>

## Proxy에서의 `NextResponse.redirect`[](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy)

Proxy는 요청이 완료되기 전에 코드를 실행할 수 있게 해줍니다. 이후 들어오는 요청을 바탕으로 `NextResponse.redirect`를 사용해 다른 URL로 리디렉트할 수 있습니다. 이는 조건(예: 인증, 세션 관리 등)에 따라 사용자를 리디렉트하거나 [대량의 리디렉트](https://nextjs.org/docs/app/guides/redirecting#managing-redirects-at-scale-advanced)를 처리하려는 경우에 유용합니다.

예를 들어 인증되지 않은 사용자를 `/login` 페이지로 리디렉트하려면:

proxy.ts

JavaScriptTypeScript
```
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
```

> **알아두면 좋아요** :
>
>   * Proxy는 `next.config.js`의 `redirects` **이후**, 렌더링 **이전**에 실행됩니다.
>

자세한 내용은 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) 문서를 참고하세요.

## 대규모 리디렉트 관리(고급)[](https://nextjs.org/docs/app/guides/redirecting#managing-redirects-at-scale-advanced)

1000개 이상의 대량 리디렉트를 관리하려면 Proxy를 사용한 맞춤 솔루션을 고려할 수 있습니다. 이렇게 하면 애플리케이션을 다시 배포하지 않고도 프로그래밍 방식으로 리디렉트를 처리할 수 있습니다.

이를 위해 다음을 고려해야 합니다:

  1. 리디렉트 맵 생성 및 저장.
  2. 데이터 조회 성능 최적화.

> **Next.js 예제** : 아래 권장 사항을 구현한 [Bloom 필터를 사용하는 Proxy](https://redirects-bloom-filter.vercel.app/) 예제를 확인하세요.

### 1\. 리디렉트 맵 생성 및 저장[](https://nextjs.org/docs/app/guides/redirecting#1-creating-and-storing-a-redirect-map)

리디렉트 맵은 데이터베이스(주로 키-값 저장소)나 JSON 파일에 저장할 수 있는 리디렉트 목록입니다.

다음과 같은 데이터 구조를 고려해 보세요:
```
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
```

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 Vercel의 [Edge Config](https://vercel.com/docs/edge-config/get-started)나 [Redis](https://vercel.com/docs/redis) 같은 데이터베이스를 읽고, 들어오는 요청에 따라 사용자를 리디렉트할 수 있습니다:

proxy.ts

JavaScriptTypeScript
```
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
```

### 2\. 데이터 조회 성능 최적화[](https://nextjs.org/docs/app/guides/redirecting#2-optimizing-data-lookup-performance)

모든 수신 요청마다 큰 데이터셋을 읽으면 느리고 비용이 많이 듭니다. 데이터 조회 성능을 최적화하는 방법은 두 가지입니다:

  * 빠른 읽기에 최적화된 데이터베이스를 사용하기
  * 큰 리디렉션 파일이나 데이터베이스를 읽기 **전에** 리디렉션이 존재하는지 효율적으로 확인할 수 있는 [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)와 같은 데이터 조회 전략 사용하기

이전 예시를 기준으로, 생성된 bloom filter 파일을 Proxy에 가져온 뒤, 수신 요청의 pathname이 bloom filter에 존재하는지 확인할 수 있습니다.

존재한다면 요청을 실제 파일을 확인하고 사용자를 적절한 URL로 리디렉션할 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)로 전달하세요. 이렇게 하면 모든 수신 요청을 느리게 만드는 대형 redirects 파일을 Proxy에 가져올 필요가 없습니다.

proxy.ts

JavaScriptTypeScript
```
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
```

다음으로 Route Handler에서:

app/api/redirects/route.ts

JavaScriptTypeScript
```
    import { NextRequest, NextResponse } from 'next/server'
    import redirects from '@/app/redirects/redirects.json'

    type RedirectEntry = {
      destination: string
      permanent: boolean
    }

    export function GET(request: NextRequest) {
      const pathname = request.nextUrl.searchParams.get('pathname')
      if (!pathname) {
        return new Response('Bad Request', { status: 400 })
      }

      // Get the redirect entry from the redirects.json file
      const redirect = (redirects as Record<string, RedirectEntry>)[pathname]

      // Account for bloom filter false positives
      if (!redirect) {
        return new Response('No redirect', { status: 400 })
      }

      // Return the redirect entry
      return NextResponse.json(redirect)
    }
```

> **알아두면 좋은 점:**
>
>   * bloom filter를 생성하려면 [`bloom-filters`](https://www.npmjs.com/package/bloom-filters)와 같은 라이브러리를 사용할 수 있습니다.
>   * 악의적인 요청을 막기 위해 Route Handler로 들어오는 요청을 반드시 검증하세요.
>

##

- [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect)
  - 함수에 대한 API Reference.

- [permanentRedirect](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)
  - 함수에 대한 API Reference.

- [proxy.js](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  - 파일에 대한 API reference.

- [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
  - Next.js 앱에 리디렉션 추가.