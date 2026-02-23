---
title: 'API 레퍼런스: Turbopack'
description: 'Turbopack은 Rust로 작성되어 Next.js에 내장된 증분 번들러로, JavaScript와 TypeScript에 최적화되어 있습니다. Pages와 App Router 모두에서 Turbopack을 사용해 훨씬 더 빠른 로컬 개발 경험을 얻을 수 있습니다.'
---

# API 레퍼런스: Turbopack | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/turbopack

Copy page

# Turbopack

최근 업데이트 2026년 2월 20일

Turbopack은 Rust로 작성되어 **Next.js**에 내장된 **증분 번들러**로, JavaScript와 TypeScript에 최적화되어 있습니다. Pages와 App Router 모두에서 Turbopack을 사용해 **훨씬 더 빠른** 로컬 개발 경험을 얻을 수 있습니다.

## Why Turbopack?[](https://nextjs.org/docs/app/api-reference/turbopack#why-turbopack)

우리는 Turbopack을 통해 Next.js의 성능을 극대화했습니다. 주요 내용은 다음과 같습니다.

  * **통합 그래프:** Next.js는 여러 출력 환경(예: 클라이언트와 서버)을 지원합니다. 여러 컴파일러를 관리하고 번들을 결합하는 작업은 번거로울 수 있습니다. Turbopack은 모든 환경을 위해 **단일 통합 그래프**를 사용합니다.
  * **번들링 vs 네이티브 ESM:** 일부 도구는 개발 환경에서 번들링을 건너뛰고 브라우저의 네이티브 ESM에 의존합니다. 작은 앱에서는 효과적이지만, 네트워크 요청이 많아지는 대형 앱에서는 속도가 느려질 수 있습니다. Turbopack은 개발 환경에서도 **번들링**을 수행하지만, 큰 앱에서도 빠르게 유지되도록 최적화된 방식으로 처리합니다.
  * **증분 계산:** Turbopack은 코어 전반에 걸쳐 작업을 병렬화하고 함수 수준까지 결과를 **캐시**합니다. 한 번 작업이 완료되면 Turbopack은 이를 반복하지 않습니다.
  * **지연 번들링:** Turbopack은 실제로 dev 서버에서 요청된 항목만 번들링합니다. 이 지연 방식 덕분에 초기 컴파일 시간과 메모리 사용량을 줄일 수 있습니다.

## Getting started[](https://nextjs.org/docs/app/api-reference/turbopack#getting-started)

Turbopack은 이제 Next.js의 **기본 번들러**입니다. 별도의 설정 없이 사용할 수 있습니다.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start"
      }
    }
[/code]

### Using Webpack instead[](https://nextjs.org/docs/app/api-reference/turbopack#using-webpack-instead)

Turbopack 대신 Webpack을 사용해야 한다면 `--webpack` 플래그로 옵트인할 수 있습니다.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev --webpack",
        "build": "next build --webpack",
        "start": "next start"
      }
    }
[/code]

## Supported features[](https://nextjs.org/docs/app/api-reference/turbopack#supported-features)

Next.js의 Turbopack은 일반적인 사용 사례에 대해 **별도 설정이 필요 없습니다**. 아래는 기본적으로 지원되는 항목과, 필요 시 Turbopack을 추가로 구성하는 방법에 대한 참고 링크입니다.

### Language features[](https://nextjs.org/docs/app/api-reference/turbopack#language-features)

기능| 상태| 비고
---|---|---
**JavaScript & TypeScript**| **지원**| 내부적으로 SWC를 사용합니다. 타입 검사는 Turbopack이 수행하지 않으므로 `tsc --watch`를 실행하거나 IDE에 의존하세요.
**ECMAScript (ESNext)**| **지원**| Turbopack은 최신 ECMAScript 기능을 지원하며 SWC와 동일한 범위를 제공합니다.
**CommonJS**| **지원**| `require()` 구문을 기본적으로 처리합니다.
**ESM**| **지원**| 정적 및 동적 `import`를 완전히 지원합니다.
**Babel**| **지원**| Next.js 16부터 구성 파일이 감지되면 Turbopack이 자동으로 Babel을 사용합니다. webpack과 달리 SWC는 항상 Next.js 내부 변환과 구 ECMAScript 버전 다운레벨링에 사용됩니다. webpack을 사용하는 Next.js는 Babel 구성 파일이 있으면 SWC를 비활성화합니다. `node_modules`의 파일은 제외되지만, [직접 `babel-loader`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)하면 포함할 수 있습니다.

### Framework and React features[](https://nextjs.org/docs/app/api-reference/turbopack#framework-and-react-features)

기능| 상태| 비고
---|---|---
**JSX / TSX**| **지원**| SWC가 JSX/TSX 컴파일을 처리합니다.
**Fast Refresh**| **지원**| 추가 설정이 필요 없습니다.
**React Server Components (RSC)**| **지원**| Next.js App Router에서 사용합니다. Turbopack은 서버/클라이언트 번들링을 정확히 보장합니다.
**루트 레이아웃 생성**| 미지원| App Router에서 루트 레이아웃을 자동 생성하지 않습니다. Turbopack이 직접 만들도록 안내합니다.

### CSS and styling[](https://nextjs.org/docs/app/api-reference/turbopack#css-and-styling)

기능| 상태| 비고
---|---|---
**글로벌 CSS**| **지원**| 애플리케이션에서 `.css` 파일을 직접 import하세요.
**CSS Modules**| **지원**| `.module.css` 파일이 기본적으로 동작합니다(Lightning CSS).
**CSS 중첩**| **지원**| Lightning CSS가 [최신 CSS 중첩](https://lightningcss.dev/)을 지원합니다.
**@import 구문**| **지원**| 여러 CSS 파일을 결합할 수 있습니다.
**PostCSS**| **지원**| `postcss.config.js`를 Node.js 워커 풀에서 자동으로 처리합니다. Tailwind, Autoprefixer 등에 유용합니다.
**Sass / SCSS**| **지원** (Next.js)| Next.js에서는 Sass가 기본 지원됩니다. 맞춤 Sass 함수(`sassOptions.functions`)는 Turbopack의 Rust 기반 구조가 webpack의 Node.js 환경처럼 JavaScript 함수를 직접 실행할 수 없기 때문에 지원되지 않습니다. 이 기능이 필요하면 webpack을 사용하세요. 향후 Turbopack 독립 사용 시 로더 구성이 필요할 가능성이 큽니다.
**Less**| 플러그인 예정| 기본적으로 아직 지원되지 않습니다. 사용자 정의 로더가 안정화되면 로더 구성이 필요할 가능성이 큽니다.
**Lightning CSS**| **사용 중**| CSS 변환을 처리합니다. `:local/:global`을 독립된 의사 클래스처럼 사용하는 등 사용 빈도가 낮은 일부 CSS Modules 기능은 아직 지원되지 않습니다. [자세한 내용은 아래를 참고하세요.](https://nextjs.org/docs/app/api-reference/turbopack#unsupported-and-unplanned-features)

### Assets[](https://nextjs.org/docs/app/api-reference/turbopack#assets)

기능| 상태| 비고
---|---|---
**정적 에셋**(이미지, 폰트)| **지원**| `import img from './img.png'`와 같은 import가 기본으로 동작합니다. Next.js에서는 `<Image />` 컴포넌트를 위한 객체를 반환합니다.
**JSON Imports**| **지원**| `.json`에서 명명형 또는 기본 import를 지원합니다.

### Module resolution[](https://nextjs.org/docs/app/api-reference/turbopack#module-resolution)

기능| 상태| 비고
---|---|---
**Path Aliases**| **지원**| `tsconfig.json`의 `paths`와 `baseUrl`을 읽어 Next.js와 동일하게 동작합니다.
**수동 별칭**| **지원**| [`next.config.js`에서 `resolveAlias`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-aliases)하세요(`webpack.resolve.alias`와 유사).
**사용자 정의 확장자**| **지원**| [`next.config.js`에서 `resolveExtensions`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-custom-extensions)하세요.
**AMD**| 부분 지원| 기본 변환은 작동하지만 고급 AMD 사용은 제한적입니다.

### Performance and Fast Refresh[](https://nextjs.org/docs/app/api-reference/turbopack#performance-and-fast-refresh)

기능| 상태| 비고
---|---|---
**Fast Refresh**| **지원**| 전체 새로고침 없이 JavaScript, TypeScript, CSS를 업데이트합니다.
**Incremental Bundling**| **지원**| Turbopack은 dev 서버에서 요청된 항목만 지연 빌드하여 대형 앱을 빠르게 유지합니다.

## Known gaps with webpack[](https://nextjs.org/docs/app/api-reference/turbopack#known-gaps-with-webpack)

애플리케이션 마이그레이션 시 알아두어야 할 webpack과 Turbopack 간 비상 trivial 동작 차이가 여러 가지 있습니다. 일반적으로 신규 애플리케이션이라면 걱정할 필요가 적습니다.

### Filesystem Root[](https://nextjs.org/docs/app/api-reference/turbopack#filesystem-root)

Turbopack은 루트 디렉터리를 사용해 모듈을 해석합니다. 프로젝트 루트 밖의 파일은 해석되지 않습니다.

예를 들어, 프로젝트 루트 밖의 의존성을(`npm link`, `yarn link`, `pnpm link` 등으로) 링크하면 해당 링크된 파일은 기본적으로 해석되지 않습니다. 이러한 파일을 해석하려면 프로젝트와 링크된 의존성의 상위 디렉터리를 루트 옵션으로 구성해야 합니다.

`next.config.js`에서 [turbopack.root](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#root-directory) 옵션을 사용해 파일 시스템 루트를 설정할 수 있습니다.

### CSS Module Ordering[](https://nextjs.org/docs/app/api-reference/turbopack#css-module-ordering)

Turbopack은 다른 방식으로 정렬되지 않은 [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)을 정렬할 때 JS import 순서를 따릅니다. 예시는 다음과 같습니다.

components/BlogPost.jsx
[code]
    import utilStyles from './utils.module.css'
    import buttonStyles from './button.module.css'
    export default function BlogPost() {
      return (
        <div className={utilStyles.container}>
          <button className={buttonStyles.primary}>Click me</button>
        </div>
      )
    }
[/code]

이 예제에서 Turbopack은 import 순서를 따라 `utils.module.css`가 생성된 CSS 청크에서 `button.module.css`보다 먼저 나타나도록 보장합니다.

Webpack도 일반적으로 동일하게 동작하지만, JS 파일이 부작용이 없다고 추론하는 등 JS 기반 순서를 무시하는 경우가 있습니다.

이 때문에 임의 순서에 의존하던 애플리케이션이 Turbopack을 도입하면 미묘한 렌더링 변화가 생길 수 있습니다. 일반적으로 해결책은 간단합니다. 예를 들어 `button.module.css`에서 `@import utils.module.css`를 사용해 순서를 강제하거나, 충돌하는 규칙을 찾아 동일한 속성을 타깃하지 않도록 변경하면 됩니다.

### Sass node_modules imports[](https://nextjs.org/docs/app/api-reference/turbopack#sass-node_modules-imports)

Turbopack은 기본적으로 `node_modules` Sass 파일 import를 지원합니다. Webpack은 이를 위해 구식 틸드 `~` 구문을 지원하지만 Turbopack은 지원하지 않습니다.

변경 전:

styles/globals.scss
[code]
    @import '~bootstrap/dist/css/bootstrap.min.css';
[/code]

변경 후:

styles/globals.scss
[code]
    @import 'bootstrap/dist/css/bootstrap.min.css';
[/code]

import를 수정할 수 없다면 `~` 구문을 실제 경로에 매핑하도록 `turbopack.resolveAlias` 구성을 추가할 수 있습니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        resolveAlias: {
          '~*': '*',
        },
      },
    }
[/code]

### Build Caching[](https://nextjs.org/docs/app/api-reference/turbopack#build-caching)

Webpack은 빌드 성능 향상을 위한 [디스크 빌드 캐시](https://webpack.js.org/configuration/cache/#cache)를 지원합니다. Turbopack도 유사한 기능을 제공하며 현재 베타입니다. Next 16부터는 아래 실험적 플래그를 설정해 Turbopack의 파일 시스템 캐시를 활성화할 수 있습니다.

  * [`experimental.turbopackFileSystemCacheForDev`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)는 기본적으로 활성화되어 있습니다.
  * [`experimental.turbopackFileSystemCacheForBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)는 현재 옵트인입니다.

> **알아두면 좋은 점:** 이 때문에 webpack과 Turbopack 성능을 비교할 때는 공정한 콜드 빌드 비교를 위해 빌드 사이에 `.next` 폴더를 삭제하거나, 워밍 빌드를 비교하려면 Turbopack 파일 시스템 캐시 기능을 활성화하세요.

### Webpack plugins[](https://nextjs.org/docs/app/api-reference/turbopack#webpack-plugins)

Turbopack은 webpack 플러그인을 지원하지 않습니다. 이는 통합을 위해 webpack의 플러그인 시스템에 의존하는 서드파티 도구에 영향을 줍니다. 대신 [webpack 로더](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)는 지원합니다. webpack 플러그인에 의존한다면 Turbopack과 호환되는 대안을 찾거나, 동등한 기능이 제공될 때까지 webpack을 계속 사용해야 합니다.

## Unsupported and unplanned features[](https://nextjs.org/docs/app/api-reference/turbopack#unsupported-and-unplanned-features)

아직 구현되지 않았거나 계획에 없는 기능은 다음과 같습니다.

  * **기존 CSS Modules 기능**

* 단독 `:local` 및 `:global` 의사 클래스(함수 형태인 `:global(...)`만 지원).
    * `@value` 규칙(CSS 변수로 대체됨).
    * `:import` 및 `:export` ICSS 규칙.
    * `.module.css`에서 `.css` 파일을 조합하는 `composes`. webpack에서는 해당 `.css` 파일을 CSS Module로 처리하지만, Turbopack에서는 항상 전역으로 취급합니다. CSS Module에서 `composes`를 사용하려면 `.css` 파일을 `.module.css` 파일로 바꿔야 합니다.
    * CSS Module에서 `.css`를 CSS Module로 가져오는 `@import`. webpack에서는 해당 `.css` 파일을 CSS Module로 처리하지만, Turbopack에서는 항상 전역으로 취급합니다. CSS Module에서 `@import`를 사용하려면 `.css` 파일을 `.module.css` 파일로 변경해야 합니다.
  * **`sassOptions.functions`** `sassOptions.functions`에 정의된 커스텀 Sass 함수는 지원되지 않습니다. 이 기능은 컴파일 중 Sass 코드에서 호출할 수 있는 JavaScript 함수를 정의합니다. Turbopack의 Rust 기반 아키텍처는 webpack의 Node.js 기반 sass-loader와 달리 `sassOptions.functions`를 통해 전달된 JavaScript 함수를 직접 실행할 수 없습니다. 커스텀 Sass 함수를 사용 중이라면 Turbopack 대신 webpack을 사용해야 합니다.
  * `next.config.js`의 **`webpack()` 구성** Turbopack이 webpack을 대체하므로 `webpack()` 구성은 인식되지 않습니다. 대신 [`turbopack` 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)을 사용하세요.
  * **Yarn PnP** Next.js의 Turbopack 지원 계획 없음.
  * **`experimental.urlImports`** Turbopack 지원 계획 없음.
  * **`experimental.esmExternals`** 지원 계획 없음. Turbopack은 Next.js의 레거시 `esmExternals` 구성을 지원하지 않습니다.
  * **일부 Next.js 실험 플래그**
    * `experimental.nextScriptWorkers`
    * `experimental.sri.algorithm`
    * `experimental.fallbackNodePolyfills` 향후 도입 예정.

각 기능 플래그와 상태에 대한 전체 세부 사항은 [Turbopack API Reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)를 참조하세요.

## Configuration[](https://nextjs.org/docs/app/api-reference/turbopack#configuration)

Turbopack은 `next.config.js`(또는 `next.config.ts`)의 `turbopack` 키를 통해 구성할 수 있습니다. 구성 옵션은 다음을 포함합니다:

  * **`rules`** 파일 변환을 위한 추가 [webpack 로더](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)를 정의합니다.
  * **`resolveAlias`** webpack의 `resolve.alias`와 유사한 수동 별칭을 생성합니다.
  * **`resolveExtensions`** 모듈 해석을 위한 파일 확장자를 변경하거나 확장합니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        // Example: adding an alias and custom file extension
        resolveAlias: {
          underscore: 'lodash',
        },
        resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
      },
    }
[/code]

더 심화된 구성 예시는 [Turbopack 구성 문서](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)를 참고하세요.

## Generating trace files for performance debugging[](https://nextjs.org/docs/app/api-reference/turbopack#generating-trace-files-for-performance-debugging)

성능이나 메모리 문제를 겪고 있으며 Next.js 팀의 진단을 돕고 싶다면, 개발 명령에 `NEXT_TURBOPACK_TRACING=1`을 추가해 트레이스 파일을 생성할 수 있습니다:
[code]
    NEXT_TURBOPACK_TRACING=1 next dev
[/code]

이 명령은 `.next/dev/trace-turbopack` 파일을 생성합니다. 조사에 도움이 되도록 [Next.js 저장소](https://github.com/vercel/next.js)에 GitHub 이슈를 만들 때 해당 파일을 포함하세요.

기본적으로 개발 서버 출력은 `.next/dev`에 기록됩니다. [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)에 대해 더 읽어보세요.

## Summary[](https://nextjs.org/docs/app/api-reference/turbopack#summary)

Turbopack은 **Rust 기반**, **증분** 번들러로, 특히 대규모 애플리케이션에서 로컬 개발과 빌드를 빠르게 만드는 것을 목표로 합니다. Next.js에 통합되어 CSS, React, TypeScript를 제로 구성으로 지원합니다.

## Version Changes[](https://nextjs.org/docs/app/api-reference/turbopack#version-changes)

Version| Changes
---|---
`v16.0.0`| Turbopack이 Next.js의 기본 번들러가 됩니다. 구성 파일이 발견되면 Babel을 자동으로 지원합니다.
`v15.5.0`| `build` 베타에 대한 Turbopack 지원
`v15.3.0`| `build`에 대한 실험적 지원
`v15.0.0`| `dev`에 대한 안정적인 Turbopack

supported.

Send
