---
title: "Battle.net"
description: "자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/battle.net

# Battle.net | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/battle.net#documentation "Direct link to heading")

<https://develop.battle.net/documentation/guides/using-oauth>

## 구성[​](https://next-auth.js.org/v3/providers/battle.net#configuration "Direct link to heading")

<https://develop.battle.net/access/clients>

## 옵션[​](https://next-auth.js.org/v3/providers/battle.net#options "Direct link to heading")

**Battle.net Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Battle.net Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/battlenet.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/battle.net#example "Direct link to heading")

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
