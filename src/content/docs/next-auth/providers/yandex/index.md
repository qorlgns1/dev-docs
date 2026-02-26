---
title: "Yandex"
description: "사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/yandex

# Yandex | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/yandex#documentation "제목으로 직접 연결")

<https://tech.yandex.com/oauth/doc/dg/concepts/about-docpage/>

## 구성[​](https://next-auth.js.org/providers/yandex#configuration "제목으로 직접 연결")

<https://oauth.yandex.com/client/new>

## 옵션[​](https://next-auth.js.org/providers/yandex#options "제목으로 직접 연결")

**Yandex Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Yandex Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/yandex.ts)

사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/yandex#example "제목으로 직접 연결")

```
    import YandexProvider from "next-auth/providers/yandex";
    ...
    providers: [
      YandexProvider({
        clientId: process.env.YANDEX_CLIENT_ID,
        clientSecret: process.env.YANDEX_CLIENT_SECRET
      })
    ]
    ...

```
