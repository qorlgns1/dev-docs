---
title: "Netlify"
description: "자체 사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/netlify

# Netlify | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/netlify#documentation "제목으로 바로 가는 링크")

<https://www.netlify.com/blog/2016/10/10/integrating-with-netlify-oauth2/>

## 구성[​](https://next-auth.js.org/v3/providers/netlify#configuration "제목으로 바로 가는 링크")

<https://github.com/netlify/netlify-oauth-example>

## 옵션[​](https://next-auth.js.org/v3/providers/netlify#options "제목으로 바로 가는 링크")

**Netlify Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Netlify Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/netlify.js)

자체 사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/netlify#example "제목으로 바로 가는 링크")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Netlify({
        clientId: process.env.NETLIFY_CLIENT_ID,
        clientSecret: process.env.NETLIFY_CLIENT_SECRET
      })
    ]
    ...

```
