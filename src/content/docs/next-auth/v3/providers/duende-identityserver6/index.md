---
title: "DuendeIdentityServer6"
description: "사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/duende-identityserver6

# DuendeIdentityServer6 | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/duende-identityserver6#documentation "Direct link to heading")

<https://docs.duendesoftware.com/identityserver/v6>

## 옵션[​](https://next-auth.js.org/v3/providers/duende-identityserver6#options "Direct link to heading")

**DuendeIdentityServer6 Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [DuendeIdentityServer6 Provider 옵션](https://github.com/nextauthjs/next-auth/tree/main/packages/next-auth/src/providers/duende-identity-server6.ts)

사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/duende-identityserver6#example "Direct link to heading")

```
    import DuendeIDS6Provider from "next-auth/providers/duende-identity-server6"

    ...
    providers: [
      DuendeIDS6Provider({
        clientId: process.env.DUENDE_IDS6_ID,
        clientSecret: process.env.DUENDE_IDS6_SECRET,
        issuer: process.env.DUENDE_IDS6_ISSUER,
      })
    ]
    ...

```

## 데모 IdentityServer[​](https://next-auth.js.org/v3/providers/duende-identityserver6#demo-identityserver "Direct link to heading")

아래 구성은 <https://demo.duendesoftware.com/>의 데모 서버용입니다.

체험해 보려면 아래 구성을 복사해 붙여넣으면 됩니다.

데모 서비스에는 **bob/bob** 또는 **alice/alice**로 로그인할 수 있습니다.

```
    import DuendeIDS6Provider from "next-auth/providers/duende-identity-server6"
    ...
    providers: [
      DuendeIDS6Provider({
        clientId: "interactive.confidential",
        clientSecret: "secret",
        issuer: "https://demo.duendesoftware.com",
      })
    ]
    ...

```
