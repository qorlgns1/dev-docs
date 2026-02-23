---
title: '파일 시스템 규칙: instrumentation.js'
description: '원본 URL: https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation'
---

# 파일 시스템 규칙: instrumentation.js | Next.js

원본 URL: https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation

[API 참고](https://nextjs.org/docs/pages/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/pages/api-reference/file-conventions)instrumentation.js

페이지 복사

# instrumentation.js

최종 업데이트 2026년 2월 20일

`instrumentation.js|ts` 파일은 애플리케이션에 관측 도구를 통합해 성능과 동작을 추적하고 프로덕션에서 문제를 디버그할 수 있게 해줍니다.

사용하려면 파일을 애플리케이션의 **root** 또는 [`src` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)를 사용 중이라면 그 안에 배치하세요.

## 내보내기[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#exports)

### `register` (선택 사항)[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#register-optional)

이 파일은 새 Next.js 서버 인스턴스가 시작될 때 **한 번** 호출되는 `register` 함수를 내보내며, 서버가 요청을 처리할 준비가 되기 전에 완료되어야 합니다. `register` 는 async 함수가 될 수 있습니다.

instrumentation.ts

JavaScriptTypeScript
[code]
    import { registerOTel } from '@vercel/otel'
     
    export function register() {
      registerOTel('next-app')
    }
[/code]

### `onRequestError` (선택 사항)[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#onrequesterror-optional)

원한다면 `onRequestError` 함수를 내보내서 **서버** 오류를 임의의 관측 서비스로 전송할 수 있습니다.

  * `onRequestError` 안에서 비동기 작업을 수행한다면 반드시 await 하세요. Next.js 서버가 오류를 포착할 때 `onRequestError` 가 호출됩니다.
  * `error` 인스턴스는 React 가 Server Components 렌더링 중에 오류를 처리한 경우 원래 발생한 오류 인스턴스가 아닐 수도 있습니다. 이 경우 오류의 `digest` 속성을 사용해 실제 오류 유형을 식별할 수 있습니다.



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

#### 매개변수[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#parameters)

이 함수는 `error`, `request`, `context` 세 개의 매개변수를 받습니다.

타입
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

  * `error`: 포착된 오류 자체(`Error` 타입)이며, 고유 ID 인 `digest` 속성을 포함합니다.
  * `request`: 오류와 연관된 읽기 전용 요청 정보입니다.
  * `context`: 오류가 발생한 컨텍스트입니다. 라우터 종류(App Router 또는 Pages Router)와 Server Components(`'render'`), Route Handlers(`'route'`), Server Actions(`'action'`), Proxy(`'proxy'`) 가운데 어떤 컨텍스트인지가 포함될 수 있습니다.



### 런타임 지정하기[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#specifying-the-runtime)

`instrumentation.js` 파일은 Node.js 와 Edge 런타임 모두에서 동작하지만, 특정 런타임을 대상으로 하려면 `process.env.NEXT_RUNTIME` 을 사용할 수 있습니다.

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

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation#version-history)

Version| Changes  
---|---  
`v15.0.0`| `onRequestError` 도입, `instrumentation` 안정화  
`v14.0.4`| `instrumentation` 의 Turbopack 지원  
`v13.2.0`| 실험적 기능으로 `instrumentation` 도입  
  
도움이 되었나요?

지원됨.

보내기
