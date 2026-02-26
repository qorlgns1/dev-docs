---
title: "42 School"
description: "The 42 School Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/42-school

# 42 School | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/42-school#documentation "Direct link to heading")

<https://api.intra.42.fr/apidoc/guides/web_application_flow>

## Configuration[​](https://next-auth.js.org/v3/providers/42-school#configuration "Direct link to heading")

<https://profile.intra.42.fr/oauth/applications/new>

## Options[​](https://next-auth.js.org/v3/providers/42-school#options "Direct link to heading")

The **42 School Provider** comes with a set of default options:

- [42 School Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/42.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/42-school#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.FortyTwo({
        clientId: process.env.FORTY_TWO_CLIENT_ID,
        clientSecret: process.env.FORTY_TWO_CLIENT_SECRET
      })
    ]
    ...

```
