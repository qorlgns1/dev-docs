---
title: 'API Reference: Turbopack'
description: 'Turbopack은 Rust로 작성된 증분 번들러로, JavaScript와 TypeScript에 최적화되어 있으며 Next.js에 내장되어 있습니다. Pages Router와 App Router 모두에서 Turbopack을 사용하면 훨씬 빠른 로컬 개발 환경을 경험할 ...'
---

# API Reference: Turbopack | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/turbopack

Copy page

# Turbopack

Last updated February 20, 2026

Turbopack은 Rust로 작성된 **증분 번들러**로, JavaScript와 TypeScript에 최적화되어 있으며 **Next.js**에 내장되어 있습니다. Pages Router와 App Router 모두에서 Turbopack을 사용하면 **훨씬 빠른** 로컬 개발 환경을 경험할 수 있습니다.

## Why Turbopack?[](https://nextjs.org/docs/pages/api-reference/turbopack#why-turbopack)

Next.js의 성능을 끌어올리기 위해 Turbopack을 구축했습니다. 주요 목표는 다음과 같습니다.

  * **통합 그래프:** Next.js는 클라이언트와 서버 같은 여러 출력 환경을 지원합니다. 여러 컴파일러를 관리하고 번들을 병합하는 것은 번거롭습니다. Turbopack은 모든 환경에 대해 **단일 통합 그래프**를 사용합니다.
  * **번들링 vs 네이티브 ESM:** 일부 도구는 개발 중 번들링을 생략하고 브라우저의 네이티브 ESM에 의존합니다. 작은 앱에서는 효과적이지만, 네트워크 요청이 많아져 큰 앱에서는 느릴 수 있습니다. Turbopack은 개발 중에도 **번들링**을 수행하지만, 큰 앱도 빠르게 유지하도록 최적화되어 있습니다.
  * **증분 계산:** Turbopack은 코어 전반에 작업을 병렬화하고 결과를 함수 수준까지 **캐시**합니다. 한 번 완료된 작업은 다시 수행하지 않습니다.
  * **지연 번들링:** Turbopack은 dev 서버가 실제로 요청한 것만 번들링합니다. 이런 지연 방식은 초기 컴파일 시간과 메모리 사용량을 줄일 수 있습니다.

## Getting started[](https://nextjs.org/docs/pages/api-reference/turbopack#getting-started)

Turbopack은 이제 Next.js의 **기본 번들러**입니다. 별도의 설정 없이 사용할 수 있습니다.

package.json
```
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start"
      }
    }
```

### Using Webpack instead[](https://nextjs.org/docs/pages/api-reference/turbopack#using-webpack-instead)

Turbopack 대신 Webpack을 사용해야 한다면 `--webpack` 플래그로 opt-in 할 수 있습니다.

package.json
```
    {
      "scripts": {
        "dev": "next dev --webpack",
        "build": "next build --webpack",
        "start": "next start"
      }
    }
```

## Supported features[](https://nextjs.org/docs/pages/api-reference/turbopack#supported-features)

Next.js에서 Turbopack은 일반적인 사용 사례에 대해 **zero-configuration**을 제공합니다. 아래는 즉시 지원되는 기능 요약과 필요할 때 Turbopack을 더 구성하는 방법에 대한 참고 링크입니다.

### Language features[](https://nextjs.org/docs/pages/api-reference/turbopack#language-features)

Feature| Status| Notes
---|---|---
**JavaScript & TypeScript**| **Supported**|  내부적으로 SWC를 사용합니다. 타입 체크는 Turbopack이 수행하지 않으므로 `tsc --watch`를 실행하거나 IDE에 의존하세요.
**ECMAScript (ESNext)**| **Supported**|  Turbopack은 최신 ECMAScript 기능을 지원하며 SWC 커버리지와 일치합니다.
**CommonJS**| **Supported**| `require()` 구문을 즉시 처리합니다.
**ESM**| **Supported**|  정적 및 동적 `import`를 완전히 지원합니다.
**Babel**| **Supported**|  Next.js 16부터 구성 파일이 감지되면 Turbopack이 자동으로 Babel을 사용합니다. webpack과 달리 SWC는 항상 Next.js 내부 변환과 구 ECMAScript 다운레벨링에 사용됩니다. Next.js에서 webpack을 사용할 때는 Babel 구성 파일이 있으면 SWC를 비활성화합니다. `node_modules`의 파일은 제외되지만, [직접 `babel-loader`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)하면 포함할 수 있습니다.

### Framework and React features[](https://nextjs.org/docs/pages/api-reference/turbopack#framework-and-react-features)

Feature| Status| Notes
---|---|---
**JSX / TSX**| **Supported**|  SWC가 JSX/TSX 컴파일을 처리합니다.
**Fast Refresh**| **Supported**|  추가 설정이 필요 없습니다.
**React Server Components (RSC)**| **Supported**|  Next.js App Router용입니다. Turbopack이 서버/클라이언트 번들링을 정확히 보장합니다.
**Root layout creation**|  Unsupported| App Router에서 루트 레이아웃 자동 생성은 지원되지 않습니다. Turbopack이 수동 생성을 안내합니다.

### CSS and styling[](https://nextjs.org/docs/pages/api-reference/turbopack#css-and-styling)

Feature| Status| Notes
---|---|---
**Global CSS**| **Supported**|  애플리케이션에서 `.css` 파일을 직접 가져올 수 있습니다.
**CSS Modules**| **Supported**| `.module.css` 파일이 네이티브로 동작합니다 (Lightning CSS).
**CSS Nesting**| **Supported**|  Lightning CSS가 [최신 CSS 네스팅](https://lightningcss.dev/)을 지원합니다.
**@import syntax**| **Supported**|  여러 CSS 파일을 결합할 수 있습니다.
**PostCSS**| **Supported**|  `postcss.config.js`를 Node.js 워커 풀에서 자동 처리합니다. Tailwind, Autoprefixer 등에 유용합니다.
**Sass / SCSS**| **Supported** (Next.js)| Next.js에서는 Sass가 기본 지원됩니다. 사용자 정의 Sass 함수(`sassOptions.functions`)는 Turbopack의 Rust 기반 아키텍처가 webpack의 Node.js 환경처럼 JavaScript 함수를 직접 실행할 수 없으므로 지원되지 않습니다. 이 기능이 필요하면 webpack을 사용하세요. 향후 독립 실행형 Turbopack 사용 시 로더 구성이 필요할 가능성이 큽니다.
**Less**|  Planned via plugins| 아직 기본 지원되지 않습니다. 커스텀 로더가 안정화되면 로더 구성이 필요할 전망입니다.
**Lightning CSS**| **In Use**|  CSS 변환을 처리합니다. 일부 사용 빈도가 낮은 CSS Modules 기능(`:local/:global`을 독립적인 의사 클래스 등)은 아직 미지원입니다. [아래에서 자세한 내용을 확인하세요.](https://nextjs.org/docs/pages/api-reference/turbopack#unsupported-and-unplanned-features)

### Assets[](https://nextjs.org/docs/pages/api-reference/turbopack#assets)

Feature| Status| Notes
---|---|---
**Static Assets** (images, fonts)| **Supported**|  `import img from './img.png'`과 같은 가져오기가 즉시 동작합니다. Next.js에서는 `<Image />` 컴포넌트를 위한 객체를 반환합니다.
**JSON Imports**| **Supported**|  `.json`에서 이름 기반 혹은 기본 import가 지원됩니다.

### Module resolution[](https://nextjs.org/docs/pages/api-reference/turbopack#module-resolution)

Feature| Status| Notes
---|---|---
**Path Aliases**| **Supported**|  `tsconfig.json`의 `paths`와 `baseUrl`을 읽어 Next.js 동작과 일치합니다.
**Manual Aliases**| **Supported**| [`next.config.js`에서 `resolveAlias`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-aliases)하세요 (`webpack.resolve.alias`와 유사).
**Custom Extensions**| **Supported**| [`next.config.js`에서 `resolveExtensions`를 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#resolving-custom-extensions)하세요.
**AMD**|  Partially Supported| 기본 변환은 동작하지만 고급 AMD 사용은 제한적입니다.

### Performance and Fast Refresh[](https://nextjs.org/docs/pages/api-reference/turbopack#performance-and-fast-refresh)

Feature| Status| Notes
---|---|---
**Fast Refresh**| **Supported**|  JavaScript, TypeScript, CSS를 전체 새로고침 없이 업데이트합니다.
**Incremental Bundling**| **Supported**|  Turbopack은 dev 서버가 요청한 것만 지연 빌드하여 큰 앱 속도를 높입니다.

## Known gaps with webpack[](https://nextjs.org/docs/pages/api-reference/turbopack#known-gaps-with-webpack)

webpack에서 Turbopack으로 마이그레이션할 때 유의해야 하는 비사소한 동작 차이가 여러 가지 있습니다. 일반적으로 새 애플리케이션에서는 덜 중요한 문제들입니다.

### Filesystem Root[](https://nextjs.org/docs/pages/api-reference/turbopack#filesystem-root)

Turbopack은 루트 디렉터리를 사용해 모듈을 해석합니다. 프로젝트 루트 밖의 파일은 해석되지 않습니다.

예를 들어 `npm link`, `yarn link`, `pnpm link` 등으로 프로젝트 루트 밖의 의존성을 연결하면 기본적으로 해당 연결 파일은 해석되지 않습니다. 이러한 파일을 해석하려면 프로젝트와 연결된 의존성 모두의 상위 디렉터리를 root 옵션으로 설정해야 합니다.

`next.config.js`에서 [turbopack.root](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#root-directory) 옵션을 사용해 파일 시스템 루트를 구성할 수 있습니다.

### CSS Module Ordering[](https://nextjs.org/docs/pages/api-reference/turbopack#css-module-ordering)

Turbopack은 다른 기준이 없을 때 [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)의 순서를 JS import 순서에 따릅니다. 예:

components/BlogPost.jsx
```
    import utilStyles from './utils.module.css'
    import buttonStyles from './button.module.css'
    export default function BlogPost() {
      return (
        <div className={utilStyles.container}>
          <button className={buttonStyles.primary}>Click me</button>
        </div>
      )
    }
```

이 예시에서 Turbopack은 import 순서를 따라, 생성된 CSS 청크에서 `utils.module.css`가 `button.module.css`보다 먼저 나오도록 보장합니다.

Webpack도 일반적으로 동일하게 동작하지만, JS 파일이 사이드 이펙트가 없다고 판단하면 JS에서 추론한 순서를 무시하는 경우가 있습니다.

이 때문에 임의 순서에 의존하던 애플리케이션이 Turbopack을 도입하면 미묘한 렌더링 변화가 생길 수 있습니다. 일반적으로 해결책은 간단하며, 예를 들어 `button.module.css`에서 `@import utils.module.css`를 호출해 순서를 강제하거나 충돌하는 규칙을 찾아 동일한 속성을 타깃하지 않도록 수정하면 됩니다.

### Sass node_modules imports[](https://nextjs.org/docs/pages/api-reference/turbopack#sass-node_modules-imports)

Turbopack은 `node_modules` Sass 파일 import를 기본 지원합니다. Webpack은 이를 위해 오래된 물결표 `~` 문법을 지원하지만 Turbopack은 지원하지 않습니다.

From:

styles/globals.scss
```
    @import '~bootstrap/dist/css/bootstrap.min.css';
```

To:

styles/globals.scss
```
    @import 'bootstrap/dist/css/bootstrap.min.css';
```

import를 변경할 수 없다면 `~` 문법을 실제 경로에 매핑하도록 `turbopack.resolveAlias` 구성을 추가할 수 있습니다.

next.config.js
```
    module.exports = {
      turbopack: {
        resolveAlias: {
          '~*': '*',
        },
      },
    }
```

### Build Caching[](https://nextjs.org/docs/pages/api-reference/turbopack#build-caching)

Webpack은 빌드 성능을 높이기 위해 [디스크 빌드 캐싱](https://webpack.js.org/configuration/cache/#cache)을 지원합니다. Turbopack도 유사한 기능을 제공하며 현재 베타 상태입니다. Next 16부터는 다음 실험적 플래그를 설정해 Turbopack 파일 시스템 캐시를 활성화할 수 있습니다.

  * [`experimental.turbopackFileSystemCacheForDev`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)는 기본적으로 활성화되어 있습니다.
  * [`experimental.turbopackFileSystemCacheForBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)는 현재 opt-in입니다.

> **알아두면 좋아요:** 이러한 이유로 webpack과 Turbopack의 성능을 비교할 때는 공정한 콜드 빌드 비교를 위해 빌드 사이에 `.next` 폴더를 삭제하거나, 터보팩 파일 시스템 캐시를 활성화해 웜 빌드를 비교하세요.

### Webpack plugins[](https://nextjs.org/docs/pages/api-reference/turbopack#webpack-plugins)

Turbopack은 webpack 플러그인을 지원하지 않습니다. 이 때문에 webpack 플러그인 시스템에 의존하는 서드파티 도구 통합에 영향이 있습니다. 대신 [webpack 로더](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)는 지원합니다. webpack 플러그인에 의존한다면 Turbopack과 호환되는 대안을 찾거나 동등한 기능이 제공될 때까지 webpack을 계속 사용해야 합니다.

## Unsupported and unplanned features[](https://nextjs.org/docs/pages/api-reference/turbopack#unsupported-and-unplanned-features)

아직 구현되지 않았거나 계획되지 않은 기능:

  * **Legacy CSS Modules features**

* 독립형 `:local` 및 `:global` 의사 클래스(함수 형태인 `:global(...)`만 지원).
    * `@value` 규칙(CSS 변수로 대체됨).
    * `:import` 및 `:export` ICSS 규칙.
    * `.module.css`에서 `.css` 파일을 조합하는 `composes`. webpack에서는 `.css` 파일을 CSS Module로 처리하지만 Turbopack에서는 항상 전역으로 취급합니다. 따라서 CSS Module에서 `composes`를 사용하려면 해당 `.css` 파일을 `.module.css` 파일로 바꿔야 합니다.
    * CSS Modules에서 `.css`를 CSS Module로 가져오는 `@import`. webpack에서는 `.css` 파일을 CSS Module로 처리하지만 Turbopack에서는 항상 전역으로 취급합니다. 따라서 CSS Module에서 `@import`를 사용하려면 해당 `.css` 파일을 `.module.css` 파일로 바꿔야 합니다.
  * **`sassOptions.functions`** `sassOptions.functions`에 정의된 사용자 지정 Sass 함수는 지원되지 않습니다. 이 기능은 컴파일 중에 Sass 코드에서 호출할 수 있는 JavaScript 함수를 정의합니다. Turbopack은 Rust 기반 아키텍처이므로 webpack의 Node.js 기반 `sass-loader`처럼 JavaScript로 작성된 함수를 직접 실행할 수 없습니다. 사용자 지정 Sass 함수를 사용 중이라면 Turbopack 대신 webpack을 사용해야 합니다.
  * **`next.config.js`의 `webpack()` 구성** Turbopack이 webpack을 대체하므로 `webpack()` 구성은 인식되지 않습니다. 대신 [`turbopack` 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)을 사용하세요.
  * **Yarn PnP** Next.js의 Turbopack에서는 지원 계획이 없습니다.
  * **`experimental.urlImports`** Turbopack에 대한 지원 계획이 없습니다.
  * **`experimental.esmExternals`** 지원 계획이 없습니다. Turbopack은 Next.js의 레거시 `esmExternals` 구성을 지원하지 않습니다.
  * **일부 Next.js 실험적 플래그**
    * `experimental.nextScriptWorkers`
    * `experimental.sri.algorithm`
    * `experimental.fallbackNodePolyfills` 향후 지원할 계획입니다.

각 기능 플래그와 상태에 대한 전체 상세 설명은 [Turbopack API Reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)를 확인하세요.

## Configuration[](https://nextjs.org/docs/pages/api-reference/turbopack#configuration)

Turbopack은 `next.config.js`(또는 `next.config.ts`)의 `turbopack` 키를 통해 구성할 수 있습니다. 구성 옵션은 다음을 포함합니다:

  * **`rules`** 파일 변환을 위한 추가 [webpack loaders](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)를 정의합니다.
  * **`resolveAlias`** webpack의 `resolve.alias`와 유사하게 수동 별칭을 만듭니다.
  * **`resolveExtensions`** 모듈 해석에 사용할 파일 확장자를 변경하거나 확장합니다.

next.config.js
```
    module.exports = {
      turbopack: {
        // Example: adding an alias and custom file extension
        resolveAlias: {
          underscore: 'lodash',
        },
        resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
      },
    }
```

보다 심층적인 구성 예시는 [Turbopack config documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)를 참고하세요.

## Generating trace files for performance debugging[](https://nextjs.org/docs/pages/api-reference/turbopack#generating-trace-files-for-performance-debugging)

성능 또는 메모리 문제를 겪고 Next.js 팀의 진단을 돕고 싶다면 개발 명령에 `NEXT_TURBOPACK_TRACING=1`을 추가하여 추적 파일을 생성할 수 있습니다:
```
    NEXT_TURBOPACK_TRACING=1 next dev
```

그러면 `.next/dev/trace-turbopack` 파일이 생성됩니다. 조사를 돕기 위해 [Next.js 저장소](https://github.com/vercel/next.js)에 GitHub 이슈를 만들 때 해당 파일을 포함하세요.

기본적으로 개발 서버 출력은 `.next/dev`에 기록됩니다. 자세한 내용은 [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)를 확인하세요.

## Summary[](https://nextjs.org/docs/pages/api-reference/turbopack#summary)

Turbopack은 로컬 개발과 빌드를 특히 대규모 애플리케이션에서 빠르게 하기 위해 설계된 **Rust 기반**, **증분형** 번들러입니다. Next.js에 통합되어 있으며, CSS·React·TypeScript를 제로 구성으로 지원합니다.

## Version Changes[](https://nextjs.org/docs/pages/api-reference/turbopack#version-changes)

Version| Changes
---|---
`v16.0.0`| Turbopack이 Next.js의 기본 번들러가 됩니다. 구성 파일이 발견되면 Babel을 자동 지원합니다.
`v15.5.0`| `build` 베타에 대해 Turbopack을 지원합니다.
`v15.3.0`| `build`에 대한 실험적 지원.
`v15.0.0`| 안정적인 `dev`용 Turbopack.

보내기