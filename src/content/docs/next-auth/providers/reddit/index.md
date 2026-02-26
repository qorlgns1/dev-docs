---
title: "Reddit"
description: "!next-auth-reddit-provider-config"
---

Source URL: https://next-auth.js.org/providers/reddit

# Reddit | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/reddit#documentation "Direct link to heading")

<https://www.reddit.com/dev/api/>

## 앱 구성[​](https://next-auth.js.org/providers/reddit#app-configuration "Direct link to heading")

1. <https://www.reddit.com/prefs/apps/>에 접속해 새 웹 앱을 생성합니다.
2. 웹 앱 이름을 입력합니다.
3. `/api/auth/callback/reddit`로 끝나는 redirect uri를 입력합니다:

![next-auth-reddit-provider-config](https://user-images.githubusercontent.com/200280/185804449-88f8d0f2-35fa-4eb5-8ecc-5e0a6c813954.png)

4. 나머지 필드는 모두 선택 사항입니다.
5. "create app" 버튼을 클릭합니다.

## 옵션[​](https://next-auth.js.org/providers/reddit#options "Direct link to heading")

**Reddit Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Reddit Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/reddit.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/reddit#example "Direct link to heading")

```
    import RedditProvider from "next-auth/providers/reddit";
    ...
    providers: [
      RedditProvider({
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET
      })
    ]
    ...

```

danger

Reddit은 해당 페이지를 거칠 때마다 매번 인증을 요구합니다.

danger

Client ID / Client Secret당 callback URL은 하나만 허용됩니다.

tip

이 Provider 템플릿에는 1시간짜리 access token만 있으며 "identity" scope만 포함됩니다. refresh token도 받으려면 다음을 따라야 합니다:

```
    providers: [
      RedditProvider({
        clientId: process.env.REDDIT_CLIENT_ID,
        clientSecret: process.env.REDDIT_CLIENT_SECRET,
        authorization: {
          params: {
            duration: "permanent",
          },
        },
      }),
    ]

```
