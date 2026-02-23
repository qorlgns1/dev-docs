---
title: '구성: next.config.js 옵션'
description: 'Next.js는 프로젝트 디렉터리 루트(예:  옆)에 있는  파일의 기본 내보내기를 통해 구성할 수 있습니다.'
---

# 구성: next.config.js 옵션 | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js

[API Reference](https://nextjs.org/docs/pages/api-reference)[Configuration](https://nextjs.org/docs/pages/api-reference/config)next.config.js Options

Copy page

# next.config.js Options

마지막 업데이트: 2026년 2월 20일

Next.js는 프로젝트 디렉터리 루트(예: `package.json` 옆)에 있는 `next.config.js` 파일의 기본 내보내기를 통해 구성할 수 있습니다.

next.config.js
[code]
    // @ts-check

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }

    module.exports = nextConfig
[/code]

## ECMAScript Modules[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#ecmascript-modules)

`next.config.js`는 JSON 파일이 아닌 일반 Node.js 모듈입니다. Next.js 서버와 빌드 단계에서 사용되며 브라우저 빌드에는 포함되지 않습니다.

[ECMAScript modules](https://nodejs.org/api/esm.html)이 필요하다면 `next.config.mjs`를 사용할 수 있습니다:

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

> **참고 사항**: `.cjs` 또는 `.cts` 확장자를 가진 `next.config`는 현재 지원되지 않습니다.

## 함수 형태의 구성[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#configuration-as-a-function)

함수도 사용할 수 있습니다:

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

### 비동기 구성[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#async-configuration)

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

### Phase[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#phase)

`phase`는 구성이 로드되는 현재 컨텍스트입니다. [사용 가능한 모든 phase](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23)를 확인할 수 있습니다. phase는 `next/constants`에서 가져올 수 있습니다:

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

## TypeScript[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#typescript)

프로젝트에서 TypeScript를 사용하는 경우 구성에 TypeScript를 적용하기 위해 `next.config.ts`를 사용할 수 있습니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      /* config options here */
    }

    export default nextConfig
[/code]

주석 처리된 줄은 `next.config.js`에서 허용되는 구성(이 [파일](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts)에 정의됨)을 배치할 수 있는 위치입니다.

그러나 어떤 구성도 필수는 아니며, 각 구성이 무엇을 하는지 모두 이해할 필요도 없습니다. 대신 이 섹션에서 활성화하거나 수정하려는 기능을 검색하면 필요한 조치를 안내합니다.

> 대상 Node.js 버전에서 사용할 수 없는 새로운 JavaScript 기능 사용은 피하세요. `next.config.js`는 Webpack이나 Babel이 파싱하지 않습니다.

이 페이지는 사용 가능한 모든 구성 옵션을 문서화합니다:

## 단위 테스트(실험적)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#unit-testing-experimental)

Next.js 15.1부터 `next/experimental/testing/server` 패키지는 `next.config.js` 파일 유닛 테스트에 도움이 되는 유틸리티를 제공합니다.

`unstable_getResponseFromNextConfig` 함수는 제공된 요청 정보를 사용해 `next.config.js`의 [`headers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers), [`redirects`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects), [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) 함수를 실행하고 라우팅 결과가 담긴 `NextResponse`를 반환합니다.

> `unstable_getResponseFromNextConfig`의 응답은 `next.config.js` 필드만 고려하며 프록시 또는 파일 시스템 라우트는 고려하지 않으므로, 프로덕션 결과가 유닛 테스트와 다를 수 있습니다.
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

- [experimental.adapterPath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath)
  - Next.js가 빌드 프로세스에 hook될 수 있도록 modifyConfig 및 buildComplete 콜백으로 사용자 지정 어댑터를 구성합니다.
- [allowedDevOrigins](https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
  - `allowedDevOrigins`를 사용해 개발 서버에 요청할 수 있는 추가 origin을 구성합니다.
- [assetPrefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)
  - CDN을 구성하기 위해 assetPrefix 설정 옵션을 사용하는 방법을 살펴봅니다.
- [basePath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)
  - `basePath`를 사용해 도메인의 하위 경로에 Next.js 애플리케이션을 배포합니다.
- [bundlePagesRouterDependencies](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
  - Pages Router용 자동 종속성 번들을 활성화합니다.
- [compress](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress)
  - Next.js는 서버 타깃일 때만 작동하는 gzip 압축을 제공하여 렌더링된 콘텐츠와 정적 파일을 압축합니다. 자세한 내용을 확인하세요.
- [crossOrigin](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin)
  - `next/script` 및 `next/head`가 생성하는 `script` 태그에 crossOrigin 태그를 추가하려면 `crossOrigin` 옵션을 사용합니다.
- [deploymentId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId)
  - 버전 스큐 보호와 캐시 무효화를 위해 사용되는 배포 식별자를 구성합니다.
- [devIndicators](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators)
  - 정적으로 최적화 중인지 알려 주는 인디케이터가 최적화된 페이지에 포함됩니다. 여기에서 옵트아웃할 수 있습니다.
- [distDir](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir)
  - 기본 .next 디렉터리 대신 사용할 사용자 지정 빌드 디렉터리를 설정합니다.
- [env](https://nextjs.org/docs/pages/api-reference/config/next-config-js/env)
  - 빌드 시점에 Next.js 애플리케이션에서 환경 변수를 추가하고 액세스하는 방법을 배웁니다.
- [exportPathMap](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap)
  - `next export`를 사용할 때 HTML 파일로 내보낼 페이지를 사용자 지정합니다.
- [generateBuildId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)
  - 애플리케이션이 제공되는 현재 빌드를 식별하는 build id를 구성합니다.
- [generateEtags](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags)
  - Next.js는 기본적으로 모든 페이지에 대한 etag를 생성합니다. etag 생성을 비활성화하는 방법을 알아보세요.
- [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
  - Next.js 앱에 사용자 지정 HTTP 헤더를 추가합니다.
- [httpAgentOptions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
  - Next.js는 기본적으로 HTTP Keep-Alive를 사용합니다. HTTP Keep-Alive를 비활성화하는 방법을 알아보세요.
- [images](https://nextjs.org/docs/pages/api-reference/config/next-config-js/images)
  - next/image 로더에 대한 사용자 지정 구성을 설정합니다.
- [isolatedDevBuild](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild)
  - 프로덕션 빌드와 충돌하지 않도록 개발 빌드에 격리된 디렉터리를 사용합니다.
- [onDemandEntries](https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries)
  - 개발 중 생성된 페이지를 Next.js가 메모리에 유지하거나 폐기하는 방식을 구성합니다.
- [optimizePackageImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
  - optimizePackageImports Next.js 구성 옵션에 대한 API 레퍼런스입니다.
- [output](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)
  - Next.js는 각 페이지에 필요한 파일을 자동으로 추적하여 애플리케이션 배포를 쉽게 합니다. 동작 방식을 알아보세요.
- [pageExtensions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)
  - Pages Router에서 페이지를 확인할 때 사용되는 기본 페이지 확장자를 확장합니다.
- [poweredByHeader](https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader)
  - Next.js는 기본적으로 `x-powered-by` 헤더를 추가합니다. 여기에서 옵트아웃하는 방법을 알아보세요.
- [productionBrowserSourceMaps](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
  - 프로덕션 빌드 중 브라우저 소스맵 생성을 활성화합니다.
- [experimental.proxyClientMaxBodySize](https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize)
  - 프록시를 사용할 때 최대 요청 본문 크기를 구성합니다.
- [reactStrictMode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)
  - 이제 전체 Next.js 런타임이 Strict Mode를 준수합니다. 옵트인하는 방법을 확인하세요.
- [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
  - Next.js 앱에 리디렉션을 추가합니다.
- [rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
  - Next.js 앱에 리라이트를 추가합니다.
- [serverExternalPackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
  - `bundlePagesRouterDependencies`로 활성화된 종속성 번들링에서 특정 종속성을 옵트아웃합니다.
- [trailingSlash](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash)
  - Next.js 페이지가 슬래시 유무에 따라 해석되도록 구성합니다.
- [transpilePackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages)
  - 로컬 패키지(모노레포 등)나 외부 종속성(`node_modules`)에서 가져온 종속성을 자동으로 트랜스파일하고 번들링합니다.
- [turbopack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack)
  - Turbopack 전용 옵션으로 Next.js를 구성합니다.
- [typescript](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript)
  - Next.js는 기본적으로 TypeScript 오류를 보고합니다. 이 동작을 옵트아웃하는 방법을 알아보세요.
- [urlImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports)
  - 외부 URL에서 모듈을 가져올 수 있도록 Next.js를 구성합니다.
- [useLightningcss](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss)
  - Lightning CSS에 대한 실험적 지원을 활성화합니다.
- [webpack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack)
  - Next.js가 사용하는 webpack 구성을 사용자 지정하는 방법을 알아보세요.
- [webVitalsAttribution](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)
  - Web Vitals 문제의 근원을 파악하기 위해 webVitalsAttribution 옵션을 사용하는 방법을 알아봅니다.

보내기
