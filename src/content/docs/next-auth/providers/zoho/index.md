---
title: "Zoho"
description: "Zoho는 에 문자열 타입의 이라는 필드를 반환합니다. 해당 내용은 docs를 참고하세요. Adapter를 사용 중이라면 데이터베이스 스키마에 이 필드를 추가하는 것을 잊지 마세요."
---

Source URL: https://next-auth.js.org/providers/zoho

# Zoho | NextAuth.js

버전: v4

참고

Zoho는 `Account`에 문자열 타입의 `api_domain`이라는 필드를 반환합니다. 해당 내용은 [docs](https://www.zoho.com/accounts/protocol/oauth/web-apps/access-token.html)를 참고하세요. [Adapter](https://next-auth.js.org/adapters)를 사용 중이라면 데이터베이스 스키마에 이 필드를 추가하는 것을 잊지 마세요.

## 문서[​](https://next-auth.js.org/providers/zoho#documentation "Direct link to heading")

<https://www.zoho.com/accounts/protocol/oauth/web-server-applications.html>

## 구성[​](https://next-auth.js.org/providers/zoho#configuration "Direct link to heading")

<https://api-console.zoho.com/>

## 옵션[​](https://next-auth.js.org/providers/zoho#options "Direct link to heading")

**Zoho Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Zoho Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/zoho.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/zoho#example "Direct link to heading")

```
    import ZohoProvider from "next-auth/providers/zoho";
    ...
    providers: [
      ZohoProvider({
        clientId: process.env.ZOHO_CLIENT_ID,
        clientSecret: process.env.ZOHO_CLIENT_SECRET
      })
    ]
    ...

```
