---
title: "Patreon"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/patreon

# Patreon | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/patreon#documentation "Direct link to heading")

<https://docs.patreon.com/#apiv2-oauth>

## 구성[​](https://next-auth.js.org/providers/patreon#configuration "Direct link to heading")

tip

[Patreon Platform](https://www.patreon.com/portal/registration/register-clients)에서 API v2 클라이언트를 생성하세요.

## 옵션[​](https://next-auth.js.org/providers/patreon#options "Direct link to heading")

**Patreon Provider**는 기본 옵션 세트와 함께 제공됩니다:

- [Patreon Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/patreon.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/patreon#example "Direct link to heading")

```
    import PatreonProvider from "next-auth/providers/patreon";
    ...
    providers: [
        PatreonProvider({
          clientId: process.env.PATREON_ID,
          clientSecret: process.env.PATREON_SECRET,
        })
    ]
    ...

```

note

[ApiV2](https://docs.patreon.com/#scopes)에서 정의된 scopes를 사용해야 합니다.
