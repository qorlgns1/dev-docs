---
title: '문서[​](https://next-auth.js.org/v3/providers/box#documentation "Direct link to heading")'
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/box

# Box | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/box#documentation "Direct link to heading")

<https://developer.box.com/reference/>

## 구성[​](https://next-auth.js.org/v3/providers/box#configuration "Direct link to heading")

<https://developer.box.com/guides/sso-identities-and-app-users/connect-okta-to-app-users/configure-box/>

## 옵션[​](https://next-auth.js.org/v3/providers/box#options "Direct link to heading")

**Box Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Box Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/box.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/box#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Box({
        clientId: process.env.BOX_CLIENT_ID,
        clientSecret: process.env.BOX_CLIENT_SECRET
      })
    ]
    ...

```
