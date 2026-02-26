---
title: "Reddit"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/reddit

# Reddit | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/reddit#documentation "Direct link to heading")

<https://www.reddit.com/dev/api/>

## 구성[​](https://next-auth.js.org/v3/providers/reddit#configuration "Direct link to heading")

<https://www.reddit.com/prefs/apps/>

## 옵션[​](https://next-auth.js.org/v3/providers/reddit#options "Direct link to heading")

**Reddit Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Reddit Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/reddit.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/reddit#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Reddit({
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET
      })
    ]
    ...

```

danger

Reddit는 해당 페이지를 거칠 때마다 매번 인증을 요구합니다.

danger

Client ID / Client Secret당 콜백 URL은 하나만 허용됩니다.

tip

이 Provider 템플릿은 1시간짜리 액세스 토큰만 가지며 'identity' 스코프만 포함합니다. refresh token도 받으려면 다음을 따라야 합니다:

```
    providers: [
      {
        id: "reddit",
        name: "Reddit",
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET,
        scope: "identity mysubreddits read", //Check Reddit API Documentation for more. The identity scope is required.
        type: "oauth",
        version: "2.0",
        params: { grant_type: "authorization_code" },
        accessTokenUrl: " https://www.reddit.com/api/v1/access_token",
        authorizationUrl:
          "https://www.reddit.com/api/v1/authorize?response_type=code&duration=permanent",
        profileUrl: "https://oauth.reddit.com/api/v1/me",
        profile: (profile) => {
          return {
            id: profile.id,
            name: profile.name,
            email: null,
          }
        },
      },
    ]

```
