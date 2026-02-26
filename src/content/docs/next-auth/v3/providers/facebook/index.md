---
title: "Facebook"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/facebook

# Facebook | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/facebook#documentation "Direct link to heading")

<https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/>

## 구성[​](https://next-auth.js.org/v3/providers/facebook#configuration "Direct link to heading")

<https://developers.facebook.com/apps/>

## 옵션[​](https://next-auth.js.org/v3/providers/facebook#options "Direct link to heading")

**Facebook Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Facebook Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/facebook.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/facebook#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Facebook({
        clientId: process.env.FACEBOOK_CLIENT_ID,
        clientSecret: process.env.FACEBOOK_CLIENT_SECRET
      })
    ]
    ...

```

tip

프로덕션 애플리케이션에서는 Facebook 로그인에 localhost URL을 사용할 수 없습니다. **localhost** 콜백 URL을 사용하려면 Facebook에서 별도의 개발용 애플리케이션을 사용해야 합니다.

tip

모바일에서 생성된 계정의 경우 이메일 주소가 반환되지 않을 수 있습니다.
