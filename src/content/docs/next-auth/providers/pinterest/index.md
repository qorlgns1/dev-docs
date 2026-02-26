---
title: "Pinterest"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/pinterest

# Pinterest | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/pinterest#documentation "Direct link to heading")

<https://developers.pinterest.com/docs/getting-started/authentication/>

## 구성[​](https://next-auth.js.org/providers/pinterest#configuration "Direct link to heading")

<https://developers.pinterest.com/apps/>

## 옵션[​](https://next-auth.js.org/providers/pinterest#options "Direct link to heading")

**Pinterest Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Pinterest Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/pinterest.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/pinterest#example "Direct link to heading")

```
    import PinterestProvider from "next-auth/providers/pinterest"
    ...
    providers: [
      PinterestProvider({
        clientId: process.env.PINTEREST_ID,
        clientSecret: process.env.PINTEREST_SECRET
      })
    ]
    ...

    :::tip
    To use in production, make sure the app has standard API access and not trial access
    :::

```
