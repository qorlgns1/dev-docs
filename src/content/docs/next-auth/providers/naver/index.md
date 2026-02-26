---
title: "Naver"
description: "원본 URL: https://next-auth.js.org/providers/naver"
---

원본 URL: https://next-auth.js.org/providers/naver

# Naver | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/naver#documentation "헤딩으로 바로 가기 링크")

<https://developers.naver.com/docs/login/overview/overview.md>

## 설정[​](https://next-auth.js.org/providers/naver#configuration "헤딩으로 바로 가기 링크")

<https://developers.naver.com/docs/login/api/api.md>

## 옵션[​](https://next-auth.js.org/providers/naver#options "헤딩으로 바로 가기 링크")

**Naver Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Naver Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/naver.ts)

원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/naver#example "헤딩으로 바로 가기 링크")

```
    import NaverProvider from "next-auth/providers/naver";
    ...
    providers: [
      NaverProvider({
        clientId: process.env.NAVER_CLIENT_ID,
        clientSecret: process.env.NAVER_CLIENT_SECRET
      })
    ]
    ...

```
