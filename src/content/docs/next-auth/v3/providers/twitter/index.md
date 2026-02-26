---
title: "Twitter"
description: "자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/v3/providers/twitter

# Twitter | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/twitter#documentation "Direct link to heading")

<https://developer.twitter.com>

## 구성[​](https://next-auth.js.org/v3/providers/twitter#configuration "Direct link to heading")

<https://developer.twitter.com/en/apps>

## 옵션[​](https://next-auth.js.org/v3/providers/twitter#options "Direct link to heading")

**Twitter Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Twitter Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/twitter.js)

자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/twitter#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Twitter({
        clientId: process.env.TWITTER_CLIENT_ID,
        clientSecret: process.env.TWITTER_CLIENT_SECRET
      })
    ]
    ...

```

tip

사용자 이메일 주소를 얻으려면 앱 권한에서 _"Request email address from users"_ 옵션을 반드시 활성화해야 합니다.

![twitter](https://user-images.githubusercontent.com/7902980/83944068-1640ca80-a801-11ea-959c-0e744e2144f7.PNG)
