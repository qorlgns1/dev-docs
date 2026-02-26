---
title: "Discord"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/discord

# Discord | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/discord#documentation "Direct link to heading")

<https://discord.com/developers/docs/topics/oauth2>

## 구성[​](https://next-auth.js.org/providers/discord#configuration "Direct link to heading")

<https://discord.com/developers/applications>

## 옵션[​](https://next-auth.js.org/providers/discord#options "Direct link to heading")

**Discord Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Discord Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/discord.ts)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/discord#example "Direct link to heading")

```
    import DiscordProvider from "next-auth/providers/discord";
    ...
    providers: [
      DiscordProvider({
        clientId: process.env.DISCORD_CLIENT_ID,
        clientSecret: process.env.DISCORD_CLIENT_SECRET
      })
    ]
    ...

```
