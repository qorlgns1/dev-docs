---
title: "시작하기"
description: "아래 예제 코드는 Next.js 앱에 인증을 추가하는 방법을 설명합니다."
---

Source URL: https://next-auth.js.org/getting-started/example

# 시작하기 | NextAuth.js

버전: v4

아래 예제 코드는 Next.js 앱에 인증을 추가하는 방법을 설명합니다.

## 새 프로젝트[​](https://next-auth.js.org/getting-started/example#new-project "헤딩으로 바로 가기")

가장 쉬운 시작 방법은 [example app](https://github.com/nextauthjs/next-auth-example)을 클론하고 README.md의 안내를 따르는 것입니다. 라이브 데모는 <https://next-auth-example.vercel.app/> 에서 확인할 수 있습니다.

## 기존 프로젝트[​](https://next-auth.js.org/getting-started/example#existing-project "헤딩으로 바로 가기")

### NextAuth 설치[​](https://next-auth.js.org/getting-started/example#install-nextauth "헤딩으로 바로 가기")

- npm
- yarn
- pnpm

```
    npm install next-auth
```

```
    yarn add next-auth
```

```
    pnpm add next-auth
```

info

TypeScript를 사용 중이라면, NextAuth.js는 패키지 내부에 타입 정의를 함께 제공합니다. `next-auth`용 TypeScript에 대해 더 알아보려면 [TypeScript documentation](https://next-auth.js.org/getting-started/typescript)을 확인하세요.

### API 라우트 추가[​](https://next-auth.js.org/getting-started/example#add-api-route "헤딩으로 바로 가기")

프로젝트에 NextAuth.js를 추가하려면 `pages/api/auth`에 `[...nextauth].js` 파일을 생성하세요. 이 파일에는 NextAuth.js의 동적 라우트 핸들러가 포함되며, 전역 NextAuth.js 구성도 모두 여기에 들어갑니다.

새 App Router(`app/`)와 함께 [Next.js 13.2](https://nextjs.org/blog/next-13-2#custom-route-handlers) 이상을 사용 중이라면, [guide](https://next-auth.js.org/configuration/initialization#route-handlers-app)를 따라 새로운 [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)를 사용해 구성을 초기화할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"import GithubProvider from "next-auth/providers/github"export const authOptions = {  // Configure one or more authentication providers  providers: [    GithubProvider({      clientId: process.env.GITHUB_ID,      clientSecret: process.env.GITHUB_SECRET,    }),    // ...add more providers here  ],}export default NextAuth(authOptions)
```

`/api/auth/*` (`signIn`, `callback`, `signOut` 등)로 들어오는 모든 요청은 NextAuth.js가 자동으로 처리합니다.

**추가 읽을거리** :

- provider, database 및 기타 옵션을 구성하는 방법에 대한 자세한 내용은 [options documentation](https://next-auth.js.org/configuration/options)을 참고하세요.
- 인증 provider를 추가하는 방법은 [여기](https://next-auth.js.org/providers)에서 더 읽어보세요.

#### 공유 세션 상태 구성[​](https://next-auth.js.org/getting-started/example#configure-shared-session-state "헤딩으로 바로 가기")

`useSession`을 사용하려면 먼저 애플리케이션 최상위에서 세션 컨텍스트인 [`<SessionProvider />`](https://next-auth.js.org/getting-started/client#sessionprovider)를 노출해야 합니다.

pages/\_app.jsx

```
    import { SessionProvider } from "next-auth/react"export default function App({  Component,  pageProps: { session, ...pageProps },}) {  return (    <SessionProvider session={session}>      <Component {...pageProps} />    </SessionProvider>  )}
```

그다음 `useSession` 인스턴스는 세션 데이터와 상태에 접근할 수 있습니다. `<SessionProvider />`는 브라우저 탭과 창 사이에서 세션을 최신 상태로 유지하고 동기화하는 역할도 합니다.

tip

NextAuth.js 클라이언트를 사용해 사용자 경험과 페이지 성능을 개선하는 방법은 [client documentation](https://next-auth.js.org/getting-started/client)에서 확인하세요. Next.js App Router를 사용 중이라면 `<SessionProvider />`는 클라이언트 컴포넌트가 필요하므로 루트 레이아웃 내부에 둘 수 없다는 점에 유의하세요. 자세한 내용은 [Next.js documentation](https://nextjs.org/docs/app/getting-started/layouts-and-pages)을 확인하세요.

### 프론트엔드 - React Hook 추가[​](https://next-auth.js.org/getting-started/example#frontend---add-react-hook "헤딩으로 바로 가기")

NextAuth.js 클라이언트의 [`useSession()`](https://next-auth.js.org/getting-started/client#usesession) React Hook은 사용자가 로그인했는지 확인하는 가장 쉬운 방법입니다.

components/login-btn.jsx

```
    import { useSession, signIn, signOut } from "next-auth/react"export default function Component() {  const { data: session } = useSession()  if (session) {    return (      <>        Signed in as {session.user.email} <br />        <button onClick={() => signOut()}>Sign out</button>      </>    )  }  return (    <>      Not signed in <br />      <button onClick={() => signIn()}>Sign in</button>    </>  )}
```

`useSession` 훅은 애플리케이션 어디에서나 사용할 수 있습니다(예: 헤더 컴포넌트).

### 백엔드 - API 라우트[​](https://next-auth.js.org/getting-started/example#backend---api-route "헤딩으로 바로 가기")

API 라우트를 보호하려면 [`getServerSession()`](https://next-auth.js.org/configuration/nextjs#unstable_getserversession) 메서드를 사용할 수 있습니다.

pages/api/restricted.js

```
    import { getServerSession } from "next-auth/next"import { authOptions } from "./auth/[...nextauth]"export default async (req, res) => {  const session = await getServerSession(req, res, authOptions)  if (session) {    res.send({      content:        "This is protected content. You can access this content because you are signed in.",    })  } else {    res.send({      error: "You must be signed in to view the protected content on this page.",    })  }}
```

### 확장성[​](https://next-auth.js.org/getting-started/example#extensibility "헤딩으로 바로 가기")

#### NextAuth.js 콜백 사용[​](https://next-auth.js.org/getting-started/example#using-nextauthjs-callbacks "헤딩으로 바로 가기")

NextAuth.js는 [내장 콜백](https://next-auth.js.org/configuration/callbacks)을 통해 인증 흐름의 다양한 부분에 훅을 걸 수 있게 해줍니다.

예를 들어 로그인 시점의 값을 프론트엔드(클라이언트 사이드)로 전달하려면, [`session`](https://next-auth.js.org/configuration/callbacks#session-callback) 콜백과 [`jwt`](https://next-auth.js.org/configuration/callbacks#jwt-callback) 콜백을 다음과 같이 조합해 사용할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    ...
    callbacks: {
      async jwt({ token, account }) {
        // Persist the OAuth access_token to the token right after signin
        if (account) {
          token.accessToken = account.access_token
        }
        return token
      },
      async session({ session, token, user }) {
        // Send properties to the client, like an access_token from a provider.
        session.accessToken = token.accessToken
        return session
      }
    }
    ...

```

이제 [`getSession`](https://next-auth.js.org/getting-started/client#getsession) 또는 [`useSession`](https://next-auth.js.org/getting-started/client#usesession)을 호출할 때마다 반환되는 데이터 객체에 `accessToken` 값이 포함됩니다.

components/accessToken.jsx

```
    import { useSession, signIn, signOut } from "next-auth/react"export default function Component() {  const { data } = useSession()  const { accessToken } = data  return <div>Access Token: {accessToken}</div>}
```

## 콜백 URL 구성 (OAuth 전용)[​](https://next-auth.js.org/getting-started/example#configuring-callback-url-oauth-only "헤딩으로 바로 가기")

[내장 provider](https://next-auth.js.org/configuration/providers/oauth) 또는 [custom provider](https://next-auth.js.org/configuration/providers/oauth#using-a-custom-provider)를 통해 OAuth provider를 사용 중이라면, provider 설정에서 콜백 URL을 구성해야 합니다. 각 provider에는 이를 설정하는 방법에 대한 단서를 제공하는 "Configuration" 섹션이 있습니다.

OAuth provider와 통합하는 방법은 [these steps](https://next-auth.js.org/configuration/providers/oauth#how-to)를 따라 확인하세요.

## 프로덕션 배포[​](https://next-auth.js.org/getting-started/example#deploying-to-production "헤딩으로 바로 가기")

사이트를 배포할 때 `NEXTAUTH_URL` 환경 변수를 웹사이트의 정식 URL로 설정하세요.

```
    NEXTAUTH_URL=https://example.com

```

tip

프로덕션에서는 앱을 배포하는 서비스에 이 값을 환경 변수로 설정해야 합니다.

Vercel에서 환경 변수를 설정하려면 [dashboard](https://vercel.com/dashboard) 또는 `vercel env pull` [command](https://vercel.com/docs/build-step#development-environment-variables)를 사용할 수 있습니다.

자세한 내용은 [deployment page](https://next-auth.js.org/deployment)를 확인하세요.
