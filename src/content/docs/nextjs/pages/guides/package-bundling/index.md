---
title: '가이드: 패키지 번들링'
description: '번들링은 애플리케이션 코드와 그 의존성을 클라이언트와 서버용으로 최적화된 출력 파일로 결합하는 과정입니다. 번들이 작을수록 로딩 속도가 빨라지고 JavaScript 실행 시간이 줄어들며 Core Web Vitals가 개선되고 서버 콜드 스타트 시간이 단축됩니다.'
---

# 가이드: 패키지 번들링 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/package-bundling

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Package Bundling

# 패키지 번들링 최적화 방법

최종 업데이트 2026년 2월 20일

번들링은 애플리케이션 코드와 그 의존성을 클라이언트와 서버용으로 최적화된 출력 파일로 결합하는 과정입니다. 번들이 작을수록 로딩 속도가 빨라지고 JavaScript 실행 시간이 줄어들며 [Core Web Vitals](https://web.dev/articles/vitals)가 개선되고 서버 콜드 스타트 시간이 단축됩니다.

Next.js는 코드 스플리팅, 트리 셰이킹 등 다양한 기법으로 자동 번들 최적화를 수행합니다. 하지만 상황에 따라 수동으로 번들을 최적화해야 할 때가 있습니다.

애플리케이션 번들을 분석하는 도구는 두 가지입니다.

  * [Next.js Bundle Analyzer for Turbopack(실험적)](https://nextjs.org/docs/pages/guides/package-bundling#nextjs-bundle-analyzer-experimental)
  * Webpack용 [`@next/bundle-analyzer` 플러그인](https://nextjs.org/docs/pages/guides/package-bundling#nextbundle-analyzer-for-webpack)

이 가이드는 각 도구 사용 방법과 [대형 번들 최적화](https://nextjs.org/docs/pages/guides/package-bundling#optimizing-large-bundles) 방법을 안내합니다.

## Next.js Bundle Analyzer (Experimental)[](https://nextjs.org/docs/pages/guides/package-bundling#nextjs-bundle-analyzer-experimental)

> v16.1 이상에서 사용 가능합니다. [전용 GitHub 토론](https://github.com/vercel/next.js/discussions/86731)에 피드백을 남기고 [turbopack-bundle-analyzer-demo.vercel.sh](https://turbopack-bundle-analyzer-demo.vercel.sh/)에서 데모를 확인할 수 있습니다.

Next.js Bundle Analyzer는 Turbopack의 모듈 그래프와 통합되어 있습니다. 정밀한 import 추적을 통해 서버 및 클라이언트 모듈을 살펴보고 큰 의존성을 쉽게 찾을 수 있습니다. 인터랙티브 Bundle Analyzer 데모를 열어 모듈 그래프를 탐색하세요.

### 1단계: Turbopack Bundle Analyzer 실행[](https://nextjs.org/docs/pages/guides/package-bundling#step-1-run-the-turbopack-bundle-analyzer)

다음 명령을 실행한 뒤 브라우저에서 인터랙티브 뷰를 열어 시작하세요.

pnpmnpmyarnbun

Terminal
```
    pnpm next experimental-analyze
```

### 2단계: 모듈 필터링 및 검사[](https://nextjs.org/docs/pages/guides/package-bundling#step-2-filter-and-inspect-modules)

UI에서 라우트, 환경(클라이언트 또는 서버), 유형(JavaScript, CSS, JSON)으로 필터링하거나 파일로 검색할 수 있습니다.

Next.js bundle analyzer UI 살펴보기

### 3단계: import 체인으로 모듈 추적[](https://nextjs.org/docs/pages/guides/package-bundling#step-3-trace-modules-with-import-chains)

트리맵은 각 모듈을 사각형으로 표시하며 면적이 모듈 크기를 나타냅니다.

모듈을 클릭하면 크기, 전체 import 체인, 애플리케이션에서 사용되는 위치를 확인할 수 있습니다.

Next.js Bundle Analyzer import 체인 보기

### 4단계: 공유 또는 비교를 위한 출력 저장[](https://nextjs.org/docs/pages/guides/package-bundling#step-4-write-output-to-disk-for-sharing-or-diffing)

분석 결과를 팀과 공유하거나 최적화 전후 번들 크기를 비교하려면 인터랙티브 뷰를 건너뛰고 `--output` 플래그로 정적 파일을 저장하세요.

pnpmnpmyarnbun

Terminal
```
    pnpm next experimental-analyze --output
```

이 명령은 출력물을 `.next/diagnostics/analyze`에 기록합니다. 결과를 비교하려면 이 디렉터리를 다른 위치로 복사하면 됩니다.

Terminal
```
    cp -r .next/diagnostics/analyze ./analyze-before-refactor
```

> Bundle Analyzer에는 더 많은 옵션이 있습니다. 전체 목록은 Next.js CLI 참조 문서를 확인하세요.

## Webpack용 `@next/bundle-analyzer`[](https://nextjs.org/docs/pages/guides/package-bundling#nextbundle-analyzer-for-webpack)

[`@next/bundle-analyzer`](https://www.npmjs.com/package/@next/bundle-analyzer)는 애플리케이션 번들 크기를 관리하도록 돕는 플러그인입니다. 각 패키지와 의존성의 크기를 시각적으로 보여 주어, 큰 의존성을 제거하거나 분할하거나 [지연 로드](https://nextjs.org/docs/app/guides/lazy-loading)할지 판단할 수 있습니다.

### 1단계: 설치[](https://nextjs.org/docs/pages/guides/package-bundling#step-1-installation)

다음 명령으로 플러그인을 설치하세요.

pnpmnpmyarnbun

Terminal
```
    pnpm add @next/bundle-analyzer
```

그다음 `next.config.js`에 번들 분석기 설정을 추가합니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {}

    const withBundleAnalyzer = require('@next/bundle-analyzer')({
      enabled: process.env.ANALYZE === 'true',
    })

    module.exports = withBundleAnalyzer(nextConfig)
```

### 2단계: 보고서 생성[](https://nextjs.org/docs/pages/guides/package-bundling#step-2-generating-a-report)

다음 명령으로 번들을 분석하세요.
```
    ANALYZE=true npm run build
    # 또는
    ANALYZE=true yarn build
    # 또는
    ANALYZE=true pnpm build
```

보고서는 브라우저에 세 개의 새 탭으로 열리며, 각각을 살펴볼 수 있습니다.

## 대형 번들 최적화[](https://nextjs.org/docs/pages/guides/package-bundling#optimizing-large-bundles)

큰 모듈을 찾았다면 해결책은 사용 사례에 따라 달라집니다. 아래는 일반적인 원인과 해결 방법입니다.

### 다수의 export를 가진 패키지[](https://nextjs.org/docs/pages/guides/package-bundling#packages-with-many-exports)

수백 개의 모듈을 export하는 패키지(아이콘/유틸리티 라이브러리 등)를 사용하는 경우, `next.config.js`에서 [`optimizePackageImports`](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) 옵션으로 import 해석을 최적화할 수 있습니다. 이 옵션은 실제 사용하는 모듈만 로드하면서도 다수의 named export를 편리하게 import할 수 있게 해줍니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        optimizePackageImports: ['icon-library'],
      },
    }

    module.exports = nextConfig
```

> **알아두면 좋아요:** Next.js는 일부 라이브러리를 자동으로 최적화하므로 `optimizePackageImports` 목록에 추가할 필요가 없습니다. 지원 패키지의 [전체 목록](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)을 확인하세요.

### 무거운 클라이언트 작업[](https://nextjs.org/docs/pages/guides/package-bundling#heavy-client-workloads)

대형 클라이언트 번들의 흔한 원인은 Client Component에서 비용이 큰 렌더링 작업을 수행하는 것입니다. 구문 하이라이트, 차트 렌더링, 마크다운 파싱처럼 데이터를 UI로 변환하는 라이브러리에서 자주 발생합니다.

해당 작업이 브라우저 API나 사용자 상호작용을 필요로 하지 않는다면 Server Component에서 실행할 수 있습니다.

다음 예시는 prism 기반 하이라이터가 Client Component에서 실행되는 경우입니다. 최종 출력이 `<code>` 블록일 뿐이어도, 전체 하이라이팅 라이브러리가 클라이언트 JavaScript 번들에 포함됩니다.

app/blog/[slug]/page.tsx
```
    'use client'

    import Highlight from 'prism-react-renderer'
    import theme from 'prism-react-renderer/themes/github'

    export default function Page() {
      const code = `export function hello() {
        console.log("hi")
      }`

      return (
        <article>
          <h1>Blog Post Title</h1>

          {/* The prism package and its tokenization logic are shipped to the client */}
          <Highlight code={code} language="tsx" theme={theme}>
            {({ className, style, tokens, getLineProps, getTokenProps }) => (
              <pre className={className} style={style}>
                <code>
                  {tokens.map((line, i) => (
                    <div key={i} {...getLineProps({ line })}>
                      {line.map((token, key) => (
                        <span key={key} {...getTokenProps({ token })} />
                      ))}
                    </div>
                  ))}
                </code>
              </pre>
            )}
          </Highlight>
        </article>
      )
    }
```

결과가 정적 HTML이어도 클라이언트는 하이라이팅 라이브러리를 다운로드하고 실행해야 하므로 번들 크기가 커집니다.

대신 하이라이팅 로직을 Server Component로 옮겨 서버에서 최종 HTML을 렌더링하세요. 클라이언트는 렌더링된 마크업만 받습니다.

app/blog/[slug]/page.tsx
```
    import { codeToHtml } from 'shiki'

    export default async function Page() {
      const code = `export function hello() {
        console.log("hi")
      }`

      // The Shiki package runs on the server and is never bundled for the client.
      const highlightedHtml = await codeToHtml(code, {
        lang: 'tsx',
        theme: 'github-dark',
      })

      return (
        <article>
          <h1>Blog Post Title</h1>

          {/* Client receives plain markup */}
          <pre>
            <code dangerouslySetInnerHTML={{ __html: highlightedHtml }} />
          </pre>
        </article>
      )
    }
```

### 사전 번들링되지 않은 외부 패키지[](https://nextjs.org/docs/pages/guides/package-bundling#external-packages-that-arent-pre-bundled)

기본적으로 애플리케이션에 import한 패키지는 번들링되지 않습니다. 모노레포나 `node_modules`에서 import하는 등 외부 패키지가 사전 번들링되지 않았다면 성능에 영향을 줄 수 있습니다.

특정 패키지를 번들에 포함하려면 `next.config.js`에서 [`transpilePackages`](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages) 옵션을 사용하세요.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      transpilePackages: ['package-name'],
    }

    module.exports = nextConfig
```

모든 패키지를 자동으로 번들링하려면 `next.config.js`에서 [`bundlePagesRouterDependencies`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies) 옵션을 사용할 수 있습니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      bundlePagesRouterDependencies: true,
    }

    module.exports = nextConfig
```

### 특정 패키지를 번들에서 제외하기[](https://nextjs.org/docs/pages/guides/package-bundling#opting-specific-packages-out-of-bundling-1)

번들에 포함되지 않아야 하는 패키지를 찾았다면 `next.config.js`의 [`serverExternalPackages`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages) 옵션으로 자동 번들링에서 제외할 수 있습니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // 외부 패키지를 자동으로 번들링:
      bundlePagesRouterDependencies: true,
      // 특정 패키지를 번들링에서 제외:
      serverExternalPackages: ['package-name'],
    }

    module.exports = nextConfig
```

##

프로덕션 대비를 위한 애플리케이션 최적화 방법을 더 알아보세요.

- [프로덕션](https://nextjs.org/docs/pages/guides/production-checklist)
  - 권장 사항Next.js 애플리케이션을 프로덕션에 배포하기 전에 최고의 성능과 사용자 경험을 보장하기 위한 권장 사항을 확인하세요.

보내기