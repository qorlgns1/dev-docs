---
title: "Mail.ru"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/mailru

# Mail.ru | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/mailru#documentation "제목으로 직접 연결")

<https://o2.mail.ru/docs>

## 구성[​](https://next-auth.js.org/v3/providers/mailru#configuration "제목으로 직접 연결")

<https://o2.mail.ru/app/>

## 옵션[​](https://next-auth.js.org/v3/providers/mailru#options "제목으로 직접 연결")

**Mail.ru Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Mail.ru Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/mailru.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/mailru#example "제목으로 직접 연결")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.MailRu({
        clientId: process.env.MAILRU_CLIENT_ID,
        clientSecret: process.env.MAILRU_CLIENT_SECRET
      })
    ]
    ...

```
