---
title: '가이드: Instrumentation'
description: 'Instrumentation은 애플리케이션에 모니터링과 로깅 도구를 통합하도록 코드를 사용하는 과정입니다. 이를 통해 애플리케이션의 성능과 동작을 추적하고, 프로덕션 환경에서 문제를 디버그할 수 있습니다.'
---

# 가이드: Instrumentation | Next.js
출처 URL: https://nextjs.org/docs/app/guides/instrumentation

# Instrumentation 설정 방법

마지막 업데이트 2026년 2월 20일

Instrumentation은 애플리케이션에 모니터링과 로깅 도구를 통합하도록 코드를 사용하는 과정입니다. 이를 통해 애플리케이션의 성능과 동작을 추적하고, 프로덕션 환경에서 문제를 디버그할 수 있습니다.

## 규칙[](https://nextjs.org/docs/app/guides/instrumentation#convention)

Instrumentation을 설정하려면 프로젝트의 **루트 디렉터리**(또는 [`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) 폴더를 사용하는 경우 그 안)에 `instrumentation.ts|js` 파일을 생성합니다.

그런 다음 해당 파일에서 `register` 함수를 내보냅니다. 이 함수는 새 Next.js 서버 인스턴스가 시작될 때 **한 번** 호출되며, 서버가 요청을 처리할 준비를 마치기 전에 완료되어야 합니다.

예를 들어 Next.js를 [OpenTelemetry](https://opentelemetry.io/) 및 [@vercel/otel](https://vercel.com/docs/observability/otel-overview)과 함께 사용하려면 다음과 같이 설정합니다:

instrumentation.ts

JavaScriptTypeScript
```
    import { registerOTel } from '@vercel/otel'

    export function register() {
      registerOTel('next-app')
    }
```

전체 구현은 [Next.js with OpenTelemetry 예제](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry)를 참고하십시오.

> **알아두면 좋은 점** :
>
>   * `instrumentation` 파일은 프로젝트 루트에 두고 `app` 또는 `pages` 디렉터리 안에 두지 마세요. `src` 폴더를 사용 중이라면 `pages`, `app`과 함께 `src` 내부에 배치하세요.
>   * [`pageExtensions` 구성 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)으로 접미사를 추가했다면, `instrumentation` 파일명도 동일한 규칙으로 업데이트해야 합니다.
>

## 예시[](https://nextjs.org/docs/app/guides/instrumentation#examples)

### 부작용을 가진 파일 임포트하기[](https://nextjs.org/docs/app/guides/instrumentation#importing-files-with-side-effects)

때로는 특정 부작용 때문에 파일을 임포트하는 것이 유용할 수 있습니다. 예를 들어 전역 변수를 정의하는 파일을 임포트하지만 코드에서 직접 사용하지 않을 수도 있습니다. 그래도 해당 패키지가 선언한 전역 변수에는 접근할 수 있습니다.

`register` 함수 내부에서 JavaScript `import` 구문을 사용하여 파일을 임포트하는 것을 권장합니다. 아래 예시는 `register` 함수에서 `import`를 사용하는 기본적인 방법을 보여줍니다:

instrumentation.ts

JavaScriptTypeScript
```
    export async function register() {
      await import('package-with-side-effect')
    }
```

> **알아두면 좋은 점:**
>
> 파일 상단이 아니라 `register` 함수 내부에서 임포트하는 것을 권장합니다. 이렇게 하면 모든 부작용을 코드의 한 위치에 모아둘 수 있고, 파일 상단에서 전역으로 임포트함으로써 생길 수 있는 의도치 않은 결과를 피할 수 있습니다.

### 런타임별 코드를 임포트하기[](https://nextjs.org/docs/app/guides/instrumentation#importing-runtime-specific-code)

Next.js는 모든 환경에서 `register`를 호출하므로, 특정 런타임(예: [Edge 또는 Node.js](https://nextjs.org/docs/app/api-reference/edge))를 지원하지 않는 코드는 조건부로 임포트해야 합니다. 현재 환경을 확인하려면 `NEXT_RUNTIME` 환경 변수를 사용할 수 있습니다:

instrumentation.ts

JavaScriptTypeScript
```
    export async function register() {
      if (process.env.NEXT_RUNTIME === 'nodejs') {
        await import('./instrumentation-node')
      }

      if (process.env.NEXT_RUNTIME === 'edge') {
        await import('./instrumentation-edge')
      }
    }
```

## Instrumentation 더 알아보기

- [instrumentation.js파일에 대한 API 레퍼런스입니다.](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)

보내기