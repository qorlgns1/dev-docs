---
title: "Google"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/google

# Google | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/google#documentation "Direct link to heading")

<https://developers.google.com/identity/protocols/oauth2>

## 구성[​](https://next-auth.js.org/v3/providers/google#configuration "Direct link to heading")

<https://console.developers.google.com/apis/credentials>

## 옵션[​](https://next-auth.js.org/v3/providers/google#options "Direct link to heading")

**Google Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Google Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/google.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/google#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Google({
        clientId: process.env.GOOGLE_CLIENT_ID,
        clientSecret: process.env.GOOGLE_CLIENT_SECRET
      })
    ]
    ...

```

danger

Google은 사용자가 처음 로그인할 때에만 애플리케이션에 Refresh Token을 제공합니다.

Google이 Refresh Token을 다시 발급하도록 강제하려면, 사용자가 계정에서 애플리케이션을 제거한 뒤 다시 로그인해야 합니다: <https://myaccount.google.com/permissions>

또는 `authorizationUrl`에 옵션을 전달해 로그인 시 항상 Refresh Token이 제공되도록 강제할 수도 있습니다. 다만 이 경우, 모든 사용자는 로그인할 때마다 애플리케이션 접근 권한을 부여할지 확인해야 합니다.

Google 계정의 RefreshToken 또는 AccessToken에 접근해야 하고, 사용자 계정을 영구 저장하기 위해 데이터베이스를 사용하지 않는다면 이것이 필요한 작업일 수 있습니다.

```
    const options = {
      ...
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
          authorizationUrl: 'https://accounts.google.com/o/oauth2/v2/auth?prompt=consent&access_type=offline&response_type=code',
        })
      ],
      ...
    }

```

tip

Google은 OAuth 프로필에서 `verified_email` 불리언 속성도 반환합니다.

이 속성을 사용해 특정 도메인에서 계정이 검증된 사용자로 접근을 제한할 수 있습니다.

```
    const options = {
      ...
      callbacks: {
        async signIn(user, account, profile) {
          if (account.provider === 'google' &&
              profile.verified_email === true &&
              profile.email.endsWith('@example.com')) {
            return true
          } else {
            return false
          }
        },
      }
      ...
    }

```
