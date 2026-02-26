---
title: "Yandex"
description: "The Yandex Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/yandex

# Yandex | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/yandex#documentation "Direct link to heading")

<https://tech.yandex.com/oauth/doc/dg/concepts/about-docpage/>

## Configuration[​](https://next-auth.js.org/v3/providers/yandex#configuration "Direct link to heading")

<https://oauth.yandex.com/client/new>

## Options[​](https://next-auth.js.org/v3/providers/yandex#options "Direct link to heading")

The **Yandex Provider** comes with a set of default options:

- [Yandex Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/yandex.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/yandex#example "Direct link to heading")

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
