---
title: "Patreon"
description: "Create a API v2 client on Patreon Platform"
---

Source URL: https://next-auth.js.org/providers/patreon

# Patreon | NextAuth.js

Version: v4

## Documentation[​](https://next-auth.js.org/providers/patreon#documentation "Direct link to heading")

<https://docs.patreon.com/#apiv2-oauth>

## Configuration[​](https://next-auth.js.org/providers/patreon#configuration "Direct link to heading")

tip

Create a API v2 client on [Patreon Platform](https://www.patreon.com/portal/registration/register-clients)

## Options[​](https://next-auth.js.org/providers/patreon#options "Direct link to heading")

The **Patreon Provider** comes with a set of default options:

- [Patreon Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/patreon.ts)

You can override any of the options to suit your own use case.

## Example[​](https://next-auth.js.org/providers/patreon#example "Direct link to heading")

```
    import PatreonProvider from "next-auth/providers/patreon";
    ...
    providers: [
        PatreonProvider({
          clientId: process.env.PATREON_ID,
          clientSecret: process.env.PATREON_SECRET,
        })
    ]
    ...

```

note

Make sure you use the scopes defined in [ApiV2](https://docs.patreon.com/#scopes)
