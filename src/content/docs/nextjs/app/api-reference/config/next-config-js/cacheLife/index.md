---
title: 'next.config.js: cacheLife'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife'
---

# next.config.js: cacheLife | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife

# cacheLife

최종 업데이트 2026년 2월 20일

`cacheLife` 옵션은 컴포넌트나 함수 내부에서 [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) 함수를 사용할 때, 그리고 [`use cache` 지시자](https://nextjs.org/docs/app/api-reference/directives/use-cache)의 범위 내에서 **사용자 정의 캐시 프로필**을 정의할 수 있게 해줍니다.

## 사용 방법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#usage)

프로필을 정의하려면 [`cacheComponents` 플래그](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)를 활성화하고, `next.config.js` 파일의 `cacheLife` 객체에 캐시 프로필을 추가하세요. 예를 들어 `blog` 프로필은 다음과 같습니다:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
      cacheLife: {
        blog: {
          stale: 3600, // 1 hour
          revalidate: 900, // 15 minutes
          expire: 86400, // 1 day
        },
      },
    }

    export default nextConfig
[/code]

이제 컴포넌트나 함수에서 아래와 같이 사용자 정의 `blog` 구성을 사용할 수 있습니다:

app/actions.ts

JavaScriptTypeScript
[code]
    import { cacheLife } from 'next/cache'

    export async function getCachedData() {
      'use cache'
      cacheLife('blog')
      const data = await fetch('/api/data')
      return data
    }
[/code]

## 참고[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#reference)

구성 객체에는 다음 형식의 키 값이 포함됩니다:

**속성**| **값**| **설명**| **요구 사항**
---|---|---|---
`stale`| `number`| 클라이언트가 서버 확인 없이 값을 캐시해야 하는 기간.| 선택
`revalidate`| `number`| 캐시가 서버에서 새로 고쳐야 하는 빈도로, 재검증 중에는 오래된 값이 제공될 수 있습니다.| 선택
`expire`| `number`| 값을 동적 모드로 전환하기 전에 오래된 상태로 유지할 수 있는 최대 기간으로, `revalidate`보다 길어야 합니다.| 선택 - `revalidate`보다 길어야 함

## 관련 항목

관련 API 레퍼런스를 확인하세요.

- [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  - Next.js 애플리케이션에서 데이터를 캐시하기 위한 "use cache" 지시자를 사용하는 방법을 알아보세요.

- [cacheHandlers](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)
  - Next.js에서 use cache 지시자에 사용할 사용자 정의 캐시 핸들러를 구성하세요.

- [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  - 캐시된 함수나 컴포넌트의 캐시 만료 시간을 설정하기 위해 cacheLife 함수를 사용하는 방법을 알아보세요.

보내기
