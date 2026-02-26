---
title: "Instagram"
description: "원본 URL: https://next-auth.js.org/v3/providers/instagram"
---

원본 URL: https://next-auth.js.org/v3/providers/instagram

# Instagram | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/instagram#documentation "Direct link to heading")

<https://developers.facebook.com/docs/instagram-basic-display-api/getting-started>

## 구성[​](https://next-auth.js.org/v3/providers/instagram#configuration "Direct link to heading")

<https://developers.facebook.com/apps/>

## 옵션[​](https://next-auth.js.org/v3/providers/instagram#options "Direct link to heading")

**Instagram Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Instagram Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/instagram.js)

각 옵션은 사용 사례에 맞게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/instagram#example "Direct link to heading")

```
    // pages/api/auth/[...nextauth].js
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Instagram({
        clientId: process.env.INSTAGRAM_CLIENT_ID,
        clientSecret: process.env.INSTAGRAM_CLIENT_SECRET
      })
    ]
    ...
    // pages/index.jsx
    import { signIn } from "next-auth/client"
    ...
    <button onClick={() => signIn("instagram")}>
      Sign in
    </button>
    ...

```

danger

Instagram API는 이메일 주소를 반환하지 않습니다.

tip

Instagram display app에서는 Facebook 앱에 callback URL을 구성해야 하며, Facebook은 localhost에서도 **https** 사용을 요구합니다. 이를 위해서는 [localhost에 SSL을 추가](https://www.freecodecamp.org/news/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec/)하거나 [ngrok](https://ngrok.com/docs) 같은 프록시를 사용해야 합니다.
