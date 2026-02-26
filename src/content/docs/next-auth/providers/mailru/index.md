---
title: "Mail.ru"
description: "사용 사례에 맞게 옵션을 원하는 대로 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/mailru

# Mail.ru | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/mailru#documentation "Direct link to heading")

<https://o2.mail.ru/docs>

## 구성[​](https://next-auth.js.org/providers/mailru#configuration "Direct link to heading")

<https://o2.mail.ru/app/>

## 옵션[​](https://next-auth.js.org/providers/mailru#options "Direct link to heading")

**Mail.ru Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Mail.ru Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/mailru.js)

사용 사례에 맞게 옵션을 원하는 대로 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/mailru#example "Direct link to heading")

```
    import MailRuProvider from "next-auth/providers/mailru";
    ...
    providers: [
      MailRuProvider({
        clientId: process.env.MAILRU_CLIENT_ID,
        clientSecret: process.env.MAILRU_CLIENT_SECRET
      })
    ]
    ...

```
