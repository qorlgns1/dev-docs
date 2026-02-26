---
title: "Facebook"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/providers/facebook

# Facebook | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/facebook#documentation "제목으로 바로 가기")

<https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/>

## 구성[​](https://next-auth.js.org/providers/facebook#configuration "제목으로 바로 가기")

<https://developers.facebook.com/apps/>

## 옵션[​](https://next-auth.js.org/providers/facebook#options "제목으로 바로 가기")

**Facebook Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Facebook Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/facebook.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/facebook#example "제목으로 바로 가기")

```
    import FacebookProvider from "next-auth/providers/facebook";
    ...
    providers: [
      FacebookProvider({
        clientId: process.env.FACEBOOK_CLIENT_ID,
        clientSecret: process.env.FACEBOOK_CLIENT_SECRET
      })
    ]
    ...

```

tip

프로덕션 애플리케이션에서는 Facebook 로그인에 localhost URL을 사용할 수 없습니다. **localhost** callback URL을 사용하려면 Facebook에서 전용 개발 애플리케이션을 사용해야 합니다.

tip

모바일에서 생성된 계정의 경우 이메일 주소가 반환되지 않을 수 있습니다.
