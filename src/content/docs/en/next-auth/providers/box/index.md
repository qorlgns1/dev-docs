---
title: 'Documentation[​](https://next-auth.js.org/providers/box#documentation "Direct link to heading")'
description: "The Box Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/box

# Box | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/box#documentation "Direct link to heading")

<https://developer.box.com/reference/>

## Configuration[​](https://next-auth.js.org/providers/box#configuration "Direct link to heading")

<https://developer.box.com/guides/sso-identities-and-app-users/connect-okta-to-app-users/configure-box/>

## Options[​](https://next-auth.js.org/providers/box#options "Direct link to heading")

The **Box Provider** comes with a set of default options:

- [Box Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/box.js)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/box#example "Direct link to heading")

```
    import BoxProvider from "next-auth/providers/box";
    ...
    providers: [
      BoxProvider({
        clientId: process.env.BOX_CLIENT_ID,
        clientSecret: process.env.BOX_CLIENT_SECRET
      })
    ]
    ...

```
