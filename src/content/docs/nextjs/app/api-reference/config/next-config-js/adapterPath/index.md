---
title: 'next.config.js: experimental.adapterPath'
description: 'Next.js는 빌드 프로세스에 연결할 수 있는 커스텀 어댑터를 만들 수 있도록 실험적 API를 제공합니다. 이는 Next.js 구성을 수정하거나 빌드 결과물을 처리해야 하는 배포 플랫폼이나 커스텀 빌드 통합에서 유용합니다.'
---

# next.config.js: experimental.adapterPath | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath

Copy page

# experimental.adapterPath

마지막 업데이트: 2026년 2월 20일

Next.js는 빌드 프로세스에 연결할 수 있는 커스텀 어댑터를 만들 수 있도록 실험적 API를 제공합니다. 이는 Next.js 구성을 수정하거나 빌드 결과물을 처리해야 하는 배포 플랫폼이나 커스텀 빌드 통합에서 유용합니다.

## 구성[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#configuration)

어댑터를 사용하려면 `experimental.adapterPath`에 어댑터 모듈 경로를 지정합니다:

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        adapterPath: require.resolve('./my-adapter.js'),
      },
    }

    module.exports = nextConfig
[/code]

## 어댑터 생성[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#creating-an-adapter)

어댑터는 `NextAdapter` 인터페이스를 구현하는 객체를 내보내는 모듈입니다:
[code]
    export interface NextAdapter {
      name: string
      modifyConfig?: (
        config: NextConfigComplete,
        ctx: {
          phase: PHASE_TYPE
        }
      ) => Promise<NextConfigComplete> | NextConfigComplete
      onBuildComplete?: (ctx: {
        routes: {
          headers: Array<ManifestHeaderRoute>
          redirects: Array<ManifestRedirectRoute>
          rewrites: {
            beforeFiles: Array<ManifestRewriteRoute>
            afterFiles: Array<ManifestRewriteRoute>
            fallback: Array<ManifestRewriteRoute>
          }
          dynamicRoutes: ReadonlyArray<ManifestRoute>
        }
        outputs: AdapterOutputs
        projectDir: string
        repoRoot: string
        distDir: string
        config: NextConfigComplete
        nextVersion: string
      }) => Promise<void> | void
    }
[/code]

### 기본 어댑터 구조[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#basic-adapter-structure)

다음은 최소한의 어댑터 예제입니다:

my-adapter.js
[code]
    /** @type {import('next').NextAdapter} */
    const adapter = {
      name: 'my-custom-adapter',

      async modifyConfig(config, { phase }) {
        // Modify the Next.js config based on the build phase
        if (phase === 'phase-production-build') {
          return {
            ...config,
            // Add your modifications
          }
        }
        return config
      },

      async onBuildComplete({
        routes,
        outputs,
        projectDir,
        repoRoot,
        distDir,
        config,
        nextVersion,
      }) {
        // Process the build output
        console.log('Build completed with', outputs.pages.length, 'pages')

        // Access different output types
        for (const page of outputs.pages) {
          console.log('Page:', page.pathname, 'at', page.filePath)
        }

        for (const apiRoute of outputs.pagesApi) {
          console.log('API Route:', apiRoute.pathname, 'at', apiRoute.filePath)
        }

        for (const appPage of outputs.appPages) {
          console.log('App Page:', appPage.pathname, 'at', appPage.filePath)
        }

        for (const prerender of outputs.prerenders) {
          console.log('Prerendered:', prerender.pathname)
        }
      },
    }

    module.exports = adapter
[/code]

## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#api-reference)

### `modifyConfig(config, context)`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#modifyconfigconfig-context)

구성을 수정할 수 있도록 next.config를 로드하는 모든 CLI 명령에서 호출됩니다.

**매개변수:**

  * `config`: 전체 Next.js 구성 객체
  * `context.phase`: 현재 빌드 단계([phases](https://nextjs.org/docs/app/api-reference/config/next-config-js#phase) 참고)

**반환값:** 수정된 구성 객체(비동기 가능)

### `onBuildComplete(context)`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#onbuildcompletecontext)

빌드 프로세스가 완료된 후 라우트와 출력에 대한 세부 정보를 포함해 호출됩니다.

**매개변수:**

  * `routes`: 헤더, 리디렉트, 리라이트, 동적 라우트에 대한 매니페스트를 포함한 객체
    * `routes.headers`: `source`, `sourceRegex`, `headers`, `has`, `missing`, 선택적 `priority` 필드를 가진 헤더 라우트 객체 배열
    * `routes.redirects`: `source`, `sourceRegex`, `destination`, `statusCode`, `has`, `missing`, 선택적 `priority` 필드를 가진 리디렉트 라우트 객체 배열
    * `routes.rewrites`: `beforeFiles`, `afterFiles`, `fallback` 배열을 포함하는 객체로, 각 배열에는 `source`, `sourceRegex`, `destination`, `has`, `missing` 필드를 가진 리라이트 라우트 객체가 있음
    * `routes.dynamicRoutes`: `source`, `sourceRegex`, `destination`, `has`, `missing` 필드를 가진 동적 라우트 객체 배열
  * `outputs`: 유형별로 구성된 모든 빌드 출력에 대한 세부 정보
  * `projectDir`: Next.js 프로젝트 디렉터리에 대한 절대 경로
  * `repoRoot`: 감지된 리포지토리 루트의 절대 경로
  * `distDir`: 빌드 출력 디렉터리의 절대 경로
  * `config`: `modifyConfig` 적용 이후의 최종 Next.js 구성
  * `nextVersion`: 사용 중인 Next.js 버전
  * `buildId`: 현재 빌드의 고유 식별자

## 출력 유형[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#output-types)

`outputs` 객체에는 서로 다른 출력 유형의 배열이 포함됩니다:

### Pages (`outputs.pages`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#pages-outputspages)

`pages/` 디렉터리의 React 페이지:
[code]
    {
      type: 'PAGES'
      id: string           // Route identifier
      filePath: string     // Path to the built file
      pathname: string     // URL pathname
      sourcePage: string   // Original source file path in pages/ directory
      runtime: 'nodejs' | 'edge'
      assets: Record<string, string>  // Traced dependencies (key: relative path from repo root, value: absolute path)
      wasmAssets?: Record<string, string>  // Bundled wasm files (key: name, value: absolute path)
      config: {
        maxDuration?: number
        preferredRegion?: string | string[]
        env?: Record<string, string>  // Environment variables (edge runtime only)
      }
    }
[/code]

### API Routes (`outputs.pagesApi`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#api-routes-outputspagesapi)

`pages/api/`의 API 라우트:
[code]
    {
      type: 'PAGES_API'
      id: string
      filePath: string
      pathname: string
      sourcePage: string   // Original relative source file path
      runtime: 'nodejs' | 'edge'
      assets: Record<string, string>
      wasmAssets?: Record<string, string>
      config: {
        maxDuration?: number
        preferredRegion?: string | string[]
        env?: Record<string, string>
      }
    }
[/code]

### App Pages (`outputs.appPages`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#app-pages-outputsapppages)

`app/` 디렉터리의 `page.{js,ts,jsx,tsx}` React 페이지:
[code]
    {
      type: 'APP_PAGE'
      id: string
      filePath: string
      pathname: string     // Includes .rsc suffix for RSC routes
      sourcePage: string   // Original relative source file path
      runtime: 'nodejs' | 'edge'
      assets: Record<string, string>
      wasmAssets?: Record<string, string>
      config: {
        maxDuration?: number
        preferredRegion?: string | string[]
        env?: Record<string, string>
      }
    }
[/code]

### App Routes (`outputs.appRoutes`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#app-routes-outputsapproutes)

`app/`의 `route.{js,ts,jsx,tsx}` API 및 메타데이터 라우트:
[code]
    {
      type: 'APP_ROUTE'
      id: string
      filePath: string
      pathname: string
      sourcePage: string
      runtime: 'nodejs' | 'edge'
      assets: Record<string, string>
      wasmAssets?: Record<string, string>
      config: {
        maxDuration?: number
        preferredRegion?: string | string[]
        env?: Record<string, string>
      }
    }
[/code]

### Prerenders (`outputs.prerenders`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#prerenders-outputsprerenders)

ISR 사용 라우트와 정적 프리렌더:
[code]
    {
      type: 'PRERENDER'
      id: string
      pathname: string
      parentOutputId: string  // ID of the source page/route
      groupId: number        // Revalidation group identifier (prerenders with same groupId revalidate together)
      pprChain?: {
        headers: Record<string, string>  // PPR chain headers (e.g., 'x-nextjs-resume': '1')
      }
      parentFallbackMode?: 'blocking' | false | null  // Fallback mode from getStaticPaths
      fallback?: {
        filePath: string
        initialStatus?: number
        initialHeaders?: Record<string, string | string[]>
        initialExpiration?: number
        initialRevalidate?: number
        postponedState?: string  // PPR postponed state
      }
      config: {
        allowQuery?: string[]     // Allowed query parameters
        allowHeader?: string[]    // Allowed headers for ISR
        bypassFor?: RouteHas[]    // Cache bypass conditions
        renderingMode?: RenderingMode
        bypassToken?: string
      }
    }
[/code]

### Static Files (`outputs.staticFiles`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#static-files-outputsstaticfiles)

정적 에셋과 자동 정적 최적화 페이지:
[code]
    {
      type: 'STATIC_FILE'
      id: string
      filePath: string
      pathname: string
    }
[/code]

### Middleware (`outputs.middleware`)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#middleware-outputsmiddleware)

미들웨어 함수(있는 경우):
[code]
    {
      type: 'MIDDLEWARE'
      id: string
      filePath: string
      pathname: string      // Always '/_middleware'
      sourcePage: string    // Always 'middleware'
      runtime: 'nodejs' | 'edge'
      assets: Record<string, string>
      wasmAssets?: Record<string, string>
      config: {
        maxDuration?: number
        preferredRegion?: string | string[]
        env?: Record<string, string>
        matchers?: Array<{
          source: string
          sourceRegex: string
          has: RouteHas[] | undefined
          missing: RouteHas[] | undefined
        }>
      }
    }
[/code]

## 라우트 정보[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#routes-information)

`onBuildComplete`의 `routes` 객체는 배포 준비가 된 처리된 패턴을 포함한 완전한 라우팅 정보를 제공합니다:

### Headers[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#headers)

각 헤더 라우트에는 다음이 포함됩니다:

  * `source`: 원본 라우트 패턴(예: `/about`)
  * `sourceRegex`: 요청을 매칭하기 위한 컴파일된 정규식
  * `headers`: 적용할 헤더의 키-값 쌍
  * `has`: 충족되어야 하는 선택적 조건
  * `missing`: 충족되지 않아야 하는 선택적 조건
  * `priority`: 내부 라우트용 선택적 플래그

### Redirects[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#redirects)

각 리디렉트 라우트에는 다음이 포함됩니다:

  * `source`: 원본 라우트 패턴
  * `sourceRegex`: 매칭을 위한 컴파일된 정규식
  * `destination`: 캡처 그룹을 포함할 수 있는 대상 URL
  * `statusCode`: HTTP 상태 코드(301, 302, 307, 308)

* `has`: 선택적 긍정 조건
  * `missing`: 선택적 부정 조건
  * `priority`: 내부 라우트를 위한 선택적 플래그

### 재작성(Rewrites)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#rewrites)

Rewrites는 세 단계로 구분됩니다:

  * `beforeFiles`: 파일 시스템(페이지 및 public 파일 포함)보다 먼저 확인
  * `afterFiles`: 페이지/공용 파일 이후, 동적 라우트 이전에 확인
  * `fallback`: 다른 모든 라우트 이후에 확인

각 rewrite에는 `source`, `sourceRegex`, `destination`, `has`, `missing`이 포함됩니다.

### 동적 라우트(Dynamic Routes)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#dynamic-routes)

동적 라우트 세그먼트(예: `[slug]`, `[...path]`)로부터 생성됩니다. 각 항목에는 다음이 포함됩니다:

  * `source`: 라우트 패턴
  * `sourceRegex`: 명명된 캡처 그룹이 있는 컴파일된 정규식
  * `destination`: 매개변수 치환이 적용된 내부 대상
  * `has`: 선택적 긍정 조건
  * `missing`: 선택적 부정 조건

## 사용 사례[](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath#use-cases)

어댑터의 일반적인 사용 사례는 다음과 같습니다:

  * **배포 플랫폼 통합** : 특정 호스팅 플랫폼에 맞춰 빌드 출력을 자동 구성
  * **에셋 처리** : 빌드 출력을 변환하거나 최적화
  * **모니터링 통합** : 빌드 메트릭과 라우트 정보를 수집
  * **맞춤 번들링** : 플랫폼별 형식으로 출력물 패키징
  * **빌드 검증** : 출력물이 특정 요구 사항을 충족하는지 확인
  * **라우트 생성** : 처리된 라우트 정보를 통해 플랫폼별 라우팅 구성을 생성

보내기
