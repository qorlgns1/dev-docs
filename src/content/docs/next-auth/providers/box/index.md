---
title: '문서[\u200b](https://next-auth.js.org/providers/box#documentation "헤딩으로 직접 연결되는 링크")'
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/box

# Box | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/box#documentation "헤딩으로 직접 연결되는 링크")

<https://developer.box.com/reference/>

## 구성[​](https://next-auth.js.org/providers/box#configuration "헤딩으로 직접 연결되는 링크")

<https://developer.box.com/guides/sso-identities-and-app-users/connect-okta-to-app-users/configure-box/>

## 옵션[​](https://next-auth.js.org/providers/box#options "헤딩으로 직접 연결되는 링크")

**Box Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Box Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/box.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/box#example "헤딩으로 직접 연결되는 링크")

```
    import BoxProvider from "next-auth/providers/box";
    ...
    providers: [
      BoxProvider({
        clientId: process.env.BOX_CLIENT_ID,
        clientSecret: process.env.BOX_CLIENT_SECRET
      })
    ]
    ...

```
