---
title: '라우팅: API Routes'
description: '> 알아두면 좋아요 : App Router를 사용하는 경우 API Routes 대신 Server Components 또는 Route Handlers를 사용할 수 있습니다.'
---

# 라우팅: API Routes | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/api-routes

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[라우팅](https://nextjs.org/docs/pages/building-your-application/routing)API Routes

# API Routes

최종 업데이트 2026년 2월 20일

예시

  * [API Routes 요청 도우미](https://github.com/vercel/next.js/tree/canary/examples/api-routes-proxy)
  * [GraphQL과 함께 사용하는 API Routes](https://github.com/vercel/next.js/tree/canary/examples/api-routes-graphql)
  * [REST와 함께 사용하는 API Routes](https://github.com/vercel/next.js/tree/canary/examples/api-routes-rest)
  * [CORS와 함께 사용하는 API Routes](https://github.com/vercel/next.js/tree/canary/examples/api-routes-cors)

> **알아두면 좋아요** : App Router를 사용하는 경우 API Routes 대신 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) 또는 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)를 사용할 수 있습니다.

API Routes는 Next.js로 **공개 API** 를 구축할 수 있는 솔루션을 제공합니다.

`pages/api` 폴더 내부의 모든 파일은 `/api/*` 로 매핑되며 `page` 가 아닌 API 엔드포인트로 처리됩니다. 이들은 서버 전용 번들이므로 클라이언트 번들 크기를 증가시키지 않습니다.

예를 들어 다음 API Route는 상태 코드 `200` 인 JSON 응답을 반환합니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    type ResponseData = {
      message: string
    }

    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<ResponseData>
    ) {
      res.status(200).json({ message: 'Hello from Next.js!' })
    }
[/code]

> **알아두면 좋아요** :
>
>   * API Routes는 기본적으로 [CORS 헤더를 지정하지 않습니다](https://developer.mozilla.org/docs/Web/HTTP/CORS). 즉 기본값으로 **동일 출처만** 허용합니다. [CORS 요청 도우미](https://github.com/vercel/next.js/tree/canary/examples/api-routes-cors)로 요청 핸들러를 감싸 이 동작을 사용자 지정할 수 있습니다.
>   * API Routes는 [정적 내보내기](https://nextjs.org/docs/pages/guides/static-exports)와 함께 사용할 수 없습니다. 단, App Router의 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)는 가능합니다.
>   * API Routes는 `next.config.js` 의 [`pageExtensions` 구성](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)의 영향을 받습니다.
>

## Parameters[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#parameters)
[code]
    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      // ...
    }
[/code]

  * `req`: [http.IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)의 인스턴스
  * `res`: [http.ServerResponse](https://nodejs.org/api/http.html#class-httpserverresponse)의 인스턴스

## HTTP Methods[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#http-methods)

API Route에서 다양한 HTTP 메서드를 처리하려면 요청 핸들러에서 `req.method` 를 사용할 수 있습니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      if (req.method === 'POST') {
        // Process a POST request
      } else {
        // Handle any other HTTP method
      }
    }
[/code]

## Request Helpers[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#request-helpers)

API Routes는 들어오는 요청(`req`)을 파싱하는 기본 제공 요청 도우미를 제공합니다:

  * `req.cookies` \- 요청이 보낸 쿠키를 포함한 객체입니다. 기본값은 `{}`
  * `req.query` \- [쿼리 문자열](https://en.wikipedia.org/wiki/Query_string)을 포함한 객체입니다. 기본값은 `{}`
  * `req.body` \- `content-type` 으로 파싱된 body를 포함한 객체이며, body가 없으면 `null` 입니다

### Custom config[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#custom-config)

모든 API Route는 다음과 같은 기본 구성을 변경하기 위해 `config` 객체를 내보낼 수 있습니다:
[code]
    export const config = {
      api: {
        bodyParser: {
          sizeLimit: '1mb',
        },
      },
      // Specifies the maximum allowed duration for this function to execute (in seconds)
      maxDuration: 5,
    }
[/code]

`bodyParser` 는 자동으로 활성화됩니다. body를 `Stream` 또는 [`raw-body`](https://www.npmjs.com/package/raw-body)로 소비하려면 이를 `false` 로 설정하세요.

자동 `bodyParsing` 을 비활성화하는 한 가지 사용 사례는 예를 들어 [GitHub](https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#validating-payloads-from-github)와 같은 **웹훅** 요청의 원시 body를 검증하는 것입니다.
[code]
    export const config = {
      api: {
        bodyParser: false,
      },
    }
[/code]

`bodyParser.sizeLimit` 는 [bytes](https://github.com/visionmedia/bytes.js)가 지원하는 형식이라면 어떤 것이든 사용할 수 있으며, 파싱된 body의 최대 크기입니다:
[code]
    export const config = {
      api: {
        bodyParser: {
          sizeLimit: '500kb',
        },
      },
    }
[/code]

`externalResolver` 는 이 라우트가 _express_ 또는 _connect_ 와 같은 외부 리졸버에 의해 처리되고 있음을 서버에 명시적으로 알리는 플래그입니다. 이 옵션을 활성화하면 해결되지 않은 요청에 대한 경고가 비활성화됩니다.
[code]
    export const config = {
      api: {
        externalResolver: true,
      },
    }
[/code]

`responseLimit` 는 기본적으로 활성화되어 있으며 API Routes의 응답 본문이 4MB를 초과하면 경고합니다.

서버리스 환경이 아닌 곳에서 Next.js를 사용하고 CDN 또는 전용 미디어 호스트를 사용하지 않을 때의 성능 영향을 이해한다면, 이 제한을 `false` 로 설정할 수 있습니다.
[code]
    export const config = {
      api: {
        responseLimit: false,
      },
    }
[/code]

`responseLimit` 은 바이트 수나 `bytes` 가 지원하는 문자열 형식(`1000`, `'500kb'`, `'3mb'` 등)을 받을 수도 있습니다. 이 값은 경고가 표시되기 전의 최대 응답 크기입니다. 기본값은 4MB입니다(위 참조).
[code]
    export const config = {
      api: {
        responseLimit: '8mb',
      },
    }
[/code]

## Response Helpers[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers)

[Server Response 객체](https://nodejs.org/api/http.html#http_class_http_serverresponse)(종종 `res` 로 줄여 씀)에는 Express.js와 유사한 도우미 메서드가 포함되어 있어 개발자 경험을 개선하고 새로운 API 엔드포인트를 더 빠르게 만들 수 있습니다.

포함된 도우미는 다음과 같습니다:

  * `res.status(code)` \- 상태 코드를 설정하는 함수입니다. `code` 는 유효한 [HTTP 상태 코드](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)여야 합니다.
  * `res.json(body)` \- JSON 응답을 전송합니다. `body` 는 [직렬화 가능한 객체](https://developer.mozilla.org/docs/Glossary/Serialization)여야 합니다.
  * `res.send(body)` \- HTTP 응답을 전송합니다. `body` 는 `string`, `object`, `Buffer` 가 될 수 있습니다.
  * `res.redirect([status,] path)` \- 지정된 경로나 URL로 리디렉션합니다. `status` 는 유효한 [HTTP 상태 코드](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)여야 합니다. 지정하지 않으면 `status` 는 "307" "Temporary redirect"로 기본 설정됩니다.
  * `res.revalidate(urlPath)` \- `getStaticProps` 를 사용하여 [수요 기반으로 페이지를 재검증](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)합니다. `urlPath` 는 `string` 이어야 합니다.

### 응답의 상태 코드 설정[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#setting-the-status-code-of-a-response)

클라이언트에 응답을 보낼 때 응답의 상태 코드를 설정할 수 있습니다.

다음 예시는 응답의 상태 코드를 `200` (`OK`)으로 설정하고 JSON 응답으로 `Hello from Next.js!` 값을 가진 `message` 속성을 반환합니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    type ResponseData = {
      message: string
    }

    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<ResponseData>
    ) {
      res.status(200).json({ message: 'Hello from Next.js!' })
    }
[/code]

### JSON 응답 보내기[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#sending-a-json-response)

클라이언트로 응답을 보낼 때 JSON 응답을 보낼 수 있으며, 이 객체는 [직렬화 가능](https://developer.mozilla.org/docs/Glossary/Serialization)해야 합니다. 실제 애플리케이션에서는 요청된 엔드포인트 결과에 따라 클라이언트에 요청 상태를 알리고 싶을 수 있습니다.

다음 예시는 상태 코드 `200` (`OK`)과 비동기 작업 결과로 JSON 응답을 보냅니다. 발생할 수 있는 오류를 처리하기 위해 try-catch 블록에 포함되어 있으며, 적절한 상태 코드와 오류 메시지를 포착해 클라이언트에 다시 보냅니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      try {
        const result = await someAsyncOperation()
        res.status(200).json({ result })
      } catch (err) {
        res.status(500).json({ error: 'failed to load data' })
      }
    }
[/code]

### HTTP 응답 보내기[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#sending-a-http-response)

HTTP 응답을 보내는 방법은 JSON 응답을 보낼 때와 동일합니다. 유일한 차이는 응답 본문이 `string`, `object`, `Buffer` 가 될 수 있다는 점입니다.

다음 예시는 상태 코드 `200` (`OK`)와 비동기 작업 결과로 HTTP 응답을 보냅니다.

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      try {
        const result = await someAsyncOperation()
        res.status(200).send({ result })
      } catch (err) {
        res.status(500).send({ error: 'failed to fetch data' })
      }
    }
[/code]

### 지정된 경로나 URL로 리디렉션[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#redirects-to-a-specified-path-or-url)

양식을 예로 들면, 사용자가 양식을 제출한 후 클라이언트를 지정된 경로나 URL로 리디렉션하고 싶을 수 있습니다.

다음 예시는 양식이 성공적으로 제출되면 클라이언트를 `/` 경로로 리디렉션합니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const { name, message } = req.body

      try {
        await handleFormInputAsync({ name, message })
        res.redirect(307, '/')
      } catch (err) {
        res.status(500).send({ error: 'Failed to fetch data' })
      }
    }
[/code]

### TypeScript 타입 추가하기[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#adding-typescript-types)

API Routes를 더 타입 안전하게 만들려면 `next` 에서 `NextApiRequest` 및 `NextApiResponse` 타입을 가져올 수 있으며, 여기에 응답 데이터 타입도 지정할 수 있습니다:
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    type ResponseData = {
      message: string
    }

    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<ResponseData>
    ) {
      res.status(200).json({ message: 'Hello from Next.js!' })
    }
[/code]

> **알아두면 좋아요** : `NextApiRequest`의 본문은 클라이언트가 어떤 페이로드든 보낼 수 있기 때문에 `any`입니다. 사용하기 전에 반드시 런타임에서 본문의 타입과 구조를 검증하세요.

## 동적 API 라우트[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#dynamic-api-routes)

API 라우트는 [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 지원하며, `pages/`에 사용하는 것과 동일한 파일 명명 규칙을 따릅니다.

pages/api/post/[pid].ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      const { pid } = req.query
      res.end(`Post: ${pid}`)
    }
[/code]

이제 `/api/post/abc` 요청은 `Post: abc`라는 텍스트로 응답합니다.

### 캣치올 API 라우트[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#catch-all-api-routes)

API 라우트는 대괄호 안에 점 세 개(`...`)를 추가하여 모든 경로를 포착하도록 확장할 수 있습니다. 예를 들어:

  * `pages/api/post/[...slug].js`는 `/api/post/a`뿐 아니라 `/api/post/a/b`, `/api/post/a/b/c` 등에도 매칭됩니다.

> **알아두면 좋아요** : `slug` 대신 `[...param]`처럼 다른 이름을 사용할 수 있습니다.

매칭된 파라미터는 페이지로 쿼리 파라미터(예시에서는 `slug`)로 전달되며, 항상 배열 형태입니다. 따라서 `/api/post/a` 경로는 다음과 같은 `query` 객체를 갖습니다:
[code]
    { "slug": ["a"] }
[/code]

`/api/post/a/b`와 동일하게 매칭되는 다른 경로의 경우, 새로운 파라미터가 배열에 추가됩니다:
[code]
    { "slug": ["a", "b"] }
[/code]

예시:

pages/api/post/[...slug].ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      const { slug } = req.query
      res.end(`Post: ${slug.join(', ')}`)
    }
[/code]

이제 `/api/post/a/b/c` 요청은 `Post: a, b, c`라는 텍스트로 응답합니다.

### 선택적 캣치올 API 라우트[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#optional-catch-all-api-routes)

캣치올 라우트는 파라미터를 이중 대괄호(`[[...slug]]`)로 감싸 선택적으로 만들 수 있습니다.

예를 들어 `pages/api/post/[[...slug]].js`는 `/api/post`, `/api/post/a`, `/api/post/a/b` 등과 매칭됩니다.

캣치올과 선택적 캣치올 라우트의 주요 차이는 선택적 라우트에서는 파라미터 없이도 경로가 매칭된다는 점입니다(위 예시의 `/api/post`).

`query` 객체는 다음과 같습니다:
[code]
    { } // GET `/api/post` (빈 객체)
    { "slug": ["a"] } // `GET /api/post/a` (단일 요소 배열)
    { "slug": ["a", "b"] } // `GET /api/post/a/b` (다중 요소 배열)
[/code]

### 주의 사항[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#caveats)

  * 사전에 정의된 API 라우트가 동적 API 라우트보다 우선하며, 동적 API 라우트는 캣치올 API 라우트보다 우선합니다. 다음 예시를 참고하세요:
    * `pages/api/post/create.js` \- `/api/post/create`와 매칭
    * `pages/api/post/[pid].js` \- `/api/post/1`, `/api/post/abc` 등과 매칭하지만 `/api/post/create`와는 매칭되지 않음
    * `pages/api/post/[...slug].js` \- `/api/post/1/2`, `/api/post/a/b/c` 등과 매칭하지만 `/api/post/create`, `/api/post/abc`와는 매칭되지 않음

## 스트리밍 응답[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#streaming-responses)

Pages Router는 API 라우트에서 스트리밍 응답을 지원하지만, Next.js 14 이상이라면 App Router를 점차 채택하고 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)를 사용할 것을 권장합니다.

다음은 `writeHead`를 사용해 API 라우트에서 응답을 스트리밍하는 방법입니다:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      res.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-store',
      })
      let i = 0
      while (i < 10) {
        res.write(`data: ${i}\n\n`)
        i++
        await new Promise((resolve) => setTimeout(resolve, 1000))
      }
      res.end()
    }
[/code]

보내기
