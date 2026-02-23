---
title: '구성: next.config.js'
description: '최종 업데이트: 2026년 2월 20일'
---

# 구성: next.config.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js

# next.config.js

최종 업데이트: 2026년 2월 20일

Next.js는 프로젝트 디렉터리 루트(예: `package.json`)에 있는 `next.config.js` 파일의 기본 export를 통해 구성할 수 있습니다.

next.config.js
[code]
    // @ts-check

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }

    module.exports = nextConfig
[/code]

## ECMAScript 모듈[](https://nextjs.org/docs/app/api-reference/config/next-config-js#ecmascript-modules)

`next.config.js`는 일반적인 Node.js 모듈이며 JSON 파일이 아닙니다. Next.js 서버와 빌드 단계에서 사용되며 브라우저 빌드에는 포함되지 않습니다.

[ECMAScript 모듈](https://nodejs.org/api/esm.html)이 필요하다면 `next.config.mjs`를 사용할 수 있습니다:

next.config.mjs
[code]
    // @ts-check

    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
      /* config options here */
    }

    export default nextConfig
[/code]

> **알아두세요** : `.cjs` 또는 `.cts` 확장을 가진 `next.config`는 현재 지원되지 않습니다.

## 함수 형태의 구성[](https://nextjs.org/docs/app/api-reference/config/next-config-js#configuration-as-a-function)

함수를 사용할 수도 있습니다:

next.config.mjs
[code]
    // @ts-check

    export default (phase, { defaultConfig }) => {
      /**
       * @type {import('next').NextConfig}
       */
      const nextConfig = {
        /* config options here */
      }
      return nextConfig
    }
[/code]

### 비동기 구성[](https://nextjs.org/docs/app/api-reference/config/next-config-js#async-configuration)

Next.js 12.1.0부터는 비동기 함수를 사용할 수 있습니다:

next.config.js
[code]
    // @ts-check

    module.exports = async (phase, { defaultConfig }) => {
      /**
       * @type {import('next').NextConfig}
       */
      const nextConfig = {
        /* config options here */
      }
      return nextConfig
    }
[/code]

### 페이즈[](https://nextjs.org/docs/app/api-reference/config/next-config-js#phase)

`phase`는 구성이 로드되는 현재 컨텍스트입니다. 사용 가능한 [페이즈](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23)를 확인할 수 있습니다. 페이즈는 `next/constants`에서 import할 수 있습니다:

next.config.js
[code]
    // @ts-check

    const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')

    module.exports = (phase, { defaultConfig }) => {
      if (phase === PHASE_DEVELOPMENT_SERVER) {
        return {
          /* development only config options here */
        }
      }

      return {
        /* config options for all phases except development here */
      }
    }
[/code]

## TypeScript[](https://nextjs.org/docs/app/api-reference/config/next-config-js#typescript)

프로젝트에서 TypeScript를 사용 중이라면 `next.config.ts`를 통해 구성에 TypeScript를 적용할 수 있습니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      /* config options here */
    }

    export default nextConfig
[/code]

주석 처리된 줄은 `next.config.js`에서 허용되는 구성(이 [파일](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts)에 정의됨)을 넣을 수 있는 위치입니다.

그러나 어떤 구성도 필수는 아니며, 각 구성의 동작을 모두 이해할 필요도 없습니다. 대신 이 섹션에서 사용하거나 수정하려는 기능을 검색하면 필요한 작업을 안내받을 수 있습니다.

> 대상 Node.js 버전에서 제공되지 않는 새로운 JavaScript 기능 사용은 피하세요. `next.config.js`는 Webpack이나 Babel이 파싱하지 않습니다.

이 페이지는 사용 가능한 모든 구성 옵션을 문서화합니다:

## 단위 테스트(실험적)[](https://nextjs.org/docs/app/api-reference/config/next-config-js#unit-testing-experimental)

Next.js 15.1부터 `next/experimental/testing/server` 패키지는 `next.config.js` 파일의 단위 테스트를 돕는 유틸리티를 제공합니다.

`unstable_getResponseFromNextConfig` 함수는 제공된 요청 정보를 사용해 `next.config.js`의 [`headers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers), [`redirects`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects), [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) 함수를 실행하고 라우팅 결과가 담긴 `NextResponse`를 반환합니다.

> `unstable_getResponseFromNextConfig`의 응답은 `next.config.js` 필드만 고려하며 프록시나 파일 시스템 라우트는 고려하지 않으므로, 프로덕션의 결과가 단위 테스트와 다를 수 있습니다.
[code]
    import {
      getRedirectUrl,
      unstable_getResponseFromNextConfig,
    } from 'next/experimental/testing/server'

    const response = await unstable_getResponseFromNextConfig({
      url: 'https://nextjs.org/test',
      nextConfig: {
        async redirects() {
          return [{ source: '/test', destination: '/test2', permanent: false }]
        },
      },
    })
    expect(response.status).toEqual(307)
    expect(getRedirectUrl(response)).toEqual('https://nextjs.org/test2')
[/code]

- [experimental.adapterPath](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath)
  - Next.js의 빌드 프로세스에 `modifyConfig`와 `onBuildComplete` 콜백으로 훅을 거는 커스텀 어댑터를 구성합니다.
- [allowedDevOrigins](https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins)
  - 개발 서버에 요청할 수 있는 추가 오리진을 `allowedDevOrigins`로 설정합니다.
- [appDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)
  - App Router를 활성화해 레이아웃, 스트리밍 등 기능을 사용합니다.
- [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)
  - CDN 구성을 위해 `assetPrefix` 설정 옵션을 사용하는 방법을 알아봅니다.
- [authInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
  - 실험적 구성 옵션인 `authInterrupts`를 활성화해 `forbidden`과 `unauthorized`를 사용하는 방법을 알아봅니다.
- [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
  - 도메인의 하위 경로에 Next.js 애플리케이션을 배포하기 위해 `basePath`를 사용합니다.
- [browserDebugInfoInTerminal](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal)
  - 개발 중 브라우저 콘솔 로그와 오류를 터미널로 전달합니다.
- [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Next.js에서 `cacheComponents` 플래그를 활성화하는 방법을 알아봅니다.
- [cacheHandlers](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)
  - Next.js에서 cache 지시문에 사용할 커스텀 캐시 핸들러를 구성합니다.
- [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
  - Next.js에서 `cacheLife` 구성을 설정하는 방법을 알아봅니다.
- [compress](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress)
  - Next.js는 렌더링된 콘텐츠와 정적 파일에 gzip 압축을 제공하며 서버 타겟에서만 동작합니다. 여기에서 자세히 알아보세요.
- [crossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)
  - `next/script`가 생성하는 `script` 태그에 crossOrigin 태그를 추가하기 위해 `crossOrigin` 옵션을 사용합니다.
- [cssChunking](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking)
  - Next.js 애플리케이션에서 CSS 파일이 청크로 나뉘는 방식을 제어하려면 `cssChunking` 옵션을 사용합니다.
- [deploymentId](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId)
  - 버전 불일치 방지와 캐시 무효화를 위해 사용되는 배포 식별자를 구성합니다.
- [devIndicators](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)
  - 개발 중 현재 보고 있는 경로 정보를 제공하는 온스크린 인디케이터를 위한 구성 옵션입니다.
- [distDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)
  - 기본 `.next` 디렉터리 대신 사용할 커스텀 빌드 디렉터리를 설정합니다.
- [env](https://nextjs.org/docs/app/api-reference/config/next-config-js/env)
  - Next.js 애플리케이션에서 빌드 시 환경 변수를 추가하고 액세스하는 방법을 배웁니다.
- [expireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)
  - ISR이 활성화된 페이지의 `stale-while-revalidate` 만료 시간을 커스터마이즈합니다.
- [exportPathMap](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap)
  - `next export`를 사용할 때 HTML 파일로 내보낼 페이지를 커스터마이즈합니다.
- [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)
  - 애플리케이션이 제공되는 현재 빌드를 식별하는 빌드 ID를 구성합니다.
- [generateEtags](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags)
  - Next.js는 기본적으로 모든 페이지에 ETag를 생성합니다. 여기에서 ETag 생성을 비활성화하는 방법을 알아보세요.
- [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
  - Next.js 앱에 커스텀 HTTP 헤더를 추가합니다.
- [htmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
  - 차단 메타데이터를 받아야 하는 사용자 에이전트 목록을 지정합니다.
- [httpAgentOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions)
  - Next.js는 기본적으로 HTTP Keep-Alive를 사용합니다. 여기에서 HTTP Keep-Alive를 비활성화하는 방법을 알아보세요.
- [images](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
  - `next/image` 로더에 대한 커스텀 구성을 제공합니다.
- [cacheHandler](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
  - Next.js 캐시를 구성하여 Redis, Memcached 등 외부 서비스를 사용해 데이터를 저장하고 재검증합니다.
- [inlineCss](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss)
  - 인라인 CSS 지원을 활성화합니다.
- [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)
  - 프로덕션 빌드와의 충돌을 방지하기 위해 개발 서버에서 독립된 빌드 출력을 사용합니다.
- [logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)
  - 개발 모드에서 Next.js를 실행할 때 데이터 페치 로그 방식을 구성합니다.
- [mdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)
  - App Router에서 MDX 파일을 컴파일하기 위해 새로운 Rust 컴파일러를 사용합니다.
- [onDemandEntries](https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries)
  - 개발 중 생성된 페이지를 Next.js가 메모리에 유지하거나 폐기하는 방식을 구성합니다.
- [optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)
  - `optimizePackageImports` Next.js 설정 옵션에 대한 API 레퍼런스입니다.
- [output](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)
  - Next.js는 각 페이지에 필요한 파일을 자동 추적해 배포를 쉽게 합니다. 동작 방식은 여기에서 확인하세요.
- [pageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)
  - Pages Router에서 페이지를 해석할 때 사용하는 기본 페이지 확장자를 확장합니다.
- [poweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)
  - Next.js는 기본적으로 `x-powered-by` 헤더를 추가합니다. 여기에서 이를 옵트아웃하는 방법을 알아봅니다.
- [productionBrowserSourceMaps](https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
  - 프로덕션 빌드 중 브라우저 소스맵 생성을 활성화합니다.
- [proxyClientMaxBodySize](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)
  - 프록시를 사용할 때 최대 요청 본문 크기를 구성합니다.
- [reactCompiler](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler)
  - React Compiler를 활성화해 컴포넌트 렌더링을 자동으로 최적화합니다.
- [reactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
  - React가 응답에 추가하는 헤더의 최대 길이를 정의합니다.
- [reactStrictMode](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode)
  - 전체 Next.js 런타임이 Strict Mode를 준수하도록 설정하는 방법을 알아봅니다.
- [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
  - Next.js 앱에 리디렉션을 추가합니다.
- [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
  - Next.js 앱에 리라이트를 추가합니다.
- [sassOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions)
  - Sass 옵션을 구성합니다.
- [serverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
  - Next.js 애플리케이션에서 Server Actions 동작을 구성합니다.
- [serverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
  - Server Components에서 HMR 새로고침 요청 간 `fetch` 응답을 캐시할지 여부를 구성합니다.
- [serverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)
  - Server Components 번들에서 특정 의존성을 제외하고 기본 Node.js `require`를 사용합니다.
- [staleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
  - Client Router 캐시의 무효화 시간을 재정의하는 방법을 알아봅니다.
- [staticGeneration*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)
  - Next.js 애플리케이션에서 정적 생성을 구성하는 방법을 알아봅니다.
- [taint](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint)
  - 객체와 값을 더럽힘(tainting) 상태로 설정합니다.
- [trailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)
  - Next.js 페이지가 후행 슬래시 유무와 함께 해석되도록 구성합니다.
- [transpilePackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages)
  - 로컬 패키지(모노레포 등)나 외부 의존성(`node_modules`)의 종속성을 자동으로 트랜스파일하고 번들링합니다.
- [turbopack](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)
  - Turbopack 전용 옵션으로 Next.js를 구성합니다.
- [turbopackFileSystemCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)
  - Turbopack 빌드에 파일 시스템 캐싱을 활성화하는 방법을 알아봅니다.
- [typedRoutes](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)
  - 정적으로 타입이 지정된 링크 지원을 활성화합니다.
- [typescript](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript)
  - Next.js가 프로덕션 빌드 중 TypeScript 오류를 처리하는 방식과 커스텀 `tsconfig` 파일을 지정하는 방법을 구성합니다.
- [urlImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports)
  - 외부 URL에서 모듈을 가져오도록 Next.js를 구성합니다.
- [useLightningcss](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss)
  - Lightning CSS에 대한 실험적 지원을 활성화합니다.
- [viewTransition](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition)
  - App Router에서 React의 ViewTransition API를 활성화합니다.
- [webpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)
  - Next.js가 사용하는 webpack 구성을 커스터마이즈하는 방법을 알아봅니다.
- [webVitalsAttribution](https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution)
  - Web Vitals 문제의 원인을 정확히 찾아내기 위해 `webVitalsAttribution` 옵션을 사용하는 방법을 알아봅니다.

보내기
