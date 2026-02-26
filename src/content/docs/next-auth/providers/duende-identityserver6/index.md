---
title: "DuendeIdentityServer6"
description: "원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/duende-identityserver6

# DuendeIdentityServer6 | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/duende-identityserver6#documentation "Direct link to heading")

<https://docs.duendesoftware.com/identityserver/v6>

## 옵션[​](https://next-auth.js.org/providers/duende-identityserver6#options "Direct link to heading")

**DuendeIdentityServer6 Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [DuendeIdentityServer6 Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/duende-identity-server6.ts)

원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/duende-identityserver6#example "Direct link to heading")

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

## 데모 IdentityServer[​](https://next-auth.js.org/providers/duende-identityserver6#demo-identityserver "Direct link to heading")

아래 구성은 <https://demo.duendesoftware.com/>의 데모 서버용입니다.

직접 시도해 보려면 아래 구성을 복사하여 붙여넣을 수 있습니다.

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
