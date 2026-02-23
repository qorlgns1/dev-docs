---
title: '파일 시스템 규칙: instrumentation.js'
description: '파일은 애플리케이션에 관측 도구를 통합하여 성능과 동작을 추적하고 프로덕션 문제를 디버깅할 수 있도록 합니다.'
---

# 파일 시스템 규칙: instrumentation.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation

[API 참조](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)instrumentation.js

페이지 복사

# instrumentation.js

마지막 업데이트 2026년 2월 20일

`instrumentation.js|ts` 파일은 애플리케이션에 관측 도구를 통합하여 성능과 동작을 추적하고 프로덕션 문제를 디버깅할 수 있도록 합니다.

사용하려면 애플리케이션의 **루트**나 [`src` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) 내부(사용 중인 경우)에 파일을 배치하세요.

## 익스포트[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#exports)

### `register` (선택)[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#register-optional)

이 파일은 새로운 Next.js 서버 인스턴스가 시작될 때 **한 번** 호출되는 `register` 함수를 익스포트하며, 서버가 요청을 처리하기 전에 완료되어야 합니다. `register`는 async 함수일 수 있습니다.

instrumentation.ts

JavaScriptTypeScript
[code]
    import { registerOTel } from '@vercel/otel'
     
    export function register() {
      registerOTel('next-app')
    }
[/code]

### `onRequestError` (선택)[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#onrequesterror-optional)

`onRequestError` 함수를 선택적으로 익스포트하여 **서버** 오류를 임의의 관측 제공자에 기록할 수 있습니다.

  * `onRequestError`에서 async 작업을 실행한다면 반드시 await 하세요. `onRequestError`는 Next.js 서버가 오류를 포착할 때 트리거됩니다.
  * `error` 인스턴스는 Server Components 렌더링 중 React에서 처리된 경우 원래 오류 인스턴스와 다를 수 있습니다. 이 경우 오류의 `digest` 속성을 사용해 실제 오류 유형을 식별할 수 있습니다.



instrumentation.ts

JavaScriptTypeScript
[code]
    import { type Instrumentation } from 'next'
     
    export const onRequestError: Instrumentation.onRequestError = async (
      err,
      request,
      context
    ) => {
      await fetch('https://.../report-error', {
        method: 'POST',
        body: JSON.stringify({
          message: err.message,
          request,
          context,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      })
    }
[/code]

#### 매개변수[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#parameters)

이 함수는 `error`, `request`, `context` 세 개의 매개변수를 받습니다.

Types
[code]
    export function onRequestError(
      error: { digest: string } & Error,
      request: {
        path: string // resource path, e.g. /blog?name=foo
        method: string // request method. e.g. GET, POST, etc
        headers: { [key: string]: string | string[] }
      },
      context: {
        routerKind: 'Pages Router' | 'App Router' // the router type
        routePath: string // the route file path, e.g. /app/blog/[dynamic]
        routeType: 'render' | 'route' | 'action' | 'proxy' // the context in which the error occurred
        renderSource:
          | 'react-server-components'
          | 'react-server-components-payload'
          | 'server-rendering'
        revalidateReason: 'on-demand' | 'stale' | undefined // undefined is a normal request without revalidation
        renderType: 'dynamic' | 'dynamic-resume' // 'dynamic-resume' for PPR
      }
    ): void | Promise<void>
[/code]

  * `error`: 포착된 오류 자체(항상 `Error` 타입)이며, 오류의 고유 ID인 `digest` 속성을 포함합니다.
  * `request`: 오류와 연관된 읽기 전용 요청 정보입니다.
  * `context`: 오류가 발생한 컨텍스트입니다. 라우터 종류(App 또는 Pages Router) 및 Server Components(`'render'`), Route Handlers(`'route'`), Server Actions(`'action'`), Proxy(`'proxy'`) 중 어디에서 발생했는지 나타낼 수 있습니다.



### 런타임 지정[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#specifying-the-runtime)

`instrumentation.js` 파일은 Node.js와 Edge 런타임 모두에서 작동하지만, `process.env.NEXT_RUNTIME`을 사용해 특정 런타임을 대상으로 지정할 수 있습니다.

instrumentation.js
[code]
    export function register() {
      if (process.env.NEXT_RUNTIME === 'edge') {
        return require('./register.edge')
      } else {
        return require('./register.node')
      }
    }
     
    export function onRequestError() {
      if (process.env.NEXT_RUNTIME === 'edge') {
        return require('./on-request-error.edge')
      } else {
        return require('./on-request-error.node')
      }
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation#version-history)

버전| 변경 사항  
---|---  
`v15.0.0`| `onRequestError` 도입, `instrumentation` 안정화  
`v14.0.4`| `instrumentation`에 대한 Turbopack 지원  
`v13.2.0`| `instrumentation` 실험적 기능으로 도입  
  
## Instrumentation 추가 학습

### [InstrumentationNext.js 앱에서 서버 시작 시 코드를 실행하는 방법을 알아보세요](https://nextjs.org/docs/app/guides/instrumentation)

유용했나요?

지원됨.

전송
