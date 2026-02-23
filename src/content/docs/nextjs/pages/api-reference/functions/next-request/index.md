---
title: '함수: NextRequest'
description: 'NextRequest는 Web Request API를 확장하여 추가 편의 메서드를 제공합니다.'
---

# 함수: NextRequest | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/functions/next-request

[API 레퍼런스](https://nextjs.org/docs/pages/api-reference)[함수](https://nextjs.org/docs/pages/api-reference/functions)NextRequest

페이지 복사

# NextRequest

마지막 업데이트 2026년 2월 20일

NextRequest는 [Web Request API](https://developer.mozilla.org/docs/Web/API/Request)를 확장하여 추가 편의 메서드를 제공합니다.

## `cookies`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#cookies)

요청의 [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) 헤더를 읽거나 변경합니다.

### `set(name, value)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#setname-value)

이름을 지정하면 해당 값의 쿠키를 요청에 설정합니다.
[code] 
    // Given incoming request /home
    // Set a cookie to hide the banner
    // request will have a `Set-Cookie:show-banner=false;path=/home` header
    request.cookies.set('show-banner', 'false')
[/code]

### `get(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getname)

쿠키 이름을 지정하면 해당 쿠키의 값을 반환합니다. 쿠키가 없으면 `undefined`가 반환되고, 여러 쿠키가 있으면 첫 번째 쿠키가 반환됩니다.
[code] 
    // Given incoming request /home
    // { name: 'show-banner', value: 'false', Path: '/home' }
    request.cookies.get('show-banner')
[/code]

### `getAll()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getall)

쿠키 이름을 지정하면 해당 쿠키의 모든 값을 반환합니다. 이름을 지정하지 않으면 요청에 있는 모든 쿠키를 반환합니다.
[code] 
    // Given incoming request /home
    // [
    //   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
    //   { name: 'experiments', value: 'winter-launch', Path: '/home' },
    // ]
    request.cookies.getAll('experiments')
    // Alternatively, get all cookies for the request
    request.cookies.getAll()
[/code]

### `delete(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#deletename)

쿠키 이름을 지정하면 해당 쿠키를 요청에서 삭제합니다.
[code] 
    // Returns true for deleted, false is nothing is deleted
    request.cookies.delete('experiments')
[/code]

### `has(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#hasname)

쿠키 이름을 지정하면 해당 쿠키가 요청에 존재하면 `true`를 반환합니다.
[code] 
    // Returns true if cookie exists, false if it does not
    request.cookies.has('experiments')
[/code]

### `clear()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#clear)

요청에서 모든 쿠키를 제거합니다.
[code] 
    request.cookies.clear()
[/code]

## `nextUrl`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#nexturl)

네이티브 [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API를 확장하여 Next.js 전용 속성을 포함한 추가 편의 메서드를 제공합니다.
[code] 
    // Given a request to /home, pathname is /home
    request.nextUrl.pathname
    // Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
    request.nextUrl.searchParams
[/code]

사용 가능한 옵션은 다음과 같습니다:

Property| Type| Description  
---|---|---  
`basePath`| `string`| URL의 [기본 경로](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)입니다.  
`buildId`| `string` | `undefined`| Next.js 애플리케이션의 빌드 식별자입니다. [커스터마이즈](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)할 수 있습니다.  
`defaultLocale`| `string` | `undefined`| [국제화](https://nextjs.org/docs/pages/guides/internationalization)를 위한 기본 로케일입니다.  
`domainLocale`| |   
\- `defaultLocale`| `string`| 도메인 내 기본 로케일입니다.  
\- `domain`| `string`| 특정 로케일과 연결된 도메인입니다.  
\- `http`| `boolean` | `undefined`| 해당 도메인이 HTTP를 사용하는지 나타냅니다.  
`locales`| `string[]` | `undefined`| 사용 가능한 로케일 배열입니다.  
`locale`| `string` | `undefined`| 현재 활성 로케일입니다.  
`url`| `URL`| URL 객체입니다.  
  
## 버전 기록[](https://nextjs.org/docs/pages/api-reference/functions/next-request#version-history)

Version| Changes  
---|---  
`v15.0.0`| `ip` 및 `geo`가 제거되었습니다.  
  
도움이 되었나요?

지원됨.

전송
