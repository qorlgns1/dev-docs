---
title: "IdentityServer4"
description: "사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다."
---

출처 URL: https://next-auth.js.org/v3/providers/identity-server4

# IdentityServer4 | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/identity-server4#documentation "Direct link to heading")

<https://identityserver4.readthedocs.io/en/latest/>

## 옵션[​](https://next-auth.js.org/v3/providers/identity-server4#options "Direct link to heading")

**IdentityServer4 Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [IdentityServer4 Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/identity-server4.js)

사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/identity-server4#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.IdentityServer4({
        id: "identity-server4",
        name: "IdentityServer4",
        scope: "openid profile email api offline_access", // Allowed Scopes
        domain:  process.env.IdentityServer4_Domain,
        clientId: process.env.IdentityServer4_CLIENT_ID,
        clientSecret: process.env.IdentityServer4_CLIENT_SECRET
      })
    ]
    ...

```

## 데모 IdentityServer[​](https://next-auth.js.org/v3/providers/identity-server4#demo-identityserver "Direct link to heading")

아래 구성은 <https://demo.identityserver.io/>의 데모 서버용입니다.

사용해 보려면 아래 구성을 복사해 붙여넣으면 됩니다.

데모 서비스에는 **bob/bob** 또는 **alice/alice**로 로그인할 수 있습니다.

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.IdentityServer4({
        id: "demo-identity-server",
        name: "Demo IdentityServer4",
        scope: "openid profile email api offline_access",
        domain:  "demo.identityserver.io",
        clientId: "interactive.confidential",
        clientSecret: "secret",
        protection: "pkce"
      })
    ]
    ...

```
