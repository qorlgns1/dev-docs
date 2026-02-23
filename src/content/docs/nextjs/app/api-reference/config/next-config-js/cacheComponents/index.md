---
title: 'next.config.js: cacheComponents'
description: '플래그는 Next.js App Router에서 데이터 가져오기 작업이 명시적으로 캐시되지 않는 한 사전 렌더링에서 제외되도록 만드는 기능입니다. 이는 서버 컴포넌트에서 동적 데이터 가져오기 성능을 최적화하는 데 유용합니다.'
---

# next.config.js: cacheComponents | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)cacheComponents

페이지 복사

# cacheComponents

최종 업데이트 2026년 2월 20일

`cacheComponents` 플래그는 Next.js App Router에서 데이터 가져오기 작업이 명시적으로 캐시되지 않는 한 사전 렌더링에서 제외되도록 만드는 기능입니다. 이는 서버 컴포넌트에서 동적 데이터 가져오기 성능을 최적화하는 데 유용합니다.

애플리케이션이 사전 렌더링된 캐시가 아닌 런타임 동안 최신 데이터를 가져와야 할 때 유용합니다.

페이지, 함수, 컴포넌트 수준에서 `use cache`로 애플리케이션의 특정 부분을 캐시하도록 정의하지 않는 한 기본적으로 데이터 가져오기가 런타임에 수행되도록 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)와 함께 사용하는 것이 예상됩니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#usage)

`cacheComponents` 플래그를 활성화하려면 `next.config.ts` 파일에서 값을 `true`로 설정합니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      cacheComponents: true,
    }
     
    export default nextConfig
[/code]

`cacheComponents`를 활성화하면 다음 캐시 함수와 구성을 사용할 수 있습니다:

  * [`use cache` 지시문](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  * `use cache`와 함께 사용하는 [`cacheLife` 함수](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
  * [`cacheTag` 함수](https://nextjs.org/docs/app/api-reference/functions/cacheTag)



## 참고[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#notes)

  * `cacheComponents`는 런타임 동안 최신 데이터 가져오기를 보장해 성능을 최적화할 수 있지만, 사전 렌더링된 콘텐츠를 제공하는 것보다 지연 시간이 늘어날 수 있습니다.



## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#version-history)

Version| Change  
---|---  
16.0.0| `cacheComponents` 도입. 이 플래그는 `ppr`, `useCache`, `dynamicIO` 플래그를 단일 통합 구성으로 제어합니다.  
  
도움이 되었나요?

지원됨.

보내기
