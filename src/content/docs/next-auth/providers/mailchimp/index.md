---
title: "Mailchimp"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/mailchimp

# Mailchimp | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/mailchimp#documentation "제목으로 직접 연결되는 링크")

<https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/>

## 구성[​](https://next-auth.js.org/providers/mailchimp#configuration "제목으로 직접 연결되는 링크")

<https://admin.mailchimp.com/account/oauth2/client/>

## 옵션[​](https://next-auth.js.org/providers/mailchimp#options "제목으로 직접 연결되는 링크")

**Mailchimp Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Mailchimp Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/mailchimp.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/mailchimp#example "제목으로 직접 연결되는 링크")

```
    import MailchimpProvider from "next-auth/providers/mailchimp";
    ...
    providers: [
      MailchimpProvider({
        clientId: process.env.MAILCHIMP_CLIENT_ID,
        clientSecret: process.env.MAILCHIMP_CLIENT_SECRET
      })
    ]
    ...

```
