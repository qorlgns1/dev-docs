---
title: "42 School"
description: "자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/v3/providers/42-school

# 42 School | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/42-school#documentation "Direct link to heading")

<https://api.intra.42.fr/apidoc/guides/web_application_flow>

## 설정[​](https://next-auth.js.org/v3/providers/42-school#configuration "Direct link to heading")

<https://profile.intra.42.fr/oauth/applications/new>

## 옵션[​](https://next-auth.js.org/v3/providers/42-school#options "Direct link to heading")

**42 School Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [42 School Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/42.js)

자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/42-school#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.FortyTwo({
        clientId: process.env.FORTY_TWO_CLIENT_ID,
        clientSecret: process.env.FORTY_TWO_CLIENT_SECRET
      })
    ]
    ...

```
