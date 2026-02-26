---
title: "FACEIT"
description: "기본 정보(email, nickname, guid, avatar)를 얻기 위한 Scopes: , ,"
---

소스 URL: https://next-auth.js.org/providers/faceit

# FACEIT | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/faceit#documentation "Direct link to heading")

<https://cdn.faceit.com/third_party/docs/FACEIT_Connect_3.0.pdf>

## 구성[​](https://next-auth.js.org/providers/faceit#configuration "Direct link to heading")

<https://developers.faceit.com/apps>

Grant type: `Authorization Code`

기본 정보(email, nickname, guid, avatar)를 얻기 위한 Scopes: `openid`, `email`, `profile`

## 옵션[​](https://next-auth.js.org/providers/faceit#options "Direct link to heading")

**FACEIT Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [FACEIT Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/faceit.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/faceit#example "Direct link to heading")

```
    import FaceItProvider from "next-auth/providers/faceit";
    ...
    providers: [
      FaceItProvider({
        clientId: process.env.FACEIT_CLIENT_ID,
        clientSecret: process.env.FACEIT_CLIENT_SECRET
      })
    ]
    ...

```
