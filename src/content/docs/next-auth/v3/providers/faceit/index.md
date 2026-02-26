---
title: "FACEIT"
description: "기본 정보(email, nickname, guid, avatar)를 얻기 위한 scopes: , ,"
---

Source URL: https://next-auth.js.org/v3/providers/faceit

# FACEIT | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/faceit#documentation "Direct link to heading")

<https://cdn.faceit.com/third_party/docs/FACEIT_Connect_3.0.pdf>

## 설정[​](https://next-auth.js.org/v3/providers/faceit#configuration "Direct link to heading")

<https://developers.faceit.com/apps>

Grant type: `Authorization Code`

기본 정보(email, nickname, guid, avatar)를 얻기 위한 scopes: `openid`, `email`, `profile`

## 옵션[​](https://next-auth.js.org/v3/providers/faceit#options "Direct link to heading")

**FACEIT Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [FACEIT Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/faceit.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/faceit#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.FACEIT({
        clientId: process.env.FACEIT_CLIENT_ID,
        clientSecret: process.env.FACEIT_CLIENT_SECRET
      })
    ]
    ...

```
