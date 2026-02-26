---
title: "Next.js"
description: "를 여기저기 전달하지 않아도 되도록 헬퍼 함수를 만들 수 있습니다:"
---

Source URL: https://next-auth.js.org/configuration/nextjs

버전: v4

# Next.js

## `getServerSession`[​](https://next-auth.js.org/configuration/nextjs#getserversession "Direct link to heading")

팁

`authOptions`를 여기저기 전달하지 않아도 되도록 헬퍼 함수를 만들 수 있습니다:

auth.ts

```
    import type {
      GetServerSidePropsContext,
      NextApiRequest,
      NextApiResponse,
    } from "next"
    import type { NextAuthOptions } from "next-auth"
    import { getServerSession } from "next-auth"

    // You'll need to import and pass this
    // to `NextAuth` in `app/api/auth/[...nextauth]/route.ts`
    export const config = {
      providers: [], // rest of your config
    } satisfies NextAuthOptions

    // Use it in server contexts
    export function auth(
      ...args:
        | [GetServerSidePropsContext["req"], GetServerSidePropsContext["res"]]
        | [NextApiRequest, NextApiResponse]
        | []
    ) {
      return getServerSession(...args, config)
    }

```

서버 사이드(예: Route Handlers, React Server Components, API routes, 또는 `getServerSideProps`)에서 호출할 때는 `session` 객체를 가져오기 위해 `getSession` 대신 이 함수를 사용하는 것을 권장합니다. 이 메서드는 특히 NextAuth.js를 데이터베이스와 함께 사용할 때 유용합니다. 서버 사이드에서 `getSession` 대신 이 메서드를 사용하면 API Route로의 추가 `fetch`를 피할 수 있어(이는 일반적으로 [Next.js에서 권장되지 않음](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props#getserversideprops-or-api-routes)) 응답 시간을 _대폭_ 줄일 수 있습니다. 또한 `getServerSession`은 쿠키 만료 시간을 올바르게 갱신하고, `callbacks.jwt` 또는 `callbacks.session`이 무언가를 변경한 경우 세션 내용도 업데이트합니다.

`getServerSession`에는 NextAuth.js를 초기화할 때 `NextAuth`에 전달하는 것과 동일한 객체를 전달해야 합니다. 이를 위해 다음과 같이 NextAuth.js 옵션을 export할 수 있습니다:

`[...nextauth].ts`에서:

```
    import NextAuth from "next-auth"
    import type { NextAuthOptions } from "next-auth"

    export const authOptions: NextAuthOptions = {
      // your configs
    }

    export default NextAuth(authOptions)

```

### `getServerSideProps`에서:[​](https://next-auth.js.org/configuration/nextjs#in-getserversideprops "Direct link to heading")

```
    import { authOptions } from "pages/api/auth/[...nextauth]"
    import { getServerSession } from "next-auth/next"

    export async function getServerSideProps(context) {
      const session = await getServerSession(context.req, context.res, authOptions)

      if (!session) {
        return {
          redirect: {
            destination: "/",
            permanent: false,
          },
        }
      }

      return {
        props: {
          session,
        },
      }
    }

```

### API Routes에서:[​](https://next-auth.js.org/configuration/nextjs#in-api-routes "Direct link to heading")

```
    import { authOptions } from "pages/api/auth/[...nextauth]"
    import { getServerSession } from "next-auth/next"

    export default async function handler(req, res) {
      const session = await getServerSession(req, res, authOptions)

      if (!session) {
        res.status(401).json({ message: "You must be logged in." })
        return
      }

      return res.json({
        message: "Success",
      })
    }

```

### App Router에서:[​](https://next-auth.js.org/configuration/nextjs#in-app-router "Direct link to heading")

Next.js의 서버 컴포넌트에서도 `getServerSession`을 사용할 수 있습니다:

```
    import { getServerSession } from "next-auth/next"
    import { authOptions } from "pages/api/auth/[...nextauth]"

    export default async function Page() {
      const session = await getServerSession(authOptions)
      return <pre>{JSON.stringify(session, null, 2)}</pre>
    }

```

정보

`useSession`은 사용자가 로그인했는지 여부와 관계없이(쿠키 존재 여부와 무관하게) `session` 객체를 반환하는 반면, `getServerSession`은 사용자가 로그인한 경우에만(인증 쿠키가 있는 경우에만) `session` 객체를 반환하고, 그렇지 않으면 `null`을 반환합니다.

주의

현재 기반이 되는 Next.js의 `cookies()` 메서드는 요청 쿠키에 대해 [읽기 전용 접근만 제공](https://beta.nextjs.org/docs/api-reference/cookies)합니다. 즉, Server Components에서 `session`의 `expires` 값이 제거됩니다. 또한 세션에는 하드 만료가 있어, 만료 후에는 사용자가 다시 로그인해야 합니다. (기본 만료 기간은 30일입니다.)

### 캐싱[​](https://next-auth.js.org/configuration/nextjs#caching "Direct link to heading")

이 함수를 사용하면 개인화된 데이터를 다루게 되므로, 이를 사용하는 페이지나 API를 [public cache](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)에 저장하면 안 됩니다. 예를 들어 [Vercel](https://vercel.com/docs/concepts/functions/serverless-functions/edge-caching) 같은 호스트는 이 함수가 설정하는 `set-cookie` 헤더 때문에 공개 캐싱을 암묵적으로 방지합니다.

## `unstable_getServerSession`[​](https://next-auth.js.org/configuration/nextjs#unstable_getserversession "Direct link to heading")

이 메서드의 이름은 `getServerSession`으로 변경되었습니다. 위 문서를 참고하세요.

## Middleware[​](https://next-auth.js.org/configuration/nextjs#middleware "Direct link to heading")

NextAuth.js와 함께 Next.js Middleware를 사용해 사이트를 보호할 수 있습니다.

Next.js 12에는 [Middleware](https://nextjs.org/docs/middleware)가 도입되었습니다. 이는 정적 페이지를 포함해 어떤 페이지에 접근하기 전에 로직을 실행하는 방법입니다. Vercel 같은 플랫폼에서는 Middleware가 [Edge](https://nextjs.org/docs/api-reference/edge-runtime)에서 실행됩니다.

아래 옵션들이 익숙해 보인다면, [이 옵션들](https://next-auth.js.org/configuration/options#options)의 부분집합이기 때문입니다. 공통 설정 객체로 추출해 재사용할 수 있습니다. 앞으로는 모든 것을 Middleware에서 실행할 수 있기를 기대합니다. ([Caveats](https://next-auth.js.org/configuration/nextjs#caveats) 참고)

`next-auth/middleware`에서 `withAuth` 미들웨어 함수를 default import 또는 named import로 가져올 수 있습니다:

### 사전 요구사항[​](https://next-auth.js.org/configuration/nextjs#prerequisites "Direct link to heading")

미들웨어에서도 NextAuth에서 사용하는 것과 동일한 secret을 설정해야 합니다. 가장 쉬운 방법은 [`NEXTAUTH_SECRET`](https://next-auth.js.org/configuration/options#nextauth_secret) 환경 변수를 설정하는 것입니다. 이 값은 [NextAuth config](https://next-auth.js.org/configuration/options#options)와 미들웨어 config 모두에서 사용됩니다.

또는 미들웨어 config의 [`secret`](https://next-auth.js.org/configuration/nextjs#secret) 옵션으로 secret을 제공할 수 있습니다.

`secret` 값을 이 `NEXTAUTH_SECRET` 환경 변수로 완전히 대체할 것을 **강력히 권장**합니다.

### 기본 사용법[​](https://next-auth.js.org/configuration/nextjs#basic-usage "Direct link to heading")

사이트 전체에 인증을 요구하려는 가장 단순한 사용 방식은 다음과 같은 `middleware.js` 파일을 추가하는 것입니다:

```
    export { default } from "next-auth/middleware"

```

이것으로 끝입니다! 이제 애플리케이션이 보호됩니다. 🎉

특정 페이지만 보호하고 싶다면, `matcher`를 포함한 `config` 객체를 export하세요:

```
    export { default } from "next-auth/middleware"

    export const config = { matcher: ["/dashboard"] }

```

이제 모든 페이지에는 계속 접근할 수 있지만, `/dashboard`에만 인증이 필요합니다.

사용자가 로그인하지 않은 경우 기본 동작은 로그인 페이지로 리디렉션하는 것입니다.

---

### `callbacks`[​](https://next-auth.js.org/configuration/nextjs#callbacks "Direct link to heading")

- **필수:** 아니요

#### 설명[​](https://next-auth.js.org/configuration/nextjs#description "Direct link to heading")

콜백은 어떤 동작이 수행될 때 무엇이 일어날지 제어하는 데 사용할 수 있는 비동기 함수입니다.

#### 예시 (기본값)[​](https://next-auth.js.org/configuration/nextjs#example-default-value "Direct link to heading")

```
     callbacks: {
       authorized({ req , token }) {
         if(token) return true // If there is a token, the user is authenticated
       }
     }

```

---

### `pages`[​](https://next-auth.js.org/configuration/nextjs#pages "Direct link to heading")

- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/nextjs#description-1 "Direct link to heading")

커스텀 로그인 페이지와 에러 페이지를 만들고 싶다면 사용할 URL을 지정합니다. 지정된 페이지는 해당 내장 페이지를 덮어씁니다.

정보

`pages` 설정은 `[...nextauth].ts`의 설정과 동일해야 합니다. 그래야 `next-auth` Middleware가 커스텀 페이지를 인지하여, 인증되지 않은 조건에서 자기 자신으로 리디렉션되는 일을 방지할 수 있습니다.

#### 예시 (기본값)[​](https://next-auth.js.org/configuration/nextjs#example-default-value-1 "Direct link to heading")

```
    import { withAuth } from "next-auth/middleware"

    export default withAuth({
      // Matches the pages config in `[...nextauth]`
      pages: {
        signIn: "/login",
        error: "/error",
      },
    })

```

자세한 내용은 [pages option](https://next-auth.js.org/configuration/pages) 문서를 참고하세요.

---

### `secret`[​](https://next-auth.js.org/configuration/nextjs#secret "Direct link to heading")

- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/nextjs#description-2 "Direct link to heading")

동일한 `secret`이 [NextAuth.js config](https://next-auth.js.org/configuration/options#options)에서 사용됩니다.

#### 예시 (기본값)[​](https://next-auth.js.org/configuration/nextjs#example-default-value-2 "Direct link to heading")

```
    secret: process.env.NEXTAUTH_SECRET

```

---

### 고급 사용법[​](https://next-auth.js.org/configuration/nextjs#advanced-usage "Direct link to heading")

NextAuth.js Middleware는 매우 유연하며, 사용하는 방법이 여러 가지입니다.

참고

옵션을 정의하지 않으면 NextAuth.js는 생략된 옵션에 대해 기본값을 사용합니다.

#### 미들웨어 래핑[​](https://next-auth.js.org/configuration/nextjs#wrap-middleware "Direct link to heading")

middleware.ts

```
    import { withAuth } from "next-auth/middleware"

    export default withAuth(
      // `withAuth` augments your `Request` with the user's token.
      function middleware(req) {
        console.log(req.nextauth.token)
      },
      {
        callbacks: {
          authorized: ({ token }) => token?.role === "admin",
        },
      },
    )

    export const config = { matcher: ["/admin"] }

```

`authorized` 콜백이 `true`를 반환할 때만 `middleware` 함수가 호출됩니다.

---

#### 사용자 정의 JWT decode 메서드[​](https://next-auth.js.org/configuration/nextjs#custom-jwt-decode-method "Direct link to heading")

`[...nextauth].ts`에서 사용자 정의 jwt decode 메서드를 설정했다면, 사용자 정의 서명 JWT를 올바르게 읽기 위해 `withAuth`에도 동일한 `decode` 메서드를 전달해야 합니다. 일관성을 위해 encode/decode 로직을 별도 함수로 분리하는 것이 좋습니다.

/api/auth/[...nextauth].ts

```
    import type { NextAuthOptions } from "next-auth"
    import NextAuth from "next-auth"
    import jwt from "jsonwebtoken"

    export const authOptions: NextAuthOptions = {
      providers: [...],
      jwt: {
        async encode({ secret, token }) {
          return jwt.sign(token, secret)
        },
        async decode({ secret, token }) {
          return jwt.verify(token, secret)
        },
      },
    }

    export default NextAuth(authOptions)

```

그리고:

middleware.ts

```
    import withAuth from "next-auth/middleware"
    import { authOptions } from "pages/api/auth/[...nextauth]"

    export default withAuth({
      jwt: { decode: authOptions.jwt?.decode },
      callbacks: {
        authorized: ({ token }) => !!token,
      },
    })

```

### 주의사항[​](https://next-auth.js.org/configuration/nextjs#caveats "Direct link to heading")

- 현재는 세션 검증만 지원합니다. 로그인 코드의 일부가 Node.js 환경에서 실행되어야 하기 때문입니다. 앞으로는 NextAuth.js가 [Edge](https://nextjs.org/docs/api-reference/edge-runtime)에서 완전히 실행될 수 있도록 하는 것이 목표입니다.
- `"jwt"` [session strategy](https://next-auth.js.org/configuration/options#session)만 지원합니다. 빠른 경험을 보장할 수 있을 만큼 Edge의 데이터베이스가 성숙해질 때까지 기다려야 합니다. (Edge 호환 데이터베이스를 알고 있다면 새로운 [Adapter](https://authjs.dev/guides/creating-a-database-adapter)를 제안해 주세요)
