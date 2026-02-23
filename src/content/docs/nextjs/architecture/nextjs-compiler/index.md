---
title: '아키텍처: Next.js Compiler'
description: 'Rust로 작성되고 SWC를 사용하는 Next.js Compiler는 Next.js가 프로덕션용 JavaScript 코드를 변환하고 최소화할 수 있게 해 줍니다. 이는 개별 파일 처리에 사용되던 Babel과 출력 번들을 최소화하던 Terser를 대체합니다.'
---

# 아키텍처: Next.js Compiler | Next.js
출처 URL: https://nextjs.org/docs/architecture/nextjs-compiler

[Next.js 문서](https://nextjs.org/docs)[아키텍처](https://nextjs.org/docs/architecture)Next.js Compiler

# Next.js Compiler

마지막 업데이트 2026년 2월 20일

Rust로 작성되고 [SWC](https://swc.rs/)를 사용하는 Next.js Compiler는 Next.js가 프로덕션용 JavaScript 코드를 변환하고 최소화할 수 있게 해 줍니다. 이는 개별 파일 처리에 사용되던 Babel과 출력 번들을 최소화하던 Terser를 대체합니다.

Next.js Compiler를 사용한 컴파일은 Babel보다 17배 빠르며 Next.js 12 버전부터 기본 활성화되어 있습니다. 기존 Babel 구성을 사용하거나 [지원되지 않는 기능](https://nextjs.org/docs/architecture/nextjs-compiler#unsupported-features)을 사용하는 경우, 애플리케이션은 Next.js Compiler를 옵트아웃하고 Babel을 계속 사용합니다.

## Why SWC?[](https://nextjs.org/docs/architecture/nextjs-compiler#why-swc)

[SWC](https://swc.rs/)는 차세대 고성능 개발자 도구를 위한 확장 가능한 Rust 기반 플랫폼입니다.

SWC는 컴파일, 최소화, 번들링 등 다양한 용도로 사용할 수 있으며 확장을 염두에 두고 설계되었습니다. 기본 제공 또는 사용자 정의 코드 변환을 실행하도록 호출할 수 있고, 이를 실행하는 상위 수준의 도구가 Next.js 같은 프레임워크입니다.

SWC를 기반으로 선택한 이유는 다음과 같습니다.

  * **확장성:** SWC는 라이브러리를 포크하거나 설계 제약을 우회하지 않고도 Next.js 내부에서 크레이트로 사용할 수 있습니다.
  * **성능:** SWC로 전환하면서 Next.js에서 Fast Refresh는 약 3배, 빌드는 약 5배 빨라졌으며 여전히 최적화 여지가 있습니다.
  * **WebAssembly:** Rust의 WASM 지원은 모든 플랫폼을 지원하고 Next.js 개발 경험을 어디서나 제공하기 위해 필수적입니다.
  * **커뮤니티:** Rust 커뮤니티와 생태계는 뛰어나며 계속 성장하고 있습니다.

## Supported Features[](https://nextjs.org/docs/architecture/nextjs-compiler#supported-features)

### Styled Components[](https://nextjs.org/docs/architecture/nextjs-compiler#styled-components)

`babel-plugin-styled-components`를 Next.js Compiler로 포팅 중입니다.

먼저 Next.js를 최신 버전으로 업데이트하세요: `npm install next@latest`. 그런 다음 `next.config.js` 파일을 업데이트합니다:

next.config.js
```
    module.exports = {
      compiler: {
        styledComponents: true,
      },
    }
```

고급 사용 사례에서는 styled-components 컴파일을 위해 개별 속성을 구성할 수 있습니다.

> 참고: Next.js에서 `styled-components`를 사용하려면 `ssr`과 `displayName` 변환이 핵심 요구 사항입니다.

next.config.js
```
    module.exports = {
      compiler: {
        // see https://styled-components.com/docs/tooling#babel-plugin for more info on the options.
        styledComponents: {
          // Enabled by default in development, disabled in production to reduce file size,
          // setting this will override the default for all environments.
          displayName?: boolean,
          // Enabled by default.
          ssr?: boolean,
          // Enabled by default.
          fileName?: boolean,
          // Empty by default.
          topLevelImportPaths?: string[],
          // Defaults to ["index"].
          meaninglessFileNames?: string[],
          // Enabled by default.
          minify?: boolean,
          // Enabled by default.
          transpileTemplateLiterals?: boolean,
          // Empty by default.
          namespace?: string,
          // Disabled by default.
          pure?: boolean,
          // Enabled by default.
          cssProp?: boolean,
        },
      },
    }
```

### Jest[](https://nextjs.org/docs/architecture/nextjs-compiler#jest)

Next.js Compiler는 테스트를 트랜스파일하며 다음과 같이 Jest와 Next.js를 함께 구성하는 일을 단순화합니다.

  * `.css`, `.module.css`(및 해당 `.scss` 변형)와 이미지 임포트 자동 모킹
  * SWC를 사용해 `transform`을 자동 설정
  * `.env`(및 모든 변형)를 `process.env`에 로드
  * 테스트 해석과 변환에서 `node_modules` 무시
  * 테스트 해석에서 `.next` 무시
  * 실험적 SWC 변환을 활성화하는 플래그를 읽기 위해 `next.config.js` 로드

먼저 Next.js를 최신 버전으로 업데이트하세요: `npm install next@latest`. 그런 다음 `jest.config.js` 파일을 업데이트합니다:

jest.config.js
```
    const nextJest = require('next/jest')

    // Providing the path to your Next.js app which will enable loading next.config.js and .env files
    const createJestConfig = nextJest({ dir: './' })

    // Any custom config you want to pass to Jest
    const customJestConfig = {
      setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
    }

    // createJestConfig is exported in this way to ensure that next/jest can load the Next.js configuration, which is async
    module.exports = createJestConfig(customJestConfig)
```

### Relay[](https://nextjs.org/docs/architecture/nextjs-compiler#relay)

[Relay](https://relay.dev/) 지원을 활성화하려면:

next.config.js
```
    module.exports = {
      compiler: {
        relay: {
          // This should match relay.config.js
          src: './',
          artifactDirectory: './__generated__',
          language: 'typescript',
          eagerEsModules: false,
        },
      },
    }
```

> **알아두면 좋은 점**: Next.js에서는 `pages` 디렉터리 안의 모든 JavaScript 파일을 라우트로 간주합니다. 따라서 `relay-compiler`에서는 `artifactDirectory` 설정을 `pages` 바깥으로 지정해야 합니다. 그렇지 않으면 `relay-compiler`가 `__generated__` 디렉터리의 소스 파일 옆에 파일을 생성하고, 이 파일이 라우트로 간주되어 프로덕션 빌드가 실패합니다.

### Remove React Properties[](https://nextjs.org/docs/architecture/nextjs-compiler#remove-react-properties)

JSX 속성을 제거할 수 있으며, 이는 주로 테스트에 사용됩니다. `babel-plugin-react-remove-properties`와 유사합니다.

기본 정규식 `^data-test`와 일치하는 속성을 제거하려면:

next.config.js
```
    module.exports = {
      compiler: {
        reactRemoveProperties: true,
      },
    }
```

사용자 지정 속성을 제거하려면:

next.config.js
```
    module.exports = {
      compiler: {
        // The regexes defined here are processed in Rust so the syntax is different from
        // JavaScript `RegExp`s. See https://docs.rs/regex.
        reactRemoveProperties: { properties: ['^data-custom$'] },
      },
    }
```

### Remove Console[](https://nextjs.org/docs/architecture/nextjs-compiler#remove-console)

이 변환은 애플리케이션 코드( `node_modules` 제외)에서 모든 `console.*` 호출을 제거합니다. `babel-plugin-transform-remove-console`과 비슷합니다.

모든 `console.*` 호출을 제거하려면:

next.config.js
```
    module.exports = {
      compiler: {
        removeConsole: true,
      },
    }
```

`console.error`를 제외한 `console.*` 출력을 제거하려면:

next.config.js
```
    module.exports = {
      compiler: {
        removeConsole: {
          exclude: ['error'],
        },
      },
    }
```

### Legacy Decorators[](https://nextjs.org/docs/architecture/nextjs-compiler#legacy-decorators)

Next.js는 `jsconfig.json` 또는 `tsconfig.json`에서 `experimentalDecorators`를 자동 감지합니다. 레거시 데코레이터는 `mobx` 같은 라이브러리의 구버전에서 흔히 사용됩니다.

이 플래그는 기존 애플리케이션과의 호환성만을 위해 지원됩니다. 새 애플리케이션에서는 레거시 데코레이터 사용을 권장하지 않습니다.

먼저 Next.js를 최신 버전으로 업데이트하세요: `npm install next@latest`. 그런 다음 `jsconfig.json` 또는 `tsconfig.json` 파일을 업데이트합니다:
```
    {
      "compilerOptions": {
        "experimentalDecorators": true
      }
    }
```

### importSource[](https://nextjs.org/docs/architecture/nextjs-compiler#importsource)

Next.js는 `jsconfig.json` 또는 `tsconfig.json`의 `jsxImportSource`를 자동으로 감지하여 적용합니다. 이는 [Theme UI](https://theme-ui.com) 같은 라이브러리에서 자주 사용됩니다.

먼저 Next.js를 최신 버전으로 업데이트하세요: `npm install next@latest`. 그런 다음 `jsconfig.json` 또는 `tsconfig.json` 파일을 업데이트합니다:
```
    {
      "compilerOptions": {
        "jsxImportSource": "theme-ui"
      }
    }
```

### Emotion[](https://nextjs.org/docs/architecture/nextjs-compiler#emotion)

`@emotion/babel-plugin`을 Next.js Compiler로 포팅 중입니다.

먼저 Next.js를 최신 버전으로 업데이트하세요: `npm install next@latest`. 그런 다음 `next.config.js` 파일을 업데이트합니다:

next.config.js
```

    module.exports = {
      compiler: {
        emotion: boolean | {
          // default is true. It will be disabled when build type is production.
          sourceMap?: boolean,
          // default is 'dev-only'.
          autoLabel?: 'never' | 'dev-only' | 'always',
          // default is '[local]'.
          // Allowed values: `[local]` `[filename]` and `[dirname]`
          // This option only works when autoLabel is set to 'dev-only' or 'always'.
          // It allows you to define the format of the resulting label.
          // The format is defined via string where variable parts are enclosed in square brackets [].
          // For example labelFormat: "my-classname--[local]", where [local] will be replaced with the name of the variable the result is assigned to.
          labelFormat?: string,
          // default is undefined.
          // This option allows you to tell the compiler what imports it should
          // look at to determine what it should transform so if you re-export
          // Emotion's exports, you can still use transforms.
          importMap?: {
            [packageName: string]: {
              [exportName: string]: {
                canonicalImport?: [string, string],
                styledBaseImport?: [string, string],
              }
            }
          },
        },
      },
    }
```

### Minification[](https://nextjs.org/docs/architecture/nextjs-compiler#minification)

Next.js의 swc 컴파일러는 v13부터 기본적으로 최소화에 사용되며 Terser보다 7배 빠릅니다.

> **알아두면 좋은 점:** v15부터 `next.config.js`에서는 최소화를 사용자 지정할 수 없습니다. `swcMinify` 플래그 지원이 제거되었습니다.

### Module Transpilation[](https://nextjs.org/docs/architecture/nextjs-compiler#module-transpilation)

Next.js는 로컬 패키지(모노레포 등)나 외부 의존성(`node_modules`)에서 종속성을 자동으로 트랜스파일하고 번들링할 수 있습니다. 이는 `next-transpile-modules` 패키지를 대체합니다.

next.config.js
```
    module.exports = {
      transpilePackages: ['@acme/ui', 'lodash-es'],
    }
```

### Modularize Imports[](https://nextjs.org/docs/architecture/nextjs-compiler#modularize-imports)

이 옵션은 Next.js 13.5에서 [`optimizePackageImports`](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)로 대체되었습니다. 수동으로 임포트 경로를 구성할 필요가 없는 새 옵션으로 업그레이드하는 것을 권장합니다.

### Define (Replacing variables during build)[](https://nextjs.org/docs/architecture/nextjs-compiler#define-replacing-variables-during-build)

`define` 옵션을 사용하면 빌드 시점에 코드의 변수를 정적으로 치환할 수 있습니다. 이 옵션은 키-값 쌍 객체를 받으며, 키는 치환할 변수, 값은 해당 변수에 대체될 값입니다.

`next.config.js`에서 `compiler.define` 필드를 사용하면 모든 환경(서버, 엣지, 클라이언트)에 변수를 정의할 수 있습니다. 또는 `compiler.defineServer`를 사용해 서버 측(서버 및 엣지) 코드에만 변수를 정의할 수 있습니다:

next.config.js
```
    module.exports = {
      compiler: {
        define: {
          MY_VARIABLE: 'my-string',
          'process.env.MY_ENV_VAR': 'my-env-var',
        },
        defineServer: {
          MY_SERVER_VARIABLE: 'my-server-var',
        },
      },
    }
```

### Build Lifecycle Hooks[](https://nextjs.org/docs/architecture/nextjs-compiler#build-lifecycle-hooks)

Next.js Compiler는 빌드 프로세스의 특정 지점에서 사용자 정의 코드를 실행할 수 있는 라이프사이클 훅을 지원합니다. 현재 지원되는 훅은 다음과 같습니다.

#### runAfterProductionCompile[](https://nextjs.org/docs/architecture/nextjs-compiler#runafterproductioncompile)

프로덕션 빌드 컴파일이 완료된 직후, 타입 검사나 정적 페이지 생성 같은 후속 작업을 실행하기 전에 동작하는 훅 함수입니다. 이 훅은 프로젝트 디렉터리와 빌드 출력 디렉터리 등 프로젝트 메타데이터에 접근할 수 있어 서드파티 도구가 소스맵과 같은 빌드 아웃풋을 수집하는 데 유용합니다.

next.config.js
```
    module.exports = {
      compiler: {
        runAfterProductionCompile: async ({ distDir, projectDir }) => {
          // Your custom code here
        },
      },
    }
```

훅은 다음 속성을 가진 객체를 전달받습니다.

  * `distDir`: 빌드 출력 디렉터리(기본값 `.next`)
  * `projectDir`: 프로젝트 루트 디렉터리

## 실험적 기능[](https://nextjs.org/docs/architecture/nextjs-compiler#experimental-features)

### SWC Trace profiling[](https://nextjs.org/docs/architecture/nextjs-compiler#swc-trace-profiling)

Chromium의 [trace event format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview?mode=html#%21=)으로 SWC 내부 변환 트레이스를 생성할 수 있습니다.

next.config.js
```
    module.exports = {
      experimental: {
        swcTraceProfiling: true,
      },
    }
```

활성화하면 swc는 `.next/` 아래에 `swc-trace-profile-${timestamp}.json` 이름의 트레이스를 생성합니다. Chromium trace viewer(chrome://tracing/, <https://ui.perfetto.dev/>[](https://ui.perfetto.dev/))나 호환 플레임그래프 뷰어(<https://www.speedscope.app/>[](https://www.speedscope.app/))에서 생성된 트레이스를 로드해 시각화할 수 있습니다.

### SWC Plugins (experimental)[](https://nextjs.org/docs/architecture/nextjs-compiler#swc-plugins-experimental)

변환 동작을 커스터마이즈하기 위해 wasm으로 작성된 SWC 실험적 플러그인 지원을 사용하도록 swc 변환을 구성할 수 있습니다.

next.config.js
```
    module.exports = {
      experimental: {
        swcPlugins: [
          [
            'plugin',
            {
              ...pluginOptions,
            },
          ],
        ],
      },
    }
```

`swcPlugins`는 플러그인을 구성하기 위한 튜플 배열을 받습니다. 각 플러그인 튜플에는 플러그인의 경로와 플러그인 설정을 위한 객체가 포함됩니다. 플러그인 경로는 npm 모듈 패키지 이름일 수도 있고 `.wasm` 바이너리 자체에 대한 절대 경로일 수도 있습니다.

## 지원되지 않는 기능[](https://nextjs.org/docs/architecture/nextjs-compiler#unsupported-features)

애플리케이션에 `.babelrc` 파일이 있는 경우 Next.js는 자동으로 Babel을 사용해 개별 파일을 변환하도록 되돌립니다. 이는 커스텀 Babel 플러그인을 활용하는 기존 애플리케이션과의 하위 호환성을 보장합니다.

커스텀 Babel 설정을 사용 중이라면 [구성을 공유해주세요](https://github.com/vercel/next.js/discussions/30174). 가능한 한 많은 일반적인 Babel 변환을 포팅하고 향후 플러그인 지원을 제공하기 위해 노력하고 있습니다.

## 버전 기록[](https://nextjs.org/docs/architecture/nextjs-compiler#version-history)

Version| Changes
---|---
`v13.1.0`| [Module Transpilation](https://nextjs.org/blog/next-13-1#built-in-module-transpilation-stable) 및 [Modularize Imports](https://nextjs.org/blog/next-13-1#import-resolution-for-smaller-bundles) 안정화.
`v13.0.0`| SWC Minifier 기본 활성화.
`v12.3.0`| SWC Minifier [stable](https://nextjs.org/blog/next-12-3#swc-minifier-stable).
`v12.2.0`| [SWC Plugins](https://nextjs.org/docs/architecture/nextjs-compiler#swc-plugins-experimental) 실험적 지원 추가.
`v12.1.0`| Styled Components, Jest, Relay, Remove React Properties, Legacy Decorators, Remove Console, jsxImportSource 지원 추가.
`v12.0.0`| Next.js Compiler [도입](https://nextjs.org/blog/next-12).