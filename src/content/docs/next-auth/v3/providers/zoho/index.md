---
title: "Zoho"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/zoho

# Zoho | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/zoho#documentation "Direct link to heading")

<https://www.zoho.com/accounts/protocol/oauth/web-server-applications.html>

## 설정[​](https://next-auth.js.org/v3/providers/zoho#configuration "Direct link to heading")

<https://api-console.zoho.com/>

## 옵션[​](https://next-auth.js.org/v3/providers/zoho#options "Direct link to heading")

**Zoho Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Zoho Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/zoho.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/zoho#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Zoho({
        clientId: process.env.ZOHO_CLIENT_ID,
        clientSecret: process.env.ZOHO_CLIENT_SECRET
      })
    ]
    ...

```
