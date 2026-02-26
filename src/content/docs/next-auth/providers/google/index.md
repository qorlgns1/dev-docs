---
title: "Google"
description: '자격 증명을 생성할 때 사용하는 "Authorized redirect URIs"에는 전체 도메인이 포함되어야 하며 콜백 경로로 끝나야 합니다. 예를 들어:'
---

Source URL: https://next-auth.js.org/providers/google

# Google | NextAuth.js

Version: v4

## 문서[​](https://next-auth.js.org/providers/google#documentation "제목으로 바로 가는 링크")

<https://developers.google.com/identity/protocols/oauth2>

## 구성[​](https://next-auth.js.org/providers/google#configuration "제목으로 바로 가는 링크")

<https://console.developers.google.com/apis/credentials>

자격 증명을 생성할 때 사용하는 "Authorized redirect URIs"에는 전체 도메인이 포함되어야 하며 콜백 경로로 끝나야 합니다. 예를 들어:

- 프로덕션: `https://{YOUR_DOMAIN}/api/auth/callback/google`
- 개발: `http://localhost:3000/api/auth/callback/google`

## 옵션[​](https://next-auth.js.org/providers/google#options "제목으로 바로 가는 링크")

**Google Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Google Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/google.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/google#example "제목으로 바로 가는 링크")

```
    import GoogleProvider from "next-auth/providers/google";
    ...
    providers: [
      GoogleProvider({
        clientId: process.env.GOOGLE_CLIENT_ID,
        clientSecret: process.env.GOOGLE_CLIENT_SECRET
      })
    ]
    ...

```

danger

Google은 사용자가 처음 로그인할 때에만 애플리케이션에 Refresh Token을 제공합니다.

Google이 Refresh Token을 다시 발급하도록 강제하려면, 사용자가 계정에서 해당 애플리케이션을 제거한 뒤 다시 로그인해야 합니다: <https://myaccount.google.com/permissions>

또는 `authorization`의 `params` 객체에 옵션을 전달해 로그인 시 항상 Refresh Token이 제공되도록 강제할 수도 있습니다. 다만 이렇게 하면 모든 사용자가 로그인할 때마다 애플리케이션 접근 권한을 부여할지 확인해야 합니다.

Google 계정의 RefreshToken 또는 AccessToken에 접근해야 하고 사용자 계정을 유지하기 위한 데이터베이스를 사용하지 않는다면, 이 방법이 필요할 수 있습니다.

```
    const options = {
      ...
      providers: [
        GoogleProvider({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
          authorization: {
            params: {
              prompt: "consent",
              access_type: "offline",
              response_type: "code"
            }
          }
        })
      ],
      ...
    }

```

tip

Google은 OAuth 프로필에 `email_verified` 불리언 속성도 반환합니다.

이 속성을 사용해 특정 도메인에서 인증된 계정을 가진 사용자로 접근을 제한할 수 있습니다.

```
    const options = {
      ...
      callbacks: {
        async signIn({ account, profile }) {
          if (account.provider === "google") {
            return profile.email_verified && profile.email.endsWith("@example.com")
          }
          return true // Do different verification for other providers that don't have `email_verified`
        },
      }
      ...
    }

```
