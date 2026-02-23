---
title: '가이드: 개발 환경'
description: 'Next.js는 뛰어난 개발자 경험을 제공하도록 설계되었습니다. 애플리케이션이 커질수록 로컬 개발 중 컴파일 속도가 느려질 수 있습니다. 이 가이드는 일반적인 컴파일 시간 성능 문제를 식별하고 해결하도록 도와줍니다.'
---

# 가이드: 개발 환경 | Next.js

Source URL: https://nextjs.org/docs/app/guides/local-development

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)개발 환경

페이지 복사

# 로컬 개발 환경을 최적화하는 방법

마지막 업데이트 2026년 2월 20일

Next.js는 뛰어난 개발자 경험을 제공하도록 설계되었습니다. 애플리케이션이 커질수록 로컬 개발 중 컴파일 속도가 느려질 수 있습니다. 이 가이드는 일반적인 컴파일 시간 성능 문제를 식별하고 해결하도록 도와줍니다.

## 로컬 개발 vs. 프로덕션[](https://nextjs.org/docs/app/guides/local-development#local-dev-vs-production)

`next dev`를 사용하는 개발 프로세스는 `next build`와 `next start`와는 다릅니다.

`next dev`는 애플리케이션에서 열거나 이동하는 경로만 컴파일합니다. 덕분에 애플리케이션의 모든 경로가 컴파일될 때까지 기다리지 않고도 개발 서버를 시작할 수 있어 더 빠르고 메모리도 덜 사용합니다. 프로덕션 빌드를 실행하면 파일을 축소하거나 콘텐츠 해시를 생성하는 등 로컬 개발에는 필요하지 않은 추가 최적화가 적용됩니다.

## 로컬 개발 성능 향상[](https://nextjs.org/docs/app/guides/local-development#improving-local-dev-performance)

### 1\. 컴퓨터의 백신 프로그램 확인[](https://nextjs.org/docs/app/guides/local-development#1-check-your-computers-antivirus)

백신 소프트웨어는 파일 접근을 느리게 할 수 있습니다. 이는 Windows에서 더 흔하지만, 백신 도구가 설치된 모든 시스템에서 문제가 될 수 있습니다.

Windows에서는 프로젝트를 [Microsoft Defender Antivirus 제외 목록](https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e#bkmk_threat-protection-settings)에 추가할 수 있습니다.

  1. **"Windows 보안"** 앱을 열고 **"바이러스 및 위협 방지"** → **"설정 관리"** → **"제외 추가 또는 제거"**를 선택합니다.
  2. **"폴더"** 제외를 추가하고, 프로젝트 폴더를 선택합니다.



macOS에서는 터미널에서 [Gatekeeper](https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-sec5599b66df/web)를 비활성화할 수 있습니다.

  1. 터미널에서 `sudo spctl developer-mode enable-terminal`을 실행합니다.
  2. **"시스템 설정"** 앱을 열고 **"개인정보 보호 및 보안"** → **"개발자 도구"**를 선택합니다.
  3. 터미널이 목록에 표시되어 있고 활성화되어 있는지 확인합니다. iTerm 또는 Ghostty 같은 서드파티 터미널을 사용한다면 목록에 추가합니다.
  4. 터미널을 재시작합니다.



사용자 또는 회사가 다른 백신 솔루션을 구성했다면 해당 제품의 설정을 점검하세요.

### 2\. Next.js를 업데이트하고 Turbopack 사용[](https://nextjs.org/docs/app/guides/local-development#2-update-nextjs-and-use-turbopack)

항상 최신 버전의 Next.js를 사용하세요. 새로운 버전에는 성능 개선이 자주 포함됩니다.

Turbopack은 이제 Next.js 개발의 기본 번들러이며 webpack 대비 큰 성능 향상을 제공합니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add next@latest
    pnpm dev  # Turbopack is used by default
[/code]

Turbopack 대신 Webpack을 사용해야 한다면 옵트인할 수 있습니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm dev --webpack
[/code]

[Turbopack에 대해 자세히 알아보기](https://nextjs.org/blog/turbopack-for-development-stable). [업그레이드 가이드](https://nextjs.org/docs/app/guides/upgrading)와 코드모드도 참고하세요.

### 3\. import를 점검하세요[](https://nextjs.org/docs/app/guides/local-development#3-check-your-imports)

코드를 import하는 방식은 컴파일과 번들링 시간에 큰 영향을 줄 수 있습니다. [패키지 번들링 최적화](https://nextjs.org/docs/app/guides/package-bundling)를 살펴보고 [Dependency Cruiser](https://github.com/sverweij/dependency-cruiser)나 [Madge](https://github.com/pahen/madge) 같은 도구를 활용하세요.

#### 아이콘 라이브러리[](https://nextjs.org/docs/app/guides/local-development#icon-libraries)

`@material-ui/icons`, `@phosphor-icons/react`, `react-icons` 같은 라이브러리는 몇 개만 사용해도 수천 개의 아이콘을 import할 수 있습니다. 필요한 아이콘만 import하도록 해보세요:
[code] 
    // Instead of this:
    import { TriangleIcon } from '@phosphor-icons/react'
     
    // Do this:
    import { TriangleIcon } from '@phosphor-icons/react/dist/csr/Triangle'
[/code]

사용 중인 아이콘 라이브러리 문서에서 어떤 import 패턴을 사용할지 확인할 수 있습니다. 이 예시는 [`@phosphor-icons/react`](https://www.npmjs.com/package/@phosphor-icons/react#import-performance-optimization)의 권장 사항을 따릅니다.

`react-icons` 같은 라이브러리는 서로 다른 아이콘 세트를 많이 포함합니다. 한 세트를 선택하면 그대로 유지하세요.

예를 들어 애플리케이션이 `react-icons`를 사용하며 다음을 모두 import하는 경우:

  * `pi` (Phosphor Icons)
  * `md` (Material Design Icons)
  * `tb` (tabler-icons)
  * `cg` (cssgg)



각 세트에서 하나씩만 사용하더라도 컴파일러는 수만 개의 모듈을 처리해야 합니다.

#### 배럴 파일[](https://nextjs.org/docs/app/guides/local-development#barrel-files)

"배럴 파일"은 다른 파일에서 많은 항목을 export하는 파일입니다. import 시 모듈 범위에 부작용이 있는지 파악하기 위해 컴파일러가 이 파일을 파싱해야 하므로 빌드 속도가 느려질 수 있습니다.

가능하면 특정 파일에서 직접 import하세요. [배럴 파일에 대해 더 알아보기](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js)와 Next.js 내장 최적화도 참고하세요.

#### 패키지 import 최적화[](https://nextjs.org/docs/app/guides/local-development#optimize-package-imports)

Next.js는 특정 패키지의 import를 자동으로 최적화할 수 있습니다. 배럴 파일을 사용하는 패키지를 사용한다면 `next.config.js`에 추가하세요:
[code] 
    module.exports = {
      experimental: {
        optimizePackageImports: ['package-name'],
      },
    }
[/code]

Turbopack은 import를 자동 분석하고 최적화합니다. 이 설정이 필요하지 않습니다.

### 4\. Tailwind CSS 설정 점검[](https://nextjs.org/docs/app/guides/local-development#4-check-your-tailwind-css-setup)

Tailwind CSS를 사용한다면 올바르게 설정되었는지 확인하세요.

일반적인 실수는 `content` 배열에 `node_modules` 같은 대규모 디렉터리를 포함해 검색 대상에 넣는 것입니다.

Tailwind CSS 3.4.8 이상은 빌드를 느려지게 할 수 있는 설정에 대해 경고합니다.

  1. `tailwind.config.js`에서 검색할 파일을 명확히 지정하세요:
[code] module.exports = {
           content: [
             './src/**/*.{js,ts,jsx,tsx}', // Good
             // This might be too broad
             // It will match `packages/**/node_modules` too
             // '../../packages/**/*.{js,ts,jsx,tsx}',
           ],
         }
[/code]

  2. 불필요한 파일 검색을 피하세요:
[code] module.exports = {
           content: [
             // Better - only scans the 'src' folder
             '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
           ],
         }
[/code]




### 5\. 커스텀 webpack 설정 점검[](https://nextjs.org/docs/app/guides/local-development#5-check-custom-webpack-settings)

추가한 커스텀 webpack 설정이 있다면 컴파일 속도를 늦출 수 있습니다.

로컬 개발에 정말 필요한지 고려해 보세요. 특정 도구를 프로덕션 빌드에만 포함하거나 기본 Turbopack 번들러와 [로더](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders) 구성을 사용하는 방법도 검토할 수 있습니다.

### 6\. 메모리 사용 최적화[](https://nextjs.org/docs/app/guides/local-development#6-optimize-memory-usage)

앱이 매우 크다면 더 많은 메모리가 필요할 수 있습니다.

[메모리 사용 최적화에 대해 더 알아보기](https://nextjs.org/docs/app/guides/memory-usage).

### 7\. 서버 컴포넌트와 데이터 패칭[](https://nextjs.org/docs/app/guides/local-development#7-server-components-and-data-fetching)

서버 컴포넌트 변경은 최신 변경 사항을 보여주기 위해 전체 페이지 재렌더링을 유도하며, 이때 컴포넌트의 새 데이터를 가져옵니다.

실험적 옵션 `serverComponentsHmrCache`는 로컬 개발에서 Hot Module Replacement(HMR) 새로 고침 간에 서버 컴포넌트의 `fetch` 응답을 캐시할 수 있게 해줍니다. 이로 인해 응답 속도가 빨라지고 과금되는 API 호출 비용이 줄어듭니다.

[실험적 옵션에 대해 더 알아보기](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache).

### 8\. Docker 대신 로컬 개발 고려[](https://nextjs.org/docs/app/guides/local-development#8-consider-local-development-over-docker)

Mac 또는 Windows에서 Docker로 개발하는 경우, Next.js를 로컬로 실행할 때보다 성능이 크게 떨어질 수 있습니다.

Mac과 Windows에서 Docker의 파일 시스템 접근 방식은 로컬 개발에서는 빠르게 동작하는 HMR이 수 초 또는 수 분이 걸리도록 만들 수 있습니다.

이 성능 차이는 Linux 환경 외부에서 Docker가 파일 시스템 작업을 처리하는 방식 때문입니다. 최상의 개발 경험을 위해 다음을 권장합니다:

  * 개발 중에는 Docker 대신 로컬 개발(`npm run dev` 또는 `pnpm dev`)을 사용하세요
  * Docker는 프로덕션 배포와 프로덕션 빌드 테스트에만 사용하세요
  * 개발에 반드시 Docker를 사용해야 한다면 Linux 머신 또는 VM에서 Docker를 사용하세요



프로덕션용 [Docker 배포](https://nextjs.org/docs/app/getting-started/deploying#docker)에 대해 더 알아보세요.

## 문제를 찾는 도구[](https://nextjs.org/docs/app/guides/local-development#tools-for-finding-problems)

### 상세 fetch 로깅[](https://nextjs.org/docs/app/guides/local-development#detailed-fetch-logging)

개발 중에 무슨 일이 일어나는지 자세히 확인하려면 `next.config.js` 파일에서 `logging.fetches` 옵션을 사용하세요:
[code] 
    module.exports = {
      logging: {
        fetches: {
          fullUrl: true,
        },
      },
    }
[/code]

[fetch 로깅에 대해 더 알아보기](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).

### Turbopack 추적[](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing)

Turbopack 추적은 로컬 개발 중 애플리케이션 성능을 이해하도록 돕는 도구입니다. 각 모듈이 컴파일되는 데 걸린 시간과 관계를 자세히 제공합니다.

  1. 최신 버전의 Next.js가 설치되어 있는지 확인합니다.

  2. Turbopack 트레이스 파일을 생성합니다:

pnpmnpmyarnbun

Terminal
[code]NEXT_TURBOPACK_TRACING=1 pnpm dev
[/code]

  3. 애플리케이션을 탐색하거나 파일을 수정해 문제를 재현합니다.

  4. Next.js 개발 서버를 중지합니다.

  5. `.next/dev` 폴더에 `trace-turbopack`이라는 파일이 생성됩니다.

  6. `npx next internal trace [path-to-file]`로 파일을 해석할 수 있습니다:
[code] npx next internal trace .next/dev/trace-turbopack
[/code]

`trace`를 사용할 수 없는 버전에서는 명령이 `turbo-trace-server`였습니다:
[code] npx next internal turbo-trace-server .next/dev/trace-turbopack
[/code]

  7. 트레이스 서버가 실행되면 <https://trace.nextjs.org/>[](https://trace.nextjs.org/)에서 트레이스를 볼 수 있습니다.

  8. 기본적으로 트레이스 뷰어는 시간을 집계합니다. 각 개별 시간을 보려면 뷰어 오른쪽 상단에서 "Aggregated in order"를 "Spans in order"로 전환하세요.




> **참고**: 트레이스 파일은 기본적으로 `.next/dev`인 개발 서버 디렉터리에 저장됩니다. 이 위치는 Next 구성 파일의 [`isolatedDevBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild) 플래그로 제어할 수 있습니다.

### 아직 문제가 있나요?[](https://nextjs.org/docs/app/guides/local-development#still-having-problems)

[Turbopack Tracing](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing) 섹션에서 생성된 trace 파일을 공유하고 [GitHub Discussions](https://github.com/vercel/next.js/discussions) 또는 [Discord](https://nextjs.org/discord)에 게시하세요.

도움이 되었나요?

지원됨.

보내기
