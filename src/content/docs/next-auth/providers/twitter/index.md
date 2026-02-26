---
title: "Twitter"
description: "Twitter는 현재 OAuth 1.0 사양을 사용하는 유일한 내장 Provider입니다. 즉,  또는 을 받는 대신 각각 과 을 받게 됩니다. Adapter를 사용하는 경우를 대비해, 데이터베이스 스키마에 이 값들도 추가해 두세요."
---

원문 URL: https://next-auth.js.org/providers/twitter

# Twitter | NextAuth.js

버전: v4

Twitter는 현재 OAuth 1.0 사양을 사용하는 유일한 내장 Provider입니다. 즉, `access_token` 또는 `refresh_token`을 받는 대신 각각 `oauth_token`과 `oauth_token_secret`을 받게 됩니다. [Adapter](https://authjs.dev/getting-started/database)를 사용하는 경우를 대비해, 데이터베이스 스키마에 이 값들도 추가해 두세요.

## 문서[​](https://next-auth.js.org/providers/twitter#documentation "Direct link to heading")

<https://developer.twitter.com>

## 구성[​](https://next-auth.js.org/providers/twitter#configuration "Direct link to heading")

<https://developer.twitter.com/en/apps>

## 옵션[​](https://next-auth.js.org/providers/twitter#options "Direct link to heading")

**Twitter Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Twitter Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/twitter.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/twitter#example "Direct link to heading")

```
    import TwitterProvider from "next-auth/providers/twitter";
    ...
    providers: [
      TwitterProvider({
        clientId: process.env.TWITTER_CLIENT_ID,
        clientSecret: process.env.TWITTER_CLIENT_SECRET
      })
    ]
    ...

```

팁

사용자 이메일 주소를 가져오려면 앱 권한에서 _"Request email address from users"_ 옵션을 활성화해야 합니다.

![twitter](https://user-images.githubusercontent.com/55143799/168702338-a95912a7-b689-4680-aa2c-6306fe3c2ec7.jpeg)

## OAuth 2.0[​](https://next-auth.js.org/providers/twitter#oauth-20 "Direct link to heading")

Twitter는 OAuth 2를 지원하며, 현재는 opt-in 방식입니다. 활성화하려면 Provider 구성에 `version: "2.0"`만 추가하면 됩니다:

```
    TwitterProvider({
      clientId: process.env.TWITTER_ID,
      clientSecret: process.env.TWITTER_SECRET,
      version: "2.0", // opt-in to Twitter OAuth 2.0
    })

```

이 변경은 간단하지만, [Twitter APIs](https://developer.twitter.com/en/docs/api-reference-index)와 상호작용할 수 있는 방식과 범위가 달라진다는 점을 유의하세요. 자세한 내용은 공식 [Twitter OAuth 2 문서](https://developer.twitter.com/en/docs/authentication/oauth-2-0)를 확인하세요.

참고

이메일은 현재 Twitter OAuth 2.0에서 지원되지 않습니다.
