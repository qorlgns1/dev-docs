---
title: "Medium"
description: "자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/v3/providers/medium

# Medium | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/medium#documentation "Direct link to heading")

<https://github.com/Medium/medium-api-docs>

## 설정[​](https://next-auth.js.org/v3/providers/medium#configuration "Direct link to heading")

<https://medium.com/me/applications>

## 옵션[​](https://next-auth.js.org/v3/providers/medium#options "Direct link to heading")

**Medium Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Medium Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/medium.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/medium#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Medium({
        clientId: process.env.MEDIUM_CLIENT_ID,
        clientSecret: process.env.MEDIUM_CLIENT_SECRET
      })
    }
    ...

```

danger

이메일 주소는 Medium API에서 반환되지 않습니다.
