---
title: "Discord"
description: "원본 URL: https://next-auth.js.org/v3/providers/discord"
---

원본 URL: https://next-auth.js.org/v3/providers/discord

# Discord | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/discord#documentation "Direct link to heading")

<https://discord.com/developers/docs/topics/oauth2>

## 구성[​](https://next-auth.js.org/v3/providers/discord#configuration "Direct link to heading")

<https://discord.com/developers/applications>

## 옵션[​](https://next-auth.js.org/v3/providers/discord#options "Direct link to heading")

**Discord Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Discord Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/discord.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/discord#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Discord({
        clientId: process.env.DISCORD_CLIENT_ID,
        clientSecret: process.env.DISCORD_CLIENT_SECRET
      })
    ]
    ...

```
