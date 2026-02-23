---
title: '함수: NextResponse'
description: 'NextResponse는 Web Response API를 확장해 추가적인 편의 메서드를 제공합니다.'
---

# 함수: NextResponse | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/functions/next-response

[API 참조](https://nextjs.org/docs/app/api-reference)[함수](https://nextjs.org/docs/app/api-reference/functions)NextResponse

페이지 복사

# NextResponse

마지막 업데이트 2026년 2월 20일

NextResponse는 [Web Response API](https://developer.mozilla.org/docs/Web/API/Response)를 확장해 추가적인 편의 메서드를 제공합니다.

## `cookies`[](https://nextjs.org/docs/app/api-reference/functions/next-response#cookies)

응답의 [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) 헤더를 읽거나 변경합니다.

### `set(name, value)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#setname-value)

이름이 주어지면, 지정한 값을 가진 쿠키를 응답에 설정합니다.
[code] 
    // Given incoming request /home
    let response = NextResponse.next()
    // Set a cookie to hide the banner
    response.cookies.set('show-banner', 'false')
    // Response will have a `Set-Cookie:show-banner=false;path=/home` header
    return response
[/code]

### `get(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#getname)

쿠키 이름을 주면 해당 쿠키의 값을 반환합니다. 쿠키가 없으면 `undefined`를 반환하며, 여러 개면 첫 번째 쿠키를 반환합니다.
[code] 
    // Given incoming request /home
    let response = NextResponse.next()
    // { name: 'show-banner', value: 'false', Path: '/home' }
    response.cookies.get('show-banner')
[/code]

### `getAll()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#getall)

쿠키 이름을 주면 해당 쿠키의 모든 값을 반환합니다. 이름을 생략하면 응답의 모든 쿠키를 반환합니다.
[code] 
    // Given incoming request /home
    let response = NextResponse.next()
    // [
    //   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
    //   { name: 'experiments', value: 'winter-launch', Path: '/home' },
    // ]
    response.cookies.getAll('experiments')
    // Alternatively, get all cookies for the response
    response.cookies.getAll()
[/code]

### `has(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#hasname)

쿠키 이름을 주면 응답에 해당 쿠키가 존재하면 `true`를 반환합니다.
[code] 
    // Given incoming request /home
    let response = NextResponse.next()
    // Returns true if cookie exists, false if it does not
    response.cookies.has('experiments')
[/code]

### `delete(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#deletename)

쿠키 이름을 주면 응답에서 해당 쿠키를 삭제합니다.
[code] 
    // Given incoming request /home
    let response = NextResponse.next()
    // Returns true for deleted, false if nothing is deleted
    response.cookies.delete('experiments')
[/code]

## `json()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#json)

주어진 JSON 본문으로 응답을 생성합니다.

app/api/route.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
     
    export async function GET(request: Request) {
      return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
    }
[/code]

## `redirect()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#redirect)

[URL](https://developer.mozilla.org/docs/Web/API/URL)로 리디렉션하는 응답을 생성합니다.
[code] 
    import { NextResponse } from 'next/server'
     
    return NextResponse.redirect(new URL('/new', request.url))
[/code]

[URL](https://developer.mozilla.org/docs/Web/API/URL)은 `NextResponse.redirect()` 메서드에서 사용하기 전에 생성하고 수정할 수 있습니다. 예를 들어 `request.nextUrl` 속성으로 현재 URL을 가져온 뒤 수정해 다른 URL로 리디렉션할 수 있습니다.
[code] 
    import { NextResponse } from 'next/server'
     
    // Given an incoming request...
    const loginUrl = new URL('/login', request.url)
    // Add ?from=/incoming-url to the /login URL
    loginUrl.searchParams.set('from', request.nextUrl.pathname)
    // And redirect to the new URL
    return NextResponse.redirect(loginUrl)
[/code]

## `rewrite()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#rewrite)

원래 URL을 유지한 채 지정된 [URL](https://developer.mozilla.org/docs/Web/API/URL)을 재작성(프록시)하는 응답을 생성합니다.
[code] 
    import { NextResponse } from 'next/server'
     
    // Incoming request: /about, browser shows /about
    // Rewritten request: /proxy, browser shows /about
    return NextResponse.rewrite(new URL('/proxy', request.url))
[/code]

## `next()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#next)

`next()` 메서드는 프록시에서 유용하며, 빠르게 반환하고 라우팅을 이어갈 수 있게 해줍니다.
[code] 
    import { NextResponse } from 'next/server'
     
    return NextResponse.next()
[/code]

`NextResponse.next({ request: { headers } })`를 사용하면 응답을 생성할 때 `headers`를 업스트림으로 전달할 수 있습니다:
[code] 
    import { NextResponse } from 'next/server'
     
    // Given an incoming request...
    const newHeaders = new Headers(request.headers)
    // Add a new header
    newHeaders.set('x-version', '123')
    // Forward the modified request headers upstream
    return NextResponse.next({
      request: {
        // New request headers
        headers: newHeaders,
      },
    })
[/code]

이 방식은 `newHeaders`를 대상 페이지·라우트·서버 액션으로 전달하며, 클라이언트에는 노출하지 않습니다. 이렇게 데이터를 업스트림으로 전달할 때 유용하지만, 해당 데이터를 포함한 헤더가 외부 서비스로 전달될 수 있으므로 주의해서 사용해야 합니다.

반대로 `NextResponse.next({ headers })`는 프록시에서 클라이언트로 헤더를 보내는 축약형입니다. 이는 **좋은 방식이 아니며** 피해야 합니다. 예를 들어 `Content-Type`과 같은 응답 헤더를 설정하면 프레임워크가 기대하는 값(예: Server Actions에서 사용하는 `Content-Type`)을 덮어써 제출 실패나 스트리밍 응답 깨짐을 유발할 수 있습니다.
[code] 
    import { type NextRequest, NextResponse } from 'next/server'
     
    async function proxy(request: NextRequest) {
      const headers = await injectAuth(request.headers)
      // DO NOT forward headers like this
      return NextResponse.next({ headers })
    }
[/code]

일반적으로 모든 수신 요청 헤더를 복사하는 것은 클라이언트나 업스트림 서비스에 민감한 데이터를 누출할 수 있으므로 피해야 합니다.

허용 목록을 사용해 들어오는 요청 헤더의 하위 집합을 만들어 전달하는 방어적인 접근을 권장합니다. 예를 들어, 사용자 정의 `x-*` 헤더를 버리고 안전한 헤더만 전달할 수 있습니다:
[code] 
    import { type NextRequest, NextResponse } from 'next/server'
     
    function proxy(request: NextRequest) {
      const incoming = new Headers(request.headers)
      const forwarded = new Headers()
     
      for (const [name, value] of incoming) {
        const headerName = name.toLowerCase()
        // Keep only known-safe headers, discard custom x-* and other sensitive ones
        if (
          !headerName.startsWith('x-') &&
          headerName !== 'authorization' &&
          headerName !== 'cookie'
        ) {
          // Preserve original header name casing
          forwarded.set(name, value)
        }
      }
     
      return NextResponse.next({
        request: {
          headers: forwarded,
        },
      })
    }
[/code]

도움이 되었나요?

지원됨.

전송
