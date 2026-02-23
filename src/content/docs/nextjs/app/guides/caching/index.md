---
title: '가이드: 캐싱'
description: 'Next.js는 렌더링 작업과 데이터 요청을 캐싱해 애플리케이션 성능을 향상시키고 비용을 절감합니다. 이 페이지에서는 Next.js 캐싱 메커니즘, 이를 구성할 수 있는 API, 그리고 서로 간의 상호 작용을 심층적으로 살펴봅니다.'
---

# 가이드: 캐싱 | Next.js

Source URL: https://nextjs.org/docs/app/guides/caching

Copy page

# Next.js의 캐싱

최종 업데이트 2026년 2월 20일

Next.js는 렌더링 작업과 데이터 요청을 캐싱해 애플리케이션 성능을 향상시키고 비용을 절감합니다. 이 페이지에서는 Next.js 캐싱 메커니즘, 이를 구성할 수 있는 API, 그리고 서로 간의 상호 작용을 심층적으로 살펴봅니다.

> **알아두면 좋아요**: 이 페이지는 Next.js의 내부 동작을 이해하는 데 도움을 주지만, Next.js를 생산적으로 사용하는 데 필수 지식은 아닙니다. Next.js의 대부분 캐싱 휴리스틱은 API 사용 방식에 의해 결정되며, 최소 구성으로도 최고의 성능을 내도록 기본값이 설정되어 있습니다. 예제를 바로 보고 싶다면 [여기서 시작하세요](https://nextjs.org/docs/app/getting-started/fetching-data).

## 개요[](https://nextjs.org/docs/app/guides/caching#overview)

아래는 주요 캐싱 메커니즘과 목적에 대한 상위 수준 요약입니다:

Mechanism| What| Where| Purpose| Duration
---|---|---|---|---
[Request Memoization](https://nextjs.org/docs/app/guides/caching#request-memoization)| 함수 반환 값| 서버| React 컴포넌트 트리에서 데이터 재사용| 요청별 라이프사이클
[Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)| 데이터| 서버| 사용자 요청과 배포 간 데이터 저장| 지속(재검증 가능)
[Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache)| HTML 및 RSC 페이로드| 서버| 렌더링 비용 절감 및 성능 향상| 지속(재검증 가능)
[Router Cache](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)| RSC 페이로드| 클라이언트| 탐색 시 서버 요청 감소| 사용자 세션 또는 시간 기반

기본적으로 Next.js는 성능을 높이고 비용을 줄이기 위해 가능한 많은 것을 캐싱합니다. 즉, 경로는 **정적으로 렌더링**되고 데이터 요청은 **캐싱**되며, 명시적으로 제외하지 않는 한 그렇습니다. 아래 다이어그램은 기본 캐싱 동작을 보여줍니다. 이는 경로가 빌드 시점에 정적으로 렌더링될 때와 정적 경로를 처음 방문할 때를 나타냅니다.

캐싱 동작은 경로가 정적 또는 동적으로 렌더링되는지, 데이터가 캐시되는지 여부, 그리고 요청이 초기 방문인지 후속 탐색인지에 따라 달라집니다. 사용 사례에 따라 개별 경로와 데이터 요청의 캐싱 동작을 구성할 수 있습니다.

`proxy`에서는 fetch 캐싱이 **지원되지 않습니다**. `proxy` 내부에서 수행되는 모든 fetch는 캐시되지 않습니다.

## 렌더링 전략[](https://nextjs.org/docs/app/guides/caching#rendering-strategies)

Next.js에서 캐싱이 어떻게 동작하는지 이해하려면 사용 가능한 렌더링 전략을 이해하는 것이 도움이 됩니다. 렌더링 전략은 경로의 HTML이 생성되는 시점을 결정하며, 이는 무엇을 캐싱할 수 있는지에 직접적인 영향을 줍니다.

### 정적 렌더링[](https://nextjs.org/docs/app/guides/caching#static-rendering)

정적 렌더링에서는 경로가 **빌드 시점** 또는 [데이터 재검증](https://nextjs.org/docs/app/guides/incremental-static-regeneration) 이후 백그라운드에서 렌더링됩니다. 결과는 캐시되며 요청 간 재사용할 수 있습니다. 정적 경로는 [Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache)에 완전히 저장됩니다.

### 동적 렌더링[](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)

동적 렌더링에서는 경로가 **요청 시점**에 렌더링됩니다. 경로가 쿠키, 헤더, 검색 매개변수 같은 요청별 정보를 사용할 때 발생합니다.

경로가 다음 API 중 하나를 사용하면 동적으로 전환됩니다:

  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)
  * [`unstable_noStore`](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)
  * `{ cache: 'no-store' }` 옵션의 [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch)

동적 경로는 Full Route Cache에 캐시되지 않지만, 데이터 요청에 대해서는 [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)를 사용할 수 있습니다.

> **알아두면 좋아요**: 동일한 경로 내에서 정적 렌더링과 동적 렌더링을 혼합하려면 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 수 있습니다.

## Request Memoization[](https://nextjs.org/docs/app/guides/caching#request-memoization)

Next.js는 [`fetch` API](https://nextjs.org/docs/app/guides/caching#fetch)를 확장해 동일한 URL과 옵션을 가진 요청을 자동으로 **메모이즈**합니다. 즉, React 컴포넌트 트리의 여러 위치에서 동일한 데이터를 가져와도 실제 호출은 한 번만 실행됩니다.

예를 들어, 경로 전체(레이아웃, 페이지, 다수의 컴포넌트 등)에서 동일한 데이터를 사용해야 한다면 트리 최상단에서 데이터를 가져와 컴포넌트 간 props로 전달할 필요가 없습니다. 대신 필요한 컴포넌트 내에서 데이터를 fetch하면서, 동일한 데이터를 위해 네트워크 요청을 여러 번 보내야 할 성능 영향을 걱정하지 않아도 됩니다.

app/example.tsx

JavaScriptTypeScript
```
    async function getItem() {
      // The `fetch` function is automatically memoized and the result
      // is cached
      const res = await fetch('https://.../item/1')
      return res.json()
    }

    // This function is called twice, but only executed the first time
    const item = await getItem() // cache MISS

    // The second call could be anywhere in your route
    const item = await getItem() // cache HIT
```

**Request Memoization 동작 방식**

  * 경로를 렌더링하는 동안 특정 요청이 처음 호출되면 메모리에 결과가 없어 캐시 `MISS`가 됩니다.
  * 함수가 실행되어 외부 소스에서 데이터를 가져오고, 결과는 메모리에 저장됩니다.
  * 동일 렌더링 패스에서 해당 요청이 다시 호출되면 캐시 `HIT`가 되어, 함수를 다시 실행하지 않고 메모리에서 데이터를 반환합니다.
  * 경로가 렌더링되고 렌더링 패스가 완료되면 메모리가 "리셋"되며 모든 request memoization 항목이 지워집니다.

> **알아두면 좋아요**:
>
>   * Request memoization은 Next.js 기능이 아닌 React 기능입니다. 다른 캐싱 메커니즘과의 상호 작용을 설명하기 위해 포함되었습니다.
>   * 메모이제이션은 `fetch` 요청의 `GET` 메서드에만 적용됩니다.
>   * 메모이제이션은 React 컴포넌트 트리에만 적용됩니다. 즉:
>     * `generateMetadata`, `generateStaticParams`, 레이아웃, 페이지, 기타 서버 컴포넌트의 `fetch` 요청에는 적용됩니다.
>     * React 컴포넌트 트리의 일부가 아닌 Route Handler의 `fetch` 요청에는 적용되지 않습니다.
>   * `fetch`가 적합하지 않은 경우(예: 일부 데이터베이스 클라이언트, CMS 클라이언트, GraphQL 클라이언트) [React `cache` 함수](https://nextjs.org/docs/app/guides/caching#react-cache-function)로 함수를 메모이즈할 수 있습니다.
>

### 지속 시간[](https://nextjs.org/docs/app/guides/caching#duration)

캐시는 서버 요청의 수명 동안 유지되며 React 컴포넌트 트리 렌더링이 끝나면 만료됩니다.

### 재검증[](https://nextjs.org/docs/app/guides/caching#revalidating)

메모이제이션은 서버 요청 간 공유되지 않고 렌더링 중에만 적용되므로 재검증할 필요가 없습니다.

### 옵트아웃[](https://nextjs.org/docs/app/guides/caching#opting-out)

메모이제이션은 `fetch` 요청의 `GET` 메서드에만 적용되며, `POST`, `DELETE` 같은 다른 메서드는 메모이즈되지 않습니다. 이 기본 동작은 React 최적화이므로 옵트아웃을 권장하지 않습니다.

개별 요청을 제어하려면 [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)의 [`signal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal) 속성을 사용할 수 있습니다.

app/example.js
```
    const { signal } = new AbortController()
    fetch(url, { signal })
```

## Data Cache[](https://nextjs.org/docs/app/guides/caching#data-cache)

Next.js에는 들어오는 **서버 요청**과 **배포** 전반에 걸쳐 데이터 fetch 결과를 **지속적으로** 저장하는 내장 Data Cache가 있습니다. 이는 Next.js가 서버에서 각 `fetch` 요청이 자체적인 지속 캐싱 의미 체계를 설정하도록 네이티브 `fetch` API를 확장했기 때문에 가능합니다.

> **알아두면 좋아요**: 브라우저에서는 `fetch`의 `cache` 옵션이 브라우저 HTTP 캐시와 상호 작용하는 방식을 나타내지만, Next.js에서는 서버 측 요청이 서버 Data Cache와 상호 작용하는 방식을 의미합니다.

`fetch`의 [`cache`](https://nextjs.org/docs/app/guides/caching#fetch-optionscache) 옵션과 [`next.revalidate`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate) 옵션을 사용해 캐싱 동작을 구성할 수 있습니다.

개발 모드에서는 `fetch` 데이터가 [HMR(Hot Module Replacement)에 재사용](https://nextjs.org/docs/app/api-reference/functions/fetch#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development)되며, [하드 새로고침](https://nextjs.org/docs/app/api-reference/functions/fetch#hard-refresh-and-caching-in-development) 시 캐싱 옵션이 무시됩니다.

**Data Cache 동작 방식**

  * `'force-cache'` 옵션이 있는 `fetch` 요청이 렌더링 중 처음 호출되면 Next.js는 Data Cache에서 캐시된 응답을 확인합니다.
  * 캐시된 응답이 있으면 즉시 반환하고 [memoized](https://nextjs.org/docs/app/guides/caching#request-memoization)됩니다.
  * 캐시된 응답이 없으면 데이터 소스에 요청을 보내고 결과를 Data Cache에 저장한 뒤 메모이즈합니다.
  * 캐시되지 않은 데이터(예: `cache` 옵션이 없거나 `{ cache: 'no-store' }` 사용)는 항상 데이터 소스에서 가져오고, 결과는 메모이즈됩니다.
  * 데이터가 캐시되었든 아니든, 동일한 데이터를 위한 중복 요청을 피하기 위해 요청은 항상 메모이즈됩니다.

> **Data Cache와 Request Memoization 간 차이점**
>
> 두 메커니즘 모두 캐시된 데이터를 재사용해 성능을 높이지만, Data Cache는 들어오는 요청과 배포 전반에 지속되며, 메모이제이션은 단일 요청의 수명 동안만 지속됩니다.

### 지속 시간[](https://nextjs.org/docs/app/guides/caching#duration-1)

Data Cache는 재검증하거나 옵트아웃하지 않는 한 들어오는 요청과 배포 간에 지속됩니다.

### 재검증[](https://nextjs.org/docs/app/guides/caching#revalidating-1)

캐시된 데이터는 두 가지 방식으로 재검증할 수 있습니다:

  * **시간 기반 재검증**: 특정 시간이 경과하고 새 요청이 들어오면 데이터를 다시 검증합니다. 변경이 드물고 신선도가 덜 중요한 데이터에 적합합니다.
  * **온디맨드 재검증**: 이벤트(예: 양식 제출)에 따라 데이터를 재검증합니다. 온디맨드 재검증은 태그 기반 또는 경로 기반 접근으로 데이터 그룹을 한 번에 재검증할 수 있습니다. (예: 헤드리스 CMS 콘텐츠가 업데이트되면) 최신 데이터를 즉시 보여주고 싶을 때 유용합니다.

#### 시간 기반 재검증[](https://nextjs.org/docs/app/guides/caching#time-based-revalidation)

정해진 간격으로 데이터를 재검증하려면 `fetch`의 `next.revalidate` 옵션을 사용해 리소스의 캐시 수명(초)을 설정하세요.
```
    // Revalidate at most every hour
    fetch('https://...', { next: { revalidate: 3600 } })
```

Alternatively, you can use [Route Segment Config options](https://nextjs.org/docs/app/guides/caching#segment-config-options) to configure all `fetch` requests in a segment or for cases where you're not able to use `fetch`.

**시간 기반 재검증 작동 방식**

  * `revalidate`가 포함된 `fetch` 요청이 처음 호출되면 외부 데이터 소스에서 데이터를 가져와 데이터 캐시에 저장합니다.
  * 지정된 기간(예: 60초) 내에 호출되는 모든 요청은 캐싱된 데이터를 반환합니다.
  * 해당 기간이 지나면 다음 요청도 캐시에 있는 (이제는 오래된) 데이터를 반환합니다.
    * Next.js가 백그라운드에서 데이터를 재검증합니다.
    * 데이터가 성공적으로 다시 가져와지면 Next.js가 새 데이터로 데이터 캐시를 업데이트합니다.
    * 백그라운드 재검증이 실패하면 이전 데이터가 그대로 유지됩니다.

이 동작은 [**stale-while-revalidate**](https://web.dev/articles/stale-while-revalidate)와 유사합니다.

#### 온디맨드 재검증[](https://nextjs.org/docs/app/guides/caching#on-demand-revalidation)

데이터는 경로별([`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath)) 또는 캐시 태그별([`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag))로 온디맨드 재검증이 가능합니다.

**온디맨드 재검증 작동 방식**

  * `fetch` 요청이 처음 호출되면 외부 데이터 소스에서 데이터를 가져와 데이터 캐시에 저장합니다.
  * 온디맨드 재검증이 트리거되면 해당 캐시 엔트리가 캐시에서 제거됩니다.
    * 이는 새 데이터를 가져올 때까지 오래된 데이터를 캐시에 유지하는 시간 기반 재검증과 다릅니다.
  * 다음 요청이 들어올 때는 다시 캐시 `MISS`가 발생하고, 데이터가 외부 데이터 소스에서 가져와져 데이터 캐시에 저장됩니다.

### 선택 해제[](https://nextjs.org/docs/app/guides/caching#opting-out-1)

`fetch` 응답을 캐시하지 않으려면 다음과 같이 할 수 있습니다.
```
    let data = await fetch('https://api.vercel.app/blog', { cache: 'no-store' })
```

## Full Route Cache[](https://nextjs.org/docs/app/guides/caching#full-route-cache)

> **관련 용어** :
>
> 빌드 시 애플리케이션의 라우트를 렌더링하고 캐싱하는 프로세스를 지칭할 때 **Automatic Static Optimization**, **Static Site Generation**, **Static Rendering**이라는 용어가 서로 바꿔 사용될 수 있습니다.

Next.js는 빌드 시 라우트를 자동으로 렌더링하고 캐싱합니다. 이렇게 하면 모든 요청마다 서버에서 렌더링하는 대신 캐시된 라우트를 제공하여 페이지 로드 속도가 빨라집니다.

Full Route Cache가 어떻게 작동하는지 이해하려면 React가 렌더링을 처리하는 방식과 Next.js가 그 결과를 어떻게 캐싱하는지 살펴보는 것이 도움이 됩니다.

### 1\. 서버에서의 React 렌더링[](https://nextjs.org/docs/app/guides/caching#1-react-rendering-on-the-server)

서버에서 Next.js는 React API를 사용해 렌더링을 조율합니다. 렌더링 작업은 개별 라우트 세그먼트와 Suspense 경계별로 청크로 나뉩니다.

각 청크는 두 단계로 렌더링됩니다.

  1. React가 서버 컴포넌트를 스트리밍에 최적화된 특별한 데이터 형식인 **React Server Component Payload**로 렌더링합니다.
  2. Next.js는 React Server Component Payload와 클라이언트 컴포넌트 JavaScript 지시문을 사용해 서버에서 **HTML**을 렌더링합니다.

이 덕분에 모든 렌더링이 끝날 때까지 기다리지 않고도 작업을 캐시하거나 응답을 보낼 수 있습니다. 대신 작업이 완료되는 대로 응답을 스트리밍할 수 있습니다.

> **React Server Component Payload란?**
>
> React Server Component Payload는 렌더링된 React 서버 컴포넌트 트리를 압축한 바이너리 표현입니다. React가 클라이언트에서 브라우저 DOM을 업데이트하는 데 사용합니다. React Server Component Payload에는 다음이 포함됩니다.
>
>   * 서버 컴포넌트의 렌더링 결과
>   * 클라이언트 컴포넌트를 렌더링할 위치와 해당 JavaScript 파일에 대한 참조
>   * 서버 컴포넌트에서 클라이언트 컴포넌트로 전달되는 모든 props
>
>
> 더 알아보려면 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 문서를 참고하세요.

### 2\. 서버에서의 Next.js 캐싱 (Full Route Cache)[](https://nextjs.org/docs/app/guides/caching#2-nextjs-caching-on-the-server-full-route-cache)

Next.js의 기본 동작은 라우트의 렌더링 결과(React Server Component Payload와 HTML)를 서버에 캐시하는 것입니다. 이는 빌드 시 정적으로 렌더링된 라우트나 재검증 중에 적용됩니다.

### 3\. 클라이언트에서의 React 하이드레이션과 조정[](https://nextjs.org/docs/app/guides/caching#3-react-hydration-and-reconciliation-on-the-client)

요청 시 클라이언트에서:

  1. HTML은 클라이언트 및 서버 컴포넌트의 빠른 비인터랙티브 초기 미리보기를 즉시 표시하는 데 사용됩니다.
  2. React Server Component Payload는 클라이언트와 렌더링된 서버 컴포넌트 트리를 조정하고 DOM을 업데이트하는 데 사용됩니다.
  3. JavaScript 지시문은 클라이언트 컴포넌트를 [hydrate](https://react.dev/reference/react-dom/client/hydrateRoot)하여 애플리케이션을 인터랙티브하게 만듭니다.

### 4\. 클라이언트에서의 Next.js 캐싱 (Router Cache)[](https://nextjs.org/docs/app/guides/caching#4-nextjs-caching-on-the-client-router-cache)

React Server Component Payload는 개별 라우트 세그먼트별로 분리된 클라이언트 측 [Router Cache](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)에 저장됩니다. 이 Router Cache는 방문한 라우트를 저장하고 향후 라우트를 프리패치하여 네비게이션 경험을 향상합니다.

### 5\. 이후 네비게이션[](https://nextjs.org/docs/app/guides/caching#5-subsequent-navigations)

추가 네비게이션이나 프리패치 시 Next.js는 React Server Component Payload가 Router Cache에 저장되어 있는지 확인합니다. 있다면 서버로 새 요청을 보내지 않습니다.

라우트 세그먼트가 캐시에 없으면 Next.js가 서버에서 React Server Component Payload를 가져와 클라이언트의 Router Cache를 채웁니다.

### 정적 렌더링과 동적 렌더링[](https://nextjs.org/docs/app/guides/caching#static-and-dynamic-rendering)

라우트가 빌드 시 캐시되는지 여부는 정적으로 렌더링되는지 동적으로 렌더링되는지에 따라 달라집니다. 정적 라우트는 기본적으로 캐시되며, 동적 라우트는 요청 시 렌더링되고 캐시되지 않습니다.

아래 다이어그램은 캐시된 데이터와 캐시되지 않은 데이터를 포함해 정적 렌더링과 동적 렌더링 라우트의 차이를 보여줍니다.

[정적 및 동적 렌더링](https://nextjs.org/docs/app/guides/caching#rendering-strategies)에 대해 더 알아보세요.

### 지속 기간[](https://nextjs.org/docs/app/guides/caching#duration-2)

기본적으로 Full Route Cache는 지속됩니다. 즉, 렌더링 결과가 사용자 요청 간에 캐시됩니다.

### 무효화[](https://nextjs.org/docs/app/guides/caching#invalidation)

Full Route Cache를 무효화하는 방법은 두 가지입니다.

  * **[데이터 재검증](https://nextjs.org/docs/app/guides/caching#revalidating)** : [데이터 캐시](https://nextjs.org/docs/app/guides/caching#data-cache)를 재검증하면 서버에서 컴포넌트를 다시 렌더링하고 새로운 렌더링 결과를 캐시하여 Router Cache도 무효화합니다.
  * **재배포** : 배포 간에 지속되는 데이터 캐시와 달리, Full Route Cache는 새 배포 시 지워집니다.

### 선택 해제[](https://nextjs.org/docs/app/guides/caching#opting-out-2)

Full Route Cache를 선택 해제하거나, 즉 들어오는 모든 요청마다 컴포넌트를 동적으로 렌더링하려면 다음을 수행하세요.

  * **[Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)를 사용**: 라우트를 Full Route Cache에서 제외하고 요청 시 동적으로 렌더링합니다. 데이터 캐시는 계속 사용할 수 있습니다.
  * **`dynamic = 'force-dynamic'` 또는 `revalidate = 0` 라우트 세그먼트 설정 옵션 사용**: Full Route Cache와 데이터 캐시를 건너뜁니다. 즉, 서버로 들어오는 모든 요청에 대해 컴포넌트를 렌더링하고 데이터를 가져옵니다. Router Cache는 클라이언트 측 캐시이므로 계속 적용됩니다.
  * **[데이터 캐시](https://nextjs.org/docs/app/guides/caching#data-cache) 선택 해제**: 라우트에 캐시되지 않는 `fetch` 요청이 있으면 해당 라우트는 Full Route Cache에서 제외됩니다. 해당 `fetch` 요청의 데이터는 들어오는 모든 요청마다 가져옵니다. 캐싱을 명시적으로 활성화한 다른 `fetch` 요청은 계속 데이터 캐시에 저장됩니다. 이를 통해 캐시된 데이터와 캐시되지 않은 데이터를 혼합할 수 있습니다.

## Client-side Router Cache[](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)

Next.js에는 레이아웃, 로딩 상태, 페이지별로 분리된 라우트 세그먼트의 RSC 페이로드를 저장하는 인메모리 클라이언트 측 Router Cache가 있습니다.

사용자가 라우트 간을 이동하면 Next.js는 방문한 라우트 세그먼트를 캐시하고 사용자가 이동할 가능성이 있는 라우트를 [prefetches](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)합니다. 이를 통해 즉각적인 뒤로/앞으로 이동, 네비게이션 간 전체 페이지 재로드 없음, 공유 레이아웃에서 브라우저 상태와 React 상태 보존이 가능합니다.

Router Cache가 제공하는 것:

  * **레이아웃**은 네비게이션 시 캐시되고 재사용됩니다([부분 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)).
  * **로딩 상태**는 [instant navigation](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states)을 위해 네비게이션 시 캐시되고 재사용됩니다.
  * **페이지**는 기본적으로 캐시되지 않지만 브라우저 뒤로/앞으로 이동 동안 재사용됩니다. 실험적 [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) 설정 옵션을 사용해 페이지 세그먼트 캐싱을 활성화할 수 있습니다.

> **알아두면 좋은 점:** 이 캐시는 Next.js와 서버 컴포넌트에만 적용되며, 브라우저의 [bfcache](https://web.dev/bfcache/)와는 다르지만 유사한 결과를 제공합니다.

### 지속 기간[](https://nextjs.org/docs/app/guides/caching#duration-3)

캐시는 브라우저의 임시 메모리에 저장됩니다. Router Cache의 지속 시간은 두 가지 요인에 의해 결정됩니다.

  * **세션** : 네비게이션 전반에 걸쳐 캐시가 유지되지만, 페이지를 새로고침하면 지워집니다.
  * **자동 무효화 기간** : 레이아웃과 로딩 상태의 캐시는 특정 시간이 지나면 자동으로 무효화됩니다. 기간은 리소스를 어떻게 [prefetched](https://nextjs.org/docs/app/api-reference/components/link#prefetch)했는지, 그리고 리소스가 [정적으로 생성](https://nextjs.org/docs/app/guides/caching#static-rendering)되었는지에 따라 달라집니다.
    * **기본 프리패칭**(`prefetch={null}` 또는 미지정): 동적 페이지는 캐시되지 않고, 정적 페이지는 5분 동안 캐시됩니다.
    * **완전 프리패칭**(`prefetch={true}` 또는 `router.prefetch`): 정적 및 동적 페이지 모두 5분 동안 캐시됩니다.

페이지를 새로고침하면 **모든** 캐시된 세그먼트가 지워지지만, 자동 무효화 기간은 프리패치된 시점부터 해당 세그먼트에만 적용됩니다.

> **알아두면 좋은 점** : 실험적 [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) 설정 옵션을 사용해 위에서 언급한 자동 무효화 시간을 조정할 수 있습니다.

### 무효화[](https://nextjs.org/docs/app/guides/caching#invalidation-1)

Router Cache를 무효화하는 방법은 두 가지입니다.

  * **서버 액션**에서:
    * 경로별 온디맨드 데이터 재검증([`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)) 또는 캐시 태그별 재검증([`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag))

* [`cookies.set`](https://nextjs.org/docs/app/api-reference/functions/cookies#setting-a-cookie) 또는 [`cookies.delete`](https://nextjs.org/docs/app/api-reference/functions/cookies#deleting-cookies)를 사용하면 Router Cache가 무효화되어 쿠키를 사용하는 라우트(예: 인증)가 최신 상태로 유지됩니다.
  * [`router.refresh`](https://nextjs.org/docs/app/api-reference/functions/use-router)를 호출하면 Router Cache가 무효화되고 현재 라우트에 대해 서버에 새 요청을 보냅니다.

### 옵트아웃[](https://nextjs.org/docs/app/guides/caching#opting-out-3)

Next.js 15부터 페이지 세그먼트는 기본적으로 옵트아웃됩니다.

> **알아두면 좋은 점:** `<Link>` 컴포넌트의 `prefetch` prop을 `false`로 설정하면 [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)도 옵트아웃할 수 있습니다.

## Cache 상호 작용[](https://nextjs.org/docs/app/guides/caching#cache-interactions)

여러 캐싱 메커니즘을 구성할 때, 서로 어떻게 상호 작용하는지 이해하는 것이 중요합니다.

### Data Cache와 Full Route Cache[](https://nextjs.org/docs/app/guides/caching#data-cache-and-full-route-cache)

  * Data Cache를 재검증하거나 옵트아웃하면 렌더 출력이 데이터에 의존하므로 Full Route Cache가 무효화됩니다.
  * Full Route Cache를 무효화하거나 옵트아웃하더라도 Data Cache에는 영향을 주지 않습니다. 캐시된 데이터와 비캐시 데이터를 모두 포함하는 라우트를 동적으로 렌더링할 수 있습니다. 페이지 대부분은 캐시된 데이터를 사용하지만 일부 컴포넌트는 요청 시 가져와야 하는 데이터에 의존할 때 유용합니다. 모든 데이터를 다시 가져오는 성능 영향을 걱정하지 않고 동적으로 렌더링할 수 있습니다.

### Data Cache와 Client-side Router cache[](https://nextjs.org/docs/app/guides/caching#data-cache-and-client-side-router-cache)

  * [Server Action](https://nextjs.org/docs/app/getting-started/updating-data)에서 [`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath) 또는 [`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)를 사용하면 Data Cache와 Router cache를 즉시 무효화할 수 있습니다.
  * [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 Data Cache를 재검증해도 Route Handler가 특정 라우트에 묶여 있지 않기 때문에 Router Cache는 즉시 무효화되지 않습니다. 따라서 강제 새로고침 또는 자동 무효화 기간이 지날 때까지 Router Cache는 이전 페이로드를 계속 제공합니다.

## APIs[](https://nextjs.org/docs/app/guides/caching#apis)

다음 표는 다양한 Next.js API가 캐싱에 어떤 영향을 미치는지 개요를 제공합니다:

API| Router Cache| Full Route Cache| Data Cache| React Cache
---|---|---|---|---
[`<Link prefetch>`](https://nextjs.org/docs/app/guides/caching#link)| Cache| | |
[`router.prefetch`](https://nextjs.org/docs/app/guides/caching#routerprefetch)| Cache| | |
[`router.refresh`](https://nextjs.org/docs/app/guides/caching#routerrefresh)| Revalidate| | |
[`fetch`](https://nextjs.org/docs/app/guides/caching#fetch)| | | Cache| Cache (GET 및 HEAD)
[`fetch` `options.cache`](https://nextjs.org/docs/app/guides/caching#fetch-optionscache)| | | Cache 또는 Opt out|
[`fetch` `options.next.revalidate`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate)| | Revalidate| Revalidate|
[`fetch` `options.next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)| | Cache| Cache|
[`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)| Revalidate (Server Action)| Revalidate| Revalidate|
[`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath)| Revalidate (Server Action)| Revalidate| Revalidate|
[`const revalidate`](https://nextjs.org/docs/app/guides/caching#segment-config-options)| | Revalidate 또는 Opt out| Revalidate 또는 Opt out|
[`const dynamic`](https://nextjs.org/docs/app/guides/caching#segment-config-options)| | Cache 또는 Opt out| Cache 또는 Opt out|
[`cookies`](https://nextjs.org/docs/app/guides/caching#cookies)| Revalidate (Server Action)| Opt out| |
[`headers`, `searchParams`](https://nextjs.org/docs/app/guides/caching#dynamic-apis)| | Opt out| |
[`generateStaticParams`](https://nextjs.org/docs/app/guides/caching#generatestaticparams)| | Cache| |
[`React.cache`](https://nextjs.org/docs/app/guides/caching#react-cache-function)| | | | Cache
[`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)| | | Cache|

### `<Link>`[](https://nextjs.org/docs/app/guides/caching#link)

기본적으로 `<Link>` 컴포넌트는 Full Route Cache에서 라우트를 자동으로 prefetch하고 React Server Component Payload를 Router Cache에 추가합니다.

Prefetching을 비활성화하려면 `prefetch` prop을 `false`로 설정할 수 있습니다. 하지만 이는 캐시를 영구적으로 건너뛰지는 않으며, 사용자가 라우트를 방문하면 해당 세그먼트는 여전히 클라이언트 측에 캐시됩니다.

[`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)에 대해 자세히 알아보세요.

### `router.prefetch`[](https://nextjs.org/docs/app/guides/caching#routerprefetch)

`useRouter` 훅의 `prefetch` 옵션을 사용하면 라우트를 수동으로 prefetch할 수 있습니다. 이때 React Server Component Payload가 Router Cache에 추가됩니다.

[`useRouter` 훅](https://nextjs.org/docs/app/api-reference/functions/use-router)의 API 레퍼런스를 확인하세요.

### `router.refresh`[](https://nextjs.org/docs/app/guides/caching#routerrefresh)

`useRouter` 훅의 `refresh` 옵션을 사용하면 라우트를 수동으로 새로고침할 수 있습니다. 이는 Router Cache를 완전히 비우고 현재 라우트에 대해 서버에 새 요청을 보냅니다. `refresh`는 Data Cache나 Full Route Cache에는 영향을 주지 않습니다.

렌더링된 결과는 React 상태와 브라우저 상태를 유지하면서 클라이언트에서 재조정됩니다.

[`useRouter` 훅](https://nextjs.org/docs/app/api-reference/functions/use-router)의 API 레퍼런스를 확인하세요.

### `fetch`[](https://nextjs.org/docs/app/guides/caching#fetch)

`fetch`가 반환하는 데이터는 Data Cache에 자동으로 캐시되지 않습니다.

기본적으로 `cache` 또는 `next.revalidate` 옵션이 제공되지 않으면:

  * [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering): 매 요청마다 `fetch`가 실행되며 항상 최신 데이터를 반환합니다.
  * [정적 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering): 가져온 데이터는 [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)에 저장되고 렌더링 출력은 [Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache)에 저장됩니다. Next.js는 경로가 재검증될 때까지 이 캐시된 결과를 제공합니다.

[`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch)에서 더 많은 옵션을 확인하세요.

### `fetch options.cache`[](https://nextjs.org/docs/app/guides/caching#fetch-optionscache)

`cache` 옵션을 `force-cache`로 설정하여 개별 `fetch` 호출을 캐싱하도록 선택할 수 있습니다:
```
    // 캐싱을 사용
    fetch(`https://...`, { cache: 'force-cache' })
```

[`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch)에서 더 많은 옵션을 확인하세요.

### `fetch options.next.revalidate`[](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate)

`fetch`의 `next.revalidate` 옵션을 사용하면 개별 `fetch` 요청의 재검증 주기(초 단위)를 설정할 수 있습니다. 이는 Data Cache를 재검증하고, 이어서 Full Route Cache도 재검증합니다. 새로운 데이터가 가져와지고 컴포넌트가 서버에서 다시 렌더링됩니다.
```
    // 최대 1시간마다 재검증
    fetch(`https://...`, { next: { revalidate: 3600 } })
```

[`fetch` API reference](https://nextjs.org/docs/app/api-reference/functions/fetch)에서 더 많은 옵션을 확인하세요.

### `fetch options.next.tags` 및 `revalidateTag`[](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)

Next.js에는 정밀한 데이터 캐싱과 재검증을 위한 캐시 태깅 시스템이 있습니다.

  1. `fetch` 또는 [`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)를 사용할 때 하나 이상의 태그로 캐시 항목을 태깅할 수 있습니다.
  2. 그런 다음 `revalidateTag`를 호출하여 해당 태그와 연결된 캐시 항목을 제거할 수 있습니다.

예를 들어, 데이터를 가져올 때 태그를 설정할 수 있습니다:
```
    // 태그와 함께 데이터 캐시
    fetch(`https://...`, { next: { tags: ['a', 'b', 'c'] } })
```

그런 다음 캐시 항목을 제거하려면 `revalidateTag`를 태그와 함께 호출합니다:
```
    // 특정 태그의 항목을 재검증
    revalidateTag('a')
```

`revalidateTag`는 목적에 따라 다음 두 곳에서 사용할 수 있습니다:

  1. [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) \- 서드파티 이벤트(예: 웹훅)에 응답하여 데이터를 재검증합니다. Route Handler는 특정 라우트에 묶여 있지 않으므로 Router Cache는 즉시 무효화되지 않습니다.
  2. [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) \- 사용자 동작(예: 양식 제출) 후 데이터를 재검증합니다. 이는 해당 라우트의 Router Cache를 무효화합니다.

### `revalidatePath`[](https://nextjs.org/docs/app/guides/caching#revalidatepath)

`revalidatePath`는 단일 작업으로 특정 경로 아래의 데이터와 라우트 세그먼트를 수동으로 재검증하고 다시 렌더링할 수 있습니다. `revalidatePath`를 호출하면 Data Cache가 재검증되고, 이어서 Full Route Cache가 무효화됩니다.
```
    revalidatePath('/')
```

`revalidatePath`는 목적에 따라 두 곳에서 사용할 수 있습니다:

  1. [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) \- 서드파티 이벤트(예: 웹훅)에 응답해 데이터를 재검증합니다.
  2. [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) \- 사용자 상호작용(예: 양식 제출, 버튼 클릭) 후 데이터를 재검증합니다.

[`revalidatePath` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)를 확인하세요.

> **`revalidatePath`** vs. **`router.refresh`** :
>
> `router.refresh`를 호출하면 Router cache가 지워지고 Data Cache나 Full Route Cache를 무효화하지 않은 채 서버에서 라우트 세그먼트를 다시 렌더링합니다.
>
> 차이점은 `revalidatePath`는 Data Cache와 Full Route Cache를 제거하지만, `router.refresh()`는 클라이언트 측 API로서 Data Cache와 Full Route Cache를 변경하지 않는다는 점입니다.

### Dynamic APIs[](https://nextjs.org/docs/app/guides/caching#dynamic-apis)

`cookies`와 `headers` 같은 동적 API 및 Pages의 `searchParams` prop은 런타임에 들어오는 요청 정보에 의존합니다. 이를 사용하면 Full Route Cache에서 옵트아웃되며, 즉 라우트가 동적으로 렌더링됩니다.

#### `cookies`[](https://nextjs.org/docs/app/guides/caching#cookies)

Server Action에서 `cookies.set` 또는 `cookies.delete`를 사용하면 Router Cache가 무효화되어 쿠키를 사용하는 라우트가 최신 상태로 유지됩니다(예: 인증 변화를 반영).

[`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API reference를 확인하세요.

### Segment Config Options[](https://nextjs.org/docs/app/guides/caching#segment-config-options)

Route Segment Config 옵션은 라우트 세그먼트 기본값을 재정의하거나 `fetch` API를 사용할 수 없을 때(예: 데이터베이스 클라이언트, 서드파티 라이브러리) 활용할 수 있습니다.

다음 Route Segment Config 옵션은 Full Route Cache에서 옵트아웃합니다:

  * `const dynamic = 'force-dynamic'`

이 구성 옵션은 모든 fetch를 Data Cache에서 옵트아웃합니다(즉, `no-store`):

  * `const fetchCache = 'default-no-store'`

자세한 옵션은 [`fetchCache`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache)를 참조하세요.

[Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) 문서를 참조하면 더 많은 옵션을 확인할 수 있습니다.

### `generateStaticParams`[](https://nextjs.org/docs/app/guides/caching#generatestaticparams)

[동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)(예: `app/blog/[slug]/page.js`)의 경우 `generateStaticParams`가 제공하는 경로는 빌드 시 Full Route Cache에 캐시됩니다. 요청 시점에는 빌드 시 알 수 없었던 경로도 처음 방문할 때 캐시됩니다.

빌드 시 모든 경로를 정적으로 렌더링하려면 `generateStaticParams`에 전체 경로 목록을 전달하세요:

app/blog/[slug]/page.js
```
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      return posts.map((post) => ({
        slug: post.slug,
      }))
    }
```

빌드 시 경로의 일부만 정적으로 렌더링하고, 나머지는 런타임에서 첫 방문 시 렌더링하려면 경로의 부분 목록을 반환하세요:

app/blog/[slug]/page.js
```
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      // Render the first 10 posts at build time
      return posts.slice(0, 10).map((post) => ({
        slug: post.slug,
      }))
    }
```

모든 경로를 첫 방문 시 정적으로 렌더링하려면 빈 배열을 반환하세요(빌드 시 렌더링되는 경로 없음). 또는 [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)을 사용하세요:

app/blog/[slug]/page.js
```
    export async function generateStaticParams() {
      return []
    }
```

> **알아두면 좋아요:** `generateStaticParams`에서는 빈 배열이라도 반드시 배열을 반환해야 합니다. 그렇지 않으면 라우트가 동적으로 렌더링됩니다.

app/changelog/[slug]/page.js
```
    export const dynamic = 'force-static'
```

요청 시 캐싱을 비활성화하려면 라우트 세그먼트에 `export const dynamicParams = false` 옵션을 추가하세요. 이 구성 옵션을 사용하면 `generateStaticParams`가 제공한 경로만 제공되며, 다른 경로는 404를 반환하거나([catch-all routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)의 경우) 매칭됩니다.

### React `cache` 함수[](https://nextjs.org/docs/app/guides/caching#react-cache-function)

React `cache` 함수는 함수의 반환값을 메모이제이션하여 동일한 함수를 여러 번 호출해도 한 번만 실행되도록 해줍니다.

`GET` 또는 `HEAD` 메서드를 사용하는 `fetch` 요청은 자동으로 메모이제이션되므로 React `cache`로 감쌀 필요가 없습니다. 그러나 다른 `fetch` 메서드를 사용할 때나 기본적으로 요청을 메모이제이션하지 않는 데이터 페칭 라이브러리(일부 데이터베이스, CMS, GraphQL 클라이언트 등)를 사용할 때는 `cache`를 이용해 수동으로 데이터 요청을 메모이제이션할 수 있습니다.

utils/get-item.ts

JavaScriptTypeScript
```
    import { cache } from 'react'
    import db from '@/lib/db'

    export const getItem = cache(async (id: string) => {
      const item = await db.item.findUnique({ id })
      return item
    })
```

Send