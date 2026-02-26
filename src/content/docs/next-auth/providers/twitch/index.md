---
title: "Twitch"
description: "다음 리디렉션 URL을 콘솔에 추가하세요"
---

Source URL: https://next-auth.js.org/providers/twitch

# Twitch | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/twitch#documentation "Direct link to heading")

<https://dev.twitch.tv/docs/authentication>

## 구성[​](https://next-auth.js.org/providers/twitch#configuration "Direct link to heading")

<https://dev.twitch.tv/console/apps>

다음 리디렉션 URL을 콘솔에 추가하세요 `http://<your-next-app-url>/api/auth/callback/twitch`

## 옵션[​](https://next-auth.js.org/providers/twitch#options "Direct link to heading")

**Twitch Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Twitch Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/twitch.ts)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/twitch#example "Direct link to heading")

```
    import TwitchProvider from "next-auth/providers/twitch";
    ...
    providers: [
      TwitchProvider({
        clientId: process.env.TWITCH_CLIENT_ID,
        clientSecret: process.env.TWITCH_CLIENT_SECRET
      })
    ]
    ...

```
