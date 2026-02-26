---
title: "osu!"
description: "원본 URL: https://next-auth.js.org/providers/osu"
---

원본 URL: https://next-auth.js.org/providers/osu

# osu! | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/osu#documentation "헤딩으로 바로 가기")

<https://osu.ppy.sh/docs/index.html#authentication>

## 구성[​](https://next-auth.js.org/providers/osu#configuration "헤딩으로 바로 가기")

<https://osu.ppy.sh/home/account/edit#new-oauth-application>

## 옵션[​](https://next-auth.js.org/providers/osu#options "헤딩으로 바로 가기")

**osu! Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [osu! Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/osu.ts)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

참고

osu!는 사용자 이메일을 **제공하지 않습니다**!

## 예제[​](https://next-auth.js.org/providers/osu#example "헤딩으로 바로 가기")

```
    import OsuProvider from "next-auth/providers/osu";
    ...
    providers: [
      OsuProvider({
        clientId: process.env.OSU_CLIENT_ID,
        clientSecret: process.env.OSU_CLIENT_SECRET
      })
    ]
    ...

```
