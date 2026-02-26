---
title: "Auth0"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/providers/auth0

# Auth0 | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/auth0#documentation "Direct link to heading")

<https://auth0.com/docs/api/authentication#authorize-application>

## 구성[​](https://next-auth.js.org/providers/auth0#configuration "Direct link to heading")

<https://manage.auth0.com/dashboard>

## 옵션[​](https://next-auth.js.org/providers/auth0#options "Direct link to heading")

**Auth0 Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Auth0 Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/auth0.ts)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/auth0#example "Direct link to heading")

```
    import Auth0Provider from "next-auth/providers/auth0";
    ...
    providers: [
      Auth0Provider({
        clientId: process.env.AUTH0_CLIENT_ID,
        clientSecret: process.env.AUTH0_CLIENT_SECRET,
        issuer: process.env.AUTH0_ISSUER
      })
    ]
    ...

```

참고

`issuer`는 완전한 URL이어야 합니다. 예: `https://dev-s6clz2lv.eu.auth0.com`
