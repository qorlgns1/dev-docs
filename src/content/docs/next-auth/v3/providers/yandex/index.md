---
title: "Yandex"
description: "원본 URL: https://next-auth.js.org/v3/providers/yandex"
---

원본 URL: https://next-auth.js.org/v3/providers/yandex

# Yandex | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/yandex#documentation "Direct link to heading")

<https://tech.yandex.com/oauth/doc/dg/concepts/about-docpage/>

## 설정[​](https://next-auth.js.org/v3/providers/yandex#configuration "Direct link to heading")

<https://oauth.yandex.com/client/new>

## 옵션[​](https://next-auth.js.org/v3/providers/yandex#options "Direct link to heading")

**Yandex Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Yandex Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/yandex.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/yandex#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Yandex({
        clientId: process.env.YANDEX_CLIENT_ID,
        clientSecret: process.env.YANDEX_CLIENT_SECRET
      })
    ]
    ...

```
