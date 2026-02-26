---
title: "Battle.net"
description: "The Battle.net Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/battle.net

# Battle.net | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/battle.net#documentation "Direct link to heading")

<https://develop.battle.net/documentation/guides/using-oauth>

## Configuration[​](https://next-auth.js.org/v3/providers/battle.net#configuration "Direct link to heading")

<https://develop.battle.net/access/clients>

## Options[​](https://next-auth.js.org/v3/providers/battle.net#options "Direct link to heading")

The **Battle.net Provider** comes with a set of default options:

- [Battle.net Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/battlenet.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/battle.net#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.BattleNet({
        clientId: process.env.BATTLENET_CLIENT_ID,
        clientSecret: process.env.BATTLENET_CLIENT_SECRET,
        region: process.env.BATTLENET_REGION
      })
    ]
    ...

```
