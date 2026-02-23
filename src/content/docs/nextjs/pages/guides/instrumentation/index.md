---
title: '가이드: 계측'
description: '계측은 코드를 사용해 모니터링 및 로깅 도구를 애플리케이션에 통합하는 과정입니다. 이를 통해 애플리케이션의 성능과 동작을 추적하고, 프로덕션 환경에서 발생하는 문제를 디버깅할 수 있습니다.'
---

# 가이드: 계측 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/instrumentation

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)계측

페이지 복사

# 계측 설정 방법

최종 업데이트 2026년 2월 20일

계측은 코드를 사용해 모니터링 및 로깅 도구를 애플리케이션에 통합하는 과정입니다. 이를 통해 애플리케이션의 성능과 동작을 추적하고, 프로덕션 환경에서 발생하는 문제를 디버깅할 수 있습니다.

## 규칙[](https://nextjs.org/docs/pages/guides/instrumentation#convention)

계측을 설정하려면 프로젝트의 **루트 디렉터리**(또는 [`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) 폴더를 사용 중이라면 해당 폴더) 안에 `instrumentation.ts|js` 파일을 만듭니다.

그런 다음 파일에서 `register` 함수를 export 합니다. 이 함수는 새 Next.js 서버 인스턴스가 시작될 때 **한 번만** 호출되며, 서버가 요청을 처리할 준비를 마치기 전에 완료되어야 합니다.

예를 들어 Next.js에서 [OpenTelemetry](https://opentelemetry.io/) 및 [@vercel/otel](https://vercel.com/docs/observability/otel-overview)을 사용하려면 다음과 같이 설정합니다.

instrumentation.ts

JavaScriptTypeScript
[code]
    import { registerOTel } from '@vercel/otel'
     
    export function register() {
      registerOTel('next-app')
    }
[/code]

전체 구현은 [Next.js with OpenTelemetry 예제](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry)를 참고하세요.

> **알아두면 좋아요** :
> 
>   * `instrumentation` 파일은 프로젝트 루트에 있어야 하며 `app` 또는 `pages` 디렉터리 내부에 두면 안 됩니다. `src` 폴더를 사용하는 경우 `pages`, `app`과 나란히 `src` 안에 파일을 배치하세요.
>   * [`pageExtensions` 설정 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)으로 접미사를 추가한다면, `instrumentation` 파일 이름도 그에 맞게 업데이트해야 합니다.
> 

## 예시[](https://nextjs.org/docs/pages/guides/instrumentation#examples)

### 부수 효과가 있는 파일 가져오기[](https://nextjs.org/docs/pages/guides/instrumentation#importing-files-with-side-effects)

어떤 파일은 그 파일이 유발하는 부수 효과 때문에 import 하는 것이 유용할 수 있습니다. 예를 들어 전역 변수를 정의하는 파일을 import 하되, 코드에서 해당 파일을 명시적으로 사용하지 않을 수도 있습니다. 그래도 그 패키지가 선언한 전역 변수에는 접근할 수 있습니다.

`register` 함수 내부에서 JavaScript `import` 구문으로 파일을 가져오는 것을 권장합니다. 다음 예제는 `register` 함수에서 `import`를 기본적으로 사용하는 방법을 보여줍니다.

instrumentation.ts

JavaScriptTypeScript
[code]
    export async function register() {
      await import('package-with-side-effect')
    }
[/code]

> **알아두면 좋아요:**
> 
> 파일 최상단이 아니라 `register` 함수 내부에서 import 하기를 권장합니다. 이렇게 하면 모든 부수 효과를 코드의 한 곳에 모아둘 수 있고, 파일 최상단에서 전역으로 import 할 때 발생할 수 있는 의도치 않은 결과를 피할 수 있습니다.

### 런타임별 코드 가져오기[](https://nextjs.org/docs/pages/guides/instrumentation#importing-runtime-specific-code)

Next.js는 모든 환경에서 `register`를 호출하므로, 특정 런타임(예: [Edge 또는 Node.js](https://nextjs.org/docs/app/api-reference/edge))를 지원하지 않는 코드는 조건부로 import 해야 합니다. 현재 환경을 확인하려면 `NEXT_RUNTIME` 환경 변수를 사용할 수 있습니다.

instrumentation.ts

JavaScriptTypeScript
[code]
    export async function register() {
      if (process.env.NEXT_RUNTIME === 'nodejs') {
        await import('./instrumentation-node')
      }
     
      if (process.env.NEXT_RUNTIME === 'edge') {
        await import('./instrumentation-edge')
      }
    }
[/code]

도움이 되었나요?

지원됨.

보내기
