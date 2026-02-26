---
title: "Salesforce"
description: "원본 URL: https://next-auth.js.org/v3/providers/salesforce"
---

원본 URL: https://next-auth.js.org/v3/providers/salesforce

# Salesforce | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/salesforce#documentation "Direct link to heading")

[https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5)

## 옵션[​](https://next-auth.js.org/v3/providers/salesforce#options "Direct link to heading")

**Salesforce Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Salesforce Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/salesforce.js)

각 옵션은 사용 사례에 맞게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/salesforce#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Salesforce({
        clientId: process.env.SALESFORCE_CLIENT_ID,
        clientSecret: process.env.SALESFORCE_CLIENT_SECRET,
      })
    ]
    ...

```
