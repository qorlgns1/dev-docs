---
title: "OneLogin"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/onelogin

# OneLogin | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/onelogin#documentation "헤딩으로 바로 가기 링크")

<https://developers.onelogin.com/openid-connect>

## 구성[​](https://next-auth.js.org/providers/onelogin#configuration "헤딩으로 바로 가기 링크")

<https://developers.onelogin.com/openid-connect/connect-to-onelogin>

## 옵션[​](https://next-auth.js.org/providers/onelogin#options "헤딩으로 바로 가기 링크")

**OneLogin Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [OneLogin Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/onelogin.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/onelogin#example "헤딩으로 바로 가기 링크")

```
    import OneLoginProvider from "next-auth/providers/onelogin";
    ...
    providers: [
      OneLoginProvider({
        clientId: process.env.ONELOGIN_CLIENT_ID,
        clientSecret: process.env.ONELOGIN_CLIENT_SECRET,
        issuer: process.env.ONELOGIN_ISSUER
      })
    ]
    ...

```
