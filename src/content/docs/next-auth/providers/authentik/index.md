---
title: "Authentik"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/authentik

# Authentik | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/authentik#documentation "Direct link to heading")

<https://goauthentik.io/docs/providers/oauth2>

## 옵션[​](https://next-auth.js.org/providers/authentik#options "Direct link to heading")

**Authentik Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Authentik Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/authentik.ts)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/authentik#example "Direct link to heading")

```
    import AuthentikProvider from "next-auth/providers/authentik";
    ...
    providers: [
      AuthentikProvider({
        clientId: process.env.AUTHENTIK_ID,
        clientSecret: process.env.AUTHENTIK_SECRET,
        issuer: process.env.AUTHENTIK_ISSUER,
      })
    ]
    ...

```

참고

`issuer`에는 끝에 슬래시가 없는 slug가 포함되어야 합니다. 예: `https://my-authentik-domain.com/application/o/My_Slug`
