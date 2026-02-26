---
title: "GitHub"
description: "원본 URL: https://next-auth.js.org/v3/providers/github"
---

원본 URL: https://next-auth.js.org/v3/providers/github

# GitHub | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/github#documentation "Direct link to heading")

<https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps>

## 구성[​](https://next-auth.js.org/v3/providers/github#configuration "Direct link to heading")

<https://github.com/settings/apps>

## 옵션[​](https://next-auth.js.org/v3/providers/github#options "Direct link to heading")

**Github Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Github Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/github.ts)

자체 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/github#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.GitHub({
        clientId: process.env.GITHUB_CLIENT_ID,
        clientSecret: process.env.GITHUB_CLIENT_SECRET
      })
    ]
    ...

```

danger

Client ID / Client Secret당 콜백 URL은 하나만 허용됩니다.

tip

개인정보 보호 설정이 활성화되어 있으면 이메일 주소는 반환되지 않습니다.
