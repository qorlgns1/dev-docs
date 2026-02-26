---
title: "Discord"
description: "The Discord Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/discord

# Discord | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/discord#documentation "Direct link to heading")

<https://discord.com/developers/docs/topics/oauth2>

## Configuration[​](https://next-auth.js.org/v3/providers/discord#configuration "Direct link to heading")

<https://discord.com/developers/applications>

## Options[​](https://next-auth.js.org/v3/providers/discord#options "Direct link to heading")

The **Discord Provider** comes with a set of default options:

- [Discord Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/discord.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/discord#example "Direct link to heading")

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
