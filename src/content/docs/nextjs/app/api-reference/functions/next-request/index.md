---
title: '함수: NextRequest'
description: 'NextRequest는 추가 편의 메서드를 제공하기 위해 Web Request API를 확장합니다.'
---

# 함수: NextRequest | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/next-request

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)NextRequest

Copy page

# NextRequest

마지막 업데이트: 2026년 2월 20일

NextRequest는 추가 편의 메서드를 제공하기 위해 [Web Request API](https://developer.mozilla.org/docs/Web/API/Request)를 확장합니다.

## `cookies`[](https://nextjs.org/docs/app/api-reference/functions/next-request#cookies)

요청의 [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) 헤더를 읽거나 변경합니다.

### `set(name, value)`[](https://nextjs.org/docs/app/api-reference/functions/next-request#setname-value)

이름을 전달하면 해당 값을 가진 쿠키를 요청에 설정합니다.
[code] 
    // Given incoming request /home
    // Set a cookie to hide the banner
    // request will have a `Set-Cookie:show-banner=false;path=/home` header
    request.cookies.set('show-banner', 'false')
[/code]

### `get(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-request#getname)

쿠키 이름을 전달하면 해당 쿠키 값을 반환합니다. 쿠키가 없으면 `undefined`를 반환합니다. 여러 쿠키가 있으면 첫 번째 쿠키를 반환합니다.
[code] 
    // Given incoming request /home
    // { name: 'show-banner', value: 'false', Path: '/home' }
    request.cookies.get('show-banner')
[/code]

### `getAll()`[](https://nextjs.org/docs/app/api-reference/functions/next-request#getall)

쿠키 이름을 전달하면 해당 쿠키의 모든 값을 반환합니다. 이름이 없으면 요청의 모든 쿠키를 반환합니다.
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

### `delete(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-request#deletename)

쿠키 이름을 전달하면 요청에서 해당 쿠키를 삭제합니다.
[code] 
    // Returns true for deleted, false is nothing is deleted
    request.cookies.delete('experiments')
[/code]

### `has(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-request#hasname)

쿠키 이름을 전달하면 요청에 쿠키가 존재하면 `true`를 반환합니다.
[code] 
    // Returns true if cookie exists, false if it does not
    request.cookies.has('experiments')
[/code]

### `clear()`[](https://nextjs.org/docs/app/api-reference/functions/next-request#clear)

요청에서 모든 쿠키를 제거합니다.
[code] 
    request.cookies.clear()
[/code]

## `nextUrl`[](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl)

Next.js 전용 속성을 포함해 네이티브 [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API를 확장하는 추가 편의 메서드를 제공합니다.
[code] 
    // Given a request to /home, pathname is /home
    request.nextUrl.pathname
    // Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
    request.nextUrl.searchParams
[/code]

사용 가능한 옵션은 다음과 같습니다:

Property| Type| Description  
---|---|---  
`basePath`| `string`| URL의 [base path](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath).  
`buildId`| `string` | `undefined`| Next.js 애플리케이션의 빌드 식별자입니다. [커스터마이징](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)이 가능합니다.  
`pathname`| `string`| URL의 pathname입니다.  
`searchParams`| `Object`| URL의 검색 매개변수입니다.  
  
> **참고:** Pages Router의 국제화 속성은 App Router에서 사용할 수 없습니다. [App Router 국제화](https://nextjs.org/docs/app/guides/internationalization)에 대해 더 알아보세요.

## Version History[](https://nextjs.org/docs/app/api-reference/functions/next-request#version-history)

Version| Changes  
---|---  
`v15.0.0`| `ip` 및 `geo`가 제거되었습니다.  
  
Was this helpful?

supported.

Send
