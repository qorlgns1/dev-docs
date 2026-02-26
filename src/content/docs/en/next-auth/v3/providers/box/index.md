---
title: 'Documentation[​](https://next-auth.js.org/v3/providers/box#documentation "Direct link to heading")'
description: "The Box Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/v3/providers/box

# Box | NextAuth.js

Version: v3

## Documentation[​](https://next-auth.js.org/v3/providers/box#documentation "Direct link to heading")

<https://developer.box.com/reference/>

## Configuration[​](https://next-auth.js.org/v3/providers/box#configuration "Direct link to heading")

<https://developer.box.com/guides/sso-identities-and-app-users/connect-okta-to-app-users/configure-box/>

## Options[​](https://next-auth.js.org/v3/providers/box#options "Direct link to heading")

The **Box Provider** comes with a set of default options:

- [Box Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/box.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/v3/providers/box#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Box({
        clientId: process.env.BOX_CLIENT_ID,
        clientSecret: process.env.BOX_CLIENT_SECRET
      })
    ]
    ...

```
