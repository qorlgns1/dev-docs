---
title: '파일 시스템 규칙: Route Segment Config'
description: '>   *  플래그가 켜져 있으면 이 페이지에 설명된 옵션은 비활성화되며, 향후 더 이상 지원되지 않습니다.'
---

# 파일 시스템 규칙: Route Segment Config | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config

[API 참조](https://nextjs.org/docs/app/api-reference) [파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions) Route Segment Config

# 라우트 세그먼트 구성(Route Segment Config)

최종 업데이트 2026년 2월 20일

> **알아두면 좋아요** :
>
>   * [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 플래그가 켜져 있으면 이 페이지에 설명된 옵션은 비활성화되며, 향후 더 이상 지원되지 않습니다.
>   * 라우트 세그먼트 옵션은 서버 컴포넌트 페이지, 레이아웃, 또는 라우트 핸들러에서만 적용됩니다.
>   * `generateStaticParams`는 `'use client'` 파일 안에서 사용할 수 없습니다.
>

라우트 세그먼트 옵션을 사용하면 다음 변수를 직접 export하여 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout), 또는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)의 동작을 설정할 수 있습니다:

옵션| 유형| 기본값
---|---|---
[`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)| `'auto' | 'force-dynamic' | 'error' | 'force-static'`| `'auto'`
[`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)| `boolean`| `true`
[`revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate)| `false | 0 | number`| `false`
[`fetchCache`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache)| `'auto' | 'default-cache' | 'only-cache' | 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'`| `'auto'`
[`runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime)| `'nodejs' | 'edge'`| `'nodejs'`
[`preferredRegion`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#preferredregion)| `'auto' | 'global' | 'home' | string | string[]`| `'auto'`
[`maxDuration`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration)| `number`| 배포 플랫폼에서 설정

## 옵션[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#options)

### `dynamic`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)

레이아웃이나 페이지의 동적 동작을 완전 정적 혹은 완전 동적으로 전환합니다.

layout.tsx | page.tsx | route.ts

JavaScript / TypeScript
[code]
    export const dynamic = 'auto'
    // 'auto' | 'force-dynamic' | 'error' | 'force-static'
[/code]

> **알아두면 좋아요** : `app` 디렉터리의 새 모델은 `pages` 디렉터리의 `getServerSideProps`, `getStaticProps`가 제공하던 이진 전부-또는-없음 방식 대신 `fetch` 요청 단위의 세분화된 캐싱 제어를 선호합니다. `dynamic` 옵션은 이전 모델로 다시 전환할 수 있는 편의 기능이자 더 단순한 마이그레이션 경로를 제공합니다.

  * **`'auto'`** (기본): 가능한 한 많이 캐시하되, 어떤 컴포넌트도 동적 동작을 선택하는 것을 막지 않는 기본 옵션입니다.

  * **`'force-dynamic'`** : [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)을 강제하여 각 사용자의 요청 시점에 라우트를 렌더링합니다. 이 옵션은 다음과 동일합니다:

    * 레이아웃이나 페이지의 모든 `fetch()` 요청 옵션을 `{ cache: 'no-store', next: { revalidate: 0 } }`로 설정합니다.
    * 세그먼트 구성을 `export const fetchCache = 'force-no-store'`로 설정합니다.
  * **`'error'`** : 레이아웃이나 페이지에서 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) 또는 캐시되지 않은 데이터를 사용하면 오류를 발생시켜 정적 렌더링과 데이터 캐싱을 강제합니다. 이 옵션은 다음과 동일합니다:

    * `pages` 디렉터리의 `getStaticProps()`.
    * 레이아웃이나 페이지의 모든 `fetch()` 요청 옵션을 `{ cache: 'force-cache' }`로 설정.
    * 세그먼트 구성을 `fetchCache = 'only-cache'`로 설정.
  * **`'force-static'`** : [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers), [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)를 비어 있는 값으로 강제하여 레이아웃이나 페이지의 정적 렌더링과 데이터 캐싱을 보장합니다. `force-static`으로 렌더링된 페이지나 레이아웃에서도 [`revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate), [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath), [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용할 수 있습니다.

> **알아두면 좋아요** :
>
>   * `getServerSideProps`, `getStaticProps`에서 `dynamic: 'force-dynamic'`, `dynamic: 'error'`로 [마이그레이션하는 방법](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)은 [업그레이드 가이드](https://nextjs.org/docs/app/guides/migrating/app-router-migration#step-6-migrating-data-fetching-methods)에서 확인하세요.
>

### `dynamicParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)

[generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)로 생성되지 않은 동적 세그먼트가 방문되었을 때의 동작을 제어합니다.

layout.tsx | page.tsx

JavaScript / TypeScript
[code]
    export const dynamicParams = true // true | false
[/code]

  * **`true`** (기본): `generateStaticParams`에 포함되지 않은 동적 세그먼트를 요청 시점에 생성합니다.
  * **`false`** : `generateStaticParams`에 포함되지 않은 동적 세그먼트는 404를 반환합니다.

> **알아두면 좋아요** :
>
>   * 이 옵션은 `pages` 디렉터리의 `getStaticPaths`가 갖던 `fallback: true | false | blocking` 옵션을 대체합니다.
>   * 처음 방문할 때 모든 경로를 정적으로 렌더링하려면 `generateStaticParams`에서 빈 배열을 반환하거나 `export const dynamic = 'force-static'`을 사용하세요.
>   * `dynamicParams = true`이면 해당 세그먼트는 [스트리밍 서버 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 사용합니다.
>

### `revalidate`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate)

레이아웃이나 페이지의 기본 재검증 시간을 설정합니다. 이 옵션은 개별 `fetch` 요청에서 지정한 `revalidate` 값을 덮어쓰지 않습니다.

layout.tsx | page.tsx | route.ts

JavaScript / TypeScript
[code]
    export const revalidate = false
    // false | 0 | number
[/code]

  * **`false`** (기본): `cache` 옵션을 `'force-cache'`로 설정하거나 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)가 사용되기 전에 탐지된 `fetch` 요청을 캐시하는 기본 추론입니다. 의미상 `revalidate: Infinity`와 같으며, 자원은 사실상 무기한 캐시됩니다. 그래도 개별 `fetch` 요청에서 `cache: 'no-store'` 또는 `revalidate: 0`을 사용해 캐시를 피하고 라우트를 동적으로 렌더링할 수 있습니다. 혹은 라우트 기본값보다 낮은 양수로 `revalidate`를 설정해 재검증 빈도를 높일 수도 있습니다.
  * **`0`** : Dynamic API나 캐시되지 않은 데이터 페치가 없더라도 레이아웃이나 페이지를 항상 [동적으로 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)하게 만듭니다. 이 옵션은 `cache` 옵션을 지정하지 않은 `fetch` 요청의 기본값을 `'no-store'`로 변경하지만, `'force-cache'`를 선택했거나 양수 `revalidate`를 지정한 `fetch` 요청은 그대로 유지합니다.
  * **`number`** : (초 단위) 레이아웃이나 페이지의 기본 재검증 주기를 `n`초로 설정합니다.

> **알아두면 좋아요** :
>
>   * `revalidate` 값은 정적으로 해석 가능해야 합니다. 예를 들어 `revalidate = 600`은 유효하지만 `revalidate = 60 * 10`은 허용되지 않습니다.
>   * `runtime = 'edge'`를 사용할 때는 `revalidate` 값을 사용할 수 없습니다.
>   * 개발 환경에서는 페이지가 항상 필요 시 렌더링되며 캐시되지 않습니다. 따라서 재검증 주기를 기다리지 않고도 변경 사항을 즉시 확인할 수 있습니다.
>

#### 재검증 빈도[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidation-frequency)

  * 하나의 라우트에 속한 각 레이아웃과 페이지의 `revalidate` 값 중 가장 낮은 값이 라우트 전체의 재검증 빈도를 결정합니다. 이를 통해 자식 페이지가 부모 레이아웃만큼 자주 재검증되도록 보장합니다.
  * 개별 `fetch` 요청이 라우트 기본 `revalidate`보다 낮은 값을 설정하면 라우트 전체의 재검증 빈도를 높일 수 있습니다. 이를 통해 특정 기준에 따라 더 자주 재검증해야 하는 라우트만 동적으로 선택할 수 있습니다.

### `fetchCache`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache)

기본 동작을 반드시 재정의해야 할 때만 사용하는 고급 옵션입니다.

기본적으로 Next.js는 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)가 사용되기 **전**에 도달 가능한 `fetch()` 요청은 **캐시**하고, Dynamic API가 사용된 **후**에 발견된 `fetch` 요청은 캐시하지 **않습니다**.

`fetchCache`는 레이아웃이나 페이지의 모든 `fetch` 요청에 대해 기본 `cache` 옵션을 재정의합니다.

layout.tsx | page.tsx | route.ts

JavaScript / TypeScript
[code]
    export const fetchCache = 'auto'
    // 'auto' | 'default-cache' | 'only-cache'
    // 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'
[/code]

  * **`'auto'`** (기본): Dynamic API 이전의 `fetch` 요청을 각각이 제공한 `cache` 옵션대로 캐시하고, Dynamic API 이후의 `fetch` 요청은 캐시하지 않는 기본 옵션입니다.
  * **`'default-cache'`** : `fetch`에 어떤 `cache` 옵션이든 전달할 수 있지만, 옵션이 없으면 `cache`를 `'force-cache'`로 설정합니다. 따라서 Dynamic API 이후의 `fetch` 요청도 정적으로 간주됩니다.
  * **`'only-cache'`** : 기본값을 `cache: 'force-cache'`로 변경해 모든 `fetch` 요청이 캐싱을 선택하도록 하며, `cache: 'no-store'`를 사용하는 `fetch` 요청이 있으면 오류를 발생시킵니다.
  * **`'force-cache'`** : 모든 `fetch` 요청의 `cache` 옵션을 `'force-cache'`로 설정하여 캐싱을 강제합니다.
  * **`'default-no-store'`** : `fetch`에 어떤 `cache` 옵션이든 전달할 수 있지만, 옵션이 없으면 `cache`를 `'no-store'`로 설정합니다. 따라서 Dynamic API 이전의 `fetch` 요청도 동적으로 간주됩니다.
  * **`'only-no-store'`** : 기본값을 `cache: 'no-store'`로 변경해 모든 `fetch` 요청이 캐싱을 거부하도록 하며, `cache: 'force-cache'`를 사용하는 `fetch` 요청이 있으면 오류를 발생시킵니다.
  * **`'force-no-store'`** : 모든 `fetch` 요청의 `cache` 옵션을 `'no-store'`로 설정해 캐싱 거부를 강제합니다. `fetch` 요청에서 `'force-cache'` 옵션을 제공하더라도 매 요청마다 다시 가져오게 됩니다.

#### 라우트 간 세그먼트 동작[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#cross-route-segment-behavior)

  * 하나의 라우트에 속한 각 레이아웃과 페이지에서 설정하는 옵션은 서로 호환되어야 합니다.
    * `'only-cache'`와 `'force-cache'`가 모두 지정되면 `'force-cache'`가 우선합니다. `'only-no-store'`와 `'force-no-store'`가 모두 지정되면 `'force-no-store'`가 우선합니다. `'force-*'` 옵션은 라우트 전체의 동작을 변경하므로, 단일 세그먼트에서 `'force-*'`를 사용하면 `'only-*'` 때문에 발생할 수 있는 오류를 방지합니다.

* `'only-*'`와 `'force-*'` 옵션의 의도는 전체 라우트가 완전히 정적이거나 완전히 동적임을 보장하는 것입니다. 즉:
      * 하나의 라우트에서 `'only-cache'`와 `'only-no-store'`를 함께 사용할 수 없습니다.
      * 하나의 라우트에서 `'force-cache'`와 `'force-no-store'`를 함께 사용할 수 없습니다.
    * 자식이 `'auto'` 또는 `'*-cache'`를 제공하는 경우, 부모는 동일한 fetch에서 서로 다른 동작이 발생할 수 있으므로 `'default-no-store'`를 제공할 수 없습니다.
  * 일반적으로 공유 부모 레이아웃은 `'auto'`로 유지하고, 자식 세그먼트마다 옵션이 달라지는 지점에서 커스터마이즈하는 것이 좋습니다.

### `runtime`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime)

애플리케이션 렌더링에는 Node.js 런타임 사용을 권장합니다. 이 옵션은 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 사용할 수 없습니다.

> **알아두면 좋은 점** : `runtime: 'edge'`는 Cache Components에서 **지원되지 않습니다**.

layout.tsx | page.tsx | route.ts

JavaScriptTypeScript
[code]
    export const runtime = 'nodejs'
    // 'nodejs' | 'edge'
[/code]

  * **`'nodejs'`** (기본값)
  * **`'edge'`**

### `preferredRegion`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#preferredregion)

layout.tsx | page.tsx | route.ts

JavaScriptTypeScript
[code]
    export const preferredRegion = 'auto'
    // 'auto' | 'global' | 'home' | ['iad1', 'sfo1']
[/code]

`preferredRegion` 지원 여부와 사용 가능한 리전은 배포 플랫폼에 따라 달라집니다.

> **알아두면 좋은 점** :
>
>   * `preferredRegion`을 지정하지 않으면 가장 가까운 부모 레이아웃의 옵션을 상속합니다.
>   * 루트 레이아웃은 기본적으로 `all` 리전을 사용합니다.
>

### `maxDuration`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration)

기본적으로 Next.js는 서버 사이드 로직(페이지 렌더링 또는 API 처리)의 실행 시간을 제한하지 않습니다. 배포 플랫폼은 Next.js 빌드 출력의 `maxDuration`을 사용해 특정 실행 제한을 추가할 수 있습니다.

**참고** : 이 설정은 Next.js `13.4.10` 이상에서 필요합니다.

layout.tsx | page.tsx | route.ts

JavaScriptTypeScript
[code]
    export const maxDuration = 5
[/code]

> **알아두면 좋은 점** :
>
>   * [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)을 사용하는 경우, 페이지 수준에서 `maxDuration`을 설정하면 해당 페이지에서 사용되는 모든 Server Actions의 기본 타임아웃을 변경할 수 있습니다.
>

### `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#generatestaticparams)

`generateStaticParams` 함수는 [동적 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)와 함께 사용하여 요청 시점이 아닌 빌드 시점에 정적으로 생성될 라우트 세그먼트 파라미터 목록을 정의할 수 있습니다.

자세한 내용은 [API 참고 문서](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 확인하세요.

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#version-history)

Version|
---|---
`v16.0.0`| `export const experimental_ppr = true`가 제거되었습니다. [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts)를 사용할 수 있습니다.
`v15.0.0-RC`| `export const runtime = "experimental-edge"`가 더 이상 권장되지 않습니다. [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge)를 사용할 수 있습니다.

보내기
