---
title: 'CLI: next CLI'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/cli/next'
---

# CLI: next CLI | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/cli/next

[API Reference](https://nextjs.org/docs/app/api-reference)[CLI](https://nextjs.org/docs/app/api-reference/cli)next CLI

페이지 복사

# next CLI

최종 업데이트: 2026년 2월 20일

Next.js CLI를 사용하면 애플리케이션을 개발, 빌드, 시작 등 다양한 작업을 수행할 수 있습니다.

기본 사용법:

pnpmnpmyarnbun

터미널
[code]
    pnpm next [command] [options]
[/code]

> **알아두면 좋아요**: `npm run`과 함께 사용할 때는 npm이 CLI 플래그를 `next`로 전달하도록 플래그 앞에 `--`를 붙이세요. `pnpm`, `yarn`, `bun`에서는 필요하지 않습니다.

## Reference[](https://nextjs.org/docs/app/api-reference/cli/next#reference)

다음 옵션을 사용할 수 있습니다:

Options| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시  
`-v` or `--version`| Next.js 버전 번호를 출력  
  
### Commands[](https://nextjs.org/docs/app/api-reference/cli/next#commands)

다음 명령을 사용할 수 있습니다:

Command| Description  
---|---  
[`dev`](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options)| 핫 모듈 리로딩, 오류 보고 등과 함께 개발 모드에서 Next.js를 시작합니다.  
[`build`](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)| 애플리케이션의 최적화된 프로덕션 빌드를 생성하며 각 라우트 정보를 표시합니다.  
[`start`](https://nextjs.org/docs/app/api-reference/cli/next#next-start-options)| 프로덕션 모드에서 Next.js를 시작합니다. 먼저 `next build`로 컴파일되어 있어야 합니다.  
[`info`](https://nextjs.org/docs/app/api-reference/cli/next#next-info-options)| Next.js 버그 보고에 활용할 수 있는 현재 시스템 정보를 출력합니다.  
[`telemetry`](https://nextjs.org/docs/app/api-reference/cli/next#next-telemetry-options)| Next.js의 완전 익명 텔레메트리 수집을 활성화하거나 비활성화합니다.  
[`typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)| 전체 빌드 없이 라우트, 페이지, 레이아웃, 라우트 핸들러에 대한 TypeScript 정의를 생성합니다.  
[`upgrade`](https://nextjs.org/docs/app/api-reference/cli/next#next-upgrade-options)| Next.js 애플리케이션을 최신 버전으로 업그레이드합니다.  
[`experimental-analyze`](https://nextjs.org/docs/app/api-reference/cli/next#next-experimental-analyze-options)| Turbopack을 사용해 번들 출력을 분석하며 빌드 아티팩트는 생성하지 않습니다.  
  
> **알아두면 좋아요**: 명령 없이 `next`를 실행하면 `next dev`의 별칭입니다.

### `next dev` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options)

`next dev`는 핫 모듈 리로딩(HMR), 오류 보고 등을 포함한 개발 모드로 애플리케이션을 시작합니다. `next dev` 실행 시 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 빌드할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--turbopack`| [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 강제로 활성화합니다(기본 활성화). `--turbo`로도 사용할 수 있습니다.  
`--webpack`| 개발용 기본 번들러인 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) 대신 Webpack을 사용합니다.  
`-p` or `--port <port>`| 애플리케이션을 시작할 포트 번호를 지정합니다. 기본값: 3000, env: PORT  
`-H`or `--hostname <hostname>`| 애플리케이션을 시작할 호스트 이름을 지정합니다. 네트워크의 다른 디바이스에서 접근 가능하게 할 때 유용합니다. 기본값: 0.0.0.0  
`--experimental-https`| HTTPS로 서버를 시작하고 자체 서명 인증서를 생성합니다.  
`--experimental-https-key <path>`| HTTPS 키 파일 경로입니다.  
`--experimental-https-cert <path>`| HTTPS 인증서 파일 경로입니다.  
`--experimental-https-ca <path>`| HTTPS 인증 기관 파일 경로입니다.  
`--experimental-upload-trace <traceUrl>`| 디버깅 트레이스 일부를 원격 HTTP URL로 전송합니다.  
  
### `next build` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)

`next build`는 애플리케이션의 최적화된 프로덕션 빌드를 생성하며 출력에는 각 라우트 정보가 포함됩니다. 예:

터미널
[code]
    Route (app)
    ┌ ○ /_not-found
    └ ƒ /products/[id]
     
    ○  (Static)   prerendered as static content
    ƒ  (Dynamic)  server-rendered on demand
[/code]

`next build` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 빌드할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--turbopack`| [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 강제로 활성화합니다(기본 활성화). `--turbo`로도 사용할 수 있습니다.  
`--webpack`| Webpack으로 빌드합니다.  
`-d` or `--debug`| 더 자세한 빌드 출력을 활성화합니다. 이 플래그를 사용하면 rewrite, redirect, header 등의 추가 빌드 정보가 표시됩니다.  
|   
`--profile`| 프로덕션 [React 프로파일링](https://react.dev/reference/react/Profiler)을 활성화합니다.  
`--no-lint`| 린팅을 비활성화합니다. _참고: Next 16에서는 `next build`에서 린팅이 제거됩니다. Next 15.5+에서 `eslint`가 아닌 린터를 사용 중이라면 빌드 중 린팅이 실행되지 않습니다._  
`--no-mangling`| [mangling](https://en.wikipedia.org/wiki/Name_mangling)을 비활성화합니다. 성능에 영향을 줄 수 있으므로 디버깅 목적에만 사용하세요.  
`--experimental-app-only`| App Router 라우트만 빌드합니다.  
`--experimental-build-mode [mode]`| 실험적 빌드 모드를 사용합니다. (선택: "compile", "generate", 기본값: "default")  
`--debug-prerender`| 개발 중 프리렌더 오류를 디버그합니다.  
`--debug-build-paths=<patterns>`| 디버깅을 위해 특정 라우트만 빌드합니다.  
  
### `next start` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-start-options)

`next start`는 애플리케이션을 프로덕션 모드로 시작합니다. 먼저 [`next build`](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)로 컴파일해야 합니다.

`next start` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 시작할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`-p` or `--port <port>`| 애플리케이션을 시작할 포트 번호를 지정합니다. (기본값: 3000, env: PORT)  
`-H` or `--hostname <hostname>`| 애플리케이션을 시작할 호스트 이름을 지정합니다(기본값: 0.0.0.0).  
`--keepAliveTimeout <keepAliveTimeout>`| 비활성 연결을 닫기 전까지 대기할 최대 밀리초를 지정합니다.  
  
### `next info` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-info-options)

`next info`는 [GitHub issue](https://github.com/vercel/next.js/issues)를 열 때 Next.js 버그를 보고하는 데 사용할 수 있는 현재 시스템 관련 정보를 출력합니다. 여기에는 OS 플랫폼/아키텍처/버전, 바이너리(Node.js, npm, Yarn, pnpm), 패키지 버전(`next`, `react`, `react-dom`) 등이 포함됩니다.

출력 예시는 다음과 같습니다:

터미널
[code]
    Operating System:
      Platform: darwin
      Arch: arm64
      Version: Darwin Kernel Version 23.6.0
      Available memory (MB): 65536
      Available CPU cores: 10
    Binaries:
      Node: 20.12.0
      npm: 10.5.0
      Yarn: 1.22.19
      pnpm: 9.6.0
    Relevant Packages:
      next: 15.0.0-canary.115 // Latest available version is detected (15.0.0-canary.115).
      eslint-config-next: 14.2.5
      react: 19.0.0-rc
      react-dom: 19.0.0
      typescript: 5.5.4
    Next.js Config:
      output: N/A
[/code]

`next info` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시  
`--verbose`| 디버깅을 위한 추가 정보를 수집  
  
### `next telemetry` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-telemetry-options)

Next.js는 일반 사용에 대한 **완전 익명** 텔레메트리 데이터를 수집합니다. 이 익명 프로그램 참여는 선택 사항이며 원하지 않으면 언제든지 옵트아웃할 수 있습니다.

`next telemetry` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`--enable`| Next.js 텔레메트리 수집을 활성화합니다.  
`--disable`| Next.js 텔레메트리 수집을 비활성화합니다.  
  
[Telemetry](https://nextjs.org/telemetry)에 대해 더 알아보기.

### `next typegen` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)

`next typegen`은 전체 빌드 없이 애플리케이션 라우트에 대한 TypeScript 정의를 생성합니다. IDE 자동완성과 라우트 사용에 대한 CI 타입 검증에 유용합니다.

기존에는 `next dev` 또는 `next build` 중에만 라우트 타입이 생성되어 `tsc --noEmit`을 직접 실행해도 라우트 타입을 검증할 수 없었습니다. 이제 타입을 독립적으로 생성해 외부에서 검증할 수 있습니다:

터미널
[code]
    # Generate route types first, then validate with TypeScript
    next typegen && tsc --noEmit
     
    # Or in CI workflows for type checking without building
    next typegen && npm run type-check
[/code]

`next typegen` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 타입을 생성할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
  
출력 파일은 `<distDir>/types`(일반적으로 `.next/dev/types` 또는 `.next/types`, [`isolatedDevBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild) 참고)에 작성됩니다:

터미널
[code]
    next typegen
    # or for a specific app
    next typegen ./apps/web
[/code]

또한 `next typegen`은 `next-env.d.ts` 파일을 생성하므로 `.gitignore`에 `next-env.d.ts`를 추가하는 것을 권장합니다.

`next-env.d.ts`는 Next.js 타입을 프로젝트에서 사용할 수 있도록 `tsconfig.json`에 포함됩니다.

타입 검사를 실행하기 전에 `next-env.d.ts`가 존재하도록 `next typegen`을 실행하세요. `next dev`와 `next build`도 `next-env.d.ts`를 생성하지만, 예를 들어 CI/CD 환경에서는 단순 타입 검사를 위해 이러한 명령을 실행하고 싶지 않을 수 있습니다.

> **알아두면 좋아요**: `next typegen`은 프로덕션 빌드 단계에서 `next.config.js`, `next.config.mjs`, `next.config.ts` 등 Next.js 구성을 로드합니다. 구성 로드가 제대로 이루어지도록 필요한 환경 변수와 의존성이 준비되어 있는지 확인하세요.

### `next upgrade` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-upgrade-options)

`next upgrade`는 Next.js 애플리케이션을 최신 버전으로 업그레이드합니다.

`next upgrade` 명령에서는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 업그레이드할 Next.js 애플리케이션이 있는 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--revision <revision>`| 업그레이드할 Next.js 버전 또는 태그를 지정합니다(예: `latest`, `canary`, `15.0.0`). 기본값은 현재 설치된 릴리스 채널입니다.  
`--verbose`| 업그레이드 중 자세한 출력을 표시합니다.  
  
### `next experimental-analyze` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-experimental-analyze-options)

`next experimental-analyze`는 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 사용해 애플리케이션 번들 출력을 분석합니다. JavaScript, CSS, 기타 에셋을 포함해 번들의 크기와 구성을 파악하는 데 도움이 되며 애플리케이션 빌드는 생성하지 않습니다.

pnpmnpmyarnbun

터미널
[code]
    pnpm next experimental-analyze
[/code]

기본적으로 분석이 완료되면 로컬 서버를 시작하여 브라우저에서 번들 구성을 탐색할 수 있습니다. 분석 도구에서는 다음과 같은 작업을 수행할 수 있습니다:

* 라우트별로 번들을 필터링하고 클라이언트 뷰와 서버 뷰를 전환합니다
  * 모듈이 포함된 이유를 보여주는 전체 import 체인을 확인합니다
  * 서버에서 클라이언트로 이어지는 컴포넌트 경계와 동적 import 전반에 걸친 import 경로를 추적합니다

최적화 전략은 [패키지 번들링](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles)을 참고하세요.

서버를 시작하지 않고 분석 출력을 디스크에 기록하려면 `--output` 플래그를 사용하세요. 출력은 `.next/diagnostics/analyze`에 기록되며, 다른 위치로 복사하거나 다른 사람과 공유할 수 있는 정적 파일을 포함합니다:

터미널
[code]
    # Write output to .next/diagnostics/analyze
    npx next experimental-analyze --output
     
    # Copy the output for comparison with a future analysis
    cp -r .next/diagnostics/analyze ./analyze-before-refactor
[/code]

`next experimental-analyze` 명령에는 다음 옵션이 있습니다:

옵션| 설명  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 분석할 디렉터리입니다. 제공하지 않으면 현재 디렉터리를 사용합니다.  
`--no-mangling`| [mangling](https://en.wikipedia.org/wiki/Name_mangling)을 비활성화합니다. 성능에 영향을 줄 수 있으므로 디버깅 용도로만 사용하세요.  
`--profile`| 프로덕션 [React 프로파일링](https://react.dev/reference/react/Profiler)을 활성화합니다. 성능에 영향을 줄 수 있습니다.  
`-o, --output`| 서버를 시작하지 않고 분석 파일을 디스크에 기록합니다. 출력은 `.next/diagnostics/analyze`에 기록됩니다.  
`--port <port>`| 애널라이저를 제공할 포트 번호를 지정합니다. (기본값: 4000, 환경 변수: PORT)  

## 예제[](https://nextjs.org/docs/app/api-reference/cli/next#examples)

### 프리렌더 오류 디버깅[](https://nextjs.org/docs/app/api-reference/cli/next#debugging-prerender-errors)

`next build` 중 프리렌더링 오류가 발생한다면 `--debug-prerender` 플래그를 전달해 보다 자세한 출력을 확인할 수 있습니다:

터미널
[code]
    next build --debug-prerender
[/code]

이는 디버깅을 쉽게 하기 위해 몇 가지 실험적 옵션을 활성화합니다:

  * 서버 코드 난축소를 비활성화합니다:
    * `experimental.serverMinification = false`
    * `experimental.turbopackMinify = false`
  * 서버 번들을 위한 소스 맵을 생성합니다:
    * `experimental.serverSourceMaps = true`
  * 프리렌더링에 사용되는 하위 프로세스에서 소스 맵을 소비할 수 있게 합니다:
    * `enablePrerenderSourceMaps = true`
  * 첫 번째 프리렌더 오류 이후에도 빌드를 계속 진행하여 모든 문제를 한 번에 확인할 수 있게 합니다:
    * `experimental.prerenderEarlyExit = false`

이렇게 하면 빌드 출력에서 더 읽기 쉬운 스택 트레이스와 코드 프레임을 확인할 수 있습니다.

> **경고** : `--debug-prerender`는 개발 환경에서의 디버깅 전용입니다. 성능에 영향을 줄 수 있으므로 `--debug-prerender`로 생성한 빌드를 프로덕션에 배포하지 마세요.

### 특정 라우트만 빌드하기[](https://nextjs.org/docs/app/api-reference/cli/next#building-specific-routes)

대규모 애플리케이션을 작업할 때 더 빠르게 디버깅할 수 있도록 `--debug-build-paths` 옵션을 사용해 App Router와 Pages Router에서 특정 라우트만 빌드할 수 있습니다. `--debug-build-paths`는 쉼표로 구분된 파일 경로를 받으며 glob 패턴을 지원합니다:

터미널
[code]
    # Build a specific route
    next build --debug-build-paths="app/page.tsx"
     
    # Build more than one route
    next build --debug-build-paths="app/page.tsx,pages/index.tsx"
     
    # Use glob patterns
    next build --debug-build-paths="app/**/page.tsx"
    next build --debug-build-paths="pages/*.tsx"
[/code]

### 기본 포트 변경하기[](https://nextjs.org/docs/app/api-reference/cli/next#changing-the-default-port)

기본적으로 Next.js는 개발 중이거나 `next start`를 사용할 때 `http://localhost:3000`을 사용합니다. 기본 포트는 `-p` 옵션으로 다음과 같이 변경할 수 있습니다:

터미널
[code]
    next dev -p 4000
[/code]

또는 `PORT` 환경 변수를 사용할 수 있습니다:

터미널
[code]
    PORT=4000 next dev
[/code]

> **알아두면 좋아요** : HTTP 서버를 부팅하는 단계가 다른 코드보다 먼저 실행되므로 `.env`에서 `PORT`를 설정할 수 없습니다.

### 개발 중 HTTPS 사용하기[](https://nextjs.org/docs/app/api-reference/cli/next#using-https-during-development)

웹훅이나 인증과 같은 특정 사용 사례에서는 `localhost`에서도 안전한 환경을 위해 [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)를 사용할 수 있습니다. Next.js는 `next dev`와 함께 `--experimental-https` 플래그를 사용해 자체 서명된 인증서를 생성할 수 있습니다:

터미널
[code]
    next dev --experimental-https
[/code]

생성된 인증서를 사용하면 Next.js 개발 서버는 `https://localhost:3000`에서 실행됩니다. 포트를 `-p`, `--port`, 또는 `PORT`로 지정하지 않는 한 기본 포트 `3000`이 사용됩니다.

`--experimental-https-key`와 `--experimental-https-cert`로 사용자 지정 인증서와 키를 제공할 수도 있습니다. 선택적으로 `--experimental-https-ca`를 사용해 사용자 지정 CA 인증서를 제공할 수 있습니다.

터미널
[code]
    next dev --experimental-https --experimental-https-key ./certificates/localhost-key.pem --experimental-https-cert ./certificates/localhost.pem
[/code]

`next dev --experimental-https`는 개발용으로만 설계되었으며 [`mkcert`](https://github.com/FiloSottile/mkcert)로 로컬에서 신뢰할 수 있는 인증서를 생성합니다. 프로덕션에서는 신뢰할 수 있는 기관이 발급한 인증서를 사용하세요.

### 다운스트림 프록시용 타임아웃 구성하기[](https://nextjs.org/docs/app/api-reference/cli/next#configuring-a-timeout-for-downstream-proxies)

다운스트림 프록시(예: AWS ELB/ALB와 같은 로드 밸런서) 뒤에 Next.js를 배포할 때는, Next의 기본 HTTP 서버 keep-alive 타임아웃을 다운스트림 프록시의 타임아웃보다 _더 길게_ 설정하는 것이 중요합니다. 그렇지 않으면 특정 TCP 연결에 대해 keep-alive 타임아웃이 도달하는 즉시 Node.js가 다운스트림 프록시에 알리지 않고 연결을 종료합니다. 이로 인해 다운스트림 프록시가 이미 종료된 연결을 재사용하려 할 때마다 프록시 오류가 발생합니다.

프로덕션 Next.js 서버의 타임아웃 값을 구성하려면 `next start`에 `--keepAliveTimeout`(밀리초 단위)을 다음과 같이 전달하세요:

터미널
[code]
    next start --keepAliveTimeout 70000
[/code]

### Node.js 인수를 전달하기[](https://nextjs.org/docs/app/api-reference/cli/next#passing-nodejs-arguments)

`next` 명령에는 어떤 [Node 인수](https://nodejs.org/api/cli.html#cli_node_options_options)든 전달할 수 있습니다. 예를 들어:

터미널
[code]
    NODE_OPTIONS='--throw-deprecation' next
    NODE_OPTIONS='-r esm' next
    NODE_OPTIONS='--inspect' next
[/code]

버전| 변경 사항  
---|---  
`v16.1.0`| `next experimental-analyze` 명령이 추가되었습니다  
`v16.0.0`| JS 번들 크기 메트릭이 `next build`에서 제거되었습니다  
`v15.5.0`| `next typegen` 명령이 추가되었습니다  
`v15.4.0`| 프리렌더 오류를 디버깅할 수 있도록 `next build`에 `--debug-prerender` 옵션이 추가되었습니다  

도움이 되었나요?

지원됨.

보내기
