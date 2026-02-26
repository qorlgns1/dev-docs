---
title: "Naver"
description: "The Naver Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/naver

# Naver | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/naver#documentation "Direct link to heading")

<https://developers.naver.com/docs/login/overview/overview.md>

## Configuration[​](https://next-auth.js.org/v3/providers/naver#configuration "Direct link to heading")

<https://developers.naver.com/docs/login/api/api.md>

## Options[​](https://next-auth.js.org/v3/providers/naver#options "Direct link to heading")

The **Naver Provider** comes with a set of default options:

- [Naver Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/naver.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/naver#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Naver({
        clientId: process.env.NAVER_CLIENT_ID,
        clientSecret: process.env.NAVER_CLIENT_SECRET
      })
    ]
    ...

```
