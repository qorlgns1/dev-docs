---
title: "Twitch"
description: "Add the following redirect URL into the console"
---

Source URL: https://next-auth.js.org/v3/providers/twitch

# Twitch | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/twitch#documentation "Direct link to heading")

<https://dev.twitch.tv/docs/authentication>

## Configuration[​](https://next-auth.js.org/v3/providers/twitch#configuration "Direct link to heading")

<https://dev.twitch.tv/console/apps>

Add the following redirect URL into the console `http://<your-next-app-url>/api/auth/callback/twitch`

## Options[​](https://next-auth.js.org/v3/providers/twitch#options "Direct link to heading")

The **Twitch Provider** comes with a set of default options:

- [Twitch Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/twitch.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/twitch#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Twitch({
        clientId: process.env.TWITCH_CLIENT_ID,
        clientSecret: process.env.TWITCH_CLIENT_SECRET
      })
    ]
    ...

```
