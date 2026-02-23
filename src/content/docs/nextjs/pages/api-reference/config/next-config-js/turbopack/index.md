---
title: 'next.config.js 옵션: turbopack'
description: '이 기능은 현재 실험 단계이며 언제든지 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 직접 사용해 보고 GitHub에서 피드백을 공유하세요.'
---

# next.config.js 옵션: turbopack | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)turbopack

페이지 복사

# turbopack

이 기능은 현재 실험 단계이며 언제든지 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 직접 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유하세요.

마지막 업데이트: 2026년 2월 20일

`turbopack` 옵션을 사용하면 다양한 파일을 변환하고 모듈을 해석하는 방법을 바꾸도록 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 사용자 정의할 수 있습니다.

> **알아두면 좋아요** : `turbopack` 옵션은 Next.js 13.0.0부터 15.2.x까지 `experimental.turbo`라는 이름이었습니다. `experimental.turbo` 옵션은 Next.js 16에서 제거됩니다.
> 
> 더 오래된 버전의 Next.js를 사용 중이라면 `npx @next/codemod@latest next-experimental-turbo-to-turbopack .`을 실행해 구성을 자동으로 마이그레이션하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      turbopack: {
        // ...
      },
    }
     
    export default nextConfig
[/code]

> **알아두면 좋아요** :
> 
>   * Next.js용 Turbopack은 기본 제공 기능을 위해 별도의 로더나 로더 설정이 필요 없습니다. CSS와 최신 JavaScript 컴파일을 기본적으로 지원하므로 `@babel/preset-env`를 사용할 때 `css-loader`, `postcss-loader`, `babel-loader`가 필요하지 않습니다.
> 

## 참고[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#reference)

### 옵션[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#options)

`turbopack` 구성에는 다음과 같은 옵션을 사용할 수 있습니다.

Option| Description  
---|---  
`root`| 애플리케이션 루트 디렉터리를 설정합니다. 절대 경로여야 합니다.  
`rules`| Turbopack으로 실행할 때 적용할 지원되는 webpack 로더 목록입니다.  
`resolveAlias`| 별칭으로 지정된 import를 대신 로드할 모듈에 매핑합니다.  
`resolveExtensions`| 파일을 import할 때 해석할 확장자 목록입니다.  
`debugIds`| JavaScript 번들 및 소스 맵에서 [debug ID](https://github.com/tc39/ecma426/blob/main/proposals/debug-id.md)를 생성하도록 활성화합니다.  
  
### 지원되는 로더[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#supported-loaders)

다음 로더는 Turbopack의 webpack 로더 구현에서 동작하도록 검증되었지만, 여기에 없는 다른 많은 webpack 로더도 대부분 동작합니다.

  * [`babel-loader`](https://www.npmjs.com/package/babel-loader) [_(Babel 구성 파일이 발견되면 자동으로 설정)_](https://nextjs.org/docs/app/api-reference/turbopack#language-features)
  * [`@svgr/webpack`](https://www.npmjs.com/package/@svgr/webpack)
  * [`svg-inline-loader`](https://www.npmjs.com/package/svg-inline-loader)
  * [`yaml-loader`](https://www.npmjs.com/package/yaml-loader)
  * [`string-replace-loader`](https://www.npmjs.com/package/string-replace-loader)
  * [`raw-loader`](https://www.npmjs.com/package/raw-loader)
  * [`sass-loader`](https://www.npmjs.com/package/sass-loader) [_(자동으로 설정됨)_](https://nextjs.org/docs/app/api-reference/turbopack#css-and-styling)
  * [`graphql-tag/loader`](https://www.npmjs.com/package/graphql-tag)

#### 누락된 Webpack 로더 기능[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#missing-webpack-loader-features)

Turbopack은 webpack 로더를 실행하기 위해 [`loader-runner`](https://github.com/webpack/loader-runner) 라이브러리를 사용하며, 표준 로더 API 대부분을 제공합니다. 하지만 일부 기능은 지원되지 않습니다.

**모듈 로딩:**

  * [`importModule`](https://webpack.js.org/api/loaders/#thisimportmodule) \- 지원되지 않음
  * [`loadModule`](https://webpack.js.org/api/loaders/#thisloadmodule) \- 지원되지 않음

**파일 시스템 및 출력:**

  * [`fs`](https://webpack.js.org/api/loaders/#thisfs) \- 부분 지원: 현재 `fs.readFile`만 구현되어 있습니다.
  * [`emitFile`](https://webpack.js.org/api/loaders/#thisemitfile) \- 지원되지 않음

**컨텍스트 속성:**

  * [`version`](https://webpack.js.org/api/loaders/#thisversion) \- 지원되지 않음
  * [`mode`](https://webpack.js.org/api/loaders/#thismode) \- 지원되지 않음
  * [`target`](https://webpack.js.org/api/loaders/#thistarget) \- 지원되지 않음

**유틸리티:**

  * [`utils`](https://webpack.js.org/api/loaders/#thisutils) \- 지원되지 않음
  * [`resolve`](https://webpack.js.org/api/loaders/#thisresolve) \- 지원되지 않음(`[`getResolve`](https://webpack.js.org/api/loaders/#thisgetresolve)`을 대신 사용) 

이러한 기능에 크게 의존하는 로더가 있다면 이슈를 등록해 주세요.

## 예시[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#examples)

### 루트 디렉터리[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#root-directory)

Turbopack은 모듈을 해석하기 위해 루트 디렉터리를 사용합니다. 프로젝트 루트 밖의 파일은 해석되지 않습니다.

프로젝트 루트 밖의 파일을 해석하지 않는 이유는 캐시 검증을 개선하고 파일 시스템 감시 오버헤드를 줄이며 필요한 해석 단계를 줄이기 위함입니다.

Next.js는 다음 파일 중 하나를 찾아 프로젝트 루트 디렉터리를 자동으로 감지합니다.

  * `pnpm-lock.yaml`
  * `package-lock.json`
  * `yarn.lock`
  * `bun.lock`
  * `bun.lockb`

워크스페이스를 사용하지 않는 등 다른 프로젝트 구조를 가지고 있다면 `root` 옵션을 수동으로 설정할 수 있습니다.

next.config.js
[code]
    const path = require('path')
    module.exports = {
      turbopack: {
        root: path.join(__dirname, '..'),
      },
    }
[/code]

프로젝트 루트 밖의 연결된 의존성(`npm link`, `yarn link`, `pnpm link` 등)을 해석하려면 프로젝트와 연결된 의존성 모두의 상위 디렉터리를 `turbopack.root`로 설정해야 합니다.

이렇게 하면 파일 시스템 감시 범위가 넓어지지만, 일반적으로 연결된 패키지를 적극적으로 작업하는 개발 중에만 필요합니다.

### webpack 로더 구성[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders)

기본 제공 범위를 넘어서는 로더 지원이 필요하면, 많은 webpack 로더가 이미 Turbopack과 함께 동작합니다. 현재 몇 가지 제한이 있습니다.

  * webpack 로더 API의 핵심 하위 집합만 구현되었습니다. 지금은 일부 인기 있는 로더를 다룰 만큼의 범위가 있으며, 앞으로 API 지원을 확장할 예정입니다.
  * JavaScript 코드를 반환하는 로더만 지원됩니다. 스타일시트나 이미지처럼 파일을 변환하는 로더는 아직 지원되지 않습니다.
  * webpack 로더에 전달되는 옵션은 순수 JavaScript 원시값, 객체, 배열이어야 합니다. 예를 들어 옵션 값으로 `require()` 플러그인 모듈을 전달할 수 없습니다.

로더를 구성하려면 설치한 로더 이름과 옵션을 `next.config.js`의 파일 확장자 매핑에 추가하세요. 규칙은 순서대로 평가됩니다.

아래 예시는 [`@svgr/webpack`](https://www.npmjs.com/package/@svgr/webpack) 로더를 사용해 `.svg` 파일을 import하고 React 컴포넌트로 렌더링할 수 있게 합니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        rules: {
          '*.svg': {
            loaders: ['@svgr/webpack'],
            as: '*.js',
          },
        },
      },
    }
[/code]

> **알아두면 좋아요** : `rules` 객체에서 사용하는 glob은 파일 이름을 기준으로 매칭됩니다. glob에 `/` 문자가 포함되면 프로젝트 상대 전체 경로를 기준으로 매칭합니다. Windows 파일 경로는 유닉스 스타일 `/` 구분자로 정규화됩니다.
> 
> Turbopack은 수정된 [Rust `globset` 라이브러리](https://docs.rs/globset/latest/globset/)를 사용합니다.

구성 옵션이 필요한 로더의 경우 문자열 대신 객체 형식을 사용할 수 있습니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        rules: {
          '*.svg': {
            loaders: [
              {
                loader: '@svgr/webpack',
                options: {
                  icon: true,
                },
              },
            ],
            as: '*.js',
          },
        },
      },
    }
[/code]

> **알아두면 좋아요** : Next.js 13.4.4 이전에는 `turbopack.rules`가 `turbo.loaders`라는 이름이었으며 `*.mdx` 대신 `.mdx`와 같은 파일 확장자만 허용했습니다.

### 고급 webpack 로더 조건[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#advanced-webpack-loader-conditions)

고급 `condition` 구문을 사용하면 로더가 실행되는 위치를 추가로 제한할 수 있습니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        rules: {
          // '*' will match all file paths, but we restrict where our
          // rule runs with a condition.
          '*': {
            condition: {
              all: [
                // 'foreign' is a built-in condition.
                { not: 'foreign' },
                // 'path' can be a RegExp or a glob string. A RegExp matches
                // anywhere in the full project-relative file path.
                { path: /^img\/[0-9]{3}\// },
                {
                  any: [
                    { path: '*.svg' },
                    // 'content' is always a RegExp, and can match
                    // anywhere in the file.
                    { content: /\<svg\W/ },
                  ],
                },
              ],
            },
            loaders: ['@svgr/webpack'],
            as: '*.js',
          },
        },
      },
    }
[/code]

  * 지원되는 불리언 연산자는 `{all: [...]}`, `{any: [...]}`, `{not: ...}`입니다.
  * 지원되는 사용자 정의 연산자는 `{path: string | RegExp}`와 `{content: RegExp}`입니다. 동일한 객체에 `path`와 `content`를 함께 지정하면 묵시적인 `and`로 동작합니다.

이 외에도 여러 내장 조건을 지원합니다.

  * `browser`: 클라이언트에서 실행될 코드를 매칭합니다. 서버 코드는 `{not: 'browser'}`로 매칭할 수 있습니다.
  * `foreign`: `node_modules` 및 일부 Next.js 내부 코드를 매칭합니다. 성능을 위해 보통 로더 대상을 `{not: 'foreign'}`으로 제한하는 것이 좋습니다.
  * `development`: `next dev`를 사용할 때 매칭합니다.
  * `production`: `next build`를 사용할 때 매칭합니다.
  * `node`: 기본 Node.js 런타임에서 실행될 코드를 매칭합니다.
  * `edge-light`: [Edge runtime](https://nextjs.org/docs/app/api-reference/edge)에서 실행될 코드를 매칭합니다.

규칙은 객체 또는 객체 배열이 될 수 있습니다. 배열은 분리된 조건을 모델링할 때 유용합니다.

next.config.js
[code]
    module.exports = {
      turbopack: {
        rules: {
          '*.svg': [
            {
              condition: 'browser',
              loaders: ['@svgr/webpack'],
              as: '*.js',
            },
            {
              condition: { not: 'browser' },
              loaders: [require.resolve('./custom-svg-loader.js')],
              as: '*.js',
            },
          ],
        },
      },
    }
[/code]

> **알아두면 좋아요** : 매칭되는 모든 규칙이 순서대로 실행됩니다.

### 별칭 해석[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#resolving-aliases)

Turbopack은 webpack의 [`resolve.alias`](https://webpack.js.org/configuration/resolve/#resolvealias) 구성처럼 별칭을 통해 모듈 해석을 수정하도록 설정할 수 있습니다.

별칭을 구성하려면 `next.config.js`에서 import 패턴을 새 대상에 매핑하세요.

next.config.js
[code]
    module.exports = {
      turbopack: {
        resolveAlias: {
          underscore: 'lodash',
          mocha: { browser: 'mocha/browser-entry.js' },
        },

},
    }
[/code]

이는 `underscore` 패키지의 import를 `lodash` 패키지로 별칭 처리합니다. 즉, `import underscore from 'underscore'`가 `underscore` 대신 `lodash` 모듈을 로드합니다.

Turbopack은 Node.js의 [conditional exports](https://nodejs.org/docs/latest-v18.x/api/packages.html#conditional-exports)와 유사하게 이 필드를 통해 조건부 별칭도 지원합니다. 현재는 `browser` 조건만 지원됩니다. 위 예시에서 브라우저 환경을 대상으로 Turbopack을 실행하면 `mocha` 모듈의 import가 `mocha/browser-entry.js`로 별칭 처리됩니다.

### 사용자 지정 확장자 해결[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#resolving-custom-extensions)

Turbopack은 webpack의 [`resolve.extensions`](https://webpack.js.org/configuration/resolve/#resolveextensions) 설정처럼 사용자 지정 확장자를 가진 모듈을 해석하도록 구성할 수 있습니다.

해석할 확장자를 지정하려면 `next.config.js`에서 `resolveExtensions` 필드를 사용하세요:

next.config.js
[code]
    module.exports = {
      turbopack: {
        resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.mjs', '.json'],
      },
    }
[/code]

이 설정은 기존 해석 확장자 목록을 제공된 리스트로 덮어씁니다. 기본 확장자를 반드시 포함하세요.

webpack에서 Turbopack으로 앱을 마이그레이션하는 방법과 추가 안내는 [Turbopack의 webpack 호환성 문서](https://turbo.build/pack/docs/migrating-from-webpack)를 참고하세요.

### 디버그 ID[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#debug-ids)

Turbopack은 JavaScript 번들과 소스 맵에 [디버그 ID](https://github.com/tc39/ecma426/blob/main/proposals/debug-id.md)를 생성하도록 구성할 수 있습니다.

디버그 ID를 구성하려면 `next.config.js`에서 `debugIds` 필드를 사용하세요:

next.config.js
[code]
    module.exports = {
      turbopack: {
        debugIds: true,
      },
    }
[/code]

이 옵션은 호환성을 보장하기 위해 디버그 ID용 폴리필을 JavaScript 번들에 자동으로 추가합니다. 디버그 ID는 `globalThis._debugIds` 전역 변수에서 확인할 수 있습니다.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack#version-history)

Version| Changes  
---|---  
`16.0.0`| `turbopack.debugIds`가 추가되었습니다.  
`16.0.0`| `turbopack.rules.*.condition`이 추가되었습니다.  
`15.3.0`| `experimental.turbo`가 `turbopack`으로 변경되었습니다.  
`13.0.0`| `experimental.turbo`가 도입되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
