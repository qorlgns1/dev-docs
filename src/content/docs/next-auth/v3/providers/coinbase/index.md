---
title: "Coinbase"
description: "자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/coinbase

# Coinbase | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/coinbase#documentation "Direct link to heading")

<https://developers.coinbase.com/api/v2>

## 구성[​](https://next-auth.js.org/v3/providers/coinbase#configuration "Direct link to heading")

<https://www.coinbase.com/settings/api>

## 옵션[​](https://next-auth.js.org/v3/providers/coinbase#options "Direct link to heading")

**Coinbase Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Coinbase Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/coinbase.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/coinbase#example "Direct link to heading")

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

팁

이 Provider 템플릿에는 2시간짜리 액세스 토큰이 포함되어 있습니다. 리프레시 토큰도 함께 반환됩니다.
