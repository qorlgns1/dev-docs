---
title: '간단한 초기화[​](https://next-auth.js.org/configuration/initialization#simple-initialization "Direct link to heading")'
description: "NextAuth.js의 주요 진입점은 에서 import하는  메서드입니다. 이 메서드는 REST API 섹션에 정의된 대로 다양한 유형의 요청을 처리합니다."
---

Source URL: https://next-auth.js.org/configuration/initialization

# 초기화 | NextAuth.js

버전: v4

NextAuth.js의 주요 진입점은 `next-auth`에서 import하는 `NextAuth` 메서드입니다. 이 메서드는 [REST API](https://next-auth.js.org/getting-started/rest-api) 섹션에 정의된 대로 다양한 유형의 요청을 처리합니다.

정보

NextAuth.js는 초기화에 [Edge Runtime](https://nextjs.org/docs/api-reference/edge-runtime)을 사용할 수 없습니다. 반면, 곧 출시될 [`@auth/nextjs` library](https://authjs.dev/reference/next-auth) (`next-auth`를 대체 예정)는 완전히 호환될 예정입니다.

NextAuth.js는 몇 가지 다른 방식으로 초기화할 수 있습니다.

## 간단한 초기화[​](https://next-auth.js.org/configuration/initialization#simple-initialization "Direct link to heading")

### API Routes (`pages`)[​](https://next-auth.js.org/configuration/initialization#api-routes-pages "Direct link to heading")

Next.js에서는 특정 경로로 시작하는 모든 요청을 받는 API 라우트를 정의할 수 있습니다. 편의상 이를 [Catch all API routes](https://nextjs.org/docs/api-routes/dynamic-api-routes#catch-all-api-routes)라고 합니다.

`/pages/api/auth/[...nextauth]` JS/TS 파일을 정의하면, `/api/auth/*`로 시작하는 모든 API 요청을 `[...nextauth]` 파일에 작성된 코드가 처리하도록 NextAuth.js에 지시하게 됩니다.

/pages/api/auth/[...nextauth].ts

```
    import NextAuth from "next-auth"

    export default NextAuth({
      ...
    })

```

여기서는 [options](https://next-auth.js.org/configuration/options)를 `NextAuth`에 전달하기만 하면 되고, 나머지는 `NextAuth`가 처리합니다.

이 방식은 코드가 단순해지고 인증 흐름에서 발생 가능한 오류를 줄여 주기 때문에 튜토리얼/문서의 다른 부분에서 권장되는 초기화 방식입니다.

### Route Handlers (`app/`)[​](https://next-auth.js.org/configuration/initialization#route-handlers-app "Direct link to heading")

[Next.js 13.2](https://nextjs.org/blog/next-13-2#custom-route-handlers)에서는 App Router (`app/`)에서 REST 스타일 요청을 처리하는 권장 방식인 [Route Handlers](https://beta.nextjs.org/docs/routing/route-handlers)를 도입했습니다.

API Routes와 매우 유사하게, Route Handler로도 NextAuth.js를 초기화할 수 있습니다.

/app/api/auth/[...nextauth]/route.ts

```
    import NextAuth from "next-auth"

    const handler = NextAuth({
      ...
    })

    export { handler as GET, handler as POST }

```

내부적으로 NextAuth.js는 Route Handler에서 초기화되고 있음을 감지하고(전달된 값이 Web [`Request` instance](https://developer.mozilla.org/en-US/docs/Web/API/Request)임을 통해 판단), [`Response` instance](https://developer.mozilla.org/en-US/docs/Web/API/Response)를 반환하는 핸들러를 돌려줍니다. Route Handler 파일은 요청을 처리하고 응답을 반환하는 이름 있는 핸들러 함수를 export해야 합니다. NextAuth.js가 정상 동작하려면 `GET`과 `POST` 핸들러가 필요하므로, 이 두 가지를 export합니다.

정보

기술적으로 Route Handler에서는 `api/` 접두사가 필수는 아니지만, 더 쉬운 마이그레이션을 위해 필수로 유지하기로 했습니다.

## 고급 초기화[​](https://next-auth.js.org/configuration/initialization#advanced-initialization "Direct link to heading")

정보

아래 내용은 API Routes를 사용한 고급 초기화를 설명하지만, [Route Handlers](https://beta.nextjs.org/docs/routing/route-handlers)를 사용할 때도 거의 동일하게 적용됩니다. 대신 `NextAuth`는 Route Handler의 처음 두 인자를 받고, 세 번째 인자는 [auth options](https://next-auth.js.org/configuration/options)가 됩니다.

특정 사용 사례에서 NextAuth.js가 원래 설계된 방식과 조금 다르게 동작하도록 해야 한다면, `[...nextauth].ts` 설정 파일은 **일반적인 [API Route](https://nextjs.org/docs/api-routes/introduction)**일 뿐이라는 점을 기억하세요.

즉, NextAuth.js를 다음과 같이 초기화할 수 있습니다:

/pages/api/auth/[...nextauth].ts

```
    import type { NextApiRequest, NextApiResponse } from "next"
    import NextAuth from "next-auth"

    export default async function auth(req: NextApiRequest, res: NextApiResponse) {
      // Do whatever you want here, before the request is passed down to `NextAuth`
      return await NextAuth(req, res, {
        ...
      })
    }

```

`...` 부분은 여전히 [options](https://next-auth.js.org/configuration/options)지만, 이제 요청에서 특정 동작을 실행/수정할 수 있습니다.

예를 들어 요청을 로깅하거나, 헤더를 추가하거나, `query` 또는 `body` 파라미터를 읽는 등 API 라우트에서 할 수 있는 작업을 수행할 수 있습니다.

팁

이것은 catch-all 라우트이므로, 어떤 종류의 NextAuth.js "action"이 실행 중인지 확인해야 합니다. REST API와 `req.query.nextauth` 파라미터를 비교하세요.

예를 들어 요청이 POST 메서드일 때 "callback" action에서 무언가를 실행하려면 `req.query.nextauth.includes("callback") && req.method === "POST"`를 확인할 수 있습니다.

참고

`NextAuth`는 내부적으로 응답을 종료합니다(`res.end`, `res.send` 또는 유사한 메서드 호출). 따라서 함수 본문에서 `NextAuth` **이후에** 코드를 실행하면 안 됩니다. `return NextAuth`를 사용하면 이를 잊지 않게 됩니다.

이 방식으로 생성한 모든 변수는 같은 스코프에 있으므로 `NextAuth` options에서도 사용할 수 있습니다.

/pages/api/auth/[...nextauth].ts

```
    import type { NextApiRequest, NextApiResponse } from "next"
    import NextAuth from "next-auth"

    export default async function auth(req: NextApiRequest, res: NextApiResponse) {

      if(req.query.nextauth.includes("callback") && req.method === "POST") {
        console.log(
          "Handling callback request from my Identity Provider",
          req.body
        )
      }

      // Get a custom cookie value from the request
      const someCookie = req.cookies["some-custom-cookie"]

      return await NextAuth(req, res, {
        ...
        callbacks: {
          session({ session, token }) {
            // Return a cookie value as part of the session
            // This is read when `req.query.nextauth.includes("session") && req.method === "GET"`
            session.someCookie = someCookie
            return session
          }
        }
      })
    }

```

실용적인 예로, 기본 로그인 페이지에서는 특정 provider를 표시하지 않되 해당 provider로 로그인은 가능하게 만들 수 있습니다. (아이디어 출처: [this discussion](https://github.com/nextauthjs/next-auth/discussions/3133)):

/pages/api/auth/[...nextauth].ts

```
    import NextAuth from "next-auth"
    import CredentialsProvider from "next-auth/providers/credentials"
    import GoogleProvider from "next-auth/providers/google"

    export default async function auth(req, res) {
      const providers = [
        CredentialsProvider(...),
        GoogleProvider(...),
      ]

      const isDefaultSigninPage = req.method === "GET" && req.query.nextauth.includes("signin")

      // Will hide the `GoogleProvider` when you visit `/api/auth/signin`
      if (isDefaultSigninPage) providers.pop()

      return await NextAuth(req, res, {
        providers,
        ...
      })
    }

```

사용 가능한 모든 action과 지원되는 메서드에 대한 자세한 내용은 [REST API documentation](https://next-auth.js.org/getting-started/rest-api) 또는 [the source code](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/index.ts)의 해당 부분을 확인하세요.

이 방식으로 `NextAuth`를 초기화하는 것은 매우 강력하지만, 신중하게 제한적으로 사용해야 합니다.

위험

`NextAuth`가 동작하는 데 필수적인 요청의 일부(예: [default cookies](https://next-auth.js.org/configuration/options#cookies))를 변경하면 예상치 못한 결과가 발생할 수 있으며, 잘못 변경할 경우 보안 취약점이 생길 가능성이 있습니다. 결과를 이해한 경우에만 변경하세요.
