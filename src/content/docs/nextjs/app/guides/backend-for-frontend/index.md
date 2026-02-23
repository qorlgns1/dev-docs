---
title: '가이드: Backend for Frontend'
description: 'Next.js는 "Backend for Frontend" 패턴을 지원합니다. 이를 통해 공개 엔드포인트를 만들어 HTTP 요청을 처리하고 HTML뿐 아니라 모든 콘텐츠 유형을 반환할 수 있습니다. 또한 데이터 소스에 접근하고 원격 데이터를 업데이트하는 등의 사이드 이펙...'
---

# 가이드: Backend for Frontend | Next.js

Source URL: https://nextjs.org/docs/app/guides/backend-for-frontend

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)Backend for Frontend

# Next.js를 프런트엔드용 백엔드로 사용하는 방법

최종 업데이트 2026년 2월 20일

Next.js는 "Backend for Frontend" 패턴을 지원합니다. 이를 통해 공개 엔드포인트를 만들어 HTTP 요청을 처리하고 HTML뿐 아니라 모든 콘텐츠 유형을 반환할 수 있습니다. 또한 데이터 소스에 접근하고 원격 데이터를 업데이트하는 등의 사이드 이펙트를 수행할 수 있습니다.

새 프로젝트를 시작할 때 `create-next-app`을 `--api` 플래그와 함께 사용하면 새 프로젝트의 `app/` 폴더에 예시 `route.ts`가 자동으로 포함되어 API 엔드포인트 생성 방법을 보여줍니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm create next-app --api
[/code]

> **알아두면 좋아요**: Next.js의 백엔드 기능은 완전한 백엔드 대체제가 아닙니다. 다음과 같은 API 계층 역할을 합니다:
>
>   * 공개적으로 접근 가능
>   * 모든 HTTP 요청 처리
>   * 모든 콘텐츠 유형 반환 가능
>

이 패턴을 구현하려면 다음을 사용하세요:

  * [라우트 핸들러](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  * [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * 페이지 라우터에서는 [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)

## 공개 엔드포인트[](https://nextjs.org/docs/app/guides/backend-for-frontend#public-endpoints)

라우트 핸들러는 공개 HTTP 엔드포인트입니다. 어떤 클라이언트든 접근할 수 있습니다.

`route.ts` 또는 `route.js` 파일 관례를 사용해 라우트 핸들러를 만드세요:

/app/api/route.ts

JavaScriptTypeScript
[code]
    export function GET(request: Request) {}
[/code]

이는 `/api`로 전송된 `GET` 요청을 처리합니다.

예외가 발생할 수 있는 작업에는 `try/catch` 블록을 사용하세요:

/app/api/route.ts

JavaScriptTypeScript
[code]
    import { submit } from '@/lib/submit'

    export async function POST(request: Request) {
      try {
        await submit(request)
        return new Response(null, { status: 204 })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected error'

        return new Response(message, { status: 500 })
      }
    }
[/code]

클라이언트로 전송되는 오류 메시지에 민감한 정보를 노출하지 마세요.

접근을 제한하려면 인증과 권한 부여를 구현하세요. [Authentication](https://nextjs.org/docs/app/guides/authentication)을 참고하세요.

## 콘텐츠 유형[](https://nextjs.org/docs/app/guides/backend-for-frontend#content-types)

라우트 핸들러를 사용하면 JSON, XML, 이미지, 파일, 일반 텍스트 등 UI가 아닌 응답을 제공할 수 있습니다.

Next.js는 일반적인 엔드포인트에 대해 파일 관례를 제공합니다:

  * [`sitemap.xml`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  * [`opengraph-image.jpg`, `twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  * [파비콘, 앱 아이콘, 애플 아이콘](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  * [`manifest.json`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  * [`robots.txt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)

다음과 같은 사용자 정의 엔드포인트도 정의할 수 있습니다:

  * `llms.txt`
  * `rss.xml`
  * `.well-known`

예를 들어 `app/rss.xml/route.ts`는 `rss.xml`용 라우트 핸들러를 만듭니다.

/app/rss.xml/route.ts

JavaScriptTypeScript
[code]
    export async function GET(request: Request) {
      const rssResponse = await fetch(/* rss endpoint */)
      const rssData = await rssResponse.json()

      const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
     <title>${rssData.title}</title>
     <description>${rssData.description}</description>
     <link>${rssData.link}</link>
     <copyright>${rssData.copyright}</copyright>
     ${rssData.items.map((item) => {
       return `<item>
        <title>${item.title}</title>
        <description>${item.description}</description>
        <link>${item.link}</link>
        <pubDate>${item.publishDate}</pubDate>
        <guid isPermaLink="false">${item.guid}</guid>
     </item>`
     })}
    </channel>
    </rss>`

      const headers = new Headers({ 'content-type': 'application/xml' })

      return new Response(rssFeed, { headers })
    }
[/code]

마크업 생성을 위해 사용하는 입력은 반드시 정제하세요.

### 요청 페이로드 소비[](https://nextjs.org/docs/app/guides/backend-for-frontend#consuming-request-payloads)

Request [인스턴스 메서드](https://developer.mozilla.org/en-US/docs/Web/API/Request#instance_methods)인 `.json()`, `.formData()`, `.text()` 등을 사용해 요청 본문에 접근하세요.

`GET`과 `HEAD` 요청에는 본문이 없습니다.

/app/api/echo-body/route.ts

JavaScriptTypeScript
[code]
    export async function POST(request: Request) {
      const res = await request.json()
      return Response.json({ res })
    }
[/code]

> **알아두면 좋아요**: 다른 시스템에 전달하기 전에 데이터를 검증하세요

/app/api/send-email/route.ts

JavaScriptTypeScript
[code]
    import { sendMail, validateInputs } from '@/lib/email-transporter'

    export async function POST(request: Request) {
      const formData = await request.formData()
      const email = formData.get('email')
      const contents = formData.get('contents')

      try {
        await validateInputs({ email, contents })
        const info = await sendMail({ email, contents })

        return Response.json({ messageId: info.messageId })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'

        return new Response(message, { status: 500 })
      }
    }
[/code]

요청 본문은 한 번만 읽을 수 있습니다. 다시 읽어야 한다면 요청을 복제하세요:

/app/api/clone/route.ts

JavaScriptTypeScript
[code]
    export async function POST(request: Request) {
      try {
        const clonedRequest = request.clone()

        await request.body()
        await clonedRequest.body()
        await request.body() // Throws error

        return new Response(null, { status: 204 })
      } catch {
        return new Response(null, { status: 500 })
      }
    }
[/code]

## 데이터 조작[](https://nextjs.org/docs/app/guides/backend-for-frontend#manipulating-data)

라우트 핸들러는 하나 이상의 소스에서 데이터를 변환, 필터링, 집계할 수 있습니다. 이를 통해 프런트엔드에서 로직을 분리하고 내부 시스템 노출을 방지합니다.

또한 무거운 계산을 서버로 오프로드해 클라이언트의 배터리와 데이터 사용량을 줄일 수 있습니다.
[code]
    import { parseWeatherData } from '@/lib/weather'

    export async function POST(request: Request) {
      const body = await request.json()
      const searchParams = new URLSearchParams({ lat: body.lat, lng: body.lng })

      try {
        const weatherResponse = await fetch(`${weatherEndpoint}?${searchParams}`)

        if (!weatherResponse.ok) {
          /* handle error */
        }

        const weatherData = await weatherResponse.text()
        const payload = parseWeatherData.asJSON(weatherData)

        return new Response(payload, { status: 200 })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'

        return new Response(message, { status: 500 })
      }
    }
[/code]

> **알아두면 좋아요**: 이 예시는 위치 데이터를 URL에 넣지 않기 위해 `POST`를 사용합니다. `GET` 요청은 캐시되거나 로깅될 수 있어 민감한 정보가 노출될 수 있습니다.

## 백엔드로 프록시하기[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxying-to-a-backend)

라우트 핸들러를 `proxy`로 사용해 다른 백엔드로 요청을 전달할 수 있습니다. 요청을 전달하기 전에 검증 로직을 추가하세요.

/app/api/[...slug]/route.ts

JavaScriptTypeScript
[code]
    import { isValidRequest } from '@/lib/utils'

    export async function POST(request: Request, { params }) {
      const clonedRequest = request.clone()
      const isValid = await isValidRequest(clonedRequest)

      if (!isValid) {
        return new Response(null, { status: 400, statusText: 'Bad Request' })
      }

      const { slug } = await params
      const pathname = slug.join('/')
      const proxyURL = new URL(pathname, 'https://nextjs.org')
      const proxyRequest = new Request(proxyURL, request)

      try {
        return fetch(proxyRequest)
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'

        return new Response(message, { status: 500 })
      }
    }
[/code]

또는 다음을 사용하세요:

  * `proxy` [재작성](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)
  * `next.config.js`의 [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)

## NextRequest와 NextResponse[](https://nextjs.org/docs/app/guides/backend-for-frontend#nextrequest-and-nextresponse)

Next.js는 [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request)와 [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) Web API를 확장하여 일반 작업을 단순화하는 메서드를 제공합니다. 이러한 확장은 라우트 핸들러와 프록시 모두에서 사용할 수 있습니다.

두 객체는 쿠키 읽기 및 조작 메서드를 제공합니다.

`NextRequest`에는 수신 요청에서 파싱된 값을 노출하는 [`nextUrl`](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl) 속성이 있어 요청의 pathname과 검색 매개변수에 쉽게 접근할 수 있습니다.

`NextResponse`는 `next()`, `json()`, `redirect()`, `rewrite()`와 같은 헬퍼를 제공합니다.

`NextRequest`를 `Request`를 기대하는 모든 함수에 전달할 수 있고, `Response`가 필요한 곳에 `NextResponse`를 반환할 수 있습니다.

/app/echo-pathname/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'

    export async function GET(request: NextRequest) {
      const nextUrl = request.nextUrl

      if (nextUrl.searchParams.get('redirect')) {
        return NextResponse.redirect(new URL('/', request.url))
      }

      if (nextUrl.searchParams.get('rewrite')) {
        return NextResponse.rewrite(new URL('/', request.url))
      }

      return NextResponse.json({ pathname: nextUrl.pathname })
    }
[/code]

[`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)와 [`NextResponse`](https://nextjs.org/docs/app/api-reference/functions/next-response)에 대해 더 알아보세요.

## 웹후크와 콜백 URL[](https://nextjs.org/docs/app/guides/backend-for-frontend#webhooks-and-callback-urls)

라우트 핸들러를 사용해 서드파티 애플리케이션의 이벤트 알림을 수신하세요.

예를 들어 CMS의 콘텐츠가 변경될 때 라우트를 재검증할 수 있습니다. 변경 시 특정 엔드포인트를 호출하도록 CMS를 구성하세요.

/app/webhook/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'

    export async function GET(request: NextRequest) {
      const token = request.nextUrl.searchParams.get('token')

      if (token !== process.env.REVALIDATE_SECRET_TOKEN) {
        return NextResponse.json({ success: false }, { status: 401 })
      }

      const tag = request.nextUrl.searchParams.get('tag')

      if (!tag) {
        return NextResponse.json({ success: false }, { status: 400 })
      }

      revalidateTag(tag)

      return NextResponse.json({ success: true })
    }
[/code]

콜백 URL도 또 다른 사용 사례입니다. 사용자가 서드파티 플로우를 완료하면 서드파티가 콜백 URL로 사용자를 돌려보냅니다. 라우트 핸들러를 사용해 응답을 검증하고 사용자를 어디로 리디렉션할지 결정하세요.

/app/auth/callback/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'

    export async function GET(request: NextRequest) {
[/code]

const token = request.nextUrl.searchParams.get('session_token')
      const redirectUrl = request.nextUrl.searchParams.get('redirect_url')

      const response = NextResponse.redirect(new URL(redirectUrl, request.url))

      response.cookies.set({
        value: token,
        name: '_token',
        path: '/',
        secure: true,
        httpOnly: true,
        expires: undefined, // session cookie
      })

      return response
    }
[/code]

## 리디렉션[](https://nextjs.org/docs/app/guides/backend-for-frontend#redirects)

app/api/route.ts

JavaScriptTypeScript
[code]
    import { redirect } from 'next/navigation'

    export async function GET(request: Request) {
      redirect('https://nextjs.org/')
    }
[/code]

[`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) 및 [`permanentRedirect`](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)에서 리디렉션에 대해 더 알아보세요.

## 프록시[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)

프로젝트당 하나의 `proxy` 파일만 허용됩니다. 특정 경로를 대상으로 하려면 `config.matcher`를 사용하세요. [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에 대해 더 알아보세요.

요청이 라우트 경로에 도달하기 전에 응답을 생성하려면 `proxy`를 사용하세요.

proxy.ts

JavaScriptTypeScript
[code]
    import { isAuthenticated } from '@lib/auth'

    export const config = {
      matcher: '/api/:function*',
    }

    export function proxy(request: Request) {
      if (!isAuthenticated(request)) {
        return Response.json(
          { success: false, message: 'authentication failed' },
          { status: 401 }
        )
      }
    }
[/code]

`proxy`를 사용하여 요청을 프록시할 수도 있습니다:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'

    export function proxy(request: Request) {
      if (request.nextUrl.pathname === '/proxy-this-path') {
        const rewriteUrl = new URL('https://nextjs.org')
        return NextResponse.rewrite(rewriteUrl)
      }
    }
[/code]

`proxy`가 생성할 수 있는 또 다른 유형의 응답은 리디렉션입니다:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'

    export function proxy(request: Request) {
      if (request.nextUrl.pathname === '/v1/docs') {
        request.nextUrl.pathname = '/v2/docs'
        return NextResponse.redirect(request.nextUrl)
      }
    }
[/code]

## 보안[](https://nextjs.org/docs/app/guides/backend-for-frontend#security)

### 헤더 처리[](https://nextjs.org/docs/app/guides/backend-for-frontend#working-with-headers)

헤더가 어디로 전달되는지 신중하게 결정하고, 들어오는 요청 헤더를 그대로 나가는 응답으로 전달하는 것을 피하세요.

  * **업스트림 요청 헤더**: Proxy에서 `NextResponse.next({ request: { headers } })`는 서버가 수신하는 헤더를 수정하며 클라이언트에게 노출하지 않습니다.
  * **응답 헤더**: `new Response(..., { headers })`, `NextResponse.json(..., { headers })`, `NextResponse.next({ headers })`, 또는 `response.headers.set(...)`는 헤더를 클라이언트로 다시 보냅니다. 여기에 민감한 값을 추가하면 클라이언트가 볼 수 있습니다.

[Proxy에서의 NextResponse 헤더](https://nextjs.org/docs/app/api-reference/functions/next-response#next)를 참고하세요.

### 레이트 리미팅[](https://nextjs.org/docs/app/guides/backend-for-frontend#rate-limiting)

Next.js 백엔드에서 레이트 리미팅을 구현할 수 있습니다. 코드 기반 검사 외에도 호스트가 제공하는 레이트 리미팅 기능을 활성화하세요.

/app/resource/route.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
    import { checkRateLimit } from '@/lib/rate-limit'

    export async function POST(request: Request) {
      const { rateLimited } = await checkRateLimit(request)

      if (rateLimited) {
        return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
      }

      return new Response(null, { status: 204 })
    }
[/code]

### 페이로드 검증[](https://nextjs.org/docs/app/guides/backend-for-frontend#verify-payloads)

들어오는 요청 데이터를 절대 신뢰하지 마세요. 콘텐츠 유형과 크기를 검증하고 사용 전에 XSS를 차단하세요.

남용을 방지하고 서버 리소스를 보호하려면 타임아웃을 사용하세요.

사용자 생성 정적 자산은 전용 서비스에 저장하세요. 가능하다면 브라우저에서 업로드하고 반환된 URI를 데이터베이스에 저장해 요청 크기를 줄이세요.

### 보호된 리소스 접근[](https://nextjs.org/docs/app/guides/backend-for-frontend#access-to-protected-resources)

액세스를 허용하기 전에 항상 자격 증명을 검증하세요. 인증과 인가를 위해 프록시만 의존하지 마세요.

응답과 백엔드 로그에서 민감하거나 불필요한 데이터를 제거하세요.

자격 증명과 API 키를 정기적으로 교체하세요.

## 프리플라이트 요청[](https://nextjs.org/docs/app/guides/backend-for-frontend#preflight-requests)

프리플라이트 요청은 `OPTIONS` 메서드를 사용해, 원본·메서드·헤더 기반으로 요청 허용 여부를 서버에 묻습니다.

`OPTIONS`가 정의되지 않으면 Next.js가 자동으로 추가하고, 다른 메서드 정의를 기반으로 `Allow` 헤더를 설정합니다.

  * [CORS](https://nextjs.org/docs/app/api-reference/file-conventions/route#cors)

## 라이브러리 패턴[](https://nextjs.org/docs/app/guides/backend-for-frontend#library-patterns)

커뮤니티 라이브러리는 Route Handler를 위해 팩토리 패턴을 사용하는 경우가 많습니다.

/app/api/[...path]/route.ts
[code]
    import { createHandler } from 'third-party-library'

    const handler = createHandler({
      /* library-specific options */
    })

    export const GET = handler
    // or
    export { handler as POST }
[/code]

이는 `GET`과 `POST` 요청에 공용 핸들러를 생성하며, 라이브러리는 요청의 `method`와 `pathname`을 기반으로 동작을 커스터마이즈합니다.

라이브러리는 `proxy` 팩토리를 제공할 수도 있습니다.

proxy.ts
[code]
    import { createMiddleware } from 'third-party-library'

    export default createMiddleware()
[/code]

> **알아두면 좋아요**: 서드파티 라이브러리는 여전히 `proxy`를 `middleware`라고 부를 수 있습니다.

## 추가 예시[](https://nextjs.org/docs/app/guides/backend-for-frontend#more-examples)

[Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route#examples)와 [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#examples) API 참조에서 더 많은 예시를 확인하세요.

예시에는 [Cookies](https://nextjs.org/docs/app/api-reference/file-conventions/route#cookies), [Headers](https://nextjs.org/docs/app/api-reference/file-conventions/route#headers), [Streaming](https://nextjs.org/docs/app/api-reference/file-conventions/route#streaming), Proxy [negative matching](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#negative-matching), 기타 유용한 코드 스니펫이 포함됩니다.

## 주의 사항[](https://nextjs.org/docs/app/guides/backend-for-frontend#caveats)

### 서버 컴포넌트[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-components)

서버 컴포넌트에서는 데이터를 Route Handler가 아닌 데이터 소스에서 직접 가져오세요.

빌드 시 사전 렌더링되는 서버 컴포넌트가 Route Handler를 사용하면 빌드 단계가 실패합니다. 빌드 중에는 이러한 요청을 수신할 서버가 없기 때문입니다.

온디맨드로 렌더링되는 서버 컴포넌트에서 Route Handler를 이용하면, 핸들러와 렌더 프로세스 간의 추가 HTTP 왕복으로 인해 느려집니다.

> 서버 측 `fetch` 요청은 절대 URL을 사용합니다. 이는 외부 서버로의 HTTP 왕복을 의미합니다. 개발 중에는 개발 서버가 외부 서버 역할을 하며, 빌드 시에는 서버가 없고, 런타임에는 공개 도메인을 통해 서버가 제공됩니다.

서버 컴포넌트는 대부분의 데이터 페칭 요구사항을 충족합니다. 그러나 다음과 같은 경우 클라이언트 측 데이터 페칭이 필요할 수 있습니다:

  * 클라이언트 전용 Web API에 의존하는 데이터:
    * Geo-location API
    * Storage API
    * Audio API
    * File API
  * 자주 폴링되는 데이터

이러한 경우 [`swr`](https://swr.vercel.app/) 또는 [`react-query`](https://tanstack.com/query/latest/docs/framework/react/overview) 같은 커뮤니티 라이브러리를 사용하세요.

### 서버 액션[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-actions)

서버 액션은 클라이언트에서 서버 측 코드를 실행하게 해주며, 주된 목적은 프론트엔드 클라이언트에서 데이터를 변경하는 것입니다.

서버 액션은 큐에 쌓입니다. 데이터 페칭에 사용하면 순차 실행이 발생합니다.

### `export` 모드[](https://nextjs.org/docs/app/guides/backend-for-frontend#export-mode)

`export` 모드는 런타임 서버 없이 정적 사이트를 출력합니다. 이 모드는 정적 사이트를 생성하며 런타임 서버가 없기 때문에 Next.js 런타임이 필요한 기능은 [지원되지 않습니다](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).

`export mode`에서는 `'force-static'`으로 설정된 [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) 라우트 세그먼트 구성과 함께 `GET` Route Handler만 지원됩니다.

이는 정적 HTML, JSON, TXT 등 파일을 생성하는 데 사용할 수 있습니다.

app/hello-world/route.ts
[code]
    export const dynamic = 'force-static'

    export function GET() {
      return new Response('Hello World', { status: 200 })
    }
[/code]

### 배포 환경[](https://nextjs.org/docs/app/guides/backend-for-frontend#deployment-environment)

일부 호스트는 Route Handler를 람다 함수로 배포합니다. 이 경우:

  * Route Handler는 요청 간 데이터를 공유할 수 없습니다.
  * 파일 시스템에 쓰기를 지원하지 않을 수 있습니다.
  * 오래 실행되는 핸들러는 타임아웃으로 종료될 수 있습니다.
  * 응답이 생성되면 연결이 종료되므로 WebSocket이 작동하지 않을 수 있습니다.

## API 레퍼런스

Route Handler와 Proxy에 대해 자세히 알아보세요.

- [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  - 특수 파일 route.js에 대한 API 레퍼런스.

- [proxy.js](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  - proxy.js 파일에 대한 API 레퍼런스.

Send
