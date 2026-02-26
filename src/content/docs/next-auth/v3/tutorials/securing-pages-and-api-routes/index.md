---
title: "페이지 및 API 라우트 보호"
description: "NextAuth.js를 사용하면 클라이언트 사이드 렌더링 페이지, 서버 사이드 렌더링 페이지, 그리고 API 라우트를 쉽게 보호할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes

# 페이지 및 API 라우트 보호 | NextAuth.js

버전: v3

NextAuth.js를 사용하면 클라이언트 사이드 렌더링 페이지, 서버 사이드 렌더링 페이지, 그리고 API 라우트를 쉽게 보호할 수 있습니다.

_아래에 소개된 접근 방식의 동작 예제는 [example project](https://github.com/nextauthjs/next-auth-example/)에서 확인할 수 있습니다._

팁

메서드 `getSession()` 과 `getToken()` 은 세션이 유효하면 `object` 를, 세션이 유효하지 않거나 만료되었으면 `null` 을 반환합니다.

## 페이지 보호[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#securing-pages "헤딩으로 직접 연결")

### 클라이언트 사이드[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#client-side "헤딩으로 직접 연결")

페이지의 데이터를 보호된 API 라우트 호출로 가져오는 경우(즉, 세션에 접근하기 위해 `getSession()` 또는 `getToken()` 을 사용하는 라우트), `useSession` React Hook을 사용해 페이지를 보호할 수 있습니다.

pages/client-side-example.js

```
    import { useSession, getSession } from "next-auth/client"

    export default function Page() {
      const [session, loading] = useSession()

      if (loading) return null

      if (!loading && !session) return <p>Access Denied</p>

      return (
        <>
          <h1>Protected Page</h1>
          <p>You can view this page because you are signed in.</p>
        </>
      )
    }

```

### 서버 사이드[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#server-side "헤딩으로 직접 연결")

`getSession()` 메서드를 사용해 서버 사이드 렌더링 페이지를 보호할 수 있습니다.

pages/server-side-example.js

```
    import { useSession, getSession } from "next-auth/client"

    export default function Page() {
      const [session, loading] = useSession()

      if (typeof window !== "undefined" && loading) return null

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
      const session = await getSession(context)
      return {
        props: { session },
      }
    }

```

팁

이 예제는 `_app.js` 를 구성하여 `session` prop을 전달하고, 페이지 로드 시점에 `useSession` 에서 즉시 사용할 수 있다고 가정합니다.

pages/\_app.js

```
    import { Provider } from "next-auth/client"

    export default ({ Component, pageProps }) => {
      return (
      )
    }

```

## API 라우트 보호[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#securing-api-routes "헤딩으로 직접 연결")

### getSession() 사용[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#using-getsession "헤딩으로 직접 연결")

`getSession()` 메서드를 사용해 API 라우트를 보호할 수 있습니다.

pages/api/get-session-example.js

```
    import { getSession } from "next-auth/client"

    export default async (req, res) => {
      const session = await getSession({ req })
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

### getToken() 사용[​](https://next-auth.js.org/v3/tutorials/securing-pages-and-api-routes#using-gettoken "헤딩으로 직접 연결")

JSON Web Token을 사용하는 경우, JWT 복호화/검증을 직접 처리하지 않고도 `getToken()` 헬퍼를 사용해 JWT 내용을 확인할 수 있습니다. 이 메서드는 서버 사이드에서만 사용할 수 있습니다.

pages/api/get-token-example.js

```
    // This is an example of how to read a JSON Web Token from an API route
    import jwt from "next-auth/jwt"

    const secret = process.env.SECRET

    export default async (req, res) => {
      const token = await jwt.getToken({ req, secret })
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

`NEXTAUTH_URL` 환경 변수를 설정하고 애플리케이션이 JWT 쿠키를 읽을 수 있다면(예: 동일한 도메인에 있는 경우), 어떤 애플리케이션에서든 `getToken()` 헬퍼 함수를 사용할 수 있습니다.

참고

`getToken` 에 전달하는 `secret` 값은 `pages/api/auth/[...nextauth].js` 에 지정한 값과 동일해야 합니다.

자세한 내용은 [JWT 옵션 문서](https://next-auth.js.org/configuration/options#jwt)를 참고하세요.
