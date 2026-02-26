---
title: "Okta"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/okta

# Okta | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/okta#documentation "Direct link to heading")

<https://developer.okta.com/docs/reference/api/oidc>

## 옵션[​](https://next-auth.js.org/providers/okta#options "Direct link to heading")

**Okta Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Okta Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/okta.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/okta#example "Direct link to heading")

```
    import OktaProvider from "next-auth/providers/okta";
    ...
    providers: [
      OktaProvider({
        clientId: process.env.OKTA_CLIENT_ID,
        clientSecret: process.env.OKTA_CLIENT_SECRET,
        issuer: process.env.OKTA_ISSUER
      })
    ]
    ...

```
