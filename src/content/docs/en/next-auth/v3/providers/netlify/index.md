---
title: "Netlify"
description: "The Netlify Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/netlify

# Netlify | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/netlify#documentation "Direct link to heading")

<https://www.netlify.com/blog/2016/10/10/integrating-with-netlify-oauth2/>

## Configuration[​](https://next-auth.js.org/v3/providers/netlify#configuration "Direct link to heading")

<https://github.com/netlify/netlify-oauth-example>

## Options[​](https://next-auth.js.org/v3/providers/netlify#options "Direct link to heading")

The **Netlify Provider** comes with a set of default options:

- [Netlify Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/netlify.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/netlify#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Netlify({
        clientId: process.env.NETLIFY_CLIENT_ID,
        clientSecret: process.env.NETLIFY_CLIENT_SECRET
      })
    ]
    ...

```
