---
title: "Facebook"
description: "The Facebook Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/facebook

# Facebook | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/facebook#documentation "Direct link to heading")

<https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/>

## Configuration[​](https://next-auth.js.org/v3/providers/facebook#configuration "Direct link to heading")

<https://developers.facebook.com/apps/>

## Options[​](https://next-auth.js.org/v3/providers/facebook#options "Direct link to heading")

The **Facebook Provider** comes with a set of default options:

- [Facebook Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/facebook.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/facebook#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Facebook({
        clientId: process.env.FACEBOOK_CLIENT_ID,
        clientSecret: process.env.FACEBOOK_CLIENT_SECRET
      })
    ]
    ...

```

tip

Production applications cannot use localhost URLs to sign in with Facebook. You need to use a dedicated development application in Facebook to use **localhost** callback URLs.

tip

Email address may not be returned for accounts created on mobile.
