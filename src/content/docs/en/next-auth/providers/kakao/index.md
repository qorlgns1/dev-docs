---
title: "Kakao"
description: "The Kakao Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/kakao

# Kakao | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/kakao#documentation "Direct link to heading")

<https://developers.kakao.com/product/kakaoLogin>

## Configuration[​](https://next-auth.js.org/providers/kakao#configuration "Direct link to heading")

<https://developers.kakao.com/docs/latest/en/kakaologin/common>

## Options[​](https://next-auth.js.org/providers/kakao#options "Direct link to heading")

The **Kakao Provider** comes with a set of default options:

- [Kakao Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/kakao.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/kakao#example "Direct link to heading")

```
    import KakaoProvider from "next-auth/providers/kakao";
    ...
    providers: [
      KakaoProvider({
        clientId: process.env.KAKAO_CLIENT_ID,
        clientSecret: process.env.KAKAO_CLIENT_SECRET
      })
    ]
    ...

```

## Instructions[​](https://next-auth.js.org/providers/kakao#instructions "Direct link to heading")

### Configuration[​](https://next-auth.js.org/providers/kakao#configuration-1 "Direct link to heading")

Create a provider and a Kakao application at `https://developers.kakao.com/console/app`. In the settings of the app under Kakao Login, activate web app, change consent items and configure callback URL.
