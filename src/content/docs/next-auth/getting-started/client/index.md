---
title: "클라이언트 API"
description: "NextAuth.js 클라이언트 라이브러리를 사용하면 React 애플리케이션에서 세션과 쉽게 상호작용할 수 있습니다."
---

Source URL: https://next-auth.js.org/getting-started/client

# 클라이언트 API | NextAuth.js

버전: v4

NextAuth.js 클라이언트 라이브러리를 사용하면 React 애플리케이션에서 세션과 쉽게 상호작용할 수 있습니다.

#### 세션 객체 예시[​](https://next-auth.js.org/getting-started/client#example-session-object "제목으로 직접 링크")

```
    {
      user: {
        name: string
        email: string
        image: string
      },
      expires: Date // This is the expiry of the session, not any of the tokens within the session
    }

```

tip

클라이언트에 반환되는 세션 데이터에는 Session Token이나 OAuth 토큰 같은 민감한 정보가 포함되지 않습니다. 표시 목적을 위해 로그인한 사용자 정보를 페이지에 보여주는 데 필요한 최소한의 페이로드(예: name, email, image)만 포함됩니다.

세션 객체에 추가 데이터를 반환해야 한다면 [session callback](https://next-auth.js.org/configuration/callbacks#session-callback)을 사용해 클라이언트에 반환되는 세션 객체를 커스터마이즈할 수 있습니다.

note

`expires` 값은 회전(rotated)됩니다. 즉, [REST API](https://next-auth.js.org/getting-started/rest-api)에서 세션을 조회할 때마다 세션 만료를 방지하기 위해 이 값도 함께 업데이트됩니다.

---

## useSession()[​](https://next-auth.js.org/getting-started/client#usesession "제목으로 직접 링크")

- 클라이언트 사이드: **Yes**
- 서버 사이드: No

NextAuth.js 클라이언트의 `useSession()` React Hook은 사용자가 로그인했는지 확인하는 가장 쉬운 방법입니다.

`pages/_app.js`에 [`<SessionProvider>`](https://next-auth.js.org/getting-started/client#sessionprovider)가 추가되어 있는지 확인하세요.

#### 예시[​](https://next-auth.js.org/getting-started/client#example "제목으로 직접 링크")

```
    import { useSession } from "next-auth/react"

    export default function Component() {
      const { data: session, status } = useSession()

      if (status === "authenticated") {
        return <p>Signed in as {session.user.email}</p>
      }

      return <a href="/api/auth/signin">Sign in</a>
    }

```

`useSession()`은 `data`와 `status` 두 값을 포함하는 객체를 반환합니다:

- **`data`** : 세 가지 값 중 하나입니다: [`Session`](https://github.com/nextauthjs/next-auth/blob/8ff4b260143458c5d8a16b80b11d1b93baa0690f/types/index.d.ts#L437-L444) / `undefined` / `null`.
  - 세션을 아직 가져오지 않은 경우 `data`는 `undefined`입니다.
  - 세션 조회에 실패한 경우 `data`는 `null`입니다.
  - 성공한 경우 `data`는 [`Session`](https://github.com/nextauthjs/next-auth/blob/8ff4b260143458c5d8a16b80b11d1b93baa0690f/types/index.d.ts#L437-L444)입니다.
- **`status`** : 가능한 세 가지 세션 상태에 매핑되는 enum입니다: `"loading" | "authenticated" | "unauthenticated"`

### 세션 필수화[​](https://next-auth.js.org/getting-started/client#require-session "제목으로 직접 링크")

Next.js가 `getServerSideProps`와 `getInitialProps`를 처리하는 방식 때문에, 보호된 페이지를 로드할 때마다 세션이 유효한지 확인하고 요청된 페이지를 생성하기 위해 서버 사이드 요청(SSR)을 해야 합니다. 이는 서버 부하를 증가시키며, 클라이언트에서 요청하는 방식이 괜찮다면 대안이 있습니다. `useSession`을 사용해 항상 유효한 세션을 갖도록 보장할 수 있습니다. 초기 로딩 상태 이후 세션이 없으면, 이에 대응하는 적절한 동작을 정의할 수 있습니다.

기본 동작은 사용자를 로그인 페이지로 리디렉션하는 것이며, 로그인에 성공하면 시작했던 페이지로 다시 돌아갑니다. 다른 동작을 원한다면 `onUnauthenticated()` 콜백을 정의할 수도 있습니다:

#### 예시[​](https://next-auth.js.org/getting-started/client#example-1 "제목으로 직접 링크")

pages/protected.jsx

```
    import { useSession } from "next-auth/react"

    export default function Admin() {
      const { status } = useSession({
        required: true,
        onUnauthenticated() {
          // The user is not authenticated, handle it here.
        },
      })

      if (status === "loading") {
        return "Loading or not authenticated..."
      }

      return "User is logged in"
    }

```

### 커스텀 클라이언트 세션 처리[​](https://next-auth.js.org/getting-started/client#custom-client-session-handling "제목으로 직접 링크")

Next.js가 `getServerSideProps` / `getInitialProps`를 처리하는 방식 때문에, 보호된 페이지를 로드할 때마다 세션이 유효한지 확인하고 요청된 페이지를 생성하기 위해 서버 사이드 요청을 해야 합니다. 이 대안은 최초 확인 시 로딩 상태를 보여주고, 이후 모든 페이지 전환은 서버 확인 및 페이지 재생성 없이 클라이언트 사이드에서 처리되도록 합니다.

pages/admin.jsx

```
    export default function AdminDashboard() {
      const { data: session } = useSession()
      // session is always non-null inside this page, all the way down the React tree.
      return "Some super secret dashboard"
    }

    AdminDashboard.auth = true

```

pages/\_app.jsx

```
    export default function App({
      Component,
      pageProps: { session, ...pageProps },
    }) {
      return (
          {Component.auth ? (
          ) : (
          )}
      )
    }

    function Auth({ children }) {
      // if `{ required: true }` is supplied, `status` can only be "loading" or "authenticated"
      const { status } = useSession({ required: true })

      if (status === "loading") {
        return <div>Loading...</div>
      }

      return children
    }

```

페이지에서 역할 기반 인증을 위한 옵션 객체 같은 것을 지원하도록 쉽게 확장/수정할 수 있습니다. 예시:

pages/admin.jsx

```
    AdminDashboard.auth = {
      role: "admin",
      loading: <AdminLoadingSkeleton />,
      unauthorized: "/login-with-different-user", // redirect to this url
    }

```

`_app`이 작성된 방식 덕분에, 인증이 필요하지 않은 페이지에서는 `/api/auth/session` 엔드포인트에 불필요하게 요청하지 않습니다.

자세한 내용은 다음 [GitHub Issue](https://github.com/nextauthjs/next-auth/issues/1210)에서 확인할 수 있습니다.

### 세션 업데이트[​](https://next-auth.js.org/getting-started/client#updating-the-session "제목으로 직접 링크")

`useSession()` 훅은 `update(data?: any): Promise<Session | null>` 메서드를 제공하며, 페이지를 다시 로드하지 않고 세션을 업데이트할 수 있습니다.

선택적으로 첫 번째 인수로 임의 객체를 전달할 수 있으며, 이 객체는 서버에서 세션 객체와 병합할 수 있도록 접근 가능합니다.

아무 인수도 전달하지 않으면 세션은 서버에서 다시 로드됩니다. (DB 업데이트 같은 서버 사이드 변경 후 세션을 갱신하려는 경우 유용합니다.)

caution

데이터 객체는 클라이언트에서 오므로, 저장 전에 서버에서 검증해야 합니다.

#### 예시[​](https://next-auth.js.org/getting-started/client#example-2 "제목으로 직접 링크")

pages/profile.tsx

```
    import { useSession } from "next-auth/react"

    export default function Page() {
      const { data: session, status, update } = useSession()

      if (status === "authenticated") {
        return (
          <>
            <p>Signed in as {session.user.name}</p>

            {/* Update the value by sending it to the backend. */}
            <button onClick={() => update({ name: "John Doe" })}>Edit name</button>
            {/*
             * Only trigger a session update, assuming you already updated the value server-side.
             * All `useSession().data` references will be updated.
             */}
            <button onClick={() => update()}>Edit name</button>
          </>
        )
      }

      return <a href="/api/auth/signin">Sign in</a>
    }

```

`strategy: "jwt"`를 사용한다고 가정하면, `update()` 메서드는 `trigger: "update"` 옵션과 함께 `jwt` 콜백을 트리거합니다. 이를 사용해 서버에서 세션 객체를 업데이트할 수 있습니다.

pages/api/auth/[...nextauth].ts

```
    ...
    export default NextAuth({
      ...
      callbacks: {
        // Using the `...rest` parameter to be able to narrow down the type based on `trigger`
        jwt({ token, trigger, session }) {
          if (trigger === "update" && session?.name) {
            // Note, that `session` can be any arbitrary object, remember to validate it!
            token.name = session.name
          }
          return token
        }
      }
    })

```

`strategy: "database"`를 사용한다고 가정하면, `update()` 메서드는 `trigger: "update"` 옵션과 함께 `session` 콜백을 트리거합니다. 이를 사용해 서버에서 세션 객체를 업데이트할 수 있습니다.

pages/api/auth/[...nextauth].ts

```
    ...
    const adapter = PrismaAdapter(prisma)
    export default NextAuth({
      ...
      adapter,
      callbacks: {
        // Using the `...rest` parameter to be able to narrow down the type based on `trigger`
        async session({ session, trigger, newSession }) {
          // Note, that `rest.session` can be any arbitrary object, remember to validate it!
          if (trigger === "update" && newSession?.name) {
            // You can update the session in the database if it's not already updated.
            // await adapter.updateUser(session.user.id, { name: newSession.name })

            // Make sure the updated value is reflected on the client
            session.name = newSession.name
          }
          return session
        }
      }
    })

```

### 세션 다시 가져오기[​](https://next-auth.js.org/getting-started/client#refetching-the-session "제목으로 직접 링크")

[`SessionProvider#refetchInterval`](https://next-auth.js.org/getting-started/client#refetch-interval) 및 [`SessionProvider#refetchOnWindowFocus`](https://next-auth.js.org/getting-started/client#refetch-on-window-focus)는 `update()` 메서드로도 대체할 수 있습니다.

note

`update()` 메서드는 `refetchInterval` 및 `refetchOnWindowFocus` 옵션과 달리 탭 간 동기화를 하지 않습니다.

pages/profile.tsx

```
    import { useEffect } from "react"
    import { useSession } from "next-auth/react"

    export default function Page() {
      const { data: session, status, update } = useSession()

      // Polling the session every 1 hour
      useEffect(() => {
        // TIP: You can also use `navigator.onLine` and some extra event handlers
        // to check if the user is online and only update the session if they are.
        // https://developer.mozilla.org/en-US/docs/Web/API/Navigator/onLine
        const interval = setInterval(() => update(), 1000 * 60 * 60)
        return () => clearInterval(interval)
      }, [update])

      // Listen for when the page is visible, if the user switches tabs
      // and makes our tab visible again, re-fetch the session
      useEffect(() => {
        const visibilityHandler = () =>
          document.visibilityState === "visible" && update()
        window.addEventListener("visibilitychange", visibilityHandler, false)
        return () =>
          window.removeEventListener("visibilitychange", visibilityHandler, false)
      }, [update])

      return <pre>{JSON.stringify(session, null, 2)}</pre>
    }

```

---

## getSession()[​](https://next-auth.js.org/getting-started/client#getsession "제목으로 직접 링크")

- 클라이언트 사이드: **Yes**
- 서버 사이드: **No** (참고: [`getServerSession()`](https://next-auth.js.org/configuration/nextjs#getserversession)

NextAuth.js는 현재 활성 세션을 반환하는 `getSession()` 헬퍼를 제공하며, 이는 **클라이언트 사이드에서만** 호출해야 합니다.

서버 사이드에서도 **여전히 사용 가능** 하지만, 앞으로는 `getServerSession` 사용을 권장합니다. 그 이유는 서버 사이드에서 불필요한 추가 `fetch` 호출을 피하기 위해서입니다. 자세한 내용은 [이 이슈](https://github.com/nextauthjs/next-auth/issues/1535)를 확인하세요.

이 헬퍼는 React 컨텍스트 밖에서 세션을 읽고 싶을 때 유용합니다.

호출 시 `getSession()`은 `/api/auth/session`으로 요청을 보내고, [session object](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/core/types.ts#L407-L425)를 담은 promise를 반환합니다. 세션이 없으면 `null`을 반환합니다.

```
    async function myFunction() {
      const session = await getSession()
      /* ... */
    }

```

서버 사이드 호출에서 `getServerSession()`을 사용해 세션을 가져오는 방법은 [페이지 및 API 라우트 보호](https://next-auth.js.org/tutorials/securing-pages-and-api-routes) 튜토리얼을 참고하세요.

---

## getCsrfToken()[​](https://next-auth.js.org/getting-started/client#getcsrftoken "제목으로 직접 링크")

- 클라이언트 사이드: **Yes**
- 서버 사이드: **Yes**

`getCsrfToken()` 메서드는 POST 요청(예: 로그인/로그아웃)에 필요한 현재 Cross Site Request Forgery Token(CSRF Token)을 반환합니다.

내장 `signIn()` 및 `signOut()` 메서드를 사용하지 않는 경우에만 이 메서드가 필요할 가능성이 큽니다.

#### 클라이언트 사이드 예시[​](https://next-auth.js.org/getting-started/client#client-side-example "제목으로 직접 링크")

```
    async function myFunction() {
      const csrfToken = await getCsrfToken()
      /* ... */
    }

```

#### 서버 사이드 예시[​](https://next-auth.js.org/getting-started/client#server-side-example "제목으로 직접 링크")

```
    import { getCsrfToken } from "next-auth/react"

    export default async (req, res) => {
      const csrfToken = await getCsrfToken({ req })
      /* ... */
      res.end()
    }

```

---

## getProviders()[​](https://next-auth.js.org/getting-started/client#getproviders "제목으로 직접 링크")

- 클라이언트 사이드: **Yes**
- 서버 사이드: **Yes**

`getProviders()` 메서드는 현재 로그인에 설정된 provider 목록을 반환합니다.

`/api/auth/providers`를 호출하여 현재 구성된 인증 provider 목록을 반환합니다.

동적 커스텀 로그인 페이지를 만들 때 유용할 수 있습니다.

---

#### API 라우트[​](https://next-auth.js.org/getting-started/client#api-route "제목으로 직접 링크")

pages/api/example.js

```
    import { getProviders } from "next-auth/react"

    export default async (req, res) => {
      const providers = await getProviders()
      console.log("Providers", providers)
      res.end()
    }

```

note

`getCsrfToken()`과 달리, 서버 사이드에서 `getProviders()`를 호출할 때는 클라이언트 사이드와 마찬가지로 아무것도 전달할 필요가 없습니다.

---

## signIn()[​](https://next-auth.js.org/getting-started/client#signin "제목으로 직접 링크")

- 클라이언트 사이드: **Yes**
- 서버 사이드: No

`signIn()` 메서드를 사용하면 로그인 흐름을 완료한 뒤 사용자가 시작했던 페이지로 돌아가도록 보장됩니다. 또한 이메일로 로그인할 때 CSRF Token도 자동으로 처리해 줍니다.

`signIn()` 메서드는 아래와 같이 클라이언트에서 다양한 방식으로 호출할 수 있습니다.

### 클릭 시 로그인 페이지로 리디렉션[​](https://next-auth.js.org/getting-started/client#redirects-to-sign-in-page-when-clicked "제목으로 직접 링크")

```
    import { signIn } from "next-auth/react"

    export default () => <button onClick={() => signIn()}>Sign in</button>

```

### 클릭 시 OAuth 로그인 흐름 시작[​](https://next-auth.js.org/getting-started/client#starts-oauth-sign-in-flow-when-clicked "제목으로 직접 링크")

기본적으로 인수 없이 `signIn()` 메서드를 호출하면 NextAuth.js 로그인 페이지로 리디렉션됩니다. 이를 건너뛰고 즉시 provider 페이지로 리디렉션하려면 provider의 `id`를 인수로 전달해 `signIn()`을 호출하세요.

예를 들어 Google로 로그인하려면:

```
    import { signIn } from "next-auth/react"

    export default () => (
      <button onClick={() => signIn("google")}>Sign in with Google</button>
    )

```

### 클릭 시 Email 로그인 흐름 시작[​](https://next-auth.js.org/getting-started/client#starts-email-sign-in-flow-when-clicked "제목으로 직접 링크")

email 흐름과 함께 사용할 때는 대상 `email`을 옵션으로 전달하세요.

```
    import { signIn } from "next-auth/react"

    export default ({ email }) => (
      <button onClick={() => signIn("email", { email })}>Sign in with Email</button>
    )

```

### `callbackUrl` 지정[​](https://next-auth.js.org/getting-started/client#specifying-a-callbackurl "제목으로 직접 링크")

`callbackUrl`은 로그인 후 사용자를 리디렉션할 URL을 지정합니다. 기본값은 로그인이 시작된 페이지 URL입니다.

`signIn()`의 두 번째 인수로 지정하면 다른 `callbackUrl`을 설정할 수 있습니다. 이는 모든 provider에서 동작합니다.

예:

- `signIn(undefined, { callbackUrl: '/foo' })`
- `signIn('google', { callbackUrl: 'http://localhost:3000/bar' })`
- `signIn('email', { email, callbackUrl: 'http://localhost:3000/foo' })`

URL은 [redirect callback handler](https://next-auth.js.org/configuration/callbacks#redirect-callback)에서 유효하다고 판단되어야 합니다. 기본적으로 같은 호스트명의 절대 URL이거나 슬래시로 시작하는 상대 URL이어야 합니다. 일치하지 않으면 홈페이지로 리디렉션됩니다. 다른 URL을 허용하려면 직접 [redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 정의할 수 있습니다.

### `redirect: false` 옵션 사용[​](https://next-auth.js.org/getting-started/client#using-the-redirect-false-option "제목으로 직접 링크")

note

redirect 옵션은 `credentials` 및 `email` provider에서만 사용할 수 있습니다.

경우에 따라 같은 페이지에서 로그인 응답을 처리하고 기본 리디렉션을 비활성화하고 싶을 수 있습니다. 예를 들어 오류(사용자가 잘못된 자격 증명을 입력한 경우 등)가 발생했을 때 같은 페이지에서 오류를 처리하고 싶을 수 있습니다. 이를 위해 두 번째 파라미터 객체에 `redirect: false`를 전달할 수 있습니다.

예:

- `signIn('credentials', { redirect: false, password: 'password' })`
  - `signIn('email', { redirect: false, email: 'bill@fillmurray.com' })`

그다음 `signIn`은 아래와 같이 resolve되는 Promise를 반환합니다:

```
    {
      /**
       * Will be different error codes,
       * depending on the type of error.
       */
      error: string | undefined
      /**
       * HTTP status code,
       * hints the kind of error that happened.
       */
      status: number
      /**
       * `true` if the signin was successful
       */
      ok: boolean
      /**
       * `null` if there was an error,
       * otherwise the url the user
       * should have been redirected to.
       */
      url: string | null
    }

```

### 추가 매개변수[​](https://next-auth.js.org/getting-started/client#additional-parameters "Direct link to heading")

`signIn()`의 세 번째 인자를 통해 `/authorize` 엔드포인트에 추가 매개변수를 전달할 수도 있습니다.

아이디어는 [Authorization Request OIDC spec](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)을 참고하세요. (가능한 매개변수는 이것들만이 아니며, 모든 매개변수가 전달됩니다)

예:

- `signIn("identity-server4", null, { prompt: "login" })` _사용자에게 항상 재인증을 요청_
- `signIn("auth0", null, { login_hint: "info@example.com" })` _제공자에게 이메일 주소 힌트 전달_

note

이 매개변수들은 [`provider.authorizationParams`](https://next-auth.js.org/configuration/providers/oauth#options)를 통해서도 설정할 수 있습니다.

note

다음 매개변수들은 서버 측에서 항상 덮어씁니다: `redirect_uri`, `state`

---

## signOut()[​](https://next-auth.js.org/getting-started/client#signout "Direct link to heading")

- 클라이언트 사이드: **Yes**
- 서버 사이드: No

로그아웃하려면 `signOut()` 메서드를 사용하세요. 이렇게 하면 로그아웃 플로우가 완료된 뒤 사용자가 시작했던 페이지로 돌아가도록 보장됩니다. 또한 CSRF 토큰도 자동으로 처리합니다.

완료되면 브라우저에서 페이지를 다시 로드합니다.

```
    import { signOut } from "next-auth/react"

    export default () => <button onClick={() => signOut()}>Sign out</button>

```

### `callbackUrl` 지정하기[​](https://next-auth.js.org/getting-started/client#specifying-a-callbackurl-1 "Direct link to heading")

`signIn()` 함수와 마찬가지로, 옵션으로 전달하여 `callbackUrl` 매개변수를 지정할 수 있습니다.

예: `signOut({ callbackUrl: 'http://localhost:3000/foo' })`

이 URL은 [redirect callback handler](https://next-auth.js.org/configuration/callbacks#redirect-callback)에서 유효하다고 판단되어야 합니다. 기본적으로는 동일한 호스트 이름의 절대 URL이거나 슬래시로 시작하는 상대 URL이어야 합니다. 일치하지 않으면 홈페이지로 리디렉션됩니다. 다른 URL을 허용하려면 사용자 정의 [redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 정의할 수 있습니다.

### `redirect: false` 옵션 사용하기[​](https://next-auth.js.org/getting-started/client#using-the-redirect-false-option-1 "Direct link to heading")

`signOut`에 `redirect: false`를 전달하면 페이지가 다시 로드되지 않습니다. 세션은 삭제되고 `useSession` 훅에 알림이 전달되므로, 사용자 관련 표시는 자동으로 로그아웃 상태로 바뀝니다. 사용자 경험이 매우 좋아질 수 있습니다.

tip

다른 페이지로 리디렉션해야 하지만 페이지 리로드를 피하고 싶다면 다음을 시도할 수 있습니다: `const data = await signOut({redirect: false, callbackUrl: "/foo"})` 여기서 `data.url`은 검증된 URL이며, Next.js의 `useRouter().push(data.url)`를 사용해 깜빡임 없이 사용자를 리디렉션할 수 있습니다.

---

## SessionProvider[​](https://next-auth.js.org/getting-started/client#sessionprovider "Direct link to heading")

note

App Router를 사용 중이라면, 서버 컨텍스트에서는 대신 [`getServerSession`](https://next-auth.js.org/configuration/nextjs#getserversession)을 사용할 것을 권장합니다. (`SessionProvider`도 App Router에서 사용할 수 있으며, pages에서 마이그레이션 중이라면 더 쉬운 선택일 수 있습니다.)

제공된 `<SessionProvider>`를 사용하면 내부적으로 [React Context](https://react.dev/learn/passing-data-deeply-with-context)를 이용해 `useSession()` 인스턴스들이 컴포넌트 간에 세션 객체를 공유할 수 있습니다. 또한 탭/창 간 세션을 최신 상태로 유지하고 동기화합니다.

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

위 예시처럼 `<SessionProvider>`에 `session` page prop을 전달하면, 서버/클라이언트 사이드 렌더링을 모두 지원하는 페이지에서 세션을 두 번 확인하는 일을 피할 수 있습니다.

다만 이는 올바른 `pageProps`를 제공한 페이지에서만 동작합니다. 보통 다음과 같이 각 페이지별로 `getInitialProps` 또는 `getServerSideProps`에서 처리합니다.

pages/index.js

```
    import { getServerSession } from "next-auth/next"
    import { authOptions } from './api/auth/[...nextauth]'

    ...

    export async function getServerSideProps({ req, res }) {
      return {
        props: {
          session: await getServerSession(req, res, authOptions)
        }
      }
    }

```

모든 페이지를 보호해야 한다면 `_app`의 `getInitialProps`에서 처리할 수 있고, 그렇지 않다면 페이지별로 처리할 수 있습니다. 또는 각 인증 확인을 블로킹(SSR)으로 두는 대신, 아래 [alternative client session handling](https://next-auth.js.org/getting-started/client#custom-client-session-handling)에 설명된 방법으로 클라이언트 사이드 페이지별 인증 확인을 할 수도 있습니다.

### 옵션[​](https://next-auth.js.org/getting-started/client#options "Direct link to heading")

`refetchOnWindowFocus`가 `true`일 때, 세션 상태는 열려 있는 모든 탭/창에서 자동으로 동기화되며, 포커스를 얻거나 잃을 때 또는 상태가 바뀔 때(예: 사용자 로그인/로그아웃) 모두 업데이트됩니다.

세션 만료 시간이 30일(기본값) 이상이라면 Provider의 기본 옵션을 바꿀 필요가 거의 없습니다. 필요하다면 클라이언트 사이드 함수에서 [`getSession()`](https://next-auth.js.org/getting-started/client#getsession)을 호출해 모든 탭/창의 세션 객체 업데이트를 트리거할 수 있습니다.

하지만 세션 동작을 커스터마이즈해야 하거나 짧은 세션 만료 시간을 사용한다면, provider에 옵션을 전달해 `useSession()` 훅 동작을 사용자 정의할 수 있습니다.

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

note

**이 옵션들은 로그인되지 않은 클라이언트에는 영향을 주지 않습니다.**

각 탭/창은 로컬 세션 상태의 자체 복사본을 유지합니다. 세션은 localStorage나 sessionStorage 같은 공유 저장소에 저장되지 않습니다. 한 탭/창에서 업데이트가 발생하면 다른 탭/창으로 메시지가 전송되어 각자의 세션 상태를 업데이트합니다.

`refetchInterval` 값을 낮게 설정하면 네트워크 트래픽과 인증된 클라이언트 부하가 증가하며, 호스팅 비용과 성능에 영향을 줄 수 있습니다.

#### 기본 경로[​](https://next-auth.js.org/getting-started/client#base-path "Direct link to heading")

사용자 정의 기본 경로를 사용하고 있고 애플리케이션 진입점이 도메인 루트 `"/"`가 아니라 예를 들어 `"/my-app/"`인 경우, `basePath` prop을 사용해 NextAuth.js가 이를 인지하도록 할 수 있습니다. 그러면 모든 리디렉션과 세션 처리가 기대대로 동작합니다.

#### 재조회 간격[​](https://next-auth.js.org/getting-started/client#refetch-interval "Direct link to heading")

대안 옵션은 [Session Refetching](https://next-auth.js.org/getting-started/client#refetching-the-session)을 참고하세요.

`refetchInterval` 옵션은 세션 만료를 방지하기 위해 서버와 통신하는 데 사용할 수 있습니다.

`refetchInterval`이 `0`(기본값)이면 세션 폴링은 수행되지 않습니다.

0이 아닌 값으로 설정하면, 클라이언트가 세션 상태를 업데이트하기 위해 서버에 접속할 주기를 초 단위로 지정합니다. 트리거 시점에 세션 상태가 만료되어 있으면, 열려 있는 모든 탭/창이 이를 반영하도록 업데이트됩니다.

`refetchInterval` 값은 항상 세션 `maxAge` [session option](https://next-auth.js.org/configuration/options#session) 값보다 작아야 합니다.

기본적으로 세션 폴링은 기기에 인터넷 연결이 없어도 계속 시도합니다. 이를 피하려면 `refetchWhenOffline`을 `false`로 설정할 수 있습니다. 그러면 [`navigator.onLine`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/onLine)을 사용해 기기가 온라인일 때만 폴링합니다.

#### 창 포커스 시 재조회[​](https://next-auth.js.org/getting-started/client#refetch-on-window-focus "Direct link to heading")

대안 옵션은 [Session Refetching](https://next-auth.js.org/getting-started/client#refetching-the-session)을 참고하세요.

`refetchOnWindowFocus` 옵션은 탭/창의 포커스를 전환할 때 세션 상태를 자동으로 업데이트할지 제어하는 데 사용할 수 있습니다.

`refetchOnWindowFocus`가 `true`(기본값)로 설정되면, 탭/창이 포커스를 얻거나 잃을 때 업데이트되고 컴포넌트 상태가 초기화됩니다.

반대로 `false`로 설정하면 세션 재조회가 중지되고 컴포넌트는 현재 상태를 유지합니다.

note

Next.js 애플리케이션의 **\_ app.js**에 대한 자세한 내용은 [**the Next.js documentation**](https://nextjs.org/docs/advanced-features/custom-app)을 참고하세요.

### 사용자 정의 기본 경로[​](https://next-auth.js.org/getting-started/client#custom-base-path "Direct link to heading")

Next.js 애플리케이션이 사용자 정의 기본 경로를 사용하는 경우, 아래 예시 및 [here](https://next-auth.js.org/configuration/options#nextauth_url) 설명처럼 `NEXTAUTH_URL` 환경 변수를 API 엔드포인트의 전체 경로로 설정하세요.

또한 아래 예시처럼 `<SessionProvider>`에 `basePath` page prop을 전달해야 NextAuth.js에서 사용자 정의 기본 경로가 완전히 설정되고 사용됩니다.

#### 예시[​](https://next-auth.js.org/getting-started/client#example-3 "Direct link to heading")

이 예시에서 사용되는 사용자 정의 기본 경로는 `/custom-route`입니다.

```
    NEXTAUTH_URL=https://example.com/custom-route/api/auth

```

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
