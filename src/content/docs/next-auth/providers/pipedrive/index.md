---
title: "Pipedrive"
description: "각 옵션은 사용 사례에 맞게 원하는 대로 재정의할 수 있습니다."
---

출처 URL: https://next-auth.js.org/providers/pipedrive

# Pipedrive | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/pipedrive#documentation "Direct link to heading")

<https://pipedrive.readme.io/docs/marketplace-oauth-authorization>

## 옵션[​](https://next-auth.js.org/providers/pipedrive#options "Direct link to heading")

**Pipedrive Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Pipedrive Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/pipedrive.ts)

각 옵션은 사용 사례에 맞게 원하는 대로 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/pipedrive#example "Direct link to heading")

```
    import PipedriveProvider from "next-auth/providers/pipedrive";
    ...
    providers: [
      PipedriveProvider({
        clientId: process.env.PIPEDRIVE_CLIENT_ID,
        clientSecret: process.env.PIPEDRIVE_CLIENT_SECRET,
      })
    ]
    ...

```
