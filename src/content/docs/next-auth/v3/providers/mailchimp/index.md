---
title: "Mailchimp"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/mailchimp

# Mailchimp | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/mailchimp#documentation "Direct link to heading")

<https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/>

## 구성[​](https://next-auth.js.org/v3/providers/mailchimp#configuration "Direct link to heading")

<https://admin.mailchimp.com/account/oauth2/client/>

## 옵션[​](https://next-auth.js.org/v3/providers/mailchimp#options "Direct link to heading")

**Mailchimp Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Mailchimp Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/mailchimp.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/mailchimp#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Mailchimp({
        clientId: process.env.MAILCHIMP_CLIENT_ID,
        clientSecret: process.env.MAILCHIMP_CLIENT_SECRET
      })
    ]
    ...

```
