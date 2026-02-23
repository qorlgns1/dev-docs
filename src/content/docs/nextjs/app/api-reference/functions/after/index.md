---
title: 'Functions: after'
description: 'Last updated February 20, 2026'
---

# Functions: after | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/after

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)after

Copy page

# after

Last updated February 20, 2026

`after`는 응답(또는 사전 렌더링)이 완료된 뒤에 실행할 작업을 예약할 수 있게 해 줍니다. 이는 로깅, 분석처럼 응답을 차단하면 안 되는 작업 및 부수 효과에 유용합니다.

[Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)([`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) 포함), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 사용할 수 있습니다.

이 함수는 응답(또는 사전 렌더링)이 끝난 후 실행될 콜백을 받습니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { after } from 'next/server'
    // Custom logging function
    import { log } from '@/app/utils'
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      after(() => {
        // Execute after the layout is rendered and sent to the user
        log()
      })
      return <>{children}</>
    }
[/code]

> **알아 두면 좋아요:** `after`는 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)가 아니며, 이를 호출해도 라우트가 동적으로 변하지 않습니다. 정적 페이지에서 사용하면 콜백은 빌드 시점 또는 페이지가 재검증될 때 실행됩니다.

## Reference[](https://nextjs.org/docs/app/api-reference/functions/after#reference)

### Parameters[](https://nextjs.org/docs/app/api-reference/functions/after#parameters)

  * 응답(또는 사전 렌더링)이 완료된 뒤 실행될 콜백 함수.



### Duration[](https://nextjs.org/docs/app/api-reference/functions/after#duration)

`after`는 라우트에 설정된 플랫폼 기본값 또는 구성된 최대 기간 동안 실행됩니다. 플랫폼이 지원한다면 [`maxDuration`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration) 라우트 세그먼트 구성을 사용해 타임아웃 한도를 설정할 수 있습니다.

## Good to know[](https://nextjs.org/docs/app/api-reference/functions/after#good-to-know)

  * 응답이 정상적으로 완료되지 않아도 `after`는 실행됩니다. 오류가 발생하거나 `notFound`, `redirect`가 호출된 경우도 포함됩니다.
  * `after` 내부에서 호출되는 함수를 중복 제거하려면 React `cache`를 사용할 수 있습니다.
  * `after`는 다른 `after` 호출 안에 중첩할 수 있습니다. 예를 들어, 추가 기능을 붙이기 위해 `after` 호출을 감싸는 유틸리티 함수를 만들 수 있습니다.



## Examples[](https://nextjs.org/docs/app/api-reference/functions/after#examples)

### With request APIs[](https://nextjs.org/docs/app/api-reference/functions/after#with-request-apis)

[`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)나 [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers) 같은 요청 API를 `after` 내부에서 사용할 수 있는지는 `after`가 어디에서 호출되는지에 따라 달라집니다.

#### In Route Handlers and Server Functions[](https://nextjs.org/docs/app/api-reference/functions/after#in-route-handlers-and-server-functions)

[Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data)에서는 `after` 콜백 안에서 `cookies`, `headers`를 직접 호출할 수 있습니다. 이는 변형이나 API 요청 뒤에 활동을 기록할 때 유용합니다. 예:

app/api/route.ts

JavaScriptTypeScript
[code]
    import { after } from 'next/server'
    import { cookies, headers } from 'next/headers'
    import { logUserAction } from '@/app/utils'
     
    export async function POST(request: Request) {
      // Perform mutation
      // ...
     
      // Log user activity for analytics
      after(async () => {
        const userAgent = (await headers()).get('user-agent') || 'unknown'
        const sessionCookie =
          (await cookies()).get('session-id')?.value || 'anonymous'
     
        logUserAction({ sessionCookie, userAgent })
      })
     
      return new Response(JSON.stringify({ status: 'success' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      })
    }
[/code]

#### In Server Components (pages and layouts)[](https://nextjs.org/docs/app/api-reference/functions/after#in-server-components-pages-and-layouts)

[Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)(페이지, 레이아웃, `generateMetadata` 포함)에서는 `after` 내부에서 `cookies`, `headers`, 기타 [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)를 사용할 수 **없습니다**. Next.js가 [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr)과 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 지원하려면 컴포넌트 트리의 어떤 부분이 요청 데이터를 읽는지 알아야 하지만, `after`는 React 렌더링 라이프사이클 이후에 실행되기 때문입니다.

Server Component에서 `after` 콜백에 요청 데이터가 필요하다면 먼저 읽은 뒤 값을 전달하세요:

app/page.tsx

JavaScriptTypeScript
[code]
    import { after } from 'next/server'
    import { cookies, headers } from 'next/headers'
    import { logUserAction } from '@/app/utils'
     
    export default async function Page() {
      // Read request data before `after` — this is allowed
      // These calls will be read during the component's rendering lifecycle
      const userAgent = (await headers()).get('user-agent') || 'unknown'
      const sessionCookie =
        (await cookies()).get('session-id')?.value || 'anonymous'
     
      after(() => {
        // Use the values read above
        logUserAction({ sessionCookie, userAgent })
      })
     
      return <h1>My Page</h1>
    }
[/code]

Server Component에서 `after` 콜백 내부에서 `cookies()`나 `headers()`를 호출하면 런타임 오류가 발생합니다.

#### With Cache Components[](https://nextjs.org/docs/app/api-reference/functions/after#with-cache-components)

[Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 때는 `cookies`, `headers`처럼 요청 데이터를 읽는 컴포넌트를 [`<Suspense>`](https://react.dev/reference/react/Suspense)로 감싸야 페이지 나머지를 정적 셸로 사전 렌더링할 수 있습니다.

요청 데이터를 동적 컴포넌트에서 읽고 `after`에 전달하는 방식으로 이 패턴을 `after`와 결합할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import { after } from 'next/server'
    import { cookies } from 'next/headers'
    import { logUserAction } from '@/app/utils'
     
    export default function Page() {
      return (
        <>
          <h1>Part of the static shell</h1>
          <Suspense fallback={<p>Loading...</p>}>
            <DynamicContent />
          </Suspense>
        </>
      )
    }
     
    async function DynamicContent() {
      const sessionCookie =
        (await cookies()).get('session-id')?.value || 'anonymous'
     
      // Schedule work after the response is sent
      after(() => {
        logUserAction({ sessionCookie })
      })
     
      return <p>Your session: {sessionCookie}</p>
    }
[/code]

이 예시에서 `<h1>`과 `<Suspense>` 폴백은 정적 셸에 포함됩니다. `DynamicContent`는 렌더링 중 쿠키를 읽고 클로저를 통해 `after`에 전달합니다. `cookies()` 호출이 `after` 콜백 **외부**(컴포넌트 렌더링 시)에 있기 때문에 제대로 동작합니다.

## Platform Support[](https://nextjs.org/docs/app/api-reference/functions/after#platform-support)

Deployment Option| Supported  
---|---  
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes  
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No  
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific  
  
Next.js를 셀프 호스팅할 때 [`after` 구성](https://nextjs.org/docs/app/guides/self-hosting#after) 방법을 알아보세요.

Reference: serverless 플랫폼에서 `after` 지원

서버리스 환경에서 `after`를 사용하려면 응답이 전송된 뒤 비동기 작업이 완료될 때까지 기다려야 합니다. Next.js와 Vercel에서는 [`waitUntil`](https://vercel.com/docs/functions/functions-api-reference#waituntil)에 전달된 모든 Promise가 완료될 때까지 서버리스 호출 수명을 연장하는 `waitUntil(promise)`라는 기본기를 사용합니다.

사용자도 `after`를 실행할 수 있도록 하려면 유사하게 동작하는 `waitUntil` 구현을 제공해야 합니다.

`after`가 호출되면 Next.js는 다음과 같이 `waitUntil`에 접근합니다:
[code]
    const RequestContext = globalThis[Symbol.for('@next/request-context')]
    const contextValue = RequestContext?.get()
    const waitUntil = contextValue?.waitUntil
[/code]

이는 `globalThis[Symbol.for('@next/request-context')]`가 다음과 같은 객체를 포함해야 함을 의미합니다:
[code]
    type NextRequestContext = {
      get(): NextRequestContextValue | undefined
    }
     
    type NextRequestContextValue = {
      waitUntil?: (promise: Promise<any>) => void
    }
[/code]

구현 예시는 다음과 같습니다.
[code]
    import { AsyncLocalStorage } from 'node:async_hooks'
     
    const RequestContextStorage = new AsyncLocalStorage<NextRequestContextValue>()
     
    // Define and inject the accessor that next.js will use
    const RequestContext: NextRequestContext = {
      get() {
        return RequestContextStorage.getStore()
      },
    }
    globalThis[Symbol.for('@next/request-context')] = RequestContext
     
    const handler = (req, res) => {
      const contextValue = { waitUntil: YOUR_WAITUNTIL }
      // Provide the value
      return RequestContextStorage.run(contextValue, () => nextJsHandler(req, res))
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/after#version-history)

Version| Changes  
---|---  
`v15.1.0`| `after`가 안정화되었습니다.  
`v15.0.0-rc`| `unstable_after`가 도입되었습니다.  
  
Was this helpful?

supported.

Send
