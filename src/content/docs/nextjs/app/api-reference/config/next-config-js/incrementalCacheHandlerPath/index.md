---
title: 'next.config.js: cacheHandler'
description: '캐시된 페이지와 데이터를 영구 스토리지에 보존하거나 Next.js 애플리케이션의 여러 컨테이너·인스턴스 간에 캐시를 공유하려면 Next.js 캐시 위치를 구성할 수 있습니다.'
---

# next.config.js: cacheHandler | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)cacheHandler

페이지 복사

# 맞춤 Next.js 캐시 핸들러

최종 업데이트 2026년 2월 20일

캐시된 페이지와 데이터를 영구 스토리지에 보존하거나 Next.js 애플리케이션의 여러 컨테이너·인스턴스 간에 캐시를 공유하려면 Next.js 캐시 위치를 구성할 수 있습니다.

> **알아두면 좋아요**: `cacheHandler`(단수) 구성은 ISR 및 라우트 핸들러 응답을 저장하고 재검증하는 등 서버 캐시 작업에 대해 Next.js가 사용하는 항목입니다. `'use cache'` 지시문에는 **사용되지 않으며**, 해당 지시문에는 [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)(복수)를 사용하세요.

next.config.js
[code]
    module.exports = {
      cacheHandler: require.resolve('./cache-handler.js'),
      cacheMaxMemorySize: 0, // disable default in-memory caching
    }
[/code]

[맞춤 캐시 핸들러](https://nextjs.org/docs/app/guides/self-hosting#configuring-caching) 예제를 보고 구현 방식에 대해 더 알아보세요.

## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#api-reference)

캐시 핸들러는 `get`, `set`, `revalidateTag`, `resetRequestCache` 메서드를 구현할 수 있습니다.

### `get()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#get)

매개변수| 타입| 설명  
---|---|---  
`key`| `string`| 캐시된 값을 찾을 키.  
  
캐시된 값을 반환하며 없으면 `null`을 반환합니다.

### `set()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#set)

매개변수| 타입| 설명  
---|---|---  
`key`| `string`| 데이터를 저장할 키.  
`data`| Data 또는 `null`| 캐시할 데이터.  
`ctx`| `{ tags: [] }`| 제공된 캐시 태그.  
  
`Promise<void>`를 반환합니다.

### `revalidateTag()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#revalidatetag)

매개변수| 타입| 설명  
---|---|---  
`tag`| `string` 또는 `string[]`| 재검증할 캐시 태그.  
  
`Promise<void>`를 반환합니다. [데이터 재검증](https://nextjs.org/docs/app/guides/incremental-static-regeneration) 또는 [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) 함수에 대해 더 알아보세요.

### `resetRequestCache()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#resetrequestcache)

이 메서드는 다음 요청 전 단일 요청을 위한 임시 메모리 캐시를 재설정합니다.

`void`를 반환합니다.

**알아두면 좋아요:**

  * `revalidatePath`는 캐시 태그 위에 얹힌 편의 계층입니다. `revalidatePath`를 호출하면 `revalidateTag` 함수가 호출되며, 이후 경로 기반으로 캐시 키에 태그를 달지 결정할 수 있습니다.



## Platform Support[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#platform-support)

배포 옵션| 지원 여부  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 예  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| 예  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 아니요  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별  
  
Next.js를 자체 호스팅할 때 [ISR 구성](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr) 방법을 알아보세요.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#version-history)

버전| 변경 사항  
---|---  
`v14.1.0`| `cacheHandler`로 이름이 변경되어 안정화됨.  
`v13.4.0`| `revalidateTag`에 대한 `incrementalCacheHandlerPath` 지원.  
`v13.4.0`| 스탠드얼론 출력에 대한 `incrementalCacheHandlerPath` 지원.  
`v12.2.0`| 실험적 `incrementalCacheHandlerPath` 추가.  
  
도움이 되었나요?

지원됨.

보내기
