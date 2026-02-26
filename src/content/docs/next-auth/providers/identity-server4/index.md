---
title: "IdentityServer4"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/identity-server4

# IdentityServer4 | NextAuth.js

버전: v4

danger

[IdentityServer4는 지원이 중단되었습니다](https://identityserver4.readthedocs.io/en/latest/#:~:text=until%20November%202022.) 그리고 2022년 11월까지만 보안 업데이트가 릴리스됩니다. 대체 provider를 고려해야 합니다.

## 문서[​](https://next-auth.js.org/providers/identity-server4#documentation "Direct link to heading")

<https://identityserver4.readthedocs.io/en/latest/>

## 옵션[​](https://next-auth.js.org/providers/identity-server4#options "Direct link to heading")

**IdentityServer4 Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [IdentityServer4 Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/identity-server4.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/identity-server4#example "Direct link to heading")

```
    import IdentityServer4Provider from "next-auth/providers/identity-server4";
    ...
    providers: [
      IdentityServer4Provider({
        id: "identity-server4",
        name: "IdentityServer4",
        issuer:  process.env.IdentityServer4_Issuer,
        clientId: process.env.IdentityServer4_CLIENT_ID,
        clientSecret: process.env.IdentityServer4_CLIENT_SECRET
      })
    ]
    ...

```
