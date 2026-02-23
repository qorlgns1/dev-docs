---
title: '가이드: 프로덕션'
description: 'Next.js 애플리케이션을 프로덕션에 배포하기 전, 최상의 사용자 경험·성능·보안을 위해 적용을 고려해야 하는 최적화와 패턴이 있습니다.'
---

# 가이드: 프로덕션 | Next.js

소스 URL: https://nextjs.org/docs/pages/guides/production-checklist

# 프로덕션용 Next.js 애플리케이션 최적화 방법

마지막 업데이트 2026년 2월 20일

Next.js 애플리케이션을 프로덕션에 배포하기 전, 최상의 사용자 경험·성능·보안을 위해 적용을 고려해야 하는 최적화와 패턴이 있습니다.

이 문서는 [애플리케이션을 빌드할 때](https://nextjs.org/docs/pages/guides/production-checklist#during-development)와 [프로덕션 배포 이전에](https://nextjs.org/docs/pages/guides/production-checklist#before-going-to-production) 참고할 수 있는 모범 사례, 그리고 알아두면 좋은 [자동 Next.js 최적화](https://nextjs.org/docs/pages/guides/production-checklist#automatic-optimizations)를 제공합니다.

## 자동 최적화[](https://nextjs.org/docs/pages/guides/production-checklist#automatic-optimizations)

다음 Next.js 최적화는 기본 활성화되어 있으며 별도 설정이 필요 없습니다.

  * **[코드 스플리팅](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts):** Next.js는 페이지 단위로 애플리케이션 코드를 자동으로 분할해, 탐색 시 현재 페이지에 필요한 코드만 로드합니다. 필요에 따라 서드파티 라이브러리를 [지연 로딩](https://nextjs.org/docs/pages/guides/lazy-loading)하는 것도 고려하세요.
  * **[프리페칭](https://nextjs.org/docs/pages/api-reference/components/link#prefetch):** 사용자의 뷰포트에 새 라우트로 이동하는 링크가 들어오면 Next.js가 백그라운드에서 해당 라우트를 프리페치하여 거의 즉시 이동할 수 있게 합니다. 필요에 따라 프리페칭을 비활성화할 수 있습니다.
  * **[Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization):** 페이지에 차단되는 데이터 요구가 없으면 정적(사전 렌더링 가능) 페이지인지 자동으로 판별합니다. 최적화된 페이지는 캐싱되어 여러 CDN 지점에서 최종 사용자에게 제공될 수 있습니다. 필요할 경우 [Server-side Rendering](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)을 선택할 수 있습니다.

이러한 기본 설정은 애플리케이션 성능을 높이고 각 네트워크 요청에서 전송되는 데이터의 비용과 양을 줄이는 데 목적이 있습니다.

## 개발 중[](https://nextjs.org/docs/pages/guides/production-checklist#during-development)

애플리케이션을 빌드하는 동안 다음 기능을 사용해 최고의 성능과 사용자 경험을 확보하는 것이 좋습니다.

### 라우팅 및 렌더링[](https://nextjs.org/docs/pages/guides/production-checklist#routing-and-rendering)

  * **[`<Link>` 컴포넌트](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating):** 클라이언트 측 내비게이션과 프리페칭에는 `<Link>` 컴포넌트를 사용하세요.
  * **[커스텀 에러](https://nextjs.org/docs/pages/building-your-application/routing/custom-error):** [500](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page) 및 [404 에러](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)를 우아하게 처리하세요.

### 데이터 패칭 및 캐싱[](https://nextjs.org/docs/pages/guides/production-checklist#data-fetching-and-caching)

  * **[API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes):** Route Handler로 백엔드 리소스에 접근하고, 민감한 시크릿이 클라이언트에 노출되지 않도록 하세요.
  * **[데이터 캐싱](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props):** 데이터 요청이 캐시되고 있는지 확인하고, 필요에 따라 캐싱을 활성화하세요. `getStaticProps`를 사용하지 않는 요청도 적절한 경우 캐시되도록 해야 합니다.
  * **[Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration):** 전체 사이트를 다시 빌드하지 않고도 빌드 후 정적 페이지를 업데이트하려면 Incremental Static Regeneration을 사용하세요.
  * **[정적 이미지](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder):** `public` 디렉터리를 사용해 이미지 등 애플리케이션의 정적 자산을 자동으로 캐시하세요.

### UI 및 접근성[](https://nextjs.org/docs/pages/guides/production-checklist#ui-and-accessibility)

  * **[Font Module](https://nextjs.org/docs/app/api-reference/components/font):** Font Module을 사용해 폰트를 최적화하면 다른 정적 자산과 함께 자동 호스팅되고, 외부 네트워크 요청이 제거되며, [레이아웃 시프트](https://web.dev/articles/cls)가 줄어듭니다.
  * **[`<Image>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/image):** Image 컴포넌트를 사용하면 이미지를 자동 최적화하고, 레이아웃 시프트를 방지하며 WebP 같은 최신 포맷으로 제공할 수 있습니다.
  * **[`<Script>` 컴포넌트](https://nextjs.org/docs/app/guides/scripts):** Script 컴포넌트를 사용해 서드파티 스크립트를 최적화하면 스크립트가 자동으로 지연 실행되어 메인 스레드를 차단하지 않습니다.
  * **[ESLint](https://nextjs.org/docs/architecture/accessibility#linting):** 내장된 `eslint-plugin-jsx-a11y` 플러그인으로 접근성 이슈를 조기에 감지하세요.

### 보안[](https://nextjs.org/docs/pages/guides/production-checklist#security)

  * **[환경 변수](https://nextjs.org/docs/app/guides/environment-variables):** `.env.*` 파일을 `.gitignore`에 추가하고, 공개 변수에만 `NEXT_PUBLIC_` 접두사를 붙이세요.
  * **[콘텐츠 보안 정책](https://nextjs.org/docs/app/guides/content-security-policy):** 콘텐츠 보안 정책을 추가해 크로스 사이트 스크립팅, 클릭재킹, 기타 코드 주입 공격 등 여러 보안 위협으로부터 애플리케이션을 보호하는 것을 고려하세요.

### 메타데이터와 SEO[](https://nextjs.org/docs/pages/guides/production-checklist#metadata-and-seo)

  * **[`<Head>` 컴포넌트](https://nextjs.org/docs/pages/api-reference/components/head):** `next/head` 컴포넌트를 사용해 페이지 제목, 설명 등 메타데이터를 추가하세요.

### 타입 안전성[](https://nextjs.org/docs/pages/guides/production-checklist#type-safety)

  * **TypeScript와 [TS Plugin](https://nextjs.org/docs/app/api-reference/config/typescript):** 타입 안전성을 강화하고 오류를 조기에 포착하기 위해 TypeScript와 TypeScript 플러그인을 사용하세요.

## 프로덕션 배포 전[](https://nextjs.org/docs/pages/guides/production-checklist#before-going-to-production)

프로덕션에 배포하기 전 `next build`를 실행해 로컬에서 애플리케이션을 빌드하고 빌드 오류를 확인한 다음, `next start`를 실행해 프로덕션과 유사한 환경에서 애플리케이션 성능을 측정할 수 있습니다.

### 코어 웹 바이탈[](https://nextjs.org/docs/pages/guides/production-checklist#core-web-vitals)

  * **[Lighthouse](https://developers.google.com/web/tools/lighthouse):** 시크릿 모드에서 Lighthouse를 실행해 사용자가 사이트를 어떻게 경험하는지 더 잘 이해하고 개선할 영역을 파악하세요. 이는 시뮬레이션 테스트이므로 Core Web Vitals 같은 필드 데이터와 함께 확인해야 합니다.

### 번들 분석[](https://nextjs.org/docs/pages/guides/production-checklist#analyzing-bundles)

[`@next/bundle-analyzer` 플러그인](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)을 사용해 JavaScript 번들의 크기를 분석하고 애플리케이션 성능에 영향을 줄 수 있는 대형 모듈과 의존성을 식별하세요.

또한 다음 도구들은 새로운 의존성을 추가할 때 애플리케이션에 미치는 영향을 이해하는 데 도움이 됩니다.

  * [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
  * [Package Phobia](https://packagephobia.com/)
  * [Bundle Phobia](https://bundlephobia.com/)
  * [bundlejs](https://bundlejs.com/)
