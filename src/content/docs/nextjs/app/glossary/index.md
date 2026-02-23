---
title: 'App Router: 용어집'
description: 'React Server Components 위에 구축되어 Next.js 13에서 도입된 라우터입니다. 파일 시스템 기반 라우팅을 사용하며 레이아웃, 중첩 라우팅, 로딩 상태, 오류 처리 등을 지원합니다. 자세한 내용은 App Router 문서를 참고하세요.'
---

# App Router: 용어집 | Next.js
출처 URL: https://nextjs.org/docs/app/glossary

# Next.js 용어집

마지막 업데이트 2026년 2월 20일

# A[](https://nextjs.org/docs/app/glossary#a)

## App Router[](https://nextjs.org/docs/app/glossary#app-router)

React Server Components 위에 구축되어 Next.js 13에서 도입된 라우터입니다. 파일 시스템 기반 라우팅을 사용하며 레이아웃, 중첩 라우팅, 로딩 상태, 오류 처리 등을 지원합니다. 자세한 내용은 [App Router 문서](https://nextjs.org/docs/app)를 참고하세요.

# B[](https://nextjs.org/docs/app/glossary#b)

## Build time[](https://nextjs.org/docs/app/glossary#build-time)

애플리케이션이 컴파일되는 단계입니다. 빌드 타임 동안 Next.js는 코드를 프로덕션용으로 최적화된 파일로 변환하고, 정적 페이지를 생성하며, 배포용 에셋을 준비합니다. [`next build` CLI 참고서](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)를 확인하세요.

# C[](https://nextjs.org/docs/app/glossary#c)

## Cache Components[](https://nextjs.org/docs/app/glossary#cache-components)

[`"use cache"` 지시문](https://nextjs.org/docs/app/api-reference/directives/use-cache)을 사용해 컴포넌트 또는 함수 단위 캐싱을 활성화하는 기능입니다. Cache Components는 정적 HTML 셸을 사전 렌더링해 즉시 제공하고, 준비가 되면 동적 콘텐츠를 스트리밍하여 단일 라우트 안에서 정적·캐시·동적 콘텐츠를 혼합할 수 있게 해줍니다. [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)로 캐시 지속 시간을 구성하고, [`cacheTag()`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)로 캐시된 데이터를 태깅하며, [`updateTag()`](https://nextjs.org/docs/app/api-reference/functions/updateTag)로 온디맨드 무효화를 수행하세요. [Cache Components 가이드](https://nextjs.org/docs/app/getting-started/cache-components)에서 더 알아보세요.

## Catch-all Segments[](https://nextjs.org/docs/app/glossary#catch-all-segments)

`[...folder]/page.js` 구문을 사용해 여러 URL 부분과 매칭할 수 있는 동적 라우트 세그먼트입니다. 남은 모든 URL 세그먼트를 캡처하며, 문서 사이트나 파일 브라우저 같은 기능 구현에 유용합니다. 자세한 내용은 [Dynamic Route Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)를 참고하세요.

## Client Bundles[](https://nextjs.org/docs/app/glossary#client-bundles)

브라우저로 전송되는 JavaScript 번들입니다. Next.js는 초기 페이로드를 줄이고 각 페이지에 필요한 코드만 로드하기 위해 [모듈 그래프](https://nextjs.org/docs/app/glossary#module-graph)를 기준으로 자동 분할합니다.

## Client Component[](https://nextjs.org/docs/app/glossary#client-component)

브라우저에서 실행되는 React 컴포넌트입니다. Next.js에서는 초기 페이지 생성 시 서버에서도 렌더링될 수 있습니다. 상태, 이펙트, 이벤트 핸들러, 브라우저 API를 사용할 수 있으며 파일 상단에 [`"use client"` 지시문](https://nextjs.org/docs/app/glossary#use-client-directive)으로 표시합니다. [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 자세히 알아보세요.

## Client-side navigation[](https://nextjs.org/docs/app/glossary#client-side-navigation)

전체 페이지 새로고침 없이 페이지 콘텐츠를 동적으로 업데이트하는 내비게이션 방식입니다. Next.js는 [`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)를 사용해 클라이언트 측 내비게이션을 수행하며, 공유 레이아웃을 상호작용 가능하게 유지하고 브라우저 상태를 보존합니다. [Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)를 참고하세요.

## Code Splitting[](https://nextjs.org/docs/app/glossary#code-splitting)

애플리케이션을 라우트 기반의 더 작은 JavaScript 청크로 나누는 과정입니다. 모든 코드를 한 번에 로드하는 대신 현재 라우트에 필요한 코드만 로드하여 초기 로딩 시간을 줄입니다. Next.js는 라우트를 기준으로 자동으로 코드 분할을 수행합니다. [Package Bundling 가이드](https://nextjs.org/docs/app/guides/package-bundling)에서 자세히 알아보세요.

# D[](https://nextjs.org/docs/app/glossary#d)

## Dynamic rendering[](https://nextjs.org/docs/app/glossary#dynamic-rendering)

[Request-time rendering](https://nextjs.org/docs/app/glossary#request-time-rendering)을 참고하세요.

## Dynamic route segments[](https://nextjs.org/docs/app/glossary#dynamic-route-segments)

요청 시점 데이터로 생성되는 [라우트 세그먼트](https://nextjs.org/docs/app/glossary#route-segment)입니다. 폴더 이름을 대괄호로 감싸는(e.g., `[slug]`) 방식으로 만들며, 블로그 게시물이나 상품 페이지처럼 동적 데이터로 라우트를 생성할 수 있습니다. [Dynamic Route Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 참고하세요.

# E[](https://nextjs.org/docs/app/glossary#e)

## Environment Variables[](https://nextjs.org/docs/app/glossary#environment-variables)

빌드 타임 또는 요청 시점에 접근 가능한 구성 값입니다. Next.js에서는 `NEXT_PUBLIC_` 접두사가 붙은 변수가 브라우저에 노출되고, 그 외 변수는 서버 측에서만 사용할 수 있습니다. [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables)를 참고하세요.

## Error Boundary[](https://nextjs.org/docs/app/glossary#error-boundary)

자식 컴포넌트 트리에서 발생하는 JavaScript 오류를 포착해 대체 UI를 표시하는 React 컴포넌트입니다. Next.js에서는 [`error.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/error)을 생성해 라우트 세그먼트를 자동으로 오류 경계로 감쌀 수 있습니다. [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling)을 확인하세요.

# F[](https://nextjs.org/docs/app/glossary#f)

## Font Optimization[](https://nextjs.org/docs/app/glossary#font-optimization)

[`next/font`](https://nextjs.org/docs/app/api-reference/components/font)를 사용한 자동 폰트 최적화입니다. Next.js는 폰트를 자체 호스팅하고, 레이아웃 시프트를 제거하며, 성능을 위한 모범 사례를 적용합니다. Google Fonts와 로컬 폰트 파일 모두에서 작동합니다. [Fonts](https://nextjs.org/docs/app/getting-started/fonts)를 참고하세요.

## File-system caching[](https://nextjs.org/docs/app/glossary#file-system-caching)

컴파일러 아티팩트를 실행 간 디스크에 저장해 `next dev` 또는 `next build` 명령 간 작업량을 줄여 컴파일 시간을 크게 단축하는 Turbopack 기능입니다. [Turbopack FileSystem Caching](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)을 참고하세요.

# H[](https://nextjs.org/docs/app/glossary#h)

## Hydration[](https://nextjs.org/docs/app/glossary#hydration)

서버에서 렌더링된 정적 HTML을 상호작용 가능하게 만들기 위해 React가 DOM에 이벤트 핸들러를 연결하는 과정입니다. 하이드레이션 동안 React는 서버 렌더링된 마크업과 클라이언트 측 JavaScript를 비교·동기화합니다. [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)에서 자세히 알아보세요.

# I[](https://nextjs.org/docs/app/glossary#i)

## Import Aliases[](https://nextjs.org/docs/app/glossary#import-aliases)

자주 사용하는 디렉터리에 대한 축약 경로 매핑입니다. 임포트 별칭은 상대 경로의 복잡성을 줄이고 코드를 더 읽기 쉽고 유지보수하기 쉽게 만듭니다. [Absolute Imports and Module Path Aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)를 참고하세요.

## Incremental Static Regeneration (ISR)[](https://nextjs.org/docs/app/glossary#incremental-static-regeneration-isr)

전체 사이트를 다시 빌드하지 않고 정적 콘텐츠를 업데이트할 수 있는 기술입니다. ISR은 페이지별로 정적 생성을 사용하면서도, 트래픽이 들어올 때 백그라운드에서 페이지를 재검증합니다. [ISR 가이드](https://nextjs.org/docs/app/guides/incremental-static-regeneration)에서 자세히 살펴보세요.

> **알아두면 좋아요**: Next.js에서 ISR은 [Revalidation](https://nextjs.org/docs/app/glossary#revalidation)이라고도 합니다.

## Intercepting Routes[](https://nextjs.org/docs/app/glossary#intercepting-routes)

현재 레이아웃 안에서 애플리케이션의 다른 부분에 있는 라우트를 로드할 수 있는 라우팅 패턴입니다. 사용자가 컨텍스트를 전환하지 않고도 모달 같은 콘텐츠를 표시하면서 URL 공유 가능성을 유지하는 데 유용합니다. [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)를 참고하세요.

## Image Optimization[](https://nextjs.org/docs/app/glossary#image-optimization)

[`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image)를 이용한 자동 이미지 최적화입니다. Next.js는 이미지를 온디맨드로 최적화하고, WebP 같은 최신 포맷으로 제공하며, 지연 로딩과 반응형 크기를 자동 처리합니다. [Images](https://nextjs.org/docs/app/getting-started/images)에서 자세히 알아보세요.

# L[](https://nextjs.org/docs/app/glossary#l)

## Layout[](https://nextjs.org/docs/app/glossary#layout)

여러 페이지 간에 공유되는 UI입니다. 레이아웃은 상태를 유지하고, 상호작용성을 보존하며, 내비게이션 시 다시 렌더링되지 않습니다. [`layout.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/layout)에서 React 컴포넌트를 내보내 정의합니다. [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)를 참고하세요.

## Loading UI[](https://nextjs.org/docs/app/glossary#loading-ui)

[라우트 세그먼트](https://nextjs.org/docs/app/glossary#route-segment)가 로드되는 동안 표시되는 대체 UI입니다. 폴더에 [`loading.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/loading)을 추가하면 페이지가 자동으로 [Suspense 경계](https://nextjs.org/docs/app/glossary#suspense-boundary)로 감싸집니다. [Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading)를 확인하세요.

# M[](https://nextjs.org/docs/app/glossary#m)

## Module Graph[](https://nextjs.org/docs/app/glossary#module-graph)

앱의 파일 의존성 그래프입니다. 각 파일(모듈)은 노드이며, import/export 관계가 간선을 형성합니다. Next.js는 이 그래프를 분석해 최적의 번들링 및 코드 분할 전략을 결정합니다. [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size)를 참고하세요.

## Metadata[](https://nextjs.org/docs/app/glossary#metadata)

브라우저와 검색 엔진에서 사용하는 페이지 정보(제목, 설명, Open Graph 이미지 등)입니다. Next.js에서는 레이아웃이나 페이지 파일에서 [`metadata` export](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) 또는 [`generateMetadata` 함수](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)를 통해 메타데이터를 정의합니다. [Metadata and OG Images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)를 참고하세요.

## Memoization[](https://nextjs.org/docs/app/glossary#memoization)

요청당(렌더 패스) 동일한 함수를 여러 번 호출하더라도 한 번만 실행되도록 함수의 반환 값을 캐싱하는 것입니다. Next.js에서는 동일한 URL과 옵션을 가진 fetch 요청이 자동으로 메모이제이션됩니다. [React Cache](https://react.dev/reference/react/cache)에 대해 더 알아보세요.

## Middleware[](https://nextjs.org/docs/app/glossary#middleware)

[Proxy](https://nextjs.org/docs/app/glossary#proxy)를 참고하세요.

# N[](https://nextjs.org/docs/app/glossary#n)

## Not Found[](https://nextjs.org/docs/app/glossary#not-found)

라우트가 존재하지 않거나 [`notFound()` 함수](https://nextjs.org/docs/app/api-reference/functions/not-found)가 호출될 때 표시되는 특수 컴포넌트입니다. 앱 디렉터리에 [`not-found.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)을 추가해 생성합니다. [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling#not-found)을 참고하세요.

# P[](https://nextjs.org/docs/app/glossary#p)

## Private Folders[](https://nextjs.org/docs/app/glossary#private-folders)

라우팅 시스템에서 제외되도록 밑줄(`_components` 등)로 시작하는 폴더입니다. 접근 가능한 라우트를 만들지 않고 코드 조직 및 공용 유틸리티를 위해 사용됩니다. 자세한 내용은 [Private Folders](https://nextjs.org/docs/app/getting-started/project-structure#private-folders)를 참고하세요.

## Page[](https://nextjs.org/docs/app/glossary#page)

특정 라우트에 고유한 UI입니다. `app` 디렉터리 안의 [`page.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/page)에서 React 컴포넌트를 export하여 정의합니다. 자세한 내용은 [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)를 참고하세요.

## Parallel Routes[](https://nextjs.org/docs/app/glossary#parallel-routes)

동일한 레이아웃 안에서 여러 페이지를 동시에 또는 조건부로 렌더링할 수 있는 패턴입니다. `@folder` 규칙을 따르는 이름 있는 슬롯으로 생성되며, 대시보드·모달·복잡한 레이아웃에 유용합니다. 자세한 내용은 [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)를 참고하세요.

## Partial Prerendering (PPR)[](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr)

단일 라우트 안에서 정적 렌더링과 동적 렌더링을 결합하는 렌더링 최적화입니다. 정적 셸은 즉시 제공되고, 동적 콘텐츠는 준비되는 대로 스트리밍되어 두 렌더링 전략의 장점을 모두 제공합니다. 자세한 내용은 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 참고하세요.

## Prefetching[](https://nextjs.org/docs/app/glossary#prefetching)

사용자가 이동하기 전에 백그라운드에서 라우트를 미리 로드하는 것입니다. Next.js는 뷰포트에 들어오는 [`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)로 연결된 라우트를 자동으로 prefetch하여 즉각적인 탐색 경험을 제공합니다. 자세한 내용은 [Prefetching guide](https://nextjs.org/docs/app/guides/prefetching)를 참고하세요.

## Prerendering[](https://nextjs.org/docs/app/glossary#prerendering)

컴포넌트를 [빌드 시간](https://nextjs.org/docs/app/glossary#build-time) 또는 [재검증](https://nextjs.org/docs/app/glossary#revalidation) 중 백그라운드에서 렌더링하는 것입니다. 결과물은 HTML과 [RSC Payload](https://nextjs.org/docs/app/glossary#rsc-payload)로, CDN에 캐시하고 제공할 수 있습니다. [Request-time APIs](https://nextjs.org/docs/app/glossary#request-time-apis)를 사용하지 않는 컴포넌트의 기본 동작입니다.

## Proxy[](https://nextjs.org/docs/app/glossary#proxy)

요청이 완료되기 전에 서버에서 코드를 실행하는 파일([`proxy.js`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy))입니다. 로깅·리디렉트·리라이트 같은 서버 측 로직을 구현하는 데 사용되며, 이전에는 Middleware로 알려졌습니다. 자세한 내용은 [Proxy guide](https://nextjs.org/docs/app/getting-started/proxy)를 참고하세요.

# R[](https://nextjs.org/docs/app/glossary#r)

## Redirect[](https://nextjs.org/docs/app/glossary#redirect)

사용자를 한 URL에서 다른 URL로 보내는 것입니다. Next.js에서는 [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)에서 설정하거나 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 반환하거나 [`redirect()` 함수](https://nextjs.org/docs/app/api-reference/functions/redirect)로 프로그래밍 방식으로 트리거할 수 있습니다. 자세한 내용은 [Redirecting](https://nextjs.org/docs/app/guides/redirecting)을 참고하세요.

## Request time[](https://nextjs.org/docs/app/glossary#request-time)

사용자가 애플리케이션에 요청을 보내는 시점입니다. 요청 시점에는 동적 라우트가 렌더링되고, 쿠키와 헤더에 접근할 수 있으며, 요청별 데이터를 사용할 수 있습니다.

## Request-time APIs[](https://nextjs.org/docs/app/glossary#request-time-apis)

요청별 데이터에 접근하여 컴포넌트가 [request-time rendering](https://nextjs.org/docs/app/glossary#request-time-rendering)을 사용하도록 만드는 함수들입니다. 다음이 포함됩니다:

  * [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies) \- 요청 쿠키에 접근
  * [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) \- 요청 헤더에 접근
  * [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) \- URL 쿼리 매개변수에 접근
  * [`draftMode()`](https://nextjs.org/docs/app/api-reference/functions/draft-mode) \- 드래프트 모드 활성화 또는 확인

## Request-time rendering[](https://nextjs.org/docs/app/glossary#request-time-rendering)

컴포넌트를 [빌드 시간](https://nextjs.org/docs/app/glossary#build-time)이 아니라 [요청 시점](https://nextjs.org/docs/app/glossary#request-time)에서 렌더링하는 것입니다. [Request-time APIs](https://nextjs.org/docs/app/glossary#request-time-apis)를 사용하면 컴포넌트는 동적이 됩니다.

## Revalidation[](https://nextjs.org/docs/app/glossary#revalidation)

캐시된 데이터를 업데이트하는 프로세스입니다. [`cacheLife()`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)로 캐시 기간을 설정하는 시간 기반, 혹은 [`cacheTag()`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)로 데이터를 태그하고 [`updateTag()`](https://nextjs.org/docs/app/api-reference/functions/updateTag)로 무효화하는 온디맨드 방식이 있습니다. 자세한 내용은 [Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)을 참고하세요.

## Rewrite[](https://nextjs.org/docs/app/glossary#rewrite)

브라우저 URL을 바꾸지 않고 들어오는 요청 경로를 다른 목적지 경로에 매핑하는 것입니다. [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)에서 설정하거나 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 반환할 수 있으며, 외부 서비스나 레거시 URL로 프록시할 때 유용합니다.

## Route Groups[](https://nextjs.org/docs/app/glossary#route-groups)

URL 구조에 영향을 주지 않고 라우트를 구성하는 방법입니다. 폴더 이름을 괄호로 감싸(e.g., `(marketing)`), 관련 라우트를 정리하고 그룹별 [레이아웃](https://nextjs.org/docs/app/glossary#layout)을 활성화할 수 있습니다. 자세한 내용은 [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups)를 참고하세요.

## Route Handler[](https://nextjs.org/docs/app/glossary#route-handler)

특정 라우트의 HTTP 요청을 처리하는 함수로, [`route.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/route)에 정의합니다. Web Request 및 Response API를 사용하며 `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS` 메서드를 처리할 수 있습니다. 자세한 내용은 [Route Handlers](https://nextjs.org/docs/app/getting-started/route-handlers)를 참고하세요.

## Route Segment[](https://nextjs.org/docs/app/glossary#route-segment)

`app` 디렉터리의 폴더로 정의된 URL 경로의 일부(두 슬래시 사이)입니다. 각 폴더는 URL 구조의 한 세그먼트를 나타냅니다. 자세한 내용은 [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)를 참고하세요.

## RSC Payload[](https://nextjs.org/docs/app/glossary#rsc-payload)

React Server Component 트리를 렌더링한 결과를 담은 compact 이진 표현입니다. 서버 컴포넌트의 렌더링 결과, 클라이언트 컴포넌트용 플레이스홀더, 컴포넌트 간에 전달되는 props를 포함합니다. 자세한 내용은 [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)를 참고하세요.

# S[](https://nextjs.org/docs/app/glossary#s)

## Server Component[](https://nextjs.org/docs/app/glossary#server-component)

App Router의 기본 컴포넌트 유형입니다. 서버에서 렌더링되고 데이터를 직접 가져올 수 있으며 클라이언트 JavaScript 번들에 추가되지 않습니다. 상태나 브라우저 API는 사용할 수 없습니다. 자세한 내용은 [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 참고하세요.

## Server Action[](https://nextjs.org/docs/app/glossary#server-action)

클라이언트 컴포넌트에 prop으로 전달하거나 form action에 바인딩하는 [Server Function](https://nextjs.org/docs/app/glossary#server-function)입니다. 주로 폼 제출과 데이터 변경에 사용됩니다. 자세한 내용은 [Server Actions and Mutations](https://nextjs.org/docs/app/getting-started/updating-data)를 참고하세요.

## Server Function[](https://nextjs.org/docs/app/glossary#server-function)

서버에서 실행되는 비동기 함수로, [`"use server"` 지시문](https://nextjs.org/docs/app/api-reference/directives/use-server)을 붙여 표시합니다. 클라이언트 컴포넌트에서 호출할 수 있으며, 클라이언트 컴포넌트에 prop으로 전달하거나 form action에 바인딩하면 [Server Actions](https://nextjs.org/docs/app/glossary#server-action)으로 호출됩니다. 자세한 내용은 [React Server Functions](https://react.dev/reference/rsc/server-functions)를 참고하세요.

## Static Export[](https://nextjs.org/docs/app/glossary#static-export)

HTML, CSS, JavaScript 파일로 구성된 완전한 정적 사이트를 생성하는 배포 모드입니다. `next.config.js`에서 `output: 'export'`를 설정하면 활성화되며, Node.js 서버 없이도 임의의 정적 파일 서버에 호스팅할 수 있습니다. 자세한 내용은 [Static Exports](https://nextjs.org/docs/app/guides/static-exports)를 참고하세요.

## Static rendering[](https://nextjs.org/docs/app/glossary#static-rendering)

[Prerendering](https://nextjs.org/docs/app/glossary#prerendering)을 참고하세요.

## Static Assets[](https://nextjs.org/docs/app/glossary#static-assets)

이미지·폰트·비디오 등 처리 없이 바로 제공되는 파일입니다. 일반적으로 `public` 디렉터리에 저장되며 상대 경로로 참조합니다. 자세한 내용은 [Static Assets](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)를 참고하세요.

## Static Shell[](https://nextjs.org/docs/app/glossary#static-shell)

브라우저에 즉시 제공되는 페이지의 프리렌더 HTML 구조입니다. [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr)이 적용되면 정적으로 렌더링 가능한 모든 콘텐츠와 나중에 스트리밍되는 동적 콘텐츠를 위한 [Suspense boundary](https://nextjs.org/docs/app/glossary#suspense-boundary) 폴백을 포함합니다.

## Streaming[](https://nextjs.org/docs/app/glossary#streaming)

페이지의 일부를 전체 렌더링을 기다리지 않고 준비되는 대로 클라이언트에 전송하는 기술입니다. [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)나 수동 `<Suspense>` 경계로 자동 활성화됩니다. 자세한 내용은 [Linking and Navigating - Streaming](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 참고하세요.

## Suspense boundary[](https://nextjs.org/docs/app/glossary#suspense-boundary)

비동기 콘텐츠를 감싸고 로딩 중 폴백 UI를 표시하는 React [`<Suspense>`](https://react.dev/reference/react/Suspense) 컴포넌트입니다. Next.js에서는 Suspense 경계가 [static shell](https://nextjs.org/docs/app/glossary#static-shell)의 끝과 [streaming](https://nextjs.org/docs/app/glossary#streaming)의 시작을 정의하여 [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr)을 가능하게 합니다.

# T[](https://nextjs.org/docs/app/glossary#t)

## Turbopack[](https://nextjs.org/docs/app/glossary#turbopack)

Next.js를 위해 만들어진 빠른 Rust 기반 번들러입니다. `next dev`의 기본 번들러이며 `next build`에서도 사용할 수 있습니다. Webpack과 비교해 훨씬 빠른 컴파일 속도를 제공합니다. 자세한 내용은 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 참고하세요.

## Tree Shaking[](https://nextjs.org/docs/app/glossary#tree-shaking)

빌드 과정에서 JavaScript 번들에서 사용되지 않는 코드를 제거하는 과정입니다. Next.js는 번들 크기를 줄이기 위해 코드를 자동으로 tree-shake합니다. 자세한 내용은 [Package Bundling guide](https://nextjs.org/docs/app/guides/package-bundling)를 참고하세요.

# U[](https://nextjs.org/docs/app/glossary#u)

## `"use cache"` Directive[](https://nextjs.org/docs/app/glossary#use-cache-directive)

컴포넌트나 함수를 캐시 가능한 대상으로 표시하는 지시문입니다. 파일 상단에 배치하면 해당 파일의 모든 export가 캐시 가능함을 나타내고, 함수나 컴포넌트 상단에 인라인으로 배치하면 특정 스코프만 캐시 가능하도록 표시할 수 있습니다. 자세한 내용은 [`"use cache"` reference](https://nextjs.org/docs/app/api-reference/directives/use-cache)에서 확인하세요.

## `"use client"` Directive[](https://nextjs.org/docs/app/glossary#use-client-directive)

서버 코드와 클라이언트 코드 사이의 경계를 표시하는 특수한 React 지시문입니다. 반드시 파일 최상단, 어떤 import나 다른 코드보다 앞에 위치해야 합니다. React 컴포넌트, 헬퍼 함수, 변수 선언, import된 모든 의존성이 [client bundle](https://nextjs.org/docs/app/glossary#client-bundles)에 포함되어야 함을 나타냅니다. 자세한 내용은 [`"use client"` reference](https://nextjs.org/docs/app/api-reference/directives/use-client)에서 확인하세요.

## `"use server"` Directive[](https://nextjs.org/docs/app/glossary#use-server-directive)

클라이언트 측 코드에서 호출할 수 있는 [Server Function](https://nextjs.org/docs/app/glossary#server-function)으로 함수를 표시하는 지시문입니다. 파일 상단에 배치하면 해당 파일의 모든 export가 Server Function임을 나타내고, 함수 상단에 인라인으로 배치하면 특정 함수만 표시할 수 있습니다. 자세한 내용은 [`"use server"` reference](https://nextjs.org/docs/app/api-reference/directives/use-server)에서 확인하세요.

# V[](https://nextjs.org/docs/app/glossary#v)

## Version skew[](https://nextjs.org/docs/app/glossary#version-skew)

애플리케이션의 새 버전을 배포한 후에도 여전히 활성 상태인 클라이언트가 이전 빌드의 JavaScript, CSS, 데이터 등을 참조할 수 있습니다. 클라이언트와 서버 버전이 어긋나는 이 상황을 버전 스큐라 하며, 누락된 에셋, Server Action 오류, 내비게이션 실패를 유발할 수 있습니다. Next.js는 [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId)를 사용해 버전 스큐를 감지하고 처리합니다. 자세한 내용은 [Self-Hosting - Version Skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew)를 참고하세요.

Was this helpful?

supported.

Send
