---
title: "예제 코드"
description: "아래 예제 코드는 Next.js 앱에 인증을 추가하는 방법을 설명합니다."
---

출처 URL: https://next-auth.js.org/v3/getting-started/example

# 예제 코드 | NextAuth.js

버전: v3

## NextAuth.js 시작하기[​](https://next-auth.js.org/v3/getting-started/example#get-started-with-nextauthjs "Direct link to heading")

아래 예제 코드는 Next.js 앱에 인증을 추가하는 방법을 설명합니다.

tip

가장 쉽게 시작하는 방법은 [example app](https://github.com/nextauthjs/next-auth-example)을 클론하고 README.md의 안내를 따르는 것입니다. 라이브 데모는 [next-auth-example.vercel.app](https://next-auth-example.vercel.app)에서 확인할 수 있습니다.

### API 라우트 추가[​](https://next-auth.js.org/v3/getting-started/example#add-api-route "Direct link to heading")

프로젝트에 NextAuth.js를 추가하려면 `pages/api/auth`에 `[...nextauth].js` 파일을 생성하세요.

[인증 제공자(provider)를 추가하는 방법 자세히 보기](https://next-auth.js.org/providers)

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"

    export default NextAuth({
      // Configure one or more authentication providers
      providers: [
        Providers.GitHub({
          clientId: process.env.GITHUB_ID,
          clientSecret: process.env.GITHUB_SECRET,
        }),
        // ...add more providers here
      ],

      // A database is optional, but required to persist accounts in a database
      database: process.env.DATABASE_URL,
    })

```

`/api/auth/*`(signin, callback, signout 등)로 들어오는 모든 요청은 NextAuth.js가 자동으로 처리합니다.

tip

provider, database 및 기타 옵션을 설정하는 방법은 [options documentation](https://next-auth.js.org/configuration/options)에서 확인하세요.

### React Hook 추가[​](https://next-auth.js.org/v3/getting-started/example#add-react-hook "Direct link to heading")

NextAuth.js 클라이언트의 `useSession()` React Hook은 사용자가 로그인했는지 확인하는 가장 쉬운 방법입니다.

pages/index.js

```
    import { signIn, signOut, useSession } from "next-auth/client"

    export default function Page() {
      const [session, loading] = useSession()

      return (
        <>
          {!session && (
            <>
              Not signed in <br />
              <button onClick={() => signIn()}>Sign in</button>
            </>
          )}
          {session && (
            <>
              Signed in as {session.user.email} <br />
              <button onClick={() => signOut()}>Sign out</button>
            </>
          )}
        </>
      )
    }

```

tip

애플리케이션 어디에서나(예: 헤더 컴포넌트) `useSession` hook을 사용할 수 있습니다.

### 세션 상태 추가[​](https://next-auth.js.org/v3/getting-started/example#add-session-state "Direct link to heading")

페이지 간에 세션 상태를 공유할 수 있게 하려면(성능 개선, 네트워크 트래픽 감소, 렌더링 중 컴포넌트 상태 변경 방지) `pages/_app.js`에서 NextAuth.js Provider를 사용할 수 있습니다.

pages/\_app.js

```
    import { Provider } from "next-auth/client"

    export default function App({ Component, pageProps }) {
      return (
      )
    }

```

tip

NextAuth.js 클라이언트를 사용해 사용자 경험과 페이지 성능을 개선하는 방법은 [client documentation](https://next-auth.js.org/getting-started/client)에서 확인하세요.

### 프로덕션에 배포하기[​](https://next-auth.js.org/v3/getting-started/example#deploying-to-production "Direct link to heading")

사이트를 배포할 때 `NEXTAUTH_URL` 환경 변수를 웹사이트의 canonical URL로 설정하세요.

```
    NEXTAUTH_URL=https://example.com

```

tip

프로덕션에서는 앱을 배포하는 서비스의 환경 변수로 이것을 설정해야 합니다.

Vercel에서 환경 변수를 설정하려면 [dashboard](https://vercel.com/dashboard)를 사용하거나 `vercel env pull` [command](https://vercel.com/docs/build-step#development-environment-variables)를 사용할 수 있습니다.
