---
title: "Netlify"
description: "자체 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

출처 URL: https://next-auth.js.org/providers/netlify

# Netlify | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/netlify#documentation "Direct link to heading")

<https://www.netlify.com/blog/2016/10/10/integrating-with-netlify-oauth2/>

## 구성[​](https://next-auth.js.org/providers/netlify#configuration "Direct link to heading")

<https://github.com/netlify/netlify-oauth-example>

## 옵션[​](https://next-auth.js.org/providers/netlify#options "Direct link to heading")

**Netlify Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Netlify Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/netlify.js)

자체 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/netlify#example "Direct link to heading")

```
    import NetlifyProvider from "next-auth/providers/netlify";
    ...
    providers: [
      NetlifyProvider({
        clientId: process.env.NETLIFY_CLIENT_ID,
        clientSecret: process.env.NETLIFY_CLIENT_SECRET
      })
    ]
    ...

```
