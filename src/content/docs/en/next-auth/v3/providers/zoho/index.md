---
title: "Zoho"
description: "The Zoho Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/zoho

# Zoho | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/zoho#documentation "Direct link to heading")

<https://www.zoho.com/accounts/protocol/oauth/web-server-applications.html>

## Configuration[​](https://next-auth.js.org/v3/providers/zoho#configuration "Direct link to heading")

<https://api-console.zoho.com/>

## Options[​](https://next-auth.js.org/v3/providers/zoho#options "Direct link to heading")

The **Zoho Provider** comes with a set of default options:

- [Zoho Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/zoho.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/zoho#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Zoho({
        clientId: process.env.ZOHO_CLIENT_ID,
        clientSecret: process.env.ZOHO_CLIENT_SECRET
      })
    ]
    ...

```
