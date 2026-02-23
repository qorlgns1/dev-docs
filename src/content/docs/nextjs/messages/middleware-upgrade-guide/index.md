---
title: '미들웨어 업그레이드 가이드'
description: 'Middleware를 GA(General Availability)로 개선하는 과정에서, 여러분의 피드백을 바탕으로 Middleware API(및 애플리케이션에서 Middleware를 정의하는 방식)에 몇 가지 변경을 적용했습니다.'
---

# 미들웨어 업그레이드 가이드 | Next.js

Source URL: https://nextjs.org/docs/messages/middleware-upgrade-guide

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)Middleware Upgrade Guide

# 미들웨어 업그레이드 가이드

Middleware를 GA(General Availability)로 개선하는 과정에서, 여러분의 피드백을 바탕으로 Middleware API(및 애플리케이션에서 Middleware를 정의하는 방식)에 몇 가지 변경을 적용했습니다.

이 업그레이드 가이드는 변경 사항과 그 이유를 이해하고, 기존 Middleware를 새로운 API로 마이그레이션하는 방법을 설명합니다. 이 가이드는 다음과 같은 Next.js 개발자를 위한 것입니다.

  * 현재 베타 Next.js Middleware 기능을 사용 중인 경우
  * 다음 안정 버전의 Next.js(`v12.2`)로 업그레이드하려는 경우

최신 릴리스(`npm i next@latest`)로 지금 바로 Middleware 사용을 업그레이드할 수 있습니다.

> **참고**: 본 가이드에 설명된 변경 사항은 Next.js `12.2`에 포함되어 있습니다. `12.2`(또는 Next.js의 `canary` 빌드)로 이동하기 전까지는 중첩 Middleware를 포함한 현재 사이트 구조를 유지할 수 있습니다.

ESLint를 구성했다면 Next.js 버전과 동일한 버전이 사용되도록 ESLint 구성을 업그레이드하기 위해 `npm i eslint-config-next@latest --save-dev`를 실행해야 합니다. 변경 사항이 반영되려면 VSCode를 재시작해야 할 수도 있습니다.

## Vercel에서 Next.js Middleware 사용하기[](https://nextjs.org/docs/messages/middleware-upgrade-guide#using-nextjs-middleware-on-vercel)

Vercel에서 Next.js를 사용 중이라면, Middleware를 사용하는 기존 배포는 계속 동작하며 Middleware를 사용한 사이트 배포도 이어갈 수 있습니다. 사이트를 다음 안정 버전의 Next.js(`v12.2`)로 업그레이드할 때는 이 업그레이드 가이드를 따라 Middleware를 업데이트해야 합니다.

## 하위 호환성 파괴 변경 사항[](https://nextjs.org/docs/messages/middleware-upgrade-guide#breaking-changes)

  1. [중첩된 Middleware 없음](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-nested-middleware)
  2. [응답 본문 제거](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)
  3. [Cookies API 개편](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)
  4. [새 User-Agent 헬퍼](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)
  5. [페이지 매치 데이터 제거](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)
  6. [내부 Next.js 요청에서 Middleware 실행](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)

## 중첩된 Middleware 없음[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-nested-middleware)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes)

  * `pages` 폴더 옆에 단일 Middleware 파일을 정의합니다.
  * 파일 이름 앞에 밑줄을 붙일 필요가 없습니다.
  * 내보낸 config 객체로 커스텀 matcher를 정의해 라우트를 지정할 수 있습니다.

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation)

기존에는 `pages` 디렉터리의 어느 레벨에서든 `_middleware.ts` 파일을 만들 수 있었으며, Middleware 실행은 파일이 위치한 경로를 기준으로 결정되었습니다.

고객 피드백을 반영해 API를 단일 루트 Middleware로 교체했고, 이를 통해 다음과 같은 개선이 이루어졌습니다.

  * **더 빠른 실행과 낮은 지연 시간**: 중첩 Middleware에서는 하나의 요청이 여러 Middleware 함수를 호출할 수 있었습니다. 단일 Middleware는 단일 함수 실행만 이루어져 더 효율적입니다.
  * **비용 절감**: Middleware 사용량은 호출당 과금됩니다. 중첩 Middleware에서는 하나의 요청이 여러 Middleware 함수를 호출하여 요청당 여러 번 과금될 수 있었습니다. 단일 Middleware는 요청당 한 번만 호출되어 비용 효율적입니다.
  * **라우트 외 조건에도 쉽게 필터링 가능**: 중첩 Middleware에서는 `pages` 디렉터리에 파일이 위치해 요청 경로 기반으로만 실행되었습니다. 단일 루트 Middleware로 전환하면 여전히 경로 기반 실행이 가능하면서도 `cookies`나 요청 헤더 존재 여부 같은 다른 조건에 따라 더욱 편리하게 실행할 수 있습니다.
  * **결정적인 실행 순서**: 중첩 Middleware에서는 하나의 요청이 여러 Middleware에 매칭될 수 있어 실행 순서를 파악하기 어려웠습니다. 예를 들어 `/dashboard/users/*` 요청은 `/dashboard/users/_middleware.ts`와 `/dashboard/_middleware.js`에 모두 매칭되었습니다. 단일 루트 Middleware는 실행 순서를 명확하게 정의합니다.
  * **Next.js Layouts(RFC) 지원**: 단일 루트 Middleware는 Next.js의 새로운 [Layouts(RFC)](https://nextjs.org/blog/layouts-rfc)를 지원하는 데 도움이 됩니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade)

애플리케이션에는 **단 하나의 Middleware 파일**만 선언해야 하며, 이 파일은 `pages` 디렉터리 옆에 위치하고 이름에 `_` 접두사를 붙이지 않아야 합니다. Middleware 파일 확장자는 `.ts` 또는 `.js` 중 하나를 사용할 수 있습니다.

Middleware는 **앱의 모든 라우트**에 대해 호출되며, 커스텀 matcher를 사용해 매칭 필터를 정의할 수 있습니다. 아래는 `/about/*` 및 `/dashboard/:path*`에서 작동하는 Middleware 예시로, 커스텀 matcher는 내보낸 config 객체에 정의되어 있습니다.

middleware.ts
```
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'

    export function middleware(request: NextRequest) {
      return NextResponse.rewrite(new URL('/about-2', request.url))
    }

    // Supports both a single string value or an array of matchers
    export const config = {
      matcher: ['/about/:path*', '/dashboard/:path*'],
    }
```

matcher config는 전체 정규식을 지원하므로 부정형 전방 탐색이나 문자 매칭 등도 사용할 수 있습니다. 특정 경로를 제외한 모든 경로를 매칭하는 부정형 전방 탐색 예시는 다음과 같습니다.

middleware.ts
```
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
```

config 옵션은 모든 요청마다 호출되지 않으므로 권장되지만, 조건문을 사용해 특정 경로에만 Middleware를 실행할 수도 있습니다. 조건문을 사용하면 Middleware 실행 순서를 명시적으로 정의할 수 있다는 장점이 있습니다. 다음 예시는 이전의 중첩 Middleware 두 개를 통합하는 방법을 보여 줍니다.

middleware.ts
```
    import type { NextRequest } from 'next/server'

    export function middleware(request: NextRequest) {
      if (request.nextUrl.pathname.startsWith('/about')) {
        // This logic is only applied to /about
      }

      if (request.nextUrl.pathname.startsWith('/dashboard')) {
        // This logic is only applied to /dashboard
      }
    }
```

## 응답 본문 없음[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-1)

  * Middleware는 더 이상 응답 본문을 생성할 수 없습니다.
  * Middleware가 본문으로 응답하면 런타임 오류가 발생합니다.
  * 응답을 처리하는 페이지/API로 `rewrite`/`redirect`를 사용하도록 마이그레이션하세요.

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-1)

클라이언트 및 서버 내비게이션의 차이를 존중하고, 개발자가 보안에 취약한 Middleware를 만들지 않도록 하기 위해 Middleware에서 응답 본문을 전송하는 기능을 제거했습니다. 이제 Middleware는 `rewrite`, `redirect` 또는 들어오는 요청 수정(예: [쿠키 설정](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped))에만 사용됩니다.

다음 패턴은 더 이상 동작하지 않습니다.
```
    new Response('a text value')
    new Response(streamOrBuffer)
    new Response(JSON.stringify(obj), { headers: 'application/json' })
    NextResponse.json()
```

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-1)

권한 부여처럼 Middleware로 응답을 반환하던 경우, 권한 오류 페이지나 로그인 폼 또는 API Route로 `rewrite`/`redirect`하도록 마이그레이션해야 합니다.

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before)

pages/_middleware.ts
```
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
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after)

middleware.ts
```
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
```

#### Edge API Routes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#edge-api-routes)

이전에 Middleware를 사용해 외부 API로 헤더를 전달했다면 이제 [Edge API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)를 사용할 수 있습니다.

pages/api/proxy.ts
```
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
```

## Cookies API 개편[](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-2)

추가됨|제거됨
---|---
`cookies.set`|`cookie`
`cookies.delete`|`clearCookie`
`cookies.getWithOptions`|`cookies`

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-2)

베타 피드백을 바탕으로 `NextRequest`와 `NextResponse`의 Cookies API를 `get`/`set` 모델에 가깝게 변경했습니다. `Cookies` API는 Map을 확장하며 [entries](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries), [values](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map/entries) 같은 메서드를 포함합니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-2)

`NextResponse`에는 다음을 포함한 `cookies` 인스턴스가 새로 제공됩니다.

  * `cookies.delete`
  * `cookies.set`
  * `cookies.getWithOptions`

이외에도 `Map`에서 확장된 다른 메서드를 제공합니다.

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-1)

pages/_middleware.ts
```
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
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-1)

middleware.ts
```
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
```

## 새 User-Agent 헬퍼[](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-3)

  * 요청 객체에서 user agent에 접근할 수 없습니다.
  * Middleware 크기를 `17kb` 줄이기 위해 새로운 `userAgent` 헬퍼를 추가했습니다.

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-3)

Middleware 크기를 줄이기 위해 요청 객체에서 user agent를 분리하고 새로운 `userAgent` 헬퍼를 만들었습니다.

이 헬퍼는 `next/server`에서 import하며, user agent를 사용하도록 선택할 수 있게 해줍니다. 헬퍼는 기존에 요청 객체에서 사용할 수 있던 것과 동일한 속성에 접근할 수 있습니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-3)

  * `next/server`에서 `userAgent` 헬퍼를 import합니다.
  * 필요한 속성을 구조 분해 할당하여 사용합니다.

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-2)

pages/_middleware.ts
```
    import { NextRequest, NextResponse } from 'next/server'

    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const viewport = request.ua.device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-2)

middleware.ts
```
    import { NextRequest, NextResponse, userAgent } from 'next/server'

    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const { device } = userAgent(request)
      const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
```

## 페이지 매치 데이터 없음[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-4)

  * 특정 페이지 매치에서 Middleware가 호출되었는지 확인하려면 [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)을 사용하세요.

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-4)

현재 Middleware는 Next.js 라우트 매니페스트(내부 설정)를 기반으로 페이지 자산을 제공하는지 추정하며, 이 값은 `request.page`를 통해 노출됩니다.

페이지 및 자산 매칭 정확도를 높이기 위해 이제 웹 표준 `URLPattern` API를 사용합니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-4)

[`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)을 사용해 특정 페이지 매치에서 Middleware가 호출되었는지 확인하세요.

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-3)

pages/_middleware.ts
```
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
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-3)

middleware.ts
```
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
```

## 내부 Next.js 요청에서 Middleware 실행[](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-5)

  * `_next`를 포함한 **모든** 요청에 대해 Middleware가 실행됩니다.

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-5)

Next.js `v12.2` 이전에는 `_next` 요청에 대해 Middleware가 실행되지 않았습니다.

Middleware를 권한 부여에 사용하는 경우, 권한 오류 페이지나 로그인 폼 또는 API Route로 `rewrite`/`redirect`하도록 마이그레이션해야 합니다.

마이그레이션 예시는 [응답 본문 없음](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)을 참고하세요.

보내기

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

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-1)

middleware.ts
```
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
```

## 새로운 User-Agent Helper[](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-3)

  * 요청 객체에서 사용자 에이전트에 접근할 수 없습니다
  * `userAgent` 헬퍼를 추가하여 Middleware 크기를 `17kb` 줄였습니다

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-3)

Middleware 크기를 줄이기 위해 요청 객체에서 사용자 에이전트를 분리하고 새로운 헬퍼 `userAgent`를 만들었습니다.

이 헬퍼는 `next/server`에서 임포트하며, 사용자 에이전트 사용 시 명시적으로 opt-in 할 수 있습니다. 요청 객체에서 사용할 수 있었던 동일한 속성에 접근할 수 있습니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-3)

  * `next/server`에서 `userAgent` 헬퍼를 임포트합니다
  * 작업에 필요한 속성을 구조 분해 할당합니다

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-2)

pages/_middleware.ts
```
    import { NextRequest, NextResponse } from 'next/server'

    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const viewport = request.ua.device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-2)

middleware.ts
```
    import { NextRequest, NextResponse, userAgent } from 'next/server'

    export function middleware(request: NextRequest) {
      const url = request.nextUrl
      const { device } = userAgent(request)
      const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
```

## 페이지 매치 데이터 삭제[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-4)

  * 특정 페이지 매치를 위한 Middleware 호출 여부를 확인하려면 [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)을 사용합니다

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-4)

현재 Middleware는 Next.js 경로 매니페스트(내부 구성)를 기반으로 페이지의 에셋을 제공하는지 추정합니다. 이 값은 `request.page`를 통해 공개됩니다.

페이지와 에셋 매칭을 더욱 정확하게 하기 위해 이제 웹 표준 `URLPattern` API를 사용합니다.

### 업그레이드 방법[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-4)

[`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)을 사용해 Middleware가 특정 페이지 매치에 대해 호출되고 있는지 확인하세요.

#### 이전[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-3)

pages/_middleware.ts
```
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
```

#### 이후[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-3)

middleware.ts
```
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
```

## 내부 Next.js 요청에서 Middleware 실행[](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)

### 변경 사항 요약[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-5)

  * Middleware는 `_next`를 포함한 모든 요청에 대해 실행됩니다

### 설명[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-5)

Next.js `v12.2` 이전에는 `_next` 요청에 대해 Middleware가 실행되지 않았습니다.

Middleware를 인증 용도로 사용하는 경우, 권한 오류를 보여주는 페이지, 로그인 폼, 또는 API Route로 `rewrite`/`redirect`를 사용하도록 마이그레이션해야 합니다.

`rewrite`/`redirect`로 마이그레이션하는 예시는 [No Response Body](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)를 참조하세요.

보내기