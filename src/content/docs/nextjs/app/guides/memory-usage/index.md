---
title: '가이드: 메모리 사용량'
description: '애플리케이션이 성장하고 기능이 풍부해질수록 로컬 개발이나 프로덕션 빌드 시 더 많은 리소스를 요구할 수 있습니다.'
---

# 가이드: 메모리 사용량 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/memory-usage

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)메모리 사용량

페이지 복사

# 메모리 사용량 최적화 방법

최종 업데이트 2026년 2월 20일

애플리케이션이 성장하고 기능이 풍부해질수록 로컬 개발이나 프로덕션 빌드 시 더 많은 리소스를 요구할 수 있습니다.

Next.js에서 메모리를 최적화하고 일반적인 메모리 문제를 해결하는 전략과 기법을 살펴봅니다.

## 종속성 수 줄이기[](https://nextjs.org/docs/app/guides/memory-usage#reduce-number-of-dependencies)

많은 수의 종속성을 가진 애플리케이션은 더 많은 메모리를 사용합니다.

[번들 분석기](https://nextjs.org/docs/app/guides/package-bundling)는 애플리케이션에서 제거해 성능과 메모리 사용량을 개선할 수 있는 대형 종속성을 조사하는 데 도움이 됩니다.

## `experimental.webpackMemoryOptimizations` 사용해 보기[](https://nextjs.org/docs/app/guides/memory-usage#try-experimentalwebpackmemoryoptimizations)

`v15.0.0`부터는 `next.config.js` 파일에 `experimental.webpackMemoryOptimizations: true`를 추가해 Webpack의 동작을 변경할 수 있으며, 최대 메모리 사용량을 줄이는 대신 컴파일 시간이 소폭 늘어날 수 있습니다.

> **참고**: 이 기능은 더 많은 프로젝트에서 시험해 보기 위한 실험 단계이지만, 위험도는 낮다고 판단됩니다.

## `--experimental-debug-memory-usage`와 함께 `next build` 실행하기[](https://nextjs.org/docs/app/guides/memory-usage#run-next-build-with---experimental-debug-memory-usage)

`14.2.0`부터는 `next build --experimental-debug-memory-usage`를 실행해 빌드 전체에 걸쳐 힙 사용량과 가비지 컬렉션 통계 같은 메모리 정보를 지속적으로 출력하는 모드로 빌드를 실행할 수 있습니다. 구성한 한계에 가까워지면 힙 스냅샷도 자동으로 생성됩니다.

> **참고**: 이 기능은 커스텀 Webpack 구성이 없는 한 자동으로 활성화되는 Webpack 빌드 워커 옵션과 호환되지 않습니다.

## 힙 프로파일 기록하기[](https://nextjs.org/docs/app/guides/memory-usage#record-a-heap-profile)

메모리 문제를 찾기 위해 Node.js에서 힙 프로파일을 기록하고 Chrome DevTools에서 로드해 잠재적인 메모리 누수 원인을 확인할 수 있습니다.

터미널에서 Next.js 빌드를 시작할 때 Node.js에 `--heap-prof` 플래그를 전달하세요:
[code] 
    node --heap-prof node_modules/next/dist/bin/next build
[/code]

빌드가 끝나면 Node.js가 `.heapprofile` 파일을 생성합니다.

Chrome DevTools에서 Memory 탭을 열고 "Load Profile" 버튼을 클릭하면 파일을 시각화할 수 있습니다.

## 힙 스냅샷 분석하기[](https://nextjs.org/docs/app/guides/memory-usage#analyze-a-snapshot-of-the-heap)

인스펙터 도구를 사용해 애플리케이션의 메모리 사용량을 분석할 수 있습니다.

`next build` 또는 `next dev` 명령을 실행할 때 명령 앞에 `NODE_OPTIONS=--inspect`를 추가하세요. 이 작업으로 기본 포트에서 인스펙터 에이전트를 노출합니다. 사용자 코드가 시작되기 전에 중단하고 싶다면 `--inspect-brk`를 대신 전달할 수 있습니다. 프로세스가 실행 중일 때 Chrome DevTools 같은 도구로 디버깅 포트에 연결해 힙 스냅샷을 기록하고 분석해 어떤 메모리가 유지되는지 확인할 수 있습니다.

`14.2.0`부터는 `--experimental-debug-memory-usage` 플래그와 함께 `next build`를 실행해 힙 스냅샷을 더 쉽게 촬영할 수도 있습니다.

이 모드에서 실행 중에는 언제든 프로세스에 `SIGUSR2` 신호를 보내 힙 스냅샷을 촬영할 수 있습니다.

힙 스냅샷은 Next.js 애플리케이션의 프로젝트 루트에 저장되며 Chrome DevTools 등 어떤 힙 분석기에서도 로드해 유지 중인 메모리를 확인할 수 있습니다. 이 모드는 아직 Webpack 빌드 워커와 호환되지 않습니다.

자세한 내용은 [힙 스냅샷 기록 및 분석 방법](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)을 참고하세요.

## Webpack 빌드 워커[](https://nextjs.org/docs/app/guides/memory-usage#webpack-build-worker)

Webpack 빌드 워커는 별도의 Node.js 워커 내부에서 Webpack 컴파일을 실행해 빌드 중 애플리케이션의 메모리 사용량을 줄여 줍니다.

`v14.1.0`부터는 커스텀 Webpack 구성이 없다면 이 옵션이 기본으로 활성화됩니다.

오래된 Next.js 버전을 사용하거나 커스텀 Webpack 구성이 있는 경우 `next.config.js`에 `experimental.webpackBuildWorker: true`를 설정해 이 옵션을 활성화할 수 있습니다.

> **참고**: 이 기능은 모든 커스텀 Webpack 플러그인과 호환되지 않을 수 있습니다.

## Webpack 캐시 비활성화하기[](https://nextjs.org/docs/app/guides/memory-usage#disable-webpack-cache)

[Webpack 캐시](https://webpack.js.org/configuration/cache/)는 빌드 속도를 개선하기 위해 생성된 Webpack 모듈을 메모리나 디스크에 저장합니다. 성능에는 도움이 되지만 캐시 데이터를 저장하기 위해 애플리케이션의 메모리 사용량이 증가합니다.

애플리케이션에 [커스텀 Webpack 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)을 추가해 이 동작을 비활성화할 수 있습니다:

next.config.mjs
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      webpack: (
        config,
        { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
      ) => {
        if (config.cache && !dev) {
          config.cache = Object.freeze({
            type: 'memory',
          })
        }
        // Important: return the modified config
        return config
      },
    }
     
    export default nextConfig
[/code]

## 정적 분석 비활성화하기[](https://nextjs.org/docs/app/guides/memory-usage#disable-static-analysis)

대규모 프로젝트에서는 타입 검사에 많은 메모리가 필요할 수 있습니다. 그러나 대부분의 프로젝트는 이러한 작업을 처리하는 전용 CI 러너를 보유합니다. 빌드가 "Running TypeScript" 단계에서 메모리 부족 문제를 일으킨다면 빌드 중 이 작업을 비활성화할 수 있습니다:

next.config.mjs
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
     
    export default nextConfig
[/code]

  * [TypeScript 오류 무시하기](https://nextjs.org/docs/app/api-reference/config/typescript#disabling-typescript-errors-in-production)



이렇게 하면 타입 오류로 인해 잘못된 배포가 발생할 수 있다는 점을 기억하세요. 정적 분석이 완료된 뒤에만 빌드를 프로덕션으로 승격하는 것을 강력히 권장합니다. Vercel에 배포한다면 커스텀 작업이 완료된 후 빌드를 프로덕션으로 승격하는 방법을 알아보기 위해 [스테이징 배포 가이드](https://vercel.com/docs/deployments/managing-deployments#staging-and-promoting-a-production-deployment)를 확인하세요.

## 소스 맵 비활성화하기[](https://nextjs.org/docs/app/guides/memory-usage#disable-source-maps)

소스 맵을 생성하면 빌드 과정에서 추가 메모리를 소모합니다.

Next.js 구성에 `productionBrowserSourceMaps: false`와 `experimental.serverSourceMaps: false`를 추가해 소스 맵 생성을 비활성화할 수 있습니다.

`cacheComponents` 기능을 사용할 때 Next.js는 `next build`의 프리렌더 단계에서 기본적으로 소스 맵을 사용합니다. 해당 단계(“Generating static pages” 이후)에 메모리 문제가 지속된다면 `enablePrerenderSourceMaps: false`를 추가해 그 단계에서 소스 맵을 비활성화해 볼 수 있습니다.

> **참고**: 일부 플러그인은 소스 맵을 활성화하므로 비활성화하려면 커스텀 구성이 필요할 수 있습니다.

## 엣지 메모리 문제[](https://nextjs.org/docs/app/guides/memory-usage#edge-memory-issues)

Next.js `v14.1.3`에서는 Edge 런타임을 사용할 때의 메모리 문제가 수정되었습니다. 해당 버전 이상으로 업데이트해 문제가 해결되는지 확인하세요.

## 엔트리 미리 로드[](https://nextjs.org/docs/app/guides/memory-usage#preloading-entries)

Next.js 서버는 요청 시점이 아니라 시작 시 각 페이지의 JavaScript 모듈을 메모리에 미리 로드합니다.

이 최적화는 더 큰 초기 메모리 사용량과 맞바꾸는 대신 더 빠른 응답 시간을 제공합니다.

이 최적화를 비활성화하려면 `experimental.preloadEntriesOnStart` 플래그를 `false`로 설정하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      experimental: {
        preloadEntriesOnStart: false,
      },
    }
     
    export default config
[/code]

Next.js는 이러한 JavaScript 모듈을 언로드하지 않으므로, 이 최적화를 비활성화하더라도 모든 페이지에 결국 요청이 들어오면 Next.js 서버의 메모리 사용량은 결국 동일해집니다.

도움이 되었나요?

지원됨.

보내기
