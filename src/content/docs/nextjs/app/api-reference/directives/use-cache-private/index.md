---
title: '지시문: use cache: private'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션에서 권장되지 않습니다. 시도해 본 뒤 GitHub에서 의견을 공유해주세요.'
---

# 지시문: use cache: private | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/directives/use-cache-private

[API 참고](https://nextjs.org/docs/app/api-reference)[지시문](https://nextjs.org/docs/app/api-reference/directives)use cache: private

# use cache: private

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션에서 권장되지 않습니다. 시도해 본 뒤 [GitHub](https://github.com/vercel/next.js/issues)에서 의견을 공유해주세요.

최종 업데이트 2026년 2월 20일

`'use cache: private'` 지시문을 사용하면 캐시된 범위 안에서 `cookies()`, `headers()`, `searchParams` 같은 런타임 요청 API에 접근하는 함수 작성이 가능합니다. 그러나 결과는 **서버에 저장되지 않으며**, 브라우저 메모리에만 캐시되고 페이지 새로고침 시 유지되지 않습니다.

다음과 같은 경우 `'use cache: private'`를 사용하세요:

  * 이미 런타임 데이터를 사용하는 함수를 캐시하고 싶은데, [런타임 접근을 외부로 옮겨 인자를 통해 값을 전달](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data)하도록 리팩터링하기가 현실적이지 않은 경우
  * 규정 준수 요구 사항 때문에 데이터를 일시적으로라도 서버에 저장할 수 없는 경우

이 지시문은 런타임 데이터를 읽으므로 함수는 모든 서버 렌더마다 실행되며 [static shell](https://nextjs.org/docs/app/getting-started/cache-components#how-rendering-works-with-cache-components) 생성 시에는 제외됩니다.

`'use cache: private'`에는 사용자 정의 캐시 핸들러를 구성할 수 없습니다.

여러 캐시 지시문을 비교하려면 [How `use cache: remote` differs from `use cache` and `use cache: private`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#how-use-cache-remote-differs-from-use-cache-and-use-cache-private)를 참고하세요.

> **알아두면 좋아요**: 이 지시문은 런타임 프리페칭에 의존하기 때문에 `experimental`로 표시되어 있습니다. 런타임 프리페칭은 [static shell](https://nextjs.org/docs/app/getting-started/cache-components#how-rendering-works-with-cache-components)을 넘어 **모든** 캐시 범위(프라이빗 캐시만이 아님)까지 라우터가 프리페치할 수 있게 해 줄 예정이지만 아직 안정화되지 않았습니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#usage)

`'use cache: private'`를 사용하려면 `next.config.ts` 파일에서 [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 플래그를 활성화하세요:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
    }

    export default nextConfig
```

그런 다음 `'use cache: private'`를 함수에 추가하고 `cacheLife` 구성을 함께 정의하세요.

> **알아두면 좋아요**: 이 지시문은 Route Handlers에서 사용할 수 없습니다.

### 기본 예제[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#basic-example)

다음 예시는 `'use cache: private'` 범위 내에서 cookies에 접근할 수 있음을 보여줍니다:

app/product/[id]/page.tsx

JavaScriptTypeScript
```
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
    import { cacheLife, cacheTag } from 'next/cache'

    export async function generateStaticParams() {
      return [{ id: '1' }]
    }

    export default async function ProductPage({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params

      return (
        <div>
          <ProductDetails id={id} />
          <Suspense fallback={<div>Loading recommendations...</div>}>
            <Recommendations productId={id} />
          </Suspense>
        </div>
      )
    }

    async function Recommendations({ productId }: { productId: string }) {
      const recommendations = await getRecommendations(productId)

      return (
        <div>
          {recommendations.map((rec) => (
            <ProductCard key={rec.id} product={rec} />
          ))}
        </div>
      )
    }

    async function getRecommendations(productId: string) {
      'use cache: private'
      cacheTag(`recommendations-${productId}`)
      cacheLife({ stale: 60 })

      // Access cookies within private cache functions
      const sessionId = (await cookies()).get('session-id')?.value || 'guest'

      return getPersonalizedRecommendations(productId, sessionId)
    }
```

> **알아두면 좋아요**: 런타임 프리페칭이 동작하려면 `stale` 시간은 최소 30초여야 합니다. 자세한 내용은 [`cacheLife` client router cache behavior](https://nextjs.org/docs/app/api-reference/functions/cacheLife#client-router-cache-behavior)를 참고하세요.

## 프라이빗 캐시에서 허용되는 Request API[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#request-apis-allowed-in-private-caches)

`'use cache: private'` 함수 안에서는 다음과 같은 요청 전용 API를 사용할 수 있습니다:

API|`use cache`에서 허용 여부|`'use cache: private'`에서 허용 여부
---|---|---
`cookies()`| No| Yes
`headers()`| No| Yes
`searchParams`| No| Yes
`connection()`| No| No

> **참고:** [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) API는 연결별 정보를 제공하므로 `use cache`와 `'use cache: private'` 모두에서 금지됩니다. 해당 정보는 안전하게 캐시할 수 없습니다.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#version-history)

버전|변경 사항
---|---
`v16.0.0`| `"use cache: private"`가 Cache Components 기능과 함께 활성화됩니다.

## 관련 항목

관련 API 참조를 확인하세요.

- [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  - Next.js 애플리케이션에서 "use cache" 지시문으로 데이터를 캐시하는 방법을 알아보세요.
- [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Next.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.
- [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  - 캐시된 함수나 컴포넌트의 만료 시간을 설정하기 위해 cacheLife 함수를 사용하는 방법을 알아보세요.
- [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
  - Next.js 애플리케이션에서 cacheTag 함수를 사용해 캐시 무효화를 관리하는 방법을 알아보세요.

보내기.