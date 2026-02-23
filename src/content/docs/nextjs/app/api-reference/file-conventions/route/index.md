---
title: '파일 시스템 규칙: route.js'
description: 'Route Handler를 사용하면 Web Request 및 Response API를 이용해 특정 라우트에 대한 사용자 정의 요청 핸들러를 만들 수 있습니다.'
---

# 파일 시스템 규칙: route.js | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/route

# route.js

마지막 업데이트: 2026년 2월 20일

Route Handler를 사용하면 Web [Request](https://developer.mozilla.org/docs/Web/API/Request) 및 [Response](https://developer.mozilla.org/docs/Web/API/Response) API를 이용해 특정 라우트에 대한 사용자 정의 요청 핸들러를 만들 수 있습니다.

route.ts

JavaScriptTypeScript
```
    export async function GET() {
      return Response.json({ message: 'Hello World' })
    }
```

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/route#reference)

### HTTP Methods[](https://nextjs.org/docs/app/api-reference/file-conventions/route#http-methods)

**route** 파일을 사용하면 특정 라우트에 대한 사용자 정의 요청 핸들러를 만들 수 있습니다. 다음 [HTTP 메서드](https://developer.mozilla.org/docs/Web/HTTP/Methods)를 지원합니다: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.

route.ts

JavaScriptTypeScript
```
    export async function GET(request: Request) {}

    export async function HEAD(request: Request) {}

    export async function POST(request: Request) {}

    export async function PUT(request: Request) {}

    export async function DELETE(request: Request) {}

    export async function PATCH(request: Request) {}

    // If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
    export async function OPTIONS(request: Request) {}
```

### Parameters[](https://nextjs.org/docs/app/api-reference/file-conventions/route#parameters)

#### `request` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-optional)

`request` 객체는 Web [Request](https://developer.mozilla.org/docs/Web/API/Request) API를 확장한 [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request) 객체입니다. `NextRequest`를 사용하면 들어오는 요청을 더욱 세밀하게 제어할 수 있으며, `cookies`에 쉽게 접근하고 확장된 파싱된 URL 객체인 `nextUrl`을 사용할 수 있습니다.

route.ts

JavaScriptTypeScript
```
    import type { NextRequest } from 'next/server'

    export async function GET(request: NextRequest) {
      const url = request.nextUrl
    }
```

#### `context` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/route#context-optional)

  * **`params`**: 현재 라우트의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 포함하는 객체로 해결되는 프로미스입니다.

app/dashboard/[team]/route.ts

JavaScriptTypeScript
```
    export async function GET(
      request: Request,
      { params }: { params: Promise<{ team: string }> }
    ) {
      const { team } = await params
    }
```

예시| URL| `params`
---|---|---
`app/dashboard/[team]/route.js`| `/dashboard/1`| `Promise<{ team: '1' }>`
`app/shop/[tag]/[item]/route.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`
`app/blog/[...slug]/route.js`| `/blog/1/2`| `Promise<{ slug: ['1', '2'] }>`

### Route Context Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)

라우트 리터럴에서 강한 타입의 `params`를 얻기 위해 `RouteContext`를 사용하여 Route Handler 컨텍스트에 타입을 지정할 수 있습니다. `RouteContext`는 전역적으로 사용할 수 있는 헬퍼입니다.

app/users/[id]/route.ts
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
>   * 타입 생성 이후에는 `RouteContext` 헬퍼가 전역적으로 제공되므로 import 할 필요가 없습니다.
>

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/route#examples)

### Cookies[](https://nextjs.org/docs/app/api-reference/file-conventions/route#cookies)

`next/headers`의 [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)를 사용해 쿠키를 읽거나 설정할 수 있습니다.

route.ts

JavaScriptTypeScript
```
    import { cookies } from 'next/headers'

    export async function GET(request: NextRequest) {
      const cookieStore = await cookies()

      const a = cookieStore.get('a')
      const b = cookieStore.set('b', '1')
      const c = cookieStore.delete('c')
    }
```

또는 [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) 헤더가 포함된 새 `Response`를 반환할 수도 있습니다.

app/api/route.ts

JavaScriptTypeScript
```
    import { cookies } from 'next/headers'

    export async function GET(request: Request) {
      const cookieStore = await cookies()
      const token = cookieStore.get('token')

      return new Response('Hello, Next.js!', {
        status: 200,
        headers: { 'Set-Cookie': `token=${token.value}` },
      })
    }
```

기본 Web API를 사용하여 요청에서 쿠키를 읽을 수도 있습니다([`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)).

app/api/route.ts

JavaScriptTypeScript
```
    import { type NextRequest } from 'next/server'

    export async function GET(request: NextRequest) {
      const token = request.cookies.get('token')
    }
```

### Headers[](https://nextjs.org/docs/app/api-reference/file-conventions/route#headers)

`next/headers`의 [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)를 사용하여 헤더를 읽을 수 있습니다.

route.ts

JavaScriptTypeScript
```
    import { headers } from 'next/headers'
    import type { NextRequest } from 'next/server'

    export async function GET(request: NextRequest) {
      const headersList = await headers()
      const referer = headersList.get('referer')
    }
```

이 `headers` 인스턴스는 읽기 전용입니다. 헤더를 설정하려면 새 `headers`가 포함된 새로운 `Response`를 반환해야 합니다.

app/api/route.ts

JavaScriptTypeScript
```
    import { headers } from 'next/headers'

    export async function GET(request: Request) {
      const headersList = await headers()
      const referer = headersList.get('referer')

      return new Response('Hello, Next.js!', {
        status: 200,
        headers: { referer: referer },
      })
    }
```

기본 Web API를 사용하여 요청에서 헤더를 읽을 수도 있습니다([`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)).

app/api/route.ts

JavaScriptTypeScript
```
    import { type NextRequest } from 'next/server'

    export async function GET(request: NextRequest) {
      const requestHeaders = new Headers(request.headers)
    }
```

### Revalidating Cached Data[](https://nextjs.org/docs/app/api-reference/file-conventions/route#revalidating-cached-data)

`revalidate` 라우트 세그먼트 구성 옵션을 사용하여 [캐시된 데이터를 리빌리데이트](https://nextjs.org/docs/app/guides/incremental-static-regeneration)할 수 있습니다.

app/posts/route.ts

JavaScriptTypeScript
```
    export const revalidate = 60

    export async function GET() {
      const data = await fetch('https://api.vercel.app/blog')
      const posts = await data.json()

      return Response.json(posts)
    }
```

### Redirects[](https://nextjs.org/docs/app/api-reference/file-conventions/route#redirects)

app/api/route.ts

JavaScriptTypeScript
```
    import { redirect } from 'next/navigation'

    export async function GET(request: Request) {
      redirect('https://nextjs.org/')
    }
```

### Dynamic Route Segments[](https://nextjs.org/docs/app/api-reference/file-conventions/route#dynamic-route-segments)

Route Handler는 [동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 사용하여 동적 데이터를 기반으로 요청 핸들러를 만들 수 있습니다.

app/items/[slug]/route.ts

JavaScriptTypeScript
```
    export async function GET(
      request: Request,
      { params }: { params: Promise<{ slug: string }> }
    ) {
      const { slug } = await params // 'a', 'b', or 'c'
    }
```

Route| 예시 URL| `params`
---|---|---
`app/items/[slug]/route.js`| `/items/a`| `Promise<{ slug: 'a' }>`
`app/items/[slug]/route.js`| `/items/b`| `Promise<{ slug: 'b' }>`
`app/items/[slug]/route.js`| `/items/c`| `Promise<{ slug: 'c' }>`

#### Static Generation with `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/route#static-generation-with-generatestaticparams)

동적 Route Handler와 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 함께 사용하면 특정 매개변수에 대해 빌드 타임에 응답을 정적으로 생성하고, 나머지 매개변수는 요청 시 동적으로 처리할 수 있습니다.

[Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 때 `generateStaticParams`와 `use cache`를 결합해 프리렌더된 매개변수와 런타임 매개변수 모두에 대한 데이터 캐싱을 활성화할 수 있습니다.

예시와 자세한 내용은 [Route Handler와 함께 사용하는 generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-route-handlers) 문서를 참고하세요.

### URL Query Parameters[](https://nextjs.org/docs/app/api-reference/file-conventions/route#url-query-parameters)

Route Handler에 전달되는 요청 객체는 `NextRequest` 인스턴스이며, [쿼리 매개변수를 더 쉽게 처리할 수 있는 추가 편의 메서드](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl)를 포함합니다.

app/api/search/route.ts

JavaScriptTypeScript
```
    import { type NextRequest } from 'next/server'

    export function GET(request: NextRequest) {
      const searchParams = request.nextUrl.searchParams
      const query = searchParams.get('query')
      // query is "hello" for /api/search?query=hello
    }
```

### Streaming[](https://nextjs.org/docs/app/api-reference/file-conventions/route#streaming)

스트리밍은 OpenAI와 같은 대규모 언어 모델(LLM) 기반의 AI 생성 콘텐츠와 함께 자주 사용됩니다. [AI SDK](https://sdk.vercel.ai/docs/introduction)에 대해 더 알아보세요.

app/api/chat/route.ts

JavaScriptTypeScript
```
    import { openai } from '@ai-sdk/openai'
    import { StreamingTextResponse, streamText } from 'ai'

    export async function POST(req: Request) {
      const { messages } = await req.json()
      const result = await streamText({
        model: openai('gpt-4-turbo'),
        messages,
      })

      return new StreamingTextResponse(result.toAIStream())
    }
```

이러한 추상화는 Web API를 사용해 스트림을 생성합니다. 기본 Web API를 직접 사용할 수도 있습니다.

app/api/route.ts

JavaScriptTypeScript
```
    // https://developer.mozilla.org/docs/Web/API/ReadableStream#convert_async_iterator_to_stream
    function iteratorToStream(iterator: any) {
      return new ReadableStream({
        async pull(controller) {
          const { value, done } = await iterator.next()

          if (done) {
            controller.close()
          } else {
            controller.enqueue(value)
          }
        },
      })
    }

    function sleep(time: number) {
      return new Promise((resolve) => {
        setTimeout(resolve, time)
      })
    }

    const encoder = new TextEncoder()

    async function* makeIterator() {
      yield encoder.encode('<p>One</p>')
      await sleep(200)
      yield encoder.encode('<p>Two</p>')
      await sleep(200)
      yield encoder.encode('<p>Three</p>')
    }

    export async function GET() {
      const iterator = makeIterator()
```

const stream = iteratorToStream(iterator)

      return new Response(stream)
    }

### 요청 본문[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-body)

표준 Web API 메서드를 사용해 `Request` 본문을 읽을 수 있습니다:

app/items/route.ts

JavaScriptTypeScript
```
    export async function POST(request: Request) {
      const res = await request.json()
      return Response.json({ res })
    }
```

### 요청 본문 FormData[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-body-formdata)

`request.formData()` 함수를 사용해 `FormData`를 읽을 수 있습니다:

app/items/route.ts

JavaScriptTypeScript
```
    export async function POST(request: Request) {
      const formData = await request.formData()
      const name = formData.get('name')
      const email = formData.get('email')
      return Response.json({ name, email })
    }
```

`formData`의 데이터는 모두 문자열이므로, 요청을 검증하고 원하는 형식(예: `number`)으로 데이터를 가져오려면 [`zod-form-data`](https://www.npmjs.com/zod-form-data)를 사용하는 것이 좋습니다.

### CORS[](https://nextjs.org/docs/app/api-reference/file-conventions/route#cors)

표준 Web API 메서드를 사용해 특정 Route Handler에 대한 CORS 헤더를 설정할 수 있습니다:

app/api/route.ts

JavaScriptTypeScript
```
    export async function GET(request: Request) {
      return new Response('Hello, Next.js!', {
        status: 200,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
      })
    }
```

> **알아두면 좋은 점** :
>
>   * 여러 Route Handler에 CORS 헤더를 추가하려면 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#cors) 또는 [`next.config.js` 파일](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cors)을 사용할 수 있습니다.
>

### Webhooks[](https://nextjs.org/docs/app/api-reference/file-conventions/route#webhooks)

Route Handler를 사용해 서드파티 서비스에서 오는 webhook을 받을 수 있습니다:

app/api/route.ts

JavaScriptTypeScript
```
    export async function POST(request: Request) {
      try {
        const text = await request.text()
        // Process the webhook payload
      } catch (error) {
        return new Response(`Webhook error: ${error.message}`, {
          status: 400,
        })
      }

      return new Response('Success!', {
        status: 200,
      })
    }
```

특히 Pages Router의 API Routes와 달리, 추가 구성이 필요하더라도 `bodyParser`를 사용할 필요가 없습니다.

### 비 UI 응답[](https://nextjs.org/docs/app/api-reference/file-conventions/route#non-ui-responses)

Route Handler를 사용해 UI가 아닌 콘텐츠를 반환할 수 있습니다. [`sitemap.xml`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts), [`robots.txt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file), [`app icons`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx), [open graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)에는 모두 기본 지원이 있습니다.

app/rss.xml/route.ts

JavaScriptTypeScript
```
    export async function GET() {
      return new Response(
        `<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">

    <channel>
      <title>Next.js Documentation</title>
      <link>https://nextjs.org/docs</link>
      <description>The React Framework for the Web</description>
    </channel>

    </rss>`,
        {
          headers: {
            'Content-Type': 'text/xml',
          },
        }
      )
    }
```

### 세그먼트 설정 옵션[](https://nextjs.org/docs/app/api-reference/file-conventions/route#segment-config-options)

Route Handler는 페이지와 레이아웃과 동일한 [route segment 구성](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)을 사용합니다.

app/items/route.ts

JavaScriptTypeScript
```
    export const dynamic = 'auto'
    export const dynamicParams = true
    export const revalidate = false
    export const fetchCache = 'auto'
    export const runtime = 'nodejs'
    export const preferredRegion = 'auto'
```

자세한 내용은 [API reference](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)를 참고하세요.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/route#version-history)

버전| 변경 사항
---|---
`v15.0.0-RC`| `context.params`가 이제 프로미스입니다. [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150)이 제공됩니다
`v15.0.0-RC`| `GET` 핸들러의 기본 캐싱이 정적에서 동적으로 변경되었습니다
`v13.2.0`| Route Handler가 도입되었습니다.