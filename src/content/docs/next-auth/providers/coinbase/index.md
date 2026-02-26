---
title: "Coinbase"
description: "원본 URL: https://next-auth.js.org/providers/coinbase"
---

원본 URL: https://next-auth.js.org/providers/coinbase

# Coinbase | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/coinbase#documentation "제목으로 바로 가는 링크")

<https://developers.coinbase.com/api/v2>

## 구성[​](https://next-auth.js.org/providers/coinbase#configuration "제목으로 바로 가는 링크")

<https://www.coinbase.com/settings/api>

## 옵션[​](https://next-auth.js.org/providers/coinbase#options "제목으로 바로 가는 링크")

**Coinbase Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Coinbase Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/coinbase.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/coinbase#example "제목으로 바로 가는 링크")

```
    import CoinbaseProvider from "next-auth/providers/coinbase";
    ...
    providers: [
      CoinbaseProvider({
        clientId: process.env.COINBASE_CLIENT_ID,
        clientSecret: process.env.COINBASE_CLIENT_SECRET
      })
    ]
    ...

```

팁

이 Provider 템플릿에는 2시간짜리 access token이 있습니다. refresh token도 함께 반환됩니다.
