---
title: "NextAuth.js"
description: "_(Google, Facebook, Auth0, Apple…)_"
---

Source URL: https://next-auth.js.org/

# NextAuth.js

## 오픈 소스. 풀스택. 데이터는 직접 소유하세요.

![Easy](https://next-auth.js.org/img/undraw_social.svg)

### 쉬움

- 인기 서비스 기본 지원
  _(Google, Facebook, Auth0, Apple…)_
- 이메일 / 패스워드리스 / 매직 링크 기본 지원
- 어떤 사용자 이름 / 비밀번호 저장소와도 사용 가능
- OAuth 1.0 및 2.0 서비스와 함께 사용 가능

![Flexible](https://next-auth.js.org/img/undraw_authentication.svg)

### 유연함

- Serverless를 위해 설계되어 어디서나 실행 가능
- 데이터베이스는 직접 선택 - 없어도 됨!
  _(MySQL, Postgres, MSSQL, MongoDB…)_
- 데이터베이스 세션 또는 JWT 선택 가능
- 웹 페이지와 API 라우트 보호

![Secure](https://next-auth.js.org/img/undraw_secure.svg)

### 보안성

- 서명되고 접두사가 붙은 서버 전용 쿠키
- HTTP POST + CSRF Token 검증
- JWS / JWE / JWK를 사용하는 JWT
- 탭 동기화, 자동 재검증, keepalive
- 클라이언트 사이드 JavaScript에 의존하지 않음

[npm install next-auth](https://www.npmjs.com/package/next-auth)

## 몇 분 만에 인증 추가!

#### 서버 /pages/api/auth/[...nextauth].js

```
    import NextAuth from 'next-auth'
    import AppleProvider from 'next-auth/providers/apple'
    import FacebookProvider from 'next-auth/providers/facebook'
    import GoogleProvider from 'next-auth/providers/google'
    import EmailProvider from 'next-auth/providers/email'

    export default NextAuth({
      providers: [
        // OAuth authentication providers...
        AppleProvider({
          clientId: process.env.APPLE_ID,
          clientSecret: process.env.APPLE_SECRET
        }),
        FacebookProvider({
          clientId: process.env.FACEBOOK_ID,
          clientSecret: process.env.FACEBOOK_SECRET
        }),
        GoogleProvider({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET
        }),
        // Passwordless / email sign in
        EmailProvider({
          server: process.env.MAIL_SERVER,
          from: 'NextAuth.js <no-reply@example.com>'
        }),
      ]
    })

```

#### 클라이언트 (App) /pages/\_app.jsx

```
    import { SessionProvider } from "next-auth/react"

    export default function App({
      Component, pageProps: { session, ...pageProps }
    }) {
      return (
      )
    }

```

#### 클라이언트 (Page) /pages/index.js

```
    import { useSession, signIn, signOut } from "next-auth/react"

    export default function Component() {
      const { data: session } = useSession()
      if(session) {
        return <>
          Signed in as {session.user.email} <br/>
          <button onClick={() => signOut()}>Sign out</button>
        </>
      }
      return <>
        Not signed in <br/>
        <button onClick={() => signIn()}>Sign in</button>
      </>
    }

```

[예제 코드](https://next-auth.js.org/getting-started/example)

NextAuth.js는 오픈 소스 커뮤니티 프로젝트입니다.
