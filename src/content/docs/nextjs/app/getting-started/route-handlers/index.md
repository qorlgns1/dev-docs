---
title: '시작하기: Route Handlers'
description: 'Route Handlers는 Web Request 및 Response API를 사용해 특정 경로에 대한 사용자 정의 요청 핸들러를 만들 수 있게 해줍니다.'
---

# 시작하기: Route Handlers | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/route-handlers

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Route Handlers

Copy page

# Route Handlers

마지막 업데이트 2026년 2월 20일

## Route Handlers[](https://nextjs.org/docs/app/getting-started/route-handlers#route-handlers)

Route Handlers는 Web [Request](https://developer.mozilla.org/docs/Web/API/Request) 및 [Response](https://developer.mozilla.org/docs/Web/API/Response) API를 사용해 특정 경로에 대한 사용자 정의 요청 핸들러를 만들 수 있게 해줍니다.

> **알아두면 좋아요**: Route Handlers는 `app` 디렉터리 안에서만 사용할 수 있습니다. 이는 `pages` 디렉터리의 [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)와 동일하므로 API Routes와 Route Handlers를 동시에 사용할 **필요가 없습니다**.

### Convention[](https://nextjs.org/docs/app/getting-started/route-handlers#convention)

Route Handlers는 `app` 디렉터리 안의 [`route.js|ts` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/route)에 정의합니다:

app/api/route.ts

JavaScriptTypeScript
```
    export async function GET(request: Request) {}
```

Route Handlers는 `page.js` 및 `layout.js`와 마찬가지로 `app` 디렉터리 내 어디든 중첩할 수 있습니다. 다만 동일한 라우트 세그먼트 수준에서 `page.js`와 `route.js` 파일이 **동시에 존재할 수는 없습니다**.

### Supported HTTP Methods[](https://nextjs.org/docs/app/getting-started/route-handlers#supported-http-methods)

다음 [HTTP 메서드](https://developer.mozilla.org/docs/Web/HTTP/Methods)를 지원합니다: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`. 지원되지 않는 메서드가 호출되면 Next.js는 `405 Method Not Allowed` 응답을 반환합니다.

### Extended `NextRequest` and `NextResponse` APIs[](https://nextjs.org/docs/app/getting-started/route-handlers#extended-nextrequest-and-nextresponse-apis)

기본 [Request](https://developer.mozilla.org/docs/Web/API/Request) 및 [Response](https://developer.mozilla.org/docs/Web/API/Response) API 지원에 더해, Next.js는 고급 사용 사례를 위한 편의 기능을 제공하기 위해 [`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)와 [`NextResponse`](https://nextjs.org/docs/app/api-reference/functions/next-response)를 확장합니다.

### Caching[](https://nextjs.org/docs/app/getting-started/route-handlers#caching)

Route Handlers는 기본적으로 캐시되지 않습니다. 하지만 `GET` 메서드에 대해 캐시를 선택적으로 적용할 수 있습니다. 다른 지원 HTTP 메서드는 **캐시되지 않습니다**. `GET` 메서드를 캐시하려면 Route Handler 파일에서 `export const dynamic = 'force-static'`과 같은 [route config 옵션](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)을 사용하세요.

app/items/route.ts

JavaScriptTypeScript
```
    export const dynamic = 'force-static'

    export async function GET() {
      const res = await fetch('https://data.mongodb-api.com/...', {
        headers: {
          'Content-Type': 'application/json',
          'API-Key': process.env.DATA_API_KEY,
        },
      })
      const data = await res.json()

      return Response.json({ data })
    }
```

> **알아두면 좋아요**: 동일한 파일에서 캐시되는 `GET` 메서드와 함께 두더라도, 다른 지원 HTTP 메서드는 **캐시되지 않습니다**.

#### With Cache Components[](https://nextjs.org/docs/app/getting-started/route-handlers#with-cache-components)

[Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 활성화하면 `GET` Route Handlers는 애플리케이션의 일반 UI 라우트와 동일한 모델을 따릅니다. 기본적으로 요청 시점에 실행되며, 동적 또는 런타임 데이터를 액세스하지 않는다면 사전 렌더링이 가능하고, `use cache`를 사용해 정적 응답에 동적 데이터를 포함할 수 있습니다.

**정적 예시** \- 동적 또는 런타임 데이터를 액세스하지 않으므로 빌드 시점에 사전 렌더링됩니다:

app/api/project-info/route.ts
```
    export async function GET() {
      return Response.json({
        projectName: 'Next.js',
      })
    }
```

**동적 예시** \- 비결정적 연산에 접근합니다. 빌드 중 `Math.random()`이 호출되면 사전 렌더링이 중단되고 요청 시점 렌더링으로 위임됩니다:

app/api/random-number/route.ts
```
    export async function GET() {
      return Response.json({
        randomNumber: Math.random(),
      })
    }
```

**런타임 데이터 예시** \- 요청별 데이터를 액세스합니다. `headers()`와 같은 런타임 API가 호출되면 사전 렌더링이 종료됩니다:

app/api/user-agent/route.ts
```
    import { headers } from 'next/headers'

    export async function GET() {
      const headersList = await headers()
      the userAgent = headersList.get('user-agent')

      return Response.json({ userAgent })
    }
```

> **알아두면 좋아요**: `GET` 핸들러가 네트워크 요청, 데이터베이스 쿼리, 비동기 파일 시스템 작업, 요청 객체 속성(`req.url`, `request.headers`, `request.cookies`, `request.body` 등), [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers), [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) 같은 런타임 API 또는 비결정적 연산을 사용하면 사전 렌더링이 중단됩니다.

**캐시된 예시** \- 동적 데이터(데이터베이스 쿼리)에 접근하지만 `use cache`로 캐시하여 사전 렌더링된 응답에 포함됩니다:

app/api/products/route.ts
```
    import { cacheLife } from 'next/cache'

    export async function GET() {
      const products = await getProducts()
      return Response.json(products)
    }

    async function getProducts() {
      'use cache'
      cacheLife('hours')

      return await db.query('SELECT * FROM products')
    }
```

> **알아두면 좋아요**: `use cache`는 Route Handler 본문 안에서 직접 사용할 수 없으므로 헬퍼 함수로 분리하세요. 캐시된 응답은 새 요청이 도착하면 `cacheLife`에 따라 재검증됩니다.

### Special Route Handlers[](https://nextjs.org/docs/app/getting-started/route-handlers#special-route-handlers)

[`sitemap.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`icon.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons) 등과 같은 특수 Route Handler와 기타 [metadata 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)은 Dynamic API나 동적 구성 옵션을 사용하지 않는 한 기본적으로 정적 상태로 유지됩니다.

### Route Resolution[](https://nextjs.org/docs/app/getting-started/route-handlers#route-resolution)

`route`는 가장 낮은 수준의 라우팅 프리미티브로 볼 수 있습니다.

  * `page`처럼 레이아웃이나 클라이언트 측 탐색에 **참여하지 않습니다**.
  * 동일한 경로에 `page.js`와 `route.js` 파일이 **함께 존재할 수 없습니다**.

Page| Route| Result
---|---|---
`app/page.js`| `app/route.js`| Conflict
`app/page.js`| `app/api/route.js`| Valid
`app/[user]/page.js`| `app/api/route.js`| Valid

각 `route.js` 또는 `page.js` 파일은 해당 경로의 모든 HTTP 메서드를 처리합니다.

app/page.ts

JavaScriptTypeScript
```
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }

    // Conflict
    // `app/route.ts`
    export async function POST(request: Request) {}
```

Route Handlers가 [프런트엔드 애플리케이션을 보완](https://nextjs.org/docs/app/guides/backend-for-frontend)하는 방법을 더 알아보거나 Route Handlers [API Reference](https://nextjs.org/docs/app/api-reference/file-conventions/route)를 살펴보세요.

### Route Context Helper[](https://nextjs.org/docs/app/getting-started/route-handlers#route-context-helper)

TypeScript에서는 전역으로 제공되는 [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper) 헬퍼를 사용해 Route Handler의 `context` 매개변수에 타입을 지정할 수 있습니다:

app/users/[id]/route.ts

JavaScriptTypeScript
```
    import type { NextRequest } from 'next/server'

    export async function GET(_req: NextRequest, ctx: RouteContext<'/users/[id]'>) {
      const { id } = await ctx.params
      return Response.json({ id })
    }
```

> **알아두면 좋아요**
>
>   * 타입은 `next dev`, `next build` 또는 `next typegen` 중에 생성됩니다.
>

## API Reference

Route Handlers에 대해 더 알아보기

- [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  - Route.js 특수 파일에 대한 API reference입니다.

- [백엔드 포 프론트엔드](https://nextjs.org/docs/app/guides/backend-for-frontend)
  - Backend for FrontendNext.js를 백엔드 프레임워크로 사용하는 방법을 알아보세요

Was this helpful?

supported.

Send