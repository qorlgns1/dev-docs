---
title: "OneLogin"
description: "The OneLogin Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/onelogin

# OneLogin | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/onelogin#documentation "Direct link to heading")

<https://developers.onelogin.com/openid-connect>

## Configuration[​](https://next-auth.js.org/providers/onelogin#configuration "Direct link to heading")

<https://developers.onelogin.com/openid-connect/connect-to-onelogin>

## Options[​](https://next-auth.js.org/providers/onelogin#options "Direct link to heading")

The **OneLogin Provider** comes with a set of default options:

- [OneLogin Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/onelogin.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/onelogin#example "Direct link to heading")

```
    import OneLoginProvider from "next-auth/providers/onelogin";
    ...
    providers: [
      OneLoginProvider({
        clientId: process.env.ONELOGIN_CLIENT_ID,
        clientSecret: process.env.ONELOGIN_CLIENT_SECRET,
        issuer: process.env.ONELOGIN_ISSUER
      })
    ]
    ...

```
