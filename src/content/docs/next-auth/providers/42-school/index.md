---
title: "42 School"
description: "원본 URL: https://next-auth.js.org/providers/42-school"
---

원본 URL: https://next-auth.js.org/providers/42-school

# 42 School | NextAuth.js

버전: v4

참고

42는 `Account`에 `created_at`이라는 필드를 반환하며, 이 값은 숫자입니다. [docs](https://api.intra.42.fr/apidoc/guides/getting_started#make-basic-requests)를 참고하세요. [Adapter](https://next-auth.js.org/adapters)를 사용하는 경우 이 필드를 데이터베이스 스키마에 반드시 추가하세요.

## 문서[​](https://next-auth.js.org/providers/42-school#documentation "Direct link to heading")

<https://api.intra.42.fr/apidoc/guides/web_application_flow>

## 구성[​](https://next-auth.js.org/providers/42-school#configuration "Direct link to heading")

<https://profile.intra.42.fr/oauth/applications/new>

## 옵션[​](https://next-auth.js.org/providers/42-school#options "Direct link to heading")

**42 School Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [42 School Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/42-school.ts)

옵션은 사용 사례에 맞게 원하는 대로 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/42-school#example "Direct link to heading")

```
    import FortyTwoProvider from "next-auth/providers/42-school";
    ...
    providers: [
      FortyTwoProvider({
        clientId: process.env.FORTY_TWO_CLIENT_ID,
        clientSecret: process.env.FORTY_TWO_CLIENT_SECRET
      })
    ]
    ...

```
