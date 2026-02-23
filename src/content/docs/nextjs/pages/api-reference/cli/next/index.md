---
title: 'CLI: next CLI'
description: 'Next.js CLI를 사용하면 애플리케이션을 개발하고, 빌드하고, 시작하는 등 다양한 작업을 수행할 수 있습니다.'
---

# CLI: next CLI | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/cli/next

[API Reference](https://nextjs.org/docs/pages/api-reference)[CLI](https://nextjs.org/docs/pages/api-reference/cli)next CLI

페이지 복사

# next CLI

마지막 업데이트 2026년 2월 20일

Next.js CLI를 사용하면 애플리케이션을 개발하고, 빌드하고, 시작하는 등 다양한 작업을 수행할 수 있습니다.

기본 사용법:

pnpmnpmyarnbun

Terminal
[code]
    pnpm next [command] [options]
[/code]

> **참고**: `npm run`을 사용할 때는 CLI 플래그 앞에 `--`를 붙여 npm이 플래그를 `next`로 전달하도록 하세요. `pnpm`, `yarn`, `bun`에는 필요하지 않습니다.

## Reference[](https://nextjs.org/docs/pages/api-reference/cli/next#reference)

다음 옵션을 사용할 수 있습니다:

Options| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시합니다.  
`-v` or `--version`| Next.js 버전 번호를 출력합니다.  
  
### Commands[](https://nextjs.org/docs/pages/api-reference/cli/next#commands)

다음 명령을 사용할 수 있습니다:

Command| Description  
---|---  
[`dev`](https://nextjs.org/docs/pages/api-reference/cli/next#next-dev-options)| 핫 모듈 리로딩, 오류 보고 등을 포함한 개발 모드로 Next.js를 시작합니다.  
[`build`](https://nextjs.org/docs/pages/api-reference/cli/next#next-build-options)| 각 경로에 대한 정보를 표시하면서 애플리케이션의 최적화된 프로덕션 빌드를 생성합니다.  
[`start`](https://nextjs.org/docs/pages/api-reference/cli/next#next-start-options)| 프로덕션 모드로 Next.js를 시작합니다. 먼저 `next build`로 컴파일해야 합니다.  
[`info`](https://nextjs.org/docs/pages/api-reference/cli/next#next-info-options)| Next.js 버그를 보고할 때 사용할 수 있는 현재 시스템의 관련 세부 정보를 출력합니다.  
[`telemetry`](https://nextjs.org/docs/pages/api-reference/cli/next#next-telemetry-options)| Next.js의 완전히 익명인 텔레메트리 수집을 활성화하거나 비활성화합니다.  
[`typegen`](https://nextjs.org/docs/pages/api-reference/cli/next#next-typegen-options)| 전체 빌드 없이 라우트, 페이지, 레이아웃, 라우트 핸들러에 대한 TypeScript 정의를 생성합니다.  
[`upgrade`](https://nextjs.org/docs/pages/api-reference/cli/next#next-upgrade-options)| Next.js 애플리케이션을 최신 버전으로 업그레이드합니다.  
[`experimental-analyze`](https://nextjs.org/docs/pages/api-reference/cli/next#next-experimental-analyze-options)| Turbopack을 사용해 번들 출력을 분석합니다. 빌드 아티팩트는 생성하지 않습니다.  
  
> **참고**: 명령 없이 `next`를 실행하면 `next dev`의 별칭입니다.

### `next dev` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-dev-options)

`next dev`는 핫 모듈 리로딩(HMR), 오류 보고 등과 함께 애플리케이션을 개발 모드로 시작합니다. `next dev` 실행 시 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 빌드할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--turbopack`| [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 강제로 활성화합니다(기본값). `--turbo`로도 사용할 수 있습니다.  
`--webpack`| 개발 시 기본 번들러인 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) 대신 Webpack을 사용합니다.  
`-p` or `--port <port>`| 애플리케이션을 시작할 포트 번호를 지정합니다. 기본값: 3000, env: PORT  
`-H`or `--hostname <hostname>`| 애플리케이션을 시작할 호스트 이름을 지정합니다. 네트워크의 다른 기기에서 애플리케이션을 사용할 수 있게 할 때 유용합니다. 기본값: 0.0.0.0  
`--experimental-https`| HTTPS로 서버를 시작하고 자체 서명 인증서를 생성합니다.  
`--experimental-https-key <path>`| HTTPS 키 파일 경로입니다.  
`--experimental-https-cert <path>`| HTTPS 인증서 파일 경로입니다.  
`--experimental-https-ca <path>`| HTTPS 인증 기관 파일 경로입니다.  
`--experimental-upload-trace <traceUrl>`| 디버깅 트레이스의 일부를 원격 HTTP URL로 보고합니다.  
  
### `next build` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-build-options)

`next build`는 애플리케이션의 최적화된 프로덕션 빌드를 생성합니다. 출력에는 각 경로에 대한 정보가 표시됩니다. 예:

Terminal
[code]
    Route (app)
    ┌ ○ /_not-found
    └ ƒ /products/[id]
     
    ○  (Static)   prerendered as static content
    ƒ  (Dynamic)  server-rendered on demand
[/code]

`next build` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 빌드할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--turbopack`| [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 강제로 활성화합니다(기본값). `--turbo`로도 사용할 수 있습니다.  
`--webpack`| Webpack으로 빌드합니다.  
`-d` or `--debug`| 더 자세한 빌드 출력을 활성화합니다. 이 플래그를 켜면 리라이트, 리디렉트, 헤더 같은 추가 빌드 출력이 표시됩니다.  
|   
`--profile`| 프로덕션용 [React 프로파일링](https://react.dev/reference/react/Profiler)을 활성화합니다.  
`--no-lint`| 린팅을 비활성화합니다. _참고: Next 16에서는 `next build`에서 린팅이 제거됩니다. eslint가 아닌 다른 린터를 사용하는 Next 15.5+에서는 빌드 중 린팅이 실행되지 않습니다._  
`--no-mangling`| [맹글링](https://en.wikipedia.org/wiki/Name_mangling)을 비활성화합니다. 성능에 영향을 줄 수 있으므로 디버깅 용도로만 사용하세요.  
`--experimental-app-only`| App Router 라우트만 빌드합니다.  
`--experimental-build-mode [mode]`| 실험적 빌드 모드를 사용합니다. (선택: "compile", "generate", 기본값: "default")  
`--debug-prerender`| 개발 환경에서 프리렌더 오류를 디버그합니다.  
`--debug-build-paths=<patterns>`| 특정 라우트만 빌드하여 디버깅합니다.  
  
### `next start` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-start-options)

`next start`는 애플리케이션을 프로덕션 모드로 시작합니다. 먼저 [`next build`](https://nextjs.org/docs/pages/api-reference/cli/next#next-build-options)로 컴파일해야 합니다.

`next start` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 애플리케이션을 시작할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`-p` or `--port <port>`| 애플리케이션을 시작할 포트 번호를 지정합니다. (기본값: 3000, env: PORT)  
`-H` or `--hostname <hostname>`| 애플리케이션을 시작할 호스트 이름을 지정합니다(기본값: 0.0.0.0).  
`--keepAliveTimeout <keepAliveTimeout>`| 비활성 연결을 닫기 전까지 대기할 최대 밀리초를 지정합니다.  
  
### `next info` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-info-options)

`next info`는 [GitHub issue](https://github.com/vercel/next.js/issues)를 열 때 Next.js 버그를 보고하는 데 사용할 수 있는 현재 시스템의 관련 정보를 출력합니다. 이 정보에는 OS 플랫폼/아키텍처/버전, 바이너리(Node.js, npm, Yarn, pnpm), 패키지 버전(`next`, `react`, `react-dom`) 등이 포함됩니다.

출력 예시는 다음과 같습니다:

Terminal
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

`next info` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h` or `--help`| 사용 가능한 모든 옵션을 표시합니다.  
`--verbose`| 디버깅을 위한 추가 정보를 수집합니다.  
  
### `next telemetry` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-telemetry-options)

Next.js는 일반적인 사용량에 대한 **완전히 익명인** 텔레메트리 데이터를 수집합니다. 이 익명 프로그램 참여는 선택 사항이며, 원하지 않으면 언제든지 옵트아웃할 수 있습니다.

`next telemetry` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`--enable`| Next.js 텔레메트리 수집을 활성화합니다.  
`--disable`| Next.js 텔레메트리 수집을 비활성화합니다.  
  
[Telemetry](https://nextjs.org/telemetry)에 대해 더 알아보세요.

### `next typegen` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-typegen-options)

`next typegen`은 전체 빌드를 수행하지 않고 애플리케이션 라우트에 대한 TypeScript 정의를 생성합니다. 이는 IDE 자동 완성 및 라우트 사용의 CI 타입 검증에 유용합니다.

이전에는 `next dev` 또는 `next build` 중에만 라우트 타입이 생성되어 `tsc --noEmit`을 직접 실행해도 라우트 타입을 검증할 수 없었습니다. 이제 타입을 독립적으로 생성하고 외부에서 검증할 수 있습니다:

Terminal
[code]
    # Generate route types first, then validate with TypeScript
    next typegen && tsc --noEmit
     
    # Or in CI workflows for type checking without building
    next typegen && npm run type-check
[/code]

`next typegen` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 타입을 생성할 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
  
출력 파일은 `<distDir>/types`(일반적으로: `.next/dev/types` 또는 `.next/types`, [`isolatedDevBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild) 참조)에 기록됩니다:

Terminal
[code]
    next typegen
    # or for a specific app
    next typegen ./apps/web
[/code]

또한 `next typegen`은 `next-env.d.ts` 파일을 생성합니다. `next-env.d.ts`를 `.gitignore`에 추가하는 것을 권장합니다.

`next-env.d.ts` 파일은 Next.js 타입을 프로젝트에서 사용할 수 있도록 `tsconfig.json`에 포함됩니다.

타입 체크 전에 `next-env.d.ts`가 존재하도록 하려면 `next typegen`을 실행하세요. `next dev`와 `next build`도 `next-env.d.ts`를 생성하지만, 예를 들어 CI/CD 환경에서 단순히 타입 체크만 하기 위해 이 명령들을 실행하는 것은 바람직하지 않을 수 있습니다.

> **참고**: `next typegen`은 프로덕션 빌드 단계에서 Next.js 구성(`next.config.js`, `next.config.mjs`, `next.config.ts`)을 로드합니다. 구성 파일이 올바르게 로드되도록 필요한 환경 변수와 의존성이 준비되어 있는지 확인하세요.

### `next upgrade` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-upgrade-options)

`next upgrade`는 Next.js 애플리케이션을 최신 버전으로 업그레이드합니다.

`next upgrade` 명령에서 사용할 수 있는 옵션은 다음과 같습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 표시합니다.  
`[directory]`| 업그레이드할 Next.js 애플리케이션이 있는 디렉터리입니다. 지정하지 않으면 현재 디렉터리를 사용합니다.  
`--revision <revision>`| 업그레이드할 Next.js 버전 또는 태그를 지정합니다(예: `latest`, `canary`, `15.0.0`). 기본값은 현재 설치된 릴리스 채널입니다.  
`--verbose`| 업그레이드 과정에서 자세한 출력을 표시합니다.  
  
### `next experimental-analyze` options[](https://nextjs.org/docs/pages/api-reference/cli/next#next-experimental-analyze-options)

`next experimental-analyze`는 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)을 사용해 애플리케이션의 번들 출력을 분석합니다. 이 명령은 JavaScript, CSS, 기타 에셋을 포함한 번들의 크기와 구성을 이해하는 데 도움이 됩니다. 애플리케이션 빌드를 생성하지 않습니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm next experimental-analyze
[/code]

기본적으로 이 명령은 분석이 완료된 후 로컬 서버를 시작하여 브라우저에서 번들 구성을 탐색할 수 있게 합니다. 분석기는 다음을 수행할 수 있습니다:

* 경로별로 번들을 필터링하고 클라이언트와 서버 뷰 사이를 전환합니다
  * 모듈이 포함된 이유를 보여 주는 전체 import 체인을 확인합니다
  * 서버에서 클라이언트로 넘어가는 컴포넌트 경계와 dynamic import 전반에 걸쳐 import를 추적합니다

최적화 전략은 [Package Bundling](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles)을 참고하세요.

서버를 시작하지 않고 분석 결과를 디스크에 기록하려면 `--output` 플래그를 사용하세요. 출력은 `.next/diagnostics/analyze`에 작성되며, 다른 위치로 복사하거나 다른 사람과 공유할 수 있는 정적 파일을 포함합니다:

Terminal
[code]
    # Write output to .next/diagnostics/analyze
    npx next experimental-analyze --output
     
    # Copy the output for comparison with a future analysis
    cp -r .next/diagnostics/analyze ./analyze-before-refactor
[/code]

`next experimental-analyze` 명령에는 다음 옵션을 사용할 수 있습니다:

Option| Description  
---|---  
`-h, --help`| 사용 가능한 모든 옵션을 보여줍니다.  
`[directory]`| 애플리케이션을 분석할 디렉터리입니다. 제공하지 않으면 현재 디렉터리를 사용합니다.  
`--no-mangling`| [mangling](https://en.wikipedia.org/wiki/Name_mangling)을 비활성화합니다. 성능에 영향을 줄 수 있으므로 디버깅 목적으로만 사용하세요.  
`--profile`| 프로덕션 [React 프로파일링](https://react.dev/reference/react/Profiler)을 활성화합니다. 성능에 영향을 줄 수 있습니다.  
`-o, --output`| 서버를 시작하지 않고 분석 파일을 디스크에 기록합니다. 출력은 `.next/diagnostics/analyze`에 작성됩니다.  
`--port <port>`| 분석기를 제공할 포트 번호를 지정합니다. (기본값: 4000, env: PORT)  
  
## 예시[](https://nextjs.org/docs/pages/api-reference/cli/next#examples)

### 프리렌더 오류 디버깅[](https://nextjs.org/docs/pages/api-reference/cli/next#debugging-prerender-errors)

`next build` 중에 프리렌더링 오류가 발생하면 `--debug-prerender` 플래그를 전달하여 더 자세한 출력을 받을 수 있습니다:

Terminal
[code]
    next build --debug-prerender
[/code]

이는 디버깅을 쉽게 하기 위해 여러 실험적 옵션을 활성화합니다:

  * 서버 코드 난독화를 비활성화합니다:
    * `experimental.serverMinification = false`
    * `experimental.turbopackMinify = false`
  * 서버 번들에 대한 소스 맵을 생성합니다:
    * `experimental.serverSourceMaps = true`
  * 프리렌더링에 사용되는 하위 프로세스에서 소스 맵 소비를 활성화합니다:
    * `enablePrerenderSourceMaps = true`
  * 첫 번째 프리렌더 오류 이후에도 빌드를 계속 진행하여 모든 문제를 한 번에 확인할 수 있게 합니다:
    * `experimental.prerenderEarlyExit = false`

이를 통해 빌드 출력에서 더 읽기 쉬운 스택 트레이스와 코드 프레임을 확인할 수 있습니다.

> **Warning** : `--debug-prerender`는 개발 중 디버깅 전용입니다. 성능에 영향을 줄 수 있으므로 `--debug-prerender`로 생성된 빌드는 프로덕션에 배포하지 마세요.

### 특정 라우트 빌드[](https://nextjs.org/docs/pages/api-reference/cli/next#building-specific-routes)

대규모 애플리케이션에서 빠르게 디버깅할 수 있도록 `--debug-build-paths` 옵션을 사용해 App Router와 Pages Router에서 특정 라우트만 빌드할 수 있습니다. `--debug-build-paths` 옵션은 쉼표로 구분된 파일 경로를 허용하며 glob 패턴을 지원합니다:

Terminal
[code]
    # Build a specific route
    next build --debug-build-paths="app/page.tsx"
     
    # Build more than one route
    next build --debug-build-paths="app/page.tsx,pages/index.tsx"
     
    # Use glob patterns
    next build --debug-build-paths="app/**/page.tsx"
    next build --debug-build-paths="pages/*.tsx"
[/code]

### 기본 포트 변경[](https://nextjs.org/docs/pages/api-reference/cli/next#changing-the-default-port)

기본적으로 Next.js는 개발 중과 `next start` 실행 시 `http://localhost:3000`을 사용합니다. 기본 포트는 다음과 같이 `-p` 옵션으로 변경할 수 있습니다:

Terminal
[code]
    next dev -p 4000
[/code]

또는 `PORT` 환경 변수를 사용할 수 있습니다:

Terminal
[code]
    PORT=4000 next dev
[/code]

> **Good to know** : HTTP 서버는 다른 코드가 초기화되기 전에 부팅되므로 `.env`에서 `PORT`를 설정할 수 없습니다.

### 개발 중 HTTPS 사용[](https://nextjs.org/docs/pages/api-reference/cli/next#using-https-during-development)

웹후크나 인증 같은 특정 사용 사례에서는 `localhost`에서 보안 환경을 제공하기 위해 [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)를 사용할 수 있습니다. Next.js는 `--experimental-https` 플래그를 사용하는 `next dev`로 자체 서명 인증서를 생성할 수 있습니다:

Terminal
[code]
    next dev --experimental-https
[/code]

생성된 인증서를 사용하면 Next.js 개발 서버가 `https://localhost:3000`에서 실행됩니다. 포트를 `-p`, `--port`, 또는 `PORT`로 지정하지 않는 한 기본 포트 `3000`이 사용됩니다.

`--experimental-https-key`와 `--experimental-https-cert`로 사용자 지정 인증서와 키를 제공할 수도 있습니다. 필요하면 `--experimental-https-ca`로 사용자 지정 CA 인증서를 추가할 수도 있습니다.

Terminal
[code]
    next dev --experimental-https --experimental-https-key ./certificates/localhost-key.pem --experimental-https-cert ./certificates/localhost.pem
[/code]

`next dev --experimental-https`는 개발용으로만 의도되며 [`mkcert`](https://github.com/FiloSottile/mkcert)를 사용해 로컬에서 신뢰할 수 있는 인증서를 생성합니다. 프로덕션에서는 신뢰할 수 있는 기관에서 발급한 인증서를 사용하세요.

### 다운스트림 프록시용 타임아웃 구성[](https://nextjs.org/docs/pages/api-reference/cli/next#configuring-a-timeout-for-downstream-proxies)

Next.js를 다운스트림 프록시(예: AWS ELB/ALB 같은 로드 밸런서) 뒤에 배포할 때는 Next의 기본 HTTP 서버가 [keep-alive 타임아웃](https://nodejs.org/api/http.html#http_server_keepalivetimeout)을 다운스트림 프록시 타임아웃보다 _길게_ 구성되어야 합니다. 그렇지 않으면 특정 TCP 연결에 대해 keep-alive 타임아웃에 도달하는 즉시 Node.js가 다운스트림 프록시에 알리지 않고 연결을 종료하므로, Node.js가 이미 종료한 연결을 프록시가 다시 사용하려 할 때 프록시 오류가 발생합니다.

프로덕션 Next.js 서버의 타임아웃 값을 구성하려면 `next start`에 `--keepAliveTimeout`(밀리초)을 다음과 같이 전달하세요:

Terminal
[code]
    next start --keepAliveTimeout 70000
[/code]

### Node.js 인수 전달[](https://nextjs.org/docs/pages/api-reference/cli/next#passing-nodejs-arguments)

`next` 명령에 [node 인수](https://nodejs.org/api/cli.html#cli_node_options_options)를 전달할 수 있습니다. 예를 들어:

Terminal
[code]
    NODE_OPTIONS='--throw-deprecation' next
    NODE_OPTIONS='-r esm' next
    NODE_OPTIONS='--inspect' next
[/code]

Version| Changes  
---|---  
`v16.1.0`| `next experimental-analyze` 명령이 추가되었습니다  
`v16.0.0`| `next build`에서 JS 번들 크기 지표가 제거되었습니다  
`v15.5.0`| `next typegen` 명령이 추가되었습니다  
`v15.4.0`| 프리렌더 오류 디버깅을 돕기 위한 `next build`의 `--debug-prerender` 옵션이 추가되었습니다  
  
도움이 되었나요?

지원됨.

보내기
