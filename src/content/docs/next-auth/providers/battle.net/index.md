---
title: "Battle.net"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/battle.net

# Battle.net | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/battle.net#documentation "Direct link to heading")

<https://develop.battle.net/documentation/guides/using-oauth>

## 구성[​](https://next-auth.js.org/providers/battle.net#configuration "Direct link to heading")

<https://develop.battle.net/access/clients>

## 옵션[​](https://next-auth.js.org/providers/battle.net#options "Direct link to heading")

**Battle.net Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Battle.net Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/battlenet.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/battle.net#example "Direct link to heading")

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

[사용 가능한 지역](https://develop.battle.net/documentation/guides/regionality-and-apis)을 기준으로 `issuer`는 다음 값 중 하나여야 합니다.

```
    type BattleNetIssuer =
      | "https://www.battlenet.com.cn/oauth"
      | "https://us.battle.net/oauth"
      | "https://eu.battle.net/oauth"
      | "https://kr.battle.net/oauth"
      | "https://tw.battle.net/oauth"

```
