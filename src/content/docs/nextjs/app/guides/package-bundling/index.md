---
title: '가이드: 패키지 번들링'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 가이드: 패키지 번들링 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/package-bundling

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)패키지 번들링

페이지 복사

# 패키지 번들링 최적화

마지막 업데이트: 2026년 2월 20일

번들링은 애플리케이션 코드와 그 의존성을 클라이언트와 서버를 위한 최적화된 출력 파일로 결합하는 과정입니다. 번들이 작아지면 로드 속도가 빨라지고 자바스크립트 실행 시간이 줄어들며 [Core Web Vitals](https://web.dev/articles/vitals)가 개선되고 서버 콜드 스타트 시간도 감소합니다.

Next.js는 코드 분할, 트리 셰이킹 등 다양한 기법으로 자동으로 번들을 최적화합니다. 그러나 경우에 따라 수동으로 번들을 최적화해야 할 때도 있습니다.

애플리케이션 번들을 분석할 수 있는 도구는 두 가지입니다.

  * [Turbopack용 Next.js 번들 분석기(실험적)](https://nextjs.org/docs/app/guides/package-bundling#nextjs-bundle-analyzer-experimental)
  * Webpack용 [`@next/bundle-analyzer` 플러그인](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)



이 가이드는 각 도구 사용 방법과 [대용량 번들 최적화](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles) 방법을 설명합니다.

## Next.js Bundle Analyzer (실험적)[](https://nextjs.org/docs/app/guides/package-bundling#nextjs-bundle-analyzer-experimental)

> v16.1 이상에서 사용할 수 있습니다. [전용 GitHub 토론](https://github.com/vercel/next.js/discussions/86731)에서 피드백을 공유하고 [turbopack-bundle-analyzer-demo.vercel.sh](https://turbopack-bundle-analyzer-demo.vercel.sh/) 데모를 확인하세요.

Next.js 번들 분석기는 Turbopack의 모듈 그래프와 통합되어 있습니다. 정밀한 import 추적을 통해 서버 및 클라이언트 모듈을 검사할 수 있어 대용량 의존성을 찾기 쉽습니다. 상호작용형 번들 분석기 데모를 열어 모듈 그래프를 탐색하세요.

### 1단계: Turbopack Bundle Analyzer 실행[](https://nextjs.org/docs/app/guides/package-bundling#step-1-run-the-turbopack-bundle-analyzer)

다음 명령을 실행한 뒤 브라우저에서 인터랙티브 뷰를 여세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm next experimental-analyze
[/code]

### 2단계: 모듈 필터링 및 검사[](https://nextjs.org/docs/app/guides/package-bundling#step-2-filter-and-inspect-modules)

UI에서 라우트, 환경(클라이언트 또는 서버), 타입(JavaScript, CSS, JSON)별로 필터링하거나 파일로 검색할 수 있습니다.

Next.js 번들 분석기 UI 둘러보기

### 3단계: import 체인으로 모듈 추적[](https://nextjs.org/docs/app/guides/package-bundling#step-3-trace-modules-with-import-chains)

트리맵은 각 모듈을 사각형으로 표시하며, 모듈 크기는 사각형 면적으로 표현됩니다.

모듈을 클릭하면 크기, 전체 import 체인, 애플리케이션에서 사용되는 위치를 확인할 수 있습니다.

Next.js Bundle Analyzer import chain 뷰

### 4단계: 공유 또는 비교를 위한 출력 저장[](https://nextjs.org/docs/app/guides/package-bundling#step-4-write-output-to-disk-for-sharing-or-diffing)

팀원과 분석 결과를 공유하거나 최적화 전후 번들 크기를 비교하려면 인터랙티브 뷰를 건너뛰고 `--output` 플래그로 정적 파일로 저장하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm next experimental-analyze --output
[/code]

이 명령은 출력물을 `.next/diagnostics/analyze`에 기록합니다. 결과를 비교하려면 이 디렉터리를 다른 위치로 복사하세요.

터미널
[code]
    cp -r .next/diagnostics/analyze ./analyze-before-refactor
[/code]

> 번들 분석기에는 더 많은 옵션이 있습니다. 전체 목록은 Next.js CLI 레퍼런스를 참조하세요.

## Webpack용 `@next/bundle-analyzer`[](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)

[`@next/bundle-analyzer`](https://www.npmjs.com/package/@next/bundle-analyzer)는 애플리케이션 번들 크기를 관리하는 데 도움이 되는 플러그인입니다. 각 패키지와 의존성의 크기를 시각화한 리포트를 생성하며, 이를 바탕으로 대형 의존성을 제거하거나 코드 분할, [지연 로딩](https://nextjs.org/docs/app/guides/lazy-loading)을 수행할 수 있습니다.

### 1단계: 설치[](https://nextjs.org/docs/app/guides/package-bundling#step-1-installation)

다음 명령으로 플러그인을 설치하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm add @next/bundle-analyzer
[/code]

그다음 `next.config.js`에 번들 분석기 설정을 추가합니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {}
     
    const withBundleAnalyzer = require('@next/bundle-analyzer')({
      enabled: process.env.ANALYZE === 'true',
    })
     
    module.exports = withBundleAnalyzer(nextConfig)
[/code]

### 2단계: 리포트 생성[](https://nextjs.org/docs/app/guides/package-bundling#step-2-generating-a-report)

다음 명령을 실행하여 번들을 분석하세요.
[code] 
    ANALYZE=true npm run build
    # or
    ANALYZE=true yarn build
    # or
    ANALYZE=true pnpm build
[/code]

리포트는 브라우저에 새 탭 세 개로 열리며, 각각을 확인할 수 있습니다.

## 대용량 번들 최적화[](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles)

대형 모듈을 찾았다면 해결 방법은 사용 사례에 따라 달라집니다. 아래는 일반적인 원인과 대응 방법입니다.

### 다수의 export를 가진 패키지[](https://nextjs.org/docs/app/guides/package-bundling#packages-with-many-exports)

수백 개의 모듈을 export하는 패키지(아이콘, 유틸리티 라이브러리 등)를 사용하는 경우 `next.config.js` 파일에서 [`optimizePackageImports`](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) 옵션으로 import 해석 방식을 최적화할 수 있습니다. 이 옵션은 많은 named export를 사용하는 import 문을 그대로 작성하면서도 실제 사용하는 모듈만 로드합니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        optimizePackageImports: ['icon-library'],
      },
    }
     
    module.exports = nextConfig
[/code]

> **알아두면 좋아요:** Next.js가 자동으로 최적화하는 라이브러리도 있어 `optimizePackageImports` 목록에 포함할 필요가 없습니다. [전체 목록](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)을 확인하세요.

### 무거운 클라이언트 작업[](https://nextjs.org/docs/app/guides/package-bundling#heavy-client-workloads)

대형 클라이언트 번들의 흔한 원인은 클라이언트 컴포넌트에서 비용이 큰 렌더링 작업을 수행하는 것입니다. 구문 강조, 차트 렌더링, 마크다운 파싱처럼 데이터를 UI로 변환하는 라이브러리에서 자주 발생합니다.

브라우저 API나 사용자 상호작용이 필요하지 않다면 해당 작업을 서버 컴포넌트에서 수행할 수 있습니다.

아래 예시는 프리즘 기반 하이라이터가 클라이언트 컴포넌트에서 실행되는 경우입니다. 최종 출력은 `<code>` 블록이지만 전체 하이라이트 라이브러리가 클라이언트 번들에 포함됩니다.

app/blog/[slug]/page.tsx
[code]
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
[/code]

이렇게 하면 결과가 정적 HTML임에도 클라이언트가 하이라이팅 라이브러리를 다운로드하고 실행해야 하므로 번들 크기가 증가합니다.

대신 하이라이팅 로직을 서버 컴포넌트로 옮겨 서버에서 최종 HTML을 렌더링하면 클라이언트는 렌더링된 마크업만 받습니다.

app/blog/[slug]/page.tsx
[code]
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
[/code]

### 특정 패키지를 번들에서 제외하기[](https://nextjs.org/docs/app/guides/package-bundling#opting-specific-packages-out-of-bundling)

서버 컴포넌트와 라우트 핸들러에서 import된 패키지는 Next.js가 자동으로 번들링합니다.

`next.config.js`에서 [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages) 옵션을 사용해 특정 패키지를 번들에서 제외할 수 있습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      serverExternalPackages: ['package-name'],
    }
     
    module.exports = nextConfig
[/code]

## 

프로덕션용 애플리케이션 최적화에 대해 더 알아보세요.

### [프로덕션 권장 사항Next.js 애플리케이션을 프로덕션에 올리기 전에 최고의 성능과 사용자 경험을 보장하기 위한 체크리스트입니다.](https://nextjs.org/docs/app/guides/production-checklist)

도움이 되었나요?

지원됨.

보내기
