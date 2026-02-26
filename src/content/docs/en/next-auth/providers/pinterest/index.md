---
title: "Pinterest"
description: "The Pinterest Provider comes with a set of default options:"
---

Source URL: https://next-auth.js.org/providers/pinterest

# Pinterest | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/pinterest#documentation "Direct link to heading")

<https://developers.pinterest.com/docs/getting-started/authentication/>

## Configuration[​](https://next-auth.js.org/providers/pinterest#configuration "Direct link to heading")

<https://developers.pinterest.com/apps/>

## Options[​](https://next-auth.js.org/providers/pinterest#options "Direct link to heading")

The **Pinterest Provider** comes with a set of default options:

- [Pinterest Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/pinterest.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/pinterest#example "Direct link to heading")

```
    import PinterestProvider from "next-auth/providers/pinterest"
    ...
    providers: [
      PinterestProvider({
        clientId: process.env.PINTEREST_ID,
        clientSecret: process.env.PINTEREST_SECRET
      })
    ]
    ...

    :::tip
    To use in production, make sure the app has standard API access and not trial access
    :::

```
