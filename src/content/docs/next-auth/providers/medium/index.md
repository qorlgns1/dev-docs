---
title: "Medium"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/medium

# Medium | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/medium#documentation "제목으로 바로 가는 링크")

<https://github.com/Medium/medium-api-docs>

## 구성[​](https://next-auth.js.org/providers/medium#configuration "제목으로 바로 가는 링크")

<https://medium.com/me/applications>

## 옵션[​](https://next-auth.js.org/providers/medium#options "제목으로 바로 가는 링크")

**Medium Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Medium Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/medium.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/medium#example "제목으로 바로 가는 링크")

```
    import MediumProvider from "next-auth/providers/medium";
    ...
    providers: [
      MediumProvider({
        clientId: process.env.MEDIUM_CLIENT_ID,
        clientSecret: process.env.MEDIUM_CLIENT_SECRET
      })
    }
    ...

```

danger

Medium API에서는 이메일 주소를 반환하지 않습니다.
