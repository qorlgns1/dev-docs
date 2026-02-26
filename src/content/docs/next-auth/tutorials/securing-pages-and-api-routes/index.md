---
title: "페이지 및 API 라우트 보안"
description: "NextAuth.js를 사용하면 클라이언트 사이드 렌더링 페이지, 서버 사이드 렌더링 페이지, 그리고 API 라우트를 쉽게 보호할 수 있습니다."
---

원문 URL: https://next-auth.js.org/tutorials/securing-pages-and-api-routes

# 페이지 및 API 라우트 보안 | NextAuth.js

버전: v4

NextAuth.js를 사용하면 클라이언트 사이드 렌더링 페이지, 서버 사이드 렌더링 페이지, 그리고 API 라우트를 쉽게 보호할 수 있습니다.

_아래에 소개된 접근 방식의 동작 예시는 [example project](https://github.com/nextauthjs/next-auth-example/)에서 확인할 수 있습니다._

팁

`getSession()`과 `getToken()` 메서드는 세션이 유효하면 `object`를, 세션이 유효하지 않거나 만료되었으면 `null`을 반환합니다.

## 페이지 보호[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#securing-pages "제목으로 바로 가는 링크")

### 클라이언트 사이드[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#client-side "제목으로 바로 가는 링크")

페이지의 데이터를 보호된 API 라우트 호출로 가져오는 경우, 즉 세션에 접근하기 위해 `getSession()` 또는 `getToken()`을 사용하는 라우트인 경우, `useSession` React Hook을 사용해 페이지를 보호할 수 있습니다.

pages/client-side-example.js

```
    import { useSession, getSession } from "next-auth/react"

    export default function Page() {
      const { data: session, status } = useSession()

      if (status === "loading") {
        return <p>Loading...</p>
      }

      if (status === "unauthenticated") {
        return <p>Access Denied</p>
      }

      return (
        <>
          <h1>Protected Page</h1>
          <p>You can view this page because you are signed in.</p>
        </>
      )
    }

```

### Next.js (Middleware)[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#nextjs-middleware "제목으로 바로 가는 링크")

NextAuth.js 4.2.0과 Next.js 12부터는 middleware 패턴을 통해 페이지를 더 쉽게 보호할 수 있습니다. 모든 페이지를 보호하려면 루트 또는 src 디렉터리( `pages`와 같은 레벨)에 `middleware.js` 파일을 만들고 다음과 같이 작성하면 됩니다.

/middleware.js

```
    export { default } from "next-auth/middleware"

```

특정 페이지만 보호하려면 `matcher`를 포함한 `config` 객체를 export하세요.

```
    export { default } from "next-auth/middleware"

    export const config = { matcher: ["/dashboard(.*)"] }

```

현재 `withAuth` middleware는 [session strategy](https://next-auth.js.org/configuration/options#session)로 `"jwt"`만 지원합니다.

자세한 내용은 [여기](https://next-auth.js.org/configuration/nextjs#middleware)에서 확인할 수 있습니다.

팁

중첩된 모든 `dashboard` 라우트(예: `/dashboard/settings`, `/dashboard/profile`)를 포함하려면 `config`에 `matcher: "/dashboard/:path*"`를 전달하면 됩니다.

다른 패턴은 [Next.js Middleware 문서](https://nextjs.org/docs/advanced-features/middleware#matcher)를 확인하세요.

### 서버 사이드[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#server-side "제목으로 바로 가는 링크")

`getServerSession` 메서드를 사용하면 서버 사이드 렌더링 페이지를 보호할 수 있습니다. 이 방식은 기존 `getSession()` 메서드와 달리, 자체 데이터를 확인하기 위한 추가 인터넷 fetch를 수행하지 않으므로 성능이 크게 향상됩니다.

보호하려는 모든 서버 렌더링 페이지마다 이를 추가해야 합니다. `getServerSession`은 대체 대상인 `getSession`과 인자가 약간 다르다는 점에 유의하세요.

pages/server-side-example.js

```
    import { getServerSession } from "next-auth/next"
    import { authOptions } from "./api/auth/[...nextauth]"
    import { useSession } from "next-auth/react"

    export default function Page() {
      const { data: session } = useSession()

      if (typeof window === "undefined") return null

      if (session) {
        return (
          <>
            <h1>Protected Page</h1>
            <p>You can view this page because you are signed in.</p>
          </>
        )
      }
      return <p>Access Denied</p>
    }

    export async function getServerSideProps(context) {
      return {
        props: {
          session: await getServerSession(
            context.req,
            context.res,
            authOptions
          ),
        },
      }
    }

```

팁

`_app.js`에서 `session` prop을 제공하면 `useSession`은 로딩 상태를 표시하지 않습니다. 이미 세션을 사용할 수 있기 때문입니다. 이 방식으로 더 매끄러운 사용자 경험을 제공할 수 있습니다.

pages/\_app.js

```
    import { SessionProvider } from "next-auth/react"

    export default function App({
      Component,
      pageProps: { session, ...pageProps },
    }) {
      return (
      )
    }

```

## API 라우트 보호[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#securing-api-routes "제목으로 바로 가는 링크")

### getServerSession() 사용[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#using-getserversession "제목으로 바로 가는 링크")

`getServerSession()` 메서드를 사용해 API 라우트를 보호할 수 있습니다.

pages/api/get-session-example.js

```
    import { getServerSession } from "next-auth/next"
    import { authOptions } from "./auth/[...nextauth]"

    export default async (req, res) => {
      const session = await getServerSession(req, res, authOptions)
      if (session) {
        // Signed in
        console.log("Session", JSON.stringify(session, null, 2))
      } else {
        // Not Signed in
        res.status(401)
      }
      res.end()
    }

```

### getToken() 사용[​](https://next-auth.js.org/tutorials/securing-pages-and-api-routes#using-gettoken "제목으로 바로 가는 링크")

JSON Web Token을 사용 중이라면 `getToken()` helper를 사용해 JWT 복호화/검증을 직접 처리하지 않고도 JWT 내용을 가져올 수 있습니다. 이 메서드는 서버 사이드에서만 사용할 수 있습니다.

pages/api/get-token-example.js

```
    // This is an example of how to read a JSON Web Token from an API route
    import { getToken } from "next-auth/jwt"

    export default async (req, res) => {
      // If you don't have NEXTAUTH_SECRET set, you will have to pass your secret as `secret` to `getToken`
      const token = await getToken({ req })
      if (token) {
        // Signed in
        console.log("JSON Web Token", JSON.stringify(token, null, 2))
      } else {
        // Not Signed in
        res.status(401)
      }
      res.end()
    }

```

팁

`NEXTAUTH_URL` 환경 변수를 설정하고, 애플리케이션이 JWT cookie를 읽을 수 있다면(예: 동일한 도메인) 어떤 애플리케이션에서든 `getToken()` helper function을 사용할 수 있습니다.

참고

`pages/api/auth/[...nextauth].js`에 지정한 `secret`과 동일한 값을 `getToken`에 전달하세요.

자세한 내용은 [JWT option 문서](https://next-auth.js.org/configuration/options#jwt)를 참고하세요.
