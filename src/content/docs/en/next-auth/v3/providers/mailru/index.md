---
title: "Mail.ru"
description: "The Mail.ru Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/mailru

# Mail.ru | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/mailru#documentation "Direct link to heading")

<https://o2.mail.ru/docs>

## Configuration[​](https://next-auth.js.org/v3/providers/mailru#configuration "Direct link to heading")

<https://o2.mail.ru/app/>

## Options[​](https://next-auth.js.org/v3/providers/mailru#options "Direct link to heading")

The **Mail.ru Provider** comes with a set of default options:

- [Mail.ru Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/mailru.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/mailru#example "Direct link to heading")

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
