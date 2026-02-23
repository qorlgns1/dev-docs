---
title: '가이드: 프로덕션'
description: '원본 URL: https://nextjs.org/docs/app/guides/production-checklist'
---

# 가이드: 프로덕션 | Next.js

원본 URL: https://nextjs.org/docs/app/guides/production-checklist

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)프로덕션

페이지 복사

# 프로덕션용 Next.js 애플리케이션 최적화 방법

최종 업데이트 2026년 2월 20일

Next.js 애플리케이션을 프로덕션에 배포하기 전에 최상의 사용자 경험, 성능, 보안을 위해 구현을 고려해야 하는 최적화와 패턴이 있습니다.

이 문서는 [애플리케이션을 빌드할 때](https://nextjs.org/docs/app/guides/production-checklist#during-development), [프로덕션 직전](https://nextjs.org/docs/app/guides/production-checklist#before-going-to-production), 그리고 알아두어야 할 [자동 Next.js 최적화](https://nextjs.org/docs/app/guides/production-checklist#automatic-optimizations)에 대한 모범 사례를 참조용으로 제공합니다.

## 자동 최적화[](https://nextjs.org/docs/app/guides/production-checklist#automatic-optimizations)

다음 Next.js 최적화는 기본적으로 활성화되어 있으며 추가 설정이 필요 없습니다.

  * **[서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components):** Next.js는 기본적으로 Server Components(서버 컴포넌트)를 사용합니다. 서버 컴포넌트는 서버에서 실행되며 클라이언트 렌더링 시 JavaScript를 요구하지 않으므로 클라이언트 측 JavaScript 번들 크기에 영향을 주지 않습니다. 이후 상호작용이 필요할 때 [Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 사용하면 됩니다.
  * **[코드 분할](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works):** 서버 컴포넌트는 라우트 세그먼트별 자동 코드 분할을 가능하게 합니다. 필요한 경우 [지연 로딩](https://nextjs.org/docs/app/guides/lazy-loading)을 통해 클라이언트 컴포넌트와 서드파티 라이브러리 로딩을 고려하세요.
  * **[프리패칭](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching):** 새로운 라우트 링크가 사용자 뷰포트에 들어오면 Next.js가 백그라운드에서 해당 라우트를 프리패치하여 거의 즉각적인 내비게이션을 제공합니다. 필요하다면 프리패칭을 비활성화할 수 있습니다.
  * **[정적 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering):** Next.js는 서버에서 서버/클라이언트 컴포넌트를 빌드 시점에 정적으로 렌더링하고 결과를 캐시하여 애플리케이션 성능을 향상시킵니다. 필요한 라우트에 대해 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 전환할 수 있습니다. 
  * **[캐싱](https://nextjs.org/docs/app/guides/caching):** Next.js는 데이터 요청, 서버/클라이언트 컴포넌트 렌더링 결과, 정적 자산 등을 캐시하여 서버·데이터베이스·백엔드 서비스로의 네트워크 요청 횟수를 줄입니다. 필요하다면 캐싱을 비활성화할 수 있습니다.



이러한 기본값은 애플리케이션 성능 향상과 각 네트워크 요청마다 전달되는 데이터 양 및 비용 절감을 목표로 합니다.

## 개발 중[](https://nextjs.org/docs/app/guides/production-checklist#during-development)

애플리케이션을 구축하면서 최상의 성능과 사용자 경험을 보장하기 위해 아래 기능 사용을 권장합니다.

### 라우팅 및 렌더링[](https://nextjs.org/docs/app/guides/production-checklist#routing-and-rendering)

  * **[레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout):** 페이지 간 UI를 공유하고 내비게이션 시 [부분 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 활성화하세요.
  * **[`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link):** [클라이언트 측 내비게이션과 프리패칭](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works)을 위해 `<Link>` 컴포넌트를 사용하세요.
  * **[오류 처리](https://nextjs.org/docs/app/getting-started/error-handling):** 커스텀 오류 페이지를 만들어 프로덕션에서 [모든 오류](https://nextjs.org/docs/app/getting-started/error-handling)와 [404 오류](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)를 우아하게 처리하세요.
  * **[클라이언트·서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples):** 서버/클라이언트 컴포넌트 권장 조합 패턴을 따르고 불필요한 클라이언트 번들 증가를 피하기 위해 [`"use client"` 경계](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#moving-client-components-down-the-tree)를 점검하세요.
  * **[동적 API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering):** [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)나 [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) 프롭 같은 동적 API는 해당 라우트 전체(또는 [Root Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)에서 사용하면 전체 앱)를 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 전환함을 인지하고, 의도적으로 사용하며 필요 시 `<Suspense>` 경계로 감싸세요.



> **알아두면 좋은 정보**: [부분 사전 렌더링(실험 기능)](https://nextjs.org/blog/next-14#partial-prerendering-preview)을 사용하면 라우트 전체를 동적으로 전환하지 않고도 라우트 일부만 동적으로 유지할 수 있습니다.

### 데이터 페칭 및 캐싱[](https://nextjs.org/docs/app/guides/production-checklist#data-fetching-and-caching)

  * **[서버 컴포넌트](https://nextjs.org/docs/app/getting-started/fetching-data):** 서버 컴포넌트를 사용해 서버에서 데이터 페칭이 주는 이점을 활용하세요.
  * **[라우트 핸들러](https://nextjs.org/docs/app/api-reference/file-conventions/route):** 클라이언트 컴포넌트에서 백엔드 리소스에 접근하려면 라우트 핸들러를 사용하되, 서버 컴포넌트에서 라우트 핸들러를 호출해 서버 요청을 하나 더 만들지는 마세요.
  * **[스트리밍](https://nextjs.org/docs/app/api-reference/file-conventions/loading):** Loading UI와 React Suspense를 사용해 서버에서 클라이언트로 UI를 점진적으로 전송하고, 데이터 페칭 동안 전체 라우트가 블로킹되는 것을 막으세요.
  * **[병렬 데이터 페칭](https://nextjs.org/docs/app/getting-started/fetching-data#parallel-data-fetching):** 필요하다면 데이터를 병렬로 가져와 네트워크 폭포수 현상을 줄이고, [데이터 프리로딩](https://nextjs.org/docs/app/getting-started/fetching-data#preloading-data)도 검토하세요.
  * **[데이터 캐싱](https://nextjs.org/docs/app/guides/caching#data-cache):** 데이터 요청이 캐시되고 있는지 확인하고 필요하다면 캐싱을 활성화하세요. `fetch`를 사용하지 않는 요청도 [캐시](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)되도록 보장하세요.
  * **[정적 이미지](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder):** `public` 디렉터리를 사용해 이미지 등 애플리케이션 정적 자산을 자동으로 캐시하세요.



### UI 및 접근성[](https://nextjs.org/docs/app/guides/production-checklist#ui-and-accessibility)

  * **[폼과 검증](https://nextjs.org/docs/app/guides/forms):** 서버 액션을 사용해 폼 제출, 서버 측 검증, 오류 처리를 수행하세요.
  * **[글로벌 오류 UI](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error):** 앱 전체에서 일관되고 접근 가능한 오류 폴백 UI와 복구를 제공하려면 `app/global-error.tsx`를 추가하세요.
  * **[글로벌 404](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#global-not-foundjs-experimental):** 앱 전체에서 매칭되지 않는 라우트에 접근 가능한 404 페이지를 제공하려면 `app/global-not-found.tsx`를 추가하세요.


  * **[폰트 모듈](https://nextjs.org/docs/app/api-reference/components/font):** 폰트 모듈을 사용해 폰트 파일을 다른 정적 자산과 함께 자동으로 호스팅하고, 외부 네트워크 요청을 제거하며, [레이아웃 시프트](https://web.dev/articles/cls)를 줄이세요.
  * **[`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image):** 이미지 컴포넌트를 사용해 이미지를 자동 최적화하고 레이아웃 시프트를 방지하며 WebP 같은 최신 포맷으로 제공하세요.
  * **[`<Script>` 컴포넌트](https://nextjs.org/docs/app/guides/scripts):** Script 컴포넌트를 사용해 서드파티 스크립트를 최적화하고, 자동 지연 로딩 및 메인 스레드 블로킹을 방지하세요.
  * **[ESLint](https://nextjs.org/docs/architecture/accessibility#linting):** 기본 제공 `eslint-plugin-jsx-a11y` 플러그인으로 접근성 문제를 조기에 발견하세요.



### 보안[](https://nextjs.org/docs/app/guides/production-checklist#security)

  * **[테인트](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint):** 민감한 데이터가 클라이언트로 노출되지 않도록 데이터 객체나 특정 값을 테인트 처리하세요.
  * **[서버 액션](https://nextjs.org/docs/app/getting-started/updating-data):** 사용자가 서버 액션을 호출할 권한이 있는지 확인하고 [보안 모범 사례](https://nextjs.org/blog/security-nextjs-server-components-actions)를 검토하세요.


  * **[환경 변수](https://nextjs.org/docs/app/guides/environment-variables):** `.env.*` 파일을 `.gitignore`에 추가하고, 공개 변수만 `NEXT_PUBLIC_` 접두사를 사용하도록 하세요.
  * **[콘텐츠 보안 정책](https://nextjs.org/docs/app/guides/content-security-policy):** 크로스 사이트 스크립팅, 클릭재킹 등 각종 코드 주입 공격으로부터 애플리케이션을 보호하기 위해 콘텐츠 보안 정책 도입을 고려하세요.



### 메타데이터와 SEO[](https://nextjs.org/docs/app/guides/production-checklist#metadata-and-seo)

  * **[메타데이터 API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images):** 페이지 제목, 설명 등을 추가해 메타데이터 API로 애플리케이션 SEO를 개선하세요.
  * **[오픈 그래프(OG) 이미지](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image):** 소셜 공유 대비를 위해 OG 이미지를 생성하세요.
  * **[사이트맵](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps) 및 [Robots](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots):** 사이트맵과 robots 파일을 생성해 검색 엔진이 페이지를 크롤링하고 인덱싱하기 쉽게 만드세요.



### 타입 안정성[](https://nextjs.org/docs/app/guides/production-checklist#type-safety)

  * **TypeScript 및 [TS 플러그인](https://nextjs.org/docs/app/api-reference/config/typescript):** TypeScript와 TypeScript 플러그인을 사용해 타입 안정성을 높이고 오류를 더 일찍 포착하세요.



## 프로덕션 이전[](https://nextjs.org/docs/app/guides/production-checklist#before-going-to-production)

프로덕션 배포 전에 `next build`를 실행해 로컬에서 애플리케이션을 빌드하고 빌드 오류를 잡은 뒤, `next start`로 프로덕션과 유사한 환경에서 성능을 측정할 수 있습니다.

### 코어 웹 바이탈[](https://nextjs.org/docs/app/guides/production-checklist#core-web-vitals)

  * **[Lighthouse](https://developers.google.com/web/tools/lighthouse):** 시크릿 모드에서 Lighthouse를 실행해 사용자가 사이트를 어떻게 경험하는지 파악하고 개선 영역을 찾으세요. 이는 시뮬레이션 테스트이므로 코어 웹 바이탈 같은 필드 데이터와 함께 확인해야 합니다.


  * **[`useReportWebVitals` 훅](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals):** 이 훅을 사용해 [코어 웹 바이탈](https://web.dev/articles/vitals) 데이터를 분석 도구로 전송하세요.



### 번들 분석[](https://nextjs.org/docs/app/guides/production-checklist#analyzing-bundles)

[`@next/bundle-analyzer` plugin](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)을 사용하여 JavaScript 번들의 크기를 분석하고 애플리케이션 성능에 영향을 줄 수 있는 큰 모듈과 의존성을 식별하세요.

또한 아래 도구들은 새 의존성을 애플리케이션에 추가할 때의 영향을 이해하는 데 도움을 줍니다:

  * [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
  * [Package Phobia](https://packagephobia.com/)
  * [Bundle Phobia](https://bundlephobia.com/)
  * [bundlejs](https://bundlejs.com/)



도움이 되었나요?

지원됨.

보내기
