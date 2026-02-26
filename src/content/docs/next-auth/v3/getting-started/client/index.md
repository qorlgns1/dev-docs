---
title: "클라이언트 API"
description: "NextAuth.js 클라이언트 라이브러리를 사용하면 React 애플리케이션에서 세션을 쉽게 다룰 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/getting-started/client

# 클라이언트 API | NextAuth.js

버전: v3

NextAuth.js 클라이언트 라이브러리를 사용하면 React 애플리케이션에서 세션을 쉽게 다룰 수 있습니다.

#### 세션 객체 예시[​](https://next-auth.js.org/v3/getting-started/client#example-session-object "Direct link to heading")

```
    {
      user: {
        name: string,
        email: string,
        image: uri
      },
      accessToken: string,
      expires: "YYYY-MM-DDTHH:mm:ss.SSSZ"
    }

```

tip

클라이언트에 반환되는 세션 데이터에는 Session Token이나 OAuth 토큰 같은 민감한 정보가 포함되지 않습니다. 프레젠테이션 목적(예: name, email, image)으로 로그인한 사용자 정보를 페이지에 표시하는 데 필요한 최소한의 페이로드만 포함합니다.

세션 객체에 추가 데이터를 반환해야 한다면 [session callback](https://next-auth.js.org/configuration/callbacks#session-callback)을 사용해 클라이언트로 반환되는 세션 객체를 커스터마이즈할 수 있습니다.

---

## useSession()[​](https://next-auth.js.org/v3/getting-started/client#usesession "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: 아니요

NextAuth.js 클라이언트의 `useSession()` React Hook은 사용자가 로그인했는지 확인하는 가장 쉬운 방법입니다.

`pages/_app.js`에 [`<Provider>`](https://next-auth.js.org/v3/getting-started/client#provider)를 추가했을 때 가장 잘 동작합니다.

#### 예시[​](https://next-auth.js.org/v3/getting-started/client#example "Direct link to heading")

```
    import { useSession } from "next-auth/client"

    export default function Component() {
      const [session, loading] = useSession()

      if (session) {
        return <p>Signed in as {session.user.email}</p>
      }

      return <a href="/api/auth/signin">Sign in</a>
    }

```

---

## getSession()[​](https://next-auth.js.org/v3/getting-started/client#getsession "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: **예**

NextAuth.js는 클라이언트 또는 서버 사이드에서 호출해 세션을 반환할 수 있는 `getSession()` 메서드를 제공합니다.

`/api/auth/session`을 호출하고, 세션 객체를 담은 promise를 반환합니다. 세션이 없으면 null을 반환합니다.

#### 클라이언트 사이드 예시[​](https://next-auth.js.org/v3/getting-started/client#client-side-example "Direct link to heading")

```
    async function myFunction() {
      const session = await getSession()
      /* ... */
    }

```

#### 서버 사이드 예시[​](https://next-auth.js.org/v3/getting-started/client#server-side-example "Direct link to heading")

```
    import { getSession } from "next-auth/client"

    export default async (req, res) => {
      const session = await getSession({ req })
      /* ... */
      res.end()
    }

```

note

서버 사이드에서 `getSession()`을 호출할 때는 `{req}` 또는 `context` 객체를 전달해야 합니다.

튜토리얼 [securing pages and API routes](https://next-auth.js.org/tutorials/securing-pages-and-api-routes)에서는 서버 사이드 호출에서 `getSession()`을 사용하는 방법을 보여줍니다.

---

## getCsrfToken()[​](https://next-auth.js.org/v3/getting-started/client#getcsrftoken "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: **예**

`getCsrfToken()` 메서드는 POST 요청(예: 로그인 및 로그아웃)에 필요한 현재 Cross Site Request Forgery Token(CSRF Token)을 반환합니다.

기본 제공 `signIn()` 및 `signOut()` 메서드를 사용하지 않는 경우에만 이 메서드가 필요할 가능성이 높습니다.

#### 클라이언트 사이드 예시[​](https://next-auth.js.org/v3/getting-started/client#client-side-example-1 "Direct link to heading")

```
    async function myFunction() {
      const csrfToken = await getCsrfToken()
      /* ... */
    }

```

#### 서버 사이드 예시[​](https://next-auth.js.org/v3/getting-started/client#server-side-example-1 "Direct link to heading")

```
    import { getCsrfToken } from "next-auth/client"

    export default async (req, res) => {
      const csrfToken = await getCsrfToken({ req })
      /* ... */
      res.end()
    }

```

---

## getProviders()[​](https://next-auth.js.org/v3/getting-started/client#getproviders "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: **예**

`getProviders()` 메서드는 현재 로그인에 구성된 provider 목록을 반환합니다.

`/api/auth/providers`를 호출하고, 현재 구성된 인증 provider 목록을 반환합니다.

동적 커스텀 로그인 페이지를 만들 때 유용할 수 있습니다.

---

#### API Route[​](https://next-auth.js.org/v3/getting-started/client#api-route "Direct link to heading")

pages/api/example.js

```
    import { getProviders } from "next-auth/client"

    export default async (req, res) => {
      const providers = await getProviders()
      console.log("Providers", providers)
      res.end()
    }

```

note

`getSession()` 및 `getCsrfToken()`과 달리, 서버 사이드에서 `getProviders()`를 호출할 때는 클라이언트 사이드 호출과 마찬가지로 아무것도 전달할 필요가 없습니다.

---

## signIn()[​](https://next-auth.js.org/v3/getting-started/client#signin "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: 아니요

`signIn()` 메서드를 사용하면 로그인 플로우를 완료한 뒤 사용자가 시작했던 페이지로 돌아가게 됩니다. 또한 이메일로 로그인할 때 CSRF Token도 자동으로 처리합니다.

`signIn()` 메서드는 아래와 같이 다양한 방식으로 클라이언트에서 호출할 수 있습니다.

#### 클릭 시 로그인 페이지로 리디렉션[​](https://next-auth.js.org/v3/getting-started/client#redirects-to-sign-in-page-when-clicked "Direct link to heading")

```
    import { signIn } from "next-auth/client"

    export default () => <button onClick={() => signIn()}>Sign in</button>

```

#### 클릭 시 Google OAuth 로그인 플로우 시작[​](https://next-auth.js.org/v3/getting-started/client#starts-google-oauth-sign-in-flow-when-clicked "Direct link to heading")

```
    import { signIn } from "next-auth/client"

    export default () => (
      <button onClick={() => signIn("google")}>Sign in with Google</button>
    )

```

#### 클릭 시 이메일 로그인 플로우 시작[​](https://next-auth.js.org/v3/getting-started/client#starts-email-sign-in-flow-when-clicked "Direct link to heading")

이메일 플로우와 함께 사용할 때는 대상 `email`을 옵션으로 전달하세요.

```
    import { signIn } from "next-auth/client"

    export default ({ email }) => (
      <button onClick={() => signIn("email", { email })}>Sign in with Email</button>
    )

```

#### callbackUrl 지정하기[​](https://next-auth.js.org/v3/getting-started/client#specifying-a-callbackurl "Direct link to heading")

`callbackUrl`은 로그인 후 사용자를 어떤 URL로 리디렉션할지 지정합니다. 기본값은 사용자의 현재 URL입니다.

`signIn()`의 두 번째 인수로 지정하면 다른 `callbackUrl`을 설정할 수 있습니다. 이는 모든 provider에서 동작합니다.

예:

- `signIn(null, { callbackUrl: 'http://localhost:3000/foo' })`
- `signIn('google', { callbackUrl: 'http://localhost:3000/foo' })`
- `signIn('email', { email, callbackUrl: 'http://localhost:3000/foo' })`

해당 URL은 [redirect callback handler](https://next-auth.js.org/configuration/callbacks#redirect-callback)에서 유효한 것으로 간주되어야 합니다. 기본적으로 같은 hostname의 절대 URL이어야 하며, 그렇지 않으면 홈페이지로 리디렉션됩니다. 상대 URL 지원을 포함해 다른 URL을 허용하려면 사용자 정의 [redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 정의할 수 있습니다.

#### redirect: false 옵션 사용하기[​](https://next-auth.js.org/v3/getting-started/client#using-the-redirect-false-option "Direct link to heading")

note

redirect 옵션은 `credentials` 및 `email` provider에서만 사용할 수 있습니다.

일부 경우에는 같은 페이지에서 로그인 응답을 처리하고 기본 리디렉션을 비활성화하고 싶을 수 있습니다. 예를 들어 오류가 발생했을 때(예: 사용자가 잘못된 자격 증명을 입력한 경우) 같은 페이지에서 오류를 처리하고 싶을 수 있습니다. 이 경우 두 번째 파라미터 객체에 `redirect: false`를 전달하면 됩니다.

예:

- `signIn('credentials', { redirect: false, password: 'password' })`
- `signIn('email', { redirect: false, email: 'bill@fillmurray.com' })`

그러면 `signIn`은 Promise를 반환하고, 다음 값으로 resolve됩니다:

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

#### 추가 파라미터[​](https://next-auth.js.org/v3/getting-started/client#additional-params "Direct link to heading")

`signIn()`의 세 번째 인수를 통해 `/authorize` endpoint에 추가 파라미터를 전달할 수도 있습니다.

아이디어는 [Authorization Request OIDC spec](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)을 참고하세요. (가능한 항목이 이것들로 제한되지는 않으며, 모든 파라미터가 전달됩니다)

예:

- `signIn("identity-server4", null, { prompt: "login" })` _항상 사용자에게 재인증 요청_
- `signIn("auth0", null, { login_hint: "info@example.com" })` _provider에 이메일 주소 힌트 제공_

note

이 파라미터들은 [`provider.authorizationParams`](https://next-auth.js.org/configuration/providers/oauth#options)로도 설정할 수 있습니다.

note

다음 파라미터는 항상 서버 사이드에서 덮어써집니다: `redirect_uri`, `state`

---

## signOut()[​](https://next-auth.js.org/v3/getting-started/client#signout "Direct link to heading")

- 클라이언트 사이드: **예**
- 서버 사이드: 아니요

`signOut()` 메서드를 사용하면 로그아웃 플로우 완료 후 사용자가 시작했던 페이지로 돌아가게 됩니다. 또한 CSRF 토큰도 자동으로 처리합니다.

완료되면 브라우저에서 페이지를 다시 로드합니다.

```
    import { signOut } from "next-auth/client"

    export default () => <button onClick={() => signOut()}>Sign out</button>

```

#### callbackUrl 지정하기[​](https://next-auth.js.org/v3/getting-started/client#specifying-a-callbackurl-1 "Direct link to heading")

`signIn()` 함수와 마찬가지로 옵션으로 `callbackUrl` 파라미터를 전달해 지정할 수 있습니다.

예: `signOut({ callbackUrl: 'http://localhost:3000/foo' })`

해당 URL은 [redirect callback handler](https://next-auth.js.org/configuration/callbacks#redirect-callback)에서 유효한 것으로 간주되어야 합니다. 기본적으로 같은 hostname의 절대 URL이어야 하며(그렇지 않으면 홈페이지로 이동), 상대 URL 지원을 포함해 다른 URL을 허용하려면 사용자 정의 [redirect callback](https://next-auth.js.org/configuration/callbacks#redirect-callback)을 정의할 수 있습니다.

#### redirect: false 옵션 사용하기[​](https://next-auth.js.org/v3/getting-started/client#using-the-redirect-false-option-1 "Direct link to heading")

`signOut`에 `redirect: false`를 전달하면 페이지가 다시 로드되지 않습니다. 세션은 삭제되고 `useSession` hook에 알림이 전달되므로, 사용자 관련 표시가 자동으로 로그아웃 상태로 보입니다. 사용자 경험이 매우 좋아질 수 있습니다.

tip

다른 페이지로 리디렉션해야 하지만 페이지 리로드를 피하고 싶다면 `const data = await signOut({redirect: false, callbackUrl: "/foo"})`를 사용할 수 있습니다. 여기서 `data.url`은 검증된 url이며, Next.js의 `useRouter().push(data.url)`를 사용하면 깜빡임 없이 사용자 리디렉션이 가능합니다.

---

## Provider[​](https://next-auth.js.org/v3/getting-started/client#provider "Direct link to heading")

제공되는 React `<Provider>`를 사용하면 내부적으로 [React Context](https://reactjs.org/docs/context.html)를 활용해 `useSession()` 인스턴스들이 컴포넌트 간에 세션 객체를 공유할 수 있습니다.

이는 성능을 향상시키고 네트워크 호출을 줄이며 렌더링 시 페이지 깜빡임을 방지합니다. 강력히 권장되며, `pages/_app.js`를 사용해 Next.js 앱의 모든 페이지에 쉽게 추가할 수 있습니다.

pages/\_app.js

```
    import { Provider } from "next-auth/client"

    export default function App({ Component, pageProps }) {
      return (
      )
    }

```

위 예시처럼 `<Provider>`에 `session` page prop을 전달하면, 서버/클라이언트 사이드 렌더링을 모두 지원하는 페이지에서 세션을 두 번 확인하는 일을 피할 수 있습니다.

다만 이는 올바른 `pageProps`를 제공하는 페이지에서만 동작합니다. 일반적으로 `getInitialProps` 또는 `getServerSideProps`에서 다음과 같이 처리합니다:

pages/index.js

```
    import { getSession } from "next-auth/client"

    ...

    export async function getServerSideProps(ctx) {
      return {
        props: {
          session: await getSession(ctx)
        }
      }
    }

```

모든 페이지를 보호해야 한다면 `_app`에서 처리할 수 있고, 그렇지 않다면 페이지별로 처리할 수 있습니다. 또는 아래 [alternative client session handling](https://next-auth.js.org/v3/getting-started/client#custom-client-session-handling)에 설명된 방법을 사용해, 각 인증 확인을 차단형(SSR)으로 수행하는 대신 페이지별 클라이언트 사이드 인증 확인을 수행할 수도 있습니다.

### 옵션[​](https://next-auth.js.org/v3/getting-started/client#options "Direct link to heading")

세션 상태는 열려 있는 모든 탭/창 간에 자동으로 동기화되며, 포커스를 얻거나 잃을 때 또는 어느 하나에서 상태가 바뀔 때마다(예: 사용자가 로그인/로그아웃) 모두 업데이트됩니다.

세션 만료 시간이 30일(기본값) 이상이라면 Provider의 기본 옵션을 변경할 필요가 거의 없습니다. 필요하다면 클라이언트 사이드 함수에서 `getSession()`을 호출해 모든 탭/창의 세션 객체 업데이트를 트리거할 수 있습니다.

하지만 세션 동작을 커스터마이즈해야 하거나 짧은 세션 만료 시간을 사용하는 경우, provider에 옵션을 전달해 `useSession()` hook의 동작을 커스터마이즈할 수 있습니다.

pages/\_app.js

```
    import { Provider } from 'next-auth/client'

    export default function App ({ Component, pageProps }) {
      return (
      )
    }

```

note

**이 옵션들은 로그인하지 않은 클라이언트에는 영향을 주지 않습니다.**

각 탭/창은 로컬 세션 상태의 자체 복사본을 유지합니다. 세션은 localStorage나 sessionStorage 같은 공유 저장소에 저장되지 않습니다. 한 탭/창에서 업데이트가 발생하면 다른 탭/창이 자신의 세션 상태를 업데이트하도록 메시지가 트리거됩니다.

`clientMaxAge` 또는 `keepAlive` 값을 낮게 설정하면 네트워크 트래픽이 증가하고 인증된 클라이언트의 부하가 커지며, 호스팅 비용과 성능에 영향을 줄 수 있습니다.

#### 클라이언트 최대 유지 시간[​](https://next-auth.js.org/v3/getting-started/client#client-max-age "Direct link to heading")

`clientMaxAge` 옵션은 클라이언트의 세션 데이터가 오래된 것으로 간주되기 전까지 유지될 수 있는 최대 시간입니다.

`clientMaxAge`가 `0`(기본값)으로 설정되면 `useSession`이 호출될 때 항상 캐시가 사용되며, 세션 상태를 가져오기 위한 명시적 호출(예: `getSession()`)이나 다른 탭/창에서 로그인 또는 로그아웃, 탭/창의 포커스 획득/손실 같은 이벤트 트리거가 있을 때만 세션 상태 업데이트가 발생합니다.

0이 아닌 값으로 설정하면, 클라이언트의 세션 데이터가 해당 시간(초)을 초과해 오래된 경우 `useSession()` 훅이 세션 상태 동기화를 위해 서버를 다시 호출합니다.

세션 만료 시간이 짧은 경우(예: 24시간 미만)가 아니라면 이 옵션을 변경할 필요는 거의 없습니다. 이 값을 너무 짧게 설정하면 부하(및 잠재적으로 호스팅 비용)가 증가합니다.

`clientMaxAge` 값은 항상 세션의 `maxAge` 옵션 값보다 낮아야 합니다.

#### Keep Alive[​](https://next-auth.js.org/v3/getting-started/client#keep-alive "Direct link to heading")

`keepAlive` 옵션은 세션 만료를 방지하기 위해 클라이언트가 서버에 얼마나 자주 접속해야 하는지를 의미합니다.

`keepAlive`가 `0`(기본값)으로 설정되면 keep alive 메시지를 보내지 않습니다.

0이 아닌 값으로 설정하면, 클라이언트가 세션 상태를 업데이트하기 위해 서버에 접속해야 하는 주기를 초 단위로 지정합니다. 트리거 시점에 세션 상태가 만료되어 있으면, 열려 있는 모든 탭/창에 이 상태가 반영되도록 업데이트됩니다.

`keepAlive` 값은 항상 세션의 `maxAge` 옵션 값보다 낮아야 합니다.

note

Next.js 애플리케이션의 **\_ app.js**에 대한 자세한 내용은 [**Next.js 문서**](https://nextjs.org/docs/advanced-features/custom-app)를 참고하세요.

## 대안[​](https://next-auth.js.org/v3/getting-started/client#alternatives "Direct link to heading")

### 커스텀 클라이언트 세션 처리[​](https://next-auth.js.org/v3/getting-started/client#custom-client-session-handling "Direct link to heading")

Next.js가 `getServerSideProps` / `getInitialProps`를 처리하는 방식 때문에, 보호된 페이지를 로드할 때마다 세션이 유효한지 확인하기 위한 서버 사이드 쿼리를 수행한 뒤 요청된 페이지를 생성해야 합니다. 이 대안 솔루션은 초기 확인 시 로딩 상태를 표시할 수 있으며, 이후의 모든 페이지 전환은 서버 확인 및 페이지 재생성 없이 클라이언트 사이드에서 이루어집니다.

pages/admin.jsx

```
    export default function AdminDashboard() {
      const [session] = useSession()
      // session is always non-null inside this page, all the way down the React tree.
      return "Some super secret dashboard"
    }

    AdminDashboard.auth = true

```

pages/\_app.jsx

```
    export default function App({ Component, pageProps }) {
      return (
          {Component.auth ? (
          ) : (
          )}
      )
    }

    function Auth({ children }) {
      const [session, loading] = useSession()
      const isUser = !!session?.user
      React.useEffect(() => {
        if (loading) return // Do nothing while loading
        if (!isUser) signIn() // If not authenticated, force log in
      }, [isUser, loading])

      if (isUser) {
        return children
      }

      // Session is being fetched, or no user.
      // If no user, useEffect() will redirect.
      return <div>Loading...</div>
    }

```

페이지 단위 역할 기반 인증을 위한 옵션 객체 같은 형태를 지원하도록 쉽게 확장/수정할 수 있습니다. 예시:

pages/admin.jsx

```
    AdminDashboard.auth = {
      role: "admin",
      loading: <AdminLoadingSkeleton />,
      unauthorized: "/login-with-different-user", // redirect to this url
    }

```

\_app 구성 방식 덕분에 인증이 필요하지 않은 페이지에서는 /api/auth/session 엔드포인트에 불필요하게 요청하지 않습니다.

자세한 내용은 다음 [Github Issue](https://github.com/nextauthjs/next-auth/issues/1210)에서 확인할 수 있습니다.

### NextAuth.js + React-Query[​](https://next-auth.js.org/v3/getting-started/client#nextauthjs--react-query "Direct link to heading")

[`react-query`](https://www.npmjs.com/package/react-query) 기반의 대체 클라이언트 사이드 API 라이브러리도 [`nextauthjs/react-query`](https://github.com/nextauthjs/react-query)에서 제공됩니다.

이미 프로젝트에서 `react-query`를 사용 중이라면, NextAuth.js와 함께 활용해 클라이언트 사이드 세션 관리를 처리할 수 있습니다. 이는 `next-auth/client`의 NextAuth.js 기본 `useSession` 및 `Provider`를 대체합니다.

자세한 내용은 저장소 [`README`](https://github.com/nextauthjs/react-query)를 참고하세요.
