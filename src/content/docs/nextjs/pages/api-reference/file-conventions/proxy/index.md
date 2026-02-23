---
title: '파일 시스템 규칙: Proxy'
description: '> 참고:  파일 규칙은 더 이상 사용되지 않으며 로 이름이 변경되었습니다. 자세한 내용은 Proxy로의 마이그레이션을 참고하세요.'
---

# 파일 시스템 규칙: Proxy | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/file-conventions/proxy

# Proxy

마지막 업데이트 2026년 2월 20일

> **참고**: `middleware` 파일 규칙은 더 이상 사용되지 않으며 `proxy`로 이름이 변경되었습니다. 자세한 내용은 [Proxy로의 마이그레이션](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#migration-to-proxy)을 참고하세요.

`proxy.js|ts` 파일은 [Proxy](https://nextjs.org/docs/app/getting-started/proxy)를 작성하고 요청이 완료되기 전에 서버에서 코드를 실행하는 데 사용됩니다. 이후 들어오는 요청에 따라 재작성, 리디렉션, 요청/응답 헤더 수정, 직접 응답 등을 통해 응답을 조정할 수 있습니다.

Proxy는 라우트가 렌더링되기 전에 실행됩니다. 인증, 로깅, 리디렉션 처리처럼 사용자 지정 서버 로직을 구현할 때 특히 유용합니다.

> **알아두면 좋아요**:
>
> Proxy는 렌더 코드와 별도로 호출되며, 최적화된 사례에서는 빠른 리다이렉트/리라이트 처리를 위해 CDN에 배포됩니다. 공유 모듈이나 전역 상태에 의존하려 해서는 안 됩니다.
>
> Proxy에서 애플리케이션으로 정보를 전달하려면 [headers](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#setting-headers), [cookies](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#using-cookies), [rewrites](https://nextjs.org/docs/app/api-reference/functions/next-response#rewrite), [redirects](https://nextjs.org/docs/app/api-reference/functions/next-response#redirect), 또는 URL을 사용하세요.

프로젝트 루트 또는 필요한 경우 `src` 내부에 `proxy.ts`(또는 `.js`) 파일을 생성하여 `pages` 또는 `app`과 동일한 계층에 위치시키세요.

[`pageExtensions`](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)를 `.page.ts` 또는 `.page.js`로 커스터마이즈했다면, 파일 이름을 각각 `proxy.page.ts` 또는 `proxy.page.js`로 지정하세요.

proxy.ts

JavaScriptTypeScript
```
    import { NextResponse, NextRequest } from 'next/server'

    // This function can be marked `async` if using `await` inside
    export function proxy(request: NextRequest) {
      return NextResponse.redirect(new URL('/home', request.url))
    }

    export const config = {
      matcher: '/about/:path*',
    }
```

## Exports[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#exports)

### Proxy function[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#proxy-function)

파일은 기본 export이거나 `proxy`로 명명된 단일 함수를 export해야 합니다. 동일한 파일에서 여러 proxy를 export하는 것은 지원되지 않습니다.

proxy.js
```
    // Example of default export
    export default function proxy(request) {
      // Proxy logic
    }
```

### Config object (optional)[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#config-object-optional)

선택적으로 Proxy 함수와 함께 config 객체를 export할 수 있습니다. 이 객체에는 Proxy가 적용될 경로를 지정하는 [matcher](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#matcher)가 포함됩니다.

### Matcher[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#matcher)

`matcher` 옵션을 사용하면 Proxy가 실행될 특정 경로를 지정할 수 있습니다. 경로는 여러 방식으로 지정할 수 있습니다.

  * 단일 경로: 문자열로 직접 경로를 정의합니다. 예: `'/about'`.
  * 여러 경로: 배열로 나열합니다. 예: `matcher: ['/about', '/contact']`는 `/about`과 `/contact` 모두에 Proxy를 적용합니다.

proxy.js
```
    export const config = {
      matcher: ['/about/:path*', '/dashboard/:path*'],
    }
```

또한 `matcher` 옵션은 정규식을 사용한 복잡한 경로 지정도 지원합니다. 예를 들어 정규식 matcher를 사용해 특정 경로를 제외할 수 있습니다.

proxy.js
```
    export const config = {
      matcher: [
        // Exclude API routes, static files, image optimizations, and .png files
        '/((?!api|_next/static|_next/image|.*\\.png$).*)',
      ],
    }
```

이를 통해 포함하거나 제외할 경로를 정밀하게 제어할 수 있습니다.

`matcher` 옵션은 다음 키를 가진 객체 배열을 허용합니다.

  * `source`: 요청 경로를 매칭하기 위한 경로 또는 패턴입니다. 직접 경로 매칭을 위한 문자열이거나 더 복잡한 매칭을 위한 패턴일 수 있습니다.
  * `locale` (선택): `false`로 설정하면 경로 매칭 시 로케일 기반 라우팅을 무시합니다.
  * `has` (선택): 헤더, 쿼리 파라미터, 쿠키 등 특정 요청 요소의 존재를 기반으로 조건을 지정합니다.
  * `missing` (선택): 특정 헤더나 쿠키가 없는 상황 등 요청 요소가 존재하지 않는 조건에 집중합니다.

proxy.js
```
    export const config = {
      matcher: [
        {
          source: '/api/:path*',
          locale: false,
          has: [
            { type: 'header', key: 'Authorization', value: 'Bearer Token' },
            { type: 'query', key: 'userId', value: '123' },
          ],
          missing: [{ type: 'cookie', key: 'session', value: 'active' }],
        },
      ],
    }
```

`source` 경로 패턴은 다음과 같습니다.

  1. 반드시 `/`로 시작해야 합니다.
  2. 명명된 매개변수를 포함할 수 있습니다: `/about/:path`는 `/about/a`와 `/about/b`를 매칭하지만 `/about/a/c`는 매칭하지 않습니다.
  3. 명명된 매개변수에 수정자를 사용할 수 있습니다(`:`로 시작). `/about/:path*`는 `*`가 0개 이상을 의미하므로 `/about/a/b/c`와 매칭됩니다. `?`는 0개 또는 1개, `+`는 1개 이상을 의미합니다.
  4. 괄호로 감싼 정규식을 사용할 수 있습니다: `/about/(.*)`는 `/about/:path*`와 동일합니다.
  5. 경로의 시작에 고정됩니다: `/about`은 `/about`과 `/about/team`을 매칭하지만 `/blog/about`은 매칭하지 않습니다.

자세한 내용은 [path-to-regexp](https://github.com/pillarjs/path-to-regexp#path-to-regexp-1) 문서를 참고하세요.

> **알아두면 좋아요**:
>
>   * `matcher` 값은 정적 분석을 위해 상수여야 합니다. 변수 같은 동적 값은 무시됩니다.
>   * 하위 호환성을 위해 Next.js는 항상 `/public`을 `/public/index`로 간주합니다. 따라서 `/public/:path` matcher는 매칭됩니다.
>

## Params[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#params)

### `request`[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#request)

Proxy를 정의할 때 기본 export 함수는 단일 매개변수 `request`를 받습니다. 이 매개변수는 들어오는 HTTP 요청을 나타내는 `NextRequest` 인스턴스입니다.

proxy.ts

JavaScriptTypeScript
```
    import type { NextRequest } from 'next/server'

    export function proxy(request: NextRequest) {
      // Proxy logic goes here
    }
```

> **알아두면 좋아요**:
>
>   * `NextRequest`는 Next.js Proxy에서 들어오는 HTTP 요청을 나타내는 타입이고, [`NextResponse`](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#nextresponse)는 HTTP 응답을 조작하고 반환하는 데 사용하는 클래스입니다.
>

## NextResponse[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#nextresponse)

`NextResponse` API를 사용하면 다음을 수행할 수 있습니다.

  * 들어오는 요청을 다른 URL로 `redirect`
  * 지정된 URL을 표시하여 응답을 `rewrite`
  * API Routes, `getServerSideProps`, `rewrite` 대상에 대해 요청 헤더 설정
  * 응답 쿠키 설정
  * 응답 헤더 설정

Proxy에서 응답을 생성하는 방법:

  1. 응답을 생성하는 라우트([Page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts) 또는 [Edge API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes))로 `rewrite`
  2. `NextResponse`를 직접 반환합니다. [응답 생성](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#producing-a-response)을 참고하세요.

## Execution order[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#execution-order)

Proxy는 **프로젝트의 모든 라우트**에 대해 호출됩니다. 따라서 [matchers](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#matcher)를 사용해 특정 라우트를 정확히 타겟팅하거나 제외하는 것이 중요합니다. 실행 순서는 다음과 같습니다.

  1. `next.config.js`의 `headers`
  2. `next.config.js`의 `redirects`
  3. Proxy(`rewrites`, `redirects` 등)
  4. `next.config.js`의 `beforeFiles`(`rewrites`)
  5. 파일 시스템 라우트(`public/`, `_next/static/`, `pages/`, `app/` 등)
  6. `next.config.js`의 `afterFiles`(`rewrites`)
  7. 동적 라우트(`/blog/[slug]`)
  8. `next.config.js`의 `fallback`(`rewrites`)

## Runtime[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#runtime)

Proxy는 기본적으로 Node.js 런타임을 사용합니다. [`runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) config 옵션은 Proxy 파일에서 사용할 수 없습니다. Proxy에서 `runtime` config 옵션을 설정하면 오류가 발생합니다.

## Advanced Proxy flags[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#advanced-proxy-flags)

Next.js `v13.1`에서는 고급 사용 사례를 처리하기 위해 `skipMiddlewareUrlNormalize`와 `skipTrailingSlashRedirect` 두 가지 추가 proxy 플래그가 도입되었습니다.

`skipTrailingSlashRedirect`는 트레일링 슬래시를 추가하거나 제거하는 Next.js 리디렉트를 비활성화합니다. 이를 통해 일부 경로에는 트레일링 슬래시를 유지하고 다른 경로에는 유지하지 않는 맞춤 처리를 proxy 내부에서 구현할 수 있어 점진적 마이그레이션이 쉬워집니다.

next.config.js
```
    module.exports = {
      skipTrailingSlashRedirect: true,
    }
```

proxy.js
```
    const legacyPrefixes = ['/docs', '/blog']

    export default async function proxy(req) {
      const { pathname } = req.nextUrl

      if (legacyPrefixes.some((prefix) => pathname.startsWith(prefix))) {
        return NextResponse.next()
      }

      // apply trailing slash handling
      if (
        !pathname.endsWith('/') &&
        !pathname.match(/((?!\.well-known(?:\/.*)?)(?:[^/]+\/)*[^/]+\.\w+)/)
      ) {
        return NextResponse.redirect(
          new URL(`${req.nextUrl.pathname}/`, req.nextUrl)
        )
      }
    }
```

`skipMiddlewareUrlNormalize`는 Next.js의 URL 정규화를 비활성화해 직접 방문과 클라이언트 전환을 동일하게 처리할 수 있도록 합니다. 일부 고급 사례에서는 원본 URL을 사용해 완전한 제어를 제공하기도 합니다.

next.config.js
```
    module.exports = {
      skipMiddlewareUrlNormalize: true,
    }
```

proxy.js
```
    export default async function proxy(req) {
      const { pathname } = req.nextUrl

      // GET /_next/data/build-id/hello.json

      console.log(pathname)
      // with the flag this now /_next/data/build-id/hello.json
      // without the flag this would be normalized to /hello
    }
```

## Examples[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#examples)

### Conditional Statements[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#conditional-statements)

proxy.ts

JavaScriptTypeScript
```
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'

    export function proxy(request: NextRequest) {
      if (request.nextUrl.pathname.startsWith('/about')) {
        return NextResponse.rewrite(new URL('/about-2', request.url))
      }

      if (request.nextUrl.pathname.startsWith('/dashboard')) {
        return NextResponse.rewrite(new URL('/dashboard/user', request.url))
      }
    }
```

### Using Cookies[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#using-cookies)

쿠키는 일반적인 헤더입니다. `Request`에서는 `Cookie` 헤더에 저장되고, `Response`에서는 `Set-Cookie` 헤더에 있습니다. Next.js는 `NextRequest`와 `NextResponse`의 `cookies` 확장을 통해 이러한 쿠키에 접근하고 조작하는 편리한 방법을 제공합니다.

  1. 들어오는 요청의 경우 `cookies`에는 `get`, `getAll`, `set`, `delete` 메서드가 있으며, `has`로 특정 쿠키의 존재를 확인하거나 `clear`로 모든 쿠키를 제거할 수 있습니다.
  2. 나가는 응답의 경우 `cookies`에는 `get`, `getAll`, `set`, `delete` 메서드가 있습니다.

proxy.ts

JavaScriptTypeScript
```
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'

    export function proxy(request: NextRequest) {
      // Assume a "Cookie:nextjs=fast" header to be present on the incoming request
      // Getting cookies from the request using the `RequestCookies` API
      let cookie = request.cookies.get('nextjs')
      console.log(cookie) // => { name: 'nextjs', value: 'fast', Path: '/' }
      const allCookies = request.cookies.getAll()
      console.log(allCookies) // => [{ name: 'nextjs', value: 'fast' }]

      request.cookies.has('nextjs') // => true
      request.cookies.delete('nextjs')
      request.cookies.has('nextjs') // => false

      // Setting cookies on the response using the `ResponseCookies` API
      const response = NextResponse.next()
      response.cookies.set('vercel', 'fast')
      response.cookies.set({
        name: 'vercel',
        value: 'fast',
        path: '/',
      })
      cookie = response.cookies.get('vercel')
      console.log(cookie) // => { name: 'vercel', value: 'fast', Path: '/' }
      // The outgoing response will have a `Set-Cookie:vercel=fast;path=/` header.

      return response
    }
```

### 헤더 설정[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#setting-headers)

`NextResponse` API를 사용해 요청 및 응답 헤더를 설정할 수 있습니다(요청 헤더 설정은 Next.js v13.0.0부터 지원).

proxy.ts

JavaScriptTypeScript
```
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'

    export function proxy(request: NextRequest) {
      // Clone the request headers and set a new header `x-hello-from-proxy1`
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('x-hello-from-proxy1', 'hello')

      // You can also set request headers in NextResponse.next
      const response = NextResponse.next({
        request: {
          // New request headers
          headers: requestHeaders,
        },
      })

      // Set a new response header `x-hello-from-proxy2`
      response.headers.set('x-hello-from-proxy2', 'hello')
      return response
    }
```

이 스니펫은 다음을 사용합니다.

  * `requestHeaders`를 업스트림에서 사용할 수 있도록 `NextResponse.next({ request: { headers: requestHeaders } })`
  * 클라이언트에 `requestHeaders`를 노출하므로 사용하지 말아야 하는 `NextResponse.next({ headers: requestHeaders })`

[Proxy에서의 NextResponse 헤더](https://nextjs.org/docs/app/api-reference/functions/next-response#next)에서 더 알아보세요.

> **알아두면 좋아요** : 백엔드 웹 서버 설정에 따라 [431 Request Header Fields Too Large](https://developer.mozilla.org/docs/Web/HTTP/Status/431) 오류가 발생할 수 있으므로 큰 헤더 설정은 피하세요.

### CORS[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#cors)

Proxy에서 CORS 헤더를 설정하여 [simple](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) 요청과 [preflighted](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests) 요청을 포함한 교차 출처 요청을 허용할 수 있습니다.

proxy.ts

JavaScriptTypeScript
```
    import { NextRequest, NextResponse } from 'next/server'

    const allowedOrigins = ['https://acme.com', 'https://my-app.org']

    const corsOptions = {
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    }

    export function proxy(request: NextRequest) {
      // Check the origin from the request
      const origin = request.headers.get('origin') ?? ''
      const isAllowedOrigin = allowedOrigins.includes(origin)

      // Handle preflighted requests
      const isPreflight = request.method === 'OPTIONS'

      if (isPreflight) {
        const preflightHeaders = {
          ...(isAllowedOrigin && { 'Access-Control-Allow-Origin': origin }),
          ...corsOptions,
        }
        return NextResponse.json({}, { headers: preflightHeaders })
      }

      // Handle simple requests
      const response = NextResponse.next()

      if (isAllowedOrigin) {
        response.headers.set('Access-Control-Allow-Origin', origin)
      }

      Object.entries(corsOptions).forEach(([key, value]) => {
        response.headers.set(key, value)
      })

      return response
    }

    export const config = {
      matcher: '/api/:path*',
    }
```

### 응답 생성[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#producing-a-response)

Proxy에서 `Response` 또는 `NextResponse` 인스턴스를 반환하여 직접 응답할 수 있습니다( [Next.js v13.1.0](https://nextjs.org/blog/next-13-1#nextjs-advanced-proxy)부터 지원).

proxy.ts

JavaScriptTypeScript
```
    import type { NextRequest } from 'next/server'
    import { isAuthenticated } from '@lib/auth'

    // Limit the proxy to paths starting with `/api/`
    export const config = {
      matcher: '/api/:function*',
    }

    export function proxy(request: NextRequest) {
      // Call our authentication function to check the request
      if (!isAuthenticated(request)) {
        // Respond with JSON indicating an error message
        return Response.json(
          { success: false, message: 'authentication failed' },
          { status: 401 }
        )
      }
    }
```

### 부정 매칭[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#negative-matching)

`matcher` 설정은 전체 정규식을 지원하므로 부정형 전방 탐색이나 문자 매칭 같은 패턴을 사용할 수 있습니다. 특정 경로를 제외한 모든 경로를 매칭하는 부정 전방 탐색 예시는 다음과 같습니다.

proxy.js
```
    export const config = {
      matcher: [
        /*
         * Match all request paths except for the ones starting with:
         * - api (API routes)
         * - _next/static (static files)
         * - _next/image (image optimization files)
         * - favicon.ico, sitemap.xml, robots.txt (metadata files)
         */
        '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
      ],
    }
```

또한 `missing` 또는 `has` 배열(또는 둘의 조합)을 사용하여 특정 요청에 대해 Proxy를 건너뛸 수도 있습니다.

proxy.js
```
    export const config = {
      matcher: [
        /*
         * Match all request paths except for the ones starting with:
         * - api (API routes)
         * - _next/static (static files)
         * - _next/image (static files)
         * - favicon.ico, sitemap.xml, robots.txt (metadata files)
         */
        {
          source:
            '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
          missing: [
            { type: 'header', key: 'next-router-prefetch' },
            { type: 'header', key: 'purpose', value: 'prefetch' },
          ],
        },

        {
          source:
            '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
          has: [
            { type: 'header', key: 'next-router-prefetch' },
            { type: 'header', key: 'purpose', value: 'prefetch' },
          ],
        },

        {
          source:
            '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
          has: [{ type: 'header', key: 'x-present' }],
          missing: [{ type: 'header', key: 'x-missing', value: 'prefetch' }],
        },
      ],
    }
```

> **알아두면 좋아요** :
>
> 부정 매처 패턴에서 `_next/data`를 제외했더라도 Proxy는 여전히 `_next/data` 경로에 대해 실행됩니다. 이는 페이지는 보호하면서 해당 데이터 경로를 보호하지 않아 발생할 수 있는 보안 문제를 방지하기 위한 의도된 동작입니다.

proxy.js
```
    export const config = {
      matcher:
        '/((?!api|_next/data|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
    }

    // Proxy will still run for /_next/data/* routes despite being excluded
```

### `waitUntil` 및 `NextFetchEvent`[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#waituntil-and-nextfetchevent)

`NextFetchEvent` 객체는 기본 [`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent) 객체를 확장하며, [`waitUntil()`](https://developer.mozilla.org/docs/Web/API/ExtendableEvent/waitUntil) 메서드를 포함합니다.

`waitUntil()` 메서드는 프로미스를 인수로 받아 해당 프로미스가 처리될 때까지 Proxy의 생애를 연장합니다. 이는 백그라운드 작업을 수행할 때 유용합니다.

proxy.ts
```
    import { NextResponse } from 'next/server'
    import type { NextFetchEvent, NextRequest } from 'next/server'

    export function proxy(req: NextRequest, event: NextFetchEvent) {
      event.waitUntil(
        fetch('https://my-analytics-platform.com', {
          method: 'POST',
          body: JSON.stringify({ pathname: req.nextUrl.pathname }),
        })
      )

      return NextResponse.next()
    }
```

### 단위 테스트(실험적)[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#unit-testing-experimental)

Next.js 15.1부터 `next/experimental/testing/server` 패키지는 proxy 파일의 단위 테스트를 돕는 유틸리티를 제공합니다. Proxy 단위 테스트는 특정 경로에서만 실행되도록 보장하고, 프로덕션에 도달하기 전에 사용자 정의 라우팅 로직이 예상대로 동작하는지 확인하는 데 도움이 됩니다.

`unstable_doesProxyMatch` 함수는 주어진 URL, 헤더, 쿠키에 대해 proxy가 실행될지 여부를 단언하는 데 사용할 수 있습니다.
```
    import { unstable_doesProxyMatch } from 'next/experimental/testing/server'

    expect(
      unstable_doesProxyMatch({
        config,
        nextConfig,
        url: '/test',
      })
    ).toEqual(false)
```

전체 proxy 함수도 테스트할 수 있습니다.
```
    import { isRewrite, getRewrittenUrl } from 'next/experimental/testing/server'

    const request = new NextRequest('https://nextjs.org/docs')
    const response = await proxy(request)
    expect(isRewrite(response)).toEqual(true)
    expect(getRewrittenUrl(response)).toEqual('https://other-domain.com/docs')
    // getRedirectUrl could also be used if the response were a redirect
```

## 플랫폼 지원[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#platform-support)

Deployment Option| Supported
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific

Next.js를 셀프 호스팅할 때 [Proxy를 구성](https://nextjs.org/docs/app/guides/self-hosting#proxy)하는 방법을 알아보세요.

## Proxy로의 마이그레이션[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#migration-to-proxy)

### 변경 이유[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#why-the-change)

`middleware` 이름을 변경한 이유는 “middleware”라는 용어가 종종 Express.js 미들웨어와 혼동되어 목적을 잘못 해석하게 만들기 때문이다. 또한 Middleware는 기능이 매우 강력해 사용을 부추길 수 있지만, 이 기능은 최후의 수단으로 사용하는 것이 권장된다.

Next.js는 개발자가 Middleware 없이도 목표를 달성할 수 있도록 더 나은 사용성을 갖춘 API를 제공하기 위해 나아가고 있다. 이것이 `middleware`의 이름을 변경한 이유다.

### 왜 "Proxy"[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#why-proxy)

Proxy라는 이름은 Middleware가 수행할 수 있는 일을 명확히 보여 준다. “proxy”라는 용어는 앱 앞에 네트워크 경계가 있음을 암시하며, 이는 Middleware의 동작과 일치한다. 또한 Middleware는 기본적으로 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)에서 실행되어 앱의 리전과 분리된 채 클라이언트에 더 가깝게 동작할 수 있다. 이러한 동작은 “proxy”라는 용어와 더 잘 맞아떨어지고 기능의 목적을 더욱 분명하게 한다.

### 어떻게 마이그레이션하나요?[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#how-to-migrate)

사용자가 다른 선택지가 없을 때를 제외하고는 Middleware에 의존하지 않기를 권장한다. 우리의 목표는 더 나은 사용성을 갖춘 API를 제공해, Middleware 없이도 목표를 달성하도록 돕는 것이다.

“middleware”라는 용어는 종종 Express.js 미들웨어와 혼동되어 오용을 유발할 수 있다. 방향성을 명확히 하기 위해 파일 규칙을 “proxy”로 이름 변경하고 있다. 이는 Middleware에서 멀어지고, 과도하게 혼재된 기능을 분리하며, Proxy의 목적을 명확히 드러낸다는 의미다.

Next.js는 `middleware.ts`에서 `proxy.ts`로 마이그레이션할 수 있는 codemod를 제공한다. 다음 명령으로 마이그레이션을 실행할 수 있다:
```
    npx @next/codemod@canary middleware-to-proxy .
```

이 codemod는 파일과 함수 이름을 `middleware`에서 `proxy`로 변경한다.
```
    // middleware.ts -> proxy.ts

    - export function middleware() {
    + export function proxy() {
```

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#version-history)

Version| Changes
---|---
`v16.0.0`| Middleware가 더 이상 권장되지 않으며 Proxy로 이름이 변경됨
`v15.5.0`| Middleware가 이제 Node.js 런타임을 사용할 수 있음(안정화)
`v15.2.0`| Middleware가 이제 Node.js 런타임을 사용할 수 있음(실험적)
`v13.1.0`| 고급 Middleware 플래그 추가
`v13.0.0`| Middleware가 요청 헤더, 응답 헤더를 수정하고 응답을 전송할 수 있음
`v12.2.0`| Middleware가 안정화됨; [업그레이드 가이드](https://nextjs.org/docs/messages/middleware-upgrade-guide) 참조
`v12.0.9`| Edge Runtime에서 절대 URL을 강제함([PR](https://github.com/vercel/next.js/pull/33410))
`v12.0.0`| Middleware(베타) 추가