---
title: "Salesforce"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/salesforce

# Salesforce | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/salesforce#documentation "Direct link to heading")

[https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5)

## 옵션[​](https://next-auth.js.org/providers/salesforce#options "Direct link to heading")

**Salesforce Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Salesforce Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/salesforce.ts)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/salesforce#example "Direct link to heading")

```
    import SalesforceProvider from "next-auth/providers/salesforce";
    ...
    providers: [
      SalesforceProvider({
        clientId: process.env.SALESFORCE_CLIENT_ID,
        clientSecret: process.env.SALESFORCE_CLIENT_SECRET,
      })
    ]
    ...

```
