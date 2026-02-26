---
title: "Battle.net"
description: "The Battle.net Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/battle.net

# Battle.net | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/battle.net#documentation "Direct link to heading")

<https://develop.battle.net/documentation/guides/using-oauth>

## Configuration[​](https://next-auth.js.org/providers/battle.net#configuration "Direct link to heading")

<https://develop.battle.net/access/clients>

## Options[​](https://next-auth.js.org/providers/battle.net#options "Direct link to heading")

The **Battle.net Provider** comes with a set of default options:

- [Battle.net Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/battlenet.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/battle.net#example "Direct link to heading")

```
    import BattleNetProvider from "next-auth/providers/battlenet";
    ...
    providers: [
      BattleNetProvider({
        clientId: process.env.BATTLENET_CLIENT_ID,
        clientSecret: process.env.BATTLENET_CLIENT_SECRET,
        issuer: process.env.BATTLENET_ISSUER
      })
    ]
    ...

```

`issuer` must be one of these values, based on the [available regions](https://develop.battle.net/documentation/guides/regionality-and-apis):

```
    type BattleNetIssuer =
      | "https://www.battlenet.com.cn/oauth"
      | "https://us.battle.net/oauth"
      | "https://eu.battle.net/oauth"
      | "https://kr.battle.net/oauth"
      | "https://tw.battle.net/oauth"

```
