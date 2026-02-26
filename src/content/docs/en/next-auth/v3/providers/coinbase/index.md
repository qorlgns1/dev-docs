---
title: "Coinbase"
description: "The Coinbase Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/coinbase

# Coinbase | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/coinbase#documentation "Direct link to heading")

<https://developers.coinbase.com/api/v2>

## Configuration[​](https://next-auth.js.org/v3/providers/coinbase#configuration "Direct link to heading")

<https://www.coinbase.com/settings/api>

## Options[​](https://next-auth.js.org/v3/providers/coinbase#options "Direct link to heading")

The **Coinbase Provider** comes with a set of default options:

- [Coinbase Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/coinbase.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/coinbase#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Coinbase({
        clientId: process.env.COINBASE_CLIENT_ID,
        clientSecret: process.env.COINBASE_CLIENT_SECRET
      })
    ]
    ...

```

tip

This Provider template has a 2 hour access token to it. A refresh token is also returned.
