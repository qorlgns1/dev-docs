---
title: "Naver"
description: "사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/naver

# Naver | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/naver#documentation "Direct link to heading")

<https://developers.naver.com/docs/login/overview/overview.md>

## 구성[​](https://next-auth.js.org/v3/providers/naver#configuration "Direct link to heading")

<https://developers.naver.com/docs/login/api/api.md>

## 옵션[​](https://next-auth.js.org/v3/providers/naver#options "Direct link to heading")

**Naver Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Naver Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/naver.js)

사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/naver#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Naver({
        clientId: process.env.NAVER_CLIENT_ID,
        clientSecret: process.env.NAVER_CLIENT_SECRET
      })
    ]
    ...

```
