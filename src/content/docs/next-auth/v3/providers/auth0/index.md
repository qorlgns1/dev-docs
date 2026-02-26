---
title: "Auth0"
description: "Auth0에서 애플리케이션을 'Single Page App'이 아닌 'Regular Web Application'으로 구성하세요."
---

출처 URL: https://next-auth.js.org/v3/providers/auth0

# Auth0 | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/auth0#documentation "Direct link to heading")

<https://auth0.com/docs/api/authentication#authorize-application>

## 구성[​](https://next-auth.js.org/v3/providers/auth0#configuration "Direct link to heading")

<https://manage.auth0.com/dashboard>

tip

Auth0에서 애플리케이션을 'Single Page App'이 아닌 'Regular Web Application'으로 구성하세요.

## 옵션[​](https://next-auth.js.org/v3/providers/auth0#options "Direct link to heading")

**Auth0 Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Auth0 Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/auth0.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/auth0#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Auth0({
        clientId: process.env.AUTH0_CLIENT_ID,
        clientSecret: process.env.AUTH0_CLIENT_SECRET,
        domain: process.env.AUTH0_DOMAIN
      })
    ]
    ...

```

note

`domain`은 정규화된 전체 도메인이어야 합니다. 예: `dev-s6clz2lv.eu.auth0.com`
